---
name: matching-references
description: Identifies references in the corpus that match a query topic, situation, or concept. Returns a list with one-line justifications for each candidate.
argument-hint: "[query string or topic]"
---

# Matching References

Identifies which references in the corpus address a given query topic, situation, or concept. The skill returns a list of candidate references with one-line justifications.

**Path convention.** Every path in this skill is written from the source-repo perspective: `corpus.commons/demo/{file}`. When the skill runs inside a deployed application (any subdir of `corpus.commons/{corpus}/apps/`), the `corpus.commons/{corpus}/` prefix is stripped one-to-one: `corpus.commons/demo/reference-index.json` resolves as `./reference-index.json`, `corpus.commons/demo/distillations/{task}/task-index.json` as `./distillations/{task}/task-index.json`, and so on. Translate at read time; do not paginate or grep for files the literal path-string fails to find.

## Retrieval order

1. **Runtime listener tables in the distillation index for the task at hand** (`corpus.commons/demo/distillations/{task}/{TASK}-DISTILLATION-INDEX.md`, per-phase listener sections; the `.md` view is the authoritative source for listener tables: the `task-index.json` runtime form carries only the phase-routing rows, not the listener tables). Check first when the query carries observable triggers: an utterance, a dynamic, a signal the practitioner noticed in the room ("the team keeps saying X", "we're stuck on Y", "someone keeps doing Z"). Skip this step on task axes whose spec carries no field-2a seed table.
2. **Phase-routing tables in the task-axis index** (`corpus.commons/demo/distillations/{task}/task-index.json`, `rows` field). Use when the query is at the level of a phase or situation type ("we're in the contributing-factor-analysis phase", "this is a stakeholder-management question") rather than an observable trigger.
3. **Concept axis** (`corpus.commons/demo/concept-index.json`) for named-concept lookups: aliases collapsed, per-source `{id, section, md_line}` pointers, cross-source coverage at a glance.
4. **Corpus catalogue** (`corpus.commons/demo/reference-index.json`) for named-reference / author / title / topic lookups.
5. **Semantic search** as a safety net for genuinely novel queries the curated indexes did not pre-think-of. Returns pointers (filenames, authors, similarity scores), never document bodies; bodies stay in the file system. See [`docs/architecture/two-layer-indexes.md`](../../../docs/architecture/two-layer-indexes.md).
6. **Grep** as a fallback when semantic search is unavailable.
7. **No-coverage is honest**: if none of the above surfaces a match, say so plainly rather than fabricate from training.

## Procedure

1. Read [`corpus.commons/demo/reference-index.json`](../../../corpus.commons/demo/reference-index.json) and [`corpus.commons/demo/concept-index.json`](../../../corpus.commons/demo/concept-index.json).
2. Match the query against `concept-index.json` first (canonical names, aliases) for concept-shaped queries; against `reference-index.json` `author`, `title`, `primary_topic`, `concept_tags` for source-shaped queries. Resolve slug-IDs to file paths via [`corpus.commons/demo/references/slug-table.json`](../../../corpus.commons/demo/references/slug-table.json).
3. Return the matches as a list with paths to the corresponding reference files, in relevance order.

## Inputs

- A query: topic, concept, or situation in plain language.

## Outputs

- A list of candidate references. For each:
  - Author and topic slug
  - Path to the deep reference
  - Path to the light reference
  - One-line justification (why this reference matches the query)

## When to use

- The user asks "is there a reference in this library on X?"
- The user describes a situation and wants the assistant to identify which references in the corpus apply.
- Pre-ingestion: before running `ingesting-resources`, check whether the source is already in the corpus. (`ingesting-resources`'s setup gates reference this skill explicitly as the first check.)

## When not to use

- The user has already named the reference. Read it directly; do not run a search to find what is already named.
- The user has named a phase of a task. Use the distillation index's phase-routing tables for that task instead. The distillation index is the situation-to-resource router; this skill is the topic-to-resource router.
- The user describes an observable trigger from the room (an utterance, a dynamic, an energy signal: "the team keeps saying X", "we're stuck arguing about Y"). Use the distillation index's runtime listener tables for the task at hand. The listener table is the moment-to-framework router and ships in any application whose task spec carries a field-2a seed table.

## Related skills

- `ingesting-resources`, add a new source to the corpus.
- `creating-distillations`, project one existing source onto one existing task axis (per-distillation).
- `creating-applications`, assemble a new application across multiple distillations.
