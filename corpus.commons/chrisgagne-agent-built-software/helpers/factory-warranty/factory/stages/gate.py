"""Stage 5, gate: deterministic checks on the built change. Any fail blocks.

Checks, each one ledger event:
  locked-tests  re-check test files against tests.lock (content, type, mode) and tests.lock against the ledger
  install typecheck lint build tests perf   the repo's commands, sandboxed; skipped when not configured
  secrets       gitleaks on the change's commits (gitleaks:allow comments ignored)
  deps          osv-scanner on the lockfiles and requirements files the change touched (exit 128, no packages, is
                skipped); a dependency change with no lockfile change fails, since nothing new can be scanned
  sast          semgrep (configured ruleset plus factory's pinned rules, nosemgrep comments ignored) on the files
                the change touched; a finding on a line the change adds fails, as do scanner errors
  rollback      for migration/irreversible classes, or when the change writes rollback.md: its `rehearse:` command, run sandboxed
  invisible     invisible, bidirectional or control characters on added lines (acceptable by a human)
  added-tests   test files the build added outside the lock; a human decides unless the runner isolates each file
  surface       the change edits files that steer the tests or the scanners (runner config, package.json scripts,
                .semgrepignore, .gitleaks.toml, ...) without them being locked
  ratchet:NAME  counts that may not rise: `absolute` (no rise at all) or `density` (per 1,000 non-blank lines of
                the scanned files, within a tolerance)
  required      every gate a risk class in risk.json requires ran and passed (not skipped)
  unchanged     after the gate's commands have run, the code and the locked tests are what the gate started with
plus an info event recording whether the theory doc changed.

Fail closed: a command that times out, can't be sandboxed, or a measurement the driver can't read is a fail.
Only a measured ratchet rise, a surface change, unlocked test files the build added and added invisible characters can
be accepted by the human (`factory accept --item ratchet:NAME|surface|added-tests|invisible`); measurement errors can't.
When a scanner fails, the change's own commands (install, build, tests) don't run: its code isn't executed, with
network, after the factory has already found a reason to stop it.
"""
from __future__ import annotations

import json
import re
import shlex
import shutil
import tomllib
from pathlib import Path

from factory import legs
from factory.hooks.guard import globmatch
from factory.ledger import sha256_file
from factory.stages.tests import check_lock, identity

PINNED_RULES = Path(__file__).resolve().parent.parent / "rules" / "semgrep"
LOCKFILES = ("package-lock.json", "npm-shrinkwrap.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock", "uv.lock",
             "Pipfile.lock", "Cargo.lock", "go.sum", "Gemfile.lock", "composer.lock")
REQUIREMENTS = re.compile(r"(^|/)requirements[\w.-]*\.txt$")  # osv-scanner reads these directly
COMMANDS = (("install", "install"), ("typecheck", "typecheck"), ("lint", "lint"), ("build", "build"),
            ("tests", "test"), ("perf", "perf"))
# Files that change how the tests run or what the scanners see. A change to one that isn't locked needs the human.
SURFACE_GLOBS = ["**/conftest.py", "**/pytest.ini", "**/tox.ini", "**/setup.cfg", "**/jest.config.*",
                 "**/vitest.config.*", "**/vitest.workspace.*", "**/.mocharc*", "**/karma.conf.*",
                 "**/playwright.config.*", "**/ava.config.*", "**/.nycrc*", "**/.c8rc*", "**/phpunit.xml*",
                 "**/.semgrepignore", "**/.semgrep.yml", ".semgrep/**", "**/.gitleaks.toml", "**/.gitleaksignore",
                 "**/osv-scanner.toml", "**/.eslintrc*", "**/eslint.config.*", "**/.eslintignore", ".factory/**",
                 # Agent instruction and settings files: every later leg, and every agent in the repo after merge, reads
                 # them as instructions (OWASP LLM Top 10 2026, LLM01 prompt injection).
                 "**/CLAUDE.md", "**/CLAUDE.local.md", "**/AGENTS.md", ".claude/**", "**/.mcp.json", ".codex/**",
                 "**/.cursorrules", ".cursor/**", ".github/copilot-instructions.md"]
