<!-- derived-from-deep: sha256:a093fe41c71549506e2e4922737724d93a0ef13f81c2a7a57959000159e5e1a3 -->
# Microsoft, Code-With Engineering Playbook (selected sections), Warranting Agent-Built Software Distillation

**Source:** Microsoft (Industry Solutions Engineering), with contributors. *Code-With Engineering Playbook* (selected sections), repository commit 016770e43d8a75be87b98c000c049f07c4a6e6f8 (2025-09-26). Licence: CC BY 4.0 for the documentation; code samples MIT. Attribution: *Code-With Engineering Playbook*, Microsoft (Industry Solutions Engineering) and contributors, CC BY 4.0; this distillation paraphrases and quotes the source, and changes were made. Scope: open.
**Coverage:** partial, operator-approved 2026-10-14. This distillation draws on an operator-approved subset of the playbook: the automated-testing pages (overview, test planning, unit, integration, end-to-end, consumer-driven contract, smoke and fault-injection testing), the whole code-reviews section, the definitions of done and of ready, and the non-functional requirements capture guide. Nothing here speaks for the playbook's other sections (performance, UI, shadow and synthetic-monitoring testing, CI/CD, observability, security and the rest).

## Warranting Agent-Built Software Relevance

The playbook is a practitioner's account of the checks a team puts around a change before it merges and ships: tests planned from the acceptance criteria, unit tests reliable enough that a failure means a bug, merging blocked when tests fail, small pull requests reviewed by someone other than the author, gates enforced by repository policy rather than goodwill, and written definitions of done, of ready and of each non-functional requirement. None of it was written about coding agents. Its value for warranting agent-built software is that it states, for human teams, many of the harness's gates as named practices with reasons attached, so a reviewer agent or the accountable builder can cite a reason for a block rather than a preference. Its recommendations are the playbook's own assertions [AP]; it reports no studies of its own, and its numbers are examples and thresholds, not measurements.

It speaks most directly to the "agent says it's done" reflex (a passing build is evidence only if the tests can fail for the right reason, and the playbook is specific about what makes a test able to fail: reliability, isolation, assertions on logic rather than on mock returns) and to the "I read the diff" reflex, where its position is double-edged: it asks reviewers to read every changed line, and it makes that possible by keeping each change small and handing the mechanical checks to automation.

**Applicability gate: clear yes.** The source surfaces questions an accountable builder asks at six of the eight phases (is "correct" written down as a check; did the test change to make the build pass; would this suite catch a wrong implementation; who reviews, and does review reach the logic; what does "done" mean here; is the availability target written down). Its contrarian positions (against tests tied to the implementation, against deferring tests, against large unfocused changes) bear directly on the harness. No lens applies; the axis declares none.

**Phase mapping.**

| Phase | Fit | What this source brings |
|---|---|---|
| 1. Specifying the change | Strong | Test cases planned from acceptance criteria at design; Definition of Ready; measurable non-functional requirements; small slices |
| 2. Triaging risk | Moderate | Security and PII checks in the reviewer's pass; security and recovery test plans; risk-prioritised test cases; breaking-change and migration-path disclosure |
| 3. Locking the tests | Strong | What makes a unit test trustworthy; state versus behavioural verification; coverage that still misses a bug; tests first |
| 4. Building in the sandbox | Thin | Only one point: tests and experiments stay out of production unless the blast radius has been weighed. The source does not cover agent permissions, sandbox isolation, untrusted input or dependency vetting |
| 5. Gating deterministically | Strong | Merge blocked on failing tests; policy-enforced PR requirements; flaky tests as defects; no new errors or warnings; smoke tests as gates |
| 6. Reviewing independently | Strong | Reviewer outside the pair; read every changed line; small PRs; review focus on logic and tests; findings resolved or reasoned "won't fix"; bias toward trusted authors |
| 7. Warranting the change | Moderate | Definition of Done as the sign-off checklist; PR template evidence fields; non-functional requirement owner and verification method; shared understanding as a review goal |
| 8. Releasing and operating | Moderate | Availability as a measurable requirement; smoke tests on deployments; canary and blue/green with a blast-radius budget; regression tests from fixed bugs; telemetry in the Definition of Done; maintainability metrics |

## Key Concepts for Warranting Agent-Built Software

1. <!-- concept: tests-as-part-of-done --> **A change without tests is unfinished, and failing tests stop the merge.** "We consider code to be incomplete if it is not accompanied by tests" [V], and "We write our tests early and block any further code merging if tests fail." [V] (Source: Microsoft, *Code-With Engineering Playbook*, docs/automated-testing/README.md, "The Fundamentals"). For a warranty, this turns "the agent says it's done" into a checkable claim: done means tests accompany the change and the merge gate ran them.

2. <!-- concept: test-planning-from-acceptance-criteria --> **Test cases are planned from the acceptance criteria while the change is designed.** The five steps run from understanding and clarifying the criteria, through positive and negative scenarios (and a decision on whether security, accessibility and reliability are in scope), to documented cases in Given-When-Then form, automation of hot paths and critical areas, and peer review of the cases [AP]. The exercise "also helps clarify the acceptance criteria and informs how we should build the solution" [V] (docs/automated-testing/test-planning.md, "Building test cases for a user story").

