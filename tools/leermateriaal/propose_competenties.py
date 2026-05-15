"""
Fase D — Competentie-destillatie subagent-runner (ADR-008 §14).

Bouwt input-payload voor een Opus-subagent die competentie-voorstellen
destilleert uit anchors + concept-records + exam_patterns.

Examenvragen worden NIET als input gebruikt (anti-circulariteit, ADR-008 §0).
Alleen exam_patterns (vraagvormen + complexiteitspatronen) zijn toegestaan.

Output: subagent-instructies in data/extractie/<X.Y>/competentie-runs/<run-id>/

Gebruik:
  python3 -m tools.leermateriaal.propose_competenties --programmaonderdeel 1.4
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
ANCHORS_FILE = ROOT / "data" / "programma" / "anchors.json"
PROGRAMMA_FILE = ROOT / "data" / "programma" / "programma.json"
EXAM_PATTERNS_DIR = ROOT / "data" / "programma" / "exam_patterns"
EXTRACTIE_DIR = ROOT / "data" / "extractie"
PROMPTS_DIR = ROOT / "prompts"
DESTILLATIE_PROMPT = PROMPTS_DIR / "competentie-destillatie-v1.md"

DESTILLATIE_MODEL = "claude-opus-4-7"


def _laad_anchors_voor_programmaonderdeel(programmaonderdeel_id: str) -> list[dict]:
    """Laad anchors voor een programmaonderdeel uit data/programma/anchors.json."""
    if not ANCHORS_FILE.exists():
        return []
    data = json.loads(ANCHORS_FILE.read_text(encoding="utf-8"))
    prefix = f"{programmaonderdeel_id}."
    return [
        anker for anker in data.get("anchors", [])
        if anker.get("anchor_id", "").startswith(prefix)
    ]


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


def _laad_exam_patterns(programmaonderdeel_id: str) -> list[dict]:
    """Laad exam_patterns voor een programmaonderdeel (NIET examenvragen).

    Exam-patterns (vraagvormen, complexiteitspatronen) zijn PO-onafhankelijke
    catalogi. We laden alles tenzij een bestand expliciet aan een ander PO
    gekoppeld is.
    """
    patterns: list[dict] = []
    for bestand in sorted(EXAM_PATTERNS_DIR.glob("*.json")):
        try:
            data = json.loads(bestand.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        eigen_po = str(data.get("programmaonderdeel", ""))
        po_lijst = data.get("programmaonderdelen", [])
        if eigen_po and eigen_po != programmaonderdeel_id:
            continue
        if po_lijst and programmaonderdeel_id not in po_lijst:
            continue
        patterns.append(data)
    return patterns


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
    run_id = datetime.now(timezone.utc).strftime("competentie-run-%Y%m%dT%H%M%SZ")

    print(f"[propose_competenties] {run_id} — programmaonderdeel {programmaonderdeel_id}")

    # Data laden
    anchors = _laad_anchors_voor_programmaonderdeel(programmaonderdeel_id)
    print(f"  Anchors: {len(anchors)}")

    records = _laad_records_voor_programmaonderdeel(programmaonderdeel_id)
    print(f"  Concept-records: {len(records)}")
    if not records:
        print("FOUT: geen records gevonden. Voer eerst concept-extractie uit.", file=sys.stderr)
        sys.exit(1)

    exam_patterns = _laad_exam_patterns(programmaonderdeel_id)
    print(f"  Exam-patterns: {len(exam_patterns)}")

    programma_context = _laad_programma_context(programmaonderdeel_id)

    # Werkmap + bestanden aanmaken
    werkmap = EXTRACTIE_DIR / programmaonderdeel_id / "competentie-runs" / run_id

    if not args.droog:
        werkmap.mkdir(parents=True, exist_ok=True)

        records_pad = werkmap / "records.json"
        anchors_pad = werkmap / "anchors.json"
        patterns_pad = werkmap / "exam_patterns.json"

        records_pad.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
        anchors_pad.write_text(json.dumps(anchors, ensure_ascii=False, indent=2), encoding="utf-8")
        patterns_pad.write_text(json.dumps(exam_patterns, ensure_ascii=False, indent=2), encoding="utf-8")

    # Record-summaries voor de prompt
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
            "definitie_snippet": str(hoofdveld.get("text", ""))[:400],
            "linked_anchors": record.get("linked_anchors", []),
        })

    prompt_tekst = DESTILLATIE_PROMPT.read_text(encoding="utf-8") if DESTILLATIE_PROMPT.exists() else (
        "[WAARSCHUWING: competentie-destillatie-v1.md niet gevonden]"
    )

    instructies = f"""# Competentie-destillatie-run {run_id} — Instructies voor Opus

