"""Transformer: strip global 4-space pdftotext-margin uit body-regels.

`pdftotext -layout` (en derivaten zoals pdftotext_compilatie_btw) levert PDF's
af met een **globale 4-space linker-margin**. Resultaat in markdown:

    Art. 1.  De belasting bedraagt ...
    Art. 2.  Voor de toepassing ...

Markdown interpreteert 4-space-indent als CODE-BLOCK — wat:
- de RAG-chunking verstoort (code-blocks krijgen andere chunk-behandeling),
- lijstitems hun lijst-context verliest,
- visueel rommelig is.

Deze transformer strip de globale 4-space margin uit body-regels. Conservatief:
- Skip regels binnen fenced code-blocks (` ``` `) — daar is indent bedoeld.
- Skip frontmatter (transformer krijgt body zonder frontmatter binnen).
- Behoud RELATIEVE indent (bv. `        sub-item` → `    sub-item`).

Conform ADR-005 §1: format-agnostische tekst-transformatie → transformer-laag.
Wired in chains waar pdftotext een margin oplevert (compilatie + ejustice).
"""
from __future__ import annotations


def unindent_pdftotext_margin(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip 4 leading spaces uit elke body-regel die er begint met 4+ spaties.

    Behoudt:
    - Regels met 0-3 leading spaces (geen indent → onaangetast)
    - Relatieve indent (`        ` → `    `, `    foo` → `foo`)
    - Fenced code blocks ` ``` ... ``` ` (binnen-code niet aangeraakt)
    - Lege regels
    """
    out_lines: list[str] = []
    in_fence = False
    for line in body.split("\n"):
        # Fence-detect (toggle)
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue
        # Strip eerste 4 spaties van het line-begin als die er staan.
        if line.startswith("    "):
            out_lines.append(line[4:])
        else:
            out_lines.append(line)
    return "\n".join(out_lines), frontmatter
