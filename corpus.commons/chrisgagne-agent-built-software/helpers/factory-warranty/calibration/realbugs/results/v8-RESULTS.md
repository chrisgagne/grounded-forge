# Replay v8 results: the factory's Claude reviewer against brooks-lint and Claude Code's `/code-review`

Pre-registered in `../PREREG-v8-other-reviewers.md` (`afb6d3b`, Amendment 1 `a59d96f`); v6's 20 pull requests;
scoring script `../compare_v8.py` and driver committed before any trial. Run 2026-10-20 on Claude Code 2.1.288, every
arm on Claude Opus 5.5. `factory-claude` and `plain` are v6's own findings (2026-10-19), judged here on their own for
the first time. One trial per arm, judged offline by ReviewBench's judge (Claude Sonnet 5).

## The pre-registered test

| Arm | Grounded precision | Grounded recall | Serious (of 3) | Findings per PR | Claude cost |
|---|---|---|---|---|---|
| `plain`: Claude Code with a plain review prompt | 81.3% | 56.2% | 3 | 7.6 | (v6) |
| `factory-claude`: the factory's brief and library | 78.2% | 47.5% | 3 | 7.1 | (v6) |
| `cc-review`: Claude Code's built-in `/code-review` | 74.5% | 18.7% | 2 | 2.7 | $6.25 |
| `brooks`: brooks-lint 1.8.0 `/brooks-review` | 72.2% | 13.7% | 0 | 5.3 | $10.71 |

- **Primary: the factory's Claude reviewer did better than brooks-lint** (precision 6.0 points higher, recall 33.8
  points higher) **and better than `/code-review`** (precision 3.7 points higher, recall 28.8 points higher).
- **The plain prompt did better than the factory's brief** (precision 3.1 points higher, recall 8.7 points higher),
  and better than both other tools.

## What it means

On Opus, the factory's brief and library add nothing over a plain "review this as a careful senior engineer" prompt;
here they cost recall. That matches v7, where Claude Code with the plain prompt found as much or a little more on 23
other pull requests. Against the two shipped tools, the factory's reviewer found two and a half to three and a half
times as much at higher precision.

Neither shipped tool is built for ReviewBench's answer key, which is mostly bugs. `/code-review` is built to report
only what it's sure of, and ran at its own "low" level on 14 of 20 pull requests ("medium" on 4, none recorded on 2);
it found about 3 issues per pull request. brooks-lint looks for maintainability risks (its six decay risks) and judged
most of what it raised by its books; the judge counted 81 of its 87 unmatched findings as true but outside the answer
key (augmented precision 87.9%, the highest of the four). So these numbers say how well each tool finds what
ReviewBench's key lists, not what each tool is worth.

## What went wrong in the harness, and what was done

- **The first 11 `/code-review` trials couldn't see the change** (Amendment 1): Bash was limited to commands starting
  with `git`, which refused `/code-review`'s own `git diff ... | tail` pipelines. They moved to
  `v8-cc-review/superseded-runs/` unjudged; both arms ran in full in Claude Code's sandbox. Every trial then ran a
  `git diff` that returned the change (checked in each log).
- **Commands refused along the way:** brooks-lint tried to write its score-history file after its report on 11 pull
  requests (the report was already written), read its own skill files with `cat` on 2 (it then used Read) and ran a
  command substitution on 1 (rc04). `/code-review` had a file read through `cd` and `sed` refused on rc04, and on
  rc13 was refused when it tried to build a test set-up outside the checkout. All are in the logs.
- **34 of brooks-lint's 106 findings named no file** its own parser (`report-parse.mjs`, which also feeds its SARIF
  output) could read; they name code by symbol. As pre-registered, they went on each change's first changed file.
  ReviewBench matches only within a file, so this can only lower brooks-lint's score. Best case, if each had matched a
  golden finding the arm missed, its recall would be 30.6%, still below the factory reviewer's 47.5%.

## Cost

Claude Code: $6.25 (`/code-review`, 20 minutes in all) and $10.71 (brooks-lint, 30 minutes). Judging four arms: API
credit, not metered per arm.

## Limits

20 pull requests already used in v6, one trial, offline scores, 3 serious golden findings in the sample. The judge is
a Claude model and every arm is Claude. `factory-claude` and `plain` ran a day earlier on an earlier Claude Code.
Neither shipped tool was given the pull request's title or description (neither takes one on a local branch); both saw
the commits. The `plain` and `factory-claude` reviewers were given them.

*Third-party home paths quoted in findings (a reviewed pull request's author's own `/Users/{name}/...`) are redacted
to `/Users/<author>/` in these records, after judging; nothing else in them is changed.*
