## 1. What I read

Read in full:

- `sort-brief.md`, `pass-i-spec.md`, and all three calibration fixtures.
- `blind-findings.md` and `fixer-audit-log.md`.
- `post-audit-deep.md`, all 363 lines.
- `source-card.md`, repository operating instructions, and the required architecture documents.

Also examined:

- Every changed passage in `frozen-deep.md`, through the complete before/after diff.
- The full source TOC and the tape passages supporting every ledger decision below, supplemented by full-file searches. I did not reread the entire tape end to end.
- Original PDF pages 14, 17, 93, 120 and 175 visually. :codex-file-citation{path="_planning/pass-i/demo/doe-hpi-handbook-vol1/source.pdf" purpose="source"}

The post-audit reference matches its supplied SHA-256: `1751c6f2182c2c36c00931bcf19065da65ce169206fd05775f7d817d812be817`. The original PDF matches the source-card checksum. The deterministic verbatim checker, run against `tape.md`, reports no findings.

No files were edited.

## 2. Sorted ledger

**Notation:** **B** identifies a blind-audit finding; **F** identifies a numbered fixer-log change. **P** means `post-audit-deep.md` line; **T** means `tape.md` line. Duplicate findings are combined; separable issues are distinguished.

### Confirmed and fixed

| Finding | Post-audit location | Source anchor | Decision |
|---|---|---|---|
| B6 / F5: “Sidney” Dekker | P322 | T7882, T11906; pp. 3-28, 5-21 | Unsupported first-name expansion correctly removed. |
| B7 / F5: “Aubrey” Daniels | P324 | T1797, T10632–10638 | Unsupported first-name expansion correctly removed. |
| B8 / F5: “Christopher” Wickens | P326 | T5521–5524, T5552–5554 | Unsupported first-name expansion correctly removed. Retaining the surname alone is sufficient; adding the supplied initials is optional. |
| B9 / F6: “Kathleen” Sutcliffe | P328 | T5418, T11445, T11939–11957 | Unsupported first-name expansion correctly removed. |
| F6: Preface citation for the named HRO authors | P328 | T308–363, T1744–1749, T11441–11452 | The Preface introduces HROs without naming these authors. Replacing that locator with Ch 1, endnote 2 is correct; the retained Ch 5 range supports the other names. |
| F4: quoted Reason passage | P86 | T1693–1697; endnote at T1793 | Correctly paraphrased under the reference’s declared third-party rule. The original `[BT]` marker identified provenance but did not make a quotation comply with “paraphrase only”. |
| B13 / F8: blanket assurance about quotations from interleaved material | P357; quotation at P42 | T1132–1148; p. 1-9; original PDF p. 17 | Correctly repaired by acknowledging the integration-table quotation. “The quiet non-events” at P229 comes from body prose above the figure, not from the figure itself. The narrower current assurance does not exclude that prose. |

### Confirmed, fix wrong or incomplete

| Finding | Post-audit location | Source anchor | Decision |
|---|---|---|---|
| B12 / F7: inaccurate layout description | P357 | Integration table, pp. 1-6 to 1-9, original PDF pp. 14 and 17; production/prevention passage, T8591–8636, original PDF p. 120 | Changing “sidebar” to prose wrapped around a figure is correct. “Two-column layouts” remains inaccurate: the integration table has three columns. The source-card counterpart at line 19 also remains inaccurate, but is outside the requested post-audit edit list. |
| Fixer’s open item: CAIB rights assertion | P7 | T5464; Ch 2, endnote 23 | The tape identifies the CAIB report but does not establish its legal status. Under the supplied trace-every-claim standard, the unsupported rights assertion must be removed. This decision concerns its source support, not whether the legal assertion is true. The fixer recognised the issue but left it unresolved. |

### Missed by the fix-in-place audit

