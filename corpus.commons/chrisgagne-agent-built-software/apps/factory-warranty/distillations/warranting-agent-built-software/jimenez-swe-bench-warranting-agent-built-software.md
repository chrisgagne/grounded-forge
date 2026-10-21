
# Jimenez et al., SWE-bench, Warranting Agent-Built Software Distillation

**Source:** Jimenez, Yang, Wettig, Yao, Pei, Press and Narasimhan (Princeton; University of Chicago), "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", ICLR 2024; arXiv:2310.06770v3 [cs.CL], 11 Nov 2024, 52 pages. Licence: CC BY 4.0. Scope: open.

**Applicability gate (Pass G.0): clear yes.** (1) The source answers practitioner questions this axis asks directly: whether "correct" for a change is written down where a machine can check it (the task instance and its two kinds of test), which claims were demonstrated rather than asserted (a patch counts only when it applies and the tests run and pass), and what a passing run still leaves unchecked (the authors' own limit on execution-based testing). (2) Its concepts land naturally in seven of the eight phases. (3) Its findings on how model patches fail (they skip the codebase's own facilities, break other modules that use what they change, and come out smaller than the real fix) are the axis's second and third reflexes seen from the code side: a green run is not safety, and something has to check what the tests cannot see.

**Phase mapping.** Primary: Phase 3, Locking the tests (fail-to-pass and pass-to-pass tests, execution-based validation on the base commit). Secondary: Phase 1, Specifying the change (the task instance as a checkable spec; what the problem statement must state); Phase 5, Gating deterministically (the resolution criterion; six patch outcomes); Phase 6, Reviewing independently (what tests miss: the greedy patch, cross-module breakage, the smaller-than-real fix). Supporting: Phase 2, Triaging risk (a change to a shared entity, a multi-file change); Phase 4, Building in the sandbox (execution feedback before submitting; the cost of a wider context); Phase 7, Warranting the change (a run record against the resolution criterion; reading a benchmark score). No rows: Phase 8, Releasing and operating (the source stops at evaluating a patch against tests and tracks nothing after it). Phase 2 rows are narrow: the source sorts no change by whether it touches auth, personal data, money or infrastructure, or by what it can break that cannot be undone.

**Transfer caveat.** The models in this paper were not agents. Each wrote one patch per issue in a single pass with greedy decoding, from an issue and retrieved files, with no execution environment and no chance to run tests (p. 5, §4; p. 30, App. D.2) [AP]; the authors call their experiments a baseline of the simplest approaches and encourage agent-based and tool-augmented methods (p. 10, §7) [AP]. All task instances are Python, from 12 popular open-source repositories, and the models evaluated are those of 2023 to 2024. Where this distillation carries a finding to an agent working in a harness, it says the step is its own inference.

## Warranting Agent-Built Software Relevance

This source supplies the corpus's working model of a change whose correctness a machine can check: a problem statement pinned to a base commit, tests that must move from fail to pass, tests that must keep passing, and a rule that the change counts only if it applies and every one of those tests runs and passes (Source: Jimenez et al., SWE-bench, p. 3, §2.2; p. 21, App. A.4–A.5) [AP]. It also shows how to check the tests themselves before trusting them: each candidate was run on the base commit and again with the fix, kept only if a test moved from fail to pass, and dropped if the base-commit failure looked like a naming error (pp. 19–20, App. A.3) [AP]. For a builder whose warranty rests on the harness rather than on reading the code, that is a ready shape for the change's spec and its locked tests.

The source is just as useful for what it says a green run misses. Model patches that applied mostly passed no target test at all; those that fixed the issue sometimes broke other modules that use the changed code; resolved patches skipped the codebase's own helpers and libraries and came out shorter and narrower than the human fix; and the authors state that execution-based testing alone is insufficient to guarantee reliable model output (p. 9, §5.1; p. 10, §7; pp. 26–29, App. C.5–C.6) [AR]. That gives the independent reviewer a concrete list of what to check that the tests cannot, and it gives the warranty assessor a vocabulary (Resolved, Breaking Resolved, No-Op, Regression) for classing a run. Its numbers keep their conditions: single-pass non-agent models, Python, retrieval setting, and repository all move the score.

## Key Concepts for Warranting Agent-Built Software

