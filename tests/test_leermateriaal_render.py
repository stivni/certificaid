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


# ─── Tests: migratie-script ────────────────────────────────────────────────────


class TestMigratieDryRun:
    def test_migratie_dry_run_werkt(self) -> None:
        """Test dat het migratie-script --dry-run draait zonder te crashen."""
        result = subprocess.run(
            [sys.executable, "-m", "tools.extractie.migrate_bron_voorstellen", "--dry-run"],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        # Mag niet crashen (exit code 0 of 0 bij "niets te migreren")
        assert result.returncode == 0 or "niet gevonden" in result.stdout


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
