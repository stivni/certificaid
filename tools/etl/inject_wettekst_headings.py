#!/usr/bin/env python3
"""
ETL-fix: converteer plain-text structuurlabels in wetteksten naar Markdown-headings.

Wetteksten omgezet via convert.py bevatten hierarchische labels als gewone
tekstregel in plaats van als Markdown-heading:

    VOOR:   "  HOOFDSTUK 2. - Definities"
    NA:     "#### HOOFDSTUK 2. - Definities"

Dit script past de conversie direct toe op de bronbestanden, zodat de tijdelijke
workaround `_herstel_structuurheadings()` in `tools/rag/rag_index.py` overbodig
wordt.

Hiërarchie (afgestemd op de structuur waarbij `## Art.` de chunk-grens vormt):

    BOEK / DEEL     →  ##    (bovenste structuurniveau)
    TITEL           →  ###
    HOOFDSTUK       →  ####
    AFDELING        →  #####
    ONDERAFDELING / SECTIE / PARAGRAAF / ONDERDEEL → ######

Gebruik:
    python tools/etl/inject_wettekst_headings.py              # dry-run (geen wijzigingen)
    python tools/etl/inject_wettekst_headings.py --apply      # schrijf wijzigingen
    python tools/etl/inject_wettekst_headings.py --file resources/bronnen/wetteksten/WVV.md
    python tools/etl/inject_wettekst_headings.py --apply --file ...
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

WETTEKSTEN_DIR = ROOT / "resources" / "bronnen" / "wetteksten"
SKIP_FILES = {"INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"}

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)

# ─── Hiërarchie-mapping ───────────────────────────────────────────────────────

_DIEPTE: dict[str, str] = {
    "BOEK":          "##",
    "DEEL":          "##",
    "TITEL":         "###",
    "HOOFDSTUK":     "####",
    "AFDELING":      "#####",
    "ONDERAFDELING": "######",
    "SECTIE":        "######",
    "PARAGRAAF":     "######",
    "ONDERDEEL":     "######",
}

# Patronen dat UITSLUITEND een structuurlabel + nummer/Romeins/letter is
# (afgestemd op _PLAIN_STRUCTUUR_RE in rag_index.py, uitgebreid met NBSP \xa0)
_STRUCTUUR_RE = re.compile(
    r"^[\s\xa0]*"
    r"(BOEK|DEEL|TITEL|HOOFDSTUK|AFDELING|ONDERAFDELING|SECTIE|PARAGRAAF|ONDERDEEL)"
    r"\s+"
    r"(?:[IVXLCDM]+[a-z]*|\d+[a-z]*|[A-Z][a-z]*)"   # Romeins, arabisch, of letter
    r"(?:\s*[\.\-–—]|\s|$)",                           # gevolgd door ., -, –, — spatie of einde
    re.IGNORECASE,
)


# ─── Conversie ───────────────────────────────────────────────────────────────

def converteer_body(body: str) -> tuple[str, int]:
    """
    Converteer plain-text structuurlabels in `body` naar Markdown-headings.

    Returnt: (nieuwe_body, aantal_conversies)

    Veiligheid:
    - Regels die al starten met `#` worden niet aangeraakt.
    - Lege regels worden overgeslagen.
    - Alleen regels die volledig aan het patroon voldoen worden geconverteerd
      (structuurlabel + nummer; labels halverwege een alinea blijven onaangeroerd).
    """
    regels = body.split("\n")
    resultaat: list[str] = []
    n_conversies = 0

    for regel in regels:
        stripped = regel.strip()

        # Sla over: al een heading of leeg
        if not stripped or stripped.startswith("#"):
            resultaat.append(regel)
            continue

        m = _STRUCTUUR_RE.match(regel)
        if m:
            keyword = m.group(1).upper()
            diepte = _DIEPTE.get(keyword, "###")
            resultaat.append(f"{diepte} {stripped}")
            n_conversies += 1
        else:
            resultaat.append(regel)

    return "\n".join(resultaat), n_conversies


def verwerk_bestand(path: Path, *, dry_run: bool = True) -> tuple[int, bool]:
    """
    Verwerk één wettekst-MD. Returnt (n_conversies, gewijzigd).
    Bij dry_run=True worden geen bestanden geschreven.
    """
    text = path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    if m:
        frontmatter_raw = text[: m.end()]
        body = text[m.end():]
    else:
        frontmatter_raw = ""
        body = text

    nieuwe_body, n_conversies = converteer_body(body)

    if n_conversies == 0:
        return 0, False

    if not dry_run:
        path.write_text(frontmatter_raw + nieuwe_body, encoding="utf-8")

    return n_conversies, True


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--apply", action="store_true",
                   help="Schrijf wijzigingen naar bestanden (default: dry-run)")
    p.add_argument("--file", type=Path,
                   help="Verwerk één specifiek bestand i.p.v. alle wetteksten")
    args = p.parse_args()

    if args.file:
        targets = [args.file.resolve()]
    else:
        targets = sorted(
            f for f in WETTEKSTEN_DIR.glob("*.md")
            if f.name not in SKIP_FILES
        )

    dry_run = not args.apply
    modus = "[DRY-RUN]" if dry_run else "[APPLY]"
    print(f"{modus} inject_wettekst_headings — {len(targets)} bestand(en)\n")

    totaal_conversies = 0
    gewijzigd: list[tuple[Path, int]] = []

    for path in targets:
        n, changed = verwerk_bestand(path, dry_run=dry_run)
        if changed:
            totaal_conversies += n
            gewijzigd.append((path, n))
            actie = "zou wijzigen" if dry_run else "gewijzigd"
            print(f"  {actie:14s} {path.name:<70}  ({n} conversies)")

    print(f"\n{'─' * 70}")
    print(f"{modus} {len(gewijzigd)}/{len(targets)} bestanden gewijzigd, "
          f"{totaal_conversies} structuurlabels → headings")

    if dry_run and gewijzigd:
        print("\nGebruik --apply om de wijzigingen door te voeren.")


if __name__ == "__main__":
    main()
