You are auditing one part of a conformance matrix, blind: you did not write it, and you have not seen the reasoning of the agent who did. The matrix maps each requirement of a published standard to the mechanism in the "factory" (this repository: a harness that runs AI-built code changes through gates and blind AI review and hands a human a warranty pack) and gives each row a status.

Read first: `conformance/BRIEF.md` (the rules and status definitions the matrix had to follow), then `DESIGN.md` and `README.md`. Then the matrix file named below, then the source text(s) it covers, IN FULL (paths below). Check the factory's code wherever a row's mechanism or evidence depends on it: grep for every test name, ledger check name and fixture the matrix cites.

For EVERY row, check four things against the source text and the code, never against your own opinion of what is good enough:
1. Requirement: is the paraphrase faithful to the source text, the citation right, and any quoted words exact?
2. Mechanism: does the factory really do what the row says?
3. Evidence: does each cited test, check or fixture exist and show what the row claims?
4. Status: does it follow the brief's definitions exactly? (demonstrated needs BOTH an every-change ledger event AND a test or fixture showing the catch; partial coverage is asserted at best.)
Also report any requirement in the source that has no row, or rows the source does not support.

Your final message is ONLY a markdown document:
- a first line: `Rows checked: N. Agree: A. Disagree: D. Missing rows: M.`
- then a table of disagreements only: `| Row ID | Field | Matrix says | You say | Basis (source page/section, or file:line in the repo) |`
- then a list of missing or unsupported rows, each with its basis.
Be exact, and cite a basis for every disagreement. Where you agree, say nothing.
