"""
RAG-index builder voor de Certificaid kennisbank.

Indexeert 5 ChromaDB-collections:
  - wetteksten   : resources/bronnen/wetteksten/*.md  (per Art.-sectie)
  - normen       : resources/bronnen/normen/*.md      (per paragraaf-sectie)
  - adviezen     : resources/bronnen/adviezen/*.md    (per sectie / heel advies)
  - tdks         : content/programmaonderdelen/*.md   (per kenniselement + doelstelling)
  - concepts     : data/concept_records/*.json        (per concept-veld)

Elk chunk krijgt contextual retrieval: de dichtstbijzijnde betekenisvolle
sectietitel wordt als eerste zin in de chunk-tekst opgenomen.

Gebruik:
  python tools/rag_index.py                    # bouw alle collections
  python tools/rag_index.py --collection normen
  python tools/rag_index.py --add-concepts     # voeg concept records toe
  python tools/rag_index.py --reset            # verwijder en herbouw alles
"""

import argparse
import json
import re
import sys
from pathlib import Path

import frontmatter
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from tqdm import tqdm

ROOT = Path(__file__).parent.parent
CHROMA_PATH = ROOT / "data" / "chroma_db"
EMBEDDING_MODEL = "BAAI/bge-m3"   # zie ADR-001

SOURCES = {
    "wetteksten":      ROOT / "resources" / "bronnen" / "wetteksten",
    "normen":          ROOT / "resources" / "bronnen" / "normen",
    "adviezen":        ROOT / "resources" / "bronnen" / "adviezen",
    "tdks":            ROOT / "content" / "programmaonderdelen",
    "bestaande_fiches": ROOT / "content" / "materie",
    "concepts":        ROOT / "data" / "concept_records",
}

MIN_CHUNK_CHARS = 100  # korter dan dit mergen we met context


def _has_real_content(text: str) -> bool:
    """
    Geeft True als een chunk échte inhoud heeft (niet alleen headings/metadata).
    Filtert chunks die enkel bestaan uit heading-achtige regels.
    """
    non_heading_chars = 0
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        # Skip heading-achtige regels (markdown + ejustice structuurhoofdstukken)
        if re.match(r"^#{1,6}\s", stripped):
            continue
        if re.match(r"^(BOEK|DEEL|TITEL|HOOFDSTUK|Afdeling|Onderafdeling|SECTIE)\s", stripped, re.I):
            continue
        if re.match(r"^#{1,5}\s*(BOEK|DEEL|TITEL|HOOFDSTUK|Afdeling)", stripped, re.I):
            continue
        non_heading_chars += len(stripped)
    return non_heading_chars >= 80  # minimaal 80 chars echte inhoud

def _is_toc_only(content: str) -> bool:
    """Detecteer of een wettekst enkel een inhoudsopgave is (geen artikeltekst).
    TOC-only: heeft Bold **Art. X** maar geen ## Art. headings met echte inhoud.
    """
    has_art_heading = bool(re.search(r"^#{1,4}\s+Art\.", content, re.MULTILINE))
    has_bold_art_ref = bool(re.search(r"^\*\*Art\.\s+", content, re.MULTILINE))
    if has_bold_art_ref and not has_art_heading:
        return True
    # Extra check: als er Art.-headings zijn maar bijna geen body (< 2000 chars tussen headings)
    if has_art_heading:
        art_sections = re.split(r"^#{1,4}\s+Art\.", content, flags=re.MULTILINE)
        avg_len = sum(len(s) for s in art_sections[1:]) / max(len(art_sections[1:]), 1)
        if avg_len < 100:  # gemiddeld < 100 chars per artikel → waarschijnlijk TOC
            return True
    return False


def get_client():
    CHROMA_PATH.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=str(CHROMA_PATH))


def get_collection(client, name: str, reset: bool = False):
    ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    if reset:
        try:
            client.delete_collection(name)
        except Exception:
            pass
    return client.get_or_create_collection(name, embedding_function=ef)


