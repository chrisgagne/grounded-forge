# Warranty pack: 20261014-172821-flag-code-that-evaluates-strings

**Change:** Flag code that evaluates strings built at run time  
**Repo:** `/private/tmp/claude-501/-Users-cgagne-Documents-LLM-Repos-repos-grounded-forge/9a408a34-2ce9-4109-807c-d2906a4c9c3a/scratchpad/showcase/factory` · **branch** `factory/20261014-172821-flag-code-that-evaluates-strings` · **baseline** `d2a55a5e6b8d` → **head** `efb202e1d675713ca3aaa291d4ea59192efd1375` (tree `7c2ad4528be2dbd63dd1827ccd35d35eef2e7d93`)  
**Builder:** claude  
**Assembled from ledger events** e001–e244 (`ledger.json`).

**Status:** READY TO SIGN

## Your decision

You're deciding whether to accept this change, with what's left over below, or send it back. You're not being asked whether the code is right: the checks and the two reviewers below answer that, against the rules listed at the end of this page. What only you can answer: is this what was asked for, and will you carry what's left over?

### What was asked for

> As the person who signs off a change, I want the gate and the factory check to flag a call to `eval`, `new Function`, or Python's `exec`, whose argument isn't a fixed string literal, so a change that adds one stops before it runs. A call with a plain string literal isn't flagged.

