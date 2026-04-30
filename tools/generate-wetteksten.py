#!/usr/bin/env python3
"""
Genereer content/wetteksten/ uit resources/wetteksten/*.md

Conversies per bronbestand:
1. Verwijder de Inhoudstafel-sectie (alles tussen "Inhoudstafel" en "Tekst")
2. Converteer **Art. X. text** → ## Art. X\n\ntext  (ankernamen: #art-x)
3. Demotion structuurheadings zodat ## Art. domineert:
   # BOEK → ### BOEK
   ## TITEL / Hoofdstuk → #### TITEL
   ### HOOFDSTUK → ##### HOOFDSTUK
   #### Afdeling → **Afdeling** (bold)
   ##### Onderafdeling → *Onderafdeling* (cursief)
4. Schrijf frontmatter en header
5. WER: split per Boek in aparte bestanden
"""

import re
import os
import sys
from pathlib import Path

RESOURCES = Path(__file__).parent.parent / "resources" / "wetteksten"
CONTENT = Path(__file__).parent.parent / "content" / "wetteksten"

# ---------------------------------------------------------------------------
# Configuratie per bronbestand
# ---------------------------------------------------------------------------

MAPPING = [
    {
        "source": "Antiwitwaswet-2017.md",
        "output": "XVII-antiwitwaswet.md",
        "itaa_sectie": "XVII",
        "afkorting": "AWW",
        "wet": "Wet 18 september 2017 tot voorkoming van het witwassen van geld en de financiering van terrorisme en tot beperking van het gebruik van contanten",
        "online": "https://www.ejustice.just.fgov.be/eli/wet/2017/09/18/2017013368/justel",
        "status": "gecoördineerd t.e.m. 24-12-2025",
        "itaa_pagina": "p. 2441",
    },
    {
        "source": "Wet-ITAA-2019.md",
        "output": "XXI-wet-itaa.md",
        "itaa_sectie": "XXI",
        "afkorting": "Wet ITAA",
        "wet": "Wet 17 maart 2019 betreffende de beroepen van accountant en belastingadviseur",
        "online": "https://www.ejustice.just.fgov.be/eli/wet/2019/03/17/2019040490/justel",
        "status": "gecoördineerd",
        "itaa_pagina": "p. 2593",
    },
    {
        "source": "WVV.md",
        "output": "XV-wvv.md",
        "itaa_sectie": "XV",
        "afkorting": "WVV",
        "wet": "Wetboek 23 maart 2019 van vennootschappen en verenigingen",
        "online": "https://www.ejustice.just.fgov.be/eli/wet/2019/03/23/2019040586/justel",
        "status": "gecoördineerd",
        "itaa_pagina": "p. 2089",
    },
    {
        "source": "KB-WVV-2019.md",
        "output": "XV-KB-wvv.md",
        "itaa_sectie": "XV (KB)",
        "afkorting": "KB WVV 2019",
        "wet": "Koninklijk besluit 29 april 2019 tot uitvoering van het Wetboek van vennootschappen en verenigingen",
        "online": "https://www.ejustice.just.fgov.be/eli/besluit/2019/04/29/2019011359/justel",
        "status": "gecoördineerd",
        "itaa_pagina": "p. 2316",
    },
    {
        "source": "VCF.md",
        "output": "IVA-vcf.md",
        "itaa_sectie": "IV.A",
        "afkorting": "VCF",
        "wet": "Decreet 13 december 2013 houdende de Vlaamse Codex Fiscaliteit",
        "online": "https://www.ejustice.just.fgov.be/eli/decreet/2013/12/13/2013036154/justel",
        "status": "gecoördineerd t.e.m. 31-12-2025",
        "itaa_pagina": "p. 593",
    },
    {
        "source": "VII-wetboek-invordering.md",
        "output": "VII-wetboek-invordering.md",
        "itaa_sectie": "VII",
        "afkorting": "WInv",
        "wet": "Wetboek 13 april 2019 van de minnelijke en gedwongen invordering van fiscale en niet-fiscale schuldvorderingen",
        "online": "https://www.ejustice.just.fgov.be/img_l/pdf/2019/04/13/2019A41000_N.pdf",
        "status": "gecoördineerd",
        "itaa_pagina": "p. 1247",
    },
    {
        "source": "WDRT.md",
        "output": "V-wdrt.md",
        "itaa_sectie": "V",
        "afkorting": "WDRT",
        "wet": "Wetboek 2 maart 1927 van de diverse rechten en taksen",
        "online": "https://www.ejustice.just.fgov.be/img_l/pdf/1927/03/02/1927030201_N.pdf",
        "status": "gecoördineerd",
        "itaa_pagina": "p. 821",
    },
    {
        "source": "Oud-BW.md",
        "output": "XI-oud-bw.md",
        "itaa_sectie": "XI (oud)",
        "afkorting": "Oud BW",
        "wet": "Wet 21 maart 1804 Oud Burgerlijk Wetboek",
        "online": "https://www.ejustice.just.fgov.be/img_l/pdf/1804/03/21/1804032150M_N.pdf",
        "status": "gecoördineerd",
        "itaa_pagina": "p. 1683",
    },
    {
        "source": "KB-WIB92.md",
        "output": "II-KB-wib92.md",
        "itaa_sectie": "II (KB)",
        "afkorting": "KB/WIB92",
        "wet": "Koninklijk besluit 27 augustus 1993 tot uitvoering van het Wetboek van de inkomstenbelastingen 1992",
        "online": "https://www.ejustice.just.fgov.be/img_l/pdf/1993/08/27/1993082751_N.pdf",
        "status": "gecoördineerd",
        "itaa_pagina": "p. 386",
    },
    {
        "source": "KB-21-10-2018.md",
        "output": "XIII-KB-wer-boekhouding.md",
        "itaa_sectie": "XIII (KB)",
        "afkorting": "KB WER 2018",
        "wet": "Koninklijk besluit 21 oktober 2018 tot uitvoering van de artikelen III.82 tot en met III.95 van het Wetboek van economisch recht",
        "online": "https://www.ejustice.just.fgov.be/mopdf/2018/10/29_1.pdf",
        "status": "in gebruik",
        "itaa_pagina": "p. 2054",
    },
    {
        "source": "Richtlijn-2013-34-EU.md",
        "output": "EU-richtlijn-2013-34.md",
        "itaa_sectie": "EU",
        "afkorting": "Richtlijn 2013/34/EU",
        "wet": "Richtlijn 2013/34/EU van het Europees Parlement en de Raad van 26 juni 2013 betreffende de jaarlijkse financiële overzichten",
        "online": "https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:02013L0034-20240528",
        "status": "gecoördineerd t.e.m. 28-05-2024",
        "itaa_pagina": "niet in ITAA-LEX",
    },
]

