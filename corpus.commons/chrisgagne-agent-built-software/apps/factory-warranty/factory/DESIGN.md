# factory v0: design

A harness that lets the person accountable for agent-built software warrant a change by reading **evidence**, not code. Builders no longer review their own code line by line; they rely on the harness. So the warranty lives in the harness, and the harness itself must be warranted.

**Compose the build layer; own the warranty layer.** Spec-and-build methodologies already exist and are widely used (obra/superpowers, GitHub Spec Kit, OpenSpec, BMAD). None of them publishes evidence that its gates catch anything; they rely on the user's review or the agents' review of their own work. So the factory does not compete on how code gets written. Stages 1, 3 and 4 are adapters: a thin default `claude -p` leg, or any methodology run inside the sandboxed worktree. The gates, the ledger, independent review, calibration and sign-off are the factory, and they don't care how the code was made.

The knowledge layer is this corpus's `warranting-agent-built-software` task axis ([spec](../../tasks/warranting-agent-built-software.md), [distillation index](../../distillations/warranting-agent-built-software/WARRANTING-AGENT-BUILT-SOFTWARE-DISTILLATION-INDEX.md)). Its eight phases are this harness's eight stages.

## Principles

1. **Evidence over assertion.** Every stage writes machine-checkable evidence to the change's ledger. The warranty pack contains nothing the ledger doesn't record. Anything a model *says* (the builder's "all tests pass", the assessor's summary) is filed as *asserted*, never as *demonstrated*.
2. **Gates are code, and they fail closed.** Stage order, pass/fail and blocking are decided by the driver from exit codes, hashes and structured findings. Models produce artefacts and findings; no model passes its own work. A tool error, a timeout, a sandbox that can't start, malformed reviewer or sorter output, a missing field, unparseable JSON or a ratchet measurement error blocks and is recorded as such; none of them passes and none silently drops a finding.
3. **Evidence binds to code.** Every stage run and outcome, the warranty pack and the signature record the commit and tree they describe. Evidence about other code, or about a worktree with uncommitted changes, doesn't count.
4. **Isolation is the OS's job.** Everything that runs builder-controlled code runs in an OS sandbox: Claude Code's sandbox for Claude legs, macOS `sandbox-exec` for commands. The PreToolUse guard is the first line, not the boundary: it reads tool calls and can't see what a script the agent wrote does when it runs.
5. **Independence.** The session that builds never reviews. Review runs as two blind legs in fresh contexts, one Claude and one Codex (a second model family), each on its own sanitised export of the code, then a sort leg reconciles them.
6. **Locked tests, locked config.** Tests accepted before the build are locked by content, type and mode in `tests.lock`; the sandbox stops any leg or command writing them, and the gate re-checks them. The config that judges a change comes from the baseline commit, never from the change.
7. **One human step, and a light one.** The accountable human signs the warranty pack or returns it, by reading the evidence, not by convening approvers. The harness never signs. Forsgren, Humble and Kim (*Accelerate*) found that approval by a body outside the work doesn't make production more stable; what they recommend is light peer review inside the team with a deployment pipeline that rejects bad changes, which the independent review and the gates stand in for here. Their data says nothing about a pack signed this way, so the calibration has to.
8. **The harness is warranted too.** Calibration fixtures (seeded-defect changes against a sample app) give a catch rate per stage, run on every harness change. A clean control change must pass (false-positive check). A miss or a broken fixture fails the run.

## Layout

```
factory/
  DESIGN.md  README.md  REVIEW-2026-10-11.md  pyproject.toml   # uv project; runtime deps: pyyaml only
  factory/                                       # Python package, CLI entry point `factory`
    cli.py ledger.py legs.py isolation.py axis.py calibrate.py
    stages/ spec.py triage.py tests.py build.py gate.py review.py warrant.py release.py
    hooks/guard.py                               # PreToolUse guard for Claude legs (first line)
    prompts/ spec.md tests.md build.md reviewer.md sort.md assessor.md
    rules/semgrep/                               # factory's pinned semgrep rules
  .claude-plugin/plugin.json                     # Claude Code plugin wrapper
  skills/factory/SKILL.md                        # how to run a change through the factory from Claude Code
  agents/independent-reviewer.md agents/warranty-assessor.md
  calibration/
    sample-app/                                  # small real app the defects are written against
    defects/{NN-name}/ story.md change.patch expect.yaml
  tests/                                         # the harness's own unit tests (pytest via uv)
```

