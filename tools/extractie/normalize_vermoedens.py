"""
Normaliseert bestaande vermoedens-bestanden (ADR-007, ADR-008).

Leidt `kenniselementen: [code, ...]` af uit het `gekoppeld_aan`-veld:
  - "[4.0.I.D.6]"                             → ["4.0.I.D.6"]
  - "[4.0.I.D.5] / [4.0.I.D.9]"              → ["4.0.I.D.5", "4.0.I.D.9"]
  - "[4.0.I.D.4] Relaties met confraters"     → ["4.0.I.D.4"]
  - "Taak: Een passend beleid vaststellen"    → []
  - "Doelstelling: Een risicoanalyse uitvoer" → []

Voeg ook `schaal_signaal`-placeholder toe als het veld ontbreekt.
`gekoppeld_aan` blijft bewaard voor traceerbaarheid.

Gebruik:
  python tools/extractie/normalize_vermoedens.py \\
      data/extractie/4.0/vermoedens/4.0.D1.1.json

  python tools/extractie/normalize_vermoedens.py \\
      data/extractie/4.0/vermoedens/   # verwerkt alle *.json in die map

  Voeg --dry-run toe om alleen te printen zonder te schrijven.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Patroon voor kenniselement-codes: 4.0.I.D.6, 4.0.I.C, 4.0.I.B, 4.0.I.C.7 …
# ---------------------------------------------------------------------------
_CODE_PAT = re.compile(r"\[(\d+\.\d+\.[A-Z](?:\.[A-Z](?:\.\d+)?)?)\]")


def extraheer_kenniselement_codes(tekst: str) -> list[str]:
    """Extraheer alle kenniselement-codes uit een vrije tekst."""
    if not tekst:
        return []
    return _CODE_PAT.findall(tekst)


def normaliseer_vermoeden(vermoeden: dict) -> dict:
    """
    Voeg `kenniselementen`-veld toe als het ontbreekt of leeg is.
    Voeg `schaal_signaal`-placeholder toe als het veld ontbreekt.
    Muteert het dict in-place en geeft het terug.
    """
    gekoppeld = vermoeden.get("gekoppeld_aan", "")
    codes = extraheer_kenniselement_codes(gekoppeld)

    # Alleen overschrijven als veld ontbreekt of nog leeg is
    if "kenniselementen" not in vermoeden:
        vermoeden["kenniselementen"] = codes

    # schaal_signaal: placeholder als ontbreekt — subagent vult in
    if "schaal_signaal" not in vermoeden:
        vermoeden["schaal_signaal"] = ""   # leeg → subagent beslist

    return vermoeden


def normaliseer_bestand(pad: Path, *, droog: bool = False) -> int:
    """
    Lees vermoedens-JSON, normaliseer elk vermoeden, schrijf terug (tenzij droog=True).
    Geeft het aantal gemuteerde vermoedens terug.
    """
    data = json.loads(pad.read_text(encoding="utf-8"))
    vermoedens = data.get("vermoedens", [])
    gewijzigd = 0

    for v in vermoedens:
        had_ke = "kenniselementen" in v
        normaliseer_vermoeden(v)
        if not had_ke:
            gewijzigd += 1

    _print_samenvatting(pad, vermoedens, droog=droog)

    if not droog:
        pad.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    return gewijzigd


def _print_samenvatting(pad: Path, vermoedens: list[dict], *, droog: bool) -> None:
    label = "[DRY-RUN] " if droog else ""
    print(f"{label}{pad.name}: {len(vermoedens)} vermoedens")
    for v in vermoedens:
        ke = v.get("kenniselementen", [])
        schaal = v.get("schaal_signaal", "")
        naam = v["naam"][:50]
        ke_str = ", ".join(ke) if ke else "—"
        print(f"  {naam!r:55} ke={ke_str}  schaal={schaal or '?'}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Normaliseer vermoedens: extraheer kenniselement-codes uit gekoppeld_aan."
    )
    parser.add_argument(
        "pad",
        help="Vermoedens-JSON of map met *.json-bestanden",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print resultaat maar schrijf niet terug",
    )
    args = parser.parse_args()

    doelpad = Path(args.pad)
    if doelpad.is_dir():
        bestanden = sorted(doelpad.glob("*.json"))
        if not bestanden:
            print(f"Geen *.json gevonden in {doelpad}")
            sys.exit(1)
    elif doelpad.is_file():
        bestanden = [doelpad]
    else:
        print(f"Pad bestaat niet: {doelpad}")
        sys.exit(1)

    totaal = 0
    for bestand in bestanden:
        totaal += normaliseer_bestand(bestand, droog=args.dry_run)

    if not args.dry_run:
        print(f"\n✓ {totaal} vermoeden(s) aangevuld met kenniselementen-veld.")
    else:
        print("\n(dry-run — geen bestanden aangepast)")


if __name__ == "__main__":
    main()
