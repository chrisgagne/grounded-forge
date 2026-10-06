# Pass I source audit: caib-report-vol1 (fix-in-place leg)

- **Date:** 2026-10-06
- **Auditor:** claude-opus-5-5, fresh subagent, fix-in-place mode. A blind cross-family leg (codex) runs separately on a frozen copy; this log was written without seeing it.
- **Deep reference:** `references/caib-report-vol1-deep.md` (355 lines, read in full)
- **Source:** `sources/converted/caib-report-vol1.md` (25,038 lines, pdftotext 26.08.0). **Read in full**, lines 1–25,038, in consecutive chunks. The last chunk (Appendix C staff lists, lines 23,751–25,038) was read with blank lines dropped.
- **Original:** `sources/ingest/caib-report-vol1.pdf` (250 pages, 156,874,175 bytes; gitignored)
- **Calibration:** protocol Pass I section and failure-mode reference read; fixtures 01, 07 and 12 read.
- **Stamp:** not set, as the dispatch instructed (the driver stamps once every leg is done).

## Counts

| | |
|---|---|
| Claims audited | about 575 (518 inline markers: 238 `[V]`, 105 `[AP]`, 14 `[AR]`, 131 `[AE]`, 30 `[BT]`; plus 17 key-statistics rows, 9 connections, 9 positions, and the header and integrity-note claims) |
| Source-anchored as written | about 540 |
| Claims corrected to the source | 21 |
| Source-external framing stripped | 2 phrases (no whole claims stripped) |
| Citations corrected (page) | 6 |
| Marker corrections | 0 |
| Quotation corrections | 0. `check-verbatim.py` reported no findings before or after the edits. |
| Header and integrity notes updated | 6 |
| Page renders used | 3 of 10 (PDF pp. 172, 203, 204), at 110 dpi |

## Verbatim check

`python3 scripts/check-verbatim.py references/caib-report-vol1-deep.md` gave "no findings" before the audit and again after all edits. The operator's tesseract second OCR (2026-10-06) already confirms every `[V]` quotation. Per the dispatch, no renders were spent on quotations.

## Changes, by line in the edited file

### Claims corrected to the source

1. **L39, Part Two opener.** "A nuclear physicist's description of high-risk technology as a bargain": the source names Alvin Weinberg, quoted through a National Research Council report on nuclear wastes, and never calls him a physicist (Part Two, p. 97, tape l. 9692). This is training-data leakage. Fixed: Weinberg is named and the NRC route given. His quoted phrase is paraphrased, following the header's third-party rule.
2. **L55, Ch 2.** "More than 70 scientists' experiments" changed to "research involved more than 70 scientists" (Ch 2, p. 27).
3. **L65, Ch 2.** "More than 2,000 square miles in Texas and Louisiana" changed to "in Texas alone exceeded 2,000 square miles". "Up to 25,000 people" changed to "more than 25,000" (Ch 2, pp. 45, 47).
4. **L69, Ch 3 sidebar.** The "kitchen-table experiment" was invented. The Osheroff sidebar describes an experiment on the loading dock of the Stanford Physics Department, with a graduate student. Its result is also restated: the pressure opened a planar crack perpendicular to the surface and did not eject foam, so the old summary "showed how hydrostatic pressure cracks the foam" overstated it. The sidebar sits on p. 54 only (Ch 3, p. 54).
5. **L77, Ch 3.5.** The object "departed ... during manoeuvres" overstated the source, which says only that it is *possible* an attitude manoeuvre imparted the departure velocity (Ch 3, p. 63). Hedged.
6. **L79, Ch 3.6.** "Reconstructs a breach of about ten inches" was wrong. The source uses a 10-inch hole as an *example* in a thermal analysis and says "the exact size of the breach will never be known" (Ch 3, p. 66). Corrected.
7. **L87, Ch 4, bolt catchers.** The Board's attribution ("inadequate oversight and confusion over the requirement") is about the X-ray weld-inspection lapse, not the "analysis and similarity" qualification. The claim now names the lapse it attributes (Ch 4, p. 87).
8. **L87, Ch 4.** A "1999 hydraulic spill" was in fact a hydrazine (hypergolic fuel) spill (Ch 4, p. 90).
9. **L87, Ch 4.** "Two Michoud closeouts were done by a single person" changed to "can be performed by a single person" (F4.2-13, Ch 4, p. 94).
10. **L87, Ch 4.** The "more than 3,000 elements" fault-tree figure comes from the Synopsis (p. 12), not Chapter 4. Chapter 4's table totals about 1,560 elements and says the Board closed "more than one thousand items". The citation is now attributed.
11. **L101, Ch 5.** "NASA's top safety official objected ... and resigned" was wrong. The man who resigned, Bryan O'Connor, was the head of the Space Shuttle Program at Headquarters. He only *later* (2002) became Associate Administrator for Safety and Mission Assurance (Ch 5, p. 107). This is identity conflation, probably prior knowledge; corrected.
12. **L121, Ch 6 sidebar.** "A sample bias" changed to "probably a sample bias", restoring the Board's hedge (Ch 6, p. 123).
13. **L127, Ch 6, STS-27R.** "Damaged 707 tiles and nearly burned through" was wrong. The source counts 707 *dings*, a single tile knocked off, and says a burn-through "may have occurred" but for an aluminium plate. The crew inspected with a camera on the arm (Ch 6, p. 127).
14. **L145, Ch 6.3.** "The co-chairs classified the strike as out of family" was wrong. The source says the USA deputy manager of Shuttle Engineering "signaled that the debris strike was initially classified as 'out-of-family'", on p. 143, not p. 142.
15. **L149, Ch 6.3.** "She and the programme manager called the STS-113 rationale poor" was wrong. Only Ham called it so ("lousy"), in an e-mail to Dittemore; Dittemore's reply says only that it "is worth looking at again" (Ch 6, pp. 147–148).
16. **L151, Ch 6.3.** The path of the second imagery request was wrong. It went from Bob White (United Space Alliance) to Lambert Austin (Shuttle Systems Integration, Johnson), who phoned the DoD Manned Space Flight Support Office. The Kennedy manager (Hale) belongs to request 1 (Ch 6, p. 150; sidebar p. 166).
17. **L157, Ch 6.3.** "Its second meeting met the phrase with shrugs" was wrong: the shrugs were members' later answers when *the Board* asked what "mandatory need" meant (Ch 6, p. 157).
18. **L157, Ch 6.3.** "No alternate trajectory was considered" was wrong. Engineers *noted that no alternate re-entry trajectory could substantially reduce heating* (Ch 6, p. 160).
19. **L159, Ch 6.3.** "Five scenarios, all concerning tile" overstated the source, which says the briefing "focused primarily on potential damage to the tiles" (Ch 6, p. 160).
20. **L159, Ch 6.3.** The claim that the Langley and Ames engineers "circulated their results widely" inverted the source. The favourable results went to a wider Johnson audience, the unfavourable one only to management and selected engineers, and neither the engineer nor his managers told the MMT. The engineers were from Langley and Johnson; Ames was the simulator site (Ch 6, p. 164).
21. **L286, App A.** "Rewrote its charter in its first week" changed to: proposed a rewritten charter in the first week, signed on 18 February (App A, p. 232).

