#!/bin/zsh
cd "${0:A:h}"
GF="$(git rev-parse --show-toplevel)"
fam=$1
for d in $fam/gemini-*/; do
  d=${d%/}; id=${d#*/}
  [[ -s $d/$id.score.json ]] && continue
  echo "$(date +%H:%M:%S) start $d"
  if [[ $fam == sol ]]; then
    codex exec -m gpt-6.1-sol -c model_reasoning_effort=high -s workspace-write --skip-git-repo-check --ephemeral -C "$PWD/$d" --add-dir "${GF}/corpus.commons/demo/sources/converted" -o "$d/final.md" "$(cat $d/prompt.md)" < /dev/null > "$d/codex.log" 2>&1
  else
    ( cd $d && claude -p --model claude-opus-5-5 --effort high --allowedTools "Read" "Grep" "Glob" "Write" --add-dir "${GF}/corpus.commons/demo/sources/converted" --output-format text "$(cat prompt.md)" > final.md 2> claude.log )
  fi
  echo "$(date +%H:%M:%S) done $d rc=$? $( [[ -s $d/$id.score.json ]] && echo scored || echo NO-SCORE)"
done
echo ALL DONE $fam
