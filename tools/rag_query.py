"""
CLI-test voor de Certificaid RAG-index.

Gebruik:
  python tools/rag_query.py "meldingsplicht bij vermoeden van witwassen"
  python tools/rag_query.py "btw-vrijstelling kleine onderneming" --collections wetteksten,normen
  python tools/rag_query.py "continuiteitsrisico" --n 10 --show-meta
"""

import argparse
import json
from pathlib import Path

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

ROOT = Path(__file__).parent.parent
CHROMA_PATH = ROOT / "data" / "chroma_db"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

ALL_COLLECTIONS = ["wetteksten", "normen", "adviezen", "tdks", "bestaande_fiches", "concepts"]


def query(question: str, collections: list[str], n: int = 5, show_meta: bool = False):
    ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))

    results = []
    for name in collections:
        try:
            col = client.get_collection(name, embedding_function=ef)
        except Exception:
            print(f"  Collection '{name}' bestaat nog niet — overgeslagen")
            continue

        res = col.query(query_texts=[question], n_results=min(n, col.count() or 1))
        docs = res["documents"][0]
        metas = res["metadatas"][0]
        distances = res["distances"][0]

        for doc, meta, dist in zip(docs, metas, distances):
            results.append({
                "collection": name,
                "score": round(1 - dist, 4),  # cosine similarity
                "bron": meta.get("bron", ""),
                "sectie": meta.get("artikel_ref") or meta.get("sectie") or meta.get("veld", ""),
                "text": doc,
                "meta": meta,
            })

    # Sorteer op score
    results.sort(key=lambda x: x["score"], reverse=True)
    top = results[:n]

    print(f"\n{'='*60}")
    print(f"Query: {question!r}")
    print(f"Collections: {', '.join(collections)}")
    print(f"{'='*60}\n")

    for i, r in enumerate(top, 1):
        print(f"[{i}] Score: {r['score']}  |  {r['collection']} — {r['bron']}  |  {r['sectie']}")
        print("-" * 60)
        # Toon max 400 chars van de tekst
        preview = r["text"][:400].replace("\n", " ")
        print(f"  {preview}{'...' if len(r['text']) > 400 else ''}")
        if show_meta:
            print(f"  META: {json.dumps(r['meta'], ensure_ascii=False)}")
        print()

    return top


def main():
    parser = argparse.ArgumentParser(description="Query de Certificaid RAG-index")
    parser.add_argument("query", help="Zoekvraag")
    parser.add_argument("--collections", default=",".join(ALL_COLLECTIONS),
                        help=f"Kommagescheiden lijst van collections (default: alle)")
    parser.add_argument("--n", type=int, default=5, help="Aantal resultaten (default: 5)")
    parser.add_argument("--show-meta", action="store_true", help="Toon ook metadata")
    args = parser.parse_args()

    collections = [c.strip() for c in args.collections.split(",")]
    query(args.query, collections, args.n, args.show_meta)


if __name__ == "__main__":
    main()
