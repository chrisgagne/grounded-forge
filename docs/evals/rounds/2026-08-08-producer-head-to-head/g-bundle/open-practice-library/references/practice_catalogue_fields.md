---
type: Reference
title: Open Practice Library practice catalogue fields
description: Defines the identity, classification, facilitation, and content fields preserved for Open Practice Library practices.
resource: https://openpracticelibrary.com/
tags:
  - catalogue
  - metadata
  - practices
sources:
  - id: open-practice-library-catalogue
    resource: https://openpracticelibrary.com/
    title: Open Practice Library — Concatenated Practice Catalogue
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---
# Practice catalogue fields

Each catalogue record preserves a practice's identity, source locator, classification metadata, facilitation guidance, and three main content fields. Optional metadata is omitted when a contributor did not supply it.

## Identity and provenance

- `title` — the practice name.
- `subtitle` — a short statement of the practice's purpose or outcome.
- Source filename — the originating Markdown filename in the Open Practice Library repository.
- `authors` — one or more contributor identifiers.

## Classification

- `mobiusTag` — the practice's position in the catalogue's [Mobius phase taxonomy](mobius_phase_tags.md).
- `tags` — topical labels. Values appearing in this catalogue snapshot are `culture`, `ideate`, `insight`, `insights`, `learn`, `measure`, `methods`, `validate`, and `value`; `insight` and `insights` are distinct source literals.
- `area` — a more specific catalogue area. Values appearing in this snapshot are `delivery-deliver`, `delivery-measure-and-learn`, `discovery-loop-outcomes`, `discovery-loop-why`, `foundation-culture-and-collaboration`, `foundation-technical`, and `options`.
- `difficulty` — the contributed difficulty label. Values appearing in this snapshot are `easy`, `moderate`, `hard`, and `null`.

## Facilitation

- `people` — a participant-count recommendation or range.
- `time` — an estimated duration or cadence.
- `participants` — the intended roles or audience.

The values of `people`, `time`, and `participants` are contributor-authored text rather than normalized units or identifiers.

## Content

- `whatIs` — what the practice is.
- `whyDo` — why a team would use it.
- `howTo` — how to run or apply it.

In the converted catalogue, these fields appear as `### What is it?`, `### Why do it?`, and `### How to do it?`.