1.  **The task instance: a change spec a machine can check.** Each instance pairs a codebase at the pull request's base commit, a problem statement, a test patch and a gold patch, split from the human pull request (Source: Jimenez et al., SWE-bench, p. 16, App. A.1; p. 18, App. A.2) [AP]. The problem statement takes the issue text and only the comments written before the pull request's first commit, "to avoid leakage of solution details" [V] (p. 16, App. A.1). Fail-to-pass tests characterise the problem statement and check that the revision addresses it; pass-to-pass tests check that it does not break existing behaviour (p. 21, App. A.5) [AP]. Every instance has at least one fail-to-pass test, 40% have two or more, and a median of 51 further tests check prior behaviour (p. 3, §2.3) [AP].

2.  **Execution-based validation of the tests.** Per candidate: reset to the base commit, install, apply the test patch and run (log_pre), apply the gold patch and run again (log_post); keep the instance only if at least one test moves from fail to pass (pp. 19–20, App. A.3) [AP]. Instances whose log_pre shows an ImportError or AttributeError are removed as potentially indicating dependency-naming errors (pp. 19–20, App. A.3) [AP]. The step generally removes half the candidates (p. 19, App. A.3) [AP].

3.  **Tests that call names the spec never states.** Instances whose tests invoke functions or classes first introduced in the solution are excluded, because the problem statement usually does not name them and such tests may be impossible to satisfy even for a human developer (Source: Jimenez et al., SWE-bench, p. 16, App. A.1) [AP].

4.  **The resolution criterion.** The patch is applied and the instance's tests are run; it resolves the issue only if it applies and all of those tests pass, and the metric is the share of instances resolved (Source: Jimenez et al., SWE-bench, p. 3, §2.2) [AP]. A task counts as solved only if every fail-to-pass and every pass-to-pass test passes, and a missing test counts as a failure; a patch that still fails to apply after one automatic repair, or a failing test command, scores 0 (p. 21, App. A.4) [AP].

5.  **Six patch outcomes.** For patches that apply, the authors class the run by which tests pass: all fail-to-pass and all pass-to-pass, Resolved; all fail-to-pass but not all pass-to-pass, Breaking Resolved; some fail-to-pass with all pass-to-pass, Partially Resolved; some fail-to-pass without all pass-to-pass, Work in Progress; no fail-to-pass with all pass-to-pass, No-Op; no fail-to-pass and some prior behaviour lost, Regression (pp. 26–28, App. C.5, Table 22) [AP]. Of Claude 2's 1,078 applied patches, 110 were Resolved, 26 Breaking Resolved, 471 No-Op and 436 Regression (p. 29, Table 23) [AP]. Most non-resolved patches pass not a single fail-to-pass test (p. 27, App. C.5) [AP].

6.  **Cross-module breakage.** In the partial passes the authors inspected, the model showed some understanding of the task, but many failed because the fix for the immediate issue did not account for other modules that use the changed entity; the baselines' view of the codebase left out inter-file dependencies and function relationships (Source: Jimenez et al., SWE-bench, p. 27, App. C.5) [AR]. In the astropy case the model edited a regex that is reused elsewhere in the file and failed existing tests as well as the target (pp. 37–38, Table 27) [AE]. The authors see potential value in letting models run fixes against existing tests before deciding whether to submit (p. 28, App. C.5) [AR].

7.  **The greedy patch.** Across the cases they examined, models wrote primitive code, did not use existing libraries or the rest of the codebase, and solved the problem exactly with little regard for code style or the codebase's constraints, where many gold patches made structural improvements that anticipate future issues (Source: Jimenez et al., SWE-bench, p. 9, §5.1) [AR]. The cases show it: a model writing its own validation function where the gold patch passes arguments to an existing call (pp. 33–34, Table 25) [AE]; a "lucky" fix that passes the tests while ignoring the codebase's own string helper (pp. 45–46, Table 31) [AE]; a generic online-style answer where the codebase needed a specific one (pp. 41–42, Table 29) [AE].

8.  **Smaller than the real fix.** Successfully applied model patches added and removed fewer lines than the gold patches and rarely edited more than one file; Claude 2's applied patches averaged 19.6 total lines against 44.1 for the matching gold patches (Source: Jimenez et al., SWE-bench, p. 7, §5; p. 8, Table 8) [AP]. The authors' case studies indicate that hallucinations, not keeping to existing code style and structure, and mishandled long-range dependencies surface more often in longer generations (p. 28, App. C.6) [AR]. Gold patches average 1.7 files, 3 functions and 32.8 lines (p. 4, Table 1) [AP].

