## 1. What I read

Read in full:

- `sort-brief.md`, `pass-i-spec.md` and all three calibration fixtures.
- `blind-findings.md` and `fixer-audit-log.md`. The 2026-10-15 findings were treated as context; only the 2026-10-17 findings enter the capture comparison.
- `post-audit-deep.md`, all 906 lines.
- `scope-extract.md`, all 183 blocks.
- `source-card.md`, the repository operating instructions and the required architecture documents.

Also read:

- The complete surrounding tape paragraphs and feature boxes needed to finish clipped extract blocks, and supporting passages for PR #23 lines outside Chapter 12.
- Every difference between `frozen-deep.md` and `post-audit-deep.md`.
- The original PDF’s Table 12.1 on PDF pages 363–364, using deterministic layout-preserving extraction: (`_planning/pass-i/demo/openstax-organizational-behavior/source.pdf`).
- Selected derived-tier search hits concerning affected claims; this was not a derived-tier fidelity audit.

Mechanical verification:

- Both deep-reference hashes match their supplied hash files.
- Every extract block matches its stated tape range.
- The PDF hash and byte size match the source card.
- The quotation checker reports seven apostrophe differences, five initial-capital differences and two interruptions by page furniture; no substantive quotation mismatch.

I did not read the rest of the tape. Historical conversion totals and earlier full-reading assertions cannot be independently established from this packet alone. No files were edited.

## 2. Sorted ledger

Line numbers below refer to `post-audit-deep.md`; tape locators refer to `tape.md`.

### Confirmed and fixed

| Deep line | Raised by | Defect and verified disposition | Tape evidence |
|---|---|---|---|
| 81 | Fixer | “Agrees ways to measure” strengthens discussion into agreement. “Talks with him about ways to measure” correctly preserves the reported action. | 3200–3209 |
| 151 | Fixer | “When they did not realise” makes a conditional circumstance definite. Restoring “even if” matches the source. | 5432–5436 |
| 171 | Fixer | The original tied screened auditions generally to the 1970s. The source dates blind auditioning and separately limits screens to some instances. The correction preserves both qualifications. | 6457–6464 |
| 258 | Both | Kyle recommends Bridget’s move; the source does not report a completed transfer. “He recommends she move” fixes the strengthening. | 9352–9369 |
| 274 | Fixer | The donation-per-purchase claim is attributed in the source to Mulvey, not Bombas. The corrected marker is accurate. | 9822–9828; 9832–9833 |
| 313 | Fixer | “Central to a growth strategy” introduces a strategic framing the passage does not state. The replacement reports the source’s assessment of reviews’ importance to Tesla’s success. | 12223–12228 |
| 374 | Fixer | “Formerly … global HR leader … and earlier HR and quality roles” implies an ordering before that global role. The source says “also held” and supplies no such sequence. Removing “earlier” resolves it. | 15027–15043 |
| 683 | Fixer | The explicit “from … through … to” career sequence orders roles the source does not order. The replacement preserves the stated beginning and pre-Trellis role while leaving the other roles unordered. | 24824–24840 |

### Confirmed, fix wrong or incomplete

None.

### Missed by the fix-in-place audit

| Deep line or location | Raised by | Remaining defect | Tape evidence |
|---|---|---|---|
| 338 | Blind | The concluding MTM assessment loses the source’s explicit “in this case” restriction to EA Engineering. | 13449–13454 |
| 9, 898; omission after 617 | Blind | Restored organisational-complexity exposition has no substantive account in Part XV. The environmental-fit matrix does not cover its internal/external distinction or management strategies. | 22513–22552 |
| 9, 898; omission after 644 | Blind | The restored resilience/foresight exposition is absent. Part XV has no Chapter 15.6 account covering it. | 23088–23111 |
| 814 | Blind | “A 25-year corporate career” drops “over”. | 29045–29049 |
| 846 | Blind | `<5% to ~20%` faithfully summarises the figures but is not verbatim wording. Its `[V]` marker requires correction. | 28079–28096 |

Two further blind findings are confirmed **outside the deep reference**:

| File and line | Deep counterpart | Raised by | Finding and disposition | Tape evidence |
|---|---|---|---|---|
| `source-card.md:23` | 898, already correct | Blind | The Kolb/Silberman passage belongs to Ch 4.2, not Ch 4.3. Replace that section locator in the source card. | 5382–5405 |
| `source-card.md:23` | 892–896, no equivalent false assertion | Blind | “Each page’s folio and running header come first in its text” is false. Strip that sentence. The converted page containing printed page 350 begins with the table continuation and places its folio later. | 18340–18416; also 5404–5405 and 14122–14125 |

These source-card defects are excluded from deep-reference capture counts.

### Over-flagged

| Deep line | Auditor | Finding rejected | Tape evidence |
|---|---|---|---|
| 238 | Fixer | The original Nadella framing is traceable. The lead-in explicitly connects relationship conflict with the benefits of empathy and introduces the box as empathetic collaboration. The expanded wording is grounded, but the original was not source-external framing. | 8269–8274 |
| 374 | Fixer | Hartmann’s contributor identity was already supported by the source’s front matter. Adding “as the front matter lists her” improves the locator but does not repair an unsupported biographical claim. | 686–698 |
| 564 | Fixer | The original reports that **many** blame Welch’s approach. The source says this. Omitting the additional conglomerate factor and the alternative Immelt account does not make that bounded statement false or exclusive. The expansion is accurate but not a required defect correction. | 20714–20717 |

