---
name: creating-lenses
description: Design a lens: the per-distillation modifier described in `docs/reference/vocabulary.md` that shapes a distillation through a perspective, role, or methodology stance. The skill is a single-process dialogue; the output is a lens spec at `corpus.commons/{corpus}/lenses/{lens-slug}.md`, ready to feed Pass G of `creating-distillations` when the operator decides which distillations the lens applies to.
argument-hint: "[optional: candidate lens name or rough idea]"
---

# Creating Lenses

A lens is a window with characteristic salience, weighting, and vocabulary. The matrix stays 2D by default (reference × task); a lens optionally shapes a distillation at projection time. This skill produces the spec the lens-applicability gate consumes.

Dialogue skill, one lens per session, no subagents. Output feeds `creating-distillations` Pass G: see [`projection-protocol.md`](../creating-distillations/projection-protocol.md) §Lens-as-optional-framing for the four-outcome applicability gate.

Three kinds of lens are first-class: personifiable-archetype, named-real-person, non-personifiable-frame.

## When to use

- The operator wants to add a lens to a forked or in-development application and needs to scope it rigorously before any per-distillation projection.
- An existing role label ("a CFO", "a senior engineer") is being used as if it were a lens but has no circumstance attached, and the looseness is producing thin lens-shaped artefacts.
- The operator has source material for a real person (LinkedIn, posts, talks) and wants a lens grounded in that material rather than an archetype.
- Two candidate lenses look like one (or one looks like two) and the boundary needs spelled.

## When not to use

- The lens is already well-scoped and stable; the operator is in implementation mode and needs `creating-distillations`.
- The frame is a one-off prompt-shaping, not a library-level artefact.
- The operator is asking for a lens index across many lenses. This skill scopes one lens at a time.

## Inputs

- Optional: a candidate lens name or rough idea ("we should have a CFO lens", "I want a queue-physics lens").
- Optional: source material for the named-real-person case (LinkedIn URL, posts, talks). The operator pastes or cites; the skill treats it as a mini-reference.
- Optional: existing lenses or task axes the new lens might overlap with.

## Output

A lens spec at `corpus.commons/{corpus}/lenses/{lens-slug}.md`. Slug conventions:

- Personifiable-archetype: `{role-or-archetype}-{distinguishing-circumstance}.md`, e.g. `engineering-manager-post-incident.md`.
- Named-real-person: `{first-last}-{role-or-distinguisher}.md`, e.g. `jane-doe-acme-cfo.md`. The slug names the person; the circumstance is in the file.
- Non-personifiable-frame: `{frame-name}-lens.md`, e.g. `loss-aversion-lens.md`, `queue-physics-lens.md`.

The spec has six sections. Every kind fills the same six sections; what each section *contains* differs by kind, the *standard* does not.

## Phase 0: Frame the work

Read aloud to the operator:

> A lens spec has six sections. The first decision, kind of lens, changes what every answer that follows will contain, so we'll commit early and revisit only if the kind turns out wrong. The standard for rigour is the same across kinds: a job described in verbs and nouns, circumstance or condition spelled out, what gets displaced when the lens is hired, a grounding contract that says where the lens's intelligence comes from and what it refuses.

Confirm the operator wants to proceed.

## Phase 1: Kind of lens

Three diagnostic questions. The operator commits to a kind at the end of this phase; the rest of the skill branches accordingly.

**a) Is there a real person you can point to in the chair when this lens is in use, with their own published material to draw from?**

If yes, with citable material (LinkedIn page, published posts, talks, interviews), and the operator wants the lens grounded in that person specifically: **named-real-person**. This is its own kind. The extra discipline: the source material is cited and treated as a mini-reference; the lens reads *as if Jane Doe were reading, given what her public material reveals about her stance*, not *as Jane Doe*. Ventriloquism is the failure mode and the grounding contract guards against it.

*The self-case is a sub-kind of named-real-person, where the named person is the operator running the skill.* The same six sections, the same grounding-contract discipline, the same ventriloquism guard — sharpened: *reads as if {operator}-at-time-T were reading; it is not {operator}-now, and {operator}-now is the seer choosing to look through it*. When source material in the operator's own voice is thin (fewer than two or three citable artefacts), do not run this skill directly. Use [`gridmaker-interview`](../gridmaker-interview/SKILL.md) instead — it runs a structured 10–15 minute interview that generates the source material, then renders the lens spec following the template below. `gridmaker-interview` defaults to writing into `corpus.local/personal/lenses/`.

