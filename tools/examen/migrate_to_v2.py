"""Migratie van examen_vragen v1 → v2 met antwoord-behoud (ADR-021 §4).

Per examen:
1. Backup huidige JSON naar data/programma/examen_vragen/_archive/v1/
2. Re-extract via tools.examen.extract_vragen_v2
3. Per v2-vraag: kopieer antwoord- en classificatie-velden van v1-record met
   matchende ID over (ook subvraag-velden waar IDs matchen)
4. Fail-loud bij ID-verlies (--allow-id-loss overrulet)
5. CLI: --examen <id> of --alle, --dry-run

Velden die uit v1 overgenomen worden:
- Antwoorden: correct_antwoord, antwoord_motivering, antwoord_bron,
  antwoord_provenance, antwoord_type, antwoord_confidence, record_gap_report,
  vraagtekst_normalized_at
- Classificatie: vak_code_in_pdf, vak_naam_in_pdf, themas, wets_verwijzingen,
  punten, vraagtype, vraagtype_label_extractie, pdf_pagina

Output: console-rapport per examen (IDs oude/nieuwe set, behouden antwoorden).
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from tools.examen.extract_vragen_v2 import (
    EXAMEN_CONFIGS_V2,
    extract_examen_v2,
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
EXAMEN_DIR = BASE_DIR / "data" / "programma" / "examen_vragen"
BACKUP_DIR = EXAMEN_DIR / "_archive" / "v1"

ANTWOORD_VELDEN = [
    "correct_antwoord",
    "antwoord_motivering",
    "antwoord_bron",
    "antwoord_provenance",
    "antwoord_type",
    "antwoord_confidence",
    "record_gap_report",
    "vraagtekst_normalized_at",
]

CLASSIFICATIE_VELDEN = [
    "vak_code_in_pdf",
    "vak_naam_in_pdf",
    "themas",
    "wets_verwijzingen",
    "punten",
    "vraagtype",
    "vraagtype_label_extractie",
    "pdf_pagina",
]


def lees_v1(examen_id: str) -> Optional[dict]:
    pad = EXAMEN_DIR / f"{examen_id}.json"
    if not pad.exists():
        return None
    return json.loads(pad.read_text(encoding="utf-8"))


def backup_v1(examen_id: str) -> Path:
    src = EXAMEN_DIR / f"{examen_id}.json"
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    dst = BACKUP_DIR / f"{examen_id}.json"
    shutil.copy2(src, dst)
    return dst


def _index_op_id(records: list[dict]) -> dict[str, dict]:
    return {r["id"]: r for r in records if "id" in r}


def _merge_subvragen(v1_sub: list[dict], v2_sub: list[dict]) -> list[dict]:
    """Merge antwoord-velden van v1-subvragen in v2-subvragen op label-match."""
    if not v1_sub:
        return v2_sub
    v1_op_label = {s.get("label"): s for s in v1_sub if s.get("label")}
    merged: list[dict] = []
    for s in v2_sub:
        label = s.get("label")
        result = dict(s)
        if label and label in v1_op_label:
            v1_s = v1_op_label[label]
            for veld in ANTWOORD_VELDEN:
                if veld in v1_s and v1_s[veld] is not None:
                    result[veld] = v1_s[veld]
        merged.append(result)
    return merged


def merge_v1_in_v2(v1_doc: dict, v2_doc: dict) -> tuple[dict, dict]:
    """Kopieer antwoord- en classificatie-velden van v1-vragen in v2-vragen.

    Returns:
        (gemerged-v2-doc, diff-report)
    """
    v1_idx = _index_op_id(v1_doc.get("vragen", []))
    v2_idx = _index_op_id(v2_doc.get("vragen", []))
    v1_ids = set(v1_idx.keys())
    v2_ids = set(v2_idx.keys())

    verloren = sorted(v1_ids - v2_ids)
    nieuw = sorted(v2_ids - v1_ids)
    behouden = sorted(v1_ids & v2_ids)

    antwoord_behouden = 0
    voor_inspectie: list[dict] = []
    for vid in behouden:
        v1_v = v1_idx[vid]
        v2_v = v2_idx[vid]
        # Antwoord-velden overnemen wanneer non-null in v1
        had_antwoord = bool(v1_v.get("correct_antwoord"))
        for veld in ANTWOORD_VELDEN:
            if veld in v1_v and v1_v[veld] is not None:
                v2_v[veld] = v1_v[veld]
        # Classificatie-velden alleen overnemen als v1 een waarde heeft
        # (we vertrouwen v1-vak-toekenning meer dan v2-heuristiek, omdat
        # de classify-stap al gedaan was)
        for veld in CLASSIFICATIE_VELDEN:
            if veld in v1_v and v1_v[veld] not in (None, "", []):
                v2_v[veld] = v1_v[veld]
        # Subvragen-merge (op label)
        if "subvragen" in v1_v and isinstance(v1_v["subvragen"], list):
            v2_v["subvragen"] = _merge_subvragen(v1_v["subvragen"], v2_v.get("subvragen", []))
        # opties soms ge-edit met antwoorden — overnemen als v1 ze had en v2 niet
        if v1_v.get("opties") and not v2_v.get("opties"):
            v2_v["opties"] = v1_v["opties"]
        if had_antwoord and v2_v.get("correct_antwoord"):
            antwoord_behouden += 1
        voor_inspectie.append({"id": vid, "had_antwoord": had_antwoord})

    diff = {
        "v1_n_vragen": len(v1_ids),
        "v2_n_vragen": len(v2_ids),
        "behouden_ids": behouden,
        "nieuwe_ids_in_v2": nieuw,
        "verloren_ids_uit_v1": verloren,
        "antwoorden_behouden": antwoord_behouden,
        "v1_met_antwoord": sum(1 for v in v1_doc.get("vragen", []) if v.get("correct_antwoord")),
    }
    v2_doc["migratie"] = {
        "uitgevoerd_op": datetime.now(timezone.utc).isoformat(),
        "v1_backup": f"data/programma/examen_vragen/_archive/v1/{v1_doc.get('examen_id', '?')}.json",
        "behouden_antwoorden": antwoord_behouden,
    }
    return v2_doc, diff


def migreer_examen(examen_id: str, dry_run: bool, allow_id_loss: bool) -> dict:
    if examen_id not in EXAMEN_CONFIGS_V2:
        raise SystemExit(f"Onbekend examen-id: {examen_id}")
    config = EXAMEN_CONFIGS_V2[examen_id]
    v1 = lees_v1(examen_id)
    if v1 is None:
        print(f"[{examen_id}] WAARSCHUWING: geen v1-JSON gevonden — alleen v2-extract")
        v1 = {"examen_id": examen_id, "vragen": []}

    print(f"[{examen_id}] v2-extract loopt ...")
    v2 = extract_examen_v2(examen_id, config)

    merged, diff = merge_v1_in_v2(v1, v2)

    print(f"  v1 → v2: {diff['v1_n_vragen']} → {diff['v2_n_vragen']} vragen")
    print(f"  behouden IDs: {len(diff['behouden_ids'])}")
    print(f"  nieuwe IDs in v2: {len(diff['nieuwe_ids_in_v2'])}")
    print(f"  verloren IDs uit v1: {len(diff['verloren_ids_uit_v1'])}")
    print(f"  v1 had antwoorden op: {diff['v1_met_antwoord']} vragen")
    print(f"  antwoorden behouden: {diff['antwoorden_behouden']}")

    if diff["verloren_ids_uit_v1"]:
        v1_idx = _index_op_id(v1.get("vragen", []))
        verloren_met_antwoord = [
            vid for vid in diff["verloren_ids_uit_v1"]
            if v1_idx.get(vid, {}).get("correct_antwoord")
        ]
        if verloren_met_antwoord:
            print(f"  ⚠ VERLOREN IDs MET ANTWOORD: {verloren_met_antwoord}")
        if not allow_id_loss:
            print(f"  ID-verlies gedetecteerd — STOP. Gebruik --allow-id-loss om te forceren.")
            print(f"  Verloren IDs (eerste 20): {diff['verloren_ids_uit_v1'][:20]}")
            raise SystemExit(1)

    if dry_run:
        print(f"  [dry-run] niets weggeschreven")
        return diff

    # Backup en schrijven
    backup_pad = backup_v1(examen_id)
    print(f"  backup: {backup_pad.relative_to(BASE_DIR)}")
    out_pad = EXAMEN_DIR / f"{examen_id}.json"
    out_pad.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"  geschreven: {out_pad.relative_to(BASE_DIR)}")
    return diff


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--examen", type=str, help="Migratie voor één examen-id")
    group.add_argument("--alle", action="store_true", help="Migreer alle bekende examens")
    parser.add_argument("--dry-run", action="store_true", help="Niets wegschrijven, alleen diff tonen")
    parser.add_argument("--allow-id-loss", action="store_true",
                        help="Sta vraag-ID-verlies toe (default: fail)")
    args = parser.parse_args(argv)

    if args.alle:
        examens = list(EXAMEN_CONFIGS_V2.keys())
    else:
        examens = [args.examen]

    totaal_behouden = 0
    for ex in examens:
        diff = migreer_examen(ex, args.dry_run, args.allow_id_loss)
        totaal_behouden += diff["antwoorden_behouden"]
    print(f"\nTotaal antwoorden behouden over {len(examens)} examens: {totaal_behouden}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
