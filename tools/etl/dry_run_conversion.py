"""
Dry-run conversie + heading-level diff voor specifieke bronnen.

Doel: bekijken wat de huidige ETL-chain als output zou produceren voor een bron,
zonder de bestaande output of provenance/trust te overschrijven. Output wordt
weggeschreven naar /tmp/dry-run-conversion/<bron>.md en de heading-level-distributie
wordt vergeleken met de huidige resources/bronnen/<bron>.md.

Gebruik:
  python3 tools/etl/dry_run_conversion.py WER WVV Oud-BW
  python3 tools/etl/dry_run_conversion.py --all-conflicts   # alle 13 outliers
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.etl.convert import (  # noqa: E402
    DEFAULT_CHAINS,
    _DEFAULT_CHAIN_FALLBACK,
    _build_frontmatter_dict,
    _cleanup_steps_for,
    _get_sub_strategy,
    get_handler,
    get_source,
    load_config,
    resolve_method,
)
from tools.etl.transformers import apply_chain  # noqa: E402

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)

CONFLICT_BRONNEN = [
    "WER", "WVV", "Oud-BW", "Strafwetboek-1867", "KB-WVV-2019",
    "Wet-verzekeringen-2014", "Decr-Waals-Directe-Belastingen",
    "MIGB-Vlaanderen", "Wet-beroepskwalificaties-2008",
    "EU-AVG-Verordening-2016-679", "EU-Richtlijn-fusie-2009-133",
    "MIGB-Brussel", "MIGB-Wallonie",
]


def heading_distribution(body: str) -> dict[int, Counter]:
    """Per level → Counter van eerste-woord types."""
    dist: dict[int, Counter] = defaultdict(Counter)
    for m in HEADING_RE.finditer(body):
        lvl = len(m.group(1))
        text = m.group(2).strip()
        head_word = text.split()[0] if text else "(empty)"
        # Normalize Art.-varianten
        if re.match(r"^Art\.\s*\d", text):
            head_word = "Art."
        elif re.match(r"^Artikel\s+\d", text):
            head_word = "Artikel"
        elif re.match(r"^Klasse\s+\d", text):
            head_word = "Klasse"
        dist[lvl][head_word.upper().rstrip(".")] += 1
    return dist


def format_dist(dist: dict[int, Counter]) -> str:
    lines = []
    for lvl in sorted(dist):
        top = sorted(dist[lvl].items(), key=lambda x: -x[1])[:6]
        s = ", ".join(f"{t}×{n}" for t, n in top)
        total = sum(dist[lvl].values())
        lines.append(f"    L{lvl}: total={total:>5}  {s}")
    return "\n".join(lines) if lines else "    (geen headings)"


def run_dry_conversion(source_name: str, out_dir: Path) -> dict:
    config = load_config()
    cfg = get_source(source_name, config)
    method = resolve_method(cfg)
    handler = get_handler(method)
    if handler is None:
        return {"source": source_name, "error": f"geen handler voor {method}"}

    # 1. Extract
    extracted = handler(cfg, source_name)
    if isinstance(extracted, dict):
        return {"source": source_name, "error": "compilatie-mode niet ondersteund in dit dry-run script"}

    # 2. Chain
    params_extract = (cfg.get("extract") or {}).get("params") or {}
    if method == "pdftotext_ejustice" and params_extract.get("simple_mode"):
        chain = ["cleanup_basics", "emit_frontmatter"]
    else:
        chain = DEFAULT_CHAINS.get(method, _DEFAULT_CHAIN_FALLBACK)

    fm = _build_frontmatter_dict(cfg, source_name, method)
    fm["_cleanup_steps"] = _cleanup_steps_for(cfg, method)
    fm["_sub_strategy"] = _get_sub_strategy(cfg)

    text, _ = apply_chain(extracted, fm, chain)

    out_path = out_dir / f"{source_name}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")

    return {"source": source_name, "method": method, "output": out_path,
            "n_chars": len(text)}


def compare_one(source_name: str, dry_path: Path) -> None:
    current = ROOT / "resources" / "bronnen" / "wetteksten" / f"{source_name}.md"
    if not current.exists():
        print(f"\n=== {source_name}: GEEN bestaande versie om te vergelijken ===")
        return
    current_body = current.read_text()
    dry_body = dry_path.read_text()

    print(f"\n=== {source_name} ===")
    print(f"  Bestaand: {current.relative_to(ROOT)} ({len(current_body):,} chars)")
    print(f"  Dry-run:  {dry_path.relative_to(dry_path.parent.parent)} ({len(dry_body):,} chars)")

    cur_dist = heading_distribution(current_body)
    dry_dist = heading_distribution(dry_body)

    print("  HUIDIGE heading-distributie:")
    print(format_dist(cur_dist))
    print("  DRY-RUN heading-distributie:")
    print(format_dist(dry_dist))

    # Check conflict: level met both article + structural in dry-run
    article_types = {"ART", "ARTIKEL", "KLASSE", "PAR"}
    structural_types = {"BOEK", "DEEL", "TITEL", "HOOFDSTUK", "AFDELING",
                        "ONDERAFDELING", "SECTIE", "ONDERDEEL", "PARAGRAAF"}
    conflicts_dry = []
    for lvl, types in dry_dist.items():
        has_art = any(t in article_types for t in types)
        has_str = any(t in structural_types for t in types)
        if has_art and has_str:
            conflicts_dry.append(lvl)
    if conflicts_dry:
        print(f"  ⚠️  Conflict in dry-run op level(s): {conflicts_dry}")
    else:
        print("  ✓ Geen heading-conflict in dry-run output")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("sources", nargs="*", help="Specifieke bron-namen om te converteren")
    p.add_argument("--all-conflicts", action="store_true",
                   help=f"Run alle 13 conflict-bronnen: {CONFLICT_BRONNEN}")
    p.add_argument("--out-dir", default="/tmp/dry-run-conversion",
                   help="Output directory (default: /tmp/dry-run-conversion)")
    args = p.parse_args()

    if args.all_conflicts:
        sources = CONFLICT_BRONNEN
    elif args.sources:
        sources = args.sources
    else:
        p.error("Geef minstens één bron op, of gebruik --all-conflicts")

    out_dir = Path(args.out_dir)
    print(f"→ Output naar: {out_dir}")
    print(f"→ Bronnen:     {sources}")

    results = []
    for s in sources:
        try:
            r = run_dry_conversion(s, out_dir)
            results.append(r)
            if "error" in r:
                print(f"\n[SKIP] {s}: {r['error']}")
            else:
                print(f"\n[OK]   {s} → {r['output']} ({r['n_chars']:,} chars)")
        except Exception as e:
            print(f"\n[FAIL] {s}: {e}")
            results.append({"source": s, "error": str(e)})

    print("\n" + "=" * 70)
    print("  HEADING-LEVEL VERGELIJKING")
    print("=" * 70)
    for r in results:
        if "output" in r:
            compare_one(r["source"], r["output"])


if __name__ == "__main__":
    main()
