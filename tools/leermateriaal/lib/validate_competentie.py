"""
Schema-validator voor competentie-YAML-bestanden (ADR-007 §competentie-schema).

Anti-fabricatie-checks:
- gebaseerd_op_concepten ≥ 2 (verplicht)
- Elke stap heeft grondslag.ref of grondslag.type == 'praktijk' met motivering
- procedure_grondslag.wettelijk_pct + praktijk_pct == 100
- Wikilinks in grondslag.ref verwijzen naar bestaande concept-record-id's

Gebruik:
  python3 -m tools.leermateriaal.lib.validate_competentie <yaml-pad>
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"

_WIKILINK_PATROON = re.compile(r"\[\[([^\]#|]+)(?:#[^\]|]*)?\|?[^\]]*\]\]")


def _bestaande_record_ids() -> set[str]:
    """Laad alle bestaande concept-record-id's uit data/concepten/records/."""
    ids: set[str] = set()
    for bestand in RECORDS_DIR.glob("*.json"):
        if not bestand.name.startswith("_"):
            ids.add(bestand.stem)
    return ids


def _extraheer_wikilinks(tekst: str) -> list[str]:
    """Extraheer alle concept-id's uit [[wikilink]]-patronen."""
    return _WIKILINK_PATROON.findall(tekst)


def validate(competentie: dict) -> list[str]:
    """Valideer een competentie-dict op anti-fabricatie-regels.

    Args:
        competentie: geladen competentie-dict (uit YAML)

    Returns:
        lijst van fout-/waarschuwingsstrings; leeg = valide
    """
    fouten: list[str] = []
    bestaande_ids = _bestaande_record_ids()

    # 1. gebaseerd_op_concepten ≥ 2
    gebaseerd = competentie.get("gebaseerd_op_concepten", [])
    if len(gebaseerd) < 2:
        fouten.append(
            f"FOUT: gebaseerd_op_concepten heeft {len(gebaseerd)} item(s); "
            f"minimaal 2 vereist (ADR-007 anti-fabricatie-regel 1)."
        )

    # 2. procedure_grondslag-controle
    procedure_grondslag = competentie.get("procedure_grondslag", {})
    wettelijk_pct = procedure_grondslag.get("wettelijk_pct")
    praktijk_pct = procedure_grondslag.get("praktijk_pct")

    if wettelijk_pct is None or praktijk_pct is None:
        fouten.append(
            "FOUT: procedure_grondslag.wettelijk_pct en/of praktijk_pct ontbreken."
        )
    elif wettelijk_pct + praktijk_pct != 100:
        fouten.append(
            f"FOUT: procedure_grondslag.wettelijk_pct ({wettelijk_pct}) + "
            f"praktijk_pct ({praktijk_pct}) = {wettelijk_pct + praktijk_pct}; "
            f"moet 100 zijn (ADR-007 anti-fabricatie-regel 3)."
        )
    elif praktijk_pct > 50:
        fouten.append(
            f"WAARSCHUWING: procedure_grondslag.praktijk_pct = {praktijk_pct}% > 50%; "
            f"verplicht mens-review (ADR-007 anti-fabricatie-regel 4)."
        )

    # 3. Stap-validatie
    stappen = competentie.get("stappen", [])
    for stap in stappen:
        nummer = stap.get("nr", "?")
        grondslag = stap.get("grondslag", {})

        if not grondslag:
            fouten.append(
                f"FOUT: stap {nummer} heeft geen grondslag-object "
                f"(ADR-007 anti-fabricatie-regel 2)."
            )
            continue

        grondslag_type = grondslag.get("type", "")
        grondslag_ref = grondslag.get("ref", "")

        if grondslag_type == "praktijk":
            # Praktijk-type vereist motivering
            if not grondslag.get("motivering", "").strip():
                fouten.append(
                    f"FOUT: stap {nummer} heeft grondslag.type='praktijk' "
                    f"maar geen motivering (ADR-007 anti-fabricatie-regel 2)."
                )
        elif not grondslag_ref:
            fouten.append(
                f"FOUT: stap {nummer} heeft geen grondslag.ref "
                f"(ADR-007 anti-fabricatie-regel 2)."
            )
        else:
            # Valideer wikilinks in grondslag.ref
            wikilinks = _extraheer_wikilinks(str(grondslag_ref))
            for link in wikilinks:
                link_id = link.strip()
                if link_id and link_id not in bestaande_ids:
                    fouten.append(
                        f"WAARSCHUWING: stap {nummer} grondslag.ref verwijst naar "
                        f"'[[{link_id}]]' maar dat record bestaat niet "
                        f"in data/concepten/records/ (ADR-007 anti-fabricatie-regel 5)."
                    )

    # 4. Wikilinks in gebaseerd_op_concepten
    for concept_id in gebaseerd:
        if concept_id not in bestaande_ids:
            fouten.append(
                f"WAARSCHUWING: gebaseerd_op_concepten verwijst naar '{concept_id}' "
                f"maar dat record bestaat niet in data/concepten/records/."
            )

    return fouten


def validate_file(yaml_pad: Path) -> list[str]:
    """Laad een YAML-bestand en valideer de competentie.

    Args:
        yaml_pad: pad naar competentie-YAML-bestand

    Returns:
        lijst van fout-/waarschuwingsstrings; leeg = valide
    """
    try:
        with open(yaml_pad, encoding="utf-8") as f:
            competentie = yaml.safe_load(f)
    except (yaml.YAMLError, OSError) as fout:
        return [f"FOUT: kon YAML niet laden: {fout}"]

    if not isinstance(competentie, dict):
        return ["FOUT: YAML-root is geen object/dict."]

    return validate(competentie)


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Gebruik: python3 -m tools.leermateriaal.lib.validate_competentie <yaml-pad>")
        sys.exit(1)

    yaml_pad = Path(sys.argv[1])
    if not yaml_pad.exists():
        print(f"FOUT: bestand niet gevonden: {yaml_pad}", file=sys.stderr)
        sys.exit(1)

    fouten = validate_file(yaml_pad)
    if fouten:
        for fout in fouten:
            print(fout)
        # Exit met code 1 als er echte fouten zijn (niet alleen warnings)
        echte_fouten = [f for f in fouten if f.startswith("FOUT:")]
        sys.exit(1 if echte_fouten else 0)
    else:
        print("OK")


if __name__ == "__main__":
    main()
