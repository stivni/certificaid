"""Library voor het splitsen van een KB- of MB-compilatie-MD in losse bodies.

Pure functies — geen filesystem-IO, geen frontmatter-bouw. De caller is
verantwoordelijk voor het lezen van de compilatie-MD en het wegschrijven van
de resultaten.

Grenzen worden gedetecteerd via FOD-page-headers van de vorm
``"FOD Financiën … Btw KB nr. X"`` of ``"FOD Financiën … Btw MB nr. X"``
(waar X een nummer of een datum kan zijn). Aaneengesloten markers met
dezelfde id worden tot één range gevoegd; per id kunnen meerdere
niet-aaneengesloten ranges voorkomen.

De ``kind``-parameter (``"kb"`` of ``"mb"``) bepaalt welk type besluit-header
wordt herkend. KB- en MB-compilaties hebben dezelfde structuur; alleen het
literaal "KB" vs "MB" in de page-header verschilt.
"""
from __future__ import annotations

import re
from collections import OrderedDict
from dataclasses import dataclass, field


_VALID_KINDS = ("kb", "mb")


def _build_fod_header_regex(kind: str) -> re.Pattern[str]:
    """Bouw de FOD-page-header regex voor een gegeven besluit-type.

    Vangt zowel ``"Btw KB nr. 1"`` / ``"Btw MB nr. 1"`` als
    ``"Btw KB 07.06.2007"`` / ``"Btw MB 20.12.2001"``.
    """
    if kind not in _VALID_KINDS:
        raise ValueError(f"kind moet één van {_VALID_KINDS} zijn, kreeg {kind!r}")
    literal = kind.upper()
    return re.compile(
        rf'^FOD Financi.n.+?(?:Btw|BTW)\s+{literal}\s+'
        r'(?:nr\.?\s+(\d+\w*)|(\d{2}[\.\-/]\d{2}[\.\-/]\d{4}))',
        re.I,
    )


# Backwards-compat: KB-default regex (oude naam, oude callers).
_FOD_HEADER = _build_fod_header_regex("kb")


@dataclass
class SplitConfig:
    """Beschrijft één gewenste split (KB of MB).

    Attributes:
        kb_id: besluit-identifier zoals die in de FOD-headers voorkomt
            (bv. ``"1"``, ``"2bis"``, ``"07.06.2007"``). De naam ``kb_id``
            is historisch en wordt voor zowel KB- als MB-splits gebruikt;
            voor MB-splits noteer je in YAML hetzelfde veld (``kb_id``)
            met de MB-id (nummer of datum).
        output: bestandspad voor het resultaat — wordt door de lib alleen
            gebruikt als sleutel in de output-dict, niet om naar te schrijven.
        wet: volledige wetnaam (info-veld voor de caller).
        extra_metadata: vrije bag voor extra frontmatter-info bij de caller.
        skip: wanneer True, slaat de splitter deze split over. Bedoeld voor
            KBs/MBs waarvan een betere individuele bron beschikbaar is (bv.
            JUSTEL-PDF) waardoor de compilatie-versie geskipt moet worden
            zodat we geen dubbele wetteksten in de RAG-index krijgen.
        skip_reason: optionele toelichting waarom deze split skip is.
    """

    kb_id: str
    output: str
    wet: str
    extra_metadata: dict = field(default_factory=dict)
    skip: bool = False
    skip_reason: str = ""


