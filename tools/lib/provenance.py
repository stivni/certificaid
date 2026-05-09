"""Provenance helpers for Certificaid artefacts.

Schema and rationale: docs/adr/ADR-004-provenance.md.
Workflow that consumes this (stale-cascade, regressie-gates): docs/adr/ADR-003-reprocessing-evaluatie.md.

YAML writes use ruamel.yaml round-trip mode so existing frontmatter formatting
(key order, quote style, list flow vs. block) is preserved.

JSON writes (concept-records) use string-append for initial inserts to preserve
existing formatting; replacements fall back to json.dumps reformat.

Concept-record per-veld provenance (ADR-007 schema 1.1 + ADR-008 §10):
----------------------------------------------------------------------
  Elk block-veld (main_rule, definitie, verplichting, stappen[], …) heeft
  een inline `_provenance`-sub-object met de chunk-ids die de LLM-extractor
  voor dit specifieke veld heeft gebruikt.

  Schema per veld:
    {
      "inputs": [{"id": "<chunk_id>", "sha256": "<chunk_sha>", "version": "rag-v1"}],
      "extracted_at": "<ISO-tijdstip>",
      "extractor": "<versie-label>",
      "stale": false,           # pas aanwezig na mark_stale.py
      "stale_reason": null      # pas aanwezig na mark_stale.py
    }

  Top-level `_provenance` op het record: alleen record-metadata
    (extractor_run, model, reviewed_by) — géén chunk-inputs.

  walk_concept_provenance(record) → iterator van (veldpad, provenance-dict)
    zodat mark_stale.py per veld kan beslissen.
  mark_field_stale(record, veldpad, reden) → werkt record in-place bij.
  sha_voor_chunk(chunk_id, chroma_collection) → haalt chunk_sha op uit ChromaDB.
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, Optional

from ruamel.yaml import YAML

PROVENANCE_KEY_MD = "provenance"        # YAML frontmatter key (.md)
PROVENANCE_KEY_JSON = "_provenance"     # top-level JSON field (.json)

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def _yaml() -> YAML:
    y = YAML()
    y.preserve_quotes = True
    # 2-space indented block sequences (`themas:\n  - x`) — matches the dominant
    # style in the existing corpus. Round-trip mode preserves per-block detected
    # styles when they differ.
    y.indent(mapping=2, sequence=4, offset=2)
    y.width = 4096  # avoid line-wrapping on long values
    return y


@dataclass
class Input:
    id: str
    sha256: Optional[str] = None  # None for URL-sourced inputs we don't locally cache
    version: Optional[str] = None


@dataclass
class Tooling:
    pipeline: str
    pipeline_version: str
    model: Optional[str] = None
    prompt_version: Optional[str] = None


# Trust-statussen — zie ADR-005 §5 (kwaliteits-gate output).
TRUST_VALID_STATUSES = ("unreviewed", "trusted", "needs-rework", "rejected")


@dataclass
class Trust:
    """QA-uitkomst per bron-MD; bepaalt of rag_index.py de bron oppakt.

    - unreviewed: default; nog niet beoordeeld → niet geïndexeerd
    - trusted:    bevestigd OK voor RAG → geïndexeerd
    - needs-rework: ETL-fix nodig voor we het in de index willen
    - rejected:   structureel niet bruikbaar; weglaten
    """
    status: str = "unreviewed"
    qa_version: Optional[str] = None
    confirmed_at: Optional[str] = None
    confirmed_by: Optional[str] = None
    rationale: Optional[str] = None

    def __post_init__(self) -> None:
        if self.status not in TRUST_VALID_STATUSES:
            raise ValueError(
                f"Invalid trust status: {self.status!r}; "
                f"expected one of {TRUST_VALID_STATUSES}"
            )


def default_trust() -> Trust:
    """Default trust voor bronnen zonder expliciete trust-marking."""
    return Trust(status="unreviewed", confirmed_by="default")


@dataclass
class Provenance:
    inputs: list[Input]
    tooling: Tooling
    generated_at: str
    stale: bool = False
    stale_reason: Optional[str] = None
    trust: Optional[Trust] = None

    def to_dict(self) -> dict:
        d = {
            "inputs": [asdict(i) for i in self.inputs],
            "tooling": asdict(self.tooling),
            "generated_at": self.generated_at,
            "stale": self.stale,
            "stale_reason": self.stale_reason,
        }
        if self.trust is not None:
            d["trust"] = asdict(self.trust)
        return d

    @classmethod
    def from_dict(cls, data: dict) -> "Provenance":
        trust_data = data.get("trust")
        return cls(
            inputs=[Input(**i) for i in data["inputs"]],
            tooling=Tooling(**data["tooling"]),
            generated_at=data["generated_at"],
            stale=data.get("stale", False),
            stale_reason=data.get("stale_reason"),
            trust=Trust(**trust_data) if trust_data else None,
        )


def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def git_short_sha(file_path: Path, repo_root: Optional[Path] = None) -> str:
    """Latest commit short-sha touching file_path; suffix '-dirty' if uncommitted local edits."""
    cwd = repo_root or Path.cwd()
    try:
        sha = subprocess.check_output(
            ["git", "log", "-1", "--format=%h", "--", str(file_path)],
            cwd=cwd,
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        if not sha:
            return "uncommitted"
        diff = subprocess.run(
            ["git", "diff", "--quiet", "HEAD", "--", str(file_path)],
            cwd=cwd,
        )
        if diff.returncode != 0:
            return f"{sha}-dirty"
        return sha
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def make_input(path: Path, *, version: Optional[str] = None, repo_root: Optional[Path] = None) -> Input:
    """Build an Input for a local file (with sha256)."""
    rel = path.relative_to(repo_root) if repo_root else path
    return Input(id=str(rel), sha256=hash_file(path), version=version)


def make_url_input(url: str, *, version: Optional[str] = None) -> Input:
    """Build an Input for a remote URL (no sha256; only id-presence stale-detection)."""
    return Input(id=url, sha256=None, version=version)


def make_provenance(
    inputs: list[Input],
    pipeline: str,
    *,
    repo_root: Optional[Path] = None,
    model: Optional[str] = None,
    prompt_version: Optional[str] = None,
) -> Provenance:
    return Provenance(
        inputs=inputs,
        tooling=Tooling(
            pipeline=pipeline,
            pipeline_version=git_short_sha(Path(pipeline), repo_root=repo_root),
            model=model,
            prompt_version=prompt_version,
        ),
        generated_at=now_iso(),
    )


def read_provenance(path: Path) -> Optional[Provenance]:
    """Read provenance block from .md (frontmatter) or .json (top-level field)."""
    if path.suffix == ".json":
        return _read_provenance_json(path)
    return _read_provenance_md(path)


def write_provenance(path: Path, prov: Provenance) -> None:
    """Add or replace the provenance block. Dispatches on file suffix."""
    if path.suffix == ".json":
        _write_provenance_json(path, prov)
    else:
        _write_provenance_md(path, prov)


def _read_provenance_md(md_path: Path) -> Optional[Provenance]:
    text = md_path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None
    data = _yaml().load(m.group(1)) or {}
    block = data.get(PROVENANCE_KEY_MD)
    if block is None:
        return None
    return Provenance.from_dict(_to_plain(block))


def _write_provenance_md(md_path: Path, prov: Provenance) -> None:
    text = md_path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    yaml = _yaml()
    if m:
        data = yaml.load(m.group(1)) or {}
        body = text[m.end():]
    else:
        data = {}
        body = text
    data[PROVENANCE_KEY_MD] = prov.to_dict()
    buf = io.StringIO()
    yaml.dump(data, buf)
    md_path.write_text(f"---\n{buf.getvalue()}---\n{body}", encoding="utf-8")


def _read_provenance_json(json_path: Path) -> Optional[Provenance]:
    data = json.loads(json_path.read_text(encoding="utf-8"))
    block = data.get(PROVENANCE_KEY_JSON)
    if block is None:
        return None
    return Provenance.from_dict(block)


def _write_provenance_json(json_path: Path, prov: Provenance) -> None:
    """Insert or replace _provenance in a JSON file.

    Initial insert uses string-append to preserve existing formatting (mixed
    inline/indented objects). Replacement of an existing block falls back to
    a full json.dumps reformat (rare path; acceptable).
    """
    text = json_path.read_text(encoding="utf-8")
    data = json.loads(text)
    has_existing = PROVENANCE_KEY_JSON in data

    if has_existing:
        data[PROVENANCE_KEY_JSON] = prov.to_dict()
        json_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        return

    # Initial insert — preserve existing formatting via string append.
    prov_block = json.dumps(prov.to_dict(), indent=2, ensure_ascii=False)
    # Indent each subsequent line by 2 to nest under the parent object.
    indented_block = prov_block.replace("\n", "\n  ")

    stripped = text.rstrip()
    if not stripped.endswith("}"):
        raise ValueError(f"{json_path}: top-level JSON does not end with '}}'")
    body = stripped[:-1].rstrip()
    sep = "" if body.endswith(",") or body.endswith("{") else ","
    new_text = f'{body}{sep}\n  "{PROVENANCE_KEY_JSON}": {indented_block}\n}}\n'
    json_path.write_text(new_text, encoding="utf-8")


def _to_plain(obj):
    """Recursively convert ruamel.yaml CommentedMap/Seq to plain dict/list."""
    if hasattr(obj, "items"):
        return {k: _to_plain(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_to_plain(v) for v in obj]
    return obj


def read_trust(path: Path) -> Trust:
    """Lees trust-blok van een bron-MD (of JSON met _provenance).

    Geeft altijd een Trust terug — ontbrekende trust of ontbrekende provenance
    wordt geïnterpreteerd als default `Trust(status="unreviewed", confirmed_by="default")`.
    Indexer kan dus altijd `read_trust(path).status == "trusted"` gebruiken.
    """
    prov = read_provenance(path)
    if prov is None or prov.trust is None:
        return default_trust()
    return prov.trust


def mark_trust(
    path: Path,
    status: str,
    *,
    confirmed_by: str = "human",
    rationale: Optional[str] = None,
    qa_version: Optional[str] = None,
) -> Trust:
    """Update het trust-blok op een bron-MD. Schrijft naar provenance.trust.

    Vereist dat het bestand al een provenance-blok heeft (run
    `tools/etl/backfill_trust_unreviewed.py` of `tools/etl/add_provenance.py` eerst).

    Returnt de nieuwe Trust.
    """
    prov = read_provenance(path)
    if prov is None:
        raise ValueError(
            f"{path}: geen provenance-blok aanwezig. "
            f"Run eerst tools/etl/backfill_trust_unreviewed.py of add_provenance.py."
        )
    new_trust = Trust(
        status=status,
        qa_version=qa_version,
        confirmed_at=now_iso(),
        confirmed_by=confirmed_by,
        rationale=rationale,
    )
    prov.trust = new_trust
    write_provenance(path, prov)
    return new_trust


def detect_stale(recorded: Provenance, current_inputs: list[Input]) -> tuple[bool, Optional[str]]:
    """Compare recorded inputs against currently-resolved inputs. Returns (is_stale, reason).

    Inputs without sha256 (e.g. URL-sourced) are checked only on id-presence,
    not on content. Real content-based detection requires a local cache.
    """
    rec = {i.id: i.sha256 for i in recorded.inputs}
    cur = {i.id: i.sha256 for i in current_inputs}
    if rec.keys() != cur.keys():
        added = sorted(cur.keys() - rec.keys())
        removed = sorted(rec.keys() - cur.keys())
        parts = []
        if added:
            parts.append(f"new inputs: {added}")
        if removed:
            parts.append(f"removed inputs: {removed}")
        return True, "; ".join(parts)
    for k, cur_hash in cur.items():
        if rec[k] is None or cur_hash is None:
            continue  # no content hash available; cannot detect content drift
        if rec[k] != cur_hash:
            return True, f"input changed: {k}"
    return False, None


# ─── Concept-record per-veld provenance (ADR-007 schema 1.1 + ADR-008 §10) ──

def walk_concept_provenance(
    record: dict,
    *,
    _path: str = "",
    _is_top_level: bool = True,
) -> Iterator[tuple[str, dict]]:
    """Genereer (veldpad, provenance-dict) voor elk block-veld met inline _provenance.

    Slaat de top-level `_provenance` over — dat is record-metadata, geen veld-provenance.
    Walkt recursief door geneste dicts (uitzondering, bouwstenen, stappen, …) en lists.

    Geeft alleen velden terug waarvan `_provenance` een dict is met een `inputs`-sleutel.
    Velden zonder provenance worden stilzwijgend overgeslagen (ADR-008 §11: niet alles is
    bron-gestuurd).

    Voorbeeld gebruik:
        for veldpad, prov_blok in walk_concept_provenance(record):
            for inp in prov_blok.get("inputs", []):
                print(veldpad, inp["id"])
    """
    if not isinstance(record, dict):
        return

    prov = record.get("_provenance")
    if not _is_top_level and isinstance(prov, dict) and "inputs" in prov:
        yield _path, prov

    for sleutel, waarde in record.items():
        if sleutel == "_provenance":
            continue
        nieuw_pad = f"{_path}.{sleutel}" if _path else sleutel
        if isinstance(waarde, dict):
            yield from walk_concept_provenance(waarde, _path=nieuw_pad, _is_top_level=False)
        elif isinstance(waarde, list):
            for index, item in enumerate(waarde):
                if isinstance(item, dict):
                    yield from walk_concept_provenance(
                        item, _path=f"{nieuw_pad}[{index}]", _is_top_level=False
                    )


def _zet_veld_via_pad(record: dict, veldpad: str, sleutel: str, waarde: object) -> bool:
    """Navigeer naar het object op veldpad en zet `sleutel = waarde`.

    Veldpad-syntaxis: "main_rule", "stappen[0]", "uitzonderingen[1].tekst", …
    Returnt True als de navigatie slaagde; False als het pad niet gevonden werd.
    """
    # Splits pad in segmenten. Elk segment is ofwel een sleutelnaam of een sleutelnaam
    # gevolgd door een lijstindex tussen vierkante haken.
    _SEGMENT_RE = re.compile(r"([^\[.]+)(?:\[(\d+)\])?")
    segmenten = _SEGMENT_RE.findall(veldpad)
    huidige = record
    for naam, index in segmenten:
        if naam not in huidige:
            return False
        huidige = huidige[naam]
        if index != "":
            i = int(index)
            if not isinstance(huidige, list) or i >= len(huidige):
                return False
            huidige = huidige[i]
    if not isinstance(huidige, dict):
        return False
    huidige[sleutel] = waarde
    return True


def mark_field_stale(record: dict, veldpad: str, reden: str) -> bool:
    """Markeer één veld van een concept-record als stale in-place.

    Navigeert naar `record[veldpad]["_provenance"]` en zet:
      - `stale = True`
      - `stale_reason = reden`
      - `stale_at = <ISO-tijdstip>`

    Returnt True als het veld gevonden en bijgewerkt werd; False als het pad
    niet bestond of geen `_provenance`-sub-object had.

    De aanroeper is verantwoordelijk voor het terugschrijven van `record` naar
    schijf (zodat write-beslissing bij mark_stale.py blijft).
    """
    # Navigeer naar het veld
    _SEGMENT_RE = re.compile(r"([^\[.]+)(?:\[(\d+)\])?")
    segmenten = _SEGMENT_RE.findall(veldpad)
    huidige = record
    for naam, index in segmenten:
        if naam not in huidige:
            return False
        huidige = huidige[naam]
        if index != "":
            i = int(index)
            if not isinstance(huidige, list) or i >= len(huidige):
                return False
            huidige = huidige[i]
    if not isinstance(huidige, dict):
        return False
    prov = huidige.get("_provenance")
    if not isinstance(prov, dict):
        return False
    prov["stale"] = True
    prov["stale_reason"] = reden
    prov["stale_at"] = now_iso()
    return True


def sha_voor_chunk(chunk_id: str, chroma_collectie) -> Optional[str]:
    """Haal de huidige `chunk_sha` op uit ChromaDB-metadata voor een gegeven chunk-id.

    Parameters
    ----------
    chunk_id:
        De stabiele chunk-id (bv. "Antiwitwaswet-2017__art_5").
    chroma_collectie:
        Een reeds geopend ChromaDB-collection-object (de aanroeper beheert de
        verbinding zodat dit een pure query-functie blijft zonder ChromaDB-import
        op module-niveau).

    Returnt de `chunk_sha`-string als die aanwezig is in de metadata, anders None.
    Geeft ook None terug als de chunk helemaal niet bestaat in de collectie.
    """
    try:
        resultaat = chroma_collectie.get(ids=[chunk_id], include=["metadatas"])
        ids = resultaat.get("ids", [])
        metas = resultaat.get("metadatas", [])
        if not ids or not metas:
            return None
        return metas[0].get("chunk_sha")
    except Exception:
        return None
