# Retrospective Facilitation (demo corpus)

**Slug:** `retro`
**Purpose:** Coach a lead engineer through a 45-60 minute team retrospective on Teams / Meet / Zoom (or in person): real-time, written-first, ending with one or two owned experiments. The audience is a lead with no facilitation training: Claude coaches, the lead reads prompts and pastes chat output back, the team does the thinking.

## 1. Problem statement

A team retrospective is a high-stakes, frequently-mishandled meeting. The team's chance to act on what just happened is rationed by safety, sequencing, and the lead's facilitation skill. Most retros default to flat lists of complaints, a few generic actions, and zero follow-through. This task axis projects the demo corpus onto the question the lead is actually holding in the moment (*"low safety, what now"*, *"blame language surfacing, redirect how"*, *"five action items on the board, which one matters"*) and routes to the framework that prices that move.

The retro axis is co-equal with the [[aar]] axis but routes for *iterative team learning* rather than *post-incident review*: regular cadence rather than event-triggered, team-internal rather than cross-functional, future-oriented experiments rather than incident-grounded actions. The canonical retrospective and team-effectiveness literature is closed-licence and absent from the demo. The demo's coverage of the same discipline runs through Gagné's *Approach Perfect Field Guide to Scrum Events* (Sprint Retrospective in canonical 5-segment form with Norm Kerth's Prime Directive, Vegas / Chatham House rules, √n voting), the *Scrum Guide 2020* (Sprint Retrospective as one of the five events), the *Open Practice Library* (Retrospectives practice, Blameless Postmortem, Five Whys, Establish Shared Principles, Psychological Safety), the *Liberating Structures Handbook* (1-2-4-All, Troika, Wise Crowds, What/So What/Now What, 15% Solutions, Discovery & Action Dialogues), the *FLO Facilitation Guide* (engagement-equity tracking, *Anxious-Annie* pattern, Vegas-rules privacy), the *LFUO Learning Review Implementation Guide* (Five Hows for recurring problems, counterfactual prohibition, just-culture as substrate), the *NHS Just Culture Guide* (NPSA-Incident-Decision-Tree blameless framing), and the *SSDL Systems Thinking Foundations* briefs (system archetypes for the *recurring problem* diagnostic). The demo cannot cite the canonical retrospective authors directly; it carries the discipline they carry through Open Practice Library, SSDL (open-licence Senge-tradition substitute), Open Kanban (open-licence constraint-thinking substitute), and the Field Guide (Norm Kerth's Prime Directive verbatim).

## 2. Practitioner questions

- The team scored 1-2 on safety check. Do I run the retro anyway, or address safety first?
- The same topic has surfaced three retros in a row. What changes how we treat it?
- The lead engineer wants to fix everything; how do I help them pick one constraint?
- Blame language is surfacing (*"if X had just..."*); how do I redirect without shaming?
- The team is helpless (*"nothing we can do"*); how do I open the response zone?
- The team agrees too quickly. How do I surface artificial harmony?
- One voice dominates; what protocol re-balances participation?
- A manager is on the call; how do I coach them to speak last?
- The last retro's experiments weren't done; how do I learn from that, not punish it?
- The team feels overwhelmed by AI tool adoption. What corpus surfaces?
- A counterfactual is being treated as analysis (*"if the build hadn't broken on Tuesday..."*); how do I redirect?

## 2a. Runtime listener grain

**Trigger unit:** an operator-described moment inside an in-progress retrospective (a phase, a signal, a stuck pattern). Generic *"how do I run a retro"* framings route to the Field Guide Sprint Retrospective section (`approach-perfect-field-guide-scrum-events`) directly; the axis fires on situated diagnostic moments.

**Response unit:** the framework, activity, or facilitation move from the corpus that addresses the moment, plus the phase context that determines *when* it fires (Phase 0 setup, Phase 0.5 experiment review, Phase 1 priming, Phase 2 data gathering, Phase 3 insight, Phase 4 experiment design, Phase 5 close).

### Seed trigger→response table

