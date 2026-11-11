# Voxmelt benchmark harness

**The measured figures below come from our own runs, written up in full in `RESULTS-2026-07-16.md`, and the accuracy figures were scored by the `wer.py` in this folder.** The Whisper runs used `run_whisper_gpu.py` under its old name, `run_voxmelt.py`; the Parakeet run used an earlier script that loaded the app's own engine, which is why the Parakeet runner here is a standalone copy. The runners, the scorer, the reference transcripts and the full environment block are here, so the method is open even though our own recordings are not.

Nothing from Voxmelt needs to be installed. `run_parakeet_cpu.py` is a standalone copy of the exact decode path the shipping app uses, with every parameter documented at the top of the file, so you can check it against anything we claim.

MIT licensed. Take it, run it on your own audio, and publish whatever you find.

---

## Quick start

```bash
cd benchmark
pip install -r requirements.txt

# Put 16-bit WAV files in clips/ and what was actually said in
# transcripts/<same-name>.ref.txt
python run_parakeet_cpu.py       # transcribes on your CPU
python wer.py transcripts/       # scores every transcript against the references
```

First run downloads the Parakeet model (about 670 MB) from Hugging Face. After that it is fully offline. Any sample rate and channel count works; the runner downmixes to mono and resamples to 16 kHz exactly as our run did.

The GPU side is optional and needs an NVIDIA card, `pip install faster-whisper`, and the CUDA 12 cuBLAS and cuDNN 9 libraries that [faster-whisper's README](https://github.com/SYSTRAN/faster-whisper) lists for GPU runs:

```bash
python run_whisper_gpu.py --model large-v3 --compute float16
python wer.py transcripts/
```

`wer.py` scores every `<name>.<engine>.txt` against the matching `<name>.ref.txt`, so both engines land in one `results.csv` once you have run both. Drop in a competitor's output as `<name>.whatever.txt` and it gets scored with identical normalization.

---

## What is in here

| Path | What |
|---|---|
| `run_parakeet_cpu.py` | CPU runner. Standalone, no Voxmelt install, GPU never touched. |
| `run_whisper_gpu.py` | Whisper/CUDA runner, mirroring the app's refined pass. |
| `wer.py` | The scorer. No dependencies. Same normalization for every engine. |
| `transcripts/*.ref.txt` | The reference text of our five clips - the scripts we read aloud. |
| `clips/` | Where your audio goes. Ours is not published; see `clips/README.md`. |
| `RESULTS-2026-07-16.md` | Our published run in full, with the environment block. |
| `requirements.txt` | Two packages for the CPU path. |

---

## What we measured, including where we lose

Ryzen 9 5900X, RTX 3080 Ti, five real recorded clips:

| Engine | Overall WER | Fast natural speech | Speed | Model load | VRAM |
|---|---|---|---|---|---|
| Whisper large-v3 (CUDA) | **7.8%** | 3.1% | 10-15x realtime | ~10 s warm | 4.2 GB |
| Parakeet TDT 0.6B v3 (CPU) | 11.9% | **2.0%** | 11-13x realtime | 4.4 s | **0.0 GB** |
| Whisper medium (CUDA) | 22.8% | 18.4% | 11-19x realtime | ~5 s warm | 2.3-2.4 GB |

**Whisper large-v3 on a GPU is the more accurate engine overall.** We publish that because it is true, and it is why large-v3 still ships in the app. What made Parakeet-on-CPU the shipping default anyway:

- It wins the **fast natural speech** clip, 2.0% against 3.1% - the clip that most resembles how people actually dictate, with filler.
- It uses **zero VRAM**, so the whole GPU stays free for the LLM that cleans the text up. On a 12 GB card that removes the evict-and-reload cycle entirely.
- Most of the remaining gap is **formatting, not mishearing**. Parakeet writes "58" and "$1800" where our reference scripts spell the numbers out, and the scorer counts each as an error. Character error rates are far closer: 7.3% against 6.1%.
- **On a machine with no NVIDIA card, the app's alternative is not large-v3.** It is a small Whisper model. Whisper medium scored 22.8% *with* a GPU; Parakeet scored 11.9% with none.

Its real weakness is rare vocabulary: it mangled "atorvastatin" in the medical clip. For dense jargon, switch to large-v3.

> **Correction, 2026-09-17.** Earlier versions of this table gave Whisper large-v3 a model
> load of "205 s" and Parakeet "3.9 s". Neither matches our own measured results, which
> are and always were in `RESULTS-2026-07-16.md`: large-v3 ~10 s warm, medium ~5 s warm,
> Parakeet 4.4 s. The figures above are now the measured ones. A benchmark that asks you
> to check its numbers has to hold its own summary to the same standard.

---

## How the scoring works, and why it is fair

Both the reference and the hypothesis go through the **same** normalization before a single error is counted:

- lowercased
- punctuation stripped
- whitespace collapsed
- for WER, number words turned into digits one word at a time, so "three" and "3" are not counted as a mismatch, but "fifty eight" scores as "50 8" and an engine that writes "58" is charged two errors

Applied identically to every engine. `wer.py` has no dependencies and is about 150 lines - read it rather than taking this paragraph's word for it.

The runners follow the same honesty rules:

- The model is fully loaded **before** timing starts; load time is reported separately rather than hidden inside the transcription time.
- Audio duration comes from the WAV header; processing time comes from a monotonic clock around the decode only.
- The transcript written to disk is exactly what gets scored. Nothing is hand-corrected in between.

---

## Known limits of this benchmark

Stated here rather than left for you to find:

- **Five clips is a small set.** It is real recorded speech rather than synthesized audio, which we consider the more useful trade, but it is not a statistically robust corpus.
- **The clips are one person's voice**, one accent, one microphone. Your mileage will differ, which is the entire reason this harness exists.
- **The references were written before recording**, so they are scripts read aloud rather than spontaneous speech. Even the fast clip's filler ("um", "like", "basically") is written into its script.
- **No cloud engine column.** Running one means uploading the clips, and we chose not to. The method supports it (`transcripts/NN.cloud-whisper.txt`) and the scorer treats any added engine identically.
- **It is first-party.** We ran it, on our hardware, on our voice. That is exactly why the code is in your hands.

---

## About Voxmelt

Voxmelt is local voice-to-text for Windows with an on-device AI text studio - dictation on your CPU, optional AI rewriting on your own GPU, nothing uploaded. [Features](../docs/FEATURES.md) · [voxmelt.com](https://voxmelt.com) · [Microsoft Store](https://apps.microsoft.com/detail/9PFCDCVKK1NQ)

The app itself is not open source. This harness is.
