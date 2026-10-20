"""OS isolation for everything that runs builder-controlled code.

The PreToolUse guard reads tool calls; it can't see what a script the agent
wrote does when it runs. So the boundary is the operating system:

  - Claude legs run with Claude Code's own sandbox switched on through
    `--settings` (`claude_sandbox`): Bash and every process it starts can write
    only inside the worktree, can't read the secret paths, and reach only the
    allowed network domains (none by default). It fails to start rather than
    run unsandboxed, and the agent can't opt a command out of it.
  - Gate commands, ratchet and rollback commands, release commands and
    builder-command adapters run under macOS `sandbox-exec` (`wrap`) with the
    same policy: writes only inside the folder the command works on and a
    private temp folder, no reads of the secret paths, no network unless the
    config grants it for that check (by default only `install` and adapters).

Both keep the git metadata, the change folder (ledger and evidence) and the
factory's config out of reach. Every process also gets a minimal environment
built from an allowlist, not the operator's environment minus a denylist.

What this does not do: hide the rest of the disk from reads (only the secret
paths are denied), stop local IPC beyond the keychain and Apple events, or
work where `sandbox-exec` can't apply a profile (Linux; a process that is
already sandboxed). There the factory refuses to run builder code unless the
config turns OS isolation off, which the ledger and the pack record.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

SANDBOX_EXEC = "/usr/bin/sandbox-exec"
SYSTEM_CA_FILE = "/etc/ssl/cert.pem"
# Paths no leg or command may read. Home-relative; also used by the guard.
SECRET_PATHS = ("~/.ssh", "~/.aws", "~/.gnupg", "~/.netrc", "~/.claude/secrets", "~/Library/Keychains",
                "~/.npmrc", "~/.pypirc", "~/.docker/config.json", "~/.kube", "~/.config/gh", "~/.git-credentials",
                "~/.config/gcloud", "~/.azure", "~/.codex/auth.json", "~/.claude/.credentials.json")
# Environment names passed through to legs and commands; everything else is dropped.
ENV_ALLOW = ("PATH", "HOME", "USER", "LOGNAME", "SHELL", "LANG", "LANGUAGE", "TERM", "TZ", "COLORTERM", "NO_COLOR",
             "VOLTA_HOME", "NVM_DIR", "NVM_BIN", "PYENV_ROOT", "PNPM_HOME", "CARGO_HOME", "RUSTUP_HOME", "GOPATH",
             "GOROOT", "JAVA_HOME", "HOMEBREW_PREFIX", "HOMEBREW_CELLAR", "HOMEBREW_REPOSITORY", "SSL_CERT_FILE",
             "SSL_CERT_DIR", "NODE_EXTRA_CA_CERTS", "REQUESTS_CA_BUNDLE", "CLAUDE_BIN", "CODEX_BIN", "CODEX_HOME")
ENV_PREFIX_ALLOW = ("LC_",)
DEFAULTS = {"os_sandbox": True, "network": ["install", "adapter"], "allowed_domains": [], "allow_write": [], "env": []}


def expand(p: str | Path) -> str:
    return os.path.realpath(os.path.expanduser(str(p)))


def secret_paths() -> list[str]:
    return [expand(p) for p in SECRET_PATHS]


def minimal_env(keep: tuple[str, ...] = (), extra: dict | None = None) -> tuple[dict, list[str]]:
    """The allowlisted environment plus the named credential variables; returns (env, names dropped)."""
    env, dropped = {}, []
    for k, v in os.environ.items():
        if k in ENV_ALLOW or k in keep or k.startswith(ENV_PREFIX_ALLOW):
            env[k] = v
        else:
            dropped.append(k)
    # The sandbox profile blocks the macOS security service, so TLS libraries that read trust anchors from it start
    # with none: semgrep then dies at startup even with no network use. A CA file lets them start; it grants no network.
    if sys.platform == "darwin" and "SSL_CERT_FILE" not in env and Path(SYSTEM_CA_FILE).exists():
        env["SSL_CERT_FILE"] = SYSTEM_CA_FILE
    env.update(extra or {})
    return env, sorted(dropped)


def git_dirs(worktree: Path) -> list[str]:
    """The worktree's `.git` entry and the repository's shared git directory."""
    out = [expand(Path(worktree) / ".git")]
    r = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], cwd=worktree,
                       capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        out.append(expand(r.stdout.strip()))
    return out


# Above this many denied paths, listing each one passes sandbox-exec's rule size limit and Claude Code's 2 MiB
# settings limit (one project in the v7 replay locked 12,846 test files).
COMPRESS_ABOVE = 1000


def compress(paths: list[str], above: int = COMPRESS_ABOVE) -> list[str]:
    """Up to `above` paths, the list as given. Beyond that, the same set with every folder whose entries are all denied
    named once: it denies nothing more of what exists, but a new file inside such a folder is denied too, where
    normally a new file next to locked tests may be added."""
    if len(paths) <= above:
        return list(paths)
    wanted = {os.path.normpath(p) for p in paths}
    full: dict[str, bool] = {}

    def is_full(d: str) -> bool:
        if d not in full:
            try:
                entries = [os.path.join(d, e) for e in os.listdir(d)]
            except OSError:
                full[d] = False
                return False
            full[d] = bool(entries) and all(
                e in wanted or (os.path.isdir(e) and not os.path.islink(e) and is_full(e)) for e in entries)
        return full[d]

    out = set()
    for p in sorted(wanted, key=len):
        top, d = p, os.path.dirname(p)
        while d and d != os.path.dirname(d) and is_full(d):
            top, d = d, os.path.dirname(d)
        out.add(top)
    return sorted(q for q in out if not any(q.startswith(o + os.sep) for o in out if o != q))


def rules(op: str, filters: list[str], limit: int = 40000) -> list[str]:
    """`(deny op ...)` lines, split so none passes sandbox-exec's 64 KiB limit for one rule."""
    out, chunk, size = [], [], 0
    for f in filters:
        if chunk and size + len(f) > limit:
            out.append(f"(deny {op} " + " ".join(chunk) + ")")
            chunk, size = [], 0
        chunk.append(f)
        size += len(f) + 1
    if chunk:
        out.append(f"(deny {op} " + " ".join(chunk) + ")")
    return out


