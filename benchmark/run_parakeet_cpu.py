#!/usr/bin/env python3
"""
Voxmelt benchmark - Parakeet-on-CPU runner (standalone).

This runs the method behind the CPU numbers published at voxmelt.com/benchmark
on YOUR clips and machine, with no part of Voxmelt installed. It is a faithful
standalone copy of the decode path the shipping app uses: same model, same
quantization, same execution provider, same thread caps, same session-edge
silence pads. Those parameters are listed in DECODE PARAMETERS below so you
can check them against any claim we make.

USAGE
-----
    pip install -r requirements.txt
    python run_parakeet_cpu.py
    python wer.py transcripts/

The first run downloads the model (~670 MB) from Hugging Face. Everything
after that is offline.

DECODE PARAMETERS (identical to the shipping engine)
----------------------------------------------------
    model             nemo-parakeet-tdt-0.6b-v3
    quantization      int8
    provider          CPUExecutionProvider  (the GPU is never touched)
    intra_op threads  min(cpu_count, 6)
    inter_op threads  1
    audio             mono float32 @ 16 kHz
    session-edge pad  0.5 s of silence on each true session edge

Why the pads: TDT greedy decode drops a word whose audio is cut flush at the
array edge, which is exactly what a real dictation session produces (the mic
opens after you have started talking; the stop click clips the final word).
Half a second of quiet context lets the encoder resolve those edge words.
A whole benchmark clip has two true edges, so both ends are padded here.

HONESTY RULES (same as every other runner in this kit)
-----------------------------------------------------
  - The model is fully loaded BEFORE timing starts; load time is reported
    separately rather than hidden inside the transcription time.
  - Audio duration comes from the WAV header; processing time comes from a
    monotonic clock around the decode only.
  - The transcript written to disk is exactly what is scored. Nothing is
    hand-corrected between transcription and scoring.
"""

import glob
import os
import platform
import time
import wave

import numpy as np

SAMPLE_RATE = 16000
BOUNDARY_PAD_SEC = 0.5
MODEL_ID = "nemo-parakeet-tdt-0.6b-v3"
ENGINE_LABEL = "voxmelt-parakeet"

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPS_DIR = os.path.join(HERE, "clips")
TRANSCRIPTS_DIR = os.path.join(HERE, "transcripts")
SPEED_CSV = os.path.join(HERE, "results-speed-yourmachine.csv")


def read_wav_16k(path):
    """WAV -> mono float32 at 16 kHz. Matches the harness that produced our published numbers."""
    with wave.open(path) as w:
        sr = w.getframerate()
        ch = w.getnchannels()
        frames = np.frombuffer(
            w.readframes(w.getnframes()), dtype=np.int16
        ).astype(np.float32) / 32768.0
    if ch > 1:
        frames = frames.reshape(-1, ch).mean(axis=1)
    if sr != SAMPLE_RATE:
        x_old = np.linspace(0.0, 1.0, len(frames))
        x_new = np.linspace(0.0, 1.0, int(len(frames) * SAMPLE_RATE / sr))
        frames = np.interp(x_new, x_old, frames).astype(np.float32)
    return frames


def load_model():
    """Load Parakeet exactly as the shipping engine loads it on a CPU machine."""
    import onnx_asr
    import onnxruntime

    sess_options = onnxruntime.SessionOptions()
    sess_options.intra_op_num_threads = min(os.cpu_count() or 4, 6)
    sess_options.inter_op_num_threads = 1

    return onnx_asr.load_model(
        MODEL_ID,
        quantization="int8",
        providers=["CPUExecutionProvider"],
        sess_options=sess_options,
    )


def environment_block(load_sec):
    try:
        import onnxruntime
        ort_ver = onnxruntime.__version__
    except Exception:
        ort_ver = "unknown"
    return f"""
CPU:                 {platform.processor() or platform.machine()}
Logical cores:       {os.cpu_count()}
Threads used:        {min(os.cpu_count() or 4, 6)} intra-op, 1 inter-op
OS:                  {platform.system()} {platform.release()}
Python:              {platform.python_version()}
onnxruntime:         {ort_ver}
Model:               {MODEL_ID} (int8 ONNX)
Execution provider:  CPUExecutionProvider (GPU untouched)
Model load:          {load_sec:.1f} s
Peak VRAM:           0.0 GB
""".strip()


def main():
    clips = sorted(glob.glob(os.path.join(CLIPS_DIR, "*.wav")))
    if not clips:
        raise SystemExit(f"No clips found in {CLIPS_DIR}")
    os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)

    print(f"Loading {MODEL_ID} (int8, CPU). First run downloads ~670 MB...")
    t0 = time.monotonic()
    model = load_model()
    load_sec = time.monotonic() - t0
    print(f"Loaded in {load_sec:.1f}s\n")

    pad = np.zeros(int(BOUNDARY_PAD_SEC * SAMPLE_RATE), dtype=np.float32)
    rows = []
    total_audio = 0.0
    total_proc = 0.0

    for path in clips:
        name = os.path.splitext(os.path.basename(path))[0]
        wave_data = read_wav_16k(path)
        audio_sec = len(wave_data) / SAMPLE_RATE

        # Both ends of a benchmark clip are true session edges.
        padded = np.concatenate([pad, wave_data, pad])

        t0 = time.monotonic()
        text = model.recognize(padded, sample_rate=SAMPLE_RATE) or ""
        proc_sec = time.monotonic() - t0

        out = os.path.join(TRANSCRIPTS_DIR, f"{name}.{ENGINE_LABEL}.txt")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(text.strip() + "\n")

        rtf = proc_sec / audio_sec if audio_sec else 0.0
        times_rt = (1.0 / rtf) if rtf else 0.0
        rows.append((name, audio_sec, proc_sec, rtf, times_rt))
        total_audio += audio_sec
        total_proc += proc_sec
        print(f"{name:14s} {audio_sec:6.1f}s audio  {proc_sec:6.2f}s decode  {times_rt:5.1f}x realtime")

    print("\n" + environment_block(load_sec))

    overall = (total_audio / total_proc) if total_proc else 0.0
    print(f"\nOverall: {total_audio:.1f}s of audio in {total_proc:.1f}s = {overall:.1f}x realtime")

    with open(SPEED_CSV, "w", encoding="utf-8", newline="") as fh:
        fh.write("clip,audio_seconds,engine,processing_seconds,rtf,times_realtime,peak_vram_gb\n")
        for name, audio_sec, proc_sec, rtf, times_rt in rows:
            fh.write(f"{name},{audio_sec:.2f},{ENGINE_LABEL},{proc_sec:.2f},{rtf:.4f},{times_rt:.2f},0.0\n")
    print(f"Wrote {SPEED_CSV}")
    print("\nNow score accuracy:  python wer.py transcripts/")


if __name__ == "__main__":
    main()
