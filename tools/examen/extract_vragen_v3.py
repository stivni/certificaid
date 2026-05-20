"""Vragen-extractie v3: typed structured blokken per vraag (ADR-021 v3.0).

BREAKING CHANGE op `vraagtekst_blokken[]`. Bouwt voort op v2: v2 levert
tekst- en tabel-blokken aan per vraag; v3 past pattern-detectoren toe op
de tekst-blokken om sub-blokken te lichten:
- proef_saldibalans, rekeningstaat, inventaris
- marktwaarde, aanpassing, bijlage_verwijzing
- mc_optie, vraag_instructie, casus_context

Plus: top-level vraag-velden `punten`, `vraag_prefix`,
`vraag_header_geextracteerd` worden uit de body gelift.

CLI:
    python3 -m tools.examen.extract_vragen_v3                # alle examens
    python3 -m tools.examen.extract_vragen_v3 --examen 2014-1
    python3 -m tools.examen.extract_vragen_v3 --dry-run     # geen schrijf-actie
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from tools.examen._v3_blok_detectoren import (
    assign_mc_opties_aan_subvragen,
    cleanup_subvraag_whitespace_residue,
    concat_v3_blokken_naar_vraagtekst,
    converteer_1koloms_tabel_naar_mc_opties,
    deduplicate_mc_optie_subvraag,
    detecteer_blokken_voor_subvraag,
    detecteer_typed_blokken,
    lift_top_level_velden,
    splits_blokken_op_gevraagd,
)
from tools.examen.extract_vragen_v2 import (
    EXAMEN_CONFIGS_V2,
    extract_examen_v2,
)

TOOL_ID = "vragen-extractie-v3"
SCHEMA_VERSIE = "3.0"
BASE_DIR = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = BASE_DIR / "data" / "programma" / "examen_vragen"

# Hergebruik v2-configs (zelfde PDFs).
EXAMEN_CONFIGS_V3 = EXAMEN_CONFIGS_V2


# ---------------------------------------------------------------------------
# Per-vraag transformatie v2 → v3
# ---------------------------------------------------------------------------

def transformeer_v2_blokken_naar_v3(
    v2_blokken: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Verzet v2-blokken (tekst/tabel/formule/figuur) naar v3-typed-blokken.

    Per v2-tekst-blok:
    1. Lift top-level velden (alleen op het eerste blok!)
    2. Run detecteer_typed_blokken → list typed v3-blokken

    Per v2-tabel/formule/figuur-blok: 1-op-1 doorgeven.

    Returns:
        (v3-blokken, top-level-velden uit body gelift). top-level-velden
        bevat eventueel 'punten', 'vraag_prefix', 'vraag_header_geextracteerd'.
    """
    v3_blokken: list[dict[str, Any]] = []
    top_velden: dict[str, Any] = {
        "punten": None,
        "vraag_prefix": None,
        "vraag_header_geextracteerd": False,
    }
    eerste_tekst_blok_gezien = False
    for blok in v2_blokken:
        btype = blok.get("type")
        if btype == "tekst":
            tekst = (blok.get("inhoud") or "").strip()
            if not tekst:
                continue
            if not eerste_tekst_blok_gezien:
                # Lift top-level velden uit eerste tekst-blok
                tekst_strip, velden = lift_top_level_velden(tekst)
                if velden.get("vraag_header_geextracteerd"):
                    top_velden.update(velden)
                tekst = tekst_strip
                eerste_tekst_blok_gezien = True
            typed = detecteer_typed_blokken(tekst)
            v3_blokken.extend(typed)
        else:
            # 1-op-1 doorgeven (tabel/formule/figuur)
            v3_blokken.append(blok)
    return v3_blokken, top_velden


