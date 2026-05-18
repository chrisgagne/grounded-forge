
# Letaw, Handbook of Software Engineering Methods (deep reference)

**Source:** Letaw, L. (2024). *Handbook of Software Engineering Methods* (2nd ed.). Oregon State University, Corvallis, OR. Licence: **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**. URL: https://open.oregonstate.education/setextbook/. ISBN not stated in source front-matter. Author contact: setextbook@lara.tech. Editor: Ashleigh McKown. Published by the Oregon State University Open Educational Resources (OER) Unit.
**Scope:** open-nc
**Structure:** Introduction (purpose, philosophy, second-edition changes); eight chapters — (1) Agile, (2) Project Management and Teamwork, (3) Requirements, (4) Unified Modeling Language Class and Sequence Diagrams, (5) Monolith versus Microservice Architectures, (6) Paper Prototyping, (7) Inclusivity Heuristics, (8) Code Smells and Refactoring; Conclusion; Glossary; consolidated References.
**Citation style:** `(Ch N, "Section name")`. The PDF was converted with pymupdf4llm 0.2.9, which produces footer-style page numbers (e.g., "Agile | 9") but does not preserve PDF page anchors as cite-able markers; section names from the converted markdown are used in their place.
**Coverage:** all substantive content (Introduction, Chapters 1–8, Conclusion, Glossary). The consolidated end-of-book References section duplicates per-chapter References and is summarised rather than enumerated.

## Author's thesis (paraphrased from source)

Letaw's stated aim is not to teach how to be a software engineer but to introduce a portable set of *software engineering methods* — "ways people achieve specific objectives in software engineering" — that "can save your project" (Introduction, opening) [V]. The definition of software engineering she adopts is the ISO/IEC/IEEE one (ISO/IEC/IEEE 24765:2017), which the source's Glossary entry renders as "Systematic application of scientific and technological knowledge, methods, and experience to the design, implementation, testing, and documentation of software" (Glossary, "software engineering") [V] [BT]. The Introduction notes that this definition "was agreed upon by the International Organization for Standardization (ISO), International Electrotechnical Commission (IEC), and the Institute of Electrical and Electronics Engineers (IEEE) and published in their glossary of systems and software engineering vocabulary" (Introduction, "What's Software Engineering?") [V] [BT]. The purpose Letaw assigns to software engineering is to help people "create sustainable, extensible programs that solve problems people care about" — where "Sustainable means it's feasible for the program to grow, exist, and be maintained" and "Extensible means it's feasible to add more features" (Introduction, "What's the Purpose of Software Engineering?") [V].

The book's organising claim is that software engineering is "a gray area of computer science": right answers can be hard to find and may not be reproducible in different contexts, the field keeps changing, and questions in software engineering look less like "Is this algorithm correct?" and more like "How does my team know this software is ready to release?" or "People keep misinterpreting my code; how do I shift it toward better understandability and maintainability?" (Introduction, "Software Engineering Is Not Black and White") [AP] [V]. From this premise, Letaw selects methods that are "known to be useful across multiple contexts," gives guidance on when and why to use them, and points readers to deeper resources for further study (Introduction, "It's Not Necessary to Study Every Detail") [AP].

A second load-bearing claim is that the book is *Agile-biased by design*: "this book is geared toward Agile software development" because Agile environments have become extremely popular and because the author endorses Agile (Introduction, "Agile Isn't Perfect, But I Really Like It"; Ch 1, "Agile") [V]. The Agile choice is evidence-backed in the text by a 2017 Hewlett Packard Enterprise survey: of 601 respondents, 51% were "leaning toward Agile," 24% used a hybrid, 16% were "pure Agile," 7% were "leaning toward Waterfall," and 2% were "pure Waterfall" (Ch 1.2, "Agile"; Hewlett Packard Enterprise, 2017) [V] [BT]. The same survey is cited for *why* organisations choose Agile: enhanced collaboration (54%), increased software quality (52%), increased customer satisfaction (49%), shorter time to market (43%), and reduced cost (42%) (Ch 1.2) [V].

A third load-bearing claim is that *the central output of every method is risk reduction*. Throughout the book Letaw frames each method as a way to manage the probability of negative project outcomes; the catalogue of risk-mitigation moves at the head of Chapter 2 is "defining and keeping track of your project, communicating with your project team, researching the implications of decisions, developing backup plans, and selecting suitable tools" (Ch 2, opening) [V]. The vocabulary is consistent: a *risk* is "the estimated probability of a loss given a set of known and unknown factors" (Ch 2, opening) [V]; *risk mitigation* is "an action taken in order to avoid a contingency" (Glossary) [V].

A fourth load-bearing claim is that *software is for humans, not computers*. UML diagrams "are for communicating with humans — not computers" (Ch 4.8, "Summary") [V]. The Inclusivity Heuristics start from the position that designing technology for "a diversity of users" is a methodology drawing on "the full range of human diversity" (Ch 7, opening, citing Microsoft) [V] [BT]. Code smells matter because "smelly code can be harder for you and others to maintain" and "leads to smellier code" (Ch 8.1, "Why Care about Code Smells?") [V].

## Part I: Agile and the software development life cycle (Ch 1)

### The SDLC and software process models

