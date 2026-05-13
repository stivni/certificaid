r"""Transformer: strip TOC-headings die later in body als 'echte' heading herhaald worden.

KB24 toont het patroon: bovenaan staan TOC-entries voor afdelingen, met
de echte heading-versies verderop in de body. De TOC-entries hebben vaak
een uitgebreide titel met optionele Art-range, terwijl de echte versie
korter is:

  ## AFDELING 1. Betalingen op de rekeningen van "btw-ontvangsten"
  Brussel, "Inning en Invordering", ...
  ### Onderafdeling 4. Betaling op de postrekening van "VAT on E-Services"
  Disposition temporaire Art. 13ter

  ## AFDELING 1                                ← echte heading
  Betalingen op de rekeningen ...

Algoritme:
1. Pak alle heading-regels in eerste 100 regels (na intro).
2. Voor elke heading: extract `<prefix>` + `<label>` + `<num>` (bv. "AFDELING 1").
3. Zoek of er een DUPLICAAT van zelfde prefix+label+num voorkomt LATER in body.
4. Als duplicaat bestaat → strip de eerste (TOC) versie + eventuele continuation-lines.

Conservatief: alleen wanneer duplicaat exact match heeft.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# Match `## AFDELING 1. ...` of `### Onderafdeling 4. ...` of `## HOOFDSTUK II. ...`
_HEADING_LABEL_RE = re.compile(
    r"^(?P<prefix>#{2,6})\s+"
    r"(?P<label>AFDELING|Onderafdeling|Hoofdstuk|HOOFDSTUK|Afdeling|TITEL|DEEL|BOEK)\s+"
    r"(?P<num>\d+\w*|[IVXLCDM]+\w*)\b",
)


def strip_duplicate_toc_headings(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip TOC-headings die als duplicaat verderop in body voorkomen."""
    lines = body.split("\n")
    n = len(lines)
    if n < 20:
        return body, frontmatter

    # Bekijk alleen de eerste 50 regels (TOC zit aan begin).
    scan_end = min(50, n)

    # Verzamel heading-info per regel (alleen heading-regels)
    toc_candidates: list[tuple[int, str]] = []  # (line_idx, label_key)
    for i in range(scan_end):
        m = _HEADING_LABEL_RE.match(lines[i])
        if m:
            key = f"{m.group('prefix')} {m.group('label').upper()} {m.group('num').upper()}"
            toc_candidates.append((i, key))

    if not toc_candidates:
        return body, frontmatter

    # Zoek voor elke candidate naar duplicaat in body AFTER de candidate-line.
    # Een candidate is TOC-entry als er een latere heading is met zelfde key.
    keys_to_strip: set[str] = set()
    for idx, key in toc_candidates:
        prefix, label, num = key.split(" ", 2)
        # Match heading van zelfde label+num verderop (na deze candidate)
        pattern = re.compile(
            rf"^{re.escape(prefix)}\s+{label}\s+{num}\b",
            re.M | re.I,
        )
        # Zoek in body NA huidige regel
        later = "\n".join(lines[idx + 1:])
        if pattern.search(later):
            keys_to_strip.add(key)

    if not keys_to_strip:
        return body, frontmatter

    # Strip de TOC-versies + hun continuation-lijnen. Per key: alleen de
    # EERSTE voorkomen strippen — de latere is de echte heading.
    stripped_keys: set[str] = set()
    out: list[str] = []
    i = 0
    while i < n:
        line = lines[i]
        m = _HEADING_LABEL_RE.match(line) if i < scan_end else None
        if m:
            key = f"{m.group('prefix')} {m.group('label').upper()} {m.group('num').upper()}"
            if key in keys_to_strip and key not in stripped_keys:
                stripped_keys.add(key)
                # Skip deze heading + eventuele continuation (non-blank, niet heading) tot blanco
                i += 1
                while i < n:
                    nxt = lines[i].strip()
                    if not nxt:
                        break
                    if _HEADING_LABEL_RE.match(lines[i]):
                        break
                    i += 1
                continue
        out.append(line)
        i += 1
    new_body = "\n".join(out)
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, frontmatter