# ---------------------------------------------------------------------------
# Chunking helpers
# ---------------------------------------------------------------------------

def _is_structural_heading(line: str) -> bool:
    """Hoofdstuk/Afdeling/Titel/DEEL-headings die context geven maar geen inhoud."""
    stripped = line.lstrip("#").strip()
    return bool(re.match(
        r"^(HOOFDSTUK|Hoofdstuk|AFDELING|Afdeling|TITEL|Titel|DEEL|Deel|BOEK|Boek|SECTIE|Sectie)",
        stripped,
    ))


def _is_article_heading(line: str) -> bool:
    return bool(re.match(r"^#{1,4}\s+Art\.", line)) or bool(re.match(r"^#{1,4}\s+Par\.", line))


def split_markdown_into_chunks(text: str, source_id: str) -> list[dict]:
    """
    Splits markdown in chunks per ## sectie.
    Korte artikels (< MIN_CHUNK_CHARS) worden samengevoegd met de vorige context-heading.
    Context-heading wordt als eerste zin aan elk chunk prepended.

    Elk chunk bevat ook chunk_index en parent_section voor context-uitbreiding (ADR-002).
    """
    lines = text.split("\n")
    chunks = []
    current_heading = ""
    current_context = ""  # meest recente structurele heading
    current_lines = []
    chunk_counter = 0

    def flush(heading, context, body_lines):
        nonlocal chunk_counter
        body = "\n".join(body_lines).strip()
        if not body:
            return
        # Contextual retrieval: prepend structurele context als eerste zin
        if context and context not in heading:
            full_text = f"{context}\n\n{heading}\n\n{body}" if heading else f"{context}\n\n{body}"
        else:
            full_text = f"{heading}\n\n{body}" if heading else body
        chunk_counter += 1
        chunks.append({
            "id":             f"{source_id}__chunk{chunk_counter}",
            "text":           full_text.strip(),
            "heading":        heading,
            "context_heading": context,
            "chunk_index":    chunk_counter,   # voor context-uitbreiding via prev/next
            "parent_section": context,         # dichtstbijzijnde BOEK/TITEL/AFDELING
        })

    for line in lines:
        # Detecteer ## heading
        if re.match(r"^#{1,4} ", line):
            # Flush vorige chunk
            if current_lines or current_heading:
                flush(current_heading, current_context, current_lines)
                current_lines = []

            if _is_structural_heading(line):
                current_context = line.lstrip("#").strip()
                current_heading = ""
            else:
                current_heading = line.lstrip("#").strip()
        else:
            current_lines.append(line)

    # Flush laatste chunk
    if current_lines or current_heading:
        flush(current_heading, current_context, current_lines)

    return chunks


# ---------------------------------------------------------------------------
# Per-collection indexers
# ---------------------------------------------------------------------------

def index_wetteksten(collection, reset: bool = False):
    src = SOURCES["wetteksten"]
    files = sorted(src.glob("*.md"))
    if not files:
        print(f"  Geen bestanden in {src}")
        return

    ids, texts, metadatas = [], [], []
    toc_skipped = 0
    for path in tqdm(files, desc="wetteksten"):
        try:
            post = frontmatter.load(str(path))
        except Exception as e:
            print(f"  Overgeslagen {path.name}: {e}")
            continue

        if _is_toc_only(post.content):
            toc_skipped += 1
            continue

        fm = post.metadata
        source_id = path.stem
        chunks = split_markdown_into_chunks(post.content, source_id)

        for chunk in chunks:
            if len(chunk["text"]) < MIN_CHUNK_CHARS or not _has_real_content(chunk["text"]):
                continue
            ids.append(chunk["id"])
            texts.append(chunk["text"])
            metadatas.append({
                "bron":           str(fm.get("wet", fm.get("bron", path.stem))),
                "bestand":        path.name,
                "artikel_ref":    chunk["heading"],
                "themas":         json.dumps(fm.get("tags", [])),
                "itaa_lex":       str(fm.get("itaa-lex-sectie", "")),
                "chunk_index":    chunk["chunk_index"],    # voor context-uitbreiding
                "parent_section": chunk["parent_section"], # BOEK/TITEL/AFDELING
                "collection":     "wetteksten",
            })

    if ids:
        _batch_upsert(collection, ids, texts, metadatas)
    print(f"  {len(ids)} chunks geïndexeerd uit {len(files)} wetteksten ({toc_skipped} TOC-only overgeslagen)")


