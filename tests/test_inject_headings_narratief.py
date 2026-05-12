"""
Unit-tests voor inject_headings_narratief (tools/etl/transformers/).

Klasse: TestInjectHeadingsNarratief

Dekt:
  - Patroon A: Vak [Roman] - titel (PB-toelichtingen)
  - Patroon B: HOOFDSTUK N alleen op de regel + volgende regel als titel
  - Patroon C: Roman chapter met 1 spatie (belastinggids)
  - Patroon D: ALL-CAPS col-0, omsloten door lege regels (VenB)
  - Patroon E: ingesprongen ALLCAPS + lege regels (VenB VAK - / BANKINFORMATIE)
  - No-op gevallen (TOC-leider-regels, reeds headings, gewone tekst)
  - Idempotentie
  - Valse positieven vermijden
  - Lege body
  - Frontmatter ongewijzigd
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl.transformers.inject_headings_narratief import inject_headings_narratief  # noqa: E402
from tools.etl.transformers import TRANSFORMERS  # noqa: E402


class TestInjectHeadingsNarratief:
    """Tests voor de inject_headings_narratief-transformer."""

    # ─── Patroon A: Vak [Roman] - titel (PB-toelichtingen) ───────────────────

    def test_vak_roman_basis(self):
        """'    Vak I - BANKREKENING EN TELEFOONNUMMER(S)' → '## Vak I - BANKREKENING...'"""
        body = "    Vak I - BANKREKENING EN TELEFOONNUMMER(S)\n\nTekst."
        result, _ = inject_headings_narratief(body, {})
        assert "## Vak I - BANKREKENING EN TELEFOONNUMMER(S)" in result

    def test_vak_roman_meerdere(self):
        """Meerdere Vak-secties worden allemaal geconverteerd."""
        body = (
            "    Vak I - BANKREKENING EN TELEFOONNUMMER(S)\n"
            "\n"
            "Tekst 1.\n"
            "\n"
            "    Vak II - PERSOONLIJKE GEGEVENS EN GEZINSLASTEN\n"
            "\n"
            "Tekst 2.\n"
        )
        result, _ = inject_headings_narratief(body, {})
        assert "## Vak I - BANKREKENING EN TELEFOONNUMMER(S)" in result
        assert "## Vak II - PERSOONLIJKE GEGEVENS EN GEZINSLASTEN" in result

    def test_vak_roman_met_haakjes(self):
        """Vak-titel met haakjes wordt correct geconverteerd."""
        body = "    Vak X - (UITGAVEN DIE RECHT GEVEN OP) BELASTINGVERMINDERINGEN\n\nTekst."
        result, _ = inject_headings_narratief(body, {})
        assert "## Vak X - (UITGAVEN DIE RECHT GEVEN OP) BELASTINGVERMINDERINGEN" in result

    def test_vak_roman_geen_paginanummer_in_heading(self):
        """Trailing paginanummer wordt verwijderd uit de Vak-heading."""
        body = "    Vak I - BANKREKENING 9\n\nTekst."
        result, _ = inject_headings_narratief(body, {})
        # Paginanummer hoort weg te zijn
        assert "## Vak I - BANKREKENING" in result
        heading_line = [l for l in result.split("\n") if l.startswith("## Vak I")][0]
        assert not heading_line.endswith("9")

    # ─── Patroon B: HOOFDSTUK N solo (fiscaal-memento) ───────────────────────

    def test_hoofdstuk_solo_met_volgende_regel(self):
        """' HOOFDSTUK 1' + volgende regel als titel → '## HOOFDSTUK 1 — DE PERSONENBELASTING...'"""
        body = " HOOFDSTUK 1\nDE PERSONENBELASTING (PB)\nBijgewerkt op 31.12.2024\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## HOOFDSTUK 1 — DE PERSONENBELASTING (PB)" in result

    def test_hoofdstuk_roman_numeral(self):
        """' HOOFDSTUK II' met Roman numeral → correct heading."""
        body = " HOOFDSTUK II\nVENNOOTSCHAPSBELASTING (VEN.B)\nTekst.\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## HOOFDSTUK II — VENNOOTSCHAPSBELASTING (VEN.B)" in result

    def test_hoofdstuk_toc_lijn_niet_geconverteerd(self):
        """TOC-lijn 'HOOFDSTUK 1 DE PERSONENBELASTING ......... 24' (geen leading space) → onveranderd."""
        body = "HOOFDSTUK 1 DE PERSONENBELASTING (PB) ...... 24\nTekst.\n"
        result, _ = inject_headings_narratief(body, {})
        # Geen heading aangemaakt voor TOC-lijn
        assert "## HOOFDSTUK" not in result

    # ─── Patroon C: Roman chapter (belastinggids) ─────────────────────────────

    def test_roman_chapter_met_leading_space(self):
        """' II Belasting en het gezin' → '## II Belasting en het gezin'."""
        body = " II Belasting en het gezin\n\nTekst over belasting.\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## II Belasting en het gezin" in result

    def test_roman_chapter_met_vraagteken(self):
        """' V Niet akkoord met de fiscus?' → heading."""
        body = " V Niet akkoord met de fiscus?\n\nTekst.\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## V Niet akkoord met de fiscus?" in result

    def test_roman_chapter_toc_met_dots_niet_geconverteerd(self):
        """TOC-lijn 'I Woord vooraf......... 9' (geen leading space, met dots) → onveranderd."""
        body = "I Woord vooraf.................................................................................................................................................................................. 9\nTekst.\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## I Woord vooraf" not in result

    def test_roman_chapter_toc_met_paginanummer_niet_geconverteerd(self):
        """' II Belasting en het gezin.... 11' (dots + paginanummer) → onveranderd."""
        body = " II Belasting en het gezin.......................................................................................................................................................... 11\nTekst.\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## II Belasting en het gezin" not in result

    # ─── Patroon D: ALL-CAPS col-0, omsloten door lege regels (VenB) ─────────

    def test_allcaps_col0_standalone(self):
        """'VOORAFGAANDE OPMERKINGEN' omsloten door lege regels → ## heading."""
        body = "Tekst daarvoor.\n\nVOORAFGAANDE OPMERKINGEN\n\nTekst erna.\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## VOORAFGAANDE OPMERKINGEN" in result

    def test_allcaps_col0_gebruikte_afkortingen(self):
        """'GEBRUIKTE AFKORTINGEN' → ## heading."""
        body = "\nGEBRUIKTE AFKORTINGEN\n\nTekst.\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## GEBRUIKTE AFKORTINGEN" in result

    def test_allcaps_col0_niet_omsloten_door_blanks(self):
        """ALL-CAPS regel die NIET omsloten is door lege regels → onveranderd."""
        body = "Vorige lijn.\nALGEMENE OPMERKINGEN\nVolgende lijn.\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## ALGEMENE OPMERKINGEN" not in result

    def test_allcaps_col0_te_kort_niet_geconverteerd(self):
        """ALL-CAPS regel korter dan 8 chars + spaties → onveranderd (te kort voor heading)."""
        body = "\nKORT\n\nTekst.\n"
        result, _ = inject_headings_narratief(body, {})
        # 'KORT' is 4 chars, niet lang genoeg
        assert "## KORT" not in result

    # ─── Patroon E: ingesprongen ALLCAPS, omsloten door lege regels (VenB) ───

    def test_vak_min_sectie(self):
        """'    VAK - RESERVES' omsloten door lege regels → ## heading (patroon E)."""
        body = "Vorige tekst.\n\n    VAK - RESERVES\n\nA. Belastbare gereserveerde winst\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## VAK - RESERVES" in result

    def test_vak_min_col0(self):
        """'VAK - RESERVES' op kolom 0 (VenB-stijl, geen omsluitende lege regels) → ## heading."""
        body = "Vorige tekst.\n\nVAK - RESERVES\nA. Belastbare gereserveerde winst\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## VAK - RESERVES" in result

    def test_vak_min_col0_met_continuatie(self):
        """'VAK - TEKST' met ALLCAPS-vervolgregel → samengevoegde heading."""
        body = "Vorige.\n\nVAK - BIJZONDERE AANSLAGEN MET BETREKKING TOT\nVERRICHTINGEN DIE VOOR\nA. Tekst.\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## VAK - BIJZONDERE AANSLAGEN MET BETREKKING TOT VERRICHTINGEN DIE VOOR" in result

    def test_bankinformatie_ingesprongen(self):
        """'    BANKINFORMATIE' omsloten door lege regels → ## heading."""
        body = "Vorige tekst.\n\n    BANKINFORMATIE\n\nIn dit vak mag niets worden ingevuld.\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## BANKINFORMATIE" in result

    def test_vak_min_niet_omsloten_niet_geconverteerd(self):
        """'    VAK - TEXT' zonder omsluitende lege regels → onveranderd."""
        body = "Vorige tekst.\n    VAK - RESERVES\nVolgende tekst.\n"
        result, _ = inject_headings_narratief(body, {})
        assert "## VAK - RESERVES" not in result

    # ─── No-op gevallen ───────────────────────────────────────────────────────

    def test_bestaande_heading_ongewijzigd(self):
        """Regels die al met ## beginnen worden overgeslagen."""
        body = "## Bestaande heading\n\nTekst.\n"
        result, _ = inject_headings_narratief(body, {})
        assert result == body

    def test_normale_tekst_ongewijzigd(self):
        """Gewone body-tekst wordt niet aangeraakt."""
        body = "Dit is normale tekst.\nMeer tekst.\n"
        result, _ = inject_headings_narratief(body, {})
        assert result == body

    def test_lege_body(self):
        """Lege body geeft lege body terug."""
        result, fm = inject_headings_narratief("", {})
        assert result == ""
        assert fm == {}

    # ─── Idempotentie ─────────────────────────────────────────────────────────

    def test_idempotent_vak(self):
        """Tweede run op reeds-geconverteerde Vak-heading verandert niets."""
        body = "    Vak I - BANKREKENING EN TELEFOONNUMMER(S)\n\nTekst."
        result1, _ = inject_headings_narratief(body, {})
        result2, _ = inject_headings_narratief(result1, {})
        assert result1 == result2

    def test_idempotent_allcaps(self):
        """Tweede run op reeds-geconverteerde ALL-CAPS heading verandert niets."""
        body = "Tekst.\n\nVOORAFGAANDE OPMERKINGEN\n\nVolgende tekst.\n"
        result1, _ = inject_headings_narratief(body, {})
        result2, _ = inject_headings_narratief(result1, {})
        assert result1 == result2

    # ─── Frontmatter ongewijzigd ──────────────────────────────────────────────

    def test_frontmatter_niet_gewijzigd(self):
        """Frontmatter-dict wordt niet aangepast door de transformer."""
        fm = {"wet": "Toelichting PB", "tags": ["2.2"], "_cleanup_steps": []}
        body = " I Woord vooraf\n\nTekst.\n"
        _, result_fm = inject_headings_narratief(body, fm)
        assert result_fm == fm

    # ─── Valse positieven vermijden ───────────────────────────────────────────

    def test_geen_heading_bij_toc_vak_met_paginanummer(self):
        """'VAK I - BANKREKENING EN TELEFOONNUMMER(S) 9' (col 0, met pagina) → onveranderd."""
        # In de TOC staan VAK-regels op kolom 0 met paginanummer; die moeten NIET
        # als heading worden gemarkeerd.
        body = "VAK I - BANKREKENING EN TELEFOONNUMMER(S) 9\n\nTekst.\n"
        result, _ = inject_headings_narratief(body, {})
        # Patroon A vereist leading whitespace (1-4 spaties); col-0 → geen match
        assert "## Vak I" not in result
        assert "## VAK I" not in result

    def test_geen_heading_bij_korte_roman_zonder_leading_space(self):
        """'II Belasting en het gezin' (zonder leading space) → onveranderd."""
        body = "II Belasting en het gezin\n\nTekst.\n"
        result, _ = inject_headings_narratief(body, {})
        # Patroon C vereist precies 1 leading space
        assert "## II Belasting" not in result

    # ─── Registratie in TRANSFORMERS ─────────────────────────────────────────

    def test_geregistreerd_in_transformers(self):
        """inject_headings_narratief moet in TRANSFORMERS-registry zitten."""
        assert "inject_headings_narratief" in TRANSFORMERS
