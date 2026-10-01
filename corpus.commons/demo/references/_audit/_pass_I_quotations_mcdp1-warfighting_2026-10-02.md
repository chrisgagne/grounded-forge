# Pass I (quotations mode): mcdp1-warfighting, 2026-10-02

**Deep reference:** `corpus.commons/demo/references/mcdp1-warfighting-deep.md` (244 lines, read in full)
**Source:** `corpus.commons/demo/sources/converted/mcdp1-warfighting.md` (3,040 lines; pdftotext of the official PDF, replacing the earlier plain-text OCR the deep reference was written from)
**Trigger:** source re-conversion. Scope is the `check-verbatim.py` work list only; the `Pass I applied` stamp and the coverage note are left as they were.

## Counts

- Failing checker lines worked: 31 (7 near, 15 interrupted, 9 missing); 2 `initial` lines need no fix.
- Quotations corrected: 4 (lines 15, 35, 149, 167).
- Quotations left as they stand, with the book's wording kept over a garbled conversion: 13.
- `interrupted` / `missing` lines whose only gap is a running header or page number: 14 (no fix).
- Claims stripped or marker-corrected: 0.
- Checker after fixes: 2 initial, 5 near, 15 interrupted, 7 missing, every one of them conversion noise listed below.

## Corrections

| Line | Old | New | Reason |
|---|---|---|---|
| 15 | John Boyd, who *"pioneered"* the OODA loop *"in his lecture, 'The Patterns of Conflict'"* [V] | John Boyd, who *"pioneered"* the OODA loop in his lecture *"The Patterns of Conflict"* [V] | The source reads `"The Patterns of Conflict."` with the period inside the closing mark; the fragment closed the inner quotation before the period. Quoting the title alone matches exactly. |
| 35 | ". . . the very nature of war makes certainty impossible" | ". . . The very nature of war makes certainty impossible" | Case changed after the ellipsis; the source starts a sentence ("The very nature"). |
| 149 | *"a commander's statement of intent should be brief and compelling — the more concise, the better . . . [Subordinates] should understand the intent of the commander at least two levels up."* [V] | a *"commander's statement of intent should be brief and compelling — the more concise, the better."* [V] Subordinates *"should understand the intent of the commander at least two levels up."* [V] | Two passages about 25 lines apart joined with an ellipsis and a bracketed substitution for "they". Split into two exact quotations. The leading "a" moved outside the quote because the conversion interleaves a column fragment ("in order to") between "a" and "commander's". |
| 167 | *"Speed over time is tempo — the consistent ability to operate quickly . . . Tempo is itself a weapon — often the most important."* [V] (Ch 2, "Speed and focus"; "Styles of warfare") | *"Speed over time is tempo — the consistent ability to operate quickly."* [V] (Ch 2, "Speed and focus") *"Tempo is itself a weapon — often the most important."* [V] (Ch 2, "Styles of warfare") | The ellipsis joined two sentences in reverse source order ("Tempo is itself a weapon" is in "Styles of warfare", which comes before "Speed and focus"). Split into two quotations, each with its own section. |

## Left as they stand: the conversion is garbled, the quote keeps the book's wording

| Line | Converted text | Quote keeps |
|---|---|---|
| 41 (Mission tactics) | `accomplished.8 We` (footnote 8 glued on) | `accomplished. We` |
| 41, 135 (Philosophy of command) | `the uncertainly, disorder, and fluidity` | `uncertainty` |
| 93 (Speed and focus) | `operate quickly.'8 Speed` (footnote 18 glued on) | `quickly. Speed` |
| 97 (Centers of gravity) | `Which, f eliminated,` | `if eliminated` |
| 111 (Professionalism) | `part of learning.6 We` (footnote 6 glued on) | `learning. We` |
| 113 (Professionalism) | `the behavior of"yes-men"-—-will` | `the behavior of 'yes-men' — will` |
| 115 (Training) | `admit mistakes ajid discuss them` | `and` |
| 129 (Maneuver warfare) | `everincreasing` (line-break hyphen lost) | `ever-increasing` |
| 149 (Commander's intent) | `behind it.° The intent` (footnote mark glued on) | `behind it. The intent` |
| 155 (Combined arms) | `nowin` | `no-win` |
| 169 (Notes 8 of Ch 4) | `missiontype` | `mission-type` |
| 216 (FM 100-5 note) | `selfreliant` | `self-reliant` |

## No fix: the gap is a running header or page number

Lines 41 (mission tactics, "87 Warfighting MCDP I"), 43 ("102 MCDP 1 Notes"), 57 ("a continuous source of friction": "8 MCDP 1 The Nature of War"), 63 ("12 MCDP 1 The Nature of War"), 79 ("24 MCDP 1 The Theory of War"), 87 ("36 MCDP 1 The Theory of War" between "an" and "inward"; the line-split "vol-ume" is rejoined by the checker), 109 ("55 Warfighting MCDP"), 145 ("85 Warfighting MCDP"), 147 and 191 ("87 Warfighting MCDP I"), 149 ("90 MCDP 1 The Conduct of War"), 153 twice ("92 MCDP 1 The Conduct of War", "93 Warfighting MCD?"), 168 (an ellipsis gap plus "102 MCDP 1 Notes"). The checker reports some of these as `missing` instead of `interrupted` where the header falls inside a quotation that also carries an ellipsis, or inside a short fragment; each passage was read in the source and matches word for word apart from the header.

## Open

- **Source-integrity notes (deep ref lines 224-226) describe the old conversion:** "the 4,478-line converted source" (now 3,040 lines), the SHA256 of the earlier file, and OCR artefacts (*Elect*, *EOREWORD*, *Eorce*) that belong to the old OCR. Left unedited as the dispatch asked; the parent should refresh them against the new sidecar.
- **Derived tier:** the four corrected quotations may be carried by the light reference or a distillation (the Tempo line and the commander's-intent lines are the most likely). The parent re-derives; nothing here is stamped.
