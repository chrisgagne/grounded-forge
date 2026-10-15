## 1. What I read

Read in full, in the brief’s prescribed order: all three calibration fixtures, `pass-i-spec.md`, and `frozen-deep.md` (229 lines). Then read all of `tape.md` (2,298 lines), including front matter, every Table 1 task and example, reference mappings, footnotes, bibliography and appendices. Also read `blind-brief.md`, `source-card.md`, the supplied repository instructions, `CLAUDE.md` and its nine listed architecture documents.

Inspected the original PDF selectively: PDF pages 9, 21, 33 and 36, covering the contents, retired-task rows, Table 2 and change log. Checked the PDF’s page count and embedded-image inventory programmatically. The complete source-text read was through the tape; I did **not** visually inspect every original PDF page.

:codex-file-citation{path="/Users/cgagne/Documents/LLM Repos/repos/grounded-forge/_planning/pass-i/chrisgagne-agent-built-software/nist-ssdf-1-1/source.pdf" purpose="source"}

Verified both hashes:

- Frozen reference: `575e0e7e20ad092db69a25d0abb0bb554d4f62959ad9885ebd23690edf66e5a9`, matching `frozen-deep.sha256`.
- Original PDF: `617746e553a9e2da49bfbd4eef0dfc3094758a39b869314e4173ac36605cde22`, matching the reference and source-card.

Ran `check-verbatim.py frozen-deep.md --source tape.md`: **no findings**. Independently checked both blockquotes with only whitespace collapsed; both matched exactly, without smart-quote normalisation. Procedural deviation: the automated check ran after the cold read.

I did not read the parallel auditor’s findings. No files were edited. The filesystem is read-only, so this response is the report; no report file or audit stamp was written.

Historical ingestion assertions remain **unverified**, rather than disproved: the acquisition/check dates, producing model and effort, exact converter version, prior reading and inspection activity, 1800-pixel inspection scale, retained table images, and staging conversions. The source-card repeats those assertions but does not independently establish them.

## 2. Findings

**No confirmed defects. No replacement or strip is required.**

The following trace summary records the checks supporting that conclusion. Line numbers refer to the frozen reference and tape.

| Frozen-reference lines | Source evidence | Result |
|---|---|---|
| 5–8 | Tape 12–105; page anchors throughout; contents at 296–306 | Title, authors, date, publication number, DOI, pagination and structure match. Licence checked separately below. |
| 13–15 | Tape 137–147, 259–286, 317–353, 421–449, 481–503 | Thesis preserves the authors’ recommendations, expected benefits, tailoring and non-prescription. |
| 21–35 | Tape 68–100, 163–248, 317–406 | Authority, audiences, acknowledgments, patent caveat, shifting left and future work are supported. |
| 37–49 | Tape 274–275, 421–449 | Both quotations are exact after joining line wraps; surrounding paraphrases preserve qualifications. |
| 53–55 | Tape 467–503 | Four groups, table interpretation, undefined terms and environment enumeration match. |
| 61–99 | Tape 515–991 | Every PO task summary and stated example traces; borrowed definitions and zero-trust pointer are present. |
| 105–113 | Tape 1003–1135 | PS requirements, examples, code-signing pointer and provenance/SBOM claims match. |
| 119–163 | Tape 1146–1751 | Every live PW task and stated example traces; retired identifiers and conditional testing language match. |
| 169–179 | Tape 1753–1987 | RV requirements, examples, response options and root-cause practices match. |
| 185–197 | Tape 1997–2298; original PDF pages 21, 33 and 36 | Appendices, bibliography, example EO mappings and table conventions match. |
| 203–207 | Tape 52, 166–170, 467–480; full-source check | All statistics match. No measured percentage reduction from SSDF adoption is reported. |
| 211–216 | Tape 385–406, 450–456, 713, 836, 1047–1050, bibliography and Table 1 mappings | All named connections occur in the source. Fourteen NISTCSF mapping entries verified. |
| 220 | Tape 421–442, 485–496 | Checklist/sequence opposition is explicit in the source. |
| 224–228 | PDF checksum; tape’s conversion declaration and anchors; exact-quotation checks; NIST policy | Verifiable provenance agrees. Historical process assertions remain unverified as described above. |

