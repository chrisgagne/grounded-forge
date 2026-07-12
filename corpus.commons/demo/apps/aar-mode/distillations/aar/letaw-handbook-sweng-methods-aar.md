# Letaw, Handbook of Software Engineering Methods, AAR Distillation

**Source:** Letaw, L. (2024). *Handbook of Software Engineering Methods* (2nd ed.). Oregon State University. Licence: CC BY-NC 4.0 (non-commercial; copyleft propagates to NC derivatives). Scope: open-nc.

## AAR Relevance

The Handbook projects onto the software-incident AAR as a *practitioner toolkit*: it names methods, not theories, and each method is framed as a risk-reduction move. (Source: Letaw, *Handbook of Software Engineering Methods*, Ch 2, opening) For the AAR facilitator, three methods dominate: the RACI matrix for locating decision-rights ambiguity as a contributory factor, fist of five for surfacing latent dissent before an action is committed, and the twelve named code smells as a shared vocabulary for design-debt contributors when an incident's root theme involves code decay. A fourth cluster — the Tuckman stage map, the triple constraint, and the project priority matrix — applies when an AAR surfaces team-dynamics or project-governance contributory factors. The projection is moderate fire: most valuable at Phase 2 (contributory-factor analysis with RACI and code smells) and Phase 4 (action design with fist of five and RACI for ownership).

## Key Concepts for AAR

1.  **RACI matrix as decision-rights audit.** The RACI matrix defines "who is Responsible (R), Accountable (A), Consulted (C), or Informed (I)" for each task or deliverable. The risk it addresses directly: "If your team doesn't know who needs to do what (or forgets, or can plausibly deny knowing), that can increase the probability of negative events" — the example is "shipping a broken product to customers because nobody was assigned to quality assurance" [V] (Source: Letaw, *Handbook*, Ch 2.4.2, "Defining Roles and Responsibilities: RACI Matrix") During an AAR, building the RACI for the moment of failure often reveals that the R and A cells were empty or doubled.

2.  **Fist of five for surfacing latent dissent before action commit.** The encoding: none (strong reject / blocks consensus) through five fingers (strong accept, willing to lead). A two-or-fewer response blocks progress and opens a conversation. The method "can reduce risk by (1) bringing problems to light and (2) increasing team motivation, ownership, and investment" [V] (Source: Ch 2.4.3, "Measuring and Building Consensus: Fist of Five Method") At action-design phase: run fist of five before finalising any action whose implementation will require sustained commitment.

3.  **Twelve named code smells as design-debt vocabulary.** Code smells are "indications that the code needs to be reorganized — a sign your software is undergoing code decay" [V] (Source: Ch 8, opening) Four families: comments (Obsolete Comment, Commented-Out Code, Redundant Comment, Long Comment); functions (Long Function, Function with Many Jobs, Function with Many Parameters); code in general (Duplicate Code, Long Lines, Inconsistent Conventions, Vague Naming). Each carries a prescription.

4.  **Code decay is self-reinforcing.** "Smelly code leads to smellier code" — letting code become disorganised signals to developers that disorganised code is acceptable. [V] (Source: Ch 8.1, "Why Care about Code Smells?") If the AAR surfaces that code smells were present before the incident, the question is when the decay began and what kept normalising it.

5.  **Tuckman stage map for group dynamics during the AAR.** The five stages — Forming, Storming, Norming, Performing, Adjourning — describe where a team is in its development. (Source: Ch 2.4, citing Tuckman 1965, borrowed-through) Teams in Storming "resist group influence, peers, peers' ideas, and tasks" — which shapes how contributory factors naming peer decisions will land.

6.  **Triple constraint as contributory-factor frame.** Time, Cost, and Scope are the three constraints; changing one requires a corresponding change in at least one other. (Source: Ch 2.2, "Triple Constraint") When a project-level incident surfaces, the triple constraint often reveals which constraint was held fixed while another was accepted as sacrificeable.

7.  **Project priority matrix for named trade-offs.** Each constraint is tagged Constrain / Enhance / Accept. (Source: Ch 2.5.2, "Balancing Constraints: Project Priority Matrix") When the AAR reconstructs the pre-incident decision environment, building the implicit project priority matrix — as the team actually understood it at the time — reveals the hidden trade-offs that local rationality was navigating.

8.  **INVEST criteria for action quality.** The INVEST acronym (Independent, Negotiable, Valuable, Estimable, Small, Testable) is native to user stories but scales to AAR-action quality assessment: an action that is not Estimable, not Testable, or not Small enough to fit in one iteration is unlikely to survive past the AAR meeting. (Source: Ch 3.6.1, citing Wake 2003, borrowed-through)

