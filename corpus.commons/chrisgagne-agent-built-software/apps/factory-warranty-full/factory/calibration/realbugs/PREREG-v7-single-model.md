# Pre-registration v7: does the factory's review brief get more out of one model than that model's own review tool?

**Status:** approved by Chris Gagné (2026-10-20: "run on both sol and opus… how does it help each of those models
relative to their built-in tools?") and in effect from the commit that adds it, before the sample is drawn and before
any trial runs. Nothing below may change after that commit; a later change is a dated amendment that judges only later
runs.

## Why

v6 (`results/v6-RESULTS.md`) settled the two-model question: the factory reviews about as well as running both labs'
own review tools. Someone with only one model is asking a different question, and v5's diagnosis, after the fact on
data already seen, suggested an answer: the factory's brief on Opus found more high-severity findings than Claude Code's
plain review (18 against 13 of 36) at slightly lower recall, and on Sol it beat `codex review` on every measure, by small
margins. This tests that on pull requests nobody here has reviewed, chosen to contain serious findings, since v6's
sample held only 3.

## Sample

`pick_v7.py`, committed with this file and run once after it: every ReviewBench pull request (commit `12e9d1a`) outside
the test set, v5's cost probe and v6's sample, with at most 2,000 changed lines, whose golden set holds at least one
true finding of high severity. (Only that label is read, never a finding's content; at the time of writing 23
qualify.) The operator checks only that each pull request's commits can be fetched.

## Arms (one trial each; each judged on its own)

| Model | `factory brief` arm | `own tool` arm |
|---|---|---|
| Opus | the factory's Claude reviewer (`claude` leg, Opus, the factory's brief, grounded in the open 17-source build), its findings before the sort | Claude Code with the plain prompt (v5's and v6's), Opus |
| Sol | the factory's Codex reviewer (`codex` leg, gpt-6.1-sol, the factory's brief and grounding), its findings before the sort | OpenAI's `codex review`, gpt-6.1-sol |

The two factory legs come from one factory run with `review.legs: [claude, codex]` (the default) at the commit recorded
in `results/v7-factory.commit`; the two own-tool arms from the v5 runner's `vendors` arm, its Claude Code and Codex
findings separated. Before the sort, so each arm is one model's work: the sort is a Claude leg.

## What decides it (primary, per model)

1. **Overall:** the factory-brief arm did better than the own-tool arm only if its grounded precision and grounded
   recall (the judge's per-pull-request averages) are each at least as high and one is higher by at least 5 points;
   worse by the same rule the other way; otherwise about the same.
2. **Serious findings:** high-severity golden true findings found (grounded, distinct). The factory-brief arm found
   more only if at least 3 more of them; fewer by the same margin; otherwise about the same.

Reported as answered for each model separately: Opus, then Sol.

## Reported, not judged

Augmented precision and recall; findings per pull request; cost per arm; and, as before, nothing here is a leaderboard
score.

**Limits, stated before the run:** 23 pull requests, one trial, offline scores. Selecting pull requests with serious
golden findings makes high-severity recall measurable, and means these pull requests aren't typical. The judge is a
Claude model, and two of the four arms are Claude.

## Amendment 1, 2026-10-20 12:45 NZDT, after the runs, before the factory's two failed pull requests are re-run

Two factory runs failed for a reason unrelated to the review brief under test. Both projects lock thousands of test
files (rd12: 12,846), and the factory listed each one: in rd12 the gate's sandbox command passed the system's argument
limit before any review ran, and in rd13 the Claude reviewer's settings file passed Claude Code's 2 MiB limit, so that
leg didn't run. Fixed in factory `c722668` (the sandbox profile goes in a file with its rules split under the size
limit; above 1,000 locked paths, whole fully-locked folders are named once; read-only legs no longer carry the locked
list). **rd12 and rd13 are re-run in the factory arm on that commit**, and both factory-brief arms re-judged. The
primary result uses the re-runs; the results also give the score with the two failures counted as no findings, as
first judged. No other pull request, arm or rule changes; the operator has read no finding of either pull request.
