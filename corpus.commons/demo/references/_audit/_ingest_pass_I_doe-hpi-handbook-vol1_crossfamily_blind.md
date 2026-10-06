## 1. What I read

**Blind audit outcome: corrections required.** No files were edited, and I did not read the parallel auditor’s findings.

Read in full:

- `blind-brief.md`, the three calibration fixtures, and `pass-i-spec.md`, in the prescribed order.
- `frozen-deep.md`, lines 1–363.
- `tape.md`, lines 1–12,939, including front matter, all five chapters, attachments, appendix, references, glossary, and concluding material.
- `source-card.md`, lines 1–23.
- The repository’s operating instructions, required architecture documents, and written ingestion procedure.

Read in part:

- `source.pdf`: 23 pages visually inspected—PDF pages 14–17, 22, 42, 47, 50–51, 84, 93, 97, 109, 113, 120, 126–131, 134 and 160—plus metadata and the final page’s extracted text. I did not independently reread the entire PDF.
- `check-verbatim.py`: quotation extraction and normalisation sections.
- DOE’s web policies for the provenance statements. The stated PDF URL was accessible; the landing-page URL could not be verified through the browser tool.

The frozen reference’s SHA-256 matches `frozen-deep.sha256`. The original PDF’s SHA-256 matches the source card. Its 175 pages, byte size, and the reported 64,289-word `pdftotext` count also check out.

Below, **D** means `frozen-deep.md` line; **T** means `tape.md` line. Page numbers are the handbook’s locators.

## 2. Findings

1. **D18 and D82 — incomplete citation range.**  
   The introductory citations locate all five principles on p. 1-19. Principles four and five are on p. 1-20: T1707–1732.  
   **Exact fix:** replace these introductory `(Ch 1, p. 1-19)` citations with `(Ch 1, pp. 1-19 to 1-20)`. The individual citations at D87–88 are already correct.

2. **D102 — unsupported coverage assertion.**  
   “Each with a historical example” is inaccurate. The Pollyanna entry explains the attitude but supplies no historical incident: T2143–2151, p. 2-6.  
   **Exact fix:** replace the opening with:  
   “The handbook names six unsafe attitudes and illustrates several with historical examples [AE] (Ch 2, pp. 2-5 to 2-6):”

3. **D125 — reversed numerical direction.**  
   Error likelihood does not fall from one in a million to one in a thousand; it increases. The source explicitly says so and conditions the first probability on complete independence: T2587–2597, p. 2-12.  
   **Exact fix:** replace the logic-example sentence with:  
   “The handbook’s logic example assumes complete independence between a maintenance technician and the supervisor checking the work, giving an overall error likelihood of one in a million. If the supervisor assumes competence and does not closely check, the likelihood increases to one in a thousand [BT] (Ch 2, p. 2-12, endnote 35).”

4. **D159 — dropped exception.**  
   The precursor list includes irreversible actions without preserving the source’s qualification that these are **not necessarily error precursors**. They are included because they are important and often overlooked: T4591–4592 and T5002–5003, pp. 2-32 and 2-37.  
   **Exact fix:** add after the list:  
   “Irreversible actions are not necessarily error precursors; the handbook includes them because they are often overlooked, leading to preventable events [BT] (Ch 2, p. 2-32; Att. A, p. 2-37).”

5. **D221, with consequences for D7 and D359 — borrowed-through attribution failure.**  
   The quotation beginning “managers will unconsciously reinforce getting the job done” is labelled `[V]` and covered by the assurance that all such quotations are the handbook’s own prose. Endnote 8 explicitly identifies the passage as adapted from a quotation by Erik Hollnagel: T8096–8100 and T10606–10608, pp. 4-4 and 4-33. Its wording matches the tape, but its treatment contradicts the reference’s declared third-party rule.  
   **Exact fixes:**
   - Replace that quoted clause at D221 with:  
     “Drawing on a quotation from Hollnagel, the handbook argues that failing to establish safety as a core value can reinforce getting the job done and make production the default value [BT] (Ch 4, p. 4-4, endnote 8).”
   - Add to D7’s third-party inventory:  
     “the Ch 4, p. 4-4 passage adapted from a quotation by Erik Hollnagel (endnote 8)”.
   - **Strip** “All `[V]` quotations are the handbook’s own prose” from D359.

