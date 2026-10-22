# Gemini Notebook against a private grounded-forge corpus, and what the matrix's layers are worth

**TL;DR.** Over 18 tests (19–22 October 2026), a private grounded-forge corpus was run blind against Google's Gemini Notebook over the same sources. It was then taken apart, layer by layer, to see what each part of the design contributes.

- **Retrieval wasn't grounded-forge's edge.**
  - On a lookup and a trap question, the two tied.
  - On the one wide synthesis, Gemini was wider: about 20 sources, including the strongest voice grounded-forge missed. grounded-forge was deeper, with every answer-key item and more insight. Quote accuracy was close.
- **grounded-forge pulled ahead where the work needs more than retrieval:**
  - applying sources to a case;
  - keeping safety cautions;
  - finding *every* instance of something;
  - running a live review.

  On an exhaustive question it found 22 of 23 items to Gemini's 15, and Gemini called its own list complete. In a live review with a participant who answers only what's asked, Gemini asked no questions at all.
- **Within grounded-forge, the distillations didn't earn their keep.** Swapping them for plain light references under the same app made no measurable difference, one-shot or live, on Opus or on Sonnet. What did the work was the audited references and the pieces built by hand for the task: a page of written principles, a facilitation procedure for live sessions, and, for the coaching review, a competency framework worth about 28 points. That led to two fixes: a quote check that now ships with `answer-from-corpus`, and an open question about the project's tagline.

Single runs or pairs, one judge family, and a private corpus: read this as a direction, not a decimal.

## Why a private corpus

The protocol at [`../../gemini-notebook-arm.md`](../../gemini-notebook-arm.md) plans this comparison over the public demo corpus and is still unrun. This round used the author's private working corpus instead: about 330 audited sources (books, papers, standards and a licensed coaching course) with light and deep references, five task axes of distillations, and lenses. 293 files went to a Gemini Notebook Pro notebook: the originals as they were (PDF, EPUB) where they existed, and Markdown where they didn't. 289 imported, and 287 corpus sources were in play for the questions.

Four PDFs failed with a bare "error, try again":
- two scanned books with no text layer, which Gemini therefore couldn't read at all, so questions touching them favoured grounded-forge for a reason that belongs to the product;
- two with a text layer, for no stated reason.

Seven Markdown files first failed on the corpus's own provenance-comment format and went in once it was fixed.

Nothing from the private corpus is published here: no source text, no distillation and no answer. Results are given as counts, scores and kinds of failure. The question files, answers, run logs and judge readings stay in the private corpus.

## Arms

- **G, Gemini Notebook:** the notebook as a user would use it, with default settings and the chat cleared before each question. Q1–Q6 carried a paragraph of rules (quote exactly, mark gaps). The rules turned out to lead Gemini, so Q1, Q2 and Q6 were rerun with the bare question a user would type, and from Q7 on Gemini got the bare question only.
- **Project mode:** a fresh Claude session over the corpus's references, using `answer-from-corpus`.
- **App mode:** the compiled AAR app (distillations, task index, AAR skills).
- **Ablations:**
  - references plus the app's instructions without distillations (M);
  - references plus only the app's principles block (P);
  - P plus an action cap, and P plus an "ask before you write" rule;
  - the app's 1,862-line facilitation procedure swapped for a one-try procedure written by Gemini or by a fresh Claude;
  - each per-source distillation replaced by that source's light reference, a quarter to a third shorter, with the task indexes, facilitator and skills unchanged (L, Q19).

How the Claude arms ran and were scored:
- **Q1–Q9:** fresh Claude Code sessions in project mode, kept blind to the keys and to Gemini's answers. They were scored by the Claude session running the round, against answer keys written before either side ran. Chris read Q7.
- **From Q10:** isolated `claude -p` runs (Opus 5.5 at effort high), with project and local settings only, an empty MCP configuration and no web. Blind Opus judges scored them against rubrics written before any arm ran. Q19 also ran each arm on Sonnet 5.5, at the same effort.

## Results

