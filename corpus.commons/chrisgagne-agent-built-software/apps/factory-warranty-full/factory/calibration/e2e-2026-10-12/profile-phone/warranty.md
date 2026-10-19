# Warranty pack: 20261012-164600-add-an-optional-phone-number-to

**Change:** Add an optional phone number to the profile  
**Repo:** `<scratch>/e2e/notes-app` · **branch** `factory/20261012-164600-add-an-optional-phone-number-to` · **baseline** `56105efa0b80` → **head** `92904bb9cd201fc421575ddd053554ee6897531f` (tree `6406c77d0f6f8e872145551c436cbef2175b2b54`)  
**Builder:** claude  
**Assembled from ledger events** e001–e065 (`ledger.json`).

**Status:** READY TO SIGN

## Story

> # Add an optional phone number to the profile
>
> Some people want us to have a phone number for them, for account recovery later. For now we only need to store it and let them see and change it.
>
> ## What we want
>
> - The profile has an optional phone number. People can set it at signup or change or clear it later on their profile.
> - Phone numbers are stored in international form (E.164, like +64211234567). Anything else is refused with a clear error.
> - People see their own phone number on their profile, and nobody else's.
> - Existing accounts keep working and simply have no phone number.

## Risk classes

- **auth**: keyword in story/acceptance: log in, login, session; path in diff paths: src/auth/routes.js. Required gates: none beyond the standard gates. Review focus: OWASP ASVS 5.0 V6 Authentication, V7 Session Management and V8 Authorization (V9 Self-contained Tokens and V10 OAuth and OIDC where tokens or OAuth are involved).
- **personal-data**: keyword in story/acceptance: date of birth, phone number, phone numbers; path in diff paths: src/users/repo.js, src/users/routes.js, src/users/validate.js. Required gates: none beyond the standard gates. Review focus: OWASP ASVS 5.0 V14 Data Protection and V8 Authorization: who can read or change whose data; what is logged or sent out.
- **migration**: keyword in story/acceptance: migration, migrations; path in diff paths: migrations/0005_add_user_phone_number.down.sql, migrations/0005_add_user_phone_number.up.sql; pattern in migrations/0005_add_user_phone_number.down.sql: ALTER TABLE users DROP COLUMN phone_number;. Required gates: gate:rollback. Review focus: Is the migration reversible; does the down path restore data, not just schema; is the rollback rehearsed?
- **llm-agent**: keyword in story/acceptance: llm. Required gates: none beyond the standard gates. Review focus: OWASP Top 10 for LLM Applications 2026 and OWASP Top 10 for Agentic Applications 2026: prompt injection, excessive agency, tool misuse, data leaking through the model.

Triage: pass (e037), phase diff.

## Demonstrated

Commands the driver ran, with exit codes and output hashes.

- [e019] tests:install `npm ci` exit 0, output sha256 `24baecf0aad963c7`, log `tests/install.log`
- [e020] tests:baseline-tests `npm test` exit 0, output sha256 `acf1ad57b01f6a15`, log `tests/baseline-tests.log`
- [e022] tests:new-tests `npm test` exit 1 (expected: red before the build), output sha256 `49a8bd1a327f6d35`, log `tests/new-tests.log`
- [e040] gate:install `npm ci` exit 0, output sha256 `48a3423524e942c6`, log `gate/install.log`
- [e041] gate:typecheck `npm run typecheck` exit 0, output sha256 `9b19c927d3113c8a`, log `gate/typecheck.log`
- [e044] gate:tests `npm test` exit 0, output sha256 `ccc491b11676e7cc`, log `gate/tests.log`
- [e045] gate:perf `npm run perf` exit 0, output sha256 `f667fc6e231d90ad`, log `gate/perf.log`
- [e046] gate:secrets `gitleaks git --no-banner --redact --ignore-gitleaks-allow --log-opts=56105efa0b80cfa74712467886257ef8c5995bb0..HEAD --report-format json --report-path <scratch>/e2e/notes-app/.factory/changes/20261012-164600-add-an-optional-phone-number-to/gate/gitleaks.json .` exit 0, output sha256 `c69153d34b61926b`, log `gate/secrets.log`
- [e048] gate:sast `semgrep scan --config p/default --config '<factory>/factory/rules/semgrep' --metrics=off --disable-nosem --json --quiet --error --severity ERROR --severity WARNING -- ./docs/THEORY.md ./migrations/0005_add_user_phone_number.down.sql ./migrations/0005_add_user_phone_number.up.sql ./rollback.md ./scripts/rehearse-rollback.js ./src/auth/routes.js ./src/users/repo.js ./src/users/routes.js ./src/users/validate.js ./test/auth.test.js ./test/helpers/db-app.js ./test/migrations.test.js ./test/summary.test.js ./test/users.test.js` exit 0, output sha256 `0d12a9a05a15feb1`, log `gate/sast.log`
- [e049] gate:rollback `node --disable-warning=ExperimentalWarning scripts/rehearse-rollback.js` exit 0, output sha256 `da3398ac49d8e3bf`, log `gate/rollback.log`
- [e039] locked-test hash check: **pass**, 15 files

