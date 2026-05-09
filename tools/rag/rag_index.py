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
import hashlib
import json
import os
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
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.lib.provenance import read_trust  # noqa: E402
DEFAULT_CHROMA_PATH = ROOT / "data" / "chroma_db"
EMBEDDING_MODEL = "BAAI/bge-m3"   # zie ADR-006
KEYWORDS_DIR = ROOT / "resources" / "bronnen" / "wetteksten" / "keywords"

# PYTORCH_ENABLE_MPS_FALLBACK is bewust UIT: de fallback ping-pong tussen
# MPS en CPU lekt geheugen bij lange runs (Mac stottert progressief).
# In plaats daarvan: max_seq_length op het model beperken zodat MPS nooit
# een te grote attention-buffer hoeft te alloceren.
MPS_MAX_SEQ_LENGTH = 2048   # ~8K chars; bedekt ~95% van chunks (avg 1.5K chars)
                            # Lange chunks (>8K chars) truncaten in de tail,
                            # maar de header+breadcrumb+begin staan altijd in de embedding

BRON_DIRS = {
    "wettekst": ROOT / "resources" / "bronnen" / "wetteksten",
    "norm":     ROOT / "resources" / "bronnen" / "normen",
    "advies":   ROOT / "resources" / "bronnen" / "adviezen",
}
CONCEPTS_DIR = ROOT / "data" / "concept_records"

MIN_CHUNK_CHARS = 100
# Aligneren met MPS_MAX_SEQ_LENGTH (2048 tokens ≈ 8K chars) zodat elke char
# in elke chunk daadwerkelijk in de embedding zit. Voorheen: 24K chars,
# maar dan wordt de tail van lange chunks niet ge-embed bij max_seq_length=2048.
MAX_CHUNK_CHARS = 8_000


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
    # Plural-mapping: NL meervoud is niet altijd +"en". Voor "advies" → "adviezen".
    PLURAL = {"wettekst": "wetteksten", "norm": "normen", "advies": "adviezen"}
    for rol in BRON_DIRS:
        files = raw.get(PLURAL[rol], raw.get(rol, [])) or []
        file_filter[rol] = set(files)
    chroma_path = ROOT / "data" / f"chroma_db_{programmaonderdeel}"
    return programmaonderdeel, file_filter, chroma_path


def _apply_filter(files: list[Path], allowed: set[str] | None) -> list[Path]:
    if allowed is None:
        return files
    return [f for f in files if f.name in allowed]


def _apply_trust_filter(
    files: list[Path], *, include_unreviewed: bool = False,
) -> tuple[list[Path], dict[str, int], dict[Path, "Trust"]]:
    """Filter op `provenance.trust.status == "trusted"` (ADR-005 §5).

    Returnt (kept, skipped_counts, trust_per_path):
      - kept: files die geïndexeerd mogen worden
      - skipped_counts: dict {status: aantal} van geweerde bestanden
      - trust_per_path: cache van Trust-objecten zodat indexers de metadata
        niet opnieuw hoeven uitlezen

    Met `--include-unreviewed` (opt-in) gaat de filter uit en worden ALLE
    bronnen geïndexeerd ongeacht status. Trust-metadata wordt nog steeds
    in ChromaDB-metadata geschreven, zodat retrieval-time-filtering nog werkt.
    """
    kept: list[Path] = []
    skipped: dict[str, int] = {}
    trust_per_path: dict[Path, "Trust"] = {}
    for f in files:
        t = read_trust(f)
        trust_per_path[f] = t
        if include_unreviewed or t.status == "trusted":
            kept.append(f)
        else:
            skipped[t.status] = skipped.get(t.status, 0) + 1
    return kept, skipped, trust_per_path


def _format_trust_skip_msg(rol: str, skipped: dict[str, int]) -> str:
    if not skipped:
        return ""
    parts = ", ".join(f"{k}: {v}" for k, v in sorted(skipped.items()))
    total = sum(skipped.values())
    return f"  → {total} {rol}-bron(nen) geskipt op trust-status ({parts})"


# ---------------------------------------------------------------------------
# Frontmatter / keywords helpers
# ---------------------------------------------------------------------------

