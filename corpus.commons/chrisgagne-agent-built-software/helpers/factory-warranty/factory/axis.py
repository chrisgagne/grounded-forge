"""Trigger→response rows from the task axis, for grounding review legs.

Two sources, one per grounding mode:

- `seeds`: the axis spec (`warranting-agent-built-software.md`, §2a) has one
  table per phase under `**Phase N: Title**`. Rows get IDs `P{phase}.{row}`.
- `distillations`: the axis's distillation index
  (`WARRANTING-AGENT-BUILT-SOFTWARE-DISTILLATION-INDEX.md`) has a
  `#### Runtime listeners: Phase N` table under
  each `### Phase N: Title`: the spec's seed rows first, then the rows the
  per-source distillations added. Each response names the distillations it
  rests on as backticked slugs. Rows get IDs `L{phase}.{row}`.

Each row gets a stable ID so a reviewer can cite the row it applied and the
driver can check the cite.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

PHASE_HEADING = re.compile(r"^\*\*Phase (\d+): (.+?)\*\*\s*$")
INDEX_PHASE = re.compile(r"^### Phase (\d+): (.+?)\s*$")
LISTENER_HEADING = re.compile(r"^#### Runtime listeners: Phase (\d+)\s*$")
SLUG = re.compile(r"`([a-z0-9][a-z0-9-]*)`")

# Phases a reviewer of a built change always gets: specifying, locking tests,
# building, gating and reviewing. Phase 2 (triage) rows come in by risk class.
REVIEW_PHASES = (1, 3, 4, 5, 6)
CLASS_TERMS = {
    "auth": r"login|session|token|permission",
    "personal-data": r"personal data",
    "llm-agent": r"LLM|prompt|agent",
    "migration": r"migration|delete|bulk update",
    "irreversible": r"migration|delete|bulk update",
    "infra": r"couples",
}


@dataclass
class Row:
    id: str
    phase: int
    phase_title: str
    trigger: str
    response: str
    sources: tuple[str, ...] = ()  # distillation slugs the response cites (listener rows only)

    def line(self) -> str:
        return f"- **{self.id}** (Phase {self.phase}: {self.phase_title}). Trigger: {self.trigger} → Response: {self.response}"


def cells(line: str) -> list[str]:
    """A markdown table row's cells; an escaped pipe stays inside its cell."""
    s = line.strip()
    if not s.startswith("|"):
        return []
    return [c.strip() for c in re.split(r"(?<!\\)\|", s.strip("|"))]


def is_body(row: list[str]) -> bool:
    return len(row) == 2 and not row[0].startswith("Trigger") and not set(row[0]) <= set("-: ")


def extract(spec_text: str) -> list[Row]:
    """Every seed row in the spec, in order."""
    start = spec_text.find("### Seed trigger")
    if start < 0:
        return []
    rows, phase, title, n = [], None, "", 0
    for line in spec_text[start:].splitlines():
        if line.startswith("## "):
            break
        m = PHASE_HEADING.match(line.strip())
        if m:
            phase, title, n = int(m.group(1)), m.group(2), 0
            continue
        row = cells(line)
        if phase is None or not is_body(row):
            continue
        n += 1
        rows.append(Row(f"P{phase}.{n}", phase, title, row[0], row[1]))
    return rows


def extract_listeners(index_text: str) -> list[Row]:
    """Every runtime listener row in the distillation index, in order."""
    rows, phase, title, n, on = [], None, "", 0, False
    for line in index_text.splitlines():
        m = INDEX_PHASE.match(line)
        if m:
            phase, title, n, on = int(m.group(1)), m.group(2), 0, False
            continue
        m = LISTENER_HEADING.match(line)
        if m:
            on = phase == int(m.group(1))
            continue
        if line.startswith("#"):
            on = False
            continue
        row = cells(line)
        if not on or not is_body(row):
            continue
        n += 1
        rows.append(Row(f"L{phase}.{n}", phase, title, row[0], row[1], tuple(dict.fromkeys(SLUG.findall(row[1])))))
    return rows


def rows_for_review(rows: list[Row], classes: list[str]) -> list[Row]:
    """Rows in play for reviewing a built change with these risk classes."""
    terms = "|".join(CLASS_TERMS[c] for c in classes if c in CLASS_TERMS)
    picked = []
    for r in rows:
        if r.phase in REVIEW_PHASES or (r.phase == 2 and terms and re.search(terms, r.trigger, re.I)):
            picked.append(r)
    return picked


def load(spec_path: str | Path) -> list[Row]:
    return extract(Path(spec_path).read_text())


def load_listeners(index_path: str | Path) -> list[Row]:
    return extract_listeners(Path(index_path).read_text())


def distillation_path(index_path: str | Path, slug: str) -> Path:
    """Where a cited slug's distillation sits: beside the index, named `{slug}-{task}.md`. A slug that names
    no file there (a hand-off to another axis, such as `aar`) has no path that exists."""
    folder = Path(index_path).parent
    return folder / f"{slug}-{folder.name}.md"
