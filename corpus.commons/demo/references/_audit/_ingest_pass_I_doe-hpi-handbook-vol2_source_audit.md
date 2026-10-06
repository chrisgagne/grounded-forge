# Pass I source audit: doe-hpi-handbook-vol2 (fix-in-place leg, same family)

**Date:** 2026-10-06
**Auditor:** claude-opus-5-5, fresh subagent, fix-in-place mode. A blind cross-family leg (codex) runs separately on a frozen copy; this log does not read or anticipate it.
**Deep reference:** `references/doe-hpi-handbook-vol2-deep.md` (307 lines; read in full, lines 1–307).
**Source:** `sources/converted/doe-hpi-handbook-vol2.md` (4,547 lines, markitdown 0.1.8; read in full, lines 1–4547).
**Calibration:** protocol Pass I and failure-mode reference read; fixtures 01, 07, 12 read before the cold read.
**Page renders:** none used. The damaged regions (matrix pp. 3–4, probe table pp. 86–87, Anatomy figure p. 88, Culpability Decision Tree p. 99, survey layouts pp. 104–127) are already declared in the deep's integrity notes and none of them carries a quotation or a cell-level claim. The source is born-digital text, not a scan, so the tesseract check does not apply.

## Verbatim check

`python3 scripts/check-verbatim.py` before the read: no findings. After edits: no findings. All 59 `[V]` quotations sit in the Foreword, Introduction, Section 3 prose or Definitions, as the header's third-party policy requires; none falls in Sections 1–2 or the survey instruments.

## Counts

| | |
|---|---|
| Claims audited | ≈383 (338 marker-bearing: 244 [AP], 59 [V], 20 [AR], 13 [BT], 2 [AE]; plus ≈45 unmarked header, structure, coverage, table, positions and integrity-note claims) |
| Source-anchored as written | ≈372 |
| Stripped (phrase or clause) | 3 |
| Corrected (over-extension, citation or figure) | 8 |
| Marker-corrected | 0 |
| Quotation-corrected | 0 |
| TOC-vs-anchors | pass: every TOC entry (Foreword to Definitions, all three sections, all three instruments) is anchored in the body with page ranges that match the tape's footers |

## Changes

1. **Line 14, strip.** "It carries forward Volume 1's formula" → "It states the paradigm behind the tools". Volume 2 states R + M → ØE as "the human performance paradigm" (Foreword, p. i) without attributing it to Volume 1; the attribution came from knowing Vol. 1.
2. **Line 16, correct.** "The tools enhance, rather than replace, existing requirements" → "offered as example practices that can enhance the implementation of existing requirements, such as those supporting…". The Foreword says "may be used to enhance approaches" and "example practices that can enhance implementation of existing requirements" (pp. i–ii); "rather than replace" is not in it.
3. **Line 20 and Part VI "Active versus latent" bullet, citation.** Added (Foreword, p. i): "active" errors come from the Foreword; the Introduction (p. 1) speaks only of errors before they cause harm.
4. **Line 152 (Project Planning), correct.** "but not for core business or level-of-effort work" → "is not typically used for core business, programme or level-of-effort work, which administrative procedures guide". The source hedges with "not typically" and names "program" too (p. 58).
5. **Line 208 (Investigating Events), correct.** "Using Volume 1's Anatomy of an Event model" → "Using the Anatomy of an Event model as a guide". The tape (p. 88) names the model without tying it to Volume 1; nowhere in Vol. 2 links the two.
6. **Line 224 (Just Culture), correct.** "no tolerance… and broad confidence that" → "zero tolerance… and widespread confidence among managers that". The source names whose confidence it is (p. 96).
7. **Part VI skill-based bullet, strip and restructure.** Removed the label "slips and lapses at the point of action": neither word appears anywhere in the tape (grep count 0). The bullet also filed place-keeping, flagging, the Do Not Disturb sign, three-way communication and the phonetic alphabet under skill-based error, a mapping the source does not make (only the situational-awareness tools in general and self-checking are tied to skill mode, pp. 5, 18; flagging and the communication tools are never assigned a performance mode). Those five now sit in their own bullet, "Error targets named without a performance mode", with the same citations.
8. **Line 278 (Connections, Volume 1), strip.** Removed "and drawn on for the Anatomy of an Event model" and the p. 88 citation (same reason as change 5); citation for the companion relationship widened to Foreword, pp. i–ii.
9. **Line 10 and line 298, correct figures.** Word counts 36,491 / 33,023 can't be reproduced: `wc -w` gives 37,576 for the converted markdown and 34,106 for `pdftotext` (alphanumeric-token counts give 32,927 / 32,888, also not matching). Replaced with the `wc -w` figures and noted the method; words per page recomputed (about 275). Page count (137), file size (2,248,402 bytes) and SHA-256 (`ebe1e008…af53d4cc`) verified against the PDF.

## Considered and retained

