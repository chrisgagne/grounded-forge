
# Letaw, Handbook of Software Engineering Methods (light reference)

**Source:** Letaw, L. (2024). *Handbook of Software Engineering Methods* (2nd ed.). Oregon State University, Corvallis, OR. Licence: CC BY-NC 4.0. https://open.oregonstate.education/setextbook/.
**Structure:** Introduction plus 8 chapters — Agile; Project Management and Teamwork; Requirements; Unified Modeling Language Class and Sequence Diagrams; Monolith versus Microservice Architectures; Paper Prototyping; Inclusivity Heuristics; Code Smells and Refactoring. Single-author book authored by Lara Letaw at Oregon State University; ISO/IEC/IEEE 24765:2017 is the source of the working definition of software engineering.

## Author's thesis (condensed)

This is a methods catalogue, not a software-engineering primer. Letaw's aim is to introduce a portable set of *software engineering methods* — ways people achieve specific objectives in software engineering — that can save a project, with guidance on when and why to use each. Software engineering is treated as a "gray area" where right answers depend on context; the book selects methods known to be useful across multiple contexts and points to fuller treatments elsewhere. The purpose of software engineering is to create sustainable, extensible programs that solve problems people care about.

Three load-bearing positions structure the book. First, it is *Agile-biased by design*: most of the methods are Agile-friendly because most contemporary teams work in Agile environments (HP 2017 survey: 51% leaning Agile, 16% pure Agile, 24% hybrid). Second, *risk reduction is the through-line*: each method is presented as a way to manage the probability of negative project outcomes (definition of risk = "the estimated probability of a loss given a set of known and unknown factors"). Third, *software is for humans, not computers*: UML diagrams must communicate to humans, the Inclusivity Heuristics start from human diversity, code smells matter because smelly code is hard for humans to maintain.

## Agile and the software development life cycle

The SDLC has five stages — Requirements, Design, Implementation, Testing, Maintenance — and software process models are patterns for traveling through them. Agile and Waterfall are the two contrasted models; Letaw notes the irony that Waterfall is most associated with Royce's (1970) article whose central claim is that Waterfall has serious flaws. Scrum is the Agile framework foregrounded: three Scrum Team roles (Scrum Master, Product Owner, Developers); five events (Sprint of one month or less, Sprint Planning, Daily Scrum at 15 minutes, Sprint Review, Sprint Retrospective); three artifacts (Product Backlog, Sprint Backlog, Increment). Three Agile methods that travel beyond Scrum are surfaced: Scrum board (columnar visualisation of work), Spike (focused investigation to answer a question or choose a path), and User story (a feature description in the "As a <role> I can <capability>, so that <receive benefit>" template).

## Project management and teamwork

Project management balances the *triple constraint*: time, cost, and scope (scope includes quality). The Managerial Skill Mix (Badawy, 1995) is interpersonal, technical, and administrative/conceptual. Three communication methods: ground rules (preemptive or reactive rules with whole-team buy-in, organised around eight diagnostic questions); RACI matrix (Responsible/Accountable/Consulted/Informed); fist of five (six-level voting from None to Five, with two-or-fewer triggering discussion). For project definition: project priority matrix (Constrain/Enhance/Accept per constraint, set once with the client); Eisenhower matrix (Do/Decide/Delegate/Delete on urgent × important); planning poker for estimation in story points or ideal days, with team-revealed cards driving discussion until estimates converge; project network diagram (Activity-on-Node directed graph showing task dependencies); task-management systems like Asana, Jira, Trello. Team development uses Tuckman's five stages (Forming, Storming, Norming, Performing, Adjourning) as the background frame.

## Requirements