It was broken into 27 behaviours (written by an AI from the story; read them to check they're what was meant). Each has a test that failed before the change [e160] and passes now [e223]:

- AC-1: Scanning a JavaScript file with the factory's pinned rules reports a finding on the line of a call to `eval` whose argument is a variable, and on no other line.
- AC-2: Scanning a JavaScript file with the factory's pinned rules reports a finding on the line of `new Function(...)` whose body argument is a variable or a string built by concatenation or by a template literal with `${...}`.
- AC-3: Scanning a JavaScript file with the factory's pinned rules reports a finding for `eval` called with a string built at run time, either by concatenating a literal with a variable or by a template literal with `${...}`.
- AC-4: Scanning a TypeScript file with the factory's pinned rules flags `eval(x)` and `new Function(x)` just as it does in JavaScript.
- AC-5: Scanning a Python file with the factory's pinned rules reports a finding on the line of `eval(x)` and on the line of `exec(x)` when the argument is a variable, an f-string with a placeholder, or a concatenation with a variable, including calls that pass extra globals/locals arguments.
- AC-6: Scanning with the factory's pinned rules reports no finding for `eval("1 + 1")` or `new Function("return 1")` in JavaScript, or for `eval("1 + 1")` or `exec("x = 1")` in Python, when the argument is one plain string literal.
- AC-7: Scanning with the factory's pinned rules reports no eval finding for methods that only share the name: a regular-expression `pattern.exec(text)` in JavaScript, or `obj.eval(x)` / `obj.exec(x)` method calls in Python and JavaScript.
- AC-8: The eval/exec findings are reported at a severity the gate blocks on (ERROR or WARNING), with a message that names evaluation of a string built at run time.
- AC-9: When a change adds a line that calls `eval` on a variable in a JavaScript file, the gate's static scan fails, and its reason names the file and line.
- AC-10: When a change adds a line that calls `exec` on a variable in a Python file, the gate's static scan fails, and its reason names the file and line.
- AC-11: When a change adds only `eval`/`exec`/`new Function` calls whose argument is a plain string literal, the gate's static scan passes.
- AC-12: An `eval(x)` already present at the baseline isn't blamed on a change that only adds other lines to the same file: the gate's static scan passes and counts it as preexisting.
- AC-13: When the build leg's work adds a call to `eval`, `new Function` or Python `exec` on a non-literal argument, the factory check exits with its blocked code, names the finding, and doesn't run the requested command.
- AC-14: When the build leg's work adds only `eval`/`exec`/`new Function` calls on a plain string literal, the factory check runs the requested command.
- AC-15: A `nosemgrep` comment on the line of an `eval(x)` call doesn't stop the gate's static scan from failing.
- AC-16: The existing pinned SQL rule still behaves as before alongside the new rule: interpolated SQL passed to `prepare` is flagged and static or parameterised SQL is not, with no eval finding reported on either file.
- AC-17: Scanning a Python file with the factory's pinned rules reports no finding for `eval(...)` or `exec(...)` when the argument is fixed text written in any literal form: a raw string (`r"x = 1"`), a triple-quoted string (`"""1 + 1"""` or `'''x = 1'''`), a string with a `b`, `u` or `rb` prefix, an f-string with no placeholder, adjacent literals (`"x = " "1"`), or a concatenation of literals only (`"x = " + "1"`), including calls that pass extra globals/locals arguments.
- AC-18: Scanning a JavaScript or TypeScript file with the factory's pinned rules reports no finding for `eval(...)` or `new Function(...)` when the argument is fixed text written in any literal form: a single-quoted string, a template literal with no `${...}`, or a concatenation of literals only (`"return " + "1"`).
- AC-19: Scanning a JavaScript file with the factory's pinned rules reports a finding on the line of each of `globalThis.eval(x)`, `window.eval(x)`, the indirect call `(0, eval)(x)`, and a call through an alias of `eval` (`const run = eval; run(x)`), and reports no finding for the same calls when the argument is one plain string literal.
- AC-20: Scanning a Python file with the factory's pinned rules reports a finding on the line of `builtins.eval(x)` and on the line of `builtins.exec(x)` after `import builtins`, and reports no finding for the same calls when the argument is one plain string literal.
- AC-21: When a change adds only `eval`/`exec` calls whose argument is fixed text written as a Python raw, triple-quoted or prefixed string literal, the gate's static scan passes.
- AC-22: When a change adds a line that calls `globalThis.eval` on a variable in a JavaScript file, or `builtins.exec` on a variable in a Python file, the gate's static scan fails, and its reason names the file and line.
- AC-23: Scanning a JavaScript file with the factory's pinned rules reports a finding on the line of each of `eval.call(null, x)`, `eval.apply(null, [x])`, `Reflect.apply(eval, null, [x])`, `globalThis['eval'](x)` and `globalThis["eval"](x)`, where `x` is a variable.
- AC-24: Scanning a JavaScript file with the factory's pinned rules reports no finding for `eval.call(null, "1 + 1")`, `eval.apply(null, ["1 + 1"])`, `Reflect.apply(eval, null, ["1 + 1"])` or `globalThis['eval']("1 + 1")`, where the evaluated argument is one plain string literal.
- AC-25: Scanning a JavaScript file with the factory's pinned rules reports no eval finding for calls that only look similar: `Reflect.apply(fn, null, [x])` where `fn` is not `eval`, `fn.call(null, x)` / `fn.apply(null, [x])` on a function other than `eval`, and `obj['eval'](x)` on an object other than the global one.
- AC-26: When a change adds a line that calls `eval.call`, `eval.apply` or `Reflect.apply(eval, ...)` on a variable in a JavaScript file, the gate's static scan fails, and its reason names the file and line.
- AC-27: The pinned eval rule file says plainly which ways of running a string as code it does not follow, and names at least: a string passed to `setTimeout` or `setInterval`, Node's `vm` module (`vm.runInNewContext`, `vm.runInThisContext`, `new vm.Script`), an alias of `eval` or `Function` assigned after its declaration or by destructuring, and in Python an alias of `eval`/`exec` or a lookup such as `getattr(builtins, "exec")`. It no longer claims to cover `eval` "however reached".

### Did the checks pass?

- The tests written before the build weren't changed afterwards: yes [e213]
- No passwords, keys or tokens were added: yes [e214]
- The code scanner found no problem on the lines added: yes [e217]
- No hidden characters were added: yes [e218]
- All the project's tests pass, the new ones included: yes [e223]
- No test, scanner or AI-instruction files were changed: yes [e226]
- The builder added no test file that could interfere with the locked tests: yes [e227]
- No scanner count rose: yes [e228]
- Every check this kind of change needs was run: yes [e229]
- The code didn't change while it was being checked: yes [e230]
- Not checked, because the project has no such command: install, typecheck, lint, build, perf.
- Two independent AI reviewers (one from Anthropic, one from OpenAI) read the change; neither rated anything serious.

### What's left over

- Minor (F1, the reviewers' words): The conformance records still describe the eval rule as unbuilt, so they no longer match what the gate enforces. **The sorting AI says this goes against the story itself.**
- Minor (F2, the reviewers' words): A Function alias declared with its value (`const F = Function; new F(x)`) is not flagged, and the 'not followed' list doesn't name it. **The sorting AI says this misses AC-27: "The pinned eval rule file says plainly which ways of running a string as code it does not follow, and names at least: a string passed to `setTimeout` or `setInterval`, Node's `vm` module (`vm.runInNewContext`, `vm.runInThisContext`, `new vm.Script`), an alias of `eval` or `Function` assigned after its declaration or by destructuring, and in Python an alias of `eval`/`exec` or a lookup such as `getattr(builtins, "exec")`. It no longer claims to cover `eval` "however reached"."**
- Minor (F3, the reviewers' words): Reaching the Function constructor through `.constructor` (e.g. `(function(){}).constructor(x)`) isn't flagged and isn't named as not followed.
- The reviewers disagreed (F4, minor): Because semgrep's constant propagation stays on, `const code = "1+1"; eval(code)` may be excluded by the `"..."` metavariable-pattern.
- LLM or agent behaviour: deterministic gates don't cover model behaviour; watch it in production.
- Undo: revert this change; nothing in it is one-way.

### Does this need someone else?

- No: nothing in it reaches personal data, money, sign-in, the database's structure or a step that can't be undone.

### Within the rules?

- Yes: every check the rules require passed or was accepted, and nothing is open above the bar.

The rules (6, in `factory/policy.yaml`); 6 are PROPOSED and not yet confirmed by you:

- A finding the review confirms as critical or high stops the change until it's fixed or you accept it. *PROPOSED; set by Claude, in the factory's design (2026-10-11).*
- If either reviewer rated a finding critical or high, the AI that sorts the findings can't clear it on its own: it stays a stop until you decide. *PROPOSED; set by Claude, from the source (2026-10-12).*
- Where a change reaches personal data or a step that can't be undone (a delete, a drop), a confirmed medium finding stops it too. *PROPOSED; set by Claude's recommendation; Chris Gagné asked for it to be added (2026-10-14).*
- A change that reaches personal data, money, sign-in or a step that can't be undone needs a qualified second person before real use; the decision page names what they should check. *PROPOSED; set by Claude (2026-10-14).*
- The code scanner stops a change only for problems on lines it adds; problems already in a file are recorded, and their count may not rise. *PROPOSED; set by Claude (2026-10-14).*
- On the real-bug replay, the factory should catch at least 80% of bug trials, catch at least 70% of bug cases every time (3 of 3), get at least 95% of defects in front of you, block at most 20% of clean-change trials, and pass at least 80% of clean changes every time. *PROPOSED; set by Claude's recommendation; Chris Gagné handed the numbers to Claude (2026-10-14).*

### Your choices

- **Sign it (accept the change):** `factory sign --change 20261014-172821-flag-code-that-evaluates-strings --by NAME` records your name, the time and this pack's fingerprint.
- **Send back:** `factory return --change 20261014-172821-flag-code-that-evaluates-strings --by NAME --reason "..."`, in your own words. What you ask for gets new behaviours and locked tests first, then the builder gets your reason.
- **Ask first:** ask about any line. Nothing is recorded until you sign or send it back.

# The evidence

## Story

> # Flag code that evaluates strings built at run time
>
> The factory's pinned semgrep rules (`factory/rules/semgrep/`) catch SQL built from strings, but nothing catches code that evaluates a string assembled at run time: JavaScript's `eval(x)` and `new Function(x)`, or Python's `eval(x)` and `exec(x)`. The OWASP Top 10 for Agentic Applications (ASI05) names this as a way generated code runs something nobody reviewed.
>
> As the person who signs off a change, I want the gate and the factory check to flag a call to `eval`, `new Function`, or Python's `exec`, whose argument isn't a fixed string literal, so a change that adds one stops before it runs. A call with a plain string literal isn't flagged.

## Risk classes

- **llm-agent**: keyword in story/acceptance: agentic. Required gates: none beyond the standard gates. Review focus: OWASP Top 10 for LLM Applications 2026 and OWASP Top 10 for Agentic Applications 2026: prompt injection, excessive agency, tool misuse, data leaking through the model.

Triage: pass (e210), phase diff.

## Demonstrated

Commands the driver ran, with exit codes and output hashes.

- [e155] tests:suite-before `PYTHONPATH=. "/Users/cgagne/Documents/LLM Repos/repos/factory/.venv/bin/python" -m pytest -q -rA -p no:cacheprovider` exit 0, output sha256 `f734a73224163371`, log `tests/suite-before.log`
- [e160] tests:new-tests `PYTHONPATH=. "/Users/cgagne/Documents/LLM Repos/repos/factory/.venv/bin/python" -m pytest -q -rA -p no:cacheprovider` exit 1 (expected: red before the build), output sha256 `04fb910059fbe223`, log `tests/new-tests.log`
- [e214] gate:secrets `gitleaks git --no-banner --redact --ignore-gitleaks-allow --log-opts=d2a55a5e6b8db26811d7f0032828525c75ff65d3..HEAD --report-format json --report-path /private/tmp/claude-501/-Users-cgagne-Documents-LLM-Repos-repos-grounded-forge/9a408a34-2ce9-4109-807c-d2906a4c9c3a/scratchpad/showcase/factory/.factory/changes/20261014-172821-flag-code-that-evaluates-strings/gate/gitleaks.json .` exit 0, output sha256 `bd56dca3830f9a84`, log `gate/secrets.log`
- [e216] gate:sast-scan `SEMGREP_SETTINGS_FILE="${TMPDIR:-/tmp}/semgrep-settings.yml" SEMGREP_LOG_FILE="${TMPDIR:-/tmp}/semgrep.log" SEMGREP_VERSION_CACHE_PATH="${TMPDIR:-/tmp}/semgrep-version" semgrep scan --config p/default --config '/Users/cgagne/Documents/LLM Repos/repos/factory/factory/rules/semgrep' --metrics=off --disable-version-check --disable-nosem --json --quiet --severity ERROR --severity WARNING -- ./factory/rules/semgrep/eval-of-built-strings.yml ./tests/test_check.py ./tests/test_eval_rule_after_send_back.py ./tests/test_eval_rule_second_send_back.py ./tests/test_gate_hardening.py ./tests/test_pinned_eval_rule.py` exit 0, output sha256 `ce8a1eb904916fe0`, log `gate/sast-scan.log`
- [e217] gate:sast `SEMGREP_SETTINGS_FILE="${TMPDIR:-/tmp}/semgrep-settings.yml" SEMGREP_LOG_FILE="${TMPDIR:-/tmp}/semgrep.log" SEMGREP_VERSION_CACHE_PATH="${TMPDIR:-/tmp}/semgrep-version" semgrep scan --config p/default --config '/Users/cgagne/Documents/LLM Repos/repos/factory/factory/rules/semgrep' --metrics=off --disable-version-check --disable-nosem --json --quiet --severity ERROR --severity WARNING -- ./factory/rules/semgrep/eval-of-built-strings.yml ./tests/test_check.py ./tests/test_eval_rule_after_send_back.py ./tests/test_eval_rule_second_send_back.py ./tests/test_gate_hardening.py ./tests/test_pinned_eval_rule.py` exit none (timed out), output sha256 ``, log `gate/sast-scan.log`
- [e223] gate:tests `PYTHONPATH=. "/Users/cgagne/Documents/LLM Repos/repos/factory/.venv/bin/python" -m pytest -q -rA -p no:cacheprovider` exit 0, output sha256 `6ad19124ab8478d3`, log `gate/tests.log`
- [e213] locked-test hash check: **pass**, 23 files

## Asserted, not evidence

The builder's own words. Nothing here was checked by running anything.

**Builder summary** (`builder-summary.md`):

> The rule now catches `eval.call`, `eval.apply`, `Reflect.apply(eval, ...)` and `globalThis['eval']` when they're given a built string. Its header no longer claims more than the rule catches, and it lists the forms it doesn't follow. The factory check passed its scans and ran the test command: **233 passed, 5 skipped, 0 failed**. The 5 skipped tests are all in `tests/test_isolation.py` and need `sandbox-exec`. All the semgrep tests ran, including the new AC-23 to AC-27 ones.
>
> ## What I changed
> Only one file: `factory/rules/semgrep/eval-of-built-strings.yml`.
>
> **New ways the JavaScript/TypeScript rule matches eval** (this covers F1 and the returned note):
> - `eval.call($THIS, $ARG, ...)`
> - `eval.apply($THIS, [$ARG, ...])` and `Reflect.apply(eval, $THIS, [$ARG, ...])`. The existing check on `$ARG` still runs, so a single plain literal like `["1 + 1"]` isn't flagged.
> - `eval.apply(null, args)` and `Reflect.apply(eval, null, args)`, where the argument list is a variable rather than written out. An argument list like that is itself built at run time. No test asks for this; I added it because without it, a variable argument list would be a one-step way around the `[x]` form.
> - `$G[$NAME](...)` where `$G` is `globalThis`, `window`, `self` or `global` and `$NAME` is exactly the quoted string `eval`. That means `obj['eval'](x)` and `globalThis[otherKey](x)` aren't flagged.
>
> Lookalike calls (`fn.call`, `fn.apply`, `Reflect.apply(fn, ...)`, `obj['eval']`) don't match any of these patterns.
>
> **Header comment:** it now lists exactly what's covered. A new "Not followed, so not flagged" paragraph names everything AC-27 requires:
> - `setTimeout` and `setInterval`
> - `vm.runInNewContext`, `vm.runInThisContext` and `new vm.Script`
> - aliases assigned after their declaration or taken by destructuring
> - Python aliases of `eval`/`exec`, and lookups like `getattr(builtins, "exec")`
>
> It also names a few other gaps: `vm.compileFunction`, `__builtins__["eval"]`, `compile()`, aliases of `globalThis.eval`, and `Function` reached through call/apply/Reflect. The phrase "however reached" isn't in the file.
>
> ## Things I'm unsure about
> - **Computed names:** the match on the name only works when the key is written right in the call, like `globalThis['eval']`. A key held in a variable (`const k = 'eval'; globalThis[k](x)`) isn't caught. The comment's list of gaps doesn't name this one.
> - **F4 isn't addressed:** the conformance docs still describe the rule as unbuilt. The story leaves that out on purpose.
> - The locked tests all looked right to me. I didn't add any tests of my own, and I didn't add any dependencies.

**Tests-leg summary** (`tests-summary.md`):

> I wrote five tests, one for each of AC-23 to AC-27, all in `tests/test_eval_rule_second_send_back.py`. I ran the factory check: its scans passed, and the suite then failed only on three of my new tests (AC-23, AC-26, AC-27). Each fails because the behaviour is missing, not because of a syntax or import error. Every other test passed or was skipped, including all the locked ones.
>
> | Criterion | File | Test | What it asserts | Result now |
> |---|---|---|---|---|
> | AC-23 | `tests/test_eval_rule_second_send_back.py` | `test_js_eval_reached_through_call_apply_reflect_or_a_computed_name_is_flagged` | Scanning a JS file with the pinned rules flags exactly lines 2–6: `eval.call(null, x)`, `eval.apply(null, [x])`, `Reflect.apply(eval, null, [x])`, `globalThis['eval'](x)` and `globalThis["eval"](x)`. Nothing else is flagged. | Fails: no findings at all |
> | AC-24 | `tests/test_eval_rule_second_send_back.py` | `test_js_eval_reached_through_call_apply_reflect_or_a_computed_name_on_a_literal_is_not_flagged` | The same five calls with the argument `"1 + 1"` produce no findings. | Passes |
> | AC-25 | `tests/test_eval_rule_second_send_back.py` | `test_js_lookalike_call_apply_reflect_and_computed_calls_are_not_flagged` | `Reflect.apply(fn, null, [x])`, `fn.call(null, x)`, `fn.apply(null, [x])`, `obj['eval'](x)` and `obj["eval"](x)` produce no findings. | Passes |
> | AC-26 | `tests/test_eval_rule_second_send_back.py` | `test_gate_sast_fails_on_an_added_eval_call_apply_or_reflect_apply_of_a_variable` | Three separate changes each add one of `eval.call`, `eval.apply` or `Reflect.apply(eval, ...)` on a variable. For each, `gate.sast` returns `fail` and its reason contains `src/run.js:2`. | Fails: the gate passes the `eval.call` change |
> | AC-27 | `tests/test_eval_rule_second_send_back.py` | `test_the_rule_file_states_what_it_does_not_follow` | The pinned rule file holding an eval rule (found by rule id, not file name) names `setTimeout`, `setInterval`, `vm.runInNewContext`, `vm.runInThisContext` and `vm.Script`. It also mentions aliases and destructuring and `getattr(builtins`, and no longer says "however reached". | Fails: no mention of `setTimeout` |
>
> - **AC-24 and AC-25 pass already.** They describe things the rule must not flag, and the current rule doesn't flag them. They are there so the build leg can't satisfy AC-23 by flagging too much.
> - **AC-27 checks less than the criterion says.** It looks for keywords anywhere in the rule file, not for exact wording. It doesn't separately check for an alias assigned after its declaration or a Python alias of `eval`/`exec`; one mention of "alias" counts for both. Because it reads the whole file, a pattern that mentions `setTimeout` would satisfy it as well as a comment would.

## Gates

| Check | Status | Event | Detail |
|---|---|---|---|
| tools | info | e212 |  |
| locked-tests | pass | e213 |  |
| secrets | pass | e214 | exit 0 |
| deps | skipped | e215 | the change touches no lockfile |
| sast-scan | pass | e216 | exit 0 |
| sast | pass | e217 | no finding on an added line; 1 finding(s) already in the touched files |
| invisible | pass | e218 | no invisible or control characters added |
| install | skipped | e219 | commands.install is not configured |
| typecheck | skipped | e220 | commands.typecheck is not configured |
| lint | skipped | e221 | commands.lint is not configured |
| build | skipped | e222 | commands.build is not configured |
| tests | pass | e223 | exit 0 |
| perf | skipped | e224 | commands.perf is not configured |
| rollback | skipped | e225 | no class in risk.json requires a rollback (no migration or irreversible path or pattern) |
| surface | pass | e226 | the change edits no test-runner, scanner or agent-instruction file |
| added-tests | pass | e227 | the build added no test files |
| ratchet:semgrep_findings | pass | e228 |  |
| required | pass | e229 |  |
| unchanged | pass | e230 |  |
| theory-doc | info | e231 |  |

**Stage outcomes:**

- spec: ready (pass)
- tests: ready (pass)
- build: ready (pass)
- triage: ready (pass)
- gate: ready (pass)
- review: ready (pass)

## Ratchet

- [e228] semgrep_findings: 4 at baseline → 4 after the change (**pass**); `SEMGREP_SETTINGS_FILE="${TMPDIR:-/tmp}/semgrep-settings.yml" SEMGREP_LOG_FILE="${TMPDIR:-/tmp}/semgrep.log" SEMGREP_VERSION_CACHE_PATH="${TMPDIR:-/tmp}/semgrep-version" semgrep scan --config p/default --config '/Users/cgagne/Documents/LLM Repos/repos/factory/factory/rules/semgrep' --metrics=off --disable-version-check --disable-nosem --json --quiet -- .`, output sha256 baseline `8cdbf47086033df7`, after `989bf28a596ccf59`

## Theory doc

- [e231] `DESIGN.md`: not changed

## Review

- [e236] reviewer-claude (claude-opus-5-5): pass, $0.75, 137.1 s
- [e238] reviewer-codex (gpt-6.1-sol): pass, 61858 tokens, 119.3 s
- [e240] sort (claude-opus-5-5): pass, $0.21, 560.3 s
- [e235] grounding: seeds (27 axis rows)

| ID | Severity | Verdict | Where | Claim | Sort reason | Resolution |
|---|---|---|---|---|---|---|
| F1 | low | confirmed | conformance/asvs-l1.md:58 | The conformance records still describe the eval rule as unbuilt, so they no longer match what the gate enforces. | conformance/asvs-l1.md:58 still reads 'instruction only' / 'asserted' / 'PROPOSED: a pinned rule for eval, new Function...', and conformance/llm-agentic.md:181 (ASI05.2) still says nothing targets uns | - |
| F2 | low | confirmed | factory/rules/semgrep/eval-of-built-strings.yml:9 | A Function alias declared with its value (`const F = Function; new F(x)`) is not flagged, and the 'not followed' list doesn't name it. | The only alias patterns (yml:63-74) bind `$ALIAS = eval`, and there is no `new $ALIAS(...)` form. The not-followed list (yml:8-13) names only Function aliases assigned after declaration or taken by de | - |
| F3 | low | confirmed | factory/rules/semgrep/eval-of-built-strings.yml:11 | Reaching the Function constructor through `.constructor` (e.g. `(function(){}).constructor(x)`) isn't flagged and isn't named as not followed. | The patterns at yml:32-74 match only `Function`, `new Function` and `$G.Function` with $G restricted to the global objects. The not-followed list at yml:8-13 covers call/apply/Reflect and computed nam | - |
| F4 | low | disputed | factory/rules/semgrep/eval-of-built-strings.yml:76 | Because semgrep's constant propagation stays on, `const code = "1+1"; eval(code)` may be excluded by the `"..."` metavariable-pattern. | The metavariable-pattern at yml:76-81 and 101-106 excludes `"..."` and does not turn off constant propagation, which semgrep can apply to identifiers. No test covers a const variable that holds a lite | - |
| F5 | low | noise | tests/test_pinned_eval_rule.py:13 | The eval acceptance tests are skipped when semgrep isn't installed. | tests/test_pinned_eval_rule.py:13 does skip when semgrep is missing. The existing SQL-rule tests use the same convention (tests/test_gate_tools.py:11 skips when a scanner is missing). A skipped test i | - |

## Irreversible operations and rollback

- No migration or irreversible class.

## Residual risks

- [e219] gate:install skipped: commands.install is not configured
- [e220] gate:typecheck skipped: commands.typecheck is not configured
- [e221] gate:lint skipped: commands.lint is not configured
- [e222] gate:build skipped: commands.build is not configured
- [e224] gate:perf skipped: commands.perf is not configured
- F1 confirmed (low), below the blocking bar and unfixed: The conformance records still describe the eval rule as unbuilt, so they no longer match what the gate enforces.
- F2 confirmed (low), below the blocking bar and unfixed: A Function alias declared with its value (`const F = Function; new F(x)`) is not flagged, and the 'not followed' list doesn't name it.
- F3 confirmed (low), below the blocking bar and unfixed: Reaching the Function constructor through `.constructor` (e.g. `(function(){}).constructor(x)`) isn't flagged and isn't named as not followed.
- F4 disputed (low): Because semgrep's constant propagation stays on, `const code = "1+1"; eval(code)` may be excluded by the `"..."` metavariable-pattern.
- LLM or agent behaviour: deterministic gates don't cover model behaviour; watch it in production.
- [e231] the theory doc did not change; the reviewers were asked to flag behaviour it describes that the diff changed.
- [e013] the guard blocked 2 tests-leg tool calls: Blocked command: this leg's shell runs only the factory check, exactly as written: /private/tmp/claude-501/-Users-cgagne-Documents-LLM-Repos-repos-grounded-forg
- [e022] the guard blocked 1 build-leg tool calls: Blocked command: this leg's shell runs only the factory check, exactly as written: /private/tmp/claude-501/-Users-cgagne-Documents-LLM-Repos-repos-grounded-forg
- [e079] the guard blocked 3 tests-leg tool calls: Blocked command: this leg's shell runs only the factory check, exactly as written: /private/tmp/claude-501/-Users-cgagne-Documents-LLM-Repos-repos-grounded-forg; Blocked: /tmp/claude-501/-Users-cgagne-Documents-LLM-Repos-repos-grounded-forge/9a408a34-2ce9-4109-807c-d2906a4c9c3a/scratchpad/showcase/.factory-worktrees/fact
- [e094] the guard blocked 1 tests-leg tool calls: Blocked command: this leg's shell runs only the factory check, exactly as written: /private/tmp/claude-501/-Users-cgagne-Documents-LLM-Repos-repos-grounded-forg
- [e158] the guard blocked 1 tests-leg tool calls: Blocked command: this leg's shell runs only the factory check, exactly as written: /private/tmp/claude-501/-Users-cgagne-Documents-LLM-Repos-repos-grounded-forg

## Sign-off

Accountable person: ______________________

Decision: [ ] sign   [ ] return

Reason (for a return): ______________________

Record the decision with `factory sign --change 20261014-172821-flag-code-that-evaluates-strings --by NAME` or `factory return --change 20261014-172821-flag-code-that-evaluates-strings --reason "..."`. The ledger records it with this pack's sha256. The harness never signs.