3. <!-- concept: definition-of-ready --> **Definition of Ready: a change is not started until it can be estimated.** "If a user story is not Ready in the beginning of the Sprint it increases the chance that the story will not be done at the end of this sprint." [V] Ready items include the input values needed, clear and complete acceptance criteria that can be measured, the business need, a size that fits a short time, and any blocking work [AP] (docs/agile-development/team-agreements/definition-of-ready.md, "Definition of Ready"; "Examples of Ready Checklist Items").

4. <!-- concept: definition-of-done --> **Definition of Done: the team's written sign-off checklist.** "The development team should decide together what their Definition of Done is and document this in the project." [V] At story level: acceptance criteria met, unit tests written and passing, existing tests passing, code review complete, sufficient diagnostics and telemetry, documentation updated, product-owner sign-off; sprint and release levels add integration, performance and end-to-end tests passing and a release marked ready by the product owner [AP] (docs/agile-development/team-agreements/definition-of-done.md, "Feature/User Story"; "Sprint Goal"; "Release/Milestone").

5. <!-- concept: measurable-non-functional-requirements --> **Non-functional requirements stated so a machine can check them.** "Be specific: Avoid ambiguity and make sure the requirement is quantitative, measurable and testable." [V] The capture template records a metric, a verification method (automated test, benchmark, simulation, prototyping), constraints and an owner for each requirement [AP]; the taxonomy's thresholds (uptime and allowed downtime, response time, error rate, complexity, coverage) are illustrative examples, not measurements [AP] (docs/design/design-patterns/non-functional-requirements-capture-guide.md, "Documenting Non-Functional Requirements - Best Practices"; "Template"; "Examples").

6. <!-- concept: unit-test-reliability --> **A test is worth trusting only if its failure means a bug.** A unit test "should be 100% reliable so failures indicate a bug in the code" [V] (docs/automated-testing/unit-testing/README.md, "Unit Testing"). Sleeps, disk reads and live third-party calls break that reliability; if code is flaky without a sleep, find out why and remove the flakiness [AP] (docs/automated-testing/unit-testing/README.md, "Things to Avoid").

7. <!-- concept: state-vs-behavioural-verification --> **Assert on the logic, not on what the double returned, and beware tests tied to the implementation.** "make assertions on your logic, not mock return values" [V]; the page's example test would still pass if the method simply returned the literal value [AE] (docs/automated-testing/unit-testing/mocking.md, "Assertions"). Mocks do behavioural verification, and "The major downside to behavioral verification is that it is tied to the implementation." [V] Tests that must be updated whenever the implementation changes lose the confidence that a passing test signals a safe change [AP] (docs/automated-testing/unit-testing/mocking.md, "Mocks").

8. <!-- concept: coverage-is-not-sufficiency --> **Full coverage can still miss the bug.** In the authoring example the first tests pass with 100% coverage, yet a known bug shows that not all inputs are covered; tests restated as intended behaviour leave 4 failing and 1 passing until the fix [AE] (docs/automated-testing/unit-testing/authoring-example.md, "Fixing the Bug"). Abstracted dependencies are never unit-covered, so integration or functional tests are still needed: "Unit testing is extremely important, but it is also not the silver bullet" [V] (docs/automated-testing/unit-testing/README.md, "Abstraction"; "Conclusion").

9. <!-- concept: small-pull-requests --> **Small, single-purpose changes are what make review possible.** "More code there is to review, the higher chances there are letting a bug sneak through." [V] (docs/code-reviews/process-guidance/README.md, "Code Reviews Shouldn't Include too Many Lines of Code"). A PR should have one reason to change the project, carry its tests and not break the build; "Start small, it is easier to create a small PR from the start than to break up a bigger one." [V] (docs/code-reviews/pull-requests.md, "Best Practices").

10. <!-- concept: reviewer-outside-the-author --> **Review by someone who did not write the change, aimed at logic and tests.** "Someone outside the pair should perform the code review." [V]; for a mob, a member who spent less or no time at the keyboard reviews [AP] (docs/code-reviews/faq.md, "We Pair or Mob. How Should This Reflect in our Code Reviews?"). Automation takes the mechanical checks so that "human reviewers can focus on architectural and functional correctness" [V]: business logic, new or changed tests, readability and maintainability, and the team's checklist of common errors (docs/code-reviews/process-guidance/reviewer-guidance.md, "Reviewer Guidance").

11. <!-- concept: policy-enforced-gates --> **Gates enforced by policy, and evidence that they ran.** PR requirements "can and should be enforced by policies" [V] (docs/code-reviews/pull-requests.md, "Pull Requests"). The evidence checklist: branch policies on every main branch, linters and unit tests in every build, each bug linked to the PR that introduced it with a note on how review might have caught it, and review checklists updated with common issues [AP] (docs/code-reviews/evidence-and-measures/README.md, "Evidence").

