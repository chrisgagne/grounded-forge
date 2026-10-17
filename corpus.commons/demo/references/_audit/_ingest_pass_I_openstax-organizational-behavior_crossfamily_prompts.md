# Second-leg prompts: openstax-organizational-behavior

## Blind leg

# Pass I, blind leg: Organizational Behavior deep reference

You are the second auditor for a deep reference written by another model. A fix-in-place auditor is working in parallel; you won't see its findings until later. Audit blind.

## Files (all in this folder)

- `frozen-deep.md`: the deep reference under audit, frozen before any edits (sha256 in `frozen-deep.sha256`).
- `tape.md`: the full converted source. Converted via: PyMuPDF 1.28.2 text blocks in content-stream order (page.get_text("blocks", sort=False)), one block per paragraph, pages split by form feed.
- `source.*` (if present): the original, for provenance checks (title, authors, date, version) and for any table, figure or chart whose values the tape can't carry cleanly.
- `source-card.md` (if present): the ingesting agent's sidecar. Audit its provenance claims too.
- `pass-i-spec.md`: the audit standard, including the fail conditions and the source-external framing list.
- `fixtures/`: three calibration exemplars. Read these before the deep reference.

**This is a scoped cross-family re-audit, not a first audit.** The deep reference has had same-family (Claude) Pass I audits only since its source was re-converted. Two rounds of new text are in scope; everything else in the deep reference is out of scope.

