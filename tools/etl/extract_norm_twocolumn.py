#!/usr/bin/env python3
"""Re-extractie van twee-kolom norm-PDFs via pymupdf block-extractie.

Pakt drie norm-PDFs aan die door pdftotext/-layout slecht werden geconverteerd:

  - ITAA-norm-intern-kwaliteitsmanagement.md
      Type "bilingual": landscape A4, NL (x0 < 415) + FR (x0 > 415).
      Alleen de NL-kolom wordt geextraheerd.

  - ITAA-norm-effectennorm.md
  - ITAA-norm-samenstellingsopdrachten-isrs4410.md
      Type "vereisten": staand A4, VEREISTEN (links) + TOEPASSINGSMODALITEITEN (rechts).
      Beide kolommen als aparte secties in lineaire volgorde.

Gebruik:
  python tools/etl/extract_norm_twocolumn.py                    # alle bekende PDFs
  python tools/etl/extract_norm_twocolumn.py --file ITAA-norm-intern-kwaliteitsmanagement.md
  python tools/etl/extract_norm_twocolumn.py --dry-run          # toon info, schrijf niet
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import pymupdf  # type: ignore  # fitz-alias; version 1.27+

ROOT = Path(__file__).resolve().parent.parent.parent

# ─── Bron-configuratie ────────────────────────────────────────────────────────

KNOWN_PDFS: dict[str, dict] = {
    "ITAA-norm-intern-kwaliteitsmanagement.md": {
        "pdf": ROOT / "resources" / "raw" / "normen" / "beexcellent-2640-kwaliteitsmanagement.pdf",
        "type": "bilingual",
        "column_split": 415,   # x-waarde: links van hier = NL, rechts = FR
    },
    "ITAA-norm-effectennorm.md": {
        "pdf": ROOT / "resources" / "raw" / "normen" / "beexcellent-2692-effectennorm.pdf",
        "type": "vereisten",
        "column_split": 400,
        "full_width_threshold": 400,  # blokken breder dan dit = sectieheader of label-rij
    },
    "ITAA-norm-samenstellingsopdrachten-isrs4410.md": {
        "pdf": ROOT / "resources" / "raw" / "normen" / "beexcellent-2091-isrs4410.pdf",
        "type": "vereisten",
        "column_split": 400,
        "full_width_threshold": 400,
    },
    "ITAA-norm-ontbinding-vereffening.md": {
        "pdf": ROOT / "resources" / "raw" / "normen" / "beexcellent-ontbinding-vereffening.pdf",
        "type": "vereisten",
        "column_split": 400,
        "full_width_threshold": 400,
    },
    "ITAA-norm-aww-geconsolideerd.md": {
        "pdf": ROOT / "resources" / "raw" / "normen" / "beexcellent-416-aww-geconsolideerd.pdf",
        "type": "vereisten",
        "column_split": 300,
        "full_width_threshold": 400,
    },
    # NL-only enkelkolom-PDFs (geen FR-kolom): we extraheren met `pdftotext -layout`
    # zodat we de bilingual-blok-decompositie en de FR-false-positive-detectie omzeilen.
    "ITAA-norm-aww-richtlijn-bibf.md": {
        "pdf": ROOT / "resources" / "raw" / "normen" / "beexcellent-4-bibf-aww.pdf",
        "type": "nl-singlecol",
    },
    "ITAA-norm-gedragslijnen-relaties-IBR.md": {
        "pdf": ROOT / "resources" / "raw" / "normen" / "gedragslijnen-relaties-IBR.pdf",
        "type": "nl-singlecol",
    },
    "ITAA-norm-opdrachtbrief.md": {
        "pdf": ROOT / "resources" / "raw" / "normen" / "nota-opdrachtbrief.pdf",
        "type": "nl-singlecol",
    },
    "ITAA-norm-aww-procedurereglement.md": {
        "pdf": ROOT / "resources" / "raw" / "normen" / "procedurereglement-AWW-art118.pdf",
        "type": "nl-singlecol",
    },
}  # Uitbreiding mogelijk: voeg hier andere twee-kolom PDFs toe met hun type-config

NORMEN_DIR = ROOT / "resources" / "bronnen" / "normen"

# ─── Regex-hulppatronen ────────────────────────────────────────────────────────

_RE_FORMFEED = re.compile(r"\x0c")
_RE_PAGE_NUM = re.compile(r"^\s*\d+\s*$")                        # losse paginanummers
_RE_PAGE_NofN = re.compile(r"^\s*(?:Page\s+)?\d+\s*/\s*\d+\s*$", re.IGNORECASE)
_RE_PAGE_NofN2 = re.compile(r"^\s*Page\s+\d+\s+of\s+\d+\s*$", re.IGNORECASE)
_RE_HERFORMULERING = re.compile(r"^\s*Herformulering\s+\w+\s+\d{4}\s*", re.IGNORECASE)
_RE_COPYRIGHT_IFAC = re.compile(r"Copyright\s+IFAC", re.IGNORECASE)
_RE_COPYRIGHT_ITAA = re.compile(r"©\s*ITAA", re.IGNORECASE)
_RE_BLANK_EXCESS = re.compile(r"\n{4,}")

# Soft-wrap samenvoegen: regels die geen structurele opener zijn
_RE_SOFT_WRAP_KEEP_SEPARATE = re.compile(
    r"^(?:"
    r"#{1,6}\s"                        # markdown heading
    r"|§\s*\d"                         # § N
    r"|\d+°"                           # 1°
    r"|\d+\.\s"                        # 1. (paragraaf)
    r"|[a-z]\)\s"                      # a) lijst
    r"|\([a-z]+\)\s"                   # (a) of (i) lijst
    r"|\([ivxlcdmIVXLCDM]+\)\s"        # (i), (ii), (iii) Romeinse lijst
    r"|-\s"                            # - bullet
    r"|•\s"                            # • bullet
    r"|HOOFDSTUK\b|TITEL\b|BOEK\b"
    r")"
)

# ─── Frontmatter helpers ───────────────────────────────────────────────────────

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def split_frontmatter(text: str) -> tuple[str, str]:
    """Geef (frontmatter_met_delimiters, body). Leeg-string als geen frontmatter."""
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return text[: m.end()], text[m.end():]


# ─── Tekst-opkuis per blok ────────────────────────────────────────────────────

def clean_block_text(text: str) -> str:
    """Basisopkuis van pymupdf-blok tekst."""
    # Verwijder form-feeds
    text = _RE_FORMFEED.sub("", text)
    # Normaliseer interne regeleindes: meerdere \n binnen blok → één \n
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()


def merge_intra_block_soft_wraps(text: str) -> str:
    """
    Voeg zachte PDF-regeleindes samen binnen een blok-tekst.

    PDF-layout produceert soms woordenlijsten waarbij elk woord op een
    aparte regel staat (bijv. 'opdrachten\\ndie\\nhij\\nuitvoert.'). Dit
    zijn intra-blok soft-wraps die niet als alinea-scheidingen bedoeld zijn.

    Strategie: een regel wordt samengevoed met de vorige als:
      - de vorige regel NIET eindigt op een zinterminator (. ; : ! ?)
        of een lijstmarker (-);
      - de huidige regel NIET begint met een structurele opener
        (heading-prefix, opsommingsnummer, bullet, §…);
      - de huidige of vorige regel is korter dan de _WRAP_THRESHOLD
        (= de normale kolombreedte in chars; korte regels zijn bijna
        altijd soft-wraps, geen nieuwe zinnen).

    Opmerking: werkt op de tekst vóór paragraaf-samenvoegen. Paragaaf-
    grenzen (dubbele \\n) worden als hard reset behandeld en altijd bewaard.
    """
    _WRAP_THRESHOLD = 60  # beexcellent-kolommen zijn ~360pt breed ≈ 60-70 chars
    _SENTENCE_END = re.compile(r"[.;:!?]\s*$")

    parts = text.split("\n")
    out: list[str] = []
    for raw in parts:
        stripped = raw.strip()
        if not stripped or not out:
            out.append(stripped)
            continue
        if _RE_SOFT_WRAP_KEEP_SEPARATE.match(stripped):
            out.append(stripped)
            continue
        prev = out[-1]
        if not prev:
            out.append(stripped)
            continue
        prev_is_short = len(prev) < _WRAP_THRESHOLD
        cur_is_short = len(stripped) < _WRAP_THRESHOLD
        prev_ends_sentence = bool(_SENTENCE_END.search(prev))
        starts_lower = stripped[0].islower() if stripped else False
        # Voeg samen als:
        # - vorige regel eindigt niet op zinterminator, OF huidige begint lower-case
        # - minstens één van de twee is korter dan de drempel (= soft-wrap signaal)
        if (prev_is_short or cur_is_short) and (starts_lower or not prev_ends_sentence):
            out[-1] = prev + " " + stripped
        else:
            out.append(stripped)
    return "\n".join(out)


def is_page_noise(text: str) -> bool:
    """True als de tekst een paginanummer, copyright-regel of voettekst is."""
    stripped = text.strip()
    if not stripped:
        return True
    if _RE_PAGE_NUM.match(stripped) and len(stripped) <= 5:
        return True
    if _RE_PAGE_NofN.match(stripped):
        return True
    if _RE_PAGE_NofN2.match(stripped):
        return True
    if _RE_HERFORMULERING.match(stripped):
        return True
    if _RE_COPYRIGHT_IFAC.search(stripped):
        return True
    if _RE_COPYRIGHT_ITAA.search(stripped):
        return True
    # Blok met alleen witruimte
    if not stripped.replace("\n", "").strip():
        return True
    return False


# ─── Sectietitel-detectie ─────────────────────────────────────────────────────

def _looks_like_section_title(text: str) -> bool:
    """
    Bepaal of een getrimde tekst een sectietitel is die een ## heading verdient.

    Criteria (conservatief om false positives in bijlagen te vermijden):
    - 1 of 2 regels lang
    - totaal 4-80 chars
    - eerste teken is hoofdletter
    - eindigt NIET met een punt, komma of dubbele punt
    - NIET alleen een getal of afkorting+punt ("1.", "A1.", "Tel. :", "RPR:")
    - NIET een VEREISTEN/TOEPASSINGSMODALITEITEN-header
    - NIET een losse naam/label met dubbele punt (bv. "Naam en voornaam:")
    - NIET een aanhef of groet (Geachte, Met de meeste hoogachting)
    - Bevat minstens één alfanumeriek woord van >= 4 letters (geen losse afkortingen)
    """
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    if not lines or len(lines) > 2:
        return False
    total = " ".join(lines)
    total_stripped = total.strip()

    # Lengte-filter: te kort of te lang
    if len(total_stripped) < 4 or len(total_stripped) >= 80:
        return False

    # Eindigt niet op punt, komma of dubbele punt
    if total_stripped.endswith((".", ",", ":")):
        return False

    # Louter getal of getal+punt ("1.", "A1.", "12")
    if re.match(r"^[A-Za-z0-9]+\.$", total_stripped):
        return False

    # Paragraafnummers die beginnen met een cijfer gevolgd door punt
    if re.match(r"^\d+\.", total_stripped):
        return False

    # TOEPASSINGSMODALITEITEN-nummers: "A" + getal + punt (bijv. "A1.", "A12.")
    # gevolgd door meer tekst zijn paragrafen, geen sectietitels
    if re.match(r"^A\d+[\.\s]", total_stripped):
        return False

    # Moet beginnen met hoofdletter
    first_char = total_stripped[0]
    if not first_char.isupper():
        return False

    # Geen ALL CAPS woorden zonder spaties (bv. "INDIEN", "TENZIJ", "VEREISTEN")
    if total_stripped.upper() == total_stripped and " " not in total_stripped.strip():
        return False

    # Geen VEREISTEN/TOEPASSINGSMODALITEITEN labels
    if re.match(r"^(VEREISTEN|TOEPASSINGSMODALITEITEN)\s*$", total_stripped):
        return False

    # Geen aanhef-/groet-formules (briefhoofden in model-bijlagen)
    if re.match(r"^(Geachte|Met de meeste|Met vriendelijke|Hoogachtend)", total_stripped):
        return False

    # Geen "Opgemaakt te" of datum-formules (formulierlabels, geen titels)
    # "Datum:" of "Datum ___" = formulier-label; "Datum van inwerkingtreding" = echte titel
    if re.match(r"^Opgemaakt te", total_stripped):
        return False
    if re.match(r"^Datum\s*[_:.\s]*$|^Datum van de |^Datum van ondertekening", total_stripped):
        return False
    if re.match(r"^Handtekening", total_stripped):
        return False

    # Geen "Ofwel," / "En" / "Tussen" (contractformules)
    if re.match(r"^(Ofwel,|En\s*$|Tussen ondergetekenden)", total_stripped):
        return False

    # Minstens 2 woorden OF één lang woord (>= 8 letters):
    # filtert losse korte labels ("Geen", "In natura") uit bijlagen
    words = total_stripped.split()
    if len(words) == 1 and len(words[0].rstrip(".,:;")) < 8:
        return False

    # Minstens één substantieel woord (>= 5 letters) zodat afkortingen als
    # "Tel. :", "ITAA-nr." enz. worden uitgesloten
    substantial_words = [w for w in re.split(r"[\s\-.:]+", total_stripped) if len(w) >= 5]
    if not substantial_words:
        return False

    return True


# ─── Type 1: bilinguaal (NL/FR) ───────────────────────────────────────────────

_RE_FRENCH_MARKER = re.compile(
    r"\b(le |la |les |du |des |de |un |une |et |ou |avec |pour |dans |sur |"
    r"est |sont |être |avoir |cette |qui |que |par |aux |il |ils |elle |elles |"
    r"ce |cet |cette |ces |mon |son |leur |leurs |dont |afin |ainsi |aussi )",
    re.IGNORECASE,
)

# FR-accenten: accenten die typisch FR maar niet NL zijn.
# NL gebruikt ë, ï, ü als trema (bv. "financiële", "reïntegratie") — die NIET opnemen.
# Typisch FR maar niet NL: é, è, ê, à, â, î, ô, ù, û, œ, æ, ç.
_RE_FRENCH_ACCENTS = re.compile(r"[àâéèêîôùûœæçÉÈÊÀÙÔÎÂÛŒ]")

# FR-starters: regels die typisch met een FR lidwoord of voornaamwoord beginnen
_RE_FRENCH_START = re.compile(r"^(Le |La |Les |Du |Des |Un |Une |Et |Ou |Il |Ce |Au |Aux )")


_RE_NL_ACCENTED_WORDS = re.compile(
    r"\b(één|vóór|nóg|nóoit|wél|dé|hé|ó|ú)\b", re.IGNORECASE
)
_RE_NL_ONLY_WORDS = re.compile(
    r"\b(wordt|worden|dient|dienen|kantoor|beroepsbeoefenaar|wetboek|"
    r"uitvoering|opdracht|overeenkomstig|tenzij|hieromtrent|derhalve|"
    r"aldus|krachtens|immers|bedoeld|mits|behoudens|teneinde|"
    r"juncto|weliswaar|respectievelijk|bovendien|nochtans)\b",
    re.IGNORECASE,
)


def _is_likely_french_line(line: str) -> bool:
    """
    Bepaal of een regel waarschijnlijk Frans is.

    Drie signalen die worden gecheckt:
    1. FR-accenten (é, è, ê, à, â, ô, etc.) die NIET in bekende NL-woorden
       voorkomen (zoals 'één', 'vóór'). NL-trema's (ë, ï, ü) worden niet
       als FR-signaal gezien.
    2. Begint met een FR-lidwoord of voornaamwoord (Le, La, Les, Du, Il, …).
    3. Twee of meer FR-stopwoorden én geen typisch NL-woord.
    """
    # Signaal 1: FR-accenten — filter eerst bekende NL-geaccentueerde woorden
    if _RE_FRENCH_ACCENTS.search(line):
        line_without_nl_accented = _RE_NL_ACCENTED_WORDS.sub("", line)
        if _RE_FRENCH_ACCENTS.search(line_without_nl_accented):
            return True

    # Signaal 2: begint met FR-lidwoord/voornaamwoord
    if _RE_FRENCH_START.match(line):
        return True

    # Signaal 3: twee of meer FR-stopwoorden + geen duidelijk NL-woord
    fr_matches = _RE_FRENCH_MARKER.findall(line)
    if len(fr_matches) >= 2 and not (line[0].isdigit() if line else False):
        if not _RE_NL_ONLY_WORDS.search(line):
            return True

    return False


def _extract_nl_from_bilingual_block(text: str) -> str:
    """
    Haal de NL-tekst op uit een blok dat zowel NL als FR bevat
    (bijv. de koptekst-blokken die beide kolommen overspannen).

    Strategie: verwerk regel voor regel. Stop zodra een duidelijk FR-patroon
    gevonden wordt. Regels die na FR-regels komen maar zelf NL zijn (bv. een
    NL-sectietitel na een FR-slot-zin) worden NIET meer opgenomen — de functie
    levert enkel het NL-voorste deel.

    Retourneert lege string als het blok puur FR lijkt.
    """
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    if not lines:
        return ""

    nl_lines: list[str] = []
    for line in lines:
        if _is_likely_french_line(line):
            break  # eerste FR-regel = einde NL-deel
        nl_lines.append(line)

    return " ".join(nl_lines).strip()


def _extract_nl_sections_from_mixed_block(text: str) -> list[str]:
    """
    Extraheer NL-secties uit een breed blok met afgewisselde NL- en FR-tekst.

    Sommige brede blokken in de kwaliteitsmanagement-norm bevatten een FR-slot
    (bv. 'objectifs en matière de qualité...') gevolgd door een NL-sectietitel
    en NL-tekst. Deze functie levert alle aaneengesloten NL-stukken als
    afzonderlijke strings.

    Retourneert een lijst van NL-segmenten (elk segment = één logisch blok).
    Lege segmenten worden weggefilterd.
    """
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    if not lines:
        return []

    segments: list[str] = []
    current_nl: list[str] = []

    for line in lines:
        if _is_likely_french_line(line):
            # FR-regel: flush eventuele NL-buffer
            if current_nl:
                # Bewaar interne structuur met newlines (niet samenvoegen met spatie)
                segments.append("\n".join(current_nl))
                current_nl = []
        else:
            current_nl.append(line)

    if current_nl:
        segments.append("\n".join(current_nl))

    return [s for s in segments if s]


def _strip_fr_lines_from_nl_block(text: str) -> str:
    """
    Verwijder duidelijk FR-regels uit een blok dat als NL-blok is geclassificeerd
    maar toch FR-tekst bevat (bv. een vertaling op de volgende regel).

    Strategie: verwerk regel voor regel. FR-regels worden overgeslagen; NL-regels
    worden behouden. Behoudt de tekststructuur (paragraaf-scheidingen, lijstitems).

    Werkt CONSERVATIEF: alleen regels waarvan we zeker zijn dat ze FR zijn worden
    verwijderd. Twijfelgevallen blijven staan.
    """
    lines = [l.strip() for l in text.split("\n")]
    kept: list[str] = []
    for line in lines:
        if line and _is_likely_french_line(line):
            continue  # FR-regel: overslaan
        kept.append(line)
    # Verwijder overbodige blanco-regels na verwijdering
    result = "\n".join(kept)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip()


def extract_bilingual(pdf_path: Path, column_split: float) -> str:
    """
    Extraheer alleen de NL-kolom (x0 < column_split) uit een landschaps-PDF.

    Verwerking per pagina:
    1. Verzamel alle NL-blokken (x0 < column_split, breedte < 75% paginabreedte).
    2. Verwerk wide blokken (>= 75% paginabreedte) apart voor sectietitelextractie.
    3. Sorteer alles samen op y0 en verwerk in leesvolgorde.

    Heading-fragmenten: sommige sectietitels zijn verdeeld over blokken op
    bijna-dezelfde y-positie (< 20pt afstand). Die worden samengevoegd.
    """
    doc = pymupdf.open(str(pdf_path))
    paragraphs: list[str] = []

    for page in doc:
        page_width = page.rect.width
        page_blocks = page.get_text("blocks")
        wide_threshold = page_width * 0.75

        # Stap 1: splits blokken in NL-kolom en wide-blokken
        # wide blokken worden omgezet naar (y0, "wide", text)-tuples
        # NL-blokken worden omgezet naar (y0, "nl", text)-tuples
        candidates: list[tuple[float, float, str, str]] = []  # (y0, x0, kind, text)

        for b in page_blocks:
            x0, y0, x1, y1, text, _bno, btype = b
            if btype != 0:
                continue
            block_width = x1 - x0

            if block_width >= wide_threshold:
                candidates.append((y0, x0, "wide", text))
            elif x0 < column_split:
                candidates.append((y0, x0, "nl", text))
            # FR-blokken (x0 >= column_split, niet wide): negeer

        # Sorteer op y0 dan x0
        candidates.sort(key=lambda c: (c[0], c[1]))

        # Stap 2: verwerk in volgorde, samenvoegen van heading-fragmenten
        pending_heading_parts: list[str] = []
        pending_y0: float = -9999.0

        def _flush_pending() -> None:
            if not pending_heading_parts:
                return
            merged = " ".join(pending_heading_parts).strip()
            if merged:
                paragraphs.append(f"\n## {merged}")
            pending_heading_parts.clear()

        for y0, x0, kind, text in candidates:
            cleaned = clean_block_text(text)
            if not cleaned or is_page_noise(cleaned):
                continue

            if kind == "wide":
                # Wide blok: kan puur FR zijn, puur NL, of gemengd NL+FR.
                # Strategie: extraheer alle NL-segmenten (ook als FR voorkomt tussenin).
                nl_segments = _extract_nl_sections_from_mixed_block(cleaned)
                if not nl_segments:
                    # Puur FR-blok: negeer, maar flush eventuele pending heading
                    if abs(y0 - pending_y0) >= 30:
                        _flush_pending()
                    continue

                # Verwerk elk NL-segment afzonderlijk
                for segment in nl_segments:
                    if not segment or is_page_noise(segment):
                        continue
                    # Zachte wraps in het segment samenvoegen
                    segment = merge_intra_block_soft_wraps(segment)
                    if _looks_like_section_title(segment):
                        if pending_heading_parts and abs(y0 - pending_y0) < 30:
                            pending_heading_parts.append(segment)
                        else:
                            _flush_pending()
                            pending_heading_parts.append(segment)
                        pending_y0 = y0
                    else:
                        _flush_pending()
                        paragraphs.append(segment)
                        pending_y0 = y0
                continue

            # NL-blok verwerken: verwijder eerst FR-regels (gemengde blokken),
            # dan zachte wraps samenvoegen.
            cleaned = _strip_fr_lines_from_nl_block(cleaned)
            if not cleaned or is_page_noise(cleaned):
                continue
            cleaned = merge_intra_block_soft_wraps(cleaned)
            is_same_y_band = abs(y0 - pending_y0) < 30
            is_title_candidate = _looks_like_section_title(cleaned)

            if is_title_candidate:
                if pending_heading_parts and is_same_y_band:
                    pending_heading_parts.append(cleaned)
                else:
                    _flush_pending()
                    pending_heading_parts.append(cleaned)
                pending_y0 = y0
            else:
                _flush_pending()
                paragraphs.append(cleaned)
                pending_y0 = y0

        _flush_pending()

    doc.close()

    body = "\n\n".join(paragraphs)
    body = _RE_BLANK_EXCESS.sub("\n\n\n", body)
    return body.strip()


# ─── Type 2: vereisten (VEREISTEN / TOEPASSINGSMODALITEITEN) ──────────────────

class _Block:
    """Intern DTO voor een pymupdf-blok."""
    __slots__ = ("x0", "y0", "x1", "y1", "text", "width")

    def __init__(self, x0: float, y0: float, x1: float, y1: float, text: str) -> None:
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.text = text
        self.width = x1 - x0


def _classify_block(block: _Block, column_split: float, full_width_threshold: float) -> str:
    """Retourneer 'full', 'left' of 'right'."""
    if block.width > full_width_threshold:
        return "full"
    if block.x0 < column_split:
        return "left"
    return "right"


def _is_vereisten_header(text: str) -> bool:
    """True als het blok de "VEREISTEN / TOEPASSINGSMODALITEITEN" label-rij is."""
    stripped = text.strip()
    # Beide labels op twee regels, of een combinatie
    return bool(re.match(
        r"^(VEREISTEN\s*\n\s*TOEPASSINGSMODALITEITEN|TOEPASSINGSMODALITEITEN\s*\n\s*VEREISTEN)$",
        stripped,
    ))


def _ensure_a_prefix(text: str) -> str:
    """
    Voeg 'A.' prefix toe als de tekst nog niet begint met 'A' gevolgd door een getal of punt.
    Bedoeld voor toepassingsmodaliteiten-blokken die nog geen A-nummer hebben.
    """
    stripped = text.strip()
    if re.match(r"^A\d*[\.\s]", stripped):
        return text  # al een A-prefix
    return f"A. {stripped}"


def _is_toepassingsmodaliteiten_right_column(first_right_text: str) -> bool:
    """
    Bepaal of de rechterkolom toepassingsmodaliteiten bevat (→ A-prefix logica)
    of gewone tekst (→ chronologisch samenvoegen, geen prefix).

    Toepassingsmodaliteiten-kolom: begint met "A" + getal (bijv. "A1.", "A2.")
    of bevat een TOEPASSINGSMODALITEITEN-kolomheader.
    """
    stripped = first_right_text.strip()
    if re.match(r"^A\d+[\.\s]", stripped):
        return True
    if re.match(r"^TOEPASSINGSMODALITEITEN\s*$", stripped):
        return True
    return False


def extract_vereisten(
    pdf_path: Path,
    column_split: float,
    full_width_threshold: float,
) -> str:
    """
    Extraheer twee-kolom norm-PDFs van het type "vereisten".

    Subtypes worden automatisch herkend op basis van de rechterkolom-inhoud:

    1. VEREISTEN + TOEPASSINGSMODALITEITEN (effectennorm, isrs4410):
       De rechterkolom begint met "A" + getal (bijv. "A1.", "A2.").
       VEREISTEN N wordt gevolgd door de bijbehorende TOEPASSINGSMODALITEITEN.
       Ontbrekende A.-prefix wordt automatisch toegevoegd.

    2. Gewone twee-kolom zonder toepassingsmodaliteiten:
       Beide kolommen worden chronologisch samengevoegd (links voor rechts
       per y-band), zonder prefix.

    Sectietitel-detectie:
    - full-width blokken die een korte titel bevatten → ## heading.
    - left/right blokken zonder partner op dezelfde y-positie → ## heading
      (alleen op twee-kolom pagina's, met minimale blokbreedte).
    - VEREISTEN/TOEPASSINGSMODALITEITEN-labelrijen → gefilterd als ruis.
    """
    doc = pymupdf.open(str(pdf_path))

    # Detecteer subtype: scan de eerste right-blokken over de eerste pagina's
    # om te bepalen of dit een toepassingsmodaliteiten-kolom is.
    is_toepassingsmodaliteiten: bool | None = None
    for page in doc:
        for b in page.get_text("blocks"):
            if b[6] != 0:
                continue
            blk = _Block(b[0], b[1], b[2], b[3], b[4])
            if _classify_block(blk, column_split, full_width_threshold) == "right":
                cleaned = clean_block_text(blk.text)
                if cleaned and not is_page_noise(cleaned):
                    is_toepassingsmodaliteiten = _is_toepassingsmodaliteiten_right_column(cleaned)
                    break
        if is_toepassingsmodaliteiten is not None:
            break
    # Veilige default: als we het niet kunnen detecteren, behandel als gewone tekst
    if is_toepassingsmodaliteiten is None:
        is_toepassingsmodaliteiten = False

    output_parts: list[str] = []

    for page in doc:
        page_blocks_raw = page.get_text("blocks")
        # Zet om in _Block-objecten en filter niet-tekst
        blocks = [
            _Block(b[0], b[1], b[2], b[3], b[4])
            for b in page_blocks_raw
            if b[6] == 0  # btype 0 = tekst
        ]

        # Sorteer op y0, dan x0 (leesrichting: boven→onder, links→rechts)
        blocks.sort(key=lambda b: (b.y0, b.x0))

        # Classificeer elk blok
        classified: list[tuple[str, _Block]] = [
            (_classify_block(b, column_split, full_width_threshold), b)
            for b in blocks
        ]

        # Bepaal welke y-posities ZOWEL een linker- als rechterblok hebben
        # (= body-regels). Blokken op y-posities zonder partner zijn potentieel
        # sectietitels die gecentreerd boven de twee kolommen staan.
        y0_left = {round(b.y0) for col, b in classified if col == "left"}
        y0_right = {round(b.y0) for col, b in classified if col == "right"}
        paired_y0 = y0_left & y0_right

        # Activeer heading-detectie voor left/right blokken ALLEEN als de pagina
        # daadwerkelijk twee-kolom inhoud heeft (min. 1 gepaard y-punt).
        # Bijlage-pagina's hebben alleen linkerkolom en triggeren geen heading-detectie.
        page_is_two_column = bool(paired_y0)

        for col, block in classified:
            cleaned = clean_block_text(block.text)
            if not cleaned or is_page_noise(cleaned):
                continue

            # Filter gecombineerde header+paginanummer blokken
            # (bv. "Openbare raadpleging juli 2024 \n\n38/54")
            block_lines = [l.strip() for l in cleaned.split("\n") if l.strip()]
            if block_lines and _RE_PAGE_NofN.match(block_lines[-1]):
                continue

            if col == "full":
                # VEREISTEN/TOEPASSINGSMODALITEITEN-labelrij: overslaan
                if _is_vereisten_header(cleaned):
                    continue
                # Sectieheader die boven beide kolommen staat
                if _looks_like_section_title(cleaned):
                    output_parts.append(f"\n## {cleaned}")
                else:
                    # Overige full-width tekst (bijv. preamble-alinea's)
                    output_parts.append(cleaned)

            elif col == "left":
                # Sectietitel-detectie voor linkerkolom:
                # - Op twee-kolom pagina's: alleen blokken ZONDER corresponderende
                #   rechterkolom-blok (= gecentreerde sectietitel), met min. breedte
                #   van 100pt (tabelcellen uitsluiten).
                # - Op enkelvoudige pagina's (bijv. sectietitelblad): ook heading-detectie
                #   toepassen (min. breedte 80pt voor minder strenge context).
                block_y = round(block.y0)
                is_unpaired = block_y not in paired_y0
                if _looks_like_section_title(cleaned):
                    if page_is_two_column and is_unpaired and block.width >= 100:
                        output_parts.append(f"\n## {cleaned}")
                    elif not page_is_two_column and block.width >= 80:
                        output_parts.append(f"\n## {cleaned}")
                    else:
                        output_parts.append(cleaned)
                else:
                    output_parts.append(cleaned)

            else:  # right
                # Sectietitel-detectie voor rechterkolom:
                # Soms staat een sectietitel in de rechterkolom (bijv. "Definities")
                # op een pagina die verder geen twee-kolom inhoud heeft.
                block_y = round(block.y0)
                is_unpaired = block_y not in paired_y0
                if (
                    not page_is_two_column
                    and is_unpaired
                    and block.width >= 50
                    and _looks_like_section_title(cleaned)
                ):
                    output_parts.append(f"\n## {cleaned}")
                elif is_toepassingsmodaliteiten:
                    # TOEPASSINGSMODALITEITEN: voeg A.-prefix toe als ontbrekend
                    prefixed = _ensure_a_prefix(cleaned)
                    output_parts.append(prefixed)
                else:
                    # Gewone rechterkolom: geen prefix
                    output_parts.append(cleaned)

    doc.close()

    body = "\n\n".join(output_parts)
    body = _RE_BLANK_EXCESS.sub("\n\n\n", body)
    return body.strip()


# ─── Hoofd-extractie-dispatcher ───────────────────────────────────────────────

def extract_body(md_filename: str, config: dict) -> str:
    """Dispatcht naar de juiste extractie-functie op basis van type."""
    pdf_path: Path = config["pdf"]
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF niet gevonden: {pdf_path}")

    pdf_type = config["type"]
    if pdf_type == "bilingual":
        return extract_bilingual(pdf_path, column_split=config["column_split"])
    elif pdf_type == "vereisten":
        return extract_vereisten(
            pdf_path,
            column_split=config["column_split"],
            full_width_threshold=config.get("full_width_threshold", 400),
        )
    else:
        raise ValueError(f"Onbekend PDF-type: {pdf_type!r}")


# ─── Bestand-verwerking ───────────────────────────────────────────────────────

def process_one(md_filename: str, config: dict, *, dry_run: bool = False) -> dict:
    """
    Verwerk één norm-MD:
    1. Lees bestaande frontmatter.
    2. Extraheer nieuwe body uit PDF.
    3. Schrijf frontmatter + nieuwe body (tenzij dry-run).

    Retourneert statistieken-dict.
    """
    md_path = NORMEN_DIR / md_filename
    pdf_path: Path = config["pdf"]

    # Lees bestaande frontmatter
    existing_frontmatter = ""
    if md_path.exists():
        existing_text = md_path.read_text(encoding="utf-8")
        existing_frontmatter, _ = split_frontmatter(existing_text)
    else:
        print(f"  ⚠ {md_filename}: MD-bestand niet gevonden — body wordt toch geextraheerd")

    # Extraheer nieuwe body
    new_body = extract_body(md_filename, config)

    h2_count = len(re.findall(r"(?m)^##\s+", new_body))
    char_count = len(new_body)

    result = {
        "file": md_filename,
        "pdf": str(pdf_path.name),
        "type": config["type"],
        "body_chars": char_count,
        "h2_headings": h2_count,
        "written": False,
    }

    if dry_run:
        print(f"  [dry-run] {md_filename}: {char_count} chars, {h2_count} ## headings")
        print(f"    PDF: {pdf_path.name} ({config['type']})")
        # Toon eerste 400 chars van de nieuwe body als preview
        preview = new_body[:400].replace("\n", "↵")
        print(f"    Preview: {preview}")
        return result

    # Herbouw MD-bestand
    if not existing_frontmatter:
        # Geen bestaande frontmatter: schrijf puur de body (suboptimaal, maar veilig)
        output = new_body + "\n"
    else:
        output = existing_frontmatter + "\n" + new_body + "\n"

    md_path.write_text(output, encoding="utf-8")
    result["written"] = True
    print(f"  ✓ {md_filename}: {char_count} chars, {h2_count} ## headings geschreven")
    return result


# ─── Hoofdprogramma ───────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--file",
        metavar="FILENAME",
        help="Verwerk alleen dit MD-bestand (naam zonder pad, bijv. ITAA-norm-intern-kwaliteitsmanagement.md)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Toon informatie maar schrijf geen bestanden",
    )
    args = parser.parse_args()

    if args.file:
        if args.file not in KNOWN_PDFS:
            names = "\n  ".join(sorted(KNOWN_PDFS))
            print(f"Fout: {args.file!r} niet bekend. Kies uit:\n  {names}", file=sys.stderr)
            sys.exit(1)
        targets = {args.file: KNOWN_PDFS[args.file]}
    else:
        targets = KNOWN_PDFS

    mode = "(dry-run) " if args.dry_run else ""
    print(f"=== extract_norm_twocolumn {mode}— {len(targets)} bestand(en) ===")

    results = []
    for md_filename, config in targets.items():
        try:
            stat = process_one(md_filename, config, dry_run=args.dry_run)
            results.append(stat)
        except FileNotFoundError as exc:
            print(f"  ✗ {md_filename}: {exc}", file=sys.stderr)
        except Exception as exc:
            print(f"  ✗ {md_filename}: onverwachte fout: {exc}", file=sys.stderr)
            raise

    written = sum(1 for r in results if r.get("written"))
    total_chars = sum(r.get("body_chars", 0) for r in results)
    total_headings = sum(r.get("h2_headings", 0) for r in results)

    print(f"\nKlaar: {written}/{len(results)} bestanden geschreven")
    print(f"Totaal: {total_chars} chars, {total_headings} ## headings")

    if args.dry_run:
        print("\nDry-run: geen bestanden gewijzigd. Verwijder --dry-run om te schrijven.")
    else:
        print("\nVolgende stap: python tools/etl/qa_bron.py --bron-rol norm")


if __name__ == "__main__":
    import os
    os.chdir(ROOT)
    main()