def detect_compilatie_boundaries(
    text: str, kind: str = "kb",
) -> list[tuple[str, int, int]]:
    """Detecteer besluit-grenzen in een KB- of MB-compilatie-tekst.

    Geeft een lijst ``[(besluit_id, start_line, end_line), ...]`` terug —
    niet-overlappend, in volgorde van voorkomen. Aaneengesloten FOD-headers
    met dezelfde id vormen één range; zodra een marker met een andere id
    verschijnt, wordt het vorige segment afgesloten.

    Het eerste segment wordt naar voren uitgebreid tot de eerste echte
    body-regel (na compilatie-frontmatter en H1), zodat content vóór de
    eerste page-marker niet verloren gaat.

    Args:
        text: ruwe pdftotext-output of compilatie-MD-tekst.
        kind: ``"kb"`` voor koninklijke besluiten of ``"mb"`` voor
            ministeriële besluiten — bepaalt welke FOD-page-headers
            herkend worden.
    """
    fod_header = _build_fod_header_regex(kind)
    lines = text.splitlines()
    markers: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = fod_header.match(line.strip())
        if m:
            kb = m.group(1) or m.group(2)
            markers.append((i, kb))

    segments: list[tuple[str, int, int]] = []
    prev_kb: str | None = None
    seg_start: int | None = None
    for i, kb in markers:
        if kb != prev_kb:
            if prev_kb is not None and seg_start is not None:
                segments.append((prev_kb, seg_start, i - 1))
            seg_start = i
            prev_kb = kb
    if prev_kb is not None and seg_start is not None:
        segments.append((prev_kb, seg_start, len(lines) - 1))

    # Eerste KB heeft soms content vóór de eerste page-marker (begin van
    # compilatie-body). Vergroot eerste segment naar de eerste echte
    # body-regel (na frontmatter + H1).
    if segments:
        first_body_line = 0
        in_frontmatter = False
        passed_h1 = False
        for i, line in enumerate(lines):
            s = line.rstrip()
            if i == 0 and s == "---":
                in_frontmatter = True
                continue
            if in_frontmatter and s == "---":
                in_frontmatter = False
                continue
            if in_frontmatter:
                continue
            if s.startswith("# "):
                passed_h1 = True
                continue
            if passed_h1 and s.strip():
                first_body_line = i
                break
        kb_id, _, end = segments[0]
        segments[0] = (kb_id, first_body_line, end)

    return segments


def detect_kb_boundaries(text: str) -> list[tuple[str, int, int]]:
    """Backwards-compat alias — detecteert KB-grenzen specifiek.

    Equivalent met ``detect_compilatie_boundaries(text, kind="kb")``.
    """
    return detect_compilatie_boundaries(text, kind="kb")


def _build_body(lines: list[str], ranges: list[tuple[int, int]]) -> str:
    """Voeg meerdere line-ranges samen tot één body-string."""
    parts: list[str] = []
    for s, e in ranges:
        parts.extend(lines[s:e + 1])
        parts.append("")
    return "\n".join(parts).strip() + "\n"


def split_btw_compilatie(
    text: str,
    splits_config: list[SplitConfig],
    kind: str = "kb",
) -> dict[str, str]:
    """Splits compilatie-tekst in losse besluit-bodies volgens splits_config.

    Voor elke SplitConfig: zoek alle line-ranges met die kb_id, voeg samen
    en geef de body terug onder de ``splits_config.output``-sleutel.
    Bevat geen frontmatter en doet geen filesystem-IO — dat is aan de caller.

    Een id die niet in de tekst voorkomt levert een lege body op
    (``""``) onder zijn output-sleutel.

    Args:
        text: ruwe compilatie-tekst (pdftotext-output of compilatie-MD).
        splits_config: gewenste splits — één per output-bestand.
        kind: ``"kb"`` of ``"mb"`` — bepaalt welk type FOD-page-header
            als boundary-marker wordt herkend.
    """
    lines = text.splitlines()
    boundaries = detect_compilatie_boundaries(text, kind=kind)

    # Groepeer alle ranges per KB-id (volgorde van eerste voorkomen).
    grouped: OrderedDict[str, list[tuple[int, int]]] = OrderedDict()
    for kb, s, e in boundaries:
        grouped.setdefault(kb, []).append((s, e))

    result: dict[str, str] = {}
    for cfg in splits_config:
        ranges = grouped.get(cfg.kb_id, [])
        if not ranges:
            result[cfg.output] = ""
            continue
        result[cfg.output] = _build_body(lines, ranges)
    return result
