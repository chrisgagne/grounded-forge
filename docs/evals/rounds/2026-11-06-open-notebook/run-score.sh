#!/bin/zsh
cd "${0:A:h}/work"
GF="$(git rev-parse --show-toplevel)"
fam=$1
for d in $fam/*/; do
  d=${d%/}
  [[ -s $d/score.json ]] && continue
  echo "$(date +%H:%M:%S) start $d"
  msg="Read brief.md in this folder and follow it exactly. Read only files in this folder and in the converted-sources folder; open nothing else."
  if [[ $fam == opus ]]; then
    ( cd $d && claude -p --model claude-opus-5-5 --effort high --allowedTools "Read" "Grep" "Glob" "Write" --add-dir "$GF/corpus.commons/demo/sources/converted" --output-format text "$msg Write score.json in this folder." > final.md 2> claude.log )
  else
    codex exec -m gpt-6.1-sol -c model_reasoning_effort=high -s workspace-write --skip-git-repo-check --ephemeral -C "$PWD/$d" --add-dir "$GF/corpus.commons/demo/sources/converted" -o "$d/final.md" "$msg Write score.json in this folder." < /dev/null > $d/codex.log 2>&1
  fi
  echo "$(date +%H:%M:%S) done $d $( [[ -s $d/score.json ]] && echo ok || echo NO-SCORE)"
done
echo ALL DONE $fam