The full per-phase routing tables are authored at [`distillations/retro/RETRO-DISTILLATION-INDEX.md`](../distillations/retro/RETRO-DISTILLATION-INDEX.md); the seeds below are the load-bearing rows the index inherits.

**Phase 0, Setup** (working agreement, safety check, confidentiality rule, Prime Directive)

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| Lead opens the retro | Norm Kerth's Retrospective Prime Directive read out loud at every retro: *"Regardless of what we discover, we understand and truly believe that everyone did the best job they could..."* (`approach-perfect-field-guide-scrum-events`) |
| Lead asks how to set confidentiality | Vegas Rule (unanimous explicit consent before sharing) or Chatham House Rule (information shared, identities not). Pick one explicitly (`approach-perfect-field-guide-scrum-events`); FLO Vegas-rules framing for online retros (`flo-facilitation-guide`) |
| Safety check returns 1-2 | Establish Shared Principles before content; Open Practice Library psychological-safety practice as the precondition (`open-practice-library`); LFUO administrative-firewall framing scales down to retro level (`lfuo-learning-review-guide-2024`) |
| Lead names manager on call | FLO engagement-equity tracking matrix (`flo-facilitation-guide`); Field Guide *manager speaks last* convention (`approach-perfect-field-guide-scrum-events`) |
| Lead wants to skip the Prime Directive | Refuse. Norm Kerth's Prime Directive is the structural blameless-by-default commitment; especially important when blame language is anticipated (`approach-perfect-field-guide-scrum-events`) |

**Phase 0.5, Experiment review** (what did we say last time, what happened)

| Trigger | Response |
|---|---|
| Last retro's experiments weren't done | TC 25-20 *real benefits come from applying results* principle scales down: review without punishment; if the experiment was unowned, the experiment design failed, not the team (`tc-25-20-army-aar`); LS 15% Solutions to reframe locus-of-control (`liberating-structures-handbook`) |
| Experiments were done, results unclear | Open Practice Library Design of Experiments practice; LFUO learning-and-validation discipline (`open-practice-library`, `lfuo-learning-review-guide-2024`) |
| Same experiment proposed three retros running | SSDL system archetypes (fixes that fail or shifting the burden may be in play); surface as hypothesis, not label (`ssdl-systems-thinking-foundations`) |
| Experiment crossed into structural-change territory | Open Kanban Holistic / Systemic value (Deming + Goldratt borrowed-through): "no single part of a system can ever bring overall improvement". Escalate to leadership rather than retry at team level (`open-kanban`) |
| Team is allergic to "experiments" framing | OPL Design of Experiments vocabulary swap; Establish Shared Principles to surface why the word lands wrong (`open-practice-library`) |

**Phase 1, Priming** (set the topic frame, surface energy, choose retro shape)

| Trigger | Response |
|---|---|
| Lead asks which retro pattern to use | Field Guide 5-segment Derby-Larsen pattern is the default; sample agenda concrete enough to facilitate (`approach-perfect-field-guide-scrum-events`); Open Practice Library Retrospective practice for alternative shapes (`open-practice-library`) |
| Team is low energy | FLO calibration-of-facilitator-presence to phase (`flo-facilitation-guide`); LS Impromptu Speed Networking or Knee-to-Knee Conversation as opener (`liberating-structures-handbook`) |
| Team is mid-incident, not mid-iteration | Route to [[aar]] axis instead; retro is iterative-team-internal, not incident-cross-functional |
| Team is overwhelmed by AI tool adoption | Establish Shared Principles + Open Practice Library Evals practice for AI overconfidence; Human-in-the-Loop practice against silent AI delegation (`open-practice-library`) |
| Lead is anxious about facilitating | FLO *Anxious-Annie* pattern: facilitator anxiety is one's own pattern, not participant problem; trust the process (`flo-facilitation-guide`) |

**Phase 2, Data gathering** (positives, deltas, insights)

