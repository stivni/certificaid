"""
Embed anchors — vult `vector` in voor elk anker in `data/anchors.json`.

Gebruikt bge-m3 (zelfde model als bronnen-RAG, ADR-006). SHA-skip: anchors
waarvan `embedding_text_sha` niet veranderd is t.o.v. de bestaande `vector`,
worden overgeslagen. Bij eerste run: alle 446 anchors embedden (~30s op MPS).

Output: `data/anchors.json` in-place geüpdatet met `vector: [float, ...]`.

Gebruik:
  python3 -m tools.extractie.embed_anchors                # incrementeel
  python3 -m tools.extractie.embed_anchors --force        # alles opnieuw
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import torch
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

ROOT = Path(__file__).resolve().parent.parent.parent
ANCHORS = ROOT / "data" / "anchors.json"
EMBEDDING_MODEL = "BAAI/bge-m3"
MPS_MAX_SEQ_LENGTH = 2048   # zelfde regel als rag_index.py


def detect_device() -> str:
    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true",
                        help="herbouw alle vectors (negeer sha-skip)")
    parser.add_argument("--device", choices=["mps", "cuda", "cpu"], default=None)
    parser.add_argument("--batch-size", type=int, default=16)
    args = parser.parse_args()

    device = args.device or detect_device()
    print(f"→ device: {device}")

    data = json.loads(ANCHORS.read_text())
    anchors = data["anchors"]

    # Bepaal welke anchors herembed nodig hebben
    todo: list[tuple[int, str]] = []
    for i, a in enumerate(anchors):
        if args.force or a.get("vector") is None:
            todo.append((i, a["embedding_text"]))
            continue
        # Check sha (zou niet moeten kunnen verschillen, maar guard)
        if a.get("vector_sha") != a.get("embedding_text_sha"):
            todo.append((i, a["embedding_text"]))

    if not todo:
        print(f"  alle {len(anchors)} anchors hebben actuele vectors — niets te doen")
        return

    print(f"  {len(todo)} anchors te embedden ({len(anchors) - len(todo)} cached)")

    model = SentenceTransformer(EMBEDDING_MODEL, device=device)
    if device == "mps":
        model.max_seq_length = MPS_MAX_SEQ_LENGTH

    # Batch-encode
    texts = [t for _, t in todo]
    indices = [i for i, _ in todo]
    vectors = []
    n_batches = (len(texts) + args.batch_size - 1) // args.batch_size
    for b in tqdm(range(0, len(texts), args.batch_size), total=n_batches, desc="    embedding"):
        chunk = texts[b:b + args.batch_size]
        embs = model.encode(
            chunk,
            batch_size=args.batch_size,
            show_progress_bar=False,
            normalize_embeddings=True,
        )
        vectors.extend(embs.tolist())
        if device == "mps":
            torch.mps.empty_cache()

    for i, idx in enumerate(indices):
        anchors[idx]["vector"] = vectors[i]
        anchors[idx]["vector_sha"] = anchors[idx]["embedding_text_sha"]

    data["embedded_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    data["embedding_model"] = EMBEDDING_MODEL

    ANCHORS.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"  → {ANCHORS.relative_to(ROOT)} ({len(todo)} vectors geüpdatet)")


if __name__ == "__main__":
    main()
