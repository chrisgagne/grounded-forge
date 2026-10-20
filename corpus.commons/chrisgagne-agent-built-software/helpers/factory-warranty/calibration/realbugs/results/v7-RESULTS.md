# Replay v7 results: does the factory's brief get more out of one model than its own review tool?

Pre-registered in `../PREREG-v7-single-model.md` (`685323f`, Amendment 1 `ac5f879`); sample drawn by `../pick_v7.py`
after that commit (all 23 ReviewBench pull requests outside the test set, v5's probe and v6's sample, at most 2,000
changed lines, whose golden set holds a true high-severity finding); scoring script `../compare_v7.py` and driver
committed before any trial (`bc239cb`). Run 2026-10-20 09:42 to 13:30, factory `bc239cb` with its default legs
(`claude`, `codex`) and the open (17-source) build; rd12 and rd13 re-run on `c722668` under Amendment 1. Each arm is
one model's findings, judged on its own by ReviewBench's judge (Claude Sonnet 5), offline. One trial per arm.

## The pre-registered test (with Amendment 1's re-runs)

| Model | Arm | Grounded precision | Grounded recall | Serious (high-severity golden) found | Findings per PR |
|---|---|---|---|---|---|
| Opus | factory's brief (its Claude reviewer, before the sort) | 87.2% | 45.1% | 28 | 10.4 |
| Opus | Claude Code, plain prompt | 87.2% | 49.6% | 29 | 10.0 |
| Sol | factory's brief (its Codex reviewer, before the sort) | 86.8% | 19.8% | 21 | 3.0 |
| Sol | `codex review` | 84.9% | 14.7% | 22 | 2.2 |

- **Sol: the factory's brief did better than `codex review`** (precision 1.9 points higher, recall 5.1 points higher).
  Serious findings: about the same (21 against 22).
- **Opus: about the same as Claude Code's own review.** Claude Code's recall was 4.5 points higher at the same
  precision, under the 5-point bar. Serious findings: about the same (28 against 29).

**As first judged** (before Amendment 1, the factory's two failed pull requests counted as no findings): Opus factory
brief 87.3% / 41.6%, 26 serious; Sol factory brief 85.6% / 18.4%, 20 serious. Under the rule, Opus about the same
overall and Claude Code found more serious findings (29 against 26, the 3-point margin); Sol about the same on both.
(`v7-compare-first-judging.txt`; the first judging is kept in each arm's `superseded-scoring/`.)

## What it means

v5's diagnosis, after the fact on seen data, suggested the factory's brief gets more serious findings out of a model
than its maker's own review. On fresh pull requests with serious findings in them, that held for neither model on
serious findings. Overall, the brief helped Sol, whose own review mode is sparse (about 2 findings per pull request),
and didn't help Opus, whose plain review already finds as much or slightly more.

So for someone with one model: on OpenAI's, the factory's brief is a measurable improvement over `codex review`; on
Anthropic's, Claude Code's own review is as good.

## What went wrong in the harness, and what was done

- **rd12 and rd13 failed in the factory arm** because both projects lock thousands of test files (rd12: 12,846) and
  the factory listed each one: the gate's sandbox command passed the argument limit (rd12), and the Claude reviewer's
  settings passed Claude Code's 2 MiB limit (rd13). Fixed in `c722668`, re-run and re-judged under Amendment 1; the
  failed runs are in `v7-factory/superseded-runs/`.
- Judging budgets were set long (3 hours) from the start after v6's timeout; no judging failed.

## Cost

| | Claude | Codex |
|---|---|---|
| Factory run (both legs, plus triage, sort and sheet) | $37.17 (plus the two re-runs) | the Sol leg |
| Own-tool runs | $9.63 (Claude Code) | `codex review` |

Codex meter (Plus plan): week 27% → 38% for the run.

## Limits

23 pull requests, one trial, offline scores. Pull requests were chosen because their golden sets contain serious
findings, so they aren't typical. The judge is a Claude model; two of the four arms are Claude. The factory's Claude
reviewer read the open build's library; Claude Code didn't, so "the factory's brief" here means the brief and its
grounding together.
