"""Staleness-detectie voor Certificaid-artefacten.

Twee modi:

  MODUS 1 — Bron-MD's (default):
    Vergelijkt de opgeslagen input-hashes van bron-MD's (YAML frontmatter) met
    de huidige bestanden op schijf. Werkt op bestaande `provenance.inputs[].sha256`.

    Gebruik:
      python tools/etl/mark_stale.py resources/bronnen/wetteksten/
      python tools/etl/mark_stale.py resources/bronnen/wetteksten/Antiwitwaswet-2017.md
      python tools/etl/mark_stale.py resources/bronnen/ --dry-run

  MODUS 2 — Concept-records (--concepts):
    Walkt alle concept-records in data/concepten/records/**/*.json.
    Per veld met inline _provenance vergelijkt het de opgeslagen `sha256` van elke
    chunk-input met de live `chunk_sha` in ChromaDB.

    Bij mismatch → veld wordt `stale: true` gemarkeerd (alleen met --apply).
    Default = dry-run: rapport zonder aanpassingen.

    Gebruik:
      python tools/etl/mark_stale.py --concepts
      python tools/etl/mark_stale.py --concepts --chroma-path data/rag/4.0
      python tools/etl/mark_stale.py --concepts --apply

    Edge-cases:
      - chunk_sha ontbreekt in record (sha_unknown): veld wordt apart gerapporteerd,
        niet als gewone stale gemarkeerd. Teken dat extractor sha niet heeft ingevuld.
      - chunk verdwenen uit ChromaDB (chunk_missing): veld wordt stale met reden
        "chunk_missing:<chunk_id>".
      - veld zonder _provenance: overgeslagen (niet alles is bron-gestuurd,
        zie ADR-008 §11).

Schema en rationale: docs/adr/ADR-004-provenance.md, ADR-007, ADR-008 §10.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

CONCEPT_RECORDS_DIR = ROOT / "data" / "concepten" / "records"
CHROMA_PATH_DEFAULT = ROOT / "data" / "rag" / "main"

from tools.lib.provenance import (  # noqa: E402
    Input,
    detect_stale,
    hash_file,
    mark_field_stale,
    now_iso,
    read_provenance,
    sha_voor_chunk,
    walk_concept_provenance,
    write_provenance,
)


# ─── Modus 1: bron-MD's ──────────────────────────────────────────────────────

def _check_bron(md_pad: Path, *, dry_run: bool = False) -> tuple[str, str]:
    """Returns (status, detail).

    status ∈ {fresh, stale-already, became-stale, recovered, no-provenance,
              no-inputs-declared, missing-input}
    """
    prov = read_provenance(md_pad)
    if prov is None:
        return "no-provenance", ""

    if not prov.inputs:
        # No inputs declared — nothing to compare. Leave state untouched.
        return ("stale-already" if prov.stale else "no-inputs-declared"), (
            prov.stale_reason or "no inputs in provenance"
        )

    current_inputs: list[Input] = []
    for recorded in prov.inputs:
        if recorded.sha256 is None:
            # URL-sourced; no local file to hash, carry forward unchanged
            current_inputs.append(recorded)
            continue
        input_path = ROOT / recorded.id
        if not input_path.exists():
            return "missing-input", recorded.id
        current_inputs.append(
            Input(id=recorded.id, sha256=hash_file(input_path), version=recorded.version)
        )

    is_stale, reason = detect_stale(prov, current_inputs)

    if not is_stale:
        if prov.stale:
            if not dry_run:
                prov.stale = False
                prov.stale_reason = None
                write_provenance(md_pad, prov)
            return "recovered", "inputs match recorded hashes again"
        return "fresh", ""

    if prov.stale:
        return "stale-already", prov.stale_reason or reason or ""

    if not dry_run:
        prov.stale = True
        prov.stale_reason = reason
        write_provenance(md_pad, prov)
    return "became-stale", reason or ""


def _scan_bronnen(paden: list[str], dry_run: bool) -> None:
    targets: list[Path] = []
    for p in paden:
        path = Path(p)
        if path.is_dir():
            md = sorted(path.rglob("*.md"))
            jsn = sorted(path.rglob("*.json"))
            targets.extend(md + jsn)
        elif path.is_file():
            targets.append(path)
        else:
            print(f"warning: {p} not found", file=sys.stderr)

    counts: dict[str, int] = {}
    interesting = {"became-stale", "recovered", "missing-input"}
    for t in targets:
        status, detail = _check_bron(t, dry_run=dry_run)
        counts[status] = counts.get(status, 0) + 1
        if status in interesting:
            print(f"  {status:18s}  {t}  ({detail})")

    print(f"\nScanned {len(targets)} files{' (dry-run)' if dry_run else ''}:")
    for status, n in sorted(counts.items()):
        print(f"  {status:18s}  {n}")


# ─── Modus 2: concept-records ────────────────────────────────────────────────

@dataclass
class VeldResultaat:
    """Uitkomst van staleness-check op één veld van één concept-record."""
    record_pad: str
    concept_naam: str
    veldpad: str
    chunk_id: str
    opgeslagen_sha: str | None
    live_sha: str | None
    status: str  # fresh | stale | chunk_missing | sha_unknown | al_stale

    def is_interessant(self) -> bool:
        return self.status != "fresh"

    def samenvatting(self) -> str:
        return (
            f"  {self.status:14s}  {self.record_pad}  [{self.veldpad}]"
            f"  chunk={self.chunk_id}"
            + (f"  opgeslagen={self.opgeslagen_sha}  live={self.live_sha}"
               if self.status == "stale" else "")
        )


def _open_chroma_collectie(chroma_pad: Path):
    """Open ChromaDB bronnen-collection; geeft None terug als niet beschikbaar."""
    try:
        import chromadb  # type: ignore  # optionele dependency
        client = chromadb.PersistentClient(path=str(chroma_pad))
        return client.get_collection("bronnen")
    except Exception as exc:
        print(f"[warn] ChromaDB niet beschikbaar op {chroma_pad}: {exc}", file=sys.stderr)
        return None


def _check_concept_veld(
    veldpad: str,
    prov_blok: dict,
    collectie,
) -> list[VeldResultaat]:
    """Controleer alle chunk-inputs van één veld. Eén resultaat per input-chunk."""
    resultaten: list[VeldResultaat] = []
    for inp in prov_blok.get("inputs", []):
        chunk_id = inp.get("id", "")
        opgeslagen_sha = inp.get("sha256")
        al_stale = prov_blok.get("stale", False)

        if al_stale:
            resultaten.append(VeldResultaat(
                record_pad="", concept_naam="", veldpad=veldpad,
                chunk_id=chunk_id, opgeslagen_sha=opgeslagen_sha,
                live_sha=None, status="al_stale",
            ))
            continue

        if opgeslagen_sha is None:
            # Extractor heeft sha niet ingevuld — structureel probleem, niet gewone stale
            resultaten.append(VeldResultaat(
                record_pad="", concept_naam="", veldpad=veldpad,
                chunk_id=chunk_id, opgeslagen_sha=None,
                live_sha=None, status="sha_unknown",
            ))
            continue

        if collectie is None:
            # ChromaDB niet beschikbaar — kan niet vergelijken
            resultaten.append(VeldResultaat(
                record_pad="", concept_naam="", veldpad=veldpad,
                chunk_id=chunk_id, opgeslagen_sha=opgeslagen_sha,
                live_sha=None, status="sha_unknown",
            ))
            continue

        live_sha = sha_voor_chunk(chunk_id, collectie)

        if live_sha is None:
            resultaten.append(VeldResultaat(
                record_pad="", concept_naam="", veldpad=veldpad,
                chunk_id=chunk_id, opgeslagen_sha=opgeslagen_sha,
                live_sha=None, status="chunk_missing",
            ))
        elif live_sha != opgeslagen_sha:
            resultaten.append(VeldResultaat(
                record_pad="", concept_naam="", veldpad=veldpad,
                chunk_id=chunk_id, opgeslagen_sha=opgeslagen_sha,
                live_sha=live_sha, status="stale",
            ))
        else:
            resultaten.append(VeldResultaat(
                record_pad="", concept_naam="", veldpad=veldpad,
                chunk_id=chunk_id, opgeslagen_sha=opgeslagen_sha,
                live_sha=live_sha, status="fresh",
            ))

    return resultaten


def _scan_concepten(
    chroma_pad: Path,
    apply: bool,
) -> None:
    """Scan alle concept-records; rapporteer stale velden; markeer bij --apply."""
    dry_run = not apply
    collectie = _open_chroma_collectie(chroma_pad)

    if not CONCEPT_RECORDS_DIR.exists():
        print(f"[warn] {CONCEPT_RECORDS_DIR} bestaat niet — geen concept-records om te scannen.")
        return

    record_paden = sorted(CONCEPT_RECORDS_DIR.rglob("*.json"))
    records_zonder_prov = 0
    records_met_stale_velden = 0
    totaal_velden_gecheckt = 0

    # Tellingen per status
    tellingen: dict[str, int] = {}

    print(f"[scan] {len(record_paden)} concept-records in {CONCEPT_RECORDS_DIR.relative_to(ROOT)}")
    if dry_run:
        print("[modus] dry-run — geen wijzigingen (gebruik --apply om te schrijven)\n")
    else:
        print("[modus] apply — stale velden worden bijgewerkt\n")

    for record_pad in record_paden:
        try:
            record = json.loads(record_pad.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"[skip] {record_pad.name}: JSON-fout: {exc}", file=sys.stderr)
            continue

        # Basischeck: is dit een concept-record?
        if "naam" not in record or "node_type" not in record:
            continue

        concept_naam = record.get("naam", "?")
        record_rel = str(record_pad.relative_to(ROOT))

        veld_resultaten: list[VeldResultaat] = []
        for veldpad, prov_blok in walk_concept_provenance(record):
            resultaten = _check_concept_veld(veldpad, prov_blok, collectie)
            for r in resultaten:
                r.record_pad = record_rel
                r.concept_naam = concept_naam
            veld_resultaten.extend(resultaten)
            totaal_velden_gecheckt += 1

        if not veld_resultaten:
            records_zonder_prov += 1

        # Verzamel per-status
        stale_velden_in_record: list[str] = []
        for r in veld_resultaten:
            tellingen[r.status] = tellingen.get(r.status, 0) + 1
            if r.is_interessant():
                print(r.samenvatting())

            # Bepaal stale-reden voor mark_field_stale
            if not apply:
                continue
            if r.status == "stale":
                reden = f"chunk_sha_changed:{r.chunk_id}"
                gelukt = mark_field_stale(record, r.veldpad, reden)
                if gelukt:
                    stale_velden_in_record.append(r.veldpad)
            elif r.status == "chunk_missing":
                reden = f"chunk_missing:{r.chunk_id}"
                gelukt = mark_field_stale(record, r.veldpad, reden)
                if gelukt:
                    stale_velden_in_record.append(r.veldpad)

        # Schrijf record terug als er velden bijgewerkt zijn
        if apply and stale_velden_in_record:
            record_pad.write_text(
                json.dumps(record, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            records_met_stale_velden += 1
            print(
                f"  [geschreven] {record_rel}  ({len(stale_velden_in_record)} veld(en) bijgewerkt)"
            )

    # Samenvatting
    print(f"\n{'═' * 60}")
    print(f"Totaal gescande records : {len(record_paden)}")
    print(f"Records zonder provenance: {records_zonder_prov}")
    print(f"Veld-checks uitgevoerd  : {totaal_velden_gecheckt}")
    print()
    print("Status per veld-check:")
    for status, aantal in sorted(tellingen.items()):
        print(f"  {status:14s}  {aantal}")

    if apply and records_met_stale_velden:
        print(f"\n[apply] {records_met_stale_velden} record(s) bijgewerkt met stale-vlaggen.")
    elif dry_run and (tellingen.get("stale", 0) + tellingen.get("chunk_missing", 0)) > 0:
        n_te_markeren = tellingen.get("stale", 0) + tellingen.get("chunk_missing", 0)
        print(f"\n[dry-run] {n_te_markeren} veld-chunk(s) zouden stale gemarkeerd worden.")
        print("          Gebruik --apply om daadwerkelijk te schrijven.")

    if tellingen.get("sha_unknown", 0) > 0:
        print(
            f"\n[let op] {tellingen['sha_unknown']} veld-chunk(s) hebben sha_unknown —"
            " de extractor heeft chunk_sha niet ingevuld."
            " Staleness-detectie is voor deze velden niet mogelijk."
            " Zie ADR-008 §'Open implementatie-eisen'."
        )


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Modus 1: bron-MD's (positional paths, backwards-compatible)
    ap.add_argument(
        "paden",
        nargs="*",
        metavar="PAD",
        help="MD-bestanden of directories met bron-MD's (Modus 1)",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Rapport only; geen wijzigingen (Modus 1)",
    )

    # Modus 2: concept-records
    ap.add_argument(
        "--concepts",
        action="store_true",
        help="Scan concept-records op stale chunk-inputs (Modus 2)",
    )
    ap.add_argument(
        "--chroma-path",
        default=None,
        metavar="PAD",
        help=(
            "Override ChromaDB-pad (Modus 2). "
            f"Default: {CHROMA_PATH_DEFAULT.relative_to(ROOT)}"
        ),
    )
    ap.add_argument(
        "--apply",
        action="store_true",
        help="Schrijf stale-vlaggen naar concept-records (Modus 2; default = dry-run)",
    )

    args = ap.parse_args()

    if args.concepts:
        # Modus 2
        if args.chroma_path:
            chroma_pad = Path(args.chroma_path)
            if not chroma_pad.is_absolute():
                chroma_pad = ROOT / chroma_pad
        else:
            chroma_pad = CHROMA_PATH_DEFAULT
        _scan_concepten(chroma_pad, apply=args.apply)
    else:
        # Modus 1 (backwards-compatible)
        if not args.paden:
            ap.error(
                "Geef bestanden/directories op (Modus 1) of gebruik --concepts (Modus 2)."
            )
        _scan_bronnen(args.paden, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
