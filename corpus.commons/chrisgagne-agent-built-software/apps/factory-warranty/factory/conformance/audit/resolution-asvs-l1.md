# Resolution: blind audit of `conformance/asvs-l1.md`

- **Audit:** `conformance/audit/sol-asvs-l1.md` (Sol, gpt-6.1-sol): 70 rows checked, 12 disagreements, 4 missing rows.
- **Source:** `grounded-forge/corpus.commons/chrisgagne-agent-built-software/sources/converted/owasp-asvs-5-0.md`. Read in full: lines 1–440 (all front matter), plus V2 (lines 545–600) and V8 (lines 1105–1160) around the disputed status rows, and each cited requirement line. Line numbers below are this file's.
- **Code checked:** `factory/stages/triage.py`, `factory/prompts/reviewer.md`, `factory/axis.py`, `factory/stages/warrant.py`, `factory/ledger.py` (config defaults), `calibration/defects/02-auth-bypass/` (all three files), `tests/test_warrant.py`; listener rows L1.35, L2.53, L5.68, L5.69 and L6.59 and seed rows P2.1 and P2.2 printed with `factory.axis`.
- **Date:** 2026-10-12. **Model:** claude-opus-5-5.

| Row ID | Field | Decision | Basis (source line or file:line) |
|---|---|---|---|
| 1.3.1 | Requirement | audit right: "and secure" restored | source 484 ("well-known and secure HTML sanitization library or framework feature") |
| 2.3.1 | Status / Note | audit right: needs a third party → asserted | source 325 (tools can't entirely verify business logic) and 327 (application-specific verifications, like existing unit and integration tests, can); nothing in the source requires an independent party. Mechanisms are instructions: `factory/stages/triage.py:72-73` (money focus), `factory/prompts/reviewer.md:17`, listener L6.59. `conformance/BRIEF.md:21` |
| 5.3.2 | Requirement | audit right: "or file metadata" and "sanitization" restored | source 826 |
| 7.4.1 | Requirement | audit right: logout and expiry are examples of termination | source 1078 ("when session termination is triggered (such as logout or expiration)") |
| 8.2.1 | Status / Note | audit right: needs a third party → asserted | source 325, 327; 337 asks for hybrid testing with "full access to the application developers", not an independent party. `calibration/defects/02-auth-bypass/expect.yaml:2` (`caught_by: [review]`, a model catch, so asserted); `factory/prompts/reviewer.md:19` |
| 8.2.2 | Status / Note | audit right: needs a third party → asserted | source 1142, 325, 327; `calibration/defects/02-auth-bypass/change.patch:49-58` (any user's profile by id, caught by review only) |
| 8.3.1 | Status / Note | audit right: needs a third party → asserted | source 1152, 325, 327, 337 (the audit's "339" is a blank line; the hybrid-testing passage is 337); `change.patch:50-53` (access on a header the caller sets) |
| 9.1.2 | Requirement | audit right: per-context allowlist and key-confusion condition restored | source 1190 |
| 9.2.1 | Requirement | audit right: conditional on a validity span being present | source 1201 ("if a validity time span is present in the token data") |
| 10.4.2 | Requirement | audit right: revocation is on a second *valid* request with a code already used to issue an access token | source 1304 (the row also keeps the source's opening condition, a code returned in the authorization response) |
| 10.4.5 | Requirement | audit right: invalidate after each use; revoke all refresh tokens for that authorization, not "the whole grant" | source 1307 |
| 14.3.1 | Requirement | audit right: client *or* session termination, and clearing when the server can't be reached | source 1674 |
| Missing: licence on reuse | new row | not added | source 25 binds reuse or distribution of the standard's own text (Frontispiece, Copyright and License), not an application or its verification, so it is outside the matrix's scope |
| Missing: pass or fail decision | new row | not added as its own row | source 100 says the scope section "establishes which requirements are included or excluded"; 122 is that test for the standard's requirements, beside 116 ("Every requirement must have a demonstrable impact on security"). The per-requirement outcome a verifier reports is carried by the new row A&C Verification reporting ¶1 (requirements checked, exceptions noted) |
| Missing: verification reporting | new row | added: A&C Verification reporting ¶1, gap | source 305 (contents "should"; non-applicable requirements "must be noted"); `factory/stages/warrant.py:79-193` (pack sections name no ASVS requirement; no applicability record); no `asvs` or `level` in `factory/ledger.py` |
| Missing: each requirement verifiably tested | new row | added: A&C Verification Mechanisms ¶1, gap | source 317; nothing maps a test or check to an ASVS ID; listener L6.59 covers only authorization and business logic under distillations grounding, so not asserted (BRIEF:30, the lower status when in doubt) |

## Other edits

- **Two rows added that the audit didn't raise,** so the new table covers every verification duty in the front matter (BRIEF:28): A&C Scope of Verification ¶1 (source 309: level sought, requirements included, rationale for exclusions; `factory/ledger.py:49-58` has no level; L2.53 never reaches a packet) → gap; A&C Scope of Verification ¶3 (source 313: disclose testing methods, ideally repeatable; `factory/stages/warrant.py:92-147`; `tests/test_warrant.py::test_pack_separates_demonstrated_from_asserted`) → asserted, as it covers one change, not an ASVS verification, and review legs run once.
- **Not added as rows:** source 297 (assurance services must not claim official OWASP certification) governs how a claim is worded, not how verification is done, and neither `README.md` nor `DESIGN.md` makes an ASVS or OWASP certification claim. Source 337 (hybrid penetration testing) is "strongly encouraged", not an obligation; the header cites it.
- **Header:** the subject line names the process rows; the ASVS-position paragraph adds source 327; the needs-a-third-party bullet now lists two groups, and a new bullet says why the four access-control and business-logic rows are asserted; finding 2 now says the report "should" summarise requirements checked and "must" note those that don't apply (source 305), and points to the new table; the counts table has a column for the new rows.

## Counts

Decisions: audit right 12, matrix right 0, neither 0. Missing rows: 2 added, 2 not added (plus 2 added for coverage of the new table).

Status changes: 2.3.1, 8.2.1, 8.2.2 and 8.3.1, needs a third party → asserted.

| Status | L1 requirements | Verification obligations |
|---|---|---|
| demonstrated | 0 | 0 |
| asserted | 45 | 1 |
| gap | 17 | 3 |
| needs a third party | 8 | 0 |
| not applicable | 0 | 0 |
| **Total** | **70** | **4** |
