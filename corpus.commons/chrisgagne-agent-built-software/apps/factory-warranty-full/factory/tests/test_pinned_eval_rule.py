"""The pinned rules flag code evaluated from a string built at run time: JavaScript/TypeScript `eval` and
`new Function`, Python `eval` and `exec`. A single plain string literal, and methods that only share the name, are
not flagged. Calls the real semgrep on tiny inputs (local only, no network)."""
import json
import os
import shutil
import subprocess

import pytest

from factory.stages import gate

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


@needs
def test_js_eval_of_a_variable_is_flagged(tmp_path):
    js = ("const input = process.argv[2];\n"
          "eval(input);\n"
          "const evaluated = input.length;\n"
          "console.log('eval', evaluated);\n")
    assert flagged(tmp_path, {"run.js": js}) == {("run.js", 2)}


@needs
def test_js_new_function_of_a_built_string_is_flagged(tmp_path):
    js = ("const body = process.argv[2];\n"
          "const f1 = new Function(body);\n"
          "const f2 = new Function('a', 'b', body);\n"
          "const f3 = new Function('return ' + body);\n"
          "const f4 = new Function(body + ';');\n"
          "const f5 = new Function(`return ${body}`);\n"
          "module.exports = { f1, f2, f3, f4, f5 };\n")
    assert flagged(tmp_path, {"fn.js": js}) == {("fn.js", n) for n in range(2, 7)}


@needs
def test_js_eval_of_a_concatenated_or_interpolated_string_is_flagged(tmp_path):
    js = ("const x = process.argv[2];\n"
          "eval(\"1 + \" + x);\n"
          "eval(x + ';');\n"
          "eval('var y = ' + x);\n"
          "eval(`return ${x}`);\n"
          "module.exports = { x };\n")
    assert flagged(tmp_path, {"run.js": js}) == {("run.js", n) for n in range(2, 6)}


@needs
def test_ts_eval_and_new_function_of_a_variable_are_flagged(tmp_path):
    ts = ("const x: string = process.argv[2];\n"
          "eval(x);\n"
          "const f = new Function(x);\n"
          "export { f };\n")
    assert flagged(tmp_path, {"run.ts": ts}) == {("run.ts", 2), ("run.ts", 3)}


@needs
def test_python_eval_and_exec_of_a_built_string_are_flagged(tmp_path):
    py = ("import sys\n"
          "x = sys.argv[1]\n"
          "eval(x)\n"
          "exec(x)\n"
          "eval(f\"{x} + 1\")\n"
          "exec(f\"y = {x}\")\n"
          "eval(\"1 + \" + x)\n"
          "exec(x + \"\\n\")\n"
          "eval(x, {})\n"
          "exec(x, {}, {})\n"
          "eval(x, globals(), locals())\n"
          "print(x)\n")
    assert flagged(tmp_path, {"run.py": py}) == {("run.py", n) for n in range(3, 12)}


@needs
def test_a_plain_string_literal_argument_is_not_flagged(tmp_path):
    js = ("eval(\"1 + 1\");\n"
          "eval('1 + 1');\n"
          "eval(`1 + 1`);\n"
          "const f = new Function(\"return 1\");\n"
          "const g = new Function('return 1');\n"
          "module.exports = { f, g };\n")
    py = ("eval(\"1 + 1\")\n"
          "exec(\"x = 1\")\n"
          "eval('1 + 1')\n"
          "exec('x = 1')\n")
    assert flagged(tmp_path, {"lit.js": js, "lit.py": py}) == set()


@needs
def test_methods_named_eval_or_exec_are_not_flagged(tmp_path):
    js = ("const text = process.argv[2];\n"
          "const pattern = /a(b)/g;\n"
          "const m = pattern.exec(text);\n"
          "const n = /c/.exec(text);\n"
          "const obj = { eval: (s) => s, exec: (s) => s };\n"
          "obj.eval(text);\n"
          "obj.exec(text);\n"
          "module.exports = { m, n };\n")
    py = ("import re\n"
          "import sys\n"
          "x = sys.argv[1]\n"
          "class Obj:\n"
          "    def eval(self, s):\n"
          "        return s\n"
          "    def exec(self, s):\n"
          "        return s\n"
          "obj = Obj()\n"
          "obj.eval(x)\n"
          "obj.exec(x)\n"
          "re.compile('a').match(x)\n")
    assert flagged(tmp_path, {"m.js": js, "m.py": py}) == set()


@needs
def test_eval_finding_is_blocking_and_says_what_it_found(tmp_path):
    results = scan(tmp_path, {"run.js": "const x = process.argv[2];\neval(x);\nconst f = new Function(x);\n",
                              "run.py": "import sys\nx = sys.argv[1]\nexec(x)\neval(x)\n"})
    where = {(str(r["path"]).removeprefix("./"), int(r["start"]["line"])) for r in results}
    assert {("run.js", 2), ("run.js", 3), ("run.py", 3), ("run.py", 4)} <= where
    for r in results:
        assert r["extra"]["severity"] in ("ERROR", "WARNING")
        message = r["extra"]["message"].lower()
        assert "eval" in message and "string" in message
