"""Smoketests voor de in-process ETL-orchestrator (`tools/etl/convert.py`).

Doel: verifiëren dat de orchestrator
  1. de juiste extractor-handler oproept,
  2. cleanup + heading-injection draait,
  3. een staging-MD met geldige frontmatter (chunk + provenance) schrijft,
  4. idempotent is (modulo `provenance.generated_at`).

We mocken de extractie zodat deze tests geen raw PDFs nodig hebben — die zitten
in `resources/raw/wetteksten/` en die map is gitignored. Apart daarvan voegen
we één optionele integration-test toe (skipped als de raw PDF ontbreekt) zodat
ontwikkelaars met de PDFs lokaal de volledige keten kunnen valideren voor
minimaal één ejustice-bron en één wetboek-bron.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from unittest import mock

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl import convert as orchestrator  # noqa: E402
from tools.lib import extractors  # noqa: E402


# ─── Test 1: orchestrator-pipeline met gemockte ejustice-extractor ────────────

# Realistische mini-input die op de output van pdftotext_ejustice lijkt:
# een paar HOOFDSTUK/AFDELING-headings + Art.-blokken.
_FAKE_EJUSTICE_BODY = """\
Inhoudstafel
Art. 1-3
Tekst
HOOFDSTUK 1. - Algemene bepalingen

Art. 1.  Voor de toepassing van deze testwet wordt verstaan onder accountant
de persoon ingeschreven in het openbaar register.

AFDELING 1. - Toetreding

Art. 2.  De toetreding gebeurt op basis van een aanvraag bij het Instituut.

Art. 3.  De aanvraag bevat alle bewijsstukken bedoeld in artikel 2.
"""


def _make_test_cfg(method: str = "pdftotext_ejustice") -> dict:
    """Bouw een minimale source-config-dict voor de orchestrator."""
    return {
        "bron_rol": "itaa_lex",
        "raw": "resources/raw/wetteksten/Test.pdf",
        "output": "resources/bronnen/wetteksten/Test.md",
        "itaa_sectie": "TEST",
        "tags": ["TEST", "smoke"],
        "bijgewerkt": "01.01.2026",
        "wet": "Test-wet 1 januari 2026 voor smoketests",
        "status": "volledig",
        "extract": {"method": method},
    }


def test_ejustice_pipeline_writes_staging_md_with_chunk_and_provenance(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """End-to-end: ejustice-extractie → cleanup → headings → frontmatter → staging."""
    # 1. Stub de extractor en config
    fake_cfg = _make_test_cfg("pdftotext_ejustice")
    monkeypatch.setattr(
        orchestrator, "load_config", lambda: {"TestBron": fake_cfg},
    )
    fake_handler = mock.Mock(return_value=_FAKE_EJUSTICE_BODY)
    monkeypatch.setattr(orchestrator, "get_handler", lambda m: fake_handler)

    # 2. Verleg staging-folder zodat we niet in de echte data/ schrijven
    monkeypatch.setattr(orchestrator, "STAGING_DIR", tmp_path)

    # 3. Stub provenance — maakt geen raw-PDF verplicht
    monkeypatch.setattr(orchestrator, "_attach_provenance", lambda *a, **kw: None)

    out = orchestrator.convert_one("TestBron")
    assert out is not None
    assert out.exists()

    text = out.read_text(encoding="utf-8")

    # Frontmatter aanwezig en uniek
    assert text.count("\n---\n") >= 1
    assert text.startswith("---\n")

    # Bron-velden uit cfg landen in frontmatter
    assert 'wet: "Test-wet 1 januari 2026 voor smoketests"' in text
    assert 'itaa-lex-sectie: "TEST"' in text
    assert 'bron_rol: "itaa_lex"' in text

    # Chunk-blok ingevoegd door process_wettekst
    assert re.search(r"^chunk:\s*$", text, re.MULTILINE) is not None
    assert re.search(r"^\s+level:\s+\d+\s*$", text, re.MULTILINE) is not None
    assert re.search(r'^\s+type:\s+"Art\."', text, re.MULTILINE) is not None

    # H1 wet-naam aanwezig (na frontmatter)
    assert re.search(r"^# Test-wet", text, re.MULTILINE) is not None

    # Artikel-headings op het correcte niveau (Art. = laagste rank)
    art_headings = re.findall(r"^(#+) Art\. ", text, re.MULTILINE)
    assert art_headings, "geen artikel-headings gevonden"
    # Alle articles op hetzelfde niveau
    assert len(set(art_headings)) == 1, f"mixed art levels: {art_headings}"

    # Structurele headings — minstens AFDELING moet als heading geïnjecteerd zijn.
    assert re.search(r"^(#+) AFDELING 1", text, re.MULTILINE) is not None


def test_orchestrator_skips_handcrafted_method(monkeypatch: pytest.MonkeyPatch) -> None:
    """Bronnen met methode `handcrafted` worden geskipped (geen output)."""
    cfg = _make_test_cfg("handcrafted")
    monkeypatch.setattr(orchestrator, "load_config", lambda: {"X": cfg})
    out = orchestrator.convert_one("X", dry_run=True)
    assert out is None


def test_orchestrator_skips_derived_method(monkeypatch: pytest.MonkeyPatch) -> None:
    """Bronnen met methode `derived` worden geskipped (fase B2 vervangt deze)."""
    cfg = _make_test_cfg("derived")
    monkeypatch.setattr(orchestrator, "load_config", lambda: {"X": cfg})
    out = orchestrator.convert_one("X", dry_run=True)
    assert out is None


# ─── Test 2: idempotentie (modulo generated_at) ────────────────────────────────

def test_pipeline_is_idempotent_modulo_generated_at(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Twee runs achter elkaar produceren identieke output, behalve provenance.generated_at."""
    fake_cfg = _make_test_cfg("pdftotext_ejustice")
    monkeypatch.setattr(orchestrator, "load_config", lambda: {"TestBron": fake_cfg})
    monkeypatch.setattr(orchestrator, "get_handler", lambda m: lambda *a, **kw: _FAKE_EJUSTICE_BODY)
    monkeypatch.setattr(orchestrator, "STAGING_DIR", tmp_path)
    monkeypatch.setattr(orchestrator, "_attach_provenance", lambda *a, **kw: None)

    out1 = orchestrator.convert_one("TestBron")
    text1 = out1.read_text(encoding="utf-8")

    out2 = orchestrator.convert_one("TestBron")
    text2 = out2.read_text(encoding="utf-8")

    # Zonder provenance is alles identiek
    assert text1 == text2