The software development lifecycle (SDLC) is "the progression of a software project through five SDLC stages" [V]: Requirements (figuring out and writing down what the software must do, how well, and under what limitations or constraints); Design (determining how the code will be structured and how users will interact with the software); Implementation (using the requirements and design to code the software); Testing (verification — that the code was written without fault — and validation — that the software is what the users or client want); and Maintenance (improving the software's existing functionality and code) (Ch 1.1, "The Software Development Life Cycle") [AP]. Patterns for traveling through the stages are called *software process models*; Agile and Waterfall are the two contrasting models the chapter foregrounds (Ch 1.1) [AP].

Letaw observes that Waterfall is "ironically" associated with an article that describes its major flaws: Royce's (1970) "Managing the development of large software systems," whose second figure depicts the model with seven stages and downward-only movement, suggesting that "movement to the previous stage is not allowed — you can't swim up a waterfall." Royce later in the same article proposes modifications, including a preliminary program design step that loops back to requirements as needed (Ch 1.1, "The Software Development Life Cycle"; Royce, 1970) [V] [BT].

Three justifications are given for studying multiple software process models: (1) to "detect and/or understand what a software development team is doing" — useful when joining a team and wanting to "ask good questions, identify what you see the team doing, and look competent in front of your team and managers"; (2) to have "ideas to choose from when you need to select a software process model or method for a new project"; and (3) to have "ideas to choose from when a project is in trouble" (Ch 1.1, "Why Care about Agile, Other Software Process Models, and Software Engineering Methods?") [V]. The CHAOS Report (Standish Group International, Inc., 2015) is cited for the claim that during fiscal years 2011-2015, "17% to 22% of software projects failed" out of the 25,000+ projects in the Standish database, "with the likelihood of project failure increasing drastically with project size" (Ch 1.1) [V] [BT].

### Agile and the Manifesto

The Agile philosophy is "summed up by the Agile *Manifesto for Software Development*" (Beck et al., 2001), which Letaw cites as the grounding document (Ch 1.2.1, "Agile") [AP] [BT]. The text positions Agile as "collaboration-oriented philosophy of creating software that values doing over comprehensive planning and documentation" (Introduction, "What's This Book Like?", topic 1) [V].

### Scrum: team, events, artifacts

Scrum is "a well-known framework for software project management" aligning with the Agile philosophy. The current Scrum Guide (Schwaber & Sutherland, 2020) divides the framework into three categories: *the team*, *the events*, and *the artifacts* (Ch 1.2.2, "Scrum") [V] [BT].

The Scrum Team "consists of one **Scrum Master**, one **Product Owner**, and **Developers**" [V] (Ch 1.2.2). The Scrum Master is "accountable for establishing Scrum as defined in the Scrum Guide" [V]; the Product Owner is "accountable for maximizing the value of the product resulting from the work of the Scrum Team" [V]; the Developers are "people in the Scrum Team that are committed to creating any aspect of a usable Increment each Sprint" [V] (Ch 1.2.2, "The Team"). Letaw summarises the focus split: the Scrum Master's focus is process, the Product Owner's focus is the product, and the Developers' focus is creating a product while following Scrum processes (Ch 1.2.2) [AP].

The five Scrum events are: the **Sprint** ("fixed-length development periods of one month or less. . . A new Sprint starts immediately after the conclusion of the previous Sprint"); **Sprint Planning** ("initiates the Sprint by laying out the work to be performed"); **Daily Scrum** ("a 15-minute event for the Developers . . . focuses on progress toward the Sprint Goal and produces an actionable plan for the next day of work"); **Sprint Review** ("to inspect the outcome of the Sprint and determine future adaptations . . . presents the results of their work to key stakeholders"); **Sprint Retrospective** ("to plan ways to increase quality and effectiveness . . . inspects how the last Sprint went") (Ch 1.2.2, "The Events") [V].

The three Scrum artifacts are: **Product Backlog** ("an emergent, ordered list of what is needed to improve the product"); **Sprint Backlog** ("composed of the Sprint Goal (why), the set of Product Backlog items selected for the Sprint (what), as well as an actionable plan for delivering the Increment (how)"); **Increment** ("a concrete stepping stone toward the Product Goal") (Ch 1.2.2, "The Artifacts") [V].

### Notable Agile methods

Three Agile methods are foregrounded as usable within Scrum or other frameworks: a **Scrum board** (organising and visualising tasks as cards on a board with columns for categories — can be a physical bulletin board or a feature of task-management software); a **Spike** ("a quick and to-the-point investigation for gathering information to help the team answer a question or choose a development path"); and a **User story** ("a short description of a software feature from the perspective of fulfilling a user need (e.g., using this format: As a <role> I can <capability>, so that <receive benefit>). Tasks, priorities, time/cost estimates, and acceptance criteria may be associated with a user story") (Ch 1.2.3, "Agile Methods") [V].

The chapter concludes that "'Agile' has associated values but no concrete meaning: it's a philosophy, and there's not just one way to follow it." Agile frameworks such as Scrum give more concrete guidance, with the Scrum Guide changing frequently (Ch 1.3, "Summary") [V] [AP].

## Part II: Project management and teamwork (Ch 2)

### Project management and the triple constraint

Project management is "the process of planning and executing a project while balancing the time, cost, and scope constraints" (Ch 2, opening; Glossary, "project management") [V]. These three constraints are *the triple constraint*: **Time** (duration, intermediate deadlines), **Cost** (monetary, personnel, and other project resources), and **Scope** (what the project is meant to accomplish and the requirements, "including quality") (Ch 2.2, "Triple Constraint") [V]. Letaw notes that "making strategic project decisions involves adjusting project constraints. If you want to reduce time and cost spent on a project or increase project scope, you'll need a corresponding change in one or more other constraints" (Ch 2.2; van Wyngaard et al., 2012) [V] [BT].

Three reasons are given for software engineers to learn about project management even when they are not project managers: (1) they might *become* a project manager; (2) they might *have* a project manager whose actions and communications will be easier to interpret with this background (RACI matrix is given as an example); (3) they might need to *self-manage* — within a flattened-hierarchy organisation or an Agile team (Ch 2.1, "Why Learn about Project Management?") [AP].

### Managerial skill mix (MSM)

Three categories of skill comprise the *managerial skill mix* (Badawy, 1995): **Interpersonal** ("Communicating effectively with anyone likely to affect the project (e.g., engineers on your team, managers, clients, contractors, IT support, etc.)"); **Technical** ("Using methods and equipment effectively (e.g., knowledge of appropriate processes, understanding and writing code, etc.)"); **Administrative and conceptual** ("Understanding the 'big picture' vision (conceptual) and being able to move macro-level pieces (e.g., teams, departments, divisions, etc.) toward that vision (administrative)") (Ch 2.3, "Managerial Skill Mix") [V] [BT]. The text observes that higher-level managers (e.g., CEOs) need a different mix than lower-level managers (e.g., project managers): a project manager "might need strong interpersonal and technical skills while only occasionally considering the big picture of how a project fits into [the] organization's overall vision" (Ch 2.3; Badawy, 1995) [V] [BT].

### Interpersonal skills: team communication

The chapter situates team communication methods against **Tuckman's model of team development** (Tuckman, 1965; Tuckman & Jensen, 1977), with five stages: **Forming** (members orient through testing each other's boundaries and existing team standards); **Storming** (members resist group influence, peers, peers' ideas, and tasks); **Norming** (team develops cohesiveness, devises new standards and roles, members express opinions); **Performing** (roles become flexible; team dynamics serve the team's function and task performance); **Adjourning** (team disbands) (Ch 2.4, "Interpersonal Skills: Team Communication") [AP] [BT].

Three concrete team-communication methods are presented:

*Establishing ground rules* — "a preemptive or reactive method for reducing team conflict and dysfunction." To be effective the rules "need buy-in from the whole team." Letaw offers eight diagnostic questions a team can use to draft rules — about vision, priorities, day-to-day communication, communication during conflict, work habits, responsiveness, what to do when team members fail expectations, and how to get to know each other (Ch 2.4.1, "Establishing Ground Rules") [V]. The text warns that "if your team gets the feeling the ground rules are silly, phony, too aspirational, too inflexible, or too authoritative, that could invalidate your team's efforts toward creating the ground rules" (Ch 2.4.1) [V].

*Defining roles and responsibilities: RACI matrix* — "a chart for defining who is responsible (R) and accountable (A) for a task or deliverable, and who should be consulted (C) or informed (I)" (Ch 2.4.2, "Defining Roles and Responsibilities: RACI Matrix") [V]. **Responsible (R)**: "Who will do the work." **Accountable (A)**: "Who will approve the work and make sure it gets done." **Consulted (C)**: "Who can discuss and offer advice about the work." **Informed (I)**: "Whom to keep up to date about the status of the work." A RACI matrix reduces risk because "If your team doesn't know who needs to do what (or forgets, or can plausibly deny knowing), that can increase the probability of a negative events and outcomes" — the example given is "shipping a broken product to customers because nobody was assigned to quality assurance" (Ch 2.4.2) [V].

*Measuring and building consensus: Fist of five* — "a method for checking and building consensus within a group of people." One person makes a statement or proposes an idea, and each person communicates agreement level by holding up a fist or up to five fingers (Ch 2.4.3, "Measuring and Building Consensus: Fist of Five Method") [V]. The encoding: **None** — Strong reject, blocks consensus; **One** — Reject, major issues need resolving now; **Two** — Weak reject, minor issues need resolving now; **Three** — Weak accept, minor issues can be resolved later; **Four** — Accept, no issues; **Five** — Strong accept, willing to lead or champion (Ch 2.4.3) [V]. The method "can reduce risk by (1) bringing problems to light and (2) increasing team motivation, ownership, and investment" (Ch 2.4.3) [V].

