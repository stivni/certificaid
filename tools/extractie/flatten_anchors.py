"""
Flatten `data/programma.json` (geneste hiërarchie) naar per-PO ankerlijsten
voor `match_bronnen.py`. Produceert hetzelfde schema als de oude
`<po>-anchors.json`, maar met code-paden uit het nieuwe schema:

  - <po>.taak.<n>
  - <po>.taak.<n>.<a/b/...>          (subtaak)
  - <po>.taak.<n>.doel.<m>
  - <po>.taak.<n>.doel.<m>.<a/b/...> (subdoel)
  - <po>.<I/II/...>[.<A/B>...]        (kenniselement, ongewijzigd)

Vervangt de oude `build_raw_anchors.py` die werkte op losse PO-JSONs
zonder hiërarchie. Run dit elke keer als `data/programma.json` verandert.

Output: data/extractie/<po>/anchors/<po>-anchors.json (overschreven)
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PROGRAMMA = ROOT / "data" / "programma.json"
OUT_BASE = ROOT / "data" / "extractie"


def _flatten_po(po: dict) -> list[dict]:
    """Maak de flat ankerlijst voor één PO. Bewaart anchor_type-onderscheid."""
    anchors: list[dict] = []
    po_code = po["code"]

    def emit(node: dict, anchor_type: str, **extra) -> None:
        a = {
            "anchor_id": node["code"],
            "anchor_type": anchor_type,
            "tekst": node.get("tekst", ""),
            "verbose": node.get("verbose"),
            "synoniemen": node.get("synoniemen", []),
        }
        a.update(extra)
        anchors.append(a)

    for taak in po.get("taken", []):
        emit(taak, "taak")
        for sub in taak.get("subtaken", []) or []:
            emit(sub, "subtaak", parent=taak["code"])
        for doel in taak.get("doelstellingen", []) or []:
            emit(doel, "doelstelling", parent=taak["code"])
            for subdoel in doel.get("subdoelen", []) or []:
                emit(subdoel, "subdoel", parent=doel["code"])

    def walk_ke(items: list[dict]) -> None:
        for it in items:
            emit(it, "kenniselement")
            if it.get("subitems"):
                walk_ke(it["subitems"])

    walk_ke(po.get("kenniselementen", []))
    return anchors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="alleen tellen, niet schrijven")
    args = parser.parse_args()

    data = json.loads(PROGRAMMA.read_text())
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    grand_total = 0
    for po in data["programmaonderdelen"]:
        po_code = po["code"]
        anchors = _flatten_po(po)
        n = len(anchors)
        grand_total += n

        # Validatie: geen ontbrekende verbose
        n_no_verbose = sum(1 for a in anchors if not a.get("verbose"))
        flag = f"  ⚠ {n_no_verbose} zonder verbose" if n_no_verbose else ""

        out_dir = OUT_BASE / po_code / "anchors"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{po_code}-anchors.json"

        payload = {
            "po": po_code,
            "titel": po.get("titel", ""),
            "generated_at": now,
            "source": "data/programma.json",
            "n_anchors": n,
            "anchors": anchors,
        }

        if not args.dry_run:
            out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

        print(f"  {po_code}: {n} anchors → {out_path.relative_to(ROOT)}{flag}")

    print(f"\nTotaal: {grand_total} ankers over {len(data['programmaonderdelen'])} PO's")
    if args.dry_run:
        print("(dry-run — geen bestanden geschreven)")


if __name__ == "__main__":
    main()
