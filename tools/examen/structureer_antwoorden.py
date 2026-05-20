"""Structureer platte modelantwoorden naar typed `correct_antwoord_blokken[]` (ADR-023).

STRICT no new content: deze tool is een **deterministische parser**. Hij leest
`correct_antwoord` (string) + `antwoord_motivering` (markdown-string) per vraag
(en subvraag) en splitst de tekst in typed blokken volgens de 9 blok-types uit
ADR-023:

- `boeking` — Debet/Credit-codeblock of inline regels
- `tabel` — markdown-tabel
- `definitie` — lemma + definitie-zin (bij antwoord_type='definitie')
- `procedure` — genummerde stappen (bij antwoord_type='procedure')
- `opsomming` — genummerde lijst met bold lemma's
- `berekening` — formule + cijfer-uitwerking
- `conclusie` — slot-conclusie / MC-keuze
- `grondslag` — afsluit-alinea `_Grondslag: ..._`
- `motivatie` — fallback voor restant-paragrafen

Geen LLM-call, geen externe kennis. Bij twijfel valt het hele antwoord terug op
één `motivatie`-blok met de volledige `antwoord_motivering` als inhoud.

CLI:
    python3 -m tools.examen.structureer_antwoorden                # alle examens
    python3 -m tools.examen.structureer_antwoorden --examen 2014-1
    python3 -m tools.examen.structureer_antwoorden --dry-run
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent
EXAMEN_DIR = BASE_DIR / "data" / "programma" / "examen_vragen"

# ---------------------------------------------------------------------------
# Pattern-detectoren (deterministische regex)
# ---------------------------------------------------------------------------

# Codeblock met boeking
_PAT_CODE_FENCE = re.compile(r"```([^`]*?)```", re.DOTALL)
# Boekings-regel: zijde + rekening + naam + bedrag
_PAT_BOEKING_REGEL = re.compile(
    r"^\s*(Debet|Credit|D|C)\s*:?\s*(\d{2,6})\s+([^\d\n]{2,80}?)\s*(?:€|EUR|euro)?\s*"
    r"(\d{1,3}(?:[.\s]\d{3})*(?:,\d{2})?|\d+,\d{2})\s*(?:€|EUR|euro)?\s*$",
    re.IGNORECASE | re.MULTILINE,
)

# Inline variant — staat midden in een lopende zin, niet aan regelbegin
_PAT_BOEKING_INLINE = re.compile(
    r"\b(Debet|Credit|D|C)\s*:?\s*(\d{2,6})\s+([^\d\n]{2,80}?)\s*(?:€|EUR|euro)?\s*"
    r"(\d{1,3}(?:[.\s]\d{3})*(?:,\d{2})?|\d+,\d{2})",
    re.IGNORECASE,
)
# Markdown-tabel: minstens 2 rijen (kop + sep + data)
_PAT_TABEL = re.compile(
    r"(?:^|\n)\s*(\|[^\n]+\|)\s*\n\s*(\|[-:|\s]+\|)\s*\n((?:\s*\|[^\n]*\|\s*\n?)+)",
    re.MULTILINE,
)
# Grondslag-afsluit-alinea
_PAT_GRONDSLAG = re.compile(r"_Grondslag:\s*([^_\n]+?)_", re.IGNORECASE)
# Genummerde bold-lemma lijst-item
_PAT_OPSOMMING_ITEM = re.compile(
    r"^\s*(\d+)\.\s+\*\*([^*\n]+?)\*\*\s*(?:[—–\-:]\s*)?(.*?)(?=\n\s*\d+\.\s+\*\*|\n\n|\Z)",
    re.MULTILINE | re.DOTALL,
)
# Conclusie/Antwoord-kop
_PAT_CONCLUSIE = re.compile(
    r"\*\*(Conclusie|Antwoord|Eindantwoord)[:\s]+\*?\*?\s*([^*\n]+)",
    re.IGNORECASE,
)
# Confidence-markers
_PAT_GROUNDED = re.compile(r"⚖️")
_PAT_INFERRED = re.compile(r"🤖")


def _detecteer_confidence(tekst: str) -> Optional[str]:
    """Return 'grounded'/'inferred'/None op basis van markers in tekst."""
    heeft_grounded = bool(_PAT_GROUNDED.search(tekst))
    heeft_inferred = bool(_PAT_INFERRED.search(tekst))
    if heeft_grounded and not heeft_inferred:
        return "grounded"
    if heeft_inferred and not heeft_grounded:
        return "inferred"
    if heeft_grounded and heeft_inferred:
        # Bij mix: dominant is inferred (conservatief)
        return "inferred"
    return None


def _parse_bedrag(s: str) -> Optional[float]:
    """Belgisch bedrag-formaat → float. Hergebruik van _v3_blok_detectoren-logica."""
    if not s:
        return None
    s = s.strip().replace(" ", "")
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    else:
        s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Blok-extractoren — elk levert (blok-dict, gebruikte_tekst-range) of None
# ---------------------------------------------------------------------------

_PAT_BULLET_BOEKING = re.compile(
    r"^\s*-\s+(?:\*\*)?(Debet|Credit|D|C)(?:\*\*)?\s*:?\s*(\d{2,6})\s+([^\d\n]{2,120}?)\s*(?:€|EUR|euro)?\s*"
    r"(\d{1,3}(?:[.\s]\d{3})*(?:,\d{2})?|\d+,\d{2})\s*(?:€|EUR|euro)?\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def _extraheer_boekingen(motivering: str) -> tuple[list[dict[str, Any]], str]:
    """Vind boekingen (codeblocks + inline + bullets) en lever per-blok een record.

    Returns: (boeking-blokken, motivering-zonder-boekings-tekst).
    """
    blokken: list[dict[str, Any]] = []
    bewaarde_ranges: list[tuple[int, int]] = []

    # 1) Codeblock-boekingen
    for m in _PAT_CODE_FENCE.finditer(motivering):
        body = m.group(1)
        regels = _parse_boekings_regels(body)
        if regels:
            confidence = _detecteer_confidence(body)
            # Context: probeer header vlak vóór codeblock
            context = _zoek_codeblock_context(motivering, m.start())
            blok: dict[str, Any] = {"type": "boeking", "regels": regels, "eenheid": "EUR"}
            if context:
                blok["context"] = context
            if confidence:
                blok["confidence"] = confidence
            blokken.append(blok)
            bewaarde_ranges.append((m.start(), m.end()))

    # 1b) Bullet-list-boekingen (`- Debet X € 100 / - Credit Y € 100`)
    bullet_matches = list(_PAT_BULLET_BOEKING.finditer(motivering))
    bullet_matches = [m for m in bullet_matches
                      if not any(s <= m.start() < e for s, e in bewaarde_ranges)]
    if len(bullet_matches) >= 2:
        groep: list = []
        for m in bullet_matches:
            if not groep:
                groep.append(m)
                continue
            gap_tekst = motivering[groep[-1].end():m.start()]
            heeft_header = bool(re.search(r"(?:^|\n)###\s+", gap_tekst))
            heeft_bold_kop = bool(re.search(r"\n\n\s*\*\*[A-Z]", gap_tekst))
            if (
                not heeft_header
                and not heeft_bold_kop
                and len(gap_tekst) < 80  # bullets staan dicht bij elkaar
            ):
                groep.append(m)
            else:
                if len(groep) >= 2:
                    _voeg_bullet_boeking_toe(groep, motivering, blokken, bewaarde_ranges)
                groep = [m]
        if len(groep) >= 2:
            _voeg_bullet_boeking_toe(groep, motivering, blokken, bewaarde_ranges)

    # 2) Inline boekings-regel-paren (Debet X / Credit Y) buiten codeblocks
    # Strategie: vind alle matches, groepeer opeenvolgende (D dan C of vv.) tot één boeking
    # Skip ranges binnen reeds-gevangen codeblocks. Splits groepen op
    # ### Stap-headers en op `**bold**`-headers (context-grenzen).
    inline_matches = list(_PAT_BOEKING_INLINE.finditer(motivering))
    inline_matches = [m for m in inline_matches
                      if not any(s <= m.start() < e for s, e in bewaarde_ranges)]
    if len(inline_matches) >= 2:
        # Groepeer aaneengesloten (gap < 200 chars) en zonder ### header tussenin
        groep: list = []
        for m in inline_matches:
            if not groep:
                groep.append(m)
                continue
            gap_tekst = motivering[groep[-1].end():m.start()]
            # Splits-grens: ### header of dubbele newline + ** kop
            heeft_header = bool(re.search(r"(?:^|\n)###\s+", gap_tekst))
            heeft_bold_section_kop = bool(
                re.search(r"\n\n\s*\*\*[A-Z]", gap_tekst)
            )
            if (
                not heeft_header
                and not heeft_bold_section_kop
                and len(gap_tekst) < 200
            ):
                groep.append(m)
            else:
                if len(groep) >= 2:
                    _voeg_inline_boeking_toe(groep, motivering, blokken, bewaarde_ranges)
                groep = [m]
        if len(groep) >= 2:
            _voeg_inline_boeking_toe(groep, motivering, blokken, bewaarde_ranges)

    # Strip de gevangen ranges uit de motivering
    if bewaarde_ranges:
        bewaarde_ranges.sort()
        stukken: list[str] = []
        cursor = 0
        for s, e in bewaarde_ranges:
            stukken.append(motivering[cursor:s])
            cursor = e
        stukken.append(motivering[cursor:])
        rest = "".join(stukken)
    else:
        rest = motivering
    return blokken, rest


def _parse_boekings_regels(body: str) -> list[dict[str, Any]]:
    """Parse de body van een codeblock naar boekings-regels."""
    regels: list[dict[str, Any]] = []
    for m in _PAT_BOEKING_REGEL.finditer(body):
        zijde_raw = m.group(1).upper()[0]  # "D" of "C"
        rek = m.group(2)
        naam = m.group(3).strip().rstrip(":,;")
        bedrag = _parse_bedrag(m.group(4))
        if bedrag is None or not naam:
            continue
        regels.append({
            "zijde": zijde_raw,
            "rekening": rek,
            "naam": naam,
            "bedrag": bedrag,
        })
    return regels


def _zoek_codeblock_context(motivering: str, code_start: int) -> Optional[str]:
    """Zoek een ### Stap-X / **Bij ...**-header vlak vóór het codeblock."""
    voor = motivering[max(0, code_start - 300):code_start]
    # Laatst-voorkomende h3-kop
    h3 = re.findall(r"^###\s+(.+?)$", voor, re.MULTILINE)
    if h3:
        return h3[-1].strip()
    # Of een bold-kop
    bold = re.findall(r"\*\*([^*\n]{3,80})\*\*\s*:?\s*$", voor, re.MULTILINE)
    if bold:
        return bold[-1].strip()
    return None