**Key-statistics table:** all three rows match. Four groups are enumerated at tape lines 469–480; “more than 150” accurately paraphrases “over 150” at line 166; Version 1.1 and February 2022 match lines 34 and 52. No changed quantity, sign, sample size or significance level was found.

**Authors’ limitations:** the reference has no separate limitations list. Its distributed caveats accurately reflect the authors’ statements: implementation requires expertise; practices form a high-level subset; applicability and formality vary; frequencies are notional; examples are optional; ordering implies neither priority nor implementation sequence; and some terms require local definitions. These trace to tape lines 194–196, 279–283, 421–442 and 481–503. Line 207’s observation about absent measured percentage reductions is accurate, but is **not** a limitation explicitly declared by the authors.

**Source-card:** bibliographic fields, publication scope, US copyright statement and checksum agree with the supplied source. Worldwide reprint and derivative-work permission is supported by the cited [NIST Technical Series Publications policy](https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-software-and-technical-series-publications). This current check does not establish that the policy was checked on the recorded ingestion date.

**Coverage:** both numbered sections, the Executive Summary, References and all three appendices have reference coverage. Every live task and retired identifier is represented. No substantive source section was found missing.

## 3. Count

**78 compound claim records checked:** 76 prose/table/metadata records and two blockquotes. Each constituent assertion was traced within its record. This is a grouped-record count, **not** an asserted count of atomic propositions.

Also checked all **101 evidence-marker occurrences**: 2 `[V]`, 52 `[AP]`, 4 `[AR]`, 30 `[AE]` and 13 `[BT]`. Source-card assertions were checked separately and are outside the 78-record count.

| Defect class | Confirmed defects |
|---|---:|
| Unsupported source-content claim | 0 |
| Evidence-marker mismatch | 0 |
| Verbatim/blockquotation mismatch | 0 |
| Changed number or dropped material qualifier | 0 |
| Finding broadened beyond the source | 0 |
| Missing substantive section / TOC mismatch | 0 |
| Uncited author or work | 0 |
| Task-application guidance | 0 |
| Post-source vocabulary | 0 |
| Source-external analytical framing | 0 |
| Demonstrably incorrect provenance | 0 |
| **Total** | **0** |

This blind leg found no confirmed source-fidelity defect. It does not certify the historical ingestion assertions or complete the two-leg Pass I gate.

## 4. Over-flag guard

- **Lines 31 and 133—causal and cost claims:** considered as possible imported domain reasoning. Clean: shifting-left benefits are explicit at tape lines 330–335; reuse benefits are explicit at 1294–1305.
- **Lines 55 and 220—prescriptive language:** clean source paraphrase. The publication itself tells adopters to define terms and enumerate environments, and explicitly rejects checklist and sequencing interpretations.
- **Lines 129 and 141—retired-task discrepancies:** clean. Table 1 and Appendix C describe different stages of the identifier history. The reference preserves their statements rather than inventing a reconciliation.
- **Line 211—CSF footnote alongside table mappings:** clean. The footnote’s non-mapping statement appears at tape lines 400–403, while Table 1 contains fourteen NISTCSF entries. The reference reports both without explaining away the tension.
- **Line 214—OWASP edition numbers:** clean. ASVS 4.0.3, MASVS 1.4.2, SAMM 1.5 and SCVS 1.0 are the editions printed in this source’s bibliography.
- **Line 207—absence of measured effectiveness percentages:** clean bounded observation about the publication, without an added methodological verdict.
- **Lines 9 and 224–226; source-card lines 20–22—historical process claims:** not classified as fabricated merely because this audit lacks execution records. Their verifiable portions agree with the supplied artefacts; the remaining assertions are expressly unverified.
- **Condensed examples throughout Table 1 summaries:** clean summarisation. The reference retains their notional status and material conditions, including appropriate use, unavailable verification, available resources and risk-based decisions.