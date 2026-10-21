"""Stage 6, review: blind read-only reviewer legs, then a Claude sort leg.

`review.legs` names the reviewers (default `[claude, codex]`): `claude` and `codex` get the factory's brief and its
grounding; `claude-plain` is Claude Code given only a plain review prompt; `codex-review` is OpenAI's own `codex
review` command. The two vendor-native legs review the way their makers built them to, so they find different things
from the factory's brief (v5 diagnosis: `calibration/realbugs/results/`).

Each reviewer works in its own export of the change's head (from `git archive`,
with agent instruction and settings files removed: `.claude/`, `CLAUDE.md`,
`AGENTS.md`, `.mcp.json`, `.codex/`), never in the builder-writable worktree,
and gets its own packet: the diff against baseline, acceptance.md, risk.json,
the theory doc if configured and, with `grounding: seeds` or
`grounding: distillations`, the axis rows in play. With distillations the
packet also carries the distillation files those rows cite; they are hashed
into the ledger but not kept in the change folder, since most are
paraphrases of copyrighted books licensed for the operator's own use. Neither sees the builder's summary, the change folder or the other's
packet, findings or live transcript; transcripts reach the change folder only
after both finish. The sort leg sees both lists.

The driver, not a model, decides what blocks, and fails closed: a reviewer's
final message must be exactly a JSON array of valid findings (an invalid item,
or prose around the array, blocks); the sort must account for every finding
exactly once with a valid verdict and a reason (anything less blocks). The
result is numbered F1.., and confirmed critical or high findings block.

What the driver can't decide: whether text in the code under review steered a
model reviewer. The briefs tell the reviewers to treat everything they read as
data; that a model complies stays a residual risk.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from factory import axis, isolation, legs
from factory.ledger import GIT_HARDENING, sha256_file
from factory.stages import brief, settings_file

SEVERITIES = ("critical", "high", "medium", "low")
VERDICTS = ("confirmed", "disputed", "noise")
BLOCKING = ("critical", "high")
# Each reviewer leg and the prefix of its finding IDs.
LEG_PREFIX = {"claude": "C", "codex": "X", "claude-plain": "P", "codex-review": "R"}
DEFAULT_LEGS = ("claude", "codex")
# `codex review` marks each finding P0 to P3.
CODEX_PRIORITY = {"0": "critical", "1": "high", "2": "medium", "3": "low"}
# Triage classes where a confirmed medium blocks too: a medium there loses or exposes someone's data (the first real
# runs' mediums were a retried delete erasing a newer note and a down migration dropping every phone number). The
# sources set no severity bar; this one is PROPOSED, for the operator to confirm.
LOWER_BAR = ("personal-data", "irreversible")
# The packet subfolder holding the distillations a distillations-grounded review may open.
DISTILLATIONS = "distillations"
# Files that instruct or configure an agent working in a folder; reviewers never see the builder's versions.
AGENT_FILES = (".claude", "CLAUDE.md", "CLAUDE.local.md", "AGENTS.md", ".mcp.json", ".codex", ".cursorrules",
               ".cursor", ".github/copilot-instructions.md")


def export_head(change, dest: Path) -> list[str]:
    """Write the change's head into dest without agent instruction or settings files; return what was removed."""
    r = subprocess.run(["git", *GIT_HARDENING, "archive", "--format=tar", "HEAD"], cwd=change.worktree,
                       capture_output=True, check=True)
    subprocess.run(["tar", "-x", "-C", str(dest)], input=r.stdout, check=True)
    return strip_agent_files(dest)


def strip_agent_files(dest: Path) -> list[str]:
    removed = []
    for p in sorted(dest.rglob("*"), key=lambda q: len(q.parts)):
        rel = p.relative_to(dest).as_posix()
        if not p.exists() and not p.is_symlink():
            continue
        if p.name in AGENT_FILES or rel in AGENT_FILES:
            removed.append(rel)
            shutil.rmtree(p) if p.is_dir() and not p.is_symlink() else p.unlink()
    return removed


