#!/usr/bin/env python3
"""
extract_programma.py
Mechanische extractie van het ITAA-examenprogramma-PDF naar JSON per programmaonderdeel.

Uitvoer: data/programmaonderdelen/_auto/<X.Y>-<naam-slug>.json
Schema: exact gelijk aan data/programmaonderdelen/4.0-deontologie.json

Gebruik:
    python3 tools/extractie/extract_programma.py

Geen LLM-calls: puur deterministisch tekst-parsen.
"""

import json
import re
import unicodedata
from pathlib import Path
from datetime import datetime, timezone

import pymupdf4llm

# ---------------------------------------------------------------------------
# Configuratie
# ---------------------------------------------------------------------------

PDF_PATH = Path("resources/raw/andere/programma.pdf")
OUTPUT_DIR = Path("data/programmaonderdelen/_auto")
PDF_VERSION = "04/2022"
PDF_SHA256 = "6a532dd301c094afd086c08358589dfe6109c1f7789c93eb84e2e140adf9f18d"

# Mapping: PDF-letter → (programmaonderdeel-code, programmaonderdeel_letter, titel, pagina-range)
# Pagina-range = PDF-paginanummers (footer), 0-indexed in markdown zijn dit de lijnblokken.
PROGRAMMAONDERDELEN = [
    {
        "letter": "B",
        "code": "1.1",
        "programmaonderdeel_letter": "B",
        "titel": "Algemene boekhouding",
        "pages": "8-10",
    },
    {
        "letter": "C",
        "code": "1.2",
        "programmaonderdeel_letter": "C",
        "titel": "Boekhoudrecht en jaarrekeningenrecht",
        "pages": "11-13",
    },
    {
        "letter": "D",
        "code": "1.3",
        "programmaonderdeel_letter": "D",
        "titel": "Analyse en kritische beoordeling van de jaarrekening",
        "pages": "14-15",
    },
    {
        "letter": "E",
        "code": "1.4",
        "programmaonderdeel_letter": "E",
        "titel": "Geconsolideerde jaarrekening en wetgeving betreffende de geconsolideerde jaarrekening",
        "pages": "16",
    },
    {
        "letter": "J",
        "code": "1.5",
        "programmaonderdeel_letter": "J",
        "titel": "Beginselen van de Europese wetgeving en internationale boekhoudkundige normen",
        "pages": "29-30",
    },
    {
        "letter": "H",
        "code": "1.6",
        "programmaonderdeel_letter": "H",
        "titel": "Externe controle",
        "pages": "24-25",
    },
    {
        "letter": "I",
        "code": "1.7",
        "programmaonderdeel_letter": "I",
        "titel": "Interne controle",
        "pages": "26-28",
    },
    {
        "letter": "G",
        "code": "1.8",
        "programmaonderdeel_letter": "G",
        "titel": "Analytische boekhouding en management accounting",
        "pages": "20-23",
    },
    {
        "letter": "F",
        "code": "1.9",
        "programmaonderdeel_letter": "F",
        "titel": "Financiële analyse en fundamentele principes van het financieel bedrijfsbeheer",
        "pages": "17-19",
    },
    {
        "letter": "L",
        "code": "2.1",
        "programmaonderdeel_letter": "L",
        "titel": "Algemene beginselen van fiscaal recht",
        "pages": "34",
    },
    {
        "letter": "P",
        "code": "2.2",
        "programmaonderdeel_letter": "P",
        "titel": "Personenbelasting",
        "pages": "41-42",
    },
    {
        "letter": "Q",
        "code": "2.3",
        "programmaonderdeel_letter": "Q",
        "titel": "Vennootschapsbelasting",
        "pages": "43-44",
    },
    {
        "letter": "S",
        "code": "2.4",
        "programmaonderdeel_letter": "S",
        "titel": "Belasting over de toegevoegde waarde",
        "pages": "46-47",
    },
    {
        "letter": "R",
        "code": "2.5",
        "programmaonderdeel_letter": "R",
        "titel": "Fiscale procedure",
        "pages": "45",
    },
    {
        "letter": "N",
        "code": "2.6",
        "programmaonderdeel_letter": "N",
        "titel": "Registratie- en successierechten",
        "pages": "37-38",
    },
    {
        "letter": "O",
        "code": "2.7",
        "programmaonderdeel_letter": "O",
        "titel": "Regionale en lokale belastingen",
        "pages": "39-40",
    },
    {
        "letter": "M",
        "code": "2.8",
        "programmaonderdeel_letter": "M",
        "titel": "Europees en internationaal fiscaal recht",
        "pages": "35-36",
    },
    {
        "letter": "K",
        "code": "3.0",
        "programmaonderdeel_letter": "K",
        "titel": "Vennootschaps- en verenigingsrecht en insolventiewetgeving",
        "pages": "31-33",
    },
    {
        "letter": "T",
        "code": "4.0",
        "programmaonderdeel_letter": "T",
        "titel": "Deontologische beginselen in verband met het beroep en beginselen op het vlak van antiwitwaswetgeving",
        "pages": "48-51",
    },
]

