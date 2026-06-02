# Voxmelt End-User License Agreement

**Version:** 2.0
**Effective date:** 2 June 2026
**Applies to:** the Voxmelt desktop application for Microsoft Windows.

---

## The short version

This is the agreement for installing and using the Voxmelt app on your own
computer. The gist:

- You get a license to **use** Voxmelt, you don't **own** it.
- Voxmelt turns your speech into text and (on Studio) cleans it up with a
  local AI. **AI isn't perfect** - transcripts and rewrites can be wrong, so
  read what comes out before you rely on it.
- Voxmelt stands on the shoulders of **open-source models** (Whisper, plus
  whatever you run through Ollama). Those keep their own licenses; using them
  is on you.
- You need the **right hardware** (an NVIDIA GPU). Speed and accuracy depend
  on it, and we can't promise any specific result on your machine.
- Don't use Voxmelt for illegal things or in life-or-death systems.

The enforceable detail is below.

---

By installing, copying, or otherwise using Voxmelt ("the Software"), you
("you") agree to this End-User License Agreement ("EULA"). If you don't
agree, don't install or use the Software.

## 1. License grant

Voxmelt ("we", "us", "our") grants you a limited, non-exclusive,
non-transferable, revocable license to install and use one copy of the
Software on each personal computer or device you own or control, for your
personal or internal business use, subject to this EULA and to the tier you're
on (Free, Pro, or Studio). Paid tiers carry additional rights described in the
[Terms of Service](./TERMS.md).

## 2. What the Software does (and what it relies on)

Voxmelt records audio from your microphone and transcribes it to text using a
local speech-to-text engine running on your GPU. On the Studio tier it can
also post-process that text - clean it up, summarise it, reformat it, or
change its tone - using a local large-language model served by Ollama, driven
by built-in or custom "AI templates."

All of this runs **on your device**. To work, the Software depends on
third-party open-source components, covered in §6.

## 3. Restrictions

You may not, and may not let others:

1. Copy, modify, adapt, translate, or create derivative works of the Software,
   except where applicable law expressly permits and that right can't be
   waived by contract.
2. Reverse-engineer, decompile, or disassemble the Software, except to the
   minimum extent the law requires (e.g. interoperability under EU Directive
   2009/24/EC).
3. Remove or alter any proprietary notices or marks.
4. Sublicense, rent, lease, lend, sell, or redistribute the Software or any
   part of it.
5. Circumvent, disable, or tamper with licensing, tier limits, trial-anchor,
   or entitlement checks.
6. Use the Software for anything illegal where you are or where the activity
   has effect - including recording or processing someone's voice without the
   consent or legal basis the law requires (see [Terms](./TERMS.md) §4).
7. Use the Software to operate life-safety, real-time medical, aviation,
   nuclear, or other systems where a failure could cause death, personal
   injury, or environmental damage.

## 4. AI output: accuracy, variability, and your responsibility

This is the most important section to actually read.

**Speech-to-text is probabilistic, not exact.** The transcription engine
predicts the most likely words from your audio. It will sometimes get words
wrong, drop words, add words, or - especially during silence, background
noise, music, or non-speech audio - **"hallucinate" text that was never
spoken.** This is a known characteristic of modern speech models, including
the Whisper family Voxmelt uses.

**Results vary with how, and what, you speak.** Accuracy is affected by your
accent, dialect, speaking pace, tone, clarity, the language and any
code-switching, specialised vocabulary, names, jargon, microphone quality, and
ambient noise. Two people saying the same words, or the same person on a
different day, can get different transcripts.

**AI post-processing changes your text on purpose.** Cleanup, summarising,
rewriting, and tone-shifting are generative operations. The model may alter
meaning, drop nuance, introduce facts that weren't there, "correct" something
that was actually right, or produce output that doesn't match your intent.
Custom templates and prompts you write can amplify this.

**Hardware shapes the result.** Which Whisper model size and which AI model
you can run, how fast they run, and sometimes how accurate they are, depend on
your GPU, its VRAM, drivers, and system load. We don't warrant any particular
speed, latency, accuracy, or quality on your hardware.

**Because of all of the above, you are responsible for reviewing and
verifying any transcript or AI output before you rely on, send, publish, or
act on it.** Voxmelt output is a draft and an assistive tool - **it is not
professional advice** and is not a substitute for legal, medical, financial,
or other expert judgment. Do not use it as the sole basis for any decision
that carries legal, financial, health, or safety consequences without
independent human review. You decide what to do with the output, and you own
the consequences of that decision.

