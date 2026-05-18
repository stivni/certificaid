"""
Vragen-extractie-v1: Extraheer examenvragen uit ITAA voorbeeldexamen-PDFs.

Deterministisch script — geen LLM-calls. Gebruikt pdfplumber voor PDF-extractie.
Themas worden op basis van trefwoorden toegewezen (niet gegenereerd).
"""

import json
import re
import pdfplumber
from datetime import datetime
from pathlib import Path

from tools.examen._sub_vragen_splitter import splits_in_sub_vragen
from tools.examen._vraagtekst_normalisatie import normaliseer as normaliseer_vraagtekst

TOOL_ID = "vragen-extractie-v1"
PDF_LIB = "pdfplumber"
BASE_DIR = Path("/Users/stivni/Documents/ITAA/certificaid")
OUTPUT_DIR = BASE_DIR / "data" / "examen_vragen"
PDF_DIR = BASE_DIR / "resources" / "raw" / "voorbeeldexamens"

EXAMEN_CONFIGS = {
    "2013-1": {
        "jaar": 2013,
        "sessie": 1,
        "pdf_bestand": "2013-1.pdf",
        "totaal_punten": 150,
    },
    "2013-2": {
        "jaar": 2013,
        "sessie": 2,
        "pdf_bestand": "2013-2.pdf",
        "totaal_punten": 150,
    },
    "2014-1": {
        "jaar": 2014,
        "sessie": 1,
        "pdf_bestand": "2014-1.pdf",
        "totaal_punten": 150,
    },
    "2015-1": {
        "jaar": 2015,
        "sessie": 1,
        "pdf_bestand": "2015_1_-_bekwaamheidsexamen_ac_1.pdf",
        "totaal_punten": 150,
    },
    "2024-1": {
        "jaar": 2024,
        "sessie": 1,
        "pdf_bestand": "Vragen schriftelijk bekwaamheidsexamen ITAA 2024.pdf",
        "totaal_punten": None,
    },
}

