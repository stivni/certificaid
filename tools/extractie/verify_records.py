"""
Subagent-runner voor blok 2 VERIFY (ADR-008 §13.2 + §13.7).

Laadt concept-records voor een programmaonderdeel (via linked_anchors[]),
voert mechanische coherentie-checks uit, en schrijft instructies voor een
Sonnet-subagent die de drie VERIFY-checks uitvoert (examenvraag-simulatie,
minicursus-haalbaarheid, semantische coherentie).

Judge-werk vereist geen Opus-synthese (ADR-008 §13.2). VERIFY draait op
VERIFY_MODEL = "claude-sonnet-4-6" — bespaart budget en tijd.

Gebruik:
  python3 -m tools.extractie.verify_records --programmaonderdeel 1.4
  python3 -m tools.extractie.verify_records --programmaonderdeel 1.4 \\
      --records-glob "data/concept_records/*.json"
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Model voor de VERIFY-subagent (ADR-008 §13.2).
# Judge-werk vereist geen Opus-synthese — Sonnet volstaat en bespaart budget.
VERIFY_MODEL = "claude-sonnet-4-6"

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concept_records"
GAPS_FILE = ROOT / "data" / "extractie" / "gaps.json"
EXAMEN_VRAGEN_DIR = ROOT / "data" / "examen_vragen"
ANCHORS_FILE = ROOT / "data" / "anchors.json"
PROMPTS_DIR = ROOT / "prompts"
VERIFY_PROMPT = PROMPTS_DIR / "concept-verify-v1.md"


# ─── Helpers ───────────────────────────────────────────────────────────────────


def laad_alle_records(records_glob: str) -> list[dict]:
    """Laad alle JSON-records die matchen met het glob-patroon."""
    bestanden = list(ROOT.glob(records_glob))
    records = []
    for bestand in bestanden:
        if bestand.name.startswith("_"):
            continue  # archief / meta bestanden overslaan
        try:
            record = json.loads(bestand.read_text(encoding="utf-8"))
            record["_bestandspad"] = str(bestand.relative_to(ROOT))
            records.append(record)
        except (json.JSONDecodeError, OSError) as fout:
            print(f"  [WAARSCHUWING] {bestand.name}: overgeslagen ({fout})", file=sys.stderr)
    return records


def load_records_for_programmaonderdeel(programmaonderdeel_id: str, records_glob: str) -> list[dict]:
    """Laad records waarvan linked_anchors[] minstens één anchor van het programmaonderdeel bevatten.

    Een anchor-id begint met '<programmaonderdeel_id>.' bv. '1.4.I.G'.
    Records zonder linked_anchors-veld worden overgeslagen.
    """
    alle_records = laad_alle_records(records_glob)
    gefilterd = []
    prefix = f"{programmaonderdeel_id}."
    for record in alle_records:
        gekoppelde_anchors = record.get("linked_anchors", [])
        if any(anker.startswith(prefix) for anker in gekoppelde_anchors):
            gefilterd.append(record)
    return gefilterd


def laad_anchors_voor_programmaonderdeel(programmaonderdeel_id: str) -> list[dict]:
    """Laad anchors voor een programmaonderdeel uit data/anchors.json."""
    if not ANCHORS_FILE.exists():
        return []
    data = json.loads(ANCHORS_FILE.read_text(encoding="utf-8"))
    prefix = f"{programmaonderdeel_id}."
    return [
        anker for anker in data.get("anchors", [])
        if anker.get("anchor_id", "").startswith(prefix)
    ]


PROGRAMMAONDERDEEL_CLASSIFICATIE_BESTAND = (
    EXAMEN_VRAGEN_DIR / "_programmaonderdeel_classificatie.json"
)


def laad_examen_vragen_voor_programmaonderdeel(programmaonderdeel_id: str) -> list[dict]:
    """Laad examenvragen voor een programmaonderdeel.

    Strategie (in volgorde van prioriteit):

    1. **Semantische classificatie** (primair): leest
       `data/examen_vragen/_programmaonderdeel_classificatie.json` en filtert
       vragen waar `programmaonderdeel_id` in `programmaonderdelen[]` zit.
       Dit is de correcte aanpak want `vak_code_in_pdf` gebruikt de oude nummering.

    2. **Fallback** op vak_code_in_pdf via -labels.json bestanden:
       wordt gebruikt als de classificatie-json ontbreekt of geen vragen levert.
       Geeft een waarschuwing zodat de beheerder de classificatie kan aanvullen.

    Geeft een platte lijst van vraag-objecten terug.
    """
    # Strategie 1: semantische classificatie via _programmaonderdeel_classificatie.json
    if PROGRAMMAONDERDEEL_CLASSIFICATIE_BESTAND.exists():
        try:
            classificatie = json.loads(
                PROGRAMMAONDERDEEL_CLASSIFICATIE_BESTAND.read_text(encoding="utf-8")
            )
            geclassificeerde_ids = {
                vraag_id
                for vraag_id, entry in classificatie.items()
                if programmaonderdeel_id in entry.get("programmaonderdelen", [])
            }

            if geclassificeerde_ids:
                vragen: list[dict] = []
                for bestand in sorted(EXAMEN_VRAGEN_DIR.glob("*.json")):
                    if bestand.name.startswith("_") or bestand.name.endswith("-labels.json"):
                        continue
                    try:
                        data = json.loads(bestand.read_text(encoding="utf-8"))
                        for vraag in data.get("vragen", []):
                            if vraag.get("id", "") in geclassificeerde_ids:
                                classificatie_entry = classificatie.get(vraag["id"], {})
                                vragen.append({
                                    **vraag,
                                    "_classificatie": classificatie_entry,
                                })
                    except (json.JSONDecodeError, OSError):
                        pass
                return vragen

            # Classificatie bestaat maar heeft geen vragen voor dit PO
            print(
                f"  [WAARSCHUWING] {PROGRAMMAONDERDEEL_CLASSIFICATIE_BESTAND.name} "
                f"bevat geen vragen voor programmaonderdeel {programmaonderdeel_id}. "
                f"Voer tools/examen/classify_vragen_naar_programmaonderdelen.py uit "
                f"om de classificatie aan te vullen. Fallback op vak_code_in_pdf.",
                file=sys.stderr,
            )
        except json.JSONDecodeError:
            print(
                f"  [WAARSCHUWING] {PROGRAMMAONDERDEEL_CLASSIFICATIE_BESTAND.name} "
                f"is geen geldige JSON. Fallback op vak_code_in_pdf.",
                file=sys.stderr,
            )
    else:
        print(
            f"  [INFO] {PROGRAMMAONDERDEEL_CLASSIFICATIE_BESTAND.name} niet gevonden. "
            f"Fallback op vak_code_in_pdf (oude nummering — mogelijk incomplete matching). "
            f"Overweeg tools/examen/classify_vragen_naar_programmaonderdelen.py te draaien.",
            file=sys.stderr,
        )

    # Strategie 2: fallback op vak_code_in_pdf via -labels.json
    vragen = []
    for labels_bestand in sorted(EXAMEN_VRAGEN_DIR.glob("*-labels.json")):
        labels_data = json.loads(labels_bestand.read_text(encoding="utf-8"))
        examen_id = labels_data.get("examen_id", "")
        vragen_bestand = EXAMEN_VRAGEN_DIR / f"{examen_id}.json"
        if not vragen_bestand.exists():
            continue
        vragen_data = json.loads(vragen_bestand.read_text(encoding="utf-8"))
        vraag_by_id = {v["id"]: v for v in vragen_data.get("vragen", [])}
        for label in labels_data.get("labels", []):
            vraag_id = label.get("vraag_id", "")
            vraag = vraag_by_id.get(vraag_id, {})
            vak_code = vraag.get("vak_code_in_pdf", "")
            if vak_code.startswith(programmaonderdeel_id) or not vak_code:
                vragen.append({**vraag, "labels": label})
    return vragen


def _record_ids(records: list[dict]) -> set[str]:
    return {r.get("id", "") for r in records if r.get("id")}


def mechanical_coherence_checks(records: list[dict]) -> list[dict]:
    """Voer mechanische coherentie-checks uit zonder LLM.

    Controleert:
    - vergelijkingsparen[].vergelijking_met → bestaat als record-id
    - edges[].target → bestaat als record-id

    Geeft een lijst van mechanische gap-objecten terug (nog niet weggeschreven).
    """
    bestaande_ids = _record_ids(records)
    gaps: list[dict] = []
    nu = datetime.now(timezone.utc).isoformat(timespec="seconds")

    for record in records:
        record_id = record.get("id", "?")

        # Vergelijkingsparen-targets
        for paar in record.get("vergelijkingsparen", []):
            doel = paar.get("vergelijking_met", "")
            if doel and doel not in bestaande_ids:
                gaps.append({
                    "record_id": record_id,
                    "aspect": "vergelijkingsparen.target-ontbreekt",
                    "reden": (
                        f"vergelijkingsparen[].vergelijking_met wijst naar '{doel}' "
                        f"maar er bestaat geen record met dat id in de geladen set."
                    ),
                    "prio": "laag",
                    "geconstateerd_door": "mechanisch",
                    "geconstateerd_op": nu,
                    "status": "open",
                })

        # Edges-targets
        for edge in record.get("edges", []):
            doel = edge.get("target", "")
            if doel and doel not in bestaande_ids:
                gaps.append({
                    "record_id": record_id,
                    "aspect": "edges.target-ontbreekt",
                    "reden": (
                        f"edges[].target wijst naar '{doel}' "
                        f"maar er bestaat geen record met dat id in de geladen set."
                    ),
                    "prio": "laag",
                    "geconstateerd_door": "mechanisch",
                    "geconstateerd_op": nu,
                    "status": "open",
                })

    return gaps


def voeg_gaps_toe(nieuwe_gaps: list[dict], gaps_bestand: Path) -> int:
    """Voeg nieuwe gaps toe aan gaps.json (append-only). Dedupliceer op record_id + aspect + status:open.

    Geeft het aantal nieuw toegevoegde gaps terug.
    """
    bestaande: list[dict] = []
    if gaps_bestand.exists():
        try:
            bestaande = json.loads(gaps_bestand.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            bestaande = []

    bestaande_sleutels = {
        (g["record_id"], g["aspect"])
        for g in bestaande
        if g.get("status") == "open"
    }

    toegevoegd = 0
    for gap in nieuwe_gaps:
        sleutel = (gap["record_id"], gap["aspect"])
        if sleutel not in bestaande_sleutels:
            bestaande.append(gap)
            bestaande_sleutels.add(sleutel)
            toegevoegd += 1

    gaps_bestand.parent.mkdir(parents=True, exist_ok=True)
    gaps_bestand.write_text(
        json.dumps(bestaande, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return toegevoegd


def schrijf_subagent_instructies(
    programmaonderdeel_id: str,
    records: list[dict],
    anchors: list[dict],
    examen_vragen: list[dict],
    run_id: str,
    werkmap: Path,
) -> Path:
    """Schrijf een Markdown-bestand met instructies voor de Opus VERIFY-subagent.

    De subagent laadt dit bestand en voert de drie VERIFY-checks uit conform
    `prompts/concept-verify-v1.md`.
    """
    werkmap.mkdir(parents=True, exist_ok=True)
    instructies_pad = werkmap / f"verify-instructies-{run_id}.md"

    # Serialiseer de input-data naar de werkmap zodat de subagent ze kan inladen
    records_pad = werkmap / f"records-{run_id}.json"
    anchors_pad = werkmap / f"anchors-{run_id}.json"
    vragen_pad = werkmap / f"examen_vragen-{run_id}.json"

    records_pad.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    anchors_pad.write_text(json.dumps(anchors, ensure_ascii=False, indent=2), encoding="utf-8")
    vragen_pad.write_text(json.dumps(examen_vragen, ensure_ascii=False, indent=2), encoding="utf-8")

    prompt_tekst = VERIFY_PROMPT.read_text(encoding="utf-8") if VERIFY_PROMPT.exists() else (
        f"[WAARSCHUWING: {VERIFY_PROMPT} niet gevonden — laad prompts/concept-verify-v1.md handmatig]"
    )

    instructies = f"""# VERIFY-run {run_id} — Instructies voor Sonnet-subagent

