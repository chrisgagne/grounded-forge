# Open Practice Library, Decision-Making Distillation

**Source:** Open Practice Library (Red Hat Open Innovation Labs community, 2016–present). 266 community-curated practice pages at `openpracticelibrary.com`. Licence: **CC BY 4.0** for content. Cloned commit `8bfa450e75dfba1e2a3c68ac0e514e587f6f116e` (2026-05-13). See `open-practice-library-deep.md` for the full deep reference.

## Decision-Making Relevance

The Open Practice Library is a *meta-source* for decision-making: it does not present a theory of decisions but a community-curated catalogue of named practices that decision-makers can pick up and run. Across the 266 practices, a sharp **decision-making subset** stands out — practices designed to surface options, prioritise among them, commit to action, and review the result. The library treats decision-making as a *facilitated group activity* rather than as a solitary cognitive task: most decision-making practices are short timeboxed group sessions with a facilitator, named participant roles, and a visual output (stickies, dots, scores, a canvas).

The decision frame the library carries is unusually explicit on three points. First, **the decision-making problem is usually a prioritisation problem**, not a single yes/no choice — most of the practices targeted at "decisions" are picking which thing to do next from a list, with the list usually generated in an upstream ideation phase. Second, **consensus is not the goal**; *Disagree and Commit* makes this explicit ("There is a common misconception that collaboration eventually requires consensus; it does not. In fact consensus can come at a very high cost to the team dynamic" (Source: Practice "Disagree and Commit", "Why do it?")). Commitment, not agreement, is the load-bearing outcome. Third, **decision-making decoupled from experimentation is dangerous**; the library repeatedly couples decision practices with experiment-design practices, treating a "decision" as a hypothesis to be tested rather than a settled answer.

This distillation projects OPL practices onto the decision-making task by surfacing the practices appropriate to each phase of a decision — frame the decision, generate options, prioritise among options, commit to action, learn from the outcome — and naming the practices the OPL catalogue offers for each phase. The OPL catalogue becomes a *router*: this distillation tells the decision-maker which OPL practices to pick up next given where they are in the decision.

## Key Concepts for Decision-Making

