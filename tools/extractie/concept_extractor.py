"""
Concept extractor: genereert een rijke concept record JSON vanuit:
  1. TDK-anker (uit PO-fiche) — definieert WAT de student moet kennen
  2. RAG retrieval over bronnen (wetteksten, normen, adviezen) — primaire bronnen
  3. Claude Sonnet 4.6 — synthetiseert het concept record

Output: data/concept_records/<id>.json

Gebruik:
  python tools/extractie/concept_extractor.py --concept "btw-belastingplicht" --po 2.4
  python tools/extractie/concept_extractor.py --concept "meldingsplicht-aww" --po 4.0 --tdk-tekst "Meldingsplicht bij vermoeden van WG/FT"
  python tools/extractie/concept_extractor.py --concept "btw-belastingplicht" --po 2.4 --dry-run
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from datetime import date

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import anthropic

ROOT = Path(__file__).resolve().parent.parent.parent
CHROMA_PATH = ROOT / "data" / "chroma_db"
OUTPUT_DIR = ROOT / "data" / "concept_records"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
CLAUDE_MODEL = "claude-sonnet-4-6"

EXCEPTION_SIGNALS = ["tenzij", "behalve", "uitzondering", "in afwijking van",
                     "uitgezonderd", "niet van toepassing", "sauf", "exception"]


# ---------------------------------------------------------------------------
# RAG retrieval
# ---------------------------------------------------------------------------

def get_rag_client():
    ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    return client, ef


def retrieve(client, ef, query: str, collections: list[str], n: int = 5) -> list[dict]:
    """Query meerdere collections en return top-N chunks gesorteerd op score."""
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
        except Exception as e:
            print(f"  ⚠️  Collection '{name}' query mislukt: {e}")

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:n * len(collections)]


def retrieve_for_concept(client, ef, concept_naam: str, tdk_tekst: str,
                          n_per_query: int = 6) -> dict[str, list[dict]]:
    """Voer 4 gerichte queries uit voor een concept."""
    bronnen_cols = ["wetteksten", "normen", "adviezen"]
    tdk_cols = ["tdks"]
    alle_cols = bronnen_cols + ["bestaande_fiches"]

    queries = {
        "definitie_scope": retrieve(client, ef,
            f"{concept_naam} definitie toepassingsgebied {tdk_tekst}", alle_cols, n_per_query),
        "uitzonderingen": retrieve(client, ef,
            f"{concept_naam} uitzondering tenzij behalve in afwijking van", bronnen_cols, n_per_query),
        "procedure": retrieve(client, ef,
            f"{concept_naam} procedure verplichting stappen", bronnen_cols, n_per_query),
        "voorbeelden": retrieve(client, ef,
            f"{concept_naam} voorbeeld praktijk geval", alle_cols, n_per_query),
        "tdk_context": retrieve(client, ef,
            f"{concept_naam} {tdk_tekst}", tdk_cols, 4),
    }
    return queries


def format_chunks_for_prompt(chunks: list[dict], max_chars: int = 2000) -> str:
    """Formatteer RAG-chunks als leesbare context voor Claude."""
    parts = []
    total = 0
    for i, chunk in enumerate(chunks, 1):
        bron_ref = f"{chunk['bron']}"
        if chunk.get("artikel"):
            bron_ref += f" — {chunk['artikel']}"
        text = chunk["text"][:800]  # max per chunk
        part = f"[{i}] {bron_ref} (score: {chunk['score']})\n{text}"
        if total + len(part) > max_chars:
            break
        parts.append(part)
        total += len(part)
    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# Claude prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """Je bent een juridisch-boekhoudkundige expert die concept records maakt voor het ITAA-bekwaamheidsexamen.

Je taak: extraheer gestructureerde kennis over een concept uit de aangeleverde bronnen.

REGELS:
1. Elke claim krijgt confidence: "grounded" als ze direct uit een bron komt, "inferred" als het een redenering is.
2. Verzin NOOIT feiten zonder bronverwijzing. Liever een leeg veld dan een onzekere claim.
3. Uitzonderingen zijn het meest getoetst op het examen — wees hier zo volledig mogelijk.
4. Het schema is uitbreidbaar — voeg extra velden toe als de bronnen dat rechtvaardigen.
5. Alle velden zijn Nederlandstalig.
6. Schrijf beknopt maar volledig. Geen herhaling van de conceptnaam in elke zin."""


def build_extraction_prompt(concept_naam: str, po_nr: str, tdk_tekst: str,
                              retrieved: dict[str, list[dict]]) -> str:
    def_scope = format_chunks_for_prompt(retrieved["definitie_scope"], 2500)
    uitz = format_chunks_for_prompt(retrieved["uitzonderingen"], 2000)
    proc = format_chunks_for_prompt(retrieved["procedure"], 1500)
    vb = format_chunks_for_prompt(retrieved["voorbeelden"], 1500)
    tdk = format_chunks_for_prompt(retrieved["tdk_context"], 800)

    return f"""Maak een concept record voor: **{concept_naam}**
Programmaonderdeel: {po_nr}
TDK-anker: {tdk_tekst}

---
## TDK-context (wat moet de student kennen?)
{tdk}

---
## Definitie & toepassingsgebied (bronnen)
{def_scope}

---
## Uitzonderingen (bronnen)
{uitz}

---
## Procedure & verplichtingen (bronnen)
{proc}

