"""
Delta-rapport: identificeer record-upgrade- en concept-discover-kandidaten
op basis van bundle-diff tussen de huidige SQLite matches-store en de
bundle-samenstelling vastgelegd in record-provenance (ADR-005 §9.1 +
ADR-008 §13.8-voorstel).

Twee dimensies:

1. **Records-dimensie** ("EXPAND-kandidaten")
   Voor elk bestaand record:
     - Welke linked_anchors heeft het record?
     - Welke chunks zijn in de huidige bundle voor die anchors die NIET in
       de record's eigen `_provenance.inputs[]` zitten?
     - Prio-bucket:
         HIGH    — record heeft `_provenance.bron_gap` ≠ null OF ≥1 veld
                   met confidence == 'inferred-common-knowledge'
                   EN ≥1 nieuwe chunk beschikbaar
         MEDIUM  — ≥1 nieuwe chunk uit een primaire-bron-collectie (IFRS,
                   ISA, wetteksten) beschikbaar
         LOW     — alleen secundaire-bron-chunks (CBN-adviezen, andere
                   normen) als delta
         NONE    — geen delta (record blijft onaangetast)

2. **Anchors-dimensie** ("DISCOVER-kandidaten")
   Voor elke anchor:
     - Welke chunks zitten in de bundle maar raken geen bestaand
       record (geen enkel record gebruikt die chunk in zijn inputs)?
     - Per anchor: aantal "orphan-chunks" + bron-samenvatting

Output: `data/extractie/delta-rapport.json` met machine-leesbare entries +
`data/extractie/delta-rapport.md` met mens-leesbare samenvatting per PO.

Gebruik:
    python3 -m tools.extractie.delta_pass
    python3 -m tools.extractie.delta_pass --db-path data/extractie/matches.sqlite3
"""
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
OUTPUT_JSON = ROOT / "data" / "extractie" / "delta-rapport.json"
OUTPUT_MD = ROOT / "data" / "extractie" / "delta-rapport.md"

import json
from tools.lib.matches_store import DEFAULT_DB_PATH, open_store, get_bundle


def _bron_uit_chunk_id(cid: str) -> str:
    """Extract bron-naam uit chunk_id (alles voor de eerste '__')."""
    return cid.split("__", 1)[0]


# Primaire-bron-prefixen: wetteksten + IFRS + ISA + IESBA. Secundair = CBN-adviezen.
_PRIMAIR_PREFIXEN = ("IAS-", "IFRS-", "IFRIC-", "ISA-", "IESBA-")


def _is_primair(bron_naam: str) -> bool:
    if any(bron_naam.startswith(p) for p in _PRIMAIR_PREFIXEN):
        return True
    # Wetteksten zoals WVV, WER, KB-*, ITAA-norm-*, WIB, WBTW
    if bron_naam.startswith(("WVV", "WER", "KB-", "ITAA-norm-", "WIB", "WBTW", "BBHR-", "BV-")):
        return True
    if "wet" in bron_naam.lower() and "advies" not in bron_naam.lower():
        return True
    return False


def _load_bundles_from_store(db_path: Path) -> dict[str, set[str]]:
    """Laad anchor → set(chunk_id) uit de SQLite matches-store."""
    conn = open_store(db_path)
    rows = conn.execute(
        "SELECT anchor_id, chunk_id FROM matches WHERE in_bundle = 1"
    ).fetchall()
    conn.close()
    bundles: dict[str, set[str]] = defaultdict(set)
    for anchor_id, chunk_id in rows:
        bundles[anchor_id].add(chunk_id)
    return dict(bundles)


def _load_records() -> list[dict]:
    out = []
    for p in sorted(RECORDS_DIR.glob("*.json")):
        if p.name.startswith("_"):
            continue
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
            r["_path"] = p.name
            out.append(r)
        except json.JSONDecodeError:
            continue
    return out


def _gather_used_chunks(record: dict) -> set[str]:
    """Verzamel alle chunk_id's die ergens in een _provenance.inputs[] van record zitten."""
    chunks: set[str] = set()

    def walk(obj):
        if isinstance(obj, dict):
            inputs = obj.get("_provenance", {}).get("inputs", []) if "_provenance" in obj else []
            if isinstance(inputs, list):
                for i in inputs:
                    if isinstance(i, dict) and i.get("id"):
                        chunks.add(i["id"])
                    elif isinstance(i, str):
                        chunks.add(i)
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    walk(record)
    return chunks


def _record_has_inferred_confidence(record: dict) -> bool:
    """True als ≥1 veld in record een confidence-label met 'inferred' heeft."""
    found = [False]

    def walk(obj):
        if found[0]:
            return
        if isinstance(obj, dict):
            conf = obj.get("confidence", "")
            if isinstance(conf, str) and "inferred" in conf:
                found[0] = True
                return
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    walk(record)
    return found[0]


