# OKF interop: the container standardised; the producer didn't

*Claims in this page are pinned to OKF v0.2, the current spec version as of July 2026. The spec is young and will move; the emitter and this page name their target version rather than claiming timeless conformance.*

## What OKF is

The Open Knowledge Format ([OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog), Apache-2.0) is a Google Cloud specification, published 12 June 2026, for shipping knowledge as a **bundle**: a directory tree of markdown concept files. One file per concept; the concept's id is its file path; YAML frontmatter with one required field (`type`); standard-markdown cross-links; reserved `index.md` files as progressive-disclosure routers; optional provenance (`sources`), trust (`generated`, `verified`), and lifecycle (`status`, `stale_after`) frontmatter families. Conformance is deliberately lax on the consumer side — consumers must tolerate unknown types, missing optional fields, and links whose targets are not in the bundle — which makes the format cheap to adopt and hard to break.

That description should sound familiar. It is the substrate this repo already runs on: markdown artefacts, curated routers, deterministic navigation preferred over embedding retrieval, git as the distribution channel. The prior-art section of the [README](../../README.md#prior-art) traces the same convergence through Jerry Liu's file-system retrieval and Karpathy's LLM wiki; OKF is the strongest instance yet because it is a platform vendor writing a spec, not a practitioner writing an essay. The matrix architecture was in production by 15 February 2026, four months before the spec was published; the convergence is independent, and it is evidence that the *container* argument is settling.

## What OKF specifies, and what it leaves open

OKF specifies the container: file shapes, frontmatter fields, link syntax, reserved names, trust-field conventions. It is silent on the **producer**: nothing in the spec says how a concept file gets made, what its claims trace to, who audited them against what, or how drift is caught when the underlying source moves. That silence is by design — a format spec should not mandate a methodology — but it relocates the hard problem rather than solving it. A conformant bundle full of confabulated claims validates exactly as cleanly as a conformant bundle of audited ones.

Google's own reference implementation makes the gap concrete: its producer is an LLM enrichment agent over BigQuery metadata and web crawl, with no source-only audit pass. For warehouse metadata, that is a reasonable trade. For a corpus of books, papers, and doctrine — the material this repo ingests — an un-audited probabilistic writer is the exact failure class the 9-pass protocol's Pass I exists to neutralise (see [`source-integrity.md`](source-integrity.md) and [`llm-epistemology.md`](llm-epistemology.md)).

So the two artefacts compose rather than compete: **OKF is a container; grounded-forge is a producer with an audit discipline.** From v0.4.0 the build emits the former from the latter.

## The mapping

The emitter (`scripts/lib/emit-okf.js`, wired into `build.js`) is a serialiser, not a transform. Every OKF surface maps from an artefact the ingestion already built and audited; nothing re-reads a source or re-derives a claim.

| grounded-forge artefact | OKF surface |
|---|---|
| distillation `{slug}-{task}.md` | concept file `/{task}/{slug}.md`, `type: distillation` |
| distillation body (verbatim, evidence markers in-band) | concept body (in-bundle cross-links repathed; content untouched) |
| `task-index.json` situation router | reserved `/{task}/index.md`, grouped link lists |
| lens spec | concept file `/lenses/{slug}.md`, `type: lens` |
| `**Source:**` line + `.source.md` sidecar `url:` | `sources:` family + `resource:` |
| `distillation-sources.json` (scope + licence per source) | `LICENCE-MANIFEST.md` (`type: licence-manifest`) + per-file `scope:` |
| `concept-index.json` co-occurrence | appended "Related concepts" links, labelled with the shared concepts |
| build identity + corpus git history | `generated: {by: grounded-forge/{version}, at: <last change of the source distillation>}` |

Two properties fall out of "serialise the built app, not the corpus":

1. **Every distribution gate applies to bundles by construction.** The emitter's input is the compiled app output, which has already passed the `max_scope` ceiling, the `max_visibility` ceiling, and the verbatim-restriction gate ([V] markers refused above open-nc scopes). A bundle is an interchange format whose whole purpose is to leave your controlled runtime; it inherits exactly the protections the apps and tarballs have, with no second gate implementation to keep in sync.
2. **Bundles are deterministic.** Rebuilding an unchanged corpus produces a byte-identical bundle. The only timestamp emitted is `generated.at`, taken from the source distillation's last git commit — stable until the distillation itself changes. Tracked bundles diff clean.

## What travels, and what doesn't

A generic OKF consumer gets the full data layer: every audited distillation with its evidence markers (`[V]`/`[AP]`/`[AR]`/`[AE]`/`[BT]`) and attribution in-band, typed and cross-linked, routed by `index.md`, licence-labelled by the manifest. That is more provenance than the format requires and more than most bundles carry.

What does *not* travel is the discipline that produced and consumes it. The situation-router semantics beyond progressive disclosure, lens *application* (a consumer sees lens specs as typed concept files; nothing in OKF says "apply this lens when it materially reweights salience"), the `answer-from-corpus` retrieval procedure, and the citation conduct in each app's CLAUDE.md are runtime, and OKF has no runtime. The bundle is the data layer; the application is the assistant. An OKF-aware tool reads the matrix's artefacts; only a grounded-forge app reads them *under the rules*.

## Trust fields: deliberately conservative

OKF v0.2's trust model derives tiers from `verified:` — unverified, machine-confirmed, human-reviewed. Emitted concept files declare `generated:` (actor `grounded-forge/{version}`, per the spec's producer/version convention) and **do not declare `verified:`**, so every concept file reads as *unverified* to a trust-aware consumer.

