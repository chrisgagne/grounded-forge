<!-- derived-from-deep: sha256:72550dcb4a79df378ed7b1441f68804581317c24bb6c65b51c20104d797fb0c4 -->
# U.S. Marine Corps, MCDP-1 Warfighting — Software / Business Distillation

**Source:** U.S. Marine Corps (1997). *MCDP 1: Warfighting*. Headquarters United States Marine Corps, Department of the Navy, 20 June 1997. PCN 142 000006 00. Supersedes FMFM 1 Warfighting (1989). **Licence:** Public domain (US Government work product). **Scope:** open.

## Software / Business Relevance

MCDP-1 is the doctrinal application of John Boyd's strategic theory — particularly the OODA loop and the concept of *operating inside the adversary's decision cycle*. The agile / lean / DevOps / SRE / startup-strategy traditions all share intellectual roots with this lineage. For software / business practitioners, MCDP-1 is unusually directly usable: a short, philosophical pamphlet whose vocabulary maps cleanly onto contemporary technology-organisation work.

Six threads are particularly relevant.

### 1. Tempo as the competitive weapon (Ch 2 Notes 18)

The OODA-loop claim — the side that completes the cycle faster, or that operates in a way the adversary cannot orient to, wins — is the foundational doctrinal statement of *tempo as strategy*. The agile / lean / DevOps / startup traditions all rest on a version of this claim:

- **Eric Ries (Lean Startup):** Build-Measure-Learn cycle speed determines the rate of validated learning.
- **Humble & Farley (Continuous Delivery):** deployment frequency is the most-correlated DORA metric; shipping faster is competing on OODA tempo.
- **Beck (XP):** weekly cycle, quarterly cycle — the cadences are designed to outpace the requirements-change cycle.
- **Steve Blank (Customer Development):** customer-development tempo determines time-to-product-market-fit.

The software-business application: where is your team's OODA tempo relative to the market / competitor / customer-need-change cycle? If the cycle outside is faster than the cycle inside, you are reacting to a market that has already moved.

### 2. Main effort / Schwerpunkt (Ch 4)

The discipline of one main effort — one team, one objective, with everything else as supporting effort that yields when in conflict — is the doctrinal version of what Goldratt teaches (Theory of Constraints: identify the constraint, exploit it, subordinate everything else to it) and what high-performing software companies operationalise as *one big bet per quarter*.

The software-business application: if your roadmap has more than one *primary* objective, your *Schwerpunkt* discipline is missing. Naming the main effort explicitly — and ensuring every team member can state it in one sentence and agrees — is the operational filter.

### 3. Mission tactics / commander's intent (Ch 4)

*Senior gives what and why; subordinates decide how.* For software organisations, this is the doctrinal version of:

- L. David Marquet's *intent-based leadership* (and *leader-leader* model).
- The OKR system (Objectives = intent; Key Results = measurable execution within intent).
- *Architectural runway* in agile architecture (the framing within which teams make local technology decisions).
- The DevOps / SRE devolution of decision authority to the team closest to the work.

The pamphlet's disciplinary requirement — *intent must be understood two levels up* — is the operational answer to *how much autonomy should I give my team?* The answer: as much as can be exercised while still supporting the intent two levels up. If your team does not know the intent two levels up, the question is not *can they be trusted?* — it is *have we communicated the intent clearly enough?*

### 4. Doctrine as a way of thinking, not a checklist (Ch 3)

The pamphlet is explicit. For software organisations, this reframes:

- Engineering standards and runbooks: are they teaching the thinking, or just transmitting the practices? Mechanical execution without underlying thinking produces drift.
- Sprint ceremonies (Scrum / SAFe / etc.): are they cultivating the discipline, or have they become theatre?
- Architectural decision records (ADRs): are they capturing the *why* — the thinking that produced the decision — or just the *what*?

The discipline is structural: the doctrine's value is in the cognitive habits it produces, not in compliance with its surface practices.

### 5. Surfaces and gaps (Ch 2)

*Avoid enemy strength; exploit weakness. Reconnaissance pull over command push.* The doctrinal phrasing of what software product strategists know as *don't compete head-on with incumbents on their strengths; find the unattended adjacency*. Geoffrey Moore's *Crossing the Chasm* / Clayton Christensen's *Innovator's Dilemma* / Blue Ocean Strategy all operationalise versions of this.

The software-business application: where in the market is the gap? Where is the incumbent's surface so strong that direct attack is pointless? The product-strategy discipline is to read the surfaces and gaps before committing the main effort.

### 6. Severity on errors of inaction, leniency on overbold errors (Ch 3)

The doctrinal rejection of *zero defects* is directly applicable to software-organisation culture. Teams operating in fear-of-mistakes / fear-of-blame cultures optimise for *don't be the one blamed*, which produces inaction.

The software-business application: the asymmetry of consequences is the structural condition for any culture of experimentation, learning, or psychological safety. Errors of commission (we shipped, it failed, we learned) should be tolerated and educational. Errors of omission (we didn't ship, we waited, we missed the window) should be the punishable failure mode. Without this asymmetry, the team will not take the actions that learning requires.

This is the operational form of Edmondson's *psychological safety* (and connects to the resilience-engineering corollary: practitioners create safety only when permitted to act).

## Cautions for software / business translation

The *Zweikampf* framing of war (a violent struggle between two hostile irreconcilable wills) rarely fits civilian business contexts — most business situations involve negotiable parties whose interests partly align (customers, partners, employees, competitors). The OODA / Schwerpunkt / mission-tactics / surfaces-and-gaps machinery transfers; the *Zweikampf* framing usually does not.

The doctrine's emphasis on *tempo as decisive* needs calibration in business contexts. Some markets reward fastest-mover; others reward last-correct-mover. The doctrinal claim is contestable in markets dominated by network effects, switching costs, or regulatory inertia. The MCDP-1 frame is most directly applicable to fast-moving, low-switching-cost, attention-driven markets (consumer software, social media, e-commerce, growth-stage SaaS) and less directly applicable to slow-moving, high-switching-cost markets (enterprise procurement, public-sector contracting, regulated industries).

## Connections to other corpus sources

- **Scrum Guide (slug 00m); Field Guide (slug 000)** — the agile / cadence application.
- **Open Kanban (slug 008)** — flow / WIP / tempo discipline.
- **Open Practice Library (slug 009)** — practitioner-facing methods for tempo + intent + main effort.
- **OpenStax *Introduction to Business* (slug 00g); *Principles of Management* (slug 00j); *Entrepreneurship* (slug 00f)** — for the academic-business vocabulary; MCDP-1 is the operational complement.
- **Jones, *Evidence-Based Software Engineering* (slug 003)** — for the empirical research on what software-engineering practices actually correlate with what outcomes; MCDP-1 is the doctrinal frame the research findings often confirm.
- **Letaw, *Handbook of Software Engineering Methods* (slug 004)** — for the catalogue of methods; MCDP-1 names the doctrine the catalogue should serve.
- **Org Topologies Primer (slug 00p)** — for the team-topology / structure layer; MCDP-1 is the warfighting-philosophy layer.
- **Barbrook-Johnson & Penn, *Systems Mapping* (slug 001)** — for the systems-thinking complement.
