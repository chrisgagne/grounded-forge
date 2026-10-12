#!/usr/bin/env bash
#
# Run every automated test: tests/*.test.py and tests/*.test.js.
# Prints one line per test file and the output of any that fail; exits
# non-zero if any fail. run-audit-fixtures.sh is left out: it is an
# operator-in-the-loop review, not an automated check.
#
# Usage (from anywhere in the repo):
#   npm test
#   bash tests/run-all.sh

set -uo pipefail

cd "$(git rev-parse --show-toplevel)" || exit 2

failed=()
for t in tests/*.test.py tests/*.test.js; do
  case "$t" in
    *.py) cmd=(python3 "$t") ;;
    *.js) cmd=(node "$t") ;;
  esac
  if out=$("${cmd[@]}" 2>&1); then
    echo "ok    $t"
  else
    echo "FAIL  $t"
    echo "$out" | sed 's/^/      /'
    failed+=("$t")
  fi
done

echo
if [ ${#failed[@]} -eq 0 ]; then
  echo "All test files passed."
else
  echo "${#failed[@]} test file(s) failed: ${failed[*]}"
  exit 1
fi
