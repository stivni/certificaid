"""Bulk-schema-validatie voor alle interpretaties onder _interpretaties/.

Itereert over elk `_interpretaties/<examen>/<vraag-id>.json`-bestand en past
dezelfde schema-checks toe als `test_interpretatie_schema.py` doet voor de
POC-subset. Voegt ook een **parity-check** toe: elke segment-map moet een
bijhorende interpretatie hebben (anders is de uitrol incompleet).

Discipline-tests die deze module afdwingt:
- Alle interpretaties zijn schema-versie 1.1
- Verplichte velden aanwezig (top + per deelvraag)
- Enum-waardes correct (vraag_herkomst, vraagtype, volledigheid)
- Coupling met segment-meta (examen_id, vraag_id)
- Vraagtype-specifieke regels (mc_keuze heeft opties, topic_only mist vraagstelling)
- Parity: elke segment-map heeft een interpretatie
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
EXAMEN_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen"
SEGMENTEN_DIR = EXAMEN_DIR / "_segmenten"
INTERP_DIR = EXAMEN_DIR / "_interpretaties"

SCHEMA_VERSIE_EXPECTED = "1.2"
VALID_HERKOMST = {"officieel", "herinnering", "hybride"}
VALID_VRAAGTYPE = {"open", "mc_keuze", "juist_fout", "onbekend"}
VALID_VOLLEDIGHEID = {"volledig", "fragment", "topic_only"}
VALID_CONTEXT_BLOK_TYPES = {
    "casus_context", "bijlage_verwijzing",
    "tabel", "gegevens_tabel", "balans", "resultatenrekening",
    "proef_saldibalans", "rekeningstaat", "inventaris", "groepsschema",
    "marktwaarde", "aanpassing", "formule",
    "figuur", "tekst",
}
VERPLICHTE_TOP_VELDEN = {
    "schema_versie", "examen_id", "vraag_id", "interpretatie_datum",
    "vraag_herkomst", "vraag_onderwerp", "themas",
    "context_blokken", "vragen",
    "herinterpretatie_motivering", "kwaliteits_flags",
    "programmaonderdeel_ids",
}

VALID_PO_CODES = {
    "1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9",
    "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8",
    "3.0", "4.0",
}
VERPLICHTE_VRAAG_VELDEN = {
    "id", "vraagtype", "motivatie_verwacht", "volledigheid",
}


def _alle_interpretaties() -> list[Path]:
    if not INTERP_DIR.exists():
        return []
    return sorted(INTERP_DIR.rglob("*.json"))


def _alle_segmenten_ids() -> list[tuple[str, str]]:
    """Return list of (examen_id, vraag_id) for elke segment-map."""
    if not SEGMENTEN_DIR.exists():
        return []
    paren: list[tuple[str, str]] = []
    for examen_dir in sorted(SEGMENTEN_DIR.iterdir()):
        if not examen_dir.is_dir():
            continue
        for vraag_dir in sorted(examen_dir.iterdir()):
            if not vraag_dir.is_dir():
                continue
            paren.append((examen_dir.name, vraag_dir.name))
    return paren


def _id_for(p: Path) -> str:
    """vraag_id uit filename (zonder .json)."""
    return p.stem


# ---------------------------------------------------------------------------
# Per-bestand tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_parseert_als_json(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(data, dict)


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_schema_versie(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data.get("schema_versie") == SCHEMA_VERSIE_EXPECTED


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_verplichte_top_velden(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    missing = VERPLICHTE_TOP_VELDEN - set(data.keys())
    assert not missing, f"{path.stem}: ontbrekende velden {missing}"


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_velden_match_pad(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    examen_id_van_pad = path.parent.name
    vraag_id_van_pad = path.stem
    assert data["examen_id"] == examen_id_van_pad
    assert data["vraag_id"] == vraag_id_van_pad


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_herkomst_enum(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["vraag_herkomst"] in VALID_HERKOMST


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_themas_strings(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    themas = data["themas"]
    assert isinstance(themas, list)
    for t in themas:
        assert isinstance(t, str) and t.strip(), (
            f"{path.stem}: thema leeg of niet-string: {t!r}"
        )


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_context_blok_types_geldig(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    for blok in data["context_blokken"]:
        assert "type" in blok, f"{path.stem}: context-blok zonder type"
        assert blok["type"] in VALID_CONTEXT_BLOK_TYPES, (
            f"{path.stem}: onbekend context-blok-type {blok['type']!r}"
        )


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_balans_actief_passief(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    for blok in data["context_blokken"]:
        if blok.get("type") != "balans":
            continue
        for sub in ("actief", "passief"):
            assert sub in blok, f"{path.stem}: balans mist {sub}"
            assert isinstance(blok[sub], dict)
            assert "headers" in blok[sub] and isinstance(blok[sub]["headers"], list)
            assert "rows" in blok[sub] and isinstance(blok[sub]["rows"], list)


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_gegevens_tabel(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    for blok in data["context_blokken"]:
        if blok.get("type") != "gegevens_tabel":
            continue
        assert "titel" in blok and isinstance(blok["titel"], str)
        assert "rijen" in blok and isinstance(blok["rijen"], list) and blok["rijen"]
        for r in blok["rijen"]:
            assert "label" in r and isinstance(r["label"], str)
            # bedrag is optioneel (mag None zijn voor niet-numerieke rijen
            # zoals datum-markers, attribute-opsommingen). Indien aanwezig
            # en niet-null, moet het numeriek zijn.
            bedrag = r.get("bedrag")
            if bedrag is not None:
                assert isinstance(bedrag, (int, float)), (
                    f"{path.stem}: gegevens_tabel rij 'bedrag' niet-numeriek: {bedrag!r}"
                )


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_vragen_niet_leeg(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    vragen = data["vragen"]
    assert isinstance(vragen, list) and vragen, f"{path.stem}: vragen[] leeg"


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_vragen_verplichte_velden(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    for v in data["vragen"]:
        missing = VERPLICHTE_VRAAG_VELDEN - set(v.keys())
        assert not missing, (
            f"{path.stem} deelvraag {v.get('id', '?')}: ontbreekt {missing}"
        )


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_vragen_enums(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    for v in data["vragen"]:
        assert v["vraagtype"] in VALID_VRAAGTYPE, (
            f"{path.stem} deelvraag {v['id']}: ongeldig vraagtype {v['vraagtype']!r}"
        )
        assert v["volledigheid"] in VALID_VOLLEDIGHEID
        assert isinstance(v["motivatie_verwacht"], bool)


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_vragen_ids_uniek(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    ids = [v["id"] for v in data["vragen"]]
    assert len(ids) == len(set(ids)), f"{path.stem}: duplicate vragen-ids {ids}"


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_mc_keuze_heeft_opties(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    for v in data["vragen"]:
        if v["vraagtype"] != "mc_keuze":
            continue
        opties = v.get("opties")
        assert isinstance(opties, list) and len(opties) >= 2, (
            f"{path.stem} deelvraag {v['id']}: mc_keuze zonder >=2 opties"
        )
        opt_ids = [o["id"] for o in opties]
        assert len(opt_ids) == len(set(opt_ids)), (
            f"{path.stem} deelvraag {v['id']}: duplicate optie-ids"
        )
        for o in opties:
            assert "id" in o and "tekst" in o


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_topic_only_consistent(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    for v in data["vragen"]:
        if v["volledigheid"] != "topic_only":
            continue
        assert v.get("vraagstelling") in (None, ""), (
            f"{path.stem} deelvraag {v['id']}: topic_only met vraagstelling"
        )
        onderwerp = v.get("topic_only_onderwerp")
        assert isinstance(onderwerp, str) and onderwerp.strip(), (
            f"{path.stem} deelvraag {v['id']}: topic_only zonder onderwerp"
        )


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_volledig_of_fragment_heeft_vraagstelling(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    for v in data["vragen"]:
        if v["volledigheid"] not in ("volledig", "fragment"):
            continue
        vs = v.get("vraagstelling")
        assert isinstance(vs, str) and vs.strip(), (
            f"{path.stem} deelvraag {v['id']}: {v['volledigheid']} zonder vraagstelling"
        )


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_programmaonderdeel_ids(path):
    """programmaonderdeel_ids: 1 of 2 entries, allemaal geldige PO-codes."""
    data = json.loads(path.read_text(encoding="utf-8"))
    po_ids = data["programmaonderdeel_ids"]
    assert isinstance(po_ids, list)
    assert 1 <= len(po_ids) <= 2, (
        f"{path.stem}: programmaonderdeel_ids moet 1-2 entries hebben, kreeg {len(po_ids)}"
    )
    for code in po_ids:
        assert code in VALID_PO_CODES, (
            f"{path.stem}: ongeldige PO-code {code!r}"
        )
    assert len(po_ids) == len(set(po_ids)), (
        f"{path.stem}: duplicate PO-codes in {po_ids}"
    )


@pytest.mark.parametrize("path", _alle_interpretaties(), ids=_id_for)
def test_motivering_niet_leeg(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    motivering = data.get("herinterpretatie_motivering", "")
    assert isinstance(motivering, str) and len(motivering.strip()) > 10


# ---------------------------------------------------------------------------
# Parity-check tussen segmenten en interpretaties
# ---------------------------------------------------------------------------

def test_alle_segmenten_hebben_interpretatie():
    """Voor elke segment-map moet een interpretatie-file bestaan."""
    ontbrekend: list[str] = []
    for examen_id, vraag_id in _alle_segmenten_ids():
        verwacht = INTERP_DIR / examen_id / f"{vraag_id}.json"
        if not verwacht.exists():
            ontbrekend.append(f"{examen_id}/{vraag_id}")
    assert not ontbrekend, (
        f"Ontbrekende interpretaties ({len(ontbrekend)}): {ontbrekend[:10]}..."
        if len(ontbrekend) > 10 else f"Ontbrekende interpretaties: {ontbrekend}"
    )


def test_interpretaties_corresponderen_met_segmenten():
    """Elke interpretatie heeft een segment-map (geen weeskinderen)."""
    segment_paren = set(_alle_segmenten_ids())
    weeskinderen: list[str] = []
    for path in _alle_interpretaties():
        examen_id = path.parent.name
        vraag_id = path.stem
        if (examen_id, vraag_id) not in segment_paren:
            weeskinderen.append(f"{examen_id}/{vraag_id}")
    assert not weeskinderen, f"Wees-interpretaties zonder segment: {weeskinderen}"
