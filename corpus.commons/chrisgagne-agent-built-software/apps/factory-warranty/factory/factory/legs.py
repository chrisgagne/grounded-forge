"""Headless legs: shell commands, `claude -p` runs and `codex exec` runs.

Patterned on grounded-forge's Pass I driver (`scripts/pass_i/run.py`, class
`Agent`): each leg is a fresh process in its own session, logged to a file,
killed with its process group when it overruns, and costed from its own output.

Every leg and command runs with a minimal environment built from an
allowlist (`isolation.minimal_env`), plus the one credential its own CLI needs
to sign in. Commands that run builder-controlled code (gate checks, adapters)
run under `sandbox-exec` with the policy the caller passes (`isolation.Policy`).
Claude legs load no MCP servers (`--strict-mcp-config`), only the settings the
caller names and a named tool set; Codex legs ignore the user's config.toml
(and its MCP servers). So a leg can't reach the operator's mail, drive or other
tools.
"""
from __future__ import annotations

import datetime as dt
import functools
import hashlib
import json
import os
import re
import shlex
import shutil
import signal
import subprocess
import time
from pathlib import Path

from factory import isolation, proxy

CODEX_RETRIES = 3
CODEX_BACKOFF_S = 60
CODEX_FALLBACKS = ["/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex"]
CLAUDE_AUTH = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN")
CODEX_AUTH = ("OPENAI_API_KEY",)
# Hosts a confined Codex leg may reach through the proxy: ChatGPT sign-in (chatgpt.com), API-key sign-in
# (api.openai.com) and token refresh (auth.openai.com).
CODEX_DOMAINS = ("chatgpt.com", "api.openai.com", "auth.openai.com")
READ_ONLY_TOOLS = "Read,Grep,Glob"
WRITE_TOOLS = "Bash,Edit,Write,Read,Grep,Glob,NotebookEdit"  # no web, publishing, scheduling or messaging tools
TAIL_CHARS = 2000


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def scrubbed_env(keep: tuple[str, ...] = (), extra_names: tuple[str, ...] = ()) -> tuple[dict, list[str]]:
    """The allowlisted environment plus `keep` (a CLI's own credential) and `extra_names` (config `isolation.env`)."""
    return isolation.minimal_env(keep=tuple(keep) + tuple(extra_names))


@functools.lru_cache(maxsize=None)
def tool_identity(name: str) -> dict:
    """Path, `--version` output and binary sha256 of a tool, so a changed scanner or CLI shows in the ledger
    (NIST SP 800-218A PW.6.2 C1; SSDF 1.1 PW.6.1)."""
    path = codex_bin() if name == "codex" else os.environ.get("CLAUDE_BIN", shutil.which("claude")) if name == "claude" \
        else shutil.which(name)
    if not path or not Path(path).exists():
        return {"name": name, "path": None}
    real = Path(path).resolve()
    try:
        out = subprocess.run([str(real), "--version"], capture_output=True, text=True, timeout=60)
        version = (out.stdout or out.stderr).strip().splitlines()[0][:200] if (out.stdout or out.stderr).strip() else ""
    except Exception as e:  # recorded, not fatal: the tool's own check fails later if it can't run
        version = f"(version check failed: {type(e).__name__})"
    return {"name": name, "path": str(real), "version": version, "sha256": hashlib.sha256(real.read_bytes()).hexdigest()}


def record_tools(change, stage: str, names: tuple[str, ...]) -> dict:
    return change.record(stage, "info", check="tools", tools=[tool_identity(n) for n in names])


def codex_bin() -> str | None:
    for c in [os.environ.get("CODEX_BIN"), shutil.which("codex"), *CODEX_FALLBACKS]:
        if c and Path(c).exists():
            return c
    return None


def _kill(p: subprocess.Popen) -> None:
    try:
        os.killpg(p.pid, signal.SIGTERM)
        p.wait(timeout=10)
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, signal.SIGKILL)
        p.wait()
    except ProcessLookupError:
        pass


def _spawn(cmd, cwd: Path, log: Path, timeout_s: int, env: dict, stderr_log: Path | None = None) -> dict:
    started, t0 = now(), time.monotonic()
    log.parent.mkdir(parents=True, exist_ok=True)
    err = stderr_log.open("wb") if stderr_log else subprocess.STDOUT
    res = {"started": started}
    with log.open("wb") as out:
        p = subprocess.Popen(cmd, cwd=cwd, stdout=out, stderr=err, stdin=subprocess.DEVNULL, env=env,
                             start_new_session=True)
        try:
            res["exit"] = p.wait(timeout=timeout_s)
        except subprocess.TimeoutExpired:
            _kill(p)
            res.update(exit=None, timed_out=True, error=f"killed after {timeout_s // 60} min")
        except BaseException:  # the driver is being stopped: take the leg down with it
            _kill(p)
            raise
        finally:
            if stderr_log:
                err.close()
    res.update(finished=now(), duration_s=round(time.monotonic() - t0, 1))
    return res