@dataclass
class Policy:
    """What one sandboxed process may touch."""
    writable: list[str]                    # folders it may write (realpaths)
    deny_write: list[str] = field(default_factory=list)  # carved out of `writable`
    deny_unlink: list[str] = field(default_factory=list)  # folders that may gain files but not be moved or removed
    network: bool = False                  # outbound network; localhost is always allowed
    label: str = ""

    def profile(self, tmp: str) -> str:
        q = lambda p: '"' + p.replace("\\", "\\\\").replace('"', '\\"') + '"'
        allow = " ".join(f"(subpath {q(p)})" for p in [*self.writable, tmp])
        lines = ["(version 1)", "(allow default)",
                 "(deny file-write*)",
                 f"(allow file-write* {allow} (literal \"/dev/null\") (literal \"/dev/zero\") "
                 "(literal \"/dev/dtracehelper\") (regex #\"^/dev/tty\") (regex #\"^/dev/fd/\"))"]
        if self.deny_write:  # later rules win in SBPL
            lines += rules("file-write*", [f"(literal {q(p)}) (subpath {q(p)})" for p in compress(self.deny_write)])
        if self.deny_unlink:  # so a locked file's folder can't be renamed away and replaced
            lines += rules("file-write-unlink", [f"(literal {q(p)})" for p in self.deny_unlink])
        lines.append("(deny file-read* " + " ".join(f"(subpath {q(p)})" for p in secret_paths()) + ")")
        if not self.network:
            # Only loopback: bind and accept locally, connect to localhost. (A broader `(allow network* (local ip
            # "localhost:*"))` also lets outbound connections through, so each operation is named.)
            lines += ["(deny network*)", '(allow network-bind (local ip "localhost:*"))',
                      '(allow network-inbound (local ip "localhost:*"))',
                      '(allow network-outbound (remote ip "localhost:*"))']
        lines += ['(deny mach-lookup (global-name "com.apple.SecurityServer") (global-name "com.apple.securityd"))',
                  "(deny appleevent-send)"]
        return "\n".join(lines) + "\n"


