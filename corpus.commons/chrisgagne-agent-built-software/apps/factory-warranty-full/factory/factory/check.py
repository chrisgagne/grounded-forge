"""factory check: the build leg's only shell command. It scans what the leg has written, then runs one of the gate's
commands.

OWASP Top 10 for Agentic Applications 2026, ASI05, asks to separate code generation from execution with a
validation gate (#5) and to scan before execution (#7). The leg writes; this scans the worktree as it stands
(invisible characters and secrets on what the leg changed, semgrep on the lines it added) and runs the named command
only if every scan passes. It runs inside the leg's sandbox, so it can't write outside the worktree or reach the
network: a registry semgrep ruleset can't be fetched here, so only a committed ruleset and the factory's pinned rules
run, and the gate runs the full set. The gate also runs everything again after the build commit. This is the leg's
check, never evidence.

  python -m factory.check SPEC.json NAME
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from factory.text import invisible_chars

BLOCKED = 3  # the exit code when a scan stops the command


class ScanError(Exception):
    """A scan couldn't establish what changed or couldn't run: the command doesn't run (fail closed)."""


def git(wt: Path, *args: str) -> str:
    r = subprocess.run(["git", "-c", "core.hooksPath=/dev/null", *args], cwd=wt, capture_output=True, text=True,
                       errors="surrogateescape")
    if r.returncode != 0:
        raise ScanError(f"git {args[0]} exited {r.returncode}: {r.stderr.strip()[:200]}")
    return r.stdout


def changed(wt: Path, baseline: str) -> dict[str, set[int] | None]:
    """Each file the leg changed since the baseline: the line numbers it added, or None for a new untracked file
    (every line is added)."""
    out, current = {}, None
    for line in git(wt, "diff", "-U0", "--no-color", "--no-ext-diff", baseline, "--").splitlines():
        if line.startswith("+++ "):
            current = None if line[4:] == "/dev/null" else line[4:].removeprefix("b/")
            if current:
                out.setdefault(current, set())
        elif line.startswith("@@") and current:
            m = re.search(r"\+(\d+)(?:,(\d+))?", line)
            start, count = int(m.group(1)), int(m.group(2) if m.group(2) is not None else 1)
            out[current].update(range(start, start + count))
    for f in git(wt, "ls-files", "--others", "--exclude-standard", "-z").split("\0"):
        if f:
            out[f] = None
    return {f: lines for f, lines in out.items() if (wt / f).is_file() and not (wt / f).is_symlink()}


def added(wt: Path, f: str, lines: set[int] | None) -> list[tuple[int, str]]:
    text = (wt / f).read_text(errors="replace").splitlines()
    return [(i, t) for i, t in enumerate(text, 1) if lines is None or i in lines]


def invisible(wt: Path, files: dict) -> list[str]:
    hits = []
    for f, lines in files.items():
        found = set()
        for _, t in added(wt, f, lines):
            found.update(invisible_chars(t.replace("\t", "")))
        if found:
            hits.append(f"{f}: {', '.join(sorted(found))}")
    return hits


def secrets(wt: Path, files: dict) -> list[str]:
    if not shutil.which("gitleaks"):
        return ["gitleaks is not on PATH, so the secrets scan can't run"]
    hits = []
    for f in files:
        r = subprocess.run(["gitleaks", "dir", "--no-banner", "--redact", "--ignore-gitleaks-allow",
                            "--report-format", "json", "--report-path", "-", "--", f],
                           cwd=wt, capture_output=True, text=True)
        if r.returncode not in (0, 1):
            return [f"gitleaks exited {r.returncode} on {f}: {r.stderr.strip()[:200]}"]
        try:
            found = json.loads(r.stdout or "[]")
        except json.JSONDecodeError:
            return [f"gitleaks' report on {f} isn't readable JSON"]
        hits += [f"{f}:{x.get('StartLine')} ({x.get('RuleID')})" for x in found]
    return hits


def sast(wt: Path, files: dict, configs: list[str]) -> list[str]:
    if not configs:
        return []
    if not shutil.which("semgrep"):
        return ["semgrep is not on PATH, so the static scan can't run"]
    tmp = Path(tempfile.mkdtemp(prefix="factory-check-"))
    env = {**os.environ, "SEMGREP_SETTINGS_FILE": str(tmp / "settings.yml"), "SEMGREP_LOG_FILE": str(tmp / "log"),
           "SEMGREP_VERSION_CACHE_PATH": str(tmp / "version"), "XDG_CONFIG_HOME": str(tmp), "HOME": str(tmp)}
    cmd = ["semgrep", "scan", *(a for c in configs for a in ("--config", c)), "--metrics=off", "--disable-version-check", "--disable-nosem",
           "--json", "--quiet", "--severity", "ERROR", "--severity", "WARNING", "--", *("./" + f for f in files)]
    try:
        r = subprocess.run(cmd, cwd=wt, capture_output=True, text=True, env=env)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if r.returncode != 0:  # without --error, findings exit 0; anything else means the scan didn't complete
        return [f"semgrep exited {r.returncode}: {r.stderr.strip()[-200:]}"]
    try:
        report = json.loads(r.stdout)
    except json.JSONDecodeError:
        return [f"semgrep's report isn't readable JSON: {r.stderr.strip()[-200:]}"]
    if report.get("errors"):
        return [f"semgrep reported errors: {str(report['errors'][0])[:200]}"]
    hits = []
    for x in report.get("results") or []:
        path = str(x.get("path", "")).removeprefix("./")
        span = set(range(int(x["start"]["line"]), int(x["end"]["line"]) + 1))
        lines = files.get(path)
        if lines is None or span & lines:
            hits.append(f"{path}:{x['start']['line']} ({x.get('check_id', '?').rsplit('.', 1)[-1]})")
    return hits


def scan(wt: Path, baseline: str, configs: list[str]) -> tuple[dict, list[str]]:
    """(the files changed since `baseline`, the problems the scans found). A scan that can't run is a problem."""
    try:
        files = changed(wt, baseline)
    except ScanError as e:
        return {}, [f"the check couldn't tell what changed ({e})"]
    problems = [f"invisible characters: {h}" for h in invisible(wt, files)]
    problems += [f"a secret: {h}" for h in secrets(wt, files)]
    problems += [f"semgrep: {h}" for h in sast(wt, files, configs)]
    return files, problems


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 2:
        print("usage: factory check SPEC.json NAME")
        return 2
    spec = json.loads(Path(args[0]).read_text())
    name, commands = args[1], spec["commands"]
    if name not in commands:
        print(f"no command named {name!r}; the check runs one of: {', '.join(commands)}")
        return 2
    wt = Path(spec["worktree"])
    files, problems = scan(wt, spec["baseline"], spec.get("semgrep_configs") or [])
    if problems:
        print(f"factory check: {name} did not run. The scans found problems in what you've written; fix them first:")
        print("\n".join(f"- {p}" for p in problems))
        return BLOCKED
    print(f"factory check: scans passed on {len(files)} changed file(s); running {name}: {commands[name]}", flush=True)
    return subprocess.run(["bash", "-c", commands[name]], cwd=wt).returncode


if __name__ == "__main__":
    sys.exit(main())
