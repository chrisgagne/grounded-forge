# Warranty pack: 20261014-135052-flag-code-that-evaluates-strings

**Change:** Flag code that evaluates strings built at run time  
**Repo:** `<scratch>/first-job/factory` · **branch** `factory/20261014-135052-flag-code-that-evaluates-strings` · **baseline** `abe1502136c9` → **head** `e963be53a848f240d8c4e405ae7967ff2e29494c` (tree `230b64905210b3776468161cdb9ef9fc8af55cde`)  
**Builder:** claude  
**Assembled from ledger events** e001–e062 (`ledger.json`).

**Status:** READY TO SIGN

## Story

> # Flag code that evaluates strings built at run time
>
> The factory's pinned semgrep rules (`factory/rules/semgrep/`) catch SQL built from strings, but nothing catches code that evaluates a string assembled at run time: JavaScript's `eval(x)` and `new Function(x)`, or Python's `eval(x)` and `exec(x)`. The OWASP Top 10 for Agentic Applications (ASI05) names this as a way generated code runs something nobody reviewed.
>
> As the person who signs off a change, I want the gate and the factory check to flag a call to `eval`, `new Function`, or Python's `exec`, whose argument isn't a fixed string literal, so a change that adds one stops before it runs. A call with a plain string literal isn't flagged.

## Risk classes

- **llm-agent**: keyword in story/acceptance: agentic. Required gates: none beyond the standard gates. Review focus: OWASP Top 10 for LLM Applications 2026 and OWASP Top 10 for Agentic Applications 2026: prompt injection, excessive agency, tool misuse, data leaking through the model.

Triage: pass (e028), phase diff.

## Demonstrated

Commands the driver ran, with exit codes and output hashes.

- [e010] tests:baseline-tests `PYTHONPATH=. "<factory>/.venv/bin/python" -m pytest -q -rA -p no:cacheprovider` exit 0, output sha256 `933cf8d1f5b19f23`, log `tests/baseline-tests.log`
- [e015] tests:new-tests `PYTHONPATH=. "<factory>/.venv/bin/python" -m pytest -q -rA -p no:cacheprovider` exit 1 (expected: red before the build), output sha256 `787b72a9e17c3bda`, log `tests/new-tests.log`
- [e032] gate:secrets `gitleaks git --no-banner --redact --ignore-gitleaks-allow --log-opts=abe1502136c932edd522d539a2e2bddfd2d50372..HEAD --report-format json --report-path <scratch>/first-job/factory/.factory/changes/20261014-135052-flag-code-that-evaluates-strings/gate/gitleaks.json .` exit 0, output sha256 `0f3739c986ed4f76`, log `gate/secrets.log`
- [e034] gate:sast-scan `SEMGREP_SETTINGS_FILE="${TMPDIR:-/tmp}/semgrep-settings.yml" SEMGREP_LOG_FILE="${TMPDIR:-/tmp}/semgrep.log" SEMGREP_VERSION_CACHE_PATH="${TMPDIR:-/tmp}/semgrep-version" semgrep scan --config p/default --config '<factory>/factory/rules/semgrep' --metrics=off --disable-version-check --disable-nosem --json --quiet --severity ERROR --severity WARNING -- ./factory/rules/semgrep/code-evaluated-from-strings.yml ./tests/test_eval_rule.py` exit 0, output sha256 `003d79d4fe59e222`, log `gate/sast-scan.log`
- [e035] gate:sast `SEMGREP_SETTINGS_FILE="${TMPDIR:-/tmp}/semgrep-settings.yml" SEMGREP_LOG_FILE="${TMPDIR:-/tmp}/semgrep.log" SEMGREP_VERSION_CACHE_PATH="${TMPDIR:-/tmp}/semgrep-version" semgrep scan --config p/default --config '<factory>/factory/rules/semgrep' --metrics=off --disable-version-check --disable-nosem --json --quiet --severity ERROR --severity WARNING -- ./factory/rules/semgrep/code-evaluated-from-strings.yml ./tests/test_eval_rule.py` exit none (timed out), output sha256 ``, log `gate/sast-scan.log`
- [e041] gate:tests `PYTHONPATH=. "<factory>/.venv/bin/python" -m pytest -q -rA -p no:cacheprovider` exit 0, output sha256 `a7a05e65fc3e1f25`, log `gate/tests.log`
- [e031] locked-test hash check: **pass**, 20 files