def build_packet(change, packet: Path, export: Path) -> tuple[list[str] | None, str | None]:
    """Fill a reviewer's packet folder. Returns (axis row ids or None when ungrounded, error)."""
    cfg = change.config
    (packet / "diff.patch").write_text(change.diff())
    for name in ("acceptance.md", "risk.json"):
        src = change.dir / name
        (packet / name).write_text(src.read_text() if src.exists() else f"({name} was not written for this change)\n")
    classes = list(json.loads((packet / "risk.json").read_text()).get("classes", {})) if (change.dir / "risk.json").exists() else []
    theory = cfg.get("theory_doc")
    if theory and (export / theory).exists():
        shutil.copy(export / theory, packet / "theory.md")
        theory_section = (f"The program's theory doc is `{packet}/theory.md` (from `{theory}` at the change's head). Read it. "
                          "Flag, as a finding, any behaviour the diff changes that the theory doc describes but the "
                          "change did not update.")
    elif theory:
        theory_section = f"The config names a theory doc (`{theory}`) but it does not exist at the change's head; say so in a low finding."
    else:
        theory_section = "No theory doc is configured for this repo."
    ids = None
    mode = cfg["review"]["grounding"]
    if mode == "seeds":
        spec = cfg.get("axis_spec")
        if not spec or not Path(spec).exists():
            return None, f"review.grounding is seeds but axis_spec ({spec}) is not readable"
        rows = axis.rows_for_review(axis.load(spec), classes)
        if not rows:
            return None, f"no seed rows found in {spec}"
        ids = [r.id for r in rows]
        (packet / "axis-rows.md").write_text("# Seed trigger→response rows in play\n\n" + "\n".join(r.line() for r in rows) + "\n")
        grounding = (f"Apply the rows in `{packet}/axis-rows.md`. Each is a trigger a practitioner notices and the "
                     "response it calls for. When a finding applies a row, set `axis_row` to its ID (for example "
                     "\"P3.1\"); otherwise leave `axis_row` out. Cite only IDs in that file.")
    elif mode == "distillations":
        index = cfg.get("axis_index")
        if not index or not Path(index).exists():
            return None, f"review.grounding is distillations but axis_index ({index}) is not readable"
        rows = axis.rows_for_review(axis.load_listeners(index), classes)
        if not rows:
            return None, f"no listener rows found in {index}"
        ids = [r.id for r in rows]
        shelf = packet / DISTILLATIONS
        shelf.mkdir()
        for slug in sorted({s for r in rows for s in r.sources}):
            src = axis.distillation_path(index, slug)
            if src.is_file():
                shutil.copy(src, shelf / f"{slug}.md")
        (packet / "axis-rows.md").write_text("# Listener trigger→response rows in play\n\n" + "\n".join(r.line() for r in rows) + "\n")
        grounding = (f"Apply the rows in `{packet}/axis-rows.md`. Each is a trigger a practitioner notices and the "
                     "response the sources call for. Many triggers are about the process around a change (the ledger, "
                     "sign-off, release); apply only those the diff, the packet or the code can show. A backticked slug "
                     f"in a response names a distillation in `{shelf}/{{slug}}.md`: open one when you need to check "
                     "what a row's response rests on, not otherwise. When a finding applies a row, set `axis_row` to its "
                     "ID (for example \"L5.3\"); otherwise leave `axis_row` out. Cite only IDs in that file. A row "
                     "is a reason to look, never evidence: every finding still needs evidence from the code.")
    else:
        grounding = "This review is ungrounded: leave `axis_row` out of every finding."
    (packet / "brief.md").write_text(brief("reviewer.md", packet=packet, worktree=export,
                                           grounding_section=grounding, theory_section=theory_section))
    return ids, None


