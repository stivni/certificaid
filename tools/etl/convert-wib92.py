#!/usr/bin/env python3
"""
Converteert WIB92.pdf (tweetalig) naar gestructureerde NL markdown.
Extraheert alleen de rechterkolom (NL) via coördinaten.
"""

import subprocess
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from lib.cleanup import fix_broken_words, merge_wrapped_lines  # noqa: E402

INPUT_PDF = "resources/raw/wetteksten/WIB92.pdf"
OUTPUT_MD = "resources/bronnen/wetteksten/WIB92.md"

# Pagina 42 = eerste pagina met artikeltekst (Art. 1)
# Pagina 1315 = laatste pagina
START_PAGE = 42
END_PAGE = 1315

# Rechterkolom: x=300 tot x=595 (pagina is 595pt breed)
COL_X = 300
COL_W = 295
PAGE_H = 842


def extract_page(pdf_path, page):
    result = subprocess.run(
        ['pdftotext', '-layout',
         '-f', str(page), '-l', str(page),
         '-x', str(COL_X), '-y', '0', '-W', str(COL_W), '-H', str(PAGE_H),
         pdf_path, '-'],
        capture_output=True, text=True
    )
    return result.stdout


def clean_lines(text):
    """Verwijder ruis: paginanummers, URL, form feeds, decoratieve lijnen."""
    lines = []
    for line in text.split('\n'):
        stripped = line.strip()
        # Verwijder lege regels, paginanummers, URL-fragmenten, decoraties
        if not stripped:
            lines.append('')
            continue
        if re.match(r'^\d+$', stripped):  # paginanummer
            continue
        if re.match(r'^(net|fisconet|www\.).*', stripped, re.I):  # URL-fragment
            continue
        if stripped in ('——', '–', '—', '–––'):  # decoratieve lijn
            continue
        if stripped == '\x0c':  # form feed
            continue
        lines.append(line)
    return '\n'.join(lines)


def join_hyphens(text):
    """Verbindt afgebroken woorden aan einde van regel.

    Delegateert naar lib.cleanup.fix_broken_words: soft hyphens (vervolg met
    kleine letter) worden samengevoegd; echte koppeltekens voor hoofdletters
    (Lid-Staten, Noord-Ierland) blijven behouden.
    """
    return fix_broken_words(text)


def normalize_whitespace(text):
    """Normaliseert meerdere spaties tot één (artefact van kolom-extractie)."""
    lines = []
    for line in text.split('\n'):
        # Behoud indentatie maar normaliseer interne spaties
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        normalized = re.sub(r'  +', ' ', stripped)
        lines.append(' ' * min(indent, 4) + normalized)  # max 4 spaties indent
    return '\n'.join(lines)


def to_markdown(text):
    """Zet koppen en artikelnummers om naar markdown-structuur."""
    lines = text.split('\n')
    md_lines = []
    prev_empty = False

    for line in lines:
        stripped = line.strip()

        # Artikel-heading: "Art. 1", "Art. 5/1", "Art. 19bis"
        art_match = re.match(r'^Art\.\s+(\d+[\w/]*)$', stripped)
        if art_match:
            art_num = art_match.group(1)
            if not prev_empty:
                md_lines.append('')
            md_lines.append(f'## Art. {art_num}')
            md_lines.append('')
            prev_empty = True
            continue

        # TITEL-heading
        if re.match(r'^TITEL\s+[IVXLC]+\.?\s*[-–]', stripped):
            if not prev_empty:
                md_lines.append('')
            md_lines.append(f'### {stripped}')
            md_lines.append('')
            prev_empty = True
            continue

        # HOOFDSTUK-heading
        if re.match(r'^HOOFDSTUK\s+', stripped):
            if not prev_empty:
                md_lines.append('')
            md_lines.append(f'#### {stripped}')
            md_lines.append('')
            prev_empty = True
            continue

        # Afdeling / Onderafdeling
        if re.match(r'^(Afdeling|Onderafdeling)\s+', stripped):
            if not prev_empty:
                md_lines.append('')
            md_lines.append(f'##### {stripped}')
            md_lines.append('')
            prev_empty = True
            continue

        # Lege regel
        if not stripped:
            if not prev_empty:
                md_lines.append('')
            prev_empty = True
            continue

        # Normale tekstregel
        md_lines.append(stripped)
        prev_empty = False

    return '\n'.join(md_lines)


def remove_consecutive_blanks(text):
    """Maximaal één lege regel na elkaar."""
    return re.sub(r'\n{3,}', '\n\n', text)


def main():
    print(f"Verwerking {INPUT_PDF} (pagina's {START_PAGE}–{END_PAGE})...")

    all_text = []
    total = END_PAGE - START_PAGE + 1

    for i, page in enumerate(range(START_PAGE, END_PAGE + 1)):
        if i % 100 == 0:
            print(f"  Pagina {page}/{END_PAGE} ({i}/{total})...")
        raw = extract_page(INPUT_PDF, page)
        cleaned = clean_lines(raw)
        all_text.append(cleaned)

    full_text = '\n'.join(all_text)
    full_text = join_hyphens(full_text)
    full_text = normalize_whitespace(full_text)
    full_text = to_markdown(full_text)
    full_text = remove_consecutive_blanks(full_text)
    full_text = merge_wrapped_lines(full_text)

    header = """---
tags: [wettekst, "II"]
itaa-lex-sectie: "II"
wet: "Wetboek 10 april 1992 van de inkomstenbelastingen 1992 (WIB92)"
status: "beschikbaar"
bijgewerkt: "10.02.2026"
bron: "Fisconet (officieuze gecoördineerde versie, editie 2026)"
---

# Wetboek van de Inkomstenbelastingen 1992 (WIB92)

*Bijgewerkt tot en met de Wet van 10.02.2026 (B.S. 27.02.2026) — officieuze gecoördineerde versie.*
*Bron: Fisconetplus.be editie 2026.*

"""

    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write(header + full_text)

    # Tel artikelen
    art_count = len(re.findall(r'^## Art\.', full_text, re.MULTILINE))
    lines = full_text.count('\n')
    print(f"\nKlaar: {art_count} artikelen, {lines} regels")
    print(f"Output: {OUTPUT_MD}")


if __name__ == '__main__':
    main()