def _voeg_bullet_boeking_toe(
    groep: list,
    motivering: str,
    blokken: list[dict[str, Any]],
    bewaarde_ranges: list[tuple[int, int]],
) -> None:
    regels = []
    for m in groep:
        zijde_raw = m.group(1).upper()[0]
        rek = m.group(2)
        naam = m.group(3).strip().rstrip(":,;")
        bedrag = _parse_bedrag(m.group(4))
        if bedrag is None or not naam:
            continue
        regels.append({"zijde": zijde_raw, "rekening": rek, "naam": naam, "bedrag": bedrag})
    if not regels:
        return
    blok: dict[str, Any] = {"type": "boeking", "regels": regels, "eenheid": "EUR"}
    # Context: zoek vóór de eerste bullet
    context = _zoek_codeblock_context(motivering, groep[0].start())
    if context:
        blok["context"] = context
    span = motivering[groep[0].start():groep[-1].end()]
    confidence = _detecteer_confidence(span)
    if confidence:
        blok["confidence"] = confidence
    blokken.append(blok)
    bewaarde_ranges.append((groep[0].start(), groep[-1].end()))


def _voeg_inline_boeking_toe(
    groep: list[re.Match],
    motivering: str,
    blokken: list[dict[str, Any]],
    bewaarde_ranges: list[tuple[int, int]],
) -> None:
    regels = []
    for m in groep:
        zijde_raw = m.group(1).upper()[0]
        rek = m.group(2)
        naam = m.group(3).strip().rstrip(":,;")
        bedrag = _parse_bedrag(m.group(4))
        if bedrag is None or not naam:
            continue
        regels.append({"zijde": zijde_raw, "rekening": rek, "naam": naam, "bedrag": bedrag})
    if not regels:
        return
    blok: dict[str, Any] = {"type": "boeking", "regels": regels, "eenheid": "EUR"}
    # Confidence van het hele groeps-fragment
    span = motivering[groep[0].start():groep[-1].end()]
    confidence = _detecteer_confidence(span)
    if confidence:
        blok["confidence"] = confidence
    blokken.append(blok)
    bewaarde_ranges.append((groep[0].start(), groep[-1].end()))


