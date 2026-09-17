# Voxmelt features, in full

Voxmelt is **local voice-to-text for Windows with an on-device AI text studio**. Speech recognition runs on your CPU, optional AI rewriting runs on your own NVIDIA GPU, and nothing you say or write is uploaded anywhere.

This document is the complete feature reference. It is the public mirror of what is on [voxmelt.com](https://voxmelt.com), kept here so the information is readable without visiting a marketing site, and so it stays available even if the site does not.

**Platform: Windows 10 (build 19041+) and Windows 11, 64-bit. Nothing else** - no macOS, no Linux, no web version, no mobile app.

---

## Contents

- [Dictation: speech to text](#dictation-speech-to-text)
- [The AI text studio](#the-ai-text-studio)
- [Voiceover: text to speech](#voiceover-text-to-speech)
- [Working without the keyboard](#working-without-the-keyboard)
- [Your transcripts](#your-transcripts)
- [Interface](#interface)
- [Privacy and offline operation](#privacy-and-offline-operation)
- [System requirements](#system-requirements)
- [Pricing and tiers](#pricing-and-tiers)
- [What Voxmelt does not do](#what-voxmelt-does-not-do)

---

## Dictation: speech to text

### Dictation that runs on your CPU, with no graphics card

NVIDIA's **Parakeet TDT 0.6B v3** transcribes in real time on ordinary CPU cores, at roughly **12x realtime**, ready about **4 seconds** after launch. No graphics card is involved and it uses **zero VRAM**, which means two things: Voxmelt runs on any modern Windows laptop, and on a machine that does have a GPU, the card stays entirely free for other work.

This is the default engine and the whole product rather than a trial mode. Coverage is **English plus 24 European languages**.

### The Whisper engine, when you need it

OpenAI's **Whisper** ships in the same app, from `tiny` through `large-v3`, on either CPU or CUDA. Switch to it for **around 100 languages**, or for the best accuracy on dense jargon and noisy audio. One toggle on the Models page; no separate download step or second install.

On our published benchmark, Whisper large-v3 on a GPU is the more accurate engine overall at 7.8% word error rate against Parakeet's 11.9%. We say so plainly because it is true. [The full numbers, including the clips where our default loses](https://voxmelt.com/benchmark), and [the harness to reproduce them yourself](../benchmark/).

### The orchestrator: two engines, one machine

Most dictation tools pick one processor and stay there. Voxmelt splits the work: speech recognition on your CPU cores, and your NVIDIA GPU left free for the local language model that rewrites the text. On a 12 GB card, that removes the evict-and-reload cycle between the speech model and the language model entirely.

Prefer the other arrangement? All-GPU mode puts Whisper back on CUDA, and Voxmelt manages the VRAM swap for you, with live telemetry, colour-coded fit indicators, and a one-click Free GPU control for when you want to game or render.

### Custom vocabulary (Pro and Studio)

Teach the transcriber the names and jargon it keeps mangling, and it corrects them automatically **on either engine**. It rejoins names that get split apart - "Box melt" becomes "Voxmelt" - and lets you map an exact mis-hearing when a name is too far off for safe matching.

Deliberately conservative, so it never rewrites a word you actually said. The transcript header shows what was corrected, with one click to see the original.

### Unlimited continuous dictation

There is no per-session length limit and no per-minute meter. Long-form dictation runs in overlapping chunks with automatic de-duplication at the seams, and chunk duration is tunable (5 / 15 / 30 / 60 seconds).

### Idle auto-stop

A recording you walk away from ends itself after 60 seconds with no human voice, using voice detection rather than raw loudness, so a noisy fan or an air conditioner cannot hold the session open. Configurable, and you can switch it off.

---

## The AI text studio

Optional, and it needs an NVIDIA GPU with 6 GB or more plus [Ollama](https://ollama.com). Without one, you still get unlimited local transcription - you paste the raw transcript instead of the polished version.

### 17 templates, 82 tones, 6 personas

One click hands your transcript to a language model running on your own machine: clean up the dictation, write the email, summarize to bullets, draft the commit message, translate it, restructure it, change the register.

The six personas are Voice Polisher, Ghostwriter, Info Distiller, Data Architect, Polyglot and Privacy Guard. Each template is a compiled prompt tuned specifically to hold its instructions on the small models that run locally, which is a different engineering problem from prompting a frontier model through an API.

[Browse every template and tone](https://voxmelt.com/presets).

### Compose: reshape text you did not dictate

Paste anything - a rough draft, a colleague's email, notes exported from another tool - pick a template and a tone, and a local model reshapes it. No microphone involved. It is a private, local alternative to pasting your work into a cloud chatbot.

### Custom templates

Write your own system prompt for work the built-in templates do not cover: medical notes, legal briefs, meeting minutes in a particular house format. Free tier gets 1 custom slot, Pro gets 5, Studio gets 30.

### Per-app tones in Mini Mode (Studio)

Bind an application to an AI template once, and anything you dictate into that app is styled automatically - conventional commit messages in your editor, plain prose in your browser. The app you are actually typing into is resolved by process, and unmapped apps fall back to your own default template rather than inheriting the last one used.

### Bring any Ollama model

22+ models in the catalog - Gemma, Qwen, DeepSeek-R1, Llama, Phi, Mistral - and anything else Ollama can serve. The orchestrator reads parameter counts from model tags and estimates VRAM automatically, so pulling a new model and having it work is the normal case rather than a configuration exercise.

Token-level streaming, cancel mid-run, and per-run tracking. Ollama is reached on `127.0.0.1:11434` and nowhere else.

---

## Voiceover: text to speech

Turn any script into narration without a recording booth. **Four voice personas across eight delivery tones - 32 combinations** - generated locally, with WAV export. Runs on the CPU, so it needs no graphics card, and there are no per-character cloud TTS fees because there is no cloud involved.

Also used for read-back: have Voxmelt read text aloud to you rather than the other way round.

---

## Working without the keyboard

### Mini Mode

Collapse Voxmelt into an always-on-top pill you can drop anywhere and snap to any screen edge. Dictate straight into whatever application has focus and the polished text lands at your cursor, with no window switch. Useful on a laptop panel, and on a second monitor.

### Global hotkeys

Rebindable OS-wide hotkeys trigger recording from inside any application. The defaults are chosen specifically not to steal a system-wide combination that Windows or another app already owns.

### Voice commands

A second always-on speech model listens in the background and fuzzy-matches spoken commands - start, stop, copy, paste, switch template - so the whole pipeline can run without touching the keyboard at all. Runs on your GPU if you have one and your CPU if you do not.

This matters most for the people for whom hands-free text entry is not a convenience: RSI, tremor, chronic pain, limited hand mobility, or simply hands that are busy with something else.

### Auto-paste

The finished text is on your clipboard, and with auto-paste enabled it lands directly at your cursor in whatever app you were in. There is no editor plugin to install and nothing to configure per application.

---

## Your transcripts

A single History library holds your sessions, with a save mode you control:

- **Off** - nothing is written to disk at all
- **Transcript only** - keeps what you said, not what the AI made of it
- **Transcript and AI output** - keeps both

Everything stays on your machine in every mode. The choice is about what Voxmelt keeps for *you*, not about what leaves.

---

## Interface

- **Five dark themes** - Nightwing, Matrix, Cyberpunk, Candy Red, Mono - matched to the website
- **Global UI zoom** from 50% to 200% via Ctrl and the scroll wheel, or Ctrl with `+` / `-` / `0`
- **"How Voxmelt works"** - a short animated explainer of the whole pipeline, on the title bar's eye button and on the first-run welcome step
- **Zero-terminal setup** - a first-run wizard installs and verifies everything, including Ollama and the models, with no command line at any point

---

## Privacy and offline operation

**Audio, transcripts, AI processing and voiceover all run on hardware you own.** The only network calls Voxmelt makes at all are the one-time model download, a licence check, and update checks. Never audio. Never transcripts.

This is architecture rather than policy. The speech engine is a sandboxed subprocess that talks JSON over stdio and has no network access by design. Ollama is bound to localhost. There is no telemetry, no analytics, and no usage counter tied to your words.

**Verify it in sixty seconds**, which is the only version of this claim worth making:

1. Open any network monitor - Windows Resource Monitor is enough.
2. Dictate a few sentences.
3. Watch the traffic.

Or more simply: unplug the network and keep working. After the one-time model download, Voxmelt behaves identically offline, which makes it usable on a plane, on a locked-down machine, on a hospital network, or in an air-gapped lab.

No account is required for the app to run.

---

## System requirements

**Minimum**

- Windows 10 build 19041 or later, or Windows 11, 64-bit
- Any modern 4-core CPU
- 8 GB RAM
- About 2 GB free disk space
- A microphone

**Optional, for the AI text studio only**

- NVIDIA GPU with 6 GB or more of VRAM
- [Ollama](https://ollama.com)

The installer is around 12 MB. The speech and voice engines download once on first run and then work offline permanently.

---

## Pricing and tiers

**One-time purchases, not subscriptions.** There is no renewal date, no recurring mandate, and nothing to cancel.

| Tier | Price | What you get |
|---|---|---|
| **Free** | Free forever | 60 minutes of dictation per day plus a daily allowance of AI cleanup runs. No card. |
| **Pro** | **$49 once** (₹3,999) | Unlimited local dictation, unlimited AI cleanup on the everyday templates, mid-size local models, all 32 voiceover voices with WAV export, custom vocabulary, 5 custom templates. |
| **Studio** | **$99 once** (₹7,999) | Everything in Pro, plus the AI Prompt and Code template packs, every model in the catalog including the flagships, per-app tones in Mini Mode, 30 custom templates. |

Every install begins with a **15-day full trial of Studio**, with no card required.

Current pricing is always at [voxmelt.com/pricing](https://voxmelt.com/pricing).

---

## What Voxmelt does not do

Stated here so you can rule it out quickly rather than discover it after installing:

- **Windows only.** No macOS, Linux, web or mobile version, and no date promised for one.
- **The AI text studio needs an NVIDIA GPU.** AMD and Intel graphics are not supported for that part. Dictation works on any CPU regardless.
- **It is not open source.** The models are open and [this benchmark harness](../benchmark/) is MIT licensed, but the application source is private.
- **There is no API and no CLI.** It is a desktop app with a global hotkey, not a service you script against. For a local transcription API, look at faster-whisper or whisper.cpp.
- **It is not a meeting recorder.** No calendar integration, no bot that joins your calls, no speaker diarization.
- **Rare vocabulary is the default engine's weak spot.** Custom vocabulary is the fix; for dense unfamiliar terminology, switch to Whisper large-v3.

---

## Links

- **Website:** [voxmelt.com](https://voxmelt.com)
- **Microsoft Store:** [apps.microsoft.com/detail/9PFCDCVKK1NQ](https://apps.microsoft.com/detail/9PFCDCVKK1NQ)
- **Benchmark and method:** [voxmelt.com/benchmark](https://voxmelt.com/benchmark) · [harness in this repo](../benchmark/)
- **Every template and tone:** [voxmelt.com/presets](https://voxmelt.com/presets)
- **Compared with other dictation tools:** [voxmelt.com/compare](https://voxmelt.com/compare)
- **Who it is for:** [voxmelt.com/use-cases](https://voxmelt.com/use-cases)
- **Changelog:** [voxmelt.com/changelog](https://voxmelt.com/changelog)
- **Support:** help@voxmelt.com

Built by [Param Nimbark](https://voxmelt.com/about). Independent, and not affiliated with NVIDIA, Microsoft, OpenAI or Ollama - those names appear here only to describe the models and platforms Voxmelt runs on.
