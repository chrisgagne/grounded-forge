#!/usr/bin/env python3
"""PreToolUse guard for the factory's tests and build legs.

Claude Code runs this before each matching tool call and passes the call as
JSON on stdin (`tool_name`, `tool_input`, `cwd`, ...). Exit 0 lets the call
run. Exit 2 blocks it, and Claude Code shows the agent the reason written to
stderr. Any error inside the guard also exits 2, logging included: a guard that
fails open is no guard.

The guard is the first line, not the boundary. It reads tool calls; it can't
see what a script the agent wrote does when it runs. The boundary is the OS
sandbox the leg runs in (factory/isolation.py): Claude Code's sandbox for
Claude legs, sandbox-exec for commands. The guard catches the plain attempts
early, with a reason the agent can act on.

What it blocks:

  Edit, Write, MultiEdit, NotebookEdit
    - a locked test file (listed in tests.lock)
    - anything under a protected folder (`.factory/` in the repo and worktree)
    - anything outside the worktree
    - with --allow-only, any path that matches none of those globs (tests leg)
  Read, Grep, Glob and Bash
    - secret paths: `.env*` files, ~/.ssh, ~/.aws, ~/.gnupg, ~/.netrc,
      ~/.claude/secrets, keychains, and any --secret path; file tools are
      checked on the resolved path, so a symlink to a secret is caught
  Bash
    - with --bash-only, every command but those exact ones, compared word by
      word after shell quoting (build leg: the factory check)
    - a write-like command that names a locked file or a protected folder
    - a recursive rm of anything outside the worktree
    - git push, history rewrites, git config changes and inline alias/core
      config, curl|sh, sudo, disk tools, DROP/TRUNCATE, and
      `factory sign|return|accept` (the human's step)

Stdlib only, so it runs under any python the hook command names. The factory
package imports `globmatch` and `read_lock` from here so there is one copy.
"""
from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import json
import os
import re
import shlex
import sys

FILE_EDIT_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}
FILE_READ_TOOLS = {"Read", "Grep", "Glob"}
HOME = os.path.expanduser("~")
# The same list as factory.isolation.SECRET_PATHS (the driver passes it with --secret); this copy is the fallback.
DEFAULT_SECRETS = ("~/.ssh", "~/.aws", "~/.gnupg", "~/.netrc", "~/.claude/secrets", "~/Library/Keychains")

SECRET_PATTERNS = [
    (re.compile(r"(?<![\w.-])\.env[\w.-]*"), ".env files hold secrets"),
    (re.compile(r"(?<![\w-])\.(ssh|aws|gnupg|netrc)(?![\w-])"), "credential folders are off limits"),
    (re.compile(r"\.claude/secrets"), "~/.claude/secrets is off limits"),
    (re.compile(r"Library/Keychains|\bsecurity\s+(find-generic-password|find-internet-password|dump-keychain|export)\b"),
     "keychains are off limits"),
]
SAFE_ENV_SUFFIXES = (".example", ".sample", ".template", ".dist")