def index_normen(collection, reset: bool = False):
    src = SOURCES["normen"]
    files = [f for f in sorted(src.glob("*.md")) if "INDEX" not in f.name]
    if not files:
        print(f"  Geen bestanden in {src}")
        return

    ids, texts, metadatas = [], [], []
    for path in tqdm(files, desc="normen"):
        try:
            post = frontmatter.load(str(path))
        except Exception as e:
            print(f"  Overgeslagen {path.name}: {e}")
            continue

        fm = post.metadata
        source_id = path.stem
        chunks = split_markdown_into_chunks(post.content, source_id)

        for chunk in chunks:
            if len(chunk["text"]) < MIN_CHUNK_CHARS or not _has_real_content(chunk["text"]):
                continue
            ids.append(chunk["id"])
            texts.append(chunk["text"])
            metadatas.append({
                "bron":           str(fm.get("norm", path.stem)),
                "bestand":        path.name,
                "sectie":         chunk["heading"],
                "themas":         json.dumps(fm.get("themas", [])),
                "chunk_index":    chunk["chunk_index"],
                "parent_section": chunk["parent_section"],
                "collection":     "normen",
            })

    if ids:
        _batch_upsert(collection, ids, texts, metadatas)
    print(f"  {len(ids)} chunks geïndexeerd uit {len(files)} normen")


def index_adviezen(collection, reset: bool = False):
    src = SOURCES["adviezen"]
    files = [f for f in sorted(src.glob("*.md")) if "INDEX" not in f.name]
    if not files:
        print(f"  Geen bestanden in {src}")
        return

    ids, texts, metadatas = [], [], []
    for path in tqdm(files, desc="adviezen"):
        try:
            post = frontmatter.load(str(path))
        except Exception as e:
            print(f"  Overgeslagen {path.name}: {e}")
            continue

        fm = post.metadata
        source_id = path.stem
        content = post.content.strip()

        # Adviezen ≤ 40.000 chars (≈ 8.000 tokens): heel advies als 1 chunk (ADR-002)
        # bge-m3 heeft een context window van 8.192 tokens — mediaan advies (~7.500 chars)
        # past ruimschoots. Alleen de ~10% grootste adviezen worden gesplitst op ##-secties.
        if len(content) <= 40_000 or not re.search(r"^#{1,4} ", content, re.MULTILINE):
            chunk_text = content
            nummer = str(fm.get("nummer", path.stem))
            ids.append(f"{source_id}__chunk1")
            texts.append(chunk_text)
            metadatas.append({
                "bron":       nummer,
                "bestand":    path.name,
                "sectie":     "",
                "themas":     json.dumps(fm.get("themas", [])),
                "datum":      str(fm.get("datum", "")),
                "collection": "adviezen",
            })
        else:
            chunks = split_markdown_into_chunks(content, source_id)
            for chunk in chunks:
                if len(chunk["text"]) < MIN_CHUNK_CHARS or not _has_real_content(chunk["text"]):
                    continue
                ids.append(chunk["id"])
                texts.append(chunk["text"])
                metadatas.append({
                    "bron":       str(fm.get("nummer", path.stem)),
                    "bestand":    path.name,
                    "sectie":     chunk["heading"],
                    "themas":     json.dumps(fm.get("themas", [])),
                    "datum":      str(fm.get("datum", "")),
                    "collection": "adviezen",
                })

    if ids:
        _batch_upsert(collection, ids, texts, metadatas)
    print(f"  {len(ids)} chunks geïndexeerd uit {len(files)} adviezen")


