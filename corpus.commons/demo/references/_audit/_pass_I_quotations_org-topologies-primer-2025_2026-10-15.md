# Pass I quotations audit: org-topologies-primer-2025 (2026-10-15)

**Mode:** quotations, plus a page-image check of every reading-order finding. Deep reference read in full (305 of 305 lines before edits; 309 after). Source: `corpus.commons/demo/sources/converted/org-topologies-primer-2025.md`, read in full (1,964 lines). Scope open-nc (CC BY-NC-SA 4.0), so `[V]` must match the converted source word for word.

**Page mapping.** The PDF has 29 pages. The converted text's `Page N` markers carry the printed page number, which is the PDF page minus one: PDF 1 is the cover, PDF 2 the "man walks into a bar" page, PDF 3 is printed "Page 2" (contents), and the closing co-creation note (PDF 29) has no marker. Confirmed on the images: PDF 5 reads "Page 4", PDF 15 reads "Page 14", PDF 23 reads "Page 22". The deep ref's `(p. N)` citations use printed page numbers.

**Work list:** `check-verbatim.py` report over the deep ref and the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), plus the human triage.

## Counts

- Actionable checker lines worked: 34 (2 glyph, 7 near, 20 interrupted, 1 missing, 4 no-quote).
- Quotation-corrected: 9 in the deep ref (15, 55, 67, 106, 130, 195, 198, 214, 250), 4 in distillations (software-business 38, 140, 42; stakeholder-engagement 8).
- Marker-corrected: 4 in the deep ref (241, 242, 243, 245: `[V]` → `[AP]`).
- Citation-corrected (page): deep 174 (five citations) and 272; decision-making 93, 100; retro 164.
- Other wording corrected: deep 243 entry label; light ref 76; software-business 122 (period moved outside the quotation).
- Stripped: 0.
- Left as is (layout interleaving, quote matches the page): 19 lines.

## Changes, deep reference

Line numbers are pre-edit (the blockquote at 214 grew by four lines, so later lines sit four lower now).

