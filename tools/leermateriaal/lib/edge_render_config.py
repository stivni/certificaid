"""Edge-render-configuratie — single source of truth voor bidirectionele edges.

ADR-010 §bidirectionele-edge-render: data-laag bewaart edges één-richting (op
de source-node, ADR-007 §edge-richting). Render-laag toont edges
bidirectioneel via een pre-render index-pass en deze config-tabel.

Per edge-type:
- `outgoing_label`: hoe de uitgaande edge rendert op de bron-fiche
- `incoming_label`: hoe de inkomende edge rendert op de target-fiche
- `bidirectional`: True als beide kanten gerenderd worden, False als alleen
  uitgaand (catch-all edges zoals `verwijst-naar` zouden te veel ruis geven
  als ze ook inkomend rendert worden — opt-out).
"""
from __future__ import annotations

from typing import TypedDict


class EdgeRenderConfig(TypedDict):
    outgoing_label: str
    incoming_label: str
    bidirectional: bool


EDGE_RENDER_CONFIG: dict[str, EdgeRenderConfig] = {
    "onderdeel-van": {
        "outgoing_label": "Behoort tot",
        "incoming_label": "Bestaat uit",
        "bidirectional": True,
    },
    "specialisatie-van": {
        "outgoing_label": "Specialisatie van",
        "incoming_label": "Specialisaties",
        "bidirectional": True,
    },
    "vereist-kennis-van": {
        "outgoing_label": "Vereist kennis van",
        "incoming_label": "Wordt voorondersteld in",
        "bidirectional": True,
    },
    "vergelijkt-met": {
        "outgoing_label": "Vergelijk met",
        "incoming_label": "Vergelijk met",
        "bidirectional": False,
    },
    "getriggerd-door": {
        "outgoing_label": "Getriggerd door",
        "incoming_label": "Triggert",
        "bidirectional": True,
    },
    "uitzondering-op": {
        "outgoing_label": "Uitzondering op",
        "incoming_label": "Uitzonderingen",
        "bidirectional": True,
    },
    "verwijst-naar": {
        "outgoing_label": "Verwijst naar",
        "incoming_label": "",
        "bidirectional": False,
    },
}

COLLAPSIBLE_DREMPEL = 7
"""Boven dit aantal inkomende edges van hetzelfde type: collapsible callout."""


def bidirectionele_edge_types() -> set[str]:
    """Set van edge-types waarvoor inverse rendering aan staat."""
    return {
        etype for etype, cfg in EDGE_RENDER_CONFIG.items()
        if cfg["bidirectional"]
    }


def incoming_label(edge_type: str) -> str:
    """Label voor de inkomende rendering, of lege string voor opt-out."""
    cfg = EDGE_RENDER_CONFIG.get(edge_type)
    if cfg is None or not cfg["bidirectional"]:
        return ""
    return cfg["incoming_label"]
