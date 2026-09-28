# Demo distillation audit and repair, 2026-09-27

The first claim-level audit of the distillation tier, the layer compiled apps ship. Every one of the 117 demo distillations was audited against its deep reference and the converted source, repaired, and the repair checked by a second, independent pass. The index files that route the apps to distillations were audited the same way.

## Audit

Claude Opus, one agent per source, following `BRIEF.md`. A claim the source supports but the deep reference lacks was graded minor drift, with a fix to add it to the deep reference.

| | Count |
|---|---|
| Distillations | 117 |
| Claims audited | 16,204 |
| Faithful | 13,257 |
| Minor drift | 2,119 |
| Unsupported | 622 |
| Contradicted | 206 |
| Hard errors (unsupported + contradicted) | 828 (5.1%) |

Hard-error rates ran from 0% (NIST SSDF, the one distillation written under the September protocol) and 1.3% (NHS Just Culture Guide) to 11.2% (MCDP 1). By axis, retro (6.2%) and software-business (6.0%) were worst; software-business distillations pulled in outside technical knowledge under book citations. Several errors started in the deep references or the task specs rather than the distillations; `DEEP-REF-FIXES.md` lists them. A calibration run on four distillations found 57 hard errors with Opus against 9 with Sonnet, so the audit used Opus throughout.

## Repair

Per-source Opus agents, following `repair/BRIEF.md`. Each finding was re-verified at source before any edit.

- **Deep references first.** 543 changes: 207 corrections, 278 passages added from the source, 58 coverage extensions where a distillation had quoted sections the deep reference did not carry.
- **Distillations.** 2,823 findings on 112 distillations: 2,407 applied as written, 410 revised because the audit's own fix was wrong or loose, 6 rejected with source evidence. Agents fixed a further 298 recurrences the audit had logged once.
- **MCDP 1.** Its deep reference carried non-source content (a Boyd lineage, *Auftragstaktik*, *Schwerpunkt*, links to another corpus); that was removed and the five distillations regenerated from the cleaned deep reference (`repair/MCDP1-REGEN-BRIEF.md`). A fresh audit of the new files found 1 unsupported claim and 23 minor drifts in 853 claims (0.1% hard, from 11.2%); all were fixed.
- **Task specs.** The `software-business`, `aar` and `retro` specs had seeded attributions the sources do not support: Conway's Law through Letaw, the six structure types as Mintzberg's, a flow-over-utilisation stance for Open Kanban, a five-segment retro agenda for the Field Guide (it has six). These are corrected so regeneration does not bring them back.
- **Priority fixes.** The LFUO guide tells interviewers not to take a person back into deep recall of a traumatic event and to leave that to mental health professionals; every distillation now says so. Psychology 2e is licensed CC BY-NC-SA 4.0. The reinforcement-schedule ranking in the OB and Psychology 2e retro distillations is the right way round. The Field Guide treats both the Sprint Goal and the Sprint Backlog as forecasts, not firm commitments. The Accounting Vol 2 build-or-buy example now counts the opportunity cost and reaches the verdict the source's rule gives.

## Independent check

A fresh Opus agent per source audited every changed line against the source (`check/BRIEF.md`).

| | Count |
|---|---|
| Changed lines checked | 3,983 |
| Faithful | 3,842 (96.5%) |
| Minor drift | 119 |
| Edit defects | 40 |
| Unsupported | 10 |
| Contradicted | 0 |

All were fixed. The check also caught a scripted fix step that had pasted auditors' instructions into seven lines and misapplied four marker changes; all are repaired, and a search of the corpus finds no residue.

## Index audit

The `*-DISTILLATION-INDEX.md` files generate each app's runtime router, and no one had audited them. Thirteen batches checked 2,264 rows against the distillations they point to (`index/BRIEF.md`): 381 rows were corrected, re-pointed to a distillation that carries the content, or, in 5 cases, deleted because no distillation on the axis carries it. This is on top of 465 row fixes the repair agents proposed for their own distillations.

## Open items

- **Source error, for the Field Guide's next edition.** The velocity worked example gives ≈30 Story Points; its own inputs give (25/45 + 24/43 + 31/50)/3 × 47 = 27.2. The distillations report the figure as the source gives it.
- **MCDP 1 applicability.** The stakeholder-engagement and software-business projections passed the applicability gate as ambiguous, not clear yes; both are kept with a narrowed scope that each file states.
- **Verbatim checking.** A mechanical check flags 60 `[V]` quotations whose words break across page headers, multi-column PDF text or OCR garbles; each was read at source and is faithful.

## Files

- `BRIEF.md`, `{slug}-{task}.json`: the audit brief and findings.
- `DEEP-REF-FIXES.md`: deep-reference and task-spec errors the audit traced upstream.
- `repair/`: per-distillation repair logs (the action on every finding), deep-reference change logs, index-row proposals, and the briefs.
- `check/`: the independent check's findings per source, the MCDP 1 re-audits, and the fix logs.
- `index/`: the index audit's findings and row edits per batch.
