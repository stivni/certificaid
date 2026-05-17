#!/usr/bin/env python3
"""
Trust-toepassings-tool voor de bronnen-QA-gate (ADR-005 §5).

Twee modi:

  1. **Mens-override** (`--status ... --confirmed-by human`): schrijft direct
     `provenance.trust.status` (+ confirmed_by="human", rationale). Raakt
     `layer2` NIET aan. Toepassing: één bron, een hele collection, of een
     hele bron-rol.

  2. **Agent-verdict-toepassing** (`--apply-from-verdicts FILE
     --subagent-id ID`): leest een verdicts-JSON (output van
     `qa_subagent_prompt.md`) en schrijft per bron `trust.layer2.*` (status,
     agent, run_at, rationale, concrete_problemen). De afgeleide regel uit
     ADR-004 (`trust.status = trusted ⇔ layer2.status = trusted OR
     confirmed_by = human`) zet `trust.status` automatisch. Een bestaande
     mens-override (`confirmed_by = "human"`) wordt NIET overschreven.

Achtergrond:
  - Trust-statussen: unreviewed | trusted | needs-rework | rejected
  - Default-state komt uit `convert.py` (zet `unreviewed` bij elke nieuwe bron)
  - Filter in `tools/rag/rag_index.py` selecteert default `status == "trusted"`

Voorbeelden:

  # Eén bron handmatig
  python tools/etl/mark_trusted.py --bron resources/bronnen/normen/X.md \\
      --status trusted --rationale "Heading-injectie OK, content compleet"

  # Hele collection in één keer (alle ITAA-normen)
  python tools/etl/mark_trusted.py --collection itaa-normen --status trusted \\
      --rationale "Vandaag heading-geïnjecteerd via inject_norm_headings.py"

  # Vanuit subagent-rapport: pas alleen "trusted"-aanbevelingen toe
  python tools/etl/mark_trusted.py --apply-from-verdicts data/etl/qa/<run-id>-verdicts.json \\
      --only-status trusted

  # Inverse: terug naar unreviewed bij ETL-update
  python tools/etl/mark_trusted.py --bron X --status unreviewed
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.lib.provenance import (  # noqa: E402
    TRUST_VALID_STATUSES,
    mark_trust,
    read_trust,
    write_layer2,
)

# Mapping van het JSON-veld `aanbevolen_status` (uit qa_subagent_prompt.md
# output) naar `layer2.status`.
LAYER2_RECOMMENDED = {
    "trusted": "trusted",
    "needs-rework": "needs-rework",
    "rejected": "rejected",
}

BRON_DIRS = {
    "wettekst": ROOT / "resources" / "bronnen" / "wetteksten",
    "norm":     ROOT / "resources" / "bronnen" / "normen",
    "advies":   ROOT / "resources" / "bronnen" / "adviezen",
}
COLLECTION_TO_DIR = {
    "wetteksten":   BRON_DIRS["wettekst"],
    "itaa-normen":  BRON_DIRS["norm"],
    "cbn-adviezen": BRON_DIRS["advies"],
}
SKIP_FILES = {"INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"}


def resolve_bron_path(arg: str) -> Path:
    """Accept absolute, relative-to-root, or bare filename (search across dirs)."""
    p = Path(arg)
    if p.is_absolute() and p.exists():
        return p
    candidate = ROOT / arg
    if candidate.exists():
        return candidate
    # Bare filename — zoek in alle bron-mappen
    if "/" not in arg:
        for d in BRON_DIRS.values():
            hits = list(d.glob(arg))
            if len(hits) == 1:
                return hits[0]
            if len(hits) > 1:
                raise SystemExit(f"Meerdere matches voor {arg!r}: {hits}")
    raise SystemExit(f"Bron niet gevonden: {arg!r}")


def collect_files_for_scope(
    *,
    bron_rol: Optional[str] = None,
    collection: Optional[str] = None,
) -> list[Path]:
    if collection:
        if collection not in COLLECTION_TO_DIR:
            raise SystemExit(f"Onbekende collection: {collection!r}. Geldig: {sorted(COLLECTION_TO_DIR)}")
        d = COLLECTION_TO_DIR[collection]
    elif bron_rol:
        if bron_rol not in BRON_DIRS:
            raise SystemExit(f"Onbekende bron-rol: {bron_rol!r}. Geldig: {sorted(BRON_DIRS)}")
        d = BRON_DIRS[bron_rol]
    else:
        raise SystemExit("Geef --collection of --bron-rol op.")

    return [f for f in sorted(d.glob("*.md")) if f.name not in SKIP_FILES]


def apply_one(
    path: Path,
    status: str,
    *,
    confirmed_by: str,
    rationale: Optional[str],
    dry_run: bool,
    caveat: Optional[str] = None,
) -> str:
    """Pas trust toe op één bestand. Returnt status-string voor rapport.

    Trust-regel (ADR-004): status=trusted vereist confirmed_by="human" of
    layer2.status="trusted". mark_trusted.py is de mens-override-tool:
    --confirmed-by default "human". layer2 wordt NIET aangeraakt door dit script.

    Caveat: bekende beperking van een trusted-bron (bv. tabel-bijlage met
    kolom-bleed). Wordt in INDEX.md getoond met ⚠️.
    """
    try:
        existing = read_trust(path)
    except Exception as exc:
        return f"error: {exc}"

    # Caveat-update detecteren: zelfde status maar caveat-wijziging is OK
    caveat_changed = caveat is not None and caveat != (existing.caveat or "")
    if existing.status == status and not caveat_changed:
        return "unchanged"

    if dry_run:
        change_desc = f"{existing.status} -> {status}"
        if caveat_changed:
            change_desc += f" (+caveat)"
        return f"would-change ({change_desc})"

    try:
        mark_trust(
            path,
            status,
            confirmed_by=confirmed_by,
            rationale=rationale,
            caveat=caveat,
        )
        change_desc = f"{existing.status} -> {status}"
        if caveat_changed:
            change_desc += " (+caveat)"
        return f"changed ({change_desc})"
    except ValueError as exc:
        return f"error: {exc}"


def cmd_single(args: argparse.Namespace) -> None:
    path = resolve_bron_path(args.bron)
    confirmed_by = args.confirmed_by or "human"
    result = apply_one(
        path,
        args.status,
        confirmed_by=confirmed_by,
        rationale=args.rationale,
        dry_run=args.dry_run,
        caveat=args.caveat,
    )
    print(f"{path.relative_to(ROOT)}: {result}")


def cmd_scope(args: argparse.Namespace) -> None:
    files = collect_files_for_scope(bron_rol=args.bron_rol, collection=args.collection)
    if not files:
        print("Geen bestanden gevonden.")
        return

    confirmed_by = args.confirmed_by or "human"
    counters: dict[str, int] = {}
    print(f"=== mark_trusted (scope) {'(dry-run) ' if args.dry_run else ''}===")
    print(f"Bestanden: {len(files)} | doelstatus: {args.status}")
    print()

    for f in files:
        result = apply_one(
            f,
            args.status,
            confirmed_by=confirmed_by,
            rationale=args.rationale,
            dry_run=args.dry_run,
        )
        # Tel categorie van resultaat
        bucket = result.split(" ")[0]
        counters[bucket] = counters.get(bucket, 0) + 1

    print("Resultaten:")
    for k in sorted(counters):
        print(f"  {k:20s} {counters[k]:>5d}")


def cmd_apply_from_verdicts(args: argparse.Namespace) -> None:
    verdicts_path = Path(args.apply_from_verdicts).resolve()
    if not verdicts_path.exists():
        raise SystemExit(f"Verdicts-bestand niet gevonden: {verdicts_path}")

    raw = json.loads(verdicts_path.read_text(encoding="utf-8"))
    # Accept either a top-level array of verdicts OR an object with key "verdicts" / "bronnen"
    if isinstance(raw, list):
        verdicts = raw
    elif isinstance(raw, dict):
        verdicts = raw.get("verdicts") or raw.get("bronnen") or []
    else:
        raise SystemExit(f"Onverwacht JSON-formaat in {verdicts_path}")

    if not verdicts:
        raise SystemExit("Geen verdicts gevonden in bestand.")

    only_filter = set(args.only_status) if args.only_status else None
    agent = (
        f"subagent-{args.subagent_id}" if args.subagent_id else "subagent-unspecified"
    )

    counters: dict[str, int] = {}
    skipped_filter = 0
    try:
        verdicts_display = verdicts_path.relative_to(ROOT)
    except ValueError:
        verdicts_display = verdicts_path
    print(f"=== mark_trusted --apply-from-verdicts {'(dry-run) ' if args.dry_run else ''}===")
    print(f"Verdicts: {verdicts_display}")
    print(f"layer2.agent: {agent}")
    if only_filter:
        print(f"Filter: alleen aanbevolen-statussen {sorted(only_filter)}")
    print()

    for v in verdicts:
        bestand = v.get("bestand")
        recommended = v.get("aanbevolen_status")
        if not bestand or not recommended:
            print(f"  WARN: verdict mist 'bestand' of 'aanbevolen_status': {v}")
            continue

        if recommended not in LAYER2_RECOMMENDED:
            print(
                f"  WARN: ongeldige aanbevolen_status {recommended!r} voor {bestand}; "
                f"verwacht een van {sorted(LAYER2_RECOMMENDED)}; overgeslagen"
            )
            continue
        layer2_status = LAYER2_RECOMMENDED[recommended]

        if only_filter and recommended not in only_filter:
            skipped_filter += 1
            continue

        try:
            path = resolve_bron_path(bestand)
        except SystemExit as exc:
            print(f"  ERROR: {exc}")
            continue

        rationale = v.get("rationale") or args.rationale
        problemen = v.get("concrete_problemen") or []

        if args.dry_run:
            existing = read_trust(path)
            old_l2 = (existing.layer2 or {}).get("status", "not_run")
            result = f"would-write-layer2 ({old_l2} -> {layer2_status})"
            bucket = "would-write-layer2"
        else:
            try:
                new_trust = write_layer2(
                    path,
                    layer2_status=layer2_status,
                    agent=agent,
                    rationale=rationale,
                    concrete_problemen=problemen,
                )
                if new_trust.confirmed_by == "human":
                    result = (
                        f"layer2={layer2_status} (top-level ongewijzigd — "
                        f"mens-override beschermt)"
                    )
                    bucket = "layer2-only"
                else:
                    result = f"layer2={layer2_status} → trust.status={new_trust.status}"
                    bucket = f"applied:{new_trust.status}"
            except Exception as exc:
                result = f"error: {exc}"
                bucket = "error"

        counters[bucket] = counters.get(bucket, 0) + 1
        if args.verbose or bucket not in {"unchanged"}:
            print(f"  {Path(bestand).name}: {result}")

    print()
    print("Samenvatting:")
    for k in sorted(counters):
        print(f"  {k:20s} {counters[k]:>5d}")
    if skipped_filter:
        print(f"  filtered-out         {skipped_filter:>5d}  (door --only-status)")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--status", choices=TRUST_VALID_STATUSES,
                   help="te zetten trust-status (vereist behalve bij --apply-from-verdicts)")
    p.add_argument("--rationale", help="optionele toelichting bij de status-wijziging")
    p.add_argument("--caveat", default=None,
                   help="optionele bekende-beperking voor een trusted bron "
                        "(wordt in INDEX.md getoond met ⚠️)")
    p.add_argument("--confirmed-by", default=None,
                   help="wie bevestigt: 'human' (default bij CLI) of '<agent-naam>' bij verdicts. "
                        "Alleen 'human' of een agent-naam zijn geldig (ADR-004).")
    p.add_argument("--dry-run", action="store_true", help="toon zonder schrijven")
    p.add_argument("--verbose", "-v", action="store_true", help="ook unchanged regels tonen")

    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--bron", help="één bron-MD (pad of bestandsnaam)")
    g.add_argument("--bron-rol", choices=sorted(BRON_DIRS), help="alle bronnen van deze rol")
    g.add_argument("--collection", choices=sorted(COLLECTION_TO_DIR), help="alle bronnen van deze collection")
    g.add_argument("--apply-from-verdicts", help="pas bulk toe vanuit een verdicts-bestand")

    p.add_argument("--only-status", nargs="+", choices=TRUST_VALID_STATUSES,
                   help="(alleen met --apply-from-verdicts) filter op aanbevolen-statussen")
    p.add_argument("--subagent-id", help="(alleen met --apply-from-verdicts) modelnaam-suffix voor confirmed_by")
    p.add_argument("--refresh", action="store_true",
                   help="na schrijven RAG-index + bron-matches refreshen "
                        "(via tools.etl.refresh_rag_and_matches). Aanbevolen na elke "
                        "trust-promotie — anders blijven anchor-bundles stale.")

    args = p.parse_args()

    if args.bron:
        if not args.status:
            p.error("--bron vereist --status")
        cmd_single(args)
    elif args.bron_rol or args.collection:
        if not args.status:
            p.error("--bron-rol/--collection vereist --status")
        cmd_scope(args)
    elif args.apply_from_verdicts:
        cmd_apply_from_verdicts(args)

    if args.refresh and not args.dry_run:
        print("\n=== --refresh: RAG-index + bron-matches verversen ===")
        from tools.etl.refresh_rag_and_matches import refresh
        refresh()


if __name__ == "__main__":
    main()
