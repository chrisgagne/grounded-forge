# Independent Pass I re-audit — 2026-08-08

The fresh-context, cross-model re-audit the README promised. Every deep reference in the demo corpus was audited at strict claim grain by a model from a different family (`gpt-5.6-sol`) than the model that produced it (Claude Opus), in a fresh session with no producing context. This replaces the retired in-context self-audit receipts as the corpus's audit-of-record.

## Method

Per source: the auditor read the deep reference in full and verified every in-scope subject-matter claim against the converted source (`sources/converted/{slug}.md`) by targeted search plus reading of matching regions, graded strictly (grade down on doubt) as FAITHFUL / MINOR-DRIFT / UNSUPPORTED / CONTRADICTED. Scope excludes the metadata header, licence/provenance notes, conversion notes, and structural tallies (these are legitimately external to the source text). "Hard" = UNSUPPORTED + CONTRADICTED. The audit was primed for the known producer failure modes: attributions to people the source never names, enumeration miscounts, dropped qualifiers, dated-fact drift, and non-verbatim [V] quotes. 17 sources were audited on 2026-08-08; 10 carry forward from the same auditor's matched-method pass of 2026-07-29 to 2026-08-01. Per-source machine-readable findings, including every error with the searches used and the source check, are the JSON receipts beside this file.

## Result, pre-repair

| Measure | Value |
|---|---|
| Deep references audited | 27 of 27 |
| Claims audited | 9,364 |
| Hard errors (UNSUPPORTED + CONTRADICTED) | 239 (2.6%) |
| Hard errors excluding cross-corpus Connections flags | 224 (2.4%) |
| MINOR-DRIFT (qualifier loss, marker misuse, paraphrase marked [V]) | 291 (3.1%) |
| Clean at strict claim grain | 97.45% |
| Fully FAITHFUL | 94.34% |

Per-source table: [`SUMMARY.txt`] in the audit staging set; the distribution is uneven. Three sources carried a third of all hard errors (open-practice-library 14.9%, openstax-entrepreneurship 4.5%, approach-perfect-field-guide 5.7%); ten sources sat at or under 1.5%; scrum-guide-2020 audited fully clean.

The dominant hard-error classes, in order: attributions to named people the source never names (training-data leakage: Akerlof, Maslow, David J. Anderson, Dave Snowden, Edward de Bono, Taiichi Ohno, and others, each absent from its source); enumeration miscounts (N-vs-M lists); taxonomy misassignment (open-practice-library's Mobius-phase labels); conflated or spliced source models (entrepreneurship's life-cycle vs funding stages); and dropped bounding qualifiers on figures. The dominant MINOR-DRIFT class is marker discipline: paraphrases and borrowed definitions carrying [V].

## Repair

Every flagged error was independently re-verified against the converted source by a separate repair agent before any edit (auditor findings were not applied blind), then fixed in the deep reference with minimal-diff edits and chased into the light reference and every task distillation where it had propagated. Fix classes: delete fabricated attributions and unsupported claims; correct counts to the source's actual count; restore dropped qualifiers; downgrade [V] to [AP]/[BT] where the text is paraphrase or borrowed; record source-internal inconsistencies rather than silently resolving them; mark conversion gaps (truncated tables/figures) as unverifiable rather than asserting their content.

Across the 27 sources: **446 audit findings repaired** (445 verified-and-fixed; 1 finding rejected on re-verification — the auditor had missed the source's "5 whys" spelling, and the flagged claim was retained as source-supported), plus **412 propagated fixes** applied where the same errors had reached light references, distillations, and two operator-view distillation indexes. A further 19 defects found by repair agents *outside* their briefs (in neighbouring files or unflagged passages) were verified and fixed individually.

**Post-repair verification.** Fresh Sol sessions re-verified the six worst-audited sources (open-practice-library, ssdl, mcdp1, open-kanban, approach-perfect-field-guide, entrepreneurship) finding-by-finding against the repaired files: two passed outright, and the residual defects flagged in the other four (retained categorical phrasings, three marker misuses, two formatting breaks, one imprecise practice list, one unverifiable README quotation) were then fixed and are reflected in the shipped files. The remaining 21 sources carry their repair agents' per-finding verification records without a second independent post-repair pass; their findings were smaller and of the same classes.

## What this does and does not establish

This audit establishes that every claim in the shipped deep references has been traced against its converted source by an independent, cross-family auditor, and that the claims that failed the trace have been repaired or removed. It does not establish that the residual error rate is zero: single-audit coverage reduces but does not eliminate injected error, judge variance at strict claim grain is real, and conversion gaps mean some source regions (truncated tables, figure interiors) cannot support verification either way. The audit also cannot verify a source's relation to the world; source selection remains the operator's accountability.

The retired 99.4% figure came from an in-context self-audit that certified the producing model's own errors; it is not comparable to any number here. The honest pre-repair figure under independent audit was 97.45% clean at strict claim grain; the post-repair corpus carries the repairs listed above with verification receipts per source.