**b) Without a specific person, is there a role-in-circumstance you can point to?**

Not "a CEO": that's an adjective. *"A CEO 48 hours after a P0 incident, regulator calling Monday, board chair asking for a one-pager"*: that's a circumstance. If yes, **personifiable-archetype**. If the operator answers in role labels with no circumstance, push back. Christensen's jobs-to-be-done discipline (*Competing Against Luck*, 2016) is what stops a role label from masquerading as a lens: the situation makes the lens specific, not the title.

**c) If you imagine the lens reading something, does it read with a person's voice, or is it more naturally a frame of attention the tool applies?**

If frame of attention: **non-personifiable-frame**. The loss-aversion lens reads through one principle; it has no idioms or anxieties of its own. The queue-physics lens reads pipelines as networks of utilisation and variability; it doesn't speak. Forcing a frame into person-form makes the tool cuter and worse.

Commit the kind in one short paragraph: which kind, and why this and not another. The kind is provisional through Phase 2; if the job spec doesn't survive the chosen kind, revisit.

## Phase 1b: Visibility

Before moving to content, ask:

> "What's the visibility of this lens? `open` (safe for any audience), `open-nc` (open with non-commercial intent), `copyrighted` (third-party material), `confidential` (client/engagement-bound), or `personal` (operator only)?"

Record the answer as `visibility:` in the lens frontmatter. No silent default. Every new lens must carry the declaration; if the operator does not answer, ask again.

**Spec-location gate.** If the operator selects `copyrighted`, `confidential`, or `personal` while authoring into `corpus.commons/`, warn:

> "Lenses with visibility `{level}` cannot live under `corpus.commons/`. The build will fail if the file lands there. Would you like me to author it to `corpus.local/{corpus}/lenses/{lens-slug}.md` instead?"

Wait for the operator's decision before writing any file. For `open` and `open-nc`, proceed to `corpus.commons/` as normal.

The visibility level determines where the file lands and which profiles ship it. Settling it now prevents a build failure later.

## Phase 2: Job × circumstance, or frame × condition

Every lens has a job. The job is what the lens is hired to do when the tool reaches for it. The circumstance (or condition) is what determines when this is the right lens to reach for.

The verb-and-noun rule applies across kinds. If the operator answers in adjectives ("the strategic lens", "the careful lens"), the jobs discipline applies: ask the verb-and-noun follow-up. *What does this lens read, under what condition, and what does its read produce that another lens's read does not?*

### Personifiable-archetype

a. **Name the job in verbs and nouns.** Not "make sense of incidents". *"Read this outage report the way a board chair would, looking for what protects the company's reputation when the regulator calls on Monday."*
b. **Spell the circumstance.** Where, when, with whom, what just happened, what comes next, what social or commercial pressure is on them. Richer constraint produces a more useful lens.
c. **Alternatives from different categories.** What might the user reach for instead? *Do nothing*, *use another lens*, *talk to a person*, *consult a different reference*. If every alternative is another lens of the same kind, the job is drawn too narrowly.
d. **Hire requires fire.** What older frame, instinct, or template does adopting this lens displace? This is the half people skip. *Fires the board-narrative reflex of attributing outages to a single individual.* *Fires the 'we communicated benefits clearly' instinct.* Specifically named; not vague.

### Named-real-person

Same skeleton as archetype, plus:

a. **Source material is cited.** Pull in the operator's LinkedIn URL, the three posts, the talk transcript. Each is treated as a mini-reference the spec carries forward. If the material is thin (fewer than two or three citable artefacts in the person's own voice), flag the lens as YELLOW in Phase 6: the operator can ship, but the grounding contract carries a probationary status.
b. **The as-if clause is explicit.** *"The lens reads as if Jane Doe were reading, given what her public material reveals about her stance"*: not *as* Jane Doe. The job description names the as-if explicitly.
c. **Ventriloquism guard.** The grounding contract (Phase 4) names it. If the named-real-person lens drifts into putting words in Jane Doe's mouth that her source material does not support, the lens has failed the trust bar.

### Non-personifiable-frame

a. **Name the frame in verbs and nouns.** Not "queue physics lens". *"Read this delivery pipeline as a network of queues whose throughput is governed by utilisation and variability, and surface the queue most starved or most flooded."*
b. **Spell the condition.** When in the tool's flow does this frame get reached for? On what kind of input? At what step? *Condition* is to a frame what *circumstance* is to a persona: same discipline, different name.
c. **Alternative frames.** What else could the tool reach for to read the same situation? Where does this frame outperform; where is it dominated?
d. **What the frame fires.** Adopting a queue-physics lens displaces the "more people will fix it" instinct. Adopting a loss-aversion lens displaces the "we communicated benefits clearly" instinct. Naming what gets displaced is what makes the lens actionable; without it, the lens is decorative.

