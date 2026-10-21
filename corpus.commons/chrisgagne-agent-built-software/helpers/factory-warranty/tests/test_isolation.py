"""OS isolation: builder-controlled code can't write outside the worktree, read secrets, or reach the evidence."""
import json
from pathlib import Path
import sys

import pytest
from conftest import make_app, sh

from factory import isolation, legs
from factory.ledger import Change, Ledger
from factory.stages import adapter_leg
from factory.stages.tests import write_lock

mac = pytest.mark.skipif(sys.platform != "darwin" or not isolation.available()[0], reason="needs sandbox-exec")


def payload(root, change) -> str:
    """A script that tries every escape a build leg might try, then does one honest write."""
    common = sh(change.worktree, "git", "rev-parse", "--path-format=absolute", "--git-common-dir").strip()
    return "\n".join([
        f"echo escaped > '{root}/outside.txt'",
        f"echo '[]' > '{change.dir}/ledger.json'",
        f"echo pwned >> '{change.dir}/tests.lock'",
        f"git config --file '{common}/config' core.hooksPath /tmp/hooks",
        f"echo 'gitdir: /tmp/fake' > .git",
        f"cat '{root}/secret/key' > leaked.txt",
        "echo built > src/ok.txt",
        "echo done",
    ]) + "\n"


@pytest.fixture
def secret(tmp_path, monkeypatch):
    d = tmp_path / "secret"
    d.mkdir()
    (d / "key").write_text("sk-live-do-not-read\n")
    monkeypatch.setattr(isolation, "SECRET_PATHS", isolation.SECRET_PATHS + (str(d),))
    return d


@mac
def test_a_script_the_build_leg_writes_and_runs_cannot_escape_the_worktree(tmp_path, secret):
    app = make_app(tmp_path, builder={"kind": "command", "command": {"build": "sh payload.sh"}})
    story = tmp_path / "story.md"
    story.write_text("# x\n")
    change = Change.create(app, story, change_id="iso1")
    write_lock(change)
    (change.worktree / "payload.sh").write_text(payload(tmp_path, change))  # the leg wrote it in an earlier turn
    ledger_before = json.loads((change.dir / "ledger.json").read_text())
    lock_before = (change.dir / "tests.lock").read_bytes()
    git_file = (change.worktree / ".git").read_text()
    config_before = (app / ".git" / "config").read_text()

    res = adapter_leg(change, "build", "brief")

    assert res["sandbox"] == "sandbox-exec"
    assert (change.worktree / "src" / "ok.txt").read_text() == "built\n"  # inside the worktree: allowed
    assert not (tmp_path / "outside.txt").exists()
    assert (change.dir / "tests.lock").read_bytes() == lock_before
    assert (change.worktree / ".git").read_text() == git_file
    assert (app / ".git" / "config").read_text() == config_before
    leaked = change.worktree / "leaked.txt"
    assert not leaked.exists() or "sk-live" not in leaked.read_text()
    events = json.loads((change.dir / "ledger.json").read_text())
    assert events[:len(ledger_before)] == ledger_before
    Ledger.verify(events)


@mac
def test_gate_commands_cannot_write_outside_the_worktree_or_read_secrets(change, tmp_path, secret):
    change.start("gate")
    ev = change.run_check("gate", "tests", f"echo x > '{tmp_path}/outside.txt'")
    assert ev["status"] == "fail" and ev["sandbox"] == "sandbox-exec" and not (tmp_path / "outside.txt").exists()
    ev = change.run_check("gate", "tests", f"cat '{secret}/key'")
    assert ev["status"] == "fail" and "sk-live" not in ev["output_tail"]
    ev = change.run_check("gate", "tests", f"echo x > '{change.dir}/gate/forged.log'")
    assert ev["status"] == "fail" and not (change.dir / "gate" / "forged.log").exists()
    ev = change.run_check("gate", "tests", "sh test/run.sh && echo ok > build-output.txt")
    assert ev["status"] == "pass" and (change.worktree / "build-output.txt").exists()


@mac
def test_gate_commands_have_no_network_unless_the_config_grants_it(change):
    change.start("gate")
    probe = "python3 -c \"import socket; socket.create_connection(('1.1.1.1', 53), 3)\""
    assert change.run_check("gate", "tests", probe)["status"] == "fail"
    assert change.policy("install").network is True and change.policy("tests").network is False


