"""
Regression-tests voor forward-compat van `tools.lib.provenance.Input`.

Aanleiding: IFRS-bronnen (gegenereerd door `tools/etl/split_ifrs_verordening.py`)
schrijven `pages` in elke input-record (bv. '53-118') om traceerbaarheid per
PDF-pagina-range vast te houden. Voor die fix kraakte `read_provenance()` met
`TypeError: Input.__init__() got an unexpected keyword argument 'pages'`,
waardoor `rag_index.py` afbrak zodra het de eerste IAS/IFRS-bron raakte.

Deze test bewaakt twee dingen:
    1. `Input.pages` bestaat als optioneel veld (None default)
    2. Onbekende velden worden genegeerd via `Input.from_dict()` (forward-compat)
"""
from __future__ import annotations

from tools.lib.provenance import Input, Provenance


def test_input_pages_field_geaccepteerd():
    inp = Input(id="bron.pdf", sha256="abc", pages="53-118")
    assert inp.pages == "53-118"


def test_input_pages_default_none():
    inp = Input(id="bron.pdf")
    assert inp.pages is None


def test_input_from_dict_negeert_onbekende_velden():
    """Forward-compat: nieuwe velden in JSON moeten oude code niet kraken."""
    data = {
        "id": "bron.pdf",
        "sha256": "abc",
        "pages": "53-118",
        "verzonnen_veld": "dit moet genegeerd worden",
        "extra_metadata": {"foo": "bar"},
    }
    inp = Input.from_dict(data)
    assert inp.id == "bron.pdf"
    assert inp.pages == "53-118"


def test_provenance_from_dict_met_pages():
    """Integratie-test: complete Provenance-roundtrip met pages-velden."""
    data = {
        "inputs": [
            {"id": "verordening.pdf", "sha256": "deadbeef", "pages": "53-118"},
            {"id": "split-tool.py", "sha256": "feedcafe"},
        ],
        "tooling": {
            "pipeline": "etl-ifrs-split",
            "pipeline_version": "1.0.0",
        },
        "generated_at": "2026-05-15T10:00:00Z",
    }
    prov = Provenance.from_dict(data)
    assert len(prov.inputs) == 2
    assert prov.inputs[0].pages == "53-118"
    assert prov.inputs[1].pages is None
