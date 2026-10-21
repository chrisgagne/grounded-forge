# Replay v6 results: varied review legs against the vendors' own tools, on fresh pull requests

Pre-registered in `../PREREG-v6-review-legs.md` (`b33bf86`); sample drawn by `../pick_v6.py` after that commit (20
ReviewBench pull requests outside the test set, at most 2,000 changed lines, `random.Random(20261019)`); scoring script
`../compare_v6.py` and driver committed before any trial (`02ed915`). Run 2026-10-19 23:55 to 2026-10-20 05:00, factory
`84da36e` with review legs `claude, claude-plain, codex-review`, grounded in the open (17-source) build, every
reviewer's own finding reported. Judged offline by ReviewBench's judge with Claude Sonnet 5. One trial per arm.

## The pre-registered test

| Arm | Grounded precision | Grounded recall | Augmented precision | Augmented recall | Findings per PR |
|---|---|---|---|---|---|
| `factory`: the factory's brief on Opus + plain Claude Code + `codex review`, then the sort | 80.6% | 64.1% | 86% | 82% | 15.1 |
| `control`: plain Claude Code twice + `codex review` | 80.2% | 62.1% | 89% | 82% | 15.7 |
| `vendors`: plain Claude Code + `codex review` | 81.3% | 56.9% | 86% | 69% | 8.1 |
| `pr-agent`: PR-Agent 0.48.0 on Claude Opus, plain-diff mode | 83.3% | 19.0% | 85% | 27% | 2.1 |

**As registered, no arm did better than another.**

- **Factory against vendors (primary): about the same.** The factory's grounded recall was 7.2 points higher, but its
  grounded precision was 0.7 points lower, and the rule needs both to be at least as high.
- **Factory against control: about the same** (within 2 points on both).
- **Control against vendors: about the same** (recall 5.2 points higher, precision 1.1 points lower).
- PR-Agent's precision was the highest and its recall far the lowest, so under the rule no arm counts as better than it
  either.

## What it means

v5's diagnosis, made after the fact on the 25 test-set pull requests, suggested the factory's brief added something a
plain review couldn't. On fresh pull requests, adding the factory's brief on Opus did about what adding a second plain
Claude Code review did: a few more points of recall, at the cost of nearly twice as many findings to read. Extra
reviews of any kind help a little; the brief isn't shown to be special.

These 20 pull requests hold only 3 high-severity golden findings, and every arm found all 3, so this sample can't say
anything about serious bugs. The judge classed 9 of the factory's findings outside the golden set as valid
high-severity issues (the augmented measure); that is reported, not judged.

## What went wrong in the harness, and what was done

- **One factory pull request (rc10) failed to apply its diff:** the base checkout converted line endings under the
  repository's own attributes. Fixed (`cecade5`: the checkout keeps bytes as committed), rehearsed, re-run, and the
  factory arm re-judged with it; the failed attempt is in `v6-factory/harness-errors/` and the first judging in
  `v6-factory/superseded-scoring/`. Without rc10 the factory scored 79% precision and 61% recall; the conclusion is the
  same. The other arms check out the repository and review it in place, so they weren't affected.
- **Judging the control timed out on one pull request** (the most findings to classify); re-run with a longer judge
  budget, resuming from the checkpoint.
- The factory's three legs reported their findings in a fixed order (factory brief first), and the judge credits a
  match to the first finding that makes it, so the factory's per-leg split in `v6-compare.txt` overstates the first
  leg; it isn't used.

## Cost

| | Claude | Codex | API credit |
|---|---|---|---|
| `factory` | $31.53 (plus the rc10 re-run) | `codex review` inside the factory | — |
| `vendors` | $7.36 | `codex review` | — |
| `control` (the second Claude review) | $7.82 | — | — |
| `pr-agent` | — | — | as in v5 |

Codex meter (Plus plan): week 22% → 27% for the whole run.

## Limits

20 pull requests, one trial, offline scores. The 2,000-line cap leaves out the largest pull requests. ReviewBench's
golden findings were mostly first raised by AI reviewers, labelled with a Claude classifier, and judged by a Claude
model, while most findings in every arm here were written by Claude models.

*Third-party home paths quoted in findings (a reviewed pull request's author's own `/Users/{name}/...`) are redacted
to `/Users/<author>/` in these records; nothing else in them is changed.*
