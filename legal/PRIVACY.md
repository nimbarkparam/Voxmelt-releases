# Voxmelt Privacy Policy

**Version:** 2.0
**Effective date:** 2 June 2026
**Applies to:** the Voxmelt desktop application for Windows and the Voxmelt
website at voxmelt.com.

---

## The short version

Voxmelt runs on your computer, not in our cloud. Your voice, your
transcripts, the text the AI cleans up, and the prompts you write **never
leave your machine and never reach us**. We literally cannot read them - we
built the app so that there's nothing on our end to read.

The only time anything touches the network is when *you* choose to: checking
for an app update, creating an optional account to manage a paid plan, or
paying for one. That's it. No telemetry, no analytics, no "anonymous" pings,
no selling data, no training AI on your voice. Ever.

The long version is below, because the law (and your trust) deserves the
detail.

---

## 1. Who we are

Voxmelt ("we", "us", "our") makes the Voxmelt desktop application. For the
limited account and billing data described in §4, we are the data
controller. You can reach us any time at **help@voxmelt.com**.

## 2. The core promise: your voice stays local

Voxmelt is **local-first by architecture, not just by policy.**

- **Audio capture** happens on your device. When you record, your microphone
  audio is held in your computer's memory and streamed to a transcription
  engine (Whisper, via `faster-whisper`) that runs **on your own GPU**.
- **Transcription** is produced locally. The text appears on your screen and
  goes to your clipboard or chosen output. It is never uploaded.
- **AI post-processing** (Studio tier) - cleaning up, summarising, rewriting,
  or re-toning your text - runs **entirely on your machine** through a local
  model served by Ollama. The prompt, the input text, and the AI's output
  never go to us or to any third party.
- **We receive none of it.** Not the audio, not the transcript, not the
  AI output, not the prompts or custom templates you write. There is no
  server-side copy because there is no server in the loop.

Audio lives in memory only while you're recording and is discarded when
processing finishes. A transcript or AI output is written to disk **only if
you save or export it**, and then it lives wherever you put it, on your
computer, under your control.

## 3. We collect no telemetry

To be unambiguous about what a lot of apps quietly do and we don't:

- **No usage analytics.** We do not track which features you use, how often
  you open the app, what you dictate, or anything else about your activity.
- **No crash reporting.** The app does not send crash dumps, stack traces, or
  diagnostic pings to us or any third party.
- **No content of any kind.** No audio, no transcripts, no AI inputs/outputs,
  no file names, no clipboard contents, no custom prompts.

You do not need an account to record, transcribe, or use AI post-processing.

## 4. The only data that ever leaves your machine

Three optional, narrowly-scoped flows, and nothing else:

### 4.1 App updates (anonymous)