# WER wordt apart afgehandeld (split per Boek)
WER_CONFIG = {
    "source": "WER.md",
    "output_dir": "XIII-wer",
    "itaa_sectie": "XIII",
    "afkorting": "WER",
    "wet": "Wetboek van Economisch Recht (wet 28 februari 2013)",
    "online": "https://www.ejustice.just.fgov.be/img_l/pdf/2013/02/28/2013A11134_N.pdf",
    "status": "gecoördineerd",
    "itaa_pagina": "p. 1859",
}


# ---------------------------------------------------------------------------
# Hulpfuncties
# ---------------------------------------------------------------------------

def extract_actual_text(content: str) -> tuple[str, str]:
    """
    Splits het bestand in (header, tekst).
    - header: alles vóór "Inhoudstafel"
    - tekst: alles na "Tekst" (de eigenlijke wettekst, zonder TOC)
    """
    lines = content.split('\n')

    # Vind "Tekst" als standalone regel
    tekst_idx = None
    for i, line in enumerate(lines):
        if line.strip() == 'Tekst':
            tekst_idx = i
            break

    if tekst_idx is None:
        # Fallback: geen "Tekst" label gevonden → gebruik de hele tekst
        return '', content

    # Header: alles vóór "Inhoudstafel"
    header_lines = []
    for line in lines:
        if line.strip() == 'Inhoudstafel':
            break
        header_lines.append(line)

    return '\n'.join(header_lines).strip(), '\n'.join(lines[tekst_idx + 1:]).strip()


