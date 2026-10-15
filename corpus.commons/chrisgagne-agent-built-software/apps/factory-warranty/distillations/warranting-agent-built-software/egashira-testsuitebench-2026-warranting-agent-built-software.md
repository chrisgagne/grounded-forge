
# Egashira et al., TestSuiteBench, Warranting Agent-Built Software Distillation

**Source:** Egashira, Mündler-Sasahara, Müller and Vechev (ETH Zurich; LogicStar.ai), *TestSuiteBench: Coding Agents Struggle to Generate Strong Test Suites from Specifications*, preprint, arXiv:2610.13065v1 [cs.SE], 9 Oct 2026. Licence: CC BY 4.0. Scope: open.

**Applicability gate (Pass G.0): clear yes.** (1) The source answers practitioner questions this axis asks directly: which claims about a build were demonstrated and which only asserted, whether "correct" is written down where a machine can check it, and how to know the harness still catches what it claims to catch. (2) Its concepts land naturally in six of the eight phases. (3) Its contrarian position, that valid tests are not strong tests, is the axis's first reflex ("the agent says it's done", "all tests pass") stated as a measured gap.

**Phase mapping.** Primary: Phase 3, Locking the tests. Secondary: Phase 1, Specifying the change (how much the specification's detail governs test strength); Phase 7, Warranting the change (a passing agent-written suite is weak evidence). Supporting: Phase 4, Building in the sandbox (an agent's own green tests after a long run); Phase 5, Gating deterministically (calibrating a test gate against planted faults; dropping tests that change across runs before counting); Phase 6, Reviewing independently (what a reviewer of a test suite looks for; what a second agent adds). No rows: Phase 2, Triaging risk (the source sorts no change by what it touches or what it can break) and Phase 8, Releasing and operating (the source stops before release).

**Transfer caveat.** The benchmark measured agents writing a test suite from a natural-language specification alone, with no implementation given, on command-line programs in compiled languages, against specifications far more detailed than typical developer documentation. It did not measure the factory's usual case, an agent writing tests in the same session as the code. Where this distillation carries a finding into that case, it says the step is its own inference.

## Warranting Agent-Built Software Relevance

This source puts a number on the gap between "the tests pass" and "the tests would catch a wrong build", which is the gap a builder warranting agent-built software has to see across. Agents on six frontier models wrote tests that mostly pass on a correct implementation (validity 88-96% for four of six) while their suites killed at most 55.5% of planted single-requirement faults, and four of six killed under 40% (Source: Egashira et al., TestSuiteBench, §3.1, "Main Results"; Table 2) [AE]. For a builder whose warranty rests on the harness rather than on reading the code, that turns "the suite is green" from evidence into a claim to be tested: a green agent-written suite shows the tests agree with the code, not that they would notice the code being wrong.

The source also brings a method the harness can borrow: score a suite by how many requirement-targeted faults it kills, with each fault built to break one requirement and be caught by one reference test (Source: Egashira et al., TestSuiteBench, §2.2, "Mutant Construction"; §2.6, "Evaluation Metrics") [AP]. And it maps where agent suites fall short (too few tests, one input where several are needed, assertions on the shape of the output rather than its content) and what does not close the gap (more ambiguity removed, the running program supplied, more agents pooled), which gives the independent reviewer and the warranty assessor specific things to look for. Its numbers keep their conditions: preprint, mutants as a proxy for real faults, detailed specifications, compiled command-line programs.

## Key Concepts for Warranting Agent-Built Software

1.  **The verification gap.** Agents can implement specifications they cannot test: their implementations pass up to 93% of reference tests while their suites kill just over half the mutants at best (Source: Egashira et al., TestSuiteBench, §1, "Introduction"; §6, "Conclusion") [AR]. New software has no existing test suite or reference implementation to verify against, so the agent's own tests carry the verification (§1, "Introduction") [AR]. For the warranty, the evidence the agent produces about its own work is the weakest link.

