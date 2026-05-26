"""Bootstrap-migratie: vult metadata.scope.in[] voor records die het nog niet hebben.

Eenmalige migratie (ADR-033 follow-up). Idempotent: skipt records met bestaand scope-veld.

Algoritme (eenvoud > volledigheid):
- Eerste entry: <naam.primair> als <concept_type> [+ definitie-kernzin indien aanwezig]
- Per element: <element.naam>: <element.kern.tekst-1e-zin>
- scope.out blijft leeg (vereist cluster-context, handmatig in mapping-fase)
- changelog-entry "bootstrap-scope" markeert auto-generation

Records die geen scope.in baseline krijgen:
- Records met al een scope-veld (idempotent skip)
- Lege skeleton-records (geen definitie + geen elementen)

Gebruik:
    python3 -m tools.lib.migrate_scope_in_bootstrap            # alle records
    python3 -m tools.lib.migrate_scope_in_bootstrap --limit 5  # eerste 5 (test)
    python3 -m tools.lib.migrate_scope_in_bootstrap --dry-run  # toon output, save niet
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import sys
from pathlib import Path

from tools.lib import records_api

logger = logging.getLogger(__name__)


RECORDS_DIR = Path(__file__).resolve().parents[2] / "data" / "concepten" / "records"
MAX_ENTRY_LEN = 180  # truncate-grens per scope.in entry


def _eerste_zin(tekst: str) -> str:
    """Eerste zin uit een tekst-blok. Truncate op MAX_ENTRY_LEN."""
    if not tekst:
        return ""
    # Strip markdown-emphasis en whitespace
    t = tekst.strip()
    # Eerste zin (op '.' of '!' of '?')
    for stop in [". ", "! ", "? ", "\n"]:
        idx = t.find(stop)
        if idx > 0:
            t = t[:idx].strip()
            break
    # Truncate harde grens
    if len(t) > MAX_ENTRY_LEN:
        t = t[: MAX_ENTRY_LEN - 1].rstrip() + "…"
    # Strip trailing markdown-emphasis
    t = t.rstrip("*").rstrip("_").strip()
    return t


def _bouw_scope_in(record: dict) -> list[str]:
    """Construeer scope.in[] uit record-inhoud."""
    entries: list[str] = []

    naam = (record.get("naam") or {}).get("primair", "").strip()
    ctype = record.get("concept_type", "").strip()
    inhoud = record.get("inhoud") or {}
    kern = inhoud.get("kern") or {}

    # Eerste entry: naam + type + eventueel definitie-zin
    definitie_tekst = ""
    defi = kern.get("definitie")
    if isinstance(defi, dict):
        definitie_tekst = _eerste_zin(defi.get("tekst", ""))

    if not definitie_tekst:
        subs = kern.get("substantie")
        if isinstance(subs, dict):
            definitie_tekst = _eerste_zin(subs.get("tekst", ""))

    if naam and ctype:
        if definitie_tekst:
            entries.append(f"{naam} ({ctype}): {definitie_tekst}")
        else:
            entries.append(f"{naam} als {ctype}")
    elif definitie_tekst:
        entries.append(definitie_tekst)

    # Per element
    for el in inhoud.get("elementen", []) or []:
        if not isinstance(el, dict):
            continue
        # element.naam = dict met "primair"-key (zelfde shape als top-level naam)
        naam_blok = el.get("naam") or {}
        if isinstance(naam_blok, dict):
            el_naam = (naam_blok.get("primair") or "").strip()
        else:
            el_naam = str(naam_blok).strip()
        # element.kern = dict met definitie/rationale-sub-blokken (zelfde shape als top-level kern)
        el_kern = el.get("kern") or {}
        el_zin = ""
        if isinstance(el_kern, dict):
            defi = el_kern.get("definitie")
            if isinstance(defi, dict):
                el_zin = _eerste_zin(defi.get("tekst", ""))
            if not el_zin:
                subs = el_kern.get("substantie")
                if isinstance(subs, dict):
                    el_zin = _eerste_zin(subs.get("tekst", ""))
        if el_naam and el_zin:
            entries.append(f"{el_naam}: {el_zin}")
        elif el_naam:
            entries.append(el_naam)
        elif el_zin:
            entries.append(el_zin)

    return entries


def _bootstrap_record(record: dict) -> tuple[bool, str]:
    """Bewerk record in-place. Retourneer (wijzigingen, reden)."""
    metadata = record.get("metadata") or {}
    if "scope" in metadata:
        return False, "scope al aanwezig"

    scope_in = _bouw_scope_in(record)
    if not scope_in:
        return False, "geen baseline content (lege definitie + lege elementen)"

    metadata["scope"] = {"in": scope_in, "out": []}
    record["metadata"] = metadata

    # Changelog-entry
    changelog = metadata.setdefault("changelog", [])
    changelog.append(
        {
            "operatie": "bootstrap-scope",
            "timestamp": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "model": "migration-script",
            "wijziging": f"scope.in bootstrap uit inhoud ({len(scope_in)} entries) — handmatig te verfijnen + scope.out leeg",
        }
    )

    return True, f"{len(scope_in)} scope.in entries toegevoegd"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=None, help="Max aantal records (debug)")
    parser.add_argument("--dry-run", action="store_true", help="Toon output, schrijf niet")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")

    record_files = sorted(RECORDS_DIR.glob("*.json"))
    if args.limit:
        record_files = record_files[: args.limit]

    print(f"Records te bekijken: {len(record_files)}")
    print(f"Mode: {'DRY-RUN (geen save)' if args.dry_run else 'LIVE (save_record)'}")
    print()

    teller = {"updated": 0, "skipped": 0, "failed": 0}

    for path in record_files:
        try:
            with path.open() as f:
                record = json.load(f)
        except Exception as exc:
            logger.warning("Laad-fout %s: %s", path.name, exc)
            teller["failed"] += 1
            continue

        wijziging, reden = _bootstrap_record(record)
        if not wijziging:
            teller["skipped"] += 1
            logger.debug("SKIP %s: %s", path.name, reden)
            continue

        if args.dry_run:
            scope = record["metadata"]["scope"]
            print(f"--- {path.stem} ({reden}) ---")
            for entry in scope["in"]:
                print(f"  in: {entry}")
            print()
        else:
            try:
                records_api.save_record(record)
                teller["updated"] += 1
                if teller["updated"] % 20 == 0:
                    print(f"  ✓ {teller['updated']} records bijgewerkt...")
            except Exception as exc:
                logger.error("save_record-fout %s: %s", path.name, exc)
                teller["failed"] += 1

    print()
    print(f"Totaal: updated={teller['updated']} skipped={teller['skipped']} failed={teller['failed']}")
    return 0 if teller["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