def convert_articles(text: str, artikel_keyword: str = 'Art') -> str:
    """
    Converteer **Art. X. tekst** → ## Art. X\n\ntekst
    Verwerkt ook EU **Artikel X** formaat.
    """
    lines = text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # Patroon 1: **Art. NUMBER.body** — body start na de scheidingsperiode
        # "Art." of "Artikel" (punt na "Artikel" is optioneel) gevolgd door nummer en scheidingspunt
        # Handles: **Art. 47. § 1. tekst**, **Art. 5.§ 1. tekst**, **Artikel 1.§ 1. tekst**
        # Body moet starten met \s, §, of [ om inline verwijzingen niet te converteren
        m = re.match(
            r'^\*\*(?:Art|Artikel)\.?\s+([\d\.:/A-Za-z]+?)\.([\s§\[].+?)\*\*\s*$',
            line
        )
        if m:
            art_num = m.group(1).rstrip('.')
            rest = m.group(2).strip()
            result.append(f'\n## Art. {art_num}')
            if rest:
                result.append(f'\n{rest}')
            i += 1
            continue

        # Patroon 1b: fallback voor body die niet met §/[/spatie begint
        m1b = re.match(
            r'^\*\*(?:Art|Artikel)\.?\s+([\d\.:/A-Za-z]+?)\.((?:[^\s§\[]).+?)\*\*\s*$',
            line
        )
        if m1b:
            art_num = m1b.group(1).rstrip('.')
            rest = m1b.group(2).strip()
            result.append(f'\n## Art. {art_num}')
            if rest:
                result.append(f'\n{rest}')
            i += 1
            continue

        # Patroon 2: **Art. NUMBER** standalone (geen tekst na het nummer)
        m2 = re.match(r'^\*\*(?:Art|Artikel)\.?\s+([\d\.:/A-Za-z]+?)\.?\*\*\s*$', line)
        if m2:
            art_num = m2.group(1).rstrip('.')
            result.append(f'\n## Art. {art_num}')
            i += 1
            continue

        # Patroon 3: EU **Artikel X** (alleen getal, geen punt)
        m3 = re.match(r'^\*\*Artikel\s+(\d+)\*\*\s*$', line)
        if m3:
            result.append(f'\n## Art. {m3.group(1)}')
            i += 1
            continue

        result.append(line)
        i += 1

    return '\n'.join(result)


def demote_structural_headings(text: str) -> str:
    """
    Demotion zodat ## Art. X het dominante heading-niveau is:
    # BOEK      → ### BOEK
    ## TITEL    → #### TITEL
    ### HFST    → ##### HFST
    #### Afd    → **Afd** (bold)
    ##### Ond   → *Ond* (cursief)
    """
    lines = text.split('\n')
    result = []
    for line in lines:
        if re.match(r'^##### ', line):
            line = '*' + line[6:].strip() + '*'
        elif re.match(r'^#### ', line):
            line = '**' + line[5:].strip() + '**'
        elif re.match(r'^### ', line):
            line = '##### ' + line[4:]
        elif re.match(r'^## (TITEL|Hoofdstuk|AFDELING)', line, re.IGNORECASE):
            line = '#### ' + line[3:]
        elif re.match(r'^# BOEK|^# TITEL|^# HOOFDSTUK|^# DEEL|^# Deel|^# Boek', line, re.IGNORECASE):
            line = '### ' + line[2:]
        result.append(line)
    return '\n'.join(result)


def clean_text(text: str) -> str:
    """Verwijder resterende JUSTEL artifacts en normaliseer witruimte."""
    # Verwijder paginakoppen
    text = re.sub(r'^Pagina\s+\d+\s+van\s+\d+.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^JUSTEL\s+-\s+Geconsolideerde.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^http://www\.ejustice.*$', '', text, flags=re.MULTILINE)
    # Normaliseer meerdere lege regels
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text.strip()


def make_frontmatter(cfg: dict) -> str:
    return f"""---
tags: [wettekst, "{cfg['itaa_sectie']}"]
itaa-lex-sectie: "{cfg['itaa_sectie']}"
afkorting: {cfg['afkorting']}
wet: "{cfg['wet']}"
status: {cfg['status']}
online: {cfg['online']}
---"""


