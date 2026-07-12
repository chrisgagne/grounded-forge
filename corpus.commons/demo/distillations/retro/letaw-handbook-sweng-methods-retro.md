# Letaw, Handbook of Software Engineering Methods, Retro Distillation

**Source:** Letaw, L. (2024). *Handbook of Software Engineering Methods* (2nd ed.). Oregon State University. Licence: CC BY-NC 4.0 (non-commercial; copyleft propagates to NC derivatives). Scope: open-nc.

## Retro Relevance

The Handbook projects onto the retrospective as a *structured-method toolkit*: every method Letaw presents is framed as a risk-reduction move [V] (Ch 2, opening), and the retro is precisely the moment when the team decides which risks to act on. Three methods carry the most weight: fist of five for surfacing latent dissent before an experiment is committed, the RACI matrix for resolving ambiguous ownership when an experiment has no clear accountable individual, and the INVEST criteria for assessing whether a proposed experiment is well-formed. A second cluster — the twelve code smells, the Inclusivity Heuristics, planning poker — applies when the retro's content surfaces code quality, UI-related friction, or estimation discipline. The projection is strong fire at Phase 4 (experiment design, where fist of five, RACI, and INVEST all apply) and moderate fire at Phase 2 (data gathering, where planning poker and code smells surface) and Phase 3 (insight, where RACI maps contributory-factor ownership).

## Key Concepts for Retro

1. <!-- concept: fist-of-five --> **Fist of five for surfacing latent dissent before experiment commit.** One person states a proposed experiment; each team member responds by holding up a fist (strong reject / blocks consensus) or one through five fingers (up to strong accept and willing to lead) [V] (Ch 2.4.3, "Measuring and Building Consensus: Fist of Five Method"). A two-or-fewer response blocks and opens a conversation. The method "can reduce risk by (1) bringing problems to light and (2) increasing team motivation, ownership, and investment" [V] (Ch 2.4.3). Crucially, the reveal is simultaneous — a sequential show of hands allows social pressure to cascade before honest signals emerge.

2. <!-- concept: raci-matrix --> **RACI matrix for ambiguous experiment ownership.** The RACI matrix defines Responsible (who does the work), Accountable (who approves and owns the outcome), Consulted (who advises), and Informed (who receives status) [V] (Ch 2.4.2, "Defining Roles and Responsibilities: RACI Matrix"). When a retro experiment lands in a cell with no named Accountable individual — "team responsible," "engineering to investigate" — it will not survive to the next experiment-review phase. Building a minimal RACI for each experiment before adjournment is the structural refusal of ambiguity.

3. <!-- concept: invest-criteria --> **INVEST criteria for experiment quality.** The INVEST acronym (Independent, Negotiable, Valuable, Estimable, Small, Testable) [V] (Ch 3.6.1, citing Wake 2003) characterises a well-formed user story; it scales directly to retro experiment design. An experiment that is not Independent (depends on another team's action), not Estimable (no one knows how long it takes), not Small (spans multiple Sprints), or not Testable (no named success criterion) has the structural shape of an experiment that will fail without producing learning.

4. <!-- concept: planning-poker --> **Planning poker as private-estimate-before-reveal discipline.** Each team member privately selects an estimate card; all reveal simultaneously; differences open a discussion [V] (Ch 2.5.5, citing Cohn 2006). Applied to retro voting: simultaneous reveal breaks the HiPPO-driven cascade that anchors group estimates to the most senior voice's number (the Jørgensen-Sjøberg finding, referenced in Jones's distillation). When choosing which retro item to deep-dive or how to weight experiments, private-before-reveal prevents early voices from anchoring the field.

5. <!-- concept: code-smells --> **Twelve named code smells as recurring-pattern vocabulary.** Four families: comments (Obsolete Comment, Commented-Out Code, Redundant Comment, Long Comment); functions (Long Function, Function with Many Jobs, Function with Many Parameters); code in general (Duplicate Code, Long Lines, Inconsistent Conventions, Vague Naming) [V] (Ch 8.3–8.5). When a retro's recurring theme is "code is hard to maintain" or "every feature takes longer than it should," naming the specific smells present gives the team a precise vocabulary for what to address — rather than the vague "technical debt" label that produces unfocused actions.