1. <!-- concept: decision-framing --> **Decision framing before option generation.** Before listing options, decide whether the problem statement is correctly framed. The library offers *Abstraction Laddering* for broadening or narrowing a problem statement, *Is – Is not – Does – Does not* (from Paulo Caroli's Lean Inception) for surfacing what the subject is and is not, and *Five Whys* (Taiichi Ohno) for chasing symptoms to root cause. *Five Whys* carries an explicit warning: "we should ask why the process failed instead of just asking why" (Source: Practice "Five Whys (5 Whys)", "Why do it?"), aimed at the failure mode of stopping at controllable resources rather than systemic processes.

2. <!-- concept: cynefin-framework --> **The Cynefin domain-of-the-decision check.** Snowden's framework, as carried in the OPL practice, asks the decision-maker to classify the decision first: Clear (best practices apply), Complicated (expert analysis surfaces multiple right answers), Complex (cause-and-effect visible only retrospectively; experiment to learn), Chaotic (act first to stabilise), Confused/Aporetic (gather more information). Each domain has a named response pattern: Sense-Categorize-Respond / Sense-Analyze-Respond / Probe-Sense-Respond / Act-Sense-Respond. The classification *gates* what kind of decision-making practice applies: Complex domains call for experimentation-first practices; Clear domains call for checklist-style execution. (Source: Practice "Cynefin Framework", "How to do it?")

3. <!-- concept: design-of-experiments --> **Hypothesis-before-decision discipline.** *Design of Experiments* reframes a "decision" as "a set of well-defined experiments that can be carried out in order to validate ideas, hypothesis and assumptions" (Source: Practice "Design of Experiments", "What is it?"). The minimum experiment fields are Hypothesis / Current Condition / Target Condition / Obstacles / Pass criteria / Measures / Learning. The practice's contrarian: "Successful experiments are not experiments that have proven our assumption as correct. Successful experiments are those that provide valid and reliable data which shows a statistically significant conclusion" (Source: Practice "Design of Experiments", "How to do it?").

4. <!-- concept: premortem --> **Premortem before commitment.** *Backcasting / Pre-mortem* (Klein / Kahneman) asks the group to imagine that the project has failed and reconstruct the reasons (Source: Practice "Backcasting / Pre-mortem", "What is it?"). The practice is explicitly framed as an antidote to groupthink and blind spots in planning. *Start At The End* (from *The Sprint Book*) is the positive twin: describe success first, then enumerate the assumptions that must hold (Source: Practice "Start At The End", "What is it?").

5. <!-- concept: prioritisation --> **Prioritisation as the most-instrumented decision activity.** The library carries a wide cluster of prioritisation practices, each with a different ergonomic profile:
   - **Dot Voting**: simplest; each participant gets N dots and distributes them. Best for quick consensus on a short list (Source: Practice "Dot voting", "What is it?").
   - **$100 Prioritisation**: relative-value allocation; each participant distributes $100 across the options. "Prioritising is hard. This is a method that helps everyone be heard, but also navigates you towards consensus in an equitable way" (Source: Practice "$100 Prioritisation", "Why do it?"). The library recommends combining with 1-2-4-All for the group variant.
   - **MoSCoW Method**: Must-have / Should-have / Could-have / Won't-have. Best for scoping decisions where some items will be cut.
   - **Impact-Effort Matrix**: 2×2 (high/low impact × high/low effort). Best for visible quadrant-based sorting.
   - **How-Now-Wow Matrix**: 2×2 with explicit creativity framing (Now = obvious / How = aspirational / Wow = creative and feasible). Best when ideation has produced many options and some need creative-risk assessment.
   - **The RICE Scoring Model**: Reach × Impact × Confidence ÷ Effort. Best when option-comparison needs explicit quantification.
   - **Eisenhower Box**: urgent × important with four actions (Do / Schedule / Delegate / Delete). Best for personal or small-team task-list decisions (Source: Practice "Eisenhower Box or Urgent-Important Matrix", "What is it?").
   - **Weighted Shortest Job First (WSJF)**: cost-of-delay-divided-by-job-size formula.
   - **Priority Sliders**: forced-allocation across multiple dimensions.

6. <!-- concept: 1-2-4-all --> **The let-everyone-be-heard pattern.** Across decision-making practices the library repeatedly uses a *silent generation → small-group convergence → large-group integration* shape. *1-2-4-All* names this directly: "All voices are heard, incorporating 'silent' conversations and expanding input diversity - No more HiPPOs (Highest Paid Person's Opinion)!" (Source: Practice "1-2-4-All", "Why do it?"). The same shape appears in *10-for-10*, *Silent Brainstorming / Brainwriting*, *6 Dimensions of Discovery*, *Force Field Analysis* (Lewin), and many others.

7. <!-- concept: confidence-voting --> **Confidence and dissent are first-class.** *Confidence Voting* (the 0–5 finger vote, popularised by Jean Tabaka) is the library's checkpoint for *before-commitment* confidence — a fist (0) blocks consensus; five fingers (5) is championship (Source: Practice "Confidence Voting", "How to do it?"). *Dissent Cards* (from L. David Marquet's *Leadership is Language*) institutionalises productive disagreement during option-generation by assigning random must-dissent roles (red cards 1:5 ratio). Both practices are first-class in the library's decision toolchain.

8. <!-- concept: disagree-and-commit --> **Disagree and Commit as the canonical commitment move.** "An approach to enable teams to transition from thinking to doing, whilst ensuring the team are committed to the execution" (Source: Practice "Disagree and Commit", "What is it?"). The practice frames commitment as intrinsic and compliance as the failure mode: compliance, on the other hand, generally results in the bare minimum and a lack of engagement (Source: Practice "Disagree and Commit", "Why do it?"). The two pre-conditions: everybody must have a meaningful choice, and there must be an agreed review point. The practice's design is to reduce the barrier between thinking and executing without coercing consensus.