def make_header(cfg: dict) -> str:
    sectie = cfg['itaa_sectie']
    afk = cfg['afkorting']
    wet_kort = cfg['wet'][:60] + ('...' if len(cfg['wet']) > 60 else '')
    return f"""# ITAA-LEX {sectie} — {afk}

[Online raadplegen]({cfg['online']}) · ejustice.just.fgov.be

**{cfg['wet']}**

Situatie: {cfg['status']}.

---
"""


def process_file(cfg: dict) -> str:
    """Verwerk één bronbestand naar Quartz-content."""
    source_path = RESOURCES / cfg['source']
    if not source_path.exists():
        # Alternatieve naam proberen
        alt = cfg.get('source_alt')
        if alt:
            source_path = RESOURCES / alt
        if not source_path.exists():
            print(f"  ⚠️  Niet gevonden: {cfg['source']}")
            return None

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    header_text, actual_text = extract_actual_text(content)
    actual_text = convert_articles(actual_text)
    actual_text = demote_structural_headings(actual_text)
    actual_text = clean_text(actual_text)

    frontmatter = make_frontmatter(cfg)
    header = make_header(cfg)
    return f"{frontmatter}\n\n{header}\n{actual_text}\n"


def process_wer(cfg: dict) -> dict[str, str]:
    """
    Verwerk WER: split per Boek.
    Geeft dict: {filename: content}
    """
    source_path = RESOURCES / cfg['source']
    if not source_path.exists():
        print(f"  ⚠️  Niet gevonden: {cfg['source']}")
        return {}

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    _, actual_text = extract_actual_text(content)

    # Split op Boek-headings (# BOEK)
    # Voeg een marker toe zodat we kunnen splitsen
    actual_text = re.sub(r'^(# BOEK .+)$', r'\n<<<SPLIT>>>\1', actual_text, flags=re.MULTILINE)
    parts = actual_text.split('\n<<<SPLIT>>>')

    results = {}

    # Index-pagina
    index_lines = [
        make_frontmatter(cfg),
        f"\n\n# ITAA-LEX XIII — WER (Wetboek van Economisch Recht)",
        f"\n[Online raadplegen]({cfg['online']}) · ejustice.just.fgov.be\n",
        f"\n**{cfg['wet']}**\n",
        f"\nSituatie: {cfg['status']}.\n",
        "\n---\n",
        "\n## Boeken\n",
    ]

    boek_count = 0
    for part in parts:
        part = part.strip()
        if not part:
            continue

        # Haal de boektitel op
        boek_match = re.match(r'^# BOEK\s+(\S+)', part, re.IGNORECASE)
        if boek_match:
            boek_nr = boek_match.group(1).rstrip('.')
            boek_nr_clean = boek_nr.lower().replace(' ', '-')
            filename = f"boek-{boek_nr_clean}.md"
            boek_titel = part.split('\n')[0].lstrip('# ').strip()

            index_lines.append(f"- [[XIII-wer/{filename.replace('.md', '')}|{boek_titel}]]\n")

            # Verwerk de Boek-inhoud
            boek_content = convert_articles(part)
            boek_content = demote_structural_headings(boek_content)
            boek_content = clean_text(boek_content)

            boek_cfg = {**cfg, 'itaa_sectie': f'XIII — {boek_titel[:30]}'}
            frontmatter = make_frontmatter({**cfg, 'itaa_sectie': 'XIII'})
            full_content = f"{frontmatter}\n\n{boek_content}\n"
            results[filename] = full_content
            boek_count += 1
        else:
            # Introductie-tekst vóór het eerste Boek
            if boek_count == 0 and part:
                index_lines.append(f"\n{part}\n")

    results['index.md'] = '\n'.join(index_lines)
    print(f"  WER gesplitst in {boek_count} Boeken")
    return results


