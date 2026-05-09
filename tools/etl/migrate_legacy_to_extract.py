"""
Migreer legacy `type:`-entries in source_config.yaml naar het nieuwe `extract:`-schema
(ADR-017, geïntroduceerd 2026-05-07).

Gebruik:
  python3 tools/etl/migrate_legacy_to_extract.py            # dry-run
  python3 tools/etl/migrate_legacy_to_extract.py --uitvoeren # schrijft source_config.yaml

Mapping (op basis van de live dispatcher in tools/etl/convert.py):
  ejustice_nl        → extract.method: pdftotext_ejustice
  ejustice_bilingual → extract.method: pdftotext_ejustice  + params.bilingual: true
                       + params.nl_col_x overgenomen uit het bronveld `nl_col_x`
  wetboek            → extract.method: custom_wetboek
  wib92              → extract.method: custom_wib92
  split              → extract.method: derived
                       + params.afgeleid_uit overgenomen uit `derived_from`
  skip               → extract.method: handcrafted
                       + params.reden overgenomen uit `note` (als aanwezig)
  raw_md             → extract.method: handcrafted
                       + params.reden: "handmatig verwerkt, geen herconversie via convert.py"

Bestaande `extract:`-blokken worden nooit overschreven (extract: wint van type:).
"""

import argparse
import sys
from pathlib import Path

import ruamel.yaml

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_PAD = ROOT / "resources" / "source_config.yaml"

# ---------------------------------------------------------------------------
# Mapping
# ---------------------------------------------------------------------------

def bouw_extract_blok(naam: str, velden: dict) -> dict | None:
    """
    Geeft een nieuw extract-blok terug op basis van de legacy `type:`-waarde,
    of None als het type onbekend is.
    """
    brontype = velden.get("type", "").strip()

    if brontype == "ejustice_nl":
        params = {}
        if velden.get("simple_mode"):
            params["simple_mode"] = True
        # start_page en end_page zijn zeldzaam voor ejustice_nl maar bewaar ze als aanwezig
        if velden.get("start_page"):
            params["start_page"] = velden["start_page"]
        if velden.get("end_page"):
            params["end_page"] = velden["end_page"]
        return {"method": "pdftotext_ejustice", "params": params} if params else {"method": "pdftotext_ejustice"}

    if brontype == "ejustice_bilingual":
        params: dict = {"bilingual": True}
        if "nl_col_x" in velden:
            params["nl_col_x"] = velden["nl_col_x"]
        if velden.get("start_page"):
            params["start_page"] = velden["start_page"]
        if velden.get("end_page"):
            params["end_page"] = velden["end_page"]
        return {"method": "pdftotext_ejustice", "params": params}

    if brontype == "wetboek":
        params = {}
        # `mode`, `col_x`, `start_page`, `wet`, `titel` zijn wetboek-specifiek —
        # convert-wetboek.py leest die rechtstreeks uit de yaml-entry, dus we
        # hoeven ze hier NIET te dupliceren in params.
        return {"method": "custom_wetboek"}

    if brontype == "wib92":
        return {"method": "custom_wib92"}

    if brontype == "split":
        params = {}
        if velden.get("derived_from"):
            params["afgeleid_uit"] = velden["derived_from"]
        return {"method": "derived", "params": params} if params else {"method": "derived"}

    if brontype in ("skip", "raw_md"):
        params: dict = {}
        notitie = velden.get("note", "")
        if notitie:
            # ruamel.yaml kan ScalarString retourneren — forceer naar str
            reden = str(notitie).strip().replace("\n", " ")
            params["reden"] = reden
        else:
            params["reden"] = (
                "handmatig verwerkt — geen herconversie via convert.py"
            )
        return {"method": "handcrafted", "params": params}

    return None  # onbekend type


# ---------------------------------------------------------------------------
# Hoofd-logica
# ---------------------------------------------------------------------------

def migreer(uitvoeren: bool = False) -> int:
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    yaml.default_flow_style = False
    yaml.width = 120

    with open(CONFIG_PAD) as bestand:
        data = yaml.load(bestand)

    sources = data.get("sources", {})

    aantal_gemigreerd: dict[str, int] = {}
    aantal_overgeslagen = 0
    aantal_al_extract = 0
    waarschuwingen: list[str] = []

    for naam, velden in sources.items():
        if velden is None:
            continue

        heeft_extract = "extract" in velden
        heeft_type = "type" in velden

        if heeft_extract and not heeft_type:
            # Al volledig gemigreerd — sla over
            aantal_al_extract += 1
            continue

        if heeft_extract and heeft_type:
            # Beide aanwezig: extract wint, maar log waarschuwing
            waarschuwingen.append(
                f"  ⚠️  {naam}: heeft zowel 'extract:' als 'type:' — "
                f"'extract:' blijft staan, 'type:' wordt verwijderd"
            )
            del velden["type"]
            aantal_al_extract += 1
            continue

        if not heeft_type:
            # Geen type, geen extract — sla over
            aantal_overgeslagen += 1
            continue

        brontype = str(velden.get("type", "")).strip()
        extract_blok = bouw_extract_blok(naam, velden)

        if extract_blok is None:
            waarschuwingen.append(
                f"  ⚠️  {naam}: onbekend type '{brontype}' — niet gemigreerd"
            )
            aantal_overgeslagen += 1
            continue

        # Voeg extract: in toe (na de bestaande velden, vóór cleanup als dat bestaat)
        # ruamel.yaml behoudt insertie-volgorde via CommentedMap
        velden["extract"] = extract_blok
        del velden["type"]

        aantal_gemigreerd[brontype] = aantal_gemigreerd.get(brontype, 0) + 1

    # Rapport
    print(f"\n{'─'*60}")
    print("Migratie-samenvatting")
    print(f"{'─'*60}")
    totaal = sum(aantal_gemigreerd.values())
    for brontype, aantal in sorted(aantal_gemigreerd.items()):
        print(f"  {brontype:<30} → {aantal:>3} gemigreerd")
    print(f"  {'─'*38}")
    print(f"  {'Totaal gemigreerd':<30}   {totaal:>3}")
    print(f"  {'Al op extract-schema':<30}   {aantal_al_extract:>3}")
    print(f"  {'Overgeslagen (geen type/onbekend)':<30}   {aantal_overgeslagen:>3}")

    if waarschuwingen:
        print(f"\nWaarschuwingen:")
        for w in waarschuwingen:
            print(w)

    if not uitvoeren:
        print(f"\n[DRY-RUN] Geen wijzigingen geschreven. Gebruik --uitvoeren om op te slaan.")
        return 0

    with open(CONFIG_PAD, "w") as bestand:
        yaml.dump(data, bestand)

    print(f"\n✅ Geschreven: {CONFIG_PAD.relative_to(ROOT)}")
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Migreer legacy type:-entries naar het ADR-017 extract:-schema"
    )
    parser.add_argument(
        "--uitvoeren",
        action="store_true",
        help="Schrijf de gewijzigde source_config.yaml (zonder dit vlag: dry-run)",
    )
    args = parser.parse_args()
    sys.exit(migreer(uitvoeren=args.uitvoeren))


if __name__ == "__main__":
    main()
