# Second-leg prompts: barbrook-johnson-systems-mapping

## Blind leg

# Pass I, blind leg: Systems Mapping: How to build and use causal models of systems deep reference

You are the second auditor for a deep reference written by another model. A fix-in-place auditor is working in parallel; you won't see its findings until later. Audit blind.

## Files (all in this folder)

- `frozen-deep.md`: the deep reference under audit, frozen before any edits (sha256 in `frozen-deep.sha256`).
- `tape.md`: the full converted source. Converted via: PyMuPDF 1.28.2 text blocks in content-stream order (page.get_text("blocks", sort=False)), one block per paragraph, pages split by form feed.
- `source.*` (if present): the original, for provenance checks (title, authors, date, version) and for any table, figure or chart whose values the tape can't carry cleanly.
- `source-card.md` (if present): the ingesting agent's sidecar. Audit its provenance claims too.
- `pass-i-spec.md`: the audit standard, including the fail conditions and the source-external framing list.
- `fixtures/`: three calibration exemplars. Read these before the deep reference.

**This is a scoped re-audit, not a first audit.** The deep reference passed Pass I against an earlier conversion that had dropped the bodies of Tables 1.2, 5.1 and 11.1–11.3 and the text labels of Figs 1.3, 3.2, 6.1 and 6.3. The source was re-converted on 2026-10-16, and Passes C–E were then run for the restored material only. Audit only that material and the deep-reference text written for it. Everything else in the deep reference is unchanged since its earlier audit and is out of scope.

- **Tape ranges to read in full** (about 2,300 of the tape's 9,853 lines): 1050–1110 (Fig 1.3), 1160–1560 (Table 1.2 and the text around it), 2395–2550 (Fig 3.2), 3660–3870 (Table 5.1), 4590–4840 (Figs 6.1–6.3), 8150–9300 (Ch 11, Tables 11.1–11.3). To check a quotation that starts or ends outside these ranges, grep the tape. Don't read the rest of the tape.
- **Deep-reference text in scope:** every line added or changed since the earlier audit (`git diff origin/main -- <deep>` from the repo root if you can). That is: the Coverage line; the Fig 1.3 bullet in Part I; the Table 1.2 table and the paragraph after it ("Methods deliberately excluded"); the Fig 3.2 sentences in the Theory of Change section; the Table 5.1 table in the PSM section; the Fig 6.1 and Fig 6.3 sentences in the FCM section; Tables 11.1, 11.2 and 11.3 and the sentences around them in "Comparing, choosing, and combining methods"; the three new rows at the end of "Key cross-method statistics and facts"; and the "Conversion path" integrity note.
- **Tables:** the tape gives table cells one fragment per line, in reading order, with no column markup. Quoted cells join those fragments with spaces. The column alignment of Tables 11.1–11.3 and the Fig 1.3 placements were read from renders of PDF pp. 26, 177, 183 and 186. Fig 1.3's placements are [AP] for that reason. check-verbatim reports three `near` findings where a slash ends a line ("templates/ inspiration", "feedbacks/ dynamical", "system/ situation"). The quotations are verbatim; this is a checker limitation.
- **Derived tier in scope:** the light reference's additions (the excluded-methods list, Fig 1.3, Table 5.1, the Tables 11.1–11.3 paragraph); aar concept 9 and the "principled place to start" row; retro's submap row and the new "Two candidate experiments" row; software-business concept 19 and the two new Phase 1 rows; and the source card's coverage sentence.
- **Audit log:** append a new section headed "## Scoped re-audit 2026-10-16: restored tables and figure labels"; don't overwrite the earlier audit.

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

# Pass I, sort leg: Systems Mapping: How to build and use causal models of systems deep reference

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
