## 1. What I read

Read in full, in the required order:

- All three calibration fixtures.
- `pass-i-spec.md`.
- `frozen-deep.md`, lines 1–332.
- `tape.md`, lines 1–1172, including all Table 1 cells, references and glossary definitions.
- `source-card.md` and `frozen-deep.sha256`.

Also read the repository operating instructions and required architecture documents.

For `source.pdf`, checked its metadata, checksum and complete text extracted deterministically with `pdftotext -layout`. That extraction matches `tape.md` byte for byte. I did **not** visually inspect rendered PDF pages.

The frozen reference’s checksum matches `frozen-deep.sha256`. The PDF’s checksum matches the checksum recorded in the reference and source card.

I did not read the parallel auditor’s findings. No files were edited.

## 2. Findings

**No source-fidelity defects found. One audit-metadata defect requires correction.**

1. **Deep-reference line 330 — dangling audit-status cross-reference.**

   **Text:** `**Pass I.** Pass I: see the stamp on line 2 and the audit log.`

   **Problem class:** Inaccurate audit metadata/internal cross-reference.

   **Evidence:** Line 2 of the frozen reference is blank. The reference contains no Pass I stamp. This is an artefact-level defect; there is no relevant tape passage. The sentence points readers to evidence of audit status that the frozen artefact does not contain.

   **Exact fix:** **Strip line 330.** Any subsequent audit-status statement should identify the actual completed audit record.

### Statistics-table result

The key-statistics table, lines 278–290, matches the tape:

| Item | Verified result |
|---|---|
| Practices | 20 |
| Tasks | 48: PO 14, PS 6, PW 19, RV 9 |
| Priorities | 21 High, 22 Medium, 5 Low |
| Tasks with “No additions to SSDF 1.1” | 10; listed task IDs match |
| Tasks tagged “Not part of SSDF 1.1” | 6; listed task IDs match |
| Tasks tagged “Modified from SSDF 1.1” | 3; listed task IDs match |
| Practice-level tags | PW.3 new; PO.5 and PS.1 modified |
| Other numerical entries | Three priority levels, three primary audiences, three informative-reference sources, EO section, workshop date, model-size wording, 19 references and approval date all match |

The practice/task totals and priority counts are explicitly labelled as the reference’s own tallies. They are not misrepresented as totals stated by NIST. Independently extracting the source’s 48 task IDs and priorities produced an exact match with the reference.

### Authors’ limitations result

The reference accurately represents the authors’ stated limitations and scope boundaries:

- Deployment and operation of AI systems are outside scope; most data governance and management are outside scope: tape lines 299–309 and 507–509.
- Practices require adaptation and are not universally applicable: lines 368–379.
- Model versioning, lineage and security guarantees have acknowledged limits: lines 380–389.
- The SSDF and Profile address cybersecurity risk management only: lines 412–427.
- Data provenance cannot always be verified because it is not always known: lines 833–838.

I found no added methodological verdict or source-external limitation presented as the authors’ position.

## 3. Counts

**Checked: 154 claim-bearing units**, counting each non-heading prose paragraph, list item or statistics row once. Composite units were checked clause by clause, including their quantities, qualifiers, citations and reference identifiers. This is a reproducible unit count, **not an asserted atomic-claim total**.

Additional checks covered:

- All 20 practice descriptions and 48 task entries.
- All 189 evidence markers: 46 `[V]`, 106 `[AP]`, 13 `[AR]`, 1 `[AE]`, 23 `[BT]`.
- All source-content headings and page anchors.
- All 13 statistics rows.
- All author/work connections.

| Defect class | Count |
|---|---:|
| Unsupported substantive claim | 0 |
| Evidence-marker mismatch | 0 |
| Verbatim mismatch | 0 |
| Changed number or dropped material qualifier | 0 |
| Overgeneralisation | 0 |
| Missing source-section coverage | 0 |
| Unsupported author/work cross-reference | 0 |
| Task-application guidance | 0 |
| Post-source vocabulary | 0 |
| Source-external analytical framing | 0 |
| Audit-metadata/internal-reference defect | **1** |
| **Total** | **1** |

The verbatim checker reported no findings. There are no blockquotes in the frozen reference.

## 4. Over-flag guard

- **Positions framed against, lines 312–314:** Clean. The source explicitly rejects checklist use and standalone use, and explicitly declines to distinguish human-written from AI-generated source code: tape lines 368–371, 284–290, 507–509 and 307–309. These are supported distinctions.
- **Normative recommendations throughout Table 1:** Clean. These report NIST’s own guidance. They do not introduce task-specific advice from the ingester.
- **“Art … than an exact science,” closed-loop manipulation and arbitrary-code risks:** Clean. These potentially evaluative or causal formulations are supplied by the source itself: lines 258–272.
- **Deterministic statistics tallies:** Clean. Their derivation is disclosed, and the counts match Table 1.
- **“October 30, 2022” in reference [1]:** Clean as reported. The tape prints that date alongside the year 2023: lines 1045–1047. The deep reference records the inconsistency instead of silently correcting it.
- **Different title in “How to Cite”:** Clean. The discrepancy is present in tape lines 94–96, compared with the cover and title page.
- **PO.5 modification tag, C1-before-R1 ordering and PW.8.1’s empty reference cell:** Supported by the tape’s column positions at lines 618–633 and 916–924. I found no transcription defect. I have not independently verified the historical claim that the ingester inspected renders.
- **Fetch date, conversion-tool version and image-classification history:** These are process-provenance attestations, not claims NIST’s publication could establish. The supplied files do not independently prove those historical events; that alone does not establish that the attestations are false. The supplied PDF identity and present conversion fidelity were independently verified.
- **Coverage:** Every section enumerated in the source’s contents has corresponding coverage. Summarising routine front-matter boilerplate does not constitute an omitted substantive section.

**Blind-leg outcome:** Source content, evidence markers, quotations, statistics and stated limitations pass this audit. Strip the dangling audit-status sentence; this report does not certify completion of the parallel audit, reconciliation or stamping workflow.