## Target-repo contract

A target repo opts in by committing `.factory/config.yaml`. The factory reads it from the **baseline commit** (`git show BASELINE:.factory/config.yaml`), not from the working tree, so neither an uncommitted edit in the main checkout nor the change itself can loosen the gates. A semgrep ruleset named by a repo path is copied out of the baseline commit too. The snapshot, the story and `change.json` are hashed into the change's first ledger event and re-checked on every load.

```yaml
commands:            # each run from the worktree root, sandboxed; exit 0 = pass
  install: npm ci
  test: npm test
  typecheck: npm run typecheck      # optional
  lint: npm run lint                # optional
  build: npm run build              # optional
  perf: npm run perf                # optional; exit non-zero when over budget
test_globs: ["test/**/*.test.*"]    # files that get locked
surface_globs: []                   # extra files that steer tests or scanners (see gate:surface)
risk_paths:                         # path globs → risk class (adds to the built-in keyword rules)
  auth: ["src/auth/**"]
  personal-data: ["src/users/**"]
  migration: ["migrations/**"]
axis_spec: /path/to/grounded-forge/corpus.commons/chrisgagne-agent-built-software/tasks/warranting-agent-built-software.md
axis_index: /path/to/grounded-forge/corpus.commons/chrisgagne-agent-built-software/distillations/warranting-agent-built-software/WARRANTING-AGENT-BUILT-SOFTWARE-DISTILLATION-INDEX.md
builder:                            # stages 1, 3 and 4 are adapters
  kind: claude                      # claude (default thin legs) | command
  command: null                     # for kind: command, run sandboxed in the worktree
ratchet:                            # counts that may not rise above the baseline's
  semgrep_findings: true            # absolute: no rise at all
  lint_warnings: npm run lint -- --format json   # density: per 1,000 non-blank lines
  density_tolerance: 0.02           # a density may rise this fraction above the baseline's
theory_doc: docs/THEORY.md          # optional; the program's theory, kept with the code
review:
  claude_model: opus
  codex_model: gpt-6.1-sol
  grounding: seeds                  # none | seeds | distillations
isolation:
  os_sandbox: true                  # false runs commands unconfined; the ledger records it
  network: [install, adapter]       # checks that may reach the network (loopback is always allowed)
  allowed_domains: []               # domains Claude legs' Bash may reach (none by default)
  allow_write: []                   # extra folders commands may write (e.g. a package cache)
  env: []                           # extra environment variable names to pass through
```

## Isolation

What runs builder-controlled code, and what confines it:

