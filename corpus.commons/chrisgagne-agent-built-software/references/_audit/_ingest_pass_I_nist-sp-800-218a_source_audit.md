# Pass I source audit: nist-sp-800-218a

- **Date:** 2026-10-15
- **Leg:** same-family (Claude Opus 5.5, fresh subagent, fix-in-place). The cross-family leg (codex) runs blind on a frozen copy; this reference counts as audited-but-unverified until that leg's findings are sorted against this log.
- **Deep reference:** `references/nist-sp-800-218a-deep.md` (332 lines), read in full, lines 1–332.
- **Source:** `sources/converted/nist-sp-800-218a.md` (1,172 lines, `pdftotext -layout`, poppler 26.08.0), read in full, lines 1–1172.
- **Calibration:** protocol Pass I and failure-mode sections; fixtures 01, 07, 12 (and 08 for the `[BT]` calibration).
- **Page renders used:** 0 of 10. The source is born-digital, so no scanned-source OCR check applies. Table 1 placement claims (PO.5 tag in the Practice column, PO.5.1 C1 printed before R1, PW.8.1's empty Informative References cell) are visible in the tape's column positions (lines 618–629, 916–924).

## Counts

| | n |
|---|---|
| Claims audited | ≈ 410 (prose sentences, task/practice bullets item by item, each informative-reference list, table cells, connections, notes) |
| Source-anchored as written | all but 2 |
| Stripped | 0 |
| Marker-corrected | 0 |
| Quotation-corrected | 0 (`check-verbatim.py`: no findings, before and after) |
| Claims corrected in place | 2 |

## Verbatim check

`python3 scripts/check-verbatim.py` on the deep reference reported no findings before the audit and none after. Table 1 quotations were spot-checked for contiguity under `-layout` interleaving (PO.1.2 C1/N1, PO.5.1 R4/R6, PS.1.1 R4/C1, PS.1.3 R4, PS.3.1 N1, RV.2.2 C1): each sits on tape lines where no other column carries text, as line 322 of the deep reference claims.

## Changes

1. **Line 97, training-data gloss.** "The AI RMF entries are given as function names and numbers (Govern, Map, Measure, Manage …)" → "given as a name and number (Govern, Map, Measure or Manage …)". The source never calls Govern/Map/Measure/Manage "functions" (the tape's only "function" hits are unrelated, lines 263, 844, 853, 939). That label is the ingester's knowledge of the AI RMF, and it contradicts the reference's own line 332 ("no glosses of the AI RMF … identifiers").
2. **Line 318, PDF metadata date.** "created 2024-07-26" → "created 2024-07-25, UTC−04:00". `pdfinfo -rawdates` gives `D:20240725200545-04'00'`; the 26 July date came from pdfinfo's conversion to the local (NZ) time zone.

## Checked and left as written

- **Tallies (Key statistics):** 20 practices, 48 tasks (PO 14, PS 6, PW 19, RV 9); priorities 21 High / 22 Medium / 5 Low; 10 "No additions"; 6 "Not part of"; 3 tasks + 2 practices "Modified": all recounted from the tape and correct.
- **Every informative-reference list in Parts III–VI** was checked against the tape's References column, task by task. All match, including the empty cells (PW.1.3, PW.4.2, PW.6.1, PW.6.2, PW.7.1, PW.8.1).
- **Page anchors (line 320)** and conversion facts (30 form feeds, 1,172 lines, 9,789 words, sha256, PDF title/author/creator): all reproduced.
- **Positions the author explicitly frames against:** all three bullets rest on explicit source rejections ("not a checklist to follow", p. 4; "should not be used without SP 800-218", p. 1, and "not on its own", p. 8; "do not distinguish between human-written and AI-generated source code, because …", p. 2, a named alternative the source declines, with its reason). None of them is an invented opposition.
- **`[BT]` on SBOM/SLSA, FISMA/OMB A-130 and OLIR (Connections, lines 306–308):** the source names each one (pp. 13, PDF p. 3, p. ii). These are named rather than cited for a borrowed claim, so the marker is loose, but the connection is in the source. This differs from fixture 08, where the name was absent from the source. Left as written; the codex leg can dispute it.
- **"The case for a separate profile" (line 15) and "The substance is Table 1" (line 19):** both supported. The Introduction gives the novel-risk argument and closes on "these novel risks" (p. 1), and the Profile says Table 1 "defines the SSDF Community Profile" (p. 6).

## Left open

- **Line 330** reads "Pass I: see the stamp on line 2 and the audit log", but line 2 is currently blank. Per dispatch the driver stamps once every leg is done, so this audit leaves both lines alone.
- **Derived tier:** a light reference exists (`references/nist-sp-800-218a.md`); there are no distillations for this slug. The light ref carries neither changed claim: it has no "function" gloss of the AI RMF entries and no PDF creation date (checked by grep). Nothing to re-derive on account of this leg; the parent re-derives and stamps per protocol after the codex leg is sorted.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `768ce9e4ad2319f06e0e291b310e0c546ef74499d0493c51d842cb185a21904a`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `d0b6f241aab79b22fa647307382486843c8cd2649291c173f9177254ccf1a827`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_nist-sp-800-218a_crossfamily_blind.md`, `_ingest_pass_I_nist-sp-800-218a_crossfamily_sort.md`, `_ingest_pass_I_nist-sp-800-218a_crossfamily_prompts.md`.

**Sort result:** The sort found 2 confirmed defects (1 fixed, 1 fix incomplete), 0 missed by the fix-in-place audit, 0 over-flagged by the fixer, 0 over-flagged by the blind auditor, 1 disputed (the PDF creation date) and 0 fix-introduced defects, with a gate verdict of pass once line 330 is stripped.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 2, the blind audit 1, both 1. The Chapman estimate is 2 in all, about 0 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Of 1 remaining edit, 0 were applied as written, 1 was applied with changed wording and 0 were declined: line 330's dangling 'Pass I: see the stamp on line 2 and the audit log.' became 'Pass I has not run.' instead of being stripped, so it is true now and the driver's stamp step rewrites it to the pointer when it inserts the line-2 stamp; the disputed creation date stays as 2024-07-25, UTC−04:00, which matches pdfinfo -rawdates D:20240725200545-04'00'.

**Gate:** pass. Deep reference sha256 `52c24a3af7af9a812b0f6948393e468142e947d505108a165b95033e65ea3780`, stamp included.

## Derived-tier fidelity check (2026-10-15)

Fidelity check of the derived tier for `nist-sp-800-218a` against its Pass I–stamped deep reference, with the tape opened at seven passages. The derived tier for this source is the light reference alone: there are no distillations and no distillation-index rows. Of 80 claims in the light reference, 7 were fixed in place: one scope widening (deployment and operation out of scope restored to *practices for* AI systems *with AI models*), two dropped hedges or quantities (PW.3.1's "provenance (when known)", RV.3.1's "some root causes"), one dropped modal (the risk-based choice of practices restored as a *should*), one consideration restated as a capability (PO.1.2.C1), one C1 given a scope it lacks (PO.5.1, *execution* environments rather than training environments), and one list of usable testing forms read as prescribed (PW.8.1.R1). `check-verbatim.py` reports no findings on the edited file. No defect was found in the deep reference.