| Finding | Post-audit location | Source anchor | Decision |
|---|---|---|---|
| B1, summary occurrence | P18 | T1654–1732; pp. 1-19 to 1-20 | The five-principle summary needs both pages. The separate objection to P82 is over-flagged below. |
| B2: historical example for every unsafe attitude | P102 | T2143–2151; p. 2-6 | Pollyanna has an explanation but no historical incident. “Each” is unsupported. |
| B3: numerical direction | P125 | T2587–2597; p. 2-12 | Error likelihood **increases**, rather than falls, from one in a million to one in a thousand. Complete independence is also an explicit assumption. |
| B4: irreversible-actions exception | P159 | T4591–4592, T5002–5003; pp. 2-32, 2-37 | The list drops the author’s qualification that irreversible actions are not necessarily error precursors. |
| B5: Hollnagel attribution and third-party handling | P221, P7, P359 | T8096–8100, T10606–10608; pp. 4-4, 4-33 | Endnote 8 explicitly identifies adaptation from a Hollnagel quotation. The retained `[V]` passage violates the declared paraphrase rule, and the inventory and assurance need corresponding repairs. |
| B10: silent reversal of the source | P344 | T5847–5853; p. 3-3 | “Lengthens” silently reverses the source’s “reduce”. Preserve the underlying controls argument without silently correcting that sentence. P16’s verbatim quotation remains accurate. |
| B11: running footer/header | P8, P361 | T6526–6530; original PDF p. 93, handbook p. 3-13 | “Managing Defenses” is in the running **header**. |
| B14: skill-based statistical conditions | P300 | T3874–3878; p. 2-23 | Restore ideal conditions, the nuclear-power study setting, and the distinct denominators for daily activities and errors. |
| B15: rule-based statistical setting | P301 | T3986–3990; p. 2-24 | Restore reduced familiarity and the nuclear-power error denominator. |
| B16: knowledge-based statistical setting | P302 | T4124–4138, T4148–4150; pp. 2-26 to 2-27 | Restore the unfamiliar-situation context and nuclear-power error denominator. |
| B17: team-error probability assumption | P303 | T2587–2594; p. 2-12 | “Checked vs unchecked” does not preserve complete independence or the source’s distinction between checking and closely checking. |
| B18: historical aviation research setting | P236, P308 | T8769–8783; pp. 4-13 to 4-14 | The percentages are historical research findings from the late 1970s. Restore that setting in both occurrences. |
| B19: page-anchor assurance | P363 | T302, T12870–12939; original PDF p. 175 | Printed page-number footers do not occur on every page. The final page is unnumbered; the TOC assigns concluding material p. xi. |
| B20: modal and conditional qualifiers | P108 | T2258–2264; p. 2-7 | Restore “can become automatic” and “under the right circumstances”. |
| B21: assumed robust-system scenario | P221 | T7998–8008; p. 4-2 | The categorical causal summary drops the assumed operational hazard and turns an illustration into an unrestricted assertion. |
| B22: corrective-action cost qualifier | P243 | T9145–9154; p. 4-18 | The source says costs will **likely** be greater. |
| B23: decision-migration boundary | P279 | T11464–11466; p. 5-13 | Restore “consistent with decision implementation”. |
| B24: apparent outcome | P118 | T2349–2354; p. 2-9 | No immediate **apparent** outcome is materially different from no immediate outcome. |

### Over-flagged

| Auditor/finding | Post-audit location | Source anchor | Decision |
|---|---|---|---|
| Blind B1, introduction occurrence | P82 | T1654–1661; p. 1-19 | P82 describes the principles as underlying truths and foundations for promoted behaviours. That introductory claim is supported on p. 1-19. Principles four and five have their own correct p. 1-20 citations at P87–88. No correction is required at P82. |
| Fixer F3 and F9 | P78, P361 | T1571–1573, T1575–1639; pp. 1-17 to 1-18 | The original “four” followed by five items faithfully preserved the source’s inconsistency. Treating that as a reference defect over-flags it. The fixer’s clarification and added inconsistency note are nevertheless accurate and can remain. Counted once. |

