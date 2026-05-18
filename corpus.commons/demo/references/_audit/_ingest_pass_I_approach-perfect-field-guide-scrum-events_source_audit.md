# Pass I audit — approach-perfect-field-guide-scrum-events

**Auditor:** claude-opus-4-7[1m] | **Effort:** xhigh | **Date:** 2026-05-13

**Subject:** `corpus.commons/demo/references/approach-perfect-field-guide-scrum-events-deep.md` (deep reference for Chris Gagné, *The Approach Perfect Field Guide to Scrum Events*, April 3, 2020 edition)

**Source-of-truth read:** `corpus.commons/demo/sources/converted/approach-perfect-field-guide-scrum-events.md` (pymupdf4llm 0.0.30 conversion of the 17-page PDF; page 1 is a cover image with no text content; substantive content runs pages 2–17). Full source coverage at Pass C.

**Calibration:** Three audit-fixture exemplars read at the start of Pass I:
- `tests/audit-fixtures/01-training-leakage.md` (canonical strip case — biographical claim source does not make).
- `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md` (marker correction — [V] on a paraphrase).
- `tests/audit-fixtures/12-clean-negative-control.md` (clean negative control; over-flagging is as costly as missing real violations).

---

## Audit method

Cold read of the deep reference against the converted source markdown, checking every non-trivial claim for source-anchoring. Special attention to: (a) biographical or post-source claims about the author; (b) cross-corpus drift (referencing the Scrum Guide or other corpus sources when the Field Guide itself does not); (c) marker mismatches ([V] without verbatim text); (d) task-application guidance smuggled into the deep tier; (e) verbatim transcription accuracy in blockquotes.

The deep reference contains approximately 470 lines of structured content, of which approximately 220 carry inline citations and evidence-class markers. Audit coverage: every prose paragraph, every blockquote, every table row, every connection/contrarian-position entry.

## Findings

### Violations found and corrected in place

**Finding 1 — Cross-corpus drift (Sprint Planning, "Goals"):** The original Pass-E text said *"The author makes the Sprint Goal SMART-style ('specific, measurable, achievable') even though the Scrum Guide itself does not — a facilitation choice."* The Field Guide's own text says only *"Identify a specific, measurable, achievable Sprint Goal that can be accomplished in the Sprint"*; the comparison to "the Scrum Guide itself does not" is a cross-corpus claim the Field Guide does not make. **Corrected** to remove the Scrum Guide comparison, retaining the [AP] paraphrase of the Field Guide's own framing.

**Finding 2 — Cross-corpus drift (Sprint Retrospective, "Input"):** The original Pass-E text said *"The author names four Scrum Values (courage, commitment, respect, openness) as a precondition, but does not include all five (focus is omitted)."* The Field Guide lists *"A culture of courage, commitment, respect, and openness"* as one of two retrospective inputs; it does not characterise these as "four of the five Scrum Values" or note that "focus" is omitted. That comparison is a cross-corpus reach to the canonical Scrum Guide's five-values structure. **Corrected** to retain the [V] quote of the four cultural conditions and remove the Scrum-Guide-five-values comparison.

**Finding 3 — Cross-corpus drift (Sprint Retrospective, "Goal"):** The original Pass-E text said *"The four named domains of self-reflection — tools, process, structure, and culture — are the author's framing; the Scrum Guide names tools, processes, and the Definition of Done."* The Field Guide does not make this contrast. **Corrected** to remove the Scrum Guide comparison, retaining the [V] quote of the four self-reflection domains.

**Finding 4 — Marker mismatch ([V] on a reconstruction; Sprint Planning, "Sample 3-Hour Sprint Planning Agenda"):** The Pass-E text marked the reconstructed Velocity formula `"if you completed 25, 24, and 31 Story Points over the last three sprint with 45, 43, and 50 days of Capacity respectively and you have a forecasted Capacity of 47 this sprint, your forecasted Velocity for this sprint is (25/45 + 24/43 + 31/50)/3 × 47 ≈ 30"` as [V] verbatim. The prose ("if you completed…") is verbatim from the source; the inline formula reconstruction in `(25/45 + 24/43 + 31/50)/3 × 47 ≈ 30` is a reconstruction of the source's multi-line equation glyph (which the source renders as bracketed mathematical fragments split across lines 277–322 of the converted markdown). The reconstruction preserves meaning but is not character-for-character verbatim. **Corrected** to split the citation: [V] on the verbatim prose portion (numbers and stated result of ≈30), [AP] on the formula reconstruction itself.

