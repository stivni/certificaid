r"""Transformer: strip TOC-residu uit ITAA-norm-MDs.

ITAA-normen worden tweekoloms uit PDF geëxtraheerd. De originele inhoudstafel
(meestal pagina 2-3 van het document) verschijnt typisch als een blok
plain-text "dotted-leader"-regels midden in de body:

    ## Inhoudstafel

    Toepassingsgebied .............................................. 6
    Datum van inwerkingtreding ................................. 7
    Definities ......................................................... 8

    ## Toepassingsgebied   ← echte content begint

Of met dash-leaders i.p.v. dots (witwasnorm-geconsolideerd):

    ALGEMENE BEPALINGEN ----------------------------------------- 4
    DEFINITIES --------------------------------------------------- 5

`strip_pdf_page_noise` (extract_norm-chain) strippet individuele
dotted-leader-regels met `\.{4,}\s*\d`. Wat overblijft:

1. De "Inhoudstafel"/"INHOUDSTAFEL"/"Inhoud"-header zelf (zonder dots).
2. TOC-regels met *minder* dan 4 dots, met dashes, of met andere subtielere
   leader-glyphs die niet door de bestaande regex worden gevangen.

Deze transformer detecteert TOC-blokken als clusters van ≥ 3 leader-regels
in een venster, strippet die regels én de eventuele "Inhoudstafel"-header die
ervóór staat. Eén losse leader-regel zonder cluster wordt NIET gestript —
dat kan een legitieme invul-stippellijn zijn (`voor de som van .... euro`).

Conform ADR-005 §1: format-agnostische tekst-transformatie → transformer-laag.
Volgt de signature `(body: str, frontmatter: dict) -> tuple[str, dict]` uit
`tools.etl.transformers.base`.
"""
from __future__ import annotations

import re

# Patroon: leader-glyphs (.../---/___) optioneel met whitespace ertussen,
# gevolgd door whitespace + 1-4 cijfers aan het einde van de regel.
# Minimaal 3 leader-glyphs zodat losse interpunctie (".") buiten beeld blijft.
_LEADER_RE = re.compile(
    r"[\.\-_]{3,}\s+\d{1,4}\s*$",
)

# "Inhoudstafel"-header detectie (case-insensitive maar exact woord-match).
# Vlagt zowel `## Inhoudstafel` als plain-text `INHOUDSTAFEL`/`Inhoud`.
_TOC_HEADER_RE = re.compile(
    r"^(#{1,6}\s+)?(INHOUDSTAFEL|INHOUDSOPGAVE|Inhoudstafel|Inhoudsopgave|Inhoud|TABLE\s+OF\s+CONTENTS|CONTENTS|Contents)\s*$",
)

# Minimum aantal leader-regels in een venster om als TOC-cluster (en
# bijhorende header-strip) te tellen. Eén losse leader-regel wordt nog steeds
# gestript omdat de regex zelf eenduidig genoeg is, maar zonder cluster
# blijft de "Inhoudstafel"-header staan.
_MIN_CLUSTER_SIZE = 3
# Maximum aantal non-leader-non-blank regels tussen leaders in een cluster.
# Iets hoger dan 1 zodat een TOC-blok met een lossse fragment-regel ertussen
# (bv. `I.`, `II.`, `Bijlage 3`) niet ontsnapt — maar laag genoeg om geen body
# in te slokken.
_MAX_GAP_IN_CLUSTER = 2

# Korte TOC-fragmenten tussen header en eerste leader-regel: Romeinse cijfers,
# arabische enkelvoudige opsomming, "Bijlage N", losse hoofdstuk-nummers.
# Worden mee gestript als ze direct vóór een TOC-cluster staan.
_TOC_FRAGMENT_RE = re.compile(
    r"^\s*(?:[IVX]+|\d+\.?|[A-Z]\.?|Bijlage\s+\d+|Annex\s+\d+|Part\s+\d+|Section\s+\d+)\s*$",
    re.I,
)


def _is_leader_line(line: str) -> bool:
    """True als regel een dotted/dashed-leader regel is (TOC-residu)."""
    return bool(_LEADER_RE.search(line))


def _is_blank(line: str) -> bool:
    return not line.strip()


