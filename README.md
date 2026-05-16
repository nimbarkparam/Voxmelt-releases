# Voxmelt-releases

Public auto-updater feed for **Voxmelt**, a local GPU-accelerated voice-to-text app with built-in AI cleanup. Built artifacts are mirrored here from the private source repo by GitHub Actions.

- **App source code** lives at [`nimbarkparam/Voxmelt`](https://github.com/nimbarkparam/Voxmelt) (private).
- **Marketing + account portal** lives at [`nimbarkparam/Voxmelt-web`](https://github.com/nimbarkparam/Voxmelt-web) (private).
- **This repo** is intentionally public so that the Tauri auto-updater on every installed copy of Voxmelt can fetch `latest.json` and the signed update payload anonymously.

## What's published here

Each tagged release attaches four assets:

| Asset | Purpose |
|---|---|
| `Voxmelt_<version>_x64-setup.exe`   | Windows NSIS installer (download this for a fresh install). |
| `Voxmelt_<version>_x64-setup.nsis.zip` | Updater payload consumed by Tauri's auto-updater. |
| `Voxmelt_<version>_x64-setup.nsis.zip.sig` | Minisign signature for the updater payload (verified by the running app). |
| `latest.json` | Updater manifest. URL fields point back at this repo's release-asset URLs. |

The Tauri updater on every Voxmelt install polls `latest.json` from this repo on each launch. When `latest.json` shows a newer `version`, the running app downloads the matching `.nsis.zip`, verifies the `.sig`, and installs the patch on next restart.

## How releases are cut

Releases are produced by a workflow in the private source repo. On every `v*` tag push:

1. Windows runner builds a signed Tauri installer + updater bundle.
2. `latest.json` is generated, with `url` fields pointing at this public mirror.
3. A release is created here using a PAT (`MIRROR_REPO_TOKEN`) with write access to this repo, attaching all four assets.

No one pushes commits here directly. All updates flow through the mirror workflow.

## What does **not** live here

- Source code (lives in [`nimbarkparam/Voxmelt`](https://github.com/nimbarkparam/Voxmelt)).
- Issue tracker (file issues against the source repo).
- Roadmap or design discussions.

## Legal

The [`legal/`](./legal/) folder contains the EULA, privacy policy, and terms of service the app and portal link to. Treat them as drafted templates - see [`legal/README.md`](./legal/README.md) for the placeholder list and the lawyer-review checklist before going live with paying users.

## Verifying a download

The installer is signed with a Microsoft Authenticode certificate (right-click the `.exe` -> Properties -> Digital Signatures). The auto-updater payload is signed with a minisign key whose public half is baked into the running app - there is no separate "trust on first use" step.

## License

The Voxmelt desktop binary is distributed under the EULA at [`legal/EULA.md`](./legal/EULA.md). The auto-updater feed infrastructure (this README, workflows mirroring artifacts here) is MIT.
