## 1. What I read

Read in full, in the required order: all three calibration fixtures, `pass-i-spec.md`, and `frozen-deep.md` (364 lines). Then read all of `tape.md` (1,210 lines), `source-card.md`, and the acquisition manifest named in the source card. Also read the brief and required repository instructions.

No audit source was read only in part. I did not read the parallel auditor’s findings or logs.

No original source files, pinned repository checkout, licence file or image were supplied in this folder. Consequently, the licence, commit date and completeness of the acquisition against the repository remain independently unverified; the acquisition manifest corroborates those assertions but is not the original evidence.

Both supplied hashes match their respective files. The prescribed verbatim checker, run against `tape.md`, reported no findings. I also checked the three substantive blockquotes manually.

**Outcome: corrections required.** Report returned here; the filesystem is read-only, so no report file or source file was changed.

## 2. Findings

1. **Deep-reference line 23 — incorrect quantity.**

   The Localisation page is described as containing “three sentences”. It contains five: two at tape line 1203, one at 1205, one at 1206 and one at 1208.

   **Exact fix:** replace `three sentences` with `five sentences`.

2. **Deep-reference line 108 — dropped qualifier broadens the claim.**

   The reference says the example scenario “does not go into what the software (here, the coworker) will do”. The source says it does not go into **the details of** what the software will do (tape lines 155–157). The scenario does describe actions by the coworker (149–152); the source’s distinction concerns detail and perspective.

   **Exact fix:** replace that sentence with:

   > The page points out that the scenario does not go into the details of what the software (here, the coworker) will do; it stays with the perspective of the person the Feature serves [AP].

3. **Deep-reference line 289 — incorrect example identity.**

   “Gjett et ord” is identified as a scenario name. It is the feature name, following `Funksjonalitet:` at tape line 995. The two scenario names follow `Eksempel:` at lines 997 and 1001. Although the source’s introductory sentence loosely calls the example a scenario (991), it does not identify “Gjett et ord” as a scenario title.

   **Exact fix:** replace `The page shows a Norwegian scenario, "Gjett et ord" [AE].` with:

   > The page shows a Norwegian feature, “Gjett et ord”, containing the scenarios “Ordmaker starter et spill” and “Gjetter blir med” [AE].

4. **Deep-reference line 359 — incorrect occurrence count.**

   The note reports four `<Term>` placeholders. There are five occurrences, using four distinct placeholder names: `file-extension` occurs twice, at tape lines 1025 and 1195; the others occur at 1032, 1034 and 1081.

   **Exact fix:** replace:

   > and four `<Term>` placeholders in the step-organization page (`file-extension`, `steps-file-pattern`, `domain-object`, `types-of-objects`)

   with:

   > and five `<Term>` occurrences in the step-organization page, using four distinct placeholder names (`file-extension`, `steps-file-pattern`, `domain-object`, `types-of-objects`)

5. **Source-card line 5 — unsupported publication metadata.**

   `publish_year: 2026` presents a publication year that neither the tape nor acquisition manifest establishes. The manifest supplies a repository snapshot date, 2026-10-08. A snapshot date does not establish when these documentation pages were published.

   **Exact fix:** replace `publish_year: 2026` with `publish_year: null`. Retain the separately recorded commit date.

## 3. Count and specific checks

**189 deep-reference claim-bearing units checked:** 153 prose, list-item, quotation or metadata units, plus all 36 cells across the 12 statistics rows. Constituent assertions, citations and evidence markers were checked within those units; this is a grouped count, not an atomic-clause count. The source card’s 13 metadata fields and remaining prose were also checked.

| Defect class | Count |
|---|---:|
| Incorrect quantities | 2 |
| Dropped qualifier / broadened claim | 1 |
| Incorrect example identity | 1 |
| Unsupported publication metadata | 1 |
| **Total** | **5** |

No additional evidence-marker, verbatim, numerical-value, cross-reference, task-application, post-source vocabulary or source-external analytical-framing defects were found.

**Key-statistics table:** all 12 rows match the tape’s values and classifications. Anchors checked include tape lines 33–41, 265, 269, 299–302, 616, 837, 484–485, 515/577, 989, 432 and 436–438. The table contains recommendations, syntax facts and historical assertions, not measured empirical results.

**Coverage:** all 12 acquired pages and every substantive source section have corresponding reference coverage. No missing-section failure was found within the declared subset. This does not independently establish that the acquisition contains every repository page in those two directories.

**Author-stated limitations:** there is no separate list purporting to reproduce the authors’ research limitations. Relevant qualifications are preserved: imperative tests suit some contexts; matching ignores step keywords; block comments are unsupported; and editor support for backticks and content types is incomplete. Missing rendered components and the uninspected image are identified as acquisition limitations, rather than attributed to the authors.

## 4. Over-flag guard

- **Source prescriptions in the deep tier:** clean. Workshop procedures, card colours, writing advice and helper-method recommendations are explicitly present in the source and attributed to it. They are not added task applications.
- **“Practitioner assertions” and “no demonstrated findings” (lines 32 and 362):** clean evidence classification. The tape supplies guidance and historical narration without reporting empirical studies.
- **Positions framed against (lines 346–353):** clean. The myths, implementation-detail criticism, database-check warning and named anti-pattern are explicit source positions.
- **Statistics row 320:** considered whether “more than 4 lines” became a mandatory threshold. The row labels it a tip, and line 261 retains “consider”; no additional defect recorded.
- **Workshop-size `[V]` row:** clean. “3-6 people” is exact, and the accompanying minimum-role statement is supported at tape line 265.
- **Blockquote punctuation:** clean. Quotation-delimiter and Markdown presentation aside, all three quoted passages match; no smart-quote normalisation was needed.
- **Named people, works and linked techniques:** clean. Each appears in the tape; the reference does not import the linked works’ contents.
- **Licence and acquisition assertions:** not labelled false merely because originals were unavailable. Their independent verification remains a stated limitation of this audit.