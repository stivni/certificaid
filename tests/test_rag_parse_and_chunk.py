"""Regressie-tests voor rag_index parsing en chunking.

Bevat tests voor wijzigingen die in deze sessie zijn geland:

  1. HEADING_RE slash-nummer support — `Onderafdeling 4/1`, `Art. 5/1` enz.
     Eerder werd 'nr' afgekapt op de eerste cijfer-groep en viel '/1' in 'naam'.

  2. Artikel + Klasse als article-types in ARTICLE_TYPES — voor EU-richtlijnen
     ('## Artikel 1') en MAR-rekeningstelsels ('## Klasse 1'). Zonder deze
     uitbreiding herkende parse_heading deze als structureel i.p.v. chunk-grens.

  3. index_adviezen has_headings-logica — een advies ≤40K MET `##`-headings
     moet via split_generic (per-sectie) chunken, NIET via één-blok-paragraph-cut.
     Vóór de fix: `if len(content) <= 40_000 or not re.search(...)` — door de OR
     ging een kort advies met headings toch via één-blok. Fix: `if not has_headings`.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.rag.rag_index import (  # noqa: E402
    _ARTICLE_TYPE_SET,
    HEADING_RE,
    parse_heading,
    split_generic,
    split_wettekst,
)


# ─── 1. HEADING_RE slash-nummer ──────────────────────────────────────────────


def test_heading_re_slash_in_nr_voor_onderafdeling():
    """REGRESSIE: Onderafdeling 4/1 mag niet 'nr=4, naam=/1 ...' produceren.

    Voor de fix capteerde HEADING_RE alleen `\\d+(?:bis|ter|quater)?` als
    nummer-deel. Voor `Onderafdeling 4/1. titel` werd nr=4 en `/1. titel`
    viel in naam — wat leidt tot lelijke breadcrumbs en niet-stabiele
    chunk-ids in afgeleide structuren.
    """
    result = parse_heading("###### Onderafdeling 4/1. titel")
    assert result is not None
    assert result["type"] == "ONDERAFDELING"
    assert result["nr"] == "4/1"
    assert result["naam"] == "titel"


def test_heading_re_slash_voor_artikel():
    """Art. 5/1 (ingelaste sub-artikel) moet nr=5/1 hebben, niet nr=5."""
    result = parse_heading("###### Art. 5/1")
    assert result is not None
    assert result["type"] == "Art."
    assert result["nr"] == "5/1"
    assert result["is_article"] is True


def test_heading_re_diepere_slash():
    """`Onderafdeling 4/1/2` — meerdere slash-niveaus moeten alle gecapteerd."""
    result = parse_heading("###### Onderafdeling 4/1/2. tweede subset")
    assert result is not None
    assert result["nr"] == "4/1/2"


def test_heading_re_decimale_punt_blijft_werken():
    """Regressie-vangnet: `Art. I.5` blijft werken (geen verschuiving naar slash)."""
    result = parse_heading("###### Art. I.5")
    assert result is not None
    # Romeins blijft Romeins
    assert result["nr"] == "I" or result["nr"] == "I.5", (
        f"Onverwachte nr-parsing voor 'Art. I.5': {result!r}"
    )


# ─── 2. Artikel + Klasse als article-boundary ────────────────────────────────


def test_article_type_set_bevat_alle_vier():
    """EU-richtlijnen gebruiken 'Artikel N', MAR gebruikt 'Klasse N'.

    Beide moeten als article-boundary (chunk-grens) gedetecteerd worden.
    """
    assert _ARTICLE_TYPE_SET == {"Art.", "Par.", "Artikel", "Klasse"}


def test_artikel_wordt_als_is_article_herkend():
    """## Artikel 1 (EU-AVG-stijl) moet is_article=True krijgen."""
    result = parse_heading("## Artikel 1")
    assert result is not None
    assert result["type"] == "Artikel"
    assert result["is_article"] is True


