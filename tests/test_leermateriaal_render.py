"""
Smoke-tests voor tools/leermateriaal/ render-tooling (ADR-007 schema 1.3 + ADR-010).

Bevat 15+ deterministische tests zonder LLM-calls en zonder netwerkverbindingen.
"""

from __future__ import annotations

import json
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent


# ─── Fixtures ──────────────────────────────────────────────────────────────────


FIXTURE_RECORD = {
    "id": "test-concept",
    "naam": "Testconcept",
    "node_type": "begrip",
    "schema_version": "1.3",
    "status": "seed",
    "linked_anchors": ["1.4.I.A", "1.4.I.B"],
    "_provenance": {
        "extractor_run": "test-run",
        "model": "claude-opus-4-7",
        "anchor_id": "1.4.I.A",
        "dekt_ook_anchors": ["1.4.I.B"],
        "reviewed_by": None,
    },
    "definitie": {
        "text": "Een testdefinitie voor smoke-testing.",
        "confidence": "grounded",
        "source": {"type": "wet", "short": "WVV art. 1:1"},
        "_provenance": {
            "inputs": [{"id": "test-chunk-001", "sha256": None, "version": "rag-v1"}]
        },
    },
    "rationale": {
        "text": "Dit concept telt omdat het het fundament legt voor consolidatieregelgeving.",
        "confidence": "inferred",
        "_provenance": {
            "inputs": [{"id": "test-chunk-001", "sha256": None, "version": "rag-v1"}],
            "verrijkt_door": "enrich-run-test",
            "verrijkt_op": "2026-05-15T00:00:00Z",
        },
    },
    "valkuilen": [
        {
            "text": "Niet verwarren met invloed van betekenis.",
            "confidence": "grounded",
            "source": {"type": "wet", "short": "WVV art. 1:14"},
            "_provenance": {
                "inputs": [{"id": "test-chunk-002", "sha256": None, "version": "rag-v1"}]
            },
        }
    ],
    "in_praktijk": [
        {
            "aspect": "Boekhoudkundige verwerking",
            "betekenis": "De standaard boekhoudkundige verwerking van dit concept.",
            "herkenningspunt": "Kijk naar de balanspost.",
            "confidence": "grounded",
            "source": {"type": "wet", "short": "KB WVV art. 3:1"},
            "_provenance": {
                "inputs": [{"id": "test-chunk-003", "sha256": None, "version": "rag-v1"}]
            },
        }
    ],
}

FIXTURE_COMPETENTIE_VALIDE = {
    "id": "test-competentie",
    "titel": "Test: Bepalen van X",
    "status": "voorgesteld",
    "schema_version": "1.0",
    "programmaonderdelen": ["1.4"],
    "voortkomend_uit": {
        "taken": ["1.4.taak.1"],
        "kenniselementen": ["1.4.I.A"],
    },
    "gebaseerd_op_concepten": ["test-concept-a", "test-concept-b"],
    "procedure_grondslag": {
        "wettelijk_pct": 80,
        "praktijk_pct": 20,
        "motivering": "Drempels zijn wettelijk; volgorde is gebruikelijke werkwijze.",
    },
    "stappen": [
        {
            "nr": 1,
            "titel": "Voer stap 1 uit",
            "input": "Aandeelhoudersregister",
            "output": "Lijst kandidaat-dochters",
            "waarom": "Scope bepalen.",
            "grondslag": {
                "type": "concept",
                "ref": "[[test-concept-a]]",
            },
            "valkuilen": [],
        }
    ],
    "_provenance": {
        "voorgesteld_door": "test-run",
        "voorgesteld_op": "2026-05-15T00:00:00Z",
        "gecureerd_door": None,
        "gecureerd_op": None,
    },
}

FIXTURE_COMPETENTIE_INVALIDE_TE_WEINIG_CONCEPTEN = {
    **FIXTURE_COMPETENTIE_VALIDE,
    "gebaseerd_op_concepten": ["slechts-één-concept"],
}

