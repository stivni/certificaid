"""Minimale unit-tests voor `tools.lib.normen_extractie`.

Doel: aantonen dat de publieke API correct is opgehangen aan de bestaande
ETL-helpers. Geen end-to-end PDF-tests (die vereisen pymupdf + bronbestanden).
"""
from __future__ import annotations

import pytest

from tools.lib.normen_extractie import (
    _is_likely_french_line,
    fix_norm_artefacts,
    inject_norm_headings,
)


def test_is_likely_french_line():
    """FR-regels worden herkend; NL-regels met losse accent-letters niet."""
    if _is_likely_french_line is None:
        pytest.skip("_is_likely_french_line niet geexporteerd in lib")

    # Duidelijk Franse regels
    assert _is_likely_french_line("La présente norme est applicable")
    assert _is_likely_french_line("Le commissaire vérifie les documents")

    # NL-regels mogen niet als FR worden geflagd
    assert not _is_likely_french_line(
        "De beroepsbeoefenaar moet de opdracht schriftelijk bevestigen"
    )
    assert not _is_likely_french_line("Een geactualiseerd kwaliteitssysteem")


def test_inject_norm_headings_promoot_genummerde_sectie():
    """Een genummerde sectie aan kolom 0 wordt naar ## gepromoot."""
    body = "Inleiding tekst.\n\n1. Toepassingsgebied\n\nDeze norm is van toepassing.\n"
    new, n = inject_norm_headings(body)
    assert "## 1. Toepassingsgebied" in new
    assert n >= 1


def test_fix_norm_artefacts_verwijdert_form_feed():
    """Form-feed characters worden verwijderd; descriptions bevat note."""
    body = "voor\n\x0c\nna"
    new, fixes = fix_norm_artefacts(body)
    assert "\x0c" not in new
    # Tenminste de form-feed-fix moet hebben aangeslagen.
    assert any("form-feed" in note.lower() for note in fixes), fixes
