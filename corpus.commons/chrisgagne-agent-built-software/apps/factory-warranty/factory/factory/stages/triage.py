"""Stage 2, triage: map the change to risk classes, and the gates and review focus each class needs.

Deterministic. Three kinds of evidence:
  keyword   words in the story and the acceptance criteria (the plan)
  path      planned or changed paths against the built-in path rules and the repo's risk_paths
  pattern   precise code patterns on the diff's changed lines outside test files

Keywords add a class's review focus; a path or pattern also adds its required
gates (a migration path or a DROP needs a rehearsed rollback; a word in the
story doesn't). Before the build, triage records what the plan touches. After the build it
re-runs on the actual diff, and blocks when the diff reaches a risk class by
path or pattern that the plan never mentioned: the agent went somewhere nobody
asked it to. The human resolves that by changing the plan or accepting the
class (`factory accept --item class:NAME`).
"""
from __future__ import annotations

import json
import re

from factory.hooks.guard import globmatch
from factory.stages.spec import parse_acceptance

CLASSES = ("auth", "personal-data", "money", "migration", "irreversible", "infra", "llm-agent", "dependency", "secrets")

KEYWORDS = {
    "auth": r"log ?in|logout|sign[- ]?in|passwords?|sessions?|jwt|oauth|oidc|sso|mfa|2fa|csrf|authenticat\w*|"
            r"authori[sz]\w*|permissions?|access control",
    "personal-data": r"pii|personal (data|information)|gdpr|date of birth|ssn|social security|passport|"
                     r"phone numbers?|email address(es)?|home address|medical|health records?",
    "money": r"payments?|invoices?|refunds?|billing|checkout|currency|stripe|paypal|payouts?|subscriptions?|pricing|"
             r"prices?|charges?|wallet",
    "migration": r"migrations?|migrate|schema change|alter table|add column|create table",
    "irreversible": r"delete|deletes|deleting|deletion|purge|wipe|drop|bulk update|irreversible|permanently|truncate",
    "infra": r"terraform|kubernetes|k8s|helm|dockerfile|docker-compose|ci pipeline|github actions|cloudformation|"
             r"iam|dns|load balancer|infrastructure",
    "llm-agent": r"llm|large language model|prompts?|openai|anthropic|claude|gpt-?\d\w*|chatgpt|embeddings?|"
                 r"langchain|tool[- ]call\w*|function[- ]calling|mcp|ai agent|agentic",
    "dependency": r"new dependency|add(s|ing)? (a |the )?(package|library|dependency)|upgrade \S+ to",
    "secrets": r"api[_ -]?keys?|secrets?|private key|credentials?|access tokens?",
}

PATHS = {
    "auth": ["**/auth/**", "**/login*"],
    "migration": ["**/migrations/**", "db/migrate/**"],
    "infra": ["**/Dockerfile*", "**/docker-compose*", ".github/workflows/**", "**/*.tf", "terraform/**", "k8s/**",
              "helm/**", "infra/**", ".gitlab-ci.yml", "Procfile"],
    "llm-agent": ["**/prompts/**", "**/llm/**"],
    "dependency": ["**/package-lock.json", "**/npm-shrinkwrap.json", "**/yarn.lock", "**/pnpm-lock.yaml",
                   "**/poetry.lock", "**/uv.lock", "**/Pipfile.lock", "**/requirements*.txt", "**/Cargo.lock",
                   "**/go.sum", "**/Gemfile.lock", "**/composer.lock"],
    "secrets": ["**/.env*", "**/*.pem", "**/*.key", "**/secrets/**", "**/credentials*"],
}

DOWN_MIGRATION = re.compile(r"(^|[._-])down\.sql$", re.I)
PATTERNS = {
    "irreversible": r"\bDROP\s+(TABLE|COLUMN|DATABASE|SCHEMA)\b|\bTRUNCATE\s+(TABLE\s+)?\w|\bDELETE\s+FROM\s+\w+\s*(;|[\"'`]|$)",
    "migration": r"\bALTER\s+TABLE\b",
    "llm-agent": (r"require\(\s*[\"'](openai|@anthropic-ai/sdk|@google/genai|@google/generative-ai|@mistralai/\w+|"
                  r"cohere-ai|ollama|ai|@ai-sdk/\w+|langchain|@langchain/\w+|llamaindex)[\"']|"
                  r"from\s+[\"'](openai|@anthropic-ai/sdk|@google/genai|@google/generative-ai|@mistralai/\w+|cohere-ai|"
                  r"ollama|ai|@ai-sdk/\w+|langchain|@langchain/\w+|llamaindex)[\"']|"
                  r"^\s*(import|from)\s+(openai|anthropic|google\.genai|google\.generativeai|mistralai|cohere|ollama|"
                  r"langchain\w*|llama_index|litellm)\b"),
    "secrets": r"-----BEGIN [A-Z ]*PRIVATE KEY-----|\bAKIA[0-9A-Z]{16}\b|\bsk-[A-Za-z0-9_-]{20,}|\bghp_[A-Za-z0-9]{30,}",
}
# A dependency line in a manifest: "name": "^1.2.3" (package.json), name==1.2 (requirements), name = "1.2" (toml).
MANIFESTS = ("package.json", "pyproject.toml", "Cargo.toml", "go.mod", "Gemfile", "composer.json")
DEP_LINE = r"^\s*\"?[@\w./-]+\"?\s*(:|==|>=|=)\s*\"?[\^~>=]*\d"

