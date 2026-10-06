# Pass I source audit: doe-hpi-handbook-vol1

- **Deep reference:** `corpus.commons/demo/references/doe-hpi-handbook-vol1-deep.md`
- **Source (tape):** `corpus.commons/demo/sources/converted/doe-hpi-handbook-vol1.md` (markitdown 0.1.5)
- **Original:** `corpus.commons/demo/sources/ingest/doe-hpi-handbook-vol1.pdf` (175 pp., SHA-256 `82546e3f…66f400e8`, verified)
- **Auditor:** claude-opus-5-5, fresh same-family leg, fix-in-place mode, 2026-10-06. A blind cross-family leg (codex) runs separately on a frozen copy; this log was written without sight of it.
- **Calibration read first:** protocol Pass I and failure-mode sections; fixtures 01, 07, 12.

## Coverage

- Deep reference read in full: 364 of 364 lines.
- Tape read in full: all 12,939 lines. Lines 1–3,499 read directly; lines 3,500–12,939 read from a scratchpad copy with blank lines and consecutive duplicate lines removed (5,788 lines; no text dropped, only figure-repeat noise collapsed).
- TOC-vs-anchors: every chapter, attachment, appendix, the glossary and the concluding material in the handbook's TOC is anchored in the deep reference. No `coverage: partial` needed; none declared.
- Scanned-source check: not applicable. The PDF is born-digital (embedded TrueType/Type 1 text fonts; `pdftotext` yields 64,289 words), so no tesseract pass was run.
- Page renders: 1 of 10 used (PDF p. 120 = handbook p. 4-12).
- Conversion facts in the integrity notes re-checked: 175 pages, 3,516,980 bytes, SHA-256 matches, tape 66,354 words, `pdftotext` 64,289 words. Source line and licence match the source card.

## Counts

| | n |
|---|---|
| Claims audited | ~490 (426 marked claims: 192 `[V]`, 94 `[AP]`, 12 `[AE]`, 128 `[BT]`; plus 18 statistics rows, 22 connection entries, 12 framed-against positions, header and integrity notes) |
| Source-anchored as written | ~479 |
| Stripped | 4 (first names the source never gives) |
| Marker-corrected / quotation reclassified | 1 |
| Corrected (framing, citation, causal over-reach, integrity notes) | 6 |
| Quotation-corrected | 0 (`check-verbatim.py`: no findings, before and after) |

## Changes, by line (line numbers as in the edited file)

1. **L18 (thesis).** "The handbook draws two operating consequences that recur through its chapters" → "Two later passages apply this view to the response to error." *Reason:* source-external framing. The handbook does not present these as its two operating consequences, and the retraining point appears only at pp. 2-27 to 2-28, so "recur through its chapters" over-reaches.
2. **L52.** "INPO responded with tools for engineers and knowledge workers" → "recognising that engineers and knowledge workers make different errors, INPO developed tools for them". *Reason:* invented causal link. The source (p. 1-11) gives INPO's reason as recognising that these workers make different errors. It does not present the tools as a response to the NRC/INEEL study.
3. **L78.** "Four general types of control are previewed:" followed by five items → "The handbook announces four general types of control and describes five". *Reason:* the source says "four" and lists five (pp. 1-17 to 1-18); the deep reference repeated the mismatch without flagging it. Also recorded under source inconsistencies (change 9).
4. **L86.** `the "individual error-prone or apathetic workers" [BT]` → paraphrase "individual workers seen as error-prone or apathetic [BT]". *Reason:* the phrase is a quotation the handbook takes from Reason (in quotation marks, endnote 17). The deep reference's own third-party rule is to paraphrase passages the handbook quotes from named authors.
5. **Connections, Dekker / Daniels / Wickens.** Stripped "Sidney", "Aubrey", "Christopher". *Reason:* training-data leakage. The tape gives only "Dekker, S.", "Daniels" and "Wickens, C.D." (grep: 0 hits for each first name).
6. **Connections, Weick and Sutcliffe.** Stripped "Kathleen" (0 hits in the tape). Citation "(Preface, p. v; …)" → "(Ch 1, endnote 2; …)". *Reason:* the Preface names no authors. The first Weick and Sutcliffe citation is Ch 1, endnote 2.
7. **Integrity notes, conversion damage.** "the production/prevention sidebar (Ch 4, p. 4-12)" → "the prose wrapped around the production/prevention figure". *Reason:* a page render shows body text wrapped around the Leadership figure, not a sidebar.
8. **Integrity notes, conversion damage.** Replaced "No `[V]` quotation in this reference is taken from an interleaved table, sidebar or figure" with an accurate statement. One `[V]` ("on problems beyond the individual", p. 1-9) does come from the integration table, from a cell whose lines survive in order (tape lines 1136–1137, contiguous). The "prevention as optional" paraphrase (p. 4-12) is reconstructed from interleaved lines and was confirmed against the render.
9. **Integrity notes, source inconsistencies.** Added: Ch 1 announces four types of controls and describes five (pp. 1-17 to 1-18).

## Checked and left as written (calibration against over-flagging)