2.  **Mutation score as test strength.** M is the share of planted faulty versions (mutants) that a suite's valid tests make fail; tests that fail on the correct reference are filtered out first, and suites run three times on the reference with tests that change behaviour removed (Source: Egashira et al., TestSuiteBench, §2.6, "Evaluation Metrics") [AP]. The target is a suite that passes the reference and kills every mutant: "A high quality test suite never kills the reference executable" (§2, "Notation") [V].

3.  **Valid but weak tests.** Validity V is the share of generated tests that pass on the correct reference; it ran 88-96% for four agents while M ran 38-56% (Source: Egashira et al., TestSuiteBench, §3.1, "Valid but Weak Tests") [AE]. The authors read the gap as tests that look like thorough testing but do not surface violations of the specification [AR].

4.  **Requirement-targeted mutants.** Each mutant is built to break one requirement and be caught by one chosen reference test; targets spread evenly over the specification's sections, and refinement raised exact single-test kills from 32.4% to 73.0% (Source: Egashira et al., TestSuiteBench, §2.2, "Candidate Construction", "Candidate Refinement"; App. B.2) [AE]. The construction prompt asks for a rule a re-implementer could plausibly get wrong across a class of inputs, not a fault tied to a literal value (App. D.1, "Mutant-suite initialization prompt") [AP]. Without the logic-level instruction, the mutating agent copied concrete values from the target test into the mutant (App. A.5, "Realism of the Mutation") [AE].

5.  **Specification detail governs test strength.** On 30 instances, generating tests from developer documentation instead of the benchmark's detailed specification cut GPT 5.6 Sol's M from 25.5% to 4.0%, with 40% fewer tests, lower validity and three times the underspecification failures per test (Source: Egashira et al., TestSuiteBench, §3.2, "Comparison with Developer-Written Documentation"; Table 5) [AE]. The authors found developer documentation "severely underspecified and thus unsuitable for test generation" (§2.1, "Generating a Draft Specification") [V].

6.  **Test design, not specification clarity, is the bottleneck.** Given the reference executable as well as the specification, Sol's validity rose from 94.4% to 98.4% but its M stayed at 38.1% against 37.7% (Source: Egashira et al., TestSuiteBench, §3.2, "Providing Reference Executables for Test Generation"; Table 4) [AE]. The ablation ran on Sol only (Table 4 caption) [AP].

7.  **Core behaviour tested, combinations left out.** The commonest miss is a suite that tests a feature with one input where the requirement needs several: a search command tested on one file misses a fault that ignores the second; a completion test that checks only that output is long and names commands passes a script for the wrong shell (Source: Egashira et al., TestSuiteBench, §3.2, "Error Analysis"; Figure 7; App. A.6) [AE].

8.  **Suites too small for the requirements.** Every model wrote smaller suites than the reference, Opus by 8.9% and Sol by about five times, and M was better where agents wrote more tests and where there were fewer requirements to cover (Source: Egashira et al., TestSuiteBench, §3.2, "Model Test Suites are (Too) Small"; Figure 6a) [AE]. The authors argue a high M needs every requirement covered, which generally takes many tests [AR].

9.  **Larger specifications, weaker suites (weakly).** M correlates negatively with the number of specification sections (Opus ρ = −0.16, Sol ρ = −0.42), a correlation the appendix calls weak across the four plotted agents (Source: Egashira et al., TestSuiteBench, §3.2, "Agents Struggle with Large Specifications"; App. A.2) [AE].

10.  **Spending buys little strength.** Cost and M have a logarithmic relationship, with increased cost giving marginal gains; Sol's M rises from 31.3% at low reasoning effort to 46.5% at xhigh, and the best agent costs $10.56 per instance for 55.5% (Source: Egashira et al., TestSuiteBench, §3.1, "Cost-Strength Tradeoff", "Reasoning Effort"; Figure 5 caption; Table 2) [AE].

11.  **More agents, modest gains.** Pooling the suites of Opus, Sol and Gemini raises the killed share from 54% (Opus alone) to 59%, leaving 41% that none kills; only 25% are killed by all three (Source: Egashira et al., TestSuiteBench, App. A.5, "Overlap of Killed Mutants") [AE].

