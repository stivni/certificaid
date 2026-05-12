"""Integration-snapshot-tests met ECHTE PDF-fixtures (ADR-005 §7 traag-pad).

In tegenstelling tot tests/test_pipeline_snapshots.py (mocked extract-output
op string-niveau) draaien deze tests de volledige pipeline op kleine PDF's
die ALS FIXTURE in tests/fixtures/extract/pdf/ wonen. Dat dekt:

- extractor-stap (pdftotext / pymupdf-block-extractie)
- transformer-chain (cleanup_basics + inject_headings_wettekst + emit_frontmatter)
- frontmatter-generatie

De fixtures zijn gekopieerd uit `resources/raw/wetteksten/` (die gitignored
is). De tests zelf zijn onafhankelijk van `resources/raw/`-aanwezigheid —
ze draaien overal waar de repo gecheckt is.

Gemarkeerd als `@pytest.mark.slow` — pre-commit hook draait `pytest -q
-m "not slow"` zodat lokale commits snel blijven. Run handmatig met:

    pytest tests/test_pipeline_snapshots_slow.py -v

Snapshot-update na een bewuste pipeline-wijziging:

    pytest tests/test_pipeline_snapshots_slow.py --snapshot-update
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl import convert as orchestrator  # noqa: E402

FIXTURES_PDF = ROOT / "tests" / "fixtures" / "extract" / "pdf"


# (fixture_naam, extract_method, extra_params) — fixture moet als <naam>.pdf in
# FIXTURES_PDF bestaan. extra_params landen onder cfg["extract"]["params"].
SLOW_FIXTURES = [
    # custom_wetboek baseline — kleine KB, geen TOC-fragment
    (
        "WBTW-KB22jun2020-e-notariaat",
        "custom_wetboek",
        {},
    ),
    # custom_wetboek + C2-regressiefixture voor strip_fisconet_artefacts:
    # bevat TOC-fragment (≥ 3 heading-blokken) + 'Titel' + 'Bron : FINANCIEN'.
    # Na de fix: schone body zonder TOC-fragment, zonder label-regels.
    (
        "WBTW-KB1-voldoening",
        "custom_wetboek",
        {},
    ),
    # pymupdf_wetboek baseline — block-aware PDF-extractie
    (
        "BW-boek1-algemene-bepalingen",
        "pymupdf_wetboek",
        {},
    ),
    # pymupdf_wetboek + mode: eu_richtlijn — C1-regressiefixture
    # EU-OJ richtlijn: 2-kolom NL-only. Na de fix: schone body zonder
    # PB-kopteksten, zonder EUR-Lex markers, zonder spaced-letter sectietitels.
    (
        "EU-Richtlijn-interest-royalties-2003-49",
        "pymupdf_wetboek",
        {"mode": "eu_richtlijn"},
    ),
]


def _strip_provenance(text: str) -> str:
    """Filter run-afhankelijke velden uit frontmatter.

    Strip:
    - `generated_at`: timestamp van de huidige run
    - `pipeline_version`: git commit hash, verandert per commit
    - `sha256`: hash van de fixture-PDF (varieert niet, maar gevoelig voor
      formaat-wijzigingen — laat staan)
    Beide eerste zouden anders bij élke commit alle slow-snapshots roden zonder dat
    er inhoudelijk iets veranderd is.
    """
    text = re.sub(
        r"^\s*generated_at:\s*['\"]?[^'\"\n]+['\"]?\s*$",
        "  generated_at: '<STRIPPED>'",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^\s*pipeline_version:\s*['\"]?[^'\"\n]+['\"]?\s*$",
        "    pipeline_version: '<STRIPPED>'",
        text,
        flags=re.MULTILINE,
    )
    return text


def _build_test_cfg(name: str, method: str, extra_params: dict) -> dict:
    """Bouw een minimale source-config-dict voor de orchestrator.

    Het `raw:`-pad wijst naar de fixture in tests/fixtures/extract/pdf/.
    """
    fixture_pdf = FIXTURES_PDF / f"{name}.pdf"
    if not fixture_pdf.exists():
        pytest.fail(f"Fixture PDF ontbreekt: {fixture_pdf}")
    return {
        "bron_rol": "itaa_lex",
        "raw": str(fixture_pdf.relative_to(ROOT)),
        "output": f"tests/__snapshots__/_unused_{name}.md",  # vervangen door tmp_path-redirect
        "itaa_sectie": "TEST",
        "tags": ["TEST", "snapshot-slow"],
        "bijgewerkt": "01.01.2026",
        "wet": f"Test-fixture: {name}",
        "status": "volledig",
        "extract": {"method": method, "params": extra_params},
    }


@pytest.mark.slow
@pytest.mark.parametrize(
    "fixture",
    SLOW_FIXTURES,
    ids=lambda f: f[0],  # gebruik de naam als test-id
)
def test_fixture_pipeline_snapshot(
    fixture: tuple,
    snapshot,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Vergelijk de pipeline-output op een fixture-PDF met de snapshot.

    Run alleen onder `pytest -m slow`. Snapshot-update via `--snapshot-update`.
    """
    name, method, extra_params = fixture
    cfg = _build_test_cfg(name, method, extra_params)

    monkeypatch.setattr(orchestrator, "load_config", lambda: {name: cfg})
    monkeypatch.setattr(orchestrator, "OUTPUT_ROOT", tmp_path)

    out = orchestrator.convert_one(name)
    assert out is not None and out.exists(), f"convert_one returnt None voor {name}"

    text = _strip_provenance(out.read_text(encoding="utf-8"))
    assert text == snapshot
