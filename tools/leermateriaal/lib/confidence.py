"""
Confidence-label helpers voor leermateriaal-rendering (ADR-007 §confidence-labels).

Confidence-waarden zijn string-tags in JSON-data; emoji zijn UI-/render-conventie.
"""

from __future__ import annotations

# Volgorde: meest "geankerd" eerst
MODE_CONFIDENCE_PRIORITY: list[str] = [
    "grounded",
    "inferred-from-aggregation",
    "inferred",
]

_LABEL_MAP: dict[str, str] = {
    "grounded": "⚖️",
    "inferred-from-aggregation": "🤖",
    "inferred": "🤖",
}

# Velden op record-niveau die een confidence-waarde kunnen dragen
_CONFIDENCE_VELDEN: list[str] = [
    "definitie",
    "main_rule",
    "verplichting",
    "doel",
]


def label(confidence: str) -> str:
    """Geef het emoji-label voor een confidence-waarde.

    Args:
        confidence: 'grounded', 'inferred-from-aggregation' of 'inferred'

    Returns:
        '⚖️' voor grounded, '🤖' voor alles anders
    """
    return _LABEL_MAP.get(confidence, "🤖")


def mode_confidence(record: dict) -> str:
    """Bepaal de meest conservatieve (meest geankerde) confidence-waarde voor een record.

    Kijkt naar de confidence van het type-specifieke hoofdveld (definitie,
    main_rule, verplichting, doel). Geeft de meest geankerde terug.

    Args:
        record: volledig concept-record dict

    Returns:
        confidence-string ('grounded' | 'inferred-from-aggregation' | 'inferred')
    """
    gevonden: list[str] = []
    for veld in _CONFIDENCE_VELDEN:
        blok = record.get(veld)
        if isinstance(blok, dict):
            conf = blok.get("confidence", "")
            if conf in MODE_CONFIDENCE_PRIORITY:
                gevonden.append(conf)

    if not gevonden:
        return "inferred"

    # Meest geankerde = laagste index in prioriteitslijst
    return min(gevonden, key=lambda c: MODE_CONFIDENCE_PRIORITY.index(c))


def inline(text: str, confidence: str) -> str:
    """Combineer tekst met inline confidence-label.

    Args:
        text: de tekst
        confidence: confidence-waarde

    Returns:
        '{text} {emoji}'
    """
    return f"{text} {label(confidence)}"
