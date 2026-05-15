"""
Bron-first matching — fase B (ADR-008).

Globale matching: alle anchors van alle 19 PO's tegelijk tegen alle bron-chunks.
Geen per-PO scope-filter — een chunk kan in bundles van meerdere ankers belanden,
ook cross-PO. Anchor-vectors zijn pre-computed in `data/programma/anchors.json` (eenmalig
ge-embed), dus geen runtime-embedding meer.

Werkwijze:
  1. Laad anchors uit data/programma/anchors.json (inline vectors).
  2. Laad alle bron-chunk-embeddings uit data/rag/main (collection `bronnen`).
  3. Cosine-matrix N_anchors × N_chunks.
  4. Per anchor: bundle = chunks waar score >= max(floor, top1 - margin).
  5. References (uit programma.json) blijven pass-through metadata in de output —
     fase C (concept-extractie) gebruikt ze om source_files-chunks verplicht
     toe te voegen aan de bundle.

Output: data/extractie/matches/<run_id>.json + symlink latest.json

Gebruik:
  python3 -m tools.extractie.match_bronnen
  python3 -m tools.extractie.match_bronnen --threshold 0.55 --margin 0.15
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import chromadb
import numpy as np
from tqdm import tqdm

ROOT = Path(__file__).resolve().parent.parent.parent
ANCHORS_PATH = ROOT / "data" / "programma" / "anchors.json"
CHROMA_PATH = ROOT / "data" / "rag" / "main"
MATCHES_DIR = ROOT / "data" / "extractie" / "matches"


def cosine_matrix(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Cosine-similarity matrix tussen rijen van a en b. Beide kunnen reeds
    genormaliseerd zijn — dan is dit gewoon a @ b.T."""
    a_norm = a / np.linalg.norm(a, axis=1, keepdims=True)
    b_norm = b / np.linalg.norm(b, axis=1, keepdims=True)
    return a_norm @ b_norm.T


def load_anchors() -> tuple[list[dict], np.ndarray]:
    if not ANCHORS_PATH.exists():
        raise SystemExit(f"data/programma/anchors.json niet gevonden — run build_anchors.py + embed_anchors.py")
    data = json.loads(ANCHORS_PATH.read_text())
    anchors = data["anchors"]
    missing = [a["anchor_id"] for a in anchors if a.get("vector") is None]
    if missing:
        raise SystemExit(
            f"{len(missing)} anchors hebben geen vector — run "
            f"`python3 -m tools.extractie.embed_anchors`"
        )
    vectors = np.array([a["vector"] for a in anchors], dtype=np.float32)
    return anchors, vectors


def load_chunks() -> tuple[list[str], np.ndarray, list[dict]]:
    if not CHROMA_PATH.exists():
        raise SystemExit(f"data/rag/main niet gevonden — bouw eerst de RAG-index")
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    col = client.get_collection("bronnen")
    print(f"  ChromaDB collection 'bronnen': {col.count()} chunks totaal")
    print(f"  embeddings ophalen (kan even duren bij grote corpus)...")
    data = col.get(include=["embeddings", "metadatas"])
    return data["ids"], np.array(data["embeddings"], dtype=np.float32), data["metadatas"]


