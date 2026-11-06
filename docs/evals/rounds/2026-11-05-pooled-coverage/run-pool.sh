#!/bin/zsh
# run-pool.sh FAMILY BASE_DIR CONVERTED_DIR CASE...
fam=$1; base=$2; conv=$3; shift 3
cd "$base"
for c in "$@"; do
  out=$c/$fam; mkdir -p $out
  [[ -s $out/pool.json ]] && continue
  echo "$(date +%H:%M:%S) start $fam $c"
  msg="Read brief.md in this folder and follow it exactly. Read only files in this folder and in the converted-sources folder; open nothing else. Write pool.json to ./$fam/pool.json instead of ./pool.json."
  if [[ $fam == opus ]]; then
    ( cd $c && claude -p --model claude-opus-5-5 --effort high --allowedTools "Read" "Grep" "Glob" "Write" --add-dir "$conv" --output-format text "$msg" > opus/final.md 2> opus/claude.log )
  else
    codex exec -m gpt-6.1-sol -c model_reasoning_effort=high -s workspace-write --skip-git-repo-check --ephemeral -C "$PWD/$c" --add-dir "$conv" -o "$c/sol/final.md" "$msg" < /dev/null > $c/sol/codex.log 2>&1
  fi
  echo "$(date +%H:%M:%S) done $fam $c $( [[ -s $out/pool.json ]] && echo ok || echo NO-POOL)"
done
echo ALL DONE $fam $base
