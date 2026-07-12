# Letaw, Handbook of Software Engineering Methods — Decision-Making Distillation

**Source:** Letaw, L. (2024). *Handbook of Software Engineering Methods* (2nd ed.). Oregon State University. CC BY-NC 4.0. https://open.oregonstate.education/setextbook/.

## Decision-Making Relevance

Letaw's *Handbook* presents software-engineering methods as risk-reduction tools — each method is repeatedly justified by what kind of decision it improves or what kind of negative outcome it averts. The book's working definition of *risk* (the estimated probability of a loss given known and unknown factors) reframes most engineering work as decision-making under uncertainty.

Five concrete decision frames recur. The **triple constraint** (time, cost, scope) forces every project decision to be a trade-off where loosening one constraint demands tightening another. The **project priority matrix** (Constrain / Enhance / Accept) makes those trade-offs explicit at project start, with the client, before pressure forces them implicitly. The **Eisenhower matrix** (urgent × important → Do / Decide / Delegate / Delete) is a first-pass task-prioritisation grid. **Fist of five** is a six-level group consensus method that catches latent dissent before commitment. **Spike** is a deliberate investigation method for choosing between development paths when the team lacks the information to estimate, prioritise, or design.

Beyond these explicit decision tools, the book offers structured decision frames for *requirements* (functional vs nonfunctional; quality attribute vs constraint; INVEST as a user-story quality check), for *architecture* (monolith vs microservices, with six structured comparisons), for *prototype fidelity* (low/medium/high — each appropriate for a different feedback-cost level), for *UML use* (five benefits weighed against three drawbacks), and for *code maintenance* (twelve named code smells, each with a refactoring prescription). The Inclusivity Heuristics give a per-decision lens for UI design choices: each design decision is interrogated through Abi, Pat, and Tim, the three personas with distinct cognitive styles.

This distillation gathers these decision frames into a working pattern: how to bound the decision space at project start; how to prioritise tasks within that space; how to make architecture, design, and code-maintenance decisions with the right cost-of-being-wrong; and how to surface latent disagreement before it becomes irreversible commitment.

## Key Concepts for Decision-Making

1.  **The triple constraint as forced trade-off.** Every project decision sits inside time × cost × scope. Adjusting one constraint requires a corresponding change in at least one other; the project priority matrix names which constraint to Constrain (fixed, can improve but not worsen), Enhance (try to improve), or Accept (can worsen if needed). Decided once with the client at project start, the matrix becomes the referent for downstream trade-off calls. (Source: Letaw, *Handbook*, Ch 2.2, "Triple Constraint"; Ch 2.5.2, "Balancing Constraints: Project Priority Matrix")

2.  **Risk as the through-line.** *Risk* is the estimated probability of a loss given known and unknown factors; *risk mitigation* is an action taken to avoid a contingency. Each method in the book is presented as a way to reduce risk: defining and tracking the project, communicating with the team, researching the implications of decisions, developing backup plans, and selecting suitable tools. A decision that doesn't name its risk exposure is poorly bounded. (Source: Ch 2, opening; Glossary)

3.  **Eisenhower matrix for task prioritisation.** A 2×2 of urgent × important: **Do** (urgent + important, "Needs to be done correctly and now"); **Decide** (not urgent + important, "Needs to be done correctly but not immediately"); **Delegate** (urgent + not important, "Needs to be done now, but mistakes can be absorbed"); **Delete** (neither, "Doesn't need to be done correctly or any time soon. Can be eliminated") [V] (Source: Letaw, *Handbook of Software Engineering Methods*, Ch 2.5.3, "Task Prioritization: Eisenhower Matrix"). First-pass prioritisation reduces risk by conserving and thoughtfully using resources and breaks out of the urgent-only "putting out fires" failure mode.

4.  **Programmed vs spike-warranted decisions.** When a task has knowns and the path is clear, estimate and commit. When the task has unknowns — risk, dependencies, "many unknowns" — run a **Spike**: ask a question, try to answer it by reading and experimenting, repeat until enough information. A spike is the structured response to "we don't yet know enough to decide." (Source: Ch 1.2.3, "Agile Methods"; Ch 2.5.4, "Finer-Grained Prioritization")