9.  **Agile-adoption evidence.** Of 601 surveyed organisations, 51% leaned toward Agile and only 2% used pure Waterfall. (Source: Ch 1.2, citing Hewlett Packard Enterprise 2017, borrowed-through) When an AAR surfaces process-method friction as a contributory factor — teams caught between Waterfall contract commitments and Agile team practice — this data gives the facilitator a baseline.

10.  **Microservices: design for failure is a posture, not a feature.** With microservices, "thinking can shift toward service-specific monitoring, logging, and design decisions about what to do when a service fails" [V] (Source: Ch 5.2.6) When an incident involved an architectural boundary — monolith vs microservices — the mismatch between the architecture's failure posture and the team's incident-response design is a legitimate contributory factor.

11.  **Ground rules as a precondition for honest accounts.** Effective ground rules "need buy-in from the whole team"; rules that feel "silly, phony, too aspirational, too inflexible, or too authoritative" invalidate the exercise. [V] (Source: Ch 2.4.1) This applies directly to the AAR spirit-and-climate step: if the ground rules for the AAR are experienced as performative rather than genuine, participant accounts will be defensive rather than honest.

12.  **Managerial skill mix mismatch as a contributory factor.** The three categories — Interpersonal, Technical, Administrative and conceptual — shift in importance at different levels. (Source: Ch 2.3, citing Badawy 1995, borrowed-through) When an AAR surfaces a decision made at the wrong level of the hierarchy, the skill-mix mismatch at that level is a structural contributory factor.

## Questions to Ask During AAR

### Phase 2: Contributory-factor analysis

| Need | Question |
|---|---|
| Decision ownership is contested | Build the RACI for the decision at the moment of failure. Where were the R and A cells empty, doubled, or contested? |
| Code was involved in the incident | Which of the twelve named code smells were present in the code that failed? How long had they been present, and what normalised their presence? |
| Team was newly formed or in conflict | Where is this team on the Tuckman map? If Storming, which group-resistance patterns shaped how information was shared or withheld before the incident? |
| Project constraints were in tension | What was the implicit project priority matrix at the time of the incident — what was Constrained, Enhance, and Accepted? Did the whole team share this understanding? |
| Architectural boundary crossed | Did the incident involve a monolith-microservices boundary? Was the architecture's failure posture matched to the incident-response plan? |

### Phase 3: Just-culture sorting

| Need | Question |
|---|---|
| Accountability is contested | Before reaching the NHS five-test tree, has a RACI been built for the relevant task? Who was Accountable (A) on the matrix at the time? |
| Individual is named as solely responsible | Did the ground rules for the AAR produce genuine psychological safety, or did performative rules suppress the accounts needed to surface shared responsibility? |

### Phase 4: Action design

| Need | Question |
|---|---|
| Action ownership is ambiguous | Build a RACI for each action before adjourning; the Accountable cell must be a named individual, not a team or role. |
| Dissent is present but unstated | Run fist of five before committing each action. A two-or-fewer response blocks; open the conversation rather than overriding it. |
| Action targets code quality | Which of the twelve code smells does the action address? Does the action name both the smell and the refactoring prescription, so success is testable? |
| Action is too large to complete before next review | Apply INVEST: is the action Small enough to fit in one iteration? Is it Testable — can someone verify it is done without ambiguity? |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| An action is assigned to "the team" or "engineering" with no named individual | RACI gap: the Accountable cell is empty, the action will not happen | Require a named individual in the Accountable cell before the action is logged |
| Code quality is named as a factor but the vocabulary stays vague ("messy", "complex") | Code-smell vocabulary is absent — the factor cannot be tracked or remediated without precision | Ask: which of the twelve named smells were present? Name each one and its prescription |
| A fist-of-five vote is taken verbally and everyone says "fine" | Verbal simultaneous reveal is impossible — social pressure has overridden honest signals | Require written or physical simultaneous reveal before any verbal discussion |
| The AAR is running after a team that recently went through a major restructuring | Tuckman regression: the team may have dropped from Performing to Forming or Storming | Acknowledge the regression explicitly; adjust facilitation expectations accordingly |
| A project commitment is described as "the only option" at the time | Implicit project priority matrix was Constrained on one dimension at the expense of the others without the team explicitly agreeing | Reconstruct the implicit matrix as it was understood at the time |

## When to Use This Reference

Reach for this source when:
- The incident involved software code and the contributory-factor analysis needs precise vocabulary for what kind of code quality problem was present.
- Decision ownership is contested and the RACI has not been built.
- An action is being proposed but no one is checking whether it is INVEST-compliant.
- Latent dissent on an action is suspected but unvoiced — fist of five is the structural mechanism.
- The AAR involves a team in Storming and the facilitator needs a frame for why peer accounts are being resisted.

