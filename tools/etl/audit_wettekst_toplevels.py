#!/usr/bin/env python3
"""
Audit-tool: detecteer wetteksten met vermoedelijke conversie-bugs.

Controles:
1. Start het eerste artikel met nummer 1 (of 1:1)?
   → Zo niet: mogelijke conversie-bug (eerste artikels ontbreken in de MD).
2. Start de eerste structuurlabel-sectie met nummer 1 (of I)?
   → Zo niet: mogelijke conversie-bug (begin van de wet ontbreekt).
3. Is het document helemaal leeg (geen artikel-headings)?
   → Speciaal geval: TOC-only of niet-geconverteerd bestand.

Output: tekstrapport en optioneel JSON.

Gebruik:
    python tools/etl/audit_wettekst_toplevels.py
    python tools/etl/audit_wettekst_toplevels.py --json data/qa/audit-toplevels.json
    python tools/etl/audit_wettekst_toplevels.py --file resources/bronnen/wetteksten/WVV.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

WETTEKSTEN_DIR = ROOT / "resources" / "bronnen" / "wetteksten"
SKIP_FILES = {"INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"}

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)

# Artikel-heading: `## Art. X` of `##### Art. 1:2` etc.
_ART_HEADING_RE = re.compile(r"^#{1,6}\s+(Art\.|Par\.)\s+(\S+)")

# Structuurlabel-heading: `## BOEK 1.` of `### Afdeling I.` etc.
_STRUCT_HEADING_RE = re.compile(
    r"^#{1,6}\s+"
    r"(BOEK|DEEL|TITEL|HOOFDSTUK|AFDELING|ONDERAFDELING)"
    r"\s+"
    r"(\S+)",
    re.IGNORECASE,
)

# "Nummer 1"-patronen voor artikel en structuurlabel
_IS_FIRST_NR_RE = re.compile(
    r"^(?:1(?::\d+)?|I|i)[\.\-–—\s,]?$"   # 1, 1:1, I, i
)


def _is_first_number(nr_str: str) -> bool:
    """Geeft True als nr_str een "begin"-nummer is (1, 1:1, I, i)."""
    nr = nr_str.rstrip(".,;:")
    return bool(_IS_FIRST_NR_RE.match(nr))


def _extract_body(text: str) -> str:
    m = _FRONTMATTER_RE.match(text)
    return text[m.end():] if m else text


def audit_bestand(path: Path) -> dict:
    """
    Voer audit uit op één wettekst-MD.

    Returns: dict met 'bestand', 'bevindingen' (list van str), 'niveau' (ok/warn/bug)
    """
    text = path.read_text(encoding="utf-8")
    body = _extract_body(text)
    lines = body.split("\n")

    bevindingen: list[str] = []
    niveau = "ok"

    # Zoek eerste artikel-heading
    eerste_art_nr: str | None = None
    eerste_art_lijn: int | None = None
    for i, line in enumerate(lines):
        m = _ART_HEADING_RE.match(line)
        if m:
            eerste_art_nr = m.group(2)
            eerste_art_lijn = i + 1
            break

    if eerste_art_nr is None:
        bevindingen.append("Geen artikel-heading (Art./Par.) gevonden — TOC-only of niet-geconverteerd")
        niveau = "warn"
    elif not _is_first_number(eerste_art_nr):
        bevindingen.append(
            f"Eerste artikel is Art. {eerste_art_nr} (regel {eerste_art_lijn}) — "
            f"verwacht Art. 1 of Art. 1:1; begin van wet ontbreekt mogelijk"
        )
        niveau = "bug"

    # Zoek eerste structuurlabel-heading
    eerste_struct_label: str | None = None
    eerste_struct_nr: str | None = None
    eerste_struct_lijn: int | None = None
    for i, line in enumerate(lines):
        m = _STRUCT_HEADING_RE.match(line)
        if m:
            eerste_struct_label = m.group(1).upper()
            eerste_struct_nr = m.group(2).rstrip(".,;:")
            eerste_struct_lijn = i + 1
            break

    if eerste_struct_label and eerste_struct_nr:
        eerste_nr_clean = eerste_struct_nr.lstrip("0")
        if not _is_first_number(eerste_nr_clean):
            bevindingen.append(
                f"Eerste {eerste_struct_label} is nr. {eerste_struct_nr} (regel {eerste_struct_lijn}) — "
                f"verwacht {eerste_struct_label} 1 of I; begin van structuur ontbreekt mogelijk"
            )
            niveau = "bug"

    if not bevindingen:
        bevindingen.append("Geen problemen gevonden")

    return {
        "bestand": path.name,
        "eerste_artikel": f"Art. {eerste_art_nr} (regel {eerste_art_lijn})" if eerste_art_nr else "—",
        "eerste_structuurlabel": (
            f"{eerste_struct_label} {eerste_struct_nr} (regel {eerste_struct_lijn})"
            if eerste_struct_label else "—"
        ),
        "bevindingen": bevindingen,
        "niveau": niveau,
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--file", type=Path,
                   help="Auditeer één specifiek bestand")
    p.add_argument("--json", type=Path,
                   help="Schrijf JSON-rapport naar dit pad")
    p.add_argument("--only-bugs", action="store_true",
                   help="Toon enkel bestanden met niveau 'bug'")
    args = p.parse_args()

    if args.file:
        targets = [args.file.resolve()]
    else:
        targets = sorted(
            f for f in WETTEKSTEN_DIR.glob("*.md")
            if f.name not in SKIP_FILES
        )

    print(f"Audit wettekst-toplevels — {len(targets)} bestand(en)\n")

    resultaten: list[dict] = []
    n_bug = 0
    n_warn = 0

    for path in targets:
        r = audit_bestand(path)
        resultaten.append(r)
        if r["niveau"] == "bug":
            n_bug += 1
        elif r["niveau"] == "warn":
            n_warn += 1

        if args.only_bugs and r["niveau"] not in ("bug", "warn"):
            continue

        icon = {"ok": "✓", "warn": "⚠️", "bug": "✗"}.get(r["niveau"], "?")
        print(f"  {icon} {path.name}")
        if r["niveau"] in ("bug", "warn"):
            print(f"    eerste artikel: {r['eerste_artikel']}")
            if r["eerste_structuurlabel"] != "—":
                print(f"    eerste structuur: {r['eerste_structuurlabel']}")
            for b in r["bevindingen"]:
                print(f"    → {b}")

    print(f"\n{'─' * 70}")
    print(f"Resultaat: {len(resultaten)} bestanden — {n_bug} bug(s), {n_warn} warn(s), "
          f"{len(resultaten) - n_bug - n_warn} ok")

    if n_bug > 0:
        print(f"\n💡 Bestanden met 'bug': conversie-fix nodig vóór trust-markering.")
        print(f"   Raadpleeg de officiële ejustice-bron en voeg ontbrekende inhoud toe.")

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(
            json.dumps(resultaten, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"\nJSON-rapport: {args.json}")


if __name__ == "__main__":
    main()
