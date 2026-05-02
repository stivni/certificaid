#!/usr/bin/env python3
"""
Herverwerk alle CBN-adviezen in content/bronnen/adviezen/ door elke pagina
opnieuw te fetchen en te structureren met YAML-frontmatter.
"""

import os
import re
import time
import subprocess
from html.parser import HTMLParser

ADVIEZEN_DIR = "/Users/stivni/Documents/ITAA/certificaid/content/bronnen/adviezen"
RAPPORT_PATH = "/Users/stivni/Documents/ITAA/certificaid/.cbn-reprocess-rapport.md"


# ─── HTML-extractors ──────────────────────────────────────────────────────────

def extract_class_content(html, class_fragment):
    """Extraheer tekstinhoud van het eerste element met class_fragment."""
    pos = html.find(class_fragment)
    if pos < 0:
        return ""
    tag_end = html.find('>', pos)
    if tag_end < 0:
        return ""
    depth = 1
    i = tag_end + 1
    while i < len(html) and depth > 0:
        next_open = html.find('<div', i)
        next_close = html.find('</div', i)
        if next_open < 0:
            next_open = len(html)
        if next_close < 0:
            next_close = len(html)
        if next_open < next_close:
            depth += 1
            i = next_open + 4
        else:
            depth -= 1
            i = next_close + 5
    content = html[tag_end + 1:i - 5]
    return content


def extract_main_content(html):
    """Fallback: extraheer <main>...</main>."""
    m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else ""


class MarkdownConverter(HTMLParser):
    """Converteert HTML naar Markdown, slaat nav-elementen over."""

    SKIP_TAGS = {'script', 'style', 'nav', 'header', 'footer', 'form',
                 'select', 'option', 'sup', 'noscript', 'iframe', 'button'}

    def __init__(self):
        super().__init__()
        self.result = []
        self.skip_depth = 0
        self.list_stack = []
        self.list_counters = []
        self.in_heading = False
        self.heading_level = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP_TAGS or self.skip_depth > 0:
            self.skip_depth += 1
            return

        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            level = int(tag[1])
            self.result.append(f'\n\n{"#" * level} ')
            self.in_heading = True
            self.heading_level = level
        elif tag == 'p':
            self.result.append('\n\n')
        elif tag in ('strong', 'b'):
            self.result.append('**')
        elif tag in ('em', 'i'):
            self.result.append('*')
        elif tag == 'br':
            self.result.append('\n')
        elif tag == 'ul':
            self.list_stack.append('ul')
            self.list_counters.append(0)
            self.result.append('\n')
        elif tag == 'ol':
            self.list_stack.append('ol')
            self.list_counters.append(0)
            self.result.append('\n')
        elif tag == 'li':
            if self.list_stack and self.list_stack[-1] == 'ol':
                self.list_counters[-1] += 1
                self.result.append(f'\n{self.list_counters[-1]}. ')
            else:
                self.result.append('\n- ')
        elif tag == 'blockquote':
            self.result.append('\n> ')
        elif tag == 'hr':
            self.result.append('\n\n---\n')
        elif tag == 'table':
            self.result.append('\n')
        elif tag == 'tr':
            self.result.append('\n| ')
        elif tag in ('td', 'th'):
            self.result.append(' | ')

    def handle_endtag(self, tag):
        if self.skip_depth > 0:
            self.skip_depth -= 1
            return

        if tag in ('strong', 'b'):
            self.result.append('**')
        elif tag in ('em', 'i'):
            self.result.append('*')
        elif tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.result.append('\n')
            self.in_heading = False
        elif tag in ('ul', 'ol'):
            if self.list_stack:
                self.list_stack.pop()
                self.list_counters.pop()
            self.result.append('\n')
        elif tag == 'tr':
            self.result.append(' |')

    def handle_data(self, data):
        if self.skip_depth > 0:
            return
        self.result.append(data)

    def get_markdown(self):
        text = ''.join(self.result)
        text = re.sub(r'[ \t]+', ' ', text)
        text = re.sub(r'\n{4,}', '\n\n\n', text)
        return text.strip()


# ─── Hulpfuncties ─────────────────────────────────────────────────────────────

def parse_date(date_str):
    """Converteer 'dd maand yyyy' naar 'yyyy-mm-dd'."""
    maanden = {
        'januari': '01', 'februari': '02', 'maart': '03', 'april': '04',
        'mei': '05', 'juni': '06', 'juli': '07', 'augustus': '08',
        'september': '09', 'oktober': '10', 'november': '11', 'december': '12'
    }
    m = re.search(r'(\d{1,2})\s+(\w+)\s+(\d{4})', date_str)
    if m:
        dag, maand, jaar = m.groups()
        maand_num = maanden.get(maand.lower(), '00')
        return f"{jaar}-{maand_num}-{int(dag):02d}"
    return ""


