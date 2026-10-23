"""Stage 7, warrant: assemble warranty.md from the ledger; record the human's sign, return or acceptance.

The pack is built by code from ledger events and the artefacts whose hashes
those events recorded; nothing a model says is filed as demonstrated. An
optional assessor leg may add a plain-language summary, filed as asserted: the
driver keeps only lines that cite ledger event ids that exist, which shows
where to look, not that the events support the line. The pack's sha256 goes into
the ledger; `sign` fails if the pack changed since, if any stage ran since, or
if the pack is not ready.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

from factory import legs
from factory.text import inert
from factory.ledger import READY_ORDER, WORK_STAGES, canonical, num, sha256_bytes, sha256_file
from factory.stages import brief, settings_file
from factory.stages.review import BLOCKING, DEFAULT_LEGS, LOWER_BAR, bar
from factory.stages.triage import RESIDUAL

CITE = re.compile(r"\[(e\d{3,})\]")



# Which company's model each review leg runs on, for the decision page.
LEG_MAKER = {"claude": "Anthropic", "claude-plain": "Anthropic", "codex": "OpenAI", "codex-review": "OpenAI"}
COUNT_WORD = {1: "One", 2: "Two", 3: "Three", 4: "Four"}


def reviewers(change) -> str:
    """The configured reviewers in plain words, e.g. "Two independent AI reviewers (from Anthropic and OpenAI)"."""
    names = list(change.config["review"].get("legs") or DEFAULT_LEGS)
    makers = sorted({LEG_MAKER.get(n, n) for n in names})
    count = COUNT_WORD.get(len(names), str(len(names)))
    noun = "reviewer" if len(names) == 1 else "reviewers"
    who = f"from {makers[0]}" if len(makers) == 1 else "from " + ", ".join(makers[:-1]) + f" and {makers[-1]}"
    return f"{count} independent AI {noun} ({who})"

def filter_cited(text: str, known: set[str]) -> tuple[list[str], list[str]]:
    """Keep lines that cite at least one ledger event and only events that exist; drop the rest."""
    kept, dropped = [], []
    for line in (ln.rstrip() for ln in text.splitlines()):
        if not line.strip():
            continue
        cites = CITE.findall(line)
        (kept if cites and all(c in known for c in cites) else dropped).append(line)
    return kept, dropped


def quote(text: str) -> str:
    return "\n".join(f"> {ln}" if ln.strip() else ">" for ln in inert(text).strip().splitlines())


def latest_artefacts(events: list[dict]) -> dict[str, tuple[str, str]]:
    """The last recorded sha256 for each artefact path: {path: (sha, event id)}."""
    out = {}
    for e in events:
        for path, sha in (e.get("artefacts") or {}).items():
            out[path] = (sha, e["id"])
    return out


POLICY = Path(__file__).resolve().parent.parent / "policy.yaml"
# What each gate check shows, in words for someone who doesn't read code.
GATE_PLAIN = {
    "locked-tests": "The tests written before the build weren't changed afterwards",
    "secrets": "No passwords, keys or tokens were added",
    "deps": "No package with a known security flaw was added",
    "sast": "The code scanner found no problem on the lines added",
    "invisible": "No hidden characters were added",
    "install": "The project installs",
    "typecheck": "The project's type check passes",
    "lint": "The project's style check passes",
    "build": "The project builds",
    "tests": "All the project's tests pass, the new ones included",
    "perf": "The project's speed check passes",
    "rollback": "The undo plan was rehearsed and worked",
    "surface": "No test, scanner or AI-instruction files were changed",
    "added-tests": "The builder added no test file that could interfere with the locked tests",
    "required": "Every check this kind of change needs was run",
    "unchanged": "The code didn't change while it was being checked",
}
PLAIN_SEVERITY = {"critical": "serious", "high": "serious", "medium": "moderate", "low": "minor"}
# What a qualified second person should check, by risk class (policy rule `second-person`).
SECOND_PERSON = {
    "personal-data": "Personal data: someone qualified checks who can see or change whose data, and an independent "
                     "penetration test before it holds real people's data.",
    "money": "Money: someone qualified checks amounts, rounding and double charges; reconcile real transactions after "
             "release.",
    "auth": "Sign-in and permissions: someone qualified checks who can reach what.",
    "irreversible": "A step that can't be undone: someone qualified confirms the backup and the undo plan before it "
                    "runs on real data.",
    "migration": "A database change: someone qualified confirms the undo plan keeps the data, not just the tables.",
}


def policy_rules() -> list[dict]:
    return (yaml.safe_load(POLICY.read_text()) or {}).get("rules", []) if POLICY.exists() else []


def asked_for(story: str) -> list[str]:
    """The story's "As ..., I want ..." lines, or its first paragraph."""
    lines = [ln.strip() for ln in story.splitlines()]
    wanted = [ln for ln in lines if re.match(r"^as (a|an|the|someone|the person)\b", ln, re.I)]
    if wanted:
        return wanted
    paras = [p.strip() for p in "\n".join(ln for ln in lines if not ln.startswith("#")).split("\n\n") if p.strip()]
    return paras[:1]


