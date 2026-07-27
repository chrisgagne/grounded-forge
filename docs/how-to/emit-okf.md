# Emit an OKF bundle

Serialise a profile's gated output as an Open Knowledge Format (OKF v0.2) bundle: a portable directory of markdown concept files any OKF-aware tool can consume. Why the format and the matrix compose — and what does and doesn't travel — is in [`docs/architecture/okf-interop.md`](../architecture/okf-interop.md).

## Commands

```bash
npm run build:matrix        # the all-axes demo bundle -> corpus.commons/demo/okf/matrix/
npm run build               # all profiles; every okf-enabled profile emits its bundle
node build.js decision      # one app profile; its bundle lands beside apps/ at {corpus}/okf/decision/
```

Emission is opt-in per profile in `builds.yaml`:

```yaml
my-profile:
  # ...existing profile fields...
  okf: true    # emit a bundle alongside the app, after app validation passes
  # or
  okf: only    # emit the bundle and no app (see the matrix profile)
```

`okf: true` bundles land at `{corpus}/okf/{profile}/`. `okf: only` profiles put the bundle at their `output_dir` and skip the app furniture (skills, agents, CLAUDE.md, docs) entirely — the gated pipeline runs into a throwaway staging directory and only the bundle ships. Field reference: [`docs/reference/build-profile-schema.md`](../reference/build-profile-schema.md).

## What you get

One concept file per (source, task) cell at `/{task}/{slug}.md`, carrying the distillation body verbatim — evidence markers and attribution in-band — under OKF frontmatter (`type: distillation`, `title`, `description`, `resource`, `sources`, `generated`, plus `task:` and `scope:` extension keys). Each task axis gets a reserved `index.md` rendered from its situation router. Lenses travel as `type: lens` concept files under `/lenses/`. The bundle root carries `index.md` (with the `okf_version` declaration, the evidence-marker legend, and the trust-model statement) and `LICENCE-MANIFEST.md` (per-source scope and licence; the bundle inherits the most-restrictive scope).

Because the emitter's input is the *built app*, the profile's `max_scope` and `max_visibility` ceilings and the [V]-verbatim gate have already been applied. A bundle can never carry material its profile's app could not.

## Validate

The build validates every bundle itself (frontmatter, reserved-file rules, internal links) and fails on violations. For the external check against the spec, use the community Rust CLI:

```bash
cargo install okf
okf validate corpus.commons/demo/okf/matrix    # conformance (spec §11)
okf info corpus.commons/demo/okf/matrix        # types, trust tiers, link graph
```

All six shipped demo bundles pass `okf validate` with 0 errors. Concept files deliberately carry no `verified:` field — see the trust-fields section of [`okf-interop.md`](../architecture/okf-interop.md) for why the bundles read as machine-generated rather than verified.

## Ship it

```bash
node scripts/package.js matrix              # okf-only profiles package their bundle
node scripts/package.js decision --okf      # package an app profile's bundle
```

Either produces a scope-labelled tarball in `{corpus}/distros/` — for example `matrix-okf-v0.4.0-open-nc.tar.gz` — with the licence manifest inside and a collision-safe `{profile}-okf/` top-level directory. The recipient untars and points any OKF v0.2 consumer at it. The scope suffix is the constraint travelling with the artefact: distribute only to recipients authorised at that level.