5.  **Fist of five for consensus.** Six-level voting (None=strong reject, blocks; One=reject, major issues; Two=weak reject, minor issues; Three=weak accept; Four=accept; Five=strong accept, willing to lead). Two-or-fewer triggers explicit discussion before commitment. The mechanism reduces risk by (1) surfacing latent dissent and (2) increasing team motivation, ownership, and investment. (Source: Ch 2.4.3)

6.  **RACI for decision rights.** Decisions about who decides, executes, advises, and observes are themselves load-bearing. RACI (Responsible / Accountable / Consulted / Informed) makes those roles explicit per task or deliverable. A team that doesn't know who needs to do what increases the probability of negative events and outcomes — "shipping a broken product to customers because nobody was assigned to quality assurance" [V] is the canonical example. (Source: Letaw, *Handbook of Software Engineering Methods*, Ch 2.4.2, "Defining Roles and Responsibilities: RACI Matrix")

7.  **Estimation under uncertainty: story points and ideal days.** Story points compare task size to other tasks; ideal days estimate focused work time. Either way, the estimate is an artefact of the decision to commit, not a prediction. **Planning poker** runs estimation as team consensus: privately decide, simultaneously reveal, discuss differences, re-estimate until convergence. The discussion is the value, not the number. (Source: Ch 2.5.5)

8.  **Architecture decision: monolith vs microservices.** Six structured comparisons make the decision tractable: communication (direct calls vs network with smart endpoints), deployment (all-at-once vs independent), scaling (whole-monolith copies vs selective service replication), testing (slow broad dependencies vs independent service tests), upgrading (atomic vs language/runtime-independent), and database (shared bottleneck vs per-service stores with eventual consistency). The ODOT TOCS case study illustrates the migration triggers — tight coupling, deploy-frequency limits, database contention, platform deprecation — that warrant the change. (Source: Ch 5.3; Ch 5.5)

9.  **Prototype fidelity as feedback-cost decision.** Low fidelity for high-level feature feedback (cheap to change); medium fidelity for small changes to accepted features; high fidelity for detailed tweaks. Choosing too high a fidelity for the question being asked wastes effort if the underlying decision changes. "If your client doesn't like your design, you might have saved time and communicated your concept just as well with a less elaborate paper prototype" [V] (Source: Letaw, *Handbook of Software Engineering Methods*, Ch 6.1, "Showing Interaction").

10.  **Inclusivity Heuristics as decision lens for UI choices.** Eight heuristics applied during heuristic evaluation by multiple independent evaluators, with three personas (Abi, Pat, Tim) reflecting distinct combinations of five cognitive facets (attitude toward risk, computer self-efficacy, information processing style, learning style, motivations). Each UI design decision is interrogated through the personas: does the design support task-motivated users with limited time as well as tech-motivated tinkerers? (Source: Ch 7)

11.  **Code-maintenance decisions: twelve named smells.** Comment smells (Obsolete, Commented-Out, Redundant, Long), function smells (Long Function, Function with Many Jobs, Function with Many Parameters), and general code smells (Duplicate Code, Long Lines, Inconsistent Conventions, Vague Naming). Each carries a refactoring prescription. Refactoring is "improving code without changing what it does" and is the structured response to technical debt — the cost of decisions deferred. (Source: Ch 8.3–8.5)

12.  **Build the requirements before deciding implementation.** Functional requirements describe what the software does; nonfunctional requirements describe how well or under what constraints. Without explicit requirements, developers prioritise what they personally find important or fun, multiple developers can implement conflicting code, stakeholders drift the project toward their fleeting wants. The decision to specify is itself a risk-reduction decision. (Source: Ch 3.2)

## Questions to Ask During Decision-Making

### Phase 1: Framing (Recognising the decision and gathering context)

| Need | Question |
|---|---|
| Name the risk | What is the estimated probability of a loss here, given known and unknown factors? Can it be stated as high/medium/low or numerically? |
| Position within the triple constraint | Which of time, cost, and scope is this decision actually about? Have we declared which constraint is Constrained, which is Enhanced, and which is Accepted on this project? |
| Test urgency vs importance | Is this in the Do, Decide, Delegate, or Delete quadrant of the Eisenhower matrix? Is the urgency real or self-imposed? |
| Decide whether to spike | Does the team have enough information to estimate and prioritise this task, or do we need a focused investigation (Spike) to gather information first? |
| Surface whose call it is | Who is Responsible, Accountable, Consulted, and Informed for this decision? If those roles aren't clear, is naming them the right first step? |
| Detect when defaults are deciding for us | Has this become a monolith / decision-by-accretion / never-refactored choice rather than an actively-made decision? What architectural or process default is silently in play? |