| Trigger | Response |
|---|---|
| One voice dominates | LS 1-2-4-All milling design that refuses HiPPO-driven discussion; Open Practice Library 1-2-4-All practice (`liberating-structures-handbook`, `open-practice-library`) |
| Written-first vs verbal-first | Field Guide chat-waterfall convention; each team member writes positives / deltas / insights individually on stickies; group like items; vote on top 3 to deep-dive (`approach-perfect-field-guide-scrum-events`); FLO equitable-engagement framing (`flo-facilitation-guide`) |
| Team agrees too quickly | LS Mini Constellations to surface positional diversity by spatial positioning (`liberating-structures-handbook`); SSDL mental-models brief: each participant holds partial-but-valid model (`ssdl-systems-thinking-foundations`) |
| Categorisation collapses to two buckets | LS What/So What/Now What three-question sequence imposes structure on the raw data (`liberating-structures-handbook`) |
| Team is helpless ("nothing we can do") | LS 15% Solutions locus-of-control reframe (Gareth Morgan borrowed-through): *"Where do you have freedom to act? What's in your 15%?"* (`liberating-structures-handbook`) |

**Phase 3, Insight / cause analysis** (the *why*, the system, the recurring pattern)

| Trigger | Response |
|---|---|
| Lead asks for root cause | LFUO position: cause is constructed, not discovered; *networked causality* replaces root cause; FLAs must avoid causal statements (scales down to retro level) (`lfuo-learning-review-guide-2024`); Field Guide *5 Whys with surprise as the signal*: "If you're rarely surprised by your root causes, you may not be digging deep enough" (`approach-perfect-field-guide-scrum-events`) |
| Counterfactual creeping in | LFUO forbidden-move list: learn why people did what they actually did, not why they did not do what hindsight suggests (`lfuo-learning-review-guide-2024`) |
| Same pattern reappearing 2+ retros | SSDL system archetypes as hypothesis-generators (fixes that fail, success to the successful, shifting the burden, drifting goals, limits to growth); test, do not label (`ssdl-systems-thinking-foundations`); Barbrook-Johnson CLD for shared-model construction when the team needs a picture (`barbrook-johnson-systems-mapping`) |
| Blame language surfacing | NHS default-to-system framing; *action singling out an individual is rarely appropriate* (`nhs-just-culture-guide`); Norm Kerth's Prime Directive re-read out loud (`approach-perfect-field-guide-scrum-events`) |
| Surprise root-cause emerges | Field Guide: *surprise is the signal of progress* (`approach-perfect-field-guide-scrum-events`); OpenStax OB attribution-bias and confirmation-bias diagnostics (`openstax-organizational-behavior`) |

**Phase 4, Experiment design** (one or two owned experiments)

| Trigger | Response |
|---|---|
| Five experiments on the board | Field Guide *one or two improvement items for the next Sprint* discipline; too much change at once dilutes every experiment (`approach-perfect-field-guide-scrum-events`); Open Kanban Theory-of-Constraints-borrowed-through framing: find the one constraint (`open-kanban`) |
| Experiments lack owners | LS Discovery & Action Dialogues' closing question: *"Who will do what when next?"*; refuse adjournment without named owner (`liberating-structures-handbook`); Letaw RACI matrix for ambiguous decision rights (`letaw-handbook-sweng-methods`) |
| Experiment is too big | Open Kanban batch-size reduction value: smaller stories, fewer concurrent items per stage (`open-kanban`); Field Guide INVEST-style discipline scaled to experiment design (`approach-perfect-field-guide-scrum-events`) |
| Improvement is a decision, not an action | Field Guide split: decisions = changes to DoD / DoR / Working Agreement; actions = new Backlog Items; different mechanisms register different commitments (`approach-perfect-field-guide-scrum-events`) |
| Team wants to commit beyond capacity | Field Guide capacity-adjusted velocity discipline; Open Kanban sustainable-pace value (Muri / overburden refused) (`approach-perfect-field-guide-scrum-events`, `open-kanban`) |

**Phase 5, Close** (commitments, gratitude, take-aways)

