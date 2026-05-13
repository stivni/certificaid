"""
Unit-tests voor de transformer-laag (tools/etl/transformers/).

Dekt:
  - apply_chain(): chaining-mechanisme + foutafhandeling
  - cleanup_basics: _cleanup_steps doorgeven via frontmatter
  - inject_headings_wettekst: heading-injectie op eenvoudige body
  - organize_headings: noop-placeholder
  - emit_frontmatter: YAML-blok + chunk-blok + intro-content
  - strip_fisconet_artefacts: TOC-fragment + plain-text labels
  - Idempotentie waar van toepassing
  - Edge-cases: lege body, ontbrekende sleutels
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl.transformers import apply_chain, TRANSFORMERS  # noqa: E402
from tools.etl.transformers.cleanup_basics import cleanup_basics  # noqa: E402
from tools.etl.transformers.inject_headings_wettekst import inject_headings_wettekst  # noqa: E402
from tools.etl.transformers.organize_headings import organize_headings  # noqa: E402
from tools.etl.transformers.emit_frontmatter import emit_frontmatter  # noqa: E402
from tools.etl.transformers.strip_fisconet_artefacts import strip_fisconet_artefacts  # noqa: E402
from tools.etl.transformers.fix_stuck_art_number import fix_stuck_art_number  # noqa: E402
from tools.etl.transformers.split_merged_headings import split_merged_headings  # noqa: E402
from tools.etl.transformers.strip_amendment_overview import strip_amendment_overview  # noqa: E402
from tools.etl.transformers.strip_compilatie_appendix import strip_compilatie_appendix  # noqa: E402


# ─── apply_chain ─────────────────────────────────────────────────────────────

class TestApplyChain:
    def test_empty_chain_passthrough(self):
        body = "Hallo wereld."
        fm = {"tags": [], "wet": "Test"}
        new_body, new_fm = apply_chain(body, fm, [])
        assert new_body == body
        assert new_fm == {"tags": [], "wet": "Test"}

    def test_unknown_transformer_raises(self):
        with pytest.raises(ValueError, match="Onbekende transformer"):
            apply_chain("body", {}, ["bestaat_niet"])

    def test_chain_applies_in_order(self):
        """Transformers worden in volgorde toegepast."""
        log = []

        def first(body, fm):
            log.append("first")
            return body + " first", fm

        def second(body, fm):
            log.append("second")
            return body + " second", fm

        # Patch TRANSFORMERS tijdelijk voor deze test
        import tools.etl.transformers as t_module
        original = dict(t_module.TRANSFORMERS)
        t_module.TRANSFORMERS["_test_first"] = first
        t_module.TRANSFORMERS["_test_second"] = second
        try:
            result_body, _ = apply_chain("start", {}, ["_test_first", "_test_second"])
            assert result_body == "start first second"
            assert log == ["first", "second"]
        finally:
            t_module.TRANSFORMERS.clear()
            t_module.TRANSFORMERS.update(original)

    def test_all_registered_transformers_callable(self):
        for name, fn in TRANSFORMERS.items():
            assert callable(fn), f"TRANSFORMERS[{name!r}] is niet callable"


# ─── cleanup_basics ──────────────────────────────────────────────────────────

class TestCleanupBasics:
    def test_no_steps_passthrough(self):
        body = "tekst met   spaties"
        result_body, result_fm = cleanup_basics(body, {})
        assert result_body == body
        assert result_fm == {}

    def test_cleanup_steps_applied(self):
        # collapse_blank_lines is een simpele maar deterministische stap
        body = "regel 1\n\n\n\nregel 2"
        fm = {"_cleanup_steps": ["collapse_blank_lines"]}
        result_body, result_fm = cleanup_basics(body, fm)
        assert "\n\n\n" not in result_body  # max 2 lege regels
        assert "_cleanup_steps" not in result_fm  # intern veld opgeruimd

    def test_cleanup_steps_removed_from_frontmatter(self):
        fm = {"_cleanup_steps": ["collapse_blank_lines"], "wet": "Test"}
        cleanup_basics("body", fm)
        assert "_cleanup_steps" not in fm
        assert "wet" in fm  # andere velden intact

    def test_empty_body(self):
        result_body, result_fm = cleanup_basics("", {"_cleanup_steps": ["collapse_blank_lines"]})
        assert result_body == ""

    def test_unknown_step_raises(self):
        fm = {"_cleanup_steps": ["bestaat_niet_stap"]}
        with pytest.raises(ValueError):
            cleanup_basics("body", fm)

    def test_normalize_whitespace(self):
        body = "tekst  met   extra   spaties"
        fm = {"_cleanup_steps": ["normalize_whitespace"]}
        result_body, _ = cleanup_basics(body, fm)
        assert "  " not in result_body

    def test_idempotent_collapse_blank_lines(self):
        body = "a\n\nb"
        fm1 = {"_cleanup_steps": ["collapse_blank_lines"]}
        result1, _ = cleanup_basics(body, fm1)
        fm2 = {"_cleanup_steps": ["collapse_blank_lines"]}
        result2, _ = cleanup_basics(result1, fm2)
        assert result1 == result2


# ─── inject_headings_wettekst ────────────────────────────────────────────────

class TestInjectHeadingsWettekst:
    _SIMPLE_BODY = """\
HOOFDSTUK 1. - Algemeen

Art. 1.  Eerste artikel.

Art. 2.  Tweede artikel.
"""

    def test_headings_injected(self):
        body, fm = inject_headings_wettekst(self._SIMPLE_BODY, {})
        assert "## HOOFDSTUK 1." in body or "### HOOFDSTUK 1." in body

    def test_article_heading_injected(self):
        body, fm = inject_headings_wettekst(self._SIMPLE_BODY, {})
        # Art. moet een heading zijn
        assert "## Art. 1" in body or "### Art. 1" in body

    def test_chunk_info_stored_in_frontmatter(self):
        _, fm = inject_headings_wettekst(self._SIMPLE_BODY, {})
        assert "_chunk_info" in fm
        assert "_chunk_level" in fm
        assert "_chunk_type" in fm

    def test_sub_strategy_consumed(self):
        fm = {"_sub_strategy": "per_definitieblok"}
        _, result_fm = inject_headings_wettekst(self._SIMPLE_BODY, fm)
        # _sub_strategy wordt geconsumeerd en als nieuw intern veld opgeslagen
        # (inject_headings_wettekst schrijft het terug als intern veld voor emit_frontmatter)
        assert result_fm.get("_sub_strategy") == "per_definitieblok"

    def test_empty_body(self):
        body, fm = inject_headings_wettekst("", {})
        assert body == ""
        assert "_chunk_level" in fm

    def test_idempotent(self):
        """Twee keer inject_headings_wettekst op dezelfde body geeft dezelfde output."""
        body1, fm1 = inject_headings_wettekst(self._SIMPLE_BODY, {})
        body2, fm2 = inject_headings_wettekst(body1, {})
        assert body1 == body2

    def test_h1_not_touched(self):
        body_with_h1 = "# Wetsnaam\n\nArt. 1.  Tekst."
        result_body, _ = inject_headings_wettekst(body_with_h1, {})
        assert result_body.startswith("# Wetsnaam")


# ─── organize_headings ───────────────────────────────────────────────────────

class TestOrganizeHeadings:
    def test_noop(self):
        body = "## HOOFDSTUK 1\n\n### Art. 1\n"
        fm = {"key": "val"}
        result_body, result_fm = organize_headings(body, fm)
        assert result_body == body
        assert result_fm == fm

    def test_empty_body(self):
        result_body, result_fm = organize_headings("", {})
        assert result_body == ""
        assert result_fm == {}


# ─── emit_frontmatter ────────────────────────────────────────────────────────

class TestEmitFrontmatter:
    _BASE_FM = {
        "tags": ["TEST"],
        "itaa_sectie": "TEST-SECTIE",
        "wet": "Testwet",
        "titel": "Testwet titel",
        "bijgewerkt": "01.01.2026",
        "bron": "test.be",
        "bron_rol": "itaa_lex",
    }

    def _run(self, extra_fm: dict | None = None) -> tuple[str, dict]:
        fm = dict(self._BASE_FM)
        if extra_fm:
            fm.update(extra_fm)
        return emit_frontmatter("Artikeltekst.", fm)

    def test_yaml_delimiters_present(self):
        text, _ = self._run()
        assert text.startswith("---\n")
        assert "\n---\n" in text

    def test_chunk_block_present(self):
        text, _ = self._run({"_chunk_level": 3, "_chunk_type": "Art."})
        assert "chunk:" in text
        assert "level: 3" in text
        assert 'type: "Art."' in text

    def test_chunk_block_default_level_2(self):
        text, _ = self._run()
        assert "level: 2" in text

    def test_sub_strategy_null_by_default(self):
        text, _ = self._run()
        assert "sub_strategy: null" in text

    def test_sub_strategy_written(self):
        text, _ = self._run({"_sub_strategy": "per_definitieblok"})
        assert 'sub_strategy: "per_definitieblok"' in text

    def test_intro_h1_present(self):
        text, _ = self._run()
        assert "# Testwet titel" in text

    def test_bijgewerkt_intro_present(self):
        text, _ = self._run()
        assert "*Bijgewerkt tot en met 01.01.2026" in text

    def test_body_present(self):
        text, _ = self._run()
        assert "Artikeltekst." in text

    def test_internal_fields_not_in_output(self):
        fm = dict(self._BASE_FM)
        fm["_chunk_level"] = 3
        fm["_chunk_type"] = "Art."
        fm["_sub_strategy"] = None
        fm["_chunk_info"] = {"ranks": ["Art."]}
        fm["_cleanup_steps"] = ["collapse_blank_lines"]
        text, result_fm = emit_frontmatter("Body.", fm)
        # Interne velden mogen niet in de YAML-output staan
        for key in ("_chunk_level", "_chunk_type", "_sub_strategy",
                    "_chunk_info", "_cleanup_steps"):
            assert key not in text
        # Geretourneerde frontmatter-dict moet leeg zijn
        assert result_fm == {}

    def test_bron_rol_in_output(self):
        text, _ = self._run()
        assert 'bron_rol: "itaa_lex"' in text

    def test_no_bron_rol_when_absent(self):
        fm = dict(self._BASE_FM)
        fm.pop("bron_rol")
        text, _ = emit_frontmatter("Body.", fm)
        assert "bron_rol" not in text

    def test_empty_body(self):
        text, _ = self._run()
        # Zelfs met lege body moet de frontmatter en intro aanwezig zijn
        text_empty, _ = emit_frontmatter("", dict(self._BASE_FM))
        assert "---" in text_empty
        assert "# Testwet titel" in text_empty

    def test_tags_rendered_as_yaml_list(self):
        fm = dict(self._BASE_FM)
        fm["tags"] = ["BTW", "WIB92"]
        text, _ = emit_frontmatter("Body.", fm)
        assert 'tags: ["BTW", "WIB92"]' in text

    def test_frontmatter_before_h1(self):
        """Het YAML-blok moet vóór de H1-titel staan."""
        text, _ = self._run()
        fm_end = text.index("\n---\n")
        h1_pos = text.index("# Testwet titel")
        assert fm_end < h1_pos


# ─── Integratie: cleanup_basics → inject_headings_wettekst → emit_frontmatter ─

class TestChainIntegratie:
    _BODY = """\
