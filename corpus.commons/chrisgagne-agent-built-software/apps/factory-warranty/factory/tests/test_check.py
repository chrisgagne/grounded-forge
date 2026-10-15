"""factory check: the build leg's only shell command scans what the leg wrote before it runs anything."""
import json
import shutil
import subprocess

import pytest

from factory import check
from factory.stages.gate import PINNED_RULES


def sh(cwd, *args):
    subprocess.run(args, cwd=cwd, check=True, capture_output=True)


@pytest.fixture
def wt(tmp_path):
    w = tmp_path / "wt"
    (w / "src").mkdir(parents=True)
    (w / "src" / "a.js").write_text("const a = 1\nmodule.exports = { a }\n")
    sh(w, "git", "init", "-q", "-b", "main")
    sh(w, "git", "add", "-A")
    sh(w, "git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "base")
    return w


def spec(tmp_path, wt, configs=()):
    base = subprocess.run(["git", "rev-parse", "HEAD"], cwd=wt, capture_output=True, text=True).stdout.strip()
    f = tmp_path / "check.json"
    f.write_text(json.dumps({"worktree": str(wt), "baseline": base, "semgrep_configs": list(configs),
                             "commands": {"test": "echo ran > ran.txt"}}))
    return str(f)


def test_a_clean_change_runs_the_command(tmp_path, wt):
    (wt / "src" / "a.js").write_text("const a = 2\nmodule.exports = { a }\n")
    (wt / "src" / "b.js").write_text("module.exports = 3\n")
    assert check.main([spec(tmp_path, wt), "test"]) == 0
    assert (wt / "ran.txt").exists()


def test_invisible_characters_stop_the_command(tmp_path, wt):
    (wt / "src" / "a.js").write_text("const a = 1 // ok‮\nmodule.exports = { a }\n")
    assert check.main([spec(tmp_path, wt), "test"]) == check.BLOCKED
    assert not (wt / "ran.txt").exists()


@pytest.mark.skipif(not shutil.which("gitleaks"), reason="needs gitleaks")
def test_a_secret_in_a_new_file_stops_the_command(tmp_path, wt):
    (wt / "src" / "c.js").write_text('const t = "ghp_' + "aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3zA5" + '"\n')
    assert check.main([spec(tmp_path, wt), "test"]) == check.BLOCKED
    assert not (wt / "ran.txt").exists()


@pytest.mark.skipif(not shutil.which("semgrep"), reason="needs semgrep")
def test_semgrep_on_an_added_line_stops_the_command(tmp_path, wt):
    (wt / "src" / "db.js").write_text(
        "function find(db, name) {\n  return db.prepare(\"SELECT * FROM users WHERE name = '\" + name + \"'\").all()\n}\n"
        "module.exports = { find }\n")
    assert check.main([spec(tmp_path, wt, [str(PINNED_RULES)]), "test"]) == check.BLOCKED
    assert not (wt / "ran.txt").exists()


def test_only_the_named_gate_commands_run(tmp_path, wt):
    assert check.main([spec(tmp_path, wt), "deploy"]) == 2
    assert not (wt / "ran.txt").exists()


def test_the_claude_build_leg_may_run_only_the_check(tmp_path, monkeypatch):
    import shlex
    from conftest import make_app
    from factory import legs
    from factory.ledger import Change
    from factory.stages import build
    from factory.stages.tests import write_lock
    app = make_app(tmp_path)
    story = tmp_path / "story.md"
    story.write_text("# x\n")
    change = Change.create(app, story, change_id="b1")
    write_lock(change)
    (change.dir / "acceptance.md").write_text("AC-1 x\ncheck: test/x\n")
    seen = {}

    def fake(prompt, cwd, log, *, settings=None, add_dirs=(), **kw):
        seen["settings"] = json.loads(settings.read_text())
        seen["brief"] = (add_dirs[0] / "brief.md").read_text()
        (cwd / "src" / "new.sh").write_text("echo hi\n")
        return {"ok": True, "family": "claude", "cmd": "claude", "started": "s", "finished": "f", "duration_s": 0,
                "result": "done", "log_path": None}

    monkeypatch.setattr(legs, "run_claude", fake)
    start = change.head()
    build.run(change)
    hook = seen["settings"]["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
    words = shlex.split(hook)
    allowed = [words[i + 1] for i, w in enumerate(words) if w == "--bash-only"]
    script = change.dir / "build" / "check"
    assert allowed and all(shlex.split(a)[0] == str(script) for a in allowed)
    assert "-I -m factory.check" in script.read_text() and all(a in seen["brief"] for a in allowed)
    names = {shlex.split(a)[1] for a in allowed}
    assert "test" in names and "install" not in names
    assert json.loads((change.dir / "build" / "check.json").read_text())["baseline"] == start  # the leg's work only


def test_the_check_fails_closed_when_it_cannot_tell_what_changed(tmp_path, wt):
    f = spec(tmp_path, wt)
    data = json.loads(open(f).read())
    data["baseline"] = "0" * 40  # a commit that doesn't exist: git diff fails
    open(f, "w").write(json.dumps(data))
    assert check.main([f, "test"]) == check.BLOCKED
    assert not (wt / "ran.txt").exists()


@pytest.mark.skipif(not shutil.which("semgrep"), reason="needs semgrep")
def test_an_added_eval_of_a_variable_stops_the_command(tmp_path, wt, capsys):
    cases = [("src/run.js", "const input = process.argv[2]\neval(input)\n", 2),
             ("src/fn.js", "const body = process.argv[2]\nconst f = new Function(body)\nmodule.exports = { f }\n", 2),
             ("src/run.py", "import sys\ncode = sys.argv[1]\nexec(code)\n", 3)]
    for path, text, line in cases:
        (wt / path).write_text(text)
        capsys.readouterr()
        assert check.main([spec(tmp_path, wt, [str(PINNED_RULES)]), "test"]) == check.BLOCKED, path
        assert f"{path}:{line}" in capsys.readouterr().out
        assert not (wt / "ran.txt").exists()
        (wt / path).unlink()


@pytest.mark.skipif(not shutil.which("semgrep"), reason="needs semgrep")
def test_an_added_eval_of_a_string_literal_lets_the_command_run(tmp_path, wt):
    (wt / "src" / "lit.js").write_text("eval(\"1 + 1\")\nconst f = new Function(\"return 1\")\nmodule.exports = { f }\n")
    (wt / "src" / "lit.py").write_text("eval(\"1 + 1\")\nexec(\"x = 1\")\n")
    assert check.main([spec(tmp_path, wt, [str(PINNED_RULES)]), "test"]) == 0
    assert (wt / "ran.txt").exists()
