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
    """Lift `punten` + `vraag_prefix` + `vraag_onderwerp` uit lopende tekst.

    Ook: strippen van "Antwoord"-residu (komt voor in elke PDF als rubriek-kop)
    en losse "Vraag :"-fragmenten die niet in een instructie-zin zitten.

    Returns:
        (gestripte_tekst, dict met velden: 'punten', 'vraag_prefix',
        'vraag_onderwerp', 'vraag_header_geextracteerd' bool).
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

    # vraag_onderwerp — conservatieve detectie van korte titel-zin aan begin
    onderwerp: Optional[str] = strip_vraag_onderwerp(nieuwe_tekst)
    if onderwerp is not None:
        # Verwijder onderwerp + de daaropvolgende "." + whitespace uit body
        # Eerst trim-leading
        cursor = nieuwe_tekst.lstrip()
        leading_offset = len(nieuwe_tekst) - len(cursor)
        if cursor.startswith(onderwerp):
            after = cursor[len(onderwerp):]
            # Verwijder leestekens + spaties
            after = re.sub(r"^\s*[.\n]\s*", "", after)
            nieuwe_tekst = nieuwe_tekst[:leading_offset] + after

    # Strip residue-tokens uit body
    nieuwe_tekst = _strip_residue_tokens(nieuwe_tekst)

    velden["punten"] = punten
    velden["vraag_prefix"] = prefix
    velden["vraag_onderwerp"] = onderwerp
    velden["vraag_header_geextracteerd"] = bool(
        punten is not None or prefix is not None or onderwerp is not None
    )
    nieuwe_tekst = nieuwe_tekst.strip()
    return nieuwe_tekst, velden


# ---------------------------------------------------------------------------
# v3.1 vraag-cleanup: residue-strippen + vraag_onderwerp-detectie
# ---------------------------------------------------------------------------

# Boekhoud-thema-titels die als één-/twee-woord onderwerp acceptabel zijn.
# Conservatief: alleen bekende lemma's. Pattern-scan toont dat <1 % van de
# vragen een echte titel heeft (alleen 2003-bibf-vrA1 'Kapitaalsubsidies' was
# een onbetwistbare match). Deze whitelist voorkomt false positives op
# eigennamen ("Dhr. Janssens") en cijfer-residu ("1", "F", "G").
_ONDERWERP_WHITELIST = {
    "kapitaalsubsidies", "kapitaalsubsidie",
    "voorraden", "voorraad",
    "afschrijvingen", "afschrijving",
    "herwaardering", "herwaarderingen",
    "waardeverminderingen", "waardevermindering",
    "consolidatie", "consolidatiekring",
    "balans", "resultatenrekening",
    "leasing", "huur",
    "deelneming", "deelnemingen",
    "octrooi", "octrooien",
    "kapitaalverhoging", "kapitaalvermindering",
    "fusie", "splitsing",
    "vereffening", "ontbinding",
    "winstverdeling", "tantième",
    "btw", "btw-aangifte",
}


def strip_vraag_onderwerp(tekst: str) -> Optional[str]:
    """Detecteer een korte boekhoud-thematitel aan het begin van de tekst.

    Conservatief: alleen lemma's uit `_ONDERWERP_WHITELIST` triggeren.
    Heuristiek:
    - Eerste woord (capital-start), gevolgd door "." of newline + casus
    - Lowercase versie moet in whitelist staan
    - Max 4 woorden (om "BTW-aangifte voor Q4" toe te laten, niet langer)

    Returns:
        Onderwerp-string (zoals het in de tekst staat, hoofdletter-behoud)
        of None.
    """
    if not tekst:
        return None
    stripped = tekst.lstrip()
    # Eerste segment voor punt of newline
    m = re.match(r"^([A-ZÉÈÊËÀÂÄÔÖÛÜÇÏÎ][\w\-]{2,}(?:\s+[A-Za-zéèêëàâäôöûüçïî\-]+){0,3})\s*\.\s+[A-Z]", stripped)
    if not m:
        return None
    kandidaat = m.group(1).strip()
    eerste_woord = kandidaat.split()[0].lower()
    # Strip trailing leestekens uit eerste_woord
    eerste_woord_clean = re.sub(r"[^\wéèêëàâäôöûüçïî\-]", "", eerste_woord)
    if eerste_woord_clean not in _ONDERWERP_WHITELIST:
        return None
    return kandidaat


_VRAAG_COLON_RE = re.compile(r"\bVraag\s*[:.?]\s*", re.IGNORECASE)
_ANTWOORD_PREFIX_RE = re.compile(r"(?:^|\n)\s*Antwoord\s*(?=[A-Z\n]|\Z)")
_PUNTEN_RESIDUE_RE = re.compile(r"\b\d{1,3}\s+PUNTEN\b")
_PUNTEN_LOW_RESIDUE_RE = re.compile(r"/\s*[\d,]+\s*punt(?:en)?\b", re.IGNORECASE)
_O_DOT_ER_WERD_RE = re.compile(r"^o\.\s+Er\s+werd\b", re.MULTILINE)


def _strip_residue_tokens(tekst: str) -> str:
    """Verwijder ruistokens uit een tekst-blok-`inhoud`.

    - "Vraag :" / "Vraag:" / "Vraag." / "Vraag?" prefixes  (let op: blijft
      werken vóór een imperatief-werkwoord, want `_INSTRUCTIE_RE` in
      `_scan_vraag_instructie` accepteert "Vraag :" als optionele aanhef en
      pakt de imperatief-zin daarna op. Hier strippen we de zwervende
      voorkomens die niet in een instructie zitten.)
    - "Antwoord" als kop-residu (komt 110× voor in PDFs als rubriek-kop)
    - "N PUNTEN" / "/ N punten" residue
    - PDF-sectie-headers van vorm "<ALL CAPS WORDS> N PUNTEN" (page-divider
      die per ongeluk in vraag-body landde — niet de vraag-punten zelf, die
      zitten in `punten`-veld)
    - "o. Er werd ..." losse fragment-prefix wordt naar "Er werd ..." gestript
    """
    nieuw = tekst
    nieuw = _VRAAG_COLON_RE.sub("", nieuw)
    nieuw = _ANTWOORD_PREFIX_RE.sub("\n", nieuw)
    # PDF-sectie-header strip — bv. "VENNOOTSCHAPSRECHT 20 PUNTEN" of
    # "ANALYSE EN KRITISCHE BEOORDELING VAN DE 25 PUNTEN" — strip volledige
    # regel inclusief aanhakende kapitaal-vervolgregel (kop kan wrappen).
    nieuw = re.sub(
        r"(?:^|\n)\s*[A-ZÉÈÊËÀÂÄÔÖÛÜÇÏÎ][A-ZÉÈÊËÀÂÄÔÖÛÜÇÏÎ\s\-]{3,80}\s+\d{1,3}\s+PUNTEN\s*\n[A-ZÉÈÊËÀÂÄÔÖÛÜÇÏÎ][A-ZÉÈÊËÀÂÄÔÖÛÜÇÏÎ\s\-]{2,80}\s*(?=\n|$)",
        "\n",
        nieuw,
    )
    nieuw = re.sub(
        r"(?:^|\n)\s*[A-ZÉÈÊËÀÂÄÔÖÛÜÇÏÎ][A-ZÉÈÊËÀÂÄÔÖÛÜÇÏÎ\s\-]{3,80}\s+\d{1,3}\s+PUNTEN\s*(?=\n|$)",
        "\n",
        nieuw,
    )
    nieuw = _PUNTEN_RESIDUE_RE.sub("", nieuw)
    nieuw = _PUNTEN_LOW_RESIDUE_RE.sub("", nieuw)
    nieuw = _O_DOT_ER_WERD_RE.sub("Er werd", nieuw)
    # Compacte dubbele witruimte
    nieuw = re.sub(r"[ \t]+", " ", nieuw)
    nieuw = re.sub(r"\n[ \t]+", "\n", nieuw)
    nieuw = re.sub(r"\n{3,}", "\n\n", nieuw)
    return nieuw


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
    """Detecteer imperatief-zin als vraag-instructie.

    Output-inhoud wordt gestript van "Vraag :"-prefix en "Antwoord"-suffix.
    """
    detecties: list[_Detectie] = []
    for m in _INSTRUCTIE_RE.finditer(tekst):
        inhoud = m.group(1).strip()
        # Strip "Vraag :"/"Vraag:"/"Vraag." aan begin (v3.1)
        inhoud = re.sub(r"^\s*Vraag\s*[:.?]\s*", "", inhoud, flags=re.IGNORECASE)
        # Strip "Antwoord" aan einde (v3.1)
        inhoud = re.sub(r"\s+Antwoord\s*$", "", inhoud, flags=re.IGNORECASE)
        inhoud = inhoud.strip()
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
# v3.2: kosten_lijst detector
# ---------------------------------------------------------------------------

# Een kost-bullet: "- post-tekst bedrag (eur(o))?"
# Post mag dubbele punt + apostrof bevatten ("kosten van vooronderzoek: studiebureau's")
# maar geen cijfers (die signaleren het bedrag).
_KOSTEN_BULLET = re.compile(
    r"(?:^|\n)\s*-\s+([A-Za-zéèêëàâäôöûüçïî][^\n0-9]{2,160}?)\s+"
    r"([\d\.\s]+(?:,\d{2})?)\s*(?:EUR|euro)?\s*(?=\n|$)",
    re.IGNORECASE,
)

# Intro-zin die suggereert dat de bullet-lijst kosten/uitgaven beschrijft.
# Conservatief: alleen bekende lemma's vlak vóór de bullets.
_KOSTEN_INTRO_LEMMA = re.compile(
    r"\b(kosten|uitgaven|bedragen|posten|investering(?:en)?)\b[^\n]{0,80}:?\s*(?:\n|$)",
    re.IGNORECASE,
)


def _scan_kosten_lijst(tekst: str) -> list[_Detectie]:
    """Detecteer een bullet-lijst met kost-posten + bedragen.

    Conservatief: minimaal 2 bullets achtereen + intro-zin met
    `kosten`/`uitgaven`/`bedragen`/`posten`/`investering(en)` vlak ervoor.
    Returnt één `kosten_lijst`-blok met `regels[{post, bedrag}]` + `eenheid`.
    """
    matches = list(_KOSTEN_BULLET.finditer(tekst))
    if len(matches) < 2:
        return []
    # Groepeer aaneengesloten bullets (< 80 chars tussen) en check intro vlak ervoor.
    groepen: list[list[re.Match]] = []
    huidige: list[re.Match] = []
    for m in matches:
        if not huidige:
            huidige.append(m)
            continue
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
        # Check intro vlak vóór (binnen 200 chars terug)
        voor_start = groep[0].start()
        voor_window = tekst[max(0, voor_start - 200):voor_start]
        if not _KOSTEN_INTRO_LEMMA.search(voor_window):
            continue
        regels = []
        for m in groep:
            bedrag = parse_bedrag(m.group(2))
            if bedrag is None:
                continue
            post = m.group(1).strip().rstrip(":,;")
            regels.append({"post": post, "bedrag": bedrag})
        if len(regels) < 2:
            continue
        blok = {
            "type": "kosten_lijst",
            "regels": regels,
            "eenheid": "EUR",
        }
        detecties.append(
            _Detectie(start=groep[0].start(), end=groep[-1].end(), blok=blok)
        )
    return detecties


# ---------------------------------------------------------------------------
# v3.2: "Gevraagd:" splitter (context↔vraag-grens)
# ---------------------------------------------------------------------------

_GEVRAAGD_MARKER = re.compile(
    r"\b(Gevraagd|Opdracht)\s*[:\.]\s*",
    re.IGNORECASE,
)


def _splits_op_gevraagd(tekst: str) -> Optional[tuple[str, str]]:
    """Als 'Gevraagd:' / 'Opdracht:' in de tekst staat, splits in (voor, na).

    Returnt None wanneer geen marker aanwezig.
    """
    m = _GEVRAAGD_MARKER.search(tekst)
    if not m:
        return None
    voor = tekst[:m.start()].strip()
    na = tekst[m.end():].strip()
    if not voor or not na:
        return None
    return voor, na


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
        # v3.2: kosten_lijst voorrang op inventaris omdat ze dezelfde
        # bullet-syntax delen; kosten_lijst vereist expliciete kosten-intro.
        ("kosten_lijst", _scan_kosten_lijst),
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

    # v3.1: residue-strip toepassen op alle tekst-blokken (PDF-sectie-headers,
    # losse "Antwoord"-kop-residus, dubbele witruimte). Daarna casus_context-
    # opzuig — beide werken op het schone resultaat.
    resultaat = _scrub_tekst_blokken(resultaat)
    resultaat = _opzuig_casus_context(resultaat)

    return resultaat


def _scrub_tekst_blokken(blokken: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Pas `_strip_residue_tokens` toe op alle `tekst`-blokken in de lijst.

    Verwijdert lege blokken die na strip < 3 tokens overhouden (typisch
    een eenzame "Antwoord" of een afgehouwen vraag-prefix-residu).
    """
    resultaat: list[dict[str, Any]] = []
    for b in blokken:
        if b.get("type") != "tekst":
            resultaat.append(b)
            continue
        inh = (b.get("inhoud") or "").strip()
        nieuw = _strip_residue_tokens(inh).strip()
        if len(nieuw.split()) < 3:
            # Te kort residue — laat blok vallen
            continue
        nieuw_blok = dict(b)
        nieuw_blok["inhoud"] = nieuw
        resultaat.append(nieuw_blok)
    return resultaat


