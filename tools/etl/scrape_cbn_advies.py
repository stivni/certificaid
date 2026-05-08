#!/usr/bin/env python3
"""
CBN-advies scraper v2 — gestructureerde extractie met behoud van semantiek.

Verbeteringen t.o.v. tools/etl/reprocess_cbn_adviezen.py:

  1. Robuuste H1-selectie
       Filtert "COMMISSIE VOOR..." (org) en "Advies van DATUM" (datum) weg,
       kiest de langste resterende H1 als titel. Geen positionele logica.

  2. Footnotes als Markdown-footnotes
       <a class="see-footnote">N</a>  →  [^N] in lopende tekst
       <li class="footnote">          →  [^N]: definitie onderaan
       Voetnootteksten staan ook in het `title=""` attribuut van de ref —
       gebruikt als fallback.

  3. Hiërarchie behouden
       ##, ###, #### blijven zoals in de bron. Geen normalisatie.

  4. Journaalpost-tabellen (`table-no-padding`)
       Speciaal handler: 6-koloms CBN-formaat → schone 5-koloms Markdown-tabel
       [D/C-marker | rknr | omschrijving | debet | credit].
       Templates (lege bedragen) en concrete voorbeelden krijgen hetzelfde
       formaat zodat downstream de structuur uniform is.

  5. Gerelateerde adviezen in frontmatter
       <h2>Gerelateerde adviezen</h2> blok → YAML-lijst met titel + URL,
       zodat downstream concept-records er direct naar kunnen linken.

  6. TOC stripping
       Detecteert genummerde plain-text TOC-blokken direct na de H1
       (`1. Naam\n\n2. Naam\n\n...`) en het `- Select -...` dropdown-artefact.

Gebruik:
    python3 tools/etl/scrape_cbn_advies.py --url URL                  # dry-run, print stdout
    python3 tools/etl/scrape_cbn_advies.py --url URL --out PATH       # schrijf naar bestand
    python3 tools/etl/scrape_cbn_advies.py --refresh PATH             # ververs bestaand bestand vanaf zijn `bron:` URL
"""
from __future__ import annotations

import argparse
import hashlib
import io
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.lib.provenance import (  # noqa: E402
    Input, Provenance, Tooling, Trust,
    git_short_sha, now_iso,
)
from ruamel.yaml import YAML  # noqa: E402


PIPELINE_REL = "tools/etl/scrape_cbn_advies.py"


def _yaml() -> YAML:
    y = YAML()
    y.preserve_quotes = True
    y.indent(mapping=2, sequence=4, offset=2)
    y.width = 4096
    return y


_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


# ─── Datatypes ────────────────────────────────────────────────────────────────

@dataclass
class JournaalpostRij:
    """Eén regel uit een boekhoudkundige journaalpost."""
    dc_marker: str = ""        # "" voor eerste debet-regel, "aan" voor credit
    rekening: str = ""
    omschrijving: str = ""
    debet: str = ""
    credit: str = ""


@dataclass
class Journaalpost:
    titel: str = "Boeking"     # "Boeking" of "Boeking — Voorbeeld N"
    rijen: list[JournaalpostRij] = field(default_factory=list)


@dataclass
class GerelateerdAdvies:
    titel: str
    url: str
    datum: str = ""           # ISO-datum als beschikbaar in HTML


# ─── HTML → Markdown parser ───────────────────────────────────────────────────

