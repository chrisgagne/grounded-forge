# Real-bug replay: fresh controls, pass mark v2, factory e1f38c2

Cases: `fresh-controls.json` (12), trials per case: 3. Claude review legs $9.48; Codex review tokens 762,558.

## Measures

| Measure | Value |
|---|---|
| bug_trials_caught | 0/0 |
| bug_trials_surfaced | 0/0 |
| bug_cases_pass_hat_k | 0/0 |
| bug_cases_pass_at_k | 0/0 |
| control_trials_false_alarm | 0/36 (0%) |
| control_trials_review_alarm | 0/36 (0%) |
| control_cases_pass_hat_k | 12/12 (100%) |
| errored_trials | 0/36 (0%) |
| grader_errors | 0/0 |

## Against the pass mark

| Measure | Pass mark | Result | Meets |
|---|---|---|---|
| bug_trials_caught | >= 80% (PROPOSED) | n/a | n/a |
| bug_cases_pass_hat_k | >= 70% (PROPOSED) | n/a | n/a |
| bug_trials_surfaced | >= 95% (PROPOSED) | n/a | n/a |
| control_trials_false_alarm | <= 20% (PROPOSED) | 0% | yes |
| control_cases_pass_hat_k | >= 80% (PROPOSED) | 100% | yes |

## Per case

| Case | Kind | Project | Trials |
|---|---|---|---|
| fc01 | control | date-fns | passed clean / passed clean / passed clean |
| fc02 | control | yargs-parser | passed clean / passed clean / passed clean |
| fc03 | control | js-yaml | passed clean / passed clean / passed clean |
| fc04 | control | immutable-js | passed clean / passed clean / passed clean |
| fc05 | control | jsdiff | passed clean / passed clean / passed clean |
| fc06 | control | jsdiff | passed clean / passed clean / passed clean |
| fc07 | control | node-semver | passed clean / passed clean / passed clean |
| fc08 | control | node-semver | passed clean / passed clean / passed clean |
| fc09 | control | markdown-it | passed clean / passed clean / passed clean |
| fc10 | control | yargs-parser | passed clean / passed clean / passed clean |
| fc11 | control | decimal.js | passed clean / passed clean / passed clean |
| fc12 | control | markdown-it | passed clean / passed clean / passed clean |
