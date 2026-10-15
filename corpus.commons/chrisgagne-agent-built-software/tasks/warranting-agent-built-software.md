---
name: Warranting agent-built software
slug: warranting-agent-built-software
corpus: chrisgagne-agent-built-software
created: 2026-10-14
status: scoped — DRAFT pending operator review
---

# Warranting agent-built software

**Slug:** `warranting-agent-built-software`
**Purpose:** Help the person accountable for software that coding agents built decide, change by change, whether it is safe to put in front of someone who depends on it, what evidence is still missing, and what the harness must do to produce that evidence, when nobody reads every line.

## 1. Problem statement

Coding agents now write most of the code, faster than anyone can read it. The builder no longer reviews the code line by line; they rely on the harness around the agent: the spec, the tests, the gates, the reviewers, the release path. So the warranty a builder gives a client (this is fit to ship; I stand behind it) lives in the harness, and the harness itself has to be warranted. The job is to decide, at each stage of a change's life (specifying it, sorting its risk, locking its tests, building it, gating it, reviewing it, signing it off, releasing and operating it), what has been *shown* rather than *asserted*, what the change can break that cannot be undone, and whether the evidence on the ledger is enough to sign. The circumstance: a small builder or team using agents to ship software for a client who cannot judge its quality, where the builder carries the liability (contract, insurer, reputation), the change may touch customer data, money or production infrastructure, and success so far is tempting everyone to stop checking. The practitioner is the accountable builder, and the harness's reviewer agents that act for them at each gate.

## 2. Practitioner questions

- Is "correct" for this change written down somewhere a machine can check, or only in the agent's summary?
- What does this change touch (auth, personal data, money, migrations, infrastructure, prompts and tools an agent will use), and which gates does that make mandatory?
- What is the worst irreversible thing the agent can do from where it is running, and what stops it?
- Which claims about this build were demonstrated (a test ran and passed, a scan ran clean) and which are only asserted ("all tests pass", "done")?
- Did the agent change a test, a fixture or a threshold to make something pass?
- Has a run of past successes become our evidence that this change is safe?
- Who could explain how this part works once the agent session ends, and where is it written?
- What would make me refuse to sign this off, and is any of it on the ledger?
- What will degrade quietly over the next year (warnings, complexity, dependencies, drift between docs and code), and what alarm catches it?
- How do I know the harness itself still catches what it claims to catch?

## 2a. Runtime listener grain

**Trigger unit:** an observable signal at a gate: a phrase in the builder's or the agent's own words ("the agent says it's done", "it worked first time", "skip permissions, it's been fine"); an agent behaviour in the session log (edits a test, adds a dependency, runs a destructive command, reports done without running anything); a feature of the diff (touches auth, a migration, a secret, a prompt or tool definition); a gap in the change's ledger (no acceptance check, a skipped gate, an unresolved review finding); or a production signal (warnings or complexity climbing, an alert nobody owns).

**Response unit:** a gate action (block, require evidence X, route to reviewer Y, ask the accountable human Z) with the grounded reason for it, cited to the source passage that warrants it, and a one-line teach the builder can carry to the next change.

### Seed trigger→response table

These are seeds. Pass G decides, per source, which triggers each distillation can actually address; a response below names where to look, not a verified claim. Where a response is a harness rule that no source in this corpus states, it says so.

**Phase 1: Specifying the change**

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| The story's acceptance criteria are prose ("works well", "handles errors") with no runnable check | Block the build until each criterion is an executable check: concrete examples as the specification, automated as acceptance tests before the code (`cucumber-bdd-gherkin`); test cases planned from the acceptance criteria while the story is designed (`microsoft-code-with-engineering-playbook`) |
| The agent is asked to "build X like Y" with no statement of what must not change | Ask what must not change: capture the non-functional requirements as measurable statements (`microsoft-code-with-engineering-playbook`), and the security requirements at a stated level (`owasp-asvs-5-0`). Stating non-goals is a harness rule |
| Nobody can say who will use the change or what they will do with it | Discover it with the people who know the domain before formulating anything: who writes and who reviews the examples (`cucumber-bdd-gherkin`); engagement and scoping with the commissioner (`uk-aqua-book-2025`) |
| The spec is long and the change is large | Slice it into small changes a reviewer can follow (`microsoft-code-with-engineering-playbook`); working in small batches (`dora-ai-assisted-swdev-2025`) |
| The builder says "the agent will figure out the details" | Name what the agent will decide unseen: a model rewarded for answering guesses rather than abstains (`why-language-models-hallucinate-kalai`); how much an agent's tests depend on the detail of the specification it was given (`egashira-testsuitebench-2026`) |

