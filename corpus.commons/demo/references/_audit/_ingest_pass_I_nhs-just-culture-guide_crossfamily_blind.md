## 1. Material read and audit scope

Read in full, in the prescribed order: all three calibration fixtures, `pass-i-spec.md`, and `frozen-deep.md`. Then read all of `tape.md` and `source-card.md`, and inspected the complete single-page original:

(`_planning/pass-i/demo/nhs-just-culture-guide/source.pdf`)

Verified both supplied SHA256 values. Independently extracted the whole poster with Poppler: its word-token multiset exactly matches the regional tape. Checked every quotation, question, recommendation, routing statement, table row, attribution and source-integrity assertion.

The verbatim checker reported only initial-letter normalisation at deep-reference line 15, explicitly permitted by the audit standard. All seven recommendation blockquotes match the tape after joining extraction line breaks; none requires smart-quote normalisation.

No prior audit findings were read. Downstream references and distillations were not inspected. No files were edited; this response is the complete report.

**Decision: the reference requires correction before passing.**

## 2. Findings

### 1. Unsupported licence assignment and source-external legal framing

**Deep lines:** 5, 184; associated classification at line 6.  
**Sidecar lines:** 7–8, 25.  
**Class:** Unsupported provenance; source-external legal framing.

**Evidence:** Neither the complete tape nor the original poster states an Open Government Licence, its version, CC BY equivalence, or derivative-distribution conditions. The footer at tape lines 108–109 supplies supporter and lineage information, without licensing terms. The sidecar repeats the licence assertion without identifying evidence for its application to this document.

This does not establish that the licence assertion is false; it establishes that the supplied materials do not substantiate it. The claim that derivatives inherit “only the attribution requirement” is also external legal analysis.

**Exact fix:**

- Deep line 5: replace the entire sentence beginning `Licence:` with:  
  `Licence: not stated in the supplied poster; not verified from the supplied materials.`
- Deep line 184: **strip**.
- Deep line 6: replace with:  
  `**Scope:** unverified — the supplied materials do not establish the claimed open licence.`
- Sidecar line 7: replace with `scope: unverified`.
- Sidecar line 8: replace with `licence: not stated in the supplied poster; unverified`.
- Sidecar line 25: **strip**.

### 2. Unsupported publisher-history and canonical-equivalence claims

**Deep line:** 5.  
**Sidecar lines:** 4, 23.  
**Class:** Unsupported provenance.

**Evidence:** Tape line 109 and the original footer establish the printed domain `improvement.nhs.uk`. They do not establish a 2022 merger, retirement of a particular publisher page, or equivalence between this mirror and a separately authenticated canonical copy. The supplied PDF cannot independently authenticate its own equivalence to another copy.

**Exact fix:**

- Deep line 5: replace the entire `Canonical URL:` sentence with:  
  `PDF URL recorded on the source card: https://cpcw.org.uk/wp-content/uploads/sites/19/2018/03/180316-NHSi_just_culture_guide_A3.pdf. The poster prints improvement.nhs.uk in its footer.`
- Sidecar line 4: replace with `publisher: NHS Improvement`.
- Sidecar line 23: replace with:  
  `The source card records the PDF URL as https://cpcw.org.uk/wp-content/uploads/sites/19/2018/03/180316-NHSi_just_culture_guide_A3.pdf. The supplied poster prints improvement.nhs.uk in its footer.`
  
### 3. Q3 summaries narrow “protocols/accepted practice” to protocols

**Deep lines:** 70, 88, 132, 148.  
**Class:** Dropped alternative; narrowed source meaning.

**Evidence:** Tape lines 68–72 explicitly include “protocols/accepted practice” in both 3a and 3b. Several summaries instead describe a protocol as the necessary condition. In particular, line 70 says that knowing departure from an agreed protocol is the **only** path to Q4. This excludes the accepted-practice wording retained in the source.

**Exact fix:**

- Line 70: retain its first sentence; replace the remainder with:  
  `Q3 proceeds to Q4 only on Yes to all three questions: applicable agreed protocols/accepted practice are in place, they were workable and in routine use, and the individual knowingly departed from “these protocols”. No to any routes to Recommendation D [AP].`
- Line 88: replace the Q3 parenthetical with:  
  `(Q3 — Yes to all three questions about applicable agreed protocols/accepted practice, workability and routine use, and knowing departure)`
- Line 132: replace `(no workable protocol, no knowing departure)` with:  
  `(No to any of 3a–3c)`
- Line 148: replace the Q3 parenthetical with:  
  `(Q3 Yes to all — applicable agreed protocols/accepted practice in place, workable and in routine use, and knowing departure from “these protocols”)`

### 4. Absence of indications becomes absence of health factors

**Deep line:** 148.  
**Class:** Dropped epistemic qualifier; overstatement.

**Evidence:** Q2 asks whether there are **indications** of substance abuse, physical ill health or mental ill health: tape lines 52, 59–60. No to all proceeds to Q3 at line 67. These answers do not establish that health factors are absent.

**Exact fix:** Replace:

`health factors absent (Q2 No to all)`

with:

`no indications of substance abuse, physical ill health or mental ill health (Q2 No to all)`

### 5. Unsupported ranking of recommendation wording

**Deep line:** 140.  
**Class:** Source-external evaluative framing.

**Evidence:** Recommendations D/E say “is unlikely to be appropriate” at tape lines 74 and 88; F says “may not be appropriate” at line 96. The poster does not rank F as a “softer formulation”. That comparison is the reference writer’s interpretation.