6. <!-- concept: code-decay-loop --> **Code decay is self-reinforcing.** "Smelly code leads to smellier code" — the presence of disorganised code signals to the team that disorganised code is acceptable, producing a reinforcing loop [V] (Ch 8.1). At a retro, if code-quality themes are recurring (Phase 0.5: same experiment three retros running), this reinforcing pattern is the structural explanation. The intervention is not effort but normalisation: a refactoring practice that becomes routine breaks the loop.

7. <!-- concept: inclusivity-heuristics --> **Eight Inclusivity Heuristics for UI-related retro items.** The heuristics — Explain benefits; Explain costs; Let users gather information at their own pace; Keep familiar features available; Enable undo/redo and backtracking; Provide an explicit path; Provide ways to try approaches; Encourage mindful tinkering [V] (Ch 7.3.1–7.3.8) — cover five cognitive facets (attitude toward risk, computer self-efficacy, information processing style, learning style, motivations). When a retro surfaces UI friction ("the team keeps misusing the tool," "users keep making the same mistake"), the Inclusivity Heuristics name whether the UI is failing risk-averse or process-oriented users specifically — not users in general.

8. <!-- concept: team-building --> **Tuckman stage map for retro group dynamics.** Forming, Storming, Norming, Performing, Adjourning [AP] (Ch 2.4, citing Tuckman 1965 and Jensen 1977). A retro on a Storming team will surface resistance patterns — members resist peers' ideas, the facilitator's structure, and any action that requires trusting a teammate. The facilitator's moves differ: ground rules need more explicit buy-in; fist of five is more important (latent resistance is higher); experiment size should be smaller (lower trust to carry a large commitment across a Sprint).

9. <!-- concept: triple-constraint --> **Triple constraint for retro-level resource decisions.** Time, Cost, and Scope are the constraints; each experiment implicitly makes a choice about which constraint is Constrained (fixed), Enhance (try to improve), or Accept (allowed to worsen) [V] (Ch 2.5.2, "Balancing Constraints: Project Priority Matrix"). When a retro proposes an experiment that requires time the team does not have, the triple constraint names the choice: if time is Constrained, the experiment must shrink in scope — it cannot be committed as-is.