def _extraheer_tabellen(motivering: str) -> tuple[list[dict[str, Any]], str]:
    """Vind markdown-tabellen → tabel-blokken."""
    blokken: list[dict[str, Any]] = []
    bewaarde_ranges: list[tuple[int, int]] = []
    for m in _PAT_TABEL.finditer(motivering):
        kop_regel = m.group(1)
        data_regels = m.group(3)
        headers = [c.strip() for c in kop_regel.strip().strip("|").split("|")]
        rows: list[list[str]] = []
        for ln in data_regels.strip().split("\n"):
            ln = ln.strip()
            if not ln.startswith("|"):
                continue
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cells) == len(headers):
                rows.append(cells)
        if not rows:
            continue
        # Confidence over het tabel-fragment
        confidence = _detecteer_confidence(m.group(0))
        blok: dict[str, Any] = {"type": "tabel", "headers": headers, "rows": rows}
        if confidence:
            blok["confidence"] = confidence
        blokken.append(blok)
        bewaarde_ranges.append((m.start(), m.end()))

    if bewaarde_ranges:
        bewaarde_ranges.sort()
        stukken: list[str] = []
        cursor = 0
        for s, e in bewaarde_ranges:
            stukken.append(motivering[cursor:s])
            cursor = e
        stukken.append(motivering[cursor:])
        rest = "".join(stukken)
    else:
        rest = motivering
    return blokken, rest


