
# Open Practice Library (light reference)

**Source:** Open Practice Library (Red Hat Open Innovation Labs community, 2016–present). 266 community-curated practice pages at `openpracticelibrary.com`. Licence: **CC BY 4.0** for content. Cloned from `https://github.com/openpracticelibrary/openpracticelibrary` at commit `8bfa450e75dfba1e2a3c68ac0e514e587f6f116e` on 2026-05-13.
**Structure:** Collection-as-source. 266 markdown practice pages organised by `mobiusTag` frontmatter across four phases: **Foundation** (111), **Discovery** (86), **Options** (32), **Delivery** (37). Each practice carries uniform YAML frontmatter (title, subtitle, mobiusTag, tags, authors, difficulty, time, people, participants) and three body fields (whatIs, whyDo, howTo). Cross-practice hyperlinks form the collection's internal compositional graph. Complete coverage; nothing omitted.

## Author's Thesis (condensed)

The Open Practice Library is the collective practice-knowledge of a community of practitioners working in agile delivery, DevOps, design thinking, product discovery, and team facilitation, contributed and moderated through an open-source pull-request workflow. Its central editorial framing is the **Mobius Loop**: every practice carries a `mobiusTag` of *foundation* (team and substrate), *discovery* (why and who), *options* (what to try), or *delivery* (build and measure). The library is not an alphabetical catalogue — it is a Mobius-Loop-shaped catalogue, with the per-practice tag as the first-order signal of when in the work cycle the practice applies.

The library's most self-aware contrarian is its own *Establish Shared Principles* practice, which warns that practices ride on values and principles underneath, and that copying the visible practices of a successful organisation without adopting the principles that originated them does not reproduce the result. The library is a library of practices that knows the limits of practice libraries. The community's editorial intent is "to move past the buzzwords to deliver real business value, quickly" — and to do so by giving practitioners named, reusable, adaptable primitives rather than canonical procedures.

## The collection's shape

| Phase | Count | Share | Reading |
|---|---|---|---|
| Foundation | 111 | 42% | Team-and-culture practices + technical-substrate practices that hold *across* the loop. |
| Discovery | 86 | 32% | Framing why-and-who: opportunity, problem, customer, alignment. |
| Options | 32 | 12% | What to try: ideation, prioritisation, experimentation. |
| Delivery | 37 | 14% | Build and measure: engineering cadence, reliability, feedback. |

Distribution is deliberately weighted toward Foundation — the curators are saying that culture and substrate are where most of the practice work lives.

## Foundation phase

Four sub-clusters:

- **Facilitation primitives.** 1-2-4-All, Affinity Mapping, Check-ins, Confidence Voting, Dot Voting, Lean Coffee, Ice Breakers, Quote Wall. Recurring shape: silent generation → small-group convergence → large-group integration. Time-boxed, participant-equalising, visual-output-producing.
- **Culture and psychological safety.** Social Contract, Elephant in the Room, Celebrating Failure, Measuring Psychological Safety, Mood Marbles, Niko Niko Calendar, GROW Model for 1-2-1 Coaching, Mentorship, Pair/Mob Programming. The cluster argues team psychological safety is produced by named repeatable rituals, not exhortation.
- **Technical-substrate engineering.** Continuous Integration → Continuous Delivery → Continuous Deployment; GitOps; Everything-as-Code; Containers; Test Automation, TDD, BDD; Defence in Depth; Threat Modeling; C4 Architecture; Architectural Decision Records (ADR); Bytesize Architecture Sessions; Emerging Architecture. The library treats the engineering substrate as foundational, not as something added later.
- **Meta-practices.** Establish Shared Principles (the principles-over-practices contrarian); Evals (AI output quality, "evals give you confidence, not certainty"); Human in the loop (HITL/HOTL/HIC); Theory of Constraints; Westrum's Cultural Typology; Open Decision Framework and the Open Organization practices.

## Discovery phase

Four sub-clusters:

