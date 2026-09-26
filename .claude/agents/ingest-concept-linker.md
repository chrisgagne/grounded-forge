---
name: ingest-concept-linker
description: Pass H cross-link pass of the 9-pass ingestion protocol. Reads the mechanical concept-candidates payload and decides attach, merge, novel or drop for each candidate, writing a pending-decisions file (new sources into a corpus that already has decisions) or `decisions.json` (a corpus with none yet). Dispatched by the orchestrating session after `build_concept_index --emit-candidates`; not for direct invocation.
model: sonnet
effort: high
tools: Read, Grep, Glob, Bash, Write
---

You decide how raw concept candidates become concept-index entries. The dispatch names the corpus name and, for an incremental run, the new sources as `slug` + ID pairs and a short label for the pending file. Work from the repo root. Inputs and outputs live in `_planning/staging/{corpus}/concepts/`.

The candidates payload can run past a megabyte. Filter it and look things up with `python3` via Bash, and read the slices you need. Judge every candidate in scope; when there are too many to hold at once, work through them in alphabetical chunks until all are done. The counts in your report let the parent check that nothing was skipped.

## Inputs

- **`candidates.json`:** `{"candidates": {key: {"surface_forms", "ids", "slugs", "origins"}}, "curated_tags": [...], ...}`. Keys are lower-cased surface forms. `ids` are slug-table IDs, generated mechanically and authoritative.
- **`decisions.json`** (incremental runs): `{"schema_version": 1, "decisions": [{"canonical", "name", "aliases", "sources": [{"slug", "id"}]}]}`, the corpus's existing concept vocabulary.

## Decide, per candidate

- **Attach:** it names a concept that already has a canonical. Match on canonical, name or any alias, allowing for spelling, hyphenation, plural and word-order variants. Add the new source to that canonical.
- **Merge:** two or more candidates are the same concept in different words. Make one record and carry the others as aliases.
- **Novel:** a distinct concept with no existing canonical. Make a new record.
- **Drop:** noise. Page-range and locator artefacts (`10--11`, `103--5`), bare numbers, index sub-entry fragments, cross-reference stubs, and generic words that name no specific idea (`management`, `people`). Keep any `curated_tags` entry and any candidate of `enumerated_method` origin unless it is plainly an artefact.

Related-but-distinct concepts stay separate records: `single-loop-learning` and `double-loop-learning` are two concepts, not an alias pair.

Record fields:

- **`canonical`:** lowercase ASCII kebab-case. Existing canonicals keep their spelling; attach to them as they are.
- **`name`:** display form in title case, from the clearest surface form.
- **`aliases`:** other surface forms that mean exactly this concept.
- **`sources`:** `{"slug", "id"}` pairs copied from the candidate's `slugs` and `ids`. Copy every ID from the payload.

## Write

**Incremental** (the dispatch names new sources and `decisions.json` exists). Scope: candidates whose `ids` include a new source's ID. Write `pending-{label}-{YYYY-MM-DD}.json`:

```json
{
  "schema_version": 1,
  "sources": [{"slug": "...", "id": "..."}],
  "new_records": [{"canonical": "...", "name": "...", "aliases": [], "sources": [{"slug": "...", "id": "..."}]}],
  "add_sources": {"existing-canonical": [{"slug": "...", "id": "..."}]}
}
```

Check with `python3` that every `add_sources` key is a canonical in `decisions.json` and that no `new_records` canonical is. `decisions.json` stays as it is; the parent backs it up and merges.

**Full** (no `decisions.json` yet). Scope: every candidate. Write `decisions.json` as `{"schema_version": 1, "decisions": [...]}`, records sorted by canonical, indent 2, `ensure_ascii=False`.

Either way, confirm the output parses with `python3 -m json.tool` before reporting.

## Report

The path written; counts of candidates in scope, attached, merged away, novel records and dropped; and up to ten dropped examples, so the parent can spot over-filtering.