def strip_tags(html):
    """Verwijder alle HTML-tags."""
    return re.sub(r'<[^>]+>', '', html)


def clean_body(text, nummer):
    """Verwijder header-ruis en TOC uit de geconverteerde body."""
    lines = text.split('\n')
    clean_lines = []
    found_real_content = False

    for line in lines:
        stripped = line.strip()

        if not found_real_content:
            # Skip COMMISSIE header
            if 'COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN' in stripped:
                continue
            # Skip herhaalde advies-titels
            if nummer and nummer in stripped and len(stripped) < 60:
                continue
            # Skip "Advies van [datum]" regel
            if re.match(r'Advies van \d', stripped):
                continue
            # Skip "- Select -" TOC-blokken
            if '- Select -' in stripped or stripped == 'Select':
                continue
            # Echte inhoud begint bij eerste ## heading of lange alinea
            if stripped.startswith('##') or (len(stripped) > 80 and not stripped.startswith('#')):
                found_real_content = True

        if found_real_content:
            clean_lines.append(line)

    result = '\n'.join(clean_lines)
    # Verwijder CBN-referentie-blokje onderaan
    result = re.sub(r'\n\nCBN-advies[^\n]*\n?$', '', result.strip())
    return result.strip()


def extract_h1_from_body(body):
    """Extraheer de eerste # heading als titel."""
    for line in body.split('\n'):
        stripped = line.strip()
        if stripped.startswith('# ') and not stripped.startswith('## '):
            return stripped[2:].strip()
    return ""


def fetch_html(url):
    """Fetch HTML via curl. Geeft (status_code, html) tuple."""
    result = subprocess.run(
        ['curl', '-s', '-w', '\n__HTTP_STATUS__%{http_code}',
         '--user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
         '--max-time', '30',
         url],
        capture_output=True, text=True
    )
    output = result.stdout
    # Splits HTTP status van body
    if '__HTTP_STATUS__' in output:
        parts = output.rsplit('__HTTP_STATUS__', 1)
        html = parts[0]
        status = int(parts[1].strip())
    else:
        html = output
        status = 0
    return status, html


def extract_url_from_file(content):
    """Extraheer de CBN-URL uit de bestaande bestandsinhoud."""
    m = re.search(r'https://www\.cbn-cnc\.be[^\s\*\]\n]+', content)
    return m.group(0).strip() if m else None


def build_output(nummer, datum, themas, url, titel, body):
    """Bouw de output Markdown op."""
    if themas:
        themas_yaml = '\n'.join(f'  - {t.strip()}' for t in themas if t.strip())
    else:
        themas_yaml = '  - (geen)'

    return f"""---
nummer: "{nummer}"
datum: {datum}
themas:
{themas_yaml}
bron: {url}
---

# {titel}

{body}
"""


# ─── Hoofd verwerking ─────────────────────────────────────────────────────────

def process_file(filepath):
    """Verwerk één bestand. Geeft (status_str, details) terug."""
    with open(filepath, 'r', encoding='utf-8') as f:
        existing_content = f.read()

    url = extract_url_from_file(existing_content)
    if not url:
        return "skip_no_url", f"Geen URL gevonden"

    # Fetch HTML
    status_code, html = fetch_html(url)
    if status_code != 200:
        return "skip_http_error", f"HTTP {status_code} voor {url}"

    # Extraheer metadata
    number_html = extract_class_content(html, 'field-advice-number')
    date_html = extract_class_content(html, 'field-advice-date')
    themes_html = extract_class_content(html, 'field-advice-themes')
    body_html = extract_class_content(html, 'field-advice-text')

    # Fallback voor body
    if not body_html or len(body_html.strip()) < 100:
        body_html = extract_main_content(html)
        used_fallback = True
    else:
        used_fallback = False

    # Metadata verwerken
    nummer_raw = strip_tags(number_html).strip()
    # Normaliseer whitespace (newlines, meerdere spaties → één spatie)
    nummer = re.sub(r'\s+', ' ', nummer_raw).strip()
    if not nummer:
        # Probeer uit de bestaande titel
        m = re.search(r'CBN-advies\s+[\w/\-]+', existing_content)
        nummer = m.group(0) if m else "CBN-advies (onbekend)"

    datum_str = strip_tags(date_html).strip()
    datum = parse_date(datum_str) if datum_str else ""

    themas = re.findall(r'<a[^>]*>([^<]+)</a>', themes_html)

    # Body converteren
    if body_html:
        converter = MarkdownConverter()
        try:
            converter.feed(body_html)
        except Exception:
            pass
        raw_md = converter.get_markdown()
        body = clean_body(raw_md, nummer)
    else:
        body = ""

    # Korte bestanden markeren
    if len(body) < 200:
        themas = ['geen inhoud']
        if not body:
            body = "*Geen inhoud beschikbaar op de bronpagina.*"

    # Titel bepalen: zoek eerst naar "# CBN-advies XXXX/YY — [titel]" patroon
    titel = ""
    for line in body.split('\n'):
        stripped = line.strip()
        if stripped.startswith('# ') and not stripped.startswith('## '):
            candidate = stripped[2:].strip()
            # Sla de kale advies-header over ("CBN-advies 2021/01" zonder beschrijving)
            if re.match(r'^CBN-advies\s+[\d/]+\s*$', candidate):
                continue
            # Sla "COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN" over
            if 'COMMISSIE' in candidate:
                continue
            titel = candidate
            break

    if not titel:
        # Gebruik nummer + slug uit URL (beschrijvender dan eerste sectie)
        slug = url.rstrip('/').split('/')[-1]
        # Verwijder trailing cijfer van slug (bv. -0, -1)
        slug = re.sub(r'-\d+$', '', slug)
        slug_readable = slug.replace('-', ' ').strip()
        titel = f"{nummer} — {slug_readable}" if nummer else slug_readable

    # Normaliseer whitespace in titel
    titel = re.sub(r'\s+', ' ', titel).strip()

    # Verwijder dubbele H1 uit body als die de titel is
    if titel:
        # Verwijder exacte match
        body = re.sub(r'^# ' + re.escape(titel) + r'\s*\n', '', body, flags=re.MULTILINE)
        # Verwijder ook kale CBN-advies headers
        body = re.sub(r'^# CBN-advies\s+[\d/]+\s*\n', '', body, flags=re.MULTILINE)
        # Verwijder COMMISSIE header
        body = re.sub(r'^# COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN\s*\n', '', body, flags=re.MULTILINE)
        body = body.strip()

    output = build_output(nummer, datum, themas, url, titel, body)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(output)

    detail = f"fallback={used_fallback}" if used_fallback else ""
    return "ok", detail


