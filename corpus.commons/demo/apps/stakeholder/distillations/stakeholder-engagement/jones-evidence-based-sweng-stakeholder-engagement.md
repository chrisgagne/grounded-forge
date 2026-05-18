# Jones, Evidence-based Software Engineering — Stakeholder-Engagement Distillation

**Source:** Derek M. Jones (2020). *Evidence-based Software Engineering: based on the publicly available data*. Version 1.0. ISBN 978-1-8382913-0-3. CC BY-SA 4.0. http://www.knosof.co.uk/ESEUR/. **Distribution note:** This distillation is a derivative of a CC BY-SA 4.0 source and carries the same SA copyleft obligation.

## Stakeholder-Engagement Relevance

Jones treats stakeholder dynamics through the lens of economic and information-asymmetry analysis rather than through the soft-skills lens of much existing stakeholder-engagement literature. The book's stakeholder analysis is concentrated in three places: (1) the vendor-client contract bidding and renegotiation dynamics in Ch 5; (2) the information-asymmetry, moral-hazard, and agency-theory framing in Ch 3.4.6–3.4.7; and (3) the stakeholder-identification and salience analysis through Lim's RALIC study in Ch 5.4.5.

The distillation is therefore narrower than the corresponding OpenStax distillations on stakeholder engagement. Jones does not discuss broad governance, community engagement, or normative ethical theories of stakeholder claims. He does provide an evidence-grounded analysis of (a) how to identify stakeholders algorithmically from network data, (b) how to prioritise stakeholder requirements quantitatively, (c) how information asymmetry and moral hazard structure vendor-client relationships, and (d) how cultural and ecosystem context shape stakeholder behaviour. Where Jones is silent — on, for example, broader stakeholder convening or on normative claims about who has moral standing — this distillation acknowledges the silence.

## Key Concepts for Stakeholder-Engagement

1. **Stakeholders identified through network analysis.** Lim's RALIC study at UCL used PageRank applied to the stakeholder-network graph (built from snowball sampling and project documentation) to rank 85 stakeholders by salience; the resulting rankings correlated strongly with the project's ground-truth ranking. This is a defensible quantitative method when the stakeholder set is large or unclear. (Source: Jones, *Evidence-based Software Engineering*, Ch 5.4.5, "Discovering functionality needed for acceptance")

2. **Stakeholder salience as the prioritisation metric.** Salience is "the degree to which managers give priority to competing stakeholder claims" (Mitchell-Agle-Wood). It can be measured by network-position metrics (PageRank), by reciprocal salience (each stakeholder rates the others), or by the directness of stakeholders' role in the system being built. (Source: Ch 5.4.5, "Discovering functionality needed for acceptance")

3. **Requirements prioritisation by fixed-budget allocation.** Regnell et al. asked stakeholders to allocate a fixed budget (100,000 units) across a list of requirements. The variance in the assigned values, computed by leaving each stakeholder out one at a time, reveals the dependence of the priority ranking on individual stakeholders. (Source: Ch 5.4.5, "Discovering functionality needed for acceptance")

4. **Information asymmetry between client and vendor.** Vendors bidding to win an implementation contract have less information than they would have after the system existed; once a vendor has built the system, they have intimate familiarity with it, and information asymmetry deters competing maintenance bidders. Mechanisms that reduce information asymmetry include: requiring source-code escrow, public APIs that allow third-party alternatives, transparent change-control procedures, and contractual provisions for documentation deliverables. (Source: Ch 3.4.6, "Information asymmetry")

5. **Moral hazard in client-vendor relationships.** Moral hazard occurs when information asymmetry exists and the more-informed party has some control over unobserved attributes. In software, this includes developers making implementation decisions on the basis of personal enjoyment or career incentives rather than the client's interest. Agency theory deals with the conflict of interests between those paying for work and those being paid. (Source: Ch 3.4.7, "Moral hazard")

6. **Contract type and management overhead.** Fixed-price contracts involve a slightly greater percentage of management time than time-and-materials contracts (Ahonen et al. study of 117 projects). Standard form contracts almost universally favour the software company that wrote them. The choice of contract type shapes the stakeholder relationship throughout the project. (Source: Ch 5.2.1, "Contracts")

