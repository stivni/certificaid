#!/usr/bin/env python3
"""Backfill QA-data uit losse `data/qa/*.json` naar `provenance.trust` frontmatter.

Achtergrond
-----------
Tot mei 2026 leefden de drie QA-lagen in losse bestanden:

  * `data/qa/qa-<rid>.json`            — Laag 1 (qa_bron.py deterministisch)
  * `data/qa/<rid>-diff-verdicts.json` — Laag 1.5 (diff_review.py)
  * `data/qa/<rid>-content-verdicts.json` — Laag 2 (subagent content-judgment)

Dat genereert kerkhof-paden van JSON's en maakt aggregatie lastig. Per ADR-005
§5 wonen deze data nu inline in `provenance.trust.layer1 / layer1_5_diff /
layer2_content` per bron-MD. Aggregaten ontstaan via `grep`-style queries.

Dit script is een eenmalige backfill:

  1. Lees alle `data/qa/qa-*.json`. Per bron: bewaar de meest recente entry
     (op basis van bestandsnaam-tijdstempel: `qa-YYYYMMDD-HHMMSS.json`).
  2. Lees alle `data/qa/*-diff-verdicts.json` — zelfde "laatste wint"-logica.
  3. Lees alle `data/qa/*-content-verdicts.json` — idem.
  4. Voor elke bron in `resources/bronnen/` schrijf de drie sub-blokken naar
     frontmatter. Onbestaande blokken blijven null.

Idempotent: tweede run met dezelfde JSON's overschrijft met dezelfde waarden.

Gebruik
-------
::

    python3 tools/etl/qa_to_frontmatter.py --dry-run    # toon wat zou veranderen
    python3 tools/etl/qa_to_frontmatter.py              # schrijf

Na succesvolle backfill kan `data/qa/*.json` verplaatst worden naar
`data/qa/archive/` (handmatig of via `--archive-after`).
"""
from __future__ import annotations

import argparse
import io
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from glob import glob
from pathlib import Path
from typing import Optional

import ruamel.yaml

ROOT = Path(__file__).resolve().parent.parent.parent
QA_DIR = ROOT / "data" / "qa"
RESOURCES_DIR = ROOT / "resources" / "bronnen"
STAGING_DIR = ROOT / "data" / "etl-staging"

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
_QA_TIMESTAMP_RE = re.compile(r"qa-(\d{8})-(\d{6})\.json$")


def _yaml_rt() -> ruamel.yaml.YAML:
    y = ruamel.yaml.YAML()
    y.preserve_quotes = True
    y.indent(mapping=2, sequence=4, offset=2)
    y.width = 4096
    return y


def _read_frontmatter(path: Path) -> tuple[Optional[dict], str]:
    text = path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    data = _yaml_rt().load(m.group(1)) or {}
    body = text[m.end():]
    return data, body


def _write_frontmatter(path: Path, data: dict, body: str) -> None:
    buf = io.StringIO()
    _yaml_rt().dump(data, buf)
    path.write_text(f"---\n{buf.getvalue()}---\n{body}", encoding="utf-8")


# ─── Layer 1 collation ───────────────────────────────────────────────────────

def _qa_file_timestamp(p: Path) -> Optional[str]:
    """Extract `YYYYMMDDHHMMSS` uit qa-bestandsnaam, of None."""
    m = _QA_TIMESTAMP_RE.search(p.name)
    if not m:
        return None
    return m.group(1) + m.group(2)


def _layer1_compact(entry: dict, run_id: str) -> dict:
    """Maak compact layer1-dict van qa_bron.py BronReport-entry."""
    flags = []
    for c in entry.get("checks", []):
        st = c.get("status")
        if st in ("warn", "fail"):
            flags.append({"name": c["name"], "status": st,
                          "detail": c.get("detail"),
                          "samples": c.get("samples", []) or []})
    return {
        "verdict": entry.get("verdict"),
        "heading_count": entry.get("heading_count"),
        "max_section_chars": entry.get("max_section_chars"),
        "file_size_chars": entry.get("file_size_chars"),
        "flags": flags,
        "run_id": run_id,
    }


