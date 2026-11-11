#!/usr/bin/env python3
"""
VoxMelt benchmark runner - the local (VoxMelt) side of the benchmark.

For every clips/NN_name.wav this script:
  1. Transcribes it with faster-whisper using THE SAME parameter stack as
     the shipping engine's authoritative refined pass (engine.py
     _get_transcribe_params: beam 5, temperature fallback ladder, the
     compression-ratio / log-prob / no-speech quality gates, VAD tuned the
     same way). Benchmarking anything else would not be benchmarking the
     product.
  2. Writes transcripts/NN_name.voxmelt-<model>.txt for wer.py to score.
  3. Measures wall-clock processing time, RTF, and peak GPU VRAM during the
     run (nvidia-smi polled on a background thread), appending one row per
     clip to results-speed.csv.
  4. Prints the environment block for RESULTS.md with real values.

USAGE
-----
    python run_whisper_gpu.py                 # large-v3 fp16 (the headline run)
    python run_whisper_gpu.py --model medium  # the "8 GB card" story
    python run_whisper_gpu.py --model large-v3 --compute int8_float16

Then score accuracy:
    python wer.py transcripts/

Honesty notes baked in:
  - The model is loaded BEFORE timing starts. Cold-start model load is
    reported separately, never folded into per-clip RTF (cloud APIs do not
    bill you for their server boot either).
  - Audio duration comes from the wav header, processing time from a
    monotonic clock around the full transcribe+decode loop.
  - The transcript written is the post-quality-gate text, exactly what the
    app's refined pass would deliver to the user.
"""

import argparse
import datetime as _dt
import os
import platform
import re
import subprocess
import sys
import threading
import time
import wave

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPS = os.path.join(HERE, "clips")
TRANSCRIPTS = os.path.join(HERE, "transcripts")
SPEED_CSV = os.path.join(HERE, "results-speed.csv")


def wav_duration_sec(path: str) -> float:
    with wave.open(path, "rb") as w:
        return w.getnframes() / float(w.getframerate())


# ── Peak-VRAM sampler ────────────────────────────────────────────────────────
# Global memory.used on the card before the model loads. On Windows the WDDM
# driver blocks per-process VRAM queries, so the honest fallback is the DELTA
# of global usage over this baseline - which isolates the benchmark's own
# footprint as long as the machine is otherwise quiet (close games/browsers
# before running; the guide says so). Per-PID readings are preferred when the
# driver provides them (Linux / TCC mode).
_BASELINE_MB = 0


def _global_used_mb() -> int:
    try:
        out = subprocess.run(
            ["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=5,
            creationflags=0x08000000 if os.name == "nt" else 0,
        )
        return int(out.stdout.strip().splitlines()[0])
    except Exception:
        return 0


class VramPeak:
    """Polls nvidia-smi every 250 ms on a daemon thread; .peak_gb holds the max
    of (per-PID reading when available, global delta over the pre-load baseline)."""

    def __init__(self):
        self.pid_peak_mb = 0
        self.global_peak_mb = 0
        self._pid = os.getpid()
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._loop, daemon=True)

    def _sample(self):
        try:
            out = subprocess.run(
                ["nvidia-smi", "--query-compute-apps=pid,used_memory", "--format=csv,noheader,nounits"],
                capture_output=True, text=True, timeout=5,
                creationflags=0x08000000 if os.name == "nt" else 0,
            )
            for line in out.stdout.strip().splitlines():
                parts = [p.strip() for p in line.split(",")]
                if len(parts) >= 2 and parts[0].isdigit() and int(parts[0]) == self._pid:
                    self.pid_peak_mb = max(self.pid_peak_mb, int(parts[1]))
        except Exception:
            pass
        self.global_peak_mb = max(self.global_peak_mb, _global_used_mb())

    def _loop(self):
        while not self._stop.is_set():
            self._sample()
            self._stop.wait(0.25)

    def __enter__(self):
        self._sample()
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join(timeout=2)
        self._sample()

    @property
    def peak_gb(self) -> float:
        if self.pid_peak_mb > 0:
            return round(self.pid_peak_mb / 1024, 1)
        delta = max(0, self.global_peak_mb - _BASELINE_MB)
        return round(delta / 1024, 1)


# ── The engine's refined-pass parameters (mirror of engine.py) ───────────────
def refined_pass_params() -> dict:
    return dict(
        language="en",  # benchmark clips are English; the app supports auto-detect
        beam_size=5,
        best_of=5,
        temperature=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
        compression_ratio_threshold=2.4,
        log_prob_threshold=-1.0,
        no_speech_threshold=0.6,
        condition_on_previous_text=True,
        repetition_penalty=1.2,
        no_repeat_ngram_size=3,
        vad_filter=True,
        hallucination_silence_threshold=2.0,
        vad_parameters=dict(
            min_silence_duration_ms=600,
            speech_pad_ms=400,
            threshold=0.3,
        ),
    )


