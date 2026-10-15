## 1. Reading and audit scope

Read in full, in the brief’s required order:

- All three calibration fixtures.
- `pass-i-spec.md`.
- `frozen-deep.md`, lines 1–626.
- `tape.md`, lines 1–2,060, including every quiz, bibliography entry and licence provision.
- `blind-brief.md` and `frozen-deep.sha256`.

Also read the repository operating contract and architecture documents. Consulted relevant portions of the ingestion protocol and verbatim-check implementation.

No original `source.*`, source-card, acquisition manifest, producer receipt, images or video contents were supplied in this folder. Their contents were not audited. I did not read the other auditor’s findings or logs.

The frozen reference’s SHA-256 matches:

`12ae9c71876f9d4e8f1fd0c8433ea4eafe45a635399560c98d73963422f236ab`

The verbatim checker, explicitly directed to `tape.md`, reported no quotation mismatches and 33 numerical claims requiring manual checking. All seven blockquotes match the source’s wording and punctuation after removing Markdown presentation and normalising quotation-mark typography.

**Decision: corrections required.** Findings 1–12 concern the reference’s content or attribution. Findings 13–16 are unresolved provenance assertions, rather than demonstrated falsehoods. No files were edited.

## 2. Numbered findings

### 1. Incorrect enumeration count

**Deep line:** 75.  
**Class:** Changed quantity.

**Problem:** “The guide’s five claims” introduces four claims. The source also has four.

**Evidence:** Tape 94–102: slow security measures; deployment delays; hiding source code; possible negligence.

**Exact fix:** Replace:

> The guide’s five claims:

with:

> The guide’s four claims:

### 2. Qualification dropped from the fixing prompt

**Deep line:** 367.  
**Class:** Dropped qualifier.

**Problem:** The summary instructs the AI to “maintain existing functionality”, omitting the source’s qualification.

**Evidence:** Tape 1457 qualifies maintaining existing functionality with “where practical”.

**Exact fix:** Replace:

> maintain existing functionality and insert no new vulnerabilities

with:

> maintain existing functionality where practical and insert no new vulnerabilities

### 3. Ambiguous source sentence silently resolved

**Deep line:** 367.  
**Class:** Unsupported paraphrase of ambiguous source wording.

**Problem:** The reference reports “silencing a crash by deleting the offending operation or even the whole functionality” as an observed failure mode. Tape 1461 instead says that AI systems “often fail … to silence the crash by deleting” those things. The source sentence is awkward and ambiguous; the reference silently resolves it into a clearer claim.

**Evidence:** Tape 1461. No other tape passage resolves the ambiguity.

**Exact fix:** Replace the sentence beginning “Identifying and fixing the true cause…” with:

> Identifying and fixing the true cause without breaking functionality is vital [AP]. PatchBench found that the most common failure was guarding the symptom with incomplete local checks; the guide also reports failures to localise the vulnerability and overly broad conditions that reject benign input [BT] [Shen2026-09]. The tape’s intervening sentence about deleting operations or functionality is ambiguous.

### 4. Model-lag statistic loses its comparison population

**Deep line:** 536.  
**Class:** Dropped qualifier; broadened finding.

**Problem:** “Lag of open-weight behind closed-weight models” broadens a comparison specifically about the most advanced models.

**Evidence:** Tape 290 explicitly compares the most advanced open-weight and closed-weight models.

**Exact fix:** Replace the metric cell with:

> Lag of the most advanced open-weight models behind the most advanced closed-weight models

Keep the value and citation.

### 5. CI-time target loses its setting

**Deep line:** 551.  
**Class:** Dropped qualifier; broadened recommendation.

**Problem:** The table presents an unqualified “Target CI time”. The source gives the target for most projects and immediately acknowledges difficulties for operational technology and software controlling physical devices.

**Evidence:** Tape 1088. Deep line 269 retains these qualifications, but the statistics row does not.

**Exact fix:** Replace the metric cell with:

> Suggested CI time for most projects; operational technology and physical-device software may find this difficult