12. <!-- concept: smoke-tests-and-blast-radius --> **Quick gates before costly stages, and the blast radius weighed before any live experiment.** A failed smoke test lets the rest of the integration or deployment chain be abandoned [AP] (docs/automated-testing/smoke-testing/README.md, "Problem Addressed"). For fault injection in production, "Thinking about the Blast Radius of the effect, should the test fail, is a crucial step to conduct beforehand." [V]; start outside production, gate CD stages, use blue/green and canary deployments, and agree a budget as a service level objective [AP] (docs/automated-testing/fault-injection-testing/README.md, "Best Practices and Advice").

## Questions to Ask During Warranting Agent-Built Software

### Phase 1: Specifying the change

| Need | Question | Source-tag |
|---|---|---|
| "Correct" is only in prose | Has each acceptance criterion become a planned test case with preconditions, steps and an expected result, before the agent starts? Which ambiguities did writing them expose? | test-planning.md, "Building test cases for a user story" |
| Negative paths are missing | Which negative and error cases are planned alongside the happy path? Are security, accessibility and reliability in or out of scope, and is that written down? | test-planning.md, "Building test cases for a user story" |
| What must not change | Which non-functional requirements does this change touch, and does each have a metric, a verification method and an owner? | non-functional-requirements-capture-guide.md, "Template" |
| The change is not ready | Does the story give the input values and measurable acceptance criteria the agent needs, and is it small enough to finish and review in a short time? | definition-of-ready.md, "Examples of Ready Checklist Items" |
| The change is large | Can it be split into self-contained changes that each add value, or released behind a hidden feature, so each PR has one reason to change? | pull-requests.md, "Best Practices" |

### Phase 2: Triaging risk

| Need | Question | Source-tag |
|---|---|---|
| Security-sensitive diff | Does the security test plan cover authentication and authorisation for this change? Has the reviewer's functionality pass looked for security flaws? | test-planning.md, "Other Test Plan Examples"; reviewer-guidance.md, "Code Quality Pass" |
| Personal data | Do any names or log lines expose customer information? Is PII handled correctly, including in logging? | reviewer-guidance.md, "Code Quality Pass" |
| Irreversible data change | Does the PR declare the change breaking, with its impact and migration path? Is there a recovery test that checks data integrity afterwards? | pull-request-template.md; test-planning.md, "Other Test Plan Examples" |
| Critical paths | Have the test cases been prioritised by risk, and are the most critical transactions tested end to end, layer by layer? | test-planning.md, "Grouping Test Cases into Test Plans"; testing-methods.md, "Vertical Test" |

### Phase 3: Locking the tests

| Need | Question | Source-tag |
|---|---|---|
| A test was edited | Did the expected behaviour change, or did the implementation change and the test follow it? If a test fails, which bug does it point to? | unit-testing/README.md, "Unit Testing"; mocking.md, "Mocks" |
| Assertions | Does each test assert on the logic the change adds, or on values the test double was told to return? | mocking.md, "Assertions" |
| Brittle tests | Do the tests verify the sequence of calls the implementation makes, so any refactor breaks them? | mocking.md, "Mocks" |
| Coverage as comfort | Coverage is high, but what input would the suite miss? Are the tests written as intended behaviour or as a description of what the code currently does? | authoring-example.md, "Fixing the Bug" |
| Order of writing | Were the tests written first, from the behaviour list, or after the code by the same session? | unit-testing/README.md, "Test-Driven Development" |
| Reliability | Does any test sleep, read from disk or call a live third-party API? Does the unit suite run in seconds? | unit-testing/README.md, "Things to Avoid" |

### Phase 5: Gating deterministically

| Need | Question | Source-tag |
|---|---|---|
| Merge gate | Is merging blocked by policy when a test fails, or by habit? | automated-testing/README.md, "The Fundamentals"; pull-requests.md, "Pull Requests" |
| Flakiness | When a check passed on retry, has the cause of the flakiness been found and removed? | unit-testing/README.md, "Things to Avoid" |
| Warnings | Does the change compile and run without errors or warnings, with no new lint findings? | pull-requests.md, "General Process"; pull-request-template.md |
| Tests deferred | Are the tests in this PR, or promised for the next one? | reviewer-guidance.md, "Code Quality Pass" |
| Performance | Which stated metric does this change's performance get checked against, and by which verification method? | non-functional-requirements-capture-guide.md, "Template" |

### Phase 6: Reviewing independently

| Need | Question | Source-tag |
|---|---|---|
| Independence | Who reviews, and did they take part in writing the change? | faq.md, "We Pair or Mob. How Should This Reflect in our Code Reviews?" |
| Depth | Has the reviewer read every changed line, in a logical order, with the whole file in view? Is the change small enough for that to be realistic? | reviewer-guidance.md, "Understand the Code You are Reviewing" |
| Focus | Did the review reach the business logic and the tests, or stop at style that automation should catch? | reviewer-guidance.md, "Reviewer Guidance" |
| Findings | Is every finding resolved, or marked "won't fix" with a reason? Have out-of-scope findings become separate work items? | author-guidance.md, "Be Open to Receive Feedback"; reviewer-guidance.md, "Take Your Time and Keep Focus on Scope" |
| Trust by reputation | Is this change being passed because its author (or agent) has been reliable before? | inclusion-in-code-review.md, "Types and Examples of Non-Inclusive Code Review Behavior" |
| History | Which past bugs trace back to changes in this area, and how might review have caught them? | evidence-and-measures/README.md, "Evidence" |

