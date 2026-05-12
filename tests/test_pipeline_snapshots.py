"""Snapshot-baseline voor de bestaande ETL-pipeline (cleanup + headings + frontmatter).

Doel: regressie-vangnet vóór de refactor naar `extractors/` + `transformers/`
(ADR-005 §1, §3, §4). We mocken de extract-stap met fixed input-strings zodat
de tests deterministisch en snel zijn (milliseconds, geen raw PDFs nodig).

Bij failure ⇒ ofwel een echte regressie (fix code) ofwel een bedoelde
verbetering (`pytest tests/test_pipeline_snapshots.py --snapshot-update` om de
snapshots bij te werken na manuele review).

Fixtures dekken één representatief geval per extract-method dat NIET via een
echte raw-file moet draaien (ejustice, wetboek, wib92). Voor html_cbn (advies)
en justel_html zou je echte HTML als fixture moeten meegeven; dat doen we in
een tweede snapshot-set (zie tests/fixtures/ en test_extractors_snapshots.py
zodra die er zijn).
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


# ─── Fake extract-outputs per method ──────────────────────────────────────────

# Realistische mini-input voor pdftotext_ejustice: TOC + paginavoetregel + body
# met HOOFDSTUK/AFDELING/Art. patronen die de heading-injectie moet vinden.
_FAKE_EJUSTICE_BODY = """\
Inhoudstafel
HOOFDSTUK 1. - Algemene bepalingen   1
  AFDELING 1. - Definities ............. 2
  AFDELING 2. - Toepassingsgebied ...... 5

Tekst
HOOFDSTUK 1. - Algemene bepalingen

AFDELING 1. - Definities

Art. 1.  Voor de toepassing van deze testwet wordt verstaan onder accountant
de persoon die ingeschreven is in het openbaar register van het Instituut.

Art. 2.  Deze wet is van toepassing op alle natuurlijke personen.

AFDELING 2. - Toepassingsgebied

Art. 3.  De wet treedt in werking op 1 januari 2026.
"""

# Mini wetboek-stijl input met BOEK > TITEL > HOOFDSTUK + Art.
_FAKE_WETBOEK_BODY = """\
BOEK I. - Inleidende bepalingen

TITEL I. - Definities

HOOFDSTUK 1. - Algemeen

Art. 1:1.  In dit wetboek wordt verstaan onder vennootschap een rechtspersoon.

Art. 1:2.  Een vennootschap heeft een eigen vermogen.

HOOFDSTUK 2. - Rechtsvorm

Art. 1:3.  De keuze van de rechtsvorm gebeurt bij oprichting.
"""

# Mini WIB92-stijl input
_FAKE_WIB92_BODY = """\
TITEL I. - Inkomstenbelastingen

HOOFDSTUK I. - Vestiging van de belasting

AFDELING I. - Personenbelasting

Art. 1.  De personenbelasting wordt geheven op het wereldwijde inkomen.

Art. 2.  Belastingplichtig zijn de natuurlijke personen.
"""

FIXTURES = {
    "ejustice_basic": ("pdftotext_ejustice", _FAKE_EJUSTICE_BODY),
    "wetboek_minimal": ("custom_wetboek", _FAKE_WETBOEK_BODY),
    "wib92_minimal": ("custom_wib92", _FAKE_WIB92_BODY),
}


def _make_test_cfg(method: str, name: str = "TestBron") -> dict:
    return {
        "bron_rol": "itaa_lex",
        "raw": f"resources/raw/wetteksten/{name}.pdf",
        "output": f"resources/bronnen/wetteksten/{name}.md",
        "itaa_sectie": "TEST",
        "tags": ["TEST", "snapshot"],
        "bijgewerkt": "01.01.2026",
        "wet": f"Test-wet voor snapshot-baseline ({method})",
        "status": "volledig",
        "extract": {"method": method},
    }


def _strip_provenance(text: str) -> str:
    """Verwijder generated_at-velden uit YAML frontmatter (varieert per run)."""
    return re.sub(
        r"^\s*generated_at:\s*['\"]?[^'\"\n]+['\"]?\s*$",
        "  generated_at: '<STRIPPED>'",
        text,
        flags=re.MULTILINE,
    )


# ─── Snapshot-tests per fixture ───────────────────────────────────────────────

@pytest.mark.parametrize("fixture_name", list(FIXTURES.keys()))
def test_pipeline_output_snapshot(
    fixture_name: str,
    snapshot,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Vergelijk de pipeline-output per fixture met de opgeslagen snapshot.

    Snapshot-update na bewuste wijziging:
        pytest tests/test_pipeline_snapshots.py --snapshot-update
    """
    method, fake_body = FIXTURES[fixture_name]
    cfg = _make_test_cfg(method, name=f"Test{fixture_name}")

    monkeypatch.setattr(orchestrator, "load_config", lambda: {f"Test{fixture_name}": cfg})
    fake_handler = mock.Mock(return_value=fake_body)
    monkeypatch.setattr(orchestrator, "get_handler", lambda m: fake_handler)
    monkeypatch.setattr(orchestrator, "STAGING_DIR", tmp_path)
    monkeypatch.setattr(orchestrator, "_attach_provenance", lambda *a, **kw: None)

    out = orchestrator.convert_one(f"Test{fixture_name}")
    assert out is not None and out.exists()
    text = out.read_text(encoding="utf-8")
    text = _strip_provenance(text)

    assert text == snapshot