### Disputed

| Finding | Post-audit location | Source anchor | Both readings |
|---|---|---|---|
| F1: “two operating consequences that recur” | P18 | T4172–4221; pp. 2-27 to 2-28; T10185–10195, p. 4-26 | **Stricter reading:** “two operating consequences” attributes an organising formulation to the handbook, and “recur” overstates the distribution of its performance-mode response discussion. **Permissive reading:** this is a thesis synthesis of two explicit prescriptions, with supporting citations, rather than a claim that the handbook formally enumerates them. The replacement is source-supported and resolves the ambiguity; retain it. |
| F2: “INPO responded” | P52 | T1242–1250; p. 1-11 | **Stricter reading:** its position after the NRC/INEEL findings implies that INPO developed tools in response to that study. The source does not say this. **Permissive reading:** “responded” can mean responding to engineers’ different error patterns, which the source explicitly states. The replacement supplies the explicit reason and is accurate; retain it. |

### Additional defect found during the sort

| Finding | Post-audit location | Source anchor | Decision |
|---|---|---|---|
| S1: chapter headers on “every page” | P355 | T1–32, T306–308, T12866–12870; original PDF p. 175 | The quoted chapter-header pattern does not occur on every page. This is a pre-existing provenance overstatement, not a defect introduced by the fixer. |

**Introduced-defect check:** no new defect found in the fixer’s edits. The unresolved two-column description predates the edits. The revised table-quotation assurance, wrapped-prose reconstruction, surname removals and added controls inconsistency are source-supported.

## 3. Remaining edits

These are exact changes to `post-audit-deep.md`. Line numbers refer to the supplied, unchanged file.

1. **P7 — add Hollnagel to the third-party inventory.**  
   Current:
   > the Daniels consequence model (Ch 4, p. 4-15),

   Replacement:
   > the Daniels consequence model (Ch 4, p. 4-15), the passage adapted from a quotation by Erik Hollnagel (Ch 4, p. 4-4, endnote 8),

2. **P7 — remove the unsupported CAIB rights assertion.**  
   Current:
   > The CAIB report the handbook cites (Ch 2, endnote 23) is itself a US Government work; the handbook's own sentences about Columbia are quotable.

   Replacement:
   > The handbook cites the Columbia Accident Investigation Board Report (Ch 2, endnote 23).

3. **P8 and P361 — correct header location.**  
   Current at both locations: `running footer`  
   Replacement: `running header`

4. **P18 — widen only the five-principle summary citation.**  
   Current first citation: `(Ch 1, p. 1-19)`  
   Replacement: `(Ch 1, pp. 1-19 to 1-20)`

5. **P102 — correct historical-example coverage.**  
   Current:
   > The handbook names six unsafe attitudes, each with a historical example [AE] (Ch 2, pp. 2-5 to 2-6):

   Replacement:
   > The handbook names six unsafe attitudes and illustrates several with historical examples [AE] (Ch 2, pp. 2-5 to 2-6):

6. **P108 — restore modal and conditional boundaries.**  
   Current:
   > ; without correction they become automatic, risk is underestimated, and eventually an event occurs, so

   Replacement:
   > ; without correction, at-risk behaviours can become automatic. Over time, people begin to underestimate hazards and the possibility of error, and under the right circumstances an event occurs [AP] (Ch 2, p. 2-7).

   Retain the following quotation beginning “Managers and supervisors”.

7. **P118 — restore “apparent”.**  
   Current: `They have no immediate outcome`  
   Replacement: `They have no immediate apparent outcome to the facility or personnel`

8. **P125 — correct direction and assumptions.**  
   Current:
   > A logic example shows a supervisor's independent check giving one-in-a-million error likelihood, falling to one in a thousand if the supervisor assumes competence and does not check [BT] (Ch 2, p. 2-12, endnote 35).

   Replacement:
   > The handbook's logic example assumes complete independence between a maintenance technician and the supervisor checking the work, giving an overall error likelihood of one in a million. If the supervisor assumes competence and does not closely check, the likelihood increases to one in a thousand [BT] (Ch 2, p. 2-12, endnote 35).

