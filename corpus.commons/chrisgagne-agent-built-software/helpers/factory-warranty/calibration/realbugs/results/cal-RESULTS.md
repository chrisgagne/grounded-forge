# Judge calibration: the Claude Code CLI against the Anthropic API

Pre-registered in `../PREREG-judge-calibration-2026-10-22.md` before the run. Five pull requests (rd01 to rd05 of
v9's `opus-plain` arm, 45 findings), re-judged 2026-10-22 with ReviewBench's own judge driven through `claude -p`
instead of the Anthropic API. Same judge model, prompts, chunking and scorer; the adapter and the wiring patch are
in `../judge-cli/`.

## Result: it misses the pre-registered rule

| Judge | Grounded precision | Grounded recall | Candidates | Matched TP | High-severity TP |
|---|---|---|---|---|---|
| Anthropic API | 96.1% | 58.7% | 45 | 30 | 4 |
| Claude Code CLI | 87.8% | 58.7% | 45 | 29 | 4 |

Precision is 8.3 points lower and recall identical. The rule asked for both within 5 points, so **the CLI-backed
judge may not stand in for the API judge**, and CLI-judged numbers must not be put beside the API-judged ones in
`v5-RESULTS.md` through `v9-RESULTS.md`.

Per pull request:

| Pull request | API (P/R) | CLI (P/R) |
|---|---|---|
| CommunityToolkit/Maui#3181 | 91.7 / 87.5 | 83.3 / 87.5 |
| ComposioHQ/agent-orchestrator#1277 | 100.0 / 40.0 | 100.0 / 40.0 |
| EdV4H/usketch#534 | 100.0 / 38.5 | 100.0 / 38.5 |
| FreeRTOS/FreeRTOS-Kernel#1379 | 100.0 / 66.7 | 66.7 / 66.7 |
| Mirkiux/featkit#17 | 88.9 / 61.1 | 88.9 / 61.1 |

## Where the two judges differ

The two judges scored **42 of the 45 findings the same way**. Two of the three disagreements are the matcher
choosing a different golden finding for the same candidate, not the classifier changing a verdict:

1. **Maui#3181, `MediaElementFromStreamPage.xaml.cs:55`** (unhandled `async void` exception). The API judge matched
   it to a golden finding the corpus labels true; the CLI judge matched it to a different golden finding the corpus
   labels false. Matched true positive becomes matched false positive.
2. **FreeRTOS#1379, `tasks.c:5500`** (the same before-and-after check in `xTaskRemoveFromEventList`). The API judge
   found no golden match and its classifier called the finding a novel true positive; the CLI judge matched it to a
   golden finding labelled false.
3. **Maui#3181, `MediaSourceConverter.shared.cs:57`** (the converter no longer round-trips). Neither judge matched
   it; the API classifier called it a false positive and the CLI classifier a true one. This is the only
   classifier-only disagreement, and it moves precision the other way.

Two of the five pull requests carry the whole gap, and `FreeRTOS#1379` has 3 candidate findings, so one changed
verdict there moves its precision 33 points. The macro average is the mean of five such numbers.

## Cost and time

5 pull requests, 45 findings, concurrency 2: **5 minutes 22 seconds** wall clock, and the weekly subscription
allowance went from 61% to 62%, which includes the session that drove the run. A 23-pull-request arm should
therefore cost about 4 to 5 points of a week. ReviewBench records the candidate's cost but not the judge's; the
adapter now appends each turn's cost to `scoring/cli-cost.jsonl`, so later runs carry their own figure. This run
has no such file, and the meter delta is all it has.

The classifier used its tools in every pull request (Read, Grep and Glob, 3 to 24 calls each), so it was reading the
checkout rather than answering from the diff alone.

## Limits

Five pull requests, one arm, one trial, and a Claude model judging Claude's findings on both sides. The
pre-registration was written before the run but **committed after it**, with the comparison script written while the
run was going, before any score was read. The rule, the five pull requests and the threshold are as they were
typed before launch, and the git history cannot show that; a reader is entitled to discount it.

## What follows

Comparisons have to stay inside one judge. New work can be judged on the CLI as long as every arm in the comparison
is judged the same way, and the published v5 to v9 tables stay closed: a new arm cannot be added to them without the
API judge, and there is no API credit to do that with.
