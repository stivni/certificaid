"""
Fase E — Leerpad-opstelling subagent-runner (ADR-008 §15).

Vereist: alle competenties voor de PO met status 'voorgesteld' of 'gecureerd'.
Bouwt input-payload voor Opus-subagent die het leerpad ordent.

Output: subagent-instructies in data/extractie/<X.Y>/leerpad-runs/<run-id>/

Gebruik:
  python3 -m tools.leermateriaal.propose_leerpad --programmaonderdeel 1.4
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
COMPETENTIES_DIR = ROOT / "data" / "concepten" / "competenties"
PROGRAMMA_FILE = ROOT / "data" / "programma" / "programma.json"
EXTRACTIE_DIR = ROOT / "data" / "extractie"
PROMPTS_DIR = ROOT / "prompts"
LEERPAD_PROMPT = PROMPTS_DIR / "leerpad-propose-v1.md"

LEERPAD_MODEL = "claude-opus-4-7"


def _laad_records_voor_programmaonderdeel(programmaonderdeel_id: str) -> list[dict]:
    """Laad concept-records voor een programmaonderdeel."""
    prefix = f"{programmaonderdeel_id}."
    records = []
    for bestand in sorted(RECORDS_DIR.glob("*.json")):
        if bestand.name.startswith("_"):
            continue
        try:
            record = json.loads(bestand.read_text(encoding="utf-8"))
            if any(a.startswith(prefix) for a in record.get("linked_anchors", [])):
                records.append(record)
        except (json.JSONDecodeError, OSError):
            pass
    return records


def _laad_competenties_voor_programmaonderdeel(programmaonderdeel_id: str) -> list[dict]:
    """Laad alle competenties voor een programmaonderdeel (alle statussen)."""
    resultaat = []
    for bestand in sorted(COMPETENTIES_DIR.glob("*.yaml")):
        if bestand.name.startswith("_"):
            continue
        try:
            with open(bestand, encoding="utf-8") as f:
                comp = yaml.safe_load(f)
            if isinstance(comp, dict) and programmaonderdeel_id in [
                str(p) for p in comp.get("programmaonderdelen", [])
            ]:
                resultaat.append(comp)
        except (yaml.YAMLError, OSError):
            pass
    return resultaat


def _laad_programma_context(programmaonderdeel_id: str) -> dict:
    """Laad programmaonderdeel-context uit programma.json."""
    if not PROGRAMMA_FILE.exists():
        return {}
    try:
        programma = json.loads(PROGRAMMA_FILE.read_text(encoding="utf-8"))
        for po in programma.get("programmaonderdelen", []):
            if str(po.get("code", "")) == programmaonderdeel_id:
                return po
    except (json.JSONDecodeError, KeyError):
        pass
    return {}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--programmaonderdeel",
        required=True,
        help="Programmaonderdeel-code, bv. '1.4'.",
    )
    parser.add_argument(
        "--droog",
        action="store_true",
        help="Droog uitvoeren: bouw payload maar schrijf geen instructies.",
    )
    args = parser.parse_args()

    programmaonderdeel_id: str = args.programmaonderdeel
    run_id = datetime.now(timezone.utc).strftime("leerpad-run-%Y%m%dT%H%M%SZ")

    print(f"[propose_leerpad] {run_id} — programmaonderdeel {programmaonderdeel_id}")

    # Competenties laden
    competenties = _laad_competenties_voor_programmaonderdeel(programmaonderdeel_id)
    print(f"  Competenties: {len(competenties)}")

    if not competenties:
        print(
            f"FOUT: geen competenties gevonden voor {programmaonderdeel_id}. "
            f"Voer eerst propose_competenties + mens-curatie uit.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Statussen controleren
    statussen = {c.get("status", "onbekend") for c in competenties}
    geldige_statussen = {"voorgesteld", "gecureerd"}
    if not statussen.issubset(geldige_statussen | {"onbekend"}):
        print(
            f"  [WAARSCHUWING] Competentie-statussen: {statussen}. "
            f"Alleen 'voorgesteld' en 'gecureerd' zijn aanbevolen.",
            file=sys.stderr,
        )

    # Records laden
    records = _laad_records_voor_programmaonderdeel(programmaonderdeel_id)
    print(f"  Concept-records: {len(records)}")

    # Programma-context
    programma_context = _laad_programma_context(programmaonderdeel_id)

    # Werkmap
    werkmap = EXTRACTIE_DIR / programmaonderdeel_id / "leerpad-runs" / run_id

    if not args.droog:
        werkmap.mkdir(parents=True, exist_ok=True)

    # Record-summaries voor didactische clustering
    record_summaries = []
    for record in records:
        hoofdveld = (
            record.get("definitie")
            or record.get("main_rule")
            or record.get("verplichting")
            or record.get("doel")
            or {}
        )
        record_summaries.append({
            "id": record.get("id", ""),
            "naam": record.get("naam", ""),
            "node_type": record.get("node_type", ""),
            "definitie_snippet": str(hoofdveld.get("text", ""))[:300],
            "linked_anchors": record.get("linked_anchors", []),
        })

    # Competentie-summaries
    comp_summaries = []
    for comp in competenties:
        comp_summaries.append({
            "id": comp.get("id", ""),
            "titel": comp.get("titel", ""),
            "status": comp.get("status", ""),
            "gebaseerd_op_concepten": comp.get("gebaseerd_op_concepten", []),
            "voortkomend_uit": comp.get("voortkomend_uit", {}),
            "stap_titels": [s.get("titel", "") for s in comp.get("stappen", [])],
        })

    prompt_tekst = LEERPAD_PROMPT.read_text(encoding="utf-8") if LEERPAD_PROMPT.exists() else (
        "[WAARSCHUWING: leerpad-propose-v1.md niet gevonden]"
    )

    instructies = f"""# Leerpad-propose-run {run_id} — Instructies voor Opus

