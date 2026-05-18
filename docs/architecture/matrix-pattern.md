# The matrix pattern: reference × task pre-projection

**The matrix moves projection from query time to ingestion time.** Each source × task cell is pre-projected once under a structured 9-pass protocol; runtime selects a cell rather than re-deriving one from raw chunks. This document walks the architectural unit—a single row of the matrix—through a concrete example, then the build that ships profiles as slices of the matrix.

## A concrete example first

Open these three files in turn:

- the [OpenStax *Organizational Behavior* deep reference](../../corpus.commons/demo/references/openstax-organizational-behavior-deep.md): the source on the reference axis
- the [decision-making projection](../../corpus.commons/demo/distillations/decision-making/openstax-organizational-behavior-decision-making.md): the source projected onto decision-making
- the [stakeholder-engagement projection](../../corpus.commons/demo/distillations/stakeholder-engagement/openstax-organizational-behavior-stakeholder-engagement.md): the source projected onto stakeholder-engagement

The deep reference is the source itself. It is task-neutral: the author's argument, with verbatim citations and evidence-classification markers. The reference does not tell you when to reach for it.

The two distillations take the same source and project it onto two different tasks. Where the deep reference covers Ch 6.4's distinction between *process conflict* (disagreement about substance) and *relationship conflict* (disagreement that becomes personal), the stakeholder-engagement distillation lands that concept as a phase-organised diagnostic table:

```markdown
### Phase 4: Surfacing Conflict (When disagreement emerges)

| Need | Question |
|---|---|
| Distinguish process from relationship conflict | Is this disagreement about the substance of the issue (productive) or about the parties (corrosive)? Surface productive process conflict; quell relationship conflict. |
| Apply the Thomas mode | Competing (when speed and authority warrant), collaborating (high-stakes integrative), compromising (time-pressured equal-power), avoiding (trivial or symptoms-not-causes), accommodating (issue matters more to others). |
| ...
```

The decision-making distillation takes the *same underlying concept* and lands it differently, as a "what to look for" pattern: *"Heated debate without a name for the binding constraint. Signal: arguments escalate but stakeholders cannot agree what the dispute is actually about. Diagnosis: relationship conflict has overtaken process conflict; participants have shifted into reactive-system processing. Follow-up: pause; reframe to process conflict explicitly."* Same source, same concept, two projections shaped by the task.

## The matrix as a literal layout

```
                  Decision-making              Stakeholder-engagement       ...
                  ───────────────              ──────────────────────
00h openstax-OB   distillations/decision-      distillations/stakeholder-
                  making/openstax-organi-      engagement/openstax-organi-
                  zational-behavior-decis-     zational-behavior-stakeho-
                  ion-making.md                lder-engagement.md

00o tc-25-20-aar  distillations/decision-      distillations/stakeholder-
                  making/tc-25-20-army-        engagement/tc-25-20-army-
                  aar-decision-making.md       aar-stakeholder-engagem-
                                               ent.md
...
```

Rows are sources, indexed by their slug-ID in [`corpus.commons/demo/references/slug-table.json`](../../corpus.commons/demo/references/slug-table.json) (a 3-character base-36 ID per source, append-only). Columns are task domains. Each distillation is a file at a deterministic path derivable from `(source-slug, task)` alone:

```
corpus.commons/demo/distillations/{task-domain}/{source-slug}-{task-domain}.md
```

That deterministic path is the dispatch mechanism. Given a source-slug and a task, the assistant knows where the projected distillation lives without needing a lookup table. The slug-table resolves IDs (which the runtime indexes carry, for compactness) back to slugs (which the file system carries, for legibility).

## What pre-projection produces

Each distillation is *a source already projected*: relevance to this task, key concepts in the task's vocabulary, diagnostic questions per phase, anti-patterns, integration with sibling sources in the task domain. The projection work, the synthesis from source narrative to task-shaped advice, has already been done at ingestion. Runtime is selection, not synthesis.

This is what the projection-time argument cashes out as: the work of "how does this source apply to this task" is done once, audited under the 9-pass protocol, and never re-derived from raw source.

## What the build does with the matrix