9.  **Localising code in long contexts.** Performance drops as context length grows; the authors explain that models see much code that does not bear on the issue and struggle to find the code that needs changing (Source: Jimenez et al., SWE-bench, p. 6, §5) [AR]. A larger retrieval budget lowered scores even where it raised recall of the right files (p. 6, §5; p. 5, Table 2) [AR], and collapsing the given files to the edited lines plus or minus 15 raised them (pp. 6–7, Table 6) [AP]. Regenerating whole files did worse than writing patches (Claude 2, 2.2% against 4.8%) (p. 7, §5) [AP].

10.  **Evidence the model could not read.** Issues can carry their evidence as linked images: 32% of matplotlib and 10% of seaborn instances, 2% overall (Source: Jimenez et al., SWE-bench, p. 6, §5) [AP]. In the seaborn case the authors attribute the failure directly to the lack of image input, and add that design diagrams and interface specifications pose the same kind of challenge (pp. 39–40, Table 28) [AE].

11.  **The limits of test-only evaluation.** The authors state that execution-based testing alone is insufficient to guarantee reliable model output, because generated code is often less comprehensive, efficient or readable than human code (Source: Jimenez et al., SWE-bench, p. 10, §7) [AR]. In preliminary work they use complexity metrics as an automatic signal: a shorter Claude 2 patch that the caption says solves the problem adds a conditional to a widely used, relatively complex class and raises its Cyclomatic complexity from 3 to 5, where the longer gold patch changes a logically simpler function (pp. 28–30, App. C.7, Figure 10) [AE].

12.  **A score belongs to its conditions.** Performance differs heavily across repositories, and the issues each model resolves "do not necessarily overlap extensively" [V] (Source: Jimenez et al., SWE-bench, p. 6, §5; p. 25, App. C.2). The same model moves with the setting: Claude 2 resolves 1.96% with sparse retrieval and 4.8% when given the files the fix edited, a setting the authors call less realistic (p. 5, §4.1; p. 6, §5) [AP]. Models with shorter context windows are inherently disadvantaged (p. 5, Table 4) [AP].

## Questions to Ask During Warranting Agent-Built Software

### Phase 1: Specifying the change

| Need | Question | Source-tag |
|---|---|---|
| Make "correct" checkable | Is the change written as a problem statement pinned to a base commit, with at least one test that must move from fail to pass and a set of tests that must keep passing? | §2.2; App. A.1, A.5 |
| Keep the fix out of the spec | Does the spec state the problem without leaking the intended solution, the way the problem statement keeps only comments written before the fix began? | App. A.1 |
| Name the interfaces | Does any test the spec relies on call a function or class the spec never names? | App. A.1 |
| Size the change | Will the fix need several files and functions, the kind of change the models handled worst, and can it be split into short fixes? | App. F; Table 8 |
| Carry what the agent cannot see | Is any of the ticket's evidence in an image, and has it been put into words and tests, or confirmed readable by the agent? | §5; Table 28 |
| State the codebase's constraints | Which of the codebase's existing helpers, libraries and conventions must the fix use, written down so a greedy patch can't skip them? | §5.1; Tables 25, 31 |

### Phase 2: Triaging risk

| Need | Question | Source-tag |
|---|---|---|
| Spot a change to shared code | Does the diff edit a function, class or pattern that other modules use, and who are those callers? | App. C.5; Table 27 |
| Spot a widely used class getting more complex | Does the change add branches to a class many callers rely on, where a simpler place for the logic exists? | App. C.7, Figure 10 |

### Phase 3: Locking the tests

| Need | Question | Source-tag |
|---|---|---|
| Tag each locked test | Is each test tagged fail-to-pass or pass-to-pass, and are both sets non-empty? | App. A.4–A.5 |
| See the new tests fail first | Was each fail-to-pass test run on the base commit and seen to fail, then seen to pass with the fix? | App. A.3 |
| Read the failure | Does any new test fail on the base commit only with an ImportError or AttributeError, a failure that may show a naming error rather than the bug? | App. A.3 |
| Keep the tests out of the agent's hands | Do the tests that will judge the change come from outside the session that writes it? | App. A.2; §4.2 |
| Judge by state, not report | Is success decided by applying the change and running the tests, not by reading the agent's account? | §2.2 |