| # | Task | Result |
|---|---|---|
| 1 | Advice for a named person, from a lens | Same choice. Gemini's answer was more concrete to act on; it quoted its sources exactly, but five claims cited passages that don't carry them. grounded-forge marked its gaps and inferences. |
| 2 | After-action review of a near-miss, with an HR question | grounded-forge 13 of 14 expected ideas. Gemini 10 asked plainly; 7 with the rules paragraph, and all 7 of those citations pointed at the wrong book. |
| 3 | Named lookup | Tie. |
| 4 | Question with a trap (the sources don't support it) | Both passed. |
| 5 | Wide synthesis with quotations (where the sources disagree on root cause) | Gemini wider: about 20 sources, including the library's strongest pro-root-cause voice, which grounded-forge missed; 39 of 40 quotations exact. grounded-forge deeper: every answer-key item, including two Gemini missed, and more insight beyond listing; 34 of 34 exact, one wrong "not in source" call. |
| 6 | Organisational case | Tie on content: Gemini stronger on flow mechanics, grounded-forge on why the agreement failed. With the rules paragraph Gemini also stated a condition and its gaps; asked plainly, it gave neither. |
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
| 15 | Review a real coaching session (pseudonymised) against a competency framework | Distillations 83.2; project mode 82.0; the full review skill's earlier report 83.5; Gemini 51, with the scope-of-practice moment missed in half its readings. |
| 17 | 14b with principles plus "ask before you write" | 6–9 facts, AAR 43–44: it asked early, then stopped. |
| 19 | Distillations (D) against light references (L), on Opus and on Sonnet: Q15's review without the framework, and a live review in the capped harness below | Review: Opus D 55.3, L 55.0; Sonnet D 43.5, L 48.0 (Q15 with the framework: 83.2). Live: on each model the two pairs split one each way; means Opus D 69.5, L 74.5; Sonnet 68.5 each. |

A harness run of Q14 with a 14-turn cap went the other way (principles 68 against procedure 62), because the procedure spent its turns on the timeline and never reached actions. Its pacing was in minutes, which a chat assistant can't see. Two changes fixed it: an exchange budget (be into analysis by halfway and into actions by three-quarters), and the history and measures questions no arm had asked. With them, the procedure finished inside the cap. It reached both facts and was preferred over principles in both blind readings (71 against 66.5, one run). Its actions were still the weaker of the two.

## What the evidence says about the layers

1. **Retrieval isn't where grounded-forge wins.** Gemini Notebook retrieves well over a few hundred sources. It tied on the lookup, and on the wide synthesis it found more sources than grounded-forge did. Its failures came from applying sources to a case and from reasoning past them, not from finding them.
2. **The harness is a real advantage.** grounded-forge runs where it can read every relevant file, spawn readers and check its own quotes. That's how it won the exhaustive question (Q9): ten parallel readers covered the whole course. A chat product can't do this from inside its retrieval budget. grounded-forge also kept the safety cautions Gemini dropped (Q8, Q15), but these tests don't show why.
3. **The distillations added little to answer quality on these tests.**
   - On AAR work, where the literature is in the model's training, references plus the app's instructions matched or beat the app with distillations (Q10M).
   - On the coaching course, which isn't in training, distillations and references tied (Q15). But every arm was given an annotated competency framework that already carries the course's techniques. Q19 withheld it: both Opus arms dropped about 28 points, and distillations and light references still tied.
   - Live, Q19 swapped the distillations for light references under the same facilitator, and on each model the pairs split one each way. A live session read only one to six library files. The facilitator and the task index carried the method, and which questions the facilitator asked decided every pair.
   - The weaker model didn't need them more. On Sonnet, light references tied live and scored slightly higher on the review (48.0 against 43.5, inside the spread between one arm's two runs).
   - Distillations cost about a third of ingestion spend in the logs since September 2026. The independent audits are the largest part; producing the references is the smallest.
4. **What did the work:**
   - **Audited references:** every strong arm stood on them.
   - **A page of written principles:** these supplied the leverage-point and one-experiment moves (Q11–Q12).
   - **A real procedure for live work:** the procedure is what makes the assistant ask, topic by topic, before it writes (Q14, Q14b, Q17). With it, Sonnet ran live reviews nearly as well as Opus (68.5 against 69.5–74.5, Q19). One-shot, a short procedure with an action cap is enough.
   - **A framework for reviewing against a standard:** withholding the competency framework cost about 28 points, and without it all eight reviews made up their own headings (Q19).
5. **Quote fidelity was the one systematic fault, in every Claude configuration.**
   - The app quoted a distillation's list item as the author's words in all three runs.
   - Project mode quoted a light reference's paraphrase as the author's words.

   The skill already forbade both, and neither was caught. `answer-from-corpus` now runs [`check_quotes.py`](../../../../.claude/skills/answer-from-corpus/check_quotes.py) before an answer goes out. It flags any author quotation that matches only a summary layer or nothing at all. Run on the Q10 answers, it caught every such case found there by hand.
6. **Gemini Notebook is an answer engine.** Given an incident and asked to run the review, it wrote a confident document from the first message, with invented specifics, and never asked a question.

## What each product can do (checked 22 October 2026)

Gemini Notebook and an agent harness (Claude Code, Codex) are different kinds of product. From the vendors' documentation:

