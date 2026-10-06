**Blind-audit result: fail pending correction.** The reference is substantially source-grounded, but the findings below require correction. No files were modified.

**1. What I read**

Read in full, in the requested sequence: all three calibration fixtures, `pass-i-spec.md`, `frozen-deep.md` (306 lines), and `tape.md` (4,547 lines). Also read `blind-brief.md`, `source-card.md`, the frozen checksum, and the repository instructions and required architecture documents.

Inspected `source.pdf` in part: visually reviewed PDF pages 1, 3, 9–10, 20, 94, 105, 115 and 131–133; inspected layout-preserving text from pages 9–10, 20 and 135–137. These include the cover, Foreword formula, applicability matrix, FACTS formatting, both diagrams, survey numbering and questionnaire wording. Inspected PDF metadata, page count, file size and checksum.

Both checksums match their supplied values. The original has 137 pages and 2,248,402 bytes.

The automated verbatim check returned no findings. All **57 substantive `[V]` quotations** match the tape’s wording after joining extraction line wraps. There are **no Markdown blockquotes**.

I did not read the fixer’s findings, prompts or logs. External reading was limited to checking the bibliographic licensing claim against DOE’s [Web Policies](https://www.energy.gov/web-policies).

**2. Findings**

1. **Unsupported cross-volume attribution and provenance**

   **Deep lines:** 7, 14, 208, 278, 298 and 304. Also `source-card.md:21`.

   **Problem:** The reference imports specific claims about Volume 1 that the supplied Volume 2 does not establish: attribution to Reason, Reason and Hobbs, Johnston and Dekker; particular Volume 1 pages and an endnote; ownership of the Anatomy of an Event model by Volume 1; Volume 1’s formula wording; and its converter version.

   **Evidence:** Tape lines 26–29 and 74–77 establish the companion relationship. Lines 3197–3199 refer readers to Volume 1, Chapter 4, for culpability methods. Lines 2934–2962 present Anatomy of an Event without attributing it to Volume 1. No passage names the outside authors or establishes the other imported details.

   **Exact fixes:**

   - Replace item (3) of line 7 with:  
     “(3) For this reference, the investigation material on pp. 85–89 and the reporting and culpability material on pp. 96–99 are paraphrased. Volume 2 refers readers to Volume 1, Chapter 4, for further detail on the culpability methods; it does not identify outside authors for these passages.”
   - Line 14: replace “It carries forward Volume 1’s formula:” with “The Foreword states:”.
   - Line 208: replace “Using Volume 1’s Anatomy of an Event model” with “Using the handbook’s Anatomy of an Event model”.
   - Replace line 278 with:  
     “- **DOE Human Performance Improvement Handbook, Volume 1.** The companion volume whose tools this volume describes, and the volume cited for further detail on the culpability methods; approving [BT] (Foreword, p. ii; Sec 3, pp. 96–97).”
   - Line 298: **strip** “the same converter family as Volume 1 (`markitdown 0.1.5`)”.
   - Line 304: **strip** “where Volume 1 writes ‘Re + Mc → ØE’”.
   - Source-card line 21: replace the clause beginning “and its just-culture…” with:  
     “Volume 2 also discusses investigation and culpability, and refers readers to Volume 1, Chapter 4, for further detail on the culpability methods.”

   These findings concern traceability within this audit, not whether the cross-volume claims might be correct elsewhere.

2. **Descriptive content marked as author argument**

   **Deep line:** 20.

   **Problem class:** Evidence-marker mismatch.

   **Problem:** “The volume divides the work three ways” describes the document’s organisation; `[AR]` classifies it as an argument.

   **Evidence:** Tape lines 170–185 describe the three sections and their intended users.

   **Exact fix:** Replace `[AR]` with `[AP]`.

3. **Sections 1 and 2 narrowed to active errors at the job site**

   **Deep lines:** 20 and 254.

   **Problem class:** Scope over-extension through an unsupported classification.

   **Problem:** The first two sections are described exclusively as addressing active errors “at the point of work” or “at the job site”. Their coverage also includes knowledge workers’ document errors and defects that can enter the system and cause later events.

   **Evidence:** Tape lines 35–37 explicitly describe delayed consequences of knowledge-worker errors. Lines 158–185 describe the sections without imposing the reference’s exclusive active/latent division. Lines 1374–1381 identify detection of document errors and defects among Section 2’s purposes.

   **Exact fix:** Replace the final sentence of line 20 and the first sentence of line 254 with:

   “Sections 1 and 2 describe behaviours that help individuals and work teams anticipate, prevent or catch errors before they harm people, facilities or the environment; Section 3 provides methods for identifying latent organisational weaknesses that provoke error or weaken defences [AP] (Introduction, p. 1; Sec 3, p. 70).”

4. **An applicability list receives an unsupported reliability verdict**

   **Deep line:** 36.

   **Problem class:** Source-external analytical framing.

   **Problem:** Calling each tool’s applicability list “the reliable statement” adds a reliability judgement. The source directs readers to those lists for detail.

   **Evidence:** Tape lines 201–204.

   **Exact fix:** Replace the final clause with:

   “each tool’s own ‘Use This Tool’ list gives further details about its applicability.”

5. **Project Planning loses its applicability qualifications**

   **Deep line:** 152.

   **Problem class:** Dropped qualifiers.

   **Problem:** “But not for core business or level-of-effort work” changes “not typically used” into an exclusion. The statement that the project work plan “covers” the listed elements also omits their discretionary, applicable-as-needed status.

   **Evidence:** Tape lines 1918–1926, printed p. 58: the tool is “not typically used” for core business, programme and level-of-effort work; the plan “may address” the elements “as applicable”.

   **Exact fixes:**

   - Replace the applicability sentence with:  
     “It is used in design work, work not governed by established administrative procedures and work involving subcontractors; it is not typically used for core business, programme or level-of-effort work, which is guided by administrative procedures [AP] (Sec 2, p. 58).”
   - Replace “The project work plan covers” with “The project work plan may address the following elements, as applicable:”.

6. **Lagging indicators’ predictive limitation becomes categorical**

   **Deep line:** 190.

   **Problem class:** Dropped qualifier.

   **Problem:** “Not predicting what comes next” is stronger than the source’s “do not necessarily predict future accomplishments”.

   **Evidence:** Tape lines 2523–2528, printed p. 77.

   **Exact fix:** Replace the lagging-indicator definition with:

   “**Lagging** indicators measure results and outcomes, representing current position and accomplishments but not necessarily predicting future accomplishments [AP] (Sec 3, p. 77).”

7. **Indicator-selection guidance turns examples and conditional criteria into fixed requirements**

   **Deep lines:** 192 and 265.

   **Problem class:** Dropped qualifiers in prose and statistics-table cells.

   **Problem:** The 1–5 scale is presented as the scale used, rather than an example. The table also drops “where possible” from quantitative and “where appropriate” from disaggregate.

   **Evidence:** Tape lines 2584–2589 and 2600–2605, printed pp. 78–79. The source expressly gives 1–5 as an example and says the seven criteria need not be equally important.

   **Exact fixes:**

   - Line 192: replace “using a simple matrix and a 1–5 scale” with “using a matrix and a simple scoring scale, for example 1–5”.
   - Replace line 265 with:  
     `| Criteria for judging a candidate indicator | seven: direct, objective, adequate, quantitative where possible, disaggregate where appropriate, practical and reliable; an example scoring scale is 1–5, and the criteria need not be equally important | [AP] (Sec 3, pp. 78–79) |`

8. **The error-type map adds classifications the source does not make**

   **Deep line:** 250.

   **Problem class:** Source-external analytical framing and unsupported vocabulary.

   **Problem:** The heading introduces “slips and lapses”, terms absent from the tape. It also places place-keeping, flagging, Do Not Disturb, three-way communication and the phonetic alphabet under a skill-based classification that their cited passages do not explicitly give.

   **Evidence:** Tape lines 343–357 and 688–691 explicitly associate situational-awareness tools and self-checking with skill-mode work. The passages for the other tools—1047–1062, 1100–1115, 1673–1684 and 936–1028—describe their targets without supplying that performance-mode classification.

   **Exact fix:** Replace line 250 with these two bullets:

   “- **Skill-based.** Situational-awareness tools are said to be particularly helpful in skill-mode work (Sec 1, p. 5); self-checking is particularly effective for skill-based, repetitive tasks performed with little conscious thought, with attention peaking when a component’s status changes (Sec 1, p. 18) [AP].

   - **Other stated tool targets.** Place-keeping addresses omitted or repeated steps as attention shifts (Sec 1, p. 29); flagging addresses returning to a wrong but similar component after a distraction (Sec 2, p. 51); the Do Not Disturb sign addresses interruptions to repetitive or critical work (Sec 1, p. 31); three-way communication and the phonetic alphabet address misunderstood messages (Sec 1, pp. 26–28) [AP].”

9. **A latent error’s undetected status is extended to the definition of every defect**

   **Deep line:** 254, second sentence.

   **Problem class:** Definition over-extension.

   **Problem:** The sentence combines latent errors and defects as conditions that “stay hidden until revealed later”. That qualification appears in the definition of latent error, not in the definition of defect.

   **Evidence:** Tape lines 4415–4416 define defect; lines 4460–4463 define latent error and its undetected status.

   **Exact fix:**

   “The Definitions distinguish an active error, which changes plant state and triggers immediate undesired consequences, from a latent error, which embeds an undesired condition or reduces equipment reliability and remains undetected until subsequent operational activities; a defect is an undesired result of an earlier engineering-process error embedded in the physical plant or design-bases documentation [AP] (Definitions, pp. 128–130).”

10. **FACTS’ original formatting is wrongly attributed to conversion damage**

    **Deep lines:** 66 and 300.

    **Problem class:** Incorrect source-integrity explanation.

    **Problem:** The reference says the numbering after step 1 was “lost in conversion”. The original PDF already numbers only Foresee. Confirm and Test are unnumbered headings; Ask and Stop are bullets.

    **Evidence:** Tape lines 579–601 and original PDF page 20, printed p. 14, visually checked.

    **Exact fixes:**

    - Line 66: replace the parenthetical conversion explanation with:  
      “The original PDF, like the converted text, numbers only Foresee as step 1; Confirm and Test are unnumbered headings, while Ask open-ended questions and Stop when unsure appear as bullets.”
    - Replace the final sentence of line 300 with:  
      “The FACTS formatting on p. 14 is preserved from the original: only Foresee is numbered, Confirm and Test are unnumbered headings, and Ask open-ended questions and Stop when unsure appear as bullets.”

11. **The reported conversion word counts do not match the supplied files**

    **Deep lines:** 10 and 298. Also `source-card.md:19`.

    **Problem class:** Incorrect quantities in provenance notes.

    **Problem:** The stated counts, 36,491 converted words and 33,023 `pdftotext` words, are not reproducible from the supplied files using whitespace-delimited counting.

    **Evidence:** Both `wc -w tape.md` and Python whitespace splitting give **37,576** words. Running `pdftotext source.pdf -` and counting the resulting whitespace-delimited words gives **34,106**. The tape still has exactly 4,547 lines. Its word count averages approximately **274 words per PDF page**.

    **Exact fixes:**

    - Line 10: replace “36,491 words” with “37,576 whitespace-delimited words”.
    - Line 298: replace the word-count sentence opening with:  
      “Post-conversion check: 37,576 whitespace-delimited words in the supplied markdown against 34,106 from `pdftotext` on the supplied PDF, approximately 274 markdown words per PDF page;”.
    - Source-card line 19: replace its count comparison with the same two counts and identify the counting method.

    An alternative counting method would need to be stated and reproducible before retaining the existing figures.

12. **A quotation contradicts the reference’s declared paraphrase-only treatment**

    **Deep lines:** 7, 226 and 302.

    **Problem class:** Quotation-handling inconsistency.

    **Problem:** Line 7 places reporting-system material on pp. 96–98 within the paraphrase-only exception. Line 226 nevertheless quotes an at-risk practice from p. 98 with `[V]`. Line 302’s assertion that every quotation comes from non-excepted material is consequently false.

    **Evidence:** Tape line 3284 exactly supports the quotation. Its wording is correct; the defect is the conflict with the declared treatment.

    **Exact fix:** In line 226, replace:

    “‘Launching a reporting system without first establishing a Just Culture’ [V]”

    with:

    “introducing an error-reporting system before establishing a just culture”

    and retain the sentence’s concluding `[AP]` classification. Line 302’s quotation-location assertion then becomes accurate for this passage.

**3. Count and coverage assessment**

**Claims checked:** **438 audit units**—413 in the deep reference and 25 in the source card. The deep-reference count comprises 374 prose sentence units and 39 statistics-table cells. Bundled lists were traced item by item, but their constituent phrases were not inflated into a purported atomic-claim count.

Separately checked all **335 substantive evidence-marker occurrences**, including 57 `[V]` quotations.

| Primary defect class | Numbered findings |
|---|---:|
| Unsupported cross-volume attribution/provenance | 1 |
| Evidence-marker mismatch | 1 |
| Scope over-extension or dropped qualifier | 5 |
| Source-external analytical framing | 2 |
| Incorrect conversion/provenance statements | 2 |
| Quotation-handling inconsistency | 1 |
| **Total** | **12** |

Repeated occurrences of the same defect are grouped within a finding.

**Statistics table:** All 13 rows’ numerical values match the tape. Row 265 requires the qualification correction in finding 7. The table contains handbook assertions, examples and instrument counts; it does not report empirical study samples, significance levels or effect estimates.

**Source limitations:** There is no separate limitations list. The distributed cautions largely match the authors’ statements: illustrative rather than definitive practices, a menu rather than requirements, retaining effective existing tools, competence and thoughtful use as prerequisites, and no guarantee of perfect performance. Findings 3 and 5–7 identify qualifications that require correction. The source additionally places detailed statistical-data analysis beyond its scope (tape lines 2557–2558); that boundary is not included in the reference’s summary.

**Coverage:** Every named tool and all three principal sections have body coverage. No TOC section is wholly missing. Matrix cell assignments and diagram connections are explicitly omitted under the reference’s declared text-only scope; they are remaining coverage limitations, not undisclosed missing chapters. This audit does not certify them as recovered.

**4. Over-flag guard**

- **Verbatim quotations:** Considered punctuation, spelling and extraction differences. No quotation-text defect found. In particular, “same affect” and the other awkward quoted wording are present in the source.
- **Author-stated efficacy claims:** “Most events” during routine activities, independent verification’s higher error-catching probability, and self-assessment as the “most powerful” tool all have source passages. Their evidential strength was not independently graded.
- **Source recommendations:** STAR, SAFER, PACTS, briefing agendas, investigation questions and reporting practices belong in the deep reference because the handbook supplies them. They are not imported task-application guidance.
- **Explicit oppositions:** Mindless tool use, blind procedure compliance, punitive investigation, consequence-based blame, industrial tourism and defensive responses to oversight are explicitly criticised by the source. The “positions against” list is substantially clean.
- **Survey numbering:** Duplicate item 48 and the stray “12.” are present in the original PDF, not introduced by conversion. Reporting item labels 1–59 with that duplication is accurate.
- **Questionnaire affirmative-answer claim:** Printed p. 122 explicitly says affirmative answers indicate no problem, although later questions include contrary wording, such as asking whether unsafe attitudes or error precursors persist. The reference follows the author’s stated instruction; this is a source inconsistency, not an unsupported imported claim.
- **Just-culture and indemnity summaries:** The source presents an aspirational balance and permits full or partial indemnity. The reference does not explicitly assert that every organisation already achieves the balance or that indemnity must be complete; I did not count those as defects.
- **Work-product grades:** The four listed grades and their definitions match the source’s example. Describing that example does not, by itself, assert a compulsory grading system.
- **Third-party paraphrase policy:** Conservatively paraphrasing INPO-related material is an operator policy, not automatically an unsupported source claim. Finding 12 concerns a specific contradiction in applying that policy.
- **Public-domain provenance:** DOE’s policy supports the government-information statement and acknowledgement request, while separately recognising potentially protected contributed material. The reference acknowledges third-party material, so I did not flag its bibliographic licensing statement. [DOE Web Policies](https://www.energy.gov/web-policies)
- **Post-source vocabulary and invented research verdicts:** No confirmed temporal vocabulary anachronism, fabricated study result, sample-size change, sign reversal or significance-level alteration was found.