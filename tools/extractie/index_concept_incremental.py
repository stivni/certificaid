"""
Embed één concept-record en upsert in de `concepten` ChromaDB-collection (ADR-006).

Probeert altijd eerst de embedding-daemon op localhost:8765 (ADR-018). Als de daemon
niet bereikbaar is, valt het script terug op een directe in-process bge-m3-load.

Bedoeld voor twee situaties:
  1. Na elke nieuwe seed-write door de extractie-subagent (live duplicate-check).
  2. Bulk-(her)indexering van alle bestaande concept_records/*.json.

Gebruik:
  # Eén concept indexeren
  python tools/extractie/index_concept_incremental.py \\
      --concept data/concept_records/beroepsgeheim-gecertificeerd-accountant.json

  # Alle concepten (her)indexeren
  python tools/extractie/index_concept_incremental.py --alle

  # Drempelcheck: vergelijk query met alle concepten (duplicate-check preview)
  python tools/extractie/index_concept_incremental.py \\
      --duplicaat-check "Beroepsgeheim van de gecertificeerd accountant" \\
      [--drempel 0.80]

  Flags:
    --chroma    ChromaDB-pad (default: data/chroma_db)
    --dry-run   Toon wat geïndexeerd zou worden, schrijf niet naar ChromaDB
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from lib.embedding_client import duplicate_check as client_duplicate_check
from lib.embedding_client import index_concept as client_index_concept
from lib.embedding_client import is_daemon_alive

CONCEPT_DIR = ROOT / "data" / "concept_records"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def laad_concept(pad: Path) -> dict:
    return json.loads(pad.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Embed één (of alle) concept-record(s) in de `concepten` ChromaDB-collection. "
            "Gebruikt de embedding-daemon als die draait (ADR-018), anders in-process."
        )
    )
    groep = parser.add_mutually_exclusive_group(required=True)
    groep.add_argument(
        "--concept",
        help="Pad naar een concept-record JSON (bijv. data/concept_records/beroepsgeheim.json)",
    )
    groep.add_argument(
        "--alle",
        action="store_true",
        help=f"Indexeer alle *.json in {CONCEPT_DIR.relative_to(ROOT)}",
    )
    groep.add_argument(
        "--duplicaat-check",
        metavar="NAAM",
        help="Controleer of een conceptnaam al bestaat in de collection (geen upsert)",
    )
    parser.add_argument(
        "--chroma",
        default=None,
        help="ChromaDB-pad (default: data/chroma_db)",
    )
    parser.add_argument(
        "--drempel",
        type=float,
        default=0.80,
        help="Rerank-drempel voor duplicaat-check (default: 0.80)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Toon wat geïndexeerd zou worden, schrijf niet",
    )
    args = parser.parse_args()

    chroma_pad = str(
        Path(args.chroma).resolve() if args.chroma
        else ROOT / "data" / "chroma_db"
    )

    # Status-melding: via daemon of in-process?
    daemon_actief = is_daemon_alive()
    modus = "via daemon (localhost:8765)" if daemon_actief else "in-process (daemon offline)"
    print(f"→ Modus: {modus}", file=sys.stderr)

    # --- Duplicaat-check modus ---
    if args.duplicaat_check:
        query = args.duplicaat_check
        print(f"→ Duplicaat-check voor: {query!r}", file=sys.stderr)
        resultaat = client_duplicate_check(
            naam=query,
            chroma_path=chroma_pad,
            threshold=args.drempel,
        )
        matches = resultaat.get("matches", [])
        top1    = resultaat.get("top1")
        totaal  = resultaat.get("total_in_collection", 0)

        print(f"  Collection bevat {totaal} concept(en).")
        if matches:
            print(f"  {len(matches)} kandidaat(en) boven drempel {args.drempel}:")
            for k in matches:
                print(
                    f"    [{k.get('rerank_score', k.get('bi_score', 0)):.3f}] "
                    f"{k['naam']!r} (id: {k['concept_id']})"
                )
        else:
            print(f"  Geen duplicaten gevonden boven drempel {args.drempel}.")
            if top1:
                score = top1.get("rerank_score", top1.get("bi_score", 0))
                print(
                    f"  Top-1 (onder drempel): [{score:.3f}] "
                    f"{top1['naam']!r} (id: {top1['concept_id']})"
                )
        return

    # --- Indexeer één of alle concepten ---
    if args.alle:
        if not CONCEPT_DIR.exists():
            print(f"Concept_records-map niet gevonden: {CONCEPT_DIR}", file=sys.stderr)
            sys.exit(1)
        # rglob: ook subdirectories per PO (data/concept_records/1.4/*.json etc.)
        # Filter underscore-files (_voorgestelde_types.yaml etc.)
        bestanden = sorted(p for p in CONCEPT_DIR.rglob("*.json")
                           if not p.name.startswith("_"))
        if not bestanden:
            print("Geen concept-records gevonden.", file=sys.stderr)
            sys.exit(0)
        print(f"→ {len(bestanden)} concept(en) indexeren …", file=sys.stderr)
    else:
        pad = Path(args.concept)
        if not pad.exists():
            print(f"Bestand niet gevonden: {pad}", file=sys.stderr)
            sys.exit(1)
        bestanden = [pad]

    geindexeerd = 0
    for bestand in bestanden:
        try:
            record = laad_concept(bestand)
        except Exception as exc:
            print(f"  Fout bij laden {bestand.name}: {exc}", file=sys.stderr)
            continue

        concept_id = record.get("id") or record.get("naam", bestand.stem)

        if args.dry_run:
            print(f"  [dry-run] zou indexeren: {concept_id!r}")
            geindexeerd += 1
            continue

        try:
            resultaat_id = client_index_concept(record=record, chroma_path=chroma_pad)
            print(f"  ✓ {resultaat_id}")
            geindexeerd += 1
        except Exception as exc:
            print(f"  ✗ Fout bij indexeren {concept_id!r}: {exc}", file=sys.stderr)

    actie = "zou indexeren" if args.dry_run else "geïndexeerd"
    print(f"\n{geindexeerd} concept(en) {actie}.", file=sys.stderr)


if __name__ == "__main__":
    main()
