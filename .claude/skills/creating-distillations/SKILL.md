---
name: creating-distillations
description: Projects one existing verified reference onto one existing task axis, gated by a per-distillation applicability check. Produces one distillation file at `corpus.commons/{corpus}/distillations/{task}/{slug}-{task}.md`, optionally with lens-applied sections or per-lens variants. Invoked by `ingesting-resources` Pass G during new-source ingestion and by `creating-applications` during per-distillation orchestration when assembling a new application.
argument-hint: "[task-name] [reference-slug]"
---

# Creating Distillations

Per-distillation projection of one source onto one task axis. Consumes a (source, task) pair plus an optional lens-set; produces one file plus an index update.

Invoked by:
- `creating-applications`, per-distillation orchestration: once per applicable (source, task) distillation.
- `ingesting-resources` Pass G: once per task axis during a new-source ingest.

Rationale, template structure, evidence discipline, four-outcome lens-applicability gate, and failure modes live in [`projection-protocol.md`](projection-protocol.md). This file is the runbook; that one is the rationale. Read both before invoking.

## When to use

- **Pass G of `ingesting-resources`.** Per task axis in the corpus, the ingest skill calls this skill once with the new (source, task) pair. The applicability gate decides whether to produce a distillation or skip.
- **Per-distillation orchestration in `creating-applications`.** When a new application is being assembled, the orchestrator calls this skill once per (source, task) distillation named in the task spec. Often dispatched as parallel sub-agents.
- **Operator follow-up.** A new task axis has landed and the operator notices a source whose existing deep reference predates the axis: invoke this skill directly to project that source onto the new task.
- **Re-projection after a deep-ref update.** The deep reference has been sharpened (often via Pass G cycling: see [`projection-protocol.md`](projection-protocol.md) §Cycling); the distillation needs to reflect the updated deep.

## When not to use

- The deep reference does not yet exist. Run `ingesting-resources` first.
- The task axis does not yet exist (no distillation directory, no index, no build profile). Run `creating-tasks` → `creating-applications` first.
- The operator wants to project *all* applicable sources onto a new axis. That's the per-distillation orchestration job inside `creating-applications`: invoke it instead, and it will call this skill once per source.

## Pre-flight

Both checks must pass:

1. **Verified deep reference exists.** Path: `corpus.commons/{corpus}/references/{slug}-deep.md`. The deep must have passed Pass I (source-only audit). If the deep does not exist, abort with the operator-facing message *"Deep reference for {slug} not found; run `ingesting-resources` first."*
2. **Task axis exists.** Path: `corpus.commons/{corpus}/distillations/{task-name}/`. The directory plus `task-index.json` (and the human-readable `{TASK-UPPERCASE}-DISTILLATION-INDEX.md` operator-inspection view) must exist. If any are missing, abort with *"Task axis {task-name} not yet scaffolded; run `creating-applications` first."*

If both pre-flight checks pass, the skill proceeds. Otherwise it fails loudly and names the gate that closed.

## Inputs

- The existing task axis name in kebab-case (e.g., `decision-making`, `learning-from-incidents`).
- The slug of the existing verified reference (e.g., `openstax-organizational-behavior`).
- Optionally, one or more lens names. Lens names refer to specs at `corpus.commons/{corpus}/lenses/{lens-slug}.md`. If a named lens has no spec file, abort and direct the operator to run `creating-lenses` first.

## Outputs

- **The distillation file** at `corpus.commons/{corpus}/distillations/{task-name}/{slug}-{task-name}.md`, produced when Pass G.0's source-applicability gate fires *clear yes* or *operator-confirmed yes*. **The distillation includes a `## Runtime triggers this source addresses` section** that maps the source's content to specific triggers from the task spec's seed table (field 2a), with teach-in-the-moment scripts. See "Trigger-grain projection" below.
- **An update to the distillation index** for the task, citing the new distillation in the appropriate phase sections **and adding rows to the per-phase runtime listener tables** for each trigger the source addresses.
- **For each lens** where the per-distillation applicability gate fires beyond *clear no*:
  - **Partial reshape:** a `## Through the {lens-name} lens` section inside the main distillation.
  - **Deep reshape:** a separate per-lens distillation at `corpus.commons/{corpus}/distillations/{task-name}/{slug}-{task-name}-{lens-name}.md`.
- **A skip log** when Pass G.0 fires *clear no* or *operator-confirmed no*. No file is generated; the skip is recorded with the reason. Lens skips at *clear no* are recorded similarly.

If the skill is invoked under parallel-batch orchestration, index updates may be written to a staging file (`_ingest_{task}_{slug}.md` in the distillation directory) instead of the canonical index, to be merged by the orchestrator's consolidator step.

## Procedure