### Phase 2: Bounding (Defining the decision and its constraints)

| Need | Question |
|---|---|
| Make the trade-off space explicit | What is being given up to enable this decision? Which constraint loosens, and which tightens? |
| Specify acceptance criteria | What must be true for this decision to be considered "done well"? In user-story terms, what is the Definition of Done? |
| Quantify nonfunctional thresholds | If this decision affects software performance or behaviour, what is the testable threshold (e.g., response time under N seconds, uptime ≥ 99.X%)? |
| Identify constraints we don't control | What constraints are externally mandated (platform, regulation, data residency) versus internally chosen (quality attributes)? |
| Apply INVEST if the decision is feature-level | Is the work item Independent (no unnecessary dependencies/overlap), Negotiable, Valuable, Estimable, Small (fits a Sprint), Testable? |

### Phase 3: Exploring (Generating alternatives)

| Need | Question |
|---|---|
| Generate enough alternatives | For an architecture or design decision, have we surfaced more than two options? For UML diagrams, more than one approach to communicating the design? |
| Use the six monolith-vs-microservice comparisons | When the decision is architectural: how does each option play out on communication, deployment, scaling, testing, upgrading, and database? |
| Consider fidelity-appropriate prototypes | If we're testing a design decision, which fidelity is right for the question being asked? Are we over-investing in polish before the underlying concept is validated? |
| Apply the Inclusivity Heuristics if UI is involved | How does this design choice land for each of Abi, Pat, and Tim? Are familiar features still available? Is undo/redo possible? Is there an explicit path for process-oriented users alongside freedom for tinkerers? |
| Surface dependencies | What other tasks or decisions depend on this one? What's waiting on it? |

### Phase 4: Deciding (Analysing and selecting)

| Need | Question |
|---|---|
| Run a fist of five before commitment | If this is a team-level decision, where does each member sit on the six-level scale? Is anyone at two-or-fewer fingers? If so, discuss before committing. |
| Estimate via planning poker for sized work | If the decision is to commit to a unit of work, have we run planning poker (private estimate → reveal → discuss → re-estimate until convergence)? |
| Apply the right method for the decision type | Is this a recurring decision (use a heuristic / template) or a novel one (use the structured method)? In Agile terms: programmed task or spike-warranted? |
| Check that requirements drove the decision | If this is an implementation or design decision, did it follow from requirements, or did we pick what felt important to the developer? |
| Communicate at appropriate fidelity for the audience | If presenting the decision via UML or diagrams: will the intended audience understand at this level of detail? Is the diagram communicating, or just satisfying convention? |

### Phase 5: Ratifying (Implementing the decision)

| Need | Question |
|---|---|
| Lock the RACI assignments | Now that the decision is made, who is Responsible, Accountable, Consulted, and Informed for execution? |
| Set Definition of Done | What set of acceptance criteria, when satisfied, will mark this work item DONE-done? |
| Pre-commit against scope creep | Now that scope, cost, and time positions are set in the project priority matrix, what response do we pre-commit to when a new feature request arrives? |
| Communicate the decision, not just the outcome | Have we made the reasoning visible to those affected, including those who weren't in the decision-room? |
| Schedule with explicit dependencies | If the decision implies multiple tasks, have we built a project network diagram (or equivalent) so predecessors are visible? |

### Phase 6: Monitoring (Was the decision a good one?)

