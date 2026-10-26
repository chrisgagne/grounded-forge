"""Stage 3, tests: tests from acceptance.md before any implementation, proven red, then locked.

The driver checks the baseline suite is green, runs the tests leg with the
guard limiting it to test files, requires every changed file to be a test file,
requires existing tests to be kept (lines may be added, not changed or
removed), requires every check line's file to exist and to contain the test it
names, requires the suite to be red with the new tests (a completed run, not a
timeout or a runner that couldn't start) and the red output to mention each
criterion's test or file, then writes tests.lock: the sha256, type and mode of
every file matching test_globs.
"""
from __future__ import annotations

import os
import re
import shutil
import stat
from pathlib import Path

from factory import check, legs
from factory.hooks.guard import globmatch, read_lock, read_lock_entries
from factory.ledger import sha256_bytes, sha256_file
from factory.stages import adapter_leg, brief, builder_command, check_commands
from factory.stages.spec import check_file, check_name, parse_acceptance


def identity(path: Path) -> tuple[str, str]:
    """(sha256, mode) of a path as git would see it: a symlink is mode 120000 and hashes its target text (never
    the file it points to); a regular file is 100755 when executable, else 100644."""
    st = os.lstat(path)
    if stat.S_ISLNK(st.st_mode):
        return sha256_bytes(os.readlink(path).encode("utf-8", "surrogateescape")), "120000"
    if stat.S_ISREG(st.st_mode):
        return sha256_file(path), "100755" if st.st_mode & 0o111 else "100644"
    return "-", "other"


def write_lock(change) -> list[str]:
    files = change.test_files()
    bad = [f for f in files if "\n" in f or "\r" in f]
    if bad:
        raise ValueError(f"test file names with line breaks can't be locked: {bad!r}")
    lines = [f"# tests.lock for change {change.id} at commit {change.head()}: sha256  mode  path"]
    lines += ["{}  {}  {}".format(*identity(change.worktree / f), f) for f in files]
    change.path("tests.lock").write_text("\n".join(lines) + "\n")
    change.record("tests", "info", check="lock", files=len(files), lock_commit=change.head(),
                  artefacts=change.hashes("tests.lock"))
    return files


def check_lock(change) -> dict:
    """Compare the worktree's test files with tests.lock by content, type and mode: changed, missing, added."""
    locked = read_lock_entries(change.dir / "tests.lock")
    current = {f: identity(change.worktree / f) for f in change.test_files()}
    return {"locked": len(locked),
            "changed": sorted(f for f in locked if f in current and current[f] != locked[f]),
            "missing": sorted(f for f in locked if f not in current),
            "added": sorted(f for f in current if f not in locked)}