The build system in [`build.js`](../../build.js) compiles slices, one per profile. Five profiles ship under `corpus.commons/demo/apps/`: [`decision`](../../corpus.commons/demo/apps/decision/) carries the *decision-making* column; [`stakeholder`](../../corpus.commons/demo/apps/stakeholder/) carries the *stakeholder-engagement* column; [`software-business`](../../corpus.commons/demo/apps/software-business/) carries the *software-business* column; [`aar-mode`](../../corpus.commons/demo/apps/aar-mode/) carries the *aar* column; [`retro-mode`](../../corpus.commons/demo/apps/retro-mode/) carries the *retro* column. Same references across all five, different task projections shipped per profile.

Each compiled app carries the runtime JSON indexes alongside the markdown content:

```
apps/decision/
├── references/
│   ├── slug-table.json                                    # ID ↔ slug
│   ├── REFERENCE-INDEX.md                                 # operator view
│   ├── openstax-organizational-behavior.md                # light ref
│   └── openstax-organizational-behavior-deep.md           # deep ref
├── reference-index.json                                   # file catalogue (runtime)
├── concept-index.json                                     # concept axis (runtime)
└── distillations/decision-making/
    ├── task-index.json                                    # situation router (runtime)
    ├── DECISION-MAKING-DISTILLATION-INDEX.md              # operator view
    └── openstax-organizational-behavior-decision-making.md
```

The selective compilation is the architectural commitment: a profile is the matrix sliced along the task axis. To verify, after `npm run build`:

```bash
diff -rq corpus.commons/demo/apps/decision/ corpus.commons/demo/apps/stakeholder/
```

The distillation directories differ. Each app's `task-index.json` differs. The build-profile CLAUDE.md differs. The reference files, `reference-index.json`, `concept-index.json`, and `slug-table.json` do not.

## Adding a task axis

Forking this repo for your own domain typically means picking your task domains. For each new task `Z`:

1. Scope the task axis with the `creating-tasks` skill (Jobs-to-be-Done discipline: verb-and-noun job, practitioner questions, source set, lens set, success criteria). The output is a task spec at `corpus.commons/demo/tasks/{task-slug}.md`.
2. Run the `creating-applications` skill (see [`.claude/skills/creating-applications/SKILL.md`](../../.claude/skills/creating-applications/SKILL.md)) with the task spec as input. The skill creates the distillation directory, the distillation index, the build profile in [`builds.yaml`](../../builds.yaml), and the build-profile CLAUDE.md template; then orchestrates per-distillation distillation production by invoking `creating-distillations` once per applicable (source, task) distillation.
3. The `creating-distillations` skill (see [`.claude/skills/creating-distillations/SKILL.md`](../../.claude/skills/creating-distillations/SKILL.md)) reads the verified deep reference and produces one distillation per (source, task) cell where Pass G's applicability gate fires.

The reference axis does not need to change. Only the column is new.

## Adding a source

Adding a new source, by contrast, runs the full 9-pass ingestion protocol ([`ingestion-protocol.md`](ingestion-protocol.md)). The deep reference is produced first. The light reference is derived from the verified deep. Then the distillations for each existing task axis are projected from the verified deep. The new row populates across all existing columns.

## Lenses

A lens is a window with characteristic salience, weighting, and vocabulary: a perspective, audience, or methodology stance. Lenses live alongside the matrix as their own artefacts at [`corpus.commons/demo/lenses/`](../../corpus.commons/demo/lenses/), not as a third axis baked into every distillation. The matrix stays 2D by default (reference × task). Inside the `creating-distillations` skill at Pass G, the per-distillation projection step runs an applicability gate per (reference, task, lens) triple: where the lens materially reweights what's salient for the distillation, pre-project (either as a tagged section inside the distillation or as a separate per-lens distillation); where it doesn't, leave the distillation lens-neutral and let the lens apply as a cheap reweight at retrieval time. Lenses are operator-opt-in per distillation, not a wholesale architectural change.

Lens design is its own step, separate from lens application. The `creating-lenses` skill at [`.claude/skills/creating-lenses/SKILL.md`](../../.claude/skills/creating-lenses/SKILL.md) produces a lens spec and writes it to `corpus.commons/demo/lenses/{lens-slug}.md`. The spec comes in three kinds (personifiable-archetype, named-real-person, non-personifiable-frame), with the same six-section structure across kinds. The spec is the input to Pass G's per-distillation applicability call; it is not a substitute for it. A lens may apply to many distillations, a few, or none; the per-distillation gate decides.
