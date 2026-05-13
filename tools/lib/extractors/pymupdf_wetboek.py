"""pymupdf-block-extractor voor wetteksten (PDF → markdown).

Alternatief voor pdftotext-layout dat structuur-bewust werkt:
  - **Blokken** met bounding-box (positie + font + size) i.p.v. ASCII-grid
  - **Kolom-detectie**: auto-clustering van block-x0 om single/dual-column
    layouts uit elkaar te halen (lost A7/A8 kolom-bleed op)
  - **Font-aware heading-detectie**: blokken met grootste font-size +
    bold worden ## headings (lost B4/B5 plain-text-structuurlabels op)
  - **Pagina-margin filter**: blokken met y in top/bottom-band gestript
    (lost A1 page-header/footers op)
  - **Paragraph-join**: opeenvolgende blokken in zelfde kolom met
    consistente indent worden samengevoegd op één regel (lost A6
    spurious line-breaks op)
  - **Tabel-detectie** (rudimentair): blokken in grid-patroon op zelfde
    y-range → markdown pipe-tabel (mitigeert C3 pseudo-tabel-bug)
  - **EU-richtlijn mode** (`mode: eu_richtlijn`): activeert extra EU
    Publicatieblad-koptekst stripping, EUR-Lex amendment-marker stripping
    en beperkt extractie tot de NL-kolom (linker kolom bij 2-kolom layout)

Niet bedoeld voor:
  - PDFs met afbeeldingen/schema's als content (D2 — vereist OCR)
  - Multi-page tables die complex breken over pagina's

Gebruik via convert.py met `extract.method: pymupdf_wetboek`:

    extract:
      method: pymupdf_wetboek
      params:
        # Optioneel — auto-detectie van column-layout per pagina
        force_columns: 2   # 1 | 2 | "auto" (default)
        column_filter: nl  # nl | fr | both (default: both)
        # y-margins voor page-header/footer filter (default: 5% van page-height)
        top_margin: 50
        bottom_margin: 50
        # EU-richtlijn mode: strip PB-kopteksten + EUR-Lex markers + NL-kolom
        mode: eu_richtlijn  # eu_richtlijn | None (default)
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import pymupdf  # type: ignore


# ─── Datatypes ────────────────────────────────────────────────────────────────

@dataclass
class Block:
    """Eén tekstblok met bounding-box en font-info."""
    x0: float
    y0: float
    x1: float
    y1: float
    text: str
    avg_font_size: float
    is_bold: bool
    column: int = 0  # 0=left/single, 1=right (in 2-column layouts)

    @property
    def width(self) -> float:
        return self.x1 - self.x0

    @property
    def height(self) -> float:
        return self.y1 - self.y0


# ─── Block-extractie per pagina ───────────────────────────────────────────────

def _extract_page_blocks(page) -> list[Block]:
    """Lees alle tekstblokken uit een PDF-pagina met font-info."""
    blocks: list[Block] = []
    for b in page.get_text("dict")["blocks"]:
        if b.get("type") != 0:  # 0 = text, 1 = image
            continue
        lines = b.get("lines", [])
        if not lines:
            continue
        text_parts = []
        sizes = []
        bold_count = 0
        total_spans = 0
        for line in lines:
            line_parts = []
            for sp in line.get("spans", []):
                line_parts.append(sp.get("text", ""))
                sz = sp.get("size")
                if sz:
                    sizes.append(sz)
                # pymupdf flags: bit 16 = bold
                if sp.get("flags", 0) & 16:
                    bold_count += 1
                total_spans += 1
            text_parts.append(" ".join(line_parts))
        text = "\n".join(text_parts).strip()
        if not text:
            continue
        bbox = b["bbox"]
        avg_size = sum(sizes) / len(sizes) if sizes else 10.0
        is_bold = (bold_count / max(total_spans, 1)) > 0.6
        blocks.append(Block(
            x0=bbox[0], y0=bbox[1], x1=bbox[2], y1=bbox[3],
            text=text,
            avg_font_size=avg_size,
            is_bold=is_bold,
        ))
    return blocks


# ─── Pagina-margin filter ─────────────────────────────────────────────────────

def _filter_margins(blocks: list[Block], page_height: float,
                    top_margin: float = 50, bottom_margin: float = 50) -> list[Block]:
    """Strip blokken in de page-header en footer-zones."""
    return [b for b in blocks
            if b.y0 > top_margin and b.y1 < (page_height - bottom_margin)]


# ─── Kolom-detectie ───────────────────────────────────────────────────────────

def _detect_columns(blocks: list[Block], page_width: float) -> tuple[int, float]:
    """Detecteer single/dual-column layout op een pagina.

    Returns (n_columns, split_x).
      n_columns: 1 of 2
      split_x: x-positie waar tweede kolom begint

    Heuristiek: bouw histogram van block-x0's per 25-punt bin. Bepaal de
    TWEE MEEST FREQUENTE anker-bins (≥3 blokken elk) — deze representeren
    typisch de linker- en rechter-kolom-margin. Als de afstand ≥200 punten
    is, is het een 2-kolom layout. Centered-headings (smaller bins
    tussen left en right) verstoren dit NIET, omdat we alleen de top-2
    nemen, niet alle bins op x-positie.

    Belangrijk voor EU-OJ: even-pages (verso) en odd-pages (recto) hebben
    afwijkende margins. Detectie loopt per pagina, dus dit werkt
    automatisch zolang de top-2 anker-bins de kolom-margins zijn.
    """
    if not blocks:
        return 1, page_width

    bins = Counter(int(b.x0) // 25 * 25 for b in blocks)
    # Sorteer op frequentie (count desc), neem alleen bins met ≥3 blokken.
    candidates = sorted(
        [(x, c) for x, c in bins.items() if c >= 3],
        key=lambda p: -p[1],
    )
    if len(candidates) < 2:
        return 1, page_width

    # Gebruik de TWEE MEEST FREQUENTE bins als kandidaten voor de
    # kolom-margins. Centered headings (smaller bins ertussen) negeren we.
    (x_a, _), (x_b, _) = candidates[0], candidates[1]
    x_left = min(x_a, x_b)
    x_right = max(x_a, x_b)
    gap = x_right - x_left

    if gap < 200:
        return 1, page_width

    split_x = (x_left + x_right) / 2
    return 2, split_x


def _assign_columns(blocks: list[Block], n_columns: int, split_x: float) -> None:
    """Zet `column`-index op elk block (in-place)."""
    if n_columns == 1:
        return
    for b in blocks:
        b.column = 1 if b.x0 >= split_x else 0


# ─── Heading-detectie via font-size ───────────────────────────────────────────

def _detect_heading_levels(blocks: list[Block]) -> dict[float, int]:
    """Cluster font-sizes en map naar markdown-heading-levels (#-##-###).

    Strategy:
      - Body-text is typisch de meest voorkomende size → niet een heading.
      - Alle UNIEKE sizes groter dan body → headings, op aflopende grootte
        gemapped naar H1, H2, H3... (max 4 niveaus).
    """
    sizes = [round(b.avg_font_size, 1) for b in blocks if len(b.text) > 30]
    if not sizes:
        return {}
    counts = Counter(sizes)
    body_size, _ = counts.most_common(1)[0]
    # Sorteer unieke sizes aflopend; pak alleen sizes > body
    bigger = sorted({s for s in sizes if s > body_size + 0.5}, reverse=True)
    levels: dict[float, int] = {}
    for i, sz in enumerate(bigger[:4], start=1):
        levels[sz] = i
    return levels


# ─── Block-classificatie en rendering ─────────────────────────────────────────

_ART_HEAD_RE = re.compile(
    # Belgisch art-num: `Art. 5`, `Art. 5bis`, `Art. 5/2`, ofwel
    # `Art.XV.125`, `Art. XV.125/4/1` (WER-stijl met roman-prefix), ofwel
    # `Art. 1:5`, `Art. 18:8` (WVV-stijl met BOEK:ARTIKEL-notatie).
    r"^\s*(Art(?:ikel)?\.?)\s*"
    r"(?:[IVXLCDM]+\.?\s*)?"          # optioneel romeins boek/titel-prefix
    r"\d+(?:[\./:]\d+)*"               # nummer met /N of :N segmenten
    r"(?:bis|ter|quater|quinquies|sexies|septies)?"
    r"\s*\.?\s*$",
    re.I,
)
# Inline-art-pattern: `Art. N . Heading-tekst` aan het begin van een regel,
# eventueel gevolgd door body op zelfde-of-volgende-regel.
_ART_INLINE_RE = re.compile(
    r"^\s*(Art(?:ikel)?\.?)\s*"
    r"((?:[IVXLCDM]+\.?\s*)?"
    r"\d+(?:[\./:]\d+)*"               # ook : voor WVV-notatie (1:5, 18:8)
    r"(?:bis|ter|quater|quinquies|sexies|septies)?)"
    r"\s*[\.\s]\s*(.+?)$",
    re.I,
)
_STRUCT_HEAD_RE = re.compile(
    r"^\s*(TITEL|BOEK|DEEL|HOOFDSTUK|AFDELING|ONDERAFDELING|"
    r"TITRE|LIVRE|PARTIE|CHAPITRE|SECTION|SOUS-SECTION)\b",
    re.I,
)


def _classify_block(block: Block, heading_levels: dict[float, int]) -> tuple[str, int]:
    """Bepaal block-type en heading-niveau.

    Returns (kind, level):
      kind: "heading" | "art_heading" | "struct_heading" | "paragraph"
      level: 1-6 (alleen relevant bij heading-types)
    """
    text = block.text.strip()
    size = round(block.avg_font_size, 1)

    # Art. N — duidelijke heading, level 6 (chunk-level voor ADR-006)
    if _ART_HEAD_RE.match(text):
        return "art_heading", 6

    # TITEL / HOOFDSTUK / etc.
    if _STRUCT_HEAD_RE.match(text):
        # Level afhankelijk van type:
        m = _STRUCT_HEAD_RE.match(text)
        kw = m.group(1).upper()
        if kw in ("DEEL", "PARTIE"):
            return "struct_heading", 2
        if kw in ("BOEK", "LIVRE"):
            return "struct_heading", 2
        if kw in ("TITEL", "TITRE"):
            return "struct_heading", 3
        if kw in ("HOOFDSTUK", "CHAPITRE"):
            return "struct_heading", 4
        if kw in ("AFDELING", "SECTION"):
            return "struct_heading", 5
        if kw in ("ONDERAFDELING", "SOUS-SECTION"):
            return "struct_heading", 6
        return "struct_heading", 4

    # Generieke heading via font-size — conservatief:
    # - tekst moet kort zijn (<120 chars)
    # - tekst mag niet eindigen op zin-vervolg leestekens
    # - moet bold zijn OF substantieel groter dan body
    if size in heading_levels and len(text) < 120:
        if not re.search(r"[;,]$", text) and not text.endswith("."):
            if block.is_bold:
                return "heading", heading_levels[size] + 1
            # Niet-bold maar wel groter font → minder zeker, vereist topniveau
            if heading_levels[size] == 1:
                return "heading", 2

    return "paragraph", 0


# ─── FR-regel stripping uit tweetalige blokken ───────────────────────────────

# Structuurlabels die UITSLUITEND in het Frans voorkomen in tweetalige wetteksten.
# NL equivalenten (TITEL, HOOFDSTUK, AFDELING, …) worden nooit als FR herkend.
# Let op: TABEL (NL) ≠ TABLEAU (FR); DROIT is FR, RECHT is NL.
# Splitsing in twee regexes: (A) woordgrens-patronen, (B) overige patroonmatches.
_FR_STRUCT_LINE_RE = re.compile(
    r"^\s*(?:TITRE|LIVRE|PARTIE|CHAPITRE|SECTION|SOUS-SECTION"
    r"|Titre|Livre|Partie|Chapitre|Section|Sous-section"
    r"|TABLEAU|Tableau"                      # FR tegenhanger van NL TABEL
    r"|VEHICULES?|Véhicules?|COMBINAISONS?"  # FR tabelhoofding in VCF-bijlage
    r"|DROIT\s+(?:FUTUR|D[''']ENREGISTREMENT)"  # Reg.rechten FR labels
    # FR-alleen zinnen als volledige regel (geen NL equivalent)
    r"|Dispositions\s+r[eé]gionales"        # "Dispositions régionales" — FR voetnoot
    r"|Alin[eé]a\s+\d"                      # "Alinéa 4 : dispositions..."
    r")\b"
    # Aanvullende patronen zonder woordgrens-eis (eindigen niet op een woordkarakter)
    r"|^\s*Note\s+\(\d+"                    # "Note (1)" — FR noot-intro
    ,
)

# "Article N er" / "Article N ère" — Frans ordegetal achter art-nummer.
# Ook: "§ N er ." — FR ordegetal voor paragraaf-aanduiding.
_FR_ARTICLE_ER_RE = re.compile(
    r"^\s*(?:"
    r"Article\s+\d+\s*(?:er|ère|re|ième|ieme|bis|ter)?\s*[.\-]?"
    r"|§\s*\d+\s*(?:er|ère|re|ième|ieme)\s*\.\s*(?:Dispositions|La\s|Le\s|Les\s)"
    r")\s*",
    re.I,
)

# Veelvoorkomende onmiskenbaar Franstalige zinsdelen in body-tekst.
# Gekozen op basis van VCF- en Registratierechten-patronen uit L2-rapport.
_FR_BODY_MARKERS_RE = re.compile(
    r"(?:"
    r"[Ll]e\s+présent\s+(?:code|décret|règlement|Code)"
    r"|[Ii]l\s+y\s+a\s+lieu\s+d[''']entendre"
    r"|d[''']entendre\s+par\s+:"
    r"|[Ll]a\s+présente\s+(?:section|disposition|loi|ordonnance)"
    r"|[Ll][''']article\s+\d+"
    r"|[Pp]ar\s+dérogation"
    r"|(?:visé|prévu|défini)(?:e|es|s)?\s+(?:à|au|aux)\s+(?:l[''']article|l[''']alinéa|les articles)"
    r")",
)


def _is_fr_only_line(line: str) -> bool:
    """Bepaal of een enkele regel onmiskenbaar Franstalig is.

    Gebruikt dezelfde patroonset als ``_strip_fr_lines_from_block`` maar
    als helper voor enkelvoudige regels (geen ``\\n``).
    """
    stripped = line.strip()
    if not stripped:
        return False
    return bool(
        _FR_STRUCT_LINE_RE.match(stripped)
        or _FR_ARTICLE_ER_RE.match(stripped)
        or _FR_BODY_MARKERS_RE.search(stripped)
    )


# Inline bilingual ` / ` separator: "TABEL I / TABLEAU I" of
# "verkrijging in rechte lijn / acquisition en ligne directe".
# Drie triggers voor FR-gedeelte na ` / `:
#   1. All-caps FR-woord (TABLEAU, ...)
#   2. Geaccentueerde letter in de eerste 40 chars na de slash (é, è, ê, â, û, ç, …)
#   3. Bekende FR-startwoorden in deze context (acquisition, tarif, tranche, etc.)
_FR_INLINE_SLASH_RE = re.compile(
    r"\s+/\s+"                                   # spatie-slash-spatie separator
    r"(?:"
    r"[A-Z][A-ZÀ-Ý]{2,}"                        # all-caps FR (TABLEAU, etc.)
    r"|(?=[^/\n]{0,40}[àáâãäåæçèéêëìíîïðñòóôõöùúûüýÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖÙÚÛÜÝ])"
                                                  # accent char binnen 40 tekens
    r"|(?:acquisition|tarif|tranche|montant|imposition|perception"
    r"|entre|pour\s|dans\s|selon\s|aux\s|par\s|du\s|de\s+la\s|le\s|les\s|la\s)"
                                                  # bekende FR-woorden
    r")"
    r".*$",                                        # rest van de regel
)


def _strip_fr_inline_suffix(text: str) -> str:
    """Strip een Franstalig gedeelte na een ` / `-separator in dezelfde regel.

    Bedoeld voor inline tweetalige labels zoals:
      "TABEL I   /   TABLEAU I" → "TABEL I"
      "verkrijging in rechte lijn en tussen partners / acquisition en ligne"
        → "verkrijging in rechte lijn en tussen partners"

    Voorzichtig patroon: alleen strippen als het FR-deel onmiskenbaar Frans is
    (begint met all-caps FR-woord of bevat geaccent. lowercase letters).

    Args:
      text: één tekstlijn (geen ``\\n``).

    Returns:
      Tekst zonder het FR-gedeelte achter de ` / `-separator, of ongewijzigd
      als het patroon niet matcht.
    """
    return _FR_INLINE_SLASH_RE.sub("", text)


def _strip_fr_lines_from_block(text: str) -> str:
    """Verwijder Franstalige regels uit een tweetalig PDF-blok.

    Context: tweetalige Belgische wetteksten (VCF, Registratierechten) bevatten
    blokken waarbij NL en FR tekst op opeenvolgende regels staan binnen
    hetzelfde PDF-blok (bv. centred headings, art-nummers, gedeeltelijke
    body-paragrafen). De `column_filter: nl`-instelling filtert kolom-1 blokken
    weg, maar heeft geen effect op blokken die de volledige breedte beslaan.

    Deze functie werkt op het ruwe blok-tekst met ``\\n``-scheidingen, vóór de
    join in ``_clean_block_text``. Ze verwijdert regels die onmiskenbaar Frans
    zijn op basis van drie criteria:
      1. Regel begint met een FR-structuurlabel (TITRE, CHAPITRE, SECTION, …)
      2. Regel is een "Article N er" French ordegetal-variant
      3. Regel bevat een onmiskenbaar Frans zinsdeel (le présent code, …)
      4. Regel is een letterlijk duplicaat van de vorige NL-regel (bv. dubbel
         art-nummer Art. 1.1.0.0.1.)

    Voor blokken zonder ``\\n`` geldt: als de volledige tekst FR is, wordt een
    lege string teruggegeven (zodat ``_is_noise_block`` het daarna verwijdert).

    Voorzichtigheidsprincipe: twijfelachtige regels worden NIET verwijderd
    (geen taal-score / probability — alleen harde patronen).

    Args:
      text: ruwe blok-tekst met ``\\n`` als regelscheiding.

    Returns:
      Gefilterde tekst met behoud van ``\\n``-scheiding voor resterende regels.
      Lege string als het volledige enkelvoudige blok FR is.
    """
    if "\n" not in text:
        # Enkelvoudige regel: verwijder als het FR-only is.
        if _is_fr_only_line(text):
            return ""
        # Strip inline bilingual suffix: "TABEL I / TABLEAU I" → "TABEL I"
        return _strip_fr_inline_suffix(text)

    lines = text.split("\n")
    kept: list[str] = []
    prev_stripped: str = ""

    for line in lines:
        stripped = line.strip()

        # Duplicaat van vorige regel (bv. art-nummer in NL én FR kolom)
        if stripped and stripped == prev_stripped:
            prev_stripped = stripped
            continue

        # FR-structuurlabel
        if _FR_STRUCT_LINE_RE.match(stripped):
            prev_stripped = stripped
            continue

        # "Article N er" (Frans ordegetal)
        if _FR_ARTICLE_ER_RE.match(stripped):
            prev_stripped = stripped
            continue

        # Onmiskenbaar Franstalig zinsdeel
        if _FR_BODY_MARKERS_RE.search(stripped):
            prev_stripped = stripped
            continue

        # Strip inline bilingual suffix (bv. "TABEL I / TABLEAU I")
        cleaned_line = _strip_fr_inline_suffix(line)
        kept.append(cleaned_line)
        prev_stripped = stripped

    return "\n".join(kept)


# ─── Text-cleanup tussen blokken ──────────────────────────────────────────────

_MULTI_WS = re.compile(r"[ \t\xa0]{2,}")
_SOFT_HYPH = re.compile(r"\xad")
_DOTTED_LEADER = re.compile(r"\s*[\.·]\s*(?:[\.·]\s*){2,}.*\d+\s*$")
_DOTTED_LEADER_INLINE = re.compile(r"\s+(?:\.\s+){3,}")
_BARE_URL = re.compile(r"^\s*(?:https?://)?www\.\S+\s*$", re.I)
_PAGE_NOISE = re.compile(
    r"^(?:\s*[-–—]\s*\d+\s*[-–—]\s*"  # `- 12 -`
    r"|\s*\d{1,4}\s*"                  # bare page number
    r"|\s*pagina\s+\d+\b.*"
    r"|\s*L\s*\d+/\d+\b.*"             # EU-OJ "L 347/31"
    r"|.*?www\.fisconetplus\b.*"       # fisconet running header
    r"|.*?FOD\s+Financi.n.*?(?:Btw|BTW)\s+(?:KB|MB).*"  # FOD-Btw-KB regel
    r")$",
    re.I,
)

# ─── EU-richtlijn specifieke patronen ─────────────────────────────────────────

# Publicatieblad-kopteksten die op y≈50 verschijnen (net buiten top_margin=50).
# Varianten:
#   "NL   L 77/4  Publicatieblad van de Europese Unie  23.3.2011"
#   "11.9.2002 L 243/1 Publicatieblad van de Europese Gemeenschappen NL"
#   "11.12.2006 NL Publicatieblad   van   de   Europese   Unie L   347/21"
#   "Nr . L 326 / 40 Publikatieblad van de Europese Gemeenschappen 21 . 11 . 86"
#       (oudere PDFs uit jaren-80: `Nr . L` prefix, spaties in datum,
#        spelling met `k` en jaar 2-cijfers)
_EU_PB_HEADER_RE = re.compile(
    r"^(?:"
    r"NL\s+"                                                # "NL " prefix
    r"|(?:\d{1,2}\s*\.\s*\d{1,2}\s*\.\s*\d{2,4}\s+)"          # datum-prefix; spaties
                                                              # in datum OK, jaar 2-4 cijfers
    r"|(?:Nr\s*\.\s*L\s+\d+\s*/\s*\d+\s+)"                   # "Nr . L 326 / 40 " (legacy)
    r")"
    r".*?(?:Publi[ck]atieblad|L\s+\d+/\d+).*$",              # k|c spelling
    re.I,
)

# EUR-Lex amendment-markers (traceer-symbolen in geconsolideerde teksten).
# Varianten in EU PB-teksten:
#   ►B / ▼B   — basistekst start / einde
#   ►M1..M9 / ▼M1..M9 — modification (amendement)
#   ►C1..C3 / ▼C1..C3 — correction / rectification (toegevoegd na bevinding
#                       in Richtlijn-2013-34-EU met 23 occurrences)
#   ◄         — close-marker bij inline-bracketing (`►C1 X ◄`)
#
# Optionele spatie tussen pijl en letter-cijfer-code (`► M1`, `▼ C3`) — komt
# voor in wijzigingsoverzicht-tabellen waar PDF-render een spatie inlast.
_EU_AMENDMENT_MARKER_RE = re.compile(
    r"[►▼]\s*[BMC]\d*|◄",
)

# Spaced-letter blokken: EU OJ rendert sectietitels soms als
# "O n d e r a f d e l i n g  3" (spaced individual chars).
# Twee varianten:
#   - single-space: "O n d e r a f d e l i n g 3"
#   - double-space (na _MULTI_WS cleanup al single-space, maar na \n→space
#     kan er alsnog een dubbele ruimte zijn tussen woorden):
#     "H e t  v e r s t r e k k e n  v a n  r e s t a u r a n t ..."
# Heuristic: ≥4 single-char alpha-tokens in de blok-tekst.
_EU_SPACED_LETTER_RE = re.compile(
    r"^(?:[A-Za-z][ ]{1,2}){4,}",
)


def _clean_block_text(text: str, eu_mode: bool = False) -> str:
    """Normaliseer whitespace en strip soft-hyphens / dotted-leaders.

    Args:
      text: ruwe blok-tekst.
      eu_mode: als True, verwijder ook EUR-Lex amendment-markers (►B, ▼M1, ...).
    """
    text = _SOFT_HYPH.sub("", text)
    # Multi-space → single (PDF justification artifact)
    text = _MULTI_WS.sub(" ", text)
    # Normaliseer line-breaks binnen block tot één spatie (PDF wraps zinnen).
    text = re.sub(r"\n+", " ", text)
    # Strip trailing dotted-leader pagination: "Foo . . . . . . . 42" → "Foo"
    text = re.sub(r"\s+(?:\.\s+){3,}(\d+)?\s*$", "", text)
    # Strip inline `. . . . .` runs (vaak TOC-style)
    text = _DOTTED_LEADER_INLINE.sub(" ", text)
    if eu_mode:
        # Strip EUR-Lex amendment-markers (►B, ▼B, ▼M1, ►M2, ...)
        text = _EU_AMENDMENT_MARKER_RE.sub("", text)
    return text.strip()


def _is_noise_block(text: str, eu_mode: bool = False) -> bool:
    """Page-headers, footers, kale URLs, page-numbers etc.

    Args:
      text: gecleande blok-tekst.
      eu_mode: als True, strip ook EU Publicatieblad-kopteksten en
               spaced-letter sectietitels.
    """
    if not text:
        return True
    if _BARE_URL.match(text):
        return True
    if _PAGE_NOISE.match(text):
        return True
    # Dotted-leader-only line (TOC residu)
    if re.fullmatch(r"[\s\.·]+\d*", text):
        return True
    # Art-range alleen (typisch TOC-vermelding): "Art. 24-26"
    if re.fullmatch(r"\s*Art(?:ikel)?\.?\s+\d+\s*[-–]\s*\d+\s*", text, re.I):
        return True
    # Plain-text Justel-structuurlabels die NIET informatief zijn:
    # "Tekst", "Titel", "Inhoudstafel", "BIJLAGEN.", "Bijlage" zonder nummer.
    # Deze duiken op als sectiesplitser in Justel-PDFs en horen niet als
    # heading of body-content.
    if re.fullmatch(
        r"\s*(?:Tekst|Titel|Inhoudstafel|BIJLAGEN\.?|Bijlage|"
        r"Aanhef|Aanvang|Wijzigingsbepalingen|"
        r"Table\s+des\s+matières|Texte|Préambule)\s*",
        text, re.I,
    ):
        return True
    # Standalone "Boek X. -" of "Hoofdstuk X. -" als label (incompleet zonder titel)
    if re.fullmatch(
        r"\s*(?:Boek|Hoofdstuk|Titel|Deel|Afdeling|Onderafdeling)\s+"
        r"[IVXLCDM\d]+\.?\s*-?\s*",
        text, re.I,
    ):
        return True
    if eu_mode:
        # EU Publicatieblad-kopteksten die op y≈50 verschijnen (net buiten
        # top_margin=50): "NL   L 77/4  Publicatieblad van de Europese Unie  23.3.2011"
        if _EU_PB_HEADER_RE.match(text):
            return True
        # Spaced-letter sectietitels: "O n d e r a f d e l i n g 3"
        # Dit zijn supplementaire sectie-subtitels naast ONDERAFDELING/AFDELING
        # headings; de gecompacteerde tekst zou woordgrenzen missen en is
        # minder informatief dan de structurele heading zelf.
        if _EU_SPACED_LETTER_RE.match(text):
            return True
        # Standalone "NL" of "I" / "II" als sectie-marker van het Publicatieblad
        if re.fullmatch(r"\s*(?:NL|FR|DE|EN)\s*", text, re.I):
            return True
        if re.fullmatch(r"\s*[IVX]+\s*", text):
            return True
    return False


# ─── Hoofd-extract per pagina ─────────────────────────────────────────────────

def _render_page(blocks: list[Block], heading_levels: dict[float, int],
                 n_columns: int, eu_mode: bool = False) -> str:
    """Render één pagina naar markdown.

    Volgorde:
      n_columns=1 → blocks sorted by y, dan x.
      n_columns=2 → alle column-0 blocks (sorted by y), dan alle column-1.

    Args:
      eu_mode: activeer EU-richtlijn specifieke filtering (PB-headers, markers).
    """
    if n_columns == 2:
        col0 = sorted([b for b in blocks if b.column == 0], key=lambda b: (b.y0, b.x0))
        col1 = sorted([b for b in blocks if b.column == 1], key=lambda b: (b.y0, b.x0))
        ordered = col0 + col1
    else:
        ordered = sorted(blocks, key=lambda b: (b.y0, b.x0))

    out_parts: list[str] = []
    for b in ordered:
        # Speciale behandeling: blok dat begint met "Art. N" — split de
        # eerste regel als heading, de rest als body.
        raw_lines = b.text.split('\n')
        first_line = raw_lines[0].strip() if raw_lines else ''
        rest_lines = raw_lines[1:]
        m_art = _ART_INLINE_RE.match(first_line)
        if m_art and not _ART_HEAD_RE.match(first_line):
            # "Art. N . Heading-tekst" met body op volgende regels
            art_num = m_art.group(2)
            heading_title = m_art.group(3).strip()
            # Heading-line; titel als korte annotation toevoegen indien zinvol
            if len(heading_title) < 80 and not re.search(r"[\.;:]$", heading_title):
                out_parts.append(f"###### Art. {art_num}. {heading_title}")
            else:
                out_parts.append(f"###### Art. {art_num}")
                # Heading-titel was eigenlijk al body — als gewone tekst toevoegen
                if heading_title:
                    rest_lines.insert(0, heading_title)
            # Body uit rest_lines (joined paragraph)
            body = _clean_block_text('\n'.join(rest_lines), eu_mode=eu_mode)
            if body and not _is_noise_block(body, eu_mode=eu_mode):
                out_parts.append(body)
            continue

        text = _clean_block_text(b.text, eu_mode=eu_mode)
        if not text or _is_noise_block(text, eu_mode=eu_mode):
            continue
        kind, level = _classify_block(b, heading_levels)
        level = min(level, 6)
        if kind in ("heading", "art_heading", "struct_heading"):
            out_parts.append("#" * level + " " + text)
        else:
            out_parts.append(text)
    return "\n\n".join(out_parts)


def _maybe_skip_toc_page(blocks: list[Block]) -> bool:
    """Detecteer of een pagina overwegend uit TOC-entries of cover-titels bestaat.

    Drie patronen worden herkend:
      1. Cover-page: geen lopende body, alleen korte titel-blokken.
      2. Dotted-leader-stijl: `Sectie ... . . . . . . . 42` (≥50% van blokken).
      3. Justel-stijl: pagina bevat "Inhoudstafel" + veel korte
         `Art. N` / `Hoofdstuk N` lijnen zonder lopende body.
    """
    if not blocks:
        return False

    # Patroon 0 — Cover-page: weinig blokken, geen lopende body, mogelijk
    # alle blokken kort (≤120 chars). Typisch eerste pagina met titel +
    # subtitle + datum + URL.
    long_blocks = sum(1 for b in blocks if len(b.text.strip()) > 200)
    short_blocks = sum(1 for b in blocks if 5 <= len(b.text.strip()) <= 120)
    if long_blocks == 0 and short_blocks >= 3 and len(blocks) < 25:
        return True

    if len(blocks) < 5:
        return False

    # Patroon 1: dotted-leaders
    toc_like = 0
    for b in blocks:
        t = b.text
        if re.search(r"\.\s*\.\s*\.\s*.{0,30}\d+\s*$", t) or _DOTTED_LEADER_INLINE.search(t):
            toc_like += 1
    if toc_like >= len(blocks) // 2:
        return True

    # Patroon 2: Justel TOC (en multi-page TOC-continuation)
    # Tellen: korte "Art. N" / "Hoofdstuk N" / "Afdeling N" regels + Art-ranges
    short_struct = 0
    art_ranges = 0
    long_body = 0
    for b in blocks:
        text = b.text.strip()
        if not text:
            continue
        # Art-ranges typisch TOC: "Art. 24-26", "Art. 5-8"
        if re.match(r"^\s*Art(?:ikel)?\.?\s+\d+\s*[-–]\s*\d+\s*$", text, re.I):
            art_ranges += 1
            continue
        # Korte structurele entries (max 80 chars, beginnen met heading-keyword)
        if (len(text) < 80
            and re.match(
                r"^\s*(?:Art(?:ikel)?\.?\s+\d+|Hoofdstuk\s+\d+|Afdeling\s+\d+|"
                r"Onderafdeling\s+\d+|TITEL\s+|BOEK\s+|DEEL\s+|Chapitre\s+|"
                r"Section\s+|Sous-section\s+|TITRE\s+|LIVRE\s+|PARTIE\s+)",
                text, re.I,
            )):
            short_struct += 1
        elif len(text) > 200:
            long_body += 1

    # TOC-page indicators:
    # - ≥2 Art-ranges (`Art. N-M`) + weinig body  → zeker TOC
    # - ≥5 korte struct-entries + geen of weinig body
    if art_ranges >= 2 and long_body <= 1:
        return True
    if short_struct >= 5 and long_body <= 1:
        return True
    if (short_struct + art_ranges) >= 4 and long_body == 0:
        return True

    return False


# ─── Publieke API ─────────────────────────────────────────────────────────────

def extract_pdf(
    pdf_path: Path,
    *,
    force_columns: Optional[int] = None,
    column_filter: str = "both",   # "nl" (only col 0), "fr" (only col 1), "both"
    top_margin: float = 50.0,
    bottom_margin: float = 50.0,
    mode: Optional[str] = None,    # "eu_richtlijn" | None
    section_start: Optional[str] = None,  # regex om start van sectie te vinden
    section_end: Optional[str] = None,    # regex om einde van sectie te vinden
    page_start: Optional[int] = None,     # 1-based start-pagina (inclusief)
    page_end: Optional[int] = None,       # 1-based eind-pagina (inclusief)
) -> str:
    """Extract een wettekst-PDF naar markdown via pymupdf block-extractie.

    Args:
      pdf_path: pad naar PDF-bestand.
      force_columns: 1 of 2 om auto-detect te overrulen.
      column_filter: bij 2-column: "nl" voor enkel linker (NL) kolom,
        "fr" voor rechter, "both" voor beide in NL→FR volgorde.
      top_margin / bottom_margin: y-zones om te strippen als page-noise.
      mode: "eu_richtlijn" activeert EU Publicatieblad-specifieke filtering:
        - Strip PB-kopteksten ("NL   L 77/4  Publicatieblad...") die op
          y≈50 staan (net buiten standaard top_margin=50)
        - Strip EUR-Lex amendment-markers (►B, ▼M1, ...)
        - Strip spaced-letter sectietitels ("O n d e r a f d e l i n g 3")
        - Beperkt column_filter standaard tot "nl" (linker NL-kolom)
    """
    eu_mode = (mode == "eu_richtlijn")

    doc = pymupdf.open(str(pdf_path))
    all_pages_md: list[str] = []

    # Page-range filter: indien page_start/page_end zijn gegeven, beperk
    # tot dat bereik (1-based inclusief).
    if page_start is not None or page_end is not None:
        start_idx = (page_start - 1) if page_start else 0
        end_idx = page_end if page_end else doc.page_count
        page_iter = [doc[i] for i in range(start_idx, min(end_idx, doc.page_count))]
    else:
        page_iter = list(doc)

    # Eerste pass: verzamel ALLE blocks om heading-levels te leren over hele PDF
    all_blocks: list[Block] = []
    per_page_blocks: list[tuple[list[Block], int, float, float]] = []
    for page in page_iter:
        blocks = _extract_page_blocks(page)
        blocks = _filter_margins(blocks, page.rect.height, top_margin, bottom_margin)
        n_cols, split_x = _detect_columns(blocks, page.rect.width)
        if force_columns:
            n_cols = force_columns
            if n_cols == 2 and split_x == page.rect.width:
                split_x = page.rect.width / 2
        _assign_columns(blocks, n_cols, split_x)
        # Filter kolommen indien gewenst
        if n_cols == 2:
            if column_filter == "nl":
                blocks = [b for b in blocks if b.column == 0]
            elif column_filter == "fr":
                blocks = [b for b in blocks if b.column == 1]
        # Strip FR-regels uit tweetalige blokken (bv. centred headings die de
        # volledige paginabreedte beslaan en dus niet door kolom-filter worden
        # gepakt). Alleen actief bij column_filter="nl".
        if column_filter == "nl":
            for b in blocks:
                b.text = _strip_fr_lines_from_block(b.text)
        all_blocks.extend(blocks)
        per_page_blocks.append((blocks, n_cols, split_x, page.rect.height))

    heading_levels = _detect_heading_levels(all_blocks)

    # Tweede pass: render — stateful TOC-skip die alleen aan het BEGIN
    # van het document werkt. Zodra echte body verschijnt, stoppen we
    # met skippen (om latere pseudo-TOC content in de body niet te
    # missen, bv. wijzigingsbepalingen die Art-ranges referencen).
    skip_mode = True   # default aan tot eerste echte body-pagina
    for blocks, n_cols, _, _ in per_page_blocks:
        if skip_mode:
            if _maybe_skip_toc_page(blocks):
                continue
            # Eerste niet-TOC pagina: zet skip_mode af.
            skip_mode = False
        md = _render_page(blocks, heading_levels, n_cols, eu_mode=eu_mode)
        if md:
            all_pages_md.append(md)

    doc.close()
    body = "\n\n".join(all_pages_md)

    # Section-filter: knip body af tot enkel content tussen section_start en
    # section_end regex-patronen. Dit is nodig voor PDFs die meer bevatten dan
    # alleen de gewenste sectie (bv. BS-publicaties met meerdere boeken).
    if section_start:
        m_start = re.search(section_start, body, re.M)
        if m_start:
            body = body[m_start.start():]
    if section_end:
        m_end = re.search(section_end, body, re.M)
        if m_end:
            body = body[: m_end.start()]
    body = body.strip() + "\n"

    return body


# ─── Extractor-interface voor convert.py ──────────────────────────────────────

def extract(cfg: dict, source_name: str) -> str:
    """convert.py-compatible extract-functie.

    Reads:
      cfg['raw']         — pad naar PDF
      cfg['extract']['params']  — optionele tuning-params
    """
    raw = cfg.get("raw")
    if not raw:
        raise RuntimeError(f"{source_name}: ontbrekend 'raw'-veld")
    pdf_path = Path(raw)
    if not pdf_path.is_absolute():
        # Resolve t.o.v. project root
        from pathlib import Path as _P
        root = _P(__file__).resolve().parent.parent.parent.parent
        pdf_path = root / raw
    if not pdf_path.exists():
        raise FileNotFoundError(f"{source_name}: PDF niet gevonden: {pdf_path}")

    params = (cfg.get("extract") or {}).get("params") or {}
    return extract_pdf(
        pdf_path,
        force_columns=params.get("force_columns"),
        column_filter=params.get("column_filter", "both"),
        top_margin=params.get("top_margin", 50.0),
        bottom_margin=params.get("bottom_margin", 50.0),
        mode=params.get("mode"),
        section_start=params.get("section_start"),
        section_end=params.get("section_end"),
        page_start=params.get("page_start"),
        page_end=params.get("page_end"),
    )
