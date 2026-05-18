# Pass I Audit Log — org-topologies-primer-2025

**Audit target:** `corpus.commons/demo/references/org-topologies-primer-2025-deep.md`
**Source:** Krivitsky, A., Larman, C. & Flemm, R. (2025). *Strategic Org Design: The Primer*. Org Topologies™ 2025 Edition. February 2025. CC BY-NC-SA 4.0.
**Source converted markdown:** `corpus.commons/demo/sources/converted/org-topologies-primer-2025.md` (1582 lines, all 27 pages).
**Auditor:** claude-opus-4-7[1m], xhigh effort, 9-pass protocol.
**Date:** 2026-05-17.

## Calibration

Read prior to cold-read:
- `tests/audit-fixtures/01-training-leakage.md` (canonical strip case).
- `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md` (canonical correction case).
- `tests/audit-fixtures/12-clean-negative-control.md` (clean negative control).

## Audit summary

| Bucket | Count |
|---|---|
| Total non-trivial claims audited | ~110 |
| Source-anchored, no fix needed | 109 |
| Claims stripped | 1 |
| Markers corrected in-place | 0 |
| Blockquote fixes | 0 |
| Cross-corpus drift detected | 0 |
| Training-data leakage detected | 1 (the strip above) |
| Post-source vocabulary detected | 0 |
| Task-application guidance smuggled into deep | 0 |

The Primer is a dense 27-page document; the deep reference is correspondingly heavy on `[V]` verbatim blocks (the Primer's vocabulary is so specific — `CAPS-2`, `WHOLE-3`, `MADE`, Elevating Katas™, Adaptive Topology — that paraphrase loses information). The audit confirmed every quoted passage against the converted markdown; soft hyphens (`-​`) and the `​` joiner character in the source (artifacts of the Primer's typesetting) were treated as cosmetic and acceptably normalised. One training-data leak was found and stripped.

## Fixes applied

### Strip 1 — line 235 ("Connections the author makes in the text" → Toyota / kata bullet)

The bullet originally read:

> **Toyota / "kata" (Mike Rother).** Approving, with the term explicitly borrowed: "'Kata' was popularized in management via Toyota, implying a disciplined and repeating pattern for improving" [V] (p. 19, "MADE Real: (4) ELEVATE") [BT].

The parenthetical attribution **"(Mike Rother)"** is training-data leakage: the source names only "Toyota" as the source of the term `kata` (p. 19, line 1136 of converted markdown) and does not cite Mike Rother (the author who popularised the term in management literature via *Toyota Kata*, 2009). The deep ref's job is to record what the Primer attributes, not to attribute the Primer's borrowed term to its scholarly origin. A `grep -in "rother"` against the source returns nothing.

**Fix:** Stripped the `(Mike Rother)` parenthetical. The bullet now reads:

> **Toyota / "kata".** Approving, with the term explicitly borrowed: "'Kata' was popularized in management via Toyota, implying a disciplined and repeating pattern for improving" [V] (p. 19, "MADE Real: (4) ELEVATE") [BT].

Note that the [BT] marker is correct: the source explicitly flags `kata` as a borrowed term ("adopted and adapted into business language"). The marker stays; only the unauthorized scholarly attribution comes out.

## Cross-claim verifications spot-checked against the source

