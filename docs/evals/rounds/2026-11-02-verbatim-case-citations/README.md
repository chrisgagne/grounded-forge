# Verbatim mode on the case-citations cases: does placing the authors' words lift citation support?

**Status: run on 2 November 2026.** Results [below](#results). On the reading fixed before running, verbatim mode **holds level** with `answer-from-corpus` on citation support: 93–98% of its citations carry their claim as stated, against 88–98%, with no citation graded *none* in 236. It covers fewer of the expected ideas on C2.

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

## Results

Run on 2 November 2026, all ten answers in one afternoon. Every number here is rebuilt by the case-citations round's [`summary.py`](../2026-11-case-citations/summary.py) and [`compare_sol.py`](../2026-11-case-citations/compare_sol.py) from the score files. Those files, the packets and the reports stay outside the repo (`/Users/Shared/aar-ab-runs/case-citations/round3-vm/` and `corpus.local/aarbuddy/projects/verbatim-reports/round3/`), the public ones with the private, so this folder carries no answer text from either corpus.

### How it ran

- **Generator.** `generate.py`, `resolve.py`, `render.py`, `template.html` and `contract.md` as at `bca4b590`, run from the main checkout's copy because `corpus.local/` lives there. The copy was compared file by file with the branch before the first run and again after the last. `flatten.py`, which writes `answer.md`, was changed in that copy minutes before the first report rendered (it is `d819d80f`'s version). For the essay form the change is whitespace only: re-flattening all ten bundles with `bca4b590`'s `flatten.py` gives byte-identical answers for nine, and for the tenth (demo C2-1) the same text with a space after five lead-in colons.
- **Questions.** Each case's prompt from `cases.json`, word for word, through `--model opus --joins both`, two runs per cell, one or two at a time.
- **Scorers.** Ten Opus 5.5 agents at effort high, one per answer in a fresh context, then Sol (`gpt-6.1-sol`, effort high, `codex exec -s read-only`) on all ten. Both families read the case-citations brief unchanged, plus a note on how its unit maps onto a verbatim answer:
  - each numbered pointer is one citation, with any lead-in that runs into it;
  - any other sentence that credits or quotes a source is one more;
  - the two calls the brief leaves open, settled the strict way, as for that round's single-packet scorers.
- **One ruling made during scoring.** Sol's first pass on demo C1-1 counted the ingestion candidates in the coverage note (books the corpus lacks) as unpointed credits and graded them *none*. The Opus scorers had read them as naming no source for a claim. The note then said so for every later scorer of both families, and Sol's demo C1-1 grade was re-run under it; the superseded file is kept beside the others. `answer-from-corpus`'s answers have no coverage note, so this sets no precedent against them.
- **The corpus since the reused runs.** The two `aarbuddy` conversions repaired on 2 November (Almaas, Dörner) appear in none of the ten reports.

### Citation support, cell by cell

Pooled over each cell's two runs. *Supports* is the share whose cited passage carries the claim as stated; *none* is U, the case-citations round's number. `answer-from-corpus` and Gemini are that round's grades, unchanged; for Gemini, the chat condition and, where it had citations, the as-asked one.

**Claude scorers (the primary grade):**

| Case | Corpus | Verbatim mode: citations, supports, partial, none | `answer-from-corpus` | Supports, verbatim minus `answer-from-corpus` | Gemini: supports, none |
|---|---|---|---|---|---|
| C1 | demo | 48: 46 (96%), 2, 0 | 75: 71 (95%), 4, 0 | +1.2 | chat 52/222 (23%), 27 (12%) |
| C2 | demo | 54: 52 (96%), 2, 0 | 100: 95 (95%), 4, 1 | +1.3 | chat 104/182 (57%), 4 (2%) |
| C1 | aarbuddy | 52: 50 (96%), 2, 0 | 64: 56 (88%), 8, 0 | **+8.7** | chat 40/296 (14%), 21 (7%) |
| C2 | aarbuddy | 40: 39 (98%), 1, 0 | 101: 99 (98%), 2, 0 | −0.5 | as asked 57/239 (24%), 7 (3%); chat 30/162 (19%), 3 (2%) |
| C3 | aarbuddy | 42: 39 (93%), 3, 0 | 89: 82 (92%), 7, 0 | +0.7 | as asked 61/138 (44%), 8 (6%); chat 28/270 (10%), 39 (14%) |

**Sol re-grade:**

| Case | Corpus | Verbatim mode | `answer-from-corpus` | Supports, verbatim minus `answer-from-corpus` | Gemini: supports, none |
|---|---|---|---|---|---|
| C1 | demo | 47: 44 (94%), 3, 0 | 78: 68 (87%), 10, 0 | +6.4 | chat 48/222 (22%), 15 (7%) |
| C2 | demo | 55: 48 (87%), 7, 0 | 116: 95 (82%), 20, 1 | +5.4 | chat 21/182 (12%), 9 (5%) |
| C1 | aarbuddy | 51: 48 (94%), 3, 0 | 70: 54 (77%), 16, 0 | +17.0 | chat 68/296 (23%), 15 (5%) |
| C2 | aarbuddy | 40: 37 (92%), 3, 0 | 119: 111 (93%), 8, 0 | −0.8 | as asked 57/239 (24%), 5 (2%); chat 39/162 (24%), 2 (1%) |
| C3 | aarbuddy | 42: 37 (88%), 5, 0 | 96: 70 (73%), 25, 1 | +15.2 | as asked 22/128 (17%), 5 (4%); chat 37/270 (14%), 18 (7%) |

