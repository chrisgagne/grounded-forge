# Vocabulary

The grammar this repo uses. Read this once; the rest of the architecture docs assume it.

## Nouns and the verbs that produce them

| Layer | Noun | Verb |
|---|---|---|
| Inputs | **source** (original + converted form) | *convert* |
| Library, layer 1 | **reference** (deep + light) | *ingest* |
| Library, layer 2 | **distillation** | *distil* |
| Modifier on distillation | **lens** | a lens *shapes* a distillation |
| Final product | **application** | *assemble* / *build* |

A *source* enters as an original (PDF, EPUB, HTML) and is *converted* to markdown (markitdown or pymupdf4llm). The converted form is read by the 9-pass ingestion protocol, which *ingests* the source into a pair of **references**: the deep reference (full-coverage, verbatim quotes, evidence markers, citation-ready) and the light reference (fast-orientation summary derived from the deep). References are task-neutral and lens-neutral; they describe the source.

A reference is *distilled* for a task axis, producing one **distillation**: the essential aspects of the reference for that task. Optional **lenses** further shape a distillation (audience perspective, role, methodology stance). A lens is not an axis; it is a per-distillation modifier applied where the operator declares the lens materially reweights the distillation.

Lenses come in three kinds, distinguished by where the lens's intelligence comes from and how the lens speaks (or doesn't):

- **Personifiable-archetype.** A role-in-circumstance lens, e.g. *engineering manager 48 hours after a P0 incident*. The lens reads *as if* the role were reading, given the named circumstance. The constraint that makes the lens useful is the circumstance, not the role label.
- **Named-real-person.** A lens grounded in a specific person's published material, e.g. *Jane Doe, CFO at Acme, from her LinkedIn page and three posts*. The source material is cited and treated as a mini-reference. The lens reads *as if Jane Doe were reading, given what her public material reveals*, not *as* Jane Doe. Ventriloquism is the named failure mode.
- **Non-personifiable-frame.** A structural lens applied to situations, e.g. *loss-aversion lens*, *queue-physics lens*. The frame reads through a principle; no first-person voice, no idioms. The frame's refusal—what it does not read—is part of the lens spec.

Lens specs live at `lenses/{lens-slug}.md` and are designed under the `creating-lenses` skill at [`.claude/skills/creating-lenses/SKILL.md`](../../.claude/skills/creating-lenses/SKILL.md).

An **application** is the distributable bundle an operator ships. The demo corpus ships five (`decision`, `stakeholder`, `software-business`, `aar-mode`, `retro-mode`), each at `corpus.commons/demo/apps/{profile}/`. An application is composed of: a corpus of references, distillations of those references for the application's task axes, optionally lenses that shape those distillations, and a runtime configuration (CLAUDE.md, build profile, distribution metadata). One application can include multiple task axes; the same reference can appear twice in one application, distilled through two different tasks.

## Matrix axes

| Axis | Name |
|---|---|
| Rows | **reference axis** |
| Columns | **task axis** |
| Modifier | **lens** (not an axis; a per-distillation modifier) |

The matrix is 2D: reference × task. Each distillation is one distillation. A lens optionally shapes a distillation at projection time.

An application is *not* a column of the task axis. An application is *assembled across* the matrix: pick references (rows), pick tasks (columns), optionally pick lenses, configure the runtime, build the distributable.

## Indexes

The runtime indexes are JSON; the operator-inspection views alongside them are markdown.

| Index | Runtime path (JSON) | Operator-inspection (Markdown) | Job |
|---|---|---|---|
| Slug table | `references/slug-table.json` | — | Per-corpus mapping from source slug to short 3-character base-36 ID. Append-only; deletions leave a tombstone. The build, ingestion, and runtime skills resolve every other index's source IDs through this table. |
| Reference index | `reference-index.json` | `references/REFERENCE-INDEX.md` | Corpus catalogue. "Is there a reference on X?" Per source: author, year, title, primary topic, concept tags, scope, line counts. |
| Concept index | `concept-index.json` | (no .md) | Concept axis. Per canonical concept: aliases, sources, and section + md_line pointers into each source where one can be mechanically resolved. |
| Per-task task index | `distillations/{task}/task-index.json` | `{TASK}-DISTILLATION-INDEX.md` | Situation router. "For phase Y of task Z, which distillation should I reach for?" Phase-by-phase routing rows as `[need, slug-id, when]` triples. |
| Lens index | — | `lenses/LENS-INDEX.md` | Lens catalogue and applicability heuristics. Operator-authored prose; stays markdown. |

The JSON runtime indexes are *derived artefacts*: produced by `scripts/build_indexes/` from the per-source extracted artefacts (Pass 1 below), the deep-ref frontmatter, and the operator-inspection markdown views. Never hand-edit the JSON. Operator changes flow through frontmatter, the slug table, and the markdown views; the build regenerates the JSON.

## Distribution scope

**Scope** governs which references ship in which app. Each deep reference carries a `**Scope:**` line; each build profile declares `max_scope:` in `builds.yaml`. The build excludes references whose scope rank exceeds the profile's ceiling. `personal` is excluded from every profile by construction.