---
## Voorbeelden uit de praktijk (bronnen)
{vb}

---
Genereer nu een volledig concept record als geldig JSON. Gebruik dit schema:

{{
  "id": "concept:{concept_naam}",
  "naam": "{concept_naam}",
  "po_ref": ["{po_nr}"],
  "tdk_anker": "{tdk_tekst}",
  "main_rule": {{
    "text": "De hoofdregel in 1-3 zinnen",
    "sources": [{{"ref": "WBTW art. X", "chunk_id": "..."}}],
    "confidence": "grounded"
  }},
  "exceptions": [
    {{
      "naam": "Korte naam van de uitzondering",
      "text": "Beschrijving van de uitzondering",
      "sources": [{{"ref": "wet art. X"}}],
      "confidence": "grounded"
    }}
  ],
  "scope": {{
    "applies_to": "Op wie/wat is het concept van toepassing?",
    "excludes": "Wie/wat is uitdrukkelijk uitgesloten?",
    "sources": [{{"ref": "..."}}]
  }},
  "obligations": [
    {{
      "text": "Verplichting",
      "sources": [{{"ref": "..."}}],
      "confidence": "grounded"
    }}
  ],
  "pitfalls": [
    {{
      "text": "Typische verkeerde aanname van studenten",
      "confidence": "inferred"
    }}
  ],
  "examples": [
    {{
      "text": "Concreet voorbeeld",
      "context": "context:horeca of context:vrij-beroep (indien van toepassing)",
      "sources": [{{"ref": "..."}}],
      "confidence": "grounded"
    }}
  ],
  "related_concepts": ["concept:naam-ander-concept"],
  "temporal": {{
    "valid_from": "...",
    "note": "Gewijzigd door wet X"
  }},
  "confidence": 0.85
}}

Geef enkel de JSON terug, zonder uitleg of markdown code blocks."""


# ---------------------------------------------------------------------------
# Extractor
# ---------------------------------------------------------------------------

def extract_concept(concept_naam: str, po_nr: str, tdk_tekst: str,
                     dry_run: bool = False) -> dict | None:
    print(f"\n{'='*60}")
    print(f"Concept: {concept_naam}  |  PO: {po_nr}")
    print(f"TDK: {tdk_tekst}")

    # RAG retrieval
    print("  → RAG retrieval...")
    client, ef = get_rag_client()
    retrieved = retrieve_for_concept(client, ef, concept_naam, tdk_tekst)

    total_chunks = sum(len(v) for v in retrieved.values())
    print(f"  → {total_chunks} chunks opgehaald")

    if dry_run:
        print("  → DRY RUN: geen Claude-call")
        return None

    # Claude generatie
    print("  → Claude generatie...")
    api_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    prompt = build_extraction_prompt(concept_naam, po_nr, tdk_tekst, retrieved)

    message = api_client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )

    raw_response = message.content[0].text.strip()

    # Parse JSON
    # Verwijder markdown code blocks als aanwezig
    raw_response = re.sub(r"^```(?:json)?\s*", "", raw_response)
    raw_response = re.sub(r"\s*```$", "", raw_response)

    try:
        record = json.loads(raw_response)
    except json.JSONDecodeError as e:
        print(f"  ❌ JSON parse mislukt: {e}")
        print(f"  Eerste 200 chars van response: {raw_response[:200]}")
        return None

    # Voeg metadata toe
    record["generated_at"] = date.today().isoformat()
    record["source_queries"] = {
        k: [{"bron": c["bron"], "artikel": c["artikel"], "score": c["score"]}
            for c in v[:3]]
        for k, v in retrieved.items()
    }

    return record


def save_record(record: dict, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    concept_id = record["id"].replace("concept:", "")
    # Verwijder speciale tekens voor bestandsnaam
    safe_name = re.sub(r"[^a-zA-Z0-9\-_]", "-", concept_id)
    path = output_dir / f"{safe_name}.json"
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2))
    print(f"  ✓ Opgeslagen: {path.relative_to(ROOT)}")
    return path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Extraheer een concept record via RAG + Claude")
    parser.add_argument("--concept", required=True,
                        help="Concept-naam (bv. 'btw-belastingplicht')")
    parser.add_argument("--po", required=True,
                        help="PO-nummer (bv. '2.4')")
    parser.add_argument("--tdk-tekst", default="",
                        help="TDK-anker tekst uit de PO-fiche")
    parser.add_argument("--dry-run", action="store_true",
                        help="Toon retrieved chunks, geen Claude-call")
    parser.add_argument("--show-chunks", action="store_true",
                        help="Toon de retrieved chunks bij dry-run")
    args = parser.parse_args()

    record = extract_concept(args.concept, args.po, args.tdk_tekst, args.dry_run)

    if record is not None:
        path = save_record(record, OUTPUT_DIR)
        print(f"\n✓ Concept record aangemaakt: {path.name}")
        # Toon samenvatting
        print(f"  main_rule: {record.get('main_rule', {}).get('text', '?')[:80]}...")
        n_exc = len(record.get("exceptions", []))
        n_pit = len(record.get("pitfalls", []))
        n_ex = len(record.get("examples", []))
        print(f"  uitzonderingen: {n_exc}, valkuilen: {n_pit}, voorbeelden: {n_ex}")
        print(f"  confidence: {record.get('confidence', '?')}")


if __name__ == "__main__":
    main()
