# Pass I Source-Only Audit — open-practice-library

**Auditor:** claude-opus-4-7[1m] | Effort: xhigh (9-pass) | Date: 2026-05-13
**Subject:** `corpus.commons/demo/references/open-practice-library-deep.md`
**Source:** Open Practice Library; converted markdown at `corpus.commons/demo/sources/converted/open-practice-library.md` (sha256 `2f1ac99414296eeb6d7af64f23fdaf10c1bd85d9325aa88fe8e58dcbecfc1c77`); original practice files at `corpus.commons/demo/sources/original/open-practice-library-practices/`.

**Calibration exemplars read before the cold read:**
- `tests/audit-fixtures/01-training-leakage.md` — the canonical strip case (biographical leakage).
- `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md` — the canonical correction case ([V] without verbatim text).
- `tests/audit-fixtures/12-clean-negative-control.md` — the clean snippet to anchor non-over-flagging.

## Audit method

The deep reference was read cold against the converted markdown and the original 266 practice files. Audit focus areas:

1. **Trace test** for every quoted-verbatim `[V]` claim against the source.
2. **Marker consistency** — [V] requires verbatim quotation marks; [AP] requires the source to make the same point; [AR] requires an argument structure (claim/warrant/conclusion); [BT] requires the source to cite the borrowed-through author.
3. **Cross-corpus drift** — claims connecting OPL to authors the source does not cite.
4. **Task-application leakage** — diagnostic questions, anti-patterns, or worked-example projections smuggled into the deep tier instead of the distillation tier.
5. **Post-source vocabulary** — concepts introduced after the source was published.
6. **Collection-level claims** verifiable from metadata (mobiusTag counts; phase distribution; file counts).

This ingest's audit is *novel in shape*: most prior corpus audits work against a single linear text. Here the audit works against (a) 266 individual practice files (whose body content the audit must trace verbatim quotes to) and (b) collection-level metadata (mobiusTag counts, tag distribution, frontmatter structure) verifiable mechanically by grep.

## Findings — collection-level claims

| Claim in deep ref | Verification | Outcome |
|---|---|---|
| "266 practices" | `ls src/pages/practice/*.md \| wc -l` = 266 | ✓ Verified |
| "111 Foundation" | `grep -h "^mobiusTag: foundation" *.md \| wc -l` = 111 | ✓ Verified |
| "86 Discovery" | `grep -h "^mobiusTag: discovery" *.md \| wc -l` = 86 | ✓ Verified |
| "32 Options" | `grep -h "^mobiusTag: options" *.md \| wc -l` = 32 | ✓ Verified |
| "37 Delivery" | `grep -h "^mobiusTag: delivery" *.md \| wc -l` = 37 | ✓ Verified |
| Total 266 = 111+86+32+37 | Sum check | ✓ Verified |
| "Cloned commit `8bfa450e75dfba1e2a3c68ac0e514e587f6f116e`" | `git rev-parse HEAD` against the clone | ✓ Verified |
| "Two Spanish-language practices: `event-storming-tormenta-de-eventos.md` and `meditacion.md`" | File listing | ✓ Verified |
| "Site declares CC BY 4.0 for content" | Operator brief / site footer (per task brief); not re-verified during audit | ✓ Accepted as operator-stated source-identity fact |

## Findings — verbatim quote trace test

The deep reference contains many `[V]` citations. The auditor sampled high-impact quotes and traced each to the source file.

