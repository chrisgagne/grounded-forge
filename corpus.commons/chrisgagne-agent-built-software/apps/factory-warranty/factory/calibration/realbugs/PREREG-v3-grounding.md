# Pre-registration v3: does the corpus help the reviewers?

**Status:** approved by Chris Gagné on 2026-10-15 and in effect from the commit that adds it, which comes before Sol picks
the cases and before any trial runs. Nothing below may change after that commit; any later change is an amendment,
dated, with its reason, and judges only runs after it.

## Why this test exists

The axis spec's success criterion (a) says: on the seeded-defect fixtures, a reviewer that consults the axis catches
more planted defects than the same reviewer without it; if not, the axis is shelf material and the gates carry the
warranty on their own. On 2026-10-11 all three groundings (none, seed rows, distillations) caught 10 of 10 planted
defects with no false alarms (`../report-2026-10-11-*.md`). That is a ceiling: the fixtures were too easy to tell the
groundings apart, so criterion (a) is unanswered, not passed and not failed. This test asks the same question on
harder material: real bugs from open-source history, which the reviewers have never seen.

## Cases

New cases, picked by Sol (GPT-6.1) with the brief `pick-cases.md` adapted as follows. The builder and the operator
don't choose cases.

- **17 BUG and 8 CONTROL** cases from the same eight projects (one control and two or three bugs per project), none of the commits already used in `tuning.json`,
  `heldout.json` or `fresh-controls.json`. Same rules for what counts as a bug fix or a clean change, same size limits
  (at most 3 code files; at most 40 changed lines for bugs, 60 for controls), same neutral story.
- No split: every case runs in both arms.
- The operator checks only that each case builds and applies, and reads nothing else about it before the run.

## Arms

The same 25 cases, 2 trials each, in each arm, on one factory commit recorded beside the results:

| Arm | Review grounding |
|---|---|
| `none` | The reviewers get the change and the project, no corpus |
| `distillations` | The reviewers may open the open corpus's distillations (`factory-warranty` app, built from `corpus.commons/chrisgagne-agent-built-software/` at a recorded commit) |

100 trials in all. Scoring rules and Amendment 1 (outage re-runs) as in `PASS-MARK.md`. Codex is the second
reviewer in both arms; the arms run interleaved, not one after the other, so a Codex outage or model change hits both.

## What decides the question (primary)

**Criterion (a) is met** if the `distillations` arm catches every time (2 of 2 trials) **at least 3 more of the 17 bug
cases** than the `none` arm, **and** its controls aren't worse: at most 1 more control case with a false alarm in any
trial.

**Otherwise it is not met**, and the README says, in these words or plainer: "By the test we set ourselves, the corpus
didn't measurably help the reviewers catch real bugs." A result in the other direction (`none` catches more) is
reported the same way, as it stands.

**Its limits, stated before the run:** 17 bug cases is a small sample. A difference of 3 can come from chance, and no
difference can hide a small real effect. The test can show a large effect; it can't rule out a small one. Two
trials per case, not three, buys more cases for the same budget: the comparison between arms gains more from cases
than from repeats.

## What else is reported (secondary, descriptive)

- **Citations:** in each arm, the share of confirmed findings that name a standard, a corpus source or an axis row.
  The expected direction is higher with the corpus. No pass mark: it's reported as measured.
- **Pass mark v2** (`pass-mark-v2.yaml`) applied to each arm separately, with its pass^k measures read at k = 2. Two
  of two is an easier bar than three of three, so these figures don't compare directly with earlier runs; the report
  says so beside them. The `distillations` arm is the configuration the factory ships with.
- **Cost:** Claude dollars and Codex tokens per arm.

## Budget

About 4M Codex tokens, run across several usage windows at `--jobs 2`; a window that runs out mid-trial is an outage
under Amendment 1, re-run, not scored.
