"""One-off migration: add a provenance block to bron-MD's based on source_config.yaml.

ETL tooling (Fase 1, ADR-005) will later write provenance natively; this script
backfills the existing corpus for both `sources:` (per-bron) and `collections:`
(bulk: CBN-adviezen, ITAA-normen) sections.

Usage:
  python tools/etl/add_provenance.py                      # everything
  python tools/etl/add_provenance.py --source AWW         # one source
  python tools/etl/add_provenance.py --collection cbn-adviezen
  python tools/etl/add_provenance.py --force              # overwrite existing
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import frontmatter
import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.lib.provenance import (  # noqa: E402
    Input,
    make_input,
    make_provenance,
    make_url_input,
    read_provenance,
    write_provenance,
)

CONFIG = ROOT / "resources" / "source_config.yaml"
INDEX_FILES = {"INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"}


# ─── sources/ (per-bron) ──────────────────────────────────────────────────────

def add_for_source(name: str, sources: dict, *, force: bool = False) -> tuple[str, str]:
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
        # Process parent first so its hash is stable before we record it as input.
        # Otherwise the child would record the pre-provenance parent-hash and flip
        # stale as soon as the parent gets its own provenance block written.
        if read_provenance(parent_path) is None:
            add_for_source(parent_name, sources, force=False)
        version = entry.get("bijgewerkt")
        inputs.append(make_input(parent_path, version=version, repo_root=ROOT))

    if not inputs:
        return "no-inputs", "neither raw nor derived; skip"

    pipeline_path = "tools/etl/convert.py"
    prov = make_provenance(inputs=inputs, pipeline=pipeline_path, repo_root=ROOT)
    write_provenance(output_path, prov)
    return "added", str(output_path)


# ─── collections/ (bulk) ──────────────────────────────────────────────────────

def _resolve_item_inputs(post: frontmatter.Post, item_specs: list[dict]) -> tuple[list[Input], str]:
    """For one .md, walk through item_inputs spec and collect resolved inputs.

    Returns (inputs, missing_detail). missing_detail is non-empty when a 'local'
    field references a file that does not exist on disk (warning, not blocker).
    """
    inputs: list[Input] = []
    missing = []
    for spec in item_specs or []:
        field = spec.get("field")
        kind = spec.get("kind")
        if not field or not kind:
            continue
        val = post.metadata.get(field)
        if not val:
            continue
        if kind == "local":
            path = ROOT / str(val)
            if path.exists():
                inputs.append(make_input(path, repo_root=ROOT))
            else:
                missing.append(f"{field}={val}")
        elif kind == "url":
            inputs.append(make_url_input(str(val)))
    return inputs, "; ".join(missing)


def add_for_collection_item(md_path: Path, cfg: dict, *, force: bool = False) -> tuple[str, str]:
    if md_path.name in INDEX_FILES:
        return "skipped-index", ""
    if not force and read_provenance(md_path) is not None:
        return "already-has-provenance", ""
    post = frontmatter.load(str(md_path))
    inputs, missing = _resolve_item_inputs(post, cfg.get("item_inputs", []))
    if not inputs:
        return "no-inputs", missing or "no resolvable item_inputs fields"
    pipeline = cfg.get("pipeline") or "tools/etl/convert.py"
    prov = make_provenance(inputs=inputs, pipeline=pipeline, repo_root=ROOT)
    write_provenance(md_path, prov)
    return "added", str(md_path)


def add_for_collection(name: str, collections: dict, *, force: bool = False) -> dict[str, int]:
    cfg = collections.get(name)
    if not cfg:
        print(f"  unknown-collection            {name}")
        return {"unknown-collection": 1}
    out_dir = ROOT / cfg.get("output_dir", "")
    if not out_dir.is_dir():
        print(f"  output-dir-missing            {name} ({out_dir})")
        return {"output-dir-missing": 1}

    counts: dict[str, int] = {}
    interesting = {"added", "no-inputs"}
    for md_path in sorted(out_dir.glob("*.md")):
        status, detail = add_for_collection_item(md_path, cfg, force=force)
        counts[status] = counts.get(status, 0) + 1
        if status in interesting:
            print(f"  {status:22s}  {md_path.name}  {detail}")
    return counts


# ─── main ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", help="One source name (sources/)")
    ap.add_argument("--collection", help="One collection name (collections/)")
    ap.add_argument("--force", action="store_true", help="Overwrite existing provenance")
    args = ap.parse_args()

    cfg = yaml.safe_load(CONFIG.read_text())
    sources = cfg.get("sources") or {}
    collections = cfg.get("collections") or {}

    do_sources = args.source or (not args.collection)
    do_collections = args.collection or (not args.source)

    grand_counts: dict[str, int] = {}

    if do_sources:
        names = [args.source] if args.source else list(sources.keys())
        # Process non-split sources first so parent hashes are stable when
        # split children record them as inputs.
        names = sorted(names, key=lambda n: (sources.get(n) or {}).get("type") == "split")
        print(f"=== sources ({len(names)}) ===")
        for n in names:
            status, detail = add_for_source(n, sources, force=args.force)
            grand_counts[f"src/{status}"] = grand_counts.get(f"src/{status}", 0) + 1
            if status in {"added", "raw-missing", "output-missing", "unknown-source",
                          "no-inputs", "derived-parent-missing"}:
                print(f"  {status:25s}  {n}  {detail}")

    if do_collections:
        names = [args.collection] if args.collection else list(collections.keys())
        for n in names:
            print(f"\n=== collection: {n} ===")
            counts = add_for_collection(n, collections, force=args.force)
            for status, c in counts.items():
                grand_counts[f"col/{n}/{status}"] = grand_counts.get(f"col/{n}/{status}", 0) + c

    print("\n=== summary ===")
    for k, v in sorted(grand_counts.items()):
        print(f"  {k:50s}  {v}")


if __name__ == "__main__":
    main()