### Phase 7: Warranting the change

| Need | Question | Source-tag |
|---|---|---|
| Done | Which Definition of Done items does the ledger show as met, and which only as claimed? | definition-of-done.md, "Feature/User Story" |
| Run evidence | Beyond the "tests passed" tick, does the PR record which test sets ran, the scenarios tried and the logs? | pull-request-template.md |
| Ownership | Does each non-functional requirement the change touches have an owner and a verification method? | non-functional-requirements-capture-guide.md, "Template" |
| Shared understanding | Who other than the author now understands this code, and is the documentation updated? | code-reviews/README.md, "Goals"; definition-of-done.md, "Feature/User Story" |

### Phase 8: Releasing and operating

| Need | Question | Source-tag |
|---|---|---|
| Availability | What uptime is the requirement, and how much downtime a year does it allow? | non-functional-requirements-capture-guide.md, "Operational Requirements" |
| Staged release | What smoke test runs on each deployment, and what stops the chain if it fails? | smoke-testing/README.md, "Applicable to" |
| Traceability | Can a failing request be followed across services by correlation ID, with parameters logged at startup? | automated-testing/README.md, "Build for Testing" |
| Decay | Which maintainability metrics (complexity, coverage, churn) are tracked against a stated threshold? | non-functional-requirements-capture-guide.md, "System Maintainability Requirements" |
| After a failure | Has the fixed bug become a regression test, and is it linked to the change that introduced it? | fault-injection-testing/README.md, "Fault injection testing in the development cycle"; evidence-and-measures/README.md, "Evidence" |

Phase 4 (building in the sandbox) gets no question table: the source speaks to it only through the production-testing point logged under trigger extensions.

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| A test's expected value changed in the same diff as the code it tests | Either the behaviour was meant to change, or the test was moved to match the implementation; a test that follows the implementation no longer signals a safe change (mocking.md, "Mocks") | Ask for the requirement that changed; if none, restore the test and treat its failure as a bug |
| Tests assert on the value a mock was set up to return | The test checks the mock's setup, not the logic (mocking.md, "Assertions") | Assert on what the change computes, or verify the calls it makes with the right parameters |
| A test sleeps, retries or reads an expected value from a file | Reliability and isolation are broken; a pass is no longer evidence (unit-testing/README.md, "Things to Avoid") | Find the cause of the flakiness and replace the sleep with a reliable state signal |
| "100% coverage" is offered as proof | Coverage shows lines ran, not that every input was checked (authoring-example.md, "Fixing the Bug") | Ask which inputs and negative cases the tests state as intended behaviour |
| The PR is large and touches several concerns | Review effectiveness falls with size, and a bug is more likely to slip through (process-guidance/README.md) | Split by self-contained value or by layer before review |
| The reviewer is the session that wrote the change | Review loses the outside view the playbook requires of a pair (faq.md) | Route to a reviewer who took no part in writing it |
| Review comments sit unresolved, or are answered "later" | In-scope deferral is not acceptable (author-guidance.md, "Be Open to Receive Feedback") | Resolve, or mark "won't fix" with a reason; move out-of-scope items to new work items |
| Integration tests carry the business-logic checks | The playbook's own pages pull two ways: one allows moving coverage to fast integration tests, the other says to keep business logic out of them (unit-testing/README.md, "Transferring Responsibility to Integration Tests"; integration-testing/README.md, "Things to Avoid") | Ask which tests would fail if a business rule were wrong, and whether they run fast enough for every change |
| An end-to-end environment holds a copy of production data | The comparison table expects this for end-to-end tests (testing-comparison.md); the reviewer's pass asks for correct treatment of PII (reviewer-guidance.md) | Confirm the PII handling for that copy before the agent gets access to it |

## When to Use This Reference

Reach for this source when:

- A gate needs a named reason drawn from ordinary engineering practice: why a failing test blocks the merge, why tests come in the same PR, why a big PR is sent back, why the author's own session cannot be the reviewer.
- The question is whether a test suite can be trusted to fail: reliability, isolation, assertions on logic, behavioural verification, coverage.
- "Done" or "ready" needs to be written as a checklist the harness can check against.
- A non-functional requirement (availability, performance, maintainability) needs to be stated with a metric, a verification method and an owner.
- A release or a live experiment needs a stop condition (smoke gates) or a blast-radius check.

Reach elsewhere for: security requirements at a stated level (`owasp-asvs-5-0`); threats specific to LLM features and agents, sandboxing and excessive agency (`owasp-llm-top10-2026`, `owasp-agentic-top10-2026`, `owasp-agentic-threats-mitigations`); measuring how strong an agent-written suite is (`egashira-testsuitebench-2026`); evidence on how AI assistance changes speed and quality (`becker-metr-ai-developer-productivity-2025`, `he-cursor-velocity-complexity-2025`, `dora-ai-assisted-swdev-2025`); formal independent assurance and sign-off roles (`uk-aqua-book-2025`). The playbook does not discuss coding agents at all; every mapping from its human-team practice to an agent harness in this file is the projection's, not the source's.

## Worked Example