FIXTURE_COMPETENTIE_INVALIDE_STAP_ZONDER_GRONDSLAG = {
    **FIXTURE_COMPETENTIE_VALIDE,
    "stappen": [
        {
            "nr": 1,
            "titel": "Stap zonder grondslag",
            "input": "Iets",
            "output": "Iets anders",
            "waarom": "Onbekend.",
            # grondslag ontbreekt opzettelijk
        }
    ],
}

FIXTURE_COMPETENTIE_WAARSCHUWING_PRAKTIJK_PCT = {
    **FIXTURE_COMPETENTIE_VALIDE,
    "procedure_grondslag": {
        "wettelijk_pct": 30,
        "praktijk_pct": 70,
        "motivering": "Veel praktijk in dit domein.",
    },
}


# ─── Tests: confidence.py ──────────────────────────────────────────────────────


class TestConfidence:
    def test_label_grounded_geeft_weegschaal(self) -> None:
        from tools.leermateriaal.lib.confidence import label

        assert label("grounded") == "⚖️"

    def test_label_inferred_geeft_robot(self) -> None:
        from tools.leermateriaal.lib.confidence import label

        assert label("inferred") == "🤖"

    def test_label_inferred_from_aggregation_geeft_robot(self) -> None:
        from tools.leermateriaal.lib.confidence import label

        assert label("inferred-from-aggregation") == "🤖"

    def test_label_onbekend_geeft_robot(self) -> None:
        from tools.leermateriaal.lib.confidence import label

        assert label("onbekend") == "🤖"

    def test_mode_confidence_op_fixture_record(self) -> None:
        from tools.leermateriaal.lib.confidence import mode_confidence

        result = mode_confidence(FIXTURE_RECORD)
        assert result == "grounded"

    def test_mode_confidence_fallback_op_leeg_record(self) -> None:
        from tools.leermateriaal.lib.confidence import mode_confidence

        result = mode_confidence({})
        assert result == "inferred"

    def test_inline_combineert_tekst_en_label(self) -> None:
        from tools.leermateriaal.lib.confidence import inline

        result = inline("Een claim", "grounded")
        assert result == "Een claim ⚖️"


# ─── Tests: wikilinks.py ───────────────────────────────────────────────────────


class TestWikilinks:
    def test_concept_link_zonder_label(self) -> None:
        from tools.leermateriaal.lib.wikilinks import concept_link

        assert concept_link("controle") == "[[controle]]"

    def test_concept_link_met_label(self) -> None:
        from tools.leermateriaal.lib.wikilinks import concept_link

        assert concept_link("controle", "Controle") == "[[controle|Controle]]"

    def test_concept_aspect_link(self) -> None:
        from tools.leermateriaal.lib.wikilinks import concept_aspect_link

        result = concept_aspect_link("leasing", "boekhoudkundige-verwerking", "Boekhoudkundige verwerking")
        assert result == "[[leasing#boekhoudkundige-verwerking|Boekhoudkundige verwerking]]"

    def test_competentie_link(self) -> None:
        from tools.leermateriaal.lib.wikilinks import competentie_link

        result = competentie_link("bepalen-consolidatieverplichting")
        assert result == "[[competenties/bepalen-consolidatieverplichting]]"

    def test_slugify_boekhoudkundige_verwerking(self) -> None:
        from tools.leermateriaal.lib.wikilinks import slugify

        assert slugify("Boekhoudkundige verwerking") == "boekhoudkundige-verwerking"

    def test_slugify_accent_stripping(self) -> None:
        from tools.leermateriaal.lib.wikilinks import slugify

        assert slugify("Éèêë verwerking") == "eeee-verwerking"

    def test_slugify_speciale_tekens(self) -> None:
        from tools.leermateriaal.lib.wikilinks import slugify

        assert slugify("WVV art. 1:14 §2") == "wvv-art-1-14-2"


# ─── Tests: frontmatter.py ─────────────────────────────────────────────────────


