---
name: creating-tasks
description: Scope a new task axis for the matrix: the column-direction in the reference × task projection. The skill is a single-process dialogue grounded in Jobs-to-be-Done discipline; the output is a task spec at `corpus.commons/{corpus}/tasks/{task-slug}.md`, ready to feed `creating-applications` for assembly into a compiled distribution.
argument-hint: "[optional: candidate task name or rough idea]"
---

# Creating Tasks

A *task axis* is the projection direction the corpus is shaped against. References are the row dimension; tasks are the column dimension. The matrix's value is that source material gets pre-projected onto task vocabulary at ingestion time, not re-derived at runtime.

Discipline enforced: *verb-and-noun job-naming under Christensen 2016 Jobs-to-be-Done framing.* *Decision-making* is a task (verb-and-noun job in a circumstance). *Software-business* is a domain (semantic field). A task axis must survive the verb-and-noun rule.

Dialogue skill, one task per session, no subagents. Output feeds `creating-applications` for assembly.

## How this skill is invoked

**Normally a sub-skill of `creating-applications`, not a user-facing entry point.** When a user asks to create an application:

1. User invokes `creating-applications`.
2. `creating-applications`'s task-spec pre-flight checks whether a task spec exists.
3. If no spec exists, `creating-applications` invokes this skill inline: the 9-phase dialogue runs in the user's conversation.
4. When this skill completes (Phase 8 GO/YELLOW), control returns to `creating-applications` for the assembly work.

Standalone invocation is rare: usually when the corpus is being expanded ahead of any specific application.

## When to invoke standalone (rare)

- Scoping a task axis without immediately assembling its application.
- An existing domain label is being treated as a task axis but has no verb attached; sharpen the scoping before committing.
- Two candidate axes that look like one (or vice versa); the boundary needs to be spelled.

## When not to use

- User asking to create an application: invoke `creating-applications` instead.
- Task axis already well-scoped and stable: use `creating-applications`.
- Adding a new *source*: that's `ingesting-resources` or `creating-distillations`.
- Adding a new *lens*: that's `creating-lenses`. Lenses are per-distillation modifiers, not axes.

## Inputs

- Optional: a candidate task name or rough idea ("we should have a `risk-assessment` axis", "I want an `incident-review` axis").
- Optional: a corpus name (defaults to the active corpus from the `creating-corpus` session or working-directory inference).
- Optional: existing task axes or sibling axes the new task might overlap with.

## Output

A task spec at `corpus.commons/{corpus}/tasks/{task-slug}.md`. Slug conventions:

- **Verb-and-noun, kebab-case.** Examples: `decision-making`, `stakeholder-engagement`, `learning-from-incidents`, `facilitating-retrospectives`, `risk-assessment`.
- **Avoid noun-only slugs** for the task slug itself. *"Strategy"* is a noun without a verb; *"strategic-planning"* survives. *"Software-business"* is a domain; *"running-a-software-business"* survives but is broad; usually it decomposes into narrower axes (`pricing-decisions`, `hiring-decisions`, etc.).
- The slug names the axis once and outlasts the operator. Choose carefully.

The spec has six sections. Every spec fills the same six sections; what each section *contains* differs by axis, the *standard* does not.

## Phase 0: Frame the work

Read aloud to the operator:

> A task spec has six fields, all binding. The discipline running through every field is Christensen's Jobs-to-be-Done framing: a task is a job a practitioner does in a circumstance, named with verbs and nouns, with alternatives that cross categories, and with a fire-list naming what older frame the new task displaces. If the task survives the discipline, the spec shapes every projection that runs against this axis.
>
> The axis you author here is not a neutral organising principle. Bowker and Star's *Sorting Things Out* (MIT Press, 1999) names the move: a classification scheme is infrastructure that shapes what becomes visible and what recedes; operators who use it long enough learn to *see* their work through its cuts (Hacking's looping effect). The choice of axes is the operator's most consequential design call. The JTBD discipline below disciplines the choice; it does not make it neutral.

Confirm the operator wants to proceed.

## Phase 1: Verb-and-noun gate

A task axis names a job. A job is a verb-and-noun: *making* a *decision*, *engaging* a *stakeholder*, *facilitating* a *retrospective*, *reviewing* an *incident*, *learning from* an *incident*.

Run all three checks below; each must pass before the axis advances.

