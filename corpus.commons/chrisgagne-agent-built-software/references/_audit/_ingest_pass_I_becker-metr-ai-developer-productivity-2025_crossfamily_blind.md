1. **What I read**

Read in full, in the requested order: all three calibration fixtures, `pass-i-spec.md`, `frozen-deep.md` (251 lines), and `tape.md` (2,951 newline-delimited lines covering all 51 pages and every appendix). Also read `blind-brief.md`, `source-card.md`, the frozen checksum, `CLAUDE.md`, and its nine required architecture documents.

Inspected the supplied PDF’s metadata and rendered pages 2, 18 and 46: Figure 1, Table 3, and Tables 7–8. Independently extracted all 51 PDF pages with `pdftotext` 26.08.0; every page matched the tape after removing page markers and surrounding whitespace. Other PDF pages received textual, rather than visual, inspection.

Checked the licence link on the [version-specific arXiv page](https://arxiv.org/abs/2507.09089v2); it points to CC BY 4.0.

The frozen-reference checksum and source-PDF checksum both match their supplied values. I did not read the parallel auditor’s findings or logs. No files were edited.

**Outcome: two corrections required in the frozen reference.**

2. **Findings**

**1 — Deep-reference line 207: dropped qualifier / strengthened attribution**

- **Problem:** “Peng et al.’s task criticised as unrepresentative and close to training data” removes the authors’ uncertainty about similarity to training data. The reference’s earlier account at line 27 correctly preserves that uncertainty.
- **Evidence:** Tape lines 106–109, §1.1, p. 3: the task is described as unrepresentative and “likely to be similar to a large amount of LLM training data,” which “may unfairly advantage” AI systems. The source does not establish actual training-data overlap.
- **Exact fix:** Replace:
  
  `with Peng et al.'s task criticised as unrepresentative and close to training data`
  
  with:
  
  `with Peng et al.'s task criticised as unrepresentative and likely to be similar to a large amount of LLM training data, which may unfairly advantage AI systems relative to humans`

**2 — Deep-reference line 251: nonexistent audit-stamp cross-reference**

- **Problem:** “Pass I: see the stamp on line 2 and the audit log” directs readers to a stamp absent from the frozen artefact. Line 2 is blank.
- **Evidence:** Frozen-reference lines 1–3. No Pass I stamp appears elsewhere in the frozen file. The supplied checksum confirms this is the designated frozen artefact.
- **Exact fix:** **Strip**:
  
  `Pass I: see the stamp on line 2 and the audit log.`
  
  A completed audit may subsequently add its actual stamp and log reference.

3. **Count and substantive checks**

**122 claim-bearing audit units checked:** 100 prose, frontmatter and bullet records, plus 22 statistics-table rows. This is a grouped-record count, not an invented atomic-proposition count; all constituent assertions, quantities, citations and markers within those records were checked.

Also checked all **202 evidence markers**: 45 `[V]`, 10 `[AP]`, 28 `[AR]`, 93 `[AE]` and 26 `[BT]`.

| Defect class | Count |
|---|---:|
| Dropped qualifier / strengthened attribution | 1 |
| Broken audit-provenance cross-reference | 1 |
| Verbatim mismatch | 0 |
| Evidence-marker mismatch | 0 |
| Changed numerical value, sign, sample size or significance | 0 |
| Missing source section | 0 |
| Uncited external author or work | 0 |
| Task-application guidance | 0 |
| Post-source vocabulary | 0 |
| Source-external analytical framing | 0 |
| **Total** | **2** |

**Quotations:** All 45 `[V]` quotations match the tape after joining line wraps. None requires smart-quote normalisation to obtain a match. There are no Markdown blockquotes. The repository’s verbatim checker also returned no findings.

**Key-statistics table:** All 22 rows match the cited tape passages or, for the three approximate intervals, Figure 1. No numerical correction is required. Figure 1 supports approximately +1% to +39% for the observed result, −32% to −14% for developer forecasts, and −31% to −10% for post-study estimates.

**Limitations:** The reference faithfully carries all three §4.1 caveats and all six Table 2 misreadings. It also preserves the authors’ cautions about exploratory subset analysis, potentially biased qualitative evidence, recording selection, recruitment, task selection, scope creep, ordering and AI experience. No source section is wholly missing.

**Source card:** No contradicted provenance claim found. Title, byline, version, date, page count, checksum, conversion method and licence attribution check out. Historical assertions about the fetch date and the producing agent’s actions cannot be independently established from the supplied artefacts.

4. **Over-flag guard**

- **Evaluative language:** “Surprisingly,” “impressive retention rate,” “moderate evidence,” and “immense progress” originate in the source. They are not auditor-added evaluations.
- **Positions framed against:** Lines 222–227 trace to explicit source criticisms, cautions or rejected design alternatives. They are not invented oppositions.
- **Figure 1 confidence level:** Appendix D.2 states that intervals default to 95%. The reference accurately says the *caption* does not specify the level; leaving the approximate figure readings unlabelled does not assert a different level.
- **Conflicting recording counts:** The source itself reports 74 retained recordings and separately uses 44 AI-allowed and 54 AI-disallowed recordings. Line 241 preserves this unresolved discrepancy instead of inventing a reconciliation.
- **Conflicting recruitment counts:** The source gives 51 preliminary respondents in Appendix G and 50 in the mid-study forecaster brief. The reference correctly distinguishes them.
- **Cursor-experience correction:** The roughly 25%-to-0% change comes directly from footnote 15. It is not an unsupported reading of Figure 12.
- **Literature percentages:** The source’s prose reports a 65% increase in requirements satisfied, while Table 3 labels Weber’s result “65% faster.” The reference identifies which account it is reproducing. Likewise, Table 3’s 55% output figure is source-supported despite the earlier prose’s 14–51% range.
- **Table 4 arithmetic:** The printed difference of 9 between displayed means of 116 and 106 is present in the source. Recording it as printed is faithful.
- **Source-only boundary:** Every named external work is cited by the paper. Descriptions of participant instructions and labelling procedures remain descriptions of the study, rather than advice to practitioners.
- **Image coverage:** The reference explicitly declares its limited image inspection and identifies Figure 1 as the exception. It does not claim comprehensive visual coverage.