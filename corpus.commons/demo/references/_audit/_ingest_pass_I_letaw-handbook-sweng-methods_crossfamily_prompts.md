# Second-leg prompts: letaw-handbook-sweng-methods

## Blind leg

# Pass I, blind leg: Handbook of Software Engineering Methods deep reference

You are the second auditor for a deep reference written by another model. A fix-in-place auditor is working in parallel; you won't see its findings until later. Audit blind.

## Files (all in this folder)

- `frozen-deep.md`: the deep reference under audit, frozen before any edits (sha256 in `frozen-deep.sha256`).
- `tape.md`: the full converted source. Converted via: PyMuPDF 1.28.2 text blocks in content-stream order (page.get_text("blocks", sort=False)), one block per paragraph, pages split by form feed.
- `source.*` (if present): the original, for provenance checks (title, authors, date, version) and for any table, figure or chart whose values the tape can't carry cleanly.
- `source-card.md` (if present): the ingesting agent's sidecar. Audit its provenance claims too.
- `pass-i-spec.md`: the audit standard, including the fail conditions and the source-external framing list.
- `fixtures/`: three calibration exemplars. Read these before the deep reference.

**This is a scoped re-audit, not a first audit.** The deep reference passed Pass I against an earlier conversion that had dropped the text of framed callout and example boxes (about 1,560 words). The source was re-converted on 2026-10-16, and Passes C–E were then run for that text only. Audit only the restored text and the deep-reference text written for it. Everything else is unchanged since the earlier audit and is out of scope. **Don't read the whole tape or the whole deep reference.**

- **Tape ranges to read in full** (about 1,100 of the tape's 4,516 lines; the restored boxes with context): 244–266, 482–516, 528–560, 656–676, 744–766, 846–870, 892–912, 987–1011, 1216–1240, 1362–1386, 1576–1596, 1665–1773, 1831–1877, 1947–1971, 2056–2076, 2132–2156, 2246–2270, 2360–2380, 2440–2470, 2791–2811, 2828–2848, 2868–3075, 3129–3153, 3205–3229, 3245–3269, 3296–3334, 3363–3383, 3454–3503, 3532–3552, 3761–3782, 4328–4348, 4449–4469. Grep the tape for anything else you need to check.
- **Deep-reference text in scope:** read only the lines added or changed since the earlier audit (`git diff origin/main -- <deep>` from the repo root). These are the Coverage line; the new "Why care: the CHAOS findings" subsection; the Manifesto sentence in "Agile and the Manifesto"; the callout sentences added in Part II (scope and quality, ground rules, gestures, story-point scales), Part III (quality attributes, the user-story format and Figure 3.3, Figure 3.4's three criteria and the Glossary's given-when-then, Figure 3.2's use case, SRS vs SDD), Part IV (the epigraph, the IDE-generated diagrams callout, the diagram-audience callout), Part V (dumb pipes, library vs service), Part VII (the "Design recommendation" sentence after each of the eight heuristics, and the two GenderMag pointers) and Part VIII (the resources callout, the two comment callouts, the three function callouts, the three general-code callouts); the new CHAOS row in "Key statistics"; and the first integrity-note paragraph.
- The CHAOS callout's figures are the callout's own; the existing "17%–22%" row comes from body text and is out of scope.
- **Derived tier in scope:** the light reference's additions (Manifesto and CHAOS sentence, the requirements worked examples, the heuristic recommendations sentence, the new CHAOS row); software-business concept 16's added Definition-of-Done sentence; the source card's coverage sentence; and the removal of the PARTIAL notes from the five distillations.
- **Audit log:** append a section headed "## Scoped re-audit 2026-10-16: restored callouts"; don't overwrite the earlier audit.

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

# Pass I, sort leg: Handbook of Software Engineering Methods deep reference

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