10. <!-- concept: ground-rules --> **Ground rules require genuine buy-in.** Effective ground rules "need buy-in from the whole team"; rules that feel "silly, phony, too aspirational, too inflexible, or too authoritative" invalidate the exercise [V] (Ch 2.4.1). For the retro: the Prime Directive and Vegas Rule (the retro's equivalent ground rules) need the same care. Performative agreement is worse than no ground rules — it suppresses honest data without replacing it with anything.

11. <!-- concept: context-dependence --> **Software development is not black and white.** "Right answers can be hard to find and may not be reproducible in different contexts" [AP] (Introduction, "Software Engineering Is Not Black and White"). Retro experiments are hypotheses, not prescriptions. A practice that worked for another team is not guaranteed to work here; the retro's experiment-design posture should hold team context as the key variable.

12. <!-- concept: eisenhower-matrix --> **Eisenhower matrix for prioritising which retro item to address.** Urgent × Important quadrant grid: Do (urgent, important), Decide (not urgent, important), Delegate (urgent, not important), Delete (not urgent, not important) [V] (Ch 2.5.3, "Task Prioritization: Eisenhower Matrix"). When five retro items are on the board and the team cannot choose, the Eisenhower matrix provides a structured first-pass filter. Items in Delete are often the ones that make the board crowded without ever being acted on.

## Questions to Ask During Retro

### Phase 2: Data gathering

| Need | Question |
|---|---|
| Vote on which item to deep-dive | Are estimates being revealed simultaneously or sequentially? If sequentially, the first number anchors the field. Use planning-poker-style simultaneous reveal. |
| Code quality is a recurring theme | Which of the twelve named code smells are present in the code the team finds hardest to work with? Name them specifically, not as "technical debt." |
| UI friction surfaces as a data point | Which of the five cognitive facets is the UI failing to support? Is it failing risk-averse users (heuristics 1-2), information-gathering users (heuristic 3), or process-oriented users (heuristic 6)? |

### Phase 3: Insight / cause analysis

| Need | Question |
|---|---|
| A recurring problem involves code | Is the decay self-reinforcing — has the presence of disorganised code normalised further disorganisation? Name the specific smells, then name what normalised them. |
| Decision ownership is contested as a cause | Build the RACI for the decision that contributed to the problem. Where was the Accountable cell empty or contested? |
| Team is resisting the insight phase | Where is this team on the Tuckman map? If Storming, resistance to peers' ideas is structural, not personal — adjust the facilitation move, not the diagnosis. |

### Phase 4: Experiment design

| Need | Question |
|---|---|
| Five experiments are on the board | Run the Eisenhower matrix: which are Do (urgent, important)? Delete the non-urgent, not-important ones. One constraint leaves more room to act than five. |
| Experiment ownership is ambiguous | Build a RACI: name the Accountable individual — not a team, not a role, a person — before the retro closes. |
| Dissent is present but unstated | Run fist of five with simultaneous reveal. A two-or-fewer response blocks; open the conversation before committing. |
| Experiment is too big | Apply INVEST: is it Small (fits in one Sprint)? Is it Estimable (someone can give a time estimate)? Is it Testable (there is a named done-condition)? Shrink until it passes. |
| Experiment references a resource constraint | Apply the triple constraint: which of the three constraints is Fixed (Constrain), to be improved (Enhance), or allowed to worsen (Accept)? Name the choice; do not leave it implicit. |

### Phase 5: Close

| Need | Question |
|---|---|
| Experiments are committed but ownership is thin | Before adjournment: for each experiment, who is Accountable? Run fist of five on the named owner's commitment level — do they show three or more fingers? |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| Experiment has "team responsible" as owner | RACI's Accountable cell is empty; no individual owns the outcome | Name one person as Accountable before the retro closes |
| Team agrees quickly on an experiment | Sequential reveal may have anchored the vote | Run fist of five with simultaneous reveal; a two-or-fewer response blocks |
| Recurring theme is "technical debt" or "code quality" | Vague label will produce vague actions | Name the specific code smells present — which of the twelve apply to the code the team finds hardest to work with? |
| Team resists the insight phase | Tuckman Storming dynamic — resistance to peers' ideas is structural, not personal | Reduce experiment size; require more explicit buy-in; don't increase pressure |
| Experiment spans multiple Sprints | Fails INVEST's "Small" criterion | Shrink: what is the smallest version that would still test the hypothesis? |
| A UI-related friction item surfaces | "User error" framing is tempting | Apply Inclusivity Heuristics: which cognitive facet is the UI failing? |
| Five experiments on the board at close | Too many commitments; none will be owned | Run the Eisenhower matrix: Delete the not-urgent, not-important items first |

## When to Use This Reference

Reach for this distillation when:
- Phase 4 (experiment design) is the moment and the team needs structured tools: fist of five for latent dissent, RACI for ownership, INVEST for quality, Eisenhower for prioritisation.
- Code quality is a recurring retro theme — the twelve named code smells provide specific vocabulary the vague "technical debt" label does not.
- The team is on the Tuckman Storming stage — the facilitation moves here (smaller experiments, more buy-in rituals, simultaneous reveal) are stage-appropriate.
- A triple-constraint trade-off needs to be named explicitly when the team is proposing a time-consuming experiment.

Prefer the Approach Perfect Field Guide for the retro agenda container. Prefer the Liberating Structures Handbook for meeting-level facilitation moves. This source is the structured-method toolkit for Phase 4 and for code-quality diagnosis in Phase 3.

## Worked Example

A team is in its third retro where "the codebase is hard to work with" appears in the data-gathering phase. The lead asks the team to name which of the twelve code smells are present rather than staying with "technical debt." The team names: Long Function, Duplicate Code, and Inconsistent Conventions. Three specific smells, not one vague category.

In Phase 3, the lead asks whether the code decay is self-reinforcing: has the presence of disorganised code normalised further disorganisation? The team agrees it has — the norm is "if the code around it is messy, new code can be messy too." This is the reinforcing pattern Letaw names [V] (Ch 8.1).

In Phase 4, five experiments are on the board. The lead runs the Eisenhower matrix: two items are not-urgent and not-important — they go to a visible "later" list. The remaining three are assessed against INVEST. One fails "Small" (spans three Sprints). It is shrunk to a single-Sprint version: refactor one high-traffic function per Sprint using a paired-programming session. A RACI is built: one named Accountable individual (not "the team"). The fist of five runs simultaneously: all show four or five fingers except one person who shows two. The team opens the conversation before committing.

The twelve code smells, RACI, INVEST, fist of five, Eisenhower matrix, and Tuckman stage framing all trace to Letaw (Ch 8.3–8.5; Ch 2.4.2; Ch 3.6.1; Ch 2.4.3; Ch 2.5.3; Ch 2.4).

## Anti-patterns This Reference Helps Avoid

- Committing experiments with "team responsible" in the owner field; the RACI's Accountable cell must name an individual before the retro closes.
- Running a verbal show-of-hands before fist of five; sequential reveal allows social pressure to cascade, suppressing the honest signal the method is designed to surface.
- Naming "technical debt" as a retro theme without specifying which of the twelve code smells are present; the vague label produces vague actions.
- Designing experiments that fail the INVEST test — not Testable (no success criterion), not Small (spans multiple Sprints), not Independent (requires another team's action) — and discovering at the next experiment review that the experiment produced no learning.
- Treating a Storming team's resistance to retro actions as individual reluctance rather than as a Tuckman-stage dynamic; the facilitation move is structural (smaller experiments, more explicit buy-in), not motivational.
- Running the retro's closing vote with sequential anchoring rather than simultaneous reveal — the first voice's preference shapes all subsequent ones.
- Framing Inclusivity Heuristic failures as "user error" rather than as UI design problems; the heuristics name the cognitive-facet mismatch precisely.
- Proposing a multi-Sprint experiment without naming the triple-constraint trade-off — which constraint is being sacrificed, and does the whole team understand that implicitly accepted sacrifice?

## Integration with Other References

| Reference | Relationship |
|---|---|
| Approach Perfect Field Guide | The Field Guide's one-or-two-improvements discipline is the container; Letaw's RACI, INVEST, and fist of five are the structured methods that populate Phase 4 within that container |
| Open Practice Library | OPL's Design of Experiments formalises the Hypothesis/Pass-criteria structure that complements Letaw's INVEST quality check |
| Jones Evidence-Based Software Engineering | Jones's Goodhart's Law test applies to the new metric an experiment might propose; Letaw's INVEST test applies to the experiment's structure; both are Phase 4 gates |
| OpenStax Organizational Behavior | OB's Tuckman stage vocabulary is the broader diagnostic for the Storming-team pattern Letaw's facilitation moves address at the practice level |
| Liberating Structures Handbook | LS's simultaneous-reveal planning-poker discipline is the same epistemic move as Letaw's fist-of-five simultaneous reveal; both counteract anchor cascade |
| OpenStax Psychology 2e | Psychology 2e's conformity and anchoring findings explain why simultaneous reveal matters mechanically; Letaw supplies the practice, Psychology 2e supplies the cognitive science |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** Planning poker is attributed to Cohn (2006) [BT] (Ch 2.5.5). INVEST is attributed to Wake (2003) [BT] (Ch 3.6.1). Tuckman's model is cited as Tuckman (1965) and Jensen (1977) [BT] (Ch 2.4). The Inclusivity Heuristics are attributed to Microsoft's framework for designing for human diversity [V] [BT] (Ch 7, opening). CHAOS Report (Standish Group, 2015) is cited for failure-rate data [BT] (Ch 1.1). The triple constraint draws on van Wyngaard et al. (2012) [BT] (Ch 2.2). None of Cohn, Wake, Tuckman, Jensen, or van Wyngaard are held directly in this corpus.

**Named limits of the source.** Letaw describes the book as "geared toward Agile software development" [V] (Introduction); the methods are framed in an Agile context. The handbook introduces software engineering methods — it names its scope as portable methods, not team coaching, facilitation, or retrospective structure. The RACI, fist of five, INVEST, and Eisenhower matrix all require the retro container (supplied by the Field Guide); this source does not supply the container. The Inclusivity Heuristics are specific to UI/UX design decisions and transfer to retro work only when a UI friction item is the retro topic.

**Evidence-marker continuity.** Fist of five's "can reduce risk by (1) bringing problems to light and (2) increasing team motivation, ownership, and investment" is `[V]` in the deep ref; the distillation carries the dual benefit without blockquoting. RACI definitions (Responsible, Accountable, Consulted, Informed) are `[V]` in the deep ref; the distillation uses these precisely. Code decay self-reinforcement ("smelly code leads to smellier code") is `[V]` in the deep ref; the distillation carries this as the reinforcing-loop framing for the code-quality recurring-problem pattern. The INVEST acronym is `[V]` in the deep ref with a Wake (2003) attribution; the distillation applies it as a quality gate without claiming it originates with Letaw.
