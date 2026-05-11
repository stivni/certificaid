#!/usr/bin/env python3
"""
Apply CBN-adviezen-staging naar resources/ met diff-based trust-reset.

Voor elke advies in data/etl-staging/CBN-*.md:
  1. Laad oude versie uit resources/bronnen/adviezen/<naam>.md
  2. Laad nieuwe versie uit staging
  3. Pas dezelfde post-processing toe op de OUDE body
  4. Compare normalized-oud met nieuw:
     - identiek of klein-diff (<5% lines) → "artefact-only", behoud trust
     - groot diff → "content-changed", reset trust.layer2 naar not_run
  5. Schrijf nieuwe body naar resource, behoud frontmatter (trust-block)
     uitgezonderd:
     - provenance.generated_at en provenance.tooling.pipeline_version: update
     - bij content-changed: trust.layer2 → not_run, trust.status → unreviewed
       (tenzij confirmed_by == "human", die override blijft)
"""
from __future__ import annotations

import difflib
import shutil
import sys
from pathlib import Path
from datetime import datetime, timezone

import frontmatter

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.lib.cbn_advies_html import (  # noqa: E402
    _strip_body_noise,
    _strip_toc_block,
    _promote_implicit_headings,
    _cleanup_markdown,
)

STAGING_DIR = ROOT / "data" / "etl-staging"
ADVIES_DIR = ROOT / "resources" / "bronnen" / "adviezen"

# Threshold: % of body lines that changed → "content-diff" trust-reset
CONTENT_DIFF_THRESHOLD = 0.05  # 5%


def normalize_old_body(body: str) -> str:
    """Pas dezelfde post-processing toe als de scraper-pipeline doet,
    zodat een 'artefact-only'-vergelijking robuust is."""
    md = _strip_body_noise(body)
    md = _strip_toc_block(md)
    md = _promote_implicit_headings(md)
    md = _cleanup_markdown(md)
    return md


def diff_ratio(old: str, new: str) -> tuple[float, int, int]:
    """Geef (ratio, lines_changed, total_lines).

    ratio = (lines_added + lines_removed) / total_lines_in_old.
    """
    old_lines = old.split("\n")
    new_lines = new.split("\n")
    matcher = difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False)
    changed = 0
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "replace":
            changed += max(i2 - i1, j2 - j1)
        elif tag in ("delete", "insert"):
            changed += (i2 - i1) + (j2 - j1)
    total = max(len(old_lines), 1)
    return changed / total, changed, total


