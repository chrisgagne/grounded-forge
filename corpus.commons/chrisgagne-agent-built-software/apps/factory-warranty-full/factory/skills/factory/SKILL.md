---
name: factory
description: Run a software change through the factory harness (spec, triage, locked tests, guarded build, deterministic gates, blind Claude + Codex review, warranty pack) and present the pack to the accountable person. Use when the user asks to build, gate, review or warrant a change with the factory, to resume a blocked factory change, or to see where one stands. Never signs, returns or accepts on the user's behalf.
---

# Running a change through the factory

The factory is a command-line harness. Its gates are code: exit codes, hashes and structured findings decide pass or block, and every stage writes to an append-only ledger in the target repo at `.factory/changes/{id}/`. Your job here is to drive the CLI, explain what it found, and hand the decision to the person accountable for the change.

The CLI is `factory` (install once with `uv tool install --editable <factory repo>`; the factory repo is two folders above this skill's base directory). If it isn't on PATH, run `uv run --project <factory repo> factory ...`.

## Steps

1. **Check the target repo opts in.** It needs `.factory/config.yaml` with at least `commands.test` and `test_globs`. If it's missing, show the user the example in the factory's README and stop; don't guess their commands.
2. **Get the story.** A markdown file saying what the change should do. If the user described it in chat, write it to a file outside `.factory/` and show it to them before running.
3. **Run it.** `factory run STORY.md --repo PATH`. It runs spec → triage → tests → build → triage → gate → review → warrant and stops at the first block. Builds and reviews can take many minutes; run it in the background and check on it rather than waiting in silence. The factory sandboxes its own legs and commands, and sandboxes can't nest: run the CLI outside your own Bash sandbox, or it refuses to run builder code and says so in the ledger.
4. **If it blocks,** read `.factory/changes/{id}/decisions-needed.md` and tell the user, plainly: what blocked, the evidence (ledger event ids, log paths), and the options it lists. Resume with `factory run --change ID --repo PATH` once they've chosen. `factory status --change ID --repo PATH` shows where each stage stands.
5. **When it finishes,** present `.factory/changes/{id}/warranty.md`: the status line, what was demonstrated, what is only asserted, gates passed/failed/skipped, review findings and their resolution, ratchet counts, whether the theory doc changed, and residual risks. Keep the pack's own split: never present a line from "Asserted, not evidence" as fact.

## Rules

- **Never sign, return or accept.** Those are the accountable person's step. Give them the exact command (`factory sign --change ID --by NAME`, `factory return --change ID --reason "..."`, `factory accept --change ID --item F1 --reason "..." --by NAME`) and let them run it. `factory sign` asks for the change id at a terminal and refuses to run headless.
- Don't edit anything under `.factory/`, `tests.lock`, or a locked test file. If a locked test looks wrong, say so; the fix is a new `factory tests` run the user approves.
- Don't summarise the builder's message as evidence. "The builder says all tests pass" is an assertion; the gate's run record is the evidence.
- Don't read the diff to reassure the user in place of the gates. If they want a second look, use the `independent-reviewer` agent in a fresh context.
