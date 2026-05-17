"""
Exporteer de bundel van één anchor met volledige chunk-teksten — input voor
de per-anchor concept-extractie subagent (ADR-008 fase C).

Leest de bundle uit de SQLite matches-store (ADR-005 §9.1).

Output: data/extractie/<po>/bundles/<po>-<anchor-id-slug>.json
met:
  - anchor info (tekst, verbose, synoniemen)
  - bundle: lijst van chunks met chunk_id, bron, sectie, score, EN volle tekst

Gebruik:
  python3 -m tools.extractie.export_bundle --po 4.0 --anchor-id 4.0.I.D.7
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

from tools.lib.matches_store import DEFAULT_DB_PATH, open_store, get_bundle

ROOT = Path(__file__).resolve().parent.parent.parent
EMBEDDING_MODEL = "BAAI/bge-m3"
DEFAULT_ANCHORS_PATH = ROOT / "data" / "programma" / "anchors.json"


def slugify(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9.-]+", "-", s).strip("-")


_BRON_DIRS = (
    ROOT / "resources" / "bronnen" / "wetteksten",
    ROOT / "resources" / "bronnen" / "normen",
    ROOT / "resources" / "bronnen" / "adviezen",
)


def _warn_if_store_stale(db_path: Path) -> None:
    """
    Loud-warning als de SQLite-store ouder is dan een trusted bron-MD.

    Implementeert de ADR-005 §9 refresh-gate als runtime-sanity-check. Blokkeert
    de export niet (soms wil je expliciet een oude store gebruiken) maar maakt
    zichtbaar dat je extractie mogelijk stale input draait.
    """
    try:
        store_mtime = db_path.stat().st_mtime
    except FileNotFoundError:
        return

    newer: list[str] = []
    for d in _BRON_DIRS:
        if not d.exists():
            continue
        for f in d.glob("*.md"):
            if f.name in {"INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"}:
                continue
            try:
                if f.stat().st_mtime > store_mtime:
                    newer.append(f.name)
            except FileNotFoundError:
                continue

    if newer:
        sample = ", ".join(sorted(newer)[:5])
        suffix = "" if len(newer) <= 5 else f" (+{len(newer) - 5} meer)"
        print(
            f"[bundle][WAARSCHUWING] {len(newer)} bron-MD's zijn nieuwer dan "
            f"de matches-store {db_path.name}: {sample}{suffix}.\n"
            f"[bundle]                ADR-005 §9 refresh-gate: draai "
            f"`python3 -m tools.etl.refresh_rag_and_matches` voor je nieuwe "
            f"extracties start, anders zit deze bundel mogelijk niet meer "
            f"synchroon met de trust-state."
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--po", required=True)
    parser.add_argument("--anchor-id", required=True)
    parser.add_argument(
        "--db-path",
        default=None,
        help="pad naar SQLite matches-store (default: data/extractie/matches.sqlite3)",
    )
    parser.add_argument("--anchors-file", default=None,
                        help="optioneel: enriched/clean anchors-bestand (voor verbose+syns)")
    parser.add_argument("--chroma-path", default=None,
                        help="default: data/rag/main")
    args = parser.parse_args()

    db_path = Path(args.db_path) if args.db_path else DEFAULT_DB_PATH
    if not db_path.is_absolute():
        db_path = ROOT / db_path

    _warn_if_store_stale(db_path)

    conn = open_store(db_path)
    bundle_chunks = get_bundle(conn, args.anchor_id)
    conn.close()

    if not bundle_chunks:
        raise SystemExit(
            f"Anchor {args.anchor_id} heeft geen bundle in {db_path}. "
            "Controleer of match_bronnen.py gedraaid heeft."
        )

    bundle_chunk_ids = [chunk_id for chunk_id, _score in bundle_chunks]
    bundle_scores = {chunk_id: score for chunk_id, score in bundle_chunks}

    print(f"[bundle] {len(bundle_chunk_ids)} chunks voor {args.anchor_id}")

    # Haal volle tekst op uit ChromaDB
    chroma_path = Path(args.chroma_path) if args.chroma_path else (ROOT / "data" / "rag" / "main")
    if not chroma_path.is_absolute():
        chroma_path = ROOT / chroma_path
    if not chroma_path.exists():
        chroma_path = ROOT / "data" / "rag" / "main"

    client = chromadb.PersistentClient(path=str(chroma_path))
    ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL, device="cpu")
    col = client.get_collection("bronnen", embedding_function=ef)

    # Batch-fetch
    res = col.get(ids=bundle_chunk_ids, include=["documents", "metadatas"])
    by_id = {cid: (doc, meta) for cid, doc, meta in zip(res["ids"], res["documents"], res["metadatas"])}

    # Optioneel: enriched anchors-bestand voor verbose + synoniemen
    anchor_meta: dict = {}
    anchors_file = Path(args.anchors_file) if args.anchors_file else DEFAULT_ANCHORS_PATH
    if not anchors_file.is_absolute():
        anchors_file = ROOT / anchors_file
    if anchors_file.exists():
        for a in json.loads(anchors_file.read_text(encoding="utf-8"))["anchors"]:
            if a["anchor_id"] == args.anchor_id:
                anchor_meta = {
                    "tekst": a.get("tekst", ""),
                    "anchor_type": a.get("anchor_type", ""),
                    "verbose": a.get("verbose", ""),
                    "synoniemen": a.get("synoniemen", []),
                }
                break

    # Bouw output: bundle items met volle tekst, gesorteerd op score (hoog → laag)
    bundle_with_text = []
    for chunk_id in bundle_chunk_ids:
        if chunk_id in by_id:
            doc, meta = by_id[chunk_id]
            bundle_with_text.append({
                "chunk_id": chunk_id,
                "chunk_sha": meta.get("chunk_sha"),
                "bron": meta.get("bron", ""),
                "bron_rol": meta.get("bron_rol", ""),
                "sectie": meta.get("sectie") or meta.get("artikel_ref", ""),
                "score": bundle_scores[chunk_id],
                "text": doc,
            })

    out = {
        "po": args.po,
        "anchor_id": args.anchor_id,
        "anchor": anchor_meta or {
            "tekst": "",
            "anchor_type": "",
            "verbose": "",
            "synoniemen": [],
        },
        "matches_source": str(db_path.relative_to(ROOT)),
        "bundle_size": len(bundle_with_text),
        "bundle": bundle_with_text,
    }

    out_dir = ROOT / "data" / "extractie" / args.po / "bundles"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.po}-{slugify(args.anchor_id)}.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    total_chars = sum(len(c["text"]) for c in bundle_with_text)
    print(f"[output] {out_path.relative_to(ROOT)}")
    print(f"         {len(bundle_with_text)} chunks, ~{total_chars:,} chars (~{total_chars // 4:,} tokens)")


if __name__ == "__main__":
    main()