Two types: functional ("a description of a behavior that a system will exhibit under specific conditions") and nonfunctional ("a description of a property or characteristic that a system must exhibit or a constraint that it must respect") — both definitions from Wiegers & Beatty (2013). Eight-attribute "good requirement" standard from Texas DIR (2008): correct, unambiguous, complete, consistent, ranked for importance/stability, verifiable, modifiable, traceable. Elicitation methods include interviews, focus groups, lab studies, and exploratory research; five factors complicate developer-led elicitation (lack of expertise, bad ideas, not knowing what they want, wanting what's bad for them, being human). Nonfunctional requirements split into *quality attributes* (nine catalogued: maintainability, portability, reliability, efficiency, integrity, memorability, flexibility, interoperability, reusability) and *constraints* (typically externally mandated; quality attributes are internally chosen). User-story specification uses **INVEST** (Independent, Negotiable, Valuable, Estimable, Small, Testable) from Wake (2003); acceptance criteria establish a Definition of Done, often in given-when-then format. Use cases are a more formal alternative (Name, Actor(s), Flow of events as required parts; identifier, preconditions, postconditions, business relevance, dependencies, extensions, priorities, nonfunctional requirements as optional parts) — less common in Agile and therefore summarised rather than expanded.

## UML class and sequence diagrams

UML is "a family of graphical notations for describing and designing software through diagrams"; published 1994, OMG standard 1997, ISO standard 2005, currently version 2. Five benefits: notation for designing and describing, forcing structured thinking, multi-level views, common language between professionals, communication without code-reading. Three drawbacks: notation variation, time cost when overdone, maintenance cost when designs change. *Class diagrams* describe classes and their static relationships, with attributes (`+` public, `−` private, `#` protected) and operations; key notations cover Notes, Class, Association (uni- and bidirectional with property names and source/target multiplicities), and Inheritance ("Class2 is a Class1"). *Sequence diagrams* describe interactions between objects (or other participants — users, databases) for a single use case; key notations cover Participant, Lifeline (dashed vertical line, top = beginning, bottom = end), Message (solid arrow), Activation Bar (call-stack indicator), Return (dashed arrow, used sparingly), Self-Call, Deletion (X on lifeline). The chapter's signature framing is that "UML diagrams are for communicating with humans — not computers."

## Monolith versus microservice architectures

A monolith is one interconnected codebase that cannot easily be divided into independent components; arises by default unless architecture is actively chosen. Microservices are separate applications, each running in its own process and independently useful. The chapter's organising structure borrows five subheadings from Lewis & Fowler (2014): *smart end points and dumb pipes* (REST API, services do translation), *componentization via services* (a component is "a unit of software that is independently replaceable and upgradeable"; advantages = independence and standardised communication; disadvantages = more expensive and potentially less secure communication), *organized around business capabilities* (each service maps to a business capability per Michell (2011); each service can have its own tech stack), *decentralized data management* (each service has its own database, eventual consistency, failure containment as a benefit), *decentralized governance* (compatibility only at the interface), and *design for failure* (service-specific monitoring, logging, fail-handling). Six structured comparisons close the chapter (communication, deployment, scaling, testing, upgrading, database). The OSU CASS / ODOT TOCS migration case study illustrates the pattern in practice: monolith → microservices was driven by tight coupling, deploy-frequency limits, database contention, and platform deprecation (.NET 4.8 → .NET 6, with Apache ActiveMQ/AMQP as the message broker and JSON for the Profile Service).

## Paper prototyping

Prototype fidelities: *low* (rough sketch, gather feedback on high-level features), *medium* (detailed, gather feedback on small changes to accepted features), *high* (polished, gather feedback on detailed tweaks). A paper prototype is a hand-drawn low-fidelity sketch; it need not be pretty, need not be static (cut shapes, arrows, annotations, strings, brass brads), and should be the size that just communicates the concept — going further is waste if the client rejects the design. Feedback method: swap drawings as users interact with the entry screen, with a *think-aloud protocol* asking the user to verbalise what they're doing, trying to do, thinking, and disliking.

## Inclusivity Heuristics

A set of eight guidelines for designing technology to work well across cognitive styles, developed at Oregon State University as part of the GenderMag Project (Burnett et al., 2016, 2021). Five cognitive facets shape interaction: attitude toward risk, computer self-efficacy, information processing style, learning style, motivations. Three personas — Abi, Pat, Tim — embody distinctive combinations of cognitive styles. The heuristics are used inside *heuristic evaluation* (Nielsen & Molich, 1990): multiple evaluators check independently, then compare findings. The eight heuristics: (1) Explain benefits of features; (2) Explain costs of features; (3) Let users gather as much information as they want, and no more; (4) Keep familiar features available; (5) Make undo/redo and backtracking available; (6) Provide an explicit path through the task; (7) Provide ways to try out different approaches; (8) Encourage tinkerers to tinker mindfully. Each heuristic is presented with a worked design example and per-persona reactions. Future planned extensions include socioeconomic diversity (Hu et al., 2021) and age diversity (McIntosh et al., 2021).

## Code smells and refactoring

Code smells are indications that code is undergoing *code decay* — a sign the code needs to be reorganised. Three reasons to care: smelly code is hard to maintain; smelly code leads to smellier code (the CSS `!important` workaround is the canonical example of laziness propagation); smelly code accumulates *technical debt* that may eventually require redevelopment or end the project. *Refactoring* is improving code without changing what it does. Four comment smells: Obsolete Comment, Commented-Out Code, Redundant Comment, Long Comment — each with a remove-or-update prescription. Three function smells: Long Function (>10 lines; aim for 5 or fewer), Function with Many Jobs, Function with Many Parameters (>4, some say >3). Four general code smells: Duplicate Code, Long Lines (>100 characters), Inconsistent Conventions, Vague Naming. The chapter's framing claim is that "too many comments can be as bad as none" — over-commenting introduces out-of-date risk, distracts from important comments, and may indicate the code itself needs to be simplified.

## Key statistics

| Metric | Value |
|---|---|
| Organisations leaning toward Agile (HP 2017, n=601) | 51% |
| Organisations using pure Agile | 16% |
| Organisations using a hybrid model | 24% |
| Organisations leaning toward Waterfall | 7% |
| Organisations using pure Waterfall | 2% |
| Agile adopters citing enhanced collaboration (HP 2017, n=403) | 54% |
| Agile adopters citing increased software quality | 52% |
| Agile adopters citing increased customer satisfaction | 49% |
| Software-project failure rate FY2011-2015 (Standish CHAOS) | 17%–22% of 25,000+ projects |
| Daily Scrum length | 15 minutes |
| Sprint length cap | one month or less |
| Long-function threshold | >10 lines (aim for ≤ 5) |
| Function-with-many-parameters threshold | >4 (some say >3) |
| Long-line threshold | >100 characters |
| Inclusivity Heuristics research base | 40+ publications on gender differences in tech use |

## Key connections

- *Agile Manifesto* (Beck et al., 2001): grounding document for the Agile chapter.
- *Royce (1970)*, "Managing the development of large software systems": cited critically/ironically — Waterfall is associated with an article whose central claim is that Waterfall has serious flaws.
- *Schwaber & Sutherland (2020), Scrum Guide*: primary source for the Scrum framework definitions used throughout Chapter 1.
- *Cohn (2006), Agile Estimating and Planning*: source for story points, ideal days, and planning poker.
- *Tuckman (1965); Tuckman & Jensen (1977)*: five-stage team-development model used as the background frame for Chapter 2.
- *Badawy (1995), Developing Managerial Skills*: source for the three-category Managerial Skill Mix.
- *Larson & Gray (2018)*: Activity-on-Node project network diagram format.
- *Wiegers & Beatty (2013), Software Requirements*: primary source for the functional/nonfunctional and quality-attribute definitions.
- *Wake (2003), "Invest in good stories"*: source of the INVEST acronym.
- *Texas DIR (2008)*: source for the eight-attribute good-requirement standard.
- *Hanington & Martin (2019), Universal Methods of Design*: pointer for fuller elicitation methods.
- *Fowler (2004), UML Distilled*: source for class-diagram property/operation definitions and a pointer for sequence diagrams.
- *Lewis & Fowler (2014); Fowler (2015, 2019)*: organising frame for Chapter 5; subheadings borrowed.
- *Michell (2011)*: business-capability definition used in microservices framing.
- *Snyder (2011), Paper Prototyping*: source for fidelity-level distinctions.
- *Burnett et al. (2016, 2021), GenderMag project*: source of the Inclusivity Heuristics and the five cognitive facets.
- *Nielsen (1994); Nielsen & Molich (1990)*: heuristic evaluation as a usability inspection method.
- *Martin (2009), Clean Code*: source for the technical-debt narrative in Chapter 8.
- *Fowler & Beck (2019), Refactoring*: further refactoring guidance.
- *ISO/IEC/IEEE 24765:2017*: source of the software-engineering definition used throughout.

## Signature contrarian positions

1. **Software engineering is a "gray area" of computer science.** Right answers depend on context; SE questions are about team-process success ("How does my team know this software is ready to release?") more than algorithmic correctness.
2. **Agile beats Waterfall as the default frame.** The book is deliberately Agile-biased because the empirical base shows Agile dominates real-world software process choice — and Waterfall is most associated with the article that itself critiques Waterfall.
3. **Risk is the through-line, not a side concern.** Each method is justified as risk reduction; project work that doesn't name and track risk is treated as missing the point.
4. **Communication beats correctness in UML.** "What's most important when creating diagrams is not following the rules or conventions but communicating with your audience." A formally-correct diagram that nobody understands has failed.
5. **Too many comments can be as bad as none.** Over-commenting goes stale, distracts from the important comments, and may indicate the code itself needs to be simplified.
6. **One-size-fits-all UI design is harmful.** The Inclusivity Heuristics frame against UI design tuned to a single cognitive style (typically the designer's), in favour of design that supports the spread across each of the five cognitive facets.
7. **Ground rules-as-performative-compliance invalidate themselves.** Letaw warns specifically that rules feeling "silly, phony, too aspirational, too inflexible, or too authoritative" can undermine the team-formation work they were meant to support.
8. **Inclusive design is a methodology, not a feature.** Drawing on Microsoft's inclusive-design language, the heuristics treat design-for-diversity as the underlying method rather than an accessibility afterthought.
