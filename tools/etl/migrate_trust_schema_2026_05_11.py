#!/usr/bin/env python3
"""
Eenmalig migratie-script: brengt alle bron-MDs op het nieuwe uniforme
provenance.trust-schema zoals gedefinieerd in ADR-004 (2026-05-11).

Transformaties per bron:

1.  DROP: trust.qa_version, trust.agent_verdict_at
2.  DROP: trust.sample_pick, trust.sample_reviewed_at, trust.sample_reviewed_by
3.  DROP: trust.layer1_5_diff (heel blok)
4.  RENAME: trust.layer1.verdict → trust.layer1.status
5.  ADD: trust.layer1.run_at: null (als afwezig)
6.  RENAME: trust.layer2_content → trust.layer2
         trust.layer2.verdict → trust.layer2.status
         trust.layer2.reviewer → trust.layer2.agent (als aanwezig)
         trust.layer2.problemen → trust.layer2.concrete_problemen (als aanwezig)
7.  ADD: trust.layer2.run_at: null (als afwezig)
8.  confirmed_by: "qa-laag1-auto" | "default" | null | None → null
9.  Trust-status-herberekening:
      - rejected/needs-rework: behoud
      - confirmed_by="human": trusted behouden
      - layer2.status="trusted": trusted behouden, confirmed_by=layer2.agent
      - anders: downgrade naar unreviewed, confirmed_by=null, rationale=null, confirmed_at=null
10. NO_TRUST / geen provenance.trust → minimum-skelet (unreviewed, all not_run)

Gebruik:
    python3 tools/etl/migrate_trust_schema_2026_05_11.py --dry-run
    python3 tools/etl/migrate_trust_schema_2026_05_11.py

Loggt per bron: [SKIP|MIGR|SKEL|EDGE] bestand  oud→nieuw
"""
from __future__ import annotations

import argparse
import io
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from ruamel.yaml import YAML  # noqa: E402

BRON_DIRS = {
    "wettekst": ROOT / "resources" / "bronnen" / "wetteksten",
    "norm":     ROOT / "resources" / "bronnen" / "normen",
    "advies":   ROOT / "resources" / "bronnen" / "adviezen",
}
SKIP_FILES = {"INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"}

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)

# confirmed_by-waarden die gelden als "geen mens, geen agent" → null
_PSEUDO_CONFIRMED_BY = {"qa-laag1-auto", "default", None, "None"}


def _yaml() -> YAML:
    y = YAML()
    y.preserve_quotes = False
    y.default_flow_style = False
    y.indent(mapping=2, sequence=4, offset=2)
    y.width = 4096
    return y


def _read_frontmatter(path: Path) -> tuple[dict | None, str]:
    text = path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    data = _yaml().load(m.group(1)) or {}
    return data, text[m.end():]


def _write_frontmatter(path: Path, data: dict, body: str) -> None:
    buf = io.StringIO()
    _yaml().dump(data, buf)
    path.write_text(f"---\n{buf.getvalue()}---\n{body}", encoding="utf-8")


