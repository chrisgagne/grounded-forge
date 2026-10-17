## 1. What I read

Read in full:

- `blind-brief.md`, all three calibration fixtures, and `pass-i-spec.md`.
- `frozen-deep.md` — all 906 lines, with findings restricted to the specified scope.
- `scope-extract.md` — all 183 blocks. A mechanical comparison confirmed that every block matches its stated `tape.md` range.
- `source-card.md`.

Read in part:

- `tape.md`: the surrounding paragraphs, tables and complete feature boxes needed to finish clipped extract blocks, and passages supporting the in-scope PR #23 lines outside Chapter 12.
- `source.pdf`: front matter and Table 12.1 on PDF pages 363–364, through deterministic extraction preserving layout.

Verified both supplied hashes. The PDF also matches the source card’s stated page count, byte size and creation date. An independent page-by-page comparison found no alphanumeric word deficits against `pdftotext -layout`.

Ran the verbatim checker. Its notices on scoped quotations concerned apostrophes or initial capitals; none established a substantive quotation mismatch.

I did not read the fixer’s findings or audit the derived tier. This remains the blind report. Historical conversion and audit-process assertions requiring earlier files or execution logs remain unverified. No files were edited.

**Outcome: the scoped reference does not pass unchanged. Six deep-reference defects and two source-card defects require correction.**

## 2. Findings

1. **Deep line 258 — recommendation reported as completed action.**

   **Evidence:** Tape lines 9361–9363 say Kyle *recommends* that Bridget move to the information systems team. They do not report that he moves her.

   **Exact fix:** Replace:

   > He moves her to an information systems team as its technical representative,

   with:

   > He recommends that she move to an information systems team as its technical representative,

2. **Deep line 338 — case-specific conclusion generalised.**

   **Evidence:** Tape lines 13451–13454 explicitly qualify the positive assessment of multiple team memberships with “in this case” and connect it to the company’s business. The reference’s concluding sentence presents the assessment as applying to MTM generally, provided it is understood well.

   **Exact fix:** Replace the paragraph’s final sentence with:

   > For EA Engineering, Science, and Technology, Inc., the box calls multiple team memberships “a highly positive strategy” [V] for achieving business outcomes (Ch 9, “EA Engineering, Science, and Technology, Inc.”).

3. **Deep lines 9 and 898; missing coverage within Part XV — restored organisational-complexity exposition omitted.**

   **Evidence:** The in-scope extract includes tape lines 22505–22557. Its substantive subsection, “Organizational Complexity”, distinguishes external and internal complexity and presents strategies for managing it. Part XV contains no account of this material. Its environmental-fit typology does not cover these strategies.

   **Exact fix:** Insert after deep line 617:

   > The section also distinguishes external complexity, arising from the organisation’s operating environment, from internal complexity in its products, technologies, people, processes and structure [AP]. Drawing on De Toni and De Zan, it presents strategies for handling high external complexity: self-managing teams or autonomous business units with entrepreneurial responsibility; simple rules and infrastructure that permit complex outputs; and developing capabilities through open networks, brand and reputation, shared values and knowledge, trust, and leadership at multiple levels [BT, De Toni and De Zan] (Ch 15.2, “Organizational Complexity”).

   Do not repair the omission merely by changing the Coverage wording.

4. **Deep lines 9 and 898; missing Chapter 15.6 coverage — restored resilience exposition omitted.**

   **Evidence:** Tape lines 23102–23111 are explicitly in scope. Their paragraph begins at tape line 23088 and explains resilience categories and organisational foresight. The deep reference ends Part XV at line 644 without covering Chapter 15.6 or these restored claims.

   **Exact fix:** Insert after deep line 644:

   > ### Organising for change in the 21st century
   >
   > The section presents nine resilience lenses grouped into three categories: structural resilience, concerning internal systemic dynamics and loosely coupled structures; integrative resilience, concerning external interconnections and social cohesion; and transformative resilience, concerning risks that require organisational transformation [AP]. It distinguishes organisational foresight from forecasting and calls for environmental scanning, discovery, innovation and experimentation to engage with uncertain futures [AP] (Ch 15.6, “Organizing for Change in the 21st Century”).

   This repairs the omission within this audit’s restored-text scope; it does not certify coverage of other, out-of-scope Chapter 15.6 material.

5. **Deep line 814 — numerical qualifier dropped.**

   **Evidence:** Tape lines 29047–29048 describe Belaga’s corporate career as “over 25 years”. The reference makes it a 25-year career.

   **Exact fix:** Replace:

   > After a 25-year corporate career,

   with:

   > After a corporate career of more than 25 years,

