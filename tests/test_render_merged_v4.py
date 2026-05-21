"""Tests voor render_merged_v4.py — schema 4.0 → Quartz-markdown.

TDD-volgorde: schrijf eerst, run rood, dan implementatie.

Gedekt:
- Per examen: content/voorbeeldexamens/<examen>.md bestaat na render
- index.md bestaat met links naar alle 7 examen-pagina's
- Vraag-eenheid: H2 anchor, vraag_onderwerp, themas
- Deelvraag: vraagstelling (skip bij topic_only), mc-opties, warning bij topic_only,
  success-callout (collapsed) voor antwoord
- Antwoord-callout-content: beantwoord / wacht_op_vraag_generatie / hard_blocked /
  antwoord=null
- Parametrized over alle 7 _merged/-files
- Idempotentie: tweede run wijzigt mtime niet
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path

import pytest

# --- Paden -----------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
MERGED_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_merged"
OUTPUT_DIR = REPO_ROOT / "content" / "voorbeeldexamens"

# Alle 7 examen-bestanden
EXAMEN_IDS = sorted(
    p.stem for p in MERGED_DIR.glob("*.json")
)

# ---------------------------------------------------------------------------
# Helpers voor importeren van de module (die nog niet bestaat bij rood-run)
# ---------------------------------------------------------------------------


def _laad_module():
    """Importeer render_merged_v4; geeft ModuleNotFoundError als niet gebouwd."""
    from tools.examen import render_merged_v4  # noqa: PLC0415

    return render_merged_v4


# ---------------------------------------------------------------------------
# Fixture: render alle examens (eenmalig per testsessie)
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def gerenderd():
    """Render alle examens en geef de module terug. Skip als module ontbreekt."""
    mod = _laad_module()
    mod.render_alle()
    return mod


# ---------------------------------------------------------------------------
# Test 1: elk examen levert een .md bestand op
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("examen_id", EXAMEN_IDS)
def test_output_bestand_bestaat(gerenderd, examen_id):
    """Na render bestaat content/voorbeeldexamens/<examen>.md."""
    pad = OUTPUT_DIR / f"{examen_id}.md"
    assert pad.exists(), f"Verwacht {pad} maar het bestaat niet"
    assert pad.stat().st_size > 0, f"{pad} is leeg"


# ---------------------------------------------------------------------------
# Test 2: index.md bestaat en bevat links naar alle examens
# ---------------------------------------------------------------------------


def test_index_bestaat(gerenderd):
    """content/voorbeeldexamens/index.md bestaat."""
    assert (OUTPUT_DIR / "index.md").exists()


def test_index_bevat_links_naar_alle_examens(gerenderd):
    """index.md bevat een link naar elk van de 7 examen-pagina's."""
    inhoud = (OUTPUT_DIR / "index.md").read_text(encoding="utf-8")
    for examen_id in EXAMEN_IDS:
        assert examen_id in inhoud, f"index.md mist link naar {examen_id}"


def test_index_bevat_tabel(gerenderd):
    """index.md bevat een markdown-tabel."""
    inhoud = (OUTPUT_DIR / "index.md").read_text(encoding="utf-8")
    # Markdown-tabel: ten minste een header-scheidingsregel
    assert "|---" in inhoud or "| ---" in inhoud, "index.md mist markdown-tabel"


# ---------------------------------------------------------------------------
# Test 3: vraag-eenheid structuur (H2 anchor, onderwerp, themas)
# ---------------------------------------------------------------------------


def test_h2_anchor_per_vraag(gerenderd):
    """Elke vraag-eenheid heeft een H2-heading met het vraag_id."""
    data = json.loads((MERGED_DIR / "2024-1.json").read_text())
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    for vraag in data["vragen"]:
        vraag_id = vraag["vraag_id"]
        assert f"## {vraag_id}" in inhoud, f"H2 anchor voor {vraag_id} ontbreekt"


def test_vraag_onderwerp_aanwezig(gerenderd):
    """vraag_onderwerp is zichtbaar in de render."""
    data = json.loads((MERGED_DIR / "2024-1.json").read_text())
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    for vraag in data["vragen"]:
        onderwerp = vraag["interpretatie"]["vraag_onderwerp"]
        assert onderwerp in inhoud, f"Onderwerp '{onderwerp}' ontbreekt in render"


