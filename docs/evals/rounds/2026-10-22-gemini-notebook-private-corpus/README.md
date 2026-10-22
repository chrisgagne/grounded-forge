# Gemini Notebook against a private grounded-forge corpus, and what the matrix's layers are worth

**TL;DR.** Over 17 questions (19–22 October 2026), a private grounded-forge corpus was run blind against Google's Gemini Notebook over the same sources. It was then taken apart, layer by layer, to see what each part of the design contributes.

- **Retrieval was a tie on simple questions.** On lookups, traps and wide syntheses, Gemini Notebook did as well.
- **grounded-forge pulled ahead where the work needs more than retrieval:**
  - applying sources to a case;
  - keeping safety cautions;
  - finding *every* instance of something;
  - running a live review.

  On an exhaustive question it found 22 of 23 items to Gemini's 15, and Gemini called its own list complete. In a live review with a participant who answers only what's asked, Gemini asked no questions at all.
- **Within grounded-forge, the distillations didn't earn their keep.** Three things did the work: the audited references, a page of written principles, and a facilitation procedure for live sessions. That led to two fixes: a quote check that now ships with `answer-from-corpus`, and an open question about the project's tagline.

Single runs or pairs, one judge family, and a private corpus: read this as a direction, not a decimal.

## Why a private corpus

The protocol at [`../../gemini-notebook-arm.md`](../../gemini-notebook-arm.md) plans this comparison over the public demo corpus and is still unrun. This round used the author's private working corpus instead: about 330 audited sources (books, papers, standards and a licensed coaching course) with light and deep references, five task axes of distillations, and lenses. The corpus owner uploaded the original files (PDFs and EPUBs as he had them, not the converted Markdown) to a Gemini Notebook Pro notebook, which took 287 of them. A few uploads failed with a bare "error, try again" that gave no reason.

Nothing from the private corpus is published here: no source text, no distillation and no answer. Results are given as counts, scores and kinds of failure. The question files, answers, run logs and judge readings stay in the private corpus.

## Arms

- **G, Gemini Notebook:** the notebook as a user would use it, with default settings and the chat cleared before each question. Most questions were asked twice, once with a paragraph of rules (quote exactly, mark gaps) and once as the bare question a user would type, because the rules turned out to lead Gemini.
- **Project mode:** a fresh Claude session over the corpus's references, using `answer-from-corpus`.
- **App mode:** the compiled AAR app (distillations, task index, AAR skills).
- **Ablations:**
  - references plus the app's instructions without distillations (M);
  - references plus only the app's principles block (P);
  - P plus an action cap, and P plus an "ask before you write" rule;
  - the app's 1,862-line facilitation procedure swapped for a one-try procedure written by Gemini or by a fresh Claude.

The Claude arms ran isolated with `claude -p` (Opus 5.5 at effort high), with project and local settings only, an empty MCP configuration, and no web. Blind judges (Opus) scored against rubrics written before any arm ran.

## Results

