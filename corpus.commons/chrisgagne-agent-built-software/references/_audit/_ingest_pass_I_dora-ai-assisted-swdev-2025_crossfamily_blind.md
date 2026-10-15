## 1. What I read

Read in full:

- `blind-brief.md`, all three calibration fixtures, and `pass-i-spec.md`, before auditing the reference.
- `frozen-deep.md`: all 383 lines.
- `tape.md`: all 13,537 lines, covering all 142 PDF pages.
- `source-card.md` and `frozen-deep.sha256`.
- Repository operating instructions and the applicable source-integrity and evidence-classification rules.

Read in part: `source.pdf`, including its metadata and visual inspection of pages 1, 17, 18 and 142. Other PDF pages were checked through their complete deterministic text conversion.

The frozen reference’s SHA-256 matches its manifest. The PDF’s SHA-256 matches the source card. Re-running pdftotext produced text byte-for-byte identical to `tape.md`: 42,980 words and 142 form feeds.

This audit remained blind: I did not read the fixer’s findings. No files were edited.

**Decision: corrections required before the frozen reference passes.**

## 2. Findings

All reference line numbers below refer to `frozen-deep.md`.

### 1. Line 5 — incorrect version-location claim

**Problem class:** Provenance overstatement.

The reference says the version mark appears “in every page footer”. The cover and back cover have neither that mark nor a numbered footer.

**Evidence:** Original PDF pp. 1 and 142; tape lines 1–12 and 13,535–13,537. Page 141 does carry `v. 2025.2`.

**Exact fix:** Replace:

> version "v. 2025.2" (the version mark in every page footer and on p. 141)

with:

> version "v. 2025.2" (the version mark in the numbered-page footers, including p. 141)

### 2. Multiple lines — `[AE]` used for empirical findings rather than author examples

**Problem class:** Evidence-marker mismatch.

The repository taxonomy defines `[AE]` as **author example**, not author empirical evidence. The occurrences below mark paraphrased survey findings, aggregate research results or methodological facts. Their content is supported, but their classification is wrong.

Occurrence numbers are counted left to right **among `[AE]` markers on that line**. Retain the surrounding text, citations and other markers.

| Reference line | Occurrences to change | Source evidence | Exact fix |
|---|---:|---|---|
| 14 | Both | pp. 3–4: dataset description and survey dates | `[AE]` → `[AP]` |
| 16 | Both | pp. 4, 37–38: adoption statistics and adjusted comparisons | `[AE]` → `[AP]` |
| 18 | All three | pp. 60, 71, 78: moderation findings | `[AE]` → `[AP]` |
| 26 | All three | p. 4: executive-summary findings | `[AE]` → `[AP]` |
| 30 | Sole occurrence | p. 5: platform findings | `[AE]` → `[AP]` |
| 84 | First, third and fourth | pp. 24–25: adoption, experience and daily interaction time | `[AE]` → `[AP]` |
| 88 | First | p. 26: reflexive-use distribution | `[AE]` → `[AP]` |
| 92 | Both | p. 27: reliance and task-use distributions | `[AE]` → `[AP]` |
| 100 | Both | p. 29: interaction surfaces and modes | `[AE]` → `[AP]` |
| 104 | First three | pp. 30–31: productivity, code quality and trust distributions | `[AE]` → `[AP]` |
| 114 | Sole occurrence | p. 35: findings explicitly attributed to the 2024 report | `[AE]` → `[BT]` |
| 126 | Sole occurrence | p. 38: this year’s outcome comparisons | `[AE]` → `[AP]` |
| 136 | Sole occurrence | p. 41: no evidence of the tested moderating effect | `[AE]` → `[AP]` |
| 140 | Sole occurrence | p. 42: changes since 2024 | `[AE]` → `[AP]` |
| 147 | Sole occurrence | p. 45: authentic-pride finding | `[AE]` → `[AP]` |
| 148 | Sole occurrence | p. 45: meaningful-work finding | `[AE]` → `[AP]` |
| 149 | Sole occurrence | p. 45: need-for-cognition finding | `[AE]` → `[AP]` |
| 150 | Sole occurrence | p. 46: existential-connection finding | `[AE]` → `[AP]` |
| 151 | Sole occurrence | p. 46: psychological-ownership findings | `[AE]` → `[AP]` |
| 152 | Sole occurrence | p. 47: skill-ranking findings | `[AE]` → `[AP]` |
| 159 | Sole occurrence | p. 50: selection and testing of candidate capabilities | `[AE]` → `[AP]` |
| 163 | First | p. 52: AI-stance moderation findings | `[AE]` → `[AP]` |
| 167 | Sole occurrence | p. 54: data-ecosystem moderation finding | `[AE]` → `[AP]` |
| 171 | First | p. 55: internal-data moderation findings | `[AE]` → `[AP]` |
| 175 | Sole occurrence | p. 56: version-control moderation findings | `[AE]` → `[AP]` |
| 179 | Sole occurrence | p. 58: small-batch moderation findings | `[AE]` → `[AP]` |
| 183 | First | p. 60: user-focus moderation finding | `[AE]` → `[AP]` |
| 187 | Sole occurrence | p. 62: platform moderation findings | `[AE]` → `[AP]` |
| 197 | First | p. 66: findings explicitly attributed to the 2024 report | `[AE]` → `[BT]` |
| 197 | Second and third | pp. 66–67: current platform findings and adoption statistics | `[AE]` → `[AP]` |
| 201 | Sole occurrence | p. 67: platform-capability ratings | `[AE]` → `[AP]` |
| 209 | First and second | pp. 70–71: platform and AI moderation findings | `[AE]` → `[AP]` |
| 217 | Sole occurrence | p. 74: valuable-work finding | `[AE]` → `[AP]` |
| 231 | Both | pp. 77–78: VSM findings | `[AE]` → `[AP]` |
| 253 | Both | p. 88: aggregate findings from Beane’s research | `[AE]` → `[AP]` |
| 277 | All nine | pp. 103–112: respondent and interview-participant statistics | `[AE]` → `[AP]` |

