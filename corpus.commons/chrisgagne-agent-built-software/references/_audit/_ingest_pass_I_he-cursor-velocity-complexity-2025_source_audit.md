# Pass I source audit: he-cursor-velocity-complexity-2025

- **Date:** 2026-10-15
- **Auditor:** claude-opus-5-5, fresh subagent, fix-in-place mode (same-family leg; a blind cross-family leg runs separately on a frozen copy)
- **Deep reference:** `references/he-cursor-velocity-complexity-2025-deep.md` (250 lines), read in full, lines 1–250
- **Tape:** `sources/converted/he-cursor-velocity-complexity-2025.md` (3,052 lines), read in full, lines 1–3052 (pp. 1–19, References and Appendices A–D included)
- **Calibration:** fixtures 01, 07, 12 read before the cold read
- **Page renders:** 4 of 10 allowed, 110 dpi: pp. 1 (Figure 1), 7 (Table 2), 8 (Table 3), 16 (Table 6). All rendered cleanly. The source is born-digital (arXiv GenPDF), so the scanned-source tesseract check does not apply.

## Counts

| | n |
|---|---|
| Claims audited (sentences or clauses, table rows, list items, notes) | ≈245 |
| Source-anchored as written | ≈240 |
| Corrected in place (wording over- or under-stated the source) | 4 |
| Stripped | 1 (a clause, not a whole claim) |
| Marker-corrected | 0 |
| Quotation-corrected | 0 |

`check-verbatim.py` before and after: no findings; 60 `[V]` markers, 25 figure claims not checked by the script. Every figure claim was checked by hand against the tape (Tables 1–9, Appendix A–D text) or against the renders.

## Gate checks