PACKAGE_KEYS = ("scripts", "jest", "mocha", "ava", "c8", "nyc", "eslintConfig")
PYPROJECT_TABLES = ("pytest", "coverage", "ruff", "semgrep")
FIX_BUILD = "Fix the implementation (never the locked tests): `factory build`, then `factory gate` and `factory review`."
UNBLOCK = {
    "locked-tests": "Restore the locked test files to their locked content, then rebuild. Locked tests change only "
                    "through a new `factory tests` run.",
    "install": "Fix what the install log shows, then rebuild.",
    "secrets": "Remove the secret from the change's commits and rotate it, then rebuild.",
    "deps": "Upgrade or drop the vulnerable dependency (see gate/deps.log), or commit the updated lockfile, then rebuild.",
    "sast": "Fix the flagged code (see gate/sast.log), then rebuild.",
    "rollback": "Add rollback.md at the worktree root with a `rehearse: <command>` line whose command restores the "
                "previous state against a test database and exits 0 only when it did, then rebuild.",
    "required": "Make the required gate run and pass (see the risk classes in risk.json), then re-run the gate.",
    "unchanged": "Find what changed the code or a locked test while the gate ran, then re-run the gate.",
}


def run(change) -> bool:
    change.start("gate")
    at_start = change.code_state()
    locked_at_start = locked_snapshot(change)
    legs.record_tools(change, "gate", ("gitleaks", "osv-scanner", "semgrep"))
    # The factory's own scanners read the change before any of its code runs (install, build, tests).
    events = [locked_tests(change), secrets(change), deps(change), sast(change), invisible(change)]
    scan_failed = [e["check"] for e in events if e["status"] == "fail" and not e.get("acceptable")]
    for check, key in COMMANDS:
        cmd = change.config["commands"].get(key)
        if cmd and scan_failed:
            events.append(change.record("gate", "skipped", check=check, applies=False,
                                        reason=f"not run: {', '.join(scan_failed)} already failed, so the change's code "
                                               "isn't executed"))
            continue
        events.append(change.run_check("gate", check, cmd) if cmd else
                      change.record("gate", "skipped", check=check, reason=f"commands.{key} is not configured"))
    events += [rollback(change), surface(change), added_tests(change)]
    events += ratchet(change)
    events.append(required(change, events))
    events.append(unchanged(change, at_start, locked_at_start))
    theory_doc(change)
    failed = [e for e in events if e["status"] == "fail"]
    acceptable = [e["check"] for e in failed if e.get("acceptable")]
    reasons = [f"gate:{e['check']} failed (event {e['id']}): {e.get('reason') or 'see its log'}" for e in failed]
    unblock = [UNBLOCK.get(e["check"], FIX_BUILD) for e in failed if not e.get("acceptable")]
    unblock += [f"Undo it, or accept it with a reason: `factory accept --change {change.id} --item {r} --reason ... "
                f"--by NAME`." for r in acceptable]
    return change.finish("gate", reasons, list(dict.fromkeys(unblock)), blocking=acceptable,
                         acceptable=bool(failed) and len(acceptable) == len(failed))


def locked_tests(change) -> dict:
    lock = change.dir / "tests.lock"
    if not lock.exists():
        return change.record("gate", "fail", check="locked-tests", reason="no tests.lock")
    written = [e for e in change.ledger.events() if e.get("check") == "lock"]
    recorded = written[-1].get("artefacts", {}).get("tests.lock") if written else None
    if not recorded or recorded != sha256_file(lock):
        return change.record("gate", "fail", check="locked-tests", lock_sha256=sha256_file(lock),
                             recorded_sha256=recorded, reason="tests.lock changed since it was written" if recorded
                             else "no ledger event records writing tests.lock")
    r = check_lock(change)
    bad = r["changed"] + r["missing"]
    reason = "; ".join(filter(None, [r["changed"] and f"changed: {', '.join(r['changed'])}",
                                     r["missing"] and f"missing: {', '.join(r['missing'])}"])) or None
    return change.record("gate", "fail" if bad else "pass", check="locked-tests", locked=r["locked"],
                         changed=r["changed"] or None, missing=r["missing"] or None, added=r["added"] or None,
                         lock_sha256=sha256_file(lock), reason=reason)


