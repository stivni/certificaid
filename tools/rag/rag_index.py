"""
RAG-index builder voor de Certificaid kennisbank.

Indexeert 6 ChromaDB-collections volgens ADR-002 v2:
  - wetteksten      : per artikel (`## Art.`); breadcrumb-prefix met namen + gestructureerd path
  - normen          : per sectie met norm-naam in breadcrumb
  - adviezen        : heel advies (≤40K chars) of gesplitst op `##` met advies-titel als breadcrumb
  - tdks            : per kenniselement + doelstelling
  - bestaande_fiches: materie-fiches als hulpbron
  - concepts        : per veld van een concept-node (ADR-009)

Elk chunk krijgt een breadcrumb-prefix (`[wet → titel-naam → ...]`) als eerste regel
in de embedded tekst, plus path-array in metadata voor citatie en filtering.

Te lange artikelen (> 24K chars) worden gesplitst op alinea-grenzen (ADR-002 v2 §6).

Gebruik:
  python tools/rag/rag_index.py                    # bouw alle collections
  python tools/rag/rag_index.py --collection normen
  python tools/rag/rag_index.py --add-concepts     # voeg concept records toe
  python tools/rag/rag_index.py --reset            # verwijder en herbouw alles
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

ROOT = Path(__file__).resolve().parent.parent.parent
CHROMA_PATH = ROOT / "data" / "chroma_db"
EMBEDDING_MODEL = "BAAI/bge-m3"   # zie ADR-001
KEYWORDS_DIR = ROOT / "resources" / "bronnen" / "wetteksten" / "keywords"

SOURCES = {
    "wetteksten":      ROOT / "resources" / "bronnen" / "wetteksten",
    "normen":          ROOT / "resources" / "bronnen" / "normen",
    "adviezen":        ROOT / "resources" / "bronnen" / "adviezen",
    "tdks":            ROOT / "content" / "programmaonderdelen",
    "bestaande_fiches": ROOT / "content" / "materie",
    "concepts":        ROOT / "data" / "concept_records",
}

MIN_CHUNK_CHARS = 100      # korter dan dit filteren we weg
MAX_CHUNK_CHARS = 24_000   # ADR-002 v2 §6 — bge-m3 8K-token-window met marge


# ---------------------------------------------------------------------------
# Frontmatter / keywords helpers
# ---------------------------------------------------------------------------

def _load_keywords(stem: str) -> dict:
    """Laad chunk-level keywords voor een wettekst (ADR-004)."""
    path = KEYWORDS_DIR / f"{stem}.json"
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            return {}
    return {}


def _prepend_keywords(text: str, heading: str, keywords_map: dict) -> str:
    """Prepend `[kw1, kw2, ...]` aan chunk-tekst als beschikbaar."""
    kws = keywords_map.get(heading, [])
    if not kws:
        return text
    return f"[{', '.join(kws)}]\n\n{text}"


def _has_real_content(text: str) -> bool:
    """Filtert chunks die enkel bestaan uit headings/structurele markers."""
    non_heading_chars = 0
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if re.match(r"^#{1,6}\s", stripped):
            continue
        if re.match(r"^(BOEK|DEEL|TITEL|HOOFDSTUK|Afdeling|Onderafdeling|SECTIE)\s", stripped, re.I):
            continue
        if re.match(r"^\[.*?\]$", stripped):  # breadcrumb-regels
            continue
        non_heading_chars += len(stripped)
    return non_heading_chars >= 80


def _is_toc_only(content: str) -> bool:
    """Detecteer of een wettekst enkel een inhoudsopgave is."""
    has_art_heading = bool(re.search(r"^#{1,4}\s+Art\.", content, re.MULTILINE))
    has_bold_art_ref = bool(re.search(r"^\*\*Art\.\s+", content, re.MULTILINE))
    if has_bold_art_ref and not has_art_heading:
        return True
    if has_art_heading:
        art_sections = re.split(r"^#{1,4}\s+Art\.", content, flags=re.MULTILINE)
        avg_len = sum(len(s) for s in art_sections[1:]) / max(len(art_sections[1:]), 1)
        if avg_len < 100:
            return True
    return False


# ---------------------------------------------------------------------------
# ChromaDB client
# ---------------------------------------------------------------------------

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
        # Nieuwe client om gecachte UUID-state te flushen (zie ADR-010)
        client = chromadb.PersistentClient(path=str(CHROMA_PATH))
        return client.create_collection(name, embedding_function=ef), client
    try:
        return client.get_collection(name, embedding_function=ef), client
    except Exception:
        return client.create_collection(name, embedding_function=ef), client


# ---------------------------------------------------------------------------
# Heading-parsing (ADR-002 v2)
# ---------------------------------------------------------------------------

STRUCTURAL_TYPES = (
    r"BOEK|Boek|DEEL|Deel|TITEL|Titel|HOOFDSTUK|Hoofdstuk|"
    r"AFDELING|Afdeling|ONDERAFDELING|Onderafdeling|"
    r"SECTIE|Sectie|ONDERDEEL|Onderdeel|PARAGRAAF|Paragraaf"
)
ARTICLE_TYPES = r"Art\.|Par\."

HEADING_RE = re.compile(
    rf"^(#{{1,6}})\s+"
    rf"(?P<type>{STRUCTURAL_TYPES}|{ARTICLE_TYPES})"
    rf"\s*"
    rf"(?P<nr>[IVXLCDM]+|\d+(?:bis|ter|quater)?)?"
    rf"\s*\.?\s*"
    rf"(?:[-—:]\s*)?"
    rf"(?P<naam>.*?)\s*\.?\s*$"
)

GENERIC_HEADING_RE = re.compile(r"^#{1,4} ")
STRUCTURAL_PREFIX_RE = re.compile(rf"^({STRUCTURAL_TYPES})\b")


def parse_heading(line: str) -> dict | None:
    """Parse markdown heading naar gestructureerde dict, of None als geen match."""
    m = HEADING_RE.match(line.rstrip())
    if not m:
        return None
    type_raw = m.group("type")
    return {
        "level": len(m.group(1)),
        "type": type_raw.upper().rstrip(".") if type_raw not in ("Art.", "Par.") else type_raw,
        "nr": (m.group("nr") or "").strip(),
        "naam": (m.group("naam") or "").strip(),
        "is_article": type_raw in ("Art.", "Par."),
        "raw": line.strip(),
    }


def build_breadcrumb(path: list[dict]) -> str:
    """
    Bouw `[wet-naam → niveau-naam → ...]`-string uit path-array.
    Naam wordt geprefereerd; fallback naar `<TYPE> <nr>` als naam leeg.
    Het artikel zelf staat niet in de breadcrumb (dat is de heading eronder).
    """
    parts = []
    for level in path:
        if level["type"] == "wet":
            parts.append(level["naam"])
        elif level["type"] in ("Art.", "Par."):
            continue
        else:
            naam = level["naam"]
            if not naam and level["nr"]:
                naam = f"{level['type']} {level['nr']}"
            elif not naam:
                naam = level["type"]
            parts.append(naam)
    return "[" + " → ".join(parts) + "]"


# ---------------------------------------------------------------------------
# Hard maximum split (ADR-002 v2 §6)
# ---------------------------------------------------------------------------

def split_long_chunk(chunk: dict, max_chars: int) -> list[dict]:
    """
    Splits een te lange chunk op alinea-grenzen (\\n\\n).
    Fallback: als één alinea zelf > max_chars, hard-split op woordgrens.
    Elke fragment krijgt suffix `_split_part = "i/N"`.
    """
    text = chunk["text"]
    if len(text) <= max_chars:
        return [chunk]

    paragraphs = text.split("\n\n")
    fragments: list[str] = []
    current: list[str] = []
    current_len = 0
    for para in paragraphs:
        para_len = len(para) + 2
        if current and current_len + para_len > max_chars:
            fragments.append("\n\n".join(current))
            current, current_len = [], 0
        if para_len > max_chars:
            words = para.split()
            buf, buf_len = [], 0
            for w in words:
                w_len = len(w) + 1
                if buf_len + w_len > max_chars:
                    if current:
                        fragments.append("\n\n".join(current + [" ".join(buf)]))
                        current, current_len = [], 0
                    else:
                        fragments.append(" ".join(buf))
                    buf, buf_len = [w], w_len
                else:
                    buf.append(w)
                    buf_len += w_len
            if buf:
                current.append(" ".join(buf))
                current_len += buf_len + 2
        else:
            current.append(para)
            current_len += para_len
    if current:
        fragments.append("\n\n".join(current))

    out = []
    for i, frag_text in enumerate(fragments, 1):
        new = dict(chunk)
        new["text"] = frag_text
        new["_split_part"] = f"{i}/{len(fragments)}"
        out.append(new)
    return out


# ---------------------------------------------------------------------------
# v2 chunking voor wetteksten — per artikel met breadcrumb + path
# ---------------------------------------------------------------------------

def split_wettekst_v2(text: str, source_id: str, fm: dict) -> list[dict]:
    """
    Splits markdown op artikel-headings. Sub-headings (### §1, ### A.) blijven inline.
    Houdt structurele stack bij voor breadcrumb + gestructureerd path per chunk.
    Past ook hard-maximum splitsing toe (ADR-002 v2 §6).
    """
    wet_naam = str(fm.get("wet") or fm.get("bron") or source_id)

    lines = text.split("\n")
    chunks: list[dict] = []
    structural_stack: list[dict] = []
    current_article: dict | None = None
    current_lines: list[str] = []
    chunk_counter = 0

    def flush():
        nonlocal chunk_counter
        if current_article is None:
            return
        body = "\n".join(current_lines).strip()
        if not body and not current_article.get("naam"):
            return

        path = [{"type": "wet", "nr": "", "naam": wet_naam}]
        for s in structural_stack:
            path.append({"type": s["type"], "nr": s["nr"], "naam": s["naam"]})
        path.append({
            "type": current_article["type"],
            "nr": current_article["nr"],
            "naam": current_article.get("naam", ""),
        })

        breadcrumb = build_breadcrumb(path)
        article_heading = current_article["raw"].lstrip("#").strip()
        full_text = f"{breadcrumb}\n\n{article_heading}\n\n{body}".strip()

        # Hard-max splitsing
        provisional = {
            "text": full_text,
            "heading": article_heading,
            "path": path,
            "breadcrumb": breadcrumb,
        }
        for fragment in split_long_chunk(provisional, MAX_CHUNK_CHARS):
            chunk_counter += 1
            chunks.append({
                "id":           f"{source_id}__chunk{chunk_counter}",
                "chunk_index":  chunk_counter,
                "text":         fragment["text"],
                "heading":      fragment["heading"],
                "path":         fragment["path"],
                "breadcrumb":   fragment["breadcrumb"],
                "_split_part":  fragment.get("_split_part", ""),
            })

    for line in lines:
        parsed = parse_heading(line)
        if parsed is None:
            current_lines.append(line)
            continue
        if parsed["is_article"]:
            flush()
            current_article = parsed
            current_lines = []
        else:
            # Stack-pruning op level: nieuwe heading op level N knipt diepere niveaus af
            structural_stack[:] = [s for s in structural_stack if s["level"] < parsed["level"]]
            structural_stack.append(parsed)

    flush()
    return chunks


# ---------------------------------------------------------------------------
# Generieke splitter voor bronnen zonder strikte artikel-structuur
# ---------------------------------------------------------------------------

def split_generic_headings(text: str, source_id: str, breadcrumb_prefix: str = "") -> list[dict]:
    """
    Splitser op iedere `## sectie`-heading — voor normen, materie-fiches, gesplitste adviezen.
    Optionele `breadcrumb_prefix` wordt aan elke chunk toegevoegd.
    """
    lines = text.split("\n")
    chunks: list[dict] = []
    current_heading = ""
    current_context = ""
    current_lines: list[str] = []
    chunk_counter = 0

    def is_structural(line: str) -> bool:
        stripped = line.lstrip("#").strip()
        return bool(STRUCTURAL_PREFIX_RE.match(stripped))

    def flush(heading: str, context: str, body_lines: list[str]):
        nonlocal chunk_counter
        body = "\n".join(body_lines).strip()
        if not body:
            return

        prefix_parts: list[str] = []
        if breadcrumb_prefix:
            prefix_parts.append(breadcrumb_prefix)
        if context and context not in heading:
            prefix_parts.append(context)
        prefix = "\n\n".join(prefix_parts)

        if heading:
            full_text = f"{prefix}\n\n{heading}\n\n{body}" if prefix else f"{heading}\n\n{body}"
        else:
            full_text = f"{prefix}\n\n{body}" if prefix else body

        chunk_counter += 1
        chunks.append({
            "id":              f"{source_id}__chunk{chunk_counter}",
            "text":            full_text.strip(),
            "heading":         heading,
            "context_heading": context,
            "chunk_index":     chunk_counter,
        })

    for line in lines:
        if GENERIC_HEADING_RE.match(line):
            if current_lines or current_heading:
                flush(current_heading, current_context, current_lines)
                current_lines = []
            if is_structural(line):
                current_context = line.lstrip("#").strip()
                current_heading = ""
            else:
                current_heading = line.lstrip("#").strip()
        else:
            current_lines.append(line)

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
    long_split_count = 0
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
        chunks = split_wettekst_v2(post.content, source_id, fm)
        # Fallback voor bronnen zonder ## Art.-headings (bv. praktijkgidzen
        # zoals fiscaal-memento, toelichting-PB; ADR-002 v2 — praktijkgidzen-TODO)
        if not chunks:
            wet_naam = str(fm.get("wet") or fm.get("bron") or source_id)
            chunks = split_generic_headings(post.content, source_id, breadcrumb_prefix=f"[{wet_naam}]")
            for c in chunks:
                # Geef alle generic-chunks een minimaal path zodat metadata uniform is
                c["path"] = [
                    {"type": "wet", "nr": "", "naam": wet_naam},
                    {"type": "sectie", "nr": "", "naam": c.get("heading", "")},
                ]
                c["breadcrumb"] = f"[{wet_naam}]" + (
                    f" → {c['heading']}" if c.get("heading") else ""
                )
        keywords_map = _load_keywords(source_id)

        for chunk in chunks:
            if len(chunk["text"]) < MIN_CHUNK_CHARS or not _has_real_content(chunk["text"]):
                continue
            if chunk.get("_split_part"):
                long_split_count += 1
            chunk_text = _prepend_keywords(chunk["text"], chunk["heading"], keywords_map)
            ids.append(chunk["id"])
            texts.append(chunk_text)
            metadatas.append({
                "bron":         str(fm.get("wet", fm.get("bron", path.stem))),
                "bestand":      path.name,
                "artikel_ref":  chunk["heading"],
                "themas":       json.dumps(fm.get("tags", [])),
                "itaa_lex":     str(fm.get("itaa-lex-sectie", "")),
                "chunk_index":  chunk["chunk_index"],
                "path":         json.dumps(chunk["path"], ensure_ascii=False),
                "breadcrumb":   chunk["breadcrumb"],
                "split_part":   chunk.get("_split_part", ""),
                "has_keywords": str(bool(keywords_map.get(chunk["heading"]))),
                "collection":   "wetteksten",
            })

    if ids:
        _batch_upsert(collection, ids, texts, metadatas)
    print(f"  {len(ids)} chunks geïndexeerd uit {len(files)} wetteksten "
          f"({toc_skipped} TOC-only overgeslagen, {long_split_count} fragments uit te lange artikelen)")


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
        norm_naam = str(fm.get("norm", path.stem))
        breadcrumb = f"[Norm — {norm_naam}]"
        chunks = split_generic_headings(post.content, source_id, breadcrumb_prefix=breadcrumb)

        for chunk in chunks:
            if len(chunk["text"]) < MIN_CHUNK_CHARS or not _has_real_content(chunk["text"]):
                continue
            ids.append(chunk["id"])
            texts.append(chunk["text"])
            metadatas.append({
                "bron":        norm_naam,
                "bestand":     path.name,
                "sectie":      chunk["heading"],
                "themas":      json.dumps(fm.get("themas", [])),
                "chunk_index": chunk["chunk_index"],
                "breadcrumb":  breadcrumb,
                "collection":  "normen",
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

        # Strip "CBN-advies " prefix uit nummer (frontmatter heeft soms volledige string)
        nummer_raw = str(fm.get("nummer", path.stem))
        nummer = re.sub(r"^CBN[- ]advies\s*", "", nummer_raw).strip()

        # Onderwerp uit eerste H1 (inhoudelijke titel; ADR-002 v2 §2 — "naam telt").
        # Sommige H1's bevatten plak-tekst na de titel doordat ETL geen lege regel heeft
        # geplaatst tussen H1 en eerste paragraaf. Pragmatisch: hard-cap op 80 chars
        # op woordgrens. Volledige onderwerp blijft beschikbaar in de eerste chunk-text.
        h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        onderwerp = h1_match.group(1).strip() if h1_match else ""
        onderwerp = re.sub(r"^CBN[- ]advies\s*\S+\s*—\s*", "", onderwerp).strip()
        if len(onderwerp) > 80:
            onderwerp = onderwerp[:80].rsplit(" ", 1)[0] + "…"

        breadcrumb = f"[CBN-advies {nummer} — {onderwerp}]" if onderwerp else f"[CBN-advies {nummer}]"

        # ADR-002 v2: ≤40K chars → 1 chunk; anders splits op ##-secties
        if len(content) <= 40_000 or not re.search(r"^#{2,4} ", content, re.MULTILINE):
            full_text = f"{breadcrumb}\n\n{content}"
            ids.append(f"{source_id}__chunk1")
            texts.append(full_text)
            metadatas.append({
                "bron":        nummer,
                "bestand":     path.name,
                "sectie":      "",
                "themas":      json.dumps(fm.get("themas", [])),
                "datum":       str(fm.get("datum", "")),
                "breadcrumb":  breadcrumb,
                "chunk_index": 1,
                "collection":  "adviezen",
            })
        else:
            chunks = split_generic_headings(content, source_id, breadcrumb_prefix=breadcrumb)
            for chunk in chunks:
                if len(chunk["text"]) < MIN_CHUNK_CHARS or not _has_real_content(chunk["text"]):
                    continue
                section_breadcrumb = (
                    f"{breadcrumb[:-1]} → {chunk['heading']}]"
                    if chunk["heading"] else breadcrumb
                )
                ids.append(chunk["id"])
                texts.append(chunk["text"])
                metadatas.append({
                    "bron":        nummer,
                    "bestand":     path.name,
                    "sectie":      chunk["heading"],
                    "themas":      json.dumps(fm.get("themas", [])),
                    "datum":       str(fm.get("datum", "")),
                    "breadcrumb":  section_breadcrumb,
                    "chunk_index": chunk["chunk_index"],
                    "collection":  "adviezen",
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

        content = post.content
        sections = re.split(r"(?=^#{2,3} )", content, flags=re.MULTILINE)
        chunk_counter = 0
        for section in sections:
            section = section.strip()
            if not section or len(section) < MIN_CHUNK_CHARS:
                continue
            chunk_counter += 1
            chunk_id = f"{source_id}__chunk{chunk_counter}"
            first_line = section.split("\n")[0].lstrip("#").strip()
            breadcrumb = f"[PO {po_nr} — {first_line}]"
            ids.append(chunk_id)
            texts.append(f"{breadcrumb}\n\n{section}")
            metadatas.append({
                "bron":       f"PO {po_nr}",
                "bestand":    path.name,
                "sectie":     first_line,
                "po_nr":      po_nr,
                "breadcrumb": breadcrumb,
                "chunk_index": chunk_counter,
                "collection": "tdks",
            })

    if ids:
        _batch_upsert(collection, ids, texts, metadatas)
    print(f"  {len(ids)} chunks geïndexeerd uit {len(files)} PO-fiches")


def index_bestaande_fiches(collection, reset: bool = False):
    """Materie-fiches als hulpbron voor concept-extractie."""
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
        breadcrumb = f"[Materie-fiche — {path.stem}]"
        chunks = split_generic_headings(post.content, source_id, breadcrumb_prefix=breadcrumb)

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
                "breadcrumb":  breadcrumb,
                "chunk_index": chunk["chunk_index"],
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

        mr = record.get("main_rule", {})
        if mr:
            add_chunk("main_rule", f"{naam}\n\n{mr.get('text', '')}", mr.get("confidence", ""))

        for i, exc in enumerate(record.get("exceptions", [])):
            add_chunk(f"exception_{i}", f"{naam} — uitzondering\n\n{exc.get('text', '')}", exc.get("confidence", ""))

        scope = record.get("scope", {})
        if scope:
            scope_text = f"{naam} — toepassingsgebied\n\nVan toepassing op: {scope.get('applies_to', '')}\nUitgesloten: {scope.get('excludes', '')}"
            add_chunk("scope", scope_text)

        for i, pit in enumerate(record.get("pitfalls", [])):
            add_chunk(f"pitfall_{i}", f"{naam} — valkuil\n\n{pit.get('text', '')}", pit.get("confidence", "inferred"))

        for i, ex in enumerate(record.get("examples", [])):
            if isinstance(ex, dict):
                add_chunk(f"example_{i}", f"{naam} — voorbeeld\n\n{ex.get('text', '')}", ex.get("confidence", ""))
            else:
                add_chunk(f"example_{i}", f"{naam} — voorbeeld\n\n{ex}")

    if ids:
        _batch_upsert(collection, ids, texts, metadatas)
    print(f"  {len(ids)} chunks geïndexeerd uit {len(files)} concept records")


# ---------------------------------------------------------------------------
# Batch upsert met tqdm-voortgangsbar (ADR-002 v2 — kostbare les uit run 1)
# ---------------------------------------------------------------------------

def _batch_upsert(collection, ids, texts, metadatas, batch_size: int = 200):
    n = len(ids)
    if n == 0:
        return
    n_batches = (n + batch_size - 1) // batch_size
    for i in tqdm(range(0, n, batch_size), desc="    embedden", total=n_batches):
        collection.upsert(
            ids=ids[i:i + batch_size],
            documents=texts[i:i + batch_size],
            metadatas=metadatas[i:i + batch_size],
        )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Bouw de Certificaid RAG-index (ADR-002 v2)")
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
        col, client = get_collection(client, name, reset=args.reset)
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
