# Pass I Audit Log — scrum-guide-2020

**Audit target:** `corpus.commons/demo/references/scrum-guide-2020-deep.md`
**Source:** Schwaber, K. & Sutherland, J. (2020). *The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game*. November 2020 edition. CC BY-SA 4.0.
**Source converted markdown:** `corpus.commons/demo/sources/converted/scrum-guide-2020.md` (681 lines, all 14 pages).
**Auditor:** claude-opus-4-7[1m], xhigh effort, 9-pass protocol.
**Date:** 2026-05-13.

## Calibration

Read prior to cold-read:
- `tests/audit-fixtures/01-training-leakage.md` (canonical strip case).
- `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md` (canonical correction case).
- `tests/audit-fixtures/12-clean-negative-control.md` (clean negative control).

## Audit summary

| Bucket | Count |
|---|---|
| Total non-trivial claims audited | ~95 |
| Source-anchored, no fix needed | 92 |
| Claims stripped | 0 |
| Markers corrected in-place | 3 |
| Cross-corpus drift detected | 0 |
| Training-data leakage detected | 0 |
| Post-source vocabulary detected | 0 |
| Task-application guidance smuggled into deep | 0 |

The deep reference is short by corpus norms (~280 lines body) because the source itself is short (14 pages) and densely definitional. Most paragraphs in the deep ref are direct quotations with `[V]` markers; the audit confirmed every quoted passage character-for-character against the converted markdown. Three marker corrections were applied; no strips were needed.

## Marker corrections

### Correction 1 — line 31 ("Scrum engages groups of people…")

Marker was `[AP]` (author paraphrase). The text was a full verbatim quotation from "Scrum Theory": "engages groups of people who collectively have all the skills and expertise to do the work and share or acquire such skills as needed" (converted markdown line 168). Fixed marker to `[V]`.

### Correction 2 — line 62 ("A size guideline is offered with rationale…")

Marker was `[AP]` on a full verbatim quotation: "The Scrum Team is small enough to remain nimble and large enough to complete significant work within a Sprint, typically 10 or fewer people. In general, we have found that smaller teams communicate better and are more productive" (converted markdown lines 248–250). Fixed marker to `[V]`.

### Correction 3 — line 243 ("Connections the author makes in the text")

The collaborators paragraph carried `[BT]` (Borrowed-through, "the author cites someone else for the claim"). But the source text in the End Note, "People" section is first-person authorial: "Jeff Sutherland worked with Jeff McKenna and John Scumniotales, and Ken Schwaber worked with Mike Smith and Chris Martin, and all of them worked together." This is the authors' own statement of who they collaborated with — not a borrowed citation. Fixed marker to `[V]` with the source's own ordering preserved and the source's "instrumental at the start" framing surfaced.

## Cross-claim verifications spot-checked against the source

| Claim | Verified against source line(s) |
|---|---|
| "a lightweight framework that helps people, teams and organizations generate value through adaptive solutions for complex problems" | 139–140 |
| "Empiricism asserts that knowledge comes from experience and making decisions based on what is observed" | 163–164 |
| "Inspection without transparency is misleading and wasteful" | 190 |
| "Inspection without adaptation is considered pointless" | 199 |
| "the adjustment must be made as soon as possible to minimize further deviation" | 206–207 |
| "Commitment, Focus, Openness, Respect, and Courage" (italics preserved) | 218 |
| "typically 10 or fewer people" | 249 |
| "The Product Owner is one person, not a committee" | 309 |
| "The Sprint is a container for all other events" | 370 |
| "Sprints are the heartbeat of Scrum, where ideas are turned into value" | 379 |
| Sprint length "fixed length events of one month or less" | 381 |
| Daily Scrum "15-minute event" | 470 |
| Sprint Planning "timeboxed to a maximum of eight hours for a one-month Sprint" | 461 |
| Sprint Review "timeboxed to a maximum of four hours for a one-month Sprint" | 497 |
| Sprint Retrospective "timeboxed to a maximum of three hours for a one-month Sprint" | 518 |
| "Only the Product Owner has the authority to cancel the Sprint" | 413–414 |
| "The Sprint Review is a working session and the Scrum Team should avoid limiting it to a presentation" | 495 |
| "The Sprint Review should never be considered a gate to releasing value" | 609 |
| "Work cannot be considered part of an Increment unless it meets the Definition of Done" | 611 |
| "The moment a Product Backlog item meets the Definition of Done, an Increment is born" | 619 |
| "The Scrum framework, as outlined herein, is immutable. While implementing only parts of Scrum is possible, the result is not Scrum" | 639–640 |
| "four formal events for inspection and adaptation within a containing event, the Sprint" | 171 |
| "five events" (in Inspection sub-section) | 197 |
| "A product is a vehicle to deliver value. It has a clear boundary, known stakeholders, well-defined users or customers" | 566–567 |
| OOPSLA 1995 first co-presentation | 656 |
| Individual Inc., Newspage, Fidelity Investments, IDX (now GE Medical) | 666 |
| Jeff McKenna, John Scumniotales, Mike Smith, Chris Martin as early collaborators | 649–650 |
| "developers" used inclusively for "researchers, analysts, scientists, and other specialists" | 21–25 |

All quotations verified. The four-formal-events / five-events distinction in the source (four inspection-and-adaptation events within the containing Sprint event = five total) is captured correctly in the deep ref and in the key-counts table.

## Cross-checks for the failure-mode catalogue

- **Training-data leakage.** No claims about Schwaber's or Sutherland's biographies, careers, or later writings were added. The deep ref records only the names of early collaborators that the source itself names in its End Note. The provenance section explicitly notes the Guide makes no internal citations beyond Creative Commons. **Pass.**
- **Post-source vocabulary.** No introduction of concepts from later editions of the Scrum Guide (e.g., 2017 or 2011 editions) or from Schwaber's or Sutherland's other works (e.g., *Agile Software Development with Scrum*, *Scrum: The Art of Doing Twice the Work in Half the Time*). The deep ref is faithful to the November 2020 edition's vocabulary. **Pass.**
- **Cross-corpus drift.** The deep ref's "Connections" section explicitly notes the Guide makes no internal citations to Agile Manifesto, Sutherland's earlier writings, or broader iterative-development literature. No such connections were smuggled in. The mention of Letaw (2024) appears only as a parenthetical to note that the Letaw→Schwaber citation runs in the wrong direction for inclusion as a Scrum-Guide-internal connection — this is a defensive disclosure, not a cross-corpus drift. **Pass.**
- **Task-application guidance smuggled into the deep.** No diagnostic questions, no decision rules, no practitioner checklists in the deep tier. All such material is in the distillations (`scrum-guide-2020-decision-making.md`, `scrum-guide-2020-stakeholder-engagement.md`). **Pass.**
- **Verbatim accuracy slips.** Blockquotes spot-checked character-by-character: the italicised five values; the "*A product is a vehicle to deliver value...*" definition; "The moment a Product Backlog item meets the Definition of Done, an Increment is born"; "Sprints are the heartbeat of Scrum, where ideas are turned into value". All preserve the source's italicisation, capitalisation, and exact wording. **Pass.**

## Gate decision

The deep reference passes Pass I and is cleared to ship. Light reference (`scrum-guide-2020.md`) and distillations (`scrum-guide-2020-decision-making.md`, `scrum-guide-2020-stakeholder-engagement.md`) derive from the audited deep and inherit the discipline by construction.
