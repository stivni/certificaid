#!/usr/bin/env python3
"""Converteert WBTW PDF (single-language NL) naar gestructureerde markdown."""

import subprocess
import re

INPUT_PDF = "resources/wetteksten/raw/WBTW-vatupdate.pdf"
OUTPUT_MD = "resources/wetteksten/WBTW.md"


def extract_text(pdf_path):
    result = subprocess.run(
        ['pdftotext', '-layout', pdf_path, '-'],
        capture_output=True, text=True
    )
    return result.stdout


def clean_and_structure(text):
    lines = text.split('\n')
    out = []
    prev_empty = False

    for line in lines:
        stripped = line.strip()

        # Verwijder ruis
        if not stripped:
            if not prev_empty:
                out.append('')
            prev_empty = True
            continue
        if re.match(r'^[-–—I/\d]+\s*-?\s*$', stripped):  # paginanummers/scheidingslijnen
            continue
        if re.match(r'^(FOD Financiën|www\.fisconet|W\.Btw|Federale|Overheidsdienst|Beleidsexpertise)', stripped):
            continue
        if re.match(r'^BELASTING OVER DE$|^TOEGEVOEGDE WAARDE$|^WETBOEK VAN DE BTW$', stripped):
            continue

        # TITEL heading
        if re.match(r'^TITEL\s+[IVXLC]+', stripped):
            if not prev_empty:
                out.append('')
            out.append(f'### {stripped}')
            out.append('')
            prev_empty = True
            continue

        # HOOFDSTUK heading
        if re.match(r'^HOOFDSTUK\s+', stripped):
            if not prev_empty:
                out.append('')
            out.append(f'#### {stripped}')
            out.append('')
            prev_empty = True
            continue

        # Afdeling
        if re.match(r'^Afdeling\s+\w+\.?\s*[-–]', stripped):
            if not prev_empty:
                out.append('')
            out.append(f'##### {stripped}')
            out.append('')
            prev_empty = True
            continue

        # "Artikel X" of "Art. X" alleenstaand op een regel
        art_match = re.match(r'^(?:Artikel|Art\.)\s+(\d+[\w/]*)\s*$', stripped)
        if art_match:
            art_num = art_match.group(1)
            if not prev_empty:
                out.append('')
            out.append(f'## Art. {art_num}')
            out.append('')
            prev_empty = True
            continue

        # "Artikel X" met tekst op dezelfde regel
        art_inline = re.match(r'^(?:Artikel|Art\.)\s+(\d+[\w/]*)\s+(.+)$', stripped)
        if art_inline:
            art_num = art_inline.group(1)
            rest = art_inline.group(2)
            if not prev_empty:
                out.append('')
            out.append(f'## Art. {art_num}')
            out.append('')
            out.append(rest)
            prev_empty = False
            continue

        out.append(stripped)
        prev_empty = False

    text = '\n'.join(out)
    # Verbind afgebroken woorden
    text = re.sub(r'(\w)-\n(\w)', r'\1\2', text)
    # Maximaal één lege regel
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def main():
    print(f"Verwerking {INPUT_PDF}...")
    raw = extract_text(INPUT_PDF)
    print(f"Ruwe tekst: {len(raw)} tekens")

    md = clean_and_structure(raw)

    art_count = len(re.findall(r'^## Art\.', md, re.MULTILINE))
    print(f"Artikelen gevonden: {art_count}")

    header = """---
tags: [wettekst, "VI.A"]
itaa-lex-sectie: "VI.A"
wet: "Wet 3 juli 1969 tot invoering van het Wetboek van de belasting over de toegevoegde waarde (WBTW)"
status: "beschikbaar"
bijgewerkt: "23.04.2020"
bron: "Fisconetplus.be (officieuze gecoördineerde versie, bijwerking nr. 35)"
waarschuwing: "⚠️ Versie 2020 — vervangen door actuele versie zodra beschikbaar"
---

# Wetboek van de Belasting over de Toegevoegde Waarde (WBTW)

*Bijgewerkt tot en met de Wet van 23.04.2020 (B.S. 11.05.2020) — officieuze gecoördineerde versie.*
*Bron: Fisconetplus.be bijwerking nr. 35.*
*⚠️ Versie 2020 — vervangen door actuele versie zodra beschikbaar van Fisconet.*

"""

    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write(header + md)

    print(f"Output: {OUTPUT_MD}")


if __name__ == '__main__':
    main()
