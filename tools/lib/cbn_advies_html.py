"""
CBN-advies HTML → Markdown library.

Verhuist uit ``tools/etl/scrape_cbn_advies.py`` (HTMLParser-subclass + helpers
+ regex-constanten). Geen filesystem-IO, geen frontmatter-bouw, geen CLI.

Publieke API:

    scrape_advies(url) -> dict          # URL → fetch → parse_html
    parse_html(html)   -> dict          # HTML → titel/body/footnotes/attachments
    select_title(text) -> str           # strip COMMISSIE-prefix + Advies-suffix
    render_markdown(parse_result) -> str  # parse-dict → markdown body

De ``parse_html``-dict bevat:

    {
        "title":       str,
        "body":        str,         # markdown body (geen frontmatter, geen H1)
        "footnotes":   list[dict],  # [{"number": str, "text": str}, ...]
        "attachments": list[dict],  # gerelateerde adviezen
                                    #   [{"titel": ..., "url": ..., "datum": ...}, ...]
        "raw_html":    str,         # ruwe HTML (voor sha256/provenance)
    }
"""
from __future__ import annotations

import re
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from html.parser import HTMLParser


# ─── Datatypes (intern) ──────────────────────────────────────────────────────

@dataclass
class _JournaalpostRij:
    """Eén regel uit een boekhoudkundige journaalpost."""
    dc_marker: str = ""        # "" voor eerste debet-regel, "aan" voor credit
    rekening: str = ""
    omschrijving: str = ""
    debet: str = ""
    credit: str = ""


@dataclass
class _Journaalpost:
    titel: str = "Boeking"
    rijen: list[_JournaalpostRij] = field(default_factory=list)


@dataclass
class _GerelateerdAdvies:
    titel: str
    url: str
    datum: str = ""


# ─── HTML → Markdown parser (intern) ────────────────────────────────────────

