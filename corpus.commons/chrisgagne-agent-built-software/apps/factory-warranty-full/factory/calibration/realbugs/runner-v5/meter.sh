#!/bin/zsh
# Reads Codex's usage meter: one tiny non-ephemeral call, then the rate limits its session file records.
CODEX=/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex
d=$(mktemp -d); (cd $d && "$CODEX" exec --skip-git-repo-check -m gpt-6.1-sol "Reply with the single word OK." < /dev/null > /dev/null 2>&1)
f=$(ls -t ~/.codex/sessions/*/*/*/*.jsonl | head -1)
python3 - "$f" <<'PY'
import json,sys
rl=None
for l in open(sys.argv[1]):
    try: r=json.loads(l)
    except: continue
    p=r.get('payload') or {}
    if p.get('type')=='token_count' and p.get('rate_limits'): rl=p['rate_limits']
print(f"5h {rl['primary']['used_percent']}%  week {rl['secondary']['used_percent']}%" if rl else "no meter reading")
PY