def unconfined(policy, os_sandbox: bool) -> str | None:
    """Why a command under this policy can't be confined, or None when it can (or needs no confinement)."""
    if policy is None or not os_sandbox:
        return None
    ok, why = isolation.available()
    return None if ok else f"refusing to run builder-controlled code unconfined: {why}"


def run_command(cmd: str, cwd: Path, log: Path, timeout_s: int, stderr_log: Path | None = None,
                policy: isolation.Policy | None = None, os_sandbox: bool = True, env_names: tuple = (),
                tmp_root: Path | None = None) -> dict:
    """Run a shell command (a gate check) with output to log; exit, tail and output hash come back.

    With a policy, the command runs under sandbox-exec; if that can't be applied, it doesn't run (fail closed).
    `policy=None` is for the factory's own scanners, which parse the repo but don't execute it."""
    log.parent.mkdir(parents=True, exist_ok=True)
    why = unconfined(policy, os_sandbox)
    if why:
        log.write_text(why + "\n")
        return {"started": now(), "finished": now(), "duration_s": 0, "exit": None, "error": why,
                "output_tail": why, "output_sha256": hashlib.sha256(log.read_bytes()).hexdigest(), "sandbox": "unavailable"}
    with isolation.Sandboxed(policy, os_sandbox, tmp_root) as box:
        env, _ = scrubbed_env(extra_names=env_names)
        env.update(box.env())
        res = _spawn(box.argv(cmd), cwd, log, timeout_s, env, stderr_log=stderr_log)
    res["sandbox"] = "sandbox-exec" if policy is not None and os_sandbox else "off" if policy is not None else "none"
    data = log.read_bytes()
    res.update(output_tail=data[-TAIL_CHARS:].decode(errors="replace"), output_sha256=hashlib.sha256(data).hexdigest())
    if res["exit"] not in (0, None) and "error" not in res:
        res["error"] = f"exit {res['exit']}"
    return res


def run_builder_command(cmd: str, cwd: Path, log: Path, timeout_s: int, extra_env: dict,
                        policy: isolation.Policy | None = None, os_sandbox: bool = True, env_names: tuple = (),
                        tmp_root: Path | None = None) -> dict:
    """A `builder.kind: command` adapter, under sandbox-exec: stdout is the leg's artefact, stderr goes beside it."""
    log.parent.mkdir(parents=True, exist_ok=True)
    why = unconfined(policy, os_sandbox)
    if why:
        log.write_text("")
        return {"started": now(), "finished": now(), "duration_s": 0, "exit": None, "error": why, "family": "command",
                "cmd": cmd, "log_path": log, "result": "", "model": "(builder command)", "ok": False,
                "output_sha256": hashlib.sha256(b"").hexdigest()}
    with isolation.Sandboxed(policy, os_sandbox, tmp_root) as box:
        # No provider credential by default: a builder command gets only the names `isolation.env` lists, so an
        # adapter that needs one key is never also handed the other provider's.
        env, _ = scrubbed_env(extra_names=env_names)
        env.update(extra_env)
        env.update(box.env())
        res = _spawn(box.argv(cmd), cwd, log, timeout_s, env, stderr_log=log.with_suffix(".stderr.txt"))
    res["sandbox"] = "sandbox-exec" if policy is not None and os_sandbox else "off"
    text = log.read_text(errors="replace")
    res.update(family="command", cmd=cmd, log_path=log, result=text, model="(builder command)",
               ok=res["exit"] == 0, output_sha256=hashlib.sha256(text.encode()).hexdigest())
    if not res["ok"] and "error" not in res:
        res["error"] = f"builder command exited {res['exit']}"
    return res