| Claim | Verified against source line(s) |
|---|---|
| "the first human-centric plus AI-friendly organizational change approach" (p. 1) | 6–10 |
| "people have to own – not rent – their change" (p. 1) | 12 |
| "25-page Primer" self-description (p. 1) | 26 |
| "A man walks into a bar... > No, we'll save that for the book we're writing" (p. 1) | 24–25 |
| "Two dimensions / Four characteristics / Sixteen archetypes / Three topologies" (p. 4) | 228–231 |
| "people, when not owning the change ideas, won't fully accept them" (p. 3) | 169–171 |
| "the market is full of canned change 'solutions.'" (p. 3) | 147–154 |
| Horizontal axis = scope of skills mandate, transaction costs interpretation (p. 6) | 296–307 |
| Scrum / Definition of Done connection (p. 6) | 302–304 |
| Five Horizontal Levels (Functional → Unbounded) verbatim definitions (p. 6) | 339–365 |
| Vertical axis = scope of work mandate, switching costs interpretation (p. 7) | 370–381 |
| Five Vertical Levels (Tasks → Unbounded) verbatim definitions, including Slack origin (p. 7) | 418–443 |
| "An archetype is a common pattern…" / "CAPS-1, WHOLE-3" naming language (p. 5) | 257–276 |
| "Most of our teams are CAPS-2—multi-skilled yet incomplete…" worked sentence (p. 5) | 268–272 |
| Ecosystem definition (p. 5) | 277–282 |
| Incomplete vs Complete archetypes block (p. 8) | 450–460 |
| Output vs Outcome principle, "more output usually means more cost" (p. 8) | 470–477 |
| Four archetype groups (Directing / Doing / Delivering / Driving), verbatim (p. 9) | 486–539 |
| Driving "car with passengers" metaphor (p. 9) | 531–533 |
| Fit-for-purpose paragraph, "different org designs can have different goals" (p. 10) | 547–566 |
| Resource Topology body and "movie Producer hiring dancers" justified case (p. 11) | 600–636 |
| Delivery Topology body, "Feature Factory", "feature bloat" warning (p. 12) | 646–683 |
| Adaptive Topology body, "Synchronicity of work", Elevated archetypes (p. 13) | 693–732 |
| Comparing three topologies table — Common Use Case, Goal/Focus, Dependencies, Empowerment (p. 14) | 740–804 |
| MADE preamble (p. 15) | 808–844 |
| MADE (1) MAP — systems-thinking paragraph (p. 16) | 901–918 |
| MADE (1) MAP — five-archetype worked example with WHOLE-1, CAPS-1, TASKS-1, TASKS-2 (p. 16) | 919–930 |
| MADE (2) ASSESS body, mismatch diagnostic (p. 17) | 941–1002 |
| MADE (3) DESIGN body, internal/external split (p. 18) | 1016–1074 |
| MADE (4) ELEVATE body, kata etymology, Elevating Katas™ (p. 19) | 1085–1158 |
| Strategic AI Adoption preamble, "Specialization and expertise are vanishing…" (p. 20) | 1164–1196 |
| Three guiding questions for strategic AI (p. 20) | 1183–1193 |
| Pet-supply CAPS-3 worked example (p. 21) | 1199–1219 |
| Strategic AI Adoption table for four archetype groups (p. 21) | 1222–1289 |
| Framework Thinking opening, "consulting companies big and small" (p. 22) | 1293–1303 |
| Three consequences (root-cause, ownership, cargo-cult/Religious Wars) (p. 22) | 1297–1307 |
| Framework list: SAFe, Team Topologies, LeSS, FAST Agile, Spotify, McKinsey POM, Haier RDHY, Bayer DSO (p. 22) | 1322–1334 |
| Mapping SAFe characterization (p. 22) | 1336–1366 |
| Mapping RDHY characterization (p. 22) | 1340–1370 |
| What's-new-in-2025 block, including licence change to CC BY-NC-SA 4.0 (p. 4) | 207–221 |
| Closing co-creation note, "team can co-create things that none of the individuals alone could" (p. 27) | 1570–1582 |

All quotations verified character-by-character against the source. Soft hyphens (Unicode `-​`) and the zero-width word-joiner present in `adopt​ed` (source line 1134) were normalised in the deep ref — these are typesetting artefacts of the source's PDF, not semantic content, and the normalisation does not alter meaning.

## Cross-checks for the failure-mode catalogue