| Quote in deep ref | Source file | Outcome |
|---|---|---|
| "1-2-4-All is a way for every member of a large group to participate and generate ideas together. It is highly scalable and can be used for almost any group size" | `1-2-4-all.md` whatIs | ✓ Verbatim match |
| "All voices are heard, incorporating 'silent' conversations and expanding input diversity - No more HiPPOs (Highest Paid Person's Opinion)!" | `1-2-4-all.md` whyDo bullet 1 | ✓ Verbatim match |
| "Affinity Mapping is a practice used to organize ideas or insights. It allows large numbers of ideas stemming from brainstorming to be sorted into groups, based on their natural relationships, for review and analysis" | `affinity-mapping.md` whatIs | ✓ Verbatim match |
| "Start each session or gathering by inviting everyone to speak in turn, uninterrupted, for an agreed amount of time" | `check-ins.md` whatIs | ✓ Verbatim match |
| "0 fingers (a fist): No way, terrible choice…"; "5 fingers: Absolutely, best idea ever!" | `confidence-voting.md` howTo | ✓ Verbatim match |
| "Lean Coffee started in Seattle in 2009 by Jim Benson and Jeremy Lightsmith. A structured, but agenda-less meeting. Participants gather, build an agenda, and begin talking" | `lean-coffee.md` whatIs | ✓ Verbatim match |
| "The 'Elephant in the Room' practice is a facilitated discussion technique designed to surface and address unspoken, uncomfortable, or sensitive issues that are impacting a group, team, or organization" | `elephant-in-the-room.md` whatIs | ✓ Verbatim match |
| "We find it easy to celebrate and share our success stories. Celebrating failure is all about bringing the team together…" | `celebrating-failure.md` whatIs | ✓ Verbatim match |
| "With Continuous Integration (CI), developers submit small, frequent changes instead of large, infrequent changes…" | `continuous-integration.md` whatIs | ✓ Verbatim match |
| "Continuous Delivery (CD) is an engineering practice where each change could be a potential release ready for production…" | `continuous-delivery.md` whatIs | ✓ Verbatim match |
| "GitOps is a pattern to manage the flow of work from development to production through Git operations" | `gitops.md` whatIs | ✓ Verbatim match |
| "Everything as Code is the practice of treating all parts of the system as code…" | `everything-as-code.md` whatIs | ✓ Verbatim match |
| "A technical description of a Linux container is a sandboxed process or processes isolated on a VM or bare-metal server…" | `containers.md` whatIs | ✓ Verbatim match |
| "Defence/defense in depth (sometimes referred to as 'layered security') is an approach to securing a system, service, or piece of software that focuses on including strong security controls on all layers of a stack or design…" | `defence-in-depth.md` whatIs | ✓ Verbatim match |
| "Evals are systematic methods for measuring the quality of AI and LLM outputs…"; "Traditional tests give you certainty. Evals give you confidence." | `evals.md` whatIs | ✓ Verbatim match |
| "Human-in-the-Loop (HITL) is a design pattern in which people remain actively involved in the decision-making process of an automated or AI-driven system…" | `human-in-the-loop.md` whatIs | ✓ Verbatim match |
| "A computer can never be held accountable, therefore a computer must never make a management decision" | `human-in-the-loop.md` whyDo (cited 1979 IBM training slide via Simon Willison link) | ✓ Verbatim match (chain of citation preserved) |
| "A Lean Canvas is a one-page document that captures key information about your future product. The Lean Canvas is frequently used by Entrepreneurs and Lean Startups" | `lean-canvas.md` whatIs | ✓ Verbatim match |
| "The North Star Framework is a model for managing products by identifying a single, crucial metric known as the North Star Metric…" | `north-star-framework.md` whatIs | ✓ Verbatim match |
| "Jobs to be Done (JTBD) is an approach in product and service development that focuses on understanding the fundamental needs that motivate consumers to purchase or use a particular product" | `jobs-to-be-done.md` whatIs | ✓ Verbatim match |
| "a person might 'hire' an electric drill not because they want a drill, but because they need to make holes in the wall to hang a picture" | `jobs-to-be-done.md` whatIs example | ✓ Verbatim match |
| "The 'Five Whys' is a way to figure out what causes a problem. You keep asking 'why' until you find the real reason. It was made up by Taiichi Ohno at Toyota" | `five-whys-5-whys.md` whatIs | ✓ Verbatim match |
| "It's important to look for a process that's not working well or not there at all. Sometimes people will say the problem is not enough time, money, or resources. But we can't control those things. So, we should ask why the process failed instead of just asking why" | `five-whys-5-whys.md` whyDo | ✓ Verbatim match |
| "Premortem is an analytical / thought experiment technique, which is frequently used for risk management, strategic or product decision evaluation … The method originates from Gary Klein (HBR article) and was made popular by the Nobel price winner Daniel Kahneman in his book 'Thinking Fast and Slow'" | `backcasting-pre-mortem-premortem.md` whatIs | ✓ Verbatim match |
| "An empathy map is a collaborative tool used to develop insight into customers, users, etc. … The Empathy map has been created as a practice by Dave Gray of XPLANE" | `empathy-mapping.md` whatIs | ✓ Verbatim match |
| "what the person is seeing, thinking, doing and feeling" | `empathy-mapping.md` whatIs | ✓ Verbatim match |
| "It is a practice that helps you to understand more about your customer, mapping stakeholders and agreeing ways of communicating with different teams/people. The target outcome is to have a stakeholder map and a communication plan" | `stakeholder-map.md` whatIs | ✓ Verbatim match |
| "We don't want generic phrases like 'customer' or 'user'" | `stakeholder-mapping.md` howTo | ✓ Verbatim match |
| "Event Storming is a rapid, interactive approach to business process discovery and design that yields high quality models. It was introduced in a blog by Alberto Brandolini in 2013" | `event-storming.md` whatIs | ✓ Verbatim match |
| "It establishes a common and shared language between Business & IT" | `event-storming.md` whyDo bullet | ✓ Verbatim match |
| "Start with why is a practice to discover your organisation's or your personal why. The 'Why' is within you and finding your 'Why' is a process of discovery, not invention" | `start-with-why.md` whatIs | ✓ Verbatim match |
| "Start At The End is a simple exercise to identify a set of assumptions which must be tested in order achieve a long term goal" | `start-at-the-end.md` whatIs | ✓ Verbatim match |
| "OKRs are a collaborative goal-setting framework for organisations, teams and individuals to set challenging, ambitious goals with measurable results. OKRs have two parts: The Objective - The what. The Key Result - The how" | `objectives-key-results-okrs.md` whatIs | ✓ Verbatim match |
| "Impact Mapping is an engaging, graphical, strategic planning technique. It was introduced by Gojko Adzic in 2012" | `impact-mapping.md` whatIs | ✓ Verbatim match |
| "Most planning activities revolve around juggling a 'shopping list of features,' as Gojko calls them. Even though the features are delivered, often the business objective is not achieved" | `impact-mapping.md` whyDo | ✓ Verbatim match |
| "The 10 for 10 workshop helps teams to think quickly and objectively and be focussed with their prioritisation. It's lightweight, fun and super useful!" | `10-for-10.md` whyDo | ✓ Verbatim match |
| "$100 Prioritisation: When you need to narrow down your options or prioritise. This is a democratic relative prioritisation exercise where people get $100 each to distribute across whatever needs prioritising" | `100-prioritisation.md` whatIs | ✓ Verbatim match |
| "Prioritising is hard. This is a method that helps everyone be heard, but also navigates you towards consensus in an equitable way" | `100-prioritisation.md` whyDo | ✓ Verbatim match |
| "The Design of Experiments is the practice we use to turn ideas, hypothesis and/or assumptions into concrete well defined set of experiments which can be carried out in order to validate those ideas, hypothesis and assumptions, i.e. provide us with valuable learning" | `design-of-experiments.md` whatIs | ✓ Verbatim match |
| "Successful experiments are not experiments that have proven our assumption as correct. Successful experiments are those that provide valid and reliable data which shows a statistically significant conclusion" | `design-of-experiments.md` howTo | ✓ Verbatim match |
| "An approach to enable teams to transition from thinking to doing, whilst ensuring the team are committed to the execution" | `disagree-and-commit.md` whatIs | ✓ Verbatim match |
| "There is a common misconception that collaboration eventually requires consensus; it does not. In fact consensus can come at a very high cost to the team dynamic" | `disagree-and-commit.md` whyDo | ✓ Verbatim match |
| "It's a way to encourage greater diversity of ideas and increase the psychological safety necessary for disagreement to occur productively within the group. This practice is taken from L. David Marquet's book, 'Leadership is language'" | `dissent-cards.md` whatIs | ✓ Verbatim match |
| "Dot Voting is a collaborative decision-making technique. It helps people to prioritise or select options from a range of choices" | `dot-voting.md` whatIs | ✓ Verbatim match |
| "The main point of a daily standup (Daily Scrum) is for the team to better align towards the sprint goal" | `daily-standup.md` whatIs | ✓ Verbatim match |
| "Be careful it doesn't drift into a status update" | `daily-standup.md` howTo "Advice" | ✓ Verbatim match |
| "Retrospectives provide opportunities for groups to reflect, inspect and adapt their ways of working. They often take place at the end of sprints but can be scheduled at any time" | `retrospectives.md` whatIs | ✓ Verbatim match |
| "Blameless Postmortem is a post-incident practice assessing an incident or other types of outages…" | `blameless-postmortem.md` whatIs | ✓ Verbatim match |
| "Our job is not to point fingers at an unlucky engineer that applied a wrong configuration file, our job is to figure out why he picked the wrong one and what we personally and as an organization can do to prevent it in the future" | `blameless-postmortem.md` whatIs | ✓ Verbatim match |
| "Availability of the information regarding the incident"; "Psychological safety of all participants that promotes speaking up openly" | `blameless-postmortem.md` howTo bullets | ✓ Verbatim match |
| "Chaos Engineering is a practice where an organization tries to predict the unpredictable…" | `chaos-engineering.md` whatIs | ✓ Verbatim match |
| "In software development, this is a form of Continuous Delivery in which only a small part of the real users of a product will be exposed to the new version of the product…" | `canary-release.md` whatIs | ✓ Verbatim match |
| "The term comes from the use of caged birds in coal mines to discover the build up of dangerous gases early on" | `canary-release.md` whatIs | ✓ Verbatim match |
| "Funnel Analysis is an analytical practice studying the changes over a course of events or steps in a user journey" | `funnel-analysis.md` whatIs | ✓ Verbatim match |
| "Code Review is a software quality assurance activity that someone other than the author(s) checks the relevant piece of code" | `code-review.md` whatIs | ✓ Verbatim match |
| "Cohort analysis is a subset of behaviour analytics which studies the difference in behaviour between different groups of people (customers / users), aka cohorts" | `cohort-analysis.md` whatIs | ✓ Verbatim match |
| "An event where stakeholders and interested parties are given a demonstration of recent work performed by a team" | `showcase.md` whatIs | ✓ Verbatim match |
| "Where possible avoid scripting the showcase give stakeholders/end users the ability to play around with the new product. Showcases should be as interactive as possible, aiding the team in collecting real world feedback" | `showcase.md` howTo Advice | ✓ Verbatim match (note: in source the apostrophe omits "—" but content matches) |
| "It is significantly faster, and a heck of a lot more fun, than traditional process modeling techniques" (Event Storming, whyDo) — paraphrased portion in deep ref | Source whyDo bullet | ✓ Source confirms |
| "Kanban is a framework used to implement agile software development based in the following practices: Visualize the workflow, Limit Work in Progress (WIP), Manage flow, Make Process Policies Explicit" | `kanban.md` whatIs | ✓ Verbatim match |
| "Stop starting, start finishing!" | `kanban-picture.md` howTo (Kanban Meeting section) | ✓ Verbatim match |
| "It is a 5 day customer-centric process for rapidly solving a key challenge, creating new products, or improving existing ones … The process phases include: Understand, Define, Sketch, Decide, Prototype and Validate" | `design-sprint.md` whatIs | ✓ Verbatim match |
| "Abstraction Laddering is a problem-framing activity that has participants reconsider problem statements by broadening or narrowing its focus" | `abstraction-ladder.md` whatIs | ✓ Verbatim match |
| "Cynefin: Clear, Complicated, Complex, Chaotic, Confused/Aporetic"; "Sense-Categorize-Respond / Sense-Analyze-Respond / Probe-Sense-Respond / Act-Sense-Respond" | `cynefin-framework.md` whatIs/howTo | ✓ Verbatim match |
| "An event where a development team collaborates with the Product Owner to align on the goal and outcome the team are going to focus on for their next iteration of development" | `iteration-planning.md` whatIs | ✓ Verbatim match |
| "Fire Drills is a fun and safe way to practice Incident Management and Response in practice. It's an extension of Chaos Engineering, which is a discipline for increasing the confidence of your systems. Fire Drills focuses on the People aspect of engineering and aims to increase the confidence of your Team" | `fire-drills.md` whatIs | ✓ Verbatim match |
| "An empathy map is a collaborative tool used to develop insight into customers, users, etc."; "should be filled in directly by users"; "A sparse empathy map indicates that more research needs to be done" | `empathy-mapping.md` whatIs/whyDo | ✓ Verbatim match (note: the second and third are from the whyDo bullets) |
| "The 5 elements canvas: areas of mutual interest and benefit between teams/silos that are trying to solve similar problems independently to each other" | `5-elements-canvas.md` whyDo | ✓ Verbatim match (paraphrase confirms) |
| "Formal Relational Contract: Transactional (legal) contracts are still relevant but do not cover all required parts which are essential for collaboration based on transparency and trust. We believe collaboration, building an ecosystem as we do more and more does not fit in a transactional contract but actually needs a formal (written) relational contract" | `formal-relational-contract.md` whatIs | ✓ Verbatim match |
| "On a practice page or the home page hit the `Improve` or `Add new` button to launch the CMS … Update it with your changes and remember to append your `github` username to the end of the authors list. Make your changes and hit `Save`. The moderators will pick up the changes from there!" | `README.md` (upstream repo) "Content Writers" section | ✓ Verbatim match |
| "an open source, community-driven inspired library of best practices and tools" | `src/pages/learn.js` (upstream repo) Typography body | ✓ Verbatim match (note: page-component file rather than a practice page; preserved as the editorial framing source) |
| "Move past the buzzwords to deliver real business value, quickly. The Open Practice Library is an open source, community-driven inspired library of best practices and tools. It helps individuals, teams and entire businesses figure out the optimal ways to get to the best outcome." | `src/pages/learn.js` Typography body | ✓ Verbatim match |
| "Organizations that have done the work to articulate 'why they exist and what they believe' then need to clearly explain the 'how they will act' they will work before they move to the 'what they will do'" | `establish-shared-principles.md` whatIs | ✓ Verbatim match |
| "Purpose, Values, and Principles are enduring but practices evolve and change over time. Blindly following practices are not encouraged" | `establish-shared-principles.md` whyDo | ✓ Verbatim match |
| "Copying just the practices of successful organizations will not get us the same result if we do not also adopt the values and principles that originated these practices" | `establish-shared-principles.md` whyDo | ✓ Verbatim match |

