# Software-Business

**Slug:** `software-business`
**Purpose:** Help a founder, CTO, engineering manager, or technical product leader work the intersection of running a software business and building the software itself, where the *software* part of the question materially shapes the answer rather than washing out into generic decision-making or generic stakeholder communication.

## 1. Problem statement

Software-business work is the set of decisions and practices at the intersection where the technical and the commercial constrain each other. A founder pricing a feature, a CTO defending technical-debt remediation to a board, an engineering manager structuring a team for predictable delivery, a product leader negotiating the build-vs-buy line against a partner roadmap: all sit in this intersection. The practitioner reaches for this axis when the question turns on a software-specific economic, organisational, legal, or operational consideration that a general business framework cannot resolve and a pure engineering framework cannot price. The corpus catches the cases where Jones's empirical findings on software-engineering ecosystems, Letaw's method discipline, the software-relevant chapters of the OpenStax business volumes, and the methodology-and-facilitation sources combine to discipline the decision.

## 2. Practitioner questions

- How do I price this feature, product, or service when our engineering effort and our competitor's engineering effort are uneven?
- How do I make a build-vs-buy decision when the buy option locks me into a partner's roadmap?
- How do I structure my engineering team for our current stage (founding / product-market-fit / scaling / maturity) without over- or under-hiring?
- How do I report technical work, technical debt, or reliability risk to a board that does not read code?
- How do I think about reliability, security, or compliance investment as a financial decision rather than as an engineering virtue?
- How do I plan a product roadmap that respects engineering capacity, accounts for technical-debt servicing, and lands the commercial commitments I have already made?
- How do I handle a software-specific risk event (incident, breach, defect, outage, regulator inquiry) across the technical, legal, PR, and customer-relationship dimensions?
- How do I structure the relationship between product, design, engineering, and go-to-market without recreating the dysfunctions Conway's Law predicts?
- How do I integrate AI capability into our product without inheriting the consultant-derivative cluster's framings of what AI is for?
- How do I evaluate an acquisition target's engineering health, technical risk, and integration cost as part of the deal valuation?

## 2a. Runtime listener grain

**Trigger unit:** an operator-described situation that names a software-business concern in software-and-business terms (a feature with both a price and a build-cost; a technical decision with a board-reporting consequence; an engineering structural choice with a customer-experience downstream). Generic management or generic engineering framings should route through `decision-making` or `stakeholder-engagement` axes instead; software-business fires when the technical and commercial constrain each other simultaneously.

**Response unit:** the framework or empirical finding from the corpus that prices the technical-commercial trade-off, plus the deliverable shape (board memo, roadmap entry, decision record, hire/role spec, incident write-up) the practitioner is producing.

### Seed trigger→response table