## Asserted, not evidence

The builder's own words. Nothing here was checked by running anything.

**Builder summary** (`builder-summary.md`):

> The gate and the factory check now flag `eval`, `new Function` and Python `exec` when an argument isn't a string literal. The full suite passes: 216 passed, 5 skipped, including all 15 tests in `tests/test_eval_rule.py`.
>
> **What I changed:** I added one file, `factory/rules/semgrep/code-evaluated-from-strings.yml`. I didn't change any code or tests. The gate's static scan (`gate.semgrep_cmd`) and the factory check (`stages/__init__.py`, `stages/tests.py`) already load every rule in `factory/rules/semgrep/`, so the new rules apply in both places. Like the SQL rule, they are marked ERROR, which both scans treat as blocking. The file has three rules:
>
> - **`factory.js-eval-of-a-built-string`** (JavaScript and TypeScript): flags `eval(...)` unless its first argument is a string literal.
> - **`factory.js-new-function-of-a-built-string`** (JavaScript and TypeScript): flags `new Function(...)` if any argument isn't a plain string literal. That includes the case where only the body is built at run time.
> - **`factory.python-eval-of-a-built-string`**: flags the built-in `eval` or `exec` unless its first argument is a string literal. Globals and locals arguments are allowed.
>
> Methods that share the name, such as `pattern.exec(text)` or `obj.eval(expr)`, aren't flagged, and neither is `Function(...)` without `new`.
>
> **What I ran:** the factory check (`.../build/check test`), twice.
> 1. **First run:** 4 failures. semgrep treated a variable that had been assigned a string literal (`const code = "1 + 1"`) as a literal, so `eval(code)` wasn't flagged. AC-1's note says a variable is flagged even if it holds a constant, so I turned that substitution off (`constant_propagation: false`) in all three rules and noted why in the file.
> 2. **Second run:** the check's own scans passed on the changed file, and the suite passed.
>
> **Things I'm unsure of:**
> - **Literals with escapes:** a JavaScript template literal with no `${...}` (for example `` eval(`1+1`) ``) is probably still flagged. The story doesn't cover that case and no test checks it. Two string literals joined with `+` are also flagged, which seems right since the argument is no longer a single literal.
> - **Repeated findings:** `new Function` with several non-literal arguments may be reported more than once on the same line. The tests compare sets of lines, so they wouldn't show this, and it doesn't change pass or fail.
> - **Documentation:** I didn't update the conformance documents, which mention the pinned rules (e.g. the ASI05 rows). They might now understate what the gate covers.
>
> No new dependency and no `rollback.md`; this change has no migration, delete or bulk update.

**Tests-leg summary** (`tests-summary.md`):

