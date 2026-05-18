# The 9-pass ingestion protocol, rationale

The runbook is at [`.claude/skills/ingesting-resources/SKILL.md`](../../.claude/skills/ingesting-resources/SKILL.md). This document explains *why* the runbook is shaped the way it is. The two files are paired; running the protocol without the rationale produces an operator who follows steps without judgment, and reading the rationale without the runbook produces theory that does not land on a file.

## A concrete example first

An OpenStax source produces three files in this order (using *Organizational Behavior* as the worked example):

1. The deep reference at [`references/openstax-organizational-behavior-deep.md`](../../references/openstax-organizational-behavior-deep.md).
2. The light reference at [`references/openstax-organizational-behavior.md`](../../references/openstax-organizational-behavior.md).
3. One distillation per task axis: the [decision-making projection](../../distillations/decision-making/openstax-organizational-behavior-decision-making.md) and the [stakeholder-engagement projection](../../distillations/stakeholder-engagement/openstax-organizational-behavior-stakeholder-engagement.md).

Each is the same shape across the 26-source demo corpus.

## Why projection at ingestion, not at query

Standard RAG retrieves a chunk of source at query time and asks the model to assemble an answer. The reshape runs once per query, against context-window pressure, with hallucination risk on every call. If the same source is read by 1,000 queries, projection runs 1,000 times.

The matrix shifts that work to ingestion. For each source, the 9-pass protocol produces a deep reference with verbatim citations, a derived light reference, and one distillation per task axis. Runtime is selection, not synthesis. If the same source is read by 1,000 queries, projection still runs once.

The trade is operator time at ingestion against runtime cost forever after. The bet is that the same sources are read for the same handful of tasks repeatedly, and the work of mapping source to task is worth doing once and reusing. See [`docs/architecture/projection-time.md`](projection-time.md) for the full cost-curve argument.

## Why source-only

The whole value of a reference in this library is that "from the source" means what it says. Without a structural enforcement, training priors leak in: biographical asides the source never states, historical context the author never provides, connections to other authors the source never cites. None of those are obviously wrong; that is what makes them dangerous. They are plausible, they make the output read more naturally, and they cannot be audited because they are not grounded in any text.

The protocol's source-only discipline is structural rather than aspirational. The deep reference cites every non-trivial claim. Each claim carries an evidence-class marker that says how the source supports it: verbatim ([V]), author paraphrase ([AP]), author argument ([AR]), author example ([AE]), or borrowed-through ([BT]). Pass I (the source-only audit) reads the finished deep reference cold and refuses to ship anything that fails the trace test. Light and distillations inherit the discipline because they derive from the audited deep without re-reading the source.

This is the same rule documented in [`docs/architecture/source-integrity.md`](source-integrity.md). The protocol is how the rule lives in the procedure.

## Why nine passes

Each pass exists for a reason. The naming below corresponds to the sections in the runbook.

