#!/usr/bin/env python3
"""
Apply ISA-specifieke ETL-transformers in-place op alle ISA-bronnen.

Pipeline per ISA-MD:

  1. Lees frontmatter + body via `python-frontmatter`.
  2. Pas `strip_isa_page_footers` toe (verwijder NBA-IBR page-footer-blokken).
  3. Pas `inject_headings_isa` toe (promoot sectielabels naar `##`-headings).
  4. Update `provenance`:
       - bump `generated_at` naar nu-ISO-Z.
       - voeg `apply_isa_transformers.py` toe aan tooling-pipeline-naam.
       - reset trust naar `unreviewed` met expliciete rationale.
  5. Schrijf het bestand terug.

Rationale: pure-tekst body-rewrite, NIET via `convert.py` om de
pipeline-version-cascade van wetteksten te vermijden (ADR-005 §4-contract
geldt direct op de body).

Gebruik:
  python3 -m tools.etl.apply_isa_transformers           # alle ISA-*.md
  python3 -m tools.etl.apply_isa_transformers --dry-run # preview, geen writes
  python3 -m tools.etl.apply_isa_transformers --file ISA-200.md
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl.transformers.strip_isa_page_footers import (  # noqa: E402
    strip_isa_page_footers,
)
from tools.etl.transformers.inject_headings_isa import (  # noqa: E402
    inject_headings_isa,
)

NORMEN_DIR = ROOT / "resources" / "bronnen" / "normen"

PIPELINE_NAME = "tools/etl/apply_isa_transformers.py"
PIPELINE_VERSION = "1.0"

NEW_RATIONALE = (
    "ETL-fix 2026-05-17: strip_isa_page_footers + inject_headings_isa "
    "transformers toegepast (in-place). NBA-IBR page-footer-blokken zijn "
    "verwijderd en ISA-sectielabels (Inleiding/Doelstelling(en)/Definities/"
    "Vereisten/Toepassingsgerichte teksten/Ingangsdatum/Bijlage) zijn naar "
    "`##`-headings gepromoot. Heroverweging trust-status volgt na QA-pass."
)


def _now_iso_z() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _ensure_dict(value, default):
    return value if isinstance(value, dict) else default


def _bump_provenance(meta: dict) -> dict:
    """Update provenance-blok zodat trust → unreviewed + nieuwe rationale +
    tooling/pipeline weerspiegelt onze in-place rewrite.

    Conform ADR-005 §2 schema: provenance.trust + provenance.tooling +
    provenance.generated_at.
    """
    prov = _ensure_dict(meta.get("provenance"), {})
    prov["generated_at"] = _now_iso_z()
    tooling = _ensure_dict(prov.get("tooling"), {})
    # Pipeline-string: behoud originele + append-onze-stap, gescheiden door ` + `
    orig_pipeline = tooling.get("pipeline") or ""
    if PIPELINE_NAME not in orig_pipeline:
        if orig_pipeline:
            tooling["pipeline"] = f"{orig_pipeline} + {PIPELINE_NAME}"
        else:
            tooling["pipeline"] = PIPELINE_NAME
    tooling["pipeline_version"] = PIPELINE_VERSION
    tooling.setdefault("model", None)
    tooling.setdefault("prompt_version", None)
    prov["tooling"] = tooling
    # Trust reset
    trust = _ensure_dict(prov.get("trust"), {})
    trust["status"] = "unreviewed"
    trust["confirmed_at"] = None
    trust["confirmed_by"] = None
    trust["rationale"] = NEW_RATIONALE
    trust.setdefault("layer1", None)
    trust.setdefault("layer2", None)
    prov["trust"] = trust
    prov.setdefault("stale", False)
    prov.setdefault("stale_reason", None)
    prov.setdefault("inputs", [])
    meta["provenance"] = prov
    return meta


def process_file(path: Path, dry_run: bool = False) -> dict:
    """Voer transformers toe op één ISA-bestand en schrijf het terug."""
    post = frontmatter.load(str(path))
    orig_body = post.content
    new_body, _ = strip_isa_page_footers(orig_body, {})
    new_body, _ = inject_headings_isa(new_body, {})

    h2_before = orig_body.count("\n## ") + (1 if orig_body.startswith("## ") else 0)
    h2_after = new_body.count("\n## ") + (1 if new_body.startswith("## ") else 0)
    lines_before = len(orig_body.splitlines())
    lines_after = len(new_body.splitlines())

    changed = new_body != orig_body
    if changed:
        post.content = new_body
        post.metadata = _bump_provenance(dict(post.metadata))

    if not dry_run and changed:
        # Schrijf via frontmatter.dump met expliciete fs-write
        with path.open("wb") as f:
            frontmatter.dump(post, f)

    return {
        "file": path.name,
        "changed": changed,
        "h2_before": h2_before,
        "h2_after": h2_after,
        "lines_before": lines_before,
        "lines_after": lines_after,
    }


def find_isa_files() -> list[Path]:
    return sorted(NORMEN_DIR.glob("ISA-*.md"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--file", help="Alleen één bestand (basename, bv. ISA-200.md)")
    args = ap.parse_args()

    if args.file:
        target = NORMEN_DIR / args.file
        if not target.is_file():
            sys.exit(f"Niet gevonden: {target}")
        files = [target]
    else:
        files = find_isa_files()

    if not files:
        sys.exit("Geen ISA-bestanden gevonden in resources/bronnen/normen/")

    print(f"Verwerken: {len(files)} ISA-bestand(en){' (dry-run)' if args.dry_run else ''}\n")
    results = []
    for p in files:
        r = process_file(p, dry_run=args.dry_run)
        results.append(r)
        delta_h2 = r["h2_after"] - r["h2_before"]
        delta_lines = r["lines_after"] - r["lines_before"]
        status = "CHG" if r["changed"] else "—  "
        print(
            f"  {status} {r['file']:35s} "
            f"h2: {r['h2_before']:3d} → {r['h2_after']:3d} ({delta_h2:+d})  "
            f"lines: {r['lines_before']:4d} → {r['lines_after']:4d} ({delta_lines:+d})"
        )

    n_changed = sum(1 for r in results if r["changed"])
    print(f"\n{n_changed}/{len(files)} bestanden gewijzigd.")
    return results


if __name__ == "__main__":
    main()
