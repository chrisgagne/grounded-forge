
# Open Practice Library, deep reference

**Source:** Open Practice Library (Red Hat Open Innovation Labs community, 2016–present). 266 community-curated practice pages at `openpracticelibrary.com`. Licence: **CC BY 4.0** for content (site-level declaration). Cloned from `https://github.com/openpracticelibrary/openpracticelibrary` at commit `8bfa450e75dfba1e2a3c68ac0e514e587f6f116e` on 2026-05-13.
**Scope:** open
**Structure:** A collection-as-source: 266 markdown practice pages organised by `mobiusTag` frontmatter across four phases — **Foundation** (111 practices; team/cultural practices that span the loop), **Discovery** (86 practices; why and who), **Options** (32 practices; what to try), **Delivery** (37 practices; build and measure). Each practice carries uniform YAML frontmatter (`title`, `subtitle`, `mobiusTag`, `tags`, `authors`, `difficulty`, `time`, `people`, `participants`) and three body fields (`whatIs`, `whyDo`, `howTo`). Cross-practice hyperlinks form the collection's internal graph.
**Citation style:** `(Practice "Title", "Section")` — section is one of `whatIs` / `whyDo` / `howTo`, plus the practice's named subheadings where present. The source has no chapter or page anchors; the practice file is the citation unit, with the frontmatter `title:` and the body section as the locator. For frontmatter facts (tags, mobiusTag, difficulty, time) the citation is `(Practice "Title", frontmatter)`. For collection-level counts (e.g., "111 Foundation practices") the citation is `(Collection metadata)` and the count is verifiable from a grep over the corpus.
**Coverage:** Collection coverage is complete for the cloned commit — all 266 practice files were ingested into the converted markdown without omission. Verbatim citation coverage is *sampled* across the four phases; the protocol does not quote-verbatim every practice (266 × ~1500 words is too much for a single deep reference). Paraphrase coverage with `[AP]` markers reaches across the major clusters in each phase; specific practices in each cluster are named so the reader can trace to the source.

## Author's thesis (paraphrased from source)

The Open Practice Library is the collective practice-knowledge of a community of practitioners working in agile delivery, DevOps, design thinking, product discovery, and team facilitation, contributed and moderated through an open-source workflow. Its central editorial claim, stated on the site's `learn` page, is: "**Move past the buzzwords to deliver real business value, quickly. The Open Practice Library is an open source, community-driven inspired library of best practices and tools. It helps individuals, teams and entire businesses figure out the optimal ways to get to the best outcome.**" [V] (site copy, `src/pages/learn.js`).

A second load-bearing claim is **purposeful framing through the Mobius Loop**. Every practice in the library carries a `mobiusTag` of *foundation*, *discovery*, *options*, or *delivery* — the four regions of the Mobius Loop process model. The library is not an alphabetical catalogue; it is a Mobius-Loop-shaped catalogue, and the `mobiusTag` per practice is the curation's first-order signal of *when* in the work cycle the practice applies [AR] (Collection metadata, evidenced by `mobiusTag` frontmatter on every practice). Foundation practices (111) are the team-and-culture-and-technical-substrate practices that hold across the loop; Discovery practices (86) frame the *why* and the *who*; Options practices (32) frame the *what to try* (ideas, experiments, prioritisation); Delivery practices (37) frame the *build-and-measure* engineering and feedback loop.

A third load-bearing claim is **practices over principles, but principles over practices**. The library's name and stated editorial intent foregrounds *practices* — "practices that empower teams to collaborate and deliver iteratively" [V] (`src/pages/learn.js`) — yet one of the practices itself, *Establish Shared Principles*, makes the contrarian case that the practices visible above the waterline ride on values, principles, and purpose underneath: "Organizations that have done the work to articulate 'why they exist and what they believe' then need to clearly explain the 'how they will act' they will work before they move to the 'what they will do'" [V] (Practice "Establish Shared Principles", "What is it?"). The same practice asserts "Purpose, Values, and Principles are enduring but practices evolve and change over time. Blindly following practices are not encouraged" [V] (Practice "Establish Shared Principles", "Why do it?") [AR]. The library, in other words, knows it is a library of practices and warns the reader against using it as one — copying the visible practices of a successful organisation without adopting the values and principles that originated them does not reproduce the result.

A fourth load-bearing claim is **the practice-page as a teaching artefact**, not as a workflow specification. Each practice's three body fields (`whatIs`, `whyDo`, `howTo`) are short — most practices fit on one printable page — and the `howTo` typically gives a numbered facilitation sequence with timeboxes and participant-role notes, not a complete procedure. The practices are intended to be picked up and adapted by a facilitator who already understands their team's context. The "Tips for Remote Working" section that recurs in many practices (e.g., 1-2-4-All, Empathy Mapping, Event Storming, Retrospectives) is a structural marker — the library assumes practices are being run by humans facing real constraints, and the tips section adapts the in-room shape to the distributed-team shape.

A fifth load-bearing claim is **the cross-practice hyperlink graph as substantive structure**. Practices reference one another not just as "see also" but as compositional building blocks: *$100 Prioritisation* recommends combining with *1-2-4-All* for facilitation [AP] (Practice "$100 Prioritisation", "Variations"); *Affinity Mapping* is invoked from inside *5 Elements Canvas*, *6 Dimensions of Discovery*, *AEIOU Observation Framework*, *Alternative Worlds*, *Rose Thorn Bud*, and many others; *Continuous Integration*, *Continuous Delivery*, and *Continuous Deployment* form a stacked sequence; *Dark Launches*, *Canary Release*, and *Blue Green Deployments* are explicitly compared against each other in their own bodies. The library is a graph, not a list — a reader using one practice is regularly pointed at adjacent practices that complete or extend it.

## Part I: The collection's shape (curatorial structure)

### Practice count by Mobius phase