class CBNAdviceParser(HTMLParser):
    """Parser voor CBN-advies pagina's met behoud van semantiek."""

    BLOCK_TAGS = frozenset(['script', 'style', 'noscript'])
    # Note: <sup> NIET hier — sommige CBN-pages hebben geen sup, andere wel,
    # en als sup een footnote-cijfer bevat willen we het als footnote-ref
    # behandelen. Default: behoud de inhoud (cijfer).

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.result: list[str] = []
        self.list_stack: list[tuple[str, int]] = []
        self.skip_stack: list[str] = []
        self._pending_nl = 0

        # Voetnoten
        # ref-anchor (id="footnoteref3_xxx") → nummer + tekst (uit title=)
        self.footnote_refs: list[tuple[str, str]] = []  # (number, title_text)
        # def-anchor (id="footnote3_xxx") → nummer + definitie (geaccumuleerd)
        self.footnote_defs: dict[str, list[str]] = {}
        self._current_footnote_def: str | None = None

        # Journaalposten
        self.journaalposten: list[Journaalpost] = []
        self._jp_current: Journaalpost | None = None
        self._jp_current_row: list[str] | None = None
        self._jp_current_cell: list[str] | None = None
        self._jp_current_cell_colspan: int = 1

        # <p class="indented"> sectietitels → ### heading
        # Als deze flag aan staat, worden <strong>/<b> markers weggefilterd
        # zodat de heading plain text is (niet "### **tekst**").
        self._in_indented_p: bool = False

        # Niet-footnote <a href="..."> links → [text](url)
        # Bevat de genormaliseerde URL zolang we binnen de link-tag zitten.
        self._pending_link_href: str | None = None

    # ── helpers ──────────────────────────────────────────────────────────────

    def _skipping(self):
        return len(self.skip_stack) > 0

    def _ensure_nl(self, n):
        if n > self._pending_nl:
            self._pending_nl = n

    def _flush(self, text=''):
        if self._pending_nl and (self.result or text.strip()):
            self.result.append('\n' * self._pending_nl)
            self._pending_nl = 0
        if text:
            self.result.append(text)

    def _emit(self, s: str):
        """Output direct naar journaalpost-cel (als we daarin zitten)
        anders naar self.result."""
        if self._jp_current_cell is not None:
            self._jp_current_cell.append(s)
        else:
            self.result.append(s)

    # ── tag handlers ─────────────────────────────────────────────────────────

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)

        # Skip blocks
        if tag in self.BLOCK_TAGS:
            self.skip_stack.append(tag)
            return
        if self._skipping():
            return

        cls = attr_dict.get('class', '')

        # ── Footnote ref: <a class="see-footnote" title="..." href="#footnoteN_..">N</a>
        if tag == 'a' and 'see-footnote' in cls:
            href = attr_dict.get('href', '')
            title = attr_dict.get('title', '')
            # Get the footnote number from href
            m = re.search(r'#footnote(\d+)_', href)
            if m:
                num = m.group(1)
                self.footnote_refs.append((num, title))
                self._flush(f'[^{num}]')
                # Skip the inner text (the number itself)
                self.skip_stack.append(tag)
                return

        # ── Footnote def: <li class="footnote" id="footnoteN_xxx">
        if tag == 'li' and 'footnote' in cls:
            fn_id = attr_dict.get('id', '')
            m = re.search(r'footnote(\d+)_', fn_id)
            if m:
                self._current_footnote_def = m.group(1)
                self.footnote_defs[m.group(1)] = []
                # Don't emit anything; we'll capture text into footnote_defs
                return

        # ── Footnote def label (skip the link text "1" inside the def)
        if tag == 'a' and 'footnote-label' in cls:
            self.skip_stack.append(tag)
            return

        # ── Journaalpost table: <table class="table-no-padding"> of "booking-table-top">
        if tag == 'table' and ('table-no-padding' in cls or 'booking-table-top' in cls):
            self._jp_current = Journaalpost()
            self._jp_current_row = None
            return

        if self._jp_current is not None:
            if tag == 'tr':
                self._jp_current_row = []
                return
            if tag in ('td', 'th'):
                self._jp_current_cell = []
                colspan = attr_dict.get('colspan', '1')
                try:
                    self._jp_current_cell_colspan = int(colspan)
                except ValueError:
                    self._jp_current_cell_colspan = 1
                return
            # Inside journaalpost table: ignore other tags' formatting (just keep text)
            return

        # ── Headings — keep hierarchy
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            level = int(tag[1])
            self._ensure_nl(2)
            self._flush('#' * level + ' ')

        elif tag == 'p':
            # <p class="indented"> is een sectietitel → ### heading
            if 'indented' in cls:
                self._in_indented_p = True
                self._ensure_nl(2)
                self._flush('### ')
            else:
                self._ensure_nl(2)

        elif tag in ('strong', 'b'):
            # Binnen een <p class="indented"> willen we GEEN ** markers —
            # de heading-prefix (### ) is al uitgestoten; enkel plain text.
            if not self._in_indented_p:
                self._flush('**')

        elif tag in ('em', 'i'):
            self._flush('*')

        elif tag == 'br':
            self._flush('  \n')

        elif tag == 'hr':
            self._ensure_nl(2)
            self._flush('---')
            self._ensure_nl(2)

        elif tag == 'ul':
            self.list_stack.append(('ul', 0))
            self._ensure_nl(1)

        elif tag == 'ol':
            self.list_stack.append(('ol', 0))
            self._ensure_nl(1)

        elif tag == 'li':
            if self.list_stack:
                kind, counter = self.list_stack[-1]
                indent = '  ' * (len(self.list_stack) - 1)
                if kind == 'ol':
                    counter += 1
                    self.list_stack[-1] = ('ol', counter)
                    self._pending_nl = 0
                    self.result.append(f'\n{indent}{counter}. ')
                else:
                    self._pending_nl = 0
                    self.result.append(f'\n{indent}- ')

        # ── Niet-footnote hyperlinks → [tekst](url) in Markdown
        # Footnote-<a>'s zijn al eerder afgehandeld (zie boven, met return).
        # Hier vangen we bij. bijlage-links, externe verwijzingen, etc.
        elif tag == 'a':
            href = attr_dict.get('href', '')
            # Sla anker-only links over (#...) en gerelateerde-adviezen-links
            # (/adviezen/... worden verwerkt door extract_gerelateerde_adviezen)
            if href and not href.startswith('#') and '/adviezen/' not in href:
                # Relatieve URLs → absoluut
                if href.startswith('/'):
                    href = f'https://www.cbn-cnc.be{href}'
                self._pending_link_href = href
                self._flush('[')

        # Generieke tabellen (niet journaalpost) — gewone Markdown-tabel
        elif tag == 'table':
            self._ensure_nl(2)

        elif tag == 'tr':
            if self._pending_nl == 0 and self.result:
                self.result.append('\n')

        elif tag in ('th', 'td'):
            self._flush('| ')

    def handle_endtag(self, tag):
        if tag in self.BLOCK_TAGS:
            if self.skip_stack and self.skip_stack[-1] == tag:
                self.skip_stack.pop()
            return

        # Pop matching skip if any
        if self.skip_stack and self.skip_stack[-1] == tag:
            self.skip_stack.pop()
            return
        if self._skipping():
            return

        # ── Footnote def end
        if tag == 'li' and self._current_footnote_def is not None:
            self._current_footnote_def = None
            return

        # ── Journaalpost table close
        if self._jp_current is not None:
            if tag in ('td', 'th'):
                # Save cell content
                cell_text = ''.join(self._jp_current_cell or []).strip()
                if self._jp_current_row is not None:
                    # Add cell, plus empty placeholders for colspan>1
                    self._jp_current_row.append(cell_text)
                    for _ in range(self._jp_current_cell_colspan - 1):
                        self._jp_current_row.append('')
                self._jp_current_cell = None
                self._jp_current_cell_colspan = 1
                return
            if tag == 'tr':
                if self._jp_current_row:
                    # Convert 6-col raw row to JournaalpostRij
                    rij = self._build_jp_rij(self._jp_current_row)
                    if rij:
                        self._jp_current.rijen.append(rij)
                self._jp_current_row = None
                return
            if tag == 'table':
                # Render journaalpost into result
                self._render_journaalpost(self._jp_current)
                self.journaalposten.append(self._jp_current)
                self._jp_current = None
                return
            return  # other tags inside table: ignore

        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self._ensure_nl(2)
        elif tag == 'p':
            self._in_indented_p = False
            self._ensure_nl(2)
        elif tag in ('strong', 'b'):
            if not self._in_indented_p:
                self._flush('**')
        elif tag == 'a':
            # Sluit een niet-footnote link: emit ](url)
            if self._pending_link_href:
                self._flush(f']({self._pending_link_href})')
                self._pending_link_href = None
        elif tag in ('em', 'i'):
            self._flush('*')
        elif tag in ('ul', 'ol'):
            if self.list_stack:
                self.list_stack.pop()
            self._ensure_nl(2)
        elif tag in ('th', 'td'):
            self._flush(' |')
        elif tag == 'table':
            self._ensure_nl(2)

    def handle_data(self, data):
        if self._skipping():
            return

        # Capture footnote definition text
        if self._current_footnote_def is not None:
            self.footnote_defs[self._current_footnote_def].append(data)
            return

        # Capture journaalpost cell text
        if self._jp_current_cell is not None:
            self._jp_current_cell.append(data)
            return
        if self._jp_current is not None:
            # Inside journaalpost table but outside a cell — ignore
            return

        text = data
        if text.strip():
            self._flush(text)
        elif self.result and not self.result[-1].endswith('\n'):
            self._flush(' ')

    # ── Journaalpost rendering ──────────────────────────────────────────────

    @staticmethod
    def _build_jp_rij(raw_cells: list[str]) -> JournaalpostRij | None:
        """
        Maak een JournaalpostRij uit de 4-6 ruwe cellen.

        CBN 6-kol layout: [rknr | aan-marker | rknr_credit | omschrijving | debet | credit]
        Maar door colspan="3" op omschrijving wordt rij 1 vaak: [rknr | omschrijving | "" | "" | debet | credit]
        We normaliseren naar { dc_marker, rekening, omschrijving, debet, credit }.
        """
        # Strip alle cellen
        cells = [c.strip() for c in raw_cells]

        # Lege rij overslaan
        if not any(cells):
            return None

        # Heuristiek: zoek de "aan"-marker positie
        aan_idx = None
        for i, c in enumerate(cells):
            if c.lower() == 'aan':
                aan_idx = i
                break

        rij = JournaalpostRij()

        if aan_idx is not None:
            # Credit-rij
            rij.dc_marker = "aan"
            # Rekeningnr is direct na "aan"
            if aan_idx + 1 < len(cells):
                rij.rekening = cells[aan_idx + 1]
            if aan_idx + 2 < len(cells):
                rij.omschrijving = cells[aan_idx + 2]
            # Bedragen: laatste 2 niet-lege cellen erna
            tail = [c for c in cells[aan_idx + 3:] if c]
            if len(tail) >= 1:
                rij.credit = tail[-1] if len(tail) == 1 else (tail[-1] or tail[-2])
            if len(tail) >= 2:
                rij.debet = tail[-2]
        else:
            # Debet-rij: eerste niet-lege cel = rknr, tweede = omschrijving
            non_empty = [(i, c) for i, c in enumerate(cells) if c]
            if non_empty:
                rij.rekening = non_empty[0][1]
                if len(non_empty) >= 2:
                    rij.omschrijving = non_empty[1][1]
                if len(non_empty) >= 3:
                    rij.debet = non_empty[-2][1] if len(non_empty) >= 4 else non_empty[2][1]
                if len(non_empty) >= 4:
                    rij.credit = non_empty[-1][1]

        return rij

    def _render_journaalpost(self, jp: Journaalpost):
        """Render een journaalpost als Markdown-tabel."""
        self._ensure_nl(2)
        self._flush('| | Rekening | Omschrijving | Debet | Credit |\n')
        self._flush('|---|----------|--------------|-------|--------|\n')
        for r in jp.rijen:
            line = f'| {r.dc_marker} | {r.rekening} | {r.omschrijving} | {r.debet} | {r.credit} |'
            self._flush(line + '\n')
        self._ensure_nl(2)

    # ── Output ──────────────────────────────────────────────────────────────

    def get_markdown(self) -> str:
        return ''.join(self.result)


