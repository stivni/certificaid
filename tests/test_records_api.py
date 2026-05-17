"""
Unit-tests voor tools.lib.records_api (ADR-019).

Fixture-strategie:
  - Daemon gemockt via monkeypatch op tools.lib.records_api._post_daemon
  - ChromaDB: echte PersistentClient onder tmp_path (geïsoleerde test-state)
  - Atomiciteit getest via OSError / RuntimeError simulaties op mock

Alle tests draaien zonder live LaunchAgent-daemon.
"""

from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Optional
from unittest.mock import MagicMock

import pytest

# ─── Fixtures ─────────────────────────────────────────────────────────────────


@pytest.fixture()
def records_dir(tmp_path: Path) -> Path:
    """Geïsoleerde records-map voor tests."""
    d = tmp_path / "concepten" / "records"
    d.mkdir(parents=True)
    return d


@pytest.fixture()
def chroma_path(tmp_path: Path) -> str:
    """Pad naar een lege test-ChromaDB."""
    return str(tmp_path / "rag")


@pytest.fixture()
def test_record() -> dict:
    """Minimaal geldig concept-record voor tests."""
    return {
        "id": "test-concept",
        "naam": "Testconcept",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
    }


@pytest.fixture()
def patched_api(monkeypatch: pytest.MonkeyPatch, records_dir: Path, chroma_path: str):
    """
    Patch records_api zodat hij de tijdelijke records_dir gebruikt én de daemon mockt.

    Geeft een namedtuple-achtig object terug met:
      .daemon_calls  — lijst van (endpoint, payload, chroma_path) tuples van alle calls
      .records_dir   — tmp records-map
      .chroma_path   — tmp chroma-pad
      .set_daemon_fail(endpoint)  — laat de mock DaemonUnavailableError gooien voor endpoint
    """
    import tools.lib.records_api as api

    # Verander RECORDS_DIR naar de tijdelijke map
    monkeypatch.setattr(api, "RECORDS_DIR", records_dir)
    monkeypatch.setattr(api, "CHROMA_PATH_DEFAULT", Path(chroma_path))

    daemon_calls: list[tuple[str, dict, str]] = []
    daemon_fails: set[str] = set()

    def mock_post_daemon(endpoint: str, payload: dict, chroma_pad: str) -> dict:
        daemon_calls.append((endpoint, payload, chroma_pad))
        if endpoint in daemon_fails:
            from tools.lib.records_api import DaemonUnavailableError
            raise DaemonUnavailableError(f"Gesimuleerde daemon-fail op /{endpoint}")
        # Simuleer succesrespons
        if endpoint == "index-concept":
            concept_id = payload.get("record", {}).get("id", "onbekend")
            return {"id": concept_id, "ok": True}
        if endpoint == "delete-concept":
            return {"id": payload.get("concept_id", ""), "ok": True}
        return {"ok": True}

    monkeypatch.setattr(api, "_post_daemon", mock_post_daemon)

    # _laad_rag_ids mocken zodat we ChromaDB niet echt nodig hebben voor audit
    # maar we laten het voor audit-tests echt werken via chroma_path
    # (zie test_audit_* hierna die _laad_rag_ids direct aanroepen)

    class PatchedApi:
        def __init__(self):
            self.daemon_calls = daemon_calls
            self.daemon_fails = daemon_fails
            self.records_dir = records_dir
            self.chroma_path = chroma_path

        def set_daemon_fail(self, endpoint: str) -> None:
            daemon_fails.add(endpoint)

        def clear_daemon_fail(self, endpoint: str) -> None:
            daemon_fails.discard(endpoint)

    return PatchedApi()


# ─── Happy path: save_record ───────────────────────────────────────────────────


def test_save_record_nieuw_id(patched_api, test_record):
    """save_record schrijft naar disk en roept daemon aan voor nieuw record."""
    import tools.lib.records_api as api

    api.save_record(test_record, chroma_path=patched_api.chroma_path)

    # Disk-check
    pad = patched_api.records_dir / "test-concept.json"
    assert pad.exists(), "Record niet op disk geschreven"
    opgeslagen = json.loads(pad.read_text(encoding="utf-8"))
    assert opgeslagen["id"] == "test-concept"

    # Daemon-check
    assert len(patched_api.daemon_calls) == 1
    endpoint, payload, _ = patched_api.daemon_calls[0]
    assert endpoint == "index-concept"
    assert payload["record"]["id"] == "test-concept"


