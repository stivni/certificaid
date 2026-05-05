#!/usr/bin/env python3
"""
Generiek conversiescript voor Fisconet-PDFs naar gestructureerde NL markdown.
Ondersteunt:
  - NL-only PDFs (mode=nl)
  - Tweetalige NL/FR PDFs met twee-kolom layout (mode=bilingual)
"""

import subprocess, re, sys, os

CONFIGS = {
    'wbtw-2026': {
        'input': 'resources/wetteksten/raw/WBTW-2026.pdf',
        'output_resources': 'resources/wetteksten/WBTW.md',
        'output_content': 'content/bronnen/wetteksten/VIA-wbtw.md',
        'mode': 'nl',
        'itaa_sectie': 'VI.A',
        'wet': 'Wet 3 juli 1969 tot invoering van het Wetboek van de belasting over de toegevoegde waarde (WBTW)',
        'bijgewerkt': '19.12.2025',
        'titel': 'Wetboek van de Belasting over de Toegevoegde Waarde (WBTW)',
        'tags': '["VI.A"]',
    },
    'reg-brussel': {
        'input': 'resources/wetteksten/raw/Registratierechten-Brussel.pdf',
        'output_resources': 'resources/wetteksten/Registratierechten-Brussel.md',
        'output_content': 'content/bronnen/wetteksten/VIII-registratierechten-brussel.md',
        'mode': 'nl',
        'itaa_sectie': 'VIII',
        'wet': 'Wetboek der Registratie-, Hypotheek- en Griffierechten — Brussels Hoofdstedelijk Gewest',
        'bijgewerkt': '16.03.2026',
        'titel': 'Registratierechten — Brussels Hoofdstedelijk Gewest',
        'tags': '["VIII", "2.6"]',
    },
    'reg-waals': {
        'input': 'resources/wetteksten/raw/Registratierechten-Waals.pdf',
        'output_resources': 'resources/wetteksten/Registratierechten-Waals.md',
        'output_content': 'content/bronnen/wetteksten/VIII-registratierechten-waals.md',
        'mode': 'nl',
        'itaa_sectie': 'VIII',
        'wet': 'Wetboek der Registratie-, Hypotheek- en Griffierechten — Waals Gewest',
        'bijgewerkt': '16.03.2026',
        'titel': 'Registratierechten — Waals Gewest',
        'tags': '["VIII", "2.6"]',
    },
    'successie-brussel': {
        'input': 'resources/wetteksten/raw/successie-brussel.pdf',
        'output_resources': 'resources/wetteksten/Successierechten-Brussel.md',
        'output_content': 'content/bronnen/wetteksten/IX-successierechten-brussel.md',
        'mode': 'nl',
        'itaa_sectie': 'IX',
        'wet': 'Wetboek der Successierechten — Brussels Hoofdstedelijk Gewest',
        'bijgewerkt': '16.03.2026',
        'titel': 'Successierechten — Brussels Hoofdstedelijk Gewest',
        'tags': '["IX", "2.6"]',
    },
    'successie-waals': {
        'input': 'resources/wetteksten/raw/successie-waals.pdf',
        'output_resources': 'resources/wetteksten/Successierechten-Waals.md',
        'output_content': 'content/bronnen/wetteksten/IX-successierechten-waals.md',
        'mode': 'nl',
        'itaa_sectie': 'IX',
        'wet': 'Wetboek der Successierechten — Waals Gewest',
        'bijgewerkt': '16.03.2026',
        'titel': 'Successierechten — Waals Gewest',
        'tags': '["IX", "2.6"]',
    },
    'successie-federaal': {
        'input': 'resources/wetteksten/raw/successie-federaal.pdf',
        'output_resources': 'resources/wetteksten/Successierechten-federaal.md',
        'output_content': 'content/bronnen/wetteksten/IX-successierechten-federaal.md',
        'mode': 'bilingual',
        'start_page': 8,
        'col_x': 0,  # NL links
        'itaa_sectie': 'IX',
        'wet': 'Wetboek der Successierechten — federaal',
        'bijgewerkt': '01.04.2026',
        'titel': 'Successierechten — federaal',
        'tags': '["IX", "2.6"]',
    },
    'vcf-update': {
        'input': 'resources/wetteksten/raw/Registratierechten-VL.pdf',
        'output_resources': 'resources/wetteksten/VCF.md',
        'output_content': 'content/bronnen/wetteksten/IVA-vcf.md',
        'mode': 'bilingual',
        'start_page': 30,
        'col_x': 0,  # NL staat links
        'itaa_sectie': 'IV.A',
        'wet': 'Decreet 13 december 2013 houdende de Vlaamse Codex Fiscaliteit (VCF)',
        'bijgewerkt': '03.04.2026',
        'titel': 'Vlaamse Codex Fiscaliteit (VCF)',
        'tags': '["IV.A", "2.6"]',
    },
    'reg-federaal': {
        'input': 'resources/wetteksten/raw/Registratierechten-federaal.pdf',
        'output_resources': 'resources/wetteksten/Registratierechten-federaal.md',
        'output_content': 'content/bronnen/wetteksten/VIII-registratierechten-federaal.md',
        'mode': 'bilingual',
        'start_page': 8,
        'col_x': 0,  # NL staat links in deze PDF (omgekeerd t.o.v. WIB92)
        'itaa_sectie': 'VIII',
        'wet': 'Wetboek der Registratie-, Hypotheek- en Griffierechten — federaal',
        'bijgewerkt': '01.04.2026',
        'titel': 'Registratierechten — federaal',
        'tags': '["VIII", "2.6"]',
    },
    'brusselse-codex-fiscale-procedure': {
        'input': 'resources/wetteksten/raw/Brusselse-Codex-Fiscale-Procedure.pdf',
        'output_resources': 'resources/wetteksten/Brusselse-Codex-Fiscale-Procedure.md',
        'output_content': 'content/bronnen/wetteksten/IVB-brusselse-codex-fiscale-procedure.md',
        'mode': 'nl',
        'itaa_sectie': 'IV.B',
        'wet': 'Ordonnantie 6 maart 2019 betreffende de Brusselse Codex Fiscale Procedure',
        'bijgewerkt': '04.06.2024',
        'titel': 'Brusselse Codex Fiscale Procedure',
        'tags': '["IV.B", "2.5"]',
    },
    'decr-waals-belastingen': {
        'input': 'resources/wetteksten/raw/Decr-Waals-Directe-Belastingen.pdf',
        'output_resources': 'resources/wetteksten/Decr-Waals-Directe-Belastingen.md',
        'output_content': 'content/bronnen/wetteksten/IVC-decr-waals-directe-belastingen.md',
        'mode': 'nl',
        'itaa_sectie': 'IV.C',
        'wet': 'Decreet 6 mei 1999 betreffende de vestiging, de invordering en de geschillen inzake de Waalse gewestelijke belastingen',
        'bijgewerkt': '03.02.2026',
        'titel': 'Decreet Waalse gewestelijke belastingen',
        'tags': '["IV.C", "2.5"]',
    },
}