6. **D322 — unsupported bibliographic expansion.**  
   The source cites Dekker and “Dekker, S.”, but does not supply “Sidney”: T7882 and T11906, pp. 3-28 and 5-21.  
   **Exact fix:** replace `Sidney Dekker` with `Dekker`. Retain the work and substantive connection.

7. **D324 — unsupported bibliographic expansion.**  
   The source cites Daniels but does not supply “Aubrey”: T1797, T10632, T10634 and T10638.  
   **Exact fix:** replace `Aubrey Daniels` with `Daniels`.

8. **D326 — unsupported bibliographic expansion.**  
   The source supplies “Wickens, C.D.” but not “Christopher”: T5521–5524 and T5552–5554.  
   **Exact fix:** replace `Christopher Wickens` with `Wickens (C.D.)`.

9. **D328 — unsupported bibliographic expansion.**  
   The source names Karl Weick, but supplies only Sutcliffe/Sutcliff’s surname: T11445, T11502, T5418 and T11939–11957. “Kathleen” is absent.  
   **Exact fix:** replace `Karl Weick and Kathleen Sutcliffe` with `Karl Weick and Sutcliffe`.

10. **D344 — silent reversal of the cited source.**  
    “It only lengthens the time between events” reverses the actual sentence on the cited page, which says “reduce the time between events”: T5847–5853, p. 3-3. The source’s frequency-reduction argument elsewhere makes the intended meaning understandable, but a source-only reference should not silently correct this wording.  
    **Exact replacement:**  
    “*Error reduction alone.* Focusing only on error reduction to prevent events is ‘a bad strategy’; the chapter instead emphasises defence-in-depth and verifying control integrity to minimise event severity (Ch 3, p. 3-3).”

11. **D8 and D361 — inaccurate layout provenance.**  
    “Managing Defenses” appears in Chapter 3’s running **header**, not its footer. This is visible on original PDF p. 93, handbook p. 3-13; compare T6526–6530.  
    **Exact fix:** replace `running footer` with `running header` at both locations.

12. **D357 and source-card L19 — inaccurate layout description.**  
    The ISM–HPI integration table has three columns. The production/prevention text wraps around a figure rather than forming an ordinary two-column sidebar. Original PDF pp. 14–17 and 120 establish both layouts.  
    **Exact fixes:**
    - Replace D357’s opening layout description with:  
      “Multi-column tables and text wrapped around figures lose their spatial reading order in the conversion. The ISM–HPI integration table (Ch 1, pp. 1-6 to 1-9) has three columns, and the production/prevention paragraph (Ch 4, p. 4-12) wraps around a figure.”
    - In source-card L19, replace `Two-column tables, the Ch 4 production/prevention sidebar` with `Multi-column tables and the Ch 4 production/prevention paragraph wrapped around a figure`.

13. **D357 — false quotation-handling assurance.**  
    “No `[V]` quotation … is taken from an interleaved table, sidebar or figure” is contradicted by D42’s quotation from the ISM table, “on problems beyond the individual”, and D229’s “the quiet non-events” from the production/prevention passage: T1132–1148 and T8606–8636.  
    **Exact fix:** replace the final two sentences of D357 with:  
    “The reference quotes a short phrase from the ISM–HPI table (p. 1-9) and from the production/prevention discussion (p. 4-12). Figure descriptions are paraphrased.”

14. **D300 — dropped statistical conditions and denominator.**  
    The `<1 in 10,000` estimate is explicitly **under ideal conditions**, from a nuclear-power study. The 25% share concerns errors in the nuclear-power industry; the 90% figure concerns a person’s daily activities: T3874–3878, p. 2-23.  
    **Exact replacement row:**
    ```markdown
    | Skill-based mode: error chance; share of daily activity; share of nuclear-power errors | <1 in 10,000 under ideal conditions, according to a nuclear-power study; ~90% of a person's daily activities; 25% of nuclear-power errors | [BT] (Ch 2, p. 2-23), endnotes 66–68 |
    ```

15. **D301 — omitted statistical setting.**  
    The 60% share concerns nuclear-power errors, and the probability discussion concerns reduced familiarity: T3986–3990, p. 2-24.  
    **Exact replacement row:**
    ```markdown
    | Rule-based mode: error chance with less familiarity; share of nuclear-power errors | ~1 in 1,000; ~60% of nuclear-power errors | [BT] (Ch 2, p. 2-24), endnotes 75–76 |
    ```

