"""
Transformer: cleanup_basics (ADR-005 §4).

Bundelt de cleanup-functies uit `tools/lib/cleanup.py` als één transformer-entry.
De concrete cleanup-stappen zijn geconfigureerd via `_cleanup_steps_for` in
`tools/etl/convert.py`, dus de stap-lijst kan per oproep verschillen.

Publieke chain-entry: ``cleanup_basics``.

Signature: (body: str, frontmatter: dict) -> tuple[str, dict]

De frontmatter wordt niet gewijzigd door deze transformer — cleanup werkt
enkel op de body.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.lib.cleanup import run_pipeline  # noqa: E402


def cleanup_basics(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Voer de default cleanup-stappen uit op de body.

    De concrete stap-lijst wordt bepaald door de `_cleanup_steps` sleutel in
    `frontmatter` (gezet door de orchestrator vóór de chain start). Als die
    sleutel ontbreekt, wordt geen cleanup uitgevoerd (pass-through).

    De `_cleanup_steps` sleutel is een intern orchestrator-veld en wordt na
    gebruik uit de frontmatter verwijderd zodat hij niet in de output landt.
    """
    steps = frontmatter.pop("_cleanup_steps", None)
    if not steps:
        return body, frontmatter

    new_body = run_pipeline(body, steps=steps, preserve_frontmatter=False)
    return new_body, frontmatter
