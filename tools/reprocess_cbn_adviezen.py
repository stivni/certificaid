#!/usr/bin/env python3
"""
Reprocess CBN adviezen: re-fetch HTML and convert to clean Markdown.
Usage: python3 tools/reprocess_cbn_adviezen.py [--test N]
"""

import os
import re
import sys
import time
import urllib.request
import urllib.error
from html.parser import HTMLParser


# ─── HTML → Markdown parser ────────────────────────────────────────────────

class CBNMarkdownParser(HTMLParser):
    """Convert CBN HTML content to clean Markdown.

    Call feed() with the *already-extracted* content fragment (no nav/chrome).
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.result = []
        self.list_stack = []  # stack of ('ul'|'ol', counter)
        self.in_pre = False
        self.skip_stack = []  # stack of tag names we are skipping
        self._pending_nl = 0  # deferred newlines

    # ── internal helpers ────────────────────────────────────────────────────

    def _skipping(self):
        return len(self.skip_stack) > 0

    def _push_skip(self, tag):
        self.skip_stack.append(tag)

    def _pop_skip(self, tag):
        # Pop the last matching tag from skip_stack
        for i in range(len(self.skip_stack) - 1, -1, -1):
            if self.skip_stack[i] == tag:
                self.skip_stack.pop(i)
                return

    def _ensure_nl(self, n):
        if n > self._pending_nl:
            self._pending_nl = n

    def _flush(self, text=''):
        if self._pending_nl and (self.result or text.strip()):
            self.result.append('\n' * self._pending_nl)
            self._pending_nl = 0
        if text:
            self.result.append(text)

    # ── tag handlers ────────────────────────────────────────────────────────

    # Tags whose entire subtree we skip
    BLOCK_TAGS = frozenset(['script', 'style', 'noscript', 'sup'])

    def handle_starttag(self, tag, attrs):
        if tag in self.BLOCK_TAGS:
            self._push_skip(tag)
            return
        if self._skipping():
            return

        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            level = int(tag[1])
            self._ensure_nl(2)
            self._flush('#' * level + ' ')

        elif tag == 'p':
            self._ensure_nl(2)

        elif tag in ('strong', 'b'):
            self._flush('**')

        elif tag in ('em', 'i'):
            self._flush('*')

        elif tag == 'br':
            self._flush('  \n')

        elif tag == 'hr':
            self._ensure_nl(2)
            self._flush('---')
            self._ensure_nl(2)

        elif tag == 'ul':
            self.list_stack.append(('ul', 0))
            self._ensure_nl(1)

        elif tag == 'ol':
            self.list_stack.append(('ol', 0))
            self._ensure_nl(1)

        elif tag == 'li':
            if self.list_stack:
                kind, counter = self.list_stack[-1]
                indent = '  ' * (len(self.list_stack) - 1)
                if kind == 'ol':
                    counter += 1
                    self.list_stack[-1] = ('ol', counter)
                    self._pending_nl = 0
                    self.result.append(f'\n{indent}{counter}. ')
                else:
                    self._pending_nl = 0
                    self.result.append(f'\n{indent}- ')
            else:
                self._pending_nl = 0
                self.result.append('\n- ')

        elif tag == 'pre':
            self.in_pre = True
            self._ensure_nl(2)
            self._flush('```\n')

        elif tag == 'code' and not self.in_pre:
            self._flush('`')

        elif tag == 'blockquote':
            self._ensure_nl(2)

        elif tag == 'th':
            self._flush('| ')

        elif tag == 'td':
            self._flush('| ')

        elif tag == 'tr':
            if self._pending_nl == 0:
                self.result.append('\n')

        # div, section, article, main, span, a → just let text through

    def handle_endtag(self, tag):
        if tag in self.BLOCK_TAGS:
            self._pop_skip(tag)
            return
        if self._skipping():
            return

        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self._ensure_nl(2)

        elif tag == 'p':
            self._ensure_nl(2)

        elif tag in ('strong', 'b'):
            self._flush('**')

        elif tag in ('em', 'i'):
            self._flush('*')

        elif tag in ('ul', 'ol'):
            if self.list_stack:
                self.list_stack.pop()
            self._ensure_nl(2)

        elif tag == 'pre':
            self.in_pre = False
            self.result.append('\n```')
            self._ensure_nl(2)

        elif tag == 'code' and not self.in_pre:
            self._flush('`')

        elif tag in ('th', 'td'):
            self._flush(' |')

        elif tag in ('div', 'section', 'article'):
            pass  # no spacing — the content inside handled it

    def handle_data(self, data):
        if self._skipping():
            return
        if self.in_pre:
            self.result.append(data)
            return
        text = data  # keep whitespace mostly intact; collapse only extreme cases
        if text.strip():
            self._flush(text)
        elif self.result and not self.result[-1].endswith('\n'):
            # preserve intra-word spaces
            self._flush(' ')

    def get_markdown(self):
        return ''.join(self.result)


# ─── Content extraction ─────────────────────────────────────────────────────

def extract_advice_content(html: str) -> str:
    """Extract the actual advice text from a CBN page.

    Strategy (ordered by specificity):
    1. The Drupal field div for advice text
    2. The article/node div
    3. The <main> tag
    4. Full <body>
    """
    patterns = [
        # Most specific: the actual advice text field
        r'<div[^>]+field--name-field-advice-text[^>]*>(.*?)</div\s*>\s*</div\s*>',
        # Drupal node content wrapper
        r'<div[^>]+class="[^"]*group-content[^"]*"[^>]*>(.*?)</div\s*>\s*</div\s*>',
        # Article node
        r'<div[^>]+class="[^"]*node--type-advice[^"]*"[^>]*>(.*?)</div\s*>\s*</div\s*>',
        # Main content block
        r'<div[^>]+id="block-cnc-cbn-content"[^>]*>(.*?)</div\s*>\s*</div\s*>',
        # <main> tag
        r'<main[^>]*>(.*?)</main>',
        # body fallback
        r'<body[^>]*>(.*?)</body>',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.DOTALL | re.IGNORECASE)
        if m and len(m.group(1).strip()) > 200:
            return m.group(1)

    return html  # absolute fallback


def clean_markdown(md: str) -> str:
    """Remove navigation noise, collapse blank lines, strip leading whitespace."""
    lines = md.split('\n')
    cleaned = []

    noise_patterns = [
        re.compile(r'^\s*you are here\s*$', re.I),
        re.compile(r'^\s*home\s*$', re.I),
        re.compile(r'^\s*gepubliceerde adviezen\s*$', re.I),
        re.compile(r'^\s*published advi[sc]e[s]?\s*$', re.I),
        re.compile(r'^\s*-\s*select\s*-\s*$', re.I),
        re.compile(r'^\s*\d{1,3}\s*$'),           # lone footnote numbers (1-3 digits)
        re.compile(r'^\s*\|\s*\|\s*$'),             # empty table rows
        re.compile(r'^\s*\\s*$'),
    ]

    for line in lines:
        if any(p.match(line) for p in noise_patterns):
            continue
        cleaned.append(line)

    result = '\n'.join(cleaned)
    result = re.sub(r'\n{3,}', '\n\n', result)  # max 2 blank lines
    result = result.strip()
    return result


# ─── Fetch ──────────────────────────────────────────────────────────────────

def fetch_html(url: str) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml',
            'Accept-Language': 'nl,en;q=0.8',
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            return resp.status, resp.read().decode('utf-8', errors='replace')
    except urllib.error.HTTPError as e:
        return e.code, ''
    except Exception as e:
        return 0, str(e)


# ─── Per-file processing ─────────────────────────────────────────────────────

def extract_url(content: str) -> str | None:
    m = re.search(r'\*\*Bron\*\*:\s*(https?://[^\s\n]+)', content)
    return m.group(1).strip() if m else None


def already_processed(content: str) -> bool:
    """True only if file has the marker AND has substantive content (>20 lines)."""
    if 'markdown via HTML-extractie' not in content:
        return False
    return content.count('\n') > 20


def process_file(filepath: str) -> tuple[str, str]:
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    if already_processed(original):
        return 'skipped', 'already processed'

    url = extract_url(original)
    if not url:
        return 'no_url', 'no URL found'

    status_code, html = fetch_html(url)
    if status_code != 200:
        return 'fetch_error', f'HTTP {status_code}'

    content_html = extract_advice_content(html)

    parser = CBNMarkdownParser()
    parser.feed(content_html)
    raw_md = parser.get_markdown()
    clean_md = clean_markdown(raw_md)

    if len(clean_md) < 100:
        return 'error', f'extracted content too short ({len(clean_md)} chars) — keeping original'

    # Extract title (first # heading)
    title_m = re.search(r'^#{1,2}\s+(.+)$', clean_md, re.MULTILINE)
    if title_m:
        title = title_m.group(1).strip()
        # Remove the H1 from body (we put it in the file header)
        clean_md = (clean_md[:title_m.start()] + clean_md[title_m.end():]).strip()
    else:
        # Fallback: use original H1 from file
        orig_h1 = re.search(r'^#\s+(.+)$', original, re.MULTILINE)
        title = orig_h1.group(1).strip() if orig_h1 else os.path.basename(filepath)

    new_content = f"""---