A builder's agent has added a refund-on-cancellation rule to a client's booking service. The session log ends with the agent's summary: all tests pass, done. The independent reviewer opens the change's ledger.

The PR is about 1,400 lines across the booking model, the payment client, a migration and the tests. The playbook's first move is size: "More code there is to review, the higher chances there are letting a bug sneak through." [V] (docs/code-reviews/process-guidance/README.md, "Code Reviews Shouldn't Include too Many Lines of Code"). The reviewer returns it to be split into the rule itself, the payment-client change and the migration, each with one reason to change (docs/code-reviews/pull-requests.md, "Best Practices").

In the rule's slice, the tests mock the payment client and assert that the refund amount equals the value the mock was set to return. The playbook names this directly:

> "make assertions on your logic, not mock return values"
> (docs/automated-testing/unit-testing/mocking.md, "Assertions") [V]

The test would pass whether or not the refund calculation is right, so it is not evidence of the rule. The reviewer asks for tests that state the rule as intended behaviour, including the negative cases (a cancellation past the refund window, a partial refund), as the test-planning page's positive-and-negative step requires (docs/automated-testing/test-planning.md, "Building test cases for a user story").

The diff also changes one existing test's expected value from a full refund to a partial one, with no matching change to the acceptance criteria. Under the playbook's account of tests that move with the implementation, this is the warning sign:

> "The major downside to behavioral verification is that it is tied to the implementation."
> (docs/automated-testing/unit-testing/mocking.md, "Mocks") [V]

A test edited to match new code no longer tells anyone the change is safe. The reviewer blocks the change until the client's product owner confirms whether the expected behaviour changed; if it did not, the original test stands and its failure is a bug (docs/automated-testing/unit-testing/README.md, "Unit Testing").

One test sleeps for two seconds before asserting, and the CI history shows it failed once and passed on retry. The playbook treats that as a defect in the test, not noise: find out why it is flaky and replace the sleep with a reliable signal (docs/automated-testing/unit-testing/README.md, "Things to Avoid"). The migration's PR must say it is breaking and give the migration path (docs/code-reviews/pull-request-template.md, "Pull Request Template"). The warranty assessor then checks the ledger against the team's written Definition of Done: tests written and passing, code review complete, documentation updated, product-owner sign-off (docs/agile-development/team-agreements/definition-of-done.md, "Feature/User Story"). The assessor records which items were demonstrated and which were only claimed, and hands the sign-or-return decision to the builder.

## Anti-patterns This Reference Helps Avoid

- **Green by editing the test.** Signal: a test's expected value changes alongside the code. The playbook's reason: a test tied to the implementation loses its value as a safety signal (mocking.md, "Mocks"). Instead: tie the change to a changed requirement, or restore the test.
- **Tests that test the double.** Signal: assertions on mocked return values. Reason: they check the mock's setup, not the logic (mocking.md, "Assertions"). Instead: assert on the logic, or verify the calls.
- **Coverage as warranty.** Signal: a coverage number stands in for test review. Reason: the authoring example reaches 100% coverage with a known bug still uncaught (authoring-example.md, "Fixing the Bug"). Instead: ask which inputs and negative cases the tests state.
- **Flaky but tolerated.** Signal: retries, sleeps, intermittent passes. Reason: a test should fail only for a bug (unit-testing/README.md, "Unit Testing"). Instead: remove the cause of the flakiness.
- **Tests to follow.** Signal: code merged with tests promised later. Reason: tests are committed in the same PR as the code (reviewer-guidance.md, "Code Quality Pass"). Instead: block the merge.
- **The giant agent PR.** Signal: one change spans many concerns. Reason: bugs slip through large reviews (process-guidance/README.md). Instead: split before review.
- **Self-review.** Signal: the writing session approves its own change. Reason: the playbook puts review outside the pair (faq.md). Instead: an independent reviewer.
- **Review by reputation.** Signal: a change passes quickly because its author has been reliable. Reason: assuming one developer's code is always good, and not reviewing it properly, is named as biased decision-making (inclusion-in-code-review.md). Instead: review the change, not the track record.
- **Gates on goodwill.** Signal: merge rules live in a README, not in branch policy. Reason: PR requirements should be enforced by policies (pull-requests.md, "Pull Requests"). Instead: encode the gate where it cannot be skipped quietly.
- **Testing in production without a blast radius.** Signal: an experiment or test is aimed at the live system first. Reason: weigh the blast radius beforehand and start outside production (fault-injection-testing/README.md, "Best Practices and Advice"). Instead: a scaled-down copy, then a staged rollout.

## Integration with Other References

