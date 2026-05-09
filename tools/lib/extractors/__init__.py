"""Extractor-handlers voor de Certificaid bronnen-ETL (ADR-005 §2).

Elke handler heeft signatuur:

    def extract(cfg: dict, source_name: str) -> str

waarbij:
    cfg          = bron-config-dict uit `resources/source_config.yaml`
    source_name  = de YAML-sleutel van de bron

Returntype is altijd een string met de ruwe (eventueel licht voorgestructureerde)
NL-tekst — zonder YAML-frontmatter, en vóór de gedeelde cleanup-pipeline en
heading-injectie. De orchestrator (`tools/etl/convert.py`) voert die stappen
nadien uit.

De registry `METHOD_HANDLERS` mapt `extract.method` (uit YAML) naar de handler.
Onbekende methods krijgen None terug — de orchestrator beslist dan om te
skippen (handcrafted, derived) of een subprocess-fallback te proberen.
"""
from __future__ import annotations

from typing import Callable

from . import (
    custom_wetboek,
    custom_wib92,
    justel_bs_bilingual,
    justel_html,
    pdftotext_ejustice,
)

ExtractFn = Callable[[dict, str], str]

METHOD_HANDLERS: dict[str, ExtractFn] = {
    "pdftotext_ejustice": pdftotext_ejustice.extract,
    "custom_wetboek": custom_wetboek.extract,
    "custom_wib92": custom_wib92.extract,
    "justel_html": justel_html.extract,
    "justel_bs_bilingual": justel_bs_bilingual.extract,
}


def get_handler(method: str) -> ExtractFn | None:
    """Zoek een handler op voor `extract.method`. None → onbekend."""
    return METHOD_HANDLERS.get(method)
