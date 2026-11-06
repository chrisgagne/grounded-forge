"""The Codex reviewer runs under the factory's sandbox-exec profile: it reads only its own folder (export, packet,
logs, private home), what its CLI needs and the system, and reaches the network only through a proxy that lets it
reach its provider."""
import json
import socket
import stat
import sys
import threading
from pathlib import Path

import pytest
from conftest import sh
from test_review_legs import leg_result

from factory import isolation, legs, proxy
from factory.stages import review

mac = pytest.mark.skipif(sys.platform != "darwin" or not isolation.available()[0], reason="needs sandbox-exec")


@pytest.fixture
def secret(tmp_path, monkeypatch):
    d = tmp_path / "secret"
    d.mkdir()
    (d / "key").write_text("sk-live-do-not-read\n")
    monkeypatch.setattr(isolation, "SECRET_PATHS", isolation.SECRET_PATHS + (str(d),))
    return d


def test_a_read_confined_profile_allows_reads_only_under_its_roots(tmp_path):
    root, need = tmp_path / "root", tmp_path / "secret-it-needs"
    pol = isolation.Policy(writable=[str(tmp_path / "w")], readable=[str(root)], read_secrets=[str(need)])
    text = pol.profile(str(tmp_path / "t"))
    lines = text.splitlines()
    assert "(deny file-read*)" in lines
    allow = next(l for l in lines if l.startswith("(allow file-read* "))
    assert f'(subpath "{root}")' in allow and f'(subpath "{tmp_path / "w"}")' in allow and "/System" in allow
    secret_deny = next(i for i, l in enumerate(lines) if l.startswith("(deny file-read* (subpath"))
    exception = next(i for i, l in enumerate(lines) if f'(literal "{need}")' in l and l.startswith("(allow file-read*"))
    assert exception > secret_deny  # later rules win: only the named secret comes back
    assert "(deny file-read*)" not in isolation.Policy(writable=[]).profile("/tmp/x")  # gate commands: unchanged


@mac
def test_a_read_confined_command_reads_only_its_roots(tmp_path, secret):
    inside, outside = tmp_path / "inside", tmp_path / "outside"
    inside.mkdir()
    outside.mkdir()
    (inside / "code.txt").write_text("inside-ok\n")
    (outside / "private.txt").write_text("outside-private\n")
    pol = isolation.Policy(writable=[], readable=[str(isolation.expand(inside))])
    cmd = (f"cat code.txt; cat '{outside}/private.txt'; ls '{Path.home()}/Documents'; cat '{secret}/key'; "
           f"echo x > '{inside}/w.txt'; echo end")
    res = legs.run_command(cmd, inside, tmp_path / "log.txt", 60, policy=pol)
    out = (tmp_path / "log.txt").read_text()
    assert res["sandbox"] == "sandbox-exec"
    assert "inside-ok" in out and "end" in out
    assert "outside-private" not in out and "sk-live" not in out
    assert "Operation not permitted" in out
    assert not (inside / "w.txt").exists()


def upstream():
    """A local TCP echo server standing in for the provider."""
    srv = socket.socket()
    srv.bind(("127.0.0.1", 0))
    srv.listen(5)

    def serve():
        while True:
            try:
                c, _ = srv.accept()
            except OSError:
                return
            data = c.recv(1024)
            c.sendall(b"echo:" + data)
            c.close()
    threading.Thread(target=serve, daemon=True).start()
    return srv


def connect(proxy_url: str, line: bytes) -> bytes:
    host, port = proxy_url.rsplit("//", 1)[1].rsplit(":", 1)
    s = socket.create_connection((host, int(port)), timeout=10)
    s.sendall(line + b"\r\n\r\n")
    head = s.recv(1024)
    body = b""
    if b" 200 " in head:
        s.sendall(b"ping")
        body = s.recv(1024)
    s.close()
    return head + body