9. **P159 — restore the irreversible-actions exception.**  
   Current:
   > Some organisations give front-line workers a precursor card for pre-job briefings

   Replacement:
   > Irreversible actions are not necessarily error precursors; the handbook includes them because they are often overlooked, leading to preventable events [BT] (Ch 2, p. 2-32; Att. A, p. 2-37). Some organisations give front-line workers a precursor card for pre-job briefings

10. **P221 — restore the assumed scenario.**  
    Current:
    > A shared belief that the system is robust is dangerous: it leads people to leave defective equipment unfixed, skip procedures, fail to report minor problems, and make non-conservative decisions under uncertainty, so physical, people, learning and "last chance" barriers fail in turn [BT] (Ch 4, p. 4-2, endnote 4 to Packer).

    Replacement:
    > The handbook illustrates how an operational hazard, combined with a strong shared belief that the system is robust, can undermine successive barriers: defective equipment is left unfixed, procedures are skipped, minor problems go unreported, and non-conservative decisions are made under uncertainty [BT] (Ch 4, p. 4-2, endnote 4 to Packer).

11. **P221 — paraphrase and attribute the Hollnagel adaptation.**  
    Current:
    > and that without safety as a demonstrated core value, "managers will unconsciously reinforce getting the job done, with production becoming the default core value" [V] (Ch 4, p. 4-4).

    Replacement:
    > and, drawing on a quotation from Hollnagel, argues that failing to establish safety as a core value can reinforce getting the job done and make production the default value [BT] (Ch 4, p. 4-4, endnote 8).

12. **P236 — restore research date and subject.**  
    Current: `Aviation research found`  
    Replacement: `Aviation accident research conducted in the late 1970s found`

13. **P243 — restore uncertainty about costs.**  
    Current: `have less immediate influence and greater cost`  
    Replacement: `have less immediate influence and are likely to cost more`

14. **P279 — restore the decision-migration boundary.**  
    Current: `decisions that migrate to the lowest level`  
    Replacement: `decisions that migrate to the lowest level consistent with their implementation`

15. **P300 — replace the statistics row.**

    Current:
    ```markdown
    | Skill-based mode: error chance; share of daily activity; share of errors | <1 in 10,000; ~90%; 25% | [BT] (Ch 2, p. 2-23), endnotes 66–68 |
    ```

    Replacement:
    ```markdown
    | Skill-based mode: error chance; share of daily activity; share of nuclear-power errors | <1 in 10,000 under ideal conditions, according to a nuclear-power study; ~90% of a person's daily activities; 25% of nuclear-power errors | [BT] (Ch 2, p. 2-23), endnotes 66–68 |
    ```

16. **P301 — replace the statistics row.**

    Current:
    ```markdown
    | Rule-based mode: error chance; share of errors | ~1 in 1,000; ~60% | [BT] (Ch 2, p. 2-24), endnotes 75–76 |
    ```

    Replacement:
    ```markdown
    | Rule-based mode: error chance with less familiarity; share of nuclear-power errors | ~1 in 1,000; ~60% of nuclear-power errors | [BT] (Ch 2, p. 2-24), endnotes 75–76 |
    ```

17. **P302 — replace the statistics row.**

    Current:
    ```markdown
    | Knowledge-based mode: error chance; share of errors | ~1 in 2 to 1 in 10; ~15% | [BT] (Ch 2, pp. 2-26 to 2-27), endnotes 83–84 |
    ```

    Replacement:
    ```markdown
    | Knowledge-based mode in unfamiliar situations: error chance; share of nuclear-power errors | ~1 in 2 to 1 in 10; ~15% of nuclear-power errors | [BT] (Ch 2, pp. 2-26 to 2-27), endnotes 83–84 |
    ```