class TestFrontmatter:
    def test_as_yaml_block_produceert_geldig_yaml(self) -> None:
        from tools.leermateriaal.lib.frontmatter import as_yaml_block

        blok = as_yaml_block({"title": "Test", "tags": ["concept", "begrip"]})
        assert blok.startswith("---\n")
        assert blok.endswith("---\n")

        # Parseerbaar als YAML
        parsed = yaml.safe_load(blok.strip("---\n").strip())
        assert parsed["title"] == "Test"

    def test_concept_fiche_frontmatter_bevat_tags(self) -> None:
        from tools.leermateriaal.lib.frontmatter import concept_fiche_frontmatter

        frontmatter = concept_fiche_frontmatter(FIXTURE_RECORD)
        assert "concept" in frontmatter["tags"]
        assert "begrip" in frontmatter["tags"]

    def test_concept_fiche_frontmatter_po_codes(self) -> None:
        from tools.leermateriaal.lib.frontmatter import concept_fiche_frontmatter

        frontmatter = concept_fiche_frontmatter(FIXTURE_RECORD)
        assert frontmatter["programmaonderdelen"] == ["1.4"]

    def test_minicursus_frontmatter_bevat_po(self) -> None:
        from tools.leermateriaal.lib.frontmatter import minicursus_frontmatter

        fm = minicursus_frontmatter("1.4", "Geconsolideerde jaarrekening", ["controle"])
        assert fm["programmaonderdeel"] == "1.4"
        assert "minicursus" in fm["tags"]


# ─── Tests: validate_competentie.py ───────────────────────────────────────────


class TestValidateCompetentie:
    def test_valide_competentie_geeft_geen_fouten(self) -> None:
        from tools.leermateriaal.lib.validate_competentie import validate

        # Fixture heeft 2 concepten maar die bestaan mogelijk niet in records/
        # We testen alleen de structurele validatie
        fouten = validate(FIXTURE_COMPETENTIE_VALIDE)
        # Alleen waarschuwingen over niet-bestaande records zijn OK (WAARSCHUWING: prefix)
        echte_fouten = [f for f in fouten if f.startswith("FOUT:")]
        assert len(echte_fouten) == 0

    def test_te_weinig_gebaseerd_op_concepten(self) -> None:
        from tools.leermateriaal.lib.validate_competentie import validate

        fouten = validate(FIXTURE_COMPETENTIE_INVALIDE_TE_WEINIG_CONCEPTEN)
        echte_fouten = [f for f in fouten if f.startswith("FOUT:")]
        assert any("gebaseerd_op_concepten" in f for f in echte_fouten)

    def test_stap_zonder_grondslag(self) -> None:
        from tools.leermateriaal.lib.validate_competentie import validate

        fouten = validate(FIXTURE_COMPETENTIE_INVALIDE_STAP_ZONDER_GRONDSLAG)
        echte_fouten = [f for f in fouten if f.startswith("FOUT:")]
        assert any("grondslag" in f for f in echte_fouten)

    def test_praktijk_pct_boven_50_geeft_waarschuwing(self) -> None:
        from tools.leermateriaal.lib.validate_competentie import validate

        fouten = validate(FIXTURE_COMPETENTIE_WAARSCHUWING_PRAKTIJK_PCT)
        waarschuwingen = [f for f in fouten if f.startswith("WAARSCHUWING:")]
        assert any("praktijk_pct" in f and "50" in f for f in waarschuwingen)

    def test_pct_som_niet_100_geeft_fout(self) -> None:
        from tools.leermateriaal.lib.validate_competentie import validate

        comp = {
            **FIXTURE_COMPETENTIE_VALIDE,
            "procedure_grondslag": {
                "wettelijk_pct": 60,
                "praktijk_pct": 60,
                "motivering": "Test",
            },
        }
        fouten = validate(comp)
        echte_fouten = [f for f in fouten if f.startswith("FOUT:")]
        assert any("100" in f for f in echte_fouten)


# ─── Tests: render_concept_fiche.py ───────────────────────────────────────────