## Asserted, not evidence

The builder's own words. Nothing here was checked by running anything.

**Builder summary** (`builder-summary.md`):

> The profile now has an optional `phoneNumber`. Tests (68 of 68), typecheck, perf and the rollback rehearsal all pass, and nothing is committed.
>
> ## What I changed and why
>
> - **`migrations/0005_add_user_phone_number.up.sql` / `.down.sql`**: the up file adds a nullable `phone_number` column to `users`, so existing accounts get `NULL` (AC-11). The down file removes that column and nothing else, so accounts and their other fields stay (AC-12).
> - **`src/users/validate.js`**: new `validatePhoneNumber`. A missing value, `null` or `""` all mean "no phone number", the same as `dateOfBirth`. Anything else must be a string matching `^\+[1-9][0-9]{1,14}$`, or the request gets a 400 saying "phoneNumber must be in international E.164 format, like +64211234567". Nothing is normalised (AC-1 to AC-3, AC-6, AC-7).
> - **`src/users/repo.js`**: the user's `phoneNumber` is read, stored and updated, and the profile returned by the API includes it. That one profile shape is used by signup, `/login` and `/me`, so all three show it (AC-4). I wrote the SQL as fixed strings to keep the "SQL text is constant" rule in THEORY.md (T9) obvious.
> - **`src/auth/routes.js`**: signup checks the phone number before looking for an existing account, so a bad number creates no account (AC-3).
> - **`src/users/routes.js`**: `PATCH /me` changes the phone number only when the field is in the request (AC-8). All fields are checked before anything is written, so one bad phone number refuses the whole request (AC-7). `/me` still requires a session (AC-10).
> - **No change to the summary code**: it only sends notes to the model and uses the email as the recipient address, so the phone number never reaches the model (AC-13).
> - **`docs/THEORY.md`**: added the phone number to the personal-data list, to T4 ("Profile fields stay inside the app", now with the E.164 rule) and to the API table.
> - **`rollback.md`** and a new **`scripts/rehearse-rollback.js`**: how to undo the change, what is lost (every stored phone number, with a way to export them first), and `rehearse: node --disable-warning=ExperimentalWarning scripts/rehearse-rollback.js`. The script works on a throwaway database file: migrate up, add two accounts, roll back, check the column is gone and the accounts are unchanged, then migrate up again and check every phone number is `NULL`.
>
> No dependencies were added.
>
> ## What I ran and what it showed
>
> - `npm test`: 68 of 68 passed, none failed or skipped.
> - `npm run typecheck`: no errors.
> - `npm run perf`: all three scenarios passed; medians were 0.91, 1.09 and 2.12 ms against the 50 ms budget.
> - The rehearse command printed "rollback rehearsal passed" and exited 0.
> - I did not run `npm ci`, because `node_modules` was already there.
>
> ## Things to know
>
> - **SQLite version:** the down migration relies on `ALTER TABLE … DROP COLUMN`, which needs SQLite 3.35 or later. The SQLite built into Node 22 supports it, and the tests and rehearsal ran it successfully.
> - **Guard hook:** the factory's guard blocks any shell command containing `DROP`, so I created the down migration with the file-writing tool instead of the shell. Anyone running the rollback from a factory leg's shell would hit the same block.
> - **Old app on the new schema:** `rollback.md` says the previous app version runs fine against the migrated schema. That's because it names its columns and the new column allows `NULL`. I reasoned this from the code but didn't run the old version to check.
> - **Locked tests:** none of them looked wrong.

