#!/usr/bin/env python3
"""Steekproef-review tool voor de bronnen-QA-gate (ADR-005 §5 Laag 3).

Nadat de auto-trust-flow (qa_bron.py + mark_trusted.py --apply-from-verdicts)
bronnen op `trusted` heeft gezet, trekt deze tool een random steekproef voor
menselijke review. De mens bewerkt de gekozen bestanden in de editor; deze tool
detecteert via mtime of er gekeken is en cascadeert bij --mark-not-ok de hele
batch (zelfde qa_version) terug naar `unreviewed`.

Trust-velden (ADR-004 v2 schema, aangevuld door deze tool):

    provenance:
      trust:
        status: trusted
        qa_version: <run-id>
        agent_verdict_at: 2026-05-09T14:00:00Z
        confirmed_by: subagent-sonnet-4-6
        rationale: "..."
        sample_pick: true                       # gezet door --pick
        sample_reviewed_at: 2026-05-09T15:30:00Z # gezet door --mark-ok / --mark-not-ok
        sample_reviewed_by: human

Modi:

  # Trek random N% van auto-trusted bronnen uit run <run-id>
  python3 tools/etl/sample_review.py --pick <run-id> --rate 10

  # Status-overzicht (optioneel filter op run-id)
  python3 tools/etl/sample_review.py --status [<run-id>]

  # Markeer pick als OK
  python3 tools/etl/sample_review.py --mark-ok <pad>

  # Markeer pick als niet-OK; cascadeert hele batch terug naar unreviewed
  python3 tools/etl/sample_review.py --mark-not-ok <pad>

Implementatie-noot:
  De Trust-dataclass in tools/lib/provenance.py bevat (nog) niet de velden
  sample_pick / sample_reviewed_at / sample_reviewed_by / agent_verdict_at.
  Daarom werkt deze tool rechtstreeks op de YAML-frontmatter via ruamel.yaml
  round-trip (zelfde stijl als provenance.py intern). Geen extra state buiten
  de frontmatter zelf — single source of truth.
"""
from __future__ import annotations

import argparse
import io
import random
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

BRON_DIRS = [
    ROOT / "resources" / "bronnen" / "wetteksten",
    ROOT / "resources" / "bronnen" / "normen",
    ROOT / "resources" / "bronnen" / "adviezen",
]
SKIP_FILES = {"INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"}

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def _yaml() -> YAML:
    y = YAML()
    y.preserve_quotes = True
    y.indent(mapping=2, sequence=4, offset=2)
    y.width = 4096
    return y


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ─── frontmatter I/O ──────────────────────────────────────────────────────────

def _read_frontmatter(path: Path) -> tuple[Optional[dict], str]:
    """Returnt (data-dict-of-None, body). data is round-trip ruamel-object."""
    text = path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    data = _yaml().load(m.group(1)) or {}
    body = text[m.end():]
    return data, body


def _write_frontmatter(path: Path, data: dict, body: str) -> None:
    buf = io.StringIO()
    _yaml().dump(data, buf)
    path.write_text(f"---\n{buf.getvalue()}---\n{body}", encoding="utf-8")


def _get_trust(data: dict) -> Optional[dict]:
    prov = data.get("provenance") if data else None
    if not isinstance(prov, dict):
        return None
    trust = prov.get("trust")
    if not isinstance(trust, dict):
        return None
    return trust


# ─── corpus walking ───────────────────────────────────────────────────────────

def _iter_bron_files() -> list[Path]:
    files: list[Path] = []
    for d in BRON_DIRS:
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name not in SKIP_FILES:
                files.append(f)
    return files


def _is_auto_trusted(trust: dict, run_id: Optional[str] = None) -> bool:
    """Bron is auto-trusted door subagent: status=trusted, confirmed_by != human."""
    if trust.get("status") != "trusted":
        return False
    confirmed_by = (trust.get("confirmed_by") or "").lower()
    if confirmed_by == "human":
        return False
    if run_id is not None and trust.get("qa_version") != run_id:
        return False
    return True


def _agent_verdict_dt(trust: dict) -> Optional[datetime]:
    """Probeer agent_verdict_at te parsen; fallback op confirmed_at."""
    raw = trust.get("agent_verdict_at") or trust.get("confirmed_at")
    if not raw:
        return None
    raw = str(raw).replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