REQUIRED_GATES = {"migration": ["gate:rollback"], "irreversible": ["gate:rollback"], "dependency": ["gate:deps"],
                  "secrets": ["gate:secrets"]}
REVIEW_FOCUS = {
    "auth": "OWASP ASVS 5.0 V6 Authentication, V7 Session Management and V8 Authorization, plus V3.3 Cookie Setup "
            "and V3.5 Browser Origin Separation where a session lives in a cookie (V9 Self-contained Tokens and V10 "
            "OAuth and OIDC where tokens or OAuth are involved).",
    "personal-data": "OWASP ASVS 5.0 V14 Data Protection and V8 Authorization: who can read or change whose data; "
                     "what is logged or sent out.",
    "money": "Amounts, rounding and currency; idempotency (no double charge); who may move money "
             "(ASVS 5.0 V2 Validation and Business Logic).",
    "migration": "Is the migration reversible; does the down path restore data, not just schema; is the rollback rehearsed?",
    "irreversible": "What can't be undone; is there a backup and a rehearsed restore?",
    "infra": "Least privilege and blast radius; build once and promote the same artefact.",
    "llm-agent": "OWASP Top 10 for LLM Applications 2026 and OWASP Top 10 for Agentic Applications 2026: prompt "
                 "injection, excessive agency, tool misuse, data leaking through the model.",
    "dependency": "Is the new dependency needed, maintained and free of known vulnerabilities (NIST SP 800-218A)?",
    "secrets": "No secret in code, config or logs; secrets come from the environment.",
}
RESIDUAL = {
    "personal-data": "Personal data: plan an independent penetration test before launch.",
    "llm-agent": "LLM or agent behaviour: deterministic gates don't cover model behaviour; watch it in production.",
    "money": "Money: reconcile real transactions after release.",
    "infra": "Infrastructure: the gates ran against the worktree, not the target environment.",
}


def classify_text(text: str, source: str) -> dict[str, list[dict]]:
    found = {}
    for cls, words in KEYWORDS.items():
        hits = sorted({m.group(0).lower() for m in re.finditer(rf"\b({words})\b", text, re.I)})
        if hits:
            found[cls] = [{"rule": "keyword", "source": source, "match": ", ".join(hits[:6])}]
    return found


def classify_paths(paths: list[str], risk_paths: dict, source: str) -> dict[str, list[dict]]:
    found = {}
    rules = {c: list(PATHS.get(c, [])) + list(risk_paths.get(c, [])) for c in set(PATHS) | set(risk_paths)}
    for cls, globs in rules.items():
        hits = [p for p in paths if any(globmatch(p, g) for g in globs)]
        if hits:
            found[cls] = [{"rule": "path", "source": source, "match": ", ".join(hits[:6])}]
    return found


ESCAPES = {"a": "\a", "b": "\b", "t": "\t", "n": "\n", "v": "\v", "f": "\f", "r": "\r", '"': '"', "\\": "\\"}


def unquote(path: str) -> str:
    """A path from a diff header: git C-quotes names with unusual characters ("b/caf\303\251.js")."""
    if not (len(path) >= 2 and path[0] == '"' and path[-1] == '"'):
        return path
    raw, i, body = bytearray(), 0, path[1:-1]
    while i < len(body):
        c = body[i]
        if c == "\\" and i + 1 < len(body):
            n = body[i + 1]
            if n in "01234567" and i + 3 < len(body) + 1 and all(ch in "01234567" for ch in body[i + 1:i + 4]):
                raw.append(int(body[i + 1:i + 4], 8))
                i += 4
                continue
            raw += ESCAPES.get(n, n).encode()
            i += 2
            continue
        raw += c.encode()
        i += 1
    return raw.decode("utf-8", "surrogateescape")


def changed_lines(diff: str, skip_globs: list[str]) -> dict[str, list[str]]:
    """Added and removed lines per file, leaving out files that match skip_globs (the tests)."""
    out, current = {}, None
    for line in diff.splitlines():
        if line.startswith("+++ "):
            path = unquote(line[4:].rstrip("\t")).removeprefix("b/")
            current = None if path == "/dev/null" or any(globmatch(path, g) for g in skip_globs) else path
            if current:
                out.setdefault(current, [])
        elif current and line[:1] in "+-" and not line.startswith("--- "):
            out[current].append(line[1:])
    return out


