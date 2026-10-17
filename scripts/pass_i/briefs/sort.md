# Pass I, sort leg: ${title} deep reference

A deep reference (`frozen-deep.md`) was audited twice, independently:
- **Blind audit**: findings in `blind-findings.md`. It didn't edit anything.
- **Fix-in-place audit**: log in `fixer-audit-log.md`, result in `post-audit-deep.md` (sha256 in `post-audit-deep.sha256`).

${notes}
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
