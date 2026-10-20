# Pre-registration v6: do varied reviewer legs make the factory a better reviewer than the vendors' own tools?

**Status:** approved by Chris Gagné (2026-10-19: "go, with codex review") and in effect from the commit that adds it,
before the sample is drawn and before any trial runs. Nothing below may change after that commit; a later change is a
dated amendment that judges only later runs.

## Why

In v5 (`PREREG-v5-head-to-head.md`, `results/`), on ReviewBench's test set, running OpenAI's `codex review` and Claude
Code bare and pooling their findings found more than the factory (grounded recall 51% against 35%; 25 of 36
high-severity golden findings against 19). A diagnosis after the fact, on the same 25 pull requests, found:

- each model found more high-severity findings under the factory's brief than under its vendor's own review (Opus 18
  against 13; Sol 15 against 14), but the factory's two reviewers, given the same brief, overlapped: pooled they found
  less than the two vendor tools, whose different review modes barely overlap;
- the factory's sort, by merging findings, lost about 3 points of recall and 2 high-severity findings;
- pooling the factory's Opus reviewer with Claude Code and `codex review` found the most (58% recall, 26 of 36).

So the factory now has `review.legs` (factory `d54718d`): `claude` (the factory's brief), `claude-plain` (Claude Code,
the plain prompt v5's bare arm used) and `codex-review` (OpenAI's own `codex review`), and sorted items keep every
reviewer's own finding. Those after-the-fact numbers come from data already seen; this test uses pull requests nobody
here has reviewed. It also separates "different ways of asking" from "more reviews": a control adds a second plain
Claude Code run to the vendor pair, so it has as many reviews as the new factory.

## Sample

`pick_v6.py`, committed with this file and run once after it: from ReviewBench's full set at commit `12e9d1a`,
excluding the 25 test-set pull requests and v5's cost probe, those with at most 2,000 changed lines, 20 drawn with
`random.Random(20261019)`. The operator reads nothing of the golden findings and checks only that each pull request's
commits can be fetched.

## Arms (one trial each)

| Arm | What runs |
|---|---|
| `factory` | The factory at the commit recorded in `results/v6-factory.commit`, review legs `claude, claude-plain, codex-review`, grounded in the open (17-source) build, as in v5 otherwise. Reported: every reviewer's own finding (`V5_REPORT=members`), whatever the sort's verdict |
| `vendors` | As v5's `vendors` arm: `codex review` and Claude Code with the plain prompt, pooled |
| `control` | The `vendors` arm's findings plus a second, separate Claude Code plain-prompt run on the same pull request |
| `pr-agent` | As v5's `pr-agent` arm |

Same runner (`runner-v5/`, extended to this sample), same judge: ReviewBench's own `npm run judge` with Claude Sonnet 5.

## What decides it (primary)

The same rule as v5: the `factory` arm did better than another arm only if its grounded precision and grounded recall
(the judge's per-pull-request averages) are each at least as high and one is higher by at least 5 points. Otherwise
"about the same on these pull requests".

Primary: `factory` against `vendors`. Also reported against the same rule: `factory` against `control` (does the
factory's mix beat as many plain reviews?) and `control` against `vendors` (does a second plain review alone add?).

## Reported, not judged

High-severity golden findings found, per arm; findings per pull request; cost per arm (Claude dollars, API credit, Codex
tokens recorded and the Codex meter); each `factory` leg alone, scored from the judge's per-finding decisions.

**Limits, stated before the run:** 20 pull requests, one trial, offline scores; the 2,000-line cap leaves out the
largest pull requests; the judge is a Claude model and most findings in every arm are written by Claude models; the
factory's design was chosen from v5's data, which this sample doesn't share.
