## 1. What I read

Read in full:

- `blind-brief.md`; all three calibration fixtures; `pass-i-spec.md`.
- `frozen-deep.md`, lines 1–526.
- `tape.md`, lines 1–2172, including all ten entries, appendices, acknowledgements and supporters.
- `source-card.md` and `frozen-deep.sha256`.
- Repository `CLAUDE.md` and its nine required architecture documents.

Inspected in part: :codex-file-citation{path="_planning/pass-i/chrisgagne-agent-built-software/owasp-agentic-top10-2026/source.pdf" purpose="source"} — complete rendered printed pages 8, 13 and 55, plus document metadata. These resolve the diagram, garbled scenario heading and image-only sponsor page. I did not visually inspect every PDF page.

Both supplied hashes match their files. PDF metadata confirms 57 pages, Word provenance, letter dimensions, the stated title field and creation timestamp. The tape contains 57 form feeds and 13,820 words.

I did not read the parallel auditor’s findings or logs. No files were edited. This response is the report; the filesystem is read-only.

**Outcome: three corrections required in the frozen reference.**

## 2. Findings

### 1. Dropped qualifier on planning

**Deep reference:** line 49, “manipulated inputs redirect goals, planning (‘panning’ as printed) and multi-step behaviour”.

**Problem class:** Dropped qualifier.

**Evidence:** Tape lines 308–310, printed p. 9, qualify planning with “when used”. The reference omits that qualification.

**Exact fix:** Replace that clause with:

> ASI01 captures the broader agentic impact where manipulated inputs redirect goals, planning (when used; “panning” as printed) and multi-step behaviour (ASI01, p. 9) [AP].

### 2. Diagram description assigns Connected data/RAG to the processing panel

**Deep reference:** line 29, the opening sentence groups “Memory and Connected data/RAG” beneath the agents within Integration/Processing.

**Problem class:** Figure-location transcription error.

**Evidence:** Original printed p. 8, PDF page 9. Memory is inside Integration/Processing. The Connected data/RAG box straddles the boundary between Inputs and Integration/Processing, below-left of the agent box, and connects bidirectionally to Memory.

**Exact fix:** Replace the opening sentence of line 29 with:

> The diagram, read from the render, has three panels: Inputs (User Prompts, API, External Agents); Integration/Processing (Policy & Governance and Human-in-the-loop above a box holding two Agents, with Memory below it); and Outputs (Tools, which lead to APIs/Resources, and External Agents). Connected data/RAG straddles the boundary between Inputs and Integration/Processing, below-left of the agent box, and connects bidirectionally to Memory (p. 8) [AP].

The remaining badge-location description on line 29 is supported.

### 3. Dangling reference to a nonexistent Pass I stamp

**Deep reference:** line 526, “Pass I: see the stamp on line 2 and the audit log.”

**Problem class:** Source-integrity metadata / broken internal cross-reference.

**Evidence:** Line 2 of the frozen reference is blank. There is no Pass I stamp in this artefact. This is a dangling reference, not evidence that an unearned stamp was applied. I did not inspect the parallel audit log.

**Exact fix:** **Strip** that final sentence. Add an audit-log reference only when the corresponding completed log and stamp exist.

## 3. Counts and required determinations

**Claims checked: 580 claim-bearing audit units:** 313 prose, list and metadata lines, plus 267 table data cells. Compound units were checked clause by clause; this is a reproducible unit count, not a claim that compound sentences contain only one proposition.

The checks also covered all **249 evidence markers** and **102 quotation spans** extracted by the repository verbatim checker. These overlap the 580 units and are not additional claims.

| Defect class | Count |
|---|---:|
| Dropped qualifier | 1 |
| Figure-location transcription | 1 |
| Source-integrity metadata / internal cross-reference | 1 |
| Unsupported source-external analytical framing | 0 |
| Evidence-marker mismatch | 0 |
| Verbatim quotation mismatch | 0 |
| Changed numerical value | 0 |
| Missing source section | 0 |
| Uncited external author/work connection | 0 |
| Added task-application guidance | 0 |
| Post-source vocabulary | 0 |
| **Total** | **3** |

**Quotations:** The verbatim checker reported no findings. No blockquotes occur in the reference. Ordinary PDF line wrapping and smart-quote differences do not constitute altered wording.

**Key-statistics table:** Matches the source. Independently checked:

- All ten examples/scenarios/mitigations/references count tuples on line 479.
- Ten entries; T1–T17; Amazon Q version v1.84.0 and the “thousands” wording.
- Twenty-five tracker rows, dated February–October 2025.
- Weekly tracker updates and the last-week digital-twin replay window.
- Five gold and twenty silver sponsor logos.
- 107 printed supporter entries.

The Appendix A, C and D tables also match their source mappings, dates, descriptions and named analysis links.

**Authors’ limitations:** There is no separate limitations list in the deep reference. The relevant author-stated caveats are preserved: unreliable separation of instructions from content (p. 9), inherent semantic divergence despite typed contracts (p. 29), and fault propagation potentially exceeding human response capacity and leaving residual risk (p. 30). I found no invented methodological limitations.

**Coverage:** Every TOC entry has corresponding coverage. All five recurring sections of each ASI entry are represented. No missing-section fail condition was found.

**Source-card provenance:** No contradiction found in its document-identification claims. Fetch date, retrieval history, historical webpage title/date, converter version and prior rendering/classification activity remain ingest-side declarations; the supplied source cannot independently establish those historical actions.

## 4. Over-flag guard

- **Imperative mitigation lists:** Clean. They reproduce the source’s own recommendations; they are not added task projections.
- **“Positions the author explicitly frames against,” lines 503–510:** Clean. Each opposition is explicit in the cited passages, including syntax-only validation, model-generated rationales, full semantic alignment, open registration and agent-held keys.
- **Strong causal or evaluative wording:** Clean where retained. Claims about ineffective perimeter security, an attribution gap making least privilege impossible, and catastrophic defensive actions appear in the source itself.
- **Hypothetical attack scenarios:** Clean as `[AE]`. Their presence under “Example Attack Scenarios” supports that classification without establishing that every scenario occurred.
- **Borrowed-through references:** Clean. The named publications, platforms, researchers and incident-analysis organisations occur in the source. The reference does not import their linked documents’ contents.
- **Inconsistent threat names and mappings:** Clean as transcription. The source itself varies T4, T6 and T12 names and contains the unusual Appendix A/C mappings. The reference appropriately preserves them.
- **Source typos:** Clean when identified or paraphrased transparently, including “AS01”, “AS04”, “LLM02;2025”, “lead by”, “criticial” and the repeated contributor name.
- **ASI02 scenario 4 heading:** Clean. The original visibly reads “Internal Query → External Exfiltration”; the tape’s symbols are extraction damage.
- **Ingester’s numerical tallies:** Clean. They are explicitly labelled as tallies and match the printed items.
- **Sponsor neutrality and governance statements:** Clean. They are present on the image-only sponsor page.
- **Absence of a standalone limitations section:** Not a defect. The source’s substantive caveats are covered in the relevant entry discussions.