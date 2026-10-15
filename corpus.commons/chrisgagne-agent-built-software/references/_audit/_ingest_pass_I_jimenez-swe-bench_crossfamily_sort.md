## 1. What I read

Read in full:

- `sort-brief.md`, `pass-i-spec.md` and all three calibration fixtures.
- `blind-findings.md` and `fixer-audit-log.md`.
- `post-audit-deep.md`: all 351 lines.
- `tape.md`: all 4,441 newline-delimited lines, covering all 52 pages.
- `source-card.md`, the repository operating instructions and required architecture documents.

Compared every change against `frozen-deep.md`. The post-audit checksum matches: `5ecfc665c7976ccd2947e6273947345f6c6cd4a4fabe5db16b84dd89582f5708`.

Independently extracted all 52 pages of :codex-file-citation{path="_planning/pass-i/chrisgagne-agent-built-software/jimenez-swe-bench/source.pdf" purpose="source"} with `pdftotext`. Every page matches its tape segment after whitespace normalisation. Also inspected layout-preserving extraction of pp. 28–29 to verify citation placement and Table 24’s columns. No figure images were visually inspected.

Ran the repository’s verbatim checker against the post-audit reference with `--source tape.md`: **no findings**.

No files were edited. This final message is the report; the filesystem is read-only.

## 2. Sorted ledger

Line numbers below refer to `post-audit-deep.md`.

| ID | Raised by | Deep line | Tape lines / page | Classification and finding |
|---|---|---:|---|---|
| 1 | Blind | 297 | 346–350, p. 4, §3 | **Missed by the fix-in-place audit.** “Under 30,000 tokens” excludes the boundary. The source excludes sequences with **more than** 30,000 tokens, leaving sequences with **at most** 30,000. The post-audit table remains wrong; line 138 correctly states the exclusion. |
| 2 | Blind | 320 | 1004–1007, p. 9, §6 | **Missed by the fix-in-place audit.** The reference combines works and datasets, then makes “none” apply to that entire collection. The source identifies program-repair and commit-guided editing **works** as most relevant, then compares the code-context scale of existing **datasets**. The post-audit wording still broadens the comparison. |
| 3 | Fixer | 253 | 2867–2870, p. 28, App. C.7 | **Disputed.** The fixer changed the semantic-similarity contrast and logical-abstraction claim from `[BT]` to `[AP]`. One reading is that the contrast belongs to the SWE-bench authors, while McCabe and Halstead are cited to identify the metrics; `[AP]` expresses that attribution more clearly. The other reading is that citations embedded in the sentence also support the metrics’ stated properties, making `[BT]` defensible for that borrowed component. The source does not establish the fixer’s categorical claim that the citations serve *only* to name the metrics. The post-audit wording is acceptable; no further edit is required. |
| 4 | Fixer | 253 | 3058–3062, p. 29, App. C.7 | **Confirmed and fixed.** The higher-complexity → greater defect likelihood / harder maintenance assertion previously sat inside a passage ending `[BT]`. In the source, McCabe is cited for counting independent execution paths, and Halstead for counting operators and operands; the intervening risk-and-maintenance sentence carries no citation. The fixer correctly separates it as an assertion by the paper’s authors, marked `[AP]`, while retaining `[BT]` on the cited definitions. |
| 5 | Fixer | 216 | 3016–3050, p. 29, Table 24 | **Over-flagged by the fixer as a required correction.** The original comparison was accurate: both SWE-Llama models have more total lines and fewer added lines, removed lines and functions than their matching gold patches. It did not assert that these were all the columns or that total lines were the only increase. Adding files edited—13b 1.6 versus 1.4; 7b 1.5 versus 1.5—is accurate enrichment, not repair of a false claim. Keep the addition. |
| 6 | Fixer | 347 | 2852–2858 and 3016–3050, pp. 28–29, App. C.6 / Table 24 | **Over-flagged by the fixer as a required correction.** The same omission occurred in the integrity-note summary, but its stated comparisons were correct. The omitted files column does not rescue “longer in most respects”: 13b exceeds gold in two of five columns; 7b exceeds it in one and ties in one. The added parenthesis is accurate and may remain. |

