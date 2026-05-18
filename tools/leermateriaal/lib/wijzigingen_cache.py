"""Wijzigingen-cache reader voor render-laag (ADR-010 §versionering).

Leest `data/leermateriaal/wijzigingen-actueel.json` (geproduceerd door
`tools/leermateriaal/build_changelog.py`) en biedt een lookup per record-id /
minicursus-id naar de laatste commit-datum. Gebruikt door render-templates
om een "Bijgewerkt sinds <basis_ref>" callout te plaatsen op gewijzigde
fiches.

Cache-bestand mag ontbreken (pre-v1.0 of nog niet gegenereerd) — module
returnt een lege wrapper.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import NamedTuple

ROOT = Path(__file__).resolve().parent.parent.parent.parent
CACHE_FILE = ROOT / "data" / "leermateriaal" / "wijzigingen-actueel.json"


class WijzigingenIndex(NamedTuple):
    basis_ref: str
    records: dict[str, str]       # id → laatste commit-datum (YYYY-MM-DD)
    minicursussen: dict[str, str]


def _leeg() -> WijzigingenIndex:
    return WijzigingenIndex(basis_ref="", records={}, minicursussen={})


def laad_wijzigingen_cache() -> WijzigingenIndex:
    """Laad cache of returnt lege index als bestand niet bestaat."""
    if not CACHE_FILE.exists():
        return _leeg()
    try:
        data = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return _leeg()

    def _laatste(datums: list[str] | None) -> str:
        return max(datums or [], default="")

    return WijzigingenIndex(
        basis_ref=data.get("basis_ref", ""),
        records={rid: _laatste(datums) for rid, datums in (data.get("records") or {}).items()},
        minicursussen={mid: _laatste(datums) for mid, datums in (data.get("minicursussen") or {}).items()},
    )