| Phase | Practice count | Share | Curatorial reading |
|---|---|---|---|
| Foundation | 111 | 42% | The largest phase by count. Foundation = team-and-culture practices (Check-ins, Social Contract, GROW Coaching, Elephant in the Room) plus technical-substrate practices (Continuous Integration, Continuous Delivery, Containers, GitOps, Everything-as-Code, Defence in Depth) that hold *across* the loop. The library treats culture and engineering substrate as equally foundational. |
| Discovery | 86 | 32% | The second-largest. Discovery = framing why-and-who: opportunity (Lean Canvas, North Star Framework, Jobs to be Done), problem space (Empathy Mapping, 5 Whys, Cynefin Framework), customer (Persona, Stakeholder Map, AEIOU Observation), alignment (Start With Why, OKRs, Impact Mapping, Strategy Design, Vision Statement). |
| Options | 32 | 12% | The smallest. Options = what to try: ideation (10-for-10, Crazy 8s, Silent Brainstorming), prioritisation ($100 Prioritisation, MoSCoW, RICE, Dot Voting, Impact-Effort Matrix), experimentation (Design Sprint, Design of Experiments, Experiment Canvas, MVP), consensus (Disagree and Commit, Dissent Cards). |
| Delivery | 37 | 14% | Delivery = build and measure: engineering cadence (Iteration/Sprint Planning, Daily Standup, Retrospectives, Scrum, Kanban, Showcase), reliability (Blameless Postmortem, Chaos Engineering, Risk Radar), feedback (Canary Release, A/B Testing, Multivari Testing, Funnel Analysis, Cohort Analysis), engineering quality (Code Review, Test Automation, TDD, Security Checklist). |
| **Total** | **266** | **100%** | |

(Source: `mobiusTag` frontmatter on each of the 266 practice files at commit `8bfa450e75dfba1e2a3c68ac0e514e587f6f116e`; counts are mechanical, derivable from grep.)

The distribution is *deliberately weighted toward Foundation*. The library's curators are saying — by the count alone — that team culture and engineering substrate are where most of the practice work lives, and that the why-what-build phases are the more situational, fewer-but-sharper-tools tail [AR] (inferred from the count distribution).

### Tag taxonomy (within-phase classification)

A secondary classification layer is the `tags:` frontmatter field. Tag distribution across the 266 practices (top tags only; many practices carry multiple tags):

| Tag | Count | Cluster |
|---|---|---|
| `culture` | 75 | Team / culture / collaboration |
| `methods` | 50 | General methodology |
| `validate` | 36 | Discovery validation |
| `value` | 32 | Discovery value framing |
| `ideate` | 24 | Options ideation |
| `insight` | 20 | Options framing |
| `learn` | 18 | Delivery feedback |
| `measure` | 12 | Delivery / measurement |

(Source: `tags:` frontmatter; counts are mechanical.)

The `culture` tag is the most common — 75 practices, roughly two-thirds of which sit under Foundation. This is the curation's second weighting toward team culture as a load-bearing concern.

### Per-practice metadata fields (structural)

Every practice page has the same frontmatter shape, which makes the library mechanically queryable:

- `title` and `subtitle` — the practice's name and a one-line gloss.
- `templateKey: practice-page` — the Gatsby template (constant across practices, structurally meaningful for site rendering).
- `date` — the last modification date of the practice page.
- `authors:` — a list of GitHub handles of the contributors who have edited the practice. Per the upstream README, "Update it with your changes and remember to append your `github` username to the end of the authors list" [V] (`README.md`, "Content Writers", step 4) — so the author list is a *contribution history*, not a single byline.
- `tags:` — zero or more tags from a small controlled vocabulary (culture, methods, validate, value, ideate, insight, learn, measure).
- `mobiusTag` — exactly one of *foundation*, *discovery*, *options*, *delivery*.
- `icon:` — path to an image file (not ingested in this corpus).
- `whatIs:`, `whyDo:`, `howTo:` — three body fields, each a short prose block (typically 50-500 words).
- `difficulty:` — easy / moderate / hard.
- `people:` — recommended participant count (e.g., "2+", "5+", "8+").
- `time:` — recommended duration (e.g., "15 - 30 minutes", "~6 Hours not including breaks", "5 Days").
- `participants:` — a list of role-names recommended for the session.
- `mediaGallery:` and `resources:` — links to external videos, images, or articles. (Not the substantive content; treated as references.)

The uniformity of this metadata is editorial discipline, not coincidence — it lets the library be re-rendered, re-indexed, and re-queried by tools that do not understand any particular practice's body. The frontmatter is the practice's API.

### The contribution workflow as quality control

The library's quality control is an open-source pull-request workflow: "On a practice page or the home page hit the `Improve` or `Add new` button to launch the CMS … Update it with your changes and remember to append your `github` username to the end of the authors list. Make your changes and hit `Save`. The moderators will pick up the changes from there!" [V] (`README.md`, "Content Writers"). Moderation runs through a `staging` branch deployed to `staging.openpracticelibrary.com` before promotion to `main` [AP] (`README.md`, "Content Moderators"). This is the same lightweight CI/CD-for-content shape that several of the library's own practices recommend for software (*Docs As Code*, *Everything-as-Code*, *Continuous Delivery*) — the library's editorial process is one of its own practices.

## Part II: Foundation phase (111 practices)

Foundation practices are the team-and-culture and technical-substrate practices that hold *across* the Mobius loop — neither phase-specific nor task-specific. The phase divides loosely into four sub-clusters: facilitation primitives, culture/psychological-safety practices, technical-substrate engineering practices, and meta-practices about how to work.

### Sub-cluster 1: Facilitation primitives

The library treats facilitation as a craft with named, reusable primitives. Examples:

- **1-2-4-All.** "1-2-4-All is a way for every member of a large group to participate and generate ideas together. It is highly scalable and can be used for almost any group size" [V] (Practice "1-2-4-All", "What is it?"). The practice carries an explicit anti-HiPPO framing: "All voices are heard, incorporating 'silent' conversations and expanding input diversity - No more HiPPOs (Highest Paid Person's Opinion)!" [V] (Practice "1-2-4-All", "Why do it?") [AR]. Cited from the Liberating Structures collection.
- **Affinity Mapping.** "Affinity Mapping is a practice used to organize ideas or insights. It allows large numbers of ideas stemming from brainstorming to be sorted into groups, based on their natural relationships, for review and analysis" [V] (Practice "Affinity Mapping", "What is it?"). The practice is referenced from at least a dozen other practices as a downstream step after ideation.
- **Check-ins.** "Start each session or gathering by inviting everyone to speak in turn, uninterrupted, for an agreed amount of time" [V] (Practice "Check-ins", "What is it?"). The why is psychological-safety framing: "It gives everyone the opportunity to speak up and be heard. This prompts the behaviour and gives permission for each person to share their own insights, establishing a good foundation for psychological safety" [V] (Practice "Check-ins", "Why do it?") [AR].
- **Confidence Voting.** A 0–5-finger vote where "0 fingers (a fist): No way, terrible choice, I will not go along with it. A way to block consensus" [V] and "5 fingers: Absolutely, best idea ever! I'll champion it" [V] (Practice "Confidence Voting", "How to do it?"). Attributed to Jean Tabaka, *Collaboration Explained* (Practice "Confidence Voting", "How to do it?") [BT].
- **Ice Breakers, Hello-World event, I Have a Dream, Quote Wall, Tribute Wall, Yes! And…** — opening rituals for sessions and team-formation moments.
- **Lean Coffee.** "Lean Coffee started in Seattle in 2009 by Jim Benson and Jeremy Lightsmith. A structured, but agenda-less meeting. Participants gather, build an agenda, and begin talking" [V] (Practice "Lean Coffee", "What is it?") [BT].