# ─── commando: --pick ─────────────────────────────────────────────────────────

def cmd_pick(run_id: str, rate: float, *, seed: Optional[int] = None) -> None:
    if rate <= 0 or rate > 100:
        raise SystemExit(f"--rate moet > 0 en ≤ 100 zijn (kreeg {rate})")

    candidates: list[Path] = []
    for path in _iter_bron_files():
        data, _ = _read_frontmatter(path)
        if data is None:
            continue
        trust = _get_trust(data)
        if trust is None:
            continue
        if not _is_auto_trusted(trust, run_id=run_id):
            continue
        candidates.append(path)

    if not candidates:
        print(f"Geen auto-trusted bronnen gevonden voor qa_version={run_id!r}.")
        return

    n = max(1, round(len(candidates) * rate / 100.0))
    rng = random.Random(seed if seed is not None else run_id)
    picks = rng.sample(candidates, k=min(n, len(candidates)))

    print(f"=== sample_review --pick run-id={run_id} rate={rate}% ===")
    print(f"Auto-trusted kandidaten: {len(candidates)}")
    print(f"Steekproef ({n}):")
    for path in picks:
        data, body = _read_frontmatter(path)
        if data is None:
            continue
        trust = _get_trust(data)
        if trust is None:
            continue
        trust["sample_pick"] = True
        # init review-velden als ze ontbreken (expliciete null = "nog niet beoordeeld")
        trust.setdefault("sample_reviewed_at", None)
        trust.setdefault("sample_reviewed_by", None)
        _write_frontmatter(path, data, body)
        try:
            rel = path.relative_to(ROOT)
        except ValueError:
            rel = path
        print(f"  pick  {rel}")


# ─── commando: --status ───────────────────────────────────────────────────────

def cmd_status(run_id: Optional[str]) -> None:
    rows: list[tuple[str, str, Path]] = []
    for path in _iter_bron_files():
        data, _ = _read_frontmatter(path)
        if data is None:
            continue
        trust = _get_trust(data)
        if trust is None:
            continue
        if not trust.get("sample_pick"):
            continue
        if run_id is not None and trust.get("qa_version") != run_id:
            continue

        reviewed_at = trust.get("sample_reviewed_at")
        agent_dt = _agent_verdict_dt(trust)
        try:
            mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        except OSError:
            mtime = None

        if reviewed_at:
            # Beoordeeld: status bepaalt OK vs niet-OK.
            # Als status weer "unreviewed" is → cascadeert door --mark-not-ok elders;
            # als status nog "trusted" is → OK.
            if trust.get("status") == "trusted":
                marker = "OK ✓"
            else:
                marker = "niet-OK ✗"
        elif agent_dt is not None and mtime is not None and mtime > agent_dt:
            marker = "bewerkt-niet-gemerkt 🔍"
        else:
            marker = "uitstaand ⏳"

        try:
            rel = str(path.relative_to(ROOT))
        except ValueError:
            rel = str(path)
        rows.append((marker, trust.get("qa_version") or "?", path))

    header = f"=== sample_review --status"
    if run_id:
        header += f" run-id={run_id}"
    header += " ==="
    print(header)
    if not rows:
        print("Geen sample_pick-bronnen gevonden.")
        return

    # Tel per categorie
    counts: dict[str, int] = {}
    for marker, _, _ in rows:
        counts[marker] = counts.get(marker, 0) + 1

    rows.sort(key=lambda r: (r[0], r[1], str(r[2])))
    for marker, qa_version, path in rows:
        try:
            rel = path.relative_to(ROOT)
        except ValueError:
            rel = path
        print(f"  {marker:30s}  qa={qa_version:20s}  {rel}")

    print()
    print("Samenvatting:")
    for k in sorted(counts):
        print(f"  {k:30s} {counts[k]:>4d}")


# ─── commando: --mark-ok / --mark-not-ok ──────────────────────────────────────

def _resolve_path(arg: str) -> Path:
    p = Path(arg)
    if p.is_absolute() and p.exists():
        return p
    cand = ROOT / arg
    if cand.exists():
        return cand
    raise SystemExit(f"Bestand niet gevonden: {arg!r}")