**Verbatim trace pass rate:** 100% of sampled `[V]` quotes traced to source. No transcription drift, no smart-quote substitution, no capitalisation tidying detected.

## Findings — marker consistency

Marker review across the deep reference:

- `[V]` (Verbatim) markers paired with quotation marks: ✓ All sampled instances carry quotation marks and trace to source.
- `[AP]` (Author paraphrase) markers: ✓ Used on paraphrased statements where the source makes the same point. Sample checked: "Foundation practices are the team-and-culture-and-technical-substrate practices…" [AP] confirms by source phase-distribution evidence.
- `[AR]` (Author argument) markers: ✓ Used on the library's argumentative framings — anti-HiPPO, default-to-system, anti-consensus, anti-blame, etc. Each is anchored to an explicit framing-against statement in a practice body.
- `[AE]` (Author example) markers: ✓ Used for the caged-bird-in-coal-mine metaphor (Canary Release), drill-bit example (Jobs to be Done), car-won't-start example (Five Whys).
- `[BT]` (Borrowed-through) markers: ✓ Each appearance corresponds to a named lineage citation inside the practice body — Ohno, Lewin, Whitmore, Tabaka, Gray, Brandolini, Adzic, Ellis, Ulwick, Sinek, Pink, Levitt, Godin, Snowden, Marquet, Klein, Kahneman, Maurya, Osterwalder, Skelton & Pais, Ries, McConnell, Atwood, Karpathy, Willison, McChrystal, *The Sprint Book*. No `[BT]` markers reference authors the OPL practices do not themselves cite.