def breaks(finding: dict, criteria: list[tuple[str, str]]) -> str:
    """The criterion (or the story) the sort says a finding shows unmet, quoted, for the decision page."""
    which = finding.get("breaks")
    if which == "story":
        return " **The sorting AI says this goes against the story itself.**"
    text = dict(criteria).get(which)
    return f" **The sorting AI says this misses {which}: \"{inert(text)}\"**" if text else ""


CLASS_PLAIN = {"personal-data": "personal data", "irreversible": "a step that can't be undone"}
EVIDENCE_PLAIN = {"keyword": 'the story or its behaviours mention "{match}"', "path": "it changes {match}",
                  "pattern": "a line it adds in {source} reads `{match}`"}


def lower_bar_reasons(change, classes) -> list[str]:
    """Why the bar dropped to moderate: each class that lowers it, with the evidence triage found for it."""
    risk = change.dir / "risk.json"
    found = json.loads(risk.read_text()).get("classes", {}) if risk.exists() else {}
    return [f"{CLASS_PLAIN[c]}, because " + "; ".join(inert(EVIDENCE_PLAIN[e["rule"]].format(**e))
                                                     for e in found.get(c, {}).get("evidence", [])[:3])
            for c in sorted(set(classes) & set(LOWER_BAR))]


def decision_page(change, classes, gate, tests, findings, accepts, not_ready, open_items=()) -> list[str]:
    """The first page of the pack, for an accountable person who doesn't read code: what was asked, what the checks
    showed, what's left over, whether someone else must look, the rules it was judged by, and the choices. Built by
    code from the ledger; the only model-written text is quoted and labelled as such."""
    out = ["## Your decision", "",
           "You're deciding whether to accept this change, with what's left over below, or send it back. You're not "
           "being asked whether the code is right: the checks and the two reviewers below answer that, against the "
           "rules listed at the end of this page. What only you can answer: is this what was asked for, and will you "
           "carry what's left over?", ""]
    out += ["### What was asked for", ""]
    out += [f"> {inert(ln)}" for ln in asked_for((change.dir / "story.md").read_text())]
    acc = change.dir / "acceptance.md"
    criteria = re.findall(r"^## (AC-\d+): (.+)$", acc.read_text(), re.M) if acc.exists() else []
    red = next((e for e in reversed(tests) if e.get("check") == "new-tests"), None)
    green = next((e for e in reversed(gate) if e.get("check") == "tests"), None)
    if criteria:
        shown = (red and red.get("exit") not in (0, None) and green and green["status"] == "pass")
        out += ["", f"It was broken into {len(criteria)} behaviours (written by an AI from the story; read them to check "
                "they're what was meant)"
                + (f". Each has a test that failed before the change [{red['id']}] and passes now [{green['id']}]:"
                   if shown else ":"), ""]
        out += [f"- {cid}: {inert(text)}" for cid, text in criteria]
    out += ["", "### Did the checks pass?", ""]
    lines, unconfigured = [], []
    for e in gate:
        check = e.get("check", "")
        plain = GATE_PLAIN.get(check) or ("No scanner count rose" if check.startswith("ratchet:") else None)
        if not plain or e.get("applies") is False:
            continue
        if e["status"] == "skipped" and "is not configured" in str(e.get("reason")):
            unconfigured.append(check)
            continue
        took = next((a for a in accepts if a["item"] in (check, f"ratchet:{check[8:]}")), None)
        mark = ("yes" if e["status"] == "pass" else f"not checked ({inert(str(e.get('reason')))})" if e["status"] == "skipped"
                else f"no, accepted by {took['by']}: {inert(took['reason'])}" if took else "**no**")
        lines.append(f"- {plain}: {mark} [{e['id']}]")
    out += lines or ["- No gate run recorded."]
    if unconfigured:
        out.append(f"- Not checked, because the project has no such command: {', '.join(unconfigured)}.")
    serious = [f for f in findings if f.get("raw_severity", f["severity"]) in ("critical", "high")]
    out.append(f"- {reviewers(change)} read the change; "
               + ("neither rated anything serious." if not serious else
                  f"a reviewer rated {len(serious)} point(s) serious: {', '.join(f['id'] for f in serious)}."))
    held = [f for f in findings if f["id"] in open_items]
    if held:
        out += ["", "### What you must decide first", "",
                "The review stopped on these. Each needs your call: send the change back, or accept the point with "
                "your reason.", ""]
        out += [f"- {f['id']} (a reviewer rated it {PLAIN_SEVERITY[f.get('raw_severity', f['severity'])]}; "
                f"the sorting AI made it {PLAIN_SEVERITY[f['severity']]}, and may not clear it alone; the reviewers' "
                f"words): {inert(f['claim'])}{breaks(f, criteria)}" for f in held]
        moderate = [f["id"] for f in held if f.get("raw_severity", f["severity"]) not in BLOCKING]
        reasons = lower_bar_reasons(change, classes)
        if moderate and reasons:
            out += ["", f"{', '.join(moderate)} stopped the change at moderate, below the usual bar, because the rules "
                    "lower the bar where a change reaches personal data or a step that can't be undone. Triage put "
                    "this change there: " + "; ".join(reasons) + ". If the change doesn't do that, accept the point "
                    "and say so in your reason."]
    out += ["", "### What's left over", ""]
    reversible = not ({"migration", "irreversible"} & set(classes))
    left = [f"- {PLAIN_SEVERITY[f['severity']].capitalize()} ({f['id']}, the reviewers' words): {inert(f['claim'])}"
            f"{breaks(f, criteria)}"
            for f in findings if f["verdict"] == "confirmed" and f["severity"] not in bar(classes)
            and f["id"] not in open_items]
    left += [f"- The reviewers disagreed ({f['id']}, {PLAIN_SEVERITY[f['severity']]}): {inert(f['claim'])}"
             for f in findings if f["verdict"] == "disputed"]
    left += [f"- Accepted by {a['by']} ({a['item']}): {inert(a['reason'])}" for a in accepts]
    left += [f"- {text}" for c, text in RESIDUAL.items() if c in classes]
    out += left or ["- Nothing the checks or the reviewers left open."]
    out.append("- Undo: " + ("revert this change; nothing in it is one-way." if reversible else
                             "this change includes a step that may not be undoable; see the rollback section below."))
    out += ["", "### Does this need someone else?", ""]
    need = [SECOND_PERSON[c] for c in SECOND_PERSON if c in classes]
    out += [f"- {n}" for n in need] or ["- No: nothing in it reaches personal data, money, sign-in, the database's "
                                        "structure or a step that can't be undone."]
    out += ["", "### Within the rules?", ""]
    out += (["- Yes: every check the rules require passed or was accepted, and nothing is open above the bar."]
            if not not_ready else ["- **No.** Not ready to sign:"] + [f"  - {inert(r)}" for r in not_ready])
    rules = policy_rules()
    proposed = [r for r in rules if r.get("status") != "confirmed"]
    if rules:
        out += ["", f"The rules ({len(rules)}, in `factory/policy.yaml`)"
                + (f"; {len(proposed)} are PROPOSED and not yet confirmed by you:" if proposed else ", all confirmed:"), ""]
        out += [f"- {r['rule']} *{r.get('status', 'PROPOSED')}; set by {r.get('set_by', 'unknown')}.*" for r in rules]
    out += ["", "### Your choices", ""]
    if held:
        out += [f"- **Accept a point:** `factory accept --change {change.id} --item {held[0]['id']} --by NAME --reason "
                "\"...\"` records that you carry it; then the pack is rebuilt for you to sign."]
    elif not not_ready:
        out += [f"- **Sign it (accept the change):** `factory sign --change {change.id} --by NAME` records your name, "
                "the time and this pack's fingerprint."]
    out += [
            f"- **Send back:** `factory return --change {change.id} --by NAME --reason \"...\"`, in your own words. What "
            "you ask for gets new behaviours and locked tests first, then the builder gets your reason.",
            "- **Ask first:** ask about any line. Nothing is recorded until you sign or send it back.", ""]
    return out