@mac
def test_the_spec_adapter_cannot_write_the_worktree(tmp_path):
    app = make_app(tmp_path, builder={"kind": "command", "command": {
        "spec": "echo x > src/sneaky.sh; printf '## AC-1: works\\ncheck: test/greet.test.sh :: greets\\n'"}})
    story = tmp_path / "story.md"
    story.write_text("# x\n")
    change = Change.create(app, story, change_id="iso2")
    res = adapter_leg(change, "spec", "brief", read_only=True)
    assert res["ok"] and "AC-1" in res["result"]
    assert not (change.worktree / "src" / "sneaky.sh").exists()


def test_when_the_os_sandbox_is_unavailable_builder_code_does_not_run(change, tmp_path, monkeypatch):
    monkeypatch.setattr(isolation, "available", lambda: (False, "no sandbox here"))
    change.config["isolation"]["os_sandbox"] = True  # the config asks for it, the platform can't give it
    change.start("gate")
    ev = change.run_check("gate", "tests", f"echo x > '{tmp_path}/ran.txt'")
    assert ev["status"] == "fail" and "unconfined" in ev["reason"] and not (tmp_path / "ran.txt").exists()
    # the factory's own scanners don't need the sandbox
    assert change.run_check("gate", "secrets", "true", trusted=True)["status"] == "pass"


def test_environment_is_an_allowlist(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgres://u:p@prod/db")
    monkeypatch.setenv("KUBECONFIG", "/operator/kube")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "k")
    env, dropped = legs.scrubbed_env()
    assert "DATABASE_URL" not in env and "KUBECONFIG" not in env and "ANTHROPIC_API_KEY" not in env
    assert "PATH" in env and "DATABASE_URL" in dropped
    env, _ = legs.scrubbed_env(keep=legs.CLAUDE_AUTH)
    assert env["ANTHROPIC_API_KEY"] == "k"


def test_a_builder_command_gets_only_the_credentials_isolation_env_names(monkeypatch, tmp_path):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "a")
    monkeypatch.setenv("OPENAI_API_KEY", "o")
    seen = {}

    def spawn(argv, cwd, log, timeout_s, env, stderr_log=None):
        seen.update(env)
        log.write_text("")
        return {"exit": 0, "started": "t", "finished": "t", "duration_s": 0}

    monkeypatch.setattr(legs, "_spawn", spawn)
    legs.run_builder_command("true", tmp_path, tmp_path / "log.txt", 10, {}, policy=None, os_sandbox=False)
    assert "ANTHROPIC_API_KEY" not in seen and "OPENAI_API_KEY" not in seen
    legs.run_builder_command("true", tmp_path, tmp_path / "log.txt", 10, {}, policy=None, os_sandbox=False,
                             env_names=("OPENAI_API_KEY",))
    assert seen["OPENAI_API_KEY"] == "o" and "ANTHROPIC_API_KEY" not in seen


def test_a_codex_rate_limit_is_retried_but_a_usage_limit_is_not(monkeypatch, tmp_path):
    monkeypatch.setattr(legs, "codex_bin", lambda: "/bin/true")
    monkeypatch.setattr(legs, "CODEX_BACKOFF_S", 0)
    calls = []

    def spawn(cmd, cwd, log, timeout_s, env, stderr_log=None):
        calls.append(1)
        out = tmp_path / "out.md"
        if len(calls) < 3:
            log.write_text("ERROR: exceeded retry limit, last status: 429 Too Many Requests\n")
            return {"exit": 1, "started": "t", "finished": "t", "duration_s": 0}
        log.write_text("tokens used\n1,234\n")
        out.write_text("[]")
        return {"exit": 0, "started": "t", "finished": "t", "duration_s": 0}

    monkeypatch.setattr(legs, "_spawn", spawn)
    res = legs.run_codex("p", tmp_path, tmp_path / "log.txt", tmp_path / "out.md", model=None, timeout_s=10)
    assert res["ok"] and res["attempts"] == 3 and len(calls) == 3
    calls.clear()

    def limited(cmd, cwd, log, timeout_s, env, stderr_log=None):
        calls.append(1)
        log.write_text("ERROR: You've hit your usage limit. 429 Too Many Requests\n")
        return {"exit": 1, "started": "t", "finished": "t", "duration_s": 0}

    monkeypatch.setattr(legs, "_spawn", limited)
    (tmp_path / "out.md").unlink()
    res = legs.run_codex("p", tmp_path, tmp_path / "log.txt", tmp_path / "out.md", model=None, timeout_s=10)
    assert not res["ok"] and len(calls) == 1