def index_tdks(collection, reset: bool = False):
    src = SOURCES["tdks"]
    files = sorted(src.glob("*.md"))
    if not files:
        print(f"  Geen bestanden in {src}")
        return

    ids, texts, metadatas = [], [], []
    for path in tqdm(files, desc="tdks"):
        try:
            post = frontmatter.load(str(path))
        except Exception as e:
            print(f"  Overgeslagen {path.name}: {e}")
            continue

        fm = post.metadata
        po_nr = str(fm.get("tags", [path.stem])[0]) if fm.get("tags") else path.stem
        source_id = path.stem

        # Chunk per ### Taak en per bullet-groep in Kenniselementen
        content = post.content
        # Splits op ### headings
        sections = re.split(r"(?=^#{2,3} )", content, flags=re.MULTILINE)
        chunk_counter = 0
        for section in sections:
            section = section.strip()
            if not section or len(section) < MIN_CHUNK_CHARS:
                continue
            chunk_counter += 1
            chunk_id = f"{source_id}__chunk{chunk_counter}"
            # Heading van de sectie
            first_line = section.split("\n")[0].lstrip("#").strip()
            ids.append(chunk_id)
            texts.append(section)
            metadatas.append({
                "bron":       f"PO {po_nr}",
                "bestand":    path.name,
                "sectie":     first_line,
                "po_nr":      po_nr,
                "collection": "tdks",
            })

    if ids:
        _batch_upsert(collection, ids, texts, metadatas)
    print(f"  {len(ids)} chunks geïndexeerd uit {len(files)} PO-fiches")


def index_bestaande_fiches(collection, reset: bool = False):
    """Indexeer bestaande materie-fiches als hulpbron voor concept-extractie.
    Gelabeld als source_type='bestaande_fiche' — niet primaire bron, wel curated kennis.
    """
    src = SOURCES["bestaande_fiches"]
    files = sorted(src.glob("*.md"))
    if not files:
        print(f"  Geen bestanden in {src}")
        return

    ids, texts, metadatas = [], [], []
    for path in tqdm(files, desc="bestaande_fiches"):
        try:
            post = frontmatter.load(str(path))
        except Exception as e:
            print(f"  Overgeslagen {path.name}: {e}")
            continue

        fm = post.metadata
        source_id = path.stem
        chunks = split_markdown_into_chunks(post.content, source_id)

        for chunk in chunks:
            if len(chunk["text"]) < MIN_CHUNK_CHARS or not _has_real_content(chunk["text"]):
                continue
            ids.append(chunk["id"])
            texts.append(chunk["text"])
            metadatas.append({
                "bron":        path.stem,
                "bestand":     path.name,
                "sectie":      chunk["heading"],
                "themas":      json.dumps(fm.get("tags", [])),
                "niveau":      str(fm.get("niveau", "")),
                "source_type": "bestaande_fiche",
                "collection":  "bestaande_fiches",
            })

    if ids:
        _batch_upsert(collection, ids, texts, metadatas)
    print(f"  {len(ids)} chunks geïndexeerd uit {len(files)} bestaande materie-fiches")


