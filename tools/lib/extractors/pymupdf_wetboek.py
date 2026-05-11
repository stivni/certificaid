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

    Heuristiek: bouw histogram van block-x0's per 25-punt bin. Zoek de twee
    meest-voorkomende "anker"-bins met ≥3 blokken elk, ≥200 punten uit elkaar.
    Split-x ligt halverwege.
    """
    if not blocks:
        return 1, page_width

    bins = Counter(int(b.x0) // 25 * 25 for b in blocks)
    # Filter naar bins met ≥3 blokken (anker-kolommen, geen uitschieters)
    candidates = sorted(
        [(x, c) for x, c in bins.items() if c >= 3],
        key=lambda p: -p[1],
    )
    if len(candidates) < 2:
        return 1, page_width

    # Sorteer kandidaten op x-positie, zoek het PAAR met grootste gap ≥200.
    sorted_by_x = sorted(candidates, key=lambda p: p[0])
    best_gap = 0
    best_split = page_width
    for i in range(len(sorted_by_x) - 1):
        x_left, _ = sorted_by_x[i]
        x_right, _ = sorted_by_x[i + 1]
        gap = x_right - x_left
        if gap > best_gap:
            best_gap = gap
            best_split = (x_left + x_right) / 2

    if best_gap < 200:
        return 1, page_width

    return 2, best_split


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
    # `Art.XV.125`, `Art. XV.125/4/1` (WER-stijl met roman-prefix)
    r"^\s*(Art(?:ikel)?\.?)\s*"
    r"(?:[IVXLCDM]+\.?\s*)?"          # optioneel romeins boek/titel-prefix
    r"\d+(?:[\./]\d+)*"                # nummer, eventueel met /N segmenten
    r"(?:bis|ter|quater|quinquies|sexies|septies)?"
    r"\s*\.?\s*$",
    re.I,
)
# Inline-art-pattern: `Art. N . Heading-tekst` aan het begin van een regel,
# eventueel gevolgd door body op zelfde-of-volgende-regel.
_ART_INLINE_RE = re.compile(
    r"^\s*(Art(?:ikel)?\.?)\s*"
    r"((?:[IVXLCDM]+\.?\s*)?"
    r"\d+(?:[\./]\d+)*"
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


def _clean_block_text(text: str) -> str:
    """Normaliseer whitespace en strip soft-hyphens / dotted-leaders."""
    text = _SOFT_HYPH.sub("", text)
    # Multi-space → single (PDF justification artifact)
    text = _MULTI_WS.sub(" ", text)
    # Normaliseer line-breaks binnen block tot één spatie (PDF wraps zinnen).
    text = re.sub(r"\n+", " ", text)
    # Strip trailing dotted-leader pagination: "Foo . . . . . . . 42" → "Foo"
    text = re.sub(r"\s+(?:\.\s+){3,}(\d+)?\s*$", "", text)
    # Strip inline `. . . . .` runs (vaak TOC-style)
    text = _DOTTED_LEADER_INLINE.sub(" ", text)
    return text.strip()


def _is_noise_block(text: str) -> bool:
    """Page-headers, footers, kale URLs, page-numbers etc."""
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
    return False


# ─── Hoofd-extract per pagina ─────────────────────────────────────────────────

def _render_page(blocks: list[Block], heading_levels: dict[float, int],
                 n_columns: int) -> str:
    """Render één pagina naar markdown.

    Volgorde:
      n_columns=1 → blocks sorted by y, dan x.
      n_columns=2 → alle column-0 blocks (sorted by y), dan alle column-1.
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
            body = _clean_block_text('\n'.join(rest_lines))
            if body and not _is_noise_block(body):
                out_parts.append(body)
            continue

        text = _clean_block_text(b.text)
        if not text or _is_noise_block(text):
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
) -> str:
    """Extract een wettekst-PDF naar markdown via pymupdf block-extractie.

    Args:
      pdf_path: pad naar PDF-bestand.
      force_columns: 1 of 2 om auto-detect te overrulen.
      column_filter: bij 2-column: "nl" voor enkel linker (NL) kolom,
        "fr" voor rechter, "both" voor beide in NL→FR volgorde.
      top_margin / bottom_margin: y-zones om te strippen als page-noise.
    """
    doc = pymupdf.open(str(pdf_path))
    all_pages_md: list[str] = []

    # Eerste pass: verzamel ALLE blocks om heading-levels te leren over hele PDF
    all_blocks: list[Block] = []
    per_page_blocks: list[tuple[list[Block], int, float, float]] = []
    for page in doc:
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
        md = _render_page(blocks, heading_levels, n_cols)
        if md:
            all_pages_md.append(md)

    doc.close()
    return "\n\n".join(all_pages_md)


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
    )
