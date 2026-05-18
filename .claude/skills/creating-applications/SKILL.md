---
name: creating-applications
description: The single entry point for creating a new application: a compiled distribution built from a corpus subset projected onto a task axis (with optional lenses + practitioner-role agents). Run this when a user says "create an app for X" or similar. The skill first ensures a task spec exists (calling `creating-tasks` internally if one does not, so the user sees a continuous experience rather than a bounce), then scaffolds the distillation directory, distillation index, build profile, CLAUDE.md template, and agent files, then orchestrates per-distillation distillation by calling `creating-distillations` for each applicable source.
argument-hint: "[application-name or task-slug]"
---

# Creating Applications

An *application* is a compiled distribution: a corpus subset projected onto a task axis (optionally through a lens-set and a practitioner-role agent-set), bundled with a CLAUDE.md template and packaged at `corpus.commons/{corpus}/apps/{profile}/`. This skill scopes and assembles one application end-to-end.

The skill is the single user-facing entry point for creating an application. Internally it delegates to two sub-skills:

1. **Task-axis scoping.** If no task spec exists at `corpus.commons/{corpus}/tasks/{task-slug}.md`, invoke the `creating-tasks` flow inline. The dialogue happens in this skill's conversation; the task spec drops at the right path; the skill continues onward without re-prompting the user. If a task spec already exists, skip.
2. **Per-distillation projection.** For each source named in the task spec, call `creating-distillations` once. Pass G's applicability gate decides which distillations fire. Often dispatched as parallel sub-agents.

