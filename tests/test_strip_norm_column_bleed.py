"""Tests voor strip_norm_column_bleed transformer.

Doel: artefacten uit tweekoloms-PDF-extractie in ITAA-normen wegfilteren.
- Pattern 1: standalone ``## VEREISTEN TOEPASSINGSMODALITEITEN`` (gemergde
  kolomtitels, pure boilerplate) → volledig strippen.
- Pattern 2: compound heading met trailing ``VEREISTEN TOEPASSINGSMODALITEITEN``
  → trailing column-bleed strippen, echte NL-heading behouden.
- Pattern 3: bilingue NL+FR heading (NL-tekst gevolgd door FR-tekst)
  → FR-deel strippen.
- Pattern 4: pure FR-heading (alle woorden FR) → volledig strippen.

NEGATIVE: legitieme NL-headings zonder bleed-marker blijven ongemoeid.
"""
from __future__ import annotations


class TestStripStandaloneVereistenToepassingsmodaliteiten:
    """Pattern 1: ``## VEREISTEN TOEPASSINGSMODALITEITEN`` solo → strippen."""

    def test_standalone_heading_wordt_gestript(self):
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = (
            "## Toepassingsgebied\n"
            "\n"
            "## VEREISTEN TOEPASSINGSMODALITEITEN\n"
            "\n"
            "1. Onderhavige norm is van toepassing op...\n"
        )
        result, _ = strip_norm_column_bleed(body, {})
        assert "VEREISTEN TOEPASSINGSMODALITEITEN" not in result
        # Echte heading erboven blijft staan.
        assert "## Toepassingsgebied" in result
        # Body-tekst eronder blijft staan.
        assert "1. Onderhavige norm" in result

    def test_meerdere_standalone_headings_allemaal_gestript(self):
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = (
            "## VEREISTEN TOEPASSINGSMODALITEITEN\n"
            "tekst 1\n"
            "## VEREISTEN TOEPASSINGSMODALITEITEN\n"
            "tekst 2\n"
        )
        result, _ = strip_norm_column_bleed(body, {})
        assert "VEREISTEN TOEPASSINGSMODALITEITEN" not in result
        assert "tekst 1" in result
        assert "tekst 2" in result


class TestStripCompoundVereistenToepassingsmodaliteiten:
    """Pattern 2: ``## <heading> VEREISTEN TOEPASSINGSMODALITEITEN`` → trailing strippen."""

    def test_compound_heading_behoudt_NL_deel(self):
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = "## II.2. Aard van de opdracht VEREISTEN TOEPASSINGSMODALITEITEN\n"
        result, _ = strip_norm_column_bleed(body, {})
        assert "## II.2. Aard van de opdracht" in result
        assert "VEREISTEN TOEPASSINGSMODALITEITEN" not in result

    def test_compound_heading_met_subsection(self):
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = (
            "## II. Algemene bepalingen die van toepassing zijn op alle "
            "verrichtingen II.1. Deontologische beginselen VEREISTEN TOEPASSINGSMODALITEITEN\n"
        )
        result, _ = strip_norm_column_bleed(body, {})
        assert "## II. Algemene bepalingen" in result
        assert "II.1. Deontologische beginselen" in result
        assert "VEREISTEN TOEPASSINGSMODALITEITEN" not in result


class TestStripBilingueHeadings:
    """Pattern 3: ``## NL-tekst FR-tekst`` → FR-deel strippen."""

    def test_aanvaarding_acceptation(self):
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = "## Aanvaarding van opdrachten Acceptation de missions\n"
        result, _ = strip_norm_column_bleed(body, {})
        assert "## Aanvaarding van opdrachten" in result
        assert "Acceptation" not in result
        assert "missions" not in result

    def test_documentatie_documentation(self):
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = "## Documentatie Documentation\n"
        result, _ = strip_norm_column_bleed(body, {})
        assert "## Documentatie" in result
        assert "Documentation" not in result


class TestStripPureFrenchHeadings:
    """Pattern 4: heading bestaat enkel uit FR-woorden (kolom-bleed-rest) → strippen."""

    def test_fin_des_relations_clients_volledig_gestript(self):
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = (
            "Beëindigen van cliëntenrelaties\n"
            "\n"
            "## Fin des relations clients\n"
            "\n"
            "demande.\n"
        )
        result, _ = strip_norm_column_bleed(body, {})
        assert "Fin des relations clients" not in result
        # Omliggende body-tekst blijft.
        assert "Beëindigen van cliëntenrelaties" in result
        assert "demande." in result


class TestNegativeCasesGeenWijziging:
    """Legitieme headings zonder bleed-marker moeten ongemoeid blijven."""

    def test_echte_vereisten_heading_blijft(self):
        """`## VEREISTEN` zonder TOEPASSINGSMODALITEITEN is een echte heading."""
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = "## VEREISTEN\n\nDe beroepsbeoefenaar dient...\n"
        result, _ = strip_norm_column_bleed(body, {})
        assert result == body

    def test_echte_toepassingsmodaliteiten_heading_blijft(self):
        """`## TOEPASSINGSMODALITEITEN` standalone is ook geen bleed."""
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = "## TOEPASSINGSMODALITEITEN\n\nWanneer van toepassing...\n"
        result, _ = strip_norm_column_bleed(body, {})
        assert result == body

    def test_aanvaarding_zonder_fr_blijft(self):
        """`## Aanvaarding van opdrachten` zonder FR-bleed blijft ongemoeid."""
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = "## Aanvaarding van opdrachten\n\nHet kantoor richt zijn systeem in...\n"
        result, _ = strip_norm_column_bleed(body, {})
        assert result == body

    def test_documentatie_zonder_fr_blijft(self):
        """`## Documentatie` zonder Documentation blijft."""
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = "## Documentatie\n\nHet kantoor dient documentatie...\n"
        result, _ = strip_norm_column_bleed(body, {})
        assert result == body

    def test_normale_body_tekst_blijft(self):
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = (
            "## 1. Algemene bepalingen\n"
            "\n"
            "De beroepsbeoefenaar past de normen toe.\n"
            "Dit geldt voor alle opdrachten.\n"
        )
        result, _ = strip_norm_column_bleed(body, {})
        assert result == body

    def test_vereisten_in_body_niet_in_heading_blijft(self):
        """`VEREISTEN TOEPASSINGSMODALITEITEN` als body-tekst (geen ##) blijft."""
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = "De afdeling VEREISTEN TOEPASSINGSMODALITEITEN bevat de regels.\n"
        result, _ = strip_norm_column_bleed(body, {})
        assert result == body


class TestIdempotency:
    """Twee maal toepassen geeft hetzelfde resultaat."""

    def test_idempotent_op_gemixte_input(self):
        from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
        body = (
            "## Toepassingsgebied\n"
            "\n"
            "## VEREISTEN TOEPASSINGSMODALITEITEN\n"
            "\n"
            "## II.2. Aard van de opdracht VEREISTEN TOEPASSINGSMODALITEITEN\n"
            "\n"
            "## Aanvaarding van opdrachten Acceptation de missions\n"
            "\n"
            "## Fin des relations clients\n"
            "\n"
            "tekst.\n"
        )
        once, _ = strip_norm_column_bleed(body, {})
        twice, _ = strip_norm_column_bleed(once, {})
        assert once == twice


class TestRegistratie:
    def test_geregistreerd_in_TRANSFORMERS(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "strip_norm_column_bleed" in TRANSFORMERS