# Output schemas for the Claude legs. Opus prefaces a final message with a line of progress prose often enough that a
# strict parser blocks reviews that did their job; the CLI's --json-schema holds the final message to the shape
# instead. The schemas only fix the shape: validate_findings and validate_sort still judge every item.
FINDINGS_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["findings"],
    "properties": {"findings": {"type": "array", "items": {
        "type": "object", "required": ["severity", "claim", "evidence"],
        "properties": {"severity": {"type": "string", "enum": list(SEVERITIES)}, "file": {"type": "string"},
                       "line": {"type": "integer"}, "claim": {"type": "string"}, "evidence": {"type": "string"},
                       "axis_row": {"type": "string"}}}}},
}
# The Codex reviewer's schema (`codex exec --output-schema`). OpenAI's strict structured output needs every property
# listed as required and no extra properties, so what's optional for Claude is nullable here.
CODEX_FINDINGS_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["findings"],
    "properties": {"findings": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "required": ["severity", "file", "line", "claim", "evidence", "axis_row"],
        "properties": {"severity": {"type": "string", "enum": list(SEVERITIES)}, "file": {"type": ["string", "null"]},
                       "line": {"type": ["integer", "null"]}, "claim": {"type": "string"},
                       "evidence": {"type": "string"}, "axis_row": {"type": ["string", "null"]}}}}},
}
SORT_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["items"],
    "properties": {"items": {"type": "array", "items": {
        "type": "object", "required": ["sources", "verdict", "reason"],
        "properties": {"sources": {"type": "array", "items": {"type": "string"}},
                       "verdict": {"type": "string", "enum": list(VERDICTS)}, "reason": {"type": "string"},
                       "severity": {"type": "string", "enum": list(SEVERITIES)}, "file": {"type": "string"},
                       "line": {"type": "integer"}, "claim": {"type": "string"}, "breaks": {"type": "string"}}}}},
}


def unwrap(raw, key: str):
    """A schema-held object `{key: [...]}` gives its list; a bare list passes through; anything else is left for the
    validator to reject."""
    if isinstance(raw, dict) and set(raw) == {key}:
        return raw[key]
    return raw


def parse_strict(text: str):
    """The final message must be exactly one JSON value: bare, or as the whole of a single code fence."""
    text = text.strip()
    m = re.fullmatch(r"```[\w-]*\n(.*?)\n?```", text, re.S)
    try:
        return json.loads(m.group(1) if m else text)
    except json.JSONDecodeError as e:
        raise ValueError(f"the final message is not exactly a JSON value ({e.msg}); prose around it isn't accepted")


def validate_findings(raw, row_ids: list[str] | None) -> list[dict]:
    """Every item must be a finding with a known severity, a claim and evidence; any invalid item rejects the list."""
    if not isinstance(raw, list):
        raise ValueError("expected a JSON array of findings")
    kept, bad = [], []
    for i, f in enumerate(raw, 1):
        if not isinstance(f, dict):
            bad.append(f"item {i} is not an object")
            continue
        sev = str(f.get("severity", "")).lower()
        claim, evidence = f.get("claim"), f.get("evidence")
        line = f.get("line")
        problems = [p for p, ok in (
            (f"severity {f.get('severity')!r}", sev in SEVERITIES),
            ("no claim", isinstance(claim, str) and claim.strip()),
            ("no evidence", isinstance(evidence, str) and evidence.strip()),
            (f"line {line!r}", line is None or (isinstance(line, int) and not isinstance(line, bool) and line >= 0)
             or (isinstance(line, str) and line.isdigit())),
            (f"file {f.get('file')!r}", f.get("file") is None or isinstance(f.get("file"), str)),
        ) if not ok]
        if problems:
            bad.append(f"item {i}: {', '.join(problems)}")
            continue
        out = {"severity": sev, "file": f.get("file") or None, "line": int(line) if line is not None else None,
               "claim": claim.strip(), "evidence": evidence.strip()}
        row = f.get("axis_row")
        if row and row_ids is not None:
            out["axis_row" if row in row_ids else "axis_row_unknown"] = row
        kept.append(out)
    if bad:
        raise ValueError("invalid findings, so the review can't be trusted to be complete: " + "; ".join(bad[:5]))
    return kept