# Exacte sectietitelpatronen per examen (in volgorde van voorkomen)
# Formaat: (regex_patroon, vak_code, vak_naam)
# De regex matcht de sectietitel in de platte tekst
EXAMEN_VAK_PATRONEN = {
    "2013-1": [
        (r"WETGEVING INZAKE DE JAARREKENING\s+15\s+PUNTEN",
         "1.1", "Wetgeving inzake de jaarrekening"),
        (r"ANALYSE EN KRITISCHE BEOORDELING VAN DE\s+25\s+PUNTEN",
         "1.2", "Analyse en kritische beoordeling van de jaarrekening"),
        (r"INTERNE CONTROLE EN ACCOUNTANTSONDERZOEK\s+50\s+PUNTEN",
         "1.3", "Interne controle en accountantsonderzoek"),
        (r"VENNOOTSCHAPSRECHT\s+20\s+PUNTEN",
         "3.1", "Vennootschapsrecht"),
        (r"VENNOOTSCHAPSRECHT\s+\(BIJZONDERE MANDATEN\)\s+30\s+PUNTEN",
         "3.2", "Vennootschapsrecht (bijzondere mandaten)"),
        (r"PERSONENBELASTING\s+20\s+PUNTEN",
         "2.1", "Personenbelasting"),
        (r"VENNOOTSCHAPSBELASTING\s+20\s+PUNTEN",
         "2.2", "Vennootschapsbelasting"),
        (r"BELASTING OVER DE TOEGEVOEGDE WAARDE\s+15\s+PUNTEN",
         "2.3", "Belasting over de toegevoegde waarde"),
        (r"BEGINSELEN VAN REGISTRATIE-\s*EN\s+10\s+PUNTEN",
         "2.4", "Beginselen van registratie- en successierechten"),
        (r"BEGINSELEN VAN EUROPEES EN INTERNATIONAAL\s+10\s+PUNTEN",
         "2.6", "Beginselen van Europees en internationaal fiscaal recht"),
        (r"FISCALE PROCEDURE\s+15\s+PUNTEN",
         "2.7", "Fiscale procedure"),
        (r"JURIDISCHE EN BEROEPSNORMEN MET BETREKKING\s+20\s+PUNTEN",
         "4.0", "Juridische en beroepsnormen / deontologie"),
    ],
    "2013-2": [
        (r"WETGEVING INZAKE DE JAARREKENING\s+15\s+PUNTEN",
         "1.1", "Wetgeving inzake de jaarrekening"),
        (r"(?:25\s+PUNTEN\s*\n)?ANALYSE EN KRITISCHE BEOORDELING VAN DE\s*\n?JAARREKENING",
         "1.2", "Analyse en kritische beoordeling van de jaarrekening"),
        (r"INTERNE CONTROLE EN ACCOUNTANTSONDERZOEK\s+50\s+PUNTEN",
         "1.3", "Interne controle en accountantsonderzoek"),
        (r"VENNOOTSCHAPSRECHT\s+20\s+PUNTEN",
         "3.1", "Vennootschapsrecht"),
        (r"VENNOOTSCHAPSRECHT\s+\(BIJZONDERE MANDATEN\)\s+30\s+PUNTEN",
         "3.2", "Vennootschapsrecht (bijzondere mandaten)"),
        (r"PERSONENBELASTING\s+20\s+PUNTEN",
         "2.1", "Personenbelasting"),
        (r"VENNOOTSCHAPSBELASTING\s+20\s+PUNTEN",
         "2.2", "Vennootschapsbelasting"),
        (r"BELASTING OVER DE TOEGEVOEGDE WAARDE\s+15\s+PUNTEN",
         "2.3", "Belasting over de toegevoegde waarde"),
        (r"BEGINSELEN VAN REGISTRATIE-\s*EN\s+10\s+PUNTEN",
         "2.4", "Beginselen van registratie- en successierechten"),
        (r"BEGINSELEN VAN EUROPEES EN INTERNATIONAAL\s+10\s+PUNTEN",
         "2.6", "Beginselen van Europees en internationaal fiscaal recht"),
        (r"FISCALE PROCEDURE\s+15\s+PUNTEN",
         "2.7", "Fiscale procedure"),
        (r"JURIDISCHE EN BEROEPSNORMEN MET BETREKKING\s+20\s+PUNTEN",
         "4.0", "Juridische en beroepsnormen / deontologie"),
    ],
    "2014-1": [
        (r"WETGEVING INZAKE DE JAARREKENING\s+15\s+PUNTEN",
         "1.1", "Wetgeving inzake de jaarrekening"),
        (r"ANALYSE EN KRITISCHE BEOORDELING VAN DE\s+25\s+PUNTEN",
         "1.2", "Analyse en kritische beoordeling van de jaarrekening"),
        (r"INTERNE CONTROLE\s+25\s+PUNTEN",
         "1.3 IC", "Interne controle"),
        (r"ACCOUNTANTSONDERZOEK\s+25\s+PUNTEN",
         "1.3 AO", "Accountantsonderzoek"),
        (r"VENNOOTSCHAPSRECHT\s+20\s+PUNTEN",
         "3.1", "Vennootschapsrecht"),
        (r"VENNOOTSCHAPSRECHT\s+\(BIJZONDERE MANDATEN\)\s+30\s+PUNTEN",
         "3.2", "Vennootschapsrecht (bijzondere mandaten)"),
        (r"PERSONENBELASTING\s+20\s+PUNTEN",
         "2.1", "Personenbelasting"),
        (r"VENNOOTSCHAPSBELASTING\s+20\s+PUNTEN",
         "2.2", "Vennootschapsbelasting"),
        (r"BELASTING OVER DE TOEGEVOEGDE WAARDE\s+15\s+PUNTEN",
         "2.3", "Belasting over de toegevoegde waarde"),
        (r"BEGINSELEN VAN REGISTRATIE-\s*EN\s+10\s+PUNTEN",
         "2.4", "Beginselen van registratie- en successierechten"),
        (r"BEGINSELEN VAN EUROPEES EN INTERNATIONAAL\s+10\s+PUNTEN",
         "2.6", "Beginselen van Europees en internationaal fiscaal recht"),
        (r"FISCALE PROCEDURE\s+15\s+PUNTEN",
         "2.7", "Fiscale procedure"),
        (r"JURIDISCHE EN BEROEPSNORMEN MET BETREKKING\s+20\s+PUNTEN",
         "4.0", "Juridische en beroepsnormen / deontologie"),
    ],
    "2015-1": [
        (r"WETGEVING INZAKE DE JAARREKENING\s+15\s+PUNTEN",
         "1.1", "Wetgeving inzake de jaarrekening"),
        (r"ANALYSE EN KRITISCHE BEOORDELING VAN DE\s+25\s+PUNTEN",
         "1.2", "Analyse en kritische beoordeling van de jaarrekening"),
        (r"INTERNE CONTROLE\s+25\s+PUNTEN",
         "1.3 IC", "Interne controle"),
        (r"ACCOUNTANTSONDERZOEK\s+25\s+PUNTEN",
         "1.3 AO", "Accountantsonderzoek"),
        (r"VENNOOTSCHAPSRECHT\s+20\s+PUNTEN",
         "3.1", "Vennootschapsrecht"),
        (r"VENNOOTSCHAPSRECHT\s+\(BIJZONDERE MANDATEN\)\s+30\s+PUNTEN",
         "3.2", "Vennootschapsrecht (bijzondere mandaten)"),
        (r"PERSONENBELASTING\s+20\s+PUNTEN",
         "2.1", "Personenbelasting"),
        (r"VENNOOTSCHAPSBELASTING\s+20\s+PUNTEN",
         "2.2", "Vennootschapsbelasting"),
        (r"BELASTING OVER DE TOEGEVOEGDE WAARDE\s+15\s+PUNTEN",
         "2.3", "Belasting over de toegevoegde waarde"),
        (r"FISCALE PROCEDURE\s+15\s+PUNTEN",
         "2.7", "Fiscale procedure"),
        (r"BEGINSELEN VAN REGISTRATIE-\s*EN\s+10\s+PUNTEN",
         "2.4", "Beginselen van registratie- en successierechten"),
        (r"BEGINSELEN VAN EUROPEES EN INTERNATIONAAL\s+10\s+PUNTEN",
         "2.6", "Beginselen van Europees en internationaal fiscaal recht"),
        (r"JURIDISCHE EN BEROEPSNORMEN MET BETREKKING\s+20\s+PUNTEN",
         "4.0", "Juridische en beroepsnormen / deontologie"),
    ],
}


