## 1. What I read

Read in full:

- `sort-brief.md`, `pass-i-spec.md` and all three calibration fixtures.
- `blind-findings.md` and `fixer-audit-log.md`.
- `post-audit-deep.md`, all 383 lines.
- `fixer-prompt.md`, `source-card.md` and `post-audit-deep.sha256`.
- Repository operating instructions and the required architecture documents; the evidence-classification taxonomy in `9-pass-protocol.md`.

**Source coverage for this sort was selective:** I independently read the complete tape pages supporting every finding: pp. 1–5, 10, 17, 19, 24–31, 35, 37–38, 41–42, 44–47, 50, 52, 54–56, 58, 60, 62, 66–67, 70–71, 74, 76–78, 88, 103–115 and 141–142. I visually inspected the cover and back cover of :codex-file-citation{path="_planning/pass-i/chrisgagne-agent-built-software/dora-ai-assisted-swdev-2025/source.pdf" purpose="source"}.

The frozen-to-post-audit diff contains exactly one change: `invited sidebars` → `signed sidebars`. The post-audit SHA-256 matches its manifest:

`1dc3fbb44daa3abf82bc223e7f70f46c1b5a1851d0d5ec1e64fbd5164db99db3`

I independently ran the verbatim checker: **no findings; 18 figure claims not checked**. That result does not certify those figure claims.

No files were edited.

## 2. Sorted ledger

All deep-reference line numbers refer to `post-audit-deep.md`. Marker occurrence numbers count only `[AE]` markers on the specified line, from left to right.

### Confirmed and fixed

| Finding | Deep line | Source | Raised by | Decision |
|---|---:|---|---|---|
| Unsupported characterisation of sidebars as “invited” | 7 | pp. 28, 44, 88 | Fixer | Confirmed and correctly fixed. Each sidebar has a named byline; the cited passages do not establish an invitation. “Signed sidebars” accurately describes them. |

### Confirmed, fix wrong or incomplete

**None.** The fixer’s sole edit correctly repairs the defect it identified.

### Missed by the fix-in-place audit: substantive and provenance defects

| Blind finding | Deep line | Source evidence | Raised by | Decision |
|---|---:|---|---|---|
| B1: version mark “in every page footer” | 5 | PDF pp. 1 and 142; tape pp. 1, 141–142 | Blind | Confirmed. Neither cover carries the version mark or a numbered footer. The version is printed on p. 141. |
| B3: Sabre benefits “grow with proficiency” | 88 | p. 26; tape 2678–2681 | Blind | Confirmed. Sabre says the trend **suggests** this explanation. The reference removes that uncertainty. |
| B4: actual two- or three-week firewall-change process | 227 | p. 76 | Blind | Confirmed. The interviewee asks whether such a process will be required; the reference presents it as an actual process description. |
| B5: reliance denominator omitted | 315 | p. 27; tape 2711–2728 | Blind | Confirmed. The 5% and 65% figures concern **AI users**. The table row must carry that denominator independently of the prose on line 92. |
| B6: 25% presented as agent-mode uptake | 329 | p. 26; tape 2682–2685 | Blind | Confirmed. The statistic covers newer features **such as** agent mode, rather than agent mode specifically. |
| B7: Adidas gains lose their subgroup restriction | 330 | p. 10; tape 605–625 | Blind | Confirmed. The gains concern teams with loosely coupled architectures and fast feedback loops. The source explicitly contrasts teams seeing little or no benefit. |
| B9: pointer to nonexistent stamp | 383 | Deep lines 1–3; line 2 is blank | Blind | Confirmed in the supplied snapshot. A future driver stamp does not make the current pointer accurate. The fixer reviewed and retained this sentence but did not raise it as a defect. |

The fixer’s prompt reserves stamping for the driver and prohibits editing a “Pass I has not run” line. That explains its caution, but the actual sentence claims a stamp already exists. This remains a blind-only capture.

### Missed by the fix-in-place audit: evidence-marker defects

The taxonomy defines `[AE]` as **author example**, not empirical evidence. Every occurrence below describes aggregate findings, research procedures or sample characteristics rather than a worked example or case. All **60 corrections** are confirmed: **58 to `[AP]`, two to `[BT]`**.

All rows were raised by the **blind auditor only** and remain unchanged.