def validate_sort(raw, inputs: dict[str, dict]) -> list[dict]:
    """The sort leg's output as the final list. It must put every input finding in exactly one item, each with a
    valid verdict and a reason; otherwise the sort is rejected (ValueError) and the review blocks."""
    if not isinstance(raw, list):
        raise ValueError("expected a JSON array of sorted items")
    items, seen, bad = [], {}, []
    for i, s in enumerate(raw, 1):
        if not isinstance(s, dict):
            bad.append(f"item {i} is not an object")
            continue
        sources = s.get("sources")
        if not isinstance(sources, list) or not sources or not all(isinstance(x, str) for x in sources):
            bad.append(f"item {i} has no sources")
            continue
        unknown = [x for x in sources if x not in inputs]
        if unknown:
            bad.append(f"item {i} names unknown findings {unknown}")
        for x in sources:
            seen.setdefault(x, []).append(i)
        verdict, reason = s.get("verdict"), s.get("reason")
        if verdict not in VERDICTS:
            bad.append(f"item {i} has verdict {verdict!r}")
        if not isinstance(reason, str) or not reason.strip():
            bad.append(f"item {i} gives no reason")
        sev = s.get("severity")
        if sev is not None and str(sev).lower() not in SEVERITIES:
            bad.append(f"item {i} has severity {sev!r}")
        line, typed = s.get("line"), True
        for field, ok in (("file", s.get("file") is None or isinstance(s.get("file"), str)),
                          ("line", line is None or (isinstance(line, int) and not isinstance(line, bool) and line >= 0)),
                          ("claim", s.get("claim") is None or (isinstance(s.get("claim"), str) and s["claim"].strip()))):
            if not ok:
                bad.append(f"item {i} has {field} {s.get(field)!r}")
                typed = False
        if unknown or verdict not in VERDICTS or not isinstance(reason, str) or not reason.strip() or not typed:
            continue
        first = inputs[sources[0]]
        severity = str(sev).lower() if sev is not None else min((inputs[x]["severity"] for x in sources),
                                                                 key=SEVERITIES.index)
        items.append({"sources": sources, "verdict": verdict, "reason": reason.strip(), "severity": severity,
                      "raw_severity": min((inputs[x]["severity"] for x in sources), key=SEVERITIES.index),
                      "file": s.get("file") or first.get("file"), "line": s.get("line") or first.get("line"),
                      "claim": s.get("claim") or first["claim"], "evidence": first["evidence"],
                      **({"breaks": s["breaks"]} if isinstance(s.get("breaks"), str)
                         and re.fullmatch(r"AC-\d+|story", s["breaks"]) else {}),
                      **({"axis_row": first["axis_row"]} if first.get("axis_row") else {}),
                      # every reviewer's own finding stays with the item, so a report can list each one in full
                      "members": [{k: inputs[x].get(k) for k in ("id", "leg", "severity", "file", "line", "claim",
                                                                 "evidence")} for x in sources]})
    twice = sorted(x for x, where in seen.items() if len(where) > 1)
    missing = sorted(x for x in inputs if x not in seen)
    if twice:
        bad.append(f"findings sorted more than once: {', '.join(twice)}")
    if missing:
        bad.append(f"findings the sort didn't account for: {', '.join(missing)}")
    if bad:
        raise ValueError("; ".join(bad[:6]))
    for i, it in enumerate(items, 1):
        it["id"] = f"F{i}"
    return items


def json_items(text: str) -> tuple[list, int]:
    """The objects in a JSON array, read one at a time, so one malformed item costs that item, not the whole review.
    Returns (items, how many couldn't be read); raises ValueError when there's no array at all."""
    if "[" not in text:
        raise ValueError("no JSON array in the final message")
    body = text[text.index("[") + 1:text.rindex("]") if "]" in text else len(text)]
    dec, items, broken, i = json.JSONDecoder(), [], 0, 0
    while True:
        start = body.find("{", i)
        if start < 0:
            return items, broken
        try:
            obj, end = dec.raw_decode(body, start)
            items.append(obj)
            i = end
        except ValueError:
            broken += 1
            nxt = body.find("},", start)
            if nxt < 0:
                return items, broken
            i = nxt + 2


def plain_findings(text: str) -> tuple[list[dict], int]:
    """A plain review's findings ({file, start_line, end_line, severity, message}) in the factory's shape. The message
    is both claim and evidence: a plain review doesn't separate them. Returns (findings, items left out)."""
    items, broken = json_items(text)
    out = []
    for it in items:
        msg = str(it.get("message") or "").strip() if isinstance(it, dict) else ""
        if not msg:
            broken += 1
            continue
        sev = str(it.get("severity") or "").lower()
        line = it.get("start_line")
        out.append({"severity": sev if sev in SEVERITIES else "medium", "file": str(it.get("file") or "") or None,
                    "line": int(line) if isinstance(line, int) or (isinstance(line, str) and line.isdigit()) else None,
                    "claim": msg, "evidence": msg})
    return out, broken


CODEX_REVIEW_ITEM = re.compile(r"^- \[P(\d)\] (.+?) — (.+?):(\d+)(?:-\d+)?\s*$\n((?:^  .*\n?)*)", re.M)


