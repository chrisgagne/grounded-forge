# Real-bug replay: HELD-OUT half, final (factory d67c073)

Cases: `heldout.json` (18), trials per case: 3. Claude review legs $9.74; Codex review tokens 0.

## Measures

| Measure | Value |
|---|---|
| bug_trials_caught | 0/36 (0%) |
| bug_trials_surfaced | 0/36 (0%) |
| bug_cases_pass_hat_k | 0/12 (0%) |
| bug_cases_pass_at_k | 0/12 (0%) |
| control_trials_false_alarm | 18/18 (100%) |
| control_trials_review_alarm | 18/18 (100%) |
| control_cases_pass_hat_k | 0/6 (0%) |
| errored_trials | 0/54 (0%) |
| grader_errors | 0/36 (0%) |
| infra_reruns | 54/54 (100%) |
| bug_trials_caught_original_rule | 0/36 (0%) |
| control_trials_false_alarm_original_rule | 18/18 (100%) |

## Against the pass mark

| Measure | Pass mark | Result | Meets |
|---|---|---|---|
| bug_trials_caught | >= 50% (PROPOSED) | 0% | no |
| bug_cases_pass_hat_k | >= 40% (PROPOSED) | 0% | no |
| bug_trials_surfaced | >= 70% (PROPOSED) | 0% | no |
| control_trials_false_alarm | <= 10% (PROPOSED) | 100% | no |
| control_cases_pass_hat_k | >= 80% (PROPOSED) | 0% | no |

Re-run once after an outage (originals in `infra-failures/`): rb02-t1, rb02-t2, rb02-t3, rb03-t1, rb03-t2, rb03-t3, rb04-t1, rb04-t2, rb04-t3, rb08-t1, rb08-t2, rb08-t3, rb10-t1, rb10-t2, rb10-t3, rb13-t1, rb13-t2, rb13-t3, rb14-t1, rb14-t2, rb14-t3, rb15-t1, rb15-t2, rb15-t3, rb19-t1, rb19-t2, rb19-t3, rb20-t1, rb20-t2, rb20-t3, rb25-t1, rb25-t2, rb25-t3, rb26-t1, rb26-t2, rb26-t3, rb28-t1, rb28-t2, rb28-t3, rb29-t1, rb29-t2, rb29-t3, rb32-t1, rb32-t2, rb32-t3, rb33-t1, rb33-t2, rb33-t3, rb34-t1, rb34-t2, rb34-t3, rb36-t1, rb36-t2, rb36-t3.

## Per case

| Case | Kind | Project | Trials |
|---|---|---|---|
| rb02 | bug | markdown-it | missed / missed / missed |
| rb03 | bug | immutable-js | missed / missed / missed |
| rb04 | bug | yargs-parser | missed / missed / missed |
| rb08 | bug | date-fns | missed / missed / missed |
| rb10 | bug | js-yaml | missed / missed / missed |
| rb13 | bug | immutable-js | missed / missed / missed |
| rb14 | control | markdown-it | false alarm: review:malfunction / false alarm: review:malfunction / false alarm: review:malfunction |
| rb15 | bug | decimal.js | missed / missed / missed |
| rb19 | bug | jsdiff | missed / missed / missed |
| rb20 | bug | node-semver | missed / missed / missed |
| rb25 | control | decimal.js | false alarm: review:malfunction / false alarm: review:malfunction / false alarm: review:malfunction |
| rb26 | control | yargs-parser | false alarm: gate:sast, review:malfunction / false alarm: gate:sast, review:malfunction / false alarm: gate:sast, review:malfunction |
| rb28 | control | js-yaml | false alarm: review:malfunction / false alarm: review:malfunction / false alarm: review:malfunction |
| rb29 | bug | markdown-it | missed / missed / missed |
| rb32 | control | date-fns | false alarm: review:malfunction / false alarm: review:malfunction / false alarm: review:malfunction |
| rb33 | bug | yargs-parser | missed / missed / missed |
| rb34 | bug | date-fns | missed / missed / missed |
| rb36 | control | node-semver | false alarm: review:malfunction / false alarm: review:malfunction / false alarm: review:malfunction |
