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
        'input': 'resources/raw/wetteksten/WBTW-2026.pdf',
        'output_resources': 'resources/bronnen/wetteksten/WBTW.md',
        'output_content': 'content/bronnen/wetteksten/VIA-wbtw.md',
        'mode': 'nl',
        'itaa_sectie': 'VI.A',
        'wet': 'Wet 3 juli 1969 tot invoering van het Wetboek van de belasting over de toegevoegde waarde (WBTW)',
        'bijgewerkt': '19.12.2025',
        'titel': 'Wetboek van de Belasting over de Toegevoegde Waarde (WBTW)',
        'tags': '["VI.A"]',
    },
    'reg-brussel': {
        'input': 'resources/raw/wetteksten/Registratierechten-Brussel.pdf',
        'output_resources': 'resources/bronnen/wetteksten/Registratierechten-Brussel.md',
        'output_content': 'content/bronnen/wetteksten/VIII-registratierechten-brussel.md',
        'mode': 'nl',
        'itaa_sectie': 'VIII',
        'wet': 'Wetboek der Registratie-, Hypotheek- en Griffierechten — Brussels Hoofdstedelijk Gewest',
        'bijgewerkt': '16.03.2026',
        'titel': 'Registratierechten — Brussels Hoofdstedelijk Gewest',
        'tags': '["VIII", "2.6"]',
    },
    'reg-waals': {
        'input': 'resources/raw/wetteksten/Registratierechten-Waals.pdf',
        'output_resources': 'resources/bronnen/wetteksten/Registratierechten-Waals.md',
        'output_content': 'content/bronnen/wetteksten/VIII-registratierechten-waals.md',
        'mode': 'nl',
        'itaa_sectie': 'VIII',
        'wet': 'Wetboek der Registratie-, Hypotheek- en Griffierechten — Waals Gewest',
        'bijgewerkt': '16.03.2026',
        'titel': 'Registratierechten — Waals Gewest',
        'tags': '["VIII", "2.6"]',
    },
    'successie-brussel': {
        'input': 'resources/raw/wetteksten/successie-brussel.pdf',
        'output_resources': 'resources/bronnen/wetteksten/Successierechten-Brussel.md',
        'output_content': 'content/bronnen/wetteksten/IX-successierechten-brussel.md',
        'mode': 'nl',
        'itaa_sectie': 'IX',
        'wet': 'Wetboek der Successierechten — Brussels Hoofdstedelijk Gewest',
        'bijgewerkt': '16.03.2026',
        'titel': 'Successierechten — Brussels Hoofdstedelijk Gewest',
        'tags': '["IX", "2.6"]',
    },
    'successie-waals': {
        'input': 'resources/raw/wetteksten/successie-waals.pdf',
        'output_resources': 'resources/bronnen/wetteksten/Successierechten-Waals.md',
        'output_content': 'content/bronnen/wetteksten/IX-successierechten-waals.md',
        'mode': 'nl',
        'itaa_sectie': 'IX',
        'wet': 'Wetboek der Successierechten — Waals Gewest',
        'bijgewerkt': '16.03.2026',
        'titel': 'Successierechten — Waals Gewest',
        'tags': '["IX", "2.6"]',
    },
    'successie-federaal': {
        'input': 'resources/raw/wetteksten/successie-federaal.pdf',
        'output_resources': 'resources/bronnen/wetteksten/Successierechten-federaal.md',
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
        'input': 'resources/raw/wetteksten/VCF-2026.pdf',
        'output_resources': 'resources/bronnen/wetteksten/VCF.md',
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
        'input': 'resources/raw/wetteksten/Registratierechten-federaal.pdf',
        'output_resources': 'resources/bronnen/wetteksten/Registratierechten-federaal.md',
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
        'input': 'resources/raw/wetteksten/Brusselse-Codex-Fiscale-Procedure.pdf',
        'output_resources': 'resources/bronnen/wetteksten/Brusselse-Codex-Fiscale-Procedure.md',
        'output_content': 'content/bronnen/wetteksten/IVB-brusselse-codex-fiscale-procedure.md',
        'mode': 'nl',
        'itaa_sectie': 'IV.B',
        'wet': 'Ordonnantie 6 maart 2019 betreffende de Brusselse Codex Fiscale Procedure',
        'bijgewerkt': '04.06.2024',
        'titel': 'Brusselse Codex Fiscale Procedure',
        'tags': '["IV.B", "2.5"]',
    },
    'decr-waals-belastingen': {
        'input': 'resources/raw/wetteksten/Decr-Waals-Directe-Belastingen.pdf',
        'output_resources': 'resources/bronnen/wetteksten/Decr-Waals-Directe-Belastingen.md',
        'output_content': 'content/bronnen/wetteksten/IVC-decr-waals-directe-belastingen.md',
        'mode': 'nl',
        'itaa_sectie': 'IV.C',
        'wet': 'Decreet 6 mei 1999 betreffende de vestiging, de invordering en de geschillen inzake de Waalse gewestelijke belastingen',
        'bijgewerkt': '03.02.2026',
        'titel': 'Decreet Waalse gewestelijke belastingen',
        'tags': '["IV.C", "2.5"]',
    },
    'eu-moeder-dochter': {
        'input': 'resources/raw/wetteksten/EU-Richtlijn-moeder-dochter-2011-96.pdf',
        'output_resources': 'resources/bronnen/wetteksten/EU-Richtlijn-moeder-dochter-2011-96.md',
        'output_content': 'content/bronnen/wetteksten/X-eu-richtlijn-moeder-dochter.md',
        'mode': 'eu_richtlijn',
        'itaa_sectie': 'X',
        'wet': 'Richtlijn 2011/96/EU van de Raad van 30 november 2011 betreffende de gemeenschappelijke fiscale regeling voor moedermaatschappijen en dochterondernemingen uit verschillende lidstaten',
        'bijgewerkt': '29.12.2011',
        'titel': 'Moeder-dochterrichtlijn 2011/96/EU',
        'tags': '["X", "2.8"]',
    },
    'eu-fusie': {
        'input': 'resources/raw/wetteksten/EU-Richtlijn-fusie-2009-133.pdf',
        'output_resources': 'resources/bronnen/wetteksten/EU-Richtlijn-fusie-2009-133.md',
        'output_content': 'content/bronnen/wetteksten/X-eu-richtlijn-fusie.md',
        'mode': 'eu_richtlijn',
        'itaa_sectie': 'X',
        'wet': 'Richtlijn 2009/133/EG van de Raad van 19 oktober 2009 betreffende de gemeenschappelijke fiscale regeling voor fusies, splitsingen, gedeeltelijke splitsingen, inbreng van activa en aandelenruil (gecodificeerde versie)',
        'bijgewerkt': '25.11.2009',
        'titel': 'Fusierichtlijn 2009/133/EG',
        'tags': '["X", "2.8"]',
    },
    'eu-interest-royalties': {
        'input': 'resources/raw/wetteksten/EU-Richtlijn-interest-royalties-2003-49.pdf',
        'output_resources': 'resources/bronnen/wetteksten/EU-Richtlijn-interest-royalties-2003-49.md',
        'output_content': 'content/bronnen/wetteksten/X-eu-richtlijn-interest-royalties.md',
        'mode': 'eu_richtlijn',
        'itaa_sectie': 'X',
        'wet': 'Richtlijn 2003/49/EG van de Raad van 3 juni 2003 betreffende een gemeenschappelijke belastingregeling inzake uitkeringen van interest en royalty\'s tussen verbonden ondernemingen van verschillende lidstaten',
        'bijgewerkt': '26.06.2003',
        'titel': 'Interest- en royalty\'srichtlijn 2003/49/EG',
        'tags': '["X", "2.8"]',
    },
}


