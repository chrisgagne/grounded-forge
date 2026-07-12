# Krivitsky, Larman & Flemm, Org Topologies Primer — Software-Business Distillation

**Source:** Alexey Krivitsky, Craig Larman & Roland Flemm (2025). *Strategic Org Design: The Primer*. Org Topologies™ 2025 Edition. February 2025. Licence: CC BY-NC-SA 4.0. https://orgtopologies.com.

## Software-Business Relevance

The Primer sits squarely in the software-business intersection: it is a strategic-org-design framework whose worked examples and framework mappings are predominantly drawn from software organisations, and whose 2025 Edition treatment of AI as a workforce element makes it a current reference for the AI-integration build/buy/architect decisions that now dominate the technical-commercial agenda. The horizontal axis is explicitly mapped to Scrum's Definition of Done. The "Software Feature Team" is the canonical End-to-End example. The "Feature Factory" failure mode of Delivery Topology is named directly. SAFe, LeSS, and Team Topologies are mapped to OT topology regions. The pet-supply e-commerce worked example walks the strategic-AI investment decision end-to-end.

The Primer encodes software-business discipline in several layers. The **three topologies as software-business stances** are decision-anchors carrying named failure modes that map directly onto software-business pathologies. Resource Topology in software is the offshore-rate-card / billable-hours model where engineers are pooled-and-assigned. Delivery Topology in software is the cross-functional Scrum-style feature team optimised for predictable delivery — *and the named failure mode is "no guarantee... that the output effectively solves the real problem or creates outcomes people care about. Products and services with 'feature bloat' are a common consequence."* Adaptive Topology in software is the Team-of-Teams operating on whole-business or partial-business scope (the Uber/Uber Eats examples), with adaptiveness and customer-centricity as the named goals. The choice of topology is a commercial commitment — Delivery topology commits to short-lead-time predictable delivery and accepts feature bloat as the failure mode the business must counter elsewhere.

The **strategic-design stance applied to software** is a counter to the most common software-business failure: choosing an engineering framework (SAFe, LeSS, Scrum-at-scale variants) as the business strategy. The Primer's chain-of-fit (business strategy → org goal → topology → frameworks) is the software-business decision rule: the framework is downstream of the topology decision, which is downstream of the org-goal decision, which is downstream of the business-strategy decision. Adopting a framework as the business strategy is the cargo-cult failure mode the Primer warns against.

The **AI-integration decision as a software-business decision** is the 2025 Edition's distinctive contribution. "Specialization and expertise are vanishing as limited resources, due to intelligence as a service" is a strategic-fact claim about the software-business landscape — and it carries the three guiding questions for where AI investment makes commercial sense (focus on the elevation area; target bottlenecks; account for human monitoring as new responsibility). The pet-supply worked example walks an AI build-vs-buy-vs-integrate decision at the architecture-team-cost-customer intersection.

The **mapping of named frameworks** (SAFe at mostly TASKS-and-CAPS levels; Rendanheyi as elevating thousands of MEs to Driving archetypes) gives software-business practitioners a vocabulary for stating which framework produces which topology and therefore which org goal and therefore which business capability. This is the missing-language software businesses often lack when comparing scaling frameworks.

A fourth thread, distinctive to software-business commitments, is the discipline of incremental elevation tied to business-objective rhythms. "Different parts of an organization (e.g. business divisions) can have their own development vector that is consistent with their business objectives." A software business with a stable Tier-1 product (Resource or Delivery topology fit) and an emerging product line (Adaptive topology fit) can hold divergent org designs simultaneously rather than forcing whole-company alignment.

This distillation gathers these threads into a working pattern: how to use the three topologies as decision-anchors with named software-business tradeoffs; how to use the chain-of-fit to keep software-framework decisions in their proper position (downstream of topology choice); how to structure AI-integration decisions as bottleneck-targeted investments rather than generic adoption; and how to use divergent topologies across business lines to fit each product's market dynamics.

## Key Concepts for Software-Business