class TestRenderConceptFiche:
    def test_render_record_produceert_frontmatter(self) -> None:
        from tools.leermateriaal.render_concept_fiche import render_record

        md = render_record(FIXTURE_RECORD)
        assert md.startswith("---\n")
        assert "title:" in md
        assert "tags:" in md

    def test_render_record_bevat_naam(self) -> None:
        from tools.leermateriaal.render_concept_fiche import render_record

        md = render_record(FIXTURE_RECORD)
        assert "Testconcept" in md

    def test_render_record_bevat_rationale_callout(self) -> None:
        from tools.leermateriaal.render_concept_fiche import render_record

        md = render_record(FIXTURE_RECORD)
        assert "[!note]" in md
        assert "Waarom dit telt" in md

    def test_render_record_bevat_anker_slug(self) -> None:
        from tools.leermateriaal.render_concept_fiche import render_record

        md = render_record(FIXTURE_RECORD)
        # in_praktijk heeft "Boekhoudkundige verwerking" → slug "boekhoudkundige-verwerking"
        assert "boekhoudkundige-verwerking" in md

    def test_render_record_bevat_provenance_bronnen(self) -> None:
        from tools.leermateriaal.render_concept_fiche import render_record

        md = render_record(FIXTURE_RECORD)
        assert "test-chunk-001" in md


# ─── Tests: render_competentie_fiche.py ───────────────────────────────────────


class TestRenderCompetentieFiche:
    def test_render_competentie_bevat_procedure_grondslag_badge(self) -> None:
        from tools.leermateriaal.render_competentie_fiche import render_competentie

        md = render_competentie(FIXTURE_COMPETENTIE_VALIDE)
        assert "⚖️ 80%" in md
        assert "🤖 20%" in md

    def test_render_competentie_bevat_stap(self) -> None:
        from tools.leermateriaal.render_competentie_fiche import render_competentie

        md = render_competentie(FIXTURE_COMPETENTIE_VALIDE)
        assert "Voer stap 1 uit" in md

    def test_render_competentie_bevat_frontmatter(self) -> None:
        from tools.leermateriaal.render_competentie_fiche import render_competentie

        md = render_competentie(FIXTURE_COMPETENTIE_VALIDE)
        assert md.startswith("---\n")


# ─── Tests: Schema 1.4-features ────────────────────────────────────────────────