12.  **Attributing a failure to the specification or the generation.** The construction loop classifies each failure (reference test failing the generated implementation, generated test failing the reference, mutant surviving the suite) as a bad generation or a specification defect, underspecification or contradiction, and fixes the specification until under 5% of generated-test failures are blamed on it (Source: Egashira et al., TestSuiteBench, §2.3, "Error Attribution", "Specification Refinement") [AP]. A claimed contradiction must quote the specification sentence exactly or the verdict is discarded (App. D.1) [AP].

## Questions to Ask During Warranting Agent-Built Software

### Phase 1: Specifying the change

| Need | Question | Source-tag |
|---|---|---|
| Know whether the spec can carry the tests | Does the spec describe each behaviour well enough that someone could build to it and test it without anything outside it, or is it developer-style documentation that left Sol's tests at 4.0% M? | §2.1; Table 5 |
| Find where the agent will decide unseen | Which behaviours does the spec leave to inference, and which of them would a test need an input combination to check? | §3.2, "Error Analysis" |
| Size the change for test strength | How many separate requirements does this change carry, and is the spec large enough that test strength is likely to drop (a weak trend, strongest for Sol)? | §3.2, "Agents Struggle with Large Specifications" |
| Fix the spec or the agent | When an agent's output fails, is the failure the generation's fault or a gap or contradiction in the spec, and can the claimed contradiction be quoted from the spec word for word? | §2.3; App. D.1 |

### Phase 3: Locking the tests

| Need | Question | Source-tag |
|---|---|---|
| Separate validity from strength | Do we know only that these tests pass on the build, or have we measured whether they fail on a build that breaks a requirement? | §2.6; §3.1 |
| Check coverage of the spec | Is there at least one test per documented behaviour, and is the suite anywhere near the size the requirements need? | §3.2, "Model Test Suites are (Too) Small"; App. D.2 |
| Check input combinations | For each feature, does a test use the combinations the requirement names (two files, not one; the all-bold flag, not a neighbouring flag)? | §3.2; App. A.6 |
| Check assertions | Does each test assert the content the requirement fixes, or only the shape of the output (length, presence of a keyword)? | App. A.6 |
| Weigh the fixes on offer | Is the proposed fix (run the program, raise reasoning effort, add another agent) one the source found moves test strength, or one it found barely moves it? | Table 4; §3.1; App. A.5 |

### Phase 4: Building in the sandbox

| Need | Question | Source-tag |
|---|---|---|
| Read an agent's report of success | Does "done" rest on tests the agent wrote, and if so, what do we know about whether those tests would catch a wrong build? | §3.1, "Valid but Weak Tests" |

### Phase 5: Gating deterministically

| Need | Question | Source-tag |
|---|---|---|
| Know the gate still catches faults | When did we last run the test gate against faults planted one requirement at a time, and what share did it catch? | §2.2; §2.6 |
| Keep the measure clean | Before counting what a suite catches, have we dropped tests that fail on the correct build and tests that change result across repeated runs? | §2.6 |
| Keep planted faults honest | If an agent seeds the faults, did it break a rule across a class of inputs, or did it copy the test's literal values so only that test can see the fault? | App. A.5; App. D.1 |

### Phase 6: Reviewing independently

| Need | Question | Source-tag |
|---|---|---|
| Review the tests, not just the code | Has the reviewer read the suite for missing combinations, loose assertions and missing behaviours, rather than checking that tests exist and pass? | §3.2; App. A.6 |
| Judge a second agent's tests | Will another agent's suite find what the first missed, given that three agents pooled added only five points? | App. A.5 |

### Phase 7: Warranting the change