def _load_keywords(stem: str) -> dict:
    """
    Laad optionele chunk-level keywords voor een bron (wordt prepended vóór embedding).

    Enkel nog gebruikt voor KeyBERT auto-gegenereerde keywords als extra context.
    Vocabulairekloven worden opgelost via query-time expansion (synoniemen in
    vermoedens-JSON, gegenereerd door de LLM die de vermoedens schrijft).
    """
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

def _merge_bis_ter(chunks: list[dict], max_chars: int) -> list[dict]:
    """
    Merge artikelen met suffix (bis, ter, quater, ...) in de chunk van het
    basisartikel. Art. 458 + 458bis + 458ter + 458quater worden één chunk.

    Logica:
    - Een artikel-nr met suffix (eindigend op 'bis', 'ter', 'quater', cijfer+letter)
      wordt beschouwd als verlengstuk van het basisartikel dat er onmiddellijk
      aan voorafgaat.
    - Merge stopt als gecombineerde chunk-grootte > max_chars.
    - Chunk-id van de samengevoegde chunk = eerste artikel in de serie.
    """
    if not chunks:
        return chunks

    _SUFFIX_RE = re.compile(
        r"^([A-Za-z0-9]+?)(bis|ter|quater|quinquies|sexies|septies|octies|"
        r"nonies|decies|\d+[a-z]+)$",
        re.IGNORECASE,
    )

    def basisnummer(nr: str) -> str:
        """Strip suffix: '458bis' → '458', '131/2' → '131/2' (ongewijzigd)."""
        m = _SUFFIX_RE.match(nr)
        return m.group(1) if m else nr

    resultaat: list[dict] = []
    i = 0
    while i < len(chunks):
        hoofd = chunks[i]
        hoofd_nr = hoofd.get("_art_nr", "")
        hoofd_basis = basisnummer(hoofd_nr)

        # Zoek volgende artikelen met hetzelfde basisnummer
        j = i + 1
        te_mergen = [hoofd]
        while j < len(chunks):
            volg = chunks[j]
            volg_nr = volg.get("_art_nr", "")
            volg_basis = basisnummer(volg_nr)
            if volg_basis != hoofd_basis:
                break
            if volg_basis == hoofd_basis and volg_nr != hoofd_nr:
                # Controleer of gecombineerde grootte nog past
                huidige_len = sum(len(c["text"]) for c in te_mergen)
                if huidige_len + len(volg["text"]) > max_chars:
                    break
                te_mergen.append(volg)
                j += 1
            else:
                break

        if len(te_mergen) == 1:
            resultaat.append(hoofd)
        else:
            # Samenvoegen: tekst met lege regel ertussen
            combined_text = "\n\n".join(c["text"] for c in te_mergen)
            merged = dict(hoofd)
            merged["text"] = combined_text
            # Behoud heading van eerste artikel; voeg suffixen toe als notitie
            suffixen = [c.get("_art_nr", "") for c in te_mergen[1:]]
            merged["heading"] = hoofd["heading"] + (
                f" [+ {', '.join(suffixen)}]" if suffixen else ""
            )
            resultaat.append(merged)

        i = j

    return resultaat