GIT = r"\bgit\b(?:\s+(?:-C\s+\S+|-c\s+\S+|--[\w-]+(?:=\S+)?|-\w+))*\s+"
DENY_PATTERNS = [
    (re.compile(GIT + r"push\b"), "git push is not allowed from a factory leg"),
    (re.compile(GIT + r"(rebase|filter-branch|filter-repo|update-ref|replace)\b"), "history rewrites are not allowed"),
    (re.compile(GIT + r"reflog\s+(expire|delete)\b"), "history rewrites are not allowed"),
    (re.compile(GIT + r"reset\b[^;&|\n]*--hard\b"), "git reset --hard is not allowed"),
    (re.compile(GIT + r"commit\b[^;&|\n]*--amend\b"), "amending commits is not allowed"),
    (re.compile(GIT + r"config\b(?![^;&|\n]*\s--(get|get-all|get-regexp|list|show-origin)\b)(?![^;&|\n]*\s-l\b)"),
     "changing git config is not allowed from a factory leg"),
    (re.compile(r"\bgit\b[^;&|\n]*\s-c\s*[\"']?(alias|core|include|includeIf|filter|diff)\."),
     "running git with inline alias, core, include, filter or diff config is not allowed"),
    (re.compile(r"\bGIT_(CONFIG|DIR|WORK_TREE|COMMON_DIR|INDEX_FILE)\w*="), "overriding git's config or directories is not allowed"),
    (re.compile(r"\b(curl|wget)\b[^;&\n]*\|\s*(sudo\s+)?[\w/]*\b(ba|z|da|k|fi)?sh\b"), "piping a download into a shell is not allowed"),
    (re.compile(r"\b(curl|wget)\b[^;&\n]*\|\s*(sudo\s+)?[\w/]*\b(python\d*|node|perl|ruby)\b"), "piping a download into an interpreter is not allowed"),
    (re.compile(r"\b(ba|z)?sh\s+(-c\s+)?[\"']?\$\(\s*(curl|wget)\b|<\(\s*(curl|wget)\b"), "running a download as a script is not allowed"),
    (re.compile(r"\b(sudo|doas)\b"), "sudo is not allowed"),
    (re.compile(r"(?:^|[;&|(\n]|\bxargs)\s*(dd|mkfs(\.\w+)?|diskutil|fdisk|gdisk|sfdisk|parted|newfs\w*|hdiutil|wipefs)\b"),
     "disk tools are not allowed"),
    (re.compile(r"(?i:\bdrop\s+(table|database|schema|view|index|column)\b)|\bTRUNCATE\b|(?i:\btruncate\s+table\b)"),
     "DROP and TRUNCATE are not allowed from a factory leg"),
    (re.compile(r"\bfactory\s+(sign|return|accept)\b"), "signing, returning and accepting are the accountable human's step"),
]
WRITE_VERBS = re.compile(
    r"\b(rm|mv|cp|rsync|tee|truncate|touch|chmod|chown|ln|unlink|shred|patch)\b"
    r"|\b(sed|perl)\b[^;&|\n]*\s-i"
    + "|" + GIT + r"(checkout|restore|rm|mv|reset|stash|apply|am|clean)\b"
    r"|\bfind\b[^;&|\n]*\s-(delete|exec)\b"
    r"|writeFile|write_text|appendFile|\bopen\([^)]*['\"][wa]")
REDIRECT = re.compile(r"(?<![0-9&])>>?\s*(?!&)([^\s;&|<>]+)")
SEGMENT_SPLIT = re.compile(r"\|\||&&|[;|\n]")
TOKEN_SPLIT = re.compile(r"[\s;&|<>()=`'\"]+")


def globmatch(path: str, pattern: str) -> bool:
    """Match a posix relative path against a glob in which ** spans folders."""
    rx, i = "", 0
    while i < len(pattern):
        if pattern.startswith("**/", i):
            rx, i = rx + "(?:.*/)?", i + 3
        elif pattern.startswith("**", i):
            rx, i = rx + ".*", i + 2
        elif pattern[i] == "*":
            rx, i = rx + "[^/]*", i + 1
        elif pattern[i] == "?":
            rx, i = rx + "[^/]", i + 1
        else:
            rx, i = rx + re.escape(pattern[i]), i + 1
    return re.fullmatch(rx, path) is not None


def read_lock_entries(path: str) -> dict[str, tuple[str, str]]:
    """tests.lock lines are `sha256  mode  relative/path` (mode as git writes it: 100644, 100755, 120000 for a
    symlink, whose sha256 is of its target text); lines starting # are comments. An older two-field line
    `sha256  path` reads with mode "?", which never matches a file on disk, so it fails safe."""
    out = {}
    with open(path) as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.split("  ", 2)
            if len(parts) == 3 and re.fullmatch(r"\d{6}|other", parts[1]):
                out[parts[2]] = (parts[0], parts[1])
            else:
                sha, rel = line.split("  ", 1)
                out[rel] = (sha, "?")
    return out


def read_lock(path: str) -> dict[str, str]:
    """{relative path: sha256} from tests.lock."""
    return {rel: sha for rel, (sha, _) in read_lock_entries(path).items()}


def expand(text: str) -> str:
    text = re.sub(r"\$\{HOME\}|\$HOME\b", HOME, text)
    return re.sub(r"(?<![\w/])~(?=/|$|\s)", HOME, text)


def real(base: str, path: str) -> str:
    return os.path.realpath(os.path.join(base, expand(path)))


def inside(path: str, folder: str) -> bool:
    return path == folder or path.startswith(folder.rstrip(os.sep) + os.sep)


