## 1. What I read

**Read in full:** `blind-brief.md`; all three calibration fixtures; `pass-i-spec.md`; `frozen-deep.md`, lines 1–451; `tape.md`, lines 1–5118, covering the converted text of all 122 pages; and `source-card.md`.

**Original inspected in part:** :codex-file-citation{path="/Users/cgagne/Documents/LLM Repos/repos/grounded-forge/_planning/pass-i/chrisgagne-agent-built-software/owasp-llm-top10-2026/source.pdf" purpose="source"} — metadata, page count, checksum, deterministic text extraction, and image/link objects on pp. 6, 9, 28, 106–107 and 121–122. Image contents were not visually inspected.

The frozen reference matches `frozen-deep.sha256`. The PDF matches the checksum declared in the reference and source card. A fresh `pdftotext -layout` extraction using Poppler 26.08.0 matches the tape **byte for byte**.

I did not read the parallel auditor’s findings or logs. No files were edited.

## 2. Findings

**1. Deep reference line 449 — inaccurate audit-status cross-reference.**

- **Text:** “**Pass I: see the stamp on line 2 and the audit log.**”
- **Problem class:** Source-integrity/provenance defect.
- **Evidence:** Line 2 of the frozen reference is blank. Line 1 records generation metadata, not a Pass I stamp. The promised stamp therefore does not exist in the artefact under audit. `pass-i-spec.md` requires the audit log to exist before stamping.
- **Exact fix:** **strip** line 449. A completed audit can subsequently add its actual stamp and log location.

**Disposition:** Correction required. I found no substantive source-fidelity defect within the declared text-only coverage.

## 3. Count and checks

**438 claim-bearing audit units checked.** This is a reproducible bundle count, not an asserted atomic-claim count: 258 remaining prose/list/statistics/provenance lines, 90 individual coverage-matrix cells, and 90 individual risk-to-framework blocks. Constituent assertions, names, quantities, qualifiers and evidence markers were checked within each bundle.

| Defect class | Count |
|---|---:|
| Inaccurate audit-status/provenance cross-reference | 1 |
| Unsupported substantive claim | 0 |
| Evidence-marker mismatch | 0 |
| Verbatim quotation mismatch | 0 |
| Changed quantity or materially dropped qualifier | 0 |
| Overgeneralised finding | 0 |
| Undeclared section omission | 0 |
| Uncited author/work connection | 0 |
| Task-application guidance introduced by the ingester | 0 |
| Post-source vocabulary | 0 |
| Source-external analytical framing | 0 |
| **Total** | **1** |

**Quotations:** All **70 `[V]` quotations** match the tape after joining layout whitespace. No wording or punctuation corrections, including smart-quote corrections, are needed. There are **no blockquotes**. The prescribed verbatim checker also returned no findings.

**Key statistics:** All **22 rows** match the tape’s values, settings and evidence classifications. This includes the incident counts and weighting, attack-success figures, disclosure metrics, poisoning experiments, session-cost example, embedding-reconstruction results and CVSS scores.

**Framework tables:** All **90 coverage-matrix cells** match pp. 58–59. The per-risk element mappings and primary/supporting classifications match the corresponding framework sections. The absent LLM10 RMF row and absent LLM02 AIVSS row are accurately recorded.

**Limitations:** There is no dedicated author-limitations list in the reference. Its descriptions of imperfect incident data, scope boundaries and mitigation limitations match the authors’ statements. The unnamed databases/classifiers observation at line 442 accurately records an absence; it does not invent an author admission or methodological verdict.

**Coverage:** Every text-bearing TOC section is represented. Figures 1–3, Appendix B’s image content and sponsor logos are explicitly excluded under the recorded operator-approved text-only scope.

## 4. Over-flag guard

- **Evaluative or causal wording:** “defense effect,” “most consequential move,” “load-bearing,” “canonical,” and “higher consequence” initially warranted scrutiny. They are present in the source itself: p. 5; p. 7; p. 13; p. 19; and pp. 50–51 respectively. They are not ingester-added judgements.
- **Security instructions in the deep tier:** Least privilege, deterministic authorisation, human approval and circuit breakers are the document’s own mitigation guidance. Their inclusion is source summary, not newly invented task application.
- **“Positions … frames against,” lines 414–429:** Each opposition is explicitly supported by the source’s rejection, prohibition, limitation or contrasting instruction. None requires inventing an opposing position.
- **Five and 250 poisoned documents, lines 381 and 391:** The source says “as few as” five and 250. The table records those demonstrated sufficient counts; it does not claim a universal minimum or necessary threshold. I did not flag the compressed wording.
- **Suspected page citations:** Line 215’s pp. 36–37 correctly span LLM05’s scenarios; the chat-template experiment occurs on p. 36, correctly cited in line 392. Neither needs correction.
- **Appendix inconsistencies, lines 443–444:** The “50 calls” example and incidents absent from entry bodies occur in the appendix passages cited. Recording them as source-internal differences is legitimate.
- **Image exclusions:** These are declared in both the reference and source card. They do not constitute silent partial coverage.
- **PDF dates:** The reference’s 2 August creation date and 4 August modification date match metadata displayed in the local New Zealand timezone. The underlying UTC dates fall on the preceding days; this is not a changed date.
- **Source-card provenance:** Title, version, licence, leads, checksum and conversion claims match the supplied artefacts. Fetch date, download URL and resource-page title remain supplied provenance, not independently verified acquisition events.