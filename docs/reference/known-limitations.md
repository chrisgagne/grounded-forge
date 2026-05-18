# Known limitations

The OpenStax demo corpus is a working illustration, not a polished product. A few of the books ship with image classification labelled PARTIAL: the deep references, light references, distillations, and Pass A/H/I audit artefacts are complete, but visual classification of every extracted image (per the 9-pass protocol's image post-pass) was not finished for some sources. Most users won't care, the matrix architecture's value is in the text-axis projections, but if you want full coverage you can finish the work yourself.

## What ships and what doesn't

| Component | Status | Where |
|---|---|---|
| 9-pass ingestion under source-only audit | Complete for 12 OpenStax books + 14 supplementary sources (26 references total) | [`corpus.commons/demo/references/`](../../corpus.commons/demo/references/), [`corpus.commons/demo/distillations/`](../../corpus.commons/demo/distillations/) |
| Pass I audit receipts (per source + cross-corpus summary) | Complete | [`docs/audit-results/`](../audit-results/), full logs in [`corpus.commons/demo/references/_audit/`](../../corpus.commons/demo/references/_audit/) |
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