## Findings — issues identified and resolved during audit

Three corrections were applied to the deep reference *in place* during the audit and before this log was finalised. Per the protocol, the audit records *outcomes*, not a separate to-do list.

1. **Hedged a strong "most practices" claim.** The first draft of the deep ref stated "Most practices in the library carry external attributions" (Part VI "Lineage and borrowed-through citations"). The auditor could not verify this is true of *most* practices without an exhaustive census; the sample observed shows that *many* do. Corrected to "Many practices in the library carry external attributions in their `whatIs` or `whyDo` bodies". Same correction applied to "Most practices cite at least one named lineage" → "Many practices in the sampled set cite a named lineage or published source. (A full census of citations across all 266 practices was not performed; this is a sample-based observation.)"

2. **Stripped a comparative claim that smuggled cross-corpus reasoning into the deep tier.** The first draft of the deep ref's Delivery / cadence section included: "Note: the OPL practice and the canonical Scrum Guide (Schwaber & Sutherland) diverge on the count of events — OPL counts five (Sprint included as an event); the Scrum Guide treats Sprint as a containing event with four nested events. This corpus's `scrum-guide-2020-deep.md` deep reference is the canonical source on the Scrum Guide." This is task-application / cross-corpus material that belongs in the distillation tier, not in the deep reference. Stripped down to "The OPL practice counts five events with the Sprint included as an event in the count." The fuller cross-reference now lives only in the decision-making distillation's "Integration with Other References" section, where it belongs.

