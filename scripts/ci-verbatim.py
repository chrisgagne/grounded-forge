#!/usr/bin/env python3
"""CI gate: verbatim quotes in every shipped app's distillations match their converted source.

Runs scripts/check-verbatim.py over corpus.commons/*/apps/*/distillations/ (what the compiled
apps and the MCP connectors serve) and fails on any failing finding (near, page, interrupted,
glyph, missing, wrong-source, no-quote) that isn't in the baseline, or on any source that
can't be found. The baseline, scripts/verbatim-baseline.json, lists the findings that were
open when the gate went in (5 Nov 2026), keyed by file, kind and quote, so line shifts don't
matter: they are repair work for an auditor, and a new mismatch can't join them unnoticed.
A baseline entry that no longer occurs is reported so it can be dropped.

    python3 scripts/ci-verbatim.py            # the CI check
    python3 scripts/ci-verbatim.py --update   # rewrite the baseline from the current findings
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASELINE = ROOT / "scripts" / "verbatim-baseline.json"
FAILING = {"glyph", "near", "page", "interrupted", "wrong-source", "missing", "no-quote"}


def shipped():
    return sorted(p.relative_to(ROOT).as_posix() for p in ROOT.glob("corpus.commons/*/apps/*/distillations/**/*.md")
                  if "INDEX" not in p.name.upper() and p.name != "README.md" and not p.name.startswith("_"))


def key(f):
    quote = " ".join((f.get("quote") or "").split())
    return f"{f['file']}|{f['kind']}|{hashlib.sha256(quote.encode()).hexdigest()[:16]}"


def findings(files):
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "check-verbatim.py"), "--json", *files],
                       cwd=ROOT, capture_output=True, text=True)
    try:
        out = json.loads(r.stdout)
    except ValueError:
        sys.exit(f"check-verbatim.py gave no JSON (exit {r.returncode}):\n{r.stderr[-2000:]}")
    return out["findings"], out.get("errors", [])


def judge(found, errors, baseline):
    """(new failing findings, baseline keys no longer found, errors)."""
    failing = {key(f): f for f in found if f["kind"] in FAILING}
    new = [f for k, f in failing.items() if k not in baseline]
    gone = sorted(set(baseline) - set(failing))
    return new, gone, errors


def main(argv):
    files = shipped()
    found, errors = findings(files)
    if "--update" in argv:
        keys = sorted({key(f) for f in found if f["kind"] in FAILING})
        BASELINE.write_text(json.dumps(keys, indent=1) + "\n")
        print(f"baseline: {len(keys)} open finding(s) written to {BASELINE.relative_to(ROOT)}")
        return 0
    baseline = set(json.loads(BASELINE.read_text())) if BASELINE.exists() else set()
    new, gone, errors = judge(found, errors, baseline)
    print(f"{len(files)} shipped distillation(s) checked; {len(baseline)} baselined finding(s) still open: "
          f"{len(baseline) - len(gone)}")
    for k in gone:
        print(f"  resolved (drop from the baseline): {k}")
    for e in errors:
        print(f"::error::{e}")
    for f in new:
        print(f"::error file={f['file']},line={f.get('line', 1)}::verbatim {f['kind']}: {f.get('quote', '')[:200]}")
    if new or errors:
        print(f"{len(new)} new verbatim finding(s), {len(errors)} error(s). Correct the quote to the source's "
              "words, or paraphrase it and change the marker (scripts/check-verbatim.py explains each kind).")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