### Technical skills: project definition

In Agile, "a project's scope is implied through sets of tasks (e.g., release plan, Product Backlog, iteration plan, Sprint Backlog)"; in other environments, scope is captured in a specific document — a *statement of work* — "stating the project's objective, deliverables (outputs), milestones, technical requirements, and limitations/exclusions" (Ch 2.5.1, "Project Scope") [V].

*Project priority matrix* — a more concrete way to state the desired balance among the three constraints. Each constraint is tagged **Constrain** ("The constraint is fixed (can get better but must not get worse)"), **Enhance** ("Try to improve (e.g., take less time, spend less, have more features)"), or **Accept** ("Can worsen (e.g., more time, more personnel, fewer features) if necessary") (Ch 2.5.2, "Balancing Constraints: Project Priority Matrix") [V]. The worked example given is an NIH grant to write software for "a medical device that automatically regulates a person's pain level" — Scope is Constrained (must work, will be tested on humans), Cost is Constrained (fixed grant amount, taxpayer-funded), Time is Accepted (intermediate results may unlock further grants) (Ch 2.5.2) [AE].

*Eisenhower matrix* (Ch 2.5.3, "Task Prioritization: Eisenhower Matrix"): the urgent × important quadrant grid. **Do** (urgent, important): "Needs to be done correctly and now" (example: documenting undocumented code so a new hire can contribute); **Decide** (not urgent, important): "Needs to be done correctly but not immediately" (example: refactoring currently-working code); **Delegate** (urgent, not important): "Needs to be done now, but mistakes can be absorbed" (example: initialising a task-management system); **Delete** (not urgent, not important): "Doesn't need to be done correctly or any time soon. Can be eliminated" (example: a pong-themed loading screen only one person wants) (Ch 2.5.3) [V] [AE]. First-pass prioritisation with the Eisenhower matrix "can reduce risk by both conserving resources and using resources thoughtfully (including yourself)" and "can also help with getting out of the mode of 'putting out fires'" where "important but nonurgent tasks [get] eternally left at the end of the to-do list (perhaps resulting in project failure)" (Ch 2.5.3) [V].

*Finer-grained prioritization* (Ch 2.5.4, "Finer-Grained Prioritization") — when multiple tasks have the same urgency level. Five techniques: ask an expert (they may know which tasks have more unknowns, more risk, more dependencies); do a *spike* (three-step recipe: come up with a question; try to find the answer by reading and experimenting; repeat until enough information); think about dependencies (who is waiting on you, how many other tasks depend on this one); ask the customer or users directly or indirectly (phone call, focus group, survey, support tickets, marketing team); voting or pairwise comparison among the team (Ch 2.5.4) [V] [AP].

*Estimation: story points, ideal days, and planning poker* (Ch 2.5.5). The Agile community (Cohn, 2006) describes "two methods for stating the size of a task": **Story points** — "Assign a number to a task representing its size relative to other tasks" (a software install and a virus scan might both be 1; a major feature might be 8) — and **Ideal days** — "Assign a number of days you think it'd take to complete the task if there were no other tasks or distractions" (Ch 2.5.5) [V] [BT]. *Velocity* is "work completed (in story points or ideal days)" per period; teams make initial velocity estimates and adjust based on accuracy (Ch 2.5.5) [V] [BT].

*Planning poker* (Cohn, 2006; Mahnič & Hovelja, 2012) is the team-consensus estimation method: each team member privately selects a card representing their estimate, all reveal simultaneously, differences open a discussion, the process repeats until estimates "become sufficiently consistent" (Ch 2.5.5) [V] [BT].

*Project network diagram* — "a directed graph showing a project's tasks, the sequence in which they should be completed, and the dependency relationships between the tasks. The nodes in the digraph represent tasks, and the lines with arrows represent dependency or sequence relationships. A project network diagram moves left to right, where left is earlier in time" (Ch 2.5.6, "Scheduling: Project Network Diagram") [V]. The Activity-on-Node (AON) format is named (Larson & Gray, 2018) (Ch 2.5.6) [BT]. For a task to appear as a node, "it needs to (at a minimum) be distinct from other tasks, and its dependent tasks (a.k.a. predecessors) must be known" (Ch 2.5.6) [V].

*Task management systems* such as Asana, Jira, and Trello are "strongly oriented toward team collaboration" and often offer Agile-inspired features; common features include create/remove/update/delete tasks, enter task descriptions and attachments, view tasks as list/board/timeline (Gantt), organise tasks into projects, assign tasks to team members with due dates, enter task status, get email notifications, add tags and categories (Ch 2.5.7, "Task Management Systems") [V]. The text notes that task-management systems "don't have a universal way to generate project network diagrams" — that capability typically lives in a fuller project-management system like MS Project (Ch 2.5.7) [V].

The chapter closes by tying every method back to risk: project management "can reduce the risk of a project failing and make it possible to complete larger projects" (Ch 2.6, "Summary") [V].

## Part III: Requirements (Ch 3)

### Two main types

A software requirement is "a rule the software must conform to: what it must do, how well, and within what constraints or limits" (Ch 3, opening) [V]. Two types: **Functional requirements** are "A description of a behavior that a system will exhibit under specific conditions" (Wiegers & Beatty, 2013, p. 599) — example: "If the user activates the 'log in' button, the login page will appear" (Ch 3.1, "Types of Requirements") [V] [BT]. **Nonfunctional requirements** are "A description of a property or characteristic that a system must exhibit or a constraint that it must respect" (Wiegers & Beatty, 2013, p. 600) — example: "If the user activates the 'log in' button, the login page will appear within 500 milliseconds" (Ch 3.1) [V] [BT].

### Why requirements matter and what makes a good requirement

Reasons requirements matter (Ch 3.2, "Why Requirements Matter"): without them developers "might prioritize functionality they personally think is important or fun to implement, but what developers want to implement might not make the project successful"; with multiple developers on the same code, requirements help them "stay in sync and pursue the same goal" (otherwise "time, effort, and money can be wasted implementing conflicting code"); without specified requirements, stakeholders can "influence the project toward satisfying their own (possibly fleeting) wants or needs," producing drift away from the project's intent (Ch 3.2) [V].

A "good requirement" standard set is borrowed from the Texas Department of Information Resources (2008): requirements should be **Correct** ("What they say is right"), **Unambiguous** ("There is only one way to interpret them"), **Complete** ("They cover all that's important"), **Consistent** ("They aren't contradictory"), **Ranked for importance and/or stability**, **Verifiable or testable** ("There's a way to figure out if they're satisfied"), **Modifiable** ("They can be changed"), **Traceable** ("It's possible to figure out where they came from"); they should also be cross-referenced to earlier documents, uniquely identifiable, and organised for maximum readability (Ch 3.3, "What Makes a Good Requirement") [V] [BT].

### Requirements elicitation

