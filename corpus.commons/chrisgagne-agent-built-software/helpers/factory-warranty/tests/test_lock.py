from factory.stages import gate
from factory.stages.tests import check_lock, write_lock


def test_lock_hashes_every_test_file(change):
    files = write_lock(change)
    assert files == ["test/greet.test.sh", "test/run.sh"]
    lines = (change.dir / "tests.lock").read_text().splitlines()
    assert lines[0].startswith("# tests.lock for change c1")
    assert all(len(ln.split("  ")[0]) == 64 for ln in lines[1:])
    assert check_lock(change) == {"locked": 2, "changed": [], "missing": [], "added": []}


def test_tamper_detection(change):
    write_lock(change)
    wt = change.worktree
    (wt / "test" / "greet.test.sh").write_text("exit 0\n")
    (wt / "test" / "run.sh").unlink()
    (wt / "test" / "extra.test.sh").write_text("true\n")
    r = check_lock(change)
    assert r["changed"] == ["test/greet.test.sh"]
    assert r["missing"] == ["test/run.sh"]
    assert r["added"] == ["test/extra.test.sh"]
    change.start("gate")
    ev = gate.locked_tests(change)
    assert ev["status"] == "fail" and "greet.test.sh" in ev["reason"]


def test_gate_catches_an_edited_tests_lock(change):
    write_lock(change)
    lock = change.dir / "tests.lock"
    lock.write_text(lock.read_text().replace("test/run.sh", "test/other.sh"))
    change.start("gate")
    ev = gate.locked_tests(change)
    assert ev["status"] == "fail" and "tests.lock changed" in ev["reason"]


def test_lock_catches_a_symlink_with_the_same_bytes_and_a_mode_change(change, tmp_path):
    write_lock(change)
    wt = change.worktree
    same = tmp_path / "same.sh"
    same.write_bytes((wt / "test" / "greet.test.sh").read_bytes())
    (wt / "test" / "greet.test.sh").unlink()
    (wt / "test" / "greet.test.sh").symlink_to(same)
    (wt / "test" / "run.sh").chmod(0o755)
    assert check_lock(change)["changed"] == ["test/greet.test.sh", "test/run.sh"]


def test_lock_records_mode_and_type(change):
    write_lock(change)
    lines = (change.dir / "tests.lock").read_text().splitlines()[1:]
    assert all(ln.split("  ")[1] == "100644" for ln in lines)


def test_unusual_file_names_are_locked_and_scanned(change):
    from factory.stages.triage import changed_lines
    wt = change.worktree
    (wt / "test" / "café.test.sh").write_text("true\n")
    (wt / "test" / "tab\there.test.sh").write_text("true\n")
    (wt / "src" / "naïve.js").write_text("DROP TABLE users;\n")
    change.commit_all("odd names")
    files = write_lock(change)
    assert "test/café.test.sh" in files and "test/tab\there.test.sh" in files
    assert "src/naïve.js" in change.changed_files()
    assert "src/naïve.js" in changed_lines(change.diff(), ["test/**"])
    (wt / "test" / "café.test.sh").write_text("false\n")
    assert check_lock(change)["changed"] == ["test/café.test.sh"]
    assert "test/café.test.sh" in change.dirty_files()
