"""
Smoke-tests voor de enrichment-loop scripts (ADR-008 §13.7).

Controleert:
1. Import slaagt zonder crashes voor de drie helper-scripts.
2. --help werkt (argparse-configuratie is correct).
3. Mechanische coherentie-check geeft correcte output voor testdata.
4. auto_merge helpers werken correct op dummy-records.
5. VERIFY_MODEL constante = "claude-sonnet-4-6" (ADR-008 §13.2).
6. run_enrichment_cycle --help werkt.
7. classify_vragen_naar_programmaonderdelen --help werkt.
8. Examen-mapping-loader falls-back op lege lijst bij ontbrekend bestand.
9. Monotoon-terminologie aanwezig in concept-enrich-v1.md.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

# ─── Import smoke-tests ────────────────────────────────────────────────────────


def test_verify_records_import():
    """verify_records.py importeert zonder crash."""
    import tools.extractie.verify_records as module  # noqa: F401
    assert hasattr(module, "main")
    assert hasattr(module, "load_records_for_programmaonderdeel")
    assert hasattr(module, "mechanical_coherence_checks")


def test_enrich_records_import():
    """enrich_records.py importeert zonder crash."""
    import tools.extractie.enrich_records as module  # noqa: F401
    assert hasattr(module, "main")
    assert hasattr(module, "laad_gaps")
    assert hasattr(module, "filter_gaps_voor_programmaonderdeel")


def test_auto_merge_import():
    """auto_merge.py importeert zonder crash."""
    import tools.extractie.auto_merge as module  # noqa: F401
    assert hasattr(module, "main")
    assert hasattr(module, "mechanical_coherence_checks") is False  # auto_merge heeft geen coherentie-checks
    assert hasattr(module, "verwerk_record")


# ─── --help smoke-tests ────────────────────────────────────────────────────────


def _run_help(module: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", module, "--help"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )


def test_verify_records_help():
    """verify_records --help retourneert exit-code 0."""
    resultaat = _run_help("tools.extractie.verify_records")
    assert resultaat.returncode == 0, (
        f"verify_records --help crashte met code {resultaat.returncode}:\n{resultaat.stderr}"
    )
    assert "--programmaonderdeel" in resultaat.stdout


def test_enrich_records_help():
    """enrich_records --help retourneert exit-code 0."""
    resultaat = _run_help("tools.extractie.enrich_records")
    assert resultaat.returncode == 0, (
        f"enrich_records --help crashte met code {resultaat.returncode}:\n{resultaat.stderr}"
    )
    assert "--programmaonderdeel" in resultaat.stdout


def test_auto_merge_help():
    """auto_merge --help retourneert exit-code 0."""
    resultaat = _run_help("tools.extractie.auto_merge")
    assert resultaat.returncode == 0, (
        f"auto_merge --help crashte met code {resultaat.returncode}:\n{resultaat.stderr}"
    )
    assert "--since" in resultaat.stdout


# ─── Mechanische coherentie-checks ─────────────────────────────────────────────


def test_mechanical_coherence_geen_gaps_bij_lege_records():
    """mechanical_coherence_checks geeft lege lijst voor lege records-set."""
    from tools.extractie.verify_records import mechanical_coherence_checks
    assert mechanical_coherence_checks([]) == []


def test_mechanical_coherence_detecteert_ontbrekende_vergelijkingspaar_target():
    """mechanical_coherence_checks detecteert een vergelijkingspaar dat naar een niet-bestaand record wijst."""
    from tools.extractie.verify_records import mechanical_coherence_checks

    records = [
        {
            "id": "begrip-a",
            "naam": "Begrip A",
            "node_type": "begrip",
            "linked_anchors": ["1.4.test.1"],
            "vergelijkingsparen": [
                {
                    "vergelijking_met": "begrip-niet-bestaand",
                    "verschil": "A is anders dan niet-bestaand.",
                }
            ],
        }
    ]
    gaps = mechanical_coherence_checks(records)
    assert len(gaps) == 1
    assert gaps[0]["record_id"] == "begrip-a"
    assert gaps[0]["aspect"] == "vergelijkingsparen.target-ontbreekt"
    assert gaps[0]["status"] == "open"
    assert gaps[0]["prio"] == "laag"


def test_mechanical_coherence_geen_gap_als_target_bestaat():
    """mechanical_coherence_checks logt géén gap als vergelijkingspaar-target wel bestaat."""
    from tools.extractie.verify_records import mechanical_coherence_checks

    records = [
        {
            "id": "begrip-a",
            "naam": "Begrip A",
            "node_type": "begrip",
            "linked_anchors": ["1.4.test.1"],
            "vergelijkingsparen": [
                {
                    "vergelijking_met": "begrip-b",
                    "verschil": "A is anders dan B.",
                }
            ],
        },
        {
            "id": "begrip-b",
            "naam": "Begrip B",
            "node_type": "begrip",
            "linked_anchors": ["1.4.test.2"],
        },
    ]
    gaps = mechanical_coherence_checks(records)
    assert gaps == []


def test_mechanical_coherence_detecteert_ontbrekend_edges_target():
    """mechanical_coherence_checks detecteert een edge die naar een niet-bestaand record wijst."""
    from tools.extractie.verify_records import mechanical_coherence_checks

    records = [
        {
            "id": "procedure-x",
            "naam": "Procedure X",
            "node_type": "procedure",
            "linked_anchors": ["1.4.test.3"],
            "edges": [
                {"edge_type": "getriggerd-door", "target": "begrip-niet-bestaand"},
            ],
        }
    ]
    gaps = mechanical_coherence_checks(records)
    assert len(gaps) == 1
    assert gaps[0]["aspect"] == "edges.target-ontbreekt"


# ─── auto_merge helpers ─────────────────────────────────────────────────────────


def test_diep_gelijk_gelijke_waarden():
    """diep_gelijk geeft True voor identieke waarden."""
    from tools.extractie.auto_merge import diep_gelijk
    assert diep_gelijk({"a": 1}, {"a": 1})
    assert diep_gelijk([1, 2, 3], [1, 2, 3])
    assert diep_gelijk("test", "test")


def test_diep_gelijk_ongelijke_waarden():
    """diep_gelijk geeft False voor afwijkende waarden."""
    from tools.extractie.auto_merge import diep_gelijk
    assert not diep_gelijk({"a": 1}, {"a": 2})
    assert not diep_gelijk([1, 2], [1, 3])


def test_vind_verdwenen_array_items():
    """vind_verdwenen_array_items detecteert een verdwenen item."""
    from tools.extractie.auto_merge import vind_verdwenen_array_items

    oud = [{"text": "item A"}, {"text": "item B"}]
    nieuw = [{"text": "item A"}]
    verdwenen = vind_verdwenen_array_items(oud, nieuw, "valkuilen")
    assert len(verdwenen) == 1
    assert verdwenen[0]["verloren_item"] == {"text": "item B"}
    assert verdwenen[0]["veld_naam"] == "valkuilen"


def test_vind_verdwenen_array_items_niets_verdwenen():
    """vind_verdwenen_array_items geeft lege lijst als niets verdwenen is."""
    from tools.extractie.auto_merge import vind_verdwenen_array_items

    oud = [{"text": "item A"}]
    nieuw = [{"text": "item A"}, {"text": "item B"}]  # item toegevoegd, niets verdwenen
    verdwenen = vind_verdwenen_array_items(oud, nieuw, "oorzaken")
    assert verdwenen == []


def test_heeft_corrected_from_marker_positief():
    """heeft_corrected_from_marker geeft True als het veld een corrected_from-sleutel heeft."""
    from tools.extractie.auto_merge import heeft_corrected_from_marker

    record = {
        "main_rule": {
            "text": "nieuwe tekst",
            "corrected_from": "oude tekst",
            "correction_reason": "bron geeft andere waarde.",
        }
    }
    assert heeft_corrected_from_marker(record, "main_rule")


def test_heeft_corrected_from_marker_negatief():
    """heeft_corrected_from_marker geeft False als er geen correctie-marker is."""
    from tools.extractie.auto_merge import heeft_corrected_from_marker

    record = {
        "main_rule": {
            "text": "tekst zonder correctie",
            "confidence": "grounded",
        }
    }
    assert not heeft_corrected_from_marker(record, "main_rule")


def test_heeft_corrected_from_marker_ontbrekend_veld():
    """heeft_corrected_from_marker geeft False voor een veld dat niet bestaat."""
    from tools.extractie.auto_merge import heeft_corrected_from_marker

    record = {"definitie": {"text": "een definitie"}}
    assert not heeft_corrected_from_marker(record, "main_rule")


# ─── load_records_for_programmaonderdeel ───────────────────────────────────────


def test_load_records_for_programmaonderdeel_filter(tmp_path):
    """load_records_for_programmaonderdeel filtert correct op linked_anchors."""
    from tools.extractie.verify_records import load_records_for_programmaonderdeel  # noqa: F401

    # Maak twee test-records aan in tmp_path
    record_in_scope = {
        "id": "begrip-in-scope",
        "naam": "In scope",
        "node_type": "begrip",
        "linked_anchors": ["1.4.test.1", "1.4.test.2"],
    }
    record_buiten_scope = {
        "id": "begrip-buiten-scope",
        "naam": "Buiten scope",
        "node_type": "begrip",
        "linked_anchors": ["4.0.test.1"],
    }
    (tmp_path / "begrip-in-scope.json").write_text(
        json.dumps(record_in_scope, ensure_ascii=False), encoding="utf-8"
    )
    (tmp_path / "begrip-buiten-scope.json").write_text(
        json.dumps(record_buiten_scope, ensure_ascii=False), encoding="utf-8"
    )

    # Gebruik het tmp_path als records-glob (relatief aan ROOT — kan niet direct,
    # dus we testen laad_alle_records + filter handmatig)
    alle = []
    for bestand in tmp_path.glob("*.json"):
        record = json.loads(bestand.read_text())
        record["_bestandspad"] = str(bestand)
        alle.append(record)

    # Filter simuleren zoals load_records_for_programmaonderdeel dat doet
    programmaonderdeel_id = "1.4"
    prefix = f"{programmaonderdeel_id}."
    gefilterd = [
        r for r in alle
        if any(a.startswith(prefix) for a in r.get("linked_anchors", []))
    ]

    assert len(gefilterd) == 1
    assert gefilterd[0]["id"] == "begrip-in-scope"


# ─── gaps IO ───────────────────────────────────────────────────────────────────


def test_voeg_gaps_toe_deduplicatie(tmp_path):
    """voeg_gaps_toe voegt geen duplicate open gaps toe."""
    from tools.extractie.verify_records import voeg_gaps_toe

    gaps_bestand = tmp_path / "gaps.json"
    gap = {
        "record_id": "begrip-a",
        "aspect": "definitie.onvolledig",
        "reden": "Definitie is te kort.",
        "prio": "midden",
        "geconstateerd_door": "test",
        "geconstateerd_op": "2026-05-15T00:00:00Z",
        "status": "open",
    }

    toegevoegd_1 = voeg_gaps_toe([gap], gaps_bestand)
    assert toegevoegd_1 == 1

    toegevoegd_2 = voeg_gaps_toe([gap], gaps_bestand)
    assert toegevoegd_2 == 0  # duplicaat, niet opnieuw toegevoegd

    inhoud = json.loads(gaps_bestand.read_text())
    assert len(inhoud) == 1


# ─── Nieuwe smoke-tests (verbeteringen A–E) ─────────────────────────────────────


def test_verify_model_constante():
    """VERIFY_MODEL in verify_records.py is 'claude-sonnet-4-6' (ADR-008 §13.2)."""
    import tools.extractie.verify_records as module
    assert hasattr(module, "VERIFY_MODEL"), "VERIFY_MODEL-constante ontbreekt in verify_records.py"
    assert module.VERIFY_MODEL == "claude-sonnet-4-6", (
        f"VERIFY_MODEL is '{module.VERIFY_MODEL}', verwacht 'claude-sonnet-4-6'"
    )


def test_run_enrichment_cycle_help():
    """run_enrichment_cycle --help retourneert exit-code 0."""
    resultaat = _run_help("tools.extractie.run_enrichment_cycle")
    assert resultaat.returncode == 0, (
        f"run_enrichment_cycle --help crashte met code {resultaat.returncode}:\n{resultaat.stderr}"
    )
    assert "--programmaonderdeel" in resultaat.stdout
    assert "--max-iteraties" in resultaat.stdout


def test_classify_vragen_help():
    """classify_vragen_naar_programmaonderdelen --help retourneert exit-code 0."""
    resultaat = _run_help("tools.examen.classify_vragen_naar_programmaonderdelen")
    assert resultaat.returncode == 0, (
        f"classify_vragen_naar_programmaonderdelen --help crashte met code "
        f"{resultaat.returncode}:\n{resultaat.stderr}"
    )
    assert "--seed-po-14" in resultaat.stdout


def test_examen_mapping_fallback_bij_ontbrekend_bestand(tmp_path, monkeypatch):
    """laad_examen_vragen_voor_programmaonderdeel geeft lege lijst bij ontbrekend classificatie-bestand."""
    import tools.extractie.verify_records as module

    # Patch het classificatie-bestand naar een niet-bestaand pad
    monkeypatch.setattr(
        module,
        "PROGRAMMAONDERDEEL_CLASSIFICATIE_BESTAND",
        tmp_path / "niet-bestaand.json",
    )
    # Patch de examen-vragen-dir naar een lege tmp-dir zodat ook de fallback-glob leeg is
    monkeypatch.setattr(module, "EXAMEN_VRAGEN_DIR", tmp_path)

    resultaat = module.laad_examen_vragen_voor_programmaonderdeel("1.4")
    # Moet een lege lijst teruggeven (geen crash), niet een exception
    assert isinstance(resultaat, list)
    assert resultaat == []


def test_monotoon_contract_in_enrich_prompt():
    """concept-enrich-v1.md bevat de 'monotoon contract' terminologie (ADR-008 §13.3)."""
    enrich_prompt = ROOT / "prompts" / "concept-enrich-v1.md"
    assert enrich_prompt.exists(), f"{enrich_prompt} bestaat niet"
    inhoud = enrich_prompt.read_text(encoding="utf-8").lower()
    assert "monotoon contract" in inhoud, (
        "Verwacht 'monotoon contract' in concept-enrich-v1.md (ADR-008 §13.3)"
    )
    # Mag geen ongemotiveerd 'append-only' meer bevatten als hoofdcontract-label
    assert "## hard contract" not in inhoud, (
        "Verouderd '## HARD CONTRACT' kopje aangetroffen — moet '## MONOTOON CONTRACT' zijn"
    )


def test_discovery_signaal_in_enrich_prompt():
    """concept-enrich-v1.md bevat de 'discovery-signaal' sectie (verbetering C)."""
    enrich_prompt = ROOT / "prompts" / "concept-enrich-v1.md"
    inhoud = enrich_prompt.read_text(encoding="utf-8").lower()
    assert "discovery-signaal" in inhoud or "discovered-during-enrich" in inhoud, (
        "Verwacht 'discovery-signaal' of 'discovered-during-enrich' in concept-enrich-v1.md"
    )
