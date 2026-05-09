#!/usr/bin/env python3
"""
Conversiescript voor Oud-BW (Burgerlijk Wetboek vóór hervorming) vanuit
JUSTEL/ejustice-formaat PDF naar gestructureerde NL markdown.

Gebruik:
  python3 tools/etl/convert-oud-bw.py

Output:
  resources/bronnen/wetteksten/Oud-BW.md

Structurele heading-hiërarchie in de PDF:
  INLEIDENDE TITEL. / BOEK I.  →  ## BOEK I.
  TITEL I.                      →  ### TITEL I.
  HOOFDSTUK I.                  →  #### HOOFDSTUK I.
  AFDELING I. / Afdeling 1.    →  ##### AFDELING I.
  Onderafdeling 1.              →  ###### Onderafdeling 1.
  EERSTE DEEL. / TWEEDE DEEL.  →  ## EERSTE DEEL.
  Boek 8. / Boek X.            →  ## Boek 8.
  Art. X. / Artikel X.         →  ## Art. X
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from lib.cleanup import (  # noqa: E402
    fix_broken_words,
    merge_heading_continuations,
    merge_wrapped_lines,
)

PDF_PAD = ROOT / "resources" / "raw" / "wetteksten" / "Oud-BW.pdf"
OUTPUT_PAD = ROOT / "resources" / "bronnen" / "wetteksten" / "Oud-BW.md"

FRONTMATTER = """\
---
tags: ["XI"]
itaa-lex-sectie: "XI"
wet: "Burgerlijk Wetboek (oud, vóór hervormingen nieuwe Burgerlijk Wetboek 2019)"
status: "beschikbaar"
bijgewerkt: "27.01.2026"
bron: "ejustice.just.fgov.be (Justel, gecoördineerde versie)"
raw-bron: "resources/raw/wetteksten/Oud-BW.pdf"
---

# Burgerlijk Wetboek (oud)

*Bijgewerkt tot en met 27.01.2026 — officieuze gecoördineerde versie via JUSTEL. Bron: ejustice.just.fgov.be.*