def run_claude(prompt: str, cwd: Path, log: Path, *, model: str, timeout_s: int, read_only: bool = False,
               permission_mode: str = "auto", settings: Path | None = None, add_dirs: tuple = (),
               effort: str | None = None, setting_sources: str | None = "project", json_schema: dict | None = None) -> dict:
    """One `claude -p` leg. The log is the stream-json transcript; the final message comes back as `result`.
    With `json_schema`, the CLI holds the final message to that schema, so `result` is the JSON object alone."""
    cmd = [os.environ.get("CLAUDE_BIN", "claude"), "-p", prompt, "--output-format", "stream-json", "--verbose",
           "--model", model, "--no-session-persistence", "--strict-mcp-config"]
    if setting_sources is not None:
        cmd += ["--setting-sources", setting_sources]
    if read_only:
        cmd += ["--tools", READ_ONLY_TOOLS, "--allowedTools", READ_ONLY_TOOLS, "--permission-mode", "dontAsk"]
    else:
        cmd += ["--tools", WRITE_TOOLS, "--permission-mode", permission_mode]
    if settings:
        cmd += ["--settings", str(settings)]
    for d in add_dirs:
        cmd += ["--add-dir", str(d)]
    if effort:
        cmd += ["--effort", effort]
    if json_schema is not None:
        cmd += ["--json-schema", json.dumps(json_schema)]
    env, _ = scrubbed_env(keep=CLAUDE_AUTH)
    res = _spawn(cmd, cwd, log, timeout_s, env)
    res.update(family="claude", log_path=log, cmd=shlex.join("<prompt>" if c == prompt else c for c in cmd))
    final, init = {}, {}
    for line in log.read_text(errors="replace").splitlines():
        try:
            j = json.loads(line)
        except json.JSONDecodeError:
            continue
        if j.get("type") == "result":
            final = j
        elif j.get("type") == "system" and j.get("subtype") == "init" and not init:
            init = j
    usage = final.get("modelUsage") or {}
    text = final.get("result") or ""
    res.update(cost_usd=final.get("total_cost_usd"), turns=final.get("num_turns"), session=final.get("session_id"),
               model=max(usage, key=lambda k: usage[k].get("costUSD", 0)) if usage else init.get("model", model),
               result=text, output_sha256=hashlib.sha256(text.encode()).hexdigest())
    res["ok"] = res["exit"] == 0 and bool(final) and not final.get("is_error")
    if not res["ok"] and "error" not in res:
        res["error"] = f"claude exited {res['exit']}: {final.get('subtype') or 'no result in the log'}"
    return res


def codex_auth_file() -> Path:
    return Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex") / "auth.json"


def codex_read_roots(binary: str) -> list[str]:
    """What the Codex CLI reads to start: its app bundle (the outermost `.app` holding the binary, since the inner
    CLI app loads resources beside it), else the folder the binary is in."""
    real = Path(isolation.expand(binary))
    apps = [p for p in real.parents if p.suffix == ".app"]
    return [str(apps[-1] if apps else real.parent)]


def codex_policy(binary: str, read, write, extra_read=()) -> isolation.Policy:
    """The profile the Codex reviewer runs under: reads only `read`, its CLI and the system; writes only `write`;
    network only to loopback (the proxy). Its sign-in file is the one secret it may read, and write, so a token
    refresh lands where the operator's own Codex finds it."""
    auth = isolation.expand(codex_auth_file())
    return isolation.Policy(writable=[*(isolation.expand(p) for p in write), auth],
                            readable=[*(isolation.expand(p) for p in read), *codex_read_roots(binary),
                                      *(isolation.expand(p) for p in extra_read)],
                            read_secrets=[auth], network=False, label="codex reviewer")


