#!/usr/bin/env python3
"""
Conversiescript voor Justel HTML-pagina's naar gestructureerde NL markdown.

Ondersteunt:
  - Enkelvoudige Justel ELI-URL  (method: justel_html)
  - Meerdere Justel URLs samenvoegen (params.urls als lijst)
  - Bilingual B.S. PDF-extractie voor KB-documenten zonder Justel HTML
    (method: justel_bs_bilingual)

Heading-niveaus (conform ADR-005 §3 + kwaliteitseisen memory):
  DEEL/BOEK  → ##
  TITEL      → ###
  HOOFDSTUK  → ####
  AFDELING   → #####
  ONDERAFDELING → ######
  Art.       → ## Art. N

Wijzigingsnota's (<W ...>) worden gesepareerd van de artikeltekst.

Gebruik (via convert.py dispatcher):
  python3 tools/etl/convert.py --source Wet-verzekeringen-2014
  python3 tools/etl/convert.py --source KB-voorafgaande-beslissingen-art22-2003
"""

import re
import subprocess
import sys
import textwrap
from pathlib import Path

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from lib.cleanup import fix_broken_words


# ---------------------------------------------------------------------------
# Heading-niveaumapping (Belgische wettekst-hiërarchie → MD-niveau)
# ---------------------------------------------------------------------------

# Vaste Belgische hiërarchie (zie ADR-005 §7):
# DEEL > BOEK > TITEL > HOOFDSTUK > AFDELING > ONDERAFDELING > Art.
# Mapping naar H2–H6; Art. krijgt ## (chunk-grens conform chunk.level=2).
_STRUCT_LEVEL = {
    "DEEL": "##",
    "BOEK": "##",
    "TITEL": "###",
    "HOOFDSTUK": "####",
    "AFDELING": "#####",
    "ONDERAFDELING": "######",
}

_STRUCT_RE = re.compile(
    r"^(DEEL|BOEK|TITEL|HOOFDSTUK|AFDELING|ONDERAFDELING|Afdeling|Onderafdeling|Boek)\b",
    re.IGNORECASE,
)


def _struct_heading(label: str) -> str:
    """Geef het markdown heading-prefix voor een structuurlabel."""
    m = _STRUCT_RE.match(label)
    if not m:
        return "####"
    key = m.group(1).upper()
    return _STRUCT_LEVEL.get(key, "####")


# ---------------------------------------------------------------------------
# Justel HTML parsing
# ---------------------------------------------------------------------------

