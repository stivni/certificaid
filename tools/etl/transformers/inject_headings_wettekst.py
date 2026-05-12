"""
Transformer: inject_headings_wettekst (ADR-005 §4).

Wraps de Belgische wettekst hiërarchie-injectielogica uit
`tools/lib/headings.py::process_wettekst` als een transformer-functie.

Verantwoordelijkheid:
  - Detecteer DEEL/BOEK/TITEL/HOOFDSTUK/AFDELING/ONDERAFDELING/Art. in de body.
  - Injecteer markdown-headings op de juiste niveaus.
  - Schrijf het chunk:-blok in de frontmatter.

De `sub_strategy`-parameter (ADR-006 §4.2) wordt gelezen uit de
`_sub_strategy` sleutel in frontmatter (ingesteld door de orchestrator).

Signature: (body: str, frontmatter: dict) -> tuple[str, dict]
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.lib.headings import (  # noqa: E402
    detect_hierarchy,
    apply_conditional_flattening,
    build_level_map,
    inject_headings,
    update_frontmatter_chunk,
)


def inject_headings_wettekst(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Injecteer Belgische wettekst-headings in de body en schrijf chunk-config.

    De chunk-configuratie wordt opgeslagen als `_chunk_info` in frontmatter
    (intern veld) en als platte sleutels `chunk_level`, `chunk_type` en
    `sub_strategy` voor gebruik door `emit_frontmatter`.

    De orchestrator leest het info-resultaat achteraf terug via `_chunk_info`
    om het in logging te gebruiken.
    """
    sub_strategy = frontmatter.pop("_sub_strategy", None)

    ranks = detect_hierarchy(body)
    reduced_ranks, merge_parent = apply_conditional_flattening(ranks)
    level_map = build_level_map(reduced_ranks, merge_parent)
    chunk_level = level_map.get("Art.", 2)

    nieuwe_body, n_conversies = inject_headings(body, level_map, merge_parent)

    # Sla chunk-info op als intern frontmatter-veld voor emit_frontmatter.
    frontmatter["_chunk_level"] = chunk_level
    frontmatter["_chunk_type"] = "Art."
    frontmatter["_sub_strategy"] = sub_strategy  # kan None zijn

    # Logging-info voor de orchestrator
    frontmatter["_chunk_info"] = {
        "ranks": ranks,
        "reduced_ranks": reduced_ranks,
        "merge_parent": merge_parent,
        "level_map": level_map,
        "chunk_level": chunk_level,
        "n_conversies": n_conversies,
    }

    return nieuwe_body, frontmatter