The recurring facilitation primitives are *time-boxed*, *participant-equalising* (designed to prevent the HiPPO problem), and *visual-output-producing* (sticky notes, dot votes, affinity clusters). The library's facilitation default is silent generation → small-group convergence → large-group integration, repeated at multiple scales.

### Sub-cluster 2: Culture and psychological safety

- **Social Contract.** A team-authored agreement on ways of working (referenced from many other practices as a session opener).
- **Elephant in the Room.** "The 'Elephant in the Room' practice is a facilitated discussion technique designed to surface and address unspoken, uncomfortable, or sensitive issues that are impacting a group, team, or organization" [V] (Practice "An Elephant in the Room", "What is it?"). The practice's structure is explicit: *Preparation & Framing → Identifying the "Elephant(s)" → Prioritizing & Selecting → Facilitated Discussion → Action Planning & Follow-Up* [AP] (Practice "An Elephant in the Room", "How to do it?").
- **Celebrating Failure.** "We find it easy to celebrate and share our success stories. Celebrating failure is all about bringing the team together in an informal and safe environment, where team members can share stories of products that went wrong and the reasons why" [V] (Practice "Celebrating Failure", "What is it?").
- **Measuring Psychological Safety, Mood Marbles, Niko Niko Calendar, Team Sentiment.** Lightweight team-state measurement practices.
- **GROW Model for 1-2-1 Coaching.** Whitmore's GROW (Goal / Reality / Options / Will) framework, presented as a structuring tool for coaching conversations [AP] (Practice "GROW Model for 1-2-1 Coaching", "How to do it?") [BT to Whitmore].
- **Mentorship, Pair Programming, Mob Programming, Knowledge Sharing.** Practices that distribute tacit knowledge across the team.

The cluster reads as the library's argument that team psychological safety is not produced by exhortation but by *named, repeatable rituals* — check-ins, mood marbles, blameless conversation structures, opening icebreakers, and explicit social contracts. The library does not separate "soft" facilitation from "hard" engineering; both live in Foundation.

### Sub-cluster 3: Technical-substrate engineering practices

This sub-cluster is the largest in Foundation by content density and includes the library's coverage of the modern continuous-delivery toolchain:

- **Continuous Integration.** "With Continuous Integration (CI), developers submit small, frequent changes instead of large, infrequent changes. When another developer accepts the changes, automated tests and build steps run to ensure that the code works as expected" [V] (Practice "Continuous Integration", "What is it?").
- **Continuous Delivery.** "Continuous Delivery (CD) is an engineering practice where each change could be a potential release ready for production. This practice builds on top of the Continuous Integration practice as its starting point and adds to the end a step that releases artifacts for anyone to use" [V] (Practice "Continuous Delivery", "What is it?"). Explicit upward-pointer to Continuous Deployment.
- **Continuous Deployment.** "With Continuous Deployment (CD), the development team maintains software so that it can be released to production at any moment, specifically on demand" [V] (Practice "Continuous Deployment", "What is it?"). The CI → CD → Continuous Deployment chain is explicit in the source.
- **GitOps.** "GitOps is a pattern to manage the flow of work from development to production through Git operations" with the slogan "If it's not in Git, it's not real" [V] (Practice "GitOps", "What is it?" / subtitle).
- **Everything-as-Code.** "Everything as Code is the practice of treating all parts of the system as code. This means, storing configuration along with Source Code in a repository such as git or svn" [V] (Practice "Everything-as-Code", "What is it?").
- **Containers.** "A technical description of a Linux container is a sandboxed process or processes isolated on a VM or bare-metal server. These processes are isolated using the tried and tested mechanisms of Linux Namespacing, CGroups, and SELinux contexts" [V] (Practice "Container", "What is it?").
- **Test Automation, Test Driven Development, Behavior-Driven Development, Pair Programming, Ping-Pong Programming, Mob Programming.** Engineering quality practices.
- **Defence in Depth, Threat Modeling.** "Defence/defense in depth (sometimes referred to as 'layered security') is an approach to securing a system, service, or piece of software that focuses on including strong security controls on all layers of a stack or design, rather that focusing all effort on securing only the outward- or user-facing parts of the solution" [V] (Practice "Defence in Depth", "What is it?").
- **C4 Architecture, Architectural Decision Records (ADR), Bytesize Architecture Sessions, Emerging Architecture.** Architecture-as-craft practices.

This sub-cluster is the library's argument that the engineering substrate — CI/CD, containers, GitOps, security-by-design — is *foundational* to delivery, not something to be added later. The practices are tagged `methods` and `culture` rather than `delivery`, signalling the editorial position that these are habits of the team rather than activities of a sprint.

### Sub-cluster 4: Meta-practices (practices about practising)

