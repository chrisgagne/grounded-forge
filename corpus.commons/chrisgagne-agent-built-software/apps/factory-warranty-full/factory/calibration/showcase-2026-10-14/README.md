# Showcase: a change taken from story to signature (2026-10-14 to 15)

The job is the same as the first real job's (`../first-job-2026-10-14/`): a pinned semgrep rule that flags `eval`, the
`Function` constructor and Python's `exec` when the argument is text built at run time (`story.md`). This time the
accountable person, Chris Gagné, read each decision page, sent the change back twice in his own words, and signed the
third pack. It ran on a throwaway clone of this repo with `config.yaml` as the target's factory config. The signed
change is `change.patch`, applied here with `git am` and the full suite green (243 tests).

## What happened

| Run | Stopped at | Why | What followed |
|---|---|---|---|
| 1 | review | A reviewer rated F1 high, and the sort lowered it to medium: the Python rule flagged fixed text written as a raw or triple-quoted string. The sort may not clear a reviewer's high on its own, so it came to Chris | **Returned (e066):** "It flags fixed text it shouldn't. Do what the story says…" |
| 2 | tests | The spec amend pointed its new criteria at test files already locked, and the guard blocked the tests leg from adding to them | Factory fix `9aeb1fc`: new criteria name new test files; a send-back stays open until its tests lock |
| 3 | review | F1, high from a reviewer: the JavaScript rule's header claimed to catch `eval` "however reached" and missed `eval.call`, `Reflect.apply` and other forms | **Returned (e145):** "Don't claim more than it catches…" Factory fix `9a1c5cf`: a clean rebuild had left a stale guard record that read as tampering |
| 4 | review | A medium finding blocked because triage put the change in the irreversible class, on the word "Drop" in the spec leg's own note | Factory fix `ad290a0`: triage reads the criteria, not the spec leg's notes |
| 5 | — | Re-check of triage, gate and review: READY TO SIGN | **Signed (e246)** |

Each send-back went through the spec and tests stages before the rebuild: new criteria were added with the old ones
kept word for word (`acceptance-locked.md` is the set as locked), and their tests were written and seen to fail
before the builder ran. The change ends with 27 criteria, each with a test that failed before the build and passes
after it.

## What the signer carried

The signed pack (`warranty.md`) lists four minor points below the bar, in the reviewers' words: the conformance
records still called the rule unbuilt (now updated in this repo); a `Function` alias declared with its value and
`(function(){}).constructor(x)` are neither flagged nor named in the rule's "not followed" list; and the reviewers
disagreed on whether `const code = "1+1"; eval(code)` is flagged. No pattern-matching rule follows every alias, so
the rule says what it doesn't follow instead of claiming it catches everything.

## Cost

Across the five runs: Claude legs $9.43 (spec $0.88, tests $2.58, build $1.62, Claude reviewer $3.02, sort $1.34) and
213,953 Codex reviewer tokens.

## Files

`story.md`, `acceptance.md` (the 27 criteria), `acceptance-locked.md`, `config.yaml`, `ledger.json` (246 hash-chained
events, the returns and the signature among them), `warranty.md` (the signed pack, decision page first), `change.patch`,
and `run1.log` to `run5.log`.

## One file changed after the run

`config.yaml`'s two axis lines (`axis_spec`, `axis_index`) were rewritten to the open corpus after the run, so the
hash event e001 recorded for it no longer matches; the run read seed rows from an earlier version of this axis spec.
Nothing else in the folder was changed, and `ledger.json` verifies end to end.

Commit ids cited here (factory commits, not grounded-forge's) are from the factory's history before it was published.