def locked_snapshot(change) -> dict:
    """(sha256, mode) of every locked path now; None when it is missing."""
    files, _ = change.locked_paths()
    return {f: identity(Path(f)) if Path(f).is_symlink() or Path(f).exists() else None for f in files}


def unchanged(change, at_start: dict, locked_at_start: dict) -> dict:
    """After every command: the code and the locked tests are what the gate started with."""
    now_ = change.code_state()
    moved = sorted(f for f, v in locked_snapshot(change).items() if locked_at_start.get(f) != v)
    problems = []
    if (now_["commit"], now_["tree"]) != (at_start["commit"], at_start["tree"]):
        problems.append(f"HEAD moved from {at_start['commit'][:12]} to {now_['commit'][:12]} while the gate ran")
    if not at_start["clean"] or not now_["clean"]:
        problems.append("the worktree has uncommitted changes" + (" after the gate's commands" if at_start["clean"] else ""))
    if moved:
        problems.append(f"locked tests changed while the gate ran: {', '.join(moved)}")
    return change.record("gate", "fail" if problems else "pass", check="unchanged", reason="; ".join(problems) or None,
                         **at_start)


def tool_missing(change, check: str, tool: str) -> dict | None:
    if shutil.which(tool):
        return None
    return change.record("gate", "fail", check=check, reason=f"{tool} is not on PATH, so this gate cannot run")


def secrets(change) -> dict:
    report = change.path("gate/gitleaks.json")
    cmd = (f"gitleaks git --no-banner --redact --ignore-gitleaks-allow "
           f"--log-opts={shlex.quote(f'{change.baseline}..HEAD')} "
           f"--report-format json --report-path {shlex.quote(str(report))} .")
    return tool_missing(change, "secrets", "gitleaks") or change.run_check("gate", "secrets", cmd, trusted=True)


def risk_classes(change) -> dict:
    path = change.dir / "risk.json"
    return json.loads(path.read_text()).get("classes", {}) if path.exists() else {}


def deps(change) -> dict:
    changed = change.changed_files()
    touched = [f for f in changed if (Path(f).name in LOCKFILES or REQUIREMENTS.search(f))
               and (change.worktree / f).exists()]
    dep_class = risk_classes(change).get("dependency", {})
    if not touched:
        if "gate:deps" in dep_class.get("required_gates", []):
            return change.record("gate", "fail", check="deps", reason="the change touches dependencies (risk class "
                                 "dependency) but no lockfile or requirements file changed, so the new dependencies "
                                 "can't be scanned; commit the updated lockfile")
        return change.record("gate", "skipped", check="deps", reason="the change touches no lockfile", applies=False)
    cmd = "osv-scanner scan source --format json " + " ".join(f"-L {shlex.quote('./' + f)}" for f in touched)
    # Exit 1 is findings and other non-zero exits are tool errors: both fail. 128 means no packages to scan.
    return tool_missing(change, "deps", "osv-scanner") or change.run_check(
        "gate", "deps", cmd, trusted=True, skip_exits={128: "osv-scanner found no package sources in the touched "
                                                            "lockfiles: no dependencies scanned"})


# semgrep writes its settings, log and version cache under HOME; in a sandbox HOME isn't writable, so they go to the
# run's private temp folder.
SEMGREP_FILES = ('SEMGREP_SETTINGS_FILE="${TMPDIR:-/tmp}/semgrep-settings.yml" '
                 'SEMGREP_LOG_FILE="${TMPDIR:-/tmp}/semgrep.log" '
                 'SEMGREP_VERSION_CACHE_PATH="${TMPDIR:-/tmp}/semgrep-version" ')


