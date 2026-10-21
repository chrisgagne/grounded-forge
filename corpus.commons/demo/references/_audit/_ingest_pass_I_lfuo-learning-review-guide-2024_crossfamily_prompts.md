# Second-leg prompts: lfuo-learning-review-guide-2024

## Blind leg

# Pass I, blind leg: Learning From Unintended Outcomes and Learning Review Implementation Guide deep reference

You are the second auditor for a deep reference written by another model. A fix-in-place auditor is working in parallel; you won't see its findings until later. Audit blind.

## Files (all in this folder)

- `frozen-deep.md`: the deep reference under audit, frozen before any edits (sha256 in `frozen-deep.sha256`).
- `tape.md`: the full converted source. Converted via: PyMuPDF 1.28.2 text blocks in content-stream order (page.get_text("blocks", sort=False)), one block per paragraph, pages split by form feed.
- `source.*` (if present): the original, for provenance checks (title, authors, date, version) and for any table, figure or chart whose values the tape can't carry cleanly.
- `source-card.md` (if present): the ingesting agent's sidecar. Audit its provenance claims too.
- `pass-i-spec.md`: the audit standard, including the fail conditions and the source-external framing list.
- `fixtures/`: three calibration exemplars. Read these before the deep reference.

**This is a scoped re-audit, not a first audit.** The deep reference passed Pass I on 2026-05-13 against an earlier conversion that had dropped about 11% of the PDF's longer lines (sidebars, pull quotes, boxes, worksheets, interview guides). The source was re-converted on 2026-10-16, and Passes C–E were then run for the restored text only. Audit only the restored material and the deep-reference text written for it. Everything else in the deep reference is unchanged since its 2026-05-13 audit and is out of scope.

