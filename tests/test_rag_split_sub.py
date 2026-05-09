"""Tests voor `chunk.sub_strategy: per_definitieblok` (ADR-006 §4.2).

Verifieert dat:
- bronnen zonder sub_strategy ongewijzigd chunken (default-pad);
- bronnen mét sub_strategy="per_definitieblok" en ≥3 sub-grenzen ge-split worden;
- sub-chunk-IDs deterministisch zijn (`<basis>__sub_<N>`);
- breadcrumb-context van het artikel bewaard blijft in elke deelchunk.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.rag.rag_index import split_wettekst  # noqa: E402


_DEFINITIE_TEXT = """# Antiwitwaswet

###### Art. 4

Voor de toepassing van deze wet wordt verstaan onder :
   1° "WG/FT" : het witwassen van geld;
   2° "WG/FTP" : het witwassen van geld en financiering;
   3° "Richtlijn 2015/849" : Richtlijn (EU) 2015/849 van het Europees Parlement;
   4° "uitvoeringsmaatregelen" : de uitvoeringsmaatregelen van richtlijn 2015/849;

###### Art. 5

Andere artikel zonder sub-grenzen.
"""


def test_sub_strategy_splits_artikel_in_deelchunks():
    """Met sub_strategy='per_definitieblok' krijgt art. 4 één intro + N sub-chunks.

    Art. 5 (zonder sub-grenzen) blijft ongewijzigd.
    """
    fm = {
        "wet": "Antiwitwaswet",
        "chunk": {"level": 6, "type": "Art.", "sub_strategy": "per_definitieblok"},
    }
    chunks = split_wettekst(_DEFINITIE_TEXT, "Antiwitwaswet-2017", fm)
    ids = [c["id"] for c in chunks]

    # Art. 4: 1 intro-chunk + 4 sub-chunks
    assert "Antiwitwaswet-2017__art_4" in ids
    assert "Antiwitwaswet-2017__art_4__sub_1" in ids
    assert "Antiwitwaswet-2017__art_4__sub_2" in ids
    assert "Antiwitwaswet-2017__art_4__sub_3" in ids
    assert "Antiwitwaswet-2017__art_4__sub_4" in ids

    # Art. 5 ongewijzigd (geen sub-grenzen → geen split)
    assert "Antiwitwaswet-2017__art_5" in ids
    assert "Antiwitwaswet-2017__art_5__sub_1" not in ids


def test_sub_chunk_breadcrumb_behoudt_artikel_context():
    """Sub-chunk-breadcrumb verlengt artikelcontext met sub-positie."""
    fm = {
        "wet": "Antiwitwaswet",
        "chunk": {"level": 6, "type": "Art.", "sub_strategy": "per_definitieblok"},
    }
    chunks = split_wettekst(_DEFINITIE_TEXT, "Antiwitwaswet-2017", fm)
    sub1 = next(c for c in chunks if c["id"].endswith("__sub_1"))

    assert "Art. 4" in sub1["breadcrumb"]
    assert "1°" in sub1["breadcrumb"]

    # Path-array bevat extra sub-niveau
    assert sub1["path"][-1] == {"type": "sub", "nr": "1°", "naam": ""}


def test_default_zonder_sub_strategy_blijft_ongewijzigd():
    """Bronnen zonder sub_strategy (null) krijgen geen sub-splits."""
    fm = {
        "wet": "Antiwitwaswet",
        "chunk": {"level": 6, "type": "Art.", "sub_strategy": None},
    }
    chunks = split_wettekst(_DEFINITIE_TEXT, "Antiwitwaswet-2017", fm)
    ids = [c["id"] for c in chunks]

    # Geen __sub_-IDs
    assert all("__sub_" not in cid for cid in ids)
    assert "Antiwitwaswet-2017__art_4" in ids
    assert "Antiwitwaswet-2017__art_5" in ids


def test_sub_chunk_ids_zijn_deterministisch():
    """Tweede run met dezelfde input geeft identieke chunk-IDs."""
    fm = {
        "wet": "Antiwitwaswet",
        "chunk": {"level": 6, "type": "Art.", "sub_strategy": "per_definitieblok"},
    }
    run1 = split_wettekst(_DEFINITIE_TEXT, "Antiwitwaswet-2017", fm)
    run2 = split_wettekst(_DEFINITIE_TEXT, "Antiwitwaswet-2017", fm)
    assert [c["id"] for c in run1] == [c["id"] for c in run2]


def test_sub_strategy_drempel_te_weinig_grenzen():
    """Onder de drempel van 3 sub-grenzen: geen split, basis-chunk blijft intact."""
    text = """# Wet

###### Art. 1

Voor de toepassing wordt verstaan onder :
   1° eerste definitie;
   2° tweede definitie.

###### Art. 2

Body.
"""
    fm = {"wet": "Wet", "chunk": {"level": 6, "type": "Art.", "sub_strategy": "per_definitieblok"}}
    chunks = split_wettekst(text, "wet", fm)
    ids = [c["id"] for c in chunks]
    # Art. 1 heeft maar 2 sub-grenzen → geen split
    assert "wet__art_1" in ids
    assert "wet__art_1__sub_1" not in ids
