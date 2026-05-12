"""Unit-tests voor `tools.lib.extractors.pymupdf_wetboek`.

Focus op pure-functie helpers (geen PDF-IO nodig):
- `_clean_block_text(text, eu_mode)` — whitespace + EUR-Lex marker stripping
- `_is_noise_block(text, eu_mode)` — PB-header detection

Volle pipeline-tests via `tests/test_pipeline_snapshots_slow.py` (vereist PDF).
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.lib.extractors.pymupdf_wetboek import _clean_block_text  # noqa: E402


# ─── EUR-Lex amendment-markers ────────────────────────────────────────────────

def test_clean_strips_basistekst_marker():
    """►B en ▼B (basistekst) worden gestript in eu_mode."""
    assert _clean_block_text("►B foo bar", eu_mode=True) == "foo bar"
    assert _clean_block_text("▼B foo bar", eu_mode=True) == "foo bar"


def test_clean_strips_modification_marker_M_with_digit():
    """►M1..M9 en ▼M1..M9 (modification) worden gestript."""
    assert _clean_block_text("►M1 foo", eu_mode=True) == "foo"
    assert _clean_block_text("▼M7 foo", eu_mode=True) == "foo"


def test_clean_strips_correction_marker_C_with_digit():
    """►C1..C3 en ▼C1..C3 (correction/rectification) — REGRESSIE-FIX (2026-05-12).

    Richtlijn-2013-34-EU bevat 23 dergelijke markers (►M1-M7, ►C1-C3, ▼C1-C3).
    De originele regex `[►▼][BM]\\d*` miste de C-variant.
    """
    assert _clean_block_text("►C1 foo", eu_mode=True) == "foo"
    assert _clean_block_text("▼C1 foo", eu_mode=True) == "foo"
    assert _clean_block_text("►C3 bar baz", eu_mode=True) == "bar baz"


def test_clean_strips_close_marker_after_bracketed_inline():
    """Inline-bracketing: `►C1 X ◄` → de `◄` close-marker moet ook weg.

    Voorbeeld uit Richtlijn-2013-34-EU r469:
      `... bestanddelen met inbegrip van ►C1 beleggingen ◄, worden ...`
    Verwachte cleanup: open-marker (►C1) + close-marker (◄) beide weg.
    """
    result = _clean_block_text(
        "bestanddelen met inbegrip van ►C1 beleggingen ◄, worden berekend",
        eu_mode=True,
    )
    # Geen ►, ◄ of ▼ meer in result
    assert "►" not in result
    assert "◄" not in result
    assert "▼" not in result
    # Inhoud blijft
    assert "beleggingen" in result
    assert "berekend" in result


def test_clean_eu_mode_off_leaves_markers_intact():
    """Default mode (eu_mode=False) raakt de markers NIET aan."""
    text = "►C1 foo ◄ ▼M1 bar"
    result = _clean_block_text(text, eu_mode=False)
    # Markers blijven aanwezig (alleen whitespace-normalisatie)
    assert "►C1" in result
    assert "◄" in result
    assert "▼M1" in result


def test_clean_does_not_break_normal_text():
    """Geen valse positieven: gewone tekst zonder markers blijft intact."""
    text = "Artikel 5. Deze richtlijn is van toepassing op natuurlijke personen."
    assert _clean_block_text(text, eu_mode=True) == text
    assert _clean_block_text(text, eu_mode=False) == text


def test_clean_strips_multiple_markers_in_one_block():
    """Meerdere markers in één blok (typisch in concordantietabellen)."""
    text = "►M1 foo ►C2 bar ▼M3 baz"
    result = _clean_block_text(text, eu_mode=True)
    assert "►" not in result
    assert "▼" not in result
    assert "foo" in result
    assert "bar" in result
    assert "baz" in result


# ─── Idempotentie ────────────────────────────────────────────────────────────

def test_clean_is_idempotent():
    """Tweede call op output verandert niets meer."""
    text = "►C1 beleggingen ◄, worden berekend"
    once = _clean_block_text(text, eu_mode=True)
    twice = _clean_block_text(once, eu_mode=True)
    assert once == twice


def test_clean_strips_marker_with_whitespace_between_arrow_and_code():
    """In sommige PDF-extracties staat een SPATIE tussen ► en de letter-cijfer-code:
    `► M1`, `► C1`. Komt voor in wijzigingsoverzicht-tabellen.

    Voorbeeld uit Richtlijn-2013-34-EU r53:
      `► M1  Richtlijn 2014/95/EU van het Europees Parlement ...`
    """
    assert _clean_block_text("► M1 Richtlijn 2014/95", eu_mode=True).strip() == "Richtlijn 2014/95"
    assert _clean_block_text("► C1 foo", eu_mode=True).strip() == "foo"
    assert _clean_block_text("▼ M3 bar", eu_mode=True).strip() == "bar"


# ─── PB-header detection (_is_noise_block) ────────────────────────────────────

def test_is_noise_pb_header_modern_NL_prefix():
    """Moderne PB-header: 'NL   L 77/4  Publicatieblad van de Europese Unie  23.3.2011'."""
    from tools.lib.extractors.pymupdf_wetboek import _is_noise_block
    assert _is_noise_block(
        "NL   L 77/4  Publicatieblad van de Europese Unie  23.3.2011",
        eu_mode=True,
    )


def test_is_noise_pb_header_modern_date_prefix():
    """PB-header met datum-prefix: '11.9.2002 L 243/1 Publicatieblad ... NL'."""
    from tools.lib.extractors.pymupdf_wetboek import _is_noise_block
    assert _is_noise_block(
        "11.9.2002 L 243/1 Publicatieblad van de Europese Gemeenschappen NL",
        eu_mode=True,
    )


def test_is_noise_pb_header_legacy_Nr_prefix_with_spaces():
    """Oudere PB-header (1986-stijl): 'Nr . L 326 / 40 Publikatieblad ... 21 . 11 . 86'.

    REGRESSIE-FIX: BTW-dertiende-richtlijn-1986 had deze niet-gestripte header
    op regel 46. Bevat:
    - `Nr . L` prefix (i.p.v. `NL` of datum)
    - spaties IN datum (`21 . 11 . 86`)
    - oude spelling `Publikatieblad` (k)
    - jaar 2-cijfers (`86` i.p.v. `1986`)
    """
    from tools.lib.extractors.pymupdf_wetboek import _is_noise_block
    assert _is_noise_block(
        "Nr . L 326 / 40 Publikatieblad van de Europese Gemeenschappen 21 . 11 . 86",
        eu_mode=True,
    )


def test_is_noise_pb_header_legacy_date_with_spaces_2digit_year():
    """Legacy PB-header met datum-prefix MET SPATIES en 2-cijfer jaar.

    Voorbeeld uit BTW-dertiende-richtlijn-1986: omgekeerde header-volgorde met
    datum eerst, en spaties tussen datumcomponenten:
      '21 . 11 . 86 Publikatieblad van de Europese Gemeenschappen Nr . L 326 / 41'
    """
    from tools.lib.extractors.pymupdf_wetboek import _is_noise_block
    assert _is_noise_block(
        "21 . 11 . 86 Publikatieblad van de Europese Gemeenschappen Nr . L 326 / 41",
        eu_mode=True,
    )


def test_is_noise_does_not_match_legitimate_content():
    """Geen valse positieven: normale wettekst niet als noise behandelen."""
    from tools.lib.extractors.pymupdf_wetboek import _is_noise_block
    assert not _is_noise_block(
        "Deze richtlijn is van toepassing op natuurlijke en rechtspersonen.",
        eu_mode=True,
    )
    assert not _is_noise_block(
        "Artikel 1. Voor de toepassing van deze richtlijn wordt verstaan onder...",
        eu_mode=True,
    )


def test_is_noise_eu_mode_off_does_not_strip_pb_header():
    """Zonder eu_mode worden EU-specifieke PB-headers niet als noise gevlagd."""
    from tools.lib.extractors.pymupdf_wetboek import _is_noise_block
    assert not _is_noise_block(
        "NL   L 77/4  Publicatieblad van de Europese Unie  23.3.2011",
        eu_mode=False,
    )


# ─── FR-regel stripping uit tweetalige blokken ───────────────────────────────

def test_strip_fr_lines_removes_titre_heading():
    """FR-structuurheading 'TITRE 1 er - Dispositions introductives' wordt gestript."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "TITEL 1 - Inleidende bepalingen \nTITRE 1 er  - Dispositions introductives"
    result = _strip_fr_lines_from_block(raw)
    assert "TITEL 1 - Inleidende bepalingen" in result
    assert "TITRE" not in result
    assert "Dispositions" not in result


