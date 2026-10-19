# Resolution: blind audit of `conformance/ssdf-218a-cisa.md`

- **Audit:** `conformance/audit/sol-ssdf-218a-cisa.md` (Sol, gpt-6.1-sol): 161 rows checked, 27 disagreements, 0 missing rows.
- **Sources** (under `grounded-forge/corpus.commons/chrisgagne-agent-built-software/sources/converted/`; line numbers below are these files'):
  - `nist-sp-800-218a.md`: read in full (lines 1–1172).
  - `cisa-secure-software-attestation-form.md`: read in full (lines 1–483).
  - `nist-ssdf-1-1.md`: read in part (PARTIAL: the three disputed tasks and the passages that bear on them, not the whole 2,298 lines). Lines read: 425–512 (Section 1's notional-frequency passage, Section 2), 670–722 (PO.2.2), 1330–1384 (PW.4.2), 1112–1120 (PS.3.2, for the 218A comparison) and 1735–1810 (the RV.1 practice and RV.1.1–RV.1.2).
- **Code checked:** the current checkout, `3a4e070`.
  - Read in full: `factory/legs.py`, `factory/stages/__init__.py`, `factory/stages/review.py`, `factory/isolation.py`, `factory/calibrate.py`, `calibration/verify-fixtures.sh`, `calibration/defects/README.md`, every file in `calibration/defects/11-reviewer-steering/`, `tests/test_review_blind.py::test_reviewers_get_separate_exports_without_agent_files`.
  - Read in part: `factory/stages/gate.py` (lines 1–260, 380–440), `factory/ledger.py` (`DEFAULTS`, `run_check`, `record_leg`, `stage_ready`, `timeout`), `factory/stages/warrant.py` (assessor, `pack_state`), `factory/hooks/guard.py` (docstring, `main`), `factory/text.py`, `factory/cli.py` (`run_stage`, `cmd_run`, `cmd_sign`), `factory/stages/triage.py` (`assess`), `DESIGN.md` (Isolation, Calibration), `calibration/realbugs/pick-cases.md`, `calibration/realbugs/PASS-MARK.md`.
  - Commit history: `git log bbd2241..HEAD`. It shows that `fd2910c` (fixture 11-reviewer-steering) landed after `bbd2241`, and the matrix's last update didn't cover it.
  - Untracked: `calibration/report-2026-10-12-seeds.md`, plus that run's work folder (its ledger, `findings-claude.json`, `findings-codex.json`, `findings.json`, `codex-log.txt`).
- **Date:** 2026-10-12. **Model:** claude-opus-5-5.

| Row ID | Field | Decision | Basis (source line or file:line) |
|---|---|---|---|
| SSDF 1.1 PO.2.2 | Requirement | audit right: periodic review of the training itself, and updating it, restored | ssdf 682–686 ("Periodically review personnel proficiency and role-based training, and update the training as needed") |
| SSDF 1.1 PW.4.2 | Requirement | audit right: "following SDLC processes" and the condition "that cannot be better met by third-party software components" restored | ssdf 1350–1353 |
| SSDF 1.1 RV.1.2 | Status / Mechanism / Evidence / Note | audit right: gap → asserted | The task asks only to review, analyse or test the code for vulnerabilities not yet detected (ssdf 1786–1788). The schedule is Example 1 (1789–1790), and examples are never required (485–488); any stated frequency is notional (439–440). The matrix's own header (its line 16) says examples never set a status. Partial coverage exists at change time: `factory/stages/gate.py:81` (scanners first), `:166–181` (deps on touched lockfiles), `:207–218` (sast on changed files), `:415` (the optional ratchet runs semgrep over `.`), `factory/stages/review.py:48–61` (reviewers get an export of the whole head). Code no change touches is never re-analysed, which leaves the row at asserted (matrix header, line 14). |
| 218A PO.3.1.R1 | Mechanism | audit right: the guard hook is on Claude legs only; Codex runs under its own read-only sandbox with `--ignore-user-config`; adapters run under `sandbox-exec` | `factory/stages/__init__.py:52–64` (guard in Claude leg settings), `factory/legs.py:226–227` (Codex argv: no settings, no hook), `factory/stages/review.py:309–310`, `factory/stages/__init__.py:131–136` (adapter under `sandbox-exec`). Status unchanged. |
| 218A PO.3.2.R2 | Mechanism / Note | audit right: the ledger holds the model name the CLI reports, or the configured fallback, not a served version | `factory/legs.py:211` (Claude: `modelUsage` key, else the init model, else the configured name), `:241–244` (Codex: the log's `model:` header, else the configured name). In the untracked 2026-10-12 run, the Codex leg recorded `gpt-6.1-sol` (the configured alias, echoed in `codex-log.txt` line 5) and the Claude legs `claude-opus-5-5`. |
| 218A PO.4.1.R1 | Mechanism | audit right: the hook and the named-tool limits cover Claude legs; Codex has only its own sandbox; guard blocks become ledger events only for spec, tests and build | `factory/stages/__init__.py:110–114` (guard log harvested in `adapter_leg` only), `factory/stages/review.py:304, 350` and `factory/stages/warrant.py:221–226` (reviewer, sort and assessor get the hook, but nothing reads their `guard.jsonl`), `factory/legs.py:226–227`. Status (demonstrated) unchanged: every leg still has a guardrail, and output validation runs on both families (`review.py:155–196`). |
| 218A PO.5 (practice modified) | Requirement / Mechanism / Evidence / Status / Note | audit right: not applicable → needs a third party | 218A 618–629: the modified practice still covers development, build, test and distribution environments, and adds AI model training. Scope 300–302 includes integrating models, so [S] can't exclude the whole practice. The factory supplies part of the environment and the rest is the producer's, as at SSDF 1.1 PO.5.1 (matrix header, line 14). Other modified rows (PS.1, PW.2.1) were also judged on the practice as modified. |
| 218A PO.5.1.R1 | Mechanism / Evidence / Status / Note | audit right: not applicable → asserted | 218A 623–625. Scope 300–302 defines "AI model development" to include "incorporating and integrating AI models into other software", so "during model development" covers the factory's integration, and [S] has no ground in the scope. Tracking: `factory/ledger.py:511–517` (cost, tokens, turns, duration per leg). Limiting: `factory/legs.py:100–103` (kill at timeout), `factory/ledger.py:60–62, 435–436` (30 min default). Nothing caps spend or rate. |
| 218A PO.5.1.R2 | Mechanism | audit right: the Codex reviewer can read the secret paths | `factory/isolation.py:157–180` (denials are Claude settings), `factory/legs.py:226–228` (none for Codex), `factory/stages/review.py:302–303`, `DESIGN.md:90, 103`. (`DESIGN.md:93` still says no leg may read the secret paths, which contradicts lines 90 and 103.) Status unchanged. |
| 218A PO.5.3.R1 | Mechanism / Evidence / Status / Note | audit right: not applicable → asserted | 218A 655–659. "Related resources" is an open "e.g." list. The Profile files testing data with training data (PS.1.2, 695–697), and the matrix already treats calibration data as in-scope testing data (its PS.1.2 and PW.3 rows). So the operator's machine hosts related resources: CLI credentials, prompts, calibration data. Partial monitoring: per-leg ledger events (`factory/ledger.py:505–517`) and hash re-checks at the pack. Nothing is continuous, and nothing watches prompts or fixtures. Asserted rather than needs a third party, in line with the matrix's 218A PO.5.3 and PO.5.1.R6 rows, where part of what's uncovered is within the factory's reach. |
| 218A PS.1.2.R1 | Requirement | audit right: confidentiality monitoring is "for non-public data only"; "continuously" restored | 218A 695–697 |
| 218A PS.3.2 (task modified) | Requirement | audit right: SLSA sits inside the task's "e.g." with the SBOM; it is an example, not a required format | 218A 744–749; compare SSDF 1.1 1114–1116 (SBOM the only example). Status (gap) unchanged: no provenance data is collected. |
| 218A PS.3.2.R2 | Mechanism / Status / Note | audit right: not applicable → needs a third party | 218A 748–754. The scope (300–302) covers integrating models, and Section 2 (393–411) expects a model produced by one organisation and run by another, under shared responsibility. Whether the hosted models were trained on sensitive data is the providers' knowledge, as the matrix found for 218A PW.7.2.R1. |
| 218A PW.1.1.C1 | Mechanism / Status / Note | audit right: not applicable → gap | 218A 778–780 doesn't limit "after AI model release" to the organisation's own releases. The scope covers integrating models (300–302). The factory's models are aliases the providers can repoint (`factory/ledger.py:59`), and nothing revisits the factory's risk model when they change. |
| 218A PW.3.1 (task added) | Mechanism / Evidence | audit right: the script prints check outcomes and compares nothing; there are twelve fixtures; 11 is unverified | `calibration/verify-fixtures.sh:47–94` (no read of `expect.yaml`; prints one row per fixture), `calibration/defects/README.md:26` (11: "not run yet"), `:28` (the "trips only its intended check" conclusion is the README's), `ls calibration/defects/` (00–11). Status unchanged. |
| 218A PW.3.1.R2 | Mechanism / Evidence | audit right: curation and fact-checking are recorded in the README and done by a person or session; the real-bug filtering is Sol's, per its brief; the script only runs checks | `calibration/verify-fixtures.sh:55–94`, `calibration/defects/README.md:11–26` (verification table and confirmation notes on 04, 08, 09), `calibration/realbugs/pick-cases.md` (selection criteria and split). Evidence relabelled instruction only. Status unchanged. |
| 218A PW.3.3 (task added) | Mechanism / Evidence / Status / Note | audit right: gap → asserted | 218A 839–841. `calibration/defects/11-reviewer-steering/change.patch:40–41` (the steering comment), `expect.yaml:1–3`, committed in `fd2910c`. Not demonstrated: `factory calibrate` runs by hand, not on every change (`conformance/BRIEF.md:20`). Sol's "catch not demonstrated" is now one run old. The untracked `calibration/report-2026-10-12-seeds.md` shows 11 caught at review, and in that run's work folder both reviewers reported the leak and the comment (`findings-claude.json` C1, C2; `findings-codex.json` X1, X3), and the sort confirmed both high (F1, F2). The Note cites the report as untracked. |
| 218A PW.3.3.R1 | Mechanism / Evidence / Status / Note | audit right: gap → asserted | 218A 839–842. `factory/calibrate.py:73–111` (fresh copy in a temp folder; triage, gate and review run for real), `:60–69` (a fail-closed review is a malfunction, not a catch), `:119` (any miss or error fails the run). Review legs run with their normal confinement (`review.py:304–310`). |
| 218A PW.4.4.R2 | Mechanism / Evidence / Status / Note | neither: gap → asserted (the audit proposed needs a third party) | 218A 870–872 asks to scan *and* thoroughly test before use. Scanning a hosted model is the providers' side (as at 218A PW.7.2.R1, 898–901). Testing is within the factory's reach, and fixture 11 now tests both review models for steering (`calibration/defects/11-reviewer-steering/expect.yaml:3`), but not as a condition of use. The uncovered part is partly the factory's, so the row isn't wholly a third party's (matrix header, line 14). |
| 218A PW.5.1.R3 | Mechanism / Evidence / Status / Note | audit right: demonstrated → asserted | 218A 881–882 asks for encoding. Encoding exists only for file names (`factory/stages/gate.py:184–194`, `tests/test_gate_hardening.py::test_a_file_named_like_an_option_cannot_switch_semgrep_off`) and for text a person reads (`factory/text.py:23–27`, `tests/test_text.py::test_inert_defuses_images_and_html_but_keeps_the_words`). Model-written code is confined, not encoded, and the old Note said so. The build leg runs it under Claude Code's sandbox, not `sandbox-exec` (`factory/stages/__init__.py:140–144`). `isolation.os_sandbox: false` turns `sandbox-exec` off (`factory/legs.py:114–117, 139`; `factory/ledger.py:477–478`). The matrix's own rule (header, line 14) then gives asserted. |
| 218A PW.8.1.R1 | Requirement / Mechanism / Evidence / Note | audit right: the listed forms "can be used"; they are not a required set; twelve fixtures, one adversarial | 218A 916–921; `ls calibration/defects/`; `calibration/defects/11-reviewer-steering/expect.yaml`. Status unchanged. |
| 218A PW.8.2.R1 | Mechanism / Evidence / Status / Note | audit right: gap → asserted | 218A 925–927. Fixture 11 tests both review models for one weak point (`expect.yaml:3`). The build, sort and assessor legs aren't tested, and calibration runs by hand (`factory/calibrate.py:93`, review only when on). |
| 218A PW.8.2.R2 | Mechanism / Note | audit right: a reported or fallback name, not a served version | `factory/legs.py:211, 241–244`; the observed Codex value equals the configured alias (see 218A PO.3.2.R2). Status (gap) unchanged. |
| CISA 1b(ii) | Mechanism / Evidence / Note | audit right: only the Claude reviewer gets the read denials (the sort is denied the change folder); Codex can read both; the test checks Claude's denials and both legs' separate paths | `factory/stages/review.py:302–304, 309–310, 350`; `tests/test_review_blind.py:44–52` (denials asserted on Claude's settings only; Codex checked for a separate cwd and live outputs outside the change folder); `DESIGN.md:103`. Status unchanged. |
| CISA 1e | Mechanism / Note | audit right: no credential store, but retained logs aren't redacted, and the Codex reviewer can read the credential files | `factory/legs.py:91–111` (raw logs), `factory/stages/review.py:315–317` (transcripts copied into the change folder), `factory/hooks/guard.py:304–310` (tool input logged), `factory/isolation.py:39–41` with `factory/legs.py:226–228` (no denial for Codex). Redaction exists only in gitleaks' report (`gate.py`, `--redact`) and triage's evidence. Status unchanged. |
| CISA 4 | Mechanism | audit right: each check runs where it applies, and the run stops at the first block | `factory/stages/gate.py:82–89` (commands not run after a scan fails), `:176` (deps skipped with no lockfile), `:210` (sast skipped with no changed files), `factory/cli.py:71` (run stops on a block). Every signable change still has gate and review ready (`factory/ledger.py:537–564`; `factory/stages/warrant.py:62`), and `commands.test` is required (`factory/ledger.py:228–229`). Status (demonstrated) unchanged. |
| CISA III (signature) | Requirement | audit right: the designee must be a producer employee; the 3PAO's agency approval must be in writing; the assessment must cover all elements, with NIST Guidance as the baseline | cisa 168–170, 176–184; Section III 341, 350–353 |
| Missing rows | - | none raised; none added | The audit found none within scope (SSDF Table 1, 218A Table 1, CISA Section III). The three-way scope in the matrix header is unchanged. |

## Other edits

- **Rows brought in line with the decisions above**, so the matrix doesn't contradict itself:
  - 218A PW.3 (practice) Note: all three tasks are now asserted.
  - 218A PW.4.4.R1 Mechanism: "the model name a CLI reports", replacing "the served model id".
  - 218A PS.3.1.R2 and 218A PS.3.2.R1 Notes: "reported model name" and "the model name the CLI reports", replacing "served model".
  - CISA 2 Note: SSDF 1.1 RV.1.2 "covers only what a change touches", replacing "is a gap".
  - The PROPOSED text in 218A PO.3.2.R2, PW.8.1.R1 and PW.8.2.R2 now compares reported model names, since that is what the ledger holds.
- **Header:**
  - A line under the update note names this resolution.
  - The Evidence bullet says the evidence this resolution added was checked at `3a4e070`.
  - The [S] bullet now says rows about the integrated hosted models apply, since the scope names "incorporating and integrating AI models into other software". [S] stays on weights, model code, training pipelines and data, reward models and model releases.
  - The counts table is updated.
- **Seen, not edited** (outside the matrix): `DESIGN.md:93` says no leg may read the secret paths, but `DESIGN.md:90, 103` and `factory/legs.py:226–228` show the Codex reviewer can. `calibration/defects/README.md:26` still marks fixture 11 not run, and `calibration/report-2026-10-12-seeds.md` is untracked.

## Counts

Decisions: audit right 26, matrix right 0, neither 1 (218A PW.4.4.R2). Missing rows: none raised, none added.

Status changes (11):

| Row | From | To |
|---|---|---|
| SSDF 1.1 RV.1.2 | gap | asserted |
| 218A PO.5 (practice modified) | not applicable | needs a third party |
| 218A PO.5.1.R1 | not applicable | asserted |
| 218A PO.5.3.R1 | not applicable | asserted |
| 218A PS.3.2.R2 | not applicable | needs a third party |
| 218A PW.1.1.C1 | not applicable | gap |
| 218A PW.3.3 | gap | asserted |
| 218A PW.3.3.R1 | gap | asserted |
| 218A PW.4.4.R2 | gap | asserted |
| 218A PW.5.1.R3 | demonstrated | asserted |
| 218A PW.8.2.R1 | gap | asserted |

New counts per status:

| Standard | Rows | demonstrated | asserted | gap | needs a third party | not applicable |
|---|---|---|---|---|---|---|
| SP 800-218 SSDF 1.1 | 47 | 6 | 13 | 9 | 14 | 5 |
| SP 800-218A Profile | 98 | 8 | 34 | 10 | 18 | 28 |
| CISA attestation form | 16 | 2 | 3 | 0 | 11 | 0 |
| **All** | **161** | **16** | **50** | **19** | **43** | **33** |