**Count:** 60 marker corrections: 58 to `[AP]`, two to `[BT]`.

### 3. Line 88 — Sabre’s proficiency explanation loses its uncertainty qualifier

**Problem class:** Dropped qualifier.

The reference reports satisfaction and time savings “that grow with proficiency”. The source reports rising satisfaction and time savings and says this **suggests** benefits grow with proficiency.

**Evidence:** p. 26, tape lines 2,678–2,681.

**Exact fix:** Replace:

> satisfaction and time savings that grow with proficiency

with:

> rising satisfaction and reported time savings, suggesting that benefits grow as users become more proficient

### 4. Line 227 — an anticipated process delay becomes an actual process description

**Problem class:** Dropped hypothetical qualifier.

The interviewee asks whether a firewall-rule change will require a two- or three-week process. The reference turns that question into a description of such processes.

**Evidence:** p. 76: “Or, are we going to have to go through a two- or threeweek process every time we want, like, a firewall rule change?” The surrounding quotation concerns uncertainty, estimation and lack of control.

**Exact fix:** Replace the final sentence with:

> An interviewee describes uncertainty about estimation and asks whether even a firewall-rule change will require a two- or three-week process (p. 76) [AE].

### 5. Line 315 — reliance statistic loses its denominator

**Problem class:** Dropped population qualifier.

The 5% and 65% figures describe **AI users**, not the entire respondent population. The prose on line 92 preserves this denominator; the statistics row does not.

**Evidence:** p. 27, tape lines 2,711–2,728.

**Exact fix:** Replace the metric cell:

> Rely on AI: not at all / moderate or more

with:

> Reliance on AI among AI users: not at all / moderate or more

Retain the values and citation.

### 6. Line 329 — Sabre’s newer-feature uptake becomes an agent-mode rate

**Problem class:** Unsupported narrowing of a statistic.

Sabre reports that 25% of users leverage newer features **like agent mode**. That does not establish a measured agent-mode usage rate of 25%.

**Evidence:** p. 26, tape lines 2,682–2,685.

**Exact fix:** Replace the row with:

> | Sabre: developer adoption / users reporting productivity gains / users leveraging newer features such as agent mode | 74% / 86% / 25% | [V] (p. 26) |

The numerical transcriptions remain correct.

### 7. Line 330 — Adidas’s subgroup condition is omitted

**Problem class:** Finding stated more broadly than its reported setting.

The gains apply to pilot teams with loosely coupled architectures and fast feedback loops. The source contrasts them with tightly coupled ERP teams that saw little or no benefit. The table’s label currently presents the gains as an undifferentiated Adidas-pilot result.

**Evidence:** p. 10, tape lines 605–625.

**Exact fix:** Replace the metric cell:

> Adidas pilot (via *Vibe Coding*)

with:

> Adidas pilot: teams with loosely coupled architectures and fast feedback loops (via *Vibe Coding*)

Retain the values and classification.

### 8. Line 281 — the survey-experience subsection is missing

**Problem class:** Coverage omission.