def assemble(change) -> tuple[str, list[str]]:
    """The warranty pack, and the reasons it is not ready to sign (empty when ready)."""
    events = change.ledger.events()
    not_ready = []
    for path, (sha, eid) in latest_artefacts(events).items():
        if path == "warranty.md":  # rewritten by this run; sign checks it against this run's hash
            continue
        if not (change.dir / path).exists() or sha256_file(change.dir / path) != sha:
            not_ready.append(f"{path} no longer matches the sha256 recorded in {eid}")
    code = change.code_state()
    if not code["clean"]:
        not_ready.append("the worktree has uncommitted changes, which no evidence covers")
    states = {s: change.stage_ready(s) for s in READY_ORDER}
    not_ready += [f"{s}: {why}" for s, (ok, why) in states.items() if not ok]
    risk = json.loads((change.dir / "risk.json").read_text()) if (change.dir / "risk.json").exists() else {}
    classes = risk.get("classes", {})
    gate = change.last_run("gate")
    tests = change.last_run("tests")
    review = change.last_run("review")
    accepts = [e for e in events if e["stage"] == "accept"]
    m = change.meta
    out = [f"# Warranty pack: {change.id}", "",
           f"**Change:** {m['title']}  ",
           f"**Repo:** `{m['repo']}` · **branch** `{m['branch']}` · **baseline** `{m['baseline'][:12]}` → "
           f"**head** `{code['commit']}` (tree `{code['tree']}`){'' if code['clean'] else ', with uncommitted changes'}  ",
           f"**Builder:** {change.config['builder']['kind']}  ",
           f"**Assembled from ledger events** e001–{events[-1]['id']} (`ledger.json`).", "",
           f"**Status:** {'READY TO SIGN' if not not_ready else 'NOT READY TO SIGN'}", ""]
    out += [f"- {r}" for r in not_ready] + ([""] if not_ready else [])
    review_findings = change.dir / "review" / "findings.json"
    findings_now = json.loads(review_findings.read_text()) if review_findings.exists() and review else []
    rev_out = change.outcome("review")
    held = [i for i in (rev_out.get("blocking") or []) if i not in change.accepted(rev_out["id"])] if rev_out else []
    out += decision_page(change, classes, gate, tests, findings_now, accepts, not_ready, held)
    out += ["# The evidence", ""]

    out += ["## Story", "", quote((change.dir / "story.md").read_text()), ""]
    out += ["## Risk classes", ""]
    if classes:
        for c, info in classes.items():
            ev = "; ".join(f"{x['rule']} in {x['source']}: {x['match']}" for x in info["evidence"][:3])
            gates = ", ".join(info["required_gates"]) or "none beyond the standard gates"
            out.append(f"- **{c}**: {ev}. Required gates: {gates}. Review focus: {info['review_focus']}")
    else:
        out.append("- None found.")
    tri = change.outcome("triage")
    out += ["", f"Triage: {tri['status'] if tri else 'not run'} ({tri['id'] if tri else '-'}), "
                f"phase {risk.get('phase', '-')}.", ""]

    out += ["## Demonstrated", "", "Commands the driver ran, with exit codes and output hashes.", ""]
    for e in tests + gate:
        if "cmd" in e and not e.get("check", "").startswith(("leg:", "ratchet:")):
            note = " (expected: red before the build)" if e.get("check") == "new-tests" else ""
            if e.get("after_event"):
                out.append(f"- [{e['id']}] {e['stage']}:{e['check']} evaluates the output of {e['after_event']}; "
                           f"it ran no command of its own, log `{(e.get('evidence') or ['-'])[0]}`")
                continue
            exit_text = e["exit"] if e.get("exit") is not None else "none (timed out)"
            out.append(f"- [{e['id']}] {e['stage']}:{e['check']} `{e['cmd']}` exit {exit_text}{note}, "
                       f"output sha256 `{(e.get('output_sha256') or '')[:16]}`, log `{(e.get('evidence') or ['-'])[0]}`")
    lock = next((e for e in reversed(gate) if e.get("check") == "locked-tests"), None)
    if lock:
        out.append(f"- [{lock['id']}] locked-test hash check: **{lock['status']}**, {lock.get('locked', 0)} files"
                   + (f"; {lock['reason']}" if lock.get("reason") else "")
                   + (f"; unlocked new test files: {', '.join(lock['added'])}" if lock.get("added") else ""))
    out.append("")

    out += ["## Asserted, not evidence", "",
            "The builder's own words. Nothing here was checked by running anything.", ""]
    for name, label in (("builder-summary.md", "Builder summary"), ("tests-summary.md", "Tests-leg summary")):
        if (change.dir / name).exists():
            out += [f"**{label}** (`{name}`):", "", quote((change.dir / name).read_text()), ""]

    out += ["## Gates", "", "| Check | Status | Event | Detail |", "|---|---|---|---|"]
    for e in gate:
        if e.get("check") in ("start", "outcome", None):
            continue
        detail = e.get("reason") or (f"exit {e['exit']}" if "exit" in e else e.get("note", ""))
        out.append(f"| {e['check']} | {e['status']} | {e['id']} | {str(detail).replace('|', '/')[:160]} |")
    out += ["", "**Stage outcomes:**", ""]
    out += [f"- {s}: {'ready' if ok else 'not ready'} ({why})" for s, (ok, why) in states.items()]
    out.append("")

    out += ["## Ratchet", ""]
    ratchets = [e for e in gate if e.get("check", "").startswith("ratchet:")]
    out += [f"- [{e['id']}] {e['check'][8:]}: {e.get('before')} at baseline → {e.get('after')} after the change "
            f"(**{e['status']}**); `{e['cmd']}`, output sha256 baseline "
            f"`{e['runs']['baseline']['output_sha256'][:16]}`, after `{e['runs']['after']['output_sha256'][:16]}`"
            for e in ratchets] or ["- No ratchet configured."]
    theory = next((e for e in reversed(gate) if e.get("check") == "theory-doc"), None)
    out += ["", "## Theory doc", ""]
    out.append(f"- [{theory['id']}] `{theory['path']}`: {'changed by this change' if theory['changed'] else 'not changed'}"
               f"{'' if theory['exists'] else ' (does not exist at head)'}" if theory else
               f"- `{change.config['theory_doc']}` is configured but no gate run recorded it." if change.config.get("theory_doc")
               else "- No theory doc configured.")
    out.append("")

    out += ["## Review", ""]
    for e in review:
        if not e.get("check", "").startswith("leg:"):
            continue
        name = e.get("leg") or e["check"][4:]
        if e["status"] == "skipped":
            out.append(f"- [{e['id']}] {name}: skipped ({e['reason']})")
            continue
        spend = f"${e['cost_usd']:.2f}" if e.get("cost_usd") is not None else f"{e.get('tokens') or '?'} tokens"
        out.append(f"- [{e['id']}] {name} ({e.get('model')}): {e['status']}, {spend}, {e.get('duration_s')} s")
    packet = next((e for e in review if e.get("check") == "packet"), None)
    if packet:
        out.append(f"- [{packet['id']}] grounding: {packet['grounding']} ({packet['axis_rows']} axis rows)")
    findings_file = change.dir / "review" / "findings.json"
    findings = json.loads(findings_file.read_text()) if findings_file.exists() and review else []
    rev = change.outcome("review")
    if findings:
        out += ["", "| ID | Severity | Verdict | Where | Claim | Sort reason | Resolution |", "|---|---|---|---|---|---|---|"]
        for f in findings:
            res = "-"
            if rev and f["id"] in (rev.get("blocking") or []):
                acc = change.accepted(rev["id"]).get(f["id"])
                res = f"accepted by {acc['by']} [{acc['id']}]: {acc['reason']}" if acc else "**open (blocks)**"
            where = f"{f.get('file')}:{f.get('line')}"
            row = [f["id"], f["severity"], f["verdict"], where, f["claim"], f["reason"], res]
            out.append("| " + " | ".join(inert(x).replace("|", "/").replace("\n", " ")[:200] for x in row) + " |")
        shown = [f for f in findings if f.get("shown")]
        if shown:
            out += ["", "What the factory ran for each blocking finding (a check that fails after the change and passed "
                    "before it shows the change in behaviour; whether that change is wanted is yours to decide):", ""]
            labels = {"shown": "Shown", "not shown": "Not shown", "argued": "Can't be run, argued only",
                      "unchecked": "Not checked (the step gave no usable answer)"}
            for f in shown:
                s = f["shown"]
                where = f" Check: `review/reproduce/{f['id']}/`." if (change.dir / "review" / "reproduce" / f["id"]).is_dir() else ""
                out.append(f"- {f['id']}: **{labels.get(s['outcome'], s['outcome'])}.** {inert(s.get('why') or '')}{where}")
    elif review:
        out.append("- No findings.")
    out.append("")

    out += ["## Irreversible operations and rollback", ""]
    rb = next((e for e in reversed(gate) if e.get("check") == "rollback"), None)
    if {"migration", "irreversible"} & set(classes):
        out.append(f"- Classes: {', '.join(sorted({'migration', 'irreversible'} & set(classes)))}.")
        if rb:
            out.append(f"- [{rb['id']}] rollback: {rb['status']}"
                       + (f", rehearsed with `{rb['cmd']}` exit {rb.get('exit')}" if rb.get("cmd") else "")
                       + (f"; {rb.get('reason') or rb.get('note')}" if rb.get("reason") or rb.get("note") else ""))
    else:
        out.append("- No migration or irreversible class.")
    out.append("")

    out += ["## Residual risks", ""]
    residual = [f"- [{e['id']}] gate:{e['check']} skipped: {e['reason']}" for e in gate
                if e["status"] == "skipped" and e.get("applies") is not False]
    residual += [f"- {f['id']} confirmed ({f['severity']}), below the blocking bar and unfixed: {inert(f['claim'])}"
                 for f in findings if f["verdict"] == "confirmed" and f["severity"] not in bar(classes)]
    residual += [f"- {f['id']} {f['verdict']} ({f['severity']}): {inert(f['claim'])}" for f in findings
                 if f["verdict"] == "disputed"]
    residual += [f"- [{a['id']}] {a['item']} accepted by {a['by']}: {a['reason']}" for a in accepts]
    residual += [f"- {text}" for c, text in RESIDUAL.items() if c in classes]
    if rb and rb.get("rehearsed") is False:
        residual.append(f"- [{rb['id']}] the rollback is described but not rehearsed.")
    if theory and not theory["changed"]:
        residual.append(f"- [{theory['id']}] the theory doc did not change; the reviewers were asked to flag behaviour it describes that the diff changed.")
    for e in (e for e in events if e.get("check") == "guard" and e.get("blocked_calls")):
        residual.append(f"- [{e['id']}] the guard blocked {e['blocked_calls']} {e['stage']}-leg tool calls: "
                        + "; ".join(e.get("reasons", [])[:3]))
    out += residual or ["- None recorded."]
    out += ["", "## Sign-off", "",
            "Accountable person: ______________________", "",
            "Decision: [ ] sign   [ ] return", "",
            "Reason (for a return): ______________________", "",
            f"Record the decision with `factory sign --change {change.id} --by NAME` or "
            f"`factory return --change {change.id} --reason \"...\"`. The ledger records it with this pack's sha256. "
            "The harness never signs.", ""]
    return "\n".join(out), not_ready