> I wrote 15 tests in `tests/test_eval_rule.py`. All 15 fail now because the behaviour is missing, and every existing test still passes. The factory check's scans passed on the new file. I made no changes outside `tests/`, and the work is uncommitted.
>
> To check each test fails for the right reason, I briefly added a wrapper that logged each test's error, then removed it and re-ran. Each test fails on its outcome: the pinned rules report nothing, `gate.sast` returns `pass`, or `check.main` returns 0. None fails from a syntax error or import problem. The wrapper left a log at `.factory-tmp/tests-brief-anqp0yqq/diag.txt`, outside the worktree. My shell can only run the check, so I couldn't delete it. It is not part of the change.
>
> Several tests also check a "positive control": a call the rule must flag, in the same scan or run, alongside the cases that must not be flagged. Without that, the "not flagged" and "passes" tests (AC-5, 6, 7, 10, 15) would pass today and prove nothing; with it, they fail until the rule exists. All tests skip if semgrep isn't installed, like the existing scanner tests.
>
> | AC | Test (all in `tests/test_eval_rule.py`) | What it asserts |
> |---|---|---|
> | AC-1 | `test_pinned_rules_flag_javascript_eval_of_a_built_string` | The pinned rules flag exactly the `eval` lines with a variable, a concatenation or a `${}` template, and not the constant declaration. |
> | AC-2 | `test_pinned_rules_flag_javascript_new_function_of_a_built_string` | `new Function` is flagged on every line where any argument is built: the body only, the last argument only, a concatenation, a template, or a built first argument. |
> | AC-3 | `test_pinned_rules_flag_typescript_eval_and_new_function` | In a `.ts` file, `eval(x)`, `new Function(x)` and `new Function("a", x)` are each flagged on their own line. |
> | AC-4 | `test_pinned_rules_flag_python_eval_and_exec_of_a_built_string` | Python `eval` and `exec` with a variable, f-string or concatenation are flagged, including calls that pass globals or locals (lines 2–8 exactly). |
> | AC-5 | `test_pinned_rules_do_not_flag_eval_of_a_string_literal` | Literal-only `eval`, `new Function` and `exec` in JS, TS and Python are not flagged; only the built-string control lines are. |
> | AC-6 | `test_pinned_rules_do_not_flag_methods_named_eval_or_exec` | `pattern.exec(text)`, `calc.eval(expr)`, `obj.eval(expr)` and `engine.exec(code)` are not flagged; only the control lines are. |
> | AC-7 | `test_sql_rule_results_are_unchanged_by_the_new_rule` | The SQL rule still reports only `bad.js:1`, `bad.js` gets exactly one finding from any rule, and static SQL in `ok.js` gets none. A built-string `eval` in the same scan is flagged. |
> | AC-8 | `test_gate_fails_a_change_that_adds_javascript_eval_of_a_variable` | `gate.sast` fails a change that adds `eval(input)`, and its reason contains `src/run.js:2`. |
> | AC-9 | `test_gate_fails_a_change_that_adds_python_exec_of_a_variable` | `gate.sast` fails a change that adds `exec(code)`, and its reason contains `src/run.py:4`. |
> | AC-10 | `test_gate_passes_a_change_that_adds_only_literal_eval` | Literal-only `eval`, `new Function` and `exec` pass with no findings and no preexisting count. Adding `exec(input())` to the same file then fails at `src/calc.py:3`. |
> | AC-11 | `test_gate_does_not_block_an_eval_already_present_at_the_baseline` | An `eval(input)` already in the file at the baseline, with the change only adding another line, passes with at least one preexisting finding recorded. |
> | AC-12 | `test_nosemgrep_comment_does_not_hide_an_eval_finding` | `eval(input); // nosemgrep` still fails `gate.sast`, and the reason contains `src/run.js:2`. |
> | AC-13 | `test_check_blocks_the_command_when_the_leg_adds_javascript_eval` | `check.main` returns `BLOCKED`, doesn't run the command, and prints the file name. This holds for `eval(input)` (`src/run.js`) and then for `new Function("a", body)` (`src/make.js`). |
> | AC-14 | `test_check_blocks_the_command_when_the_leg_adds_python_exec` | `check.main` returns `BLOCKED` and doesn't run the command for a Python `exec(code)`, then for `eval(code)`. |
> | AC-15 | `test_check_runs_the_command_when_the_leg_adds_only_literal_eval` | A built `exec(code)` blocks. Once the files hold only literal `exec`, `eval` and `new Function`, `check.main` returns 0 and the command runs. |

## Gates

| Check | Status | Event | Detail |
|---|---|---|---|
| tools | info | e030 |  |
| locked-tests | pass | e031 |  |
| secrets | pass | e032 | exit 0 |
| deps | skipped | e033 | the change touches no lockfile |
| sast-scan | pass | e034 | exit 0 |
| sast | pass | e035 | no findings |
| invisible | pass | e036 | no invisible or control characters added |
| install | skipped | e037 | commands.install is not configured |
| typecheck | skipped | e038 | commands.typecheck is not configured |
| lint | skipped | e039 | commands.lint is not configured |
| build | skipped | e040 | commands.build is not configured |
| tests | pass | e041 | exit 0 |
| perf | skipped | e042 | commands.perf is not configured |
| rollback | skipped | e043 | no class in risk.json requires a rollback (no migration or irreversible path or pattern) |
| surface | pass | e044 | the change edits no test-runner, scanner or agent-instruction file |
| added-tests | pass | e045 | the build added no test files |
| ratchet:semgrep_findings | pass | e046 |  |
| required | pass | e047 |  |
| unchanged | pass | e048 |  |
| theory-doc | info | e049 |  |

