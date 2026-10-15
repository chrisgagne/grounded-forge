## 1. What I read

Read in full: `sort-brief.md`, all three calibration fixtures, `pass-i-spec.md`, `blind-findings.md`, `fixer-audit-log.md`, and all 251 lines of `post-audit-deep.md`. Also read the repository’s `CLAUDE.md` and its nine required architecture documents.

Compared `frozen-deep.md` with `post-audit-deep.md`: the only edits are at lines 90 and 202. Checked both edits and every reported defect against the relevant tape passages. Checked the frozen and post-audit artefacts for the claimed stamp. The post-audit SHA-256 matches `post-audit-deep.sha256`.

This was a sort of the two audits, with targeted source verification, rather than a third full-source audit. No files were edited.

## 2. Sorted ledger

Line numbers below refer to `post-audit-deep.md`; they also match the frozen reference.

| Finding | Raised by | Classification | Source check and disposition |
|---|---|---|---|
| **Line 90: author commentary presented as developer testimony.** The frozen wording joins “Developers say…” to the quotation beginning “Sometimes, portions…”, implying continued developer attribution. | Fixer | **Confirmed and fixed** | Tape **1061–1073**, App. C.1.2, **p. 19**: the developer quotations have explicit boundaries; the sentence at **1068–1069** is the authors’ intervening commentary. Introducing it with “The authors add:” correctly restores attribution. The added `[AE]` on the preceding developer-evidence paraphrase is supported. |
| **Line 202: row heading restricts the population to AI-allowed recordings while the row also reports AI-disallowed recordings.** | Fixer | **Confirmed and fixed** | Tape **1408–1413**, App. C.3.2, **p. 26**, distinguishes **44 AI-allowed** recordings from **54 AI-disallowed** recordings. The original values already distinguished the conditions, so this was a heading-scope defect, not a numerical error. “AI use in labelled recordings” correctly covers both populations; the added denominator of 44 is source-supported. |
| **Line 207: omitted uncertainty about similarity to training data.** | Blind | **Missed by the fix-in-place audit** | Tape **106–109**, §1.1, **p. 3**, says the task is **likely** to resemble substantial LLM training data and **may** unfairly advantage AI. “Criticised as … close to training data” retains attribution but strengthens the proposition being attributed. The post-audit reference still needs the qualifier restored. |
| **Line 251: reference to a nonexistent stamp on line 2.** | **Both**: blind finding 2; fixer’s “Left open” | **Missed by the fix-in-place audit — repair deferred** | **No tape passage applies:** this is an artefact-provenance defect. Line **2 is blank** in both supplied references, and neither contains the referenced Pass I stamp. Anticipated driver stamping does not make the current cross-reference valid. The fixer noticed this but left it unresolved. |

For the last entry, “missed” follows the brief’s definition of a blind finding that remains unfixed. It was a **repair omission**, not a detection omission, by the fixer.

**Confirmed, fix wrong or incomplete:** no attempted correction falls into this category. Both actual edits are correct.

**Over-flagged:** none.

**Disputed:** none.

**Ancillary source-only observation:** the fixer correctly identifies the paper’s erroneous cross-reference in footnote 5: tape **207**, **p. 5**, points to C.3.4, while the block-randomisation sensitivity result appears at **1793–1801**, App. E.3, **p. 33**. Deep-reference lines **144 and 201** already cite E.3 correctly. This is a source defect, requires no deep-reference edit, and is excluded from capture counts.

**Defects introduced by the fixer:** none found. Both changed passages preserve the source’s wording, quantities and distinctions.

## 3. Remaining edits

1. **Line 207 — restore the source’s uncertainty.**

   Current text:

   ```text
   with Peng et al.'s task criticised as unrepresentative and close to training data
   ```

   Replacement:

   ```text
   with Peng et al.'s task criticised as unrepresentative and likely to be similar to a large amount of LLM training data, which may unfairly advantage AI systems relative to humans
   ```

   Verified against tape **106–109**, §1.1, **p. 3**. Preserve the existing `[BT]` marker and citations.

2. **Line 251 — strip the unsupported audit cross-reference.**

   Current text:

   ```text
   Pass I: see the stamp on line 2 and the audit log.
   ```

   **Strip.** Preserve the rest of the paragraph. The supplied artefact has no stamp on line 2; do not replace this sentence with an assertion that stamping has occurred.

## 4. Counts

Counts use distinct defects, merging the two auditors’ observations about the same stamp cross-reference.

| Measure | Count |
|---|---:|
| Confirmed deep-reference defects | **4** |
| Confirmed and correctly fixed | **2** |
| Attempted fixes wrong or incomplete | **0** |
| Blind findings remaining unfixed | **2** |
| Of those: overlooked by fixer / explicitly deferred | **1 / 1** |
| Over-flagged — fixer | **0** |
| Over-flagged — blind | **0** |
| Disputed | **0** |
| New defects introduced by fixer | **0** |

The fixer receives capture credit for the stamp defect because its log explicitly raises it, despite deferring repair. The source’s footnote error is excluded.

Capture: fixer=3 blind=2 both=1

## 5. Gate verdict

**Pass once the two remaining edits are applied.** Both fixer edits are supported, and all confirmed deep-reference findings will then be resolved.

This verdict does not assert that final stamping or derived-tier re-derivation and provenance checks have been performed. Those remain the driver’s responsibilities under `pass-i-spec.md`.