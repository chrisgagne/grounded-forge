## 1. What I read

Read in full: `sort-brief.md`, `blind-brief.md`, `pass-i-spec.md`, all three calibration fixtures, both audit reports, `source-card.md`, and all 459 lines of `post-audit-deep.md`.

Compared every change between `frozen-deep.md` and `post-audit-deep.md`. Verified the post-audit SHA-256 against its sidecar.

Read the prescribed tape ranges in full: 1050–1110, 1160–1560, 2395–2550, 3660–3870, 4590–4840 and 8150–9300; extended the FCM range through 4905 and checked additional passages relevant to the findings. Independently inspected original PDF pages 25, 26, 52, 98, 100 and 186. PDF page numbers below count from the PDF’s first page.

Re-ran `check-verbatim.py` against the supplied post-audit reference and tape. Its three slash-related `near` results and one running-header interruption are conversion/checker artefacts, not quotation defects.

This is a sort of the supplied scoped re-audits, including the historical corrections recorded in the fixer’s log. It is not a fresh audit of the entire book. No files were modified.

## 2. Sorted ledger

| ID | Finding and auditor | Classification | Independent determination and evidence |
|---|---|---|---|
| H1 | Historical fixer: restore capitalisation and exclamation mark in “You basically cannot avoid having it do this to you!” | **Confirmed and fixed** | Post-audit line **81** matches tape **1587–1588**. |
| H2 | Historical fixer: Fig 1.2 placements over-extended the converted text | **Over-flagged — fixer** | The original PDF, **p. 25**, supports the earlier description: Rich Pictures, PSM and FCM emphasise participation; BBN and SD are toward the formal end; CLD is near the middle. Fragmented conversion alone does not invalidate a claim supported by the original figure. The replacement at post-audit line **48** also introduces the unsupported description “prose-captured placements”; tape **949–1050** supplies figure labels and general explanatory prose, not those placements in prose. See remaining edit 1. |
| F1 | Scoped fixer: remove “about 1,300 words” from the coverage statement | **Confirmed and fixed** | Removed at post-audit line **9**. The five restored table ranges alone contain approximately 1,800 whitespace-delimited tokens, including headings and page furniture; the figure-label ranges add further text. Tape **1199–1538, 3696–3845, 8198–8865, 8979–9073, 9140–9281** supports removing the unsubstantiated estimate. |
| F2 | Scoped fixer: “The descriptions place several of these near the book’s methods” | **Confirmed and fixed** | Post-audit line **75** now accurately identifies description and further-reading cells. The cited cells describe methods, their origins and reading suggestions; they do not collectively make the claimed proximity judgement. Tape **1272–1318, 1327–1345, 1386–1406, 1496–1516**. |
| F3 | Scoped fixer: simplify “the bullet glyph-free cells are joined across line breaks” | **Editorial correction; no substantive defect asserted** | Post-audit line **330** now says “cells are joined across line breaks”. This accurately describes the presentation of tape **8198–8865**. The fixer explicitly called this editorial and said the claim was unchanged; it should not inflate the defect count. |
| F4 | Scoped fixer: replace the obsolete assertion that all figures are caption-only | **Confirmed, fix incomplete** | Post-audit line **457** correctly recognises restored content from Figs 1.3, 3.2, 6.1 and 6.3. Its final sentence still says every other figure is caption-only, although lines **47–48** describe placements in Figs 1.1 and 1.2. Those are figure-content claims. Tape **949–1045** and original PDF **p. 25** establish the distinction. See remaining edit 2. |
| B1/F5 | Both auditors: light reference’s “embed any map in a Rich Picture” | **Confirmed, fix incomplete — derived tier** | The defect remains in the light reference, line **57**. Post-audit line **378** is already correct: Table 11.3 proposes embedding CLD, FCM, PSM and ToC maps, sketching SD outputs, and supplies no BBN entry. Tape **9216–9234**; original PDF **p. 186**. Both suggested replacements remove the overstatement; the blind auditor’s replacement also preserves the SD proposal. No deep-reference edit is needed. |
| B2 | Blind auditor: categorical forecasting prohibition in the software-business distillation | **Missed by the fix-in-place audit — derived tier** | The final sentence at software-business line **73** remains defective. Post-audit lines **358–366** correctly preserve a table of *most appropriate* methods and its simplification warning. Tape **8970–8973, 8994–8998, 9050–9056, 9078–9081** does not support saying no method forecasts such market or organisation-design questions. The fixer checked the table quotations but overlooked this additional sentence. |
| F6 | Fixer: light reference’s “causal/cognitive mapping, which they would most likely have added next” | **Disputed** | Post-audit line **59** accurately reproduces tape **1226–1240**. **Defect reading:** “next” adds a priority or sequence absent from the source’s counterfactual expansion of scope. **Clean reading:** “would most likely have added” reasonably compresses “most likely would have included had we expanded our focus”; it does not necessarily predict future publication plans. The fixer’s proposed wording is more precise, but this is not a clear source-integrity failure. |

