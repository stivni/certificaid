#!/usr/bin/env python3
"""
Apply wetteksten-staging naar resources/ met diff-based trust-reset.

Variant van apply_adviezen_staging voor wetteksten. Voert pdftotext-cleanup
opnieuw door op de oude body en vergelijkt met de nieuwe extractie.

Strikter dan adviezen omdat:
  - wetteksten gebruiken DEFAULT_STEPS (remove_page_artifacts, remove_toc, etc.)
  - kleine diffs in body zijn typisch artefact-cleanup
  - grote diffs (>5%) = structurele extractor-verandering, reset trust
"""
from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path
from datetime import datetime, timezone

import frontmatter

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.lib.cleanup import (  # noqa: E402
    remove_page_artifacts,
    collapse_blank_lines,
)

STAGING_DIR = ROOT / "data" / "etl-staging"
WETTEKST_DIR = ROOT / "resources" / "bronnen" / "wetteksten"

CONTENT_DIFF_THRESHOLD = 0.05  # 5%


def normalize_old_body(body: str) -> str:
    """Pas dezelfde cleanup-pipeline toe als de extractor zou doen."""
    md = remove_page_artifacts(body)
    md = collapse_blank_lines(md)
    return md.strip()


def diff_ratio(old: str, new: str) -> float:
    o, n = old.split("\n"), new.split("\n")
    m = difflib.SequenceMatcher(None, o, n, autojunk=False)
    ch = 0
    for tag, i1, i2, j1, j2 in m.get_opcodes():
        if tag == "replace":
            ch += max(i2 - i1, j2 - j1)
        elif tag in ("delete", "insert"):
            ch += (i2 - i1) + (j2 - j1)
    return ch / max(len(o), 1)


def update_wettekst(staging_path: Path, resource_path: Path, *, dry_run: bool = False) -> dict:
    staging_post = frontmatter.load(str(staging_path))
    resource_post = frontmatter.load(str(resource_path))

    old_body = resource_post.content
    new_body = staging_post.content
    if not new_body.strip():
        return {"status": "skip-empty", "file": resource_path.name}

    norm_old = normalize_old_body(old_body)
    new_stripped = new_body.strip()

    if norm_old == new_stripped:
        diff_type = "identical"
        ratio = 0.0
    else:
        ratio = diff_ratio(norm_old, new_stripped)
        diff_type = "artefact" if ratio < CONTENT_DIFF_THRESHOLD else "content"

    new_fm = dict(resource_post.metadata)
    prov = new_fm.setdefault("provenance", {})
    prov["generated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    staging_prov = staging_post.metadata.get("provenance") or {}
    if staging_prov.get("tooling"):
        prov_tooling = prov.setdefault("tooling", {})
        prov_tooling["pipeline"] = staging_prov["tooling"].get("pipeline", prov_tooling.get("pipeline"))
        prov_tooling["pipeline_version"] = staging_prov["tooling"].get("pipeline_version", "")

    reset = False
    trust = prov.get("trust") or {}
    confirmed_by = trust.get("confirmed_by")
    if diff_type == "content" and confirmed_by != "human":
        layer2 = trust.setdefault("layer2", {})
        layer2["status"] = "not_run"
        layer2["agent"] = None
        layer2["run_at"] = None
        layer2["rationale"] = None
        layer2["concrete_problemen"] = []
        trust["status"] = "unreviewed"
        trust["confirmed_by"] = None
        trust["confirmed_at"] = None
        trust["rationale"] = "Trust gereset 2026-05-11: ETL-fix wetteksten met content-diff > 5%"
        reset = True

    if dry_run:
        return {"status": "dry-run", "file": resource_path.name, "diff_type": diff_type, "ratio": ratio, "reset": reset}

    new_post = frontmatter.Post(content=new_body, **new_fm)
    resource_path.write_text(frontmatter.dumps(new_post) + "\n", encoding="utf-8")
    return {"status": "applied", "file": resource_path.name, "diff_type": diff_type, "ratio": round(ratio, 4), "reset": reset}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--pattern", default="WBTW-KB*",
                   help="glob in data/etl-staging/ (default WBTW-KB*)")
    args = p.parse_args()

    staging_files = sorted(STAGING_DIR.glob(args.pattern + ".md"))
    if not staging_files:
        print(f"Geen staging files matching '{args.pattern}.md'")
        return

    counters = {"identical": 0, "artefact": 0, "content": 0, "skip-empty": 0, "missing": 0}
    reset_count = 0
    reports = []
    for sp in staging_files:
        rp = WETTEKST_DIR / sp.name
        if not rp.exists():
            counters["missing"] += 1
            continue
        try:
            r = update_wettekst(sp, rp, dry_run=args.dry_run)
        except Exception as e:
            print(f"  ⚠️  {sp.name}: {type(e).__name__}: {e}")
            continue
        reports.append(r)
        counters[r.get("diff_type", r["status"])] = counters.get(r.get("diff_type", r["status"]), 0) + 1
        if r.get("reset"):
            reset_count += 1

    print()
    print(f"=== Apply wetteksten-staging {'(dry-run)' if args.dry_run else ''} (pattern={args.pattern}*) ===")
    print(f"Verwerkt:    {len(reports)}")
    for k in ("identical", "artefact", "content"):
        print(f"  {k:10s}: {counters[k]}")
    print(f"  reset:       {reset_count}")
    content = [r for r in reports if r.get("diff_type") == "content"]
    if content:
        print()
        print("Content-diffs (top 10):")
        for r in sorted(content, key=lambda x: -x["ratio"])[:10]:
            print(f"  {r['ratio']:.3f}  {r['file']}")


if __name__ == "__main__":
    main()
