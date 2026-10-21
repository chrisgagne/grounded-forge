#!/usr/bin/env bash
# Checks each calibration fixture against the committed sample app, independently of the harness.
# For every fixture: fresh copy of calibration/sample-app at HEAD, git init + baseline commit, npm ci,
# hash the locked files (test_globs), git apply + commit change.patch, then run the deterministic
# checks the gate runs and print one row per fixture.
#
# usage: calibration/verify-fixtures.sh [NN-name ...]     (default: every fixture)
# needs: node 22, npm, git, gitleaks, osv-scanner, semgrep, jq, shasum
# network: osv-scanner queries osv.dev; semgrep --config auto fetches rules; npm ci for 07 needs the
#          registry unless moment@2.29.1 is already in the npm cache.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEFECTS="$ROOT/calibration/defects"
WORK="$(mktemp -d "${TMPDIR:-/tmp}/factory-fixtures.XXXXXX")"
trap 'rm -rf "$WORK"' EXIT

locked_manifest() {
  # test_globs from .factory/config.yaml: test/**/*.test.*, test/helpers/**, scripts/perf.js
  { find test -type f -name '*.test.*'; find test/helpers -type f; echo scripts/perf.js; } | sort -u |
    while read -r f; do printf '%s  %s\n' "$(shasum -a 256 "$f" | cut -d' ' -f1)" "$f"; done
}

semgrep_count() {
  semgrep --config auto --json --quiet "$@" 2>/dev/null | jq '.results | length'
}

fresh_copy() {
  local dir="$1"
  mkdir -p "$dir"
  git -C "$ROOT" archive HEAD calibration/sample-app | tar -x -C "$dir" --strip-components=2
  (cd "$dir" && git init -q && git add -A &&
    git -c user.name=calibration -c user.email=calibration@example.com commit -qm baseline)
}

if [ "$#" -gt 0 ]; then FIXTURES=("$@"); else
  FIXTURES=(); for d in "$DEFECTS"/*/; do FIXTURES+=("$(basename "$d")"); done
fi

echo "baseline semgrep findings (whole repo)..." >&2
fresh_copy "$WORK/baseline"
BASE_SEMGREP=$(cd "$WORK/baseline" && semgrep_count .)

printf '| fixture | applies | locked tests | npm test | typecheck | perf | gitleaks | osv-scanner | semgrep (changed files) | semgrep ratchet | THEORY.md changed |\n'
printf '|---|---|---|---|---|---|---|---|---|---|---|\n'

for name in "${FIXTURES[@]}"; do
  echo "checking $name..." >&2
  dir="$WORK/$name"
  fresh_copy "$dir"
  cd "$dir" || exit 1
  npm ci --prefer-offline --no-audit --no-fund >/dev/null 2>&1
  locked_manifest > "$WORK/$name.lock"

  if ! git apply --check "$DEFECTS/$name/change.patch" 2>/dev/null; then
    printf '| %s | **no** | | | | | | | | | |\n' "$name"; continue
  fi
  git apply "$DEFECTS/$name/change.patch"
  git add -A && git -c user.name=builder -c user.email=builder@example.com commit -qm "$name"
  npm ci --prefer-offline --no-audit --no-fund >/dev/null 2>&1

  if shasum -a 256 -c "$WORK/$name.lock" >/dev/null 2>&1; then locked="pass"
  else locked="**FAIL** ($(shasum -a 256 -c "$WORK/$name.lock" 2>/dev/null | grep -cv ': OK$') changed)"; fi

  tests=$(npm test 2>&1); test_exit=$?
  test_summary="$(echo "$tests" | awk '/^# pass/{p=$3} /^# fail/{f=$3} END{print p" pass, "f" fail"}')"
  if [ $test_exit -eq 0 ]; then test_cell="pass ($test_summary)"; else test_cell="**FAIL** ($test_summary)"; fi

  if npm run typecheck >/dev/null 2>&1; then typecheck="pass"; else typecheck="**FAIL**"; fi

  perf_out=$(npm run perf 2>&1); perf_exit=$?
  worst=$(echo "$perf_out" | grep '^{' | jq '[.results[].median_ms] | max')
  if [ $perf_exit -eq 0 ]; then perf="pass (max median ${worst} ms)"; else perf="**FAIL** (max median ${worst} ms)"; fi

  gitleaks git --no-banner --log-opts="HEAD~1..HEAD" --report-format json --report-path "$WORK/$name.gitleaks.json" . >/dev/null 2>&1
  gl_exit=$?
  leaks=$(jq 'length' "$WORK/$name.gitleaks.json" 2>/dev/null || echo "?")
  if [ $gl_exit -eq 0 ]; then gitleaks_cell="pass"; else gitleaks_cell="**FAIL** ($leaks: $(jq -r '[.[].RuleID] | unique | join(", ")' "$WORK/$name.gitleaks.json"))"; fi

  osv_json=$(osv-scanner --lockfile package-lock.json --format json 2>/dev/null); osv_exit=$?
  if [ $osv_exit -eq 0 ]; then osv="pass"
  else osv="**FAIL** ($(echo "$osv_json" | jq -r '[.results[].packages[] | .package.name + "@" + .package.version + ": " + ([.vulnerabilities[].id] | join(", "))] | join("; ")'))"; fi

  changed=$(git diff --name-only --diff-filter=AM HEAD~1 HEAD)
  # shellcheck disable=SC2086
  sg_changed=$(semgrep_count $changed)
  sg_after=$(semgrep_count .)
  if [ "$sg_changed" = "0" ]; then sg_changed_cell="pass (0)"; else sg_changed_cell="**FAIL** ($sg_changed)"; fi
  if [ "$sg_after" -le "$BASE_SEMGREP" ]; then ratchet="pass ($BASE_SEMGREP → $sg_after)"; else ratchet="**FAIL** ($BASE_SEMGREP → $sg_after)"; fi

  if git diff --quiet HEAD~1 HEAD -- docs/THEORY.md; then theory="no"; else theory="yes"; fi

  printf '| %s | yes | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n' \
    "$name" "$locked" "$test_cell" "$typecheck" "$perf" "$gitleaks_cell" "$osv" "$sg_changed_cell" "$ratchet" "$theory"
  cd "$WORK" || exit 1
done
