"""Tests voor tools/lib/compilatie_split.py."""
from __future__ import annotations

from pathlib import Path

import pytest

from tools.lib.compilatie_split import (
    SplitConfig,
    detect_compilatie_boundaries,
    detect_kb_boundaries,
    split_btw_compilatie,
)


_ROOT = Path(__file__).resolve().parent.parent
_COMPILATIE_MD = _ROOT / "resources" / "bronnen" / "wetteksten" / "WBTW-KB-compilatie.md"


def test_detect_kb_boundaries_minimal():
    text = (
        "FOD Financiën — Btw KB nr. 1\n"
        "bla\n"
        "FOD Financiën — Btw KB nr. 2\n"
        "bla bla\n"
    )
    boundaries = detect_kb_boundaries(text)
    kb_ids = [b[0] for b in boundaries]
    assert "1" in kb_ids and "2" in kb_ids


def test_split_btw_compilatie_minimal():
    text = (
        "FOD Financiën — Btw KB nr. 1\n"
        "inhoud-1\n"
        "FOD Financiën — Btw KB nr. 2\n"
        "inhoud-2\n"
    )
    cfgs = [
        SplitConfig(kb_id="1", output="kb1.md", wet="KB nr. 1"),
        SplitConfig(kb_id="2", output="kb2.md", wet="KB nr. 2"),
    ]
    result = split_btw_compilatie(text, cfgs)
    assert set(result.keys()) == {"kb1.md", "kb2.md"}
    assert "inhoud-1" in result["kb1.md"]
    assert "inhoud-2" in result["kb2.md"]
    # Geen kruisbesmetting tussen KB's.
    assert "inhoud-2" not in result["kb1.md"]
    assert "inhoud-1" not in result["kb2.md"]


@pytest.mark.skipif(
    not _COMPILATIE_MD.exists(),
    reason="compilatie-MD ontbreekt",
)
def test_split_compilatie_smoke():
    text = _COMPILATIE_MD.read_text()
    boundaries = detect_kb_boundaries(text)
    unique_kbs = {b[0] for b in boundaries}
    assert len(unique_kbs) >= 30, (
        f"verwachtte minstens 30 unieke KB's in compilatie, vond {len(unique_kbs)}"
    )


# ─── MB-detectie en splitsing ────────────────────────────────────────────────


def test_detect_mb_boundaries_minimal():
    text = (
        "FOD Financiën — Btw MB nr. 1\n"
        "bla\n"
        "FOD Financiën — Btw MB nr. 2\n"
        "bla bla\n"
    )
    boundaries = detect_compilatie_boundaries(text, kind="mb")
    mb_ids = [b[0] for b in boundaries]
    assert "1" in mb_ids and "2" in mb_ids


def test_detect_mb_does_not_match_kb_headers():
    # KB-headers in input mogen NIET gedetecteerd worden in mb-modus.
    text = (
        "FOD Financiën — Btw KB nr. 3\n"
        "kb-inhoud\n"
        "FOD Financiën — Btw MB nr. 1\n"
        "mb-inhoud\n"
    )
    mb_boundaries = detect_compilatie_boundaries(text, kind="mb")
    mb_ids = {b[0] for b in mb_boundaries}
    assert mb_ids == {"1"}, f"verwachtte enkel MB-id 1, vond {mb_ids}"

    kb_boundaries = detect_compilatie_boundaries(text, kind="kb")
    kb_ids = {b[0] for b in kb_boundaries}
    assert kb_ids == {"3"}, f"verwachtte enkel KB-id 3, vond {kb_ids}"


def test_split_btw_compilatie_mb_kind_isolates_bodies():
    text = (
        "FOD Financiën — Btw MB nr. 1\n"
        "mb1-inhoud\n"
        "FOD Financiën — Btw MB 20.12.2001\n"
        "mb-datum-inhoud\n"
    )
    cfgs = [
        SplitConfig(kb_id="1", output="mb1.md", wet="MB nr. 1"),
        SplitConfig(kb_id="20.12.2001", output="mbdatum.md", wet="MB 20.12.2001"),
    ]
    result = split_btw_compilatie(text, cfgs, kind="mb")
    assert "mb1-inhoud" in result["mb1.md"]
    assert "mb-datum-inhoud" in result["mbdatum.md"]
    assert "mb-datum-inhoud" not in result["mb1.md"]


def test_detect_compilatie_boundaries_invalid_kind_raises():
    with pytest.raises(ValueError, match="kind"):
        detect_compilatie_boundaries("dummy", kind="zz")
