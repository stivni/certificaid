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
# `[IVX]+\.?` dekt ook `II.`, `III.` enz. (Romein-nummers met afsluitende punt).
_TOC_FRAGMENT_RE = re.compile(
    r"^\s*(?:[IVX]+\.?|\d+\.?|[A-Z]\.?|Bijlage\s+\d+|Annex\s+\d+|Part\s+\d+|Section\s+\d+)\s*$",
    re.I,
)

# Leaderless TOC-entries: regels die TOC-residu zijn maar zonder klassieke
# dotted/dashed-leaders. Twee subpatronen:
#
# Sub-patroon A — eindigt op ` . <getal>` (spatie-punt-spatie-getal), eventueel
#   gevolgd door één of meer extra woorden (bv. `... . 34 Het`):
#   "Organisatie van de beroepsbeoefenaar ... . 7"
#   "Bijlage 1 – Voorbeeld van opdrachtbrief ... . 33"
#   "## Communicatie met het management ... . 34 Het"
# Sub-patroon B — multi-spatie-leaders: ≥3 opeenvolgende spaties midden in de
#   regel (pdftotext-layout-artifact bij kolom-gebaseerde TOC-inzet):
#   "Nakoming    van       de         waakzaamheidsverplichtingen..."
#   Herkenbaar doordat het patroon \w+\s{3,}\w+ aanwezig is.
#
# CONSERVATIEF: dit patroon wordt ALLEEN gebruikt in het venster tussen een
# Inhoudstafel-label en de eerste echte ## heading (zie _strip_leaderless_toc_block).
# Buiten dat venster nooit aanraken — anders false-positives op body-tekst.
_LEADERLESS_TOC_PAGINA_RE = re.compile(
    r"\s+\.\s+\d{1,3}(?:\s+\S+)*\s*$",
)