def extract_pdf_pages(pdf_path: Path) -> tuple[list[str], int]:
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            pages.append(text)
    return pages, len(pages)


def strip_studocu(text: str) -> str:
    text = re.sub(r"lOMoARcPSD\|\d+\n?", "", text)
    text = re.sub(r"Downloaded by[^\n]+\n?", "", text)
    text = re.sub(r"SSccaann.*?\n", "", text)
    text = re.sub(r"SSttuuddooccuu.*?\n", "", text)
    return text


def detect_vraagtype(tekst: str, opties: list) -> str:
    tl = tekst.lower()
    if any(k in tl for k in ["juist", "fout", "waar", "niet waar"]):
        return "J/F"
    if opties and len(opties) >= 2:
        if any(k in tl for k in ["bereken", "berekening"]):
            return "berekening+MC"
        return "MC"
    if any(k in tl for k in ["bereken", "berekening", "bepaal het bedrag", "bereken het bedrag"]):
        return "berekening"
    return "open"


def extract_themas(tekst: str) -> list[str]:
    tl = tekst.lower()
    themas = []
    mapping = [
        (["alarmbel"], "alarmbelprocedure"),
        (["consolidatieverschil", "consolidatietabel", "consolidatiepercentage", "geconsolideerde jaarrekening"], "consolidatie"),
        (["functiescheiding", "ic-doel", "interne controle doelstelling"], "interne-controle"),
        (["omzett", "omvorming", "controleverslag omzet"], "omzetting-vennootschap"),
        (["antiwitwas", "cfi", "compliance officer", "witwasverantwoordelijke", "ubo-register", "amlco"], "antiwitwaswet"),
        (["beroepsgeheim", "discretieplicht"], "beroepsgeheim"),
        (["onafhankelijkheid", "bestuursmandaat", "patrimoniumvennootschap", "monopolieopdracht"], "onafhankelijkheid"),
        (["btw-aftrek", "btw-rooster", "herziening aftrek", "belasting over de toegevoegde"], "btw"),
        (["personenwagen", "firmawagen", "voordeel alle aard wagen"], "personenwagen-btw"),
        (["stopzettingsmeerwaarde"], "stopzettingsmeerwaarden"),
        (["gespreide taxatie", "gespreide belasting"], "gespreide-taxatie"),
        (["voorziening", "grote herstellingen"], "voorzieningen"),
        (["successierecht", "nalatenschap", "legataris", "testament"], "successierechten"),
        (["registratierecht"], "registratierechten"),
        (["oeso", "dubbelbelasting", "vaste inrichting", "bijkantoor", "moeder-dochterrichtlijn"], "internationaal-fiscaal-recht"),
        (["thin cap", "notionele intrest", "dbi", "verworpen uitgaven"], "vennootschapsbelasting"),
        (["huwelijksquotiënt", "kadastraal inkomen"], "personenbelasting"),
        (["bevestigingsbrief", "confirmatie", "confirmatiebrieven"], "confirmatiebrieven"),
        (["brutoverkoopmarge", "nettobedrijfskapitaal", "liquiditeit in", "rentabiliteit"], "jaarrekeninganalyse"),
        (["ontbinding", "vereffening"], "ontbinding-vereffening"),
        (["vraag om inlichtingen", "onderzoekstermijn", "verjaring", "inkohiering"], "fiscale-procedure"),
        (["kwaliteitstoetsing", "permanente vorming", "confrater"], "beroepsnormen"),
        (["contantengr", "contante betaling"], "contantengrens"),
        (["kapitaalverhoging", "kapitaalvermindering", "vastklik"], "kapitaaloperaties"),
        (["herwaarderingsmeerwaarde"], "herwaarderingsmeerwaarden"),
        (["interimdividend"], "dividend"),
        (["nettothesaurie", "werkkapitaalbehoefte"], "werkkapitaalbehoefte"),
        (["interne pensioenbelofte"], "interne-pensioenbelofte"),
        (["dbi-aftrek", "definitief belaste inkomsten"], "dbi-aftrek"),
        (["overdraagbare verlies", "overgedragen verlies"], "fiscale-verliezen"),
        (["transfer pricing", "abnormaal voordeel"], "transfer-pricing"),
        (["ifrs", "ias "], "ifrs"),
        (["wvv", "wetboek vennootschappen en verenigingen"], "wvv"),
        (["liquidatietest"], "liquidatietest"),
        (["quasi inbreng"], "quasi-inbreng"),
        (["margeregeling", "vat refund"], "btw-margeregeling"),
        (["software", "immateriële vaste activa", "immaterieel vast"], "immateriële-vaste-activa"),
        (["goodwill", "meerprijs", "overnamepremie"], "goodwill"),
        (["afschrijving", "afschrijvingsregel", "afschrijvingspercentage"], "afschrijvingen"),
        (["auditmethode", "auditprocedure", "onthoudende verklaring", "controleverklaring"], "auditopdracht"),
        (["toegestaan kapitaal", "machtiging kapitaal"], "toegestaan-kapitaal"),
        (["individueel controlerecht", "controlerecht vennoot"], "individueel-controlerecht"),
        (["onderhoudsuitkering", "alimentatie", "onderhoud echtgenoot"], "onderhoudsuitkering"),
        (["aandelenportefeuille", "aandelen portefeuille", "effectenportefeuille"], "beleggingsportefeuille"),
        (["woonstaatheffing", "roerende voorheffing", "dividendbelasting"], "roerende-voorheffing"),
        (["bezwaar aanslag", "bezwaarschrift", "ambtshalve aanslag"], "belastingprocedure"),
        (["stopzetting btw", "stop btw", "herziening recht op aftrek"], "btw-stopzetting"),
        (["bvba", "nv", "cvba", "vennootschapsvormen", "rechtsvormen"], "vennootschapsrecht"),
        (["sociale balans", "sociale lasten", "rsz"], "sociale-bijdragen"),
        (["herwaardering", "herwaarderingswaarde"], "herwaarderingsmeerwaarden"),
        (["inbreng natura", "inbreng in natura"], "inbreng-in-natura"),
        (["continuïteit", "going concern"], "continuiteitsbeginsel"),
        (["jaarverslag", "bestuursverslag"], "jaarverslag"),
        (["statutaire reserve", "wettelijke reserve"], "reserves"),
        (["kapitaalsubsidie", "investeringssubsidie"], "kapitaalsubsidies"),
        (["intercalaire interest", "geactiveerde intrest"], "intercalaire-intresten"),
        (["vereffenaar", "liquidateur", "vereffening bvba"], "ontbinding-vereffening"),
        (["intrinsieke waarde", "fractiewaarde", "schuldgraad", "operationele cash flow", "netto rendabiliteit"], "financiële-begrippen"),
        (["analytische test", "cijferbeoordeling", "analytische procedure"], "analytische-procedures"),
        (["budget interne controle", "budget van de interne"], "interne-controle"),
        (["publiciteit accountant", "reclame accountant", "publiciteit voeren"], "publiciteit-beroepsnormen"),
        (["btw-aangifte", "roosters van de btw", "btw-rooster invullen", "btw aangifte rooster"], "btw-aangifte"),
        (["dakwerk", "bouwdienst", "onroerende dienst", "dienst onroerend goed"], "btw-plaatsbepaling"),
        (["faillissementsboedel", "openbaar verkoop", "curator"], "btw-bijzondere-regelingen"),
        (["belastingplichtige bijberoep", "drempel kleine ondernemer"], "btw-vrijstellingsregeling"),
        (["trein paris", "dienst in voertuig", "plaats van dienst"], "btw-plaatsbepaling"),
        (["b2b dienst", "intracommunautaire dienst", "britse onderneming btw"], "btw-plaatsbepaling"),
        (["koopbelofte", "stroman", "lasthebber anoniem"], "registratierechten"),
        (["hoedanigheid begiftigde", "wettelijk erfgenaam", "legataris algemeen", "bijzonder legataris"], "successierechten"),
        (["functiescheiding taken", "autorisatie bewaren registratie", "inkoopcyclus"], "interne-controle"),
        (["klantenfiches", "verkoopafdeling risico", "nieuwe klant aanmaken"], "interne-controle"),
        (["erelonen advocaat", "gerechtelijke kosten", "voorziening rechtszaak"], "auditopdracht"),
        (["consolidatietabel", "controlepercentage", "belang percentage"], "consolidatie"),
        (["disconto vordering", "lange termijn vordering", "contante waarde"], "waarderingsregels"),
        (["diverse inkomsten", "artikel 90", "occasionele verrichting"], "personenbelasting"),
        (["herschilderen", "groot onderhoud gebouw", "schilderwerk"], "voorzieningen"),
        (["onderhoudsuitkering kapitaalvorm", "alimentatie kapitaal", "éénmalige onderhouds"], "onderhoudsuitkering"),
        (["aandelenportefeuille", "meerwaarde aandelen", "dbi-aftrek aandelen"], "beleggingsportefeuille"),
        (["woonstaatheffing", "luxemburgse interesten", "interesten buitenland"], "internationale-belasting"),
        (["bewaringsplicht", "bewaarplicht bestelbonnen"], "fiscale-procedure"),
        (["onderzoekstermijn personenbelasting", "5 jaar pb", "7 jaar pb"], "fiscale-procedure"),
        (["btw vzw", "vrijgestelde vzw", "gemengde belastingplichtige"], "btw"),
        (["driehoeksverkeer", "intracommunautaire levering", "ic-levering"], "btw-intracommunautair"),
        (["niet-overbrenging", "register niet-overbrengingen", "laptop gsm filiaal"], "btw"),
        (["fusierichtlijn", "ivzw splitsing", "grensoverschrijdende fusie"], "fusierichtlijn"),
        (["oeso pensioen", "ambtenaar pensioen", "dubbele nationaliteit"], "internationaal-fiscaal-recht"),
        (["adjustments", "aanvaardingsprocedure accountant"], "auditopdracht"),
        (["deontologisch probleem", "beroepsbeoefenaar weigeren"], "beroepsnormen"),
        (["verkoopscyclus doelstelling", "verkoopcyclus", "financieel operationeel conformiteit"], "interne-controle"),
    ]
    for keywords, tag in mapping:
        if any(k in tl for k in keywords):
            themas.append(tag)
    return themas[:5]