def codex_review_findings(text: str, repo: Path) -> list[dict]:
    """`codex review`'s comments (`- [P1] title — /path/file:12-14` and an indented explanation) in the factory's shape."""
    roots = {str(repo), str(repo.resolve()), str(repo.resolve()).removeprefix("/private")}
    out = []
    for m in CODEX_REVIEW_ITEM.finditer(text):
        path = m.group(3).strip()
        for root in roots:
            if path.startswith(root + "/"):
                path = path[len(root) + 1:]
        body = " ".join(l.strip() for l in m.group(5).splitlines()).strip()
        out.append({"severity": CODEX_PRIORITY.get(m.group(1), "low"), "file": path, "line": int(m.group(4)),
                    "claim": m.group(2).strip(), "evidence": body or m.group(2).strip()})
    return out


def native_repo(change, dest: Path) -> Path:
    """A repository for `codex review`: branch `base` holds the change's baseline and HEAD its head, both without
    agent instruction or settings files, so the diff it reviews is the change and nothing a builder planted."""
    git = lambda *a: subprocess.run(["git", *GIT_HARDENING, *a], cwd=dest, check=True, capture_output=True)
    dest.mkdir(parents=True)
    git("init", "-q", "-b", "change")  # not "head": it clashes with HEAD on a case-insensitive disk
    r = subprocess.run(["git", *GIT_HARDENING, "archive", "--format=tar", change.baseline], cwd=change.worktree,
                       capture_output=True, check=True)
    subprocess.run(["tar", "-x", "-C", str(dest)], input=r.stdout, check=True)
    strip_agent_files(dest)
    git("add", "-A", "-f")
    git("commit", "-q", "--allow-empty", "-m", "base")
    git("branch", "base")
    for p in dest.iterdir():
        if p.name != ".git":
            shutil.rmtree(p) if p.is_dir() and not p.is_symlink() else p.unlink()
    export_head(change, dest)
    git("add", "-A", "-f")
    git("commit", "-q", "--allow-empty", "-m", "change")
    return dest


def show_blocking(change, cfg: dict, items: list[dict], block: list[str], work: Path) -> None:
    """For each blocking item, the reproduction step (factory/reproduce.py): a check the factory runs that fails after
    the change and passed before it, or the reason it can't be run. The outcome goes on the sheet beside the finding;
    it doesn't change what blocks. The signer decides whether a shown change in behaviour is wanted."""
    from factory import reproduce
    trees = work / "reproduce-trees"
    base, head = trees / "base", trees / "head"
    base.mkdir(parents=True)
    r = subprocess.run(["git", *GIT_HARDENING, "archive", "--format=tar", change.baseline], cwd=change.worktree,
                       capture_output=True, check=True)
    subprocess.run(["tar", "-x", "-C", str(base)], input=r.stdout, check=True)
    strip_agent_files(base)
    head.mkdir()
    export_head(change, head)
    setup = cfg.get("reproduce_setup")
    if setup:  # the operator's committed command (installing dependencies, say); it may use the network
        for name, tree in (("base", base), ("head", head)):
            policy = isolation.Policy(writable=[str(tree.resolve())], network=True, label=f"reproduce-setup-{name}")
            res = legs.run_command(setup, tree, change.path(f"review/reproduce-setup-{name}.log"), change.timeout(),
                                   policy=policy, os_sandbox=change.config["isolation"].get("os_sandbox", True))
            change.record("review", "info", check=f"reproduce-setup:{name}", exit=res.get("exit"),
                          evidence=[f"review/reproduce-setup-{name}.log"])
    for it in items:
        if it["id"] not in block:
            continue
        out = reproduce.reproduce(it, base, head, work / "reproduce" / it["id"], model=cfg["claude_model"],
                                  timeout_s=change.timeout("review"))
        check = work / "reproduce" / it["id"] / "check"
        if check.is_dir():
            shutil.copytree(check, change.dir / "review" / "reproduce" / it["id"], dirs_exist_ok=True)
        it["shown"] = {"outcome": out["outcome"], "why": out.get("why"), "head_only": out.get("head_only", False)}
        change.record("review", "info", check=f"reproduce:{it['id']}", outcome=out["outcome"], why=out.get("why"),
                      cost_usd=(out.get("leg") or {}).get("cost_usd"), runs=out.get("runs"))


