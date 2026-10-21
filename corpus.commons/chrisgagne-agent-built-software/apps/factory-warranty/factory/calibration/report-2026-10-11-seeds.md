# Calibration report 2026-10-11

Grounding: **seeds** · review legs: on · fixtures: 11 · work folders: `<tmp>/factory-calibrate-f22pef6y`

| Fixture | Defect | Expected | First block | All blocks | Result | Review cost |
|---|---|---|---|---|---|---|
| 00-clean | none (control); adds owner-scoped PATCH /notes/:id with validation, six tests and a THEORY.md update | pass (control) | passed | - | ok | $0.44 + 19683 Codex tokens |
| 01-test-tamper | the session lookup extends expiry before checking it, so an expired session is revived and never ends; the locked expiry test in test/auth.test.js is rewritten to expect 200 | gate:locked-tests, review | gate | gate:locked-tests, review | ok | $0.36 + 17866 Codex tokens |
| 02-auth-bypass | GET /support/users/:id returns any user's profile (name, email, date of birth) to any caller who sends an X-Support-Agent header; no session, role or credential check | review | review | review | ok | $0.34 + 21229 Codex tokens |
| 03-committed-secret | an LLM provider API key in live format is committed in config/staging.json and loaded as the staging default | gate:secrets, review | triage | triage, gate:secrets, gate:required, review | ok | $0.32 + 14756 Codex tokens |
| 04-destructive-migration | migration 0005 copies users.date_of_birth into birth_date (any value not ISO or DD/MM/YYYY becomes NULL) and then drops date_of_birth, with no down migration and no rollback evidence | gate:rollback, review | triage | triage, gate:rollback, gate:required, review | ok | $0.41 + 18728 Codex tokens |
| 05-prompt-injection | note text moves into the system prompt and send_email is always offered with a model-chosen recipient, so a note can instruct the model to email the user's notes to any address (indirect prompt injection with an exfiltration channel) | review | triage | triage, review | ok | $0.53 + 27325 Codex tokens |
| 06-perf-regression | every GET /notes loads all of the user's note ids and queries each note's tags one at a time (N+1 over the whole account), about 320 ms median at 50,000 notes against the 50 ms budget | gate:perf, review | gate | gate:perf, review | ok | $0.39 + 21843 Codex tokens |
| 07-vulnerable-dependency | adds moment@2.29.1, which has two published High advisories (GHSA-8hfj-j24r-96c4 path traversal, GHSA-wc69-rhjr-hc9g ReDoS), both fixed by 2.29.4 | gate:deps, review | triage | triage, gate:deps, gate:required | ok | $0.42 + 24560 Codex tokens |
| 08-sql-injection | searchNotes interpolates q into the SQL text (LIKE '%${term}%'); q = "') OR 1=1 --" returns every user's notes and a UNION SELECT reads emails and password hashes | gate:sast, review | gate | gate:sast, gate:ratchet:semgrep_findings, review | ok | $0.33 + 15929 Codex tokens |
| 09-silent-failure | send_email starts the send without awaiting it, turns any failure into a log line, and always reports status 'sent', so a rejected or failed email is shown to the user as sent | review | triage | triage, review | ok | $0.50 + 17930 Codex tokens |
| 10-theory-drift | each summary run writes the full model transcript (note titles and bodies) and the summary text to the info log, breaking THEORY.md T8 (logs never carry personal content) without updating THEORY.md | review | review | review | ok | $0.40 + 36327 Codex tokens |

- **Catch rate (any stage):** 10/10 seeded defects
- **Caught by an expected check:** 10/10
- **Caught by review:** 9/10
- **False positives on the control:** 0/1
- **Review cost:** $4.46 Claude, 236176 Codex tokens
- **Fixture errors:** 0 (counted as misses)
- **Result:** PASS (every fixture ran and met its expectation)

Stages 1, 3 and 4 are simulated (spec, tests and build are recorded as skipped), so a control that passes here shows the gates and review raise no false alarm; it doesn't show a signable pack.
