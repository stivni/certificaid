"""Smoketests voor qa_bron.py in staging-modus.

Verifieert dat:
1. `iter_staging_targets()` MD-bestanden vindt onder `data/etl-staging/`
2. `qa_one_bron(..., staging=True)` een chunk_config_valid-check toevoegt
3. de chunk-config-validatie correct fail/pass rapporteert
4. de langste-sectie-check `chunk.level` uit frontmatter respecteert
"""
from __future__ import annotations

from pathlib import Path

import pytest

from tools.etl.qa_bron import (
    STAGING_DIR,
    _parse_chunk_config,
    check_chunk_config,
    check_max_section,
    check_no_column_bleed,
    iter_staging_targets,
    qa_one_bron,
)

ROOT = Path(__file__).resolve().parent.parent


# ─── Smoketest op echte staging-bestanden ───────────────────────────────────

@pytest.fixture(scope="module")
def staging_files() -> list[Path]:
    if not STAGING_DIR.exists():
        pytest.skip(f"Staging-map ontbreekt: {STAGING_DIR}")
    files = iter_staging_targets(None)
    if not files:
        pytest.skip("Geen staging-bestanden aanwezig")
    return files


def test_staging_targets_gevonden(staging_files: list[Path]) -> None:
    assert len(staging_files) > 0
    for f in staging_files:
        assert f.suffix == ".md"
        assert f.parent == STAGING_DIR


def test_qa_one_bron_staging_voegt_chunk_config_check_toe(staging_files: list[Path]) -> None:
    """Bij staging-mode moet exact één check `chunk_config_valid` aanwezig zijn."""
    sample = staging_files[0]
    report = qa_one_bron(sample, staging=True)
    check_names = [c.name for c in report.checks]
    assert check_names.count("chunk_config_valid") == 1


def test_qa_one_bron_resources_geen_chunk_config_check(staging_files: list[Path]) -> None:
    """Bij niet-staging mode (default) mag chunk_config_valid niet worden uitgevoerd."""
    sample = staging_files[0]
    report = qa_one_bron(sample, staging=False)
    check_names = [c.name for c in report.checks]
    assert "chunk_config_valid" not in check_names


def test_staging_md_heeft_geldige_chunk_config(staging_files: list[Path]) -> None:
    """Geen enkele staging-MD mag een ontbrekende of ongeldige chunk-config hebben."""
    failures = []
    for f in staging_files:
        report = qa_one_bron(f, staging=True)
        for c in report.checks:
            if c.name == "chunk_config_valid" and c.status == "fail":
                failures.append((f.name, c.detail))
    assert not failures, f"chunk-config fails: {failures[:5]}"


# ─── Eenheidstests op de helpers ───────────────────────────────────────────

VALID_FRONTMATTER = """tags: ["X"]
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs: []
"""


def test_parse_chunk_config_basis() -> None:
    cfg = _parse_chunk_config(VALID_FRONTMATTER)
    assert cfg is not None
    assert cfg["level"] == 2
    assert cfg["type"] == "Art."
    assert cfg["sub_strategy"] is None


def test_check_chunk_config_pass() -> None:
    res = check_chunk_config(VALID_FRONTMATTER)
    assert res.status == "pass"


def test_check_chunk_config_fail_ontbrekend() -> None:
    res = check_chunk_config('tags: ["X"]\n')
    assert res.status == "fail"
    assert "chunk-config" in (res.detail or "")


def test_check_chunk_config_fail_ongeldig_level() -> None:
    fm = "chunk:\n  level: 9\n  type: \"Art.\"\n  sub_strategy:\n"
    res = check_chunk_config(fm)
    assert res.status == "fail"


def test_check_no_column_bleed_skipt_md_tabel_en_toc_bijwerking() -> None:
    """False-positives skippen:
    - markdown-tabelrijen (regels die met `|` beginnen)
    - plain-text tabel-context (Bijwerking-TOC + tabulaire datarijen)
    Een echte krantenkolom-bleed-regel in lopende tekst wordt nog wel gewarnd.
    """
    # 1. Markdown-tabelrij — geen warn.
    md_table = "| Activa                       Passiva |\n| 100                          200    |\n"
    assert check_no_column_bleed(md_table).status == "pass"

    # 2. WBTW-stijl Bijwerking-TOC met datarijen — geen warn.
    toc_bijwerking = (
        "KB nr. 6 - Lijst van de bijwerkingen\n"
        "\n"
        "       Bijwerking       t.e.m. B.S. van                       Te vervangen pagina's\n"
        "\n"
        " Bijw. 01 / 01.01.2012   - Volledige uitgave\n"
    )
    assert check_no_column_bleed(toc_bijwerking).status == "pass"

    # 3. Echte twee-kolom-bleed: één geïsoleerde regel met grote spatie-run
    #    midden in lopende tekst (geen tabulaire neighbours) — moet warn geven.
    real_bleed = (
        "Dit is een normale paragraaf zonder tabulaire structuur die\n"
        "loopt over meerdere regels en geen brede spatie-runs bevat.\n"
        "Wordt voor de toepassing van dit wetboek, met een aan een                        Po schorsende voorwaarde onderworpen handeling.\n"
        "Daarna gaat de gewone lopende tekst rustig verder zonder\n"
        "kolommen of brede spatie-uitlijningen in zicht.\n"
    )
    assert check_no_column_bleed(real_bleed).status == "warn"


def test_check_max_section_respecteert_forced_level() -> None:
    """Forced level=6 op body zonder ###### → gehele body als één sectie gemeten."""
    body = "## A\nlorem\n## B\n" + ("x" * 50)
    res_default, _ = check_max_section(body, heading_count=2, forced_level=None)
    assert res_default.status == "pass"
    # Met forced_level=6 zijn er geen ###### headings → één sectie van len(body)
    _, max_forced = check_max_section(body, heading_count=2, forced_level=6)
    assert max_forced == len(body)