def test_themas_tags_aanwezig(gerenderd):
    """themas zijn zichtbaar in de render (als tags of inline)."""
    data = json.loads((MERGED_DIR / "2024-1.json").read_text())
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    for vraag in data["vragen"]:
        themas = vraag["interpretatie"].get("themas", [])
        for thema in themas[:2]:  # check eerste 2 themas
            assert thema in inhoud, f"Thema '{thema}' ontbreekt in render"


# ---------------------------------------------------------------------------
# Test 4: deelvraag-structuur
# ---------------------------------------------------------------------------


def test_vraagstelling_aanwezig_bij_volledig(gerenderd):
    """Vraagstelling is aanwezig voor deelvragen met volledigheid != topic_only."""
    data = json.loads((MERGED_DIR / "2024-1.json").read_text())
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    for vraag in data["vragen"]:
        for deelvraag in vraag["interpretatie"]["vragen"]:
            if deelvraag.get("volledigheid") != "topic_only":
                vraagstelling = deelvraag.get("vraagstelling") or ""
                if vraagstelling.strip():
                    # Check dat minstens een deel van de vraagstelling zichtbaar is
                    fragment = vraagstelling[:30].strip()
                    assert fragment in inhoud, (
                        f"Vraagstelling fragment '{fragment}' ontbreekt voor "
                        f"deelvraag {deelvraag['id']}"
                    )


def test_mc_opties_aanwezig(gerenderd):
    """MC-opties worden gerenderd als bullet-lijst."""
    data = json.loads((MERGED_DIR / "2024-1.json").read_text())
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    for vraag in data["vragen"]:
        for deelvraag in vraag["interpretatie"]["vragen"]:
            if deelvraag.get("vraagtype") == "mc_keuze":
                opties = deelvraag.get("opties", [])
                for optie in opties[:2]:
                    # Formaat: - **{id}**: {tekst}
                    optie_id = optie["id"]
                    assert f"**{optie_id}**" in inhoud, (
                        f"MC-optie {optie_id} ontbreekt in render"
                    )


def test_topic_only_warning_callout(gerenderd):
    """Bij topic_only deelvraag: warning callout aanwezig."""
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    # vr10 sub-a is topic_only
    assert "[!warning]" in inhoud, "Geen warning callout gevonden (topic_only)"
    assert "Topic only" in inhoud or "topic_only" in inhoud.lower(), (
        "Warning callout bevat geen topic-only aanduiding"
    )


def test_geen_vraagstelling_bij_topic_only(gerenderd):
    """Bij topic_only deelvraag wordt geen lege vraagstelling gerenderd."""
    data = json.loads((MERGED_DIR / "2024-1.json").read_text())
    # vr10-a is topic_only met vraagstelling=null
    vr10 = next(v for v in data["vragen"] if v["vraag_id"] == "2024-1-vr10")
    deelvraag_a = next(d for d in vr10["interpretatie"]["vragen"] if d["id"] == "a")
    assert deelvraag_a["volledigheid"] == "topic_only"
    assert deelvraag_a["vraagstelling"] is None
    # Geen "None" of leeg placeholder in de output
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    # Er mag geen letterlijke "None" paragraaf zijn
    assert "\nNone\n" not in inhoud


# ---------------------------------------------------------------------------
# Test 5: antwoord-callout aanwezig (success collapsed)
# ---------------------------------------------------------------------------


def test_success_callout_aanwezig_per_deelvraag(gerenderd):
    """Elke deelvraag heeft een success-callout (collapsed)."""
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    # Minimaal 1 collapsed success callout
    assert "[!success]-" in inhoud, "Geen collapsed success callout gevonden"
    assert "Antwoord (klik om te openen)" in inhoud


def test_success_callout_aanwezig_bij_geen_antwoord(gerenderd):
    """Ook bij antwoord=null wordt een success-callout gerenderd (met placeholder)."""
    inhoud = (OUTPUT_DIR / "2013-2.md").read_text(encoding="utf-8")
    assert "[!success]-" in inhoud, "Geen success callout bij examen zonder antwoorden"
    assert "Antwoord wacht op concept-laag" in inhoud, (
        "Placeholder tekst 'Antwoord wacht op concept-laag' ontbreekt"
    )


