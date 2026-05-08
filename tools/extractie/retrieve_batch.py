"""
Batch-retrieval voor concept-extractie (ADR-008 §2.B).

Voert per vermoeden een 5-niveau multi-query retrieval uit:
  1. Programmaonderdeel-niveau   → brede context (PO-titel)
  2. Taakblok-niveau             → taken + doelstellingen van alle gelinkte taakblokken
  3. Kenniselementen-niveau      → ke-teksten voor codes in vermoeden.kenniselementen
                                   (overgeslagen als kenniselementen leeg is)
  4. Vermoeden-niveau            → naam + rationale
  5. Synoniemen                  → query-time expansion voor vocabulairekloven

Input: PO-niveau vermoedens-bestand (data/extractie/<po>/vermoedens/<po>.json).
Elk vermoeden heeft taakblokken[] (meerdere mogelijk), kenniselementen[], synoniemen[].
Output: JSON naar stdout — shallow copy van alle vermoeden-velden + chunks per vermoeden.

Gebruik:
  python tools/extractie/retrieve_batch.py \\
      --vermoedens data/extractie/4.0/vermoedens/4.0.json \\
      --programmaonderdeel data/programmaonderdelen/4.0-deontologie.json \\
      [--chroma data/chroma_db_4.0] \\
      [--bi-top-n 80] \\
      [--rerank-drempel 0.40] \\
      [--max-per-vermoeden 20] \\
      > data/extractie/4.0/retrieval/4.0.json
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
    taakblokken: list[dict],
    po_titel: str,
    ke_index: dict[str, str],
) -> list[str]:
    """
    Bouw de 5-niveau querylijst voor één vermoeden.
    taakblokken: alle PO-taakblok-dicts die bij dit vermoeden horen (kan meerdere zijn).
    Lege strings worden gefilterd zodat geen lege queries het model passeren.
    """
    queries: list[str] = []

    # Niveau 1: programmaonderdeel
    if po_titel:
        queries.append(po_titel)

    # Niveau 2: alle gelinkte taakblokken (taken + doelstellingen)
    for taakblok in taakblokken:
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

    # Niveau 5: LLM-gegenereerde synoniemen (query-time expansion)
    # Overbrugt vocabulairekloven (bv. "beroepsgeheim" ≠ "geheimen die toevertrouwd")
    for syn in vermoeden.get("synoniemen", []):
        syn = syn.strip()
        if syn:
            queries.append(syn)

    return queries


def _verzamel_kandidaten(
    sub_queries: list[str],
    cols: dict,
    bi_top_n: int,
) -> list:
    """
    Stap 1 (gedeeld): voer bi-encoder uit voor alle sub-queries, dedupliceer op
    chunk_id, bewaar het beste bi-score per chunk.
    """
    seen: dict[str, object] = {}
    for q in sub_queries:
        for r in _retrieve_candidates(cols, q, list(cols.keys()), bi_top_n):
            if r.chunk_id not in seen or r.score > seen[r.chunk_id].score:
                seen[r.chunk_id] = r
    return list(seen.values())


def bi_only_retrieve(
    sub_queries: list[str],
    cols: dict,
    bi_top_n: int,
    max_per_vermoeden: int,
) -> list:
    """
    Bi-encoder-only retrieval: geen cross-encoder reranking.
    Sorteert op bi-score. Snel: seconden per vermoeden.
    """
    kandidaten = _verzamel_kandidaten(sub_queries, cols, bi_top_n)
    return sorted(kandidaten, key=lambda r: r.score, reverse=True)[:max_per_vermoeden]


def single_pass_rerank(
    sub_queries: list[str],
    rerank_query: str,
    cols: dict,
    reranker,
    bi_top_n: int,
    max_per_vermoeden: int,
) -> list:
    """
    Single-pass reranking (ADR-008 §2.B):

    1. Bi-encoder op alle sub-queries → unieke kandidatenpool (~150–200 chunks)
    2. Cross-encoder eénmalig op de volledige unieke pool tegen rerank_query
       (= vermoeden naam, meest focale query)
    3. Sorteer op rerank-score, return top-N

    Voordeel vs. multi-query reranking:
      - Oud: 5 queries × 80 paren reranken = 400 cross-encoder calls/vermoeden
      - Nieuw: ~150–200 unieke paren reranken = 1× cross-encoder pass/vermoeden
      → ~3× minder werk → ~2–3 min op MPS voor 24 vermoedens

    Kwaliteitsvoordeel: de cross-encoder begrijpt de semantiek van het paar
    (query, chunk) en corrigeert zwakke bi-scores. Art. 458 SW scoort laag
    bij de bi-encoder voor 'Beroepsgeheim' (andere woordkeuze), maar de
    cross-encoder herkent de relatie wel.
    """
    kandidaten = _verzamel_kandidaten(sub_queries, cols, bi_top_n)
    if not kandidaten:
        return []

    paren = [(rerank_query, r.text) for r in kandidaten]
    scores = reranker.predict(paren)
    for r, s in zip(kandidaten, scores):
        r.rerank_score = float(s)

    kandidaten.sort(key=lambda r: r.rerank_score, reverse=True)
    return kandidaten[:max_per_vermoeden]


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
    Voer 5-niveau retrieval uit voor elk vermoeden (PO-niveau input).
    Elk vermoeden kan aan meerdere taakblokken hangen — alle worden meegenomen.
    Output-vermoedens zijn een shallow copy van de input + chunks-veld.
    """
    po_nr    = vermoedens_data.get("po", po_data.get("programmaonderdeel", ""))
    po_titel = po_data.get("titel", "")

    ke_index = bouw_ke_index(po_data)
    cols     = open_collections(client_chroma, ef, BRONNEN_COLS)

    if not cols:
        print(
            "⚠ Geen bronnen-collection gevonden in ChromaDB. "
            "Bouw de index eerst met tools/rag/rag_index.py.",
            file=sys.stderr,
        )
        sys.exit(1)

    output_vermoedens = []

    for vermoeden in vermoedens_data.get("vermoedens", []):
        naam = vermoeden.get("naam", "?")
        print(f"  → {naam} …", file=sys.stderr)

        # Verzamel alle gelinkte taakblok-dicts (vermoeden kan aan meerdere hangen)
        taakblok_codes = vermoeden.get("taakblokken", [])
        taakblokken = [
            tb for code in taakblok_codes
            if (tb := get_taakblok(po_data, code)) is not None
        ]

        sub_queries = bouw_sub_queries(vermoeden, taakblokken, po_titel, ke_index)

        if no_rerank:
            chunks = bi_only_retrieve(sub_queries, cols, bi_top_n, max_per_vermoeden)
            print(
                f"    {len(sub_queries)} queries → {len(chunks)} chunks (bi-only)",
                file=sys.stderr,
            )
        else:
            chunks = single_pass_rerank(
                sub_queries,
                rerank_query=naam,
                cols=cols,
                reranker=reranker,
                bi_top_n=bi_top_n,
                max_per_vermoeden=max_per_vermoeden,
            )
            print(
                f"    {len(sub_queries)} queries → {len(chunks)} chunks (single-pass rerank)",
                file=sys.stderr,
            )

        # Shallow copy van alle vermoeden-velden (ADR-008 §B-bis) + chunks
        output_vermoeden = {k: v for k, v in vermoeden.items()}
        output_vermoeden["chunks"] = [chunk_naar_dict(c) for c in chunks]
        output_vermoedens.append(output_vermoeden)

    return {
        "po":         po_nr,
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
        help="PO-niveau vermoedens-JSON (bijv. data/extractie/4.0/vermoedens/4.0.json)",
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
            "Default: single-pass reranking (bi-encoder pool + 1× cross-encoder per vermoeden)."
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
    # Voor single-pass reranking: gebruik MPS als beschikbaar, tenzij --device cpu
    # MPS is nodig voor acceptabele snelheid (~2–3 min vs. >15 min op CPU)
    no_rerank = args.no_rerank
    if args.device:
        device = args.device
    elif no_rerank:
        device = None   # cpu volstaat voor bi-only
    else:
        device = "mps"  # single-pass rerank: MPS verplicht
    modus = "bi-only" if no_rerank else f"single-pass rerank (device={device})"
    print(
        f"→ Retrieval-stack laden voor {n} vermoedens "
        f"(PO {vermoedens_data.get('po', '?')}, {modus}) …",
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