def update_advies(staging_path: Path, advies_path: Path, *, dry_run: bool = False) -> dict:
    """Pas één advies-update toe. Returnt rapport-dict."""
    staging_post = frontmatter.load(str(staging_path))
    advies_post = frontmatter.load(str(advies_path))

    old_body = advies_post.content
    new_body = staging_post.content

    if not new_body.strip():
        return {"status": "skip-empty", "file": advies_path.name}

    # Normalize old for comparison
    normalized_old = normalize_old_body(old_body).strip()
    new_stripped = new_body.strip()

    if normalized_old == new_stripped:
        diff_type = "identical"
        ratio = 0.0
    else:
        # Check of de enige toevoeging een leading H1 + blank is — voorheen
        # voegde `extract_advice` H1 niet altijd toe; nieuwe scraper-versie doet
        # het wel consistent. Behandel dat als artefact-only.
        new_lines = new_stripped.split("\n")
        if (len(new_lines) >= 2
                and new_lines[0].startswith("# ")
                and new_lines[1].strip() == ""):
            rest = "\n".join(new_lines[2:]).strip()
            if rest == normalized_old:
                diff_type = "artefact"
                ratio = 0.0
            else:
                ratio, _, _ = diff_ratio(rest, normalized_old)
                diff_type = "artefact" if ratio < CONTENT_DIFF_THRESHOLD else "content"
        else:
            ratio, _, _ = diff_ratio(normalized_old, new_stripped)
            diff_type = "artefact" if ratio < CONTENT_DIFF_THRESHOLD else "content"

    # Build new resource: keep frontmatter, update body
    new_fm = dict(advies_post.metadata)

    # Update provenance.generated_at + pipeline_version
    prov = new_fm.setdefault("provenance", {})
    prov["generated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    staging_prov = staging_post.metadata.get("provenance") or {}
    if staging_prov.get("tooling"):
        prov_tooling = prov.setdefault("tooling", {})
        prov_tooling["pipeline"] = staging_prov["tooling"].get("pipeline", prov_tooling.get("pipeline"))
        prov_tooling["pipeline_version"] = staging_prov["tooling"].get("pipeline_version", "")

    # Optionally reset trust on content-diff
    reset = False
    trust = prov.get("trust") or {}
    confirmed_by = trust.get("confirmed_by")
    if diff_type == "content" and confirmed_by != "human":
        # Reset layer2
        layer2 = trust.setdefault("layer2", {})
        layer2["status"] = "not_run"
        layer2["agent"] = None
        layer2["run_at"] = None
        layer2["rationale"] = None
        layer2["concrete_problemen"] = []
        # Reset top-level (afgeleide regel)
        trust["status"] = "unreviewed"
        trust["confirmed_by"] = None
        trust["confirmed_at"] = None
        trust["rationale"] = "Trust gereset 2026-05-11: re-scrape met scraper-fixes, content-diff > 5%"
        reset = True

    if dry_run:
        return {
            "status": "dry-run",
            "file": advies_path.name,
            "diff_type": diff_type,
            "ratio": ratio,
            "reset": reset,
        }

    # Write new file
    new_post = frontmatter.Post(content=new_body, **new_fm)
    advies_path.write_text(frontmatter.dumps(new_post) + "\n", encoding="utf-8")

    return {
        "status": "applied",
        "file": advies_path.name,
        "diff_type": diff_type,
        "ratio": round(ratio, 4),
        "reset": reset,
    }


def main():
    import argparse
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--limit", type=int, default=None)
    args = p.parse_args()

    staging_files = sorted(STAGING_DIR.glob("CBN-*.md"))
    if args.limit:
        staging_files = staging_files[:args.limit]

    counters = {"identical": 0, "artefact": 0, "content": 0, "skip-empty": 0, "missing": 0}
    reset_count = 0
    reports = []

    for staging_path in staging_files:
        advies_path = ADVIES_DIR / staging_path.name
        if not advies_path.exists():
            counters["missing"] += 1
            continue
        try:
            r = update_advies(staging_path, advies_path, dry_run=args.dry_run)
        except Exception as e:  # noqa: BLE001
            print(f"  ⚠️  {staging_path.name}: {type(e).__name__}: {e}")
            continue
        reports.append(r)
        dt = r.get("diff_type", r["status"])
        counters[dt] = counters.get(dt, 0) + 1
        if r.get("reset"):
            reset_count += 1

    print()
    print(f"=== Apply adviezen-staging {'(dry-run)' if args.dry_run else ''} ===")
    print(f"Totaal verwerkt: {len(reports)}")
    print(f"  identical:    {counters['identical']}")
    print(f"  artefact:     {counters['artefact']}  (klein-diff, trust behouden)")
    print(f"  content:      {counters['content']}  (groot-diff)")
    print(f"  reset count:  {reset_count}  (trust naar unreviewed)")
    if counters["skip-empty"]:
        print(f"  skip-empty:   {counters['skip-empty']}")
    if counters["missing"]:
        print(f"  missing:      {counters['missing']}")

    # Voorbeelden van content-diff voor inspectie
    content_diffs = [r for r in reports if r.get("diff_type") == "content"]
    if content_diffs:
        print()
        print(f"Eerste 10 content-diff adviezen (ratio):")
        for r in sorted(content_diffs, key=lambda x: -x["ratio"])[:10]:
            print(f"  {r['ratio']:>6.3f}  {r['file']}")


if __name__ == "__main__":
    main()
