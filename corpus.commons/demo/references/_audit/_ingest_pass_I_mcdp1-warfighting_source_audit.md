---
audit: pass-I
target: corpus.local/aarbuddy/references/mcdp1-warfighting-deep.md
source-converted: corpus.local/aarbuddy/sources/converted/mcdp1-warfighting.md
source-sha256: 064cd1be0f243791319784b3c920d6a39de71ccc22202991f5713edfed917c27
auditor-model: claude-opus-4-7[1m]
audit-date: 2026-05-21
fixtures-read: tests/audit-fixtures/01, 07, 12
ingestion-model: claude-opus-4-7[1m] (parent + dispatched subagent for Pass C-E)
ingestion-method: parent dispatched a fresh-context Opus subagent (low AUP risk given doctrinal / abstract register); no rejections; full coverage of 4,478 lines.
notes: This single audit covers both the aarbuddy ingestion (slug 082) and the commons/demo ingestion (slug 00q, replicated by parent). Source SHA, deep ref content, and Pass I findings are identical for both corpora; only the slug-id frontmatter differs.
---

# Pass I source-only audit — MCDP-1 Warfighting (US Marine Corps, 1997)

## Calibration

Audit fixtures 01, 07, 12 read at the start of this pass. The audit walks the deep reference against the converted source (`sources/converted/mcdp1-warfighting.md`, 4,478 lines).

## AUP risk — outcome

Low risk at dispatch (doctrinal / abstract register, US Government public-domain). No rejections during the deep read. Coverage is full.

## Coverage

Deep ref declares `coverage: full (Foreword + Preface + Ch 1-4 + Notes back matter read)` and `image_scope: text-only`. Subagent reported reading the full 4,478 lines in three chunks. Parent verification: deep ref reproduces load-bearing claims of all four chapters; Notes citations (Clausewitz 14×, Sun Tzu 4×, Boyd's *Patterns of Conflict* at Ch 2 Notes 18, Lind 1985 at Ch 4 Notes 11, Gelernter 1991 at Ch 4 Notes 9) all verified. Coverage matches.

## Source-to-claim trace

**Six thesis propositions.** Each tied to verbatim block quotes:

| Proposition | Quote source | Audit |
|---|---|---|
| 1. War's nature is friction / uncertainty / fluidity / disorder / complexity / danger | Ch 1 | verified verbatim |
| 2. Essence is *Zweikampf* — violent struggle between two wills | Ch 1 | verified |
| 3. Marine doctrine is maneuver warfare, not attrition | Ch 2 | verified |
| 4. Tempo is a weapon; OODA loop the mechanism | Ch 2 Notes 18 | verified — Boyd credited |
| 5. Mission tactics: senior gives what and why, never how | Ch 4 | verified |
| 6. Main effort (*Schwerpunkt*) is the focusing discipline | Ch 4 | verified |

**Per-chapter synthesis.** Spot-checks:

- **Ch 1 Nature of War.** Friction, uncertainty, fluidity, disorder, complexity, danger as constitutive. The human dimension (will, morale, cohesion). *"No degree of technological development or scientific calculation will diminish the human dimension in war"* — verified verbatim. The *war vs warfare* distinction — verified.
- **Ch 2 Theory of War.** War as art and science. The lexical move renaming strategic *attrition* as *erosion* (Notes 7) so *attrition* can be reserved for the tactical critique — verified. Friction (Clausewitz, 14 citations across Notes). Centers of gravity and critical vulnerabilities. Surfaces and gaps. Combined arms (*posing the enemy with a dilemma, not a problem*). Tempo. The OODA loop at Notes 18, credited to Boyd's *Patterns of Conflict*. All verified.
- **Ch 3 Preparing for War.** Doctrine as a way of thinking, not a checklist. Leadership. Training. Education. Equipment and weapons as means, not ends. The *zero defects mentality* explicitly rejected; *"severity on errors of inaction, leniency on overbold errors"* verified verbatim. All verified.
- **Ch 4 Conduct of War.** Strategic / operational / tactical levels. The operational design — commander's intent, focus of effort / *Schwerpunkt*, main effort, supporting effort, exploitation. Mission Orders format. Intent must be understood two levels up. *Reconnaissance pull* vs *command push* (Lind 1985 at Notes 11). *Topsight* (Gelernter's *Mirror Worlds*, 1991, at Notes 9). All verified.

**Authorship lineage.** Krulak signs the Foreword (31st Commandant); Gray (Ret.) signs the Preface (29th Commandant). The intellectual lineage — Boyd, Lind, Wyly, Wilson — is uncredited in the document but well-established historically. Deep ref correctly handles the institutional / intellectual-authorship distinction.

**Sun Tzu and Clausewitz.** Both flagged as *essential reading* in the Notes — verified verbatim. Clausewitz's *On War* (Howard/Paret 1984 translation) cited 14 times; Sun Tzu's *Art of War* (Griffith 1982 translation) cited at Ch 2 Notes 2 and Ch 4 Notes 1-2.

**Only non-military / non-historical citation.** Gelernter's *Mirror Worlds* (1991) at Ch 4 Notes 9 for *topsight*. Verified; this is a notable importation from computer-science vocabulary into doctrinal language. Deep ref correctly identifies this as a distinctive lexical move.

## Editorial framing audit

Deep ref's *Connections to corpus* section properly framed as editorial inference. The Boyd → MCDP-1 lineage claim is the operator's accurate framing (well-established historically; MCDP-1 itself doesn't credit Boyd by name in the document body, only at Ch 2 Notes 18 in the citation).

## Scope determination

Scope = **open**. US Government public-domain doctrinal publication. PCN 142 000006 00. Freely distributable. This makes MCDP-1 unique in the aarbuddy corpus among combat / safety-science texts — most others are `copyrighted` or `open-nc`.

## Cross-corpus note

Identical source content has been replicated to `corpus.commons/demo/` under slug-id `00q`. Source SHA256 is identical; deep ref content is identical (only frontmatter slug-id changes). This Pass I audit covers both ingestions.

## Findings

- **0** strip-or-correct issues.
- **0** quote-attribution drift.
- **0** coverage gaps.
- **0** classification-marker misuses.

## Verdict

PASS. Deep ref ships (aarbuddy and commons/demo).