| Need | Question |
|---|---|
| Compare actual to estimated | If we estimated in story points or ideal days, what did the work actually take? What does the variance imply for future estimates (velocity adjustment)? |
| Watch for code smells accumulating | Are the smells the team is introducing post-decision (Long Function, Duplicate Code, Inconsistent Conventions) signalling that the architectural decision was wrong, or that we're under-refactoring under deadline pressure? |
| Look for cross-service / cross-component drift | If the decision was for microservices, are we maintaining decentralised data management and decentralised governance — or are services slowly coupling back? |
| Detect technical-debt accumulation | Are we deferring refactoring as a normal practice? "Smelly code leads to smellier code" — is the rate of decay accelerating? |
| Revisit the project priority matrix when context changes | If a client changes Scope from Constrained to Accept (or vice versa), have we acknowledged the trade-off explicitly and re-priced the rest of the work? |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| Project decisions about time, cost, or scope are being made implicitly and reactively | The triple constraint is operating but the project priority matrix has not been agreed with the client (Source: Ch 2.2, "Triple Constraint"; Ch 2.5.2, "Balancing Constraints: Project Priority Matrix") | Draw the matrix explicitly with the client before the next scope-change request arrives; name which constraint is Constrained, which Enhanced, which Accepted |
| Team commits to a unit of work without a fist-of-five check and dissent surfaces after implementation begins | Latent dissent not surfaced — the consensus-measurement step was skipped (Source: Ch 2.4.3, "Measuring and Building Consensus: Fist of Five Method") | Run fist of five before any significant team-level commitment; anyone at two or fewer fingers triggers a discussion before commitment |
| Estimation is done by the most senior developer or project lead alone | Planning-poker value is being forfeited — the discussion is the value, not the number (Source: Ch 2.5.5) | Switch to planning poker: privately decide, simultaneously reveal, discuss differences, re-estimate until convergence |
| Architecture choice (monolith vs microservices) was made by convention or by what the team already knows | Appropriateness check was skipped — the six structured comparisons (communication, deployment, scaling, testing, upgrading, database) were not run (Source: Ch 5.3) | Run the six comparisons explicitly; surface which dimensions matter most for the project; document the trade-off reasoning |
| A task is unknown enough that estimation is unreliable but the team commits anyway | Spike-warranted but skipped — the path has enough unknowns that the team cannot reliably estimate or prioritise (Source: Ch 1.2.3, "Agile Methods") | Define the spike question; timebox the investigation; commit only after the unknown is resolved |
| A UI design decision treats one user type's preferences as universal | Inclusivity-heuristics step skipped — the three personas with distinct cognitive facets were not walked through the design (Source: Ch 7) | Apply the eight heuristics through Abi, Pat, and Tim; surface where the design serves one cognitive style and blocks another |

## When to Use This Reference