def test_save_record_bestaand_id(patched_api, test_record):
    """save_record update bestaand record in-place (disk + RAG)."""
    import tools.lib.records_api as api

    # Eerste opslag
    api.save_record(test_record, chroma_path=patched_api.chroma_path)

    # Update
    bijgewerkt = dict(test_record, naam="Bijgewerkt concept")
    api.save_record(bijgewerkt, chroma_path=patched_api.chroma_path)

    pad = patched_api.records_dir / "test-concept.json"
    opgeslagen = json.loads(pad.read_text(encoding="utf-8"))
    assert opgeslagen["naam"] == "Bijgewerkt concept"

    # Twee daemon-aanroepen (eerste + update)
    assert len(patched_api.daemon_calls) == 2
    for endpoint, _, _ in patched_api.daemon_calls:
        assert endpoint == "index-concept"


def test_save_record_zonder_id_fout(patched_api):
    """save_record zonder 'id'-veld gooit ValueError."""
    import tools.lib.records_api as api

    with pytest.raises(ValueError, match="geen 'id'-veld"):
        api.save_record({"naam": "Geen id"}, chroma_path=patched_api.chroma_path)

    # Geen daemon-call
    assert len(patched_api.daemon_calls) == 0


# ─── Happy path: rename_record ────────────────────────────────────────────────


