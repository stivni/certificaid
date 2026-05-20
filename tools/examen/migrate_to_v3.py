"""Migratie van examen_vragen v2 → v3 met antwoord-behoud (ADR-021 v3.0).

Per examen:
1. Backup huidige v2-JSON naar data/programma/examen_vragen/_archive/v2/
2. Re-extract via tools.examen.extract_vragen_v3 (v2-pipeline + post-processor)
3. Per v3-vraag: kopieer antwoord-, classificatie- en 2024-1-velden van
   v2-record met matchende ID over (ook subvraag-velden waar IDs/labels matchen)
4. Fail-loud bij ID-verlies (--allow-id-loss overrulet)
5. CLI: --examen <id> of --alle, --dry-run

Behouden v2-velden (mag niet verloren bij v2 → v3):
- Antwoorden: correct_antwoord, antwoord_motivering, antwoord_bron,
  antwoord_provenance, antwoord_type, antwoord_confidence, record_gap_report,
  vraagtekst_normalized_at
- Classificatie: vak_code_in_pdf, vak_naam_in_pdf, themas, wets_verwijzingen,
  punten, vraagtype, vraagtype_label_extractie, pdf_pagina
- 2024-1-specifiek (ADR-022): vraag_herkomst, vraag_volledigheid,
  vraag_herinterpreteerd, mc_opties_gestructureerd, antwoord_hint_in_vraag
- Sub-vragen genest: alle bovenstaande velden in subvragen[]/sub_vragen[]
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from tools.examen.extract_vragen_v3 import (
    EXAMEN_CONFIGS_V3,
    extract_examen_v3,
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
EXAMEN_DIR = BASE_DIR / "data" / "programma" / "examen_vragen"
BACKUP_DIR = EXAMEN_DIR / "_archive" / "v2"

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

# 2024-1-specifieke velden (ADR-022) — moeten ook bewaard
ADR022_VELDEN = [
    "vraag_herkomst",
    "vraag_volledigheid",
    "vraag_herinterpreteerd",
    "mc_opties_gestructureerd",
    "antwoord_hint_in_vraag",
]

# ADR-023 / v3.1: typed antwoord-blokken — moeten over migratie bewaard
ADR023_VELDEN = [
    "correct_antwoord_blokken",
]

ALLE_BEHOUDEN = ANTWOORD_VELDEN + CLASSIFICATIE_VELDEN + ADR022_VELDEN + ADR023_VELDEN


def lees_v2(examen_id: str) -> Optional[dict]:
    pad = EXAMEN_DIR / f"{examen_id}.json"
    if not pad.exists():
        return None
    return json.loads(pad.read_text(encoding="utf-8"))


def backup_v2(examen_id: str) -> Path:
    src = EXAMEN_DIR / f"{examen_id}.json"
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    dst = BACKUP_DIR / f"{examen_id}.json"
    shutil.copy2(src, dst)
    return dst


def _index_op_id(records: list[dict]) -> dict[str, dict]:
    return {r["id"]: r for r in records if "id" in r}


def _merge_subvragen(v2_sub: list[dict], v3_sub: list[dict]) -> list[dict]:
    """Merge antwoord-velden van v2-subvragen in v3-subvragen op label-match."""
    if not v2_sub:
        return v3_sub
    v2_op_label = {s.get("label"): s for s in v2_sub if s.get("label")}
    v2_op_id = {s.get("id"): s for s in v2_sub if s.get("id")}
    merged: list[dict] = []
    for s in v3_sub:
        result = dict(s)
        # Match op id of label
        v2_s = None
        if s.get("id") and s["id"] in v2_op_id:
            v2_s = v2_op_id[s["id"]]
        elif s.get("label") and s["label"] in v2_op_label:
            v2_s = v2_op_label[s["label"]]
        if v2_s is not None:
            for veld in ALLE_BEHOUDEN:
                if veld in v2_s and v2_s[veld] is not None:
                    result[veld] = v2_s[veld]
        merged.append(result)
    return merged


def merge_v2_in_v3(v2_doc: dict, v3_doc: dict) -> tuple[dict, dict]:
    """Kopieer antwoord- en classificatie-velden van v2-vragen in v3-vragen.

    Returns:
        (gemerged-v3-doc, diff-report)
    """
    v2_idx = _index_op_id(v2_doc.get("vragen", []))
    v3_idx = _index_op_id(v3_doc.get("vragen", []))
    v2_ids = set(v2_idx.keys())
    v3_ids = set(v3_idx.keys())

    verloren = sorted(v2_ids - v3_ids)
    nieuw = sorted(v3_ids - v2_ids)
    behouden = sorted(v2_ids & v3_ids)

    antwoord_behouden = 0
    gap_reports_behouden = 0
    adr022_behouden = 0
    for vid in behouden:
        v2_v = v2_idx[vid]
        v3_v = v3_idx[vid]
        had_antwoord = bool(v2_v.get("correct_antwoord"))
        had_gap_report = bool(v2_v.get("record_gap_report"))
        had_adr022 = any(v2_v.get(k) is not None for k in ADR022_VELDEN)
        for veld in ALLE_BEHOUDEN:
            if veld in v2_v and v2_v[veld] is not None:
                v3_v[veld] = v2_v[veld]
        # Subvragen-merge (op label of id)
        for sleutel in ("subvragen", "sub_vragen"):
            if sleutel in v2_v and isinstance(v2_v[sleutel], list):
                v3_v[sleutel] = _merge_subvragen(v2_v[sleutel], v3_v.get(sleutel, []))
        # Opties (legacy) — overnemen als v2 ze had en v3 niet
        if v2_v.get("opties") and not v3_v.get("opties"):
            v3_v["opties"] = v2_v["opties"]
        if had_antwoord and v3_v.get("correct_antwoord"):
            antwoord_behouden += 1
        if had_gap_report and v3_v.get("record_gap_report"):
            gap_reports_behouden += 1
        if had_adr022 and any(v3_v.get(k) is not None for k in ADR022_VELDEN):
            adr022_behouden += 1

    diff = {
        "v2_n_vragen": len(v2_ids),
        "v3_n_vragen": len(v3_ids),
        "behouden_ids": behouden,
        "nieuwe_ids_in_v3": nieuw,
        "verloren_ids_uit_v2": verloren,
        "antwoorden_behouden": antwoord_behouden,
        "v2_met_antwoord": sum(1 for v in v2_doc.get("vragen", []) if v.get("correct_antwoord")),
        "gap_reports_behouden": gap_reports_behouden,
        "v2_met_gap_report": sum(1 for v in v2_doc.get("vragen", []) if v.get("record_gap_report")),
        "adr022_behouden": adr022_behouden,
        "v2_met_adr022": sum(
            1 for v in v2_doc.get("vragen", [])
            if any(v.get(k) is not None for k in ADR022_VELDEN)
        ),
    }
    v3_doc["migratie"] = {
        "uitgevoerd_op": datetime.now(timezone.utc).isoformat(),
        "v2_backup": f"data/programma/examen_vragen/_archive/v2/{v2_doc.get('examen_id', '?')}.json",
        "behouden_antwoorden": antwoord_behouden,
        "behouden_gap_reports": gap_reports_behouden,
        "behouden_adr022_velden": adr022_behouden,
    }
    return v3_doc, diff


def migreer_examen(examen_id: str, dry_run: bool, allow_id_loss: bool) -> dict:
    if examen_id not in EXAMEN_CONFIGS_V3:
        raise SystemExit(f"Onbekend examen-id: {examen_id}")
    config = EXAMEN_CONFIGS_V3[examen_id]
    v2 = lees_v2(examen_id)
    if v2 is None:
        print(f"[{examen_id}] WAARSCHUWING: geen v2-JSON gevonden — alleen v3-extract")
        v2 = {"examen_id": examen_id, "vragen": []}

    print(f"[{examen_id}] v3-extract loopt ...")
    v3 = extract_examen_v3(examen_id, config)

    merged, diff = merge_v2_in_v3(v2, v3)

    print(f"  v2 → v3: {diff['v2_n_vragen']} → {diff['v3_n_vragen']} vragen")
    print(f"  behouden IDs: {len(diff['behouden_ids'])}")
    print(f"  nieuwe IDs in v3: {len(diff['nieuwe_ids_in_v3'])}")
    print(f"  verloren IDs uit v2: {len(diff['verloren_ids_uit_v2'])}")
    print(f"  v2 had antwoorden op: {diff['v2_met_antwoord']} | behouden: {diff['antwoorden_behouden']}")
    print(f"  v2 had gap-reports op: {diff['v2_met_gap_report']} | behouden: {diff['gap_reports_behouden']}")
    print(f"  v2 had ADR-022-velden op: {diff['v2_met_adr022']} | behouden: {diff['adr022_behouden']}")

    if diff["verloren_ids_uit_v2"]:
        v2_idx = _index_op_id(v2.get("vragen", []))
        verloren_met_antwoord = [
            vid for vid in diff["verloren_ids_uit_v2"]
            if v2_idx.get(vid, {}).get("correct_antwoord")
        ]
        if verloren_met_antwoord:
            print(f"  ⚠ VERLOREN IDs MET ANTWOORD: {verloren_met_antwoord}")
        if not allow_id_loss:
            print(f"  ID-verlies gedetecteerd — STOP. Gebruik --allow-id-loss om te forceren.")
            print(f"  Verloren IDs (eerste 20): {diff['verloren_ids_uit_v2'][:20]}")
            raise SystemExit(1)

    # Fail-loud bij antwoord-verlies
    if diff["antwoorden_behouden"] < diff["v2_met_antwoord"]:
        verschil = diff["v2_met_antwoord"] - diff["antwoorden_behouden"]
        print(f"  ⚠ ANTWOORD-VERLIES: {verschil} antwoord(en) niet doorgekomen")
        if not allow_id_loss:
            raise SystemExit(1)

    if dry_run:
        print(f"  [dry-run] niets weggeschreven")
        return diff

    # Backup en schrijven
    backup_pad = backup_v2(examen_id)
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
                        help="Sta vraag-ID-verlies en antwoord-verlies toe (default: fail)")
    args = parser.parse_args(argv)

    if args.alle:
        examens = list(EXAMEN_CONFIGS_V3.keys())
    else:
        examens = [args.examen]

    totaal_antw = 0
    totaal_gap = 0
    totaal_adr022 = 0
    for ex in examens:
        diff = migreer_examen(ex, args.dry_run, args.allow_id_loss)
        totaal_antw += diff["antwoorden_behouden"]
        totaal_gap += diff["gap_reports_behouden"]
        totaal_adr022 += diff["adr022_behouden"]
    print(f"\nTotaal antwoorden behouden over {len(examens)} examens: {totaal_antw}")
    print(f"Totaal gap-reports behouden over {len(examens)} examens: {totaal_gap}")
    print(f"Totaal ADR-022-velden behouden over {len(examens)} examens: {totaal_adr022}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