1. <!-- concept: horizontal-axis-as-dod --> **The horizontal axis as Scrum's Definition of Done.** "To make a connection to the popular software development approach Scrum, in that model, the horizontal axis is the increasing completeness of the Definition of Done." Rightward movement is DoD-expansion: a team that can satisfy a DoD that includes shipping-to-production end-to-end is structurally more rightward on the OT map than a team whose DoD requires a separate operations function. (Source: Krivitsky, Larman & Flemm, *Org Topologies Primer* 2025, p. 6, "Horizontal Dimension: Skills Mandate")

2. <!-- concept: ot-two-axes --> **The two axes as commercial-decision dimensions.** The horizontal axis carries "the transaction costs (a.k.a. overhead costs) to deliver value (decreasing from left to right!), and with that, how much waste from concept to cash." The vertical axis carries "the switching costs to work on something different (decreasing from bottom to top), and, therefore how easy it is for the whole organization to switch direction." Software-business commitments can be priced explicitly on these axes — moving rightward reduces concept-to-cash latency; moving upward reduces strategic-pivot cost. (pp. 6–7)

3. <!-- concept: resource-topology --> **Resource Topology in software.** The offshore-rate-card / billable-hours / staff-augmentation model. Justified when the directing-doing relationships are genuinely temporary (the movie-producer-hires-dancers pattern: a client engagement, a contract project, a wind-down maintenance phase). Failure mode: "Learning in this topology is largely confined to improving existing skills rather than discovering new ones." Predictable cost structure; high coordination tax; weak innovation capacity. (p. 11, "Resource Topology")

4. <!-- concept: delivery-topology --> **Delivery Topology in software (the Feature Factory failure mode).** "In some domains, this topology is called a 'Feature Factory' since Delivery units can provide a near-endless stream of features." Cross-functional Scrum-style teams optimised for predictable feature delivery. Named failure mode: "Notice that there is no guarantee in this topology that the output effectively solves the real problem or creates outcomes people care about. Products and services with 'feature bloat' are a common consequence." Fit when the challenge is delivery, not discovery. (p. 12, "Delivery Topology")

5. <!-- concept: adaptive-topology --> **Adaptive Topology in software (Team-of-Teams).** "The Adaptive Topology merges 'directing, doing, and delivering' into one holistic unit within the Driving archetypes, where humans, AI agents, and robots collaborate on complex problems in an adaptive way." Boundaries between teams replaced by larger constructs (Team-of-Teams). Emergent quality: "synchronicity of work" where "the Driving archetype allows all parties to work in unison." Fit for market disruptors and startups, where "growth and learning are crucial." (p. 13, "Adaptive Topology")

6. <!-- concept: chain-of-fit --> **The chain-of-fit as the software-framework decision rule.** Business strategy → organisational goal → topology → frameworks. SAFe, LeSS, Team Topologies, FAST Agile, Spotify Model are *frameworks-as-tools-for-elevating-toward-a-topology* — not as decisions themselves. "Org Topologies—including but not limited to Resource, Delivery, or Adaptive—serve as a reference for assessing and designing a new target structure supporting the org design goals. And while the Elevating Katas provide one set of guides to get change going, of course people will also get guidance from existing frameworks, while aiming for the target topology." (p. 22, "Strategic Org Design vs. Framework Thinking")

7. <!-- concept: safe-to-ot-mapping --> **The SAFe-to-OT-map worked observation.** "Observe the OT map for SAFe; anyone can easily see that SAFe is mostly implemented with interdependent incomplete teams working on components at the Tasks level, and fast-flow teams at the Capabilities level." A software business considering SAFe should expect to land mostly at TASKS-and-CAPS archetypes; if the business strategy requires WHOLE-3 archetypes (whole-business end-to-end), SAFe is the wrong tool. (p. 22, "Mapping SAFe")