def _extraheer_grondslag(motivering: str) -> tuple[Optional[dict[str, Any]], str]:
    """Vind de _Grondslag:..._-afsluit-alinea."""
    m = _PAT_GRONDSLAG.search(motivering)
    if not m:
        return None, motivering
    bronnen_raw = m.group(1).strip().rstrip(".")
    # Split op ; of , — maar wees zorgvuldig met komma's in artikel-lijsten
    # ("KB WVV art. 3:130, lid 1" mag niet gesplitst worden op die komma)
    # Vuistregel: split alleen op ; en op " en " als verbindingswoord
    bronnen = [b.strip() for b in re.split(r";|\s+en\s+(?=[A-Z])", bronnen_raw) if b.strip()]
    if not bronnen:
        bronnen = [bronnen_raw]
    blok = {"type": "grondslag", "bronnen": bronnen}
    rest = motivering[:m.start()] + motivering[m.end():]
    return blok, rest


def _extraheer_opsomming(motivering: str, antwoord_type: Optional[str]) -> tuple[Optional[dict[str, Any]], str]:
    """Bij antwoord_type='opsomming' (of als opsomming-lijst duidelijk dominant
    is) extract genummerde bold-items.
    """
    items: list[dict[str, Any]] = []
    laatste_eind = 0
    eerste_start: Optional[int] = None
    for m in _PAT_OPSOMMING_ITEM.finditer(motivering):
        if eerste_start is None:
            eerste_start = m.start()
        lemma = m.group(2).strip()
        toelichting = m.group(3).strip()
        confidence = _detecteer_confidence(m.group(0))
        item: dict[str, Any] = {"lemma": lemma}
        if toelichting:
            # Strip trailing ⚖️/🤖-marker want die zit al in confidence
            toelichting_clean = re.sub(r"\s*[⚖️🤖]+\s*$", "", toelichting).strip()
            if toelichting_clean:
                item["toelichting"] = toelichting_clean
        if confidence:
            item["confidence"] = confidence
        items.append(item)
        laatste_eind = m.end()
    if len(items) < 2:
        return None, motivering
    # Alleen als antwoord_type expliciet opsomming is, OF als de items
    # zo dominant zijn dat ze het hele motivering-stuk vullen
    relevant = antwoord_type == "opsomming"
    if not relevant and eerste_start is not None:
        # Check of items > 50% van motivering bedekken
        bedekking = (laatste_eind - eerste_start) / max(1, len(motivering))
        relevant = bedekking > 0.5
    if not relevant:
        return None, motivering
    blok = {"type": "opsomming", "items": items}
    rest = motivering[:eerste_start] + motivering[laatste_eind:]
    return blok, rest