def cmd_mark_ok(arg: str) -> None:
    path = _resolve_path(arg)
    data, body = _read_frontmatter(path)
    if data is None:
        raise SystemExit(f"{path}: geen frontmatter.")
    trust = _get_trust(data)
    if trust is None:
        raise SystemExit(f"{path}: geen provenance.trust-blok.")
    if not trust.get("sample_pick"):
        raise SystemExit(f"{path}: sample_pick is niet true (geen steekproef-pick).")

    trust["sample_reviewed_at"] = now_iso()
    trust["sample_reviewed_by"] = "human"
    # status blijft 'trusted'
    _write_frontmatter(path, data, body)

    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        rel = path
    print(f"OK ✓ {rel}")
    print(f"  trust.status blijft: {trust.get('status')}")
    print(f"  sample_reviewed_at: {trust['sample_reviewed_at']}")


def cmd_mark_not_ok(arg: str) -> None:
    path = _resolve_path(arg)
    data, body = _read_frontmatter(path)
    if data is None:
        raise SystemExit(f"{path}: geen frontmatter.")
    trust = _get_trust(data)
    if trust is None:
        raise SystemExit(f"{path}: geen provenance.trust-blok.")
    if not trust.get("sample_pick"):
        raise SystemExit(f"{path}: sample_pick is niet true (geen steekproef-pick).")

    qa_version = trust.get("qa_version")
    if not qa_version:
        raise SystemExit(f"{path}: trust.qa_version ontbreekt; cascade onmogelijk.")

    timestamp = now_iso()
    cascade_msg = f" — sample_review afgekeurd door mens op {timestamp}"

    # 1) Markeer de pick zelf als reviewed + niet-OK (status → unreviewed via cascade hieronder).
    trust["sample_reviewed_at"] = timestamp
    trust["sample_reviewed_by"] = "human"
    _write_frontmatter(path, data, body)

    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        rel = path
    print(f"niet-OK ✗ {rel}")
    print(f"  qa_version: {qa_version}")
    print()
    print("Cascade: alle auto-trusted bronnen in dezelfde batch → unreviewed")

    cascade_count = 0
    for cand in _iter_bron_files():
        cdata, cbody = _read_frontmatter(cand)
        if cdata is None:
            continue
        ctrust = _get_trust(cdata)
        if ctrust is None:
            continue
        if ctrust.get("qa_version") != qa_version:
            continue
        if not _is_auto_trusted(ctrust, run_id=qa_version):
            # ook al niet meer trusted; sla over
            continue

        ctrust["status"] = "unreviewed"
        existing_rationale = ctrust.get("rationale") or ""
        ctrust["rationale"] = (existing_rationale + cascade_msg).strip()
        _write_frontmatter(cand, cdata, cbody)
        cascade_count += 1
        try:
            crel = cand.relative_to(ROOT)
        except ValueError:
            crel = cand
        print(f"  cascade  {crel} → unreviewed")

    print()
    print(f"Totaal teruggezet: {cascade_count}")


# ─── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--pick", metavar="RUN_ID", help="trek random sample uit auto-trusted bronnen")
    g.add_argument("--status", nargs="?", const="__ALL__", metavar="RUN_ID",
                   help="toon overzicht (optioneel filter op run-id)")
    g.add_argument("--mark-ok", metavar="BESTAND", help="markeer pick als OK")
    g.add_argument("--mark-not-ok", metavar="BESTAND",
                   help="markeer pick als niet-OK; cascadeert batch → unreviewed")

    p.add_argument("--rate", type=float, default=10.0,
                   help="(met --pick) percentage te trekken (default: 10)")
    p.add_argument("--seed", type=int, help="(met --pick) RNG-seed voor reproduceerbaarheid")

    args = p.parse_args()

    if args.pick:
        cmd_pick(args.pick, args.rate, seed=args.seed)
    elif args.status:
        run_id = None if args.status == "__ALL__" else args.status
        cmd_status(run_id)
    elif args.mark_ok:
        cmd_mark_ok(args.mark_ok)
    elif args.mark_not_ok:
        cmd_mark_not_ok(args.mark_not_ok)


if __name__ == "__main__":
    main()