- **Tape ranges to read in full** (the restored spans with about 12 lines of context; 2,814 of the tape's 5,358 lines): 8–78, 353–407, 421–511, 539–614, 633–699, 776–856, 886–945, 973–1009, 1042–1085, 1093–1249, 1314–1376, 1467–1498, 1507–1590, 1671–1703, 1733–1785, 1802–1826, 1854–1909, 1937–1977, 1991–2020, 2039–2075, 2106–2174, 2200–2235, 2265–2300, 2330–2363, 2415–2446, 2474–2628, 2636–2673, 2705–2740, 2771–2796, 2909–2937, 2943–3005, 3074–3117, 3167–3203, 3273–3358, 3401–3425, 3432–3456, 3593–3617, 3903–3927, 4025–4146 (Appendix D in full), 4195–4224, 4221–4400 (Appendices G and H in full), 4413–4873, 4895–5038 (Handout E in full), 5066–5106, 5185–5227. To check a quoted sentence that starts or ends outside these ranges, grep the tape. Don't read the rest of the tape.
- **Deep-reference text in scope:** every line added or changed since the 2026-05-13 audit. Diff the deep reference against git `origin/main` if you can (`git diff origin/main -- <deep>`). Otherwise it is: the Coverage and Citation style lines (8–9); the new "Front matter: epigraphs" section; the additions in Part I (Just Culture sidebars and the Dekker box, organisational-learning pull quotes, the "How we got here" opening and Tidwell quote); Part II (Leader's Intent for an FLA, the "conditions" box); Part III (the GAP sidebar, Wenatchee, accident-investigation requirements, the Dekker and Fire Operations RMC pull quotes, Elkhorn 2) and the new "The FLA process at a glance (Part 4)" subsection; Part IV (the elephant-in-the-room box, NTDP and data sidebars, the assurance limit, the "Open, Frequent Communication" paragraph, the basic-to-complex transition box, Gregg Creek); Part V (Isaacs pull quote, Little Venus, interview tips, No Signed Witness Statements, FEAR THE FUSION, the three boxed items after Sand Tables); Part VI (NAFRI quote, the Five Hows graphic paragraph that replaced a "not yet read" note, Leader's Intent for a Complex FLA); Part VII (Meadow Creek, the RMC "optimal employees" quote); Part VIII (Readbacks, Ziegler, the cause box, the privacy box); Part IX (the completed third LR question, "administer pause", the LR outline graphic); Part X (the Handout C list that replaced a "did not extract" note; Handout D's six AAR-type questions and the completed fifth HRO question); Part XI (PARADIGM CHECK POINT); Part XII (Davies Creek caption); the new Parts XIII–XVII (Appendix D, Appendix F, Appendices G and H, Handout B, Handout E); the Glossary pull quote; the thesis's last paragraph; the additions to "Connections" and "Positions"; and the two rewritten integrity-note paragraphs.
- **Image-held text:** three of Handout C's five boxes (confirmation, outcome and hindsight bias, PDF pp. 87–88) and all of Appendix F (PDF pp. 77–78) are not in the tape. The deep reference describes them as [AP] from a tesseract OCR, and the OCR text is in this folder as `ocr-pdf-p77.txt`, `ocr-pdf-p78.txt`, `ocr-pdf-p87.txt` and `ocr-pdf-p88.txt`. Check those [AP] claims against the OCR and, where needed, a render. The Part 4 graphic (PDF p. 22), the Five Hows graphic (p. 46) and the LR outline (p. 59) give their labels in drawing order in the tape; their order in the deep reference comes from renders.
- **Known check-verbatim noise, already hand-checked:** quotations that run past a box at the foot of a page report `missing` or `page` (Part 1 "Just Culture" restorative-justice sentence; Part 5 "Forming the FLA team"; Part 9 "Serious Crimes"); "ergonomic7," is a glued footnote marker; "101- 37" is a digit hyphen split across a line. "institutioned", "happed", "it about" and "administer pause" are as printed.
- **Derived tier in scope:** the light reference's additions; in the aar distillation concepts 7 and 15–20 and the new question and signal rows; in the retro distillation concepts 4 and 10–13, the new rows and the rewritten worked-example sentence and evidence note; in the software-business distillation concepts 7, 15 and 16 and the new 5b and 5d rows; in the stakeholder distillation the Appendix F sentences (concept 6, the "Who has been harmed" row); the new LFUO rows in AAR-DISTILLATION-INDEX.md and RETRO-DISTILLATION-INDEX.md and the edited row in STAKEHOLDER-ENGAGEMENT-DISTILLATION-INDEX.md.
- **Audit log:** the log file already holds the 2026-05-13 audit. Keep it: append a new section headed "## Scoped re-audit 2026-10-16: restored text" rather than overwriting the file.

## Task

Read the three fixtures, then `pass-i-spec.md`, then `frozen-deep.md` cold. Trace every claim (prose, table cell, evidence marker, blockquote, cross-reference, thesis paragraph, statistics row, "positions the author frames against", source-integrity notes) to a passage in `tape.md` or the original.

Report every defect:
- a claim with no source passage;
- a wrong evidence marker (`[V]` without exact verbatim text, `[AP]` without author content, and so on);
- a blockquote that doesn't match the tape character for character, other than smart-quote normalisation (say which);
- a changed quantity, sample size, sign, significance level or dropped qualifier (for an empirical source, check every number in the deep reference against the tape);
- a finding stated more broadly than the source's setting supports;
- a section of the source missing from the coverage;
- a cross-reference to an author or work the source doesn't cite;
- task-application guidance in the deep tier;
- post-source vocabulary;
- source-external analytical framing (evaluative labels, plausibility judgements, methodological verdicts, invented oppositions, causal explanation the source doesn't give).

The test is "which passage says it?", not "is it true?".

Also say whether the deep reference's key-statistics table (if any) matches the tape, and whether its list of the source's limitations matches what the authors themselves state.

## Output

1. What you read in full and in part.
2. Findings, numbered. For each: the deep reference line, the problem class, the evidence (tape line or page), and the exact fix: the replacement text, or "strip".
3. A count: claims checked, defects by class.
4. Over-flag guard: list anything you considered flagging but judged clean, with the reason. Over-flagging is as costly as missing a defect.

Edit no file other than the report.


## Sort leg

# Pass I, sort leg: Learning From Unintended Outcomes and Learning Review Implementation Guide deep reference

A deep reference (`frozen-deep.md`) was audited twice, independently:
- **Blind audit**: findings in `blind-findings.md`. It didn't edit anything.
- **Fix-in-place audit**: log in `fixer-audit-log.md`, result in `post-audit-deep.md` (sha256 in `post-audit-deep.sha256`).

The source is `tape.md`, with the original (`source.*`, if present) for provenance and for any table, figure or chart. The audit standard is `pass-i-spec.md`, and `fixtures/` holds three calibration exemplars.

Read the fixtures and `pass-i-spec.md`, then both audits, then `post-audit-deep.md` in full. Check each finding against the tape yourself; neither audit is authoritative. Sort every finding from both audits into:
- **Confirmed and fixed:** a real defect, correctly fixed in the post-audit deep.
- **Confirmed, fix wrong or incomplete.**
- **Missed by the fix-in-place audit:** a blind-audit finding not fixed in the post-audit deep and still a defect.
- **Over-flagged:** doesn't hold against the source. Say whose.
- **Disputed:** a genuine judgement call; give both readings.

Also check whether any fix-in-place edit introduced a new defect.

## Output

1. What you read.
2. The sorted ledger, with the post-audit-deep line and tape line or page for each.
3. **Remaining edits:** an exact, numbered list of changes still needed in `post-audit-deep.md`. Give the current text and the replacement, or "strip". Only include edits you've verified against the source.
4. Counts: confirmed, missed, over-flagged (by each auditor), disputed.
5. A gate verdict once the remaining edits are applied: pass, or fail with reasons.

Edit no file other than the report.
