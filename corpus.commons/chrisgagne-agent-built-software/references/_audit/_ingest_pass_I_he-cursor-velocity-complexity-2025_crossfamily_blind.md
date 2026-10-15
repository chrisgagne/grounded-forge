**1. What I read**

Read in full, in the required order: all three calibration fixtures, `pass-i-spec.md`, `frozen-deep.md` (249 lines), and `tape.md` (3,052 lines, pages 1–19, including all references and Appendices A–D). Also read `blind-brief.md`, `source-card.md`, the checksum file, and the repository instructions and required architecture documents.

Inspected the original PDF’s metadata, Figure 1, and Tables 2, 3 and 6 visually. Checked table alignment using deterministic layout extraction on pages 4, 14, 17 and 18. Independently extracted all 19 PDF pages and confirmed that every page’s converted text occurs in the tape.

Original PDF: :codex-file-citation{path="/Users/cgagne/Documents/LLM Repos/repos/grounded-forge/_planning/pass-i/chrisgagne-agent-built-software/he-cursor-velocity-complexity-2025/source.pdf" purpose="source"}

The frozen-reference and PDF checksums match their recorded values. I did not read the parallel auditor’s findings. No files were edited; this report is delivered here because the environment is read-only.

**2. Findings**

1. **Deep reference line 29 — dropped uncertainty qualifier.**

   **Problem:** “pointing to slowdown mechanisms such as developer over-optimism, low AI reliability and high task complexity” omits the source’s qualification that these mechanisms are *potential*.

   **Evidence:** Tape lines 137–143, page 2, explicitly describe “potential slowdown mechanisms”. The reference should retain that uncertainty when reporting the cited study’s explanations.

   **Exact fix:** Replace:

   “pointing to slowdown mechanisms such as developer over-optimism, low AI reliability and high task complexity”

   with:

   “pointing to potential slowdown mechanisms such as developer over-optimism, low AI reliability and high task complexity”.

2. **Deep reference line 127 — dropped statistical-significance qualifier.**

   **Problem:** “no estimator finds an effect on duplicate density” broadens the source’s finding of no *significant* effect into absence of an effect.

   **Evidence:** Tape lines 2443–2446, page 16, state that all three estimators find no significant effects. Table 6 reports nonzero duplicate-density point estimates: +7.03%, +1.61% and −0.34% (tape lines 2351, 2371 and 2379). Visual inspection confirms that these coefficients are unstarred.

   **Exact fix:** Replace:

   “no estimator finds an effect on duplicate density”

   with:

   “no estimator finds a statistically significant effect on duplicate line density”.

3. **Deep reference line 249 — dangling audit-provenance reference.**

   **Problem:** “Pass I: see the stamp on line 2 and the audit log” points to a stamp that does not exist in the frozen reference. Line 2 is blank. This is a premature provenance pointer, rather than evidence of an actual unearned stamp.

   **Evidence:** Frozen reference lines 1–3 and 249. The tape cannot substantiate an ingestion audit’s completion.

   **Exact fix:** **Strip** the sentence:

   “Pass I: see the stamp on line 2 and the audit log.”

4. **Source-card line 18 — overbroad description of extraction corruption.**

   **Deep-reference counterpart:** Line 239 describes the affected tables more precisely and requires no correction.

   **Problem:** The sidecar says the tables’ “significance stars attach to every cell in the text layer”. That description is too broad. In Tables 2 and 6, the erroneous stars attach to coefficient estimates, while standard errors and percentage-change cells remain unstarred. Table 3 has the broader corruption described in the deep reference.

   **Evidence:** Tape lines 956–973, 1120–1172 and 2336–2385; original Tables 2, 3 and 6 on pages 7, 8 and 16.

   **Exact fix:** Replace:

   “Tables are extracted column by column and their significance stars attach to every cell in the text layer; the deep reference records how they were read.”

   with:

   “Tables are extracted column by column. The tape misassigns significance stars to coefficient estimates in Tables 2 and 6, and to coefficients, standard errors and diagnostic entries in Table 3; the deep reference records how significance was checked against the original PDF.”