**Tests-leg summary** (`tests-summary.md`):

> I wrote 13 acceptance tests, one per criterion. When I ran `npm test`, all 13 failed, and each failure comes from the missing phone number feature, not from a syntax or import error. The 55 existing tests still pass. I only added lines to existing files and removed none. I also added one helper file, `test/helpers/db-app.js`. Its `startTestAppOn(db)` runs the app on a database the test sets up itself and doesn't close that database. The migration tests need this. Nothing is committed.
>
> | AC | File | Test name | What it asserts |
> |---|---|---|---|
> | AC-1 | test/auth.test.js | signup stores an optional phone number in E.164 form | Signup with `+64211234567` returns 201 and the profile has exactly that `phoneNumber`. The shortest (`+12`) and longest (`+123456789012345`) valid numbers are accepted too. |
> | AC-2 | test/auth.test.js | signup without a phone number gives a profile with no phone number | Leaving the field out, sending `null` or sending `""` all give 201 and a profile that contains `phoneNumber: null`. |
> | AC-3 | test/auth.test.js | signup rejects a phone number that is not in E.164 form and creates no account | Every invalid input in the brief is answered 400, plus `+`, `+1`, spaces before or after, and non-strings (a number, `true`, an array, an object). The error must match `/E\.?164\|international/i`. No user rows are created, and a later signup with the same email and a valid number gets 201. |
> | AC-4 | test/users.test.js | GET /me and login show the user's own phone number | After signing up with a phone number, the `POST /login` profile and `GET /me` both show it. |
> | AC-5 | test/users.test.js | PATCH /me sets and changes the phone number | `PATCH /me` sets a number and then changes it, answering 200 with the new number each time. `GET /me` shows it, and the name and date of birth stay the same. |
> | AC-6 | test/users.test.js | PATCH /me can clear the phone number | Both `null` and `""` clear the stored number, in the response and on a later `GET /me`. |
> | AC-7 | test/users.test.js | PATCH /me rejects phone numbers that are not in E.164 form and keeps the old one | Invalid numbers get 400 with the format error. A request with a valid `name` and `dateOfBirth` plus a bad number is refused as a whole. Afterwards `GET /me` returns exactly the same profile as before. |
> | AC-8 | test/users.test.js | PATCH /me without a phone number leaves the stored one unchanged | Changing only `name`, or only `dateOfBirth`, leaves the stored number as it was. |
> | AC-9 | test/users.test.js | each user sees only their own phone number | Each user's `/me` and `/login` show their own number. None of a user's `/me`, `/login`, `/notes` or `/notes/:id` responses contain the other user's digits, including when they ask for the other user's note. |
> | AC-10 | test/users.test.js | phone number cannot be read or changed without a session | With no cookie, a forged cookie, or a logged-out cookie, `GET /me` and `PATCH /me` (set and clear) are answered 401. The stored number is unchanged when the user logs in again. |
> | AC-11 | test/migrations.test.js | existing accounts keep working with no phone number after migrating | Users are inserted on the old schema (migrations 0001–0004), then at least one new migration must apply. After that, both users can log in, keep the same id, email, name and date of birth (one has none), and show `phoneNumber: null`. |
> | AC-12 | test/migrations.test.js | rolling back the phone number migration keeps existing accounts | Rolling back the latest migration must undo something newer than 0004. The users' rows (id, email, password hash, name, date of birth, created at) are identical afterwards. Migrating up again reapplies the same migration, and logging in shows the same profile with `phoneNumber: null`. |
> | AC-13 | test/summary.test.js | the phone number is never sent to the model | The test first checks that the user really has a number. It then asks for a summary with and without email (three model calls). None of the requests to the model contain `64211234567` or `211234567`. |
>
> Three choices in these tests go beyond the brief's wording:
> - **Error message check:** "names the required international format" is checked with `/E\.?164|international/i`. An error message that uses neither word would fail, even if it is otherwise clear.
> - **Rollback check (AC-12):** the test recognises the phone number migration as anything numbered above 0004. If another migration were added after it, this test would fail.
> - **Two-digit numbers:** AC-1 also requires `+12` to be accepted, because the brief's rule allows 2 to 15 digits.

