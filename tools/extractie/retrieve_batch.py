"""
Batch-retrieval voor concept-extractie (ADR-008 §2.B).

Voert per vermoeden een 4-niveau multi-query retrieval uit:
  1. Programmaonderdeel-niveau   → brede context (PO-titel)
  2. Taakblok-niveau             → taken + doelstellingen van het taakblok
  3. Kenniselementen-niveau      → ke-teksten voor codes in vermoeden.kenniselementen
                                   (overgeslagen als kenniselementen leeg is)
  4. Vermoeden-niveau            → naam + rationale

Eén bge-m3 model-load voor alle queries.
Output: JSON naar stdout (chunks per vermoeden, gesorteerd op rerank_score).

Gebruik:
  python tools/extractie/retrieve_batch.py \\
      --vermoedens data/extractie/4.0/vermoedens/4.0.D1.1.json \\
      --programmaonderdeel data/programmaonderdelen/4.0-deontologie.json \\
      [--chroma data/chroma_db_4.0] \\
      [--bi-top-n 80] \\
      [--rerank-drempel 0.40] \\
      [--max-per-vermoeden 20] \\
      > data/extractie/4.0/retrieval/4.0.D1.1.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from lib.retrieval import (
    build_retrieval_stack,
    open_collections,
    multi_query_retrieve,
    _retrieve_candidates,
    BRONNEN_COLS,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def laad_programmaonderdeel(pad: Path) -> dict:
    return json.loads(pad.read_text(encoding="utf-8"))


def bouw_ke_index(po_data: dict) -> dict[str, str]:
    """
    Bouw een platte code→tekst-index van alle kenniselementen in de PO-JSON.
    Zowel toplevel-items als subitems worden opgenomen.
    """
    index: dict[str, str] = {}
    for ke in po_data.get("kenniselementen", []):
        code = ke.get("code", "")
        tekst = ke.get("tekst", "")
        if code:
            index[code] = tekst
        for sub in ke.get("subitems", []):
            scode = sub.get("code", "")
            stekst = sub.get("tekst", "")
            if scode:
                index[scode] = stekst
    return index


def get_taakblok(po_data: dict, code: str) -> dict | None:
    for tb in po_data.get("taakblokken", []):
        if tb.get("code") == code:
            return tb
    return None


def bouw_sub_queries(
    vermoeden: dict,
    taakblok: dict | None,
    po_titel: str,
    ke_index: dict[str, str],
) -> list[str]:
    """
    Bouw de 4-niveau querylijst voor één vermoeden.
    Lege strings worden gefilterd zodat geen lege queries het model passeren.
    """
    queries: list[str] = []

    # Niveau 1: programmaonderdeel
    if po_titel:
        queries.append(po_titel)

    # Niveau 2: taakblok (taken + doelstellingen)
    if taakblok:
        for t in taakblok.get("taken", []):
            tekst = t.get("tekst", "").strip()
            if tekst:
                queries.append(tekst)
        for d in taakblok.get("doelstellingen", []):
            tekst = d.get("tekst", "").strip()
            if tekst:
                queries.append(tekst)

    # Niveau 3: kenniselementen (optioneel — leeg is geldig)
    for code in vermoeden.get("kenniselementen", []):
        ke_tekst = ke_index.get(code, "").strip()
        if ke_tekst:
            queries.append(ke_tekst)

    # Niveau 4: vermoeden zelf
    naam = vermoeden.get("naam", "").strip()
    if naam:
        queries.append(naam)
    rationale = vermoeden.get("rationale", "").strip()
    if rationale:
        queries.append(rationale)

    return queries


def bi_only_retrieve(
    sub_queries: list[str],
    cols: dict,
    bi_top_n: int,
    max_per_vermoeden: int,
) -> list:
    """
    Bi-encoder-only retrieval: geen cross-encoder reranking.
    Verzamelt kandidaten over alle sub-queries, dedupliceert op chunk_id,
    sorteert op bi-score (cosine-similarity). Snel: seconden ipv minuten.
    """
    seen: dict[str, object] = {}  # chunk_id → best RetrievalResult
    for q in sub_queries:
        kandidaten = _retrieve_candidates(cols, q, list(cols.keys()), bi_top_n)
        for r in kandidaten:
            if r.chunk_id not in seen or r.score > seen[r.chunk_id].score:
                seen[r.chunk_id] = r
    resultaten = sorted(seen.values(), key=lambda r: r.score, reverse=True)
    return resultaten[:max_per_vermoeden]


def chunk_naar_dict(chunk) -> dict:
    """Converteer een RetrievalResult naar een serialiseerbaar dict."""
    return {
        "chunk_id":     chunk.chunk_id,
        "bron":         chunk.bron,
        "artikel":      chunk.artikel,
        "bron_rol":     chunk.meta.get("bron_rol", ""),
        "rerank_score": round(chunk.rerank_score, 4),
        "bi_score":     round(chunk.score, 4),
        "text":         chunk.text,
    }


# ---------------------------------------------------------------------------
# Hoofdlogica
# ---------------------------------------------------------------------------

def verwerk_vermoedens(
    vermoedens_data: dict,
    po_data: dict,
    client_chroma,
    ef,
    reranker,
    *,
    bi_top_n: int = 80,
    rerank_drempel: float = 0.40,
    max_per_vermoeden: int = 20,
    no_rerank: bool = False,
) -> dict:
    """
    Voer 4-niveau retrieval uit voor elk vermoeden.
    Geeft een output-dict terug klaar voor JSON-serialisatie.
    """
    taakblok_code = vermoedens_data.get("taakblok", "")
    po_nr         = po_data.get("programmaonderdeel", "")
    po_titel      = po_data.get("titel", "")

    ke_index  = bouw_ke_index(po_data)
    taakblok  = get_taakblok(po_data, taakblok_code)
    cols      = open_collections(client_chroma, ef, BRONNEN_COLS)

    if not cols:
        print(
            f"⚠ Geen bronnen-collection gevonden in ChromaDB. "
            f"Bouw de index eerst met tools/rag/rag_index.py.",
            file=sys.stderr,
        )
        sys.exit(1)

    output_vermoedens = []

    for vermoeden in vermoedens_data.get("vermoedens", []):
        naam = vermoeden.get("naam", "?")
        print(f"  → {naam} …", file=sys.stderr)

        sub_queries = bouw_sub_queries(vermoeden, taakblok, po_titel, ke_index)

        if no_rerank:
            chunks = bi_only_retrieve(sub_queries, cols, bi_top_n, max_per_vermoeden)
            print(
                f"    {len(sub_queries)} queries → {len(chunks)} chunks (bi-only)",
                file=sys.stderr,
            )
        else:
            chunks = multi_query_retrieve(
                sub_queries,
                cols,
                BRONNEN_COLS,
                reranker,
                bi_top_n=bi_top_n,
                rerank_threshold=rerank_drempel,
                max_per_query=max_per_vermoeden,
                expand_context=True,
            )
            print(
                f"    {len(sub_queries)} queries → {len(chunks)} chunks "
                f"(rerank ≥ {rerank_drempel})",
                file=sys.stderr,
            )

        output_vermoedens.append({
            "naam":             naam,
            "node_type":        vermoeden.get("node_type", ""),
            "rationale":        vermoeden.get("rationale", ""),
            "kenniselementen":  vermoeden.get("kenniselementen", []),
            "schaal_signaal":   vermoeden.get("schaal_signaal", ""),
            "chunks":           [chunk_naar_dict(c) for c in chunks],
        })

    return {
        "po":         po_nr,
        "taakblok":   taakblok_code,
        "vermoedens": output_vermoedens,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "4-niveau batch-retrieval per vermoeden (ADR-008). "
            "Output: JSON naar stdout."
        )
    )
    parser.add_argument(
        "--vermoedens",
        required=True,
        help="Vermoedens-JSON (na normalize_vermoedens.py)",
    )
    parser.add_argument(
        "--programmaonderdeel",
        required=True,
        help="Programmaonderdeel-JSON (bijv. data/programmaonderdelen/4.0-deontologie.json)",
    )
    parser.add_argument(
        "--chroma",
        default=None,
        help="ChromaDB-pad (default: data/chroma_db)",
    )
    parser.add_argument(
        "--bi-top-n",
        type=int,
        default=80,
        help="Bi-encoder top-N per query (default: 80)",
    )
    parser.add_argument(
        "--rerank-drempel",
        type=float,
        default=0.40,
        help="Minimale rerank-score (default: 0.40)",
    )
    parser.add_argument(
        "--max-per-vermoeden",
        type=int,
        default=20,
        help="Max chunks per vermoeden in output (default: 20)",
    )
    parser.add_argument(
        "--device",
        default=None,
        help="Device voor embedding + reranker: mps | cuda | cpu (default: cpu via retrieval.py)",
    )
    parser.add_argument(
        "--no-rerank",
        action="store_true",
        help=(
            "Sla cross-encoder reranking over — enkel bi-encoder (snel, seconden/vermoeden). "
            "Aanbevolen voor batch-runs; de extractie-subagent doet eigen relevantie-oordeel."
        ),
    )
    args = parser.parse_args()

    vermoedens_pad = Path(args.vermoedens)
    po_pad         = Path(args.programmaonderdeel)
    chroma_pad     = Path(args.chroma) if args.chroma else ROOT / "data" / "chroma_db"

    if not vermoedens_pad.exists():
        print(f"Vermoedens-bestand niet gevonden: {vermoedens_pad}", file=sys.stderr)
        sys.exit(1)
    if not po_pad.exists():
        print(f"Programmaonderdeel-JSON niet gevonden: {po_pad}", file=sys.stderr)
        sys.exit(1)

    vermoedens_data = json.loads(vermoedens_pad.read_text(encoding="utf-8"))
    po_data         = json.loads(po_pad.read_text(encoding="utf-8"))

    n = len(vermoedens_data.get("vermoedens", []))
    device    = args.device  # None = default (cpu) uit retrieval.py
    no_rerank = args.no_rerank
    modus     = "bi-only (geen reranker)" if no_rerank else f"bi+rerank, device={device or 'cpu'}"
    print(
        f"→ Retrieval-stack laden voor {n} vermoedens "
        f"(taakblok {vermoedens_data.get('taakblok', '?')}, {modus}) …",
        file=sys.stderr,
    )

    client_chroma, ef, reranker = build_retrieval_stack(chroma_pad, device=device)

    result = verwerk_vermoedens(
        vermoedens_data,
        po_data,
        client_chroma,
        ef,
        reranker,
        bi_top_n=args.bi_top_n,
        rerank_drempel=args.rerank_drempel,
        max_per_vermoeden=args.max_per_vermoeden,
        no_rerank=no_rerank,
    )

    # Schrijf JSON naar stdout; progress naar stderr
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
