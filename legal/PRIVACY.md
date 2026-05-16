# Blah2Text Privacy Policy

**Version:** 1.0
**Effective date:** 12 May 2026
**Applies to:** the Blah2Text desktop application AND any future website
operated by Blah2Text at the blah2text.com domain.

---

We at Blah2Text ("we", "us", "our") respect your privacy. This
policy explains what data Blah2Text collects, why, where it is stored,
who it is shared with, and how to exercise your rights over it.

If anything here is unclear, email us at help@blah2text.com.

## 1. Who we are

Blah2Text

We are the data controller for the personal data described in this
policy.

## 2. What data we collect — and what we DON'T

### Data Blah2Text collects automatically — local only

When you use the Blah2Text desktop application, the following stays on
your computer and is **never transmitted** to us unless you opt in to
the features called out in §3 and §4:

- Your sequences (action graphs, names, settings).
- Your schedules (triggers, target sequences).
- Local preferences (theme, mini-mode position, master-password
  configuration, EULA acceptance flag).
- Local execution reports (which actions ran, when, success/failure).

This data lives in `%APPDATA%\app.blah2text.desktop\` on Windows.

### Data Blah2Text collects only with your active opt-in

#### Crash reports (default: ON, opt-out)

When the app crashes we send a report containing:
- App version, OS version, processor architecture.
- The action type that was executing when the crash occurred (e.g.
  "OpenApplication"), but **NOT** the action's properties (no paths,
  no commands, no typed text).
- The crash stack trace.

We use our crash-reporting provider for crash reports.

You can disable this in **Settings → Privacy → Send anonymous crash
reports**.

#### Anonymous usage analytics (default: OFF, opt-in)

If you turn this on, we collect anonymised events that help us
improve the product:
- App launch / quit.
- Sequence created / run.
- Schedule created (with trigger TYPE only — e.g. "hotkey" — NEVER
  the configuration like which chord or which app).
- Settings panel opened, feature used.
- Approximate time-zone (for scheduling-feature analysis).

We do NOT collect:
- Sequence names, sequence contents, or action parameters.
- File paths, folder paths, command-line strings.
- Hotkey chord values or watched file paths.
- Any text the user has typed inside the app.

We use our analytics provider for usage analytics.

You can enable / disable this in **Settings → Privacy → Help improve
Blah2Text**.

### Data Blah2Text collects when you create a Blah2Text account (Phase 7+)

If and when you choose to create a Blah2Text account (required only for
cloud sync and paid features):

- Email address — used as your account identifier and for
  service-related email (e.g. password resets, important notices).
- Authentication tokens — managed by our authentication provider
  (our authentication provider).
- Sign-in metadata — IP address (for fraud detection, retained 30
  days), device label, last-seen timestamp.

If you sign in with a third-party provider (Google), that provider
shares your email and basic profile (name, avatar URL) with us;
nothing more.

### Data we collect when you cloud-sync sequences (Phase 7+, opt-in)

Only when you turn on cloud sync, your sequences (names, action graphs,
schedules) are encrypted in transit (TLS) and stored in our database
hosted by our database provider (region: asia-south-1 (Mumbai)).

Encryption-at-rest is provided by the underlying database. End-to-end
encryption is on the roadmap.

### Data we collect when you subscribe (Phase 8+)

Payment processing is handled by our payment processor. We never see or store your
card number. From our payment processor we receive:

- Your our customer ID with our payment processor, subscription status, and renewal date.
- Country code (for tax purposes).
- The last 4 digits of your card (for display in the billing
  dashboard).

Our payment processor's own privacy policy applies to the data they hold.

## 3. Why we use this data

| Purpose | Data used | Lawful basis (GDPR) |
|---|---|---|
| Run the app | Local data only | N/A — never leaves device |
| Diagnose crashes | Crash reports (opt-out) | Legitimate interest |
| Improve the product | Usage analytics (opt-in) | Consent |
| Operate your account | Email, auth tokens | Contract |
| Sync your sequences | Sequence data (opt-in) | Contract |
| Bill your subscription | payment-processor metadata | Contract |
| Detect fraud / abuse | Sign-in IPs (30 days) | Legitimate interest |
| Send service emails | Email | Legitimate interest |

We do not use your data for advertising, ad personalisation, or
sale to third parties. Ever.

## 4. Who we share data with

We share data only with the processors listed below, only as needed
to operate the service:

| Processor | What they get | Where they're located | Why |
|---|---|---|---|
| Crash-reporting provider | Crash reports (opt-out) | EU (eu.sentry.io) | Crash diagnostics |
| Analytics provider | Anonymous usage events (opt-in) | EU (eu.posthog.com) | Product analytics |
| Auth + database provider | Account + cloud-synced sequences | asia-south-1 (Mumbai) | Auth + database |
| our payment processor | Customer ID, subscription state | Global | Payment processing |
| Update distribution provider | App update fetches (anonymous) | Global | Auto-update distribution |

We will not share your data with any other third party without your
consent, except where required by law (e.g. valid court order).

## 5. Where data is stored

Local app data: on your computer at
`%APPDATA%\app.blah2text.desktop\`.

Cloud-synced data: in the database provider region asia-south-1 (Mumbai) (set
before Phase 7 ships).

We do not transfer data to countries outside the storing region
without using appropriate safeguards (Standard Contractual Clauses
where required).

## 6. How long we keep data

| Data | Retention |
|---|---|
| Local app data | As long as the app is installed; deleted on uninstall |
| Crash reports | 90 days, then deleted |
| Usage analytics | 12 months, then aggregated and anonymised |
| Account data | As long as your account exists + 30 days after deletion |
| Sign-in IP addresses | 30 days |
| Cloud-synced sequences | Until you delete them or close the account |
| payment-processor billing records | As required by tax / accounting law (typically 7 years) |

## 7. Your rights

If you have a Blah2Text account, you can at any time:

- **Access** the data we hold about you — Settings → Privacy → Export
  my data, or email help@blah2text.com.
- **Correct** inaccurate data — Settings → Account, or email us.
- **Delete** your account and all associated data — Settings →
  Account → Delete account. All cloud data is removed within 30 days;
  payment-processor billing records may be retained for legal compliance.
- **Restrict or object** to processing — email help@blah2text.com.
- **Port** your data to another service — Settings → Privacy → Export
  my data produces a JSON file you can import elsewhere.
- **Withdraw consent** for analytics or crash reports — toggle them
  off in Settings → Privacy at any time.
- **Lodge a complaint** with your local data-protection authority
  (e.g. ICO in the UK, your state's Attorney General in the US, the
  CNIL in France).

If you do not have an account, only local data exists, and you can
delete it by uninstalling Blah2Text.

For users in the European Economic Area, the United Kingdom, and
Switzerland, your rights under the GDPR / UK GDPR apply.

For users in California, your rights under the CCPA / CPRA apply,
including the right to know, the right to delete, the right to
correct, and the right to opt out of the sale or sharing of personal
information (we do neither).

For users in India, your rights under the Digital Personal Data
Protection Act 2023 apply.

## 8. Children

Blah2Text is not directed at children under 13 (or under 16 in the EU).
We do not knowingly collect data from children. If you believe a
child has provided us data, email help@blah2text.com and we will delete
it.

## 9. Security

We use industry-standard measures to protect your data, including
encryption in transit (TLS), encryption at rest where supported by
the underlying provider, and least-privilege access controls. No
system is perfectly secure, however; if you suspect a breach of your
account, email help@blah2text.com immediately.

If we discover a security incident affecting your data, we will
notify you and (where required) your data-protection authority within
72 hours.

## 10. Changes to this policy

We may update this policy from time to time. Material changes will
be announced inside the app (Settings → About → Updates) and on this
page. The most current version is always available at
[github.com/nimbarkparam/Blah2Text-releases/blob/master/legal/PRIVACY.md](https://github.com/nimbarkparam/Blah2Text-releases/blob/main/legal/PRIVACY.md).

## 11. Contact

Privacy questions, data-rights requests, or complaints:
help@blah2text.com

Blah2Text