**a) Does the candidate slug name a verb-and-noun job?**

- *"Decision-making"*: yes. *Making* (verb) a *decision* (noun).
- *"Stakeholder-engagement"*: yes. *Engaging* (verb) a *stakeholder* (noun).
- *"Software-business"*: no. Two nouns, no verb. **Push back.**
- *"Strategy"*: no. Noun only. **Push back.**

If the candidate fails, ask: *what verb does the practitioner do?* If the operator answers *"think strategically"*, the task is *strategic-thinking* or *strategic-planning*, not *strategy*. If the operator answers *"run a software business"*, the task is too broad to be one axis; it decomposes into many narrower axes that share the corpus.

**b) Is there a recognisable circumstance in which the job happens?**

A task without a circumstance is too broad. *"Decision-making"* survives because every decision happens in a circumstance the operator can name (under uncertainty, under time pressure, with conflict, with limited information). *"Software-business"* fails this even after attaching a verb: *"running a software business"* in *what* circumstance?

The circumstance is *the situation in which a practitioner reaches for this task*. It is the route a query takes to find the axis. Without a circumstance, the axis cannot be routed to.

**c) Does the task differ from sibling tasks already in the corpus?**

If the operator already has `decision-making` and `stakeholder-engagement` and proposes `decision-engagement`, ask where the new task lives that the existing two don't already cover. Tasks should be *non-overlapping enough that a query routes to one*, even when adjacent tasks both apply. Overlap is expected at the edges; collapse means one of the two should be merged or renamed.

If any check fails, the candidate is not yet a task. Revise the slug or revise the framing, and re-enter Phase 1.

## Phase 2: Job × circumstance, the JTBD anchor

Christensen's *Competing Against Luck* (2016) is the anchor. The framework: a customer (the practitioner) *hires* a product (a task-projected distillation) to do a *job* in a *circumstance*, shaped by alternatives.

Four moves to spell the job out:

**a) Name the job in verbs and nouns, with the circumstance attached.**

Not *"support decision-making"*. *"Help a practitioner narrow a non-programmed decision to its binding constraint when more than one alternative looks plausible and the cost of being wrong is high."*

Not *"help with retros"*. *"Help a facilitator design and run a one-hour sprint retrospective that produces 1-2 committed experiments, in a team that has psychological-safety capacity but is short on retro-design experience."*

The circumstance is dense, not generic. Richer constraint produces a more useful task axis. The denseness is what makes the axis routable from a query.

**b) Surface alternatives from different categories.**

What might the practitioner reach for instead? *Do nothing*, *use a sibling task axis*, *ask a colleague*, *use a non-corpus resource*, *defer the decision*. If every alternative is another task axis of the same kind, the job is drawn too narrowly: the task isn't differentiated from its siblings.

If the only alternatives are *"the consultant version of this work"* or *"the AI tool that does this generically"*, ask why this corpus-projected version exists. The answer should name a specific value the matrix-projected work delivers that the alternatives don't.

**c) Hire requires fire.**

What older frame, instinct, or template does adopting this task axis displace? The half people skip.

- *Decision-making* fires the *intuition-only* and *single-stakeholder* reflexes; adopting it commits the operator to surfacing alternatives, weighing them, naming the constraint.
- *Stakeholder-engagement* fires the *announce-and-defend* and *one-size-fits-all-comms* reflexes; adopting it commits the operator to mapping stakeholders, designing for the room, attending to power dynamics.
- *Learning-from-incidents* fires the *find-the-person-to-blame* and *single-cause-narrative* reflexes; adopting it commits the operator to systemic, blameless, multi-cause framing.

If the operator can't name what gets fired, the axis isn't doing the work; it's a label, not a discipline.

**d) Practitioner questions: the seed for phase decomposition.**

List five to ten concrete questions a practitioner of this task actually asks in the field. These become the seed for the per-phase diagnostic tables in the distillation index.

If the operator can't list five, the task axis is not yet ready to be projected; return to Phase 1 later. The minimum is *enough questions to populate the phases that will route from this axis*.

Examples for `decision-making`:
- *"Is this a programmed or non-programmed decision?"*
- *"What's the binding constraint we haven't surfaced?"*
- *"Who has standing on this decision, and who has voice but not vote?"*
- *"What's the cost-of-delay vs the cost-of-being-wrong?"*
- *"What alternatives are we not considering because of cognitive defaults?"*