| Deep line | `[AE]` occurrences | Source page(s) | Verified content | Replacement |
|---:|---|---|---|---|
| 14 | 1, 2 | 3–4 | Dataset description; survey dates | `[AP]` |
| 16 | 1, 2 | 4, 37–38 | Adoption findings; adjusted outcome comparisons | `[AP]` |
| 18 | 1–3 | 60, 71, 78 | User-focus, platform and VSM moderation findings | `[AP]` |
| 26 | 1–3 | 4 | Executive-summary findings | `[AP]` |
| 30 | 1 | 5 | Platform adoption and findings | `[AP]` |
| 84 | 1, 3, 4 | 24–25 | Adoption, experience and daily interaction time | `[AP]` |
| 88 | 1 | 26 | Reflexive-use distribution | `[AP]` |
| 92 | 1, 2 | 27 | Reliance and task-use distributions | `[AP]` |
| 100 | 1, 2 | 29 | Interaction surfaces and modes | `[AP]` |
| 104 | 1–3 | 30–31 | Productivity, code-quality and trust distributions | `[AP]` |
| 114 | 1 | 35 | Numerical findings attributed to the 2024 report | `[BT]` |
| 126 | 1 | 38 | Current outcome comparisons | `[AP]` |
| 136 | 1 | 41 | No evidence of the tested moderating effect | `[AP]` |
| 140 | 1 | 42 | Changes from the 2024 findings | `[AP]` |
| 147 | 1 | 45 | Authentic-pride finding | `[AP]` |
| 148 | 1 | 45 | Meaningful-work finding | `[AP]` |
| 149 | 1 | 45 | Need-for-cognition finding | `[AP]` |
| 150 | 1 | 46 | Existential-connection finding | `[AP]` |
| 151 | 1 | 46 | Psychological-ownership findings | `[AP]` |
| 152 | 1 | 47 | Skill-ranking findings | `[AP]` |
| 159 | 1 | 50 | Selection and testing of candidate capabilities | `[AP]` |
| 163 | 1 | 52 | AI-stance moderation findings | `[AP]` |
| 167 | 1 | 54 | Data-ecosystem moderation finding | `[AP]` |
| 171 | 1 | 55 | Internal-data moderation findings | `[AP]` |
| 175 | 1 | 56 | Version-control moderation findings | `[AP]` |
| 179 | 1 | 58 | Small-batch moderation findings | `[AP]` |
| 183 | 1 | 60 | User-focus moderation findings | `[AP]` |
| 187 | 1 | 62 | Platform moderation findings | `[AP]` |
| 197 | 1 | 66 | Platform findings attributed to the 2024 report | `[BT]` |
| 197 | 2, 3 | 66–67 | Current platform findings and adoption statistics | `[AP]` |
| 201 | 1 | 67 | Aggregate platform-capability ratings | `[AP]` |
| 209 | 1, 2 | 70–71 | Platform associations and AI moderation findings | `[AP]` |
| 217 | 1 | 74 | Valuable-work finding | `[AP]` |
| 231 | 1, 2 | 77–78 | VSM findings | `[AP]` |
| 253 | 1, 2 | 88 | Aggregate findings from Beane’s research | `[AP]` |
| 277 | 1–9 | 103–112 | Survey and interview sample characteristics | `[AP]` |

At line 253, Beane reports findings across occupations and research projects. Those passages do not summarise a particular illustrative case. `[AP]` accurately preserves their status as his reported findings.

### Over-flagged

| Finding | Deep line | Source | Raised by | Decision |
|---|---:|---|---|---|
| B8: omitted “Survey experience” subsection | 281 | p. 113; tape 10787–10796, 10821–10830 | Blind | **Over-flagged as a mandatory coverage repair.** The subsection exists and its proposed summary is supported. However, the supplied coverage gate concerns missing TOC chapters. Methodology is represented, and line 281 does not claim to enumerate every survey-development procedure. Omitting this detail from a synthesis does not establish unread source coverage or an unsupported claim. |

No insertion is required for B8.

### Disputed

**None.**

### Fixer’s reviewed-and-kept observations

These were review notes, not additional defect captures.

| Deep line | Observation | Source | Sort outcome |
|---:|---|---|---|
| 152 | Increased importance of prompt engineering | p. 47 | Retain. “Also increased” supports reading the preceding prompt-engineering change as an increase. Correct its `[AE]` marker separately. |
| 379 | Interview quotations anonymous by design | p. 115 | Retain. The publication describes editing for anonymity and presents anonymous participant quotations. |
| 88 | Sabre adoption reaching 74% over 18 months | p. 26 | Retain. The source explicitly connects its 18-month tracking period with adoption reaching 74%. |
| 377 | Cluster 4 and instability trade-off tensions | pp. 17, 19, 41, 66, 70 | Retain. These tensions occur in the source and are recorded without an external verdict. |
| 383 | Stamp pointer retained for the driver | Deep lines 1–3 | Resolve as B9 above; the pointer is currently false. |

**New defects introduced by the fixer: none.** The complete diff contains only the supported “signed sidebars” replacement.

## 3. Remaining edits

Apply these changes to the supplied 383-line `post-audit-deep.md`. Line numbers refer to that unchanged snapshot.

1. **Line 5.** Current:
   `version "v. 2025.2" (the version mark in every page footer and on p. 141)`  
   Replacement:
   `version "v. 2025.2" (recorded on p. 141)`

2. **Line 88.** Current:
   `satisfaction and time savings that grow with proficiency`  
   Replacement:
   `rising satisfaction and reported time savings over time, suggesting that benefits grow as users become more proficient`