| Reference | Relationship |
|---|---|
| UK Duck Book, QA of code (`uk-duck-book-qa-of-code`) | Close agreement on what makes a test trustworthy: the Duck Book's deterministic tests, where the only reason to fail is incorrect code, match the playbook's 100%-reliable unit test; both use Arrange/Act/Assert and run tests on every change. They part on pairing: the Duck Book recommends pair programming as the most timely form of code review, while the playbook asks for a reviewer from outside the pair. The Duck Book also lets managers rely on proportionate assurance without reading the code, where the playbook asks the reviewer to read every changed line |
| UK Aqua Book (`uk-aqua-book-2025`) | The Aqua Book's rule that the assurer and the analyst shall be independent is the governance form of the playbook's code-level rule that someone outside the pair reviews. The Aqua Book adds the formal sign-off roles the playbook leaves to the product owner |
| Cucumber BDD and Gherkin (`cucumber-bdd-gherkin`) | The playbook places Given-When-Then test cases inside test planning; Cucumber supplies the discovery conversation that should come before them and the declarative style that keeps scenarios stable. Both warn that tests tied to implementation detail must change whenever the implementation does: the playbook for mock-based behavioural verification, Cucumber for imperative scenarios |
| TestSuiteBench (`egashira-testsuitebench-2026`) | The playbook's authoring example shows a fully covered suite missing a bug; TestSuiteBench measures that gap directly, scoring agent-written suites by the requirement-specific mutants they kill. The playbook's coverage thresholds are examples, so this source is where a suite's strength gets measured |
| OpenSSF, finding and fixing vulnerabilities with AI (`openssf-finding-fixing-vulnerabilities-ai`) | Both turn a fixed problem into a check that runs again: the playbook through regression tests written from fixed issues and a full-regression plan that keeps every fixed bug; OpenSSF through deterministic checks on every change rather than reruns of a non-deterministic AI. OpenSSF extends the playbook's review to AI-proposed changes and the prompt-injection risk of reviewing untrusted PRs with agents |
| NIST SSDF 1.1 (`nist-ssdf-1-1`) | The playbook's evidence checklist links each bug to the PR that introduced it and notes how review might have caught it; the SSDF asks for root-cause analysis of vulnerabilities and for eradicating the class, which takes that record further |
| OWASP ASVS 5.0 (`owasp-asvs-5-0`) | The playbook's security non-functional requirements and security test plan name authentication, authorisation and common web flaws only in outline; the ASVS supplies the verifiable requirements at a chosen level |
| DORA, AI-assisted software development (`dora-ai-assisted-swdev-2025`) | The playbook's small-PR guidance is a practice-level case for small batches; DORA reports working in small batches as a capability that amplifies AI's influence on product performance |
| He et al., Cursor velocity and complexity (`he-cursor-velocity-complexity-2025`) | He et al. report static-analysis warnings and complexity rising and staying after agent adoption; the playbook's maintainability requirements (complexity, coverage, churn with stated thresholds) are a way to set the alarm for that drift |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The playbook cites outside work that is not held in this corpus: an outside author's definitions of test doubles and mocks, outside blog posts behind its testing-pyramid figure and its claim that many teams write too many end-to-end tests, an outside article on the consumer-driven contract approach, an outside study for the estimate that a production bug costs about six times as much as one caught in implementation, outside principles of chaos experimentation, an outside security lifecycle's fuzzing requirement, an outside outage cited for blast radius, and outside guides on code review and inspection [BT]. This distillation uses none of them as evidence and does not name them.

**Named limits of the source.** The subset is partial by operator approval; the playbook's performance, UI, shadow and synthetic-monitoring testing pages, its CI/CD and observability sections, and its per-attribute non-functional requirement pages are not held, and links to them are not followed. The pages are practitioner guidance from one consulting organisation, written for human teams; they do not mention coding agents, and every mapping to an agent harness above is this projection's. Its numbers are recommendations, heuristics or illustrative thresholds (for example, more than 3 arguments as a complexity flag; 80% coverage as "commonly targeted" [V]), not measured results. The playbook carries an internal tension on whether business logic may be tested in integration tests (see What to Look For). The source does not speak to agent sandboxing, agent permissions, untrusted input or dependency provenance (Phase 4).

**Evidence-marker continuity.** Every quotation marked `[V]` here is copied from a `[V]` passage in the Pass I-stamped deep reference, including the two worked-example blockquotes. The playbook's recommendations keep their `[AP]` marking as the playbook's own assertions; worked-example details keep `[AE]`. The deep reference carries more verbatim passages than this file uses; the rest are paraphrased with their file-and-heading citation. Short citations in the tables give the file name and heading; the full path is in the deep reference's structure block.

