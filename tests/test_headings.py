"""Regressie-tests voor `tools.lib.headings`.

Gebruikt echte wetteksten uit `resources/bronnen/wetteksten/` om te valideren
dat de hiërarchie-detectie + conditional flattening voldoen aan de afspraken
uit ADR-005 §7 en ADR-006 §4.1.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from tools.lib.headings import (
    BELGISCHE_HIERARCHIE,
    DEFAULT_MERGE_GROUPS,
    apply_conditional_flattening,
    build_level_map,
    detect_hierarchy,
    inject_headings,
    process_wettekst,
    update_frontmatter_chunk,
)

ROOT = Path(__file__).resolve().parent.parent
WETTEKSTEN_DIR = ROOT / "resources" / "bronnen" / "wetteksten"


# ─── Helpers ────────────────────────────────────────────────────────────────

def _load(naam: str) -> str:
    path = WETTEKSTEN_DIR / naam
    return path.read_text(encoding="utf-8")


def _info_for(naam: str) -> dict:
    """Loop process_wettekst over een wettekst en geef het info-dict terug."""
    text = _load(naam)
    _, info = process_wettekst(text)
    return info


# ─── Constanten ──────────────────────────────────────────────────────────────

def test_belgische_hierarchie_volgorde():
    assert BELGISCHE_HIERARCHIE == [
        "DEEL", "BOEK", "TITEL", "HOOFDSTUK", "AFDELING", "ONDERAFDELING",
    ]


def test_default_merge_groups():
    assert ("DEEL", "BOEK") in DEFAULT_MERGE_GROUPS
    assert ("AFDELING", "ONDERAFDELING") in DEFAULT_MERGE_GROUPS


# ─── Per-wet regressie ──────────────────────────────────────────────────────

def test_wvv_hierarchie_en_merges():
    info = _info_for("WVV.md")
    assert info["ranks"] == [
        "DEEL", "BOEK", "TITEL", "HOOFDSTUK", "AFDELING", "ONDERAFDELING", "Art.",
    ]
    assert info["chunk_level"] == 6
    # Beide default merges moeten triggeren omdat 7 ranks > 5
    assert info["merge_parent"].get("BOEK") == "DEEL"
    assert info["merge_parent"].get("ONDERAFDELING") == "AFDELING"
    # reduced_ranks ≤ 5
    assert len(info["reduced_ranks"]) <= 5


def test_wet_itaa_2019_hierarchie_geen_merges():
    info = _info_for("Wet-ITAA-2019.md")
    assert info["ranks"] == ["HOOFDSTUK", "AFDELING", "ONDERAFDELING", "Art."]
    assert info["chunk_level"] == 5
    assert info["merge_parent"] == {}
    assert info["reduced_ranks"] == info["ranks"]


def test_wib92_begint_met_titel():
    info = _info_for("WIB92.md")
    # Begint met TITEL (geen DEEL) maar bevat alle lagere lagen → 5 ranks → Art. = H6
    assert info["ranks"][0] == "TITEL"
    assert "DEEL" not in info["ranks"]
    assert info["chunk_level"] == 6


def test_antiwitwaswet_2017_begint_met_boek():
    info = _info_for("Antiwitwaswet-2017.md")
    assert info["ranks"][0] == "BOEK"
    assert "DEEL" not in info["ranks"]
    assert info["chunk_level"] == 6


def test_btw_dertiende_richtlijn_geen_structuurlabels():
    info = _info_for("BTW-dertiende-richtlijn-1986.md")
    assert info["ranks"] == ["Art."]
    assert info["reduced_ranks"] == ["Art."]
    assert info["merge_parent"] == {}
    assert info["chunk_level"] == 2


# ─── Unit tests op losse functies ───────────────────────────────────────────

def test_detect_hierarchy_lege_body():
    assert detect_hierarchy("") == ["Art."]


def test_detect_hierarchy_negeert_lowercase_romein():
    # "deel van de activa" — lowercase 'v' mag niet als Romeins worden herkend
    body = "Sommige deel van de activa zijn vrijgesteld.\n"
    assert detect_hierarchy(body) == ["Art."]


def test_apply_conditional_flattening_geen_overflow():
    ranks = ["HOOFDSTUK", "AFDELING", "ONDERAFDELING", "Art."]
    reduced, merge_parent = apply_conditional_flattening(ranks)
    assert reduced == ranks
    assert merge_parent == {}


def test_apply_conditional_flattening_overflow_zeven_ranks():
    # WVV-achtige situatie
    ranks = ["DEEL", "BOEK", "TITEL", "HOOFDSTUK", "AFDELING", "ONDERAFDELING", "Art."]
    reduced, merge_parent = apply_conditional_flattening(ranks)
    assert len(reduced) == 5
    assert merge_parent["BOEK"] == "DEEL"
    assert merge_parent["ONDERAFDELING"] == "AFDELING"


def test_build_level_map_basis():
    ranks = ["HOOFDSTUK", "AFDELING", "ONDERAFDELING", "Art."]
    lm = build_level_map(ranks, merge_parent={})
    assert lm["HOOFDSTUK"] == 2
    assert lm["AFDELING"] == 3
    assert lm["ONDERAFDELING"] == 4
    assert lm["Art."] == 5


def test_build_level_map_absorbed_krijgt_zelfde_niveau():
    ranks = ["BOEK", "TITEL", "HOOFDSTUK", "AFDELING", "Art."]
    merge_parent = {"BOEK": "DEEL"}
    lm = build_level_map(ranks, merge_parent)
    assert lm["BOEK"] == 2
    assert lm["DEEL"] == 2  # absorbed → zelfde niveau als absorbing


def test_inject_headings_artikel_omzetting():
    body = "# Wet X\n\nArt. 1. Definities.\nDe wet definieert ...\n"
    level_map = {"Art.": 2}
    new_body, n = inject_headings(body, level_map, merge_parent={})
    assert "## Art. 1. Definities." in new_body
    assert n >= 1
    # H1 onaangeraakt
    assert new_body.startswith("# Wet X")


def test_inject_headings_merge_combineert_deel_en_boek():
    body = (
        "# Wet X\n\n"
        "DEEL I. Algemeen\n\n"
        "BOEK 1. Inleiding\n\n"
        "Art. 1. Definitie.\n"
    )
    # WVV-achtige config: DEEL+BOEK gemerged
    ranks = ["BOEK", "TITEL", "HOOFDSTUK", "AFDELING", "Art."]
    merge_parent = {"BOEK": "DEEL"}
    level_map = build_level_map(ranks, merge_parent)
    new_body, _ = inject_headings(body, level_map, merge_parent)
    # Verwacht een gecombineerde heading
    assert "DEEL I. Algemeen - BOEK 1. Inleiding" in new_body


def test_inject_headings_merge_herhaalt_deel_voor_alle_boeken():
    """Alle BOEKs binnen een DEEL krijgen het DEEL-prefix, niet alleen de eerste."""
    body = (
        "# Wet X\n\n"
        "DEEL I. Eerste deel\n\n"
        "BOEK 1. Eerste boek\n\n"
        "Art. 1. art1.\n\n"
        "BOEK 2. Tweede boek\n\n"
        "Art. 2. art2.\n\n"
        "BOEK 3. Derde boek\n\n"
        "Art. 3. art3.\n\n"
        "DEEL II. Tweede deel\n\n"
        "BOEK 4. Vierde boek\n\n"
        "Art. 4. art4.\n"
    )
    ranks = ["BOEK", "TITEL", "HOOFDSTUK", "AFDELING", "Art."]
    merge_parent = {"BOEK": "DEEL"}
    level_map = build_level_map(ranks, merge_parent)
    new_body, _ = inject_headings(body, level_map, merge_parent)
    # Alle 3 BOEKs binnen DEEL I krijgen DEEL I-prefix
    assert "DEEL I. Eerste deel - BOEK 1. Eerste boek" in new_body
    assert "DEEL I. Eerste deel - BOEK 2. Tweede boek" in new_body
    assert "DEEL I. Eerste deel - BOEK 3. Derde boek" in new_body
    # BOEK 4 binnen DEEL II krijgt DEEL II-prefix
    assert "DEEL II. Tweede deel - BOEK 4. Vierde boek" in new_body
    # Geen standalone BOEK-headings (zonder DEEL-prefix)
    assert "## BOEK 2." not in new_body
    assert "## BOEK 3." not in new_body
    assert "## BOEK 4." not in new_body


def test_inject_headings_geen_context_geen_prefix():
    """Als BOEK voor DEEL komt (geen context), blijft het standalone."""
    body = (
        "# Wet X\n\n"
        "BOEK 1. Eerste boek zonder DEEL ervoor\n\n"
        "Art. 1. art1.\n\n"
        "DEEL I. Eerste deel\n\n"
        "BOEK 2. Met DEEL\n\n"
        "Art. 2. art2.\n"
    )
    ranks = ["BOEK", "TITEL", "HOOFDSTUK", "AFDELING", "Art."]
    merge_parent = {"BOEK": "DEEL"}
    level_map = build_level_map(ranks, merge_parent)
    new_body, _ = inject_headings(body, level_map, merge_parent)
    # BOEK 1: standalone (geen voorafgaande DEEL)
    assert "## BOEK 1. Eerste boek zonder DEEL ervoor" in new_body
    # BOEK 2: met DEEL-prefix
    assert "DEEL I. Eerste deel - BOEK 2. Met DEEL" in new_body


# ─── Frontmatter ────────────────────────────────────────────────────────────

def test_update_frontmatter_chunk_voegt_blok_toe():
    fm = "---\ntitle: Test\nslug: test\n---\n"
    nieuw = update_frontmatter_chunk(fm, chunk_level=5)
    assert "chunk:" in nieuw
    assert "level: 5" in nieuw
    assert 'type: "Art."' in nieuw
    assert nieuw.endswith("---\n")


def test_update_frontmatter_chunk_vervangt_bestaand_blok():
    fm = (
        "---\n"
        "title: Test\n"
        "chunk:\n"
        "  level: 2\n"
        '  type: "Art."\n'
        "  sub_strategy: null\n"
        "slug: test\n"
        "---\n"
    )
    nieuw = update_frontmatter_chunk(fm, chunk_level=6)
    assert "level: 6" in nieuw
    assert "level: 2" not in nieuw
    # slug-key blijft behouden
    assert "slug: test" in nieuw


# ─── End-to-end via process_wettekst ────────────────────────────────────────

def test_process_wettekst_geeft_string_en_info():
    text = _load("Wet-ITAA-2019.md")
    nieuwe_tekst, info = process_wettekst(text)
    assert isinstance(nieuwe_tekst, str)
    assert isinstance(info, dict)
    assert set(info.keys()) >= {
        "ranks", "reduced_ranks", "merge_parent",
        "level_map", "chunk_level", "n_conversies",
    }


def test_process_wettekst_zet_chunk_blok_in_frontmatter():
    text = _load("Wet-ITAA-2019.md")
    nieuwe_tekst, info = process_wettekst(text)
    # Frontmatter moet chunk-blok bevatten met juiste level
    head = nieuwe_tekst.split("---\n", 2)[1] if nieuwe_tekst.startswith("---\n") else ""
    assert "chunk:" in head
    assert f"level: {info['chunk_level']}" in head
