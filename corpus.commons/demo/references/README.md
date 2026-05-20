# corpus.commons/demo/references/

Light and deep references. The reference axis of the matrix. One source per file pair: `{author}-{topic}.md` (light) and `{author}-{topic}-deep.md` (deep).

## What goes here

- **Deep reference** (`{author}-{topic}-deep.md`): full ingestion output. Verbatim citations with section or page anchors. Inline evidence-classification markers (`[V]`, `[AP]`, `[AR]`, `[AE]`, `[BT]`). Author thesis, walkthrough by part or chapter, key statistics with provenance, connections the author makes, positions the author frames against, citation and integrity notes. The opening metadata block carries `**Source:**` (citation + licence string), `**Scope:**` (one of `open`, `open-nc`, `copyrighted`, `confidential`, `personal`; the build's `max_scope` filter reads this), `**Structure:**`, and `**Citation style:**`. ~500-2500 lines typical.
- **Light reference** (`{author}-{topic}.md`): condensed orientation document derived from the verified deep. Flatter section structure (depth-2 headings only). Inherits citation discipline from the deep. ~100-300 lines typical.
- **`slug-table.json`**: append-only mapping from each reference's slug to a 3-character base-36 ID. The join key beneath the runtime indexes at the corpus root (`reference-index.json`, `concept-index.json`).

## What does not go here

- Task-application guidance. Diagnostic questions, anti-patterns, worked-example projections, integration tables. Those live in `corpus.commons/demo/distillations/{task}/`. The reference tier is faithful summarisation of the source; the projection tier is library-level synthesis.
- Source PDFs or EPUBs. Raw sources go in `docs/sources/` (gitignored).

## How files are produced

Every reference here is produced by the 9-pass ingestion protocol documented at the substrate `docs/architecture/ingestion-protocol.md`. The skill that runs the protocol is the substrate `ingesting-resources` skill.

A deep reference does not ship until Pass I (source-only audit) passes. A light reference is derived from the verified deep, not from the source.

## File naming

```
{author-slug}-{topic-slug}.md         Light reference
{author-slug}-{topic-slug}-deep.md    Deep reference
```

The slug is lowercase, hyphen-separated. Author slug is the primary author's surname or recognisable identifier; topic slug is a short term capturing the source's central theme. The demo's `openstax-organizational-behavior.md` and `openstax-organizational-behavior-deep.md` are a worked pair.

The demo corpus ships 25 reference pairs (25 deep + 25 light) across the OpenStax books and the supplementary sources. Per-source Pass A ledgers, Pass H verification logs, and Pass I source-only audits live under [`_audit/`](_audit/) as the integrity record; they are excluded from the compiled distribution.