*Requirements elicitation* is "the process of gathering requirements" (Ch 3.4, "Requirements Elicitation"; Glossary, "requirements elicitation") [V]. Methods to detect stakeholders' wants and needs include **interviews** (structured, semi-structured, unstructured), **focus groups** ("small, group conversations in which the participants discuss topics among themselves, with moderator guidance"), **lab studies** ("Participants perform tasks in a controlled setting"), and **exploratory research** ("Multiple methods of immersing oneself within the world of relevant people and products, with the purpose of gaining knowledge and developing empathy for stakeholders"). The fly-on-the-wall example: noticing people can't find Aisle 25 because of unexpected placement leads to prioritising the Aisle Map feature (Ch 3.4) [V] [AE]. Hanington and Martin (2019) is cited for fuller treatment (Ch 3.4) [BT].

Letaw catalogues five factors that complicate developer-led requirements gathering: stakeholders "might not have experience or expertise," "might not have good ideas," "might not know what they want," "might want what's bad for them or others," and "are humans" who "communicate imperfectly" (Ch 3.4, "Requirements Elicitation") [V].

### Nonfunctional requirements: quality attributes and constraints

Quality attributes are "words for describing 'a service or performance characteristic of software'" (Wiegers & Beatty, 2013, p. 601) (Ch 3.5.1, "Quality Attributes") [V] [BT]. The catalogue offered (each with a one-line definition): **Maintainability** ("Amount of effort needed for developers to update, refactor, or otherwise modify the software's code"); **Portability** ("Amount of effort needed to run the software on different platforms"); **Reliability** ("How often the software's functions succeed or fail"); **Efficiency** ("Number of resources the software requires"); **Integrity** ("How frequently the software loses data"); **Memorability** ("Amount of time users must spend relearning functionality"); **Flexibility** ("Number of different ways the software can be used"); **Interoperability** ("Ease with which the software can integrate with other software"); **Reusability** ("Extent to which the code can easily be used to solve other problems") (Ch 3.5.1) [V]. Each attribute "can be converted to a scale," and nonfunctional requirements are specified by setting a "performance threshold" against the scale (Ch 3.5.1) [V].

*Constraints* are nonfunctional requirements that aren't about quality attributes; example types (Wiegers & Beatty, 2013) include those limiting technology choices, target platforms, what about the software can change (backward compatibility), how code can be written (coding/documentation standards), and how data can be handled (e.g., "must only be stored on US servers") (Ch 3.5.2, "Constraints") [V] [BT]. Letaw distinguishes constraints from quality attributes by their origin: "constraints are often externally mandated, while quality attributes can be chosen internally by the team" (Ch 3.5.2) [V] [AR].

### Functional requirements: three formats and user stories

Three example formats for functional requirements appear in the chapter (Ch 3.6, "Functional Requirements") [AP]: a plain action-effect statement ("When the 'register' button is activated, the user's information is added to the database and a 'thank you for registering' screen displays"); the *user story* format ("As a wholesaler, I want to see the wholesale and retail prices when I go to 'product view' so that I know how much money I'm going to make"); the *given-when-then* format ("Given a user has performed at least one editing action, when they activate the 'action history' window, they see a list of editing actions they have taken"). The given-when-then format is "commonly used to write user story acceptance criteria: a set of statements that, when true, indicate that the user story has been completed" (Ch 3.6) [V].

*User stories* are "a method for specifying functional requirements. They describe a small piece of the software's functionality in a simple and easy-to-read sentence. They are written in plain English so that nontechnical people (e.g., users, clients, other stakeholders) can understand them" (Ch 3.6.1, "User Stories") [V]. The **INVEST** acronym (Wake, 2003) characterises a good user story (Ch 3.6.1) [V] [BT]:

- **I**ndependent: "Does not have unnecessary dependencies or overlap with other user stories."
- **N**egotiable: "Encourages instead of discourages discussion and gives developers flexibility."
- **V**aluable: "Fulfills a user need."
- **E**stimable: "Can be given a time estimate."
- **S**mall: "Can fit into a single development period (e.g., a two-week Sprint)."
- **T**estable: "Possible to determine it's done."

Each INVEST letter is given with a worked example contrasting a not-quite-good user story with a better one (Ch 3.6.1) [AE]. Acceptance criteria establish the *Definition of Done* (DoD) — "what must be true about the functionality specified by the user story for the user story to be considered done" (Ch 3.6.1) [V].

### Use cases

A use case is "a more formal method of specifying functional requirements . . . structured descriptions of what a system is required to do when a user interacts" (Ch 3.6.2, "Use Cases") [V]. Every use case has a **Name** ("A short title for the use case that often starts with a verb"); **Actor(s)** ("The user or users (human/nonhuman/computer) that are interacting with the software"); and **Flow of events** ("Sequence of actions describing the interaction between the actor and the software (a.k.a. 'basic course of action' or 'success scenario')") (Ch 3.6.2, "Required Parts of a Use Case") [V]. Optional parts include identifier (e.g., UC-002), preconditions, postconditions, business relevance, dependencies, extensions, priorities, and nonfunctional requirements (Ch 3.6.2, "Additional Parts of a Use Case") [V]. "As use cases are less common in Agile, the remainder of this section will provide only a summary of how use cases are structured" (Ch 3.6.2) [V].

### Requirements specification

*Requirements specification* (noun) is the document containing the requirements; the document may also be called a *software requirements specification* (SRS) (Ch 3.7, "Requirements Specification") [V]. Letaw declines to teach the SRS abstractly: "The best way to learn about SRSs is to look at some" and provides five freely-available examples (manufacturing data distribution, conservation-practice assessment, a PDF splitter/merger, EEG processing software, library software) (Ch 3.7) [V].

## Part IV: UML class and sequence diagrams (Ch 4)

### Why diagrams (and why UML)

Diagrams help in at least two ways: they can "help you plan software you will create" — once created they can communicate to the team what should be implemented and let the team "evaluate whether your plans are any good (e.g., are clear, are logical, reflect your project's desired quality attributes)"; and they can "help you describe software you've already created" — for documentation and evaluation, with audiences including other developers, supervisors, candidate developers, integrators, "curious end users, and students of software engineering" (Ch 4.1, "How Diagrams Help") [V]. Diagrams "must communicate clearly and at an appropriate level of detail for your intended audience. If your intended audience does not understand your diagram — or misunderstands it — your diagram has failed" (Ch 4.2, "What Diagrams Must Do Well") [V].

*Unified Modeling Language* is "a family of graphical notations for describing and designing software through diagrams" — especially applicable to object-oriented software. UML "was first published in 1994, became a standard of the Object Management Group (OMG) in 1997, and became an ISO standard in 2005. UML is currently on version 2" (Ch 4.3, "What Is UML?") [V] [BT].

Five benefits of UML (Ch 4.4, "Why Use UML?") [V]:
1. UML provides "notation for designing software so that your implementation will be structured" and "notation for describing the existing design of software so that you can evaluate whether the design is any good."
2. UML diagramming "forces you to think about software design in a structured way" — countering the tendency, when designing in one's mind, to be "sloppy about it — thinking about the aspects of the design they want to think about."
3. UML provides views at different design levels (class, component, package).
4. UML provides "a common language between software professionals."
5. UML diagrams give a way to communicate "without asking them to look through code" — useful for onboarding new developers and for managers.

Three drawbacks (Ch 4.5, "Why NOT Use UML?") [V]: "People tend to vary their UML notation, which can cause confusion" (tips: keep notation basic, explain complex notation); "Getting UML notation right can take a lot of time" — if a diagram takes longer to make than a code explanation would take, "the diagram isn't helping"; UML diagrams "can require a lot of maintenance" if software design changes frequently (though "some IDEs can generate some UML diagrams from your code").