# ---------------------------------------------------------------------------
# Test 6: antwoord-callout-content per status
# ---------------------------------------------------------------------------


def test_beantwoord_mc_keuze_gekozen_optie(gerenderd):
    """Bij beantwoord mc_keuze staat gekozen_optie_id zichtbaar in callout."""
    # 2024-1-vr1 deelvraag c: mc_keuze, gekozen=c
    data = json.loads((MERGED_DIR / "2024-1.json").read_text())
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    vr1 = next(v for v in data["vragen"] if v["vraag_id"] == "2024-1-vr1")
    ant = vr1["antwoord"]
    for a in ant["vraag_antwoorden"]:
        if a["antwoord_status"] == "beantwoord" and a.get("gekozen_optie_id"):
            gekozen = a["gekozen_optie_id"]
            assert f"Antwoord: {gekozen}" in inhoud, (
                f"Gekozen optie '{gekozen}' niet zichtbaar in antwoord-callout"
            )


def test_beantwoord_open_vraag_blokken(gerenderd):
    """Bij beantwoord open vraag worden typed blokken gerenderd."""
    # 2024-1-vr1 deelvraag a: open, beantwoord, heeft conclusie + grondslag blokken
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    # De conclusie-blok bevat een stuk tekst
    data = json.loads((MERGED_DIR / "2024-1.json").read_text())
    vr1 = next(v for v in data["vragen"] if v["vraag_id"] == "2024-1-vr1")
    ant = vr1["antwoord"]
    deelvraag_a = next(a for a in ant["vraag_antwoorden"] if a["id"] == "a")
    for blok in deelvraag_a.get("blokken", []):
        if blok["type"] == "conclusie":
            fragment = blok["tekst"][:40]
            assert fragment in inhoud, (
                f"Conclusie-blok fragment '{fragment}' ontbreekt in render"
            )


def test_wacht_op_vraag_generatie_placeholder(gerenderd):
    """Bij wacht_op_vraag_generatie staat de juiste placeholder."""
    # 2024-1-vr10 deelvraag a: wacht_op_vraag_generatie
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    assert "Vraag-inhoud niet gereconstrueerd" in inhoud, (
        "Placeholder voor wacht_op_vraag_generatie ontbreekt"
    )


# ---------------------------------------------------------------------------
# Test 7: parametrized over alle 7 bestanden
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("examen_id", EXAMEN_IDS)
def test_output_is_valide_markdown(gerenderd, examen_id):
    """Output is niet leeg en bevat ten minste een H1 en H2."""
    inhoud = (OUTPUT_DIR / f"{examen_id}.md").read_text(encoding="utf-8")
    assert "# " in inhoud, f"{examen_id}.md mist H1 heading"
    assert "## " in inhoud, f"{examen_id}.md mist H2 heading"
    assert "[!success]-" in inhoud, f"{examen_id}.md mist collapsed antwoord-callout"


@pytest.mark.parametrize("examen_id", EXAMEN_IDS)
def test_alle_vraag_ids_aanwezig(gerenderd, examen_id):
    """Alle vraag-ids uit de JSON zijn terug te vinden in de render."""
    data = json.loads((MERGED_DIR / f"{examen_id}.json").read_text())
    inhoud = (OUTPUT_DIR / f"{examen_id}.md").read_text(encoding="utf-8")
    for vraag in data["vragen"]:
        vraag_id = vraag["vraag_id"]
        assert vraag_id in inhoud, (
            f"vraag_id '{vraag_id}' ontbreekt in {examen_id}.md"
        )


# ---------------------------------------------------------------------------
# Test 8: idempotentie
# ---------------------------------------------------------------------------


