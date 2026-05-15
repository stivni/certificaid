"""
Subagent-runner voor blok 3 ENRICH (ADR-008 §13.3 + §13.7).

Filtert open gaps uit data/extractie/gaps.json voor een programmaonderdeel,
bouwt een input-payload per record (record + gap-entries + bron-bundle),
en schrijft instructies voor een Opus-subagent die de verrijking uitvoert.

Na de subagent-run markeert dit script de verwerkte gaps als
`status: "enriched-pending-verify"` (niet "applied" — auto_merge.py
controleert eerst of er niets verloren gegaan is).

Gebruik:
  python3 -m tools.extractie.enrich_records --programmaonderdeel 1.4
  python3 -m tools.extractie.enrich_records --programmaonderdeel 1.4 \\
      --only-prio hoog,midden
  python3 -m tools.extractie.enrich_records --programmaonderdeel 1.4 \\
      --markeer-gaps-na-run data/extractie/verify-runs/verify-run-....md
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concept_records"
GAPS_FILE = ROOT / "data" / "extractie" / "gaps.json"
BUNDLES_DIR = ROOT / "data" / "extractie"
PROMPTS_DIR = ROOT / "prompts"
ENRICH_PROMPT = PROMPTS_DIR / "concept-enrich-v1.md"


# ─── Helpers ───────────────────────────────────────────────────────────────────


def laad_gaps(gaps_bestand: Path, status_filter: str = "open") -> list[dict]:
    """Laad gap-entries met een bepaalde status."""
    if not gaps_bestand.exists():
        return []
    try:
        alle_gaps = json.loads(gaps_bestand.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    return [g for g in alle_gaps if g.get("status") == status_filter]


def filter_gaps_voor_programmaonderdeel(
    gaps: list[dict],
    records: list[dict],
    prio_filter: list[str] | None,
) -> dict[str, list[dict]]:
    """Groepeer open gaps per record_id, gefilterd op prioriteit.

    Retourneert een dict: record_id → lijst van gap-entries.
    Alleen records die in de meegeleverde `records`-lijst zitten worden meegenomen.
    """
    beschikbare_ids = {r.get("id", "") for r in records}
    gegroepeerd: dict[str, list[dict]] = {}

    for gap in gaps:
        record_id = gap.get("record_id", "")
        if record_id not in beschikbare_ids:
            continue
        if prio_filter and gap.get("prio") not in prio_filter:
            continue
        gegroepeerd.setdefault(record_id, []).append(gap)

    return gegroepeerd


def laad_record(record_id: str) -> dict | None:
    """Laad een concept-record uit data/concepten/records/<id>.json."""
    pad = RECORDS_DIR / f"{record_id}.json"
    if not pad.exists():
        return None
    try:
        return json.loads(pad.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def zoek_bron_bundle(record: dict, programmaonderdeel_id: str) -> list[dict]:
    """Zoek de meest recente bron-bundle voor de anchors van dit record.

    Kijkt in data/extractie/<po>/bundles/ naar bundle-bestanden die overeenkomen
    met de linked_anchors[] van het record. Retourneert een gecombineerde lijst
    van chunks (gededupliceerd op chunk_id).
    """
    gekoppelde_anchors = record.get("linked_anchors", [])
    bundles_map_hoofd = BUNDLES_DIR / programmaonderdeel_id / "bundles"
    alle_chunks: dict[str, dict] = {}  # chunk_id → chunk

    # Zoek ook in andere PO-mappen voor cross-PO anchors
    po_ids = {anker.split(".")[0] + "." + anker.split(".")[1] for anker in gekoppelde_anchors if "." in anker}

    for po_id in po_ids:
        bundles_map = BUNDLES_DIR / po_id / "bundles"
        if not bundles_map.exists():
            continue
        for anker_id in gekoppelde_anchors:
            if not anker_id.startswith(po_id + "."):
                continue
            # Bouw de verwachte bestandsnaam op (slugify met koppeltekens)
            import re
            slug = re.sub(r"[^a-zA-Z0-9.-]+", "-", anker_id).strip("-")
            bundle_pad = bundles_map / f"{po_id}-{slug}.json"
            if bundle_pad.exists():
                try:
                    bundle_data = json.loads(bundle_pad.read_text(encoding="utf-8"))
                    for chunk in bundle_data.get("bundle", []):
                        chunk_id = chunk.get("chunk_id", "")
                        if chunk_id and chunk_id not in alle_chunks:
                            alle_chunks[chunk_id] = chunk
                except (json.JSONDecodeError, OSError):
                    pass

    return list(alle_chunks.values())


def schrijf_subagent_instructies(
    programmaonderdeel_id: str,
    records_met_gaps: list[dict],
    run_id: str,
    werkmap: Path,
) -> Path:
    """Schrijf Markdown-instructies voor de Opus ENRICH-subagent.

    Elk record krijgt zijn eigen sectie met:
    - Het volledige bestaande record (inline JSON)
    - De gap-entries voor dat record
    - Beschikbare bron-chunks (samenvatting van beschikbare bundles)
    """
    werkmap.mkdir(parents=True, exist_ok=True)
    instructies_pad = werkmap / f"enrich-instructies-{run_id}.md"

    prompt_tekst = ENRICH_PROMPT.read_text(encoding="utf-8") if ENRICH_PROMPT.exists() else (
        f"[WAARSCHUWING: {ENRICH_PROMPT} niet gevonden — laad prompts/concept-enrich-v1.md handmatig]"
    )

    secties: list[str] = []
    for invoer in records_met_gaps:
        record = invoer["record"]
        gap_entries = invoer["gap_entries"]
        bron_bundle = invoer["bron_bundle"]
        record_id = record.get("id", "?")

        bundle_samenvatting = (
            f"{len(bron_bundle)} chunks beschikbaar "
            f"(bronnen: {', '.join(sorted({c.get('bron_rol', '?') for c in bron_bundle}))})"
        )

        # Schrijf de bron-bundle naar een apart bestand om de instructies leesbaar te houden
        bundle_pad = werkmap / f"bundle-{record_id}-{run_id}.json"
        bundle_pad.write_text(
            json.dumps(bron_bundle, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        secties.append(f"""
