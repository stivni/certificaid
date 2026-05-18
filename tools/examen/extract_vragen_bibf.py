"""
Vragen-extractie-v1-bibf: extraheer examenvragen uit BIBF voorbeeldexamen-PDFs (2003, 2008).

Deterministisch script — geen LLM-calls. Schema identiek aan tools/examen/extract_vragen.py
(ITAA-voorbeeldexamens), met letter-codering A-K i.p.v. PO-codes 1.1/1.2/...

Twee BIBF-examens:
- 2003-bibf.pdf — 17 mei 2003, 100 pt, GEEN modelantwoorden
- 2008-bibf.pdf — 24 mei 2008, 100 pt, MET modelantwoorden (uniek)

BIBF werd in 2019 geabsorbeerd door ITAA — vandaar dat deze voorbeeldexamens
relevant blijven voor bevragingsstijl, hoewel de inhoud (WVV, WIB, etc.) verouderd kan zijn.

Output: data/programma/examen_vragen/{2003,2008}-bibf.json
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import pdfplumber

from tools.examen._vraagtekst_normalisatie import normaliseer as normaliseer_vraagtekst

TOOL_ID = "vragen-extractie-v1-bibf"
PDF_LIB = "pdfplumber"
BASE_DIR = Path("/Users/stivni/Documents/ITAA/certificaid")
OUTPUT_DIR = BASE_DIR / "data" / "programma" / "examen_vragen"
PDF_DIR = BASE_DIR / "resources" / "raw" / "voorbeeldexamens"


# Watermerk-lijnen die genegeerd moeten worden bij vraagtekst-opbouw
WATERMARK_PATTERNS = [
    re.compile(r"^lOMoARcPSD\|"),
    re.compile(r"^messages\.downloaded_by\s*$"),
    re.compile(r"^messages\."),
    re.compile(r"^Downloaded by Stijn"),
    re.compile(r"^NAAM\s*:"),
    re.compile(r"^VOORNAAM\s*:"),
    re.compile(r"^LIDNUMMER\s*:"),
    re.compile(r"^-\s*pag\s*\d+"),
    re.compile(r"^Praktisch bekwaamheidsexamen 17 mei 2003 – vragen\s*$"),
    re.compile(r"^Studocu is not sponsored"),
    re.compile(r"^Scan to open"),
]

SECTION_HEADERS = {
    "A": "A. Algemene boekhouding",
    "B": "B. Wetgeving op de boekhouding en de jaarrekening + opstellen, analyse en kritische beoordeling van de jaarrekening",
    "C": "C. Algemene beginselen van het financieel beheer",
    "D": "D. Organisatie van de boekhouding en de administratieve diensten van de onderneming",
    "E": "E. BTW",
    "F": "F. Personenbelasting",
    "G": "G. Vennootschapsbelasting",
    "H": "H. Belastingprocedures (2008: + registratie- en successierechten)",
    "I": "I. Vennootschapsrecht, ondernemingen in moeilijkheden (2003: + registratie/successie + douane/accijnzen)",
    "J": "J. Beginselen van het arbeids- en sociaal zekerheidsrecht",
    "K": "K. Plichtenleer",
}


# ---------------------------------------------------------------------------
# Tekst-extractie + watermerk-filtering
# ---------------------------------------------------------------------------

def filter_watermark(text: str) -> str:
    """Verwijder watermerk-regels uit een tekstblok."""
    out = []
    for line in text.splitlines():
        if any(p.search(line) for p in WATERMARK_PATTERNS):
            continue
        out.append(line)
    return "\n".join(out)


def extract_pages(pdf_path: Path) -> list[tuple[int, str]]:
    """Geeft [(paginanummer, schone-tekst)] terug."""
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            raw = page.extract_text() or ""
            clean = filter_watermark(raw)
            pages.append((i, clean))
    return pages


# ---------------------------------------------------------------------------
# 2003-bibf — vraag-definities
# ---------------------------------------------------------------------------

# Anchor = unieke substring die vraag-begin markeert in PDF-tekst
# End anchor = unieke substring die vraag-einde markeert (= begin volgende vraag of sectie)
# Punten: expliciet in 2003 (uit PDF)

VRAGEN_2003 = [
    # (vraag_nr, vak_code, vraagtype, punten, pdf_pagina, start_anchor, end_anchor, themas)
    ("A.1", "A", "berekening", 5, 2, "A.1. Kapitaalsubsidies.", "Op de proef- en saldibalans staan volgende bedragen:",
     ["kapitaalsubsidies", "afsluitingsboekingen"]),
    ("A.2", "A", "berekening", 5, 2, "Op de proef- en saldibalans staan volgende bedragen:", "B. WETGEVING OP DE BOEKHOUDING",
     ["voorraadwaardering", "waardevermindering-handelsgoederen", "afsluitingsboekingen"]),
    ("B.1", "B", "open", 3, 2, "B.1. Vraag: Welke ondernemingen", "B.2. Vraag:",
     ["vereenvoudigde-boekhouding"]),
    ("B.2", "B", "open", 2, 2, "B.2. Vraag:", "B.3. Vraag:",
     ["centraal-boek"]),
    ("B.3", "B", "open", 5, 2, "B.3. Vraag:\nWelke activa", "B.4. Vraag:",
     ["herwaarderingsmeerwaarden"]),
    ("B.4", "B", "open", 2, 2, "B.4. Vraag:", "B.5. Vraag:",
     ["inrichtingskosten-gehuurde-gebouwen"]),
    ("B.5", "B", "open", 3, 2, "B.5. Vraag:", "C. ALGEMENE BEGINSELEN",
     ["kapitaalsubsidies", "toelichting-jaarrekening"]),
    ("C.1", "C", "berekening", 4, 3, "C.1. Op de balans staan volgende bedragen", "C.2. Naast de balans",
     ["netto-bedrijfskapitaal", "liquiditeitsratio", "solvabiliteitsratio"]),
    ("C.2", "C", "berekening", 1, 3, "C.2. Naast de balans", "D. ORGANISATIE VAN DE BOEKHOUDING",
     ["operationele-cashflow"]),
    ("D.1", "D", "open", 3, 3, "D.1 Een persoon vestigt zich als zelfstandige om een taverne", "D.2 Een zelfstandige schrijnwerker",
     ["administratieve-organisatie", "btw-belastingplichtige"]),
    ("D.2", "D", "open", 2, 3, "D.2 Een zelfstandige schrijnwerker", "DEELDOMEIN FISCALITEIT",
     ["btw-voorschotten", "bewaarplicht-documenten"]),
    ("E.1", "E", "MC", 2, 4, "E.1 Gelieve een kruisje te plaatsen", "E.2 Welk is de aftrekbare BTW",
     ["btw-belastingplichtige", "recht-op-aftrek"]),
    ("E.2", "E", "berekening", 2, 4, "E.2 Welk is de aftrekbare BTW", "E.3 Is er BTW verschuldigd",
     ["btw-aftrek", "btw-geschenken", "intracommunautaire-verwerving"]),
    ("E.3", "E", "J/F", 2, 4, "E.3 Is er BTW verschuldigd", "E.4 Welk is het wettelijk tijdstip",
     ["btw-verschuldigd", "voordeel-alle-aard", "intracommunautaire-levering"]),
    ("E.4", "E", "open", 2, 5, "E.4 Welk is het wettelijk tijdstip", "E.5 Gelieve de juiste keuze",
     ["btw-listings", "btw-voorschot-december", "btw-stopzetting"]),
    ("E.5", "E", "J/F", 2, 5, "E.5 Gelieve de juiste keuze te omcirkelen", "F. PERSONENBELASTING",
     ["dagboek-ontvangsten", "btw-administratie"]),
    ("F.1", "F", "berekening", 10, 5, "F. PERSONENBELASTING", "G. VENNOOTSCHAPSBELASTING",
     ["bedrijfsleider-bezoldiging", "forfaitaire-beroepskosten", "voordeel-alle-aard-auto", "kadastraal-inkomen"]),
    ("G.1", "G", "berekening", 10, 6, "G. VENNOOTSCHAPSBELASTING", "H. BELASTINGPROCEDURES",
     ["vennootschapsbelasting-aangifte", "dbi-aftrek", "verworpen-uitgaven", "liberaliteiten"]),
    ("H.1", "H", "MC", 1, 6, "H.1. Binnen welke termijn", "Inzake Directe Belastingen:",
     ["btw-regularisatie", "verjaringstermijn"]),
    ("H.2", "H", "open", 4, 7, "H.2. De belastingplichtige heeft geen verzoek", "DEELDOMEIN VENNOOTSCHAPSRECHT",
     ["laattijdige-aangifte", "ambtshalve-aanslag"]),
    ("I.1", "I", "J/F", 2, 7, "I. 1 Worden er in België accijnzen", "I.2. Een handelaar wenst",
     ["accijnzen", "intracommunautaire-verwerving"]),
    ("I.2", "I", "open", 11, 7, "I.2. Een handelaar wenst zijn eenmanszaak", "I.3. Wat zijn de verplichtingen",
     ["omzetting-eenmanszaak-bvba", "inbreng-natura", "registratierechten"]),
    ("I.3", "I", "open", 4, 7, "I.3. Wat zijn de verplichtingen van een vennootschap ingeval", "I.4. Wat zijn de mogelijke gevolgen",
     ["alarmbelprocedure", "overgedragen-verlies"]),
    ("I.4", "I", "open", 3, 8, "I.4. Wat zijn de mogelijke gevolgen", "J. BEGINSELEN VAN HET ARBEIDS",
     ["neerlegging-jaarrekening-nbb", "ontbinding-van-rechtswege"]),
    ("J.1", "J", "open", 2.5, 8, "J.1. Ten gevolge van het verlies van een grote klant", "J.2 Een werkgever wenst",
     ["sociale-bijdragen-zelfstandige", "regularisatie-bijdragen"]),
    ("J.2", "J", "open", 2.5, 8, "J.2 Een werkgever wenst één van zijn werknemers", "K. PLICHTENLEER",
     ["ontslag-procedure", "opzegtermijn"]),
    ("K.1", "K", "open", 4, 8, "K.1 : Beschrijf de deontologische regels", "K.2 : Gelden diezelfde regels",
     ["overdracht-dossier", "confraterrelaties-bibf"]),
    ("K.2", "K", "open", 1, 8, "K.2 : Gelden diezelfde regels", "***",
     ["overdracht-dossier", "interberoepsrelaties-iab-ibr"]),
]


# ---------------------------------------------------------------------------
# 2008-bibf — vraag-definities (vraagtekst t/m "Antwoord:", daarna antwoord)
# ---------------------------------------------------------------------------

# 2008 heeft modelantwoorden. Per vraag: start_anchor, end_anchor.
# Antwoord-blok herkenning: alles tussen "Antwoord:" (of in latere vragen geen marker — antwoord volgt direct na opgave)
# en de volgende vraag/sectie.

VRAGEN_2008 = [
    # (vraag_nr, vak_code, vraagtype, punten, pdf_pagina, start_anchor, end_anchor, themas)
    ("A.1", "A", "berekening", None, 3, "A.1 In 2007 bedragen de bruto bezoldigingen", "A.2 In januari 2008",
     ["vakantiegeld", "voorzieningen", "afsluitingsboekingen"]),
    ("A.2", "A", "berekening", None, 3, "A.2 In januari 2008, ontvangt u een factuur", "A.3 De voorraden bedragen",
     ["te-ontvangen-facturen", "btw-aftrek", "matching-principe"]),
    ("A.3", "A", "berekening", None, 4, "A.3 De voorraden bedragen op 1 januari N", "A.4 Een kleine vennootschap",
     ["voorraadwijzigingen", "afsluitingsboekingen"]),
    ("A.4", "A", "berekening", None, 4, "A.4 Een kleine vennootschap heeft de rechtspersoonlijkheid", "B. WETGEVING OP DE BOEKHOUDING",
     ["oprichtingskosten", "afschrijvingen", "personenwagen", "boekjaar-korter-dan-12-maanden"]),
    ("B.1", "B", "berekening", None, 5, "B.1 In een groep controleert vennootschap A", "B.2 De hierboven vermelde vennootschap B stelt",
     ["deelneming-verbonden-onderneming", "groepsstructuur"]),
    ("B.2", "B", "open", None, 5, "B.2 De hierboven vermelde vennootschap B stelt 5 voltijdse equivalenten", "B.3 De hierboven vermelde vennootschap A heeft 12.000 EUR",
     ["jaarrekening-schema", "groottecriteria", "geconsolideerde-grondslag"]),
    ("B.3", "B", "open", None, 6, "B.3 De hierboven vermelde vennootschap A heeft 12.000 EUR, exclusief BTW", "B.4 In de sociale balans",
     ["commissaris-bezoldiging", "toelichting-jaarrekening"]),
    ("B.4", "B", "open", None, 6, "B.4 In de sociale balans heeft een rubriek", "C. ALGEMENE BEGINSELEN VAN HET FINANCIEEL BEHEER",
     ["sociale-balans", "opleidingskosten"]),
    ("C.1", "C", "open", None, 6, "C.1 Wat verstaat men met", "C.2 Een vennootschap heeft jaarlijks ongeveer",
     ["behoefte-aan-bedrijfskapitaal", "werkkapitaal"]),
    ("C.2", "C", "berekening", None, 7, "C.2 Een vennootschap heeft jaarlijks ongeveer 30.000", "D. ORGANISATIE VAN DE BOEKHOUDING",
     ["cashflow-analyse", "investeringskrediet", "kapitaalaflossingen"]),
    ("D.1", "D", "open", None, 7, "D.1 Een persoon vestigt zich als zelfstandige om een taverne", "D.2 Een zelfstandige schrijnwerker",
     ["administratieve-organisatie", "horeca-administratie", "btw-belastingplichtige"]),
    ("D.2", "D", "open", None, 8, "D.2 Een zelfstandige schrijnwerker stelt offertes", "DEELDOMEIN FISCALITEIT",
     ["btw-voorschotten", "bewaarplicht-documenten"]),
    ("E.1", "E", "open", None, 9, "E.1 Een van uw cliënten, detailhandelaar in textielproducten", "E.2",
     ["btw-regime-overgang", "forfaitair-regime", "stock-detaxatie"]),
    ("E.2", "E", "berekening", None, 9, "E.2\nWelke zijn de vakken in de periodieke BTW aangifte", "E.3",
     ["btw-aangifte-vakken", "intracommunautaire-levering", "margeregeling", "tweedehandswagens"]),
    ("E.3", "E", "open", None, 11, "E.3\n1. Welke is de uiterste datum waarover U beschikt om de BTW af te trekken", "F. PERSONENBELASTING",
     ["btw-aftrektermijn", "btw-vrijstellingsregeling", "btw-eenheid", "plaats-van-de-dienst"]),
    ("F.1", "F", "open", None, 12, "F.1 Gert is ongehuwd en woont in Mechelen", "F.2 Riet en Piet zijn gehuwd",
     ["hypothecaire-lening", "intrestaftrek", "woonbonus", "enige-woning"]),
    ("F.2", "F", "open", None, 12, "F.2 Riet en Piet zijn gehuwd in het wettelijk stelsel", "F.3 Een echtpaar heeft dienstencheques",
     ["onroerende-inkomsten", "meerwaarde-onroerend-goed", "huwelijksvermogensstelsel"]),
    ("F.3", "F", "berekening", None, 12, "F.3 Een echtpaar heeft dienstencheques aangekocht", "F.4 Wim is gehuwd met Inge",
     ["dienstencheques", "belastingvermindering", "huwelijksquotient"]),
    ("F.4", "F", "open", None, 13, "F.4 Wim is gehuwd met Inge in het stelsel van scheiding van goederen", "F.5",
     ["scheiding-van-goederen", "hypothecaire-lening", "aftrekbare-besteding"]),
    ("F.5", "F", "MC", None, 13, "F.5: Wat is juist inzake belastbaar tijdperk", "F 6",
     ["belastbaar-tijdperk", "toerekening-inkomsten"]),
    ("F.6", "F", "MC", None, 13, "F 6. Wat is geen vrijgesteld inkomen", "F7",
     ["vrijgesteld-inkomen", "sociale-voordelen"]),
    ("F.7", "F", "MC", None, 13, "F7. Welke uitgave vormt een aftrekbare besteding", "G. VENNOOTSCHAPSBELASTING",
     ["aftrekbare-besteding", "beschermde-eigendommen"]),
    ("G.1", "G", "berekening", None, 14, "G1. De vennootschap “Green”", "H. BELASTINGPROCEDURES",
     ["vennootschapsbelasting-aangifte", "kmo-tarief", "investeringsaftrek", "verworpen-uitgaven", "notionele-intrestaftrek", "voordeel-alle-aard-auto"]),
    ("H.1", "H", "open", None, 15, "H1. Hoe dient U een rechtsgeldig bezwaar in", "H2. In welke omstandigheden",
     ["bezwaar-personenbelasting", "bezwaartermijn"]),
    ("H.2", "H", "open", None, 15, "H2. In welke omstandigheden kan de fiscale administratie", "H.3 Ik (woonachtig in Gent)",
     ["tekenen-en-indicien", "aanslagprocedure"]),
    ("H.3", "H", "open", None, 15, "H.3 Ik (woonachtig in Gent) wil mijn effecten op naam", "DEELDOMEIN VENNOOTSCHAPSRECHT",
     ["schenking-effecten", "schenkingsrechten", "successierechten", "nederlandse-notaris"]),
    ("I.1", "I", "open", None, 17, "I.1 De raad van bestuur van een NV wenst over te gaan tot een kapitaalverhoging", "I.2 Wanneer verplicht het Wetboek",
     ["toegestaan-kapitaal", "kapitaalverhoging"]),
    ("I.2", "I", "open", None, 17, "I.2 Wanneer verplicht het Wetboek van vennootschappen een financieel plan", "I.3 De zaakvoerder van een BVBA",
     ["financieel-plan", "oprichting-vennootschap"]),
    ("I.3", "I", "open", None, 18, "I.3 De zaakvoerder van een BVBA is de enige vennoot", "I.4 Kan een burgerlijke vennootschap",
     ["belangenconflict-zaakvoerder", "bijzonder-verslag"]),
    ("I.4", "I", "open", None, 18, "I.4 Kan een burgerlijke vennootschap die de rechtsvorm", "I.5 Welk is de aansprakelijkheid",
     ["burgerlijke-vennootschap", "gerechtelijk-akkoord"]),
    ("I.5", "I", "open", None, 18, "I.5 Welk is de aansprakelijkheid van de oprichters van een BVBA", "J. BEGINSELEN VAN HET ARBEIDS",
     ["oprichtersaansprakelijkheid", "bvba", "nv"]),
    ("J.1", "J", "open", None, 19, "J.1 Bart is op 1 februari 2001 in dienst getreden", "K. PLICHTENLEER",
     ["ontslag-dringende-reden", "opzegvergoeding", "termijn-betekening"]),
    ("K.1", "K", "open", None, 20, "K.1 De afgevaardigd bestuurder van een NV gespecialiseerd in het domein van de voedingsnijverheid", "K.2. Je bent stagiair BiBF",
     ["onverenigbaarheid", "bestuursmandaat", "onafhankelijkheid"]),
    ("K.2", "K", "open", None, 20, "K.2. Je bent stagiair BiBF. Bij de overdracht van een dossier stuurt jouw\nvoorganger Patrick", "K.3 Je bent stagiair BIBF. Nico",
     ["ronselen-cliënteel", "confraterrelaties-bibf", "vertrouwelijkheid"]),
    ("K.3", "K", "open", None, 21, "K.3 Je bent stagiair BIBF. Nico, een vriend", "K.4. Rik is stagiair geworden",
     ["overdracht-dossier", "aanbrengcommissie", "confraterrelaties-bibf"]),
    ("K.4", "K", "open", None, 21, "K.4. Rik is stagiair geworden nadat hij", "K.5",
     ["tuchtsanctie", "schorsing", "permanente-vorming", "lidgeld"]),
    ("K.5", "K", "open", None, 22, "K.5\nDe echtgenoten Philippe en Isabelle", "***",
     ["boekhoudvennootschap", "rechtspersoon-bibf", "doelomschrijving", "aandelenverdeling"]),
]


# ---------------------------------------------------------------------------
# Anchor-based vraag-extractie
# ---------------------------------------------------------------------------

def _collapse_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _find_anchor(full_text: str, anchor: str) -> int:
    """Vind anchor in full_text, whitespace-tolerant. Retourneert positie in originele tekst of -1.

    Strategie: voer substring-match uit op een whitespace-genormaliseerde versie van
    full_text, maar bewaar een mapping van genormaliseerde positie → originele positie.
    """
    normalized = []
    pos_map = []  # pos_map[i] = positie in full_text van character i in normalized
    in_ws = False
    for i, ch in enumerate(full_text):
        if ch.isspace():
            if not in_ws and normalized:
                normalized.append(" ")
                pos_map.append(i)
            in_ws = True
        else:
            normalized.append(ch)
            pos_map.append(i)
            in_ws = False
    norm_str = "".join(normalized)
    norm_anchor = _collapse_ws(anchor)
    idx = norm_str.find(norm_anchor)
    if idx == -1:
        return -1
    return pos_map[idx]


def extract_between(full_text: str, start_anchor: str, end_anchor: str) -> Optional[str]:
    """Geef tekstblok tussen start_anchor (inclusief) en end_anchor (exclusief).

    Whitespace-tolerant: anchors hoeven niet exact te matchen qua spaties/newlines.
    """
    s = _find_anchor(full_text, start_anchor)
    if s == -1:
        return None
    # Zoek end_anchor vanaf positie na start
    rest = full_text[s + 1 :]
    e_in_rest = _find_anchor(rest, end_anchor)
    if e_in_rest == -1:
        return full_text[s:].strip()
    return full_text[s : s + 1 + e_in_rest].strip()


def split_question_answer(block: str) -> tuple[str, Optional[str]]:
    """Splits een 2008-blok in (vraagtekst, antwoord-blok) op "Antwoord:".

    Sommige 2008-vragen hebben het antwoord direct na de opgave (zonder "Antwoord:"-label),
    dan keren we het volledige blok als vraagtekst terug (consumer moet daarmee omgaan).
    """
    # Match "Antwoord:" of "Antwoord :" of "Antwoord\n" als regel-begin
    m = re.search(r"\n\s*Antwoord\s*:?\s*\n", block)
    if m:
        vraag = block[: m.start()].strip()
        antwoord = block[m.end() :].strip()
        return vraag, antwoord
    return block.strip(), None


def truncate_motivering(antwoord: str, max_chars: int = 100) -> str:
    """Geeft eerste zin/regel van antwoord (max ~100 chars) voor `correct_antwoord`."""
    if not antwoord:
        return ""
    first_para = antwoord.split("\n\n")[0]
    first_line = first_para.split("\n")[0].strip()
    if len(first_line) <= max_chars:
        return first_line
    return first_line[:max_chars].rsplit(" ", 1)[0] + "…"


# ---------------------------------------------------------------------------
# JSON-builder
# ---------------------------------------------------------------------------

def build_vraag_record(
    examen_id: str,
    vraag_nr: str,
    vak_code: str,
    vraagtype: str,
    punten: Optional[float],
    pdf_pagina: int,
    vraagtekst: str,
    correct_antwoord: Optional[str],
    antwoord_motivering: Optional[str],
    themas: list[str],
) -> dict:
    return {
        "id": f"{examen_id}-vr{vraag_nr.replace('.', '')}",
        "vraag_nr": vraag_nr,
        "punten": punten,
        "pdf_pagina": pdf_pagina,
        "vak_code_in_pdf": vak_code,
        "vak_naam_in_pdf": SECTION_HEADERS[vak_code],
        "vraagtype": vraagtype,
        "vraagtekst": vraagtekst,
        "correct_antwoord": correct_antwoord,
        "antwoord_motivering": antwoord_motivering,
        "themas": themas,
        "wets_verwijzingen": [],
        "opties": [],
        "subvragen": [],
    }


def process_examen(
    examen_id: str,
    pdf_filename: str,
    jaar: int,
    sessie: int,
    totaal_punten: int,
    vraag_defs: list[tuple],
    has_answers: bool,
) -> dict:
    pdf_path = PDF_DIR / pdf_filename
    pages = extract_pages(pdf_path)
    full_text = "\n".join(t for _, t in pages)
    n_pages = len(pages)

    vragen = []
    for vraag_nr, vak_code, vraagtype, punten, pdf_pagina, start_anchor, end_anchor, themas in vraag_defs:
        block = extract_between(full_text, start_anchor, end_anchor)
        if block is None:
            raise RuntimeError(f"{examen_id}: vraag {vraag_nr} niet gevonden (anchor: {start_anchor!r})")

        if has_answers:
            vraagtekst, antwoord = split_question_answer(block)
            correct_antwoord = truncate_motivering(antwoord) if antwoord else None
            antwoord_motivering = normaliseer_vraagtekst(antwoord) if antwoord else None
        else:
            vraagtekst = block
            correct_antwoord = None
            antwoord_motivering = None
        vraagtekst = normaliseer_vraagtekst(vraagtekst)

        vragen.append(
            build_vraag_record(
                examen_id=examen_id,
                vraag_nr=vraag_nr,
                vak_code=vak_code,
                vraagtype=vraagtype,
                punten=punten,
                pdf_pagina=pdf_pagina,
                vraagtekst=vraagtekst,
                correct_antwoord=correct_antwoord,
                antwoord_motivering=antwoord_motivering,
                themas=themas,
            )
        )

    return {
        "examen_id": examen_id,
        "jaar": jaar,
        "sessie": sessie,
        "bron_pdf": f"resources/raw/voorbeeldexamens/{pdf_filename}",
        "totaal_punten": totaal_punten,
        "extractie": {
            "tool": TOOL_ID,
            "pdf_lib": PDF_LIB,
            "extracted_at": datetime.now(timezone.utc).isoformat(),
            "n_vragen": len(vragen),
            "n_pages": n_pages,
        },
        "vragen": vragen,
    }


# ---------------------------------------------------------------------------
# Entry
# ---------------------------------------------------------------------------

def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for examen_id, pdf_filename, jaar, sessie, totaal, vraag_defs, has_answers in [
        ("2003-bibf", "2003-bibf.pdf", 2003, 1, 100, VRAGEN_2003, False),
        ("2008-bibf", "2008-bibf.pdf", 2008, 1, 100, VRAGEN_2008, True),
    ]:
        doc = process_examen(examen_id, pdf_filename, jaar, sessie, totaal, vraag_defs, has_answers)
        out_path = OUTPUT_DIR / f"{examen_id}.json"
        out_path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"  → {out_path.relative_to(BASE_DIR)} ({doc['extractie']['n_vragen']} vragen, {doc['extractie']['n_pages']} pagina's)")

        # Verify totaal punten klopt waar mogelijk
        pt_sum = sum((v["punten"] or 0) for v in doc["vragen"])
        if has_answers:
            # 2008 heeft geen per-vraag punten
            print(f"    (2008: per-vraag punten = null; sectie-totalen via INDEX.md)")
        else:
            print(f"    punten-som: {pt_sum} (verwacht: {totaal})")


if __name__ == "__main__":
    main()