def _extraheer_procedure(motivering: str, antwoord_type: Optional[str]) -> tuple[Optional[dict[str, Any]], str]:
    """Bij antwoord_type='procedure' extract genummerde stappen."""
    if antwoord_type != "procedure":
        return None, motivering
    stappen: list[dict[str, Any]] = []
    laatste_eind = 0
    eerste_start: Optional[int] = None
    for m in _PAT_OPSOMMING_ITEM.finditer(motivering):
        if eerste_start is None:
            eerste_start = m.start()
        nummer = int(m.group(1))
        kop = m.group(2).strip()
        rest = m.group(3).strip()
        beschrijving = f"{kop}: {rest}" if rest else kop
        # Strip ⚖️/🤖 trailing
        beschrijving = re.sub(r"\s*[⚖️🤖]+\s*$", "", beschrijving).strip()
        confidence = _detecteer_confidence(m.group(0))
        stap: dict[str, Any] = {"nummer": nummer, "beschrijving": beschrijving}
        if confidence:
            stap["confidence"] = confidence
        stappen.append(stap)
        laatste_eind = m.end()
    if len(stappen) < 2:
        return None, motivering
    blok = {"type": "procedure", "stappen": stappen}
    rest_tekst = motivering[:eerste_start] + motivering[laatste_eind:]
    return blok, rest_tekst


def _extraheer_definitie(
    motivering: str,
    correct_antwoord: str,
    antwoord_type: Optional[str],
) -> tuple[Optional[dict[str, Any]], str]:
    """Bij antwoord_type='definitie' tracht een definitie-blok te bouwen.

    Lemma = eerste **fettte** zinsdeel of het beste alternatief; definitie_zin
    = eerste paragraaf van motivering.
    """
    if antwoord_type != "definitie":
        return None, motivering
    eerste_para = motivering.split("\n\n", 1)[0].strip()
    if not eerste_para:
        return None, motivering
    # Zoek lemma — fettte zinsdeel aan begin
    m_lemma = re.match(r"\s*(?:Een|De|Het)?\s*\*\*([^*]+?)\*\*", eerste_para)
    lemma = m_lemma.group(1).strip() if m_lemma else None
    if not lemma:
        # Fallback — gebruik correct_antwoord eerste 60 chars
        ca_strip = (correct_antwoord or "").strip()
        if ca_strip:
            lemma = ca_strip.split(".")[0].strip()[:60]
    if not lemma:
        return None, motivering
    confidence = _detecteer_confidence(eerste_para)
    blok: dict[str, Any] = {
        "type": "definitie",
        "lemma": lemma,
        "definitie_zin": eerste_para,
    }
    if confidence:
        blok["confidence"] = confidence
    # Definitie-blok consumeert alleen de eerste para; rest blijft
    rest = motivering[len(eerste_para):].lstrip()
    return blok, rest


def _extraheer_conclusie(motivering: str) -> tuple[Optional[dict[str, Any]], str]:
    """Vind **Conclusie:** of **Antwoord:**-paragraaf."""
    m = _PAT_CONCLUSIE.search(motivering)
    if not m:
        return None, motivering
    inhoud = m.group(2).strip().rstrip(".")
    if not inhoud:
        return None, motivering
    blok = {"type": "conclusie", "inhoud": inhoud}
    confidence = _detecteer_confidence(m.group(0))
    if confidence:
        blok["confidence"] = confidence
    # Conclusie strippen uit motivering
    rest = motivering[:m.start()] + motivering[m.end():]
    return blok, rest