# ─── HTML-extractor snapshot-tests (parser-laag óók in het vangnet) ───────────
#
# Voor html_cbn en html_justel willen we de HTML→MD parser-logica óók
# beschermen — niet alleen cleanup/headings/frontmatter. We mocken daarom
# op fetch-niveau (één laag dieper dan de wettekst-tests hierboven): een mini
# HTML-fixture uit tests/fixtures/extract/ wordt teruggegeven, daarna draait
# de echte parser + de echte pipeline. Resultaat snapshot we als één geheel.

FIXTURES_DIR = ROOT / "tests" / "fixtures" / "extract"


def _read_fixture(name: str) -> str:
    return (FIXTURES_DIR / name).read_text(encoding="utf-8")


def test_cbn_advies_pipeline_snapshot(
    snapshot, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """End-to-end snapshot voor cbn_advies: fixture HTML → parser → pipeline → MD."""
    html_fixture = _read_fixture("cbn_advies_minimal.html")

    # Mock de fetch in cbn_advies_html, laat parser + scrape_advies draaien
    from tools.lib import cbn_advies_html
    monkeypatch.setattr(
        cbn_advies_html,
        "_fetch_html",
        lambda url: (200, html_fixture),
    )

    cfg = {
        "bron": "https://www.cbn-cnc.be/nl/adviezen/test-snapshot",
        "bron_rol": "interpretatief",
        "wet": "CBN-advies snapshot-fixture",
        "tags": ["TEST", "snapshot"],
        "bijgewerkt": "01.01.2026",
        "status": "volledig",
        "extract": {"method": "cbn_advies"},
    }
    monkeypatch.setattr(orchestrator, "load_config", lambda: {"TestCBN": cfg})
    monkeypatch.setattr(orchestrator, "STAGING_DIR", tmp_path)
    monkeypatch.setattr(orchestrator, "_attach_provenance", lambda *a, **kw: None)

    out = orchestrator.convert_one("TestCBN")
    assert out is not None and out.exists()
    text = _strip_provenance(out.read_text(encoding="utf-8"))
    assert text == snapshot


def test_justel_html_pipeline_snapshot(
    snapshot, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """End-to-end snapshot voor justel_html: fixture HTML → parser → pipeline → MD."""
    html_fixture_bytes = _read_fixture("justel_html_minimal.html").encode("utf-8")

    # De justel_html-extractor importeert convert_justel via een sys.path-truc
    # ("from etl import convert_justel as _legacy"), dus we moeten de fetch
    # via die specifieke binding mocken — niet via tools.etl.convert_justel.
    from tools.lib.extractors import justel_html as justel_extractor
    monkeypatch.setattr(
        justel_extractor._legacy, "fetch_justel",
        lambda url, timeout=60: html_fixture_bytes,
    )

    cfg = {
        "bron_rol": "itaa_lex",
        "source_url": "https://ejustice.example/justel/test",
        "raw": "resources/raw/wetteksten/TestJustel.html",
        "output": "resources/bronnen/wetteksten/TestJustel.md",
        "wet": "Test-wet voor justel-snapshot",
        "tags": ["TEST", "snapshot"],
        "bijgewerkt": "01.01.2026",
        "status": "volledig",
        "itaa_sectie": "TEST",
        "extract": {"method": "justel_html"},
    }
    monkeypatch.setattr(orchestrator, "load_config", lambda: {"TestJustel": cfg})
    monkeypatch.setattr(orchestrator, "STAGING_DIR", tmp_path)
    monkeypatch.setattr(orchestrator, "_attach_provenance", lambda *a, **kw: None)

    out = orchestrator.convert_one("TestJustel")
    assert out is not None and out.exists()
    text = _strip_provenance(out.read_text(encoding="utf-8"))
    assert text == snapshot