### Phase 4: Building in the sandbox

| Need | Question | Source-tag |
|---|---|---|
| Run before submitting | Did the agent run the existing tests against its change before it reported done? | App. C.5 |
| Weigh more context | If the harness is giving the agent more of the codebase, has anyone checked whether results got better or worse? | §5; Table 2 |
| Check the edit's form | Did the agent edit with a patch or regenerate whole files? | §5 |

### Phase 5: Gating deterministically

| Need | Question | Source-tag |
|---|---|---|
| Define the pass | Does the gate pass only when every locked fail-to-pass and pass-to-pass test ran and passed, with a missing test counted as a failure? | App. A.4 |
| Class the run | Which of the six outcomes is this run: Resolved, Breaking Resolved, Partially Resolved, Work in Progress, No-Op or Regression? | App. C.5, Table 22 |
| Add a signal beyond tests | Is there an automatic measure (complexity on the touched functions and classes) that would flag a passing change that made a shared class harder to maintain, used knowing the authors call it preliminary? | App. C.7 |
| Calibrate the gate | Has the gate been run on fixtures built like task instances (a real past change, its tests validated on the base commit) to show it still catches what it should? This use is this distillation's inference | App. A.3 |

### Phase 6: Reviewing independently

| Need | Question | Source-tag |
|---|---|---|
| Review what tests can't see | Has someone checked the change for comprehensiveness, efficiency and readability, which the authors say tests alone do not guarantee? | §7 |
| Check reuse | Does the diff add its own helper or primitive code beside a facility the codebase or an existing library already provides? | §5.1; Tables 25, 31 |
| Check callers | Does the diff change an entity other modules use, and were those modules' tests run? | App. C.5 |
| Check footprint | Is the diff much smaller than the spec's scope, touching one file where the problem spans several? | Table 8; App. F |
| Check placement | Did the logic go into a complex, widely used class where a simpler function would hold it? | App. C.7 |
| Check fit | Does the patch follow the codebase's own style and naming where it does the same thing elsewhere? | Table 32 |

### Phase 7: Warranting the change

| Need | Question | Source-tag |
|---|---|---|
| Find the run record | Does the pack show the locked tests' run against the change, each fail-to-pass and pass-to-pass result, and the outcome class? | App. A.4; App. C.5 |
| Read a benchmark claim | Is a model's benchmark score being offered as a reason to trust this change, and does the pack say the score varies by repository, setting and model? | §5; App. C.2 |
| Name what the tests didn't check | Does the pack say what the passing run leaves unchecked (reuse, callers, readability) and who checked it? | §7 |
| Check intent | Does the pack show the change does what the client meant, not only what the tests encode? | App. E |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| The fix passes its target tests and an existing test elsewhere now fails | Breaking Resolved: the issue's behaviour achieved, prior behaviour lost (App. C.5) [AP] | Block; list the callers of what changed and run their tests |
| The agent reports a fix and no fail-to-pass test passes | No-Op or Regression, the commonest outcomes for non-resolved patches (App. C.5; Table 23) [AP] | Return it; ask whether the codebase changed at all, and what broke if it did |
| A new test fails on the base commit only with an ImportError or AttributeError | Possible naming error, the kind the authors removed from validation (App. A.3) [AP] | Don't count it as fail-to-pass; fix the test until it fails on the bug |
| A locked test calls a function or class the spec never names | A test on an unstated interface, which may be impossible to satisfy from the spec (App. A.1) [AP] | Name the interface in the spec, or rewrite the test against stated behaviour |
| The diff adds a helper, a type cast or a generic workaround beside an existing facility | The greedy patch (§5.1) [AR]; Tables 25, 29 and 31 [AE] | Require the reuse or a stated reason |
| The diff is a few lines in one file for a problem the spec places across several | Smaller than the real fix (Table 8) [AP]; models struggle with multi-line, multi-file changes (App. F) [AR] | Ask what a wider fix would handle that this one doesn't |
| A shared regex, base class or utility is edited to fix one caller's case | Cross-module breakage (App. C.5) [AR]; Table 27 [AE] | Require a caller list and pass-to-pass tests over each caller |
| The ticket's evidence is a screenshot or chart | Evidence the model could not read; a failure the authors attribute to missing image input (Table 28) [AE] | Transcribe what the image shows into the spec and tests |
| Widening the agent's context is proposed as the fix for poor results | More retrieved context lowered scores even as recall rose (§5; Table 2) [AR] | Measure on this codebase before keeping it |

