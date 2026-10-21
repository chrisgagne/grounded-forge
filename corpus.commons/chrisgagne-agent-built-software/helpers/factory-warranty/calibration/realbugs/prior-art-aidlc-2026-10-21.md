# The factory against AWS Labs' AI-DLC, mechanism by mechanism (2026-10-21)

Recorded so the README's comparison can be checked. Not an evaluation: neither system was run. A Claude agent read
each system's own documentation and code and cited what each does.

- **AI-DLC:** github.com/awslabs/aidlc-workflows, v2.11.1, commit `7c93048a`. **PARTIAL:** about 45,000 lines of
  docs and 206,000 of TypeScript, so the relevant parts were read, not all of it (the README, the guide's
  introduction, interaction modes and state-and-audit chapters, the sensor, commit-provenance and construction
  references, the construction stage and protocol files, the reviewer protocol and agent, and targeted ranges of the
  engine). Its GitHub issues and pull requests weren't read. "Not found" below means a search of `core/`, `docs/`,
  `harness/`, `plugins/` and `scripts/` found nothing.
- **The factory:** this repository on 2026-10-21, before `897e6a8`; the files cited were read in full.

Paths for AI-DLC are relative to its repository root.

| Mechanism | The factory | AI-DLC |
|---|---|---|
| Tests before the build | A tests leg writes them from the criteria; the driver requires that only test files changed, the suite is red, and each criterion's test is named in the red output; then they're locked by hash, the builder can't write them, and the gate re-hashes them (`factory/stages/tests.py:114-165`, `factory/ledger.py:456-477`, `factory/stages/gate.py:107-123`). No human approves them before they lock. | A "Testing Contract" in the plan, which a person approves before any code (`core/aidlc-common/stages/construction/code-generation.md:150-165, 206-340`). Red-then-green is done by the same agent that writes the code, and recording the red run is an instruction (`:389-444`). Nothing locks the test files; plan re-approval after edits applies only under Guard Policy `strict`, off by default in every scope except `enterprise` (`:271-275`, `docs/guide/workflow-profiles.md:53-58`). |
| Checks run by the system | Locked tests, gitleaks, osv-scanner, semgrep (added lines), install, typecheck, lint, build, tests, rollback rehearsal and ratchets, from config read at the baseline commit; repository commands run under macOS `sandbox-exec` (`factory/stages/gate.py`, `factory/isolation.py:5-25, 143-163`). | Six sensors, all advisory by default (`core/sensors/*.md`, `docs/reference/07-sensor-system.md:308-309`). One human-approved verification command is run and its exit code recorded (`core/tools/aidlc-construction-checkpoints.ts:1304-1364`). Scanners appear as agent knowledge and CI configuration it writes, not as checks it runs on the user's code (not found). No sandbox: "not a sandbox" (`core/hooks/runtime-integrity.ts:1-8`). |
| Independent review | Two reviewers by default, Claude and Codex, each blind to the builder's account and to each other, then a sort that can't clear a serious finding alone (`factory/stages/review.py`). The Codex reviewer's read-only sandbox can still read the whole disk (`DESIGN.md:103`). | One reviewer sub-agent per reviewed stage; it doesn't see the builder's diary but reads the code summary and plan (`core/aidlc-common/protocols/stage-protocol-reviewer.md:7, 133`). Default is Sonnet at medium effort on Claude Code (`docs/guide/06-agents.md:126`); another model family is an option. "The reviewer never blocks" (`06-agents.md:328`). |
| What the signer reads | One decision page built by code from the ledger, in plain words, with model-written text labelled as asserted (`factory/stages/warrant.py`). One gate, at the end. | Approval gates at the end of almost every stage, and plan approval before code (`docs/guide/07-interaction-modes.md:92, 115-132`); plain-language rules for the chat (`stage-protocol.md:60-92`); the artefacts are Markdown documents and code. |
| Audit trail | Every event hash-chained to the last, with an anchor kept outside the change folder and checked on every read; not cryptographic, and rewritable by someone with the operator's access (`factory/ledger.py:95-196`, `README.md`). | 121 event types; append-only by convention and a write guard, which its guide calls "a guardrail, not a security boundary" (`docs/guide/10-state-and-audit.md:154-157`). No per-event hash chain (not found). Commit-level provenance with signed commits (`docs/reference/20-commit-provenance.md`). |
| Isolation of the builder | Claude Code's sandbox forced on, writes denied to locked tests and records, secret paths unreadable, network allowlisted (`factory/isolation.py:218-242`). macOS only. | Harness permissions and ordering hooks; no OS sandbox or network control (`docs/reference/06-hooks-and-tools.md:241-242`). |
| Scope | 8 stages, release a stub; one change; macOS; Claude Code and Codex. About 5,000 lines of Python, v0.1.0. | 5 phases, 33 stages, 14 agents, requirements to operations; 7 coding tools; macOS, Linux and Windows; v2.11, an AWS Labs team. |
| Evidence it works | Pre-registered tests v3 to v9 with results, including where the review loses (`calibration/realbugs/results/`). | None found; benchmarks are on the roadmap (`docs/roadmap.md:309-314`). |

**Verdict.** AI-DLC is far broader and more mature, and it puts a person's approval of the plan before any code,
which the factory doesn't. On locked tests, system-run scanners in a sandbox, blind review by two model families, a
hash-chained log and a plain-words decision page, the factory enforces in code what AI-DLC leaves to instructions,
advisory checks or harness permissions. Neither authenticates who signs. The factory's evidence is small,
self-run, judged by a model and limited to its review stage.

*The comparison found one factory bug, since fixed (`897e6a8`): the decision page said "one from Anthropic, one from
OpenAI" whatever reviewers were configured.*
