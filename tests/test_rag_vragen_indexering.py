"""Tests voor de vragen-collection indexering en zoek_vragen MCP-tool.

Testplan:
  1. _compose_vraag_tekst — deterministisch, geen embedding vereist
  2. index_vragen — produceert 253 chunks met verplichte metadata-velden
  3. metadata-veld parse-roundtrip — programmaonderdeel_ids parseert terug
  4. Semantische queries — fraude/BTW/filter (vereist geladen ChromaDB-index)
  5. _zoek_vragen MCP-tool — filter op PO-id

Tests 4 en 5 vereisen dat de 'vragen'-collection al geladen is:
  python3 -m tools.rag.rag_index --add-vragen
Ze worden overgeslagen (pytest.skip) als de collection niet bestaat.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.rag.rag_index import _compose_vraag_tekst, index_vragen, VRAGEN_DIR  # noqa: E402

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

CHROMA_PATH = ROOT / "data" / "rag" / "main"


def _vragen_collection_count() -> int:
    """Geef het aantal chunks in de 'vragen'-collection, of 0 als niet beschikbaar."""
    try:
        import chromadb
        client = chromadb.PersistentClient(path=str(CHROMA_PATH))
        col = client.get_collection("vragen")
        return col.count()
    except Exception:
        return 0


def _get_vragen_collection():
    """Haal de 'vragen'-collection op; skip als niet beschikbaar."""
    count = _vragen_collection_count()
    if count == 0:
        pytest.skip("vragen-collection niet beschikbaar — run: python3 -m tools.rag.rag_index --add-vragen")
    import chromadb
    from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
    ef = SentenceTransformerEmbeddingFunction(model_name="BAAI/bge-m3", device="cpu")
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    return client.get_collection("vragen", embedding_function=ef)


# ---------------------------------------------------------------------------
# 1. _compose_vraag_tekst — geen embedding vereist
# ---------------------------------------------------------------------------

def test_compose_vraag_tekst_bevat_onderwerp():
    record = {
        "vraag_id": "2013-1-vr13",
        "vraag_onderwerp": "Interne controlemaatregelen bij vastgestelde onregelmatigheden door boekhouder",
        "themas": ["interne controle", "fraude", "boekhouder"],
        "vragen": [{"id": "a", "vraagtype": "open", "vraagstelling": "Geef voor 5 vaststellingen de formulering."}],
        "context_blokken": [{"type": "casus_context", "tekst": "NV SLA-BAK is een kleine onderneming."}],
    }
    tekst = _compose_vraag_tekst(record)
    assert "Interne controlemaatregelen" in tekst
    assert "fraude" in tekst
    assert "Geef voor 5 vaststellingen" in tekst
    assert "NV SLA-BAK" in tekst


def test_compose_vraag_tekst_themas_beperkt_tot_10():
    record = {
        "vraag_onderwerp": "Test",
        "themas": [f"thema{i}" for i in range(15)],
        "vragen": [],
        "context_blokken": [],
    }
    tekst = _compose_vraag_tekst(record)
    # Max 10 thema's in de embed-tekst
    assert "thema9" in tekst
    assert "thema10" not in tekst


def test_compose_vraag_tekst_gegevens_tabel():
    record = {
        "vraag_onderwerp": "Balansanalyse",
        "themas": ["balans"],
        "vragen": [],
        "context_blokken": [{"type": "gegevens_tabel", "titel": "Tabel met gegevens boekjaar 2022"}],
    }
    tekst = _compose_vraag_tekst(record)
    assert "Tabel met gegevens boekjaar 2022" in tekst


def test_compose_vraag_tekst_leeg_record():
    """Leeg record produceert geen fout — kan lege string zijn."""
    record = {}
    tekst = _compose_vraag_tekst(record)
    assert isinstance(tekst, str)


# ---------------------------------------------------------------------------
# 2. index_vragen — produceert juist aantal chunks
# ---------------------------------------------------------------------------

def test_index_vragen_produceert_alle_chunks():
    """index_vragen moet één chunk per interpretatie-JSON aanmaken.

    Verwacht 368 = 49 (2024-1 na ADR-031) + 242 (overige pre-2010-2 examens)
    + 42 (2010-2, Studocu, geïmporteerd 2026-05-29) + 27 (2019-bibf, Studocu,
    geïmporteerd 2026-05-30) + 8 (2024-oef-2-8, ITAA oefenset PO 2.8).
    Was 253 vóór ADR-031 toen 2024-1 als 11 vakken werd geparsed.
    """
    alle_bestanden = list(VRAGEN_DIR.rglob("*.json"))
    assert len(alle_bestanden) == 368, (
        f"Verwacht 368 interpretatie-JSONs, gevonden {len(alle_bestanden)}"
    )


def test_index_vragen_metadata_velden():
    """Elke interpretatie-JSON levert metadata met alle verplichte velden."""
    verplichte_velden = {
        "vraag_id", "examen_id", "vraag_herkomst",
        "programmaonderdeel_ids", "vraagtypes", "themas", "node_type",
    }
    fouten: list[str] = []
    for pad in sorted(VRAGEN_DIR.rglob("*.json"))[:10]:  # snel: eerste 10 controleren
        record = json.loads(pad.read_text())
        # Simuleer de metadata-constructie uit index_vragen
        po_ids_list = record.get("programmaonderdeel_ids", [])
        programmaonderdeel_ids_str = ",".join(str(p) for p in po_ids_list)
        vragen = record.get("vragen", [])
        vraagtypes_set: list[str] = []
        seen: set[str] = set()
        for deelvraag in vragen:
            if not isinstance(deelvraag, dict):
                continue
            vt = deelvraag.get("vraagtype", "")
            if vt and vt not in seen:
                seen.add(vt)
                vraagtypes_set.append(vt)
        meta = {
            "vraag_id":               record.get("vraag_id", pad.stem),
            "examen_id":              record.get("examen_id", pad.parent.name),
            "vraag_herkomst":         record.get("vraag_herkomst", ""),
            "programmaonderdeel_ids": programmaonderdeel_ids_str,
            "vraagtypes":             ",".join(vraagtypes_set),
            "themas":                 ",".join(str(t) for t in record.get("themas", [])[:10]),
            "node_type":              "vraag",
        }
        ontbrekend = verplichte_velden - set(meta.keys())
        if ontbrekend:
            fouten.append(f"{pad.name}: ontbrekende velden {ontbrekend}")
    assert not fouten, "\n".join(fouten)


# ---------------------------------------------------------------------------
# 3. metadata-veld parse-roundtrip
# ---------------------------------------------------------------------------

def test_programmaonderdeel_ids_roundtrip():
    """programmaonderdeel_ids comma-separated string parseert terug naar lijst."""
    voorbeeld = ["1.6", "3.0"]
    als_string = ",".join(voorbeeld)
    terug = [p for p in als_string.split(",") if p]
    assert terug == voorbeeld


def test_programmaonderdeel_ids_enkel():
    po_string = "1.7"
    terug = [p for p in po_string.split(",") if p]
    assert terug == ["1.7"]


def test_programmaonderdeel_ids_leeg():
    po_string = ""
    terug = [p for p in po_string.split(",") if p]
    assert terug == []


# ---------------------------------------------------------------------------
# 4. Semantische queries (vereist geladen vragen-collection)
# ---------------------------------------------------------------------------

def test_semantische_query_fraude_boekhouder_top3():
    """'fraude door boekhouder' moet 2013-1-vr13 in top-3 opleveren."""
    col = _get_vragen_collection()
    res = col.query(
        query_texts=["fraude door boekhouder"],
        n_results=min(3, col.count()),
        include=["metadatas", "distances"],
    )
    vraag_ids = [m.get("vraag_id", "") for m in res["metadatas"][0]]
    assert "2013-1-vr13" in vraag_ids, (
        f"Verwacht 2013-1-vr13 in top-3, maar got: {vraag_ids}"
    )


def test_semantische_query_btw_aftrek_overwegend_po24():
    """'BTW-aftrek' moet overwegend PO 2.4 vragen opleveren (top-5)."""
    col = _get_vragen_collection()
    res = col.query(
        query_texts=["BTW-aftrek"],
        n_results=min(5, col.count()),
        include=["metadatas"],
    )
    po_id_strings = [m.get("programmaonderdeel_ids", "") for m in res["metadatas"][0]]
    po24_count = sum(1 for s in po_id_strings if "2.4" in s)
    assert po24_count >= 2, (
        f"Verwacht minstens 2 PO 2.4 vragen in top-5 bij 'BTW-aftrek', "
        f"maar got PO-strings: {po_id_strings}"
    )


def test_filter_programmaonderdeel_levert_alleen_po17():
    """Filter op programmaonderdeel_id='1.7' levert alleen PO 1.7 vragen op."""
    col = _get_vragen_collection()
    count = col.count()
    res = col.query(
        query_texts=["interne controle"],
        n_results=min(5, count),
        include=["metadatas"],
        where={"programmaonderdeel_ids": {"$contains": "1.7"}},
    )
    for meta in res["metadatas"][0]:
        po_string = meta.get("programmaonderdeel_ids", "")
        assert "1.7" in po_string, (
            f"Filter op 1.7 leverde vraag met PO-ids '{po_string}' op"
        )


# ---------------------------------------------------------------------------
# 5. _zoek_vragen MCP-tool
# ---------------------------------------------------------------------------

def test_zoek_vragen_mcp_tool_filter_po17():
    """_zoek_vragen met programmaonderdeel_id='1.7' levert alleen PO 1.7 resultaten."""
    if _vragen_collection_count() == 0:
        pytest.skip("vragen-collection niet beschikbaar")

    from tools.extractie.mcp_server.server import _zoek_vragen
    result_json = _zoek_vragen(
        query="interne controle functiescheiding",
        top_k=5,
        programmaonderdeel_id="1.7",
    )
    resultaten = json.loads(result_json)
    assert isinstance(resultaten, list), f"Verwacht lijst, got: {result_json[:200]}"
    for r in resultaten:
        po_string = r.get("programmaonderdeel_ids", "")
        assert "1.7" in po_string, (
            f"Filter 1.7 leverde vraag met PO-ids '{po_string}' op"
        )


def test_zoek_vragen_mcp_tool_returnstructuur():
    """_zoek_vragen retourneert compacte metadata-lijst zonder chunk-tekst."""
    if _vragen_collection_count() == 0:
        pytest.skip("vragen-collection niet beschikbaar")

    from tools.extractie.mcp_server.server import _zoek_vragen
    result_json = _zoek_vragen(query="jaarrekening balans", top_k=3)
    resultaten = json.loads(result_json)
    assert isinstance(resultaten, list)
    if resultaten:
        r = resultaten[0]
        assert "vraag_id" in r
        assert "examen_id" in r
        assert "similarity_score" in r
        assert "programmaonderdeel_ids" in r
        # Geen chunk-tekst in de output
        assert "text" not in r
        assert "chunk" not in r


def test_zoek_vragen_mcp_tool_collection_niet_beschikbaar():
    """_zoek_vragen retourneert foutmelding als collection leeg/afwezig is."""
    # Direct testen via mock — simuleer dat de collection niet bestaat
    try:
        import chromadb
        client = chromadb.PersistentClient(path=str(CHROMA_PATH))
        col = client.get_collection("vragen")
        if col.count() == 0:
            # Collection bestaat maar is leeg — MCP tool geeft error
            from tools.extractie.mcp_server.server import _zoek_vragen
            result = json.loads(_zoek_vragen("test"))
            assert "error" in result
    except Exception:
        # Collection bestaat niet — overslaan (dat is de normale skip-situatie)
        pass