7. **Bidding dynamics shape the post-contract relationship.** Bidding decisions are driven by factors with little or no connection to technical aspects: keeping staff busy, bidding the maximum the client will pay, bidding low to recoup losses during maintenance, getting a foot in the door with small projects. The signing of a contract is the start of cost negotiation, not the end. (Source: Ch 5.2, "Pitching for projects")

8. **Stakeholder culture is path-dependent.** Cultures develop through social learning, conformist transmission, and reciprocity. Stable cultures within a company persist beyond the people who established them. Cross-cultural stakeholder engagement involves navigating these path-dependent cultural differences. (Source: Ch 3.4.4, "Social learning"; Ch 4.4.2, "Culture")

9. **Cultural intelligence is not just cognitive.** Engagement across cultural boundaries requires attention to embodied cultural patterns: spatial metaphors for time differ between English (horizontal) and Chinese (vertical) speakers; metaphors for political position differ across cultures. These shape what stakeholders attend to and how they reason. (Source: Ch 4.4.2, "Culture")

10. **Cooperation requires reciprocity, transitivity, and reputation.** Cooperation through direct reciprocity is stable when the probability of repeat interaction Pi meets c/b < Pi (where c is the cost of cooperation and b is the mutual benefit). Cooperation through indirect reciprocity (reputation-based) is stable when the probability of knowing a member's reputation, Pk, meets c/b < Pk. These conditions explain why long-running stakeholder relationships sustain cooperation while one-off interactions tend to defect. (Source: Ch 3.4.8, "Group survival")

11. **Free-riders need to be detected and managed.** Groups face threats from social loafing (member effort decreases as group size increases) and from members exploiting the group's benefits without contributing. Punishment of free-riders is costly to the punisher but stabilises cooperation. (Source: Ch 3.4.8, "Group survival"; Ch 3.4.9, "Group problem solving")

12. **Estimates given by professionals are anchored on the customer's number.** Jørgensen and Sjøberg showed that professionals' estimates are strongly shifted by the customer's offered estimate. When engaging stakeholders during estimation, the order in which information is exchanged matters. (Source: Ch 5.3, "Resource estimation")

## Questions to Ask During Stakeholder Engagement

### Phase 1: Mapping (identifying who is at the table and who isn't)

| Need | Question |
|---|---|
| Identify the network of stakeholders, not just the visible ones | Who would PageRank-style network analysis identify as salient, beyond the people I've already named? Have I done a snowball sampling pass — asking each named stakeholder who else should be involved? |
| Identify the implicit stakeholders (those without a seat at the table) | Whose interests are affected by this decision but who isn't represented? Maintainers of dependent systems? Future users? The build team? |
| Map the information-asymmetry structure | Which parties have more information than they share? Who has intimate familiarity that would deter competing alternatives? |
| Identify the cultural boundaries that cross the stakeholder set | What cultural assumptions does each stakeholder bring (geographic, generational, departmental, professional)? Where will embodied-cultural differences trip up communication? |

### Phase 2: Framing (defining the engagement question)

| Need | Question |
|---|---|
| Is this engagement under risk or uncertainty? | If under uncertainty, expect heuristic-driven behaviour from stakeholders, not optimisation. |
| What is the cost-benefit of engaging vs not engaging this stakeholder? | If a stakeholder has low salience and high engagement cost, deferring their input may be defensible. If high salience and low cost, prioritise. |
| What information asymmetry exists, and how can it be reduced? | Source-code escrow, public APIs, documentation requirements, transparent change-control, third-party audit — each reduces information asymmetry differently. |
| What is the contract type, and what dynamics does it create? | Fixed-price drives different behaviour than time-and-materials. Standard form contracts favour the drafter. |

### Phase 3: Convening (designing the engagement format)

| Need | Question |
|---|---|
| What is the right scale of group? | Brainstorming groups consistently underperform individuals on idea generation, per Jones (Ch 3.4.9). Social loafing scales with group size. If the goal is idea generation, use individuals first and combine later. |
| What is the right cultural register? | Cultural intelligence requires cognitive and embodied adaptation. Be deliberate about communication-style differences across the group. |
| What is the speaking order? | The Asch conformity result shows that group decisions are biased by the order of speakers. Use private input collection before group discussion. |
| How will free-riders be detected? | If the group is large enough for social loafing, design the engagement so individual contributions are visible. |