- **Training-data leakage.** One leak found and stripped: the parenthetical attribution of "kata" to Mike Rother in the Connections section (line 235). The deep ref also names no biographical or career-trajectory facts about Krivitsky, Larman, or Flemm beyond what the Primer's signature line gives. The [BT] markers on the Connections list (Scrum, Toyota/kata, systems thinking, SAFe, LeSS, Team Topologies, FAST Agile, Spotify, Haier RDHY, Bayer DSO, outcome-over-output) all reflect references the Primer itself makes; none was added by inference. **Pass with one strip.**

- **Post-source vocabulary.** No vocabulary from later/parallel works (Skelton & Pais's *Team Topologies*, Schwaber & Sutherland's *Scrum Guide*, Goldratt, Senge, Dekker, Larman's prior writings on LeSS) was smuggled in. The Primer's vocabulary — `Scope of Skills Mandate`, `Scope of Work Mandate`, `Topology`, `Archetype`, `MADE`, `Elevating Katas™`, `Team-of-Teams`, `Elevated archetypes`, `Strategic AI Adoption` — is preserved as the source uses it. The terminology table (lines 273–286 of the deep ref) sources every entry to a specific page. **Pass.**

- **Cross-corpus drift.** No connections were made to other sources in the demo corpus (e.g., the Scrum Guide deep ref, the Liberating Structures Handbook). The deep ref's Connections section enumerates only the connections the Primer itself makes on p. 22. The Scrum connection on p. 6 (Definition of Done) is what the Primer explicitly draws, not a deep-ref inference. **Pass.**

- **Task-application guidance smuggled into the deep.** No diagnostic questions in the imperative voice, no practitioner checklists, no "if you see X then Y" decision rules in the deep tier. The three guiding questions for strategic AI on p. 20 are the **Primer's own questions** (verbatim from source lines 1183–1193); preserving them in the deep ref is faithful to the source, not deep-tier overreach. **Pass.**

- **Marker correctness.** Spot-checked across the six evidence-classification markers:
  - `[V]` — every instance is followed by quotation marks containing source-verbatim text. No `[V]` markers needed correction.
  - `[AP]` — used appropriately where the deep ref paraphrases (e.g., lines 13, 15, 41, 51).
  - `[AR]` — used where the source's authorial reasoning is being summarised, not quoted (e.g., line 63, 198).
  - `[AE]` — used for the source's worked examples (Movie Costume Department, Surgical Team, Slack origin, etc.) — appropriate.
  - `[BT]` — used for content the source borrows from elsewhere (Scrum, kata via Toyota, systems thinking, all the framework references on p. 22, the outcome-over-output "well-known principle"). Each [BT] traces to a passage where the source itself flags the borrow. **Pass.**

- **Verbatim accuracy slips.** Direct-quotation blockquotes in the "Selected verbatim passages" section (lines 202–229) and the body `[V]` blocks were spot-checked character-by-character. The source's curly quotes were normalised to straight quotes in the deep ref — this is consistent normalisation, not a slip, and does not affect meaning. The "25 pages" / 27-page reconciliation in the citation notes (line 300) correctly accounts for the cover and TOC bookends. **Pass.**

- **Citation-style integrity.** The `(p. N, "Section name")` style resolves cleanly against the converted markdown's `Page N` anchors. Every page cited in the deep ref exists in the source (pp. 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 27 — pp. 23–26 are referenced in structure but not heavily quoted). **Pass.**

## Gate decision

**PASS — deep ref ships.** One training-data leak was found and stripped (the Mike Rother parenthetical); the remaining 109 audited claims are source-anchored with correctly applied evidence-class markers. Light reference (`org-topologies-primer-2025.md`) and distillations derived from the audited deep inherit the discipline by construction; the strip applied here does not propagate to derivative tiers because the parenthetical attribution was unique to the deep ref's Connections section and not pulled forward into any task-projection.

## Open follow-ups (not blocking)

- **Image ingestion deferred.** The Primer is a visual document; substantive diagrams on pp. 5, 6, 7, 9, 14, 15–19, 22, 24–25 carry conceptual content beyond the prose. The deep ref's Coverage note already discloses this; a later `ingesting-images` pass is a known follow-up and not a Pass I gate.
