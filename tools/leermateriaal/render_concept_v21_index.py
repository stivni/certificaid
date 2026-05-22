"""Genereer content/concepten/index.md — overzicht van alle 396 schema 2.1-records.

Groepering: per concept_type, daarbinnen gevuld eerst, dan stubs (alfabetisch).
"""

from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RECORDS_DIR = REPO / "data" / "concepten" / "records"
OUT = REPO / "content" / "concepten" / "index.md"

TYPE_ORDER = [
    "verrichting",
    "procedure",
    "kader",
    "regime",
    "instrument",
    "balanspost",
    "ratio",
    "methode",
    "principe",
    "actor",
]
TYPE_LABEL = {
    "verrichting": "Verrichtingen",
    "procedure": "Procedures",
    "kader": "Kaders",
    "regime": "Regimes",
    "instrument": "Instrumenten",
    "balanspost": "Balansposten",
    "ratio": "Ratio's",
    "methode": "Methoden",
    "principe": "Principes",
    "actor": "Actoren",
}


def main() -> None:
    records = []
    for f in sorted(RECORDS_DIR.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        ops = (d.get("metadata") or {}).get("operaties_uitgevoerd") or {}
        records.append(
            {
                "id": d["id"],
                "naam": d.get("naam", {}).get("primair", d["id"]),
                "concept_type": d.get("concept_type", "?"),
                "primary_po": (d.get("metadata") or {}).get("primary_po", "?"),
                "is_stub": not (d.get("inhoud") or {}),
                "has_check": "claims_checken" in ops,
                "ops": list(ops.keys()),
            }
        )

    by_type: dict[str, list] = {}
    for r in records:
        by_type.setdefault(r["concept_type"], []).append(r)

    total = len(records)
    filled = sum(1 for r in records if not r["is_stub"])
    checked = sum(1 for r in records if r["has_check"])

    lines = [
        "---",
        'title: "Concepten (schema 2.1)"',
        "tags:",
        "  - catalogus",
        "---",
        "",
        "# Concepten — schema 2.1 (in opbouw)",
        "",
        "Nieuwe didactische conceptlaag, gestuurd door "
        "[`schema 2.1`](https://github.com/stivni/certificaid/blob/main/data/concepten/schema-2.1.schema.json) "
        "(ADR-025 + ADR-029). Bron-JSON in `data/concepten/records/`.",
        "",
        f"**Stand van zaken**: {total} records — {filled} gevuld ({100*filled//total}%), "
        f"{total-filled} stub. Met `claims_checken`: {checked}.",
        "",
        "> [!warning] Render is voor **inspectie**, niet voor studie",
        "> Vrijwel alle claims zijn nog `🤖 verondersteld` (één-pas-extractie). Gebruik niet voor "
        "examenvoorbereiding zolang records geen `claims_checken` doorlopen hebben. Oude schema 2.0-fiches: "
        "[Archief](_archive/).",
        "",
        "## Legenda",
        "",
        "- ✅ = gevuld (heeft `inhoud`)",
        "- 🌱 = stub (alleen metadata)",
        "- 📖 geciteerd · 🔗 afgeleid · 🤖 verondersteld (ai) · 🧠 verondersteld (mens) · ❓ betwijfeld · ❌ weerlegd",
        "",
    ]

    extra_types = [t for t in by_type.keys() if t not in TYPE_ORDER]
    for ctype in TYPE_ORDER + sorted(extra_types):
        items = by_type.get(ctype)
        if not items:
            continue
        n_filled = sum(1 for r in items if not r["is_stub"])
        lines.append(f"## {TYPE_LABEL.get(ctype, ctype.capitalize())} ({n_filled}/{len(items)})")
        lines.append("")
        items_sorted = sorted(items, key=lambda r: (r["is_stub"], r["naam"].lower()))
        for r in items_sorted:
            mark = "🌱" if r["is_stub"] else "✅"
            check = " ✔️" if r["has_check"] else ""
            lines.append(
                f"- {mark}{check} [[{r['id']}|{r['naam']}]] · PO {r['primary_po']}"
            )
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT} ({total} records)")


if __name__ == "__main__":
    main()
