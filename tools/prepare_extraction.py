"""
Bereidt één concept voor op extractie door een Claude Code agent.

1. Haalt RAG-chunks op via rag_query.py
2. Schrijft een gestructureerd context-bestand naar data/extraction_queue/

De Claude Code scheduled task leest dat bestand en genereert het concept record.

Gebruik:
  python tools/prepare_extraction.py --concept meldingsplicht-aww --po 4.0 \
      --tdk "Meldingsplicht bij vermoeden van WG/FT aan de CFI"
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import date

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

ROOT = Path(__file__).parent.parent
CHROMA_PATH = ROOT / "data" / "chroma_db"
QUEUE_DIR = ROOT / "data" / "extraction_queue"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

BRONNEN_COLS = ["wetteksten", "normen", "adviezen"]
ALL_COLS = ["wetteksten", "normen", "adviezen", "tdks", "bestaande_fiches"]


def retrieve(query: str, collections: list[str], n: int = 6) -> list[dict]:
    ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    results = []
    for name in collections:
        try:
            col = client.get_collection(name, embedding_function=ef)
            if col.count() == 0:
                continue
            res = col.query(query_texts=[query], n_results=min(n, col.count()))
            for doc, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
                results.append({
                    "collection": name,
                    "score": round(1 - dist, 4),
                    "bron": meta.get("bron", ""),
                    "artikel": meta.get("artikel_ref") or meta.get("sectie") or "",
                    "text": doc,
                })
        except Exception:
            pass
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:n]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--concept", required=True)
    parser.add_argument("--po", required=True)
    parser.add_argument("--tdk", default="")
    parser.add_argument("--n", type=int, default=5, help="Chunks per query")
    args = parser.parse_args()

    concept = args.concept
    po = args.po
    tdk = args.tdk or concept

    print(f"→ RAG retrieval voor: {concept}")

    queries = {
        "definitie_scope": f"{concept} definitie toepassingsgebied {tdk}",
        "uitzonderingen":  f"{concept} uitzondering tenzij behalve in afwijking van",
        "procedure":       f"{concept} procedure verplichting stappen termijn",
        "voorbeelden":     f"{concept} voorbeeld praktijk geval",
    }

    all_chunks = {}
    for q_name, q_text in queries.items():
        cols = BRONNEN_COLS if "uitzon" in q_name or "proce" in q_name else ALL_COLS
        chunks = retrieve(q_text, cols, args.n)
        all_chunks[q_name] = chunks
        print(f"  {q_name}: {len(chunks)} chunks")

    # Schrijf context-bestand
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    out_path = QUEUE_DIR / f"{concept}.md"

    lines = [
        f"# Extractie-context: {concept}",
        f"",
        f"**PO**: {po}  ",
        f"**TDK-anker**: {tdk}  ",
        f"**Datum**: {date.today().isoformat()}  ",
        f"**Output**: `data/concept_records/{concept}.json`",
        f"",
    ]

    for q_name, chunks in all_chunks.items():
        lines.append(f"## {q_name.replace('_', ' ').title()}")
        lines.append("")
        for i, c in enumerate(chunks, 1):
            ref = c["bron"]
            if c.get("artikel"):
                ref += f" — {c['artikel']}"
            lines.append(f"**[{i}] {ref}** (score: {c['score']})")
            lines.append("")
            # Max 600 chars per chunk
            lines.append(c["text"][:600])
            lines.append("")
        lines.append("")

    out_path.write_text("\n".join(lines))
    print(f"✓ Context-bestand: {out_path.relative_to(ROOT)}")
    print(f"  Totaal chunks: {sum(len(v) for v in all_chunks.values())}")


if __name__ == "__main__":
    main()
