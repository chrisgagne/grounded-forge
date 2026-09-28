# Retro Distillation Index

> **Purpose:** Situation-to-resource router for retrospective-facilitation work. "I'm at this point in a retro — which references should I reach for?"

This is the *when-to-use* layer for the retrospective task. It partitions the task into seven phases (Phase 0 setup; Phase 0.5 experiment review; Phase 1 priming; Phase 2 data gathering; Phase 3 insight / cause analysis; Phase 4 experiment design; Phase 5 close) and lists distillations appropriate to each phase. For the *what-is* layer (descriptions of each reference), read [`reference-index.json`](../../reference-index.json) at the corpus root. For the task-axis scoping that produced this index, see [`corpus.commons/demo/tasks/retro.md`](../../tasks/retro.md).

**Workflow:** Distillation index (when) → distillation (how) → deep reference (citations, if needed).

The retro axis is the iterative team-internal counterpart to the event-triggered cross-functional [[aar]] axis; see [`distillations/aar/AAR-DISTILLATION-INDEX.md`](../aar/AAR-DISTILLATION-INDEX.md) for the AAR side of the same conversation.

---

## Format

Two table shapes appear in this index.

**Phase-by-phase tables** (the main routing layer) use four columns. The "Need" column describes the situation; "Reference" names the source; "Distillation" links to the projected distillation; "Reach for this when" gives a one-line routing cue.

```markdown
| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| ... | ... | ... | ... |
```

**Quick-start tables** (the situation-first lookup) use three columns: a situation description, the primary references that apply, and the distillation file paths.

```markdown
| Situation | Primary references | Distillations |
|---|---|---|
| ... | ... | ... |
```

Concepts within a distillation may be referenced with line ranges (`{file}.md L{start}-L{end}`) for fine-grained pointers. The build validates the filename inside the backticks; line ranges are a human convention.

---

## Quick start by retro situation

| Situation | Primary references | Distillations |
|---|---|---|
| **First retro for a new team** | Field Guide Sprint Retrospective sample agenda + Open Practice Library Retrospectives | `approach-perfect-field-guide-scrum-events-retro.md`, `open-practice-library-retro.md` |
| **Low safety check score (1-2 out of 5)** | Open Practice Library Psychological Safety + Establish Shared Principles | `open-practice-library-retro.md` |
| **Recurring problem 3+ retros running** | SSDL system archetypes + Barbrook-Johnson CLD + Open Kanban Holistic value | `ssdl-systems-thinking-foundations-retro.md`, `barbrook-johnson-systems-mapping-retro.md`, `open-kanban-retro.md` |
| **Blame language surfacing** | NHS default-to-system + Field Guide Prime Directive | `nhs-just-culture-guide-retro.md`, `approach-perfect-field-guide-scrum-events-retro.md` |
| **One voice dominating** | Liberating Structures 1-2-4-Whole Group + FLO engagement-equity tracking | `liberating-structures-handbook-retro.md`, `flo-facilitation-guide-retro.md` |
| **Manager on the call** | FLO engagement-equity tracking + Field Guide strict participant control (invited only by the entire Scrum Team; support, not steer) | `flo-facilitation-guide-retro.md`, `approach-perfect-field-guide-scrum-events-retro.md` |
| **Five experiments on the board** | Field Guide one-or-two discipline + Open Kanban batch-size practice | `approach-perfect-field-guide-scrum-events-retro.md`, `open-kanban-retro.md` |
| **Last retro's experiments not done** | TC 25-20 follow-up rule + LS 15% Solutions + Open Practice Library Design of Experiments | `tc-25-20-army-aar-retro.md`, `liberating-structures-handbook-retro.md`, `open-practice-library-retro.md` |
| **AI-adoption friction** | Open Practice Library Evals + Human-in-the-Loop + Establish Shared Principles | `open-practice-library-retro.md` |
| **Counterfactual creeping in** | LFUO forbidden-move list | `lfuo-learning-review-guide-2024-retro.md` |
| **Team-internal cadence (not incident-triggered)** | Field Guide Sprint Retrospective + Scrum Guide canonical event | `approach-perfect-field-guide-scrum-events-retro.md`, `scrum-guide-2020-retro.md` |
| **Same impediment surfacing repeatedly across retros — structural mismatch suspected** | Org Topologies Primer — archetype-mismatch vocabulary + structural-vs-process classification | `org-topologies-primer-2025-retro.md` |

---

## Phase 0: Setup (working agreement, safety, confidentiality, Prime Directive)

| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| Read Norm Kerth's Retrospective Prime Directive aloud | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | At every retro: *"Regardless of what we discover, we understand and truly believe that everyone did the best job they could..."* — especially when blame language is anticipated. |
| Choose Vegas Rule or Chatham House Rule explicitly | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | A retro is about to start without a named confidentiality rule. Vegas Rule (unanimous explicit consent before sharing) or Chatham House Rule (information shared, identities not). Pick one. |
| Frame Vegas-rules privacy for online retros | FLO Facilitation Guide | `flo-facilitation-guide-retro.md` | Online-retro-specific privacy and confidentiality framing; recording-as-consent (not default). |
| Run a safety check at the start | Open Practice Library | `open-practice-library-retro.md` | Check-ins and Establish Shared Principles are the Open Practice Library practices for the safety move; if safety is 1-2, address it before the topic (the retro task spec rule, not the library's). |
| Establish shared principles before content | Open Practice Library | `open-practice-library-retro.md` | Against copy-practice-without-principles: copying practices without the values and principles behind them will not get the same result; name why and how the team will act before what it will do. |
| Handle a manager on the call | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | Field Guide strict participant control: no one else attends unless invited by the entire Scrum Team, and non-team attendees support rather than steer; FLO engagement-equity tracking matrix supports operationalising it. |
| Surface power-dynamics before opening | FLO Facilitation Guide | `flo-facilitation-guide-retro.md` | Engagement-equity tracking matrix; foundation-of-trust for honest exchange. |
| Set the Scrum Retrospective frame | Schwaber & Sutherland, The Scrum Guide | `scrum-guide-2020-retro.md` | Sprint Retrospective as one of the four inspect-and-adapt events inside the Sprint, the one that concludes it; team inspects individuals, interactions, processes, tools, Definition of Done; 3h timebox for monthly Sprint. |
| Default to the Derby-Larsen six-segment shape | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | The 1½-hour Sprint Retrospective in its six-segment form is the default; sample agenda concrete enough to facilitate. |
| Frame the retro as team-internal iterative, not incident-triggered | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | If the team is mid-incident, route to [[aar]] axis instead; retro is iterative team-internal cadence. |
| Hold default-to-system framing in the substrate | NHS Improvement, Just Culture Guide | `nhs-just-culture-guide-retro.md` | "Action singling out an individual is rarely appropriate" — even in retro context, the guide's prior, applied by analogy, frames blame language. |
| Read the team's Tuckman stage before opening | OpenStax, Principles of Management | `openstax-principles-management-retro.md` | Forming (polite, surface), storming (contested), norming (ground rules), performing (self-directed): ask how much structure the stage calls for; with a storming team, acknowledge the storm before data gathering. Match the setup structure to the stage. |
| Check for hygiene-factor suppression before content | OpenStax, Principles of Management | `openstax-principles-management-retro.md` | If a live anxiety (job security, org change, manager conflict) is in the room, Herzberg's hygiene framing suggests it may crowd out motivator-level engagement. Name it or address it before the topic phase. |
| Safety check returns 1-2 | U.S. Marine Corps, MCDP 1: Warfighting | `mcdp1-warfighting-retro.md` | Ch 3 critique rule: a team member's willingness to admit mistakes "depends on the commander's willingness to tolerate them". Before asking for mistakes, the lead (and any manager) states that admitted mistakes will be discussed, not punished; trust "is a product of confidence and familiarity" and is not rebuilt in one retro. |
| Lead names manager on call | U.S. Marine Corps, MCDP 1: Warfighting | `mcdp1-warfighting-retro.md` | Brief the manager before the retro: open by stating tolerance for admitted mistakes (Ch 3, "Training"), and invite disagreement before the team commits; MCDP 1 makes honest opinion before a decision a duty (Ch 3, "Professionalism"). |

## Phase 0.5: Experiment review (what did we say last time, what happened)

| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| Review last retro's experiments without punishment | US Army, TC 25-20 | `tc-25-20-army-aar-retro.md` | *Real benefits come from applying results* scales down to retro level; if the experiment was unowned, the experiment design failed, not the team. |
| Treat experiments as designed-not-declared | Open Practice Library | `open-practice-library-retro.md` | Design of Experiments practice — the experiment is a hypothesis, the outcome is the evidence. |
| Reframe locus-of-control when last experiment stalled | Liberating Structures Handbook | `liberating-structures-handbook-retro.md` | 15% Solutions: *"Where do you have freedom to act? What's in your 15%?"* — the handbook's own question; it separately quotes Gareth Morgan on "15-percent initiatives", borrowed-through. |
| Detect *same experiment 3+ retros running* pattern | SSDL, Systems Thinking Foundations (Brief 1.07) | `ssdl-systems-thinking-foundations-retro.md` | Fixes that fail or shifting the burden may be in play; surface as hypothesis-generator, not label. |
| Escalate when experiment crosses to structural-change | Open Kanban | `open-kanban-retro.md` | Holistic / Systemic value (Deming + Goldratt borrowed-through): "no single part of a system can ever bring overall improvement"; the team's part alone will not bring it, so raise fixes that lie outside the team rather than retry at team level. |
| Surface the *team is allergic to "experiments" framing* problem | Open Practice Library | `open-practice-library-retro.md` | Establish Shared Principles to surface why the word lands wrong before swapping vocabulary. |
| Detect the structural-repeat pattern when the same experiment re-surfaces | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-retro.md` | Third or fourth retro proposing essentially the same experiment is the structural-mismatch detection signal; ask whether the team is failing or retrospecting against a structural constraint it cannot change unilaterally. |
| Reframe from team-failure to structural-constraint | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-retro.md` | When an experiment hasn't taken hold, apply the Primer's single-team-island warning: "A single high-performing team can't deliver its full potential if surrounding structures and processes remain unchanged." Reframe before generating another 15% experiment. |
| Last retro's experiments weren't done | U.S. Marine Corps, MCDP 1: Warfighting | `mcdp1-warfighting-retro.md` | Sort before judging: an experiment tried boldly that failed is the kind of error MCDP 1 treats leniently (no "zero defects" mentality); one never started is inaction, taken up as a topic rather than a sanction. Ask why, starting with its owner and stated purpose (Ch 3, "Professionalism"; Ch 4, "Commander's intent"). |
| Same experiment proposed three retros running | U.S. Marine Corps, MCDP 1: Warfighting | `mcdp1-warfighting-retro.md` | Main-effort rule: a commitment is "not an irretrievable one", and when shifting "we seek to exploit success rather than reinforce failure" (Ch 4, "Main effort"); ask what in this Sprint calls for the experiment, not habit (Ch 4, "Decisionmaking"). |

## Phase 1: Priming (set the topic frame, surface energy, choose retro shape)

| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| Choose the retro shape that fits this Sprint's content | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | Field Guide six-segment Derby-Larsen pattern is the default; sample agenda includes positives / deltas / insights / √n voting. |
| Reach for alternate retro shapes from the catalogue | Open Practice Library | `open-practice-library-retro.md` | Open Practice Library Retrospective practice with multiple shapes when the default doesn't fit. |
| Open with an energising structure | Liberating Structures Handbook | `liberating-structures-handbook-retro.md` | LS Impromptu Speed Networking or Knee-to-Knee Conversation as opener when team is low-energy. |
| Calibrate facilitator presence to phase | FLO Facilitation Guide | `flo-facilitation-guide-retro.md` | High-presence community building early; lighter once the team owns the conversation: participate in discussions but don't lead. |
| Frame AI-adoption-friction retro | Open Practice Library | `open-practice-library-retro.md` | Evals practice (against AI overconfidence); Human-in-the-Loop (against silent AI delegation); Establish Shared Principles to surface what principles govern the team's AI use before it commits to adoption or delegation. |
| Detect the *Anxious-Annie* facilitator pattern in oneself | FLO Facilitation Guide | `flo-facilitation-guide-retro.md` | When the urge to fill a silence or rush in because the stickies are sparse is rising — locate it as one's own anxiety, not the team's problem; let the silence breathe before prompting. *Trust the process*. |
| Route mid-incident to AAR axis | (cross-axis) | (`aar` axis — see [[aar]]) | If the team is mid-incident rather than mid-iteration, retro is wrong axis; route to AAR. |
| Frame the retro through Scrum's empiricism pillars | Schwaber & Sutherland, The Scrum Guide | `scrum-guide-2020-retro.md` | Transparency / Inspection / Adaptation — the retro is where the team adapts its own way of working, one of the four inspect-and-adapt events inside the Sprint. |
| Use OT mapping as a priming activity when structural recurring topic is suspected | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-retro.md` | When the same topic has surfaced two or more retros with experiments not moving the needle, spend 10 minutes mapping the team's current archetype against the work being demanded. The mismatch (if any) is the priming insight that frames the data-gathering phase. |
| Surface the team's current archetype before content | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-retro.md` | Ask: what is our archetype today (TASKS-2 multi-skill incomplete? CAPS-2 multi-skill capability-focused? CAPS-3 end-to-end ownership)? What archetype does the work being demanded require? The gap, if named, changes the data-gathering frame. |

## Phase 2: Data gathering (positives, deltas, insights)

| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| Run chat-waterfall written-first input | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | Each team member writes positives / deltas / insights individually on stickies; group like items; vote on top 3 to deep-dive. (Applied reading: writing before talking keeps the first voice from setting the field.) |
| Run 1-2-4-All to refuse HiPPO-driven discussion | Liberating Structures Handbook | `liberating-structures-handbook-retro.md` | LS 1-2-4-All: individual reflection → pairs → groups of 4-6 → whole group; by the whole-group round every participant has formed and tested a view, so a dominant voice finds it harder to anchor the room. |
| Run 1-2-4-All from the Open Practice Library | Open Practice Library | `open-practice-library-retro.md` | Open Practice Library's 1-2-4-All practice — against HiPPOs. |
| Run Troika Consulting when team has parallel individual challenges | Liberating Structures Handbook | `liberating-structures-handbook-retro.md` | Three-person 10-min-per-focal-person rounds; peer honing → between-peer conversation → with-focal-person conversation. |
| Track engagement equity in real time | FLO Facilitation Guide | `flo-facilitation-guide-retro.md` | Contribution log adapted from FLO's engagement-equity tracking matrix (which logs the facilitator's own responses); surface who has spoken / not spoken; rebalance via written-first or structured rounds. |
| Surface artificial-harmony pattern when team agrees too quickly | Liberating Structures Handbook | `liberating-structures-handbook-retro.md` | LS Mini Constellations: spatial positioning by degree of agreement; speak from the distance as a "role"; surfaces range without forcing a vote. |
| Surface mental-model partiality | SSDL, Systems Thinking Foundations (Brief 1.03) | `ssdl-systems-thinking-foundations-retro.md` | Each participant holds a partial-but-valid model; mental models are "resistant to change, especially among individuals who aren't personally experiencing any negative system effects". |
| Reframe a helpless team to 15% Solutions | Liberating Structures Handbook | `liberating-structures-handbook-retro.md` | LS 15% Solutions: locus-of-control reframe; *"Where do you have freedom to act? What's in your 15%?"* — without denying the 85%. |
| Apply What/So What/Now What sequence to the raw data | Liberating Structures Handbook | `liberating-structures-handbook-retro.md` | Three-question sequence imposes structure: What (data) → So What (pattern) → Now What (next step). Refuse jumping to Now-What. |
| Detect dominance pattern | FLO Facilitation Guide | `flo-facilitation-guide-retro.md` | FLO engagement-equity tracking, adapted as a contribution log; when one voice is dominating, pause and rebalance. |
| Use planning-poker-style estimates for retro vote weight | Letaw, Handbook of Software Engineering Methods | `letaw-handbook-sweng-methods-retro.md` | When voting on which retro item to deep-dive, private estimate → simultaneous reveal beats sequential reveal which anchors. |
| Team agrees too quickly | U.S. Marine Corps, MCDP 1: Warfighting | `mcdp1-warfighting-retro.md` | Until a decision is stated, honest disagreement is a duty; after it, everyone supports it as their own (Ch 3, "Professionalism"). Ask for the dissent before the vote. |
| Team is helpless ("nothing we can do") | U.S. Marine Corps, MCDP 1: Warfighting | `mcdp1-warfighting-retro.md` | Sort the deltas against MCDP 1's five examples of self-induced friction (unclear goal, lack of coordination, unclear or complicated plans, complex task organizations or command relationships, complicated technologies); the self-induced ones are the team's to act on (Ch 1, "Friction"). |

