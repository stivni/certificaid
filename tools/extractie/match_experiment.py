"""Matching-experiment: evalueer verschillende bundling-strategieën op de gold-set.

Doel: bepalen welke matching-strategie (threshold, margin, knee, etc.) de beste
recall@gold + precision oplevert. Werkwijze:

  1. Laad anchors + chunks + gold-set
  2. Bereken cosine-matrix éénmalig
  3. Voor elke strategie: bundle per anchor → tel hoeveel gold-bron-stems
     in de bundle zitten (bron-niveau, niet chunk-niveau)
  4. Rapporteer recall + bundle-grootte-stats per strategie

Recall-definitie: voor een anchor in de gold-set met expected bron-stems
`{X, Y, Z}`: recall = | bundle_bron_stems ∩ expected | / | expected |.
Een bron-stem zit in `bundle_bron_stems` als minstens één chunk van die bron
in de bundle staat.

Precision-proxy: gemiddelde bundle-grootte (lager = preciezer mits recall hoog).

Gebruik:
  python3 -m tools.extractie.match_experiment

Output: console-tabel + data/etl/qa/matching-experiment-<ts>.json
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from tools.extractie.match_bronnen import (
    cosine_matrix,
    find_knee,
    load_anchors,
    load_chunks,
)

ROOT = Path(__file__).resolve().parent.parent.parent
GOLD_PATH = ROOT / "tools" / "extractie" / "gold" / "matching-gold-set.json"
OUT_DIR = ROOT / "data" / "qa"


def bron_stem(bestand: str) -> str:
    """`X.md` → `X` (gebruikt voor gold-set vergelijking)."""
    return bestand[:-3] if bestand.endswith(".md") else bestand


def evaluate_strategy(
    name: str,
    anchors: list[dict],
    anchor_vecs: np.ndarray,
    chunk_ids: list[str],
    chunk_vecs: np.ndarray,
    chunk_metas: list[dict],
    sim: np.ndarray,
    bundle_fn,  # (scores_desc, ranked_idx) → bundle_idx
    gold: list[dict],
) -> dict:
    """Evalueer één strategie tegen de gold-set."""
    # Per anchor: bouw bundle
    anchor_id_to_bundle: dict[str, list[int]] = {}
    bundle_sizes = []
    for i, a in enumerate(anchors):
        scores = sim[i, :]
        ranked_idx = np.argsort(-scores)
        scores_desc = scores[ranked_idx]
        bundle_idx = bundle_fn(scores_desc, ranked_idx)
        anchor_id_to_bundle[a["anchor_id"]] = bundle_idx
        bundle_sizes.append(len(bundle_idx))

    # Evalueer recall op gold
    per_anchor_recall = []
    per_anchor_detail = []
    for g in gold:
        aid = g["anchor_id"]
        expected = set(g["must_match"])
        bundle_idx = anchor_id_to_bundle.get(aid, [])
        bundle_brons = {bron_stem(chunk_metas[j].get("bestand", "")) for j in bundle_idx}
        hits = expected & bundle_brons
        misses = expected - bundle_brons
        recall = len(hits) / max(len(expected), 1)
        per_anchor_recall.append(recall)
        per_anchor_detail.append({
            "anchor_id": aid,
            "expected": sorted(expected),
            "hit": sorted(hits),
            "miss": sorted(misses),
            "bundle_size": len(bundle_idx),
            "recall": round(recall, 3),
        })

    return {
        "strategy": name,
        "mean_recall": round(float(np.mean(per_anchor_recall)), 3),
        "min_recall": round(float(np.min(per_anchor_recall)), 3),
        "n_perfect": sum(1 for r in per_anchor_recall if r == 1.0),
        "median_bundle_size": int(np.median(bundle_sizes)),
        "max_bundle_size": int(np.max(bundle_sizes)),
        "n_uncovered_anchors": sum(1 for s in bundle_sizes if s == 0),
        "per_anchor": per_anchor_detail,
    }


def main() -> None:
    print("[gold] laden...")
    gold = json.loads(GOLD_PATH.read_text())["gold"]
    print(f"  {len(gold)} anchor-paren in gold-set")

    print("[anchors] laden...")
    anchors, anchor_vecs = load_anchors()
    print(f"  {len(anchors)} anchors, dim={anchor_vecs.shape[1]}")

    print("[chunks] laden uit ChromaDB...")
    chunk_ids, chunk_vecs, chunk_metas = load_chunks()
    print(f"  {len(chunk_ids)} chunks")

    print("[match] cosine-matrix berekenen...")
    sim = cosine_matrix(anchor_vecs, chunk_vecs)
    print(f"  matrix shape: {sim.shape}")

    # Definieer strategieën
    def margin_strategy(threshold, margin):
        def f(scores_desc, ranked_idx):
            top1 = float(scores_desc[0])
            anchor_threshold = max(threshold, top1 - margin)
            return [int(j) for k, j in enumerate(ranked_idx) if scores_desc[k] >= anchor_threshold]
        return f

    def knee_strategy(floor, min_bundle, max_bundle, drop=0.85):
        def f(scores_desc, ranked_idx):
            sz = find_knee(scores_desc, floor=floor, min_bundle=min_bundle,
                           max_bundle=max_bundle, proportional_drop=drop)
            return [int(j) for j in ranked_idx[:sz]]
        return f

    strategies = [
        ("margin-0.55-0.15 (huidige)", margin_strategy(0.55, 0.15)),
        ("margin-0.50-0.15",           margin_strategy(0.50, 0.15)),
        ("knee-floor0.45-drop0.85-min10-max200", knee_strategy(0.45, 10, 200, 0.85)),
        ("knee-floor0.45-drop0.80-min10-max200", knee_strategy(0.45, 10, 200, 0.80)),
        ("knee-floor0.40-drop0.85-min10-max300", knee_strategy(0.40, 10, 300, 0.85)),
        ("knee-floor0.40-drop0.80-min15-max300", knee_strategy(0.40, 15, 300, 0.80)),
        ("knee-floor0.40-drop0.75-min20-max300", knee_strategy(0.40, 20, 300, 0.75)),
    ]

    print(f"\n[eval] {len(strategies)} strategieën × {len(gold)} gold-paren")
    results = []
    for name, fn in strategies:
        print(f"  → {name}...")
        r = evaluate_strategy(name, anchors, anchor_vecs, chunk_ids, chunk_vecs,
                              chunk_metas, sim, fn, gold)
        results.append(r)

    # Console-rapport
    print(f"\n{'='*100}")
    print(f"{'Strategie':<32} {'mean-recall':>12} {'min-recall':>12} {'#perfect':>10} {'med-bundle':>12} {'max-bundle':>12} {'#uncov':>8}")
    print(f"{'-'*100}")
    for r in results:
        print(f"{r['strategy']:<32} {r['mean_recall']:>12.3f} {r['min_recall']:>12.3f} "
              f"{r['n_perfect']:>10} {r['median_bundle_size']:>12} {r['max_bundle_size']:>12} "
              f"{r['n_uncovered_anchors']:>8}")
    print(f"{'='*100}\n")

    # Per anchor: misses voor best-recall-strategie
    best = max(results, key=lambda r: (r["mean_recall"], -r["median_bundle_size"]))
    print(f"BESTE STRATEGIE: {best['strategy']} (recall={best['mean_recall']})")
    print(f"\nPer-anchor misses (best strategy):")
    for d in best["per_anchor"]:
        miss_str = ", ".join(d["miss"]) if d["miss"] else "—"
        print(f"  {d['anchor_id']:15} recall={d['recall']:.2f}  bundle={d['bundle_size']:>4}  misses: {miss_str}")

    # JSON
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = OUT_DIR / f"matching-experiment-{ts}.json"
    out.write_text(json.dumps({
        "timestamp": ts,
        "n_anchors": len(anchors),
        "n_chunks": len(chunk_ids),
        "n_gold_pairs": len(gold),
        "strategies": results,
    }, indent=2, ensure_ascii=False))
    print(f"\n[output] {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