def bar(classes) -> tuple[str, ...]:
    """The severities that block, for a change in these triage classes."""
    return BLOCKING + ("medium",) if set(classes) & set(LOWER_BAR) else BLOCKING


def overruled(it: dict, sev: tuple[str, ...] = BLOCKING) -> bool:
    """A reviewer rated it at the bar and the sort didn't confirm it at the bar. The sort is a model, so it may not
    lift a block on its own: NIST SP 800-218A, PW.1.1 C2, asks that no AI model sit in the critical path of a
    significant security decision without a human in the loop. A human resolves it with `factory accept`."""
    return it.get("raw_severity") in sev and not (it["verdict"] == "confirmed" and it["severity"] in sev)


def blocking(items: list[dict], sev: tuple[str, ...] = BLOCKING) -> list[str]:
    return [it["id"] for it in items
            if (it["verdict"] == "confirmed" and it["severity"] in sev) or overruled(it, sev)]


def run(change) -> bool:
    change.start("review")
    legs.record_tools(change, "review", ("claude", "codex"))  # every leg kind runs one of these two CLIs
    work = change.tmpdir("review-")
    try:
        return _run(change, change.config["review"], change.config["legs"], work)
    finally:
        shutil.rmtree(work, ignore_errors=True)


def keep(change, src: Path, rel: str) -> Path:
    """Copy a file from a leg's private folder into the change folder."""
    dest = change.path(rel)
    if src.exists():
        shutil.copy(src, dest)
    return dest


