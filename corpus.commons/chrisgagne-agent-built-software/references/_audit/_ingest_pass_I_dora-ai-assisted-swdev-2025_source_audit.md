# Pass I source audit: dora-ai-assisted-swdev-2025

- **Deep reference:** `references/dora-ai-assisted-swdev-2025-deep.md` (384 lines; read in full, lines 1–384)
- **Source:** `sources/converted/dora-ai-assisted-swdev-2025.md` (13,537 lines; read in full, lines 1–13,537, cover to p. 142 back cover)
- **Mode:** audit, fix in place. Same-family leg (Claude). A blind cross-family leg (codex) runs separately on a frozen copy. This log does not stamp the deep reference; the driver stamps once both legs are done.
- **Date:** 2026-10-15
- **Calibration:** read fixtures 01, 07 and 12 before the cold read.
- **Page renders:** none used (0 of 10). The cluster-profile descriptions on pp. 17–18 were checked against the interleaved tape text, which holds every word the deep reference paraphrases.

## Checks run

- `scripts/check-verbatim.py` before and after the audit: no findings either time (18 figure claims not checked). No quotation needed correcting.
- Page anchors: computed form-feed page numbers for about 110 tape lines (every chapter opener, every subsection the deep reference cites, every interview and pull quotation). All non-`[V]` page citations match; the checker covers the `[V]` pages.
- Provenance in the source-integrity notes, checked against the files: sha256 `b403c537…f8` matches; `pdfinfo` gives 142 pages, Adobe InDesign, created 15 October 2025; the tape has 13,537 lines, 42,980 words and 142 form feeds; the chapter-opener line numbers (705, 2404, 3569, 5081, 6376, 7248, 7712, 8397, 8879, 9487, 10769, 12589) each start the stated page.
- TOC against anchors: every Contents entry (p. 2) and every chapter, sidebar and case note in the tape is covered by a heading or anchor in the deep reference, from the executive summary to the p. 141 licence line. No `coverage: partial`; none needed.

## Counts

| Item | Count |
|---|---|
| Inline evidence markers traced | 502 (185 `[V]`, 52 `[AP]`, 133 `[AR]`, 88 `[AE]`, 44 `[BT]`) |
| Key-statistics rows traced | 24 |
| Connection bullets traced | 18 |
| "Frames against" bullets traced | 12 (each has an explicit passage: "is a myth", "does not hold up", "caution against", "common misconception", "pitfalls", "isn't falling behind", and so on) |
| Header and source-integrity statements traced | about 30 |
| Source-anchored | all but one |
| Stripped | 0 |
| Corrected | 1 (source-external characterisation) |
| Marker-corrected | 0 |
| Quotation-corrected | 0 |

## Changes

1. **Line 7 (Type line): "invited sidebars" → "signed sidebars".** No passage says the sidebars were invited. The source shows only that each sidebar carries a byline (pp. 28, 44, 88). This is source-external framing; the fix keeps the factual part.

## Reviewed and kept (recorded so the second leg can sort them)

- Line 152, skill reprioritisation: "higher adopters rated prompt engineering and … syntax memorisation as more important". p. 47 says adoption "impacted" prompt engineering's importance, then that it "also increased" syntax memorisation's. The "also" supports reading the first as an increase. Kept.
- Line 379, "Interview quotations are anonymous by design (p. 115)". p. 115 says quotations were edited "only in cases where required for clarity or anonymity", and no quotation names its speaker. Supported closely enough. Kept.
- Line 88, Sabre "adoption … rising to 74% over 18 months". p. 26 tracks adoption "over the past 18 months" and says it "has surged to 74%". Kept.
- Line 377, the notes on cluster 4 ("low throughput" on p. 17, cited for "speed without stability" on p. 19) and on the two instability trade-off readings (pp. 41, 66, 70). These record tensions as printed and pass no verdict. Kept.
- Line 383, "Pass I: see the stamp on line 2 and the audit log." This is the driver's stamp line, left untouched as instructed.

## Derived tier

A light reference exists (`references/dora-ai-assisted-swdev-2025.md`); there is no distillation for this slug under `distillations/warranting-agent-built-software/`. The light reference does not carry the one changed claim: its Structure line says "sidebars by Edward Fraser, Daniella Villalba and Matt Beane", with no "invited". No derived claim depends on this edit, so it needs no re-derivation. The parent still re-stamps provenance after the driver stamps, because the deep reference's hash has changed.

## Open

- Cross-family leg pending (driver-run, blind). Until it reports, treat this reference as audited but unverified.
- Nothing else is open.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `22d2a6c2d0cd9601ef832858d73f02693967557a21f2c6c392906949d666266b`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `1dc3fbb44daa3abf82bc223e7f70f46c1b5a1851d0d5ec1e64fbd5164db99db3`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_dora-ai-assisted-swdev-2025_crossfamily_blind.md`, `_ingest_pass_I_dora-ai-assisted-swdev-2025_crossfamily_sort.md`, `_ingest_pass_I_dora-ai-assisted-swdev-2025_crossfamily_prompts.md`.

**Sort result:** The sort counts 68 confirmed defects (1 confirmed and fixed by the fix-in-place audit, 0 with a wrong or incomplete fix, 67 missed by it and caught blind), 0 over-flagged by the fixer, 1 over-flagged by the blind auditor (B8, the Survey experience subsection), 0 disputed, 0 introduced by the fixer, and a gate verdict of pass once the remaining edits are applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 1, the blind audit 67, both 0. The Chapman estimate is 135 in all, about 67 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Of 42 remaining edits, 37 were applied as written (the 35 marker edits correcting 60 [AE] markers to 58 [AP] and 2 [BT], plus the AI-user reliance and Adidas-subgroup table rows), 4 with changed wording (line 5 keeps the footer claim but limits it to the numbered pages, pp. 2–141, which the tape shows all carry v. 2025.2; line 88 keeps the source's 'steady rise' and credits the 'suggests' to the Sabre note; line 227 follows the interviewee's own words on p. 76; the Sabre table row uses the source's 'newest' features and 'increased productivity'), and 1 declined (edit 7, stripping the line-383 stamp pointer: scripts/pass_i/run.py writes that exact pointer itself and inserts the stamp at line 2 in finalize, so it becomes accurate when the driver stamps, and the brief reserves that line to the driver).

**Gate:** pass. Deep reference sha256 `05b9ee7f273ffe9ac74c7ba80aaf62eda52032c97037b9d71d195bdc09bc2433`, stamp included.

## Derived-tier fidelity check (2026-10-15)

The light reference for DORA's *State of AI-assisted Software Development* (2025) was checked against the stamped deep reference, with the tape opened at 16 passages. Of 103 claims, 9 were fixed in place. Two restored attribution: the mirror-and-multiplier framing to Kalliamvakou, and the Stack Overflow comparison to interviewees rather than the authors. Four restored dropped or weakened hedges: "not yet evolved", "may add cognitive load", "not necessarily a goal", and "needs to be treated as a transformation effort". One narrowed a widened scope: friction moves "for the individual". One corrected a changed frequency: "as likely by simple observation as from a dashboard" replaced "often". One restated a causal phrasing as the association the report gives: ownership "not associated with" a diminished sense, with the tool-like-a-compiler clause reattached to AI. The verbatim check on the edited file reports no findings. No distillation or task-index row exists yet for this source, and no defect was found in the deep reference.