Do not reach for this source as the primary AAR protocol or the just-culture sorting tool — TC 25-20, LFUO, and NHS carry those. This source is the practitioner-methods layer for software-incident-specific contributory factors.

## Worked Example

A team is reviewing an incident where a hotfix deployment failed because no one knew who owned the deployment checklist review step. The facilitator builds a RACI for the deployment process as it existed at the time of the incident: the Responsible cell has two engineers, the Accountable cell is empty, the Consulted cell lists the team lead (who was on leave), and the Informed cell is empty. (Source: Letaw, *Handbook of Software Engineering Methods*, Ch 2.4.2, "Defining Roles and Responsibilities: RACI Matrix".) The contributory factor is named precisely: empty Accountable cell on the deployment checklist review, normalised by the team lead's consistent availability before the incident. In Phase 4, the proposed action is to add a deployment checklist sign-off step. Before committing, the facilitator runs fist of five (Ch 2.4.3): two engineers show two fingers — not a block, but enough to open a conversation. The two concerns surface: the checklist adds latency to hotfix cycles, and the current environment makes the checklist unworkable without tool changes. The action is refined to a tool-integrated automated check rather than a manual step. The INVEST test (Ch 3.6.1) is applied: the automated check is Small (one iteration), Testable (pipeline CI shows green/red), and Estimable (a named engineer estimates it at two days). The revised action is committed with a named owner and a named date.

## Anti-patterns This Reference Helps Avoid

- Closing an AAR action item with "team responsible" or "engineering responsible" rather than a named Accountable (A) individual.
- Naming code quality as a contributory factor without a shared vocabulary for which smells were present and how they compounded.
- Running a fist-of-five-style check verbally, which allows social pressure to override honest signals.
- Treating team conflict during the AAR as personality friction rather than as a Tuckman-stage dynamic.
- Framing project-level trade-offs as post-hoc surprises without reconstructing the implicit project priority matrix participants were navigating before the incident.
- Designing actions that are not Testable or not Small — actions without a clear done-condition will not survive to next review.
- Skipping the AAR's spirit-and-climate step, then concluding that accounts were honest.

## Integration with Other References

| Reference | Relationship |
|---|---|
| Jones Evidence-Based Software Engineering (jones-evidence-based-sweng) | Jones provides the empirical corrective for the beliefs underlying the methods this source names; when the incident involves metric targets or productivity assumptions, Jones is the companion — this source names the method, Jones names whether the belief backing it has empirical support |
| NHS Just Culture Guide (nhs-just-culture-guide) | NHS provides the five-test decision tree for individual-vs-system accountability; this source provides the RACI that the NHS test needs as input — the Accountable cell in the RACI answers NHS Q3's "did the individual knowingly depart from an agreed protocol?" |
| TC 25-20 (tc-25-20-army-aar) | TC 25-20 provides the protocol structure; this source provides the software-specific decision-rights and code-quality vocabulary for Phase 2 analysis |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The Tuckman stage model (Tuckman 1965; Tuckman & Jensen 1977) is cited borrowed-through in the source (Ch 2.4); Tuckman is not held directly in this corpus. The INVEST acronym (Wake 2003) is cited borrowed-through (Ch 3.6.1); Wake is not held directly. The Hewlett Packard Enterprise 2017 Agile-adoption survey is cited borrowed-through (Ch 1.2); the survey is not held directly. The Badawy 1995 managerial skill-mix framework is cited borrowed-through (Ch 2.3); Badawy is not held directly. The triple constraint framing (van Wyngaard et al. 2012) is cited borrowed-through (Ch 2.2); van Wyngaard is not held directly.

**Named limits of the source.** The Handbook is "geared toward Agile software development" by design; the author endorses Agile explicitly and the method coverage reflects that bias. The source does not address incident review methodology, just-culture sorting, or facilitation protocol. The code-smells catalogue is a named set of twelve; the author does not claim it is exhaustive, and the literature contains additional named smells outside this set. The RACI matrix is presented as a team-design tool rather than an incident-analysis tool; adaptation to post-incident RACI reconstruction is operator-applied.

**Evidence-marker continuity.** The RACI risk quotation is `[V]` in the deep ref; the distillation quotes it in Concept 1 with the `[V]` marker. The fist-of-five risk-reduction quotation is `[V]` in the deep ref; the distillation preserves it in Concept 2. The code-smells definition quotation is `[V]` in the deep ref; the distillation preserves it in Concept 3. The Tuckman model is `[AP]` in the deep ref with `[BT]` to Tuckman 1965; the distillation preserves the borrowed-through flag in Concept 5 and in this section.
