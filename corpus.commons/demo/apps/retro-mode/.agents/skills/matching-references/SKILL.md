---
name: matching-references
description: Identifies sources in the corpus that match a query topic, situation, or concept. Returns a list with one-line justifications for each candidate, with paths to the relevant distillations.
argument-hint: "[query string or topic]"
---

# Matching References

Identifies which sources in the corpus address a given query topic, situation, or concept. The skill returns a list of candidate sources with one-line justifications, naming the distillation(s) that project each source onto the task axes the app ships.

Distillations are the source-grounded product. The reference tier (light + deep) lives at corpus level as the audit-of-record but does not travel with the compiled app, so this skill returns distillation paths rather than reference paths.

**Path convention.** Every path in this skill is written from the app's perspective: `./distillations/{task}/{slug}-{task}.md`, `./concept-index.json`, `./slug-table.json`. The distillations directory and the runtime JSON indexes sit at the app root.

## Retrieval order

1. **Runtime listener tables in the distillation index for the task at hand** (`./distillations/{task}/{TASK}-DISTILLATION-INDEX.md`, per-phase listener sections; the `.md` view is the authoritative source for listener tables: the `task-index.json` runtime form carries only the phase-routing rows, not the listener tables). Check first when the query carries observable triggers: an utterance, a dynamic, a signal the practitioner noticed in the room ("the team keeps saying X", "we're stuck on Y", "someone keeps doing Z"). Skip this step on task axes whose spec carries no field-2a seed table.
2. **Phase-routing tables in the task-axis index** (`./distillations/{task}/task-index.json`, `rows` field). Use when the query is at the level of a phase or situation type ("we're in the contributing-factor-analysis phase", "this is a stakeholder-management question") rather than an observable trigger.
3. **Concept axis** (`./concept-index.json`) for named-concept lookups: aliases collapsed, per-source `{id, context}` pointers, cross-source coverage at a glance.
4. **Slug-table scan** (`./slug-table.json`) for named-source / author / title lookups when the user names a specific work or author. Resolve the slug-ID to distillation paths via `./distillations/{task}/{slug}-{task}.md` for each task the app ships.
5. **No-coverage is honest**: if none of the above surfaces a match, say so plainly rather than fabricate from training.

## Procedure

1. Read `./concept-index.json` and `./slug-table.json`.
2. Match the query against `concept-index.json` first (canonical names, aliases) for concept-shaped queries; against `slug-table.json`'s slugs for source-shaped queries (author/title strings often appear in the slug itself).
3. For each matched slug, find the distillation files that project it onto the task axes this app ships (look under `./distillations/`).
4. Return the matches as a list with paths to the corresponding distillation files, in relevance order.

## Inputs

- A query: topic, concept, or situation in plain language.

## Outputs

- A list of candidate sources. For each:
  - Author / topic slug
  - Path(s) to the distillation(s) for the task axes the app ships
  - One-line justification (why this source matches the query)

## When to use

- The user asks "is there a source in this corpus on X?"
- The user describes a situation and wants the assistant to identify which sources apply.

## When not to use

- The user has already named the source and the task. Read the distillation directly; do not run a search to find what is already named.
- The user has named a phase of a task. Use the distillation index's phase-routing tables for that task instead. The distillation index is the situation-to-resource router; this skill is the topic-to-resource router.
- The user describes an observable trigger from the room (an utterance, a dynamic, an energy signal: "the team keeps saying X", "we're stuck arguing about Y"). Use the distillation index's runtime listener tables for the task at hand. The listener table is the moment-to-framework router and ships in any application whose task spec carries a field-2a seed table.

## Related skills

- `answer-from-corpus`: the default source-grounded retrieval skill.
