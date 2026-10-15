# factory

A harness that lets the person accountable for agent-built software warrant a change by reading **evidence** instead of code. Agents write the spec, the tests and the code; the factory runs deterministic gates, two blind reviews from different model families, and records every step on an append-only ledger. It ends with a warranty pack that separates what was *demonstrated* (a command ran on this commit, here is its exit code and output hash) from what was only *asserted* (the builder says it's done). The accountable person signs the pack or returns it. The harness never signs.

[DESIGN.md](DESIGN.md) is the spec, including what the harness guarantees and what it doesn't. [REVIEW-2026-10-11.md](REVIEW-2026-10-11.md) records an adversarial review and its fixes. The knowledge layer is this corpus's `warranting-agent-built-software` task axis ([spec](../../tasks/warranting-agent-built-software.md), [distillation index](../../distillations/warranting-agent-built-software/WARRANTING-AGENT-BUILT-SOFTWARE-DISTILLATION-INDEX.md)); its eight phases are the eight stages.

## Install

Needs macOS (for `sandbox-exec`), Python 3.12+ and [uv](https://docs.astral.sh/uv/), plus on PATH: `git`, `claude` (Claude Code), `gitleaks`, `osv-scanner`, `semgrep`, and the Codex CLI (`codex` on PATH, `$CODEX_BIN`, or the ChatGPT app's bundled binary).

```bash
uv tool install --editable /path/to/factory   # puts `factory` on PATH
factory --help
```

Or run it from the repo without installing: `uv run --project /path/to/factory factory --help`.

To drive it from Claude Code, load the plugin (a skill and two agents):

```bash
claude --plugin-dir /path/to/factory
```

**Run `factory` from an unsandboxed shell.** It sandboxes what it runs with `sandbox-exec` and Claude Code's sandbox, and sandboxes can't nest: started from inside a sandboxed shell (Claude Code's sandboxed Bash, for one), it refuses to run builder code and Claude legs exit, both with a reason in the ledger.

## Opt a repo in

Commit `.factory/config.yaml` to the target repo. The factory reads it from the change's baseline commit, so neither an uncommitted edit nor the change itself can loosen the gates; a semgrep ruleset at a repo path is copied out of the baseline too.

```yaml
commands:                 # each runs sandboxed from the worktree root; exit 0 = pass
  install: npm ci
  test: npm test          # required
  typecheck: npm run typecheck
  lint: npm run lint
  build: npm run build
  perf: npm run perf      # exit non-zero when over budget
  deploy_preview: ...     # release stage only
  smoke: ...              # release stage only
test_globs: ["test/**"]   # required: the files that get locked. Include test config and helpers you don't want the builder to touch.
surface_globs: []         # extra files that steer tests or scanners; the gate flags changes to them
risk_paths:               # path globs → risk class, on top of the built-in rules
  auth: ["src/auth/**"]
  personal-data: ["src/users/**"]
axis_spec: /path/to/grounded-forge/corpus.commons/chrisgagne-agent-built-software/tasks/warranting-agent-built-software.md
axis_index: /path/to/grounded-forge/corpus.commons/chrisgagne-agent-built-software/distillations/warranting-agent-built-software/WARRANTING-AGENT-BUILT-SOFTWARE-DISTILLATION-INDEX.md
builder:
  kind: claude            # claude (thin default legs) | command
  command: null           # see "Builder adapters"
ratchet:
  semgrep_findings: true  # absolute: semgrep findings over the whole repo may not rise at all
  lint_warnings: npm run lint -- --format json   # density: warnings per 1,000 non-blank lines may not rise
  density_tolerance: 0.02 # how far (as a fraction) a density may rise above the baseline's
  # either may be a mapping: {command: ..., mode: absolute|density, tolerance: 0.05, files: ["src/**"]}
theory_doc: docs/THEORY.md
review:
  claude_model: opus
  codex_model: gpt-6.1-sol
  grounding: seeds        # none | seeds (the spec's seed rows) | distillations (the index's listener rows and the distillations they cite)
# Optional, with defaults:
legs: {claude_model: opus, permission_mode: acceptEdits, timeout_minutes: 30, setting_sources: project}
gate: {timeout_minutes: 15, semgrep_config: p/default}   # plus the pinned rules; `auto` needs semgrep metrics on
isolation:
  os_sandbox: true        # false runs commands unconfined (recorded in the ledger); don't
  network: [install, adapter]   # checks that may reach the network; loopback is always allowed
  allowed_domains: []     # domains a Claude leg's Bash may reach, e.g. [registry.npmjs.org]
  allow_write: []         # extra folders commands may write, e.g. [~/.npm]
  env: []                 # extra environment variable names to pass through
worktree_root: null       # default: ../.factory-worktrees/{repo name}/ (never inside the repo)
```

The factory adds `.factory/changes/` to the repo's `.git/info/exclude`; the change folders never get committed.

## Run a change

```bash
factory run STORY.md --repo PATH        # new change: stages 1-7, stops at the first block
factory run --change ID --repo PATH     # resume at the first stage that isn't ready
factory status --change ID --repo PATH  # where each stage stands
```

Each stage is also its own command: `factory spec|triage|tests|build|gate|review|warrant|release --change ID --repo PATH` (`spec --recheck` re-checks a hand-edited `acceptance.md`; `tests --recheck` re-checks the tests already committed, without a leg; `warrant --assessor` adds a plain-language summary, filed as asserted). One factory process works on a change at a time.

When a stage blocks, `.factory/changes/{id}/decisions-needed.md` says what blocked, the evidence, and what would unblock it.

| Stage | What runs | Blocks when |
|---|---|---|
| 1 spec | a read-only leg writes `acceptance.md` | a criterion lacks an `AC-N` id or a `check:` line, or the leg changed the worktree |
| 2 triage | keyword, path and diff-pattern rules → `risk.json` | after the build, the diff reaches a risk class by path or code pattern that the story and acceptance never mentioned |
| 3 tests | a sandboxed leg writes tests | baseline red; non-test files touched; existing tests changed or removed; a check line's file or test name missing; the new tests pass before the build; the red run timed out or couldn't start, or its output never mentions a criterion's test |
| 4 build | a sandboxed leg implements the change; the driver commits it | leftovers in the worktree, the leg fails, or it changes nothing |
| 5 gate | locked tests (content, type, mode); your commands, sandboxed; gitleaks; osv-scanner; semgrep (your ruleset plus `factory/rules/semgrep/`); rollback; test/scanner config edits (`surface`); ratchets; required gates; code unchanged by the gate's own commands | any check fails |
| 6 review | Claude and Codex review blind, read-only, each on its own sanitised export; a Claude leg sorts their findings | a reviewer's or the sort's output is invalid or incomplete, or a confirmed critical or high finding is open |
| 7 warrant | code assembles `warranty.md` from the ledger | a stage isn't ready or isn't at the current commit, the worktree has uncommitted changes, or an artefact or log changed after the ledger recorded it |
| 8 release | `deploy_preview` and `smoke`, sandboxed | no valid signature for the current commit |

## The human step

```bash
factory sign   --change ID --by NAME                      # at a terminal; asks you to type the change id
factory return --change ID --reason "..." [--by NAME]     # the next build's prompt carries the reason
factory accept --change ID --item F2 --reason "..." --by NAME            # a confirmed review finding
factory accept --change ID --item class:dependency --reason "..." --by NAME   # an unplanned risk class
factory accept --change ID --item ratchet:semgrep_findings --reason "..." --by NAME   # a measured ratchet rise
factory accept --change ID --item surface --reason "..." --by NAME       # an edit to test or scanner config
```

`sign` fails if the pack changed since it was assembled, if any stage ran or a return was recorded since, if the pack isn't ready, or if the worktree isn't at the commit and tree the pack covers with nothing uncommitted. A signature records the signer, the time, the pack's sha256, the commit, the tree and a seal over them. After a return, the change needs a new build commit (and fresh triage, gate, review and pack) before anyone can sign. An acceptance covers the stage run it follows; re-running that stage needs a fresh one. Gate failures other than a measured ratchet rise or a surface edit can't be accepted.

## What's in a change folder

`.factory/changes/{id}/`: `change.json`, `story.md`, `config.yaml` (snapshot from the baseline commit), `ledger.json`, `acceptance.md`, `risk.json`, `tests.lock`, `builder-summary.md` (asserted), `warranty.md`, `decisions-needed.md`, and a folder per stage with briefs, leg settings, leg transcripts (`*.jsonl`, stream-json), command logs, review packets and the guard's block log.

`ledger.json` is a hash chain, anchored outside the change folder: every append also records the event count and the last event's hash in `.git/factory/anchors/{id}.json`, and every read checks both, so an edited, removed, truncated or rewritten history fails to load. The ledger and the evidence are tamper-evident against the agents and against accidents; someone with your own file access could rewrite the ledger and its anchor together, and a signature is a record, not a cryptographic signature.

## Isolation

Builder-controlled code runs in an OS sandbox; the guard is a first line, not the boundary.

- **Claude legs** run with Claude Code's sandbox switched on through `--settings` (`failIfUnavailable`, no unsandboxed escape hatch, `strictAllowlist` network with `isolation.allowed_domains`, none by default). Bash and everything it starts can write the worktree and nothing that matters outside it: not git metadata, the change folder, the repo's `.factory/`, Claude settings or a locked test; and can't read the secret paths (`~/.ssh`, `~/.aws`, `~/.gnupg`, `~/.netrc`, `~/.claude/secrets`, keychains, `~/.npmrc`, `~/.kube`, `~/.config/gh` and others; see DESIGN.md).
- **Gate commands, ratchet and rollback commands, release commands and builder-command adapters** run under `sandbox-exec` with the same limits, plus: a locked test can't be written, replaced or moved even to put it back, and there's no network unless the check is in `isolation.network` (by default `install` and adapters). When `sandbox-exec` can't apply a profile, the command doesn't run.
- **Every leg and command** gets an environment built from an allowlist plus its own CLI's credential; `DATABASE_URL`, `KUBECONFIG` and the like never reach them.

What it doesn't cover, plainly: reads of your files outside the secret paths; Claude Code's per-user temp folder (`/tmp/claude-UID`), which every Claude leg can write and which other Claude Code sessions use for scratch files; local IPC beyond the keychain and Apple events; anything a check granted network can send; and Linux (no `sandbox-exec`). `sandbox-exec` is deprecated by Apple, though it works on macOS 26.5. Claude Code 2.1.288 ignores the guard hook's `onFailure: "block"`, so the guard catches its own errors and exits 2.

## The guard

`factory/hooks/guard.py` is a Claude Code PreToolUse hook, installed for every Claude leg through `--settings`. It exits 2 with a reason (which the agent sees) for: edits to locked tests, to protected paths (git metadata, the change folder, `.factory/`, Claude settings), or outside the worktree; reads of secret paths, checked on the resolved path so a symlink to a secret is caught; write-like Bash commands naming a locked or protected path; recursive `rm` outside the worktree; `git push`, history rewrites, git config changes, inline alias/core config and `GIT_*` overrides; `curl … | sh`; `sudo`; disk tools; `DROP`/`TRUNCATE`; and `factory sign|return|accept`. Any error inside the guard, logging included, blocks. It reads tool calls, so it can't see what a script does when it runs; the sandbox is what stops that, and the gate re-checks the locked tests anyway.

## Builder adapters

Stages 1, 3 and 4 are adapters. With `builder.kind: command`, the factory runs your command, under `sandbox-exec`, in the worktree instead of its own `claude -p` leg (the spec adapter gets a read-only worktree). `command` is a string (run for all three stages) or a mapping (`{spec: ..., tests: ..., build: ...}`; stages left out use the default leg). The command gets `FACTORY_STAGE`, `FACTORY_STORY`, `FACTORY_ACCEPTANCE`, `FACTORY_BRIEF` (the factory's own brief for that stage), `FACTORY_TESTS_LOCK`, `FACTORY_TEST_COMMAND` and `FACTORY_TEST_GLOBS`. Its stdout is the stage's artefact: `acceptance.md` for spec, the asserted summary otherwise. While it runs, the guard is written to the worktree's `.claude/settings.local.json`. An adapter that starts a Claude Code session runs that session inside `sandbox-exec`, where Claude Code's own sandbox can't nest and its config writes outside the worktree fail; give it what it needs with `isolation.allow_write` knowing that widens the boundary. The checks after each stage are the same however the code was made.

## Calibration

```bash
factory calibrate                      # every fixture in calibration/defects/
factory calibrate --grounding none     # the A/B: run once each with none, seeds and distillations
factory calibrate --only 03-name --no-review
```

Each fixture (`story.md`, `change.patch`, `expect.yaml`) runs against a fresh copy of `calibration/sample-app/`: stages 1 and 3 are simulated (the baseline's tests are locked), the patch stands in for the build, and triage, gate, review and warrant run for real. Every stage runs even after an earlier one blocks, so the report (`calibration/report-{date}-{grounding}.md`) shows each stage's catches, the catch rate, false positives on the clean control, review cost and an overall PASS/FAIL. `factory calibrate` exits 1 if any fixture errors or misses; errored fixtures count in the rates. A review that failed closed on invalid leg output shows as `review:malfunction`, never as a catch. With `--no-review`, fixtures only review is expected to catch are reported n/a. Work folders are kept in a temp folder the report names.

In the recorded runs under `calibration/` (reports, logs, packs), the machine's absolute paths are replaced by fixed placeholders: `<factory>` for this repo, `<grounded-forge>` for the grounded-forge repo, `<scratch>` for the operator's session scratch folder (`<scratch>…` where the record had already cut the path short) and `<tmp>` for the system temp folder. `calibration/showcase-2026-10-14/` is the exception: its ledger hash-binds its files, so they keep their paths.

## Develop

```bash
uv run pytest        # the harness's own tests: no model spend; needs macOS, git, gitleaks, osv-scanner and semgrep on PATH
```