def index_concepts(collection):
    src = SOURCES["concepts"]
    if not src.exists():
        print(f"  {src} bestaat nog niet — sla concepts over")
        return

    files = sorted(src.glob("*.json"))
    if not files:
        print(f"  Geen concept records in {src}")
        return

    ids, texts, metadatas = [], [], []
    for path in tqdm(files, desc="concepts"):
        try:
            record = json.loads(path.read_text())
        except Exception as e:
            print(f"  Overgeslagen {path.name}: {e}")
            continue

        concept_id = record.get("id", path.stem)
        po_ref = json.dumps(record.get("po_ref", []))

        def add_chunk(suffix, text, confidence=""):
            if not text or len(text.strip()) < MIN_CHUNK_CHARS:
                return
            ids.append(f"{concept_id}__{suffix}")
            texts.append(text.strip())
            metadatas.append({
                "bron":       concept_id,
                "bestand":    path.name,
                "veld":       suffix,
                "po_ref":     po_ref,
                "confidence": confidence,
                "collection": "concepts",
            })

        naam = record.get("naam", concept_id)

        # main_rule
        mr = record.get("main_rule", {})
        if mr:
            add_chunk("main_rule", f"{naam}\n\n{mr.get('text', '')}", mr.get("confidence", ""))

        # exceptions
        for i, exc in enumerate(record.get("exceptions", [])):
            add_chunk(f"exception_{i}", f"{naam} — uitzondering\n\n{exc.get('text', '')}", exc.get("confidence", ""))

        # scope
        scope = record.get("scope", {})
        if scope:
            scope_text = f"{naam} — toepassingsgebied\n\nVan toepassing op: {scope.get('applies_to', '')}\nUitgesloten: {scope.get('excludes', '')}"
            add_chunk("scope", scope_text)

        # pitfalls
        for i, pit in enumerate(record.get("pitfalls", [])):
            add_chunk(f"pitfall_{i}", f"{naam} — valkuil\n\n{pit.get('text', '')}", pit.get("confidence", "inferred"))

        # examples
        for i, ex in enumerate(record.get("examples", [])):
            if isinstance(ex, dict):
                add_chunk(f"example_{i}", f"{naam} — voorbeeld\n\n{ex.get('text', '')}", ex.get("confidence", ""))
            else:
                add_chunk(f"example_{i}", f"{naam} — voorbeeld\n\n{ex}")

    if ids:
        _batch_upsert(collection, ids, texts, metadatas)
    print(f"  {len(ids)} chunks geïndexeerd uit {len(files)} concept records")


# ---------------------------------------------------------------------------
# Batch upsert (ChromaDB max ~5000 per batch)
# ---------------------------------------------------------------------------

def _batch_upsert(collection, ids, texts, metadatas, batch_size=500):
    for i in range(0, len(ids), batch_size):
        collection.upsert(
            ids=ids[i:i+batch_size],
            documents=texts[i:i+batch_size],
            metadatas=metadatas[i:i+batch_size],
        )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Bouw de Certificaid RAG-index")
    parser.add_argument("--collection", choices=["wetteksten", "normen", "adviezen", "tdks", "bestaande_fiches", "concepts"],
                        help="Indexeer alleen deze collection (default: alles)")
    parser.add_argument("--add-concepts", action="store_true",
                        help="Voeg/vernieuw concept records toe aan concepts collection")
    parser.add_argument("--reset", action="store_true",
                        help="Verwijder en herbouw de collection(s)")
    args = parser.parse_args()

    client = get_client()

    to_index = [args.collection] if args.collection else ["wetteksten", "normen", "adviezen", "tdks", "bestaande_fiches"]
    if args.add_concepts:
        to_index = ["concepts"]

    for name in to_index:
        print(f"\n→ Indexeer collection: {name}")
        col = get_collection(client, name, reset=args.reset)
        if name == "wetteksten":
            index_wetteksten(col, args.reset)
        elif name == "normen":
            index_normen(col, args.reset)
        elif name == "adviezen":
            index_adviezen(col, args.reset)
        elif name == "tdks":
            index_tdks(col, args.reset)
        elif name == "bestaande_fiches":
            index_bestaande_fiches(col, args.reset)
        elif name == "concepts":
            index_concepts(col)

    print("\n✓ Klaar.")


if __name__ == "__main__":
    main()
