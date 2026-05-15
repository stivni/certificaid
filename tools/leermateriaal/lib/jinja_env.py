"""
Jinja2 Environment setup voor leermateriaal-templates (ADR-010).

Laadt templates vanuit tools/leermateriaal/templates/ met strict undefined-mode
zodat ontbrekende variabelen vroeg falen. Registreert confidence_label en slugify
als Jinja2-filters.
"""

from __future__ import annotations

from pathlib import Path

from jinja2 import ChainableUndefined, Environment, FileSystemLoader

from tools.leermateriaal.lib.confidence import label as confidence_label_fn
from tools.leermateriaal.lib.wikilinks import slugify as slugify_fn

_TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"

_env: Environment | None = None


def get_env() -> Environment:
    """Haal de geconfigureerde Jinja2 Environment op (singleton).

    Filters beschikbaar in templates:
    - ``confidence_label``: confidence-string → emoji ('grounded' → '⚖️', anders '🤖')
    - ``slugify``: tekst → URL-slug

    Returns:
        geconfigureerde Jinja2 Environment
    """
    global _env
    if _env is None:
        _env = Environment(
            loader=FileSystemLoader(str(_TEMPLATES_DIR)),
            undefined=ChainableUndefined,
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
        )
        _env.filters["confidence_label"] = confidence_label_fn
        _env.filters["slugify"] = slugify_fn
    return _env
