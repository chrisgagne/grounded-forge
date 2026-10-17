# Replay v4 results: did round two stop fewer good changes?

Pre-registered in `../PREREG-v4-false-stops.md` (`e3b63e3`, Amendment 1 `b271b27`, Amendment 2 `c30f72a`); cases
`../v4-cases.json` (`b07a7a3`), picked by Sol and committed before any trial; scoring script `../compare_v4.py`
(`d244f35`), committed before any trial was graded. Run 2026-10-16 13:40 to 20:55, the `v3` arm on factory `4e4dd14`
and the `v4` arm on `e3b63e3` (code identical to `3d12aac`), each from its own pinned checkout, both reading the
`factory-warranty` app built from grounded-forge `25a0cbb6`. 20 cases (8 bug, 12 control), 2 trials each, in each arm,
interleaved in batches of five cases. Graded blind by Sol (gpt-6.1-sol) against each bug's fix. Reported as it stands.

## The pre-registered test

| | `v3` arm | `v4` arm (round two) | Rule | Met |
|---|---|---|---|---|
| Good-change trials stopped (of 24) | 2 | 2 | `v4` at most half of `v3` (1), and at most 5 | no |
| Bug cases caught on both trials (of 8) | 7 | 7 | `v4` at least `v3` less one (6) | yes |

**Round two doesn't work, as pre-registered.** Round two's changes didn't measurably cut false stops without costing
catches: on these cases there was almost nothing to cut. Both arms stopped the same good change on both trials, caught
the same seven bugs on both trials and missed the same one.

**By Amendment 1 alone** (each trial whose outage re-run hit the outage again counted as a stop or a miss): `v3` 10 of
24 good-change trials stopped and 2 of 8 bugs caught on both trials, `v4` 8 and 4. The first criterion isn't met that
way either.

## What stopped the good changes

All four stops, two in each arm, are case w12: jsdiff `4428de9c`, upstream subject "Remove dead code", which deletes
`if (toPos < 0) { toPos = 0; }` from `applyPatch`. In every stop a reviewer rated it critical and named a trigger, as
round two's brief requires: a new-file hunk, `@@ -0,0 +1,4 @@`, now computes `toPos = -1`.

The operator checked that trigger after scoring by running jsdiff before and after the commit (`../w12-check/run.sh`):

| Input | Before | After |
|---|---|---|
| A parsed new-file patch (`@@ -0,0 +1,2 @@`) | correct | correct, identical |
| A parsed insert at the top of a file | correct | correct, identical |
| `structuredPatch`'s own hunk for a new file | starts at line 1 | starts at line 1 |
| A hunk object built by hand with `oldStart: 0` | `top`, `x`, `y` | `x`, `y`, `top` (wrong) |

`parsePatch` adds 1 to `oldStart` when the old side is empty, and `structuredPatch` never emits 0, so the guard can't
fire on any patch the library reads or makes. The reviewers traced the arithmetic from the header text and missed the
parser's adjustment. Only a hand-built hunk object reaches the changed behaviour. These are false stops; a named
trigger made the findings look evidenced without making them right.

## Reported, not judged

| | `v3` arm | `v4` arm |
|---|---|---|
| Review legs out of time | 0 | 0 |
| Confirmed findings naming a standard, source or library row | 30 of 56 (54%) | 31 of 55 (56%) |
| Claude review legs | $22.68 | $22.70 |
| Codex review tokens (excluding cached input) | 1,734,413 | 1,760,340 |

Codex's recorded token figure counts only non-cached input and output. Codex's own session logs show total use,
cached input included, running about ten times higher on comparable Sol work the same day.

**Against v3.** In the v3 replay the corpus arm, on the same `4e4dd14` factory, stopped 7 of 16 good-change trials
(44%). Here that factory stopped 2 of 24 (8%), under the proposed 20% bar. The cases differ and both samples are small,
so the false-stop rate depends on which changes are tested more than either run can pin down.

## Outages

Codex's five-hour usage limit ran out twice. Under Amendment 1 each outage trial was re-run once; under Amendment 2
each re-run that hit the outage again was run again once Codex answered: 15 trials in the `v3` arm and 11 in the `v4`
arm (records in each arm's `infra-failures-repeat/`). Every trial in the final count had a completed Codex review.
While pausing the run, the `v3` harness crashed tidying up two outage trials outside the batch it was running (w11-t1,
w12-t1); it had already moved them to `infra-failures/`, so they ran fresh with their batch, as Amendment 1 re-runs.

## A third model family on the grading (descriptive)

Sol picked the cases, reviews as one of the two reviewers and grades the bug trials. As a cross-check, TypeSafe's Jev
(`jev-1.13.0`) was asked the same question about every finding in every bug trial of v3 and v4
(`../jev_grade_check.py`, committed `4b4f946` before any Jev call; answers in `jev-check/`). Its answers change no
registered result; Sol's grade stays the registered one.

- **Finding by finding:** 212 of 250 agree (85%). Jev said a finding describes the bug 134 times, Sol 108; both 102.
  Jev is the more generous grader: 32 findings it matched Sol didn't, 6 the other way.
- **On what decides a catch** (a blocking finding that describes the bug): 95 of 97 trials agree. Both disagreements
  are case v06, where Jev counts a catch Sol didn't (`v3-none` trial 1, `v3-distillations` trial 2).
- **On every registered count:** identical. Bug cases caught on both trials: `v3-none` 11, `v3-distillations` 16,
  `v4-arm-v3` 7, `v4-arm-v4` 7, by either grader.

Jev's threshold (0.5) was set before the call. 247,384 Jev input tokens in all.

## Limits

12 good changes and 8 bugs are small samples: the test could show a large drop in false stops, and there was none to
show. Sol picked the cases and graded them; Jev agreeing is a second model, not a human check. The w12 check was run
by the operator after scoring, and only for w12.
