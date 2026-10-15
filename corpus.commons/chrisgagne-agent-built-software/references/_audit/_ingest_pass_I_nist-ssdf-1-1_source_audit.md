# Pass I source audit: nist-ssdf-1-1

- **Date:** 2026-10-15
- **Mode:** audit (fix in place), same-family leg (Claude Opus 5.5). A blind cross-family leg (Codex) runs in parallel on a frozen copy; the driver stamps once every leg is done. The deep reference is not stamped by this leg.
- **Deep reference:** `references/nist-ssdf-1-1-deep.md` (229 lines), read in full: lines 1–229.
- **Tape:** `sources/converted/nist-ssdf-1-1.md` (2298 lines), read in full: lines 1–2298 (cover, authority, front matter, §1, §2, all of Table 1 pp. 5–19 with footnotes 1–9, References pp. 20–23, Appendices A–C).
- **Calibration:** protocol Pass I + failure-mode reference; fixtures 01, 07, 12 read before the cold read.
- **Page renders used:** 1 of 10 (PDF p. 21 / printed p. 12), to check the shading claims at deep lines 129 and 197. The source is born-digital, not scanned, so the tesseract check doesn't apply.

## Counts

| Measure | Count |
|---|---|
| Claims audited | ~110 (approximate count) |
| Source-anchored as written | all but 1 |
| Corrected (paraphrase distorted the source) | 1 |
| Stripped | 0 |
| Marker-corrected | 0 |
| Quotation-corrected | 0 |

Claims are counted as the separable assertions in each paragraph, table row, statistics row and connections bullet. Frontmatter provenance and process notes (Coverage line, source-integrity bullets about conversion and acquisition) were checked for consistency with the tape (36 PDF pages, footnotes 1–9, Table 1 spanning printed pp. 5–19, editorial page anchors and appendix labels) but not counted as source claims.

## Verbatim check

`python3 scripts/check-verbatim.py` before and after: **no findings**. Both blockquotes (Executive Summary p. vi; §1 p. 3) match the tape word for word.

## Changes

1. **Line 145 (PW.5.1 examples), corrected.** "support secure coding with development-tool training" misread Example 5, which is about development environments, not training on tools. The source (Table 1, PW.5.1, p. 13): "Use development environments with automated features that encourage or require the use of secure coding practices with just-in-time training-in-place." Now reads "use development environments whose automated features encourage or require secure coding with just-in-time training-in-place". Marker `[AP] [AE]` unchanged.

## Checked and kept (possible flags, judged clean)

- **Line 129 / 197, shading.** "unshaded rows" for retired identifiers and "shaded live-practice rows": Appendix C (p. 27) says retired practices and tasks are indicated "by a lack of shading", and the p. 12 render shows PW.3.1, PW.3.2 and PW.4.3 unshaded against shaded live rows.
- **Line 141, PW.4.5 discrepancy.** Table 1 (p. 13) says "Moved to PW.4.1 and PW.4.4"; Appendix C says "Deleted PW.4.5 (merged into PW.4.4)". The deep reference records both without adjudicating. Clean.
- **Line 211, NISTCSF.** "against fourteen tasks": 14 NISTCSF rows in Table 1 (PO.1.1–PO.1.3, PO.2.1–PO.2.3, PO.5.1, PO.5.2, PS.1.1, PS.2.1, PS.3.1, PW.1.1, PW.4.1, PW.4.4). PR.AT and ID.RA are category-level as stated. The closing clause ("the source does not comment on how these sit with the footnote") puts footnote 2's "do not map" next to the Table 1 listings, two explicit source statements, without judging between them. Kept, on the same grounds as line 141. The cross-family leg may read it as framing; if so, it's a disputed item, not a confirmed defect.
- **Line 207.** "it does not provide a measured percentage reduction in vulnerabilities". This is an absence claim, confirmed by the full read, and records provenance without grading the source.
- **Line 133, PW.4 `[AR]`.** The practice's purpose statement (lower costs, expedite development, decrease the likelihood of new vulnerabilities, "particularly important" for security functionality) supports the paraphrase and the argument marker.
- **Line 5 / 228, licence.** The worldwide-permission claim rests on the external NIST policy page named and dated in line 228. The Authority page (PDF p. 3) supports "not subject to copyright in the United States". This is provenance metadata, not a source claim.
- **Front matter and connections (lines 21–25, 212–216).** Every cited external work (IR 7864, SP 800-53 Rev. 5, IR 7692, SP 800-160 Vol. 1, SP 800-207, the code-signing white paper, BSA, BSIMM12, CNCF, IDA SOAR, IEC 62443-4-1, ISO/IEC 27034-1/29147/30111, MSSDL, PCI Secure SLC 1.1, the five SAFECode guides, the four OWASP editions, IR 8397, NISTLABEL, NTIA SBOM, SP 800-161 Rev. 1 second draft, SP 800-181, draft SP 800-216, EO 14028, and the three footnote 4 getting-started works) appears in the source's references or footnotes. No cross-corpus drift.

