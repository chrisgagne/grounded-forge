## Scoped re-audit 2026-10-16: restored tables and figure labels

**Outcome:** No defects found in the scoped deep-reference additions. Two defects found in derived additions, with exact fixes below. This is the blind-leg report; findings have not been compared with the other auditor’s findings.

### 1. Material read

Read in full:

- `blind-brief.md`, all three calibration fixtures, `pass-i-spec.md`, `frozen-deep.md` and `source-card.md`.
- Every prescribed tape range: 1050–1110, 1160–1560, 2395–2550, 3660–3870, 4590–4840 and 8150–9300.
- The specified additions to the light reference, AAR, retro and software-business distillations, identified against `origin/main`.

Inspected relevant parts of the original PDF: title and legal pages; Fig 1.3 on PDF p. 26; Fig 3.2 on p. 52; Figs 6.1 and 6.3 on pp. 98 and 100; and table layouts on pp. 177, 183 and 186.

(`_planning/pass-i/demo/barbrook-johnson-systems-mapping/source.pdf`)

Ran `check-verbatim.py` against the frozen reference and supplied tape. Verified the frozen-reference checksum and the PDF checksum recorded in the source card.

The remaining tape was not substantively read. Unchanged deep-reference content was read for context but was not re-audited. Historical conversion comparisons and the claimed full-document OCR check were not independently reproduced.

### 2. Findings

1. **Light reference, line 57 — unsupported generalisation of Table 11.3.**

   **Text:** “embed any map in a Rich Picture”.

   **Deep-reference anchor:** frozen-deep.md, line 378.

   **Evidence:** Tape lines 9216–9234; Table 11.3, PDF p. 186. The RP row specifies embedding CLD, FCM, PSM and ToC maps. Its SD cell specifies sketching plots of SD outputs; its BBN cell is blank. The deep reference preserves these distinctions correctly. “Any map” broadens the listed proposal.

   **Exact fix:** Replace that clause with:

   > embed CLD, FCM, PSM or ToC maps in a Rich Picture, or sketch plots of System Dynamics outputs

2. **Software-business distillation, line 73 — source-external methodological verdict; dropped qualification.**

   **Text:** “A market or org-design question with many influential factors is one the book says no method here forecasts.”

   **Deep-reference anchors:** frozen-deep.md, lines 358–366.

   **Evidence:** Tape lines 8970–8973, 8994–8998, 9050–9056 and 9078–9081; Table 11.2, PDF p. 183. The authors offer a simplified judgement about the *most appropriate* methods. “None” appears for forecasting where the salient aspect is a highly interconnected open system or a variety of stakeholder perspectives. They explicitly qualify the table as a simplification that omits decision-relevant aspects. They do not state a categorical inability to forecast market or organisation-design questions.

   **Exact fix:** Replace the final sentence with:

   > For a market or organisation-design question, consider whether either of those system properties is salient; the authors caution that Table 11.2 simplifies the choice and omits other relevant aspects.

### 3. Count and verification outcome

**81 composite claim-bearing units checked:** 69 deep-reference rows or paragraphs, 11 derived rows or paragraphs, and the source-card coverage paragraph. This counting convention treats each table row as one unit; every populated cell within each scoped row was checked.

| Defect class | Count |
|---|---:|
| Unsupported generalisation | 1 |
| Source-external methodological verdict / dropped qualification | 1 |
| Wrong evidence marker | 0 |
| Verbatim quotation defect | 0 |
| Changed quantity or sign | 0 |
| Unsupported cross-reference | 0 |
| Missing scoped coverage | 0 |
| Task guidance in the deep tier | 0 |
| Post-source vocabulary | 0 |
| **Total** | **2** |

**Key-statistics table:** All three new rows match the tape: fifteen Table 1.2 entries; three stakeholder-suggested and four system-suggested PSM starting-point categories; and the Table 11.1 ease-of-use classifications.

**Authors’ limitations:** The scoped exclusion reasons and method constraints match the authors’ statements. The Table 11.2 simplification warning is preserved in the deep reference. Finding 2 concerns its loss in a derived application. Unchanged limitations elsewhere were outside this re-audit.

No scoped source section was found missing from coverage. The restored material is represented in the deep reference without requiring exhaustive reproduction of every source detail.

### 4. Over-flag guard

- **Three slash-related `near` results:** Clean. “templates/inspiration”, “feedbacks/dynamical” and “system/situation” reproduce words split after a slash by the conversion. These are checker limitations.
- **Quotation typography:** Clean. Straight versus curly quotation marks, including nested quotation marks around “Policies”, do not alter the quoted content.
- **Fig 1.3 placements:** Clean. The original visual supports the reported regions and overlaps. `[AP]` appropriately marks the placement descriptions.
- **Fig 3.2 labels and categories:** Clean. The quoted outputs, outcome and impact match the tape and visual; the single funding input is supported.
- **FCM quantities:** Clean. Fig 6.1 contains weights spanning −0.5 to +1. Fig 6.3 shows four scenarios, six identified factors and twenty iterations. The addition says “iterations”, preserving the distinction from elapsed time.
- **Table 5.1’s “two part of the map”:** Clean as a quotation. The grammatical error is present in the source.
- **Table 11.1’s evaluative language:** Clean. “Low risk”, “meaningless analysis”, “highly sensitive to assumptions” and “full rigorous simulation” are the authors’ table wording.
- **Table 11.2’s surprising entries:** Clean. The restored cell alignments match the original table, including its forecasting entries.
- **AAR and retro questions:** Clean. Their new quoted questions match Table 5.1; applying them to reviews or experiments is appropriate in the distillation tier.
- **Software-business concept 19’s new hybrid examples:** Clean. The CLD/SD additions from PSM and the ToC addition from BBN match Table 11.3.
- **Historical provenance assertions:** Not classified as defects merely because the supplied audit packet does not independently establish earlier reading activity or OCR execution. Those historical assertions remain unverified by this leg.

No files were modified. The workspace is read-only, so this report is supplied here rather than appended to the audit log.