### Source-external framing stripped

- **L182.** The charter statement was "quoted in full because it is the report's organising claim". That is the ingester's evaluation; it now reads "boxed at the head of Chapter 7".
- **L223.** "The mechanism is stated precisely" was an evaluative label; it now reads "sets out the mechanism step by step".

### Citations corrected

- L69: the testing paragraph, (Ch 3, p. 53) to (Ch 3, pp. 52–53).
- L83: R3.8-1 and R3.8-2, (Ch 3, p. 84) to (Ch 3, p. 83).
- L117: the 0.006 ft-lb requirement, (Ch 6, p. 121) to (Ch 6, pp. 121–122).
- L135: "every bit of padding" (p. 138), (Ch 6, pp. 135–137) to (Ch 6, pp. 135–138).
- L145: p. 142 to p. 143 (with item 14).
- L276: the paperwork-review sentence, cited (Ch 10, p. 221), now (Ch 10, pp. 220–221).

### Added from page images

- **L172.** The findings F6.3-9 to F6.3-17 lose their numbers in the tape. A render of PDF p. 172 (printed p. 171) recovers them, and the paraphrased findings now carry F6.3-5, -6, -8, -10, -11, -13, -14, -16 and -17.

### Header and integrity notes

- **L8, OCR caveat.** "No second OCR ... was possible" was stale. It now records the operator's tesseract second OCR.
- **L10, citation style.** "Equals the PDF page index" was misleading. Renders show PDF page = printed page + 1, because the PDF opens with an unnumbered cover; the form-feed count equals the printed page. Clarified.
- **L343, conversion.** "Is not in the repository" now reads: not committed (over GitHub's limit); the local copy sits, gitignored, at `sources/ingest/`.
- **L347, reading order.** The p. 202 contractor-dependence reassembly and the p. 203 "Twice in NASA history" sentence are both confirmed against renders of PDF pp. 203–204. The p. 203 split is caused by the interleaved left-column paragraph, not by a column boundary; the wording is corrected.
- **L347, F-numbers.** The note now says the lost F6.3 numbers were recovered from the p. 171 render.
- **L349.** The "No second OCR" paragraph is replaced by "Second OCR", recording the operator's result as briefed.

## Checked and left as written (selected)

- **Ch 8, p. 202 contractor dependence (L240).** The render confirms the producer's reassembly: the left column ends "the decision process was also affected", and the right column opens "by NASA's dependence on the contractor". The paraphrase stands.
- **Source inconsistencies (L353).** All seven were confirmed in the tape at the cited pages. Fishback against Fischbeck and "January 23" are the report's own, per the operator's OCR.
- **Connections and Positions.** Every entry traces to a passage, an endnote or an appendix: Turner (Ch 8, n. 1), Weick (n. 47), Starbuck and Milliken (n. 4), McCurdy (Ch 5, n. 12; Ch 8, nn. 15, 32), HRT and NAT authors (Ch 7 endnotes), Vaughan as a Group II researcher (App C, p. 244). No invented oppositions: each position is one the Board explicitly argues against.
- **Key statistics.** All 17 rows trace.
- **L75.** "Imagery ... of the wing underside on orbit" is kept: R3.4-3 asks NASA to "obtain and downlink" the images, which implies in flight.

## Derived tier (not edited; parent re-derives)

Light reference `references/caib-report-vol1.md`, L20 ("Other factors"):

- "single-person closeouts". The deep now says two closeout processes *can be* performed by one person (F4.2-13). The light wording reads as a lapse that occurred; check it.
- "A 3,000-element fault tree ... (Ch 4, pp. 85–95)". The 3,000 figure is the Synopsis's (p. 12); add that citation.

Distillations (`aar`, `decision-making`, `retro`): grepped for every changed claim (Weinberg, O'Connor, Osheroff, STS-27R, the imagery-request path, shrugs, alternate trajectory, Langley/Ames, the breach size, hydrazine, Michoud, square miles, charter). **No hits.** None carries a changed claim.

## Open

- **Cross-family leg.** It is pending. Until it is sorted against this log, this audit stands as audited-but-unverified.
- **PDF page offset (+1).** It affects anyone mapping the operator's "PDF p. N" notes to printed pages. The operator's "PDF p. 178" ("year"/"years") is printed p. 177, consistent with the deep's L182 citation (Ch 7, p. 177).


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `9242329b5fdf2e6dec7723dbe50458ce3df787db32111fb5b7bdd522914d7961`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `71f023bf18578560455744c9d2f7e5e69f50c65e63fdd42e175a0168c67d12b3`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_caib-report-vol1_crossfamily_blind.md`, `_ingest_pass_I_caib-report-vol1_crossfamily_sort.md`, `_ingest_pass_I_caib-report-vol1_crossfamily_prompts.md`.

**Sort result:** The sort confirmed 57 distinct defects (26 fixed by the fix-in-place audit, 2 fixed incompletely, 29 missed), found 1 over-flag by the blind auditor and 3 by the fixer, left 2 findings disputed (F2, S1), and gave the gate as fail pending 31 edit groups, pass once they are applied.

**Remaining edits applied (2026-10-06):** Of the 31 remaining edit groups, 13 were applied as written, 18 with changed wording and none declined; the substantive wording changes were edit 12 (kept F4.2-13's present tense "can be performed" and its plain "close-out processes"), edit 20 (kept p. 128 for the STS-35 and STS-42 table rows and moved only the STS-56/58 and STS-87 cites to p. 129), edit 25 (follows the source's "ground personnel failed to ask" Brown), and edit 31 (keeps the STS-173 caption as a source-internal oddity: the number appears nowhere else in the report), with the rest tightened to the source's words (render of printed p. 139 confirmed edit 22's conclusion reading).

**Gate:** accepted by operator. Deep reference sha256 `8cd7d1373dc709e78ea4e6ad94d386c93d9ffe43c1e22354b765e7f24db6ee24`, stamp included.

## Derived-tier fidelity check (2026-10-06)

The derived tier of `caib-report-vol1` was checked against its audited deep reference, with the converted tape opened to confirm wording and anchors. Files checked: the light reference, the AAR, decision-making and retro distillations, and the source's 27 rows across the three distillation indexes. About 417 claims and rows were checked; 27 narrow edits were made, a few of them fixing more than one defect in the same sentence. Light reference: 7. AAR: 11. Decision-making: 6. Retro: 2. Retro index: 1. Five kinds of fix were made. (1) Dropped hedges restored: the Board's "may well have subtly influenced" on schedule pressure and decisions, "may" on marginal voices, and NASA's "challenging but feasible" rescue study. (2) Widened scope or added claims cut back: "only the imagery could have settled it", "until no one sees the total", "mission goals", "before every flight", "are warnings", and practices credited to all three benchmark organisations. (3) Changed quantities and wording corrected: "much" to "most", "accepted" to "acceptable". (4) Attribution and markers corrected: the White House and Congress, not a deadline, put NASA on probation; a recommended In-Flight Anomaly assigned as an action; the rescue study credited to NASA; Tufte's slide analysis re-marked `[BT]`; two missing `[V]` markers added; one Ch 7 anchor added. (5) Distillation-voice text fixed: corpus-scope superlatives removed from the AAR and retro relevance sections, and interpretive labels marked as application. Every edited file passes `scripts/check-verbatim.py`. Index column counts match their headers, and every cross-referenced slug exists. No defect was found in the deep reference.