| Rank | Scope | What goes here |
|---|---|---|
| 0 | `open` | Public-domain, CC0, CC BY, CC BY-SA, MIT, Apache, government works |
| 1 | `open-nc` | CC BY-NC, CC BY-NC-SA: open with non-commercial restriction |
| 2 | `copyrighted` | Published all-rights-reserved material the operator has legitimate access to |
| 3 | `confidential` | Bounded-access engagement material (client docs, past AARs, incident data) |
| 4 | `personal` | Operator's own private notes, journals, drafts |

Full taxonomy and build-filter table: [`docs/reference/scope-taxonomy.md`](scope-taxonomy.md).

## Lens visibility

**Visibility** is the lens-side analogue of Scope: it governs which lenses ship in which app, and where a lens spec is allowed to live in the file tree. The five levels are the Scope taxonomy borrowed verbatim.

Each lens carries `visibility:` in its frontmatter. Each build profile declares `max_visibility:` in `builds.yaml`. The build excludes lenses whose visibility rank exceeds the profile's ceiling, and regenerates the app's `LENS-INDEX.md` from the filtered set so no broken links appear.

| Rank | Visibility | What goes here |
|---|---|---|
| 0 | `open` | Lenses safe for any audience, including corpus.commons-tracked apps |
| 1 | `open-nc` | Open with non-commercial redistribution intent |
| 2 | `copyrighted` | Lens drawing on all-rights-reserved third-party material |
| 3 | `confidential` | Lens carrying client-engagement detail or material under explicit confidentiality |
| 4 | `personal` | Operator's own private working notes; must not ship in any profile |

**Spec-location gate (hard).** Lenses with visibility `copyrighted`, `confidential`, or `personal` cannot live under `corpus.commons/`. The build fails with a "move to corpus.local/" message if they do. `open` and `open-nc` lenses are unrestricted in spec location.

Visibility is parallel to Scope, not unified with it. They are two separate filtering systems on two separate artefact types: Scope filters references; Visibility filters lenses. Neither extends to the other.

The `creating-lenses` skill at [`.claude/skills/creating-lenses/SKILL.md`](../../.claude/skills/creating-lenses/SKILL.md) captures the visibility declaration at authorship time and warns if the operator attempts to author a high-visibility lens into `corpus.commons/`. The build-time enforcement is documented in [`docs/architecture/copyright.md`](../architecture/copyright.md#lens-visibility).

## Mechanical-index pipeline artefacts

The Pass H ingestion-side artefacts that feed the build:

| Artefact | Path | Produced by | Consumed by |
|---|---|---|---|
| Discovery JSON | `_planning/discovery/{slug}.json` | one-time Sonnet discovery scan of the converted source | Pass H's preprocessor (Phase 1) |
| Extracted artefact | `_planning/extracted/{corpus}/{slug}.json` | the deterministic preprocessor at `scripts/mechanical_index/preprocess.py` | Pass H's concept-index build (Phase 3) |
| Reference staging | `_planning/staging/{corpus}/refs/{slug}.json` | per-source Sonnet refs pass over the deep-ref frontmatter | `build_reference_index.py` |
| Concept candidates | `_planning/staging/{corpus}/concepts/candidates.json` | `build_concept_index.py --emit-candidates` | the Sonnet cross-link pass |
| Concept decisions | `_planning/staging/{corpus}/concepts/decisions.json` | the Sonnet cross-link pass | `build_concept_index.py --assemble` |

The `extracted artefact` is the load-bearing one. It carries: back-matter `book_index_entries` (with page locators where present), `enumerated_methods` (author-curated method names with body lines where located), the source's `headings` tree, the `page_marker_map` when conversion preserved page anchors, and the dispatcher's `derived_tier` log. Cross-source aggregation across these artefacts feeds the corpus-wide concept candidate set the Sonnet cross-link pass adjudicates.

A `concept-axis entry` is one canonical record in `concept-index.json`: `{canonical, name, aliases[], sources[]}` where each source carries `{id, section?, md_line?, context?}`. The `section` is the deepest body heading whose title matched the canonical name or one of its aliases (or, for enumerated-method matches, the heading enclosing the body line). Sections from front-matter / back-matter (CONTENTS, INDEX, REFERENCES, single-letter dividers) are intentionally excluded.

## Skill boundary

Ingestion stops at reference. Distillation is a separate step.

| Skill | Owns | Passes |
|---|---|---|
| `ingesting-resources` | source → reference; also drives the mechanical-index pipeline at Pass H | A, B, C, D, E, F, plus H (preprocessor + Sonnet refs pass + Sonnet cross-link + index build) and I against the reference |
| `creating-tasks` | task-axis spec (Jobs-to-be-Done scoping) | n/a; a design dialogue, not a pass |
| `creating-applications` | task spec + corpus subset → compiled application | orchestrates G across the named source set |
| `creating-distillations` | reference × task [× lens] → distillation | G, plus H and I against the distillation |
| `creating-lenses` | lens spec (input to G's lens-applicability gate) | n/a; a design dialogue, not a pass |

For convenience, the ingestion skill's final step prompts the operator to chain distillations for any applicable task axes immediately. The verb boundary is separated; the operator workflow can still be a single call when the operator wants today's behaviour.

Re-ingestion (new edition, model advance, Pass I failure on the reference) flags existing distillations as stale; the operator decides which to re-distil rather than automatic re-projection.