def _find_clusters(lines: list[str]) -> list[tuple[int, int]]:
    """Detecteer clusters van leader-regels.

    Een cluster is een sequentie van ≥ _MIN_CLUSTER_SIZE leader-regels, mogelijk
    onderbroken door ≤ _MAX_GAP_IN_CLUSTER non-leader-non-blank regels (echte
    blanco regels tellen niet als gap — TOC-blokken hebben vaak witregels).

    Returns: lijst van (start_idx, end_idx) ranges (eind exclusief).
    """
    clusters: list[tuple[int, int]] = []
    n = len(lines)
    i = 0
    while i < n:
        if not _is_leader_line(lines[i]):
            i += 1
            continue
        # Begin van mogelijke cluster
        start = i
        last_leader = i
        gap = 0
        count = 1
        j = i + 1
        while j < n:
            if _is_leader_line(lines[j]):
                last_leader = j
                count += 1
                gap = 0
                j += 1
                continue
            if _is_blank(lines[j]):
                # blanks tellen niet als gap maar verlengen ook niet eindeloos:
                # twee opeenvolgende blanks → cluster eindigt
                if j + 1 < n and _is_blank(lines[j + 1]):
                    break
                j += 1
                continue
            # non-leader, non-blank
            gap += 1
            if gap > _MAX_GAP_IN_CLUSTER:
                break
            j += 1
        if count >= _MIN_CLUSTER_SIZE:
            clusters.append((start, last_leader + 1))
        i = max(last_leader + 1, j)
    return clusters


def _expand_cluster_with_header(
    lines: list[str], start: int, end: int,
) -> tuple[int, int]:
    """Breid cluster-range uit naar voor met "Inhoudstafel"-header indien
    aanwezig binnen redelijke afstand, korte TOC-fragmenten (`1.`, `I.`)
    mee opslokken.

    Naar voren: scan terug tot we ofwel een TOC-header vinden (dan mee strippen),
    ofwel een echte body-regel (dan stoppen, behoud `start`). Korte
    TOC-fragmenten (`1.`, `I.`, `Bijlage 3`) worden mee gestript als er
    daarna een header gevonden wordt.

    Naar achteren: hier conservatief — we breiden NIET uit voorbij de laatste
    leader-regel om geen body in te slokken.
    """
    new_start = start
    pending: list[int] = []  # indices van TOC-fragmenten of blanks, mee te
                             # nemen alleen als een header gevonden wordt
    k = start - 1
    max_lookback = 6  # max regels terug (incl. blanks + fragmenten)
    while k >= 0 and (start - k) <= max_lookback:
        line = lines[k]
        if _is_blank(line):
            pending.append(k)
            k -= 1
            continue
        if _TOC_HEADER_RE.match(line.rstrip()):
            # Header gevonden — alles vanaf header tot cluster mee strippen.
            new_start = k
            break
        if _TOC_FRAGMENT_RE.match(line):
            pending.append(k)
            k -= 1
            continue
        # echte body-regel — stop
        break
    return new_start, end


def strip_norm_toc_residue(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip TOC-residu: clusters van dotted/dashed-leader-regels + eventuele
    "Inhoudstafel"-header die ervóór staat.

    Idempotent: tweede pass op de output van een eerste pass geeft hetzelfde
    resultaat.
    """
    if not body:
        return body, frontmatter

    lines = body.split("\n")
    clusters = _find_clusters(lines)
    # Geen cluster én geen losse leader-regels → niets te doen.
    has_solo_leader = any(_is_leader_line(ln) for ln in lines)
    if not clusters and not has_solo_leader:
        return body, frontmatter

    # Bouw set van te verwijderen regel-indices.
    # 1) Per cluster: hele cluster + eventueel uitgebreide header-range.
    # 2) Losse leader-regels (buiten clusters): elke regel die op zichzelf
    #    een leader-pattern is, wordt ook gestript — consistent met
    #    `strip_pdf_page_noise`.
    to_drop: set[int] = set()
    for start, end in clusters:
        new_start, new_end = _expand_cluster_with_header(lines, start, end)
        for idx in range(new_start, new_end):
            to_drop.add(idx)
    for i, ln in enumerate(lines):
        if i in to_drop:
            continue
        if _is_leader_line(ln):
            to_drop.add(i)

    new_lines = [ln for i, ln in enumerate(lines) if i not in to_drop]
    new_body = "\n".join(new_lines)

    # Collapse runs van lege regels die door de strip kunnen ontstaan.
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)

    return new_body, frontmatter