- **Establish Shared Principles.** The contrarian practice that argues for "principles over practices" within a practice library (see Author's Thesis above). The iceberg metaphor — practices above the water, principles and values below — is explicit [AP] (Practice "Establish Shared Principles", "What is it?") with an embedded image reference.
- **Evals.** A 2026-era addition: "Evals are systematic methods for measuring the quality of AI and LLM outputs. They serve the same purpose as Test Automation — giving you confidence that your system behaves correctly — but they are fundamentally different. **Traditional tests give you certainty. Evals give you confidence.**" [V] (Practice "Evals", "What is it?") [AR]. Cites Karpathy's "march of nines" framing for confidence thresholds [BT] (Practice "Evals", "What is it?").
- **Human in the loop.** Same 2026 cohort: "Human-in-the-Loop (HITL) is a design pattern in which people remain actively involved in the decision-making process of an automated or AI-driven system. Rather than handing full control to a machine, a human reviews, approves, or corrects the system's output before it takes effect" [V] (Practice "Human in the loop", "What is it?"). Distinguishes three oversight models (HITL, HOTL, HIC) [AP] (Practice "Human in the loop", "What is it?").
- **The Theory of Constraints, The Matrix of Principles, Westrums Cultural Typology Assessment.** Frameworks-as-practices.
- **Open Decision Framework, Open Decision Making, Open Leader Persona, Open Leadership Mindset.** A set of practices contributed from the Red Hat *Open Organization* tradition.

## Part III: Discovery phase (86 practices)

Discovery practices frame the why-and-who: opportunity recognition, problem space, customer understanding, and alignment. Four sub-clusters: opportunity framing, problem-space exploration, customer/stakeholder understanding, and strategic alignment.

### Sub-cluster 1: Opportunity framing

- **Lean Canvas.** "A Lean Canvas is a one-page document that captures key information about your future product. The Lean Canvas is frequently used by Entrepreneurs and Lean Startups" [V] (Practice "Lean Canvas", "What is it?"). Nine-section canvas: Problem, Target Customer, UVP, Solutions, Channels, Revenue, Cost, Key Metrics, Unfair Advantage [AP] (Practice "Lean Canvas", "How to do it?"). Attributed to Ash Maurya, based on Osterwalder's Business Model Canvas [BT].
- **North Star Framework.** "The North Star Framework is a model for managing products by identifying a single, crucial metric known as the North Star Metric. According to Sean Ellis, who coined this term, this is the single metric that best captures the core value that your product delivers to customers" [V] (Practice "North Star Framework", "What is it?") [BT to Sean Ellis]. Seven-point checklist for what a North Star Metric is (expresses value; represents vision and strategy; leading indicator; actionable; understandable; measurable; not a vanity metric) [AP] (Practice "North Star Framework", "Why do it?").
- **Jobs to be Done.** "Jobs to be Done (JTBD) is an approach in product and service development that focuses on understanding the fundamental needs that motivate consumers to purchase or use a particular product" [V] (Practice "Jobs to be Done", "What is it?"). Attributed to Tony Ulwick [BT]. The canonical drill-bit example: "a person might 'hire' an electric drill not because they want a drill, but because they need to make holes in the wall to hang a picture" [V] (Practice "Jobs to be Done", "What is it?") [AE].
- **5 Elements Canvas, 6 Dimensions of Discovery.** Multi-perspective opportunity-framing canvases (Development / Operations / Leadership / Product / Architecture; People & culture / Tools & technologies / Process / Communication / Work environment / Governance).
- **Strategy Design.** A multi-component strategic-framing practice using the "Corporate Forest" metaphor (Giant Oak / Fast Redwood / Maple Tree / Dogwood / Wildflowers / Ferns; Bees / Birds / Mushrooms; Invasive Kudzu / Fire / Strangler Fig) [AP] (Practice "Strategy Design", "How to do it?") — a sustained nature metaphor for competitive-landscape mapping.

### Sub-cluster 2: Problem-space exploration

- **5 Whys.** "The 'Five Whys' is a way to figure out what causes a problem. You keep asking 'why' until you find the real reason. It was made up by Taiichi Ohno at Toyota" [V] (Practice "Five Whys (5 Whys)", "What is it?") [BT to Ohno]. The car-won't-start example is canonical [AE] (Practice "Five Whys (5 Whys)", "Why do it?"). The practice carries the contrarian: "It's important to look for a process that's not working well or not there at all. Sometimes people will say the problem is not enough time, money, or resources. But we can't control those things. So, we should ask why the process failed instead of just asking why" [V] (Practice "Five Whys (5 Whys)", "Why do it?") [AR].
- **Cynefin Framework.** Snowden's framework for "categorizes situations into five domains: Clear, Complicated, Complex, Chaotic, Confused/Aporetic" [AP] (Practice "Cynefin Framework", "What is it?") [BT to Snowden]. Each domain has its named response pattern (Sense-Categorize-Respond; Sense-Analyze-Respond; Probe-Sense-Respond; Act-Sense-Respond) [V] (Practice "Cynefin Framework", "How to do it?").
- **Abstraction Laddering.** "Abstraction Laddering is a problem-framing activity that has participants reconsider problem statements by broadening or narrowing its focus" [V] (Practice "Abstraction Laddering", "What is it?").
- **Is – Is not – Does – Does not.** A four-quadrant problem-definition practice, attributed to Paulo Caroli's Lean Inception methodology [BT] (Practice "Is – Is not – Does – Does not", "What is it?").
- **Backcasting / Pre-mortem.** "Premortem is an analytical / thought experiment technique … The method originates from Gary Klein (HBR article) and was made popular by the Nobel price winner Daniel Kahneman in his book 'Thinking Fast and Slow'" [V] (Practice "Backcasting / Pre-mortem", "What is it?") [BT to Klein, Kahneman]. The technique: imagine the project has failed and reconstruct the reasons [AP] (Practice "Backcasting / Pre-mortem", "What is it?").
- **Force Field Analysis (Lewin).** Forces FOR change vs forces AGAINST change, scored on a 1-5 scale [AP] (Practice "Force Field Analysis - Force Field Map", "How to do it?") [BT to Kurt Lewin].
- **PESTEL Analysis, SWOT Analysis, Stacey Matrix, Wardley Mapping.** Framework-driven analysis practices.

### Sub-cluster 3: Customer and stakeholder understanding

- **Empathy Mapping.** "An empathy map is a collaborative tool used to develop insight into customers, users, etc. … The Empathy map has been created as a practice by Dave Gray of XPLANE" [V] (Practice "Empathy Mapping", "What is it?") [BT to Gray]. Senses captured: "what the person is seeing, thinking, doing and feeling" [V] (Practice "Empathy Mapping", "What is it?").
- **User Persona, Proto-Persona.** Persona artefacts at two depths of formality.
- **Stakeholder Map.** "It is a practice that helps you to understand more about your customer, mapping stakeholders and agreeing ways of communicating with different teams/people. The target outcome is to have a stakeholder map and a communication plan" [V] (Practice "Stakeholder Map", "What is it?"). The mapping shape is Power × Interest (or Power × Sentiment) [AP] (Practice "Stakeholder Map", "How to do it?").
- **Stakeholder Mapping (Mobius Outcome Delivery).** A variant using concentric circles (Primary / Secondary / Other Stakeholders) rather than a 2D quadrant [AP] (Practice "Stakeholder Mapping (Mobius Outcome Delivery)", "What is it?").
- **Stakeholder RACI Map.** RACI (Responsible / Accountable / Consulted / Informed) applied to stakeholder roles [AP] (Practice "Stakeholder RACI Map", "What is it?").
- **Stakeholders Interview.** Structured one-on-one interview practice for understanding what stakeholders want and need from a product [AP] (Practice "Stakeholders Interview", "What is it?").
- **AEIOU Observation Framework.** "AEIOU stands for: A - Activities, E - Environments, I - Interactions, O - Objects, U - Users. This heuristic framework provides an observation technique used to document contextual inquiries during ethnographic studies" [V] (Practice "AEIOU Observation Framework", "What is it?") [BT to Rick E. Robinson].
- **Emotional Journey, Experience Mapping, Service Blueprint, Domain Storytelling, Event Storming.** Customer-journey-and-process-modeling practices. Event Storming is "a rapid, interactive approach to business process discovery and design that yields high quality models. It was introduced in a blog by Alberto Brandolini in 2013" [V] (Practice "Event Storming", "What is it?") [BT to Brandolini]. The output: shared understanding, scope/boundaries, UI screen inventory, Aggregate inventory [AP] (Practice "Event Storming", "What is it?").

### Sub-cluster 4: Strategic alignment

- **Start With Why.** "Start with why is a practice to discover your organisation's or your personal why. The 'Why' is within you and finding your 'Why' is a process of discovery, not invention" [V] (Practice "Start With Why", "What is it?") [BT to Simon Sinek]. The practice cites Theodore Levitt's drill-bit observation (relayed through Seth Godin) and Dan Pink's *Drive* (autonomy / mastery / purpose) [BT].
- **Vision Statement, Mission Statements, Raison d'être, Why do we exist.** Purpose-articulation practices.
- **Objectives & Key Results (OKRs).** "OKRs are a collaborative goal-setting framework for organisations, teams and individuals to set challenging, ambitious goals with measurable results. OKRs have two parts: The Objective - The what. The Key Result - The how" [V] (Practice "Objectives & Key Results (OKRs)", "What is it?"). Nine-point Good Objectives guidance (outcome focussed; inspiring; ambitious but achievable; qualitative; time bound; clear and memorable; limit to 5; owned by team; support company mission) [AP] (Practice "Objectives & Key Results (OKRs)", "How to do it?").
- **Impact Mapping.** "Impact Mapping is an engaging, graphical, strategic planning technique. It was introduced by Gojko Adzic in 2012" [V] (Practice "Impact Mapping", "What is it?") [BT to Adzic]. The technique reorients planning away from "a 'shopping list of features,' as Gojko calls them. Even though the features are delivered, often the business objective is not achieved" [V] (Practice "Impact Mapping", "Why do it?") [AR]. Cites David Marquet's "leadership by intent" [BT].
- **Start At The End.** "Start At The End is a simple exercise to identify a set of assumptions which must be tested in order achieve a long term goal … The technique is derived from Chapter 4 of The Sprint Book" [V] (Practice "Start At The End", "What is it?") [BT to The Sprint Book].
- **MSPOTs, V2MOMs, NCTs, MBOs.** Goal-setting frameworks (Mission/Strategy/Plays/Omissions/Targets; Vision/Values/Methods/Obstacles/Measures; Narrative/Commitment/Task; Management by Objectives).
- **Lean Value Tree, Outcome Mapping, Where to Start.** Hierarchy-of-outcome practices.
- **The Big Picture, Threat Modeling, Independent Service Heuristics (ISH).** Architecture-and-system framing practices. ISH is from Team Topologies (Skelton and Pais) [BT] (Practice "Independent Service Heuristics (ISH)", "What is it?").

## Part IV: Options phase (32 practices)

Options practices answer *what to try*. Three sub-clusters: ideation, prioritisation, and experimentation framing.

### Sub-cluster 1: Ideation

- **10-for-10.** "The 10 for 10 workshop helps teams to think quickly and objectively and be focussed with their prioritisation. It's lightweight, fun and super useful!" [V] (Practice "10-for-10", "Why do it?"). The shape: 5 minutes ideation → 1 minute self-prune to top 10 → stick all top-10s → dot-vote → re-order [AP] (Practice "10-for-10", "How to do it?").
- **Crazy 8s, Silent Brainstorming, Idea Cyclone, Alternative Worlds, How Might We.** Convergent-divergent ideation primitives.
- **Creativity Warmups.** Pre-ideation warm-up exercises drawn from the Torrance Test of Creative Thinking [BT] (Practice "Creativity Warmups", "Why do it?").
- **Design Sprint.** "It is a 5 day customer-centric process for rapidly solving a key challenge, creating new products, or improving existing ones … The process phases include: Understand, Define, Sketch, Decide, Prototype and Validate" [V] (Practice "Design Sprint", "What is it?") [BT to the GV/Sprint Book lineage].
- **Lean Inception, Lean UX Workshop, Mood Board, Experiment Canvas.** Structured idea-shaping workshops.

### Sub-cluster 2: Prioritisation

- **$100 Prioritisation.** "Where you need to narrow down your options or prioritise. This is a democratic relative prioritisation exercise where people get $100 each to distribute across whatever needs prioritising" [V] (Practice "$100 Prioritisation", "What is it?"). The contrarian is implicit in the design: "It's a method that helps everyone be heard, but also navigates you towards consensus in an equitable way" [V] (Practice "$100 Prioritisation", "Why do it?") [AR].
- **MoSCoW Method.** Must-have / Should-have / Could-have / Won't-have prioritisation [AP] (Practice "MoSCow Method", "What is it?").
- **Impact-Effort Prioritisation Matrix.** Two-axis 2×2 (high/low impact × high/low effort) [AP].
- **How-Now-Wow Prioritisation Matrix.** Similar 2×2 with explicit creativity framing (Now = obvious; How = aspirational; Wow = creative and feasible) [AP].
- **The RICE Scoring Model.** Reach × Impact × Confidence ÷ Effort. A four-factor formula for prioritisation [AP].
- **Dot Voting.** "Dot Voting is a collaborative decision-making technique. It helps people to prioritise or select options from a range of choices" [V] (Practice "Dot voting", "What is it?"). The simplest and most-referenced prioritisation primitive in the library.
- **Eisenhower Box.** Four-quadrant urgent × important matrix with four actions (Do / Schedule / Delegate / Delete) [V] (Practice "Eisenhower Box or Urgent-Important Matrix", "What is it?").
- **Weighted Shortest Job First (WSJF), VUE your priorities, Priority Sliders, Kanban Priorities.** Quantitative and slider-based prioritisation.

### Sub-cluster 3: Experimentation and decision framing

- **Design of Experiments.** "The Design of Experiments is the practice we use to turn ideas, hypothesis and/or assumptions into concrete well defined set of experiments which can be carried out in order to validate those ideas, hypothesis and assumptions, i.e. provide us with valuable learning" [V] (Practice "Design of Experiments", "What is it?"). Minimum design fields: Hypothesis / Current Condition / Target Condition / Obstacles / Pass / Measures / Learning [AP] (Practice "Design of Experiments", "How to do it?"). The practice carries a contrarian: "Successful experiments are not experiments that have proven our assumption as correct. Successful experiments are those that provide valid and reliable data which shows a statistically significant conclusion" [V] (Practice "Design of Experiments", "How to do it?") [AR].
- **Minimum Viable Product (MVP), Dark Launches, Split Testing - A/B Testing.** MVP is "an MVP is the version of a product with the highest learning per unit of effort" [paraphrase consistent with Practice "Minimum Viable Product (MVP)"]. Dark Launches "releases new features to a subset of your end-users and then capture their behaviors and feedback" [V] (Practice "Dark Launches", "What is it?").
- **Disagree and Commit.** "An approach to enable teams to transition from thinking to doing, whilst ensuring the team are committed to the execution" [V] (Practice "Disagree and Commit", "What is it?"). The contrarian: "There is a common misconception that collaboration eventually requires consensus; it does not. In fact consensus can come at a very high cost to the team dynamic" [V] (Practice "Disagree and Commit", "Why do it?") [AR]. Frames commitment as intrinsic and compliance as the failure mode.
- **Dissent Cards.** "It's a way to encourage greater diversity of ideas and increase the psychological safety necessary for disagreement to occur productively within the group. This practice is taken from L. David Marquet's book, 'Leadership is language'" [V] (Practice "Dissent Cards", "What is it?") [BT to Marquet]. Red-card-must-dissent / black-card-free-choice mechanic, with a 1:5 red:black ratio.
- **Example Mapping.** Four-colour-sticky structure (yellow story / blue rules / green examples / red questions) for fleshing out acceptance criteria [AP] (Practice "Example Mapping", "How to do it?").

## Part V: Delivery phase (37 practices)

Delivery practices are the build-and-measure phase. Three sub-clusters: cadence practices, reliability/safety practices, and feedback/learning practices.

### Sub-cluster 1: Cadence practices

- **Scrum.** Presented as the "3-5-3 formation" — 3 Roles (Product Owner / Scrum Master / Development Team Members), 5 Events (Sprint Planning / Daily Standup / Sprint Review / Sprint Retrospective / Sprint), 3 Artifacts (Product Backlog / Sprint Backlog / Product Increment) [AP] (Practice "Scrum", "How to do it?"). The OPL practice counts five events with the Sprint included as an event in the count.
- **Iteration (Sprint) Planning.** "An event where a development team collaborates with the Product Owner to align on the goal and outcome the team are going to focus on for their next iteration of development" [V] (Practice "Iteration (Sprint) Planning", "What is it?"). 1-hr-per-week-of-iteration rule of thumb [AP] (Practice "Iteration (Sprint) Planning", "How to do it?").
- **Daily Standup.** "The main point of a daily standup (Daily Scrum) is for the team to better align towards the sprint goal" [V] (Practice "Daily Standup", "What is it?"). Three canonical questions: yesterday / today / blockers [AP] (Practice "Daily Standup", "What is it?"). The contrarian: "Be careful it doesn't drift into a status update" [V] (Practice "Daily Standup", "How to do it?") [AR].
- **Retrospectives.** "Retrospectives provide opportunities for groups to reflect, inspect and adapt their ways of working. They often take place at the end of sprints but can be scheduled at any time" [V] (Practice "Retrospectives", "What is it?"). The library carries multiple retrospective variants: *4Ls Retrospective* (Liked / Learned / Lacked / Longed-for), *Rose, Thorn, Bud*, *Plus, Minus, Interesting (PMI +-?) Retro*, *Realtime Retrospective*, *Design Retro : Active*, *Futurespective*.
- **Showcase / Sprint Review.** "An event where stakeholders and interested parties are given a demonstration of recent work performed by a team" [V] (Practice "Showcase", "What is it?").
- **Kanban.** "Kanban is a framework used to implement agile software development based in the following practices: Visualize the workflow, Limit Work in Progress (WIP), Manage flow, Make Process Policies Explicit" [V] (Practice "Kanban", "What is it?"). Companion practice **Kanban Picture** uses the slogan "Stop starting, start finishing!" [V] (Practice "Kanban Picture", "How to do it?") [AR].
- **Story Kick-offs, Story RePointing, Backlog Refinement.** Story-level cadence practices.

### Sub-cluster 2: Reliability and safety practices

- **Blameless Postmortem.** "Blameless Postmortem is a post-incident practice assessing an incident or other types of outages, its timeline, environment conditions, and all possible factors that lead an incident to happen" [V] (Practice "Blameless Postmortem", "What is it?"). Contains an explicit quote on framing: "Our job is not to point fingers at an unlucky engineer that applied a wrong configuration file, our job is to figure out why he picked the wrong one and what we personally and as an organization can do to prevent it in the future" [V] (Practice "Blameless Postmortem", "What is it?") [AR]. Two foundations: "Availability of the information regarding the incident" and "Psychological safety of all participants that promotes speaking up openly" [V] (Practice "Blameless Postmortem", "How to do it?").
- **Chaos Engineering.** "Chaos Engineering is a practice where an organization tries to predict the unpredictable. It can be used to achieve resilience against infrastructure failures, network failures, and application failures … with chaos engineering, we introduce failures on purpose on production systems to see how they withstand the chaos" [V] (Practice "Chaos Engineering", "What is it?").
- **Risk Radar, Risk Management, ROAM Boards.** Risk-monitoring practices.
- **Canary Release.** "In software development, this is a form of Continuous Delivery in which only a small part of the real users of a product will be exposed to the new version of the product. The team would monitor for regressions, performance issues and other adverse effects and can easily move users back to the working old version if issues are spotted. The term comes from the use of caged birds in coal mines to discover the build up of dangerous gases early on" [V] (Practice "Canary Release", "What is it?") [AE].
- **Blue Green Deployments.** Twin-environment swap pattern with a load-balancer cut-over [AP] (Practice "Blue Green Deployments", "What is it?").
- **Feature Toggles, Dark Launches.** Toggle-driven progressive-exposure practices.
- **Security Checklist.** Three-phase secure-code-review checklist (Before pushing code / Before completing the code review / During the review) from SafeStack.io [AP] (Practice "Security checklist", "What is it?") [BT to SafeStack].
- **Wheel-of-Misfortune.** A role-play exercise where the team practices incident response on past postmortems (referenced from Blameless Postmortem) [AP] (Practice "Wheel-of-Misfortune", "What is it?").
- **Fire Drills.** "Fire Drills is a fun and safe way to practice Incident Management and Response in practice. It's an extension of Chaos Engineering, which is a discipline for increasing the confidence of your systems. Fire Drills focuses on the People aspect of engineering and aims to increase the confidence of your Team" [V] (Practice "Fire Drills", "What is it?").

### Sub-cluster 3: Feedback and learning practices

- **Cohort Analysis.** "Cohort analysis is a subset of behaviour analytics which studies the difference in behaviour between different groups of people (customers / users), aka cohorts" [V] (Practice "Cohort Analysis", "What is it?").
- **Funnel Analysis.** "Funnel Analysis is an analytical practice studying the changes over a course of events or steps in a user journey" [V] (Practice "Funnel Analysis", "What is it?"). Cited explicitly as a Lean Startup "tune the engine" / "innovation accounting" practice [BT to Ries] (Practice "Funnel Analysis", "Why do it?").
- **Split Testing - A/B Testing, Split Testing - Multivari Testing.** A/B and multi-variable testing.
- **Usability Testing, Guerilla Testing, Heuristic Evaluation, Cognitive walkthrough.** User-research practices.
- **Agile Health Check.** Team self-assessment against agile-manifesto principles on a 1-10 scale via dot voting [AP] (Practice "Agile Health Check", "How to do it?").
- **Burnup Chart, Burndown** (Foundation), **Cumulative Flow Diagram** (referenced from Kanban Picture). Visualisation-of-work practices.
- **Code Review.** "Code Review is a software quality assurance activity that someone other than the author(s) checks the relevant piece of code" [V] (Practice "Code Review", "What is it?"). Three types: Inspections (long), Walkthroughs (mid-level), Short reviews (10 min) [AP] (Practice "Code Review", "How to do it?"). Cited authority: Steve McConnell's *Code Complete* (collective ownership) and Jeff Atwood's "ten commandments of egoless programming" [BT].

## Part VI: Cross-phase patterns and recurring shapes

### The facilitation-first pattern

A high proportion of practices across all four phases — including engineering-substrate practices and reliability practices — are described as *facilitated sessions*, not as solo activities. The recurring shape is: *prepare the room/board → silent generation → small-group convergence → large-group integration → action items*. This shape is named explicitly in *1-2-4-All* but appears under different names in *Affinity Mapping*, *6 Dimensions of Discovery*, *10-for-10*, *Crazy 8s*, *4Ls Retrospective*, *Rose Thorn Bud*, *Empathy Mapping*, *Force Field Analysis*, and many others.

### The "Tips for Remote Working" structural marker

A recurring sub-heading inside the `howTo` body field is "Tips for Remote Working" (or "Tips for Remote Sessions"). It appears in dozens of practices, including *Affinity Mapping*, *Event Storming*, *Empathy Mapping*, *Retrospectives*, *Iteration (Sprint) Planning*, *Stakeholder Map*. The marker is editorially significant: the library has been maintained through and past the 2020–2023 shift to remote and hybrid work, and the practice pages were updated rather than deprecated.

### The cross-practice link as compositional building block

Practices reference one another not for "further reading" but for compositional substitution. Examples observable in the corpus:

- *6 Dimensions of Discovery* explicitly invokes *Affinity Mapping* as its convergence step.
- *Disagree and Commit* and *Dissent Cards* explicitly pair (the cards make the disagree-and-commit move easier).
- *Dark Launches* is contrasted with *Canary Release* and *A/B Testing* inside its own body, naming the distinguishing question for each.
- *$100 Prioritisation* invokes *1-2-4-All* as its preferred conversation structure for group variants.
- *Five Whys* is invoked from within *Retrospectives* as a drill-down technique.
- *Blameless Postmortem* invokes *Wheel-of-Misfortune* as a follow-on training practice.
- *Open Decision Framework* is referenced from *Start With Why* as Red Hat's worked example of finding an organisation's why.

The internal-link graph is the library's third structural layer (after Mobius phase and tag), and it carries semantic content: practices are recommended *together*, with the library curators encoding which combinations they have seen work [AR] (Collection internal structure).

### Lineage and borrowed-through citations

Many practices in the library carry external attributions in their `whatIs` or `whyDo` bodies. The `[BT]` (borrowed-through) connections observed during the deep read include:

- *1-2-4-All*: Liberating Structures collection (cited explicitly).
- *Five Whys*: Taiichi Ohno at Toyota.
- *Force Field Analysis*: Kurt Lewin (social science).
- *Confidence Voting*: Jean Tabaka, *Collaboration Explained*.
- *GROW Model*: Sir John Whitmore.
- *Empathy Mapping*: Dave Gray of XPLANE.
- *Event Storming*: Alberto Brandolini (2013 blog).
- *Impact Mapping*: Gojko Adzic (2012).
- *North Star Framework*: Sean Ellis (term origin); Amplitude (playbook reference).
- *Jobs to be Done*: Tony Ulwick.
- *Start With Why*: Simon Sinek; cites Theodore Levitt (drill-bit), Seth Godin (*This Is Marketing*), Dan Pink (*Drive*).
- *Start At The End*: *The Sprint Book*.
- *Cynefin Framework*: Dave Snowden (implicit; named domains and responses).
- *Disagree and Commit*: pattern attributed to L. David Marquet's *Leadership is Language* via the related *Dissent Cards* practice.
- *Dissent Cards*: L. David Marquet, *Leadership is Language*.
- *Backcasting / Pre-mortem*: Gary Klein (HBR); Daniel Kahneman, *Thinking Fast and Slow*.
- *Lean Canvas*: Ash Maurya (and Alexander Osterwalder's Business Model Canvas).
- *Independent Service Heuristics*: Team Topologies (Matthew Skelton, Manuel Pais).
- *Cognitive Loadometer*: Team Topologies (Skelton, Pais); cites John Sweller's *Cognitive Load Theory*.
- *Funnel Analysis*: Eric Ries, *The Lean Startup* (innovation accounting).
- *Code Review*: Steve McConnell, *Code Complete*; Jeff Atwood (egoless programming).
- *Evals*: Andrej Karpathy (the "march of nines" framing).
- *Human in the loop*: 1979 IBM internal training slide (via Simon Willison's blog) — "A computer can never be held accountable, therefore a computer must never make a management decision".
- *Open Decision Framework*: Red Hat People Team.
- *Group Launch Facilitation*: Gen. McChrystal ("gardener" leadership model).

The borrowed-through density in this sample is high. The library characterises itself, in its own framing, as "a community-driven inspired library of best practices and tools" [V] (`src/pages/learn.js`) — *inspired by* and citing prior published practice literature rather than originating from scratch. Many practices in the sampled set cite a named lineage or published source. (A full census of citations across all 266 practices was not performed; this is a sample-based observation.)

## Part VII: Positions the library explicitly frames against

A small number of contrarian positions are stated explicitly in practice bodies, not in editorial framing. These are the source's own framing-against:

1. **Against HiPPOs (Highest Paid Person's Opinion).** Explicit in *1-2-4-All* ("All voices are heard, incorporating 'silent' conversations and expanding input diversity - No more HiPPOs!" [V]). Implicit in the broader silent-generation pattern that runs across the facilitation practices.
2. **Against consensus-as-requirement.** *Disagree and Commit*: "There is a common misconception that collaboration eventually requires consensus; it does not. In fact consensus can come at a very high cost to the team dynamic" [V] (Practice "Disagree and Commit", "Why do it?").
3. **Against "the shopping list of features".** *Impact Mapping*: "Most planning activities revolve around juggling a 'shopping list of features,' as Gojko calls them. Even though the features are delivered, often the business objective is not achieved" [V] (Practice "Impact Mapping", "Why do it?"). Echoed in *Start At The End*.
4. **Against blame in incident response.** *Blameless Postmortem*: "Our job is not to point fingers at an unlucky engineer that applied a wrong configuration file, our job is to figure out why he picked the wrong one and what we personally and as an organization can do to prevent it in the future" [V] (Practice "Blameless Postmortem", "What is it?").
5. **Against output-measurement when outcome is the question.** *OKRs* (Good Key Results Guidance): "Quantitative measurement of value - Measure desired outcomes and impact, i.e. results, not tasks completed" [V] (Practice "Objectives & Key Results (OKRs)", "How to do it?").
6. **Against treating non-improvements as success.** *Design of Experiments*: "Successful experiments are not experiments that have proven our assumption as correct. Successful experiments are those that provide valid and reliable data which shows a statistically significant conclusion" [V] (Practice "Design of Experiments", "How to do it?").
7. **Against copying practices without principles.** *Establish Shared Principles*: "Blindly following practices are not encouraged, establish a set of shared principles and you can weather the storms that beat at your door … Copying just the practices of successful organizations will not get us the same result if we do not also adopt the values and principles that originated these practices" [V] (Practice "Establish Shared Principles", "Why do it?"). Notable as the library's most self-aware contrarian.
8. **Against status-update standups.** *Daily Standup*: "As mentioned above, the main point of a stand up is alignment. Be careful it doesn't drift into a status update" [V] (Practice "Daily Standup", "How to do it?").
9. **Against AI overconfidence in evaluation.** *Evals*: "Traditional tests give you certainty. Evals give you confidence … No single eval can tell you the system is working perfectly. Instead, multiple evals across different dimensions combine to build a level of confidence" [V] (Practice "Evals", "What is it?").
10. **Against silent AI delegation in high-stakes work.** *Human in the loop*: "A computer can never be held accountable, therefore a computer must never make a management decision" [V] (Practice "Human in the loop", "Why do it?") [BT to a 1979 IBM internal training slide].

## Citation and source-integrity notes

**Conversion path.** No format conversion needed. The 266 source files are markdown with YAML frontmatter; they were concatenated into a single converted markdown by a deterministic Python script that parsed each frontmatter and rendered each practice as a `## {title}` section with metadata, whatIs, whyDo, and howTo blocks separated by `---` rules. Files grouped by `mobiusTag` (Foundation → Discovery → Options → Delivery) and alphabetised by filename within each phase. SHA256 of converted markdown: `2f1ac99414296eeb6d7af64f23fdaf10c1bd85d9325aa88fe8e58dcbecfc1c77`.

**Citation style decision.** `(Practice "Title", "Section")` — the practice file is the citation unit because the source has no chapter or page anchors. For collection-level facts that span multiple practices (e.g., "111 Foundation practices"), the citation is `(Collection metadata)` and the count is mechanically reproducible by grepping `mobiusTag:` across the 266 files.

**Coverage discipline.** Full collection coverage is preserved — all 266 practice files were read into the converted markdown. Verbatim citation density is *sampled* across the four phases: most-cited practices in each phase have inline `[V]` quotes; the rest of the cluster is paraphrased with `[AP]` markers. This is the appropriate shape for a 266-practice catalogue ingest — a deep reference that quoted every practice in full would be ~150k words and would defeat the purpose of having a deep reference.

**Cross-corpus discipline.** The deep reference does not connect OPL practices to authors outside the OPL library *unless the library itself cites them*. Where a practice cites Ohno, Lewin, Whitmore, Brandolini, Adzic, Marquet, Klein, Kahneman, Ries, Sinek, McConnell, Atwood, Snowden, Karpathy, Willison, Skelton & Pais, Schwaber & Sutherland, etc., those are recorded as `[BT]` (borrowed-through). Where the library does not cite an author, that author is not connected to OPL in this reference — the source-only discipline applies. The Mobius Loop framing itself is treated as the library's internal construct (the `mobiusTag` frontmatter is present on every practice); the *Stakeholder Mapping (Mobius Outcome Delivery)* practice file names "Mobius Outcome Delivery" in its title, but the source pages do not characterise the external lineage of the Mobius Loop model beyond that title reference, so this deep reference does not either.

**Two non-English practices.** The cloned commit contains two Spanish-language practices: `event-storming-tormenta-de-eventos.md` (a Spanish translation of `event-storming.md`) and `meditacion.md` (Spanish version of `meditation.md`). Both are preserved verbatim in the converted markdown; the deep reference cites only the English originals. No translation work was done. These two files plus their English originals account for 4 of the 266 practice count; the per-phase counts and the percentage calculations treat each `.md` file equally regardless of language.

**The practice count.** Exactly 266 `.md` files in `src/pages/practice/` at commit `8bfa450e75dfba1e2a3c68ac0e514e587f6f116e`. Distribution: 111 Foundation, 86 Discovery, 32 Options, 37 Delivery, 0 Unclassified (every file has a `mobiusTag`). Counts are mechanical; the operator can re-derive them by `grep -h "^mobiusTag:" src/pages/practice/*.md | sort | uniq -c`.
