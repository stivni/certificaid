"""Detecteer examen-vragen met visuele content (tabel, schema, figuur).

Doel: voorkomen dat de antwoord-pipeline blind tekst-only interpreteert.
Visuele vragen vereisen verplichte PNG-Read in de antwoord-agent of een
vision-her-interpretatie vooraf (zie vr8-incident — pijlrichtingen verkeerd
geïnterpreteerd uit OCR-tekst → antwoord volledig fout).

Signalen (in volgorde van zekerheid):
1. `kwaliteits_flags` bevat visuele marker (`tabel_in_pdf_zichtbaar`,
   `schema_in_pdf_zichtbaar`, `figuur_in_pdf_zichtbaar`).
2. `context_blokken[]` bevat een typed blok met visuele aard:
   `tabel`, `groepsschema`, `balans`, `resultatenrekening`,
   `proef_saldibalans`, `rekeningstaat`, `inventaris`, `gegevens_tabel`.
3. Vraagstelling/casus-tekst bevat verwijzing naar visueel element:
   "zie onderstaande tabel", "het schema", "de figuur", "(zie PNG)",
   "in de bijlage", "vul onderstaande tabel aan".

Output:
- `data/programma/examen_vragen/_visuele_vragen.json` — gestructureerde lijst
  per vraag, met `signalen` (welke triggers) en `aanbevolen_actie`.
- Optioneel (`--stamp`): voegt `vision_review_nodig: true` toe aan
  interpretatie-files met signaal.

CLI:
    python3 -m tools.examen.detect_visuele_vragen
    python3 -m tools.examen.detect_visuele_vragen --stamp
    python3 -m tools.examen.detect_visuele_vragen --po 1.4
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
INTERPRETATIES_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_interpretaties"
OUTPUT_PAD = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_visuele_vragen.json"

# Visuele kwaliteits_flags
VISUELE_FLAGS = {
    "tabel_in_pdf_zichtbaar",
    "schema_in_pdf_zichtbaar",
    "figuur_in_pdf_zichtbaar",
    "diagram_in_pdf_zichtbaar",
}

# Visuele context-blok-types
VISUELE_BLOK_TYPES = {
    "tabel",
    "groepsschema",
    "balans",
    "resultatenrekening",
    "proef_saldibalans",
    "rekeningstaat",
    "inventaris",
    "gegevens_tabel",
}

# Regex-patronen voor tekstuele verwijzingen naar visuele elementen.
# Case-insensitive. Word-boundaries waar zinvol.
_TEKST_PATRONEN: list[tuple[str, re.Pattern[str]]] = [
    ("zie_png_marker",       re.compile(r"\(zie\s+(schema|tabel|figuur|bijlage)\s+in\s+(de\s+)?png\)", re.I)),
    ("zie_onderstaande",     re.compile(r"\bzie\s+onderstaand(e)?\s+(tabel|schema|figuur|grafiek)", re.I)),
    ("vul_tabel_aan",        re.compile(r"\bvul\s+(de\s+|onderstaand(e)?\s+)?tabel\s+(aan|in)", re.I)),
    ("vul_in_schema",        re.compile(r"\bvul\s+(de\s+|onderstaand(e)?\s+)?(schema|matrix)\s+(aan|in)", re.I)),
    ("kruis_aan",            re.compile(r"\bkruis\s+(de\s+|het\s+)?(juiste|onjuiste|correct(e)?|fout(ieve)?)\s+\w+\s+aan", re.I)),
    ("zie_bijlage",          re.compile(r"\bzie\s+(de\s+)?bijlage", re.I)),
    ("op_basis_van_de_bal",  re.compile(r"\bop\s+basis\s+van\s+(de\s+)?(balans|resultatenrekening|jaarrekening)", re.I)),
    ("onderstaand_schema",   re.compile(r"\bonderstaand(e)?\s+(schema|figuur|grafiek)", re.I)),
    ("het_schema_de_fig",    re.compile(r"\b(het\s+volgend(e)?\s+|de\s+volgend(e)?\s+|in\s+(het|onderstaand(e)?)\s+)(schema|figuur|grafiek|tabel)", re.I)),
]


def _laad_interpretatie(pad: Path) -> dict[str, Any] | None:
    try:
        return json.loads(pad.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"WARN: kon {pad} niet lezen: {exc}", file=sys.stderr)
        return None


def _signalen_voor_vraag(interp: dict[str, Any]) -> list[dict[str, Any]]:
    """Vind alle visuele-signalen voor één interpretatie."""
    signalen: list[dict[str, Any]] = []

    # 1. kwaliteits_flags
    for vlag in interp.get("kwaliteits_flags") or []:
        if vlag in VISUELE_FLAGS:
            signalen.append({"type": "kwaliteits_flag", "waarde": vlag})

    # 2. Visueel typed context-blok
    for blok in interp.get("context_blokken") or []:
        bt = blok.get("type")
        if bt in VISUELE_BLOK_TYPES:
            signalen.append({"type": "context_blok", "waarde": bt})

    # 3. Tekstuele patronen in casus_context en vraagstellingen
    teksten: list[tuple[str, str]] = []
    for blok in interp.get("context_blokken") or []:
        if blok.get("tekst"):
            teksten.append(("casus_context", blok["tekst"]))
    for v in interp.get("vragen") or []:
        if v.get("vraagstelling"):
            teksten.append((f"vraagstelling-{v.get('id', '?')}", v["vraagstelling"]))

    for veld, tekst in teksten:
        for patroon_naam, patroon in _TEKST_PATRONEN:
            if patroon.search(tekst):
                signalen.append({
                    "type": "tekst_patroon",
                    "patroon": patroon_naam,
                    "veld": veld,
                })

    return signalen


def _aanbevolen_actie(signalen: list[dict[str, Any]]) -> str:
    """Bepaal aanbevolen actie op basis van signaal-sterkte."""
    if not signalen:
        return "geen"
    sterk = any(s["type"] in {"kwaliteits_flag", "context_blok"} for s in signalen)
    if sterk:
        return "vision_review_aanbevolen"
    # Alleen tekst-patronen → minder zeker; PNG-Read in antwoord-pas volstaat
    return "png_read_in_antwoord_pas"


def detect_all(po_filter: str | None = None) -> dict[str, Any]:
    resultaten: list[dict[str, Any]] = []
    n_totaal = 0
    n_signaal = 0
    n_sterk = 0
    n_zwak = 0

    for examen_dir in sorted(INTERPRETATIES_DIR.iterdir()):
        if not examen_dir.is_dir():
            continue
        for pad in sorted(examen_dir.glob("*.json")):
            data = _laad_interpretatie(pad)
            if data is None:
                continue
            n_totaal += 1
            if po_filter:
                if po_filter not in (data.get("programmaonderdeel_ids") or []):
                    continue
            signalen = _signalen_voor_vraag(data)
            if not signalen:
                continue
            actie = _aanbevolen_actie(signalen)
            n_signaal += 1
            if actie == "vision_review_aanbevolen":
                n_sterk += 1
            elif actie == "png_read_in_antwoord_pas":
                n_zwak += 1
            resultaten.append({
                "examen_id": data.get("examen_id", examen_dir.name),
                "vraag_id": data.get("vraag_id", pad.stem),
                "vraag_onderwerp": data.get("vraag_onderwerp") or "",
                "programmaonderdeel_ids": data.get("programmaonderdeel_ids") or [],
                "vraag_pad": str(pad.relative_to(REPO_ROOT)),
                "signalen": signalen,
                "aanbevolen_actie": actie,
            })

    # Sorteer: sterk eerst, dan PO-volgorde
    resultaten.sort(key=lambda r: (
        0 if r["aanbevolen_actie"] == "vision_review_aanbevolen" else 1,
        r["programmaonderdeel_ids"][0] if r["programmaonderdeel_ids"] else "",
        r["vraag_id"],
    ))

    return {
        "schema_versie": "1.0",
        "gegenereerd_op": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "po_filter": po_filter,
        "n_totaal_vragen_gescand": n_totaal,
        "n_met_signaal": n_signaal,
        "n_sterk_signaal": n_sterk,
        "n_zwak_signaal": n_zwak,
        "vragen": resultaten,
    }


def stamp_interpretaties(rapport: dict[str, Any]) -> int:
    """Voeg `vision_review_nodig`-veld toe aan interpretaties met sterk signaal.

    Veld-waarde: dict met `actie` + `signalen`.
    Returns: aantal effectieve writes.
    """
    n_stamps = 0
    for item in rapport["vragen"]:
        if item["aanbevolen_actie"] != "vision_review_aanbevolen":
            continue
        pad = REPO_ROOT / item["vraag_pad"]
        data = _laad_interpretatie(pad)
        if data is None:
            continue
        nieuwe = {
            "actie": item["aanbevolen_actie"],
            "signalen": item["signalen"],
        }
        if data.get("vision_review_nodig") == nieuwe:
            continue  # idempotent
        data["vision_review_nodig"] = nieuwe
        pad.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        n_stamps += 1
    return n_stamps


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--po", help="Filter op één PO (bv. 1.4).")
    parser.add_argument(
        "--stamp",
        action="store_true",
        help="Voeg vision_review_nodig-veld toe aan interpretaties met sterk signaal.",
    )
    args = parser.parse_args(argv)

    rapport = detect_all(po_filter=args.po)
    OUTPUT_PAD.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PAD.write_text(
        json.dumps(rapport, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"[detect] {rapport['n_totaal_vragen_gescand']} vragen gescand")
    print(f"[detect] {rapport['n_met_signaal']} met visueel signaal")
    print(f"  - {rapport['n_sterk_signaal']} sterk (vision_review_aanbevolen)")
    print(f"  - {rapport['n_zwak_signaal']} zwak (png_read_in_antwoord_pas)")
    print(f"[detect] rapport → {OUTPUT_PAD.relative_to(REPO_ROOT)}")

    if args.stamp:
        n = stamp_interpretaties(rapport)
        print(f"[detect] {n} interpretaties gestempeld met vision_review_nodig")

    return 0


if __name__ == "__main__":
    sys.exit(main())