The questions are concrete and verb-led. They are the load-bearing artefact of this phase; the distillation index will route from queries against them.

**e) Runtime listener grain: what fires the corpus in the moment.**

Practitioner questions name the phases of the work. They do *not* name the moments at which the right framework should fire. A task axis that stops at phase-level routing produces shelf material; a task axis that names the runtime listener grain produces a coach.

The three moves below all need to land before the axis is shippable.

**i) Name the trigger unit.** What does a practitioner of this task *notice in the moment* that should fire the corpus? Examples:
- AAR axis: utterances ("we just need to be more careful"), observed dynamics (defensive routines, blame instincts), silences (where the room won't go).
- Retro axis: energy signals (low engagement, dominant voices, withdrawal), recurring themes across iterations, team-mood patterns.
- Decision-making axis: observations about how the decision is being framed (single-criterion thinking, anchoring, missing alternatives).
- Stakeholder-engagement axis: signals from the relational field (stance shifts, escalation language, power moves, withdrawal).

The trigger unit varies by axis. **Name it explicitly.** If the operator can only describe the trigger as "the practitioner notices something is wrong", the trigger grain is not yet useful; push for the specific *kind* of noticing.

**ii) Name the response unit.** What does the corpus surface *in response to that specific noticing*? Examples:
- A framework with a diagnostic question and a teach-in-the-moment script.
- A structure to deploy (a Liberating Structure, a retro exercise, an inquiry move).
- A reframe to offer.
- A specific source's specific passage, cited and applied.

The response unit must be *teachable in the moment*. "Consider Argyris" is not a response unit; *"Espoused vs. Theory-in-Use as diagnostic: are the team's stated values matching their decisions under pressure? Teach by reading back two recent decisions and asking which value each enacted."* is.

**iii) Produce a seed trigger→response table.** Per phase, list at least five trigger→response pairs (more for axes with rich runtime texture). Each row:
- A trigger phrased in the practitioner's own observable terms (an utterance, a dynamic, a signal), recognisable without classifying the phase first.
- A response naming the framework or structure to surface, with enough texture that `creating-applications` can author the teach-in-the-moment material from it.

The seed table is the most important artefact in the spec. `creating-applications` reads it to author the distillation index's runtime listener tables; `creating-distillations` reads it during Pass G to decide which triggers each source can address.

If the operator can name the phases but cannot produce the trigger→response table, defer the axis until they can name what fires the corpus *in the moment*.

Example seed pairs for `learning-from-incidents` Phase 3 (Analyse):

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| Team converges on "person X made a mistake" within 5 minutes | Deming 94/6 + Dekker local rationality; teach: shift question from "who erred" to "what made this outcome likely" |
| Final "why" in 5-Whys is "we need better training" | Person-shaped vs system-shaped diagnosis; teach: a corrective action that says "be more careful" is a signal you found a symptom category, not a contributing factor |
| Story collapses into single-cause narrative | Multi-chain 5-Whys + Star Model; teach: complex outcomes have networked causality; refuse to pick "the" cause |
| Participant says "we couldn't have predicted this" | Drift signature check; teach: most incidents are gradual margin erosion, not Black Swans; ask what the team was getting away with before this one |
| Two participants give incompatible accounts of the same moment | Local rationality + work-as-imagined vs work-as-done; teach: both accounts are likely true *from where each was standing*; the gap is the system showing itself |

**Anti-pattern: source-chapter triggers.** If the operator's triggers are restatements of source headings ("when discussing contributing factors, surface CFA framework"), the grain is wrong. Triggers come from what the *practitioner observes in the room*, not from what the corpus's chapters are called.

## Phase 3: Corpus fit, which sources apply

List existing reference slugs likely to apply. The claim is provisional; Pass G makes the binding per-distillation call later.

Also surface candidates the operator wants to ingest to fill gaps. Hand off to `finding-resources` and `ingesting-resources` before `creating-applications` runs.

If fewer than three sources plausibly apply, two paths:

- **Ingest first.** `finding-resources` → `ingesting-resources`, then re-enter this skill.
- **Defer the axis.** Acknowledge the corpus is not yet shaped for this task. Park the spec.

## Phase 4: Intended lenses

List lens slugs from `corpus.commons/{corpus}/lenses/` that will reach for this task. If a named lens doesn't yet exist, hand off to `creating-lenses` first.

