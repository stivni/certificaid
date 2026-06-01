"""
Quartz-frontmatter helpers voor leermateriaal-rendering (ADR-010 §fiche-structuur).

Produceert YAML-frontmatter-blokken die Quartz verwerkt als page metadata,
tags en wikilink-navigatie.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import yaml

from tools.leermateriaal.lib.confidence import mode_confidence


def _programmaonderdeel_codes_uit_anchors(linked_anchors: list[str]) -> list[str]:
    """Extraheer unieke programmaonderdeel-codes uit een lijst anchor-id's.

    Elke anchor-id begint met '<po>.' bv. '1.4.I.A'. We nemen het prefix tot
    de eerste punt na het eerste punt (X.Y formaat).

    Args:
        linked_anchors: lijst van anchor-id's

    Returns:
        gesorteerde unieke lijst van programmaonderdeel-codes, bv. ['1.4', '4.0']
    """
    codes: set[str] = set()
    for anker in linked_anchors:
        delen = anker.split(".")
        if len(delen) >= 2:
            codes.add(f"{delen[0]}.{delen[1]}")
    return sorted(codes)


def concept_fiche_frontmatter(record: dict) -> dict:
    """Genereer Quartz-frontmatter voor een concept-fiche.

    Args:
        record: volledig concept-record dict (schema 1.2/1.3)

    Returns:
        frontmatter dict klaar voor as_yaml_block()
    """
    linked_anchors = record.get("linked_anchors", [])
    programmaonderdelen = _programmaonderdeel_codes_uit_anchors(linked_anchors)

    # Tags: concept + node_type + programmaonderdeel-codes
    tags: list[str] = ["concept"]
    node_type = record.get("node_type", "")
    if node_type:
        tags.append(node_type)
    tags.extend(f"po-{code.replace('.', '-')}" for code in programmaonderdelen)

    return {
        "title": record.get("naam", record.get("id", "")),
        "tags": tags,
        "linked_anchors": linked_anchors,
        "programmaonderdelen": programmaonderdelen,
        "confidence": mode_confidence(record),
        "node_type": node_type,
        "status": record.get("status", "seed"),
        "schema_version": record.get("schema_version", "1.2"),
        "gegenereerd_uit": f"data/concepten/records/{record.get('id', '')}.json",
        "gegenereerd_op": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }


def competentie_fiche_frontmatter(competentie: dict) -> dict:
    """Genereer Quartz-frontmatter voor een competentie-fiche.

    Args:
        competentie: volledig competentie-record dict (schema 1.5 JSON, node_type=competentie)

    Returns:
        frontmatter dict
    """
    programmaonderdelen: list[str] = [
        str(p) for p in competentie.get("programmaonderdelen", [])
    ]

    tags: list[str] = ["competentie"]
    competency_type = competentie.get("competency_type", "")
    if competency_type:
        tags.append(competency_type)
    tags.extend(f"po-{code.replace('.', '-')}" for code in programmaonderdelen)

    return {
        "title": competentie.get("titel", competentie.get("naam", competentie.get("id", ""))),
        "tags": tags,
        "programmaonderdelen": programmaonderdelen,
        "status": competentie.get("status", "voorgesteld"),
        "schema_version": competentie.get("schema_version", "1.5"),
        "gegenereerd_uit": f"data/concepten/records/{competentie.get('id', '')}.json",
        "gegenereerd_op": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }


def minicursus_frontmatter(
    programmaonderdeel_code: str,
    programmaonderdeel_titel: str,
    gerelateerde_concept_ids: list[str],
) -> dict:
    """Genereer Quartz-frontmatter voor een minicursus.

    Args:
        programmaonderdeel_code: bv. '1.4'
        programmaonderdeel_titel: bv. 'Geconsolideerde jaarrekening'
        gerelateerde_concept_ids: lijst van concept-id's in deze minicursus

    Returns:
        frontmatter dict
    """
    return {
        "title": f"{programmaonderdeel_code} {programmaonderdeel_titel}",
        "tags": [
            "overzicht",
            f"po-{programmaonderdeel_code.replace('.', '-')}",
        ],
        "programmaonderdeel": programmaonderdeel_code,
        "gerelateerde_concepten": gerelateerde_concept_ids,
        "gegenereerd_op": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }


def as_yaml_block(frontmatter: dict) -> str:
    """Serialiseer een frontmatter-dict naar een YAML-frontmatter-blok.

    Args:
        frontmatter: dict met frontmatter-velden

    Returns:
        string die begint met '---\\n' en eindigt op '---\\n'
    """
    yaml_tekst = yaml.safe_dump(
        frontmatter,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    )
    return f"---\n{yaml_tekst}---\n"
