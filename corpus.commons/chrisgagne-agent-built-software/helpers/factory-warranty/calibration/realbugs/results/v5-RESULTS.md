# Replay v5 results: the factory against open prior art

Pre-registered in `../PREREG-v5-head-to-head.md` (`68367e2`, Amendment 1 `e2aa948`): part A, ReviewBench's 25-pull-
request test set (GitHub, MIT, commit `12e9d1a`), judged offline by ReviewBench's own judge with the leaderboard's
judge model, Claude Sonnet 5; part B, 15 good changes picked by Sol (`v5-controls.json`, `d400274`). One trial per arm.
Scoring script `../compare_v5.py` (`dd3edc3`), committed before any arm was judged. Run 2026-10-19, factory at
`507dd37` (the open, 17-source build and the wider review brief, which passed its check, `../CHECK-v5-wider-brief.md`).
Offline scores: ReviewBench says they can't be published as leaderboard scores, and they aren't.

## Part A: ReviewBench test set

| Arm | Grounded precision | Grounded recall | High-severity golden found (of 36) | Findings per PR |
|---|---|---|---|---|
| `vendors`: `codex review` + Claude Code (Opus 5.5, plain prompt), pooled | 87% | 51% | 25 | 12.8 |
| `factory`: Claude (Opus) + Sol reviewers with the factory's brief, then its sort | 86% | 35% | 19 | 9.8 |
| `pr-agent`: PR-Agent 0.48.0, plain-diff mode, Claude Opus via the API | 82% | 14% | 8 | 2.4 |

Per-pull-request averages, as the scoring script reads them; pooled across all findings they differ by up to four
points. **As registered: the factory did better than PR-Agent; the vendors arm did better than the factory and than
PR-Agent.**

## Part B: 15 good changes

| | `factory` | `vendors` | `pr-agent` |
|---|---|---|---|
| Good changes stopped | 2 | 4 | 7 |

**As registered: the factory and the vendors arm each stopped fewer than PR-Agent; factory against vendors is about
the same (a difference of 2, under the bar of 3).** PR-Agent's count depends on our stop rule (any "key issue to
review"), which it reports on most changes.

## Diagnosis after the fact (descriptive, not registered)

Every reviewer's raw findings from the factory arm were kept (`v5-a-factory/raw-reviewers/`) and judged the same way
(`v5-a-factory-raw-*`). Recomputed from the judge's per-finding decisions:

| | Precision | Recall | High-severity found | Findings per PR |
|---|---|---|---|---|
| Opus, factory's brief | 87% | 38% | 18 | 9.8 |
| Opus, plain Claude Code | 87% | 42% | 13 | 10.8 |
| Sol, factory's brief | 92% | 16% | 15 | 2.9 |
| Sol, `codex review` | 87% | 11% | 14 | 2.0 |
| Factory, both reviewers before its sort | 87% | 40% | 21 | 12.7 |
| Factory, after its sort | 86% | 37% | 19 | 9.8 |
| Vendors, pooled | 87% | 52% | 25 | 12.8 |

- Each model found more high-severity findings under the factory's brief than under its vendor's own review.
- The factory's two reviewers, given the same brief, overlapped: pooled they recall 40%, against 52% for the two vendor
  tools, whose findings barely overlap (of the golden findings the vendors arm found, 131 came from Claude Code alone,
  30 from `codex review` alone, 10 from both).
- The sort, by merging findings, cost about 3 points of recall and 2 high-severity findings.
- Pooling the factory's Opus reviewer with Claude Code and `codex review` would have found the most (58% recall, 26 of
  36 high-severity). Whether that is "different ways of asking" or "more reviews" these data can't say.

These cuts were chosen after seeing the results, on the same 25 pull requests. They shaped the factory's next version
(`review.legs`, factory `d54718d`), which PREREG-v6 tests on pull requests nobody here has reviewed.

## Cost

| | Claude | Codex | API credit |
|---|---|---|---|
| `factory` (part A) | $39.01 | 1,563,378 tokens recorded (excluding cached input) | — |
| `vendors` (part A) | $13.00 (Claude Code) | not recorded by `codex review` | — |
| `pr-agent` (part A) | — | — | 614,241 tokens |

Codex meter (Plus plan) for the evening's runs: week 12% → 22%.

## What went wrong in the harness, and what was done

- **Judge settings.** The first judging failed on every pull request: the judge's model library sent a thinking
  setting Claude Sonnet 5 rejects. Fixed with the library's own `compat.forceAdaptiveThinking`; every score above comes
  from the clean run. Later judging runs hit dropped API connections and were re-run; the judge resumes from its
  checkpoint.
- **Two factory pull requests (rb21, rb23)** couldn't apply their diffs: the base tree came from `git archive` (which
  drops export-ignored files) and the fixture's first commit applied the project's `.gitignore` and line-ending rules.
  Both fixed (factory `44eef25`, `7439a03`); the failed attempts are in `v5-a-factory/harness-errors/`; the other arms
  check out the repository directly and weren't affected.
- **One factory review leg malfunctioned (rb10)** and stands as recorded.
- **Bare reviewers' time limit.** The runner first gave the bare reviewers 30 minutes, and plain Claude Code ran past
  it on the first pull request; they now get the factory's 60, and a timeout is recorded rather than crashing the run
  (`e0733b1`), before any vendors trial was recorded.
- **One malformed item.** Claude Code's answer for rb04 had one malformed JSON item; the runner now reads answers item
  by item (`f945051`), decided before any vendors finding was judged, and rb04 was re-read from its saved log.
- **Disclosure.** While testing the scoring script, part B's partial results printed (PR-Agent had stopped 2 of its
  first 5 good changes). The script was already written; nothing in it changed.

## Limits

One trial per arm; 25 pull requests and 15 good changes; offline scores. ReviewBench's golden findings were mostly
first raised by AI reviewers and labelled with a Claude classifier, and the judge is a Claude model, grading arms whose
findings are mostly Claude-written. PR-Agent ran in its local plain-diff mode, which sees the diff but not the
repository; the factory's reviewers read the whole codebase. Part B's stop rules for the other arms are our reading of
their output.
