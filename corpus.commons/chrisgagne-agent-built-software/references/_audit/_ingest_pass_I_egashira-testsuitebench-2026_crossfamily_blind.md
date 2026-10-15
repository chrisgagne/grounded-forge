## 1. What I read

Read in full:

- `blind-brief.md`.
- All three calibration fixtures, before the cold read.
- `pass-i-spec.md`.
- `frozen-deep.md`, all 341 lines.
- `tape.md`, all 2,860 lines and 13,308 words, including references, all appendices, all eight prompts and Table 7.
- `frozen-deep.sha256`, repository `CLAUDE.md` and its listed architecture documents.

The frozen reference’s SHA-256 matches the supplied digest: `dcbb789ee1829356bc3867e65a2da99f804897138047c46b0fc7a44140811e9e`.

No original `source.*`, source card, acquisition manifest, PDF layout extraction or figure images were supplied. Consequently, this is a complete **tape-based audit**, with original-document provenance checks unresolved. I did not read the parallel auditor’s findings.

The repository verbatim checker reported **zero findings**. Findings 3–4 below concern the brief’s stricter requirement of character-for-character blockquote matching, rather than changed author wording.

No files were edited. This message is the report; filesystem access is read-only.

## 2. Findings

### 1. The abstract is incorrectly credited with naming the validity metric

**Deep lines:** 140 and 337.  
**Class:** Incorrect source attribution.

**Problem:** Both lines say the abstract calls the metric “Validity Score”. The abstract reports that suites are largely valid and 88% of tests pass, but never uses “Validity Score”, “Validity Rate” or the symbol V.

**Evidence:** Tape lines 17–35, versus Figure 1’s explicit “Validity Score V” at lines 70–74 and §2.6’s “Validity Rate (V)” at lines 398–402.

**Exact fixes:**

At line 140, replace the second sentence with:

> Figure 1 calls it the Validity Score (Figure 1 caption) [AP].

At line 337, replace the corresponding sentence with:

> It calls V both “Validity Rate” (§2.6, App. C) and “Validity Score” (Figure 1).

### 2. A narrowly stated objection becomes a broader opposition

**Deep line:** 324.  
**Class:** Source-external analytical framing; broadened opposition.

**Problem:** Under “Positions the author explicitly frames against”, the label presents generic rule-based mutation itself as an opposed measure of test-suite strength. The source’s objection is narrower: such mutations cannot guarantee faults violating specific requirements. It does not reject their use as a strength measure generally.

**Evidence:** Tape lines 58–61.

**Exact replacement:**

> - *Generic rule-based mutations as a guarantee of requirement-specific faults.* The authors say that measuring a suite’s strength requires faults violating specific requirements, which generic rule-based mutations cannot guarantee (§1, “Introduction”).

### 3. The thesis blockquote reflows the tape’s line breaks

**Deep line:** 43.  
**Class:** Literal blockquote mismatch — formatting only.

**Problem:** The words match, but the quotation collapses two source line breaks. This passes the repository checker’s whitespace normalisation but does not match the tape character for character under the blind brief’s stated exception of smart-quote normalisation only.

**Evidence:** Tape lines 93–95.

**Exact replacement, preserving the tape’s internal line breaks:**

```markdown
> "These results reveal a critical gap: agents can build software they cannot verify. Until they can turn
> specifications into strong test suites, fully autonomous development of new software remains out of
> reach" (§1, "Introduction") [V]
```

The quotation ends before the source’s semicolon and continuation. That endpoint is a contiguous excerpt, not an unmarked internal omission.

### 4. The “valid but weak tests” blockquote also reflows line breaks

**Deep line:** 179.  
**Class:** Literal blockquote mismatch — formatting only.

**Problem:** The author wording and final full stop match. Two internal source line breaks have been collapsed.

**Evidence:** Tape lines 494–496.

**Exact replacement:**

```markdown
> "While the models
> are capable of writing valid tests, giving the impression of well tested software, they fail to write
> discriminative tests that would actually surface specification violations." (§3.1, "Valid but Weak Tests") [V]
```

