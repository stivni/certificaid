"""Concept-tree renderer voor schema 2.2.

Leest `data/concepten/concept-tree.json` (gegenereerd uit `docs/granulariteit-skelet.md`
door `tools/extractie/build_concept_tree.py`) en rendert een aanklikbare Quartz-markdown
tree naar `content/concepten/tree.md`.

Iconen per concept_type (uit het record zelf opgehaald):
- 🏛️ kader · ⚙️ verrichting · 📋 procedure · 🔧 instrument
- 📊 balanspost · 🧮 ratio · 📜 regime · ✴️ principe · 👤 actor
- ⏳ virtual (id niet in records)

Tags: K/E/G/R · Σ · ⚠️ uitdovend · 🚫 afgeschaft · 📌 historisch.

Usage:
    python3 -m tools.leermateriaal.render_tree_v22
"""
from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TREE_PATH = REPO / "data" / "concepten" / "concept-tree.json"
RECORDS_DIR = REPO / "data" / "concepten" / "records"
OUT_PATH = REPO / "content" / "concepten" / "tree.md"

TYPE_ICON = {
    "instrument": "🔧",
    "verrichting": "⚙️",
    "procedure": "📋",
    "balanspost": "📊",
    "ratio": "🧮",
    "regime": "📜",
    "kader": "🏛️",
    "principe": "✴️",
    "actor": "👤",
}

GELDIGHEID_SUFFIX = {
    "uitdovend": " ⚠️",
    "afgeschaft": " 🚫",
    "historisch": " 📌hist",
    "ontwerp": " 📌ontwerp",
}


def load_records() -> dict[str, dict]:
    out = {}
    for fp in RECORDS_DIR.glob("*.json"):
        try:
            r = json.loads(fp.read_text())
        except Exception:
            continue
        if (r.get("metadata") or {}).get("schema_version") != "2.2":
            continue
        out[r["id"]] = r
    return out


def label(node: dict, records: dict[str, dict]) -> str:
    """Render één tree-knoop als markdown-item-tekst."""
    nid = node.get("id", "?")
    is_record = node.get("is_record") is True
    rec = records.get(nid) if is_record else None
    naam = (rec.get("naam") or {}).get("primair", nid) if rec else nid

    if is_record:
        icon = TYPE_ICON.get((rec or {}).get("concept_type", ""), "•")
        link = f"[[{nid}|{naam}]]"
    else:
        icon = "⏳"
        link = f"~~{naam}~~"  # strike-through voor virtual

    cats = node.get("categorieen") or []
    cat_str = "/".join(cats)
    cat_part = f" `[{cat_str}]`" if cat_str else ""

    # Σ-flag
    sigma = " Σ" if node.get("is_sigma") else ""
    kand = " ⏳kandidaat" if node.get("is_kandidaat") else ""

    # Geldigheid suffix (uit record)
    geld = ""
    if rec:
        gld = (((rec.get("inhoud") or {}).get("gebruikscontext") or {}).get("geldigheid") or {}).get("status", "")
        geld = GELDIGHEID_SUFFIX.get(gld, "")

    # Annotatie (uit tree-JSON, kort)
    anno = node.get("annotatie") or ""
    anno_part = f" _{anno}_" if anno and not anno.startswith("(bestaand") else ""

    return f"{icon} {link}{cat_part}{sigma}{kand}{geld}{anno_part}"


def render_node(node: dict, records: dict[str, dict], depth: int = 0) -> list[str]:
    lines = [("  " * depth) + f"- {label(node, records)}"]
    for child in node.get("children") or []:
        lines.extend(render_node(child, records, depth + 1))
    return lines


def render_cluster(cluster: dict, records: dict[str, dict], heading_depth: int = 3) -> list[str]:
    raw = cluster.get("naam", "?")
    # Maak human-readable: streepjes → spaties, sentence-case
    naam = raw.replace("-", " ").strip()
    naam = naam[:1].upper() + naam[1:] if naam else raw
    anno = cluster.get("annotatie") or ""
    title = f"{'#' * heading_depth} {naam}"
    if anno:
        title += f" _{anno}_"
    lines = ["", title, ""]
    for node in cluster.get("nodes") or []:
        lines.extend(render_node(node, records, depth=0))
    return lines


def render_discipline_header(disc: dict, records: dict[str, dict]) -> list[str]:
    did = disc.get("id", "?")
    rec = records.get(did)
    naam = (rec.get("naam") or {}).get("primair", did) if rec else did.replace("-", " ").capitalize()
    is_virtual = disc.get("is_virtual") or not disc.get("is_record")
    icon = "⏳" if is_virtual else TYPE_ICON.get((rec or {}).get("concept_type", ""), "🏛️")
    cats = disc.get("categorieen") or []
    cat_part = f" `[{'/'.join(cats)}]`" if cats else ""

    if is_virtual:
        head = f"## {icon} {naam}{cat_part} _(virtual — geen eigen record)_"
    else:
        head = f"## {icon} [[{did}|{naam}]]{cat_part}"
    return [head, ""]


