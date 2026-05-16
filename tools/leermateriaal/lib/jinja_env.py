"""
Jinja2 Environment setup voor leermateriaal-templates (ADR-010).

Laadt templates vanuit tools/leermateriaal/templates/ met strict undefined-mode
zodat ontbrekende variabelen vroeg falen. Registreert confidence_label, slugify,
regex_replace, regex_search en truncate_cell als Jinja2-filters.
"""

from __future__ import annotations

import re
from pathlib import Path

from jinja2 import ChainableUndefined, Environment, FileSystemLoader

from tools.leermateriaal.lib.confidence import label as confidence_label_fn
from tools.leermateriaal.lib.wikilinks import slugify as slugify_fn

_TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"

_env: Environment | None = None


def _regex_replace(waarde: str, patroon: str, vervanging: str = "") -> str:
    """Vervang regex-matches in een string."""
    return re.sub(patroon, vervanging, str(waarde))


def _regex_search(waarde: str, patroon: str) -> str:
    """Geef eerste regex-match terug, of lege string als geen match."""
    treffer = re.search(patroon, str(waarde))
    return treffer.group(0) if treffer else ""


def _truncate_cel(waarde: str, lengte: int = 120, suffix: str = "…") -> str:
    """Kap een string af op `lengte` tekens voor gebruik in tabelcellen."""
    tekst = str(waarde)
    if len(tekst) <= lengte:
        return tekst
    return tekst[:lengte].rstrip() + suffix


def get_env() -> Environment:
    """Haal de geconfigureerde Jinja2 Environment op (singleton).

    Filters beschikbaar in templates:
    - ``confidence_label``: confidence-string → emoji ('grounded' → '⚖️', anders '🤖')
    - ``slugify``: tekst → URL-slug
    - ``regex_replace``: regex-substitutie
    - ``regex_search``: geeft eerste match terug
    - ``truncate_cel``: kap af op N tekens (default 120) voor tabelcellen

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
        _env.filters["regex_replace"] = _regex_replace
        _env.filters["regex_search"] = _regex_search
        _env.filters["truncate_cel"] = _truncate_cel
    return _env
