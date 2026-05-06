"""
CLI-test voor de Certificaid RAG-index.

Gebruik:
  python tools/rag/rag_query.py "meldingsplicht bij vermoeden van witwassen"
  python tools/rag/rag_query.py "btw-vrijstelling kleine onderneming" --collections wetteksten,normen
  python tools/rag/rag_query.py "continuiteitsrisico" --n 10 --show-meta
  python tools/rag/rag_query.py "meldingsplicht" --rerank          # met cross-encoder reranking
  python tools/rag/rag_query.py "meldingsplicht" --rerank --expand # + context-uitbreiding
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

from lib.retrieval import (
    EMBEDDING_MODEL,
    ALL_COLLECTIONS,
    build_retrieval_stack,
    open_collections,
    retrieve_and_rerank,
    _retrieve_candidates,
)


def query_simple(question: str, collections: list[str], n: int, show_meta: bool):
    """Eenvoudige bi-encoder query (snel, geen reranking)."""
    ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    client = chromadb.PersistentClient(path=str(ROOT / "data" / "chroma_db"))
    cols = open_collections(client, ef, collections)

    results = _retrieve_candidates(cols, question, collections, bi_top_n=n)
    results.sort(key=lambda x: x.score, reverse=True)
    top = results[:n]

    _print_results(question, collections, top, show_meta, reranked=False)
    return top


def query_with_rerank(
    question: str,
    collections: list[str],
    n: int,
    show_meta: bool,
    expand: bool,
):
    """Bi-encoder + cross-encoder reranking + optionele context-uitbreiding."""
    client, ef, reranker = build_retrieval_stack(ROOT / "data" / "chroma_db")
    cols = open_collections(client, ef, collections)

    results = retrieve_and_rerank(
        question, cols, collections, reranker,
        bi_top_n=max(n * 5, 50),
        rerank_threshold=0.0,   # toon alles, gesorteerd op rerank-score
        max_results=n,
        expand_context=expand,
    )

    _print_results(question, collections, results, show_meta, reranked=True)
    return results


def _print_results(question, collections, results, show_meta, reranked):
    print(f"\n{'='*65}")
    print(f"Query: {question!r}")
    print(f"Collections: {', '.join(collections)}")
    if reranked:
        print(f"Mode: bi-encoder + reranker (bge-reranker-v2-m3)")
    print(f"{'='*65}\n")

    for i, r in enumerate(results, 1):
        score_str = (
            f"rerank={r.rerank_score:.3f} | bi={r.score:.3f}"
            if reranked else
            f"score={r.score:.3f}"
        )
        print(f"[{i}] {score_str}  |  {r.collection} — {r.bron}  |  {r.artikel}")
        print("-" * 65)
        preview = r.text[:400].replace("\n", " ")
        print(f"  {preview}{'...' if len(r.text) > 400 else ''}")
        if show_meta:
            print(f"  META: {json.dumps(r.meta, ensure_ascii=False)}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Query de Certificaid RAG-index")
    parser.add_argument("query", help="Zoekvraag")
    parser.add_argument(
        "--collections",
        default=",".join(["wetteksten", "normen", "adviezen"]),
        help="Kommagescheiden lijst van collections",
    )
    parser.add_argument("--n", type=int, default=5, help="Aantal resultaten (default: 5)")
    parser.add_argument("--rerank", action="store_true", help="Gebruik cross-encoder reranking")
    parser.add_argument("--expand", action="store_true", help="Context-uitbreiding (±2 artikelen voor wetteksten)")
    parser.add_argument("--show-meta", action="store_true", help="Toon ook metadata")
    args = parser.parse_args()

    collections = [c.strip() for c in args.collections.split(",")]

    if args.rerank:
        query_with_rerank(args.query, collections, args.n, args.show_meta, args.expand)
    else:
        query_simple(args.query, collections, args.n, args.show_meta)


if __name__ == "__main__":
    main()
