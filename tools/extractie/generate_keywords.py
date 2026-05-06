"""
Genereer chunk-level semantische keywords voor wetteksten (ADR-004, ADR-012).

Gebruikt KeyBERT met BAAI/bge-m3 als backbone — volledig lokaal, geen API-kosten.
Keywords worden prepended aan de chunk-tekst bij indexering zodat de embedding
semantisch rijker is (zie rag_index.py: _prepend_keywords).

Gebruik:
  python tools/extractie/generate_keywords.py                        # alle wetteksten
  python tools/extractie/generate_keywords.py --source Antiwitwaswet-2017
  python tools/extractie/generate_keywords.py --priority             # AWW, WIB92, WBTW, WVV, Wet-ITAA, WER, ...
  python tools/extractie/generate_keywords.py --dry-run              # toon chunks zonder keywords te genereren

Installatie (eenmalig):
  pip3 install keybert

Vereisten:
  - BAAI/bge-m3 al gedownload (automatisch als rag_index.py eerder gedraaid is)
  - sentence-transformers >= 3.0.0
"""

import argparse
import json
import re
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent.parent
KEYWORDS_DIR = ROOT / "resources" / "bronnen" / "wetteksten" / "keywords"
WETTEKSTEN_DIR = ROOT / "resources" / "bronnen" / "wetteksten"

EMBEDDING_MODEL = "BAAI/bge-m3"

# Wetteksten die het meest bevraagd worden op het examen
PRIORITY_SOURCES = [
    "Antiwitwaswet-2017",
    "WIB92",
    "WBTW",
    "WVV",
    "Wet-ITAA-2019",
    "WER",
    "KB-WVV-2019",
    "KB-21-10-2018",
    "Wetboek-Invordering",
    "WDRT",
]


def _chunk_wettekst(path: Path) -> list[dict]:
    """Splits een wettekst-bestand in artikel-chunks (zelfde logica als rag_index.py)."""
    try:
        post = frontmatter.load(str(path))
    except Exception as e:
        print(f"  ⚠️  Kon {path.name} niet laden: {e}")
        return []

    content = post.content
    chunks = []
    current_heading = ""
    current_lines = []

    for line in content.split("\n"):
        if re.match(r"^#{1,4} ", line):
            if current_lines and current_heading:
                body = "\n".join(current_lines).strip()
                if len(body) >= 80:
                    chunks.append({"heading": current_heading, "body": body[:800]})
            stripped = line.lstrip("#").strip()
            if re.match(r"^(HOOFDSTUK|AFDELING|TITEL|DEEL|BOEK|SECTIE)", stripped, re.I):
                current_heading = ""
            else:
                current_heading = stripped
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines and current_heading:
        body = "\n".join(current_lines).strip()
        if len(body) >= 80:
            chunks.append({"heading": current_heading, "body": body[:800]})

    return chunks


def load_keybert_model():
    """Laad KeyBERT met bge-m3 als backbone."""
    try:
        from keybert import KeyBERT
        from sentence_transformers import SentenceTransformer
    except ImportError:
        print("❌ KeyBERT niet geïnstalleerd. Installeer via: pip3 install keybert")
        sys.exit(1)

    print(f"  → KeyBERT laden met {EMBEDDING_MODEL}...")
    sentence_model = SentenceTransformer(EMBEDDING_MODEL)
    return KeyBERT(model=sentence_model)


def generate_keywords_for_chunk(kw_model, text: str, top_n: int = 8) -> list[str]:
    """
    Extraheer keywords uit een chunk-tekst via KeyBERT.
    Combineert 1-gram en 2-gram keyphrases.
    """
    # KeyBERT vindt keyphrases die semantisch het meest op de hele tekst lijken
    keywords_1gram = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 1),
        stop_words=None,
        top_n=top_n // 2,
    )
    keywords_2gram = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words=None,
        top_n=top_n // 2,
    )

    # Combineer en dedupliceer
    seen = set()
    result = []
    for kw, _ in keywords_1gram + keywords_2gram:
        kw_clean = kw.strip().lower()
        if kw_clean not in seen and len(kw_clean) > 2:
            seen.add(kw_clean)
            result.append(kw.strip())

    return result[:top_n]


