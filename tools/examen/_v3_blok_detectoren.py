"""Pattern-detectoren voor v3-blok-types (ADR-021 v3.0).

Functioneert als post-processor: krijgt een platte tekst (de inhoud van een
v2 `tekst`-blok of een vraag-segment) en breekt het op in typed v3-blokken.

Strategie — top-down:
1. **Lift top-level vraag-velden** (`punten`, `vraag_prefix`) uit de tekst en
   verwijder ze uit de body.
2. **Detecteer MAR-/balans-/inventaris-/marktwaarde-/aanpassing-blokken** —
   greedy line-by-line.
3. **Detecteer mc_optie-blokken** — regel-prefix `A.`/`a)` met tekst.
4. **Detecteer bijlage_verwijzing** — zinsdeel met "in bijlage".
5. **Detecteer casus_context** vs `vraag_instructie` — eerste verhalende
   paragraaf vs. imperatief-paragraaf.
6. **Restant** → `tekst`-blok (fallback).

Het script bouwt geen blok wanneer een detector unzeker is — fallback naar
`tekst` is de veilige default.

Pure functies, geen pdfplumber-dependency. Direct testbaar.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Optional

# ---------------------------------------------------------------------------
# Top-level vraag-veld extractie
# ---------------------------------------------------------------------------

_PUNTEN_UPPERCASE = re.compile(r"\b(\d{1,3})\s+PUNTEN\b")
_PUNTEN_LOWERCASE = re.compile(r"/\s*([\d,]+)\s*punt(?:en)?", re.IGNORECASE)
# Vraag-prefix-patronen — laat label als groep 1 staan
_VRAAG_PREFIX_PATRONEN = [
    re.compile(r"^\s*(Vraag\s+\d+[a-z]?)\b"),
    re.compile(r"^\s*([A-Z]\.\d+)\.?\b"),  # bv. "A.1." / "B.5"
    re.compile(r"^\s*(vr[AB]\d{1,2})\b"),  # bibf
]


def lift_top_level_velden(tekst: str) -> tuple[str, dict[str, Any]]:
    """Lift `punten` + `vraag_prefix` uit lopende tekst.

    Returns:
        (gestripte_tekst, dict met velden: 'punten', 'vraag_prefix',
        'vraag_header_geextracteerd' bool).
    """
    velden: dict[str, Any] = {}
    nieuwe_tekst = tekst

    # punten
    punten: Optional[float] = None
    m_up = _PUNTEN_UPPERCASE.search(nieuwe_tekst)
    if m_up:
        punten = float(m_up.group(1))
        nieuwe_tekst = nieuwe_tekst[:m_up.start()] + nieuwe_tekst[m_up.end():]
    else:
        m_low = _PUNTEN_LOWERCASE.search(nieuwe_tekst)
        if m_low:
            punten = float(m_low.group(1).replace(",", "."))
            nieuwe_tekst = nieuwe_tekst[:m_low.start()] + nieuwe_tekst[m_low.end():]

    # vraag_prefix
    prefix: Optional[str] = None
    nieuwe_tekst_strip = nieuwe_tekst.lstrip()
    for pat in _VRAAG_PREFIX_PATRONEN:
        m = pat.match(nieuwe_tekst_strip)
        if m:
            prefix = m.group(1)
            # Verwijder prefix + trailing punt + "…" + spaties uit nieuwe_tekst
            cutoff_in_strip = m.end()
            # ook trailing-konst "…" / "." / spaties strippen
            rest = nieuwe_tekst_strip[cutoff_in_strip:]
            rest = re.sub(r"^\s*[…\.]+\s*", "", rest)
            n_strip = len(nieuwe_tekst) - len(nieuwe_tekst_strip)
            nieuwe_tekst = nieuwe_tekst[:n_strip] + rest
            break

    velden["punten"] = punten
    velden["vraag_prefix"] = prefix
    velden["vraag_header_geextracteerd"] = bool(punten is not None or prefix is not None)
    nieuwe_tekst = nieuwe_tekst.strip()
    return nieuwe_tekst, velden


# ---------------------------------------------------------------------------
# Cijfer-parsing
# ---------------------------------------------------------------------------

_BEDRAG_RE = re.compile(r"\d{1,3}(?:[.\s]\d{3})*,\d{2}|\d{1,3}(?:[.\s]\d{3})+|\d+,\d{2}")


def parse_bedrag(s: str) -> Optional[float]:
    """Parse Belgisch bedrag-formaat: '7.000,00' / '500,00' / '105 000' → float.

    Returns None bij geen match.
    """
    if not s:
        return None
    s = s.strip()
    # Verwijder spaties als thousands-sep
    s = s.replace(" ", "")
    # Komma is decimaal, punt is thousands
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    else:
        s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Typed blok-detectoren
# ---------------------------------------------------------------------------

# Proef-saldibalans-regel: rek-nr (2-6 cijfers) + naam + D/C + bedrag + (euro)?
_PSB_REGEL = re.compile(
    r"(?<!\w)(\d{2,6})\s+([A-ZÉÈÊËÀÂÄÔÖÛÜÇÏÎ][\w\séèêëàâäôöûüçïî\-/&\.()'\"]{2,80}?)\s+([DC])\s+([\d\.\s]+,\d{2})(?:\s*(?:EUR|euro))?",
)

# Rekeningstaat-regel: rek-nr + " - " + naam + bedrag (bv. 2013-2 correctie-tabel)
_REKENINGSTAAT_REGEL = re.compile(
    r"(?<!\w)(\d{4,6})\s*-\s*([A-Za-zéèêëàâäôöûüçïî][\w\séèêëàâäôöûüçïî\-/&\.()'\"]{2,80}?)\s+([\d\.\s]+,\d{2})",
)

# Inventaris-bullet: "- post bedrag,00"
_INVENTARIS_REGEL = re.compile(
    r"(?:^|[\n\s])-\s+([A-Za-zéèêëàâäôöûüçïî][\w\séèêëàâäôöûüçïî\-/&\.()'\"]{2,80}?)\s+([\d\.\s]+,\d{2})",
)

# Marktwaarde
_MARKTWAARDE = re.compile(
    r"(?:de\s+)?(marktprijs|marktwaarde|reële\s+waarde)(?:\s+van\s+(?:de\s+)?([\w\s\-]{2,60}?))?\s+(?:bedraagt|is)\s+([\d\.\s]+,\d{2})\s*(?:EUR|euro)?",
    re.IGNORECASE,
)

# Aanpassing (afgeprijsd / afprijzing / waardevermindering / opwaardering)
_AANPASSING = re.compile(
    r"\b(afgeprijsd|afprijzing|opwaardering|waardevermindering|herwaardering)\b(?:[^.]{0,150}?(?:bedrag(?:en)?\s+van|voor)\s+(?:een\s+totaal\s+bedrag\s+van\s+)?)?\s*([\d\.\s]+,\d{2})",
    re.IGNORECASE,
)

# Bijlage-verwijzing
_BIJLAGE = re.compile(
    r"\b((?:in|als|zie)\s+bijlage[^.]{0,200}\.|bijlage(?:n)?\s+\d+[^.]{0,150}\.)",
    re.IGNORECASE,
)

# Vraag-instructie — imperatief begin
_INSTRUCTIE_VERBS = (
    "Geef", "Bereken", "Bepaal", "Motiveer", "Verklaar", "Beschrijf",
    "Leg uit", "Schrijf", "Boek", "Maak", "Stel", "Vermeld", "Noem",
    "Welke", "Wat is", "Hoe", "Beoordeel", "Toon aan", "Identificeer",
    "Som op", "Geef weer", "Antwoord",
)
_INSTRUCTIE_RE = re.compile(
    r"(?:^|\.\s+|\bVraag\s*:\s*)((?:" + "|".join(re.escape(v) for v in _INSTRUCTIE_VERBS) + r")\b[^.?!]*[.?!])",
    re.IGNORECASE,
)

# Casus-intro
_CASUS_INTRO = re.compile(
    r"\b((?:De\s+(?:vennootschap|NV|BV|BVBA|CV|cli[eë]nt|heer|onderneming)|NV|BV|BVBA|CV|De\s+heer|Mevrouw)\s+[A-Z][^.]{5,300}\.)",
)

# MC-optie aan begin van regel
_MC_OPTIE_RE = re.compile(
    r"^\s*([A-D]|[a-d])[.)]\s+(.{2,300})$",
    re.MULTILINE,
)


@dataclass
class _Detectie:
    """Eén pattern-match in de input-tekst (positie + blok-dict)."""

    start: int
    end: int
    blok: dict[str, Any]


def _scan_proef_saldibalans(tekst: str) -> list[_Detectie]:
    """Scan opeenvolgende PSB-regels en groepeer ze in één blok.

    Een PSB-blok = ≥ 2 opeenvolgende matches met < 60 chars tekstuele ruis
    ertussen.
    """
    matches = list(_PSB_REGEL.finditer(tekst))
    if len(matches) < 2:
        return []
    # Groepeer aaneengesloten matches
    groepen: list[list[re.Match]] = []
    huidige: list[re.Match] = []
    for m in matches:
        if not huidige:
            huidige.append(m)
            continue
        # Als de gap met vorige match klein is (< 80 chars), zelfde groep
        gap = m.start() - huidige[-1].end()
        if gap < 80:
            huidige.append(m)
        else:
            groepen.append(huidige)
            huidige = [m]
    if huidige:
        groepen.append(huidige)
    detecties: list[_Detectie] = []
    for groep in groepen:
        if len(groep) < 2:
            continue
        regels = []
        for m in groep:
            regels.append({
                "rekening": m.group(1),
                "naam": m.group(2).strip(),
                "zijde": m.group(3),
                "bedrag": parse_bedrag(m.group(4)) or 0.0,
            })
        blok = {
            "type": "proef_saldibalans",
            "regels": regels,
            "eenheid": "EUR",
        }
        detecties.append(_Detectie(start=groep[0].start(), end=groep[-1].end(), blok=blok))
    return detecties


def _scan_rekeningstaat(tekst: str) -> list[_Detectie]:
    """Scan opeenvolgende 'NNNNNN - naam bedrag' regels (zonder D/C kolom)."""
    matches = list(_REKENINGSTAAT_REGEL.finditer(tekst))
    if len(matches) < 2:
        return []
    groepen: list[list[re.Match]] = []
    huidige: list[re.Match] = []
    for m in matches:
        if not huidige:
            huidige.append(m)
            continue
        gap = m.start() - huidige[-1].end()
        if gap < 120:
            huidige.append(m)
        else:
            groepen.append(huidige)
            huidige = [m]
    if huidige:
        groepen.append(huidige)
    detecties: list[_Detectie] = []
    for groep in groepen:
        if len(groep) < 2:
            continue
        regels = []
        for m in groep:
            regels.append({
                "rekening": m.group(1),
                "naam": m.group(2).strip(),
                "bedrag": parse_bedrag(m.group(3)) or 0.0,
            })
        blok = {
            "type": "rekeningstaat",
            "regels": regels,
            "eenheid": "EUR",
        }
        detecties.append(_Detectie(start=groep[0].start(), end=groep[-1].end(), blok=blok))
    return detecties


def _scan_inventaris(tekst: str) -> list[_Detectie]:
    """Scan opeenvolgende bullet-lijst regels met post + bedrag."""
    matches = list(_INVENTARIS_REGEL.finditer(tekst))
    if len(matches) < 2:
        return []
    groepen: list[list[re.Match]] = []
    huidige: list[re.Match] = []
    for m in matches:
        if not huidige:
            huidige.append(m)
            continue
        gap = m.start() - huidige[-1].end()
        if gap < 60:
            huidige.append(m)
        else:
            groepen.append(huidige)
            huidige = [m]
    if huidige:
        groepen.append(huidige)
    detecties: list[_Detectie] = []
    for groep in groepen:
        if len(groep) < 2:
            continue
        regels = []
        for m in groep:
            regels.append({
                "post": m.group(1).strip(),
                "bedrag": parse_bedrag(m.group(2)) or 0.0,
            })
        blok = {
            "type": "inventaris",
            "regels": regels,
            "eenheid": "EUR",
        }
        detecties.append(_Detectie(start=groep[0].start(), end=groep[-1].end(), blok=blok))
    return detecties


def _scan_marktwaarde(tekst: str) -> list[_Detectie]:
    detecties: list[_Detectie] = []
    for m in _MARKTWAARDE.finditer(tekst):
        bedrag = parse_bedrag(m.group(3))
        if bedrag is None:
            continue
        post = (m.group(2) or "").strip() or None
        blok: dict[str, Any] = {
            "type": "marktwaarde",
            "bedrag": bedrag,
            "eenheid": "EUR",
        }
        if post:
            blok["post"] = post
        detecties.append(_Detectie(start=m.start(), end=m.end(), blok=blok))
    return detecties


def _scan_aanpassing(tekst: str) -> list[_Detectie]:
    detecties: list[_Detectie] = []
    for m in _AANPASSING.finditer(tekst):
        bedrag = parse_bedrag(m.group(2))
        if bedrag is None:
            continue
        type_lc = m.group(1).lower()
        # Normaliseer type-label
        if "afprijz" in type_lc or "afgeprijsd" in type_lc:
            ttype = "afprijzing"
        elif "opwaard" in type_lc:
            ttype = "opwaardering"
        elif "waardevermind" in type_lc:
            ttype = "waardevermindering"
        elif "herwaard" in type_lc:
            ttype = "herwaardering"
        else:
            ttype = type_lc
        blok: dict[str, Any] = {
            "type": "aanpassing",
            "subtype": ttype,
            "bedrag": bedrag,
            "eenheid": "EUR",
        }
        detecties.append(_Detectie(start=m.start(), end=m.end(), blok=blok))
    return detecties


def _scan_bijlage(tekst: str) -> list[_Detectie]:
    detecties: list[_Detectie] = []
    for m in _BIJLAGE.finditer(tekst):
        blok = {
            "type": "bijlage_verwijzing",
            "beschrijving": m.group(1).strip(),
        }
        detecties.append(_Detectie(start=m.start(), end=m.end(), blok=blok))
    return detecties


def _scan_mc_opties(tekst: str) -> list[_Detectie]:
    """Detecteer MC-opties — alleen wanneer ≥ 2 opties op opeenvolgende regels.

    Vermijdt false positives op gewone tekst die toevallig met "A. " begint.
    """
    matches = list(_MC_OPTIE_RE.finditer(tekst))
    if len(matches) < 2:
        return []
    # Filter op opeenvolgende labels (A,B,C of a,b,c,d)
    labels = [m.group(1) for m in matches]
    labels_set = set(labels)
    # Moet labels A, B of a, b (minimaal 2 opvolgend) bevatten
    is_upper_seq = "A" in labels_set and "B" in labels_set
    is_lower_seq = "a" in labels_set and "b" in labels_set
    if not (is_upper_seq or is_lower_seq):
        return []
    detecties: list[_Detectie] = []
    for m in matches:
        blok = {
            "type": "mc_optie",
            "label": m.group(1),
            "tekst": m.group(2).strip(),
        }
        detecties.append(_Detectie(start=m.start(), end=m.end(), blok=blok))
    return detecties


def _scan_vraag_instructie(tekst: str) -> list[_Detectie]:
    """Detecteer imperatief-zin als vraag-instructie."""
    detecties: list[_Detectie] = []
    for m in _INSTRUCTIE_RE.finditer(tekst):
        inhoud = m.group(1).strip()
        # Strip trailing-witruimte
        if len(inhoud) < 8:
            continue
        # Bereken start van de groep (niet de hele match)
        groep_start = m.start(1)
        groep_end = m.end(1)
        blok = {
            "type": "vraag_instructie",
            "inhoud": inhoud,
        }
        detecties.append(_Detectie(start=groep_start, end=groep_end, blok=blok))
    return detecties


def _scan_casus_context(tekst: str) -> list[_Detectie]:
    """Detecteer casus-intro (verhalende paragraaf)."""
    detecties: list[_Detectie] = []
    for m in _CASUS_INTRO.finditer(tekst):
        inhoud = m.group(1).strip()
        if len(inhoud) < 20:
            continue
        blok = {
            "type": "casus_context",
            "inhoud": inhoud,
        }
        detecties.append(_Detectie(start=m.start(1), end=m.end(1), blok=blok))
    return detecties


# ---------------------------------------------------------------------------
# Composit: typed-blokken uit één tekst
# ---------------------------------------------------------------------------

def detecteer_typed_blokken(tekst: str) -> list[dict[str, Any]]:
    """Hoofdfunctie: krijgt platte tekst, geeft list[blok-dict] in volgorde.

    Strategie:
    1. Alle detectoren runnen, kandidaten verzamelen met (start, end, blok).
    2. Resolve overlaps — prioriteit: psb > rekeningstaat > inventaris >
       marktwaarde > aanpassing > bijlage > mc_optie > vraag_instructie >
       casus_context.
    3. Vul gaten op met tekst-blokken.
    """
    if not tekst or not tekst.strip():
        return []

    prio_volgorde: list[tuple[str, callable]] = [
        ("proef_saldibalans", _scan_proef_saldibalans),
        ("rekeningstaat", _scan_rekeningstaat),
        ("inventaris", _scan_inventaris),
        ("marktwaarde", _scan_marktwaarde),
        ("aanpassing", _scan_aanpassing),
        ("bijlage", _scan_bijlage),
        ("mc_optie", _scan_mc_opties),
        ("vraag_instructie", _scan_vraag_instructie),
        ("casus_context", _scan_casus_context),
    ]

    # Verzamel alle kandidaten met prio-index
    kandidaten: list[tuple[int, _Detectie]] = []
    for prio, (_, fn) in enumerate(prio_volgorde):
        for det in fn(tekst):
            kandidaten.append((prio, det))

    # Sorteer op (start, prio) — als overlap, eerst-gewonnen
    kandidaten.sort(key=lambda x: (x[1].start, x[0]))

    # Resolve overlaps — greedy
    geselecteerd: list[_Detectie] = []
    laatste_end = 0
    for prio, det in kandidaten:
        if det.start < laatste_end:
            # Overlap met eerder geselecteerd → skip (lagere prio of latere positie)
            continue
        geselecteerd.append(det)
        laatste_end = det.end

    # Sorteer op start
    geselecteerd.sort(key=lambda d: d.start)

    # Vul gaten op met tekst-blokken
    resultaat: list[dict[str, Any]] = []
    cursor = 0
    for det in geselecteerd:
        if det.start > cursor:
            gat = tekst[cursor:det.start].strip()
            if gat:
                resultaat.append({"type": "tekst", "inhoud": gat})
        resultaat.append(det.blok)
        cursor = det.end
    # Trailing tekst
    if cursor < len(tekst):
        gat = tekst[cursor:].strip()
        if gat:
            resultaat.append({"type": "tekst", "inhoud": gat})

    return resultaat


# ---------------------------------------------------------------------------
# Backward-compat: render typed blok naar markdown voor flat vraagtekst
# ---------------------------------------------------------------------------

def render_blok_als_markdown(blok: dict[str, Any]) -> str:
    """Render een v3-blok als markdown-string (voor concat-vraagtekst).

    Voor tekst-blokken: alleen `inhoud`.
    Voor tabel-achtige blokken: markdown-tabel.
    Voor scalars (marktwaarde, aanpassing): één regel.
    """
    btype = blok.get("type")
    if btype == "tekst":
        return (blok.get("inhoud") or "").strip()
    if btype == "tabel":
        rows = blok.get("rows", [])
        headers = blok.get("headers")
        if not rows and not headers:
            return ""
        if headers:
            n_kol = len(headers)
        else:
            n_kol = max((len(r) for r in rows), default=0)
            headers = [""] * n_kol
        hdr = "| " + " | ".join(headers) + " |"
        sep = "|" + "|".join(["---"] * n_kol) + "|"
        data_rows = ["| " + " | ".join((r + [""] * (n_kol - len(r)))) + " |" for r in rows]
        return "\n".join([hdr, sep, *data_rows])
    if btype in ("proef_saldibalans", "rekeningstaat"):
        regels = blok.get("regels", [])
        if btype == "proef_saldibalans":
            headers = ["Rekening", "Naam", "Zijde", "Bedrag"]
            rs = [[r["rekening"], r["naam"], r["zijde"], f"{r['bedrag']:.2f}"] for r in regels]
        else:
            headers = ["Rekening", "Naam", "Bedrag"]
            rs = [[r["rekening"], r["naam"], f"{r['bedrag']:.2f}"] for r in regels]
        hdr = "| " + " | ".join(headers) + " |"
        sep = "|" + "|".join(["---"] * len(headers)) + "|"
        body = ["| " + " | ".join(r) + " |" for r in rs]
        return "\n".join([hdr, sep, *body])
    if btype == "inventaris":
        regels = blok.get("regels", [])
        return "\n".join(f"- {r['post']}: {r['bedrag']:.2f} EUR" for r in regels)
    if btype == "balans":
        delen = []
        if blok.get("activa"):
            delen.append("**Activa**")
            for r in blok["activa"]:
                delen.append(f"- {r['rubriek']}: {r.get('bedrag', '')}")
        if blok.get("passiva"):
            delen.append("**Passiva**")
            for r in blok["passiva"]:
                delen.append(f"- {r['rubriek']}: {r.get('bedrag', '')}")
        return "\n".join(delen)
    if btype == "resultatenrekening":
        regels = blok.get("regels", [])
        return "\n".join(f"- {r['post']}: {r.get('bedrag', '')}" for r in regels)
    if btype == "marktwaarde":
        post = blok.get("post") or "post"
        return f"Marktwaarde {post}: {blok['bedrag']:.2f} EUR"
    if btype == "aanpassing":
        return f"Aanpassing ({blok.get('subtype', 'onbekend')}): {blok['bedrag']:.2f} EUR"
    if btype == "bijlage_verwijzing":
        return f"_{blok.get('beschrijving', '')}_"
    if btype == "casus_context":
        return f"> {blok.get('inhoud', '')}"
    if btype == "vraag_instructie":
        return f"**{blok.get('inhoud', '')}**"
    if btype == "mc_optie":
        return f"{blok['label']}. {blok['tekst']}"
    if btype == "berekening_gegeven":
        return blok.get("formule", "")
    if btype == "formule":
        return blok.get("inhoud", "")
    if btype == "figuur":
        return f"[figuur: {blok.get('caption', '')}]"
    return ""


def concat_v3_blokken_naar_vraagtekst(blokken: list[dict[str, Any]]) -> str:
    """Bouw flat vraagtekst op uit v3-blokken (backward-compat)."""
    parts = [render_blok_als_markdown(b) for b in blokken]
    return "\n\n".join(p for p in parts if p).strip()
