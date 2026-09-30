# Topic layer: schema-2 vs schema-3 concept index, paired answers

**TL;DR.** On the demo `decision` app, answers routed through the schema-3 concept index (a topics block read whole, concept rows fetched by topic) matched answers routed through the schema-2 index (every concept row read whole) on quality, and cost 10% fewer tokens. A blind cross-family judge picked the schema-3 answer once, the schema-2 answer twice and called one a tie; rubric totals were 74 and 76 of 80. Neither arm had a grounding failure. The saving is small here because demo's index is small (41 KB); the topics block is a quarter of the file, and the gap should widen on a large corpus, which this round doesn't test.

## Question

Does reading a concept index as topics first, then rows, lose anything a model finds by reading every concept row, when it answers a real question inside a compiled app?

## Arms

Both arms are the demo `decision` app, exported from git into separate folders and hashed before the first run (`receipts/hashes.txt`). Their 29 distillations are identical; the concept index, the `answer-from-corpus` skill, the app's `CLAUDE.md` and four copied docs differ.

- **P, schema 2:** the app as it ships on `main` before this change. The skill reads the whole concept index.
- **Q, schema 3:** the app built on this branch. The skill reads the topics block once, picks topics, fetches their rows by topic ID, and greps a named concept directly.

The arm folders were given neutral names, and no runner was told it was part of a comparison.

## Method

Four questions, one of each shape the skill distinguishes, plus one that turns on a disagreement:

| | Question | Shape |
|---|---|---|
| Q1 | Our leadership team keeps reopening decisions we already made … How do we make decisions stick without shutting down legitimate dissent? | diagnostic |
| Q2 | What does the library say about making decisions under uncertainty and complexity? | synthesis |
| Q3 | What is the Agreement/Uncertainty Matrix, and when should I use it? | named concept |
| Q4 | When a company makes a big decision, should it put shareholders first or weigh all stakeholders? Where do the sources disagree? | disagreement |

Each question ran once per arm: a fresh Claude Opus agent inside the app folder read the app's `CLAUDE.md`, followed its `answer-from-corpus` skill in app mode, and wrote a 300–500 word answer with the skill's trace footer (`receipts/answers/`). Token counts are the agents' own totals (`receipts/tokens.json`).

Judging was blind and cross-family. For each question, `gpt-5.6-sol` (Codex, high effort, read-only) received the question, the rubric (`receipts/rubric.md`), the two answers with trace footers stripped and labelled X and Y in random order, and the shared distillations to check claims against. It scored each answer 1–5 on grounding, coverage, precision and usefulness, listed claims it couldn't support, and picked a winner or a tie (`receipts/verdicts/`). The X/Y key is in `receipts/judge-key.json`. Scripts: `receipts/scripts/`.

## Results

| | Tokens P / Q | Distillations read P / Q | Judge's pick | Rubric total P / Q (of 20) |
|---|---|---|---|---|
| Q1 diagnostic | 187k / 170k | 4 / 3 | Q | 17 / 18 |
| Q2 synthesis | 268k / 240k | 10 / 8 | tie | 20 / 20 |
| Q3 named concept | 112k / 96k | 1 / 1 | P | 19 / 18 |
| Q4 disagreement | 240k / 224k | 9 / 7 | P | 20 / 18 |
| **All four** | **808k / 729k (−10%)** | 24 / 19 | Q 1, P 2, tie 1 | **76 / 74** |

On every question, arm Q read a subset of the distillations arm P read.

What decided the three non-ties:

- **Q1 (Q):** more precise, with a cleaner test for when a decision may be reopened; both answers grounded.
- **Q3 (P):** wording. Q called the distillation's worked example "the app's"; P separated the distillation's inference from the handbook's claim more carefully.
- **Q4 (P):** partly a judging artefact. Q said the concept index files the finance text under "maximise shareholder wealth", which is true of the index, but the judge had only the distillations and marked it unsupported. Q also overstated one source's position.

## Found along the way

- **Both arms hit the same index credit error.** The concept index credits OpenStax *Principles of Finance* with shareholder-wealth and agency-theory concepts its decision-making distillation doesn't carry. The schema-3 debate topic surfaced the error; it didn't cause it.
- **Vocabulary gaps.** Arm Q's greps for groupthink, escalation, consensus and dissent found no concept rows: those ideas live only in distillation text.

## What this round doesn't show

- **Scale.** Demo's index is 41 KB; a large corpus's runs to hundreds of kilobytes, where reading it whole dominates the cost. The token effect there is untested.
- **Variance.** One run per question per arm, one judge. The differences in the three non-ties are the size of run-to-run wording differences.
- **Project mode.** Only app mode ran; project-mode retrieval over references is untested.