_MULTI_SPACE_LEADER_RE = re.compile(
    r"\w\s{3,}\w",
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


def _is_real_heading(line: str) -> bool:
    """True als de regel een echte markdown ## heading is (geen TOC-entry).

    Een TOC-entry als `## Communicatie ... . 34 Het` is een heading *met*
    paginanummer-suffix — wordt hier als NIET-echte heading beschouwd zodat
    het mee gestript kan worden vanuit een leaderless-TOC-blok.
    Een echte heading als `## Toepassingsgebied` bevat geen paginanummer.
    """
    if not line.lstrip().startswith("#"):
        return False
    # Heading met paginanummer-suffix is een TOC-entry, geen echte heading.
    # Patroon: regel eindigt op ` . <getal>` (optioneel gevolgd door tekst)
    # of op ` <getal>` na ruimte.
    if _LEADERLESS_TOC_PAGINA_RE.search(line):
        return False
    return True


def _is_leaderless_toc_entry(line: str) -> bool:
    """True als de regel een leaderless TOC-entry is.

    Detecteert twee sub-patronen:
    - Paginanummer-suffix: eindigt op ` . <getal>` of op ruimte + getal.
    - Multi-spatie-leaders: ≥3 opeenvolgende spaties midden in de tekst
      (pdftotext-artifact voor kolom-gebaseerde TOC-layout).
    - Losse Bijlage/Annex/Appendix items gevolgd door paginanummer.

    NOOIT aanroepen buiten een Inhoudstafel-venster — te generiek voor body-tekst.
    """
    stripped = line.strip()
    if not stripped:
        return False
    # Sub-patroon A: eindigt op paginanummer
    if _LEADERLESS_TOC_PAGINA_RE.search(line):
        return True
    # Sub-patroon B: multi-spatie-leaders (≥3 spaties tussen woorden)
    if _MULTI_SPACE_LEADER_RE.search(stripped):
        return True
    return False


# Maximum aantal regels vooruit te scannen voor de eerste echte heading
# nadat een Inhoudstafel-label gevonden is.
_MAX_LEADERLESS_TOC_SCAN = 50


def _is_toc_entry_in_window(line: str) -> bool:
    """True als de regel een TOC-entry is binnen een Inhoudstafel-venster.

    Herkent:
    - Klassieke dotted/dashed-leader-regels.
    - Leaderless TOC-entries (paginanummer-suffix, multi-spatie-leaders).
    - Klassieke korte TOC-fragmenten (Romein-nummers, `Bijlage N`, enz.).
    - Headings met paginanummer-suffix (die TOC-entries zijn, geen echte headings).
    """
    if _is_leader_line(line):
        return True
    if _is_leaderless_toc_entry(line):
        return True
    if _TOC_FRAGMENT_RE.match(line):
        return True
    # Heading-met-paginanummer (TOC-entry gepromoveerd tot ## heading)
    if line.lstrip().startswith("#") and _LEADERLESS_TOC_PAGINA_RE.search(line):
        return True
    return False


def _is_body_paragraph(line: str) -> bool:
    """True als de regel een echte body-paragraaf is die NIET gestript mag worden.

    Onderscheidt body-tekst van TOC-fragmenten in het Inhoudstafel-venster.
    Conservatief: geeft False terug bij twijfel (liever iets te veel strippen
    in een bewezen TOC-context dan body-tekst verliezen).

    Niet als body-paragraaf beschouwd (= mag gestript worden in TOC-venster):
    - Blanco regels.
    - Klassieke TOC-entries (leader-regels, leaderless paginanummer, multi-spatie).
    - Korte TOC-fragmenten (Romein, arabisch, Bijlage N, enz.).
    - Elke regel die begint met een heading-prefix (#).

    Wél als body-paragraaf beschouwd (= NIET strippen):
    - Een regel die begint met een kleine letter of een cijfer gevolgd door tekst
      die GEEN paginanummer-patroon heeft én GEEN multi-spatie-leader heeft —
      alleen als de regel minstens ~40 tekens lang is (lange zin, geen TOC-label).
    - Elke regel die begint met bijv. 'De ', 'Het ', 'Een ', 'Overeenkomstig',
      'Conform', 'Ingevolge', 'Dit ' — typische body-zinnen in ITAA-normen.
    """
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith("#"):
        return False
    if _is_leader_line(line):
        return False
    if _is_leaderless_toc_entry(line):
        return False
    if _TOC_FRAGMENT_RE.match(stripped):
        return False
    # Bijlage-entry met langere tekst (maar geen paginanummer): valt ook onder TOC.
    # Herkenbaar als: begint met "Bijlage" of "Annex" of "BIJLAGE" + rest tekst.
    if re.match(r"^\s*(?:Bijlage|BIJLAGE|Annex|ANNEX)\b", line):
        return False
    # Sectie-genummerde TOC-entries zoals "II.4. Specifieke bepalingen..."
    if re.match(r"^\s*(?:[IVX]+|\d+)[\.\:]\d*\.?\s+\S", line):
        return False
    # Bereik tot hier: vermoedelijk een echte body-paragraaf.
    return True


def _find_leaderless_toc_blocks(lines: list[str]) -> list[tuple[int, int]]:
    """Detecteer TOC-blokken zonder klassieke dotted/dashed-leaders.

    Een leaderless TOC-blok bestaat uit:
    1. Een Inhoudstafel-header-regel (_TOC_HEADER_RE match).
    2. Regels erna (≤ _MAX_LEADERLESS_TOC_SCAN) die GEEN echte body-paragraaf
       zijn: blanco, TOC-entries, headings met paginanummer, korte fragmenten.
    3. Grens: de eerste echte ## heading (zonder paginanummer-suffix) OF een
       echte body-paragraaf.

    Conservatief: wordt ALLEEN gestript als er minstens één herkenbare
    TOC-entry in het venster staat NA de header. Als de eerste niet-lege regel
    al een echte body-paragraaf is, blijft de Inhoudstafel-header ook staan.

    Returns: lijst van (start_idx, end_idx) ranges (eind exclusief) die
    gestript moeten worden.
    """
    blocks: list[tuple[int, int]] = []
    n = len(lines)
    i = 0
    while i < n:
        if not _TOC_HEADER_RE.match(lines[i].rstrip()):
            i += 1
            continue
        # Inhoudstafel-label gevonden op positie i.
        toc_header_idx = i
        scan_limit = min(n, toc_header_idx + 1 + _MAX_LEADERLESS_TOC_SCAN)
        j = toc_header_idx + 1

        # Eerste niet-lege regel na de header bepaalt of we strippen.
        first_real_line_is_body = False
        jj = j
        while jj < scan_limit:
            line = lines[jj]
            if _is_blank(line):
                jj += 1
                continue
            if _is_real_heading(line):
                # Directe echte heading na Inhoudstafel-label:
                # strip het label (lege inhoudsopgave-sectie).
                break
            if _is_body_paragraph(line):
                first_real_line_is_body = True
            break

        if first_real_line_is_body:
            # Eerste niet-lege niet-heading regel is body-tekst → behoud.
            i += 1
            continue

        # Scan voorwaarts voor de eerste echte heading.
        end_idx = toc_header_idx + 1  # default: strip alleen header
        found_real_heading = False
        while j < scan_limit:
            line = lines[j]
            if _is_real_heading(line):
                end_idx = j
                found_real_heading = True
                break
            if _is_body_paragraph(line):
                # Echte body-paragraaf in het venster → stop.
                end_idx = j
                break
            j += 1
        if not found_real_heading and end_idx == toc_header_idx + 1:
            # Conservatief: als er geen echte heading gevonden werd en geen
            # body-paragraaf, strip alleen de header-regel zelf.
            pass
        blocks.append((toc_header_idx, end_idx))
        i = end_idx
    return blocks


def _find_orphan_leaderless_toc_lines(lines: list[str]) -> set[int]:
    """Detecteer losse leaderless TOC-entries die buiten een Inhoudstafel-venster staan.

    Een "weesvogel" leaderless TOC-entry is:
    - Een regel die `_is_leaderless_toc_entry` triggert (paginanummer-suffix of
      multi-spatie-leaders).
    - De directe voorganger (de vorige niet-lege regel) is GEEN echte body-paragraaf.
    - De directe opvolger (de volgende niet-lege regel) is GEEN echte body-paragraaf.

    Dit dekt het patroon in aww-richtlijn-bibf:
      `...aanmerkstekst...`  (body)
      `<blank>`
      `Organisatie ... . 7`  ← directe voorganger is de blanco → geen body
      `<blank>`
      `## heading`           ← directe opvolger is heading → geen body
      `Nakoming    van...`   ← direct na heading (geen blanco) → heading voor

    CONSERVATIEF: controleer de directe niet-lege buurregels (niet verder terug).
    Als zowel de vorige als de volgende niet-lege regel geen body-paragraaf is,
    wordt de TOC-entry gestript.
    """
    to_drop: set[int] = set()
    n = len(lines)

    def prev_nonblank(idx: int) -> str:
        """Geef de vorige niet-lege regel terug (of lege string als niet bestaat)."""
        for k in range(idx - 1, -1, -1):
            if lines[k].strip():
                return lines[k]
        return ""

    def next_nonblank(idx: int) -> str:
        """Geef de volgende niet-lege regel terug (of lege string als niet bestaat)."""
        for k in range(idx + 1, n):
            if lines[k].strip():
                return lines[k]
        return ""

    for i, line in enumerate(lines):
        if not _is_leaderless_toc_entry(line):
            continue
        # Vorige niet-lege regel mag geen echte body-paragraaf zijn.
        if _is_body_paragraph(prev_nonblank(i)):
            continue
        # Volgende niet-lege regel mag geen echte body-paragraaf zijn.
        if _is_body_paragraph(next_nonblank(i)):
            continue
        to_drop.add(i)
    return to_drop


def strip_norm_toc_residue(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip TOC-residu: clusters van dotted/dashed-leader-regels + eventuele
    "Inhoudstafel"-header die ervóór staat. Tevens standalone Inhoudstafel-labels
    zonder dotted-leaders + leaderless TOC-entries in het venster erna, plus
    wees-TOC-entries (leaderless entries die buiten een Inhoudstafel-venster staan).

    Idempotent: tweede pass op de output van een eerste pass geeft hetzelfde
    resultaat.
    """
    if not body:
        return body, frontmatter

    lines = body.split("\n")
    to_drop: set[int] = set()

    # --- Stap 1: leaderless TOC-blokken (nieuwe extensie) ---
    # Dit loopt VOOR de cluster-detectie zodat Inhoudstafel-labels zonder
    # dotted-leaders ook worden opgepikt.
    for start, end in _find_leaderless_toc_blocks(lines):
        for idx in range(start, end):
            to_drop.add(idx)

    # --- Stap 2: wees-leaderless TOC-entries (nieuwe extensie) ---
    # Losse TOC-entries zonder Inhoudstafel-context, omringd door headings/blanks.
    to_drop.update(_find_orphan_leaderless_toc_lines(lines))

    # --- Stap 3: klassieke cluster-detectie (bestaande logica) ---
    clusters = _find_clusters(lines)
    has_solo_leader = any(_is_leader_line(ln) for ln in lines)

    if clusters or has_solo_leader:
        for start, end in clusters:
            new_start, new_end = _expand_cluster_with_header(lines, start, end)
            for idx in range(new_start, new_end):
                to_drop.add(idx)
        for i, ln in enumerate(lines):
            if i in to_drop:
                continue
            if _is_leader_line(ln):
                to_drop.add(i)

    if not to_drop:
        return body, frontmatter

    new_lines = [ln for i, ln in enumerate(lines) if i not in to_drop]
    new_body = "\n".join(new_lines)

    # Collapse runs van lege regels die door de strip kunnen ontstaan.
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)

    return new_body, frontmatter
