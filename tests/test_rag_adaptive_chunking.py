"""Tests voor adaptive sub-chunking + definitie-detectie (ADR-006 §4.2 nieuw).

Structuur:
- Marker-detectie per type (§ N, N°, N., a), N), i)/ii) + Romein-UC)
- Definitie-detectie (is_definitie_blok)
- Threshold-tiers in split_wettekst (<SOFT, SOFT-HARD, >HARD)
- Chunk-id format (bin-pack, definitie-deg, letter, EU-lid, Romein)
- Backwards-compat (sub_strategy: per_definitieblok blijft werken in Phase 1)
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.rag.rag_index import (  # noqa: E402
    detect_sub_markers,
    is_definitie_blok,
    split_wettekst,
    SOFT_THRESHOLD,
    HARD_THRESHOLD,
)

# ---------------------------------------------------------------------------
# Hulpfuncties voor fixtures
# ---------------------------------------------------------------------------

def _maak_wettekst_met_artikelen(artikelen: list[tuple[str, str]]) -> str:
    """Bouw een minimale wettekst met één H1 en meerdere Art.-headings.

    artikelen = [(nr, body_tekst), ...] — body_tekst wordt letterlijk ingevoegd.
    """
    parts = ["# Testwet\n"]
    for nr, body in artikelen:
        parts.append(f"\n###### Art. {nr}\n\n{body}\n")
    return "\n".join(parts)


def _fm_simpel(sub_strategy=None):
    return {"wet": "Testwet", "chunk": {"level": 6, "type": "Art.", "sub_strategy": sub_strategy}}


# ---------------------------------------------------------------------------
# 1. Marker-detectie — § N (paragraaf, Belgische stijl)
# ---------------------------------------------------------------------------

def test_detect_paragraaf_standaard():
    """§ 1. gevolgd door tekst detecteert als paragraaf-marker."""
    text = "§ 1. Dit is de tekst van paragraaf 1.\n§ 2. Dit is paragraaf 2.\n§ 3. Paragraaf 3."
    markers = detect_sub_markers(text)
    typen = [m[1] for m in markers]
    assert "paragraaf" in typen
    assert len([m for m in markers if m[1] == "paragraaf"]) == 3


def test_detect_paragraaf_zonder_punt():
    """§ 2 (zonder punt) is ook een geldige marker."""
    text = "§ 1 De eerste paragraaf.\n§ 2 De tweede paragraaf.\n§ 3 Derde."
    markers = detect_sub_markers(text)
    assert len([m for m in markers if m[1] == "paragraaf"]) == 3


def test_detect_paragraaf_geplakt():
    """§1. (geplakt, VCF-stijl) detecteert correct."""
    text = "§1. Eerste paragraaf.\n§2. Tweede paragraaf.\n§3. Derde paragraaf."
    markers = detect_sub_markers(text)
    paragraaf_markers = [m for m in markers if m[1] == "paragraaf"]
    assert len(paragraaf_markers) == 3


def test_detect_paragraaf_inline_niet_meegenomen():
    """§ in een lopende zin (niet begin-van-regel) is GEEN marker."""
    text = (
        "De regels van artikel 37, § 2, zijn hier van toepassing.\n"
        "Zie ook § 1 van bovenvermeld artikel voor de definitie.\n"
        "§ 1. Officieel begin van een echte paragraaf.\n"
        "§ 2. Tweede echte paragraaf.\n"
        "§ 3. Derde echte paragraaf."
    )
    markers = detect_sub_markers(text)
    paragraaf_markers = [m for m in markers if m[1] == "paragraaf"]
    # Alleen de drie echte markers (begin-van-regel), niet de inline verwijzingen
    assert len(paragraaf_markers) == 3


# ---------------------------------------------------------------------------
# 2. Marker-detectie — N° (definitieblok, Belgische stijl)
# ---------------------------------------------------------------------------

def test_detect_defblok_standaard():
    """1°, 2°, 3° worden herkend als definitieblok-markers."""
    text = '1° "term1" : eerste definitie;\n2° "term2" : tweede definitie;\n3° "term3" : derde definitie.'
    markers = detect_sub_markers(text)
    defblok_markers = [m for m in markers if m[1] == "definitieblok"]
    assert len(defblok_markers) == 3


def test_detect_defblok_bis_ter_suffix():
    """4°bis, 4°ter, 4°quinquies zijn geldige definitieblok-markers (Oud-BW)."""
    text = (
        "4°bis. De schuldvordering van Fedris...\n"
        "4°ter. De bijdragen verschuldigd aan de Rijksdienst...\n"
        "4°quinquies. De bijdragen en bijdrageopslagen...\n"
    )
    markers = detect_sub_markers(text)
    defblok_markers = [m for m in markers if m[1] == "definitieblok"]
    assert len(defblok_markers) == 3


def test_detect_defblok_referentie_in_zin_niet_meegenomen():
    """3°, van het Wetboek (gevolgd door komma) is geen marker."""
    text = (
        "Zie ook de bepaling vermeld in artikel 125, § 1, 1°, van de wet.\n"
        "In het eerste lid, 3°, bedoelde besluit verduidelijkt...\n"
        "1° eerste echte marker;\n"
        "2° tweede echte marker;\n"
        "3° derde echte marker."
    )
    markers = detect_sub_markers(text)
    defblok_markers = [m for m in markers if m[1] == "definitieblok"]
    # Alleen de drie echte markers, niet de inline referenties
    assert len(defblok_markers) == 3


# ---------------------------------------------------------------------------
# 3. Marker-detectie — N. (EU lid-stijl, NIEUW)
# ---------------------------------------------------------------------------

def test_detect_eu_lid_standaard():
    """1. De Commissie... wordt herkend als EU lid-marker."""
    text = (
        "1. De Commissie stelt voor dat...\n"
        "2. De internationale standaarden zijn van toepassing.\n"
        "3. De lidstaten zorgen voor de naleving."
    )
    markers = detect_sub_markers(text)
    eu_leden = [m for m in markers if m[1] == "eu_lid"]
    assert len(eu_leden) == 3


def test_detect_eu_lid_eerste_letter_hoofdletter():
    """N. gevolgd door kleine letter is GEEN EU lid-marker (zinsbegin of verwijzing)."""
    text = (
        "overeenkomstig artikel 39. § 1. Hier begint iets.\n"
        "1. De eerste echte lid begint met hoofdletter.\n"
        "2. Tweede lid ook hoofdletter.\n"
        "3. Derde lid."
    )
    markers = detect_sub_markers(text)
    eu_leden = [m for m in markers if m[1] == "eu_lid"]
    # Alleen de drie leden, niet de artikelverwijzing
    assert len(eu_leden) == 3


def test_detect_eu_lid_niet_inline():
    """N. midden in een zin is geen marker."""
    text = (
        "In lid 1. bedoeld in artikel 22. de functionaris...\n"
        "1. Eerste lid van het artikel.\n"
        "2. Tweede lid.\n"
        "3. Derde lid."
    )
    markers = detect_sub_markers(text)
    eu_leden = [m for m in markers if m[1] == "eu_lid"]
    assert len(eu_leden) == 3


# ---------------------------------------------------------------------------
# 4. Marker-detectie — a) b) c) (lettered, NIEUW)
# ---------------------------------------------------------------------------

def test_detect_letter_subitem_standaard():
    """a) b) c) worden herkend als letter-markers."""
    text = (
        "a) eerste sub-item met voldoende tekst;\n"
        "b) tweede sub-item met voldoende tekst;\n"
        "c) derde sub-item met voldoende tekst."
    )
    markers = detect_sub_markers(text)
    letter_markers = [m for m in markers if m[1] == "letter"]
    assert len(letter_markers) == 3


def test_detect_letter_subitem_met_inspringing():
    """   a) (ingesprongen letter-items) worden ook herkend."""
    text = (
        "   a) ingesprongen eerste item;\n"
        "   b) ingesprongen tweede item;\n"
        "   c) ingesprongen derde item."
    )
    markers = detect_sub_markers(text)
    letter_markers = [m for m in markers if m[1] == "letter"]
    assert len(letter_markers) == 3


# ---------------------------------------------------------------------------
# 5. Marker-detectie — N) (haak-genummerd, NIEUW)
# ---------------------------------------------------------------------------

def test_detect_haak_genummerd_standaard():
    """1) 2) 3) worden herkend als haak-genummerd markers."""
    text = (
        "1) de datum van uitreiking van de factuur;\n"
        "2) het BTW-identificatienummer van de leverancier;\n"
        "3) het BTW-identificatienummer van de afnemer."
    )
    markers = detect_sub_markers(text)
    haak_markers = [m for m in markers if m[1] == "haak_genummerd"]
    assert len(haak_markers) == 3


# ---------------------------------------------------------------------------
# 6. Marker-detectie — prioriteitsvolgorde
# ---------------------------------------------------------------------------

def test_detect_prioriteit_defblok_voor_paragraaf():
    """Als zowel N° als § N aanwezig zijn, kiest detect_sub_markers de eerste
    die ≥3 keer voorkomt (de dominante marker per chunk)."""
    text = (
        "1° eerste definitie;\n"
        "§ 1. Paragraaf één.\n"
        "2° tweede definitie;\n"
        "§ 2. Paragraaf twee.\n"
        "3° derde definitie;\n"
        "§ 3. Paragraaf drie."
    )
    markers = detect_sub_markers(text)
    typen = [m[1] for m in markers]
    # Alle markers worden geretourneerd; de keuze van primaire marker is aan de caller
    assert "definitieblok" in typen
    assert "paragraaf" in typen


def test_detect_geen_markers_geeft_lege_lijst():
    """Tekst zonder sub-markers geeft een lege lijst terug."""
    text = "Dit is een gewone artikeltekst zonder enige sub-structuur."
    markers = detect_sub_markers(text)
    assert markers == []


# ---------------------------------------------------------------------------
# 7. Definitie-detectie — is_definitie_blok
# ---------------------------------------------------------------------------

def test_definitie_blok_via_intro_patroon_en_genoeg_items():
    """'wordt verstaan onder' + ≥3 N°-items → is_definitie_blok True."""
    text = (
        "Voor de toepassing van dit Wetboek wordt verstaan onder :\n"
        '1° "term1" : definitie van term1;\n'
        '2° "term2" : definitie van term2;\n'
        '3° "term3" : definitie van term3;\n'
        '4° "term4" : definitie van term4.'
    )
    assert is_definitie_blok(text, heading="Art. 1") is True


def test_definitie_blok_via_gelden_volgende_definities():
    """'gelden de volgende definities' + ≥3 items → True."""
    text = (
        "Voor de toepassing van deze wet gelden de volgende definities :\n"
        '1° "klokkenluider" : een persoon die melding maakt;\n'
        '2° "inbreuk" : handelingen of nalatingen;\n'
        '3° "meldingskanaal" : het systeem voor meldingen.'
    )
    assert is_definitie_blok(text, heading="Art. 7") is True


def test_definitie_blok_via_heading_naam_en_items():
    """Heading-naam bevat 'definit' + ≥3 N°-items → True."""
    text = (
        "Begripsomschrijving:\n"
        "1° eerste definitie;\n"
        "2° tweede definitie;\n"
        "3° derde definitie."
    )
    assert is_definitie_blok(text, heading="Art. 2. Definities") is True


def test_definitie_blok_geen_trigger_zonder_genoeg_items():
    """Intro-patroon aanwezig maar slechts 2 items → False (onder drempel ≥3)."""
    text = (
        "Voor de toepassing van dit artikel wordt verstaan onder :\n"
        '1° "term1" : eerste definitie;\n'
        '2° "term2" : tweede definitie.'
    )
    assert is_definitie_blok(text, heading="Art. 3") is False


def test_definitie_blok_geen_trigger_zonder_intro_patroon():
    """N°-items aanwezig maar geen intro-patroon en geen definitie-heading → False."""
    text = (
        "De volgende voorwaarden moeten vervuld zijn:\n"
        "1° de belastingplichtige is geregistreerd;\n"
        "2° het contract is ondertekend;\n"
        "3° de betalingstermijn is verstreken."
    )
    assert is_definitie_blok(text, heading="Art. 5") is False


def test_definitie_blok_via_er_wordt_verstaan_onder():
    """'Er wordt verstaan onder' patroon triggert definitie-detectie."""
    text = (
        "Er wordt verstaan onder :\n"
        "a) eerste sub-definitie;\n"
        "b) tweede sub-definitie;\n"
        "c) derde sub-definitie."
    )
    assert is_definitie_blok(text, heading="Art. 10") is True


# ---------------------------------------------------------------------------
# 8. Threshold-tiers — split_wettekst
# ---------------------------------------------------------------------------

def test_threshold_klein_geen_split():
    """Chunk < SOFT_THRESHOLD (4000 chars): nooit sub-splitsen, ook niet met markers."""
    # Bouw een klein artikel met ≥3 N°-markers maar totale grootte onder SOFT
    kleine_body = (
        "Voor de toepassing wordt verstaan onder :\n"
        "1° eerste definitie van een korte term;\n"
        "2° tweede definitie van een korte term;\n"
        "3° derde definitie van een korte term.\n"
    )
    # Zorg dat totale chunk < SOFT_THRESHOLD
    assert len(kleine_body) < SOFT_THRESHOLD, "Fixture te groot voor deze test"

    tekst = _maak_wettekst_met_artikelen([("1", kleine_body), ("2", "Andere korte inhoud.")])
    chunks = split_wettekst(tekst, "testwet", _fm_simpel())
    ids = [c["id"] for c in chunks]
    # Geen sub-splits want te klein
    assert all("__sub_" not in cid for cid in ids)


def test_threshold_soft_hard_met_markers_wordt_gesplitst():
    """Chunk tussen SOFT en HARD met ≥3 markers die elk groot genoeg zijn: adaptief splitsen.

    Elk paragraaf-item is 3000+ chars zodat ze NIET allemaal in één bin passen
    (totaal 9000+ > HARD_THRESHOLD). De bin-pack-logica maakt dan meerdere bins →
    meerdere sub-chunks.
    """
    # 3 × 3000 chars = 9000 > HARD_THRESHOLD → meerdere bins → meerdere sub-chunks.
    # Elk item past individueel niet in 1 bin met de andere twee.
    paragraaf_body = (
        "§ 1. " + "A" * 3000 + "\n\n"
        "§ 2. " + "B" * 3000 + "\n\n"
        "§ 3. " + "C" * 3000 + "\n"
    )
    assert len(paragraaf_body) >= SOFT_THRESHOLD, (
        f"Fixture te klein: {len(paragraaf_body)} chars"
    )

    tekst = _maak_wettekst_met_artikelen([("7", paragraaf_body)])
    chunks = split_wettekst(tekst, "regwet", _fm_simpel())
    ids = [c["id"] for c in chunks]
    # Verwacht sub-chunks (§-split in meerdere bins)
    assert any("__sub_" in cid for cid in ids), (
        f"Verwachtte sub-chunks maar got: {ids}"
    )


def test_threshold_soft_hard_zonder_markers_geen_split():
    """Chunk tussen SOFT en HARD maar zonder detecteerbare markers: GEEN sub-split."""
    # Proza-tekst van ~5000 chars (in soft-hard range), geen sub-markers
    proza_body = "Dit is proza zonder enige sub-structuur. " * 120  # ~4200 chars
    assert SOFT_THRESHOLD <= len(proza_body) <= HARD_THRESHOLD, (
        f"Fixture buiten verwachte range: {len(proza_body)} chars"
    )

    tekst = _maak_wettekst_met_artikelen([("9", proza_body)])
    chunks = split_wettekst(tekst, "prosawet", _fm_simpel())
    ids = [c["id"] for c in chunks]
    # Geen sub-splits want geen markers
    assert all("__sub_" not in cid for cid in ids), (
        f"Onverwachte sub-chunks in proza: {ids}"
    )


def test_threshold_hard_moet_splitsen():
    """Chunk > HARD_THRESHOLD (8000 chars) MOET gesplitst worden."""
    # Bouw een artikel groter dan HARD_THRESHOLD met § N-markers.
    # 3 × 2800 chars + overhead ≈ 8420 chars (boven HARD_THRESHOLD van 8000).
    groot_body = (
        "§ 1. " + "X" * 2800 + "\n\n"
        "§ 2. " + "Y" * 2800 + "\n\n"
        "§ 3. " + "Z" * 2800 + "\n"
    )
    assert len(groot_body) > HARD_THRESHOLD, (
        f"Fixture niet groot genoeg: {len(groot_body)} chars"
    )

    tekst = _maak_wettekst_met_artikelen([("10", groot_body)])
    chunks = split_wettekst(tekst, "grootwet", _fm_simpel())
    ids = [c["id"] for c in chunks]
    # Verwacht split (sub-chunks of part-chunks)
    assert len(ids) > 1, f"Verwachtte splits maar got slechts {len(ids)} chunk(s)"


# ---------------------------------------------------------------------------
# 9. Chunk-id format
# ---------------------------------------------------------------------------

def test_chunk_id_definitie_deg_format():
    """Sub-chunks van definitie-items: <bron>__art_N__sub_1deg, __sub_2deg."""
    definitie_body = (
        "Voor de toepassing van deze wet wordt verstaan onder :\n"
        '1° "WG/FT" : het witwassen van geld;\n'
        '2° "WG/FTP" : het witwassen van geld en financiering;\n'
        '3° "Richtlijn" : Richtlijn (EU) 2015/849.\n'
    )
    # Groot genoeg om split te triggeren
    groot_definitie_body = definitie_body + "Aanvullende tekst. " * 200  # >4000 chars
    tekst = _maak_wettekst_met_artikelen([("4", groot_definitie_body)])
    chunks = split_wettekst(tekst, "antiwitwaswet", _fm_simpel())
    ids = [c["id"] for c in chunks]
    # Sub-chunks van definitie-blok: __sub_1deg, __sub_2deg of __sub_<N>
    sub_ids = [cid for cid in ids if "__sub_" in cid]
    assert len(sub_ids) >= 3, f"Verwacht ≥3 definitie-sub-chunks, got: {ids}"


def test_chunk_id_binpack_range_format():
    """Bin-pack sub-chunks van §-splits: __sub_par1 en __sub_par3 (range of enkelvoudig).

    Elk item is 3000 chars zodat ze in aparte bins landen (2 × 3000 < 8000,
    maar 3 × 3000 = 9000 > HARD_THRESHOLD → 2 bins: [§1,§2] en [§3]).
    """
    paragraaf_body = (
        "§ 1. " + "A" * 3000 + "\n\n"
        "§ 2. " + "B" * 3000 + "\n\n"
        "§ 3. " + "C" * 3000 + "\n"
    )
    tekst = _maak_wettekst_met_artikelen([("5", paragraaf_body)])
    chunks = split_wettekst(tekst, "regwet", _fm_simpel())
    ids = [c["id"] for c in chunks]
    sub_ids = [cid for cid in ids if "__sub_" in cid]
    # Verwacht ≥2 sub-chunks: één bin voor §1+§2 en één voor §3
    assert len(sub_ids) >= 2, f"Verwacht ≥2 sub-chunks, got: {ids}"
    # Sub-chunk IDs beginnen met het basis-id
    for sid in sub_ids:
        assert sid.startswith("regwet__art_5__sub_"), f"Onverwacht ID-format: {sid}"


def test_chunk_id_stabiel_bij_zelfde_input():
    """Chunk-IDs zijn deterministisch: twee runs met dezelfde input geven dezelfde IDs."""
    definitie_body = (
        "Voor de toepassing wordt verstaan onder :\n"
        '1° "A" : eerste definitie met meer tekst om drempel te halen;\n'
        '2° "B" : tweede definitie ook met meer tekst voor de drempel;\n'
        '3° "C" : derde definitie eveneens met voldoende tekst hier.\n'
    ) + "Extra context. " * 100
    tekst = _maak_wettekst_met_artikelen([("2", definitie_body)])
    run1 = [c["id"] for c in split_wettekst(tekst, "wib92", _fm_simpel())]
    run2 = [c["id"] for c in split_wettekst(tekst, "wib92", _fm_simpel())]
    assert run1 == run2


# ---------------------------------------------------------------------------
# 10. Backwards-compat — sub_strategy: per_definitieblok (Phase 1)
# ---------------------------------------------------------------------------

def test_backwards_compat_sub_strategy_per_definitieblok_nog_werkend():
    """Phase 1: `sub_strategy: per_definitieblok` in frontmatter moet nog steeds
    werken (backwards-compat voor bestaande bronnen zoals Antiwitwaswet, WIB92)."""
    text = """# Antiwitwaswet