- A software project's triple constraint trade-offs are implicit — the project priority matrix needs to be drawn explicitly with the client.
- A team is defaulting to one architecture (monolith or microservices) without running the six-comparison decision.
- A design or UI decision needs an inclusivity-aware lens — the eight heuristics applied through the three personas.
- A requirements-vs-implementation tension is suspected (developers prioritising what's fun to build, scope drifting toward stakeholder whims) — the requirements chapter and INVEST framing apply.
- A team-level decision is being committed without surfacing latent dissent — fist of five before commitment.
- Estimation needs to become a team conversation rather than a one-person guess — planning poker with story points or ideal days.
- A task list needs first-pass prioritisation — Eisenhower matrix on urgent × important.
- A development path is unclear and the team is at risk of committing to a wrong direction — spike before estimating.
- Code quality is decaying and the team needs a vocabulary for refactoring decisions — the twelve named code smells.
- A role ambiguity is blocking decisions — RACI matrix to clarify Responsible / Accountable / Consulted / Informed.
- The book deliberately stays method-level and does not cover specific technology choices, detailed Agile vs Waterfall comparative analysis, ethics, security, or quantitative cost models; reach for Jones, *Evidence-based Software Engineering*, for evidence-calibrated views on Agile practice claims.

## Worked Example

A four-person development team is starting a new web application for a regional nonprofit. At kickoff, the project manager runs the project priority matrix with the client (Source: Ch 2.5.2, "Balancing Constraints: Project Priority Matrix"): Scope is Constrained (the MVP feature list is fixed), Time is Enhanced (deliver in 12 weeks), Cost is Accepted (budget can flex slightly if scope is met). This sets the referent for all downstream trade-offs.

In Week 1, the team identifies an authentication module as a high-risk unknown — the lead developer has never integrated the client's legacy SSO system. Rather than estimating and committing, the team runs a spike (Source: Ch 1.2.3, "Agile Methods"): two days, one developer, answering the question "Can we integrate this SSO with our stack?" The spike resolves the unknown; the subsequent planning-poker estimation converges in one round.

In Week 4, a UI design decision about the dashboard layout is proposed. Before committing, the designer walks the design through Abi, Pat, and Tim (Source: Ch 7). The Tim persona — tech-motivated, comfortable tinkering — is well served by an expert shortcut menu. The Abi persona — task-motivated, low computer self-efficacy — is blocked: the shortcut menu replaces the explicit guided-path UI she relies on. The designer adds a visible "guided mode" toggle rather than removing the shortcut menu.

Before the Week 6 scope-change request (the client wants to add a reporting module), the project manager returns to the project priority matrix: Scope is Constrained; the request requires loosening the constraint, which means a corresponding tightening of Time (push to 14 weeks) or Cost (add budget). The trade-off is named and agreed rather than absorbed silently. All framework citations trace back through the deep reference.

## Integration with Other References

| Reference | How it pairs with Letaw |
|---|---|
| **OpenStax, *Organizational Behavior*** (Ch 6) | Provides the general six-step decision process, programmed vs non-programmed decisions, and bounded-rationality barriers. Letaw operationalises the same concepts for software projects: spike ≈ non-programmed decision response; Eisenhower matrix ≈ task-triage under urgency pressure. |
| **OpenStax, *Principles of Management*** (Ch 17–18) | Provides the strategic planning and control-cycle frame (PDCA, MBO, balanced scorecard) within which Letaw's project-level methods sit. Management for the organisational level; Letaw for the team level. |
| **Jones, *Evidence-based Software Engineering*** | Jones calibrates which Agile practice claims are evidence-based and which are folklore. Use Letaw for how to run the practices; use Jones to know which outcome claims for those practices are supported by data. |
| **OpenStax, *Principles of Marketing*** (Ch 11) | The Gap Model of Service Quality complements Letaw's Inclusivity Heuristics — both treat user/customer experience as the load-bearing measure of design success. |
| **Gagné, *Field Guide to Scrum Events*** | The Field Guide operationalises the Scrum events that Letaw uses as context for planning poker, story points, spikes, and the Sprint Backlog. Letaw for the methods themselves; Field Guide for how to facilitate the events where those methods are used. |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The deep reference contains the following `[BT]` citations — passages where the handbook cites named third parties not held as separate primary references in this corpus:

- *Agile Manifesto (Beck et al. 2001)* — not held as a standalone reference. Grounding document for the Agile philosophy in Ch 1.
- *Schwaber & Sutherland (2020), Scrum Guide* — held as a primary reference in this corpus (`scrum-guide-2020`). Cited in Ch 1.2.2 for Scrum team, events, and artifacts definitions.
- *Cohn (2006), Agile Estimating and Planning* — not held. Primary source for story points and planning poker definitions (Ch 2.5.5).
- *Tuckman (1965); Tuckman & Jensen (1977)* — not held. Source of the five-stage team-development model cited for team communication context.
- *Wiegers & Beatty (2013), Software Requirements* — not held. Primary source for functional / nonfunctional / quality-attribute / constraint definitions (Ch 3).
- *Wake (2003), "Invest in good stories"* — not held. Source of the INVEST acronym for good user stories (Ch 3.6.1).
- *Lewis & Fowler (2014), Microservices; Fowler (2015)* — not held. Organising frame for the six structured monolith-vs-microservices comparisons (Ch 5). Chapter subheadings are borrowed from Lewis & Fowler.
- *Burnett et al. (2016, 2021), GenderMag Project* — not held. Primary source for the Inclusivity Heuristics, the five cognitive facets, and the three personas (Ch 7).
- *Martin (2009), Clean Code* — not held. Source for the technical-debt narrative in Ch 8.
- *Fowler & Beck (2019), Refactoring* — not held. Cited for further refactoring guidance beyond the twelve named smells.
- *ISO/IEC/IEEE 24765:2017* — not held. Source of the software-engineering definition used throughout.
- *CHAOS Report (Standish Group, 2015)* — not held. Cited for project-failure rates (17–22% of projects failing, 2011–2015).

**Named limits of the source.** The handbook explicitly stays method-level: no specific technology choices (Python vs Java, AWS vs Azure), no detailed Agile-vs-Waterfall comparative analysis (the book is Agile-biased by design), no quantitative cost models (risk is treated qualitatively), no ethics or security coverage beyond cognitive-style inclusivity.

**Evidence-marker continuity.** This distillation paraphrases throughout; verbatim passages live in the deep reference (`letaw-handbook-sweng-methods-deep.md`). Key `[V]` passages that this distillation paraphrases — including the triple-constraint definition (Ch 2.2), the RACI shipping-failure example (Ch 2.4.2), the fist-of-five encoding (Ch 2.4.3), the spike definition (Ch 1.2.3), and the develop-vs-grade prototype-fidelity rule (Ch 6) — are cited by chapter and section name in the Key Concepts section above.