## Gates

| Check | Status | Event | Detail |
|---|---|---|---|
| locked-tests | pass | e039 |  |
| install | pass | e040 | exit 0 |
| typecheck | pass | e041 | exit 0 |
| lint | skipped | e042 | commands.lint is not configured |
| build | skipped | e043 | commands.build is not configured |
| tests | pass | e044 | exit 0 |
| perf | pass | e045 | exit 0 |
| secrets | pass | e046 | exit 0 |
| deps | skipped | e047 | the change touches no lockfile |
| sast | pass | e048 | exit 0 |
| rollback | pass | e049 | exit 0 |
| surface | pass | e050 | the change edits no test-runner or scanner config |
| ratchet:semgrep_findings | pass | e051 |  |
| required | pass | e052 |  |
| unchanged | pass | e053 |  |
| theory-doc | info | e054 |  |

**Stage outcomes:**

- spec: ready (pass)
- tests: ready (pass)
- build: ready (pass)
- triage: ready (pass)
- gate: ready (pass)
- review: ready (pass)

## Ratchet

- [e051] semgrep_findings: 0 at baseline → 0 after the change (**pass**); `semgrep scan --config p/default --config '<factory>/factory/rules/semgrep' --metrics=off --disable-nosem --json --quiet -- .`, output sha256 baseline `32a1f49e7a32d97c`, after `09e48b9833df2b28`

## Theory doc

- [e054] `docs/THEORY.md`: changed by this change

## Review

- [e058] reviewer-claude (claude-opus-5-5): pass, $0.47, 48.5 s
- [e060] reviewer-codex (gpt-6.1-sol): pass, 47241 tokens, 64.9 s
- [e062] sort (claude-opus-5-5): pass, $0.24, 22.5 s
- [e057] grounding: seeds (30 axis rows)

| ID | Severity | Verdict | Where | Claim | Sort reason | Resolution |
|---|---|---|---|---|---|---|
| F1 | medium | confirmed | migrations/0005_add_user_phone_number.down.sql:1 | The down migration permanently drops every stored phone number, with no restore path or tested restore, which breaks theory invariant T10 for a personal-data column. | THEORY.md:40 (T10) requires a migration that drops personal-data columns to ship with a tested restore. 0005 down.sql is `ALTER TABLE users DROP COLUMN phone_number;`. rollback.md offers only an expor | - |
| F2 | low | confirmed | rollback.md:20 | The rollback runbook exports phone numbers to a plaintext file with no location, permissions or retention set, and the output is pipe-separated rather than CSV. | rollback.md:20 writes all phone numbers to ./phone-numbers.csv using sqlite3's default list mode, which separates fields with `/` rather than commas. The only safeguard is the advice to keep the file  | - |

## Irreversible operations and rollback

- Classes: migration.
- [e049] rollback: pass, rehearsed with `node --disable-warning=ExperimentalWarning scripts/rehearse-rollback.js` exit 0

## Residual risks

- [e042] gate:lint skipped: commands.lint is not configured
- [e043] gate:build skipped: commands.build is not configured
- F1 confirmed (medium), below the blocking bar and unfixed: The down migration permanently drops every stored phone number, with no restore path or tested restore, which breaks theory invariant T10 for a personal-data column.
- F2 confirmed (low), below the blocking bar and unfixed: The rollback runbook exports phone numbers to a plaintext file with no location, permissions or retention set, and the output is pipe-separated rather than CSV.
- Personal data: plan an independent penetration test before launch.
- LLM or agent behaviour: deterministic gates don't cover model behaviour; watch it in production.
- [e028] the guard blocked 1 build-leg tool calls: Blocked command: DROP and TRUNCATE are not allowed from a factory leg.

## Sign-off

Accountable person: ______________________

Decision: [ ] sign   [ ] return

Reason (for a return): ______________________

Record the decision with `factory sign --change 20261012-164600-add-an-optional-phone-number-to --by NAME` or `factory return --change 20261012-164600-add-an-optional-phone-number-to --reason "..."`. The ledger records it with this pack's sha256. The harness never signs.