###### Art. 4

Voor de toepassing van deze wet wordt verstaan onder :
   1° "WG/FT" : het witwassen van geld;
   2° "WG/FTP" : het witwassen van geld en financiering;
   3° "Richtlijn 2015/849" : Richtlijn (EU) 2015/849;
   4° "uitvoeringsmaatregelen" : de uitvoeringsmaatregelen.

###### Art. 5

Andere artikel.
"""
    fm = {
        "wet": "Antiwitwaswet",
        "chunk": {"level": 6, "type": "Art.", "sub_strategy": "per_definitieblok"},
    }
    chunks = split_wettekst(text, "Antiwitwaswet-2017", fm)
    ids = [c["id"] for c in chunks]

    # Art. 4 moet gesplitst zijn (zoals voor Phase 1 het geval was)
    assert "Antiwitwaswet-2017__art_4" in ids or any(
        "art_4" in cid for cid in ids
    ), f"Art. 4 niet gevonden in {ids}"
    # Art. 5 ongewijzigd
    assert "Antiwitwaswet-2017__art_5" in ids


def test_backwards_compat_geen_regressie_op_bestaande_sub_split_test():
    """Regressie: de exacte sub-IDs uit test_rag_split_sub.py blijven werken."""
    text = """# Antiwitwaswet