- **TOC vs anchors:** every section in the paper (§1–§6, Data Availability, Acknowledgments, References, Appendices A, B.1–B.3, C, D, Tables 1–9, Figures 1–7) appears in the Structure line and is anchored in the body or notes. Coverage line is accurate; no `coverage: partial`.
- **Provenance:** PDF sha256 matches the deep reference and source card (`9ad060ac…4da9`); pdfinfo gives 19 pages, creator arXiv GenPDF, created 2026-01-27; tape is 3,052 lines and 17,912 words as stated; the 19 `{page-N}` line numbers in the notes match the tape.
- **Render-based claims:** Table 2 stars (lines added \*, warnings and complexity \*\*\*, commits and duplicate density none), Table 3 stars (Cursor → complexity \*\*, both lines-added → quality main effects and Cursor → warnings none, all other coefficients \*\*\*) and Table 6 stars (TWFE duplicate density none, other TWFE \*\*\*; Callaway and Sant'Anna lines added \*\*, others none) all confirmed on the renders. The notes' description of how the default-mode tape garbles the stars is accurate.
- **Table 1** (column-interleaved in the tape): contributors 1.0 / 3.0 / 10.0 / 19.2 and stars median 51.0, mean 1,475.3 decoded from the tape's column runs and consistent.
- **Connections section:** every cited work is cited by the paper at the place given; reference numbers match the bibliography.
- **Positions section:** all five are explicit framings in the source ("challenges both unbridled optimism and categorical pessimism", "cannot be extrapolated from prior studies", "challenges simplistic narratives", TWFE "may produce biased estimates", "generation-first, leaving quality maintenance as an afterthought"). No invented oppositions.
- **Source-external framing:** none found. No evidence-quality rankings, plausibility verdicts or methodological grades in the ingester's voice; the source-integrity notes record provenance and printed inconsistencies without grading the paper.
- **Task guidance, post-source vocabulary, training-data leakage:** none.

## Changes

1. **Line 29** (Becker et al.): "pointing to slowdown mechanisms" → "pointing to potential slowdown mechanisms". The source (p. 2) says "pointing to potential slowdown mechanisms"; dropping "potential" hardened a hedged claim.
2. **Line 125** (Appendix B.1, TWFE): "only under effect homogeneity, which staggered adoption likely violates" → "only under both the parallel trend and the effect-homogeneity assumptions, and that effect homogeneity is likely violated under staggered adoption". The source (p. 15) conditions the variance-weighted-average equivalence on both assumptions.
3. **Line 169** (Figure 1 description): "warnings and complexity, grouped as technical debt / quality measures" → the three measures (warnings, complexity, duplicate line density) "sit in a dashed box labelled 'Technical Debt / Quality Measures'". The p. 1 render shows duplicate line density inside the box; the arrow styles the deep reference gives (solid/dashed/solid/dotted, two solid negative arrows back to velocity) are confirmed.
4. **Line 200** (Key statistics, Table 8): metric label "Logic Error / Security new warnings per repository-month" → "change in mean new warnings per repository per month, pre- to post-adoption". +2.09 and +1.98 are Table 8's Change column, not levels.
5. **Line 247** (licence note): stripped "and the arXiv abstract page". The abstract page is not part of the source; the licence is anchored by the p. 1 notice, which the line keeps.

## Derived tier

- Light reference `references/he-cursor-velocity-complexity-2025.md` exists. A grep for the changed wording (slowdown mechanisms, homogeneity, Figure 1 grouping, Logic Error / Security, abstract page) finds none of it there, so no light-reference claim is known to depend on these edits. Re-derive and stamp per protocol after the driver closes Pass I anyway.
- No distillations exist for this slug.

## Left open

- Nothing in the deep reference. The paper's own inconsistencies (complexity 41.6% vs 25.1%/25%; 806/1,380 vs 801/1,172 repositories; Appendix A's "Figure 5" for Table 5; B.1's "Section 3.1.3") are already recorded as printed in the source-integrity notes.
- Line 249 says "Pass I: see the stamp on line 2"; line 2 is blank until the driver stamps. Left as instructed.
- Not stamped; the driver stamps after the cross-family leg.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `2beed195e8ae6876b884945554243156b7b00bc5ba775a2958f95218379b6425`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `8b9de3a06974cd8dd3e76ab068bc17d23730a304c8548828a0bb0c2ddb2f396f`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_he-cursor-velocity-complexity-2025_crossfamily_blind.md`, `_ingest_pass_I_he-cursor-velocity-complexity-2025_crossfamily_sort.md`, `_ingest_pass_I_he-cursor-velocity-complexity-2025_crossfamily_prompts.md`.

**Sort result:** The sort found 6 confirmed original deep-reference defects (4 fixed correctly by the fix-in-place audit, 0 fixed wrongly, 2 missed by it), 1 new defect introduced by a fixer edit, 1 confirmed defect outside the deep reference, 0 over-flagged by either auditor, 1 disputed (fixer) and 0 disputed (blind), capture fixer=4 blind=3 both=1, and a gate verdict of pass once its three remaining edits are applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 4, the blind audit 3, both 1. The Chapman estimate is 9 in all, about 3 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** All 3 remaining edits were applied as written (line 127 restores 'statistically significant' per tape line 2445; line 169 'dashed' → 'dotted' box, confirmed on the p. 1 render; line 249's dangling stamp pointer stripped), none changed or declined, and the disputed Figure 1 grouping finding was settled for the fixer because the p. 1 render shows all three quality measures inside the labelled box.

**Gate:** accepted by operator. Deep reference sha256 `81bef9e67174513471e3b115de00c3ae5719b119ee252b911a740b90461421c7`, stamp included.

## Derived-tier fidelity check (2026-10-15)

The light reference for `he-cursor-velocity-complexity-2025` was traced against its audited deep reference, with the tape opened at §1, §2, §4.2, §5.1 and Appendix C; 73 claims checked, 10 narrow edits across 9 sentences. The fixes restored four dropped hedges ("may generate", "may stem from" two possible sources, "may lead to" abandonment, and "fully" in "does not fully explain"), narrowed two widened scopes ("systematically investigated" prior studies; complexity debt "in projects that use AI heavily"), replaced an interpretive "direct" with the source's "holding other dynamics constant", reattached the slightly weaker warning and complexity effects to the cohort split rather than the language split, attributed the "generation-first" judgement to the authors, and restated the Kumar et al. connection as the deep gives it. The source has no distillation and no distillation-index row; seven mentions of it in other sources' distillations claim nothing the deep reference lacks. No deep-reference defect was found, and the verbatim check on the edited file is clean.