def _restant_naar_motivatie(motivering: str) -> list[dict[str, Any]]:
    """Restant-tekst opdelen in `motivatie`-blokken per paragraaf."""
    if not motivering or not motivering.strip():
        return []
    paragrafen = [p.strip() for p in re.split(r"\n\s*\n", motivering) if p.strip()]
    blokken: list[dict[str, Any]] = []
    for p in paragrafen:
        confidence = _detecteer_confidence(p)
        # Probeer een kop te lichten als de paragraaf begint met **bold-zin:** of ### kop
        kop: Optional[str] = None
        m_h3 = re.match(r"###\s+(.+?)\n(.*)", p, re.DOTALL)
        m_bold_kop = re.match(r"\*\*([^*]{3,80})\*\*\s*[:\.]?\s*\n?(.*)", p, re.DOTALL)
        if m_h3:
            kop = m_h3.group(1).strip()
            inhoud = m_h3.group(2).strip()
        elif m_bold_kop and len(p.split("\n", 1)[0]) < 100:
            kop = m_bold_kop.group(1).strip()
            inhoud = m_bold_kop.group(2).strip()
            # Sanity: alleen als rest niet leeg is, anders pakt motivatie
            # de hele paragraaf
            if not inhoud:
                kop = None
                inhoud = p
        else:
            inhoud = p
        if not inhoud.strip():
            continue
        blok: dict[str, Any] = {"type": "motivatie", "inhoud": inhoud}
        if kop:
            blok["kop"] = kop
        if confidence:
            blok["confidence"] = confidence
        blokken.append(blok)
    return blokken


# ---------------------------------------------------------------------------
# Hoofd-parser
# ---------------------------------------------------------------------------

def structureer_antwoord(
    correct_antwoord: Optional[str],
    antwoord_motivering: Optional[str],
    antwoord_type: Optional[str] = None,
) -> list[dict[str, Any]]:
    """Bouw `correct_antwoord_blokken[]` uit bestaande platte velden.

    STRICT geen nieuwe inhoud. Bij parser-fail: fallback naar één motivatie-blok
    met de volledige antwoord_motivering als inhoud.
    """
    if not correct_antwoord and not antwoord_motivering:
        return []
    motivering = (antwoord_motivering or "").strip()
    if not motivering:
        # Alleen correct_antwoord, geen motivering
        return [{"type": "motivatie", "inhoud": (correct_antwoord or "").strip()}]

    blokken: list[dict[str, Any]] = []

    # 1) Trek grondslag eruit (achter-aan)
    grondslag, motivering = _extraheer_grondslag(motivering)

    # 2) Trek codeblock-/inline-boekingen eruit
    boekingen, motivering = _extraheer_boekingen(motivering)

    # 3) Trek markdown-tabellen eruit
    tabellen, motivering = _extraheer_tabellen(motivering)

    # 4) Trek definitie-blok eruit (bij type=definitie, neemt eerste paragraaf)
    definitie, motivering = _extraheer_definitie(motivering, correct_antwoord or "", antwoord_type)

    # 5) Trek procedure (bij type=procedure)
    procedure, motivering = _extraheer_procedure(motivering, antwoord_type)

    # 6) Trek opsomming (bij type=opsomming of dominante lijst)
    opsomming, motivering = _extraheer_opsomming(motivering, antwoord_type)

    # 7) Trek conclusie/antwoord-kop eruit
    conclusie, motivering = _extraheer_conclusie(motivering)

    # 8) Restant → motivatie-blokken
    motivatie_blokken = _restant_naar_motivatie(motivering)

    # Stel blok-volgorde samen — natuurlijke leesvolgorde
    if definitie:
        blokken.append(definitie)
    blokken.extend(motivatie_blokken)
    if opsomming:
        blokken.append(opsomming)
    if procedure:
        blokken.append(procedure)
    blokken.extend(boekingen)
    blokken.extend(tabellen)
    if conclusie:
        blokken.append(conclusie)
    if grondslag:
        blokken.append(grondslag)

    # Fallback: als er geen enkel blok uitgekomen is (alleen lege restant)
    # gebruik de volledige antwoord_motivering als één motivatie-blok
    if not blokken:
        blokken.append({"type": "motivatie", "inhoud": (antwoord_motivering or "").strip()})

    return blokken


