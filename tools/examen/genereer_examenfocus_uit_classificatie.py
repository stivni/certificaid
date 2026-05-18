"""Bootstrap-generator voor `data/exam_focus/examenfocus--*.json`.

Zet bestaande vraag-classificaties (`_programmaonderdeel_classificatie.json`)
om naar examenfocus-stub-objecten zodat minicursus-render mode A (ADR-009 §6)
meteen werkt zonder dat een agent eerst alle examenfocus-records moet
cureren.

Eén examenfocus per geclassificeerde vraag. `concept_ids` is de
brede-fallback-set: alle concept-records van het primaire PO van de vraag
(ze voldoen daarmee aan de `concept_ids ⊆ records(PO)` filter, maar maken
geen fijne pedagogische distinctie — dat is curator-werk later).

Bestaande examenfocus-bestanden met `_provenance.curator: "mens"` of
`"agent"` (= echte curatie, geen bootstrap) worden NIET overschreven.
Bootstrap-objecten krijgen `_provenance.curator: "bootstrap"`.

Gebruik:
  python3 -m tools.examen.genereer_examenfocus_uit_classificatie
  python3 -m tools.examen.genereer_examenfocus_uit_classificatie --dry-run
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
EXAMEN_VRAGEN_DIR = ROOT / "data" / "programma" / "examen_vragen"
EXAM_FOCUS_DIR = ROOT / "data" / "exam_focus"
CLASSIFICATIE_FILE = EXAMEN_VRAGEN_DIR / "_programmaonderdeel_classificatie.json"


def _load_classificatie() -> dict:
    if not CLASSIFICATIE_FILE.exists():
        return {}
    return json.loads(CLASSIFICATIE_FILE.read_text(encoding="utf-8"))


def _records_per_po() -> dict[str, list[str]]:
    """Map PO-code → list van concept-record-IDs (linked_anchors prefix-match)."""
    result: dict[str, list[str]] = {}
    for pad in RECORDS_DIR.glob("*.json"):
        if pad.name.startswith("_"):
            continue
        try:
            r = json.loads(pad.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        record_id = r.get("id") or pad.stem
        anchors = r.get("linked_anchors", []) or []
        for a in anchors:
            # PO-code = eerste twee dot-segmenten (bv. "1.5.IV.B" → "1.5")
            parts = a.split(".")
            if len(parts) >= 2:
                po_code = f"{parts[0]}.{parts[1]}"
                result.setdefault(po_code, []).append(record_id)
    # Dedupliceer + sorteer voor deterministische output
    return {po: sorted(set(ids)) for po, ids in result.items()}


def _examen_tier(examen_id: str) -> str:
    """Lees `representativiteit_tier` uit examen-JSON; default 'C'."""
    pad = EXAMEN_VRAGEN_DIR / f"{examen_id}.json"
    if not pad.exists():
        return "C"
    try:
        data = json.loads(pad.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return "C"
    return data.get("representativiteit_tier", "C")


def _vraag_metadata(vraag_id: str, examen_id: str) -> tuple[str, str]:
    """Returns (vraag_nr, vak_naam) uit examen-JSON. Lege tuple bij niet-vinden."""
    pad = EXAMEN_VRAGEN_DIR / f"{examen_id}.json"
    if not pad.exists():
        return ("", "")
    try:
        data = json.loads(pad.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return ("", "")
    for v in data.get("vragen", []) or []:
        if v.get("id") == vraag_id:
            return (str(v.get("vraag_nr", "")), v.get("vak_naam_in_pdf", ""))
    return ("", "")


def _bootstrap_id(vraag_id: str) -> str:
    """Bootstrap-examenfocus krijgt id `examenfocus--bootstrap--<vraag_id>`."""
    return f"examenfocus--bootstrap--{vraag_id}"


def _is_overschrijfbaar(pad: Path) -> bool:
    """True als het bestand een bootstrap-stub is (geen mens/agent-curatie)."""
    if not pad.exists():
        return True
    try:
        existing = json.loads(pad.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return True
    curator = (existing.get("_provenance") or {}).get("curator", "")
    return curator == "bootstrap" or curator == ""


def genereer() -> tuple[int, int, int]:
    """Genereer examenfocus-stubs. Returnt (geschreven, overgeslagen, errors)."""
    classificatie = _load_classificatie()
    if not classificatie:
        print("[bootstrap] Geen classificatie-bestand gevonden — niets te doen.")
        return (0, 0, 0)

    records_per_po = _records_per_po()
    EXAM_FOCUS_DIR.mkdir(parents=True, exist_ok=True)

    nu = datetime.now(timezone.utc).isoformat(timespec="seconds")

    geschreven = 0
    overgeslagen = 0
    errors = 0

    for vraag_id, meta in classificatie.items():
        pos = meta.get("programmaonderdelen", []) or []
        if not pos:
            continue
        # Eerste PO als primair
        po_code = pos[0]
        concept_ids = records_per_po.get(po_code, [])
        if not concept_ids:
            errors += 1
            print(f"  [error] {vraag_id}: geen records voor PO {po_code}", flush=True)
            continue

        # examen_id = "<jaar>-<sessie>" prefix uit vraag_id "2024-1-vr7" → "2024-1"
        delen = vraag_id.rsplit("-", 1)
        examen_id = delen[0] if len(delen) == 2 else vraag_id

        vraag_nr, vak_naam = _vraag_metadata(vraag_id, examen_id)
        tier = _examen_tier(examen_id)

        focus_id = _bootstrap_id(vraag_id)
        pad = EXAM_FOCUS_DIR / f"{focus_id}.json"

        if not _is_overschrijfbaar(pad):
            overgeslagen += 1
            continue

        focus = {
            "id": focus_id,
            "schema_version": "1.0",
            "naam": vak_naam or f"Bootstrap-focus voor {vraag_id}",
            "concept_ids": concept_ids,
            "vraagvorm_id": "",
            "complexiteitspatroon_id": "",
            "wat_getoetst_wordt": (
                "Bootstrap-stub: deze focus is automatisch gegenereerd uit "
                "_programmaonderdeel_classificatie.json. concept_ids dekt alle "
                f"records van PO {po_code} — een curator kan dit verfijnen naar "
                "de echt geraakte concepten."
            ),
            "typische_formulering": [],
            "voorbeeldvragen": [
                {
                    "examen_id": examen_id,
                    "vraag_id": vraag_id,
                    "vraag_nr": vraag_nr,
                    "tier": tier,
                },
            ],
            "_provenance": {
                "tool": "tools/examen/genereer_examenfocus_uit_classificatie.py",
                "curator": "bootstrap",
                "created_at": nu,
                "updated_at": nu,
                "confidence": "inferred",
                "bron_classificatie": meta.get("rationale", "")[:200],
            },
        }
        pad.write_text(json.dumps(focus, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        geschreven += 1

    return (geschreven, overgeslagen, errors)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Toon plan, geen schrijfacties")
    args = parser.parse_args()

    if args.dry_run:
        cls = _load_classificatie()
        print(f"Classificatie-entries: {len(cls)}")
        po_count: dict[str, int] = {}
        for meta in cls.values():
            for p in meta.get("programmaonderdelen", []) or []:
                po_count[p] = po_count.get(p, 0) + 1
        for po, n in sorted(po_count.items()):
            print(f"  PO {po}: {n} vragen")
        return 0

    geschreven, overgeslagen, errors = genereer()
    print(f"\n[bootstrap] {geschreven} examenfocus-stubs geschreven, "
          f"{overgeslagen} overgeslagen (curator-handmatig), "
          f"{errors} errors.")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