Per-distillation lens applicability is decided downstream at Pass G. The spec names the lens set the orchestrator carries through; it does not pre-decide which distillations fire.

Default is *no lenses*. Most task axes stay 2D; lenses fire on a minority of distillations.

If the operator names many lenses, ask why. More than three or four may be hiding a sub-axis that should be its own task: *if every lens shifts the projection materially, the lens may be doing the work the axis should be doing*.

## Phase 4a: Intended runtime agents

A *runtime agent* is a Claude Code custom agent definition shipped in the compiled distribution at `.claude/agents/{agent-slug}.md`. The agent is the practitioner-role entry point: tool palette, model tier, pacing rule, refusal list specialised to one role on this axis.

Zero or more agents per axis, depending on how many practitioner roles the axis serves with materially different work.

Three diagnostic questions:

**a) How many practitioner roles does this task axis serve with materially different work?** If one, declare one agent (or zero if generic Claude reading the corpus is sufficient). If several, declare one per role.

Test for "materially different work": would the *pacing*, *refusal list*, *tool palette*, or *model tier* differ? If yes, separate agents. If the only difference is which corpus subsections the role reads, that's the same role with different topical interests; one agent, let macro-routing handle it.

**b) For each agent, what is the role doing in one sentence?** Verb-and-noun. *"Facilitates a 60-90 minute AAR session interactively, one phase at a time"*: yes. *"Helps with AARs"*: too generic.

**c) Does each agent need something the generic-Claude default doesn't provide?** A pacing rule, a refusal list, or a constrained tool palette. If not, drop the agent declaration.

Spec field is a list of agent slugs (verb-and-noun, kebab-case): `aar-facilitator`, `aar-learning-coach`, `retro-coach`. Each gets a file at `.claude/agents/{agent-slug}.md` authored by `creating-applications`.

If the file already exists (operator hand-authored), `creating-applications` validates against the role description rather than overwriting.

**Default:** zero agents. Add only when practitioner-role differentiation is load-bearing.

## Phase 5: Overlap with existing task axes

Does this task overlap with existing axes in the corpus? Name the overlap concretely.

Two kinds of overlap:

- **Complementary overlap.** Both axes apply to the same situation but emphasise different work. Example: `decision-making` and `stakeholder-engagement` overlap heavily, since a decision affecting stakeholders is both a decision and an engagement. Each axis is reached for a different lead question (*what should we do?* vs *how do we talk about it?*). Complementary overlap is healthy; the matrix architecture is built for it.
- **Collapsing overlap.** Two candidate axes serve the same practitioner question through the same source projection. Example: `decision-making` and `decision-quality-assurance` collapse because the practitioner question (*am I making this decision well?*) is the same. One of the two should be merged or renamed.

Name overlap explicitly. Sources whose existing distillations may need integration-section updates after the new axis lands should be flagged here; the orchestrator (`creating-applications`) reads this field to know which deeps may need refreshing.

## Phase 6: Success criteria

How would the operator know in 3-6 months whether this task axis was worth the work? One paragraph.

Two shapes work:

- **Use-pattern criterion.** *"A practitioner using the `{profile}` app should be able to drop their {situation} into the assistant and get routed to the right distillation on 8/10 substantive queries without grep-and-read."*
- **Corpus-state criterion.** *"The distillations for {sibling axis} should have non-trivial cross-references to this axis by month 3, showing the axes carry adjacent work that practitioners actually traverse."*

Both shapes are forward-looking and falsifiable. Aspirational language ("becomes the canonical resource for X") is too soft to evaluate; rewrite if the operator drifts there.

## Phase 7: Spec assembly

Render at `corpus.commons/{corpus}/tasks/{task-slug}.md`. Template:

