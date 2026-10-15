# Pass I source audit: cisa-secure-software-attestation-form

- **Date:** 2026-10-15
- **Auditor:** claude-opus-5-5, fresh subagent, same-family leg (fix-in-place). A blind cross-family leg (codex) runs separately on a frozen copy; this log was written without seeing it.
- **Deep reference:** `references/cisa-secure-software-attestation-form-deep.md`, 244 lines, read in full (1–244).
- **Source tape:** `sources/converted/cisa-secure-software-attestation-form.md`, 483 lines, read in full (1–483). Poppler `pdftotext -layout`.
- **Original consulted:** `sources/original/cisa-secure-software-attestation-form.pdf`. 2 page renders out of the 10 allowed (pp. 9 and 10, 110 dpi), used to check the appendix table, which the layout tape interleaves. `pdfinfo`, `pdfinfo -meta`, `shasum -a 256`, `pdfimages -list` and a pypdf AcroForm field listing were used to check the source-integrity notes. The source is a born-digital text PDF, not a scan, so the tesseract scanned-source check does not apply.

## Counts

| Item | Count |
|---|---|
| Claims audited | 177 (147 marked claims: 104 [V], 22 [AP], 20 [BT], 1 [AE]; 30 unmarked claims in the header, prose and source-integrity notes) |
| Source-anchored as written | 175 |
| Stripped | 0 |
| Corrected (claim reworded to the source) | 2 |
| Marker-corrected | 0 |
| Quotation-corrected | 0 |

## Verbatim check

`python3 scripts/check-verbatim.py` before and after the edits: `3 apostrophe; 19 figure claim(s) not checked`. The three apostrophe lines (lines 35, 37, 106: `'` vs `’`) need no fix. There were no `glyph`, `near`, `page`, `interrupted`, `wrong-source`, `missing` or `no-quote` lines. I checked the 19 figures by hand against the tape: dates, the 3 h 20 min burden, the control number and expiry, 2.5→3.0, 73 FR 71659, and every SSDF code in the Part VII table. All match.

## Changes

1. **Line 15 (thesis), source-external framing, corrected.** The line read "The authority it gives runs from FISMA, through Executive Order 14028, … to OMB Memorandum M-22-18". That puts the E.O. inside a chain of authority from FISMA, which the source never does. The source (p. 2, tape lines 59–85) presents three items one after another. FISMA authorises the OMB Director to promulgate information security standards. E.O. 14028 required NIST guidance and requires the OMB Director to ensure agency compliance with it. OMB issued M-22-18 "to that end". The line now sets out the three items in the source's order, each with what the source says of it, and asserts no derivation from FISMA. The quotation, markers and citation are unchanged.
2. **Line 31 (heading), corrected for the same reason.** "The legal chain (p. 2)" is now "FISMA, E.O. 14028 and M-22-18 (p. 2)". The section body was already anchored and is unchanged.
3. **Line 168 (Part VII), incomplete description of the table, corrected.** The line read "The table's columns are Attestation Requirements, Related E.O. 14028 Subsection, and Related SSDF Practices and Tasks". The p. 9 and p. 10 renders show a fourth column, with no heading and no entries, between the subsection and SSDF columns. The tape cannot show an empty column. The line now names the three headed columns and records the empty fourth, citing the page image.

## Checked and found anchored (selected)

