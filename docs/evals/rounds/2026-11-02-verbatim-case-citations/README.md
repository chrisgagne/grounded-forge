# Verbatim mode on the case-citations cases: does placing the authors' words lift citation support?

**Status: designed, not run.** Ready to run at `bca4b590`, which has the two generator fixes round 2 called for (below).

## Why this round

The [case-citations round](../2026-11-case-citations/) is the larger study of how well citations carry their claims:

- three practitioner cases, over a public and a private corpus, two runs each;
- about 1,500 citations;
- each graded by Claude scorers and re-graded by Sol, with 96% agreement on which citations miss.

19% of Gemini Notebook's markers carried their claim as stated; 83% of `answer-from-corpus`'s credits did.

Verbatim mode's [round 1](../2026-11-02-verbatim-vs-gemini/) and [round 2](../2026-11-02-verbatim-vs-gemini-2/) judged it against Gemini on a different rubric:

- one score per claim, not per citation marker;
- a split between support as delivered and support as recovered;
- six answers in all.

Their numbers can't be set beside the case-citations ones. This round adds verbatim mode as a third arm to the case-citations table: the same cases, the same unit of scoring, the same grade and the same two scorer families. The existing arms are reused as they are.

## Reused, not re-run

From the case-citations round:

- the cases and answer keys ([`cases.json`](../2026-11-case-citations/cases.json), [`keys.json`](../2026-11-case-citations/keys.json));
- the scoring brief (`scores/scoring-brief.md`);
- the tallying and cross-family scripts ([`summary.py`](../2026-11-case-citations/summary.py), [`compare_sol.py`](../2026-11-case-citations/compare_sol.py));
- every Gemini capture and every `answer-from-corpus` run with its scores, Claude's and Sol's. The public ones are in that folder. The private ones are under `/Users/Shared/aar-ab-runs/case-citations/` (`G/`, `aarbuddy-*.out/`, `scores-private/`, `scores-private-sol/`), reported as counts only, as there.

No Gemini question is asked again, and no `answer-from-corpus` answer is regenerated.

## The new arm

- **Runs.** `scripts/verbatim/generate.py --model opus --joins both`, with each case's prompt as the question, two runs per cell:

  | Case | Corpora |
  |---|---|
  | C1 | `demo`, `aarbuddy` |
  | C2 | `demo`, `aarbuddy` |
  | C3 | `aarbuddy` |

  That is 10 answers, matching `answer-from-corpus`'s cells. Record the generator commit before the first run, and change nothing in it until the last.
- **What is scored.** `answer.md` in its essay form, the closest to the memo C1 and C2 ask for.
- **The unit.** The case-citations unit, as its design states it: a sentence that credits a source by name or quotes it. In a verbatim answer that is each placed span, and each join sentence that credits a source.
- **Scorers.** Opus 5.5 in a fresh context, with the case-citations scoring brief unchanged, then a Sol re-grade of all 10 answers through `compare_sol.py`.
- **Private results** are reported as counts and kinds of failure only. No answer text, passage or quotation leaves the private tier.

## The two fixes round 2 called for, in place at `bca4b590`

1. **Every credited sentence carries a pointer.** In round 2, 22 of 54 attributed sentences on the Marines question had no pointer, because the model wrote them in its joins. Such a sentence is now a *pointed paraphrase*: the model's own sentence with an anchor, which the resolver places and points to. `generate.py` finds join sentences that credit a source, runs one repair pass on them, and stops on any credit left without a pointer. A fresh run on the Marines question had 12 pointed paraphrases and no credit left without a pointer.
2. **Placed quotations are checked against the page, not just the conversion.** Converter markup (table bars, Pandoc fences and blockquote markers) and run-in headings are left out of placed text. The renderer compares each quotation word for word with its page in the original. It sets a word the conversion split ("bet ter") as the page prints it, and records any other difference. The check reads the original's text layer, so an OCR slip the PDF's own text shares, like round 2's "AID" for "AND", goes uncaught. Report the page-check counts beside quotation exactness.

## Reading the result, stated before running

Per cell, compare verbatim mode's grades with `answer-from-corpus`'s on the same case and corpus. Gemini's are reported beside both.

- **Verbatim mode lifts citation support** if its share graded *supports* beats `answer-from-corpus`'s by 5 points or more in at least three of the five cells, with its *does-not-support* share no higher in any cell.
- **It holds level** if the *supports* shares are within 5 points in at least three cells. Verbatim mode's case then rests on how easily a reader can check its citations, which this rubric does not score.
- **It costs support** if it falls 5 points or more below in at least three cells.
- **Quotation exactness** is counted against the converted text, where verbatim mode is exact by construction, and against the printed page through the renderer's check, the stronger test.
- **Expected ideas** on C1 and C2 are reported beside `answer-from-corpus`'s. Building an answer around placed passages could cost coverage, and this would show it.
- Cost and time per answer.

## Limits, stated before running

- The case-citations round's caveats carry over: three cases and two runs; cases written with the corpora in view; Claude as case writer, scorer and arm.
- The reused arms ran on 31 October and 1 November 2026. The `aarbuddy` corpus has changed a little since, with two conversions repaired on 2 November. The result reports what changed, rather than re-running the old arms.
- Per-citation support favours an arm that cites less. Verbatim mode cites more densely than `answer-from-corpus`, so its counts are compared as shares, never as raw numbers.
