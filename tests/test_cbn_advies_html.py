"""Tests voor tools/lib/cbn_advies_html.py."""
from __future__ import annotations

from tools.lib.cbn_advies_html import select_title


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
