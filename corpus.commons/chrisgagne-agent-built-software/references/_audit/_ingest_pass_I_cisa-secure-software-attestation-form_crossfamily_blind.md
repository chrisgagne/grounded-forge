## 1. What I read

**Read in full:** `blind-brief.md`; all three calibration fixtures; `pass-i-spec.md`; `frozen-deep.md` (244 lines); `tape.md` (all ten pages, including the final form feed); `source-card.md`; and `frozen-deep.sha256`. I also read `CLAUDE.md` and its nine required architecture documents.

**Original inspected in part:** :codex-file-citation{path="_planning/pass-i/chrisgagne-agent-built-software/cisa-secure-software-attestation-form/source.pdf" purpose="source"} — metadata and XMP, document structure, image inventory, all pages’ annotations and AcroForm fields, and the appendix text and layout on pages 9–10. I did not visually render all ten pages.

**Integrity checks:**

- The frozen reference’s SHA-256 matches `frozen-deep.sha256`.
- The original PDF’s SHA-256 matches the checksum recorded in the reference and source card.
- Fresh Poppler `pdftotext -layout` output matches `tape.md` byte for byte.
- The PDF has ten pages, no embedded images, and the recorded metadata and form fields.
- The verbatim checker returned three permissible apostrophe normalisations and no failing quotation matches. Its 19 figure claims were checked manually.

**Audit independence:** I did not read the fixer’s findings, logs, or status. The verbatim checker ran after the initial cold read, rather than before it as the specification requests.

No files were edited. The filesystem is read-only, so this response is the complete report; no report file was written.

## 2. Findings

1. **Deep-reference line 244 — incorrect audit cross-reference.**

   **Text:** `**Audit.** Pass I: see the stamp on line 2 and the audit log.`

   **Problem class:** Administrative/source-integrity cross-reference error.

   **Evidence:** Line 2 of `frozen-deep.md` is blank. The frozen reference contains no Pass I stamp and identifies no audit-log path. This is a reference-internal defect; no tape passage can substantiate the asserted stamp location.

   **Exact fix:** **strip** line 244. Once the completed audit log exists and a stamp has actually been applied, add a verified audit pointer.

   **Qualification:** The absence of a stamp is expected in a pre-audit snapshot. The defect is the pointer to a stamp that is absent, not the unstamped state itself.

**No source-fidelity defects found.** I found no unsupported substantive claim, incorrect evidence marker, changed quantity, dropped load-bearing qualifier, missing source section, fabricated cited connection, task-application guidance, post-source vocabulary, or source-external analytical framing.

**Key-statistics table:** All ten rows match the tape. This includes the control number and expiration date, form version, reporting burden, memorandum dates, attestation-trigger date, version-change example, routine-use notice, and enumeration of Section III requirements. The appendix’s ten mapping rows also match pages 9–10, including all SSDF codes and their assignment to requirements.

**Limitations:** Line 242 accurately records omissions from the document: it provides no POA&M specification, definition of “consistent use,” or attestation deadline. These are observations about absent content, **not limitations expressly stated by CISA**. The reference labels them “What the form does not state,” so it does not misattribute them as the author’s methodological judgements.

## 3. Count

**Claims checked: 107 claim-bearing units** — 87 prose, metadata, or list entries and 20 table rows. Each unit’s constituent assertions and table cells were traced separately; this count uses claim-bearing lines rather than an inflated atomic-claim total. All **147 evidence-marker occurrences** were reviewed: 104 `[V]`, 22 `[AP]`, 20 `[BT]`, and one `[AE]`.

| Defect class | Count |
|---|---:|
| Unsupported substantive claim | 0 |
| Evidence-marker mismatch | 0 |
| Verbatim mismatch beyond permitted normalisation | 0 |
| Quantity or qualifier error | 0 |
| Over-extension beyond source scope | 0 |
| Missing source-section coverage | 0 |
| Unsupported author/work connection | 0 |
| Task guidance, post-source vocabulary, or external analytical framing | 0 |
| Incorrect administrative audit cross-reference | 1 |
| **Total** | **1** |

**Disposition:** The substantive reference passes this blind leg’s source-fidelity checks. The administrative pointer requires correction. This report does not apply a stamp or replace the subsequent reconciliation of both audit legs.

## 4. Over-flag guard

- **Lines 35, 37 and 106: straight versus curly apostrophes.** The checker identified these three cases. They preserve the words and fall within permitted smart-quote normalisation.
- **Line 135: quotation spanning pages 6–7.** The interrupted text is page furniture and footnote material, not an omitted clause. The complete wording also appears uninterrupted in the appendix, tape lines 420–425.
- **Lines 164 and 234: “employs” versus “employed.”** Both variants exist: tape line 327 uses “employs”; line 457 uses “employed.” The reference correctly preserves the discrepancy.
- **Lines 62 and 234: repeated “directly.”** The awkward wording is present on page 5, tape line 233. Correcting it would reduce fidelity.
- **Lines 170 and 181: four SSDF codes without their usual dot.** Page 10 prints `PO 1.1`, `PW 7.1`, `PW 8.1` and `RV 1.1`. Their transcription is correct.
- **`[V]` markers in tables.** The codes and figures reproduce source values. Structural requirement labels identify rows; they do not masquerade as verbatim prose.
- **Line 17: abbreviated thesis summary.** It summarises the four practices; the detailed sections preserve “good-faith effort,” “to the greatest extent feasible,” risk-based encryption, and the other operative qualifiers.
- **Lines 5 and 238: copyright determination.** The reference explicitly attributes the determination to the operator and distinguishes it from the PDF’s statements. It is not presented as CISA’s claim.
- **Lines 9 and 226: 483 source lines.** Numbered output places a terminal form feed on line 484. All substantive content ends on line 483; this does not conceal missing coverage.
- **Line 222: no explicitly opposed positions.** The document states requirements and exclusions without constructing the invented oppositions prohibited by the audit specification.
- **Source-card provenance:** The metadata year, checksum, titles, page count, image inventory and field claims are supported. Historical fetch/check dates cannot be independently reconstructed from the supplied files. The separately attributed March 2024 news-release claim remains unverified: the linked page returned HTTP 403 and a follow-up search returned no result. I have not treated that access failure as evidence that the claim is false.