def test_idempotent_geen_mtime_wijziging(gerenderd, tmp_path):
    """Tweede render-run wijzigt mtime niet als content onveranderd is."""
    mod = _laad_module()

    # Eerste run al gedaan door fixture. Sla mtime op.
    mtimes_voor = {
        p.name: p.stat().st_mtime
        for p in OUTPUT_DIR.glob("*.md")
    }

    # Kleine pauze zodat een echte schrijfactie andere mtime zou geven
    time.sleep(0.05)

    # Tweede run
    mod.render_alle()

    mtimes_na = {
        p.name: p.stat().st_mtime
        for p in OUTPUT_DIR.glob("*.md")
    }

    for naam, mtime_voor in mtimes_voor.items():
        mtime_na = mtimes_na.get(naam)
        assert mtime_na == mtime_voor, (
            f"{naam}: mtime veranderd bij identieke render "
            f"({mtime_voor} → {mtime_na})"
        )


# ---------------------------------------------------------------------------
# Test 9: specifieke render-details
# ---------------------------------------------------------------------------


def test_deelvraag_header_format(gerenderd):
    """Deelvraag-headers gebruiken H3 met label_in_pdf of id."""
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    # Deelvragen staan als H3: "### Vraag A" of "### Vraag a"
    assert "### Vraag " in inhoud, "H3 deelvraag-headers ontbreken"


def test_motivatie_verwacht_hint(gerenderd):
    """Bij motivatie_verwacht=True staat een hint in de render."""
    # vr10-a heeft motivatie_verwacht=true
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    assert "motivering" in inhoud.lower(), (
        "Geen motivering-hint bij deelvraag met motivatie_verwacht=true"
    )


def test_confidence_iconen_aanwezig(gerenderd):
    """Confidence-iconen (⚖️ of 🤖) zijn aanwezig in antwoord-blokken."""
    # 2024-1 heeft antwoorden met confidence=inferred
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    assert "🤖" in inhoud or "⚖️" in inhoud, (
        "Geen confidence-iconen gevonden in antwoord-blokken"
    )


def test_balans_render_twee_subtabellen(gerenderd):
    """Balans-blok rendert als twee genummerde sub-tabellen (Actief / Passief)."""
    # 2013-1 heeft een balans-blok
    inhoud = (OUTPUT_DIR / "2013-1.md").read_text(encoding="utf-8")
    assert "**Balans**" in inhoud, "Balans-kop ontbreekt"
    assert "**Actief**" in inhoud, "Balans Actief-subkop ontbreekt"
    assert "**Passief**" in inhoud, "Balans Passief-subkop ontbreekt"


def test_gegevens_tabel_render(gerenderd):
    """gegevens_tabel rendert als 2-koloms markdown-tabel met titel."""
    # 2013-1 heeft gegevens_tabel blokken
    inhoud = (OUTPUT_DIR / "2013-1.md").read_text(encoding="utf-8")
    # Titel van een gegevens_tabel
    data = json.loads((MERGED_DIR / "2013-1.json").read_text())
    vraag = data["vragen"][0]
    for blok in vraag["interpretatie"].get("context_blokken", []):
        if blok["type"] == "gegevens_tabel":
            titel = blok["titel"]
            assert titel in inhoud, f"gegevens_tabel titel '{titel}' ontbreekt"
            break


def test_boeking_render_als_tabel(gerenderd):
    """boeking-blok rendert als 4-koloms markdown-tabel."""
    # 2003-bibf heeft boeking-blokken in antwoord
    inhoud = (OUTPUT_DIR / "2003-bibf.md").read_text(encoding="utf-8")
    # Boeking-tabel heeft Zijde | Rekening | Naam | Bedrag als headers
    assert "Zijde" in inhoud, "Boeking-tabel header 'Zijde' ontbreekt"
    assert "Rekening" in inhoud, "Boeking-tabel header 'Rekening' ontbreekt"
    assert "Bedrag" in inhoud, "Boeking-tabel header 'Bedrag' ontbreekt"


def test_casus_context_als_blockquote(gerenderd):
    """casus_context rendert als blockquote (begint met '> ')."""
    inhoud = (OUTPUT_DIR / "2024-1.md").read_text(encoding="utf-8")
    # Blockquote: minimaal één regel die begint met "> "
    assert any(
        line.startswith("> ") and not line.startswith("> [!")
        for line in inhoud.splitlines()
    ), "casus_context als blockquote ontbreekt"