---

# {title}

**Bron**: {url}
**Status**: markdown via HTML-extractie (eigen parser)

---

{clean_md}
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return 'ok', f'rewritten ({len(clean_md)} chars)'


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    base_dir = '/Users/stivni/Documents/ITAA/certificaid/content/bronnen/adviezen'
    rapport_path = '/Users/stivni/Documents/ITAA/certificaid/.cbn-reprocess-rapport.md'

    test_mode = '--test' in sys.argv
    test_count = int(sys.argv[sys.argv.index('--test') + 1]) if test_mode else None

    files = sorted(f for f in os.listdir(base_dir) if f.endswith('.md'))
    if test_mode:
        files = files[:test_count]

    total = len(files)
    counts = {k: 0 for k in ('ok', 'skipped', 'fetch_error', 'error', 'no_url')}
    errors = []

    print(f'Verwerken {total} bestanden{"  [TEST MODE]" if test_mode else ""}...\n')

    for i, filename in enumerate(files, 1):
        filepath = os.path.join(base_dir, filename)
        try:
            status, msg = process_file(filepath)
        except Exception as e:
            status, msg = 'error', str(e)

        counts[status] = counts.get(status, 0) + 1
        line = f'{i:3d}/{total}  [{status:11s}]  {filename[:60]:<60}  {msg}'
        print(line, flush=True)

        if status in ('fetch_error', 'error', 'no_url'):
            errors.append(line)

        # Write rapport every 50 files (and at the end)
        if i % 50 == 0 or i == total:
            with open(rapport_path, 'w', encoding='utf-8') as f:
                f.write('# CBN herverwerking rapport\n\n')
                f.write(f'Totaal: {total}  |  ok: {counts["ok"]}  |  overgeslagen: {counts["skipped"]}  |  fouten: {counts["fetch_error"] + counts["error"]}\n\n')
                f.write(f'Voortgang: {i}/{total}\n\n')
                if errors:
                    f.write('## Fouten\n\n')
                    for e in errors:
                        f.write(f'- {e}\n')

        if status == 'ok':
            time.sleep(0.35)

    print(f'\n{"─" * 70}')
    print(f'Klaar: {counts["ok"]} herschreven, {counts["skipped"]} overgeslagen, '
          f'{counts.get("fetch_error",0)} fetch-fouten, {counts.get("error",0)} andere fouten')
    if errors:
        print(f'\nFouten ({len(errors)}):')
        for e in errors:
            print(f'  {e}')
    print(f'\nRapport: {rapport_path}')


if __name__ == '__main__':
    main()