## Record: `{record_id}`

**Gaps te verwerken** ({len(gap_entries)} stuks):

```json
{json.dumps(gap_entries, ensure_ascii=False, indent=2)}
```

**Bron-bundle**: `{bundle_pad.relative_to(ROOT)}` — {bundle_samenvatting}

**Bestaand record** (`data/concepten/records/{record_id}.json`):

```json
{json.dumps(record, ensure_ascii=False, indent=2)}
```

---
""")

    aantal_records = len(records_met_gaps)
    aantal_gaps = sum(len(r["gap_entries"]) for r in records_met_gaps)

    instructies = f"""# ENRICH-run {run_id} — Instructies voor Opus-subagent

**Programmaonderdeel**: {programmaonderdeel_id}
**Run-id**: {run_id}
**Gegenereerd op**: {datetime.now(timezone.utc).isoformat(timespec="seconds")}
**Records te verwerken**: {aantal_records}
**Gaps te verwerken**: {aantal_gaps}

## Jouw taak

Verrijk de onderstaande concept-records door de gevraagde gaps in te vullen.
Werk conform `prompts/concept-enrich-v1.md` (prompt hieronder als referentie).

**Hard contract** (herhaling van de prompt):
- Behoud álle bestaande velden en array-items.
- Corrigeren mag — verplicht met `corrected_from` + `correction_reason` + bron.
- Verwijderen verboden.
- Alleen gevraagde gaps verwerken.

## Na je run

Na het verwerken van alle records, schrijf een korte samenvatting naar stdout
zoals beschreven in de prompt.

**Markeer GEEN gap-statussen** — dat doet `enrich_records.py --markeer-gaps-na-run`.

---

## Records en gaps

{''.join(secties)}

---

## Prompt-referentie (concept-enrich-v1.md)

