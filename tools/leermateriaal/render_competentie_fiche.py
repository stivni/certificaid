"""
Deterministisch renderer voor competentie-fiches (ADR-007 competentie-schema 1.5).

Leest JSON-records met node_type=competentie uit data/concepten/records/ en schrijft
Quartz-compatibele Markdown-fiches naar content/competenties/<id>.md.

Valideer eerst via validate_competentie.py — records met fouten worden overgeslagen.

Geen LLM-calls — volledig deterministisch.

Gebruik:
  python3 -m tools.leermateriaal.render_competentie_fiche \\
      --competentie bepalen-consolidatieverplichting
  python3 -m tools.leermateriaal.render_competentie_fiche --alle
  python3 -m tools.leermateriaal.render_competentie_fiche --programmaonderdeel 1.4
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
OUTPUT_DIR = ROOT / "content" / "competenties"


def _laad_alle_competenties() -> list[tuple[Path, dict]]:
    """Laad alle JSON-records met node_type=competentie (skip bestanden die beginnen met _)."""
    resultaat: list[tuple[Path, dict]] = []
    for bestand in sorted(RECORDS_DIR.glob("*.json")):
        if bestand.name.startswith("_"):
            continue
        try:
            competentie = json.loads(bestand.read_text(encoding="utf-8"))
            if isinstance(competentie, dict) and competentie.get("node_type") == "competentie":
                resultaat.append((bestand, competentie))
        except (json.JSONDecodeError, OSError) as fout:
            print(f"  [WAARSCHUWING] {bestand.name}: overgeslagen ({fout})", file=sys.stderr)
    return resultaat


def _filter_op_programmaonderdeel(
    competenties: list[tuple[Path, dict]], programmaonderdeel_id: str
) -> list[tuple[Path, dict]]:
    """Filter competenties op programmaonderdeel via programmaonderdelen[]."""
    return [
        (pad, comp) for pad, comp in competenties
        if programmaonderdeel_id in [str(p) for p in comp.get("programmaonderdelen", [])]
    ]


def render_competentie(competentie: dict) -> str:
    """Render één competentie-dict naar Markdown-string.

    Args:
        competentie: volledig competentie-dict (schema 1.0)

    Returns:
        volledige Markdown-string incl. frontmatter
    """
    from tools.leermateriaal.lib.frontmatter import as_yaml_block, competentie_fiche_frontmatter
    from tools.leermateriaal.lib.jinja_env import get_env

    frontmatter = competentie_fiche_frontmatter(competentie)
    frontmatter_yaml = as_yaml_block(frontmatter)

    env = get_env()
    template = env.get_template("competentie_fiche.md.j2")

    return template.render(
        competentie=competentie,
        frontmatter_yaml=frontmatter_yaml,
    )


def render_naar_bestand(
    competentie: dict, output_dir: Path, droog: bool = False
) -> Path:
    """Render een competentie en schrijf naar content/competenties/<id>.md."""
    competentie_id = competentie.get("id", "onbekend")
    output_pad = output_dir / f"{competentie_id}.md"

    inhoud = render_competentie(competentie)

    if not droog:
        output_dir.mkdir(parents=True, exist_ok=True)
        output_pad.write_text(inhoud, encoding="utf-8")

    return output_pad


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    groep = parser.add_mutually_exclusive_group(required=True)
    groep.add_argument("--competentie", help="Competentie-id, bv. 'bepalen-consolidatieverplichting'.")
    groep.add_argument("--alle", action="store_true", help="Render alle competenties.")
    groep.add_argument(
        "--programmaonderdeel",
        help="Render competenties voor een programmaonderdeel, bv. '1.4'.",
    )
    parser.add_argument(
        "--output-map",
        default=str(OUTPUT_DIR.relative_to(ROOT)),
        help="Output-map (relatief aan repo-root). Default: content/competenties/",
    )
    parser.add_argument(
        "--droog",
        action="store_true",
        help="Droog uitvoeren: render maar schrijf niets weg.",
    )
    parser.add_argument(
        "--skip-validatie",
        action="store_true",
        help="Sla validatie over (niet aanbevolen).",
    )
    args = parser.parse_args()

    output_dir = ROOT / args.output_map

    # Competenties laden
    alle_competenties = _laad_alle_competenties()

    if args.competentie:
        te_renderen = [
            (pad, comp) for pad, comp in alle_competenties
            if comp.get("id") == args.competentie
        ]
        if not te_renderen:
            print(f"FOUT: geen competentie gevonden met id '{args.competentie}'.", file=sys.stderr)
            sys.exit(1)
    elif args.alle:
        te_renderen = alle_competenties
    else:
        te_renderen = _filter_op_programmaonderdeel(alle_competenties, args.programmaonderdeel)
        if not te_renderen:
            print(
                f"FOUT: geen competenties gevonden voor programmaonderdeel '{args.programmaonderdeel}'.",
                file=sys.stderr,
            )
            sys.exit(1)

    # Validatie + renderen
    from tools.leermateriaal.lib.validate_competentie import validate

    verwerkt = 0
    overgeslagen = 0
    output_paden: list[Path] = []

    for pad, competentie in te_renderen:
        competentie_id = competentie.get("id", "?")

        # Valideer eerst
        if not args.skip_validatie:
            fouten = validate(competentie)
            echte_fouten = [f for f in fouten if f.startswith("FOUT:")]
            waarschuwingen = [f for f in fouten if f.startswith("WAARSCHUWING:")]

            for w in waarschuwingen:
                print(f"  [{competentie_id}] {w}", file=sys.stderr)

            if echte_fouten:
                print(
                    f"  [OVERGESLAGEN] {competentie_id}: {len(echte_fouten)} validatiefouten.",
                    file=sys.stderr,
                )
                for fout in echte_fouten:
                    print(f"    - {fout}", file=sys.stderr)
                overgeslagen += 1
                continue

        try:
            output_pad = render_naar_bestand(competentie, output_dir, droog=args.droog)
            output_paden.append(output_pad)
            verwerkt += 1
        except Exception as fout:
            print(f"  [FOUT] {competentie_id}: {fout}", file=sys.stderr)
            overgeslagen += 1

    # Rapport
    print(f"[render_competentie_fiche] {verwerkt} competenties verwerkt, {overgeslagen} overgeslagen.")
    if args.droog:
        print("  [droog] Geen bestanden weggeschreven.")
    else:
        for pad in output_paden:
            print(f"  → {pad.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
