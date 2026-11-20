# Voxmelt

**Private voice-to-text for any Windows PC, plus an on-device AI text studio.**

[![Get Voxmelt from the Microsoft Store](https://img.shields.io/badge/Microsoft%20Store-Download-0078D4?logo=microsoft&logoColor=white)](https://apps.microsoft.com/detail/9PFCDCVKK1NQ)
[![Website](https://img.shields.io/badge/voxmelt.com-Website-3b8bdb)](https://voxmelt.com)
[![Latest release](https://img.shields.io/github/v/release/nimbarkparam/Voxmelt-releases?label=latest)](https://github.com/nimbarkparam/Voxmelt-releases/releases/latest)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-lightgrey)](https://voxmelt.com/download)

Voxmelt turns speech into text on your own machine. Press a hotkey in any app and speak: the text
goes on your clipboard or is pasted where you are typing. Dictation runs on your CPU with NVIDIA's
Parakeet v3, so no graphics card is needed. With an NVIDIA GPU, a local model rewrites, summarises
or translates what you dictated in one click.

Your audio and text never leave the PC. It works with Wi-Fi off once the models are downloaded, and
there are no usage analytics or crash reports by default.

> **The name is Voxmelt** - vox + melt. If a search engine "corrected" your spelling on the way
> here, you are in the right place.

---

## Install

The current version is **1.20.0** ([release notes](https://github.com/nimbarkparam/Voxmelt-releases/releases/latest)).

**Recommended - Microsoft Store** (one click, no SmartScreen warning, Store-managed updates):

**https://apps.microsoft.com/detail/9PFCDCVKK1NQ**

**Direct installer** (same app, with a built-in auto-updater; not code-signed yet, so Windows shows
a SmartScreen prompt on first run):

**https://github.com/nimbarkparam/Voxmelt-releases/releases/latest/download/Voxmelt-Setup.exe**

The installer is about 5 MB and the app about 12 MB on disk. On first run Voxmelt downloads its
speech engine and model, about 840 MB (roughly 1.0 GB on disk), then works offline.

Every install starts with a **15-day full trial, no card**.

---

## What it does

| | |
|---|---|
| **CPU dictation** | NVIDIA Parakeet TDT 0.6B v3 (int8) transcribes on your CPU, 11 to 13x realtime on the benchmark PC, ready about 4 seconds after launch. English plus 24 European languages. |
| **Whisper engine** | Whisper ships in the same app for about 100 languages: tiny on the CPU, every size up to Large v3 Turbo on an NVIDIA GPU. The best pick for dense jargon. |
| **AI text studio** | One click hands your transcript to a local model through [Ollama](https://ollama.com): rewrite, proofread, summarise, translate, restyle. 17 templates, 80+ tones, 6 personas. Needs an NVIDIA GPU. |
| **Compose** | Paste any text and reshape it without recording anything. A private, local alternative to pasting into a cloud chatbot. |
| **Voiceover** | On-device read-aloud in up to 32 voice combinations (4 voice personas across 8 tones). Runs on the CPU. All 32 voices and WAV export come with Pro and Studio. |
| **Mini Mode** | An always-on-top pill. Dictate from it and the text is pasted at your cursor. |
| **Hands-free** | Rebindable global hotkeys plus voice commands (start, stop, copy, paste, switch template), so the pipeline runs without the keyboard. |
| **Custom vocabulary** | Teach it the names and terms it keeps mishearing: 25 on Pro, up to 500 on Studio. |
| **History** | A sessions library with a save mode you control, including one that writes nothing to disk at all. |

**[Every feature in full, section by section](./docs/FEATURES.md)** - engines, templates,
voiceover, hands-free operation, privacy, requirements, plans, and an honest list of what Voxmelt
does not do.

---

## The benchmark, stated honestly

Five scripted real-world clips, references written **before** recording, the same scorer for every
engine, every raw output published. Full method and the per-clip tables:
**https://voxmelt.com/benchmark**

**The harness that produced these numbers is in this repo, MIT licensed:
[`benchmark/`](./benchmark/).** Runners, scorer, reference transcripts and the environment block.
Nothing from Voxmelt needs to be installed: run it on your own audio and publish whatever you find.
The app itself is not open source; only the harness is.

| Engine | Overall WER | Fast natural speech | Character error rate | Peak VRAM |
|---|---|---|---|---|
| Whisper large-v3 (GPU) | **7.8%** | 3.1% | **6.1%** | 4.2 GB |
| **Parakeet v3 (CPU only)** | 11.9% | **2.0%** | 7.3% | **0** |
| Whisper medium (GPU) | 22.8% | 18.4% | 16.7% | 2.3 GB |

Measured on a Ryzen 9 5900X (12 cores) with an RTX 3080 Ti 12 GB, Windows 11.

Read that table properly, because the headline number is not the interesting one:

- Whisper large-v3 on a GPU **wins overall**, and that is exactly why it still ships in the app.
- On **fast natural speech with filler**, the clip most like how people actually dictate, Parakeet
  on a CPU beats it, 2.0% against 3.1%, and it loads in about 4 seconds with no VRAM.
- Most of the overall gap is formatting, not mishearing: Parakeet writes numbers as digits where the
  reference scripts spell them out, and the strict scorer counts each one as an error. Character
  error rate is nearly level: 7.3% against 6.1%.
- The comparison that decided the default: on a PC with no NVIDIA card, the alternative is not
  large-v3 (it needs CUDA), it is a small Whisper model. Whisper medium scored 22.8% **with** a GPU.

Its one real weak spot in this set is rare drug names in the medical clip. If you dictate dense
jargon, switch to Whisper.

---

## Verifying the privacy claim

This is the part you should not take on trust:

1. Open any network monitor (Windows Resource Monitor works).
2. Dictate a few sentences in Voxmelt.
3. Watch the traffic. You will see licence checks (which carry a salted hash of your machine ID),
   update checks on the direct-download build, and model downloads. No audio, no transcripts.

Or simpler: turn off your network and keep dictating. It keeps working.

Audio sits in memory while you record and is discarded when processing ends. Full policy:
https://voxmelt.com/privacy

---

## Requirements

- Windows 10 (build 19041+) or Windows 11, 64-bit
- Any modern 4-core x64 CPU, 8 GB RAM (16 GB recommended), about 1.0 GB free disk for the speech
  engine and model
- A microphone
- **Optional:** an NVIDIA GPU with 6 GB+ VRAM plus Ollama for the AI text studio (driver 525 or
  newer, 570 or newer on Blackwell cards), and the one-time GPU add-on (about 1.3 GB) for Whisper
  above Tiny

No macOS, no Linux, no mobile, no web version.

---

## Pricing

| Plan | Price | What it adds |
|---|---|---|
| Free | $0 | A 15-day full trial, no card, then 60 minutes of dictation a day, a daily AI taste and 10 minutes a day of read-aloud. Mini Mode closes after 5 idle minutes. No custom vocabulary |
| Pro | **$49 once** | Unlimited dictation, Mini Mode stays open, 25 vocabulary terms and 25 corrections, unlimited AI on the everyday templates, all 32 voices with WAV export, mid-size models, 5 custom templates. Up to 3 PCs you own |
| Studio | **$99 once** | Everything in Pro, plus up to 500 vocabulary terms, uncapped corrections, no device cap, the AI Prompt and Code packs, every model including the flagships, 30 custom templates and a direct line to the maker |

**Pay once, owned forever.** No subscription, no renewal date, nothing to cancel. In India, Rs 3,999
and Rs 7,999. Plans and the full FAQ: https://voxmelt.com/pricing

---

## About this repository

This repo is the **public mirror**. It exists so the auto-updater in every installed copy of
Voxmelt can fetch its manifest anonymously, so the installer has a stable public download URL, and
so the documentation and benchmark method are readable without visiting a marketing site. The
application source is private.

| Folder | What |
|---|---|
| [`benchmark/`](./benchmark/) | The benchmark harness, MIT licensed. Runners, scorer, reference transcripts, the full published run. |
| [`docs/`](./docs/) | Complete feature reference. |
| [`legal/`](./legal/) | EULA, privacy policy, terms and refund policy, synced from the source repo. |

Each tagged release publishes:

| Asset | Purpose |
|---|---|
| `Voxmelt-Setup.exe` | Versionless installer link, always the newest build |
| `Voxmelt_<version>_x64-setup.exe` | Versioned Windows installer |
| `Voxmelt_<version>_x64-setup.exe.sig` | Minisign signature, verified by the running app |
| `latest.json` | Updater manifest, pointing at this repo's release assets |
| `voxmelt-stt-x64.zip` / `voxmelt-tts-x64.zip` | Frozen speech and voice engines, fetched on first run |

Releases are cut by CI in the private source repo on every `v*` tag: a Windows runner builds and
signs the bundle, generates `latest.json`, and publishes here. No release asset is ever uploaded by
hand; `docs/` and `benchmark/` are maintained here directly, and `legal/` is synced automatically.

**Support and bug reports:** help@voxmelt.com
**Press, reviews and partnerships:** ela@voxmelt.com

---

## Links

- Website: **https://voxmelt.com**
- Microsoft Store: **https://apps.microsoft.com/detail/9PFCDCVKK1NQ**
- Download page: https://voxmelt.com/download
- Benchmark and method: **https://voxmelt.com/benchmark** (harness: [`benchmark/`](./benchmark/))
- Every feature in full: [`docs/FEATURES.md`](./docs/FEATURES.md)
- Who it is for: https://voxmelt.com/use-cases
- Comparison with other dictation tools: https://voxmelt.com/compare
- Changelog: https://voxmelt.com/changelog
- About: https://voxmelt.com/about

Guides:

- Offline dictation on Windows: https://voxmelt.com/offline-dictation-windows
- Dictation without a graphics card: https://voxmelt.com/dictation-without-gpu
- Dictating prompts to AI agents: https://voxmelt.com/dictate-to-ai-agents

Built by the Voxmelt team. Independent, and not affiliated with NVIDIA, Microsoft, OpenAI or
Ollama: those names appear here only to describe the models and platforms Voxmelt runs on.
