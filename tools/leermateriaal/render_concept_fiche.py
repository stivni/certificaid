"""
Deterministisch renderer voor concept-fiches (ADR-007 schema 1.3 + ADR-010).

Leest JSON-records uit data/concepten/records/ en schrijft Quartz-compatibele
Markdown-fiches naar content/concepten/<id>.md.

Geen LLM-calls — volledig deterministisch.

Gebruik:
  python3 -m tools.leermateriaal.render_concept_fiche --record controle
  python3 -m tools.leermateriaal.render_concept_fiche --alle
  python3 -m tools.leermateriaal.render_concept_fiche --programmaonderdeel 1.4
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
OUTPUT_DIR = ROOT / "content" / "concepten"


def _laad_alle_records() -> list[dict]:
    """Laad alle JSON-records (skip bestanden die beginnen met _)."""
    records = []
    for bestand in sorted(RECORDS_DIR.glob("*.json")):
        if bestand.name.startswith("_"):
            continue
        try:
            record = json.loads(bestand.read_text(encoding="utf-8"))
            records.append(record)
        except (json.JSONDecodeError, OSError) as fout:
            print(f"  [WAARSCHUWING] {bestand.name}: overgeslagen ({fout})", file=sys.stderr)
    return records


def _filter_op_programmaonderdeel(records: list[dict], programmaonderdeel_id: str) -> list[dict]:
    """Filter records op programmaonderdeel via linked_anchors[]."""
    prefix = f"{programmaonderdeel_id}."
    return [
        r for r in records
        if any(anker.startswith(prefix) for anker in r.get("linked_anchors", []))
    ]


def _extraheer_chunk_ids(record: dict) -> list[str]:
    """Extraheer alle unieke chunk-id's uit _provenance.inputs over het hele record."""
    chunk_ids: list[str] = []
    gezien: set[str] = set()

    def _zoek_in(obj: object) -> None:
        if isinstance(obj, dict):
            if "inputs" in obj:
                for input_item in obj["inputs"]:
                    if isinstance(input_item, dict):
                        chunk_id = input_item.get("id", "")
                        if chunk_id and chunk_id not in gezien:
                            chunk_ids.append(chunk_id)
                            gezien.add(chunk_id)
            for waarde in obj.values():
                _zoek_in(waarde)
        elif isinstance(obj, list):
            for item in obj:
                _zoek_in(item)

    _zoek_in(record)
    return chunk_ids


def _voeg_anker_slugs_toe(record: dict) -> dict:
    """Auto-genereer anker_slug voor in_praktijk[]-blokken zonder slug (schema 1.3)."""
    from tools.leermateriaal.lib.wikilinks import slugify

    in_praktijk = record.get("in_praktijk", [])
    for blok in in_praktijk:
        if "anker_slug" not in blok and "aspect" in blok:
            blok["anker_slug"] = slugify(blok["aspect"])
    return record


def bouw_inverse_edges_index(records: list[dict]) -> dict[str, dict[str, list[str]]]:
    """Bouw map target_id → {edge_type: [source_id, ...]} over alle records.

    ADR-010 §bidirectionele-edge-render: edges leven op de bron-node (ADR-007
    §edge-richting). Voor render-tijd inverse-edges-display moet target-node
    weten welke bron-records naar hem verwijzen. Eén pass over alle records
    levert die index — daarna O(1) lookup per record.

    Alleen edge-types die in EDGE_RENDER_CONFIG als bidirectional staan worden
    opgenomen. `verwijst-naar` (catch-all) wordt opt-out — anders zou een
    populair concept dozijnen inkomende verwijzingen tonen.

    Args:
        records: lijst van concept-records

    Returns:
        dict mapping target-id naar dict van edge-type naar list van source-ids
    """
    from tools.leermateriaal.lib.edge_render_config import bidirectionele_edge_types

    bidirectionele = bidirectionele_edge_types()
    index: dict[str, dict[str, list[str]]] = {}

    for record in records:
        source_id = record.get("id")
        if not source_id:
            continue
        for edge in record.get("edges", []) or []:
            if not isinstance(edge, dict):
                continue
            edge_type = edge.get("type")
            target_id = edge.get("target")
            if not target_id or edge_type not in bidirectionele:
                continue
            index.setdefault(target_id, {}).setdefault(edge_type, []).append(source_id)

    # Sorteer voor deterministische render-output
    for target_id in index:
        for edge_type in index[target_id]:
            index[target_id][edge_type].sort()

    return index