- **Opportunity framing.** Lean Canvas (Ash Maurya, derived from Osterwalder's Business Model Canvas); North Star Framework (Sean Ellis; seven-point metric checklist); Jobs to be Done (Tony Ulwick; drill-bit example); 5 Elements Canvas; 6 Dimensions of Discovery; Strategy Design (Corporate Forest metaphor).
- **Problem-space exploration.** 5 Whys (Taiichi Ohno, Toyota; ask why the process failed, not just why); Cynefin Framework (Snowden; Clear / Complicated / Complex / Chaotic / Confused with named responses); Abstraction Laddering; Is – Is not – Does – Does not (Paulo Caroli's Lean Inception); Backcasting / Pre-mortem (Klein / Kahneman); Force Field Analysis (Lewin); PESTEL, SWOT, Stacey Matrix, Wardley Mapping.
- **Customer and stakeholder understanding.** Empathy Mapping (Dave Gray, XPLANE); User Persona, Proto-Persona; Stakeholder Map (Power × Interest); Stakeholder Mapping (concentric circles); Stakeholder RACI Map; Stakeholders Interview; AEIOU Observation Framework; Emotional Journey; Experience Mapping; Service Blueprint; Domain Storytelling; Event Storming (Alberto Brandolini, 2013).
- **Strategic alignment.** Start With Why (Sinek); Vision/Mission Statements; OKRs; Impact Mapping (Gojko Adzic, 2012; against the "shopping list of features"); Start At The End (from *The Sprint Book*); MSPOTs, V2MOMs, NCTs, MBOs; Lean Value Tree; Independent Service Heuristics (Team Topologies).

## Options phase

Three sub-clusters:

- **Ideation.** 10-for-10; Crazy 8s; Silent Brainstorming; Idea Cyclone; Alternative Worlds; How Might We; Creativity Warmups (Torrance Test of Creative Thinking); Design Sprint (5-day customer-centric process); Lean Inception; Experiment Canvas.
- **Prioritisation.** $100 Prioritisation; MoSCoW; Impact-Effort Matrix; How-Now-Wow Matrix; RICE Scoring Model; Dot Voting; Eisenhower Box (urgent × important); Weighted Shortest Job First (WSJF); VUE your priorities; Priority Sliders; Kanban Priorities.
- **Experimentation and decision framing.** Design of Experiments (hypothesis / current condition / target / obstacles / pass / measures / learning); Minimum Viable Product; Dark Launches; Split Testing (A/B); Disagree and Commit (the consensus-is-not-required contrarian); Dissent Cards (Marquet's *Leadership is Language*); Example Mapping (yellow/blue/green/red four-colour sticky structure).

## Delivery phase

Three sub-clusters:

- **Cadence practices.** Scrum (3 roles / 5 events / 3 artifacts in OPL's framing); Iteration (Sprint) Planning; Daily Standup (yesterday/today/blockers; "be careful it doesn't drift into a status update"); Retrospectives (multiple formats: 4Ls, Rose Thorn Bud, Plus Minus Interesting, Realtime, Design Retro Active, Futurespective); Showcase / Sprint Review; Kanban (visualise / limit WIP / manage flow / make policies explicit; "Stop starting, start finishing"); Story Kick-offs; Story RePointing; Backlog Refinement.
- **Reliability and safety.** Blameless Postmortem ("our job is not to point fingers"); Chaos Engineering; Risk Radar; Canary Release (caged-bird metaphor); Blue Green Deployments; Feature Toggles; Security Checklist (SafeStack); Wheel-of-Misfortune; Fire Drills.
- **Feedback and learning.** Cohort Analysis; Funnel Analysis (Ries's innovation accounting); Split Testing A/B and Multivari; Usability Testing; Guerilla Testing; Heuristic Evaluation; Cognitive Walkthrough; Agile Health Check; Burnup Chart; Code Review (McConnell on collective ownership; Atwood on egoless programming).

## The cross-practice link graph

The library is a graph, not a list. Practices reference one another as compositional building blocks: 1-2-4-All inside $100 Prioritisation; Affinity Mapping inside 6 Dimensions of Discovery and Empathy Mapping and Rose Thorn Bud and many others; Five Whys inside Retrospectives; Disagree and Commit pairing with Dissent Cards; Dark Launches contrasted with Canary Release and A/B Testing inside its own body; Blameless Postmortem pointing forward to Wheel-of-Misfortune. The internal-link graph is the library's third structural layer (after Mobius phase and tag) and carries semantic content about which practices belong *together*.

## The "Tips for Remote Working" pattern

A recurring sub-heading inside many practice `howTo` bodies. The library has been maintained through the 2020–2023 shift to remote work and the practices were updated rather than deprecated. Marker of editorial continuity.

## Per-practice metadata as the library's API

Every practice has the same frontmatter shape: title, subtitle, templateKey, date, authors (a contribution history, not a byline), tags, mobiusTag, icon, whatIs, whyDo, howTo, difficulty, people, time, participants, mediaGallery, resources. The uniformity is the library's API — it lets the catalogue be mechanically queried, re-indexed, and re-rendered without per-practice parsing logic. The contribution workflow ("hit the Improve or Add new button to launch the CMS; login with your GitHub Account; update with your changes and append your github username to the authors list") is itself an instance of several practices in the library — Docs As Code, Everything-as-Code, Continuous Delivery.

## Key Connections (borrowed-through, in the library)

The library's practices cite a wide external lineage. Named explicitly inside practice bodies:

- Liberating Structures (1-2-4-All).
- Taiichi Ohno / Toyota (Five Whys).
- Kurt Lewin (Force Field Analysis).
- Jean Tabaka, *Collaboration Explained* (Confidence Voting).
- Sir John Whitmore (GROW Model).
- Dave Gray / XPLANE (Empathy Mapping).
- Alberto Brandolini (Event Storming, 2013).
- Gojko Adzic (Impact Mapping, 2012).
- Sean Ellis (North Star Metric); Amplitude (playbook).
- Tony Ulwick (Jobs to be Done).
- Simon Sinek (Start With Why); Theodore Levitt (drill-bit); Seth Godin (*This Is Marketing*); Dan Pink (*Drive*).
- *The Sprint Book* / GV (Start At The End; Design Sprint).
- Dave Snowden (Cynefin Framework — implicit through named domains).
- L. David Marquet, *Leadership is Language* (Dissent Cards; pattern in Disagree and Commit).
- Gary Klein (HBR), Daniel Kahneman (*Thinking Fast and Slow*) (Backcasting / Pre-mortem).
- Ash Maurya, Alexander Osterwalder (Lean Canvas; Business Model Canvas).
- Matthew Skelton and Manuel Pais / Team Topologies (Independent Service Heuristics; Cognitive Loadometer).
- John Sweller, *Cognitive Load Theory* (Cognitive Loadometer).
- Eric Ries, *The Lean Startup* (Funnel Analysis; innovation accounting).
- Steve McConnell, *Code Complete*; Jeff Atwood (Code Review).
- Andrej Karpathy (Evals, "march of nines").
- 1979 IBM internal training slide via Simon Willison (Human in the loop, "a computer can never be held accountable").
- Red Hat People Team (Open Decision Framework).
- Gen. McChrystal (Group Launch Facilitation, "gardener" leadership).

## Signature Contrarian Positions (named in practice bodies)

1. **Against HiPPOs (Highest Paid Person's Opinion).** Silent-generation patterns across many facilitation practices, named explicitly in 1-2-4-All.
2. **Against consensus-as-requirement.** Disagree and Commit: "collaboration eventually requires consensus; it does not. In fact consensus can come at a very high cost to the team dynamic."
3. **Against the "shopping list of features".** Impact Mapping and Start At The End: outcomes over outputs.
4. **Against blame in incident response.** Blameless Postmortem: "our job is not to point fingers."
5. **Against output-measurement when outcome is the question.** OKRs: measure desired outcomes and impact, i.e. results, not tasks completed.
6. **Against treating non-improvements as success.** Design of Experiments: successful experiments are those that provide statistically significant data, not those that confirm a hypothesis.
7. **Against copying practices without principles.** Establish Shared Principles: the library's most self-aware contrarian.
8. **Against status-update standups.** Daily Standup: the main point is alignment, not status.
9. **Against AI overconfidence in evaluation.** Evals: evals give you confidence, not certainty.
10. **Against silent AI delegation in high-stakes work.** Human in the loop: a computer must never make a management decision.