def run(change, assessor: bool = False) -> bool:
    change.start("warrant")
    text, not_ready = assemble(change)
    if assessor:
        text = add_assessor(change, text)
    change.path("warranty.md").write_text(text)
    pack = sha256_file(change.dir / "warranty.md")
    return change.finish("warrant", not_ready, ["Settle each item above, then re-run `factory warrant`."],
                         pack_sha256=pack, artefacts=change.hashes("warranty.md"))


def add_assessor(change, draft: str) -> str:
    draft_file = change.path("warrant/draft.md")
    draft_file.write_text(draft)
    prompt = brief("assessor.md", ledger=change.dir / "ledger.json", draft=draft_file)
    prompt_file = change.path("warrant/assessor-brief.md")
    prompt_file.write_text(prompt)
    res = legs.run_claude(f"Read {prompt_file} in full and do what it asks. Your final message is only the summary lines.",
                          change.dir, change.path("warrant/assessor-log.jsonl"),
                          model=change.config["legs"]["claude_model"], timeout_s=change.timeout(), read_only=True,
                          setting_sources=change.config["legs"].get("setting_sources"),
                          settings=settings_file(change, "warrant", "assessor"))
    change.record_leg("warrant", "assessor", res, prompt_file)
    if not res["ok"]:
        return draft
    known = {e["id"] for e in change.ledger.events()}
    kept, dropped = filter_cited(res["result"], known)
    change.path("warrant/assessor-dropped.md").write_text("\n".join(dropped) + "\n")
    change.record("warrant", "info", check="assessor-filter", kept=len(kept), dropped=len(dropped),
                  evidence=["warrant/assessor-dropped.md"])
    if not kept:
        return draft
    head, rest = draft.split("## Story", 1)
    return (head + "## Assessor's summary (asserted, not evidence)\n\n"
            "A model wrote these lines. The driver kept only lines that cite ledger events that exist; it did not "
            "check that those events support what the line says. Read the sections below for the evidence.\n\n"
            + "\n".join(kept) + "\n\n## Story" + rest)