# ─── HTML extractie helpers ───────────────────────────────────────────────────

def extract_advice_content(html: str) -> str:
    """Extraheer het echte adviesblok uit de pagina."""
    patterns = [
        r'<div[^>]+field--name-field-advice-text[^>]*>(.*?)</div\s*>\s*</div\s*>',
        r'<div[^>]+class="[^"]*group-content[^"]*"[^>]*>(.*?)</div\s*>\s*</div\s*>',
        r'<main[^>]*>(.*?)</main>',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.DOTALL | re.IGNORECASE)
        if m and len(m.group(1).strip()) > 200:
            return m.group(1)
    return html


def select_title(html: str) -> str | None:
    """Robuuste titelselectie: filter org-naam + datum, kies langste rest.

    Sommige oudere CBN-pagina's combineren org-naam + titel in één <h1>:
      "COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN CBN-advies 106/4 - Titel Advies van 1 jan 1990"
    In dat geval strippen we de prefix/suffix en houden enkel de eigenlijke titel.
    """
    candidates = []
    for m in re.finditer(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = re.sub(r'\s+', ' ', text)
        if not text:
            continue
        if 'COMMISSIE' in text.upper() or 'COMMISSION DES' in text.upper():
            # Probeer de eigenlijke titel te extraheren:
            # strip "COMMISSIE VOOR ... NORMEN" of "COMMISSION DES NORMES ..." prefix
            cleaned = re.sub(
                r'^(?:COMMISSIE\s+VOOR\b.*?NORMEN|COMMISSION\s+DES\s+NORMES[^\n]*?)\s+',
                '', text, flags=re.IGNORECASE
            )
            # strip "Advies van DD maand YYYY" of "Avis du ..." suffix
            cleaned = re.sub(
                r'\s+(?:Advies|Avis)\s+(?:van|du)\s+\d.*$', '', cleaned, flags=re.IGNORECASE
            )
            cleaned = cleaned.strip()
            # Alleen opnemen als er nog een zinvolle titel overblijft
            if cleaned and len(cleaned) > 5 and not re.match(
                r'^(?:Advies|Avis)\s+(?:van|du)\s+\d', cleaned, re.IGNORECASE
            ):
                candidates.append(cleaned)
            continue
        if re.match(r'^Advies van\s+\d', text, re.IGNORECASE):
            continue
        if re.match(r'^Avis du\s+\d', text, re.IGNORECASE):  # FR variant
            continue
        candidates.append(text)
    if not candidates:
        return None
    return max(candidates, key=len)


def extract_gerelateerde_adviezen(html: str) -> list[GerelateerdAdvies]:
    """Extraheer 'Gerelateerde adviezen' blok als gestructureerde lijst."""
    refs: list[GerelateerdAdvies] = []
    m = re.search(r'<h2[^>]*>Gerelateerde adviezen</h2>(.*?)(?=<aside|<footer|</main|</article)',
                  html, re.DOTALL | re.IGNORECASE)
    if not m:
        return refs
    block = m.group(1)
    # Find each views-row
    for row_m in re.finditer(r'<div[^>]+class="views-row"[^>]*>(.*?)(?=<div[^>]+class="views-row"|</div\s*>\s*</div\s*>\s*</div)',
                              block, re.DOTALL):
        row_html = row_m.group(1)
        # Datum
        date_m = re.search(r'datetime="([^"]+)"', row_html)
        datum = date_m.group(1)[:10] if date_m else ""
        # Titel-link
        link_m = re.search(r'<a[^>]+href="(/nl/adviezen/[^"]+)"[^>]*>([^<]+)</a>', row_html)
        if link_m:
            href = link_m.group(1)
            titel = link_m.group(2).strip()
            url = f"https://www.cbn-cnc.be{href}"
            refs.append(GerelateerdAdvies(titel=titel, url=url, datum=datum))
    return refs


def extract_advice_date(html: str) -> str | None:
    """Extract advies-datum uit 'Advies van DATUM' H1 of <time> tag."""
    # H1: "Advies van 20 februari 2013"
    for m in re.finditer(r'<h1[^>]*>(?:Advies van|Avis du)\s+([^<]+)</h1>', html, re.IGNORECASE):
        return m.group(1).strip()
    # <time datetime="2013-02-20T...">
    m = re.search(r'<time\s+datetime="(\d{4}-\d{2}-\d{2})', html)
    if m:
        return m.group(1)
    return None


# ─── Markdown post-processing ────────────────────────────────────────────────

_TOC_NUMBERED_LINE = re.compile(r'^\s*\d+\.\s+\S')
_SELECT_DROPDOWN = re.compile(r'^\s*-\s*Select\s*-')

# Noise-regels die op CBN-pagina's voorkomen, ongeacht of ze als <h1> of plain
# zijn gerenderd. We strippen ze uit de body zodat enkel inhoudelijke tekst overblijft.
_BODY_NOISE_LINE_PATTERNS = [
    # Org-naam — robuust voor typos ("BOEKHOUNIDGE" i.p.v. "BOEKHOUDKUNDIGE" in CBN-2017-13)
    re.compile(r'^[ \t]*#?\s*COMMISSIE\s+VOOR\b.*NORMEN\s*$', re.IGNORECASE),
    re.compile(r'^[ \t]*#?\s*COMMISSION\s+DES\s+NORMES\b.*$', re.IGNORECASE),  # FR variant
    # Datum-line ("Advies van 5 oktober 2011" / "Avis du …")
    re.compile(r'^[ \t]*#?\s*Advies\s+van\s+\d.*$', re.IGNORECASE),
    re.compile(r'^[ \t]*#?\s*Avis\s+du\s+\d.*$', re.IGNORECASE),
    # Duplicaat van titel-H1 (begint met "# CBN-advies" of "# Avis CNC")
    re.compile(r'^[ \t]*#\s+CBN-advies\s.*$', re.IGNORECASE),
    re.compile(r'^[ \t]*#\s+Avis\s+CNC\s.*$', re.IGNORECASE),
    # Lege H1's: `#`, `# `, `#   \xa0`, etc.
    re.compile(r'^[ \t]*#[ \t]*[\xa0\s]*$'),
]


def _is_body_noise(line: str) -> bool:
    return any(p.match(line) for p in _BODY_NOISE_LINE_PATTERNS)


def _strip_body_noise(md: str) -> str:
    """
    Strip noise-regels uit de body:
      - H1 met "COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN"
      - Plain-text variant van dezelfde
      - "Advies van DATUM" als H1 of als gewone regel
      - Duplicate titel-H1 ("# CBN-advies ...")

    Doet dit overal in de body — niet enkel aan de top — omdat sommige pagina's
    deze regels op verschillende posities hebben.
    """
    out = []
    for line in md.split('\n'):
        if _is_body_noise(line):
            continue
        out.append(line)
    return '\n'.join(out)


def strip_toc_block(md: str) -> str:
    """
    Verwijder TOC-artefact direct na de eerste H1/H2:
      - "- Select - ..." dropdown-regel
      - Genummerde lijst (1. ... 2. ...) zonder secundaire content
    Stopt bij eerste echte sectie (## of empty-line gevolgd door tekst).
    """
    lines = md.split('\n')
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Detect "- Select -..." artifact
        if _SELECT_DROPDOWN.match(line):
            i += 1
            continue
        result.append(line)
        i += 1

    # Now detect a TOC block: sequence of numbered list items immediately
    # followed by a `## ` header, with no paragraphs in between.
    md = '\n'.join(result)

    # Find the first ## heading
    hh = re.search(r'^##\s+', md, re.MULTILINE)
    if not hh:
        return md
    head_pos = hh.start()
    head_section = md[:head_pos]
    rest = md[head_pos:]

    # In head_section, strip trailing numbered-list-only block
    head_lines = head_section.split('\n')
    # walk backwards: drop trailing lines that match _TOC_NUMBERED_LINE or are blank
    drop_count = 0
    for j in range(len(head_lines) - 1, -1, -1):
        line = head_lines[j]
        if line.strip() == '':
            drop_count += 1
            continue
        if _TOC_NUMBERED_LINE.match(line):
            drop_count += 1
            continue
        break

    if drop_count > 2:  # need at least one numbered item to consider it a TOC
        head_lines = head_lines[:len(head_lines) - drop_count]
        head_section = '\n'.join(head_lines).rstrip() + '\n\n'
        return head_section + rest

    return md


def append_footnotes(md: str, footnote_defs: dict[str, list[str]],
                     footnote_refs: list[tuple[str, str]]) -> str:
    """
    Voeg de footnote-definities toe aan het einde van het document
    in Markdown-footnote syntax: [^N]: definition

    Als geen `<li class="footnote">` definities zijn opgevangen,
    fallback op de title= attributen van de refs.
    """
    if not footnote_defs and not footnote_refs:
        return md

    seen = set()
    blocks = []

    # Verzamel uit footnote_defs (autoritatief)
    for num, parts in footnote_defs.items():
        text = ''.join(parts).strip()
        text = re.sub(r'\s+', ' ', text)
        if text:
            blocks.append(f'[^{num}]: {text}')
            seen.add(num)

    # Fallback: refs met title=
    for num, title in footnote_refs:
        if num in seen:
            continue
        title = re.sub(r'\s+', ' ', title.strip())
        if title:
            blocks.append(f'[^{num}]: {title}')
            seen.add(num)

    if not blocks:
        return md

    # Sort by number
    blocks.sort(key=lambda b: int(re.match(r'\[\^(\d+)\]', b).group(1)))
    return md.rstrip() + '\n\n' + '\n\n'.join(blocks) + '\n'


_IMPLICIT_HEADING_PATTERNS = [
    # *Voorbeeld 1* / *Voorbeeld 1: titel* / *Voorbeeld 1 - titel*
    re.compile(r'^\s*\*\s*(Voorbeeld\s+\d+[^*\n]*?)\s*\*\s*$'),
    # *Casus N* / *Geval N* (zelfde patroon als Voorbeeld)
    re.compile(r'^\s*\*\s*(Casus\s+\d+[^*\n]*?|Geval\s+\d+[^*\n]*?)\s*\*\s*$'),
    # CBN-pagina's gebruiken soms enkel "**Inleiding**" / "**Algemeen**" etc.
    re.compile(r'^\s*\*\*\s*(Inleiding|Algemeen|Conclusie|Onderwerp van het advies|Toepassingsgebied|Boekhoudkundige verwerking|Voorbeelden?|Samenvatting|Besluit)\s*\*\*\s*$', re.IGNORECASE),
    # **N. Sectietitel** of **N.N. Sectietitel** — vetgedrukte stand-alone paragraaf
    # die een genummerd sectietitel is (4–80 tekens na het nummer).
    # Capt: "**3. BOEKHOUDKUNDIGE VERWERKING**" of "**1.2. Toepassing van de norm**"
    re.compile(r'^\s*\*\*(\d+(?:\.\d+)*\.?\s+[^\*\n]{4,80}?)\*\*\s*$'),
]

# Brede variant voor vetgedrukte ongenummerde sectietitels — alleen promoveren
# als de lijn volledig geïsoleerd staat (vorige én volgende lijn zijn leeg).
# Minimumlengte 20 tekens om inline-bold-fragmenten te vermijden.
_BOLD_TITLE_STANDALONE = re.compile(r'^\s*\*\*([^\*\n]{20,}?)\*\*\s*$')


def promote_implicit_headings(md: str) -> str:
    """
    Detecteer paragrafen die feitelijk sectietitels zijn (in italic of bold)
    en converteer naar `## ` headings — zodat de chunker ze als grenzen ziet.

    Specifieke patronen (zonder contextcheck):
        *Voorbeeld 1*           → ## Voorbeeld 1
        *Voorbeeld 2: aankoop*  → ## Voorbeeld 2: aankoop
        **Inleiding**           → ## Inleiding
        **3. BOEKHOUDKUNDIGE VERWERKING** → ## 3. BOEKHOUDKUNDIGE VERWERKING

    Brede patronen (MET contextcheck: vorige + volgende lijn leeg):
        **Toepassingsgebied van de aanbevolen principes** → ## Toepassingsgebied...
    Uitgesloten: regels die eindigen op .?! (dan is het een zin, geen titel).
    """
    lines = md.split('\n')
    out_lines = []
    for i, line in enumerate(lines):
        replaced = False

        # Specifieke patronen — geen contextcheck nodig
        for pat in _IMPLICIT_HEADING_PATTERNS:
            m = pat.match(line)
            if m:
                title = m.group(1).strip()
                out_lines.append(f'## {title}')
                replaced = True
                break

        if not replaced:
            # Brede bold-only paragraaf — enkel promoveren als geïsoleerd
            m = _BOLD_TITLE_STANDALONE.match(line)
            if m:
                prev_blank = (i == 0 or not lines[i - 1].strip())
                next_blank = (i >= len(lines) - 1 or not lines[i + 1].strip())
                if prev_blank and next_blank:
                    title = m.group(1).strip()
                    # Sla over als de tekst eindigt als een zin (dan is het proza)
                    if not re.search(r'[\.\?\!]$', title):
                        out_lines.append(f'## {title}')
                        replaced = True

        if not replaced:
            out_lines.append(line)
    return '\n'.join(out_lines)


def cleanup_markdown(md: str) -> str:
    """Algemene cleanup: blank-runs, footnote-refs, trailing artefacten."""
    # Strip lone whitespace lines
    lines = [(l if l.strip() else '') for l in md.split('\n')]
    md = '\n'.join(lines)

    # Footnote-refs: collapse `[^N]\n` of `[^N]\n.` naar inline.
    # Vóór punctuatie: zero whitespace.
    md = re.sub(r'(\[\^\d+\])\s*\n\s*([\.\,\;\:\)\]])', r'\1\2', md)
    # Vóór gewone letterlijke tekst: één spatie. NIET collapsen vóór `|` (tabel)
    # of `#` (heading) of `-` (list-item) — die markeren een nieuw blok.
    md = re.sub(
        r'(\[\^\d+\])[ \t]*\n[ \t]+(?=[A-Za-zéèêëàâîïôûüçñ"“”\(\[])',
        r'\1 ', md
    )

    # Trailing-artefact verwijderen: rij van losse asterisken op een regel
    md = re.sub(r'^\s*\*+(\s*\*+)*\s*$', '', md, flags=re.MULTILINE)

    # Max 2 blank lines
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip() + '\n'


# ─── Fetch ──────────────────────────────────────────────────────────────────

def fetch_html(url: str) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
            'Accept': 'text/html,application/xhtml+xml',
            'Accept-Language': 'nl,en;q=0.8',
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            return resp.status, resp.read().decode('utf-8', errors='replace')
    except urllib.error.HTTPError as e:
        return e.code, ''
    except Exception as e:
        return 0, str(e)


# ─── High-level scrape ──────────────────────────────────────────────────────

@dataclass
class ScrapedAdvice:
    titel: str
    url: str
    datum: str
    gerelateerde: list[GerelateerdAdvies]
    body: str
    journaalposten: list[Journaalpost]


def scrape(url: str) -> tuple[ScrapedAdvice, str]:
    """Scrape een CBN-advies pagina.

    Returnt (ScrapedAdvice, raw_html). De raw HTML wordt teruggegeven zodat
    de provenance-builder een sha256 kan berekenen voor stale-detectie bij
    latere refreshes.
    """
    status, html = fetch_html(url)
    if status != 200:
        raise RuntimeError(f"HTTP {status} voor {url}")

    titel = select_title(html) or "(geen titel gevonden)"
    datum = extract_advice_date(html) or ""
    gerelateerde = extract_gerelateerde_adviezen(html)

    content_html = extract_advice_content(html)
    parser = CBNAdviceParser()
    parser.feed(content_html)
    raw_md = parser.get_markdown()

    # Strip H1's en "COMMISSIE..." / "Advies van DATUM"-noise uit de body.
    # De titel komt al apart in render_full_markdown via een eigen H1; eventuele
    # H1's in de body zijn dus duplicaten/noise (org-naam, datum, of titel).
    raw_md = _strip_body_noise(raw_md)

    body = strip_toc_block(raw_md)
    body = promote_implicit_headings(body)
    body = append_footnotes(body, parser.footnote_defs, parser.footnote_refs)
    body = cleanup_markdown(body)

    adv = ScrapedAdvice(
        titel=titel,
        url=url,
        datum=datum,
        gerelateerde=gerelateerde,
        body=body,
        journaalposten=parser.journaalposten,
    )
    return adv, html


def _build_provenance(html: str, url: str) -> Provenance:
    """Bouw een nieuw provenance-blok voor een (re-)scrape via deze pipeline.

    De input is de URL met sha256 over de gefetched HTML — zo kan stale-detectie
    later inhoud-veranderingen op de CBN-pagina oppikken.

    Trust wordt geforceerd op `unreviewed` na een ETL-update (volgt ADR-004
    §"Verband met stale": bestaande trust-confirmatie vervalt bij re-scrape).
    """
    sha = hashlib.sha256(html.encode("utf-8", errors="replace")).hexdigest()
    return Provenance(
        inputs=[Input(id=url, sha256=sha, version=None)],
        tooling=Tooling(
            pipeline=PIPELINE_REL,
            pipeline_version=git_short_sha(Path(PIPELINE_REL), repo_root=ROOT),
            model=None,
            prompt_version=None,
        ),
        generated_at=now_iso(),
        stale=False,
        stale_reason=None,
        trust=Trust(
            status="unreviewed",
            qa_version=None,
            confirmed_at=now_iso(),
            confirmed_by="default",
            rationale="reset na ETL-update via scrape_cbn_advies.py",
        ),
    )


def _gerelateerde_to_yaml_list(gerelateerde: list[GerelateerdAdvies]) -> list[dict]:
    """Convert naar YAML-vriendelijke lijst (volgorde behouden)."""
    out = []
    for r in gerelateerde:
        item = {"titel": r.titel, "url": r.url}
        if r.datum:
            item["datum"] = r.datum
        out.append(item)
    return out


def _read_existing_frontmatter(path: Path) -> tuple[dict, str]:
    """Lees bestaand .md → (frontmatter dict, body). Lege dict als geen frontmatter."""
    if not path.exists():
        return {}, ""
    text = path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    yaml = _yaml()
    data = yaml.load(m.group(1)) or {}
    return data, text[m.end():]


def render_full_markdown(
    adv: ScrapedAdvice,
    raw_html: str,
    *,
    existing_frontmatter: dict | None = None,
) -> str:
    """Render een complete .md met frontmatter + H1 + body.

    Bij `existing_frontmatter` wordt deze als basis genomen — bestaande
    velden (themas, nummer, etc.) blijven intact. We updaten/voegen toe:
      - bron, datum (als ontbreekt)
      - gerelateerde_adviezen (nieuw of vervangen)
      - provenance (volledig vervangen door _build_provenance)
    """
    fm = dict(existing_frontmatter or {})

    # Behoud-of-vul velden
    fm.setdefault("nummer", _nummer_from_title(adv.titel) or "")
    fm.setdefault("datum", adv.datum or "")
    fm.setdefault("themas", [])
    fm["bron"] = adv.url

    # Gerelateerde adviezen — altijd vervangen (nieuwste scrape is leidend)
    if adv.gerelateerde:
        fm["gerelateerde_adviezen"] = _gerelateerde_to_yaml_list(adv.gerelateerde)
    elif "gerelateerde_adviezen" in fm:
        del fm["gerelateerde_adviezen"]

    # Provenance vervangen
    prov = _build_provenance(raw_html, adv.url)
    fm["provenance"] = prov.to_dict()

    yaml = _yaml()
    buf = io.StringIO()
    yaml.dump(fm, buf)
    fm_text = buf.getvalue()

    return f"---\n{fm_text}---\n\n# {adv.titel}\n\n{adv.body}"


def _nummer_from_title(titel: str) -> str | None:
    """Extract 'CBN-advies NNNN/NN' uit een H1-titel."""
    m = re.match(r'^\s*(CBN-advies\s+\S+?)\s*[–\-—]', titel)
    if m:
        return m.group(1).strip()
    return None


# ─── CLI ────────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description='Scrape CBN-advies pagina naar Markdown.')
    p.add_argument('--url', help='URL van het advies (voor nieuwe scrape)')
    p.add_argument('--out', help='Schrijf output naar dit bestand (default bij --refresh: <path>.v2)')
    p.add_argument('--refresh', help='Pad naar bestaand .md — herlaad vanaf zijn bron-URL en behoud frontmatter-velden (themas, nummer, ...)')
    p.add_argument('--apply', action='store_true', help='Bij --refresh: overschrijf het bron-bestand zelf (default: schrijf naar <path>.v2)')
    args = p.parse_args()

    existing_fm: dict = {}
    refresh_path: Path | None = None

    if args.refresh:
        refresh_path = Path(args.refresh)
        if not refresh_path.exists():
            print(f"Niet gevonden: {refresh_path}", file=sys.stderr)
            sys.exit(1)
        existing_fm, _ = _read_existing_frontmatter(refresh_path)
        # URL afleiden uit bestaande frontmatter
        if "bron" in existing_fm and existing_fm["bron"]:
            args.url = str(existing_fm["bron"])
        else:
            print(f"Geen 'bron:' URL in {refresh_path}", file=sys.stderr)
            sys.exit(1)
        if not args.out:
            args.out = str(refresh_path) if args.apply else str(refresh_path) + '.v2'

    if not args.url:
        p.error('Geef --url of --refresh')

    adv, raw_html = scrape(args.url)
    md = render_full_markdown(adv, raw_html, existing_frontmatter=existing_fm)

    if args.out:
        Path(args.out).write_text(md, encoding='utf-8')
        print(f"Geschreven naar {args.out}", file=sys.stderr)
        print(f"  Titel: {adv.titel}", file=sys.stderr)
        print(f"  Datum: {adv.datum}", file=sys.stderr)
        print(f"  Gerelateerde adviezen: {len(adv.gerelateerde)}", file=sys.stderr)
        print(f"  Journaalposten: {len(adv.journaalposten)}", file=sys.stderr)
        print(f"  Body lengte: {len(adv.body)} chars", file=sys.stderr)
        if existing_fm:
            preserved = sorted(k for k in existing_fm if k not in {"bron", "provenance", "gerelateerde_adviezen"})
            print(f"  Behouden frontmatter-velden: {preserved}", file=sys.stderr)
    else:
        print(md)


if __name__ == '__main__':
    main()