The methodology summary covers question selection, localisation, recruitment and survey flows, but omits the separately headed **Survey experience** subsection.

**Evidence:** p. 113, tape lines 10,787–10,796 and 10,821–10,830. The authors describe cognitive interviews and usability tests, with targets for completion time, comprehension and effort.

**Exact fix:** Insert after the first sentence of line 281:

> The authors use cognitive interviews and usability tests to keep average survey completion time and effort low and questionnaire comprehension high (p. 113) [AP].

### 9. Line 383 — nonexistent Pass I stamp

**Problem class:** Incorrect audit-provenance claim.

The reference directs the reader to “the stamp on line 2”. Line 2 of the frozen reference is blank. The sentence therefore asserts an audit trail that this artefact does not contain.

**Evidence:** Frozen reference lines 1–3; verified frozen-file hash.

**Exact fix:** **Strip**:

> Pass I: see the stamp on line 2 and the audit log.

Do not replace it with a passing stamp before the audit is completed and logged.

## 3. Count and required checks

**Claims checked:** 163 compound claim-bearing blocks, including prose paragraphs, list entries, statistics rows, metadata and source-integrity notes. Each compound block was checked clause by clause; this is a block-grain count, not a claim that the reference contains only 163 atomic propositions.

Additional checks covered:

- **501 evidence-marker occurrences**, excluding the explanatory marker mention in the source-integrity notes.
- **24 key-statistics rows.**
- **12 positions framed against.**
- All contents entries and reference anchors.

| Defect class | Count |
|---|---:|
| Evidence-marker mismatches | 60 |
| Dropped qualifiers, denominators or setting restrictions | 5 |
| Incorrect provenance claims | 2 |
| Coverage omissions | 1 |
| **Total defect occurrences** | **68** |

The nine numbered findings group related occurrences. No changed numerical values, signs, credible-interval levels, invented cross-references, post-source vocabulary, independent task guidance or source-external analytical framing were found.

**Key-statistics table:** All reported numerical values match the tape. Three rows require contextual corrections: reliance’s AI-user denominator, Sabre’s newer-feature measure and Adidas’s subgroup condition.

**Author-stated limitations:** The limitations listed on line 287 match pp. 113, 115, 117 and 123. Elsewhere, the reference also preserves the authors’ limited-dataset qualification, snapshot qualification, early-stage sociocognitive cautions and first-iteration model status. I found no invented methodological limitation or verdict.

**Quotation check:** Running `check-verbatim.py` with `--source tape.md` reported no findings. There are no blockquotes. No defective inline quotation was found; ordinary extraction line wrapping was normalised, without rewriting wording or punctuation. The checker’s 18 unchecked figure claims were not treated as verified automatically.

## 4. Over-flag guard

- **Numerical `[V]` table entries:** Kept. The repository’s deep-reference template explicitly permits `[V]` statistics transcriptions. Regrouping correctly transcribed figures in a table is not, by itself, a paraphrased prose quotation.
- **Hypothetical examples, lines 40, 78, 223 and 245:** Kept. `[AE]` means author example; hypothetical cases qualify. They need not describe observed events.
- **Cluster profiles, lines 60–66:** Kept as author-created representative profiles. Their shares and descriptions match the source; pp. 17–18 were also checked visually.
- **Interview and company cases:** Their `[AE]` markers were retained where they identify cases or participant examples rather than aggregate findings.
- **“Empirical anchor”, “a myth”, “mature adoption”, “modest impact” and “risk compensation”:** Kept. These potentially evaluative expressions come from the source.
- **Nyquist statement:** Kept. Whatever its scientific merits, the report explicitly states it in the p. 10 footnote. This audit tests source fidelity.
- **Cluster 4’s inconsistent speed/stability description:** Kept. The inconsistency exists between the source’s pp. 17 and 19 and is disclosed on line 377.
- **78% certainty and 21% probability:** Kept. Both are printed on p. 46; their rounded sum is not an ingestion error.
- **“Comparisons” alongside causal wording:** Kept. Note 20 explicitly acknowledges occasional causal language while treating the analyses ultimately as comparisons.
- **Practical recommendations:** Kept where they report the authors’ recommendations. They are not independently generated task applications.
- **Chart-only omissions:** Kept within the declared text-only image scope. Every contents chapter is represented; the survey-experience subsection is the specific coverage omission identified above.
- **Historical process claims:** Fetch date, producing-model settings, operator image-scope approval and earlier rendering activity cannot be reconstructed from the frozen package alone. I have not presented those historical assertions as independently verified.