**Programmaonderdeel**: {programmaonderdeel_id}
**Run-id**: {run_id}
**Gegenereerd op**: {datetime.now(timezone.utc).isoformat(timespec="seconds")}
**Model**: {VERIFY_MODEL} (judge-werk vereist geen Opus-synthese — ADR-008 §13.2)

## Jouw taak

Voer de drie VERIFY-checks uit zoals beschreven in `prompts/concept-verify-v1.md`.
De prompt is hieronder als referentie opgenomen. Werk strikt read-only:
schrijf alleen naar `data/extractie/gaps.json`.

## Input-bestanden

- **Records** ({len(records)} stuks): `{records_pad.relative_to(ROOT)}`
- **Anchors** ({len(anchors)} stuks): `{anchors_pad.relative_to(ROOT)}`
- **Examenvragen** ({len(examen_vragen)} stuks): `{vragen_pad.relative_to(ROOT)}`
- **Gaps-output**: `data/extractie/gaps.json` (append-only)

## Instructie

1. Laad de drie input-bestanden hierboven.
2. Voer Check A (examenvraag-simulatie), Check B (minicursus-haalbaarheid)
   en Check C (semantische coherentie) uit zoals beschreven in de prompt.
3. Schrijf gevonden gaps naar `data/extractie/gaps.json` (append, niet overschrijven).
4. Schrijf de samenvatting naar stdout.

