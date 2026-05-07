"""One-off migration: add a provenance block to bron-MD's based on source_config.yaml.

ETL tooling (Fase 1, ADR-005) will later write provenance natively; this script
backfills the existing corpus.

Usage:
  python tools/etl/add_provenance.py --source AWW
  python tools/etl/add_provenance.py            # all sources
  python tools/etl/add_provenance.py --force    # overwrite existing provenance
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.lib.provenance import (  # noqa: E402
    Input,
    make_input,
    make_provenance,
    read_provenance,
    write_provenance,
)

CONFIG = ROOT / "resources" / "source_config.yaml"


def add_for_source(name: str, sources: dict, *, force: bool = False) -> tuple[str, str]:
    """Returns (status, detail)."""
    if name not in sources:
        return "unknown-source", ""
    entry = sources[name] or {}
    output_rel = entry.get("output")
    raw_rel = entry.get("raw")
    if not output_rel:
        return "no-output", ""
    output_path = ROOT / output_rel
    if not output_path.exists():
        return "output-missing", str(output_path)

    if not force and read_provenance(output_path) is not None:
        return "already-has-provenance", ""

    inputs: list[Input] = []
    if raw_rel:
        raw_path = ROOT / raw_rel
        if not raw_path.exists():
            return "raw-missing", str(raw_path)
        version = entry.get("bijgewerkt")
        inputs.append(make_input(raw_path, version=version, repo_root=ROOT))
    elif entry.get("type") == "split" and entry.get("derived_from"):
        parent_name = entry["derived_from"]
        parent_entry = sources.get(parent_name) or {}
        parent_output = parent_entry.get("output")
        if not parent_output:
            return "derived-no-parent-output", parent_name
        parent_path = ROOT / parent_output
        if not parent_path.exists():
            return "derived-parent-missing", str(parent_path)
        version = entry.get("bijgewerkt")
        inputs.append(make_input(parent_path, version=version, repo_root=ROOT))

    if not inputs:
        return "no-inputs", "neither raw nor derived; skip"

    pipeline_path = "tools/etl/convert.py"
    prov = make_provenance(inputs=inputs, pipeline=pipeline_path, repo_root=ROOT)
    write_provenance(output_path, prov)
    return "added", str(output_path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", help="One source name; if omitted, process all")
    ap.add_argument("--force", action="store_true", help="Overwrite existing provenance")
    args = ap.parse_args()

    cfg = yaml.safe_load(CONFIG.read_text())
    sources = cfg.get("sources", {}) or {}
    names = [args.source] if args.source else list(sources.keys())

    counts: dict[str, int] = {}
    for n in names:
        status, detail = add_for_source(n, sources, force=args.force)
        counts[status] = counts.get(status, 0) + 1
        if status in {"added", "raw-missing", "output-missing", "unknown-source", "no-inputs"}:
            print(f"  {status:25s}  {n}  {detail}")

    print(f"\n{len(names)} sources scanned:")
    for status, n in sorted(counts.items()):
        print(f"  {status:25s}  {n}")


if __name__ == "__main__":
    main()
