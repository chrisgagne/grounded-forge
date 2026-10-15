## 1. What I read

Read in full: `sort-brief.md`; all three calibration fixtures; `pass-i-spec.md`; `blind-findings.md`; `fixer-audit-log.md`; and `post-audit-deep.md`, lines 1–451.

Also read the repository operating instructions and architecture documents, `source-card.md`, the original versions of both edited passages and the audit-status line in `frozen-deep.md`, and these source passages:

- `tape.md` lines 539–758: LLM02, including regulatory applicability and obligations.
- Lines 1125–1175: poisoning stages and their surrounding explanation.
- Lines 1785–1835, 1880–1930: embedding risks and controls, including GDPR notification.

This was a sort of the reported findings and fixer edits, not a new full-source audit. No PDF images were needed for these textual findings.

The post-audit SHA-256 matches `post-audit-deep.sha256`: `10fddc5dae62761caf8e77cf8a0ebe1b50e2c7a543d92db9e9d69c4d56d16566`. The complete frozen-to-post diff contains exactly the two logged edits. The verbatim checker, run against `tape.md`, reports no findings.

No files were changed.

## 2. Sorted ledger

| Finding | Raised by | Post-audit line | Source anchor | Disposition |
|---|---|---:|---|---|
| Pointer to a nonexistent Pass I stamp on line 2 | **Both**: blind finding 1; fixer “Left open” | 449 | Artefact-level evidence: line 2 is blank; no stamp appears in the reference. `pass-i-spec.md` requires logging before stamping. No tape passage applies. | **Confirmed, fix incomplete.** The pointer remains inaccurate. The fixer recognised the defect but deferred it; this is not a blind-only miss. |
| “Stored vectors steering retrieved content toward steered answers” | **Fixer** change 2 | 209 | Tape 1145–1155, especially 1150–1151; p. 33 | **Disputed.** The fixer’s reading: the compression obscures poisoning’s role and becomes circular. Alternative reading: within a paragraph explicitly about poisoning, the phrase describes compromised vectors influencing retrieval and answers; its awkwardness does not establish a changed substantive claim. The replacement accurately follows the tape and can remain. |
| `[BT]` on the regulatory-regimes connection | **Fixer** change 1 | 409 | Tape 573–574, 582–583, 703–717, 1819–1820 and 1914–1918; pp. 18–19, 21, 51, 53 | **Disputed.** The fixer’s reading: applicability is the document’s own assertion, so `[AP]` or an unmarked catalogue is more precise than borrowed-through. Alternative reading: the named instruments and articles supply external authority for the reported obligations, making `[BT]` defensible. The taxonomy does not explicitly resolve this treatment of legal and standards references. |

**Confirmed and fixed:** none unequivocally established. The poisoning replacement is source-faithful, but whether its predecessor constituted a defect remains disputed.

**Missed by the fix-in-place audit:** none. The only blind finding was also explicitly raised by the fixer.

**Over-flagged:** none conclusively established; the two contested fixer findings are recorded as disputed.

**New defect introduced by the fixer:** line 409’s added assertion, **“not cited as sources for claims”**, is too categorical. The source expressly connects erasure obligations to GDPR Article 17 and CCPA §1798.105 (tape 573–574), notification to GDPR Article 33 (712–713; 1917–1918), and serious-incident obligations to EU AI Act Article 73 (703–706). Whether these warrant `[BT]` is debatable; denying their use as authority for claims goes beyond what the tape supports. This introduced defect is excluded from capture counts.

## 3. Remaining edits

1. **Line 449 — strip the entire line.**

   Current:
   ```markdown
   **Pass I: see the stamp on line 2 and the audit log.**
   ```

   Replacement: **strip**.

   A subsequent driver stamp should record the actual completed audit and log location without relying on a prospective line number.

2. **Line 409 — remove the categorical denial.**

   Current:
   ```markdown
   - Regulatory regimes named as applicable, not cited as sources for claims: EU AI Act (Regulation (EU) 2024/1689, Article 73), GDPR (Articles 17 and 33), HIPAA, CCPA/CPRA (§1798.105), ISO/IEC 42001 (LLM02, pp. 18–22; LLM09, pp. 51, 53).
   ```

   Replacement:
   ```markdown
   - Regulatory regimes named as applicable: EU AI Act (Regulation (EU) 2024/1689, Article 73), GDPR (Articles 17 and 33), HIPAA, CCPA/CPRA (§1798.105), ISO/IEC 42001 (LLM02, pp. 18–22; LLM09, pp. 51, 53).
   ```

   This preserves the verified connection without requiring a ruling on the disputed original marker.

## 4. Counts

| Category | Count |
|---|---:|
| Confirmed original defects | 1 |
| Confirmed and fixed | 0 |
| Confirmed, fix wrong or incomplete | 1 |
| Blind-only defects missed by fixer | 0 |
| Over-flagged — fixer | 0 |
| Over-flagged — blind | 0 |
| Disputed | 2 |
| Confirmed defects introduced by fixer, counted separately | 1 |

The fixer’s explicit acknowledgement of line 449 counts as raising it, despite leaving it unchanged. Disputed findings and the introduced defect are excluded below.

Capture: fixer=1 blind=1 both=1

## 5. Gate verdict

**Pass once the two remaining edits are applied**, within the declared operator-approved text-only scope.

The driver must then complete the actual audit stamp and the protocol’s required derived-tier re-derivation and provenance stamping. This report does not certify those subsequent operations as completed.