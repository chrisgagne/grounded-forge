# Live build with the factory check (2026-10-14)

Factory `f597ef2` on the sample app: spec, triage, tests, build, triage and gate run live (review not run, to keep Codex use light). The Claude build leg's shell could run only the factory check.

## Ledger outcomes and build events

| Event | Stage | Check | Status | Note |
|---|---|---|---|---|
| e005 | spec | outcome | pass |  |
| e008 | triage | outcome | pass |  |
| e016 | tests | outcome | pass |  |
| e017 | build | start | info |  |
| e018 | build | check-command | info |  |
| e019 | build | leg:build | pass | $0.21 |
| e020 | build | builder-summary | info | the builder's own account: asserted, not evidence |
| e021 | build | commit | info |  |
| e022 | build | outcome | pass |  |
| e025 | triage | outcome | pass |  |
| e047 | gate | outcome | pass |  |

## The build leg's tool calls

- Read: `brief.md`
- Grep: `tag`
- Read: `routes.js`
- Grep: `validateNoteInput|Not A Tag|toLowerCase|trim`
- Edit: `routes.js`
- Bash: `check typecheck`
- Bash: `check test`

## What the check printed first (each Bash call)

- factory check: scans passed on 2 changed file(s); running typecheck: npm run typecheck
- factory check: scans passed on 2 changed file(s); running test: npm test

Guard blocks: 0.

Seen in this run and fixed after it: semgrep tried to reach semgrep.dev:443 (most likely its version check; the sandbox blocked it and the scan still completed; the check now passes `--disable-version-check`, not yet re-run live); the scans covered the locked acceptance tests as well as the leg's edit (they now start from the commit the build began at); `perf` wasn't offered (every configured gate command but `install` now is).
