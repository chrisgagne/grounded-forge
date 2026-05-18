<!-- markdownlint-disable MD024 -->

# Decisions and non-decisions

The architectural choices in this repo are easy to read by looking at what shipped. The choices *not* shipped—the alternatives considered, weighed, and turned down—are harder to recover from the code. This page makes them explicit.

The bar for inclusion: an option that a reasonable AI engineer would expect to see, plus a reason it isn't here. Decisions live on the left; the reasoning lives on the right. Where a non-decision is genuinely interesting (the bet had a real upside), the reasoning carries the cost-benefit, not a dismissal.

For the grammar that names what *did* ship (source, reference, distillation, application, lens), see [`docs/reference/vocabulary.md`](../reference/vocabulary.md).

---

## Retrieval architecture

### Decision: matrix pre-projection at ingestion time

Ingest the source once, project it onto each task axis at ingestion, store the projection as a file on disk. At query time, route via curated indexes and read the already-projected distillation. The reshape from source to task happens once per source, not once per query.

The architectural argument is in [`overview.md`](overview.md), [`projection-time.md`](projection-time.md), and [`matrix-pattern.md`](matrix-pattern.md). The protocol that produces each distillation is in [`ingestion-protocol.md`](ingestion-protocol.md). The grammar is in [`docs/reference/vocabulary.md`](../reference/vocabulary.md).

### Considered: standard RAG (retrieve-and-reshape at query time)

Standard RAG retrieves a chunk of source at query time and asks the LLM to assemble an answer. It is the right pattern when the question space is unbounded, the task domain is unknown in advance, or the corpus changes faster than ingestion time. For the use case this repo addresses—repeated work in a known set of task domains—the per-query reshape is repeated waste. See [`projection-time.md`](projection-time.md) for the cost-curve framing and the conditions under which standard RAG remains the right tool.

### Considered: vector-store-only retrieval

A vector store can answer "find me documents similar to this query" without the operator authoring any indexes. The matrix instead bets that an operator who has already paid the curation cost (writing the per-task distillation index) gets better routing than an embedding model can guess at. The bet is in [`two-layer-indexes.md`](two-layer-indexes.md): the curated indexes do *what-is* and *when-to-use* routing that a vector store can't recover by similarity.

The semantic-search backend (Chroma, see below) sits *beneath* the curated indexes as a safety net for genuinely novel queries, not above them. That ordering is the load-bearing commitment.

### Decision: Chroma as the semantic-search backend, default-on, regenerated on clone

Embed each corpus into a Chroma collection persisted at `{corpus_root}/chroma/`. Chroma lives *inside* the corpus, not at the repo root: it is corpus-bound data, parallel to references and distillations, and travels with the corpus when the corpus moves between tiers. The DB is gitignored everywhere; it is a derived index, regenerated on clone with one command (`python3 scripts/setup-chroma.py` for the demo corpus, `--corpus {path}` for any other). The recipe ships, the index does not.

The decision to regenerate-on-clone rather than ship the index: vectors are model + library-version bound, so a forker with a different chromadb version or a different embedding function would get unusable vectors. Provenance is also auditable when the recipe is what ships, because operators can see what was embedded by reading the script, where a tracked binary index would have to be trusted on faith.

Default embedding function is chromadb's `DefaultEmbeddingFunction` (ONNX runtime, `all-MiniLM-L6-v2`, ~80MB downloaded to per-machine cache on first call). No PyTorch, no sentence-transformers dependency in the default path. First-clone setup is ~30s for the demo corpus after the ONNX cache warms.

### Considered: ship a cross-encoder reranker by default

A cross-encoder reranks vector-similarity candidates by scoring `(query, candidate)` pairs more accurately than embeddings alone. The quality bump is real on synthesis queries where multiple candidates cluster at similar distances. Cost is the sentence-transformers / PyTorch stack (~hundreds of MB) and one extra model load per session.

The flag exists (`setup-chroma.py --check --rerank`) but is opt-in, not default. The honest framing: this has been thought about, but the tokens haven't been burned to evaluate whether the quality bump justifies the install size for *this* corpus shape. A fork that runs the comparison and reports back closes that loop.

---

## Source integrity

### Decision: 9-pass ingestion protocol with source-only audit

Every reference is produced by a protocol that reads the full source, attaches a citation to every non-trivial claim, classifies evidence by type (`[V]`, `[AP]`, `[AR]`, `[AE]`, `[BT]`), and refuses to ship anything that fails a final source-only audit (Pass I). The protocol is in [`ingestion-protocol.md`](ingestion-protocol.md); the rationale is in [`source-integrity.md`](source-integrity.md).

### Decision: PreToolUse hook gating deep-ref writes

A structural validator at `.claude/hooks/validate-deep-ref.py` fires *before* every Write or Edit against `references/*-deep.md`, predicts the post-write content from the tool input, and blocks the call with stderr feedback if structural contracts are violated (frontmatter present, citation tail after each blockquote, evidence markers well-formed, no `TODO` / `[citation pending]` artefacts).

Discipline lives at write time, not only at audit time. The Pass I audit is *model-level* and runs once per ingestion; the hook is *deterministic* and runs every time a deep reference is touched. Three layers of source-integrity discipline reinforce each other:

1. **Deterministic gate** (this hook): blocks structurally bad writes pre-emptively.
2. **Heuristic critic** (`scripts/audit-deep-ref.py`): runs on demand, finds claim-line weaknesses, citation gaps, drift words. Has false positives by design; operator decides what to fix.
3. **Model-level audit** (Pass I): reads the deep ref cold and verifies every claim traces to the source.

### Considered: claim-line coverage in the hook