class _CBNAdviceParser(HTMLParser):
    """Parser voor CBN-advies pagina's met behoud van semantiek."""

    BLOCK_TAGS = frozenset(['script', 'style', 'noscript'])

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.result: list[str] = []
        self.list_stack: list[tuple[str, int]] = []
        self.skip_stack: list[str] = []
        self._pending_nl = 0

        # Voetnoten
        self.footnote_refs: list[tuple[str, str]] = []
        self.footnote_defs: dict[str, list[str]] = {}
        self._current_footnote_def: str | None = None

        # Journaalposten
        self.journaalposten: list[_Journaalpost] = []
        self._jp_current: _Journaalpost | None = None
        self._jp_current_row: list[str] | None = None
        self._jp_current_cell: list[str] | None = None
        self._jp_current_cell_colspan: int = 1

        self._in_indented_p: bool = False
        self._pending_link_href: str | None = None
        # Index in self.result waar de huidige <p> begint — voor
        # post-detect-fix waarbij we een bold-only <p> achteraf promoveren
        # naar een ## heading.
        self._p_start_idx: int | None = None
        # Tabel-context: gebruikt om <br> binnen td/th als spatie te behandelen
        # (visuele wrap, geen semantische break) en om whitespace-only data
        # tussen </td> en <td> te negeren.
        self._in_table_cell: bool = False
        self._in_table_row: bool = False

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
        if self._jp_current_cell is not None:
            self._jp_current_cell.append(s)
        else:
            self.result.append(s)

    # ── tag handlers ─────────────────────────────────────────────────────────

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)

        if tag in self.BLOCK_TAGS:
            self.skip_stack.append(tag)
            return
        if self._skipping():
            return

        cls = attr_dict.get('class', '')

        # ─── TOC-div skip: <div class="toc..."> / <form class="toc..."> ────
        # CBN-adviezen renderen de inhoudstafel in een <div class="toc toc-
        # responsive"> + een <form class="toc-mobile"> + bevatten een
        # <ol class="toc-level-root">. Block-level skip houdt nested
        # children automatisch buiten de body-output. De skip_stack-logica
        # in handle_endtag haalt de markering weer op bij sluit-tag.
        if tag in ('div', 'form', 'ol', 'ul') and ('toc' in cls.lower()):
            self.skip_stack.append(tag)
            return

        if tag == 'a' and 'see-footnote' in cls:
            href = attr_dict.get('href', '')
            title = attr_dict.get('title', '')
            m = re.search(r'#footnote(\d+)_', href)
            if m:
                num = m.group(1)
                self.footnote_refs.append((num, title))
                self._flush(f'[^{num}]')
                self.skip_stack.append(tag)
                return

        if tag == 'li' and 'footnote' in cls:
            fn_id = attr_dict.get('id', '')
            m = re.search(r'footnote(\d+)_', fn_id)
            if m:
                self._current_footnote_def = m.group(1)
                self.footnote_defs[m.group(1)] = []
                return

        if tag == 'a' and 'footnote-label' in cls:
            self.skip_stack.append(tag)
            return

        if tag == 'table' and ('table-no-padding' in cls or 'booking-table-top' in cls):
            self._jp_current = _Journaalpost()
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
            return

        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            level = int(tag[1])
            self._ensure_nl(2)
            self._flush('#' * level + ' ')

        elif tag == 'p':
            if 'indented' in cls:
                self._in_indented_p = True
                self._ensure_nl(2)
                self._flush('### ')
            else:
                self._ensure_nl(2)
                # Markeer paragraph-start zodat we bij </p> kunnen
                # detecteren of de content bold-only is (→ heading).
                # _flush eerst zodat \n's al in result zitten, dan
                # nemen we positie nadien op.
                self._flush('')  # forceer pending_nl-flush
                self._p_start_idx = len(self.result)

        elif tag in ('strong', 'b'):
            if not self._in_indented_p:
                self._flush('**')

        elif tag in ('em', 'i'):
            self._flush('*')

        elif tag == 'br':
            if self._in_table_cell:
                self._flush(' ')  # visuele wrap in cell, geen semantische break
            else:
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

        elif tag == 'a':
            href = attr_dict.get('href', '')
            if href and not href.startswith('#') and '/adviezen/' not in href:
                if href.startswith('/'):
                    href = f'https://www.cbn-cnc.be{href}'
                self._pending_link_href = href
                self._flush('[')

        elif tag == 'table':
            self._ensure_nl(2)

        elif tag == 'tr':
            if self._pending_nl == 0 and self.result:
                self.result.append('\n')
            self._in_table_row = True

        elif tag in ('th', 'td'):
            self._in_table_cell = True
            self._flush('| ')

    def handle_endtag(self, tag):
        if tag in self.BLOCK_TAGS:
            if self.skip_stack and self.skip_stack[-1] == tag:
                self.skip_stack.pop()
            return

        if self.skip_stack and self.skip_stack[-1] == tag:
            self.skip_stack.pop()
            return
        if self._skipping():
            return

        if tag == 'li' and self._current_footnote_def is not None:
            self._current_footnote_def = None
            return

        if self._jp_current is not None:
            if tag in ('td', 'th'):
                cell_text = ''.join(self._jp_current_cell or []).strip()
                if self._jp_current_row is not None:
                    self._jp_current_row.append(cell_text)
                    for _ in range(self._jp_current_cell_colspan - 1):
                        self._jp_current_row.append('')
                self._jp_current_cell = None
                self._jp_current_cell_colspan = 1
                return
            if tag == 'tr':
                if self._jp_current_row:
                    rij = self._build_jp_rij(self._jp_current_row)
                    if rij:
                        self._jp_current.rijen.append(rij)
                self._jp_current_row = None
                return
            if tag == 'table':
                self._render_journaalpost(self._jp_current)
                self.journaalposten.append(self._jp_current)
                self._jp_current = None
                return
            return

        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self._ensure_nl(2)
        elif tag == 'p':
            self._in_indented_p = False
            # Bold-only detection: als de hele inhoud van deze <p>
            # bestaat uit een enkele **...** span (met ev. trailing
            # whitespace), is dit een sectie-heading die de CBN-redacteur
            # in plaats van <h2> als bold-tekst heeft opgemaakt. Promoot
            # naar ## heading (max 150 chars titel).
            if self._p_start_idx is not None:
                end = len(self.result)
                p_content = ''.join(self.result[self._p_start_idx:end]).strip()
                m = re.fullmatch(
                    r'\*\*([^*\n]{2,150}?)\*\*\s*[\.\,\:]?\s*',
                    p_content,
                )
                if m:
                    title = m.group(1).strip()
                    # Strip footnote-marker uit titel (verstoort heading)
                    title = re.sub(r'\s*\[\^\d+\]\s*', '', title).strip()
                    if title and not title.endswith(('.', ';', ':')):
                        # Vervang de p-content door een H2-heading.
                        del self.result[self._p_start_idx:end]
                        self.result.append(f'## {title}')
                self._p_start_idx = None
            self._ensure_nl(2)
        elif tag in ('strong', 'b'):
            if not self._in_indented_p:
                self._flush('**')
        elif tag == 'a':
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
            # Geen close-pipe per cel: de closing-pipe wordt aan </tr> emit.
            # Per-cel `' |'` levert dubbele pipes op tussen cellen (`| A || B |`).
            self._in_table_cell = False
        elif tag == 'tr':
            # Closing pipe van de rij (eenmaal, niet per cel).
            self._flush('|')
            self._in_table_row = False
        elif tag == 'table':
            self._ensure_nl(2)

    def handle_data(self, data):
        if self._skipping():
            return

        if self._current_footnote_def is not None:
            self.footnote_defs[self._current_footnote_def].append(data)
            return

        if self._jp_current_cell is not None:
            self._jp_current_cell.append(data)
            return
        if self._jp_current is not None:
            return

        text = data

        # Tabel-context: tussen </td> en <td> binnen tr is whitespace-only
        # data (HTML-indentatie). Die mag geen extra pipes/spaces injecteren.
        if self._in_table_row and not self._in_table_cell and not text.strip():
            return

        # Binnen een td/th: collapse newlines/tabs naar spaties (geen
        # semantische breaks in cell-content; markdown-tabel-rij moet op
        # één regel staan).
        if self._in_table_cell:
            text = re.sub(r"[\n\t]+", " ", text)
            text = re.sub(r"  +", " ", text)

        if text.strip():
            self._flush(text)
        elif self.result and not self.result[-1].endswith('\n'):
            self._flush(' ')

    # ── Journaalpost rendering ──────────────────────────────────────────────

    @staticmethod
    def _build_jp_rij(raw_cells: list[str]) -> _JournaalpostRij | None:
        cells = [c.strip() for c in raw_cells]
        if not any(cells):
            return None

        aan_idx = None
        for i, c in enumerate(cells):
            if c.lower() == 'aan':
                aan_idx = i
                break

        rij = _JournaalpostRij()

        if aan_idx is not None:
            rij.dc_marker = "aan"
            if aan_idx + 1 < len(cells):
                rij.rekening = cells[aan_idx + 1]
            if aan_idx + 2 < len(cells):
                rij.omschrijving = cells[aan_idx + 2]
            tail = [c for c in cells[aan_idx + 3:] if c]
            if len(tail) >= 1:
                rij.credit = tail[-1] if len(tail) == 1 else (tail[-1] or tail[-2])
            if len(tail) >= 2:
                rij.debet = tail[-2]
        else:
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

    def _render_journaalpost(self, jp: _Journaalpost):
        self._ensure_nl(2)
        self._flush('| | Rekening | Omschrijving | Debet | Credit |\n')
        self._flush('|---|----------|--------------|-------|--------|\n')
        for r in jp.rijen:
            line = f'| {r.dc_marker} | {r.rekening} | {r.omschrijving} | {r.debet} | {r.credit} |'
            self._flush(line + '\n')
        self._ensure_nl(2)

    def get_markdown(self) -> str:
        return ''.join(self.result)