- **Appendix row assignment (line 230, Part VII table).** The tape interleaves the columns. The pdfplumber extraction the note cites could not be re-run here: pdfplumber is not installed, and the PyMuPDF wheel is the wrong architecture. The p. 9 and p. 10 renders confirm the assignment directly. Practice 1's parent row and 1a–1f are separate rows. Row 2 → 4e(iii) with 13 codes, four of them printed without the dot. Row 3 → 4e(vi) with 10 codes. Practice 4 and 4a–4c share one cell → 4e(iv) with 19 codes. Every code matches the table.
- **Section III vs appendix wording (line 164).** Checked word by word. "employs"/"employed" in practice 4 is the only difference, and the appendix has no row for the further attestation.
- **Form fields (line 232).** The pypdf listing matches every stated fact: the two p. 3 route checkboxes and their tooltips; the six Section I checkboxes and seven product rows on p. 5; the producer and contact fields split across pp. 5–6; on p. 7, Check Box26 beside the further attestation, a /Sig field, Date Signed, Name, Title, and Check Box20 beside the 3PAO statement; no fields beside practices 1–4; and the tooltip spelling "Designess".
- **Metadata and conversion (lines 5, 9, 226).** Title, subject, author, creator (Acrobat PDFMaker 23 for Word), tagged, AcroForm, JavaScript, 10 pages, XMP dates (2024-04-23T12:30:06-04:00, 2024-04-26T11:52:35-04:00), `xmpRights:Marked` False, the sha256, 483 lines and 2,767 words, 10 form feeds, and no images all match.
- **Page anchors (line 228).** All nine page-start lines and the 1d break (lines 296–312, appendix 420–425) are correct.
- **Third-party assessment, POA&M, signer, scope, conditions, burden statement and connections list:** every quotation and paraphrase traces to pp. 1–8 of the tape.

## Derived tier

- **Light reference** (`references/cisa-secure-software-attestation-form.md`) carries the corrected claim in its line 11: "The authority runs from FISMA, through E.O. 14028, … to OMB M-22-18 as amended by M-23-16". Re-derive it from the audited deep. Its line 19 states the three items separately and matches the corrected deep. It does not carry the table-column description.
- **Distillations:** none exist for this slug.

## Left open

- The deep ref's line 244 ("Pass I: see the stamp on line 2 and the audit log") points at a stamp the driver has not yet written. Line 2 is blank. This leg did not stamp, as dispatched.
- Line 230 still says the row assignment "was confirmed from the PDF with pdfplumber's table extraction". I could not re-run that extraction. The page renders confirm the same assignment, so the claim stands as the ingester's record.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `24c6c303e741099c13b74bb6b4bf3ee7261f88a6d4d420a2010cb12f1c49a1d9`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `ba43954f638905ae58bfe203ef162081a170d7c0f67fbc77022e3da0a418fd17`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_cisa-secure-software-attestation-form_crossfamily_blind.md`, `_ingest_pass_I_cisa-secure-software-attestation-form_crossfamily_sort.md`, `_ingest_pass_I_cisa-secure-software-attestation-form_crossfamily_prompts.md`.

**Sort result:** The sort confirmed 3 defects in the original deep reference (2 fixed, 1 fix incomplete), found 0 missed by the fix-in-place audit, 0 over-flagged by either auditor, 0 disputed and 0 fix-introduced, with capture fixer=3 blind=1 both=1, and gave a pass verdict once its one remaining edit was applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 3, the blind audit 1, both 1. The Chapman estimate is 3 in all, about 0 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Of 1 remaining edit, 0 were applied as written, 0 applied with changed wording, and 1 declined: stripping the line-244 pointer 'Pass I: see the stamp on line 2 and the audit log.', because the driver writes that exact wording and inserts its stamp as line 2 at finalisation (scripts/pass_i/run.py:356-357), so the pointer is true once the driver stamps and was false only in the pre-stamp state the sort read.

**Gate:** pass. Deep reference sha256 `cdf9ad705824a193cbb37dd21c05cca244458c62285ddda633b4bf1eee6f2a51`, stamp included.

## Derived-tier fidelity check (2026-10-15)

The fidelity check of the derived tier for `cisa-secure-software-attestation-form` read the audited deep reference and the converted tape in full and checked the light reference, the only derived file for this source: no distillation or distillation-index row exists for it. Of 83 claims in the light reference, 4 were fixed in place: one widened scope (the designee who signs must be an employee of the producer), one missing anchor (the appendix table rows now carry pp. 9–10), one framing the deep reference lacks (E.O. 14028 subsection (4)(e) described as "the authority" rather than the source of the requirements the minimum requirements address), and one widened claim (NIST Guidance is part of the 3PAO's assessment baseline, not the whole of it). All verbatim passages and appendix codes match the source, the verbatim check reports no findings, and no defect was found in the deep reference.
