# Projection time: ingestion versus query

![A hand-drawn cost-curve sketch in a working notebook, titled "Projection-time". Three curves are plotted on hand-ruled axes (cost ↑ vs queries →): "file-by-file + grep" rises steeply from near the origin (grounded, but pays every time); "matrix" starts high on the y-axis and rises gently across the page (grounded once at ingestion, cheap after); "RAG" runs parallel to matrix at a lower offset (cheap, ungrounded). A small arrow labelled "break-even ~?" points to where grep crosses matrix. Two handwritten captions below the plot: "the win isn't cost. it's grounding at cost-parity with the cheapest alternatives that ground at all." and "first principles. measured comparison TBD." Pencil portraits of two ragdoll cats named "lila" and "yana" with a small heart between them sit in the bottom-right corner. Same notebook, desk, ruler, and compass-rose mug as the matrix page.](../assets/cost-curves.png)

*Same notebook as the matrix page. The shape is the argument; the numbers will follow.*

## A concrete example first

Open [`corpus.commons/demo/distillations/decision-making/openstax-organizational-behavior-decision-making.md`](../../corpus.commons/demo/distillations/decision-making/openstax-organizational-behavior-decision-making.md). The "Phase 2: Bounding" table contains diagnostic questions for managerial decision-making, projected from [`corpus.commons/demo/references/openstax-organizational-behavior-deep.md`](../../corpus.commons/demo/references/openstax-organizational-behavior-deep.md)'s Part on Decision-Making (Ch 6 of the OpenStax source), where the underlying concepts appear in the source narrative. The projection from source narrative to diagnostic question is the work. In standard RAG, that work runs at query time. Here it has already run.

This document compares the two cost curves and names the conditions under which the matrix wins.

## Standard RAG: pay per query

The canonical RAG pipeline retrieves chunks from a vector store, concatenates them with the user's query, and asks the model to synthesise an answer. The synthesis happens once per query, and the operator pays three costs in parallel. Multiple chunks fight for tokens against the user's query and the system prompt, so recall trades off against precision. The model decides how to map source passages onto the user's question on every query, and if the task domain is unusual, training-priors bleed in. And the same passage, retrieved twice for two different queries, can produce two inconsistent characterisations, because citation discipline is enforced (or not) at generation time, not at ingestion.

The cost curve is roughly linear in query volume. If the same source is read by 1,000 queries, projection runs 1,000 times.

## The matrix: pay once at ingestion

The 9-pass ingestion protocol ([`ingestion-protocol.md`](ingestion-protocol.md)) inverts the cost curve. For each source:

1. Read the source in full, not in chunks.
2. Produce a deep reference with verbatim citations and evidence classification (`[V]` verbatim, `[AP]` author paraphrase, `[AR]` author argument, `[AE]` author example, `[BT]` borrowed-through).
3. Produce a light reference derived from the verified deep.
4. Produce one distillation per task domain, projecting the source onto that task's diagnostic questions, anti-patterns, and integration with sibling sources.
5. Run a source-only audit pass that fails if any claim cannot be traced.

The cost is amortised across every future query. If the same source is read by 1,000 queries, projection still runs once. The trade is operator time at ingestion against runtime cost forever after.

## What this looks like at runtime

The compiled assistant routes via the distillation index, reads the distillation, cites back to the deep reference. The model is selecting from prepared distillations, not assembling them. Smaller context windows do real work: loading the distillation plus the relevant section of the deep is enough for most queries, and vector retrieval over chunked raw source becomes optional. The hallucination surface shrinks because the reshape has already been audited and the model is no longer the projection layer. Citation discipline is structural rather than performative: every claim in a distillation traces, by construction, to a marked passage in the deep reference.

## Routing cost is amortised across the session, not paid per query