- **Gemini Notebook does things the harnesses don't:**
  - Studio outputs: audio and video overviews, slide decks, mind maps, reports, data tables and quizzes;
  - click-through citations to the exact passage;
  - Drive sources that stay in sync;
  - sharing with named users, or as a public notebook ([sharing](https://support.google.com/gemininotebook/answer/16206563));
  - research that brings web sources in;
  - use from the Gemini app; nothing to install.
- **The harnesses do things Gemini Notebook doesn't:**
  - Choosing the model and the reasoning effort ([Claude Code](https://code.claude.com/docs/en/model-config), [Codex](https://learn.chatgpt.com/docs/models)). Gemini Notebook documents neither ([chat help](https://support.google.com/gemininotebook/answer/16179559)).
  - Reading a whole library from local files. A notebook is capped (300 sources on Pro), and each notebook is independent: "Gemini Notebook can't access information across multiple notebooks at the same time" ([help](https://support.google.com/gemininotebook/answer/16206563)).
  - Shell, file edits, MCP connectors, subagents, browser and computer control, reusable skills, and project instruction files. Gemini Notebook's nearest is a chat style or role set under Configure Chat ([chat help](https://support.google.com/gemininotebook/answer/16179559)).
  - Scripted runs (`claude -p`, `codex exec`, SDKs). Gemini Notebook's Enterprise API (v1alpha, updated 9 October 2026) creates, shares and deletes notebooks, sources and audio overviews, but has no call to ask a notebook a question ([API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.cloud.notebooklm.v1alpha)).
- **Gemini Notebook is gaining agency.**
  - Since 16 July 2026 each notebook has "a secure cloud computer" that writes and runs code, available on Ultra and rolling out to Pro ([Google](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)).
  - Its chat can search the web, run code and create files, features Google labels "experimental and in early development" ([chat help](https://support.google.com/gemininotebook/answer/16179559)).

  Calling it "chat-only" is already out of date.

That's the frame for this round. On retrieval the two are comparable. grounded-forge's clearest wins (Q9, Q14b, the quote check) come from things only an agent can do: read everything, run a procedure, and check its own output.

## Trust: what each side did with what it didn't know

Both sides invented specifics when filling gaps. What separated them was whether they said so.

- **Gemini's inventions:**
  - a rollback version and a paging tool the case never named (Q10, Q14b);
  - an outcome nobody reported ("error rate drops to zero", Q10) and assumptions credited to the manager that he never voiced;
  - a course level that doesn't exist (Q9);
  - in the coaching review (Q15), a rating tier and a "fourth depth" the framework doesn't have, and about 15 evidence errors per review against 6–7 for the Claude arms.
- **The Claude arms invented too.** In Q10 the blind judges flagged invented case detail as often in the references-only arm as in Gemini's (4 of 6 readings each), including runs counted as employers and an assumption about the rollback stated as fact.
- **grounded-forge marked its inferences and gaps:**
  - "the mapping is mine" at each bridge and six named gaps (Q1);
  - a condition its advice rests on, stated without being asked (Q6), where Gemini, asked plainly, gave neither a condition nor gaps;
  - "about 95% complete" on the exhaustive question (Q9).
- **Gemini didn't.** It marked an inference once in Q1 and named no gaps. It called a list that held 15 of 23 items in full "comprehensive, re-verified" (Q9). Live, it wrote a finished document before it knew the facts and never asked a question (Q14b).

The trust problem is unflagged confidence: specific claims presented as established, in exactly the places a reader can't check. A tool that's wrong but says "this is my inference" can be used with care; one that's wrong and sounds certain can't be, for anything that matters.

## Caveats

- **The judges are Claude, and so is every arm but Gemini.** Gemini's answers were judged by Claude against rubrics Claude wrote before the runs. Mechanical checks (facts counted from tags, timestamps and quotes matched against text) carry the cross-family claims where they exist.
- **The tests were few:** mostly one or two runs per arm, one corpus and one domain pair. In Q19, two runs of the same live arm differed by about 10 points, twice the gap between the arms' means: a null result at small n, not proof that the two are equivalent.
- **Gemini wasn't given every chance:**
  - Asked plainly, it used its library less than it could have.
  - Its saved notes become ticked sources, and its Studio files survive "Delete chat history" and are read in later chats. A saved note reached Q4 and a Studio file reached one of the Q14 runs. From then on, notes were unticked and Studio files deleted between runs, and the affected runs are marked.
  - "Copy notebook" re-ingests every source; a copy of this notebook failed with 163 of 296 sources in.
  - Its citations are chunk numbers that mean nothing outside the notebook.
- **Q14's first Gemini runs were coached** by a participant that nudged it 20 times in one run. Q14b's gated participant supersedes them.
- **Confidentiality.** The coaching test used a real client session, pseudonymised before any arm saw it. Its transcript, reviews and judge readings are kept out of version control.

## What changed

- `answer-from-corpus` checks author quotations before it answers (`check_quotes.py`, with tests in [`tests/check-quotes.test.py`](../../../../tests/check-quotes.test.py)).
- The README's findings now carry this round's results. Its claim that the matrix is necessary on non-canonical material is narrowed to what was shown.