def main():
    files = sorted([
        f for f in os.listdir(ADVIEZEN_DIR)
        if f.endswith('.md')
    ])
    total = len(files)
    print(f"Verwerking van {total} bestanden gestart...\n")

    results = {"ok": [], "skip_no_url": [], "skip_http_error": [], "error": []}
    rapport_lines = [
        f"# CBN Herverwerking rapport\n",
        f"Totaal bestanden: {total}\n",
    ]

    for i, filename in enumerate(files, 1):
        filepath = os.path.join(ADVIEZEN_DIR, filename)

        try:
            status, detail = process_file(filepath)
        except Exception as e:
            status = "error"
            detail = str(e)

        results[status].append((filename, detail))

        # Voortgang tonen
        status_icon = "✓" if status == "ok" else "✗"
        print(f"[{i:3d}/{total}] {status_icon} {filename[:60]:<60} {detail}")

        # Rapport elke 50 bestanden tussentijds bijwerken
        if i % 50 == 0:
            rapport_lines.append(f"\n## Voortgang na {i} bestanden\n")
            rapport_lines.append(f"- OK: {len(results['ok'])}\n")
            rapport_lines.append(f"- Geen URL: {len(results['skip_no_url'])}\n")
            rapport_lines.append(f"- HTTP-fout: {len(results['skip_http_error'])}\n")
            rapport_lines.append(f"- Fout: {len(results['error'])}\n")
            with open(RAPPORT_PATH, 'w', encoding='utf-8') as f:
                f.writelines(rapport_lines)
            print(f"\n  → Tussentijds rapport geschreven ({i}/{total})\n")

        # Wacht tussen requests
        time.sleep(0.3)

    # Eindrapport
    rapport_lines.append(f"\n## Eindresultaten\n")
    rapport_lines.append(f"- ✓ OK: {len(results['ok'])}\n")
    rapport_lines.append(f"- ⚠ Geen URL: {len(results['skip_no_url'])}\n")
    rapport_lines.append(f"- ✗ HTTP-fout: {len(results['skip_http_error'])}\n")
    rapport_lines.append(f"- ✗ Fout: {len(results['error'])}\n")

    if results['skip_no_url']:
        rapport_lines.append(f"\n### Bestanden zonder URL\n")
        for fn, _ in results['skip_no_url']:
            rapport_lines.append(f"- {fn}\n")

    if results['skip_http_error']:
        rapport_lines.append(f"\n### HTTP-fouten\n")
        for fn, detail in results['skip_http_error']:
            rapport_lines.append(f"- {fn}: {detail}\n")

    if results['error']:
        rapport_lines.append(f"\n### Verwerkingsfouten\n")
        for fn, detail in results['error']:
            rapport_lines.append(f"- {fn}: {detail}\n")

    with open(RAPPORT_PATH, 'w', encoding='utf-8') as f:
        f.writelines(rapport_lines)

    print(f"\n{'='*60}")
    print(f"Klaar. {len(results['ok'])}/{total} bestanden bijgewerkt.")
    print(f"Rapport: {RAPPORT_PATH}")


if __name__ == '__main__':
    main()
