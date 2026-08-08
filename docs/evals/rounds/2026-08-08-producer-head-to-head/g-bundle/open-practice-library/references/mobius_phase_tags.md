---
type: Reference
title: Open Practice Library Mobius phase tags
description: Defines the Mobius phase taxonomy used to group practices in the Open Practice Library catalogue.
resource: https://openpracticelibrary.com/
tags:
  - mobius-loop
  - practices
  - taxonomy
sources:
  - id: open-practice-library-catalogue
    resource: https://openpracticelibrary.com/
    title: Open Practice Library — Concatenated Practice Catalogue
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---
# Mobius phase tags

The `mobiusTag` field places a practice in the Mobius Loop phase where it is most useful, while Foundation practices span the loop.

## Values

- `foundation` — team and cultural practices that hold across the loop.
- `discovery` — why-and-who framing: opportunity, problem, customer, and alignment practices.
- `options` — what-to-try framing: ideas, experiments, and prioritisation practices.
- `delivery` — build-and-measure framing: engineering, operations, and feedback practices.
- Unclassified — the catalogue's label for a practice whose contributor left `mobiusTag` blank; it is not a literal populated tag value.

## Catalogue snapshot

The ingested catalogue contains 266 practices: 111 Foundation, 86 Discovery, 32 Options, and 37 Delivery. Every practice in this snapshot has one of the four populated `mobiusTag` values, so none are Unclassified.
