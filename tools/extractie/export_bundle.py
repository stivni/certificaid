"""
Exporteer de bundel van één anchor met volledige chunk-teksten — input voor
de per-anchor concept-extractie subagent (ADR-008 fase C).

Output: data/extractie/<po>/bundles/<po>-<anchor-id-slug>.json
met:
  - anchor info (tekst, verbose, synoniemen)
  - bundle: lijst van chunks met chunk_id, bron, sectie, score, EN volle tekst

Gebruik:
  python3 -m tools.extractie.export_bundle --po 4.0 --anchor-id 4.0.I.D.7 \\
      --matches-file data/extractie/4.0/matches/4.0-matches.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

ROOT = Path(__file__).resolve().parent.parent.parent
EMBEDDING_MODEL = "BAAI/bge-m3"


def slugify(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9.-]+", "-", s).strip("-")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--po", required=True)
    parser.add_argument("--anchor-id", required=True)
    parser.add_argument("--matches-file", required=True,
                        help="bv. data/extractie/4.0/matches/4.0-matches.json")
    parser.add_argument("--anchors-file", default=None,
                        help="optioneel: enriched/clean anchors-bestand (voor verbose+syns)")
    parser.add_argument("--chroma-path", default=None,
                        help="default: data/rag/<po>")
    args = parser.parse_args()

    matches_path = Path(args.matches_file)
    if not matches_path.is_absolute():
        matches_path = ROOT / matches_path
    matches = json.loads(matches_path.read_text())

    # Vind het anchor
    anchor_view = next(
        (a for a in matches["anchors"] if a["anchor_id"] == args.anchor_id),
        None,
    )
    if anchor_view is None:
        raise SystemExit(f"Anchor {args.anchor_id} niet gevonden in {matches_path}")

    bundle_chunk_ids = [c["chunk_id"] for c in anchor_view["bundle"]]
    if not bundle_chunk_ids:
        raise SystemExit(f"Anchor {args.anchor_id} heeft een lege bundle")

    print(f"[bundle] {len(bundle_chunk_ids)} chunks voor {args.anchor_id}")

    # Haal volle tekst op uit ChromaDB
    chroma_path = Path(args.chroma_path) if args.chroma_path else (ROOT / f"data/rag/{args.po}")
    if not chroma_path.exists():
        chroma_path = ROOT / "data" / "rag" / "main"

    client = chromadb.PersistentClient(path=str(chroma_path))
    ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL, device="cpu")
    col = client.get_collection("bronnen", embedding_function=ef)

    # Batch-fetch
    res = col.get(ids=bundle_chunk_ids, include=["documents", "metadatas"])
    by_id = {cid: (doc, meta) for cid, doc, meta in zip(res["ids"], res["documents"], res["metadatas"])}

    # Optioneel: enriched anchors-bestand voor verbose + synoniemen
    anchor_meta = {}
    if args.anchors_file:
        af = Path(args.anchors_file)
        if not af.is_absolute():
            af = ROOT / af
        for a in json.loads(af.read_text())["anchors"]:
            if a["anchor_id"] == args.anchor_id:
                anchor_meta = {
                    "tekst": a.get("tekst", ""),
                    "anchor_type": a.get("anchor_type", ""),
                    "verbose": a.get("verbose", ""),
                    "synoniemen": a.get("synoniemen", []),
                }
                break

    # Bouw output: bundle items met volle tekst, gesorteerd op score (al gesorteerd)
    bundle_with_text = []
    for c in anchor_view["bundle"]:
        cid = c["chunk_id"]
        if cid in by_id:
            doc, meta = by_id[cid]
            bundle_with_text.append({
                "chunk_id": cid,
                "chunk_sha": c.get("chunk_sha") or meta.get("chunk_sha"),
                "bron": meta.get("bron", ""),
                "bron_rol": meta.get("bron_rol", ""),
                "sectie": meta.get("sectie") or meta.get("artikel_ref", ""),
                "score": c["score"],
                "text": doc,
            })

    out = {
        "po": args.po,
        "anchor_id": args.anchor_id,
        "anchor": anchor_meta or {
            "tekst": anchor_view.get("tekst", ""),
            "anchor_type": anchor_view.get("anchor_type", ""),
            "verbose": anchor_view.get("verbose", ""),
            "synoniemen": anchor_view.get("synoniemen", []),
        },
        "matches_source": str(matches_path.relative_to(ROOT)),
        "bundle_size": len(bundle_with_text),
        "bundle": bundle_with_text,
    }

    out_dir = ROOT / "data" / "extractie" / args.po / "bundles"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.po}-{slugify(args.anchor_id)}.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))

    total_chars = sum(len(c["text"]) for c in bundle_with_text)
    print(f"[output] {out_path.relative_to(ROOT)}")
    print(f"         {len(bundle_with_text)} chunks, ~{total_chars:,} chars (~{total_chars//4:,} tokens)")


if __name__ == "__main__":
    main()