def run(change, recheck: bool = False) -> bool:
    """With `recheck`, no leg runs: the same checks run on the tests committed since the baseline (after a check
    line or a test name was fixed)."""
    change.start("tests")
    cfg, cmds = change.config, change.config["commands"]
    acceptance = change.dir / "acceptance.md"
    if not acceptance.exists():
        return change.finish("tests", ["no acceptance.md"], ["Run `factory spec` first."])
    criteria, problems = parse_acceptance(acceptance.read_text())
    if problems:
        return change.finish("tests", problems, ["Fix acceptance.md and run `factory spec --recheck`."])
    dirty = change.dirty_files()
    if dirty:
        return change.finish("tests", [f"the worktree has uncommitted changes before the tests leg: {', '.join(dirty[:10])}"],
                             [f"Discard them (`git -C {change.worktree} checkout -- . && git -C {change.worktree} clean -fd`), "
                              "then re-run `factory tests`."])
    # After a send-back (a build exists and its tests are locked), only criteria the lock doesn't cover get tests,
    # and the suite must be green at the current build before they're added.
    lock = change.dir / "tests.lock"
    again = not recheck and lock.exists() and change.outcome("build") is not None
    new = [cr for cr in criteria if not covered(change, cr["check"], set(read_lock(lock)))] if again else criteria
    if again and not new:
        change.record("tests", "info", check="no-new-criteria", note="the send-back added no criteria; the lock stands")
        return change.finish("tests", [])
    if cmds.get("install") and change.run_check("tests", "install", cmds["install"])["status"] == "fail":
        return change.finish("tests", ["install failed on the baseline"], ["Fix the install command, then re-run."])
    base = change.run_check("tests", "suite-before", cmds["test"]) if again else baseline_suite(change, cmds)
    if base["status"] == "fail":
        return change.finish("tests", [f"the suite is already red (event {base['id']}) "
                                       f"{'at the current build' if again else 'at the baseline'}, so a red suite "
                                       "after adding tests would prove nothing"], ["Make it green first."])
    if recheck:
        before = change.baseline
        change.record("tests", "info", check="recheck", note="no leg: checking the tests committed since the baseline")
    else:
        before = change.head()
        checks = None if builder_command(change, "tests") else check_commands(change, "tests", before, ["test"])
        run_rule = (f"Run the suite with the factory check, exactly as written: `{checks[0]}`. It scans what you've "
                    "written (invisible characters, secrets, and semgrep on the lines you added) and runs "
                    f"`{cmds['test']}` only if the scans pass. Any other shell command is blocked: look at files with "
                    "Read, Grep and Glob, and write them with Edit and Write." if checks else
                    f"Run the suite with `{cmds['test']}`.")
        scope = (f"Tests for {', '.join(cr['id'] for cr in criteria if cr not in new)} are already written and locked: "
                 f"leave them as they are. Write tests only for {', '.join(cr['id'] for cr in new)}, which the current "
                 "code doesn't do yet, in the new files their check lines name: the locked files can't be edited, not "
                 "even to add a test." if again else "Write a test for every criterion.")
        prompt = brief("tests.md", acceptance=acceptance.read_text(), test_globs=", ".join(cfg["test_globs"]),
                       run_rule=run_rule, scope=scope)
        res = adapter_leg(change, "tests", prompt, allow_only=cfg["test_globs"], bash_only=checks)
        if res.get("result"):
            change.path("tests-summary.md").write_text(res["result"])
        if not res["ok"]:
            return change.finish("tests", [f"the tests leg failed: {res.get('error')}"], ["Re-run `factory tests`."])
    touched = sorted(set(change.dirty_files()) | set(change.changed_files(before)))
    outside = [f for f in touched if not any(globmatch(f, g) for g in cfg["test_globs"])]
    if not touched or outside:
        why = (["the tests leg wrote no test files"] if not touched else
               [f"the tests leg changed files that are not tests: {', '.join(outside)}"])
        change.record("tests", "fail", check="only-tests", touched=touched, reason=why[0])
        return change.finish("tests", why, ["Re-run `factory tests`; the leg may write only files matching test_globs."])
    weakened = weakened_tests(change, before)
    if weakened:
        change.record("tests", "fail", check="existing-tests", weakened=weakened,
                      reason="the tests leg changed or removed lines of tests that existed before it")
        return change.finish("tests", [f"the tests leg changed or removed existing tests: {', '.join(weakened)}"],
                             [f"Discard its changes (`git -C {change.worktree} checkout -- . && git -C {change.worktree} "
                              "clean -fd`) and re-run `factory tests`; it may add tests, not edit existing ones."])
    change.commit_all(f"factory: acceptance tests for {change.id}", "tests")
    files = change.test_files()
    unproven = [f"{cr['id']} ({why})" for cr in criteria for why in [unproven_reason(change, cr["check"], files)] if why]
    if unproven:
        change.record("tests", "fail", check="check-lines", unproven=unproven,
                      reason="a check line names a test file or test that doesn't exist")
        return change.finish("tests", [f"no test for {'; '.join(unproven)}"],
                             ["Fix the check lines in acceptance.md (`factory spec --recheck`), then `factory tests --recheck`; or "
                              f"reset the worktree to the baseline (`git -C {change.worktree} reset --hard "
                              f"{change.baseline[:12]}`) and re-run `factory tests`."])
    # The scans the gate runs first, on what the tests leg wrote, before the driver runs it (OWASP ASI05 #7).
    from factory.stages.gate import PINNED_RULES  # here, not at the top: the gate imports this module
    rules = cfg["gate"]["semgrep_config"]
    _, problems = check.scan(change.worktree, before, [c for c in (rules,) if Path(c).exists()] + [str(PINNED_RULES)])
    if problems:
        change.record("tests", "fail", check="scan", reason="; ".join(problems)[:600])
        return change.finish("tests", [f"what the tests leg wrote fails a scan, so it wasn't run: {'; '.join(problems[:3])}"],
                             ["Re-run `factory tests`; the tests leg must not add secrets, invisible characters or "
                              "flagged code."])
    change.record("tests", "pass", check="scan", note="invisible characters, secrets and semgrep on the tests leg's work")
    red = change.run_check("tests", "new-tests", cmds["test"])
    if red["status"] == "pass":
        return change.finish("tests", [f"the suite passes with the new tests before {'the rebuild' if again else 'any implementation'} "
                                       f"(event {red['id']}), so they don't test the change"], ["Re-run `factory tests`."])
    if red.get("exit") is None or red["exit"] >= 126:
        return change.finish("tests", [f"the test command didn't complete (event {red['id']}: "
                                       f"{red.get('reason') or 'exit ' + str(red.get('exit'))}), so its failure isn't "
                                       "evidence that the new tests are red"], ["Fix the test command or the timeout, "
                                                                               "then re-run `factory tests`."])
    output = (change.dir / red["evidence"][0]).read_text(errors="replace")
    silent = [cr["id"] for cr in new if not mentioned(cr["check"], output)]  # the locked ones were shown red before
    if silent:
        return change.finish("tests", [f"the red run's output (event {red['id']}) never mentions the test or test file "
                                       f"for {', '.join(silent)}, so there is no evidence those tests ran"],
                             ["Make the test command report test names or files, or fix the check lines."])
    change.record("tests", "pass", check="red", note=f"the suite fails with the new tests (event {red['id']}), "
                                                     "as it must before the build")
    write_lock(change)
    # The criteria the lock now covers: the base a later send-back may only add to.
    change.path("tests/acceptance-locked.md").write_text(acceptance.read_text())
    change.record("tests", "info", check="acceptance-locked", artefacts=change.hashes("tests/acceptance-locked.md"))
    return change.finish("tests", [])


