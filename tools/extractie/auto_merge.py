"""
AUTO-MERGE + LOG — mechanisch script voor blok 4 (ADR-008 §13.4 + §13.7).

Vergelijkt concept-records op schijf met een git-referentie (default HEAD).
Herstelt verdwenen toplevel-velden (hard merge) en logt verdwenen array-items
(soft log). Geen LLM, geen mens-blokkade.

Garandeert het monotoon contract (ADR-008 §13.3): verbetering is welkom,
regressie niet. Een toplevel-veld kan niet verdwijnen zonder corrected_from-marker.

Twee niveaus (ADR-008 §13.4):
  Hard (auto-merge) — monotoon contract afdwingen op toplevel-velden:
    Een toplevel-veld is verdwenen t.o.v. git-ref EN heeft geen corrected_from-marker
    in het nieuwe record → het script zet het veld terug. Logt naar enrich-warnings.json
    met action "auto-merged".

  Soft (log) — signaleer mogelijke regressie in array-items:
    Een array-item binnen een behouden veld is verdwenen → logt naar enrich-warnings.json
    met action "logged-only". Geen automatische actie; latere VERIFY-ronde of mens
    kan terugkijken.

Gebruik:
  python3 -m tools.extractie.auto_merge
  python3 -m tools.extractie.auto_merge --since HEAD~1
  python3 -m tools.extractie.auto_merge --since abc1234 --droog
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concept_records"
WARNINGS_FILE = ROOT / "data" / "extractie" / "enrich-warnings.json"


# ─── Git helpers ───────────────────────────────────────────────────────────────


def gewijzigde_record_bestanden(git_ref: str) -> list[Path]:
    """Geef de concept-record-bestanden die gewijzigd zijn t.o.v. git_ref.

    Filtert op data/concept_records/*.json. Bestanden die alleen in git_ref
    bestaan (verwijderd) worden niet teruggegeven.
    """
    try:
        uitvoer = subprocess.check_output(
            ["git", "diff", "--name-only", git_ref, "--", "data/concept_records/"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as fout:
        print(f"[FOUT] git diff mislukt: {fout}", file=sys.stderr)
        sys.exit(1)

    bestanden: list[Path] = []
    for regel in uitvoer.splitlines():
        regel = regel.strip()
        if not regel.endswith(".json"):
            continue
        pad = ROOT / regel
        if pad.exists() and not pad.name.startswith("_"):
            bestanden.append(pad)
    return bestanden


def laad_record_uit_git(pad: Path, git_ref: str) -> dict | None:
    """Laad de inhoud van een bestand op een git-referentie.

    Retourneert None als het bestand op die referentie niet bestond.
    """
    try:
        relatief = pad.relative_to(ROOT)
        inhoud = subprocess.check_output(
            ["git", "show", f"{git_ref}:{relatief}"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
        return json.loads(inhoud)
    except subprocess.CalledProcessError:
        return None  # bestand bestond niet in git_ref
    except json.JSONDecodeError as fout:
        print(f"  [WAARSCHUWING] JSON-parse-fout voor {pad.name} @ {git_ref}: {fout}", file=sys.stderr)
        return None


# ─── Merge-logica ──────────────────────────────────────────────────────────────


def heeft_corrected_from_marker(nieuw_record: dict, veld_naam: str) -> bool:
    """Controleer of het veld in het nieuwe record een corrected_from-marker heeft.

    Kijkt op het veld zelf (als het een dict is met corrected_from-sleutel) én
    in enrich_runs-provenance (als string-vermelding van het veld).
    """
    veld = nieuw_record.get(veld_naam)
    if isinstance(veld, dict) and "corrected_from" in veld:
        return True
    # Ook controleren op verwijzingen in enrich_runs
    top_prov = nieuw_record.get("_provenance", {})
    for enrich_run in top_prov.get("enrich_runs", []):
        if veld_naam in enrich_run.get("gaps_verwerkt", []):
            return True
    return False


def diep_gelijk(a, b) -> bool:
    """Controleer diepe gelijkheid van twee waarden."""
    return json.dumps(a, sort_keys=True, ensure_ascii=False) == json.dumps(b, sort_keys=True, ensure_ascii=False)


def vind_verdwenen_array_items(oud_veld, nieuw_veld, veld_naam: str) -> list[dict]:
    """Vergelijk arrays van een veld; retourneer verdwenen items als warning-objecten."""
    if not isinstance(oud_veld, list) or not isinstance(nieuw_veld, list):
        return []
    verdwenen: list[dict] = []
    for item in oud_veld:
        aanwezig = any(diep_gelijk(item, nieuw_item) for nieuw_item in nieuw_veld)
        if not aanwezig:
            verdwenen.append({
                "veld_naam": veld_naam,
                "verloren_item": item,
            })
    return verdwenen


def verwerk_record(
    pad: Path,
    git_ref: str,
    run_id: str,
    droog: bool,
) -> tuple[int, int]:
    """Verwerk één record-bestand.

    Retourneert (aantal_gerevert, aantal_gelogd).
    """
    nieuw_record = json.loads(pad.read_text(encoding="utf-8"))
    oud_record = laad_record_uit_git(pad, git_ref)
    if oud_record is None:
        return 0, 0  # nieuw bestand, niet aanwezig in git_ref

    record_id = nieuw_record.get("id", pad.stem)
    nu = datetime.now(timezone.utc).isoformat(timespec="seconds")

    # Metadata-velden die we nooit vergelijken (git-versionering, run-ids, etc.)
    sla_over = {"_provenance", "_bestandspad"}

    oud_toplevel = set(oud_record.keys()) - sla_over
    nieuw_toplevel = set(nieuw_record.keys()) - sla_over
    verdwenen_velden = oud_toplevel - nieuw_toplevel

    warnings: list[dict] = []
    gerevert = 0
    gelogd = 0

    # Hard merge: verdwenen toplevel-velden terugzetten
    for veld_naam in sorted(verdwenen_velden):
        if heeft_corrected_from_marker(nieuw_record, veld_naam):
            # Expliciete correctie — niet terugzetten
            continue
        # Veld is verdwenen zonder motivering → terugzetten
        warnings.append({
            "record_id": record_id,
            "veld_pad": veld_naam,
            "verloren_item": oud_record[veld_naam],
            "verloren_in_run": run_id,
            "verloren_op": nu,
            "action": "auto-merged",
            "status": "unreviewed",
        })
        if not droog:
            nieuw_record[veld_naam] = oud_record[veld_naam]
        gerevert += 1

    # Soft log: verdwenen array-items binnen behouden velden
    for veld_naam in oud_toplevel & nieuw_toplevel:
        oud_veld = oud_record.get(veld_naam)
        nieuw_veld = nieuw_record.get(veld_naam)
        verdwenen_items = vind_verdwenen_array_items(oud_veld, nieuw_veld, veld_naam)
        for item_info in verdwenen_items:
            warnings.append({
                "record_id": record_id,
                "veld_pad": item_info["veld_naam"],
                "verloren_item": item_info["verloren_item"],
                "verloren_in_run": run_id,
                "verloren_op": nu,
                "action": "logged-only",
                "status": "unreviewed",
            })
            gelogd += 1

    if warnings:
        voeg_warnings_toe(warnings, WARNINGS_FILE, droog)

    # Schrijf het bijgewerkte record terug (alleen als er hard-merges waren)
    if gerevert > 0 and not droog:
        pad.write_text(
            json.dumps(nieuw_record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    return gerevert, gelogd


# ─── Warnings IO ───────────────────────────────────────────────────────────────


def voeg_warnings_toe(nieuwe_warnings: list[dict], warnings_bestand: Path, droog: bool) -> None:
    """Voeg warnings toe aan enrich-warnings.json (append-only)."""
    if droog:
        return
    bestaande: list[dict] = []
    if warnings_bestand.exists():
        try:
            bestaande = json.loads(warnings_bestand.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            bestaande = []
    bestaande.extend(nieuwe_warnings)
    warnings_bestand.parent.mkdir(parents=True, exist_ok=True)
    warnings_bestand.write_text(
        json.dumps(bestaande, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


# ─── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--since",
        default="HEAD",
        help="Git-referentie om mee te vergelijken (default: HEAD). "
             "Gebruik bv. 'HEAD~1', een commit-SHA of een branch-naam.",
    )
    parser.add_argument(
        "--droog",
        action="store_true",
        help="Droog uitvoeren: analyseer maar schrijf niets weg (geen merges, geen warnings).",
    )
    args = parser.parse_args()

    git_ref: str = args.since
    run_id = datetime.now(timezone.utc).strftime("auto-merge-%Y%m%dT%H%M%SZ")
    print(f"[auto-merge] {run_id} — vergelijking met git-ref: {git_ref}")
    if args.droog:
        print("  [droog] Droog-modus actief — geen bestanden worden gewijzigd.")

    # Gewijzigde records ophalen
    print(f"[git] gewijzigde records ophalen t.o.v. {git_ref} ...")
    gewijzigde_bestanden = gewijzigde_record_bestanden(git_ref)
    print(f"  {len(gewijzigde_bestanden)} gewijzigde record-bestanden gevonden")

    if not gewijzigde_bestanden:
        print("  Niets te doen.")
        return

    # Records verwerken
    totaal_gerevert = 0
    totaal_gelogd = 0
    for pad in sorted(gewijzigde_bestanden):
        record_id = pad.stem
        try:
            gerevert, gelogd = verwerk_record(pad, git_ref, run_id, args.droog)
        except Exception as fout:
            print(f"  [FOUT] {record_id}: {fout}", file=sys.stderr)
            continue

        if gerevert > 0 or gelogd > 0:
            modus = "[droog] " if args.droog else ""
            print(
                f"  {modus}{record_id}: "
                f"{gerevert} veld(en) teruggezet, {gelogd} array-item(s) gelogd"
            )
        totaal_gerevert += gerevert
        totaal_gelogd += gelogd

    print(f"\n[samenvatting]")
    print(f"  Records geanalyseerd  : {len(gewijzigde_bestanden)}")
    print(f"  Velden teruggezet     : {totaal_gerevert}")
    print(f"  Array-items gelogd    : {totaal_gelogd}")
    if not args.droog:
        if totaal_gerevert > 0 or totaal_gelogd > 0:
            print(f"  Warnings-bestand      : {WARNINGS_FILE.relative_to(ROOT)}")
    else:
        print(f"  [droog] Geen bestanden gewijzigd.")


if __name__ == "__main__":
    main()