**Phase 2: Triaging risk**

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| The diff touches login, sessions, tokens or permissions | Require the matching ASVS chapters at the level the client's data warrants (`owasp-asvs-5-0`) |
| The change stores or moves personal data | ASVS data-protection requirements plus a privacy check with local law in view, and documentation- or source-led (hybrid) security testing rather than black-box testing alone (`owasp-asvs-5-0`) |
| The change adds an LLM call, a prompt, a tool an agent can call, or memory | Check the LLM and agentic threat lists for the feature's shape (`owasp-llm-top10-2026`, `owasp-agentic-top10-2026`, `owasp-agentic-threats-mitigations`, `nist-sp-800-218a`) |
| A migration, a delete or a bulk update is in the plan | Classify as irreversible; a human approves high-impact actions, and the gate sits outside the AI's own instructions (`owasp-agentic-threats-mitigations`, `openssf-finding-fixing-vulnerabilities-ai`). A rehearsed rollback and restore test is a harness rule |
| The change is business-critical, or complex enough that nobody can predict its effects | Scale the assurance to the risk and the complexity (`uk-aqua-book-2025`, `uk-duck-book-qa-of-code`) |

**Phase 3: Locking the tests**

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| The agent proposes changing a test so the build goes green | Block; success is judged by tests the agent did not write (`jimenez-swe-bench`), and a finding becomes a durable check rather than a preference the AI can move (`openssf-finding-fixing-vulnerabilities-ai`). Locking the tests and recording a human's reason for any revision are harness rules |
| The tests were written by the same agent session after the code | Treat as asserted, not demonstrated; agents' test suites from specifications miss much of the intended behaviour (`egashira-testsuitebench-2026`); write the tests before the logic (`uk-duck-book-qa-of-code`, `cucumber-bdd-gherkin`) |
| A test checks the agent's output text rather than the system's state | Judge the outcome by running the tests against the changed code, not by reading the agent's report (`jimenez-swe-bench`) |
| The suite passes, but nobody knows whether it would catch a wrong implementation | Measure the suite's strength against seeded faults, one requirement at a time (`egashira-testsuitebench-2026`) |
| The suite takes minutes, so it runs rarely | Run all the tests on every change, automatically (`uk-duck-book-qa-of-code`, `microsoft-code-with-engineering-playbook`) |

**Phase 4: Building in the sandbox**

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| "Skip permissions, it's been fine for months" | Keep the sandbox: isolation scales with what the agent can do, and excessive agency is a named risk (`openssf-finding-fixing-vulnerabilities-ai`, `owasp-agentic-top10-2026`, `owasp-llm-top10-2026`) |
| The agent's environment can reach production credentials or data | Remove the reach, not just the intent; privilege and confused-deputy threats (`owasp-agentic-threats-mitigations`, `owasp-agentic-top10-2026`) |
| The agent reads untrusted content (web pages, issues, emails) while holding tools | Indirect prompt injection; separate reading from acting (`owasp-llm-top10-2026`, `owasp-agentic-threats-mitigations`) |
| The agent adds a dependency nobody asked for | Supply-chain check before accepting (`nist-ssdf-1-1`, `nist-sp-800-218a`, `owasp-llm-top10-2026`) |
| The agent runs for an hour unattended and reports success | A report of success is a claim: confident output is no evidence of correctness (`why-language-models-hallucinate-kalai`), and AI results vary from run to run, so check the evidence (`openssf-finding-fixing-vulnerabilities-ai`) |

**Phase 5: Gating deterministically**

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| "It worked first time", or a flaky check passed on retry | One success isn't evidence: tests are repeatable and reproducible (`uk-duck-book-qa-of-code`), and an AI run repeated gives different results (`openssf-finding-fixing-vulnerabilities-ai`) |
| A gate was skipped "just this once" | Log it as a deviation and make the skip visible on the warranty pack; an attestation covers the practices as performed (`cisa-secure-software-attestation-form`, `nist-ssdf-1-1`) |
| The pipeline builds different artefacts for test and for production | Protect the integrity and provenance of what ships (`nist-ssdf-1-1`). Building once and promoting the same artefact is a harness rule |
| Lint and type errors are suppressed rather than fixed | Treat suppressions as findings for review, not passes (a harness rule); automate the style checks so human review goes to the logic (`microsoft-code-with-engineering-playbook`) |
| A performance number moved and nobody set a budget | State the performance requirement as a measurable target and check the change against it (`microsoft-code-with-engineering-playbook`) |
| The secrets scan or dependency audit is "noisy" so it was turned off | Tune it, don't drop it: triage, deduplicate and validate the findings (`openssf-finding-fixing-vulnerabilities-ai`) |

**Phase 6: Reviewing independently**

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| The same session that wrote the code reviews it | Require a reviewer outside the writing session: the assurer is independent of the analyst (`uk-aqua-book-2025`), and agents don't approve each other's changes (`openssf-finding-fixing-vulnerabilities-ai`). A second model family is a harness rule, backed by the factory's own audit record rather than a corpus source |
| The reviewer's findings are long and nobody sorts them | Sort into confirmed, disputed and noise; unresolved findings block the pack (a harness rule); validate and deduplicate findings before acting on them (`openssf-finding-fixing-vulnerabilities-ai`) |
| The builder approves because reading the diff is too slow | Confidence need not come from reading the code: it comes from the team's approach, proportionate QA and checks on the outputs (`uk-duck-book-qa-of-code`); assure a black-box system by its inputs and outputs (`uk-aqua-book-2025`) |
| The reviewer and builder agree too quickly | Ask what each would need to see to change their mind (a harness rule); humans review the fix as well as the AI (`openssf-finding-fixing-vulnerabilities-ai`) |
| The change "looks fine" but touches something with a history of incidents | Pull the history first: analyse past vulnerabilities for their root causes and the classes they belong to (`nist-ssdf-1-1`) |