18. **P303 — replace the statistics row.**

    Current:
    ```markdown
    | Team-error example: checked vs unchecked supervisor verification | 1 in 1,000,000 vs 1 in 1,000 | [BT] (Ch 2, p. 2-12), endnote 35 |
    ```

    Replacement:
    ```markdown
    | Team-error illustration: independent technician and supervisor checks vs no close supervisor check | 1 in 1,000,000 assuming complete independence; 1 in 1,000 without close supervisor checking | [BT] (Ch 2, p. 2-12), endnote 35 |
    ```

19. **P308 — restore historical research context in the metric cell.**  
    Current:
    > Aviation accidents involving crew failures in communication, decision-making, leadership

    Replacement:
    > Aviation accident research conducted in the late 1970s: crew failures in interpersonal communication, decision-making and leadership

20. **P344 — remove the silent correction.**  
    Current:
    > - *Error reduction alone.* Focusing only on error reduction to prevent events is "a bad strategy", because it only lengthens the time between events (Ch 3, p. 3-3).

    Replacement:
    > - *Error reduction alone.* Focusing only on error reduction to prevent events is "a bad strategy"; the chapter instead emphasises defence-in-depth and verifying control integrity to minimise event severity (Ch 3, p. 3-3).

21. **P355 — narrow the header assurance.**  
    Current:
    > running headers ("Department of Energy / Human Performance Handbook / Chapter N …") repeat on every page.

    Replacement:
    > the conversion also preserves repeated chapter headers ("Department of Energy / Human Performance Handbook / Chapter N …").

22. **P357 — correct the remaining layout description.**  
    Current:
    > Two-column layouts did not: the ISM–HPI integration table (Ch 1, pp. 1-6 to 1-9) and the prose wrapped around the production/prevention figure (Ch 4, p. 4-12) interleave columns

    Replacement:
    > The three-column ISM–HPI integration table (Ch 1, pp. 1-6 to 1-9) and the prose wrapped around the production/prevention figure (Ch 4, p. 4-12) lose their spatial reading order in the conversion

23. **P359 — strip the false authorship assurance.**  
    Strip:
    > All `[V]` quotations are the handbook's own prose.

24. **P363 — correct page-anchor coverage.**  
    Current:
    > **Citation style.** `(Ch N, p. N-M)` using the handbook's printed page numbers, chosen because the converted text preserves them as footers on every page.

    Replacement:
    > **Citation style.** `(Ch N, p. N-M)` using the handbook's printed page numbers, which survive as footers on numbered pages. The TOC lists Concluding Material as p. xi; the final PDF page has no printed page number.

## 4. Counts

Counts use distinct issues, merging overlaps between auditors and repeated occurrences. B1 is split between its defective summary citation and clean introductory citation; F6 is split between the first-name expansion and wrong locator.

| Outcome | Count |
|---|---:|
| **Confirmed defects, total** | **28** |
| Confirmed and correctly fixed | 7 |
| Confirmed, fix incomplete or recognised but left unresolved | 2 |
| Missed blind findings still requiring correction | 18 |
| Additional pre-existing defect found during this sort | 1 |
| **Over-flagged by blind auditor** | **1** |
| **Over-flagged by fixer** | **1** |
| **Disputed** | **2** |
| Defects introduced by fixer edits | 0 |

“Missed” is a subset of confirmed defects, not an additional total. The 21 unresolved confirmed issues require the 24 numbered edit operations above.

## 5. Gate verdict

**After edits 1–24: PASS for the deep-reference source-fidelity gate.**

The current file **fails** because the confirmed residual defects remain. The replacements resolve them; the two disputed fixer changes are already expressed in source-supported wording. The TOC comparison reveals no missing chapter, substantive attachment, appendix or glossary coverage, and the quotation checker reports no textual mismatches.

Pass I stamping and re-derivation of the light reference and distillations remain the parent workflow’s required subsequent steps; this sort has not performed or certified them.