9. <!-- concept: architectural-decision-records --> **The architectural-decision-record artefact.** *Architectural Decision Records (ADR)* documents the *what was decided and why* once a decision has been made. ADRs support a quick reference to past decisions, stakeholder communication of reasoning, and open transparent communication about why each choice was made (Source: Practice "Architectural Decision Records (ADR)", "Why do it?"). The library treats decision-recording as itself a practice — the decision is not finished when the meeting ends; it is finished when the rationale is in version control.

10. <!-- concept: open-decision-framework --> **The Open Decision Framework.** A Red Hat-originated meta-practice for making transparent decisions; the library carries it as a worked example of how to find an organisation's "why" (Source: Practice "Start With Why", "How to do it?"). The framework's value for decision-making is structural — it surfaces stakeholders, decision rights, and the path from input to commitment, all visibly.

11. <!-- concept: theory-of-constraints --> **The Theory of Constraints applied to decision-making.** The library's *Theory of Constraints* practice frames decision-making in resource-constrained settings: optimise the constraint, not the non-constraints. The framing helps decision-makers avoid the failure mode of solving problems that are not the binding constraint (Source: Practice "The Theory of Constraints", "What is it?").

12. <!-- concept: retrospectives --> **The retrospective as decision-review.** *Retrospectives* (and its many variants — 4Ls, Rose Thorn Bud, Plus Minus Interesting, Realtime Retrospective, Design Retro Active, Futurespective) are the library's mechanism for reviewing decisions: did the decision produce the predicted outcome? what would we change? Decisions are not closed when they ship; they are closed when the retrospective draws an action item from the outcome.

## Questions to Ask During Decision-Making

### Phase 0: Decide whether the situation is a decision at all

| Need | Question | OPL practice |
|---|---|---|
| Check the framing | Is the problem statement correct? Should it be broadened or narrowed? | *Abstraction Laddering* |
| Test the definition | What is the subject? What is it not? What does it do? What does it not do? | *Is – Is not – Does – Does not* |
| Test the cause | If you keep asking "why" five times, what is the root cause? Is it a process issue rather than a resource issue? | *Five Whys* |
| Classify the domain | Is the decision in a Clear, Complicated, Complex, Chaotic, or Confused domain? Which response pattern applies? | *Cynefin Framework* |
| Test the trigger | Is the time/effort proportionate to the consequences? Does the decision need a structured session at all? | *Theory of Constraints*; library-level judgement |

### Phase 1: Frame the decision

| Need | Question | OPL practice |
|---|---|---|
| Imagine the failure | If this fails badly in 12 months, what will the reasons turn out to have been? | *Backcasting / Pre-mortem* |
| Imagine the success | What does success look like in 12 months? What assumptions must hold? | *Start At The End* |
| Surface the elephant | Is there an unspoken issue blocking the conversation that needs to be named first? | *An Elephant in the Room* |
| Establish safety | Is the room safe enough for honest input? Have we done a check-in? | *Check-ins*; *Social Contract* |
| Map the forces | What forces favour this change? What forces resist it? Score each on 1-5. | *Force Field Analysis* (Lewin) |

### Phase 2: Generate options

| Need | Question | OPL practice |
|---|---|---|
| Generate options widely and equitably | Have we heard from everyone before letting the loudest voice dominate? | *1-2-4-All*; *Silent Brainstorming*; *10-for-10* |
| Push for creative options | What would Disney do? What would Tesla do? Who would tackle this differently? | *Alternative Worlds* |
| Stretch beyond the obvious | What are 8 sketched options in 8 minutes? | *Crazy 8s* |
| Ensure dissent surfaces | Is there a structured way to make disagreement productive? | *Dissent Cards* |
| Reframe as experiments | What hypothesis does each option correspond to? What experiment tests it? | *Design of Experiments*; *Experiment Canvas* |