## Phase 3: Insight / cause analysis (the *why*, the system, the recurring pattern)

| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| Refuse the "root cause" framing | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-retro.md` | Cause-as-construction; *networked causality* replaces root cause; cause "is always something we create by recreating the event" (Appendix B) — scales down to retro level. |
| Refuse counterfactual reasoning | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-retro.md` | "If this person had done X..." is the forbidden move; learn why people did what they actually did, not what hindsight suggests. |
| Apply Five Whys with surprise-as-progress-signal | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | At a retrospective: ask "why" five times (give or take); "if you're rarely surprised by your root causes, you may not be digging deep enough." |
| Apply Five Whys from the Open Practice Library | Open Practice Library | `open-practice-library-retro.md` | OPL Five Whys practice: keep asking why until you find the real reason; when the answer is time, money or resources, ask why the process failed instead. |
| Test the recurring pattern against system archetypes | SSDL, Systems Thinking Foundations (Brief 1.07) | `ssdl-systems-thinking-foundations-retro.md` | Five archetypes — Fixes that Fail, Success to the Successful, Shifting the Burden, Drifting Goals, Limits to Growth. Hypothesis-generators, not labels. |
| Build a CLD for the recurring problem | Barbrook-Johnson & Penn, Systems Mapping | `barbrook-johnson-systems-mapping-retro.md` | When the team needs a picture: causal loop diagram surfaces feedback loops producing the pattern. |
| Map mental models of the recurring problem | SSDL, Systems Thinking Foundations (Brief 1.03) | `ssdl-systems-thinking-foundations-retro.md` | Each participant holds partial-but-valid model; surface partial models *before* discussing solutions. |
| Redirect blame language to system | NHS Improvement, Just Culture Guide | `nhs-just-culture-guide-retro.md` | *Action singling out an individual is rarely appropriate*; default-to-system prior surfaces in any retro where blame language is rising. |
| Re-read Norm Kerth's Prime Directive when blame surfaces | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | The Prime Directive is structural blameless-by-default commitment; especially important when blame language re-surfaces mid-retro. |
| Apply attribution-bias frame to participant accounts | OpenStax, Organizational Behavior | `openstax-organizational-behavior-retro.md` | Fundamental attribution error (underestimating situational causes, overestimating personal ones) pushes accounts toward individual blame; self-serving bias credits success to the team and failure to people outside the room (Ch 3.3). Redirect to conditions before individuals. |
| Apply confirmation-bias diagnostic | OpenStax, Psychology 2e | `openstax-psychology-2e-retro.md` | Confirmation bias "focuses on information that confirms existing beliefs" (Ch 7.3, Table 7.3): a team that has already decided what the problem is reads the board to confirm it; name the disconfirming sticky and ask the group to account for it. |
| Apply hindsight-bias diagnostic | OpenStax, Psychology 2e | `openstax-psychology-2e-retro.md` | Hindsight bias contaminating retro accounts; surface and bracket. |
| Detect a local fix for a systemic cause | Open Kanban | `open-kanban-retro.md` | "No single part of a system can ever bring overall improvement"; ask whether the insight points to a local symptom or a systemic pattern. |
| Detect drift on team norms / Definition of Done | Schwaber & Sutherland, The Scrum Guide | `scrum-guide-2020-retro.md` | Definition of Done is one of the five retro-inspection domains; if the DoD was not honoured during the Sprint, surface why as a process question, not a blame question. |
| Detect software-team measurement-driven framing | Jones, Evidence-Based Software Engineering | `jones-evidence-based-sweng-retro.md` | Goodhart's Law (measurement collapses under control pressure); cone-of-uncertainty as artefact; anchoring to a stakeholder's number; estimate peaks at multiples of seven hours (unit choice shifts the number). |
| Diagnose team dynamics stage (Tuckman) producing contested accounts | OpenStax, Principles of Management | `openstax-principles-management-retro.md` | A storming team (members vying for leadership, choosing sides) may give contested data; read that as the stage, not pathology. Name the stage before treating the symptom. |
| Diagnose Five Dysfunctions pattern in insight phase | OpenStax, Principles of Management | `openstax-principles-management-retro.md` | When artificial harmony (fast consensus, no disagreement) or a recurring problem shows up: test whether the chain (absence of trust → fear of conflict → lack of commitment → avoidance of accountability → inattention to results) explains it; naming the dysfunction locates the lever. |
| Name the ethical dimension of a recurring practice | OpenStax, Business Ethics | `openstax-business-ethics-retro.md` | When the retro surfaces a practice that harms someone outside the team (user, downstream colleague, customer), name it as an ethical gap — not just a process gap. |
| Check for safe-channel absence when problems went unreported | OpenStax, Business Ethics | `openstax-business-ethics-retro.md` | If a known problem was not surfaced in previous retros, ask what raising it would have cost and whether an internal channel existed (Ch 7.5). |
| Name the archetype mismatch precisely when recurring impediment is structural | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-retro.md` | "We are a CAPS-2 archetype ... being asked to deliver CAPS-3 outcomes ...; the cross-silo handoff that produces our recurring impediment is the structural mismatch, not a process problem." Precision beats vague "siloed" or "cross-functional issues" language. |
| Distinguish 15%-experimentable from structural-escalation | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-retro.md` | When team is naming structural impediments: which moves are genuinely within the team's locus of control (15% Solutions), and which would require changing the archetype itself — which the team cannot do unilaterally? |
| Detect the topology-mismatch pattern producing the recurring topic | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-retro.md` | Is this a Resource-drag pattern (utilisation pressure blocking end-to-end ownership)? A Delivery-bloat pattern (features unvalidated against outcome)? Name the pattern. |
| Apply local-optimisation test to proposed experiments | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-retro.md` | Before committing to multiple individually-defensible experiments, test: will they combine to improve the system goal, or will they compete? Primer: "If each element (e.g. policies, structures) is optimized in isolation, the performance of the whole system may actually decline." |
| Blame language surfacing | U.S. Marine Corps, MCDP 1: Warfighting | `mcdp1-warfighting-retro.md` | Critique rule: focus "not so much on the actions we took as on why we took those actions and why they brought the results they did" (Ch 3, "Training"). Pair with the NHS default-to-system prior and LFUO's counterfactual rule. |