def environment_block(model_size: str, compute_type: str, load_sec: float) -> str:
    import faster_whisper
    import ctranslate2

    gpu_name, vram_total, driver = "unknown", "?", "?"
    cuda = "?"
    try:
        out = subprocess.run(
            ["nvidia-smi", "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"],
            capture_output=True, text=True, timeout=5,
            creationflags=0x08000000 if os.name == "nt" else 0,
        ).stdout.strip()
        gpu_name, vram_total, driver = [p.strip() for p in out.split(",")[:3]]
    except Exception:
        pass
    try:
        smi = subprocess.run(
            ["nvidia-smi"], capture_output=True, text=True, timeout=5,
            creationflags=0x08000000 if os.name == "nt" else 0,
        ).stdout
        m = re.search(r"CUDA Version:\s*([\d.]+)", smi)
        if m:
            cuda = m.group(1)
    except Exception:
        pass

    return f"""
GPU:                 {gpu_name} ({vram_total})
NVIDIA driver:       {driver}
CUDA version:        {cuda}
OS:                  {platform.system()} {platform.release()} ({platform.version()})
Whisper model:       {model_size}
Compute type:        {compute_type}
faster-whisper ver:  {faster_whisper.__version__} (CTranslate2 {ctranslate2.__version__})
Model load time:     {load_sec:.1f}s (one-time, excluded from per-clip RTF)
Date:                {_dt.date.today().isoformat()}
References written:  before recording (ground truth = the script, not a post-hoc transcript)
""".strip()


def main():
    ap = argparse.ArgumentParser(description="Run the VoxMelt side of the benchmark.")
    ap.add_argument("--model", default="large-v3", help="Whisper model size (default large-v3)")
    ap.add_argument("--compute", default="float16", help="Compute type (default float16)")
    args = ap.parse_args()

    clips = sorted(
        f for f in os.listdir(CLIPS) if f.lower().endswith(".wav")
    ) if os.path.isdir(CLIPS) else []
    if not clips:
        print("No .wav files in clips/. Record the 5 clips first - see RECORDING_GUIDE.md.")
        sys.exit(1)

    from faster_whisper import WhisperModel

    engine_label = f"voxmelt-{'large' if args.model.startswith('large') else args.model}"
    global _BASELINE_MB
    _BASELINE_MB = _global_used_mb()
    print(f"GPU baseline before load: {_BASELINE_MB} MB used by other apps")
    print(f"Loading {args.model} ({args.compute}) on CUDA...")
    t0 = time.monotonic()
    model = WhisperModel(args.model, device="cuda", compute_type=args.compute)
    load_sec = time.monotonic() - t0
    print(f"Loaded in {load_sec:.1f}s.\n")

    params = refined_pass_params()
    rows = []
    for fn in clips:
        clip_id = os.path.splitext(fn)[0]
        path = os.path.join(CLIPS, fn)
        dur = wav_duration_sec(path)

        with VramPeak() as vram:
            t1 = time.monotonic()
            segments, _info = model.transcribe(path, **params)
            text = " ".join(s.text.strip() for s in segments).strip()
            elapsed = time.monotonic() - t1

        out_path = os.path.join(TRANSCRIPTS, f"{clip_id}.{engine_label}.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text + "\n")

        rtf = elapsed / dur if dur > 0 else 0.0
        x_rt = (1.0 / rtf) if rtf > 0 else 0.0
        rows.append(
            f"{clip_id},{dur:.1f},{args.model},{args.compute},"
            f"{elapsed:.2f},{rtf:.3f},{x_rt:.1f},{vram.peak_gb}"
        )
        print(f"{clip_id}: {dur:.1f}s audio -> {elapsed:.2f}s ({x_rt:.1f}x realtime, peak {vram.peak_gb} GB) -> {os.path.basename(out_path)}")

    # Append to the speed CSV (header created by the kit; recreate if missing).
    header = "clip,audio_seconds,model,compute_type,processing_seconds,rtf,times_realtime,peak_vram_gb"
    exists = os.path.isfile(SPEED_CSV)
    with open(SPEED_CSV, "a" if exists else "w", encoding="utf-8", newline="") as f:
        if not exists:
            f.write(header + "\n")
        f.write("\n".join(rows) + "\n")
    print(f"\nAppended {len(rows)} rows to results-speed.csv")

    print("\n-- Environment block (paste into RESULTS.md) --")
    print(environment_block(args.model, args.compute, load_sec))
    print("\nNext: python wer.py transcripts/")


if __name__ == "__main__":
    main()
