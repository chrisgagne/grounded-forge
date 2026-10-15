"""The change folder, its config snapshot and its append-only ledger.

A change lives at `{repo}/.factory/changes/{id}/`. It holds `change.json`
(repo, worktree, baseline commit), `story.md`, a snapshot of the repo's
`.factory/config.yaml` taken when the change was created (so a build can't
loosen its own gates), `ledger.json` and every artefact the stages write.

`ledger.json` is a list of events. Each event carries `prev`, the sha256 of the
event before it, so an edit to any earlier event breaks the chain. On every
append the driver also writes an anchor outside the change folder (in the
repo's git directory: the event count and the sha256 of the last event), and
every read checks the ledger against it, so a truncated ledger, an edited last
event or a rewritten history fails to load. Only the driver writes events;
models write artefacts that the driver files. No leg or command can write the
change folder or the git directory (factory/isolation.py).

What this protects against: a leg or a builder command changing the record,
and accidents. What it doesn't: someone with the operator's own file access,
who can rewrite the ledger and the anchor together. There is no signing key;
a signature records who said they signed, bound to the pack, commit and time.
"""
from __future__ import annotations

import contextlib
import datetime as dt
import fcntl
import hashlib
import json
import os
import re
import subprocess
import tempfile
import threading
from pathlib import Path

import yaml

from factory import isolation, legs
from factory.text import inert
from factory.hooks.guard import globmatch, read_lock

STATUSES = ("pass", "fail", "blocked", "skipped", "info")
WORK_STAGES = ("spec", "triage", "tests", "build", "gate", "review")
# Readiness order for sign-off: each stage's last outcome must be newer than the one before it.
READY_ORDER = ("spec", "tests", "build", "triage", "gate", "review")
# Stages whose evidence describes the built code: their outcome must be at the worktree's current commit and tree.
BOUND_STAGES = ("build", "triage", "gate", "review")
GENESIS = "0" * 64

DEFAULTS = {
    "commands": {},
    "test_globs": [],
    "risk_paths": {},
    "axis_spec": None,
    "axis_index": None,
    "theory_doc": None,
    "builder": {"kind": "claude", "command": None},
    "ratchet": {"semgrep_findings": False, "lint_warnings": None},
    "review": {"claude_model": "opus", "codex_model": "gpt-6.1-sol", "grounding": "seeds"},
    # acceptEdits: file edits in the worktree go through; Bash runs only sandboxed (autoAllowBashIfSandboxed);
    # anything that would need a prompt is denied, since a headless leg has no one to ask.
    "legs": {"claude_model": "opus", "permission_mode": "acceptEdits", "effort": None, "timeout_minutes": 30,
             "setting_sources": "project"},
    "gate": {"timeout_minutes": 15, "semgrep_config": "p/default"},
    "worktree_root": None,
    "isolation": dict(isolation.DEFAULTS),
}


class LedgerError(Exception):
    pass


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(Path(path).read_bytes())


def num(event_id: str) -> int:
    return int(event_id.lstrip("e"))


def canonical(event: dict) -> bytes:
    return json.dumps(event, sort_keys=True, separators=(",", ":")).encode()