def semgrep_cmd(change, targets: list[str], blocking: bool) -> str:
    """The configured ruleset plus factory's pinned rules (factory/rules/semgrep/). Targets are passed as `./path`
    after `--`, so a file name can't be read as an option; nosemgrep comments don't suppress findings. `blocking`
    keeps only ERROR and WARNING findings; the exit code is not the verdict (sast() reads the report)."""
    config = change.config["gate"]["semgrep_config"]
    flags = "--severity ERROR --severity WARNING " if blocking else ""
    metrics = "on" if config == "auto" else "off"  # semgrep refuses --config auto with metrics off
    paths = " ".join(shlex.quote(t if t == "." else "./" + t) for t in targets)
    return (f"{SEMGREP_FILES}semgrep scan --config {shlex.quote(config)} --config {shlex.quote(str(PINNED_RULES))} "
            f"--metrics={metrics} --disable-version-check --disable-nosem --json --quiet {flags}-- {paths}")


def semgrep_errors(text: str) -> list[str] | None:
    """The `errors` semgrep reported, or None when its output isn't the JSON report."""
    try:
        j = json.loads(text)
    except json.JSONDecodeError:
        return None
    if not isinstance(j, dict) or not isinstance(j.get("errors"), list):
        return None
    return [str(e.get("message") or e.get("type") or e)[:200] if isinstance(e, dict) else str(e)[:200]
            for e in j["errors"]]


def sast(change) -> dict:
    files = [f for f in change.changed_files() if (change.worktree / f).is_file() and not (change.worktree / f).is_symlink()]
    if not files:
        return change.record("gate", "skipped", check="sast", reason="no changed files to scan", applies=False)
    missing = tool_missing(change, "sast", "semgrep")
    if missing:
        return missing
    scan = change.run_check("gate", "sast-scan", semgrep_cmd(change, files, True), trusted=True)
    text = (change.dir / scan["evidence"][0]).read_text(errors="replace")
    errors = semgrep_errors(text)
    base = dict(check="sast", cmd=scan["cmd"], after_event=scan["id"], evidence=scan["evidence"])
    if scan["status"] != "pass" or errors is None or errors:
        why = (f"semgrep exited {scan.get('exit')}" if scan["status"] != "pass" else "semgrep's report isn't readable JSON"
               if errors is None else f"semgrep reported errors: {'; '.join(errors[:3])}")
        return change.record("gate", "fail", **base, reason=f"{why}, so the scan may not have covered the change")
    # Only findings on lines this change adds block. Findings already in a touched file were there at the baseline:
    # they are recorded, and the semgrep ratchet keeps their count from rising.
    added = added_lines(change, files)
    hits, old = [], 0
    for r in json.loads(text).get("results") or []:
        path = str(r.get("path", "")).removeprefix("./")
        lines = set(range(int(r["start"]["line"]), int(r["end"]["line"]) + 1))
        if lines & added.get(path, set()):
            hits.append(f"{r.get('check_id', '?').rsplit('.', 1)[-1]} at {path}:{r['start']['line']}")
        else:
            old += 1
    if hits:
        return change.record("gate", "fail", **base, findings=hits, preexisting=old,
                             reason=f"semgrep flags lines this change adds: {'; '.join(hits[:5])}")
    return change.record("gate", "pass", **base, preexisting=old,
                         note=f"no finding on an added line; {old} finding(s) already in the touched files" if old
                         else "no findings")


