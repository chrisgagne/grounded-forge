I'm reading how the gate's static scan and the factory check use the pinned rules, so I can write acceptance criteria tied to tests.

## AC-1: Scanning a JavaScript file with the factory's pinned rules reports a finding on each line that calls `eval` with an argument that isn't a string literal: a variable, a string concatenation, or a template literal containing `${...}`.
check: tests/test_eval_rule.py :: test_pinned_rules_flag_javascript_eval_of_a_built_string
assumption: an argument counts as "fixed" only if it is a string literal at the call site. A variable is flagged even if it holds a constant.

## AC-2: Scanning a JavaScript file with the factory's pinned rules reports a finding on each line that calls `new Function(...)` where any argument isn't a string literal, including when only the last argument (the function body) is built at run time.
check: tests/test_eval_rule.py :: test_pinned_rules_flag_javascript_new_function_of_a_built_string
assumption: only `new Function(...)` is covered, as the story names it. Calling `Function(...)` without `new` is out of scope.

## AC-3: Scanning a TypeScript file with the factory's pinned rules reports `eval(x)` and `new Function(x)` with a non-literal argument the same way it does for JavaScript.
check: tests/test_eval_rule.py :: test_pinned_rules_flag_typescript_eval_and_new_function

## AC-4: Scanning a Python file with the factory's pinned rules reports a finding on each line that calls the built-in `eval` or `exec` with a first argument that isn't a string literal: a variable, an f-string, or a concatenation. This includes calls that also pass globals or locals.
check: tests/test_eval_rule.py :: test_pinned_rules_flag_python_eval_and_exec_of_a_built_string

## AC-5: Scanning with the factory's pinned rules reports no finding for `eval`, `new Function`, or Python `exec` when every argument is a plain string literal, for example `eval("1 + 1")`, `new Function("return 1")` and `exec("x = 1")`.
check: tests/test_eval_rule.py :: test_pinned_rules_do_not_flag_eval_of_a_string_literal

## AC-6: Scanning with the factory's pinned rules reports no finding for a method that happens to be called `exec` or `eval` on some object, such as a JavaScript regular expression's `pattern.exec(text)` or a Python object's `obj.eval(expr)`.
check: tests/test_eval_rule.py :: test_pinned_rules_do_not_flag_methods_named_eval_or_exec
assumption: only the global `eval`/`exec` and `new Function` are in scope. Methods with these names on other objects are not.

## AC-7: The existing SQL rule's results are unchanged: interpolated SQL passed to `db.prepare` is still reported once, and static SQL passed to `db.exec(...)` or `db.prepare(...)` with a bound parameter is still not reported, by any pinned rule.
check: tests/test_eval_rule.py :: test_sql_rule_results_are_unchanged_by_the_new_rule

## AC-8: When a change adds a JavaScript line that calls `eval` on a non-literal argument, the gate's static scan fails, and its reason names the file and line of the call.
check: tests/test_eval_rule.py :: test_gate_fails_a_change_that_adds_javascript_eval_of_a_variable

## AC-9: When a change adds a Python line that calls `exec` on a non-literal argument, the gate's static scan fails, and its reason names the file and line of the call.
check: tests/test_eval_rule.py :: test_gate_fails_a_change_that_adds_python_exec_of_a_variable

## AC-10: When a change adds only `eval`/`new Function`/`exec` calls whose arguments are string literals, the gate's static scan passes and reports no errors from the pinned rules.
check: tests/test_eval_rule.py :: test_gate_passes_a_change_that_adds_only_literal_eval

## AC-11: If an `eval(x)` with a non-literal argument was already in a file at the baseline and the change only adds other lines to that file, the gate's static scan passes and records the finding as already there.
check: tests/test_eval_rule.py :: test_gate_does_not_block_an_eval_already_present_at_the_baseline

## AC-12: A `nosemgrep` comment on a line that calls `eval` on a non-literal argument doesn't stop the gate's static scan from failing the change.
check: tests/test_eval_rule.py :: test_nosemgrep_comment_does_not_hide_an_eval_finding

## AC-13: When a build leg has added a JavaScript `eval` or `new Function` call on a non-literal argument, the factory check exits with its blocked code, does not run the requested command, and names the file in its message.
check: tests/test_eval_rule.py :: test_check_blocks_the_command_when_the_leg_adds_javascript_eval

## AC-14: When a build leg has added a Python `eval` or `exec` call on a non-literal argument, the factory check exits with its blocked code and does not run the requested command.
check: tests/test_eval_rule.py :: test_check_blocks_the_command_when_the_leg_adds_python_exec

## AC-15: When a build leg has added only `eval`/`new Function`/`exec` calls whose arguments are string literals, the factory check runs the requested command.
check: tests/test_eval_rule.py :: test_check_runs_the_command_when_the_leg_adds_only_literal_eval
