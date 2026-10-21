## 1. What I read

Read in full:

- `sort-brief.md`, all three calibration fixtures and `pass-i-spec.md`.
- `blind-findings.md`, `fixer-audit-log.md` and `post-audit-deep.md` (526 lines).
- `tape.md` (2,172 lines).
- Repository `CLAUDE.md` and its nine required architecture documents.
- `source-card.md` and the current corpus light reference.

Compared the complete frozen/post-audit diff: only lines 19 and 462 changed. Both supplied deep-reference hashes match. The original PDF’s hash matches the source card.

Independently rendered printed PDF pages 8, 13 and 55. These establish the diagram’s layout, the garbled scenario heading and the image-only sponsor material. I did not visually inspect every PDF page.

The repository verbatim checker, run against `post-audit-deep.md` with `tape.md` explicitly supplied, reported **no findings**.

No files were edited; this response is the report.

## 2. Sorted ledger

All deep-reference locations below refer to `post-audit-deep.md`. Compound audit findings are separated where their components require different judgements.

| ID | Raised by | Deep line | Source location | Classification and determination |
|---|---|---:|---|---|
| F1a | Fixer | 19 | Tape 1683–1686, p. 44 | **Confirmed and fixed.** The source makes the ASI Exploits and Incidents **initiative** the subject seeking to inform and establish the Top 10. The frozen wording substituted the tracker and added “run by”. The replacement correctly restores the source’s subject and removes the unsupported administrative attribution. |
| F1b | Fixer | 19 | Tape 1683–1684, p. 44 | **Disputed.** The fixer also called `[AR]` incorrect. One reading treats this as a reported organisational purpose, favouring `[AP]`; another treats the purpose statement as part of the authors’ argument for the initiative, permitting `[AR]`. The source supports the content under either reading. Retain the present `[AP]`; no further edit is required. |
| F2a | Fixer | 462 | Tape 340–347, 711–727, 810–812, 1777–1786, 1808–1814, 1826–1837, 1868–1879, 1898–1911 and 1936–1954; pp. 10, 19, 22, 46–49 | **Over-flagged by fixer.** The original comparison states directly checkable relationships between passages in this source. It neither imports external analysis nor explicitly attributes the comparison to the authors. Calling it “ingester’s comparison” improves provenance clarity, but its previous absence does not establish a source-fidelity defect. The retained edit is accurate. |
| F2b | Fixer | 462 | Tape 724–727 and 1054–1056, pp. 19 and 28 | **Over-flagged by fixer.** Omitting ASI07 scenario 5 did not invalidate the seven-name tally: Agent-in-the-Middle was already represented through ASI04 scenario 6. The paragraph did not promise every occurrence of each name. Adding the second occurrence is supported supplementary detail, rather than a necessary completeness correction. |
| B1 | Blind; fixer considered and retained | 49 | Tape 308–310, p. 9 | **Missed by the fix-in-place audit.** The source qualifies planning with “when used”. Restoring that qualification preserves the source’s explicit scope: planning is conditional within the broader description of agentic impact. The fixer’s decision to retain the omission leaves this defect unresolved. |
| B2 | Blind | 29 | Original PDF, printed p. 8 / PDF p. 9; labels at tape 252–277 | **Missed by the fix-in-place audit.** The rendered Connected data/RAG box straddles the Inputs–Integration/Processing boundary. The reference groups it wholly within Integration/Processing. Memory is inside that panel; Connected data/RAG connects bidirectionally to it. The blind correction is supported. |
| B3 | Blind | 526 | Internal metadata: deep line 2 is blank; no tape counterpart | **Missed by the fix-in-place audit.** The sentence directs readers to a nonexistent stamp. This is a broken internal reference, not evidence that an unearned stamp was applied. The fixer explicitly leaves stamping to the driver, which does not make the present pointer valid. |

There are **no confirmed findings whose substantive fixes remain wrong or incomplete within the deep reference**.

The fixer also raised two findings outside the deep reference:

| Location | Raised by | Source location | Determination |
|---|---|---|---|
| Light reference, line 13 | Fixer | Tape 1683–1684, p. 44 | **Confirmed, correction outstanding outside this sort’s edit scope.** “Its incident tracker seeks…” repeats the subject substitution. The current light reference still contains it. Excluded from deep-reference capture counts. |
| Light reference, line 61 | Fixer | The scenario/tracker passages listed under F2a | **Over-flagged by fixer.** “Several tracker rows share names with entry scenarios” accurately describes the source’s contents. Explicitly labelling the comparison is optional clarification. |

The audits’ retained-clean determinations concerning imperative mitigations, explicit oppositions, borrowed-through references, source inconsistencies, sponsor statements and section coverage hold against the supplied source.

**New defects introduced by fixer edits:** none found. Line 19 now follows the source’s subject and wording. Line 462’s added ASI07 occurrence, page citation and provenance label are supported. Sharing a name does not assert that the MCP and A2A scenarios are the same incident.

## 3. Remaining edits

Apply these three changes to `post-audit-deep.md`.

1. **Line 49 — restore the planning qualifier.**

   Current:

   > planning ("panning" as printed) and multi-step behaviour

   Replacement:

   > planning (when used; "panning" as printed) and multi-step behaviour

2. **Line 29 — replace its opening sentence with the following two sentences.**

   Current:

   > The diagram, read from the render, has three panels: Inputs (User Prompts, API, External Agents); Integration/Processing (Policy & Governance and Human-in-the-loop above a box holding two Agents, with Memory and Connected data/RAG below it); and Outputs (Tools, which lead to APIs/Resources, and External Agents) (p. 8) [AP].

   Replacement:

   > The diagram, read from the render, has three panels: Inputs (User Prompts, API, External Agents); Integration/Processing (Policy & Governance and Human-in-the-loop above a box holding two Agents, with Memory below it); and Outputs (Tools, which lead to APIs/Resources, and External Agents). Connected data/RAG straddles the boundary between Inputs and Integration/Processing, below-left of the agent box, and connects bidirectionally to Memory (p. 8) [AP].

3. **Line 526 — strip only this final sentence.**

   > Pass I: see the stamp on line 2 and the audit log.

## 4. Counts

Counts below use the atomic findings distinguished in the ledger. “Missed” is a subset of confirmed defects.

| Classification | Deep reference | Outside deep reference | Total |
|---|---:|---:|---:|
| Confirmed defects | 4 | 1 | 5 |
| Confirmed and fixed | 1 | 0 | 1 |
| Confirmed, correction outstanding | 3 | 1 | 4 |
| Missed by fixer | 3 | 0 | 3 |
| Over-flagged by fixer | 2 | 1 | 3 |
| Over-flagged by blind auditor | 0 | 0 | 0 |
| Disputed | 1 | 0 | 1 |
| New defects introduced by fixer | 0 | — | 0 |

For capture, the fixer’s explicit rejection of the planning omission as a defect does not count as raising a confirmed defect. Optional clarifications, the disputed marker judgement and light-reference findings are excluded.

Capture: fixer=1 blind=3 both=0

## 5. Gate verdict

**Pass once the three remaining edits are applied.** The source supports the retained substantive content, quotation checking is clean, TOC coverage is complete, and neither fixer edit introduced a new defect.

The present snapshot still requires those edits. Final logging and stamping, followed by derived-tier re-derivation and provenance stamping, remain the driver’s separate completion steps.