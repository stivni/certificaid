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
    cbn_advies,
    custom_wetboek,
    custom_wib92,
    iesba,
    itaa_norm,
    justel_bs_bilingual,
    justel_change_lg,
    justel_html,
    md_passthrough,
    pdftotext_compilatie_btw,
    pdftotext_ejustice,
    pdftotext_narratief,
    pymupdf_wetboek,
)

# Een handler levert ofwel een string (1-op-1 bron→MD) ofwel een
# ``dict[output_path, body_text]`` (compilatie: 1-op-N). De orchestrator
# detecteert het type en handelt schrijven + frontmatter dienovereenkomstig af.
ExtractFn = Callable[[dict, str], "str | dict[str, str]"]

METHOD_HANDLERS: dict[str, ExtractFn] = {
    "pdftotext_ejustice": pdftotext_ejustice.extract,
    "pdftotext_narratief": pdftotext_narratief.extract,
    "custom_wetboek": custom_wetboek.extract,
    "custom_wib92": custom_wib92.extract,
    "iesba": iesba.extract,
    "justel_html": justel_html.extract,
    "justel_change_lg": justel_change_lg.extract,
    "justel_bs_bilingual": justel_bs_bilingual.extract,
    "pdftotext_compilatie_btw": pdftotext_compilatie_btw.extract,
    "cbn_advies": cbn_advies.extract,
    "extract_norm": itaa_norm.extract,
    "pymupdf_wetboek": pymupdf_wetboek.extract,
    "md_passthrough": md_passthrough.extract,
}

# Methodes die een dict retourneren (1-op-N output). De orchestrator gebruikt
# deze set om te beslissen of N losse bestanden moeten worden geschreven.
COMPILATIE_METHODS: set[str] = {"pdftotext_compilatie_btw"}


def get_handler(method: str) -> ExtractFn | None:
    """Zoek een handler op voor `extract.method`. None → onbekend."""
    return METHOD_HANDLERS.get(method)