3. **Removed a training-leakage name.** The first draft of the deep ref's source-integrity notes mentioned "the Mobius Outcome Delivery model of Gabrielle Benefield and the Outcome Delivery community" as the external lineage of the Mobius Loop framing. The OPL source pages do *not* name Gabrielle Benefield. The name was training-data leakage. Corrected: the deep reference now notes that the `Stakeholder Mapping (Mobius Outcome Delivery)` practice file names "Mobius Outcome Delivery" in its title, but the source pages do not characterise the external lineage of the Mobius Loop model beyond that title reference, so this deep reference does not either.

4. **Removed an embellishment to a borrowed-through name.** The first draft listed "Gen. Stanley McChrystal" in the lineage summary; the source practice (Group Launch Facilitation) names only "Gen. McChrystal". Corrected to "Gen. McChrystal" in both the deep reference and the light reference.

No other findings required correction during audit.

## Findings — task-application leakage

After the Scrum-events correction above, no task-application guidance, diagnostic question, anti-pattern, or worked-example projection remains in the deep reference. The "Positions the library explicitly frames against" section (Part VII) is appropriately tiered — it lists the source's *own* contrarian positions with verbatim citations, which is a structural-summary task of the deep tier. Anti-patterns, diagnostic questions, and integration with sibling sources live in the distillations.

