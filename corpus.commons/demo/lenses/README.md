# corpus.commons/demo/lenses/

Lens specs live here. A lens is the optional per-distillation modifier described in the substrate `docs/reference/vocabulary.md`: a window with characteristic salience, weighting, and vocabulary that shapes how a distillation is read.

The matrix is 2D by default (reference × task). A lens is not an axis; it is a per-distillation modifier applied where the operator declares the lens materially reweights the distillation. The per-distillation call is made at Pass G of the 9-pass protocol; see the `creating-distillations` skill's `projection-protocol.md` §Lens-as-optional-framing for the per-distillation gate.

## What goes here

One file per lens. Three kinds:

- **Personifiable-archetype.** A role-in-circumstance lens. Slug: `{role-or-archetype}-{distinguishing-circumstance}.md`, e.g. `engineering-manager-post-incident.md`.
- **Named-real-person.** A lens grounded in a specific person's published material. Slug: `{first-last}-{role-or-distinguisher}.md`, e.g. `jane-doe-acme-cfo.md`. The slug names the person; the circumstance is in the file.
- **Non-personifiable-frame.** A structural frame applied to situations. Slug: `{frame-name}-lens.md`, e.g. `loss-aversion-lens.md`, `queue-physics-lens.md`.

Every lens file uses the six-section template documented in the substrate `creating-lenses` skill Phase 5.

## How a lens gets here

Run `creating-lenses`. The skill is a single-process dialogue that walks an operator through the six phases and writes the spec.

Lens design is a separate step from lens application. The spec produced here is the input to per-distillation projection at Pass G; it is not a substitute for it. The lens may apply to many distillations, a few, or none.

## Lens index

`LENS-INDEX.md` in this directory is a catalogue of lenses with applicability heuristics, populated as lenses accumulate. See the substrate `docs/reference/vocabulary.md` §Indexes for the index discipline.