def test_the_proxy_tunnels_only_to_allowed_hosts_on_the_allowed_port():
    srv = upstream()
    port = srv.getsockname()[1]
    with proxy.AllowlistProxy(["127.0.0.1"], port=port) as p:
        assert p.url.startswith("http://127.0.0.1:")
        assert b"echo:ping" in connect(p.url, f"CONNECT 127.0.0.1:{port} HTTP/1.1".encode())
        assert b" 403 " in connect(p.url, f"CONNECT 127.0.0.1:{port + 1} HTTP/1.1".encode())
        assert b" 403 " in connect(p.url, b"CONNECT example.com:443 HTTP/1.1")
        assert b" 403 " in connect(p.url, f"GET http://127.0.0.1:{port}/ HTTP/1.1".encode())
        assert b" 403 " in connect(p.url, b"CONNECT 127.0.0.1@example.com:443 HTTP/1.1")
    assert p.allowed == {f"127.0.0.1:{port}"}
    assert {"example.com:443", f"127.0.0.1:{port + 1}"} <= p.denied
    srv.close()


def fake_spawn(seen):
    def spawn(cmd, cwd, log, timeout_s, env, stderr_log=None):
        seen.update(cmd=list(cmd), env=dict(env), cwd=cwd)
        if cmd[0] == isolation.SANDBOX_EXEC:
            seen["profile"] = Path(cmd[2]).read_text()
        out = Path(cmd[cmd.index("-o") + 1])
        out.write_text("[]")
        log.write_text("tokens used\n10\n")
        return {"exit": 0, "started": "t", "finished": "t", "duration_s": 0}
    return spawn


def codex_dirs(tmp_path):
    d = tmp_path / "codex"
    for sub in ("export", "packet", "logs"):
        (d / sub).mkdir(parents=True)
    return d


def test_codex_runs_inside_the_factory_profile_with_its_own_sandbox_off(tmp_path, monkeypatch):
    monkeypatch.setattr(legs, "codex_bin", lambda: "/bin/echo")
    monkeypatch.setattr(isolation, "available", lambda: (True, "ok"))
    seen = {}
    monkeypatch.setattr(legs, "_spawn", fake_spawn(seen))
    d = codex_dirs(tmp_path)
    res = legs.run_codex("p", d / "export", d / "logs" / "log.txt", d / "logs" / "out.md", model=None, timeout_s=10,
                         read=[d])
    assert res["ok"] and res["sandbox"] == "sandbox-exec"
    cmd = seen["cmd"]
    assert cmd[:2] == [isolation.SANDBOX_EXEC, "-f"]
    assert cmd[cmd.index("-s") + 1] == "danger-full-access"  # nested sandboxes are refused; ours is the boundary
    assert "(deny file-read*)" in seen["profile"]
    assert f'(subpath "{isolation.expand(d)}")' in seen["profile"]
    assert "(deny network*)" in seen["profile"]  # only loopback: the proxy
    env = seen["env"]
    assert env["HTTPS_PROXY"].startswith("http://127.0.0.1:") and env["HTTPS_PROXY"] == env["https_proxy"]
    assert env["CODEX_HOME"].startswith(isolation.expand(d) + "/")
    assert res["confinement"]["read_roots"] and res["confinement"]["proxy_hosts"] == list(legs.CODEX_DOMAINS)


def test_codex_does_not_run_unconfined_when_the_sandbox_is_unavailable(tmp_path, monkeypatch):
    monkeypatch.setattr(legs, "codex_bin", lambda: "/bin/echo")
    monkeypatch.setattr(isolation, "available", lambda: (False, "nested"))
    seen = {}
    monkeypatch.setattr(legs, "_spawn", fake_spawn(seen))
    d = codex_dirs(tmp_path)
    res = legs.run_codex("p", d / "export", d / "logs" / "log.txt", d / "logs" / "out.md", model=None, timeout_s=10,
                         read=[d])
    assert not res["ok"] and "unconfined" in res["error"] and not seen


def test_with_os_sandbox_off_codex_keeps_its_own_read_only_sandbox(tmp_path, monkeypatch):
    monkeypatch.setattr(legs, "codex_bin", lambda: "/bin/echo")
    seen = {}
    monkeypatch.setattr(legs, "_spawn", fake_spawn(seen))
    d = codex_dirs(tmp_path)
    res = legs.run_codex("p", d / "export", d / "logs" / "log.txt", d / "logs" / "out.md", model=None, timeout_s=10,
                         read=[d], os_sandbox=False)
    assert res["ok"] and res["sandbox"] == "off"
    assert seen["cmd"][0] != isolation.SANDBOX_EXEC and seen["cmd"][seen["cmd"].index("-s") + 1] == "read-only"


