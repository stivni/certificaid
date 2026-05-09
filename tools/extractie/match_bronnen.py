"""
Bron-first matching — fase B van de extractie-pipeline (ADR-008).

Voert deterministische cosine-similarity uit tussen anchor-embeddings en
bron-chunks om per anchor een bundel relevante chunks te bouwen.

Werkwijze:
  - Leest enriched anchors uit data/extractie/<po>/anchors/<po>-anchors.json
    (gegenereerd door fase A: anchor-verrijking via subagent).
  - Bundle = chunks waar score >= max(floor, top1 - margin) (adaptive bundling).
  - Configureerbare chroma-path (default: data/chroma_db_<po>/ als die bestaat).
  - Output: data/extractie/<po>/matches/<po>-matches.json (ephemeral, kan in gitignore).

Volledig deterministisch — geen LLM-calls (zie ADR-008 §2).

Gebruik:
  python3 -m tools.extractie.match_bronnen --po 4.0
  python3 -m tools.extractie.match_bronnen --po 4.0 --threshold 0.55 --margin 0.15
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import chromadb
import numpy as np
import yaml
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from sentence_transformers import SentenceTransformer

ROOT = Path(__file__).resolve().parent.parent.parent
EMBEDDING_MODEL = "BAAI/bge-m3"
CHROMA_PATH_MAIN = ROOT / "data" / "chroma_db"


# ---------------------------------------------------------------------------
# Anchor-extractie uit programmaonderdeel-JSON (fallback als geen enriched JSON)
# ---------------------------------------------------------------------------

def _extract_kenniselementen(items: list, parent_path: list[str]) -> list[dict]:
    out = []
    for ke in items:
        code = ke["code"]
        text = ke["tekst"]
        full_text = " — ".join(parent_path + [text]) if parent_path else text
        out.append({
            "anchor_id": code,
            "anchor_type": "kenniselement",
            "tekst": text,
            "verbose": full_text,
            "synoniemen": [],
        })
        if "subitems" in ke:
            out.extend(_extract_kenniselementen(ke["subitems"], parent_path + [text]))
    return out


def build_anchors_from_po(po_data: dict) -> list[dict]:
    po_titel = po_data["titel"]
    anchors = []
    kern_blokken = set(po_data.get("scope", {}).get("kern_taakblokken", []))
    for tb in po_data.get("taakblokken", []):
        tb_code = tb["code"]
        if kern_blokken and tb_code not in kern_blokken:
            continue
        for i, taak in enumerate(tb.get("taken", []), 1):
            anchors.append({
                "anchor_id": f"{tb_code}.taak.{i}",
                "anchor_type": "taak",
                "taakblok": tb_code,
                "tekst": taak["tekst"],
                "verbose": f"{po_titel} — {taak['tekst']}",
                "synoniemen": [],
            })
        for i, doel in enumerate(tb.get("doelstellingen", []), 1):
            tekst = doel["tekst"] if isinstance(doel, dict) else doel
            anchors.append({
                "anchor_id": f"{tb_code}.doel.{i}",
                "anchor_type": "doelstelling",
                "taakblok": tb_code,
                "tekst": tekst,
                "verbose": f"{po_titel} — {tekst}",
                "synoniemen": [],
            })

    kern_ke = set(po_data.get("scope", {}).get("kern_kenniselementen", []))
    for ke in po_data.get("kenniselementen", []):
        if kern_ke and ke["code"] not in kern_ke:
            continue
        anchors.extend(_extract_kenniselementen([ke], parent_path=[po_titel]))
    return anchors


def load_anchors(po: str, override_path: str | None = None) -> tuple[list[dict], str]:
    """Laad anchors. Override-pad → dat. Anders productie-pad. Anders fallback uit PO-JSON."""
    if override_path:
        path = Path(override_path)
        if not path.is_absolute():
            path = ROOT / path
        data = json.loads(path.read_text())
        return data["anchors"], path.name

    enriched_path = ROOT / "data" / "extractie" / po / "anchors" / f"{po}-anchors.json"
    if enriched_path.exists():
        data = json.loads(enriched_path.read_text())
        return data["anchors"], "enriched"

    po_path = next((ROOT / "data" / "programmaonderdelen").glob(f"{po}-*.json"))
    return build_anchors_from_po(json.loads(po_path.read_text())), "fallback-from-po"


def anchor_embedding_text(a: dict) -> str:
    """Combineer verbose + synoniemen tot embedding-tekst."""
    parts = [a.get("verbose") or a["tekst"]]
    syns = a.get("synoniemen") or []
    if syns:
        parts.append("Synoniemen: " + ", ".join(syns))
    return " ".join(parts)


# ---------------------------------------------------------------------------
# Cosine similarity
# ---------------------------------------------------------------------------

def cosine_matrix(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    a_norm = a / np.linalg.norm(a, axis=1, keepdims=True)
    b_norm = b / np.linalg.norm(b, axis=1, keepdims=True)
    return a_norm @ b_norm.T


# ---------------------------------------------------------------------------
# ChromaDB-pad detectie
# ---------------------------------------------------------------------------

def detect_chroma_path(po: str, override: str | None = None) -> Path:
    if override:
        return Path(override)
    scoped = ROOT / "data" / f"chroma_db_{po}"
    if scoped.exists():
        return scoped
    return CHROMA_PATH_MAIN


# ---------------------------------------------------------------------------
# Hoofd
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--po", required=True, help="programmaonderdeel-code, bv. 4.0")
    parser.add_argument("--threshold", type=float, default=0.55,
                        help="absolute floor cosine-drempel (bge-m3 baseline ligt hoog, ~0.55+). "
                             "Met --margin: bundel-drempel = max(threshold, top1 - margin).")
    parser.add_argument("--margin", type=float, default=None,
                        help="margin-from-top: chunk in bundle als score >= top1_score - margin. "
                             "Gecombineerd met --threshold als floor. Default: alleen threshold.")
    parser.add_argument("--top-k-display", type=int, default=10,
                        help="hoeveel top-K te tonen per chunk/anchor in de output (info, geen filter)")
    parser.add_argument("--chroma-path", default=None, help="override ChromaDB-pad")
    parser.add_argument("--out-suffix", default="",
                        help="suffix voor output-bestand (bv. 'v2', 'verrijkt')")
    parser.add_argument("--anchors-file", default=None,
                        help="override anchor-bestand (default: data/extractie/<po>/anchors/<po>-anchors.json)")
    args = parser.parse_args()

    # ------ Anchors ------
    anchors, source = load_anchors(args.po, args.anchors_file)
    print(f"[anchors] {len(anchors)} stuks (bron: {source})")
    print(f"          taken: {sum(1 for a in anchors if a['anchor_type']=='taak')}, "
          f"doelstellingen: {sum(1 for a in anchors if a['anchor_type']=='doelstelling')}, "
          f"kenniselementen: {sum(1 for a in anchors if a['anchor_type']=='kenniselement')}")

    # ------ Chunks ------
    scope_path = ROOT / "data" / "programmaonderdelen" / f"{args.po}-bronnen-scope.yaml"
    scope = yaml.safe_load(scope_path.read_text())
    scope_files = []
    for cat in ("wetteksten", "normen", "adviezen"):
        scope_files.extend(scope.get("bronnen", {}).get(cat) or [])

    chroma_path = detect_chroma_path(args.po, args.chroma_path)
    print(f"[chroma] {chroma_path.relative_to(ROOT)}")

    client = chromadb.PersistentClient(path=str(chroma_path))
    ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL, device="cpu")
    col = client.get_collection("bronnen", embedding_function=ef)

    chunk_data = col.get(
        where={"bestand": {"$in": scope_files}},
        include=["embeddings", "metadatas", "documents"],
    )
    chunk_ids = chunk_data["ids"]
    chunk_embs = np.array(chunk_data["embeddings"])
    chunk_metas = chunk_data["metadatas"]
    chunk_docs = chunk_data["documents"]
    print(f"[chunks] {len(chunk_ids)} stuks uit {len(set(m['bestand'] for m in chunk_metas))} bronnen")
    if len(chunk_ids) == 0:
        raise SystemExit("Geen chunks gevonden — is de RAG-index gebouwd?")

    by_rol = {}
    for m in chunk_metas:
        by_rol[m.get("bron_rol", "?")] = by_rol.get(m.get("bron_rol", "?"), 0) + 1
    print(f"          per bron_rol: {by_rol}")

    # ------ Anchor-embeddings ------
    print(f"[embed] anchors embedden ({EMBEDDING_MODEL})...")
    model = SentenceTransformer(EMBEDDING_MODEL, device="cpu")
    anchor_texts = [anchor_embedding_text(a) for a in anchors]
    anchor_embs = model.encode(anchor_texts, normalize_embeddings=False, show_progress_bar=True)

    # ------ Similarity ------
    sim = cosine_matrix(np.array(anchor_embs), chunk_embs)
    threshold = args.threshold

    # ------ Per-chunk view ------
    chunk_view = []
    for j, cid in enumerate(chunk_ids):
        scores = sim[:, j]
        top_idx = np.argsort(-scores)[: args.top_k_display]
        meta = chunk_metas[j]
        # Bundel-anchors (boven drempel)
        strong_anchor_idx = [int(i) for i in np.where(scores >= threshold)[0]]
        strong_anchor_idx.sort(key=lambda i: -scores[i])
        chunk_view.append({
            "chunk_id": cid,
            "bron": meta.get("bron", ""),
            "bron_rol": meta.get("bron_rol", ""),
            "sectie": meta.get("sectie") or meta.get("artikel_ref", ""),
            "preview": chunk_docs[j][:200].replace("\n", " "),
            "max_score": round(float(scores[top_idx[0]]), 4),
            "n_strong_anchors": len(strong_anchor_idx),
            "top_anchors": [
                {
                    "anchor_id": anchors[i]["anchor_id"],
                    "anchor_type": anchors[i]["anchor_type"],
                    "tekst": anchors[i]["tekst"],
                    "score": round(float(scores[i]), 4),
                }
                for i in top_idx
            ],
        })

    # ------ Per-anchor view: BUNDEL = chunks boven adaptive drempel ------
    anchor_view = []
    for i, a in enumerate(anchors):
        scores = sim[i, :]
        # Sorteer chunks aflopend op score
        ranked = sorted(range(len(chunk_ids)), key=lambda j: -scores[j])
        top1_score = float(scores[ranked[0]])
        # Adaptive drempel: max(absolute floor, top1 - margin) als margin opgegeven
        if args.margin is not None:
            anchor_threshold = max(threshold, top1_score - args.margin)
        else:
            anchor_threshold = threshold
        bundle_idx = [j for j in ranked if scores[j] >= anchor_threshold]
        # Top-K-display voor de "bijna-bundel" (info)
        display_idx = ranked[: args.top_k_display]
        anchor_view.append({
            "anchor_id": a["anchor_id"],
            "anchor_type": a["anchor_type"],
            "tekst": a["tekst"],
            "verbose": a.get("verbose", ""),
            "synoniemen": a.get("synoniemen", []),
            "max_score": round(top1_score, 4),
            "anchor_threshold": round(anchor_threshold, 4),
            "bundle_size": len(bundle_idx),
            "covered": len(bundle_idx) > 0,
            "bundle": [
                {
                    "chunk_id": chunk_ids[j],
                    "bron": chunk_metas[j].get("bron", ""),
                    "bron_rol": chunk_metas[j].get("bron_rol", ""),
                    "sectie": chunk_metas[j].get("sectie") or chunk_metas[j].get("artikel_ref", ""),
                    "score": round(float(scores[j]), 4),
                }
                for j in bundle_idx
            ],
            "top_chunks_display": [
                {
                    "chunk_id": chunk_ids[j],
                    "bron": chunk_metas[j].get("bron", ""),
                    "sectie": chunk_metas[j].get("sectie") or chunk_metas[j].get("artikel_ref", ""),
                    "score": round(float(scores[j]), 4),
                }
                for j in display_idx
            ],
        })

    # ------ Summary + percentielen ------
    all_max_per_chunk = np.array([c["max_score"] for c in chunk_view])
    all_max_per_anchor = np.array([a["max_score"] for a in anchor_view])
    bundle_sizes = np.array([a["bundle_size"] for a in anchor_view])
    n_uncovered = int((bundle_sizes == 0).sum())
    n_orphan_chunks = int((all_max_per_chunk < threshold).sum())

    summary = {
        "po": args.po,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "embedding_model": EMBEDDING_MODEL,
        "threshold": threshold,
        "anchor_source": source,
        "chroma_path": str(chroma_path.relative_to(ROOT)),
        "stats": {
            "n_anchors": len(anchors),
            "n_chunks": len(chunk_ids),
            "n_uncovered_anchors": n_uncovered,
            "n_orphan_chunks": n_orphan_chunks,
            "bundle_size_p25": float(np.percentile(bundle_sizes, 25)),
            "bundle_size_median": float(np.percentile(bundle_sizes, 50)),
            "bundle_size_p75": float(np.percentile(bundle_sizes, 75)),
            "bundle_size_max": int(bundle_sizes.max()),
            "max_score_per_chunk_min": float(all_max_per_chunk.min()),
            "max_score_per_chunk_median": float(np.median(all_max_per_chunk)),
            "max_score_per_chunk_max": float(all_max_per_chunk.max()),
            "max_score_per_anchor_min": float(all_max_per_anchor.min()),
            "max_score_per_anchor_median": float(np.median(all_max_per_anchor)),
            "max_score_per_anchor_max": float(all_max_per_anchor.max()),
        },
    }

    print("\n[summary]")
    for k, v in summary["stats"].items():
        print(f"  {k}: {v}")

    # Per-anchor-type breakdown
    print("\n[per anchor-type] mediane max_score (lager = slechter gedekt)")
    for t in ("taak", "doelstelling", "kenniselement"):
        scores_t = [a["max_score"] for a in anchor_view if a["anchor_type"] == t]
        if scores_t:
            print(f"  {t:14s} n={len(scores_t):3d}  med={np.median(scores_t):.3f}  "
                  f"min={min(scores_t):.3f}  max={max(scores_t):.3f}  "
                  f"uncovered={sum(1 for s in scores_t if s < threshold)}")

    out_dir = ROOT / "data" / "extractie" / args.po / "matches"
    out_dir.mkdir(parents=True, exist_ok=True)
    suffix = f"-{args.out_suffix}" if args.out_suffix else ""
    out_path = out_dir / f"{args.po}-matches{suffix}.json"
    out_path.write_text(json.dumps({
        "summary": summary,
        "chunks": chunk_view,
        "anchors": anchor_view,
    }, ensure_ascii=False, indent=2))
    print(f"\n[output] {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