### Phase 4: Surfacing conflict (welcoming productive disagreement)

| Need | Question |
|---|---|
| Distinguish process conflict from relationship conflict | Process conflict (about how to do the work) is generally productive; relationship conflict (interpersonal animosity) is harmful regardless of intensity. |
| Reduce anchoring on the customer's first number | When estimating, separate the elicitation of stakeholder priorities from the customer's existing number; otherwise the priorities will be shifted by the anchor. |
| Watch for moral hazard | Is a stakeholder making decisions on the basis of personal enjoyment, career incentives, or revenge — rather than on the basis of stated project interests? |

### Phase 5: Reaching agreement

| Need | Question |
|---|---|
| Use fixed-budget allocation for requirements prioritisation | Each stakeholder allocates a fixed unit budget across the requirements; the variance reveals which priorities depend on which individuals. |
| Pre-commit against future scope creep | The signing of a contract is the start of cost negotiation; design the agreement to make scope-change costs visible and traceable. |
| Build credible commitment | Without enforcement, reputation, or repeated interaction, agreements unravel under future pressure. Design for repeated interaction or reputational reasons to honour the agreement. |
| Address voiceless stakeholders structurally | Future users, dependent systems, environment — all need credible proxy representation if their interests are to be reflected in the agreement. |

### Phase 6: Ratifying

| Need | Question |
|---|---|
| Lock in the legal terms with information-asymmetry awareness | Contract provisions for transparency (escrow, documentation, change-control) reduce the post-contract information advantage of the implementing vendor. |
| Plan for the post-ratification information asymmetry | The vendor that implements the system will become the information-asymmetric party for any subsequent change. Design the agreement to allow third-party alternatives to be viable. |

### Phase 7: Post-engagement

| Need | Question |
|---|---|
| Sustain the long-running relationship through repeated interaction | Cooperation through direct reciprocity is stable when the probability of repeat interaction meets the cost/benefit threshold. Sustain the relationship by maintaining repeat-interaction dynamics. |
| Track free-rider dynamics over time | Social loafing increases with group size; in long-running stakeholder relationships, watch for member effort to drop as the group scales. |
| Re-check the information-asymmetry structure | Has the vendor accumulated enough familiarity with the system to deter competing alternatives? If so, what mitigation is available (source code review, third-party audit, document deliverables)? |

## What to Look For

- **Loudest stakeholders treated as most salient.** Network-position analysis would often identify quieter stakeholders as more structurally central. Signal: engagement is shaped by the most vocal parties. Diagnosis: the salience mapping relied on who spoke up, not on who is structurally connected. Follow-up: run a snowball-sampling pass to find the overlooked.
- **Customer's first number anchoring the engagement.** Estimates and priorities align suspiciously closely with the customer's opening position. Signal: the team's estimates cluster near what the customer said first. Diagnosis: anchoring is operating. Follow-up: separate elicitation of team priorities from the customer's stated number before combining.
- **Information asymmetry hardening post-contract.** The implementing vendor becomes the sole party with intimate system knowledge, making alternative providers non-viable. Signal: renewal discussions produce no credible alternative bids. Diagnosis: the contract lacked information-asymmetry mitigation provisions. Follow-up: design escrow, documentation deliverables, and public API requirements into the next agreement.
- **Social loafing scaling with group size.** In large stakeholder groups, individual effort drops and free-rider dynamics emerge. Signal: in groups above 6–8, some participants are visibly less engaged than in smaller settings. Diagnosis: group size has exceeded the threshold where individual accountability is natural. Follow-up: design individual-contribution visibility into the engagement structure.

## When to Use This Reference

