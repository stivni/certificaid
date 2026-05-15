"""
Semantische classificatie van examenvragen naar programmaonderdelen (ADR-008 §13 E).

Leest alle examenvragen uit data/programma/examen_vragen/*.json (niet de -labels.json bestanden),
leest PO-titels uit data/programma/anchors.json, en schrijft instructies + payload voor een
Sonnet-subagent die de classificatie uitvoert.

De subagent produceert data/programma/examen_vragen/_programmaonderdeel_classificatie.json.

Huidig seed-bestand (PO 1.4, handmatig geclassificeerd op basis van consolidatie-keywords):
  Zie --seed-po-14 vlag — vult een seed in voor 9 vragen die duidelijk PO 1.4 raken.

Gebruik:
  python3 -m tools.examen.classify_vragen_naar_programmaonderdelen
  python3 -m tools.examen.classify_vragen_naar_programmaonderdelen --seed-po-14
  python3 -m tools.examen.classify_vragen_naar_programmaonderdelen --droog

Vervolgstap (full classificatie):
  1. Bekijk de gegenereerde subagent-instructies in
     data/programma/examen_vragen/_classificatie-instructies.md
  2. Lanceer een Sonnet-subagent met die instructies.
  3. De subagent schrijft data/programma/examen_vragen/_programmaonderdeel_classificatie.json
  4. verify_records.py laadt automatisch de juiste vragen via
     laad_examen_vragen_voor_programmaonderdeel().
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
EXAMEN_VRAGEN_DIR = ROOT / "data" / "examen_vragen"
ANCHORS_FILE = ROOT / "data" / "anchors.json"
CLASSIFICATIE_BESTAND = EXAMEN_VRAGEN_DIR / "_programmaonderdeel_classificatie.json"
INSTRUCTIES_BESTAND = EXAMEN_VRAGEN_DIR / "_classificatie-instructies.md"

# Handmatige seed voor PO 1.4 — geselecteerd op consolidatie-keywords
# (consolid*, moeder, dochter, vermogensmutatie, intragroep, eliminati,
#  consolidatieverschil, goodwill, deelneming) via tekstscan op alle vragen.
SEED_PO_14: dict[str, dict] = {
    "2013-1-vr6": {
        "vraag_id": "2013-1-vr6",
        "vak_code_in_pdf": "1.2",
        "vak_naam_in_pdf": "Geconsolideerde jaarrekening",
        "programmaonderdelen": ["1.4"],
        "confidence": "hoog",
        "rationale": (
            "Vraag gaat over de opstelling van een geconsolideerde jaarrekening "
            "(vermelding dochtervennootschappen in balans) — kerninhoud van PO 1.4."
        ),
    },
    "2013-1-vr7": {
        "vraag_id": "2013-1-vr7",
        "vak_code_in_pdf": "1.2",
        "vak_naam_in_pdf": "Geconsolideerde jaarrekening",
        "programmaonderdelen": ["1.4"],
        "confidence": "hoog",
        "rationale": (
            "Vraag over afsluitingsdatum geconsolideerde jaarrekening — "
            "procedureel aspect van PO 1.4."
        ),
    },
    "2014-1-vr7": {
        "vraag_id": "2014-1-vr7",
        "vak_code_in_pdf": "1.2",
        "vak_naam_in_pdf": "Geconsolideerde jaarrekening",
        "programmaonderdelen": ["1.4"],
        "confidence": "hoog",
        "rationale": (
            "Vraag over afsluitingsdatum geconsolideerde jaarrekening — "
            "procedureel aspect van PO 1.4."
        ),
    },
    "2014-1-vr8": {
        "vraag_id": "2014-1-vr8",
        "vak_code_in_pdf": "1.2",
        "vak_naam_in_pdf": "Geconsolideerde jaarrekening",
        "programmaonderdelen": ["1.4"],
        "confidence": "hoog",
        "rationale": (
            "Tabel invullen voor moeder M met deelnemingen in A (70 %), B (30 %), C (60 %), "
            "D (20 %) — consolidatiemethode-keuze (integrale vs. evenredige vs. "
            "vermogensmutatie). Kerninhoud van PO 1.4."
        ),
    },
    "2015-1-vr11": {
        "vraag_id": "2015-1-vr11",
        "vak_code_in_pdf": "1.2",
        "vak_naam_in_pdf": "Geconsolideerde jaarrekening",
        "programmaonderdelen": ["1.4"],
        "confidence": "hoog",
        "rationale": (
            "Vraag definieert positief consolidatieverschil en vraagt de vier voornaamste "
            "oorzaken — kernbegrip van PO 1.4 (goodwill bij consolidatie)."
        ),
    },
}


# ─── Helpers ───────────────────────────────────────────────────────────────────


def laad_alle_vragen() -> list[dict]:
    """Laad alle vragen uit data/programma/examen_vragen/*.json (niet -labels.json)."""
    vragen: list[dict] = []
    for bestand in sorted(EXAMEN_VRAGEN_DIR.glob("*.json")):
        naam = bestand.name
        if naam.startswith("_") or naam.endswith("-labels.json"):
            continue
        try:
            data = json.loads(bestand.read_text(encoding="utf-8"))
            for vraag in data.get("vragen", []):
                vraag["_examen_id"] = data.get("examen_id", bestand.stem)
                vragen.append(vraag)
        except (json.JSONDecodeError, OSError):
            pass
    return vragen


def laad_po_overzicht() -> list[dict]:
    """Laad unieke PO-titels uit data/programma/anchors.json."""
    if not ANCHORS_FILE.exists():
        return []
    data = json.loads(ANCHORS_FILE.read_text(encoding="utf-8"))
    gezien: dict[str, str] = {}
    for anker in data.get("anchors", []):
        po = anker.get("po", "")
        titel = anker.get("po_titel", "")
        if po and po not in gezien:
            gezien[po] = titel
    return [{"po": po, "po_titel": titel} for po, titel in sorted(gezien.items())]


def laad_bestaande_classificatie() -> dict[str, dict]:
    """Laad bestaande classificatie (als het bestand bestaat)."""
    if not CLASSIFICATIE_BESTAND.exists():
        return {}
    try:
        return json.loads(CLASSIFICATIE_BESTAND.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def schrijf_classificatie(classificatie: dict[str, dict]) -> None:
    """Schrijf de classificatie naar het output-bestand."""
    CLASSIFICATIE_BESTAND.write_text(
        json.dumps(classificatie, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def schrijf_subagent_instructies(
    vragen: list[dict],
    po_overzicht: list[dict],
    al_geclassificeerd: set[str],
) -> Path:
    """Schrijf instructies voor de Sonnet-subagent die de classificatie uitvoert."""
    nog_te_classificeren = [v for v in vragen if v.get("id", "") not in al_geclassificeerd]

    po_tekst = "\n".join(
        f"- `{po['po']}`: {po['po_titel']}"
        for po in po_overzicht
    )

    vragen_tekst = json.dumps(
        [
            {
                "id": v.get("id"),
                "vak_code_in_pdf": v.get("vak_code_in_pdf", ""),
                "vak_naam_in_pdf": v.get("vak_naam_in_pdf", ""),
                "vraagtekst": v.get("vraagtekst", "")[:300],  # Eerste 300 tekens volstaan
                "themas": v.get("themas", []),
            }
            for v in nog_te_classificeren
        ],
        ensure_ascii=False,
        indent=2,
    )

    instructies = f"""# Examenvragen-classificatie naar programmaonderdelen — Subagent-instructies

**Gegenereerd op**: {datetime.now(timezone.utc).isoformat(timespec='seconds')}
**Model**: claude-sonnet-4-6
**Nog te classificeren**: {len(nog_te_classificeren)} vragen

## Jouw taak

Classificeer elke examenvraag hieronder naar het (de) juiste programmaonderdeel(en).

Een vraag kan meerdere programmaonderdelen raken (bv. een vraag over
'consolidatieverschil en fiscale behandeling' raakt PO 1.4 én een fiscaliteits-PO).

## Programmaonderdelen

{po_tekst}

## Output-schema per vraag

```json
{{
  "<vraag_id>": {{
    "vraag_id": "...",
    "vak_code_in_pdf": "...",
    "vak_naam_in_pdf": "...",
    "programmaonderdelen": ["1.4", "..."],
    "confidence": "hoog | midden | laag",
    "rationale": "<1-2 zin uitleg>"
  }}
}}
```

## Output-locatie

Schrijf het resultaat als één JSON-object naar:
`data/programma/examen_vragen/_programmaonderdeel_classificatie.json`

Gebruik de bestaande seed-entries als voorbeeld voor het formaat
(die staan al in het bestand als je dit leest).

**Merge met bestaande inhoud**: lees eerst het bestaande bestand,
voeg toe — overschrijf bestaande entries niet zonder reden.

## Richtlijnen

- Gebruik `vak_code_in_pdf` als eerste signaal (bv. "1.4" → PO 1.4).
- Maar: `vak_code_in_pdf` is de **oude nummering** uit de PDF.
  Koppel inhoudelijk: een vraag over 'geconsolideerde jaarrekening'
  of 'consolidatiemethode' hoort bij PO 1.4, ook als de code "1.2" zegt.
- Gebruik `themas[]` en `vraagtekst` voor twijfelgevallen.
- `confidence: "hoog"` als de koppeling duidelijk is uit de vraagtekst.
- `confidence: "midden"` bij redelijke afleiding maar niet 100 % zeker.
- `confidence: "laag"` bij gok of onduidelijke vraag.

## Vragen te classificeren

```json
{vragen_tekst}
```
"""

    INSTRUCTIES_BESTAND.write_text(instructies, encoding="utf-8")
    return INSTRUCTIES_BESTAND


# ─── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--seed-po-14",
        action="store_true",
        help="Schrijf de handmatige PO 1.4 seed-entries naar "
             "_programmaonderdeel_classificatie.json (9 vragen met consolidatie-keywords).",
    )
    parser.add_argument(
        "--droog",
        action="store_true",
        help="Droog uitvoeren: toon wat er zou worden gegenereerd maar schrijf niets weg.",
    )
    args = parser.parse_args()

    # Vragen en PO-overzicht laden
    print("[classificatie] vragen laden ...")
    vragen = laad_alle_vragen()
    print(f"  {len(vragen)} vragen geladen")

    po_overzicht = laad_po_overzicht()
    print(f"  {len(po_overzicht)} programmaonderdelen geladen uit {ANCHORS_FILE.relative_to(ROOT)}")

    bestaande = laad_bestaande_classificatie()
    print(f"  {len(bestaande)} vragen al geclassificeerd")

    # Seed voor PO 1.4 schrijven indien gevraagd
    if args.seed_po_14:
        nieuwe_seed = {k: v for k, v in SEED_PO_14.items() if k not in bestaande}
        if nieuwe_seed:
            if not args.droog:
                bestaande.update(nieuwe_seed)
                schrijf_classificatie(bestaande)
                print(
                    f"[seed] {len(nieuwe_seed)} PO 1.4 seed-entries toegevoegd aan "
                    f"{CLASSIFICATIE_BESTAND.relative_to(ROOT)}"
                )
            else:
                print(f"[droog] {len(nieuwe_seed)} PO 1.4 seed-entries NIET geschreven")
        else:
            print("[seed] Alle PO 1.4 seed-entries zijn al aanwezig")

    # Subagent-instructies schrijven
    al_geclassificeerd = set(bestaande.keys())
    nog_te_doen = len(vragen) - len(al_geclassificeerd & {v.get("id") for v in vragen})
    print(f"\n[instructies] {nog_te_doen} vragen nog te classificeren")

    if nog_te_doen > 0:
        if not args.droog:
            instructies_pad = schrijf_subagent_instructies(vragen, po_overzicht, al_geclassificeerd)
            print(f"[subagent] instructies geschreven naar {instructies_pad.relative_to(ROOT)}")
            print(
                f"\nVolgende stap: open {instructies_pad.relative_to(ROOT)} "
                f"in een Sonnet-subagent-sessie om de volledige classificatie uit te voeren."
            )
            print(
                f"\nNa de classificatie laadt verify_records.py automatisch de juiste vragen "
                f"via laad_examen_vragen_voor_programmaonderdeel() — "
                f"geen handmatige koppeling meer nodig."
            )
        else:
            print(f"[droog] subagent-instructies NIET geschreven")
    else:
        print("[classificatie] Alle vragen zijn al geclassificeerd — klaar.")

    # Samenvatting
    print(f"\n[samenvatting]")
    print(f"  Totaal vragen          : {len(vragen)}")
    print(f"  Al geclassificeerd     : {len(al_geclassificeerd)}")
    print(f"  Nog te classificeren   : {nog_te_doen}")
    if not args.droog and CLASSIFICATIE_BESTAND.exists():
        print(f"  Classificatie-bestand  : {CLASSIFICATIE_BESTAND.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