# the human's step -------------------------------------------------------------------

def pack_state(change) -> tuple[dict | None, str | None]:
    """The latest warrant outcome, or why there is no signable pack."""
    w = change.outcome("warrant")
    if not w:
        return None, "no warranty pack: run `factory warrant`"
    pack = change.dir / "warranty.md"
    if not pack.exists() or sha256_file(pack) != w["pack_sha256"]:
        return w, f"warranty.md changed since it was assembled in {w['id']}; re-run `factory warrant`"
    later = [e for e in change.ledger.events()
             if num(e["id"]) > num(w["id"]) and e["stage"] in WORK_STAGES + ("return",)]
    if later and later[0]["stage"] == "return":
        return w, (f"the pack was returned ({later[0]['id']}) after it was assembled; rebuild, then gate, review "
                   "and warrant again")
    if later:
        return w, f"{later[0]['stage']} ran after the pack was assembled ({later[0]['id']}); re-run `factory warrant`"
    problem = change.code_problem(w, "the pack")
    if problem:
        return w, problem
    return w, None


SEALED = ("change", "by", "at", "pack_sha256", "commit", "tree", "warrant_event")


def seal(fields: dict) -> str:
    """The sha256 that binds a signature's fields together: pack, commit, tree, signer and time."""
    return sha256_bytes(canonical({k: fields.get(k) for k in SEALED}))


