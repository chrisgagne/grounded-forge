# grounded-forge against Gemini Notebook: what the evals show

Between 31 October and 5 November 2026, seven eval rounds put the same questions to Gemini Notebook and to grounded-forge, over the same sources, and checked every citation or claim against the books. This page gathers what held across them, with each figure at the grain it was measured at. Each round's own README has the design, the per-answer tables and the caveats in full.

## What was compared

- **Gemini Notebook** on Google's Pro plan, with the corpus's original files uploaded as sources, at default chat settings and, in one round, under a strict custom chat style. Google doesn't say which model answers a Notebook chat; the Ultra plan and Gemini 4 Argon weren't tested in Notebook ([one unscored Argon run](rounds/2026-11-05-gemini-strict-style/#which-gemini) in the Gemini app cited whole files per section).
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
| [Round 3b](rounds/2026-11-02-verbatim-case-citations/#round-3b-after-the-fixes) | the same cases, after three generator fixes | 7 (verbatim mode) | citation | Opus, then a Sol re-grade of all 7 |
| [Per-sentence re-grade](rounds/2026-11-case-citations/) | the case-citations cases | Gemini's 13 cited answers | sentence, markers taken together | Sol and Opus |
| [Strict chat style](rounds/2026-11-05-gemini-strict-style/) | the case-citations cases, both libraries | 10 (Gemini, strict style) | marker, then sentence | Sol and Opus |
| [Pooled coverage](rounds/2026-11-05-pooled-coverage/) | the case-citations cases, both libraries | 57, every arm | idea, pooled across answers | Opus and Sol |

Sol (`gpt-6.1-sol`) is from a different model family from Claude, and wrote none of the answers.

## What held across the rounds

**Where Gemini cites, its markers land near the claim, not on it.** A Gemini citation tells the reader where the topic lives; a grounded-forge citation tells them where the claim lives.
- **Per sentence, about 40% against 82–91%.** Gemini often puts two to six markers on one sentence, each backing a part, so the fair unit is the sentence with its markers taken together. Graded that way, 41% (Sol) and 39% (Opus) of Gemini's cited sentences were carried by their markers, across both libraries. What the markers still missed was mostly what the sentence added: a number, the application to the case, a stronger verb. `answer-from-corpus` carried 86% (public) and 82% (private) of its cited sentences, and verbatim mode, whose pointers name one passage each and rarely stack, 91% of its pointers in Sol's grading (89% in round 3b).
- **One marker at a time, the gap looks bigger:** 19% of Gemini's markers carried their sentence in Sol's grading, because a marker backing one part of a sentence counts as partial. That figure measures how precise each marker is, not how often a sentence is supported.
- **`answer-from-corpus` is graded at a coarser grain.** A credit names a whole source, and the scorer searched the book for the claim, which is an easier test than checking one chunk. Verbatim mode is the like-for-like arm.
- **Outright misses were rare on both sides:** Gemini 1–7% of markers per case under Sol, grounded-forge 0–2%. Gemini's problem is claims that go a little further than their passages, not invention.

**A one-paragraph chat style roughly doubles Gemini's rate.** Told to cite only what a passage says, to mark its own inferences as "My inference:" without a citation, and to quote only exact words, Gemini's cited sentences carried by their markers rose from about 40% to 73% (Sol) and 71% (Opus): 64–67% on the public notebook, 76–77% on the private one. It gets there by citing fewer sentences, not by finding better passages, and its quotations became mostly exact. Nothing in Gemini enforces the style; a user has to know to set it.

**Asked for a memo, Gemini often doesn't cite at all.** In 7 of 10 as-asked runs, it wrote the memo as a Studio report with no citation markers.

**grounded-forge's quotations are exact; Gemini's are few and loose.**
- `answer-from-corpus`: 142 of 146 quotations found word for word.
- Verbatim mode: 132 of 132 match the converted text. Of the 113 with an original to check against, 110 also match the printed page.
- Gemini put about 60 strings in quotation marks across 20 answers, and 9 were in a source word for word. In round 2 it credited one phrase to an author whose book doesn't contain it.

**Gemini's claims often go further than their passages.** Its cited passages were real wherever a judge checked. The gap is in what the sentence beside them claims: specifics the passage lacks, a passage applied to a point it doesn't make, a hedge dropped.
- Round 1: 12 of Gemini's 23 claims were fully supported, against all 14 forge quotations and 10–11 of 12 other forge claims.
- Round 2, question 2: as delivered, 38–42% of Gemini's quotations and attributed claims were supported under Opus and 47% under Sol, against the forge answer's 57–66% and 64%.

**grounded-forge's answers carry more supported ideas.** The [pooled-coverage round](rounds/2026-11-05-pooled-coverage/) pooled every distinct idea across all 57 answers to the cases, with no list written in advance, and checked each against the library. In both families' pooling and on both libraries, `answer-from-corpus` and verbatim mode (after round 3b let the model size the answer) carried 12–18 more supported ideas per answer than Gemini's default chat answers: 50–54 against 38–39 in Sol's pooling, 33–40 against 21–24 in Opus's. `answer-from-corpus` also leads per word; verbatim mode's lead is partly length. Verbatim mode in round 3, with a fixed budget of placed passages, carried about as many as Gemini's chat answers. Gemini's Studio reports carry more ideas than its chat answers, at the lowest density of any arm.

**Verbatim mode holds level with `answer-from-corpus` on citation support.** Its pre-registered lift was 5 points or more in three of five cells. Under the Claude scorers it lifted support in one (+8.7), and was within 5 points in the other four. Under Sol it would have met the lift. Its value is that every claim opens its passage and printed page in one click, which this rubric doesn't score.

## Where Gemini led

On round 2's demo question, under the Opus judges, Gemini's claims were more often supported as delivered: 62% against 52–57%. Twenty-two of the forge answer's attributed sentences had no pointer. Under Sol the forge answer led: 69% against 64%, because Sol counted the source a sentence names as its pointer.

Since then, every sentence that credits a source is a *pointed paraphrase*, with its own pointer, and the generator stops on any it finds without one. In round 3, three slipped through, across 10 answers. Round 3b added a model sweep for credits a word list misses, and none of its 7 answers left one without a pointer.

## Effort to check

How much effort a reader saves depends on how effort is counted.
- **Round 1:** checking the forge answer took a third to a half of the judge operations.
- **Round 2:** the rubric charged nothing for reading a passage the answer already shows. Gemini shows one for every marker, so its supported claims cost nothing to check either, and the gap closed.
- **Where a claim fails,** the forge answer's line and page pointers let a judge find the right place in one step. The judges worked from Gemini's captured popups, which name the file and show the chunk but not its page, so they searched the whole file. Gemini's own interface does more: checked on 4 November 2026, a marker opens the chunk in the notebook's source view, highlighted in the extracted text, under a scan of its page.

## Limits

- **Claude is on both sides.** grounded-forge's answers are written by Claude, and Claude is the primary scorer. Sol re-graded the case-citations round, round 2 and round 3. It agreed with the Claude scorers on 96% of miss calls in the case-citations round, and on every one in rounds 3 and 3b. In round 2 it agreed on 85% of delivered calls, against 94% between the two Opus judges. Round 1 was judged by Opus only.
- **Blinding was thin.** Judges guessed which kind of tool wrote an answer from its form, pointer blocks against citation popups.
- **One Gemini plan.** Gemini Notebook ran on the Pro plan and grounded-forge on Claude Opus 5.5, Anthropic's top model. The comparison is between the products as an individual buys them, not between the two companies' best models.
- **The numbers are small.** Three cases, four questions, one or two runs each, written with the corpora in view. Read this as a direction, not a rate.
- **Coverage has no answer key.** The case-citations round's keys were written by Claude, which also wrote grounded-forge's answers, so coverage comes from the pooled round, where Opus and Sol each pooled the ideas and the ranking holds in both.
- **Scale.** Gemini's share of markers carrying the claim as stated fell from 23–57% on the public notebook to 10–24% on the private one. Its miss rate didn't rise. The private corpus is reported as counts only.