## When to Use This Reference

- Reach for it when writing a change's spec and tests in a form a gate can check: it is the corpus's worked construction of a problem statement, fail-to-pass and pass-to-pass tests, and validation on the base commit.
- Reach for it when classing a run at the gate or on the warranty pack: the resolution criterion and the six outcomes give names to "fixed but broke something" and "changed nothing".
- Reach for it when a reviewer needs to know what a passing run still misses in model-written code: reuse, callers, footprint, placement.
- Reach for it when someone cites a benchmark score, this one included, as a reason to trust a change.
- Reach for another source when the question is how strong agent-written tests are (`egashira-testsuitebench-2026`), what a change touches and which security gates that makes mandatory (the standards and threat lists), how the sandbox should limit an agent (`openssf-finding-fixing-vulnerabilities-ai`, `owasp-agentic-top10-2026`), or what happens after release (`he-cursor-velocity-complexity-2025`, `dora-ai-assisted-swdev-2025`). This source does not cover risk classes, sandboxing or operation.

## Worked Example

*Scenario (operator-authored).* A two-person studio maintains a booking app for a client. The ticket: dates on the confirmation email show in the wrong timezone; the client attached a screenshot of the email beside the booking screen. The agent changes the shared date-formatting helper that the email, the invoice and the calendar export all call, adds its own small timezone-conversion function rather than using the timezone library the project already depends on, writes one new test, and reports done. The diff is nine lines in one file. The independent reviewer reads the ledger, not the diff.

*Applying the source.* The reviewer first asks what the run shows. A patch counts as resolving an issue only when it applies and every locked test passes:

> "If the patch applies successfully and all of these tests pass we consider the proposed solution to have successfully resolved the issue. The metric for our benchmark is the percentage of task instances that are resolved." (Source: Jimenez et al., SWE-bench, p. 3, §2.2) [V]

The ledger has one new test and no pass-to-pass set, so there is nothing to show that the invoice and calendar export still work. Following the task-instance shape (p. 21, App. A.5) [AP], the reviewer asks the harness to tag the new test fail-to-pass and to lock the existing invoice, calendar and email tests as pass-to-pass. Run on the base commit, the new test fails with an AttributeError, because it calls a function the agent's own patch introduces. The authors removed such failures from their validation as possible naming errors (pp. 19–20, App. A.3) [AP] and excluded tests that call names the problem statement never states (p. 16, App. A.1) [AP], so the reviewer sends the test back to be rewritten against the stated behaviour: an email for a booking in a given zone shows that zone's time.

With the rewritten test, the fix passes its target test, and the calendar export test fails. That is a Breaking Resolved run (p. 27, App. C.5) [AP], and the authors name the cause they saw in such cases:

> "a change that correctly resolves the immediate issue does not account for other modules that use and are affected by the changed entity" (Source: Jimenez et al., SWE-bench, p. 27, App. C.5) [V]

The reviewer blocks the change and adds two review notes the tests would not raise. The new conversion function sits beside a library the project already uses, the pattern the authors saw across model patches (p. 9, §5.1) [AR]; and the nine-line, one-file diff is narrower than a problem that touches three outputs, in line with model patches that rarely edited more than one file (p. 7, §5; Table 8) [AP]. The screenshot is transcribed into the spec as the expected and actual times, since a model without image input cannot use it (Table 28) [AE]. This harness's agent, unlike the paper's models, could have run the existing tests before reporting done; sending it back to do so is the authors' suggested remedy (p. 28, App. C.5) [AR], applied here as this distillation's inference.

The next run passes every fail-to-pass and pass-to-pass test, using the existing library. The pack records the run as Resolved and still names what the run did not check, because the authors are explicit that tests alone don't settle it:

> "Lastly, while this work evaluates models using execution-based code testing, relying solely on this method is insufficient to guarantee reliable performance of model generations, as we find automated code generations from LMs can frequently be less comprehensive, efficient, or readable compared to human-written solutions." (Source: Jimenez et al., SWE-bench, p. 10, §7) [V]