- **Pass A: Context.** Confirming what the source is and that the full source is available, *before* any reading begins, prevents silent partial coverage from contaminating downstream work. A partial deep ref that claims completeness is worse than no deep ref at all. Pass A also captures the source's licence (the upstream legal status) and the operator's distribution scope (one of `open`, `open-nc`, `copyrighted`, `confidential`, `personal`); both ride on the deep ref. Licence governs attribution and derivative-rights; scope is a mechanical filter the build reads at compile time. They usually correlate but can diverge: a CC BY paper used inside a confidential engagement is Licence `CC BY 4.0`, Scope `confidential`. See [README.md](../../README.md#distribution-scope) for the taxonomy. Pass A optionally runs the *discovery scan*: a one-time Sonnet pass over the converted source that emits `_planning/discovery/{slug}.json` describing what author-curated artefacts (book index, page markers, headings, enumerated methods) survived conversion. The discovery JSON feeds Pass H's deterministic preprocessor; the scan re-runs on Pass H if Pass A skipped it.
- **Pass B: Structural read.** Mapping the source's shape before reading for content keeps the deep read oriented. The author's named cases, signature contrarian positions, and citation lineage are signposts that the deep read uses; without them, the deep read drifts.
- **Pass C: Deep read with citations.** Reading the source in full and attaching a citation to every non-trivial claim is where the source-only discipline is built. Every later pass operates on cited material.
- **Pass D: Blockquote extraction.** Selecting the small number of passages that warrant verbatim treatment, and verifying their exactness against the source, gives the deep ref its load-bearing evidence. Blockquotes are expensive (they take space and risk introducing transcription errors); doing this in a dedicated pass keeps the discipline visible.
- **Pass E: Synthesis.** Assembling Passes A-D into the canonical deep-reference structure (thesis, parts, key statistics, connections, framed-against positions). The structure is uniform across the corpus so downstream consumers know where to look.
- **Pass F: Light-reference derivation.** Deriving the light ref from the verified deep without re-reading the source. The light ref is the file most queries will read first; producing it from the audited deep, not from the source, is what guarantees the light ref inherits the source-only discipline.
- **Pass G: Distillation projection.** Producing one distillation per task axis. The projection from source-vocabulary to task-vocabulary happens here. Library-level synthesis (cross-reference integration) is permitted in this tier because distillations are derivative work; the deep tier remains faithful summary.
- **Pass H: Cross-reference.** Driving the mechanical-index pipeline so the new source is routable from the runtime JSON indexes. Pre-migration, Pass H asked the ingesting LLM to author REFERENCE-INDEX entries and concept-A-Z pointers by inference and update per-task distillation indexes by hand. That shape drifted under load (live testing found canonical post-Agile references with zero concept-index entries despite being in the corpus) and confused the boundary between mechanical work and semantic work. The current shape splits the work explicitly: Python does the structural extraction and the index assembly; constrained Sonnet passes do the semantic work that needs LLM judgment. Step-by-step in the [runbook](../../.claude/skills/ingesting-resources/9-pass-protocol.md) §Pass H. Two Sonnet steps inside Pass H: the *refs pass* (per-source frontmatter → `{author, year, title, primary_topic, concept_tags}`, delegated because frontmatter prose varies by source and a regex would mis-attribute silently) and the *cross-link pass* (corpus-wide concept aliasing and novel-vs-existing decisions, the architectural-meat step the spec calls out as non-substitutable by regex).
- **Pass I: Source-only audit.** A final guard that reads the deep reference cold and refuses to ship anything that fails the trace test. Every prior pass is one model session, and the audit is the structural enforcement that catches what those sessions missed.

The split between deep-ref-producing passes (A-E), derived-artefact passes (F-G), corpus-integration (H), and audit (I) is what lets the protocol amortise cost across artefacts. Passes F and G do not re-read the source; the deep reference is the single source of truth for everything downstream.

### A note on the discovery scan's tier recommendation

The Pass A discovery JSON carries a `pass_h_tier_recommendation` field that names which mechanical-extraction tier (anchor-linked, page-marker-resolved, flattened-plaintext, inference-only) the scan thinks the source falls into. **Do not route Pass H from that field.** A 288-source scan during the mechanical-index migration showed ~57% drift between the recommendation and the canonical tier vocabulary; the field is noisy because the scanning agent's tier vocabulary varied. The deterministic preprocessor at [`scripts/mechanical_index/dispatch.py`](../../scripts/mechanical_index/dispatch.py) instead reads `book_index.shape`, `page_markers.present`, and `headings.quality` directly: the underlying observations the recommendation should have been computed from. Multi-tier sources fall out naturally: Forsgren's *Accelerate* has an anchor-linked List-of-Figures, a plaintext Quick Reference, and a flattened-plaintext back-matter index, and every applicable handler fires. The recommendation field is retained for diagnostic logging only; routing trusts the observations.

## What this replaces

In standard RAG, none of these passes happen. The system retrieves a chunk and asks a model to assemble an answer at query time. The reshape, the citation discipline, the evidence classification, and the audit all run (or do not run) inside one query-time generation.

The matrix moves the work to ingestion. Citation discipline is enforced, evidence classification is recorded, and the audit runs once per source. Runtime is lookup.

## When the protocol is the wrong tool

- **Open-domain Q&A.** If the question space is unbounded and the task domain is unknown in advance, you cannot pre-project. RAG remains the right pattern.
- **High-velocity sources.** If the corpus changes faster than ingestion time, the projection is stale before it ships.
- **Single-projection use.** If a source is read for one task only, the matrix overhead is not earned. A single distillation plus a light ref is enough.

## Cost of ingestion (observed)

The protocol amortises cost over query-time use; that means it pays its full cost upfront. Concrete numbers from the May 2026 OpenStax pilot ingestion (the corpus has since grown to 26 sources with five task axes; the numbers below describe the original 12-book + two-axis baseline):

- **Sources:** 12 OpenStax books, 165–995 source pages each (mean ~480 pages), ~5,800 source pages total.
- **Output:** 8,602 deep-reference lines across the 12 books (mean ~717 lines per deep ref); plus 12 light references, 24 distillations (12 books × 2 axes at the time of the pilot), 12 Pass A ledgers, 12 Pass H verifications, 12 Pass I audit logs.
- **Wall-clock:** the pilot landed at 20:32 on 2026-05-05; the remaining 11 books landed at 01:36 on 2026-05-06, giving ~5h 04min for 11 books, or roughly 28 min wall-clock per book when run in parallel batches of 3-5 sub-agents. Extrapolated, ~5h 30min total wall-clock for the 12-book corpus.
- **Model and effort:** Opus 4.7 at `xhigh` effort with adaptive thinking. Token cost not separately recorded; estimable from line counts and OpenStax pricing if needed.
- **Operator effort:** the per-book ingestion is largely orchestrated: kick off the skill, watch the run summary, intervene at the borderline applicability calls. The load-bearing operator decision is made *before* any source is ingested: which task axes does the corpus project onto, and what do those axes mean? That decision is made once at corpus-design time and lived with forever after. Per-source ingestion is mechanical; the axis design is where the operator's skill lands. (The framing is Bainbridge's, *Ironies of Automation*, 1983: as you automate the routine work, the residual human work concentrates in the design choices that the automation cannot make for you.)

A fork ingesting a 12-source corpus at similar scale should expect roughly half a day of wall-clock plus an Opus 4.7 token bill in the low hundreds of dollars; a fork ingesting one source for a hand-curated personal library should expect about half an hour and a few dollars.

The architectural choice is whether the stable structure is the *source* or the *task*. The matrix bets on the task. The 9-pass protocol is what the bet pays for.
