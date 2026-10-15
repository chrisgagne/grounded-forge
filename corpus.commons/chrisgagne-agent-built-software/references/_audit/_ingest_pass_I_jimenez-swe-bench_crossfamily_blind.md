## 1. What I read

Read in full, in the required order: all three calibration fixtures; `pass-i-spec.md`; `frozen-deep.md` (351 lines); and `tape.md` (4,441 newline-delimited lines, all 52 pages). Also read the complete brief, source card and frozen-reference checksum, plus the repository operating instructions and required architecture documents.

Checked the original PDF through deterministic extraction of every page. All 52 pages match the tape after whitespace normalisation, and every printed page number matches its page marker. Separately inspected layout-preserving extraction of PDF pages 1, 4–8 and 23–30 to check provenance, table alignment and the incomplete Lite passages. No successful visual inspection of figure images was completed; no numerical finding depends on reading chart pixels.

Both supplied checksums match their files. The arXiv record confirms the authors, version dates, DOI, subjects and CC BY 4.0 licence link. [arXiv record](https://arxiv.org/abs/2310.06770)

I did not read the parallel auditor’s findings or logs. No files were edited. This report is delivered here because the filesystem is read-only.

**Blind-leg result: two corrections required.**

## 2. Findings

### 1. The statistics table changes an inclusive token limit to an exclusive one

**Deep-reference line:** 297 — “10,000 under 30,000 tokens used”.

**Problem class:** Changed quantitative qualifier.

**Evidence:** Tape lines 346–350, p. 4, §3. The authors exclude sequences **with more than** 30,000 tokens. This leaves sequences of **at most** 30,000 tokens. The reference’s main discussion at line 138 states the exclusion correctly, but the statistics table changes its boundary.

**Exact fix:** Replace the value cell at line 297 with:

> 19,000 issue-PR pairs from 37 repositories; 10,000 instances with at most 30,000 tokens used

Keep the existing `[AP]` marker and citation.

### 2. The connections summary broadens the scope of the code-context comparison

**Deep-reference line:** 320 — the combined list of program-repair work, code-editing work and defect datasets, followed by “named as the most relevant prior work, none with SWE-bench’s scale of code context”.

**Problem class:** Scope overstatement.

**Evidence:** Tape lines 1004–1007, p. 9, §6. The authors identify program-repair and commit-guided editing **works** as most relevant. Their subsequent comparison concerns existing **datasets**. The reference merges these statements, making “none” apply to the combined collection of works and datasets.

**Exact fix:** Retain the bold list of works and datasets, but replace everything after its colon with:

> the authors identify automated program repair and commit-guided code editing as the most relevant work, then state that none of the existing datasets presents code context at SWE-bench’s scale [BT] (p. 9, §6).

## 3. Count and required checks

**Claims checked:** Every substantive claim in the frozen reference, including compound prose, numerical assertions, quotations, evidence markers, cross-references and provenance notes. For a reproducible counting convention, this comprises **304 audit units**: 139 non-heading prose/metadata/quotation lines and 165 body-table cells. Compound assertions within a unit were traced individually. Another 23 table-header cells and 36 headings were checked for labels, scope and section coverage. These counts are audit units, not an inflated estimate of atomic propositions.

| Defect class | Confirmed defects |
|---|---:|
| Changed quantitative qualifier | 1 |
| Scope overstatement | 1 |
| Unsupported or invented substantive claim, otherwise | 0 |
| Evidence-marker mismatch | 0 |
| Verbatim/blockquotation mismatch | 0 |
| Missing source section | 0 |
| Uncited author/work cross-reference | 0 |
| Task-application guidance | 0 |
| Post-source vocabulary | 0 |
| Source-external analytical framing | 0 |
| **Total** | **2** |

**Key-statistics table:** All numerical values match the tape or transparently stated calculations from its tables. Of its 21 rows, 20 are faithful as written; line 297 needs the inclusive-limit correction above. The table appropriately preserves the paper’s conflicting Claude 2 percentages and distinguishes the authors’ No-Op percentage statement from the percentages calculated from Table 23.

**Authors’ limitations:** Lines 259–263 accurately represent all three limitations stated in §7, tape lines 1020–1028: Python-only instances; deliberately simple baseline methods, with encouragement for other approaches; and the insufficiency of execution-based testing alone to guarantee reliable generations. No external methodological criticism has been added to that list.

**Coverage:** Every main-text section and Appendix A–F subsection has corresponding coverage. All ten appendix cases, Tables 25–34, are represented. Summarising rather than reproducing every repository-specific statistic is not a missing-section failure.

**Provenance:** The PDF checksum, page count, page markers, newline count, word count and pdftotext long-token counts are correct. The abandoned markitdown output and historical ingestion session are not supplied, so their reported word counts, comparison counts and historical actions remain independently unverified; they are not counted as confirmed defects.

## 4. Over-flag guard

- **Line 351: automated `no-quote` warning.** The verbatim checker reports the literal `[V]` in the evidence-marker legend. This defines the marker; it does not mark an unquoted source claim. No correction required.

- **Blockquotes and `[V]` passages.** No wording defect found after restoring layout whitespace. Straight/curly quotation-mark normalisation does not change the words. The quoted fragment at line 249 is a contiguous excerpt, not an internally shortened quotation.

- **“Surprisingly poorly”, “primitive Python”, “lucky”, and the more efficient Django solution.** These evaluations occur in the authors’ own discussion: tape lines 712–715, 964–969, 4069–4079 and 4187–4202. They are not imported judgements.

- **The seaborn failure attributed directly to absent image input.** This is a strong causal attribution, but the authors explicitly make it at tape lines 3738–3741. Reporting it as their attribution is clean.

- **The positions framed against other approaches.** The source explicitly contrasts self-contained coding problems, contrived benchmark tasks, “potpourri” evaluations, dense retrieval in this setting and semantic-similarity scoring. These are not invented oppositions.

- **Claude 2’s 1.96% versus 1.97%, and Claude 3 Opus’s higher result.** These inconsistencies originate in the source. The reference identifies them rather than silently reconciling them.

- **The GPT-4 collapsed-context comparison.** The 1.3% → 3.4% statement is in the source, despite the differing oracle figure elsewhere. The reference records the discrepancy at line 343.

- **“Generally removes half” versus the construction funnel.** The former describes the validation-engine step at tape lines 1627–1630. It need not equal the attrition across every subsequent filtering step. Both statements are faithfully attributed.

- **No-Op percentages and SWE-Llama patch lengths.** The reference’s explicit table calculations are correct. Identifying arithmetic discrepancies is not an external methodological verdict.

- **The incomplete Lite passages.** The malformed §2.4 sentence and unfinished Appendix A.7 are present in fresh extraction of the original PDF. The pointer to Appendix A.7 does appear separately in §2.4, supporting line 129.

- **Table 29’s repository identity.** Although its task-instance label says sympy, its URLs, issue and patches identify pylint. The reference reports the mismatch explicitly.

- **Figure 10’s class/function terminology and error-type discrepancy.** These come from the source’s text and caption. The reference preserves their attribution.

- **4,441 versus 4,468 lines.** There are 4,441 newline-delimited lines. Python’s broader `splitlines()` additionally counts embedded Unicode line separators in figure text. The stated newline count is correct.

- **Full textual coverage with uninspected figures.** The reference explicitly declares text-only image scope and limits chart reporting to source prose and captions. It does not claim visual verification.