The detailed step-by-step procedure—applicability gate logic, projection-template structure, evidence discipline, lens-as-optional-framing—lives in [`projection-protocol.md`](projection-protocol.md). The runbook summary:

1. **Read the verified deep reference.** The deep is the only input at this step; the source is not re-read. (See `projection-protocol.md` §Failure modes for why.)
2. **Run the source-applicability gate** (`projection-protocol.md` §Pass G.0). Three outcomes: clear yes → proceed; clear no → log skip and exit; ambiguous → ask the operator and proceed per their call.
3. **Project the source onto the task** using the standard nine-section template (`projection-protocol.md` §Projection template). The structure is uniform across the corpus; do not deviate, add sections, or reorder.
4. **For each named lens, run the lens-applicability gate** (`projection-protocol.md` §Lens-as-optional-framing). Four outcomes:
   - **Clear no.** No additional artefact. Log the skip.
   - **Clear yes, partial reshape.** Add a `## Through the {lens-name} lens` section inside the distillation.
   - **Clear yes, deep reshape.** Produce a separate per-lens distillation file.
   - **Ambiguous.** Ask the operator; proceed per their call.
5. **Trigger-grain projection.** Read the task spec's field 2a (seed trigger→response table) and identify which triggers this source can address. For each:
   - Add a row to the distillation's `## Runtime triggers this source addresses` section: trigger | source's content that addresses it | teach-in-the-moment script (1-3 sentences).
   - Add a row to the distillation index's runtime listener table for the appropriate phase: trigger | framework name + cite to this distillation.
   - The source may extend the seed table (surface triggers the spec didn't anticipate but the source clearly addresses); log these extensions in a `## Trigger extensions surfaced by this source` section so the operator can fold them back into the task spec.
   - If the source addresses zero triggers in the seed table, that is a signal Pass G.0 should reconsider: the source may apply at the *phase* level but not at the *moment* level, which means the distillation will be shelf material at runtime even if the phase-routing fires it. Default: still produce the distillation but flag the trigger-mismatch in the distillation header so the operator can address it.
6. **Update the distillation index** to cite the new file(s) in the phase sections where they apply *and* add trigger-table rows for the triggers the source addresses. If running under parallel-batch orchestration, write to a staging file instead and let the orchestrator's consolidator merge it.
7. **Run `npm run build`** to verify the affected profile compiles cleanly. Required after every Mode-2 run when invoked standalone; the orchestrator runs a final build after all per-distillation invocations complete when running under `creating-applications`.

## Re-runs and overwrites

If the distillation already exists for the (source, task) pair, the skill does not silently overwrite. Two paths:

- **Refresh after a deep-ref update.** Delete or rename the existing distillation; rerun the skill. The applicability check runs again; the file is regenerated from the current deep.
- **Merge changes.** The skill does not merge. Generate the new version into a temporary path, diff against the existing, and apply the diff manually.

## Failure modes to watch

The full catalogue with worked examples lives in [`projection-protocol.md`](projection-protocol.md) §Failure modes. The headlines:

- **Skipping the source-applicability gate.** Generating a distillation for a (source, task) pair where the source doesn't actually fit produces a file that strains, reaches, and reads as filler. Better to skip and record the skip.
- **Skipping the lens-applicability gate.** Pre-projecting against every named lens by default inflates the corpus with thin lens-shaped variations of the same content. The default for lenses is *do nothing*; pre-project only where the lens materially reweights the distillation.
- **Re-reading the source.** Distillation projection is from the verified deep, not from the source. Re-reading reintroduces failure modes the deep ref has already audited out (training-prior leakage, drift, evidence-marker confusion).
- **Smuggling new claims into distillations.** If a concept is not in the deep reference, it does not belong in the distillation. Re-ingest if the concept warrants inclusion.
- **Re-extracting verbatim from the source at Pass G.** Verbatim blockquotes in distillations are *copies* of already-audited Pass D blockquotes from the deep ref, with the evidence marker preserved. Re-extracting from the source reopens the failure modes Pass D closed.
- **Mismatched task vocabulary.** The distillation's working vocabulary should be the task's own: *decisions* for decision-making, *stakeholders* for stakeholder-engagement, *incidents* for incident-review, etc. Source-author vocabulary is preserved in the deep reference; task-applied vocabulary lives in the distillations.

## Related skills

- `creating-tasks`: scopes a new task axis. Run before this skill if the named task axis does not yet exist.
- `creating-applications`: assembles a new application. Invokes this skill once per (source, task) distillation.
- `ingesting-resources`: runs the 9-pass protocol. Pass G calls this skill once per task axis the corpus carries.
- `creating-lenses`: designs a lens spec. Run before this skill if a named lens doesn't yet exist.
- `matching-references`: find an existing source by topic before assuming a distillation is needed.