def _prio_voor_record(record: dict, delta_chunks: set[str]) -> str:
    """Bepaal prio-bucket op basis van record-toestand + delta-chunks."""
    if not delta_chunks:
        return "NONE"

    heeft_bron_gap = bool(record.get("_provenance", {}).get("bron_gap"))
    heeft_inferred = _record_has_inferred_confidence(record)
    heeft_primair_delta = any(_is_primair(_bron_uit_chunk_id(c)) for c in delta_chunks)

    if (heeft_bron_gap or heeft_inferred) and heeft_primair_delta:
        return "HIGH"
    if heeft_primair_delta:
        return "MEDIUM"
    return "LOW"


def _po_uit_anchor(anchor_id: str) -> str:
    parts = anchor_id.split(".")
    return f"{parts[0]}.{parts[1]}" if len(parts) >= 2 else anchor_id


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument(
        "--db-path",
        type=Path,
        default=None,
        help="pad naar SQLite matches-store (default: data/extractie/matches.sqlite3)",
    )
    args = p.parse_args()

    db_path = args.db_path or DEFAULT_DB_PATH
    if not db_path.is_absolute():
        db_path = ROOT / db_path

    if not db_path.exists():
        raise SystemExit(
            f"SQLite matches-store niet gevonden: {db_path}. "
            "Draai eerst `python3 -m tools.extractie.match_bronnen`."
        )

    print(f"Bundles laden uit: {db_path.relative_to(ROOT)}\n")
    bundles = _load_bundles_from_store(db_path)
    print(f"Anchors met bundle: {len(bundles)}")

    records = _load_records()
    print(f"Records geladen: {len(records)}")

    # === Records-dimensie ===
    # Filter op echt-nieuwe-bron-chunks (IFRS/IAS/IFRIC/ISA) om threshold-drift uit te sluiten.
    def _is_echt_nieuw(cid: str) -> bool:
        bron = _bron_uit_chunk_id(cid)
        return bron.startswith(("IAS-", "IFRS-", "IFRIC-", "ISA-"))

    records_rapport = []
    for r in records:
        used_chunks = _gather_used_chunks(r)
        linked_anchors = r.get("linked_anchors", [])

        # Union van echt-nieuwe-bron-chunks in de huidige bundles van zijn anchors
        beschikbaar = set()
        for aid in linked_anchors:
            for cid in bundles.get(aid, set()):
                if _is_echt_nieuw(cid):
                    beschikbaar.add(cid)

        # Echte delta = beschikbaar maar record gebruikt 'm niet
        echte_delta = beschikbaar - used_chunks

        if not echte_delta and not r.get("_provenance", {}).get("bron_gap"):
            continue  # geen werk

        prio = _prio_voor_record(r, echte_delta)
        if prio == "NONE" and not r.get("_provenance", {}).get("bron_gap"):
            continue

        # Top-bronnen samenvatting
        bronnen_per_chunk = defaultdict(int)
        for cid in echte_delta:
            bronnen_per_chunk[_bron_uit_chunk_id(cid)] += 1
        top_bronnen = sorted(bronnen_per_chunk.items(), key=lambda x: -x[1])[:5]

        records_rapport.append({
            "record": r["_path"],
            "naam": r.get("naam", ""),
            "node_type": r.get("node_type", ""),
            "linked_anchors": linked_anchors,
            "bron_gap": r.get("_provenance", {}).get("bron_gap"),
            "heeft_inferred": _record_has_inferred_confidence(r),
            "used_inputs_count": len(used_chunks),
            "echte_delta_count": len(echte_delta),
            "top_bronnen": [{"bron": b, "n": n} for b, n in top_bronnen],
            "prio": prio,
        })

    # === Anchors-dimensie ===
    alle_gebruikte_chunks: set[str] = set()
    for r in records:
        alle_gebruikte_chunks |= _gather_used_chunks(r)

    anchors_rapport = []
    for aid, chunks in sorted(bundles.items()):
        # Alleen echt-nieuwe-bron chunks die geen record raken
        nieuwe_uit_nieuwe_bron = {c for c in chunks if _is_echt_nieuw(c)}
        orphan_chunks = nieuwe_uit_nieuwe_bron - alle_gebruikte_chunks
        if not orphan_chunks:
            continue

        bronnen_per_chunk = defaultdict(int)
        for cid in orphan_chunks:
            bronnen_per_chunk[_bron_uit_chunk_id(cid)] += 1
        top_bronnen = sorted(bronnen_per_chunk.items(), key=lambda x: -x[1])[:8]

        anchors_rapport.append({
            "anchor_id": aid,
            "po": _po_uit_anchor(aid),
            "orphan_chunks_count": len(orphan_chunks),
            "top_bronnen": [{"bron": b, "n": n} for b, n in top_bronnen],
        })

    # === Output JSON ===
    out = {
        "gegenereerd_op": datetime.now(timezone.utc).isoformat(),
        "store": str(db_path.relative_to(ROOT)),
        "records": records_rapport,
        "anchors": anchors_rapport,
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"→ {OUTPUT_JSON.relative_to(ROOT)}")

    # === Output MD ===
    md = []
    md.append("# Delta-rapport — bron-refresh-impact")
    md.append("")
    md.append(f"_Gegenereerd op {out['gegenereerd_op']}._")
    md.append(f"_Store: `{out['store']}`_")
    md.append("")

    md.append("## Samenvatting")
    md.append("")
    prio_counts = defaultdict(int)
    for r in records_rapport:
        prio_counts[r["prio"]] += 1
    md.append(f"- **Records met delta**: {len(records_rapport)} (van {len(records)})")
    md.append(f"  - HIGH (bron-gap of inferred + primaire delta): **{prio_counts['HIGH']}**")
    md.append(f"  - MEDIUM (primaire delta, grounded record): {prio_counts['MEDIUM']}")
    md.append(f"  - LOW (alleen secundaire delta): {prio_counts['LOW']}")
    md.append(f"- **Anchors met orphan-chunks** (mogelijk nieuwe fenomenen): {len(anchors_rapport)}")
    md.append("")

    # Per PO breakdown
    per_po_records = defaultdict(lambda: defaultdict(int))
    for r in records_rapport:
        for aid in r["linked_anchors"]:
            po = _po_uit_anchor(aid)
            per_po_records[po][r["prio"]] += 1
            break  # tel record één keer
    per_po_anchors = defaultdict(int)
    for a in anchors_rapport:
        per_po_anchors[a["po"]] += a["orphan_chunks_count"]

    md.append("## Per programmaonderdeel")
    md.append("")
    md.append("| PO | Records HIGH | MEDIUM | LOW | Orphan primaire-chunks |")
    md.append("|---|---|---|---|---|")
    alle_po = sorted(set(per_po_records.keys()) | set(per_po_anchors.keys()))
    for po in alle_po:
        h = per_po_records[po]["HIGH"]
        m = per_po_records[po]["MEDIUM"]
        lc = per_po_records[po]["LOW"]
        o = per_po_anchors[po]
        md.append(f"| {po} | {h} | {m} | {lc} | {o} |")
    md.append("")

    # Top-HIGH records
    high_records = [r for r in records_rapport if r["prio"] == "HIGH"]
    high_records.sort(key=lambda r: -r["echte_delta_count"])

    md.append("## Top HIGH-prio records (bron-upgrade-kandidaten)")
    md.append("")
    md.append("Records met een expliciete `bron_gap` of `inferred-common-knowledge`-claim, waar nu primaire bronnen beschikbaar zijn.")
    md.append("")
    md.append("| Record | PO | echte-delta | Top bronnen (chunks) |")
    md.append("|---|---|---|---|")
    for r in high_records[:30]:
        po = _po_uit_anchor(r["linked_anchors"][0]) if r["linked_anchors"] else "?"
        bronnen = ", ".join(f"{b['bron'][:30]} ({b['n']})" for b in r["top_bronnen"][:3])
        md.append(f"| `{r['record']}` | {po} | {r['echte_delta_count']} | {bronnen} |")
    if len(high_records) > 30:
        md.append(f"\n_… +{len(high_records) - 30} meer HIGH-records (zie JSON-rapport)._")
    md.append("")

    # Top anchors met orphan chunks
    md.append("## Top anchors met orphan-chunks (DISCOVER-kandidaten)")
    md.append("")
    md.append("Anchors waar echt-nieuwe-bron-chunks beschikbaar zijn die nog géén record raken — mogelijk nieuwe fenomenen.")
    md.append("")
    md.append("| Anchor | PO | orphan-count | Top bronnen (chunks) |")
    md.append("|---|---|---|---|")
    anchors_rapport.sort(key=lambda a: -a["orphan_chunks_count"])
    for a in anchors_rapport[:30]:
        bronnen = ", ".join(f"{b['bron'][:30]} ({b['n']})" for b in a["top_bronnen"][:3])
        md.append(f"| {a['anchor_id']} | {a['po']} | {a['orphan_chunks_count']} | {bronnen} |")
    if len(anchors_rapport) > 30:
        md.append(f"\n_… +{len(anchors_rapport) - 30} meer anchors (zie JSON-rapport)._")
    md.append("")

    OUTPUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"→ {OUTPUT_MD.relative_to(ROOT)}")
    print()
    print(f"HIGH records: {prio_counts['HIGH']}, MEDIUM: {prio_counts['MEDIUM']}, LOW: {prio_counts['LOW']}")
    print(f"Anchors met orphan-chunks: {len(anchors_rapport)}")


if __name__ == "__main__":
    main()
