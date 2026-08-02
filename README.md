# Voxmelt

**Private voice-to-text for any Windows PC, plus an on-device AI text studio.**

[![Get Voxmelt from the Microsoft Store](https://img.shields.io/badge/Microsoft%20Store-Download-0078D4?logo=microsoft&logoColor=white)](https://apps.microsoft.com/detail/9PFCDCVKK1NQ)
[![Website](https://img.shields.io/badge/voxmelt.com-Website-3b8bdb)](https://voxmelt.com)
[![Latest release](https://img.shields.io/github/v/release/nimbarkparam/Voxmelt-releases?label=latest)](https://github.com/nimbarkparam/Voxmelt-releases/releases/latest)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-lightgrey)](https://voxmelt.com/download)

Voxmelt turns speech into finished text on your own machine. Press a hotkey, talk, and
NVIDIA's Parakeet v3 model transcribes you in real time **on your CPU** - no graphics
card required. If you do have an NVIDIA GPU, it stays free for the part that actually
benefits from it: a local LLM that rewrites, summarizes, or translates your words in one
click.

Nothing is uploaded. Not the audio, not the transcript, not a usage counter tied to your
words. The only network calls Voxmelt makes are model download, licensing, and update
checks - and you can confirm that yourself with any network monitor in about sixty
seconds.

> **The name is Voxmelt** - vox + melt. If a search engine "corrected" your spelling on
> the way here, you are in the right place.

---

## Install

**Recommended - Microsoft Store** (one click, no SmartScreen warning, Store-managed updates):

**https://apps.microsoft.com/detail/9PFCDCVKK1NQ**

**Direct installer** (same app, built-in auto-updater, currently unsigned so Windows will
show a SmartScreen prompt on first run):

**https://github.com/nimbarkparam/Voxmelt-releases/releases/latest/download/Voxmelt-Setup.exe**

The installer is around 12 MB. Speech models download once on first run and then work
offline forever.

---

## What it does

| | |
|---|---|
| **CPU dictation** | NVIDIA Parakeet TDT 0.6B v3 (int8 ONNX) transcribes on ordinary CPU cores at roughly 12x realtime. Ready about 4 seconds after launch. English plus 24 European languages. |
| **Whisper engine** | Switch to OpenAI Whisper (tiny through large-v3, CPU or CUDA) for around 100 languages and the best accuracy on dense jargon. Both engines ship in the app. |
| **AI text studio** | One click hands your transcript to a local model via [Ollama](https://ollama.com): rewrite, proofread, summarize, translate, restyle. 17 templates, 80+ tones, 6 personas. Needs an NVIDIA GPU. |
| **Compose** | Paste any text and reshape it without recording anything. A private local alternative to pasting into a cloud chatbot. |
| **Voiceover** | Local text-to-speech, 4 personas x 8 tones = 32 voice combinations, WAV export. Runs on CPU. |
| **Mini Mode** | An always-on-top pill you can drop anywhere. Dictate straight into whatever app has focus; polished text lands at your cursor. |
| **Hands-free** | Rebindable global hotkeys plus voice commands (start, stop, copy, paste, switch template) so the pipeline runs without the keyboard. |

---

## The benchmark, stated honestly

Five real recorded clips, references written **before** recording, same scorer for every
engine, every raw output published. Full method and the per-clip tables:
**https://voxmelt.com/benchmark**

| Engine | Overall WER | Fast natural speech | Cold load | VRAM |
|---|---|---|---|---|
| Whisper large-v3 (RTX 3080 Ti) | **7.8%** | 3.1% | 205s | 4.2 GB |
| **Parakeet v3 (CPU only)** | 11.9% | **2.0%** | **3.9s** | **0** |
| Whisper medium (GPU) | 22.8% | 18.4% | 45s | 2.3 GB |

Read that table properly, because the headline number is not the interesting one:

- Whisper large-v3 on a GPU **wins overall**, and that is exactly why it still ships in
  the app. We are not going to pretend otherwise on our own benchmark page.
- On **fast natural speech with filler** - the clip that most resembles how people
  actually dictate - Parakeet on a CPU beats it, 2.0% against 3.1%.
- Most of the overall gap is formatting, not mishearing. Parakeet writes "58" and
  "$1800" where our reference scripts spell the numbers out, and the scorer counts every
  one of those as an error. Character error rate is nearly level: 7.3% against 6.1%.
- The comparison that decided the default: on a machine with no NVIDIA card, the
  alternative is not large-v3 (it needs CUDA), it is a small Whisper model. Whisper
  medium scored 22.8% **with** a GPU. Parakeet scores 11.9% with none, in four seconds,
  using no VRAM.

Its real weakness is rare vocabulary. It mangled "atorvastatin" in the medical clip. If
you dictate dense jargon, switch to large-v3.

---

## Verifying the privacy claim

This is the part you should not take on trust:

1. Open any network monitor (Windows Resource Monitor works).
2. Dictate a few sentences in Voxmelt.
3. Watch the traffic. Model download happens once; after that you will see licensing and
   update checks and nothing else. No audio, no transcripts.

Or simpler: turn off your network and keep dictating. It keeps working.

---

## Requirements

- Windows 10 (build 19041+) or Windows 11, 64-bit
- Any modern 4-core CPU, 8 GB RAM, ~2 GB free disk
- A microphone
- **Optional, for the AI text studio only:** NVIDIA GPU with 6 GB+ VRAM, plus Ollama

No macOS, no Linux, no mobile, no web version.

---

## Pricing

Free tier is free forever: 60 minutes of dictation per day, plus a daily allowance of AI
cleanup runs. No card required. Every install also starts with a 15-day full trial of
everything.

Paid plans are subscriptions: **Pro $9.99/month**, **Studio $14.99/month**. Managed at
[voxmelt.com](https://voxmelt.com/pricing).

---

## About this repository

This repo is the **public release mirror**. It exists so the auto-updater in every
installed copy of Voxmelt can fetch its manifest anonymously, and so the installer has a
stable public download URL. The application source is private.

Each tagged release publishes:

| Asset | Purpose |
|---|---|
| `Voxmelt-Setup.exe` | Versionless installer link, always the newest build |
| `Voxmelt_<version>_x64-setup.exe` | Versioned Windows installer |
| `Voxmelt_<version>_x64-setup.exe.sig` | Minisign signature, verified by the running app |
| `latest.json` | Updater manifest, pointing at this repo's release assets |
| `voxmelt-stt-x64.zip` / `voxmelt-tts-x64.zip` | Frozen speech and voice engines, fetched on first run |

Releases are cut by CI in the private source repo on every `v*` tag: a Windows runner
builds and signs the bundle, generates `latest.json`, and publishes here. Nobody commits
to this repo by hand.

The [`legal/`](./legal/) folder mirrors the EULA, privacy policy, terms, and refund
policy that the app and website link to. It is synced automatically from the source repo.

**Support and bug reports:** help@voxmelt.com

---

## Links

- Website: **https://voxmelt.com**
- Microsoft Store: **https://apps.microsoft.com/detail/9PFCDCVKK1NQ**
- Benchmark and method: **https://voxmelt.com/benchmark**
- Feature comparison vs other dictation tools: **https://voxmelt.com/compare**
- Changelog: **https://voxmelt.com/changelog**
- About and the story: **https://voxmelt.com/about**

Built by [Param Nimbark](https://voxmelt.com/about). Independent, and not affiliated with
NVIDIA, Microsoft, or OpenAI - those names appear here only to describe the models and
platforms Voxmelt runs on.
