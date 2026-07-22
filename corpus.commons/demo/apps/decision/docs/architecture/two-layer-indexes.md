# Two-layer indexes: catalogue and router

![A hand-drawn notebook page titled "TWO-LAYER INDEXES" in block caps, with the subtitle "catalogue · concept · router · lens — all resolving through one slug-table" underneath. A second handwritten line reads: "operators edit markdown. build regenerates JSON. runtime reads JSON only." Below the title, a long horizontal bar at the bottom of the page labelled `slug-table.json` (caption: "the join key. append-only. 3-char base-36 ID per source.") with four arrows rising upward to four JSON-index boxes arranged left-to-right: `reference-index.json` (catalogue. one record per source. author / year / title / primary topic / concept tags); `concept-index.json` (concept axis. one record per concept. aliases collapsed. per-source section + line pointers); `task-index.json` (situation router. phase rows. (need, slug-id, when) triples. one file per task axis); `lens-index.json` (lens catalogue. notices-first / recedes / native-vocab. operator-authored salience). To the left of three of the four JSON boxes, dashed-outline shadow boxes labelled REFERENCE-INDEX.md, {TASK}-DISTILLATION-INDEX.md, and LENS-INDEX.md, each connected to its JSON with a dashed arrow labelled "built by build script." Between the second and third JSON boxes, a dashed placeholder labelled "(no markdown view)" marking concept-index.json's missing shadow. Off to the right of the page, a separate boxed cluster labelled "Chroma" (vector store. rebuilt from corpus content. not hand-edited. fifth tier — different contract), connected to the slug-table with a thin dotted line. Bottom-right handwritten note: "five files. one slug-table beneath them. each index does one job mechanically." The notebook sits on a wooden desk with a compass-rose ceramic mug top-right, a wooden ruler along the right edge, and a mechanical pencil at the bottom-left edge of the page.](../assets/two-layer-indexes.png)

*The five files and the slug-table beneath them. Three of the four indexes ship with a markdown view operators can browse; `concept-index.json` is the exception (too large to hand-edit). Chroma sits parallel as the fifth tier: vector store, not hand-edited index, different contract.*

## A concrete example first

[`reference-index.json`](../../reference-index.json) answers "What is X?" for the corpus. One entry per source: slug-ID, author, year, title, primary topic, concept tags, scope, line counts.

[`distillations/decision-making/task-index.json`](../../distillations/decision-making/task-index.json) answers "In phase X of a decision, which references should I reach for?" Phase-by-phase rows as `[need, slug-id, when]` triples.

[`concept-index.json`](../../concept-index.json) is the concept axis that sits between the two: per canonical concept, the slug-IDs of every source that covers it, plus body section names and md_line pointers where one can be resolved mechanically.

These three indexes do different jobs and live in different files. The separation is load-bearing.

## Why split them

A single combined index collapses three different lookup tasks:

- *Identification:* "Is there a source in this library that addresses constraints under uncertainty?" The user has a topic; they want the source.
- *Concept lookup:* "Where in the corpus is *Accumulations* discussed?" The user names a concept and wants every source-and-section that treats it.
- *Routing:* "I am in the bounding phase of a decision; what helps?" The user has a situation; they want the right resource for *now*.

If you build one index, the three lookups compete for the same entry shape. The entry either describes the source (good for identification, useless for routing), describes the situation (good for routing, mismatched for identification), or lists concept occurrences (good for concept lookup, doesn't tell you what the source *is about* overall). Most large knowledge bases default to identification entries and then bury the routing logic in prose: *"If you are doing X, this might be useful."* Readers cannot scan that.

Split, each index does its job mechanically:

- The corpus catalogue stays declarative. One record per source, derived from frontmatter.
- The concept axis stays cross-source. One record per concept, with aliases collapsed by a constrained Sonnet pass.
- The task-axis router stays imperative. Rows describe situations and route to source-IDs.

## Two tiers, three indexes, one slug table

The runtime indexes ship as JSON. Operator-inspection views ship alongside as markdown. The runtime reads JSON only; the markdown is for humans browsing the corpus.

| Index | Runtime path | Operator view | Job |
|---|---|---|---|
| Slug table | `references/slug-table.json` | — | Append-only mapping from source slug to 3-character base-36 ID. Resolves every other index's IDs to file paths. |
| Reference index | `reference-index.json` | — | File catalogue. One record per source. |
| Concept index | `concept-index.json` | — | Concept axis. One record per canonical concept; aliases collapsed; per-source section + md_line pointers. |
| Task index | `distillations/{task}/task-index.json` | `{TASK}-DISTILLATION-INDEX.md` | Situation router. Phase-by-phase rows mapping `(need, slug-id, when)`. One file per task axis. |
| Lens index | `lens-index.json` | `lenses/LENS-INDEX.md` | Lens catalogue. One record per lens; `salience` block split from the operator-authored markdown. See *Lens-aware retrieval* below. |

Sitting beneath these four operator-authored indexes is a *fifth* artefact category—the semantic-search backend (Chroma)—that fills a different role. It is not an index the operator hand-edits; it is a vector store rebuilt from the corpus content. The fifth-tier framing and its contract are in *A fourth tier beneath the indexes* below.

The JSON is derived. Operators don't hand-edit it. The build scripts at [`scripts/build_indexes/`](../../scripts/build_indexes/) regenerate every JSON index from the operator-inspection markdown views, the per-source extracted artefacts, and the deep-ref frontmatter. The pipeline is documented in [`ingestion-protocol.md`](ingestion-protocol.md) §Pass H.

## Shape of the reference index

```json
{
  "00h": {
    "slug": "openstax-organizational-behavior",
    "author": "OpenStax / Black et al.",
    "year": 2019,
    "title": "Organizational Behavior",
    "primary_topic": "Applied behavioural science examining individual, group, and organisational factors that shape work behaviour.",
    "concept_tags": ["organisational-behavior", "motivation", "leadership", ...],
    "lines_light": 137,
    "lines_deep": 745,
    "scope": "open-nc"
  }
}
```

Author / year / title / primary_topic / concept_tags come from a Sonnet pass over the deep-ref frontmatter: free-form prose ("Beck et al. (2001)", "Bennett, G., Cougler Blom, B., Riessner, S., & Currie, S. (2019)", "OpenStax with no year") that a regex would get ~90% right and silently mis-attribute the rest. The mechanical fields (slug-table ID, `**Scope:**` line, light/deep line counts) come from Python.

The catalogue is about *the work*. It does not tell you when to use the source.

## Shape of the concept index

```json
{
  "after-action-review": {
    "name": "After-Action Review",
    "aliases": ["aar"],
    "sources": [
      {"id": "005", "context": "FLA / Learning Review four-tool ladder"},
      {"id": "00o", "section": "Chapter 1 The After-Action Review", "md_line": 97}
    ]
  }
}
```

Built in two stages. (1) Python aggregates concept candidates across every source's `extracted artefact`: enumerated-method names (author-curated) plus back-matter book-index entries that appear in ≥2 distinct source slugs (single-source back-matter entries are corpus-level noise). (2) A constrained Sonnet pass adjudicates aliases (e.g., `reflective-system` / `System 2` → `dual-process-theory`; `AAR` → alias of `after-action-review`), filters noise (URL boilerplate, single-letter dividers, generic backmatter terms), and decides novel-vs-existing. The build script then re-attaches section + md_line pointers mechanically: enumerated_method body lines first (highest confidence), heading-tree substring match as fallback, with generic front/back-matter headings (CONTENTS, INDEX, REFERENCES) blocked.

The concept index is about *the corpus's concept vocabulary*. It tells you which sources cover a concept and where in each source the concept's body treatment sits.

## Shape of the task index

```json
{
  "task": "decision-making",
  "sections": [
    {
      "section": "Phase 2: Bounding",
      "columns": ["need", "id", "when"],
      "rows": [
        ["Identify stakeholders affected", "00h",
         "Need to consider whose interests are at stake before generating alternatives."],
        ["Apply the relevant GAAP principle", "00a",
         "The choice involves revenue recognition, expense matching, cost, ..."]
      ]
    }
  ]
}
```

One JSON per task axis. Rows are flat `[need, slug-id, when]` triples: field names live once in `columns`, not per-row, so 1,100 rows don't re-pay scaffolding overhead. The 3-column "quick start" tables that appear in the markdown operator view are dropped from the JSON; they're a redundant view of the same routing surface the phase-by-phase tables already cover.

The task index is about *the situation*. Read it when you have a phase in mind. It tells you which references to reach for and in what order.

## How the indexes work together

The compiled assistant's retrieval pattern at session start:

1. Load the corpus-level JSON indexes: `slug-table.json`, `reference-index.json`, `concept-index.json`. ~28k tokens on the demo corpus; loaded once per session, amortised across every subsequent query.
2. Load the task-axis `task-index.json` for the domain(s) in play. ~17-19k tokens per axis on the demo corpus.
3. For a *named lookup* query, resolve through `reference-index.json` to the slug, then read the light → deep refs.
4. For a *diagnostic* query, route through `task-index.json` for the relevant phase, then read the distillations the rows point to.
5. For a *synthesis* query, decompose into sub-claims, route across `concept-index.json` and `task-index.json` for coverage, then read lights and deeps until each sub-claim has a strong source.

Per-query cost on the demo corpus, post-migration: 28-47k tokens for index reads depending on which axis is loaded, vs ~131k tokens of the pre-migration `.md` indexes. See [`projection-time.md`](projection-time.md) for the steady-state numbers.

## A fourth tier beneath the indexes: semantic search as routing, not content

The semantic-search backend (Chroma) sits *beneath* the curated indexes in the retrieval hierarchy. Order:

1. `concept-index.json` for named-concept lookups.
2. `reference-index.json` for named-reference / topic lookups.
3. `task-index.json` for the task at hand.
4. Semantic search as a safety net for genuinely novel queries the curated indexes did not pre-think-of.

**Status:** steps 1–3 are live; step 4 is designed but not yet wired into runtime. Chroma is built by [`scripts/setup-chroma.py`](../../scripts/setup-chroma.py), but the shipped retrieval skills (`answer-from-corpus`, `matching-references`) currently route through the curated indexes only. The relevance-floor discipline below is the intended behaviour of the fallback tier and the pointer-only contract it must honour once wired.

The principle that makes this clean is the same one that makes the curated indexes work: **the index returns pointers; the file system holds the distillations.** Semantic-search responses carry filenames, authors, titles, and similarity scores, never document bodies. The assistant reads the matched files via the file system before answering.

This contract has three concrete consequences:

- **Responses stay small.** A semantic-search call asking for `n_results: 50` with metadata-only fits comfortably in a tool response. The same call with `documents` included can overflow tool-response size limits and force a silent fallback to grep, which has happened in practice in adjacent projects with the same architecture.
- **A relevance floor becomes informative.** With pointer-only responses, the assistant can ask for many candidates and apply a similarity floor in post-processing. Many candidates above the floor means the corpus serves the query; few or none means it does not. *Zero candidates above the floor is a real signal that the library is silent on the question*. The no-coverage-honest discipline gets enforced at the retrieval layer rather than left to the model's discretion.
- **The mechanism is swappable.** Whether the routing layer is grep, ChromaDB, or some future retrieval backend, the contract is the same: pointers in, file-system reads out. The ChromaDB integration is a pure mechanism change, not an architectural shift.

The principle generalises: **the index is not a content store**, regardless of what mechanism implements it. Standard RAG conflates the two by including chunked content in the search response, which is a soft form of reshape: the search result is the answer chunk. The matrix architecture says: the index returns which distillations to read, the file system holds the distillations, the distillations are what was projected once at ingestion.

## Why JSON, not Markdown, for the runtime

Operator-edited markdown was the pre-migration shape. The migration replaced markdown runtime with JSON for three reasons:

- **Token-cost asymmetry.** Markdown re-pays scaffolding overhead per row (`| col1 | col2 |`, `**bold**`, `---` dividers); JSON pays field names once per section. Slug-IDs (`00h`) replace 30-character filenames at every routing-row mention. Per-query index cost on the demo corpus dropped from ~131k tokens to 28-47k.
- **Mechanical-extraction discipline.** The pre-migration Pass H asked the ingesting LLM to author concept-A-Z entries by inference, which drifted under load: live testing found ~4 canonical post-Agile references with zero concept-index entries despite being in the corpus. JSON's structure makes the data flow auditable: per-source extraction → corpus-wide aggregation → constrained Sonnet cross-link → assembly. Each step has a discrete artefact at a known path.
- **Operator legibility didn't pay its keep for the reference catalogue.** An early version of the catalogue was 223kB of operator-authored markdown. In practice operators inspected it ~once per quarter while the runtime read it on every query. The cost was paid by the runtime; the value was held by the operator. The reference catalogue now ships as JSON only — the `answer-from-corpus` skill is the human interface; the JSON is the runtime interface. Task and lens catalogues retain operator-view markdowns because their authoring loop genuinely sits in markdown.

The operator-inspection markdown views still ship in the source repo and the compiled apps. They're not load-bearing at runtime; they're a backup readable surface for browsing the corpus. The build pipeline regenerates the JSON from the markdown plus the extracted artefacts whenever the operator updates the markdown.

## Lens-aware retrieval

Lenses are per-distillation modifiers applied where they materially reweight what's salient. The index pattern survives the addition unmodified. The task-axis index acquires lens-tagged rows where applicability fires; the reference and concept indexes remain lens-neutral catalogues. The semantic-search layer respects the same routing-not-content contract regardless of lens presence.

The lens index follows the same two-layer pattern: `lens-index.json` is the runtime artefact, `lenses/LENS-INDEX.md` is the operator-inspection view. The JSON is built deterministically from the markdown table by [`scripts/build_indexes/build_lens_index.py`](../../scripts/build_indexes/build_lens_index.py), which splits each row's *Native vocabulary & salience* cell into a structured `salience` block (`notices_first`, `recedes`, `native_vocabulary` as a phrase list). Lens specs themselves remain markdown; they're operator-authored prose reached for via the JSON's `spec_path` field when the query needs the grounding contract, fire-list, or trust-breaking-failure-mode reasoning.