# ---------------------------------------------------------------------------
# v3.1: opzuig-logica voor casus_context
# ---------------------------------------------------------------------------

_IMPERATIEF_START_RE = re.compile(
    r"^\s*(?:" + "|".join(re.escape(v) for v in _INSTRUCTIE_VERBS) + r")\b",
    re.IGNORECASE,
)


def _opzuig_casus_context(blokken: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Promoveer tekst-blokken vóór de eerste vraag_instructie naar casus_context.

    Conservatieve heuristiek (v3.1):
    - Alleen blokken die NU `type: tekst` zijn
    - Vóór de eerste `vraag_instructie`-positie in de lijst
    - Inhoud ≥ 50 tokens (woordvellen)
    - Geen imperatief-start (vermijdt dat een vermomde instructie wordt
      opgezogen)
    """
    # Bepaal index van eerste vraag_instructie
    eerste_instr_idx = next(
        (i for i, b in enumerate(blokken) if b.get("type") == "vraag_instructie"),
        None,
    )
    if eerste_instr_idx is None:
        return blokken
    resultaat: list[dict[str, Any]] = []
    for i, b in enumerate(blokken):
        if (
            i < eerste_instr_idx
            and b.get("type") == "tekst"
        ):
            inhoud = (b.get("inhoud") or "").strip()
            n_tokens = len(inhoud.split())
            if n_tokens >= 50 and not _IMPERATIEF_START_RE.match(inhoud):
                resultaat.append({"type": "casus_context", "inhoud": inhoud})
                continue
        resultaat.append(b)
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


# ---------------------------------------------------------------------------
# v3.2: post-processors voor MC-deduplicatie + tabel→mc_optie conversie
# + "Gevraagd:" splitter + subvraag-whitespace cleanup
# ---------------------------------------------------------------------------

_MC_OPTIE_VERWACHTING_RE = re.compile(
    r"\b(?:kruis\s+aan|het\s+juiste\s+antwoord|welke\s+(?:van|zijn|is)|"
    r"kies\s+(?:de|het)|duid\s+aan|aanvinken|juist[/\s]+fout|waar[/\s]+onwaar)\b",
    re.IGNORECASE,
)


def _is_1koloms_inhoud(rows: list[list[str]]) -> bool:
    """True als alle rijen exact 1 niet-lege cel hebben (of 2 cellen waarvan
    de tweede leeg is — typisch een checkbox-kolom in de PDF-tabel).
    """
    if not rows:
        return False
    for r in rows:
        if not isinstance(r, list):
            return False
        niet_leeg = [c for c in r if isinstance(c, str) and c.strip()]
        if len(niet_leeg) != 1:
            return False
    return True


def _label_volgorde(n: int) -> list[str]:
    """Genereer A, B, C, ... voor n items."""
    if n <= 26:
        return [chr(ord("A") + i) for i in range(n)]
    return [str(i + 1) for i in range(n)]


def converteer_1koloms_tabel_naar_mc_opties(
    blokken: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """v3.2: converteer 1-koloms tabellen (≥ 3 rijen) na een MC-instructie
    naar `mc_optie`-blokken.

    Heuristiek:
    - Zoek `tabel`-blokken met `_is_1koloms_inhoud`-rijen, ≥ 3 rijen
    - Check of ergens in een eerder blok (`tekst`, `vraag_instructie`) een
      MC-instructie staat (kruis aan / het juiste antwoord / welke ...)
    - Vervang het tabel-blok door een sequentie van `mc_optie`-blokken
      met labels A/B/C/...

    Returnt nieuwe blokken-lijst.
    """
    if not blokken:
        return blokken
    resultaat: list[dict[str, Any]] = []
    instructie_gezien = False
    for blok in blokken:
        btype = blok.get("type")
        if btype in ("tekst", "vraag_instructie", "casus_context"):
            inhoud = blok.get("inhoud") or ""
            if _MC_OPTIE_VERWACHTING_RE.search(inhoud):
                instructie_gezien = True
        if (
            btype == "tabel"
            and instructie_gezien
            and _is_1koloms_inhoud(blok.get("rows") or [])
            and len(blok.get("rows") or []) >= 3
        ):
            rows = blok["rows"]
            labels = _label_volgorde(len(rows))
            for label, rij in zip(labels, rows):
                niet_leeg = [c for c in rij if isinstance(c, str) and c.strip()]
                tekst = niet_leeg[0].strip() if niet_leeg else ""
                resultaat.append({
                    "type": "mc_optie",
                    "label": label,
                    "tekst": tekst,
                })
            # `instructie_gezien` blijft True zodat een vraag met meerdere
            # subvragen + telkens een 1-koloms tabel allemaal geconverteerd
            # worden (bv. 2013-1-vr2 met 3 subvragen + 3 MC-tabellen).
            continue
        resultaat.append(blok)
    return resultaat


def deduplicate_mc_optie_subvraag(
    vraagtekst_blokken: list[dict[str, Any]],
    subvraag_labels: list[str],
) -> list[dict[str, Any]]:
    """v3.2: verwijder `mc_optie`-blokken waarvan het `label` overlapt met
    een subvraag-letter-marker.

    `subvraag_labels` zijn de labels uit `subvragen[]`, bv. ['a)', 'b)', 'c)'].
    Een mc_optie met label "a" matched met subvraag-label "a)" of "a".
    """
    if not subvraag_labels:
        return vraagtekst_blokken
    # Normaliseer subvraag-labels: strip parens/dots, lowercase
    sub_letters = set()
    for s in subvraag_labels:
        if not s:
            continue
        cleaned = s.strip().lower().rstrip(")").rstrip(".")
        if cleaned:
            sub_letters.add(cleaned)
    if not sub_letters:
        return vraagtekst_blokken
    resultaat: list[dict[str, Any]] = []
    for b in vraagtekst_blokken:
        if b.get("type") == "mc_optie":
            label = (b.get("label") or "").strip().lower().rstrip(")").rstrip(".")
            if label in sub_letters:
                # Skip — dit is een subvraag-marker, geen MC-optie
                continue
        resultaat.append(b)
    return resultaat


_KORT_RESIDUE_LEN = 50


def cleanup_subvraag_whitespace_residue(
    vraagtekst_blokken: list[dict[str, Any]],
    subvraag_labels: list[str],
    subvraag_teksten: Optional[list[str]] = None,
) -> tuple[list[dict[str, Any]], dict[str, str]]:
    """v3.2: als een tekst-blok < 50 tekens direct na een subvraag-residue staat
    en geen eigen letter-marker bevat, hecht het terug aan de vorige subvraag.

    Returnt (gefilterde blokken, dict[subvraag_label → terug-te-koppelen-tekst]).
    De caller gebruikt het dict om de subvraag-`tekst` aan te vullen.

    Twee scenario's:
    1. Korte tekst-residue na een subvraag-marker (mc_optie of "X)"-tekst) →
       plak aan de marker.
    2. Loose korte tekst-blok wiens inhoud een substring is van een bestaande
       subvraag-tekst (PDF-wrap residue) → laat vallen.
    """
    if not subvraag_labels:
        return vraagtekst_blokken, {}
    sub_set = {
        (s or "").strip().lower().rstrip(")").rstrip(".")
        for s in subvraag_labels
    }
    sub_set.discard("")
    resultaat: list[dict[str, Any]] = []
    plak_aan: dict[str, str] = {}
    laatste_sub_label: Optional[str] = None
    for b in vraagtekst_blokken:
        btype = b.get("type")
        if btype == "mc_optie":
            lbl = (b.get("label") or "").strip().lower().rstrip(")").rstrip(".")
            if lbl in sub_set:
                laatste_sub_label = lbl
                resultaat.append(b)
                continue
            laatste_sub_label = None
            resultaat.append(b)
            continue
        if btype == "tekst":
            inh = (b.get("inhoud") or "").strip()
            # 1) Korte tekst-residue na een subvraag-marker → plak aan
            if (
                laatste_sub_label is not None
                and len(inh) < _KORT_RESIDUE_LEN
                and not re.match(r"^[A-Za-z][\.\)]\s+", inh)
            ):
                plak_aan[laatste_sub_label] = (
                    plak_aan.get(laatste_sub_label, "") + " " + inh
                ).strip()
                laatste_sub_label = None
                continue
            # 2) Loose korte tekst die letterlijk in een bestaande subvraag-
            #    tekst voorkomt → drop (PDF-wrap residue).
            if (
                subvraag_teksten
                and len(inh) < _KORT_RESIDUE_LEN
                and not re.match(r"^[A-Za-z][\.\)]\s+", inh)
            ):
                gedropt = False
                for sv_tekst in subvraag_teksten:
                    if sv_tekst and inh in sv_tekst:
                        gedropt = True
                        break
                if gedropt:
                    laatste_sub_label = None
                    continue
            # 3) Tekst-blok dat begint met "X)" of "X." — markeer als
            #    subvraag-marker. Indien dezelfde inhoud al in subvraag X
            #    zit → drop (PDF-page-wrap residue); anders bewaren als
            #    marker.
            m_marker = re.match(r"^\s*([A-Za-z])[\)\.]\s+(.*)", inh, re.DOTALL)
            if m_marker:
                lbl = m_marker.group(1).lower()
                if lbl in sub_set:
                    payload = m_marker.group(2).strip()
                    # Vergelijk met subvraag-tekst van diezelfde label
                    if subvraag_teksten:
                        # Map sub label index → tekst
                        sub_pairs = list(zip(
                            [
                                (s or "").strip().lower().rstrip(")").rstrip(".")
                                for s in subvraag_labels
                            ],
                            subvraag_teksten,
                        ))
                        for sub_lbl, sub_t in sub_pairs:
                            if sub_lbl == lbl and sub_t:
                                # Vergelijk eerste 30 chars (PDF wrap voegt
                                # \n in, dus exact-vergelijking is broos)
                                p_norm = re.sub(r"\s+", " ", payload)[:80]
                                s_norm = re.sub(r"\s+", " ", sub_t)[:80]
                                if p_norm and (
                                    p_norm in s_norm or s_norm in p_norm
                                ):
                                    # Duplicaat — drop
                                    laatste_sub_label = lbl
                                    break
                        else:
                            laatste_sub_label = lbl
                            resultaat.append(b)
                            continue
                        # gedropt → laatste_sub_label gezet, geen append
                        continue
                    laatste_sub_label = lbl
                    resultaat.append(b)
                    continue
        laatste_sub_label = None
        resultaat.append(b)
    return resultaat, plak_aan


def splits_blokken_op_gevraagd(
    blokken: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """v3.2: als een tekst-blok 'Gevraagd:' / 'Opdracht:' bevat, splits het.

    Tekst ervóór → casus_context (mits ≥ 50 tokens), erna → opnieuw door
    detecteer_typed_blokken halen.
    """
    nieuw: list[dict[str, Any]] = []
    for b in blokken:
        if b.get("type") != "tekst":
            nieuw.append(b)
            continue
        inh = (b.get("inhoud") or "").strip()
        if not inh:
            nieuw.append(b)
            continue
        split = _splits_op_gevraagd(inh)
        if split is None:
            nieuw.append(b)
            continue
        voor, na = split
        # voor → casus_context indien lang genoeg, anders gewone tekst
        if voor:
            if len(voor.split()) >= 20:
                nieuw.append({"type": "casus_context", "inhoud": voor})
            else:
                nieuw.append({"type": "tekst", "inhoud": voor})
        # na → opnieuw door pipeline halen
        if na:
            sub_blokken = detecteer_typed_blokken(na)
            nieuw.extend(sub_blokken)
    return nieuw


def detecteer_blokken_voor_subvraag(tekst: str) -> list[dict[str, Any]]:
    """v3.2: bouw `vraagtekst_blokken[]` voor één subvraag.

    Haalt dezelfde detector-pipeline over de subvraag-tekst, maar zonder
    casus_context-opzuig (subvragen zijn zelden lang verhalend) en zonder
    de "Gevraagd:"-splitter (subvragen bevatten zelden die marker).
    """
    if not tekst or not tekst.strip():
        return []
    return detecteer_typed_blokken(tekst)


# ---------------------------------------------------------------------------
# v3.3: MC-toewijzing aan subvragen
# ---------------------------------------------------------------------------

_SUBVRAAG_MARKER_RE = re.compile(
    r"(?:^|\n)\s*([a-f])\)\s+",
    re.MULTILINE,
)
"""Subvraag-marker in een originele vraagtekst: nieuwe regel + 'a)' / 'b)' ..."""


def _fingerprint_mc_tekst(tekst: str) -> str:
    """Normaliseer een mc_optie-tekst voor robuuste substring-zoekactie.

    Strips whitespace + lowercased, behoudt eerste 40 chars (genoeg om
    uniek te zijn binnen één vraag, robuust tegen line-wrap / case-verschil).
    """
    norm = re.sub(r"\s+", " ", (tekst or "").strip().lower())
    return norm[:40]


def _zoek_positie_in_origineel(
    origineel_norm: str, fingerprint: str, vorige_pos: int
) -> Optional[int]:
    """Zoek de eerste positie van `fingerprint` in `origineel_norm` vanaf
    `vorige_pos`. Returnt None als niet gevonden."""
    if not fingerprint:
        return None
    pos = origineel_norm.find(fingerprint, vorige_pos)
    if pos < 0:
        # Fallback: zoek vanaf begin (mc_opties kunnen out-of-order zijn
        # bij rare PDF-extracties)
        pos = origineel_norm.find(fingerprint, 0)
    return pos if pos >= 0 else None


def _label_voor_index(i: int) -> str:
    """Lever A, B, C, ... voor index 0, 1, 2, ..."""
    if i < 26:
        return chr(ord("A") + i)
    return str(i + 1)


def assign_mc_opties_aan_subvragen(
    vraagtekst_blokken: list[dict[str, Any]],
    subvragen: list[dict[str, Any]],
    origineel_vraagtekst: str,
) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    """v3.3: verplaats `mc_optie`-blokken van vraag-niveau naar subvragen.

    Algoritme:
      1. Bouw `origineel_norm`: lowercased + whitespace-genormaliseerd
         versie van de oorspronkelijke vraagtekst.
      2. Detecteer subvraag-marker-posities (a)/b)/c)/...) in `origineel_norm`
         via `_SUBVRAAG_MARKER_RE`.
      3. Per `mc_optie`-blok in `vraagtekst_blokken`: zoek positie via
         fingerprint van zijn `tekst`. Wijs toe aan de subvraag wiens marker
         direct ervoor staat.
      4. mc_opties zonder bijhorende subvraag-marker (vóór de eerste marker
         of onvindbaar) blijven op vraag-niveau.
      5. Hernummer mc_opties per subvraag (A, B, C, ... opnieuw per groep).

    Args:
        vraagtekst_blokken: huidige v3-blokken op vraag-niveau.
        subvragen: subvraag-records met `label` (bv. 'a)') en optioneel
            `vraagtekst_blokken`.
        origineel_vraagtekst: de oorspronkelijke v2-vraagtekst (ongewijzigd
            door v3-pipeline). Gebruikt voor positie-matching.

    Returns:
        (nieuwe_vraagtekst_blokken, dict[subvraag_label_norm → list[mc_optie]])
        — caller is verantwoordelijk voor het effectief inhechten in de
        subvraag-records.
    """
    if not subvragen or not origineel_vraagtekst:
        return vraagtekst_blokken, {}
    mc_opties_op_vraagniveau = [
        (i, b) for i, b in enumerate(vraagtekst_blokken)
        if b.get("type") == "mc_optie"
    ]
    if not mc_opties_op_vraagniveau:
        return vraagtekst_blokken, {}

    # Normaliseer origineel voor substring-zoektocht
    origineel_norm = re.sub(r"\s+", " ", origineel_vraagtekst.lower())

    # Detecteer subvraag-marker-posities in origineel
    marker_posities: list[tuple[str, int]] = []  # (label_norm, start_pos)
    for m in _SUBVRAAG_MARKER_RE.finditer(origineel_vraagtekst):
        letter = m.group(1).lower()
        # Map naar positie in origineel_norm: gebruik genormaliseerde versie
        # van de tekst tot aan de match-start
        prefix_norm = re.sub(r"\s+", " ", origineel_vraagtekst[:m.start()].lower())
        marker_posities.append((letter, len(prefix_norm)))

    if not marker_posities:
        return vraagtekst_blokken, {}

    # Set van bekende subvraag-labels (uit subvragen[]) voor validatie
    subvraag_labels_norm: list[str] = []
    for sv in subvragen:
        if not isinstance(sv, dict):
            continue
        lbl = (sv.get("label") or "").strip().lower().rstrip(")").rstrip(".")
        if lbl:
            subvraag_labels_norm.append(lbl)
    subvraag_labels_set = set(subvraag_labels_norm)

    # Filter marker_posities tot alleen markers waarvan label ook in
    # subvragen[] bestaat (vermijdt false positives op casus-tekst zoals
    # "a) Onderneming X" die niet als subvraag-marker telt).
    marker_posities = [
        (lbl, pos) for (lbl, pos) in marker_posities if lbl in subvraag_labels_set
    ]
    if not marker_posities:
        return vraagtekst_blokken, {}

    # Bouw mapping: mc_optie-blok-index → (positie_in_origineel, subvraag_label of None)
    toewijzing: dict[int, Optional[str]] = {}
    vorige_zoek_pos = 0
    for idx_in_blokken, blok in mc_opties_op_vraagniveau:
        fp = _fingerprint_mc_tekst(blok.get("tekst") or "")
        pos = _zoek_positie_in_origineel(origineel_norm, fp, vorige_zoek_pos)
        if pos is None:
            toewijzing[idx_in_blokken] = None
            continue
        # Vind meest recente subvraag-marker vóór deze positie
        toegewezen_label: Optional[str] = None
        for lbl, mpos in marker_posities:
            if mpos <= pos:
                toegewezen_label = lbl
            else:
                break
        toewijzing[idx_in_blokken] = toegewezen_label
        # Vooruit-cursor zodat opeenvolgende mc_opties in volgorde blijven
        vorige_zoek_pos = pos + len(fp)

    # Groepeer per subvraag in PDF-volgorde
    per_subvraag: dict[str, list[dict[str, Any]]] = {}
    blokken_op_vraagniveau_te_verwijderen: set[int] = set()
    for idx_in_blokken, lbl in toewijzing.items():
        if lbl is None:
            continue
        blok = vraagtekst_blokken[idx_in_blokken]
        per_subvraag.setdefault(lbl, []).append(dict(blok))
        blokken_op_vraagniveau_te_verwijderen.add(idx_in_blokken)

    # Hernummer labels per subvraag (A/B/C/D opnieuw)
    for lbl, mc_lijst in per_subvraag.items():
        for i, mc in enumerate(mc_lijst):
            mc["label"] = _label_voor_index(i)

    # Bouw nieuwe vraagtekst_blokken (zonder de verplaatste mc_opties)
    nieuwe_blokken = [
        b for i, b in enumerate(vraagtekst_blokken)
        if i not in blokken_op_vraagniveau_te_verwijderen
    ]
    return nieuwe_blokken, per_subvraag