### Phase 3: Prioritise among options

| Need | Question | OPL practice |
|---|---|---|
| Quick group consensus | Who likes which option? Each person gets N dots. | *Dot voting* |
| Relative-value allocation | Each person has $100. Where do you place it? | *$100 Prioritisation* |
| Cut some options explicitly | Which options are Must / Should / Could / Won't? | *MoSCoW Method* |
| Trade impact against effort | Where does each option land on a 2×2 of impact × effort? | *Impact-Effort Prioritisation Matrix* |
| Trade creativity against feasibility | Where does each option land on a 2×2 of feasibility × creativity? | *How-Now-Wow Prioritisation Matrix* |
| Quantify the comparison | What is the Reach × Impact × Confidence ÷ Effort score? | *The RICE Scoring Model* |
| Personal / small-team decisions | Is it urgent? Is it important? | *Eisenhower Box or Urgent-Important Matrix* |
| Cost-of-delay-aware sequencing | What is the WSJF score? | *Weighted Shortest Job First* |
| Force-allocate across dimensions | Where does each option sit on each priority slider? | *Priority Sliders* |

### Phase 4: Check confidence before committing

| Need | Question | OPL practice |
|---|---|---|
| Confidence check before commitment | On a 0-5 finger scale, how confident is each team member in this decision? | *Confidence Voting* |
| Surface remaining concerns | Anyone showing 0, 1, or 2 fingers — what is your bottom-line reason? | *Confidence Voting*, "Learn and gain consensus" mode |
| Re-vote after surfacing | Have we addressed the dissent enough to re-vote? | *Confidence Voting*, "Vote and move forward" mode |

### Phase 5: Commit to action

| Need | Question | OPL practice |
|---|---|---|
| Move from thinking to doing | What is the first step each person commits to? With whom? By when? | *Action steps* |
| Commit without forcing consensus | Can the dissenters commit to executing while preserving their disagreement? | *Disagree and Commit* |
| Define the review point | When will we inspect the outcome? What evidence will tell us to course-correct? | *Disagree and Commit* (review-point pre-condition) |
| Record the decision | What was decided? Why? What were the options considered? | *Architectural Decision Records (ADR)* |
| Define what "done" means | Have we agreed on the Definition of Done for this decision's execution? | *Definition of Done* |

### Phase 6: Review the decision after the fact

| Need | Question | OPL practice |
|---|---|---|
| Inspect and adapt | Did the decision produce the predicted outcome? What worked? What didn't? | *Retrospectives*; *4Ls Retrospective*; *Rose, Thorn, Bud*; *Plus, Minus, Interesting* |
| Diagnose post-incident | If the decision led to an incident, what factors contributed? | *Blameless Postmortem* |
| Track decision-as-experiment | Did the experiment pass? What did we learn? | *Design of Experiments*, "Learning" field |
| Course-correct | Should we course-correct? At what review point? | *Disagree and Commit* (review-point) |

## What to Look For

