# Second-leg prompts: aristotle-rhetoric

## Blind leg

# Pass I, blind leg: Rhetoric deep reference

You are the second auditor for a deep reference written by another model. A fix-in-place auditor is working in parallel; you won't see its findings until later. Audit blind.

## Files (all in this folder)

- `frozen-deep.md`: the deep reference under audit, frozen before any edits (sha256 in `frozen-deep.sha256`).
- `tape.md`: the full converted source. Converted via: manual: heading marks only.
- `source.*` (if present): the original, for provenance checks (title, authors, date, version) and for any table, figure or chart whose values the tape can't carry cleanly.
- `source-card.md` (if present): the ingesting agent's sidecar. Audit its provenance claims too.
- `pass-i-spec.md`: the audit standard, including the fail conditions and the source-external framing list.
- `fixtures/`: three calibration exemplars. Read these before the deep reference.

The ingested source is W. Rhys Roberts's published English translation of Aristotle's Rhetoric (Clarendon Press, 1924), as transcribed by The Internet Classics Archive. The tape is that English text with only `# Book N` / `## Part N` heading marks added; the original (`aristotle-rhetoric.txt`) is the same plain text, so there are no page renders to check.
Evidence-marker convention for this source: `[V]` marks Roberts's English exactly as the tape prints it. The protocol's rule that "a translation can never carry [V]" is about an ingester's own rendering of a non-English source; it does not apply here, because Roberts's translation is itself the source being ingested. Do not strip or downgrade a `[V]` for being a translation. Do check that every `[V]` quotation matches the tape character for character (run `scripts/check-verbatim.py`), and flag any wording that presents a quotation as Aristotle's Greek rather than Roberts's English.
The text is 68,240 words in 60 parts (Bk I Parts 1–15, Bk II Parts 1–26, Bk III Parts 1–19). Read the whole tape; if a leg cannot, it must say which line ranges it read. Citations are `(Bk N, Part M)`, with `line N` added for the numbered lines of argument in Bk II Part 23.
Typical defects to hunt: dropped hedges and qualifications (Aristotle hedges often: "as a rule", "for the most part", "in a sense"), conditions lost from a claim, comparatives made absolute, a line of argument or example credited to the wrong part, and interpretive framing from later rhetorical theory (ethos/pathos/logos as named labels, "the rhetorical triangle", "kairos", Bekker numbers) that the tape does not use. The tape uses "character", "emotions" and "the proof, or apparent proof" for the three modes.
Licence: public domain (published 1924; translator died 1929). The archive's closing notice claims copyright in its web presentation only.
For the derived-tier fidelity check: the two distillations end with an "Integration with Other References" section naming other demo sources (OpenStax Organizational Behavior, OpenStax Business Ethics, MCDP 1, NHS Just Culture, Liberating Structures, FLO). Check each claim those rows make about another source against that source's deep reference at `corpus.commons/demo/references/{slug}-deep.md`; narrow or remove any row its deep reference does not support.

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

# Pass I, sort leg: Rhetoric deep reference

A deep reference (`frozen-deep.md`) was audited twice, independently:
- **Blind audit**: findings in `blind-findings.md`. It didn't edit anything.
- **Fix-in-place audit**: log in `fixer-audit-log.md`, result in `post-audit-deep.md` (sha256 in `post-audit-deep.sha256`).


The ingested source is W. Rhys Roberts's published English translation of Aristotle's Rhetoric (Clarendon Press, 1924), as transcribed by The Internet Classics Archive. The tape is that English text with only `# Book N` / `## Part N` heading marks added; the original (`aristotle-rhetoric.txt`) is the same plain text, so there are no page renders to check.
Evidence-marker convention for this source: `[V]` marks Roberts's English exactly as the tape prints it. The protocol's rule that "a translation can never carry [V]" is about an ingester's own rendering of a non-English source; it does not apply here, because Roberts's translation is itself the source being ingested. Do not strip or downgrade a `[V]` for being a translation. Do check that every `[V]` quotation matches the tape character for character (run `scripts/check-verbatim.py`), and flag any wording that presents a quotation as Aristotle's Greek rather than Roberts's English.
The text is 68,240 words in 60 parts (Bk I Parts 1–15, Bk II Parts 1–26, Bk III Parts 1–19). Read the whole tape; if a leg cannot, it must say which line ranges it read. Citations are `(Bk N, Part M)`, with `line N` added for the numbered lines of argument in Bk II Part 23.
Typical defects to hunt: dropped hedges and qualifications (Aristotle hedges often: "as a rule", "for the most part", "in a sense"), conditions lost from a claim, comparatives made absolute, a line of argument or example credited to the wrong part, and interpretive framing from later rhetorical theory (ethos/pathos/logos as named labels, "the rhetorical triangle", "kairos", Bekker numbers) that the tape does not use. The tape uses "character", "emotions" and "the proof, or apparent proof" for the three modes.
Licence: public domain (published 1924; translator died 1929). The archive's closing notice claims copyright in its web presentation only.
For the derived-tier fidelity check: the two distillations end with an "Integration with Other References" section naming other demo sources (OpenStax Organizational Behavior, OpenStax Business Ethics, MCDP 1, NHS Just Culture, Liberating Structures, FLO). Check each claim those rows make about another source against that source's deep reference at `corpus.commons/demo/references/{slug}-deep.md`; narrow or remove any row its deep reference does not support.

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