```markdown
---
name: {Task name}
slug: {task-slug}
corpus: {corpus-name}
created: {date}
status: scoped | assembled
---

# {Task name}

**Slug:** `{task-slug}`
**Purpose:** {one sentence — what work this axis supports, in what circumstance, for what practitioner}

## 1. Problem statement

{One paragraph. Concrete, not aspirational. The verb-and-noun job, the circumstance, the practitioner. Reflects Phase 2(a).}

## 2. Practitioner questions

{Five to ten concrete questions, each starting with a verb or a question word. These seed the phase decomposition in the distillation index. Reflects Phase 2(d).}

## 2a. Runtime listener grain

**Trigger unit:** {what the practitioner notices in the moment — utterances, dynamics, energy signals, silences, observed artefacts. Named specifically; see Phase 2(e)(i).}

**Response unit:** {what the corpus surfaces in response — framework + teach-in-the-moment script, structure to deploy, reframe, inquiry move. Named specifically; see Phase 2(e)(ii).}

### Seed trigger→response table

{Per-phase tables, **at least five rows per phase**. Each row pairs a real-time-recognisable trigger with the response the corpus should fire. The AAR-INDEX precedent runs 7–15 rows per phase; aim for the texture, not the minimum. Reflects Phase 2(e)(iii).}

**Phase 1: {phase name}**

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| ... | ... |

**Phase 2: {phase name}**

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| ... | ... |

{Repeat per phase.}

## 3. Available sources

{List of existing reference slugs in the corpus likely to apply. Plus any new sources the operator plans to ingest before running `creating-applications`. Pass G inside `creating-distillations` makes the binding per-distillation call later. Reflects Phase 3.}

## 4. Intended lenses

{List of lens slugs that will reach for this task. May be empty (most axes are lens-neutral). Reflects Phase 4.}

## 4a. Intended runtime agents

{List of agent slugs and a one-sentence role description for each. May be empty. Each entry shape:

- `{agent-slug}`: {one-sentence verb-and-noun role description, naming pacing/refusal/tool palette difference from generic Claude where applicable}.

Reflects Phase 4a.}

## 5. Overlap

{Named overlaps, both complementary and collapsing. Names sources whose existing distillations may need integration-section updates. Reflects Phase 5.}

## 6. Success criteria

{One paragraph, forward-looking, falsifiable, evaluable in 3-6 months. Reflects Phase 6.}

## Discipline

- **Verb-and-noun.** The job is named with a verb and a noun. Adjectives are not a task; nouns alone are not a task.
- **Job × circumstance.** A task is a job in a circumstance, not a domain. The circumstance is the route a query takes to find the axis.
- **Hire requires fire.** Adopting this task displaces a named older frame. The fire is recorded here: {what gets fired}.
- **Phases route from practitioner questions.** The distillation index inherits the phase decomposition from the practitioner questions, not from the source's chapter structure.
- **Runtime listener grain.** The seed trigger→response table in §2a names what fires the corpus in the moment. `creating-applications` inherits the grain to author the distillation index's runtime tables; `creating-distillations` reads it at Pass G to map each source's content to the triggers it can address.
- **Runtime agents (optional).** §4a names zero-or-more practitioner-role agents the application ships. Empty by default; populate when practitioner-role differentiation requires materially different pacing, refusal lists, or tool palettes per role. `creating-applications` authors one agent file per declared agent at `.claude/agents/{agent-slug}.md`.

## Author anchors

- Christensen, *Competing Against Luck* (2016): the JTBD framework anchoring the verb-and-noun + job × circumstance discipline.
- {others as they apply to the specific axis}
```

Render in the operator's voice. Avoid stock phrases. Write the practitioner-questions section specifically enough that `creating-applications` can seed the phase decomposition from it.

## Phase 8: Go / no-go

Apply the heuristics:

**GO if:**
- The slug passes the verb-and-noun gate.
- The job × circumstance survives Phase 2's discipline: verb-and-noun named, circumstance richly spelled, alternatives that cross categories, a fired frame named.
- **The runtime listener grain is named: trigger unit, response unit, and a seed trigger→response table with at least five rows per phase.** This is what separates a scoping doc from a coach-shaped projection brief.
- The corpus has at least three references that plausibly apply (or the operator commits to ingesting them before `creating-applications`).
- The overlap with existing axes is named, with no collapsing overlap unresolved.
- The success criterion is forward-looking and falsifiable.

**NO-GO (rework):**
- No verb-and-noun job survives the gate. The candidate is a domain, not a task.
- The operator can't list five practitioner questions. The axis isn't ready; revisit when the practitioner work is clearer.
- **The operator cannot name a trigger unit, or cannot produce a seed trigger→response table at any phase.** The axis is not ready to project as a runtime artefact; defer until the practitioner observation work is clearer.
- The corpus has zero or one source that plausibly applies. Run `finding-resources` first.
- Collapsing overlap with an existing axis. Merge or rename.
- Success criterion is aspirational rather than falsifiable. Rewrite.

