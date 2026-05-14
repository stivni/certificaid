"""
Tests voor `tools/etl/transformers/strip_itaa_norm_footers.py`.

Dekt zowel de bestaande patronen als de uitbreiding voor:
  1. Standalone paginanummers (regel met enkel een getal, omringd door witregels).
  2. Variant-footers zonder ©-symbool (`ITAA – Norm ...`).
  3. Standalone `Inhoud`-headers die als pagina-residu van een TOC overblijven.

False-positive-bescherming:
  - genummerde opsommingen (`1° de regel ...`, `1. iets`, `1) iets`) blijven.
  - getallen in tabelrijen / inline tekst blijven.
  - bona-fide kopjes met het woord 'Inhoud' (bv. `## Inhoud van de opdracht`)
    blijven onaangetast.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl.transformers.strip_itaa_norm_footers import (  # noqa: E402
    strip_itaa_norm_footers,
)


def _run(body: str) -> str:
    new, _ = strip_itaa_norm_footers(body, {})
    return new


# ─── Bestaande patronen (regression-vangnet) ─────────────────────────────────

class TestBestaandePatronen:
    def test_strip_copyright_footer_met_copyright_symbool(self):
        body = (
            "Normale tekst over permanente vorming.\n"
            "© ITAA – Norm permanente vorming p. 3\n"
            "Meer tekst hierna.\n"
        )
        out = _run(body)
        assert "© ITAA" not in out
        assert "Normale tekst" in out
        assert "Meer tekst" in out

    def test_strip_goedgekeurd_hreb_footer(self):
        body = (
            "Inleiding van het document.\n"
            "Goedgekeurd HREB (2024-03-15)- ter goedkeuring van de minister voorgelegd 3/47\n"
            "Volgende paragraaf.\n"
        )
        out = _run(body)
        assert "Goedgekeurd HREB" not in out
        assert "Inleiding" in out

    def test_strip_heading_met_pagina_marker(self):
        body = (
            "Tekst.\n"
            "## VERZOEK TOT GOEDKEURING OKTOBER 2025 64/64\n"
            "Andere tekst.\n"
        )
        out = _run(body)
        assert "VERZOEK TOT GOEDKEURING" not in out


# ─── Nieuwe patronen — POSITIVE cases ────────────────────────────────────────

class TestStandalonePaginaNummers:
    def test_strip_bare_paginanummer_tussen_witregels(self):
        # Page-noise: een digit op een eigen regel, omringd door witregels.
        body = (
            "Einde van pagina één met een zin.\n"
            "\n"
            "1\n"
            "\n"
            "Begin van pagina twee.\n"
        )
        out = _run(body)
        assert "\n1\n" not in out
        assert "Einde van pagina één" in out
        assert "Begin van pagina twee" in out

    def test_strip_meerdere_paginanummers_in_zelfde_body(self):
        body = (
            "Pagina A.\n"
            "\n"
            "1\n"
            "\n"
            "Pagina B.\n"
            "\n"
            "2\n"
            "\n"
            "Pagina C.\n"
            "\n"
            "12\n"
            "\n"
            "Pagina D.\n"
        )
        out = _run(body)
        # Drie standalone paginanummers moeten weg zijn.
        for marker in ("\n1\n", "\n2\n", "\n12\n"):
            assert marker not in out
        assert "Pagina A" in out and "Pagina D" in out

    def test_strip_paginanummer_met_voorloop_whitespace(self):
        # pdftotext -layout laat soms whitespace staan voor het cijfer.
        body = (
            "Vorige paragraaf.\n"
            "\n"
            "    3\n"
            "\n"
            "Volgende paragraaf.\n"
        )
        out = _run(body)
        assert "Vorige paragraaf" in out
        assert "Volgende paragraaf" in out
        # De standalone '3' (met of zonder spaces) hoort weg
        for ln in out.split("\n"):
            assert ln.strip() != "3"


class TestVariantFootersZonderCopyrightSymbol:
    def test_strip_itaa_dash_norm_zonder_copyright(self):
        body = (
            "Inhoudelijke tekst.\n"
            "ITAA – Norm permanente vorming p. 5\n"
            "Volgende zin.\n"
        )
        out = _run(body)
        # Het footer-residu zonder © hoort eruit.
        assert "ITAA – Norm permanente vorming" not in out
        assert "Inhoudelijke tekst" in out
        assert "Volgende zin" in out

    def test_strip_itaa_dash_met_voorloop_whitespace(self):
        body = (
            "Para.\n"
            "    ITAA – Norm domiciliëring van vennootschappen\n"
            "Vervolg.\n"
        )
        out = _run(body)
        assert "ITAA – Norm domic" not in out
        assert "Para." in out
        assert "Vervolg." in out


class TestStandaloneInhoudHeader:
    def test_strip_inhoud_als_standalone_regel(self):
        # Pagina-residu uit TOC-pagina: enkel 'Inhoud' op een eigen regel
        body = (
            "## OPDRACHTBRIEF\n"
            "\n"
            "Inhoud\n"
            "\n"
            "Alhoewel de verplichting om een opdrachtbrief af te sluiten...\n"
        )
        out = _run(body)
        # 'Inhoud' op zichzelf moet weg
        assert not any(ln.strip() == "Inhoud" for ln in out.split("\n"))
        assert "Alhoewel de verplichting" in out

    def test_strip_inhoud_met_voorloop_whitespace(self):
        body = (
            "Eerste paragraaf.\n"
            "\n"
            "    Inhoud\n"
            "\n"
            "Tweede paragraaf.\n"
        )
        out = _run(body)
        assert not any(ln.strip() == "Inhoud" for ln in out.split("\n"))
        assert "Eerste paragraaf" in out
        assert "Tweede paragraaf" in out


# ─── Nieuwe patronen — NEGATIVE cases (false-positive-bescherming) ───────────

class TestFalsePositiveBescherming:
    def test_behoud_genummerde_opsomming_met_graden(self):
        # '1° de regel ...' is een typische juridische opsomming en mag niet weg.
        body = (
            "De beroepsbeoefenaar voldoet aan:\n"
            "1° de eis van permanente vorming;\n"
            "2° de eis van onafhankelijkheid.\n"
        )
        out = _run(body)
        assert "1° de eis" in out
        assert "2° de eis" in out

    def test_behoud_genummerde_opsomming_met_punt(self):
        # '1. iets' moet blijven — niet ge-strippt als paginanummer.
        body = (
            "Stappen:\n"
            "1. Verzamel documenten\n"
            "2. Controleer volledigheid\n"
        )
        out = _run(body)
        assert "1. Verzamel documenten" in out
        assert "2. Controleer volledigheid" in out

    def test_behoud_inline_cijfer_in_zin(self):
        # Cijfer in een zin moet blijven.
        body = (
            "Het lid moet minstens 40 uur per jaar volgen.\n"
            "Bij overschrijding is 1 sanctie van toepassing.\n"
        )
        out = _run(body)
        assert "minstens 40 uur" in out
        assert "1 sanctie" in out

    def test_behoud_heading_met_inhoud_in_titel(self):
        # Bona-fide heading 'Inhoud van de opdracht' mag niet weg.
        body = (
            "## Inhoud van de opdracht\n"
            "\n"
            "De opdracht omvat ...\n"
            "\n"
            "### Inhoud en draagwijdte\n"
            "\n"
            "Tekst.\n"
        )
        out = _run(body)
        assert "## Inhoud van de opdracht" in out
        assert "### Inhoud en draagwijdte" in out

    def test_behoud_itaa_woord_in_normale_zin(self):
        # 'ITAA' in een normale zin (zonder dash + footer-vorm) mag niet weg.
        body = (
            "Het ITAA is het instituut voor accountants.\n"
            "Het ITAA – het Instituut – heeft een rol in toezicht.\n"
        )
        out = _run(body)
        assert "Het ITAA is het instituut" in out
        # Tweede regel bevat een em-dash gebruikt als inline-haakje, niet als footer.
        # Footer-detectie vereist dat na de em-dash een herkenbare footer-vorm
        # ('Norm ...', een paginanummer of vergelijkbaar) volgt.
        assert "Het ITAA – het Instituut" in out