def sign(change, by: str) -> tuple[bool, str]:
    w, problem = pack_state(change)
    if problem:
        return False, problem
    if w["status"] != "pass":
        return False, f"the pack is not ready to sign: {w.get('reason')}"
    fields = {"change": change.id, "by": by, "at": legs.now(), "pack_sha256": w["pack_sha256"],
              "commit": w["commit"], "tree": w["tree"], "warrant_event": w["id"]}
    e = change.record("sign", "pass", check="signature", **fields, seal=seal(fields))
    return True, f"signed by {by} ({e['id']}) at commit {w['commit'][:12]}, pack sha256 {w['pack_sha256']}"


def return_(change, reason: str, by: str | None) -> tuple[bool, str]:
    w = change.outcome("warrant")
    change.finish("return", [f"returned by {by or 'the accountable human'}: {reason}"],
                  [f"`factory run --change {change.id}`: spec adds criteria for what the reason asks, tests writes and "
                   "locks tests for them, then the build (its prompt carries the reason), gate, review and warrant."],
                  by=by, request=reason, pack_sha256=w["pack_sha256"] if w else None)
    return True, f"returned ({change.outcome('return')['id']}): {reason}"


def accept(change, item: str, reason: str, by: str) -> tuple[bool, str]:
    stage = "review" if re.fullmatch(r"F\d+", item) else "triage" if item.startswith("class:") else \
        "gate" if item.startswith("ratchet:") or item in ("surface", "added-tests", "invisible") else None
    if not stage:
        return False, ("only review findings (F1), triage classes (class:NAME), measured ratchet rises (ratchet:NAME), "
                       "test/scanner config changes (surface), unlocked test files the build added (added-tests) "
                       "and added invisible characters (invisible) can be accepted")
    out = change.outcome(stage)
    if not out or out["status"] != "blocked" or item not in (out.get("blocking") or []):
        return False, f"{item} is not blocking the latest {stage} run"
    e = change.record("accept", "info", check="acceptance", item=item, reason=reason, by=by, applies_to=out["id"])
    return True, f"accepted {item} ({e['id']}); it covers {stage} run {out['id']}"