# Niveau-waarden in de PDF
NIVEAU_MAP = {
    "integratie": "integratie",
    "toepassen": "toepassen",
    "weten en inzien": "weten en inzien",
}


# ---------------------------------------------------------------------------
# Hulpfuncties
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    """Zet tekst om naar filename-safe slug (lowercase, koppeltekens)."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    text = text.strip("-")
    return text


def clean_text(text: str) -> str:
    """Verwijder overbodige whitespace, page-headers/footers, markdown-opmaak."""
    # Verwijder paginafooter-patronen zoals "8 - 04/2022"
    text = re.sub(r"\*\*\d+\s*-\s*04/2022\*\*", "", text)
    # Verwijder markdown bold/italic markers
    text = re.sub(r"\*+([^*]+)\*+", r"\1", text)
    # Verwijder afbeelding-placeholders
    text = re.sub(r"==>.*?<==", "", text)
    # Verwijder leading/trailing pijlen (➢ > -)
    text = re.sub(r"^[➢>\-–•]\s*", "", text.strip())
    # Normaliseer whitespace
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_niveau(block: str) -> str:
    """Extraheer het niveau uit sectie 1."""
    m = re.search(
        r'vereiste niveau[:\s]*["“”]?(integratie|toepassen|weten en inzien)["“”]?',
        block,
        re.IGNORECASE,
    )
    if m:
        return NIVEAU_MAP.get(m.group(1).lower(), m.group(1).lower())
    return "integratie"


def parse_taken_doelstellingen_table(block: str) -> list[dict]:
    """
    Parseer de markdown-tabel met Taken | Doelstellingen.
    Retourneert lijst van taakblokken: [{"taken": [...], "doelstellingen": [...]}]
    Detecteert ook "Deel 1" / "Deel 2" annotaties in sommige PO's.

    pymupdf4llm genereert tabellen als lijn-per-lijn:
      |Taak-tekst|Doelstelling-tekst|
    Elke tabel-rij staat op één lijn (inclusief <br> voor meerdere items).
    """
    taakblokken = []

    # Zoek de tabel-sectie
    table_match = re.search(
        r"\|[*_\s]*Taken[*_\s]*\|[*_\s]*Doelstellingen[*_\s]*\|(.*?)(?=\n##|\Z)",
        block,
        re.DOTALL | re.IGNORECASE,
    )
    if not table_match:
        # Probeer alternatief formaat (sommige PO's gebruiken aparte ## headers)
        return _parse_taken_doelstellingen_nontable(block)

    table_content = table_match.group(1)

    current_deel = 1
    huidig_blok = {"deel": 1, "taken": [], "doelstellingen": []}

    for lijn in table_content.split("\n"):
        lijn = lijn.strip()
        if not lijn or not lijn.startswith("|"):
            continue

        # Verwijder scheidingsrij (|---|---|)
        if re.match(r"^\|[-\s|]+\|$", lijn):
            continue

        # Split op pipe: |taak|doelstelling|
        parts = lijn.split("|")
        # parts[0] is leeg (lijn begint met |), parts[1] = taak, parts[2] = doelstelling
        if len(parts) < 3:
            continue

        taken_cel = parts[1].strip()
        doel_cel = parts[2].strip() if len(parts) > 2 else ""

        # Reinig markdown-opmaak in cellen
        taken_cel = re.sub(r"\*+([^*]+)\*+", r"\1", taken_cel)
        doel_cel = re.sub(r"\*+([^*]+)\*+", r"\1", doel_cel)

        taken_tekst = taken_cel.strip()
        doel_tekst = doel_cel.strip()

        # Detecteer "Deel 1" / "Deel 2" annotaties (in bold, zoals **Deel 1**)
        if re.match(r"^deel\s*[12]$", taken_tekst.lower()):
            if huidig_blok["taken"] or huidig_blok["doelstellingen"]:
                taakblokken.append(huidig_blok)
            deel_num = int(re.search(r"\d", taken_tekst).group())
            current_deel = deel_num
            huidig_blok = {"deel": deel_num, "taken": [], "doelstellingen": []}
            continue

        if not taken_tekst and not doel_tekst:
            continue

        # Taken: splits op <br> voor meerdere taken in 1 cel
        taken_items = _split_cell_items(taken_tekst)
        doel_items = _split_cell_items(doel_tekst)

        for t in taken_items:
            if t:
                huidig_blok["taken"].append({"tekst": t})
        for d in doel_items:
            if d:
                huidig_blok["doelstellingen"].append({"tekst": d})

    if huidig_blok["taken"] or huidig_blok["doelstellingen"]:
        taakblokken.append(huidig_blok)

    return taakblokken


def _parse_taken_doelstellingen_nontable(block: str) -> list[dict]:
    """
    Fallback: parseer Taken en Doelstellingen uit ongestructureerde tekst.
    Ondersteunt drie subformaten:
      1. '## **Taken**' en '## **Doelstellingen**' als aparte headers (C, H, J)
      2. '**Taken** <tekst>' gevolgd door '## **Doelstellingen**' (E)
      3. Gemengde tabel zonder header-rij (I): **Taken Doelstellingen** samen
    """
    taakblok = {"deel": 1, "taken": [], "doelstellingen": []}

    # Formaat 1: ## **Taken** header (C, H, J)
    taken_m = re.search(
        r"## \*\*Taken\*\*\s*\n(.*?)(?=\n## \*\*Doelstellingen\*\*|## \*\*3\.|$)",
        block,
        re.DOTALL,
    )
    doel_m = re.search(
        r"## \*\*Doelstellingen\*\*\s*\n(.*?)(?=\n## \*\*3\.|## _\*\*[A-Z]\.|$)",
        block,
        re.DOTALL,
    )

    if taken_m or doel_m:
        if taken_m:
            for line in taken_m.group(1).split("\n"):
                t = clean_text(line)
                if t and not t.startswith("|") and len(t) > 3:
                    taakblok["taken"].append({"tekst": t})
        if doel_m:
            for line in doel_m.group(1).split("\n"):
                d = clean_text(line)
                if d and not d.startswith("|") and len(d) > 3:
                    taakblok["doelstellingen"].append({"tekst": d})
        return [taakblok] if (taakblok["taken"] or taakblok["doelstellingen"]) else []

    # Formaat 2: **Taken** <inline tekst> gevolgd door ## **Doelstellingen** (E)
    taken_inline_m = re.search(
        r"\*\*Taken\*\*\s+(.+?)(?=\n## \*\*Doelstellingen\*\*|\n## \*\*3\.)",
        block,
        re.DOTALL,
    )
    doel_m2 = re.search(
        r"## \*\*Doelstellingen\*\*\s*\n(.*?)(?=\n## \*\*3\.|$)",
        block,
        re.DOTALL,
    )

    if taken_inline_m:
        tekst = clean_text(taken_inline_m.group(1))
        if tekst:
            taakblok["taken"].append({"tekst": tekst})
    if doel_m2:
        for line in doel_m2.group(1).split("\n"):
            d = clean_text(line)
            if d and len(d) > 3:
                taakblok["doelstellingen"].append({"tekst": d})

    if taakblok["taken"] or taakblok["doelstellingen"]:
        return [taakblok]

    # Formaat 3: alles na "Taken en doelstellingen" zonder header-rij (I)
    td_m = re.search(
        r"Taken en doelstellingen[^\n]*\n(.*?)(?=\n## \*\*3\.|\n## _\*\*[A-Z]\.|$)",
        block,
        re.DOTALL,
    )
    if td_m:
        content = td_m.group(1)
        # Probeer Genoemde-items te extraheren na ➢
        items = re.findall(r"➢\s*(.+?)(?=➢|\Z)", content, re.DOTALL)
        for item in items:
            d = clean_text(item)
            if d and len(d) > 5:
                taakblok["doelstellingen"].append({"tekst": d})
        # Eerste lijn als taak
        first_line = content.split("\n")[0]
        t = clean_text(first_line)
        if t and len(t) > 5:
            taakblok["taken"].append({"tekst": t})

    return [taakblok] if (taakblok["taken"] or taakblok["doelstellingen"]) else []


def _split_cell_items(cel: str) -> list[str]:
    """
    Splits een cel-inhoud in afzonderlijke items.

    Strategie:
    - Als de cel ➢ bevat: split op ➢ (➢ = expliciete item-scheiding)
      <br> binnen een ➢-item is een regelafbreking (wordt spatie).
    - Geen ➢: de cel is één item. <br> zijn regelafbrekingen (worden spaties).
      Uitzondering: 'leerdoelen:'-blokken in F-PO worden ook gevonden.
    """
    if "➢" in cel:
        # Split op ➢, behandel <br> als spatie (regelafbreking binnen ➢-item)
        cel_merged = re.sub(r"<br>\s*", " ", cel, flags=re.IGNORECASE)
        parts = cel_merged.split("➢")
        items = []
        for part in parts:
            part = clean_text(part)
            if part and len(part) > 2:
                items.append(part)
        return items
    else:
        # Geen ➢: split op <br> met heuristic:
        # - <br> gevolgd door hoofdletter → nieuw item
        # - <br> gevolgd door kleine letter of leesteken → regelafbreking (spatie)
        # Splits eerst op alle <br>
        parts = re.split(r"<br>", cel, flags=re.IGNORECASE)
        items = []
        current_parts = []
        for part in parts:
            part_stripped = part.strip()
            if not part_stripped:
                continue
            if current_parts and part_stripped and part_stripped[0].isupper():
                # Nieuwe zin begint: sla huidige op en begin nieuw item
                combined = " ".join(current_parts)
                combined = clean_text(combined)
                if combined and len(combined) > 2:
                    items.append(combined)
                current_parts = [part_stripped]
            else:
                # Voortzetting van huidige zin
                current_parts.append(part_stripped)
        if current_parts:
            combined = " ".join(current_parts)
            combined = clean_text(combined)
            if combined and len(combined) > 2:
                items.append(combined)
        return items


def parse_kenniselementen(block: str, po_code: str) -> list[dict]:
    """
    Parseer de kenniselementen-sectie.

    De PDF gebruikt een diep-geneste hiërarchie:
      - I. Sectie-header (Romein) → identificeert 'deel' (1 of 2)
        - A. Kenniselement (Hoofdletter) → top-level KE, code = <po>.I.A
          1. Subitem (Arabisch) → code = <po>.I.A.1
             1. Sub-subitem → code = <po>.I.A.1.1
          - A. Subitem in hoofd-stijl (indien geen Romein-hiërarchie)

    Voor sectie II (gewone bedrijfsuitoefening in 1.1) staan de items als:
      A. Oprichtingskosten ...   → 1.1.II.A
      H. Eigen middelen          → 1.1.II.H
        1. subitems              → 1.1.II.H.1

    Top-level output: de Hoofdletter-kenniselementen (niet de Romein-headers).
    Romein-headers worden gebruikt om het 'deel'-veld te bepalen.
    """
    kenniselementen = []

    # Zoek de kenniselementen-sectie
    ke_match = re.search(
        r"## \*\*3\.\s*Kenniselementen\*\*\s*\n(.*?)(?=\n## _\*\*[A-Z]\.|$)",
        block,
        re.DOTALL,
    )
    if not ke_match:
        ke_match = re.search(
            r"3\.\s*Kenniselementen[^\n]*\n(.*?)$",
            block,
            re.DOTALL,
        )
    if not ke_match:
        return kenniselementen

    ke_text = ke_match.group(1)

    # Reinig paginafooters, afbeeldingen en markdown-opmaak
    ke_text = re.sub(r"\*\*\d+\s*-\s*04/2022\*\*\s*\n?", "", ke_text)
    ke_text = re.sub(r"\*\*==>.*?<==\*\*\s*\n?", "", ke_text)
    ke_text = re.sub(r"==>.*?<==\s*\n?", "", ke_text)
    ke_text = re.sub(r"\*+([^*]+)\*+", r"\1", ke_text)

    def romein_to_num(r: str) -> int:
        vals = {
            "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
            "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
            "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15,
            "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19, "XX": 20,
        }
        return vals.get(r.upper(), 1)

    def is_romein(s: str) -> bool:
        return bool(re.match(r"^[IVX]+$", s, re.IGNORECASE)) and s.upper() in {
            "I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII",
            "XIV","XV","XVI","XVII","XVIII","XIX","XX"
        }

    def is_romein_header(letter: str, tekst: str) -> bool:
        """
        Detecteer of een Romein-getal een echte sectie-header is (niet een letter-item).

        Regels:
        1. Sectie-headers hebben ALL-CAPS tekst (bijv. 'BASISREGELS VAN DE BOEKHOUDING').
        2. Patronen als 'Voor de taken onder deel X' zijn ook sectie-headers.
        3. Als het geen geldig Romein-getal is, dan is het geen sectie-header.
        """
        if not is_romein(letter):
            return False
        # Patroon: "Voor de taken onder deel ..."
        if re.match(r"voor de taken onder deel", tekst, re.IGNORECASE):
            return True
        # ALL-CAPS controle: als de tekst grotendeels in hoofdletters staat
        words = re.findall(r"[A-Za-z]+", tekst)
        if not words:
            return False
        caps_count = sum(1 for w in words if w.isupper() and len(w) > 1)
        return caps_count >= len(words) * 0.5  # 50%+ woorden zijn ALL-CAPS

    # Parseer regels
    lines = ke_text.split("\n")

    # We bouwen een geneste structuur van kennis-items
    # Hiërarchie-niveaus:
    #   romein: I. II. III. ... (ALL-CAPS tekst) → bepaalt 'deel', NIET als KE opgeslagen
    #   hoofd:  A. B. C. ... of I. J. K. (mixed case) → top-level kenniselement
    #   arabisch: 1. 2. 3. ... → subitem van hoofd
    #   klein: a) b) c) ...    → sub-subitem van arabisch

    # Patroon voor Romein of Hoofd: '- X. tekst' of 'X. tekst' aan het begin
    ROMEIN_OF_HOOFD = re.compile(r"^[-\s]*([A-Z]{1,6})\.\s+(.+)$")
    ARAB = re.compile(r"^\s*(\d+)\.\s+(.+)$")
    KLEIN = re.compile(r"^\s+([a-z])\)\s+(.+)$")

    current_deel = 1
    current_deel_tekst = None
    current_hoofd_code = None
    current_arab_code = None

    # ke_dict speelt rol van geordende dict: code -> dict
    ke_dict: dict[str, dict] = {}
    ke_order: list[str] = []  # volgorde van top-level KE codes (Hoofd-niveau)

    def add_ke(code: str, ke: dict):
        ke_dict[code] = ke
        if code not in ke_order:
            ke_order.append(code)

    def get_or_create_ke(code: str, deel: int, tekst: str) -> dict:
        if code not in ke_dict:
            ke = {"deel": deel, "code": code, "tekst": tekst, "_subitems": []}
            add_ke(code, ke)
        return ke_dict[code]

    for raw_line in lines:
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped:
            continue

        # Romein-of-Hoofd item (letter aan het begin)
        m = ROMEIN_OF_HOOFD.match(stripped)
        if m:
            letter = m.group(1)
            tekst = clean_text(m.group(2))

            if is_romein_header(letter, tekst):
                # Romein-sectie-header (ALL-CAPS of 'Voor de taken'): update deel, geen KE
                current_deel = romein_to_num(letter)
                current_hoofd_code = None
                current_arab_code = None
            elif is_romein(letter) and current_deel == 1:
                # Romein-getal, geen actieve sectie → is zelf een KE (bijv. 2.x PO's)
                # Code: <po>.<romein_letter>
                code = f"{po_code}.{letter.upper()}"
                ke = get_or_create_ke(code, 1, tekst)
                current_hoofd_code = code
                current_arab_code = None
            else:
                # Enkelvoudige hoofdletter (A-Z), OF Romein-letter binnen een actieve sectie
                # → Hoofd-KE binnen actieve deel
                code = f"{po_code}.{_romein_str(current_deel)}.{letter}"
                ke = get_or_create_ke(code, current_deel, tekst)
                current_hoofd_code = code
                current_arab_code = None
            continue

        # Arabisch-item
        m = ARAB.match(stripped)
        if m:
            num = m.group(1)
            tekst = clean_text(m.group(2))
            if current_hoofd_code:
                parent_code = current_hoofd_code
                code = f"{current_hoofd_code}.{num}"
            else:
                code = f"{po_code}.{_romein_str(current_deel)}.{num}"
                parent_code = f"{po_code}.{_romein_str(current_deel)}"

            ke = {"code": code, "tekst": tekst, "_subitems": []}
            ke_dict[code] = ke
            if parent_code in ke_dict:
                ke_dict[parent_code]["_subitems"].append(ke)
            current_arab_code = code
            continue

        # Klein-item
        m = KLEIN.match(line)  # gebruik originele lijn voor inspring-detectie
        if m and current_arab_code:
            letter_k = m.group(1)
            tekst = clean_text(m.group(2))
            code = f"{current_arab_code}.{letter_k}"
            ke = {"code": code, "tekst": tekst}
            ke_dict[code] = ke
            if current_arab_code in ke_dict:
                ke_dict[current_arab_code]["_subitems"].append(ke)
            continue

    # Bouw de finale kenniselementen-lijst
    def finalize(ke: dict) -> dict:
        result = {}
        for k, v in ke.items():
            if k == "_subitems":
                continue
            result[k] = v
        if ke.get("_subitems"):
            result["subitems"] = [finalize(s) for s in ke["_subitems"]]
        return result

    # Bepaal welk niveau top-level is:
    # Als er Hoofd-items zijn (lettercode A-Z) → die zijn top-level
    # Als er alleen Romein-items zijn die ZELF als KE bedoeld zijn (niet sectie-headers) → Romein is top-level
    hoofd_codes = [c for c in ke_order if c in ke_dict]

    # Check of er Romein-level items zijn die als sectie-header zijn gezien vs als KE
    # Als alle ke_dict entries direkt Romein zijn (geen .I.A maar wel .I) → Romein is top-level
    romein_top = [c for c in ke_dict if re.match(rf"^{re.escape(po_code)}\.[IVX]+$", c, re.IGNORECASE)]

    if hoofd_codes:
        # Er zijn Hoofd-items: gebruik die als top-level
        result = [finalize(ke_dict[c]) for c in hoofd_codes]
    elif romein_top:
        # Alleen Romein-items: die zijn de echte KEs
        result = [finalize(ke_dict[c]) for c in romein_top if c in ke_dict]
    else:
        # Fallback: gebruik alle ke_dict items
        result = [finalize(ke_dict[c]) for c in ke_dict]

    return result


def _romein_str(deel: int) -> str:
    """Converteer een deel-nummer naar Romein-string."""
    vals = ["I","II","III","IV","V","VI","VII","VIII","IX","X",
            "XI","XII","XIII","XIV","XV","XVI","XVII","XVIII","XIX","XX"]
    if 1 <= deel <= len(vals):
        return vals[deel - 1]
    return str(deel)


def extract_intro_tekst(block: str) -> str | None:
    """Extraheer optionele intro-tekst na '3. Kenniselementen' header maar vóór eerste lijst-item."""
    ke_match = re.search(
        r"3\.\s*Kenniselementen[^\n]*\n+(.*?)(?=\n[-\s]*[IVX]+\.\s|\n\s*[A-Z]\.\s|\Z)",
        block,
        re.DOTALL | re.MULTILINE,
    )
    if not ke_match:
        return None
    tekst = clean_text(ke_match.group(1))
    if len(tekst) < 20:
        return None
    return tekst


def extract_po_block(full_md: str, letter: str) -> str:
    """
    Extraheer het markdown-blok voor programmaonderdeel met gegeven letter.
    Ondersteunt twee formaten uit pymupdf4llm:
      1. '## _**X. Titel**_ '  (meeste PO's)
      2. '- _**X. Titel**_ '   (laatste PO, T)
    """
    # Patroon 1: ## _**X. ... (tot volgende ## _**[A-Z]. of - _**[A-Z]. of einde)
    pattern1 = rf"(## _\*\*{re.escape(letter)}\..*?)(?=\n## _\*\*[A-Z]\.|(?=\n- _\*\*[A-Z]\.)|\Z)"
    m = re.search(pattern1, full_md, re.DOTALL)
    if m:
        return m.group(1)

    # Patroon 2: - _**X. ... (voor de laatste PO)
    pattern2 = rf"(- _\*\*{re.escape(letter)}\..*?)(?=\n## _\*\*[A-Z]\.|(?=\n- _\*\*[A-Z]\.)|\Z)"
    m = re.search(pattern2, full_md, re.DOTALL)
    if m:
        return m.group(1)

    return ""


def build_taakblokken_met_codes(taakblokken_raw: list[dict], po_code: str) -> list[dict]:
    """
    Voeg codes toe aan taakblokken: <po_code>.D1.1, <po_code>.D1.2, etc.
    Detecteer deel-nummering.
    """
    result = []
    teller_per_deel = {}

    for blok in taakblokken_raw:
        deel = blok.get("deel", 1)
        teller_per_deel[deel] = teller_per_deel.get(deel, 0) + 1
        volg = teller_per_deel[deel]
        code = f"{po_code}.D{deel}.{volg}"

        result.append({
            "deel": deel,
            "code": code,
            "taken": blok.get("taken", []),
            "doelstellingen": blok.get("doelstellingen", []),
        })

    return result


def po_to_json(po_config: dict, full_md: str) -> dict:
    """Bouw het volledige JSON-object voor één programmaonderdeel."""
    letter = po_config["letter"]
    po_code = po_config["code"]

    block = extract_po_block(full_md, letter)

    if not block:
        print(f"  WAARSCHUWING: geen blok gevonden voor letter {letter}")
        block = ""

    niveau = parse_niveau(block)
    taakblokken_raw = parse_taken_doelstellingen_table(block)
    taakblokken = build_taakblokken_met_codes(taakblokken_raw, po_code)
    kenniselementen = parse_kenniselementen(block, po_code)

    # Introductietekst (optioneel, zoals bij 1.1)
    intro = extract_intro_tekst(block)

    # Bouw scope op basis van taakblokken en kenniselementen
    kern_taakblokken = [t["code"] for t in taakblokken if t.get("deel", 1) == 1]
    kern_kenniselementen = [k["code"] for k in kenniselementen if k.get("deel", 1) == 1]

    result = {
        "programmaonderdeel": po_code,
        "programmaonderdeel_letter": po_config["programmaonderdeel_letter"],
        "titel": po_config["titel"],
        "niveau": niveau,
        "source": {
            "type": "itaa-programma",
            "version": PDF_VERSION,
            "pages": po_config["pages"],
        },
        "scope": {
            "kern_taakblokken": kern_taakblokken,
            "kern_kenniselementen": kern_kenniselementen,
            "voorbehoud": None,
        },
    }

    if intro:
        result["intro_tekst"] = intro

    result["taakblokken"] = taakblokken
    result["kenniselementen"] = kenniselementen

    result["_provenance"] = {
        "inputs": [
            {
                "id": "resources/raw/andere/programma.pdf",
                "sha256": PDF_SHA256,
                "version": PDF_VERSION,
            }
        ],
        "tooling": {
            "pipeline": "auto",
            "pipeline_version": "extract_programma-v1",
            "model": None,
            "prompt_version": None,
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "stale": False,
        "stale_reason": None,
    }

    return result


def main():
    print(f"Lees PDF: {PDF_PATH}")
    full_md = pymupdf4llm.to_markdown(str(PDF_PATH))
    print(f"  {len(full_md)} tekens geladen")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    resultaten = []

    for po_config in PROGRAMMAONDERDELEN:
        code = po_config["code"]
        titel = po_config["titel"]
        print(f"\nVerwerk {code} ({po_config['letter']}): {titel[:50]}...")

        try:
            po_json = po_to_json(po_config, full_md)

            # Bepaal bestandsnaam
            titel_slug = slugify(titel)
            # Gebruik de code als prefix, maar maak titels niet te lang
            titel_kort = "-".join(titel_slug.split("-")[:5])
            filename = f"{code}-{titel_kort}.json"
            output_path = OUTPUT_DIR / filename

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(po_json, f, ensure_ascii=False, indent=2)

            n_taak = sum(len(t["taken"]) for t in po_json["taakblokken"])
            n_doel = sum(len(t["doelstellingen"]) for t in po_json["taakblokken"])
            n_ke = len(po_json["kenniselementen"])

            resultaten.append({
                "code": code,
                "bestand": str(output_path),
                "taken": n_taak,
                "doelstellingen": n_doel,
                "kenniselementen": n_ke,
            })

            print(f"  -> {filename}")
            print(f"     taken={n_taak}, doelstellingen={n_doel}, kenniselementen={n_ke}")

        except Exception as e:
            print(f"  FOUT bij {code}: {e}")
            import traceback
            traceback.print_exc()

    print("\n" + "=" * 60)
    print("SAMENVATTING")
    print("=" * 60)
    for r in resultaten:
        print(f"  {r['code']:5s}  taken={r['taken']:2d}  doel={r['doelstellingen']:2d}  KE={r['kenniselementen']:2d}")
    print(f"\nTotaal: {len(resultaten)}/{len(PROGRAMMAONDERDELEN)} programmaonderdelen geëxtraheerd")
    print(f"Output: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