def test_rename_record(patched_api, test_record):
    """rename_record verplaatst record: oud bestand weg, nieuw aangemaakt, RAG bijgewerkt."""
    import tools.lib.records_api as api

    # Maak oud record aan
    api.save_record(test_record, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()

    nieuw_record = dict(test_record, id="test-concept-hernoemd", naam="Hernoemd")
    api.rename_record("test-concept", nieuw_record, chroma_path=patched_api.chroma_path)

    # Oud bestand weg
    assert not (patched_api.records_dir / "test-concept.json").exists()
    # Nieuw bestand aangemaakt
    nieuw_pad = patched_api.records_dir / "test-concept-hernoemd.json"
    assert nieuw_pad.exists()
    opgeslagen = json.loads(nieuw_pad.read_text(encoding="utf-8"))
    assert opgeslagen["id"] == "test-concept-hernoemd"

    # Daemon: delete-concept(oud) + index-concept(nieuw)
    assert len(patched_api.daemon_calls) == 2
    assert patched_api.daemon_calls[0][0] == "delete-concept"
    assert patched_api.daemon_calls[0][1]["concept_id"] == "test-concept"
    assert patched_api.daemon_calls[1][0] == "index-concept"
    assert patched_api.daemon_calls[1][1]["record"]["id"] == "test-concept-hernoemd"


# ─── Happy path: delete_record ────────────────────────────────────────────────


def test_delete_record(patched_api, test_record):
    """delete_record verwijdert bestand en roept daemon aan."""
    import tools.lib.records_api as api

    api.save_record(test_record, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()

    api.delete_record("test-concept", chroma_path=patched_api.chroma_path)

    pad = patched_api.records_dir / "test-concept.json"
    assert not pad.exists(), "Record nog op disk na delete"

    assert len(patched_api.daemon_calls) == 1
    endpoint, payload, _ = patched_api.daemon_calls[0]
    assert endpoint == "delete-concept"
    assert payload["concept_id"] == "test-concept"


# ─── Atomiciteit: daemon-fail bij save_record ─────────────────────────────────


def test_save_record_daemon_fail_geen_disk_residu(patched_api, test_record):
    """Bij daemon-fail tijdens save_record: geen disk-residu (ADR-019 atomiciteitscontract)."""
    import tools.lib.records_api as api

    patched_api.set_daemon_fail("index-concept")

    with pytest.raises(api.DaemonUnavailableError):
        api.save_record(test_record, chroma_path=patched_api.chroma_path)

    # Geen disk-residu
    pad = patched_api.records_dir / "test-concept.json"
    assert not pad.exists(), "Disk-residu aangetroffen na daemon-fail"


def test_save_record_disk_fail_rollback_rag(monkeypatch, patched_api, test_record):
    """Bij disk-fail na geslaagde daemon-call: rollback via /delete-concept (ADR-019)."""
    import tools.lib.records_api as api

    # Laat disk-write falen door de pad.write_text te patchen
    originele_write = Path.write_text

    schrijf_teller = {"n": 0}

    def slechte_write(self, *args, **kwargs):
        schrijf_teller["n"] += 1
        if schrijf_teller["n"] == 1 and "test-concept" in str(self):
            raise OSError("Gesimuleerde disk-fout")
        return originele_write(self, *args, **kwargs)

    monkeypatch.setattr(Path, "write_text", slechte_write)

    with pytest.raises(OSError, match="Disk-write mislukt"):
        api.save_record(test_record, chroma_path=patched_api.chroma_path)

    # Daemon werd aangeroepen: eerst index-concept, dan delete-concept (rollback)
    endpoints = [call[0] for call in patched_api.daemon_calls]
    assert "index-concept" in endpoints
    assert "delete-concept" in endpoints

    rollback_call = next(c for c in patched_api.daemon_calls if c[0] == "delete-concept")
    assert rollback_call[1]["concept_id"] == "test-concept"


# ─── Atomiciteit: rename_record edge-cases ────────────────────────────────────


def test_rename_record_new_id_gelijk_aan_old_id(patched_api, test_record):
    """rename_record met new_id == old_id gooit ValueError."""
    import tools.lib.records_api as api

    api.save_record(test_record, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()

    with pytest.raises(ValueError, match="new_id == old_id"):
        api.rename_record(
            "test-concept",
            dict(test_record),  # zelfde id
            chroma_path=patched_api.chroma_path,
        )


def test_rename_record_oud_id_niet_gevonden(patched_api):
    """rename_record op niet-bestaand oud_id gooit RecordNotFoundError."""
    import tools.lib.records_api as api

    nieuw_record = {"id": "nieuw", "naam": "Nieuw"}
    with pytest.raises(api.RecordNotFoundError):
        api.rename_record(
            "bestaat-niet",
            nieuw_record,
            chroma_path=patched_api.chroma_path,
        )


# ─── Edge case: delete_record op onbestaande id ──────────────────────────────


def test_delete_record_niet_bestaand_id(patched_api):
    """delete_record op onbestaande id gooit RecordNotFoundError."""
    import tools.lib.records_api as api

    # Zorg dat RAG ook leeg is (mock retourneert lege set)
    with pytest.raises(api.RecordNotFoundError):
        api.delete_record("bestaat-niet", chroma_path=patched_api.chroma_path)


# ─── Audit parity ─────────────────────────────────────────────────────────────


def test_audit_parity_leeg(patched_api):
    """audit_parity op lege disk en lege RAG geeft ok=True."""
    import tools.lib.records_api as api

    # Beide leeg → ok
    resultaat = api.audit_parity(chroma_path=patched_api.chroma_path)
    assert resultaat["ok"] is True
    assert resultaat["ghosts"] == []
    assert resultaat["missing"] == []


def test_audit_parity_detecteert_missing(patched_api, test_record):
    """audit_parity detecteert records op disk die niet in RAG zitten."""
    import tools.lib.records_api as api

    # Schrijf bestand rechtstreeks naar disk (bypass API → geen RAG-entry)
    pad = patched_api.records_dir / "test-concept.json"
    pad.write_text(json.dumps(test_record) + "\n", encoding="utf-8")

    resultaat = api.audit_parity(chroma_path=patched_api.chroma_path)
    assert resultaat["ok"] is False
    assert "test-concept" in resultaat["missing"]
    assert resultaat["ghosts"] == []


def test_audit_parity_detecteert_ghost(monkeypatch, patched_api):
    """audit_parity detecteert ids in RAG die niet op disk staan."""
    import tools.lib.records_api as api

    # Simuleer een ghost in RAG
    monkeypatch.setattr(
        api, "_laad_rag_ids",
        lambda chroma_path: {"ghost-concept"}
    )

    resultaat = api.audit_parity(chroma_path=patched_api.chroma_path)
    assert resultaat["ok"] is False
    assert "ghost-concept" in resultaat["ghosts"]
    assert resultaat["missing"] == []


def test_audit_parity_beide_aanwezig(patched_api, test_record):
    """audit_parity geeft ok=True als disk en RAG identiek zijn."""
    import tools.lib.records_api as api

    api.save_record(test_record, chroma_path=patched_api.chroma_path)

    # Na save_record: disk = {"test-concept"}, RAG = {} (mock-daemon schrijft niet echt)
    # We patchen _laad_rag_ids om de mock-state te weerspiegelen
    from unittest.mock import patch
    with patch.object(api, "_laad_rag_ids", return_value={"test-concept"}):
        resultaat = api.audit_parity(chroma_path=patched_api.chroma_path)
        assert resultaat["ok"] is True
        assert resultaat["ghosts"] == []
        assert resultaat["missing"] == []


# ─── CLI exit-codes ───────────────────────────────────────────────────────────


def test_cli_audit_exit_0_bij_geen_drift(monkeypatch, patched_api):
    """CLI 'audit' geeft exit 0 bij ok-state."""
    import tools.lib.records_api as api

    monkeypatch.setattr(api, "_laad_disk_ids", lambda: set())
    monkeypatch.setattr(api, "_laad_rag_ids", lambda chroma_path: set())

    exit_code = api._cli_audit(patched_api.chroma_path, fix=False)
    assert exit_code == 0


def test_cli_audit_exit_1_bij_drift(monkeypatch, patched_api):
    """CLI 'audit' geeft exit 1 bij drift."""
    import tools.lib.records_api as api

    monkeypatch.setattr(api, "_laad_disk_ids", lambda: {"ontbreekt-in-rag"})
    monkeypatch.setattr(api, "_laad_rag_ids", lambda chroma_path: set())

    exit_code = api._cli_audit(patched_api.chroma_path, fix=False)
    assert exit_code == 1


# ─── CLI reindex-all ──────────────────────────────────────────────────────────


def test_cli_reindex_all_raakt_alle_disk_ids(patched_api, test_record):
    """reindex-all indexeert alle records op disk opnieuw."""
    import tools.lib.records_api as api

    # Schrijf twee records rechtstreeks (bypass API)
    for i in range(2):
        record = dict(test_record, id=f"record-{i}", naam=f"Record {i}")
        (patched_api.records_dir / f"record-{i}.json").write_text(
            json.dumps(record) + "\n", encoding="utf-8"
        )

    patched_api.daemon_calls.clear()
    exit_code = api._cli_reindex_all(patched_api.chroma_path)
    assert exit_code == 0

    # Twee /index-concept calls (één per record)
    endpoints = [c[0] for c in patched_api.daemon_calls]
    assert endpoints.count("index-concept") == 2


# ─── Concurrentie: serialisatie via daemon-lock ───────────────────────────────


def test_save_record_concurrentie_serialiseert(patched_api, test_record):
    """
    Meerdere gelijktijdige save_record-aanroepen serialiseren correct
    (geen torn writes). Regressietest op daemon-lock discipline (ADR-019).

    Controleert enkel dat alle records uiteindelijk op disk staan
    en alle daemon-calls plaatsvonden (mock-niveau, geen echte concurrency-race).
    """
    import tools.lib.records_api as api

    records = [dict(test_record, id=f"concurrent-{i}") for i in range(5)]
    fouten: list[Exception] = []

    def schrijf(record):
        try:
            api.save_record(record, chroma_path=patched_api.chroma_path)
        except Exception as exc:
            fouten.append(exc)

    threads = [threading.Thread(target=schrijf, args=(r,)) for r in records]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert fouten == [], f"Fouten bij concurrent schrijven: {fouten}"
    for i in range(5):
        assert (patched_api.records_dir / f"concurrent-{i}.json").exists()
