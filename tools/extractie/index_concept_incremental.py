"""
Embed één concept-record en upsert in de `concepten` ChromaDB-collection (ADR-006).

Bedoeld voor twee situaties:
  1. Na elke nieuwe seed-write door de extractie-subagent (live duplicate-check).
  2. Bulk-(her)indexering van alle bestaande concept_records/*.json.

De te embedden tekst per concept = naam + node_type + main_rule.tekst (of definitie.tekst).
Metadata die opgeslagen wordt:
  - concept_id, naam, node_type, status, schema_version
  - edge_targets: komma-gescheiden lijst van edge-targets (voor walking)
  - bron_short: verkorte bronverwijzing uit main_rule.source.short

Gebruik:
  # Eén concept indexeren
  python tools/extractie/index_concept_incremental.py \\
      --concept data/concept_records/beroepsgeheim-gecertificeerd-accountant.json

  # Alle concepten (her)indexeren
  python tools/extractie/index_concept_incremental.py --alle

  # Drempelcheck: vergelijk query met alle concepten (duplicate-check preview)
  python tools/extractie/index_concept_incremental.py \\
      --duplicaat-check "Beroepsgeheim van de gecertificeerd accountant" \\
      [--drempel 0.80]

  Flags:
    --chroma    ChromaDB-pad (default: data/chroma_db)
    --dry-run   Toon wat geïndexeerd zou worden, schrijf niet naar ChromaDB
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
    RetrievalResult,
    EMBEDDING_MODEL,
    RERANKER_MODEL,
)

CONCEPT_DIR    = ROOT / "data" / "concept_records"
COLLECTIE_NAAM = "concepten"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def laad_concept(pad: Path) -> dict:
    return json.loads(pad.read_text(encoding="utf-8"))


def bouw_embed_tekst(record: dict) -> str:
    """
    Bouw de tekst die geëmbed wordt voor dit concept.
    Prioriteit: naam → node_type → main_rule/definitie-tekst.
    """
    delen = []

    naam = record.get("naam", "").strip()
    if naam:
        delen.append(naam)

    node_type = record.get("node_type", "").strip()
    if node_type:
        delen.append(f"({node_type})")

    # Haal kernregel of definitie op
    for veldnaam in ("main_rule", "definitie"):
        veld = record.get(veldnaam)
        if isinstance(veld, dict):
            tekst = veld.get("text", veld.get("tekst", "")).strip()
            if tekst:
                delen.append(tekst[:500])   # cap voor embedding-venster
                break
        elif isinstance(veld, str) and veld.strip():
            delen.append(veld.strip()[:500])
            break

    return " — ".join(delen) if delen else naam


def bouw_metadata(record: dict) -> dict:
    """Sla relevante metadata op naast de embedding."""
    edge_targets = [
        e.get("target", "") for e in record.get("edges", [])
        if e.get("target")
    ]
    bron_short = ""
    for veldnaam in ("main_rule", "definitie"):
        veld = record.get(veldnaam)
        if isinstance(veld, dict):
            bron_short = veld.get("source", {}).get("short", "")
            if bron_short:
                break

    return {
        "concept_id":    record.get("id", ""),
        "naam":          record.get("naam", ""),
        "node_type":     record.get("node_type", ""),
        "status":        record.get("status", ""),
        "schema_version": str(record.get("schema_version", "")),
        "edge_targets":  ",".join(edge_targets),
        "bron_short":    bron_short,
    }


# ---------------------------------------------------------------------------
# Indexering
# ---------------------------------------------------------------------------

def indexeer_concept(
    record: dict,
    collectie,
    *,
    droog: bool = False,
) -> str:
    """
    Embed en upsert één concept-record in de `concepten`-collection.
    Geeft het concept-id terug.
    """
    concept_id = record.get("id") or record.get("naam", "?")
    tekst      = bouw_embed_tekst(record)
    meta       = bouw_metadata(record)

    if droog:
        print(f"  [dry-run] zou indexeren: {concept_id!r}")
        print(f"    tekst: {tekst[:120]!r}")
        return concept_id

    collectie.upsert(
        ids=[concept_id],
        documents=[tekst],
        metadatas=[meta],
    )
    return concept_id


def open_of_maak_collectie(client, ef):
    """Open bestaande of maak nieuwe `concepten`-collection aan."""
    try:
        return client.get_collection(COLLECTIE_NAAM, embedding_function=ef)
    except Exception:
        return client.get_or_create_collection(COLLECTIE_NAAM, embedding_function=ef)


# ---------------------------------------------------------------------------
# Duplicate-check
# ---------------------------------------------------------------------------

def duplicate_check(
    query: str,
    collectie,
    reranker,
    *,
    drempel: float = 0.80,
    top_n: int = 10,
) -> list[dict]:
    """
    Embed een query-naam en zoek naar bestaande concepten met hoge gelijkenis.
    Geeft een lijst van kandidaten boven de drempel terug (gesorteerd op rerank_score).
    """
    count = collectie.count()
    if count == 0:
        return []

    res = collectie.query(
        query_texts=[query],
        n_results=min(top_n, count),
        include=["documents", "metadatas", "distances"],
    )

    kandidaten = []
    for doc, meta, dist, cid in zip(
        res["documents"][0], res["metadatas"][0],
        res["distances"][0], res["ids"][0],
    ):
        bi_score = round(1 - dist, 4)
        kandidaten.append({
            "concept_id":  cid,
            "naam":        meta.get("naam", ""),
            "bi_score":    bi_score,
            "text":        doc,
        })

    if not kandidaten:
        return []

    # Cross-encoder reranking
    paren = [(query, k["text"]) for k in kandidaten]
    scores = reranker.predict(paren)
    for k, s in zip(kandidaten, scores):
        k["rerank_score"] = round(float(s), 4)

    boven_drempel = [k for k in kandidaten if k["rerank_score"] >= drempel]
    boven_drempel.sort(key=lambda x: x["rerank_score"], reverse=True)
    return boven_drempel


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Embed één (of alle) concept-record(s) in de `concepten` ChromaDB-collection."
    )
    groep = parser.add_mutually_exclusive_group(required=True)
    groep.add_argument(
        "--concept",
        help="Pad naar een concept-record JSON (bijv. data/concept_records/beroepsgeheim.json)",
    )
    groep.add_argument(
        "--alle",
        action="store_true",
        help=f"Indexeer alle *.json in {CONCEPT_DIR.relative_to(ROOT)}",
    )
    groep.add_argument(
        "--duplicaat-check",
        metavar="NAAM",
        help="Controleer of een conceptnaam al bestaat in de collection (geen upsert)",
    )
    parser.add_argument(
        "--chroma",
        default=None,
        help="ChromaDB-pad (default: data/chroma_db)",
    )
    parser.add_argument(
        "--drempel",
        type=float,
        default=0.80,
        help="Rerank-drempel voor duplicaat-check (default: 0.80)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Toon wat geïndexeerd zou worden, schrijf niet",
    )
    args = parser.parse_args()

    chroma_pad = Path(args.chroma) if args.chroma else ROOT / "data" / "chroma_db"

    print("→ Retrieval-stack laden …", file=sys.stderr)
    client, ef, reranker = build_retrieval_stack(chroma_pad)
    collectie = open_of_maak_collectie(client, ef)

    # --- Duplicaat-check modus ---
    if args.duplicaat_check:
        query = args.duplicaat_check
        print(f"→ Duplicaat-check voor: {query!r}", file=sys.stderr)
        kandidaten = duplicate_check(
            query, collectie, reranker, drempel=args.drempel
        )
        if kandidaten:
            print(f"  {len(kandidaten)} kandidaat(en) boven drempel {args.drempel}:")
            for k in kandidaten:
                print(f"    [{k['rerank_score']:.3f}] {k['naam']!r} (id: {k['concept_id']})")
        else:
            print(f"  Geen duplicaten gevonden boven drempel {args.drempel}.")
        return

    # --- Indexeer één of alle concepten ---
    if args.alle:
        if not CONCEPT_DIR.exists():
            print(f"Concept_records-map niet gevonden: {CONCEPT_DIR}", file=sys.stderr)
            sys.exit(1)
        bestanden = sorted(CONCEPT_DIR.glob("*.json"))
        if not bestanden:
            print("Geen concept-records gevonden.", file=sys.stderr)
            sys.exit(0)
        print(f"→ {len(bestanden)} concept(en) indexeren …", file=sys.stderr)
    else:
        pad = Path(args.concept)
        if not pad.exists():
            print(f"Bestand niet gevonden: {pad}", file=sys.stderr)
            sys.exit(1)
        bestanden = [pad]

    geindexeerd = 0
    for bestand in bestanden:
        try:
            record = laad_concept(bestand)
        except Exception as e:
            print(f"  Fout bij laden {bestand.name}: {e}", file=sys.stderr)
            continue

        concept_id = indexeer_concept(record, collectie, droog=args.dry_run)
        print(f"  {'[dry]' if args.dry_run else '✓'} {concept_id}")
        geindexeerd += 1

    actie = "zou indexeren" if args.dry_run else "geïndexeerd"
    print(f"\n{geindexeerd} concept(en) {actie}.", file=sys.stderr)

    if not args.dry_run:
        print(
            f"  Collectie '{COLLECTIE_NAAM}' bevat nu {collectie.count()} record(s).",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