Keep the quoted value and citation.

### 6. Severity thresholds omit required adaptation

**Deep line:** 559.  
**Class:** Dropped qualifier.

**Problem:** The table reproduces the severity thresholds without the source’s instruction to adapt them to the system.

**Evidence:** Tape 1378; deep line 349 correctly retains that instruction.

**Exact fix:** Append to the value cell:

> ; “Adjust the thresholds to your system.”

Keep `[V] [BT] [Yan2026]`.

### 7. Package-hallucination statistic omits “average” and cohort date

**Deep line:** 564.  
**Class:** Dropped qualifiers.

**Problem:** The compressed table entry omits that the percentages are averages and that the models were available in 2024. These details matter when comparing this row with the newer-model replication.

**Evidence:** Tape 1504. Deep line 381 preserves both details.

**Exact fix:** Replace the row with:

> | Package hallucination (USENIX Security 25), models available in 2024 | 576,000 code samples, 16 LLMs; “the average percentage of hallucinated packages is at least 5.2% for commercial models and 21.7% for open-source models” | [V] [BT] [Spracklen2025] (Finding.md, § “Have humans review the fix”) |

### 8. Zero-observation result omits its boundary and caveat

**Deep line:** 566.  
**Class:** Dropped qualifiers; broadened finding.

**Problem:** “None in 1,134 short Python snippets from six models” omits that the observation concerns imports for everyday tasks using mainstream libraries. It also omits the explicit warning that the samples cannot establish a zero rate.

**Evidence:** Tape 1506. The same passage reports nonexistent imports from every model when prompted for niche or nonexistent libraries. Deep line 381 retains these distinctions.

**Exact fix:** Replace the row with:

> | Package hallucination, everyday tasks using mainstream libraries (arXiv, no venue listed) | No hallucinated package names observed in imports from 1,134 short Python snippets generated by six models; the samples were too small to establish a zero rate. Every model imported nonexistent packages when prompted for niche or nonexistent libraries. | [AP] [BT] [Hillah2026] (Finding.md, § “Have humans review the fix”) |

### 9. MDASH agent-count attribution points to the wrong key

**Deep line:** 543.  
**Class:** Citation attribution.

**Problem:** The table attributes the “more than 100” count to `[Bishop2026]`. In the tape, Bishop supports the preceding description of the staged system; the ensuing ensemble-count and stage description is attributed to Kim.

**Evidence:** Tape 638–643. Deep line 202 already includes `[Kim2026]` for this material.

**Exact fix:** In line 543, replace:

> [Bishop2026]

with:

> [Kim2026]

### 10. Two `[V]` statistics rows change the source’s numerical wording

**Deep lines:** 546 and 557.  
**Class:** Evidence-marker mismatch — two occurrences.

**Problem:** These rows claim verbatim extraction while changing number words into digits. The magnitudes are correct, but the rendered words are not character-exact.

**Evidence:**

- Tape 756 gives the OSS-CRS result using “twenty-five” and “sixteen”.
- Tape 1337 gives the reviewer count using “ten”.

**Exact fixes:**

- Line 546: replace the value with:

  > “twenty-five vulnerabilities across sixteen projects”

- Line 557: replace:

  > 10 reviewers endorsed a non-existent oracle

  with:

  > ten dedicated AI reviewers endorsed a non-existent oracle

  Change this row’s `[V]` to `[AP]`; retain `[BT]`, the key and locator.

### 11. Anthropic connection summary assigns an availability citation the wrong role

**Deep line:** 579.  
**Class:** Cross-reference scope/attribution.

**Problem:** The opening description treats the listed Anthropic sources collectively as evidence of AI capability and process advice. `[Anthropic2026-06-12-Export-Control]` is used for interruption of external-service availability.

**Evidence:** Tape 267; contrasted with the capability and process passages at 68–76, 490–499 and 579–586.

**Exact fix:** After “across threat models, sandboxing, discovery, deduplication, validation, triage and fixing”, insert:

> . [Anthropic2026-06-12-Export-Control] is cited separately for the interruption of external model availability (Finding.md, § “External versus local models”)

Retain the subsequent sentence about prompting disagreement.

### 12. Incident-report connection lacks the locator for Capoot

**Deep line:** 595.  
**Class:** Citation locator.

**Problem:** `[Capoot2026]` appears in the connection list, but neither supplied section locator contains its use.

**Evidence:** Capoot is cited at tape 267, under “External versus local models”. It is not cited in “Need for sandboxes” or “Evaluate merge/pull requests”.

**Exact fix:** Add this locator to the citation parenthesis:

> ; § “External versus local models”

### 13. Acquisition identity is asserted without its supporting record

**Deep lines:** 5 and 7.  
**Class:** Unverified provenance.

**Problem:** The commit hash, commit date, acquisition URL and acquisition-record assertions cannot be independently traced to the supplied tape. This does not establish that they are wrong.

**Evidence:** Tape 1 establishes the source-file path; tape 3–9 and 35 establish title, byline and authorship. Tape 5 mentions `gen-html`. The tape supplies no commit identity or acquisition record.

**Exact fix:** Replace the acquisition portion of line 5 with:

> Acquisition metadata recorded in this frozen reference: https://best.openssf.org/Finding-and-Fixing-Vulnerabilities-Using-AI/ ; repository https://github.com/ossf/wg-best-practices-os-developers ; commit 82590814cc174d8707cc805462cb53488d2d7f92, dated 2026-10-05. The acquisition record was not supplied for this blind audit, so these details remain independently unverified. The tape identifies the file as docs/Finding-and-Fixing-Vulnerabilities-Using-AI/Finding.md.

In line 7, replace the acquisition-record parenthesis with:

> (the tape comments that each chapter is intentionally its own H1 and refers to `gen-html`)

### 14. Local image availability is unverified

**Deep lines:** 20 and 623.  
**Class:** Unverified provenance.

**Problem:** The reference asserts that image files exist at a local converted-source path. The tape establishes relative image links and alt text, but cannot establish that this local directory exists or contains the images.

**Evidence:** The tape’s image links, including 118, 130, 1404 and 1786. No image files were supplied in the audit folder.

**Exact fix:** Replace both local-image-availability assertions with:

> The tape contains relative image links and alt text. Image binaries were not supplied for this blind audit; figure descriptions here are based on alt text and surrounding prose.

### 15. Conversion fidelity and manifest completeness are unverified

**Deep line:** 619.  
**Class:** Unverified provenance.

**Problem:** The tape cannot establish that it reproduces a pinned repository file byte for byte, that only front matter and MDX imports were dropped, that the original had 36,745 words, or that the acquisition manifest recorded complete coverage.

The tape’s own line and word counts are correct.

**Evidence:** Tape 1 establishes the file marker; tape 2049–2060 contains the licence ending. Direct counting confirms 2,060 lines and 36,749 whitespace-delimited words. No original or manifest was supplied.

**Exact fix:** Replace line 619 with:

> - **Source and conversion.** The supplied tape identifies one file, `docs/Finding-and-Fixing-Vulnerabilities-Using-AI/Finding.md`, and contains 2,060 lines and 36,749 whitespace-delimited words. Its final section is the licence. The acquisition manifest and original repository file were not supplied for this blind audit, so the pinned-commit identity, conversion operations, byte fidelity, original word count and manifest completeness declaration remain unverified.

### 16. Producer full-read claim lacks its receipt

**Deep line:** 620.  
**Class:** Unverified provenance.

**Problem:** The claim that the producing session read every line, with ranges recorded in a receipt, cannot be verified from the source itself. The receipt is absent.

**Evidence:** No passage in tape 1–2060 records the producer’s actions.

**Exact fix:** Replace line 620 with:

> - **Producer read coverage.** The frozen reference states that its producing session read every tape line and recorded the ranges in a producer receipt. That receipt was not supplied for this blind audit; the producer’s read coverage remains unverified.

## 3. Counts and required assessments