### Class diagrams

A class diagram "describes a system's classes and the static relationships that exist among them. Class diagrams also show properties and operations of a class. Properties represent the structure of a class (e.g., instance variables) and operations represent the functionality provided by the class (e.g., methods; Fowler, 2004)" (Ch 4.6, "Class Diagrams") [V] [BT].

Notational conventions enumerated (Ch 4.6.1, "UML Class Diagram Notation") [V]:
- **Notes** — "for placing comments on class diagrams."
- **Class** — attribute and operation listing; **+** indicates public, **−** private, **#** protected; attribute types, method parameters and return types, default values may be shown.
- **Association** — "a class contains a reference to an object(s) of the other class in the form of a property."
- **Unidirectional association** — arrow indicating "Class1 has a Class2."
- **Property names** and **multiplicities** (source and target) annotate associations to specify how many instances of each side relate.
- **Bidirectional association** — both sides hold the reference, with multiplicities on both ends.
- **Inheritance** — "Class2 is a subclass of Class1; Class2 is a Class1."

### Sequence diagrams

A sequence diagram "describes interactions between objects. Usually, the diagram shows a single use case or scenario. Sequence diagrams are a type of interaction diagram and are not as good for showing object implementation details" (Ch 4.7, "Sequence Diagrams") [V]. Participants (the "columns") "are often objects" but "this is not always the case. For example, a participant can be a user." Users "are sometimes represented as stick figures (without the box)"; "another possible non-object participant could be a database" (Ch 4.7) [V].

Notational conventions for sequence diagrams (Ch 4.7.1, "UML Sequence Diagram Notation") [V]:
- **Participant** — column whose name appears in the box at the top.
- **Lifeline** — "Vertical dashed line represents the life span of the participant. Top is beginning of life, and bottom is the end. Life ends when the participant is deleted."
- **Message** — "Interaction from one participant to another is shown by the solid line with arrow. Often a method call."
- **Activation bar** — "Box on lifeline indicates when the participant is active. Indicates method is on call stack."
- **Return** — "Dashed line with arrow indicates method return. Use only when it helps communicate something important about the interaction."
- **Self-call** — "Method calling self. Solid line with arrow points back to participant's own lifeline."
- **Deletion** — "End of participant's life. Indicated by an X on the lifeline."

The chapter's signature framing: "UML diagrams are for communicating with humans — not computers" (Ch 4.8, "Summary") [V].

## Part V: Monolith versus microservice architectures (Ch 5)

### Definitions

*High-level architecture* is "the software's all-encompassing code design" — "an abstraction that usually represents the entire codebase" (Ch 5, opening) [V]. The chapter concentrates on two architectures (monolith, microservices) without claiming to cover every option (Ch 5, opening) [V].

*Monolith software* is "one interconnected codebase that cannot easily be divided into multiple independent components that run separately and are individually useful" (Ch 5.1, "Monolith Architecture") [V]. Letaw notes that monoliths are "so common that [they] can arise without having to plan" — first programs are typically small monoliths, and adding code/files/classes/components without architectural change produces bigger monoliths (Ch 5.1) [V] [AP].

*Microservices* are "separate applications, each of which runs in a separate process and could be individually useful" (Ch 5.2, "Microservice Architecture") [V]. The chapter borrows the section subheadings from Lewis & Fowler (2014) and points to Fowler (2019)'s Microservices Guide for more (Ch 5.2) [BT].

### Five microservice characteristics (Lewis & Fowler subheadings)

*Smart end points and dumb pipes*: "The communication pipe within a microservice architecture is simple, and the services themselves take care of translating and otherwise processing messages." Microservices "commonly communicate through a REST API, which allows these kinds of messages: GET, POST (create), PUT (update), or DELETE" (Ch 5.2.1) [V] [BT].

*Componentization via services*: "In a microservice architecture, components are services. The Lewis and Fowler (2014) definition of a component is 'a unit of software that is independently replaceable and upgradeable.' A service provides functionality while running in its own process. A monolith typically has code with tight coupling and components that run in the same process" (Ch 5.2.2) [V] [BT]. The advantages: **independence** ("Each individual service can be updated, tested, launched, and stopped without requiring the same from other components") and **standardized component communication** ("Service communication pipes can be simple and the same each time . . . less thinking, fewer mistakes, and less violation of encapsulation"). The disadvantages: **more expensive communication** (network calls slower and heavier than direct calls) and **potentially less secure communication** (network traffic "more prone to interception and alteration") (Ch 5.2.2) [V].

*Organized around business capabilities*: client-server is "organized around technology"; microservices are "organized around business capabilities," where a business capability is "the potential of a business resource (or groups of resources) to produce customer value by acting on their environment via a process using other tangible and intangible resources" (Michell, 2011) (Ch 5.2.3) [V] [BT]. Examples Letaw offers: a manufacturer slicing wheat dough into 0.5-cm noodle strips in 1.2 seconds; a loan officer leading a customer through securing a loan; a pet food distributor regularly shipping nutritionally balanced cat food; software making a video file mobile-compatible (Ch 5.2.3) [V] [AE]. "One implication of being focused on business capabilities is that each microservice can have its own tech stack (including its own database)" (Ch 5.2.3) [V].

*Decentralized data management*: "In a microservice architecture, each service typically has its own database instead of sharing a centralized database. This is part of decoupling the software's components, which has many benefits including failure containment. A disadvantage is that if two microservices need to share data, the two copies of that data can become inconsistent." Microservice databases "are said to have *eventual consistency*, which means that, with time, each microservice will have the most up-to-date information, but meanwhile, there could be a mismatch (perhaps one that will annoy or mislead human users)" (Ch 5.2.4) [V].

*Decentralized governance*: "Microservices need only be compatible at their interfaces (communication pipe), leaving flexibility in how each is implemented. For example, each service can be written in a different language, reducing the weight of tech stack decisions . . ." Conversely, a monolith team "might only need to maintain a small set of technologies" (Ch 5.2.5) [V].

*Design for failure*: with services on different processes/machines built by different teams using different technologies, "thinking can shift toward service-specific monitoring, logging, and design decisions about what to do when a service fails — including what to tell the user." With a monolith, "more thought might be put into how to revert quickly if a deployment fails (because failure might mean no part of the monolith works)." Monoliths can be designed for failure, but "that's not as natural a tendency as with microservices" (Ch 5.2.6) [V].

### Six comparison questions

Section 5.3 organises monolith-vs-microservice differences into six structured comparisons (Fowler, 2015; Lewis & Fowler, 2014) (Ch 5.3) [V] [BT]:

1. **Communication** — Monolith: direct calls and over a network; varied means. Microservices: typically over a network via standardised pipes (e.g., HTTP); end points must be "smarter" because pipes are "dumb" (Ch 5.3.1) [V].
2. **Deployment** — Monolith: often deployed "all at once." Microservices: independently deployable; can be stopped without stopping connected services (Ch 5.3.2) [V].
3. **Scaling** — Monolith: copied onto multiple machines, each of which "must have enough space, memory, processing speed, and the like to support the entire monolith." Microservices: more options, including replicating only the more-used services (Ch 5.3.3) [V].
4. **Testing** — Microservices: each service independently testable. Monolith: testing influenced by dependencies that "could reach broadly across the software (and make for slow tests)" (Ch 5.3.4) [V].
5. **Upgrading** — Microservices: each service can be written in a different language, run in different contexts, and theoretically be upgraded independently. Monolith: upgrading "may require more care" because each component must be compatible with the new context (Ch 5.3.5) [V].
6. **Database** — Monolith: "might have just one database, potentially a very large one" — bottleneck risk, slow backups/restores, but a single place for account management and maintenance. Microservices: "each microservice typically has its own data storage" (Ch 5.3.6) [V].