def render_record(record: dict, inverse_edges: dict[str, list[str]] | None = None) -> str:
    """Render één concept-record naar Markdown-string.

    Args:
        record: volledig concept-record dict (schema 1.2/1.3)
        inverse_edges: optioneel {edge_type: [source_id, ...]} met de inkomende
            edges voor dit record. None betekent geen inverse-rendering (snel pad
            voor save_record per individuele write). Volledige inverse-display
            vereist `render_concept_fiche --alle` met de globale index.

    Returns:
        volledige Markdown-string incl. frontmatter
    """
    from tools.leermateriaal.lib.confidence import label as confidence_label, mode_confidence
    from tools.leermateriaal.lib.edge_render_config import COLLAPSIBLE_DREMPEL
    from tools.leermateriaal.lib.frontmatter import as_yaml_block, concept_fiche_frontmatter
    from tools.leermateriaal.lib.jinja_env import get_env
    from tools.leermateriaal.lib.wijzigingen_cache import laad_wijzigingen_cache

    # Voeg anker_slugs toe (schema 1.3 — auto-genereer als ontbrekend)
    record = _voeg_anker_slugs_toe(record)

    # Frontmatter
    frontmatter = concept_fiche_frontmatter(record)
    frontmatter_yaml = as_yaml_block(frontmatter)

    # Confidence-label voor header
    conf = mode_confidence(record)
    mode_confidence_label = confidence_label(conf)

    # Chunk-ids voor bronnen-sectie
    chunk_ids = _extraheer_chunk_ids(record)

    # Wijzigingen-badge (ADR-010 §versionering) — lege cache = geen badge
    cache = laad_wijzigingen_cache()
    wijziging_datum = cache.records.get(record.get("id", ""), "")

    # Jinja2 rendering
    env = get_env()
    template = env.get_template("concept_fiche.md.j2")

    return template.render(
        record=record,
        frontmatter_yaml=frontmatter_yaml,
        mode_confidence_label=mode_confidence_label,
        chunk_ids=chunk_ids,
        rationale=record.get("rationale"),
        inverse_edges=inverse_edges or {},
        collapsible_drempel=COLLAPSIBLE_DREMPEL,
        wijziging_datum=wijziging_datum,
        wijziging_basis_ref=cache.basis_ref,
    )


def is_synthese_record(record: dict) -> bool:
    """True voor records met node_type='synthese' (ADR-010 §implicatie-2)."""
    return record.get("node_type") == "synthese"


def render_naar_bestand(
    record: dict,
    output_dir: Path,
    droog: bool = False,
    inverse_edges: dict[str, list[str]] | None = None,
) -> Path | None:
    """Render een record en schrijf naar content/concepten/<id>.md.

    Synthese-records (node_type='synthese') krijgen géén losse fiche (ADR-010
    §implicatie-2): ze leven uitsluitend ingebed in een minicursus.
    Returnt None voor synthese-records; bestaande fiche wordt verwijderd.

    Args:
        record: concept-record dict
        output_dir: doelmap
        droog: als True, schrijf niets weg
        inverse_edges: optionele {edge_type: [source_id, ...]} met inkomende edges
            voor dit record. Zie render_record() voor semantiek.

    Returns:
        pad van het output-bestand, of None voor synthese-records
    """
    record_id = record.get("id", "onbekend")
    output_pad = output_dir / f"{record_id}.md"

    if is_synthese_record(record):
        if not droog and output_pad.exists():
            output_pad.unlink()
        return None

    inhoud = render_record(record, inverse_edges=inverse_edges)

    if not droog:
        output_dir.mkdir(parents=True, exist_ok=True)
        output_pad.write_text(inhoud, encoding="utf-8")

    return output_pad


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    groep = parser.add_mutually_exclusive_group(required=True)
    groep.add_argument("--record", help="Record-id om te renderen, bv. 'controle'.")
    groep.add_argument("--alle", action="store_true", help="Render alle records.")
    groep.add_argument(
        "--programmaonderdeel",
        help="Render records voor een programmaonderdeel, bv. '1.4'.",
    )
    parser.add_argument(
        "--output-map",
        default=str(OUTPUT_DIR.relative_to(ROOT)),
        help="Output-map (relatief aan repo-root). Default: content/concepten/",
    )
    parser.add_argument(
        "--droog",
        action="store_true",
        help="Droog uitvoeren: render maar schrijf niets weg.",
    )
    args = parser.parse_args()

    output_dir = ROOT / args.output_map

    # Records laden
    alle_records = _laad_alle_records()

    if args.record:
        te_renderen = [r for r in alle_records if r.get("id") == args.record]
        if not te_renderen:
            print(f"FOUT: geen record gevonden met id '{args.record}'.", file=sys.stderr)
            sys.exit(1)
    elif args.alle:
        te_renderen = alle_records
    else:
        te_renderen = _filter_op_programmaonderdeel(alle_records, args.programmaonderdeel)
        if not te_renderen:
            print(
                f"FOUT: geen records gevonden voor programmaonderdeel '{args.programmaonderdeel}'.",
                file=sys.stderr,
            )
            sys.exit(1)

    # Bouw inverse-edges-index over ALLE records (niet alleen de te-renderen
    # subset) — anders missen we inkomende edges van records buiten de filter.
    inverse_index = bouw_inverse_edges_index(alle_records)

    # Renderen
    verwerkt = 0
    geskipt_synthese = 0
    output_paden: list[Path] = []

    for record in te_renderen:
        record_id = record.get("id", "?")
        inverse_for_record = inverse_index.get(record_id, {})
        try:
            pad = render_naar_bestand(
                record, output_dir, droog=args.droog, inverse_edges=inverse_for_record
            )
            if pad is None:
                geskipt_synthese += 1
            else:
                output_paden.append(pad)
            verwerkt += 1
        except Exception as fout:
            print(f"  [FOUT] {record_id}: {fout}", file=sys.stderr)

    # Rapport
    print(f"[render_concept_fiche] {verwerkt} records verwerkt ({geskipt_synthese} synthese-skips).")
    if args.droog:
        print("  [droog] Geen bestanden weggeschreven.")
    else:
        for pad in output_paden:
            print(f"  → {pad.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
