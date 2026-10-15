# Pass I source audit: uk-aqua-book-2025

- **Deep reference:** `corpus.commons/chrisgagne-agent-built-software/references/uk-aqua-book-2025-deep.md` (544 lines; read in full, lines 1–544).
- **Source tape:** `corpus.commons/chrisgagne-agent-built-software/sources/converted/uk-aqua-book-2025.md` (1,436 lines; read in full, lines 1–1436).
- **Also checked:** the HTML at `sources/ingest/uk-aqua-book-2025.html`, the source card `sources/original/uk-aqua-book-2025.source.md`, the acquisition record `_planning/staging/chrisgagne-agent-built-software/acquisition/uk-aqua-book-2025.json`, and the three SVGs in `sources/converted/uk-aqua-book-2025-images/` (text layer and element counts; the risk-matrix SVG rasterised once with Quick Look). The original is HTML, so no pdftoppm page renders were used.
- **Auditor:** Claude Opus 5.5, same-family leg, fresh context. A blind cross-family (codex) leg runs separately on a frozen copy; this log was written without seeing it.
- **Date:** 2026-10-15. Mode: fix in place. The deep reference is not stamped here; the driver stamps once every leg is done.

## Counts

| Item | Count |
|---|---|
| Claims audited | 362 marker-bearing claims (130 [V], 166 [AP], 4 [AR], 11 [AE], 51 [BT]) plus about 45 unmarked claims in the Source, Structure, figure, Key statistics and integrity-note blocks |
| Source-anchored as written | all but the 8 below |
| Stripped | 1 |
| Corrected (factual or attribution) | 6 |
| Marker-corrected | 1 |
| Quotation-corrected | 0 (`check-verbatim.py`: no findings before or after) |

TOC-vs-anchors: every heading in the tape (Acknowledgements, Ch 1–10 with all numbered subsections and boxes, "Improving the book") appears in the deep reference's anchor list and body citations. Pass.

## Changes

1. **Line 5, Source line. Stripped** "with the GOV.UK record updated 2025-11-24". No artefact carries that date: the source card says "first published 2025-07-30" and the acquisition record's `public_updated_at` is 2025-07-30. Also reworded "lists the publishing organisations as the GOV.UK page names them" to credit the source record, which is where the list comes from (its `publisher` field).
2. **Line 33, thesis. Corrected attribution.** "in the defined senses of the UK Government Functional Standards" made the Standards the source of the definitions. The tape defines the terms itself and says only "This is consistent with the UK Government Functional Standards" (tape l.127). Now: "in senses it defines itself and calls consistent with".
3. **Line 39. Marker corrected [BT] → [AP].** That the original book was compiled by the Quality Assurance Working Group set up after Macpherson's review is the book's own account of its history ("Acknowledgements"), not a claim it borrows from another work.
4. **Line 211. Corrected.** "the matrix cells are embedded raster images". The SVG's single embedded raster (`#img0`, 323×172 PNG) is blank white; the cells are vector shapes with five red fills (#A50021, #FF5050, #FF7C80, #FF9999, #FFCCCC) and no text. Now: unlabelled cells in shades of red; the SVG adds no cell-level wording.
5. **Line 453, 9.6 Multi-use models. Corrected modal force.** The deep said "the analyst should very clearly communicate"; the tape says "it is important that the analyst very clearly communicates" (l.1322). In this book "should" is a defined comply-or-explain term, and line 70 promises the reference keeps modal force, so the paraphrase now keeps the source's wording.
6. **Line 505, Connections. Corrected attribution.** "UK Government Functional Standards: the source of the shall/should/may conventions" is now "the book says its shall/should/may conventions are consistent with them" (same reason as change 2).
7. **Line 534, conversion path. Corrected hashes.** The stated tape sha256 (`f5734e02…`) and HTML sha256 (`256b9242…`) matched neither the files nor the manifest. Actual and manifest values agree: tape `c8ff4140884f8d7cdb3d4e130f2e11197235dfde8dcce3c314e85ae9fc1ada1d`, HTML `7182986afa6388ec31d3195ba07d01c214e16674f81c29a760c3b94f882009e0`. The stated values probably predate the safelinks rewrite, but nothing on disk confirms that.
8. **Line 538, Figures note. Corrected.** "its cells are embedded raster images, not inspected here" is now "its cells are unlabelled shapes filled in shades of red, and its one embedded raster is a blank white image" (same evidence as change 4).

