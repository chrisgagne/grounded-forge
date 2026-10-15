# Copyright

**Caveat first: the author is not a lawyer, the AI that helped write this isn't either, and nothing here is legal advice. Unlawful use is not endorsed. The risk of any operator choice is the operator's; checking with qualified counsel in the operator's jurisdiction is the operator's job.**

The build system and the ingestion protocol are neutral infrastructure. They work on whatever the operator points them at. Whether copyright concerns arise depends on the operator's situation, not on anything the tool does.

## A few use patterns the author has thought about

- **Private or internal knowledge base.** A team using the matrix on their own internal materials, licensed reference works, or documents they have rights to. Sits between the team and the rights holders.
- **Personal library.** An individual using the matrix on books they have legitimately obtained a licence to use for the purpose, producing a personal knowledge base they don't redistribute.
- **Public distribution with explicit permission.** CC-BY 4.0, public domain, or sources licensed for redistribution. Follow the licence.
- **Public distribution without explicit permission.** The case where the question is most live. I personally find this idea too risky for my own context. Talk to a lawyer in your jurisdiction before publishing at any scale.

## What this repo's defaults are

The shipped demo corpus is mixed-licence open or open-nc material: the OpenStax twelve-book set is mostly CC BY-NC-SA 4.0 (one volume, *Introduction to Business*, is CC BY 4.0), and the supplementary sources span CC BY 4.0, CC BY-SA 4.0, US-government public-domain, and several methodology documents under various permissive open licences. Derivative artefacts (deep references, light references, distillations) inherit each source's licence. Each deep reference records its licence and scope in frontmatter. See [`../../LICENSE-CONTENT`](../../LICENSE-CONTENT) for the full split, and `npm run remove-corpus:openstax` to strip the OpenStax-derived content for commercial use.

## Scope, the mechanical layer

Above the *legal* layer sits a *mechanical* layer the build and packager do enforce. Each deep reference carries a `**Scope:**` field (`open`, `open-nc`, `copyrighted`, `confidential`, or `personal`). Each build profile declares a `max_scope` ceiling. The build excludes references whose scope exceeds the ceiling. `personal` is admitted by no profile.

`npm run package` extends the same mechanism into shipped tarballs. The packager:

- Computes the most-restrictive scope across the bundled references and stamps it into the tarball filename (`decision-v0.2.1-open-nc.tar.gz`). The constraint travels with the artefact: a recipient who sees `confidential` in the filename sees the constraint before opening the file.
- Writes a `LICENCE-MANIFEST.md` into the tarball at the root, one row per reference with its individual scope and licence. The recipient can audit.
- Refuses to package secrets (`.env`, `credentials.json`, `*.pem`), operator-only artefacts (`_audit/`, `_planning/`, `_ingest_*`), or references missing a `**Scope:**` line. These are build-state bugs, not user choices.

Scope cannot make an unlawful use lawful. It can make accidental misalignment *less likely*. A profile with `max_scope: open-nc` is unlikely to ship `confidential` client material because the filter excludes it at build time; a `personal` reference is excluded by construction. A tarball labelled `personal` carries the constraint in its filename, but a recipient can rename it, ignore it, or redistribute it anyway. The label is advisory, not enforceable.

The full scope taxonomy is at [`../reference/scope-taxonomy.md`](../reference/scope-taxonomy.md); the build's filter and the packager's labelling are described there.

## Lens visibility

Lens visibility is the lens-side parallel to reference Scope. It is a separate filtering system on a separate artefact type: Scope filters references; visibility filters lenses. Neither extends to the other.

Each lens spec carries `visibility:` in its YAML frontmatter. Each build profile declares `max_visibility:` in `builds.yaml`. The five levels are the Scope taxonomy borrowed verbatim:

| Rank | Visibility | What goes here |
|---|---|---|
| 0 | `open` | Lenses safe for any audience, including corpus.commons-tracked apps |
| 1 | `open-nc` | Open with non-commercial redistribution intent |
| 2 | `copyrighted` | Lens drawing on all-rights-reserved third-party material the operator can use but not freely redistribute |
| 3 | `confidential` | Lens carrying client-engagement detail, identities, or material under explicit confidentiality |
| 4 | `personal` | Operator's own private working notes; excluded from every profile by construction |

Build-time enforcement has three parts:

1. **Spec-location gate (hard).** The build walks every lens under `corpus.commons/`. Any lens with `visibility:` of `copyrighted`, `confidential`, or `personal` fails the build: "Lens {path} has visibility={X}; lenses above `open-nc` cannot live under corpus.commons/. Move to corpus.local/." The two lower tiers (`open`, `open-nc`) are unrestricted in spec location.

2. **App-shipping filter.** For each profile, the build copies only lenses where `visibility <= max_visibility`. Excluded lenses do not appear in the app's `lenses/` directory.

3. **LENS-INDEX regeneration.** The per-app `LENS-INDEX.md` is generated from the filtered lens list, not copied verbatim from the hand-authored source. Excluded lenses simply don't appear. The hand-authored source `LENS-INDEX.md` in `lenses/` remains the seed catalogue; it lists every lens regardless of visibility and is not used at runtime by apps.

The authorship side of the gate lives in the `creating-lenses` skill at [`.claude/skills/creating-lenses/SKILL.md`](../../.claude/skills/creating-lenses/SKILL.md): the skill prompts the operator for a visibility level early in the authorship dialogue and warns before writing a high-visibility lens to `corpus.commons/`. The vocabulary entry is in [`../reference/vocabulary.md`](../reference/vocabulary.md#lens-visibility).

**No silent default.** Every lens must carry an explicit `visibility:` declaration. Missing the field is a build failure, not a default-to-open. Silent defaults are how the accidental-shipping pattern occurs; requiring explicit declaration is the corrective.

## What the tool does not do

The build does not detect verbatim material at the byte level. It does not arbitrate fair use. It does not validate that the operator's stated licence matches the source's actual licence: the deep ref's frontmatter says what the operator typed, not what the source legally is. The packager refuses obviously-wrong shipments (missing scope, secrets, operator-only artefacts) but cannot catch a scope value that's stated correctly but applied to the wrong source.

The mechanical layer reduces the chance that a misaligned shipment happens by accident. It does not remove the operator's responsibility to review what's going out the door. Treat the build's output and the packager's manifest as the *first* check; the operator's own scan before sharing is the *load-bearing* one. The legal stance above remains the operator's regardless.

## What the operator inherits

The legal and mechanical layers above cover what the operator redistributes. They do not cover what the operator depends on. Three named dependencies travel with every artefact this repo produces, and naming them honestly is the prerequisite for any serious copyright stance.

- **Foundation-model dependency.** The 9-pass protocol, the distillation pipeline, and the runtime retrieval all run on top of a foundation model. The model's training corpus, terms of service, and inference economics travel into every artefact. Operators who care about source provenance should also care about the model's. The architecture does not solve this dependency; it names it.
- **Ingestion-time labour.** The 9-pass protocol moves cost from query time to ingestion time. That cost lands somewhere: typically as operator-curator hours under the human-in-the-loop discipline, and as compute spent on LLM API calls during each pass. [`projection-time.md`](projection-time.md) carries the cost-curve argument; the labour profile of the ingestion side belongs here too, because what is being externalised is also what is being paid for.
- **Source-selection accountability.** The mechanical scope filter excludes by ceiling; the curation decision sits upstream of the filter and is the operator's alone. Crawford's *Atlas of AI* (Yale University Press, 2021) names this as the structural pattern: AI systems externalise classification costs onto the people who curate the source material, then mask the choice in the system's outputs. The matrix architecture surfaces the operator's choice (the corpus is named, the source-cards are inspectable, the audit log is inspectable), but the choice itself remains the operator's. There is no neutral curation.
