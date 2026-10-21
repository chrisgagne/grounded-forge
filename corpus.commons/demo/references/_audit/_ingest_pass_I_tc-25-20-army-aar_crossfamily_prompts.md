# Second-leg prompts: tc-25-20-army-aar

## Blind leg

# Pass I, blind leg: A Leader's Guide to After-Action Reviews deep reference

You are the second auditor for a deep reference written by another model. A fix-in-place auditor is working in parallel; you won't see its findings until later. Audit blind.

## Files (all in this folder)

- `frozen-deep.md`: the deep reference under audit, frozen before any edits (sha256 in `frozen-deep.sha256`).
- `tape.md`: the full converted source. Converted via: PyMuPDF 1.28.2 text blocks in content-stream order (page.get_text("blocks", sort=False)), one block per paragraph, pages split by form feed.
- `source.*` (if present): the original, for provenance checks (title, authors, date, version) and for any table, figure or chart whose values the tape can't carry cleanly.
- `source-card.md` (if present): the ingesting agent's sidecar. Audit its provenance claims too.
- `pass-i-spec.md`: the audit standard, including the fail conditions and the source-external framing list.
- `fixtures/`: three calibration exemplars. Read these before the deep reference.

**This is a scoped re-audit, not a first audit.** The deep reference passed Pass I on 2026-05-13 against an earlier conversion that had dropped the text of Figures 1-1 to 1-4. The source was re-converted on 2026-10-16, and Passes C–E were then re-run for the restored text only. Audit only the restored material and the deep-reference text written for it; everything else in the deep reference is unchanged since its 2026-05-13 audit and is out of scope.

- **Tape range to read in full:** lines 100–345 of the tape (Ch 1 from "Definition and Purpose" through Figure 1-4 "The AAR Process", into the opening of Ch 2). The restored text is tape lines 166–329: Figure 1-1 (AAR Key Points), Figure 1-2 (AAR Format), Figure 1-3 (Types of AARs), Figure 1-4 (The AAR Process) and the NOTE lines introducing them. Also read tape lines 760–800 (Figure 4-1) and 885–897 (Figure 4-2), which the new text cross-refers to. Don't read the rest of the tape.
- **Deep-reference text in scope:** the Coverage line (line 9); the last sentence of thesis paragraph 3 (line 17) and the Figure 1-4 sentence in thesis paragraph 4 (line 19); Part I "Formal versus informal AARs" from "Three figures accompany this section" through the Figure 1-3 table and the sentence after it (lines 44–58); Part I "Four-step AAR process" from "Chapters 2 through 5 detail" through "The Planning and Preparation items follow the order of the section headings in Chapters 2 and 3" (lines 70–78); the "C2" spelling in Part IV technique 2 (line 178); the two new rows "Key points in all AARs" and "Items in the AAR format" in the Key planning targets table; and the first paragraph of "Citation and source-integrity notes". Check the claim at lines 77–78 against the Ch 2 and Ch 3 section headings (grep the tape for the ALL-CAPS headings).
- The figures' bullets are drawn glyphs, so the tape gives each list item as a bare line; a [V] quotation that joins the items with spaces is verbatim. Figure 1-4's "integrate into tutors training plans" is as printed in the PDF (PDF p. 8, already checked against a render); don't flag it as a conversion error.
- **Derived tier in scope:** the light reference's new Figure 1-1 to 1-4 paragraphs, its thesis Figure 1-4 clause and its two new table rows; in `distillations/aar/tc-25-20-army-aar-aar.md` concepts 2, 3, 16 and 17, the Phase 0 row "Is the plan complete?", the Phase 5 row "Has the result reached the assessment?" and the "When to Use" first bullet; in `distillations/retro/tc-25-20-army-aar-retro.md` concept 13 and the Phase 1 row "Have we said what was supposed to happen?"; and the new TC 25-20 rows in `AAR-DISTILLATION-INDEX.md` (Phase 0, "Check the plan and the run against the TC's checklists") and `RETRO-DISTILLATION-INDEX.md` (Phase 1, "Walk the AAR's three questions in order").
- **Audit log:** the log file already holds the 2026-05-13 audit. Keep it: append a new section headed "## Scoped re-audit 2026-10-16: restored Figures 1-1 to 1-4" rather than overwriting the file.

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

# Pass I, sort leg: A Leader's Guide to After-Action Reviews deep reference

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
