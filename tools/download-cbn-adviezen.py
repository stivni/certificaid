#!/usr/bin/env python3
"""
Download alle CBN-adviezen van cbn-cnc.be en sla ze op als doorzoekbare markdown-bestanden.
"""

import os
import re
import time
import subprocess
import sys
from datetime import datetime

BASE_URL = "https://www.cbn-cnc.be"
INDEX_URL = f"{BASE_URL}/nl/adviezen"
OUTPUT_DIR = "/Users/stivni/Documents/ITAA/certificaid/resources/adviezen"
RAPPORT_PATH = "/Users/stivni/Documents/ITAA/certificaid/.cbn-download-rapport.md"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
RATE_LIMIT = 0.5  # seconden tussen requests

os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch(url):
    """Haal een URL op met curl."""
    result = subprocess.run(
        ["curl", "-s", "-L", "--max-time", "30", "--user-agent", USER_AGENT, url],
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    return result.stdout

def extract_text(html):
    """Extraheer schone tekst uit HTML."""
    # Verwijder scripts en styles eerst
    text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    # Probeer eerst <main> te vinden
    main_match = re.search(r'<main[^>]*>(.*?)</main>', text, re.DOTALL | re.IGNORECASE)
    if main_match:
        text = main_match.group(1)
    else:
        # Fallback: verwijder nav/header/footer
        text = re.sub(r'<nav[^>]*>.*?</nav>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<header[^>]*>.*?</header>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<footer[^>]*>.*?</footer>', '', text, flags=re.DOTALL | re.IGNORECASE)
    # Vervang block-level tags door newlines
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</(p|div|li|h[1-6]|tr|td|th|blockquote|article|section)>', '\n', text, flags=re.IGNORECASE)
    # Strip alle resterende tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # HTML entities
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'&lt;', '<', text)
    text = re.sub(r'&gt;', '>', text)
    text = re.sub(r'&quot;', '"', text)
    text = re.sub(r'&#39;', "'", text)
    text = re.sub(r'&[a-zA-Z]+;', ' ', text)
    text = re.sub(r'&#\d+;', ' ', text)
    # Witruimte opruimen
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r' *\n *', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def extract_title(html):
    """Haal de paginatitel op uit H1 of title-tag."""
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
    if h1:
        title = re.sub(r'<[^>]+>', '', h1.group(1)).strip()
        if title:
            return title
    title_tag = re.search(r'<title[^>]*>(.*?)</title>', html, re.DOTALL | re.IGNORECASE)
    if title_tag:
        title = re.sub(r'<[^>]+>', '', title_tag.group(1)).strip()
        title = re.sub(r'\s*[|\-–]\s*CBN.*$', '', title).strip()
        if title:
            return title
    return "CBN Advies"

def get_url_list():
    """Haal de lijst van alle advies-URLs op van de indexpagina."""
    print(f"Ophalen URL-lijst van {INDEX_URL}...")
    html = fetch(INDEX_URL)
    urls = re.findall(r'href="(/nl/adviezen/[^"]+)"', html)
    # Filter de indexpagina zelf en speciale pagina's
    urls = [u for u in urls if u != '/nl/adviezen' and not u.endswith('/adviezen')]
    urls = list(dict.fromkeys(urls))  # deduplicate, behoud volgorde
    print(f"Gevonden: {len(urls)} URLs")
    return urls

def url_to_filename(url_path):
    """Converteer URL-pad naar bestandsnaam."""
    slug = url_path.split('/nl/adviezen/')[-1].strip('/')
    # Vervang slashes in slug door underscore (subpagina's)
    slug = slug.replace('/', '_')
    if not slug:
        return None
    return f"{slug}.md"

def download_advies(url_path, stats):
    """Download één advies en sla op als markdown. Returns True als succesvol."""
    filename = url_to_filename(url_path)
    if not filename:
        stats['skip'] += 1
        return False

    filepath = os.path.join(OUTPUT_DIR, filename)

    # Skip als bestand al bestaat
    if os.path.exists(filepath):
        stats['existing'] += 1
        return False

    full_url = f"{BASE_URL}{url_path}"
    html = fetch(full_url)

    if not html or len(html) < 200:
        stats['errors'].append(f"Lege response: {full_url}")
        stats['error'] += 1
        return False

    text = extract_text(html)

    # Kwaliteitscheck: sla over als tekst te kort (navigatiepagina's)
    if len(text) < 500:
        stats['skip'] += 1
        return False

    title = extract_title(html)

    # Sla op
    content = f"""# {title}

**Bron**: {full_url}
**Status**: verbatim tekst via HTML-extractie

---

{text}
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    stats['success'] += 1
    return True

def write_rapport(stats, urls_total, elapsed):
    """Schrijf het downloadrapport."""
    rapport = f"""# CBN Adviezen Download Rapport

**Datum**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Duur**: {elapsed:.0f} seconden

## Resultaat

| Categorie | Aantal |
|-----------|--------|
| Totaal URLs verwerkt | {urls_total} |
| Succesvol gedownload | {stats['success']} |
| Al aanwezig (skip) | {stats['existing']} |
| Overgeslagen (te kort) | {stats['skip']} |
| Fouten | {stats['error']} |

## Fouten

"""
    if stats['errors']:
        for err in stats['errors']:
            rapport += f"- {err}\n"
    else:
        rapport += "Geen fouten.\n"

    with open(RAPPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(rapport)

    print(f"\nRapport geschreven naar {RAPPORT_PATH}")

def main():
    stats = {
        'success': 0,
        'existing': 0,
        'skip': 0,
        'error': 0,
        'errors': []
    }

    urls = get_url_list()
    start = time.time()

    for i, url_path in enumerate(urls, 1):
        filename = url_to_filename(url_path)

        # Check of al bestaat (voor voortgangsmelding)
        if filename and os.path.exists(os.path.join(OUTPUT_DIR, filename)):
            stats['existing'] += 1
            if i % 50 == 0:
                print(f"  [{i}/{len(urls)}] {stats['success']} nieuw, {stats['existing']} bestaand, {stats['skip']} skip, {stats['error']} fouten")
            continue

        result = download_advies(url_path, stats)

        if i % 20 == 0 or (result and stats['success'] % 10 == 0):
            elapsed = time.time() - start
            print(f"  [{i}/{len(urls)}] {stats['success']} nieuw | {stats['existing']} bestaand | {stats['skip']} skip | {stats['error']} fouten | {elapsed:.0f}s", flush=True)

        time.sleep(RATE_LIMIT)

    elapsed = time.time() - start
    print(f"\nKlaar! {stats['success']} nieuw gedownload, {stats['existing']} bestaand, {stats['skip']} overgeslagen, {stats['error']} fouten. ({elapsed:.0f}s)")

    write_rapport(stats, len(urls), elapsed)

if __name__ == '__main__':
    main()