Between those two delegations, the skill does its own scaffolding work: distillation directory, distillation index (seeded from the task spec's practitioner questions and runtime listener grain), build profile in `builds.yaml`, `package.json` build script, `build-profiles/{profile}.md` CLAUDE.md template, and one agent file per agent declared in the task spec.

## When to use

- A user wants a new application: a new compiled distribution shipping a slice of the corpus for a specific job. Phrasing varies: *"create an AAR facilitator app"*, *"build me a coaching tool from this corpus"*, *"I want a distribution for incident review"*. Route all such asks here.
- A corpus reshape: the operator wants a new build profile that ships a different slice of the corpus to a different audience for a different task.
- After ingesting new sources that warrant their own application rather than just extending existing axes: e.g. a corpus of AAR-specific sources where the operator wants the AAR-shaped distribution as a first-class profile.

## When not to use

- You want to add a single source to an existing application's distillation column. Run `creating-distillations` directly.
- The question is "is there an existing application that covers X?" Read `builds.yaml` and the per-task distillation indexes.
- The change is a small renaming or path-substitute across an existing application. That's manual editing, not a new application.

## Pre-flight

The skill expects a task-axis spec at `corpus.commons/{corpus}/tasks/{task-slug}.md`. If the spec does not exist, the skill invokes `creating-tasks` inline (Step 0 below).

The task spec carries (per the `creating-tasks` contract):

1. **Problem statement.** What specific work the application is meant to support. One paragraph. Concrete, not aspirational.
2. **Practitioner questions.** 5-10 concrete questions a practitioner asks in the field. Seed for the per-phase diagnostic tables in the distillation index.
2a. **Runtime listener grain.** Trigger unit, response unit, and a seed trigger→response table with at least five rows per phase. **Required, not optional.** `creating-applications` reads it to author the distillation index's runtime tables; `creating-distillations` reads it at Pass G to map each source's content to the triggers it can address. Without it the application is a catalogue, not a coach.
3. **Available sources.** Which existing references in the corpus, by slug, are likely to apply. The source-set the orchestrator iterates Pass G over.
4. **Intended lenses.** Which lenses from `corpus.commons/{corpus}/lenses/` will reach for this task. Per-distillation applicability decided downstream at Pass G.
4a. **Intended runtime agents.** List of agent slugs and role descriptions. Zero-or-more agents per axis. This skill authors one file per declared agent at `.claude/agents/{agent-slug}.md` in Step 4a.
5. **Overlap with existing task axes.** Where the new axis overlaps with existing axes. Flags sources whose existing distillations may need integration-section updates.
6. **Success criteria.** How the operator would know in 3-6 months whether the application was worth the work.

If any required field is missing, the skill fails with a specific message rather than degrading silently. The operator returns to `creating-tasks` to fill the gap, then re-invokes this skill.

## Procedure

Step 0 ensures a task spec exists; Steps 1-4 scaffold the application; Step 4a authors any declared agents; Step 5 orchestrates per-distillation distillation.

### Step 0: Ensure a task spec exists

When invoked, the skill identifies the *intended task slug*. Sources of the slug, in order of preference:

1. **Operator-supplied argument.** If the operator invoked the skill with a slug (`/creating-applications learning-from-incidents` or *"create an app for learning-from-incidents"*), use it directly.
2. **Inferred from the user's natural ask.** If the operator said *"create an AAR facilitator app"* or *"build me a coaching tool"*, infer a candidate slug (e.g. `learning-from-incidents` for AAR work; `coaching-engagements` for coaching). State the inference back to the operator and ask them to confirm or rename before continuing.
3. **Operator-stated outright.** If the operator hasn't named a slug, ask: *"what work is this application meant to support?"* and shape the answer into a candidate slug.

Once the slug is provisional, check whether `corpus.commons/{corpus}/tasks/{task-slug}.md` exists.

**If the spec exists:** read it. Verify the six required fields. If any are missing, surface the gap and ask whether to update via `creating-tasks` (re-running the relevant phases) or proceed as-is. Default: update; the missing fields are usually load-bearing.

**If the spec does not exist:** invoke the `creating-tasks` skill at `.claude/skills/creating-tasks/SKILL.md` inline. The 9-phase JTBD dialogue runs in this conversation as part of *this* skill's flow.

When `creating-tasks` returns with a verdict:
- **GO:** the spec landed. Proceed to Step 1.
- **YELLOW:** the spec landed with caveats (thin corpus, fired-frame-without-example, etc.). Surface the caveats and ask whether to proceed or pause. Default: proceed; YELLOW is shippable.
- **NO-GO:** no spec was authored. Stop. Tell the operator the next move (often `finding-resources` to ingest more material, or wait until practitioner work is clearer).

### Step 1: Read the task spec

Read `corpus.commons/{corpus}/tasks/{task-slug}.md`. Confirm all six required fields are present. If any are missing, abort with the operator-facing message naming the missing fields.

Record the task spec in working memory:
- Task slug (e.g. `learning-from-incidents`)
- Task display name (e.g. *Learning from Incidents*)
- Profile slug (typically derived from the task slug, e.g. `learning-from-incidents`; operator may override)
- Source slugs to iterate (from spec field 3)
- Lens slugs to evaluate (from spec field 4)
- Overlap notes (from spec field 5)

### Step 2: Create the distillation directory and index

Create `corpus.commons/{corpus}/distillations/{task-slug}/` if it does not already exist.

Author `corpus.commons/{corpus}/distillations/{task-slug}/{TASK-UPPERCASE}-DISTILLATION-INDEX.md` (the operator-inspection view; the runtime reads `task-index.json` generated by `scripts/build_indexes/build_task_index.py`). Use the existing distillation indexes as the structural model: see [`corpus.commons/demo/distillations/decision-making/DECISION-MAKING-DISTILLATION-INDEX.md`](../../../corpus.commons/demo/distillations/decision-making/DECISION-MAKING-DISTILLATION-INDEX.md) and [`corpus.commons/demo/distillations/stakeholder-engagement/STAKEHOLDER-ENGAGEMENT-DISTILLATION-INDEX.md`](../../../corpus.commons/demo/distillations/stakeholder-engagement/STAKEHOLDER-ENGAGEMENT-DISTILLATION-INDEX.md) for reference.

Seed the index with:

- **Header.** Title, purpose, last-updated date (today).
- **Format section.** Standard text: what the index does, how to read it.
- **Quick start by {task} type.** Seeded with empty rows; populated row-by-row as Step 5 fires Pass G on each source.
- **Phase-by-phase guide.** One section per phase, derived from the task spec's practitioner questions (field 2). The questions become phase headers if they group naturally into phases; otherwise the operator names the phases. Each phase has an empty *Phase routing table* to be populated by Pass G.
- **Runtime listener tables (per phase).** Inherit the seed trigger→response table from the task spec's field 2a, one table per phase, with at least the rows the spec carries plus space for Pass G extensions. Structure: per-phase markdown table, two columns: *recognisable-in-real-time trigger* on the left, *framework + teach-in-the-moment script* on the right. When a query carries observable signals, the assistant routes from the listener table to the distillation rather than from the phase-routing table.
- **Reference categories.** Empty section; populated row-by-row as distillations land.
- **Anti-patterns this index helps avoid.** Empty section; populated based on the patterns the orchestrator surfaces during Step 5.

The index is created with the structure in place but minimal content. Step 5's per-distillation projections populate the rows.

**Two routing layers, not one.** Phase-routing is the *macro-router* (query mentions a phase or situation type → candidate distillations). Runtime listener table is the *micro-router* (query mentions an observable trigger → framework that fires in the moment). Both ship; the assistant uses the listener table first when a query carries observable signals, the phase-routing table when the query is at the situation-type level.

### Step 3: Create the build-profile CLAUDE.md template

Author `{corpus-root}/build-profiles/{profile-slug}.md`. Use existing profile templates as the structural model: see [`corpus.commons/demo/build-profiles/decision.md`](../../../corpus.commons/demo/build-profiles/decision.md) and [`corpus.commons/demo/build-profiles/stakeholder.md`](../../../corpus.commons/demo/build-profiles/stakeholder.md) for reference.

The template carries:

- The application's purpose: who is the audience, what task does it support, what is its scope.
- A "retrieval order" section telling the runtime assistant how to read the application's content (index first, then distillation, then deep ref: the canonical order from the matrix architecture).
- A "what the application ships" section listing the references and distillations it carries.
- A "what the application does NOT ship" section naming the scope boundaries (what task axes are *not* in this dist; what audience this is *not* for).
- A pointer to the application-specific lens set (if any) and how lens-aware queries are handled.
- A `## Capability binding` section: see Step 3a.

Adapt the template to the application's specifics. Do not copy-paste decision.md without reshaping: the template's structure is reusable, its content is not.

### Step 3a: Scaffold the capability-binding section

Per [`docs/architecture/capability-binding.md`](../../../docs/architecture/capability-binding.md), every application declares the abstract capabilities it benefits from at the profile boundary: never inside a substrate skill, rarely inside a corpus-bound skill. This skill is substrate; it MUST NOT *declare* capabilities itself. It MUST *scaffold* capability declarations into the artefacts it produces (the `builds.yaml` entry in Step 4 and the CLAUDE.md template in this step). The distinction is load-bearing: the substrate stays capability-blind, the apps it generates carry capability-awareness at the right layer.

Ask the operator (one prompt, batched): *"Does this application ride on user-owned work tools, chat (Slack / Teams), issue trackers (Shortcut / Linear / Jira), notes archives (Obsidian / Confluence / Notion / Drive), calendar, delivery metrics, or anything similar? For each: what does the app do when it's bound, and what's the graceful fallback when it isn't?"*

The operator's answer falls into one of three shapes:

- **None.** Some applications are pure library lookup with text output (most demo profiles). Scaffold a minimal generic capability anyway (usually `notes-archive` with a "paste markdown manually" fallback) so the conformance pattern is visible to the runtime. Every app shows the pattern; the field's presence is itself the conformance signal.
- **One or more abstract names.** Capability names are deliberately abstract: `chat-export`, `issue-tracker`, `notes-archive`, `calendar`, `delivery-metrics` are the names already in use across the repo's profiles. Avoid naming a concrete server (`slack`, `shortcut`, `obsidian`): those belong in the user's `~/.claude/capabilities.toml`, not in the profile. If the operator names a capability that doesn't fit any existing name, accept the new name ad-hoc (vocabulary governance is open question §5 in the spec).
- **An integration-heavy skill exists**, e.g. the app ships a `/foo-start [id]` skill that structurally cannot run without a binding. Surface this in the prompt and route the operator to Step 4b (skill-level declaration) after this step. Most apps will have zero or one such skill; the bar is *structural impossibility*, not *would be nice to have*.

Write the `## Capability binding` section into the CLAUDE.md template using the worked example in `docs/architecture/capability-binding.md` §4 as the structural model. The section names each abstract capability, the bound behaviour, and the unbound (fallback) behaviour. The unbound path is the conformance test: every framework citation, every distillation read, every routing decision still works when nothing is bound.

### Step 4: Register the build profile

Append a new entry to [`builds.yaml`](../../../builds.yaml) following the existing entries' shape. The entry carries:

- `name`: `{profile-slug}`.
- `description`: one paragraph explaining the application's purpose, target audience, and corpus scope. Visible in build output.
- `source_dir`: the corpus root (typically `corpus.commons/{corpus}`).
- `output_dir`: `corpus.commons/{corpus}/apps/{profile-slug}`.
- `claude_md`: `build-profiles/{profile-slug}.md` (created in Step 3).
- `distillations`: which distillation directories to include. The new task-slug must be in the list. Optionally include sibling axes if the application is meant to be multi-axis (rare; most applications are single-task).
- `lenses`: `true` if the application ships the lens set, `false` if not.
- `agents`: `include: [list of agent slugs]` per the task spec's field 4a. Empty list (`[]`) if the task spec declares no runtime agents.
- `recommends_capabilities`: one or more `{name, purpose, fallback}` entries per the operator's Step 3a answers. Always present; even apps with no MCP integration carry a minimal generic entry so the conformance pattern is visible. Capabilities are abstract names; the user's `~/.claude/capabilities.toml` binds concretes. See [`docs/architecture/capability-binding.md`](../../../docs/architecture/capability-binding.md) §4 for the shape.
- `ignore_dangling`: the standard list of paths the validation should not chase. Copy from a sibling profile and adjust.

Append a new build script to [`package.json`](../../../package.json) following the existing scripts' shape:

```json
"build:{profile-slug}": "node build.js {profile-slug}"
```

Run `npm run build:{profile-slug}` to verify the profile scaffolds cleanly. The build will run against an empty (or stub) distillation directory at this point: that's expected. The validation should pass on structure and referential integrity. If it fails, fix the scaffolding before proceeding to Step 4a (if agents declared) or Step 5.

### Step 4a: Author runtime agent definitions (if declared in task spec field 4a)

If the task spec carries field 4a with one or more agent slugs, author one file per declared agent at `.claude/agents/{agent-slug}.md`. Each agent file has YAML frontmatter (name, description, tools, model, color) plus a markdown system prompt. The shape follows Claude Code's custom-agent conventions. The demo profiles ship no runtime agents; the `.claude/agents/` directory is empty in the shipped demo. When a downstream application defines its first agent, the resulting file becomes the local precedent for the shape.

**Skill-placement rule for any practitioner-role skills authored alongside this application.** Skills that cite this application's references or task axis are *corpus-bound* and belong at `{corpus-root}/.claude/skills/{skill-slug}/SKILL.md`: they travel with the corpus. Skills that are corpus-agnostic patterns (e.g. a new variant of `matching-references` or `audit-attribution`) are *substrate* and belong at the repo-root `.claude/skills/{skill-slug}/SKILL.md`. The build resolver checks the corpus first, then substrate; either location ships into the compiled app's flat `.claude/skills/`. If the operator authors a new corpus-bound skill, also enumerate it in this profile's `skills:` list in `builds.yaml`. See the substrate-vs-corpus-bound section of the repo-root CLAUDE.md for the discovery model.

Each authored agent carries:

- **YAML frontmatter:** `name` (matches slug), `description` (when to invoke this agent), `tools` (constrained palette: typically `Read, Grep, Glob, Edit, Write, Skill` for runtime agents; runtime agents rarely need WebFetch / WebSearch / Bash), `model` (default `sonnet`; `opus` only when the role's reasoning grain genuinely needs it), `color` (visual marker).
- **Operating frame:** the discipline the agent holds (blameless framing for AAR, generative facilitation for retro, etc.), grounded in cited corpus sources.
- **Retrieval order:** the runtime-listener-table-first pattern (see `matching-references` SKILL.md), with the specific listener tables for this task axis named.
- **Pacing rule:** interactive (one-phase-at-a-time, pause-and-wait) vs generative (produce-the-artefact). Most runtime facilitator agents are interactive; most analyser agents are generative.
- **Refusal list:** what the agent refuses by default (single-cause narratives, person-shaped corrective actions, counterfactuals, etc., grounded in the corpus's discipline).
- **Trigger-grain integration:** explicit instruction to read the per-phase listener tables first when the query carries observable triggers.
- **Output format:** what artefact the agent produces and where it saves it.

If the agent file already exists (operator hand-authored it earlier), read it and validate against the task spec's role description for that agent rather than overwriting. Surface discrepancies for the operator to reconcile.

Update `builds.yaml`'s `agents.include` list for this profile to include all declared agent slugs. Re-run `npm run build:{profile-slug}` to confirm the agents copy into `apps/{profile}/.claude/agents/` cleanly.

### Step 4b: Declare integration-heavy corpus-bound skills (if any)

If Step 3a identified one or more corpus-bound skills that are *structurally impossible* without a binding (the classic case: `/foo-start [id]` cannot synthesise an id it cannot fetch), declare them per [`docs/architecture/capability-binding.md`](../../../docs/architecture/capability-binding.md) §3. For each integration-heavy skill, append to its frontmatter:

```yaml
requires_capabilities: [{capability-name}]
fallback_for_capabilities: [{capability-name}]
```

Then add a `## Capability binding` paragraph below the frontmatter naming the bound behaviour, the unbound fallback (either *fail closed* with a clear binding instruction or a precisely-bounded *degraded path*), and the discipline of never fabricating data the binding would have produced.

**The bar is structural impossibility, not convenience.** Most corpus-bound skills are *framework-application*: they read the corpus and apply distillations, with optional MCP enrichment when present. Those skills MUST NOT declare capabilities (they SHOULD NOT clutter their frontmatter with bindings they only opportunistically use). The repo's worked examples are: `aar-start`, `aar-new`, `obs-coach`, `obs-health`, `obs-report` carry frontmatter declarations; `aar-actions`, `aar-deep`, `retro-*`, `aletheia-session`, `coaching-feedback`, `mentoring-feedback`, `meeting-review` do not. Most new applications will produce zero integration-heavy skills.

### Step 5: Orchestrate per-distillation distillation

For each source slug in the task spec's field 3, invoke `creating-distillations` with the (source, task) pair. Pass G's source-applicability gate inside `creating-distillations` decides whether the source applies; if it does, the distillation is produced and the index is updated. If it doesn't, the skip is logged with the reason.

Two ways to invoke:

- **Sequential.** Run `creating-distillations` once per (source, task) distillation. Slower; appropriate for small source sets (≤ 5 sources) or when the operator wants to review each distillation.
- **Parallel (sub-agents).** Dispatch each (source, task) distillation as a sub-agent. Faster for larger source sets. The parallel-batch pattern in `ingesting-resources/SKILL.md` is the model.

**Concurrency hazard.** Multiple sub-agents updating the same distillation index file race. Mitigation: each sub-agent writes its index entries to a staging file (`_ingest_{task}_{source-slug}.md` in the distillations directory); a final consolidator step merges all staging files into the canonical index.

Lens applicability is handled inside `creating-distillations` at Pass G: this skill passes the lens-set through and does nothing extra.

After all per-distillation invocations complete:

1. **Consolidate staging files** (if parallel-batch was used) into the canonical distillation index. Remove the staging files.
2. **Review the populated index for coverage.** Does each phase have plausible coverage? Are categorisations consistent? Are there phases left empty that the corpus should address? The build's referential-integrity check confirms paths resolve; it does not check whether the index makes sense as a router.
3. **Run `npm run build`** to verify the new profile (and any sibling profiles) compile cleanly.

## Run summary

Output a list at the end recording:

- **Source × task applicability decisions.** Per source: applied / skipped / operator-confirmed, with the reason.
- **Per-lens applicability decisions** (per source × task × lens distillation): no pre-projection / partial reshape / deep reshape / operator-confirmed.
- **File paths produced.** Every distillation file, every index update, every staging file consolidated.
- **Validation status.** Build result for the new profile and any sibling profiles affected.

## Cycling: scaffolding sometimes reshapes the task spec

The orchestrator step sometimes reveals the task spec was wrong:

- **Source set too narrow.** Pass G fires on fewer distillations than expected; index has empty phases. Ingest more via `ingesting-resources` and re-orchestrate, or accept thin coverage and document it.
- **Source set too broad.** Index has too many rows per phase; routing collapses. Tighten spec field 3 or revisit the task definition.
- **Phase decomposition wrong.** Practitioner questions don't decompose into phases the source set lands on. Re-shape the phases or use a different organising structure (e.g. *types of question* rather than *phases of work*).
- **Lens set misaligned.** Lens-applicability gate fires very rarely or very often. Both are signals: rare = over-specified; pervasive = lens may be doing the work the task axis should be doing.

When the orchestrator reveals a spec problem, update the spec and re-run. Do not paper over the gap by editing the distillation index by hand.

## Re-runs and overwrites

The skill does not silently overwrite an existing application. Two paths:

- **Refresh after a task-spec update.** Delete or rename the existing distillation directory, build profile, and CLAUDE.md template; rerun the skill.
- **Augment without rebuild.** Operator added new sources to the corpus and wants them projected onto the existing task axis. Skip Steps 1-4; run only Step 5 against the new sources. Equivalent to invoking `creating-distillations` directly for each new source.

## Failure modes to watch

- **Skipping the scoping step.** Running without a task spec is a quiet failure: the orchestrator runs but the distillation index has no organising structure beyond what Claude improvises. The pre-flight is the gate.
- **Generic application templates.** The CLAUDE.md template should be specific to the application's audience and task. Copy-paste-with-rename produces filler.
- **Orphan phase headers.** If Pass G doesn't fire on any source for a given phase, the phase header stays orphan. Populate via additional source ingest, or remove the phase: orphans degrade the router.
- **Skipping the build verification.** Step 4's and Step 5's `npm run build` are not optional. The validation catches dangling references and structural problems.
- **Conflating scoping and orchestration.** If producing scoping decisions during Step 5, the pre-flight failed: return to `creating-tasks` rather than improvising scoping here.
- **Naming a concrete server in the profile.** *"Pulls from Slack and Shortcut"* in the CLAUDE.md template or `requires: slack` in `builds.yaml` is a conformance failure ([`capability-binding.md`](../../../docs/architecture/capability-binding.md)). Profile declares the abstract capability (`chat-export`, `issue-tracker`); the user's `~/.claude/capabilities.toml` binds the concrete. The scaffolded text should not name a server.
- **Substrate skill carrying capability declarations.** This skill is substrate. It scaffolds capability declarations into the app it produces; it does not declare any itself in `.claude/skills/creating-applications/SKILL.md`. If a future maintainer reaches for `requires_capabilities:` here, the bright line is broken.

## Related skills

- `creating-tasks`: scopes a new task axis. Upstream; produces the task spec this skill consumes.
- `creating-distillations`: per-distillation projection. Downstream; this skill invokes it once per applicable distillation.
- `creating-lenses`: designs a lens spec. Run before this skill when the task spec names lenses that don't yet exist.
- `ingesting-resources`: ingests a new source. Use when the orchestrator reveals thin source coverage.
- `creating-corpus`: scaffolds a new corpus directory tree. The corpus must exist before this skill can compile into it.
