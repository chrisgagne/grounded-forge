#!/usr/bin/env python3
"""Run Pass I of the 9-pass ingestion protocol for one or more sources, end to end.

The orchestrating session used to sequence Pass I by hand: dispatch the
fix-in-place auditor and the blind cross-family auditor, wait, run the sort,
apply its remaining edits, stamp, check the derived tier. Every handback cost a
turn at the orchestrator's full context. This driver runs the same sequence as
code. Each leg is a fresh headless agent (`claude -p` or `codex exec`), so no
leg shares context with the session that wrote the deep reference, and the
orchestrator's part shrinks to launching the driver and reading its summary.

Per source, in order (each step is skipped when its output is already on disk,
so a rerun resumes):

  packet     freeze the deep reference; copy the tape, original, source card,
             the Pass I spec and three calibration fixtures into a work folder
  fixer      fix-in-place audit (the `ingest-auditor` agent), in parallel with
  blind      blind audit by the second leg, on the frozen copy
  sort       the second leg sorts both audits against the source
  apply      a fresh agent verifies and applies the sort's remaining edits and
             brings the light reference and distillations into line
  gate       stops the source for an operator decision unless the apply leg
             reports pass with nothing open
  finalize   copies the second leg's records into `references/_audit/`,
             appends them to the audit log, stamps the deep reference
  fidelity   a fresh agent checks the derived tier against the audited deep
  provenance stamps the derived tier with the deep reference's hash

The second leg should be a different model family from the one that wrote the
deep reference (protocol, Pass I). `--second codex` is the default when the
writer was Claude. A source scoped confidential or personal never goes to the
other family: its second leg runs as a fresh Claude agent and the stamp says
audited-but-unverified. `--second none` skips the second leg, sort and apply,
with the same label.

Usage:
    python3 -m scripts.pass_i.run --corpus corpus.local/my-corpus SLUG [SLUG ...]
    python3 -m scripts.pass_i.run --corpus ... SLUG --dry-run
    python3 -m scripts.pass_i.run --corpus ... SLUG --accept-gate SLUG

Work folders: `_planning/pass-i/{corpus-name}/{slug}/` (gitignored). Each holds
`status.json` (steps, cost, session IDs), every brief sent, and every report.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from string import Template

import yaml

REPO = Path(__file__).resolve().parents[2]
BRIEFS = Path(__file__).parent / "briefs"
PROTOCOL = REPO / ".claude/skills/ingesting-resources/9-pass-protocol.md"
FIXTURES = ["01-training-leakage.md", "07-marker-mismatch-V-without-verbatim.md", "12-clean-negative-control.md"]
CODEX_FALLBACKS = ["/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex"]
UNSHARED_SCOPES = {"confidential", "personal"}
PRINT_LOCK = threading.Lock()


def say(slug: str, msg: str) -> None:
    with PRINT_LOCK:
        print(f"{dt.datetime.now():%H:%M:%S} [{slug}] {msg}", flush=True)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def frontmatter(path: Path) -> dict:
    if not path.exists():
        return {}
    m = re.match(r"---\n(.*?)\n---", path.read_text(), re.S)
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def codex_bin() -> str | None:
    for c in [os.environ.get("CODEX_BIN"), shutil.which("codex"), *CODEX_FALLBACKS]:
        if c and Path(c).exists():
            return c
    return None


def pass_i_spec() -> str:
    text = PROTOCOL.read_text()
    start = text.index("## Pass I: Source-only audit")
    end = text.index("\n---\n", start)
    return text[start:end] + "\n"


class Agent:
    """One headless leg. Returns a dict with ok, cost and session details."""

    def __init__(self, args):
        self.args = args

    def run(self, family: str, prompt: str, cwd: Path, log: Path, out: Path | None = None,
            agent: str | None = None, read_only: bool = False) -> dict:
        if family == "claude":
            cmd = [os.environ.get("CLAUDE_BIN", "claude"), "-p", prompt, "--output-format", "json",
                   "--permission-mode", self.args.permission_mode]
            cmd += ["--agent", agent] if agent else ["--model", self.args.claude_model, "--effort", self.args.effort]
        else:
            cmd = [self.args.codex_bin, "exec", *(["-m", self.args.codex_model] if self.args.codex_model else []),
                   "-s", "read-only" if read_only else "workspace-write",
                   "--skip-git-repo-check", "-C", str(cwd)]
            if out:
                cmd += ["-o", str(out)]
            cmd.append(prompt)
        if self.args.dry_run:
            shown = [c for c in cmd if c != prompt]
            return {"ok": True, "dry_run": " ".join(shown[:8]) + f" … (cwd {Source.rel(cwd)})"}
        started = dt.datetime.now()
        err = log.with_suffix(".stderr.txt").open("w") if family == "claude" else subprocess.STDOUT
        with log.open("w") as f:
            p = subprocess.Popen(cmd, cwd=cwd, stdout=f, stderr=err, stdin=subprocess.DEVNULL, start_new_session=True)
            try:
                code = p.wait(timeout=self.args.timeout * 60)
            except subprocess.TimeoutExpired:
                os.killpg(p.pid, signal.SIGTERM)
                p.wait()
                return {"ok": False, "error": f"killed after {self.args.timeout} min", "log": str(log)}
            finally:
                if err is not subprocess.STDOUT:
                    err.close()
        res = {"ok": code == 0, "exit": code, "minutes": round((dt.datetime.now() - started).seconds / 60, 1), "log": str(log)}
        if family == "claude":
            try:
                j = json.loads(log.read_text())
                res.update(cost_usd=j.get("total_cost_usd"), session=j.get("session_id"),
                           turns=j.get("num_turns"),
                           model=max(j.get("modelUsage") or {None: {}}, key=lambda k: (j.get("modelUsage") or {}).get(k, {}).get("costUSD", 0)))
                if out and not out.exists() and j.get("result"):
                    out.write_text(j["result"])
            except (json.JSONDecodeError, OSError):
                pass
        else:
            m = re.search(r"tokens used\s*\n?\s*([\d,]+)", log.read_text(errors="ignore"), re.I)
            res.update(tokens=m.group(1) if m else None, model=self.args.codex_model or "Codex default model")
        return res


class Source:
    def __init__(self, args, slug: str, notes: str):
        self.args, self.slug, self.notes = args, slug, notes
        self.corpus = Path(args.corpus)
        self.root = REPO / self.corpus
        self.deep = self.root / "references" / f"{slug}-deep.md"
        self.light = self.root / "references" / f"{slug}.md"
        self.tape = self.root / "sources/converted" / f"{slug}.md"
        self.card = self.root / "sources/original" / f"{slug}.source.md"
        self.log = self.root / "references/_audit" / f"_ingest_pass_I_{slug}_source_audit.md"
        self.work = REPO / "_planning/pass-i" / self.corpus.name / slug
        self.status_path = self.work / "status.json"
        self.status = json.loads(self.status_path.read_text()) if self.status_path.exists() else {"steps": {}}
        self.lock = threading.Lock()
        meta = frontmatter(self.card)
        self.scope = str(meta.get("scope") or self._deep_field("Scope") or "unknown")
        self.title = str(meta.get("title") or slug)
        self.tape_desc = f"Converted via: {meta['converted_via']}." if meta.get("converted_via") else ""
        self.original = self._find_original(meta.get("checksum_sha256"))
        self.second = args.second
        self.second_reason = ""
        if self.second == "codex" and self.scope in UNSHARED_SCOPES:
            self.second, self.second_reason = "claude", f"scope {self.scope}: kept within the writer's family"
        self.agent = Agent(args)

    def _deep_field(self, name: str) -> str | None:
        m = re.search(rf"^\*\*{name}:\*\*\s*(\S+)", self.deep.read_text(), re.M) if self.deep.exists() else None
        return m.group(1) if m else None

    def _find_original(self, checksum: str | None) -> Path | None:
        if not checksum:
            return None
        for d in ("sources/original", "sources/ingest"):
            for p in sorted((self.root / d).glob("*")):
                if p.is_file() and not p.name.endswith((".source.md", ".md")) and sha256(p) == checksum:
                    return p
        return None

    # bookkeeping ---------------------------------------------------------
    def done(self, step: str) -> bool:
        return self.status["steps"].get(step, {}).get("ok") is True

    def record(self, step: str, result: dict) -> None:
        with self.lock:
            self.status["steps"][step] = {**result, "at": dt.datetime.now().isoformat(timespec="seconds")}
            if not self.args.dry_run:
                self.status_path.write_text(json.dumps(self.status, indent=2))

    def fill(self, brief: str, **extra) -> str:
        values = dict(
            corpus=str(self.corpus), slug=self.slug, title=self.title, scope=self.scope,
            deep=self.rel(self.deep), light=self.rel(self.light), tape=self.rel(self.tape),
            log=self.rel(self.log), packet=self.rel(self.work), render_cap=self.args.render_cap,
            tape_desc=self.tape_desc, notes=f"\n{self.notes}\n" if self.notes else "",
            original_line=f"`{self.rel(self.original)}`" if self.original else "not available; work from the tape",
            deep_lines=self._lines(self.deep), tape_lines=self._lines(self.tape), **extra)
        return Template((BRIEFS / brief).read_text()).safe_substitute(values)

    @staticmethod
    def rel(p: Path) -> str:
        return str(p.relative_to(REPO)) if p.is_absolute() and p.is_relative_to(REPO) else str(p)

    @staticmethod
    def _lines(p: Path) -> int:
        return p.read_text(errors="ignore").count("\n") if p.exists() else 0

    # steps ---------------------------------------------------------------
    def check(self) -> str | None:
        for p in (self.deep, self.tape):
            if not p.exists():
                return f"missing {self.rel(p)}"
        head = self.deep.read_text().split("\n")[:5]
        if any(line.startswith("<!-- Pass I applied") for line in head) and not self.done("finalize"):
            return "deep reference already carries a Pass I stamp; remove it to re-audit"
        return None

    def packet(self) -> dict:
        if self.args.dry_run:
            return {"ok": True}
        self.work.mkdir(parents=True, exist_ok=True)
        shutil.copy(self.deep, self.work / "frozen-deep.md")
        (self.work / "frozen-deep.sha256").write_text(f"{sha256(self.deep)}  frozen-deep.md\n")
        shutil.copy(self.tape, self.work / "tape.md")
        if self.original:
            shutil.copy(self.original, self.work / f"source{self.original.suffix}")
        if self.card.exists():
            shutil.copy(self.card, self.work / "source-card.md")
        (self.work / "pass-i-spec.md").write_text(pass_i_spec())
        (self.work / "fixtures").mkdir(exist_ok=True)
        for f in FIXTURES:
            shutil.copy(REPO / "tests/audit-fixtures" / f, self.work / "fixtures" / f)
        return {"ok": True, "original": self.rel(self.original) if self.original else None,
                "second": self.second, "second_reason": self.second_reason}

    def fixer(self) -> dict:
        if self.second == "none":
            line = "No second leg runs on this source."
        else:
            line = f"A blind second leg ({self.second}) runs in parallel on a frozen copy; don't wait for it."
        prompt = self.fill("fixer.md", second_leg_line=line)
        self.save("fixer-prompt.md", prompt)
        before = self.log.stat().st_mtime if self.log.exists() else 0
        res = self.agent.run("claude", prompt, REPO, self.work / "fixer-log.json", agent="ingest-auditor")
        if not self.args.dry_run and not (self.log.exists() and self.log.stat().st_mtime > before):
            res.update(ok=False, error=f"no audit log written at {self.rel(self.log)}")
        return res

    def blind(self) -> dict:
        prompt = self.fill("blind.md")
        self.save("blind-brief.md", prompt)
        out = self.work / "blind-findings.md"
        res = self.agent.run(self.second, self._legprompt("blind-brief.md", "blind audit", out), self.work,
                             self.work / "blind-log.txt", out=out, read_only=True)
        return self._expect(res, out)

    def sort(self) -> dict:
        if not self.args.dry_run:
            shutil.copy(self.log, self.work / "fixer-audit-log.md")
            shutil.copy(self.deep, self.work / "post-audit-deep.md")
            (self.work / "post-audit-deep.sha256").write_text(f"{sha256(self.deep)}  post-audit-deep.md\n")
        self.save("sort-brief.md", self.fill("sort.md"))
        out = self.work / "sort.md"
        res = self.agent.run(self.second, self._legprompt("sort-brief.md", "sort leg", out), self.work,
                             self.work / "sort-log.txt", out=out, read_only=True)
        return self._expect(res, out)

    def apply(self) -> dict:
        prompt = self.fill("apply.md")
        self.save("apply-prompt.md", prompt)
        res = self.agent.run("claude", prompt, REPO, self.work / "apply-log.json")
        return self._expect(res, self.work / "apply-report.json")

    def gate(self) -> dict:
        if self.second == "none":
            return {"ok": True, "gate": "pass"}
        if self.args.dry_run:
            return {"ok": True}
        report = json.loads((self.work / "apply-report.json").read_text())
        accepted = self.slug in (self.args.accept_gate or [])
        if (report.get("gate") == "pass" and not report.get("open")) or accepted:
            return {"ok": True, "gate": "accepted by operator" if accepted else "pass"}
        lines = [f"# Pass I needs a decision: {self.slug}", "",
                 f"Apply leg gate: **{report.get('gate')}**", "", f"Sort: {report.get('sort_result')}", "",
                 f"Applied: {report.get('applied_note')}", "", "## Open questions", ""]
        lines += [f"- {q}" for q in report.get("open") or ["(none listed; the gate failed)"]]
        lines += ["", "Settle these in the deep reference, then rerun with "
                  f"`--accept-gate {self.slug}` to stamp and finish."]
        self.save("decisions-needed.md", "\n".join(lines) + "\n")
        return {"ok": False, "gate": "needs-decision", "file": self.rel(self.work / "decisions-needed.md")}

    def finalize(self) -> dict:
        if self.args.dry_run:
            return {"ok": True}
        today = dt.date.today().isoformat()
        steps = self.status["steps"]
        fixer_model = steps.get("fixer", {}).get("model") or "Claude"
        report = json.loads((self.work / "apply-report.json").read_text()) if self.second != "none" else {}
        same = report.get("same_family") or "see the audit log"
        aud = self.log.parent
        cross = self.second == "codex"
        if self.second == "none":
            second_stamp = "none (audited-but-unverified)"
        elif cross:
            second_stamp = f"{steps.get('blind', {}).get('model')} blind audit and sort (Codex CLI)"
        else:
            second_stamp = f"fresh {steps.get('blind', {}).get('model') or 'Claude'} blind audit and sort, same family (audited-but-unverified)"
        if self.second != "none":
            tag = "crossfamily" if cross else "secondleg"
            (aud / f"_ingest_pass_I_{self.slug}_{tag}_blind.md").write_text((self.work / "blind-findings.md").read_text())
            (aud / f"_ingest_pass_I_{self.slug}_{tag}_sort.md").write_text((self.work / "sort.md").read_text())
            (aud / f"_ingest_pass_I_{self.slug}_{tag}_prompts.md").write_text(
                f"# Second-leg prompts: {self.slug}\n\n## Blind leg\n\n" + (self.work / "blind-brief.md").read_text()
                + "\n\n## Sort leg\n\n" + (self.work / "sort-brief.md").read_text())
        lines = self.deep.read_text().split("\n")
        pending = re.compile(r"Pass I (has not run|not yet run|hasn't run|is pending|pending)\.?|Pass I\. Not yet run\.?", re.I)
        lines = [pending.sub("Pass I: see the stamp on line 2 and the audit log.", line) for line in lines]
        lines.insert(1, f"<!-- Pass I applied {today} | Fix-in-place leg: fresh {fixer_model} agent, {same} | "
                        f"Second leg: {second_stamp} | Audit log: _audit/{self.log.name} -->")
        self.deep.write_text("\n".join(lines))
        new_sha = sha256(self.deep)
        section = [f"\n\n## Second leg\n"]
        if self.second == "none":
            section.append("No second leg ran. Treat this reference as audited-but-unverified: the protocol asks for a "
                           "blind audit by a different model family before a reference counts as passed.")
        else:
            frozen = (self.work / "frozen-deep.sha256").read_text().split()[0]
            post = (self.work / "post-audit-deep.sha256").read_text().split()[0]
            who = (f"{steps.get('blind', {}).get('model')} via the Codex CLI, read-only sandbox" if cross else
                   f"a fresh Claude agent ({self.second_reason or 'second family not used'}); audited-but-unverified")
            section += [f"**Auditor:** {who}, for both the blind leg and the sort leg.", "",
                        "**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep "
                        f"reference (sha256 `{frozen}`) blind, with the full tape, the original where available and the "
                        "source card. In a separate run it then read both audits and the post-audit deep reference "
                        f"(sha256 `{post}`), checked each finding against the source, and sorted them. Files: "
                        + ", ".join(f"`_ingest_pass_I_{self.slug}_{tag}_{k}.md`" for k in ("blind", "sort", "prompts"))
                        + ".", "",
                        f"**Sort result:** {report.get('sort_result')}", "",
                        f"**Remaining edits applied ({today}):** {report.get('applied_note')}", "",
                        f"**Gate:** {steps.get('gate', {}).get('gate', 'pass')}. Deep reference sha256 `{new_sha}`, stamp included."]
        with self.log.open("a") as f:
            f.write("\n".join(section) + "\n")
        return {"ok": True, "sha256": new_sha}

    def fidelity(self) -> dict:
        derived = [self.light, *(self.root / "distillations").glob(f"*/{self.slug}-*.md")]
        if not any(p.exists() for p in derived):
            return {"ok": True, "skipped": "no derived files"}
        prompt = self.fill("fidelity.md")
        self.save("fidelity-prompt.md", prompt)
        out = self.work / "fidelity-report.md"
        res = self._expect(self.agent.run("claude", prompt, REPO, self.work / "fidelity-log.json"), out)
        if res["ok"] and not self.args.dry_run:
            m = re.search(r"## Summary for the audit log\s*\n(.+)", out.read_text(), re.S)
            summary = m.group(1).strip() if m else "See the fidelity report in the Pass I work folder."
            with self.log.open("a") as f:
                f.write(f"\n## Derived-tier fidelity check ({dt.date.today().isoformat()})\n\n{summary}\n")
        return res

    def provenance(self) -> dict:
        cmd = [sys.executable, "scripts/check_derived_provenance.py", "--root", str(self.root), "--stamp", "--slug", self.slug]
        if self.args.dry_run:
            return {"ok": True}
        r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
        return {"ok": r.returncode == 0, "output": (r.stdout + r.stderr)[-800:]}

    # helpers -------------------------------------------------------------
    def save(self, name: str, text: str) -> None:
        if not self.args.dry_run:
            (self.work / name).write_text(text)

    def _legprompt(self, brief: str, what: str, out: Path) -> str:
        tail = "" if self.second == "codex" else f" Write the complete report to {out.name} in this folder."
        return (f"Read {brief} in this folder in full and carry out the {what} it describes. Work at your highest "
                f"reasoning effort. Your final message is the complete report in the format the brief asks for.{tail}")

    def _expect(self, res: dict, out: Path) -> dict:
        if not self.args.dry_run and res.get("ok") and not (out.exists() and out.stat().st_size > 0):
            res.update(ok=False, error=f"no output at {self.rel(out)}")
        return res

    # sequence ------------------------------------------------------------
    def step(self, name: str, fn) -> bool:
        if self.done(name):
            say(self.slug, f"{name}: already done")
            return True
        say(self.slug, f"{name}: start")
        res = fn()
        self.record(name, res)
        extra = res.get("error") or res.get("gate") or res.get("skipped") or res.get("dry_run") or ""
        cost = f" ${res['cost_usd']:.2f}" if res.get("cost_usd") else ""
        say(self.slug, f"{name}: {'ok' if res.get('ok') else 'STOPPED'}{cost} {extra}".rstrip())
        return bool(res.get("ok"))

    def run(self) -> str:
        problem = self.check()
        if problem:
            say(self.slug, f"not started: {problem}")
            return problem
        if not self.step("packet", self.packet):
            return "packet failed"
        if self.second == "none":
            if not self.step("fixer", self.fixer):
                return "fixer failed"
        else:
            with ThreadPoolExecutor(2) as ex:
                legs = [ex.submit(self.step, "fixer", self.fixer), ex.submit(self.step, "blind", self.blind)]
                if not all(f.result() for f in legs):
                    return "a first-round leg failed"
            for name in ("sort", "apply"):
                if not self.step(name, getattr(self, name)):
                    return f"{name} failed"
        for name in ("gate", "finalize", "fidelity", "provenance"):
            if not self.step(name, getattr(self, name)):
                return f"stopped at {name}"
        return "done"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("slugs", nargs="+")
    ap.add_argument("--corpus", required=True, help="corpus root, e.g. corpus.local/my-corpus")
    ap.add_argument("--second", choices=["codex", "claude", "none"], default="codex",
                    help="model family for the blind and sort legs (default codex)")
    ap.add_argument("--codex-model", default=os.environ.get("PASS_I_CODEX_MODEL"),
                    help="model for Codex legs (env PASS_I_CODEX_MODEL; default: Codex's configured model)")
    ap.add_argument("--claude-model", default="opus", help="model for the apply and fidelity legs")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--permission-mode", default="auto", help="for headless claude legs")
    ap.add_argument("--notes", type=Path, help="YAML mapping slug → notes added to every brief for that source")
    ap.add_argument("--jobs", type=int, default=3, help="sources run at once (each runs two legs at once)")
    ap.add_argument("--timeout", type=int, default=90, help="minutes before a leg is killed")
    ap.add_argument("--render-cap", type=int, default=10, help="page renders allowed per leg")
    ap.add_argument("--accept-gate", nargs="*", metavar="SLUG", help="stamp these sources despite open questions")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.second == "codex":
        args.codex_bin = codex_bin()
        if not args.codex_bin:
            ap.error("--second codex needs the Codex CLI: put `codex` on PATH or set CODEX_BIN")
    notes = yaml.safe_load(args.notes.read_text()) if args.notes else {}
    sources = [Source(args, s, str(notes.get(s, "")).strip()) for s in args.slugs]
    with ThreadPoolExecutor(args.jobs) as ex:
        results = dict(zip(args.slugs, ex.map(lambda s: s.run(), sources)))

    print("\nPass I summary")
    for s in sources:
        steps = s.status["steps"]
        cost = sum(v.get("cost_usd") or 0 for v in steps.values())
        print(f"  {s.slug}: {results[s.slug]} (Claude legs ${cost:.2f}; work folder {s.rel(s.work)})")
    return 0 if all(r == "done" for r in results.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
