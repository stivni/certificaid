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
    r"est |sont |être |avoir |cette |qui |que |par |aux )",
    re.IGNORECASE,
)


def _extract_nl_from_bilingual_block(text: str) -> str:
    """
    Haal de NL-tekst op uit een blok dat zowel NL als FR bevat
    (bijv. de koptekst-blokken die beide kolommen overspannen).

    Strategie: neem alleen de eerste regel die geen duidelijk FR-patroon bevat,
    of als het een NL+FR-sectietitel is, neem de eerste NL-zin.
    Retourneert lege string als het blok puur FR lijkt.
    """
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    if not lines:
        return ""

    nl_lines: list[str] = []
    for line in lines:
        # Stop zodra we een duidelijk Franstalige regel treffen
        if _RE_FRENCH_MARKER.search(line) and not line[0].isdigit():
            # Controleer of het echt FR is: bevat accenten typisch voor FR maar niet NL
            if re.search(r"[àâêôûœæçÉÈÀÙÔÎÏÊÂÛŒ]", line):
                break
            # Of bevat FR-stopwoorden aan het begin
            if re.match(r"^(Le |La |Les |Du |Des |Un |Une |Et |Ou )", line):
                break
        nl_lines.append(line)

    return " ".join(nl_lines).strip()


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
                # Wide blok: kijk of er een NL-sectietitel in zit
                nl_part = _extract_nl_from_bilingual_block(cleaned)
                if nl_part and not is_page_noise(nl_part) and _looks_like_section_title(nl_part):
                    # Laat pending heading accumuleren — niet flushen:
                    # de wide blok kan tussen twee NL heading-fragmenten zitten
                    # (bv. KANTOORNIVEAU staat naast de wide blok op zelfde y)
                    # We voegen de wide-heading toe aan een aparte pending-candidate;
                    # als er al pending fragmenten zijn op nabije y, samenvoegen.
                    if pending_heading_parts and abs(y0 - pending_y0) < 30:
                        pending_heading_parts.append(nl_part)
                    else:
                        _flush_pending()
                        pending_heading_parts.append(nl_part)
                    pending_y0 = y0
                else:
                    # Overige wide blokken (FR-overflow, paginanummers): negeer
                    # maar flush wel eventuele pending heading die niet op deze y zit
                    if abs(y0 - pending_y0) >= 30:
                        _flush_pending()
                continue

            # NL-blok verwerken
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