def collect_layer1(qa_dir: Path) -> dict[str, dict]:
    """Doorzoek qa-*.json en geef per bron de meest recente layer1-dict.

    Sleutelt op bestandsnaam (basename); zelfde bron in resources én staging
    worden gemapt op dezelfde key.
    """
    files = sorted(qa_dir.glob("qa-*.json"))
    files = [f for f in files if _QA_TIMESTAMP_RE.search(f.name)]
    files.sort(key=lambda p: _qa_file_timestamp(p) or "")

    out: dict[str, dict] = {}
    for f in files:
        ts = _qa_file_timestamp(f)
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  ! kan {f.name} niet lezen: {e}", file=sys.stderr)
            continue
        run_id = data.get("run_id") or (ts or f.stem)
        for entry in data.get("bronnen", []):
            bestand = entry.get("bestand", "")
            if not bestand:
                continue
            key = Path(bestand).name
            out[key] = _layer1_compact(entry, run_id)
    return out


# ─── Layer 1.5 collation ─────────────────────────────────────────────────────

def _diff_compact(entry: dict, run_id: str) -> dict:
    return {
        "verdict": entry.get("diff_verdict") or entry.get("verdict"),
        "rationale": entry.get("rationale"),
        "kritieke_observaties": entry.get("kritieke_observaties") or [],
        "auto": bool(entry.get("auto", False)),
        "run_id": run_id,
    }


def collect_diff_verdicts(qa_dir: Path) -> dict[str, dict]:
    files = sorted(qa_dir.glob("*-diff-verdicts.json"))
    out: dict[str, dict] = {}
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  ! kan {f.name} niet lezen: {e}", file=sys.stderr)
            continue
        run_id = data.get("run_id") or f.stem.replace("-diff-verdicts", "")
        verdicts = data.get("verdicts", []) if isinstance(data, dict) else data
        for entry in verdicts:
            bestand = entry.get("bestand", "")
            if not bestand:
                continue
            key = Path(bestand).name
            out[key] = _diff_compact(entry, run_id)
    return out


# ─── Layer 2 collation ───────────────────────────────────────────────────────

def _content_compact(entry: dict, run_id: str) -> dict:
    return {
        "verdict": entry.get("aanbevolen_status") or entry.get("verdict"),
        "rationale": entry.get("rationale"),
        "problemen": entry.get("concrete_problemen") or entry.get("problemen") or [],
        "sterkte": entry.get("concrete_sterke_punten") or entry.get("sterkte") or [],
        "auto": bool(entry.get("auto", False)),
        "run_id": run_id,
    }


def collect_content_verdicts(qa_dir: Path) -> dict[str, dict]:
    """Lees alle *-content-verdicts.json + qa-batch-*-verdicts.json (legacy)."""
    files = sorted(qa_dir.glob("*-content-verdicts.json"))
    files += sorted(qa_dir.glob("qa-batch-*-verdicts.json"))
    out: dict[str, dict] = {}
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  ! kan {f.name} niet lezen: {e}", file=sys.stderr)
            continue
        if isinstance(data, dict):
            run_id = data.get("run_id") or f.stem.replace("-content-verdicts", "").replace("-verdicts", "")
            verdicts = data.get("verdicts", [])
        else:
            run_id = f.stem.replace("-content-verdicts", "").replace("-verdicts", "")
            verdicts = data if isinstance(data, list) else []
        for entry in verdicts:
            bestand = entry.get("bestand", "")
            if not bestand:
                continue
            key = Path(bestand).name
            out[key] = _content_compact(entry, run_id)
    return out


# ─── Frontmatter-write ───────────────────────────────────────────────────────

def _strip_nones(d: dict) -> dict:
    """Verwijder keys met None-waarde — frontmatter blijft compacter."""
    return {k: v for k, v in d.items() if v is not None}


