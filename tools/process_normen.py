#!/usr/bin/env python3
"""
Verwerk ITAA normen:
1. Lees resources/normen/*.md
2. Decode HTML entities
3. Verwijder TOC-ruis (regels met "....") en losse paginanummers
4. Voeg rijke frontmatter toe (naam, datum, toepassingsgebied, themas, itaa-lex-sectie)
5. Schrijf naar content/bronnen/normen/
6. Download domiciliëringsnorm PDF en verwerk

Gebruik: python3 tools/process_normen.py
"""

import re
import html
import os
import urllib.request
import subprocess
from pathlib import Path

# Metadata per norm: (output_bestandsnaam, naam, datum, toepassingsgebied, themas, itaa_lex_sectie, url)
NORMEN_META = {
    "algemene-controlenorm.md": {
        "output": "ITAA-norm-algemene-controlenorm.md",
        "naam": "Algemene Controlenorm",
        "datum": "1991-09-30",
        "toepassingsgebied": "Alle gecertificeerde accountants bij uitvoering van controleopdrachten",
        "themas": ["controle", "accountancy", "rapportering", "verslag"],
        "itaa_lex_sectie": "XXI",
        "url": "https://www.itaa.be/nl/algemene-controlenorm/",
    },
    "aww-reglement-iab.md": {
        "output": "ITAA-norm-aww-reglement.md",
        "naam": "AWW-Reglement (IAB/ITAA) — Norm antiwitwas",
        "datum": "2020-03-31",
        "toepassingsgebied": "Alle ITAA-leden als onderworpen entiteit onder de Antiwitwaswet 2017",
        "themas": ["antiwitwas", "cliëntenonderzoek", "UBO", "AMLCO", "risicoanalyse", "meldingsplicht"],
        "itaa_lex_sectie": "XVII",
        "url": "https://www.itaa.be/nl/aww-reglement-iab/",
    },
    "gedragslijnen-relaties-IBR.md": {
        "output": "ITAA-norm-gedragslijnen-relaties-IBR.md",
        "naam": "Gedragslijnen inzake de betrekkingen tussen IBR en IAB/ITAA",
        "datum": None,
        "toepassingsgebied": "ITAA-leden bij samenwerking met of verwijzing naar bedrijfsrevisoren (IBR)",
        "themas": ["samenwerking", "IBR", "bedrijfsrevisor", "gedeelde opdrachten"],
        "itaa_lex_sectie": "XXI",
        "url": None,
    },
    "kmo-controlenorm.md": {
        "output": "ITAA-norm-kmo-controlenorm.md",
        "naam": "KMO-Controlenorm — Norm contractuele controle KMO's en kleine (i)vzw's",
        "datum": "2019-01-01",
        "toepassingsgebied": "Accountants en bedrijfsrevisoren bij contractuele controle van KMO's en kleine vzw's (niet-beursgenoteerd)",
        "themas": ["controle", "KMO", "assurance", "samenstellingsopdrachten", "gedeelde wettelijk voorbehouden opdrachten"],
        "itaa_lex_sectie": "XXI",
        "url": "https://www.itaa.be/nl/kmo-controle-norm/",
    },
    "norm-omzetting-vennootschap.md": {
        "output": "ITAA-norm-omzetting-vennootschap.md",
        "naam": "Norm — Verslag bij omzetting van een vennootschap",
        "datum": None,
        "toepassingsgebied": "ITAA-leden bij opdracht tot opstellen verslag bij vennootschapsomzetting (WVV art. 14:1–14:9)",
        "themas": ["vennootschapsrecht", "omzetting", "verslag", "WVV"],
        "itaa_lex_sectie": "XV",
        "url": "https://www.itaa.be/nl/norm-inzake-het-verslag-op-te-stellen-bij-de-omzetting-van-een-vennootschap/",
    },
    "norm-ontbinding-vereffening.md": {
        "output": "ITAA-norm-ontbinding-vereffening.md",
        "naam": "Norm — Opdracht bij ontbinding en vereffening van vennootschappen",
        "datum": None,
        "toepassingsgebied": "ITAA-leden aangesteld als vereffenaar of belast met verslag bij ontbinding en vereffening (WVV art. 2:69–2:75)",
        "themas": ["vennootschapsrecht", "ontbinding", "vereffening", "verslag", "WVV"],
        "itaa_lex_sectie": "XV",
        "url": "https://www.itaa.be/nl/norm-inzake-de-opdracht-bij-de-ontbinding-en-vereffening-van-vennootschappen/",
    },
    "norm-permanente-vorming.md": {
        "output": "ITAA-norm-permanente-vorming.md",
        "naam": "Norm Permanente Vorming ITAA",
        "datum": "2020-12-01",
        "toepassingsgebied": "Alle ITAA-leden (actief + stagiairs) — uurverplichting per driejarige periode",
        "themas": ["permanente vorming", "stage", "opleiding", "uren", "sanctie"],
        "itaa_lex_sectie": "XXI",
        "url": "https://www.itaa.be/nl/norm-permanente-vorming/",
    },
    "nota-opdrachtbrief.md": {
        "output": "ITAA-norm-opdrachtbrief.md",
        "naam": "Nota Opdrachtbrief — Aanbeveling inzake de opdrachtbrief",
        "datum": None,
        "toepassingsgebied": "Alle ITAA-leden bij aanvang van elke opdracht (wettelijke verplichting)",
        "themas": ["opdrachtbrief", "opdrachtenrecht", "aanvang opdracht", "cliëntenrelatie"],
        "itaa_lex_sectie": "XXI",
        "url": "https://www.itaa.be/nl/opdrachtbrief/",
    },
    "procedurereglement-AWW-art118.md": {
        "output": "ITAA-norm-aww-procedurereglement.md",
        "naam": "Procedurereglement Tuchtkamer AWW (art. 118 Antiwitwaswet)",
        "datum": None,
        "toepassingsgebied": "Tuchtkamer ITAA bij behandeling van AWW-inbreuken — procedure voor beroepsbeoefenaars",
        "themas": ["antiwitwas", "tucht", "tuchtkamer", "procedure", "sanctie"],
        "itaa_lex_sectie": "XVII",
        "url": None,
    },
}