### Stop-condition

If no job survives the discipline (verb-and-noun, circumstance or condition richly spelled, alternatives that cross categories, something specific gets fired) the lens does not have a job. Either rewrite it or recognise it as a flavour of an existing lens and merge.

## Phase 3: What the lens fires (the fire test)

Phase 2(d) named what gets fired. Phase 3 makes the fire explicit and tests it.

a. **Is the fired frame named, or vague?** Vague doesn't count. "Old way of thinking" is not a fire. *"Fires the board-narrative reflex of attributing outages to a single individual"* is a fire.

b. **Is the fired frame *active* in current outputs?** If the operator can't show an example where the fired frame currently produces the wrong reading, the new lens may be solving an imagined problem. Push for the example. (For library lenses, the example is a real query the existing distillations answer poorly through the missing frame.)

c. **Will the fired frame go quietly?** Habits don't surrender on instruction. If the fired frame is entrenched, the lens needs a displacement plan: repeated reweighting at retrieval time, contrast with the old read explicitly, or pre-projection at Pass G into the distillations where the fire most needs to land.

If the fire test fails (nothing named, no example, no displacement plan), the lens does not have purchase. Mark YELLOW in Phase 6.

## Phase 4: Grounding contract

This is the load-bearing section. The contract is the spine of the spec, not an appendix.

a. **Where does the lens's intelligence come from?**
   - *From the corpus.* The lens draws on one or more references already in the library. Name them by slug. Highest defensibility: the lens's reads trace to ingested references that have passed the source-only audit.
   - *From a tradition or synthesis.* The lens is a composite (e.g. a "drift lens" combining accident-modelling traditions) and carries an explicit provenance note naming each contributing author and the fragment they contribute.
   - *From the model's priors.* The lens has no corpus anchor. Allowed, but the trust bar is lower and the spec flags it.
   - *From cited external material (named-real-person only).* The person's published material is the source; the spec carries the URLs and treats them as a mini-reference.

b. **What does the lens refuse?**
   - A corpus-grounded lens refuses to fabricate when its references are silent.
   - A non-personifiable frame refuses to over-read: it names the limit of its frame (queue physics doesn't read culture; loss aversion doesn't read systemic incentive design).
   - A personifiable-archetype lens refuses to ventriloquise: it doesn't claim a voice it has no warrant for.
   - A named-real-person lens refuses to assert what the person's source material doesn't support. Ventriloquism is the explicit failure mode.

c. **Anthropomorphism guard.** Phrase the guard in the lens file itself. A lens does not need to be personified. *Agent* is a convenient label for software that mimes human behaviour, but the underlying mechanism is different: no human greps a book. A lens shapes what the assistant reads through; it does not pretend to be a self doing the reading. Configuring a lens as if it were an agent loads in scaffolding (voice, motivation, anxieties) the runtime does not use and cannot honour.

   - For personifiable-archetype: the spec opens with *this lens reads as if X were reading; it is not X*.
   - For named-real-person: the as-if clause names the person and the source material. Drift into first-person voice of the named person is the alarm.
   - For non-personifiable-frame: no first-person pronouns; no claims of feeling; the voice is structural.

d. **Three trust-breaking failure modes, named concretely.** Examples:
   - A citation that resolves to nothing.
   - A read that contradicts what the operator can see directly.
   - A voice too confident given the lens's actual range.
   - For personifiable-archetype: ventriloquism.
   - For named-real-person: putting words in the person's mouth their material does not support.
   - For non-personifiable-frame: scope creep, the frame reading things outside its range.

## Phase 5: Spec assembly

Render the spec as a single document. Save to `corpus.commons/{corpus}/lenses/{lens-slug}.md`. Template:

```markdown
---
name: {Lens name}
kind: archetype | real-person | frame
slug: {lens-slug}
visibility: open | open-nc | copyrighted | confidential | personal
---

# {Lens name}

**Kind:** archetype | real-person | frame
**Purpose:** {one sentence: what this lens reads, under what condition, and what its read produces that other lenses' reads do not}

## Job × circumstance (or frame × condition)

{The verb-and-noun job statement. The circumstance or condition richly spelled. The alternatives the lens displaces, across categories. The fire-list: what older frame this lens replaces when adopted. For named-real-person: the as-if clause and the source material cited.}

## What the lens fires

{The named, current, displaceable frame this lens replaces when adopted. The example where the fired frame currently produces the wrong reading. The displacement plan if the fired frame is entrenched.}

## Grounding contract

- **Intelligence source:** corpus / synthesis / model priors / cited external material
- **Refuses:** {what the lens does not do}
- **Anthropomorphism guard:** {the as-if clause; the structural-voice rule; the alarm signal for drift}
- **Trust-breaking failure modes:** {three, named concretely}

## Source material  (named-real-person only)

- {citations: LinkedIn URL, post titles and URLs, talk transcripts, interviews}

## Author anchors

- Christensen, *Competing Against Luck*: for the jobs framework that grounds the job × circumstance / frame × condition discipline.
- {others as they apply to the lens's intelligence source}

## Salience and vocabulary

{What this lens notices first. What recedes. The lens's native vocabulary. Specific. This is what the retrieval-time fallback in `projection-protocol.md` reads to apply the lens cheaply at query time when no pre-projected distillation exists.}

## Response modulation (when the task axis carries field 2a)

{Optional. When the lens applies to a task axis whose spec carries field 2a (trigger→response tables), describe how this lens reshapes the *response unit*. The trigger unit (what the practitioner observes) does not change under a lens; the response unit may shift to foreground different sources, vocabulary, or framings. Example: a *board-chair* lens applied to the AAR axis doesn't change the trigger "team converges on X made a mistake" but reshapes the response from a Just-Culture decision-tree teach to a *narrative-protection* teach. If lens-neutral on task-spec triggers, write *"no response modulation; lens applies at retrieval-time fallback only"*.}
```

Render in the operator's voice. Avoid stock phrases. The salience-and-vocabulary section is what the retrieval-time fallback uses; write it specifically enough to be useful when no pre-projected (source, task, lens) distillation exists. The response-modulation section tells `creating-distillations` how to reshape the teach-in-the-moment scripts at Pass G.

## Phase 6: Go / no-go

Apply the heuristics:

**GO if:**
- The kind is committed and survives Phase 2's discipline.
- A job × circumstance or frame × condition row survives the boundary tests: the job stated in verbs and nouns, the situation spelled, alternatives that cross categories, an older frame named that this lens replaces.
- The fire test passes: something specific and current gets displaced.
- The grounding contract is committed in writing, with three concrete trust-breaking failure modes.

**NO-GO (rework):**
- No row survives the boundary rules. Either rewrite or merge with an existing lens.
- The lens is personifiable on paper but the operator cannot sustain the circumstance richness. Either add circumstance or recast as non-personifiable.
- The lens is non-personifiable but the operator keeps slipping it back into person-form. It has a hidden personification; restart Phase 1 with that admission.
- The operator cannot commit to the grounding contract. The lens has no spine; build something else.