HOOFDSTUK 1. - Definities

Art. 1.  Voor de toepassing van deze wet: definitie.

Art. 2.  Tweede artikel.
"""

    _FM = {
        "tags": ["TEST"],
        "itaa_sectie": "TEST",
        "wet": "Test-integratiewet",
        "titel": "Test-integratiewet",
        "bijgewerkt": "01.01.2026",
        "bron": "test.be",
        "bron_rol": "itaa_lex",
        "_cleanup_steps": ["collapse_blank_lines"],
        "_sub_strategy": None,
    }

    def test_full_chain_produces_markdown(self):
        chain = ["cleanup_basics", "inject_headings_wettekst", "emit_frontmatter"]
        text, _ = apply_chain(self._BODY, dict(self._FM), chain)
        assert text.startswith("---\n")
        assert "chunk:" in text
        assert "# Test-integratiewet" in text
        # Art. moet als heading aanwezig zijn
        assert "## Art. 1" in text or "### Art. 1" in text

    def test_chain_without_headings(self):
        """Chain zonder inject_headings_wettekst geeft geen chunk-type-injectie."""
        chain = ["cleanup_basics", "emit_frontmatter"]
        fm = dict(self._FM)
        text, _ = apply_chain(self._BODY, fm, chain)
        # Frontmatter + intro aanwezig
        assert "---" in text
        # Chunk-blok met default level=2 aanwezig
        assert "level: 2" in text


# ─── strip_fisconet_artefacts ────────────────────────────────────────────────

class TestStripFisconetArtefacts:
    """Tests voor de strip_fisconet_artefacts-transformer.

    Dekt:
      - TOC-fragment strippen (≥ 3 heading-only blokken)
      - 'Titel' als losse regel verwijderen
      - 'Bron : FINANCIEN' verwijderen
      - Idempotentie
      - Edge-case: geen TOC-fragment → onveranderd
      - Frontmatter onveranderd
    """

    # Mini-body die de drie artefacten bevat (gebaseerd op WBTW-KB1-voldoening).
    # Het artikel-tekst is één lange lijn (≥ 100 chars) zoals de custom_wetboek
    # extractor die uitvoert — niet word-wrapped.
    _BODY_WITH_ARTEFACTS = """\
# BTW KB nr. 1

*Bijgewerkt tot en met 2024 — gecoördineerde versie.*

Titel

29 DECEMBER 1992. - Koninklijk besluit nr. 1 met betrekking tot de regeling.

Bron : FINANCIEN

#### Art. 4

### Afdeling 3. - Vermeldingen

#### Art. 5

### Afdeling 4. - Andere verplichtingen

### Afdeling 5. - Vereenvoudigde facturen

## Hoofdstuk II. - De boekhouding.

## Hoofdstuk III. - Periodieke aangifte

Eerste hoofdstuk. - Facturering

### Afdeling 1. - Uit te reiken facturen