### Case study: ODOT TOCS migration

Section 5.5 narrates a real migration: OSU's Center for Applied Systems and Software (CASS) helped the Oregon Department of Transportation convert TOCS (Transportation Operation Center System), a "statewide computer-aided dispatch software," from monolith to microservices, starting with the home screen (Ch 5.5, "Case Study: Microservice Architecture") [V] [AE]. The user-side problem: "dispatcher centers in different parts of Oregon had different needs . . . but had to use the same home screen, which could not be easily configured" (Ch 5.5) [V]. The developer-side drivers were technical-debt accumulation, deploy frequency limits ("CASS could only deploy TOCS a few times a year because the software had to be tested and deployed in its entirety"), database contention pressure, and platform deprecation ("their technology stack was becoming deprecated because Microsoft stopped releasing updates to the .NET Framework after version 4.8") (Ch 5.5) [V] [AE]. The new architecture integrates with the remaining monolith via a *WinGui Gateway* that is "responsible for preparing data from the services so it can be used by the New Home Screen UI" using the .NET 6 stack, and a *Message Broker* (Apache ActiveMQ) using the AMQP standard. Each service has its own database, with JSON used for the Profile Service rather than the monolith's relational store (Ch 5.5) [V] [AE]. Fern (2022) is cited as the source video (Ch 5.5) [BT].

## Part VI: Paper prototyping (Ch 6)

### Fidelity levels

UI prototypes come in "fidelities" — low, medium, and high (Ch 6, opening; Snyder, 2011) [V] [BT]. *Low fidelity*: "A rough sketch that is often drawn by hand, drawn using an app and stylus, or made using software specifically for creating low-fidelity prototypes. At this fidelity, you can gather feedback on higher-level features and have the flexibility to make large, low-cost changes" (Ch 6, opening) [V]. *Medium fidelity*: "A detailed illustration often created using a professional drawing or presentation tool (e.g., Visio, PowerPoint, and the like), or perhaps a careful and detailed hand drawing. At this fidelity, to keep costs low, you can gather feedback on small changes to defined and accepted features that you plan to keep but might change the look of" (Ch 6, opening) [V]. *High fidelity*: "A polished, detailed illustration that looks like a finished UI" — typically built in Photoshop, Illustrator, or a GUI builder; appropriate for gathering "feedback about detailed tweaks to specific features to make focused and incremental improvements" (Ch 6, opening) [V].

A paper prototype is "a hand-drawn sketch of a UI design that's based on the software's requirements. It doesn't need to be pretty or artistic. It can be simple and reduce the UI to only the most important elements (i.e., it is often low fidelity)" (Ch 6, opening) [V].

### Showing interaction and harvesting feedback

A paper prototype "needn't be static or limited to one sheet of paper." Letaw lists craft methods: cut out small paper shapes that can be moved (e.g., a submenu rectangle), place arrows and annotations, add strings to show UI element movement; "I've even seen people use brass brads for spinnable elements" (Ch 6.1, "Showing Interaction") [V] [AP]. The warning is pragmatic: "if your client doesn't like your design, you might have saved time and communicated your concept just as well with a less elaborate paper prototype" (Ch 6.1) [V].

The feedback method (Ch 6.2, "Showing Your Concept to Others"): "give your user the entry screen drawing, then either give them a task . . . or let them explore on their own. Watch as they tap buttons or otherwise interact. Be ready to quickly swap in other drawings to respond to their interactions" — a manual-stand-in for app navigation [V]. The *think-aloud protocol* asks the user to verbalise "what they're doing, what they're trying to do, what questions they have at that moment, what they don't like, and so on" (Ch 6.2; Glossary, "think-aloud protocol") [V].

The chapter closes with the rationale: "Paper prototyping can help reduce project costs by giving a way to detect user interface design flaws before they are implemented" (Ch 6.3, "Summary") [V].

## Part VII: Inclusivity Heuristics (Ch 7)

### Background and provenance

The Inclusivity Heuristics are "guidelines for designing technology to work well for a diversity of users." Using them is "a way to practice *inclusive design*: it is 'a methodology . . . that enables and draws on the full range of human diversity. Most importantly, this means including and learning from people with a range of perspectives' (Microsoft)" (Ch 7, opening) [V] [BT]. The heuristics were also called "Cognitive Style Heuristics" and "GenderMag Heuristics" (Burnett et al., 2021) and were developed by human-computer interaction researchers at Oregon State University as part of the GenderMag Project — backed by "more than 40 publications about gender differences in how people use technology" (Ch 7.1, "Background") [V] [BT]. Future expansions toward socioeconomic diversity (Hu et al., 2021) and age diversity (McIntosh et al., 2021) are anticipated (Ch 7.1) [V] [BT].

### Five cognitive facets

In their current form the heuristics "give advice for how to support five cognitive facets involved in how people interact with technology for the first time" (Burnett et al., 2016) (Ch 7, opening) [V] [BT]:

1. **Attitude toward risk** (risk-averse to risk-tolerant).
2. **Computer self-efficacy** (low to high).
3. **Information processing style** (comprehensive to selective).
4. **Learning style** (process-oriented to mindful tinkering to tinkering).
5. **Motivations** (task-motivated to motivated by tech interest).

A *cognitive style* is "a cognitive facet value" (Ch 7, opening) [V]. The text introduces three personas — **Abi**, **Pat**, and **Tim** — each carrying a distinctive combination of cognitive styles; "the personas can have any gender and picture" (Ch 7.2, "Inclusivity Heuristics Personas") [V].

Heuristics are "meant to be used within a usability inspection method called *heuristic evaluation*" (Nielsen & Molich, 1990): "multiple evaluators independently check whether a technology design follows the heuristics. They make note of any issues and compare results. The output is a combined set of usability issues" (Ch 7.1) [V] [BT].

### The eight heuristics

Each heuristic is paired with a worked design example and a description of Abi's, Pat's, and Tim's reactions (Ch 7.3.1–7.3.8) [V]:

1. **Explain (to Users) the Benefits of Using New and Existing Features.** Abi and Pat are pragmatic about technology, with limited spare time; they prefer familiar features unless benefits are clear. Abi is risk-averse and avoids features with "unknown time costs and other risks"; Pat is also cautious but open to trying features for task relevance; Tim is enthusiastic about discovery and willing to risk using features without prior knowledge of their costs (Ch 7.3.1) [V].
2. **Explain (to Users) the Costs of Using New and Existing Features.** Abi and Pat prefer to "reduce risk by avoiding features that might require significant time and effort"; Tim is "more open to taking risks and may be willing to invest additional time and effort into using features, even if they aren't directly related to the current task" (Ch 7.3.2) [V].
3. **Let Users Gather as Much Information as They Want, and No More Than They Want.** Abi and Pat "approach decision-making by diligently gathering and thoroughly reviewing relevant information before acting"; Tim "prefers to dive right into the first option that catches their interest and pursue it. They will backtrack if necessary" (Ch 7.3.3) [V].
4. **Keep Familiar Features Available.** Abi (lower computer self-efficacy, more risk-averse) "tends toward self-blame and will stop using unfamiliar features if problems arise"; Pat (moderate self-efficacy, risk-averse) "will attempt alternative methods to succeed for a while" before falling back on familiar features; Tim (higher self-efficacy, more risk-tolerant) "tends to blame the technology itself and may invest considerable extra time exploring various workarounds" (Ch 7.3.4) [V].
5. **Make Undo/Redo and Backtracking Available.** Abi and Pat "tend to avoid taking actions in technology that may be difficult to undo or reverse"; Tim is "willing to take actions in technology that might be incorrect or require reversal" (Ch 7.3.5) [V].
6. **Provide an Explicit Path through the Task.** Abi, "as a process-oriented learner, prefers to approach tasks in a systematic and step-by-step way"; Tim and Pat (more inclined toward tinkering) "prefer not to be confined by strict and predetermined processes" and thrive when free to explore and experiment (Ch 7.3.6) [V].
7. **Provide Ways to Try Out Different Approaches.** Abi (lower self-efficacy) tends toward self-blame and may stop using the tech altogether; Pat (moderate self-efficacy) "will attempt alternative methods to succeed for a period"; Tim (higher self-efficacy) "tends to blame the technology itself" and explores "numerous workarounds in order to overcome the issue" (Ch 7.3.7) [V].
8. **Encourage Tinkerers to Tinker Mindfully.** Tim's "learning style revolves around tinkering, but at times Tim becomes excessively engrossed in tinkering, leading to long distractions"; Pat by contrast "embraces a learning approach that involves actively experimenting with new features. Pat does so mindfully, however, taking the time to reflect on each step taken during the learning process" (Ch 7.3.8) [V].

The chapter summary lists all eight heuristics together (Ch 7.4, "Summary") [V].

## Part VIII: Code smells and refactoring (Ch 8)

### What code smells are and why they matter

Code smells are "indications that the code needs to be reorganized — a sign your software is undergoing *code decay*" (Ch 8, opening; Glossary, "code decay") [V]. Letaw lists six diagnostic self-thoughts (Ch 8, opening) [V]:
- "I would *never show this code* during an interview."
- "I'm going to *start over* and rewrite this code from scratch."
- "Every time I look at this code, I have to *re-figure-out* what it does."
- "These *comments don't match the code* . . ."
- "Why is this *code repeated* in three different places?"
- "I want to switch out this component, but *that'll break X, Y, and Z* in this other place, and I don't want to deal with that."

Three reasons to address code smells (Ch 8.1, "Why Care about Code Smells?") [V]: (1) smelly code is "harder for you and others to maintain because the code is unclear" — and when code is hard to maintain, developers "work around it or re-create the same functionality elsewhere"; (2) "Smelly code leads to smellier code" — letting code become disorganised signals to yourself and others that disorganised code is acceptable; the CSS `!important` workaround is offered as an example of the laziness pattern; (3) smelly code "builds up technical debt" — as sloppy software grows, "it will get more difficult to deal with," may force more hires, productivity declines, and ultimately the software "may have to be redeveloped entirely (which doesn't always solve the problem). Or the project could fail" (Ch 8.1; Martin, 2009) [V] [BT].

*Refactoring* is "when you improve your code without changing what the code does. Refactoring is a way to pay down technical debt" (Ch 8.2, "Your Code Stinks—Now What?"; Glossary, "refactoring") [V].

### Code smells about comments

Four smells with prescriptions (Ch 8.3, "Comments"; Ch 8.3.1; Ch 8.3.2) [V]:

- **Obsolete Comment** ("no longer describes the code") — Remove or update.
- **Commented-Out Code** ("somebody thought they'd need that code later, but the commented-out block is now getting out of date and in the way") — Remove. "If you're feeling risk-averse, save a backup or use a version-control system."
- **Redundant Comment** ("states what would already be immediately apparent to a programmer of any level") — Remove. "Less is more."
- **Long Comment** ("multiple sentences, complicated, goes into a lot of detail") — Simplify the code to be more self-explanatory; shorten or remove the comment.

The framing claim: "too many comments can be as bad as none" (Ch 8.3, "Comments") [V]. Three drawbacks of having many comments: they "get out of date quickly" and produce a mix of accurate and inaccurate comments (eroding trust in all of them); writing comments for straightforward code "can distract from the important comments"; lots of comments may "indicate the code needs to be simplified" (Ch 8.3.1) [V].

### Code smells about functions

Three smells (Ch 8.4.1, "Code Smells about Functions") [V]:

- **Long Function** ("more than 10 lines or so") — Break into multiple functions. "Aim for five lines or fewer."
- **Function with Many Jobs** ("doing more than what its name suggests, doing things that aren't closely related, doing many things") — Break into multiple functions.
- **Function with Many Parameters** ("more than four, some say more than three") — "As appropriate, pass an object that combines the parameters, make calls within the function to get the parameter data, break into multiple functions, or find another way of reducing the number of parameters."

### Code smells about code in general

Four smells (Ch 8.5.1, "Code Smells about Code in General") [V]:

- **Duplicate Code** ("same code in multiple places") — "Consolidate into one place, but watch out for creating unwanted dependencies."
- **Long Lines** ("more than 100 characters or so") — "Shorten by breaking into multiple lines, converting to a function call, defining new variables, and so on."
- **Inconsistent Conventions** ("formatting code differently in different places, or untidily") — "Follow whatever style conventions the code is already using. If it's a new project, plan to be self-consistent or follow accepted conventions for the language you're using."
- **Vague Naming** ("does not communicate what the function, variable, etc. is for") — "Rename it, even if the name is long. Long names can sometimes replace comments."

The chapter's overarching claim: "Cleaning up your code can help make your software sustainable and extensible and can make your teammates happier, too" (Ch 8.6, "Summary") [V].

## Key statistics (with provenance)

| Metric | Value | Classification |
|---|---|---|
| Organisations "leaning toward Agile" as primary software process model | 51% (n=601) | [V] (Ch 1.2, citing Hewlett Packard Enterprise, 2017) |
| Organisations using "hybrid" software process model | 24% | [V] (Ch 1.2) |
| Organisations using "pure Agile" | 16% | [V] (Ch 1.2) |
| Organisations "leaning toward Waterfall" | 7% | [V] (Ch 1.2) |
| Organisations using "pure Waterfall" | 2% | [V] (Ch 1.2) |
| Agile adopters citing enhanced collaboration | 54% (n=403) | [V] (Ch 1.2) |
| Agile adopters citing increased software quality | 52% | [V] (Ch 1.2) |
| Agile adopters citing increased customer satisfaction | 49% | [V] (Ch 1.2) |
| Agile adopters citing shorter time to market | 43% | [V] (Ch 1.2) |
| Agile adopters citing reduced cost of development | 42% | [V] (Ch 1.2) |
| Software-project failure rate FY2011-2015 | 17%–22% of 25,000+ projects | [V] (Ch 1.1, citing Standish CHAOS Report 2015) |
| Daily Scrum length | 15 minutes | [V] (Ch 1.2.2) |
| Sprint length cap | "one month or less" | [V] (Ch 1.2.2) |
| Function-parameter threshold for "many parameters" smell | More than 4 (some say more than 3) | [V] (Ch 8.4.1) |
| Long-function threshold | Roughly more than 10 lines; aim for ≤ 5 | [V] (Ch 8.4.1) |
| Long-line threshold | Roughly more than 100 characters | [V] (Ch 8.5.1) |
| Inclusivity Heuristics research base | 40+ publications | [V] (Ch 7.1) |

