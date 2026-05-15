"""
Enrichment-cycle orchestrator (ADR-008 §13.6 + §13.7).

Orchestreert de volledige VERIFY → ENRICH → AUTO-MERGE loop voor een
programmaonderdeel autonoom tot er geen open gaps meer zijn (of totdat het
maximum aantal iteraties bereikt is).

Per iteratie:
  1. Bepaal welke gaps open zijn (status "open" of "discovered-during-enrich").
  2. Stop als er geen open gaps zijn.
  3. Stop als alle resterende open gaps de status "unable-from-bronnen" hebben —
     die zijn niet oplosbaar zonder corpus-uitbreiding.
  4. Schrijf instructies voor de VERIFY-subagent (via verify_records.py).
  5. Schrijf instructies voor de ENRICH-subagent (via enrich_records.py).
  6. Print welke twee manuele agent-launches nodig zijn.
  7. Wacht op bevestiging van de mens dat de subagent-runs voltooid zijn.
     (In onbeheerde modus: --onbeheerd vereist handmatig --markeer-na-run daarna.)

Na elke iteratie:
  - auto_merge.py wordt automatisch uitgevoerd (deterministisch, geen LLM).
  - Een iteratie-samenvatting wordt toegevoegd aan het cycle-rapport.

Output: data/extractie/<po>/cycle-runs/cycle-<id>.md

Gebruik:
  python3 -m tools.extractie.run_enrichment_cycle --programmaonderdeel 1.4
  python3 -m tools.extractie.run_enrichment_cycle --programmaonderdeel 1.4 \\
      --max-iteraties 3
  python3 -m tools.extractie.run_enrichment_cycle --programmaonderdeel 1.4 \\
      --droog

Beperkingen (ADR-008 §2):
  - Geen anthropic-API-calls vanuit dit script.
  - LLM-werk gebeurt uitsluitend via manueel gelanceerde subagent-sessies.
  - Dit script schrijft instructie-bestanden en coördineert de cycle-state.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
GAPS_FILE = ROOT / "data" / "extractie" / "gaps.json"

# Statussen die als "open" gelden voor de cyclus
OPEN_STATUSSEN = {"open", "discovered-during-enrich"}
# Status die aangeeft dat een gap echt niet oplosbaar is zonder extra bronnen
BLOKKERENDE_STATUS = "unable-from-bronnen"


# ─── Gaps helpers ──────────────────────────────────────────────────────────────


def laad_gaps(gaps_bestand: Path) -> list[dict]:
    """Laad alle gap-entries uit gaps.json."""
    if not gaps_bestand.exists():
        return []
    try:
        return json.loads(gaps_bestand.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def open_gaps(alle_gaps: list[dict]) -> list[dict]:
    """Geef gaps terug met status in OPEN_STATUSSEN."""
    return [g for g in alle_gaps if g.get("status") in OPEN_STATUSSEN]


def alleen_unable(gaps: list[dict]) -> bool:
    """Geef True als alle open gaps de status 'unable-from-bronnen' hebben."""
    if not gaps:
        return False
    return all(g.get("status") == BLOKKERENDE_STATUS for g in gaps)


# ─── Subagent-instructies via bestaande runners ────────────────────────────────


def genereer_verify_instructies(
    programmaonderdeel_id: str,
    droog: bool,
) -> tuple[int, str | None]:
    """Roep verify_records.py aan om subagent-instructies te genereren.

    Retourneert (returncode, pad_naar_instructies_bestand_of_None).
    """
    cmd = [
        sys.executable, "-m", "tools.extractie.verify_records",
        "--programmaonderdeel", programmaonderdeel_id,
    ]
    if droog:
        cmd.append("--droog")
    resultaat = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if resultaat.returncode != 0:
        print(resultaat.stderr, file=sys.stderr)
        return resultaat.returncode, None

    # Extraheer het pad uit de stdout-output
    for regel in resultaat.stdout.splitlines():
        if "verify-instructies-" in regel and ".md" in regel:
            for deel in regel.split():
                if "verify-instructies-" in deel and ".md" in deel:
                    return 0, deel.strip()
    return 0, None


def genereer_enrich_instructies(
    programmaonderdeel_id: str,
    droog: bool,
) -> tuple[int, str | None]:
    """Roep enrich_records.py aan om subagent-instructies te genereren.

    Retourneert (returncode, pad_naar_instructies_bestand_of_None).
    """
    cmd = [
        sys.executable, "-m", "tools.extractie.enrich_records",
        "--programmaonderdeel", programmaonderdeel_id,
    ]
    if droog:
        cmd.append("--droog")
    resultaat = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if resultaat.returncode != 0:
        print(resultaat.stderr, file=sys.stderr)
        return resultaat.returncode, None

    # Extraheer het pad uit de stdout-output
    for regel in resultaat.stdout.splitlines():
        if "enrich-instructies-" in regel and ".md" in regel:
            for deel in regel.split():
                if "enrich-instructies-" in deel and ".md" in deel:
                    return 0, deel.strip()
    return 0, None


def voer_auto_merge_uit(droog: bool) -> int:
    """Roep auto_merge.py aan na een enrich-ronde."""
    cmd = [sys.executable, "-m", "tools.extractie.auto_merge"]
    if droog:
        cmd.append("--droog")
    resultaat = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(resultaat.stdout)
    if resultaat.returncode != 0:
        print(resultaat.stderr, file=sys.stderr)
    return resultaat.returncode


# ─── Cycle-rapport ─────────────────────────────────────────────────────────────


def schrijf_cycle_rapport(
    programmaonderdeel_id: str,
    cycle_id: str,
    iteraties: list[dict],
    reden_stoppen: str,
    werkmap: Path,
) -> Path:
    """Schrijf het gecombineerde cycle-rapport naar werkmap/cycle-<id>.md."""
    werkmap.mkdir(parents=True, exist_ok=True)
    rapport_pad = werkmap / f"cycle-{cycle_id}.md"

    regels = [
        f"# Enrichment-cycle {cycle_id} — PO {programmaonderdeel_id}",
        f"",
        f"**Gegenereerd op**: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"**Reden stoppen**: {reden_stoppen}",
        f"",
    ]

    for iteratie in iteraties:
        n = iteratie["iteratie_nr"]
        regels += [
            f"## Iteratie {n}",
            f"",
            f"- **Open gaps bij aanvang**: {iteratie['open_gaps_aanvang']}",
            f"- **VERIFY-instructies**: `{iteratie.get('verify_instructies', 'n.v.t.')}`",
            f"- **ENRICH-instructies**: `{iteratie.get('enrich_instructies', 'n.v.t.')}`",
            f"- **Open gaps na auto-merge**: {iteratie.get('open_gaps_na', '?')}",
            f"- **Nieuwe discovered-during-enrich gaps**: {iteratie.get('nieuwe_discovery_gaps', 0)}",
            f"",
        ]

    regels += [
        f"## Manuele stappen per iteratie",
        f"",
        f"Per iteratie zijn twee manuele agent-launches nodig:",
        f"",
        f"**Stap 1 — VERIFY (Sonnet-subagent)**:",
        f"Open het `verify-instructies-<run-id>.md` bestand in een Sonnet-sessie.",
        f"De subagent voert de drie VERIFY-checks uit en schrijft naar `data/extractie/gaps.json`.",
        f"",
        f"**Stap 2 — ENRICH (Opus-subagent)**:",
        f"Na VERIFY: open het `enrich-instructies-<run-id>.md` bestand in een Opus-sessie.",
        f"Na afloop: `python3 -m tools.extractie.enrich_records --programmaonderdeel {programmaonderdeel_id} --markeer-gaps-na-run <enrich-instructies-pad>`",
        f"",
        f"`run_enrichment_cycle.py` voert `auto_merge.py` automatisch uit na stap 2.",
    ]

    rapport_pad.write_text("\n".join(regels) + "\n", encoding="utf-8")
    return rapport_pad


# ─── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--programmaonderdeel",
        required=True,
        help="Programmaonderdeel-code, bv. '1.4' of '4.0'.",
    )
    parser.add_argument(
        "--max-iteraties",
        type=int,
        default=3,
        help="Maximum aantal VERIFY→ENRICH-iteraties (default: 3). "
             "De cyclus stopt eerder als er geen open gaps meer zijn.",
    )
    parser.add_argument(
        "--droog",
        action="store_true",
        help="Droog uitvoeren: genereer instructies maar schrijf niets weg en voer auto_merge niet uit.",
    )
    args = parser.parse_args()

    programmaonderdeel_id: str = args.programmaonderdeel
    max_iteraties: int = args.max_iteraties

    cycle_id = datetime.now(timezone.utc).strftime("cycle-%Y%m%dT%H%M%SZ")
    werkmap = ROOT / "data" / "extractie" / programmaonderdeel_id / "cycle-runs"

    print(f"[cycle] {cycle_id} — programmaonderdeel {programmaonderdeel_id}")
    print(f"[cycle] max-iteraties: {max_iteraties}")
    print()

    iteraties: list[dict] = []
    reden_stoppen = f"maximum iteraties ({max_iteraties}) bereikt"

    for iteratie_nr in range(1, max_iteraties + 1):
        print(f"{'='*60}")
        print(f"[cycle] Iteratie {iteratie_nr} van {max_iteraties}")
        print(f"{'='*60}")

        # Bepaal open gaps
        alle_gaps = laad_gaps(GAPS_FILE)
        huidige_open_gaps = open_gaps(alle_gaps)
        print(f"[gaps] {len(huidige_open_gaps)} open gaps (statussen: open + discovered-during-enrich)")

        # Stop-condities
        if not huidige_open_gaps:
            reden_stoppen = "geen open gaps meer"
            print(f"[cycle] Gestopt: {reden_stoppen}")
            break

        if alleen_unable(huidige_open_gaps):
            reden_stoppen = (
                f"alle {len(huidige_open_gaps)} open gaps hebben status "
                f"'unable-from-bronnen' — niet oplosbaar zonder corpus-uitbreiding"
            )
            print(f"[cycle] Gestopt: {reden_stoppen}")
            break

        iteratie_data: dict = {
            "iteratie_nr": iteratie_nr,
            "open_gaps_aanvang": len(huidige_open_gaps),
        }

        # Stap 1: VERIFY-instructies genereren
        print(f"\n[cycle] Stap 1: VERIFY-instructies genereren ...")
        rc, verify_pad = genereer_verify_instructies(programmaonderdeel_id, args.droog)
        if rc != 0:
            print(f"[FOUT] verify_records.py mislukt (exitcode {rc})", file=sys.stderr)
            reden_stoppen = f"fout in verify_records.py (iteratie {iteratie_nr})"
            break
        iteratie_data["verify_instructies"] = verify_pad or "droog-modus"

        # Stap 2: ENRICH-instructies genereren
        print(f"[cycle] Stap 2: ENRICH-instructies genereren ...")
        rc, enrich_pad = genereer_enrich_instructies(programmaonderdeel_id, args.droog)
        if rc != 0:
            print(f"[FOUT] enrich_records.py mislukt (exitcode {rc})", file=sys.stderr)
            reden_stoppen = f"fout in enrich_records.py (iteratie {iteratie_nr})"
            break
        iteratie_data["enrich_instructies"] = enrich_pad or "droog-modus"

        # Print manuele instructies voor de mens
        print(f"\n{'─'*60}")
        print(f"MANUELE STAPPEN VEREIST — iteratie {iteratie_nr}")
        print(f"{'─'*60}")
        print(f"")
        print(f"Stap 1: VERIFY (Sonnet-subagent)")
        if verify_pad:
            print(f"  Open: {verify_pad}")
        print(f"  Model: claude-sonnet-4-6 (ADR-008 §13.2)")
        print(f"  Output: schrijft naar data/extractie/gaps.json")
        print(f"")
        print(f"Stap 2: ENRICH (Opus-subagent)")
        if enrich_pad:
            print(f"  Open: {enrich_pad}")
        print(f"  Na afloop markeer-stap:")
        if enrich_pad:
            print(f"    python3 -m tools.extractie.enrich_records \\")
            print(f"      --programmaonderdeel {programmaonderdeel_id} \\")
            print(f"      --markeer-gaps-na-run {enrich_pad}")
        print(f"")
        print(f"Daarna: bevestig dat beide runs klaar zijn en herstart run_enrichment_cycle.py")
        print(f"  (of gebruik --droog om de instructies te bekijken zonder te wachten)")
        print(f"{'─'*60}")

        # AUTO-MERGE automatisch uitvoeren (deterministisch, geen LLM)
        if not args.droog:
            print(f"\n[cycle] auto_merge.py uitvoeren ...")
            rc_merge = voer_auto_merge_uit(args.droog)
            if rc_merge != 0:
                print(f"[WAARSCHUWING] auto_merge.py gaf exitcode {rc_merge}", file=sys.stderr)
        else:
            print(f"[droog] auto_merge.py NIET uitgevoerd")

        # Tel nieuwe discovered-during-enrich gaps
        alle_gaps_na = laad_gaps(GAPS_FILE)
        open_gaps_na = open_gaps(alle_gaps_na)
        nieuwe_discovery = sum(
            1 for g in alle_gaps_na
            if g.get("status") == "discovered-during-enrich"
            and not any(
                og.get("record_id") == g.get("record_id")
                and og.get("aspect") == g.get("aspect")
                for og in alle_gaps
            )
        )
        iteratie_data["open_gaps_na"] = len(open_gaps_na)
        iteratie_data["nieuwe_discovery_gaps"] = nieuwe_discovery
        iteraties.append(iteratie_data)

        print(f"\n[cycle] Iteratie {iteratie_nr} afgerond:")
        print(f"  Open gaps na iteratie : {len(open_gaps_na)}")
        print(f"  Nieuwe discovery-gaps : {nieuwe_discovery}")

        # In droge modus: slechts één iteratie tonen
        if args.droog:
            print(f"\n[droog] Cyclus gestopt na 1 iteratie (droog-modus).")
            reden_stoppen = "droog-modus — slechts één iteratie getoond"
            break
    else:
        iteraties.append({
            "iteratie_nr": max_iteraties,
            "open_gaps_aanvang": len(open_gaps(laad_gaps(GAPS_FILE))),
        })

    # Cycle-rapport schrijven
    if not args.droog:
        rapport_pad = schrijf_cycle_rapport(
            programmaonderdeel_id=programmaonderdeel_id,
            cycle_id=cycle_id,
            iteraties=iteraties,
            reden_stoppen=reden_stoppen,
            werkmap=werkmap,
        )
        print(f"\n[cycle] Rapport geschreven naar {rapport_pad.relative_to(ROOT)}")

    print(f"\n[cycle] Klaar. Reden stoppen: {reden_stoppen}")


if __name__ == "__main__":
    main()