16. **D302 — omitted statistical setting.**  
    The 15% share concerns nuclear-power errors. The probability estimate concerns unfamiliar knowledge-based situations: T4124–4138 and T4148–4150, pp. 2-26 to 2-27.  
    **Exact replacement row:**
    ```markdown
    | Knowledge-based mode in unfamiliar situations: error chance; share of nuclear-power errors | ~1 in 2 to 1 in 10; ~15% of nuclear-power errors | [BT] (Ch 2, pp. 2-26 to 2-27), endnotes 83–84 |
    ```

17. **D303 — omitted probability assumption.**  
    The one-in-a-million value belongs to an illustration assuming complete independence between technician and supervisor. “Checked vs unchecked” alone loses that condition: T2587–2594, p. 2-12; original PDF p. 42.  
    **Exact replacement row:**
    ```markdown
    | Team-error illustration: independent technician and supervisor checks vs no close supervisor check | 1 in 1,000,000 assuming complete independence; 1 in 1,000 without close supervisor checking | [BT] (Ch 2, p. 2-12), endnote 35 |
    ```

18. **D236 and D308 — omitted historical research setting.**  
    The aviation percentages are introduced as findings from research conducted in the late 1970s: T8769–8772, p. 4-13. Both summaries omit that setting.  
    **Exact fixes:**
    - At D236, replace `Aviation research found` with `Aviation accident research conducted in the late 1970s found`.
    - At D308, replace the metric cell with:  
      `Aviation accident research conducted in the late 1970s: crew failures in interpersonal communication, decision-making and leadership`
    - Retain the three percentages and existing citation.

19. **D363 — overbroad page-anchor assurance.**  
    The footers do not occur on “every page”. The final PDF page has no printed page number, although the TOC assigns Concluding Material p. xi: T302 and T12870–12939; original PDF p. 175.  
    **Exact replacement:**  
    “**Citation style.** `(Ch N, p. N-M)` using the handbook’s printed page numbers, which survive as footers on numbered pages. The TOC lists Concluding Material as p. xi; the final PDF page has no printed page number.”

20. **D108 — dropped modal and conditional qualifiers.**  
    The paraphrase makes automatic behaviour and an eventual event categorical. The source says at-risk behaviours **can** become automatic and an event occurs **under the right circumstances**: T2258–2264, p. 2-7.  
    **Exact fix:** replace the clause following the “Persistent use” quotation with:  
    “Without correction, at-risk behaviours can become automatic; over time people begin to underestimate hazards and the possibility of error, and under the right circumstances an event occurs [AP] (Ch 2, p. 2-7).”  
    Retain the subsequent quotation about managerial feedback.

21. **D221 — hypothetical illustration generalised into a causal assertion.**  
    The robust-system passage presents successive barrier failures without retaining the author’s assumed scenario: an operational hazard coexists with a strong belief that the system is robust. T7998–8008, p. 4-2, explicitly introduces that scenario.  
    **Exact replacement for the opening sentence:**  
    “The handbook illustrates how an operational hazard, combined with a strong shared belief that the system is robust, can undermine successive barriers: defective equipment is left unfixed, procedures are skipped, minor problems go unreported, and non-conservative decisions are made under uncertainty [BT] (Ch 4, p. 4-2, endnote 4 to Packer).”

22. **D243 — dropped uncertainty qualifier.**  
    “Greater cost” is categorical; the source says the cost of corrective actions addressing individual factors **will likely** be greater: T9151–9154, p. 4-18.  
    **Exact fix:** replace `have less immediate influence and greater cost` with `have less immediate influence and are likely to cost more`.

23. **D279 — dropped boundary on decision migration.**  
    The Berkeley finding does not simply put decisions at the lowest level. It specifies the lowest level **consistent with decision implementation**: T11464–11466, p. 5-13.  
    **Exact fix:** replace `decisions that migrate to the lowest level` with `decisions that migrate to the lowest level consistent with their implementation`.

24. **D118 — absence of an apparent outcome changed into absence of an outcome.**  
    Latent errors have “no immediate **apparent** outcome to the facility or to personnel”: T2349–2354, p. 2-9. Removing “apparent” obscures the distinction between hidden effects and no effects.  
    **Exact fix:** replace `They have no immediate outcome` with `They have no immediate apparent outcome to the facility or personnel`.