Pooled over all five cells, 96% of verbatim mode's citations carry their claim under the Claude scorers (226 of 236) and 91% under Sol (214 of 235). For `answer-from-corpus` the figures are 94% and 83%; for Gemini under Sol, 19%. The two families agree on whether a verbatim citation misses for all 225 citations both graded, and on the three-way grade for 209 (93%). Where they differ, Sol is the stricter on 13 and Opus on 3. Wrong book: none under the Claude scorers. Sol flags two, both under the strict secondary-source rule: a theorist named in the sentence, and the passage from a book that discusses him (Reinertsen through Open Kanban on the public corpus, one like it on the private).

### Against the reading fixed before running

- **Lifts citation support** needed verbatim mode's *supports* share 5 points or more above `answer-from-corpus`'s in at least three of the five cells, with its *none* share no higher in any. Under the Claude scorers it is 5 points above in one cell (private C1, +8.7). **Not met.** Its *none* share is 0% in every cell, never higher.
- **Holds level** needed the *supports* shares within 5 points in at least three cells. They are within 5 in four (+1.2, +1.3, −0.5, +0.7). **Met.**
- **Costs support** needed it 5 points or more below in at least three cells. It is below in one cell, by half a point. **Not met.**

Under Sol's grades the lift reading would be met, at +5 or more in four cells (+6.4, +5.4, +17.0, +15.2), *none* at 0% throughout. The two families disagree less about verbatim mode than about `answer-from-corpus`. Sol marks `answer-from-corpus`'s credits partial about twice as often as the Claude scorers do (17% against 6% pooled) and verbatim mode's only somewhat more (9% against 4%). So the lift Sol sees is mostly Sol finding more stretches in `answer-from-corpus`'s credits. The primary grade sits near its ceiling on both arms, at 88–98%, which leaves little room for a 5-point gap in any cell but private C1. By the rule fixed before running, verbatim mode's case rests on what this rubric does not score: a reader can check each citation from its pointer, the passage and its page.

### Kinds of failure

- **No citation misses.** In 236 citations under the Claude scorers and 235 under Sol, none is graded *none*.
- **The partials are stretches in framing,** in both families' notes, on both corpora:
  - a lead-in that claims more than its passage: a passage said to settle a disagreement it doesn't address, or cast as a reply to an author it doesn't answer;
  - a dropped hedge or scope condition ("can", "usually", "often", the circumstances the source sets);
  - an intensifier or an added "only";
  - on C3, an inner-parts teaching cast as a claim about organisations.
  
  These are the same kinds as `answer-from-corpus`'s partials, at a lower rate: 4% of citations against 6% under the Claude scorers, 9% against 17% under Sol.
- **Credits without a pointer.** The credit check repaired 18 join sentences across eight runs, and the generator reported none left. The scorers still found three it missed (two by Opus, one by Sol, different sentences): a join naming an author or source with no pointer. Two were graded *supports*, one *partial*.
- **Converter debris in placed text.** Six placed spans carry text from the conversion rather than the author's sentence:
  - a run-in heading;
  - a column heading the converter ran into the paragraph (a CAIB conclusion that opens "Recommendation:");
  - table-header text;
  - table bars;
  - list bullets and link markup (two spans);
  - a footnote link and e-book markup.
  
  The span with table bars, on private C3, also runs from the author's answer into the interviewer's next question and credits it to the author; the Claude scorer graded it *partial*. The page check flagged two of the six, the column heading and the table-header text. The rest come from sources whose original isn't held, or whose text layer carries the same debris.

### Quotation exactness and the page check

