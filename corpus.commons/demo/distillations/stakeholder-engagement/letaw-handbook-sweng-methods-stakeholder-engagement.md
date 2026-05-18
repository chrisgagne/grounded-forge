# Letaw, Handbook of Software Engineering Methods — Stakeholder-Engagement Distillation

**Source:** Letaw, L. (2024). *Handbook of Software Engineering Methods* (2nd ed.). Oregon State University. CC BY-NC 4.0. https://open.oregonstate.education/setextbook/.

## Stakeholder-Engagement Relevance

Letaw's *Handbook* threads stakeholder engagement through four chapters rather than confining it to one. **Chapter 2 (Project Management and Teamwork)** addresses the engagement of *team members* — Tuckman's five-stage development model, ground rules with whole-team buy-in, RACI matrix for decision rights, fist of five for consensus — and the engagement of *clients* via the project priority matrix decided "before the project starts, with the client." **Chapter 3 (Requirements)** is the chapter most directly about external stakeholder engagement: requirements elicitation through interviews, focus groups, lab studies, and exploratory research; user stories that frame functionality from the user's perspective; client conversations to set priorities and acceptance criteria. **Chapter 6 (Paper Prototyping)** is a structured method for engaging users in design feedback through low-fidelity prototypes and the think-aloud protocol. **Chapter 7 (Inclusivity Heuristics)** reframes stakeholder engagement as inclusive design: building technology that "draws on the full range of human diversity" and explicitly engaging stakeholders across attitudes toward risk, computer self-efficacy, information processing style, learning style, and motivations, embodied as the personas Abi, Pat, and Tim.

A unifying theme runs through these threads: each engagement method is presented as *risk mitigation*. Ground rules reduce team-conflict risk. RACI reduces the risk of "shipping a broken product to customers because nobody was assigned to quality assurance." Fist of five reduces decision-commitment risk by surfacing latent dissent. Requirements elicitation reduces drift risk by capturing what stakeholders actually want before code is written. Paper prototyping reduces design-failure risk by getting user feedback before code is written. The Inclusivity Heuristics reduce the risk of designing software that excludes the diversity of real users.

This distillation gathers these threads into a working pattern: how to engage *team* stakeholders during project formation and execution; how to elicit requirements from *external* stakeholders (clients, users, regulators); how to test design decisions with *user* stakeholders before committing implementation; and how to extend stakeholder engagement to the full range of cognitive styles users actually bring.

## Key Concepts for Stakeholder-Engagement