class TestSchema14Render:
    """Smoke-tests voor schema 1.4-render-features (ADR-007 §schema 1.4)."""

    def test_bouwsteen_blok_rendert_waarom_en_voorbeeld(self) -> None:
        """Bouwsteen-blok schema 1.4 (titel/wat/waarom/voorbeeld_inline/grondslag) rendert volledig."""
        from tools.leermateriaal.render_concept_fiche import render_record

        record = {
            "id": "test-bouwsteen",
            "naam": "Test",
            "node_type": "begrip",
            "schema_version": "1.4",
            "status": "seed",
            "linked_anchors": ["1.4.I.A"],
            "_provenance": {"extractor_run": "test", "model": "test", "anchor_id": "1.4.I.A"},
            "definitie": {"text": "Een definitie."},
            "bouwstenen": [
                {
                    "titel": "Korte titel",
                    "wat": "Wat-veld",
                    "waarom": "Waarom-veld",
                    "voorbeeld_inline": "Aurelia doet X.",
                    "grondslag": "KB WVV art. 1:14",
                    "confidence": "grounded",
                }
            ],
        }
        md = render_record(record)
        assert "Korte titel" in md
        assert "Wat-veld" in md
        assert "Waarom-veld" in md or "Waarom?" in md
        assert "Aurelia doet X." in md

    def test_synthese_record_rendert_vergelijkingstabel(self) -> None:
        """node_type: synthese krijgt eigen render-tak met vergelijkingstabel."""
        from tools.leermateriaal.render_concept_fiche import render_record

        record = {
            "id": "test-synthese",
            "naam": "Synthese",
            "node_type": "synthese",
            "schema_version": "1.4",
            "status": "seed",
            "linked_anchors": ["1.4.I.A"],
            "gebaseerd_op_concepten": ["concept-a", "concept-b"],
            "_provenance": {"extractor_run": "test", "model": "test", "anchor_id": "1.4.I.A"},
            "inleiding": {"text": "Inleidingstekst."},
            "vergelijkingstabel": {
                "data": "| A | B |\n|---|---|\n| 1 | 2 |",
                "confidence": "inferred",
            },
        }
        md = render_record(record)
        assert "Inleidingstekst." in md
        assert "Vergelijkingstabel" in md or "| A | B |" in md

    def test_stap_blok_rendert_hoe_en_substappen(self) -> None:
        """Competentie-stap-blok met hoe + substappen rendert volledig."""
        from tools.leermateriaal.render_competentie_fiche import render_competentie

        competentie = {
            "id": "test-comp",
            "titel": "Test competentie",
            "status": "voorgesteld",
            "schema_version": "1.1",
            "programmaonderdelen": ["1.4"],
            "voortkomend_uit": {"taken": [], "kenniselementen": []},
            "gebaseerd_op_concepten": ["concept-a", "concept-b"],
            "procedure_grondslag": {
                "wettelijk_pct": 80,
                "praktijk_pct": 20,
                "motivering": "Test.",
            },
            "stappen": [
                {
                    "nr": 1,
                    "titel": "Eerste stap",
                    "wat": "Wat-uitleg.",
                    "hoe": "1. Doe X.\n2. Doe Y.",
                    "grondslag": "[[concept-a]]",
                    "voorbeeld": {
                        "scenario": "Scenario met Aurelia.",
                        "substappen": [
                            {"nr": 1, "titel": "Sub", "type": "balans", "data": "| A |\n|---|"},
                        ],
                    },
                }
            ],
        }
        md = render_competentie(competentie)
        assert "🛠️ Hoe" in md or "**Hoe**" in md
        assert "Doe X." in md
        assert "Scenario met Aurelia." in md
        assert "📊" in md or "Substap" in md

    def test_valkuil_advies_titel_fallback_op_correctie(self) -> None:
        """Valkuil-render gebruikt advies-veld; valt terug op correctie."""
        from tools.leermateriaal.render_competentie_fiche import render_competentie

        for valkuil_dict in [
            {"advies": "Doe altijd Z", "vaak_fout": "Y vergeten", "grondslag": "[[a]]"},
            {"correctie": "Doe altijd Z", "foute_aanname": "Y vergeten", "grondslag": "[[a]]"},
        ]:
            competentie = {
                "id": "test", "titel": "T", "status": "voorgesteld",
                "schema_version": "1.0", "programmaonderdelen": ["1.4"],
                "voortkomend_uit": {"taken": [], "kenniselementen": []},
                "gebaseerd_op_concepten": ["a", "b"],
                "procedure_grondslag": {"wettelijk_pct": 100, "praktijk_pct": 0, "motivering": "T"},
                "stappen": [{
                    "nr": 1, "titel": "S", "grondslag": "[[a]]",
                    "valkuilen": [valkuil_dict],
                }],
            }
            md = render_competentie(competentie)
            assert "Doe altijd Z" in md
            assert "Y vergeten" in md


# ─── Tests: Callout-conventies (ADR-010 §Callout-conventies 2026-05-16) ──────