## Phase 4: Experiment design (one or two owned experiments)

| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| Hold the one-or-two-experiments discipline | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | Field Guide: *"It's better to have one or two improvement items for the next Sprint than to have too much to change at once."* One or two changes at a time, not a list. |
| Limit the experiment list | Open Kanban | `open-kanban-retro.md` | Reduce the Batch Size practice: commit to the one or two experiments the team can finish; leave the rest on a visible backlog. |
| Split improvements into decisions vs actions | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | Decisions = changes to Definition of Done / Definition of Ready / Working Agreement; actions = new Backlog Items. Different mechanisms register different commitments. |
| Refuse adjournment without named owner | Liberating Structures Handbook | `liberating-structures-handbook-retro.md` | LS Discovery & Action Dialogues' closing question: *"Who will do what when next?"* — surfacing solutions and volunteers in one structure. |
| Resolve decision-rights ambiguity in experiment ownership | Letaw, Handbook of Software Engineering Methods | `letaw-handbook-sweng-methods-retro.md` | RACI matrix when ownership is ambiguous; the matrix is the artefact that registers the agreement. |
| Reduce batch size of the proposed experiment | Open Kanban | `open-kanban-retro.md` | "Reduce the Batch Size of your Efforts"; run the smallest version of the experiment that still tests the hypothesis; limiting WIP (here, concurrent experiments) is a consequence of batch-size reduction, not the other way around. |
| Refuse overwork commitments | Open Kanban | `open-kanban-retro.md` | Respect-for-people value pairs sustainable pace with Lean's Muri 無理; an exhausted team is "the perfect recipe for disaster". |
| Surface latent dissent before commit | Letaw, Handbook of Software Engineering Methods | `letaw-handbook-sweng-methods-retro.md` | Fist of five six-level voting before commit — *two or fewer fingers is the cue to stop, discuss and re-vote*; surfaces latent dissent the meeting tone is suppressing. |
| Frame the experiment as Design of Experiments | Open Practice Library | `open-practice-library-retro.md` | The hypothesis is named; the pass criterion is named; the measures and learning are named. |
| Refuse copy-without-principles | Open Practice Library | `open-practice-library-retro.md` | Establish Shared Principles practice; the experiment is grounded in the underlying principle, not just the surface practice. |
| Apply capacity-adjusted velocity discipline | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | When experiment will compete with delivery commitment for Sprint capacity: if carried-over work in process meets or exceeds forecast velocity and is all still valuable, *"we strongly recommend against taking in any new work this Sprint"* (Sprint Planning); commit only to experiments the team has real capacity for. |
| Apply Disagree and Commit when team is stuck | Open Practice Library | `open-practice-library-retro.md` | Against consensus-as-requirement; the experiment is committed to even if not unanimously endorsed; the disagreement is named, not buried. |
| Apply Locke goal-theory criteria to experiment design | OpenStax, Principles of Management | `openstax-principles-management-retro.md` | Specific, stretching, accepted and committed-to (Locke) plus measurable and time-bound (SMART); vague experiments are non-commitments. Apply these criteria before adjourning. |
| Design for SDT autonomy — team chooses, not manager assigns | OpenStax, Principles of Management | `openstax-principles-management-retro.md` | SDT: intrinsic motivation requires autonomy; assigned experiments produce lower follow-through than team-chosen ones. If an experiment must be assigned, build in modification latitude. |
| Choose the change model that fits the experiment scope | OpenStax, Principles of Management | `openstax-principles-management-retro.md` | Lewin (stable, incremental), Kotter (urgency-framed, top-down), Cooperrider AI (abundance-based, bottom-up), CAS (self-organising). Match the model to the change's complexity and power distribution. |
| Name the ethical dimension before committing to an experiment | OpenStax, Business Ethics | `openstax-business-ethics-retro.md` | When the experiment crosses stakeholder boundaries — affecting users, customers, or colleagues outside the team — name it as an obligation (ethical minimum / maximum), not just an option. |
| Frame team-level experiments as topology-adjacent moves | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-retro.md` | Even within the existing archetype, what experiment moves the team rightward (broader skill mandate) or upward (broader work mandate) on the OT axes by a small amount? These are the genuine 15% moves available inside the current archetype. |
| Frame structural moves as escalation-with-evidence | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-retro.md` | If the insight is structural, the experiment isn't a team experiment — it's an escalation. Design it: who to, what evidence to attach (the OT mapping itself), what precise request (a structural experiment, not a permission or complaint). |
| Defend against framework-recommendation as retro experiment | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-retro.md` | "We should adopt SAFe / LeSS / Team Topologies" as a team-level retro experiment is the cargo-cult failure mode. Reframe: what topology do we need, and what concrete archetype change moves us toward it? |
| Use the Elevating-Kata-as-experiment framing for structural escalations | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-retro.md` | Structural escalations should propose experiments, not decisions: a defined small change with a named hypothesis, a check-point, and a re-mapping plan. This matches the retro experiment discipline (one or two owned experiments per retro). |
| Five experiments on the board | U.S. Marine Corps, MCDP 1: Warfighting | `mcdp1-warfighting-retro.md` | Main effort: recognise one action "as the most critical to success at that moment"; the others support it or wait (Ch 4, "Main effort"). Pairs with the Field Guide's one-or-two rule. |
| Give each experiment a purpose, not only a task | U.S. Marine Corps, MCDP 1: Warfighting | `mcdp1-warfighting-retro.md` | Commander's intent: "Of the two, the intent is predominant"; state the experiment as "[task] in order to [purpose]" so the owner can adapt when the task stops fitting (Ch 4, "Commander's intent"). |