The audits’ clean findings concerning restored table cells, Fig 3.2’s categories, FCM weights and iterations, and the three added statistics rows hold against the checked tape passages and relevant original figures. The authors’ Table 11.2 simplification warning remains intact in the deep reference.

The historical full-document reading and OCR assertions are **unverified process claims**, not established defects. Neither agreement between auditors nor agreement with the source card independently verifies that those activities occurred.

**Defects introduced by fixes:** H2’s replacement introduces unsupported provenance wording at line 48. F4 repairs the main obsolete assertion but retains an inaccurate blanket exception. No other defect was found in the four scoped edits.

## 3. Remaining edits to `post-audit-deep.md`

1. **Line 48 — replace the complete bullet.**

   **Current:**

   > - **Fig 1.2** — *emphasis on participation* × *intuitive-easy-to-start ↔ formal-harder-to-start*. Positions the methods on those two spectra (the converted-markdown figure layout was fragmented by OCR; the prose-captured placements include PSM and FCM as participation-emphasising, BBN as neutral on participation, and System Dynamics as on the formal end of the second axis).

   **Replacement:**

   > - **Fig 1.2** — *emphasis on participation* × *intuitive-easy-to-start ↔ formal-harder-to-start*. Rich Pictures, PSM and FCM are positioned toward the participation-emphasising end; BBN and System Dynamics toward the participation-neutral end. Rich Pictures and Theory of Change are toward the intuitive end; BBN and System Dynamics toward the formal end; CLD is near the middle [AP] (Ch 1, Fig 1.2; original PDF p. 25).

   Verified against the original figure on PDF p. 25; axis labels also appear at tape **1010–1045**.

2. **Line 457 — replace its final sentence.**

   **Current:**

   > All other figures are referenced by caption only, and their captions and surrounding prose are the source of every claim about them.

   **Replacement:**

   > Part I also describes the positions of methods in Figs 1.1 and 1.2.

   Verified against post-audit lines **47–48**, tape **949–1045**, and original PDF p. 25. This removes the inaccurate blanket provenance assertion.

These are the only required deep-reference edits identified by this sort. The two confirmed derived-tier defects require separate corrections; neither can be repaired by changing the already accurate deep-reference passages.

## 4. Counts

Counts deduplicate the Rich Picture finding shared by both auditors and distinguish the historical audit from the current scoped audit.

| Outcome | Count |
|---|---:|
| Confirmed auditor findings | **6** |
| — Correctly fixed | 3 |
| — Fix incomplete or still outstanding, including derived tier | 2 |
| — Missed by the fixer | 1 |
| Additional defect introduced by a historical fix | **1** |
| Over-flagged — blind auditor | **0** |
| Over-flagged — fixer | **1** |
| Disputed | **1** |
| Editorial correction excluded from defect counts | **1** |

The fixer’s over-flag is historical. No current scoped blind finding was over-flagged.

## 5. Gate verdict

**Scoped deep-reference gate: PASS once remaining edits 1–2 are applied.**

**Complete Pass I shipment gate: FAIL until the two confirmed derived-tier defects are corrected and the affected derived artefacts are re-derived or reconciled and stamped against the final audited deep.** Applying only the deep-reference edits leaves the light-reference overgeneralisation and the software-business forecasting prohibition in place.

This verdict does not certify a new full-book audit or independently verify the historical OCR and full-read process assertions.