## 3. Count and required conclusions

**Checked:** 182 claim-bearing units in the deep reference, counted at paragraph, list-item and table-row level. Composite units were traced clause by clause; 182 is not an asserted count of atomic propositions.

This included:

- 420 operative evidence markers: 188 `[V]`, 94 `[AP]`, 126 `[BT]` and 12 `[AE]`.
- 195 quotation spans extracted by the checker.
- All 18 statistics rows, including their values, sample descriptions and citations.
- All 22 connection entries and 12 explicitly opposed positions.
- All source-integrity notes and the source card’s provenance fields.

**24 numbered findings**, grouped by primary problem class:

| Problem class | Findings |
|---|---:|
| Incomplete citation range | 1 |
| Unsupported bibliographic name expansions | 4 |
| Unsupported coverage assertion | 1 |
| Dropped qualifiers, conditions or settings | 11 |
| Reversed direction or silent source correction | 2 |
| Borrowed-through attribution failure | 1 |
| Inaccurate conversion or layout assurances | 4 |
| **Total** | **24** |

Repeated occurrences of the same defect are grouped within a finding.

**Quotations:** the deterministic checker reported no mismatches. There are no blockquotes. A stricter comparison identified only the nested quotation-mark changes at D18 and D257, discussed below.

**Key statistics:** all printed numerical values and sample sizes match the tape. The table needs the contextual repairs in findings 14–18. I found no altered significance level or fabricated numerical result.

**Coverage:** no chapter or substantive attachment/appendix is absent from the reference’s anchor coverage. All five chapters, Chapter 2 Attachments A–B, Chapter 3 Appendix A, Chapter 4 Attachments A–C, and the glossary are represented.

**Author-stated limitations:** there is no separate limitations list to validate. The represented boundaries—particularly that this is not a human-factors manual or a modification of existing safety requirements—match T365–369. The conversion observations are editorial provenance notes, not limitations stated by the authors.

## 4. Over-flag guard

- **D16’s “reduce the time between events”: clean as a quotation.** T5850 contains precisely that wording. Its inconsistency with the frequency-reduction argument does not justify changing the quotation. D344’s silent reversal is the defect.
- **D18 and D257’s nested quotation marks: clean.** Inner double quotation marks become single marks inside the outer quotation. The words and sentence punctuation match; the supplied checker expressly permits this nesting convention.
- **Other smart-quote differences: clean.** Straight/curly quotation marks and apostrophes do not change the quoted content.
- **“Classic” at D171: clean.** The handbook itself calls Chernobyl a classic example, T5753–5755. This is not an inserted evaluative label.
- **The BEM leverage and cost discussion: source-grounded.** T9145–9154 supplies the comparison. Only the lost “likely” qualifier requires correction.
- **D78’s “four” followed by five control categories: preserved source inconsistency.** T1571–1573 says four, while T1575–1639 supplies five headings. I did not count faithful reproduction as an invented quantity.
- **D299’s NRC-study row: clean.** It remains bounded to 35 events over six years and accurately reports 270 errors and the 81%/19% split.
- **D309’s approximate blameless-act percentage: clean.** The approximation preserves the tentative numerical character of “perhaps 90 percent or more”, T10503–10504.
- **The twelve “frames against” entries: grounded.** Each corresponds to an explicit criticism, warning or distinction in the source; none requires inventing an opposing school.
- **Recommendations concerning retraining, investigations, reporting and leadership: legitimate source prescriptions.** Their imperative content does not make them task-application guidance inserted by the ingester.
- **The named authors and works themselves: cited by the source.** Findings 6–9 concern unsupported first-name expansions, not fabricated author connections.
- **Reported source inconsistencies: substantially supported.** Chapter-title discrepancies, erroneous internal cross-references, attachment naming, the working-memory expressions and the two strategic formula forms occur in the tape.
- **Provenance measurements and permission statements: supported.** Checksums, page count and word counts match. The ISPI and Mager/Pipe permission statements occur at T10654–10679. DOE’s public-domain and acknowledgement policy wording also checks out. [DOE Web Policies](https://www.energy.gov/web-policies).
- **Historical ingestion assertions remain records, not independently proven events.** The supplied brief identifies `markitdown 0.1.5`; the files alone cannot independently establish the download date or verify every unsupplied light reference and distillation. I have not treated that evidential limit as proof those records are false.