## Runtime triggers this source addresses

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| The story's acceptance criteria are prose ("works well", "handles errors") with no runnable check | Test cases defined from the acceptance criteria while the story is designed; clarify ambiguities with the product owner; Given-When-Then form (test-planning.md, "Building test cases for a user story"); Ready means measurable criteria (definition-of-ready.md) | Block the build until each criterion is a planned test case with an expected result. Writing the cases is how the vague criteria get clarified, not a step after it. |
| The agent is asked to "build X like Y" with no statement of what must not change | Non-functional requirements stated as quantitative, measurable and testable, each with a metric, verification method and owner (non-functional-requirements-capture-guide.md); area-regression plans check that a change in one area has not affected others (test-planning.md, "Common Test Plans") | Ask which quality attributes this change must hold, and write each as a number with a check. Then name the regression plan that proves nothing else moved. |
| Nobody can say who will use the change or what they will do with it | Ready stories address a business need (definition-of-ready.md); end-to-end cases are designed from the end user's perspective (testing-methods.md, "E2E Test Cases Design Guidelines") | Send it back as not Ready: without a user and a business need, no end-to-end case can be written for it. |
| The spec is long and the change is large | Small PRs with one reason to change; break into self-contained changes that add value or release hidden features (pull-requests.md, "Best Practices"); Ready stories are small enough to finish in a short time (definition-of-ready.md) | Split it before the agent starts: each slice should be a change one reviewer can read in full. |
| The builder says "the agent will figure out the details" | Ready requires the details and input values the work needs, and an unready story is more likely to finish undone (definition-of-ready.md, "Definition of Ready") | The details the agent fills in unseen are the ones nobody will test. Write the input values and acceptance criteria first. |
| The diff touches login, sessions, tokens or permissions | Security test plan covers authentication and authorisation (test-planning.md, "Other Test Plan Examples"); the reviewer's functionality pass looks for security flaws (reviewer-guidance.md, "Code Quality Pass") | Route to a reviewer who runs the security pass, and require the security test plan's cases for this flow; take the requirement level from the ASVS. |
| The change stores or moves personal data | Reviewer checks for names revealing customer information and correct handling of PII, including logging (reviewer-guidance.md, "Code Quality Pass"); privacy is a named non-functional requirement (non-functional-requirements-capture-guide.md) | Require the reviewer to check every log line and identifier the change adds for personal data before it merges. |
| A migration, a delete or a bulk update is in the plan | The PR template asks whether the change is breaking, its impact and migration path (pull-request-template.md); a recovery test plan checks data integrity after failure (test-planning.md) | Require the PR to declare the change breaking with a migration path, and a recovery test that checks the data afterwards. The rehearsed rollback stays a harness rule. |
| The change is business-critical, or complex enough that nobody can predict its effects | Prioritise test cases by risk; automate hot paths and critical areas (test-planning.md); test the most critical transactions vertically, layer by layer (testing-methods.md, "Vertical Test") | Spend the testing where failure costs most: the critical transactions get end-to-end, layer-by-layer cases before sign-off. |
| The agent proposes changing a test so the build goes green | Tests tied to the implementation lose their meaning as a safety signal (mocking.md, "Mocks"); a unit test's failure should indicate a bug in the code (unit-testing/README.md, "Unit Testing") | Block. A failing test is reporting a bug until a changed requirement says otherwise. |
| The tests were written by the same agent session after the code | Write tests early; test-driven development writes the test first from a behaviour list (automated-testing/README.md, "The Fundamentals"; unit-testing/README.md, "Test-Driven Development") | Treat after-the-fact tests as a description of what the code does, not of what it should do. Check them against the planned cases. |
| A test checks the agent's output text rather than the system's state | Assert on the logic, not on values the double returned; prefer state verification (mocking.md, "Assertions"; "Mocks") | Ask what the test would do if the logic were wrong. If it would still pass, it is not evidence. |
| The suite passes, but nobody knows whether it would catch a wrong implementation | A suite at 100% coverage still missed a bug until intended-behaviour tests were added (authoring-example.md, "Fixing the Bug") | Coverage says the lines ran. Ask which inputs the tests state as intended behaviour, and add the negative cases. |
| The suite takes minutes, so it runs rarely | A unit suite should take no more than a couple of seconds; slow tests belong in the outer loop at the PR stage or later; sleeps and disk reads are what slow them (unit-testing/README.md; why-unit-tests.md, "Speed Up Development") | Make the unit suite fast enough to run on every change, and move the slow tests to the PR gate rather than dropping them. |
| "It worked first time", or a flaky check passed on retry | A unit test should be 100% reliable; find the cause of flakiness and remove it (unit-testing/README.md, "Unit Testing"; "Things to Avoid") | One pass, or a pass on retry, says the test can be flaky. Fix the cause before the pass counts. |
| A gate was skipped "just this once" | Merging is blocked when tests fail; PR requirements should be enforced by policies (automated-testing/README.md, "The Fundamentals"; pull-requests.md, "Pull Requests") | Put the gate in branch policy so a skip needs an override someone can see. Record the override on the ledger. |
| Lint and type errors are suppressed rather than fixed | Code should compile and run without errors or warnings, with no new lint findings; automation takes the mechanical checks so review goes to the logic (pull-requests.md, "General Process"; pull-request-template.md; process-guidance/README.md, "Automate Whenever Reasonable") | Hold the change to no new errors or warnings. A suppression added in the same diff is a finding for the reviewer (a harness rule). |
| A performance number moved and nobody set a budget | Performance requirements as measurable targets with a verification method (non-functional-requirements-capture-guide.md, "Template"; "Performance Requirements"); log performance metrics (automated-testing/README.md, "Build for Testing") | Write the target and its check before judging the change. A number with no target cannot fail. |
| The same session that wrote the code reviews it | "Someone outside the pair should perform the code review." [V] (faq.md, "We Pair or Mob. How Should This Reflect in our Code Reviews?") | Route to a reviewer who did not take part in writing the change. The writer's view is the one review exists to check. |
| The reviewer's findings are long and nobody sorts them | Each comment is resolved or marked "won't fix" with reasons; in-scope work is not deferred; out-of-scope concerns become new work items (author-guidance.md; reviewer-guidance.md) | Every finding gets one of three outcomes: fixed, "won't fix" with a reason, or a new work item. None stays open at sign-off. |
| The builder approves because reading the diff is too slow | Reviewers read every changed line; review effectiveness falls with size, so PRs stay small; automation handles the mechanical checks (reviewer-guidance.md; process-guidance/README.md) | If the diff is too big to read, it is too big to approve: split it. Automation clears the style so reading goes to the logic and the tests. |
| The reviewer and builder agree too quickly | Assuming one developer's code is always good and not reviewing it properly is named as biased decision-making (inclusion-in-code-review.md) | Ask whether the change was reviewed or its author was trusted. Review the code, not the record. |
| The change "looks fine" but touches something with a history of incidents | Each bug is linked to the PR that introduced it, with a note on how review might have caught it; review checklists are updated with common issues (evidence-and-measures/README.md, "Evidence") | Pull the linked bug history for this area first, and review against the checklist items it produced. |
| The pack says "all tests pass" with no run record | The PR template pairs the checklist with test sets used, scenarios tried and relevant logs (pull-request-template.md) | A tick is a claim. Send it back for the test sets, scenarios and logs; requiring a run record is a harness rule. |
| A risk is listed with no owner and no rollback | Each non-functional requirement records an owner and a verification method (non-functional-requirements-capture-guide.md, "Template") | Give the risk an owner and a check before sign-off. |
| The client wants it today and the review is still open | Code review complete is a Definition of Done item; out-of-scope issues should not block the PR (definition-of-done.md; reviewer-guidance.md, "Take Your Time and Keep Focus on Scope") | Separate the open findings: in-scope ones block the change, out-of-scope ones become work items and do not. Ship only when the in-scope list is empty. |
| Nobody could explain how this part works if the agent were unavailable | Shared understanding is one of review's three goals; adding a less familiar reviewer spreads expertise; documentation updated is a done item (code-reviews/README.md, "Goals"; author-guidance.md, "Add Relevant Reviewers"; definition-of-done.md) | Add a reviewer who must come away able to explain the change, and check the documentation is updated before sign-off. |
| The release goes straight to everyone | Smoke tests gate deployments and let the chain be abandoned on failure; canary and blue/green deployments and a blast-radius check for live experiments (smoke-testing/README.md; fault-injection-testing/README.md, "Best Practices and Advice") | Put a smoke gate after each deployment stage with a stop on failure. A staged rollout is a harness rule; the playbook's canary advice is written for fault-injection experiments. |
| There is no service-level target, so every alert is urgent | Availability stated as uptime with allowed downtime; a service level objective as the budget for experiments (non-functional-requirements-capture-guide.md, "Operational Requirements"; fault-injection-testing/README.md) | Write the availability target first; it decides which alerts can wait. |
| Warnings and code complexity climb release after release | Maintainability requirements with metrics and example thresholds for complexity, coverage and churn (non-functional-requirements-capture-guide.md, "System Maintainability Requirements") | Set a threshold for each and check it on every release, so drift fails a check instead of going unseen. |
| Something went wrong after release | Regression and acceptance tests written from fixed issues and resolved incidents; full regression includes every fixed bug; bugs linked to the introducing PR (fault-injection-testing/README.md; test-planning.md; evidence-and-measures/README.md) | The fix is not done until it is a regression test in the full plan and the bug is linked to the change that introduced it. |