- **Header item (3), Vol. 1 credits to Reason, Reason and Hobbs, Johnston and Dekker.** This is a cross-source statement, but it is a rights decision, explicitly sourced to Vol. 1 with chapter, page and endnote, and paired with the statement that Vol. 2 names no outside author. Spot-checked against the Vol. 1 tape: endnote 23 is Dekker's *Field Guide* (Vol. 1 line 7882); the Foresight and Substitution Tests sit at Vol. 1 pp. 4-24 to 4-25. Retained. The word "parallel" is the ingester's judgement; a cross-family auditor may reasonably flag it.
- **Integrity note "where Volume 1 writes 'Re + Mc → ØE'."** Verified in the Vol. 1 tape (line 1512). It explains the subscript rendering, not a claim about Vol. 2's content. Retained.
- **Positions the author explicitly frames against.** Each entry traces to an explicit at-risk practice or a direct statement (e.g. "cannot follow them blindly", p. 20; "most events occur during so-called 'routine' activities", p. 35). None is an invented opposition. Retained.
- **Decision Making "Where problem solving looks backward…".** Both halves are in the source (pp. 61, 63); the juxtaposition is mild and retained.

## Left open

- The sidecar `sources/original/doe-hpi-handbook-vol2.source.md` repeats the unreproducible 36,491 / 33,023 word counts. Not edited (outside this leg's remit).
- Cross-family leg pending; until it reports, treat this reference as audited but unverified.

## Derived-tier claims the parent should re-derive

Not edited here. These carry claims the corrected deep no longer supports:

- **Light ref `references/doe-hpi-handbook-vol2.md`, line 62:** "Skill-based slips and lapses: self-checking, place-keeping, flagging, the Do Not Disturb sign and communication tools" carries the stripped label and the unsupported mapping (change 7).
- **Light ref, line 74:** "cited for the culpability methods and the Anatomy of an Event" carries the stripped Vol. 1 → Anatomy link (changes 5, 8).
- **AAR distillation `distillations/aar/doe-hpi-handbook-vol2-aar.md`, lines 64, 86, 135:** frame errors as skill-based "slips" and file place-keeping and flagging under them (change 7). Line 14 already matches the corrected deep. Line 161's cross-reference table credits the Anatomy of an Event to Vol. 1. That is library-level synthesis and may be legitimate at the distillation tier if the Vol. 1 deep supports it, but it should not rest on the Vol. 2 deep.
- **Any derived artefact** that says the tools "enhance rather than replace" requirements (change 2), says Project Planning is never used for core business (change 4), or calls R + M → ØE Volume 1's formula as a Vol. 2 claim (change 1). A grep of the light ref and the three distillations found no occurrences, but the re-derivation should confirm.

The deep reference was not stamped; the driver stamps once both legs are done.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `66ba0ea9d3fd8e52a106a558747e4cd931917fa84989229006f769c32c98c7a8`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `44cbef6476496f50bc79da5b21ee3fa5e7e81a9103a0355cd3db7dc43c01548b`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_doe-hpi-handbook-vol2_crossfamily_blind.md`, `_ingest_pass_I_doe-hpi-handbook-vol2_crossfamily_sort.md`, `_ingest_pass_I_doe-hpi-handbook-vol2_crossfamily_prompts.md`.

**Sort result:** The sort counted 13 confirmed defect groups (4 confirmed and fixed, 2 fix incomplete, 7 missed by the fix-in-place audit), 0 over-flagged by the blind auditor, 0 over-flagged by the fixer, 1 disputed (B3), 0 new defects introduced, and a gate verdict of fail pending its fourteen remaining edits, pass once they are applied.

**Remaining edits applied (2026-10-06):** Of the fourteen remaining edits, six were applied as written (2, 3, 4, 8, 11, 13), eight with changed wording that follows the source more closely (1 adds the Foreword p. i basis for paraphrasing and cites p. 96 alone for the Volume I referral; 5 and 6 use 'the facility' and the defect definition's own phrasing; 7 uses the Introduction p. 2 referral with an [AP] anchor; 9 restores 'what has been accomplished'; 10 adds that the seven criteria need not be equally important; 12 also drops the 'In the converted text' qualifier, confirmed against PDF p. 14; 14 follows the source's 'launching ... before establishing' wording), and none was declined; disputed B3 was settled with the Introduction's own scope wording (tape lines 158-185).

**Gate:** accepted by operator. Deep reference sha256 `29455d641792a2d3feb957c290e37115412d33b646aecff8e6380e800198d7a4`, stamp included.

## Derived-tier fidelity check (2026-10-06)

The fidelity check of the derived tier for `doe-hpi-handbook-vol2` read the audited deep reference in full and read the light reference, the three distillations (aar, decision-making, retro) and the source's 27 index rows in full. Wording and anchors were checked against the converted tape where needed. About 427 claims and rows were checked and 27 fixed: 6 in the light reference, 7 in the AAR distillation, 7 in the decision-making distillation, 6 in the retro distillation and 1 index row. The fixes were of six kinds:

- A paraphrase-only page range that overstated the deep's set (pp. 85–99 for pp. 85–89 and 96–99), in all four files.
- Superlatives and corpus-scope comparisons in the distillation's own voice (3).
- Dropped hedges or narrowed scope put back (4).
- Wrong anchors or wrong-tool attributions (3).
- Changed quantities or counts (2).
- Claims the deep lacks, including a culpability-tree branch the deep says it cannot reconstruct and an invented causal link (about 8), plus small wording drifts toward the deep's terms.

No [V] quotation was wrong. `check-verbatim.py` reports no findings on every edited file. No defect was found in the deep reference.
