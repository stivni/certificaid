"""
Bronnen-index — leesbare summary per bron-MD voor LLM-pipelines en mensen.

Genereert twee artefacten uit dezelfde scan over `resources/bronnen/**/*.md`:

  1. `data/bronnen-index.json`  — machine-readable; gebruikt door scripts
     en LLM-subagenten om reference-mappings te leggen zonder elk frontmatter
     zelf te moeten lezen.
  2. `resources/bronnen/INDEX.md` — mens-leesbare versie: samenvattingstabel
     per type × trust-status, daarna per type alle bronnen gesorteerd op
     trust-status (problemen bovenaan, trusted onderaan).

Eén commando, één bron van waarheid:

    python3 tools/lib/bronnen_index.py --force

Schema per JSON-entry (nieuw schema ADR-004 2026-05-11):

    {
      "bestand": "Antiwitwaswet-2017.md",
      "bron_rol": "wettekst" | "norm" | "advies",
      "titel": "Wet 18 september 2017 ...",
      "korte_naam": "Antiwitwaswet 2017",
      "tags": ["XVII", "4.0"],
      "trust_status": "trusted" | "unreviewed" | "needs-rework" | "rejected",
      "trust_confirmed_by": "human" | "subagent-..." | null,
      "layer1_status": "not_run" | "pass" | "warn" | "fail" | null,
      "layer2_status": "not_run" | "trusted" | "needs-rework" | "rejected" | null,
      "stem": "Antiwitwaswet-2017"
    }

Stale-detectie: vergelijk mtime van index-bestanden met
`max(mtime(resources/bronnen/**/*.md))`. `ensure_fresh()` regenereert beide
bestanden zodra een bron-MD nieuwer is dan een van beide outputs.

Gebruik in andere scripts:

    from tools.lib.bronnen_index import ensure_fresh, load_index
    ensure_fresh()
    idx = load_index()
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent.parent
INDEX_PATH = ROOT / "data" / "bronnen-index.json"
INDEX_MD_PATH = ROOT / "resources" / "bronnen" / "INDEX.md"
BRONNEN_DIRS = {
    "wettekst": ROOT / "resources" / "bronnen" / "wetteksten",
    "norm": ROOT / "resources" / "bronnen" / "normen",
    "advies": ROOT / "resources" / "bronnen" / "adviezen",
}

# Volgorde voor mens-leesbare index: problemen bovenaan, trusted onderaan.
TRUST_ORDER = {
    "rejected": 0,
    "needs-rework": 1,
    "unreviewed": 2,
    "unknown": 3,
    "trusted": 4,
}

# Statussen die we expliciet willen tellen in de samenvattingstabel.
TRUST_COLUMNS = ("trusted", "unreviewed", "needs-rework", "rejected", "unknown")

ROL_LABEL = {
    "wettekst": "Wetteksten",
    "norm": "Normen",
    "advies": "Adviezen",
}


def _korte_naam(stem: str, fm: dict) -> str:
    """Heuristische korte naam voor wetteksten/normen/adviezen.

    Wetteksten gebruiken al beknopte filenames (Antiwitwaswet-2017, WIB92, ...).
    Normen idem (ITAA-norm-aww-geconsolideerd → 'AWW geconsolideerd' niet trivial,
    laat de stem als korte naam staan).
    Adviezen: gebruik nummer uit frontmatter als kort.
    """
    if "nummer" in fm and fm["nummer"]:
        # CBN-advies 2012/10
        return str(fm["nummer"])
    return stem.replace("-", " ").replace("_", " ")


def build_index() -> list[dict]:
    """Loop over alle bron-MDs en bouw een lichte index."""
    entries: list[dict] = []
    for bron_rol, src_dir in BRONNEN_DIRS.items():
        if not src_dir.exists():
            continue
        for path in sorted(src_dir.glob("*.md")):
            if path.name in ("INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"):
                continue
            try:
                post = frontmatter.load(str(path))
            except Exception:
                continue
            fm = post.metadata or {}
            prov = fm.get("provenance") or {}
            trust = prov.get("trust") or {}
            trust_status = trust.get("status") or "unknown"
            # Nieuw schema (ADR-004 2026-05-11): layer1.status en layer2.status.
            # Fallback op "layer2_content" voor bronnen die nog niet gemigreerd zijn.
            layer1 = trust.get("layer1") or {}
            layer2 = trust.get("layer2") or trust.get("layer2_content") or {}
            titel = (
                fm.get("wet")
                or fm.get("norm")
                or fm.get("titel")
                or fm.get("nummer")
                or path.stem
            )
            entry = {
                "bestand": path.name,
                "bron_rol": bron_rol,
                "stem": path.stem,
                "titel": str(titel),
                "korte_naam": _korte_naam(path.stem, fm),
                "tags": list(fm.get("tags") or []),
                "trust_status": trust_status,
                "trust_confirmed_by": trust.get("confirmed_by"),
                # layer1_status: lees .status; fallback op .verdict (pre-migratie bronnen)
                "layer1_status": layer1.get("status") or layer1.get("verdict"),
                # layer2_status: lees .status; fallback op .verdict (pre-migratie bronnen)
                "layer2_status": layer2.get("status") or layer2.get("verdict"),
            }
            entries.append(entry)
    return entries


def _max_bron_mtime() -> float:
    latest = 0.0
    for src_dir in BRONNEN_DIRS.values():
        if not src_dir.exists():
            continue
        for p in src_dir.glob("*.md"):
            if p.name in ("INDEX.md", "README.md"):
                continue
            mt = p.stat().st_mtime
            if mt > latest:
                latest = mt
    return latest


def is_stale() -> bool:
    """Stale als JSON of Markdown ontbreekt, of ouder is dan een bron-MD."""
    if not INDEX_PATH.exists() or not INDEX_MD_PATH.exists():
        return True
    try:
        idx_mtime = min(
            INDEX_PATH.stat().st_mtime, INDEX_MD_PATH.stat().st_mtime
        )
    except OSError:
        return True
    return _max_bron_mtime() > idx_mtime


# ─── Markdown-rendering ──────────────────────────────────────────────────────


def _render_summary_table(entries: list[dict]) -> str:
    """Tabel: rijen = type, kolommen = trust-status, cel = aantal."""
    by_rol: dict[str, Counter] = defaultdict(Counter)
    for e in entries:
        by_rol[e["bron_rol"]][e["trust_status"]] += 1

    header = "| Type | Totaal | " + " | ".join(s.capitalize() for s in TRUST_COLUMNS) + " |"
    sep = "|" + "|".join(["---"] * (2 + len(TRUST_COLUMNS))) + "|"
    rows = [header, sep]

    totals = Counter()
    for rol in ("wettekst", "norm", "advies"):
        cnt = by_rol.get(rol, Counter())
        total = sum(cnt.values())
        totals.update(cnt)
        cells = [str(cnt.get(s, 0)) if cnt.get(s, 0) else "—" for s in TRUST_COLUMNS]
        rows.append(f"| {ROL_LABEL[rol]} | {total} | " + " | ".join(cells) + " |")
    grand = sum(totals.values())
    cells = [str(totals.get(s, 0)) if totals.get(s, 0) else "—" for s in TRUST_COLUMNS]
    rows.append(f"| **Totaal** | **{grand}** | " + " | ".join(cells) + " |")
    return "\n".join(rows)


def _trust_badge(status: str) -> str:
    """Compacte visuele markering per trust-status."""
    return {
        "trusted": "✅ trusted",
        "unreviewed": "◻️ unreviewed",
        "needs-rework": "⚠️ needs-rework",
        "rejected": "❌ rejected",
        "unknown": "❓ unknown",
    }.get(status, status)


def _verdict_short(v: str | None) -> str:
    if not v:
        return "—"
    return v


def _render_rol_table(rol: str, entries: list[dict]) -> str:
    """Tabel per type, gesorteerd op trust-status (problemen bovenaan)."""
    sorted_entries = sorted(
        entries,
        key=lambda e: (
            TRUST_ORDER.get(e["trust_status"], 99),
            e["bestand"].lower(),
        ),
    )
    header = "| Bestand | Trust | L1 | L2 | Confirmed-by | Titel |"
    sep = "|---|---|---|---|---|---|"
    rows = [header, sep]
    for e in sorted_entries:
        titel = e["titel"]
        if len(titel) > 90:
            titel = titel[:87] + "…"
        # Pipes in titel ontsnappen voor markdown-tabel.
        titel = titel.replace("|", r"\|")
        confirmed = e.get("trust_confirmed_by") or "—"
        rows.append(
            f"| `{e['bestand']}` "
            f"| {_trust_badge(e['trust_status'])} "
            f"| {_verdict_short(e.get('layer1_status'))} "
            f"| {_verdict_short(e.get('layer2_status'))} "
            f"| {confirmed} "
            f"| {titel} |"
        )
    return "\n".join(rows)


def render_markdown(entries: list[dict]) -> str:
    """Render volledige `INDEX.md` voor `resources/bronnen/`."""
    by_rol: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_rol[e["bron_rol"]].append(e)

    parts: list[str] = []
    parts.append("# Bronnen-index")
    parts.append("")
    parts.append(
        "Auto-gegenereerd door `tools/lib/bronnen_index.py`. **Niet handmatig "
        "editen** — wijzigingen worden bij de eerstvolgende rebuild overschreven. "
        "Voor de machine-leesbare versie zie `data/bronnen-index.json`."
    )
    parts.append("")
    parts.append(
        "**Trust-statussen** (zie ADR-005 §5): "
        "`trusted` = klaar voor RAG-index; `unreviewed` = nog niet beoordeeld; "
        "`needs-rework` = ETL-fix vereist; `rejected` = bron afgekeurd."
    )
    parts.append("")
    parts.append("## Overzicht")
    parts.append("")
    parts.append(_render_summary_table(entries))
    parts.append("")

    for rol in ("wettekst", "norm", "advies"):
        rol_entries = by_rol.get(rol, [])
        if not rol_entries:
            continue
        parts.append(f"## {ROL_LABEL[rol]} ({len(rol_entries)})")
        parts.append("")
        parts.append(_render_rol_table(rol, rol_entries))
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


# ─── Schrijven ───────────────────────────────────────────────────────────────


def _write_outputs(entries: list[dict]) -> None:
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(
        json.dumps(
            {"n_bronnen": len(entries), "bronnen": entries},
            ensure_ascii=False,
            indent=2,
        )
    )
    INDEX_MD_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_MD_PATH.write_text(render_markdown(entries))


def ensure_fresh(*, verbose: bool = True) -> Path:
    """Regenereer de index (JSON + Markdown) als hij stale is."""
    if is_stale():
        entries = build_index()
        _write_outputs(entries)
        if verbose:
            print(
                f"  bronnen-index ververst: {len(entries)} bronnen → "
                f"{INDEX_PATH.relative_to(ROOT)} + {INDEX_MD_PATH.relative_to(ROOT)}"
            )
    return INDEX_PATH


def load_index() -> list[dict]:
    """Laad de index. Roept ensure_fresh() aan."""
    ensure_fresh()
    data = json.loads(INDEX_PATH.read_text())
    return data["bronnen"]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="forceer rebuild")
    args = parser.parse_args()

    if args.force or is_stale():
        entries = build_index()
        _write_outputs(entries)
        rol_counts = Counter(e["bron_rol"] for e in entries)
        trust_counts = Counter(e["trust_status"] for e in entries)
        print(f"  {len(entries)} bronnen geïndexeerd: {dict(rol_counts)}")
        print(f"  trust-distributie: {dict(trust_counts)}")
        print(f"  → {INDEX_PATH.relative_to(ROOT)}")
        print(f"  → {INDEX_MD_PATH.relative_to(ROOT)}")
    else:
        print(
            f"  bronnen-index up-to-date: "
            f"{INDEX_PATH.relative_to(ROOT)} + {INDEX_MD_PATH.relative_to(ROOT)}"
        )