def test_strip_fr_lines_removes_chapitre_heading():
    """FR-structuurheading 'Chapitre 1er - ...' wordt gestript."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "Hoofdstuk 1 - Algemene bepalingen en definities \nChapitre 1er - Dispositions générales et définitions"
    result = _strip_fr_lines_from_block(raw)
    assert "Hoofdstuk 1" in result
    assert "Chapitre" not in result


def test_strip_fr_lines_removes_duplicate_art_number():
    """Dubbel art-nummer 'Art. 1.1.0.0.1. \\nArt. 1.1.0.0.1.' → enkel bewaard."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "Art. 1.1.0.0.1. \nArt. 1.1.0.0.1."
    result = _strip_fr_lines_from_block(raw)
    # Slechts één instantie overblijft
    assert result.count("Art. 1.1.0.0.1") == 1


def test_strip_fr_lines_removes_fr_body_line():
    """FR-body-regel na NL-regel met 'Dans le présent' wordt gestript."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "In deze codex wordt verstaan onder : \nDans le présent code, il y a lieu d'entendre par :"
    result = _strip_fr_lines_from_block(raw)
    assert "In deze codex" in result
    assert "Dans le présent" not in result


def test_strip_fr_lines_preserves_pure_nl_block():
    """Zuiver NL-blok zonder FR-regels blijft volledig intact."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = ("1° belastingen en toebehoren : de belastingen in \n"
           "hoofdsom waarop deze codex van toepassing is, in \n"
           "voorkomend geval met inbegrip van de opcentiemen")
    result = _strip_fr_lines_from_block(raw)
    assert "belastingen en toebehoren" in result
    assert "hoofdsom" in result
    assert "opcentiemen" in result


