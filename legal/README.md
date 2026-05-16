# Blah2Text legal documents

This folder contains the three documents Blah2Text users agree to when
they install or sign up:

| File | Audience | Where it appears |
|---|---|---|
| [`EULA.md`](./EULA.md) | Anyone installing the desktop app | Installer (accept-to-install) + Settings → About → Legal |
| [`PRIVACY.md`](./PRIVACY.md) | Anyone using the app or website | Settings → About → Legal + portal footer |
| [`TERMS.md`](./TERMS.md) | Anyone with a Blah2Text account or paid plan | Settings → About → Legal + portal footer + first sign-up |

---

## ⚠️ Before going live with paying users

These documents are **drafted as professional starting templates with
placeholders the owner fills in**. They are NOT legal advice and have
NOT been reviewed by counsel. Before:

- You take any payment, or
- You let anyone outside your immediate team install the app, or
- You make Blah2Text publicly downloadable from a domain you own,

…have a lawyer in your jurisdiction review all three. Ask them to
specifically check:

1. The **governing law** clause matches your incorporation jurisdiction.
2. The **liability cap** is enforceable where your users live (some EU
   states cap how low you can cap; California has rules around
   consumer-software liability waivers).
3. The **subscription terms** match standard subscription disclosures (auto-renewal, cancellation rights, refund policy)
   (auto-renewal, cancellation rights, refund policy) — failure here
   is the #1 cause of chargebacks.
4. The **privacy policy** lists every data field you actually collect
   and is consistent with what the app does. If we add new telemetry
   later, this file gets updated.
5. The **EULA** "no reverse engineering" clause is enforceable where
   your users live (some EU states forbid blanket bans).

## Placeholders you must fill in

Every `[…]` bracket in the three documents is a placeholder. As of
this draft, the placeholders are:

- `Blah2Text` — legal entity name on file with our payment processor
- `` — address on incorporation papers
- `help@blah2text.com` — e.g. `support@blah2text.com`
- `help@blah2text.com` — can be the same; e.g. `privacy@blah2text.com`
- `India (Mumbai, Maharashtra)` — e.g. "the State of Delaware, United States" or
  "the courts of Mumbai, India". Match your incorporation.
- `[Subscription Price]` — fill in after pricing is locked in Phase 8
- `[Free Trial Days]` — if you offer one (default suggestion: 14)

A simple find-and-replace before publishing handles all of them.

## Versioning

Each document carries a version line at the top. Bump the version when
the document changes materially. The app stores the user's last-accepted
EULA version in localStorage as `blah2text_eula_accepted_v1`; bumping the
EULA version automatically re-prompts existing users on next launch.