8. <!-- concept: rendanheyi --> **The Rendanheyi mapping (Haier's micro-enterprises).** "RDHY elevates its thousands of micro-enterprises (MEs) that directly interact with users, and optimizing for autonomy and customer-focused value creation." Rendanheyi is a software-business reference for what an Adaptive-Topology-at-scale looks like — useful when senior leadership asks "can we get there from here". (p. 22, "Mapping RDHY")

9. <!-- concept: strategic-ai-adoption --> **Strategic AI adoption as a commercial decision.** "A key insight when designing with OT: Specialization and expertise are vanishing as limited resources, due to intelligence as a service. That makes it much easier to elevate an organization!" The structural consequence: "top-right Driving archetypes will become more feasible" as AI lowers the cost of broader skill and work mandates. The commercial decision is not whether to adopt AI but where — focused on the elevation area, targeting bottlenecks. (p. 20, "Strategic AI Adoption")

10. <!-- concept: ai-investment-questions --> **The three AI-investment questions as a software-business filter.** (1) "What parts of the organization are the focus of development with OT? Focus your AI investment in the area you are elevating." (2) "What archetypes are part of your target, and what are the major bottlenecks or constraints limiting their rapid adoption? Find the early points where AI can make an outsized impact." (3) "Do the AIs need monitoring by humans? That implies new responsibilities and processes in your organization." The third question has a hidden cost: human-monitoring overhead must be priced into the AI investment. (p. 20)

11. <!-- concept: pet-supply-ai-example --> **The pet-supply e-commerce worked example as an AI investment archetype.** Resource topology → target Delivery topology with CAPS-3 teams; bottleneck is front-end skill; AI investment targeted at front-end agents; human monitoring assigned to existing front-end specialists in their new CAPS-3 roles. This is the canonical worked example for a software business deciding *which* AI capability to build/buy/integrate. (pp. 20–21, "Strategic AI Adoption")

12. <!-- concept: divergent-designs --> **Different designs for different parts of the company.** "Companies may also choose different org designs for different parts of the company. One division might focus on servicing existing customers on a legacy product, while another is experimenting with new offerings—each requiring its own goal and design." A software business with a mature SaaS product (Delivery topology fit) and an emerging AI product (Adaptive topology fit) can hold both simultaneously. (p. 18, "MADE Real: (3) DESIGN")

13. <!-- concept: output-vs-outcome --> **Output-vs-outcome as a software-business commercial discipline.** "More output usually means more cost or investment, which can lower profit (an outcome). Investing to increase outcomes (healthy people, profit) is justified; 'investing' to increase output is suspect." In software businesses, this is the discipline against feature-velocity as the headline metric; the Delivery Topology's "feature bloat" failure mode is its commercial expression. (p. 8, "Output versus Outcome Archetypes")

14. <!-- concept: named-archetype-language --> **The named-archetype language as software-business communication infrastructure.** "Most of our teams are CAPS-2—multi-skilled yet incomplete, lacking certain capabilities. There are also functional TASKS-1 parties supporting our CAPS-2 teams. This creates dependencies and challenges that are managed by CAPS-1 and PART-1 groups…" One sentence describing a software-organisation ecosystem that conveys delivery latency, coordination overhead, and product-strategy constraint simultaneously. Cross-business-line communication ("the platform team is CAPS-3, your team needs to be PART-2 to consume it") becomes precise. (p. 5, "Language of Org Design")

## Questions to Ask During Software-Business Decisions

### Phase 1: Strategic positioning (Where the software business needs to be)

| Need | Question |
|---|---|
| Test the chain-of-fit | What is the business strategy, what org goal does it require, what topology delivers that goal, and *then* what frameworks could be tools? If the discussion starts with "should we adopt X framework", reframe to start with the strategy. |
| Locate the product in the topology landscape | Is this a stable predictable product (Resource or Delivery fit), a fast-feature-flow product (Delivery fit), or a market-disruptor / new-market product (Adaptive fit)? Different products require different topologies. |
| Surface implicit Resource framing | Is the engineering organisation currently being framed as a billable-hours / staff-augmentation / engineer-pool resource? That is Resource Topology and carries its named failure mode. |
| Test the topology against the AI landscape | Now that "specialization and expertise are vanishing as limited resources", does the target topology presume scarce expertise that no longer applies? The elevation target may be more ambitious than previously feasible. |

### Phase 2: Org-and-architecture choice (Topology, framework, AI integration)

| Need | Question |
|---|---|
| Name the target archetype set | Express the target as "move R&D from TASKS-1 + CAPS-1 to CAPS-3 with PART-2 platform support" or similar. Precision in the OT vocabulary makes the commercial commitment crisp. |
| Decide framework as downstream-tool | Given the target topology, which framework's practices help us elevate? SAFe lands mostly at TASKS and CAPS; LeSS lands at CAPS-3 / PART-2; FAST Agile lands at Adaptive; Spotify model varies. The framework is the means, not the end. |
| Run the AI-bottleneck question | Where in the target archetype set is the elevation bottleneck? Front-end skill? DevOps skill? PM-engineering bridge? Domain expertise? AI investment should target the bottleneck, not be spread evenly. |
| Account for human-monitoring overhead | If the AI investment substitutes for human work, what new human-monitoring responsibilities does it create? That overhead is a cost, not a free win. |
| Choose divergent designs across business lines | If the business has multiple product lines with different market dynamics, can each carry its own topology? A whole-company single-design choice is often the wrong one for software businesses with mixed maturity. |

### Phase 3: Engineering / product / sales / commercial alignment

| Need | Question |
|---|---|
| Test the Delivery Topology against outcome guarantees | If we're targeting Delivery Topology for fast feature delivery, what mechanism counters the "feature bloat" failure mode? Is there a discovery / outcome-validation function outside the Delivery teams? |
| Anchor sales commitments on Sprint Goal, not Sprint Backlog | If sales is committing externally to features, anchor on the Sprint-Goal-level (outcome) commitment rather than Sprint-Backlog-level (output) commitment — the OT vocabulary makes the difference explicit. |
| Surface Conway's-Law alignment | The OT mapping is essentially a Conway's-Law analysis: the software architecture will reflect the team boundaries. Does the proposed architecture imply a topology change? |
| Test the PMO / Resource-Topology drift in growth periods | As the company grows, does the PMO function (project managers, resource-allocation governance) reassert Resource-Topology framing? "The Directing Archetypes in the upper left quadrant treat the Doing Archetypes as 'resources,'" — this is the named drift pattern. |
| Test for whole-company single-design assumption | Is the proposed change a whole-company adoption of one topology, when divergent designs per business line would fit better? |

### Phase 4: Strategic AI integration as a software-business decision

| Need | Question |
|---|---|
| Locate AI investment in the elevation area | Which target archetype are we trying to enable? Direct AI investment there, not generic. |
| Identify the bottleneck AI can dissolve | What is the constraint currently preventing elevation to the target archetype? Front-end skill, ops skill, domain knowledge, integration knowledge? AI investment targeted at the bottleneck has outsized commercial impact. |
| Decide build-vs-buy-vs-integrate against architecture | Where in the architecture does the AI capability sit? Inside the monolith, as a separate service, as a vendor integration? Each choice has topology implications. |
| Price human-monitoring as new responsibility | What human roles take on AI-monitoring responsibility? Often the displaced specialists are the right candidates; price the role-transition costs explicitly. |
| Pre-empt the people-displacement framing | If the AI investment is framed (internally or externally) as people-displacement, the engagement failure mode is predictable. Frame as elevation: "our front-end specialists become AI-agent-monitoring leads in the new CAPS-3 teams." |

### Phase 5: Commitment and announcement

| Need | Question |
|---|---|
| Declare the target topology in the OT vocabulary | Crisp named-archetype description of the target state for both internal and external stakeholders. |
| Anchor framework choices as topology-tools | When announcing "we are adopting Framework X", reframe as "we are elevating to Topology Y, and Framework X gives us the practices for the Y transition." |
| Acknowledge the topology's named failure mode | Honest naming of the topology's failure mode (Resource: coordination; Delivery: feature bloat; Adaptive: high-variance outcomes) signals commercial maturity. |
| Commit to incremental elevation with explicit re-mapping | "Elevation can be an incremental process." Commit to the first 1–2 Elevating Kata experiments and to the re-mapping cadence. Avoid big-bang reorganisation framing. |
| Plan the divergent-design accommodation | If different business lines hold different topologies, communicate the per-line design rather than forcing a unified message. |

### Phase 6: Review (Closing the elevation loop)

| Need | Question |
|---|---|
| Re-MAP the current state | Has the target archetype shift actually happened, or did the change stall at announcement? Re-mapping is the empirical test. |
| Re-ASSESS strategic alignment | Has the business objective shifted such that a different target topology is now the fit? |
| Surface emerging bottlenecks | Which new bottlenecks have emerged now that the original ones are dissolved? AI-driven elevation often surfaces coordination and prioritisation bottlenecks. |
| Check for drift back to Resource framing | Is the language of "resources" creeping back in commercial discussions? That signals Resource-Topology drift under predictability pressure. |
| Identify Elevating Katas worth naming | Which practices that worked here are worth codifying as named Katas for future elevation cycles? |

## Anti-Patterns and Failure Modes

1. **"Adopt SAFe / LeSS / Team Topologies" as the business strategy.** The framework decision should be downstream of the topology decision, which should be downstream of the org-goal decision. Reversing the order is the named cargo-cult failure. (p. 22)

2. **Treating engineers as fungible resources.** The Resource Topology framing in commercial language ("how many engineers do we have to allocate") produces the named failure mode: learning confined to existing skills, no discovery capacity. (p. 11)

3. **Feature-Factory commitment without discovery.** Choosing Delivery Topology for fast feature flow without an outcome-validation mechanism produces "feature bloat... a common consequence." (p. 12)

4. **Whole-company single-design forced on mixed business lines.** Different products require different topologies; forcing one design on all is named as a missed-fit pattern. (p. 18)

5. **Generic "adopt AI" without bottleneck targeting.** Spreading AI investment evenly rather than at the bottlenecks limiting elevation. The Primer is explicit: "Focus your AI investment in the area you are elevating." (p. 20)

6. **AI investment without human-monitoring cost pricing.** The Primer flags monitoring as "an important responsibility for human workers" — pricing it as zero is a commercial mistake. (p. 20)

7. **Strategic-leadership decoupling from internal design.** Senior leaders defining business objectives but treating org-design as someone else's problem. The Primer names this as the strategic-design failure mode. (p. 10)

8. **Single-team interventions in an unchanged software ecosystem.** "A single high-performing team can't deliver its full potential if surrounding structures and processes remain unchanged." Common in software when a "two-pizza team" pilot is launched into an unchanged platform / data / ops surround. (p. 4)

9. **Local engineering-element optimisation without systems-thinking.** Reward systems, structures, or processes changed in isolation. "Performance of the whole system may actually decline (flow can get worse!)." Common in engineering-performance programmes that change one practice in isolation. (p. 16)

10. **Drift back to Resource Topology under quarterly-predictability pressure.** Common in publicly-traded software businesses where utilisation reporting reasserts Resource-Topology framing. The named drift pattern that must be defended against. (p. 11)

## Worked Examples (from the source)

- **The pet-supply e-commerce AI investment (pp. 20–21).** Mature e-commerce product in Resource topology. Business objective: retain customers. Org goal: fast flow to parity. Target topology: Delivery with CAPS-3 teams. AI investment focus: R&D (the elevation area). Bottleneck: front-end design and coding skill. Decision: AI agents to autonomously design and code front ends. Monitoring: existing front-end designers become agent monitors in the new CAPS-3 teams. End-to-end software-business decision walked through the chain-of-fit and the three AI-investment questions.

- **The SAFe mapping (p. 22).** "SAFe is mostly implemented with interdependent incomplete teams working on components at the Tasks level, and fast-flow teams at the Capabilities level." A software business considering SAFe can read its topology implication directly: predominantly TASKS-and-CAPS, not Adaptive. If the business strategy requires Adaptive (market-disruptor stance), SAFe is the wrong tool.

- **The Rendanheyi (Haier RDHY) mapping (p. 22).** "RDHY elevates its thousands of micro-enterprises (MEs) that directly interact with users, and optimizing for autonomy and customer-focused value creation." A reference for what Adaptive-at-scale looks like in practice — useful for software businesses considering whether Adaptive Topology is achievable at their scale.

- **The Uber/Uber Eats Partial-Business example (p. 7).** Two separate profit centres within one company, each operating as Partial-Business-Focus units with cross-team collaboration inside each unit. A software-business reference for divergent-design accommodation: same company, different product lines, different topologies.

- **The running MADE example (pp. 16–19).** Software-org starting state: WHOLE-1 product manager, CAPS-1 project-manager pool, TASKS-1 back-end pool, two TASKS-2 cross-functional dev+test teams. Mapped as Resource Topology. Strategic mismatch surfaced (strategy needs speed; org optimises for utilisation). Designed target: Delivery Topology with cross-functional end-to-end teams. Elevated: Doing archetypes restructured into two cross-functional end-to-end teams.

## Integration with Other References

- **Scrum Guide (Schwaber & Sutherland, 2020).** OT explicitly maps the horizontal axis to "the increasing completeness of the Definition of Done." The DoD-expansion test is the practical bridge: can the team satisfy a DoD that includes shipping-to-production end-to-end (CAPS-3) or only a partial-DoD (TASKS-2)? See `scrum-guide-2020-software-business.md`.

- **Approach Perfect Field Guide to Scrum Events.** OT's "elevation is incremental" and "periodic re-mapping" map onto the Field Guide's Sprint-Review-and-Retrospective cadence. The Field Guide's discipline on the difference between Sprint-Goal-level commitments (outcome) and Sprint-Backlog-level commitments (output) is the commercial-language equivalent of OT's outcome-vs-output discipline. See `approach-perfect-field-guide-scrum-events-software-business.md`.

- **Jones Evidence-Based Software Engineering.** Jones provides the empirical software-economics base (intangible-product pricing, AI-integration cost modelling, agency-theory analysis, Bass diffusion) that complements OT's strategic-design framework. Where OT names the topology choice, Jones prices it. See `jones-evidence-based-sweng-software-business.md`.

- **Letaw Handbook of Software Engineering Methods.** Letaw's architecture-and-method catalogue is the technical-decision complement to OT's org-design framework. Conway's Law connects them: the architecture choice and the topology choice are two views of the same decision. See `letaw-handbook-sweng-methods-software-business.md`.

- **Barbrook-Johnson Systems Mapping.** The MAP step's systems-thinking discipline is the qualitative-CLD / quantitative-System-Dynamics complement OT requires but does not provide. When org-design dynamics show feedback structure (utilisation pressure → headcount cuts → output drop → utilisation pressure), Barbrook-Johnson provides the dynamic-modelling vocabulary. See `barbrook-johnson-systems-mapping-software-business.md`.

- **SSDL Systems Thinking Foundations.** The system-archetype catalogue (shifting the burden, fixes that fail, limits to growth) provides the diagnostic vocabulary for the dynamics that constrain software-business elevation. The "shifting the burden" archetype is particularly relevant when build-vs-buy decisions create vendor dependencies that erode in-house capability. See `ssdl-systems-thinking-foundations-software-business.md`.

- **Open Kanban / Open Practice Library.** OT's Elevating Katas™ as "thoughtful experiments to change the organizational structure, processes, policies" map onto Open Practice Library's discovery-and-delivery practice catalogue and Open Kanban's flow-and-feedback discipline. See `open-kanban-software-business.md` and `open-practice-library-software-business.md`.

## Citation and Source-Integrity Notes

- All claims and worked examples trace to the *Org Topologies Primer* 2025 Edition. The deep reference is at `corpus.commons/demo/references/org-topologies-primer-2025-deep.md`.
- The Primer is published under CC BY-NC-SA 4.0; this distillation inherits the ShareAlike obligation alongside the corpus's other SA-licensed derivatives.
- The Primer is a 27-page document; citations use the form `(p. N, "Section name")` against the page numbers preserved by the converted markdown.