**Claims checked:** 1,025 claim/evidence units: 748 prose sentence or list-item units, 270 substantive table cells, and seven blockquotes. This is a grouped-unit count, not a claim that every independent clause constitutes a separately counted atomic claim. Headings and locators were also checked for coverage and correspondence.

**Findings:** 16 numbered findings, comprising 13 content/attribution defects and four unresolved provenance groups. Finding 10 contains two marker occurrences.

| Problem class | Count |
|---|---:|
| Incorrect enumeration quantity | 1 |
| Dropped qualifiers or broadened scope | 6 |
| Unsupported resolution of ambiguous source wording | 1 |
| Citation attribution, role or locator | 3 |
| Evidence-marker mismatch | 2 |
| Unverified provenance groups | 4 |
| Blockquote mismatch | 0 |
| Missing source chapter or substantive section | 0 |
| Uncited author/work introduced | 0 |
| Added task-application guidance | 0 |
| Post-source vocabulary | 0 |

**Key-statistics table:** All 44 rows were checked. The numerical magnitudes, sample sizes, percentages, dates and directions match the tape. It does **not** pass unchanged: findings 4–10 identify missing qualifications, an attribution correction and two verbatim-marker issues. No significance level or sign was changed.

**Author-stated limitations:** There is no separate limitations list in the reference. Its distributed account generally matches the authors’ stated boundaries: excluded topics, changing technologies, unsound and stochastic analysis, guardrail constraints, complex-patch limitations, uncertainty about prescription and repeated-run context, and continuing review requirements. The principal omissions are in the statistics table, especially the package-hallucination setting and zero-rate caveat.

**Coverage:** All ten enumerated source divisions are represented. The counts of 46 quizzes, 141 bibliography entries, 16 images and eight Google Drive video links match the tape. All quiz keys and answer summaries match. No TOC-versus-body coverage failure was found.

## 4. Over-flag guard

- **Numerical `[V]` entries without quotation marks:** Not blanket-flagged. The repository protocol expressly permits directly extracted numerical statistics in `[V]` table entries. Finding 10 concerns changed textual representations, rather than ordinary numerical extraction.
- **“Approving”, “neutral” and similar connection labels:** Not blanket-flagged. The canonical template requests how the guide cites sources. Most labels reasonably describe the guide’s use of those sources; findings 11–12 address specific citation-role and locator problems.
- **The “positions framed against” section:** Clean. The tape explicitly rejects or warns against the listed positions, including refusing AI, waiting for restricted models, relying on text-only controls, accepting consensus as proof, unreviewed loops, security-relevant vibe coding and ASLR alone.
- **Practitioner instructions in the body:** Clean as source summaries. The guide itself gives these instructions. Their imperative subject matter does not make them added task-axis guidance.
- **“Strong evidence”, “junior developers”, “maintenance nightmare” and “worst case”:** Clean. These potentially evaluative formulations come from the guide itself: tape 126, 534, 1501 and 1408.
- **Apparently conflicting Linux-kernel capability reports:** Preserved. Tape 1799 reports unsuccessful exploitation of identified areas, while 1814 reports successful vulnerability chains. The reference faithfully records both without inventing a reconciliation.
- **Attack-time statistics with differing disclosure/patch endpoints:** Preserved. The tape itself states those endpoints. This audit does not repair the guide’s claims against outside knowledge.
- **1Password and PatchBench results:** Their body treatment is appropriately bounded and retains the criticisms, exploit-blocking caveat and functional-correctness distinction.
- **Bibliography-only works and venue labels:** Clean. The 19 uncited-by-key entries are correctly listed, and “arXiv, no venue listed” describes the supplied bibliography rather than claiming that the work was never published elsewhere.
- **Blockquote typography:** Clean. Outer quotation delimiters, Markdown emphasis and straight/curly quotation conventions do not change the quoted words. No silently shortened or reworded blockquote was found.
- **Figure descriptions:** Clean against the tape’s alt text and surrounding prose. The reference does not invent chart values. Actual image contents remain outside this audit’s supplied evidence.