# ─── HTML extractie helpers ───────────────────────────────────────────────────

def _extract_advice_content(html: str) -> str:
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


def _normalize_unicode_title(text: str) -> str:
    """Vervang Unicode-hyphens / soft-hyphens in een titel-string door ASCII.

    Wordt gebruikt door `select_title` en `_select_title_html`. De body
    krijgt deze normalisatie via `_cleanup_markdown`, maar de title gaat
    apart door de orchestrator naar de H1 — zonder deze pas zou U+2010
    in titels overleven.
    """
    if not text:
        return text
    return (text
            .replace('‐', '-')   # U+2010 HYPHEN
            .replace('¬', '-')   # U+00AC NOT SIGN (pseudo-soft-hyphen)
            .replace(' ', ' ')   # U+00A0 NBSP → ASCII space
            .replace('ĳ', 'ij')
            .replace('Ĳ', 'IJ')
            .replace('&amp;quot;', '"')
            .replace('&amp;#039;', "'")
            .replace('&amp;amp;', '&')
            .replace('&amp;', '&'))


def select_title(text: str) -> str:
    """Strip 'COMMISSIE VOOR ... NORMEN' prefix en 'Advies van DD ...' suffix.

    Werkt op een platte tekst (bv. een H1-string die in oudere CBN-pagina's
    de org-naam, de titel en de datum samenpropt op één regel).
    """
    if text is None:
        return ""
    cleaned = _normalize_unicode_title(text)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    # Strip "COMMISSIE VOOR ... NORMEN" of "COMMISSION DES NORMES ..." prefix
    cleaned = re.sub(
        r'^(?:COMMISSIE\s+VOOR\b.*?NORMEN|COMMISSION\s+DES\s+NORMES[^\n]*?)\s+',
        '', cleaned, flags=re.IGNORECASE
    )
    # Strip "Advies van DATUM" of "Avis du DATUM" suffix
    cleaned = re.sub(
        r'\s+(?:Advies|Avis)\s+(?:van|du)\s+\d.*$', '', cleaned, flags=re.IGNORECASE
    )
    return cleaned.strip()