The runtime indexes load once and stay in context. Subsequent queries in the same session route against the already-loaded indexes: no second read, no second tokenisation. The same is true of any distillation the user has already pulled into the conversation. The routing tax that finding 1 in the [README's *Audit receipts and evals*](../../README.md#audit-receipts-and-evals) charged against the matrix on canonical material is a *first-query* cost; the second and subsequent queries on related topics pay only the incremental read of any new distillation the index points to.

Concrete numbers post-migration (May 2026, demo corpus, 27 sources):

| Indexes | Tokens (cl100k_base) | Loaded |
|---|---|---|
| Corpus-level (slug-table + reference-index + concept-index) | ~28k | Every session, once. |
| Per-axis task index (decision-making / stakeholder-engagement / software-business / aar / retro) | ~17-19k each | Per task domain in play, once. |
| **Per-query first-load (corpus-level + one task axis)** | **~28-47k** | First query in the session. |
| Per-query nth-load | ~0 (incremental distillation reads only) | Subsequent same-session queries. |

The pre-migration `.md` baseline was ~131k tokens for the same indexes loaded per query; the *amortisation argument was sound but it compounded against a 4× larger first-load cost*. The mechanical-index migration (Phase 4 of the migration, May 2026) collapsed the first-load by switching the runtime indexes from markdown to JSON, introducing slug-ID compression, and dropping the redundant 3-column "quick start" tables that re-said what the phase-by-phase tables already routed. Per-query token ratio: **34-36% of the .md baseline** on the demo corpus, **48.9% in the aggregate-all-axes worst case**. Index design at [`two-layer-indexes.md`](two-layer-indexes.md).

Session amortisation compounds with the migration's per-query gain. A four-query session in the decision-making domain pre-migration paid ~131k tokens on the first query and ~131k tokens of cached re-read on each subsequent query (cache hit, but still on the larger surface). The same session post-migration pays ~45k on the first query and ~45k of cached re-read on the rest. The per-query saving multiplies across the session, not just against the first answer. This is the matrix's value-add on the work it was designed for—repeated work in a known task domain across a session—and it shows up most clearly there, least clearly on isolated one-shot queries where the index load amortises against a single answer.

## What this argument can and cannot show

The cost-curve framing is argued from first principles: ingestion cost is paid once per source under audit; query cost is paid per question against the projected distillation rather than against raw chunks. The architecture's commitment is that this trade pays off for the use case it targets: repeated work in known task domains where the same sources get re-read for the same handful of tasks.

The architecture has *not* produced a measured per-query token comparison against standard RAG on the same corpus and queries. That measurement would be the obvious confirmation of the cost-curve claim. Two things stand in its way. First, the comparison is shape-mismatched: standard RAG's per-query cost is dominated by chunk retrieval and assembly tokens, while the matrix's per-query cost is dominated by the distillation read; comparing them at the token level requires a fixed quality bar, and quality measurement runs into the limit named below. Second, the architectural-quality metric the matrix is built to defend (per-claim auditability against operator-curated material) is structurally invisible to the single-LLM-as-judge rubric the eval harness uses; the verification surface and the architecture's defence are the same thing. The eval section in the [README's *Audit receipts and evals*](../../README.md#audit-receipts-and-evals) names this finding directly (finding 4).

The honest position: the cost-curve argument holds at the artefact level (the ingestion cost is real, dated, recorded; the query path is shorter than RAG's by construction); the per-query measurement that would confirm it numerically is a target for the next eval-rubric rework, not for the current release.

## Closest published cousins

- **Andrej Karpathy, "LLM Wiki" gist** (4 April 2026). Karpathy argues for compiled, lookup-shaped knowledge artefacts over retrieve-and-reshape pipelines. The matrix is a concrete realisation of that argument with task-axis projection added.
- **RAG+** ([Wang et al., "RAG+: Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning", EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1630/)). RAG+ adds an application step to standard RAG, retrieving usage examples alongside source chunks. The matrix moves the application step from retrieval time to ingestion time.
- **Anthropic Skills** (Zhang and Murag, "Don't Build Agents, Build Skills Instead", AI Engineer talk, 2026). Skills as compiled, file-system-dispatched artefacts. The matrix uses the same dispatch shape: a set of pre-projected files, selected by index, read on demand.
- **Jerry Liu, "Files Are All You Need"**. Closest framing for file-system retrieval as an alternative to vector-store retrieval. The matrix lives entirely on the file system.

Three older traditions sit close enough that distinguishing the matrix from each is worth doing once. The Cyc-style microtheory tradition (Lenat & Marcus 2023, arXiv:2308.04445) builds logically partitioned predicate calculus; the matrix's task-axis projections are natural-language distillations derived from prose. Clancey's strategic-vs-domain knowledge separation (Clancey, AI Magazine 7(3), 1986) splits along reasoning role; the matrix's two axes are *source* and *task*. The stochastic-parrots critique (Bender et al., FAccT 2021) targets generative fluency without grounded reference; the 9-pass source-only audit gates fidelity to source, not source to world. The full citations and architectural insights for each are in the [README's prior-art section](../../README.md#prior-art).

## When the matrix is the wrong tool

- **Open-domain Q&A.** If the question space is unbounded and you do not know the task domain in advance, you cannot pre-project. RAG remains the right pattern.
- **High-velocity sources.** If the corpus changes faster than ingestion time, the projection is stale before it ships. The matrix wants reasonably stable sources (books, papers, methodology documents).
- **Single-projection use.** If a source is only ever read for one task, the matrix architecture is overkill; a single distillation plus a light ref is enough.

The architectural choice is whether the stable structure is the *source* or the *task*. The matrix bets on the task: the same sources are read for the same handful of tasks repeatedly, and the work of mapping source to task is worth doing once and reusing.