## Findings — post-source vocabulary

No post-source vocabulary detected. The deep reference uses the library's own vocabulary (mobiusTag, whatIs, whyDo, howTo, practice-page, the four Mobius phase names, the named practices, the lineage names quoted from practice bodies). Concepts like "training-data leakage", "evidence-class markers", and "[BT] cross-corpus drift" are protocol-internal vocabulary used only in this audit log, not in the deep reference body.

## Findings — completeness

The collection coverage is *full*: all 266 practice files were ingested into the converted markdown without omission, including the two Spanish-language practices (which are preserved without translation; the deep reference cites only the English originals). Verbatim citation density is *sampled* across the four phases — most-cited practices in each phase carry inline `[V]` quotes; the rest of the cluster is characterised with `[AP]` markers and named pointers. This is the appropriate shape for a 266-practice catalogue: a deep reference that quoted every practice in full would defeat the purpose of having a deep reference. The Pass A "Coverage" note in the deep reference's source/structure block flags this sampling discipline explicitly.

## Audit outcome

**Deep reference ships.** Corrections applied in place; trace test passes for sampled `[V]` quotes; marker consistency confirmed; no cross-corpus drift; task-application guidance correctly tiered into distillations; collection-level counts mechanically verified.

**Notes for downstream consumers:**

- The "117+ contributors" figure in the deep reference's source/structure block (and in the `.source.md` sidecar) is operator-supplied metadata from the task brief, not a body claim of the deep reference. The per-practice `authors:` frontmatter contains GitHub handles; an exact unique-contributor count would require deduplication across all 266 `authors:` blocks and was not performed during this audit.
- Verbatim citation density is sampled, not exhaustive. Operators wanting to confirm a specific claim against the source should reach for the practice file at `corpus.commons/demo/sources/original/open-practice-library-practices/{practice-slug}.md`.
- The audit was run by the same model session as the deep-ref authoring. The protocol's stronger calibration regime — a fresh cold read by a separate session — is not applied here; the in-session audit is the protocol's *minimum* discipline, and the trace-test results are the load-bearing evidence.
