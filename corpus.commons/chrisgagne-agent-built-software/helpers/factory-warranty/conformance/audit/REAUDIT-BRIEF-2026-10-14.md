You are re-auditing 11 rows of a conformance matrix, blind. You did not write them and you have not seen the status
the author gave them: the rows in `conformance/audit/reaudit-rows-2026-10-14.md` carry no status and no note. The
factory (this repository) changed on 2026-10-14 (commits fbe025a..HEAD: a schema for the Codex reviewer, a stage-order
check before each stage command, and a "factory check" that is the only shell command the build and tests legs may
run). These 11 rows describe those changes.

Read first, in full: `conformance/BRIEF.md` (the status definitions) and `DESIGN.md`. Then the 11 rows and the
matrix's "How to read this" section, both in `conformance/audit/reaudit-rows-2026-10-14.md` (its caveats apply). To
stay blind, do not open `conformance/llm-agentic.md`, `conformance/BRIEF.md`'s neighbours under `conformance/` other
than BRIEF.md, or anything under `conformance/audit/` except these two files. Then, from the sources, the full text of every
entry the rows cite: in `grounded-forge/corpus.commons/chrisgagne-agent-built-software/sources/converted/owasp-llm-top10-2026.md`
the entries LLM01, LLM03, LLM07 and LLM10; in `.../converted/owasp-agentic-top10-2026.md` the entries ASI05, ASI07,
ASI08 and ASI09. Read each of those entries whole, not just the cited strategy. Then the code: `factory/check.py`,
`factory/hooks/guard.py`, `factory/stages/__init__.py`, `factory/stages/build.py`, `factory/stages/tests.py`,
`factory/stages/review.py`, `factory/legs.py`, `factory/cli.py`, `factory/isolation.py`, `factory/prompts/build.md`,
`factory/prompts/tests.md`, and every test the rows cite (grep for each name). `calibration/live-build-2026-10-14/`
holds one live build that used the check.

For EVERY row, judge against the source text and the code, never your own opinion of what is good enough:
1. Requirement: faithful to the source, citation right?
2. Mechanism: does the factory really do what the row says? Name any overclaim.
3. Evidence: does each cited test, check or file exist and show what the row claims?
4. Status: assign one yourself, by the brief's definitions exactly (demonstrated needs BOTH an every-change ledger
   event AND a test or fixture showing the catch; a strategy with several parts is demonstrated only if every part is;
   partial coverage is asserted at best; gap means nothing addresses the main ask).

Your final message is ONLY a markdown document:
- first line: `Rows: 11. Sources read: <entries, with line ranges>.`
- then one table with every row: `| Row ID | Your status | Mechanism accurate? (yes, or what is wrong) | Evidence holds? (yes, or what is wrong) | Basis (source entry and strategy, file:line) |`
- then any requirement in those entries that the changes now bear on but no row covers.
Be exact; cite a basis for every status.

Commit ids cited here (factory commits, not grounded-forge's) are from the factory's history before it was published.
