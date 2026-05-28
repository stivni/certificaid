"""Index-pagina-generator voor schema 2.2-fiches.

Genereert:
- `content/concepten/_index-po.md` — fiches gegroepeerd per PO (op basis van ankers)
- `content/concepten/_index-type.md` — fiches gegroepeerd per concept_type
- `content/concepten/_index-categorie.md` — fiches gegroepeerd per K/E/G/R-categorie
- `content/concepten/_index.md` — landing met links naar bovenstaande + zoek-tips

Usage:
    python3 -m tools.leermateriaal.render_index_v22
"""
from __future__ import annotations

import collections
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RECORDS_DIR = REPO / "data" / "concepten" / "records"
OUT_DIR = REPO / "content" / "concepten"
ANCHORS_PATH = REPO / "data" / "programma" / "anchors.json"

CONCEPT_TYPE_ICON = {
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

CATEGORIE_ICON = {
    "kader": "🏛️",
    "entiteit": "🏢",
    "gebeurtenis": "📅",
    "regeling": "📋",
}


def load_records() -> list[dict]:
    out = []
    for fp in sorted(RECORDS_DIR.glob("*.json")):
        try:
            r = json.loads(fp.read_text())
        except Exception:
            continue
        if (r.get("metadata") or {}).get("schema_version") != "2.2":
            continue
        out.append(r)
    return out


def load_po_titles() -> dict[str, str]:
    a = json.loads(ANCHORS_PATH.read_text())
    titles = {}
    for an in a.get("anchors") or []:
        po = an.get("po")
        po_titel = an.get("po_titel")
        if po and po_titel and po not in titles:
            titles[po] = po_titel
    return titles


def primary_po(record: dict) -> str | None:
    """Eerste PO-prefix uit anchors (bv. '2.4.III' → '2.4')."""
    ankers = (record.get("metadata") or {}).get("ankers") or []
    for a in ankers:
        # PO-pattern: X.Y of X.Y.Z[.W]
        parts = a.split(".")
        if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
            return f"{parts[0]}.{parts[1]}"
    return None


def fiche_link(rec: dict) -> str:
    naam = (rec.get("naam") or {}).get("primair", rec["id"])
    ctype = rec.get("concept_type", "")
    icon = CONCEPT_TYPE_ICON.get(ctype, "•")
    return f"- {icon} [[{rec['id']}|{naam}]]"


def render_po_index(records: list[dict], po_titles: dict[str, str]) -> str:
    by_po: dict[str, list] = collections.defaultdict(list)
    geen_po = []
    for r in records:
        po = primary_po(r)
        if po:
            by_po[po].append(r)
        else:
            geen_po.append(r)

    lines = [
        "---",
        'title: "Concepten — per programmaonderdeel"',
        "tags:",
        "  - concept-index",
        "  - schema-2.2",
        "---",
        "",
        "# Concepten per programmaonderdeel",
        "",
        f"_359 schema-2.2 concept-fiches, gegroepeerd op primaire PO uit de ankers._",
        "",
    ]
    for po in sorted(by_po.keys(), key=lambda x: tuple(int(p) for p in x.split('.'))):
        titel = po_titles.get(po, "")
        lines.append(f"## PO {po} — {titel}  ({len(by_po[po])} fiches)")
        lines.append("")
        for r in sorted(by_po[po], key=lambda x: (x.get("naam") or {}).get("primair", x["id"]).lower()):
            lines.append(fiche_link(r))
        lines.append("")
    if geen_po:
        lines.append(f"## Zonder PO-anker  ({len(geen_po)} fiches)")
        lines.append("")
        for r in sorted(geen_po, key=lambda x: (x.get("naam") or {}).get("primair", x["id"]).lower()):
            lines.append(fiche_link(r))
        lines.append("")
    return "\n".join(lines) + "\n"


def render_type_index(records: list[dict]) -> str:
    by_type: dict[str, list] = collections.defaultdict(list)
    for r in records:
        by_type[r.get("concept_type", "onbekend")].append(r)

    lines = [
        "---",
        'title: "Concepten — per type"',
        "tags:",
        "  - concept-index",
        "  - schema-2.2",
        "---",
        "",
        "# Concepten per concept-type",
        "",
        "_Schema 2.2 kent 9 concept-types. Klik door per categorie._",
        "",
    ]
    for ctype in sorted(by_type.keys()):
        icon = CONCEPT_TYPE_ICON.get(ctype, "•")
        lines.append(f"## {icon} {ctype}  ({len(by_type[ctype])} fiches)")
        lines.append("")
        for r in sorted(by_type[ctype], key=lambda x: (x.get("naam") or {}).get("primair", x["id"]).lower()):
            lines.append(fiche_link(r))
        lines.append("")
    return "\n".join(lines) + "\n"


def render_categorie_index(records: list[dict]) -> str:
    by_cat: dict[str, list] = collections.defaultdict(list)
    for r in records:
        cats = (r.get("metadata") or {}).get("categorieen") or ["onbekend"]
        for c in cats:
            by_cat[c].append(r)

    lines = [
        "---",
        'title: "Concepten — per K/E/G/R-categorie"',
        "tags:",
        "  - concept-index",
        "  - schema-2.2",
        "---",
        "",
        "# Concepten per K/E/G/R-categorie",
        "",
        "_Vier super-categorieën: **kader** (wettelijk kader), **entiteit** (object/instrument), **gebeurtenis** (verrichting/procedure), **regeling** (regime/voordeel/uitzondering)._",
        "",
    ]
    for cat in ["kader", "entiteit", "gebeurtenis", "regeling", "onbekend"]:
        if cat not in by_cat:
            continue
        icon = CATEGORIE_ICON.get(cat, "•")
        lines.append(f"## {icon} {cat}  ({len(by_cat[cat])} fiches)")
        lines.append("")
        for r in sorted(by_cat[cat], key=lambda x: (x.get("naam") or {}).get("primair", x["id"]).lower()):
            lines.append(fiche_link(r))
        lines.append("")
    return "\n".join(lines) + "\n"


def render_landing(records: list[dict]) -> str:
    return f"""---
title: "Concepten — overzicht"
tags:
  - concept-index
  - schema-2.2
---

# Concepten — overzicht

**{len(records)} concept-fiches** in schema 2.2 voor het ITAA-bekwaamheidsexamen Gecertificeerd Accountant.

## Navigatie

- [[_index-po|📚 Per programmaonderdeel (PO)]] — best startpunt om PO-gericht te studeren
- [[_index-type|🔖 Per concept-type]] — instrument · verrichting · procedure · balanspost · ratio · regime · kader · principe · actor
- [[_index-categorie|🗂 Per K/E/G/R-categorie]] — kader · entiteit · gebeurtenis · regeling

## Confidence-iconen

Elke claim toont:
- 📖 **geciteerd** — directe verwijzing naar primaire bron (wettekst/KB/CBN/IFRS)
- 🔗 **afgeleid** — synthese uit meerdere bronnen + logica
- 🤖 **verondersteld** — eigen redenering zonder primaire bron (verifieer)
- ❓ **betwijfeld** — bron-conflict, verdere check nodig
- ❌ **weerlegd** — verkeerd gebleken

## Bouwsteen-types

Schema 2.2 onderscheidt 11 platte bouwsteen-types:
- 💡 begrip · 👣 stap · 📏 drempel · 📜 regel · ↪️ uitzondering
- 🧭 vuistregel · ⚙️ mechanisme · ⚠️ risico · 🧮 formule
- ✴️ principe · 🚧 beperking

## Status-banners

- 📝 **Concept** — content uit één extract-pass; niet door verify-pass
- 🌱 **Skeleton** — alleen structuur, geen content (intermediair)

## Geldigheid-banners (voor regelingen/regimes)

- (in-voege) — geen banner: nog actueel
- ⚠️ uitdovend — wordt afgebouwd
- 🚫 afgeschaft — niet meer van toepassing
- 📌 historisch — alleen relevant voor oude dossiers
- 📌 ontwerp — wet/regelgeving nog niet in voege
"""


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    records = load_records()
    print(f"Geladen: {len(records)} schema-2.2 records")
    po_titles = load_po_titles()
    print(f"PO-titels: {len(po_titles)}")

    (OUT_DIR / "index.md").write_text(render_landing(records), encoding="utf-8")
    (OUT_DIR / "_index-po.md").write_text(render_po_index(records, po_titles), encoding="utf-8")
    (OUT_DIR / "_index-type.md").write_text(render_type_index(records), encoding="utf-8")
    (OUT_DIR / "_index-categorie.md").write_text(render_categorie_index(records), encoding="utf-8")

    print(f"Geschreven naar {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
