# Pass I source audit: jimenez-swe-bench

**Date:** 2026-10-15
**Auditor:** claude-opus-5-5, fresh subagent (same-family leg). A blind cross-family leg (codex) runs separately on a frozen copy; this log was written without reading it.
**Deep reference:** `references/jimenez-swe-bench-deep.md` (351 lines; read in full, 351/351).
**Source:** `sources/converted/jimenez-swe-bench.md` (4,441 lines; read in full, 4,441/4,441, all 52 `{page-N}` pages).
**Calibration:** read fixtures 01, 07 and 12 before the cold read.
**Page renders used:** 1 of 10 (p. 25, to confirm the Appendix A.7 break is in the PDF). `pdftotext -layout` checks on pp. 4, 8, 24, 25 and 27 to confirm table row/column pairings (Table 8 Claude 2 row, Table 14, Table 19 psf/requests row, §2.4 gap sentence).

## Verbatim check

- First run: 1 finding, `no-quote` at line 351 (the evidence-markers note names `[V]` in prose; no quotation was intended). Cleared by setting the marker names in code spans.
- Final run: no findings. Every `[V]` quotation and blockquote matches the tape.
- Source is born-digital (pdftotext text layer), not scanned, so the tesseract second-OCR check does not apply.

## Counts

| | Count |
|---|---|
| Claims audited (prose sentences, table cells/rows, list items, markers, cross-references, integrity notes) | ~310 |
| Source-anchored as written | ~306 |
| Stripped | 0 |
| Marker-corrected | 1 (line 253, three marker changes in one passage) |
| Precision-corrected (claim made complete, not reversed) | 2 (lines 216, 347) |
| Quotation-corrected | 0 |
| Verbatim-check false positive cleared | 1 (line 351) |

TOC-vs-anchors: every section of the PDF (§1–§10, references, Appendices A.1–A.7, B.1, C.1–C.7, D.1–D.3, E, F with Tables 25–34) has anchor coverage in the deep. No `coverage: partial`. Pass.

## Changes

1. **Line 253 (App. C.7), marker correction.** The authors' contrast between semantic-similarity scoring and metrics "founded upon logical abstractions" was marked `[BT]`, as if credited to McCabe and Halstead. McCabe and Halstead are cited only to name the metrics; the contrast is the authors' own (p. 28). Changed to `[AP]`. The sentence "A higher Cyclomatic complexity score suggests a more complex function that has higher likelihood of defects…" carries no citation in the source (p. 29) and sat under a `[BT]`; split it out as `[AP]` ("the authors add"). The two definitional sentences, which the source does cite, keep `[BT]` with the citation named inline.
2. **Line 216 (App. C.6, Table 24), precision.** The deep said SWE-Llama's patches are longer than the gold in total lines but shorter in lines added, removed and functions. That is correct, but it left out files edited, where 13b is higher (1.6 against 1.4) and 7b matches (1.5 each). Added, so the comparison with the authors' "longer in most respects" is complete.
3. **Line 347 (integrity note), precision.** Same omission in the "figures that don't line up" list; added "(and 13b in files edited)".
4. **Line 351, verbatim-check false positive.** Marker names in the evidence-markers note put in code spans so the checker reads them as names, not a `[V]` claim. Wording unchanged.

## Checked and left as written (would-be flags not raised)