No blind finding is over-flagged.

### Disputed

| Deep line | Raised by | Both readings and disposition | Tape evidence |
|---|---|---|---|
| 274 | Fixer | **Fixer’s reading:** ending the quotation at “motivates employees” omits what employees are motivated to do, broadening the conclusion. **Alternative reading:** the fragment is verbatim, and the surrounding passage explicitly discusses increased engagement and successfully motivating staff. It is a defensible condensation rather than demonstrably misleading quotation. The expanded quotation resolves the ambiguity; retain it, but exclude this finding from confirmed counts. | 9843–9846 |
| 374 | Fixer | **Fixer’s reading:** an unsourced illustrative profile belongs under `[AE]`. **Alternative reading:** its biographical summary also satisfies `[AP]`, because it paraphrases content the author supplies. The taxonomy does not make these uses unambiguously exclusive. `[AE]` is appropriate in the post-audit text; no further edit is needed. | 15018–15050; protocol evidence-marker taxonomy |

### Defects introduced by fixer edits

None established. All replacement claims trace to the source, including the expanded CSR quotation and the added Welch/Immelt context. The Coverage-line addition concerns audit status and is reserved to the orchestrator.

The blind audit’s Table 12.1 guard also holds: the original prints “Substitute Leadership” and “Instrumental Leadership”; its placements agree with line 484. No correction from domain knowledge is warranted.

## 3. Remaining edits

These are the five verified changes still needed in `post-audit-deep.md`. Locations use its present numbering.

1. **Line 338 — replace the final sentence.**

   Current:

   > The box concludes that MTM, understood well, is "a highly positive strategy" [V] (Ch 9, "EA Engineering, Science, and Technology, Inc.").

   Replacement:

   > For EA Engineering, Science, and Technology, Inc., the box calls multiple team memberships "a highly positive strategy" [V] for achieving business outcomes (Ch 9, "EA Engineering, Science, and Technology, Inc.").

2. **After line 617 — insert the missing organisational-complexity account.**

   Current: no paragraph between the final environmental-fit bullet and `### Mechanistic versus organic structures`.

   Insert:

   > The section distinguishes external complexity, arising from the organisation's operating environment, from internal complexity in its products, technologies, people, processes and structure [AP]. Drawing on De Toni and De Zan, it presents three approaches to managing high external complexity: self-managing teams or autonomous business units with entrepreneurial responsibility to the larger organisation; simple rules and infrastructure that permit complex outputs; and building organisational capabilities through open networks, brand and reputation, shared values and knowledge, trust, and leadership at multiple levels [BT, De Toni and De Zan] (Ch 15.2, "Organizational Complexity").

3. **After line 644 — insert the missing resilience/foresight account.**

   Current: Part XV ends after the Amazon culture paragraph, immediately before Part XVI.

   Insert:

   ```markdown
   ### Organising for change in the 21st century

   Drawing on the 2018 Global Risks Perception Survey report, the section presents nine resilience lenses grouped into three categories: structural resilience, concerning internal systemic dynamics and loosely coupled structures; integrative resilience, concerning external interconnections and social cohesion; and transformative resilience, concerning risks that require organisational transformation. It distinguishes organisational foresight from forecasting and calls for environmental scanning, discovery, innovation and experimentation to engage with uncertain futures [BT, World Economic Forum] (Ch 15.6, "Organizing for Change in the 21st Century").
   ```

4. **Line 814 — restore the numerical qualifier.**

   Current:

   > After a 25-year corporate career,

   Replacement:

   > After a corporate career of more than 25 years,

5. **Line 846 — correct the evidence marker.**

   Current:

   ```markdown
   | TEA range across GEM economies | <5% to ~20% | [V] (Ch 19.1) |
   ```

   Replacement:

   ```markdown
   | TEA range across GEM economies | <5% to ~20% | [AP] (Ch 19.1) |
   ```

The two source-card corrections are recorded separately in the ledger. No Coverage-line, stamp or audit-status rewrite is included here.

## 4. Counts

The fixer’s 13 logged edits are adjudicated separately, including the wording and marker changes combined in its Hartmann row.

| Measure | Count |
|---|---:|
| Confirmed unique deep-reference defects | 13 |
| Confirmed and correctly fixed | 8 |
| Confirmed, fix wrong or incomplete | 0 |
| Missed deep-reference defects still requiring edits | 5 |
| Confirmed source-card defects, counted separately | 2 |
| Fixer over-flags | 3 |
| Blind over-flags | 0 |
| Disputed fixer findings | 2 |
| Disputed blind findings | 0 |
| Defects introduced by fixer edits | 0 |

The blind audit raised six confirmed deep-reference defects: five within PR #42 scope and one within PR #23 scope. Its two source-card findings are additional and excluded from capture.

Blind-only (PR #23 lines): 1  
Blind-only (re-anchoring lines): 0

Capture: fixer=8 blind=5 both=1

## 5. Gate verdict

**Pass for the scoped deep-reference gate once remaining edits 1–5 are applied.** The current file fails unchanged.

The two substantive omissions require added accounts; weakening the coverage wording would not repair them. The two source-card corrections remain outstanding separately. This verdict does not certify out-of-scope material or replace the subsequent apply, derived-tier fidelity and stamping legs.