## Connections the author makes in the text

- *Agile Manifesto* (Beck et al., 2001) — approving, grounding the Agile philosophy of Chapter 1 [BT] (Ch 1.2.1).
- *Royce (1970)*, "Managing the development of large software systems" — critical/ironic; Letaw notes Waterfall is often associated with an article describing its flaws [BT] (Ch 1.1).
- *Schwaber & Sutherland (2020), Scrum Guide* — approving, primary source for the Scrum framework definitions [BT] (Ch 1.2.2).
- *Cohn (2006), Agile Estimating and Planning* — approving, source for story points / ideal days / planning poker [BT] (Ch 2.5.5).
- *Mahnič & Hovelja (2012)* on planning poker for user-story estimation — approving [BT] (Ch 2.5.5).
- *Tuckman (1965)* and *Tuckman & Jensen (1977)* — approving, source for the five-stage team-development model [BT] (Ch 2.4).
- *Badawy (1995), Developing Managerial Skills* — approving, source for the three-category Managerial Skill Mix [BT] (Ch 2.3).
- *Larson & Gray (2018), Project Management* — neutral attribution for the Activity-on-Node project network diagram format [BT] (Ch 2.5.6).
- *van Wyngaard, Pretorius, & Pretorius (2012)* — neutral, on the triple-constraint trade-off [BT] (Ch 2.2).
- *Wiegers & Beatty (2013), Software Requirements* (3rd ed.) — approving, primary source for the functional/nonfunctional and quality-attribute definitions [BT] (Ch 3.1, 3.5).
- *Wake (2003), "Invest in good stories"* — approving, source of the INVEST acronym for good user stories [BT] (Ch 3.6.1).
- *Texas Department of Information Resources (2008)* — approving, source for the eight-attribute good-requirement standard [BT] (Ch 3.3).
- *Hanington & Martin (2019), Universal Methods of Design* — approving, pointer to fuller treatment of elicitation methods [BT] (Ch 3.4).
- *Fowler (2004), UML Distilled* — approving, source for class-diagram property/operation definitions and a pointer for sequence diagrams [BT] (Ch 4.6, 4.7).
- *Lewis & Fowler (2014), Microservices*, and *Fowler (2015), Microservice trade-offs* — approving, organising frame for Chapter 5 (subheadings borrowed from Lewis & Fowler) [BT] (Ch 5.2, 5.3).
- *Michell (2011)*, "A focused approach to business capability" — approving, source of the business-capability definition used in microservices framing [BT] (Ch 5.2.3).
- *Snyder (2011), Paper Prototyping* — neutral attribution for fidelity-level disagreement and the practice generally [BT] (Ch 6).
- *Burnett et al. (2016, 2021)*, GenderMag project publications — approving, source of the Inclusivity Heuristics and the five cognitive facets [BT] (Ch 7).
- *Microsoft Inclusive Design* — approving, source of the inclusive-design definition [BT] (Ch 7).
- *Nielsen (1994); Nielsen & Molich (1990)* — approving, source of heuristic evaluation as a usability inspection method [BT] (Ch 7.1).
- *Hu et al. (2021)* and *McIntosh et al. (2021)* — neutral attribution, foreshadowing socioeconomic and age extensions to the heuristics [BT] (Ch 7.1).
- *Martin (2009), Clean Code* — approving, source for the technical-debt narrative in Chapter 8 [BT] (Ch 8.1).
- *Fowler & Beck (2019), Refactoring* — approving, reference for further refactoring guidance [BT] (Ch 8, references).
- *Shvets (n.d.), refactoring.guru* — approving, reference for further refactoring patterns [BT] (Ch 8, references).
- *ISO/IEC/IEEE 24765:2017* — approving, source of the software-engineering definition used throughout [BT] (Introduction; Glossary).

## Positions the author explicitly frames against

- **"Software engineering as black-and-white algorithmic correctness."** Letaw insists software engineering is "a gray area of computer science"; the question shape is "How does my team know this software is ready to release?" not "Is this algorithm correct?" (Introduction, "Software Engineering Is Not Black and White").
- **Teaching every detail.** "It's Not Necessary to Study Every Detail of Software Engineering" — the book deliberately curates "a set of software engineering methods that are known to be useful across multiple contexts" rather than aiming for completeness (Introduction).
- **Waterfall as default.** The chapter on Agile is framed against Waterfall by noting that "Ironically, people often associate Waterfall with an article that describes Waterfall's major flaws" (Ch 1.1, "The Software Development Life Cycle").
- **Many comments as virtuous.** "Too many comments can be as bad as none." Letaw frames against the over-commenting impulse with three concrete drawbacks (out-of-date risk, distraction from the important comments, comments as a signal that code should be simplified) (Ch 8.3).
- **Rigid UML correctness over communication.** "What's most important when creating diagrams is not following the rules or conventions but communicating with your audience." Sticking to formal UML correctness when a clearer human-readable approach exists is framed as missing the point (Ch 4.7; Ch 4.4 drawback 2; Ch 4.8 summary).
- **Treating risk as background instead of foreground.** Each method in the project-management chapter is justified as a risk-mitigation tool; the implicit position framed against is project work that does not name and track risk (Ch 2).
- **One-size-fits-all UI design.** The Inclusivity Heuristics frame against UI design tuned to a single cognitive style (typically the designer's), in favour of design that supports the spread across each of the five cognitive facets (Ch 7).
- **Ground rules as performative compliance.** Letaw warns specifically that rules feeling "silly, phony, too aspirational, too inflexible, or too authoritative" can invalidate the exercise — framing against checkbox-style ground-rule artefacts (Ch 2.4.1).

## Citation and source-integrity notes

The source was provided as a 5,159-line markdown file converted from PDF via pymupdf4llm 0.2.9. Conversion preserved chapter and section headings (Ch N, "Section name"), figure captions, code blocks, glossary entries, and reference lists; it did not preserve PDF page anchors as cite-able markers (the only page markers are footer-style "Chapter Name | N" lines that recur per page). The citation style is therefore `(Ch N, "Section name")`. Direct quotations are taken from the converted markdown and verified against the supplied source text.

The ISBN is not stated in the front matter of the source as supplied; the deep reference records "ISBN not stated in source front-matter" rather than guessing. The author's contact (setextbook@lara.tech), licence (CC BY-NC 4.0), publisher (Oregon State University, via the OSU Open Educational Resources Unit), publication year (2024), edition (2nd), and URL (https://open.oregonstate.education/setextbook/) are all sourced from the front matter.

Coverage is full: Introduction, Chapters 1 through 8, the Conclusion, the Glossary, and the consolidated References list were all read end-to-end as part of Pass C. The figures referenced throughout (Figure 1.1, 1.2, 2.1, 3.1–3.5, 4.1–4.18, 5.1, 6.1–6.3, 7.1–7.9) are described in the converted markdown by their captions and surrounding prose; the image axis has not been classified in this run (text-only scope; `ingesting-images` is the follow-up if visual classification is needed).
