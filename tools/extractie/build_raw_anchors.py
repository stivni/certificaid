"""
Genereer raw-anchor-lijst per programmaonderdeel — input voor fase A
(anchor-verrijking) van de bron-first concept-extractie-pipeline (ADR-008).

In tegenstelling tot `match_bronnen.build_anchors_from_po` wordt **geen**
kern-filter toegepast: alle taken, doelstellingen en kenniselementen (incl.
subitems) komen in de output. Voor productie willen we globaal matchen — de
scope-filter was experiment-erfenis.

Output: data/extractie/<po>/anchors/<po>-anchors.raw.json

Gebruik:
  python3 -m tools.extractie.build_raw_anchors                # alle PO's
  python3 -m tools.extractie.build_raw_anchors --po 2.2       # één PO
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PO_DIR = ROOT / "data" / "programmaonderdelen"
OUT_DIR_BASE = ROOT / "data" / "extractie"


def _walk_kenniselementen(items: list, parent_path: list[str]) -> list[dict]:
    out: list[dict] = []
    for ke in items:
        code = ke["code"]
        tekst = ke["tekst"]
        out.append({
            "anchor_id": code,
            "anchor_type": "kenniselement",
            "tekst": tekst,
            "parent_path": list(parent_path),
        })
        if "subitems" in ke and ke["subitems"]:
            out.extend(_walk_kenniselementen(ke["subitems"], parent_path + [tekst]))
    return out


def _dedup_ids(anchors: list[dict]) -> list[dict]:
    """Suffix duplicate anchor_ids met `__2`, `__3`, ... — eerste occurrence
    behoudt de originele id. Nodig omdat de PO-PDF-destillatie soms dezelfde
    KE-nummering hergebruikt voor verschillende secties (bv. PO 1.9 heeft
    `I.B.1` viermaal voor verschillende onderwerpen)."""
    seen: dict[str, int] = {}
    for a in anchors:
        aid = a["anchor_id"]
        seen[aid] = seen.get(aid, 0) + 1
        if seen[aid] > 1:
            a["anchor_id"] = f"{aid}__{seen[aid]}"
    return anchors


def build_all_anchors(po_data: dict) -> list[dict]:
    anchors: list[dict] = []
    po_titel = po_data["titel"]

    for tb in po_data.get("taakblokken", []):
        tb_code = tb["code"]
        tb_titel = tb.get("titel", "")
        for i, taak in enumerate(tb.get("taken", []), 1):
            tekst = taak["tekst"] if isinstance(taak, dict) else taak
            anchors.append({
                "anchor_id": f"{tb_code}.taak.{i}",
                "anchor_type": "taak",
                "taakblok": tb_code,
                "taakblok_titel": tb_titel,
                "tekst": tekst,
            })
        for i, doel in enumerate(tb.get("doelstellingen", []), 1):
            tekst = doel["tekst"] if isinstance(doel, dict) else doel
            anchors.append({
                "anchor_id": f"{tb_code}.doel.{i}",
                "anchor_type": "doelstelling",
                "taakblok": tb_code,
                "taakblok_titel": tb_titel,
                "tekst": tekst,
            })

    for ke in po_data.get("kenniselementen", []):
        anchors.extend(_walk_kenniselementen([ke], parent_path=[po_titel]))

    return _dedup_ids(anchors)


def list_po_files(po_filter: str | None) -> list[Path]:
    if po_filter:
        files = sorted(PO_DIR.glob(f"{po_filter}-*.json"))
    else:
        files = sorted(p for p in PO_DIR.glob("*.json"))
    return [p for p in files if not p.name.startswith("README")]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--po", default=None, help="filter op PO-code, bv. 2.2")
    parser.add_argument("--force", action="store_true",
                        help="overschrijf bestaande raw-anchors.json")
    args = parser.parse_args()

    files = list_po_files(args.po)
    if not files:
        raise SystemExit(f"Geen PO-JSONs gevonden{f' voor {args.po}' if args.po else ''}")

    for po_file in files:
        data = json.loads(po_file.read_text())
        po = str(data["programmaonderdeel"])
        anchors = build_all_anchors(data)

        out_dir = OUT_DIR_BASE / po / "anchors"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{po}-anchors.raw.json"

        if out_path.exists() and not args.force:
            print(f"  {po}: {out_path.relative_to(ROOT)} bestaat al — skip (--force om te overschrijven)")
            continue

        out_path.write_text(json.dumps({
            "po": po,
            "titel": data["titel"],
            "po_file": po_file.name,
            "n_anchors": len(anchors),
            "anchors": anchors,
        }, ensure_ascii=False, indent=2))
        print(f"  {po}: {len(anchors)} anchors → {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
