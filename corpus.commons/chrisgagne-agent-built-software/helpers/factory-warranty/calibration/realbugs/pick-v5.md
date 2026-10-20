You are choosing the cases for a pre-registered comparison of how often three AI code reviewers wrongly stop good changes. The factory's builder and its operator must not choose cases; you do. Twelve open-source projects are cloned under ./repos/: the eight in ./projects.json and the four in ./projects-v5.json. Use git (log, show, diff, -S searches) to inspect their default-branch history. You may not modify anything. The commits listed in ./used-commits-v5.txt were used before: never pick one of them.

Each case will be replayed like this:
- BUG case, from a real bug-fix commit F with parent P: the reviewers' baseline is F's tree with the fix's TEST-file changes undone; the change it reviews is the reverse of F's NON-test changes (so the buggy code comes back). No reviewer sees F's commit message, its tests or its issue.
- CONTROL case, from a real non-fix commit C with parent P: the baseline is P's tree; the change is C's NON-test changes. Test-file changes are dropped.
- Each change is presented with the same neutral story: "A contributor's change to <project>. Review it before it merges."

Pick 15 CONTROL cases from these twelve projects: at most 2 from any one project, and at least 5 from the four projects in ./projects-v5.json. There are no BUG cases this time; ignore the BUG rules below except where the CONTROL rules refer to them.

BUG cases must ALL hold:
1. The commit fixes incorrect behaviour (a logic or correctness bug). Not security, not performance, not docs, not typings-only, not build/CI/tooling, not dependency bumps, not lint/style.
2. The same commit adds or changes a regression test, which is evidence the old behaviour was wrong.
3. Its non-test change is small and self-contained: at most 3 code files, at most 40 changed lines in code files, no generated files (dist/, build output, lockfiles, package.json), not a merge commit.
4. A careful reviewer could in principle see the defect from the reverted diff plus the surrounding source, without an external spec beyond common knowledge of the domain.
5. Prefer fixes whose code diff does not consist mostly of comments that name the bug.
CONTROL cases must ALL hold:
1. A feature, refactor or behaviour change that is not a bug fix, touching source code (at most 3 code files and at most 60 changed lines in code files, no generated files, no package.json or lockfile; if it changes behaviour, the same commit updates the tests).
2. No later commit reverts it or fixes a bug it introduced: check the following history for reverts and for fixes touching the same lines or naming it. Say what you checked.
If a case looks like it could trip a content-safety filter, skip it and pick another.

Do not split the cases. Give each case an opaque id x01..x15 assigned in random order (not grouped by project or kind), and state the random seed or method you used.

For every case record: test_files = the commit's changed files that are tests or test fixtures; code_files = the other changed files (must be non-empty).

Your final message is ONLY a JSON object, no prose and no code fence:
{"method": "how you assigned ids, with the seed", "cases": [CASE, ...]}
where CASE = {"id": "xNN", "kind": "bug"|"control", "project": "<folder under repos/>", "commit": "<full sha of F or C>", "parent": "<full sha of P>", "code_files": [...], "test_files": [...], "code_lines_changed": N, "ground_truth": "BUG: one or two sentences on what the buggy (pre-fix) code does wrong, with an input that shows it, taken from the commit and its test. CONTROL: one sentence on what the commit does.", "evidence": "BUG: the commit subject and the test that shows the defect. CONTROL: the commit subject and what you checked to believe it was never fixed or reverted."}
