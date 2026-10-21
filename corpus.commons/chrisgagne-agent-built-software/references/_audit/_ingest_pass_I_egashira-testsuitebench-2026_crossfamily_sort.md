## 1. What I read

Read in full:

- `sort-brief.md`, `pass-i-spec.md` and all three calibration fixtures.
- `blind-findings.md`, `fixer-audit-log.md` and `blind-brief.md`.
- `post-audit-deep.md`: all 341 lines.
- `tape.md`: all 2,860 lines, including references, appendices, eight prompts and Table 7.
- Repository `CLAUDE.md` and its nine listed architecture documents.
- The acquisition manifest and producer receipt found elsewhere in the repository.

Compared both fixer edits against `frozen-deep.md`. The post-audit reference’s SHA-256 matches `post-audit-deep.sha256`.

Although the audit folder contains no original, the repository contains :codex-file-citation{path="corpus.commons/chrisgagne-agent-built-software/sources/ingest/egashira-testsuitebench-2026.pdf" purpose="source"}. I inspected its metadata and deterministic layout extraction of pages 5–8 and 24–25. Both its SHA-256 and the tape’s SHA-256 match the acquisition manifest. The PDF’s rights metadata explicitly identifies CC BY 4.0.

This report is the output. No files were edited.

## 2. Sorted ledger

Line numbers refer to the unchanged `post-audit-deep.md`.

| Finding | Raised by | Post-audit line(s) | Tape line(s) or original evidence | Disposition |
|---|---|---:|---|---|
| F1: Table 2 caption presented as literal caption wording without quotation marks, under `[AP]` | Fixer | 158 | Tape 433–434; PDF p. 6 | **Confirmed and fixed.** “Reads:” introduces copied caption wording; lowercasing its opening word does not make it a substantive paraphrase. The fixer correctly restored the capital, quotation marks and `[V]`. |
| F2: DeepSeek citation incorrectly grouped with system/model cards | Fixer | 316 | Tape 865–867; 859, 879–882, 928–932; citation sites 223, 423–425, 1418–1420 | **Confirmed and fixed.** DeepSeek’s cited work is an arXiv preprint. The replacement accurately distinguishes it from the other cited publications and correctly adds the construction-model citation. |
| B1: Abstract credited with naming “Validity Score” | Blind | 140, 337 | Abstract: tape 17–35; Figure 1: 70–74; metric definition: 398–402 | **Missed by the fix-in-place audit.** Neither occurrence was corrected. The abstract contains no metric name; Figure 1 supplies “Validity Score”. These are two defective attribution occurrences. |
| B2: Generic rule-based mutation framed broadly as an opposed measure of test-suite strength | Blind | 324 | Tape 58–61 | **Missed by the fix-in-place audit.** The source objects specifically to these mutations’ inability to guarantee requirement-specific faults. The bullet’s label broadens that into opposition to their use as a strength measure. Its explanatory sentence preserves the narrower claim, but does not repair the broader label. |
| B3: Thesis blockquote collapses source line breaks | Blind | 43 | Tape 93–95 | **Missed by the fix-in-place audit under the explicit literal-match requirement.** Author wording is correct; two internal newlines are replaced by spaces. This is a formatting defect, not a changed substantive claim. |
| B4: “Valid but weak tests” blockquote collapses source line breaks | Blind | 179 | Tape 494–496 | **Missed by the fix-in-place audit under the same literal-match requirement.** Author wording and punctuation are correct; two internal newlines are replaced by spaces. |
| B5: Licence and open scope lack supporting provenance | Blind; fixer also left licence verification open | 5–6 | No declaration in tape; original PDF XMP `dc:rights` identifies `http://creativecommons.org/licenses/by/4.0/` | **Over-flagged as a remaining defect by the blind auditor.** Its packet limitation was real, but the original now verifies the stated licence and supports `Scope: open`. The fixer’s open item is resolved. |
| B6: Converter identity/version and conversion attribution unsupported | Blind | 33, 329, 333 | Acquisition manifest: `converted_via`, `pages`, `words`; matching tape hash; tape 336–383, 433–470, 632–699; PDF pp. 5–8, 24–25 | **Over-flagged by the blind auditor.** The manifest records markitdown 0.1.5 and 25 pages. The producer receipt records the conversion and layout checks. Comparing the tape with the original confirms the disrupted column alignment. |
| B7: PDF/tape agreement with acquisition-manifest hashes unsupported | Blind; fixer left PDF verification open | 329 | Independently calculated PDF and tape SHA-256 values both match the acquisition manifest | **Over-flagged as a remaining defect by the blind auditor.** The historical integrity assertion is substantiated. The fixer’s PDF open item is resolved. |
| B8: PDF layout checks and figure-inspection provenance unavailable | Blind; fixer left layout verification open | 133, 169, 246, 333, 335 | Producer receipt; repeated layout extraction of PDF pp. 5–8 and 24–25; tape 336–383, 431, 433–470, 593–615, 632–699, 2164–2860 | **Over-flagged as a remaining defect by the blind auditor.** The receipt documents the checks, and repeating them confirms the tables and Figure 4 values. Table 7’s tape loses row alignment; layout text preserves it. Line 335 assigns image inspection to the orchestrator; it does not claim that inspection occurred. |