# ---------------------------------------------------------------------------
# Examen-pass: loop over alle vragen + subvragen
# ---------------------------------------------------------------------------

def structureer_examen(
    examen_pad: Path,
    schrijven: bool = True,
) -> dict[str, int]:
    """Structureer alle antwoorden in één examen-bestand.

    Returns: stats dict met count-ers.
    """
    doc = json.loads(examen_pad.read_text(encoding="utf-8"))
    stats = {
        "vragen_total": 0,
        "vragen_met_antwoord": 0,
        "vragen_gestructureerd": 0,
        "subvragen_met_antwoord": 0,
        "subvragen_gestructureerd": 0,
        "fallback_motivatie_only": 0,
    }
    nu = datetime.now(timezone.utc).isoformat()
    for v in doc.get("vragen", []):
        stats["vragen_total"] += 1
        ca = v.get("correct_antwoord")
        am = v.get("antwoord_motivering")
        if ca or am:
            stats["vragen_met_antwoord"] += 1
            blokken = structureer_antwoord(ca, am, v.get("antwoord_type"))
            if blokken:
                v["correct_antwoord_blokken"] = blokken
                stats["vragen_gestructureerd"] += 1
                # provenance-marker
                prov = v.get("antwoord_provenance") or {}
                if isinstance(prov, dict):
                    prov["correct_antwoord_blokken_geextracteerd_op"] = nu
                    v["antwoord_provenance"] = prov
                # Fallback-detectie
                if len(blokken) == 1 and blokken[0].get("type") == "motivatie":
                    stats["fallback_motivatie_only"] += 1
        for sleutel in ("subvragen", "sub_vragen"):
            for s in v.get(sleutel) or []:
                if not isinstance(s, dict):
                    continue
                sca = s.get("correct_antwoord")
                sam = s.get("antwoord_motivering")
                if sca or sam:
                    stats["subvragen_met_antwoord"] += 1
                    sb = structureer_antwoord(
                        sca, sam,
                        s.get("antwoord_type") or v.get("antwoord_type"),
                    )
                    if sb:
                        s["correct_antwoord_blokken"] = sb
                        stats["subvragen_gestructureerd"] += 1
                        if len(sb) == 1 and sb[0].get("type") == "motivatie":
                            stats["fallback_motivatie_only"] += 1
    if schrijven:
        examen_pad.write_text(
            json.dumps(doc, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return stats


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--examen", type=str, default=None,
                        help="Eén examen-id (bv. 2014-1); default = alle")
    parser.add_argument("--dry-run", action="store_true",
                        help="Niets schrijven, alleen stats")
    args = parser.parse_args(argv)

    examen_files: list[Path] = []
    if args.examen:
        p = EXAMEN_DIR / f"{args.examen}.json"
        if not p.exists():
            print(f"Niet gevonden: {p}", file=sys.stderr)
            return 1
        examen_files = [p]
    else:
        for p in sorted(EXAMEN_DIR.glob("*.json")):
            if p.name.startswith("_"):
                continue
            if p.name.endswith("-labels.json"):
                continue
            examen_files.append(p)

    totaal: dict[str, int] = {}
    for f in examen_files:
        s = structureer_examen(f, schrijven=not args.dry_run)
        print(
            f"[{f.name}] "
            f"vragen {s['vragen_gestructureerd']}/{s['vragen_met_antwoord']} "
            f"sub {s['subvragen_gestructureerd']}/{s['subvragen_met_antwoord']} "
            f"fallback {s['fallback_motivatie_only']}"
        )
        for k, v in s.items():
            totaal[k] = totaal.get(k, 0) + v
    print()
    print(f"Totaal vragen-antwoorden gestructureerd: "
          f"{totaal.get('vragen_gestructureerd', 0)}/{totaal.get('vragen_met_antwoord', 0)}")
    print(f"Totaal subvraag-antwoorden gestructureerd: "
          f"{totaal.get('subvragen_gestructureerd', 0)}/{totaal.get('subvragen_met_antwoord', 0)}")
    print(f"Fallback-motivatie-only: {totaal.get('fallback_motivatie_only', 0)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
