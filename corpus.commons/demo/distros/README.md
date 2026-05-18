# distros/

Packaged release tarballs for the demo apps. Each tarball is one self-contained Claude Code project that a recipient can untar and run.

## Producing a tarball

```bash
npm run package decision           # one app
npm run package:all                # every built app
```

Each run writes `{app}-v{version}-{scope}.tar.gz` to this directory. Re-running overwrites the existing tarball at the same version.

## Filename convention

`{app}-v{version}-{scope}.tar.gz`. The `{scope}` segment is the most-restrictive scope across the bundled references. Levels (least → most restrictive):

| Scope | Meaning |
|---|---|
| open | Public, redistributable, no commercial restriction. |
| open-nc | Public, redistributable, non-commercial use only. |
| copyrighted | Single-organisation redistribution. |
| confidential | Single-organisation use; no further redistribution. |
| personal | Single-recipient use; not for sharing. |

The constraint travels with the artefact. A `decision-v0.2.1-personal.tar.gz` says to its recipient: *for your use only*. Renaming to strip the suffix is the recipient's choice and the recipient's risk.

## Safety gates

`npm run package` refuses to produce a tarball if any of the following are true:

- A secret-shaped file is present (`.env`, `credentials.json`, `*.pem`, `*.key`).
- An operator-only artefact is present (`_audit/`, `_planning/`, `_ingest_*`).
- A reference is missing its `**Scope:**` line, or carries a scope value that isn't in the taxonomy.

These are *build-state bugs*, not user choices. Scope mixing (e.g. an `open` and a `personal` reference in the same app) is not refused; it produces a `personal` tarball.

## What's inside

Each tarball contains the app's full self-contained folder plus a `LICENCE-MANIFEST.md` at the root listing every bundled reference with its individual scope and licence. The recipient can audit before opening.

## Recipient install

```bash
tar -xzf decision-v0.2.1-open-nc.tar.gz
cd decision
claude .
```
