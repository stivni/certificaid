"""Provenance helpers for Certificaid artefacts.

Schema and rationale: docs/adr/ADR-004-provenance.md.
Workflow that consumes this (stale-cascade, regressie-gates): docs/adr/ADR-003-reprocessing-evaluatie.md.
"""
from __future__ import annotations

import hashlib
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import frontmatter

PROVENANCE_KEY = "provenance"


@dataclass
class Input:
    id: str
    sha256: str
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
    rel = path.relative_to(repo_root) if repo_root else path
    return Input(id=str(rel), sha256=hash_file(path), version=version)


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
    post = frontmatter.load(str(md_path))
    block = post.metadata.get(PROVENANCE_KEY)
    if block is None:
        return None
    return Provenance.from_dict(block)


def write_provenance(md_path: Path, prov: Provenance) -> None:
    """Write or overwrite the provenance block in a markdown file's frontmatter."""
    post = frontmatter.load(str(md_path))
    post.metadata[PROVENANCE_KEY] = prov.to_dict()
    with open(md_path, "wb") as f:
        frontmatter.dump(post, f)


def detect_stale(recorded: Provenance, current_inputs: list[Input]) -> tuple[bool, Optional[str]]:
    """Compare recorded inputs against currently-resolved inputs. Returns (is_stale, reason)."""
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
        if rec[k] != cur_hash:
            return True, f"input changed: {k}"
    return False, None