def baseline_suite(change, cmds) -> dict:
    """The suite at the baseline commit. With tests already committed on top of it (a re-run or a recheck), it runs in
    a throwaway worktree at the baseline, so those red tests don't count as a red baseline."""
    if change.head() == change.baseline:
        return change.run_check("tests", "baseline-tests", cmds["test"])
    base = change.tmpdir("tests-baseline-")
    try:
        change.git("worktree", "add", "--detach", str(base), change.baseline)
        if cmds.get("install"):
            inst = legs.run_command(cmds["install"], base, change.path("tests/baseline-install.log"),
                                    change.timeout("gate"), policy=change.policy("install", base),
                                    os_sandbox=change.os_sandbox(), tmp_root=change.worktree.parent / ".factory-tmp")
            if inst["exit"] != 0:
                return change.record("tests", "fail", check="baseline-tests", cmd=cmds["install"], exit=inst["exit"],
                                     evidence=["tests/baseline-install.log"],
                                     artefacts=change.hashes("tests/baseline-install.log"),
                                     reason=f"the install failed at the baseline ({inst.get('error') or inst['exit']})")
        return change.run_check("tests", "baseline-tests", cmds["test"], cwd=base)
    finally:
        change.git("worktree", "remove", "--force", str(base), check=False)
        shutil.rmtree(base, ignore_errors=True)


QUOTE_ESCAPE = re.compile(r"\\([\"'`])")


def norm(text: str) -> str:
    return " ".join(text.lower().split())


def source_text(path: Path) -> str:
    """A test file's text with escaped quotes read as the quote: `'the caller\\'s note'` names "the caller's note"."""
    return QUOTE_ESCAPE.sub(r"\1", path.read_text(errors="replace"))


def unproven_reason(change, check: str, files: list[str]) -> str | None:
    """Why a check line isn't backed by a test: its file is missing, or the file doesn't contain its test name."""
    f, name = check_file(check), check_name(check)
    if f not in files:
        return f"{f} doesn't exist or isn't covered by test_globs"
    if name and norm(name) not in norm(source_text(change.worktree / f)):
        return f"{f} has no test named {name!r}"
    return None


def covered(change, check: str, locked: set[str]) -> bool:
    """Whether a criterion's check line names a locked test file (and a test that file contains)."""
    f, name = check_file(check), check_name(check)
    return f in locked and (not name or norm(name) in norm(source_text(change.worktree / f)))


def mentioned(check: str, output: str) -> bool:
    out = norm(output)
    return bool(check_name(check)) and norm(check_name(check)) in out or norm(check_file(check)) in out


def weakened_tests(change, before: str) -> list[str]:
    """Test files that existed at `before` whose lines the tests leg changed or removed (adding lines is fine)."""
    existing = {f for f in change.git_z("ls-tree", "-r", "--name-only", before)
                if any(globmatch(f, g) for g in change.config["test_globs"])}
    out = []
    for f in sorted(existing):
        if not os.path.lexists(change.worktree / f):
            out.append(f"{f} (deleted)")
            continue
        stats = change.git_z("diff", "--numstat", "--no-renames", before, "--", f)
        removed = [s.split("\t")[1] for s in stats if s.count("\t") >= 2]
        if any(r == "-" or int(r) > 0 for r in removed):
            out.append(f)
    return out