def make_placeholder(sectie: str, wet: str, bs: str, pagina: str, ejustice_url: str = None) -> str:
    """Maak een placeholder-pagina voor een ontbrekende wettekst."""
    tags_str = f'[wettekst, "{sectie}", ontbrekend]'
    online_str = ejustice_url or f"https://www.ejustice.just.fgov.be"
    return f"""---
tags: {tags_str}
itaa-lex-sectie: "{sectie}"
wet: "{wet}"
status: "⏳ tekst nog niet beschikbaar"
online: {online_str}
---

# ITAA-LEX {sectie}

**{wet}**

> [!warning] Tekst niet beschikbaar
>
> De gecoördineerde tekst van deze wet is nog niet lokaal beschikbaar.
>
> **Publicatie**: {bs} — ITAA-LEX {pagina}
>
> [Online raadplegen]({online_str}) · ejustice.just.fgov.be
>
> Zie ook: [[../resources/wetteksten/status|Status wetteksten]] voor instructies om deze wet toe te voegen.
"""


# ---------------------------------------------------------------------------
# Placeholders voor ontbrekende wetten (volledige ITAA-LEX index)
# ---------------------------------------------------------------------------

PLACEHOLDERS = [
    {
        "output": "I-voorafgaande-beslissingen.md",
        "sectie": "I",
        "wet": "Wet 24 december 2002 — systeem van voorafgaande beslissingen in fiscale zaken",
        "bs": "B.S. 31 december 2002",
        "pagina": "p. 1",
        "url": "https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&cn=2002122430&table_name=wet",
    },
    {
        "output": "II-wib92.md",
        "sectie": "II",
        "wet": "Wetboek 10 april 1992 van de inkomstenbelastingen 1992 (WIB92)",
        "bs": "B.S. 30 juli 1992",
        "pagina": "p. 5",
        "url": "https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&cn=1992041032&table_name=wet",
    },
    {
        "output": "III-wigb.md",
        "sectie": "III",
        "wet": "KB 23 november 1965 — Wetboek van de met de inkomstenbelastingen gelijkgestelde belastingen (WIGB)",
        "bs": "B.S. 18 januari 1966",
        "pagina": "p. 529",
        "url": "https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&table_name=wet",
    },
    {
        "output": "IVB-brussel-fiscale-procedure.md",
        "sectie": "IV.B",
        "wet": "Ordonnantie 6 maart 2019 betreffende de Brusselse Codex Fiscale Procedure",
        "bs": "B.S. 19 maart 2019",
        "pagina": "p. 771",
        "url": "https://www.ejustice.just.fgov.be",
    },
    {
        "output": "IVC-waals-gewestelijke-belastingen.md",
        "sectie": "IV.C",
        "wet": "Decreet W.R. 6 mei 1999 betreffende de vestiging, invordering en geschillen inzake directe gewestelijke belastingen",
        "bs": "B.S. 1 juli 1999",
        "pagina": "p. 791",
        "url": "https://www.ejustice.just.fgov.be",
    },
    {
        "output": "VIA-wbtw.md",
        "sectie": "VI.A",
        "wet": "Wet 3 juli 1969 — Wetboek van de belasting over de toegevoegde waarde (WBTW)",
        "bs": "B.S. 17 juli 1969",
        "pagina": "p. 865",
        "url": "https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&nm=1969070305&table_name=titel",
    },
    {
        "output": "VIII-registratierechten.md",
        "sectie": "VIII",
        "wet": "KB nr. 64, 30 november 1939 — Wetboek van registratie-, hypotheek- en griffierechten",
        "bs": "B.S. 1 december 1939",
        "pagina": "p. 1273",
        "url": "https://www.ejustice.just.fgov.be",
    },
    {
        "output": "IX-successierechten.md",
        "sectie": "IX",
        "wet": "KB nr. 308, 31 maart 1936 — Wetboek der successierechten",
        "bs": "B.S. 7 april 1936",
        "pagina": "p. 1445",
        "url": "https://www.ejustice.just.fgov.be",
    },
    {
        "output": "X-eu-belastingen.md",
        "sectie": "X",
        "wet": "Europese en internationale belastingen (moeder-dochterrichtlijn, interest/royalties, fusierichtlijn, modelverdrag OESO)",
        "bs": "diverse publicaties",
        "pagina": "p. 1557",
        "url": "https://eur-lex.europa.eu",
    },
    {
        "output": "XI-bw-2019.md",
        "sectie": "XI",
        "wet": "Wetboek 13 april 2019 Burgerlijk Wetboek",
        "bs": "B.S. 14 mei 2019",
        "pagina": "p. 1581",
        "url": "https://www.ejustice.just.fgov.be",
    },
    {
        "output": "XII-strafwetboek.md",
        "sectie": "XII",
        "wet": "Wet 8 juni 1867 Strafwetboek + Wetboek 29 februari 2024 Strafwetboek 2024",
        "bs": "B.S. 9 juni 1867 / B.S. 8 april 2024",
        "pagina": "p. 1855",
        "url": "https://www.ejustice.just.fgov.be",
    },
    {
        "output": "XIV-betalingsachterstand.md",
        "sectie": "XIV",
        "wet": "Wet 2 augustus 2002 betreffende de bestrijding van de betalingsachterstand bij handelstransacties",
        "bs": "B.S. 7 augustus 2002",
        "pagina": "p. 2085",
        "url": "https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&table_name=wet",
    },
    {
        "output": "XVI-arbeidsovereenkomsten.md",
        "sectie": "XVI",
        "wet": "Wet 3 juli 1978 betreffende de arbeidsovereenkomsten",
        "bs": "B.S. 22 augustus 1978",
        "pagina": "p. 2403",
        "url": "https://www.ejustice.just.fgov.be",
    },
    {
        "output": "XVIII-klokkenluiders.md",
        "sectie": "XVIII",
        "wet": "Wet 28 november 2022 betreffende de bescherming van melders van inbreuken (klokkenluiderswet)",
        "bs": "B.S. 15 december 2022",
        "pagina": "p. 2495",
        "url": "https://www.ejustice.just.fgov.be",
    },
    {
        "output": "XIX-avg.md",
        "sectie": "XIX",
        "wet": "Verordening (EU) 2016/679 — Algemene Verordening Gegevensbescherming (AVG/GDPR)",
        "bs": "PB.L 119, 4 mei 2016",
        "pagina": "p. 2507",
        "url": "https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:32016R0679",
    },
    {
        "output": "XX-eu-beroepskwalificaties.md",
        "sectie": "XX",
        "wet": "Wet 12 februari 2008 tot instelling van een algemeen kader voor de erkenning van EU-beroepskwalificaties",
        "bs": "B.S. 2 april 2008",
        "pagina": "p. 2575",
        "url": "https://www.ejustice.just.fgov.be",
    },
]