**Phase 7: Warranting the change**

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| The pack says "all tests pass" with no run record | Asserted, not demonstrated; send it back for the run record (a harness rule) |
| A risk is listed with no owner and no rollback | Don't sign: the approver reviews the assurance evidence and signs off on the stated assurance state (`uk-aqua-book-2025`) |
| The client wants it today and the review is still open | Name the trade-off aloud: what skipping tests risks in a time crunch (`uk-duck-book-qa-of-code`), and assurance proportionate to the risk (`uk-aqua-book-2025`) |
| Nobody could explain how this part works if the agent were unavailable | Don't sign yet: the person who submits AI-written code is the one responsible for it (`uk-duck-book-qa-of-code`). Naming a human who holds the theory of this area is a harness rule |
| The builder signs because the last ten went fine | Felt speed and measured speed part ways (`becker-metr-ai-developer-productivity-2025`); early velocity gains fade while added complexity stays (`he-cursor-velocity-complexity-2025`) |

**Phase 8: Releasing and operating**

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| The release goes straight to everyone | Release and deploy with a human gate and a way to stop (`openssf-finding-fixing-vulnerabilities-ai`). A staged rollout with a stop condition is a harness rule |
| There is no service-level target, so every alert is urgent | State availability and performance as measurable requirements (`microsoft-code-with-engineering-playbook`) |
| Warnings and code complexity climb release after release | Track them: in projects adopting an agentic coding tool, velocity gains were transient while static-analysis warnings and complexity rose and stayed (`he-cursor-velocity-complexity-2025`) |
| Throughput rose with AI assistance and so did instability | Look at delivery stability alongside speed (`dora-ai-assisted-swdev-2025`) |
| Something went wrong after release | Find the root cause, fix the class rather than the instance, and turn it into a durable check (`nist-ssdf-1-1`, `openssf-finding-fixing-vulnerabilities-ai`) |

## 3. Available sources

All open or open-nc; Pass G makes the binding call on each.

- Standards and threat lists: `nist-ssdf-1-1`, `nist-sp-800-218a`, `cisa-secure-software-attestation-form`, `owasp-asvs-5-0`, `owasp-llm-top10-2026`, `owasp-agentic-top10-2026`, `owasp-agentic-threats-mitigations`.
- Evidence on AI-assisted development: `becker-metr-ai-developer-productivity-2025`, `he-cursor-velocity-complexity-2025`, `jimenez-swe-bench`, `why-language-models-hallucinate-kalai`, `dora-ai-assisted-swdev-2025`, `egashira-testsuitebench-2026`.
- Practice and assurance guidance: `cucumber-bdd-gherkin`, `microsoft-code-with-engineering-playbook`, `uk-duck-book-qa-of-code`, `uk-aqua-book-2025`, `openssf-finding-fixing-vulnerabilities-ai`.

## 4. Intended lenses

None.

## 4a. Intended runtime agents

- `independent-reviewer`: reviews one change from a fresh context against the change's ledger and this axis's phase distillations; read-only tools; never the session that built the change; refuses to pass a change on the builder's or agent's assertions alone.
- `warranty-assessor`: assembles the warranty pack from the ledger, separating demonstrated from asserted; writes nothing the ledger does not record; hands the sign-or-return decision to the accountable human and never makes it.

## 5. Overlap

None in this corpus. Learning from an incident after release is a separate job; Phase 8 stops at finding the root cause and turning it into a durable check.

## 6. Success criteria

By 2027-01-31: (a) on the factory's seeded-defect calibration fixtures, a reviewer that consults this axis catches more of the planted defects than the same reviewer without it, on the same changes; (b) at least ten real changes have shipped through the factory with a warranty pack the accountable human signed after reading the pack, not the diff; (c) no post-release incident in that period traces to a gate the pack recorded as passed without a run record. If (a) shows no difference, the axis is shelf material and the gates carry the warranty on their own.

## Discipline

- **Verb-and-noun.** *Warranting* (verb) *agent-built software* (noun phrase).
- **Job × circumstance.** A change built by agents, for a client who can't judge it, where the builder carries the liability.
- **Hire requires fire.** This axis fires three reflexes: "the agent says it's done" (assertion taken as evidence), "it worked first time" (success taken as safety), and "I read the diff" (line-by-line human review as the safety mechanism, which cannot keep pace with agent output).
- **Phases route from practitioner questions.** The eight phases are the stages of a change's life in the harness, not the chapters of any source.
- **Runtime listener grain.** Triggers are signals at a gate (words, agent behaviour, diff features, ledger gaps, production signals); responses are gate actions with grounded reasons.
- **Runtime agents.** Two: the independent reviewer and the warranty assessor.
- **Open sources only.** Every source this axis cites is open or open-nc. A response no source here supports is labelled a harness rule, not given a borrowed citation.