_AVAILABLE: dict[str, tuple[bool, str]] = {}


def available() -> tuple[bool, str]:
    """Whether sandbox-exec can apply a profile here (it can't on Linux, or inside another sandbox)."""
    if "r" in _AVAILABLE:
        return _AVAILABLE["r"]
    if sys.platform != "darwin" or not Path(SANDBOX_EXEC).exists():
        res = (False, f"{SANDBOX_EXEC} is not available on {sys.platform}")
    else:
        p = subprocess.run([SANDBOX_EXEC, "-p", "(version 1)(allow default)", "/usr/bin/true"],
                           capture_output=True, text=True)
        res = (p.returncode == 0, "ok" if p.returncode == 0 else
               f"sandbox-exec could not apply a profile (exit {p.returncode}: {p.stderr.strip()}); "
               "is the factory itself running inside a sandbox?")
    _AVAILABLE["r"] = res
    return res


class Sandboxed:
    """Context manager: a private temp folder plus the argv prefix that confines a command to the policy."""

    def __init__(self, policy: Policy | None, enabled: bool = True, tmp_root: Path | None = None):
        self.policy, self.enabled, self.tmp_root = policy, enabled, tmp_root
        self.tmp: str | None = None
        self.profile_file: str | None = None

    def __enter__(self):
        if self.tmp_root:
            Path(self.tmp_root).mkdir(parents=True, exist_ok=True)
        self.tmp = expand(tempfile.mkdtemp(prefix="factory-run-", dir=self.tmp_root))
        return self

    def __exit__(self, *exc):
        shutil.rmtree(self.tmp, ignore_errors=True)
        if self.profile_file:
            Path(self.profile_file).unlink(missing_ok=True)

    def env(self) -> dict:
        return {"TMPDIR": self.tmp + "/", "TMP": self.tmp, "TEMP": self.tmp}

    def argv(self, cmd: str) -> list[str]:
        if self.policy is None or not self.enabled:
            return ["/bin/bash", "-c", cmd]
        # The profile goes in a file, not on the command line: a project with thousands of locked test files makes it
        # longer than the system's argument limit. The file sits outside every folder the command may write.
        fd, self.profile_file = tempfile.mkstemp(prefix="factory-profile-", suffix=".sb")
        with os.fdopen(fd, "w") as f:
            f.write(self.policy.profile(self.tmp))
        return [SANDBOX_EXEC, "-f", self.profile_file, "/bin/bash", "-c", cmd]


def claude_sandbox(deny_write: list[str], allowed_domains: list[str], deny_read: list[str] = ()) -> dict:
    """Claude Code settings (`sandbox` and `permissions`) for a leg.

    Claude Code's sandbox lets Bash write the working folder and `--add-dir`
    folders; `deny_write` carves out what must stay out of reach. Reads of the
    secret paths are denied to Bash and to the file tools.
    """
    secrets = secret_paths() + list(deny_read)
    deny_write = compress(deny_write)
    return {
        "sandbox": {
            "enabled": True,
            "failIfUnavailable": True,          # exit rather than run Bash unconfined
            "allowUnsandboxedCommands": False,  # the agent can't opt a command out
            "autoAllowBashIfSandboxed": True,
            "excludedCommands": [],
            "filesystem": {"denyWrite": list(deny_write), "denyRead": secrets},
            "network": {"allowedDomains": list(allowed_domains), "strictAllowlist": True,
                        "allowLocalBinding": True},
        },
        "permissions": {
            "deny": [f"Read(/{p}/**)" for p in secrets] + [f"Read(/{p})" for p in secrets]
                    + [f"Edit(/{p}/**)" for p in deny_write] + [f"Edit(/{p})" for p in deny_write],
        },
    }