| # | Task | Result |
|---|---|---|
| 1 | Advice for a named person, from a lens | Same choice. Gemini quoted its sources exactly but misapplied several passages; grounded-forge marked its gaps and inferences. |
| 2 | After-action review of a near-miss, with an HR question | grounded-forge 13 of 14 expected ideas. Gemini 10 asked plainly; 7 with the rules paragraph, and all 7 of those citations pointed at the wrong book. |
| 3 | Named lookup | Tie. |
| 4 | Question with a trap (the sources don't support it) | Both passed. |
| 5 | Wide synthesis with quotations | Gemini wider (40 quotations, 1 misquote); grounded-forge deeper (34 of 34 exact, one wrong "not in source" call). |
| 6 | Organisational case | Tie on content; grounded-forge stated its condition and gaps. |
| 7 | Reading a job posting through a lens | Both good; grounded-forge deeper. |
| 8 | Safety question on a coaching course | Both grounded. Gemini left out the course's contraindication for clients with a history of psychosis. |
| 9 | Find *every* referral and contraindication in that course | grounded-forge 22 of 23 key items with the right sessions, and an honest "about 95%". Gemini 15 (plus 3 partial), several sessions wrong, an invented level, and the psychosis caution missed again, while calling its list "comprehensive, re-verified". |
| 10 | AAR write-up, all facts given (one-shot) | App with distillations 87; references only 79; Gemini 62. |
| 10M | Same, references + the app's instructions, no distillations | 88. |
| 11 | Same, the 1,862-line procedure swapped for a one-try one | Claude-written 89; Gemini-written 85. |
| 12 | Same, references + the app's 11 principle lines only | 86.5. |
| 13 | 12 plus "three to five actions" | 86.5: tighter actions, thinner analysis. |
| 14 | Live review: a simulated manager holds 32 hidden facts | Procedure 21 facts, AAR 73; principles only 11 facts, 54; Gemini 40, and it asked only when the participant nudged it. |
| 14b | Same, participant answers only what is asked | Procedure 27 facts, AAR 84; principles only 2 facts, 28; Gemini 0 facts in three runs, 26–30. |
| 15 | Review a real coaching session (pseudonymised) against a competency framework | Distillations 83; project mode 82; the full review skill's earlier report 84; Gemini 51, with the scope-of-practice moment missed in half its readings. |
| 17 | 14b with principles plus "ask before you write" | 6–9 facts, AAR 43–44: it asked early, then stopped. |

A harness run of Q14 with a 14-turn cap went the other way (principles 68 against procedure 62), because the procedure spent its turns on the timeline and never reached actions. Its pacing was in minutes, which a chat assistant can't see. Two changes fixed it: an exchange budget (be into analysis by halfway and into actions by three-quarters), and the history and measures questions no arm had asked. With them, the procedure finished inside the cap. It reached both facts and was preferred over principles in both blind readings (71 against 66.5, one run). Its actions were still the weaker of the two.

## What the evidence says about the layers

1. **Retrieval isn't where grounded-forge wins.** Gemini Notebook retrieves well over a few hundred sources, and on lookups and wide syntheses it matched or out-quoted the matrix.
2. **The harness is a real advantage.** grounded-forge runs where it can read every relevant file, spawn readers and check its own quotes. That's why it won the exhaustive question (Q9) and kept the cautions (Q8, Q15). A chat product can't do this from inside its retrieval budget.
3. **The distillations added little to answer quality on these tests.**
   - On AAR work, where the literature is in the model's training, references plus the app's instructions matched or beat the app with distillations (Q10M).
   - On the coaching course, which isn't in training, distillations and references tied (Q15). But every arm was given an annotated competency framework that already carries the course's techniques, so that test couldn't isolate the layer.
   - Distillations cost about a third of ingestion spend. The independent audits are the largest part; producing the references is the smallest.
4. **What did the work:**
   - **Audited references:** every strong arm stood on them.
   - **A page of written principles:** these supplied the leverage-point and one-experiment moves (Q11–Q12).
   - **A real procedure for live work:** the procedure is what makes the assistant ask, topic by topic, before it writes (Q14, Q14b, Q17). One-shot, a short procedure with an action cap is enough.
5. **Quote fidelity was the one systematic fault, in every Claude configuration.**
   - The app quoted a distillation's list item as the author's words in all three runs.
   - Project mode quoted a light reference's paraphrase as the author's words.

   The skill already forbade both, and neither was caught. `answer-from-corpus` now runs [`check_quotes.py`](../../../../.claude/skills/answer-from-corpus/check_quotes.py) before an answer goes out. It flags any author quotation that matches only a summary layer or nothing at all, and it caught every such case found by hand in this round.
6. **Gemini Notebook is an answer engine.** Given an incident and asked to run the review, it wrote a confident document from the first message, with invented specifics, and never asked a question.

## Caveats

- **The judges are Claude, and so are three of the four arms.** Gemini's answers were judged by a Claude judge against rubrics Claude wrote before the runs. Mechanical checks (facts counted from tags, timestamps and quotes matched against text) carry the cross-family claims where they exist.
- **The tests were few:** mostly one or two runs per arm, one corpus and one domain pair.
- **Gemini wasn't given every chance:**
  - Asked plainly, it used its library less than it could have.
  - Its Studio files survive "Delete chat history" and are read in later chats, which contaminated one of the Q14 runs; the affected runs are marked.
  - Its citations are chunk numbers that mean nothing outside the notebook.
- **Q14's first Gemini runs were coached** by a participant that nudged it 20 times in one run. Q14b's gated participant supersedes them.
- **Confidentiality.** The coaching test used a real client session, pseudonymised before any arm saw it. Its transcript, reviews and judge readings are kept out of version control.

## What changed

- `answer-from-corpus` checks author quotations before it answers (`check_quotes.py`, with tests in [`tests/check-quotes.test.py`](../../../../tests/check-quotes.test.py)).
- The README's findings now carry this round's results. Its claim that the matrix is necessary on non-canonical material is narrowed to what was shown.
