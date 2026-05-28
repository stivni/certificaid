"""
Wikilink-generatie voor Quartz-compatibele Obsidian-stijl links (ADR-007 §aspect-anker).

Alle links volgen het patroon [[pad|label]] of [[pad]].
Quartz lost [[id]] op als relatieve link naar content/<map>/<id>.md.
"""

from __future__ import annotations

import re
import unicodedata


def slugify(text: str) -> str:
    """Converteer tekst naar een URL-vriendelijke slug.

    - Lowercase
    - Accenten strippen (NFD decomposition + filter)
    - Non-alphanum (behalve koppeltekens) → koppelteken
    - Dubbele koppeltekens samenvoegen
    - Leading/trailing koppeltekens verwijderen

    Args:
        text: invoertekst, bv. "Boekhoudkundige verwerking"

    Returns:
        slug, bv. "boekhoudkundige-verwerking"
    """
    # Normaliseer naar NFD voor accent-stripping
    genormaliseerd = unicodedata.normalize("NFD", text.lower())
    # Filter combining characters (accenten) weg
    zonder_accenten = "".join(
        c for c in genormaliseerd if unicodedata.category(c) != "Mn"
    )
    # Vervang non-alphanumerieke tekens (behalve koppelteken) door koppelteken
    slug = re.sub(r"[^a-z0-9\-]+", "-", zonder_accenten)
    # Samenvoegen van dubbele koppeltekens
    slug = re.sub(r"-{2,}", "-", slug)
    # Strip leading/trailing koppeltekens
    return slug.strip("-")


def concept_link(record_id: str, label: str | None = None) -> str:
    """Genereer een wikilink naar een concept-fiche.

    Args:
        record_id: het record-id, bv. 'controle'
        label: optioneel weergavelabel

    Returns:
        '[[controle|Controle]]' of '[[controle]]'
    """
    if label:
        return f"[[{record_id}|{label}]]"
    return f"[[{record_id}]]"


def concept_aspect_link(
    record_id: str, anker_slug: str, label: str | None = None
) -> str:
    """Genereer een wikilink naar een specifiek aspect-anker op een concept-fiche.

    Args:
        record_id: het record-id, bv. 'leasing'
        anker_slug: de anker-slug, bv. 'boekhoudkundige-verwerking'
        label: optioneel weergavelabel

    Returns:
        '[[leasing#boekhoudkundige-verwerking|Boekhoudkundige verwerking]]'
        of '[[leasing#boekhoudkundige-verwerking]]'
    """
    pad = f"{record_id}#{anker_slug}"
    if label:
        return f"[[{pad}|{label}]]"
    return f"[[{pad}]]"