def added_lines(change, files: list[str]) -> dict[str, set[int]]:
    """Line numbers, in the change's head, that the change adds to each file (a zero-context diff on the baseline)."""
    out, current = {}, None
    diff = change.git("diff", "-U0", "--no-color", "--no-ext-diff", f"{change.baseline}..HEAD", "--", *files)
    for line in diff.splitlines():
        if line.startswith("+++ "):
            current = None if line[4:] == "/dev/null" else line[4:].removeprefix("b/")
        elif line.startswith("@@") and current:
            m = re.search(r"\+(\d+)(?:,(\d+))?", line)
            start, count = int(m.group(1)), int(m.group(2) if m.group(2) is not None else 1)
            out.setdefault(current, set()).update(range(start, start + count))
    return out


def rollback(change) -> dict:
    """A rollback.md this change wrote is rehearsed, whether or not a class requires one: a rollback the pack offers is
    demonstrated, never only described. One left at the root by an earlier change doesn't count."""
    needs = sorted(c for c, info in risk_classes(change).items() if "gate:rollback" in info.get("required_gates", []))
    doc = change.worktree / "rollback.md"
    written = "rollback.md" in set(change.changed_files()) | set(change.dirty_files()) and doc.exists()
    if not needs and not written:
        return change.record("gate", "skipped", check="rollback", applies=False,
                             reason="no class in risk.json requires a rollback (no migration or irreversible path or pattern)")
    why = f"risk class {', '.join(needs)} requires" if needs else "rollback.md is in the change, so it needs"
    if not written:
        return change.record("gate", "fail", check="rollback",
                             reason=f"{why} rollback.md at the worktree root written for this change; "
                                    + ("the one there is unchanged since the baseline" if doc.exists() else "there is none"))
    m = re.search(r"^\s*[-*]?\s*rehearse:\s*`?([^`\n]+?)`?\s*$", doc.read_text(), re.M | re.I)
    if not m:
        return change.record("gate", "fail", check="rollback", rollback_sha256=sha256_file(doc),
                             reason=f"{why} a rehearsed rollback; rollback.md names no `rehearse:` command")
    return change.run_check("gate", "rollback", m.group(1).strip())


# Runners that load each test file in its own process or module registry, so a new test file can't patch what a
# locked test sees. Anything else (pytest, mocha, a shell script) fails closed. PROPOSED: the axis sources set the
# principle (an agent asks before it alters a test, Crickett via Ojstersek; a fixture adjusted so a result passes is
# normalised deviance, Vaughan) but say nothing about runners.
ISOLATING = re.compile(r"\bnode\b[^|;&]*--test\b|\bjest\b|\bvitest\b")
NOT_ISOLATING = re.compile(r"--test-isolation[= ]none|--no-isolate|--isolate[= ]false")


def invisible(change) -> dict:
    """Invisible, bidirectional or control characters on lines the change adds: they can hide code or instructions
    from a human reader while a model or compiler still reads them (OWASP LLM Top 10 2026, LLM01)."""
    from factory.text import invisible_chars
    hits = {}
    current = None
    for line in change.diff().splitlines():
        if line.startswith("+++ "):
            current = line[4:].removeprefix("b/")
        elif current and line.startswith("+") and not line.startswith("+++"):
            found = invisible_chars(line[1:].replace("\t", ""))
            if found:
                hits.setdefault(current, set()).update(found)
    if not hits:
        return change.record("gate", "pass", check="invisible", note="no invisible or control characters added")
    detail = "; ".join(f"{f}: {', '.join(sorted(c))}" for f, c in sorted(hits.items()))
    return change.record("gate", "fail", check="invisible", files=sorted(hits), acceptable=True,
                         reason=f"the change adds invisible, bidirectional or control characters ({detail})")


def runner_command(change, cmd: str) -> str:
    """`npm test`, `yarn test`, `pnpm run x` resolved to the script it runs, read from the BASELINE's package.json, so
    the build can't change which runner gets credited."""
    m = re.fullmatch(r"\s*(?:npm|yarn|pnpm)(?:\s+run)?\s+([\w:-]+)\s*", cmd)
    if not m:
        return cmd
    try:
        scripts = json.loads(change.git("show", f"{change.baseline}:package.json")).get("scripts") or {}
    except Exception:  # no package.json at the baseline: nothing to resolve
        return cmd
    return scripts.get(m.group(1)) or cmd