def fetch_justel(url: str, timeout: int = 60) -> bytes:
    """Haal de Justel HTML-pagina op."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; Certificaid/1.0)"}
    r = requests.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()
    if "Help Eli" in r.text[:500]:
        raise ValueError(f"Justel ELI URL geeft foutpagina: {url}")
    if len(r.content) < 50_000:
        raise ValueError(
            f"Justel pagina te klein ({len(r.content)} bytes) — "
            f"mogelijk JS-only rendering; gebruik een andere URL: {url}"
        )
    return r.content


def _is_structure_anchor(tag: Tag) -> bool:
    """Is dit een structuurlabel-anker (LNK0001, LNK0002, ...)?"""
    name = tag.get("name", "")
    return bool(re.match(r"^LNK\d+$", name))


def _is_article_anchor(tag: Tag) -> bool:
    """Is dit een artikel-anker (Art.N)?"""
    name = tag.get("name", "")
    return bool(re.match(r"^Art\.\d", name))


def _get_article_number_from_href(tag: Tag) -> str:
    """Extraheer artikelnummer uit een link zoals <a href='#LNK0002'>2</a>."""
    return tag.get_text(strip=True).strip()


def parse_justel_html(html_bytes: bytes, language: str = "nl") -> tuple[str, str, str]:
    """
    Parseer Justel HTML-pagina naar (wet_naam, bijgewerkt, body_markdown).

    Structuur van de Justel tekst-sectie (div#list-title-3):
      <a name="LNK0001">DEEL 1.</a> - BESCHRIJVING<br><br>
      <a name="Art.1"></a>Artikel <a href="#Art.2">1</a>. Tekst...<br>
      <a name="Art.2" href="#Art.1">Art.</a> <a href="#LNK0002">2</a>. Tekst<br>
      ----------<br>
      (<font color="red">1</font>)<W <a href="...">2018-12-06/11</a>, art. 11; ...><br>
    """
    soup = BeautifulSoup(html_bytes, "html.parser")

    # --- Metadata uit de titelsectie ---
    title_box = soup.find("div", id="list-title-1")
    title_text = title_box.get_text(" ", strip=True) if title_box else ""
    wet_match = re.search(r"\d+\s+\w+\s+\d{4}\.\s+-\s+(.+?)(?:\s*\(NOTA|$)", title_text)
    wet_naam = wet_match.group(1).strip().rstrip(".") if wet_match else "onbekend"
    bijgewerkt_match = re.search(r"tekstbijwerking tot\s+(\d+-\d+-\d+)", title_text)
    bijgewerkt = bijgewerkt_match.group(1) if bijgewerkt_match else ""

    # --- Artikeltekst uit div#list-title-3 ---
    text_box = soup.find("div", id="list-title-3")
    if not text_box:
        raise ValueError("Geen div#list-title-3 gevonden in de Justel HTML")

    output_lines: list[str] = []
    children = list(text_box.children)
    n = len(children)
    i = 0

    # Werkbuffers
    current_parts: list[str] = []   # tekst-onderdelen voor de huidige regel
    in_sep_block = False             # na ---------- separator?
    in_notes_block = False           # opeenvolgende nota-regels na eerste nota

    def flush(force_blank: bool = False):
        """
        Verwerk de inhoud van current_parts tot een regel en voeg toe.
        Retourneert True als er iets geplakt is.
        """
        nonlocal in_sep_block, in_notes_block
        raw = "".join(current_parts).strip()
        raw = re.sub(r"[ \t]{2,}", " ", raw)
        raw = raw.replace("\xa0", " ").strip()
        current_parts.clear()

        if not raw:
            if force_blank and (not output_lines or output_lines[-1] != ""):
                output_lines.append("")
            return False

        # Wijzigingsnota-separator: ----------
        if re.match(r"^-{3,}$", raw):
            in_sep_block = True
            return False

        # Wijzigingsnota: patroon na separator of na vorige nota
        # Formaat: "(N)<W datum, art. X; Inwerkingtreding: datum>"
        # De font-tag wordt geskipt → "()" zonder getal of met spatie ertussen
        is_note_context = in_sep_block or in_notes_block
        if is_note_context:
            in_sep_block = False
            # Normaliseer "(  )" of "( 1 )" → matching patroon
            stripped_raw = re.sub(r"\(\s*\d*\s*\)", "(N)", raw)
            if re.match(r"^\(N\)\s*<[A-Z]", stripped_raw):
                # Wijzigingsnota → skippen (niet inline in de tekst)
                in_notes_block = True  # volgende nota's ook skippen
                return False
            # Bevat "<W" als aanduiding van een wijziging (fallback)
            if "<W " in raw or "<W\t" in raw:
                in_notes_block = True
                return False
            # Toch geen nota — beëindig notes-blok
            in_notes_block = False

        # Normale tekst
        if not output_lines or output_lines[-1] != "":
            output_lines.append("")  # blanco scheiding
        # Ongedaan: de blanco is al er of hoeft er niet
        output_lines.append(raw)
        return True

    def ensure_blank():
        if output_lines and output_lines[-1] != "":
            output_lines.append("")

    def add_heading(prefix: str, text: str):
        nonlocal in_notes_block, in_sep_block
        in_notes_block = False
        in_sep_block = False
        ensure_blank()
        output_lines.append(f"{prefix} {text}")
        output_lines.append("")

    # --- Hoofdloop ---
    while i < n:
        elem = children[i]

        # NavigableString: tekst-inhoud
        if isinstance(elem, NavigableString):
            s = str(elem)
            # Non-breaking spaces → gewone spatie
            s = s.replace("\xa0", " ")
            if s.strip():
                current_parts.append(s)
            i += 1
            continue

        if not isinstance(elem, Tag):
            i += 1
            continue

        tag = elem.name

        # --- <br> → einde van de huidige regel ---
        if tag == "br":
            flush(force_blank=False)
            i += 1
            continue

        # --- <sup> → amendementsmarker (getal) → negeren ---
        if tag == "sup":
            i += 1
            continue

        # --- <font color="red"> → amendementsmarkering → negeren ---
        if tag == "font":
            i += 1
            continue

        # --- <h2> binnen text_box (de "Tekst" kop) → negeren ---
        if tag == "h2":
            i += 1
            continue

        # --- <p> → paragraaf ---
        if tag == "p":
            flush()
            p_text = elem.get_text(" ", strip=True)
            if p_text:
                ensure_blank()
                output_lines.append(p_text)
                output_lines.append("")
            i += 1
            continue

        # --- <a> → meest complexe geval ---
        if tag == "a":
            name_attr = elem.get("name", "")
            href_attr = elem.get("href", "")
            elem_text = elem.get_text(strip=True)

            # Structuurlabel-anker: <a name="LNK0001">DEEL 1.</a>
            if re.match(r"^LNK\d+$", name_attr) and elem_text:
                flush()
                label = elem_text

                # Lees de vervolgtekst (subtitel na " - ")
                subtitle_parts: list[str] = []
                j = i + 1
                while j < n:
                    c = children[j]
                    if isinstance(c, NavigableString):
                        s = c.replace("\xa0", " ").strip()
                        if s:
                            subtitle_parts.append(s)
                        j += 1
                    elif isinstance(c, Tag) and c.name == "br":
                        j += 1  # sla de br over en stop
                        break
                    elif isinstance(c, Tag) and re.match(r"^LNK\d+$", c.get("name", "")):
                        break  # volgend structuurlabel
                    elif isinstance(c, Tag) and re.match(r"^Art\.\d", c.get("name", "")):
                        break  # volgend artikel
                    else:
                        j += 1

                subtitle = " ".join(subtitle_parts).strip()
                subtitle = re.sub(r"^[-–—]\s*", "", subtitle).strip()

                m = _STRUCT_RE.match(label)
                if m:
                    prefix = _struct_heading(label)
                    heading_text = f"{label} — {subtitle}" if subtitle else label
                    add_heading(prefix, heading_text)
                else:
                    # Sectie-titel (Doel, Toepassingsgebied, etc.)
                    if label and not re.match(r"^Art\.", label):
                        ensure_blank()
                        output_lines.append(f"**{label}**")
                        output_lines.append("")

                i = j
                continue

            # Artikel-anker (leeg, name="Art.1"):
            # <a name="Art.1"></a>Artikel <a href="#Art.2">1</a>. tekst
            if re.match(r"^Art\.\d", name_attr) and not elem_text:
                flush()
                in_notes_block = False
                in_sep_block = False
                art_num_str = ""
                art_body_parts: list[str] = []
                j = i + 1
                reading_num = True
                first_body_piece = True  # strip leading ". " op eerste stuk
                while j < n:
                    c = children[j]
                    if isinstance(c, NavigableString):
                        s = c.replace("\xa0", " ")
                        stripped = s.strip()
                        if reading_num:
                            if stripped in ("Artikel", "Art.", ""):
                                j += 1
                                continue
                            if stripped.startswith("."):
                                rest = stripped.lstrip(".").strip()
                                if rest:
                                    art_body_parts.append(rest)
                                reading_num = False
                                first_body_piece = False
                                j += 1
                                continue
                        else:
                            if first_body_piece:
                                first_body_piece = False
                                # Strip leading ". " die na artikelnummer-link staat
                                s2 = s.replace("\xa0", " ")
                                if s2.lstrip().startswith("."):
                                    s2 = s2.lstrip().lstrip(".").strip()
                                art_body_parts.append(s2)
                            else:
                                art_body_parts.append(s)
                        j += 1
                    elif isinstance(c, Tag) and c.name == "a":
                        inner = c.get_text(strip=True)
                        if reading_num and re.match(r"^[\d/\w]+$", inner):
                            art_num_str = inner.strip()
                            reading_num = False
                        elif reading_num:
                            j += 1
                            continue
                        else:
                            if first_body_piece:
                                first_body_piece = False
                            art_body_parts.append(inner)
                        j += 1
                    elif isinstance(c, Tag) and c.name in ("sup", "font"):
                        j += 1
                    elif isinstance(c, Tag) and c.name == "br":
                        break
                    else:
                        j += 1

                ensure_blank()
                output_lines.append(f"## Art. {art_num_str}")
                output_lines.append("")
                body_text = "".join(art_body_parts).strip()
                body_text = re.sub(r"[ \t]{2,}", " ", body_text)
                if body_text:
                    output_lines.append(body_text)
                i = j
                continue

            # Artikel-anker (niet leeg, name="Art.N", text="Art."):
            # <a name="Art.2" href="#Art.1">Art.</a> <a href="#LNK0002">2</a>. tekst
            if re.match(r"^Art\.\d", name_attr) and elem_text == "Art.":
                flush()
                in_notes_block = False
                in_sep_block = False
                art_num_str = ""
                art_body_parts: list[str] = []
                j = i + 1
                reading_num = True
                first_body_piece2 = True
                while j < n:
                    c = children[j]
                    if isinstance(c, NavigableString):
                        s = c.replace("\xa0", " ")
                        stripped = s.strip()
                        if reading_num:
                            if stripped.startswith("."):
                                rest = stripped.lstrip(".").strip()
                                if rest:
                                    art_body_parts.append(rest)
                                reading_num = False
                                first_body_piece2 = False
                                j += 1
                                continue
                            elif stripped:
                                art_body_parts.append(s)
                            j += 1
                        else:
                            if first_body_piece2:
                                first_body_piece2 = False
                                s2 = s.replace("\xa0", " ")
                                if s2.lstrip().startswith("."):
                                    s2 = s2.lstrip().lstrip(".").strip()
                                art_body_parts.append(s2)
                            else:
                                art_body_parts.append(s)
                            j += 1
                    elif isinstance(c, Tag) and c.name == "a":
                        inner = c.get_text(strip=True).strip()
                        if reading_num and re.match(r"^[\d/\w]+$", inner):
                            art_num_str = inner
                            reading_num = False
                        elif not reading_num:
                            if first_body_piece2:
                                first_body_piece2 = False
                            art_body_parts.append(inner)
                        j += 1
                    elif isinstance(c, Tag) and c.name in ("sup", "font"):
                        j += 1
                    elif isinstance(c, Tag) and c.name == "br":
                        break
                    else:
                        j += 1

                ensure_blank()
                output_lines.append(f"## Art. {art_num_str}")
                output_lines.append("")
                body_text = "".join(art_body_parts).strip()
                body_text = re.sub(r"[ \t]{2,}", " ", body_text)
                if body_text:
                    output_lines.append(body_text)
                i = j
                continue

            # Alle andere <a> → extraheer tekst
            if elem_text:
                current_parts.append(elem_text)
            i += 1
            continue

        # Andere tags: extraheer tekst
        text = elem.get_text(" ", strip=True)
        if text:
            current_parts.append(text)
        i += 1

    # Flush resterende inhoud
    flush()

    # Post-processing
    body = _postprocess(output_lines)
    return wet_naam, bijgewerkt, body


def _postprocess(lines: list[str]) -> str:
    """
    Finale cleanup van de geparste regels:
    - Verwijder B.S.-ruis (headers, footers)
    - Collapse opeenvolgende lege regels
    - Herstel PDF-afbreking
    - Strip 'Tekst' label van de Justel section-header
    """
    result: list[str] = []
    prev_blank = True  # start als "blank" zodat eerste non-blank direct toe gaat

    noise_re = re.compile(
        r"^(?:"
        r"Tekst\s*$"                         # Justel sectie-heading "Tekst"
        r"|MONITEUR BELGE|BELGISCH STAATSBLAD"
        r"|Pagina \d+ van \d+"
        r"|ejustice\.just\.fgov|www\.ejustice"
        r"|Copyright Belgisch"
        r")",
        re.IGNORECASE,
    )

    for line in lines:
        stripped = line.strip()

        # Ruis verwijderen
        if noise_re.match(stripped):
            continue

        # Lege regels: max één op een rij
        if not stripped:
            if not prev_blank:
                result.append("")
                prev_blank = True
            continue

        prev_blank = False
        # BR-artefacten ("BR>" aan het eind van een regel)
        stripped = re.sub(r"\s*BR>$", "", stripped)
        result.append(stripped)

    # Herstel afgebroken woorden
    text = "\n".join(result)
    text = fix_broken_words(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ---------------------------------------------------------------------------
# Frontmatter genereren
# ---------------------------------------------------------------------------

def make_frontmatter_justel(cfg: dict, source_name: str, wet_naam: str,
                             bijgewerkt: str) -> str:
    """Genereer YAML frontmatter voor een Justel-HTML-extract."""
    tags = cfg.get("tags", [])
    tags_str = str(tags).replace("'", '"')
    itaa = cfg.get("itaa_sectie", "")
    wet = cfg.get("wet", wet_naam)
    bij = cfg.get("bijgewerkt", bijgewerkt)
    bron_rol = cfg.get("bron_rol", "itaa_lex")

    return textwrap.dedent(f"""\
        ---
        tags: {tags_str}
        itaa-lex-sectie: "{itaa}"
        wet: "{wet}"
        bron_rol: "{bron_rol}"
        status: "beschikbaar"
        bijgewerkt: "{bij}"
        bron: "www.ejustice.just.fgov.be (Justel, gecoördineerde versie)"
        chunk:
          level: 2
          type: "Art."
          sub_strategy: null
        ---

        # {wet}

        *Bijgewerkt tot en met {bij} — gecoördineerde versie via Justel.*

    """)


# ---------------------------------------------------------------------------
# Bilingual B.S. PDF-extractie (voor KB zonder Justel HTML)
# ---------------------------------------------------------------------------

def extract_bs_bilingual_nl(pdf_paths: list[str], nl_col_x: int = 290,
                             page_width: int = 595) -> str:
    """
    Extraheer de NL-kolom uit bilinguele Belgisch Staatsblad PDF-pagina's.
    Combineert meerdere losse PDF-pagina's (1 PDF per B.S. pagina) tot één tekst.
    """
    parts: list[str] = []
    col_w = page_width - nl_col_x

    for pdf_path in pdf_paths:
        cmd = [
            "pdftotext", "-layout",
            "-x", str(nl_col_x), "-y", "0",
            "-W", str(col_w), "-H", "842",
            pdf_path, "-",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"pdftotext mislukt voor {pdf_path}: {result.stderr}")
        parts.append(result.stdout)

    return "\n".join(parts)


def clean_bs_bilingual_text(text: str) -> str:
    """
    Opschonen van bilinguele B.S.-tekst na NL-kolom-extractie:
    - Verwijder B.S.-headers en -footers
    - Strip kolom-lekresten (enkele letters/tekens van de FR-kolom)
    - Verwijder "Verslag aan de Koning" (preambule, geen wettekst)
    - Verwijder aanhef/preambule (Gelet op ..., Overwegende dat ...)
    - Verwijder handtekeningblok na het laatste artikel
    - Zet "Artikel N. tekst" om naar "## Art. N" headings
    """
    lines = text.split("\n")
    result: list[str] = []
    prev_blank = False
    in_verslag = False
    in_preambule = False
    found_besluit = False
    found_last_art = False  # na het laatste "Art. N." artikel

    noise_re = re.compile(
        r"^(?:"
        r"MONITEUR BELGE|BELGISCH STAATSBLAD"
        r"|SERVICE PUBLIC|FEDERALE OVERHEIDSDIENST"
        r"|— Ed\.\s+\d|− Ed\.\s+\d"
        r"|\d{4,5}\s*$"         # B.S. pagina-nummers
        r"|Copyright|www\."
        r")",
        re.IGNORECASE,
    )

    # Detecteer einde-artikel patronen (handtekening / slotformule)
    end_article_re = re.compile(
        r"^(?:ALBERT|FILIP|BOUDEWIJN|Gegeven te|Van Koningswege|"
        r"De Minister|D\. REYNDERS|Nota's?|^\(\d+\))",
        re.IGNORECASE,
    )

    for raw_line in lines:
        # Form feeds verwijderen
        raw_line = raw_line.replace("\x0c", "")
        # Strip kolom-lekresten (FR-kolom die overloopt in de NL-kolom):
        # Heuristiek: als een regel begint met 0-3 tekens (letters/cijfers/punct)
        # gevolgd door 4 of meer spaties, dan is het prefix een kolom-lek.
        # Behoud regels die beginnen met spaties alleen (ingesprongen NL tekst).
        stripped = re.sub(r"^.{0,3}\s{4,}", "", raw_line)
        stripped = stripped.strip()

        if not stripped:
            if not prev_blank:
                result.append("")
                prev_blank = True
            continue

        # B.S. ruis
        if noise_re.match(stripped):
            prev_blank = False
            continue

        # Verslag aan de Koning: overslaan (preambule, geen wettekst)
        if re.match(r"^VERSLAG AAN DE KONING", stripped, re.I):
            in_verslag = True
            continue
        if in_verslag:
            # Einde verslag bij herhaalde KB-datum (deel 2 van dubbele publicatie)
            if re.match(r"^\d{1,2}\s+JANUARI\s+\d{4}", stripped, re.I):
                in_preambule = True
                in_verslag = False
            continue

        # Aanhef/Preambule
        if in_preambule:
            if re.match(r"Hebben Wij besloten", stripped, re.I):
                found_besluit = True
                in_preambule = False
            continue

        if not found_besluit:
            continue

        # Handtekeningblok / slotformule na het dispositief overslaan
        if end_article_re.match(stripped):
            break

        # Artikel-heading: "Artikel N. tekst" of "Art. N. tekst"
        art_m = re.match(r"^(?:Artikel|Art\.)\s+([\d/\w]+)\.\s*(.*)", stripped, re.I)
        if art_m:
            art_num = art_m.group(1)
            art_body = art_m.group(2).strip()
            if not prev_blank:
                result.append("")
            result.append(f"## Art. {art_num}")
            result.append("")
            if art_body:
                result.append(art_body)
            prev_blank = False
            continue

        result.append(stripped)
        prev_blank = False

    text_out = "\n".join(result)
    text_out = fix_broken_words(text_out)
    text_out = re.sub(r"\n{3,}", "\n\n", text_out)
    return text_out.strip()


# ---------------------------------------------------------------------------
# Hoofd-conversiefuncties
# ---------------------------------------------------------------------------

def convert_justel_html(cfg: dict, source_name: str, dry_run: bool = False) -> str:
    """Converteer een Justel HTML-pagina naar markdown (method: justel_html)."""
    params = cfg.get("extract", {}).get("params", {})
    source_url = params.get("start_url") or cfg.get("source_url")
    if not source_url:
        raise ValueError(
            f"source_url of extract.params.start_url ontbreekt voor {source_name}"
        )

    output_path = ROOT / cfg["output"]

    print(f"  → Ophalen: {source_url}")
    html = fetch_justel(source_url)
    print(f"  → Parseren ({len(html):,} bytes HTML)")

    wet_naam, bijgewerkt, body = parse_justel_html(html)
    print(f"  → Wet: {wet_naam[:60]}")
    print(f"  → Bijgewerkt: {bijgewerkt}")

    art_count = len(re.findall(r"^## Art\.", body, re.MULTILINE))
    struct_count = len(re.findall(
        r"^#{2,6}\s+(?:DEEL|TITEL|HOOFDSTUK|Afdeling)", body, re.MULTILINE
    ))
    print(f"  → Artikelen: {art_count}, structurele headings: {struct_count}")

    frontmatter = make_frontmatter_justel(cfg, source_name, wet_naam, bijgewerkt)
    content = frontmatter + body + "\n"

    if not dry_run:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
        print(
            f"  ✓ Geschreven: {output_path.relative_to(ROOT)} "
            f"({len(content):,} tekens)"
        )

    return str(output_path)


def convert_justel_bs_bilingual(cfg: dict, source_name: str,
                                 dry_run: bool = False) -> str:
    """
    Converteer bilinguele B.S. PDF-pagina's naar markdown (method: justel_bs_bilingual).
    Bedoeld voor KB-documenten die niet als Justel-HTML beschikbaar zijn.
    """
    params = cfg.get("extract", {}).get("params", {})
    raw_files = params.get("raw_files", [])
    if not raw_files:
        raw_single = cfg.get("raw")
        if raw_single:
            raw_files = [raw_single]
        else:
            raise ValueError(
                f"extract.params.raw_files of raw ontbreekt voor {source_name}"
            )

    nl_col_x = params.get("nl_col_x", 290)
    output_path = ROOT / cfg["output"]

    pdf_paths = [str(ROOT / f) for f in raw_files]
    print(f"  → Extraheer NL-kolom uit {len(pdf_paths)} PDF(s) (x={nl_col_x})")
    for p in pdf_paths:
        if not Path(p).exists():
            raise FileNotFoundError(f"PDF niet gevonden: {p}")

    raw_text = extract_bs_bilingual_nl(pdf_paths, nl_col_x=nl_col_x)
    print(f"  → Ruwe tekst: {len(raw_text):,} tekens")

    cleaned = clean_bs_bilingual_text(raw_text)
    print(f"  → Na cleanup: {len(cleaned):,} tekens")

    art_count = len(re.findall(r"^## Art\.", cleaned, re.MULTILINE))
    print(f"  → Artikelen: {art_count}")

    # Frontmatter
    tags = cfg.get("tags", [])
    tags_str = str(tags).replace("'", '"')
    itaa = cfg.get("itaa_sectie", "")
    wet = cfg.get("wet", source_name)
    bij = cfg.get("bijgewerkt", "")
    bron_rol = cfg.get("bron_rol", "itaa_lex")

    frontmatter = textwrap.dedent(f"""\
        ---
        tags: {tags_str}
        itaa-lex-sectie: "{itaa}"
        wet: "{wet}"
        bron_rol: "{bron_rol}"
        status: "beschikbaar"
        bijgewerkt: "{bij}"
        bron: "ejustice.just.fgov.be (B.S. originele publicatie — NL-kolom)"
        chunk:
          level: 2
          type: "Art."
          sub_strategy: null
        ---

        # {wet}

        *Gepubliceerd in het Belgisch Staatsblad — gecoördineerde versie niet beschikbaar via Justel.*

    """)

    content = frontmatter + cleaned + "\n"

    if not dry_run:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
        print(
            f"  ✓ Geschreven: {output_path.relative_to(ROOT)} "
            f"({len(content):,} tekens)"
        )

    return str(output_path)
