# Known limitations

All 28 sources ran the full 9-pass protocol, and every deep reference and every distillation is independently audited claim by claim, every verified finding repaired, receipts published. The text-axis projections, where the matrix's value lives, are complete. One component is partial: image classification for 6 of the 12 OpenStax books (the deep references, light references, distillations, and Pass A/H/I audit artefacts are all present; visual classification of every extracted image, per the 9-pass protocol's image post-pass, was not finished for the sources listed below). Partial coverage is labelled per source, per the source-integrity rule; finish it yourself if your use needs the visual axis.

## What ships and what doesn't

| Component | Status | Where |
|---|---|---|
| 9-pass ingestion under source-only audit | All 9 passes ran across 12 OpenStax books + 16 supplementary sources (28 references total); the original in-context Pass I was superseded by the independent audit below | [`corpus.commons/demo/references/`](../../corpus.commons/demo/references/), [`corpus.commons/demo/distillations/`](../../corpus.commons/demo/distillations/) |
| Pass I audit receipts (per source + cross-corpus summary) | Independent cross-family audit of every deep reference: 9,364 claims traced at strict claim grain across the 2026-08-08 batch, a pre-repair hard-error rate of 2.6% found, all verified findings repaired and propagated downstream; NIST SSDF audited 2026-09-27. Receipts in `_audit/independent-2026-08-08/` and `_audit/independent-2026-09-27/`. The original in-context receipts remain for provenance but are not independent verification. | [`docs/audit-results/`](../audit-results/), receipts in [`corpus.commons/demo/references/_audit/`](../../corpus.commons/demo/references/_audit/) |
| Distillation quotations | Quotations marked `[V]` were checked word for word against the converted sources on 2026-09-27; quotations the source relays from someone else (a named author, law, saying or interviewee) carry `[BT]`. Other quoted text in a distillation (facilitation scripts, key terms) is the distillation's own wording, and the runtime paraphrases it rather than quoting it. | [`corpus.commons/demo/distillations/`](../../corpus.commons/demo/distillations/) |
| Distillation claim audit | Every claim in the 117 distillations audited against its deep reference and source on 2026-09-27: a pre-repair hard-error rate of 5.1% found, every finding re-verified and repaired, deep-reference and task-spec errors fixed upstream, the five MCDP 1 distillations regenerated. An independent pass checked every changed line (96.5% faithful, none contradicted; the rest fixed), and the index files were audited row by row. Receipts in `_audit/distillations-2026-09-27/`. | [`docs/audit-results/`](../audit-results/), receipts in [`corpus.commons/demo/references/_audit/`](../../corpus.commons/demo/references/_audit/) |
| Comparative eval harness (4-method, blind judge) | Runnable in this release; full results summarised qualitatively in the README (corpora used extend beyond the demo corpus) | [`docs/evals/`](../evals/), [`docs/evals/harness/`](../evals/harness/) |
| Image classification | PARTIAL for 6 of 12 OpenStax books (see below) | [`corpus.commons/demo/sources/converted/`](../../corpus.commons/demo/sources/converted/) |
| Semantic-search retrieval | Persisted Chroma collection ships with the repo | [`scripts/setup-chroma.py`](../../scripts/setup-chroma.py), [`docs/architecture/two-layer-indexes.md`](../architecture/two-layer-indexes.md) |
| Lens pre-projection (per-distillation modifier) | Lens library shipped; per-distillation applicability decided at Pass G | [`corpus.commons/demo/lenses/`](../../corpus.commons/demo/lenses/) |

## Architectural limits

The architecture's intrinsic limits—what the matrix cannot do by design—are documented at [`docs/architecture/known-architectural-limits.md`](../architecture/known-architectural-limits.md). The limits below are *operational*: gaps in the current release, fillable in later work.

## What's partial

| Source | Status |
|---|---|
| `psychology-2e` | ~6 substantive image entries; ~324 unclassified JPEGs remain |
| `economics-3e` | ~21 curated entries; ~265 unclassified JPEGs remain |
| `accounting-vol1` | ~10 confirmed entries; ~38 unclassified PNGs remain (plus the JPEG bulk) |
| `principles-management`, `principles-marketing`, `principles-finance` | Image entries present but in stub format; per-figure descriptions not yet authored |

The PARTIAL labelling is honest: per the source-integrity rule, partial coverage must be explicitly marked, never silently delivered. The IMAGE-INDEX.yaml entries for these sources carry comments to that effect.

## Completion procedures

To finish the image classification or to clear the demo and start fresh, see [`docs/how-to/extend-or-clear-the-demo.md`](../how-to/extend-or-clear-the-demo.md).
