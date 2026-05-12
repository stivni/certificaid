"""Tests voor tools/lib/cbn_advies_html.py."""
from __future__ import annotations

from tools.lib.cbn_advies_html import select_title, _promote_implicit_headings


def test_select_title_strip_commissie_prefix():
    text = (
        "COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN "
        "CBN-advies 2022/15 - Bla bla "
        "Advies van 1 januari 2022"
    )
    result = select_title(text)
    assert "COMMISSIE" not in result
    assert "Advies van" not in result
    assert "CBN-advies 2022/15" in result or "Bla bla" in result


# ─── _promote_implicit_headings — italic standalone heading-promotie ──────────

def test_promote_italic_standalone_long():
    """REGRESSIE-FIX: een lange italic-standalone-regel tussen blank lines
    is een Q&A-titel die als ## heading geprommoveerd moet worden.

    Voorbeeld uit CBN-Q&A-adviezen:
        *Vragen in verband met de vaststelling van de aanschaffingswaarde*
    """
    md = (
        "Body voor.\n"
        "\n"
        "*Vragen in verband met de vaststelling van de aanschaffingswaarde*\n"
        "\n"
        "Body na.\n"
    )
    result = _promote_implicit_headings(md)
    assert "## Vragen in verband met de vaststelling van de aanschaffingswaarde" in result
    assert "*Vragen in verband" not in result  # italic-marker is weg


def test_promote_italic_short_not_promoted():
    """Korte italic (< 20 chars) blijft inline italic — niet promoveren."""
    md = "Body.\n\n*kort*\n\nMeer body.\n"
    result = _promote_implicit_headings(md)
    assert "## kort" not in result
    assert "*kort*" in result


def test_promote_italic_in_paragraph_not_promoted():
    """Italic die NIET tussen lege regels staat (inline emphasis) blijft."""
    md = (
        "Een zin met *emphasis op een woord langer dan twintig chars* in body.\n"
    )
    result = _promote_implicit_headings(md)
    assert "## " not in result


def test_promote_italic_with_trailing_period_not_promoted():
    """Italic met zin-einde-punt is geen heading."""
    md = "\n*Dit is een hele zin die eindigt met een punt.*\n\n"
    result = _promote_implicit_headings(md)
    # Mag niet als heading geprommoveerd worden (heeft zin-einde)
    assert "## Dit is een hele zin" not in result


def test_promote_italic_preserves_legitimate_bold():
    """Bestaande bold-promotie blijft werken (geen regressie)."""
    md = "\n**Boekhoudkundige verwerking**\n\nBody.\n"
    result = _promote_implicit_headings(md)
    assert "## Boekhoudkundige verwerking" in result