1. **Stakeholders defined (Letaw's framing).** Stakeholders include clients, managers, users, governments, developers of integrated software, the development team, and yourself. Requirements can come from any stakeholder. (Source: Letaw, *Handbook*, Ch 3.4, "Requirements Elicitation")

2. **Tuckman's five stages of team development.** Forming (orientation, testing boundaries); Storming (resistance to group influence); Norming (cohesiveness, new standards); Performing (flexible roles serving team and task); Adjourning (disbanding). Team-stakeholder engagement methods fit different stages: ground rules emerge in Forming and Norming; RACI is most useful in Norming and Performing; fist of five reduces Storming-into-paralysis risk. (Source: Ch 2.4, citing Tuckman 1965 and Tuckman & Jensen 1977 [BT])

3. **Ground rules with whole-team buy-in.** A preemptive or reactive method for reducing team conflict and dysfunction. To be effective, ground rules need buy-in from the whole team; rules feeling "silly, phony, too aspirational, too inflexible, or too authoritative" invalidate the effort. Eight diagnostic questions are offered as starting points; the criterion of "meaningful and authentic" is invariant. (Source: Ch 2.4.1)

4. **RACI matrix for explicit decision rights.** Responsible (who does the work), Accountable (who approves and ensures completion), Consulted (who advises), Informed (who is kept up to date). The matrix reduces risk by preventing the failure mode in which no one knows who needs to do what — the canonical example is "shipping a broken product to customers because nobody was assigned to quality assurance." (Source: Ch 2.4.2)

5. **Fist of five for consensus.** Six-level voting: None (strong reject, blocks), One (reject, major issues), Two (weak reject), Three (weak accept), Four (accept), Five (strong accept, willing to lead). Two-or-fewer triggers discussion; the team or its leader decides how much consensus is required. The mechanism surfaces latent dissent and increases team motivation, ownership, and investment. (Source: Ch 2.4.3)

6. **Project priority matrix decided with the client.** Time, cost, and scope are each tagged Constrain (fixed), Enhance (try to improve), or Accept (can worsen). Ideally defined before the project starts, with the client, and referenced throughout. The matrix anchors client-stakeholder conversations when the inevitable "can you also add this feature?" arrives. (Source: Ch 2.5.2)

7. **Five reasons developer-led requirements elicitation needs care.** Stakeholders might not have experience or expertise, might not have good ideas, might not know what they want, might want what is bad for them or others, and are humans who communicate imperfectly. None of these is a reason to skip the engagement; each is a reason to design the engagement with care. (Source: Ch 3.4)

8. **Four elicitation methods.** Interviews (structured / semi-structured / unstructured); focus groups (small group conversations with moderator guidance); lab studies (participants perform tasks in a controlled setting, then give feedback); exploratory research (immersing oneself in the world of relevant people and products — fly-on-the-wall observations, ethnographic methods). Hanington & Martin (2019) [BT] provides fuller treatment. (Source: Ch 3.4)

9. **User stories as stakeholder-perspective specification.** "As a <role> I can <capability>, so that <receive benefit>." Written in plain English so non-technical stakeholders can understand them. Stakeholders may originate user stories; clients guide prioritisation; conversation about each user story extracts details that get added back to the card. The INVEST acronym (Independent, Negotiable, Valuable, Estimable, Small, Testable) characterises a good user story — and the *N* (Negotiable) is the explicit invitation to ongoing stakeholder conversation. (Source: Ch 3.6.1, citing Wake 2003 [BT])

10. **Definition of Done negotiated with the client.** Acceptance criteria say what must be true about the functionality for the user story to be considered done. Often written in given-when-then format. The DoD is a stakeholder-engagement artefact: it is the boundary between "developer says done" and "client agrees it is done." (Source: Ch 3.6.1)

11. **Paper prototyping with users via swap-and-watch.** Once a paper prototype is in hand, give the user the entry screen drawing and either a task or free exploration. Watch how they interact; quickly swap in other drawings to respond. Combine with a *think-aloud protocol* — asking the user to verbalise what they are doing, trying to do, asking, and disliking. The method is cheap, fast, and surfaces design problems before code commitment. (Source: Ch 6.2; Glossary, "think-aloud protocol")

12. **Inclusivity Heuristics and three personas.** Eight heuristics for designing technology to work well for a diversity of users, framed through three personas (Abi, Pat, Tim) with different combinations of five cognitive facets (attitude toward risk, computer self-efficacy, information processing style, learning style, motivations). The heuristics extend stakeholder engagement to those whose cognitive styles differ from the design team's. (Source: Ch 7, citing Burnett et al. 2016, 2021 [BT])

13. **Heuristic evaluation as multi-evaluator inspection.** Multiple evaluators independently check whether a design follows the heuristics; results are then combined. The independence reduces individual-evaluator bias; the combination surfaces issues no single evaluator would catch. (Source: Ch 7.1, citing Nielsen & Molich 1990 [BT])

14. **The ODOT TOCS migration as a worked case in user-stakeholder needs driving architecture.** Dispatcher centres in different parts of Oregon had different needs but were forced to use the same monolithic home screen; the inability to configure for local stakeholders was the primary user-perspective driver of the monolith-to-microservices migration. Architecture decisions can be stakeholder-driven. (Source: Ch 5.5)

15. **Software engineering as collaboration.** The Agile philosophy values "collaboration-oriented" software development; the Agile Manifesto (Beck et al., 2001) [BT] is cited as the grounding document. HP's 2017 survey found that 54% of Agile adopters cite "enhanced collaboration between teams that don't usually work together" as a benefit — the highest of the five reported benefits. (Source: Ch 1.2; Introduction, "What's This Book Like?")

## Questions to Ask During Stakeholder-Engagement

### Phase 1: Mapping (Identifying who has standing)

| Need | Question |
|---|---|
| Identify the full stakeholder list | Who is affected by this software project — clients, managers, users, governments, developers of integrated software, the development team, ourselves? Have we surfaced stakeholders beyond the immediately-visible ones? |
| Identify the requirements sources | From whom must we gather requirements? Where are the wants and needs we still need to detect? |
| Identify decision-rights gaps | For each significant decision or deliverable, who is Responsible, Accountable, Consulted, Informed? Where is the role assignment ambiguous? |
| Surface latent users | Who will use the software but is not currently in the room? Are users with different cognitive styles (across attitude to risk, self-efficacy, processing style, learning style, motivations) represented? |
| Identify team stakeholders by Tuckman stage | Where is the team in its development arc? Forming (need orientation methods)? Storming (need conflict-management methods)? Norming (need standards-building methods)? |

### Phase 2: Framing (Bounding the engagement before convening)

| Need | Question |
|---|---|
| Set ground rules with whole-team buy-in | What ground rules does this team need? Are they meaningful and authentic, or do they feel silly, phony, or aspirational? Has the whole team bought in? |
| Decide the project priority matrix with the client | Have we agreed with the client which of time, cost, and scope is Constrained, Enhanced, or Accepted? Will this matrix be the referent when scope-creep questions arrive? |
| Choose the elicitation method | Which method fits this stakeholder and this question — structured interview, semi-structured interview, focus group, lab study, or exploratory research? |
| Anticipate the five elicitation pitfalls | Could this stakeholder lack experience/expertise to articulate what they want? Could they have bad ideas? Not know what they want? Want what is bad for them? Communicate imperfectly? |
| Frame user stories for the conversation | If user stories are the artefact, are they in the "As a <role> I can <capability>, so that <receive benefit>" template? Do they meet INVEST? |

### Phase 3: Convening (How to engage in the moment)

| Need | Question |
|---|---|
| Use the right consensus instrument | For a team decision: would fist of five surface latent dissent before commitment? For a high-stakes choice, are we requiring all hands at 3+? |
| Listen for what stakeholders are not saying | Are we using techniques (open-ended questions, group dynamics, observation) that surface the wants and needs stakeholders cannot or will not articulate? |
| Apply the think-aloud protocol if observing users | If users are interacting with prototypes or working software, are we asking them to verbalise what they are doing, trying to do, asking, and disliking? |
| Engage diverse cognitive styles | Are we checking how Abi (low self-efficacy, risk-averse, process-oriented), Pat (moderate, mixed style), and Tim (high self-efficacy, risk-tolerant, tinkerer) each experience this design? |
| Use heuristic evaluation for design decisions | Have multiple evaluators independently checked the design against the eight Inclusivity Heuristics? Is the combined output the basis for revisions? |

### Phase 4: Capturing (Recording what was learned)

| Need | Question |
|---|---|
| Translate elicited needs into requirements | Are functional requirements and nonfunctional requirements both captured? Do they meet the eight-attribute good-requirement standard? |
| Document the Definition of Done | For each user story, what set of acceptance criteria, when satisfied, will mark it DONE-done? Have we negotiated this with the client? |
| Update the RACI matrix | As work emerges from the engagement, do new tasks or deliverables need explicit role assignment? |
| Update ground rules | Has the engagement surfaced team-process issues that should change the ground rules? |
| Annotate the project priority matrix | Has the engagement changed the constraint priorities? If so, who needs to be informed? |

### Phase 5: Following through (Maintaining engagement over time)

| Need | Question |
|---|---|
| Use Sprint Review for client engagement | Are we using Sprint Reviews to present results to key stakeholders and decide future adaptations? Are the right stakeholders in the room? |
| Use Sprint Retrospective for team engagement | Are we using Sprint Retrospectives to plan improvements to quality and effectiveness? Are improvements actually adopted between Sprints? |
| Maintain stakeholder-facing artefacts | Are user stories, RACI matrix, project priority matrix, and Inclusivity Heuristics evaluations being kept current as the project evolves? |
| Use spikes to investigate emerging questions | When new stakeholder concerns surface, are we running structured spikes to gather information before committing to direction? |
| Watch for stakeholder drift | Are we noticing when stakeholders' priorities or constraints shift? When the project priority matrix needs to be re-decided with the client? |

### Phase 6: Closing (Adjourning well)

| Need | Question |
|---|---|
| Adjourn the team intentionally | Tuckman's fifth stage names team disbanding as a phase. Are we marking it, recognising contributions, and capturing lessons learned? |
| Close the client engagement | Has the project priority matrix been honoured? Has the Definition of Done been satisfied across all delivered user stories? Are remaining items explicitly deferred rather than abandoned? |
| Capture user feedback for next iteration | Have we collected post-implementation user feedback? Are insights flowing to whichever team picks up the next iteration? |
| Document decisions for future stakeholders | Have we left enough decision history that future maintainers can pick up where we left off? |

## What to Look For

**Signal:** The team is asking "can you also add this feature?" mid-project.
**Diagnosis:** The project priority matrix was not decided with the client before the project started, or is not being referenced in scope conversations.
**Follow-up:** Return to the matrix with the client. Name the constraint trade-off explicitly: adding scope requires relaxing time, cost, or existing scope.

**Signal:** Requirements elicitation produces thin, vague user stories.
**Diagnosis:** One or more of the five pitfalls has fired — the stakeholder does not know what they want, cannot articulate it, or is communicating imperfectly.
**Follow-up:** Shift elicitation method. If interviews have produced vague answers, try exploratory research (fly-on-the-wall observation) or lab studies (task performance with feedback).

**Signal:** The team has consensus but commits to an unrealistic schedule.
**Diagnosis:** Fist of five was not used, or the minimum-consensus threshold was not specified, allowing latent dissent to remain silent while appearing to assent.
**Follow-up:** Re-run the fist-of-five vote with an explicit minimum (e.g., all hands at 3+). Name the latent dissent before the Sprint starts.

**Signal:** A UI design excludes users with lower self-efficacy or different information-processing styles.
**Diagnosis:** The design was built for designer-like users (Abi and Pat were not represented in the engagement).
**Follow-up:** Run heuristic evaluation against the eight Inclusivity Heuristics with multiple evaluators. Identify which cognitive facets the design fails and revise accordingly.

**Signal:** A team member learns of a key client decision through informal channels, not through a formal stakeholder process.
**Diagnosis:** The RACI matrix has a gap — the role of Informed was not assigned for that decision type.
**Follow-up:** Update the RACI matrix. Identify what else the gap may be hiding.

## When to Use This Reference

- A *new software team is forming* and needs Tuckman-aware engagement methods (ground rules, RACI, fist of five).
- *Requirements elicitation is underway* and the team needs structured methods (interviews, focus groups, lab studies, exploratory research) with awareness of the five common pitfalls.
- A *user-facing design decision* needs validation before code commitment — paper prototyping with think-aloud protocol.
- A *UI design needs inclusive-design evaluation* — heuristic evaluation against the eight Inclusivity Heuristics via Abi, Pat, and Tim.
- A *client conversation* about scope/cost/time trade-offs needs an artefact (project priority matrix).
- *User stories need writing or auditing* for INVEST quality and Definition-of-Done specification.
- A *cross-stakeholder coordination question* (who decides, who is informed) needs a RACI matrix.
- A *Sprint Review or Retrospective* needs framing to maximise stakeholder voice and team improvement.

## Worked Example

A four-person web development team is contracted to build an internal scheduling tool for a regional healthcare clinic. Three weeks into requirements elicitation, they have a backlog of thirty-two user stories — but the Product Owner suspects half are the wrong things to build.

The team returns to the project priority matrix (Ch 2.5.2). With the clinic director, they agree: *time* is Constrained (the tool must be live before the summer hiring surge), *scope* is Enhanced (build the most valuable features), *cost* is Accepted (budget can flex modestly). This matrix immediately collapses fifteen stories into a "later" bucket that the client agrees to defer.

For the remaining seventeen stories, the team uses semi-structured interviews (Ch 3.4) with two distinct stakeholder groups: the schedulers who will use the tool daily, and the clinic managers who need summary views. The interviews surface a conflict: schedulers want to see individual staff constraints (holidays, shift limits); managers want to see department-level availability. A focus group with both groups together reveals that the apparent conflict is a prioritisation disagreement, not a requirements conflict — both features are needed, but the schedulers' constraint view is the higher-leverage starting point.

The team writes six stories in INVEST format, each with a given-when-then Definition of Done negotiated with the clinic director. Before coding begins, they run a paper prototype with three schedulers using the think-aloud protocol (Ch 6.2). Two of the six stories are immediately rewritten based on what the think-aloud surfaces.

The Inclusivity Heuristics evaluation (Ch 7) flags that the current design assumes high computer self-efficacy — the Abi persona would struggle with the date-entry field. The team adds an inline calendar widget. When the tool ships, scheduler adoption is 94% in the first week; clinic management requests the department-view feature for Sprint 2.

The scenario is operator-authored. The project-priority-matrix framing (Ch 2.5.2), the five elicitation-pitfall framework (Ch 3.4), the INVEST user-story discipline (Ch 3.6.1), the think-aloud protocol (Ch 6.2), and the Inclusivity Heuristics / Abi persona (Ch 7) are all `[V]`-marked passages in the deep reference. No verbatim source blockquotes appear in this distillation.

## Anti-patterns This Reference Helps Avoid

- **Selecting stakeholders by who is easy to reach rather than by who affects or is affected** — the full stakeholder list (clients, managers, users, governments, integrated-software developers, the development team, yourself) is the starting frame.
- **Producing user stories without client-negotiated Definitions of Done** — the DoD is the boundary between "developer says done" and "client agrees it is done."
- **Treating ground rules as boilerplate** — ground rules that feel "silly, phony, too aspirational, too inflexible, or too authoritative" fail; the criterion of "meaningful and authentic" is invariant.
- **Skipping the project priority matrix** — without it, every scope-creep conversation is a fresh negotiation with no anchor.
- **Designing for the modal user only** — the Abi, Pat, and Tim personas expose the cognitive-style diversity the design must serve; designing only for Tim produces a tool that excludes Abi.
- **Using fist of five as a rubber stamp** — a two-or-fewer vote that does not trigger discussion produces false consensus and later surface as dropped commitments.
- **Running heuristic evaluation with a single evaluator** — individual-evaluator bias is the failure mode; the multi-evaluator-then-combine discipline is what makes heuristic evaluation useful.
- **Choosing elicitation method by habit rather than by stakeholder fit** — fly-on-the-wall observation when interviews have failed is the exploratory-research move the *Handbook* names.
- **Treating the RACI matrix as a project-launch artefact** — the matrix needs updating as new work and new decision types emerge.
- **Skipping the Adjourning stage** — Tuckman's fifth stage names disbanding as a phase that deserves marking; teams that skip it carry the frictions of the ending project into the next one.

## Integration with Other References

| Reference | Connection |
|---|---|
| OpenStax *Organizational Behavior* (Chs 9, 10, 11, 13, 14) | Provides the broad stakeholder-engagement theory (group interdependence, integration techniques, communication networks, power bases, conflict-resolution modes, negotiation stages). Letaw's *Handbook* operationalises this for software projects: Tuckman's stages frame the team-development arc; RACI implements decision rights more concretely than role-clarity frames in OB; fist of five is the software-team equivalent of consensus-building methods. |
| OpenStax *Business Ethics* (Ch 3) | The Mitchell-Agle-Wood salience model (power, legitimacy, urgency) provides the stakeholder-mapping theory Letaw's *Handbook* lacks. Combine: use Mitchell-Agle-Wood to identify which stakeholders to engage; use Letaw's methods (interviews, focus groups, paper prototyping, Inclusivity Heuristics) to engage them. |
| OpenStax *Principles of Marketing* (Chs 3, 11) | Consumer buying behaviour, B2B buying centre, Gap Model of Service Quality, RATER dimensions, 5A customer journey. For software products with customer-facing components, marketing's customer-engagement vocabulary complements Letaw's user-engagement methods. |
| OpenStax *Principles of Management* (Chs 13, 14, 15) | Mintzberg's managerial roles (interpersonal, informational, decisional) sit upstream of RACI; servant leadership and the Tannenbaum-Schmidt continuum sit upstream of fist-of-five's consensus orientation. |
| OpenStax *Business Law* (Ch 2, ADR-tier framework; Ch 5–9, contract law) | When stakeholder engagement reaches dispute, contractual, or arbitral domains, business-law provides the formal escalation framework Letaw's pre-formal methods feed into. |
| Scrum Guide 2020 | Scrum's Sprint Review and Sprint Retrospective are the cadenced stakeholder-engagement structures; Letaw's methods (interviews, paper prototyping, Inclusivity Heuristics) populate the work done *inside* those structures. Use Scrum for the rhythm; use Letaw for the methods. |
| Open Practice Library | OPL's *Stakeholders Interview*, *Empathy Mapping*, and *Stakeholder RACI Map* practices are field-ready versions of Letaw's academic-textbook treatments. Use Letaw to understand the method rationale; use OPL for the facilitation shape. |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The following authors and bodies are cited in the source but are not held as primary references in this corpus. Practitioners needing the foundational treatment should consult these directly:
- Tuckman (1965) and Tuckman & Jensen (1977) — five-stage team-development model (Ch 2.4) [BT]
- Beck et al. (2001), Agile Manifesto — grounding document for the Agile philosophy (Ch 1.2.1) [BT]
- Wake (2003), "Invest in good stories" — INVEST acronym for good user stories (Ch 3.6.1) [BT]
- Hanington & Martin (2019) — fuller treatment of requirements-elicitation methods (Ch 3.4) [BT]
- Burnett et al. (2016, 2021), GenderMag project — source of the Inclusivity Heuristics and five cognitive facets (Ch 7) [BT]
- Nielsen & Molich (1990); Nielsen (1994) — heuristic evaluation as a usability inspection method (Ch 7.1) [BT]
- Wiegers & Beatty (2013), *Software Requirements* — functional/nonfunctional and quality-attribute definitions (Ch 3.1, 3.5) [BT]
- Texas Department of Information Resources (2008) — eight-attribute good-requirement standard (Ch 3.3) [BT]
- ISO/IEC/IEEE 24765:2017 — software-engineering definition used throughout [BT]
- Hewlett Packard Enterprise (2017) survey — Agile adoption data (Ch 1.2) [BT]

**Named limits of the source.** The text explicitly acknowledges or implies these scope boundaries:
- Detailed stakeholder-mapping frameworks (Mitchell-Agle-Wood salience; Freeman stakeholder theory) are not developed. The *Handbook* names stakeholders implicitly and engages them through methods but does not develop a stakeholder-mapping theory.
- Negotiation theory (BATNA, distributive vs integrative bargaining, principled negotiation) is not developed. Letaw's engagement methods are upstream of formal negotiation.
- Cross-cultural stakeholder engagement is addressed only in passing (ground rules will vary by culture, Ch 2.4.1). Hofstede and culture-aware engagement are not developed.
- Power and politics dynamics (French and Raven, resource dependence) are not developed. RACI is a decision-rights artefact, not a power analysis.
- Regulatory-stakeholder engagement (privacy law, accessibility law) is gestured at through quality attributes and constraints but not developed.
- The source is CC BY-NC 4.0 (open-nc); derivative works for commercial purposes require permission.

**Evidence-marker continuity.** The deep reference at `corpus.commons/demo/references/letaw-handbook-sweng-methods-deep.md` uses `[V]`, `[AP]`, `[AR]`, `[AE]`, and `[BT]` markers throughout (111 `[V]`, 57 `[BT]`, 11 `[AP]`, 1 `[AR]`). This distillation paraphrases throughout; Key Concepts drawn from the source's method chapters are `[V]` in the deep ref (verbatim from source). The Agile Manifesto, Tuckman model, INVEST acronym, and the eight-attribute good-requirement standard are all `[BT]` in the deep ref (cited in the source). The healthcare-clinic scheduling example in the Worked Example is operator-authored. The five-elicitation-pitfalls framing and the ODOT TOCS microservices case are `[V]` and `[AE]` respectively in the deep ref.
