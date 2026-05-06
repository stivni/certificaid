#!/usr/bin/env python3
"""
Scrapt het BTW-wetboek (WBTW) van ejustice.just.fgov.be als HTML
en converteert naar gestructureerde markdown.
URL: https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&nm=1969070305&table_name=titel
"""

import urllib.request
import re
import html
import sys
from html.parser import HTMLParser

URL = "https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&nm=1969070305&table_name=titel"
OUTPUT_MD = "resources/wetteksten/WBTW.md"


class WBTWParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_text_div = False
        self.depth = 0
        self.text_parts = []
        self.current_text = []
        self.target_div_id = "list-title-3"  # div met artikeltekst op ejustice

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'div' and attrs_dict.get('id') == self.target_div_id:
            self.in_text_div = True
            self.depth = 1
        elif self.in_text_div and tag == 'div':
            self.depth += 1

        if self.in_text_div and tag == 'br':
            self.current_text.append('\n')
        if self.in_text_div and tag == 'a':
            # Anker voor artikel-naam
            name = attrs_dict.get('name', '')
            if name.startswith('Art.') or name.startswith('LNK'):
                self.current_text.append(f'__ANCHOR_{name}__')

    def handle_endtag(self, tag):
        if self.in_text_div and tag == 'div':
            self.depth -= 1
            if self.depth == 0:
                self.in_text_div = False
                self.text_parts.append(''.join(self.current_text))

    def handle_data(self, data):
        if self.in_text_div:
            self.current_text.append(data)

    def handle_entityref(self, name):
        if self.in_text_div:
            self.current_text.append(html.unescape(f'&{name};'))

    def handle_charref(self, name):
        if self.in_text_div:
            self.current_text.append(html.unescape(f'&#{name};'))


def fetch_html(url):
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (compatible; research-tool)',
        'Accept': 'text/html,application/xhtml+xml',
        'Accept-Language': 'nl-BE,nl;q=0.9'
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode('utf-8', errors='replace')


def parse_to_markdown(raw_text):
    """Verwerk de ruwe tekst naar markdown met ## Art. X headings."""
    # Vervang ankers door artikel-headings
    # __ANCHOR_Art.1__ -> ## Art. 1
    text = re.sub(r'__ANCHOR_Art\.(\w+)__\s*Artikel\s+\w+\.?\s*', r'## Art. \1\n\n', raw_text)
    # Verwijder resterende ankers
    text = re.sub(r'__ANCHOR_\w+__', '', text)

    # Verwijder HTML-ruis en lege regels normaliseren
    lines = []
    for line in text.split('\n'):
        stripped = line.strip()

        # Verwijder paginacoördinaten, nummers, lege fragmenten
        if not stripped:
            lines.append('')
            continue
        if re.match(r'^\d+$', stripped):
            continue

        # TITEL heading
        if re.match(r'^TITEL\s+[IVXLC]+\.?\s*[-–.]', stripped):
            lines.append('')
            lines.append(f'### {stripped}')
            lines.append('')
            continue

        # HOOFDSTUK heading
        if re.match(r'^HOOFDSTUK\s+', stripped):
            lines.append('')
            lines.append(f'#### {stripped}')
            lines.append('')
            continue

        # Afdeling
        if re.match(r'^Afdeling\s+', stripped):
            lines.append('')
            lines.append(f'##### {stripped}')
            lines.append('')
            continue

        lines.append(stripped)

    text = '\n'.join(lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def main():
    print(f"Ophalen WBTW van ejustice...")
    print(f"URL: {URL}")

    try:
        html_content = fetch_html(URL)
    except Exception as e:
        print(f"Fout bij ophalen: {e}")
        sys.exit(1)

    print(f"HTML opgehaald ({len(html_content)} bytes). Parsen...")

    # Probeer meerdere div-IDs (ejustice gebruikt wisselende nummering)
    parser = WBTWParser()

    # Zoek de div met artikeltekst — probeer verschillende IDs
    for div_id in ["list-title-3", "list-title-4", "list-title-2"]:
        parser2 = WBTWParser()
        parser2.target_div_id = div_id
        parser2.feed(html_content)
        if parser2.text_parts and len(''.join(parser2.text_parts)) > 1000:
            parser = parser2
            print(f"Artikeltekst gevonden in div#{div_id}")
            break

    if not parser.text_parts:
        # Fallback: dump alle tekst uit de pagina
        print("Geen div gevonden, fallback naar volledige tekst-extractie...")
        raw = re.sub(r'<[^>]+>', ' ', html_content)
        raw = html.unescape(raw)
        raw_text = raw
    else:
        raw_text = ''.join(parser.text_parts)

    print(f"Ruwe tekst: {len(raw_text)} tekens")

    md_content = parse_to_markdown(raw_text)

    art_count = len(re.findall(r'^## Art\.', md_content, re.MULTILINE))
    print(f"Artikelen gevonden: {art_count}")

    if art_count < 10:
        # Bewaar ruwe tekst voor diagnose
        with open('/tmp/wbtw-raw.txt', 'w') as f:
            f.write(raw_text[:5000])
        print("Weinig artikelen gevonden — ruwe tekst bewaard in /tmp/wbtw-raw.txt voor diagnose")

    header = """---
tags: [wettekst, "VI.A"]
itaa-lex-sectie: "VI.A"
wet: "Wet 3 juli 1969 tot invoering van het Wetboek van de belasting over de toegevoegde waarde (WBTW)"
status: "beschikbaar"
bron: "ejustice.just.fgov.be (gecoördineerde versie)"
---

# Wetboek van de Belasting over de Toegevoegde Waarde (WBTW)

*Bron: ejustice.just.fgov.be — gecoördineerde versie.*

"""

    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write(header + md_content)

    print(f"Output: {OUTPUT_MD}")


if __name__ == '__main__':
    main()