def extract_nl_text(pdf, mode, start_page=None, col_x=300):
    info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    pages_match = re.search(r'Pages:\s+(\d+)', info)
    total_pages = int(pages_match.group(1)) if pages_match else 300

    if mode == 'eu_richtlijn':
        # Official Journal PDFs: twee-kolom layout, gebruik pdftotext zonder -layout
        r = subprocess.run(['pdftotext', pdf, '-'], capture_output=True, text=True)
        return r.stdout
    elif mode == 'nl':
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


def clean_and_structure_eu(text):
    """Structureert EU Official Journal richtlijntekst naar markdown."""
    lines = text.split('\n')
    out = []
    prev_empty = False

    eu_noise = [
        r'^L\s+\d+/\d+\s*$',                          # paginareferentie "L 157/49"
        r'^NL\s*$',
        r'^Publicatieblad van de Europese Unie',
        r'^\d{1,2}\.\d{1,2}\.\d{4}\s*$',             # datum "26.6.2003"
        r'^\(\d+\)\s*$',                               # losse voetnootnummers
        r'^C\d+/\d+\s*$',
    ]

    for line in lines:
        stripped = line.strip()

        if not stripped:
            if not prev_empty:
                out.append('')
            prev_empty = True
            continue

        if any(re.match(p, stripped) for p in eu_noise):
            continue

        # "Artikel X" alleen op een regel → ## Artikel X
        if re.match(r'^Artikel\s+\d+\s*$', stripped):
            num = re.match(r'^Artikel\s+(\d+)', stripped).group(1)
            if not prev_empty:
                out.append('')
            out.append(f'## Artikel {num}')
            out.append('')
            prev_empty = True
            continue

        # BIJLAGE
        if re.match(r'^BIJLAGE', stripped):
            if not prev_empty:
                out.append('')
            out.append(f'## {stripped}')
            out.append('')
            prev_empty = True
            continue

        # Overwegende-paragrafen: "(1) Tekst..." blijven gewone alinea's
        out.append(stripped)
        prev_empty = False

    text = '\n'.join(out)
    # Verbind afgebroken woorden (koppelteken aan regelende)
    text = re.sub(r'(\w)-\n(\w)', r'\1\2', text)
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

    if cfg['mode'] == 'eu_richtlijn':
        md = clean_and_structure_eu(text)
        art_count = len(re.findall(r'^## Artikel\b', md, re.MULTILINE))
    else:
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