# Domiciliëringsnorm: directe PDF beschikbaar
DOMICILIERING_PDF_URL = "https://www.itaa.be/wp-content/uploads/20240902-NORM-DOMICIERING.pdf"
DOMICILIERING_META = {
    "output": "ITAA-norm-domiciliering.md",
    "naam": "Norm Domiciliëring",
    "datum": "2024-09-02",
    "toepassingsgebied": "ITAA-leden die domicilieringsdiensten aanbieden aan cliënten",
    "themas": ["domiciliëring", "maatschappelijke zetel", "cliëntenrelatie"],
    "itaa_lex_sectie": "XXI",
    "url": "https://www.itaa.be/nl/norm-domiciliering/",
}


def clean_toc_and_pagenums(text: str) -> str:
    """Verwijder TOC-regels (met ......) en losse paginanummers."""
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        # TOC-regel: bevat reeks punten of tabs gevolgd door een paginanummer
        if re.search(r'\.{4,}', line) and re.search(r'\d+\s*$', line):
            continue
        # Lege TOC met tabs/spaties + nummer
        if re.match(r'^[\t ]*\d+[\t ]*$', line) and len(line.strip()) <= 4:
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def strip_frontmatter(text: str) -> tuple[str, str]:
    """Splits de tekst in (frontmatter, body). Geeft ('', text) terug als geen frontmatter."""
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", text
    fm = text[: end + 4]
    body = text[end + 4:].lstrip("\n")
    return fm, body


def build_frontmatter(meta: dict) -> str:
    lines = ["---"]
    lines.append(f'tags: [norm, itaa]')
    lines.append(f'naam: "{meta["naam"]}"')
    if meta.get("datum"):
        lines.append(f'datum: {meta["datum"]}')
    lines.append(f'type: norm')
    if meta.get("itaa_lex_sectie"):
        lines.append(f'itaa-lex-sectie: "{meta["itaa_lex_sectie"]}"')
    lines.append(f'toepassingsgebied: "{meta["toepassingsgebied"]}"')
    lines.append("themas:")
    for t in meta["themas"]:
        lines.append(f"  - {t}")
    if meta.get("url"):
        lines.append(f'bron: itaa.be')
        lines.append(f'url: {meta["url"]}')
    else:
        lines.append(f'bron: itaa.be')
    lines.append("---")
    return "\n".join(lines)