def find_knee(scores_desc: np.ndarray, floor: float = 0.40,
              min_bundle: int = 10, max_bundle: int = 200,
              proportional_drop: float = 0.85) -> int:
    """Adaptive knee-detectie op aflopende cosine-scores.

    Strategie (proportionele drempel):
      1. Hard floor: alle scores < `floor` vallen sowieso af.
      2. Adaptive drempel = top1 × proportional_drop. Een chunk hoort bij
         de bundle als score >= max(floor, top1*proportional_drop).
      3. Safeguards: [min_bundle, max_bundle].

    Achterliggende intuïtie: anchors met een scherpe top (hoge top1, snelle
    drop) krijgen een KLEINE bundle (top 5-15) want de echt relevante chunks
    zijn vlot zichtbaar. Anchors met een vlakke distributie (lage top1, weinig
    drop) krijgen een GROTERE bundle want de signaal-noise-ratio is laag en
    we hebben meer chunks nodig om de relevante content te dekken.

    Retourneert: bundle-grootte (aantal chunks in bundle).
    """
    n = len(scores_desc)
    if n == 0:
        return 0
    top1 = float(scores_desc[0])
    threshold = max(floor, top1 * proportional_drop)
    # Tel hoeveel chunks de drempel halen
    bundle_size = int(np.sum(scores_desc >= threshold))
    # Clip naar [min_bundle, max_bundle]
    bundle_size = max(min(bundle_size, max_bundle), min(min_bundle, n))
    return bundle_size


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strategy", choices=["margin", "knee"], default="margin",
                        help="bundling strategie. 'margin' (default): chunk in bundle "
                             "als score >= max(threshold, top1 - margin). 'knee': "
                             "adaptive knie-detectie op de score-curve, met floor + "
                             "min/max-bundle als safeguards.")
    parser.add_argument("--threshold", type=float, default=0.55,
                        help="absolute floor cosine-drempel (default 0.55 voor margin, "
                             "0.40 voor knee)")
    parser.add_argument("--margin", type=float, default=0.15,
                        help="margin-strategie: chunk in bundle als score >= "
                             "max(threshold, top1 - margin) (default 0.15)")
    parser.add_argument("--knee-min-bundle", type=int, default=5,
                        help="knee-strategie: minimum bundle-grootte (default 5)")
    parser.add_argument("--knee-max-bundle", type=int, default=500,
                        help="knee-strategie: maximum bundle-grootte (default 500)")
    parser.add_argument("--top-k-display", type=int, default=10,
                        help="hoeveel top-K te tonen per chunk (info, geen filter)")
    args = parser.parse_args()
    # Knee-strategie heeft lagere default-floor
    if args.strategy == "knee" and args.threshold == 0.55:
        args.threshold = 0.40

    print("[anchors] laden...")
    anchors, anchor_vecs = load_anchors()
    print(f"  {len(anchors)} anchors met vectors ({anchor_vecs.shape[1]} dims)")

    print("[chunks] laden uit ChromaDB...")
    chunk_ids, chunk_vecs, chunk_metas = load_chunks()
    n_chunks = len(chunk_ids)
    print(f"  {n_chunks} chunks geladen")

    by_rol: dict[str, int] = {}
    for m in chunk_metas:
        by_rol[m.get("bron_rol", "?")] = by_rol.get(m.get("bron_rol", "?"), 0) + 1
    print(f"  per bron_rol: {by_rol}")

    print(f"[match] cosine-matrix {len(anchors)} × {n_chunks} ...")
    sim = cosine_matrix(anchor_vecs, chunk_vecs)
    print(f"  matrix shape: {sim.shape}")

    if args.strategy == "knee":
        print(f"[bundle] knee-detectie (floor={args.threshold}, min={args.knee_min_bundle}, max={args.knee_max_bundle})")
    else:
        print(f"[bundle] margin-thresholding (floor={args.threshold}, margin={args.margin})")
    anchor_view = []
    for i, a in enumerate(tqdm(anchors, desc="    anchors")):
        scores = sim[i, :]
        # Sorteer chunks aflopend op score
        ranked_idx = np.argsort(-scores)
        top1_score = float(scores[ranked_idx[0]])

        if args.strategy == "knee":
            scores_desc = scores[ranked_idx]
            bundle_size = find_knee(
                scores_desc,
                floor=args.threshold,
                min_bundle=args.knee_min_bundle,
                max_bundle=args.knee_max_bundle,
            )
            bundle_idx = [int(j) for j in ranked_idx[:bundle_size]]
            anchor_threshold = float(scores[bundle_idx[-1]]) if bundle_idx else args.threshold
        else:
            anchor_threshold = max(args.threshold, top1_score - args.margin)
            bundle_idx = [int(j) for j in ranked_idx if scores[j] >= anchor_threshold]
        display_idx = ranked_idx[: args.top_k_display].tolist()

        anchor_view.append({
            "anchor_id": a["anchor_id"],
            "po": a["po"],
            "tekst": a["tekst"],
            "max_score": round(top1_score, 4),
            "anchor_threshold": round(float(anchor_threshold), 4),
            "bundle_size": len(bundle_idx),
            "covered": len(bundle_idx) > 0,
            "bundle": [
                {
                    "chunk_id": chunk_ids[j],
                    "chunk_sha": chunk_metas[j].get("chunk_sha"),
                    "bestand": chunk_metas[j].get("bestand", ""),
                    "bron_rol": chunk_metas[j].get("bron_rol", ""),
                    "sectie": chunk_metas[j].get("sectie") or chunk_metas[j].get("artikel_ref", ""),
                    "score": round(float(scores[j]), 4),
                }
                for j in bundle_idx
            ],
            "top_chunks_display": [
                {
                    "chunk_id": chunk_ids[j],
                    "bestand": chunk_metas[j].get("bestand", ""),
                    "score": round(float(scores[int(j)]), 4),
                }
                for j in display_idx
            ],
            # Pass-through references — fase C voegt deze chunks verplicht toe.
            "references": a.get("references", []),
        })

    # ------ Summary ------
    bundle_sizes = np.array([a["bundle_size"] for a in anchor_view])
    max_scores = np.array([a["max_score"] for a in anchor_view])
    n_uncovered = int((bundle_sizes == 0).sum())
    n_with_refs = sum(1 for a in anchor_view if a["references"])

    # Per-PO breakdown
    by_po: dict[str, dict] = {}
    for a in anchor_view:
        po = a["po"]
        by_po.setdefault(po, {"n": 0, "median_score": [], "uncovered": 0, "median_bundle": []})
        by_po[po]["n"] += 1
        by_po[po]["median_score"].append(a["max_score"])
        by_po[po]["median_bundle"].append(a["bundle_size"])
        if a["bundle_size"] == 0:
            by_po[po]["uncovered"] += 1
    for po, st in by_po.items():
        st["median_score"] = round(float(np.median(st["median_score"])), 4)
        st["median_bundle"] = int(np.median(st["median_bundle"]))

    run_id = datetime.now(timezone.utc).strftime("run-%Y%m%dT%H%M%SZ")
    summary = {
        "run_id": run_id,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "threshold": args.threshold,
        "margin": args.margin,
        "n_anchors": len(anchors),
        "n_chunks": n_chunks,
        "n_uncovered_anchors": n_uncovered,
        "n_anchors_with_refs": n_with_refs,
        "bundle_size_p25": float(np.percentile(bundle_sizes, 25)),
        "bundle_size_median": float(np.percentile(bundle_sizes, 50)),
        "bundle_size_p75": float(np.percentile(bundle_sizes, 75)),
        "bundle_size_max": int(bundle_sizes.max()),
        "max_score_p10": float(np.percentile(max_scores, 10)),
        "max_score_median": float(np.median(max_scores)),
        "max_score_max": float(max_scores.max()),
        "by_po": by_po,
    }

    print("\n[summary]")
    for k, v in summary.items():
        if k == "by_po":
            continue
        print(f"  {k}: {v}")

    print("\n[per PO]")
    for po, st in sorted(by_po.items()):
        print(f"  {po}: n={st['n']:3d}  med-score={st['median_score']:.3f}  "
              f"med-bundle={st['median_bundle']:3d}  uncovered={st['uncovered']}")

    # ------ Schrijven ------
    MATCHES_DIR.mkdir(parents=True, exist_ok=True)
    out_path = MATCHES_DIR / f"{run_id}.json"
    out_path.write_text(json.dumps({
        "summary": summary,
        "anchors": anchor_view,
    }, ensure_ascii=False, indent=2))
    print(f"\n[output] {out_path.relative_to(ROOT)}")

    # Update latest-pointer (relative symlink)
    latest = MATCHES_DIR / "latest.json"
    if latest.exists() or latest.is_symlink():
        latest.unlink()
    latest.symlink_to(out_path.name)
    print(f"[latest] {latest.relative_to(ROOT)} → {out_path.name}")


if __name__ == "__main__":
    main()