## TOC-vs-anchors

Every TOC entry (Executive Summary; §1; §2; References; Appendix A; Appendix B; Appendix C; Tables 1 and 2) and every front-matter unit (Authority, Abstract, Acknowledgments, Audience, Note to Readers, Patent Disclosure Notice) is anchored in the deep reference. Every practice and task in Table 1, including the retired identifiers, has a body anchor. No `coverage: partial` needed. Gate passes.

## Fail-condition sweep

There's no training leakage, no post-source vocabulary, no task-application guidance, no evidence-quality rankings, plausibility judgements, methodological verdicts or evaluative labels, and no market or legal framing. The single "frames against" entry (line 220) rests on the source's explicit statement that "The intention of the SSDF is not to create a checklist to follow" (§1, p. 3), so it isn't an invented opposition.

## Derived tier

- **Light reference** (`references/nist-ssdf-1-1.md`): doesn't carry the PW.5.1 Example 5 claim (its PW/PO summary lines don't mention development-tool training). No re-derivation is needed for this change, but the deep reference's hash has changed, so the provenance stamp needs refreshing once the driver closes Pass I.
- **Distillations:** none in `distillations/` reference `nist-ssdf-1-1`.

## Open

- The cross-family leg's findings are still to be sorted (confirmed / missed / over-flagged / disputed) by the driver.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `575e0e7e20ad092db69a25d0abb0bb554d4f62959ad9885ebd23690edf66e5a9`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `d03e176171335f302218937fbd05b31071eaa75ddcfcc4ae12948dfd9843d425`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_nist-ssdf-1-1_crossfamily_blind.md`, `_ingest_pass_I_nist-ssdf-1-1_crossfamily_sort.md`, `_ingest_pass_I_nist-ssdf-1-1_crossfamily_prompts.md`.

**Sort result:** The sort found 1 confirmed defect (PW.5.1 Example 5, correctly fixed by the fix-in-place audit), 0 missed by the fix-in-place audit, 0 over-flagged by the fixer, 0 over-flagged by the blind auditor, 0 disputed and 0 fix-introduced defects, with a gate verdict of pass.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 1, the blind audit 0, both 0. The Chapman estimate is 1 in all, about 0 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** The sort listed no remaining edits, so none were applied as written, none with changed wording and none declined; the one confirmed fix (deep line 145, PW.5.1 Example 5) was re-checked against tape lines 1440–1442 and stands.

**Gate:** pass. Deep reference sha256 `93d22e3be667bc14742194e82189753c7bd7c09cc962392a548ceff8de56e5f3`, stamp included.

## Derived-tier fidelity check (2026-10-15)

The light reference `nist-ssdf-1-1.md` was checked in full against the audited deep reference, with the NIST SP 800-218 tape opened for wording and anchors: 33 claim units checked, 2 fixed. One fix restored scope (RV.1 gathers all potential vulnerability reports and investigates the credible ones, not only credible reports); one restored a dropped hedge (Appendix A maps EO 14028 Section 4e subsections to practices and tasks that can help address them as part of a risk-based approach). Every other unit, anchor and marker traces to the deep reference. No distillations or distillation-index rows exist for this source. No defect was found in the deep reference.