def extract_wetsrefs(tekst: str) -> list[str]:
    refs = []
    patterns = [
        r"art(?:ikel)?\.?\s*\d+[a-z]?(?:\s*[,/]\s*\d+)?(?:\s*§\s*\d+)?\s*(?:W(?:VV|IB|BTW|\.Venn\.?)|KB|BW|AWW)",
        r"(?:W(?:VV|IB\s*(?:19)?92|BTW)|W\.Venn\.)\s*art(?:ikel)?\.?\s*\d+",
        r"artikel\s+9\d[,\s]+\d°\s+WIB",
        r"(?:richtlijn|RL)\s*\d{4}/\d+/(?:EG|EU|EEG)",
        r"KB\s*(?:van\s*)?\d{1,2}[/-]\d{1,2}[/-]\d{2,4}",
    ]
    for p in patterns:
        for f in re.findall(p, tekst, re.IGNORECASE):
            fc = f.strip()
            if fc and fc not in refs:
                refs.append(fc)
    return refs[:10]


def parse_opties(blok: str) -> list[dict]:
    opties = []
    # Patroon: expliciete A./B./C. labels
    pat = re.compile(
        r"^\s*([A-Da-d])[.)]\s*(.+?)(?=^\s*[A-Da-d][.)]\s|\Z)",
        re.MULTILINE | re.DOTALL
    )
    matches = list(pat.finditer(blok))
    if matches and len(matches) >= 2:
        for m in matches:
            opties.append({"label": m.group(1).upper(), "tekst": m.group(2).strip()[:300]})
        return opties

    # Patroon: alinea's na "Antwoord"
    pos = blok.find("\nAntwoord")
    if pos == -1:
        pos = blok.find("Antwoord")
    if pos >= 0:
        na = blok[pos + len("Antwoord"):].strip()
        alineas = [a.strip() for a in re.split(r"\n{2,}", na) if a.strip() and len(a.strip()) > 8]
        alineas = [a for a in alineas if not re.match(r"^(Vraag\s+\d|VRAAG|Downloaded|\*)", a)]
        if len(alineas) >= 2:
            for i, a in enumerate(alineas[:6]):
                opties.append({"label": chr(65 + i), "tekst": a[:300]})
    return opties