## Checked and left as written

- The source-native oddities in the integrity notes ("problem-solving, -making", "follow the conduct the", "quantative", "should to fully", "any that websites" ×2, "its affect on", "valuation verification", "meets it specified", "could have a significant reputational", "Department of Energy Strategy and Net Zero") are all present in the HTML, so they are not conversion faults.
- 16 `<tr>` elements in the HTML (10 + 4 data rows, 2 header rows); all four `<img>` tags have `alt=""`.
- The SVG claims for the life-cycle diagram (stages at top, right, bottom and left; "Start" and "Sign-off" upper left; centre iteration note; proportionality note at upper right) and for Figure 3-1 (axis and row-end labels) match the SVG text layer and coordinates.
- *Positions the author explicitly frames against.* Each of the five entries rests on an explicit negation in the source ("is more than", "This does not mean", "it is not necessary", "must not be viewed in isolation", "is not a linear process"). These are the source's own framing, not invented oppositions.
- The Connections list's "GOV.UK Service Manual" label is read from the link targets in 9.7.2 (`gov.uk/service-manual/...`). Left as written.

## Open

- **Line 542, link hygiene.** Which two links were safelinks (9.5 and 10.1.2) can't be checked from the tape or HTML, since both were rewritten. It is consistent with the AI Playbook `<a rel="external">` in 9.5 and the DESNZ `<a rel="external">` in 10.1.2, both gov.uk URLs marked external. The claim rests on the operator's record.
- **Line 543** still reads "Audit pending. This reference has not been through Pass I." Left untouched as instructed; the driver updates it at stamping.
- The note at line 540 lists where "must" appears. The list leaves out 3.2's prose ("appropriate mitigations must be considered") but doesn't claim to be complete, so it was left as written.

## Derived tier

- No light reference (`references/uk-aqua-book-2025.md`) and no `uk-aqua-book-2025-*` distillation exists, so there is nothing to re-derive for this slug.
- Four other sources' distillations in `distillations/warranting-agent-built-software/` cite `uk-aqua-book-2025` in cross-reference rows: microsoft-code-with-engineering-playbook, egashira-testsuitebench-2026, uk-duck-book-qa-of-code and openssf-finding-fixing-vulnerabilities-ai. They cite assurer–analyst independence, proportionality, Duck Book linkage and black-box automatic tests. None of the eight changes above touches those claims. If a later re-derivation copies the Functional Standards attribution (changes 2 and 6) or the 9.6 modal (change 5), use the corrected wording.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `ee3d8943c9a2601bea99c4ab44cc3306cde57a719fa29733c87135907f77716e`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `ea27733557ab02703f3a9e3747d8f750308f2a32501735ad99f6ea78c4b23bd2`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_uk-aqua-book-2025_crossfamily_blind.md`, `_ingest_pass_I_uk-aqua-book-2025_crossfamily_sort.md`, `_ingest_pass_I_uk-aqua-book-2025_crossfamily_prompts.md`.

**Sort result:** The sort confirmed 12 original defects (9 fixed by the fixer, 1 fixed incompletely, 2 missed by the fixer), found 0 over-flagged by the fixer and 0 by the blind auditor, 0 disputed, and 1 new defect introduced by the fixer (capture fixer=10 blind=6 both=4), with a gate verdict of pass once its 4 remaining edits are applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 10, the blind audit 6, both 4. The Chapman estimate is 14.4 in all, about 2.4 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Of the 4 remaining edits, 2 were applied as written (line 459 thresholds-only director agreement, adding only 'the'; line 542 location parenthetical stripped) and 2 with changed wording (the uncertainty Connections entry split into two bullets keeping the stance labels, Toolkit 'approving' with an added Ch 10 '10.1.1' anchor and NAO 'neutral'; the risk-matrix raster described as a partly transparent white glow shaped like the word 'Risk' drawn behind the 'Risk' label, confirmed by extracting the PNG), and none were declined.

**Gate:** pass. Deep reference sha256 `04a8c90ff68023de5d50d08e86c18643abdeed56bc9d6adf2404bcfa9c181a0f`, stamp included.
