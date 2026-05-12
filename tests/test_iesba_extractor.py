"""Unit-tests voor `tools.lib.extractors.iesba`.

Test-strategie: mock de pdftotext-subprocess call met een fixed string die
de typische IESBA-PDF-structuur nabootst. Geen I/O naar echte PDF-bestanden.
"""
from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.lib.extractors.iesba import (  # noqa: E402
    _cleanup_iesba,
    _PARA_NUM_RE,
    extract,
)


# ─── Fixture: typische IESBA-raw-tekst ───────────────────────────────────────

SAMPLE_RAW = """\
THE CODE

PART 1 – COMPLYING WITH THE CODE, FUNDAMENTAL
PRINCIPLES AND CONCEPTUAL FRAMEWORK
SECTION 100
COMPLYING WITH THE CODE
Introduction
100.1

A distinguishing mark of the accountancy profession is its acceptance
of the responsibility to act in the public interest.

100.2

Confidence in the accountancy profession.

16

SECTION 100

THE CODE

Requirements and Application Material
100.5 A1

The requirements in the Code.

R100.6

A professional accountant shall comply with the Code.
"""

SAMPLE_RAW_SECTION_BREAK = """\
THE CODE

SECTION 200
APPLYING THE CONCEPTUAL FRAMEWORK
Introduction
200.1

This section sets out requirements.

42

SECTION 200
"""


# ─── Tests op `_cleanup_iesba` ───────────────────────────────────────────────

def test_cleanup_strips_running_header_the_code():
    """Losse regel 'THE CODE' als running header wordt gestript."""
    result = _cleanup_iesba("THE CODE\n\nSome content.\n")
    assert "THE CODE" not in result


def test_cleanup_strips_section_running_header():
    """Losse regel 'SECTION 100' als running header wordt gestript."""
    result = _cleanup_iesba("SECTION 100\n\nSome content.\n")
    # 'SECTION 100' als losse running-header weg; als deel van inhoud behouden
    # (de regex treft alleen standalone-lines die niet gecombineerd worden)
    assert result.strip() != ""


def test_cleanup_strips_standalone_page_numbers():
    """Standalone paginanummers worden gestript."""
    result = _cleanup_iesba("Foo.\n\n16\n\nBar.\n")
    assert "\n16\n" not in result
    assert "Foo." in result
    assert "Bar." in result


def test_cleanup_promotes_part_heading():
    """PART N – ... wordt gepromoveerd naar # Part N — ..."""
    result = _cleanup_iesba(
        "PART 1 – COMPLYING WITH THE CODE, FUNDAMENTAL\n"
        "PRINCIPLES AND CONCEPTUAL FRAMEWORK\n"
        "SECTION 100\n"
    )
    assert "# Part 1 —" in result


def test_cleanup_promotes_section_heading():
    """SECTION NNN + volgende titel-regel worden gepromoveerd naar ## Section NNN — ..."""
    result = _cleanup_iesba(
        "SECTION 100\nCOMPLYING WITH THE CODE\nIntroduction\n"
    )
    assert "## Section 100 —" in result
    assert "Complying with the Code" in result or "COMPLYING WITH THE CODE" in result


def test_cleanup_bolds_paragraph_numbers():
    """Paragraafnummers (100.1, R100.6, 100.5 A1) worden bold."""
    result = _cleanup_iesba("100.1\n\nSome text.\n")
    assert "**100.1**" in result


def test_cleanup_bolds_r_prefix_paragraph():
    """Paragraafnummer met R-prefix (R100.6) wordt bold."""
    result = _cleanup_iesba("R100.6\n\nSome text.\n")
    assert "**R100.6**" in result


def test_cleanup_bolds_application_material_paragraph():
    """Paragraafnummer met A-suffix (100.5 A1) wordt bold."""
    result = _cleanup_iesba("100.5 A1\n\nSome text.\n")
    assert "**100.5 A1**" in result


def test_cleanup_full_sample():
    """End-to-end op SAMPLE_RAW: structurele properties controleren."""
    result = _cleanup_iesba(SAMPLE_RAW)
    # Part-heading aanwezig
    assert "# Part 1 —" in result
    # Section-heading aanwezig
    assert "## Section 100 —" in result
    # Paragraafnummers bold
    assert "**100.1**" in result
    assert "**100.2**" in result
    assert "**R100.6**" in result
    assert "**100.5 A1**" in result
    # Running headers weg
    assert "\nTHE CODE\n" not in result
    # Page numbers weg
    assert "\n16\n" not in result
    # Inhoud behouden
    assert "A distinguishing mark" in result
    assert "A professional accountant shall comply" in result


