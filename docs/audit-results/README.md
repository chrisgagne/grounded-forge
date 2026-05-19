# Pass I audit summaries

Pass I of the 9-pass ingestion protocol is the source-only audit. Every body claim, table cell, evidence-class marker, and cross-reference in a deep reference is read cold against the converted source markdown; the question per claim is "can I trace this to a passage in the source?". Where the answer is no, the claim is stripped or flagged. The deep reference does not ship until Pass I passes.

Pass I produces a per-source audit log. The full logs ship in the source repo under [`corpus.commons/demo/references/_audit/`](../../corpus.commons/demo/references/_audit/) (Pass A ledgers, Pass H verification, Pass I source audits). They are excluded from the compiled distribution.

Pass H's audit shape changed under the mechanical-index migration. Pre-migration Pass H was an LLM-authoring step ("did the agent author the right concept-axis entries?"); the audit asked whether inferred concept entries matched the source's actual concept coverage. Post-migration Pass H is a deterministic preprocessor plus two constrained Sonnet passes, with the build assembling JSON indexes mechanically; the audit shape is now whether the preprocessor extracted the right structure and whether the Sonnet cross-link pass made the right alias / merge / novel calls. A Phase-5 corpus-wide re-run will surface that audit; for now Pass H verification logs continue to live alongside Pass I logs at the same path. See [`../architecture/ingestion-protocol.md`](../architecture/ingestion-protocol.md) §Pass H for the rationale.

This file is the cross-corpus summary across the 12-book OpenStax portion of the demo corpus.

## Aggregate

| Statistic | OpenStax corpus |
|---|---|
| Sources audited | 12 |
| Total claims audited | ~3,080 |
| Claims source-anchored without modification | ~3,062 |
| Marker corrections | 7 |
| Strips (no source support) | 7 |
| Other fixes (verbatim slips, rewordings) | 4 |
| Approximate uncorrected-claim rate at first read | ~99.4% |
| Task-application guidance found in deep ref (tier violation) | 0 |
| Post-source vocabulary detected | 0 |

The headline number is the **uncorrected-claim rate at first read (~99.4%)**: of every 1000 claims a deep reference asserts, ~6 needed correction or strip before the deep was deemed shippable. The most common failure modes were (a) evidence-marker mismatches (claim is real but the verbatim-vs-paraphrase marker was wrong) and (b) over-claiming verbatim wording slightly different from the source. Tier-violations (task-application guidance leaking into the deep ref) and post-source vocabulary (terms or framings not in the source) were caught at zero. Those are guarded by Pass C's citation discipline, not by Pass I.

## Per-source

| Source | Claims audited | Anchored | Marker fix | Strip | Other fixes |
|---|---:|---:|---:|---:|---:|
| accounting-vol1 | 320 | 318 | 1 | 1 | 0 |
| accounting-vol2 | ~220 | ~217 | 0 | 0 | 1 verbatim slip |
| business-ethics | (sectional, 100% pass) | all | 0 | 0 | 0 |
| business-law | ~310 | 308 | 0 | 0 | 0 |
| economics-3e | ~340 | all | 0 | 0 | 0 |
| entrepreneurship | ~210 | ~208 | 1 | 1 | 0 |
| introduction-business | 230 | 227 | 1 | 0 | 1 verbatim slip |
| organizational-behavior | 280 | 277 | 1 | 1 | 0 |
| principles-finance | ~240 | 239 | 1 | 0 | 0 |
| principles-management | ~310 | ~306 | 1 | 1 | 2 rewordings |
| principles-marketing | 230 | 229 | 0 | 1 | 0 |
| psychology-2e | 190 | 188 | 1 | 1 | 0 |

Counts vary in granularity per source. Some audits used a tabular count (lines and sections); others (`business-ethics`, `economics-3e`) used a sectional-pass-fail format because the source's structure made section-by-section verification more natural than per-claim aggregation.

## What Pass I does and does not catch

Pass I verifies fidelity to source. It does not and cannot verify quality of source. A 9-pass source-only protocol against a derivative or fashionable source produces a faithful projection of derivative or fashionable content. **Source selection is the operator's job and the rule the protocol does not enforce.** See [`source-integrity.md`](../architecture/source-integrity.md) for the integrity rule and what it covers.

**The 99.4% is not a runtime-answer-accuracy number.** Pass I checks backward: it reads claims that were already written into a deep reference, cold, against the converted source. The 99.4% says *when the writer model deliberately left a citation trail, the trail resolved on re-read*. It does not say *runtime answers grounded in these deep references will be 99.4% accurate*. A runtime answer inherits the deep references' citation-fidelity only as long as it stays inside Pass-I-audited material. The moment the answer synthesises, extrapolates, or fills a gap around the projected material, Pass I no longer covers it. The audit-fidelity claim is strong and defensible. The runtime-accuracy claim needs a different eval.

For the empirical question of whether pre-projection actually improves end-user answer quality compared to (a) generic Claude, (b) Claude with research forced, or (c) Claude with raw source files, see the [comparative eval methodology](../evals/methodology.md) and harness shipped alongside.

## Reading the per-source logs

Each `_ingest_pass_I_{slug}_source_audit.md` file documents:

- The audit procedure for that source (how the cold-read and verification by grep was performed).
- The audit-result counts (claims audited, anchored, marker-corrected, stripped).
- Each specific fix applied during the audit, with location (line in deep ref pre-fix), the original text, the issue, and the fix.
- Spot-checks performed (claim, source-citation, verification line).
- Notes for future re-ingestion.

The log is the integrity record. If a downstream user wants to re-verify a specific claim in a deep reference, the corresponding audit log is the entry point.
