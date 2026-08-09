# Known limitations

All 27 sources ran the full 9-pass protocol, and the 27-source deep-reference tier was independently re-audited claim-by-claim on 2026-08-08 — 9,364 claims traced to source, every verified finding repaired, receipts published. The text-axis projections, where the matrix's value lives, are complete. One component is partial: image classification for 6 of the 12 OpenStax books (the deep references, light references, distillations, and Pass A/H/I audit artefacts are all present; visual classification of every extracted image, per the 9-pass protocol's image post-pass, was not finished for the sources listed below). Partial coverage is labelled per source, per the source-integrity rule; finish it yourself if your use needs the visual axis.

## What ships and what doesn't

| Component | Status | Where |
|---|---|---|
| 9-pass ingestion under source-only audit | All 9 passes ran across 12 OpenStax books + 15 supplementary sources (27 references total); the original in-context Pass I was superseded by the independent re-audit below | [`corpus.commons/demo/references/`](../../corpus.commons/demo/references/), [`corpus.commons/demo/distillations/`](../../corpus.commons/demo/distillations/) |
| Pass I audit receipts (per source + cross-corpus summary) | Independent cross-family re-audit completed 2026-08-08: 9,364 claims traced at strict claim grain, a pre-repair hard-error rate of 2.6% found, all verified findings repaired and propagated downstream. Receipts in `_audit/independent-2026-08-08/`. The original in-context receipts remain for provenance but are not independent verification. | [`docs/audit-results/`](../audit-results/), receipts in [`corpus.commons/demo/references/_audit/`](../../corpus.commons/demo/references/_audit/) |
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