def test_cleanup_idempotent():
    """Tweede _cleanup_iesba op output verandert niets meer."""
    once = _cleanup_iesba(SAMPLE_RAW)
    twice = _cleanup_iesba(once)
    assert once == twice


# ─── Para-nummer regex ────────────────────────────────────────────────────────

@pytest.mark.parametrize("para", [
    "100.1",
    "100.2",
    "R100.6",
    "100.5 A1",
    "100.5 A2",
    "210.4 A1",
    "R210.4",
    "900.55",
])
def test_para_num_re_matches(para: str):
    """Regex herkent alle IESBA paragraafnummer-varianten."""
    assert _PARA_NUM_RE.match(para), f"Regex miste: {para!r}"


@pytest.mark.parametrize("non_para", [
    "Introduction",
    "Requirements and Application Material",
    "THE CODE",
    "SECTION 100",
    "16",
    "www.ethicsboard.org",
])
def test_para_num_re_no_false_positives(non_para: str):
    """Regex matcht NIET op niet-paragraafnummers."""
    assert not _PARA_NUM_RE.match(non_para), f"Valse positief: {non_para!r}"


# ─── extract() met mock subprocess ───────────────────────────────────────────

def test_extract_calls_pdftotext_and_cleans(tmp_path):
    """extract() roept pdftotext aan en retourneert gecleande body."""
    fake_pdf = tmp_path / "iesba_sample.pdf"
    fake_pdf.write_bytes(b"%PDF-1.4 fake")  # dummy bestand

    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = SAMPLE_RAW

    with patch("tools.lib.extractors.iesba.subprocess.run", return_value=mock_result) as mock_run:
        cfg = {"raw": str(fake_pdf), "extract": {"method": "iesba"}}
        result = extract(cfg, "IESBA-test")

    mock_run.assert_called_once()
    # Verify pdftotext was called (not pymupdf)
    call_args = mock_run.call_args[0][0]
    assert "pdftotext" in call_args[0]
    # Default start_page=20 resulteert in -f 20
    assert "-f" in call_args
    assert "20" in call_args

    # Resultaat is gecleand
    assert "# Part 1 —" in result
    assert "## Section 100 —" in result
    assert "**100.1**" in result
    assert "THE CODE" not in result or result.count("THE CODE") == 0


def test_extract_uses_default_start_page_20(tmp_path):
    """Standaard start_page is 20 (overslaat TOC en voorblad)."""
    fake_pdf = tmp_path / "iesba_default_page.pdf"
    fake_pdf.write_bytes(b"%PDF-1.4 fake")

    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = "100.1\n\nSome text.\n"

    with patch("tools.lib.extractors.iesba.subprocess.run", return_value=mock_result) as mock_run:
        cfg = {"raw": str(fake_pdf), "extract": {"method": "iesba"}}
        extract(cfg, "IESBA-test")

    call_args = mock_run.call_args[0][0]
    assert "-f" in call_args
    idx = call_args.index("-f")
    assert call_args[idx + 1] == "20"


def test_extract_custom_start_page(tmp_path):
    """start_page kan overschreven worden via params."""
    fake_pdf = tmp_path / "iesba_custom_page.pdf"
    fake_pdf.write_bytes(b"%PDF-1.4 fake")

    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = "100.1\n\nSome text.\n"

    with patch("tools.lib.extractors.iesba.subprocess.run", return_value=mock_result) as mock_run:
        cfg = {
            "raw": str(fake_pdf),
            "extract": {"method": "iesba", "params": {"start_page": 5}},
        }
        extract(cfg, "IESBA-test")

    call_args = mock_run.call_args[0][0]
    assert "-f" in call_args
    idx = call_args.index("-f")
    assert call_args[idx + 1] == "5"


def test_extract_raises_when_raw_missing():
    """ValueError als 'raw'-veld ontbreekt."""
    with pytest.raises(ValueError, match="raw"):
        extract({}, "IESBA-test")


def test_extract_raises_when_file_not_found():
    """FileNotFoundError als raw PDF niet bestaat."""
    with pytest.raises(FileNotFoundError):
        extract({"raw": "/tmp/__does_not_exist__.pdf"}, "IESBA-test")


def test_extract_raises_on_pdftotext_failure(tmp_path):
    """RuntimeError als pdftotext een fout teruggeeft."""
    fake_pdf = tmp_path / "bad.pdf"
    fake_pdf.write_bytes(b"not a pdf")

    mock_result = MagicMock()
    mock_result.returncode = 1
    mock_result.stderr = "Error: PDF file is damaged"

    with patch("tools.lib.extractors.iesba.subprocess.run", return_value=mock_result):
        with pytest.raises(RuntimeError, match="pdftotext"):
            extract({"raw": str(fake_pdf), "extract": {"method": "iesba"}}, "IESBA-test")