| Runs | Confined by | May write | May not |
|---|---|---|---|
| Claude spec, tests and build legs (and their Bash children) | Claude Code's sandbox, through `--settings`: `enabled`, `failIfUnavailable`, `allowUnsandboxedCommands: false`, no excluded commands, `network.allowedDomains` from config with `strictAllowlist` | the worktree; Claude Code's per-user temp folder (`/tmp/claude-UID`) | write git metadata, the change folder, the repo's `.factory/`, `.claude/settings*.json` or any locked test; read the secret paths; reach any domain not allowed |
| Gate commands, ratchet commands, the rollback rehearsal, release commands, builder-command adapters | `sandbox-exec` with a generated profile (`factory/isolation.py`) | the folder the command works in (the worktree, or the ratchet's baseline checkout); a private temp folder; `isolation.allow_write` | the same as above, plus: replace or move a locked test or the folders that hold it; reach the network unless the check is in `isolation.network`; look up the keychain service; send Apple events |
| The spec adapter | `sandbox-exec`, read-only worktree | a private temp folder | write the worktree |
| Claude reviewers, sort, assessor | read-only tools (Read, Grep, Glob) plus the same settings | nothing | read secret paths; the Claude reviewer and the sort can't read the change folder; the Claude reviewer can't read Codex's folders |
| Codex reviewer | Codex's own `-s read-only` sandbox, `--ignore-user-config` | nothing | (reads the whole disk; see below) |
| The factory's own scanners (gitleaks, osv-scanner, semgrep) | not sandboxed: they parse the repo but don't execute it; targets are passed so a file name can't become an option | their reports | |

Secret paths (no read by a Claude leg, which the guard and its settings deny, or by a sandboxed command; the Codex reviewer's read-only sandbox does not deny them, a residual risk listed below): `~/.ssh`, `~/.aws`, `~/.gnupg`, `~/.netrc`, `~/.claude/secrets`, `~/Library/Keychains`, `~/.npmrc`, `~/.pypirc`, `~/.docker/config.json`, `~/.kube`, `~/.config/gh`, `~/.git-credentials`, `~/.config/gcloud`, `~/.azure`, `~/.codex/auth.json`, `~/.claude/.credentials.json`.

Every process gets an environment built from an allowlist (`PATH`, `HOME`, locale, toolchain homes such as `VOLTA_HOME`, CA bundles), plus the one credential its own CLI needs (`ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` or `CLAUDE_CODE_OAUTH_TOKEN` for Claude legs; `OPENAI_API_KEY` for Codex), plus names listed in `isolation.env`. A `builder.kind: command` adapter gets no provider credential at all unless `isolation.env` names it. `DATABASE_URL`, `KUBECONFIG` and anything else not on the list never reach a leg or command.

When `sandbox-exec` can't apply a profile (not macOS, or the factory itself is running inside a sandbox, where profiles can't nest), builder-controlled commands don't run: the check fails with the reason. When Claude Code's sandbox can't start, the leg exits (`failIfUnavailable`). `isolation.os_sandbox: false` is the operator's explicit opt-out; each command's ledger event records `sandbox: off`.

The driver keeps its own scratch folders (briefs passed to legs, review exports, ratchet baseline checkouts, command temp folders) in `.factory-tmp/` beside the worktrees, outside every leg's and command's write access. The driver's own git calls run with `core.hooksPath=/dev/null` and `core.fsmonitor=false`.

**Not covered, plainly:**

- Reads. Apart from the secret paths (and the change folder for the Claude reviewer and the sort), legs and commands can read the operator's files. The Codex reviewer's read-only sandbox can read the whole disk, including the change folder.
- Claude Code's per-user temp folder `/tmp/claude-UID` is writable by every Claude leg (Claude Code forces it as the sandbox's `TMPDIR`). Other Claude Code sessions of the same user keep scratch files there, so a build leg can write into them. The factory keeps nothing there.
- `sandbox-exec` is deprecated by Apple (it still works on macOS 26.5) and its profile here starts from `(allow default)`: it confines writes, secret reads, network and two IPC paths, not every operation. Local IPC to other services is still allowed, and a check that is granted network (by default `install`, and adapters) can send what it can read.
- Claude Code hooks run outside its sandbox. The guard is the factory's own hook; a target repo's committed `.claude/settings.json` hooks (baseline content, which legs can't modify) also run for write legs.
- `onFailure: "block"` is set on the guard hook, but Claude Code 2.1.288 accepts and ignores it (checked 2026-10-11): a crashed hook doesn't block there. The guard catches every error itself and exits 2.
- Gate commands run with the network off by default; a test suite that needs the network needs `isolation.network: [install, tests]` or similar, and then can send what it reads.

## The ledger

`.factory/changes/{change-id}/` in the target repo (git-ignored by the target), holding `ledger.json` and the artefacts. `ledger.json` is an append-only list of events:

```json
{"id": "e012", "stage": "gate", "check": "tests", "status": "pass",
 "started": "...", "finished": "...", "cmd": "npm test", "exit": 0, "sandbox": "sandbox-exec",
 "output_tail": "...", "output_sha256": "...", "evidence": ["gate/tests.log"],
 "artefacts": {"gate/tests.log": "..."}, "recorded": "...", "prev": "..."}
```

Every event has an id, stage, status (`pass | fail | blocked | skipped | info`) and, where a command ran, the command, exit code, output hash and the hash of every evidence file it names. Statuses are written by the driver only. Each event carries `prev`, the sha256 of the event before it.

**What protects it.** On every append the driver writes an anchor in the repo's git directory (`.git/factory/anchors/{change-id}.json`: the event count and the sha256 of the last event), and every read checks the chain and the anchor. A truncated ledger, an edited last event, a history rewritten with a recomputed chain, or a missing anchor fails to load; the CLI stops with exit 3 and says why. Appends hold an interprocess lock and write through a unique fsynced temp file, and one factory process holds a change at a time. No leg or command can write the change folder or the git directory (see Isolation).

**What it doesn't protect against.** Someone with the operator's own file access can rewrite the ledger and its anchor together. There is no signing key: a signature records who said they signed, bound to the pack hash, the commit, the tree, the change and the time by a seal (a sha256 over those fields) that release re-checks, so an edit to any of them is caught unless the editor also recomputes the seal, the chain and the anchor. That is tamper-evidence against the agents and against accidents, not non-repudiation. A crash between writing the ledger and writing its anchor leaves them disagreeing; reads then fail closed and the operator decides.

## Stages

`factory run STORY.md --repo PATH` runs stages 1–7 in order and stops at the first block, writing `decisions-needed.md` (what blocked, what evidence would unblock it). Each stage is also its own subcommand (`factory spec|triage|tests|build|gate|review|warrant|sign|return|release`) taking `--change ID`. A stage command runs only when the stage it follows is ready, passed or with every blocked item accepted: tests and the first triage follow spec, build follows tests, triage after a build follows the build, the gate follows that triage, and review follows the gate. A refused command records `check: order` in the ledger and runs nothing. Calibration and replay call the stages directly, because a measurement runs every stage on purpose.

Every stage run starts with an event recording the commit, tree and cleanliness of the worktree, and ends with an outcome that records them again. A stage counts as ready only if its latest outcome is newer than its latest start (an interrupted rerun is not ready), newer than the stage before it, and, for build, triage, gate and review, at the worktree's current commit and tree with nothing uncommitted. Triage, gate and review also block when the code changed while they ran.

1. **spec.** A read-only leg turns the story into `acceptance.md`: numbered criteria, each with a `check:` line naming the test file and test that will prove it. Deterministic gate: every criterion has an ID and a check line; otherwise blocked. If the spec leg left the worktree changed, the stage blocks instead of committing it.
2. **triage.** Deterministic first: changed or planned paths against `risk_paths`, plus built-in keyword rules over the story, acceptance and (after build) the diff, map to risk classes: `auth`, `personal-data`, `money`, `migration`, `irreversible`, `infra`, `llm-agent`, `dependency`, `secrets`. Output `risk.json`: classes, the evidence for each, and the required gates and review focus each class triggers (e.g. `migration` → requires a rehearsed rollback; `dependency` → requires `gate:deps`; `auth`/`personal-data` → ASVS chapters in review focus; `llm-agent` → OWASP LLM and agentic lists in review focus). Triage re-runs after the build on the actual diff and blocks on a class the diff reaches by path or pattern that the plan never mentioned.
3. **tests.** A leg writes tests from `acceptance.md` in the worktree, before any implementation. The driver requires: a clean worktree to start; only test files touched; existing tests kept (lines may be added to an existing test file, not changed or removed; nothing is committed when they are); each check line's file to exist and contain the test it names; the suite to be **red** with the new tests in a completed run (a timeout, a sandbox that couldn't start or an exit of 126 or more is not red); and the red output to mention each criterion's test or file. So the test command must name every test it runs, passed ones included: TAP and `node --test` do; pytest needs `-rA` or `-v`, since `-q` prints a passing test as a dot (the factory's first job on its own repo stopped there, on a criterion whose existing test was meant to keep passing). Then it writes `tests.lock`: sha256, mode (`100644`, `100755`, or `120000` for a symlink, hashed by its target text) and path of every file matching `test_globs`.
4. **build.** A leg implements the change in the worktree under the guard and the sandbox, and leaves its work uncommitted; the driver commits it. The build refuses a worktree with leftovers from an earlier leg. A Claude build leg's shell runs one thing: the factory check (`factory/check.py`), written into the change folder, which the leg can run but not write. The check scans what the leg has written so far: invisible characters and secrets in what it changed, and semgrep, with a committed ruleset and the pinned rules, on the lines it added. It runs the named gate command (any configured one but `install`, which needs the network) only if every scan passes. The scans cover what the leg changed since the commit the build started from. The guard allows only those exact commands, word for word, so generation and execution are separated by a scan (OWASP ASI05 #5 and #7), and the leg's shell runs from an allowlist rather than a deny list (#6). The leg reads with Read, Grep and Glob and writes with Edit and Write. The check runs inside the leg's sandbox, with no network, so a registry ruleset waits for the gate. The tests leg gets the same check with one command, `test`, so the tests it writes are scanned before they run. If git or a scanner can't run, the check refuses to run the command. After the tests leg, the driver runs the same scans on what it wrote before it runs the new tests itself (`tests:scan`). A builder command adapter keeps its own shell, under sandbox-exec. The builder's final message is stored as `builder-summary.md` and is only ever shown as *asserted*.
5. **gate.** Deterministic, every check one event; any fail blocks:
   - `locked-tests`: `tests.lock` matches the hash its ledger event recorded, and every locked file matches by content, type and mode.
   - `install`, `typecheck`, `lint`, `build`, `tests`, `perf`: the repo's commands, sandboxed.
   - `secrets`: `gitleaks` on the change's commits, ignoring `gitleaks:allow` comments.
   - `deps`: `osv-scanner` on the lockfiles and requirements files the change touched; a dependency change with no lockfile change fails, since nothing new can be scanned.
   - `sast`: `semgrep` (the configured ruleset plus factory's pinned rules) on the touched files, passed as `./path` after `--`, with `nosemgrep` comments ignored; errors in semgrep's report fail.
   - `added-tests`: test files the build added that the lock doesn't cover. Under a runner that isolates each test file (`node --test`, jest, vitest; `npm test` is resolved from the baseline's package.json) they pass and the pack lists them; under any other runner, pytest included, they could patch what a locked test sees, so a human accepts them (`--item added-tests`). The sources set the principle (an agent asks before it alters a test: Crickett, via Ojstersek; adjusting a fixture until a result passes is normalised deviance: Vaughan); the runner list is PROPOSED.
   - `rollback`: when a class requires it, or whenever the change writes one, `rollback.md` with a `rehearse:` command that runs sandboxed and exits 0. Only a `rollback.md` this change wrote counts; one an earlier change left at the root does not. A rollback the pack offers is rehearsed, never only described. The exit code is the command's own claim that it restored the previous state; write the command so it checks that.
   - `surface`: the change edits files that steer the tests or the scanners and aren't locked (runner config such as `conftest.py`, `jest.config.*`, `.mocharc*`; `package.json` `scripts`, `jest`, `mocha` and similar keys; `pyproject.toml` `[tool.pytest]` and similar tables; `.semgrepignore`, `.gitleaks.toml`, `.gitleaksignore`, `osv-scanner.toml`; eslint config; `.factory/`; plus `surface_globs`).
   - `ratchet:NAME`: see below.
   - `required`: every gate a risk class in `risk.json` requires ran in this gate run and passed; a skipped required gate fails.
   - `unchanged`: after every command, the commit, tree, cleanliness and locked tests are what the gate started with.

   **Ratchet.** Each count declares a mode. `absolute` (the default for `semgrep_findings`): the count may not rise at all, because any new security finding is a finding. `density` (the default for `lint_warnings`): warnings and complexity counts grow with codebase size, so a ratchet on absolute totals trips on almost any change that adds code and then gets waived as routine (He et al. 2025, arXiv 2511.04427, report that AI coding speeds teams up only briefly while static-analysis warnings and complexity stay up). A density ratchet compares findings per 1,000 non-blank lines of the scanned files (the files the tool's JSON names, or `files:` globs) at baseline and after the change, and fails when the density rises more than `density_tolerance` (a fraction, default 0.02) above the baseline's. Either form may be written as a mapping `{command, mode, tolerance, files}`. The ledger records both raw counts and both line counts. A measurement the driver can't trust (a disallowed exit code, output that isn't JSON, a count that isn't a non-negative integer, semgrep reporting more scan errors than at baseline, a failed baseline install) fails as a measurement error.

   Only a measured ratchet rise, a `surface` change, unlocked test files the build added and added invisible characters can be accepted by the human, with a reason, in the ledger (`factory accept --item ratchet:NAME`, `--item surface`, `--item added-tests` or `--item invisible`). Measurement errors and every other gate failure can't.
6. **review.** Two blind legs in fresh contexts, read-only: `claude -p` (read-only tools) and `codex exec -s read-only`. Each works in its own `git archive` export of the head with agent instruction and settings files removed (`.claude/`, `CLAUDE.md`, `AGENTS.md`, `.mcp.json`, `.codex/` and the like), never in the builder-writable worktree, with its own packet: the diff against baseline, `acceptance.md`, `risk.json`, the `theory_doc` if configured and the axis rows for the phases and risk classes in play: with `grounding: seeds`, the spec's seed trigger→response rows (`P{phase}.{n}`); with `grounding: distillations`, the distillation index's runtime listener rows (`L{phase}.{n}`, the seed rows plus those the per-source distillations added) and the distillation files they cite, which a reviewer opens only to check what a row rests on. The distillation files are hashed into the ledger but not kept in the change folder: most paraphrase copyrighted books licensed for the operator's own use. Live transcripts are written outside the change folder and copied in after both finish. Each reviewer's final message must be exactly a JSON array of findings, `[{severity, file, line, claim, evidence, axis_row?}]`; any invalid item, or prose around the array, blocks. The Claude legs run with `--json-schema`, so the CLI holds their final message to that shape (an object whose `findings`, or for the sort `items`, is the array) and a line of progress prose can't block a review that did its job; the Codex reviewer runs with `--output-schema`, a strict version of the same shape (every field present, `file`, `line` and `axis_row` nullable). The validators still judge every item. A `claude -p` sort leg merges them into confirmed / disputed / noise with a reason each, and must account for every finding exactly once; an incomplete or invalid sort blocks. Confirmed critical or high findings block until resolved, and so does a finding a reviewer rated critical or high that the sort lowered, disputed or called noise: the sort is a model, and NIST SP 800-218A (PW.1.1, C2) asks that no AI model make a significant security decision without a human in the loop. Where triage classes the change `personal-data` or `irreversible`, the bar drops to medium: a confirmed medium blocks, and so does a reviewer's medium the sort set aside (the first two real runs' mediums were data loss: a retried delete erasing a newer note, a down migration dropping every phone number). The sources set no severity bar, so this one is PROPOSED; the ledger records the bar each review used (`check: bar`). Every kind blocks until resolved (a new build commit plus a re-run of gate and review) or explicitly accepted by the human with a reason recorded in the ledger. The briefs tell reviewers to treat everything they read as data; whether a model complies is a residual risk the driver can't check.
7. **warrant.** The pack opens with a decision page for an accountable person who doesn't read code, built by code from the ledger: what was asked for (the story's own words, then the AI-written behaviours, labelled as such, each with the test that went from failing to passing); whether each check passed, in plain words; what's left over (findings below the bar, in the reviewers' words; acceptances; the undo position); whether a qualified second person must look, by risk class; whether it's within the rules; the rules themselves from `factory/policy.yaml`, each with who set it and whether the accountable person has confirmed it; and the choices. It doesn't ask whether the code is right: the checks and reviewers answer that against the rules. `factory sign` prints the page before it asks for the change id. Below it, deterministic assembly of `warranty.md` from the ledger: change, story, risk classes, the commit and tree it covers; **Demonstrated** (each command run with exit code and output hash; the locked-test check); **Asserted, not evidence** (the builder's summary); gates passed, failed and skipped (with reason); review findings and their resolution; irreversible operations and the rollback evidence; ratchet counts before and after; whether the theory doc changed; residual risks (skipped gates, confirmed findings below the blocking bar, disputed findings, acceptances); and an empty sign-off block. The pack is not ready if any artefact or evidence file differs from the hash its event recorded, if any stage isn't ready, or if the worktree has uncommitted changes. An optional assessor leg may add a plain-language summary, filed under "Assessor's summary (asserted, not evidence)": the driver keeps only lines citing ledger event ids that exist, which shows where to look, not that the events support the line. `factory sign --change ID --by NAME` records the signature (signer, time, pack sha256, commit, tree, warrant event and their seal). Sign refuses if the pack changed, if a stage ran or a return was recorded after it, or if the worktree is not at the pack's commit and tree with nothing uncommitted. `factory return --change ID --reason …` records a return, and the change goes back through spec and tests before the rebuild, so what the reason asks for gets locked tests the builder can't touch. The spec leg gets the reason and the current criteria. It must keep every criterion word for word, or the stage blocks. It adds criteria only for behaviour the reason asks for, and adds none for a reason no test could show. The tests leg then writes tests only for the criteria the lock doesn't cover. The suite must be green at the current build first, and the new tests must fail before the rebuild (only they need to show in that red run). The lock is then rewritten with them in it. With no new criteria, the lock stands and no tests leg runs. Then the build, whose prompt carries the reason, and a new triage, gate, review and pack, before anyone can sign. Without this, the first real job's builder wrote its own tests for a send-back, and in pytest those share a process with the locked ones.
8. **release.** v0 stub: refuses to run without a valid signature (the latest sign event, its seal intact, its pack, commit and tree matching the pack it names and the worktree now, nothing after it); runs an optional `commands.deploy_preview` and `commands.smoke`, sandboxed, recording the outputs.

## Legs

`legs.py` runs headless agents the way grounded-forge's Pass I driver does (`scripts/pass_i/run.py`, class `Agent`): `claude -p PROMPT --output-format stream-json --model … --permission-mode …` with a timeout and a JSON log, and `codex exec -m MODEL -s read-only|workspace-write --skip-git-repo-check --ignore-user-config -C CWD -o OUT PROMPT`. The Codex binary is `$CODEX_BIN`, else `codex` on PATH, else `/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex`. Read-only Claude legs pass `--tools` and `--allowedTools` limited to Read, Grep, Glob. Write legs default to `--permission-mode acceptEdits`: edits in the worktree go through, Bash runs only sandboxed (`autoAllowBashIfSandboxed`), and anything that would need a prompt is denied because a headless leg has no one to ask. Every Claude leg gets `--settings` with the sandbox, the permission denies and the guard hook, and `--strict-mcp-config`. Every leg's brief, transcript, cost and duration go into the ledger, with the hashes of the brief and transcript files.

## Calibration

`factory calibrate [--grounding none|seeds|distillations] [--only NN-name] [--no-review]` runs each fixture in `calibration/defects/` against a fresh copy of `calibration/sample-app/`:

1. Copy the sample app to a temp dir, `git init`, commit the baseline, run `install`, write `tests.lock` from the baseline's test files (stages 1 and 3 are simulated: the baseline's tests are the locked acceptance tests, and `story.md` is the story).
2. Apply `change.patch` with `git apply` and commit it: this simulates the build (stage 4).
3. Run triage, gate and review for real; then warrant.
4. Record every stage that blocked and compare with `expect.yaml`.

`expect.yaml`:

```yaml
should_block: true                 # false for the clean control
caught_by: [gate:locked-tests]     # acceptable catching checks, any of:
                                   # gate:locked-tests gate:tests gate:typecheck gate:lint gate:secrets
                                   # gate:deps gate:sast gate:perf gate:rollback gate:surface gate:required triage review
defect: one-line description of the planted defect
```

The report (`calibration/report-{date}-{grounding}.md`) is a table of fixture × catching stage × expected, the catch rate, false positives on the control, review cost and an overall PASS/FAIL. Errored fixtures stay in the denominators. A review that blocks before its findings are sorted (a leg failed or returned an invalid list) is reported as `review:malfunction`: it failed closed, which protects the operator, but detected nothing, so it is never a catch, and on the control it counts as a false alarm. `factory calibrate` exits 1 when any fixture errors or misses; with `--no-review`, a fixture only review is expected to catch is reported n/a instead. Because stages 1, 3 and 4 are simulated, a passing control shows that the gates and review raise no false alarm, not that the full pipeline produces a signable pack. Running with `--grounding none`, `--grounding seeds` and `--grounding distillations` gives the A/B the axis's success criterion asks for.

## Plugin wrapper

`.claude-plugin/plugin.json` names the plugin `factory`. `skills/factory/SKILL.md` tells Claude Code how to run a change through the factory from an interactive session (call the CLI, read `decisions-needed.md`, present the warranty pack, never sign). `agents/independent-reviewer.md` and `agents/warranty-assessor.md` match the axis spec's §4a roles.

## What the harness guarantees, and what it doesn't

It guarantees, by code: a pack is signable only when every stage passed (or a human accepted the specific acceptable item, with a reason) on the exact commit and tree the pack names, with nothing uncommitted; the locked tests are byte-, type- and mode-identical to what was locked before the build; the config, rules and test commands that judged the change came from the baseline commit; every command and leg ran with a minimal environment, and builder-controlled code ran in an OS sandbox that kept it out of the evidence, the git metadata, the secret paths and (by default) the network; nothing in the ledger, the evidence files or the signature was changed after it was recorded, short of someone rewriting the ledger and its anchor with the operator's own access.

It doesn't guarantee: that the tests test the right thing (the acceptance criteria and the human's reading of them carry that); that the test runner ran every locked test (the gate checks the runner's config files and exit code, not a runner-specific list of executed tests); that model reviewers weren't steered by text in the code they read; that a rollback command really restores data (its exit code is its own claim); confidentiality of the operator's files outside the secret paths; or non-repudiation of a signature.

## Out of scope for v0

Real deploys; multi-change queues; a signing key; runner-specific checks of which tests ran; OS isolation on Linux.

## Next: rules the axis sources add, not yet built

Distillations on an earlier version of this axis spec ground each of these; none is enforced by code yet.

1. **A named theory-holder.** Naur (*Programming as Theory Building*): a program's theory (how it relates to the world it serves, why each part is as it is, and how to change it) stays bound to the people who hold it, ranks above every written product, and can't be rebuilt from documentation alone. Neither the builder leg nor the reviewers hold it, and independence isn't theory. So each area in `risk_paths` names a human `theory_holder`; the pack names the holder for every area the change touches; `theory_doc` misfits the review raises are candidates, and the verdict on fit is the holder's. A change in an area with no holder is flagged on the pack as a change nobody can vouch for.
2. **Prototype, then lock.** Brooks (*No Silver Bullet*): clients can't specify what they want until they've tried a running version. Locking tests before the build assumes the opposite. A `factory prototype` path builds an unlocked, never-signable, never-releasable change for the client to try; the story and acceptance are rewritten from what they learned, and only then are tests locked. A spec change after trying a version is a human decision on the ledger.
3. **Retire checks as well as add them.** Vaughan (*The Challenger Launch Decision*): fixes carry their own side effects (after Challenger the count of single-point-failure items nearly doubled, and the label became a still more routine signal), and sanctioned exceptions become routine practice. Every `factory accept` is counted per area and per item; a rising count triggers a review of that area's exceptions together, with expiries. Every gate states what it catches; a gate whose calibration catches nothing across runs is reviewed for merging or retirement, so the list of checks doesn't only grow.
4. **Seeded defects stay offline.** Bainbridge (*Ironies of Automation*): raising a system's failure rate artificially to keep its operators alert costs their trust in it. Calibration fixtures run against the sample app, never inside the human's live queue of changes to sign.
5. **Earned standard changes.** Kim et al. (*The DevOps Handbook*) let a change class with a recorded record of success (change success rate, time to restore) be pre-approved; Microsoft's agentic maturity model calls keeping agents tightly bound when the data shows they could safely do more an anti-pattern. Vaughan and Cook (*How Complex Systems Fail*) warn that a run of clean outcomes is a run of bets that paid, not evidence about the next change. So a class (say, copy changes outside `risk_paths`) can earn lighter review only from the factory's own ledger history, by stated thresholds, and loses it on the first failure.
6. **Repeated trials for review.** Anthropic (*Demystifying evals for AI agents*): pass@k asks whether one of k attempts succeeds, pass^k whether all do, and model graders need calibrating against human experts. Calibration runs each review-only fixture k times and reports pass^k, and reviewer verdicts are checked against a human expert's on a sample.
7. **High stakes, slower releases.** The Google SRE book (Ch. 33): Google's appetite for release speed, funded by error budgets, rests on most products not putting lives at risk; where they do, the approach is conservative. A `stakes: high` setting makes `release` require a staged rollout, a named second reader of the pack, and no release on a pack with any accepted exception.
8. **LLM output in the product is checked by code.** OWASP Top 10 for LLM Applications 2026: a model's output is untrusted input to whatever consumes it, checked structurally in trusted code, not by a second model call; that catches format violations, not semantic manipulation. For `llm-agent` changes, review focus asks where each model output lands and what code validates it there.