**YELLOW (ship with explicit caveat):**
- The corpus has two or three sources that apply but the operator wants the axis assembled now. Ship as a *thin axis*; the spec carries the thin-corpus caveat in field 3.
- The task axis has high overlap with an existing axis but the operator judges the dual maintenance worth it. Ship; the spec carries the overlap as an open issue.
- The fired frame is named but the operator cannot produce an example where the old frame currently produces the wrong reading. Ship; expect the axis to read poorly for the first weeks until the old frame stops firing on routing.

After GO, point the operator at `creating-applications` with this task spec as input.

## Failure modes to watch in the dialogue

- **Domain-stuck.** Candidate slugs come back as domains, not tasks: `software-business`, `leadership`, `data-engineering`, `marketing`. Push the verb-and-noun question: *what does a practitioner of this **do**?* If the answer doesn't land in verbs and nouns, the domain hasn't decomposed into tasks yet; defer.

- **Verb-without-circumstance.** A verb-and-noun job arrives without a circumstance. *"Decision-making"* in the abstract is the canonical example. The circumstance is the route a query takes; without it, the axis is unroutable.

- **Adjective-driven.** *"Strategic"*, *"thoughtful"*, *"careful"*: these describe the *manner* of the task, not the task. Manner is a lens; task is the verb-and-noun. Separate them.

- **Phase decomposition from source chapters.** Phases mirror an existing source's chapter structure rather than the practitioner questions. Conflates source organisation with task structure. The distillation index is a situation-to-resource router, not a table of contents.

- **Missing trigger grain.** Phases and practitioner questions are in hand but the *in-the-moment-noticeable* signal isn't. Without the trigger grain, `creating-applications` can author only a phase-level catalogue, not a runtime listener. Push: *when the practitioner is mid-task and the right framework needs to surface, what observable signal tells them to reach for it?*

- **Abstract triggers.** Triggers come back conceptual ("when the team's decision-making is biased", "when stakeholders are misaligned") rather than observable (a specific utterance, an observed silence, a recurring phrase). Conceptual triggers can't be recognised in real-time without first classifying the situation, which defeats the listener. *"People say the right thing but decisions reveal otherwise"* is observable; *"when there's a values-action gap"* is conceptual.

- **Unteachable responses.** A framework arrives as the response unit without naming what the practitioner does *with* the framework in the moment. *"Surface Argyris"* is not a response unit; *"Espoused vs. Theory-in-Use: read back two recent decisions, ask which value each enacted"* is. The framework is shelf material until it teaches in the moment.

- **Trigger table as source restatement.** Triggers come back as restatements of source headings or chapter titles ("when discussing contributing factors, surface CFA framework"). This is the source's organisation projected upward, not the practitioner's observation projected downward. Triggers come from the room, not the table of contents.

- **Lens proliferation.** Eight lenses for one new axis often signals an axis that's too broad: what looks like one task with many lenses is several adjacent tasks. *If every lens shifts the projection materially, the lens is doing the work the axis should be doing.*

- **Source-set thinness.** Two sources apply, the axis ships anyway. Yellow it: thin distillations in the matrix are honest, but the architectural shape gets committed (thin column, thin distribution).

- **Success-criterion drift.** *"Becomes the canonical resource for X"*: too soft. *"Practitioners use it instead of training data on N% of queries"*: falsifiable.

- **Overlap that collapses.** A new axis serves the same practitioner question through the same source projection as an existing axis. Two near-identical distillations result. Merge or rename; don't ship both and let runtime sort it out.

- **"It's a domain but I want it as a task."** The honest move is `creating-corpus` for a sub-corpus dedicated to the domain, with tasks inside it, not bending `creating-tasks` to accept a domain as a task.

## Related skills

- `creating-corpus`: scaffolds a new corpus before its first task can be scoped.
- `finding-resources`: triages candidate sources. Useful when the corpus has thin coverage on the candidate axis.
- `ingesting-resources`: runs the 9-pass protocol on a new source.
- `creating-lenses`: designs a lens spec. Run before this skill if a Phase 4 lens doesn't yet exist.
- `creating-applications`: assembles the application from the task spec this skill produces.
- `creating-distillations`: per-distillation projection that `creating-applications` orchestrates.