1. **Ch 12.7–12.9** (PR #23, 2026-10-15): text restored by hand to the old conversion, then written up in the deep reference, plus a full same-family Pass I of the whole deep reference that changed lines across the book.
2. **The 2026-10-16 re-conversion's restored text** (PR #42, 2026-10-17): about 21,700 words in 235 runs (mostly the opening of feature boxes: Exploring Managerial Careers, Managerial Leadership, Ethics in Practice, Cultural Intelligence, Catching the Entrepreneurial Spirit and others, plus some body text and tables), written up as new or extended deep-reference paragraphs, then a scoped same-family Pass I (13 edits).

**Tape in scope:** `scope-extract.md` in the packet folder (`_planning/pass-i/demo/openstax-organizational-behavior/`; the Codex legs' working folder) holds every in-scope tape range verbatim, 183 blocks, about 30,000 words, each headed with its `tape.md` line numbers. Read it in full, every block; where a block starts or ends inside a feature box or paragraph, read on in `tape.md` to the box's title and its end. For an in-scope deep-reference line whose passage is outside the extract (the PR #23 lines outside Ch 12), grep `tape.md` for the passage and read the whole paragraph or box around it. Don't read the rest of the tape.

**Deep-reference lines in scope** (numbering of `frozen-deep.md`, `post-audit-deep.md` and the deep reference as the legs find it, which is the same; the earlier audit log's line numbers are offset by one to three lines, so locate its findings by their text):
- Written or changed for the restored text (PR #42): 9 23 33 35 51 57 63 69 81 93 115 134 149 151 161 169 171 201 205 211 238 248 258 274 287 291 297 301 313 314 320 338 364 374 386 390 392 400 402 406 412 414 432 436 442 512 522 524 538 540 544 546 552 554 558 564 584 586 596 604 648 679 683 694 696 704 718 722 753 755 763 784 806 814 898.
- Written or changed by PR #23 (Ch 12.7–12.9 is lines 480–508; the rest are the full same-family Pass I's edits across the book): 15 17 41 103 109 187 193 199 217 269 278 286 328 334 342 348 352 384 450 480 482 484 486 488 490 492 494 496 498 500 502 504 506 508 532 580 672 700 708 710 782 846 856 860 861 877 883 885 888 904.
- Changed by the 2026-10-16 re-conversion's re-anchoring: 8 892 894 896.
Line 9 (Coverage) and lines 892–904 (integrity notes) are process statements: check their claims about the source (what was restored, what is excluded, footnotes, tables), not their audit-status wording, which the orchestrator rewrites after this run. Every other line is out of scope; read it only as context.

**Fix-in-place audit for this run:** `fixer-audit-log.md` is the whole audit log. Its section "Scoped re-audit 2026-10-17: restored feature boxes and body text" is the fix-in-place leg for the PR #42 lines; `frozen-deep.md` is the deep reference just before those 13 edits, so the blind leg sees the text that audit saw. The PR #23 lines' same-family audit (the 2026-10-15 sections above it) was applied before the freeze, so `frozen-deep.md` already carries its fixes there. The sort leg: sort the 2026-10-17 section's findings and every blind-audit finding; treat the 2026-10-15 sections as context only. For the `Capture:` line, count only confirmed defects in the PR #42 lines (the 2026-10-17 section against the blind audit's findings on those lines), and give the blind leg's confirmed defects in the PR #23 and re-anchoring lines on a separate line, `Blind-only (PR #23 lines): N`.

**Feature labels:** each box page in the PDF carries one ALL-CAPS feature label; the 2026-10-17 audit checked all 56 against a pdftotext dump. A box title that reads like another feature type (for example "Sustainability and Responsible Management: …" under MANAGERIAL LEADERSHIP) is not a label error. Check a label against the original only if the tape gives you a reason.

**Derived tier in scope (apply and fidelity legs):** claims in the light reference, the five distillations and this source's index rows that draw on an in-scope deep-reference line or on a line this run changes. Other derived claims are out of scope; leave them unless one contradicts an edit made here. Don't edit the deep reference's Coverage line, its integrity notes' audit-status wording, its stamp, or the coverage statements in the light reference, distillations and source card that name the single-family audit: the orchestrator rewrites those after the run.

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

# Pass I, sort leg: Organizational Behavior deep reference

A deep reference (`frozen-deep.md`) was audited twice, independently:
- **Blind audit**: findings in `blind-findings.md`. It didn't edit anything.
- **Fix-in-place audit**: log in `fixer-audit-log.md`, result in `post-audit-deep.md` (sha256 in `post-audit-deep.sha256`).


**This is a scoped cross-family re-audit, not a first audit.** The deep reference has had same-family (Claude) Pass I audits only since its source was re-converted. Two rounds of new text are in scope; everything else in the deep reference is out of scope.

1. **Ch 12.7–12.9** (PR #23, 2026-10-15): text restored by hand to the old conversion, then written up in the deep reference, plus a full same-family Pass I of the whole deep reference that changed lines across the book.
2. **The 2026-10-16 re-conversion's restored text** (PR #42, 2026-10-17): about 21,700 words in 235 runs (mostly the opening of feature boxes: Exploring Managerial Careers, Managerial Leadership, Ethics in Practice, Cultural Intelligence, Catching the Entrepreneurial Spirit and others, plus some body text and tables), written up as new or extended deep-reference paragraphs, then a scoped same-family Pass I (13 edits).

**Tape in scope:** `scope-extract.md` in the packet folder (`_planning/pass-i/demo/openstax-organizational-behavior/`; the Codex legs' working folder) holds every in-scope tape range verbatim, 183 blocks, about 30,000 words, each headed with its `tape.md` line numbers. Read it in full, every block; where a block starts or ends inside a feature box or paragraph, read on in `tape.md` to the box's title and its end. For an in-scope deep-reference line whose passage is outside the extract (the PR #23 lines outside Ch 12), grep `tape.md` for the passage and read the whole paragraph or box around it. Don't read the rest of the tape.

**Deep-reference lines in scope** (numbering of `frozen-deep.md`, `post-audit-deep.md` and the deep reference as the legs find it, which is the same; the earlier audit log's line numbers are offset by one to three lines, so locate its findings by their text):
- Written or changed for the restored text (PR #42): 9 23 33 35 51 57 63 69 81 93 115 134 149 151 161 169 171 201 205 211 238 248 258 274 287 291 297 301 313 314 320 338 364 374 386 390 392 400 402 406 412 414 432 436 442 512 522 524 538 540 544 546 552 554 558 564 584 586 596 604 648 679 683 694 696 704 718 722 753 755 763 784 806 814 898.
- Written or changed by PR #23 (Ch 12.7–12.9 is lines 480–508; the rest are the full same-family Pass I's edits across the book): 15 17 41 103 109 187 193 199 217 269 278 286 328 334 342 348 352 384 450 480 482 484 486 488 490 492 494 496 498 500 502 504 506 508 532 580 672 700 708 710 782 846 856 860 861 877 883 885 888 904.
- Changed by the 2026-10-16 re-conversion's re-anchoring: 8 892 894 896.
Line 9 (Coverage) and lines 892–904 (integrity notes) are process statements: check their claims about the source (what was restored, what is excluded, footnotes, tables), not their audit-status wording, which the orchestrator rewrites after this run. Every other line is out of scope; read it only as context.

**Fix-in-place audit for this run:** `fixer-audit-log.md` is the whole audit log. Its section "Scoped re-audit 2026-10-17: restored feature boxes and body text" is the fix-in-place leg for the PR #42 lines; `frozen-deep.md` is the deep reference just before those 13 edits, so the blind leg sees the text that audit saw. The PR #23 lines' same-family audit (the 2026-10-15 sections above it) was applied before the freeze, so `frozen-deep.md` already carries its fixes there. The sort leg: sort the 2026-10-17 section's findings and every blind-audit finding; treat the 2026-10-15 sections as context only. For the `Capture:` line, count only confirmed defects in the PR #42 lines (the 2026-10-17 section against the blind audit's findings on those lines), and give the blind leg's confirmed defects in the PR #23 and re-anchoring lines on a separate line, `Blind-only (PR #23 lines): N`.

**Feature labels:** each box page in the PDF carries one ALL-CAPS feature label; the 2026-10-17 audit checked all 56 against a pdftotext dump. A box title that reads like another feature type (for example "Sustainability and Responsible Management: …" under MANAGERIAL LEADERSHIP) is not a label error. Check a label against the original only if the tape gives you a reason.

**Derived tier in scope (apply and fidelity legs):** claims in the light reference, the five distillations and this source's index rows that draw on an in-scope deep-reference line or on a line this run changes. Other derived claims are out of scope; leave them unless one contradicts an edit made here. Don't edit the deep reference's Coverage line, its integrity notes' audit-status wording, its stamp, or the coverage statements in the light reference, distillations and source card that name the single-family audit: the orchestrator rewrites those after the run.

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
2. The sorted ledger, with the post-audit-deep line, the tape line or page, and who raised it (fixer, blind or both) for each.
3. **Remaining edits:** an exact, numbered list of changes still needed in `post-audit-deep.md`. Give the current text and the replacement, or "strip". Only include edits you've verified against the source.
4. Counts: confirmed, missed, over-flagged (by each auditor), disputed. End the section with one line in exactly this form, counting confirmed defects in the deep reference only:

   `Capture: fixer=N blind=N both=N`

   `fixer` is every confirmed defect the fix-in-place audit raised, whether or not its fix was right; `blind` is every one the blind audit raised; `both` is those both raised (the same defect in the same claim, however each worded it). Leave out disputed findings, defects outside the deep reference (source card, other files) and defects the fix-in-place edits introduced, which the blind audit never saw.
5. A gate verdict once the remaining edits are applied: pass, or fail with reasons.

Edit no file other than the report.