- A vendor-client engagement needs analysis of the information-asymmetry and moral-hazard dynamics shaping the relationship, not just the surface requirements.
- A stakeholder network is large or unclear and the team needs a defensible quantitative method for identifying who matters most.
- Requirements prioritisation is producing results that feel driven by one or two voices; fixed-budget allocation is the structural alternative.
- An estimate anchoring problem is suspected — the team's numbers are tracking the customer's opening position.
- A long-running stakeholder relationship is showing signs of cooperation breakdown and the team needs a framework for diagnosing why.
- Cross-cultural engagement is in play and the team needs to go beyond cognitive awareness to embodied-cultural-pattern attention.

## Worked Example

A mid-size digital-agency is contracted to build a compliance-management platform for a financial-services client. The initial stakeholder-mapping exercise identifies four groups: the client's compliance team (primary), the client's IT group (secondary), the agency's development team (third), and the platform's eventual end users — compliance officers at the client's corporate customers (fourth). The fourth group has no representative in the engagement.

**Network analysis.** A snowball-sampling pass surfaces two compliance officers at the client's largest corporate customer who have been consulted informally about the requirements but are not in any formal engagement. PageRank-style network mapping shows them as structurally central — they will shape adoption in the corporate-customer segment the client depends on for revenue. They are invited into a structured requirements session. (Source: Ch 5.4.5, "Discovering functionality needed for acceptance")

**Fixed-budget allocation.** The compliance team, IT group, and the two newly-included corporate-customer officers each allocate 100,000 units across 18 candidate requirements. The leave-one-out variance analysis shows that three requirements' priority rankings are almost entirely driven by the IT group; without IT input, those three requirements would not appear in the top 10. This is flagged: the IT group's priorities may not reflect end-user value. (Source: Ch 5.4.5)

**Information-asymmetry mitigation.** The contract is a time-and-materials arrangement. The agency recommends adding three provisions: source-code escrow, a public API on the compliance-data layer, and a documentation deliverable at each sprint boundary. The client initially resists; the agency explains that without these, the client's maintenance-renewal conversations will have no credible competitive alternative. The provisions are added. (Source: Ch 3.4.6, "Information asymmetry")

**Anchoring guard.** During sprint-5 scope discussion, the client mentions their expectation that a new integration feature will cost "around 40 hours." The agency separates the estimation session from the client's opening statement, producing independent estimates before disclosing the client's figure. The independent estimate is 110 hours. The gap is surfaced and resolved before any commitment. (Source: Ch 5.3, "Resource estimation")

The scenario is operator-authored; all framework citations trace through `references/jones-evidence-based-sweng-deep.md`. Stakeholder-network analysis via PageRank (Ch 5.4.5), fixed-budget allocation (Ch 5.4.5), information-asymmetry structure (Ch 3.4.6), anchoring on the customer's number (Ch 5.3), and cooperation-threshold conditions (Ch 3.4.8) are `[AP]`- or `[V]`-marked passages in the deep ref. No verbatim source blockquotes appear in this distillation.

## Anti-patterns This Reference Helps Avoid

- Treating the first-listed or loudest stakeholders as the most salient, without testing against network-position metrics.
- Allowing the customer's first number to anchor the requirements prioritisation; the resulting estimates will be shifted toward the customer's preference, not the team's best estimate.
- Treating moral hazard as a hypothetical rather than a structural feature of long-running stakeholder relationships.
- Using fixed-price contracts where the requirements are uncertain and information asymmetry favours the vendor; designing the agreement without the information-asymmetry mitigation mechanisms (escrow, public APIs, documentation deliverables).
- Treating brainstorming groups as productive idea-generating mechanisms; the evidence shows individuals consistently outperform groups for idea quantity and quality.
- Allowing social loafing to scale silently in large stakeholder groups, without making individual contributions visible.
- Allowing the post-contract information asymmetry to deter competing maintenance bids; the established vendor's intimate familiarity with the system becomes a moat that traps the client.
- Generalising stakeholder-engagement practices across cultural boundaries without attending to embodied differences (time-as-space, category boundaries, communication style).
- Treating reciprocity-based cooperation as automatic; it requires the probability of repeat interaction (or reputation knowledge) to meet a quantitative threshold.

## Integration with Other References