def added_tests(change) -> dict:
    """Test files the build added that the lock doesn't cover. Under a runner that shares one process across test
    files, such a file can monkeypatch the code or fixtures a locked test relies on, so a human decides."""
    added = check_lock(change)["added"]
    if not added:
        return change.record("gate", "pass", check="added-tests", note="the build added no test files")
    cmd = runner_command(change, change.config["commands"].get("test") or "")
    if ISOLATING.search(cmd) and not NOT_ISOLATING.search(cmd):
        return change.record("gate", "pass", check="added-tests", files=added,
                             note=f"the build added unlocked test files; `{cmd}` runs each test file in isolation")
    return change.record("gate", "fail", check="added-tests", files=added, acceptable=True,
                         reason=f"the build added test files the lock doesn't cover ({', '.join(added[:5])}); under "
                                f"`{cmd}` they may share a process with the locked tests and change what those tests see")


def surface(change) -> dict:
    """Fail when the change edits what steers the tests or the scanners, unless those files are locked."""
    from factory.hooks.guard import read_lock
    globs = SURFACE_GLOBS + list(change.config.get("surface_globs") or [])
    locked = set(read_lock(change.dir / "tests.lock")) if (change.dir / "tests.lock").exists() else set()
    hits = []
    for f in change.changed_files():
        if f in locked:
            continue
        if any(globmatch(f, g) for g in globs):
            hits.append(f)
        elif Path(f).name == "package.json":
            keys = changed_keys(change, f, lambda t: json.loads(t), PACKAGE_KEYS)
            hits += [f"{f} ({', '.join(keys)})"] if keys else []
        elif Path(f).name == "pyproject.toml":
            keys = changed_keys(change, f, lambda t: tomllib.loads(t).get("tool", {}), PYPROJECT_TABLES)
            hits += [f"{f} ([tool.{', tool.'.join(keys)}])"] if keys else []
    if not hits:
        return change.record("gate", "pass", check="surface",
                             note="the change edits no test-runner, scanner or agent-instruction file")
    return change.record("gate", "fail", check="surface", files=hits, acceptable=True,
                         reason=f"the change edits files that steer the tests, the scanners or the agents: {', '.join(hits)}")


def changed_keys(change, rel: str, parse, keys: tuple) -> list[str]:
    """Which of `keys` differ between the baseline's and the head's version of a config file (all, if unreadable)."""
    def load(rev: str):
        r = change.git("show", f"{rev}:{rel}", check=False)
        try:
            return parse(r) if r else {}
        except Exception:
            return None
    before, after = load(change.baseline), load("HEAD")
    if before is None or after is None or not isinstance(before, dict) or not isinstance(after, dict):
        return list(keys)
    return [k for k in keys if before.get(k) != after.get(k)]


def required(change, events: list[dict]) -> dict:
    """Every gate a risk class requires ran in this run and passed."""
    status = {e["check"]: e for e in events}
    missing = []
    for cls, info in sorted(risk_classes(change).items()):
        for g in info.get("required_gates", []):
            check = g.removeprefix("gate:")
            e = status.get(check)
            if not e or e["status"] != "pass":
                missing.append(f"{cls} requires {g}, which {'did not run' if not e else e['status']}"
                               + (f" ({e.get('reason')})" if e and e.get("reason") else ""))
    return change.record("gate", "fail" if missing else "pass", check="required", reason="; ".join(missing) or None)


