# Overview: the reference × task matrix

**Runtime is selection, not synthesis.** Two axes: references on one, task domains on the other. Each cell is pre-projected once at ingestion under a structured 9-pass protocol. At query time, the assistant routes to a cell and reads it. The reshape has already happened. *Selection beats reshape* is the constraint claim; the matrix is the architecture that delivers it.

## A concrete example first

Open [`corpus.commons/demo/references/openstax-organizational-behavior-deep.md`](../../corpus.commons/demo/references/openstax-organizational-behavior-deep.md). That is one distillation on the *reference axis*: a single source, ingested once, citations and evidence-classification markers in place.

Now open the [decision-making distillation](../../corpus.commons/demo/distillations/decision-making/openstax-organizational-behavior-decision-making.md) and the [stakeholder-engagement distillation](../../corpus.commons/demo/distillations/stakeholder-engagement/openstax-organizational-behavior-stakeholder-engagement.md). Same source, two different files. Each is the source projected onto one *task axis*: decision-making, stakeholder-engagement. The diagnostic questions, the "what to look for" patterns, and the worked example all differ between the two. Same evidence, two presentations.

That pair of files is one row of the matrix. The demo corpus today projects sources onto five task axes (decision-making, stakeholder-engagement, software-business, aar, retro); the architecture supports as many task axes as a domain needs.

## The architectural claim

Standard RAG retrieves a chunk of source at query time and asks the LLM to assemble an answer. The reshape is paid per query, against context-window pressure, with hallucination risk on every call.

The matrix shifts the projection from query time to ingestion time. For each source, an LLM operating under a structured 9-pass protocol produces (a) a deep reference with verbatim citations and evidence classification, and (b) one distillation per task domain. The distillation is the source already projected: relevance, diagnostic questions, anti-patterns, integration. At query time, selection is the work. The reshape has already happened. Runtime is cheaper because there is no per-query reshape against context-window pressure; the output is more grounded because the projection has been audited under the protocol; and the assistant operates on smaller working context than open-ended retrieval would require.

## Indexes do the routing, and they are derived artefacts, not operator-authored

The runtime ships three corpus-level JSON indexes plus one task-axis JSON per shipped task:

- [`reference-index.json`](../../corpus.commons/demo/reference-index.json) is the corpus catalogue. "What is X?" Author, topic, key claims. Use it to find the reference.
- [`concept-index.json`](../../corpus.commons/demo/concept-index.json) is the concept axis. "Where is concept Y discussed?" Per canonical concept: every source that covers it, plus body section pointers where one can be resolved mechanically.
- The per-task task indexes at `distillations/{task}/task-index.json`, one per task axis the corpus carries (the demo ships five: decision-making, stakeholder-engagement, software-business, aar, retro). Each is a situation-to-resource router: "in phase X of task Y, what should I reach for?" Each compiled app ships the task-index for its profile's axis only.

The split matters. Mixing the three collapses what-is, where-is, and when-to-use into one index and produces the unhelpful list-everything outcome familiar from large knowledge bases. Treated separately, each does its job.

These indexes are *derived artefacts*. The runtime reads JSON; the build scripts at [`scripts/build_indexes/`](../../scripts/build_indexes/) regenerate the JSON from the per-source extracted artefacts, the deep-ref frontmatter, and operator-inspection markdown views (`REFERENCE-INDEX.md`, per-task `{TASK}-DISTILLATION-INDEX.md`) that ship alongside for human browsing. Operators don't hand-edit the JSON; all edits flow through the markdown plus the frontmatter, and the build picks them up. See [`two-layer-indexes.md`](two-layer-indexes.md) for the index design.

## What changes for the assistant at runtime

The build compiles a slice of the matrix per profile. Each compiled profile is an application, a distributable bundle. [`corpus.commons/demo/apps/decision/`](../../corpus.commons/demo/apps/decision/) ships all references plus one column: the decision-making distillations and the per-axis `task-index.json` that routes through them. [`corpus.commons/demo/apps/stakeholder/`](../../corpus.commons/demo/apps/stakeholder/) ships all references plus the stakeholder-engagement column. The corpus-level runtime indexes (`slug-table.json`, `reference-index.json`, `concept-index.json`) are identical across apps; the per-axis task index is what makes the app what it is. The compiled assistant routes via the indexes, reads the distillation, cites back to the deep reference. The runtime skips the per-query reshape, the chunked retrieval over raw source, and the mid-answer mapping of passage to task; the mapping has already been made.

## What changes for the operator at ingestion

The ingestion protocol ([`ingestion-protocol.md`](ingestion-protocol.md)) does the work that standard RAG defers. Source is read in full, not chunked. Citations are verbatim. Evidence is classified (verbatim, author paraphrase, author argument, author example, borrowed-through). A source-only audit catches any claim that drifted away from the text. The distillations are projected from the verified deep reference; they do not re-read the source.

This is paid once per source and read forever after.

## What ships

The repo carries: the build system, the 9-pass ingestion protocol, the operator skills, a 28-source OpenStax-plus-supplementary demo corpus (mostly CC BY-NC-SA 4.0 and CC BY 4.0), five task-axis projections, the lens library, and a per-corpus Chroma collection for semantic-search routing.

The two-axis structure (reference × task) is the load-bearing part of the architecture. Lenses are per-distillation modifiers, not a third axis: a lens is a window with characteristic salience, weighting, and vocabulary (an audience perspective, a role, a methodology stance), applied where the operator declares it materially reweights what's salient for a given distillation. The matrix stays 2D by default; lenses are operator-opt-in per distillation. This preserves the projection-time argument (distillations are pre-projected where it's worth it) without committing to "every lens pre-projected against every distillation" (expensive maximalism) or "all lenses applied at retrieval" (which gives back the projection-time gain).

Semantic search via Chroma sits beneath the curated indexes in the retrieval hierarchy, not above them. The curated index entries are the operator's pre-thought-of routing; semantic search is the safety net for genuinely novel queries. It is built by `setup-chroma.py` but not yet wired into the shipped retrieval skills, which currently route through the curated indexes only. See [`two-layer-indexes.md`](two-layer-indexes.md).

For the cost-curve argument against standard RAG, see [`projection-time.md`](projection-time.md). For the worked matrix-pattern example, see [`matrix-pattern.md`](matrix-pattern.md). For the indexing layer, see [`two-layer-indexes.md`](two-layer-indexes.md). For the integrity rule that gates the whole system, see [`source-integrity.md`](source-integrity.md). For *why* the matrix exists (the underlying epistemological problem the architecture is solving against), see [`llm-epistemology.md`](llm-epistemology.md).