The four provenance findings accurately described what the blind auditor could not verify from its supplied packet. They do not establish defects once the repository’s original and acquisition records are checked.

The mutation-opposition finding is confirmed despite the fixer’s explicit decision to retain the bullet: the source names a bounded construction difficulty, whereas the label generalises the objection. Narrowing the label preserves everything the source says.

**Confirmed, fix wrong or incomplete:** none.

**Disputed findings:** none. The blockquote findings are resolved by the blind brief’s explicit character-for-character rule; ordinary whitespace-normalised quotation checking would permit their existing presentation.

**Defects introduced by fixer edits:** none. Both changed passages trace to the tape. The new inline caption quotation is a contiguous excerpt; omitting its terminal full stop does not create an internal omission or change its meaning.

The key-statistics table matches the tape. The four limitations bullets preserve the authors’ stated limitations. No missing source section, unsupported cross-author connection or task-application guidance was found.

## 3. Remaining edits

Only these five verified changes are needed. Line numbers below precede any insertion of quotation line breaks.

1. **Line 140 — replace the second sentence.**

   Current:

   > The abstract and Figure 1 call it the Validity Score (Abstract; Figure 1 caption) [AP].

   Replacement:

   > Figure 1 calls it the Validity Score (Figure 1 caption) [AP].

   Evidence: tape 17–35 and 70–74.

2. **Line 337 — replace the metric-naming sentence.**

   Current:

   > It calls V both "Validity Rate" (§2.6, App. C) and "Validity Score" (Abstract, Figure 1).

   Replacement:

   > It calls V both "Validity Rate" (§2.6, App. C) and "Validity Score" (Figure 1).

   Evidence: tape 70–74, 398–402 and 1449–1452.

3. **Line 324 — replace the entire bullet.**

   Current:

   > - *Generic rule-based mutation as a measure of test-suite strength.* The authors require faults that violate specific requirements, which such mutations cannot guarantee (§1, "Introduction").

   Replacement:

   > - *Generic rule-based mutations as a guarantee of requirement-specific faults.* The authors say that measuring a suite's strength requires faults violating specific requirements, which generic rule-based mutations cannot guarantee (§1, "Introduction").

   Evidence: tape 58–61.

4. **Line 43 — preserve the thesis quotation’s internal source line breaks.**

   Current:

   ```markdown
   > "These results reveal a critical gap: agents can build software they cannot verify. Until they can turn specifications into strong test suites, fully autonomous development of new software remains out of reach" (§1, "Introduction") [V]
   ```

   Replacement:

   ```markdown
   > "These results reveal a critical gap: agents can build software they cannot verify. Until they can turn
   > specifications into strong test suites, fully autonomous development of new software remains out of
   > reach" (§1, "Introduction") [V]
   ```

   Evidence: tape 93–95. The endpoint before the semicolon remains a valid contiguous excerpt.

5. **Line 179 — preserve the second blockquote’s internal source line breaks.**

   Current:

   ```markdown
   > "While the models are capable of writing valid tests, giving the impression of well tested software, they fail to write discriminative tests that would actually surface specification violations." (§3.1, "Valid but Weak Tests") [V]
   ```

   Replacement:

   ```markdown
   > "While the models
   > are capable of writing valid tests, giving the impression of well tested software, they fail to write
   > discriminative tests that would actually surface specification violations." (§3.1, "Valid but Weak Tests") [V]
   ```

   Evidence: tape 494–496.

No provenance replacement or strip is needed.

## 4. Counts

Confirmed defects are counted by affected claim occurrence. B1 affects two separate attribution claims; each other confirmed finding affects one passage.

| Category | Count |
|---|---:|
| Confirmed defects | 7, across 6 ledger findings |
| Confirmed and fixed | 2 |
| Confirmed, fix wrong or incomplete | 0 |
| Missed by fixer and still present | 5, across 4 blind findings |
| Over-flagged by fixer | 0 |
| Over-flagged by blind | 4 provenance finding groups |
| Disputed | 0 |
| Defects introduced by fixer edits | 0 |

The capture counts include the two literal-formatting defects required by the blind brief. No provenance finding, outside-file defect or newly introduced defect is included.

Capture: fixer=2 blind=5 both=0

## 5. Gate verdict

**Pass once the five remaining edits are applied.**

The corrected reference will have complete tape coverage, source-supported claims and markers, and verified acquisition provenance. The driver must then record the completed audit and apply its stamp; the existing “Audit pending” line should remain until that happens.