- **Against the converted text:** 132 of 132 placed quotations are found word for word, as the resolver requires before it places anything. The keyword-match round's `quotes.py` located 120 of them mechanically. The other 12 differ only by line-break hyphens, list bullets and link markup, a footnote numeral or table bars, and both scorer families checked each by eye: 132 of 132 under both.
- **Against the printed page:** of the 132 quotations, 113 have an original to check against (the other 19 come from sources whose original file the corpus doesn't hold). 110 of those 113 match their page word for word, 14 of them after the renderer set a word the conversion split as the page prints it. The three that differ:
  - a compound the conversion joined, where the page prints two words;
  - a column heading the converter ran into the paragraph, which isn't on the page;
  - converter table-header text, which isn't on the page.

  As the design says, the check reads the original's text layer, so a slip the text layer shares would pass.

### Expected ideas (C1, C2)

Ideas present, summed over the cell's two runs (11 a run on C1, 13 on C2), with the number credited to a source that carries them in brackets.

| Case | Corpus | Verbatim mode | `answer-from-corpus` | Gemini | Sol: verbatim, `answer-from-corpus`, Gemini |
|---|---|---|---|---|---|
| C1 | demo | 19/22 (15) | 20/22 (18) | chat 17 (16); as asked 19 (17) | 17, 18, 15 |
| C2 | demo | **14/26 (14)** | 21/26 (20) | 18 (18) both conditions | 14, 18, 20 |
| C1 | aarbuddy | 18/22 (16) | 18/22 (16) | chat 15 (14); as asked 16 (15) | 15, 16, 15 |
| C2 | aarbuddy | **14/26 (13)** | 19/26 (19) | as asked 15 (13); chat 14 (13) | 13, 16, 14–15 |

On C1 verbatim mode covers what `answer-from-corpus` does, within an idea per pair of runs, and misses the same keys: the Definition of Done on both corpora, and output against outcome on the private one. **On C2 it costs coverage:** 5 to 7 fewer ideas per pair under the Claude scorers, 3 to 4 under Sol, and below Gemini on the public corpus. The ideas it drops are breadth ones that `answer-from-corpus` reached:

- on both corpora: intent two levels up, the after-action review's rules, and the simple, complicated and complex split;
- on the private corpus: work as imagined against work as done;
- on the public corpus, in one run of the two: preoccupation with failure and the independent technical authority.

It cites fewer sources per answer, 5.5 and 6.5 on C2 against 7.5 and 12. The model step aims at 8 to 14 placed spans across 4 to 6 sections, and on a 13-idea synthesis that budget shows.

### Density, cost and time

- **Density.** Verbatim mode cited *less* densely than `answer-from-corpus`, not more as the limits above expected: 20–27 citations per answer against 32–51. Its distinct sources per answer were 5.5–8.5 against 7.5–19. Support is compared as shares, so this doesn't change the reading. But the caveat that per-citation support favours the arm that cites less now cuts towards verbatim mode.
- **Length.** 1,320–1,947 words of prose per answer in the essay form, pointer blocks aside, against `answer-from-corpus`'s 1,330–1,632.
- **Cost and time.** $47.89 of allowance for the ten, $3.94–6.35 an answer (mean $4.79), with the credit pass $0.77–0.95 of it on the eight runs where it ran. Seven to thirteen minutes an answer (mean 10). `answer-from-corpus` cost $2.18 and about four minutes an answer. Scoring was ten Opus agents of about 110,000–130,000 tokens each, and ten Sol runs on the ChatGPT subscription.

| Report | Spans placed | Quotations | Pointed paraphrases | Credits the credit pass fixed | Page check: checked, match | Cost | Minutes |
|---|---|---|---|---|---|---|---|
| demo C1-1 | 23 of 23 | 14 | 9 | 1 | 10, 9 | $5.05 | 7.8 |
| demo C1-2 | 24 of 24 | 14 | 10 | 1 | 11, 11 | $4.35 | 8.3 |
| demo C2-1 | 29 of 29 | 14 | 15 | 1 | 14, 14 | $5.00 | 9.5 |
| demo C2-2 | 25 of 25 | 13 | 12 | 2 | 13, 12 | $4.71 | 7.2 |
| aarbuddy C1-1 | 28 of 28 | 13 | 15 | 0 | 10, 10 | $6.35 | 10.4 |
| aarbuddy C1-2 | 23 of 23 | 14 | 9 | 0 | 11, 11 | $3.94 | 11.0 |
| aarbuddy C2-1 | 22 of 22 | 11 | 11 | 2 | 11, 11 | $4.65 | 11.7 |
| aarbuddy C2-2 | 18 of 18 | 14 | 4 | 1 | 14, 14 | $4.16 | 10.9 |
| aarbuddy C3-1 | 16 of 16 | 11 | 5 | 4 | 9, 8 | $4.91 | 12.8 |
| aarbuddy C3-2 | 26 of 26 | 14 | 12 | 6 | 10, 10 | $4.77 | 11.6 |
| **All** | **234 of 234** | **132** | **102** | **18** | **113, 110** | **$47.89** | **10.1** |

Every anchor resolved on the first pass, so no repair pass ran.

## What it says

Placing the authors' words doesn't raise the share of citations that carry their claim on the primary grade, because `answer-from-corpus`'s credits already carry theirs 88–98% of the time. Neither arm's citations miss. Verbatim mode stretches a claim less often (4% against 6% partial under the Claude scorers, 9% against 17% under Sol), its quotations are the converted text by construction, and a reader can open the page behind each one. Against Gemini Notebook, on the same cases and grade, both forge arms sit far from it: 19% of Gemini's markers carry their claim as stated under Sol, against 91% of verbatim mode's citations and 83% of `answer-from-corpus`'s.

The price is breadth and money. On the 13-idea C2 synthesis it covers 5 to 7 fewer ideas than `answer-from-corpus`, and it costs about twice as much and two and a half times as long per answer. The next lever is the model step's span budget, or a second pass that checks the plan against the question's parts before placing anything. That is a change to the generator, so a round of its own.

Three cases, two runs, Claude as case writer, one scorer family and both forge arms. Read the direction, not the decimals.