**YELLOW (ship with explicit caveat):**
- Named-real-person status without enough citable material (fewer than two or three artefacts in the person's own voice). Ship as probationary; the spec carries the caveat.
- The lens has high overlap with an existing lens. Ship, but the spec carries the deduplication question as an open issue.
- The fire test surfaces a fired frame but no displacement plan. Ship; expect the lens to read poorly for the first weeks until the old frame stops firing.

After GO, two index-update steps before the lens is reachable at runtime:

1. **Add a row to `corpus.commons/{corpus}/lenses/LENS-INDEX.md`.** Five columns: `Kind`, `Slug` (as a `[slug](slug.md)` link), `Purpose` (one sentence, copy the spec's `**Purpose:**` line), `Reach for when` (one sentence, when this lens fires), `Native vocabulary & salience`. The salience cell follows a strict three-part shape the JSON builder parses: `Notices first: <comma-separated phrases>. Recedes: <comma-separated phrases>. Native: *<comma-separated italicised phrases>.*` Break this shape and the build fails.
2. **Rebuild the runtime JSON.** Run `python -m scripts.build_indexes.build_lens_index --corpus {corpus}`. The builder parses the LENS-INDEX.md table, splits the salience cell into the structured `salience` block (`notices_first`, `recedes`, `native_vocabulary` as a phrase list), and writes `corpus.commons/{corpus}/lens-index.json`. The JSON is what `answer-from-corpus`'s lens-applicability check reads at runtime; the markdown stays as the operator-inspection view.

Then point the operator at `creating-distillations` with this lens named (standalone, or via `creating-applications` orchestration when the lens applies across multiple distillations). The lens spec feeds Pass G's per-distillation applicability evaluation; it is not a substitute for it. The lens may apply to many distillations, a few, or none: the per-distillation gate decides.

## Failure modes to watch in the dialogue

- **Adjective-stuck.** The operator describes the lens in adjectives ("strategic", "careful", "thorough"). Ask the verb-and-noun follow-up: *what does this lens read, under what condition, and what does its read produce that another lens's read does not?* If the operator can't get past adjectives, the lens does not have a job yet.

- **Role-without-circumstance.** "A CEO lens", "a finance lens". Ask the circumstance. Where? When? Just after what? With whom? The lens that survives the question is a lens; the lens that doesn't is an adjective wearing a job title.

- **Personifiable-by-default.** The operator's instinct is to reach for a persona when a frame would do. Ask whether the lens needs a person, or whether the frame survives without one. Most lenses worth having are non-personifiable; the persona shape is a familiar template, not a design conclusion.

- **Source-thin named-real-person.** The operator names a real person but has only the LinkedIn page: no posts, no talks, no material in the person's own voice beyond the profile. Flag the lens YELLOW. The lens can ship, but the spec carries a probationary status until the source material thickens.

- **Fire without example.** The operator names what the lens fires but cannot produce an example where the fired frame currently produces the wrong reading. Push for the example. A lens that fires nothing actually wrong is a lens solving an imagined problem.

- **Grounding-contract drift.** The operator's intelligence source is "the model" but the spec is described as if it were corpus-grounded. Name the source explicitly. Model-priors lenses are allowed; their trust bar is lower, and the spec flags it.

- **As-if collapse (named-real-person).** The operator slips from *reads as if Jane Doe were reading* to *reads as Jane Doe*. The as-if clause is explicit, the anthropomorphism guard is named, and ventriloquism is one of the three trust-breaking failure modes the spec carries.

- **Scope creep (non-personifiable-frame).** The operator wants the queue-physics lens to read culture, or the loss-aversion lens to read systemic incentive design. The frame's refusal is part of the grounding contract. *Queue physics doesn't read culture.* *Loss aversion doesn't read systemic incentive design.* The refusal is what keeps the frame useful.

## Discipline (binding)

- *Verb-and-noun rule.* If the operator answers a job or frame question in adjectives, push back. *"The strategic lens"* is not a lens; *"read this acquisition the way the finance team did six months before the deal collapsed"* is moving towards one.
- *Circumstance richness.* "A CEO" is not enough. "Queue physics" is not enough. The constraint that makes the lens useful is what makes it specific.
- *Alternatives from different categories.* If every alternative is the same family of frame, the job is too narrow.
- *Hire requires fire.* No fire = no purchase = no lens.
- *Personification is a tool, not a default.* If the operator wants a persona out of habit, ask whether the frame survives without it. If it does, the lens is non-personifiable.
- *Honest no-coverage.* If the operator cannot answer a phase question, record it as an open question with a recommendation in the spec.
- *Single-process, operator-in-the-dialogue.* No subagents. One lens per session.
- *No code.* The skill produces a spec. Implementation is handled by `creating-distillations` and the runtime.

## Citation in the spec

- Christensen, *Competing Against Luck* (2016), named once at first invocation of the jobs framework. The discipline's rules (verb-and-noun framing, situation over role label, alternatives across categories, older frame named that gets displaced) are then used without re-citation.
- Other authors as the lens's intelligence source warrants. Author and work in prose. No verbatim quotes from copyrighted sources.

## Pre-flight

- For named-real-person lenses, have the source material available before starting. The skill will ask for citations during Phase 2.
- For corpus-grounded lenses, have the relevant reference slugs available so the grounding contract names them concretely.

## Related skills

- `creating-distillations`: per-distillation projection. Takes a lens spec and decides per (source, task, lens) distillation whether to pre-project. See [`projection-protocol.md`](../creating-distillations/projection-protocol.md) §Lens-as-optional-framing.
- `creating-applications`: orchestrates `creating-distillations` across the source set when assembling a new application; lens spec flows through the orchestrator to each per-distillation invocation.
- `ingesting-resources`: if the lens's intelligence source includes references not yet in the library, ingest them first.
- `matching-references`: if the lens is corpus-grounded and the operator is unsure which references anchor it, run this first.