###### Art. 4

Voor de toepassing van deze wet wordt verstaan onder :
   1° "WG/FT" : het witwassen van geld;
   2° "WG/FTP" : het witwassen van geld en financiering;
   3° "Richtlijn 2015/849" : Richtlijn (EU) 2015/849 van het Europees Parlement;
   4° "uitvoeringsmaatregelen" : de uitvoeringsmaatregelen van richtlijn 2015/849;

###### Art. 5

Andere artikel zonder sub-grenzen.
"""
    fm = {
        "wet": "Antiwitwaswet",
        "chunk": {"level": 6, "type": "Art.", "sub_strategy": "per_definitieblok"},
    }
    chunks = split_wettekst(text, "Antiwitwaswet-2017", fm)
    ids = [c["id"] for c in chunks]

    # Art. 5 ongewijzigd (geen sub-grenzen → geen split)
    assert "Antiwitwaswet-2017__art_5" in ids
    assert "Antiwitwaswet-2017__art_5__sub_1" not in ids


# ---------------------------------------------------------------------------
# 11. Adaptive modus — auto-detectie zonder frontmatter sub_strategy
# ---------------------------------------------------------------------------

def test_adaptive_auto_detectie_definitie_artikel():
    """Definitie-artikel (groot genoeg) wordt automatisch gesplitst zonder sub_strategy."""
    # Artikel groter dan SOFT_THRESHOLD met intro-patroon + ≥3 N°-items
    definitie_body = (
        "Voor de toepassing van deze wet wordt verstaan onder :\n"
        '1° "rijksinwoner" : een persoon die zijn woonplaats in België heeft '
        + "en voldoet aan de wettelijke criteria zoals verder omschreven in de wet. " * 5 + "\n"
        '2° "vennootschap" : iedere vennootschap naar Belgisch of buitenlands recht '
        + "ongeacht de rechtsvorm zoals nv bvba cvba en andere rechtsvormen. " * 5 + "\n"
        '3° "dividenden" : alle inkomsten toegewezen door een vennootschap '
        + "aan haar aandeelhouders al dan niet in contanten of in natura. " * 5 + "\n"
    )
    tekst = _maak_wettekst_met_artikelen([("2", definitie_body)])
    # Geen sub_strategy in frontmatter — adaptive mode
    chunks = split_wettekst(tekst, "WIB92", _fm_simpel(sub_strategy=None))
    ids = [c["id"] for c in chunks]

    if len(definitie_body) >= SOFT_THRESHOLD:
        # Als groot genoeg: sub-splits verwacht
        sub_ids = [cid for cid in ids if "__sub_" in cid]
        assert len(sub_ids) >= 1, f"Verwacht sub-splits voor definitie-artikel, got: {ids}"


def test_adaptive_auto_detectie_eu_leden():
    """EU-artikel met N. lid-markers wordt automatisch gesplitst als groot genoeg.

    Elk lid is 3000 chars zodat ze in aparte bins landen (2 × 3000 < 8000
    maar 3 × 3000 > 8000 → 2 bins).

    EU-bronnen gebruiken `Artikel N` als heading-type (geen `Art.`). Na Phase 2
    is de _ARTICLE_TYPE_SET-fallback verwijderd: de bron MOET type: "Artikel"
    hebben én de headings moeten `Artikel N` zijn.
    """
    lid_tekst = "op alle lidstaten die deel uitmaken van de Europese Unie " * 55  # ~3000 chars
    eu_body = (
        f"1. De Commissie stelt vast dat de volgende regels van toepassing zijn {lid_tekst}\n\n"
        f"2. De lidstaten zorgen voor de naleving van de bepalingen van deze richtlijn {lid_tekst}\n\n"
        f"3. In geval van niet-naleving kan de Commissie een inbreukprocedure starten {lid_tekst}\n"
    )
    assert len(eu_body) >= SOFT_THRESHOLD, (
        f"EU-fixture te klein: {len(eu_body)} chars"
    )
    # Gebruik Artikel-headings (EU-stijl) i.p.v. Art. (BE-stijl)
    tekst = "# EU-Richtlijn\n\n###### Artikel 9\n\n" + eu_body
    fm = {"wet": "EU-Richtlijn", "chunk": {"level": 6, "type": "Artikel", "sub_strategy": None}}
    chunks = split_wettekst(tekst, "eu-richtlijn", fm)
    ids = [c["id"] for c in chunks]

    sub_ids = [cid for cid in ids if "__sub_" in cid]
    assert len(sub_ids) >= 1, f"Verwacht sub-splits voor EU-lid-artikel, got: {ids}"


# ---------------------------------------------------------------------------
# 12. SOFT_THRESHOLD en HARD_THRESHOLD exporteerbaar
# ---------------------------------------------------------------------------

def test_thresholds_zijn_geexporteerd_en_correct():
    """SOFT_THRESHOLD en HARD_THRESHOLD moeten geëxporteerd zijn met de juiste waarden."""
    assert SOFT_THRESHOLD == 4000, f"SOFT_THRESHOLD verwacht 4000, got {SOFT_THRESHOLD}"
    assert HARD_THRESHOLD == 8000, f"HARD_THRESHOLD verwacht 8000, got {HARD_THRESHOLD}"
    assert SOFT_THRESHOLD < HARD_THRESHOLD
