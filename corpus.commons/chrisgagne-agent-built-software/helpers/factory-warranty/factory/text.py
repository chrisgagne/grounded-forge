"""Model-written text made inert before a person reads it: the pack, decisions-needed.md and the terminal.

A builder or reviewer leg's words reach the signer. Without this, a control sequence could rewrite the terminal, an
invisible or bidirectional character could hide or reorder what the signer reads, and a Markdown image would make the
signer's viewer fetch a remote URL when the pack opens (OWASP LLM Top 10 2026, LLM05 improper output handling and
LLM01 prompt injection; OWASP Agentic Top 10 2026, ASI09 human-agent trust exploitation).
"""
from __future__ import annotations

import re

# C0 and C1 controls except tab and newline; zero-width, word-joiner and BOM; bidirectional embeddings, overrides and
# isolates; variation selectors; the Unicode tag block.
INVISIBLE = re.compile("[\x00-\x08\x0b-\x1f\x7f-\x9f​-‏ -‮⁠-⁤⁦-⁯﻿"
                       "︀-️\U000e0000-\U000e007f\U000e0100-\U000e01ef]")


def invisible_chars(text: str) -> list[str]:
    """The distinct invisible or control characters in text, as U+XXXX."""
    return sorted({f"U+{ord(c):04X}" for c in INVISIBLE.findall(text)})


def inert(text: str) -> str:
    """Strip controls and invisible characters; escape Markdown images and raw HTML tags so nothing renders or fetches."""
    text = INVISIBLE.sub("", str(text))
    text = text.replace("![", "!\\[")
    return re.sub(r"<(?=[A-Za-z/!?])", "&lt;", text)
