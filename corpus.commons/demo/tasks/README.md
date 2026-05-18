# Task specs

Task specs land here, one per task axis. The substrate `creating-tasks` skill authors them.

A task spec is the Jobs-to-be-Done definition of one column in the reference × task matrix: the verb-and-noun job, the practitioner questions, the source set, the lens set, the success criteria. It is the operator-authored truth that the build profile, the distillation directory, and the practitioner-role agents are all derived from.

## Current demo state

The demo ships five live task axes:

- `decision-making` (26 distillations)
- `stakeholder-engagement` (26 distillations)
- `software-business` (23 distillations; 3 Pass G skips routed cross-axis; spec at `software-business.md`)
- `aar` (18 distillations; spec at `aar.md`)
- `retro` (18 distillations; spec at `retro.md`)

The runtime artefacts each axis drives (`distillations/{axis}/task-index.json` and the operator-inspection `{TASK}-DISTILLATION-INDEX.md`) are present and current.

The `decision-making` and `stakeholder-engagement` axes were scoped before the `creating-tasks` skill was formalised; their canonical specs are still to be written for v0.2.2.

## Path resolution

This directory is referenced by the substrate `docs/architecture/matrix-pattern.md` and the `creating-tasks` and `creating-applications` skills as the canonical write-location for task specs.
