"""
Structuur-audit van bron-MDs — basis voor level-driven chunking.

Doel: per bron in kaart brengen welke heading-types op welk niveau voorkomen,
zodat we kunnen besluiten welk level de chunk-grens hoort te zijn én welke
bronnen ETL-werk nodig hebben.

Wat het script per bron rapporteert:
  - Headings-distributie: voor elk (level, categorie) een count
    * categorie: "structural" (BOEK/TITEL/HOOFDSTUK/...) | "article" (Art./Par./Artikel/Klasse)
                 | "other" (heading die geen van beide matcht)
  - Conflicten: levels waarop zowel structural als article headings staan
    → die bron heeft ETL-werk nodig om level-driven chunking deterministisch te maken
  - Aanbevolen chunk-level: hoogste level waar voornamelijk article-headings staan

Wat het globaal samenvat:
  - Aantal bronnen met conflict
  - Histogrammen van "aanbevolen chunk-level" per bron-rol
  - Bronnen zonder enige article-heading (vereisen volledige ETL-injection)

Gebruik:
  python3 tools/rag/rag_structure_audit.py                       # alle trusted bronnen
  python3 tools/rag/rag_structure_audit.py --bron-rol wettekst   # filter
  python3 tools/rag/rag_structure_audit.py --include-unreviewed
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.rag.rag_index import (  # noqa: E402
    BRON_DIRS,
    HEADING_RE,
    STRUCTURAL_PREFIX_RE,
    _apply_trust_filter,
    parse_heading,
)

QA_DIR = ROOT / "data" / "qa"

# Headings die we niet als "echt" willen tellen (titelpagina-noise, intro)
ANY_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def categorize_heading(line: str) -> dict | None:
    """Categoriseer één heading-regel.

    Returnt {level, type, category, naam, raw} of None als het geen heading is.
    category ∈ {"structural", "article", "other"}.
    """
    m = ANY_HEADING_RE.match(line.rstrip())
    if not m:
        return None
    level = len(m.group(1))
    text = m.group(2).strip()

    # Probeer eerst de bestaande HEADING_RE (matcht structural + article types)
    parsed = parse_heading(line)
    if parsed is not None:
        category = "article" if parsed["is_article"] else "structural"
        return {
            "level": parsed["level"],
            "type": parsed["type"],
            "category": category,
            "naam": parsed["naam"],
            "raw": line.strip(),
        }

    # Headings die niet matchen: alles wat niet met een herkenbaar type begint
    # (bv. "## Overwegingen", "# Wet ...", "## Inwerkingtreding")
    # Speciale gevallen om af te splitsen
    head_word = text.split()[0] if text else ""
    if STRUCTURAL_PREFIX_RE.match(text):
        # Structureel-type met onverwacht nummer-format (bv. "TITEL I bis")
        return {"level": level, "type": head_word.upper().rstrip("."),
                "category": "structural", "naam": text, "raw": line.strip()}
    return {"level": level, "type": "(plain)", "category": "other",
            "naam": text[:60], "raw": line.strip()}


def audit_bron(path: Path, rol: str) -> dict:
    try:
        post = frontmatter.load(str(path))
    except Exception as e:
        return {"bestand": path.name, "rol": rol, "error": str(e)}

    fm = post.metadata
    body = post.content

    # Frontmatter chunk-config (huidige waarde)
    chunk_fm = fm.get("chunk") or {}
    fm_level = chunk_fm.get("level")
    fm_type = chunk_fm.get("type")

    # Per (level, type) tellen
    level_types: dict[int, Counter] = defaultdict(Counter)
    level_categories: dict[int, Counter] = defaultdict(Counter)
    sample_per_level: dict[int, list[str]] = defaultdict(list)

    for line in body.split("\n"):
        cat = categorize_heading(line)
        if cat is None:
            continue
        lvl = cat["level"]
        level_types[lvl][cat["type"]] += 1
        level_categories[lvl][cat["category"]] += 1
        if len(sample_per_level[lvl]) < 2:
            sample_per_level[lvl].append(cat["raw"])

    # Conflict-detectie: levels waar zowel article als structural voorkomt
    conflicts = [lvl for lvl, cats in level_categories.items()
                 if cats.get("article", 0) > 0 and cats.get("structural", 0) > 0]

    # Aanbevolen chunk-level = laagste level waarop article-headings staan
    article_levels = sorted(
        (lvl for lvl, cats in level_categories.items() if cats.get("article", 0) > 0),
    )
    aanbevolen_level = article_levels[0] if article_levels else None
    aanbevolen_type = None
    if aanbevolen_level is not None:
        types_at_level = level_types[aanbevolen_level]
        # Kies het meest voorkomende article-type op dat level
        article_types_only = Counter()
        for line in body.split("\n"):
            cat = categorize_heading(line)
            if cat and cat["level"] == aanbevolen_level and cat["category"] == "article":
                article_types_only[cat["type"]] += 1
        if article_types_only:
            aanbevolen_type = article_types_only.most_common(1)[0][0]

    # Total counts
    total_article = sum(c.get("article", 0) for c in level_categories.values())
    total_structural = sum(c.get("structural", 0) for c in level_categories.values())
    total_other = sum(c.get("other", 0) for c in level_categories.values())

    return {
        "bestand": path.name,
        "rol": rol,
        "fm_chunk_level": fm_level,
        "fm_chunk_type": fm_type,
        "level_distribution": {
            str(lvl): {
                "types": dict(level_types[lvl]),
                "categories": dict(level_categories[lvl]),
                "sample": sample_per_level[lvl],
            }
            for lvl in sorted(level_categories)
        },
        "conflicts": conflicts,
        "n_article": total_article,
        "n_structural": total_structural,
        "n_other": total_other,
        "aanbevolen_chunk_level": aanbevolen_level,
        "aanbevolen_chunk_type": aanbevolen_type,
    }


# ---------------------------------------------------------------------------
# Rapport
# ---------------------------------------------------------------------------

def _format_level_row(lvl: int, info: dict) -> str:
    types = info["types"]
    cats = info["categories"]
    type_str = ", ".join(f"{t}×{n}" for t, n in sorted(types.items(), key=lambda x: -x[1])[:5])
    cat_str = "+".join(f"{k}={v}" for k, v in sorted(cats.items()))
    return f"      L{lvl}: {cat_str:30}  types: {type_str}"


def render_bron(r: dict) -> str:
    if "error" in r:
        return f"  {r['bestand']}: ERROR {r['error']}"
    lines = [f"  {r['bestand']}  (FM: level={r['fm_chunk_level']}, type={r['fm_chunk_type']!r})"]
    for lvl, info in r["level_distribution"].items():
        lines.append(_format_level_row(int(lvl), info))
    if r["conflicts"]:
        lines.append(f"      ⚠️  CONFLICT op level(s) {r['conflicts']} (zowel structural als article)")
    if r["aanbevolen_chunk_level"] is None:
        lines.append("      ⛔ Geen article-headings gevonden — ETL-injection vereist")
    else:
        lines.append(f"      → Aanbevolen: chunk.level={r['aanbevolen_chunk_level']}, "
                     f"chunk.type={r['aanbevolen_chunk_type']!r}")
    return "\n".join(lines)


def render_summary(results: list[dict]) -> str:
    valid = [r for r in results if "error" not in r]
    by_rol: dict[str, list[dict]] = defaultdict(list)
    for r in valid:
        by_rol[r["rol"]].append(r)

    out = ["", "=" * 70, "  STRUCTUUR-AUDIT — samenvatting", "=" * 70]

    for rol, items in sorted(by_rol.items()):
        n = len(items)
        n_conflict = sum(1 for r in items if r["conflicts"])
        n_no_article = sum(1 for r in items if r["aanbevolen_chunk_level"] is None)
        level_hist = Counter(r["aanbevolen_chunk_level"] for r in items
                             if r["aanbevolen_chunk_level"] is not None)
        type_hist = Counter(r["aanbevolen_chunk_type"] for r in items
                            if r["aanbevolen_chunk_type"] is not None)
        fm_consistent = sum(1 for r in items
                            if r["fm_chunk_level"] == r["aanbevolen_chunk_level"]
                            and r["fm_chunk_level"] is not None)

        out.append(f"\n=== {rol.upper()} — {n} bronnen ===")
        out.append(f"  Conflicten (structural+article op zelfde level): {n_conflict}")
        out.append(f"  Geen article-headings (ETL-injection nodig):     {n_no_article}")
        out.append(f"  Frontmatter chunk.level klopt met data:          {fm_consistent}/{n}")
        out.append("  Aanbevolen chunk-level verdeling:")
        for lvl in sorted(level_hist):
            out.append(f"    L{lvl}: {level_hist[lvl]} bronnen")
        out.append("  Aanbevolen chunk-type verdeling:")
        for t, c in type_hist.most_common():
            out.append(f"    {t!r:12}: {c} bronnen")

    return "\n".join(out)


def render_outliers(results: list[dict]) -> str:
    valid = [r for r in results if "error" not in r]
    out = ["", "=" * 70, "  OUTLIERS — ETL-werk vereist", "=" * 70]

    conflicts = [r for r in valid if r["conflicts"]]
    no_article = [r for r in valid if r["aanbevolen_chunk_level"] is None]
    mismatch = [r for r in valid
                if r["fm_chunk_level"] is not None
                and r["aanbevolen_chunk_level"] is not None
                and r["fm_chunk_level"] != r["aanbevolen_chunk_level"]]

    if conflicts:
        out.append(f"\n🟡 CONFLICT — structural én article op zelfde level ({len(conflicts)} bronnen)")
        out.append("   ETL-fix: structureel-type promoveren naar hoger level (of article degraderen)")
        for r in conflicts:
            out.append(f"   • {r['bestand']:<55} conflict op level(s) {r['conflicts']}")

    if no_article:
        out.append(f"\n🔴 GEEN article-headings — kan niet logisch chunken ({len(no_article)} bronnen)")
        out.append("   ETL-fix: heading-injection (zoals MAR-vzw / MAR-ondernemingen) vereist")
        for r in no_article:
            sample = next(iter(r["level_distribution"].items()), None)
            sample_str = f" — eerste heading: {sample[1]['sample'][0]!r}" if sample else ""
            out.append(f"   • {r['bestand']}{sample_str}")

    if mismatch:
        out.append(f"\n🟢 FRONTMATTER-MISMATCH — chunk.level klopt niet ({len(mismatch)} bronnen)")
        out.append("   Fix: frontmatter chunk.level bijwerken naar aanbevolen waarde")
        for r in mismatch:
            out.append(
                f"   • {r['bestand']:<55} fm.level={r['fm_chunk_level']}  →  aanbevolen={r['aanbevolen_chunk_level']}  ({r['aanbevolen_chunk_type']!r})"
            )

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--bron-rol", choices=["wettekst", "norm", "advies"],
                   help="Audit alleen deze bron-rol (default: alle drie)")
    p.add_argument("--include-unreviewed", action="store_true",
                   help="Ook bronnen met trust.status != trusted")
    p.add_argument("--verbose", action="store_true",
                   help="Print per-bron details (anders alleen outliers + summary)")
    args = p.parse_args()

    rollen = [args.bron_rol] if args.bron_rol else ["wettekst", "norm", "advies"]
    results: list[dict] = []

    for rol in rollen:
        src = BRON_DIRS[rol]
        files = sorted(src.glob("*.md"))
        files = [f for f in files if "INDEX" not in f.name]
        files, skipped, _ = _apply_trust_filter(files, include_unreviewed=args.include_unreviewed)
        if skipped:
            parts = ", ".join(f"{k}: {v}" for k, v in sorted(skipped.items()))
            print(f"\n→ {rol}: {len(files)} bronnen geaudit, {sum(skipped.values())} geskipt ({parts})")
        else:
            print(f"\n→ {rol}: {len(files)} bronnen geaudit")
        for f in files:
            results.append(audit_bron(f, rol))

    print(render_summary(results))
    print(render_outliers(results))

    if args.verbose:
        print("\n" + "=" * 70)
        print("  PER-BRON DETAIL")
        print("=" * 70)
        for r in results:
            print()
            print(render_bron(r))

    # JSON-rapport
    QA_DIR.mkdir(parents=True, exist_ok=True)
    ts = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_path = QA_DIR / f"structure-audit-{ts}.json"
    out_path.write_text(json.dumps({
        "timestamp": ts,
        "include_unreviewed": args.include_unreviewed,
        "bronnen": results,
    }, indent=2, ensure_ascii=False))
    print(f"\n→ JSON-rapport: {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
