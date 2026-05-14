"""Regressie-tests voor `_sweep_orphans_per_bron` in rag_index.

Doel van de orphan-sweep (ADR-005 §5, deze sessie toegevoegd):
  Bij re-conversie van een bron kan de chunk-structuur wijzigen (extra artikel,
  hernoemde sectie, andere sub_strategy). De `chunk_sha`-skip in _batch_upsert
  detecteert ongewijzigde chunks via id-vergelijking — maar oude chunk-ids die
  niet meer worden gegenereerd blijven achter in ChromaDB als orphans.

De sweep:
  1. Groepeert nieuwe chunk-ids per `bestand` (metadata-veld)
  2. Per bestand: haalt bestaande ids op via `where={"bestand": ...}`
  3. Delete elke id die wel bestaat maar niet meer in de nieuwe set zit
  4. Bronnen die NIET in deze run voorkomen worden NIET aangeraakt
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.rag.rag_index import _sweep_orphans_per_bron  # noqa: E402


class FakeCollection:
    """Minimale ChromaDB-collection mock: ondersteunt get(where=) en delete(ids=)."""

    def __init__(self, store: dict[str, str]):
        # store: {chunk_id: bestand}
        self.store = dict(store)
        self.deleted: list[str] = []

    def get(self, where: dict, include: list[str]):
        target = where["bestand"]
        ids = [cid for cid, bestand in self.store.items() if bestand == target]
        return {"ids": ids}

    def delete(self, ids: list[str]):
        for cid in ids:
            self.store.pop(cid, None)
            self.deleted.append(cid)


def test_orphan_sweep_verwijdert_oude_ids():
    """Re-conversie van X.md: structuur wijzigt, oude id `X__art_5` is weg.

    Vóór de sweep: oude id blijft in Chroma als orphan.
    Na de sweep: verwijderd.
    """
    col = FakeCollection({
        "X__art_1": "X.md",
        "X__art_2": "X.md",
        "X__art_5": "X.md",   # weggegaan na re-conversie
        "Y__art_1": "Y.md",   # andere bron — niet aanraken
    })
    # Huidige run produceert alleen art_1 en art_2 voor X.md
    new_ids = ["X__art_1", "X__art_2"]
    new_metadatas = [
        {"bestand": "X.md"},
        {"bestand": "X.md"},
    ]
    n_orphans = _sweep_orphans_per_bron(col, new_ids, new_metadatas)
    assert n_orphans == 1
    assert col.deleted == ["X__art_5"]
    # Y.md ongemoeid
    assert "Y__art_1" in col.store


def test_orphan_sweep_geen_orphans_geen_delete():
    """Als nieuwe set identiek is aan bestaande: 0 deletes."""
    col = FakeCollection({
        "X__art_1": "X.md",
        "X__art_2": "X.md",
    })
    new_ids = ["X__art_1", "X__art_2"]
    new_metadatas = [{"bestand": "X.md"}, {"bestand": "X.md"}]
    n_orphans = _sweep_orphans_per_bron(col, new_ids, new_metadatas)
    assert n_orphans == 0
    assert col.deleted == []


def test_orphan_sweep_negeert_bronnen_niet_in_run():
    """Bron Z.md zit in Chroma maar wordt niet aangeboden in deze run.
    De sweep mag Z.md NIET aanraken — daarvoor is `remove_bron.py` of de
    trust-cascade in mark_trusted.py.
    """
    col = FakeCollection({
        "X__art_1": "X.md",
        "Z__art_1": "Z.md",   # niet in deze run
        "Z__art_2": "Z.md",
    })
    new_ids = ["X__art_1"]
    new_metadatas = [{"bestand": "X.md"}]
    n_orphans = _sweep_orphans_per_bron(col, new_ids, new_metadatas)
    assert n_orphans == 0
    assert col.deleted == []
    # Z.md-chunks blijven
    assert "Z__art_1" in col.store
    assert "Z__art_2" in col.store


def test_orphan_sweep_meerdere_bronnen_in_één_run():
    """Meerdere bronnen tegelijk: sweep per bron geïsoleerd."""
    col = FakeCollection({
        "X__art_1": "X.md",
        "X__art_oud": "X.md",
        "Y__sec_a": "Y.md",
        "Y__sec_oud": "Y.md",
    })
    new_ids = ["X__art_1", "Y__sec_a"]
    new_metadatas = [{"bestand": "X.md"}, {"bestand": "Y.md"}]
    n_orphans = _sweep_orphans_per_bron(col, new_ids, new_metadatas)
    assert n_orphans == 2
    assert set(col.deleted) == {"X__art_oud", "Y__sec_oud"}


def test_orphan_sweep_lege_input_doet_niets():
    col = FakeCollection({"X__art_1": "X.md"})
    n_orphans = _sweep_orphans_per_bron(col, [], [])
    assert n_orphans == 0
    assert col.deleted == []


def test_orphan_sweep_overleeft_chroma_exception():
    """Als collection.get of .delete faalt, mag de sweep niet crashen."""

    class FailingCollection:
        def __init__(self):
            self.deleted = []

        def get(self, where, include):
            raise RuntimeError("Chroma down")

        def delete(self, ids):
            raise RuntimeError("Chroma down")

    col = FailingCollection()
    n_orphans = _sweep_orphans_per_bron(col, ["X__art_1"], [{"bestand": "X.md"}])
    # Geen crash, 0 verwijderingen
    assert n_orphans == 0
