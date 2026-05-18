#!/usr/bin/env bash
#
# Pass I audit-fixture regression runner.
#
# Use when adopting a new model in the 9-pass ingestion protocol, or after
# editing the Pass I procedure. The script prints each fixture in
# tests/audit-fixtures/, pauses for the operator to record whether Pass I
# (running under the candidate model) flagged the violation correctly,
# and writes a verdict log to tests/audit-fixtures/_runs/.
#
# This is intentionally not an LLM-in-the-loop runner: the article that
# motivated this corpus warns against mechanising the verdict, because
# self-evaluation bias re-enters. The operator records the verdict; the
# script's job is presentation and logging only.
#
# Usage:
#   bash tests/run-audit-fixtures.sh                    # interactive run
#   bash tests/run-audit-fixtures.sh --dry-run          # print fixtures, no logging
#   bash tests/run-audit-fixtures.sh --list             # one-line summary per fixture
#
# Run from the repo root.

set -euo pipefail

FIXTURE_DIR="tests/audit-fixtures"
RUNS_DIR="${FIXTURE_DIR}/_runs"

if [ ! -d "${FIXTURE_DIR}" ]; then
  echo "Error: ${FIXTURE_DIR} not found. Run this script from the repo root." >&2
  exit 1
fi

MODE="interactive"
case "${1:-}" in
  --dry-run) MODE="dry-run" ;;
  --list)    MODE="list" ;;
  -h|--help)
    sed -n '3,22p' "$0"
    exit 0
    ;;
  "") ;;
  *) echo "Unknown argument: $1" >&2; exit 2 ;;
esac

fixtures=$(find "${FIXTURE_DIR}" -maxdepth 1 -type f -name '[0-9][0-9]-*.md' | sort)
fixture_count=$(printf '%s\n' "${fixtures}" | grep -c . || true)

if [ "${fixture_count}" -eq 0 ]; then
  echo "Error: no fixtures found in ${FIXTURE_DIR}/." >&2
  exit 1
fi

if [ "${MODE}" = "list" ]; then
  for f in ${fixtures}; do
    id=$(grep -m1 '^id:' "$f" | sed 's/^id:[[:space:]]*//')
    mode=$(grep -m1 '^failure_mode:' "$f" | sed 's/^failure_mode:[[:space:]]*//')
    severity=$(grep -m1 '^severity:' "$f" | sed 's/^severity:[[:space:]]*//')
    printf '%-50s  %-10s  %s\n' "${id}" "${severity}" "${mode}"
  done
  exit 0
fi

# Capture run metadata (interactive mode only).
if [ "${MODE}" = "interactive" ]; then
  mkdir -p "${RUNS_DIR}"
  printf 'Candidate model identifier (e.g. claude-opus-4-7): '
  read -r MODEL_ID
  if [ -z "${MODEL_ID}" ]; then
    echo "Error: model identifier required." >&2
    exit 2
  fi
  RUN_DATE=$(date -u +%Y-%m-%d)
  RUN_TIME=$(date -u +%H%M%SZ)
  LOG="${RUNS_DIR}/${RUN_DATE}-${RUN_TIME}-${MODEL_ID}.md"
  {
    echo "# Pass I audit-fixture run"
    echo
    echo "**Model:** ${MODEL_ID}"
    echo "**Started (UTC):** ${RUN_DATE} ${RUN_TIME}"
    echo "**Fixture count:** ${fixture_count}"
    echo
    echo "| ID | Severity | Operator verdict | Notes |"
    echo "|---|---|---|---|"
  } > "${LOG}"
  echo
  echo "Logging to ${LOG}"
fi

i=0
for f in ${fixtures}; do
  i=$((i + 1))
  echo
  echo "============================================================"
  echo "Fixture ${i} of ${fixture_count}: $(basename "$f")"
  echo "============================================================"
  echo
  cat "$f"
  echo

  if [ "${MODE}" = "dry-run" ]; then
    continue
  fi

  echo "------------------------------------------------------------"
  echo "Run Pass I against this fixture using the candidate model."
  echo "Then record the operator verdict."
  echo
  printf 'Verdict, did Pass I flag the violation correctly? [pass / miss / overflag / skip]: '
  read -r VERDICT
  printf 'Notes (one line, optional): '
  read -r NOTES

  id=$(grep -m1 '^id:' "$f" | sed 's/^id:[[:space:]]*//')
  severity=$(grep -m1 '^severity:' "$f" | sed 's/^severity:[[:space:]]*//')
  printf '| %s | %s | %s | %s |\n' \
    "${id}" "${severity}" "${VERDICT}" "${NOTES}" >> "${LOG}"
done

if [ "${MODE}" = "interactive" ]; then
  {
    echo
    echo "**Completed (UTC):** $(date -u +%Y-%m-%d\ %H%M%SZ)"
  } >> "${LOG}"
  echo
  echo "Run complete. Log: ${LOG}"
  echo
  echo "Operator decision: does Pass I still earn its keep under ${MODEL_ID}?"
  echo "  - 'pass' on every violation fixture and the negative control → yes."
  echo "  - any 'miss' → investigate before rolling the model into ingestion."
  echo "  - 'overflag' on the negative control → re-tune calibration; an auditor"
  echo "    that flags clean material is as costly as one that misses violations."
fi