def parse_subvragen(blok: str) -> list[dict]:
    subvragen = []
    pat = re.compile(
        r"(?:^|\n)\s*([a-f])\)\s+(.+?)(?=\n\s*[a-f]\)\s|\n\s*Antwoord\b|\n\s*Vraag\s+\d|\Z)",
        re.DOTALL | re.MULTILINE
    )
    for m in pat.finditer(blok):
        label = m.group(1) + ")"
        subtekst = m.group(2).strip()
        pm = re.search(r"[….]{1,3}\s*/\s*([\d,]+)\s*punt(?:en)?", subtekst)
        punten = float(pm.group(1).replace(",", ".")) if pm else None
        if subtekst:
            subvragen.append({"label": label, "tekst": subtekst[:500], "punten": punten})
    return subvragen


def pagina_van_tekst(zoektekst: str, pages: list[str]) -> int:
    """Zoek pagina (1-indexed) waar deze tekst voorkomt."""
    for i, p in enumerate(pages):
        if zoektekst in p:
            return i + 1
    return 1


def extract_vragen_uit_sectie(
    sectie_tekst: str,
    vak_code: str,
    vak_naam: str,
    examen_id: str,
    vr_counter_start: int,
    pages: list[str],
) -> tuple[list[dict], int]:
    vragen = []
    vr_counter = vr_counter_start

    # Splits sectie op vraagnummers
    blokken = re.split(r"(?=\nVraag\s+\d+[a-z]?\s*[….]{0,3}\s*(?:/|\Z))", sectie_tekst)
    vraag_blokken = [b.strip() for b in blokken if re.search(r"^Vraag\s+\d+", b.strip())]

    for blok in vraag_blokken:
        kop = re.match(
            r"Vraag\s+(\d+[a-z]?)\s*[….]{0,3}\s*(?:/\s*([\d,]+)\s*punt(?:en)?)?",
            blok, re.IGNORECASE
        )
        if not kop:
            continue

        vraag_nr = kop.group(1)
        punten = float(kop.group(2).replace(",", ".")) if kop.group(2) else None

        # Zoek pagina via uniek fragment
        fragment = blok[:80].replace("\n", " ").strip()
        pdf_pagina = 1
        for i, p in enumerate(pages):
            if re.search(rf"Vraag\s+{re.escape(vraag_nr)}\s", p):
                # Extra check: bevat de pagina ook een woord uit het fragment?
                frag_words = fragment.split()[:5]
                if any(w in p for w in frag_words if len(w) > 4):
                    pdf_pagina = i + 1
                    break
                pdf_pagina = i + 1  # Eerste match als fallback

        vraagtekst = normaliseer_vraagtekst(blok[:2000])
        opties = parse_opties(blok)
        subvragen = parse_subvragen(blok)
        vraagtype = detect_vraagtype(blok, opties)
        themas = extract_themas(blok)
        wets_refs = extract_wetsrefs(blok)

        vr_counter += 1
        vraag: dict = {
            "id": f"{examen_id}-vr{vr_counter}",
            "vraag_nr": vraag_nr,
            "punten": punten,
            "pdf_pagina": pdf_pagina,
            "vak_code_in_pdf": vak_code,
            "vak_naam_in_pdf": vak_naam,
            "vraagtype": vraagtype,
            "vraagtekst": vraagtekst,
            "sub_vragen": splits_in_sub_vragen(vraagtekst),
            "correct_antwoord": None,
            "antwoord_motivering": None,
            "themas": themas,
            "wets_verwijzingen": wets_refs,
        }
        if opties:
            vraag["opties"] = opties
        if subvragen:
            vraag["subvragen"] = subvragen

        vragen.append(vraag)

    return vragen, vr_counter


