"""Extractor voor `justel_html` — Justel HTML-pagina van ejustice.

Gekopieerd uit `tools/etl/convert_justel.py` (parse_justel_html + helpers).
Cleanup en frontmatter zijn NIET hier — die worden in de orchestrator gedaan.

NB: Het oorspronkelijke `convert_justel_html` voegt zelf een frontmatter toe
(make_frontmatter_justel) inclusief een chunk-blok. Wij retourneren alleen de
body; de orchestrator bouwt de frontmatter en injecteert het chunk-blok via
`tools.lib.headings.process_wettekst`.
"""
from __future__ import annotations

# Hergebruik de werkende parser uit het bestaande convert_justel-script.
# We importeren via een relatief sys.path-trucje zodat de logica niet
# gedupliceerd hoeft te worden.
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

# Ondanks dat de filename een hyphen-vrije variant is, importeer
# `tools.etl.convert_justel` rechtstreeks via het etl-subpad.
from etl import convert_justel as _legacy  # type: ignore  # noqa: E402


def extract(cfg: dict, source_name: str) -> str:
    """Haal Justel HTML op, parse, en geef de markdown-body terug (zonder frontmatter)."""
    params = (cfg.get("extract") or {}).get("params") or {}
    source_url = params.get("start_url") or cfg.get("source_url")
    if not source_url:
        raise ValueError(
            f"source_url of extract.params.start_url ontbreekt voor {source_name}"
        )

    html = _legacy.fetch_justel(source_url)
    _wet_naam, _bijgewerkt, body = _legacy.parse_justel_html(html)
    return body