**Stage outcomes:**

- spec: ready (pass)
- tests: ready (pass)
- build: ready (pass)
- triage: ready (pass)
- gate: ready (pass)
- review: ready (pass)

## Ratchet

- [e046] semgrep_findings: 4 at baseline → 4 after the change (**pass**); `SEMGREP_SETTINGS_FILE="${TMPDIR:-/tmp}/semgrep-settings.yml" SEMGREP_LOG_FILE="${TMPDIR:-/tmp}/semgrep.log" SEMGREP_VERSION_CACHE_PATH="${TMPDIR:-/tmp}/semgrep-version" semgrep scan --config p/default --config '<factory>/factory/rules/semgrep' --metrics=off --disable-version-check --disable-nosem --json --quiet -- .`, output sha256 baseline `bec5182c98b75a9e`, after `bd012c87e1a352e0`

## Theory doc

- [e049] `DESIGN.md`: not changed

## Review

- [e054] reviewer-claude (claude-opus-5-5): pass, $0.55, 93.1 s
- [e056] reviewer-codex (gpt-6.1-sol): pass, 66699 tokens, 52.8 s
- [e058] sort (claude-opus-5-5): pass, $0.28, 29.3 s
- [e053] grounding: seeds (27 axis rows)

| ID | Severity | Verdict | Where | Claim | Sort reason | Resolution |
|---|---|---|---|---|---|---|
| F1 | low | confirmed | factory/rules/semgrep/code-evaluated-from-strings.yml:33 | The rules only match bare eval/exec calls and `new Function`, so equivalent forms such as `Function(body)` without `new`, `vm.runIn*`, string `setTimeout` and aliased or indirect eval get past the gat | code-evaluated-from-strings.yml:18 and :33 match only `eval($CODE, ...)` and `new Function(..., $ARG, ...)`, and the Python rule matches only bare `eval`/`exec`. Nothing covers `Function(...)` without | - |
| F2 | low | confirmed | conformance/llm-agentic.md:181 | The conformance records still say no eval/new Function/exec rule exists, even though this change adds one. | conformance/llm-agentic.md:181 still says "nothing targets unsafe evaluators" and lists the pinned eval/new Function/exec rule as PROPOSED. conformance/asvs-l1.md:58 still says "instruction only"/asse | - |

## Irreversible operations and rollback

- No migration or irreversible class.

## Residual risks

- [e037] gate:install skipped: commands.install is not configured
- [e038] gate:typecheck skipped: commands.typecheck is not configured
- [e039] gate:lint skipped: commands.lint is not configured
- [e040] gate:build skipped: commands.build is not configured
- [e042] gate:perf skipped: commands.perf is not configured
- F1 confirmed (low), below the blocking bar and unfixed: The rules only match bare eval/exec calls and `new Function`, so equivalent forms such as `Function(body)` without `new`, `vm.runIn*`, string `setTimeout` and aliased or indirect eval get past the gate and the check.
- F2 confirmed (low), below the blocking bar and unfixed: The conformance records still say no eval/new Function/exec rule exists, even though this change adds one.
- LLM or agent behaviour: deterministic gates don't cover model behaviour; watch it in production.
- [e049] the theory doc did not change; the reviewers were asked to flag behaviour it describes that the diff changed.
- [e013] the guard blocked 2 tests-leg tool calls: Blocked command: this leg's shell runs only the factory check, exactly as written: <scratch>…
- [e022] the guard blocked 1 build-leg tool calls: Blocked command: this leg's shell runs only the factory check, exactly as written: <scratch>…

## Sign-off

Accountable person: ______________________

Decision: [ ] sign   [ ] return

Reason (for a return): ______________________

Record the decision with `factory sign --change 20261014-135052-flag-code-that-evaluates-strings --by NAME` or `factory return --change 20261014-135052-flag-code-that-evaluates-strings --reason "..."`. The ledger records it with this pack's sha256. The harness never signs.