| Need | Question | Source-tag |
|---|---|---|
| Class the test evidence | Does the pack treat "the agent's suite passes" as demonstrated strength, when it shows only validity? | §3.1 |
| Find a strength measure on the ledger | Is there a recorded measure of what the suite catches (planted faults killed), with its conditions? | §2.6 |
| Name the limits of that measure | Does the pack say planted faults are a proxy and need not match the faults this change will meet in use? | §5 |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| Every test the agent wrote passes, and the pack cites that as the evidence | Validity read as strength; in the benchmark, high validity sat beside M of 38-56% (§3.1) [AE] | Ask for a strength measure: seed single-requirement faults and record how many the suite catches |
| The agent's suite has far fewer tests than the spec has behaviours | Suite-size shortfall; Sol's suites were about five times smaller than the reference (§3.2) [AE] | Count tests against documented behaviours; require at least one meaningful test per behaviour (the benchmark's own prompt asked this, App. D.2) [AP] |
| Each feature is tested once, with a default or single input | Input combinations omitted, the commonest miss in the error analysis (§3.2) [AE] | Ask, per requirement, which combination would expose a build that gets it wrong, and whether a test uses it |
| A test asserts length, non-emptiness or that a keyword appears | Shape-only assertion; the Elvish-completion test passed a script for the wrong shell (App. A.6) [AE] | Require the assertion to pin the content the requirement fixes |
| The fix proposed for weak tests is "give the agent the running program" or "use more agents" | Remedies the source measured as moving test strength little or modestly (Table 4; App. A.5) [AE] | Turn effort to test design: which requirements and combinations are untested |
| The spec is the project's README or developer docs | Underspecification; M fell from 25.5% to 4.0% on developer documentation (Table 5) [AE] | Rewrite the change's behaviour as a spec someone could build and test from without outside knowledge |
| Planted faults are each caught only by the test they were copied from | Literal-bound faults; the mutating agent copied test values unless told to break logic (App. A.5) [AE] | Instruct the seeding agent to break a rule across an input class, then check a sample by hand |

## When to Use This Reference

- Reach for it when the evidence for a change is an agent-written test suite and the question is how much that suite is worth. It is the corpus's measured account of agent-written test strength.
- Reach for it when designing or calibrating the harness's test gate: it supplies a construction for requirement-targeted planted faults and a clean scoring rule.
- Reach for it when someone proposes a cheap fix for weak agent tests (more effort, the running program, a second agent) and the team needs to know what was measured.
- Reach for it in Phase 1 when the spec is thin: it is the corpus's number for how far spec detail moves agent test strength.
- Reach for another source when the question is how to write good tests by hand (`uk-duck-book-qa-of-code`, `microsoft-code-with-engineering-playbook`, `cucumber-bdd-gherkin`), how agent code fares against tests it did not write (`jimenez-swe-bench`), or what a change touches and which gates that makes mandatory (the standards and threat lists). This source does not sort risk and does not cover release.

## Worked Example

*Scenario (operator-authored).* A two-person studio uses a coding agent to add an export command to a client's command-line reporting tool: the command writes selected records to CSV, can merge several input files, and must skip records flagged as deleted. The agent reports done after an hour; its 31 new tests all pass, and the draft warranty pack says "all tests pass, export feature complete". The independent reviewer reads the pack, not the diff.

*Applying the source.* The reviewer classes "all tests pass" as validity, not strength. The source's central result is that agents can write tests that pass while missing the faults they should catch:

> "While the models are capable of writing valid tests, giving the impression of well tested software, they fail to write discriminative tests that would actually surface specification violations." (Source: Egashira et al., TestSuiteBench, §3.1, "Valid but Weak Tests") [V]

The benchmark measured suites written from a spec with no implementation in hand; this agent wrote its tests in the same session as the code, a case the source did not measure. Treating its passing suite as no stronger is this distillation's inference, not the source's finding.

The reviewer checks the suite the way the error analysis reads one (Source: Egashira et al., TestSuiteBench, §3.2, "Error Analysis") [AE]. The merge behaviour is tested with one input file; the deleted-record rule is tested by one fixture where the only record is deleted, asserting that the output is empty. That is the pattern the authors report:

> "We observe this to be a common pattern where core functionality is tested but input combinations and edge cases are omitted from test suites" (Source: Egashira et al., TestSuiteBench, §3.2, "Error Analysis") [V]

The reviewer asks the harness to seed three faults, each breaking one rule across its input class rather than a literal value (the source's mutant discipline, App. D.1 and App. A.5) [AP]: merge reads only the first file; deleted records are skipped only when they come first; the CSV header is written once per input file. The suite kills one of the three. The ledger records the result with its conditions, and the reviewer sends the change back with three asks: tests for merge with two or more files, a mixed deleted-and-live fixture, and a header check on a multi-file merge.

The agent proposes reading the real tool's output to write better tests. The reviewer notes that supplying the reference executable raised Sol's validity but left its mutation score where it was (Table 4) [AE], so the ask stays on test design. The accountable builder signs once the re-run kills all three seeded faults, and the pack states that seeded faults are a proxy that "need not reflect the distribution of real-world faults" (§5, "Mutants as a Proxy for Test Strength") [V].

## Anti-patterns This Reference Helps Avoid

- **Green as proof.** *Signal:* the pack's test evidence is "the agent's tests pass". *Why it fails:* passing on the build is validity; in the benchmark it sat at 88-96% while strength sat at 38-56% (§3.1) [AE]. *Instead:* record a strength measure next to the pass record.
- **Buying strength with spend.** *Signal:* weak tests met by a bigger model or a higher effort setting. *Why it fails:* cost gives marginal gains on a log curve, and the best agent reached 55.5% (§3.1; Figure 5) [AE]. *Instead:* name the untested requirements and combinations and ask for tests of those.
- **The running program as the cure.** *Signal:* "let it see the real tool's output and it will write better tests". *Why it fails:* for Sol, validity rose and strength did not (Table 4) [AE]. *Instead:* keep the review on what the tests exercise.
- **More agents, same blind spots.** *Signal:* a second or third agent writes extra tests and the suite is called covered. *Why it fails:* pooling three agents raised the killed share from 54% to 59% (App. A.5) [AE]. *Instead:* direct the extra effort at named gaps.
- **README as spec.** *Signal:* the agent is pointed at developer docs to write tests. *Why it fails:* on 30 instances M fell to 4.0% from 25.5% (Table 5) [AE]. *Instead:* write the change's behaviour as a spec complete enough to build and test from.
- **Seeded faults that only one test can see.** *Signal:* every planted fault is caught, each by the test it was cut from. *Why it fails:* an agent seeding faults copied the test's literal values unless told to break logic, and the single-test criterion cannot tell those faults from good ones (App. A.5) [AE]. *Instead:* require logic-level faults and sample them by hand.
- **Reading a benchmark number as a promise.** *Signal:* a figure such as *agents kill 55% of faults* quoted as a property of this project's tests. *Why it fails:* the number holds for detailed specs, compiled command-line programs and planted faults, and the authors say it may overestimate agents: "suggesting that our evaluation may still overestimate agents’ test-generation performance" (§5, "Specification Realism") [V]. *Instead:* measure the project's own suite.

## Integration with Other References

| Reference | Relationship |
|---|---|
| `jimenez-swe-bench` | The other half of the evidence question. SWE-bench judges agent patches by the tests from the human pull request, tests the agent did not write (Jimenez et al., §2.2; App. A.2) and says execution-based testing alone is insufficient (§7); TestSuiteBench measures how strong the tests are when the agent writes them, and cites Jimenez et al. (2024) among code-generation benchmarks [BT]. Together they say: agent code checked against independent tests is evidence; agent code checked against its own tests is much weaker evidence |
| `uk-duck-book-qa-of-code` | Supplies the test-design rules this source's error analysis finds agents breaking: cover boundary, positive, negative, zero and missing inputs, and build expected outcomes independently rather than copying the code's output ("Test that new logic is correct using unit tests"; "Minimise your test data"). This source supplies the measure of how often agent suites fall short of them |
| `microsoft-code-with-engineering-playbook` | Its unit-test authoring example has tests passing at 100% coverage while a bug shows not all inputs are covered ("Fixing the Bug"): the same validity-without-strength gap in a hand-written suite. This source quantifies it for agent-written suites and offers planted faults as the check that coverage does not give |
| `openssf-finding-fixing-vulnerabilities-ai` | The guide holds that task verifiers sit in the trusted computing base, that one checking the wrong property can confidently approve an incorrect result, and that verifiers should be tested with known-good and known-bad cases ("Preparing CI/CD") [AR]/[AP]. This source is a worked construction of exactly that: the reference as the known-good case, requirement-targeted mutants as the known-bad cases, and a score |
| `uk-aqua-book-2025` | For black-box AI models, assurance should include validation and verification of the automatic tests that the model behaves as expected (Ch 8, "8.5 Black box models") [AP]. This source gives a way to verify the tests themselves |
| `cucumber-bdd-gherkin` | Concrete examples of a small upcoming change, talked through, written in a form that can be automated, and automated as failing tests before the implementation (docs/bdd/index.md, "Three practices") [AP]. This source's finding that agents omit input combinations, and that spec detail drives test strength (Table 5), argues for naming those combinations as examples before the build; that link is this distillation's inference |
| `he-cursor-velocity-complexity-2025` | He et al. report complexity climbing in agent-assisted projects and relay a suggestion that training favours passing tests over non-functional quality (§5.2) [BT]. Both sources find agent output that passes its checks while falling short on something the checks do not see: maintainability there, test strength here |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The benchmark's 200 starting programs, executables and reference suites come from an earlier benchmark the authors build on; its construction is relayed, not audited here [BT]. The re-implementation successes (a compiler, a browser) and the claim that autonomous development depends on strong verification are cited from prior reports [BT]. The prior test-generation benchmarks in the related-work comparison, and the prior work on natural-language ambiguity and on rule-based mutation, are cited by the authors and not held in this corpus [BT]. Of the works the paper cites, only Jimenez et al. (2024) is held here (`jimenez-swe-bench`).

**Named limits of the source.** Mutants are a proxy for test strength: they target a sample of requirements, and

> "each mutant violates a single requirement by design and need not reflect the distribution of real-world faults" (Source: Egashira et al., TestSuiteBench, §5, "Mutants as a Proxy for Test Strength") [V]

The specifications are far more detailed than typical developer documentation, so the evaluation may overestimate agents; every artefact inherits the reference implementation's bugs; the benchmark covers only command-line programs in compiled languages (§5) [AP]. Test generation was measured from the specification alone, not alongside the agent's own code. The reference-executable and developer-documentation ablations ran on GPT 5.6 Sol only, the latter on 30 instances (Tables 4-5) [AP]. The paper is a preprint; benchmark data and code are announced for release on publication (Reproducibility Statement) [AP]. Coding agents built the benchmark's specifications, suites and mutants, validated by the pipeline's checks and by hand (AI Usage Statement) [AP]. Model names are as the paper gives them.

**Evidence-marker continuity.** Results carry `[AE]` as in the deep reference; the authors' readings of them (the capability gap, test design as the bottleneck, the practitioner implication) carry `[AR]`; construction and metric definitions carry `[AP]`. Six verbatim passages are copied from the deep reference's audited `[V]` blocks (§2 "Notation"; §2.1; §3.1 "Valid but Weak Tests"; §3.2 "Error Analysis"; §5 "Mutants as a Proxy for Test Strength", used twice; §5 "Specification Realism"); none was re-extracted from the tape. The §1 "critical gap" passage is paraphrased in Key Concept 1 rather than quoted. Cross-references in the integration table cite the sibling deep references' own sections and markers.

## Runtime triggers this source addresses

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| The builder says "the agent will figure out the details" (Phase 1) | Developer documentation instead of a detailed spec cut Sol's test strength from 25.5% to 4.0% on 30 instances, with three times the underspecification failures per test (§3.2; Table 5) [AE] | Details left to the agent are details its tests are unlikely to pin down. Write down what each behaviour must do before the build, in enough detail to test from. |
| The story's acceptance criteria are prose ("works well", "handles errors") with no runnable check (Phase 1) | The authors found developer-written documentation too underspecified for test generation and built specs that describe every tested behaviour explicitly (§2.1) [AP] | Prose criteria give an agent nothing to aim its tests at. Turn each into a stated behaviour a test could fail on. |
| The spec is long and the change is large (Phase 1) | Test strength correlates negatively, if weakly, with the number of spec sections (Sol ρ = −0.42, Opus ρ = −0.16) (§3.2; App. A.2) [AE] | More requirements per change tends to mean a weaker suite per requirement. Split the change, or check test coverage per requirement. |
| The tests were written by the same agent session after the code (Phase 3) | Agent suites written from a spec were 88-96% valid yet killed 38-56% of planted faults (§3.1) [AE]. Same-session tests were not measured; treating them as no stronger is this distillation's inference | Treat these tests as asserted, not demonstrated. Before they count, measure what they catch. |
| The suite passes, but nobody knows whether it would catch a wrong implementation (Phase 3) | Mutation score against requirement-targeted planted faults, each meant to be caught by one test, after dropping tests that fail on the correct build (§2.2; §2.6) [AP] | Seed faults that each break one requirement and count how many the suite kills. That count, with its conditions, goes on the ledger. |
| The agent runs for an hour unattended and reports success (Phase 4) | Valid tests give an impression of well-tested software without surfacing violations; the authors link this, without a citation, to agents writing large suites yet missing failures in their own code [AR] (§3.1, "Valid but Weak Tests") | "Done" backed by its own green tests is a claim. Ask what those tests would catch, not whether they pass. |
| "It worked first time", or a flaky check passed on retry (Phase 5) | Before scoring, suites run three times on the correct build and tests whose result changes are removed (§2.6) [AP] | A test that changes result between runs can't count as evidence either way. Run it repeatedly and take it out of the count until it's stable. |
| The pack says "all tests pass" with no run record (Phase 7) | Even with a run record, passing measures validity; strength is a separate number (§2.6; §3.1) [AE] | Send it back for the run record, and ask for a strength measure beside it. "All tests pass" says the tests agree with the code. |

## Trigger extensions surfaced by this source

| Phase | Trigger (what the practitioner notices) | Response (grounded in this source) |
|---|---|---|
| 3 | The agent's suite has far fewer tests than the spec has behaviours | Require at least one meaningful test per documented behaviour; suites smaller than the requirements need scored lower, and Sol's were about five times smaller than the reference (§3.2; App. D.2) [AE] |
| 3 | Each feature is tested once, with a single or default input | Ask which input combination would expose a wrong build and require a test that uses it; omitted combinations were the commonest miss (§3.2, "Error Analysis") [AE] |
| 3 / 6 | A test asserts only the shape of the output (length, non-empty, a keyword appears) | Require the assertion to pin the content the requirement fixes; a shape-only check passed a script for the wrong shell (App. A.6) [AE] |
| 3 | "Give the agent the running program and it will write better tests" | Expect validity to rise and strength not to; for Sol, M moved from 37.7% to 38.1% (Table 4) [AE] |
| 3 | "Turn up the reasoning effort" or "use the bigger model" for the tests | Expect marginal gains on a log curve; Sol 31.3% to 46.5% from low to xhigh, best agent 55.5% (§3.1) [AE] |
| 6 | "Have a second agent write more tests" | Expect modest gains; three agents pooled killed 59% against 54% for the best alone (App. A.5) [AE] |
| 5 | Nobody has checked the test gate against planted faults | Calibrate the gate with faults that each break one requirement, spread evenly over the spec, and score what it catches (§2.2; §2.6) [AP] |
| 5 | Every planted fault is caught only by the test it was derived from | Check the faults break logic across an input class rather than a test's literal values; an uninstructed agent copied literals (App. A.5; App. D.1) [AE] |
| 7 | The pack cites the agent's own suite passing as the evidence for the change | Don't sign on that line alone: ask for the share of seeded single-requirement faults the suite kills, stated with the proxy caveat that planted faults need not match real ones (§2.6; §5) [AP] |
| 1 | An agent's output fails and the team argues whether the spec or the agent is wrong | Classify the failure as a generation fault or a spec defect (underspecified or contradictory), and require any claimed contradiction to quote the spec exactly (§2.3; App. D.1) [AP] |
