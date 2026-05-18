---
title: "Systems Thinking Foundations (Methods Briefs Series 1)"
authors: ["Allie Farrell", "Min Hu", "William Liem", "Ellis Ballard", "Mikayla Branz", "Lucy Chin", "Ebuwa I. Evbuoma"]
publisher: "Social System Design Lab, Brown School at Washington University in St. Louis"
publication_date: 2021
url: "https://openscholarship.wustl.edu/ssdl/"
dois:
  - "10.7936/c89k-d163"  # 1.07 System Archetypes (canonical DOI verified in Pass A)
  # Per-brief DOIs for 1.02, 1.03, 1.05, 1.06 carry the same 10.7936/... pattern;
  # each brief's exact DOI is recorded in its individual citation block inside the converted markdown.
scope: open
licence: "CC BY-SA 4.0"
licence_url: "https://creativecommons.org/licenses/by-sa/4.0/"
ingested: 2026-05-13
original_format: pdf_bundle
checksum_sha256: be1b1914cff29ca9590bbadb6e3b714add55302bd332197b0fbcc95829d7fe19
checksums_individual:
  Accumulations.pdf: 6d25e29616299354fc37ce4fe481d4944b92f76d6a92b15f05fe86186624f22c
  Characteristics of Complex Problems.pdf: 881271744ad892298ae6f0ce3a8d4929295bb0a9e05a8d9f087d1b1510c817ee
  Mental Models.pdf: 3b6a6fa10daa0e49e8965b369aa60753721c1c7cf197e3734e265c0422fb9684
  System Archetypes.pdf: acc98acbe1215fa6e7d906c959d01a0b077aa538dead92eeecb1f83272bf00b5
  Understanding Systems from a Feedback Perspective.pdf: d318edb9676e1477a3489a174c0ee5ceb872311057b4e6a03cfd52f94b01bafd
---

# Source: Systems Thinking Foundations (SSDL Methods Briefs Series 1)

A collection-as-source ingest of 5 of 7 *Methods Briefs Series 1: Systems Thinking Foundations* from the Wash-U Brown School Social System Design Lab. Published 2021 under CC BY-SA 4.0. The 5 ingested briefs are short focused notes (4–7 pages each) on field-agnostic systems-thinking concepts originally codified in the Forrester/Senge/Meadows tradition:

| Series # | Brief | Pages |
|---|---|---:|
| 1.02 | Characteristics of Complex Problems | 4 |
| 1.03 | Mental Models | 5 |
| 1.05 | Understanding Systems from a Feedback Perspective | 6 |
| 1.06 | Accumulations | 6 |
| 1.07 | System Archetypes | 7 |

Series 1 was published by SSDL between 2021 and 2024 at https://openscholarship.wustl.edu/ssdl/. The series description in the footer of each brief states that the curriculum *"focuses on introducing core concepts of systems thinking and system dynamics as they relate to issues of education equity. This series draws from community-based modeling work with educators and students over the last ten years."* The education-equity context is the *applied domain* for the worked examples; the *conceptual frame* is the field-agnostic systems-thinking tradition the briefs translate (Senge, Meadows, Sterman, Kim, Hovmand, Wolstenholme).

## Briefs deliberately excluded from this ingest

Two briefs from Series 1 are **not** in this bundle:

- **1.01 *Systems Thinking Iceberg: Diving Beneath the Surface in Education Systems***. Sonnet-probe verdict: *"The entire frame is built around education and the systems-thinking concepts are subordinate."* The concept (events / patterns / structures / mental models layered iceberg) gets its operational meaning *only* through a one-page school-discipline walkthrough; the iceberg-layer definitions are stated abstractly and never expanded outside the education frame. Heavy vocabulary leakage into conceptual sections.
- **1.04 *Framing Dynamic Problems***. Sonnet-probe verdict: *"the case study is integrated and load-bearing, not adjacent."* The static-to-dynamic reframe and behavior-over-time graph technique are demonstrated *only* through a 2-page Nevada community education-equity board worked example; a software-engineering practitioner would have to work through the case to extract the technique.

The 5 briefs in this bundle (1.02, 1.03, 1.05, 1.06, 1.07) have field-agnostic concepts with education examples as **decorative illustrations**: the concept stands without the example; the example is replaceable. A software-engineering practitioner reads these as systems-thinking content with minimal translation friction (the sonnet probes verified this per brief).

## Licence note — CC BY-SA 4.0 with ShareAlike propagation

Each brief carries an explicit licence statement on its last page: *"[Brief title] © 2021 by Social System Design Lab is licensed under CC BY-SA 4.0"*. SA propagation applies: derivatives produced from this source (the deep reference and distillations) inherit SA-compatible licensing. The corpus's existing CC BY-SA 4.0 sources (Jones ESEUR, Schwaber & Sutherland Scrum Guide) carry the same propagation. Build profiles with `max_scope: open` ship this source; profiles with stricter ceilings would exclude it.

## Pass-G discipline applied at ingest

The 5 briefs use education-equity worked examples (achievement-gap dynamics, exclusionary discipline, teacher burnout, parent-teacher trust loops). The ingestion protocol's Pass-G projection step translated these to task-vocabulary worked examples in the distillation files; the education examples are preserved in the **deep reference** (where source-claim provenance lives) but do not appear as worked-examples in the **distillations** (where the task's working vocabulary lives). This applies the projection-protocol's *mismatched task vocabulary* failure-mode discipline.

## Role in corpus

**Closes the systems-thinking gap.** Systems-thinking is one of the demo corpus's load-bearing methodology areas. Brief 1.07 *System Archetypes* is the direct Senge/Meadows-tradition substitute under a clean open licence, covering Fixes that Fail, Shifting the Burden, Tragedy of the Commons, Limits to Growth as field-agnostic archetypes. The other four briefs carry the foundational concepts archetypes assumes (mental models, feedback loops, accumulations, characteristics of complex problems).

Pairs naturally with **Barbrook-Johnson & Penn *Systems Mapping*** (Wave 2): Barbrook-Johnson is the *methods-level* grounding (CLDs, System Dynamics, Theory of Change as tools); SSDL is the *concepts-level* grounding (archetypes, feedback, mental models as ideas).

## Files in this ingest

- `Accumulations.pdf` (1.06)
- `Characteristics of Complex Problems.pdf` (1.02)
- `Mental Models.pdf` (1.03)
- `System Archetypes.pdf` (1.07): headline pick
- `Understanding Systems from a Feedback Perspective.pdf` (1.05)

All 5 PDFs are preserved in this directory; the converted markdown concatenates them in series order (1.02 → 1.03 → 1.05 → 1.06 → 1.07).

## Recovery note

This ingest was originally dispatched as a single sub-agent on 2026-05-13. The agent completed Passes A–G + Pass I cleanly and produced the deep reference, light reference, two distillations, audit log, and converted markdown, then stalled mid-Pass-H during canonical-index edits (REFERENCE-INDEX additions completed; distillation-index additions not yet started; sidecar not yet written; PDFs not yet moved from ingest/). The remaining steps were completed manually in-line: sidecar written, PDFs moved, distillation-index headers updated, build verified.