- **Pattern: The loudest voice is driving the priority.** Signal: the team has a direction before anyone has spoken, or quieter members withdraw after the first proposal. Diagnosis: HiPPO (Highest Paid Person's Opinion) pattern — "No more HiPPOs!" is the explicit OPL framing. Follow-up: run a silent-generation practice (1-2-4-All, Silent Brainstorming) before any open discussion; surface all views before any view is evaluated.
- **Pattern: The group is moving toward consensus without confidence.** Signal: agreement is emerging but the energy in the room feels flat or forced. Diagnosis: probable coerced consensus — "If there is disagreement within the team, consensus is generally achieved through coercion." Follow-up: run Confidence Voting before the commitment step; surface 0-2-finger concerns before they become latent dissent in execution.
- **Pattern: The decision is framed as a yes/no when it is really a prioritisation.** Signal: the conversation is stuck on whether to do a thing rather than which things to do in what order. Diagnosis: wrong decision frame — most OPL decision practices are prioritisation tools, not binary-choice tools. Follow-up: reframe as "given N options, which do we invest in next and in what order?"; run a prioritisation practice.
- **Pattern: A decision is being treated as settled when no review point has been set.** Signal: commitment was reached in the session, but nobody named when the decision will be revisited. Diagnosis: missing review point — Disagree and Commit's second pre-condition is "an agreed review point." Follow-up: name the review point before ending the session; put it in the ADR.
- **Pattern: The same failure is recurring across retrospectives.** Signal: the same issue appears in multiple retrospectives with action items that never clear. Diagnosis: the retrospective is producing observations, not decisions; or the decisions are not being followed by committed actions with owners. Follow-up: use Action Steps practice; require a named owner, named next step, and a deadline for every retrospective action.
- **Pattern: A complex domain decision is being treated with best-practice tools.** Signal: checklists, standard playbooks, and established procedures are being applied to a situation exhibiting significant uncertainty. Diagnosis: Cynefin domain misclassification — Complex domains call for Probe-Sense-Respond (experiment first), not Sense-Categorize-Respond (apply best practice). Follow-up: run Cynefin classification as Phase 0; if the domain is Complex, reframe options as experiments with hypothesis and pass criteria.

## When to Use This Reference

- A team needs a structured group session to make a decision and wants a named practice to run.
- A prioritisation problem has many options and the team needs an equitable method for choosing among them.
- A decision is being made in a group and the HiPPO pattern or groupthink risk needs structural mitigation.
- A commitment is approaching and the team needs to surface latent dissent before execution begins.
- A decision needs to be recorded with rationale so future decision-makers can understand the original reasoning.
- A post-decision review needs to be structured (retrospective, blameless postmortem, design-of-experiments learning stage).
- A facilitator needs a route from "we have a problem" to "we have a committed next action" with named steps and tools.

## Anti-patterns This Reference Helps Avoid

- **HiPPO decisions** (Highest Paid Person's Opinion). The library treats the HiPPO failure mode as the canonical anti-pattern; *1-2-4-All* and the silent-generation pattern across many facilitation practices are designed against it.
- **Coerced consensus.** Consensus achieved through coercion produces compliance, not commitment. The library's contrarian (*Disagree and Commit*): "consensus can come at a very high cost to the team dynamic. If there is disagreement within the team, consensus is generally achieved through coercion; team members try to be compelling rather than curious, they ask leading and self-affirming questions, suppress dissent and push for consensus" (Source: Practice "Disagree and Commit", "Why do it?").
- **Analysis paralysis.** The library names this failure mode explicitly in *Disagree and Commit*. The cure is short timeboxes and explicit review points, not better analysis.
- **The shopping list of features.** *Impact Mapping* names this anti-pattern directly: "Most planning activities revolve around juggling a 'shopping list of features,' as Gojko calls them. Even though the features are delivered, often the business objective is not achieved" (Source: Practice "Impact Mapping", "Why do it?"). The library's response: orient decisions to outcomes, not outputs.
- **Status-update standups.** *Daily Standup*: "Be careful it doesn't drift into a status update" (Source: Practice "Daily Standup", "How to do it?"). The standup's value as a decision-making artefact is alignment-and-blocker-surfacing; status reporting is a different artefact.
- **Treating an experiment outcome as success because it confirmed the hypothesis.** *Design of Experiments*: "Successful experiments are not experiments that have proven our assumption as correct. Successful experiments are those that provide valid and reliable data which shows a statistically significant conclusion" (Source: Practice "Design of Experiments", "How to do it?").
- **Skipping confidence voting before commitment.** A decision recorded but not confidence-checked leaves dissent latent; latent dissent surfaces during execution as foot-dragging.
- **Skipping the retrospective.** Decisions without retrospectives accumulate unresolved learning; the next decision uses the same false priors.
- **Picking practices without principles.** The library's most self-aware anti-pattern. *Establish Shared Principles*: "Blindly following practices are not encouraged" and "Copying just the practices of successful organizations will not get us the same result if we do not also adopt the values and principles that originated these practices" (Source: Practice "Establish Shared Principles", "Why do it?"). Decision-making practices imported without the principle they encode (e.g., "all voices are heard" behind 1-2-4-All) reproduce the shape but not the value.
- **Treating AI output as authoritative for high-stakes decisions.** *Human in the loop*: the library carries the IBM-1979 line — "A computer can never be held accountable, therefore a computer must never make a management decision" (Source: Practice "Human in the loop", "Why do it?"). Decision practices that delegate the *commit* step to an AI without a human review gate are an emerging anti-pattern named in the library.

## Worked Example

A cross-functional product team must decide which of five candidate features to invest in for the next quarter. The backlog is long; the team lead suspects the loudest voices are driving priority.

Phase 0 — framing: the team runs *Cynefin Framework* (Source: Practice "Cynefin Framework", "How to do it?") to place the decision in the Complicated domain — expert analysis is needed, but a single right answer exists. They note it is a prioritisation problem, not a yes/no choice (Source: Practice "Disagree and Commit", "Why do it?").

Phase 1 — frame: the team runs *Backcasting / Pre-mortem* (Source: Practice "Backcasting / Pre-mortem", "What is it?") to surface failure modes for each candidate, then *Start At The End* to name success assumptions.

Phase 2 — generate options: the facilitator uses *Silent Brainstorming* and *1-2-4-All* (Source: Practice "1-2-4-All", "Why do it?") to hear all voices before any discussion, explicitly blocking the HiPPO pattern.

Phase 3 — prioritise: the team runs *$100 Prioritisation* (Source: Practice "$100 Prioritisation", "Why do it?") combined with *Impact-Effort Matrix*. Two features that scored high on effort and low on impact are removed from contention.

Phase 4 — confidence check: *Confidence Voting* (Source: Practice "Confidence Voting", "How to do it?") is run before commitment. One engineer shows two fingers; the facilitator surfaces the concern — a technical dependency the group had missed. The team adjusts scope.

Phase 5 — commit and record: the team uses *Disagree and Commit* (Source: Practice "Disagree and Commit", "What is it?") with a named review point at six weeks. The decision is documented in an *Architectural Decision Record* (Source: Practice "Architectural Decision Records (ADR)", "Why do it?").

Phase 6 — review: at six weeks the retrospective uses *Rose, Thorn, Bud* to evaluate whether the prioritised feature delivered its predicted impact.

All framework citations trace through the deep reference.

## Integration with Other References

| Reference | Connection |
|---|---|
| NHS Just Culture Guide | OPL's *Blameless Postmortem* and the NHS Just Culture Guide are conceptually aligned: both treat the default response to an incident as system-level investigation rather than individual blame. The Just Culture Guide is the formal decision-tree for who-bears-accountability; OPL's *Blameless Postmortem* is the session-structure for the team-level conversation. Together they cover *who is the right locus of corrective action* (Just Culture) and *how do we run the conversation* (OPL). |
| US Forest Service LFUO/FLA/Learning Review Guide | OPL practices (Retrospectives, Blameless Postmortem, Disagree and Commit, Five Whys) are the general-purpose facilitation toolkit equivalent of the LFUO/FLA's more formal incident-learning protocol. The LFUO's three foundational principles (Just Culture, Systems Thinking, Learning) align with OPL's contrarian positions — blame-free, system-default, learning-oriented. OPL is the general library; LFUO is the high-consequence wildland-fire-domain operationalisation. |
| OpenStax, *Principles of Management* | OpenStax provides the *theoretical* decision-making content (programmed vs non-programmed decisions, six-step rational model, PDCA, Rest's ethical model); OPL provides the *practitioner* toolkit (named, time-boxed, group-facilitated practices that operationalise the theory). Read OpenStax for the model of the decision; read OPL for the named practice that executes the corresponding step. |
| OpenStax, *Organizational Behavior* | Groupthink and escalation of commitment are named OB phenomena that OPL practices are designed against. 1-2-4-All and Silent Brainstorming directly counter groupthink; Backcasting/Pre-mortem and Disagree and Commit counter escalation. Use OB to diagnose which group-decision pathology is in play; use OPL to pick the practice that counters it. |
| Scrum Guide 2020 | OPL's *Scrum* practice and the canonical Scrum Guide diverge on event count (OPL counts five events including the Sprint; the Guide counts the Sprint as a container with four nested events). For framework definition use the Scrum Guide; for practitioner facilitation of Scrum events use OPL practices (Iteration Planning, Daily Standup, Sprint Review/Showcase, Retrospectives). |
| Jones, *Evidence-Based Software Engineering* | Jones's argument that most software-engineering "theories" are folklore dovetails with OPL's *Design of Experiments* — both reject decision-by-prior and call for hypothesis-then-measurement. Use Jones for the case that prior literature is unreliable; use OPL for the structured practice that puts experiment-driven decision-making into a team's hands. |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The OPL library cites numerous external authorities within its practice pages; those cited by name but not held as primary references in this corpus include:

- *Taiichi Ohno* — cited as the originator of Five Whys (Practice "Five Whys (5 Whys)", "Why do it?") [BT]. Not held as a primary reference.
- *Paulo Caroli / Lean Inception* — cited as the originator of *Is – Is not – Does – Does not* (Practice "Is – Is not – Does – Does not", "What is it?") [BT].
- *David J. Anderson / Kanban* — cited as the origin of the *Theory of Constraints* connection in several workflow-management practices [BT].
- *L. David Marquet, Leadership is Language* — cited as the origin of *Dissent Cards* (Practice "Dissent Cards") [BT].
- *Jean Tabaka, Collaboration Explained* — cited as the originator of Confidence Voting's 0–5 finger scale (Practice "Confidence Voting", "How to do it?") [BT].
- *Dave Snowden / Cynefin Framework* — cited approvingly throughout; not held as a primary reference separate from OPL's representation [BT].
- *Gary Klein* — cited in the *Backcasting / Pre-mortem* practice for the pre-mortem technique [BT].
- *Simon Sinek* — cited in *Start With Why* (Practice "Start With Why", "What is it?") [BT].
- *Gojko Adzic* — cited in *Impact Mapping* for the term and concept (Practice "Impact Mapping", "What is it?") [BT].

The integration-with-other-references section makes claims about how OPL practices and other corpus sources pair; those are distillation-level synthesis, not OPL's own claims, and are identified as such in that section.

**Named limits of the source.** OPL is a community-curated catalogue of named facilitation and delivery practices; it is not a decision theory text. It does not provide quantitative decision methods (NPV, expected value, option pricing), legal or regulatory frameworks, domain-specific standards, or a structural account of why the practices work beyond the community rationale each practice carries. The library is open to community additions and revisions; the deep reference reflects the state of the cloned commit (`8bfa450e75dfba1e2a3c68ac0e514e587f6f116e`, 2026-05-13) and does not speak to content added after that date.

**Evidence-marker continuity.** This distillation paraphrases throughout; verbatim passages live in the deep reference (`open-practice-library-deep.md`). Key Concept citations use `(Source: Practice "[Name]", "[Section]")` anchors that map directly to the deep ref's `[V]` extracts. The anti-patterns section derives from explicit OPL body text formulations (marked `[V]` in the deep ref) and is not imported from outside the source.