# ---------------------------------------------------------------------------
# Hoofd-uitvoering
# ---------------------------------------------------------------------------

def main():
    CONTENT.mkdir(parents=True, exist_ok=True)

    # Verwerk bestanden met beschikbare tekst
    print("\n=== Verwerking bronbestanden ===")
    generated = []
    for cfg in MAPPING:
        # Correctie voor bestandsnaam die anders is
        source_name = cfg['source']
        if source_name == "VII-wetboek-invordering.md":
            cfg = {**cfg, 'source': 'Wetboek-Invordering.md'}

        output_path = CONTENT / cfg['output']
        print(f"  {cfg['source']} → {cfg['output']}")
        content = process_file(cfg)
        if content:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            generated.append(cfg['output'])
            print(f"    ✓ {len(content)//1024}KB")
        else:
            print(f"    ✗ Overgeslagen (bronbestand niet gevonden)")

    # Verwerk WER (split per Boek)
    print(f"\n  {WER_CONFIG['source']} → {WER_CONFIG['output_dir']}/ (split per Boek)")
    wer_dir = CONTENT / WER_CONFIG['output_dir']
    wer_dir.mkdir(exist_ok=True)
    wer_parts = process_wer(WER_CONFIG)
    for filename, content in wer_parts.items():
        out_path = wer_dir / filename
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"    ✓ {WER_CONFIG['output_dir']}/{filename} ({len(content)//1024}KB)")

    # Maak placeholders
    print("\n=== Placeholders voor ontbrekende wetten ===")
    for ph in PLACEHOLDERS:
        out_path = CONTENT / ph['output']
        content = make_placeholder(ph['sectie'], ph['wet'], ph['bs'], ph['pagina'], ph.get('url'))
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ⏳ {ph['output']}")

    print(f"\n✅ Klaar. Bestanden geschreven naar {CONTENT}")
    print(f"   {len(generated)} wetteksten + {len(wer_parts)} WER-bestanden + {len(PLACEHOLDERS)} placeholders")


if __name__ == '__main__':
    main()