**Confirmed, fix wrong or incomplete:** none.

### Checker warning and the fixer’s open question

| Item | Raised or discussed by | Deep line | Tape lines / page | Disposition |
|---|---|---:|---|---|
| Literal `[V]` in the marker legend | Fixer; independently cleared by blind | 351 | Not applicable: editorial marker definition | **Over-flagged by the automated checker, not by either auditor.** The legend names a marker; it does not mark a source quotation. Code spans clear the warning without changing meaning. Excluded from auditor over-flag counts. |
| Bug-tag count versus “absolute majority” of issues | Fixer’s open question; blind also checked | 125 | 1846–1851, p. 21; Table 13, p. 24 | **No deep-reference defect.** The source explicitly makes the majority assertion, and the reference attributes it to the authors. The table counts tags, not a mutually exclusive census of issues. Whether the source adequately supports its assertion is a source-quality question, not an attribution failure. Neither auditor asserted a confirmed defect here. |

The auditors’ other “checked and left” and “over-flag guard” entries are clean-check records, not additional allegations. My source checks support their dispositions:

- The quoted evaluations, seaborn image-input attribution and explicitly opposed approaches occur in the source.
- The Claude percentages, collapsed-context comparison, No-Op arithmetic and case-table inconsistencies are preserved as source statements or transparently identified discrepancies.
- The Lite gaps occur in the original PDF.
- Text-only figure coverage is declared; the reference does not claim visual verification.
- Historical markitdown results and ingestion actions remain provenance statements that the supplied materials do not independently establish. That uncertainty is not evidence of fabrication.

### Defects introduced by the fixer

**None found.** The added Table 24 values match the original table. The marker split preserves the source’s assertions and cited definitions. The code-span edit changes presentation only.

## 3. Remaining edits

Exactly **two** verified changes remain.

1. **Line 297 — replace the training-data value cell.**

   Current:

   > 19,000 issue-PR pairs from 37 repositories; 10,000 under 30,000 tokens used

   Replacement:

   > 19,000 issue-PR pairs from 37 repositories; 10,000 instances with at most 30,000 tokens used

   Preserve the existing `[AP]` marker and citation. Verified against tape lines 346–350, p. 4, §3.

2. **Line 320 — retain the bold list, and replace the text after its colon.**

   Current:

   > named as the most relevant prior work, none with SWE-bench's scale of code context [BT] (p. 9, §6).

   Replacement:

   > the authors identify automated program repair and commit-guided code editing as the most relevant work, then state that none of the existing datasets presents code context at SWE-bench's scale [BT] (p. 9, §6).

   Verified against tape lines 1004–1007, p. 9, §6.

## 4. Counts

Counts use distinct defects in distinct claims, rather than edit operations. The disputed mixed-attribution sentence is excluded from confirmed capture. The two Table 24 additions are counted separately as over-flagged required corrections at their two occurrences.

| Classification | Count |
|---|---:|
| Confirmed defects, total | 3 |
| Confirmed and fixed | 1 |
| Confirmed, fix wrong or incomplete | 0 |
| Missed by the fix-in-place audit | 2 |
| Over-flagged by fixer | 2 |
| Over-flagged by blind | 0 |
| Disputed | 1 |
| New defects introduced by fixer | 0 |

The automated legend warning and the source-quality question about bug tags are excluded from these auditor-finding counts.

Capture: fixer=1 blind=2 both=0

## 5. Gate verdict

**Pass once the two remaining edits are applied.** Both outstanding defects have exact, source-verified corrections. No coverage failure or defect introduced by the fixer was found.

The current post-audit reference remains **fail** until those edits are made. Release completion also requires the driver’s audit stamp and the protocol’s light-reference re-derivation and provenance stamp; this report does not certify those operations as completed.