3. **Line 227.** Current:
   `An interviewee describes two- or three-week processes for a firewall rule change and the uncertainty of estimation (p. 76) [AE].`  
   Replacement:
   `An interviewee describes uncertainty about estimation and asks whether a firewall-rule change will require a two- or three-week process (p. 76) [AE].`

4. **Line 315, metric cell.** Current:
   `Rely on AI: not at all / moderate or more`  
   Replacement:
   `Reliance on AI among AI users: not at all / moderate or more`

5. **Line 329, metric cell.** Current:
   `Sabre: adoption / report productivity gain / use agent mode`  
   Replacement:
   `Sabre: developer adoption / users reporting productivity gains / users leveraging newer features such as agent mode`

6. **Line 330, metric cell.** Current:
   `Adidas pilot (via *Vibe Coding*)`  
   Replacement:
   `Adidas pilot: teams with loosely coupled architectures and fast feedback loops (via *Vibe Coding*)`

7. **Line 383. Strip:**
   `Pass I: see the stamp on line 2 and the audit log.`

For edits 8–42, the current text is `[AE]` at each specified occurrence. Replace only those markers, preserving surrounding text, citations and other markers. Occurrences count `[AE]` markers from left to right on the original line.

8. **Line 14:** occurrences 1 and 2 → `[AP]`.
9. **Line 16:** occurrences 1 and 2 → `[AP]`.
10. **Line 18:** occurrences 1–3 → `[AP]`.
11. **Line 26:** occurrences 1–3 → `[AP]`.
12. **Line 30:** occurrence 1 → `[AP]`.
13. **Line 84:** occurrences 1, 3 and 4 → `[AP]`.
14. **Line 88:** occurrence 1 → `[AP]`; retain occurrence 2.
15. **Line 92:** occurrences 1 and 2 → `[AP]`.
16. **Line 100:** occurrences 1 and 2 → `[AP]`.
17. **Line 104:** occurrences 1–3 → `[AP]`; retain occurrence 4.
18. **Line 114:** occurrence 1 → `[BT]`.
19. **Line 126:** occurrence 1 → `[AP]`.
20. **Line 136:** occurrence 1 → `[AP]`.
21. **Line 140:** occurrence 1 → `[AP]`.
22. **Line 147:** occurrence 1 → `[AP]`.
23. **Line 148:** occurrence 1 → `[AP]`.
24. **Line 149:** occurrence 1 → `[AP]`.
25. **Line 150:** occurrence 1 → `[AP]`.
26. **Line 151:** occurrence 1 → `[AP]`.
27. **Line 152:** occurrence 1 → `[AP]`.
28. **Line 159:** occurrence 1 → `[AP]`.
29. **Line 163:** occurrence 1 → `[AP]`; retain occurrence 2.
30. **Line 167:** occurrence 1 → `[AP]`.
31. **Line 171:** occurrence 1 → `[AP]`; retain occurrence 2.
32. **Line 175:** occurrence 1 → `[AP]`.
33. **Line 179:** occurrence 1 → `[AP]`.
34. **Line 183:** occurrence 1 → `[AP]`; retain occurrences 2 and 3.
35. **Line 187:** occurrence 1 → `[AP]`.
36. **Line 197:** occurrence 1 → `[BT]`; occurrences 2 and 3 → `[AP]`.
37. **Line 201:** occurrence 1 → `[AP]`.
38. **Line 209:** occurrences 1 and 2 → `[AP]`; retain occurrence 3.
39. **Line 217:** occurrence 1 → `[AP]`.
40. **Line 231:** occurrences 1 and 2 → `[AP]`.
41. **Line 253:** occurrences 1 and 2 → `[AP]`.
42. **Line 277:** occurrences 1–9 → `[AP]`.

These 42 numbered instructions repair **67 defect occurrences**.

## 4. Counts

Counts use defect occurrences: each incorrect marker is one defect; each separately defective claim is one defect.

| Classification | Count |
|---|---:|
| Confirmed defects, total | **68** |
| Confirmed and fixed | 1 |
| Confirmed, fix wrong or incomplete | 0 |
| Missed by the fix-in-place audit | **67** |
| Over-flagged by fixer | 0 |
| Over-flagged by blind auditor | **1** |
| Disputed | 0 |
| Defects introduced by fixer | 0 |

The blind auditor’s 68 reported occurrences resolve to 67 confirmed defects and one over-flag. The fixer’s single reported defect is confirmed. There is no overlapping capture; reviewing and retaining a defective claim does not count as raising it.

Capture: fixer=1 blind=67 both=0

## 5. Gate verdict

**Pass once all remaining edits above are applied and verified.** No unresolved disputed finding or chapter-coverage failure remains from this sort.

The supplied snapshot currently **fails** because the 67 confirmed defects remain. After correction, the driver must complete the audit record and stamping, and perform the required derived-tier re-derivation and provenance checks before release.