The same heuristic the audit script runs (every non-trivial claim must have a citation marker or parenthetical) was considered for the hook. Rejected: the hook needs to be fast and false-positive-free, otherwise the first thing the operator does is disable it. Heuristics belong in the on-demand audit, not in the write-time gate. The structural / heuristic / model-level split is the discipline this gets right.

### Considered: blanket prohibition on training-data assertions

A naive guardrail would scan deep references for unsourced confident claims and block them. The protocol does this work model-side (Pass I), where the model can read a passage and check the trace. A hook can't tell the difference between an unsourced confident claim ("Kahneman shows that…") and a sourced confident claim ("Kahneman shows that…(Ch 3, p. 47)"); both are surface-shaped the same. Anything stronger than the structural check belongs in the on-demand audit.

---

## Multi-agent orchestration

### Decision: parallel subagents at ingestion via the Task tool

The `ingesting-resources` skill dispatches a subagent per source for parallel ingestion at the empirical sweet spot of 4–5 simultaneous Opus 4.7 subagents (rate limits drop requests above that; coordination overhead dominates below). Per-source staging files for shared indexes prevent read-modify-write races on canonical files; a consolidator pass merges staging into the canonical indexes after all sources finish. See `.claude/skills/ingesting-resources/SKILL.md` § *Parallel-batch operations*.

### Considered: Claude Code agent teams

Agent teams—a current Claude Code experimental feature (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, v2.1.32+)—coordinate multiple independent Claude Code sessions via a shared task list, mailbox, and file-locking. A "lead" session creates the team; teammates work independently and message each other. Split-pane visualisation runs in tmux or iTerm2.

The fit looked plausible: a lead coordinating ingestion across 6 teammates each handling 2 books in parallel, with inter-teammate messaging for cross-reference discovery. Rejected for this repo because:

1. **Experimental status, brittle preconditions.** A public-repo demo that requires an experimental env var and either tmux or iTerm2 trades reliability for novelty. The first 30 seconds of clone-and-run is where the architectural argument lands or doesn't; "set this env var, install tmux, then…" is friction the README absorbs.
2. **Wrong wow factor for the audience.** The headline claim is *retrieval quality and source-integrity discipline*, not parallel orchestration. A reviewer evaluating "AI assistants trained on content" cares about how grounded the answers are, not how cleverly the ingestion was parallelised.
3. **Single-session subagents already cover the parallel-ingestion need.** 4–5 Opus 4.7 subagents fan out cleanly via the Task tool with per-source staging files. The marginal benefit of true multi-session agent teams over within-session subagents is small at this corpus scale.

The decision is reversible: a later release with a corpus large enough that within-session subagent rate limits become the binding constraint could revisit. For now, the within-session pattern is documented, working, and shipped.

### Considered: programmatic orchestration via the Claude Agent SDK

The Claude Agent SDK (Python / TS) lets you build agent loops outside Claude Code. Useful for production systems with custom interfaces. Not relevant here: this repo *is* a Claude Code artefact. The skills, hooks, and plugin manifest are first-party Claude Code surfaces.

---

## Distribution

### Decision: ship as a Claude Code plugin

`.claude-plugin/plugin.json` is the manifest. The plugin auto-discovers skills under `.claude/skills/`, hooks declared in `.claude/settings.json`, and the rest of the bundled config. Installable via `/plugin install` once published; for the moment, clone-and-run works identically because the repo *is* the plugin layout. The cost of adding the manifest is negligible; the benefit is the one-command install path for someone forking the architecture.

### Decision: multiple build profiles as proof of the matrix pattern

The demo corpus ships five public build profiles in `corpus.commons/demo/apps/` — `decision`, `stakeholder`, `software-business`, `aar-mode`, `retro-mode` — each a compiled assembly carrying all references plus one task-axis's distillations and per-axis index. The build is `node build.js --all`; the demonstration is `diff -rq corpus.commons/demo/apps/decision/ corpus.commons/demo/apps/stakeholder/`. Same references across all five; the distillations directory, the per-axis task-index, and the CLAUDE.md template differ per profile. The matrix architecture made visible at the file system.

A sixth task axis would be a new column with a new build profile, not a new repo. The cost of an additional column is one operator decision (what is this task axis for?) plus one ingestion run per existing source plus an updated or new application entry in `builds.yaml` (one application can include multiple task axes). The reference axis is shared across columns.

### Considered: audio hooks (Stop / Notification) on Mac

A Sonnet-drafted todo proposed audio notifications on session-end. Rejected: cute, irrelevant to the architectural pitch. A reviewer evaluating retrieval architecture is not moved by "my Mac dings when ingestion finishes." Reverse course if a use case appears.

### Considered: shipping demo transcripts

Capturing 3–5 `/answer-from-library` transcripts (one Named lookup, one Diagnostic, one Synthesis) as static markdown so a reviewer who can't clone-and-run still sees the system working. Deferred to a later push, not because the artefact is wrong, but because operator-led capture against the live corpus has more credibility than scripted output. The Chroma `--check` path provides a smaller version of the same demonstration: a reviewer who runs `python3 scripts/setup-chroma.py --check` sees natural-language queries route to pre-projected distillations, without involving Claude Code at all.

---

## What's not yet decided

- **Reranker evaluation against this corpus.** Whether the cross-encoder rerank meaningfully improves retrieval over the curated indexes + chromadb default has not been measured. The flag is shipped; the comparison is open.

---

## How to read this page

The pattern is this. Where two reasonable options existed, the chosen one gets a one-line statement and a link to the architectural document; the rejected one gets a paragraph that names the cost it would have imposed. The asymmetry is intentional. The decisions speak through the code; the non-decisions speak through this page.