def split_wettekst(text: str, source_id: str, fm: dict) -> list[dict]:
    """
    Splits markdown op artikel-headings. Sub-headings blijven inline.
    Chunk-id = `<source_id>__art_<nr>` (stabiel, zie ADR-006 §3.1).

    Preprocessing:
    - Plain-text structuurlabels (BOEK, TITEL, HOOFDSTUK, AFDELING, ...)
      worden omgezet naar markdown-headings zodat ze in de context-stack
      worden meegenomen (breadcrumb).
    - Bis/ter/quater-artikelen worden gemerged met hun basisartikel.
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
                "_art_nr":     nr,   # voor bis/ter-merge
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
    return _merge_bis_ter(chunks, MAX_CHUNK_CHARS)


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
    """ChromaDB-upsert batch grootte. Iets kleiner op MPS i.v.m. geheugen."""
    return 64 if device == "mps" else 200


def make_embedding_function(model_name: str, device: str):
    """
    ChromaDB-compatibele embedding-functie.

    Op MPS: max_seq_length=1024 om MPS-attention-buffer overflow te voorkomen
    (bge-m3 default = 8192, te groot voor MPS bij lange chunks).
    Tussen batches torch.mps.empty_cache() om geheugenlek te voorkomen.
    Hierdoor is PYTORCH_ENABLE_MPS_FALLBACK NIET nodig — geen ping-pong, geen leak.
    """
    if device == "mps":
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer(model_name, device=device)
        # Beperk seq-length: 1024 tokens (~4K chars) past zeker in MPS-buffer
        model.max_seq_length = MPS_MAX_SEQ_LENGTH

        class MPSEmbeddingFunction:
            def name(self) -> str:          # vereist door nieuwere ChromaDB versies
                return "mps-bge-m3"

            def __call__(self, input: list[str]) -> list[list[float]]:
                embeddings = model.encode(
                    input,
                    batch_size=8,             # snel zonder buffer-overflow
                    show_progress_bar=False,
                    normalize_embeddings=True,
                )
                # Expliciete cache-flush tegen MPS geheugenlek
                torch.mps.empty_cache()
                return embeddings.tolist()

        return MPSEmbeddingFunction()

    return SentenceTransformerEmbeddingFunction(model_name=model_name, device=device)


def _chunk_sha(text: str) -> str:
    """SHA256 van chunk-tekst, eerste 16 hex-chars (voldoende voor collision-detectie)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def _fetch_existing_shas(collection, ids: list[str]) -> dict[str, str]:
    """
    Haal bestaande chunk_sha-metadata op voor de opgegeven IDs.
    Retourneert {chunk_id: sha}. Ontbrekende IDs zijn gewoon afwezig in het dict.
    """
    if not ids:
        return {}
    try:
        # ChromaDB retourneert alleen IDs die bestaan — ontbrekende worden stil overgeslagen
        result = collection.get(ids=ids, include=["metadatas"])
        return {
            eid: em.get("chunk_sha", "")
            for eid, em in zip(result["ids"], result["metadatas"])
        }
    except Exception:
        return {}


def _batch_upsert(collection, ids, texts, metadatas, batch_size: int = 200):
    """
    Embed en upsert chunks — sla chunks over waarvan de tekst niet veranderd is
    (chunk_sha-vergelijking, ADR-004).

    Algoritme:
      1. Bereken SHA voor elke chunk-tekst
      2. Haal bestaande SHA's op uit ChromaDB (één batch-get)
      3. Filter: alleen nieuwe of gewijzigde chunks doorsturen naar het embedding-model
      4. Voeg chunk_sha toe aan metadata zodat de volgende run kan vergelijken
    """
    n = len(ids)
    if n == 0:
        return

    shas = [_chunk_sha(t) for t in texts]
    existing = _fetch_existing_shas(collection, ids)

    nieuwe_ids: list[str] = []
    nieuwe_texts: list[str] = []
    nieuwe_metas: list[dict] = []

    for chunk_id, text, meta, sha in zip(ids, texts, metadatas, shas):
        if existing.get(chunk_id) == sha:
            continue   # ongewijzigd → skip embedding
        meta = dict(meta)
        meta["chunk_sha"] = sha
        nieuwe_ids.append(chunk_id)
        nieuwe_texts.append(text)
        nieuwe_metas.append(meta)

    overgeslagen = n - len(nieuwe_ids)
    if overgeslagen:
        print(f"    {overgeslagen}/{n} chunks ongewijzigd → overgeslagen")
    if not nieuwe_ids:
        return

    n_nieuw = len(nieuwe_ids)
    n_batches = (n_nieuw + batch_size - 1) // batch_size
    for i in tqdm(range(0, n_nieuw, batch_size), desc="    embedden", total=n_batches):
        collection.upsert(
            ids=nieuwe_ids[i:i + batch_size],
            documents=nieuwe_texts[i:i + batch_size],
            metadatas=nieuwe_metas[i:i + batch_size],
        )


