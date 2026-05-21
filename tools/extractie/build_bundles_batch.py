"""Bulk context-bundle builder voor concept-extract (2-pass architectuur).

Bouwt bundles voor meerdere fiches sequentieel via build_context_bundle.build_bundle().
Daemon-model is eenmalig gewarmd; subsequente calls profiteren van gecachede verbinding.

Usage:
    # Alle fiches voor een programmaonderdeel
    python3 -m tools.extractie.build_bundles_batch --po 1.1

    # Alle openstaande fiches (status != gerealiseerd)
    python3 -m tools.extractie.build_bundles_batch --all

    # Subset uit bestand (één fiche_id per regel)
    python3 -m tools.extractie.build_bundles_batch --from-file fiches.txt

    # Met extra opties
    python3 -m tools.extractie.build_bundles_batch --po 2.3 --top-k-bronnen 7 --no-full-2pass

Opties:
    --po <code>          Filtert op primary_po exact (bv. "1.1", "2.3")
    --all                Alle fiches in candidates.sqlite3
    --from-file <pad>    Lees fiche_id-lijst uit bestand (één per regel)
    --max-v1 N           Max v1-records per bundle (default 3)
    --max-onderdelen-queries N  Max kind-specifieke queries per bundle (default 3)
    --top-k-bronnen N    Top-K per bronnen-query (default 5)
    --no-full-2pass      Legacy mode: pending-markers in bundle i.p.v. echte daemon-calls
    --skip-existing      Sla fiches over waarvoor al een bundle bestaat
    --out-dir <pad>      Output-directory (default: data/extractie/_bundles/)
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DB_PATH = REPO / "data" / "extractie" / "candidates.sqlite3"
BUNDLES_DIR = REPO / "data" / "extractie" / "_bundles"

# Import na path-setup zodat tools.extractie module beschikbaar is
sys.path.insert(0, str(REPO))
from tools.extractie.build_context_bundle import build_bundle, _daemon_beschikbaar  # noqa: E402


def _laad_fiches_voor_po(po: str) -> list[str]:
    """Alle fiche_ids met primary_po == po."""
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT fiche_id FROM candidates WHERE primary_po = ? ORDER BY fiche_id",
        (po,),
    ).fetchall()
    conn.close()
    return [r[0] for r in rows]


def _laad_alle_fiches() -> list[str]:
    """Alle fiche_ids, ongeacht status."""
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("SELECT fiche_id FROM candidates ORDER BY fiche_id").fetchall()
    conn.close()
    return [r[0] for r in rows]


def _laad_fiches_uit_bestand(pad: Path) -> list[str]:
    """Lees fiche_ids uit bestand — één per regel, # is commentaar."""
    fiches = []
    for regel in pad.read_text().splitlines():
        regel = regel.strip()
        if regel and not regel.startswith("#"):
            fiches.append(regel)
    return fiches