def _to_plain(obj):
    """Recursief CommentedMap → plain dict/list."""
    if hasattr(obj, "items"):
        return {k: _to_plain(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_to_plain(v) for v in obj]
    return obj


def _minimum_trust_skeleton() -> dict:
    """Minimaal trust-blok voor bronnen zonder enige trust-info."""
    return {
        "status": "unreviewed",
        "confirmed_at": None,
        "confirmed_by": None,
        "rationale": None,
        "layer1": {
            "status": "not_run",
            "run_id": None,
            "run_at": None,
            "heading_count": None,
            "max_section_chars": None,
            "file_size_chars": None,
            "flags": [],
        },
        "layer2": {
            "status": "not_run",
            "agent": None,
            "run_at": None,
            "rationale": None,
            "concrete_problemen": [],
        },
    }


def migrate_trust(trust_raw: dict) -> tuple[dict, str]:
    """Transformeer een trust-blok naar het nieuwe schema.

    Returnt (nieuw_trust_dict, log_beschrijving).
    """
    trust = _to_plain(trust_raw) if trust_raw else {}

    oud_status = trust.get("status", "MISSING")
    oud_confirmed_by = trust.get("confirmed_by")

    # ── Stap 1-3: DROP verouderde top-level velden ───────────────────────────
    for drop_key in (
        "qa_version", "agent_verdict_at",
        "sample_pick", "sample_reviewed_at", "sample_reviewed_by",
        "layer1_5_diff",
    ):
        trust.pop(drop_key, None)

    # ── Stap 4-5: layer1 transformatie ───────────────────────────────────────
    l1 = trust.get("layer1")
    if isinstance(l1, dict):
        l1 = _to_plain(l1)
        # verdict → status
        if "verdict" in l1 and "status" not in l1:
            l1["status"] = l1.pop("verdict")
        # run_at toevoegen als afwezig
        if "run_at" not in l1:
            l1["run_at"] = None
        # Gestandaardiseerde volgorde van keys
        ordered_l1 = {
            "status": l1.get("status", "not_run"),
            "run_id": l1.get("run_id"),
            "run_at": l1.get("run_at"),
            "heading_count": l1.get("heading_count"),
            "max_section_chars": l1.get("max_section_chars"),
            "file_size_chars": l1.get("file_size_chars"),
            "flags": l1.get("flags", []),
        }
        trust["layer1"] = ordered_l1
    else:
        trust["layer1"] = {
            "status": "not_run",
            "run_id": None,
            "run_at": None,
            "heading_count": None,
            "max_section_chars": None,
            "file_size_chars": None,
            "flags": [],
        }

    # ── Stap 6-7: layer2_content → layer2 ────────────────────────────────────
    l2_raw = trust.pop("layer2_content", None) or trust.pop("layer2", None)
    if isinstance(l2_raw, dict):
        l2 = _to_plain(l2_raw)
        # verdict → status
        if "verdict" in l2 and "status" not in l2:
            l2["status"] = l2.pop("verdict")
        # reviewer → agent
        if "reviewer" in l2 and "agent" not in l2:
            l2["agent"] = l2.pop("reviewer")
        # problemen → concrete_problemen
        if "problemen" in l2 and "concrete_problemen" not in l2:
            l2["concrete_problemen"] = l2.pop("problemen")
        # run_at toevoegen als afwezig
        if "run_at" not in l2:
            l2["run_at"] = None
        # DROP "sterkte" (niet in nieuw schema)
        l2.pop("sterkte", None)
        # DROP "auto" (niet in nieuw schema)
        l2.pop("auto", None)
        # DROP "run_id" van layer2 (niet in nieuw schema op layer2-niveau)
        l2.pop("run_id", None)
        ordered_l2 = {
            "status": l2.get("status", "not_run"),
            "agent": l2.get("agent"),
            "run_at": l2.get("run_at"),
            "rationale": l2.get("rationale"),
            "concrete_problemen": l2.get("concrete_problemen", []),
        }
        trust["layer2"] = ordered_l2
    else:
        trust["layer2"] = {
            "status": "not_run",
            "agent": None,
            "run_at": None,
            "rationale": None,
            "concrete_problemen": [],
        }

    # ── Stap 8: confirmed_by normaliseren ─────────────────────────────────────
    cb = trust.get("confirmed_by")
    if str(cb) in {"qa-laag1-auto", "default", "None"} or cb is None:
        trust["confirmed_by"] = None

    # ── Stap 9: Trust-status-herberekening ───────────────────────────────────
    current_status = trust.get("status", "unreviewed")
    layer2_status = trust["layer2"].get("status", "not_run")
    layer2_agent = trust["layer2"].get("agent")
    new_confirmed_by = trust.get("confirmed_by")

    if current_status in ("rejected", "needs-rework"):
        # Regel 1: behoud rejected/needs-rework (confirmed_by al genormaliseerd)
        nieuw_status = current_status
        reden = "behoud (rejected/needs-rework)"
    elif new_confirmed_by == "human":
        # Regel 2: human override
        nieuw_status = "trusted"
        reden = "behoud trusted (human)"
    elif layer2_status == "trusted":
        # Regel 3: layer2 trusted
        # confirmed_by: gebruik layer2.agent als dat gezet is; anders behoud
        # de bestaande top-level confirmed_by (die in het oude schema al correct
        # was gezet door promote_staging.py).
        nieuw_status = "trusted"
        if layer2_agent:
            trust["confirmed_by"] = layer2_agent
        # else: behoud bestaande confirmed_by (kan een agent-naam zijn die al
        # op trust-top-level stond in het oude schema)
        reden = f"behoud trusted (layer2.agent={layer2_agent or trust.get('confirmed_by')})"
    else:
        # Regel 4: downgrade naar unreviewed
        nieuw_status = "unreviewed"
        trust["confirmed_by"] = None
        trust["rationale"] = None
        trust["confirmed_at"] = None
        reden = f"downgrade → unreviewed (was: {oud_status}, cb: {oud_confirmed_by})"

    trust["status"] = nieuw_status

    # Gestandaardiseerde top-level volgorde
    ordered_trust = {
        "status": trust["status"],
        "confirmed_at": trust.get("confirmed_at"),
        "confirmed_by": trust.get("confirmed_by"),
        "rationale": trust.get("rationale"),
        "layer1": trust["layer1"],
        "layer2": trust["layer2"],
    }

    log = (
        f"[MIGR] status: {oud_status!r} → {nieuw_status!r}  "
        f"confirmed_by: {str(oud_confirmed_by)!r} → {str(trust.get('confirmed_by'))!r}  "
        f"({reden})"
    )
    return ordered_trust, log


def process_file(path: Path, dry_run: bool) -> tuple[str, str]:
    """Verwerk één bron-MD. Returnt (actie, log)."""
    data, body = _read_frontmatter(path)
    if data is None:
        return "SKIP", f"[SKIP] geen frontmatter: {path.name}"

    prov = data.get("provenance")
    if not isinstance(prov, dict):
        prov = {}
        data["provenance"] = prov

    trust_raw = prov.get("trust")

    # Edge case: leeg trust-blok (NO_TRUST) → minimum-skelet
    if not isinstance(trust_raw, dict) or not trust_raw:
        new_trust = _minimum_trust_skeleton()
        log = f"[SKEL] {path.name} → minimum-skelet (unreviewed, all not_run)"
        if not dry_run:
            prov["trust"] = new_trust
            _write_frontmatter(path, data, body)
        return "SKEL", log

    # Normale migratie
    new_trust, mig_log = migrate_trust(trust_raw)
    log = f"{mig_log}  [{path.name}]"

    if not dry_run:
        prov["trust"] = new_trust
        _write_frontmatter(path, data, body)

    return "MIGR", log


def collect_files() -> list[Path]:
    files: list[Path] = []
    for d in BRON_DIRS.values():
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name in SKIP_FILES:
                continue
            files.append(f)
    return files


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dry-run", action="store_true",
                   help="toon statistieken zonder te schrijven")
    p.add_argument("--verbose", "-v", action="store_true",
                   help="log ook ongewijzigde bronnen")
    args = p.parse_args()

    files = collect_files()
    print(f"=== migrate_trust_schema_2026_05_11 {'(DRY-RUN) ' if args.dry_run else ''}===")
    print(f"Bestanden: {len(files)}\n")

    counters: Counter = Counter()
    logs: list[str] = []

    for path in files:
        actie, log = process_file(path, dry_run=args.dry_run)
        counters[actie] += 1
        logs.append(log)
        if args.verbose or actie in ("SKEL", "EDGE", "SKIP"):
            print(f"  {log}")
        elif actie == "MIGR":
            # Toon altijd de migratie-log (inclusief wat er veranderd is)
            print(f"  {log}")

    print(f"\n=== Samenvatting ===")
    for k, v in sorted(counters.items()):
        print(f"  {k:6s} {v:>5d}")
    print(f"  TOTAAL {len(files):>4d}")


if __name__ == "__main__":
    main()