def transformeer_vraag(vraag: dict[str, Any]) -> dict[str, Any]:
    """Transformeer één v2-vraag naar v3-vraag."""
    nieuw = dict(vraag)
    v2_blokken = vraag.get("vraagtekst_blokken", []) or []
    v3_blokken, top_velden = transformeer_v2_blokken_naar_v3(v2_blokken)
    # v3.2: post-processors in volgorde:
    #   1. "Gevraagd:" splitten (creëert evt. extra casus_context/instructie)
    #   2. mc_optie ↮ subvraag deduplicatie (verwijdert subvraag-marker-blokken;
    #      moet vóór de tabel→mc conversie zodat die niet weer mc_opties met
    #      a/b/c-labels creëert die meteen weggewist worden)
    #   3. tabel→mc conversie (echte MC-alternatieven uit 1-koloms tabellen)
    v3_blokken = splits_blokken_op_gevraagd(v3_blokken)
    subvragen_vroeg = vraag.get("subvragen") or vraag.get("sub_vragen") or []
    sub_labels_vroeg = [
        s.get("label") for s in subvragen_vroeg if isinstance(s, dict)
    ]
    if sub_labels_vroeg:
        v3_blokken = deduplicate_mc_optie_subvraag(v3_blokken, sub_labels_vroeg)
    v3_blokken = converteer_1koloms_tabel_naar_mc_opties(v3_blokken)
    nieuw["vraagtekst_blokken"] = v3_blokken
    # Top-level velden: alleen overschrijven als detector een waarde gaf,
    # anders bestaande v2-velden bewaren (vooral 'punten' kan al gepopulariseerd
    # zijn via de v2-header-parser).
    if top_velden.get("vraag_prefix") is not None:
        nieuw["vraag_prefix"] = top_velden["vraag_prefix"]
    if top_velden.get("punten") is not None:
        # Alleen overschrijven als v2 geen 'punten' had (None) — anders v2 winnen
        # (v2-header-parser is preciezer voor de "Vraag N / X punten" syntax).
        if nieuw.get("punten") in (None, 0, 0.0):
            nieuw["punten"] = top_velden["punten"]
    # v3.1: vraag_onderwerp
    if top_velden.get("vraag_onderwerp") is not None:
        nieuw["vraag_onderwerp"] = top_velden["vraag_onderwerp"]
    else:
        # Behoud bestaande waarde of zet expliciet null
        nieuw.setdefault("vraag_onderwerp", None)
    nieuw["vraag_header_geextracteerd"] = top_velden.get("vraag_header_geextracteerd", False)

    # v3.2: whitespace-cleanup voor subvraag-residue (dedup is al gebeurd
    # vóór de tabel→mc conversie hierboven).
    subvragen = nieuw.get("subvragen") or nieuw.get("sub_vragen") or []
    sub_labels = [s.get("label") for s in subvragen if isinstance(s, dict)]
    if sub_labels:
        sub_teksten = [
            (s.get("tekst") or "") for s in subvragen if isinstance(s, dict)
        ]
        nieuw["vraagtekst_blokken"], plak_aan = cleanup_subvraag_whitespace_residue(
            nieuw["vraagtekst_blokken"], sub_labels, subvraag_teksten=sub_teksten
        )
        if plak_aan and isinstance(subvragen, list):
            for sv in subvragen:
                if not isinstance(sv, dict):
                    continue
                lbl = (sv.get("label") or "").strip().lower().rstrip(")").rstrip(".")
                if lbl in plak_aan:
                    bestaande = (sv.get("tekst") or "").strip()
                    sv["tekst"] = (bestaande + " " + plak_aan[lbl]).strip()

    # v3.2: subvragen krijgen eigen typed vraagtekst_blokken[]
    for sleutel in ("subvragen", "sub_vragen"):
        sub_list = nieuw.get(sleutel)
        if not isinstance(sub_list, list):
            continue
        for sv in sub_list:
            if not isinstance(sv, dict):
                continue
            sv_tekst = (sv.get("tekst") or "").strip()
            if sv_tekst:
                detected = detecteer_blokken_voor_subvraag(sv_tekst)
                if detected:
                    sv["vraagtekst_blokken"] = detected

    # v3.3: verplaats mc_opties van vraag-niveau naar subvragen op basis van
    # PDF-volgorde-positie (zie ADR-021 v3.3). Werkt enkel wanneer subvragen[]
    # bestaat met lowercase letter-markers (a)/b)/c)/...). Voor 2024-1 herinne-
    # ringsvragen (geen `subvragen[]`, alleen `sub_vragen[]` met A/B/C-labels)
    # is dit een no-op.
    if isinstance(nieuw.get("subvragen"), list) and nieuw["subvragen"]:
        origineel_vraagtekst = vraag.get("vraagtekst") or ""
        if origineel_vraagtekst:
            nieuwe_blokken, per_subvraag = assign_mc_opties_aan_subvragen(
                nieuw["vraagtekst_blokken"],
                nieuw["subvragen"],
                origineel_vraagtekst,
            )
            if per_subvraag:
                nieuw["vraagtekst_blokken"] = nieuwe_blokken
                # Hecht mc_opties in bij elke subvraag
                for sv in nieuw["subvragen"]:
                    if not isinstance(sv, dict):
                        continue
                    lbl_norm = (sv.get("label") or "").strip().lower().rstrip(
                        ")"
                    ).rstrip(".")
                    mc_opties_voor_sv = per_subvraag.get(lbl_norm)
                    if not mc_opties_voor_sv:
                        continue
                    bestaande = sv.get("vraagtekst_blokken") or []
                    sv["vraagtekst_blokken"] = list(bestaande) + mc_opties_voor_sv

    # Reconstrueer vraagtekst (concat van v3-blokken) wanneer geen tabel
    bevat_tabel = any(b.get("type") == "tabel" for b in nieuw["vraagtekst_blokken"])
    if not bevat_tabel:
        nieuw["vraagtekst"] = concat_v3_blokken_naar_vraagtekst(nieuw["vraagtekst_blokken"])
    # Bij tabel laten we vraagtekst zoals v2 hem had (markdown-tabel)
    return nieuw


