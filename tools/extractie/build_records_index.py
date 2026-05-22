"""Bouw een compacte records-index voor agent-prompts (schema v1.5).

Outputs (beide in data/concepten/):
- `records-index.json`         — verbose: per record {id, naam, concept_type,
                                  ankers, status, definitie, substantie?, valkuilen}.
                                  Gebruik bij record-update of zoek-tooling.
- `records-index.compact.txt`  — minimaal: één regel per concept_type-groep met ID-lijst.
                                  ~3-5 KB. Inject in agent-prompts voor scope-overlap-check.

Schema v1.5 wijzigingen (t.o.v. v1.4):
- Leest `metadata.ankers` (was `metadata.linked_anchors`).
- Leest `inhoud.kern.definitie.tekst` (was `inhoud.definitie.text`).
- Toont indien aanwezig ook `inhoud.kern.substantie.tekst` (kort) en aantal valkuilen.
- Geen `primary_po` meer (gedropt in v1.5).

CLI:
    python3 -m tools.extractie.build_records_index
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
RECORDS_DIR = REPO_ROOT / "data" / "concepten" / "records"
VERBOSE_OUT = REPO_ROOT / "data" / "concepten" / "records-index.json"
COMPACT_OUT = REPO_ROOT / "data" / "concepten" / "records-index.compact.txt"


def _kort(tekst: str, max_chars: int) -> str:
    tekst = (tekst or "").strip()
    if not tekst:
        return ""
    if len(tekst) <= max_chars:
        return tekst
    return tekst[: max_chars - 1].rstrip() + "…"


def kort_kern_veld(rec: dict, veld: str, max_chars: int = 120) -> str:
    """Haal `inhoud.kern.<veld>.tekst` op en kort indien nodig.

    Schema v1.5: kern-wrapper. `veld` ∈ {definitie, substantie, rationale}.
    """
    inhoud = rec.get("inhoud") or {}
    kern = inhoud.get("kern") or {}
    sub = kern.get(veld) or {}
    if not isinstance(sub, dict):
        return ""
    return _kort(sub.get("tekst", ""), max_chars)


def bouw_index_entry(rec: dict) -> dict:
    naam = rec.get("naam") or {}
    metadata = rec.get("metadata") or {}
    inhoud = rec.get("inhoud") or {}

    entry = {
        "id": rec.get("id", ""),
        "naam": naam.get("primair", ""),
        "concept_type": rec.get("concept_type", ""),
        "ankers": metadata.get("ankers") or [],
        "status": metadata.get("status", "seed"),
    }

    definitie = kort_kern_veld(rec, "definitie", max_chars=120)
    if definitie:
        entry["definitie"] = definitie

    substantie = kort_kern_veld(rec, "substantie", max_chars=100)
    if substantie:
        entry["substantie"] = substantie

    valkuilen = inhoud.get("valkuilen")
    if isinstance(valkuilen, list) and valkuilen:
        entry["valkuilen_count"] = len(valkuilen)

    afkorting = naam.get("afkorting")
    if afkorting:
        entry["afkorting"] = afkorting

    return entry


def bouw_compact_index(entries: list[dict]) -> str:
    """Plat tekst-formaat, ID-only per concept_type-groep.

    Output voorbeeld:
        # Records-index (compact) — 396 records totaal
        # Gebruik: scope-overlap-check vóór nieuw record aanmaken.

        ## instrument (24)
        achtergestelde-lening · banklening · obligatielening · ...

        ## verrichting (17)
        fusie · inkoop-eigen-aandelen · kapitaalvermindering · ...
    """
    groepen: dict[str, list[str]] = {}
    for e in entries:
        groepen.setdefault(e["concept_type"], []).append(e["id"])

    lines = [f"# Records-index (compact) — {len(entries)} records totaal",
             "# Gebruik: scope-overlap-check vóór nieuw record aanmaken.",
             ""]
    for concept_type in sorted(groepen):
        ids = sorted(groepen[concept_type])
        lines.append(f"## {concept_type} ({len(ids)})")
        lines.append(" · ".join(ids))
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Bouw records-index (verbose + compact) — schema v1.5.")
    parser.add_argument("--verbose-only", action="store_true",
                        help="Schrijf alleen verbose JSON, niet compact .txt")
    args = parser.parse_args()

    records = sorted(RECORDS_DIR.glob("*.json"))
    if not records:
        print(f"FOUT: geen records gevonden in {RECORDS_DIR}", file=sys.stderr)
        return 1

    entries = []
    voor_concept_type: dict[str, int] = {}
    voor_status: dict[str, int] = {}
    for pad in records:
        try:
            rec = json.loads(pad.read_text())
        except json.JSONDecodeError as e:
            print(f"  ⚠️  {pad.name}: ongeldige JSON ({e})", file=sys.stderr)
            continue
        entry = bouw_index_entry(rec)
        entries.append(entry)
        voor_concept_type[entry["concept_type"]] = voor_concept_type.get(entry["concept_type"], 0) + 1
        voor_status[entry["status"]] = voor_status.get(entry["status"], 0) + 1

    # Verbose JSON
    verbose_index = {
        "schema_version": "2.1",
        "totaal": len(entries),
        "samenstelling": {
            "per_concept_type": dict(sorted(voor_concept_type.items())),
            "per_status": dict(sorted(voor_status.items())),
        },
        "records": sorted(entries, key=lambda e: e["id"]),
    }
    VERBOSE_OUT.parent.mkdir(parents=True, exist_ok=True)
    VERBOSE_OUT.write_text(json.dumps(verbose_index, ensure_ascii=False, indent=2) + "\n")
    verb_kb = VERBOSE_OUT.stat().st_size / 1024
    print(f"✓ Verbose:  {VERBOSE_OUT.name}  ({verb_kb:.1f} KB)")

    # Compact .txt
    if not args.verbose_only:
        compact = bouw_compact_index(entries)
        COMPACT_OUT.write_text(compact)
        comp_kb = COMPACT_OUT.stat().st_size / 1024
        print(f"✓ Compact:  {COMPACT_OUT.name}  ({comp_kb:.1f} KB)")

    print(f"\n  {len(entries)} records · per_concept_type: {voor_concept_type}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