That is deliberate. Pass I — the source-only audit behind every distillation — is run by the same model family that produced the references; the repo's own eval documentation describes it as internal consistency, not independent verification. Claiming OKF's `verified:` on that basis would launder an internal check into an external assurance. The audit receipts live at corpus level in the producing repository (`docs/audit-results/`); the bundle's root `index.md` says exactly that. When the format's trust semantics and the repo's honesty standard disagree about what "verified" means, the honest reading wins.

## The task axis, expressed in a format that lacks one

OKF's model is one canonical file per concept; it has no task dimension. But concept ids are file paths, and directory nesting is unrestricted — so the bundle *expresses* the task axis as structure: `/decision-making/openstax-organizational-behavior.md` and `/retro/openstax-organizational-behavior.md` are different concept files, same source, different projection, each linking its siblings ("Same source, other task axes").

The shipped `matrix` bundle carries all five demo task axes — 116 concept files from 27 sources — in one tree. Diffing any two axis directories shows the same sources projected differently, which is the matrix architecture made visible inside someone else's format. A consumer that knows nothing about task axes still navigates it correctly, because to OKF it is just directories; a consumer that reads the root `index.md` learns what the directories mean.

## Validation and the receipt

Conformance is checked twice:

- **Build-time (Node, always on):** every emitted concept file carries frontmatter with `type:`; reserved files carry none (root `index.md` may declare only `okf_version`); every bundle-absolute link resolves inside the bundle. Violations fail the build.
- **External (Rust CLI, the receipt):** the community [`okf` toolkit](https://crates.io/crates/okf) (`cargo install okf`) tracks spec v0.2. As of the v0.4.0 release, all six shipped demo bundles pass `okf validate` — 0 errors — and `okf info` reports the full internal link graph unbroken. The residual warnings are honest ones: `mcdp1-warfighting` records no source URL anywhere in the corpus of record, so its concept files carry no `resource:` field rather than an invented one.

The decision to emit rather than fork Google's producer is recorded in [`decisions-and-non-decisions.md`](decisions-and-non-decisions.md). The operator procedure is in [`docs/how-to/emit-okf.md`](../how-to/emit-okf.md).