## Anti-patterns This Reference Helps Avoid

- **Fixed means safe.** *Signal:* the target test passes and the pack says done. *Why it fails:* a run can pass every fail-to-pass test and still break existing behaviour, the Breaking Resolved class (App. C.5) [AP]. *Instead:* lock pass-to-pass tests over the callers and require both sets to pass.
- **Counting a test that never tested the bug.** *Signal:* a new test "fails before, passes after", but its base-commit failure is an ImportError or AttributeError. *Why it fails:* that failure may come from naming, not from the bug, and the authors removed such cases from validation (App. A.3) [AP]. *Instead:* read the base-commit failure before tagging the test.
- **Tests that only the solution could satisfy.** *Signal:* locked tests call functions the spec never names. *Why it fails:* such tests may be impossible to satisfy from the problem statement, even for a human (App. A.1) [AP]. *Instead:* name the interface in the spec or test stated behaviour.
- **Taking the passing patch as the right patch.** *Signal:* a resolved run whose diff adds its own helper beside an existing one. *Why it fails:* the authors call such a fix "lucky" and doubt it would survive review or future issues (Table 31) [AE]. *Instead:* review for reuse and fit to the codebase.
- **More context as the cure.** *Signal:* poor results met by feeding the agent more of the codebase. *Why it fails:* in the paper's setup, more retrieved context lowered results even when it raised recall (§5; Table 2) [AR]. *Instead:* measure the change on this codebase, and consider narrowing the context to where the fix belongs.
- **A benchmark score as a warranty.** *Signal:* a model's leaderboard score is cited as the reason to trust a change. *Why it fails:* performance differs heavily by repository and setting, and different models solve different issues (§5; App. C.2) [AP]. *Instead:* rely on this change's own run record and the gate's calibration on this codebase.

## Integration with Other References

| Reference | Relationship |
|---|---|
| `egashira-testsuitebench-2026` | The other half of the test-evidence question. SWE-bench judges model patches against tests split from the human pull request and applied only at evaluation, outside the model's input (App. A.2; App. A.4; §4.2) [AP]; TestSuiteBench measures how weak tests are when an agent writes them from a spec, and cites SWE-bench among code-generation benchmarks [BT]. Together: agent code checked against independent tests is evidence, and agent code checked against its own tests is much weaker evidence |
| `why-language-models-hallucinate-kalai` | Kalai et al. class SWE-bench's scoring as binary with no credit for an uncertainty response (§4.1, Table 2; App. F.3) [AP], argue that such scoring rewards guessing over abstaining (§4.1) [AR], and propose adding explicit confidence targets to mainstream benchmarks such as SWE-bench (§4.2) [AP]. This source's resolution metric is that binary score; its six-outcome analysis does separate a No-Op from a Regression. See the named disagreement |
| `becker-metr-ai-developer-productivity-2025` | Becker et al.'s developers, working in large, mature repositories, report AI making unwanted changes in other parts of the code (App. C.1.3) [AE]: field reports of the cross-module breakage this source finds in benchmark patches. Becker et al. also read their slowdown as some evidence that capability in the wild may be lower than common benchmarks suggest (§4) [AR]; see the named disagreement |
| `he-cursor-velocity-complexity-2025` | He et al. find static-analysis warnings and code complexity rising and staying risen in projects that adopt an agentic coding tool (§4.1.2) [AE]. This source's single complexity case (Figure 10) shows the mechanism at patch scale. He et al. add that complexity metrics were designed for human code and their fit to AI-written patterns is open (§6) [AR], a caution on using them as a gate signal |
| `openssf-finding-fixing-vulnerabilities-ai` | The guide says agents need to run tests to be effective ("Preparing the sandbox", "Value of sandboxes") [AP] and that a robust CI/CD system must check the AI's work ("Preparing CI/CD") [AP]: the execution feedback this source's authors point to as a remedy (App. C.5) [AR]. The guide also relays studies in which AI fixes that had to touch several files or code paths often failed or broke behaviour ("Do not presume AI can correctly fix all vulnerabilities") [BT], in line with this source's multi-file finding |
| `uk-duck-book-qa-of-code` | The Duck Book's golden rules (review any LLM-written code yourself; you alone are responsible for it) ("Vibe coding: Using LLMs to write code in the workplace") [AR] set who answers for a passing patch. This source supplies what that reviewer should look for that the tests don't: reuse, callers, footprint |
| `microsoft-code-with-engineering-playbook` | Its area-regression test plan (cases for the changed area and its integration points) and full-regression plan ("Grouping Test Cases into Test Plans") [AP] are the practice behind this source's pass-to-pass set. This source shows what happens without them: fixes that break other modules |
| `dora-ai-assisted-swdev-2025` | DORA finds working in small batches amplifies AI's effect on product performance (p. 58) [AE]. This source finds models more adept when the fix is short and struggling with multi-file changes (App. F) [AR]. Both point the harness to small changes; that pairing is this distillation's inference |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The authors cite prior work for benchmark saturation, for what makes a good benchmark, for models being distracted by long context, for the retriever, for the base model and fine-tuning method behind SWE-Llama, for the two complexity metrics, and for the AI-safety questions in App. E [BT]; none of those works is held in this corpus, and this distillation does not draw on them. The self-contained coding benchmarks the paper sets itself against are named in the deep reference, not here.