def run_codex(prompt: str, cwd: Path, log: Path, out: Path, *, model: str | None, timeout_s: int,
              sandbox: str = "read-only", output_schema: Path | None = None, effort: str | None = None,
              read=None, os_sandbox: bool = True, tmp_root: Path | None = None, extra_read=(),
              domains=None) -> dict:
    """One `codex exec` leg; its final message is written to `out` and comes back as `result`. With `output_schema`
    (a JSON Schema file), Codex holds the final message to that shape. `effort` sets Codex's reasoning effort; left
    out, the CLI's default applies (it reports "none").

    With `read` (the folders the leg may read), the leg runs confined: under sandbox-exec with `codex_policy`, a
    private Codex home holding only the sign-in, and its network through an `AllowlistProxy` to `domains` (default
    `CODEX_DOMAINS`). macOS refuses a sandbox inside a sandbox, so Codex's own sandbox is switched off there
    (`-s danger-full-access`) and the factory's profile is the boundary for Codex and every command it runs. If the
    profile can't be applied, the leg doesn't run. `os_sandbox=False` (the operator's opt-out) runs Codex with its
    own `-s sandbox` instead, reading the whole disk."""
    binary = codex_bin()
    if not binary:
        return {"ok": False, "family": "codex", "cmd": "codex exec", "error": "Codex CLI not found (set CODEX_BIN)",
                "started": now(), "finished": now(), "duration_s": 0, "log_path": None}
    confined = read is not None and os_sandbox
    home = codex_home(out.parent.parent) if confined else None
    policy = codex_policy(binary, [*read, out.parent, home], [out.parent, home], extra_read) if confined else None
    if confined:
        why = unconfined(policy, True)
        if why:
            return {"ok": False, "family": "codex", "cmd": "codex exec", "error": why, "sandbox": "unavailable",
                    "started": now(), "finished": now(), "duration_s": 0, "log_path": None}
    cmd = [binary, "exec", *(["-m", model] if model else []), "-s", "danger-full-access" if confined else sandbox,
           "--skip-git-repo-check", "--ephemeral", "--ignore-user-config", "-C", str(cwd), "-o", str(out),
           *(["-c", f'model_reasoning_effort="{effort}"'] if effort else []),
           *(["--output-schema", str(output_schema)] if output_schema else []), prompt]
    env, _ = scrubbed_env(keep=CODEX_AUTH)
    hosts = list(domains or CODEX_DOMAINS)
    seen = {"allowed": set(), "denied": set()}
    for attempt in range(CODEX_RETRIES + 1):
        if confined:
            with isolation.Sandboxed(policy, True, tmp_root) as box, proxy.AllowlistProxy(hosts) as px:
                run_env = {**env, **box.env(), **px.env(), "CODEX_HOME": str(home)}
                res = _spawn(box.argv(cmd), cwd, log, timeout_s, run_env)
            seen["allowed"] |= px.allowed
            seen["denied"] |= px.denied
        else:
            res = _spawn(cmd, cwd, log, timeout_s, env)
        text = log.read_text(errors="replace")
        # A rate limit (HTTP 429) or a model at capacity is transient; retry with backoff. A usage limit ("try again
        # at ...") is not, and fails.
        transient = "429 Too Many Requests" in text or "model is at capacity" in text
        if res["exit"] == 0 or not transient or "usage limit" in text or attempt == CODEX_RETRIES:
            break
        time.sleep(CODEX_BACKOFF_S * (attempt + 1))
    res.update(family="codex", log_path=log, cmd=shlex.join("<prompt>" if c == prompt else c for c in cmd),
               attempts=attempt + 1, sandbox="sandbox-exec" if confined else "off" if read is not None else "codex")
    if confined:
        res["confinement"] = {"read_roots": sorted(set(policy.readable)), "write": policy.writable,
                              "proxy_hosts": hosts, "proxy_allowed": sorted(seen["allowed"]),
                              "proxy_denied": sorted(seen["denied"])}
    tokens = re.search(r"tokens used\s*\n?\s*([\d,]+)", text, re.I)
    used = re.search(r"^model:\s*(\S+)", text, re.M)
    result = out.read_text() if out.exists() else ""
    res.update(tokens=int(tokens.group(1).replace(",", "")) if tokens else None,
               model=used.group(1) if used else (model or "Codex default model"),
               result=result, output_sha256=hashlib.sha256(result.encode()).hexdigest())
    res["ok"] = res["exit"] == 0 and bool(result.strip())
    if not res["ok"] and "error" not in res:
        res["error"] = f"codex exited {res['exit']}" if res["exit"] else "codex wrote no final message"
    return res


def codex_home(root: Path) -> Path:
    """A Codex home holding only the sign-in, so Codex reads no personal config, instructions, history or memories
    (`codex review` has no --ignore-user-config; a confined `codex exec` can't read ~/.codex). The sign-in is linked,
    never copied."""
    home = root / "codex-home"
    home.mkdir(parents=True, exist_ok=True)
    auth = codex_auth_file()
    if auth.exists() and not (home / "auth.json").exists():
        (home / "auth.json").symlink_to(auth)
    return home


def run_codex_review(repo: Path, log: Path, *, base: str, title: str, model: str | None, timeout_s: int,
                     home: Path, effort: str | None = None) -> dict:
    """OpenAI's own review command, `codex review --base`, on a repository whose `base` branch is where the change
    started and whose HEAD is where it ends. Its review is the stdout (the `result`); progress goes beside it."""
    binary = codex_bin()
    if not binary:
        return {"ok": False, "family": "codex", "cmd": "codex review", "error": "Codex CLI not found (set CODEX_BIN)",
                "started": now(), "finished": now(), "duration_s": 0, "log_path": None}
    cmd = [binary, "review", "--base", base, "--title", title[:200], *(["-c", f'model="{model}"'] if model else []),
           *(["-c", f'model_reasoning_effort="{effort}"'] if effort else [])]
    env, _ = scrubbed_env(keep=CODEX_AUTH)
    env["CODEX_HOME"] = str(home)
    res = _spawn(cmd, repo, log, timeout_s, env, stderr_log=log.with_suffix(".progress.txt"))
    text = log.read_text(errors="replace")
    progress = log.with_suffix(".progress.txt").read_text(errors="replace") if log.with_suffix(".progress.txt").exists() else ""
    tokens = re.search(r"tokens used\s*\n?\s*([\d,]+)", progress, re.I)
    res.update(family="codex", log_path=log, cmd=shlex.join(cmd), result=text, model=model or "Codex default model",
               tokens=int(tokens.group(1).replace(",", "")) if tokens else None,
               output_sha256=hashlib.sha256(text.encode()).hexdigest())
    if "usage limit" in progress:
        res["error"] = "codex usage limit"
    res["ok"] = res["exit"] == 0 and "error" not in res
    if not res["ok"] and "error" not in res:
        res["error"] = f"codex review exited {res['exit']}"
    return res