| Line | Finding | Change | Source |
|---|---|---|---|
| 15 | near: the four mapping elements joined with semicolons; the page sets them as a numbered list (PDF 5) | Each element quoted separately: "Two dimensions of org design", "Four organizational characteristics", "Sixteen archetypes within four groups" and "Three distinctive organizational topologies" [V] | src 291, 305–308 |
| 55 | near: `('CAPS-1', 'WHOLE-3',..)`; the page reads `("CAPS-1", "WHOLE-3",...)` | Ellipsis now three dots (nested quotes stay single, as house style) | src 377–378 |
| 67 | near: the source sets the period inside the quote, `“flow.”` | Quote now ends `'flow.'"` | src 607 |
| 106 | near: three bullet items (PDF 14) joined with semicolons | Each core feature quoted separately | src 882–887 |
| 130 | interrupted: in reading order on the page (PDF 17), but the four bullet items were joined with semicolons | Lead-in, each bullet and the closing sentence quoted separately, joined outside the quotation marks | src 1152–1170 |
| 174 | (not in report) the pet-supply example and its three answers are on printed p. 20 (PDF 21), cited as p. 21 | "follows on p. 21" → "p. 20"; four `(p. 21, "Strategic AI Adoption")` citations → p. 20 | src 1420–1470 |
| 195 | near: the framework list joined with semicolons; the page (PDF 23, read at 150 dpi) sets it as bullets, and "Spotify Model / McKinsey" and "Product Operating model" are two separate bullets, not one item | Rewritten: The Primer lists "More framework mappings examples": SAFe, Team Topologies, Large-Scale Scrum (LeSS), FAST Agile, Spotify Model / McKinsey, Product Operating model, Haier's RDHY, Bayer's DSO, "and many more" [V] | src 1711–1723 |
| 198 | missing: hyphens where the source has U+2011 non-breaking hyphens in `micro‑enterprises` and `customer‑focused` | Non-breaking hyphens restored; `[V]` kept. Finding stays `missing`: see Left as is | src 1644–1652, 1675–1681 |
| 214 | interrupted (blockquote): lead-in and list are one run on the page (PDF 5, right column), but the quote added semicolons and inline numbering | Blockquote reset as a list: the lead-in and each item quoted on its own line | src 291, 305–308 |
| 241, 242 | no-quote: "Listed among frameworks that can be mapped onto the OT grid" is a description of how the source uses LeSS / Team Topologies, not a quotation | `[V]` → `[AP]` (`[BT]` kept) | src 1711–1715 |
| 243 | no-quote: same pattern; the entry label also read "Spotify Model, McKinsey Product Operating model" | `[V]` → `[AP]`; label now "FAST Agile, Spotify Model / McKinsey, Product Operating model", as the page's bullets read | src 1717–1719 |
| 245 | no-quote: same pattern (Bayer's DSO) | `[V]` → `[AP]` | src 1722 |
| 250 | near: the source sets the period inside the quote, `‘solutions.’` | Quote now ends `'solutions.'"` | src 227–228 |
| 272 | (not in report) pet-supply worked example cited p. 21 | → p. 20 | src 1428–1433 |

## Changes, derived tier

- `distillations/software-business/…-software-business.md:38, :140`: the RDHY quote (glyph): non-breaking hyphens restored in `micro‑enterprises` and `customer‑focused`.
- `…-software-business.md:42`: question 1 quote ended "you are elevating." where the source has a comma and goes on. It now carries the full sentence, as deep 170 does.
- `…-software-business.md:122`: "Focus your AI investment in the area you are elevating." The period moved outside the quotation, since the source sentence goes on.
- `distillations/stakeholder-engagement/…-stakeholder-engagement.md:8`: "canned change 'solutions.'" (near, same as deep 250).
- `distillations/decision-making/…-decision-making.md:93, :100`: generic "adopt AI" and the pet-supply example cited p. 21; now p. 20.
- `distillations/retro/…-retro.md:164`: the evidence-continuity note cited the deep's CAPS-3 `[V]` passages at p. 21; now p. 20, matching deep 174.
- `references/org-topologies-primer-2025.md:76` (light ref): the framework list read "Spotify Model / McKinsey Product Operating model"; now "Spotify Model / McKinsey, Product Operating model", as the page's bullets read.
- Propagation grep of the light ref and all five distillations: "canned change", "WHOLE-3',", "Two dimensions of org design", "Broad scope", "Synchronous work", "Spotify", "McKinsey", "Product Operating", "Bayer", "micro-enterprises", "customer-focused", "'flow", "Focus your AI investment", "one WHOLE-1 unit", "consisting of", "pet-supply", "Listed among", "p. 21". No other copy of a corrected quotation found. The light ref's "Two dimensions of org design." (line 63) is an unquoted Key Statistics bullet, not a quotation.
- Claims the derived tier may carry: the framework list (deep 195, 243) now names "Spotify Model / McKinsey" and "Product Operating model" as two entries; the light ref is updated, and the distillations name only "Spotify model". The deep ref's content hash has changed, so the derived-provenance stamps on the light ref and distillations need re-stamping by the parent.

## Reading-order check

Every interrupted, near and missing line in the report, checked against the page image (80 dpi; PDF 23 also at 150 dpi). "Matches page" means the quoted text is one run in reading order on the page, a table cell, a column or a box.

| Line | Finding | PDF page | Matches page | Action |
|---|---|---|---|---|
| deep 15 | near | 5 | no (semicolons joined list items) | corrected |
| deep 55 | near | 6 | no (`,..` for `,...`) | corrected |
| deep 67 | near | 9 | no (period outside quote) | corrected |
| deep 73 | interrupted | 9 | yes: sentence and next paragraph; "Outcome Archetypes" is a figure label | left |
| deep 106 | near | 14 | no (semicolons joined bullets) | corrected |
| deep 112 (Delivery) | interrupted | 15 | yes: one table cell | left |
| deep 112 (Adaptive) | interrupted | 15 | yes: one table cell | left |
| deep 114 (Delivery) | interrupted | 15 | yes: one table cell | left |
| deep 115 (Resource) | interrupted | 15 | yes: one table cell | left |
| deep 115 (Delivery) | interrupted | 15 | yes: one table cell | left |
| deep 115 (Adaptive) | interrupted | 15 | yes: one table cell | left |
| deep 119 | interrupted | 16 | yes: two paragraphs in the left column; gap is diagram labels | left |
| deep 128 | interrupted | 17 | yes: two paragraphs in the left column; gap is diagram labels | left |
| deep 130 | interrupted | 17 | in order, but semicolons added between bullets | corrected |
| deep 142 | interrupted | 19 | yes: two paragraphs in the left column; gap is diagram labels | left |
| deep 170 | interrupted | 21 | yes: question and its bullet answer in the grey box | left |
| deep 171 | interrupted | 21 | yes: question and its bullet answer in the grey box | left |
| deep 193 | interrupted | 23 | yes: left column, paragraph, lead-in and bullets; gap is diagram labels | left |
| deep 195 | near | 23 | no (semicolons; two bullets merged into one item) | corrected |
| deep 197 | interrupted | 23 | yes: the "Mapping SAFe" column | left |
| deep 198 | missing | 23 | yes: the "Mapping RDHY" column (glyph aside) | glyph corrected, `[V]` kept |
| deep 214 | interrupted (blockquote) | 5 | in order, but semicolons and inline numbering added | corrected |
| deep 229 | interrupted (blockquote) | 23 | yes: lead-in and first two bullets | left |
| deep 250 | near | 4 | no (period outside quote) | corrected |
| deep 295 | interrupted | 5 | yes: left column, "What's new in the 2025 Edition"; gap is the right column | left |
| software-business 42 (q1) | interrupted | 21 | yes: grey box | left (sentence completed, see above) |
| software-business 42 (q2) | interrupted | 21 | yes: grey box | left |
| stakeholder-engagement 8 | near | 4 | no (period outside quote) | corrected |

**Tally:** 28 lines. Matches page 19 (18 interrupted, 1 missing); corrected 9 (7 near, 2 interrupted that added list punctuation); reclassified to `[AP]` 0. The triage's estimate of about 19 layout-caused findings holds.

The p. 21 archetype-group table quotes (deep 178–181, not in the report) were also checked against PDF 22: each quoted cell matches the page.

## Left as is (conversion noise)

- **Deep 73, 119, 128, 142** (interrupted): figure labels ("Outcome Archetypes"; the MADE-diagram labels "(1) MAP", "(4) ELEVATE", "Existing OD" and so on) sit between paragraphs that are contiguous on the page (PDF 9, 16, 17, 19).
- **Deep 112, 114, 115** (six interrupted): `pdftotext` read the p. 14 comparison table row by row across wrapped cells. Each quote is one cell on the page (PDF 15).
- **Deep 170, 171; software-business 42 (two)** (interrupted): the p. 20 question box sits beside the pet-supply column; the converter interleaved the two. Each question and its bullet answer are one run in the box (PDF 21).
- **Deep 193, 197, 229 (now 233)** (interrupted): p. 22 has three columns plus two maps; the converter interleaved the SAFe and RDHY columns, map labels and the left column. Each quote is one run in its column (PDF 23).
- **Deep 198** (missing): both RDHY paragraphs match the source word for word (src 1644–1652 and 1675–1681), but the converter put 764 characters of the SAFe column and the consequences list between them, more than the checker's 400-character gap window. On the page they are consecutive paragraphs in one column (PDF 23).
- **Deep 295 (now 299)** (interrupted): the right column's "Designing and Elevating" paragraph is interleaved into the left column's "What's new" section (PDF 5).

## Triage cross-check

- **deep 241, 242** (no-quote, `[V]` on a cited-work entry, "Listed among frameworks that can be mapped onto the OT grid"): fixed, `[V]` → `[AP]`, `[BT]` kept.
- **deep 243, 245** (no-quote, "Listed among framework examples"): fixed, `[V]` → `[AP]`, `[BT]` kept. On 243 the page also showed that the entry label merged two bullets; the label now follows the page.
- Reading-order findings: every interrupted, near and missing line is in the table above, with its PDF page and verdict.

## Checker counts

- Before: 30 apostrophe, 2 glyph, 37 initial, 7 near, 20 interrupted, 1 cross-source, 1 missing, 4 no-quote (34 failing).
- After: 32 apostrophe, 37 initial, 18 interrupted, 1 cross-source, 1 missing (19 failing, all layout interleaving listed under Left as is). Apostrophe rose by two because deep 67 and 250 now match at that non-failing level.

## Open

- Stamp left as is (quotations mode). No commit made, no build run.
- Several distillations cite the pet-supply example as "pp. 20–21" (aar 102, decision-making 141, software-business 44 and 136, stakeholder-engagement 119, retro 40). The example sits wholly on printed p. 20; the range includes the right page, so it was left.
- "Spotify Model / McKinsey" and "Product Operating model" are two bullets on the page; they may be one name that wrapped onto a second bullet. The deep and light refs now follow the page as printed.
- Out of scope for a quotations pass, for a full Pass I: deep line 9 says image classification was completed, while line 301 says it was deferred; and line 303 counts "27 numbered pages" where the PDF has 29 (printed "Page 2"–"Page 27" plus the unnumbered cover, intro and closing pages).