Findings 3–4 are exclusively formatting discrepancies. There is no changed wording or evidence-class error.

### 5. The licence claim lacks supporting provenance in the supplied packet

**Deep lines:** 5–6.  
**Class:** Unverified provenance; unresolved distribution-scope basis.

**Problem:** “Licence: CC BY 4.0” cannot be traced to the tape. The linked Creative Commons page identifies a licence, but does not establish that this paper carries it. The accompanying `Scope: open` therefore cannot be independently certified from the supplied materials.

**Evidence:** No licence declaration occurs anywhere in tape lines 1–2860. The front matter establishes title, authors, affiliations, links and arXiv version/date, but not licence.

**Exact replacement for the licence sentence:**

> Licence: not verified from the supplied tape; the original licence declaration was not supplied.

The `Scope: open` declaration requires acquisition evidence before certification. **Do not infer a different licence or scope merely from the missing evidence.**

This is an unresolved provenance claim, not a finding that CC BY 4.0 is false.

### 6. Converter identity and version are asserted without supporting records

**Deep lines:** 33, 329 and 333.  
**Class:** Unverified conversion provenance.

**Problem:** The tape shows extraction artefacts, but does not identify the converter or its version. The packet does not substantiate “markitdown 0.1.5” or attribute the displaced table columns and footer positions specifically to markitdown.

**Evidence:** Tape’s displaced table columns at lines 336–383, 433–470 and 632–699; no converter declaration anywhere in the tape.

**Exact fixes:**

At line 33, replace the final sentence with:

> Rationale: the tape preserves section numbers and run-in headings; page numbers appear as bare footer digits around extracted figures and tables.

At line 329, replace:

> markitdown 0.1.5 from the 25-page arXiv PDF

with:

> converter and version not independently verified in this audit

At line 333, replace the opening sentence with:

> The tape separates or interleaves columns in Tables 1, 2, 3, 6 and 7.

### 7. Acquisition-manifest hash verification cannot be substantiated

**Deep line:** 329, final sentence.  
**Class:** Unverified integrity provenance.

**Problem:** Neither the PDF nor acquisition manifest is supplied. The frozen-reference digest does not establish the claimed PDF/tape agreement with that manifest.

**Evidence:** No manifest or original PDF is present. `frozen-deep.sha256` concerns the deep reference alone.

**Exact replacement:**

> Agreement of the original PDF and converted tape with the acquisition manifest was not independently verified in this audit; neither the PDF nor manifest was supplied.

This finding does not establish that the claimed historical verification failed.

### 8. Claimed PDF/layout checks are unavailable for independent verification

**Deep lines:** 133, 169, 246 and 333; image-inspection statement at 335.  
**Class:** Unverified original-document inspection provenance.

**Problem:** The reference claims checks against `pdftotext -layout`, including alignment of tables and Figure 4. That extraction and the PDF are absent. Likewise, no image files are supplied for the stated orchestrator inspection. The statement that Table 7’s rows are readable **only** from layout text is not demonstrated by this packet.

**Evidence:** Tape carries the relevant values at lines 336–383, 431, 433–470, 593–615, 632–699 and 2164–2860. No original or layout extraction is supplied.

**Exact fixes:**

Line 133:

> Source: Table 1 in the supplied tape [AE]. The reported PDF layout check was not independently verified in this audit.

Line 169:

> Source: Table 2 in the supplied tape [AE]. The reported PDF layout check was not independently verified in this audit.

At line 246, replace the table-introduction sentence with:

> Table 6 records the following values (Table 6) [AE]:

Replace line 333 with:

> **Tables.** The tape separates or interleaves columns in Tables 1, 2, 3, 6 and 7. The reference’s reported PDF layout checks could not be independently verified because neither the original PDF nor layout extraction was supplied. This reference cites Table 7 for its captioned scope of all 165 instances, rather than individual repository rows.

Replace line 335’s final sentence with:

> Figure image inspection was unavailable in this blind audit; no image files were supplied.

These are provenance gaps. The reconstructed table values themselves match the tape.