def transformeer_subvragen(subvragen: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Past dezelfde transformatie toe op subvragen, indien ze blokken hebben.

    Let op: deze functie wordt aangeroepen vóór `transformeer_vraag` de
    subvraag-`tekst` opnieuw door de detector haalt (v3.2). Hier doen we
    alleen het minimum: v2-blokken → v3-blokken transformatie voor subvragen
    die al `vraagtekst_blokken` hebben (legacy 2024-1-pad).
    """
    nieuwe: list[dict[str, Any]] = []
    for sv in subvragen:
        nieuwe_sv = dict(sv)
        v2_blk = sv.get("vraagtekst_blokken")
        if isinstance(v2_blk, list) and v2_blk:
            v3_blk, _ = transformeer_v2_blokken_naar_v3(v2_blk)
            nieuwe_sv["vraagtekst_blokken"] = v3_blk
        nieuwe.append(nieuwe_sv)
    return nieuwe


def extract_examen_v3(examen_id: str, config: dict[str, Any]) -> dict[str, Any]:
    """Run v2 + post-processor om v3-output te krijgen."""
    v2 = extract_examen_v2(examen_id, config)
    nieuwe_vragen = []
    for v in v2.get("vragen", []):
        v3_vraag = transformeer_vraag(v)
        # Subvragen
        if "subvragen" in v3_vraag and isinstance(v3_vraag["subvragen"], list):
            v3_vraag["subvragen"] = transformeer_subvragen(v3_vraag["subvragen"])
        if "sub_vragen" in v3_vraag and isinstance(v3_vraag["sub_vragen"], list):
            v3_vraag["sub_vragen"] = transformeer_subvragen(v3_vraag["sub_vragen"])
        nieuwe_vragen.append(v3_vraag)
    v2["schema_versie"] = SCHEMA_VERSIE
    v2["vragen"] = nieuwe_vragen
    v2["extractie"]["tool"] = TOOL_ID
    v2["extractie"]["extracted_at"] = datetime.now(timezone.utc).isoformat()
    # Statistieken
    type_counts: dict[str, int] = {}
    for v in nieuwe_vragen:
        for b in v.get("vraagtekst_blokken", []):
            t = b.get("type", "?")
            type_counts[t] = type_counts.get(t, 0) + 1
    v2["extractie"]["blok_type_counts"] = type_counts
    return v2


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--examen", type=str, default=None,
                        help="Eén examen-id (bv. 2014-1); default = alle")
    parser.add_argument("--dry-run", action="store_true",
                        help="Schrijf niets weg, print alleen samenvatting")
    args = parser.parse_args(argv)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    examens = (
        [(args.examen, EXAMEN_CONFIGS_V3[args.examen])]
        if args.examen
        else list(EXAMEN_CONFIGS_V3.items())
    )

    for examen_id, config in examens:
        print(f"\n[{examen_id}] v3-extractie ...")
        out = extract_examen_v3(examen_id, config)
        counts = out["extractie"].get("blok_type_counts", {})
        n_vr = out["extractie"]["n_vragen"]
        print(f"  → {n_vr} vragen | blok-types: {counts}")
        if not args.dry_run:
            out_path = OUTPUT_DIR / f"{examen_id}.json"
            with out_path.open("w", encoding="utf-8") as f:
                json.dump(out, f, ensure_ascii=False, indent=2)
            print(f"    geschreven: {out_path.relative_to(BASE_DIR)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
