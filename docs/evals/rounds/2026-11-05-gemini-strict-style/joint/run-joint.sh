#!/bin/zsh
cd "${0:A:h}/sol-base"
fam=$1
for d in gemini-*/; do
  d=${d%/}
  if [[ $fam == sol ]]; then
    [[ -s $d/result.json ]] && continue
    echo "$(date +%H:%M:%S) start sol $d"
    codex exec -m gpt-6.1-sol -c model_reasoning_effort=high -s read-only --skip-git-repo-check --ephemeral -C "$PWD/$d" -o "$d/result.json" "Read brief.md and follow it exactly." < /dev/null > "$d/codex.log" 2>&1
  else
    [[ -s $d/result-claude.json ]] && continue
    echo "$(date +%H:%M:%S) start opus $d"
    ( cd "$d" && claude -p --model claude-opus-5-5 --effort high --allowedTools "Read" --output-format text "Read brief.md in the current folder and follow it exactly. Read packet.md in full. Do not read any other file. Your final message is the JSON object only." > result-claude.json 2> claude.log )
  fi
  echo "$(date +%H:%M:%S) done $d rc=$?"
done
echo ALL DONE $fam