def count_findings(text: str) -> tuple[int | None, list[str], str | None]:
    """(count, files the output names, problem) from a tool's JSON output: semgrep ({results: [...]}), ESLint
    ([{filePath, messages: [...]}]), a list, or {count: N}. A count is a non-negative integer or it's a problem."""
    try:
        j = json.loads(text)
    except json.JSONDecodeError as e:
        return None, [], f"the output isn't JSON ({e.msg})"
    files: list[str] = []
    n = None
    if isinstance(j, dict):
        if isinstance(j.get("results"), list):
            n = len(j["results"])
            scanned = (j.get("paths") or {}).get("scanned")
            files = [p for p in scanned if isinstance(p, str)] if isinstance(scanned, list) else []
        elif "count" in j:
            n = j["count"]
    elif isinstance(j, list):
        if j and all(isinstance(x, dict) and "messages" in x for x in j):
            if not all(isinstance(x["messages"], list) for x in j):
                return None, [], "an ESLint entry's messages isn't a list"
            n = sum(len(x["messages"]) for x in j)
            files = [x["filePath"] for x in j if isinstance(x.get("filePath"), str)]
        else:
            n = len(j)
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        return None, [], f"no non-negative finding count in the output (got {n!r})"
    return n, files, None


def tracked_matching(cwd: Path, globs: list[str]) -> list[str]:
    """Files git tracks in cwd that match the globs (for a density ratchet whose output names no files)."""
    if not globs:
        return []
    import subprocess
    r = subprocess.run(["git", "ls-files", "-z"], cwd=cwd, capture_output=True)
    names = [n.decode("utf-8", "surrogateescape") for n in r.stdout.split(b"\0") if n]
    return [n for n in names if any(globmatch(n, g) for g in globs)]


def nonblank_lines(cwd: Path, files: list[str]) -> tuple[int | None, str | None]:
    total = 0
    for f in files:
        p = Path(f) if Path(f).is_absolute() else Path(cwd) / f
        if not p.is_file():
            return None, f"the output names {f}, which isn't a file"
        total += sum(1 for ln in p.read_text(errors="replace").splitlines() if ln.strip())
    return total, None


def ratchet_specs(change) -> list[dict]:
    """The configured ratchet counts, each {name, command, mode, tolerance, trusted, ok_exits}.

    `semgrep_findings: true` is absolute (any new security finding is a finding). `lint_warnings: CMD` is density.
    Either may be a mapping {command, mode: absolute|density, tolerance} to choose."""
    cfg = change.config.get("ratchet") or {}
    default_tol = float(cfg.get("density_tolerance", 0.02))
    specs = []
    for name, default_mode in (("semgrep_findings", "absolute"), ("lint_warnings", "density")):
        v = cfg.get(name)
        if not v:
            continue
        spec = v if isinstance(v, dict) else {} if v is True else {"command": v}
        trusted = name == "semgrep_findings" and not spec.get("command")
        specs.append({"name": name, "command": spec.get("command") or semgrep_cmd(change, ["."], False),
                      "mode": spec.get("mode", default_mode), "tolerance": float(spec.get("tolerance", default_tol)),
                      "files": list(spec.get("files") or []),
                      "trusted": trusted, "ok_exits": [0] if trusted else spec.get("ok_exits", [0, 1])})
        if specs[-1]["mode"] not in ("absolute", "density"):
            raise SystemExit(f"ratchet.{name}.mode must be absolute or density, not {specs[-1]['mode']!r}")
    return specs


def measure(change, spec: dict, cwd: Path, which: str) -> dict:
    name = spec["name"]
    log = change.path(f"gate/ratchet-{name}-{which}.json")
    res = legs.run_command(spec["command"], cwd, log, change.timeout("gate"), stderr_log=log.with_suffix(".stderr.txt"),
                           policy=None if spec["trusted"] else change.policy(f"ratchet:{name}", cwd),
                           os_sandbox=change.os_sandbox(), tmp_root=change.worktree.parent / ".factory-tmp")
    text = log.read_text(errors="replace")
    count, files, problem = count_findings(text)
    if res["exit"] is None or res["exit"] not in spec["ok_exits"]:
        problem = (f"{which} run exited {res['exit']}" if res["exit"] is not None else
                   f"{which} run didn't complete: {res.get('error')}")
    errors = semgrep_errors(text) if spec["trusted"] else []
    out = {"count": count, "exit": res["exit"], "output_sha256": res["output_sha256"], "log": change.rel(log),
           "errors": len(errors) if errors is not None else None}
    if spec["mode"] == "density" and not problem:
        files = files or tracked_matching(cwd, spec["files"])
        if not files:
            problem = f"{which} output names no scanned files, so there are no lines to measure density against"
        else:
            out["lines"], problem = nonblank_lines(cwd, files)
            if not problem and not out["lines"]:
                problem = f"{which}: the scanned files have no non-blank lines"
    out["problem"] = problem
    return out