**Named limits of the source.** The authors state three: all instances are Python; their experiments are a baseline of the simplest approaches, not agents or tool-augmented systems; and execution-based testing alone is insufficient (p. 10, §7) [AP]. The qualitative findings rest on cases the authors selected (p. 7, §5.1; p. 32, App. F) [AP], and the complexity-metric work is called preliminary (p. 28, App. C.7) [AP]. The deep reference records places where the text and tables don't agree, among them Claude 2's sparse-retrieval score (1.96% in the text, 1.97% in Table 5), the v3 Table 5 listing Claude 3 Opus above Claude 2 while the text still calls Claude 2 the best, and the No-Op share (the text says 60% to 70% of no-target-test patches; Table 23's counts give 51% to 66%). This distillation reports both figures where it uses them, or the table's. Appendix A.7, on SWE-bench Lite's selection, breaks off in the PDF itself, so Lite's criteria are not in the source. Table 23 does not state its retrieval setting.

**Evidence-marker continuity.** Procedures and reported results carry `[AP]`; the authors' explanations (the greedy patch, cross-module breakage, the localisation account, the execution-feedback remedy) carry `[AR]`; the appendix cases and Figure 10 carry `[AE]`. Five passages are copied from the deep reference's audited `[V]` blocks: the leakage phrase (App. A.1), the non-overlap phrase (§5), and three blockquotes in the worked example (§2.2; App. C.5; §7). Key Concept 11 paraphrases the §7 limit (`[AR]`); the exact words are in the worked example. The §5.1 greedy-patch passage and the App. F summary are paraphrased rather than quoted. None was re-extracted from the tape. Cross-references in the integration table cite the sibling deep references' own sections and markers.

## Runtime triggers this source addresses

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| The story's acceptance criteria are prose ("works well", "handles errors") with no runnable check (Phase 1) | Fail-to-pass tests characterise the problem statement; every task instance has at least one (App. A.5; §2.3) [AP] | Each criterion needs a test that fails on the code as it is and passes once the change is right. Until it has one, it isn't checkable. |
| The spec is long and the change is large (Phase 1) | Models handled short fixes better and struggled with multi-line, multi-file changes; applied patches rarely touched more than one file (App. F; Table 8) [AR] | A big multi-file change is where model patches come up short. Split it, or expect the first patch to be narrower than the fix. |
| The builder says "the agent will figure out the details" (Phase 1) | The greedy patch: models solved the problem exactly with little regard for the codebase's style or constraints, and skipped its existing libraries (§5.1) [AR] | Details left to the agent get solved the shortest way. Write down which helpers, libraries and conventions the fix must use. |
| The agent proposes changing a test so the build goes green (Phase 3) | Patches are judged against tests taken from the human pull request and applied at evaluation, outside the model's input (App. A.2; §4.2; App. A.4) [AP]. Blocking the edit follows from that design; the source does not discuss an agent editing tests | The tests that judge the change have to come from outside the change. Keep them locked and route any revision through a person. |
| The tests were written by the same agent session after the code (Phase 3) | Every SWE-bench test was validated by execution: seen to fail on the base commit and pass with the fix (App. A.3) [AP]. The source did not measure agent-written tests | Before these count, run each on the base commit and see it fail for the right reason, then pass with the change. |
| A test checks the agent's output text rather than the system's state (Phase 3) | Resolution is decided by applying the patch and running the tests (§2.2) [AP] | The agent's account of what it did is not the test. Run the tests against the changed code. |
| The suite passes, but nobody knows whether it would catch a wrong implementation (Phase 3) | Execution-based validation keeps a test only if it moves from fail to pass, and drops base-commit failures that look like naming errors (App. A.3) [AP] | The minimum is that each target test has been seen failing on the old code. If it never failed, it proves nothing about the fix. |
| The agent runs for an hour unattended and reports success (Phase 4) | Of applied model patches that did not resolve the issue, most passed no target test, as No-Ops or Regressions (App. C.5; Table 23) [AP] | A report of success says nothing about which outcome this is. Run the locked tests and class the result. |
| The builder approves because reading the diff is too slow (Phase 6) | Execution-based testing alone is insufficient; generated code is often less comprehensive, efficient or readable (§7) [AR] | Skipping the diff means something else must check what the tests can't: reuse, callers, footprint and readability. Name who does. |
| The pack says "all tests pass" with no run record (Phase 7) | The resolution criterion: every fail-to-pass and pass-to-pass test passes, and a missing test counts as a failure (App. A.4) [AP] | "All tests pass" needs the run: which tests, which result, which outcome class. A missing test is a failed test. |

## Trigger extensions surfaced by this source

| Phase | Trigger (what the practitioner notices) | Response (grounded in this source) |
|---|---|---|
| 1 | The ticket's evidence is a screenshot, chart or mock-up image | Transcribe what the image shows into the spec and its tests, or confirm the agent can read images; the authors attribute a failure directly to the lack of image input (Table 28) [AE] |
| 1 / 3 | A locked test calls a function or class the spec never names | Name the interface in the spec or rewrite the test against stated behaviour; tests on names only the solution introduces may be impossible to satisfy from the problem statement (App. A.1) [AP] |
| 2 / 6 | The diff edits a shared function, base class or reused pattern to fix one caller's case | Require a caller list and pass-to-pass tests over each caller; fixes that did not account for other modules using the changed entity broke them (App. C.5) [AR]; Table 27 [AE] |
| 3 | A new test's failure on the base commit is an ImportError or AttributeError | Don't count it as fail-to-pass; the authors removed such failures as possible naming errors (App. A.3) [AP] |
| 3 | The locked tests have no pass-to-pass set | Lock the existing tests over what the change touches as pass-to-pass; a run that passes its targets can still break prior behaviour (App. A.5; App. C.5) [AP] |
| 4 | The agent reports done without running the existing tests against its change | Send it back to run them before submitting; the authors see potential value in letting models run fixes against existing tests first (App. C.5) [AR]. The paper's models could not; applying it to an agent is this distillation's inference |
| 4 | The harness widens the agent's context to improve results | Measure the effect before keeping it; more retrieved context lowered resolution even where recall rose, in the paper's single-pass setup (§5; Table 2) [AR] |
| 5 | The run passes the fail-to-pass tests while a pass-to-pass test fails | Class it Breaking Resolved and block (App. C.5, Table 22) [AP] |
| 5 | The agent reports a fix and no fail-to-pass test passes | Class it No-Op or Regression and return it (App. C.5, Table 22) [AP] |
| 6 | The diff is much smaller than the spec's scope, often a single file | Ask what a wider fix would handle; applied model patches ran shorter than human fixes and rarely touched more than one file (Table 8) [AP] |
| 6 | The diff adds its own helper, cast or generic workaround beside a facility the codebase or an existing library already provides | Require the reuse or a stated reason; model patches skipped existing libraries and the rest of the codebase (§5.1) [AR]; Tables 25, 29, 31 [AE] |
| 6 | The change adds a branch to a widely used, already complex class | Ask whether the logic belongs in a simpler function; the authors' preliminary complexity metric flagged such a patch though it passed (App. C.7, Figure 10) [AE] |
| 7 | The pack or proposal cites a model's benchmark score as the reason to trust the change | Require this change's own run record; benchmark performance differs heavily by repository and setting, and different models solve different issues (§5; App. C.2) [AP] |