def process_norm(src_path: Path, meta: dict, out_dir: Path) -> None:
    text = src_path.read_text(encoding="utf-8")
    _, body = strip_frontmatter(text)

    # Decode HTML entities
    body = html.unescape(body)

    # Verwijder TOC-ruis
    body = clean_toc_and_pagenums(body)

    # Bouw nieuwe frontmatter
    fm = build_frontmatter(meta)

    output = fm + "\n\n" + body.strip() + "\n"
    out_path = out_dir / meta["output"]
    out_path.write_text(output, encoding="utf-8")
    print(f"  ✓ {meta['output']}")


def download_and_process_pdf(url: str, meta: dict, out_dir: Path) -> None:
    """Download een PDF, converteer met pdftotext, verwerk naar markdown."""
    norm_name = meta["output"].replace(".md", "")
    pdf_path = Path(f"/tmp/{norm_name}.pdf")
    txt_path = Path(f"/tmp/{norm_name}.txt")

    print(f"  Downloading {url}...")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            pdf_path.write_bytes(resp.read())
        print(f"  Downloaded ({pdf_path.stat().st_size} bytes)")
    except Exception as e:
        print(f"  ✗ Download mislukt: {e}")
        return

    # Converteer PDF naar tekst
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), str(txt_path)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  ✗ pdftotext mislukt: {result.stderr}")
        return

    text = txt_path.read_text(encoding="utf-8", errors="replace")

    # Basis opkuis
    body = clean_toc_and_pagenums(text)

    # Verwijder paginascheidingstekens (form feed)
    body = body.replace("\x0c", "\n---\n")

    fm = build_frontmatter(meta)
    output = fm + "\n\n" + body.strip() + "\n"

    out_path = out_dir / meta["output"]
    out_path.write_text(output, encoding="utf-8")
    print(f"  ✓ {meta['output']} (via PDF)")


def main():
    src_dir = Path("resources/normen")
    out_dir = Path("content/bronnen/normen")
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=== Verwerken bestaande normen ===")
    for filename, meta in NORMEN_META.items():
        src_path = src_dir / filename
        if not src_path.exists():
            print(f"  ⚠ {filename} niet gevonden — overgeslagen")
            continue
        process_norm(src_path, meta, out_dir)

    print("\n=== Domiciliëringsnorm downloaden ===")
    download_and_process_pdf(DOMICILIERING_PDF_URL, DOMICILIERING_META, out_dir)

    print("\n=== ISA-570 (al verwerkt) kopiëren ===")
    isa_src = Path("content/bronnen/normen/ISA-570-herzien.md")
    if isa_src.exists():
        print(f"  ✓ ISA-570-herzien.md al aanwezig")
    else:
        isa_raw = Path("resources/normen/raw/ISA-570-herzien-2023-NL.pdf")
        if isa_raw.exists():
            print(f"  ISA-570 PDF aanwezig, verwerken...")
            isa_meta = {
                "output": "ISA-570-herzien.md",
                "naam": "ISA 570 (herzien) — Continuïteitsveronderstelling",
                "datum": "2023-01-01",
                "toepassingsgebied": "Accountants bij assurance-opdrachten waarbij continuïteitsrisico beoordeeld wordt",
                "themas": ["continuïteitsrisico", "going concern", "ISA", "assurance", "controle"],
                "itaa_lex_sectie": "XXI",
                "url": None,
            }
            download_and_process_pdf(str(isa_raw), isa_meta, out_dir)
        else:
            print("  ⚠ ISA-570 niet gevonden")

    print("\n=== Klaar ===")
    print(f"Normen staan in: {out_dir}")
    print(f"Bestanden: {list(out_dir.glob('*.md'))}")


if __name__ == "__main__":
    os.chdir(Path(__file__).parent.parent)  # Ga naar projectroot
    main()