"""

# Ruis-patronen (ejustice/JUSTEL-formaat)
RUIS_PATRONEN = [
    r"^JUSTEL\s*-\s*Geconsolideerde wetgeving",
    r"^http://www\.ejustice",
    r"^Copyright Belgisch",
    r"^Pagina \d+ van \d+",
    r"^[-–—=]{3,}$",
    r"^\d{4}-\d{2}-\d{2}/\d+\s*$",   # datum-codes zoals "1804-03-21/30"
    r"^Dossiernummer\s*:",
    r"^Situatie\s*:",
    r"^Publicatie\s*:",
    r"^Bron\s*:",
    r"^Inwerkingtreding\s*:",
    r"^Nota.*:\s*$",
    r"^\d+\s*$",
    r"^\(Opgeheven\)$",
]


def extraheer_tekst(pdf_pad: str) -> str:
    """Extraheer volledige tekst met pdftotext -layout (NL-only ejustice PDF)."""
    resultaat = subprocess.run(
        ["pdftotext", "-layout", pdf_pad, "-"],
        capture_output=True, text=True,
    )
    if resultaat.returncode != 0:
        raise RuntimeError(f"pdftotext mislukt: {resultaat.stderr}")
    return resultaat.stdout


def verwerk_tekst(tekst: str) -> str:
    """Converteer ruwe pdftotext-output naar gestructureerde markdown."""
    regels = tekst.split("\n")
    uitvoer: list[str] = []
    vorige_leeg = False
    in_inhoudsopgave = False
    inhoudsopgave_gezien = False

    for regel in regels:
        ontdaan = regel.strip()

        # ---------------------------------------------------------------
        # Inhoudsopgave: overslaan tot 'Tekst'-markering
        # ---------------------------------------------------------------
        if in_inhoudsopgave:
            # JUSTEL gebruikt 'Tekst' als scheidingslijn tussen TOC en inhoud
            if re.match(r"^Tekst$", ontdaan):
                in_inhoudsopgave = False
            continue

        # Lege regels
        if not ontdaan:
            if not vorige_leeg:
                uitvoer.append("")
            vorige_leeg = True
            continue

        # Start inhoudsopgave (alleen de eerste keer)
        if not inhoudsopgave_gezien and re.match(r"^Inhoudstafel$", ontdaan, re.I):
            in_inhoudsopgave = True
            inhoudsopgave_gezien = True
            continue

        # Ruis verwijderen
        if any(re.match(p, ontdaan, re.I) for p in RUIS_PATRONEN):
            continue

        # ---------------------------------------------------------------
        # Structurele headings
        # ---------------------------------------------------------------

        # INLEIDENDE TITEL → ## (top-niveau, gelijk aan BOEK)
        if re.match(r"^INLEIDENDE TITEL\.?\s*[-—]", ontdaan):
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"## {ontdaan}")
            uitvoer.append("")
            vorige_leeg = True
            continue

        # BOEK I. / BOEK II. etc. → ##
        if re.match(r"^BOEK\s+[IVXLCDM]+", ontdaan):
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"## {ontdaan}")
            uitvoer.append("")
            vorige_leeg = True
            continue

        # Boek 8. (Boek 8 Bewijs — nieuwe stijl) → ##
        if re.match(r"^Boek\s+\d+", ontdaan):
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"## {ontdaan}")
            uitvoer.append("")
            vorige_leeg = True
            continue

        # EERSTE DEEL. / TWEEDE DEEL. → ##
        if re.match(r"^(EERSTE|TWEEDE|DERDE|VIERDE) DEEL", ontdaan):
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"## {ontdaan}")
            uitvoer.append("")
            vorige_leeg = True
            continue

        # TITEL I. → ###
        if re.match(r"^TITEL\s+[IVXLCDM]+", ontdaan):
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"### {ontdaan}")
            uitvoer.append("")
            vorige_leeg = True
            continue

        # HOOFDSTUK I. → #### (ook Hoofdstuk X. lowercase — Boek 8 stijl)
        if re.match(r"^HOOFDSTUK\s+", ontdaan) or re.match(r"^Hoofdstuk\s+\d+", ontdaan):
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"#### {ontdaan}")
            uitvoer.append("")
            vorige_leeg = True
            continue

        # AFDELING I. / AFDELING 1. (uppercase) → #####
        if re.match(r"^AFDELING\s+", ontdaan):
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"##### {ontdaan}")
            uitvoer.append("")
            vorige_leeg = True
            continue

        # Afdeling 1. (mixed case) → #####
        if re.match(r"^Afdeling\s+", ontdaan):
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"##### {ontdaan}")
            uitvoer.append("")
            vorige_leeg = True
            continue

        # Onderafdeling 1. → ######
        if re.match(r"^Onderafdeling\s+", ontdaan):
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"###### {ontdaan}")
            uitvoer.append("")
            vorige_leeg = True
            continue

        # ---------------------------------------------------------------
        # Artikel-headings
        # ---------------------------------------------------------------

        # "Artikel X." of "Artikel X" als alleenstaande regel (geen verdere tekst)
        oud_artikel_match = re.match(r"^Artikel\s+([\d][\d./\w]*\.?)\s*$", ontdaan)
        if oud_artikel_match:
            art_nr = oud_artikel_match.group(1).rstrip(".")
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"## Art. {art_nr}")
            uitvoer.append("")
            vorige_leeg = True
            continue

        # Boek 8-stijl: "Art. 8.1.Definitietitel" — aaneengesloten zonder spatie
        # Voorbeeld: "Art. 8.1.Definities", "Art. 8.4.Regels die de bewijslast bepalen"
        # Ook: "Art. 8.2. Algemene regel" — artikelnummer eindigt op punt, titel volgt
        # MOET vóór de algemene art_inline_match staan (specifieke vorm eerst)
        art_b8_match = re.match(r"^Art\.\s+(8\.\d+(?:bis|ter|quater)?(?:/\d+)?)[.\s]+(.*)", ontdaan)
        if art_b8_match:
            art_nr = art_b8_match.group(1).rstrip(".")
            ondertitel = art_b8_match.group(2).strip()
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"## Art. {art_nr}")
            uitvoer.append("")
            if ondertitel:
                uitvoer.append(ondertitel)
            vorige_leeg = not bool(ondertitel)
            continue

        # "Art. X." of "Art. X" alleenstaand
        art_alleen_match = re.match(r"^Art\.\s+([\d][\d./\w]*\.?)\s*$", ontdaan)
        if art_alleen_match:
            art_nr = art_alleen_match.group(1).rstrip(".")
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"## Art. {art_nr}")
            uitvoer.append("")
            vorige_leeg = True
            continue

        # "Art. X. tekst..." of "Art. X.[noot]... tekst..."
        art_inline_match = re.match(
            r"^Art\.\s+([\d][\d./\w]*\.?)\s*(?:\[\d+.*?\]\d*\s*)?(.+)$",
            ontdaan,
        )
        if art_inline_match:
            art_nr = art_inline_match.group(1).rstrip(".")
            tekst_rest = art_inline_match.group(2).strip()
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"## Art. {art_nr}")
            uitvoer.append("")
            if tekst_rest:
                uitvoer.append(tekst_rest)
            vorige_leeg = not bool(tekst_rest)
            continue

        # "Artikel X. tekst..." met tekst erachter
        oud_inline_match = re.match(
            r"^Artikel\s+([\d][\d./\w]*\.?)\s+(.+)$",
            ontdaan,
        )
        if oud_inline_match:
            art_nr = oud_inline_match.group(1).rstrip(".")
            tekst_rest = oud_inline_match.group(2).strip()
            if not vorige_leeg:
                uitvoer.append("")
            uitvoer.append(f"## Art. {art_nr}")
            uitvoer.append("")
            if tekst_rest:
                uitvoer.append(tekst_rest)
            vorige_leeg = not bool(tekst_rest)
            continue

        # ---------------------------------------------------------------
        # Gewone tekstregel
        # ---------------------------------------------------------------
        uitvoer.append(ontdaan)
        vorige_leeg = False

    resultaat = "\n".join(uitvoer)
    resultaat = fix_broken_words(resultaat)
    resultaat = re.sub(r"\n{3,}", "\n\n", resultaat)
    resultaat = merge_wrapped_lines(resultaat)
    resultaat = merge_heading_continuations(resultaat)
    return resultaat.strip()


def main():
    if not PDF_PAD.exists():
        print(f"Fout: PDF niet gevonden: {PDF_PAD}")
        sys.exit(1)

    print(f"Extraheer tekst uit {PDF_PAD.name}...")
    ruwe_tekst = extraheer_tekst(str(PDF_PAD))
    print(f"  Ruwe tekst: {len(ruwe_tekst):,} tekens")

    print("Verwerk naar gestructureerde markdown...")
    inhoud = verwerk_tekst(ruwe_tekst)

    # Kwaliteitsmeting
    art_count = len(re.findall(r"^## Art\.", inhoud, re.MULTILINE))
    boek_count = len(re.findall(r"^## (BOEK|INLEIDENDE|EERSTE|TWEEDE|Boek)\b", inhoud, re.MULTILINE))
    titel_count = len(re.findall(r"^### TITEL\b", inhoud, re.MULTILINE))
    hfst_count = len(re.findall(r"^#### HOOFDSTUK\b", inhoud, re.MULTILINE))
    afd_count = len(re.findall(r"^##### (AFDELING|Afdeling)\b", inhoud, re.MULTILINE))
    plain_structuur = len(re.findall(
        r"^\s*(BOEK|TITEL|HOOFDSTUK)\s+[IVXLCDM0-9]", inhoud, re.MULTILINE
    ))

    print(f"  Artikelen (## Art.): {art_count}")
    print(f"  BOEK-headings (##): {boek_count}")
    print(f"  TITEL-headings (###): {titel_count}")
    print(f"  HOOFDSTUK-headings (####): {hfst_count}")
    print(f"  AFDELING-headings (#####): {afd_count}")
    print(f"  Resterende plain-text structuurlabels: {plain_structuur}  ← moet 0 zijn")

    # Kwaliteitscheck
    if art_count < 100:
        print(f"  WAARSCHUWING: slechts {art_count} artikelen — verwacht >1000")
    if plain_structuur > 0:
        print(f"  WAARSCHUWING: {plain_structuur} structuurlabels nog als plain text!")

    # Schrijf output
    OUTPUT_PAD.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PAD.write_text(FRONTMATTER + inhoud + "\n")
    print(f"\nGeschreven: {OUTPUT_PAD.relative_to(ROOT)}")
    print(f"Bestandsgrootte: {OUTPUT_PAD.stat().st_size:,} bytes")
    print(f"Regels: {OUTPUT_PAD.read_text().count(chr(10)):,}")


if __name__ == "__main__":
    main()
