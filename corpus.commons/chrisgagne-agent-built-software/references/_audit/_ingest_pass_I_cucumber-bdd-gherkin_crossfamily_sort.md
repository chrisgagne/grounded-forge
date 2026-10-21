## 1. What I read

Read in full: `sort-brief.md`, `pass-i-spec.md`, all three calibration fixtures, `blind-findings.md`, `fixer-audit-log.md`, `post-audit-deep.md` (364 lines), and `tape.md` (1,210 lines). Also read `source-card.md`, its acquisition manifest, and the repository operating instructions.

Compared `frozen-deep.md` with `post-audit-deep.md`: the only changes are at lines 38 and 232. The post-audit file matches its supplied SHA-256.

No original source files, licence file or image are supplied in this folder. Provenance assertions are corroborated by the acquisition manifest rather than independently verified against originals.

No files were changed. This response is the report; the filesystem is read-only.

## 2. Sorted ledger

All deep-reference line numbers below refer to `post-audit-deep.md`.

| Finding | Raised by | Deep line | Tape anchor | Decision and reason |
|---|---|---:|---|---|
| Implementation-details claim lacks the `When` citation | Fixer | 38 | 671–688, especially 687; observable outcomes at 690–708 | **Confirmed and fixed.** The added `When` anchor locates the implementation-details prescription; retaining `Then` supports the observable-output claim. |
| Both Highlander rules described as having ninja examples | Fixer | 232 | 586–607 | **Confirmed and fixed.** Only the first rule supplies ninja steps. The second supplies one named example followed by `...`. The replacement accurately distinguishes them. |
| Localisation page described as containing “three sentences” | Blind | 23 | 1203–1208 | **Missed by the fix-in-place audit.** There are five sentences: two at 1203 and one each at 1205, 1206 and 1208. |
| Omission of “the details of” broadens the description of the coworker example | Blind | 108 | 143–157, especially 155–157 | **Missed by the fix-in-place audit.** The source excludes implementation detail, rather than everything the coworker does. The qualifier needs restoring. |
| “Gjett et ord” identified as a scenario name | Blind; explicitly considered and retained by fixer | 289 | 991–1005, especially 995, 997 and 1001 | **Missed by the fix-in-place audit.** The source introduction loosely calls the block a scenario, but the block identifies “Gjett et ord” as its feature title and supplies two separately named examples. The introduction does not support assigning that title to a scenario. |
| “Four `<Term>` placeholders” allegedly understates their number | Blind | 359 | 1025, 1032, 1034, 1081 and 1195 | **Disputed.** There are five occurrences and four distinct names. The blind auditor reads “four placeholders” as an occurrence count, which is wrong. The alternative reading treats the parenthesised list as an inventory of four distinct placeholders, which is accurate. The sentence does not explicitly claim four occurrences or one occurrence per name. |
| `publish_year: 2026` unsupported as publication metadata | Blind | —; `source-card.md` line 5 | No publication-year statement in the tape; acquisition manifest records `commit_date: 2026-10-08` | **Confirmed, fix absent; outside the deep reference.** A repository snapshot date does not establish publication year. The deep’s line 5 correctly presents the date as belonging to the commit, so this is not an additional deep-reference defect. |

**Confirmed, fix wrong or incomplete:** none among the fixer’s two edits.

**Over-flagged:** none conclusively. The placeholder-count finding is disputed rather than counted as an over-flag.

**Defects introduced by the fixer:** none. Both changed passages match the tape, and the diff contains no other edits.

The fixer’s other “considered and kept” passages do not require correction:

- “Quoted approvingly” at lines 330 and 335 describes quotations used to frame the pages’ own arguments (tape 54–58 and 406–412).
- “Described neutrally” at line 333 reasonably describes the workshop-model summaries (251–257).
- “Formulation before automation” at line 346 is supported by the stated progression and requirement for feedback on wording (33–37, 408–412).
- Historical attribution markers at lines 193–194 and 324 follow the reference’s declared classification and trace to tape 432–438.
- Licence metadata at line 5 is corroborated by the source card and acquisition manifest; original licence verification remains a provenance limitation.

## 3. Remaining edits

These are the exact, verified changes still required in `post-audit-deep.md`.

1. **Line 23 — sentence count**

   Current:
   ```
   three sentences
   ```

   Replacement:
   ```
   five sentences
   ```

2. **Line 108 — restore the source’s qualifier**

   Current:
   ```
   The page points out that the scenario does not go into what the software (here, the coworker) will do; it stays with the perspective of the person the Feature serves [AP].
   ```

   Replacement:
   ```
   The page points out that the scenario does not go into the details of what the software (here, the coworker) will do; it stays with the perspective of the person the Feature serves [AP].
   ```

3. **Line 289 — correct the example’s identity**

   Current:
   ```
   The page shows a Norwegian scenario, "Gjett et ord" [AE].
   ```

   Replacement:
   ```
   The page shows a Norwegian feature, "Gjett et ord", containing the scenarios "Ordmaker starter et spill" and "Gjetter blir med" [AE].
   ```

The disputed placeholder wording is excluded from mandatory edits. The confirmed source-card defect is outside this section’s requested file scope; its correction would be `publish_year: 2026` → `publish_year: null`.

## 4. Counts

Counts treat each distinct defective claim once.

| Classification | Count |
|---|---:|
| Confirmed deep-reference defects | 5 |
| Confirmed and correctly fixed | 2 |
| Confirmed fixer findings with wrong or incomplete fixes | 0 |
| Missed by the fix-in-place audit | 3 |
| Confirmed defect outside the deep reference | 1 |
| Over-flagged — fixer | 0 |
| Over-flagged — blind | 0 |
| Disputed — blind | 1 |
| New defects introduced by fixer edits | 0 |

The fixer’s consideration and retention of the Norwegian wording does not count as capturing a defect: it explicitly judged that wording acceptable. The source-card defect and disputed placeholder finding are excluded from capture.

Capture: fixer=2 blind=3 both=0

## 5. Gate verdict

**Pass once the three remaining deep-reference edits are applied**, for fidelity to the supplied tape within the declared operator-approved subset.

All 12 acquired pages have corresponding coverage. Neither fixer edit introduces a defect, and no unresolved confirmed deep-reference defect remains after the listed corrections. The placeholder wording is defensible as an inventory of distinct names.

This verdict does not independently certify acquisition completeness, licence evidence or the uninspected image. The source-card publication-year correction remains outstanding outside the deep-reference gate.