def generate_keywords_for_file(
    path: Path,
    kw_model,
    dry_run: bool = False,
) -> dict:
    """Genereer keywords voor alle chunks in één wettekst-bestand."""
    chunks = _chunk_wettekst(path)
    if not chunks:
        print(f"  Geen chunks gevonden in {path.name}")
        return {}

    print(f"  {len(chunks)} chunks te verwerken...")

    if dry_run:
        return {c["heading"]: ["[dry-run]"] for c in chunks}

    keywords_map = {}
    for i, chunk in enumerate(chunks):
        try:
            kws = generate_keywords_for_chunk(kw_model, chunk["body"])
            keywords_map[chunk["heading"]] = kws
        except Exception as e:
            print(f"  ⚠️  Chunk {i+1} ({chunk['heading'][:30]}): {e}")

        # Voortgang tonen elke 25 chunks
        if (i + 1) % 25 == 0:
            print(f"    {i + 1}/{len(chunks)} chunks verwerkt...")

    return keywords_map


def save_keywords(stem: str, keywords_map: dict) -> Path:
    """Sla keywords op als JSON in de keywords-map."""
    KEYWORDS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = KEYWORDS_DIR / f"{stem}.json"
    out_path.write_text(json.dumps(keywords_map, ensure_ascii=False, indent=2))
    return out_path


def main():
    parser = argparse.ArgumentParser(
        description="Genereer chunk-level keywords voor wetteksten (KeyBERT, lokaal)"
    )
    parser.add_argument("--source", help="Naam van één wettekst (stem, zonder .md)")
    parser.add_argument("--priority", action="store_true",
                        help="Verwerk alleen prioritaire wetteksten")
    parser.add_argument("--force", action="store_true",
                        help="Overschrijf bestaande keywords-bestanden")
    parser.add_argument("--dry-run", action="store_true",
                        help="Toon chunks zonder keywords te genereren")
    args = parser.parse_args()

    # Bepaal welke bestanden verwerkt worden
    if args.source:
        files = [WETTEKSTEN_DIR / f"{args.source}.md"]
        if not files[0].exists():
            print(f"❌ {files[0]} niet gevonden")
            sys.exit(1)
    elif args.priority:
        files = [WETTEKSTEN_DIR / f"{s}.md" for s in PRIORITY_SOURCES
                 if (WETTEKSTEN_DIR / f"{s}.md").exists()]
    else:
        files = sorted(
            f for f in WETTEKSTEN_DIR.glob("*.md")
            if "INDEX" not in f.name and "compilatie" not in f.name.lower()
        )

    # Filter al-verwerkte bestanden (tenzij --force of --dry-run)
    if not args.force and not args.dry_run:
        to_process = [f for f in files if not (KEYWORDS_DIR / f"{f.stem}.json").exists()]
        skipped = len(files) - len(to_process)
        if skipped:
            print(f"  {skipped} bestanden al verwerkt (gebruik --force om te overschrijven)")
        files = to_process

    if not files:
        print("✓ Alle bestanden al verwerkt.")
        return

    print(f"Te verwerken: {len(files)} wetteksten\n")

    # Laad KeyBERT model (eenmalig voor alle bestanden)
    kw_model = None if args.dry_run else load_keybert_model()

    total_chunks = 0
    for path in files:
        print(f"\n{'='*55}")
        print(f"Verwerk: {path.stem}")
        kw = generate_keywords_for_file(path, kw_model, args.dry_run)
        if kw:
            out = save_keywords(path.stem, kw)
            total_chunks += len(kw)
            # Toon een voorbeeld
            first_heading = next(iter(kw))
            first_kws = kw[first_heading]
            print(f"  ✓ {len(kw)} artikel-keywords → {out.relative_to(ROOT)}")
            print(f"  Voorbeeld — {first_heading}: {first_kws}")

    print(f"\n✓ Klaar — {total_chunks} artikel-keywords voor {len(files)} wetteksten.")
    print(f"  Keywords worden automatisch gebruikt bij de volgende rag_index.py run.")


if __name__ == "__main__":
    main()
