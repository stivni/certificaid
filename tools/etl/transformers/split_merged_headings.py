"""Transformer: splits gemerged hiërarchie-headings op één regel.

Belgische wetteksten gebruiken een hiërarchie `DEEL > BOEK > TITEL > HOOFDSTUK >
AFDELING > ONDERAFDELING` (ADR-005 §7). Soms rendert de PDF-extractor twee
opeenvolgende niveaus op één regel, gescheiden met ` - `:

    `##### Afdeling 1. Gemeenschappelijke bepalingen. - Onderafdeling 2. Bevoegdheden.`

Dat is een merge die `inject_headings_wettekst` (of de extractor zelf) heeft
gemaakt — beide structuurlabels zaten in het PDF-block als één regel. Gevolg:
de hiërarchie-detectie via `process_wettekst.detect_hierarchy` ziet het diepere
niveau (ONDERAFDELING) niet als aparte rank.

Deze transformer detecteert het patroon en splitst in twee headings, met de
tweede één markdown-niveau dieper.

Conform ADR-005 §1: format-agnostische tekst-transformatie → transformer-laag.
"""
from __future__ import annotations

import re

# Belgische wettekst-hiërarchie labels (case-insensitive match).
# Volgorde belangrijk: langere labels eerst zodat regex ze prefereert.
_LABELS = r"(?:Onderafdeling|Hoofdstuk|Afdeling|Titel|Boek|Deel|ONDERAFDELING|HOOFDSTUK|AFDELING|TITEL|BOEK|DEEL)"

# Match: `^(#+) (LABEL_A) X. <rest1>. - (LABEL_B) Y. <rest2>$`
#
# Voorbeelden:
#   `##### Afdeling 1. Gemeenschappelijke bepalingen. - Onderafdeling 2. Foo.`
#   `## DEEL 3. De verenigingen en stichtingen. - BOEK 9. VZW.`
#
# `<rest1>` mag zelf geen ` - ` bevatten (anders ambigu). Capture-groepen:
#   1=hashes  2=label_a  3=num_a  4=tail_a  5=label_b  6=num_b  7=tail_b
_MERGED_HEADING_RE = re.compile(
    rf"^(#+)\s+"
    rf"({_LABELS})\s+([^\s.]+)\.\s*([^\n]*?)\s+-\s+"
    rf"({_LABELS})\s+([^\s.]+)\.\s*(.*)$",
)


def split_merged_headings(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Splits regels met `## Label A X. ... - Label B Y. ...` in twee headings.

    Het diepere label krijgt één extra `#` (één niveau dieper) in markdown.
    """
    out_lines: list[str] = []
    for line in body.split("\n"):
        m = _MERGED_HEADING_RE.match(line)
        if not m:
            out_lines.append(line)
            continue
        hashes, label_a, num_a, tail_a, label_b, num_b, tail_b = m.groups()
        deeper_hashes = hashes + "#" if len(hashes) < 6 else hashes
        # Eerste heading
        first = f"{hashes} {label_a} {num_a}." + (f" {tail_a.strip()}" if tail_a.strip() else "")
        # Tweede heading, één niveau dieper
        second = f"{deeper_hashes} {label_b} {num_b}." + (f" {tail_b.strip()}" if tail_b.strip() else "")
        out_lines.append(first)
        out_lines.append("")  # lege regel tussen headings
        out_lines.append(second)
    return "\n".join(out_lines), frontmatter