def _select_title_html(html: str) -> str | None:
    """Robuuste titelselectie uit een volledige HTML-pagina (interne helper).

    Sommige oudere CBN-pagina's combineren org-naam + titel in één <h1>:
      "COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN CBN-advies 106/4 - Titel ..."
    In dat geval strippen we via ``select_title`` de prefix/suffix en houden
    enkel de eigenlijke titel.
    """
    candidates = []
    for m in re.finditer(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = re.sub(r'\s+', ' ', text)
        if not text:
            continue
        if 'COMMISSIE' in text.upper() or 'COMMISSION DES' in text.upper():
            cleaned = select_title(text)
            if cleaned and len(cleaned) > 5 and not re.match(
                r'^(?:Advies|Avis)\s+(?:van|du)\s+\d', cleaned, re.IGNORECASE
            ):
                candidates.append(cleaned)
            continue
        if re.match(r'^Advies van\s+\d', text, re.IGNORECASE):
            continue
        if re.match(r'^Avis du\s+\d', text, re.IGNORECASE):
            continue
        candidates.append(text)
    if not candidates:
        return None
    return _normalize_unicode_title(max(candidates, key=len))


def _extract_gerelateerde_adviezen(html: str) -> list[_GerelateerdAdvies]:
    """Extraheer 'Gerelateerde adviezen' blok als gestructureerde lijst."""
    refs: list[_GerelateerdAdvies] = []
    m = re.search(r'<h2[^>]*>Gerelateerde adviezen</h2>(.*?)(?=<aside|<footer|</main|</article)',
                  html, re.DOTALL | re.IGNORECASE)
    if not m:
        return refs
    block = m.group(1)
    for row_m in re.finditer(
        r'<div[^>]+class="views-row"[^>]*>(.*?)(?=<div[^>]+class="views-row"|</div\s*>\s*</div\s*>\s*</div)',
        block, re.DOTALL,
    ):
        row_html = row_m.group(1)
        date_m = re.search(r'datetime="([^"]+)"', row_html)
        datum = date_m.group(1)[:10] if date_m else ""
        link_m = re.search(r'<a[^>]+href="(/nl/adviezen/[^"]+)"[^>]*>([^<]+)</a>', row_html)
        if link_m:
            href = link_m.group(1)
            titel = _normalize_unicode_title(link_m.group(2).strip())
            url = f"https://www.cbn-cnc.be{href}"
            refs.append(_GerelateerdAdvies(titel=titel, url=url, datum=datum))
    return refs


def _extract_advice_date(html: str) -> str | None:
    """Extract advies-datum uit 'Advies van DATUM' H1 of <time> tag."""
    for m in re.finditer(r'<h1[^>]*>(?:Advies van|Avis du)\s+([^<]+)</h1>', html, re.IGNORECASE):
        return m.group(1).strip()
    m = re.search(r'<time\s+datetime="(\d{4}-\d{2}-\d{2})', html)
    if m:
        return m.group(1)
    return None


# ─── Markdown post-processing ────────────────────────────────────────────────

_TOC_NUMBERED_LINE = re.compile(r'^\s*\d+\.\s+\S')
_SELECT_DROPDOWN = re.compile(r'^\s*-\s*Select\s*-')

_BODY_NOISE_LINE_PATTERNS = [
    re.compile(r'^[ \t]*#?\s*COMMISSIE\s+VOOR\b.*NORMEN\s*$', re.IGNORECASE),
    re.compile(r'^[ \t]*#?\s*COMMISSION\s+DES\s+NORMES\b.*$', re.IGNORECASE),
    re.compile(r'^[ \t]*#?\s*Advies\s+van\s+\d.*$', re.IGNORECASE),
    re.compile(r'^[ \t]*#?\s*Avis\s+du\s+\d.*$', re.IGNORECASE),
    re.compile(r'^[ \t]*#\s+CBN-advies\s.*$', re.IGNORECASE),
    re.compile(r'^[ \t]*#\s+Avis\s+CNC\s.*$', re.IGNORECASE),
    re.compile(r'^[ \t]*#[ \t]*[\xa0\s]*$'),
    # TOC-blob met `--`-separators: `-- Item -- Item -- Item ...` of
    # `1. Item -- 2. Item -- 3. Item ...`. Geen whitespace-vereiste
    # tussen item-einde en volgende `--` (dekt zowel `Item -- Item`
    # als `Item-- Item` varianten).
    re.compile(r'^\s*-{2,}\s+\S.+?-{2,}\s+\S.+?-{2,}\s+\S'),
    # Hetzelfde patroon maar beginnend met content i.p.v. `--`:
    # `Item-- Item-- Item ...` of `Item -- Item -- Item ...`.
    re.compile(r'^\s*\S.+?-{2,}\s+\S.+?-{2,}\s+\S.+?-{2,}\s+\S'),
    # TOC-fragment dat met `. ----` of `, ----` begint (continuation
    # van vorige TOC-regel met dotted-leader-restant).
    re.compile(r'^\s*[\.\,]\s*-{2,}\s+\S'),
]


def _is_body_noise(line: str) -> bool:
    return any(p.match(line) for p in _BODY_NOISE_LINE_PATTERNS)


def _strip_body_noise(md: str) -> str:
    out = []
    for line in md.split('\n'):
        if _is_body_noise(line):
            continue
        out.append(line)
    return '\n'.join(out)


def _strip_toc_block(md: str) -> str:
    lines = md.split('\n')
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if _SELECT_DROPDOWN.match(line):
            i += 1
            continue
        result.append(line)
        i += 1

    md = '\n'.join(result)

    hh = re.search(r'^##\s+', md, re.MULTILINE)
    if not hh:
        return md
    head_pos = hh.start()
    head_section = md[:head_pos]
    rest = md[head_pos:]

    head_lines = head_section.split('\n')

    # Strategie: tel alle TOC-numbered-lines in de head-sectie. Als er ≥3
    # van zijn (sterke indicatie dat de hele head een TOC is), strip ALLE
    # numbered-lines + de blank-regels eromheen, ook als er niet-TOC-tekst
    # tussen zit (bv. een gedupliceerde titel-fragment of `CBN-advies XX/Y`-
    # repeat). Dit voorkomt dat een enkele niet-TOC-regel het break uit de
    # walking-loop triggert en TOC-items niet meer gestript worden.
    num_count = sum(1 for ln in head_lines if _TOC_NUMBERED_LINE.match(ln))
    if num_count >= 3:
        kept = []
        for ln in head_lines:
            if _TOC_NUMBERED_LINE.match(ln):
                continue
            # Strip ook: "CBN-advies X/Y The Title"-style repeat-lines
            # (titel-fragmenten die de scraper soms duplicate boven de body)
            # en losse `---- Item`-regels (TOC-continuation met 4+ dashes).
            stripped = ln.strip()
            if (stripped.startswith(('CBN-advies', 'Avis CNC'))
                    and not stripped.startswith('# ')):
                continue
            # `---- text` als enkele regel — TOC-continuation
            if re.match(r'^-{2,}\s+\S', stripped):
                continue
            kept.append(ln)
        head_section = '\n'.join(kept).rstrip() + '\n\n'
        return head_section + rest

    # Oude fallback voor kleinere TOCs: walk backwards en strip de
    # contigue numbered/blank-block direct vóór de eerste `##`.
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

    if drop_count > 2:
        head_lines = head_lines[:len(head_lines) - drop_count]
        head_section = '\n'.join(head_lines).rstrip() + '\n\n'
        return head_section + rest

    return md


def _append_footnotes(md: str, footnote_defs: dict[str, list[str]],
                      footnote_refs: list[tuple[str, str]]) -> str:
    if not footnote_defs and not footnote_refs:
        return md

    seen = set()
    blocks = []

    for num, parts in footnote_defs.items():
        text = ''.join(parts).strip()
        text = re.sub(r'\s+', ' ', text)
        if text:
            blocks.append(f'[^{num}]: {text}')
            seen.add(num)

    for num, title in footnote_refs:
        if num in seen:
            continue
        title = re.sub(r'\s+', ' ', title.strip())
        if title:
            blocks.append(f'[^{num}]: {title}')
            seen.add(num)

    if not blocks:
        return md

    blocks.sort(key=lambda b: int(re.match(r'\[\^(\d+)\]', b).group(1)))
    return md.rstrip() + '\n\n' + '\n\n'.join(blocks) + '\n'


_IMPLICIT_HEADING_PATTERNS = [
    re.compile(r'^\s*\*\s*(Voorbeeld\s+\d+[^*\n]*?)\s*\*\s*$'),
    re.compile(r'^\s*\*\s*(Casus\s+\d+[^*\n]*?|Geval\s+\d+[^*\n]*?)\s*\*\s*$'),
    re.compile(
        r'^\s*\*\*\s*(Inleiding|Algemeen|Conclusie|Onderwerp van het advies|'
        r'Toepassingsgebied|Boekhoudkundige verwerking|Voorbeelden?|Samenvatting|Besluit)\s*\*\*\s*$',
        re.IGNORECASE,
    ),
    re.compile(r'^\s*\*\*(\d+(?:\.\d+)*\.?\s+[^\*\n]{4,80}?)\*\*\s*$'),
    # B4-SP2: bold boeking-labels zijn subsectie-headings in CBN-adviezen.
    # De 20-char drempel van _BOLD_TITLE_STANDALONE dekt "Boeking eerste jaar"
    # (19 chars) niet — vang expliciete Boeking-patronen hier op.
    re.compile(r'^\s*\*\*(Boeking\s+[^\*\n]{3,}?)\*\*\s*$', re.IGNORECASE),
]

_BOLD_TITLE_STANDALONE = re.compile(r'^\s*\*\*([^\*\n]{20,}?)\*\*\s*$')
# Italic-equivalent: enkele asterisks rond een lange tekst (≥20 chars) op een
# eigen regel. Toegevoegd 2026-05-13 voor B5-patroon in CBN-Q&A-adviezen waar
# vragen-titels als italic-standalone staan i.p.v. heading.
_ITALIC_TITLE_STANDALONE = re.compile(r'^\s*\*([^\*\n]{20,}?)\*\s*$')


def _promote_implicit_headings(md: str) -> str:
    lines = md.split('\n')
    out_lines = []
    for i, line in enumerate(lines):
        replaced = False

        for pat in _IMPLICIT_HEADING_PATTERNS:
            m = pat.match(line)
            if m:
                title = m.group(1).strip()
                out_lines.append(f'## {title}')
                replaced = True
                break

        if not replaced:
            m = _BOLD_TITLE_STANDALONE.match(line)
            if m:
                prev_blank = (i == 0 or not lines[i - 1].strip())
                next_blank = (i >= len(lines) - 1 or not lines[i + 1].strip())
                if prev_blank and next_blank:
                    title = m.group(1).strip()
                    if not re.search(r'[\.\?\!]$', title):
                        out_lines.append(f'## {title}')
                        replaced = True

        if not replaced:
            m = _ITALIC_TITLE_STANDALONE.match(line)
            if m:
                prev_blank = (i == 0 or not lines[i - 1].strip())
                next_blank = (i >= len(lines) - 1 or not lines[i + 1].strip())
                if prev_blank and next_blank:
                    title = m.group(1).strip()
                    if not re.search(r'[\.\?\!]$', title):
                        out_lines.append(f'## {title}')
                        replaced = True

        if not replaced:
            out_lines.append(line)
    return '\n'.join(out_lines)


def _normalize_tables(md: str) -> str:
    """Repareer markdown-tabel-issues (E1/E2).

    - Inject `|---|---|` separator-rij na de header-rij als die ontbreekt.
    - Multi-line cellen: join cel-inhoud die over meerdere regels loopt
      (zonder pipe op de volgende regel) terug op één regel.

    Voorbeeld input:
        | Header A | Header B |
        | A1 | B1 |
        | A2 | B2 |
    Output:
        | Header A | Header B |
        |---|---|
        | A1 | B1 |
        | A2 | B2 |
    """
    lines = md.split('\n')
    out: list[str] = []
    i = 0

    def is_table_row(line: str) -> bool:
        s = line.strip()
        return s.startswith('|') and s.endswith('|') and s.count('|') >= 2

    def is_separator(line: str) -> bool:
        s = line.strip()
        if not (s.startswith('|') and s.endswith('|')):
            return False
        # Tussen pipes moet alleen dashes/spaties/colons staan.
        cells = s.strip('|').split('|')
        return all(re.fullmatch(r'\s*:?-+:?\s*', c) for c in cells)

    def col_count(line: str) -> int:
        # Aantal kolommen = aantal pipes - 1 in de stripped row
        s = line.strip().strip('|')
        return s.count('|') + 1

    while i < len(lines):
        line = lines[i]
        if is_table_row(line):
            # Verzamel alle opeenvolgende tabel-rijen
            table_start = i
            # Eerst: join multi-line cell-content. Een tabel-rij eindigt
            # op `|`; als de volgende regel NIET met `|` begint maar wel
            # tekst bevat, en de regel daarna een tabel-rij is, dan was
            # die niet-pipe-regel waarschijnlijk een vervolg van een
            # cel-inhoud die over een newline brak.
            rows = []
            while i < len(lines):
                if is_table_row(lines[i]):
                    rows.append(lines[i])
                    i += 1
                elif (lines[i].strip()
                      and i + 1 < len(lines)
                      and is_table_row(lines[i + 1])
                      and rows):
                    # Multi-line cel: append aan laatste rij vóór sluit-`|`.
                    cont = lines[i].strip()
                    # Strip laatste `|`, voeg continuation toe, voeg `|` terug.
                    last = rows[-1].rstrip()
                    if last.endswith('|'):
                        rows[-1] = last[:-1].rstrip() + ' ' + cont + ' |'
                    else:
                        rows[-1] = last + ' ' + cont
                    i += 1
                else:
                    break

            # Check separator: tweede rij moet separator zijn.
            if len(rows) >= 2 and not is_separator(rows[1]):
                cols = col_count(rows[0])
                sep = '|' + '|'.join(['---'] * cols) + '|'
                rows.insert(1, sep)
            elif len(rows) == 1:
                # Single-row table: voeg dummy separator toe.
                cols = col_count(rows[0])
                sep = '|' + '|'.join(['---'] * cols) + '|'
                rows.append(sep)

            out.extend(rows)
        else:
            out.append(line)
            i += 1
    return '\n'.join(out)


def _normalize_heading_hierarchy(md: str) -> str:
    """Normaliseer heading-hiërarchie (B2/B3 fixes).

    - Demote: een heading mag niet meer dan 1 niveau hoger zijn dan de vorige
      (`#` → `####` zonder `##`/`###` ertussen wordt `#` → `##`).
    - Strip lege headings: `## `, `## *`, `## **` zonder tekst.
    - Strip bold/italic-markering ROND een heading-tekst (`## **Title**` → `## Title`).
      Niet als bold/italic enkel een DEEL van de heading is (`## Een **deel** bold`).
    - Extra H1's na de eerste worden gedemoteerd naar H2: een mens-geschreven
      document heeft slechts één H1 aan het begin.

    De CBN-orchestrator (cbn_advies.py) prepend een `# Title` H1 AAN de body
    NA deze normalisatie. Daarom initialiseren we met een impliciete H1
    (last_level = 1): elke ## of dieper heading wordt gemeten t.o.v. de
    impliciete title-H1. `### Sub` direct na de body-start wordt dan
    `## Sub` (demoted), wat klopt met de feitelijke hiërarchie.
    """
    # Eerste pass: welke niveaus komen voor in het document?
    # Als `###` bestaat maar `##` niet — schrijver gaf `###` een betekenis,
    # dan demoten we `####` naar `###` (i.p.v. naar `##`). Anders demoten
    # we strikt naar last_level+1.
    levels_present = set()
    for ln in md.split('\n'):
        m = re.match(r'^(#{1,6})\s+\S', ln)
        if m:
            levels_present.add(len(m.group(1)))

    lines = md.split('\n')
    out = []
    last_level = 1  # Impliciete H1 vanuit orchestrator
    seen_h1 = False
    # Original-level → mapped-level cache. Siblings (zelfde original-level)
    # krijgen zo consistent dezelfde mapped-level, ook bij multi-step
    # niveau-skips.
    level_map: dict[int, int] = {}
    for ln in lines:
        m = re.match(r'^(#{1,6})\s+(.+?)\s*$', ln)
        if not m:
            out.append(ln)
            continue
        level = len(m.group(1))
        text = m.group(2).strip()

        # Strip bold/italic-markering die de hele heading-tekst omhult.
        m2 = re.match(r'^\*\*(.+?)\*\*\s*$', text)
        if m2:
            text = m2.group(1).strip()
        else:
            m2 = re.match(r'^\*(.+?)\*\s*$', text)
            if m2:
                text = m2.group(1).strip()

        # Lege heading? Skip.
        if not text or text in ('**', '*', '#'):
            continue

        # H1-deduplicate: alleen de eerste H1 behouden, latere H1's → H2.
        if level == 1:
            if seen_h1:
                level = 2
            else:
                seen_h1 = True

        # Hierarchy-demote: forceer geen-skip (= demote naar last_level+1).
        # Exceptie: als er INTERMEDIAIRE levels elders in het document
        # voorkomen, behoud een dieper level — de schrijver heeft die
        # extra hiërarchie-laag een betekenis gegeven.
        if level in level_map:
            mapped = level_map[level]
            if mapped > last_level + 1:
                mapped = last_level + 1
                level_map[level] = mapped
        else:
            # Default: demote naar last_level+1 (geen skip toegestaan).
            target = last_level + 1
            # Maar als ALLE intermediaire levels (last_level+1 t/m level-1)
            # ELDERS in het document voorkomen, mag het oorspronkelijke
            # level behouden blijven (de schrijver maakt onderscheid).
            intermediates = list(range(last_level + 1, level))
            if intermediates and all(i in levels_present for i in intermediates):
                target = level  # alle tussenlagen bestaan → keep level
            mapped = min(level, target)
            level_map[level] = mapped
        level = mapped

        out.append('#' * level + ' ' + text)
        last_level = level
    return '\n'.join(out)


def _cleanup_markdown(md: str) -> str:
    # ─── 1. Unicode-normalisatie (A4) ────────────────────────────────────────
    # Vervang non-breaking spaces (U+00A0) door gewone spaties.
    md = re.sub(r'\xa0+', ' ', md)
    # U+2010 HYPHEN → ASCII hyphen-minus. CBN-HTML gebruikt soms U+2010
    # i.p.v. U+002D, wat tokenization en search verstoort.
    md = md.replace('‐', '-')
    # U+00AC NOT SIGN (¬) wordt door sommige CBN-pagina's gebruikt als
    # pseudo-soft-hyphen (bv. `VVPR¬aandelen`); normaliseer naar gewone hyphen.
    md = md.replace('¬', '-')
    # U+0133 IJ-ligatuur → "ij" (komt voor in oudere PDF-extractie).
    md = md.replace('ĳ', 'ij').replace('Ĳ', 'IJ')
    # Eventuele dubbele spaties die ontstaan door collapse weer normaliseren,
    # behalve aan begin van regel (markdown indent kan betekenisvol zijn).
    md = re.sub(r'(?<=\S)  +', ' ', md)

    # ─── 2. HTML-entities decoderen (G2) ─────────────────────────────────────
    # convert_charrefs=True in de parser dekt enkelvoudig-gecodeerde entities,
    # maar dubbel-gecodeerde entities (`&amp;quot;`, `&amp;#039;`) komen door
    # in body en frontmatter. Decodeer ze hier post-hoc.
    md = (md
          .replace('&amp;quot;', '"')
          .replace('&amp;#039;', "'")
          .replace('&amp;apos;', "'")
          .replace('&amp;amp;', '&')
          .replace('&amp;lt;', '<')
          .replace('&amp;gt;', '>')
          .replace('&amp;nbsp;', ' ')
          # Standalone `&amp;` (literal "&") als laatste — orde belangrijk.
          .replace('&amp;', '&'))

    # ─── 3. Whitespace normalisatie ──────────────────────────────────────────
    lines = [(l if l.strip() else '') for l in md.split('\n')]
    md = '\n'.join(lines)

    # ─── 4. Footnote-marker line-break-fixes (A6) ────────────────────────────
    # `[^N]\n.` of `[^N]\n,` etc — punctuatie op nieuwe regel: trek terug.
    md = re.sub(r'(\[\^\d+\])\s*\n\s*([\.\,\;\:\)\]])', r'\1\2', md)
    # `[^N]\n<leading-ws><kleinletter>` — zin loopt door, vervang break met spatie.
    md = re.sub(
        r'(\[\^\d+\])[ \t]*\n[ \t]+(?=[a-zéèêëàâîïôûüçñ"“”\(\[])',
        r'\1 ', md
    )
    # `[^N]\n<kleinletter>` — zelfde, zonder leading whitespace.
    md = re.sub(
        r'(\[\^\d+\])\n(?=[a-zéèêëàâîïôûüçñ])',
        r'\1 ', md
    )

    # ─── 4b. PDF-pagina-overgang line-break normalisatie (A6) ────────────────
    # Patroon: zin breekt midden door PDF-pagina-grens binnen één paragraaf.
    # VOORZICHTIG: alleen joinen bij EXACT één newline (geen blank line),
    # gevolgd door non-empty content met kleine letter / leesteken. Behoudt
    # paragraph-breaks (`\n\n`) ongemoeid.
    # "stelt vast dat de\n  voorwaarden niet" → "stelt vast dat de voorwaarden niet"
    md = re.sub(
        r'(\b[a-zéèêëàâîïôûüçñ]{3,})\n[ \t]+(?=[a-zéèêëàâîïôûüçñ])',
        r'\1 ',
        md,
    )
    # Joined woord-met-trailing-hyphen op regelgrens: "be-\nstaande" → "bestaande"
    # (vereist hyphenated lower-case continuation, geen blank line)
    md = re.sub(
        r'(\b[a-zéèêëàâîïôûüçñ]{2,})-\n[ \t]*(?=[a-zéèêëàâîïôûüçñ])',
        r'\1',
        md,
    )

    # ─── 5. Malformed italic/bold (D4) ───────────────────────────────────────
    # `*text *` (spatie voor sluitende `*`) → `*text* ` — verschuif spatie
    # naar buiten zodat italic-span CommonMark-compliant sluit.
    # Content moet starten met non-whitespace (anders matched de regex
    # spuriously over twee aangrenzende italic-spans heen).
    md = re.sub(
        r'\*(\S[^*\n]{0,200}?)([ \t]+)\*(?!\*)',
        lambda m: '*' + m.group(1).rstrip() + '*' + m.group(2),
        md,
    )
    # Idem voor bold `**text **`.
    md = re.sub(
        r'\*\*(\S[^*\n]{0,200}?)([ \t]+)\*\*',
        lambda m: '**' + m.group(1).rstrip() + '**' + m.group(2),
        md,
    )

    # ─── 6. Losse asterisk-regels strippen ───────────────────────────────────
    md = re.sub(r'^\s*\*+(\s*\*+)*\s*$', '', md, flags=re.MULTILINE)

    # ─── 7. Losse `[^N]` op eigen regel als artefact (D3) ────────────────────
    # Een regel die enkel uit footnote-markers bestaat is meestal een floating
    # artefact dat de scraper na een tabel-cel kwijt is geraakt. Verwijder
    # (de definitie blijft onderaan in de footnotes-sectie).
    md = re.sub(r'^\s*(?:\[\^\d+\]\s*){1,3}\s*$', '', md, flags=re.MULTILINE)

    # ─── 8. TOC-blob met `--`-separators op één regel ────────────────────────
    # Patroon (a): `1. Inleiding ------ 2. Toepassing ------ 3. ...` —
    # plain-text concatenatie van een TOC. Geen body-content; strippen.
    md = re.sub(
        r'^\s*\d+\.\s+\S[^\n]{0,80}(?:\s*-{2,}\s*\d+\.\s+\S[^\n]{0,80}){2,}\s*$',
        '', md, flags=re.MULTILINE,
    )
    # Patroon (b): `-- Eerste -- Tweede -- Derde ...` — TOC zonder nummering,
    # met `-- ` als prefix-separator. Vereist ≥3 items zodat we geen normale
    # zin met enkele em-dashes raken.
    md = re.sub(
        r'^\s*-{2,}[ \t]+\S[^\n]{0,80}(?:\s*-{2,}[ \t]+\S[^\n]{0,80}){2,}\s*$',
        '', md, flags=re.MULTILINE,
    )

    # ─── 8b. Demote misclassified `### <full sentence>` (B1/B5) ──────────────
    # De parser zet `<p class="indented">` om naar `### `. Voor korte labels
    # ("Voorbeeld 1", "Casus") is dat correct, maar voor volledige zinnen
    # (typisch >80 chars of eindigend op leesteken) is dat een bug. Demote
    # terug naar plain paragraaf.
    def _demote_sentence_h3(m: re.Match) -> str:
        body = m.group(1).rstrip()
        if len(body) > 80 or re.search(r'[\.\,\;\:\?]$', body):
            return body
        return m.group(0)
    md = re.sub(r'^###\s+(.+?)\s*$', _demote_sentence_h3, md, flags=re.MULTILINE)

    # ─── 8c. Strip footnote-markers uit heading-regels ─────────────────────
    # `## Kleine[^3] vereniging` → `## Kleine vereniging` — voetnoot-markers
    # in headings worden door veel markdown-renderers niet goed weergegeven
    # en verstoren de heading-tekst voor RAG-retrieval. De voetnoot-definitie
    # blijft onderaan staan (alleen de inline-ref wordt gestript).
    def _strip_footnote_from_heading(m: re.Match) -> str:
        prefix = m.group(1)
        text = m.group(2)
        cleaned = re.sub(r'\[\^\d+\]', '', text)
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        return f'{prefix} {cleaned}'
    md = re.sub(
        r'^(#{1,6})\s+(.+?)\s*$',
        _strip_footnote_from_heading,
        md,
        flags=re.MULTILINE,
    )

    # ─── 9. Duplicate top-level H1 wegwerken (B3) ────────────────────────────
    # Als er twee opeenvolgende `# Title`-regels staan met identieke tekst,
    # houd de eerste.
    lines = md.split('\n')
    out = []
    last_h1 = None
    for ln in lines:
        m = re.match(r'^#\s+(.+?)\s*$', ln)
        if m and last_h1 is not None and m.group(1).strip() == last_h1:
            continue  # skip duplicate
        out.append(ln)
        if m:
            last_h1 = m.group(1).strip()
        elif ln.strip():
            last_h1 = None  # reset tussen niet-blanke regels
    md = '\n'.join(out)

    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip() + '\n'


# ─── Fetch ──────────────────────────────────────────────────────────────────

def _fetch_html(url: str) -> tuple[int, str]:
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


# ─── Publieke API ───────────────────────────────────────────────────────────

def parse_html(html: str) -> dict:
    """Parse een CBN-advies HTML-string naar een gestructureerde dict.

    De ``body`` is een markdown-string (geen frontmatter, geen H1-regel).
    De H1 met de advies-titel wordt apart in ``title`` teruggegeven.

    Returns:
        {
            "title":       str,
            "body":        str,
            "footnotes":   list[dict],   # [{"number": "1", "text": "..."}, ...]
            "attachments": list[dict],   # gerelateerde adviezen
            "raw_html":    str,
        }
    """
    title = _select_title_html(html) or ""
    datum = _extract_advice_date(html) or ""
    gerelateerde = _extract_gerelateerde_adviezen(html)

    content_html = _extract_advice_content(html)
    parser = _CBNAdviceParser()
    parser.feed(content_html)
    raw_md = parser.get_markdown()

    raw_md = _strip_body_noise(raw_md)
    body = _strip_toc_block(raw_md)
    body = _promote_implicit_headings(body)
    body = _normalize_heading_hierarchy(body)
    body = _normalize_tables(body)
    body = _append_footnotes(body, parser.footnote_defs, parser.footnote_refs)
    body = _cleanup_markdown(body)

    # Footnotes als gestructureerde lijst (op nummer, oplopend)
    footnotes: list[dict] = []
    seen: set[str] = set()
    for num, parts in parser.footnote_defs.items():
        text = re.sub(r'\s+', ' ', ''.join(parts).strip())
        if text:
            footnotes.append({"number": num, "text": text})
            seen.add(num)
    for num, ftitle in parser.footnote_refs:
        if num in seen:
            continue
        text = re.sub(r'\s+', ' ', ftitle.strip())
        if text:
            footnotes.append({"number": num, "text": text})
            seen.add(num)
    try:
        footnotes.sort(key=lambda f: int(f["number"]))
    except (ValueError, KeyError):
        pass

    attachments: list[dict] = []
    for r in gerelateerde:
        item = {"titel": r.titel, "url": r.url}
        if r.datum:
            item["datum"] = r.datum
        attachments.append(item)

    return {
        "title": title,
        "body": body,
        "footnotes": footnotes,
        "attachments": attachments,
        "raw_html": html,
        "datum": datum,
    }


def scrape_advies(url: str) -> dict:
    """URL → fetched HTML → parse_html(html) → result.

    Voegt ``url`` toe aan de result-dict zodat callers de bron meekrijgen.
    Raised RuntimeError bij niet-200 response.
    """
    status, html = _fetch_html(url)
    if status != 200:
        raise RuntimeError(f"HTTP {status} voor {url}")
    result = parse_html(html)
    result["url"] = url
    return result


def render_markdown(parse_result: dict) -> str:
    """parse_result-dict → markdown-body (geen frontmatter).

    Geeft alleen de body terug zoals geproduceerd door ``parse_html``.
    De caller (CLI) kan zelf frontmatter en H1 toevoegen.
    """
    return parse_result.get("body", "")
