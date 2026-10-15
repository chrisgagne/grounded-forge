# The factory's first real job (2026-10-14)

The job: add a pinned semgrep rule that flags `eval`, `new Function` and Python's `exec` on input that isn't a string
literal (`story.md`). It's a real backlog item, from the matrix's PROPOSED fix for OWASP ASI05.2. It ran on a throwaway
clone of this repo, with `config.yaml` committed there as the target's factory config. The driver was this repo's
factory at `3b52990` (attempts 2 and 3).

| Attempt | Stopped at | Why | What changed |
|---|---|---|---|
| 1 | tests | The baseline suite was red inside the gate's sandbox: the factory's own tests assumed sandbox-exec could nest, semgrep died with no TLS trust anchors (the profile blocks the macOS security service), and semgrep couldn't write its settings under HOME | `3b52990`: test apps follow sandbox availability; commands get a CA file on macOS; semgrep's files go to the run's temp folder. The suite now passes inside the gate profile |
| 2 | tests | The red run never named AC-14's test: an existing test meant to keep passing, which `pytest -q` prints as a dot | The target's test command became `pytest -q -rA`; DESIGN now says a test command must name every test it runs |
| 3 | — | READY TO SIGN | — |

Attempt 3: spec $0.34, tests leg $1.13, build leg $0.63, Claude reviewer $0.55, sort $0.28 (about $2.93 of Claude), and
66,699 Codex review tokens. The change is `change.patch`: a new rule file (57 lines) and its tests (259 lines). The
gate passed with the full suite. Review confirmed two low findings, both below the blocking bar, listed in
`warranty.md` under residual risks. The rule doesn't catch `Function()` without `new`, `vm.runIn*`, a string
`setTimeout` or an aliased eval. And the conformance matrix still says no such rule exists. The guard blocked two
tests-leg calls and one build-leg call that went outside the check; each leg carried on with its file tools.

**Not signed.** Signing is the accountable person's step, at a terminal, in the clone that holds the change's ledger.
If the pack is signed, `change.patch` applies to this repo with `git am`.

Commit ids cited here (factory commits, not grounded-forge's) are from the factory's history before it was published.