class Guard:
    def __init__(self, worktree: str, locked: list[str], protect: list[str], allow_only: list[str],
                 secrets: list[str] | None = None, deny_read: list[str] = (), bash_only: list[str] | None = None):
        self.worktree = os.path.realpath(worktree)
        self.bash_only = bash_only
        self.locked = {os.path.realpath(os.path.join(self.worktree, p)) for p in locked}
        self.protect = [os.path.realpath(p) for p in protect]
        self.allow_only = allow_only
        self.secret_dirs = [os.path.realpath(os.path.expanduser(p)) for p in (secrets or DEFAULT_SECRETS)]
        self.deny_read = [os.path.realpath(os.path.expanduser(p)) for p in deny_read]

    # what a path or token refers to ------------------------------------------
    def is_locked(self, p: str) -> bool:
        return p in self.locked

    def is_protected(self, p: str) -> bool:
        return any(inside(p, d) for d in self.protect)

    def names_guarded(self, text: str, cwd: str) -> str | None:
        """Return a locked or protected path this command text names, if any."""
        for tok in TOKEN_SPLIT.split(text):
            if not tok or tok.startswith("-"):
                continue
            p = real(cwd, tok)
            if self.is_locked(p) or self.is_protected(p):
                return p
            if any(inside(lock, p) for lock in self.locked) or any(inside(d, p) for d in self.protect):
                return p  # a folder that holds locked or protected files
            if any(c in tok for c in "*?[") and any(fnmatch.fnmatch(lock, p) for lock in self.locked):
                return p
        return None

    @staticmethod
    def secret(text: str) -> str | None:
        text = expand(text)
        for rx, why in SECRET_PATTERNS:
            for m in rx.finditer(text):
                if m.group(0).startswith(".env") and m.group(0).endswith(SAFE_ENV_SUFFIXES):
                    continue
                return f"{why} ({m.group(0)})"
        return None

    def secret_path(self, p: str) -> str | None:
        """Why the resolved path p is a secret, if it is."""
        if any(inside(p, d) for d in self.secret_dirs):
            return f"{p} is in a credential folder"
        if any(inside(p, d) for d in self.deny_read):
            return f"{p} is outside what this leg may read"
        name = os.path.basename(p)
        if name.startswith(".env") and not name.endswith(SAFE_ENV_SUFFIXES):
            return f"{p} is a .env file"
        return None

    # decisions ---------------------------------------------------------------
    def decide(self, payload: dict) -> str | None:
        """Return the reason to block this tool call, or None to allow it."""
        tool = payload.get("tool_name", "")
        args = payload.get("tool_input") or {}
        cwd = payload.get("cwd") or self.worktree
        if tool in FILE_EDIT_TOOLS:
            raw = args.get("file_path") or args.get("notebook_path") or ""
            return self.edit(real(cwd, raw), raw)
        if tool in FILE_READ_TOOLS:
            why = self.secret(" ".join(str(v) for v in args.values() if isinstance(v, str)))
            for key in ("file_path", "path", "notebook_path"):  # the file the tool opens, symlinks resolved
                if not why and isinstance(args.get(key), str) and args[key]:
                    why = self.secret_path(real(cwd, args[key]))
            return f"Blocked read: {why}." if why else None
        if tool == "Bash":
            return self.bash(args.get("command", ""), cwd)
        return None

    def edit(self, p: str, raw: str) -> str | None:
        if self.is_locked(p):
            return (f"Blocked: {raw} is a locked test. Locked tests define done for this change; make them "
                    "pass by changing the implementation, not the test.")
        if self.is_protected(p):
            return f"Blocked: {raw} is inside a protected .factory/ folder, which only the factory driver writes."
        if not inside(p, self.worktree):
            return f"Blocked: {raw} is outside the worktree ({self.worktree}). Work only inside the worktree."
        if self.secret(p) or self.secret_path(p):
            return f"Blocked: {raw} looks like a secrets file."
        rel = os.path.relpath(p, self.worktree).replace(os.sep, "/")
        if self.allow_only and not any(globmatch(rel, g) for g in self.allow_only):
            return (f"Blocked: this leg may only write test files matching {self.allow_only}; {rel} is not one. "
                    "Write tests only; the implementation comes in the build stage.")
        return None

    def bash(self, command: str, cwd: str) -> str | None:
        if self.bash_only is not None:
            try:
                words = shlex.split(command)
            except ValueError:
                words = None
            if words and any(words == shlex.split(a) for a in self.bash_only):
                return None
            return ("Blocked command: this leg's shell runs only the factory check, exactly as written: "
                    + "; ".join(self.bash_only) + ". Look at files with Read, Grep and Glob; change them with Edit "
                    "and Write.")
        why = self.secret(command)
        if why:
            return f"Blocked command: {why}."
        for rx, why in DENY_PATTERNS:
            if rx.search(command):
                return f"Blocked command: {why}."
        for seg in SEGMENT_SPLIT.split(command):
            for target in REDIRECT.findall(seg):
                target = target.strip("\"'")
                p = real(cwd, target)
                if self.is_locked(p) or self.is_protected(p):
                    return f"Blocked command: it writes to {target}, which is locked or protected."
            if WRITE_VERBS.search(seg):
                named = self.names_guarded(seg, cwd)
                if named:
                    return (f"Blocked command: it changes or removes {named}, which is (or holds) a locked test or "
                            "a protected .factory/ path. Leave locked tests as they are.")
            why = self.recursive_rm_outside(seg, cwd)
            if why:
                return why
        if re.search(r"\bxargs\b[^;&\n]*\b(rm|mv|cp|chmod|truncate)\b", command) and self.names_guarded(command, cwd):
            return "Blocked command: it feeds a locked or protected path to a write command through xargs."
        return None

    def recursive_rm_outside(self, seg: str, cwd: str) -> str | None:
        try:
            words = shlex.split(seg)
        except ValueError:
            words = seg.split()
        while words and (re.match(r"^\w+=", words[0]) or words[0] in ("command", "env", "nice", "time", "exec")):
            words = words[1:]
        if not words or os.path.basename(words[0]) != "rm":
            return None
        flags = [w for w in words[1:] if w.startswith("-")]
        if not any(f == "--recursive" or (not f.startswith("--") and ("r" in f or "R" in f)) for f in flags):
            return None
        for t in (w for w in words[1:] if not w.startswith("-")):
            t = expand(t)
            if "$" in t:
                return f"Blocked command: recursive rm of {t}, which the guard cannot resolve."
            if not inside(real(cwd, t), self.worktree):
                return f"Blocked command: recursive rm of {t}, which is outside the worktree."
        return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="factory PreToolUse guard")
    ap.add_argument("--worktree", required=True)
    ap.add_argument("--lock", help="tests.lock to protect")
    ap.add_argument("--protect", action="append", default=[], help="folder the leg may not write")
    ap.add_argument("--allow-only", action="append", default=[], help="globs the leg may write (tests leg)")
    ap.add_argument("--log", help="append each block to this JSONL file")
    ap.add_argument("--secret", action="append", default=[], help="a path no tool may read")
    ap.add_argument("--deny-read", action="append", default=[], help="a folder this leg may not read")
    ap.add_argument("--bash-only", action="append", default=None, help="the only shell command this leg may run")
    args = ap.parse_args(argv)  # bad arguments exit 2, which blocks
    payload, reason = {}, None
    try:
        payload = json.loads(sys.stdin.read() or "{}")
        locked = list(read_lock(args.lock)) if args.lock and os.path.exists(args.lock) else []
        reason = Guard(args.worktree, locked, args.protect, args.allow_only, args.secret or None,
                       args.deny_read, args.bash_only).decide(payload)
    except BaseException as e:  # fail closed
        reason = f"factory guard error, blocking to be safe: {type(e).__name__}: {e}"
    if reason is None:
        return 0
    try:  # best effort: a log that can't be written never turns a block into an allow
        if args.log:
            with open(args.log, "a") as f:
                f.write(json.dumps({"at": dt.datetime.now().isoformat(timespec="seconds"),
                                    "tool": payload.get("tool_name") if isinstance(payload, dict) else None,
                                    "input": payload.get("tool_input") if isinstance(payload, dict) else None,
                                    "reason": reason}) + "\n")
    except BaseException:
        pass
    try:
        print(reason, file=sys.stderr)
    except BaseException:
        pass
    return 2


if __name__ == "__main__":
    try:
        code = main()
    except BaseException:  # anything at all, argparse included, blocks
        code = 2
    sys.exit(code if code in (0, 2) else 2)
