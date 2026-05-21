"""
Live progress-monitor voor skeleton-passes (ADR-025).

Toont DB-state van candidates: totaal, per-kind, per-PO, recente mutaties.
Optionele watch-mode refresht elke N seconden — handig om in een aparte
terminal te draaien tijdens parallelle skeleton-runs.

Gebruik:
  # One-shot snapshot
  python3 -m tools.extractie.monitor_skeleton_progress

  # Watch-mode (refresh elke 5s)
  python3 -m tools.extractie.monitor_skeleton_progress --watch

  # Watch met specifieke interval
  python3 -m tools.extractie.monitor_skeleton_progress --watch --interval 10

  # JSON-output voor scripting
  python3 -m tools.extractie.monitor_skeleton_progress --json

  # Toon alleen recente activiteit van laatste N minuten
  python3 -m tools.extractie.monitor_skeleton_progress --recent 2
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.extractie import candidates_db  # noqa: E402


def _clear_screen() -> None:
    """Cross-platform terminal-clear."""
    print("\033[2J\033[H", end="")


def _print_snapshot(recent_min: int = 5) -> None:
    """Eén momentopname van DB-state."""
    stats = candidates_db.statistieken()
    per_po = candidates_db.progress_per_po()
    recent = candidates_db.recente_activiteit(sinds_minuten=recent_min, limit=20)

    nu = datetime.now().strftime("%H:%M:%S")
    print(f"\n=== Skeleton-progress @ {nu} ===\n")

    # Totalen
    print(f"  Totaal kandidaten: {stats['totaal']}")
    print(f"  Met embedding:     {stats['met_embedding']}")
    print(f"  Cross-PO:          {stats['cross_po']}")
    print(f"  Gerealiseerd:      {stats['gerealiseerd']}")
    print(f"  Openstaand:        {stats['openstaand']}")

    # Per kind
    if stats["per_kind"]:
        print("\n  Per kind:")
        for kind, n in sorted(stats["per_kind"].items(), key=lambda kv: -kv[1]):
            print(f"    {kind:18s} {n:4d}")

    # Per PO (compact)
    if per_po:
        print("\n  Per PO (primary · voorstellen · gerealiseerd):")
        for po in sorted(per_po.keys()):
            s = per_po[po]
            print(f"    {po:6s}  primary={s['primary']:3d}  voorstellen={s['voorstellen']:3d}  gerealiseerd={s['gerealiseerd']:3d}")

    # Recente activiteit
    if recent:
        print(f"\n  Recente activiteit (laatste {recent_min} min · {len(recent)} entries):")
        for r in recent[:15]:
            marker = "✨" if r["nieuw"] else "🔄"
            tijd = r["laatste_wijziging"][11:19]  # HH:MM:SS
            pos_str = ",".join(r["voorgesteld_door_pos"])
            print(f"    {tijd} {marker} [{r['kind']:12s}] {r['fiche_id']:40s} ({pos_str})")
    else:
        print(f"\n  (geen activiteit in laatste {recent_min} min)")


def _print_json() -> None:
    """JSON-output voor scripting/piping."""
    stats = candidates_db.statistieken()
    per_po = candidates_db.progress_per_po()
    recent = candidates_db.recente_activiteit(sinds_minuten=5, limit=50)
    print(json.dumps({
        "tijdstip": datetime.now().isoformat(),
        "stats": stats,
        "per_po": per_po,
        "recente_activiteit": recent,
    }, indent=2, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--watch", action="store_true", help="Refresh modus (gebruik Ctrl-C om te stoppen)")
    parser.add_argument("--interval", type=int, default=5, help="Refresh-interval seconden (default 5)")
    parser.add_argument("--recent", type=int, default=5, help="Recente-activiteit-window in minuten (default 5)")
    parser.add_argument("--json", action="store_true", help="JSON-output, geen formatting")
    args = parser.parse_args()

    if args.json:
        _print_json()
        return 0

    if not args.watch:
        _print_snapshot(recent_min=args.recent)
        return 0

    # Watch-mode
    try:
        while True:
            _clear_screen()
            _print_snapshot(recent_min=args.recent)
            print(f"\n  (refresh elke {args.interval}s · Ctrl-C om te stoppen)")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\n\nStop.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