**Exact fix:** Replace the first sentence with:

`Recommendations D and E say “is unlikely to be appropriate”; Recommendation F says “may not be appropriate” and directs the reader to organisational guidance likely to include senior HR advice on the degree of mitigation (Q3–Q5 recommendations) [AP].`

Retain the following sentence.

### 6. Invented structural intention: contributors considered “before the individual”

**Deep line:** 172.  
**Class:** Source-external causal/design framing; overgeneralisation.

**Evidence:** The poster explicitly opposes treating wider patient-safety issues as individual issues: tape lines 26–28. It does not say the tree was built to consider contributors “before the individual”. Indeed, Q1 first asks about individual intention and can immediately route to management action: lines 42–49. The preamble’s narrower claim concerns principles considered before **formal management action**, lines 15–17.

**Exact fix:** Replace the paragraph with:

`The source does not identify a named opposing author or school. It states that using the guide helps protect patients “by removing the tendency to treat wider patient safety issues as individual issues” (Preamble, paragraph 3) [V]. It also says the guide highlights principles to consider before formal management action is directed at an individual staff member (Preamble, paragraph 2) [AP].`

### 7. Sidecar invents an individual-support versus wider-investigation choice

**Deep line:** No direct counterpart; sidecar line 21.  
**Class:** Invented opposition; source meaning changed.

**Evidence:** The sidecar describes deciding whether individual support is required “versus whether a wider systemic investigation is the right response”. Every recommendation preserves wider investigation or wider actions: tape lines 45–49, 54–56, 62–64, 74–77, 88–91, 96–99 and 103–105. Individual intervention and wider investigation are not mutually exclusive alternatives.

**Exact fix:** Replace sidecar line 21 with:

`The poster attributes the guide to the work of Professor James Reason and the National Patient Safety Agency’s Incident Decision Tree. It supports a conversation between managers about whether a staff member involved in a patient safety incident requires specific individual support or intervention to work safely. It states that action singling out an individual is rarely appropriate because most patient safety issues have deeper causes requiring wider action. Every recommendation retains wider investigation or wider actions.`

## 3. Counts and required checks

**Claims checked:** 69 claim-bearing units in the deep reference, plus 17 sidecar units. A unit is a substantive paragraph, numbered item, question, blockquote, metadata field or statistics row; every constituent assertion was traced. This count avoids presenting an arbitrary count of atomic clauses.

Also checked all 65 evidence-marker occurrences, including descriptive mentions of markers.

**Defects: seven findings**, grouping repeated occurrences of the same defect:

| Primary class | Count |
|---|---:|
| Unsupported provenance/licensing | 2 |
| Dropped alternatives or qualifiers | 2 |
| Source-external analytical framing | 2 |
| Invented opposition in sidecar | 1 |

No independent blockquote mismatch, numerical error, uncited author connection, missing substantive source section, task-application insertion or post-source terminology defect was found. Findings 5–6 involve unsupported content presented under `[AR]`; their remedy is substantive replacement, rather than merely changing the marker.

**Key-statistics table:** All six rows match the poster: five tests; eleven sub-questions; seven recommendation exits; four caveats; two exits explicitly saying singling out is unlikely to be appropriate; and two explicitly directing appropriate management action. Seven counts exit locations, including the identical D/E recommendations.

**Author-stated limitations:** The four caveats at deep lines 17 and 27–30 faithfully cover tape lines 30–41. The reference does not invent an author-stated empirical limitations list.

## 4. Over-flag guard

- **Seven recommendations despite identical D/E wording:** Clean. The reference explicitly counts separate exit locations and discloses the duplication.
- **A–G labels:** Clean. Line 8 expressly identifies them as editorial labels and maps them accurately to the poster.
- **Q3 extraction order:** Clean. The tape emits 3b/3c before 3a, but preserves the numbered questions and correct routing. The reference restores their numbered order.
- **Initial lowercase “action” at line 15:** Clean under the specification’s explicit allowance for the checker’s `initial` category.
- **Blockquote layout:** Clean. Joining PDF extraction line breaks changes layout, not wording. All seven quoted recommendation bodies match.
- **Ordinary paraphrases such as “residual”, “filter” and “decomposition”:** Not defects by themselves. They describe directly observable routing or the explicit one-action-at-a-time rule. Findings above concern added or changed meaning.
- **Individual action remaining possible under D/E:** Clean. “May include, but not be limited to, the individual” directly supports line 124.
- **Wider investigation retained after deliberate harm:** Clean. Recommendation A explicitly requires it.
- **Source-given operational guidance:** Clean in the deep tier. Reporting the poster’s recommendations does not itself introduce task-application guidance.
- **Reason and the NPSA Incident Decision Tree:** Clean `[BT]` attribution. Both are named in the footer; no additional theory or biography is imported.
- **2018 dating and A3 format:** Supported by PDF metadata and dimensions. March 2018 is consistent with creation/modification metadata and the recorded URL, although the poster prints no publication date.
- **Logos and values strapline:** Their omission from the tape is disclosed and confirmed visually. No substantive decision-tree or preamble section is missing. Line 180’s “every textual element” should be understood with that disclosed exception.
- **Downstream A–G consistency at line 178:** Not verified in this blind packet. This is an operational consistency assertion, not an author claim; no inconsistency is inferred merely because downstream files were not supplied.