**Programmaonderdeel**: {programmaonderdeel_id}
**Run-id**: {run_id}
**Gegenereerd op**: {datetime.now(timezone.utc).isoformat(timespec="seconds")}
**Model**: {LEERPAD_MODEL}

## Jouw taak

Stel een leerpad voor programmaonderdeel {programmaonderdeel_id} voor
conform `prompts/leerpad-propose-v1.md`.

## Ordening-principe (didactische opbouw)

oriëntatie → conceptuele basis (begrippen/regels) → wie (actoren) →
hoe (procedures/methoden via competenties) → bijzonderheden (uitzonderingen) →
context (IFRS, Europese richtlijn, etc.)

## Anti-fabricatie

- Oriëntatie-blokken MOETEN rationale_hint geven die verwijst naar bestaande
  concept-records (id's hieronder).
- Thematische clusters MOGEN ALLEEN bestaande record-id's bevatten.
- Geen nieuwe competentie-id's bedenken — gebruik alleen id's hieronder.

## Competenties beschikbaar ({len(competenties)} stuks)

```json
{json.dumps(comp_summaries, ensure_ascii=False, indent=2)}
```

## Concept-records beschikbaar ({len(records)} stuks)

```json
{json.dumps(record_summaries, ensure_ascii=False, indent=2)}
```

## Programmaonderdeel-context

Titel: {programma_context.get('titel', '?')}
Intro: {str(programma_context.get('intro_tekst', ''))[:600]}

## Output-locatie

Schrijf het leerpad als YAML naar:
`data/concepten/leerpaden/{programmaonderdeel_id}.yaml`

Schema: zie `prompts/leerpad-propose-v1.md` §Leerpad-schema

---

## Prompt-referentie (leerpad-propose-v1.md)

{prompt_tekst}
"""

    if not args.droog:
        instructies_pad = werkmap / "instructies.md"
        instructies_pad.write_text(instructies, encoding="utf-8")
        print(f"\n[propose_leerpad] Instructies geschreven: {instructies_pad.relative_to(ROOT)}")
        print(f"\nVolgende stap:")
        print(f"  Open {instructies_pad.relative_to(ROOT)} in een Opus-subagent-sessie.")
        print(f"  Output: data/concepten/leerpaden/{programmaonderdeel_id}.yaml")
        print(f"  Daarna: python3 -m tools.leermateriaal.render_minicursus \\")
        print(f"            --programmaonderdeel {programmaonderdeel_id}")
    else:
        print("[droog] Instructies NIET weggeschreven.")
        print(f"[droog] Payload: {len(competenties)} competenties, {len(records)} records")


if __name__ == "__main__":
    main()
