## AC-1: Scanning a JavaScript file with the factory's pinned rules reports a finding on the line of a call to `eval` whose argument is a variable, and on no other line.
check: tests/test_pinned_eval_rule.py :: test_js_eval_of_a_variable_is_flagged

## AC-2: Scanning a JavaScript file with the factory's pinned rules reports a finding on the line of `new Function(...)` whose body argument is a variable or a string built by concatenation or by a template literal with `${...}`.
check: tests/test_pinned_eval_rule.py :: test_js_new_function_of_a_built_string_is_flagged

## AC-3: Scanning a JavaScript file with the factory's pinned rules reports a finding for `eval` called with a string built at run time, either by concatenating a literal with a variable or by a template literal with `${...}`.
check: tests/test_pinned_eval_rule.py :: test_js_eval_of_a_concatenated_or_interpolated_string_is_flagged

## AC-4: Scanning a TypeScript file with the factory's pinned rules flags `eval(x)` and `new Function(x)` just as it does in JavaScript.
check: tests/test_pinned_eval_rule.py :: test_ts_eval_and_new_function_of_a_variable_are_flagged

## AC-5: Scanning a Python file with the factory's pinned rules reports a finding on the line of `eval(x)` and on the line of `exec(x)` when the argument is a variable, an f-string with a placeholder, or a concatenation with a variable, including calls that pass extra globals/locals arguments.
check: tests/test_pinned_eval_rule.py :: test_python_eval_and_exec_of_a_built_string_are_flagged

## AC-6: Scanning with the factory's pinned rules reports no finding for `eval("1 + 1")` or `new Function("return 1")` in JavaScript, or for `eval("1 + 1")` or `exec("x = 1")` in Python, when the argument is one plain string literal.
check: tests/test_pinned_eval_rule.py :: test_a_plain_string_literal_argument_is_not_flagged

## AC-7: Scanning with the factory's pinned rules reports no eval finding for methods that only share the name: a regular-expression `pattern.exec(text)` in JavaScript, or `obj.eval(x)` / `obj.exec(x)` method calls in Python and JavaScript.
check: tests/test_pinned_eval_rule.py :: test_methods_named_eval_or_exec_are_not_flagged

## AC-8: The eval/exec findings are reported at a severity the gate blocks on (ERROR or WARNING), with a message that names evaluation of a string built at run time.
check: tests/test_pinned_eval_rule.py :: test_eval_finding_is_blocking_and_says_what_it_found

## AC-9: When a change adds a line that calls `eval` on a variable in a JavaScript file, the gate's static scan fails, and its reason names the file and line.
check: tests/test_gate_hardening.py :: test_gate_sast_fails_on_an_added_js_eval_of_a_variable

## AC-10: When a change adds a line that calls `exec` on a variable in a Python file, the gate's static scan fails, and its reason names the file and line.
check: tests/test_gate_hardening.py :: test_gate_sast_fails_on_an_added_python_exec_of_a_variable

## AC-11: When a change adds only `eval`/`exec`/`new Function` calls whose argument is a plain string literal, the gate's static scan passes.
check: tests/test_gate_hardening.py :: test_gate_sast_passes_on_eval_of_a_string_literal

## AC-12: An `eval(x)` already present at the baseline isn't blamed on a change that only adds other lines to the same file: the gate's static scan passes and counts it as preexisting.
check: tests/test_gate_hardening.py :: test_a_preexisting_eval_does_not_block_a_change

## AC-13: When the build leg's work adds a call to `eval`, `new Function` or Python `exec` on a non-literal argument, the factory check exits with its blocked code, names the finding, and doesn't run the requested command.
check: tests/test_check.py :: test_an_added_eval_of_a_variable_stops_the_command

## AC-14: When the build leg's work adds only `eval`/`exec`/`new Function` calls on a plain string literal, the factory check runs the requested command.
check: tests/test_check.py :: test_an_added_eval_of_a_string_literal_lets_the_command_run

## AC-15: A `nosemgrep` comment on the line of an `eval(x)` call doesn't stop the gate's static scan from failing.
check: tests/test_gate_hardening.py :: test_nosemgrep_does_not_hide_an_eval_finding

## AC-16: The existing pinned SQL rule still behaves as before alongside the new rule: interpolated SQL passed to `prepare` is flagged and static or parameterised SQL is not, with no eval finding reported on either file.
check: tests/test_gate_tools.py :: test_pinned_rule_flags_interpolated_sql_but_not_static_sql

## AC-17: Scanning a Python file with the factory's pinned rules reports no finding for `eval(...)` or `exec(...)` when the argument is fixed text written in any literal form: a raw string (`r"x = 1"`), a triple-quoted string (`"""1 + 1"""` or `'''x = 1'''`), a string with a `b`, `u` or `rb` prefix, an f-string with no placeholder, adjacent literals (`"x = " "1"`), or a concatenation of literals only (`"x = " + "1"`), including calls that pass extra globals/locals arguments.
check: tests/test_eval_rule_after_send_back.py :: test_python_fixed_text_in_any_literal_form_is_not_flagged

