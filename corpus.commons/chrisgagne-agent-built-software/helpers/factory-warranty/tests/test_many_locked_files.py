"""A project with thousands of locked test files: locked paths are compressed to whole folders where every file in the
folder is locked, and the rules are split under sandbox-exec's size limit; a read-only leg's settings don't list the
locked files at all (Claude Code refuses settings over 2 MiB)."""
import os
import subprocess

import pytest

from factory import isolation
from factory.stages import settings_file


def project(tmp_path, n=13000):
    root = tmp_path.resolve()
    (root / "src").mkdir()
    (root / "src" / "a.js").write_text("x")
    for i in range(n):
        d = root / "test" / f"g{i % 40}"
        d.mkdir(parents=True, exist_ok=True)
        (d / f"t{i}.test.js").write_text("x")
    (root / "test" / "helper.js").write_text("x")  # not locked, so test/ itself isn't a whole locked folder
    return root, [str(p) for p in (root / "test").rglob("*.test.js")]


def test_compress_names_whole_locked_folders_only(tmp_path):
    root, locked = project(tmp_path)
    c = isolation.compress(locked)
    assert len(c) == 40 and all(os.path.dirname(p) == str(root / "test") for p in c)
    assert str(root / "test") not in c  # helper.js isn't locked


@pytest.mark.skipif(not isolation.available()[0], reason="sandbox-exec unavailable")
def test_thirteen_thousand_locked_files_still_sandbox(tmp_path):
    root, locked = project(tmp_path)
    with isolation.Sandboxed(isolation.Policy(writable=[str(root)], deny_write=locked)) as box:
        r = subprocess.run(box.argv(f"echo hi > {root}/src/new.txt; echo no > {root}/test/g1/t1.test.js"),
                           capture_output=True, text=True, env={**box.env(), "PATH": "/usr/bin:/bin"})
    assert (root / "src" / "new.txt").read_text() == "hi\n"  # the rest of the tree stays writable
    assert (root / "test" / "g1" / "t1.test.js").read_text() == "x"  # a locked test stays locked
    assert r.returncode != 0


def test_a_read_only_legs_settings_leave_out_the_locked_files(change, monkeypatch):
    many = [f"test/t_{i:05d}.test.sh" for i in range(30000)]
    monkeypatch.setattr(type(change), "locked_paths", lambda self: (many, {}))
    f = settings_file(change, "review", "reviewer-claude")
    assert f.stat().st_size < 200_000 and "t_00001" not in f.read_text()
