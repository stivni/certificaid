"""
Bronnen-index — leesbare summary per bron-MD voor LLM-pipelines.

`data/bronnen-index.json` is een lichte index van alle bron-MDs
(`resources/bronnen/{wetteksten,normen,adviezen}/*.md`) met de velden die een
LLM-subagent nodig heeft om reference-mappings te leggen (zonder 571 frontmatters
zelf te moeten lezen).

Schema per entry:

    {
      "bestand": "Antiwitwaswet-2017.md",
      "bron_rol": "wettekst",
      "titel": "Wet 18 september 2017 tot voorkoming van het witwassen...",
      "korte_naam": "Antiwitwaswet 2017",       # voor wetteksten
      "tags": ["XVII", "4.0"],
      "trust_status": "trusted",
      "stem": "Antiwitwaswet-2017"               # zonder .md, voor chunk-id-prefix
    }

Stale-detectie: vergelijk `mtime(bronnen-index.json)` met
`max(mtime(resources/bronnen/**/*.md))`. Index is stale als een bron-MD nieuwer
is. `ensure_fresh()` regenereert in dat geval — automatisch en transparant.

Gebruik in andere scripts:

    from tools.lib.bronnen_index import ensure_fresh, load_index
    ensure_fresh()
    idx = load_index()
"""

from __future__ import annotations

import json
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent.parent
INDEX_PATH = ROOT / "data" / "bronnen-index.json"
BRONNEN_DIRS = {
    "wettekst": ROOT / "resources" / "bronnen" / "wetteksten",
    "norm": ROOT / "resources" / "bronnen" / "normen",
    "advies": ROOT / "resources" / "bronnen" / "adviezen",
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
            if path.name in ("INDEX.md", "README.md"):
                continue
            try:
                post = frontmatter.load(str(path))
            except Exception:
                continue
            fm = post.metadata or {}
            trust_status = (
                (fm.get("provenance") or {}).get("trust", {}).get("status", "unknown")
            )
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
            }
            entries.append(entry)
    return entries


def _max_bron_mtime() -> float:
    latest = 0.0
    for src_dir in BRONNEN_DIRS.values():
        if not src_dir.exists():
            continue
        for p in src_dir.glob("*.md"):
            mt = p.stat().st_mtime
            if mt > latest:
                latest = mt
    return latest


def is_stale() -> bool:
    """Index is stale als hij niet bestaat, leeg is, of ouder dan een bron-MD."""
    if not INDEX_PATH.exists():
        return True
    try:
        idx_mtime = INDEX_PATH.stat().st_mtime
    except OSError:
        return True
    return _max_bron_mtime() > idx_mtime


def ensure_fresh(*, verbose: bool = True) -> Path:
    """Regenereer de index als hij stale is. Returnt het pad naar index."""
    if is_stale():
        entries = build_index()
        INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
        INDEX_PATH.write_text(json.dumps({
            "n_bronnen": len(entries),
            "bronnen": entries,
        }, ensure_ascii=False, indent=2))
        if verbose:
            print(f"  bronnen-index ververst: {len(entries)} bronnen → {INDEX_PATH.relative_to(ROOT)}")
    return INDEX_PATH


def load_index() -> list[dict]:
    """Laad de index. Roept ensure_fresh() aan."""
    ensure_fresh()
    data = json.loads(INDEX_PATH.read_text())
    return data["bronnen"]


if __name__ == "__main__":
    # CLI: forceer rebuild
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="forceer rebuild")
    args = parser.parse_args()

    if args.force or is_stale():
        entries = build_index()
        INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
        INDEX_PATH.write_text(json.dumps({
            "n_bronnen": len(entries),
            "bronnen": entries,
        }, ensure_ascii=False, indent=2))
        from collections import Counter
        rol_counts = Counter(e["bron_rol"] for e in entries)
        trust_counts = Counter(e["trust_status"] for e in entries)
        print(f"  {len(entries)} bronnen geïndexeerd: {dict(rol_counts)}")
        print(f"  trust-distributie: {dict(trust_counts)}")
        print(f"  → {INDEX_PATH.relative_to(ROOT)}")
    else:
        print(f"  bronnen-index up-to-date: {INDEX_PATH.relative_to(ROOT)}")