**Phase 1, Strategic positioning** (pricing, market entry, build-vs-buy, portfolio decisions, AI integration choices)

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| Operator names a pricing decision tied to engineering effort | Cost-classification primitives (`openstax-accounting-vol2`), pricing strategies (`openstax-principles-marketing`), capacity-vs-flow framing (`open-kanban`, `jones-evidence-based-sweng` on resource estimation) |
| Operator frames a build-vs-buy decision | Make-or-buy relevant-cost analysis (`openstax-accounting-vol2`), agency theory in vendor-client relations (`jones-evidence-based-sweng`), microservices boundary case (`letaw-handbook-sweng-methods`) |
| Operator names market entry or product-portfolio decision | Five-forces and PESTEL (`openstax-principles-management`), entrepreneurship pivot framework (`openstax-entrepreneurship`), product-economics in the cognitive-capitalism chapter (`jones-evidence-based-sweng`) |
| Operator describes an AI-integration decision (productisation, build/buy, vendor selection) | Cognitive-capitalism + agency-theory framing (`jones-evidence-based-sweng`), externalised-cost frame (architecture's `llm-epistemology.md` plus `openstax-business-ethics`) |
| Operator names a competitive-response decision with engineering implications | Strategy-environment-scan framing (`openstax-principles-management`), Conway's-Law-shaped team-structure question (`letaw-handbook-sweng-methods`) |

**Phase 2, Product and engineering economics** (technical-debt servicing, capacity planning, ROI on engineering investment, reliability-as-business-decision)

| Trigger | Response |
|---|---|
| Operator names technical-debt remediation against revenue work | Relevant-cost discipline (`openstax-accounting-vol2`), Jones on the post-1980 evidence collapse and KLOC-power-law mythology (`jones-evidence-based-sweng`) |
| Operator describes a reliability investment against a commercial milestone | Jones on the bi-exponential fault-report pattern and reliability statistics, CVP + breakeven framing (`openstax-accounting-vol2`) |
| Operator names a capacity-planning decision (hiring, contractor mix, team size) | Resource estimation under uncertainty and the cone of uncertainty as artefact (`jones-evidence-based-sweng`), triple-constraint discipline (`letaw-handbook-sweng-methods`) |
| Operator describes a roadmap-capacity mismatch | Velocity / capacity-adjusted velocity formula (`approach-perfect-field-guide-scrum-events`), flow economics over utilisation (`open-kanban`) |
| Operator names a "speed vs quality" tension | Jones on the survival-adjusted maintenance-to-development ratio, Goldratt theory of constraints (`openstax-accounting-vol2`), Sprint Goal discipline (`scrum-guide-2020`) |

**Phase 3, Team and capability building** (hiring, structure, levelling, culture, succession)

| Trigger | Response |
|---|---|
| Operator names a hiring or role-structure decision for software work | Organisational-design primitives (`openstax-principles-management`, six structures from Mintzberg), Tuckman team-stage map (`letaw-handbook-sweng-methods`) |
| Operator describes an engineering-management culture decision | Organisational-behaviour individual-and-group level (`openstax-organizational-behavior`), psychological-safety + authority-gradient (`nhs-just-culture-guide` cross-axis) |
| Operator names a levelling, performance, or compensation decision | Motivation frameworks (Maslow, Herzberg, SDT) at `openstax-principles-management`, `openstax-organizational-behavior`; Pink-style autonomy/mastery/purpose contrast |
| Operator describes a succession or knowledge-transfer concern | Tacit-knowledge / Nonaka-Takeuchi (`openstax-principles-management` Ch 18.6, the corpus's only substantive treatment), Jones on cognitive-capitalism |
| Operator names a contractor / vendor / hybrid-team decision | Agency theory and moral hazard in vendor-client relations (`jones-evidence-based-sweng`), Letaw on RACI and decision rights |

**Phase 4, Operations and process** (delivery cadence, governance, decision rights, change management)

| Trigger | Response |
|---|---|
| Operator names a delivery-cadence question (sprints, releases, deployment frequency) | Scrum framework (`scrum-guide-2020`), facilitation depth per event (`approach-perfect-field-guide-scrum-events`), Kanban flow primitives (`open-kanban`) |
| Operator describes a change-management situation specific to software work | Open Practice Library options for foundation/discovery/options/delivery phases (`open-practice-library`), Liberating Structures for engagement (`liberating-structures-handbook`) |
| Operator names a governance or decision-rights ambiguity | RACI + decision-rights mechanics (`letaw-handbook-sweng-methods`), Disagree and Commit / 1-2-4-All (`open-practice-library`) |
| Operator describes a systems-mapping or causal-loop need to diagnose a delivery system | Barbrook-Johnson & Penn methods catalogue (`barbrook-johnson-systems-mapping`), system archetypes (`ssdl-systems-thinking-foundations`) |
| Operator names a retrospective or learning-loop need | Field Guide retro (`approach-perfect-field-guide-scrum-events`), Kerth's Prime Directive, Open Practice Library blameless-postmortem |

**Phase 5, Risk, reliability, compliance** (incidents, security, legal, regulatory, ethics)

| Trigger | Response |
|---|---|
| Operator names an incident-response or post-incident-learning concern | NHS Just Culture decision aid (`nhs-just-culture-guide`), TC 25-20 AAR (`tc-25-20-army-aar`), LFUO Learning Review (`lfuo-learning-review-guide-2024`) |
| Operator describes a legal exposure (contract, IP, employment, consumer-protection) | OpenStax Business Law primitives (`openstax-business-law`), Business Ethics duty-of-care chapters (`openstax-business-ethics`) |
| Operator names a compliance investment with engineering cost | Cost-as-decision-relative (`openstax-accounting-vol2`), Jones on quality-cost statistics |
| Operator describes a security or reliability event with PR + customer dimensions | NHS Just Culture default-to-system framing (`nhs-just-culture-guide`), TC 25-20 spirit-and-climate (`tc-25-20-army-aar`), Business Ethics social-contract argument |
| Operator names an AI-ethics or extractive-cost question | Business Ethics normative-stakeholder frame (`openstax-business-ethics`), architectural framing in `docs/architecture/llm-epistemology.md` |

**Phase 6, Stakeholder communication** (board reporting, exec alignment, investor relations, customer messaging)

| Trigger | Response |
|---|---|
| Operator names a board-paper or exec-memo concern with technical content | Grunig-Hunt linkage model (`openstax-business-ethics`), Mitchell-Agle-Wood stakeholder prioritisation, plus the `business-executive-stakeholder` lens |
| Operator describes a fundraising or investor-update need | OpenStax Principles of Finance primitives (`openstax-principles-finance`), entrepreneurship funding-ladder (`openstax-entrepreneurship`) |
| Operator names a cross-function negotiation (engineering vs product vs sales) | TKI five negotiation modes (`openstax-business-law`), positions-vs-interests framing (`openstax-organizational-behavior` Ch 6) |
| Operator describes a customer-communication concern with technical content | Service-profit chain + Gap Model / RATER (`openstax-principles-marketing`), 5A customer journey |
| Operator names a CTO-to-board translation problem | The `cto` lens fires; Mintzberg's roles (`openstax-principles-management`), `business-executive-stakeholder` lens cross-cuts |

## 3. Available sources

All 27 sources in the demo corpus are candidates; per-source applicability decided by `creating-distillations` Pass G. Tiering for Pass G priority:

- **Strong fire (named in the build-profile description):** `jones-evidence-based-sweng`, `letaw-handbook-sweng-methods`, plus all twelve OpenStax titles (organizational-behavior, principles-management, principles-marketing, principles-finance, accounting-vol1, accounting-vol2, business-ethics, business-law, entrepreneurship, introduction-business, psychology-2e, economics-3e).
- **Moderate fire (methodology / facilitation / systems primitives that apply to software work):** `scrum-guide-2020`, `approach-perfect-field-guide-scrum-events`, `open-kanban`, `open-practice-library`, `liberating-structures-handbook`, `ssdl-systems-thinking-foundations`, `barbrook-johnson-systems-mapping`.
- **Light fire (facilitation / AAR sources that may apply to incident-response or learning-loop questions but are primarily other-axis):** `tc-25-20-army-aar`, `nhs-just-culture-guide`, `lfuo-learning-review-guide-2024`, `flo-facilitation-guide`. Pass G likely to skip or produce thin distillations.

## 4. Intended lenses

- `cto`: strong fire. The CTO-as-reader is the canonical software-business audience.
- `business-executive-stakeholder`: strong fire. The board-and-exec reader-type for whom the software-business intersection is most opaque.
- `pm-bounded-by-ba-role`: strong fire. The PM-bounded-by-business-analyst role that sits closest to the intersection.

Other lenses (`builder`, `agentic-builder`, `chris-gagne-consultant-coach`) may fire on specific questions but are not the primary lens-set for this axis.

## 4a. Intended runtime agents

None for v0.2.x. The software-business axis ships without practitioner-role agents; the deployed application reads the distillation index and the cross-axis fallback (`decision-making`, `stakeholder-engagement`) directly through the bundled CLAUDE.md.

## 5. Overlap

- **Significant with `decision-making`** on the strategic-positioning, product-economics, and operations phases. The same source (e.g. `openstax-principles-management`) projects differently onto each axis; the software-business projection sharpens to the technical-commercial intersection where decision-making's projection covers the broader decision discipline. Integration-section updates expected in the decision-making distillations for: `jones`, `letaw`, `openstax-principles-management`, `openstax-accounting-vol2`, `openstax-principles-finance`, `openstax-business-law`, `openstax-business-ethics`, `openstax-entrepreneurship`, `openstax-principles-marketing`.
- **Significant with `stakeholder-engagement`** on the stakeholder-communication phase. The Phase 6 communication patterns inherit from the stakeholder-engagement distillations of `openstax-organizational-behavior` and `openstax-business-ethics`; the software-business projection adds the CTO-to-board translation and engineering-content-translation specificity.
- **Light with `lfuo`, `tc-25-20`, `nhs-just-culture`** on incident-response. Pass G may skip these on software-business; if it fires, the projection should narrow to the software-specific failure-mode and avoid duplicating the facilitation-axis treatment.

## 6. Success criteria

In 3-6 months, a founder, CTO, engineering manager, or technical product leader using the deployed `software-business` app should be able to ask a question that turns on the technical-commercial intersection (a board memo, a build-vs-buy decision record, an incident write-up, a hire spec) and get back a source-grounded answer that names specific frameworks from the corpus (Jones on the post-1980 evidence collapse, Mintzberg's organisational structures, Goldratt's theory of constraints, the NHS Just Culture decision tree, Conway's Law as applied through Letaw), cites them through the deep references, and produces a deliverable in the shape the practitioner asked for. The falsifier: an LLM-judge eval comparing software-business app answers against (a) the same model running raw on the same question and (b) the decision-making app's answer where decision-making is the wrong axis, showing the software-business app citing software-specific empirical findings the other two methods do not surface. Bar: 60% of test queries with software-specific Jones / Letaw / Conway citations in the software-business answer that do not appear in the matched-decision-making baseline.

## Discipline

- **Verb-and-noun.** The axis covers "make a software-business decision" and "produce a software-business deliverable": verb-and-noun jobs in named circumstances. *Software-business* as a slug is a domain hint, not the job; the job is decided / produced.
- **Job × circumstance.** Every phase has a circumstance: pricing under partner-roadmap uncertainty, technical-debt remediation against board-reporting cycle, incident-response with PR + legal dimensions. Without the circumstance, route to `decision-making` or `stakeholder-engagement`.
- **Hire requires fire.** Adopting this axis fires: the consultant-derivative cluster's framings of software-business questions ("AI is what the consultant deck says it is", "technical debt is a virtue claim", "engineering capacity is a hiring problem"). The axis projects sources that price the trade-offs differently from the consultant-frequency mean.
- **Phases route from practitioner questions.** The six phases above derive from the §2 practitioner questions, not from any source's chapter structure.
- **Runtime listener grain.** The seed trigger→response tables in §2a name what fires the corpus in the moment. `creating-applications` inherits these to author the runtime tables in the distillation index; `creating-distillations` reads them at Pass G to map each source's content to the triggers it can address.
- **Pass G owns the per-distillation call.** The source set in §3 is the candidate; Pass G inside `creating-distillations` decides applicability per source, per distillation. The tiering is a hint, not a binding.
- **Lenses are operator-opt-in.** §4 names three strong-fire lenses; per-distillation applicability is decided at Pass G.

## Author anchors

- Christensen, *Competing Against Luck* (2016): JTBD framing.
- Jones, *Evidence-Based Software Engineering*: the empirical anchor for the software-specific claims this axis is built to surface.
- Conway, "How Do Committees Invent?" (1968): the team-structure-vs-product-structure mapping that runs underneath the team-and-capability-building phase, surfaced through Letaw's microservices and design chapters.
- Goldratt, *The Goal*: constraint thinking that runs underneath the product-and-engineering-economics phase, surfaced through OpenStax Accounting Vol 2's Theory of Constraints chapter.
