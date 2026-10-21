# Resolution: Sol's blind re-audit of 11 LLM/Agentic rows (2026-10-14)

Sol (gpt-6.1-sol) re-audited the 11 rows the factory changes of 2026-10-14 touched, blind: it got the rows without
status or notes (`reaudit-rows-2026-10-14.md`) and the brief `REAUDIT-BRIEF-2026-10-14.md`, and read the cited
OWASP entries whole (LLM01, LLM03, LLM07, LLM10; ASI05, ASI07, ASI08, ASI09: line ranges in its first line), the code,
and the tests. 180,538 Codex tokens.

**Status.** Sol's status is the status: the operator doesn't grade the operator's work. All 11 are asserted. LLM03.3
moves from gap to asserted; the other 10 were asserted and stay so. No row reached demonstrated.

**Mechanism text corrected to Sol's reading** (each an overclaim it named):
- LLM03.3: command adapters and the Codex reviewer keep open shells; the guard matches words, it doesn't validate
  inputs against schemas.
- LLM07.2, LLM10.1: a builder command adapter can write and run code in one shell run; the check doesn't scan
  symlinks or git-ignored files.
- LLM07.3: the guard covers calls to the guarded tools and reads selected arguments, not "every call's arguments";
  a stage checks its immediate predecessor; `build:guard` is written only when the guard blocked something.
- ASI05.5: not every failure path fails closed (an assessor failure leaves the pack usable); legs share the worktree
  and the user's temp folder, so they aren't per-session environments.
- ASI05.6: "no elevated runs" was unsupported: only `sudo` in a leg's command text is blocked.
- ASI05.7: transcripts and logs are kept, not a full audit of every run; the rollback rehearsal and ratchets still
  run after a failed scan; the check's runs have no ledger events of their own.
- ASI08.5: release, not everything, needs a signature; granted network is used before sign-off; the calibration
  reports simulate spec, tests and build.

**Fixed in code** (`6e2af55`), from Sol's findings:
- The check failed open: if `git diff` failed, it scanned nothing and ran the command; a nonzero semgrep exit with a
  readable report passed. Both now refuse to run the command (tests/test_check.py::test_the_check_fails_closed_when_it_cannot_tell_what_changed).
- The driver ran the tests leg's new tests without a scan. It now runs the check's scans first and blocks on a
  problem (`tests:scan`; tests/test_tests_stage.py::test_the_driver_scans_the_new_tests_before_it_runs_them).
- The sort's `file`, `line` and `claim` weren't type-checked (tests/test_spec_review_axis.py::test_a_sort_item_with_a_mistyped_field_is_rejected).
- The live Codex schema check had no artefact in the repo: `conformance/evidence/codex-schema-live-2026-10-14.md`.

**Left open, as Sol found them:** command adapters' shells; git-ignored and symlinked files outside the check's scans;
no check-specific ledger event; no detection or approval of elevated runs inside configured commands; schema versions
and audiences (ASI07.9). Sol's list of other strategies these changes bear on (LLM01 #4, #5, #7, #8, #11; LLM03 #1, #2,
#4, #6–#9; LLM07 #5, #6, #8–#10; LLM10 #2–#4, #7–#9; ASI05 #1, #2, #4; ASI07 #6; ASI08 #3, #4, #7, #10; ASI09 #6,
#7) names rows that exist in the matrix but weren't in this re-audit: they keep their 2026-10-13 audited status until
a full re-audit.