def _apply_to_md(
    path: Path,
    *,
    layer1: Optional[dict],
    diff: Optional[dict],
    content: Optional[dict],
    dry_run: bool,
) -> dict:
    data, body = _read_frontmatter(path)
    if data is None:
        return {"file": str(path), "skipped": "no-frontmatter"}

    prov = data.setdefault("provenance", {})
    if not isinstance(prov, dict):
        return {"file": str(path), "skipped": "provenance-not-dict"}
    trust = prov.get("trust")
    if not isinstance(trust, dict):
        trust = {}
        prov["trust"] = trust

    changed = False
    if layer1:
        compact = _strip_nones(layer1)
        if trust.get("layer1") != compact:
            trust["layer1"] = compact
            changed = True
    if diff:
        compact = _strip_nones(diff)
        if trust.get("layer1_5_diff") != compact:
            trust["layer1_5_diff"] = compact
            changed = True
    if content:
        compact = _strip_nones(content)
        if trust.get("layer2_content") != compact:
            trust["layer2_content"] = compact
            changed = True

    if changed and not dry_run:
        _write_frontmatter(path, data, body)

    return {
        "file": str(path),
        "changed": changed,
        "wrote_layer1": bool(layer1),
        "wrote_diff": bool(diff),
        "wrote_content": bool(content),
    }


# ─── Hoofdflow ───────────────────────────────────────────────────────────────

def find_md_for_basename(name: str) -> Optional[Path]:
    """Zoek de bron-MD voor een basename. Eerst resources/bronnen/, dan staging."""
    for sub in ("wetteksten", "normen", "adviezen"):
        p = RESOURCES_DIR / sub / name
        if p.exists():
            return p
    p = STAGING_DIR / name
    if p.exists():
        return p
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--qa-dir", type=Path, default=QA_DIR)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--archive-after", action="store_true",
                        help="verplaats verbruikte JSON's naar data/qa/archive/")
    args = parser.parse_args()

    print(f"=== qa_to_frontmatter (qa-dir={args.qa_dir}) ===")
    layer1_map = collect_layer1(args.qa_dir)
    diff_map = collect_diff_verdicts(args.qa_dir)
    content_map = collect_content_verdicts(args.qa_dir)

    print(f"  Layer 1 entries:    {len(layer1_map)}")
    print(f"  Layer 1.5 entries:  {len(diff_map)}")
    print(f"  Layer 2 entries:    {len(content_map)}")
    print()

    all_keys = set(layer1_map) | set(diff_map) | set(content_map)
    print(f"Te verwerken bron-MDs: {len(all_keys)}")

    n_changed = 0
    n_skipped = 0
    n_not_found = 0
    for name in sorted(all_keys):
        md = find_md_for_basename(name)
        if md is None:
            n_not_found += 1
            continue
        result = _apply_to_md(
            md,
            layer1=layer1_map.get(name),
            diff=diff_map.get(name),
            content=content_map.get(name),
            dry_run=args.dry_run,
        )
        if "skipped" in result:
            n_skipped += 1
            continue
        if result["changed"]:
            n_changed += 1

    label = "DRY-RUN" if args.dry_run else "OK"
    print(f"\n{label}: {n_changed} bestand(en) gewijzigd, {n_skipped} geskipt, "
          f"{n_not_found} niet gevonden in resources/staging.")

    if args.archive_after and not args.dry_run:
        archive_dir = args.qa_dir / "archive" / datetime.now(timezone.utc).strftime("backfill-%Y%m%d-%H%M%S")
        archive_dir.mkdir(parents=True, exist_ok=True)
        moved = 0
        for pattern in ("qa-*.json", "*-diff-verdicts.json", "*-content-verdicts.json",
                        "qa-batch-*-verdicts.json"):
            for f in args.qa_dir.glob(pattern):
                if f.is_file():
                    shutil.move(str(f), str(archive_dir / f.name))
                    moved += 1
        print(f"Archive: {moved} bestand(en) verplaatst naar {archive_dir.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
