#!/usr/bin/env python3
"""
Download missende ITAA-normen van BeExcellent (beexcellentnl.itaa.be).

Vereist: actieve ingelogde sessie in Chrome voor beexcellentnl.itaa.be
Gebruik:  python3 tools/download_beexcellent_normen.py

Wat dit script doet:
1. Haalt sessiecookies uit Chrome via browser_cookie3
2. Downloadt elk bestand via /ContentService/content/file/{id}/{hash}/meta → S3 presigned URL
3. Converteert PDF naar tekst met pdftotext, DOCX met python-docx
4. Voegt YAML frontmatter toe
5. Schrijft naar content/bronnen/normen/

HTML-tekst normen (Fusie/splitsing, artikelen 56-60) worden rechtstreeks via
de ContentService API opgehaald en met markdownify geconverteerd.
"""

import json
import html
import subprocess
import sys
import os
import requests
import browser_cookie3
from pathlib import Path
from markdownify import markdownify as md

# ---------------------------------------------------------------------------
# Normen die als bestand (PDF/DOCX) opgeslagen zijn op BeExcellent
# ---------------------------------------------------------------------------
FILE_NORMEN = [
    {
        "article_id": 4,
        "hash": "1c5b1643d35717566a2ed1be652651ce",
        "output": "ITAA-norm-aww-richtlijn-bibf.md",
        "naam": "AWW-Richtlijn (BIBF) — Richtlijn antiwitwas boekhoudkundige beroepen",
        "datum": "2020-03-31",
        "toepassingsgebied": "Erkende boekhouders en fiscalisten (BIBF-leden) als onderworpen entiteit",
        "themas": ["antiwitwas", "cliëntenonderzoek", "UBO", "AMLCO", "risicoanalyse", "meldingsplicht", "BIBF"],
        "itaa_lex_sectie": "XVII",
    },
    {
        "article_id": 416,
        "hash": "903f2ad7c26c8dd86f8119f22eba38f6",
        "output": "ITAA-norm-aww-geconsolideerd.md",
        "naam": "Geconsolideerde AWW-norm — IAB-norm + BIBF-richtlijn gecombineerd",
        "datum": "2022-04-26",
        "toepassingsgebied": "Alle ITAA-leden (gecertificeerde accountants + belastingadviseurs)",
        "themas": ["antiwitwas", "cliëntenonderzoek", "UBO", "AMLCO", "risicoanalyse", "meldingsplicht", "geconsolideerd"],
        "itaa_lex_sectie": "XVII",
    },
    {
        "article_id": 2091,
        "hash": "af94a4f8dc38966775bf8e7394db2c32",
        "output": "ITAA-norm-samenstellingsopdrachten-isrs4410.md",
        "naam": "Norm inzake de Samenstellingsopdrachten (ISRS 4410)",
        "datum": "2025-05-09",
        "toepassingsgebied": "ITAA-leden bij samenstellingsopdrachten (niet-assurance) voor jaarrekeningen en financiële overzichten",
        "themas": ["samenstellingsopdrachten", "ISRS 4410", "assurance", "jaarrekening", "niet-assurance"],
        "itaa_lex_sectie": "XXI",
    },
    {
        "article_id": 2640,
        "hash": "bd506f44c6d29a5326e39213f2d041c4",
        "output": "ITAA-norm-intern-kwaliteitsmanagement.md",
        "naam": "Norm Algemene Vereisten Intern Kwaliteitsmanagement",
        "datum": "2025-09-03",
        "toepassingsgebied": "Alle ITAA-leden — kwaliteitssysteem voor het beroepskantoor",
        "themas": ["kwaliteitsmanagement", "intern kwaliteitssysteem", "kantoororganisatie"],
        "itaa_lex_sectie": "XXI",
    },
    {
        "article_id": 2692,
        "hash": "126c7fe88db58398313b11f0a5643ed5",
        "output": "ITAA-norm-effectennorm.md",
        "naam": "Effectennorm — Norm beoordeling financiële en boekhoudkundige gegevens (nog niet in werking)",
        "datum": "2026-03-31",
        "toepassingsgebied": "ITAA-leden bij opdracht tot beoordeling van getrouwheid en volledigheid financiële gegevens",
        "themas": ["effectennorm", "beoordeling", "financiële gegevens", "assurance"],
        "itaa_lex_sectie": "XXI",
        "opmerking": "⚠️ Nog niet in werking per 2026-04-21",
    },
]