class TestCalloutConventies:
    """Verifieer dat alle callout-typen correct worden gegenereerd (ADR-010 §Callout-conventies)."""

    def _maak_record(self, **extra) -> dict:
        basis = {
            "id": "test-callout",
            "naam": "Callout-test",
            "node_type": "begrip",
            "schema_version": "1.4",
            "status": "seed",
            "linked_anchors": ["1.4.I.A"],
            "_provenance": {"extractor_run": "test", "model": "test", "anchor_id": "1.4.I.A"},
        }
        basis.update(extra)
        return basis

    def test_tl_dr_callout_summary_niet_collapsible(self) -> None:
        """TL;DR uit definitie → [!summary] zonder collapsible suffix."""
        from tools.leermateriaal.render_concept_fiche import render_record

        record = self._maak_record(definitie={"text": "Een zin. Nog meer tekst."})
        md = render_record(record)
        assert "> [!summary] Korte inhoud" in md
        assert "> [!summary]-" not in md  # NIET collapsible

    def test_definitie_geen_blockquote(self) -> None:
        """Definitie-tekst staat als gewone paragraaf, NIET in een extra blockquote buiten de callout."""
        from tools.leermateriaal.render_concept_fiche import render_record

        # Gebruik een definitie met meerdere zinnen zodat de volledige tekst
        # als gewone paragraaf verschijnt en de TL;DR-callout alleen de eerste zin bevat.
        record = self._maak_record(
            definitie={"text": "Eerste zin. Tweede zin met meer uitleg over het concept."}
        )
        md = render_record(record)
        # Volledige tekst als gewone paragraaf
        assert "Tweede zin met meer uitleg over het concept." in md
        # De [!summary] callout bevat alleen de eerste zin
        assert "> [!summary] Korte inhoud" in md
        assert "> Eerste zin." in md  # in de callout
        # "Tweede zin" mag NIET als blockquote verschijnen
        assert "> Tweede zin" not in md

    def test_valkuilen_warning_collapsible_per_item(self) -> None:
        """Valkuilen → [!warning]- collapsible, één per item."""
        from tools.leermateriaal.render_concept_fiche import render_record

        record = self._maak_record(
            definitie={"text": "Test."},
            valkuilen=[
                {"text": "Fout A.", "confidence": "grounded"},
                {"text": "Fout B.", "confidence": "grounded"},
            ],
        )
        md = render_record(record)
        # Twee aparte collapsible warning-callouts
        assert md.count("> [!warning]-") == 2

    def test_vergelijkingsparen_info_collapsible_per_paar(self) -> None:
        """Vergelijkingsparen → [!info]- per paar, NIET één grote container."""
        from tools.leermateriaal.render_concept_fiche import render_record

        record = self._maak_record(
            definitie={"text": "Test."},
            vergelijkingsparen=[
                {"vergelijking_met": "concept-a", "verschil": "Verschil X."},
                {"vergelijking_met": "concept-b", "verschil": "Verschil Y."},
            ],
        )
        md = render_record(record)
        assert "> [!info]- Niet verwarren met [[concept-a]]" in md
        assert "> [!info]- Niet verwarren met [[concept-b]]" in md
        assert "<details>" not in md  # oude HTML-render weg

    def test_in_praktijk_tip_callout(self) -> None:
        """in_praktijk[*] → [!tip]- callout per aspect."""
        from tools.leermateriaal.render_concept_fiche import render_record

        record = self._maak_record(
            definitie={"text": "Test."},
            in_praktijk=[
                {
                    "aspect": "Testaspect",
                    "betekenis": "Uitleg van het aspect.",
                    "herkenningspunt": "Kijk naar X.",
                    "confidence": "grounded",
                }
            ],
        )
        md = render_record(record)
        assert "> [!tip]- Testaspect" in md
        assert "id=\"testaspect\"" in md  # HTML-anker aanwezig
        assert "{id=" not in md  # geen Quartz-syntax {id=...}

    def test_edges_onderdeel_van_info_niet_collapsible(self) -> None:
        """Edges onderdeel-van → inline [!info] zonder collapsible suffix."""
        from tools.leermateriaal.render_concept_fiche import render_record

        record = self._maak_record(
            definitie={"text": "Test."},
            edges=[{"type": "onderdeel-van", "target": "parent-concept"}],
        )
        md = render_record(record)
        assert "> [!info] Behoort tot: [[parent-concept]]" in md
        assert "> [!info]- Behoort tot:" not in md  # NIET collapsible

    def test_bevat_edges_niet_gerenderd_in_niet_synthese(self) -> None:
        """Edges van type 'bevat' worden NIET gerenderd op niet-synthese-fiches."""
        from tools.leermateriaal.render_concept_fiche import render_record

        record = self._maak_record(
            definitie={"text": "Test."},
            edges=[{"type": "bevat", "target": "child-concept"}],
        )
        md = render_record(record)
        assert "Bestaat uit" not in md
        assert "child-concept" not in md

    def test_voorbeeld_ontbreekt_todo_callout(self) -> None:
        """Geen voorbeeld in record → [!todo] callout (niet collapsible)."""
        from tools.leermateriaal.render_concept_fiche import render_record

        record = self._maak_record(definitie={"text": "Test."})
        md = render_record(record)
        assert "> [!todo] Voorbeeld ontbreekt" in md
        assert "> [!todo]-" not in md  # NIET collapsible

    def test_stap_voorbeeld_in_example_callout(self) -> None:
        """Stap.voorbeeld.scenario → [!example]- callout (collapsible)."""
        from tools.leermateriaal.render_competentie_fiche import render_competentie

        competentie = {
            "id": "test", "titel": "T", "status": "voorgesteld",
            "schema_version": "1.1", "programmaonderdelen": ["1.4"],
            "voortkomend_uit": {"taken": [], "kenniselementen": []},
            "gebaseerd_op_concepten": ["a", "b"],
            "procedure_grondslag": {"wettelijk_pct": 80, "praktijk_pct": 20, "motivering": "T"},
            "stappen": [{
                "nr": 1, "titel": "Stap 1", "grondslag": "[[a]]",
                "voorbeeld": {
                    "scenario": "Aurelia doet iets met Brugse.",
                    "substappen": [],
                },
            }],
        }
        md = render_competentie(competentie)
        assert "> [!example]-" in md
        assert "Aurelia doet iets met Brugse." in md

    def test_competentie_voorbeelden_in_example_callouts(self) -> None:
        """Competentie.voorbeelden[] → [!example]- callout per voorbeeld."""
        from tools.leermateriaal.render_competentie_fiche import render_competentie

        competentie = {
            "id": "test", "titel": "T", "status": "voorgesteld",
            "schema_version": "1.1", "programmaonderdelen": ["1.4"],
            "voortkomend_uit": {"taken": [], "kenniselementen": []},
            "gebaseerd_op_concepten": ["a", "b"],
            "procedure_grondslag": {"wettelijk_pct": 80, "praktijk_pct": 20, "motivering": "T"},
            "stappen": [{"nr": 1, "titel": "S", "grondslag": "[[a]]"}],
            "voorbeelden": [
                {
                    "situatie": "Situatie X is aanwezig.",
                    "conclusie": "Conclusie Y.",
                    "grondslag": "[[a]]",
                    "redenering": "Redenering Z.",
                }
            ],
        }
        md = render_competentie(competentie)
        assert "> [!example]-" in md
        assert "Conclusie Y." in md
        assert "Redenering Z." in md

    def test_edge_callout_gevolgd_door_blank_line(self) -> None:
        """Edge-breadcrumb-callout heeft een blank line tussen callout en definition-text (anti-merge)."""
        from tools.leermateriaal.render_concept_fiche import render_record

        record = self._maak_record(
            definitie={"text": "Definitie-tekst hier."},
            edges=[{"type": "specialisatie-van", "target": "parent-x"}],
        )
        md = render_record(record)
        # Verwachte volgorde: callout-regel, blank line, definition-paragraaf
        # Niet acceptabel: callout-regel direct gevolgd door definition (zou mergen)
        callout_lijn = "> [!info] Specialisatie van: [[parent-x]]"
        idx = md.find(callout_lijn)
        assert idx >= 0, "edge-callout ontbreekt"
        na_callout = md[idx + len(callout_lijn):]
        # Eerste karakters na de callout-regel moeten dubbele newline (= blank line) zijn
        assert na_callout.startswith("\n\n"), (
            f"edge-callout moet gevolgd worden door blank line (Quartz lazy-continuation): "
            f"got {na_callout[:30]!r}"
        )

    def test_consecutive_valkuilen_gescheiden_door_blank_line(self) -> None:
        """Twee opeenvolgende valkuilen worden door blank line gescheiden (anti-merge)."""
        from tools.leermateriaal.render_concept_fiche import render_record

        record = self._maak_record(
            definitie={"text": "Test."},
            valkuilen=[
                {"text": "Eerste valkuil.", "confidence": "grounded"},
                {"text": "Tweede valkuil.", "confidence": "grounded"},
            ],
        )
        md = render_record(record)
        # Zoek de eerste en tweede [!warning]- callout
        eerste = md.find("> [!warning]- Eerste valkuil")
        tweede = md.find("> [!warning]- Tweede valkuil")
        assert eerste >= 0 and tweede > eerste
        # Tussen einde van eerste callout-blok en begin tweede moet een blank line zitten
        tussen = md[eerste:tweede]
        assert "\n\n" in tussen, (
            f"twee valkuilen moeten door blank line gescheiden zijn, anders mergden ze in Quartz: "
            f"tussen={tussen!r}"
        )

    def test_eerste_zin_filter_behoudt_eurobedragen(self) -> None:
        """eerste_zin-filter splitst NIET op duizendtal-punten in €-bedragen."""
        from tools.leermateriaal.lib.jinja_env import _eerste_zin

        tekst = "Aurelia betaalt € 1.600.000 voor Brugse. Geen verdere details."
        # Eerste zin moet het volledige bedrag bevatten
        resultaat = _eerste_zin(tekst, 120)
        assert "€ 1.600.000" in resultaat
        assert "voor Brugse" in resultaat

    def test_eerste_zin_filter_behoudt_wetsverwijzingen(self) -> None:
        """eerste_zin-filter splitst NIET op 'art.' wanneer dat een Belgisch-juridische afkorting is."""
        from tools.leermateriaal.lib.jinja_env import _eerste_zin

        tekst = "De plicht staat in WVV art. 3:22 e.v. Vrijstellingen staan elders."
        resultaat = _eerste_zin(tekst, 120)
        assert "WVV art. 3:22" in resultaat

    def test_gebaseerd_op_concepten_geen_trailing_separator(self) -> None:
        """Lijst van concepten in competentie-fiche eindigt zonder dangling ` · `."""
        from tools.leermateriaal.render_competentie_fiche import render_competentie

        competentie = {
            "id": "test", "titel": "T", "status": "voorgesteld",
            "schema_version": "1.1", "programmaonderdelen": ["1.4"],
            "voortkomend_uit": {"taken": [], "kenniselementen": []},
            "gebaseerd_op_concepten": ["concept-a", "concept-b", "concept-c"],
            "procedure_grondslag": {"wettelijk_pct": 80, "praktijk_pct": 20, "motivering": "T"},
            "stappen": [{"nr": 1, "titel": "S", "grondslag": "[[a]]"}],
        }
        md = render_competentie(competentie)
        # Laatste wikilink mag niet gevolgd worden door ` · ` voor newline
        assert "[[concept-c]] · " not in md, "trailing separator detected"
        assert "[[concept-c]]" in md

    def test_geen_beslisboom_in_competentie(self) -> None:
        """Beslisboom-blok wordt NIET gerenderd in competentie-fiche (ADR-010 §C.1)."""
        from tools.leermateriaal.render_competentie_fiche import render_competentie

        competentie = {
            "id": "test", "titel": "T", "status": "voorgesteld",
            "schema_version": "1.1", "programmaonderdelen": ["1.4"],
            "voortkomend_uit": {"taken": [], "kenniselementen": []},
            "gebaseerd_op_concepten": ["a", "b"],
            "procedure_grondslag": {"wettelijk_pct": 80, "praktijk_pct": 20, "motivering": "T"},
            "stappen": [{"nr": 1, "titel": "S", "grondslag": "[[a]]"}],
            "beslisboom": [
                {"vraag": "Is er controle?", "ja": "Integrale consolidatie.", "nee": "Nee."}
            ],
        }
        md = render_competentie(competentie)
        assert "Is er controle?" not in md  # beslisboom niet gerenderd


# ─── Tests: CLI --help ─────────────────────────────────────────────────────────


class TestCliHelp:
    @pytest.mark.parametrize("module", [
        "tools.leermateriaal.render_concept_fiche",
        "tools.leermateriaal.render_competentie_fiche",
        "tools.leermateriaal.render_minicursus",
        "tools.leermateriaal.propose_competenties",
        "tools.leermateriaal.propose_leerpad",
    ])
    def test_help_werkt(self, module: str) -> None:
        result = subprocess.run(
            [sys.executable, "-m", module, "--help"],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        assert result.returncode == 0
        assert "usage" in result.stdout.lower() or "gebruik" in result.stdout.lower()
