"""Regressie-tests voor `normalize_artikel_to_art` transformer.

In deze sessie uitgebreid om ook markdown-prefix-varianten te normaliseren:
EU-bronnen (zoals EU-AVG via custom_wetboek) hebben 'Artikel N' al als
markdown-heading `## Artikel 1` in de raw. Voorheen miste de transformer
die omdat hij alleen plain-text `^Artikel N` op kolom 0 herkende.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl.transformers.normalize_artikel_to_art import (  # noqa: E402
    normalize_artikel_to_art,
)


def _run(body: str) -> str:
    out, _ = normalize_artikel_to_art(body, {})
    return out


# ─── Bestaande gedrag: plain-text op kolom 0 ─────────────────────────────────


def test_plain_text_artikel_wordt_naar_art_genormaliseerd():
    """`Artikel 86` op kolom 0 → `Art. 86`."""
    assert _run("Artikel 86\n") == "Art. 86\n"


def test_plain_text_artikel_met_inline_body():
    """`Artikel 46. Tekst...` → `Art. 46\\n\\nTekst...`."""
    out = _run("Artikel 46. Elk kassasysteem moet voorzien zijn van X.\n")
    assert "Art. 46" in out
    assert "Elk kassasysteem moet voorzien zijn van X." in out
    # Heading op eigen regel, body op aparte regel
    assert "Art. 46\n\nElk kassasysteem" in out


def test_indented_artikel_blijft_ongemoeid():
    """Body-tekst met 'Artikel N.' op niet-kolom-0 (geïndenteerd of na chars)
    mag NIET genormaliseerd worden — anders breken we wettekst-citaties.
    """
    assert _run("  Artikel 46 wordt aangepast\n") == "  Artikel 46 wordt aangepast\n"
    assert _run("zie Artikel 46.\n") == "zie Artikel 46.\n"


# ─── REGRESSIE: markdown-prefix variant ──────────────────────────────────────


def test_md_heading_artikel_wordt_genormaliseerd():
    """`## Artikel 1` (markdown-heading) → `Art. 1` (plain).

    Reden: inject_headings_wettekst zet daarna de juiste level op basis van
    detect_hierarchy. Voor EU-AVG (chunk.level=2 voor Artikel) wordt het dan
    `## Art. 1`; voor BE-wetteksten (chunk.level=6) `###### Art. 1`.
    """
    assert _run("## Artikel 1\n") == "Art. 1\n"
    assert _run("###### Artikel 5\n") == "Art. 5\n"


def test_md_heading_artikel_met_punt():
    """`## Artikel 5.` → `Art. 5`."""
    assert _run("## Artikel 5.\n") == "Art. 5\n"


def test_md_heading_artikel_met_inline_body():
    """`## Artikel 46. Tekst...` → `Art. 46\\n\\nTekst...`."""
    out = _run("## Artikel 46. Elk kassasysteem moet voorzien zijn van X.\n")
    assert "Art. 46\n\nElk kassasysteem" in out


def test_md_heading_artikel_slash_nummer():
    """`## Artikel 5/3` (ingelaste sub-artikel) → `Art. 5/3`."""
    assert _run("## Artikel 5/3\n") == "Art. 5/3\n"


def test_md_heading_artikel_bis():
    """`## Artikel 12bis` → `Art. 12bis`."""
    assert _run("## Artikel 12bis\n") == "Art. 12bis\n"


def test_md_heading_andere_woorden_blijven_ongemoeid():
    """`## HOOFDSTUK I` mag niet als Artikel gezien worden."""
    assert _run("## HOOFDSTUK I\n") == "## HOOFDSTUK I\n"


def test_volledige_eu_avg_achtige_input():
    """End-to-end mini-fragment EU-AVG-stijl."""
    body = """# AVG

## HOOFDSTUK I

## Artikel 1

Eerste artikel.

## Artikel 2. Wijze van toepassing.

Tweede artikel.
"""
    out = _run(body)
    # Headings zijn weg, plain Art.
    assert "## Artikel" not in out
    assert "Art. 1" in out
    assert "Art. 2" in out
    # Inline body kreeg eigen regel
    assert "Art. 2\n\nWijze van toepassing." in out
    # HOOFDSTUK ongemoeid
    assert "## HOOFDSTUK I" in out