# ---------------------------------------------------------------------------
# HTML-tekst normen (per sectie opgeslagen in BeExcellent)
# ---------------------------------------------------------------------------
HTML_NORMEN = [
    {
        "article_ids": [56, 57, 58, 59, 60],
        "output": "ITAA-norm-fusie-splitsing.md",
        "naam": "Norm inzake de Controle van Fusie- en Splitsingsverrichtingen van Vennootschappen",
        "datum": "2013-12-13",
        "toepassingsgebied": "ITAA-leden aangesteld voor controle van fusie- of splitsingsverslag (WVV art. 12:26–12:55)",
        "themas": ["fusie", "splitsing", "vennootschapsrecht", "verslag", "ruilverhouding", "WVV"],
        "itaa_lex_sectie": "XV",
    },
]

BASE_URL = "https://beexcellentnl.itaa.be"
RAW_DIR = Path("resources/normen/raw")
OUT_DIR = Path("content/bronnen/normen")


def get_cookies():
    """Haal Chrome-sessiecookies op voor beexcellentnl.itaa.be."""
    try:
        cookies = browser_cookie3.chrome(domain_name='.itaa.be')
        return cookies
    except Exception as e:
        print(f"  ✗ Kon cookies niet ophalen: {e}")
        print("  Zorg dat Chrome open is en je ingelogd bent op beexcellentnl.itaa.be")
        sys.exit(1)


def get_presigned_url(session, article_id, file_hash):
    """Haal de presigned S3 URL op via het meta endpoint."""
    url = f"{BASE_URL}/ContentService/content/file/{article_id}/{file_hash}/meta"
    resp = session.get(url)
    if resp.status_code != 200:
        raise Exception(f"Meta endpoint {url}: HTTP {resp.status_code}")
    data = resp.json()
    return data["url"]


def download_file(presigned_url, dest_path):
    """Download een bestand van S3 via de presigned URL."""
    resp = requests.get(presigned_url, stream=True)
    resp.raise_for_status()
    dest_path.write_bytes(resp.content)
    return len(resp.content)


def pdf_to_text(pdf_path):
    """Converteer PDF naar tekst met pdftotext."""
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        capture_output=True
    )
    if result.returncode != 0:
        raise Exception(f"pdftotext mislukt: {result.stderr.decode()}")
    return result.stdout.decode("utf-8", errors="replace")


def docx_to_text(docx_path):
    """Converteer DOCX naar markdown met pandoc als dat beschikbaar is, anders plain text."""
    # Probeer pandoc
    result = subprocess.run(
        ["pandoc", str(docx_path), "-t", "markdown", "--wrap=none"],
        capture_output=True
    )
    if result.returncode == 0:
        return result.stdout.decode("utf-8", errors="replace")
    # Fallback: python-docx
    try:
        from docx import Document
        doc = Document(str(docx_path))
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n\n".join(paragraphs)
    except Exception as e:
        raise Exception(f"DOCX conversie mislukt (pandoc + python-docx beide gefaald): {e}")


def clean_text(text):
    """Verwijder TOC-ruis en losse paginanummers."""
    import re
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        if re.search(r'\.{4,}', line) and re.search(r'\d+\s*$', line):
            continue
        if re.match(r'^[\t ]*\d+[\t ]*$', line) and len(line.strip()) <= 4:
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def build_frontmatter(meta):
    lines = ["---"]
    lines.append("tags: [norm, itaa]")
    lines.append(f'naam: "{meta["naam"]}"')
    if meta.get("datum"):
        lines.append(f'datum: {meta["datum"]}')
    lines.append("type: norm")
    if meta.get("itaa_lex_sectie"):
        lines.append(f'itaa-lex-sectie: "{meta["itaa_lex_sectie"]}"')
    lines.append(f'toepassingsgebied: "{meta["toepassingsgebied"]}"')
    lines.append("themas:")
    for t in meta["themas"]:
        lines.append(f"  - {t}")
    if meta.get("opmerking"):
        lines.append(f'opmerking: "{meta["opmerking"]}"')
    lines.append("bron: beexcellentnl.itaa.be")
    lines.append("---")
    return "\n".join(lines)


