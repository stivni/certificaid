"""
CLI-tool voor de Certificaid RAG-index (ADR-006).

Gebruik:
  python tools/rag/rag_query.py "meldingsplicht bij vermoeden van witwassen"
  python tools/rag/rag_query.py "beroepsgeheim accountant" --bron-rol wettekst,norm
  python tools/rag/rag_query.py "continuiteitsrisico" --n 10 --show-meta
  python tools/rag/rag_query.py "meldingsplicht" --rerank
  python tools/rag/rag_query.py "meldingsplicht" --rerank --expand
  python tools/rag/rag_query.py "antiwitwas" --concepten       # zoek ook in concepten
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
    BRONNEN_COLS,
    build_retrieval_stack,
    open_collections,
    retrieve_and_rerank,
    _retrieve_candidates,
    _detect_device,
)


def query_simple(
    question: str,
    selected_cols: list[str],
    bron_rollen: list[str] | None,
    n: int,
    show_meta: bool,
    chroma_path: Path,
):
    device = _detect_device()
    ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL, device=device)
    client = chromadb.PersistentClient(path=str(chroma_path))
    cols = open_collections(client, ef, selected_cols)

    results = _retrieve_candidates(cols, question, selected_cols, bi_top_n=n, bron_rollen=bron_rollen)
    results.sort(key=lambda x: x.score, reverse=True)
    top = results[:n]

    _print_results(question, selected_cols, bron_rollen, top, show_meta, reranked=False)
    return top


def query_with_rerank(
    question: str,
    selected_cols: list[str],
    bron_rollen: list[str] | None,
    n: int,
    show_meta: bool,
    expand: bool,
    chroma_path: Path,
):
    client, ef, reranker = build_retrieval_stack(chroma_path)
    cols = open_collections(client, ef, selected_cols)

    results = retrieve_and_rerank(
        question, cols, selected_cols, reranker,
        bi_top_n=max(n * 5, 50),
        rerank_threshold=0.0,
        max_results=n,
        expand_context=expand,
        bron_rollen=bron_rollen,
    )

    _print_results(question, selected_cols, bron_rollen, results, show_meta, reranked=True)
    return results


def _print_results(question, selected_cols, bron_rollen, results, show_meta, reranked):
    print(f"\n{'='*65}")
    print(f"Query: {question!r}")
    print(f"Collections: {', '.join(selected_cols)}")
    if bron_rollen:
        print(f"Bron-rollen: {', '.join(bron_rollen)}")
    if reranked:
        print("Mode: bi-encoder + reranker (bge-reranker-v2-m3)")
    print(f"{'='*65}\n")

    for i, r in enumerate(results, 1):
        score_str = (
            f"rerank={r.rerank_score:.3f} | bi={r.score:.3f}"
            if reranked else f"score={r.score:.3f}"
        )
        bron_rol = r.meta.get("bron_rol", r.collection)
        print(f"[{i}] {score_str}  |  {bron_rol} — {r.bron}  |  {r.artikel}")
        print("-" * 65)
        preview = r.text[:400].replace("\n", " ")
        print(f"  {preview}{'...' if len(r.text) > 400 else ''}")
        if show_meta:
            print(f"  META: {json.dumps(r.meta, ensure_ascii=False)}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Query de Certificaid RAG-index (ADR-006)")
    parser.add_argument("query", help="Zoekvraag")
    parser.add_argument("--bron-rol",
                        help="Kommagescheiden bron-rollen: wettekst,norm,advies (default: alle)")
    parser.add_argument("--concepten", action="store_true",
                        help="Zoek ook in concepten-collection")
    parser.add_argument("--n", type=int, default=5, help="Aantal resultaten (default: 5)")
    parser.add_argument("--rerank", action="store_true", help="Cross-encoder reranking")
    parser.add_argument("--expand", action="store_true",
                        help="Context-uitbreiding (±2 artikelen voor wetteksten)")
    parser.add_argument("--show-meta", action="store_true", help="Toon metadata")
    parser.add_argument("--chroma-path", help="Pad naar ChromaDB (default: data/rag/main)")
    args = parser.parse_args()

    chroma_path = Path(args.chroma_path) if args.chroma_path else ROOT / "data" / "rag" / "main"
    bron_rollen = [r.strip() for r in args.bron_rol.split(",")] if args.bron_rol else None
    selected_cols = BRONNEN_COLS + (["concepten"] if args.concepten else [])

    if args.rerank:
        query_with_rerank(args.query, selected_cols, bron_rollen, args.n, args.show_meta,
                          args.expand, chroma_path)
    else:
        query_simple(args.query, selected_cols, bron_rollen, args.n, args.show_meta, chroma_path)


if __name__ == "__main__":
    main()