## 5. Your content

You keep **all** rights to what you create with the Software - your audio,
your transcripts, the AI output, and any custom templates or prompts. We claim
no ownership of any of it, and because the Software runs locally, we don't
receive it in the first place (see the [Privacy Policy](./PRIVACY.md)). What
you produce, and how you use it, is yours and your responsibility.

## 6. Third-party open-source components

Voxmelt is built on, and downloads on your behalf, third-party open-source
software and models, each under **its own license**:

- The **Whisper** speech-to-text family and the `faster-whisper`/CTranslate2
  runtime;
- **Ollama**, the local model runtime; and
- the **AI models you choose to download and run** through it - for example
  Llama (Meta's community license), Gemma (Google's terms), Qwen, Mistral, and
  others.

We grant you no rights in these components beyond what their own licenses
give you, and we make no warranties about them. **You are responsible for
reviewing and complying with the license of each model you download and use**,
including any restrictions on commercial use or acceptable use. The Software
helps you fetch these components for convenience; their authors, not us, are
responsible for them.

## 7. Updates

The Software includes an automatic-update mechanism that periodically checks
the public releases feed and installs new versions. By using the Software you
consent to receiving updates, which may add, change, or remove features. An
update may include a new version of this EULA; continuing to use the Software
after an update constitutes acceptance of the updated EULA. You may disable
automatic updates in **Settings → About → Updates**, but you remain
responsible for the security and correctness of any out-of-date version you
keep running.

## 8. Ownership

The Software is **licensed, not sold.** We retain all right, title, and
interest in the Software and its intellectual property. This EULA grants you
no rights to our trademarks or branding beyond what's needed to lawfully use
the Software.

## 9. Disclaimer of warranties

THE SOFTWARE IS PROVIDED "AS IS" AND "AS AVAILABLE", WITHOUT WARRANTY OF ANY
KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, AND
FREEDOM FROM DEFECTS. WE DO NOT WARRANT THAT THE SOFTWARE WILL BE
UNINTERRUPTED, ERROR-FREE, OR SECURE, OR THAT ANY TRANSCRIPT OR AI OUTPUT WILL
BE ACCURATE, COMPLETE, OR FIT FOR YOUR PURPOSE. YOU USE THE SOFTWARE, AND RELY
ON ITS OUTPUT, AT YOUR OWN RISK.

Some jurisdictions don't allow the exclusion of certain warranties, so some of
the above may not apply to you.

## 10. Limitation of liability

TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT WILL VOXMELT BE
LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE
DAMAGES, OR ANY LOSS OF PROFITS, REVENUES, DATA, OR USE, OR FOR ANY LOSS
ARISING FROM INACCURATE OR UNEXPECTED TRANSCRIPTION OR AI OUTPUT, ARISING OUT
OF OR RELATED TO YOUR USE OF THE SOFTWARE, WHETHER IN CONTRACT, TORT, OR ANY
OTHER THEORY, EVEN IF WE HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

OUR TOTAL CUMULATIVE LIABILITY ARISING OUT OF OR RELATED TO THIS EULA WILL NOT
EXCEED THE GREATER OF (a) THE AMOUNT YOU PAID US IN THE TWELVE MONTHS BEFORE
THE EVENT GIVING RISE TO THE CLAIM, OR (b) US $50.

Some jurisdictions don't allow these limitations, so some may not apply to
you. If you're a consumer in a jurisdiction with stronger protections (such as
the EU), those protections apply to the extent the law requires.

## 11. Termination

This EULA is effective until terminated. We may terminate it on written notice
if you breach it; on termination you must stop using and uninstall all copies
of the Software. You may terminate at any time by uninstalling the Software.
Sections 5, 6, 8, 9, 10, and 12 survive termination.

## 12. Governing law

This EULA is governed by the laws of India (Mumbai, Maharashtra), without
regard to conflict-of-laws principles. Disputes will be brought exclusively in
the courts of Mumbai, Maharashtra, India, and you consent to their personal
jurisdiction. If you're a consumer in the EU, you may also bring disputes in
the courts of your country of residence under EU consumer-protection law.

## 13. Changes

We may update this EULA. Material changes trigger a re-acceptance prompt the
next time you launch the Software; continued use after the prompt is
acceptance. The current version always lives at
[github.com/nimbarkparam/Voxmelt-releases/blob/main/legal/EULA.md](https://github.com/nimbarkparam/Voxmelt-releases/blob/main/legal/EULA.md).

## 14. Contact

Questions about this EULA: **help@voxmelt.com**

Voxmelt