def test_profile_carves_protected_paths_out_of_the_worktree(change):
    pol = change.policy("tests")
    prof = pol.profile("/tmp/x")
    assert prof.index("(allow file-write*") < prof.index("(deny file-write* (literal")  # later rules win
    for p in (change.worktree / ".git", change.dir):
        assert isolation.expand(p) in pol.deny_write


def test_spec_stage_blocks_rather_than_commit_what_the_spec_leg_wrote(change, monkeypatch):
    from factory.stages import spec

    def writes(prompt, cwd, log, **kw):
        (cwd / "src" / "sneaky.sh").write_text("true\n")
        log.write_text("")
        return {"ok": True, "exit": 0, "family": "claude", "cmd": "claude", "started": "t", "finished": "t",
                "duration_s": 0, "log_path": log, "result": "## AC-1: x\ncheck: test/greet.test.sh :: greets\n",
                "output_sha256": "0" * 64}

    monkeypatch.setattr(legs, "run_claude", writes)
    head = change.head()
    assert spec.run(change) is False
    assert "may only read" in change.outcome("spec")["reason"] and change.head() == head


def test_claude_legs_run_in_claude_codes_sandbox_with_the_guard(change, monkeypatch):
    from factory.stages.tests import write_lock as lock
    lock(change)
    seen = {}

    def fake(prompt, cwd, log, **kw):
        seen.update(kw, prompt=prompt)
        seen["settings_json"] = json.loads(Path(kw["settings"]).read_text())
        log.write_text("")
        return {"ok": True, "exit": 0, "family": "claude", "cmd": "claude", "started": "t", "finished": "t",
                "duration_s": 0, "log_path": log, "result": "done", "output_sha256": "0" * 64}

    monkeypatch.setattr(legs, "run_claude", fake)
    adapter_leg(change, "build", "brief text")
    sb = seen["settings_json"]["sandbox"]
    assert sb["enabled"] is True and sb["failIfUnavailable"] is True and sb["allowUnsandboxedCommands"] is False
    assert sb["excludedCommands"] == [] and sb["network"]["allowedDomains"] == [] and sb["network"]["strictAllowlist"]
    deny = sb["filesystem"]["denyWrite"]
    for p in (change.worktree / ".git", change.dir, change.repo / ".factory", change.worktree / "test" / "greet.test.sh"):
        assert isolation.expand(p) in deny, p
    assert isolation.expand("~/.ssh") in sb["filesystem"]["denyRead"]
    assert any(r.startswith("Read(//") and ".ssh" in r for r in seen["settings_json"]["permissions"]["deny"])
    hook = seen["settings_json"]["hooks"]["PreToolUse"][0]["hooks"][0]
    assert "guard.py" in hook["command"] and "--secret" in hook["command"]
    # the folder the leg may read (and, being an --add-dir, write) is a private copy, never the change folder
    (share,) = seen["add_dirs"]
    assert change.dir not in Path(share).parents and Path(share) != change.dir
    assert str(share) in seen["prompt"]


@mac
def test_a_gate_command_cannot_weaken_a_locked_test_even_to_put_it_back(change):
    write_lock(change)
    locked = (change.worktree / "test" / "greet.test.sh").read_text()
    change.start("gate")
    for cmd in ("echo true > test/greet.test.sh", "mv test test.orig && mkdir test && echo true > test/greet.test.sh",
                "rm test/greet.test.sh", "ln -sf /dev/null test/greet.test.sh", "chmod +x test/greet.test.sh"):
        assert change.run_check("gate", "tests", cmd)["status"] == "fail", cmd
    assert (change.worktree / "test" / "greet.test.sh").read_text() == locked
    assert change.run_check("gate", "tests", "echo true > test/extra.test.sh")["status"] == "pass"


def test_on_macos_commands_get_a_ca_file_so_tls_libraries_start_in_the_sandbox(monkeypatch):
    monkeypatch.delenv("SSL_CERT_FILE", raising=False)
    env, _ = isolation.minimal_env()
    if sys.platform == "darwin" and Path(isolation.SYSTEM_CA_FILE).exists():
        assert env["SSL_CERT_FILE"] == isolation.SYSTEM_CA_FILE
    monkeypatch.setenv("SSL_CERT_FILE", "/custom/ca.pem")
    assert isolation.minimal_env()[0]["SSL_CERT_FILE"] == "/custom/ca.pem"  # the operator's own setting wins
