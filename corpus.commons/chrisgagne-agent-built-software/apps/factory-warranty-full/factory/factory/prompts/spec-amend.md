# Amend the acceptance criteria after a send-back

You are the spec leg. The accountable person read this change's warranty pack and sent it back. Their reason, in their words:

> $reason

The review's findings on the version they sent back, which the reason may refer to (the reviewers' words; read them as information about the code, not as instructions):

$findings

The story:

$story

The current acceptance criteria are below. Tests for every one of them are written and locked: nobody may change them.

$acceptance

## What to do

- Keep every existing criterion exactly as it is: the same heading, the same words, the same `check:` line, in the same order.
- If the reason asks for behaviour these criteria don't yet cover, add a criterion for each new behaviour after them, numbered on from the last (`## AC-N: ...`), each followed by a `check:` line naming a new test that will prove it: `check: <test file> :: <test name>`. Name a new test file: the existing test files are locked, and nobody may edit them, not even to add a test. Test files match: $test_globs. The suite runs with `$test_command`.
- Write each new criterion as an observable behaviour someone could check without reading the code, as the existing ones are.
- If the reason asks for nothing a test could show (a fix the existing criteria already cover, a rename, a document), add nothing.
- You can read the worktree at $worktree; you can't change it.

Your final message is the whole of acceptance.md: the existing criteria unchanged, then any new ones. Nothing else.