def split_tekst_op_secties(
    volledige_tekst: str,
    patronen: list[tuple[str, str, str]],
) -> list[tuple[str, str, str]]:
    """
    Splits de volledige tekst op sectietitels.
    Geeft lijst van (vak_code, vak_naam, sectie_tekst) terug.
    """
    # Vind alle sectieposities
    gevonden: list[tuple[int, int, str, str]] = []  # (start, eind_van_titel, code, naam)
    for patroon, code, naam in patronen:
        m = re.search(patroon, volledige_tekst, re.IGNORECASE)
        if m:
            gevonden.append((m.start(), m.end(), code, naam))

    if not gevonden:
        return [("onbekend", "Onbekend", volledige_tekst)]

    # Sorteer op positie
    gevonden.sort(key=lambda x: x[0])

    # Bouw secties
    secties = []
    for i, (start, eind_titel, code, naam) in enumerate(gevonden):
        sectie_start = start  # inclusief sectietitel
        sectie_eind = gevonden[i + 1][0] if i + 1 < len(gevonden) else len(volledige_tekst)
        sectie_tekst = volledige_tekst[sectie_start:sectie_eind]
        secties.append((code, naam, sectie_tekst))

    return secties


def parse_standaard_examen(pages: list[str], examen_id: str) -> list[dict]:
    volledige_tekst = strip_studocu("\n".join(pages))
    patronen = EXAMEN_VAK_PATRONEN[examen_id]
    secties = split_tekst_op_secties(volledige_tekst, patronen)

    alle_vragen = []
    vr_counter = 0

    for vak_code, vak_naam, sectie_tekst in secties:
        vragen, vr_counter = extract_vragen_uit_sectie(
            sectie_tekst, vak_code, vak_naam, examen_id, vr_counter, pages
        )
        alle_vragen.extend(vragen)

    return alle_vragen