def test_strip_fr_lines_removes_section_heading():
    """FR 'Section' en 'Sous-section' headings worden gestript."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "Afdeling 1 - Algemene bepalingen \nSection 1re - Dispositions générales"
    result = _strip_fr_lines_from_block(raw)
    assert "Afdeling 1" in result
    assert "Section" not in result


def test_strip_fr_lines_removes_fr_article_1er():
    """'Article 1 er' (FR art-aanduiding met 'er') wordt gestript."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "Artikel 1 \nArticle 1 er"
    result = _strip_fr_lines_from_block(raw)
    assert "Artikel 1" in result
    assert "Article 1 er" not in result


def test_strip_fr_lines_removes_titre_droit_enregistrement():
    """'TITRE I ER - DROIT D\\'ENREGISTREMENT' — bekende FR-heading in Reg.rechten."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "TITEL I - REGISTRATIERECHT \nTITRE I ER - DROIT D'ENREGISTREMENT"
    result = _strip_fr_lines_from_block(raw)
    assert "REGISTRATIERECHT" in result
    assert "DROIT" not in result
    assert "ENREGISTREMENT" not in result


def test_strip_fr_lines_no_effect_on_single_nl_line():
    """Enkelvoudige NL-regel (geen \\n) blijft ongewijzigd."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "TITEL 1 - Inleidende bepalingen"
    result = _strip_fr_lines_from_block(raw)
    assert result == raw


