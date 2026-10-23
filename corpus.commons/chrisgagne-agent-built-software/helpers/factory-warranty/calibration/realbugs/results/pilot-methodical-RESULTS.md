# Methodical 0.11.0, three pull requests: an exploratory pilot

**Not a pre-registered comparison.** Three pull requests, one trial per arm, chosen as a pilot to decide whether a
full 23-pull-request run earns its cost. The numbers below do not belong in `v5-RESULTS.md` through
`v9-RESULTS.md`, and they were judged on the Claude Code CLI, which
[misses the calibration rule](cal-RESULTS.md) against the API judge the published tables used.

Both arms were judged by the same CLI-backed judge, so they can be read against each other. The baseline is v9's
`opus-plain` arm (Claude Code with a plain prompt) on the same three pull requests, judged in the calibration run.
Methodical ran at version 0.11.0 (`d2c1b3c`), five seats, its own routing.

| Arm | Grounded P | Grounded R | Augmented P | Augmented R | Findings | Matched TP | Novel TP | Serious TP |
|---|---|---|---|---|---|---|---|---|
| Methodical 0.11.0 | 80.6% | 51.2% | 79.5% | 82.6% | 116 | 20 | 72 | 4 |
| Claude Code, plain prompt | 94.4% | 55.3% | 89.7% | 61.4% | 28 | 19 | 6 | 2 |

By the harness's rule, **the plain prompt did better**: its grounded precision is 13.8 points higher and its
grounded recall 4.2 points higher. Methodical produced 4 times the findings and matched one more golden true
positive for it.

The augmented figures are where Methodical's volume shows: 72 of its 91 unmatched findings were classified as real
issues the golden set never flagged, against 6 of 9 for the plain prompt, which lifts its augmented recall to 82.6%
against 61.4%. Those findings sit at the bottom of the severity range (low-severity grounded precision 55.6%,
recall 34.3%), so what the extra spend buys is a long tail of real but minor observations, not the serious bugs the
corpus is built around. On serious golden findings Methodical matched 4 against the plain prompt's 2, out of 6 on
these three pull requests, which is too few to read anything into.

| | Methodical | Plain prompt |
|---|---|---|
| Cost to produce the reviews | $7.92 | $1.58 |
| Cost to judge | $5.95, 120 judge turns | nil: judged inside the calibration run |

Per pull request:

| Pull request | Methodical (P/R, findings, novel TP) | Plain (P/R, findings, novel TP) |
|---|---|---|
| CommunityToolkit/Maui#3181 | 78.6 / 75.0, 54, 31 | 83.3 / 87.5, 14, 2 |
| ComposioHQ/agent-orchestrator#1277 | 80.0 / 40.0, 29, 18 | 100.0 / 40.0, 6, 1 |
| EdV4H/usketch#534 | 83.3 / 38.5, 33, 23 | 100.0 / 38.5, 8, 3 |

## What it says about the full run

A 23-pull-request Methodical arm would cost roughly $60 to produce and 25 to 40 points of a weekly subscription
allowance to judge, on this pilot's rate of about 30 classifier turns per pull request. What it would buy is a
firmer version of a result this pilot already points at, and one the harness has now found three times: a
scaffolded review process does not beat a plain prompt on these corpora. The factory's own brief didn't
(`v9-RESULTS.md`), both labs' review commands at their default settings didn't, and Methodical doesn't here.

The five departures from Methodical as designed (no tests first, one round, no North Star, escalation `none`, and
our JSON list at the end) and the open questions for its author are in `../PILOT-methodical.md`. Its author has not
been asked yet, and a full run before those answers would risk measuring a misconfiguration rather than the tool.
