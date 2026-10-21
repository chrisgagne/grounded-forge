"""After the second send-back: eval reached through eval.call, eval.apply, Reflect.apply(eval, ...) or a computed
name on the global object (globalThis['eval']) is flagged when the evaluated argument is built at run time, not when
it's one plain string literal, and calls that only look similar aren't. The rule file says plainly which ways of
running a string as code it doesn't follow. Calls the real semgrep on tiny inputs."""
import json
import os
import shutil
import subprocess

import pytest
import yaml
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


def eval_rule_files() -> list:
    """The pinned rule files that hold a rule about eval (found by rule id, not by file name)."""
    found = []
    for path in sorted(gate.PINNED_RULES.glob("*.y*ml")):
        rules = (yaml.safe_load(path.read_text()) or {}).get("rules") or []
        if any("eval" in str(r.get("id", "")).lower() for r in rules):
            found.append(path)
    return found


@needs
def test_js_eval_reached_through_call_apply_reflect_or_a_computed_name_is_flagged(tmp_path):
    js = ("const x = process.argv[2];\n"
          "eval.call(null, x);\n"
          "eval.apply(null, [x]);\n"
          "Reflect.apply(eval, null, [x]);\n"
          "globalThis['eval'](x);\n"
          "globalThis[\"eval\"](x);\n"
          "module.exports = { x };\n")
    assert flagged(tmp_path, {"run.js": js}) == {("run.js", n) for n in range(2, 7)}


@needs
def test_js_eval_reached_through_call_apply_reflect_or_a_computed_name_on_a_literal_is_not_flagged(tmp_path):
    js = ("eval.call(null, \"1 + 1\");\n"
          "eval.apply(null, [\"1 + 1\"]);\n"
          "Reflect.apply(eval, null, [\"1 + 1\"]);\n"
          "globalThis['eval'](\"1 + 1\");\n"
          "globalThis[\"eval\"](\"1 + 1\");\n"
          "module.exports = {};\n")
    assert flagged(tmp_path, {"lit.js": js}) == set()


@needs
def test_js_lookalike_call_apply_reflect_and_computed_calls_are_not_flagged(tmp_path):
    js = ("const x = process.argv[2];\n"
          "function fn(s) { return s; }\n"
          "Reflect.apply(fn, null, [x]);\n"
          "fn.call(null, x);\n"
          "fn.apply(null, [x]);\n"
          "const obj = { eval: (s) => s };\n"
          "obj['eval'](x);\n"
          "obj[\"eval\"](x);\n"
          "module.exports = { obj };\n")
    assert flagged(tmp_path, {"look.js": js}) == set()


@needs
def test_gate_sast_fails_on_an_added_eval_call_apply_or_reflect_apply_of_a_variable(tmp_path):
    for name, line in (("call", "eval.call(null, input);"), ("apply", "eval.apply(null, [input]);"),
                       ("reflect", "Reflect.apply(eval, null, [input]);")):
        change = new_change(tmp_path / name, name=f"e-{name}")
        commit(change, {"src/run.js": f"const input = process.argv[2];\n{line}\n"})
        change.start("gate")
        ev = gate.sast(change)
        assert ev["status"] == "fail" and "src/run.js:2" in ev["reason"], (name, ev)


def test_the_rule_file_states_what_it_does_not_follow():
    files = eval_rule_files()
    assert files, f"no pinned rule file with an eval rule under {gate.PINNED_RULES}"
    text = "\n".join(p.read_text() for p in files)
    lower = text.lower()
    for named in ("setTimeout", "setInterval", "vm.runInNewContext", "vm.runInThisContext", "vm.Script"):
        assert named.lower() in lower, f"the rule file doesn't name {named}"
    assert "alias" in lower and "destructur" in lower, "the rule file doesn't name aliases assigned by destructuring"
    assert "getattr(builtins" in lower, "the rule file doesn't name a lookup such as getattr(builtins, \"exec\")"
    assert "however reached" not in lower
