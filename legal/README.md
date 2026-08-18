# Voxmelt legal documents

This folder is the **source of truth** for the legal documents Voxmelt users
agree to when they install or subscribe. `sync-legal.yml` mirrors this folder
to the public `Voxmelt-releases` repo on every change, so the in-app "Legal"
links and the portal always point at the current text without shipping a new
binary.

| File | Audience | Where it appears |
|---|---|---|
| [`EULA.md`](./EULA.md) | Anyone installing the desktop app | Installer (accept-to-install) + Settings → About → Legal |
| [`PRIVACY.md`](./PRIVACY.md) | Anyone using the app or website | Settings → About → Legal + portal `/privacy` |
| [`TERMS.md`](./TERMS.md) | Anyone with an account or paid plan | Settings → About → Legal + portal `/privacy#terms` + first sign-up |
| [`REFUND.md`](./REFUND.md) | Anyone on a paid plan | Portal `/privacy#refund` + billing flow |

These mirror the combined legal page the portal serves at
`voxmelt.com/privacy` (Privacy + EULA + Terms + Refund as sections), which is
also the URL submitted for Google OAuth verification. **Keep the two in sync**,
and never water down the Google "Limited Use" disclosures in the Privacy
Policy - Google's reviewers look for them verbatim.

## What these documents now cover

As of v2.0 (2 June 2026) these were rewritten to describe **Voxmelt as it
actually is** - a local voice-to-text app with optional on-device AI
post-processing. (Earlier drafts were adapted from a different product's
templates and referenced features Voxmelt doesn't have.) They now address the
risks specific to this product:

- **Local-first privacy** - audio, transcripts, AI output, and prompts never
  leave the device; **no telemetry, no crash pings, no analytics**. This is a
  binding promise, so keep the app's behaviour matching it: if telemetry is
  ever added, the Privacy Policy must be updated *first*.
- **AI accuracy** - transcripts and AI rewrites can be wrong, can hallucinate,
  and vary by accent/tone/language/wording and by hardware; the user is
  responsible for reviewing output, and it's explicitly **not professional
  advice**. (EULA §4, Terms §4.)
- **Third-party open-source models** - Whisper, Ollama, and the models the user
  pulls (Llama, Gemma, Qwen, Mistral, …) keep their own licenses; the user is
  responsible for complying with each. (EULA §6.)
- **Recording consent** - the user is responsible for consent under wiretap and
  biometric-privacy laws (e.g. BIPA); we create/store no voiceprints. (Privacy
  §5, Terms §4.)
- **Purchases** - one-time payment, perpetual licence, nothing to cancel,
  30-day price-change notice, 15-day no-card trial, no-refund-after-cycle with
  an outage exception and a statutory-rights carve-out.

## ⚠️ Still get a lawyer before scaling paid users

These are professional starting templates aligned to the product, **not legal
advice, and not reviewed by counsel.** Before you take payment at scale or go
broadly public, have a lawyer in your jurisdiction review all four and check:

1. The **governing law** clause (India / Mumbai) matches your incorporation.
2. The **liability cap** is enforceable where your users live (some EU states
   and California restrict how low you can cap consumer-software liability).
3. The **one-time purchase disclosures** meet the rules where you sell
   (e.g. US state ARL laws + the FTC negative-option rule, EU consumer law).
   Billing disclosures that do not match what is actually charged are the #1
   cause of chargebacks.
4. The **privacy policy** lists exactly what you collect and matches what the
   app does (today: nothing but optional account + billing data).
5. The **AI-output and recording-consent disclaimers** are sufficient for your
   target markets, especially if you sell into regulated users (legal/medical).

## Versioning

Each document carries a version line. Bump it on material change. The app
stores the user's last-accepted EULA version; bumping the EULA version
re-prompts existing users on next launch. The portal section's "Last updated"
date should be bumped to match when the corresponding doc changes.