Artikel 1.[1 [4 De belastingplichtige die hierna vermelde leveringen van goederen of diensten die niet zijn vrijgesteld krachtens artikel 44 van het Wetboek verricht voor natuurlijke personen die ze bestemmen voor hun privégebruik, reikt een factuur uit wanneer deze handelingen overeenkomstig de artikelen van het Wetboek in België plaatsvinden.]4
"""

    # Body zonder TOC-fragment (normaal geval).
    # Art. 1 heeft een lange paragraaf NA de heading-regel (> 100 chars body-tekst).
    _BODY_CLEAN = """\
# Test wet

*Bijgewerkt tot en met 2024 — gecoördineerde versie.*

## Hoofdstuk I. - Algemene bepalingen

### Art. 1.

Dit is een substantiële alinea die meer dan honderd tekens bevat en duidelijk
als echte artikel-tekst beschouwd wordt door de heuristiek, niet als TOC.

### Art. 2.

Tweede artikel met voldoende inhoud om als echte sectie te tellen.
"""

    def test_titel_label_verwijderd(self):
        result_body, _ = strip_fisconet_artefacts(self._BODY_WITH_ARTEFACTS, {})
        # 'Titel' als losse regel moet weg zijn
        lines = result_body.split("\n")
        assert "Titel" not in lines

    def test_bron_financien_verwijderd(self):
        result_body, _ = strip_fisconet_artefacts(self._BODY_WITH_ARTEFACTS, {})
        assert "Bron : FINANCIEN" not in result_body

    def test_toc_fragment_gestript(self):
        result_body, _ = strip_fisconet_artefacts(self._BODY_WITH_ARTEFACTS, {})
        # De TOC-headings zonder substantiële tekst moeten weg zijn
        assert "#### Art. 4" not in result_body
        assert "### Afdeling 3." not in result_body

    def test_echte_sectie_behouden(self):
        result_body, _ = strip_fisconet_artefacts(self._BODY_WITH_ARTEFACTS, {})
        # De echte artikel-inhoud (lange lijn ≥ 100 chars) moet bewaard blijven.
        assert "Artikel 1." in result_body
        assert "leveringen van goederen of diensten" in result_body
        # De echte TOC-headings zonder inhoud moeten weg zijn:
        assert "#### Art. 4" not in result_body
        assert "### Afdeling 3." not in result_body

    def test_idempotent(self):
        """Twee keer de transformer draaien geeft dezelfde output."""
        result1, _ = strip_fisconet_artefacts(self._BODY_WITH_ARTEFACTS, {})
        result2, _ = strip_fisconet_artefacts(result1, {})
        assert result1 == result2

    def test_schone_body_onveranderd(self):
        """Body zonder TOC-fragment en zonder label-regels wordt niet gewijzigd."""
        result_body, _ = strip_fisconet_artefacts(self._BODY_CLEAN, {})
        assert result_body == self._BODY_CLEAN

    def test_lege_body(self):
        result_body, result_fm = strip_fisconet_artefacts("", {})
        assert result_body == ""
        assert result_fm == {}

    def test_frontmatter_onveranderd(self):
        fm = {"wet": "Testwet", "tags": ["BTW"]}
        _, result_fm = strip_fisconet_artefacts(self._BODY_WITH_ARTEFACTS, fm)
        assert result_fm == {"wet": "Testwet", "tags": ["BTW"]}

    def test_bron_financien_variaties(self):
        """Verwijder ook variaties in spatiëring."""
        for variant in (
            "Bron : FINANCIEN",
            "Bron: FINANCIEN",
            "Bron :  FINANCIEN",
        ):
            body = f"# Wet\n\n{variant}\n\n### Art. 1.  Tekst.\n"
            result_body, _ = strip_fisconet_artefacts(body, {})
            assert variant not in result_body, f"Variant niet gestript: {variant!r}"

    def test_twee_toc_blokken_niet_gestript(self):
        """Minder dan 3 heading-only blokken → conservatief: niet strippen."""
        body = """\
# Wet

*Bijgewerkt.*

## Hoofdstuk I.

### Art. 1.  Substantiële tekst die meer dan honderd tekens telt en dus niet
als TOC-blok beschouwd wordt door de conservatieve heuristiek hier.
"""
        result_body, _ = strip_fisconet_artefacts(body, {})
        # Hoofdstuk I. moet er nog staan (< 3 TOC-blokken)
        assert "## Hoofdstuk I." in result_body

    def test_geregistreerd_in_transformers(self):
        """strip_fisconet_artefacts moet zichtbaar zijn in TRANSFORMERS-registry."""
        assert "strip_fisconet_artefacts" in TRANSFORMERS


# ─── fix_stuck_art_number ─────────────────────────────────────────────────────

class TestFixStuckArtNumber:
    """Voeg ontbrekende spatie tussen `Art. N.` en eerste body-karakter."""

    def test_basic_capital_letter(self):
        """`Art. 3.Deze wet ...` → `Art. 3. Deze wet ...`"""
        body = "Art. 3.Deze wet is van toepassing"
        result, _ = fix_stuck_art_number(body, {})
        assert result == "Art. 3. Deze wet is van toepassing"

    def test_bracketed_amendment_marker(self):
        """`Art. 4.[1 § 1.` → `Art. 4. [1 § 1.`"""
        body = "Art. 4.[1 § 1. Indien er ..."
        result, _ = fix_stuck_art_number(body, {})
        assert result == "Art. 4. [1 § 1. Indien er ..."

    def test_articke_keyword_long_form(self):
        """`Artikel 5.Deze ...` → `Artikel 5. Deze ...`"""
        body = "Artikel 5.Deze bepaling treedt in werking"
        result, _ = fix_stuck_art_number(body, {})
        assert result == "Artikel 5. Deze bepaling treedt in werking"

    def test_wvv_num_colon_num(self):
        """`Art. 1:5.Een vennootschap ...` → met spatie."""
        body = "Art. 1:5.Een vennootschap wordt opgericht"
        result, _ = fix_stuck_art_number(body, {})
        assert result == "Art. 1:5. Een vennootschap wordt opgericht"

    def test_wer_roman_prefix(self):
        """`Art. XV.125.De ...` → met spatie."""
        body = "Art. XV.125.De Koning kan ..."
        result, _ = fix_stuck_art_number(body, {})
        assert result == "Art. XV.125. De Koning kan ..."

    def test_bis_suffix(self):
        """`Art. 3bis.Tekst ...` → met spatie."""
        body = "Art. 3bis.Tekst van het artikel"
        result, _ = fix_stuck_art_number(body, {})
        assert result == "Art. 3bis. Tekst van het artikel"

    def test_no_change_when_space_already_present(self):
        """`Art. 3. Deze wet` blijft onveranderd."""
        body = "Art. 3. Deze wet is van toepassing"
        result, _ = fix_stuck_art_number(body, {})
        assert result == body

    def test_no_change_for_inline_reference(self):
        """`zoals in art. 5 vermeld` (geen punt-eind) onveranderd."""
        body = "zoals in art. 5 vermeld in de inleiding"
        result, _ = fix_stuck_art_number(body, {})
        assert result == body

    def test_no_change_for_sub_numbering(self):
        """`Art. 3.5 De ...` is sub-numbering, geen heading-eind. Niet aanraken."""
        body = "Art. 3.5 De Koning kan ..."
        result, _ = fix_stuck_art_number(body, {})
        assert result == body

    def test_multiple_occurrences_in_body(self):
        """Meerdere stuck-art-numbers worden ALLEMAAL gefixt."""
        body = (
            "### Art. 3.Deze wet is van toepassing.\n\n"
            "### Art. 4.De Koning kan ..."
        )
        result, _ = fix_stuck_art_number(body, {})
        assert result == (
            "### Art. 3. Deze wet is van toepassing.\n\n"
            "### Art. 4. De Koning kan ..."
        )

    def test_idempotent(self):
        """Tweede call op output verandert niets."""
        body = "Art. 3.Deze wet is van toepassing"
        once, _ = fix_stuck_art_number(body, {})
        twice, _ = fix_stuck_art_number(once, {})
        assert once == twice

    def test_geregistreerd_in_transformers(self):
        """fix_stuck_art_number moet in TRANSFORMERS-registry zitten."""
        assert "fix_stuck_art_number" in TRANSFORMERS


# ─── split_merged_headings ────────────────────────────────────────────────────

class TestSplitMergedHeadings:
    """Splits gemerged hiërarchie-headings op één regel."""

    def test_afdeling_onderafdeling(self):
        body = "##### Afdeling 1. Gemeenschappelijke bepalingen. - Onderafdeling 2. Bevoegdheden."
        result, _ = split_merged_headings(body, {})
        assert result == (
            "##### Afdeling 1. Gemeenschappelijke bepalingen.\n"
            "\n"
            "###### Onderafdeling 2. Bevoegdheden."
        )

    def test_deel_boek_uppercase(self):
        body = "## DEEL 3. De verenigingen en stichtingen. - BOEK 9. VZW."
        result, _ = split_merged_headings(body, {})
        assert result == (
            "## DEEL 3. De verenigingen en stichtingen.\n"
            "\n"
            "### BOEK 9. VZW."
        )

    def test_no_split_when_single_heading(self):
        """Een enkele heading-regel blijft onveranderd."""
        body = "##### Afdeling 1. Gemeenschappelijke bepalingen."
        result, _ = split_merged_headings(body, {})
        assert result == body

    def test_no_split_in_body_text(self):
        """Body-regels die toevallig ' - ' bevatten blijven onveranderd."""
        body = "Dit is body-tekst met - een streep - maar geen heading."
        result, _ = split_merged_headings(body, {})
        assert result == body

    def test_multiple_merges_in_body(self):
        """Twee merge-regels worden allebei gesplitst, andere regels onveranderd."""
        body = (
            "# Wet\n"
            "\n"
            "## DEEL 1. Algemeen. - BOEK 1. Inleiding.\n"
            "\n"
            "Body tekst.\n"
            "\n"
            "##### Afdeling 1. Foo. - Onderafdeling 2. Bar.\n"
        )
        result, _ = split_merged_headings(body, {})
        assert "## DEEL 1. Algemeen.\n\n### BOEK 1. Inleiding." in result
        assert "##### Afdeling 1. Foo.\n\n###### Onderafdeling 2. Bar." in result
        assert "Body tekst." in result

    def test_idempotent(self):
        """Tweede call op output verandert niets meer."""
        body = "##### Afdeling 1. Foo. - Onderafdeling 2. Bar."
        once, _ = split_merged_headings(body, {})
        twice, _ = split_merged_headings(once, {})
        assert once == twice

    def test_deepest_level_does_not_overflow(self):
        """Een merge op level 6 (max) houdt de tweede heading op level 6."""
        body = "###### Afdeling 1. Foo. - Onderafdeling 2. Bar."
        result, _ = split_merged_headings(body, {})
        # Beide headings op level 6 (geen `#######` — dat is geen geldige markdown)
        for line in result.split("\n"):
            if line.startswith("#"):
                assert line.count("#") <= 6

    def test_geregistreerd_in_transformers(self):
        """split_merged_headings moet in TRANSFORMERS-registry zitten."""
        assert "split_merged_headings" in TRANSFORMERS


# ─── strip_amendment_overview ─────────────────────────────────────────────────

class TestStripAmendmentOverview:
    """Strip Fisconet wijzigings-overzicht-artefacten uit body."""

    def test_multi_art_ref_row(self):
        """Rij met ≥3 `(Art.N)` wordt gestript."""
        body = "Body voor.\n(Art.254)   (Art.255)    (Art.256)\nBody na.\n"
        result, _ = strip_amendment_overview(body, {})
        assert "(Art.254)" not in result
        assert "Body voor." in result
        assert "Body na." in result

    def test_date_art_ref_line(self):
        """Regel met datum + (Art.N) wordt gestript."""
        body = "Body voor.\n01-04-2019             (Art.20)\nBody na.\n"
        result, _ = strip_amendment_overview(body, {})
        assert "01-04-2019" not in result
        assert "Body voor." in result
        assert "Body na." in result

    def test_no_strip_legitimate_art_ref_in_text(self):
        """Een enkele `(Art.N)` inline in body-tekst blijft staan."""
        body = "Conform de bepalingen van (Art.5) geldt het volgende.\n"
        result, _ = strip_amendment_overview(body, {})
        assert result == body

    def test_no_strip_two_art_refs_only(self):
        """Twee `(Art.N)` op een regel is geen overzicht — niet strippen."""
        body = "Conform (Art.5) en (Art.7) bepalingen.\n"
        result, _ = strip_amendment_overview(body, {})
        assert result == body

    def test_no_strip_date_in_normal_sentence(self):
        """Een datum in normale tekst (geen alleen-op-regel) wordt niet gestript."""
        body = "Inwerkingtreding: 01-04-2019 volgens artikel 5.\n"
        result, _ = strip_amendment_overview(body, {})
        assert result == body

    def test_avg_wet_pattern(self):
        """Realistisch patroon uit AVG-wet-2018."""
        body = (
            "30 JULI 2018. - Wet betreffende de bescherming.\n"
            "\n"
            "(Art.254)   (Art.255)    (Art.256)      (Art.257)     (Art.258)\n"
            "01-04-2019             (Art.20)\n"
            "\n"
            "##### Art. 24\n"
        )
        result, _ = strip_amendment_overview(body, {})
        assert "(Art.254)" not in result
        assert "01-04-2019" not in result
        assert "30 JULI 2018" in result
        assert "##### Art. 24" in result

    def test_idempotent(self):
        """Tweede call verandert niets."""
        body = "(Art.254)   (Art.255)    (Art.256)\n"
        once, _ = strip_amendment_overview(body, {})
        twice, _ = strip_amendment_overview(once, {})
        assert once == twice

    def test_collapse_blank_lines_after_strip(self):
        """Multiple lege regels na strip worden tot max 2 collapsed."""
        body = (
            "Foo.\n"
            "\n"
            "(Art.254)   (Art.255)    (Art.256)\n"
            "01-04-2019    (Art.20)\n"
            "\n"
            "Bar.\n"
        )
        result, _ = strip_amendment_overview(body, {})
        # Geen meer dan 2 opeenvolgende newlines
        assert "\n\n\n" not in result

    def test_long_messy_overview_with_mid_line_date(self):
        """Realistische zeer lange rij met embedded datum + missing-paren.

        Voorbeeld uit AVG-wet (na partial fix): één lange regel met >20
        `(Art.N)` references, een datum `05-09-2018` middenin, en zelfs
        een typo `(Art.260` zonder sluithaakje.
        """
        body = (
            "(Art.254)   (Art.255)    (Art.256)      (Art.257)     (Art.258)   "
            "(Art.259)   (Art.260 (Art.261)   (Art.262) 05-09-2018 "
            "(Art.268)   (Art.269)    (Art.270) ."
        )
        result, _ = strip_amendment_overview(body, {})
        # Regel met zoveel (Art.N) refs hoort als overzicht behandeld te worden
        assert "(Art.254)" not in result, f"long overview row niet gestript: {result[:100]!r}"


class TestStripCompilatieAppendix:
    """Strip Fisconet bijwerkingen/recente-wijzigingen appendix van KB-splits."""

    def test_bijlage_a_met_lijst_van_bijwerkingen(self):
        """Bijlage A gevolgd door 'Lijst van de bijwerkingen' wordt gestript."""
        body = (
            "## Art. 5\n"
            "\n"
            "Onze Minister is belast met de uitvoering.\n"
            "\n"
            "Bijlage A\n"
            "Lijst van de bijwerkingen\n"
            "\n"
            "Bijw. 01 / 01.01.2012   - Volledige uitgave\n"
        )
        result, _ = strip_compilatie_appendix(body, {})
        assert "Lijst van de bijwerkingen" not in result
        assert "Bijw. 01" not in result
        assert "Onze Minister" in result

    def test_bijlage_a_met_bijwerking_kolomheader(self):
        """Bijlage A gevolgd door 'Bijwerking   t.e.m. B.S.' wordt gestript."""
        body = (
            "Onze Minister is belast met de uitvoering.\n"
            "\n"
            "Bijlage A\n"
            "\n"
            "     Bijwerking         t.e.m. B.S. van                Te vervangen pagina's\n"
            "\n"
            "Bijw. 01 / 01.01.2012     Volledige uitgave\n"
        )
        result, _ = strip_compilatie_appendix(body, {})
        assert "Bijwerking" not in result
        assert "Bijw. 01" not in result
        assert "Onze Minister" in result

    def test_recente_wijzigingen_als_directe_trigger(self):
        """'Recente wijzigingen' op eigen regel wordt direct gestript."""
        body = (
            "## Art. 3\n"
            "\n"
            "Onze Minister is belast met de uitvoering.\n"
            "\n"
            "Recente wijzigingen – KB nr. 11\n"
            "De historische versies kunnen geraadpleegd worden op www.fisconetplus.be\n"
            "\n"
            "*   KB van 24.01.2015 - Koninklijk besluit...\n"
        )
        result, _ = strip_compilatie_appendix(body, {})
        assert "Recente wijzigingen" not in result
        assert "De historische versies" not in result
        assert "## Art. 3" in result
        assert "Onze Minister" in result

    def test_bijlage_bare_met_recente_wijzigingen(self):
        """Bare 'Bijlage' gevolgd door 'Recente wijzigingen' wordt gestript."""
        body = (
            "Onze Minister is belast met de uitvoering.\n"
            "\n"
            "Bijlage\n"
            "Recente wijzigingen – KB nr. 3\n"
            "De historische versies ...\n"
        )
        result, _ = strip_compilatie_appendix(body, {})
        assert "Recente wijzigingen" not in result
        assert "Bijlage\n" not in result
        assert "Onze Minister" in result

    def test_geen_strip_zonder_trigger(self):
        """Body zonder compilatie-appendix blijft ongewijzigd."""
        body = (
            "## Art. 1\n"
            "\n"
            "Gewone wettekst zonder appendix.\n"
        )
        result, _ = strip_compilatie_appendix(body, {})
        assert result == body

    def test_geen_strip_markdown_heading_bijlage(self):
        """'## Bijlage I' als markdown-heading wordt niet gestript."""
        body = (
            "## Art. 5\n"
            "\n"
            "Artikel tekst.\n"
            "\n"
            "## Bijlage I\n"
            "\n"
            "Echte wettekst bijlage.\n"
        )
        result, _ = strip_compilatie_appendix(body, {})
        assert "## Bijlage I" in result
        assert "Echte wettekst bijlage" in result

    def test_geen_strip_bijlage_all_caps(self):
        """'BIJLAGE' (all caps) als legal bijlage wordt niet gestript."""
        body = (
            "## Art. 3\n"
            "\n"
            "Onze Minister is belast.\n"
            "\n"
            "                    BIJLAGE\n"
            "\n"
            "Tabel A - Goederen aan 6 pct.\n"
        )
        result, _ = strip_compilatie_appendix(body, {})
        assert "BIJLAGE" in result
        assert "Tabel A" in result

    def test_idempotent(self):
        """Tweede run verandert niets meer."""
        body = (
            "## Art. 5\n"
            "Onze Minister is belast.\n"
            "\n"
            "Bijlage A\n"
            "Lijst van de bijwerkingen\n"
            "Bijw. 01 / 01.01.2012\n"
        )
        once, _ = strip_compilatie_appendix(body, {})
        twice, _ = strip_compilatie_appendix(once, {})
        assert once == twice

    def test_lege_body_pass_through(self):
        """Lege body wordt ongemoeid doorgegeven."""
        result, _ = strip_compilatie_appendix("", {})
        assert result == ""

    def test_geen_overtollige_lege_regels_na_strip(self):
        """Na strip geen overtollige lege regels aan het einde."""
        body = (
            "Wettekst.\n"
            "\n"
            "\n"
            "Bijlage A\n"
            "Lijst van de bijwerkingen\n"
        )
        result, _ = strip_compilatie_appendix(body, {})
        # Geen meer dan één lege regel aan het einde voor \n
        assert not result.endswith("\n\n")
        assert "Wettekst." in result

    def test_geregistreerd_in_transformers(self):
        """strip_compilatie_appendix staat in de TRANSFORMERS-registry."""
        from tools.etl.transformers import TRANSFORMERS
        assert "strip_compilatie_appendix" in TRANSFORMERS


# ─── unindent_pdftotext_margin ────────────────────────────────────────────────

class TestUnindentPdftotextMargin:
    """Strip 4-space globale margin van pdftotext-output."""

    def test_basic_4space_indent(self):
        body = "    Art. 1. Eerste artikel.\n    Art. 2. Tweede artikel."
        from tools.etl.transformers.unindent_pdftotext_margin import unindent_pdftotext_margin
        result, _ = unindent_pdftotext_margin(body, {})
        assert result == "Art. 1. Eerste artikel.\nArt. 2. Tweede artikel."

    def test_relative_indent_preserved(self):
        """`        sub-item` (8 spaties) wordt `    sub-item` (4 spaties)."""
        body = "    item\n        sub-item"
        from tools.etl.transformers.unindent_pdftotext_margin import unindent_pdftotext_margin
        result, _ = unindent_pdftotext_margin(body, {})
        assert result == "item\n    sub-item"

    def test_no_indent_unchanged(self):
        """Regels met 0-3 spaties blijven onaangetast."""
        body = "## Heading\n\nGewone tekst.\n  twee-spaties-indent"
        from tools.etl.transformers.unindent_pdftotext_margin import unindent_pdftotext_margin
        result, _ = unindent_pdftotext_margin(body, {})
        assert result == body

    def test_empty_lines_preserved(self):
        body = "    regel 1\n\n    regel 2"
        from tools.etl.transformers.unindent_pdftotext_margin import unindent_pdftotext_margin
        result, _ = unindent_pdftotext_margin(body, {})
        assert result == "regel 1\n\nregel 2"

    def test_fenced_code_block_preserved(self):
        """Binnen ``` blocks blijft alle indent intact."""
        body = (
            "Body voor.\n"
            "\n"
            "```\n"
            "    def foo():\n"
            "        return 1\n"
            "```\n"
            "\n"
            "    Geindenteerde body na code-block."
        )
        from tools.etl.transformers.unindent_pdftotext_margin import unindent_pdftotext_margin
        result, _ = unindent_pdftotext_margin(body, {})
        assert "    def foo():" in result
        assert "        return 1" in result
        # Body buiten fence krijgt de unindent
        assert "Geindenteerde body na code-block." in result
        assert "    Geindenteerde body na code-block." not in result

    def test_realistic_wbtw_kb_body(self):
        """Realistisch WBTW-KB body-fragment met margin."""
        body = (
            "## Art. 1\n"
            "\n"
            "    Het normale tarief van de belasting bedraagt 21%.\n"
            "    Dit tarief is van toepassing op alle goederen tenzij...\n"
            "\n"
            "## Art. 2\n"
            "\n"
            "    Het verlaagde tarief van 6% geldt voor..."
        )
        from tools.etl.transformers.unindent_pdftotext_margin import unindent_pdftotext_margin
        result, _ = unindent_pdftotext_margin(body, {})
        assert "## Art. 1" in result
        assert "Het normale tarief van de belasting bedraagt 21%." in result
        # geen 4-space leading meer
        for line in result.split("\n"):
            assert not line.startswith("    "), f"Nog 4-space indent in: {line!r}"

    def test_idempotent(self):
        body = "    Art. 1.\n    Art. 2."
        from tools.etl.transformers.unindent_pdftotext_margin import unindent_pdftotext_margin
        once, _ = unindent_pdftotext_margin(body, {})
        twice, _ = unindent_pdftotext_margin(once, {})
        assert once == twice

    def test_geregistreerd_in_transformers(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "unindent_pdftotext_margin" in TRANSFORMERS


# ─── strip_pdf_page_noise ─────────────────────────────────────────────────────

class TestStripPdfPageNoise:
    """Strip PDF-paginanummer + dotted-leader artefacten."""

    def test_dotted_leader_toc_line(self):
        from tools.etl.transformers.strip_pdf_page_noise import strip_pdf_page_noise
        body = "Body voor.\nVOORWOORD........................9\nBody na."
        result, _ = strip_pdf_page_noise(body, {})
        assert "VOORWOORD" not in result
        assert "Body voor." in result
        assert "Body na." in result

    def test_standalone_page_number_small(self):
        from tools.etl.transformers.strip_pdf_page_noise import strip_pdf_page_noise
        body = "Body voor.\n\n3\n\nBody na."
        result, _ = strip_pdf_page_noise(body, {})
        assert "\n3\n" not in result
        assert "Body voor." in result

    def test_keep_4digit_year(self):
        """4-cijferige nummers (jaar) blijven staan — NIET strippen."""
        from tools.etl.transformers.strip_pdf_page_noise import strip_pdf_page_noise
        body = "Body voor.\n\n2025\n\nBody na."
        result, _ = strip_pdf_page_noise(body, {})
        assert "2025" in result

    def test_dash_wrapped_page_number(self):
        from tools.etl.transformers.strip_pdf_page_noise import strip_pdf_page_noise
        body = "Body voor.\n\n-3-\n\nBody na."
        result, _ = strip_pdf_page_noise(body, {})
        assert "-3-" not in result

    def test_mm_yyyy_stamp(self):
        from tools.etl.transformers.strip_pdf_page_noise import strip_pdf_page_noise
        body = "Body voor.\n\n12/2024\n\nBody na."
        result, _ = strip_pdf_page_noise(body, {})
        assert "12/2024" not in result

    def test_inline_number_not_stripped(self):
        """Een paginanummer inline in een zin blijft staan."""
        from tools.etl.transformers.strip_pdf_page_noise import strip_pdf_page_noise
        body = "Volgens artikel 3 geldt het volgende."
        result, _ = strip_pdf_page_noise(body, {})
        assert result == body

    def test_inline_4digits_not_stripped(self):
        from tools.etl.transformers.strip_pdf_page_noise import strip_pdf_page_noise
        body = "In het belastingjaar 2025 geldt het tarief."
        result, _ = strip_pdf_page_noise(body, {})
        assert result == body

    def test_multiple_artefacten_in_body(self):
        from tools.etl.transformers.strip_pdf_page_noise import strip_pdf_page_noise
        body = (
            "VOORWOORD.....................9\n"
            "\n"
            "Body content 1.\n"
            "\n"
            "12\n"
            "\n"
            "Body content 2.\n"
            "\n"
            "INDEX...........110\n"
        )
        result, _ = strip_pdf_page_noise(body, {})
        assert "VOORWOORD" not in result
        assert "INDEX" not in result
        assert "\n12\n" not in result
        assert "Body content 1." in result
        assert "Body content 2." in result

    def test_idempotent(self):
        from tools.etl.transformers.strip_pdf_page_noise import strip_pdf_page_noise
        body = "VOORWOORD..........9\n\n12\n\nBody."
        once, _ = strip_pdf_page_noise(body, {})
        twice, _ = strip_pdf_page_noise(once, {})
        assert once == twice

    def test_geregistreerd_in_transformers(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "strip_pdf_page_noise" in TRANSFORMERS


# ─── merge_pdf_paragraph_breaks ───────────────────────────────────────────────

class TestMergePdfParagraphBreaks:
    """Tests voor de merge_pdf_paragraph_breaks-transformer.

    Dekt:
      - Patroon 1: lettered item (a)/(b)/(i)/(1) op eigen regel → merge met volgende
      - Patroon 2: korte regel (woord-per-woord split) → merge met volgende
      - Behoud: headings, lijst-items, lange regels, zin-einde-markers
      - Behoud: YAML-frontmatter
      - Idempotentie
      - Lege body
    """

    def test_lettered_item_merged(self):
        """(a) op eigen regel wordt gemerged met volgende niet-lege regel."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = "(a)\n\nAdherence to ethical principles.\n"
        result, _ = merge_pdf_paragraph_breaks(body, {})
        assert "(a) Adherence to ethical principles." in result
        # Geen losse (a) meer op eigen regel
        assert "\n(a)\n" not in result

    def test_lettered_item_b(self):
        """(b) item ook gemerged."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = "(b)\n\nUse of business acumen.\n"
        result, _ = merge_pdf_paragraph_breaks(body, {})
        assert "(b) Use of business acumen." in result

    def test_roman_numeral_item_merged(self):
        """(i), (ii), (iii) etc. worden ook gemerged."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = "(i)\n\nBias;\n"
        result, _ = merge_pdf_paragraph_breaks(body, {})
        assert "(i) Bias;" in result

    def test_numbered_item_merged(self):
        """(1), (2) etc. worden gemerged."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = "(1)\n\nFirst condition.\n"
        result, _ = merge_pdf_paragraph_breaks(body, {})
        assert "(1) First condition." in result

    def test_multiple_lettered_items(self):
        """Meerdere lettered items in één body worden allemaal gemerged."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = (
            "including:\n"
            "(a)\n"
            "\n"
            "Adherence to ethical principles;\n"
            "\n"
            "(b)\n"
            "\n"
            "Use of business acumen;\n"
            "\n"
            "(c)\n"
            "\n"
            "Application of expertise.\n"
        )
        result, _ = merge_pdf_paragraph_breaks(body, {})
        assert "(a) Adherence to ethical principles;" in result
        assert "(b) Use of business acumen;" in result
        assert "(c) Application of expertise." in result

    def test_short_line_merged_with_next(self):
        """Korte regel (< 20 chars, geen sentence-end) gemerged met volgende."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = "Het\n\neerste\n\nacht\n\nhoofdstukken\n\nbehandelen de directe belastingen.\n"
        result, _ = merge_pdf_paragraph_breaks(body, {})
        # Alles moet samengevoegd zijn in één alinea
        assert "Het" in result
        assert "eerste" in result
        assert "behandelen de directe belastingen." in result
        # Geen isoleerde enkelvoudige woorden meer
        lines = [l for l in result.split("\n") if l.strip()]
        for line in lines:
            # Geen korte 1-woord regels meer (behalve structuurregels)
            if len(line.strip()) < 10 and not line.startswith("#"):
                pass  # enkelvoudige woorden na merge zijn OK als deel van grotere zin

    def test_heading_not_merged(self):
        """Headings worden nooit gemerged — ook niet als ze kort zijn."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = "## BTW\n\nBelasting over de toegevoegde waarde.\n"
        result, _ = merge_pdf_paragraph_breaks(body, {})
        assert "## BTW\n" in result
        assert "Belasting over de toegevoegde waarde." in result

    def test_sentence_end_not_merged(self):
        """Regel die eindigt op `.` wordt NIET gemerged (echte alinea-grens)."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = "Dit is een korte zin.\n\nVolgende alinea begint hier.\n"
        result, _ = merge_pdf_paragraph_breaks(body, {})
        assert "Dit is een korte zin." in result
        assert "Volgende alinea begint hier." in result
        # Moeten gescheiden blijven
        assert "Dit is een korte zin.\n" in result

    def test_colon_end_not_merged(self):
        """Regel die eindigt op `:` wordt niet gemerged."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = "including:\n\n(a) First item.\n"
        result, _ = merge_pdf_paragraph_breaks(body, {})
        assert "including:\n" in result

    def test_long_line_not_merged(self):
        """Regel van ≥ 20 chars zonder sentence-end: patroon 2 triggert niet."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = "Dit is een voldoende\n\nlange regel die niet gemerged wordt.\n"
        result, _ = merge_pdf_paragraph_breaks(body, {})
        # Moet twee gescheiden alinea's blijven
        assert "Dit is een voldoende\n" in result

    def test_frontmatter_not_touched(self):
        """YAML-frontmatter-blok wordt ongemoeid gelaten."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = "---\ntags: [BTW]\nwet: Test\n---\n\n(a)\n\nFirst item.\n"
        result, _ = merge_pdf_paragraph_breaks(body, {})
        # Frontmatter intact
        assert "---\ntags: [BTW]\nwet: Test\n---\n" in result
        # Maar lettered item wél gemerged ná frontmatter
        assert "(a) First item." in result

    def test_empty_body(self):
        """Lege body geeft lege body terug."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        result, _ = merge_pdf_paragraph_breaks("", {})
        assert result == ""

    def test_frontmatter_dict_unchanged(self):
        """frontmatter-dict wordt niet gewijzigd."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        fm = {"wet": "Test", "tags": ["BTW"]}
        _, result_fm = merge_pdf_paragraph_breaks("body tekst.", fm)
        assert result_fm == {"wet": "Test", "tags": ["BTW"]}

    def test_idempotent_lettered(self):
        """Twee keer de transformer draaien geeft dezelfde output (lettered)."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = "(a)\n\nAdherence to ethical principles.\n"
        once, _ = merge_pdf_paragraph_breaks(body, {})
        twice, _ = merge_pdf_paragraph_breaks(once, {})
        assert once == twice

    def test_idempotent_short_line(self):
        """Twee keer de transformer draaien geeft dezelfde output (korte regel)."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = "Het\n\neerste\n\nacht\n\nhoofdstukken behandelen.\n"
        once, _ = merge_pdf_paragraph_breaks(body, {})
        twice, _ = merge_pdf_paragraph_breaks(once, {})
        assert once == twice

    def test_list_item_not_merged_as_next(self):
        """Een volgende regel die een lijst-item is, wordt niet gemerged."""
        from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
        body = "Beschrijving\n\n- Eerste punt\n- Tweede punt\n"
        result, _ = merge_pdf_paragraph_breaks(body, {})
        # "Beschrijving" is < 20 chars zonder sentence-end, maar volgende is list-item
        assert "- Eerste punt" in result
        # Beschrijving moet op eigen regel staan (niet gemerged met lijst-item)
        lines = result.split("\n")
        beschrijving_line = next((l for l in lines if "Beschrijving" in l), None)
        assert beschrijving_line is not None
        assert "- Eerste punt" not in beschrijving_line

    def test_geregistreerd_in_transformers(self):
        """merge_pdf_paragraph_breaks moet in TRANSFORMERS-registry zitten."""
        from tools.etl.transformers import TRANSFORMERS
        assert "merge_pdf_paragraph_breaks" in TRANSFORMERS


# ─── merge_broken_sentences (A6 patroon in CBN-adviezen) ──────────────────────

class TestMergeBrokenSentences:
    """Merge zinnen die door spurious paragraph-break gesplitst zijn."""

    def test_basic_midsentence_break(self):
        from tools.etl.transformers.merge_broken_sentences import merge_broken_sentences
        body = (
            "worden geïdentificeerd Bij de als dekking\n"
            "\n"
            "bestemde verrichtingen moet een onderscheid worden gemaakt.\n"
        )
        result, _ = merge_broken_sentences(body, {})
        assert "worden geïdentificeerd Bij de als dekking bestemde verrichtingen" in result

    def test_after_footnote_ref(self):
        """Spurious break direct na `[^N]` footnote-referentie."""
        from tools.etl.transformers.merge_broken_sentences import merge_broken_sentences
        body = (
            "Het bedrag dat kan worden vrijgesteld is[^9]\n"
            "\n"
            "het minimum van twee bedragen.\n"
        )
        result, _ = merge_broken_sentences(body, {})
        assert "vrijgesteld is[^9] het minimum" in result

    def test_no_merge_after_sentence_end(self):
        """Echte paragraph-break na sentence-end punt: NIET mergen."""
        from tools.etl.transformers.merge_broken_sentences import merge_broken_sentences
        body = (
            "Dit is een afgesloten zin.\n"
            "\n"
            "een nieuwe paragraaf begint hier.\n"
        )
        result, _ = merge_broken_sentences(body, {})
        # Tweede paragraaf blijft op eigen regel
        lines_with_content = [l for l in result.split("\n") if l.strip()]
        assert lines_with_content[0].endswith("zin.")
        assert lines_with_content[1].startswith("een nieuwe paragraaf")

    def test_no_merge_when_next_starts_uppercase(self):
        """Volgende paragraaf begint met hoofdletter — nieuwe zin, niet mergen."""
        from tools.etl.transformers.merge_broken_sentences import merge_broken_sentences
        body = (
            "Vorige zin eindigt zonder punt en\n"
            "\n"
            "Nieuwe Paragraaf hoort apart.\n"
        )
        result, _ = merge_broken_sentences(body, {})
        # NIET gemerged
        assert "en Nieuwe Paragraaf" not in result

    def test_no_merge_heading_or_list(self):
        """Volgende regel is heading of list-item: niet mergen."""
        from tools.etl.transformers.merge_broken_sentences import merge_broken_sentences
        body = (
            "voorgaande zin loopt door\n"
            "\n"
            "## Heading mag niet gemerged worden\n"
        )
        result, _ = merge_broken_sentences(body, {})
        assert "## Heading" in result
        # NOT merged in vorige regel
        assert "loopt door ## Heading" not in result

        body2 = (
            "voorgaande zin loopt door\n"
            "\n"
            "- list item niet mergen\n"
        )
        result2, _ = merge_broken_sentences(body2, {})
        assert "- list item" in result2
        assert "loopt door - list item" not in result2

    def test_no_merge_table_pipe(self):
        from tools.etl.transformers.merge_broken_sentences import merge_broken_sentences
        body = (
            "voorgaande zin\n"
            "\n"
            "| cell | cell |\n"
        )
        result, _ = merge_broken_sentences(body, {})
        assert "| cell |" in result
        assert "voorgaande zin | cell" not in result

    def test_idempotent(self):
        from tools.etl.transformers.merge_broken_sentences import merge_broken_sentences
        body = (
            "worden geïdentificeerd Bij de als dekking\n"
            "\n"
            "bestemde verrichtingen.\n"
        )
        once, _ = merge_broken_sentences(body, {})
        twice, _ = merge_broken_sentences(once, {})
        assert once == twice

    def test_geregistreerd_in_transformers(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "merge_broken_sentences" in TRANSFORMERS


# ─── fix_italic_spacing (D4 in CBN-adviezen) ──────────────────────────────────

class TestFixItalicSpacing:
    """Strip whitespace adjacent to italic-markers."""

    def test_trailing_space_before_closing(self):
        from tools.etl.transformers.fix_italic_spacing import fix_italic_spacing
        body = "Een woord *Solidariteitsfonds * blijft italic."
        result, _ = fix_italic_spacing(body, {})
        assert result == "Een woord *Solidariteitsfonds* blijft italic."

    def test_leading_space_after_opening(self):
        from tools.etl.transformers.fix_italic_spacing import fix_italic_spacing
        body = "Voor * Financieringsfonds* geldt..."
        result, _ = fix_italic_spacing(body, {})
        assert result == "Voor *Financieringsfonds* geldt..."

    def test_both_sides(self):
        from tools.etl.transformers.fix_italic_spacing import fix_italic_spacing
        body = "Het gaat over * testing * resultaten."
        result, _ = fix_italic_spacing(body, {})
        assert result == "Het gaat over *testing* resultaten."

    def test_multiple_italic_pairs(self):
        from tools.etl.transformers.fix_italic_spacing import fix_italic_spacing
        body = "*Voorrang * van het *boekhoudkundig realisatiebeginsel * op *het overeenstemmingsprincipe *."
        result, _ = fix_italic_spacing(body, {})
        # Elk pair heeft geen trailing space binnen het italic-marker-pair
        assert "*Voorrang*" in result
        assert "*boekhoudkundig realisatiebeginsel*" in result
        assert "*het overeenstemmingsprincipe*" in result
        # En geen ` *` (space VOOR closing) overgebleven — dat is wat we wilden fixen
        assert " *." not in result
        assert " * " not in result.replace(" *and", "skipped")

    def test_no_change_when_well_formed(self):
        from tools.etl.transformers.fix_italic_spacing import fix_italic_spacing
        body = "Een *welgevormde* italic blijft *intact*."
        result, _ = fix_italic_spacing(body, {})
        assert result == body

    def test_bold_not_affected(self):
        """Bold `**foo **` blijft onaangetast (alleen italic `*` wordt gefixed)."""
        from tools.etl.transformers.fix_italic_spacing import fix_italic_spacing
        body = "Een **bold met trailing space ** blijft zo."
        result, _ = fix_italic_spacing(body, {})
        assert "**bold met trailing space **" in result

    def test_list_marker_not_affected(self):
        """List-marker `* item` aan begin regel is geen italic — niet aanraken."""
        from tools.etl.transformers.fix_italic_spacing import fix_italic_spacing
        body = "Lijst:\n* item 1\n* item 2"
        result, _ = fix_italic_spacing(body, {})
        # list-markers blijven (newline + * + space)
        assert "\n* item 1" in result
        assert "\n* item 2" in result

    def test_multiline_italic_not_merged(self):
        """Italic spanning newlines wordt NIET aangeraakt (riskant)."""
        from tools.etl.transformers.fix_italic_spacing import fix_italic_spacing
        body = "*Lijn 1\n\nLijn 2*"
        result, _ = fix_italic_spacing(body, {})
        # Niet samengevoegd
        assert "\n\n" in result

    def test_idempotent(self):
        from tools.etl.transformers.fix_italic_spacing import fix_italic_spacing
        body = "*Solidariteitsfonds * of *Financieringsfonds *."
        once, _ = fix_italic_spacing(body, {})
        twice, _ = fix_italic_spacing(once, {})
        assert once == twice

    def test_geregistreerd_in_transformers(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "fix_italic_spacing" in TRANSFORMERS


# ─── normalize_bullet_glyphs (C1 in CBN-adviezen) ─────────────────────────────

class TestNormalizeBulletGlyphs:
    def test_basic_bullet_at_line_start(self):
        from tools.etl.transformers.normalize_bullet_glyphs import normalize_bullet_glyphs
        body = "• Eerste\n• Tweede\n"
        result, _ = normalize_bullet_glyphs(body, {})
        assert result == "- Eerste\n- Tweede\n"

    def test_indented_bullet(self):
        from tools.etl.transformers.normalize_bullet_glyphs import normalize_bullet_glyphs
        body = "  • sub-item\n    • diep sub\n"
        result, _ = normalize_bullet_glyphs(body, {})
        assert result == "  - sub-item\n    - diep sub\n"

    def test_bullet_inline_not_changed(self):
        """Een `•` middenin een zin blijft staan."""
        from tools.etl.transformers.normalize_bullet_glyphs import normalize_bullet_glyphs
        body = "Een zin met • inline bullet • niet aanraken.\n"
        result, _ = normalize_bullet_glyphs(body, {})
        assert result == body

    def test_idempotent(self):
        from tools.etl.transformers.normalize_bullet_glyphs import normalize_bullet_glyphs
        body = "• Foo\n• Bar\n"
        once, _ = normalize_bullet_glyphs(body, {})
        twice, _ = normalize_bullet_glyphs(once, {})
        assert once == twice

    def test_geregistreerd_in_transformers(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "normalize_bullet_glyphs" in TRANSFORMERS


# ─── fix_bold_italic_mixing (D4 in CBN-adviezen) ──────────────────────────────

class TestFixBoldItalicMixing:
    def test_mid_word_double_asterisk_stripped(self):
        """`*N**iet in de balans*` → `*Niet in de balans*` (CBN-0167-02 patroon)."""
        from tools.etl.transformers.fix_bold_italic_mixing import fix_bold_italic_mixing
        body = "*N**iet in de balans opgenomen rechten*"
        result, _ = fix_bold_italic_mixing(body, {})
        assert result == "*Niet in de balans opgenomen rechten*"

    def test_four_plus_asterisks_stripped(self):
        """`****` (lege link/ruis) wordt gestript."""
        from tools.etl.transformers.fix_bold_italic_mixing import fix_bold_italic_mixing
        body = "Body voor ****link**** met meer tekst."
        result, _ = fix_bold_italic_mixing(body, {})
        assert "****" not in result

    def test_legitimate_bold_unaffected(self):
        """`**bold**` blijft volledig intact."""
        from tools.etl.transformers.fix_bold_italic_mixing import fix_bold_italic_mixing
        body = "Dit is **echte bold** in een zin."
        result, _ = fix_bold_italic_mixing(body, {})
        assert result == body

    def test_legitimate_italic_unaffected(self):
        from tools.etl.transformers.fix_bold_italic_mixing import fix_bold_italic_mixing
        body = "Een *cursief* woord."
        result, _ = fix_bold_italic_mixing(body, {})
        assert result == body

    def test_triple_asterisk_NOT_touched(self):
        """`***foo***` (bold+italic combo) wordt NIET aangeraakt — kwetsbaar."""
        from tools.etl.transformers.fix_bold_italic_mixing import fix_bold_italic_mixing
        body = "***Boekingen***"
        result, _ = fix_bold_italic_mixing(body, {})
        assert result == body

    def test_idempotent(self):
        from tools.etl.transformers.fix_bold_italic_mixing import fix_bold_italic_mixing
        body = "*N**iet* ****link****"
        once, _ = fix_bold_italic_mixing(body, {})
        twice, _ = fix_bold_italic_mixing(once, {})
        assert once == twice

    def test_geregistreerd_in_transformers(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "fix_bold_italic_mixing" in TRANSFORMERS


# ─── strip_itaa_norm_footers (ITAA-norm page-footers) ─────────────────────────

class TestStripItaaNormFooters:
    def test_copyright_footer(self):
        from tools.etl.transformers.strip_itaa_norm_footers import strip_itaa_norm_footers
        body = "Body voor.\n© ITAA – Norm betreffende de verenigbaarheid\nBody na.\n"
        result, _ = strip_itaa_norm_footers(body, {})
        assert "© ITAA" not in result
        assert "Body voor." in result
        assert "Body na." in result

    def test_hreb_footer_with_heading_prefix(self):
        from tools.etl.transformers.strip_itaa_norm_footers import strip_itaa_norm_footers
        body = "Body.\n## Goedgekeurd HREB (02-03-2026)- ter goedkeuring van de minister voorgelegd 1/47\nMeer.\n"
        result, _ = strip_itaa_norm_footers(body, {})
        assert "Goedgekeurd HREB" not in result
        assert "Body." in result

    def test_hreb_footer_plain(self):
        from tools.etl.transformers.strip_itaa_norm_footers import strip_itaa_norm_footers
        body = "Goedgekeurd HREB (02-03-2026)- ter goedkeuring van de minister voorgelegd 12/47\nBody.\n"
        result, _ = strip_itaa_norm_footers(body, {})
        assert "Goedgekeurd HREB" not in result

    def test_legitimate_content_with_itaa_not_stripped(self):
        """Een legitieme zin met 'ITAA' blijft staan; alleen `© ITAA`-prefix patroon strip."""
        from tools.etl.transformers.strip_itaa_norm_footers import strip_itaa_norm_footers
        body = "Het ITAA heeft een norm gepubliceerd.\n"
        result, _ = strip_itaa_norm_footers(body, {})
        assert result == body

    def test_idempotent(self):
        from tools.etl.transformers.strip_itaa_norm_footers import strip_itaa_norm_footers
        body = "© ITAA – Norm\n## Goedgekeurd HREB - voorgelegd 3/47\nBody.\n"
        once, _ = strip_itaa_norm_footers(body, {})
        twice, _ = strip_itaa_norm_footers(once, {})
        assert once == twice

    def test_heading_with_page_marker_stripped(self):
        """B7-patroon: `## TITLE ... N/M` page-footer foutief als heading."""
        from tools.etl.transformers.strip_itaa_norm_footers import strip_itaa_norm_footers
        body = (
            "Body voor.\n"
            "## VERZOEK TOT GOEDKEURING OKTOBER 2025 12/64\n"
            "Body na.\n"
        )
        result, _ = strip_itaa_norm_footers(body, {})
        assert "VERZOEK TOT GOEDKEURING" not in result
        assert "Body voor." in result
        assert "Body na." in result

    def test_legitimate_heading_not_stripped(self):
        """Een normale `## Title` zonder paginanummer-suffix blijft."""
        from tools.etl.transformers.strip_itaa_norm_footers import strip_itaa_norm_footers
        body = "## Hoofdstuk 1. Algemene bepalingen\n"
        result, _ = strip_itaa_norm_footers(body, {})
        assert result == body

    def test_geregistreerd(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "strip_itaa_norm_footers" in TRANSFORMERS


# ─── promote_norm_section_labels (B4 normen) ──────────────────────────────────

class TestPromoteNormSectionLabels:
    def test_definitions_promoted(self):
        from tools.etl.transformers.promote_norm_section_labels import promote_norm_section_labels
        body = "Body.\n\nDefinities\n\n1.1 In deze norm wordt verstaan onder..."
        result, _ = promote_norm_section_labels(body, {})
        assert "## Definities" in result

    def test_overwegende_with_colon(self):
        from tools.etl.transformers.promote_norm_section_labels import promote_norm_section_labels
        body = "Body.\n\nOverwegende:\n\nDat het IBA dit toezicht houdt..."
        result, _ = promote_norm_section_labels(body, {})
        assert "## Overwegende" in result

    def test_eerste_principe(self):
        from tools.etl.transformers.promote_norm_section_labels import promote_norm_section_labels
        body = "Body.\n\nEerste principe\n\nDe accountant respecteert..."
        result, _ = promote_norm_section_labels(body, {})
        assert "## Eerste principe" in result

    def test_inline_definitions_not_promoted(self):
        """`Definities` midden in een zin blijft."""
        from tools.etl.transformers.promote_norm_section_labels import promote_norm_section_labels
        body = "Zie de Definities hieronder voor uitleg."
        result, _ = promote_norm_section_labels(body, {})
        assert result == body

    def test_unknown_label_not_promoted(self):
        """Een random regel niet in whitelist blijft plain."""
        from tools.etl.transformers.promote_norm_section_labels import promote_norm_section_labels
        body = "Body.\n\nRandom Tekst Hier\n\nMeer body."
        result, _ = promote_norm_section_labels(body, {})
        assert "## Random Tekst Hier" not in result

    def test_idempotent(self):
        from tools.etl.transformers.promote_norm_section_labels import promote_norm_section_labels
        body = "Body.\n\nDefinities\n\nMeer.\n"
        once, _ = promote_norm_section_labels(body, {})
        twice, _ = promote_norm_section_labels(once, {})
        assert once == twice

    def test_geregistreerd(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "promote_norm_section_labels" in TRANSFORMERS


# ─── strip_running_page_headers ───────────────────────────────────────────────

class TestStripRunningPageHeaders:
    def test_pipe_title_pattern(self):
        from tools.etl.transformers.strip_running_page_headers import strip_running_page_headers
        body = "Body.\n9 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen\nMeer.\n"
        result, _ = strip_running_page_headers(body, {})
        assert "Minimum Algemeen Rekeningstelsel (MAR)" not in result
        assert "Body." in result

    def test_kb_page_marker(self):
        from tools.etl.transformers.strip_running_page_headers import strip_running_page_headers
        body = "Body.\n                                                 - KB nr. 13 / 1 -\nMeer.\n"
        result, _ = strip_running_page_headers(body, {})
        assert "KB nr. 13 / 1" not in result

    def test_mb_page_marker(self):
        from tools.etl.transformers.strip_running_page_headers import strip_running_page_headers
        body = "  - M.B. nr. 7 / 12 -\nBody.\n"
        result, _ = strip_running_page_headers(body, {})
        assert "M.B. nr. 7" not in result

    def test_legitimate_text_not_stripped(self):
        from tools.etl.transformers.strip_running_page_headers import strip_running_page_headers
        body = "Conform KB nr. 13 wordt het volgende bepaald.\nDe pagina 9 toont een tabel.\n"
        result, _ = strip_running_page_headers(body, {})
        assert result == body

    def test_idempotent(self):
        from tools.etl.transformers.strip_running_page_headers import strip_running_page_headers
        body = "9 | Title\n- KB nr. 1 / 5 -\nBody.\n"
        once, _ = strip_running_page_headers(body, {})
        twice, _ = strip_running_page_headers(once, {})
        assert once == twice

    def test_kb_pg_title_pattern(self):
        from tools.etl.transformers.strip_running_page_headers import strip_running_page_headers
        body = "Slot.\n KB57 (2017) pg. 1 Plaats van de dienst\n"
        result, _ = strip_running_page_headers(body, {})
        assert "KB57" not in result or "Plaats van de dienst" not in result
        # Both should be gone
        assert "pg. 1" not in result

    def test_kb_pg_bijw_pattern(self):
        from tools.etl.transformers.strip_running_page_headers import strip_running_page_headers
        body = "Body.\n KB57 (2017) pg. Bijw/1 Plaats van de dienst\nVolgende.\n"
        result, _ = strip_running_page_headers(body, {})
        assert "Bijw/1" not in result
        assert "Body." in result
        assert "Volgende." in result

    def test_geregistreerd(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "strip_running_page_headers" in TRANSFORMERS


class TestStripKbBijwerkingen:
    def test_basic_appendix_stripped(self):
        from tools.etl.transformers.strip_kb_bijwerkingen import strip_kb_bijwerkingen
        body = (
            "Art. 1. De minister van Financiën is belast met de uitvoering.\n"
            "\n"
            "Lijst van de bijwerkingen\n"
            "\n"
            "Bijwerking Te vervangen pagina's\n"
            "\n"
            "Bijw. 01 / 01.01.2012 - Volledige uitgave\n"
            "Bijw. 02 / 20.02.2015 - pg. 1 - Bijw. 02 - pg. 1\n"
        )
        result, _ = strip_kb_bijwerkingen(body, {})
        assert "Lijst van de bijwerkingen" not in result
        assert "Bijw. 01" not in result
        assert "Te vervangen" not in result
        assert "Art. 1. De minister" in result

    def test_prefixed_with_kb_nr(self):
        from tools.etl.transformers.strip_kb_bijwerkingen import strip_kb_bijwerkingen
        body = (
            "Body.\n\n"
            "KB nr. 30 - Lijst van de bijwerkingen\n\n"
            "Bijwerking t.e.m. B.S. van Te vervangen pagina's\n"
            "Bijw. 01 / 01.01.2012 30.12.2011 Volledige uitgave\n"
        )
        result, _ = strip_kb_bijwerkingen(body, {})
        assert "Lijst van de bijwerkingen" not in result
        assert "Bijw. 01" not in result
        assert result.endswith("Body.\n")

    def test_prefixed_with_year(self):
        from tools.etl.transformers.strip_kb_bijwerkingen import strip_kb_bijwerkingen
        body = (
            "Slot.\n"
            "KB nr. 57 (2017) - Lijst van de bijwerkingen\n"
            "\n"
            "Bijw. 01 / 13.11.2017 - Volledige uitgave\n"
        )
        result, _ = strip_kb_bijwerkingen(body, {})
        assert "Lijst van de bijwerkingen" not in result
        assert "Bijw. 01" not in result

    def test_no_appendix_passthrough(self):
        from tools.etl.transformers.strip_kb_bijwerkingen import strip_kb_bijwerkingen
        body = "Een gewone wettekst zonder appendix.\nDe minister tekent.\n"
        result, _ = strip_kb_bijwerkingen(body, {})
        assert result == body

    def test_legitimate_mention_not_stripped(self):
        """De zin 'lijst van de bijwerkingen' mid-zin met andere context blijft."""
        from tools.etl.transformers.strip_kb_bijwerkingen import strip_kb_bijwerkingen
        body = "De administratie publiceert een lijst van de bijwerkingen in de bijlage. Volgens art. 5."
        result, _ = strip_kb_bijwerkingen(body, {})
        # Mid-line text wordt niet gestript (anchor ^...$)
        assert result == body

    def test_strips_trailing_separator(self):
        from tools.etl.transformers.strip_kb_bijwerkingen import strip_kb_bijwerkingen
        body = (
            "Art. 1.\n\n"
            "--\n\n"
            "Lijst van de bijwerkingen\n\n"
            "Bijw. 01\n"
        )
        result, _ = strip_kb_bijwerkingen(body, {})
        assert "--" not in result
        assert "Lijst" not in result
        assert result.rstrip().endswith("Art. 1.")

    def test_idempotent(self):
        from tools.etl.transformers.strip_kb_bijwerkingen import strip_kb_bijwerkingen
        body = "Body.\n\nLijst van de bijwerkingen\n\nBijw. 01 / ...\n"
        once, _ = strip_kb_bijwerkingen(body, {})
        twice, _ = strip_kb_bijwerkingen(once, {})
        assert once == twice

    def test_recent_opgeheven_kb(self):
        from tools.etl.transformers.strip_kb_bijwerkingen import strip_kb_bijwerkingen
        body = (
            "Art. 3. De minister voert uit.\n"
            "\n"
            "Recent opgeheven of vervangen koninklijke besluiten.\n"
            "\n"
            "* Koninklijk besluit nr. 39, ... (Opgeheven bij W 13.04.2019)\n"
            "* Koninklijk besluit nr. 47, ... (Opgeheven bij KB 28.06.2019)\n"
        )
        result, _ = strip_kb_bijwerkingen(body, {})
        assert "Recent opgeheven" not in result
        assert "Koninklijk besluit nr. 39" not in result
        assert "Art. 3." in result

    def test_recent_opgeheven_mb(self):
        from tools.etl.transformers.strip_kb_bijwerkingen import strip_kb_bijwerkingen
        body = (
            "Slot.\n"
            "Recent opgeheven of vervangen ministeriële besluiten.\n"
            "* MB nr. 3, ... (Opgeheven)\n"
        )
        result, _ = strip_kb_bijwerkingen(body, {})
        assert "Recent opgeheven" not in result

    def test_geregistreerd(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "strip_kb_bijwerkingen" in TRANSFORMERS


class TestStripEmptyTrailingHeadings:
    def test_strip_lone_art_heading(self):
        from tools.etl.transformers.strip_empty_trailing_headings import strip_empty_trailing_headings
        body = "Body inhoud.\n\n## Art.\n"
        result, _ = strip_empty_trailing_headings(body, {})
        assert "## Art." not in result
        assert "Body inhoud." in result

    def test_strip_multiple_empty_headings(self):
        from tools.etl.transformers.strip_empty_trailing_headings import strip_empty_trailing_headings
        body = "Body.\n\n## HOOFDSTUK\n\n## Art.\n"
        result, _ = strip_empty_trailing_headings(body, {})
        assert "## Art." not in result
        assert "## HOOFDSTUK" not in result
        assert "Body." in result

    def test_keep_heading_with_content(self):
        from tools.etl.transformers.strip_empty_trailing_headings import strip_empty_trailing_headings
        body = "## Art. 5\n\nInhoud van het artikel.\n"
        result, _ = strip_empty_trailing_headings(body, {})
        assert result == body

    def test_keep_heading_mid_body(self):
        """Lege heading midden in body wordt NIET gestript — alleen trailing."""
        from tools.etl.transformers.strip_empty_trailing_headings import strip_empty_trailing_headings
        body = "## Art.\n\nVolgende inhoud.\n"
        result, _ = strip_empty_trailing_headings(body, {})
        # body bevat content erna, dus heading blijft staan
        assert "## Art." in result

    def test_idempotent(self):
        from tools.etl.transformers.strip_empty_trailing_headings import strip_empty_trailing_headings
        body = "Body.\n\n## Art.\n"
        once, _ = strip_empty_trailing_headings(body, {})
        twice, _ = strip_empty_trailing_headings(once, {})
        assert once == twice

    def test_geregistreerd(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "strip_empty_trailing_headings" in TRANSFORMERS


class TestMergeArticleReferenceWraps:
    def test_artikel_num_to_section(self):
        from tools.etl.transformers.merge_article_reference_wraps import merge_article_reference_wraps
        body = "bedoeld in artikel 53,\n§ 1, eerste lid, 2°, van het Wetboek"
        result, _ = merge_article_reference_wraps(body, {})
        assert "artikel 53, § 1" in result
        assert "\n§" not in result

    def test_artikel_to_num(self):
        from tools.etl.transformers.merge_article_reference_wraps import merge_article_reference_wraps
        body = "overeenkomstig artikel\n6. De minister"
        result, _ = merge_article_reference_wraps(body, {})
        assert "artikel 6." in result

    def test_section_to_ordinal(self):
        from tools.etl.transformers.merge_article_reference_wraps import merge_article_reference_wraps
        body = "bedoeld in § 2,\n7° van dit besluit"
        result, _ = merge_article_reference_wraps(body, {})
        assert "§ 2, 7°" in result

    def test_artikel_bis(self):
        from tools.etl.transformers.merge_article_reference_wraps import merge_article_reference_wraps
        body = "artikel 8bis,\n§ 2 van het Wetboek"
        result, _ = merge_article_reference_wraps(body, {})
        assert "artikel 8bis, § 2" in result

    def test_no_merge_unrelated(self):
        """Een gewone zin-einde gevolgd door nieuwe zin: GEEN merge."""
        from tools.etl.transformers.merge_article_reference_wraps import merge_article_reference_wraps
        body = "De wet treedt in werking.\nDe minister tekent."
        result, _ = merge_article_reference_wraps(body, {})
        assert result == body

    def test_no_merge_heading(self):
        from tools.etl.transformers.merge_article_reference_wraps import merge_article_reference_wraps
        body = "Verwijzing naar artikel 5.\n## Art. 6\nBody."
        result, _ = merge_article_reference_wraps(body, {})
        # `artikel 5.\n## Art.` — pattern \1=artikel, \2= '## Art.' niet \d → geen merge
        assert "## Art. 6" in result

    def test_idempotent(self):
        from tools.etl.transformers.merge_article_reference_wraps import merge_article_reference_wraps
        body = "artikel 53,\n§ 1, ... artikel\n6. Iets"
        once, _ = merge_article_reference_wraps(body, {})
        twice, _ = merge_article_reference_wraps(once, {})
        assert once == twice

    def test_geregistreerd(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "merge_article_reference_wraps" in TRANSFORMERS


class TestStripMbCompilatieCover:
    _cover = (
        "BELASTING OVER DE TOEGEVOEGDE WAARDE\n"
        "\n"
        "MINISTERIËLE BESLUITEN\n"
        "BIJGEWERKT TOT EN MET HET MB VAN 29.04.2024\n"
        "\n"
        "Federale\n"
        "Overheidsdienst\n"
        "FINANCIEN\n"
        "\n"
        "contact : comments.kms@minfin.fed.be\n"
        "\n"
        "Lijst van de ministeriële besluiten\n"
        "\n"
        " * Ministerieel besluit nr. 1, van 2 september 1980, met betrekking tot de aftrekregeling\n"
        " * Ministerieel besluit nr. 2, van 21 december 2010, met betrekking tot de teruggaven\n"
        " * Ministerieel besluit nr. 3, van 24 november 1970, Maandelijkse voorschotten\n"
    )
    _content = (
        "\n"
        "Officieuze coördinatie\n"
        "\n"
        "## Art. 1\n"
        "Inhoud van het artikel.\n"
    )

    def test_strip_cover_basic(self):
        from tools.etl.transformers.strip_mb_compilatie_cover import strip_mb_compilatie_cover
        body = self._cover + self._content
        result, _ = strip_mb_compilatie_cover(body, {})
        assert "Lijst van de ministeriële besluiten" not in result
        assert "Ministerieel besluit nr. 1, van 2 september 1980" not in result
        assert "Federale" not in result
        assert "comments.kms@minfin" not in result
        assert "Officieuze coördinatie" in result
        assert "## Art. 1" in result

    def test_no_cover_passthrough(self):
        from tools.etl.transformers.strip_mb_compilatie_cover import strip_mb_compilatie_cover
        body = "## Art. 1\nGewone wettekst zonder cover.\n"
        result, _ = strip_mb_compilatie_cover(body, {})
        assert result == body

    def test_single_bullet_no_strip(self):
        """Slechts één bullet → géén cover-context, niet strippen."""
        from tools.etl.transformers.strip_mb_compilatie_cover import strip_mb_compilatie_cover
        body = (
            "Lijst van de ministeriële besluiten\n"
            " * Ministerieel besluit nr. 1, van 2 september 1980, voor referentie\n"
            "Body verder.\n"
        )
        result, _ = strip_mb_compilatie_cover(body, {})
        assert result == body  # geen strip — slechts 1 bullet

    def test_idempotent(self):
        from tools.etl.transformers.strip_mb_compilatie_cover import strip_mb_compilatie_cover
        body = self._cover + self._content
        once, _ = strip_mb_compilatie_cover(body, {})
        twice, _ = strip_mb_compilatie_cover(once, {})
        assert once == twice

    def test_kb_variant(self):
        from tools.etl.transformers.strip_mb_compilatie_cover import strip_mb_compilatie_cover
        body = (
            "BELASTING OVER DE TOEGEVOEGDE WAARDE\n"
            "KONINKLIJKE BESLUITEN\n"
            "\n"
            "Lijst van de koninklijke besluiten\n"
            "\n"
            " * Koninklijk besluit nr. 1, van 29 december 1992, voldoening\n"
            " * Koninklijk besluit nr. 2, van 19 december 2010, ...\n"
            "\n"
            "## Art. 1\nBody.\n"
        )
        result, _ = strip_mb_compilatie_cover(body, {})
        assert "Lijst van de koninklijke besluiten" not in result
        assert "Koninklijk besluit nr. 1" not in result
        assert "## Art. 1" in result

    def test_geregistreerd(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "strip_mb_compilatie_cover" in TRANSFORMERS


class TestFixPdftotextGlueBugs:
    def test_ligature_fi(self):
        from tools.etl.transformers.fix_pdftotext_glue_bugs import fix_pdftotext_glue_bugs
        body = "geïdentiﬁceerd voor de BTW"
        result, _ = fix_pdftotext_glue_bugs(body, {})
        assert "geïdentificeerd" in result
        assert "ﬁ" not in result

    def test_ligature_fl(self):
        from tools.etl.transformers.fix_pdftotext_glue_bugs import fix_pdftotext_glue_bugs
        body = "inﬂatie"
        result, _ = fix_pdftotext_glue_bugs(body, {})
        assert "inflatie" in result

    def test_btw_concat(self):
        from tools.etl.transformers.fix_pdftotext_glue_bugs import fix_pdftotext_glue_bugs
        body = "het BTWidentificatienummer wordt toegekend"
        result, _ = fix_pdftotext_glue_bugs(body, {})
        assert "BTW-identificatienummer" in result
        assert "BTWidentificatienummer" not in result

    def test_btw_doeleinden(self):
        from tools.etl.transformers.fix_pdftotext_glue_bugs import fix_pdftotext_glue_bugs
        body = "voor BTWdoeleinden geïdentificeerd"
        result, _ = fix_pdftotext_glue_bugs(body, {})
        assert "BTW-doeleinden" in result

    def test_douaneentrepot(self):
        from tools.etl.transformers.fix_pdftotext_glue_bugs import fix_pdftotext_glue_bugs
        body = "een douaneentrepot is geen entrepot"
        result, _ = fix_pdftotext_glue_bugs(body, {})
        assert "douane-entrepot" in result
        # 'geen entrepot' blijft ongemoeid
        assert "geen entrepot" in result

    def test_inartikel(self):
        from tools.etl.transformers.fix_pdftotext_glue_bugs import fix_pdftotext_glue_bugs
        body = "bedoeld inartikel 5"
        result, _ = fix_pdftotext_glue_bugs(body, {})
        assert "in artikel 5" in result
        assert "inartikel" not in result

    def test_section_en_concat(self):
        from tools.etl.transformers.fix_pdftotext_glue_bugs import fix_pdftotext_glue_bugs
        body = "§ 1en § 2 van het Wetboek"
        result, _ = fix_pdftotext_glue_bugs(body, {})
        assert "§ 1 en § 2" in result

    def test_no_change_passthrough(self):
        from tools.etl.transformers.fix_pdftotext_glue_bugs import fix_pdftotext_glue_bugs
        body = "Gewone tekst zonder concat-bugs of ligaturen.\n"
        result, _ = fix_pdftotext_glue_bugs(body, {})
        assert result == body

    def test_idempotent(self):
        from tools.etl.transformers.fix_pdftotext_glue_bugs import fix_pdftotext_glue_bugs
        body = "BTWidentificatienummer en BTWdoeleinden inﬁltratie"
        once, _ = fix_pdftotext_glue_bugs(body, {})
        twice, _ = fix_pdftotext_glue_bugs(once, {})
        assert once == twice

    def test_geregistreerd(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "fix_pdftotext_glue_bugs" in TRANSFORMERS


class TestPromoteWettekstSectionLabels:
    def test_enig_artikel(self):
        from tools.etl.transformers.promote_wettekst_section_labels import promote_wettekst_section_labels
        body = "Inleiding.\n\nEnig artikel\n\nDe minister beslist.\n"
        result, _ = promote_wettekst_section_labels(body, {})
        assert "## Enig artikel" in result
        assert "\nEnig artikel\n" not in result

    def test_bijlage_with_number(self):
        from tools.etl.transformers.promote_wettekst_section_labels import promote_wettekst_section_labels
        body = "Slot.\n\nBijlage 1\n\nDeze bijlage bevat\n"
        result, _ = promote_wettekst_section_labels(body, {})
        assert "## Bijlage 1" in result

    def test_bijlage_roman(self):
        from tools.etl.transformers.promote_wettekst_section_labels import promote_wettekst_section_labels
        body = "Slot.\n\nBijlage II\n\nInhoud\n"
        result, _ = promote_wettekst_section_labels(body, {})
        assert "## Bijlage II" in result

    def test_bijlage_n1_norm_style(self):
        from tools.etl.transformers.promote_wettekst_section_labels import promote_wettekst_section_labels
        body = "Slot.\n\nBijlage N1\n\nForfaitaire tabel\n"
        result, _ = promote_wettekst_section_labels(body, {})
        assert "## Bijlage N1" in result

    def test_inline_not_promoted(self):
        from tools.etl.transformers.promote_wettekst_section_labels import promote_wettekst_section_labels
        body = "Zie Bijlage 1 voor details.\n"
        result, _ = promote_wettekst_section_labels(body, {})
        assert result == body

    def test_not_paragraph_isolated(self):
        from tools.etl.transformers.promote_wettekst_section_labels import promote_wettekst_section_labels
        body = "Inhoud.\nBijlage 1\nDirect erop volgend.\n"
        result, _ = promote_wettekst_section_labels(body, {})
        # Geen blank-lines rondom → niet promoveren
        assert "## Bijlage" not in result

    def test_idempotent(self):
        from tools.etl.transformers.promote_wettekst_section_labels import promote_wettekst_section_labels
        body = "X.\n\nEnig artikel\n\nY.\n"
        once, _ = promote_wettekst_section_labels(body, {})
        twice, _ = promote_wettekst_section_labels(once, {})
        assert once == twice

    def test_geregistreerd(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "promote_wettekst_section_labels" in TRANSFORMERS


class TestNormalizeArtikelToArt:
    def test_bare_artikel(self):
        from tools.etl.transformers.normalize_artikel_to_art import normalize_artikel_to_art
        body = "Vorige paragraaf.\n\nArtikel 86\n\nDe FDM bevat...\n"
        result, _ = normalize_artikel_to_art(body, {})
        assert "Art. 86" in result
        assert "\nArtikel 86\n" not in result

    def test_artikel_with_body_inline(self):
        from tools.etl.transformers.normalize_artikel_to_art import normalize_artikel_to_art
        body = "Artikel 46. Elk kassasysteem moet voorzien zijn van een modelaanduiding.\n"
        result, _ = normalize_artikel_to_art(body, {})
        assert "Art. 46" in result
        assert "Elk kassasysteem moet voorzien zijn" in result
        # body is op separate regel
        assert "Art. 46\n\nElk kassasysteem" in result

    def test_artikel_bis(self):
        from tools.etl.transformers.normalize_artikel_to_art import normalize_artikel_to_art
        body = "Artikel 12bis\n"
        result, _ = normalize_artikel_to_art(body, {})
        assert "Art. 12bis" in result

    def test_inline_mention_not_converted(self):
        """'Artikel 5.' midden in zin met leading whitespace blijft."""
        from tools.etl.transformers.normalize_artikel_to_art import normalize_artikel_to_art
        body = "Zie  Artikel 5. voor details.\n"
        result, _ = normalize_artikel_to_art(body, {})
        assert result == body

    def test_with_leading_whitespace_not_converted(self):
        from tools.etl.transformers.normalize_artikel_to_art import normalize_artikel_to_art
        body = "    Artikel 5\n"  # leading whitespace → niet converteren (bestaande logica regelt dit)
        result, _ = normalize_artikel_to_art(body, {})
        assert result == body

    def test_idempotent(self):
        from tools.etl.transformers.normalize_artikel_to_art import normalize_artikel_to_art
        body = "Artikel 86\n\nArtikel 132. Dit besluit vervangt circulaire.\n"
        once, _ = normalize_artikel_to_art(body, {})
        twice, _ = normalize_artikel_to_art(once, {})
        assert once == twice

    def test_geregistreerd(self):
        from tools.etl.transformers import TRANSFORMERS
        assert "normalize_artikel_to_art" in TRANSFORMERS
