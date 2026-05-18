"""Tests voor tools.examen.extract_vragen_v2 (ADR-021).

Strategie:
- Unit-tests op pure helpers (tabel_is_geldig, render_tabel_als_markdown,
  concat_blokken_naar_vraagtekst, splits_blokken_in_vragen).
- Stub-page-objecten voor extract_blokken_uit_page (geen echte PDF nodig).
- Integration-smoke-test op resources/raw/voorbeeldexamens/2014-1.pdf om
  vr8-tabel-detectie te bevestigen.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from tools.examen.extract_vragen_v2 import (
    Blok,
    PDF_DIR,
    blok_naar_dict,
    concat_blokken_naar_vraagtekst,
    extract_blokken_uit_page,
    extract_examen_v2,
    EXAMEN_CONFIGS_V2,
    pad_rijen_naar_zelfde_lengte,
    render_tabel_als_markdown,
    splits_blokken_in_vragen,
    tabel_is_geldig,
)


# ---------------------------------------------------------------------------
# Pure helpers
# ---------------------------------------------------------------------------

class TestTabelIsGeldig:
    def test_geldige_volle_tabel(self):
        rows = [["a", "b"], ["c", "d"], ["e", "f"]]
        assert tabel_is_geldig(rows) is True

    def test_te_klein(self):
        assert tabel_is_geldig([["a", "b"]]) is False
        assert tabel_is_geldig([["a"], ["b"], ["c"]]) is False

    def test_invul_tabel_met_header_wordt_geaccepteerd(self):
        # Invul-tabel zoals 2014-1-vr8: corner-cell leeg, header gevuld, data
        # leeg (intentioneel — student vult in). Moet geaccepteerd worden.
        rows = [
            ["", "Controle", "Belang", "Methode"],
            ["M in A", "", "", ""],
            ["M in B", "", "", ""],
        ]
        assert tabel_is_geldig(rows) is True

    def test_invul_tabel_met_volle_eerste_rij(self):
        rows = [
            ["A", "B", "C"],
            ["", "", ""],
            ["", "", ""],
        ]
        # eerste rij 100% gevuld → toegestaan
        assert tabel_is_geldig(rows) is True

    def test_grotendeels_lege_tabel_zonder_header_wordt_verworpen(self):
        rows = [
            ["", "", ""],
            ["", "x", ""],
            ["", "", ""],
        ]
        assert tabel_is_geldig(rows) is False


class TestPadRijen:
    def test_pad_uneven(self):
        out = pad_rijen_naar_zelfde_lengte([["a", "b"], ["c"]])
        assert out == [["a", "b"], ["c", ""]]

    def test_leeg(self):
        assert pad_rijen_naar_zelfde_lengte([]) == []


class TestRenderTabelAlsMarkdown:
    def test_met_headers(self):
        blok = Blok(type="tabel", headers=["A", "B"], rows=[["1", "2"], ["3", "4"]])
        md = render_tabel_als_markdown(blok)
        assert "| A | B |" in md
        assert "|---|---|" in md
        assert "| 1 | 2 |" in md
        assert "| 3 | 4 |" in md

    def test_zonder_headers(self):
        blok = Blok(type="tabel", rows=[["x", "y"]])
        md = render_tabel_als_markdown(blok)
        # Synthetic empty headers
        assert "|---|---|" in md
        assert "| x | y |" in md


class TestConcatBlokken:
    def test_alleen_tekst(self):
        blokken = [
            {"type": "tekst", "inhoud": "Hello"},
            {"type": "tekst", "inhoud": "World"},
        ]
        out = concat_blokken_naar_vraagtekst(blokken)
        assert "Hello" in out
        assert "World" in out

    def test_tekst_en_tabel(self):
        blokken = [
            {"type": "tekst", "inhoud": "Vul tabel"},
            {"type": "tabel", "headers": ["A", "B"], "rows": [["1", "2"]]},
        ]
        out = concat_blokken_naar_vraagtekst(blokken)
        assert "Vul tabel" in out
        assert "| A | B |" in out

    def test_figuur(self):
        blokken = [{"type": "figuur", "caption": "diagram"}]
        out = concat_blokken_naar_vraagtekst(blokken)
        assert "figuur" in out


class TestBlokNaarDict:
    def test_tekst(self):
        b = Blok(type="tekst", inhoud="  hi  ")
        d = blok_naar_dict(b)
        assert d == {"type": "tekst", "inhoud": "hi"}

    def test_tabel_met_bbox(self):
        b = Blok(
            type="tabel",
            rows=[["a", "b"]],
            headers=["H1", "H2"],
            bron_bbox=(1.0, 2.0, 3.0, 4.0),
            page=7,
        )
        d = blok_naar_dict(b)
        assert d["type"] == "tabel"
        assert d["headers"] == ["H1", "H2"]
        assert d["bron_bbox"]["page"] == 7
        assert d["bron_bbox"]["top"] == 2.0


# ---------------------------------------------------------------------------
# Vraag-splitsing
# ---------------------------------------------------------------------------

class TestSplitsBlokkenInVragen:
    def test_eenvoudig_twee_vragen(self):
        blokken = [
            Blok(type="tekst", inhoud="Vraag 1 … / 5 punten\nWat is X?"),
            Blok(type="tekst", inhoud="Vraag 2 … / 3 punten\nWat is Y?"),
        ]
        vragen = splits_blokken_in_vragen(blokken)
        assert len(vragen) == 2
        assert vragen[0].vraag_nr == "1"
        assert vragen[0].punten == 5.0
        assert vragen[1].vraag_nr == "2"
        assert vragen[1].punten == 3.0

    def test_tabel_volgt_op_vraag(self):
        blokken = [
            Blok(type="tekst", inhoud="Vraag 4 … / 9 punten\nVul tabel"),
            Blok(type="tabel", rows=[["a", "b"]], headers=None),
            Blok(type="tekst", inhoud="Vraag 5 … / 2 punten\nNew"),
        ]
        vragen = splits_blokken_in_vragen(blokken)
        assert len(vragen) == 2
        # Eerste vraag krijgt tabel-blok
        assert any(b.type == "tabel" for b in vragen[0].blokken)
        # Tweede vraag krijgt geen tabel
        assert not any(b.type == "tabel" for b in vragen[1].blokken)

    def test_meerdere_vragen_in_één_tekstblok(self):
        # Een page-tekst-blok bevat twee vraag-headers
        blokken = [
            Blok(type="tekst", inhoud="Vraag 1 … / 1 punten\nA\nVraag 2 … / 2 punten\nB"),
        ]
        vragen = splits_blokken_in_vragen(blokken)
        assert len(vragen) == 2
        assert vragen[0].vraag_nr == "1"
        assert vragen[1].vraag_nr == "2"


# ---------------------------------------------------------------------------
# Stub-page voor extract_blokken_uit_page
# ---------------------------------------------------------------------------

class _StubTable:
    def __init__(self, bbox, rows):
        self.bbox = bbox
        self._rows = rows

    def extract(self):
        return self._rows


class _StubPage:
    def __init__(self, words, tables):
        self._words = words
        self._tables = tables

    def find_tables(self, table_settings=None):
        return self._tables

    def extract_words(self, **kw):
        return self._words


class TestExtractBlokkenUitPage:
    def test_zonder_tabel(self):
        words = [
            {"text": "Hello", "x0": 0, "x1": 30, "top": 10, "bottom": 20},
            {"text": "World", "x0": 32, "x1": 60, "top": 10, "bottom": 20},
        ]
        page = _StubPage(words, [])
        blokken, verworpen = extract_blokken_uit_page(page, 1, None)
        assert len(blokken) == 1
        assert blokken[0].type == "tekst"
        assert "Hello World" in blokken[0].inhoud
        assert verworpen == []

    def test_met_geldige_tabel(self):
        words = [
            {"text": "Voor", "x0": 0, "x1": 30, "top": 10, "bottom": 20},
            {"text": "tabel", "x0": 0, "x1": 30, "top": 100, "bottom": 110},
            # Woord binnen tabel-bbox → moet eruit gefilterd worden
            {"text": "INSIDE", "x0": 50, "x1": 80, "top": 60, "bottom": 70},
            {"text": "Na", "x0": 0, "x1": 30, "top": 200, "bottom": 210},
        ]
        tabel = _StubTable(
            bbox=(40, 40, 200, 90),
            rows=[["A", "B"], ["c", "d"], ["e", "f"]],
        )
        page = _StubPage(words, [tabel])
        blokken, verworpen = extract_blokken_uit_page(page, 1, None)
        # 3 blokken: voor, tabel, na
        types = [b.type for b in blokken]
        assert types.count("tabel") == 1
        assert types.count("tekst") >= 2
        tekst_inhoud = " ".join(b.inhoud or "" for b in blokken if b.type == "tekst")
        assert "INSIDE" not in tekst_inhoud
        assert "Voor" in tekst_inhoud
        assert "Na" in tekst_inhoud
        # Headers detectie: eerste rij volledig gevuld
        tabel_blok = next(b for b in blokken if b.type == "tabel")
        assert tabel_blok.headers == ["A", "B"]
        assert tabel_blok.rows == [["c", "d"], ["e", "f"]]

    def test_te_kleine_tabel_wordt_verworpen(self):
        words = [{"text": "Hi", "x0": 0, "x1": 10, "top": 10, "bottom": 20}]
        tabel = _StubTable(bbox=(0, 0, 100, 100), rows=[["a"]])
        page = _StubPage(words, [tabel])
        blokken, verworpen = extract_blokken_uit_page(page, 1, None)
        assert all(b.type != "tabel" for b in blokken)
        assert len(verworpen) == 1
        assert verworpen[0]["reden"] == "validatie_faalt"


# ---------------------------------------------------------------------------
# Integration smoke: 2014-1 vr8
# ---------------------------------------------------------------------------

PDF_2014_1 = PDF_DIR / "2014-1.pdf"


@pytest.mark.skipif(not PDF_2014_1.exists(), reason="2014-1.pdf niet beschikbaar")
class TestSmoke2014_1:
    """Smoke-test: extract op 2014-1 → vr8 moet een tabel-blok bevatten."""

    def test_vr8_heeft_tabel_blok(self):
        out = extract_examen_v2("2014-1", EXAMEN_CONFIGS_V2["2014-1"])
        assert out["schema_versie"] == "2.0"
        assert out["extractie"]["n_vragen"] == 46
        vr8 = next(v for v in out["vragen"] if v["id"] == "2014-1-vr8")
        assert vr8["vraagtekst_blokken"], "vr8 zonder blokken"
        types = [b["type"] for b in vr8["vraagtekst_blokken"]]
        assert "tabel" in types, f"geen tabel in vr8, types={types}"
        # Tabel-blok: headers bevatten CONTROLEPERCENTAGE
        tabel_blokken = [b for b in vr8["vraagtekst_blokken"] if b["type"] == "tabel"]
        joined = " ".join(
            " ".join(b.get("headers") or []) + " " + " ".join(c for r in b["rows"] for c in r)
            for b in tabel_blokken
        )
        assert "CONTROLEPERCENTAGE" in joined