**3. Counts and explicit checks**

Checked **132 compound claim records**: 119 claim-bearing paragraphs, bullets or statistics rows in the deep reference, plus 12 source-card metadata fields and its body paragraph. This is a record-level count; component assertions within each record were checked individually but are not counted separately.

| Defect class | Count |
|---|---:|
| Dropped uncertainty qualifier | 1 |
| Dropped statistical-significance qualifier | 1 |
| Dangling audit-provenance reference | 1 |
| Overbroad extraction-provenance description | 1 |
| Wrong quantities, signs, sample sizes or significance levels | 0 |
| Verbatim or evidence-marker defects | 0 |
| Missing source sections | 0 |
| Uncited-author cross-references | 0 |
| Added task guidance, post-source vocabulary or source-external analytical framing | 0 |
| **Total** | **4** |

Inspected all **240 evidence-marker occurrences**. The verbatim checker reported no findings, while explicitly leaving 25 figure claims for manual checking. Independently checked all **52 marked quotations**: each matches the tape after whitespace and smart-quote normalisation. There are no blockquotes.

**Key-statistics table:** All **28 rows** match their cited source passages numerically. Signs, sample sizes, uncertainty values and reported significance classifications are correct. Where the tape corrupts significance stars, the original PDF confirms the reference’s classifications.

**Authors’ limitations:** The list matches the authors’ stated limitations: the five internal-validity limitations, external-validity boundaries, estimator disagreement, autonomy-level identification, insufficient language coverage, the descriptive convenience sample, and uncertainty about applying complexity metrics to AI-generated code. No external methodological verdict is presented as an author-stated limitation.

**Coverage:** Every numbered substantive section and Appendices A–D has corresponding coverage. No section-level omission was found.

**4. Over-flag guard**

- **Statistics rows marked `[V]`: clean.** The repository’s verbatim-checking procedure explicitly permits numerical figure claims under this marker. Rearranging source numbers into a statistics table is not itself a marker violation.
- **Practical recommendations, lines 157–161: clean.** Refactoring sprints, scaled test coverage, Cursor rules, quality-aware assistants, self-throttling and extra review scrutiny all come from §5.2, tape lines 1590–1621.
- **Evaluative and plausibility language: clean.** “Highly plausible”, “which is unlikely”, “strong evidence”, “inherently more complex”, “complexity debt” and “comprehension tax” are the authors’ own language or explicitly attributed interpretations.
- **Causal language concerning the GMM models: clean as attribution.** The paper itself makes these causal interpretations and describes its diagnostic tests as validating the required moment conditions. This audit tests faithful reporting, not whether those methodological claims are correct.
- **Figure 1’s arrow descriptions, line 169: clean.** Visual inspection confirms the solid positive velocity and complexity arrows, dashed positive warnings arrow, dotted duplication arrow, and solid negative arrows from warnings and complexity to velocity.
- **Inconsistent complexity percentages and repository totals: clean.** Line 241 explicitly records the source’s discrepancies instead of silently reconciling them. The statistics table identifies which passage supplies each value.
- **“1.84x baseline increase”: clean.** This wording occurs in §4.2. It should not be replaced by an auditor’s independent reinterpretation of the coefficients.
- **Positions framed against, lines 227–231: clean.** The source expressly challenges the stated optimism, pessimism, extrapolation, estimator use and generation-first design.
- **Named connections, lines 206–223: clean.** The cited people and works occur in the paper’s references, and the described connections are supported by its body.
- **Historical ingestion assertions:** The recorded fetch date, generating model and earlier inspection actions cannot be independently reconstructed from the supplied source files. I have not labelled them fabricated merely because their historical execution records were not supplied.