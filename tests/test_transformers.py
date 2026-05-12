"""
Unit-tests voor de transformer-laag (tools/etl/transformers/).

Dekt:
  - apply_chain(): chaining-mechanisme + foutafhandeling
  - cleanup_basics: _cleanup_steps doorgeven via frontmatter
  - inject_headings_wettekst: heading-injectie op eenvoudige body
  - organize_headings: noop-placeholder
  - emit_frontmatter: YAML-blok + chunk-blok + intro-content
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