{prompt_tekst}
"""

    instructies_pad.write_text(instructies, encoding="utf-8")
    return instructies_pad


def markeer_gaps_als_enriched(
    gap_entries: list[dict],
    gaps_bestand: Path,
    run_id: str,
) -> int:
    """Markeer verwerkte gaps als 'enriched-pending-verify'.

    Zoekt elke gap op basis van record_id + aspect + status:open en
    update de status. Retourneert het aantal gemarkeerde gaps.
    """
    if not gaps_bestand.exists():
        return 0
    alle_gaps = json.loads(gaps_bestand.read_text(encoding="utf-8"))

    # Bouw een opzoekset van te markeren gaps
    te_markeren = {
        (g["record_id"], g["aspect"])
        for g in gap_entries
        if g.get("status") == "open"
    }

    gemarkeerd = 0
    nu = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for gap in alle_gaps:
        sleutel = (gap.get("record_id", ""), gap.get("aspect", ""))
        if sleutel in te_markeren and gap.get("status") == "open":
            gap["status"] = "enriched-pending-verify"
            gap["enrich_run"] = run_id
            gap["enriched_op"] = nu
            gemarkeerd += 1

    gaps_bestand.write_text(
        json.dumps(alle_gaps, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return gemarkeerd


# ─── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--programmaonderdeel",
        required=True,
        help="Programmaonderdeel-code, bv. '1.4' of '4.0'.",
    )
    parser.add_argument(
        "--gaps-bestand",
        default=str(GAPS_FILE.relative_to(ROOT)),
        help="Pad naar gaps.json (relatief aan repo-root).",
    )
    parser.add_argument(
        "--only-prio",
        default=None,
        help="Kommagescheiden prioriteitsfilter, bv. 'hoog,midden'. "
             "Default: alle prioriteiten.",
    )
    parser.add_argument(
        "--markeer-gaps-na-run",
        default=None,
        metavar="INSTRUCTIES_PAD",
        help="Pad naar het instructies-bestand van een eerder gegenereerde run. "
             "Als opgegeven: markeer de bijbehorende gaps als 'enriched-pending-verify' "
             "en stop. Geen nieuwe instructies genereren.",
    )
    parser.add_argument(
        "--droog",
        action="store_true",
        help="Droog uitvoeren: genereer instructies maar schrijf niets weg.",
    )
    args = parser.parse_args()

    programmaonderdeel_id: str = args.programmaonderdeel
    gaps_bestand = ROOT / args.gaps_bestand
    prio_filter: list[str] | None = (
        [p.strip() for p in args.only_prio.split(",")]
        if args.only_prio
        else None
    )

    # Modus: gaps markeren na een eerder gegenereerde run
    if args.markeer_gaps_na_run:
        instructies_pad = Path(args.markeer_gaps_na_run)
        if not instructies_pad.exists():
            print(f"[FOUT] Instructies-bestand niet gevonden: {instructies_pad}", file=sys.stderr)
            sys.exit(1)
        # Extraheer de run-id uit de bestandsnaam
        run_id = instructies_pad.stem.replace("enrich-instructies-", "")
        # Laad de gaps die voor die run golden (alle open gaps op het moment)
        alle_open_gaps = laad_gaps(gaps_bestand, status_filter="open")
        # We markeren alle gaps voor records van dit programmaonderdeel
        # (de subagent heeft die allemaal verwerkt)
        from tools.extractie.verify_records import load_records_for_programmaonderdeel
        records = load_records_for_programmaonderdeel(
            programmaonderdeel_id, "data/concepten/records/*.json"
        )
        record_ids = {r.get("id", "") for r in records}
        relevante_gaps = [g for g in alle_open_gaps if g.get("record_id") in record_ids]
        if prio_filter:
            relevante_gaps = [g for g in relevante_gaps if g.get("prio") in prio_filter]

        if not args.droog:
            gemarkeerd = markeer_gaps_als_enriched(relevante_gaps, gaps_bestand, run_id)
            print(f"[markeer] {gemarkeerd} gaps gemarkeerd als 'enriched-pending-verify'")
        else:
            print(f"[droog] {len(relevante_gaps)} gaps NIET gemarkeerd (--droog actief)")
        return

    run_id = datetime.now(timezone.utc).strftime("enrich-run-%Y%m%dT%H%M%SZ")
    print(f"[enrich] {run_id} — programmaonderdeel {programmaonderdeel_id}")

    # Stap 1: gaps laden en filteren
    print(f"[gaps] laden uit {gaps_bestand.relative_to(ROOT)} ...")
    open_gaps = laad_gaps(gaps_bestand, status_filter="open")
    print(f"  {len(open_gaps)} open gaps totaal")

    # Stap 2: records laden
    from tools.extractie.verify_records import load_records_for_programmaonderdeel
    records = load_records_for_programmaonderdeel(
        programmaonderdeel_id, "data/concepten/records/*.json"
    )
    print(f"[records] {len(records)} records voor programmaonderdeel {programmaonderdeel_id}")

    # Stap 3: gaps per record groeperen
    gaps_per_record = filter_gaps_voor_programmaonderdeel(open_gaps, records, prio_filter)
    print(
        f"[filter] {len(gaps_per_record)} records hebben open gaps "
        f"(prio-filter: {prio_filter or 'alle'})"
    )
    if not gaps_per_record:
        print("  Geen open gaps gevonden voor dit programmaonderdeel — klaar.")
        return

    # Stap 4: per record het record + bundle ophalen
    records_met_gaps: list[dict] = []
    for record_id, gap_entries in sorted(gaps_per_record.items()):
        record = laad_record(record_id)
        if record is None:
            print(
                f"  [WAARSCHUWING] Record '{record_id}' niet gevonden in "
                f"data/concepten/records/ — overgeslagen.",
                file=sys.stderr,
            )
            continue
        bron_bundle = zoek_bron_bundle(record, programmaonderdeel_id)
        records_met_gaps.append({
            "record": record,
            "gap_entries": gap_entries,
            "bron_bundle": bron_bundle,
        })
        prio_telling = {}
        for g in gap_entries:
            prio = g.get("prio", "?")
            prio_telling[prio] = prio_telling.get(prio, 0) + 1
        print(
            f"  {record_id}: {len(gap_entries)} gaps "
            f"({', '.join(f'{v} {k}' for k, v in sorted(prio_telling.items()))}), "
            f"{len(bron_bundle)} bron-chunks"
        )

    # Stap 5: subagent-instructies schrijven
    werkmap = ROOT / "data" / "extractie" / programmaonderdeel_id / "enrich-runs"
    if not args.droog:
        instructies_pad = schrijf_subagent_instructies(
            programmaonderdeel_id=programmaonderdeel_id,
            records_met_gaps=records_met_gaps,
            run_id=run_id,
            werkmap=werkmap,
        )
        print(f"[subagent] instructies geschreven naar {instructies_pad.relative_to(ROOT)}")
        print(
            f"\nVolgende stap: open {instructies_pad.relative_to(ROOT)} "
            f"in een Opus-subagent-sessie om de verrijking uit te voeren.\n"
            f"Na de run: python3 -m tools.extractie.enrich_records "
            f"--programmaonderdeel {programmaonderdeel_id} "
            f"--markeer-gaps-na-run {instructies_pad.relative_to(ROOT)}"
        )
    else:
        print(
            f"[droog] subagent-instructies NIET geschreven (--droog actief). "
            f"{len(records_met_gaps)} records zouden worden verrijkt."
        )

    # Samenvatting
    totaal_gaps = sum(len(r["gap_entries"]) for r in records_met_gaps)
    prio_totaal: dict[str, int] = {}
    for invoer in records_met_gaps:
        for g in invoer["gap_entries"]:
            p = g.get("prio", "?")
            prio_totaal[p] = prio_totaal.get(p, 0) + 1

    print(f"\n[samenvatting]")
    print(f"  Records te verrijken : {len(records_met_gaps)}")
    print(f"  Gaps te verwerken    : {totaal_gaps}")
    for prio_niveau in ["hoog", "midden", "laag"]:
        n = prio_totaal.get(prio_niveau, 0)
        print(f"    {prio_niveau:6s}         : {n}")


if __name__ == "__main__":
    main()