# ─── Test 3: registry compleet voor de B1-scope ────────────────────────────────

def test_registry_has_all_b1_methods() -> None:
    """ADR-005 §2: minstens deze 5 methodes moeten in-process gerouteerd zijn."""
    expected = {
        "pdftotext_ejustice",
        "custom_wetboek",
        "custom_wib92",
        "justel_html",
        "justel_bs_bilingual",
    }
    assert expected.issubset(extractors.METHOD_HANDLERS.keys())


# ─── Test 4 (optioneel): integration met echte raw PDF voor één wetboek ───────

_WETBOEK_INTEGRATION_TARGET = "WBTW"
_RAW_WETBOEK_PDF = ROOT / "resources" / "raw" / "wetteksten" / "WBTW-2026.pdf"


@pytest.mark.skipif(
    not _RAW_WETBOEK_PDF.exists(),
    reason=f"Raw PDF ontbreekt ({_RAW_WETBOEK_PDF.relative_to(ROOT)})",
)
def test_wetboek_full_pipeline_integration(tmp_path: Path,
                                           monkeypatch: pytest.MonkeyPatch) -> None:
    """End-to-end test op één wetboek-bron — vereist de raw PDF lokaal."""
    monkeypatch.setattr(orchestrator, "STAGING_DIR", tmp_path)

    out = orchestrator.convert_one(_WETBOEK_INTEGRATION_TARGET, dry_run=False)
    assert out is not None and out.exists()
    text = out.read_text(encoding="utf-8")

    # Sanity-checks: er moeten artikelen en een chunk-blok zijn.
    art_count = len(re.findall(r"^#+ Art\. ", text, re.MULTILINE))
    assert art_count > 100, f"Verwacht >100 artikelen, kreeg {art_count}"
    assert re.search(r"^chunk:\s*$", text, re.MULTILINE) is not None