## AC-18: Scanning a JavaScript or TypeScript file with the factory's pinned rules reports no finding for `eval(...)` or `new Function(...)` when the argument is fixed text written in any literal form: a single-quoted string, a template literal with no `${...}`, or a concatenation of literals only (`"return " + "1"`).
check: tests/test_eval_rule_after_send_back.py :: test_js_and_ts_fixed_text_in_any_literal_form_is_not_flagged

## AC-19: Scanning a JavaScript file with the factory's pinned rules reports a finding on the line of each of `globalThis.eval(x)`, `window.eval(x)`, the indirect call `(0, eval)(x)`, and a call through an alias of `eval` (`const run = eval; run(x)`), and reports no finding for the same calls when the argument is one plain string literal.
check: tests/test_eval_rule_after_send_back.py :: test_js_other_ways_of_calling_eval_on_a_built_string_are_flagged

## AC-20: Scanning a Python file with the factory's pinned rules reports a finding on the line of `builtins.eval(x)` and on the line of `builtins.exec(x)` after `import builtins`, and reports no finding for the same calls when the argument is one plain string literal.
check: tests/test_eval_rule_after_send_back.py :: test_python_builtins_eval_and_exec_of_a_built_string_are_flagged

## AC-21: When a change adds only `eval`/`exec` calls whose argument is fixed text written as a Python raw, triple-quoted or prefixed string literal, the gate's static scan passes.
check: tests/test_eval_rule_after_send_back.py :: test_gate_sast_passes_on_eval_of_fixed_text_in_any_literal_form

## AC-22: When a change adds a line that calls `globalThis.eval` on a variable in a JavaScript file, or `builtins.exec` on a variable in a Python file, the gate's static scan fails, and its reason names the file and line.
check: tests/test_eval_rule_after_send_back.py :: test_gate_sast_fails_on_an_added_qualified_eval_or_exec_of_a_variable

## AC-23: Scanning a JavaScript file with the factory's pinned rules reports a finding on the line of each of `eval.call(null, x)`, `eval.apply(null, [x])`, `Reflect.apply(eval, null, [x])`, `globalThis['eval'](x)` and `globalThis["eval"](x)`, where `x` is a variable.
check: tests/test_eval_rule_second_send_back.py :: test_js_eval_reached_through_call_apply_reflect_or_a_computed_name_is_flagged

## AC-24: Scanning a JavaScript file with the factory's pinned rules reports no finding for `eval.call(null, "1 + 1")`, `eval.apply(null, ["1 + 1"])`, `Reflect.apply(eval, null, ["1 + 1"])` or `globalThis['eval']("1 + 1")`, where the evaluated argument is one plain string literal.
check: tests/test_eval_rule_second_send_back.py :: test_js_eval_reached_through_call_apply_reflect_or_a_computed_name_on_a_literal_is_not_flagged

## AC-25: Scanning a JavaScript file with the factory's pinned rules reports no eval finding for calls that only look similar: `Reflect.apply(fn, null, [x])` where `fn` is not `eval`, `fn.call(null, x)` / `fn.apply(null, [x])` on a function other than `eval`, and `obj['eval'](x)` on an object other than the global one.
check: tests/test_eval_rule_second_send_back.py :: test_js_lookalike_call_apply_reflect_and_computed_calls_are_not_flagged

## AC-26: When a change adds a line that calls `eval.call`, `eval.apply` or `Reflect.apply(eval, ...)` on a variable in a JavaScript file, the gate's static scan fails, and its reason names the file and line.
check: tests/test_eval_rule_second_send_back.py :: test_gate_sast_fails_on_an_added_eval_call_apply_or_reflect_apply_of_a_variable

## AC-27: The pinned eval rule file says plainly which ways of running a string as code it does not follow, and names at least: a string passed to `setTimeout` or `setInterval`, Node's `vm` module (`vm.runInNewContext`, `vm.runInThisContext`, `new vm.Script`), an alias of `eval` or `Function` assigned after its declaration or by destructuring, and in Python an alias of `eval`/`exec` or a lookup such as `getattr(builtins, "exec")`. It no longer claims to cover `eval` "however reached".
check: tests/test_eval_rule_second_send_back.py :: test_the_rule_file_states_what_it_does_not_follow

## Summary

- **AC-1 to AC-22** are copied over exactly as they were: same headings, same wording, same `check:` lines, same order.
- **AC-23 to AC-26** add the ways of calling `eval` that the reviewers named: `eval.call`, `eval.apply`, `Reflect.apply(eval, ...)` and `globalThis['eval']`. One criterion covers what gets flagged, one covers plain-literal arguments that shouldn't be, and one covers calls that only look similar. The last one requires the gate to fail on these calls.
- **AC-27** covers "say plainly in the rule what it can't follow". It requires the rule file to name the forms the rule still misses. I added it because a test can check the file's text, even though the brief says to skip changes that are only documentation. Drop it if you count it as documentation.
  - It also stops the build leg from adding coverage for the forms it lists, unless the rule file's wording is updated to match.
- **Not covered:** F4 (the conformance docs still describe the rule as unbuilt). It's a document change that no test can show, so there's no criterion for it.
- **New test file:** all the new tests go in `tests/test_eval_rule_second_send_back.py`, since the existing test files are locked.