def index_wetteksten(
    collection,
    file_filter: set[str] | None = None,
    batch_size: int = 200,
    *,
    include_unreviewed: bool = False,
):
    src = BRON_DIRS["wettekst"]
    files = _apply_filter(sorted(src.glob("*.md")), file_filter)
    if not files:
        print(f"  Geen wetteksten{' in scope' if file_filter else ''}")
        return

    files, trust_skipped, trust_per_path = _apply_trust_filter(files, include_unreviewed=include_unreviewed)
    msg = _format_trust_skip_msg("wettekst", trust_skipped)
    if msg:
        print(msg)
    if not files:
        print("  Geen trusted wetteksten — niets te indexeren")
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
            t = trust_per_path.get(path)
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
                "trust_status":       t.status if t else "unknown",
                "trust_confirmed_by": t.confirmed_by or "" if t else "",
            })

    if ids:
        _batch_upsert(collection, ids, texts, metadatas, batch_size=batch_size)
    print(f"  {len(ids)} chunks uit {len(files)} wetteksten "
          f"({toc_skipped} TOC-only overgeslagen, {long_split_count} lange artikelen gesplitst)")


def index_normen(
    collection,
    file_filter: set[str] | None = None,
    batch_size: int = 200,
    *,
    include_unreviewed: bool = False,
):
    src = BRON_DIRS["norm"]
    files = [f for f in sorted(src.glob("*.md")) if "INDEX" not in f.name]
    files = _apply_filter(files, file_filter)
    if not files:
        print(f"  Geen normen{' in scope' if file_filter else ''}")
        return

    files, trust_skipped, trust_per_path = _apply_trust_filter(files, include_unreviewed=include_unreviewed)
    msg = _format_trust_skip_msg("norm", trust_skipped)
    if msg:
        print(msg)
    if not files:
        print("  Geen trusted normen — niets te indexeren")
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

        # Fallback: geen secties gevonden → splits op alinea-grenzen om mega-chunks
        # te vermijden (bv. ITAA-norm-aww-geconsolideerd.md heeft 0 headings, ~50K chars)
        if not chunks:
            full_text = f"{breadcrumb}\n\n{post.content.strip()}"
            if len(full_text) < MIN_CHUNK_CHARS or not _has_real_content(full_text):
                continue
            base_chunk = {
                "id": f"{source_id}__sec_volledig",
                "text": full_text,
                "heading": "",
                "path": [],
                "breadcrumb": breadcrumb,
            }
            for fragment in split_long_chunk(base_chunk, MAX_CHUNK_CHARS):
                part = fragment.get("_split_part", "")
                fid = (
                    f"{source_id}__sec_volledig_part{part.split('/')[0]}"
                    if part else f"{source_id}__sec_volledig"
                )
                ids.append(fid)
                texts.append(fragment["text"])
                t = trust_per_path.get(path)
                metadatas.append({
                    "bron_rol":  "norm",
                    "bron":      norm_naam,
                    "bestand":   path.name,
                    "sectie":    "",
                    "themas":    json.dumps(fm.get("themas", [])),
                    "breadcrumb": breadcrumb,
                    "split_part": part,
                    "trust_status":       t.status if t else "unknown",
                    "trust_confirmed_by": t.confirmed_by or "" if t else "",
                })
            continue

        for chunk in chunks:
            if len(chunk["text"]) < MIN_CHUNK_CHARS or not _has_real_content(chunk["text"]):
                continue
            # Splits ook hier: één H1-norm zonder verdere headings produceert
            # vaak één megachunk. ADR-006 §4: hard max 24K chars.
            for fragment in split_long_chunk(chunk, MAX_CHUNK_CHARS):
                part = fragment.get("_split_part", "")
                fid = f"{chunk['id']}_part{part.split('/')[0]}" if part else chunk["id"]
                ids.append(fid)
                texts.append(fragment["text"])
                t = trust_per_path.get(path)
                metadatas.append({
                    "bron_rol":  "norm",
                    "bron":      norm_naam,
                    "bestand":   path.name,
                    "sectie":    chunk["heading"],
                    "themas":    json.dumps(fm.get("themas", [])),
                    "breadcrumb": breadcrumb,
                    "split_part": part,
                    "trust_status":       t.status if t else "unknown",
                    "trust_confirmed_by": t.confirmed_by or "" if t else "",
                })

    if ids:
        _batch_upsert(collection, ids, texts, metadatas, batch_size=batch_size)
    print(f"  {len(ids)} chunks uit {len(files)} normen")