| Reference | Connection |
|---|---|
| OpenStax *Business Ethics* (this corpus) | Normative ethical theories of stakeholder claims (utilitarianism, Kantianism, virtue ethics), Donaldson-Preston stakeholder theory, Mitchell-Agle-Wood as an ethical frame — these are outside Jones's scope. Use OpenStax Business Ethics for the normative frame; use Jones for the evidence-grounded economic analysis. |
| OpenStax *Organizational Behavior* (this corpus) | OB's conflict-mode selection (TKI five modes), power bases, and negotiation stages are the theoretical complement to Jones's agency-theory analysis. Process conflict vs relationship conflict (Jones's framing) maps onto OB's conflict-management framework. |
| Letaw, *Handbook of Software Engineering Methods* (this corpus) | Letaw's requirements-elicitation methods (interviews, focus groups, lab studies, exploratory research) are how the Product Owner gathers stakeholder input; Jones's fixed-budget allocation and network-analysis methods are how that input gets prioritised and weighted. Use Letaw for elicitation; use Jones for prioritisation and structural analysis. |
| Liberating Structures Handbook (this corpus) | The LS handbook assumes good-faith conversation with the people most affected; Jones surfaces the structural ways vendor-client engagement can be distorted by contract dynamics. Use Jones to surface the distortion; use LS to design the conversation that mitigates it. |
| Open Practice Library (this corpus) | OPL's *Formal Relational Contract* and *Stakeholder RACI Map* are the operational counterparts to Jones's analysis of how contract type shapes the stakeholder relationship. OPL gives the practice; Jones gives the economic rationale for why it matters. |
| Scrum Guide (this corpus) | The Scrum Guide assumes good-faith Product-Owner-to-stakeholder engagement; Jones surfaces the information asymmetries and incentive structures (bidding dynamics, moral hazard) that can distort this engagement in practice. Use Jones when the question is "what structural distortions should we design against?"; use the Scrum Guide for the engagement structure itself. |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The following authors and bodies are cited in the source but are not held as primary references in this corpus:
- Mitchell, Agle, and Wood — stakeholder salience model (Ch 5.4.5) [BT]
- Lim (RALIC study at UCL) — PageRank-based stakeholder-network analysis (Ch 5.4.5) [BT]
- Regnell et al. — fixed-budget allocation for requirements prioritisation (Ch 5.4.5) [BT]
- Ahonen et al. — fixed-price vs time-and-materials management overhead study (Ch 5.2.1) [BT]
- Jørgensen and Sjøberg — anchoring study on professional estimates (Ch 5.3) [BT]
- Asch — conformity and speaking-order effects on group decisions (Ch 3.4.9) [BT]
- Axelrod — reciprocity and cooperation theory (Ch 3.4.8) [BT]

**Named limits of the source.** The text explicitly acknowledges or implies these scope boundaries:
- Normative ethical theories of stakeholder claims (utilitarianism, Kantianism, virtue ethics, Donaldson-Preston stakeholder theory) are not addressed; Jones's analysis is economic, not ethical.
- Broad governance, board structures, or community engagement beyond software development are outside scope.
- TKI conflict-mode selection, formal negotiation theory beyond agency theory, are not addressed.
- The Mitchell-Agle-Wood salience model is mentioned but used as an algorithmic ranking method, not as an ethical framework.
- Jones explicitly disclaims rigour on some of his own models: "most of these models were created by your author after seeing the data, what is sometimes known as HARKing" [V] (Ch 1, "What has been learned?").

**Evidence-marker continuity.** The deep reference at `references/jones-evidence-based-sweng-deep.md` uses `[V]`, `[AP]`, `[AR]`, `[AE]`, and `[BT]` markers inline throughout. The PageRank stakeholder-network study (Ch 5.4.5) is `[AP]`; the information-asymmetry framing (Ch 3.4.6) is `[AP]`; the anchoring study on professionals' estimates (Ch 5.3) is `[AP]`; the borrowed-through citation chain (Mitchell-Agle-Wood, Regnell, Jørgensen-Sjøberg, Asch, Axelrod) is `[BT]`. Jones's contrarian positions (HARKing disclaimer, evidence-based research as "essentially a blank slate") are `[AR]`. This distillation paraphrases throughout; no verbatim blockquotes appear here.