| Trigger | Response |
|---|---|
| Lead doesn't know how to close | Field Guide retro-close pattern: read back commitments, name owners, name when each lands (`approach-perfect-field-guide-scrum-events`); LS What/So What/Now What ending on Now What with named next step (`liberating-structures-handbook`) |
| Take-away unclear | LS Six Words exercise (compress to <8 words to surface what's load-bearing); useful for the *one thing* this retro decided (`liberating-structures-handbook`) |
| Lead wants to thank the team | TC 25-20 closing-comments rule scales down: leader summarises, ends positively, links to next iteration, leaves so team can debrief in private (`tc-25-20-army-aar`); FLO modelling-as-through-line (`flo-facilitation-guide`) |
| Lead asks how to remember what to bring to next retro | Open Practice Library Retrospective + Establish Shared Principles practices for working-agreement maintenance (`open-practice-library`); Open Kanban *learning-as-precondition-for-continuous-improvement* (`open-kanban`) |
| Team scored 1-2 on closing safety check | Address safety before next retro; LFUO post-event-readback discipline scales down (`lfuo-learning-review-guide-2024`); FLO counsel-out discipline (`flo-facilitation-guide`) |

## 3. Available sources

All Pass-G-applicable demo distillations in `distillations/retro/` are candidates; per-source applicability decided by `creating-distillations` Pass G during ingestion.

**Strong fire (canonical retrospective methodology, demo-corpus version):**

- `approach-perfect-field-guide-scrum-events`: Sprint Retrospective in canonical Derby-Larsen 5-segment form; Norm Kerth's Retrospective Prime Directive verbatim; Vegas Rule / Chatham House Rule confidentiality choice; √n voting heuristic; 5-Whys with *surprise as the signal*; one-or-two-improvements-per-Sprint discipline; decisions-vs-actions split; capacity-adjusted velocity. The corpus's closest-to-canonical retrospective source.
- `scrum-guide-2020`: Sprint Retrospective as one of five canonical events; team inspects individuals, interactions, processes, tools, Definition of Done; identifies most impactful changes; 3h timebox for monthly Sprint.
- `open-practice-library`: Retrospective practice with multiple shapes; Blameless Postmortem with information-availability + psychological-safety foundations; Five Whys; Pre-mortem / Backcasting; Establish Shared Principles (against copy-without-principles); 1-2-4-All (against HiPPOs); Disagree and Commit (against consensus-as-requirement); Blameless Postmortem (against blame); Evals + Human-in-the-Loop (against AI overconfidence and silent delegation).
- `liberating-structures-handbook`: 1-2-4-All, Troika Consulting, Wise Crowds, What/So What/Now What (named *After Action Debrief* in the handbook, with Center for Creative Leadership attribution), 15% Solutions, Discovery & Action Dialogues (closing on *Who will do what when next?*), 25-to-10, Mini Constellations, TRIZ, Wicked Questions, Simple Rules, Six Words.

**Strong fire (cause analysis & systemic framing):**

- `nhs-just-culture-guide`: default-to-system framing for blame language; five-test decision tree (used as background discipline, not a primary retro move).
- `lfuo-learning-review-guide-2024`: counterfactual prohibition; Five Hows; cause-as-construction; networked causality; recommendations-vs-lessons-learned distinction scaled down to retro level.
- `ssdl-systems-thinking-foundations`: five briefs covering complex-problem characteristics, mental models, feedback thinking with CLDs, accumulations, system archetypes. The retro projection treats the archetypes as recurring-problem diagnostics.
- `barbrook-johnson-systems-mapping`: Causal Loop Diagrams and Theory of Change as shared-model artefacts when the retro's *recurring problem* needs a picture.

**Strong fire (facilitation craft):**

- `flo-facilitation-guide`: facilitative-vs-transmissive question framing; *Anxious-Annie* facilitator-anxiety pattern; Vegas-rules privacy; engagement-equity tracking; resist-thoroughness in feedback; no-pressuring-tone discipline; UDL accessibility lens.

**Strong fire (experiment / action discipline):**

- `open-kanban`: learning-as-precondition for continuous improvement; Holistic / Systemic Approach value (Deming + Goldratt borrowed-through) for one-constraint focus; batch-size reduction; sustainable-pace (Muri refused); pull-based scheduling. The corpus's open-licence Goldratt-tradition substitute for the *find the one constraint* discipline.
- `letaw-handbook-sweng-methods`: fist of five for surfacing latent dissent before commitment; RACI matrix for ambiguous decision rights; INVEST for retro-experiment quality.

**Moderate fire (organisational / team substrate):**

- `tc-25-20-army-aar`: discovery vs critique on epistemic grounds; train-to-weakness; closing-comments rule; the AAR-vs-critique framing transfers when the retro borders on incident review.
- `openstax-organizational-behavior`: group dynamics, conflict types, communication models, perception biases, decision-making biases. The behavioural substrate for the facilitator's diagnostic vocabulary.
- `openstax-principles-management`: PDCA, change management, organisational-design primitives (Mintzberg, six structures) when retro insights surface structural questions, motivation frameworks for the *helpless team* diagnostic.
- `openstax-psychology-2e`: hindsight bias, perception, memory, social-influence (Asch conformity, normative vs informational influence) for the facilitator's diagnostic vocabulary.
- `jones-evidence-based-sweng`: evidence-based discipline (Goodhart's Law, cone-of-uncertainty as artefact, anchoring to customer's number); useful in software-team retros where measurement-driven framing is in play.

**Light fire (specific contexts):**

- `openstax-business-ethics`: accountability frames when retro surfaces ethical exposure.

**Pass G likely skip (no retro-relevant content):**

- `openstax-accounting-vol1`, `openstax-accounting-vol2`, `openstax-business-law`, `openstax-economics-3e`, `openstax-entrepreneurship`, `openstax-introduction-business`, `openstax-principles-finance`, `openstax-principles-marketing`. Each is routed cross-axis.

## 4. Intended lenses

The demo lens library carries `builder`, `agentic-builder`, `pm-bounded-by-ba-role`, `cto`, `business-executive-stakeholder`, and `chris-gagne-consultant-coach`. Of these:

- `cto`: moderate fire. When retro insights surface structural / org-design questions that need executive translation.
- `business-executive-stakeholder`: moderate fire. When the lead needs to escalate a team-level insight to leadership in language the leadership will hear.
- `pm-bounded-by-ba-role`: moderate fire. When a PM-bounded role is participating in the retro and the role's constraints are part of the diagnostic.

Per-distillation applicability decided at Pass G.

## 4a. Intended runtime agents

The retro task ships with a `retro-facilitator` agent that hosts:

- The seven-phase coaching loop (Phase 0 setup; Phase 0.5 experiment review; Phase 1 priming; Phase 2 data gathering; Phase 3 insight; Phase 4 experiment design; Phase 5 close).
- The Norm Kerth Prime Directive read-aloud at every retro.
- The Vegas / Chatham House confidentiality choice as an explicit Phase 0 step.
- The chat-waterfall written-first input pattern.
- The one-or-two-experiments discipline (Goldratt-borrowed-through via Open Kanban).
- The decisions-vs-actions split (Field Guide).
- The counterfactual / blame-language / artificial-harmony refusal list.

The agent is invoked by the operator command `/retro-facilitate`.

## 5. Overlap

- **Significant with `aar`** on the cause-analysis phase (Phase 3). The same sources (LFUO 2024, NHS Just Culture, SSDL, Liberating Structures, Open Practice Library) fire on both axes. The retro projection sharpens to *team-internal iterative learning* (the team retrospects on itself); the AAR projection sharpens to *cross-functional post-incident review* (the org learns about an event). Same sources, different framings. Cross-link [[aar]] for the event-triggered side.
- **Moderate with `decision-making`** on the experiment-design phase. The same sources project differently: decision-making's projection covers the decision discipline broadly; retro's projection sharpens to *commit one or two experiments the team owns*. Integration-section updates expected in the decision-making distillations of Field Guide, Scrum Guide, Open Practice Library, Liberating Structures, Open Kanban.
- **Moderate with `stakeholder-engagement`** on the leadership-escalation move. When a retro insight crosses team-level authority, the same Mitchell-Agle-Wood / Grunig-Hunt scaffolding applies.
- **Light with `software-business`** on software-team retros where measurement and capacity decisions are in play. Jones distillation may need integration-section update for retro-mode reading.

## 6. Success criteria

A lead engineer with no facilitation training can run a 45-60 minute retro with Claude coaching them through the seven phases, ending with one or two experiments owned by individuals and tracked in the team's tracker (or as markdown in the unbound fallback). Team safety score does not drop across the retro; lead reports the retro felt different from previous ones; at least one experiment from a prior retro is reviewed in the experiment-review phase of the next retro.

The falsifier: an LLM-judge eval comparing retro-axis answers on a held-out set of retro-prompts against (a) the demo's `decision-making` axis applied to the same prompts and (b) the same model running raw on the same prompts. Bar: 60% of test queries cite the Field Guide + Open Practice Library + Liberating Structures together, with the trigger→response routing visibly different from the decision-making projection of the same sources.

## Discipline

- **The team does the thinking.** The lead facilitates. Claude coaches. The team owns the experiments. The runtime agent never produces experiments the team did not propose.
- **Written-first, always.** Chat waterfall as default input. Equalises non-native speakers, introverts, and high-power-distance cultures. FLO's engagement-equity framing reinforces this.
- **One constraint.** Five experiments mean zero follow-through. Open Kanban's Holistic / Systemic value (Deming + Goldratt borrowed-through) carries the *find the one constraint* discipline; the demo cannot cite Goldratt directly.
- **Prime Directive every time.** Norm Kerth's *"regardless of what we discover, we understand that everyone did the best job they could..."* is read out loud at every retro, especially when blame language surfaces. The Field Guide carries this verbatim.
- **No counterfactuals.** LFUO's forbidden move scales down to retro level. State the rule out loud at the start when the team is mid-incident retrospective. Redirect to why people did what they actually did.
- **Source-integrity gap-honesty.** When a participant or reader names a canonical retrospective or systems-thinking author the demo does not hold directly, surface that the framing is carried borrowed-through Field Guide / Open Practice Library / Liberating Structures / SSDL / Open Kanban. Do not paper over the absence; direct citation of those authors is not available in this open distribution.
- **Pass G owns per-distillation applicability.** The source set in §3 is the candidate set; Pass G decides which retro distillation each source produces.
- **Runtime listener grain.** The seed trigger→response tables in §2a name what fires the corpus in the moment. The runtime listener table is the *micro-router* (query mentions an observable trigger, framework fires); the phase-routing table is the *macro-router* (query mentions a phase, candidate distillations follow). Both ship.

## Author anchors

- Gagné, *The Approach Perfect Field Guide to Scrum Events* (2020): Sprint Retrospective in canonical 5-segment Derby-Larsen form with Norm Kerth's Prime Directive verbatim; the corpus's closest-to-canonical retrospective source; CC BY 4.0.
- Schwaber & Sutherland, *The Scrum Guide* (November 2020): Sprint Retrospective as one of the five canonical events; CC BY-SA 4.0.
- Red Hat Open Innovation Labs community, *Open Practice Library*: community-curated practice catalogue including Retrospectives, Blameless Postmortem, Five Whys, Establish Shared Principles; CC BY 4.0.
- Heft & Pattillo (compilers), *Engaging Everyone with Liberating Structures Handbook* (2010): ~32 LS designs; Center-for-Creative-Leadership-attributed What/So What/Now What named as *After Action Debrief*; CC BY-NC-SA 3.0.
- Hurtado, *Open Kanban*: the corpus's open-licence Goldratt-tradition substitute via the Holistic / Systemic Approach to Change value (Deming + Goldratt explicitly cited); CC BY 3.0.

**What the demo does NOT carry (not openly redistributable):** the canonical retrospective and team-effectiveness literature. The discipline is carried borrowed-through the open sources named in §4 above.
