"""Provenance helpers for Certificaid artefacts.

Schema and rationale: docs/adr/ADR-004-provenance.md.
Workflow that consumes this (stale-cascade, regressie-gates): docs/adr/ADR-003-reprocessing-evaluatie.md.

YAML writes use ruamel.yaml round-trip mode so existing frontmatter formatting
(key order, quote style, list flow vs. block) is preserved.
"""
from __future__ import annotations

import hashlib
import io
import re
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from ruamel.yaml import YAML

PROVENANCE_KEY = "provenance"

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


@dataclass
class Provenance:
    inputs: list[Input]
    tooling: Tooling
    generated_at: str
    stale: bool = False
    stale_reason: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "inputs": [asdict(i) for i in self.inputs],
            "tooling": asdict(self.tooling),
            "generated_at": self.generated_at,
            "stale": self.stale,
            "stale_reason": self.stale_reason,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Provenance":
        return cls(
            inputs=[Input(**i) for i in data["inputs"]],
            tooling=Tooling(**data["tooling"]),
            generated_at=data["generated_at"],
            stale=data.get("stale", False),
            stale_reason=data.get("stale_reason"),
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


def read_provenance(md_path: Path) -> Optional[Provenance]:
    """Read provenance block from markdown YAML frontmatter, or None if absent."""
    text = md_path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None
    data = _yaml().load(m.group(1)) or {}
    block = data.get(PROVENANCE_KEY)
    if block is None:
        return None
    # ruamel returns CommentedMap/Seq; convert to plain for dataclass construction
    return Provenance.from_dict(_to_plain(block))


def write_provenance(md_path: Path, prov: Provenance) -> None:
    """Add or replace the provenance block, preserving existing YAML formatting."""
    text = md_path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    yaml = _yaml()
    if m:
        data = yaml.load(m.group(1)) or {}
        body = text[m.end():]
    else:
        data = {}
        body = text
    data[PROVENANCE_KEY] = prov.to_dict()
    buf = io.StringIO()
    yaml.dump(data, buf)
    md_path.write_text(f"---\n{buf.getvalue()}---\n{body}", encoding="utf-8")


def _to_plain(obj):
    """Recursively convert ruamel.yaml CommentedMap/Seq to plain dict/list."""
    if hasattr(obj, "items"):
        return {k: _to_plain(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_to_plain(v) for v in obj]
    return obj


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
