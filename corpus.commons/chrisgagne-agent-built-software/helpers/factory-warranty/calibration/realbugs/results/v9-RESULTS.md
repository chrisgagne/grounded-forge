# Replay v9 results: the factory's brief against a plain prompt on Sol, and both labs' review commands at higher effort

Pre-registered in `../PREREG-v9-plain-and-built-in.md` (`5163310`, Amendment 1 `beb52d4`); v7's 23 pull requests; scoring script
`../compare_v9.py` and driver committed before any trial. Run 2026-10-21 on Claude Code 2.1.288 and Codex CLI
0.162.0-alpha.17.2. The four v7 arms are reused as judged in v7. One trial per arm, judged offline by ReviewBench's
judge (Claude Sonnet 5).

## The pre-registered test

| Model | Reviewing with | Grounded precision | Grounded recall | Serious found (of 48)\* | Findings per PR |
|---|---|---|---|---|---|
| Sol | the factory's brief and library (v7) | 86.8% | 19.8% | 20 | 3.0 |
| Sol | a plain prompt | 85.4% | 22.1% | 26 | 3.8 |
| Sol | a plain prompt, reasoning effort "high" | 86.0% | 28.4% | 30 | 5.4 |
| Sol | `codex review` (v7) | 84.9% | 14.7% | 22 | 2.2 |
| Sol | `codex review`, reasoning effort "high" (Amendment 1) | 89.8% | 22.1% | 27 | 3.5 |
| Opus | the factory's brief and library (v7) | 87.2% | 45.1% | 28 | 10.4 |
| Opus | Claude Code with a plain prompt (v7) | 87.2% | 49.6% | 30 | 10.0 |
| Opus | Claude Code's `/code-review` | 84.7% | 26.6% | 25 | 4.3 |
| Opus | `/code-review high` | 87.8% | 46.2% | 28 | 9.8 |
| Opus | `/code-review xhigh` | 82.7% | 55.9% | 34 | 14.4 |

\*High-severity golden findings matched as true, the pre-registered count (v6's). v7 counted any match to a true
high-severity golden finding; by that count the reused arms are 21, 22, 28 and 29 (as in v7), and the new ones 26,
30, 25, 29 and 34 (`codex review` at "high": 27). The order is the same.

**Primary:**

1. **Sol: the factory's brief and a plain prompt came out about the same.** The plain prompt's recall was 2.3 points
   higher and its precision 1.4 points lower, and it found more serious bugs (26 against 20).
2. **Opus: the plain prompt did better than `/code-review` at its default** (precision 2.5, recall 23.0 points higher),
   and about the same as `/code-review high` and `/code-review xhigh`. `xhigh` traded 4.5 points of precision for 6.3
   of recall and found the most serious bugs of any arm (34 against the plain prompt's 30).

Also by the rule: Sol at "high" effort did better than Sol with a plain prompt at the default and than `codex
review`; `/code-review high` did better than `/code-review` at its default. Opus with the brief, with the plain prompt
and with `/code-review high` each did better than every Sol arm; `xhigh`'s lower precision kept it from clearing the
rule against them.

**Amendment 1, `codex review` at "high"** (comparisons chosen after seeing the results above): it did better than
`codex review` at its default (precision 4.9, recall 7.4 points higher), and came out about the same as Sol with the
factory's brief (precision 3.0, recall 2.3 points higher) and as Sol's plain prompt at "high" (precision 3.8 higher,
recall 6.3 lower).

## What it means

**The factory's brief doesn't beat a plain prompt on either model.** v7's finding that it beat `codex review` on Sol
says more about `codex review` (about 2 findings per pull request) than about the brief: a plain prompt beat `codex
review` too. On Opus, v7 and v8 already showed the plain prompt as good or better. The brief's wins over PR-Agent,
brooks-lint, `codex review` and `/code-review` at its default are wins over tools that hold the model back, not
evidence that the brief adds anything.

**Effort matters more than the brief.** Every Sol run before v9, the factory's leg included, ran at the Codex CLI's
default reasoning effort, which it reports as "none". At "high", Sol's plain prompt found 6.3 more points of recall and
4 more serious bugs. Both labs' review commands are held back by their defaults: `/code-review` picks a low level,
and at `high` it matches the plain prompt, at `xhigh` it finds the most serious bugs, for about four times the plain
prompt's cost; `codex review` at "high" beats its own default and draws level with the factory's brief.

## What went wrong in the harness, and what was done

- Judging `sol-plain-high` failed once and passed on the driver's retry.
- `/code-review xhigh` on rd11 ran 14 minutes; a tool call inside it timed out, and the review finished.
- Every run completed and was read: no timeouts, no unreadable answers, every Sol run at its intended effort.

## Cost

| Arm | Claude | Codex |
|---|---|---|
| `/code-review` (default) | $8.78 | |
| `/code-review high` | $15.36 | |
| `/code-review xhigh` | $38.10 | |
| Sol plain, default and "high" | | Plus meter: week 2% → 18% for both arms |
| `codex review` at "high" (Amendment 1) | | Plus meter: week 18% → 28%; the 5-hour limit stopped it after 19 pull requests, and the last 4 ran once it reset |

The v7 plain Claude Code arm cost $9.63 on the same 23 pull requests.

## Limits

23 pull requests chosen for their serious findings and already used in v7; one trial; offline scores. The judge is a
Claude model. The v7 arms ran a day earlier on earlier CLI versions. The factory's brief was not run at Sol's "high"
effort, so this doesn't show whether the brief helps a model that reasons more. Claude Code's own effort for the
plain arm was the CLI's default.

*Third-party home paths quoted in findings (a reviewed pull request's own `/Users/{name}/...`, including test
fixtures) are redacted to `/Users/<author>/` in these records, after judging; nothing else in them is changed.*