**Finding 5 — Marker mismatch ([V] on a paraphrase frame; "Connections the author makes in the text"):** The Pass-E text concluded the long `ap.tips/...` shortlink listing with `[V] (throughout)`. The shortlinks themselves appear verbatim from the source, but the framing prose ("The guide makes extensive internal cross-references… — to companion videos and supplementary articles on the Approach Perfect site — covering…") is the auditor's paraphrase of the source's structural pattern. The original [V] marker was on a paraphrase frame containing verbatim shortlinks; structurally inconsistent. **Corrected** to mark the entry [AP] with a parenthetical note that the shortlinks themselves appear verbatim.

### Non-violations checked and cleared

The following potential violations were considered and rejected after re-reading the source:

- **The author's "Wellington, New Zealand" provenance** (Source line, "Citation and source-integrity notes"): the converted source explicitly carries *"Chris Gagné — Approach Perfect, Limited (https://approachperfect.com) — Wellington, New Zealand"* in the Introduction sign-off (lines 39–41). Clean.
- **The April 3, 2020 publication date** (frontmatter, "Source" line): the source's Introduction states *"This particular edition was last updated on April 3rd, 2020"* (line 30). Clean.
- **The "knowledge as a first-class output" framing** (The Sprint, "Outputs"): the source explicitly lists *two* Sprint outputs — *"A usable, potentially-releasable product Increment"* and *"Increased useful knowledge about product, customers, competition, and the Scrum Team"* (lines 115–117). The "first-class" framing is a paraphrase of the two-output structure; non-violating.
- **The "five Scrum events plus Backlog Refinement" framing** (Author's thesis, paragraph 3; Part VI header): the source's Introduction states the guide covers *"the five standard Scrum Events and Backlog Refinement"* (line 6); the "Scrum Events at a Glance" table has six rows (Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective, Backlog Refinement, with the last marked "not officially a Scrum event"); the "five standard plus one non-Scrum" framing is the author's own structural framing of the table. Clean.
- **The two explicit Scrum Guide references** ("Daily Scrum, 'Sample 15-Minute Daily Scrum Agenda'"; "Connections the author makes in the text"): both are sourced citations the Field Guide itself makes — the Introduction's *"'textbook' Scrum (scrumguides.org)"* reference and the Daily Scrum's three-questions device *"(from the Scrum Guide™, scrumguides.org)"*. Correctly marked [BT] (borrowed-through) in both places. Not cross-corpus drift.
- **Norm Kerth's Retrospective Prime Directive verbatim** (Sprint Retrospective, "Sample 1½-Hour Sprint Retrospective Agenda"): character-by-character comparison against source lines 695–698 confirms exact match including the comma-separated four-clause structure and the closing "the situation at hand." Clean blockquote.
- **The coffee-temperature worked example** (Sprint Planning, "Sample 3-Hour Sprint Planning Agenda"): the deep ref preserves the source's exact phrasing for both the outcome example *("As a coffee drinker, I can have coffee that's just the right temperature so that I can delight in its ideal taste")* and the implementation contrast *("Integrate the Acme steam-heating element into the brew assembly")*. Verified against source lines 348–351. Clean.
- **The mature-team 85–115% delivery range** (Sprint Planning, "Tips"): exact match to source line 408. Clean.
- **The Sprint Retrospective √n voting heuristic** (Sprint Retrospective, "Sample 1½-Hour Sprint Retrospective Agenda"): the deep ref's paraphrase ("approximate square root of the topic count in votes (~9 topics = 3 votes, ~16 topics = 4 votes, ~25 topics = 5 votes, etc)") matches source lines 720–722 character-for-character within the quoted portion. Clean.
- **The 13+2 minute Daily Scrum agenda allocation** (Daily Scrum, "Sample 15-Minute Daily Scrum Agenda"): source lines 469–480 confirm the 13-minute three-question segment and the 2-minute Sprint Backlog/Burn-Down update segment. Clean.
- **The Sprint Review's seven-segment 1-hour agenda** (Sprint Review, "Sample 1-Hour Sprint Review Agenda"): seven segments totalling 60 minutes verified against source lines 589–618: 5+5+30+5+5+5+5 = 60. Clean.
- **The non-interference rule across events** (Sprint Planning; Daily Scrum; recurring): the verbatim rule *"Participants who are not Scrum Team members must understand that this is not their event and they may not interfere with the team's process, only support the team"* appears identically at source lines 214–217 (Sprint Planning) and lines 450–452 (Daily Scrum). Clean.

### Task-application guidance check

The deep reference's structure contains no diagnostic questions, no anti-pattern checklists, and no decision-tree worked applications. The "Positions the author explicitly frames against" section is structurally faithful summary of what the source argues against; it does not synthesise these into a task-axis diagnostic. The "Connections the author makes in the text" section is structurally faithful summary of citations the source makes; it does not extend connections beyond what the source cites. Task-application content lives in the two distillations (decision-making and stakeholder-engagement); the deep tier is tier-separated correctly. **Clean.**

### Coverage check

The deep reference covers all six event sections (Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective, Backlog Refinement) and all uniform sub-sections (Goal(s), Timing, Participants, Inputs, Output(s), Sample Agenda, Tips) where they exist. The "Scrum Events at a Glance" table is cited as a separate section. Page 1 (cover image, no text) is explicitly noted in the structure and coverage lines. **Coverage complete.**

## Outcome

**4 cross-corpus-drift violations corrected in place** (Findings 1, 2, 3 above; Findings 1 and 2 were the most consequential because they generalised the Field Guide's specific language into Scrum-Guide-framework claims the Field Guide does not make).

**2 marker-mismatch corrections** (Findings 4 and 5; both involved a [V] marker on a passage that mixed verbatim source content with auditor reconstruction or framing).

**0 training-data leakage findings.** The deep reference makes no biographical claims about the author beyond what the source's sign-off itself carries ("Chris Gagné — Approach Perfect, Limited — Wellington, New Zealand"). Note: the operator-supplied provenance prose in the `.source.md` sidecar carries additional context about the author and related tooling — that provenance is curator-context (per the sidecar template's "provenance prose" allowance), not deep-reference content, and is correctly partitioned to the sidecar.

**0 post-source-vocabulary findings.** All Field-Guide-specific terms (Parking Lot, positives/deltas/insights, Capacity-adjusted Velocity formula, Vegas Rule, Chatham House Rule, the coffee-temperature worked example) are sourced.

**0 distillation-guidance smuggled into the deep tier.**

**0 verbatim transcription errors** beyond the Velocity-formula reconstruction noted in Finding 4 (which was a marker-class issue, not a transcription error — the reconstructed formula resolves to the same value the source states).

## Audit-result summary

| Audit dimension | Count |
|---|---|
| Claims audited (approx. non-trivial sentences with markers) | ~220 |
| Source-anchored claims | ~220 |
| Claims stripped or rewritten as cross-corpus-drift fix | 3 (Findings 1, 2, 3) |
| Markers corrected ([V] → [AP] or split) | 2 (Findings 4, 5) |
| Training-data leakage findings | 0 |
| Post-source vocabulary findings | 0 |
| Task-application guidance findings | 0 |
| Verbatim transcription errors | 0 |
| Coverage complete | yes (pages 2–17; page 1 is the cover image with no extractable text) |

**Verdict: Deep reference ships.** Light reference (Pass F) and distillations (Pass G) derived from the audited deep reference; both inherit the corrected source-only discipline by construction. Index updates staged in `_ingest_*` files per parallel-batch convention; canonical index merges will pick up the deep ref's audited content.