class Ledger:
    """An append-only, hash-chained event list, checked against an external anchor on every read and append.

    `anchor` is a file outside the change folder that holds the event count and the hash of the last event.
    A ledger without an anchor (a bare Ledger in a test) checks only its chain."""

    def __init__(self, path: Path, anchor: Path | None = None):
        self.path = Path(path)
        self.anchor = Path(anchor) if anchor else None
        self._lock = threading.Lock()

    def _raw(self) -> list[dict]:
        if not self.path.exists():
            return []
        try:
            events = json.loads(self.path.read_text())
        except json.JSONDecodeError as e:
            raise LedgerError(f"{self.path} is not valid JSON: {e}") from e
        if not isinstance(events, list) or not all(isinstance(e, dict) for e in events):
            raise LedgerError(f"{self.path} is not a list of events")
        return events

    def events(self) -> list[dict]:
        """The events, after checking the chain and the anchor."""
        events = self._raw()
        head = self.verify(events)
        self.check_anchor(len(events), head)
        return events

    @staticmethod
    def verify(events: list[dict]) -> str:
        """Check ids and the hash chain; return the hash of the last event (GENESIS when empty)."""
        prev = GENESIS
        for i, e in enumerate(events):
            if e.get("id") != f"e{i + 1:03d}":
                raise LedgerError(f"ledger event {i + 1} has id {e.get('id')!r}; events were removed or reordered")
            if e.get("prev") != prev:
                raise LedgerError(f"ledger event {e['id']} does not chain to the event before it; the ledger was edited")
            prev = sha256_bytes(canonical(e))
        return prev

    def read_anchor(self) -> dict | None:
        if not self.anchor or not self.anchor.exists():
            return None
        try:
            return json.loads(self.anchor.read_text())
        except json.JSONDecodeError as e:
            raise LedgerError(f"the ledger's anchor {self.anchor} is not valid JSON: {e}") from e

    def check_anchor(self, count: int, head: str) -> None:
        if not self.anchor:
            return
        a = self.read_anchor()
        if a is None:
            if count:
                raise LedgerError(f"the ledger has {count} events but its anchor {self.anchor} is missing")
            return
        if a.get("count") != count:
            raise LedgerError(f"the ledger has {count} events but its anchor records {a.get('count')}: events were "
                              "removed or added outside the factory")
        if a.get("head") != head:
            raise LedgerError("the ledger's last event doesn't match the hash its anchor records: the ledger was edited")

    def write_anchor(self, count: int, head: str) -> None:
        if not self.anchor:
            return
        self.anchor.parent.mkdir(parents=True, exist_ok=True)
        atomic_write(self.anchor, json.dumps({"ledger": str(self.path), "count": count, "head": head,
                                              "updated": now()}, indent=1))

    @contextlib.contextmanager
    def locked(self):
        """An interprocess lock on this ledger (and a thread lock, for legs run in parallel)."""
        with self._lock, open(self.path.with_name(self.path.name + ".lock"), "a") as fh:
            fcntl.flock(fh, fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(fh, fcntl.LOCK_UN)

    def append(self, stage: str, status: str, **fields) -> dict:
        if status not in STATUSES:
            raise LedgerError(f"status {status!r} is not one of {STATUSES}")
        if status in ("blocked", "skipped") and not fields.get("reason"):
            raise LedgerError(f"a {status} event needs a reason")
        code = fields.get("exit")
        if code is not None and status in ("pass", "fail") and (status == "pass") != (code == 0):
            raise LedgerError(f"status {status} contradicts exit code {code}")
        with self.locked():
            events = self.events()
            event = {"id": f"e{len(events) + 1:03d}", "stage": stage, "status": status,
                     **{k: v for k, v in fields.items() if v is not None},
                     "recorded": now(), "prev": sha256_bytes(canonical(events[-1])) if events else GENESIS}
            atomic_write(self.path, json.dumps(events + [event], indent=1))
            # A crash between these two writes leaves the ledger one event ahead of its anchor; reads then fail
            # closed and the operator decides.
            self.write_anchor(len(events) + 1, sha256_bytes(canonical(event)))
        return event


def atomic_write(path: Path, text: str) -> None:
    """Write via a unique temp file in the same folder, fsync, then rename over the target."""
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def load_config(repo: Path, commit: str = "HEAD") -> dict:
    """The config as committed at `commit` (the change's baseline), never the working tree's or the change's."""
    r = subprocess.run(["git", *GIT_HARDENING, "show", f"{commit}:.factory/config.yaml"], cwd=repo,
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f".factory/config.yaml is not committed at {commit[:12]} in {repo}: the target repo opts in "
                         "by committing .factory/config.yaml (the factory reads it from the baseline commit, so a "
                         "change can't rewrite its own gates)")
    return merge(DEFAULTS, yaml.safe_load(r.stdout) or {})


def merge(base: dict, over: dict) -> dict:
    out = dict(base)
    for k, v in over.items():
        out[k] = merge(base[k], v) if isinstance(v, dict) and isinstance(base.get(k), dict) else v
    return out


def config_problems(cfg: dict) -> list[str]:
    problems = []
    if not cfg["commands"].get("test"):
        problems.append("commands.test is required")
    if not cfg["test_globs"]:
        problems.append("test_globs is required (the files that get locked)")
    if cfg["builder"].get("kind") not in ("claude", "command"):
        problems.append("builder.kind must be claude or command")
    if cfg["builder"].get("kind") == "command" and not cfg["builder"].get("command"):
        problems.append("builder.kind: command needs builder.command")
    if cfg["review"].get("grounding") not in ("none", "seeds", "distillations"):
        problems.append("review.grounding must be none, seeds or distillations")
    if cfg["review"].get("grounding") == "distillations" and not cfg.get("axis_index"):
        problems.append("review.grounding: distillations needs axis_index (the axis's distillation index)")
    return problems


# The driver's own git calls never run repository hooks or an fsmonitor command, whatever the config says.
GIT_HARDENING = ("-c", "core.hooksPath=/dev/null", "-c", "core.fsmonitor=false", "-c", "user.name=factory",
                 "-c", "user.email=factory@localhost")


def git(cwd: Path, *args: str, check: bool = True) -> str:
    r = subprocess.run(["git", *GIT_HARDENING, *args], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed in {cwd}: {r.stderr.strip()}")
    return r.stdout.strip()


def anchor_path(repo: Path, change_id: str) -> Path:
    """Where a change's ledger anchor lives: the repo's git directory, which no leg or command can write."""
    common = Path(git(repo, "rev-parse", "--path-format=absolute", "--git-common-dir"))
    return common / "factory" / "anchors" / f"{change_id}.json"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:32].strip("-") or "change"


def pin_rules(repo: Path, baseline: str, cfg: dict, cdir: Path) -> dict:
    """A semgrep ruleset named by a path in the repo is copied out of the baseline commit, so the change can't
    rewrite the rules that judge it."""
    rules = (cfg.get("gate") or {}).get("semgrep_config")
    if not rules or rules == "auto" or rules.startswith(("p/", "r/", "s/", "http://", "https://")) or Path(rules).is_absolute():
        return cfg
    r = subprocess.run(["git", *GIT_HARDENING, "archive", baseline, rules], cwd=repo, capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"gate.semgrep_config {rules!r} is not committed at the baseline {baseline[:12]}")
    dest = cdir / "baseline-rules"
    dest.mkdir(parents=True, exist_ok=True)
    subprocess.run(["tar", "-x", "-C", str(dest)], input=r.stdout, check=True)
    return merge(cfg, {"gate": {"semgrep_config": str(dest / rules)}})


class Change:
    def __init__(self, repo: Path, change_id: str, check: bool = True):
        self.repo = Path(repo).resolve()
        self.id = change_id
        self.dir = self.repo / ".factory" / "changes" / change_id
        if not (self.dir / "change.json").exists():
            raise SystemExit(f"no change {change_id} in {self.repo}/.factory/changes")
        self.meta = json.loads((self.dir / "change.json").read_text())
        self.config = merge(DEFAULTS, yaml.safe_load((self.dir / "config.yaml").read_text()) or {})
        self.ledger = Ledger(self.dir / "ledger.json", anchor_path(self.repo, change_id))
        self.worktree = Path(self.meta["worktree"])
        self.baseline = self.meta["baseline"]
        if check:
            self.check_frozen()

    def check_frozen(self) -> None:
        """The config snapshot, story and change.json must be as the change's first event recorded them."""
        events = self.ledger.events()
        first = events[0] if events else {}
        for rel, sha in (first.get("artefacts") or {}).items():
            if not (self.dir / rel).exists() or sha256_file(self.dir / rel) != sha:
                raise LedgerError(f"{rel} changed after change {self.id} was created (event {first.get('id')})")

    # creating ------------------------------------------------------------------
    @classmethod
    def create(cls, repo: Path, story: Path, change_id: str | None = None, overrides: dict | None = None) -> Change:
        repo = Path(repo).resolve()
        baseline = git(repo, "rev-parse", "HEAD")
        cfg = merge(load_config(repo, baseline), overrides or {})
        problems = config_problems(cfg)
        if problems:
            raise SystemExit("config problems in .factory/config.yaml:\n  " + "\n  ".join(problems))
        story_text = Path(story).read_text()
        title = next((ln.lstrip("# ").strip() for ln in story_text.splitlines() if ln.strip()), "change")
        change_id = change_id or f"{dt.datetime.now():%Y%m%d-%H%M%S}-{slugify(title)}"
        cdir = repo / ".factory" / "changes" / change_id
        if cdir.exists():
            raise SystemExit(f"change {change_id} already exists")
        root = Path(cfg["worktree_root"]) if cfg["worktree_root"] else repo.parent / ".factory-worktrees" / repo.name
        worktree = (root / change_id).resolve()
        if worktree == repo or repo in worktree.parents:
            raise SystemExit(f"worktree_root puts the worktree inside the repo ({worktree}); the change folder and git "
                             "metadata must stay outside what legs can write")
        exclude = Path(git(repo, "rev-parse", "--git-common-dir"))
        exclude = (exclude if exclude.is_absolute() else repo / exclude) / "info" / "exclude"
        exclude.parent.mkdir(parents=True, exist_ok=True)
        lines = exclude.read_text().splitlines() if exclude.exists() else []
        for pattern in (".factory/changes/", ".claude/settings.local.json"):
            if pattern not in lines:
                lines.append(pattern)
        exclude.write_text("\n".join(lines) + "\n")
        anchor = anchor_path(repo, change_id)
        if anchor.exists():  # left by a change folder the operator removed; keep it, out of the way
            anchor.rename(anchor.with_name(f"{anchor.name}.superseded-{dt.datetime.now():%Y%m%d-%H%M%S}"))
        cdir.mkdir(parents=True)
        worktree.parent.mkdir(parents=True, exist_ok=True)
        git(repo, "worktree", "add", "-b", f"factory/{change_id}", str(worktree), baseline)
        (cdir / "story.md").write_text(story_text)
        cfg = pin_rules(repo, baseline, cfg, cdir)
        (cdir / "config.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False))
        (cdir / "change.json").write_text(json.dumps(
            {"id": change_id, "repo": str(repo), "worktree": str(worktree), "baseline": baseline,
             "branch": f"factory/{change_id}", "title": title, "created": now()}, indent=1))
        change = cls(repo, change_id, check=False)
        change.ledger.append("new", "info", note=f"change created from {Path(story).name}", baseline=baseline,
                             worktree=str(worktree), config_from=f"{baseline}:.factory/config.yaml",
                             artefacts=change.hashes("story.md", "config.yaml", "change.json"))
        return change

    @contextlib.contextmanager
    def exclusive(self):
        """Hold the change for one command: a second factory process on the same change fails at once."""
        with open(self.dir / ".run.lock", "a") as fh:
            try:
                fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise SystemExit(f"another factory process is working on change {self.id}; wait for it to finish")
            try:
                yield self
            finally:
                fcntl.flock(fh, fcntl.LOCK_UN)

    # paths and git ---------------------------------------------------------------
    def path(self, rel: str) -> Path:
        p = self.dir / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        return p

    def rel(self, p: Path) -> str:
        return str(Path(p).relative_to(self.dir))

    def hashes(self, *rels: str) -> dict[str, str]:
        return {r: sha256_file(self.dir / r) for r in rels if (self.dir / r).exists()}

    def git(self, *args: str, check: bool = True) -> str:
        return git(self.worktree, *args, check=check)

    def head(self) -> str:
        return self.git("rev-parse", "HEAD")

    def tree(self) -> str:
        return self.git("rev-parse", "HEAD^{tree}")

    def code_state(self) -> dict:
        """The commit and tree the worktree is at, and whether it has uncommitted changes."""
        return {"commit": self.head(), "tree": self.tree(), "clean": not self.dirty_files()}

    def code_problem(self, recorded: dict, what: str) -> str | None:
        """Why evidence recorded at `recorded` (an event with commit/tree) doesn't describe the code as it is now."""
        if not recorded.get("commit") or not recorded.get("tree"):
            return f"{what} ({recorded.get('id')}) records no commit, so it can't be tied to the code"
        now_ = self.code_state()
        if (recorded["commit"], recorded["tree"]) != (now_["commit"], now_["tree"]):
            return (f"{what} ({recorded.get('id')}) ran on commit {recorded['commit'][:12]}, but the worktree is at "
                    f"{now_['commit'][:12]}; re-run it")
        if not now_["clean"]:
            return f"the worktree has uncommitted changes, which no evidence covers"
        if recorded.get("clean") is False:
            return f"{what} ({recorded.get('id')}) ran on a worktree with uncommitted changes"
        return None

    def diff(self) -> str:
        return self.git("diff", f"{self.baseline}..HEAD")

    def git_z(self, *args: str) -> list[str]:
        """A git listing run with -z: paths exactly as stored, whatever characters they hold."""
        r = subprocess.run(["git", *GIT_HARDENING, *args, "-z"], cwd=self.worktree, capture_output=True)
        if r.returncode != 0:
            raise RuntimeError(f"git {' '.join(args)} failed in {self.worktree}: {r.stderr.decode(errors='replace')}")
        return [p.decode("utf-8", "surrogateescape") for p in r.stdout.split(b"\0") if p]

    def changed_files(self, since: str | None = None) -> list[str]:
        return self.git_z("diff", "--name-only", "--no-renames", f"{since or self.baseline}..HEAD")

    def dirty_files(self) -> list[str]:
        out, entries = [], self.git_z("status", "--porcelain=v1", "--untracked-files=all", "--no-renames")
        for e in entries:
            out.append(e[3:])
        return out

    def commit_all(self, message: str) -> bool:
        if not self.dirty_files():
            return False
        self.git("add", "-A")
        self.git("commit", "-q", "--no-verify", "-m", message)
        return True

    def test_files(self) -> list[str]:
        """Every file (or symlink) in the worktree that matches test_globs, tracked or not."""
        tracked = self.git_z("ls-files")
        untracked = self.git_z("ls-files", "--others", "--exclude-standard")
        return sorted(f for f in set(tracked + untracked)
                      if os.path.lexists(self.worktree / f) and not (self.worktree / f).is_dir()
                      and any(globmatch(f, g) for g in self.config["test_globs"]))

    def timeout(self, kind: str = "legs") -> int:
        return max(1, int(float(self.config[kind]["timeout_minutes"]) * 60))

    # isolation -------------------------------------------------------------------
    def protected(self, cwd: Path | None = None) -> list[str]:
        """Paths no leg or command may write: git metadata, the change folder, the factory config, Claude settings."""
        wt = self.worktree
        paths = isolation.git_dirs(cwd or wt) + isolation.git_dirs(wt) + [
            isolation.expand(p) for p in (self.repo / ".factory", self.dir, wt / ".factory",
                                          wt / ".claude" / "settings.json", wt / ".claude" / "settings.local.json")]
        return list(dict.fromkeys(paths))

    def locked_paths(self, cwd: Path | None = None) -> tuple[list[str], list[str]]:
        """Locked test files under `cwd` (default: the worktree), and the folders that hold them."""
        lock = self.dir / "tests.lock"
        if not lock.exists():
            return [], []
        base = Path(isolation.expand(cwd or self.worktree))
        files = [str(base / rel) for rel in read_lock(lock)]
        folders = {str(base / parent) for rel in read_lock(lock) for parent in Path(rel).parents if str(parent) != "."}
        return files, sorted(folders)

    def policy(self, check: str, cwd: Path | None = None, writable: bool = True) -> isolation.Policy:
        """The sandbox for a command that runs builder-controlled code in `cwd` (default: the worktree).

        Locked test files can't be written, replaced or moved (nor their folders), so a test script can't weaken a
        locked test, run, and put it back."""
        iso = self.config["isolation"]
        cwd = Path(cwd or self.worktree)
        extra = [isolation.expand(p) for p in iso.get("allow_write") or []]
        locked, folders = self.locked_paths(cwd)
        return isolation.Policy(writable=([isolation.expand(cwd)] if writable else []) + extra,
                                deny_write=self.protected(cwd) + locked, deny_unlink=folders,
                                network=check in (iso.get("network") or []), label=check)

    def tmpdir(self, prefix: str) -> Path:
        """A scratch folder for the driver, beside the worktrees: outside every leg's and command's write access
        (Claude Code's per-user temp folder, /tmp/claude-UID, is writable by every Claude leg, so nothing goes there)."""
        root = self.worktree.parent / ".factory-tmp"
        root.mkdir(parents=True, exist_ok=True)
        return Path(tempfile.mkdtemp(prefix=prefix, dir=root))

    def os_sandbox(self) -> bool:
        return bool(self.config["isolation"].get("os_sandbox", True))

    # ledger helpers --------------------------------------------------------------
    def record(self, stage: str, status: str, **fields) -> dict:
        return self.ledger.append(stage, status, **fields)

    def start(self, stage: str) -> dict:
        """Open a stage run, recording the code it starts from."""
        return self.record(stage, "info", check="start", **self.code_state())

    def run_check(self, stage: str, check: str, cmd: str, cwd: Path | None = None,
                  skip_exits: dict[int, str] | None = None, trusted: bool = False) -> dict:
        """Run a command and record it: exit 0 passes, an exit named in skip_exits is skipped with that reason,
        anything else fails. Builder-controlled commands run sandboxed; `trusted` is for the factory's own scanners."""
        log = self.path(f"{stage}/{check}.log")
        started = now()
        res = legs.run_command(cmd, cwd or self.worktree, log, self.timeout("gate"),
                               policy=None if trusted else self.policy(check, cwd), os_sandbox=self.os_sandbox(),
                               env_names=tuple(self.config["isolation"].get("env") or ()),
                               tmp_root=self.worktree.parent / ".factory-tmp")
        skip = (skip_exits or {}).get(res["exit"])
        status = "pass" if res["exit"] == 0 else "skipped" if skip else "fail"
        return self.record(stage, status, check=check, cmd=cmd, exit=res["exit"],
                           started=started, finished=now(), duration_s=res["duration_s"],
                           output_tail=res["output_tail"], output_sha256=res["output_sha256"], sandbox=res.get("sandbox"),
                           evidence=[self.rel(log)], artefacts=self.hashes(self.rel(log)), reason=skip or res.get("error"))

    def record_leg(self, stage: str, name: str, res: dict, prompt_file: Path | None) -> dict:
        """Record a leg. `output_sha256` hashes its final message; `artefacts` hashes the brief and transcript files,
        which the pack re-checks."""
        files = [p for p in (prompt_file, res.get("log_path"), Path(res["log_path"]).with_suffix(".stderr.txt")
                             if res.get("log_path") else None) if p and Path(p).exists() and self.dir in Path(p).parents]
        evidence = [self.rel(p) for p in files]
        return self.record(stage, "pass" if res["ok"] else "fail", check=f"leg:{name}", leg=name,
                           family=res["family"], cmd=res["cmd"], exit=res.get("exit"), model=res.get("model"),
                           cost_usd=res.get("cost_usd"), tokens=res.get("tokens"), turns=res.get("turns"),
                           started=res["started"], finished=res["finished"], duration_s=res["duration_s"],
                           prompt_sha256=sha256_file(prompt_file) if prompt_file and prompt_file.exists() else None,
                           output_sha256=res.get("output_sha256"), evidence=evidence,
                           artefacts=self.hashes(*evidence), reason=res.get("error"))

    def last_run(self, stage: str) -> list[dict]:
        """Events of the latest run of a stage: everything after its last start event."""
        events = [e for e in self.ledger.events() if e["stage"] == stage]
        starts = [i for i, e in enumerate(events) if e.get("check") == "start"]
        return events[starts[-1]:] if starts else []

    def outcome(self, stage: str) -> dict | None:
        found = [e for e in self.ledger.events() if e["stage"] == stage and e.get("check") == "outcome"]
        return found[-1] if found else None

    def accepted(self, after_id: str) -> dict[str, dict]:
        """Items the human accepted after the given event, keyed by item."""
        return {e["item"]: e for e in self.ledger.events() if e["stage"] == "accept" and num(e["id"]) > num(after_id)}

    def last_start(self, stage: str) -> dict | None:
        found = [e for e in self.ledger.events() if e["stage"] == stage and e.get("check") == "start"]
        return found[-1] if found else None

    def stage_ready(self, stage: str) -> tuple[bool, str]:
        out = self.outcome(stage)
        if not out:
            return False, f"{stage} has not run"
        started = self.last_start(stage)
        if started and num(started["id"]) > num(out["id"]):
            return False, f"a {stage} run started ({started['id']}) and never finished; re-run it"
        i = READY_ORDER.index(stage)
        if i > 0:
            before = self.outcome(READY_ORDER[i - 1])
            if before and num(before["id"]) > num(out["id"]):
                return False, f"{stage} ran before the latest {READY_ORDER[i - 1]}; re-run it"
        returned = self.outcome("return")
        if stage in ("spec", "tests", "build") and returned and num(returned["id"]) > num(out["id"]):
            # A send-back goes through spec and tests before the rebuild, so what it asks for gets locked tests.
            return False, f"the pack was returned ({returned['id']}) after the last {stage}; re-run {stage}"
        if stage in BOUND_STAGES:
            problem = self.code_problem(out, f"the latest {stage}")
            if problem:
                return False, problem
        if out["status"] == "pass":
            return True, "pass"
        blocking = out.get("blocking") or []
        if out["status"] == "blocked" and out.get("acceptable") and blocking:
            missing = [b for b in blocking if b not in self.accepted(out["id"])]
            if not missing:
                return True, "blocked items accepted by the human"
            return False, f"{stage} blocked on {', '.join(missing)} (accept or resolve)"
        return False, f"{stage} {out['status']}: {out.get('reason', '')}".strip()

    def finish(self, stage: str, reasons: list[str], unblock: list[str] | None = None,
               blocking: list[str] | None = None, acceptable: bool = False, **fields) -> bool:
        """Close a stage run. No reasons means pass; otherwise blocked, with decisions-needed.md written."""
        decisions = self.dir / "decisions-needed.md"
        fields = {**self.code_state(), **fields}  # every outcome records the code it describes
        started = self.last_start(stage)
        if started and started.get("commit") and (started["commit"], started.get("tree")) != (fields["commit"], fields["tree"]) \
                and stage in ("triage", "gate", "review"):
            reasons = list(reasons) + [f"the code changed while {stage} ran (from {started['commit'][:12]} to "
                                       f"{fields['commit'][:12]}); re-run it"]
        if not reasons:
            self.record(stage, "pass", check="outcome", **fields)
            if decisions.exists() and decisions.read_text().startswith(f"<!-- stage: {stage} "):
                decisions.unlink()
            return True
        ev = self.record(stage, "blocked", check="outcome", reason="; ".join(reasons), blocking=blocking or None,
                         acceptable=acceptable or None, **fields)
        lines = [f"<!-- stage: {stage} event: {ev['id']} -->", f"# Decisions needed: {self.id}", "",
                 f"**Blocked at {stage}** (ledger event {ev['id']}).", "", "## What blocked", ""]
        lines += [f"- {inert(r)}" for r in reasons]
        lines += ["", "## What would unblock it", ""] + [f"- {u}" for u in (unblock or ["Fix the cause and re-run the stage."])]
        lines += ["", f"Evidence: `{self.dir}/ledger.json` and the files it names.", ""]
        decisions.write_text("\n".join(lines))
        return False