- Integrity notes' arithmetic on Table 23 (No-Op shares 52%/51%/66%/63%/63%) re-computed: correct. The deep records the mismatch with the text's "60% to 70%" without resolving it, which is the right register.
- Table 14 fix-share ranges, Table 18, Table 19 (psf/requests 15.91 Claude 2, 18.18 SWE-Llama 7b), Table 5, Table 6, Table 7, Table 8, Table 23, Table 24, Table 15 counts and Table 12 licences: all match the tape and `-layout` pairings.
- "Positions the author explicitly frames against": all five items rest on an explicit contrast in the source ("However", "In the real world… not as simple", "In contrast", "drawbacks with such a 'potpourri' style setup", "ill-suited", "Unlike semantic similarity scoring functions"). No invented oppositions.
- Connections section: every named work is cited in the source at the location given; "Lost in the middle" and "Code Llama" titles come from the reference list.
- Source line's arXiv-listing details (version dates, CC BY 4.0) are Pass A provenance, labelled as coming from the arXiv listing rather than the PDF. Not a source claim; left.
- Conversion note's markitdown token counts are provenance about the conversion run, not claims about the source; not verifiable from the tape, left as provenance.
- A.7 gap: confirmed on the p. 25 render and in `-layout` output; "on the SWE-bench task" in the deep matches the PDF ("SWE-\nbench"), where the tape's "SWEbench" is the pdftotext hyphen join the deep already records.

## Open

- §A.5 says "the absolute majority of issues are associated with bug fixes", while Table 13 counts 442 Bug tags of 2,289. Tags are not issues and "Other" tags co-occur, so this is not a clear contradiction; the deep reports the sentence as the authors' note and does not list it among mismatches. Left for the cross-family leg to weigh.

## Derived tier

- Light reference `references/jimenez-swe-bench.md` exists; not edited. It does not carry the changed claims: its App. C.7 sentence (line 60) reports the Figure 10 case and the authors' conclusion, not the McCabe/Halstead marker split, and it has no Table 24 comparison. Line 85 lists McCabe (1976) and Halstead (1977) as "the complexity metrics in App. C.7", which stays correct. Re-derivation is still owed under the protocol's provenance stamp, but no claim needs to change.
- No distillations exist for this slug.

## Stamp

Not stamped, per dispatch: the driver stamps once every leg is done. The deep reference's "Pass I has not run." line, if present, was not touched.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `7646b635b2ce0eb0b8c6d68bb637af133b9f3ab3150564d6ba754959ec896424`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `5ecfc665c7976ccd2947e6273947345f6c6cd4a4fabe5db16b84dd89582f5708`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_jimenez-swe-bench_crossfamily_blind.md`, `_ingest_pass_I_jimenez-swe-bench_crossfamily_sort.md`, `_ingest_pass_I_jimenez-swe-bench_crossfamily_prompts.md`.

**Sort result:** The sort found 3 confirmed defects (1 fixed in place, 0 with a wrong or incomplete fix, 2 missed by the fix-in-place audit), 2 over-flagged by the fixer, 0 over-flagged by the blind auditor, 1 disputed and 0 introduced by the fixer, with a gate verdict of pass once the two remaining edits are applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 1, the blind audit 2, both 0. The Chapman estimate is 5 in all, about 2 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Of the two remaining edits, one was applied as written (line 297, 10,000 instances with at most 30,000 tokens, p. 4 §3) and one with changed wording (line 320: the cited program-repair and commit-guided editing works keep [BT], and the authors' statement that no existing dataset matches SWE-bench's code-context scale is marked [AP], matching line 59 and p. 9 §6), with none declined; the disputed line 253 marker change was settled against p. 28–29 App. C.7 as acceptable and left.

**Gate:** pass. Deep reference sha256 `d44a7b6dafcb6e2de6a428704b33b5f822a6b1b2d4856cf41949ea985587415a`, stamp included.

## Derived-tier fidelity check (2026-10-15)

Pass I fidelity check of the derived tier for `jimenez-swe-bench` (Jimenez et al., SWE-bench, arXiv:2310.06770v3): the light reference was read in full against the audited deep reference, with the tape opened at four passages. No distillation or distillation-index row exists for this source. Of 86 claims checked in the light reference, 2 were fixed in place. One relabelled the training set to match its §1 anchor ("non-testing task instances", not §3's "issue-PR pairs"). The other restored a dropped intensifier ("struggle significantly"). The verbatim check is clean, and no defect was found in the deep reference.