def classify_diff(lines: dict[str, list[str]]) -> dict[str, list[dict]]:
    found = {}
    for path, body in lines.items():
        down = bool(DOWN_MIGRATION.search(path.rsplit("/", 1)[-1]))
        for cls, rx in PATTERNS.items():
            m = next((m for ln in body if (m := re.search(rx, ln, re.I if cls != "secrets" else 0))), None)
            if m:
                # Never copy a secret into the evidence: keep its first 8 characters only.
                hit = m.group(0)[:8] + "…[redacted]" if cls == "secrets" else m.string.strip()[:120]
                # A DROP in a down migration is the rollback path, not a new one-way step: every additive migration
                # has one. It files under migration, whose rehearsed rollback covers it.
                found.setdefault("migration" if down and cls == "irreversible" else cls, []).append(
                    {"rule": "pattern", "source": path, "match": hit})
        if path.rsplit("/", 1)[-1] in MANIFESTS:
            hit = next((ln.strip() for ln in body if re.search(DEP_LINE, ln)), None)
            if hit:
                found.setdefault("dependency", []).append({"rule": "pattern", "source": path, "match": hit[:120]})
    return found


def planned_paths(text: str) -> list[str]:
    """Paths the story or acceptance names in backticks or check lines."""
    paths = re.findall(r"`([\w./-]+/[\w.-]+|[\w-]+\.\w{1,5})`", text)
    paths += [ln.split(":", 1)[1].split("::")[0].strip().strip("`") for ln in text.splitlines()
              if ln.strip().lower().startswith("check:")]
    return sorted(set(paths))


def merge(*maps: dict) -> dict[str, list[dict]]:
    out = {}
    for m in maps:
        for cls, ev in m.items():
            out.setdefault(cls, []).extend(ev)
    return out


def criteria_text(acceptance: str) -> str:
    """The criteria and their check lines: what will be built. The spec leg's own notes around them aren't the plan,
    so a word there ("drop it if you count it as documentation") doesn't put the change in a risk class."""
    return "\n".join(f"## {c['id']}: {c['text']}\ncheck: {c['check'] or ''}" for c in parse_acceptance(acceptance)[0])


def assess(story: str, acceptance: str, risk_paths: dict, changed: list[str] | None = None,
           diff: str | None = None, test_globs: list[str] = ()) -> dict:
    """The risk.json content. `changed` and `diff` are None before the build."""
    plan_text = story + "\n" + criteria_text(acceptance)
    planned = merge(classify_text(plan_text, "story/acceptance"),
                    classify_paths(planned_paths(plan_text), risk_paths, "planned paths"))
    actual = {}
    if changed is not None:
        actual = merge(classify_paths(changed, risk_paths, "diff paths"),
                       classify_diff(changed_lines(diff or "", list(test_globs))))
    every = merge(planned, actual)
    classes = {}
    for c in (c for c in CLASSES if c in every):
        strong = any(e["rule"] != "keyword" for e in every[c])  # a word in the story adds review focus, not gates
        classes[c] = {"evidence": every[c], "strength": "path or pattern" if strong else "keyword only",
                      "required_gates": REQUIRED_GATES.get(c, []) if strong else [], "review_focus": REVIEW_FOCUS[c]}
    return {"phase": "plan" if changed is None else "diff", "classes": classes,
            "unplanned": sorted(c for c in actual if c not in planned)}


def run(change) -> bool:
    change.start("triage")
    acceptance = change.dir / "acceptance.md"
    built = change.outcome("build") is not None
    risk = assess((change.dir / "story.md").read_text(), acceptance.read_text() if acceptance.exists() else "",
                  change.config["risk_paths"] or {}, change.changed_files() if built else None,
                  change.diff() if built else None, change.config["test_globs"])
    change.path("risk.json").write_text(json.dumps(risk, indent=1))
    change.record("triage", "info", check="classes", phase=risk["phase"], classes=sorted(risk["classes"]),
                  unplanned=risk["unplanned"] or None, artefacts=change.hashes("risk.json"))
    reasons = [f"the diff reaches risk class {c} ({risk['classes'][c]['evidence'][-1]['match']}), which the story "
               "and acceptance didn't plan for" for c in risk["unplanned"]]
    unblock = [f"If {c} is intended, accept it: `factory accept --change {change.id} --item class:{c} --reason ... "
               f"--by NAME`; otherwise rebuild without it (`factory build`)." for c in risk["unplanned"]]
    return change.finish("triage", reasons, unblock, blocking=[f"class:{c}" for c in risk["unplanned"]],
                         acceptable=True, phase=risk["phase"])
