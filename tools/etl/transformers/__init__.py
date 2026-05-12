"""
Transformer-laag voor de Certificaid ETL-pipeline (ADR-005 §4).

Elke transformer is een pure functie:
    (body: str, frontmatter: dict) -> tuple[str, dict]

TRANSFORMERS is de centrale registry: {"naam": callable}.
apply_chain() voert een geordende lijst transformers in volgorde uit.
"""
from __future__ import annotations

from tools.etl.transformers.base import TransformerFn
from tools.etl.transformers.cleanup_basics import cleanup_basics
from tools.etl.transformers.inject_headings_wettekst import inject_headings_wettekst
from tools.etl.transformers.organize_headings import organize_headings
from tools.etl.transformers.emit_frontmatter import emit_frontmatter

TRANSFORMERS: dict[str, TransformerFn] = {
    "cleanup_basics": cleanup_basics,
    "inject_headings_wettekst": inject_headings_wettekst,
    "organize_headings": organize_headings,
    "emit_frontmatter": emit_frontmatter,
}


def apply_chain(
    body: str,
    frontmatter: dict,
    chain: list[str],
) -> tuple[str, dict]:
    """Voer een chain van transformers in volgorde uit.

    Args:
        body: markdown-body (zonder frontmatter-blok).
        frontmatter: huidige frontmatter als plain dict (wordt doorgegeven
            en kan door elke transformer worden gewijzigd).
        chain: geordende lijst van transformer-namen (sleutels in TRANSFORMERS).

    Returns:
        (body, frontmatter) na alle transformers toegepast.

    Raises:
        ValueError: als een chain-naam niet in TRANSFORMERS staat.
    """
    for name in chain:
        fn = TRANSFORMERS.get(name)
        if fn is None:
            raise ValueError(
                f"Onbekende transformer: {name!r}. "
                f"Beschikbaar: {sorted(TRANSFORMERS)}"
            )
        body, frontmatter = fn(body, frontmatter)
    return body, frontmatter