def main() -> None:
    ap = argparse.ArgumentParser(description="Bulk context-bundle builder.")
    groep = ap.add_mutually_exclusive_group(required=True)
    groep.add_argument("--po", help="Filtert op primary_po (bv. '1.1')")
    groep.add_argument("--all", action="store_true", help="Alle fiches")
    groep.add_argument("--from-file", metavar="PAD", help="Bestand met fiche_id-lijst")

    ap.add_argument("--max-v1", type=int, default=3)
    ap.add_argument("--max-onderdelen-queries", type=int, default=3)
    ap.add_argument("--top-k-bronnen", type=int, default=5)
    ap.add_argument("--no-full-2pass", action="store_true",
                    help="Legacy pending-markers (geen daemon-calls)")
    ap.add_argument("--skip-existing", action="store_true",
                    help="Sla fiches over waarvoor al een bundle bestaat")
    ap.add_argument("--out-dir", help="Output-directory (default: data/extractie/_bundles/)")
    args = ap.parse_args()

    # Bepaal fiche-lijst
    if args.po:
        fiches = _laad_fiches_voor_po(args.po)
        print(f"▶ {len(fiches)} fiches voor primary_po={args.po}", file=sys.stderr)
    elif getattr(args, "all"):
        fiches = _laad_alle_fiches()
        print(f"▶ {len(fiches)} fiches totaal", file=sys.stderr)
    else:
        pad = Path(args.from_file)
        if not pad.exists():
            print(f"Bestand niet gevonden: {pad}", file=sys.stderr)
            sys.exit(1)
        fiches = _laad_fiches_uit_bestand(pad)
        print(f"▶ {len(fiches)} fiches uit {pad}", file=sys.stderr)

    if not fiches:
        print("Geen fiches gevonden.", file=sys.stderr)
        sys.exit(0)

    out_dir = Path(args.out_dir) if args.out_dir else BUNDLES_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    full_2pass = not args.no_full_2pass

    # Controleer daemon eenmalig
    if full_2pass:
        if _daemon_beschikbaar():
            print("✓ Daemon bereikbaar op localhost:8765 (full-2pass modus)", file=sys.stderr)
        else:
            print(
                "⚠ Daemon NIET bereikbaar — automatische fallback naar legacy pending-markers.",
                file=sys.stderr,
            )
            print(
                "  Start daemon met: launchctl kickstart -k gui/$(id -u)/com.certificaid.embedding-daemon",
                file=sys.stderr,
            )
            full_2pass = False

    # Statistieken
    totaal = len(fiches)
    geslaagd = 0
    overgeslagen = 0
    mislukt: list[tuple[str, str]] = []
    totaal_hits = 0
    totaal_grootte_kb = 0.0
    totaal_tijd = 0.0

    print(f"\n{'─' * 60}", file=sys.stderr)

    batch_t0 = time.time()
    for i, fiche_id in enumerate(fiches, 1):
        out_path = out_dir / f"{fiche_id}.json"

        if args.skip_existing and out_path.exists():
            print(f"[{i:3d}/{totaal}] SKIP  {fiche_id} (al bestaat)", file=sys.stderr)
            overgeslagen += 1
            continue

        try:
            fiche_t0 = time.time()
            bundle = build_bundle(
                fiche_id,
                max_v1=args.max_v1,
                max_onderdelen_queries=args.max_onderdelen_queries,
                top_k_bronnen=args.top_k_bronnen,
                full_2pass=full_2pass,
            )
            out_path.write_text(json.dumps(bundle, ensure_ascii=False, indent=2))

            fiche_tijd = time.time() - fiche_t0
            size_kb = out_path.stat().st_size / 1024
            n_hits = sum(
                sum(1 for h in b.get("hits", []) if "_pending" not in h)
                for b in bundle["bronnen_resultaten"]
            )
            modus_indicator = "2P" if bundle.get("full_2pass") else "LP"

            print(
                f"[{i:3d}/{totaal}] OK    {fiche_id:<40} "
                f"{size_kb:6.1f} KB  {fiche_tijd:5.1f}s  {n_hits} hits  [{modus_indicator}]",
                file=sys.stderr,
            )

            geslaagd += 1
            totaal_hits += n_hits
            totaal_grootte_kb += size_kb
            totaal_tijd += fiche_tijd

        except Exception as exc:
            print(
                f"[{i:3d}/{totaal}] FOUT  {fiche_id:<40} {exc}",
                file=sys.stderr,
            )
            mislukt.append((fiche_id, str(exc)))

    # Samenvatting
    batch_tijd = time.time() - batch_t0
    print(f"\n{'─' * 60}", file=sys.stderr)
    print(f"Klaar in {batch_tijd:.1f}s totaal", file=sys.stderr)
    print(f"  Geslaagd:      {geslaagd}/{totaal}", file=sys.stderr)
    print(f"  Overgeslagen:  {overgeslagen}", file=sys.stderr)
    print(f"  Mislukt:       {len(mislukt)}", file=sys.stderr)
    print(f"  Totaal hits:   {totaal_hits}", file=sys.stderr)
    print(f"  Totaal grootte: {totaal_grootte_kb:.1f} KB ({totaal_grootte_kb / 1024:.2f} MB)", file=sys.stderr)
    if geslaagd > 0:
        print(f"  Gem. build-tijd: {totaal_tijd / geslaagd:.1f}s per fiche", file=sys.stderr)
        print(f"  Gem. grootte:    {totaal_grootte_kb / geslaagd:.1f} KB per fiche", file=sys.stderr)
    if mislukt:
        print("\nMislukte fiches:", file=sys.stderr)
        for fiche_id, fout in mislukt:
            print(f"  {fiche_id}: {fout}", file=sys.stderr)

    sys.exit(0 if not mislukt else 1)


if __name__ == "__main__":
    main()