## Trigger extensions surfaced by this source

| Phase | Trigger (proposed) | Response |
|---|---|---|
| 3. Locking the tests | A test sleeps, reads an expected value from disk or calls a live third-party API | Block: each breaks the speed, isolation or reliability a unit test needs; wrap the dependency and replace the sleep with a reliable state signal (unit-testing/README.md, "Things to Avoid") |
| 3. Locking the tests | The tests verify the exact sequence of calls the implementation makes | Flag: behavioural verification ties the test to the implementation, so the next refactor will break it and invite an edit to the test (mocking.md, "Mocks"); prefer state checks or fakes |
| 4. Building in the sandbox | The agent proposes running tests or experiments against the live production system | Block until the blast radius is weighed; integration tests run in a scaled-down copy environment, and fault injection starts outside production (integration-testing/README.md, "Things to Avoid"; fault-injection-testing/README.md, "Best Practices and Advice") |
| 5. Gating deterministically | Code arrives with tests promised for a later PR | Block: tests are committed in the same PR as the code (reviewer-guidance.md, "Code Quality Pass") |
| 6. Reviewing independently | A finding outside the change's scope is holding up the merge, or an in-scope finding is answered "later" | Move out-of-scope findings to new work items; resolve in-scope ones now (reviewer-guidance.md, "Take Your Time and Keep Focus on Scope"; author-guidance.md, "Be Open to Receive Feedback") |
| 8. Releasing and operating | The change ships with no diagnostics, and a failure cannot be traced across services | Require the Definition of Done's diagnostics and telemetry item: parameters logged at startup, correlation IDs across systems (definition-of-done.md; automated-testing/README.md, "Build for Testing") |
| 8. Releasing and operating | A bug is fixed with no regression test and no link to the change that introduced it | Return the fix: add the regression test to the full-regression plan and link the bug to its PR (test-planning.md, "Common Test Plans"; evidence-and-measures/README.md, "Evidence") |