def judge(spec: dict, b: dict, a: dict) -> tuple[str, str | None, bool, dict]:
    """(status, reason, whether a human may accept it, numbers) for one ratchet."""
    if b["problem"] or a["problem"]:
        return "fail", f"measurement error: {b['problem'] or a['problem']}", False, {}
    if spec["trusted"] and (a["errors"] or 0) > (b["errors"] or 0):
        return "fail", (f"measurement error: semgrep reported {a['errors']} errors after the change "
                        f"(baseline {b['errors']}), so it scanned less"), False, {}
    if spec["mode"] == "absolute":
        if a["count"] > b["count"]:
            return "fail", f"rose from {b['count']} at baseline to {a['count']}", True, {}
        return "pass", None, False, {}
    bd, ad = 1000 * b["count"] / b["lines"], 1000 * a["count"] / a["lines"]
    nums = {"density_before": round(bd, 3), "density_after": round(ad, 3), "tolerance": spec["tolerance"]}
    if ad > bd * (1 + spec["tolerance"]) + 1e-9:
        return "fail", (f"density rose from {bd:.2f} to {ad:.2f} per 1,000 lines ({b['count']}/{b['lines']} → "
                        f"{a['count']}/{a['lines']}), beyond the {spec['tolerance']:.0%} tolerance"), True, nums
    return "pass", None, False, nums


def ratchet(change) -> list[dict]:
    specs = ratchet_specs(change)
    if not specs:
        return []
    base = change.tmpdir("ratchet-baseline-")
    events = []
    try:
        change.git("worktree", "add", "--detach", str(base), change.baseline)
        install = change.config["commands"].get("install")
        base_install = None
        if install and any(not s["trusted"] for s in specs):
            base_install = legs.run_command(install, base, change.path("gate/ratchet-baseline-install.log"),
                                            change.timeout("gate"), policy=change.policy("install", base),
                                            os_sandbox=change.os_sandbox(),
                                            tmp_root=change.worktree.parent / ".factory-tmp")
        for spec in specs:
            b = measure(change, spec, base, "baseline")
            a = measure(change, spec, change.worktree, "after")
            if base_install and base_install["exit"] != 0 and not spec["trusted"]:
                b["problem"] = f"the baseline install failed ({base_install.get('error') or base_install['exit']})"
            status, reason, acceptable, nums = judge(spec, b, a)
            events.append(change.record("gate", status, check=f"ratchet:{spec['name']}", cmd=spec["command"],
                                        mode=spec["mode"], before=b["count"], after=a["count"],
                                        lines_before=b.get("lines"), lines_after=a.get("lines"), **nums,
                                        runs={"baseline": b, "after": a}, evidence=[b["log"], a["log"]],
                                        artefacts=change.hashes(b["log"], a["log"]), reason=reason,
                                        acceptable=acceptable or None))
    finally:
        change.git("worktree", "remove", "--force", str(base), check=False)
        shutil.rmtree(base, ignore_errors=True)
    return events


def theory_doc(change) -> dict | None:
    doc = change.config.get("theory_doc")
    if not doc:
        return None
    path = change.worktree / doc
    return change.record("gate", "info", check="theory-doc", path=doc, exists=path.exists(),
                         changed=doc in change.changed_files(),
                         doc_sha256=sha256_file(path) if path.exists() else None)
