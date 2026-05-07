"""
RAG-index builder voor de Certificaid kennisbank.

Indexeert twee ChromaDB-collections (ADR-006):
  - bronnen   : wetteksten + normen + adviezen samen, met `bron_rol`-metadata
  - concepten : concept-records per node-veld (ADR-007)

Chunking per brontype (ADR-006 §4):
  - wettekst : per artikel (`## Art.`); breadcrumb-prefix + gestructureerd path
  - norm      : per `##`-sectie met norm-naam in breadcrumb
  - advies    : heel advies (≤40K chars) of gesplitst op `##` met advies-titel

Chunk-id-stabiliteit (ADR-006 §3.1, ADR-004):
  - wettekst : `<bron-stem>__art_<nr>`       bv. Antiwitwaswet-2017__art_5
  - norm      : `<bron-stem>__sec_<slug>`
  - advies    : `<bron-stem>` (één chunk) of `<bron-stem>__sec_<slug>` (gesplitst)

Te lange artikelen (> 24K chars) worden gesplitst op alinea-grenzen (ADR-006 §4).

Device auto-detect (ADR implementatie-backlog):
  MPS (Apple Silicon) > CUDA > CPU. Override via --device.

Scope-modus (POC vertical-slice, zie roadmap.md Fase 2):
  --scope path/to/<programmaonderdeel>-bronnen-scope.yaml

Gebruik:
  python tools/rag/rag_index.py                              # alle bronnen-types
  python tools/rag/rag_index.py --bron-rol norm              # alleen normen
  python tools/rag/rag_index.py --scope data/programmaonderdelen/4.0-bronnen-scope.yaml
  python tools/rag/rag_index.py --add-concepten              # concept-records indexeren
  python tools/rag/rag_index.py --reset                      # verwijder en herbouw
  python tools/rag/rag_index.py --device cpu                 # forceer device
"""

import argparse
import json
import re
import sys
from pathlib import Path

import frontmatter
import yaml
import chromadb
import torch
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from tqdm import tqdm

ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_CHROMA_PATH = ROOT / "data" / "chroma_db"
EMBEDDING_MODEL = "BAAI/bge-m3"   # zie ADR-006
KEYWORDS_DIR = ROOT / "resources" / "bronnen" / "wetteksten" / "keywords"

BRON_DIRS = {
    "wettekst": ROOT / "resources" / "bronnen" / "wetteksten",
    "norm":     ROOT / "resources" / "bronnen" / "normen",
    "advies":   ROOT / "resources" / "bronnen" / "adviezen",
}
CONCEPTS_DIR = ROOT / "data" / "concept_records"

MIN_CHUNK_CHARS = 100
MAX_CHUNK_CHARS = 24_000   # ADR-006 §4 — bge-m3 8K-token-window met marge


# ---------------------------------------------------------------------------
# Device detectie
# ---------------------------------------------------------------------------

def detect_device() -> str:
    """
    Detecteer GPU. Volgorde: MPS (Apple Silicon) → CUDA → fout.
    CPU wordt niet gebruikt voor embedding — te traag voor productie.
    Forceer CPU via --device cpu enkel voor debugging.
    """
    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    raise RuntimeError(
        "Geen GPU gevonden (MPS of CUDA vereist). "
        "Gebruik --device cpu enkel voor debugging."
    )


# ---------------------------------------------------------------------------
# Scope-loader (POC vertical-slice)
# ---------------------------------------------------------------------------

def load_scope(scope_yaml_path: Path) -> tuple[str, dict[str, set[str]], Path]:
    """
    Laad een scope-YAML en return:
      - programmaonderdeel-id (bv. "4.0")
      - file_filter: dict bron_rol → set bestandsnamen in scope
      - chroma_path: aparte ChromaDB-path voor deze scope
    """
    data = yaml.safe_load(scope_yaml_path.read_text())
    programmaonderdeel = str(data.get("programmaonderdeel", scope_yaml_path.stem))
    raw = data.get("bronnen", {})
    file_filter: dict[str, set[str]] = {}
    for rol in BRON_DIRS:
        files = raw.get(rol + "en", raw.get(rol, [])) or []   # "wetteksten" of "wettekst"
        file_filter[rol] = set(files)
    chroma_path = ROOT / "data" / f"chroma_db_{programmaonderdeel}"
    return programmaonderdeel, file_filter, chroma_path