def extract_nl_text(pdf, mode, start_page=None, col_x=300):
    info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    pages_match = re.search(r'Pages:\s+(\d+)', info)
    total_pages = int(pages_match.group(1)) if pages_match else 300

    if mode == 'nl':
        r = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True)
        return r.stdout
    else:
        # Bilingual: extraheer rechterkolom per pagina
        parts = []
        sp = start_page or 1
        for p in range(sp, total_pages + 1):
            r = subprocess.run(
                ['pdftotext', '-layout', '-f', str(p), '-l', str(p),
                 '-x', str(col_x), '-y', '0', '-W', str(595 - col_x), '-H', '842',
                 pdf, '-'],
                capture_output=True, text=True
            )
            parts.append(r.stdout)
            if p % 100 == 0:
                print(f'  pagina {p}/{total_pages}...')
        return '\n'.join(parts)


def clean_and_structure(text, wet_naam):
    lines = text.split('\n')
    out = []
    prev_empty = False

    noise_patterns = [
        r'^(FOD Financiën|www\.fisconet|W\.Btw|W\.Reg|Federale|Overheidsdienst|Beleidsexpertise)',
        r'^BELASTING OVER DE$|^TOEGEVOEGDE WAARDE$|^WETBOEK VAN DE BTW$',
        r'^WETBOEK DER REGISTRATIE',
        r'^VLAAMSE CODEX FISCALITEIT$',
        r'^bijgewerkt tot|^BIJGEWERKT TOT',
        r'^WWW\.',
        # Justel-format (ejustice) ruis
        r'^JUSTEL - Geconsolideerde wetgeving',
        r'^http://www\.ejustice',
        r'^Dossiernummer\s*:',
        r'^Situatie\s*:',
        r'^Bron\s*: (BRUSSELS|WAALSE|BRUSSEL|FOD|JUSTITIE)',
        r'^Publicatie\s*:',
        r'^Inwerkingtreding\s*:',
        r'^Inhoudstafel$',
        r'^Tekst$',
        r'^Nota.*:$',
        r'^Copyright Belgisch',
        r'^Pagina \d+ van \d+',
        r'^Art\.\s+[\d][\d]*[-–,/]',  # TOC-artikelranges zoals "Art. 1-4", "Art. 5-8"
        r'^[-–—=]{3,}$',
        r'^\d+$',
        r'^[IVX]+/\d+\s*-?\s*$',  # paginanummers zoals "I/1 -"
        r'^-\s*[IVX]+/\d+\s*-$',
    ]

    for line in lines:
        stripped = line.strip()

        if not stripped:
            if not prev_empty:
                out.append('')
            prev_empty = True
            continue

        # Ruis verwijderen
        if any(re.match(p, stripped, re.I) for p in noise_patterns):
            continue
        if re.match(r'^net\w*plus\.be', stripped, re.I):
            continue

        # TITEL
        if re.match(r'^TITEL\s+[IVXLC]+', stripped):
            if not prev_empty:
                out.append('')
            out.append(f'### {stripped}')
            out.append('')
            prev_empty = True
            continue

        # HOOFDSTUK
        if re.match(r'^HOOFDSTUK\s+', stripped):
            if not prev_empty:
                out.append('')
            out.append(f'#### {stripped}')
            out.append('')
            prev_empty = True
            continue

        # Afdeling / Onderafdeling
        if re.match(r'^(Afdeling|Onderafdeling)\s+', stripped):
            if not prev_empty:
                out.append('')
            out.append(f'##### {stripped}')
            out.append('')
            prev_empty = True
            continue

        # Artikel X (alleenstaand) — ook VCF-formaat Art. 1.1.0.0.1.
        art_match = re.match(r'^(?:Artikel|Art\.)\s+([\d][\d./\w]*)\s*\.?\s*$', stripped)
        if art_match:
            art_num = art_match.group(1).rstrip('.')
            if not prev_empty:
                out.append('')
            out.append(f'## Art. {art_num}')
            out.append('')
            prev_empty = True
            continue

        # Artikel X met tekst erachter
        art_inline = re.match(r'^(?:Artikel|Art\.)\s+([\d][\d./\w]*\.?)\s+(.+)$', stripped)
        if art_inline:
            art_num = art_inline.group(1).rstrip('.')
            if not prev_empty:
                out.append('')
            out.append(f'## Art. {art_num}')
            out.append('')
            out.append(art_inline.group(2))
            prev_empty = False
            continue

        out.append(stripped)
        prev_empty = False

    text = '\n'.join(out)
    text = re.sub(r'(\w)-\n(\w)', r'\1\2', text)  # afgebroken woorden
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def make_header(cfg):
    return f"""---
tags: {cfg['tags']}
itaa-lex-sectie: "{cfg['itaa_sectie']}"
wet: "{cfg['wet']}"
status: "beschikbaar"
bijgewerkt: "{cfg['bijgewerkt']}"
bron: "Fisconetplus.be (officieuze gecoördineerde versie)"
---

# {cfg['titel']}

*Bijgewerkt tot en met {cfg['bijgewerkt']} — officieuze gecoördineerde versie. Bron: Fisconetplus.be.*

"""


def convert(name):
    cfg = CONFIGS[name]
    print(f"\n=== {name} ({cfg['input']}) ===")

    text = extract_nl_text(
        cfg['input'],
        cfg['mode'],
        cfg.get('start_page'),
        cfg.get('col_x', 300)
    )
    print(f"Tekst: {len(text)} tekens")

    md = clean_and_structure(text, cfg['wet'])
    art_count = len(re.findall(r'^## Art\.', md, re.MULTILINE))
    print(f"Artikelen: {art_count}")

    content = make_header(cfg) + md

    with open(cfg['output_resources'], 'w') as f:
        f.write(content)
    with open(cfg['output_content'], 'w') as f:
        f.write(content)

    print(f"Output: {cfg['output_resources']} + {cfg['output_content']}")
    return art_count


if __name__ == '__main__':
    targets = sys.argv[1:] if len(sys.argv) > 1 else list(CONFIGS.keys())
    for name in targets:
        if name not in CONFIGS:
            print(f"Onbekend: {name}. Beschikbaar: {list(CONFIGS.keys())}")
            continue
        convert(name)

    print("\nKlaar.")
