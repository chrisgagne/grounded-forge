# grounded-forge against Gemini Notebook: what the evals show

Between 31 October and 2 November 2026, four eval rounds put the same questions to Gemini Notebook and to grounded-forge, over the same sources, and checked every citation or claim against the books. This page gathers what held across them, with each figure at the grain it was measured at. Each round's own README has the design, the per-answer tables and the caveats in full.

## What was compared

- **Gemini Notebook,** with the corpus's original files uploaded as sources, default chat settings.
- **grounded-forge in two forms.**
  - `answer-from-corpus` in project mode, reading the corpus's audited references and converted text.
  - [Verbatim mode](../architecture/verbatim-mode-proposal.md), where the model writes the argument, and code places each quotation from the converted source and gives every credited claim a pointer to its passage and printed page.
- **Two libraries.**
  - The public `demo` corpus: 31 open sources, 35 files in its notebook.
  - A private corpus in the low hundreds of sources, with the same files in a second notebook. Private results are reported as counts only.

| Round | Questions | Answers | Scored per | Scorers |
|---|---|---|---|---|
| [Case citations](rounds/2026-11-case-citations/) | 3 practitioner cases, both libraries | 30 (`answer-from-corpus` and Gemini) | citation, about 1,500 in all | Claude scorers, then a Sol re-grade of all 30 |
| [Verbatim round 1](rounds/2026-11-02-verbatim-vs-gemini/) | 1 (NZ pandemic), private | 2 | claim | 2 blind Opus judges |
| [Verbatim round 2](rounds/2026-11-02-verbatim-vs-gemini-2/) | 3, one corpus each | 6 | claim, from a shared claim list | 12 single-answer Opus judges, then 6 Sol judges |
| [Verbatim round 3](rounds/2026-11-02-verbatim-case-citations/) | the case-citations cases | 10 (verbatim mode) | citation | Opus, then a Sol re-grade of all 10 |

Sol (`gpt-6.1-sol`) is from a different model family from Claude, and wrote none of the answers.

## What held across the rounds

**Where Gemini cites, its markers land near the claim, not on it.**
- In the case-citations round, 19% of Gemini's markers opened a chunk that carries the claim as stated, under Sol. The rest mostly carried part of it, or a weaker form.
- `answer-from-corpus`'s credits carried their claim 83% of the time under Sol and 94% under the Claude scorers. Verbatim mode's carried it 91% and 96% (round 3).
- Outright misses were rare on both sides: Gemini 1–7% of markers per case under Sol, grounded-forge 0–2%.

**Asked for a memo, Gemini often doesn't cite at all.** In 7 of 10 as-asked runs, it wrote the memo as a Studio report with no citation markers.

**grounded-forge's quotations are exact; Gemini's are few and loose.**
- `answer-from-corpus`: 142 of 146 quotations found word for word.
- Verbatim mode: 132 of 132 match the converted text. Of the 113 with an original to check against, 110 also match the printed page.
- Gemini put about 60 strings in quotation marks across 20 answers, and 9 were in a source word for word. In round 2 it credited one phrase to an author whose book doesn't contain it.

**Gemini's claims often go further than their passages.** Its cited passages were real wherever a judge checked. The gap is in what the sentence beside them claims: specifics the passage lacks, a passage applied to a point it doesn't make, a hedge dropped.
- Round 1: 12 of Gemini's 23 claims were fully supported, against all 14 forge quotations and 10–11 of 12 other forge claims.
- Round 2, question 2: as delivered, 38–42% of Gemini's quotations and attributed claims were supported under Opus and 47% under Sol, against the forge answer's 57–66% and 64%.

**Coverage of the expected ideas is about level.** Both arms covered the case-citations answer keys about equally. Verbatim mode covered fewer on the broadest case: 14 of 26 expected ideas, against `answer-from-corpus`'s 21 and 19. Building an answer around placed passages narrowed a broad synthesis.

**Verbatim mode holds level with `answer-from-corpus` on citation support.** Its pre-registered lift was 5 points or more in three of five cells. Under the Claude scorers it lifted support in one (+8.7), and was within 5 points in the other four. Under Sol it would have met the lift. Its value is that every claim opens its passage and printed page in one click, which this rubric doesn't score.

## Where Gemini led

On round 2's demo question, under the Opus judges, Gemini's claims were more often supported as delivered: 62% against 52–57%. Twenty-two of the forge answer's attributed sentences had no pointer. Under Sol the forge answer led: 69% against 64%, because Sol counted the source a sentence names as its pointer.

Since then, every sentence that credits a source is a *pointed paraphrase*, with its own pointer, and the generator stops on any it finds without one. In round 3, three slipped through, across 10 answers.

## Effort to check

How much effort a reader saves depends on how effort is counted.
- **Round 1:** checking the forge answer took a third to a half of the judge operations.
- **Round 2:** the rubric charged nothing for reading a passage the answer already shows. Gemini shows one for every marker, so its supported claims cost nothing to check either, and the gap closed.
- **Where a claim fails,** the forge answer's line and page pointers let a judge find the right place in one step. Gemini names the book only.

## Limits

- **Claude is on both sides.** grounded-forge's answers are written by Claude, and Claude is the primary scorer. Sol re-graded the case-citations round, round 2 and round 3. It agreed with the Claude scorers on 96% of miss calls in the case-citations round, and on every one in round 3. In round 2 it agreed on 85% of delivered calls, against 94% between the two Opus judges. Round 1 was judged by Opus only.
- **Blinding was thin.** Judges guessed which kind of tool wrote an answer from its form, pointer blocks against citation popups.
- **The numbers are small.** Three cases, four questions, one or two runs each, written with the corpora in view. Read this as a direction, not a rate.
- **Scale.** Gemini's share of markers carrying the claim as stated fell from 23–57% on the public notebook to 10–24% on the private one. Its miss rate didn't rise. The private corpus is reported as counts only.
