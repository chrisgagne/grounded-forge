#!/usr/bin/env python3
"""Pass I driver regression tests: the sequencing, not the auditing.

`scripts/pass_i/run.py` runs Pass I as code: packet, two audit legs, sort,
apply, gate, stamp, fidelity check, provenance stamp. These tests swap the
`claude` and `codex` CLIs for stubs (via CLAUDE_BIN and CODEX_BIN) that write
the file each brief asks for, then check what the driver does with them. No
model runs, and no real corpus is touched: each case copies one open demo
source into a temp corpus.

Four properties, each a case that raises on failure:
  1. A full two-leg run stamps the deep reference, appends the second leg to the
     audit log, copies its records into `_audit/`, and stamps the derived tier.
  2. A failed gate stops the source before the stamp and writes
     decisions-needed.md; `--accept-gate` resumes from there without rerunning
     any leg.
  3. `--second none` skips the second leg and stamps audited-but-unverified.
  4. `--second claude` runs the second leg on the Claude stub, never Codex, and
     stamps audited-but-unverified.
  5. A deep-reference defect reported by the fidelity check stops the source
     before the provenance stamp; `--accept-gate` finishes it.
  6. `--promote-original` moves the original out of `sources/ingest/` and
     rewrites its path in the deep reference before the stamp, so the stamped
     hash is the final one.

Usage:
    python3 tests/pass-i-driver.test.py
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEMO = REPO / "corpus.commons/demo"
SLUG = "nhs-just-culture-guide"

STUB_CLAUDE = r'''#!/bin/bash
prompt="$2"; agent=""
for ((i=1;i<=$#;i++)); do [ "${!i}" = "--agent" ] && { j=$((i+1)); agent="${!j}"; }; done
echo "$prompt" >> "$STUB_CALLS"
if [ "$agent" = "ingest-auditor" ]; then
  log=$(echo "$prompt" | grep -o 'Write the log to `[^`]*`' | sed 's/.*`\(.*\)`/\1/')
  printf '# Pass I log\n\n12 claims audited, 1 corrected.\n' > "$log"
elif echo "$prompt" | grep -q 'apply leg'; then
  pk=$(echo "$prompt" | grep -o 'packet folder is `[^`]*`' | sed 's/.*`\(.*\)`/\1/')
  echo "{\"same_family\":\"12 claims audited, 1 corrected\",\"sort_result\":\"pass\",\"applied_note\":\"1 applied\",\"gate\":\"$STUB_GATE\",\"open\":[],\"derived_changes\":[]}" > "$pk/apply-report.json"
elif echo "$prompt" | grep -q 'fidelity check'; then
  f=$(echo "$prompt" | grep -o '`[^`]*fidelity-report.md`' | head -1 | tr -d '`')
  printf 'report\n\n## Summary for the audit log\n\nFidelity stub summary.\n' > "$f"
  echo "${STUB_DEEP_DEFECTS:-[]}" > "$(dirname "$f")/fidelity-deep-defects.json"
else
  out=$(echo "$prompt" | grep -o 'Write the complete report to [^ ]*' | sed 's/.* //; s/\.$//')
  printf 'second-leg report (claude)\n' > "$out"
fi
echo '{"result":"done","total_cost_usd":0.01,"session_id":"stub","num_turns":1,"modelUsage":{"stub-claude":{"costUSD":0.01}}}'
'''

STUB_CODEX = r'''#!/bin/bash
out=""; for ((i=1;i<=$#;i++)); do [ "${!i}" = "-o" ] && { j=$((i+1)); out="${!j}"; }; done
echo codex >> "$STUB_CALLS"
printf 'second-leg report (codex)\n' > "$out"; printf 'tokens used\n1,234\n'
'''


class Case:
    def __init__(self, scope: str | None = None):
        self.tmp = Path(tempfile.mkdtemp(prefix="pass-i-test-"))
        self.root = self.tmp / f"corpus-{self.tmp.name}"
        for sub in ("references/_audit", "sources/converted", "sources/original", "distillations"):
            (self.root / sub).mkdir(parents=True)
        lines = (DEMO / f"references/{SLUG}-deep.md").read_text().split("\n")
        (self.root / f"references/{SLUG}-deep.md").write_text(
            "\n".join(l for l in lines if not l.startswith("<!-- Pass I applied")))
        shutil.copy(DEMO / f"references/{SLUG}.md", self.root / "references")
        shutil.copy(DEMO / f"sources/converted/{SLUG}.md", self.root / "sources/converted")
        card = (DEMO / f"sources/original/{SLUG}.source.md").read_text()
        if scope:
            card = "\n".join(f"scope: {scope}" if l.startswith("scope:") else l for l in card.split("\n"))
        (self.root / f"sources/original/{SLUG}.source.md").write_text(card)
        for d in DEMO.glob(f"distillations/*/{SLUG}-*.md"):
            (self.root / "distillations" / d.parent.name).mkdir(exist_ok=True)
            shutil.copy(d, self.root / "distillations" / d.parent.name)
        for name, body in (("claude", STUB_CLAUDE), ("codex", STUB_CODEX)):
            p = self.tmp / f"stub-{name}.sh"
            p.write_text(body)
            p.chmod(0o755)
        self.calls = self.tmp / "calls.txt"
        self.work = REPO / "_planning/pass-i" / self.root.name / SLUG

    def run(self, *extra: str, gate: str = "pass", deep_defects: str = "[]") -> subprocess.CompletedProcess:
        env = {**os.environ, "CLAUDE_BIN": str(self.tmp / "stub-claude.sh"),
               "CODEX_BIN": str(self.tmp / "stub-codex.sh"), "STUB_CALLS": str(self.calls), "STUB_GATE": gate,
               "STUB_DEEP_DEFECTS": deep_defects}
        return subprocess.run([sys.executable, "-m", "scripts.pass_i.run", "--corpus", str(self.root), SLUG, *extra],
                              cwd=REPO, env=env, capture_output=True, text=True)

    def stamp(self) -> str:
        return self.deep_text().split("\n")[1]

    def deep_text(self) -> str:
        return (self.root / f"references/{SLUG}-deep.md").read_text()

    def log(self) -> str:
        return (self.root / f"references/_audit/_ingest_pass_I_{SLUG}_source_audit.md").read_text()

    def cleanup(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)
        shutil.rmtree(self.work.parent, ignore_errors=True)


def check(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def full_two_leg_run(c: Case) -> None:
    r = c.run()
    check(r.returncode == 0, f"run failed:\n{r.stdout}\n{r.stderr}")
    check(c.stamp().startswith("<!-- Pass I applied") and "Codex CLI" in c.stamp(), f"bad stamp: {c.stamp()}")
    check("## Second leg" in c.log() and "## Derived-tier fidelity check" in c.log(), "audit log sections missing")
    for k in ("blind", "sort", "prompts"):
        check((c.root / f"references/_audit/_ingest_pass_I_{SLUG}_crossfamily_{k}.md").exists(), f"no {k} record")
    check("derived-from-deep: sha256:" in (c.root / f"references/{SLUG}.md").read_text(), "light ref not stamped")


def gate_stops_then_accepts(c: Case) -> None:
    r = c.run(gate="fail")
    check(r.returncode == 1 and "stopped at gate" in r.stdout, f"gate did not stop:\n{r.stdout}")
    check("Pass I applied" not in c.deep_text(), "stamped despite a failed gate")
    check((c.work / "decisions-needed.md").exists(), "no decisions-needed.md")
    legs = c.calls.read_text().count("\n")
    r = c.run("--accept-gate", SLUG, gate="fail")
    check(r.returncode == 0, f"accept failed:\n{r.stdout}")
    check(c.stamp().startswith("<!-- Pass I applied"), "not stamped after --accept-gate")
    rerun = c.calls.read_text().split("\n")[legs:]
    check(not any("fix-in-place mode" in l or l == "codex" for l in rerun), "a leg reran after --accept-gate")


def no_second_leg(c: Case) -> None:
    r = c.run("--second", "none")
    check(r.returncode == 0, f"run failed:\n{r.stdout}")
    check("none (audited-but-unverified)" in c.stamp(), f"bad stamp: {c.stamp()}")
    check("codex" not in c.calls.read_text().split("\n"), "Codex ran with --second none")


def same_family_second_leg(c: Case) -> None:
    r = c.run("--second", "claude")
    check(r.returncode == 0, f"run failed:\n{r.stdout}")
    check("codex" not in c.calls.read_text().split("\n"), "Codex ran with --second claude")
    check("same family (audited-but-unverified)" in c.stamp(), f"bad stamp: {c.stamp()}")


def fidelity_deep_defect_stops(c: Case) -> None:
    r = c.run(deep_defects='["line 96: quotation marks misplaced"]')
    check(r.returncode == 1 and "stopped at deep_check" in r.stdout, f"deep defect did not stop:\n{r.stdout}")
    steps = json.loads((c.work / "status.json").read_text())["steps"]
    check("provenance" not in steps, "derived tier stamped before the fix")
    r = c.run("--accept-gate", SLUG, deep_defects='["line 96: quotation marks misplaced"]')
    check(r.returncode == 0, f"accept failed:\n{r.stdout}")
    digest = hashlib.sha256((c.root / f"references/{SLUG}-deep.md").read_bytes()).hexdigest()
    check(digest in (c.root / f"references/{SLUG}.md").read_text(), "derived tier not stamped after accept")


def promote_original(c: Case) -> None:
    pdf = c.root / "sources/ingest/original-file.pdf"
    pdf.parent.mkdir(parents=True, exist_ok=True)
    pdf.write_bytes(b"%PDF-1.4 stub original")
    digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
    card = c.root / f"sources/original/{SLUG}.source.md"
    card.write_text(re.sub(r"(?m)^checksum_sha256:.*$", f"checksum_sha256: {digest}", card.read_text()))
    deep = c.root / f"references/{SLUG}-deep.md"
    deep.write_text(deep.read_text() + "\nOriginal received as `sources/ingest/original-file.pdf`.\n")
    r = c.run("--promote-original")
    check(r.returncode == 0, f"run failed:\n{r.stdout}")
    check(not pdf.exists() and (c.root / "sources/original/original-file.pdf").exists(), "original not moved")
    check("sources/ingest/" not in c.deep_text(), "deep reference still names sources/ingest/")
    light = (c.root / f"references/{SLUG}.md").read_text()
    check(hashlib.sha256(deep.read_bytes()).hexdigest() in light, "derived stamp doesn't match the final deep reference")


def main() -> int:
    cases = [(full_two_leg_run, None), (gate_stops_then_accepts, None),
             (no_second_leg, None), (same_family_second_leg, "confidential"),
             (fidelity_deep_defect_stops, None), (promote_original, None)]
    failures = 0
    for fn, scope in cases:
        c = Case(scope)
        try:
            fn(c)
            print(f"  ok    {fn.__name__}")
        except AssertionError as e:
            failures += 1
            print(f"  FAIL  {fn.__name__}: {e}")
        finally:
            c.cleanup()
    print(f"\n{len(cases) - failures}/{len(cases)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
