"""Shared helpers for the JSON index builders."""

from __future__ import annotations

import json
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def corpus_root(corpus: str) -> Path:
    """Resolve a corpus name to its on-disk root, preferring commons over local."""
    commons = repo_root() / "corpus.commons" / corpus
    if commons.is_dir():
        return commons
    local = repo_root() / "corpus.local" / corpus
    if local.is_dir():
        return local
    return commons


def load_slug_table(corpus: str) -> dict:
    path = corpus_root(corpus) / "references" / "slug-table.json"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def slug_to_id(slug_table: dict) -> dict[str, str]:
    return {slug: rid for rid, slug in slug_table["slugs"].items() if slug is not None}


def deep_ref_path(corpus: str, slug: str) -> Path:
    return corpus_root(corpus) / "references" / f"{slug}-deep.md"


def light_ref_path(corpus: str, slug: str) -> Path:
    return corpus_root(corpus) / "references" / f"{slug}.md"


def extracted_path(corpus: str, slug: str) -> Path:
    return repo_root() / "_planning" / "extracted" / corpus / f"{slug}.json"


def staging_dir(corpus: str, kind: str) -> Path:
    return repo_root() / "_planning" / "staging" / corpus / kind


def index_output_dir(corpus: str) -> Path:
    return corpus_root(corpus)


def count_lines(path: Path) -> int | None:
    if not path.is_file():
        return None
    with path.open("r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def read_scope(deep_path: Path) -> str | None:
    """Read the ``**Scope:**`` line from a deep-ref frontmatter block.

    The Scope line is mechanically reliable: it is operator-authored, single-
    token, drawn from a fixed vocabulary (open, open-nc, copyrighted,
    confidential, personal). Author/year are not; they ride the Sonnet pass.
    """
    if not deep_path.is_file():
        return None
    with deep_path.open("r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith("**Scope:**"):
                value = stripped[len("**Scope:**"):].strip()
                return value.split()[0] if value else None
            if line.startswith("## "):
                break
    return None
