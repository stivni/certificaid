"""Integration-snapshot-tests met ECHTE raw-bronnen (ADR-005 §7 traag-pad).

In tegenstelling tot tests/test_pipeline_snapshots.py (mocked extract-output)
draaien deze tests de volledige pipeline op een echte PDF in
`resources/raw/wetteksten/`. Dat dekt:

- extractor-stap (pdftotext / pymupdf-block-extractie)
- transformer-chain (cleanup_basics + inject_headings_wettekst + emit_frontmatter)
- frontmatter-generatie

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


# Kleine bronnen waar de full pipeline < 1s draait — geschikt voor regressie-vangnet.
# Bron moet bestaan in resources/raw/ (gitignored), anders skip de test.
SLOW_FIXTURES = [
    # method: custom_wetboek (~0.6s)
    "WBTW-KB22jun2020-e-notariaat",
    # method: custom_wetboek — C2-regressiefixture voor strip_fisconet_artefacts
    # Bevat TOC-fragment (≥ 3 heading-blokken) + 'Titel' + 'Bron : FINANCIEN'.
    # Na de fix: schone body zonder TOC-fragment, zonder label-regels.
    "WBTW-KB1-voldoening",
    # method: pymupdf_wetboek (~0.5s) — block-aware PDF-extractie
    "BW-boek1-algemene-bepalingen",
    # method: pymupdf_wetboek + mode: eu_richtlijn — C1-regressiefixture
    # EU-OJ richtlijn: 6-pagina's NL-only 2-kolom, small PDF.
    # Na de fix: schone body zonder PB-kopteksten, zonder EUR-Lex markers,
    # zonder spaced-letter sectietitels; Artikel 1-8 correct als headings.
    "EU-Richtlijn-interest-royalties-2003-49",
]


def _strip_provenance(text: str) -> str:
    """Filter run-afhankelijke velden uit frontmatter.

    Strip:
    - `generated_at`: timestamp van de huidige run
    - `pipeline_version`: git commit hash, verandert per commit
    Beide zouden anders bij élke commit alle slow-snapshots roden zonder dat
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


def _raw_exists(source_name: str) -> bool:
    """Check of de bijbehorende raw-file bestaat (gitignored — kan ontbreken)."""
    import yaml
    cfg_path = ROOT / "resources" / "source_config.yaml"
    with open(cfg_path) as f:
        cfg = yaml.safe_load(f)
    src = cfg.get("sources", {}).get(source_name)
    if not src:
        return False
    raw_rel = src.get("raw")
    if not raw_rel:
        return False
    return (ROOT / raw_rel).exists()


@pytest.mark.slow
@pytest.mark.parametrize("source_name", SLOW_FIXTURES)
def test_real_bron_pipeline_snapshot(
    source_name: str,
    snapshot,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Vergelijk de volledige pipeline-output op een echte raw met de snapshot.

    Skipt automatisch als de raw-file ontbreekt (gitignored — kan lokaal weg zijn).
    """
    if not _raw_exists(source_name):
        pytest.skip(f"raw ontbreekt voor {source_name} (resources/raw/ is gitignored)")

    # Leid de pipeline-output naar tmp_path
    monkeypatch.setattr(orchestrator, "STAGING_DIR", tmp_path)

    out = orchestrator.convert_one(source_name)
    assert out is not None and out.exists(), f"convert_one returnt None voor {source_name}"

    text = _strip_provenance(out.read_text(encoding="utf-8"))
    assert text == snapshot