def fake_codex(bin_dir: Path, probes: list[str]) -> Path:
    """A stand-in Codex CLI: it tries each probe read, prints what it got, and answers an empty findings list."""
    script = bin_dir / "codex"
    bin_dir.mkdir(parents=True, exist_ok=True)
    reads = "\n".join(f"echo '--- {p}'; cat '{p}' 2>&1 | head -c 200; echo" for p in probes)
    script.write_text("#!/bin/sh\n"
                      'while [ $# -gt 0 ]; do [ "$1" = -o ] && out="$2"; shift; done\n'
                      f"{reads}\n"
                      "echo '--- export'; cat src/greet.sh\n"
                      "echo '[]' > \"$out\"\n")
    script.chmod(script.stat().st_mode | stat.S_IXUSR)
    return script


@mac
def test_the_codex_reviewer_cannot_read_the_change_folder_the_other_reviewer_or_the_operators_files(
        change, tmp_path, monkeypatch, secret):
    wt = change.worktree
    (wt / "src" / "greet.sh").write_text('echo "Hello there, $1"\n')
    change.commit_all("build")
    (change.dir / "builder-summary.md").write_text("BUILDER-SAYS-ALL-GOOD\n")
    private = tmp_path / "operator-notes.txt"
    private.write_text("OPERATOR-PRIVATE\n")
    work_root = change.worktree.parent / ".factory-tmp"
    probes = [str(change.dir / "builder-summary.md"), str(private), f"{secret}/key"]
    monkeypatch.setenv("CODEX_BIN", str(fake_codex(tmp_path / "codex-bin", probes)))
    monkeypatch.setattr(legs, "codex_bin", lambda: str(tmp_path / "codex-bin" / "codex"))
    seen = {}

    def claude(prompt, cwd, log, **kw):
        # the Claude reviewer leaves a file in its own folder for Codex to try to read
        (Path(cwd).parent / "logs" / "claude-scratch.txt").write_text("CLAUDE-REVIEWER-NOTES\n")
        seen["claude_scratch"] = Path(cwd).parent / "logs" / "claude-scratch.txt"
        return leg_result(log, "[]")

    real_codex = legs.run_codex

    def codex(prompt, cwd, log, out, **kw):
        # probe the Claude reviewer's folder too, now that it exists
        fake_codex(tmp_path / "codex-bin", probes + [str(seen["claude_scratch"])])
        return real_codex(prompt, cwd, log, out, **kw)

    monkeypatch.setattr(legs, "run_claude", claude)
    monkeypatch.setattr(legs, "run_codex", codex)
    monkeypatch.setattr(review, "DEFAULT_LEGS", ("claude", "codex"))
    # run Claude first so its file exists before Codex probes
    monkeypatch.setattr(review, "ThreadPoolExecutor", SerialExecutor)
    assert review.run(change) is True, (change.dir / "decisions-needed.md").read_text()
    out = (change.dir / "review" / "codex-log.txt").read_text()
    assert "Hello there" in out  # its own export: readable
    for leaked in ("BUILDER-SAYS-ALL-GOOD", "OPERATOR-PRIVATE", "sk-live", "CLAUDE-REVIEWER-NOTES"):
        assert leaked not in out, out
    leg = [e for e in change.ledger.events() if e.get("check") == "leg:reviewer-codex"][-1]
    assert leg["sandbox"] == "sandbox-exec"
    assert not any(str(work_root) == r for r in leg["confinement"]["read_roots"])


class SerialExecutor:
    """ThreadPoolExecutor stand-in that runs each job when it's submitted, in order."""

    def __init__(self, *a):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def submit(self, fn, *a):
        class Done:
            def __init__(self, v):
                self.v = v

            def result(self):
                return self.v
        return Done(fn(*a))
