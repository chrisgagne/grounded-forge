"""After the send-back: fixed text is fixed code in whatever literal form it's written (raw, triple-quoted, prefixed,
f-string with no placeholder, adjacent literals, a concatenation of literals only, a template literal with no ${...}),
and the other ways of reaching eval and exec (globalThis.eval, window.eval, (0, eval), an alias of eval,
builtins.eval/exec) are flagged when the argument is built at run time. Calls the real semgrep on tiny inputs."""
import json
import os
import shutil
import subprocess

import pytest
from conftest import make_app

from factory.ledger import Change
from factory.stages import gate
from factory.stages.tests import write_lock

needs = pytest.mark.skipif(not shutil.which("semgrep"), reason="needs semgrep")


def scan(tmp_path, files: dict) -> list[dict]:
    """semgrep's results for `files` (name -> text) under factory's pinned rules only."""
    src = tmp_path / "src"
    src.mkdir(exist_ok=True)
    for name, text in files.items():
        (src / name).write_text(text)
    home = tmp_path / "home"
    home.mkdir(exist_ok=True)
    out = subprocess.run(["semgrep", "scan", "--config", str(gate.PINNED_RULES), "--metrics=off", "--json", "--quiet",
                          "--disable-version-check", "--disable-nosem", "--", *files], cwd=src, capture_output=True,
                         text=True, env={**os.environ, "SEMGREP_SETTINGS_FILE": str(home / "s.yml"),
                                         "SEMGREP_LOG_FILE": str(home / "log"),
                                         "SEMGREP_VERSION_CACHE_PATH": str(home / "v"),
                                         "XDG_CONFIG_HOME": str(home), "HOME": str(home)})
    assert out.returncode == 0, out.stderr[-500:]
    report = json.loads(out.stdout)
    assert not report.get("errors"), report["errors"]
    return report.get("results") or []


def flagged(tmp_path, files: dict) -> set[tuple[str, int]]:
    return {(str(r["path"]).removeprefix("./"), int(r["start"]["line"])) for r in scan(tmp_path, files)}


def new_change(root, name="e1") -> Change:
    app = make_app(root)
    story = root / "s.md"
    story.write_text("# Evaluate\n")
    change = Change.create(app, story, change_id=name)
    write_lock(change)
    return change


def commit(change, files: dict) -> None:
    for rel, text in files.items():
        p = change.worktree / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    change.commit_all("build")


PY_FIXED_TEXT = ('eval(r"1 + 1")\n'
                 "exec(r'x = 1')\n"
                 'eval("""1 + 1""")\n'
                 "exec('''x = 1''')\n"
                 'exec("""\n'
                 'x = 1\n'
                 '""")\n'
                 'eval(b"1 + 1")\n'
                 'exec(u"x = 1")\n'
                 'exec(rb"x = 1")\n'
                 'eval(f"1 + 1")\n'
                 'exec(f"x = 1")\n'
                 'exec("x = " "1")\n'
                 'exec("x = " + "1")\n'
                 'eval("1 + " + "1")\n'
                 'eval(r"1 + 1", {})\n'
                 "exec('''x = 1''', {}, {})\n"
                 'exec(b"x = 1", globals(), locals())\n'
                 'eval(f"1 + 1", {}, {})\n'
                 'exec("x = " "1", {})\n'
                 'exec("x = " + "1", globals(), locals())\n')


@needs
def test_python_fixed_text_in_any_literal_form_is_not_flagged(tmp_path):
    assert flagged(tmp_path, {"fixed.py": PY_FIXED_TEXT}) == set()


@needs
def test_js_and_ts_fixed_text_in_any_literal_form_is_not_flagged(tmp_path):
    js = ("eval('1 + 1');\n"
          "eval(`1 + 1`);\n"
          "eval(\"1 + \" + \"1\");\n"
          "eval('1 + ' + '1');\n"
          "const f = new Function('return 1');\n"
          "const g = new Function(`return 1`);\n"
          "const h = new Function(\"return \" + \"1\");\n"
          "module.exports = { f, g, h };\n")
    ts = ("eval('1 + 1');\n"
          "eval(`1 + 1`);\n"
          "eval(\"1 + \" + \"1\");\n"
          "const f = new Function('return 1');\n"
          "const g = new Function(`return 1`);\n"
          "const h = new Function(\"return \" + \"1\");\n"
          "export { f, g, h };\n")
    assert flagged(tmp_path, {"fixed.js": js, "fixed.ts": ts}) == set()


@needs
def test_js_other_ways_of_calling_eval_on_a_built_string_are_flagged(tmp_path):
    built = ("const x = process.argv[2];\n"
             "globalThis.eval(x);\n"
             "window.eval(x);\n"
             "(0, eval)(x);\n"
             "const run = eval;\n"
             "run(x);\n"
             "module.exports = { x };\n")
    fixed = ("globalThis.eval(\"1 + 1\");\n"
             "window.eval(\"1 + 1\");\n"
             "(0, eval)(\"1 + 1\");\n"
             "const run = eval;\n"
             "run(\"1 + 1\");\n"
             "module.exports = { run };\n")
    assert flagged(tmp_path, {"built.js": built, "fixed.js": fixed}) == {("built.js", n) for n in (2, 3, 4, 6)}


@needs
def test_python_builtins_eval_and_exec_of_a_built_string_are_flagged(tmp_path):
    built = ("import builtins\n"
             "import sys\n"
             "x = sys.argv[1]\n"
             "builtins.eval(x)\n"
             "builtins.exec(x)\n"
             "print(x)\n")
    fixed = ("import builtins\n"
             "builtins.eval(\"1 + 1\")\n"
             "builtins.exec(\"x = 1\")\n")
    assert flagged(tmp_path, {"built.py": built, "fixed.py": fixed}) == {("built.py", 4), ("built.py", 5)}


@needs
def test_gate_sast_passes_on_eval_of_fixed_text_in_any_literal_form(tmp_path):
    change = new_change(tmp_path)
    commit(change, {"src/fixed.py": PY_FIXED_TEXT})
    change.start("gate")
    ev = gate.sast(change)
    assert ev["status"] == "pass"


@needs
def test_gate_sast_fails_on_an_added_qualified_eval_or_exec_of_a_variable(tmp_path):
    js = new_change(tmp_path / "js", name="e-js")
    commit(js, {"src/run.js": "const input = process.argv[2];\nglobalThis.eval(input);\n"})
    js.start("gate")
    ev = gate.sast(js)
    assert ev["status"] == "fail" and "src/run.js:2" in ev["reason"]

    py = new_change(tmp_path / "py", name="e-py")
    commit(py, {"src/run.py": "import builtins\nimport sys\ncode = sys.argv[1]\nbuiltins.exec(code)\n"})
    py.start("gate")
    ev = gate.sast(py)
    assert ev["status"] == "fail" and "src/run.py:4" in ev["reason"]