def parse_2024_1(pages: list[str]) -> list[dict]:
    vragen = []
    examen_id = "2024-1"

    vraag_vak_mapping = {
        "1":  ("3.1",                   "Vennootschapsrecht"),
        "2":  ("1.3 Externe controle",  "Externe controle / accountantsonderzoek"),
        "3":  ("1.3 Interne controle",  "Interne controle"),
        "4":  ("3.2",                   "Bijzondere mandaten — ontbinding/omzetting"),
        "5":  ("2.1",                   "Personenbelasting"),
        "6":  ("4.0",                   "Deontologie en AWW"),
        "7":  ("1.1/IFRS",              "Wetgeving jaarrekening + IFRS"),
        "8":  ("2.2",                   "Vennootschapsbelasting"),
        "9":  ("2.7",                   "Fiscale procedure"),
        "10": ("1.2",                   "Analyse en kritische beoordeling jaarrekening"),
        "11": ("2.3",                   "BTW"),
    }

    volledige_tekst = strip_studocu("\n".join(pages))

    # 2024-1: Hoofdvragen "1 Vennootschapsrecht", "2 Externe controle" etc.
    patroon = re.compile(r"(?:^|\n)(\d{1,2})\s+([A-Z][^\n]+)", re.MULTILINE)
    matches = list(patroon.finditer(volledige_tekst))

    vr_counter = 0
    for i, m in enumerate(matches):
        nr = m.group(1)
        if nr not in vraag_vak_mapping:
            continue
        vak_code, vak_naam = vraag_vak_mapping[nr]
        start = m.start()
        eind = matches[i + 1].start() if i + 1 < len(matches) else len(volledige_tekst)
        blok = volledige_tekst[start:eind].strip()

        pdf_pagina = 1
        for pag_nr, p in enumerate(pages, start=1):
            if re.search(rf"^{re.escape(nr)}\s+[A-Z]", p, re.MULTILINE):
                pdf_pagina = pag_nr
                break

        opties = parse_opties(blok)
        subvragen = parse_subvragen(blok)
        vraagtype = detect_vraagtype(blok, opties)
        themas = extract_themas(blok)
        wets_refs = extract_wetsrefs(blok)

        vr_counter += 1
        norm_vraagtekst = normaliseer_vraagtekst(blok[:2000])
        vraag: dict = {
            "id": f"{examen_id}-vr{vr_counter}",
            "vraag_nr": nr,
            "punten": None,
            "pdf_pagina": pdf_pagina,
            "vak_code_in_pdf": vak_code,
            "vak_naam_in_pdf": vak_naam,
            "vraagtype": vraagtype,
            "vraagtekst": norm_vraagtekst,
            "sub_vragen": splits_in_sub_vragen(norm_vraagtekst),
            "correct_antwoord": None,
            "antwoord_motivering": None,
            "themas": themas,
            "wets_verwijzingen": wets_refs,
        }
        if opties:
            vraag["opties"] = opties
        if subvragen:
            vraag["subvragen"] = subvragen
        vragen.append(vraag)

    return vragen