def test_strip_fr_lines_returns_empty_for_single_fr_line():
    """Enkelvoudige FR-only-regel (zonder \\n) → lege string (noise-filter pakt hem op)."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "Dispositions régionales (art. 3, al. 1 er , 8° de la loi spéciale)"
    result = _strip_fr_lines_from_block(raw)
    assert result == ""


def test_strip_fr_lines_returns_empty_for_single_titre_line():
    """Enkelvoudige 'TITRE ...' FR-regel → lege string."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "TITRE I ER - DROIT D'ENREGISTREMENT"
    result = _strip_fr_lines_from_block(raw)
    assert result == ""


def test_strip_fr_lines_removes_vehicules_a_moteur():
    """'VEHICULES A MOTEUR' na 'MOTORVOERTUIGEN' wordt gestript."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "MOTORVOERTUIGEN \nVEHICULES A MOTEUR"
    result = _strip_fr_lines_from_block(raw)
    assert "MOTORVOERTUIGEN" in result
    assert "VEHICULES" not in result


def test_strip_fr_lines_removes_tableau():
    """'TABLEAU I' na 'TABEL I' wordt gestript."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "TABEL I \nTABLEAU I"
    result = _strip_fr_lines_from_block(raw)
    assert "TABEL I" in result
    assert "TABLEAU" not in result


def test_strip_fr_lines_removes_droit_futur():
    """'DROIT FUTUR (à partir du 01.01.2028)' na NL-equivalent wordt gestript."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "TOEKOMSTIG RECHT (vanaf 01.01.2028) \nDROIT FUTUR (à partir du 01.01.2028)"
    result = _strip_fr_lines_from_block(raw)
    assert "TOEKOMSTIG RECHT" in result
    assert "DROIT FUTUR" not in result


# ─── Inline bilingual slash-separator stripping ───────────────────────────────

def test_strip_fr_lines_strips_inline_tableau_suffix():
    """'TABEL I   /   TABLEAU I' → 'TABEL I' (inline suffix gestript)."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "TABEL I   /   TABLEAU I \nverkrijging in rechte lijn en tussen partners / acquisition en ligne directe et entre partenaires"
    result = _strip_fr_lines_from_block(raw)
    assert "TABEL I" in result
    assert "TABLEAU" not in result
    assert "verkrijging in rechte lijn" in result
    assert "acquisition" not in result


def test_strip_fr_inline_suffix_all_caps_fr():
    """Enkelvoudige TABEL / TABLEAU-regel via _strip_fr_inline_suffix."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_inline_suffix
    assert _strip_fr_inline_suffix("TABEL II / TABLEAU II").strip() == "TABEL II"


def test_strip_fr_inline_suffix_accented():
    """Inline FR-suffix met geaccentueerde letter wordt gestript."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_inline_suffix
    result = _strip_fr_inline_suffix("belasting / impôt")
    assert "belasting" in result
    assert "impôt" not in result


def test_strip_fr_inline_suffix_acquisition():
    """Inline 'acquisition' als FR-indicator."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_inline_suffix
    result = _strip_fr_inline_suffix(
        "verkrijging in rechte lijn / acquisition en ligne directe"
    )
    assert "verkrijging" in result
    assert "acquisition" not in result


def test_strip_fr_inline_suffix_preserves_nl_after_slash():
    """Puur NL-tekst na slash wordt NIET gestript (geen FR-indicator)."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_inline_suffix
    result = _strip_fr_inline_suffix("art. 2.8.4.2.1 / geef mij een euro")
    assert "geef mij een euro" in result


def test_strip_fr_lines_returns_empty_for_single_fr_dispositions():
    """Single-line 'Dispositions régionales...' → lege string."""
    from tools.lib.extractors.pymupdf_wetboek import _strip_fr_lines_from_block
    raw = "Dispositions régionales (art. 3, al. 1 er , 8° de la loi spéciale)"
    assert _strip_fr_lines_from_block(raw) == ""