def process_file_norm(session, norm_meta):
    name = norm_meta["output"]
    article_id = norm_meta["article_id"]
    file_hash = norm_meta["hash"]

    print(f"\n  Downloading artikel {article_id} ({name})...")

    # Haal presigned URL op
    presigned_url = get_presigned_url(session, article_id, file_hash)

    # Download het bestand
    ext = "pdf" if "pdf" in presigned_url.lower() or norm_meta.get("hash", "").endswith("pdf") else "docx"
    # Bepaal extensie uit originele bestandsnaam via artikel-metadata
    resp_meta = session.get(f"{BASE_URL}/ContentService/content/file/{article_id}/{file_hash}/meta")
    mime = resp_meta.json().get("originalMimeType", "")
    if "pdf" in mime:
        ext = "pdf"
    elif "wordprocessingml" in mime or "docx" in mime:
        ext = "docx"

    raw_path = RAW_DIR / f"beexcellent-{article_id}.{ext}"
    size = download_file(presigned_url, raw_path)
    print(f"    ✓ {size:,} bytes → {raw_path}")

    # Converteer naar tekst
    if ext == "pdf":
        text = pdf_to_text(raw_path)
        text = clean_text(text)
    else:
        text = docx_to_text(raw_path)

    # Schrijf output
    fm = build_frontmatter(norm_meta)
    out_path = OUT_DIR / norm_meta["output"]
    out_path.write_text(fm + "\n\n" + text.strip() + "\n", encoding="utf-8")
    print(f"    ✓ {norm_meta['output']}")


def fetch_html_article(session, article_id):
    """Haal de HTML-tekst op van een BeExcellent artikel via de ContentService API."""
    url = f"{BASE_URL}/ContentService/articles/{article_id}?replaceVariables=1"
    resp = session.get(url)
    resp.raise_for_status()
    data = resp.json()
    title = data.get("title", "")
    content = data.get("content", {})
    html_text = content.get("text", "") if content.get("contentType") == "text" else ""
    return title, html_text


def process_html_norm(session, norm_meta):
    name = norm_meta["output"]
    print(f"\n  Ophalen HTML-norm {name}...")

    sections = []
    for art_id in norm_meta["article_ids"]:
        title, html_text = fetch_html_article(session, art_id)
        if html_text:
            # HTML entities + markdown conversie
            html_decoded = html.unescape(html_text)
            section_md = md(html_decoded, heading_style="ATX")
            sections.append(f"## {title}\n\n{section_md.strip()}")
            print(f"    ✓ Artikel {art_id}: {title}")
        else:
            print(f"    ⚠ Artikel {art_id}: geen tekst (type: {fetch_html_article.__name__})")

    body = "\n\n".join(sections)
    fm = build_frontmatter(norm_meta)
    out_path = OUT_DIR / norm_meta["output"]
    out_path.write_text(fm + "\n\n" + body.strip() + "\n", encoding="utf-8")
    print(f"    ✓ {norm_meta['output']}")


def main():
    os.chdir(Path(__file__).parent.parent)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=== Ophalen Chrome-cookies voor itaa.be ===")
    cookies = get_cookies()

    session = requests.Session()
    session.cookies = cookies
    session.headers["User-Agent"] = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )

    # Test de sessie
    test = session.get(f"{BASE_URL}/ContentService/auth/identity")
    if test.status_code != 200:
        print(f"✗ Sessie werkt niet: HTTP {test.status_code}. Controleer of je ingelogd bent.")
        sys.exit(1)
    identity = test.json()
    print(f"✓ Ingelogd als: {identity.get('realName', '?')} ({identity.get('userName', '?')})")

    print("\n=== Downloaden bestand-normen ===")
    for norm in FILE_NORMEN:
        try:
            process_file_norm(session, norm)
        except Exception as e:
            print(f"  ✗ {norm['output']}: {e}")

    print("\n=== Ophalen HTML-tekst normen ===")
    for norm in HTML_NORMEN:
        try:
            process_html_norm(session, norm)
        except Exception as e:
            print(f"  ✗ {norm['output']}: {e}")

    print("\n=== Klaar ===")
    results = list(OUT_DIR.glob("ITAA-norm-*.md"))
    print(f"{len(results)} normen in {OUT_DIR}:")
    for f in sorted(results):
        print(f"  {f.name}")


if __name__ == "__main__":
    main()