def test_klasse_wordt_als_is_article_herkend():
    """## Klasse 1 (MAR-stijl) moet is_article=True krijgen."""
    result = parse_heading("## Klasse 1: Eigen vermogen, voorzieningen ...")
    assert result is not None
    assert result["type"] == "Klasse"
    assert result["is_article"] is True


def test_hoofdstuk_blijft_structureel_niet_article():
    """## HOOFDSTUK I mag NIET als article worden gedetecteerd."""
    result = parse_heading("## HOOFDSTUK I")
    assert result is not None
    assert result["type"] == "HOOFDSTUK"
    assert result["is_article"] is False


def test_split_wettekst_chunk_op_artikel_voor_eu_bron():
    """EU-AVG-achtige bron met `## Artikel N` en `## HOOFDSTUK X`:
    chunks moeten per Artikel zijn, niet per Hoofdstuk.
    """
    body = """# AVG

## HOOFDSTUK I

intro

## Artikel 1

Eerste artikel body.

## Artikel 2

Tweede artikel body.

## HOOFDSTUK II

intro 2

## Artikel 3

Derde artikel body.
"""
    fm = {"wet": "AVG", "chunk": {"level": 2, "type": "Artikel"}}
    chunks = split_wettekst(body, "AVG-test", fm)
    # 3 artikelen → 3 chunks. Hoofdstukken zijn structureel (breadcrumb), niet chunk.
    chunk_ids = [c["id"] for c in chunks]
    assert len(chunks) == 3, f"Verwacht 3 Artikel-chunks, kreeg {chunk_ids}"
    assert all("__art_" in cid for cid in chunk_ids)


def test_split_wettekst_chunk_op_klasse_voor_mar():
    """MAR-bron met `## Klasse N`: chunks per Klasse."""
    body = """# MAR

## Klasse 1: Eigen vermogen

10 Kapitaal
100 Geplaatst kapitaal

## Klasse 2: Vaste activa

20 Oprichtingskosten
"""
    fm = {"wet": "MAR", "chunk": {"level": 2, "type": "Klasse"}}
    chunks = split_wettekst(body, "MAR-test", fm)
    assert len(chunks) == 2, f"Verwacht 2 Klasse-chunks, kreeg {[c['id'] for c in chunks]}"


# ─── 3. index_adviezen has_headings-logica (Bug 2) ───────────────────────────


def test_advies_met_headings_wordt_op_secties_gechunkt():
    """REGRESSIE-FIX: een advies met `##`-headings moet via split_generic
    chunken op heading-grenzen, niet als één blok worden behandeld.

    Vóór de fix: `if len(content) <= 40_000 or not has_headings:` — door
    de OR ging een kort advies (zoals 95% van CBN-adviezen) altijd via
    single-block + paragraph-cut, ook al waren er logische ##-secties.
    Fix: `if not has_headings:` — adviezen met headings krijgen sectie-chunks.

    Test via split_generic (de functie die wordt aangeroepen in de heading-pad).
    """
    content = """# CBN-advies 2021/10

## Inleiding

Inleidende sectie met genoeg tekst om boven MIN_CHUNK_CHARS te zitten.
""" + "Lorem ipsum dolor sit amet. " * 8 + """

## Boekhoudkundige verwerking

Tweede sectie met genoeg body-tekst voor een aparte chunk.
""" + "Consectetur adipiscing elit. " * 8 + """

## Conclusie

Derde sectie met afsluitende tekst, ruim boven de min-chars-drempel.
""" + "Sed do eiusmod tempor incididunt. " * 8

    chunks = split_generic(content, "CBN-test", breadcrumb_prefix="[CBN-advies 2021/10]")
    headings = [c["heading"] for c in chunks]
    # Drie ##-secties → drie chunks met respectievelijke headings
    assert "Inleiding" in headings
    assert "Boekhoudkundige verwerking" in headings
    assert "Conclusie" in headings
    assert len(chunks) >= 3, (
        f"Verwacht ≥3 sectie-chunks, kreeg {len(chunks)}: {headings}"
    )