- All 192 `[V]` quotations pass `check-verbatim.py`. Spot-traced page numbers on the quotations at pp. 1-16, 2-27, 3-3, 4-6, 4-10, 4-15, 4-26, 5-11 and on the glossary pages (ii, iv, v, vi, vii, viii, ix): all correct.
- Every endnote attribution in `[BT]` claims was checked against the chapter reference lists: Ch 1 nn. 2, 5, 8–11, 15, 17–19; Ch 2 nn. 16, 23, 24, 27, 31–35, 41, 43, 44, 47, 59, 60, 64, 66–68, 74–76, 82–84, 90, 94, 96, 97; Ch 3 nn. 2, 5, 8–11, 18, 22, 23, 27, 29; Ch 4 nn. 4, 14, 15, 17–20, 24–36, ♠; Ch 5 nn. 3, 7, 11–13, 20–29. All correct.
- Statistics table: all 18 rows match the tape.
- "Positions the author explicitly frames against": all 12 are framed by the source itself (e.g. "a faulty assumption", "a bad strategy", "a waste of time … an insult to the worker", "are not root causes"). None is invented.
- Unmarked 2–4-word terms in quotation marks that come from cited authors ("strong but wrong rules", "resident pathogens", "pilot error", "last chance" barriers) are terms, not passages. Left as written.

## Open items for the parent

- **Header, third-party note:** "The CAIB report the handbook cites (Ch 2, endnote 23) is itself a US Government work." This is a rights judgment the source does not make. It sits in rights metadata rather than in a source claim, so I left it. Strip it if the corpus treats header rights notes as source claims. The Columbia sentences it covers are the handbook's own unquoted prose either way.
- **Cross-family leg:** pending (codex, blind). Until it is sorted, treat this reference as audited but unverified.
- Not stamped, per dispatch. The "Pass I has not run." line was not touched.

## Derived-tier claims to re-derive (not edited here)

- **Light reference** `corpus.commons/demo/references/doe-hpi-handbook-vol1.md`, L12: "Two operating consequences recur." This carries the framing removed from deep L18 (change 1).
- **AAR distillation** `corpus.commons/demo/distillations/aar/doe-hpi-handbook-vol1-aar.md`, L172: "Sidney Dekker". The first name was stripped from the deep reference (change 5).
- Grep found no other changed claim in the light reference or in the `aar`, `decision-making` and `retro` distillations: no "INPO responded", no quoted "individual error-prone or apathetic", no "four general types", no "sidebar", no "Aubrey", "Christopher" or "Kathleen".


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `e3ea93b9a2771f8eff21021a7d1426d8c68ba0c3f901e598688cbc7fbee40043`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `1751c6f2182c2c36c00931bcf19065da65ce169206fd05775f7d817d812be817`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_doe-hpi-handbook-vol1_crossfamily_blind.md`, `_ingest_pass_I_doe-hpi-handbook-vol1_crossfamily_sort.md`, `_ingest_pass_I_doe-hpi-handbook-vol1_crossfamily_prompts.md`.

**Sort result:** The sort confirmed 28 defects (7 correctly fixed, 2 fixed incompletely or left open, 18 missed by the fix-in-place audit, 1 found by the sort itself), found 1 over-flagged by the blind auditor and 1 by the fixer, left 2 disputed, and gave a gate verdict of fail as it stood and pass after its 24 edits.

**Remaining edits applied (2026-10-06):** Of the 24 remaining edits, 13 were applied as written, 11 with changed wording (5 'most' rather than 'several' since five of six attitudes carry examples; 6, 7, 8, 12, 19 and 20 moved closer to the source's words; 10 kept the barrier names and 'very dangerous'; 11 kept the source's 'will unconsciously' instead of 'can'; 14 added 'down'; 22 kept 'interleave columns' under 'Multi-column layouts'), and none were declined; both disputed fixer changes (F1, F2) were retained as source-supported.

**Gate:** accepted by operator. Deep reference sha256 `7675603708056246a950d02ad2da6dd54d85b8b812f0096a1cc0bf955cd8a5c2`, stamp included.

## Derived-tier fidelity check (2026-10-06)

The derived tier for `doe-hpi-handbook-vol1` (US DOE, *Human Performance Improvement Handbook, Vol. 1*, DOE-HDBK-1028-2009, scope open) was checked against the stamped deep reference, with the converted tape opened where wording or anchors needed it. About 434 claims and rows were checked across the light reference (96, 3 fixed), the AAR distillation (135, 15 fixed), the decision-making distillation (85, 5 fixed), the retro distillation (80, 5 fixed), and this source's index rows (AAR 18, 1 fixed; retro 11, 2 fixed; decision-making 9, none fixed). That makes 31 fixes in all. Kinds of fix:
- detail correct in the tape but absent from the deep, narrowed to the deep (12);
- scope widened or a hedge dropped ("tells" for "can", "only", "exactly", a narrowed slip/lapse definition);
- a changed quantity ("90 percent" for "90 percent or more");
- a misplaced quote context (the "Competence does not guarantee positive control" quote sits under personal dependency, not team errors);
- a remedy misstated ("a clearer rule" for retraining) and a precursor misnamed ("identical displays");
- an unsupported culpability-tree outcome and a mislabelled tool list;
- a near-verbatim run from third-party Att. B material that is paraphrase-only;
- two corpus-scope or evaluative phrases in the distillations' own voice;
- three index-row edits to keep the rows tracing to the distillations.

Column counts and slug references were clean. `check-verbatim.py` passes on every edited file. No deep-reference defect was found.
