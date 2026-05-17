#!/usr/bin/env python3
"""
Refresh RAG-index + bron-matches in één atomaire run (ADR-005 §refresh-gate).

Achtergrond
-----------
`mark_trusted.py` zet wel de trust-status maar raakt de RAG-index niet aan.
Resultaat: een bron op `trusted` zetten maakt hem nog niet zichtbaar voor
`match_bronnen.py` (anchor-bundles) tot iemand de reindex draait. Als je
daarna alvast nieuwe extracties laat lopen, werken die op stale bundles
en missen ze de net getrustete bron volledig.

Dit script lost dat op door beide stappen achter elkaar te draaien:

    1. `python3 tools/rag/rag_index.py`        — incremental upsert (SHA-check)
    2. `python3 -m tools.extractie.match_bronnen` — verse anchor-bundles

Gebruik
-------
Direct (na elke trust-promotie):

    python3 -m tools.etl.refresh_rag_and_matches

Via mark_trusted.py-wrapper (zie `--refresh`):

    python3 tools/etl/mark_trusted.py --bron X --status trusted --refresh

Aanvullende vlag-passthrough naar rag_index.py:
    --bron-rol {wettekst,norm,advies}    beperk de reindex tot één rol
    --include-unreviewed                 verstoor de trust-gate (alleen voor debug)

Aanvullende vlag-passthrough naar match_bronnen.py:
    --margin <float>                     bundling-margin (default in subscript)
    --threshold <float>                  absolute floor cosine-drempel

De wrapper retourneert exit-code 0 alleen als beide stappen lukken; bij
een crash in stap 1 wordt stap 2 niet meer aangevuurd (anders mismatch
tussen index en bundles).
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RAG_INDEX = ROOT / "tools" / "rag" / "rag_index.py"
MATCHES_LATEST = ROOT / "data" / "extractie" / "matches" / "latest.json"


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _run(cmd: list[str], *, label: str) -> None:
    print(f"\n=== [{_now()}] {label} ===")
    print(f"$ {' '.join(cmd)}\n")
    result = subprocess.run(cmd, cwd=ROOT)
    if result.returncode != 0:
        raise SystemExit(
            f"\n!! {label} faalde met exit-code {result.returncode}. "
            f"Refresh afgebroken; matches NIET ververst."
        )


def refresh(
    *,
    bron_rol: str | None = None,
    include_unreviewed: bool = False,
    match_margin: float | None = None,
    match_threshold: float | None = None,
) -> None:
    # Stap 1 — RAG-index incremental upsert
    rag_cmd: list[str] = [sys.executable, str(RAG_INDEX)]
    if bron_rol:
        rag_cmd += ["--bron-rol", bron_rol]
    if include_unreviewed:
        rag_cmd += ["--include-unreviewed"]
    _run(rag_cmd, label="Stap 1/2 — RAG-index incremental upsert")

    # Stap 2 — Bron-matching (anchor-bundles)
    match_cmd: list[str] = [sys.executable, "-m", "tools.extractie.match_bronnen"]
    if match_margin is not None:
        match_cmd += ["--margin", str(match_margin)]
    if match_threshold is not None:
        match_cmd += ["--threshold", str(match_threshold)]
    _run(match_cmd, label="Stap 2/2 — Bron-matching (anchor-bundles)")

    # Final-state samenvatting
    print(f"\n=== [{_now()}] Refresh klaar ===")
    if MATCHES_LATEST.exists() or MATCHES_LATEST.is_symlink():
        target = MATCHES_LATEST.resolve()
        print(f"matches/latest.json → {target.name}")
    else:
        print("WAARSCHUWING: matches/latest.json ontbreekt — match-script schreef niets.")


def main() -> None:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--bron-rol",
        choices=("wettekst", "norm", "advies"),
        help="beperk reindex tot één bron-rol (default: alle drie)",
    )
    p.add_argument(
        "--include-unreviewed",
        action="store_true",
        help="negeer trust-gate voor debug (default: alleen trusted-bronnen)",
    )
    p.add_argument(
        "--margin",
        type=float,
        default=None,
        help="match_bronnen.py --margin doorgeven",
    )
    p.add_argument(
        "--threshold",
        type=float,
        default=None,
        help="match_bronnen.py --threshold doorgeven",
    )
    args = p.parse_args()
    refresh(
        bron_rol=args.bron_rol,
        include_unreviewed=args.include_unreviewed,
        match_margin=args.margin,
        match_threshold=args.threshold,
    )


if __name__ == "__main__":
    main()