## Phase 5: Close (commitments, gratitude, take-aways)

| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| Close with What/So What/Now What | Liberating Structures Handbook | `liberating-structures-handbook-retro.md` | LS three-question sequence ending on Now-What with named next step; the closing structure when team needs a shape. |
| Apply the retro close: appreciations and meta-retrospective | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | Field Guide wrap-up: appreciations, then a few minutes retrospecting on the retrospective ("How did it go for the team? What would they like to try next time?"). |
| Compress the take-away to six words | Liberating Structures Handbook | `liberating-structures-handbook-retro.md` | LS Six Words exercise — Mulago Foundation criteria (<8 words, verb, target population, measurable outcome); surface what's load-bearing. |
| Apply TC 25-20 closing-comments rule scaled down | US Army, TC 25-20 | `tc-25-20-army-aar-retro.md` | Leader summarises key points, ends positively, links to next iteration, then leaves so team can discuss in private. |
| Reinforce modelling-as-through-line | FLO Facilitation Guide | `flo-facilitation-guide-retro.md` | The lead and coach model the practices they want the team to adopt, through the close: the lead models curiosity, the coach models transparent facilitation. |
| Mark experiment-not-done case for next-retro review | Gagné, The Approach Perfect Field Guide to Scrum Events | `approach-perfect-field-guide-scrum-events-retro.md` | Capture each improvement where it will be seen: a Backlog Item for the next Sprint, or a change to the DoD, DoR or Working Agreement. Next retro's experiment review (Phase 0.5) names each one done or not done before new data. |
| Address closing-safety-check 1-2 | FLO Facilitation Guide | `flo-facilitation-guide-retro.md` | Counsel-out discipline scales down: a participant who seems deeply struggling gets a private conversation after the retro, not a public prompt during it. |
| Confirm learning-as-precondition-for-improvement | Open Kanban | `open-kanban-retro.md` | "Learning is the key concept before continuous improvement can ever happen!"; Retrospectives are one of the source's named ways to run Learn and Improve Continuously; the experiment is downstream of learning, so confirm the team can say what it now understands that it didn't before. |
| File the retro output to the team's tracker (or markdown fallback) | Open Practice Library | `open-practice-library-retro.md` | Retrospective practice's outputs: action items / experiments to track; bound capability is `issue-tracker`, unbound is markdown. |
| Confirm the PDCA Act step is named before close | OpenStax, Principles of Management | `openstax-principles-management-retro.md` | The retro is the Check step; Act must be named (owner, date, next Plan input) before the session closes. Unnamed Act = Check without consequence. |
| Cross-link to AAR axis when an event surfaces in retro | (cross-axis) | (`aar` axis — see [[aar]]) | When the retro surfaces a specific incident the team wants to learn from in cross-functional shape, route to AAR. |
| Schedule the next OT re-mapping as a structural-check cadence | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-retro.md` | When structural escalation or archetype-mismatch work is in flight, close by naming when the team will re-MAP the archetype. Quarterly is defensible; tie it to a calendar date. "Periodic re-mapping with Org Topologies is an easy and fast way to complete a learning loop of feedback and adapting." |

## Reference categories

The references below are listed by Pass G applicability fire. Strong-fire references produce a substantive distillation; moderate-fire produces a focused distillation on the specific retro moment; light-fire produces a thin distillation routing cross-axis where the source has more material.

**Strong fire (canonical retrospective methodology, demo-corpus version):**

- `approach-perfect-field-guide-scrum-events-retro.md` — Sprint Retrospective in its six-segment Derby-Larsen form; Norm Kerth's Retrospective Prime Directive verbatim; Vegas / Chatham House rules; √n voting; 5-Whys with the surprise check; one-or-two-improvements discipline; decisions-vs-actions split; capacity-adjusted velocity; appreciations and a meta-retrospective at the close.
- `scrum-guide-2020-retro.md` — Sprint Retrospective as one of the four inspect-and-adapt events inside the Sprint; team inspects individuals / interactions / processes / tools / Definition of Done; 3h timebox for monthly Sprint.
- `open-practice-library-retro.md` — Retrospective practice with multiple shapes; Blameless Postmortem; Five Whys; Establish Shared Principles; 1-2-4-All; Disagree and Commit; Design of Experiments; Evals; Human-in-the-Loop.
- `liberating-structures-handbook-retro.md` — 1-2-4-All, Troika, Wise Crowds, What/So What/Now What, 15% Solutions, Discovery & Action Dialogues, Mini Constellations, TRIZ, Wicked Questions, Q Storming, Levels of Accountability, Impromptu Speed Networking and Knee-to-Knee openers, Six Words.

**Strong fire (cause analysis & systemic framing):**

- `nhs-just-culture-guide-retro.md` — default-to-system framing for blame language; five-test decision tree as background discipline.
- `lfuo-learning-review-guide-2024-retro.md` — counterfactual prohibition; Five Hows; cause-as-construction; networked causality.
- `ssdl-systems-thinking-foundations-retro.md` — five briefs covering complex-problem characteristics, mental models, feedback thinking with CLDs, accumulations, system archetypes; recurring-problem diagnostic substrate.
- `barbrook-johnson-systems-mapping-retro.md` — CLDs and Theory of Change as shared-model artefacts when *recurring problem* needs a picture.

**Strong fire (facilitation craft):**

- `flo-facilitation-guide-retro.md` — facilitative-vs-direct-teaching framing; *Anxious-Annie* facilitator-anxiety pattern; Vegas-rules privacy; engagement-equity tracking; resist-thoroughness in feedback; no-pressuring-tone discipline.

**Strong fire (experiment / action discipline):**

- `open-kanban-retro.md` — learning-as-precondition for continuous improvement; Holistic / Systemic value (Deming + Goldratt borrowed-through); batch-size reduction; sustainable-pace; waste as a named category; communication vs collaboration.
- `letaw-handbook-sweng-methods-retro.md` — fist of five, RACI, INVEST scaled to experiment design.

**Moderate fire (organisational / team substrate):**

- `tc-25-20-army-aar-retro.md` — discovery vs critique on epistemic grounds; train-to-weakness; closing-comments rule.
- `openstax-organizational-behavior-retro.md` — group dynamics, conflict types, communication models, perception biases, decision-making biases.
- `openstax-principles-management-retro.md` — PDCA, Tuckman stages, motivation frameworks for the *helpless team* diagnostic, Lencioni's Five Dysfunctions, Follett's integration path, change-management models, Locke goal theory.
- `openstax-psychology-2e-retro.md` — hindsight bias and the other decision biases (availability, anchoring, confirmation), attribution errors, reconstructive memory, social influence (Asch conformity, groupthink), motivation and stress.
- `jones-evidence-based-sweng-retro.md` — Goodhart's Law, cone-of-uncertainty as artefact, anchoring; useful for software-team retros where measurement framing is in play.

**Light fire (specific contexts):**

- `openstax-business-ethics-retro.md` — accountability frames when retro surfaces ethical exposure.

**Light fire (vocabulary and structural-classification tool — narrow applicability):**

- `org-topologies-primer-2025-retro.md` — Krivitsky, Larman & Flemm, *Strategic Org Design: The Primer* (CC BY-NC-SA 4.0). The Primer is *not* a retrospective-facilitation text and does not address ceremony structure, safety check, or data-gathering methodology. It is reached for as a *vocabulary* and *structural-vs-process classification* tool for the team-archetype-mismatch subset of recurring retro topics: when the same impediment surfaces three or more retros running and team-level experiments are not moving the needle. Principal applicability: Phase 0.5 (structural-repeat detection), Phase 1 (OT-mapping as priming activity when structural recurring topic suspected), Phase 3 (archetype-mismatch precise naming; 15%-vs-structural distinction; topology-mismatch pattern detection), Phase 4 (framing team-level experiments as topology-adjacent moves; structural escalation design; defence against framework-recommendation experiments; Elevating-Kata-as-experiment framing), Phase 5 (schedule next OT re-mapping as structural-check cadence). Phase 0 and Phase 2 receive no OT rows.

**Moderate fire (review stance and error climate from military doctrine):**

- `mcdp1-warfighting-retro.md` — U.S. Marine Corps, *MCDP 1: Warfighting* (1997). Public domain (US Government work); scope=open. Not a retrospective method: it gives the lead a stance, and the mechanics come from the method sources. Ch 3 critique discipline (review even after success and promptly, all hands encouraged to contribute, candour depends on the tolerance of whoever holds authority, focus on why actions were taken); Ch 3 error climate (no "zero defects" mentality, leniency for errors of boldness, severity for errors of inaction carried into the retro as a topic rather than a sanction, honest dissent before a decision and support after it); Ch 4 main effort and commander's intent for experiment design; Ch 1 self-induced friction as a delta-sorting prompt. Principal applicability: Phase 0, 0.5, 2, 3, 4.

**Pass G skip (no retro-relevant content; routed cross-axis):**

- `openstax-accounting-vol1`, `openstax-accounting-vol2` — accounting; route to `decision-making` and `software-business`.
- `openstax-business-law` — law; route to `decision-making`.
- `openstax-economics-3e` — economics; route to `decision-making`.
- `openstax-entrepreneurship` — entrepreneurship; route to `decision-making`.
- `openstax-introduction-business` — intro business; route to `decision-making`.
- `openstax-principles-finance` — finance; route to `decision-making`.
- `openstax-principles-marketing` — marketing; route to `decision-making`.

---

## Anti-patterns this index helps avoid

- **Skipping the Prime Directive.** Norm Kerth's *"regardless of what we discover..."* is the structural blameless-by-default commitment; especially important when blame language is anticipated. Read it aloud.
- **Five experiments on the board.** A long list spreads the team's effort. Field Guide one-or-two discipline + Open Kanban batch-size reduction.
- **Counterfactual creep.** LFUO's forbidden move scales down to retro level; redirect to *why people did what they actually did*.
- **Single-cause framing for a recurring problem.** SSDL system archetypes are hypothesis-generators, not labels; LFUO networked-causality replaces root cause.
- **Verbal-first input.** Field Guide written-first input (positives, deltas and insights on individual sticky notes before discussion); FLO engagement-equity tracking. Writing before talking keeps the first voice from setting the field.
- **Adjourning without named owner.** LS Discovery & Action Dialogues' *"Who will do what when next?"* is the structural refusal.
- **Mid-incident routing as retro.** Retro is iterative team-internal; if event-triggered cross-functional, route to [[aar]].
- **Source-integrity papering-over.** When the participant names a canonical retro author (Kerth, Derby & Larsen, Deming, Goldratt, Senge), surface that the framing is carried borrowed-through the Field Guide / Open Kanban / SSDL and the demo cannot cite directly.
- **Treating last retro's unfulfilled experiment as a team-failure.** TC 25-20 *real benefits come from applying results*: if ownership of the experiment was ambiguous, the experiment design failed, not the team (the TC retro distillation's reading).
- **Manager-on-call dominating early.** FLO engagement-equity tracking and its coach-to-lead ask that the manager listen, not evaluate, and speak last + Field Guide strict participant control (invited only by the entire Scrum Team; support, not steer) — operationalise both.
