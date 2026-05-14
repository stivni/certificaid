"""Regressie-tests voor de transformer-chain-volgorde in convert.DEFAULT_CHAINS.

In deze sessie verplaatst: `split_merged_headings` MOET vóór `inject_headings_wettekst`
lopen in elke chain die beide bevat. Vóór de fix stond split_merged_headings ERNA,
waardoor de Afdeling+Onderafdeling-merge die inject_headings produceerde, weer
ongedaan werd gemaakt.

Zie ADR-006 §4.1 (conditional flattening) en de issue-diagnose in deze sessie.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl.convert import DEFAULT_CHAINS  # noqa: E402


def test_split_merged_headings_loopt_voor_inject_headings_wettekst():
    """Voor elke chain die zowel `inject_headings_wettekst` als
    `split_merged_headings` bevat: split_merged_headings moet eerst lopen.

    Anders mergeert inject_headings Afdeling+Onderafdeling en wordt het
    daarna weer ongedaan gemaakt → de bron eindigt zonder de gewenste merge.
    """
    for method, chain in DEFAULT_CHAINS.items():
        if "inject_headings_wettekst" in chain and "split_merged_headings" in chain:
            idx_split = chain.index("split_merged_headings")
            idx_inject = chain.index("inject_headings_wettekst")
            assert idx_split < idx_inject, (
                f"Chain {method!r}: split_merged_headings moet vóór "
                f"inject_headings_wettekst lopen, maar volgorde is "
                f"split={idx_split}, inject={idx_inject}"
            )


def test_alle_wettekst_chains_bevatten_beide_transformers():
    """Sanity-check: alle chains die `inject_headings_wettekst` bevatten,
    moeten ook `split_merged_headings` hebben — anders kunnen PDF-extractie-
    artefacten (Afdeling-en-Onderafdeling op één regel) niet opgesplitst worden.
    """
    chains_with_inject = [
        m for m, c in DEFAULT_CHAINS.items() if "inject_headings_wettekst" in c
    ]
    for method in chains_with_inject:
        assert "split_merged_headings" in DEFAULT_CHAINS[method], (
            f"Chain {method!r} bevat inject_headings_wettekst maar geen "
            f"split_merged_headings — onvolledige preprocessing."
        )