def _apply_filter(files: list[Path], allowed: set[str] | None) -> list[Path]:
    if allowed is None:
        return files
    return [f for f in files if f.name in allowed]


# ---------------------------------------------------------------------------
# Frontmatter / keywords helpers
# ---------------------------------------------------------------------------

def _load_keywords(stem: str) -> dict:
    path = KEYWORDS_DIR / f"{stem}.json"
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            return {}
    return {}


def _prepend_keywords(text: str, heading: str, keywords_map: dict) -> str:
    kws = keywords_map.get(heading, [])
    if not kws:
        return text
    return f"[{', '.join(kws)}]\n\n{text}"


def _has_real_content(text: str) -> bool:
    non_heading_chars = 0
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if re.match(r"^#{1,6}\s", stripped):
            continue
        if re.match(r"^(BOEK|DEEL|TITEL|HOOFDSTUK|Afdeling|Onderafdeling|SECTIE)\s", stripped, re.I):
            continue
        if re.match(r"^\[.*?\]$", stripped):
            continue
        non_heading_chars += len(stripped)
    return non_heading_chars >= 80


def _is_toc_only(content: str) -> bool:
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


def _slug(text: str) -> str:
    """Maak een bestandsnaam-veilige slug uit een heading-tekst."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:60] or "sectie"


# ---------------------------------------------------------------------------
# ChromaDB client
# ---------------------------------------------------------------------------

def get_client(chroma_path: Path):
    chroma_path.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=str(chroma_path))


def get_collection(client, chroma_path: Path, name: str, ef, reset: bool = False):
    if reset:
        try:
            client.delete_collection(name)
        except Exception:
            pass
        client = chromadb.PersistentClient(path=str(chroma_path))
        return client.create_collection(name, embedding_function=ef), client
    try:
        return client.get_collection(name, embedding_function=ef), client
    except Exception:
        return client.create_collection(name, embedding_function=ef), client


# ---------------------------------------------------------------------------
# Heading-parsing (ADR-006)
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
# Hard maximum split (ADR-006 §4)
# ---------------------------------------------------------------------------

def split_long_chunk(chunk: dict, max_chars: int) -> list[dict]:
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
# Chunking — wetteksten (per artikel, stabiele id op art-nr)
# ---------------------------------------------------------------------------

def split_wettekst(text: str, source_id: str, fm: dict) -> list[dict]:
    """
    Splits markdown op artikel-headings. Sub-headings blijven inline.
    Chunk-id = `<source_id>__art_<nr>` (stabiel, zie ADR-006 §3.1).
    """
    wet_naam = str(fm.get("wet") or fm.get("bron") or source_id)
    lines = text.split("\n")
    chunks: list[dict] = []
    structural_stack: list[dict] = []
    current_article: dict | None = None
    current_lines: list[str] = []
    art_counter: dict[str, int] = {}  # voor duplicate art-nrs (bis/ter)

    def flush():
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

        # Stabiel chunk-id op art-nr
        nr = current_article["nr"] or "ongenummerd"
        art_key = f"art_{nr}"
        art_counter[art_key] = art_counter.get(art_key, 0) + 1
        suffix = f"_{art_counter[art_key]}" if art_counter[art_key] > 1 else ""
        chunk_id = f"{source_id}__{art_key}{suffix}"

        full_text = f"{breadcrumb}\n\n{article_heading}\n\n{body}".strip()
        provisional = {
            "id": chunk_id,
            "text": full_text,
            "heading": article_heading,
            "path": path,
            "breadcrumb": breadcrumb,
        }
        for i, fragment in enumerate(split_long_chunk(provisional, MAX_CHUNK_CHARS), 1):
            fid = f"{chunk_id}_part{i}" if fragment.get("_split_part") else chunk_id
            chunks.append({
                "id":          fid,
                "text":        fragment["text"],
                "heading":     fragment["heading"],
                "path":        fragment["path"],
                "breadcrumb":  fragment["breadcrumb"],
                "_split_part": fragment.get("_split_part", ""),
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
            structural_stack[:] = [s for s in structural_stack if s["level"] < parsed["level"]]
            structural_stack.append(parsed)

    flush()
    return chunks


# ---------------------------------------------------------------------------
# Chunking — generiek (normen, adviezen; stabiele id op sectie-slug)
# ---------------------------------------------------------------------------

def split_generic(text: str, source_id: str, breadcrumb_prefix: str = "") -> list[dict]:
    """
    Splitser op iedere `##`-heading. Chunk-id = `<source_id>__sec_<slug>`.
    """
    lines = text.split("\n")
    chunks: list[dict] = []
    current_heading = ""
    current_context = ""
    current_lines: list[str] = []
    slug_counter: dict[str, int] = {}

    def is_structural(line: str) -> bool:
        stripped = line.lstrip("#").strip()
        return bool(STRUCTURAL_PREFIX_RE.match(stripped))

    def flush(heading: str, context: str, body_lines: list[str]):
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

        slug_base = _slug(heading) if heading else "intro"
        slug_counter[slug_base] = slug_counter.get(slug_base, 0) + 1
        suffix = f"_{slug_counter[slug_base]}" if slug_counter[slug_base] > 1 else ""
        chunk_id = f"{source_id}__sec_{slug_base}{suffix}"

        chunks.append({
            "id":              chunk_id,
            "text":            full_text.strip(),
            "heading":         heading,
            "context_heading": context,
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
# Per-bron-rol indexers → allen schrijven naar 'bronnen' collection
# ---------------------------------------------------------------------------

def _mps_safe_batch_size(device: str) -> int:
    """MPS heeft beperkte GPU-buffer per batch — gebruik kleinere batches."""
    return 16 if device == "mps" else 200


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


def index_wetteksten(collection, file_filter: set[str] | None = None, batch_size: int = 200):
    src = BRON_DIRS["wettekst"]
    files = _apply_filter(sorted(src.glob("*.md")), file_filter)
    if not files:
        print(f"  Geen wetteksten{' in scope' if file_filter else ''}")
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
        chunks = split_wettekst(post.content, source_id, fm)

        # Fallback voor bronnen zonder ## Art.-headings
        if not chunks:
            wet_naam = str(fm.get("wet") or fm.get("bron") or source_id)
            chunks = split_generic(post.content, source_id, breadcrumb_prefix=f"[{wet_naam}]")
            for c in chunks:
                c["path"] = [
                    {"type": "wet", "nr": "", "naam": wet_naam},
                    {"type": "sectie", "nr": "", "naam": c.get("heading", "")},
                ]
                c["breadcrumb"] = f"[{wet_naam}]" + (f" → {c['heading']}" if c.get("heading") else "")

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
                "bron_rol":    "wettekst",
                "bron":        str(fm.get("wet", fm.get("bron", path.stem))),
                "bestand":     path.name,
                "artikel_ref": chunk["heading"],
                "themas":      json.dumps(fm.get("tags", [])),
                "itaa_lex":    str(fm.get("itaa-lex-sectie", "")),
                "path":        json.dumps(chunk.get("path", []), ensure_ascii=False),
                "breadcrumb":  chunk.get("breadcrumb", ""),
                "split_part":  chunk.get("_split_part", ""),
                "has_keywords": str(bool(keywords_map.get(chunk["heading"]))),
            })

    if ids:
        _batch_upsert(collection, ids, texts, metadatas, batch_size=batch_size)
    print(f"  {len(ids)} chunks uit {len(files)} wetteksten "
          f"({toc_skipped} TOC-only overgeslagen, {long_split_count} lange artikelen gesplitst)")


def index_normen(collection, file_filter: set[str] | None = None, batch_size: int = 200):
    src = BRON_DIRS["norm"]
    files = [f for f in sorted(src.glob("*.md")) if "INDEX" not in f.name]
    files = _apply_filter(files, file_filter)
    if not files:
        print(f"  Geen normen{' in scope' if file_filter else ''}")
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
        chunks = split_generic(post.content, source_id, breadcrumb_prefix=breadcrumb)

        # Fallback: geen secties gevonden → één chunk voor de hele norm
        if not chunks:
            full_text = f"{breadcrumb}\n\n{post.content.strip()}"
            if len(full_text) >= MIN_CHUNK_CHARS and _has_real_content(full_text):
                ids.append(f"{source_id}__sec_volledig")
                texts.append(full_text)
                metadatas.append({
                    "bron_rol":  "norm",
                    "bron":      norm_naam,
                    "bestand":   path.name,
                    "sectie":    "",
                    "themas":    json.dumps(fm.get("themas", [])),
                    "breadcrumb": breadcrumb,
                })
            continue

        for chunk in chunks:
            if len(chunk["text"]) < MIN_CHUNK_CHARS or not _has_real_content(chunk["text"]):
                continue
            ids.append(chunk["id"])
            texts.append(chunk["text"])
            metadatas.append({
                "bron_rol":  "norm",
                "bron":      norm_naam,
                "bestand":   path.name,
                "sectie":    chunk["heading"],
                "themas":    json.dumps(fm.get("themas", [])),
                "breadcrumb": breadcrumb,
            })

    if ids:
        _batch_upsert(collection, ids, texts, metadatas, batch_size=batch_size)
    print(f"  {len(ids)} chunks uit {len(files)} normen")


def index_adviezen(collection, file_filter: set[str] | None = None, batch_size: int = 200):
    src = BRON_DIRS["advies"]
    files = [f for f in sorted(src.glob("*.md")) if "INDEX" not in f.name]
    files = _apply_filter(files, file_filter)
    if not files:
        print(f"  Geen adviezen{' in scope' if file_filter else ''}")
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

        nummer_raw = str(fm.get("nummer", path.stem))
        nummer = re.sub(r"^CBN[- ]advies\s*", "", nummer_raw).strip()

        h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        onderwerp = h1_match.group(1).strip() if h1_match else ""
        onderwerp = re.sub(r"^CBN[- ]advies\s*\S+\s*—\s*", "", onderwerp).strip()
        if len(onderwerp) > 80:
            onderwerp = onderwerp[:80].rsplit(" ", 1)[0] + "…"

        breadcrumb = f"[CBN-advies {nummer} — {onderwerp}]" if onderwerp else f"[CBN-advies {nummer}]"

        if len(content) <= 40_000 or not re.search(r"^#{2,4} ", content, re.MULTILINE):
            full_text = f"{breadcrumb}\n\n{content}"
            ids.append(f"{source_id}__volledig")
            texts.append(full_text)
            metadatas.append({
                "bron_rol":  "advies",
                "bron":      nummer,
                "bestand":   path.name,
                "sectie":    "",
                "themas":    json.dumps(fm.get("themas", [])),
                "datum":     str(fm.get("datum", "")),
                "breadcrumb": breadcrumb,
            })
        else:
            chunks = split_generic(content, source_id, breadcrumb_prefix=breadcrumb)
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
                    "bron_rol":  "advies",
                    "bron":      nummer,
                    "bestand":   path.name,
                    "sectie":    chunk["heading"],
                    "themas":    json.dumps(fm.get("themas", [])),
                    "datum":     str(fm.get("datum", "")),
                    "breadcrumb": section_breadcrumb,
                })

    if ids:
        _batch_upsert(collection, ids, texts, metadatas, batch_size=batch_size)
    print(f"  {len(ids)} chunks uit {len(files)} adviezen")


# ---------------------------------------------------------------------------
# Concepten-collection (ADR-007)
# ---------------------------------------------------------------------------

def index_concepten(collection, batch_size: int = 200):
    if not CONCEPTS_DIR.exists():
        print(f"  {CONCEPTS_DIR} bestaat nog niet — sla concepten over")
        return

    files = sorted(CONCEPTS_DIR.glob("*.json"))
    if not files:
        print(f"  Geen concept-records in {CONCEPTS_DIR}")
        return

    ids, texts, metadatas = [], [], []

    for path in tqdm(files, desc="concepten"):
        try:
            record = json.loads(path.read_text())
        except Exception as e:
            print(f"  Overgeslagen {path.name}: {e}")
            continue

        concept_id = record.get("id", path.stem)

        def add_chunk(suffix, text, confidence=""):
            if not text or len(text.strip()) < MIN_CHUNK_CHARS:
                return
            ids.append(f"{concept_id}__{suffix}")
            texts.append(text.strip())
            metadatas.append({
                "bron_rol":   "concept",
                "concept_id": concept_id,
                "bestand":    path.name,
                "veld":       suffix,
                "confidence": confidence,
            })

        naam = record.get("naam", concept_id)
        node_type = record.get("node_type", "")

        mr = record.get("main_rule", {})
        if mr:
            add_chunk("main_rule", f"{naam}\n\n{mr.get('text', '')}", mr.get("confidence", ""))

        definitie = record.get("definitie", {})
        if definitie:
            add_chunk("definitie", f"{naam}\n\n{definitie.get('text', '')}", definitie.get("confidence", ""))

        for i, exc in enumerate(record.get("exceptions", [])):
            add_chunk(f"exception_{i}", f"{naam} — uitzondering\n\n{exc.get('text', '')}", exc.get("confidence", ""))

        scope = record.get("scope", {})
        if scope:
            scope_text = (
                f"{naam} — toepassingsgebied\n\n"
                f"Van toepassing op: {scope.get('applies_to', '')}\n"
                f"Uitgesloten: {scope.get('excludes', '')}"
            )
            add_chunk("scope", scope_text)

        for i, pit in enumerate(record.get("pitfalls", [])):
            add_chunk(f"pitfall_{i}", f"{naam} — valkuil\n\n{pit.get('text', '')}", pit.get("confidence", "inferred"))

        for i, ex in enumerate(record.get("voorbeeld_inline", record.get("examples", []))):
            if isinstance(ex, dict):
                add_chunk(f"voorbeeld_{i}", f"{naam} — voorbeeld\n\n{ex.get('text', '')}", ex.get("confidence", ""))
            else:
                add_chunk(f"voorbeeld_{i}", f"{naam} — voorbeeld\n\n{ex}")

    if ids:
        _batch_upsert(collection, ids, texts, metadatas, batch_size=batch_size)
    print(f"  {len(ids)} chunks uit {len(files)} concept-records")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Bouw de Certificaid RAG-index (ADR-006)")
    parser.add_argument("--bron-rol", choices=["wettekst", "norm", "advies"],
                        help="Indexeer alleen deze bron-rol (default: alle drie)")
    parser.add_argument("--scope",
                        help="Pad naar bronnen-scope.yaml — schrijft naar aparte chroma_db_<programmaonderdeel>/")
    parser.add_argument("--add-concepten", action="store_true",
                        help="Indexeer of vernieuw concept-records in de concepten-collection")
    parser.add_argument("--reset", action="store_true",
                        help="Verwijder en herbouw de collection(s)")
    parser.add_argument("--device", choices=["mps", "cuda", "cpu"],
                        help="Device voor embedding-model (default: auto-detect)")
    args = parser.parse_args()

    device = args.device or detect_device()
    print(f"→ Device: {device}")

    file_filter: dict[str, set[str]] = {}
    chroma_path = DEFAULT_CHROMA_PATH
    if args.scope:
        programmaonderdeel, file_filter, chroma_path = load_scope(Path(args.scope))
        print(f"→ Scope: {programmaonderdeel} — {chroma_path.name}")
    print(f"→ ChromaDB: {chroma_path}")

    ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL, device=device)
    batch_size = _mps_safe_batch_size(device)
    client = get_client(chroma_path)

    if args.add_concepten:
        print("\n→ Indexeer collection: concepten")
        col, client = get_collection(client, chroma_path, "concepten", ef, reset=args.reset)
        index_concepten(col, batch_size=batch_size)
    else:
        print("\n→ Indexeer collection: bronnen")
        col, client = get_collection(client, chroma_path, "bronnen", ef, reset=args.reset)

        rollen = [args.bron_rol] if args.bron_rol else ["wettekst", "norm", "advies"]
        for rol in rollen:
            scope_for_rol = file_filter.get(rol) if args.scope else None
            if args.scope and scope_for_rol is not None and not scope_for_rol:
                print(f"  Geen {rol}en in scope — overgeslagen")
                continue
            if rol == "wettekst":
                index_wetteksten(col, scope_for_rol, batch_size=batch_size)
            elif rol == "norm":
                index_normen(col, scope_for_rol, batch_size=batch_size)
            elif rol == "advies":
                index_adviezen(col, scope_for_rol, batch_size=batch_size)

    print("\n✓ Klaar.")


if __name__ == "__main__":
    main()
