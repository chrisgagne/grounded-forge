You are reviewing a change before it merges. The repository is checked out at the change's head; the branch `base` is where the change started, and the whole change is in $diff (`git diff base...HEAD`).

What the author says about it:
$story

Review it as a careful senior engineer and report every issue worth raising. Your final message is ONLY a JSON array, no prose and no code fence, one object per issue:
{"file": "path from the repository root", "start_line": 1, "end_line": 1, "severity": "critical|high|medium|low", "message": "what is wrong and why it matters"}
An empty array if you find nothing.