def index_adviezen(
    collection,
    file_filter: set[str] | None = None,
    batch_size: int = 200,
    *,
    include_unreviewed: bool = False,
):
    src = BRON_DIRS["advies"]
    files = [f for f in sorted(src.glob("*.md")) if "INDEX" not in f.name]
    files = _apply_filter(files, file_filter)
    if not files:
        print(f"  Geen adviezen{' in scope' if file_filter else ''}")
        return

    files, trust_skipped, trust_per_path = _apply_trust_filter(files, include_unreviewed=include_unreviewed)
    msg = _format_trust_skip_msg("advies", trust_skipped)
    if msg:
        print(msg)
    if not files:
        print("  Geen trusted adviezen — niets te indexeren")
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
            base_chunk = {
                "id": f"{source_id}__volledig",
                "text": full_text,
                "heading": "",
                "path": [],
                "breadcrumb": breadcrumb,
            }
            for fragment in split_long_chunk(base_chunk, MAX_CHUNK_CHARS):
                part = fragment.get("_split_part", "")
                fid = f"{source_id}__volledig_part{part.split('/')[0]}" if part else f"{source_id}__volledig"
                ids.append(fid)
                texts.append(fragment["text"])
                t = trust_per_path.get(path)
                metadatas.append({
                    "bron_rol":  "advies",
                    "bron":      nummer,
                    "bestand":   path.name,
                    "sectie":    "",
                    "themas":    json.dumps(fm.get("themas", [])),
                    "datum":     str(fm.get("datum", "")),
                    "breadcrumb": breadcrumb,
                    "split_part": part,
                    "trust_status":       t.status if t else "unknown",
                    "trust_confirmed_by": t.confirmed_by or "" if t else "",
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
                for fragment in split_long_chunk(chunk, MAX_CHUNK_CHARS):
                    part = fragment.get("_split_part", "")
                    fid = f"{chunk['id']}_part{part.split('/')[0]}" if part else chunk["id"]
                    ids.append(fid)
                    texts.append(fragment["text"])
                    t = trust_per_path.get(path)
                    metadatas.append({
                        "bron_rol":  "advies",
                        "bron":      nummer,
                        "bestand":   path.name,
                        "sectie":    chunk["heading"],
                        "themas":    json.dumps(fm.get("themas", [])),
                        "datum":     str(fm.get("datum", "")),
                        "breadcrumb": section_breadcrumb,
                        "split_part": part,
                        "trust_status":       t.status if t else "unknown",
                        "trust_confirmed_by": t.confirmed_by or "" if t else "",
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
    parser.add_argument("--include-unreviewed", action="store_true",
                        help="Indexeer ook bronnen met trust.status != trusted "
                             "(default: alleen trusted, ADR-005 §5).")
    args = parser.parse_args()

    device = args.device or detect_device()
    print(f"→ Device: {device}")

    file_filter: dict[str, set[str]] = {}
    chroma_path = DEFAULT_CHROMA_PATH
    if args.scope:
        programmaonderdeel, file_filter, chroma_path = load_scope(Path(args.scope))
        print(f"→ Scope: {programmaonderdeel} — {chroma_path.name}")
    print(f"→ ChromaDB: {chroma_path}")

    ef = make_embedding_function(EMBEDDING_MODEL, device)
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
                index_wetteksten(col, scope_for_rol, batch_size=batch_size,
                                 include_unreviewed=args.include_unreviewed)
            elif rol == "norm":
                index_normen(col, scope_for_rol, batch_size=batch_size,
                             include_unreviewed=args.include_unreviewed)
            elif rol == "advies":
                index_adviezen(col, scope_for_rol, batch_size=batch_size,
                               include_unreviewed=args.include_unreviewed)

    print("\n✓ Klaar.")


if __name__ == "__main__":
    main()