def run_extractie():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for examen_id, config in EXAMEN_CONFIGS.items():
        pdf_path = PDF_DIR / config["pdf_bestand"]
        print(f"\n[{examen_id}] Extractie van {pdf_path.name} ...")

        pages, n_pages = extract_pdf_pages(pdf_path)

        if examen_id == "2024-1":
            vragen = parse_2024_1(pages)
        else:
            vragen = parse_standaard_examen(pages, examen_id)

        totaal_gevonden = sum(v["punten"] for v in vragen if v["punten"] is not None)

        output = {
            "examen_id": examen_id,
            "jaar": config["jaar"],
            "sessie": config["sessie"],
            "bron_pdf": f"resources/raw/voorbeeldexamens/{config['pdf_bestand']}",
            "totaal_punten": config["totaal_punten"],
            "extractie": {
                "tool": TOOL_ID,
                "pdf_lib": PDF_LIB,
                "extracted_at": datetime.now().isoformat(),
                "n_vragen": len(vragen),
                "n_pages": n_pages,
            },
            "vragen": vragen,
        }

        output_path = OUTPUT_DIR / f"{examen_id}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)

        print(f"  → {len(vragen)} vragen | {totaal_gevonden:.0f} punten"
              f" (verwacht {config['totaal_punten']}) | {n_pages} pagina's")


if __name__ == "__main__":
    run_extractie()