def render_subdiscipline_header(sub: dict, records: dict[str, dict]) -> list[str]:
    sid = sub.get("id", "?")
    rec = records.get(sid)
    naam = (rec.get("naam") or {}).get("primair", sid) if rec else sid.replace("-", " ").capitalize()
    icon = TYPE_ICON.get((rec or {}).get("concept_type", ""), "🏛️")
    cats = sub.get("categorieen") or []
    cat_part = f" `[{'/'.join(cats)}]`" if cats else ""
    if sub.get("is_record"):
        head = f"### {icon} [[{sid}|{naam}]]{cat_part}"
    else:
        head = f"### {icon} {naam}{cat_part} _(virtual)_"
    return [head, ""]


def main() -> int:
    tree = json.loads(TREE_PATH.read_text())
    records = load_records()

    lines = [
        "---",
        'title: "Concept-tree"',
        "tags:",
        "  - concept-index",
        "  - schema-2.2",
        "---",
        "",
        "# Concept-tree",
        "",
        f"Hiërarchische weergave van **{tree.get('disciplines', []) and sum(1 for _ in tree['disciplines'])} disciplines** met alle clusters en records uit `docs/granulariteit-skelet.md`. Gegenereerd: {tree.get('gegenereerd_op','?')}.",
        "",
        "**Iconen** — 🏛️ kader · ⚙️ verrichting · 📋 procedure · 🔧 instrument · 📊 balanspost · 🧮 ratio · 📜 regime · ✴️ principe · 👤 actor · ⏳ virtual (geen record).",
        "**Tags** — K = kader · E = entiteit · G = gebeurtenis · R = regeling.",
        "**Markers** — Σ verzamel-record · ⏳kandidaat nog te ontwikkelen · ⚠️ uitdovend · 🚫 afgeschaft.",
        "",
        "Bekijk ook: [[_index-po|per programmaonderdeel]] · [[_index-type|per type]] · [[_index-categorie|per K/E/G/R-categorie]].",
        "",
        "---",
        "",
    ]

    n_nodes_total = 0
    n_virtual = 0

    def count(node):
        nonlocal n_nodes_total, n_virtual
        n_nodes_total += 1
        if not node.get("is_record"):
            n_virtual += 1
        for c in node.get("children") or []:
            count(c)

    for disc in tree.get("disciplines") or []:
        lines.extend(render_discipline_header(disc, records))
        # Eerst clusters die direct onder discipline hangen
        for cluster in disc.get("clusters") or []:
            lines.extend(render_cluster(cluster, records, heading_depth=3))
            for n in cluster.get("nodes") or []:
                count(n)
        # Dan sub-disciplines
        for sub in disc.get("subdisciplines") or []:
            lines.extend(render_subdiscipline_header(sub, records))
            for cluster in sub.get("clusters") or []:
                lines.extend(render_cluster(cluster, records, heading_depth=4))
                for n in cluster.get("nodes") or []:
                    count(n)

    # Orphan records die niet in tree zitten
    tree_ids = set()
    def collect_ids(node):
        tree_ids.add(node.get("id"))
        for c in node.get("children") or []:
            collect_ids(c)
    for disc in tree.get("disciplines") or []:
        tree_ids.add(disc.get("id"))
        for cl in disc.get("clusters") or []:
            for n in cl.get("nodes") or []:
                collect_ids(n)
        for sub in disc.get("subdisciplines") or []:
            tree_ids.add(sub.get("id"))
            for cl in sub.get("clusters") or []:
                for n in cl.get("nodes") or []:
                    collect_ids(n)
    orphans = sorted(set(records) - tree_ids)
    if orphans:
        lines.extend(["", "---", "", "## Orphan-records _(niet in skelet)_", ""])
        for oid in orphans:
            rec = records[oid]
            naam = (rec.get("naam") or {}).get("primair", oid)
            ctype = rec.get("concept_type", "")
            icon = TYPE_ICON.get(ctype, "•")
            lines.append(f"- {icon} [[{oid}|{naam}]]")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Geschreven: {OUT_PATH} ({len(lines)} lijnen)")
    print(f"Tree-nodes: {n_nodes_total} ({n_virtual} virtual)")
    print(f"Orphan-records: {len(orphans)}")
    if orphans:
        print(f"  → {orphans[:5]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