6. **Deep line 846 — `[V]` marker on a synthesised numerical range.**

   **Evidence:** Tape lines 28090–28091 describe nearly 20 percent in Ecuador and less than 5 percent in several named countries. The reference’s compact range is a faithful paraphrase, but `<5% to ~20%` is not verbatim source wording.

   **Exact fix:** Replace the row with:

   > | TEA range across GEM economies | <5% to ~20% | [AP] (Ch 19.1) |

7. **Source-card line 23 — incorrect source-section locator.**

   **Deep-reference counterpart:** Line 898 correctly identifies Chapter 4.2.

   **Evidence:** Tape lines 5382–5393 contain the Kolb/Silberman passage and footnote 15. The running section identifier at tape line 5404 is “4.2 • Reinforcement and Behavioral Change”, printed page 99.

   **Exact fix:** In the source card, replace:

   > the end of Ch 4.3’s “allowing time for reentry” sentence

   with:

   > the end of Ch 4.2’s “allowing time for reentry” sentence

8. **Source-card line 23 — inaccurate description of extraction order.**

   **Deep-reference counterpart:** Lines 892–896 refer readers to this conversion account.

   **Evidence:** The tape preserves content-stream order, which does not consistently put folios and running headers first. For example, the page containing printed page 350 begins with the continuation of Table 12.1; its folio and running header occur at the end, immediately before the next form feed. The same ordering is visible around tape lines 5404–5405 and 14122–14125.

   **Exact fix:** **Strip**:

   > Each page’s folio and running header come first in its text.

## 3. Counts and required checks

**Claims checked:** all constituent claims in **126 in-scope claim-bearing lines**, plus three heading anchors. This is a count of composite, line-level claim units—not an invented atomic-claim total. The source card’s provenance statements were checked separately.

| Defect class | Deep reference | Source card |
|---|---:|---:|
| Recommendation strengthened into completed action | 1 | 0 |
| Generalisation beyond the source’s setting | 1 | 0 |
| Missing substantive coverage | 2 | 0 |
| Dropped numerical qualifier | 1 | 0 |
| Evidence-marker mismatch | 1 | 0 |
| Incorrect section locator | 0 | 1 |
| Incorrect conversion description | 0 | 1 |
| **Total** | **6** | **2** |

**PR #42 scoped defects:** 5, including the two restored-text coverage omissions.  
**Blind-only (PR #23 lines): 1**  
**Re-anchoring-line defects:** 0.

No capture comparison is calculated: that requires the subsequent sort against the fixer’s findings.

**Key-statistics table:** its sole in-scope row, line 846, matches the tape numerically but needs the marker correction above. The other fourteen rows were read as context and were not re-audited.

**Source limitations:** there is no separate source-limitations list. The reviewed qualifications concerning Watson’s group-performance results, Tuckman’s sequence, appraisal-technique suitability and Lewin’s stability assumption match statements the source makes. I found no unsupported methodological verdict in the scoped integrity notes.

## 4. Over-flag guard

- **Table 12.1, line 484:** clean. The original PDF really prints “Substitute Leadership” and “Instrumental Leadership”. Its row placements match the reference. Correcting the heading from domain knowledge would reduce source fidelity.
- **Table 14.3, line 596:** clean. Its unusual power-distribution wording and explanatory footnote are both present in the source.
- **Ault passage, line 248:** considered a speaker-attribution concern, but not counted. The quoted words occur exactly in OpenStax’s narration of Ault’s conclusion; the reference does not explicitly claim they came from a recorded direct utterance.
- **Expectancy equation, line 287:** clean when read as a whole. The following sentence specifies summation across outcomes and resolves the opening shorthand.
- **Watson results, line 187:** clean. The intervals, absence of significant overall differences at the later intervals, and advantages on perspectives and alternatives match the tape.
- **Drucker opposition, line 888:** clean. The source itself explicitly says culture is more influential than strategy in the stated respects.
- **Papa John’s, line 35:** the assessment of Schnatter’s continuing ethical commitment is surprising, but it is the source’s assessment.
- **French disconnection law, line 755, and federal-law coverage, line 696:** retained. These statements reproduce the source’s claims; this audit does not determine their legal accuracy.
- **Feature labels:** no label defect established. In particular, line 586 correctly retains the Managerial Leadership label despite its title beginning “Sustainability and Responsible Management”.
- **Source-card conversion totals:** the exact historical line-match totals were not independently reproduced. Different extraction settings produce different line boundaries; that alone does not establish a defect. The independent page-level word comparison found no missing alphanumeric words.
- **Historical process assertions:** dates of fetching, prior converter failures and prior full-reading claims cannot be established from the frozen reference and current tape alone. They remain unverified rather than being counted as fabricated.