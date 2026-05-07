#!/usr/bin/env python3
"""
Generiek conversiescript voor Fisconet-PDFs naar gestructureerde NL markdown.
Ondersteunt:
  - NL-only PDFs (mode=nl)
  - Tweetalige NL/FR PDFs met twee-kolom layout (mode=bilingual)
"""

import subprocess, re, sys, os
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
YAML_PATH = ROOT / "resources" / "source_config.yaml"

sys.path.insert(0, str(ROOT / "tools"))
from lib.cleanup import (  # noqa: E402
    fix_broken_words,
    merge_heading_continuations,
    merge_wrapped_lines,
)


def load_wetboek_config(name):
    """Lees een wetboek-entry uit source_config.yaml en map naar het interne cfg-formaat."""
    with open(YAML_PATH) as f:
        cfg = yaml.safe_load(f)
    sources = cfg.get("sources", {})
    if name not in sources:
        return None
    entry = sources[name]
    if entry.get("type") != "wetboek":
        return None
    return {
        "name": name,
        "input": entry["raw"],
        "output_resources": entry["output"],
        "output_content": entry.get("content"),
        "mode": entry["mode"],
        "wet": entry["wet"],
        "titel": entry["titel"],
        "bijgewerkt": entry["bijgewerkt"],
        "itaa_sectie": entry["itaa_sectie"],
        "tags": entry["tags"],
        "col_x": entry.get("col_x"),
        "start_page": entry.get("start_page"),
    }


def all_wetboek_names():
    with open(YAML_PATH) as f:
        cfg = yaml.safe_load(f)
    return [k for k, v in cfg.get("sources", {}).items() if v.get("type") == "wetboek"]



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
    in_toc = False
    seen_toc = False  # eenmalig: alleen de eerste 'Inhoudstafel' is een TOC-start
    in_wijzigingsnota = False

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
        r'^Nota.*:$',
        r'^Copyright Belgisch',
        r'^Pagina \d+ van \d+',
        r'^Art\.\s+[\d][\d]*[-–,/]',  # fallback voor losstaande TOC-artikelranges
        r'^[-–—=]{3,}$',
        r'^\d+$',
        r'^[IVX]+/\d+\s*-?\s*$',  # paginanummers zoals "I/1 -"
        r'^-\s*[IVX]+/\d+\s*-$',
    ]

    for line in lines:
        stripped = line.strip()

        # Wijzigingsnota-blok (meerdere regels): skip tot blanco regel
        if in_wijzigingsnota:
            if not stripped:
                in_wijzigingsnota = False
                if not prev_empty:
                    out.append('')
                    prev_empty = True
            continue

        # Inhoudstafel-modus: alles skippen tot een eind-marker
        if in_toc:
            # Ejustice gebruikt 'Tekst' tussen TOC en inhoud
            if re.match(r'^Tekst$', stripped):
                in_toc = False
                continue
            # Fisconetplus stijl 1 (WBTW): 'kale' chapter heading op eigen regel
            if re.match(r'^HOOFDSTUK\s+[IVXLC]+(?:bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)?$', stripped):
                in_toc = False
                # doorvallen: dit is de eerste echte heading
            # Fisconetplus stijl 2 (Successierechten): 'BOEK X - Titel' / 'HOOFDSTUK X - Titel'
            # zonder leader-dots+paginanummer (TOC-entries hebben '....... 6' aan het eind).
            elif (re.match(r'^(?:BOEK|HOOFDSTUK)\s+[IVXLC]+\w*\s+-\s+\S', stripped)
                    and not re.search(r'\.{2,}', stripped)):
                in_toc = False
                # doorvallen
            else:
                continue

        if not stripped:
            if not prev_empty:
                out.append('')
            prev_empty = True
            continue

        # Begin van Inhoudstafel (eenmalig per document)
        if not seen_toc and re.match(r'^Inhoudstafel$', stripped, re.I):
            in_toc = True
            seen_toc = True
            continue

        # Wijzigingsnota-intro vlak na 'Artikel N': 'Art. N, ... werd/wordt/met ingang/B.S./Numac' →
        # opening + alle vervolgregels (over PDF-regelafbreking heen) skippen tot blanco regel.
        # Moet vóór de noise-filter staan, anders consumeert die de openingsregel zonder de
        # vervolgregels mee te nemen (zie Art. 1, Art. 53 in WBTW).
        if (re.match(r'^Art\.\s+\d+\w*\s*,', stripped)
                and re.search(r'\b(werd|wordt|met ingang|B\.S\.|Numac)\b', stripped)):
            in_wijzigingsnota = True
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
    text = fix_broken_words(text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = merge_wrapped_lines(text)
    text = merge_heading_continuations(text)
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
    text = fix_broken_words(text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = merge_wrapped_lines(text)
    text = merge_heading_continuations(text)
    return text.strip()


def make_header(cfg):
    wet = cfg['wet'].replace('"', '\\"')  # escape " als \" voor geldige YAML
    tags = cfg['tags']
    if isinstance(tags, list):
        tags_str = '[' + ', '.join(f'"{t}"' for t in tags) + ']'
    else:
        tags_str = tags
    return f"""---
tags: {tags_str}
itaa-lex-sectie: "{cfg['itaa_sectie']}"
wet: "{wet}"
status: "beschikbaar"
bijgewerkt: "{cfg['bijgewerkt']}"
bron: "Fisconetplus.be (officieuze gecoördineerde versie)"
---

# {cfg['titel']}

*Bijgewerkt tot en met {cfg['bijgewerkt']} — officieuze gecoördineerde versie. Bron: Fisconetplus.be.*

"""


def convert(name):
    cfg = load_wetboek_config(name)
    if cfg is None:
        raise KeyError(f"Geen wetboek-entry voor '{name}' in source_config.yaml")
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
    if cfg.get('output_content'):
        with open(cfg['output_content'], 'w') as f:
            f.write(content)
        print(f"Output: {cfg['output_resources']} + {cfg['output_content']}")
    else:
        print(f"Output: {cfg['output_resources']}")
    return art_count


if __name__ == '__main__':
    targets = sys.argv[1:] if len(sys.argv) > 1 else all_wetboek_names()
    for name in targets:
        try:
            convert(name)
        except KeyError as e:
            print(f"Onbekend: {e}")

    print("\nKlaar.")
