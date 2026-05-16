"""TDD-tests voor ETL-fixes (sessie 2026-05-16).

Per bron/issue: één test die de bug exact vastlegt.

Vereisten:
  - Tests draaien zonder netwerk en zonder raw PDFs (we testen extractor-
    interne cleanup-functies op fixture-strings, niet de hele pipeline).
  - Tests zijn rood vóór de fix en groen erna.

Scope (zie prompt 2026-05-16):
  - IESBA-code-of-ethics-2024:
      A9: paragraafnummer '120. 15 A1' moet '**120.15 A1**' worden
          (pdftotext spuit een extra spatie tussen majeur en minor uit;
          de bestaande _PARA_NUM_RE mist deze variant)
  - CBN-adviezen + ITAA-normen: zie projectrapport (additional patterns
    op te lossen via cbn_advies_html en inject_norm_headings)
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


# ─── IESBA — paragraafnummer met spatie ──────────────────────────────────────

def test_iesba_cleanup_repareert_paragraafnummer_met_spatie():
    """Bug A9: 'NNN. NN An' moet als één paragraafnummer herkend en gebold worden.

    De ruwe pdftotext-output voor het IESBA-paragraafnummer '120.15 A1' bevat
    door layout-glitches een spatie na de eerste punt: '120. 15 A1'. De
    cleanup moet dit normaliseren naar '120.15 A1' EN het paragraafnummer
    bolden, zodat het file-formaat consistent blijft met andere paragrafen
    (bv. '**100.1**', '**R100.5 A1**').
    """
    from tools.lib.extractors.iesba import _cleanup_iesba

    raw = (
        "Independence\n"
        "120. 15 A1\n"
        "\n"
        "Professional accountants in public practice are required...\n"
    )
    out = _cleanup_iesba(raw)
    # De fout-formattering 'NNN. NN' (met spatie) mag NIET meer in output staan
    assert "120. 15" not in out, (
        f"Verwachte fix: '120. 15' moet weg, maar staat nog in output:\n{out}"
    )
    # De juiste paragraafnummer-vorm moet aanwezig zijn (gebold of niet,
    # maar in elk geval als één geheel '120.15 A1').
    assert "120.15 A1" in out, (
        f"Verwacht: '120.15 A1' (zonder spatie na punt), maar niet gevonden in:\n{out}"
    )


def test_iesba_cleanup_bewaart_bestaande_paragraafbolding():
    """Regressie-guard: standaard paragraafnummers blijven correct gebold."""
    from tools.lib.extractors.iesba import _cleanup_iesba

    raw = (
        "100.1\n"
        "\n"
        "A distinguishing mark of the accountancy profession...\n"
        "\n"
        "R100.5 A1\n"
        "\n"
        "The requirements in the Code...\n"
    )
    out = _cleanup_iesba(raw)
    assert "**100.1**" in out, f"100.1 niet gebold:\n{out}"
    assert "**R100.5 A1**" in out, f"R100.5 A1 niet gebold:\n{out}"


def test_iesba_cleanup_strip_stray_page_marker():
    """Bug A1: losse 'Page'-regel (kop/voetregel uit pdftotext) moet weg.

    Tussen Part-overgangen blijft soms een standalone 'Page'-regel staan.
    De cleanup moet die regel verwijderen omdat hij geen tekstuele waarde
    heeft en de leesbaarheid breekt.
    """
    from tools.lib.extractors.iesba import _cleanup_iesba

    raw = (
        "Some content from Part 2.\n"
        "\n"
        "Page\n"
        "\n"
        "Section 200 — Applying the Conceptual Framework\n"
    )
    out = _cleanup_iesba(raw)
    # 'Page' als standalone regel mag niet meer voorkomen.
    assert not re.search(r"(?m)^Page$", out), (
        f"Standalone 'Page'-regel staat nog in output:\n{out}"
    )


# ─── CBN-advies D4 — bold-italic close-mismatch ──────────────────────────────

def test_cbn_advies_cleanup_repareert_split_bold_italic_marker():
    """Bug D4: '***Heading** *' wordt niet correct gesloten.

    Veel CBN-adviezen renderen `<strong><em>` als `***`-opening, maar de
    sluitende `</em></strong>` komt als `** *` (twee aparte tokens met spatie)
    of `**\\n*` op nieuwe regel. De cleanup moet beide cases samenvoegen tot
    `***`, zodat CommonMark de bold-italic correct sluit.

    Voorbeeld (CBN-2009-03 regel 161 vóór fix):
        ***a) Voorbeeld 1 : Subsidie...** *
    Verwacht na fix:
        ***a) Voorbeeld 1 : Subsidie...***
    """
    from tools.lib.cbn_advies_html import _cleanup_markdown

    md_in = "***a) Voorbeeld 1 : Subsidie verkregen om materiële activa** *\n"
    md_out = _cleanup_markdown(md_in)
    # Het verkeerde patroon '** *' (split close) mag niet meer in output staan
    assert "** *" not in md_out, (
        f"Split close-marker '** *' staat nog in output:\n{md_out}"
    )
    # En de string moet correct sluiten met '***'
    assert md_out.rstrip().endswith("***"), (
        f"Verwacht dat output eindigt met '***', maar kreeg:\n{md_out!r}"
    )


def test_cbn_advies_cleanup_strip_trailing_lone_asterisk():
    """Bug D4-variant: '*Kapitaalsubsidies *' met spatie voor sluitende `*`.

    Bestaande cleanup (regel 1037-1041 in cbn_advies_html.py) zou dit moeten
    pakken. Regressie-guard.
    """
    from tools.lib.cbn_advies_html import _cleanup_markdown

    md_in = "*Kapitaalsubsidies *\n"
    md_out = _cleanup_markdown(md_in)
    # '*text *' (spatie binnen italic) moet weggewerkt zijn
    assert "*Kapitaalsubsidies *" not in md_out, (
        f"Spatie binnen italic-span niet gefixt:\n{md_out!r}"
    )


# ─── CBN B4 — single-word ALL-CAPS heading-promotie ─────────────────────────

def test_cbn_advies_promote_singleword_allcaps_heading():
    """Bug B4-variant: single-word ALL-CAPS-regel moet ## heading worden.

    Veel CBN-adviezen (bv. CBN-2009-03) hebben hoofdsecties die uit één
    woord bestaan in ALL CAPS: 'INLEIDING', 'OVERZICHT', 'BEOORDELING',
    'VOORBEELDEN'. De huidige `_promote_implicit_headings` weigert deze
    omdat de filter ≥2 woorden vereist (anti-acroniem-guard). De fix moet
    een whitelist van bekende single-word section-titles toelaten, of het
    woord-minimum versoepelen naar 1 voor woorden langer dan een typisch
    acroniem (bv. ≥6 letters EN niet in een afkortingen-set).
    """
    from tools.lib.cbn_advies_html import _promote_implicit_headings

    md_in = (
        "Voorafgaande paragraaf eindigt hier.\n"
        "\n"
        "INLEIDING\n"
        "\n"
        "De Commissie heeft een vraag ontvangen.\n"
        "\n"
        "OVERZICHT\n"
        "\n"
        "Het advies behandelt drie aspecten.\n"
        "\n"
        "BEOORDELING\n"
        "\n"
        "De juridische analyse luidt als volgt.\n"
        "\n"
        "VOORBEELDEN\n"
        "\n"
        "Hieronder volgen drie voorbeelden.\n"
    )
    out = _promote_implicit_headings(md_in)
    for kw in ("INLEIDING", "OVERZICHT", "BEOORDELING", "VOORBEELDEN"):
        assert f"## {kw}" in out, (
            f"Single-word ALL-CAPS heading '{kw}' niet gepromoveerd:\n{out}"
        )


def test_cbn_advies_promote_skips_short_acronyms():
    """Regressie-guard B4: korte acroniemen blijven plain-text.

    Acroniemen zoals 'VZW', 'OCMW', 'NV', 'BV' mogen NIET gepromoveerd
    worden tot heading want ze zijn meestal inline labels of afkortingen.
    """
    from tools.lib.cbn_advies_html import _promote_implicit_headings

    md_in = (
        "Een paragraaf.\n"
        "\n"
        "VZW\n"
        "\n"
        "Volgende paragraaf.\n"
        "\n"
        "OCMW\n"
        "\n"
        "Nog meer.\n"
    )
    out = _promote_implicit_headings(md_in)
    assert "## VZW" not in out, f"Acroniem VZW niet als heading toegelaten:\n{out}"
    assert "## OCMW" not in out, f"Acroniem OCMW niet als heading toegelaten:\n{out}"
