"""Gate checks that call the real scanners on tiny inputs (local only, no network)."""
import json
import os
import shutil
import subprocess

import pytest

from factory.stages import gate

needs = pytest.mark.skipif(not (shutil.which("osv-scanner") and shutil.which("semgrep")), reason="scanner missing")


def test_an_exit_named_as_skip_is_recorded_as_skipped_not_passed(change):
    change.start("gate")
    ev = change.run_check("gate", "deps", "exit 128", skip_exits={128: "no dependencies scanned"})
    assert (ev["status"], ev["exit"], ev["reason"]) == ("skipped", 128, "no dependencies scanned")
    assert change.run_check("gate", "deps", "exit 3", skip_exits={128: "x"})["status"] == "fail"


@needs
def test_osv_on_a_lockfile_with_no_packages_is_skipped(change):
    (change.worktree / "package-lock.json").write_text(json.dumps(
        {"name": "x", "version": "1.0.0", "lockfileVersion": 3, "packages": {"": {"name": "x"}}}))
    change.commit_all("empty lockfile")
    change.start("gate")
    ev = gate.deps(change)
    assert ev["status"] == "skipped" and ev["exit"] == 128 and "no dependencies scanned" in ev["reason"]


@needs
def test_pinned_rule_flags_interpolated_sql_but_not_static_sql(tmp_path):
    (tmp_path / "bad.js").write_text("export const f = (db, q) => db.prepare(`SELECT * FROM notes WHERE title LIKE '%${q}%'`).all();\n")
    (tmp_path / "ok.js").write_text("export const g = (db) => db.exec(`CREATE TABLE IF NOT EXISTS t (id INTEGER)`);\n"
                                    "export const h = (db, q) => db.prepare('SELECT * FROM t WHERE id = ?').get(q);\n")
    out = subprocess.run(["semgrep", "scan", "--config", str(gate.PINNED_RULES), "--metrics=off", "--json", "--quiet",
                          "--disable-version-check", "bad.js", "ok.js"], cwd=tmp_path, capture_output=True, text=True,
                         env={**os.environ, "SEMGREP_SETTINGS_FILE": str(tmp_path / "s.yml"),
                              "SEMGREP_LOG_FILE": str(tmp_path / "log"), "SEMGREP_VERSION_CACHE_PATH": str(tmp_path / "v")})
    hits = [(r["path"], r["start"]["line"]) for r in json.loads(out.stdout)["results"]]
    assert hits == [("bad.js", 1)]