## 3. Counts and required determinations

**Claims checked:** All **189 evidence-marked claim groups**: 19 `[V]`, 62 `[AP]`, 20 `[AR]`, 74 `[AE]` and 14 `[BT]`. Independently checked all **184 data/label cells across 51 table rows**, all six unmarked opposition bullets, the structural inventory, cross-references and source-integrity statements. The cell count overlaps the marked groups; these are not 373 distinct atomic claims.

| Finding class | Count |
|---|---:|
| Incorrect source attribution | 1 finding, two occurrences |
| Broadened/source-external opposition | 1 |
| Literal blockquote formatting mismatch | 2 |
| Unverified provenance groups | 4 |
| Changed numerical values, signs or thresholds | 0 |
| Evidence-marker classification errors | 0 |
| Missing source sections | 0 |
| Uncited-author/work cross-references | 0 |
| Task-application guidance | 0 |
| Post-source vocabulary | 0 |

**Key-statistics table:** All **28 rows match the tape**, including quantities, denominators, directions, model identities and qualifications. The other four reconstructed tables also match the recoverable tape columns.

**Authors’ limitations:** The four limitation bullets match §5, tape lines 788–818. They preserve untargeted requirement gaps, exact-input mutant risks, uncertain correspondence to real-world faults, unusually detailed specifications and possible performance overestimation, inherited implementation bugs/incidental behaviour, and the compiled command-line scope.

**Coverage:** No missing section or appendix was found. The reference covers §1–§6, both disclosure statements, related-work connections, A.1–A.6, B.1–B.3, Appendix C, all eight Appendix D prompts and Appendix E’s catalogue scope.

**Disposition:** Two substantive corrections, two literal-formatting corrections under the brief’s strict wording, and four unresolved provenance groups. This blind leg does not issue an unconditional Pass I certification.

## 4. Over-flag guard

- **“Surprising”, “modest gains”, “reasonable proxy”, logarithmic cost relationship and Pareto frontier:** Clean. These evaluations are the authors’ own, at tape lines 489–502, 803–804 and 1019–1020.
- **Test design as the bottleneck:** Clean as attributed author argument. The source explicitly states it at lines 88–91 and 826–828. The reference also identifies the executable ablation as Sol-only.
- **88% validity and 82% implementation pass rate:** Clean. Both appear in the abstract, lines 30–34. They need not equal any individual model’s result.
- **55.5% versus 54% for Opus:** Clean. Table 2/main results report 55.5%; the pooled-mutant overlap analysis separately reports 6,584/12,130, rounded to 54%. The reference preserves both source reports.
- **73%/0.2% versus 73.0%/0.17%:** Clean. The abstract rounds the construction results reported more precisely in §2.2.
- **Language percentages summing to 101%:** Clean. Figure 4 supplies those rounded percentages; counts sum to 165.
- **Six target tests versus at most six:** Clean. The reference preserves both §2.2’s description and Appendix B.2’s capacity constraint.
- **Internet-access filtering at test versus repository level:** Clean. The source itself uses both descriptions, and line 337 records the distinction.
- **`build.sh` versus `compile.sh`, and misplaced metric cross-references:** Clean. These discrepancies belong to the source and are accurately recorded.
- **Prompt instructions resembling practitioner guidance:** Clean. They describe the paper’s construction/evaluation prompts, rather than advising a downstream user.
- **Appendix E summarised without reproducing 165 rows:** Clean coverage. Its purpose and column meanings are captured; no individual-row claim is made.
- **Other opposition bullets:** Clean. The source explicitly qualifies reimplementation successes, distinguishes validity from discriminative strength, tests specification ambiguity, rejects inspected documentation as underspecified, and contrasts prior benchmark scopes.
- **Historical ingestion read claims:** Not independently provable from a finished reference, but not flagged as fabricated. The reference’s actual section coverage is complete.
- **No lexical quotation defects:** All 19 `[V]` passages match source wording under the repository checker’s conversion normalisation. The two blockquote findings concern raw line breaks alone.