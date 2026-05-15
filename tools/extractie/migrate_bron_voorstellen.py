"""
Eenmalig migratie-script: _bron_voorstellen.json → gaps.json (ADR-008 §16).

Wat dit script doet:
1. Leest data/extractie/_bron_voorstellen.json
2. Converteert elk voorstel naar een gaps.json-entry met aspect_type: "bron-gap"
3. Voegt aspect_type: "concept-gap" toe aan bestaande gaps (als ontbrekend)
4. Schrijft de gecombineerde set terug naar data/extractie/gaps.json
5. Verwijdert _bron_voorstellen.json na succesvolle migratie

Na uitvoering: verwijder dit script (CLAUDE.md regel 9 — geen leftovers).

Gebruik:
  python3 -m tools.extractie.migrate_bron_voorstellen --dry-run
  python3 -m tools.extractie.migrate_bron_voorstellen
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
BRON_VOORSTELLEN_BESTAND = ROOT / "data" / "extractie" / "_bron_voorstellen.json"
GAPS_BESTAND = ROOT / "data" / "extractie" / "gaps.json"


def _laad_gaps(gaps_bestand: Path) -> list[dict]:
    """Laad bestaande gaps.json (leeg als het bestand niet bestaat)."""
    if not gaps_bestand.exists():
        return []
    try:
        data = json.loads(gaps_bestand.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def _laad_bron_voorstellen(bestand: Path) -> list[dict]:
    """Laad _bron_voorstellen.json. Ondersteunt zowel root-lijst als {voorstellen: [...]}."""
    if not bestand.exists():
        return []
    try:
        data = json.loads(bestand.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("voorstellen", [])
    except json.JSONDecodeError:
        return []
    return []


def _voorstel_naar_bron_gap(voorstel: dict) -> dict:
    """Converteer een _bron_voorstellen-entry naar een gaps.json bron-gap entry."""
    return {
        "aspect_type": "bron-gap",
        "aspect": "bron-corpus-uitbreiding",
        "po": voorstel.get("po", ""),
        "anchor_id": voorstel.get("anchor_id", ""),
        "reden": voorstel.get("ontbrekende_kennis", ""),
        "ontbrekende_kennis": voorstel.get("ontbrekende_kennis", ""),
        "voorgestelde_bronnen": voorstel.get("voorgestelde_bronnen", []),
        "menselijke_beslissing": voorstel.get("human_decision", None),
        "prio": "midden",
        "status": "open",
        "geconstateerd_door": voorstel.get("geconstateerd_door", "migrate_bron_voorstellen"),
        "geconstateerd_op": voorstel.get("geconstateerd_op", datetime.now(timezone.utc).isoformat(timespec="seconds")),
    }


def migreer(dry_run: bool = False) -> None:
    """Voer de migratie uit.

    Args:
        dry_run: als True, print preview maar schrijf niets weg
    """
    # 1. Laad bestaande data
    bestaande_gaps = _laad_gaps(GAPS_BESTAND)
    bron_voorstellen = _laad_bron_voorstellen(BRON_VOORSTELLEN_BESTAND)

    print(f"[migratie] Bestaande gaps.json entries: {len(bestaande_gaps)}")
    print(f"[migratie] _bron_voorstellen.json entries: {len(bron_voorstellen)}")

    if not bron_voorstellen:
        if not BRON_VOORSTELLEN_BESTAND.exists():
            print("[migratie] _bron_voorstellen.json niet gevonden — niets te migreren.")
        else:
            print("[migratie] _bron_voorstellen.json is leeg — niets te migreren.")
        return

    # 2. Voeg aspect_type: "concept-gap" toe aan bestaande entries zonder aspect_type
    aangepaste_bestaande = 0
    for gap in bestaande_gaps:
        if "aspect_type" not in gap:
            gap["aspect_type"] = "concept-gap"
            aangepaste_bestaande += 1

    print(f"[migratie] {aangepaste_bestaande} bestaande entries krijgen aspect_type: 'concept-gap'")

    # 3. Converteer bron-voorstellen naar bron-gap entries (dedupliceer op anchor_id)
    bestaande_bron_gap_sleutels = {
        (g.get("po", ""), g.get("anchor_id", ""))
        for g in bestaande_gaps
        if g.get("aspect_type") == "bron-gap"
    }

    nieuwe_bron_gaps: list[dict] = []
    dubbel = 0
    for voorstel in bron_voorstellen:
        sleutel = (voorstel.get("po", ""), voorstel.get("anchor_id", ""))
        if sleutel in bestaande_bron_gap_sleutels:
            dubbel += 1
            continue
        nieuwe_bron_gaps.append(_voorstel_naar_bron_gap(voorstel))
        bestaande_bron_gap_sleutels.add(sleutel)

    print(f"[migratie] {len(nieuwe_bron_gaps)} nieuwe bron-gap entries (overgeslagen: {dubbel} dubbel)")

    # 4. Gecombineerde lijst
    gecombineerd = bestaande_gaps + nieuwe_bron_gaps

    if dry_run:
        print("\n[dry-run] Preview (eerste 3 nieuwe bron-gap entries):")
        for entry in nieuwe_bron_gaps[:3]:
            print(json.dumps(entry, ensure_ascii=False, indent=2))
        print(f"\n[dry-run] Finaal totaal: {len(gecombineerd)} entries")
        print("[dry-run] Geen wijzigingen weggeschreven.")
        return

    # 5. Wegschrijven
    GAPS_BESTAND.parent.mkdir(parents=True, exist_ok=True)
    GAPS_BESTAND.write_text(
        json.dumps(gecombineerd, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"[migratie] gaps.json bijgewerkt: {len(gecombineerd)} entries totaal")

    # 6. _bron_voorstellen.json verwijderen
    BRON_VOORSTELLEN_BESTAND.unlink()
    print(f"[migratie] {BRON_VOORSTELLEN_BESTAND.name} verwijderd.")

    print(f"\n[samenvatting]")
    print(f"  Gemigreerd                 : {len(nieuwe_bron_gaps)} bron-gap entries")
    print(f"  Bestaande entries bijgewerkt: {aangepaste_bestaande} (+ aspect_type: concept-gap)")
    print(f"  Finaal totaal              : {len(gecombineerd)} entries in gaps.json")
    print(f"\nVOLGENDE STAP: verwijder dit script:")
    print(f"  git rm {Path(__file__).relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview: droog uitvoeren zonder wijzigingen.",
    )
    args = parser.parse_args()

    migreer(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