---

## Prompt-referentie (concept-verify-v1.md)

{prompt_tekst}
"""

    instructies_pad.write_text(instructies, encoding="utf-8")
    return instructies_pad


# ─── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--programmaonderdeel",
        required=True,
        help="Programmaonderdeel-code, bv. '1.4' of '4.0'.",
    )
    parser.add_argument(
        "--records-glob",
        default="data/concept_records/*.json",
        help="Glob-patroon voor concept-records (relatief aan repo-root). "
             "Default: data/concept_records/*.json",
    )
    parser.add_argument(
        "--gaps-bestand",
        default=str(GAPS_FILE.relative_to(ROOT)),
        help="Pad naar gaps.json (relatief aan repo-root).",
    )
    parser.add_argument(
        "--droog",
        action="store_true",
        help="Droog uitvoeren: voer checks uit maar schrijf niets weg.",
    )
    args = parser.parse_args()

    programmaonderdeel_id: str = args.programmaonderdeel
    gaps_bestand = ROOT / args.gaps_bestand

    run_id = datetime.now(timezone.utc).strftime("verify-run-%Y%m%dT%H%M%SZ")
    print(f"[verify] {run_id} — programmaonderdeel {programmaonderdeel_id}")

    # Stap 1: records laden
    print(f"[records] laden via glob '{args.records_glob}' ...")
    records = load_records_for_programmaonderdeel(programmaonderdeel_id, args.records_glob)
    print(f"  {len(records)} records voor programmaonderdeel {programmaonderdeel_id}")
    if not records:
        print("  Geen records gevonden — controleer linked_anchors[] in de records.", file=sys.stderr)
        sys.exit(1)

    # Stap 2: anchors laden
    anchors = laad_anchors_voor_programmaonderdeel(programmaonderdeel_id)
    print(f"[anchors] {len(anchors)} anchors geladen uit {ANCHORS_FILE.relative_to(ROOT)}")
    if not anchors:
        print(
            f"  [WAARSCHUWING] Geen anchors gevonden voor {programmaonderdeel_id} in "
            f"{ANCHORS_FILE.relative_to(ROOT)}. VERIFY-checks C1/C2 zullen beperkt zijn.",
            file=sys.stderr,
        )

    # Stap 3: examenvragen laden
    examen_vragen = laad_examen_vragen_voor_programmaonderdeel(programmaonderdeel_id)
    print(f"[examen_vragen] {len(examen_vragen)} vragen geladen voor programmaonderdeel {programmaonderdeel_id}")

    # Stap 4: mechanische coherentie-checks
    print("[mechanisch] coherentie-checks ...")
    mechanische_gaps = mechanical_coherence_checks(records)
    print(
        f"  {len(mechanische_gaps)} mechanische gaps gevonden "
        f"(vergelijkingsparen-targets, edges-targets)"
    )

    # Stap 5: mechanische gaps wegschrijven
    if mechanische_gaps and not args.droog:
        toegevoegd = voeg_gaps_toe(mechanische_gaps, gaps_bestand)
        print(f"  {toegevoegd} nieuwe mechanische gaps toegevoegd aan {gaps_bestand.relative_to(ROOT)}")
    elif mechanische_gaps and args.droog:
        print(f"  [droog] {len(mechanische_gaps)} gaps NIET weggeschreven (--droog actief)")

    # Stap 6: subagent-instructies schrijven
    werkmap = ROOT / "data" / "extractie" / programmaonderdeel_id / "verify-runs"
    if not args.droog:
        instructies_pad = schrijf_subagent_instructies(
            programmaonderdeel_id=programmaonderdeel_id,
            records=records,
            anchors=anchors,
            examen_vragen=examen_vragen,
            run_id=run_id,
            werkmap=werkmap,
        )
        print(f"[subagent] instructies geschreven naar {instructies_pad.relative_to(ROOT)}")
        print(
            f"\nVolgende stap: open {instructies_pad.relative_to(ROOT)} "
            f"in een Opus-subagent-sessie om de LLM-checks uit te voeren."
        )
    else:
        print("[droog] subagent-instructies NIET geschreven (--droog actief)")

    # Samenvatting
    print(f"\n[samenvatting]")
    print(f"  Records gecheckt          : {len(records)}")
    print(f"  Mechanische gaps gevonden : {len(mechanische_gaps)}")
    print(f"  Examenvragen geladen      : {len(examen_vragen)}")
    if not args.droog:
        print(f"  gaps.json                 : {gaps_bestand.relative_to(ROOT)}")
        print(f"  Subagent-werkmap          : {werkmap.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