**Programmaonderdeel**: {programmaonderdeel_id}
**Run-id**: {run_id}
**Gegenereerd op**: {datetime.now(timezone.utc).isoformat(timespec="seconds")}
**Model**: {DESTILLATIE_MODEL}

## Jouw taak

Destilleer competentie-voorstellen voor programmaonderdeel {programmaonderdeel_id}
conform `prompts/competentie-destillatie-v1.md`. Geen vooraf vastgelegd aantal —
stel zoveel competenties voor als het programmaonderdeel werkelijk vraagt.

**KRITISCH**: Gebruik GEEN examenvragen als input. Alleen de meegeleverde
concept-records, anchors en exam_patterns.

## Anti-fabricatie-regels (hard — herhaling voor zekerheid)

1. Stel ALLEEN competenties voor waarvan de procedure mechanisch afleidbaar is
   uit de gerefereerde concept-records hieronder.
2. Elke stap MOET grondslag.ref hebben — [[concept-id]], wettekst, of
   type: praktijk met expliciete motivering.
3. gebaseerd_op_concepten ≥ 2 verplicht.
4. Voorbeelden ALLEEN op basis van scenario's uit de definitie-teksten hieronder.
5. procedure_grondslag.wettelijk_pct + praktijk_pct == 100.

## Input-bestanden

- **Records** ({len(records)} stuks):
{"  " + chr(10) + "  ".join(f"- `{r.get('id', '?')}` ({r.get('node_type', '?')}): {str((r.get('definitie') or r.get('main_rule') or r.get('verplichting') or r.get('doel') or {{}}).get('text', ''))[:100]}..." for r in records)}

- **Anchors** ({len(anchors)} stuks): `{werkmap.relative_to(ROOT) if not args.droog else "data/extractie/.../anchors.json"}`
- **Exam-patterns** ({len(exam_patterns)} bestanden): vraagvormen + complexiteitspatronen

## Programmaonderdeel-context

Titel: {programma_context.get('titel', '?')}
Intro: {str(programma_context.get('intro_tekst', ''))[:500]}

## Output-locatie

Schrijf elke competentie als YAML-bestand naar:
`data/concepten/competenties/<id>.yaml`

Schema: zie `prompts/competentie-destillatie-v1.md` §Output-schema

---

## Prompt-referentie (competentie-destillatie-v1.md)

{prompt_tekst}
"""

    if not args.droog:
        instructies_pad = werkmap / "instructies.md"
        instructies_pad.write_text(instructies, encoding="utf-8")
        print(f"\n[propose_competenties] Instructies geschreven: {instructies_pad.relative_to(ROOT)}")
        print(f"\nVolgende stap:")
        print(f"  Open {instructies_pad.relative_to(ROOT)} in een Opus-subagent-sessie.")
        print(f"  Output: data/concepten/competenties/<id>.yaml (aantal volgt uit scope)")
        print(f"  Daarna: python3 -m tools.leermateriaal.render_competentie_fiche \\")
        print(f"            --programmaonderdeel {programmaonderdeel_id}")
    else:
        print("[droog] Instructies NIET weggeschreven.")
        print("[droog] Payload opgebouwd:")
        print(f"  Records: {len(records)}, Anchors: {len(anchors)}, Patterns: {len(exam_patterns)}")


if __name__ == "__main__":
    main()
