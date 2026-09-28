#!/bin/bash
# Cloud sessions only: copy Chris's voice skills from the private
# job-search-ops repo into this checkout's .claude/skills/. A cloud session
# loads repo-committed skills and none of the claude.ai account's plugins, and
# this repo is public, so the skills can't be committed here. The copies are
# gitignored, and Claude Code picks up new skills in .claude/skills/ without a
# restart. Never fails session start.

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

log() { echo "[fetch-voice-skills] $*" >&2; }

DEST="$CLAUDE_PROJECT_DIR/.claude/skills"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

if ! git clone -q --depth 1 https://github.com/chrisgagne/job-search-ops.git "$TMP/jso" 2>/dev/null; then
  log "job-search-ops not reachable; add it to this cloud session to load the voice skills"
  exit 0
fi

for src in "$TMP"/jso/plugins/voice/skills/*/; do
  name=$(basename "$src")
  # Never overwrite a skill this repo tracks.
  if git -C "$CLAUDE_PROJECT_DIR" ls-files --error-unmatch ".claude/skills/$name" >/dev/null 2>&1; then
    log "skipped $name: this repo tracks a skill with that name"
    continue
  fi
  rm -rf "${DEST:?}/$name"
  cp -R "$src" "$DEST/$name"
  log "loaded $name"
done

exit 0