def _run(change, cfg: dict, lc: dict, work: Path) -> bool:
    names = list(cfg.get("legs") or DEFAULT_LEGS)
    folders, removed, row_ids = {}, [], None
    for name in [n for n in names if n != "codex-review"] or ["claude"]:  # the packet is built even for a native-only set
        export, packet, logs = (work / name / d for d in ("export", "packet", "logs"))
        for d in (export, packet, logs):
            d.mkdir(parents=True)
        removed = export_head(change, export)
        row_ids, err = build_packet(change, packet, export)
        if err:
            return change.finish("review", [err], ["Fix axis_spec or axis_index in .factory/config.yaml, or set "
                                                  "review.grounding: none."])
        shutil.copytree(packet, change.dir / "review" / f"packet-{name}", dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns(DISTILLATIONS))
        folders[name] = (export, packet, logs)
    if "codex-review" in names:
        (work / "codex-review" / "logs").mkdir(parents=True)
        folders["codex-review"] = (native_repo(change, work / "codex-review" / "repo"), None,
                                   work / "codex-review" / "logs")
    first = next(n for n in folders if folders[n][1] is not None)
    shelf = folders[first][1] / DISTILLATIONS
    change.record("review", "info", check="packet", grounding=cfg["grounding"], axis_rows=len(row_ids) if row_ids else 0,
                  legs=names, theory_doc=change.config.get("theory_doc"), agent_files_removed=removed or None,
                  artefacts=change.hashes(*(f"review/packet-{n}/{f.name}" for n in folders if folders[n][1] is not None
                                            for f in sorted(folders[n][1].iterdir()) if f.is_file())),
                  distillations={f.name: sha256_file(f) for f in sorted(shelf.iterdir())} if shelf.is_dir() else None)
    ask = lambda packet: (f"Read {packet}/brief.md in full and carry out the review it describes. Your final message "
                          "is only the JSON array of findings it asks for.")
    story = change.dir / "story.md"
    story_text = story.read_text() if story.exists() else "(no description)"
    # A Claude reviewer may not read the change folder or the other reviewers' folders. Codex's read-only sandbox can
    # read the whole disk, including the change folder (the builder's summary) and the Claude reviewer's live
    # transcript: a residual risk to its blindness, listed in DESIGN.
    claude_settings = {n: settings_file(change, "review", f"reviewer-{n}",
                                        deny_read=[change.dir, *(work / o for o in folders if o != n)])
                       for n in names if n in ("claude", "claude-plain")}
    if "codex" in folders:
        (folders["codex"][2] / "findings-schema.json").write_text(json.dumps(CODEX_FINDINGS_SCHEMA))
    timeout_s, retries = change.timeout("review"), int(cfg.get("timeout_retries", 0))
    logname = {"claude": "claude-log.jsonl", "codex": "codex-log.txt", "claude-plain": "claude-plain-log.jsonl",
               "codex-review": "codex-review-log.txt"}

    def once(name: str) -> dict:
        export, packet, logs = folders[name]
        if name == "claude":
            return legs.run_claude(ask(packet), export, logs / logname[name], model=cfg["claude_model"],
                                   timeout_s=timeout_s, read_only=True, add_dirs=(packet,),
                                   setting_sources=lc.get("setting_sources"), settings=claude_settings[name],
                                   json_schema=FINDINGS_SCHEMA, effort=cfg.get("claude_effort"))
        if name == "codex":
            return legs.run_codex(ask(packet), export, logs / logname[name], logs / "codex-final.md",
                                  model=cfg.get("codex_model"), timeout_s=timeout_s,
                                  output_schema=logs / "findings-schema.json", effort=cfg.get("codex_effort"))
        if name == "claude-plain":
            prompt = brief("reviewer-plain.md", diff=packet / "diff.patch", story=story_text)
            change.path(f"review/packet-{name}/plain-brief.md").write_text(prompt)
            return legs.run_claude(prompt, export, logs / logname[name], model=cfg["claude_model"],
                                   timeout_s=timeout_s, read_only=True, add_dirs=(packet,),
                                   setting_sources=lc.get("setting_sources"), settings=claude_settings[name],
                                   effort=cfg.get("claude_effort"))
        return legs.run_codex_review(export, logs / logname[name], base="base", title=story_text.splitlines()[0][:200],
                                     model=cfg.get("codex_model"), timeout_s=timeout_s, home=legs.codex_home(work),
                                     effort=cfg.get("codex_effort"))

    def leg(name: str) -> dict:
        """One reviewer, retried when it runs out of time; each earlier attempt's log is kept and listed."""
        earlier = []
        for attempt in range(retries + 1):
            res = once(name)
            if not res.get("timed_out") or attempt == retries:
                res.update(review_attempts=attempt + 1, timed_out_earlier=earlier)
                return res
            earlier.append({"attempt": attempt + 1, "error": res.get("error"),
                            "log": keep(change, folders[name][2] / logname[name],
                                        f"review/{name}-timed-out-{attempt + 1}.log")})

    with ThreadPoolExecutor(len(names)) as ex:
        futures = {n: ex.submit(leg, n) for n in names}
        results = {n: f.result() for n, f in futures.items()}
    inputs, problems = {}, []
    for name, res in results.items():  # the ledger is written from one thread, after every reviewer finishes
        for e in res.get("timed_out_earlier") or []:
            change.record("review", "info", check=f"timed-out:{name}", attempt=e["attempt"], error=e["error"],
                          evidence=[change.rel(e["log"])], retried=True)
    for name in names:
        res = results[name]
        res["log_path"] = keep(change, folders[name][2] / logname[name], f"review/{logname[name]}")
        if name == "codex":
            keep(change, folders[name][2] / "codex-final.md", "review/codex-final.md")
        if name == "codex-review":  # its progress output holds the token count and any usage-limit message
            keep(change, folders[name][2] / "codex-review-log.progress.txt", "review/codex-review-log.progress.txt")
        evidence_brief = change.dir / "review" / f"packet-{name}" / ("plain-brief.md" if name == "claude-plain"
                                                                      else "brief.md")
        change.record_leg("review", f"reviewer-{name}", res, evidence_brief if evidence_brief.exists() else None)
        if not res["ok"]:
            if res.get("timed_out"):
                problems.append(f"the {name} reviewer ran out of time ({res['review_attempts']} attempts of "
                                f"{timeout_s // 60} min) and named no finding")
            else:
                problems.append(f"the {name} review leg failed: {res.get('error')}")
            continue
        unreadable = 0
        try:
            if name in ("claude", "codex"):
                found = validate_findings(unwrap(parse_strict(res["result"]), "findings"), row_ids)
            elif name == "claude-plain":
                found, unreadable = plain_findings(res["result"])
            else:
                found = codex_review_findings(res["result"], folders[name][0])
        except ValueError as e:
            change.record("review", "fail", check=f"findings:{name}", reason=str(e)[:400])
            problems.append(f"the {name} review leg's final message is not a valid findings list: {e}")
            continue
        found = [{"id": f"{LEG_PREFIX[name]}{i}", "leg": name, **f} for i, f in enumerate(found, 1)]
        change.path(f"review/findings-{name}.json").write_text(json.dumps(found, indent=1))
        change.record("review", "info", check=f"findings:{name}", count=len(found), unreadable_items=unreadable or None,
                      artefacts=change.hashes(f"review/findings-{name}.json"))
        inputs.update({f["id"]: f for f in found})
    if problems:
        return change.finish("review", problems, ["Re-run `factory review`; every leg must return a findings list."])
    if inputs:
        sp, sl = work / "sort" / "packet", work / "sort" / "logs"
        sp.mkdir(parents=True)
        sl.mkdir(parents=True)
        fp, fe = folders[first][1], folders[first][0]
        for f in ("diff.patch", "acceptance.md", "risk.json", "theory.md", "axis-rows.md"):
            if (fp / f).exists():
                shutil.copy(fp / f, sp / f)
        for name in names:
            shutil.copy(change.dir / "review" / f"findings-{name}.json", sp / f"findings-{name}.json")
        (sp / "sort-brief.md").write_text(brief("sort.md", packet=sp, worktree=fe))
        shutil.copytree(sp, change.dir / "review" / "packet-sort", dirs_exist_ok=True)
        res = legs.run_claude(f"Read {sp}/sort-brief.md in full and do the sort it describes. Your final message is "
                              "only the JSON array it asks for.", fe, sl / "sort-log.jsonl",
                              model=cfg["claude_model"], timeout_s=change.timeout(), read_only=True, add_dirs=(sp,),
                              setting_sources=lc.get("setting_sources"), json_schema=SORT_SCHEMA,
                              settings=settings_file(change, "review", "sort", deny_read=[change.dir]))
        res["log_path"] = keep(change, sl / "sort-log.jsonl", "review/sort-log.jsonl")
        change.record_leg("review", "sort", res, change.dir / "review" / "packet-sort" / "sort-brief.md")
        if not res["ok"]:
            return change.finish("review", [f"the sort leg failed: {res.get('error')}"], ["Re-run `factory review`."])
        try:
            items = validate_sort(unwrap(parse_strict(res["result"]), "items"), inputs)
        except ValueError as e:
            change.record("review", "fail", check="sort", reason=str(e)[:400])
            return change.finish("review", [f"the sort is incomplete or invalid, so findings could go missing: {e}"],
                                 ["Re-run `factory review`; the sort must account for every finding exactly once."])
    else:
        change.record("review", "skipped", check="leg:sort", reason="neither reviewer reported a finding")
        items = []
    risk = change.dir / "risk.json"
    classes = sorted(json.loads(risk.read_text()).get("classes", {})) if risk.exists() else []
    sev = bar(classes)
    lowered = sorted(set(classes) & set(LOWER_BAR))
    block = blocking(items, sev)
    if cfg.get("reproduce") and block:  # before findings.json is written and hashed: the outcome is part of each item
        show_blocking(change, cfg, items, block, work)
    change.path("review/findings.json").write_text(json.dumps(items, indent=1))
    by_verdict = {v: sum(1 for it in items if it["verdict"] == v) for v in VERDICTS}
    change.record("review", "info", check="sorted", **by_verdict, artefacts=change.hashes("review/findings.json"))
    change.record("review", "info", check="bar", severities=list(sev), classes=lowered or None)
    why = f" (medium blocks: the change reaches {', '.join(lowered)})" if lowered else ""
    reasons = [f"{it['id']} a reviewer rated it {it['raw_severity']}; the sort made it {it['verdict']} {it['severity']}, "
               f"so a human decides{why if it['raw_severity'] not in BLOCKING else ''}: {it['claim']} "
               f"({it.get('file')}:{it.get('line')})" if overruled(it, sev) else
               f"{it['id']} confirmed {it['severity']}{why if it['severity'] not in BLOCKING else ''}: {it['claim']} "
               f"({it.get('file')}:{it.get('line')})"
               + (f" [{it['shown']['outcome']}: {it['shown']['why']}]" if it.get("shown") else "")
               for it in items if it["id"] in block]
    return change.finish("review", reasons, [
        "Resolve: `factory build` (its prompt carries the open findings), then `factory gate` and `factory review`.",
        f"Or accept each, with a reason: `factory accept --change {change.id} --item F1 --reason ... --by NAME`."],
        blocking=block, acceptable=True)