The app periodically checks our **public releases feed** on GitHub
(`github.com/nimbarkparam/Voxmelt-releases`) to see if a newer version is
available, and downloads it if so. This is an ordinary file fetch. We do not
attach an identifier to it; what GitHub logs for any public download (e.g. an
IP address, briefly, for abuse prevention) is governed by
[GitHub's privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).
You can disable automatic updates in **Settings → About → Updates**.

### 4.2 Your account (optional - only to manage a paid plan)

You can use Voxmelt's free tier and trial with **no account at all**. An
account exists for one reason: to attach a paid (Pro/Studio) license to you.
If you create one, we store, in our database provider **Supabase**
(region: ap-south-1, Mumbai), under row-level security so that **only you can
read your own row**:

- Your **email address** - your account identifier and the address we use for
  service email (password resets, billing notices, important changes).
- Your **plan/license status** - which tier you're on and whether it's active.
- Basic **authentication metadata** managed by Supabase (sign-in tokens,
  last-seen timestamp).

### 4.3 Signing in with Google (optional)

If you create an account, you may sign in with email + password **or** with
"Continue with Google." If you choose Google:

- We request only the **basic sign-in scopes**: your **email address**, your
  **name**, and your **profile picture**. Nothing else.
- We request, receive, and store **no** other Google data. We access **no**
  Gmail, Drive, Calendar, Contacts, or any other restricted or sensitive
  Google scope.
- We use this data for **one purpose only**: to create and authenticate your
  Voxmelt account and link your license to you. We never use it for
  advertising or profiling, we never sell or rent it, we never use it to
  train any AI or machine-learning model, and we share it only with Supabase
  (our authentication/database processor acting on our behalf).
- **Voxmelt's use and transfer to any other app of information received from
  Google APIs will adhere to the
  [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy),
  including the Limited Use requirements.**
- Your Google profile data is stored in Supabase under row-level security so
  only you can read it. You can **revoke Voxmelt's access** at any time from
  the "Third-party apps & services" page of your Google Account, and request
  deletion of your account record at any time.

### 4.4 Billing (optional - only if you subscribe)

Payments are handled by **Razorpay**. We never see or store your full card
number. From Razorpay we receive only what's needed to operate your
subscription: a customer/subscription identifier, your subscription status
and renewal date, a country code (for tax), and (for display in your billing
page) the last four digits of your card. Razorpay's own
[privacy policy](https://razorpay.com/privacy/) governs the data it holds.

## 5. Voice, biometrics, and what we do *not* do with your audio

Because Voxmelt is a voice product, we want to be explicit:

- We do **not** create, extract, store, or transmit **voiceprints** or any
  other biometric identifier from your audio. Transcription converts speech
  to text on your device; no biometric template of your voice is generated by
  us or sent anywhere.
- If a future version offers **speaker labelling / diarization**, it runs
  locally on your machine like everything else, and any speaker data stays on
  your device.
- **Recording other people is your responsibility.** Laws in many places
  (for example, "all-party consent" wiretap statutes and biometric-privacy
  laws such as Illinois' BIPA) govern when and how you may record or process
  someone else's voice. Voxmelt gives you a local tool; you are responsible
  for having the consent and legal basis required where you are and where the
  people you record are. See the [Terms of Service](./TERMS.md) §4.

## 6. Why we use the little data we hold

| Purpose | Data used | Lawful basis (GDPR) |
|---|---|---|
| Run the app | Local data only - never leaves your device | N/A |
| Operate your account | Email, auth metadata | Contract |
| Authenticate Google sign-in | Google email, name, avatar | Contract / consent |
| Bill your subscription | Razorpay metadata | Contract |
| Send service email | Email | Legitimate interest |

We do not use your data for advertising, ad personalisation, profiling, AI
training, or sale to third parties. Ever.

## 7. Who we share data with

Only the processors below, only as needed to run the optional account/billing
features:

| Processor | What they get | Why |
|---|---|---|
| Supabase | Account email, plan status, Google profile basics | Authentication + database |
| Razorpay | Subscription/customer metadata | Payment processing |
| GitHub | Anonymous app-update fetches | Public release distribution |
| Google (if you use Google SSO) | The sign-in exchange itself | Authentication |

We will not share your data with anyone else without your consent, except
where strictly required by law (e.g. a valid court order).

## 8. Where data is stored and how long we keep it

| Data | Location | Retention |
|---|---|---|
| Everything you record/transcribe/generate | Your computer only | Until you delete it |
| Local app settings | Your computer (`%APPDATA%\app.voxmelt.desktop\`) | Until you uninstall |
| Account email + plan status | Supabase (ap-south-1, Mumbai) | While your account exists; deleted within 30 days of account deletion |
| Google profile basics | Supabase (ap-south-1, Mumbai) | Same as account; removed on deletion |
| Razorpay billing records | Razorpay | As required by tax/accounting law (typically up to 7 years) |

Where data must cross borders (e.g. our India-region database serving a user
elsewhere), we rely on appropriate safeguards such as Standard Contractual
Clauses where required.

## 9. Your rights

If you have an account, you can at any time:

- **Access / export** your account data - email **help@voxmelt.com**.
- **Correct** inaccurate data - Settings → Account, or email us.
- **Delete** your account and associated data - Settings → Account → Delete
  account (or email us). Cloud account data is removed within 30 days;
  Razorpay billing records may be retained where law requires.
- **Withdraw consent** for Google sign-in - revoke from your Google Account's
  "Third-party apps & services" page.
- **Object / restrict / port** - email **help@voxmelt.com**.
- **Complain** to your data-protection authority (e.g. the ICO in the UK, the
  CNIL in France, your State Attorney General in the US, the Data Protection
  Board in India).

If you don't have an account, only **local** data exists - delete it by
clearing your settings or uninstalling Voxmelt.

Region-specific rights apply and we honour them: **GDPR / UK GDPR** (EEA, UK,
Switzerland), the **CCPA/CPRA** (California - including the right to know,
delete, correct, and opt out of sale/sharing, which we do not do anyway), and
the **Digital Personal Data Protection Act 2023** (India).

## 10. Children

Voxmelt is not directed at children under 13 (or under 16 in the EU). We do
not knowingly collect data from children. If you believe a child has provided
us account data, email **help@voxmelt.com** and we'll delete it.

## 11. Security

The strongest privacy control here is structural: the sensitive stuff never
leaves your device, so there's no server for an attacker to breach. For the
limited account data we do hold, we use encryption in transit (TLS),
encryption at rest where the provider supports it, row-level security so users
can only read their own records, and least-privilege access. No system is
perfectly secure; if you suspect a problem with your account, email
**help@voxmelt.com** immediately. If we ever discover an incident affecting
your account data, we'll notify you and (where required) the relevant
authority within 72 hours.

## 12. Changes to this policy

We may update this policy. Material changes will be announced in the app
(Settings → About) and on this page, and the current version always lives at
[github.com/nimbarkparam/Voxmelt-releases/blob/main/legal/PRIVACY.md](https://github.com/nimbarkparam/Voxmelt-releases/blob/main/legal/PRIVACY.md).
If a change ever expands what data we collect, we'll say so plainly rather
than burying it.

## 13. Contact

Privacy questions, data-rights requests, or complaints:
**help@voxmelt.com**

Voxmelt
