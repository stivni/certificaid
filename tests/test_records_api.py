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
def content_dir(tmp_path: Path) -> Path:
    """Geïsoleerde content/concepten-map voor tests."""
    d = tmp_path / "content" / "concepten"
    d.mkdir(parents=True)
    return d


@pytest.fixture()
def patched_api(monkeypatch: pytest.MonkeyPatch, records_dir: Path, chroma_path: str, content_dir: Path):
    """
    Patch records_api zodat hij de tijdelijke records_dir gebruikt, de daemon mockt
    en render-calls registreert zonder echte Jinja2-afhankelijkheid.

    Geeft een object terug met:
      .daemon_calls    — lijst van (endpoint, payload, chroma_path) tuples
      .render_calls    — lijst van (record_id,) tuples van render-aanroepen
      .delete_fiche_calls — lijst van concept_id's van verwijderde markdown-fiches
      .records_dir     — tmp records-map
      .content_dir     — tmp content/concepten-map
      .chroma_path     — tmp chroma-pad
      .set_daemon_fail(endpoint)  — laat de mock DaemonUnavailableError gooien voor endpoint
      .set_render_fail()          — laat de render-mock een Exception gooien
    """
    import tools.lib.records_api as api

    # Verander RECORDS_DIR en CONTENT_CONCEPTEN_DIR naar de tijdelijke mappen
    monkeypatch.setattr(api, "RECORDS_DIR", records_dir)
    monkeypatch.setattr(api, "CHROMA_PATH_DEFAULT", Path(chroma_path))
    monkeypatch.setattr(api, "CONTENT_CONCEPTEN_DIR", content_dir)

    daemon_calls: list[tuple[str, dict, str]] = []
    daemon_fails: set[str] = set()
    render_calls: list[str] = []
    render_fail: list[bool] = [False]
    delete_fiche_calls: list[str] = []

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

    def mock_render_concept_fiche(record: dict, content_dir: Optional[Path] = None) -> None:
        concept_id = record.get("id", "onbekend")
        render_calls.append(concept_id)
        if render_fail[0]:
            raise RuntimeError(f"Gesimuleerde render-fout voor {concept_id}")

    def mock_verwijder_concept_fiche(concept_id: str, content_dir: Optional[Path] = None) -> None:
        delete_fiche_calls.append(concept_id)

    monkeypatch.setattr(api, "_post_daemon", mock_post_daemon)
    monkeypatch.setattr(api, "_render_concept_fiche", mock_render_concept_fiche)
    monkeypatch.setattr(api, "_verwijder_concept_fiche", mock_verwijder_concept_fiche)

    # _laad_rag_ids mocken zodat we ChromaDB niet echt nodig hebben voor audit
    # maar we laten het voor audit-tests echt werken via chroma_path
    # (zie test_audit_* hierna die _laad_rag_ids direct aanroepen)

    class PatchedApi:
        def __init__(self):
            self.daemon_calls = daemon_calls
            self.daemon_fails = daemon_fails
            self.render_calls = render_calls
            self.delete_fiche_calls = delete_fiche_calls
            self.records_dir = records_dir
            self.content_dir = content_dir
            self.chroma_path = chroma_path

        def set_daemon_fail(self, endpoint: str) -> None:
            daemon_fails.add(endpoint)

        def clear_daemon_fail(self, endpoint: str) -> None:
            daemon_fails.discard(endpoint)

        def set_render_fail(self) -> None:
            render_fail[0] = True

        def clear_render_fail(self) -> None:
            render_fail[0] = False

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
    """audit_parity geeft ok=True als disk, RAG én content identiek zijn."""
    import tools.lib.records_api as api

    api.save_record(test_record, chroma_path=patched_api.chroma_path)

    # Schrijf ook een markdown-fiche in de content_dir
    (patched_api.content_dir / "test-concept.md").write_text("# Test\n", encoding="utf-8")

    # Na save_record: disk = {"test-concept"}, RAG = {} (mock-daemon schrijft niet echt)
    # We patchen _laad_rag_ids om de mock-state te weerspiegelen
    from unittest.mock import patch
    with patch.object(api, "_laad_rag_ids", return_value={"test-concept"}):
        resultaat = api.audit_parity(
            chroma_path=patched_api.chroma_path,
            content_dir=patched_api.content_dir,
        )
        assert resultaat["ok"] is True
        assert resultaat["ghosts"] == []
        assert resultaat["missing"] == []
        assert resultaat["content_ontbreekt"] == []
        assert resultaat["content_extra"] == []


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


# ─── Timeout-mitigatie (ADR-019 §"Timeout-mitigatie") ────────────────────────


def test_cold_start_timeout_eerste_call_60s(monkeypatch, records_dir, tmp_path, test_record):
    """
    Eerste save_record-call na module-import gebruikt 60s timeout (cold-start).
    Tweede call gebruikt 10s.

    ADR-019 §"Timeout-mitigatie" mitigatie 1.
    """
    import importlib
    import tools.lib.records_api as api
    import requests

    # Reset de cold-start-state door de module-variabele terug te zetten
    monkeypatch.setattr(api, "_eerste_daemon_call_gedaan", False)
    monkeypatch.setattr(api, "RECORDS_DIR", records_dir)
    # Isoleer content_dir zodat er geen bestanden in het echte content/concepten/ worden geschreven
    monkeypatch.setattr(api, "CONTENT_CONCEPTEN_DIR", tmp_path / "content_concepten")
    monkeypatch.setattr(api, "_render_concept_fiche", lambda record, content_dir=None: None)

    ontvangen_timeouts: list[int] = []

    def mock_requests_post(url, json=None, timeout=None, **kwargs):
        ontvangen_timeouts.append(timeout)
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.raise_for_status = lambda: None
        mock_response.json.return_value = {"ok": True}
        return mock_response

    monkeypatch.setattr(requests, "post", mock_requests_post)

    # Eerste call — verwacht: 60s timeout
    api.save_record(test_record, chroma_path=str(records_dir / "rag"))
    assert ontvangen_timeouts[0] == 60, (
        f"Eerste call verwachtte 60s timeout, kreeg {ontvangen_timeouts[0]}s"
    )

    # Tweede call — verwacht: 10s timeout (DAEMON_TIMEOUT)
    record_2 = dict(test_record, id="test-concept-2")
    api.save_record(record_2, chroma_path=str(records_dir / "rag"))
    assert ontvangen_timeouts[1] == 10, (
        f"Tweede call verwachtte 10s timeout, kreeg {ontvangen_timeouts[1]}s"
    )


def test_timeout_met_server_success_ghost_recovery(monkeypatch, records_dir, test_record):
    """
    Scenario: daemon ontvangt verzoek + voert RAG-upsert uit, maar client hit timeout.
    Gevolg: ghost in RAG, record niet op disk.

    Verwacht gedrag (ADR-019 §"Timeout-mitigatie" mitigatie 3):
    - save_record triggert audit_parity → detecteert ghost
    - roept /delete-concept aan voor ghost-rollback
    - logt warning
    - re-raiset de originele timeout-exception

    ADR-019 §"Timeout-mitigatie" mitigatie 2 + 3.
    """
    import tools.lib.records_api as api
    import requests

    monkeypatch.setattr(api, "_eerste_daemon_call_gedaan", True)  # Sla cold-start over
    monkeypatch.setattr(api, "RECORDS_DIR", records_dir)

    concept_id = test_record["id"]

    # Bijhouden welke daemon-endpoints zijn aangeroepen
    daemon_calls: list[str] = []

    def mock_post_daemon(endpoint: str, payload: dict, chroma_pad: str) -> dict:
        daemon_calls.append(endpoint)
        if endpoint == "index-concept":
            # Simuleer: daemon doet de upsert maar client ziet timeout
            raise requests.exceptions.Timeout("Gesimuleerde timeout na server-success")
        if endpoint == "delete-concept":
            # Rollback geslaagd
            return {"ok": True}
        return {"ok": True}

    monkeypatch.setattr(api, "_post_daemon", mock_post_daemon)

    # audit_parity moet de ghost detecteren: daemon deed de upsert (concept_id in RAG)
    # maar record staat niet op disk (records_dir is leeg)
    def mock_audit_parity(chroma_path=None):
        return {
            "disk_ids": set(),
            "rag_ids": {concept_id},
            "ghosts": [concept_id],   # concept_id is ghost (RAG maar niet disk)
            "missing": [],
            "ok": False,
        }

    monkeypatch.setattr(api, "audit_parity", mock_audit_parity)

    # save_record moet: exception re-raisen + ghost opgeruimd hebben
    with pytest.raises((api.DaemonUnavailableError, requests.exceptions.Timeout)):
        api.save_record(test_record, chroma_path=str(records_dir / "rag"))

    # Ghost-rollback: /delete-concept moet aangeroepen zijn
    assert "delete-concept" in daemon_calls, (
        "Ghost-rollback via /delete-concept niet aangeroepen na timeout + ghost-detectie"
    )

    # Record mag niet op disk staan (timeout voor disk-write)
    assert not (records_dir / f"{concept_id}.json").exists(), (
        "Record staat onterecht op disk na timeout-failure"
    )


def test_disk_fail_na_daemon_success_ghost_recovery(monkeypatch, patched_api, test_record):
    """
    Scenario: daemon-call slaagt (RAG-upsert OK), maar disk-write gooit OSError.
    Gevolg zonder mitigatie: ghost in RAG.

    Verwacht gedrag (ADR-019 §"Atomiciteitscontract"):
    - save_record triggert audit_parity na de OSError
    - detecteert ghost → roept /delete-concept aan
    - re-raiset OSError

    Dit test de post-failure ghost-recovery ook bij disk-fouten.
    """
    import tools.lib.records_api as api

    concept_id = test_record["id"]

    # Originele _post_daemon is al gemockt door patched_api (succesvol).
    # Laat alleen disk-write falen.
    originele_write = Path.write_text
    schrijf_teller = {"n": 0}

    def slechte_write(self, *args, **kwargs):
        schrijf_teller["n"] += 1
        if schrijf_teller["n"] == 1 and concept_id in str(self):
            raise OSError("Gesimuleerde disk-fout na geslaagde daemon-call")
        return originele_write(self, *args, **kwargs)

    monkeypatch.setattr(Path, "write_text", slechte_write)

    # audit_parity simuleert de ghost-toestand
    def mock_audit_parity(chroma_path=None):
        return {
            "disk_ids": set(),
            "rag_ids": {concept_id},
            "ghosts": [concept_id],
            "missing": [],
            "ok": False,
        }

    monkeypatch.setattr(api, "audit_parity", mock_audit_parity)

    with pytest.raises(OSError, match="Disk-write mislukt"):
        api.save_record(test_record, chroma_path=patched_api.chroma_path)

    # Ghost-rollback: zowel de initiële rollback (huidig pad) als de parity-recovery
    # moeten /delete-concept aanroepen. In beide gevallen: delete-concept in daemon_calls.
    endpoints = [c[0] for c in patched_api.daemon_calls]
    assert "delete-concept" in endpoints, (
        "/delete-concept niet aangeroepen na disk-fout + ghost-detectie"
    )


def test_geen_valse_rollback_bij_fout_voor_daemon_call(monkeypatch, patched_api, test_record):
    """
    Scenario: save_record faalt vóór de daemon-call (bv. ValueError op ontbrekend id-veld).
    In dit geval is er geen ghost in RAG → geen /delete-concept aanroep verwacht.

    Verwacht gedrag: audit_parity wordt eventueel aangeroepen maar detecteert geen ghost
    → geen rollback.

    ADR-019 §"Timeout-mitigatie": "Geen valse rollback" scenario.
    """
    import tools.lib.records_api as api

    # Record zonder id → faalt vóór daemon-call
    record_zonder_id = {"naam": "Geen id"}

    with pytest.raises(ValueError, match="geen 'id'-veld"):
        api.save_record(record_zonder_id, chroma_path=patched_api.chroma_path)

    # Geen daemon-calls
    assert len(patched_api.daemon_calls) == 0, (
        f"Daemon onterecht aangeroepen: {patched_api.daemon_calls}"
    )

    # Geen rollback via /delete-concept
    delete_calls = [c for c in patched_api.daemon_calls if c[0] == "delete-concept"]
    assert delete_calls == [], "Valse rollback: /delete-concept aangeroepen zonder ghost"


def test_geen_valse_rollback_bij_fout_voor_daemon_call_connection_error(
    monkeypatch, records_dir, test_record
):
    """
    Scenario: save_record faalt doordat de daemon niet bereikbaar is (ConnectionError).
    Daemon heeft niets gedaan → geen ghost → geen /delete-concept rollback verwacht.

    audit_parity zou het concept_id als MISSING (niet als ghost) rapporteren
    want het staat niet op disk én niet in RAG.
    """
    import tools.lib.records_api as api

    monkeypatch.setattr(api, "_eerste_daemon_call_gedaan", True)
    monkeypatch.setattr(api, "RECORDS_DIR", records_dir)

    concept_id = test_record["id"]
    delete_calls: list[str] = []

    def mock_post_daemon(endpoint: str, payload: dict, chroma_pad: str) -> dict:
        if endpoint == "index-concept":
            raise api.DaemonUnavailableError("Daemon niet bereikbaar")
        if endpoint == "delete-concept":
            delete_calls.append(endpoint)
            return {"ok": True}
        return {"ok": True}

    monkeypatch.setattr(api, "_post_daemon", mock_post_daemon)

    # audit_parity: geen ghost (daemon deed niets)
    def mock_audit_parity(chroma_path=None):
        return {
            "disk_ids": set(),
            "rag_ids": set(),   # daemon deed niets → geen ghost
            "ghosts": [],
            "missing": [],
            "ok": True,
        }

    monkeypatch.setattr(api, "audit_parity", mock_audit_parity)

    with pytest.raises(api.DaemonUnavailableError):
        api.save_record(test_record, chroma_path=str(records_dir / "rag"))

    # Geen valse rollback: /delete-concept niet aangeroepen want geen ghost
    assert delete_calls == [], (
        f"Valse rollback: /delete-concept aangeroepen zonder ghost. Calls: {delete_calls}"
    )


# ─── Content-sync (ADR-019 §"Content-sync") ──────────────────────────────────


def test_save_record_triggert_render(patched_api, test_record):
    """
    save_record roept render_concept_fiche aan na succesvolle disk-write.
    ADR-019 §"Content-sync": drie-stappen-flow RAG → disk → render.
    """
    import tools.lib.records_api as api

    api.save_record(test_record, chroma_path=patched_api.chroma_path)

    # Render moet zijn aangeroepen voor het correcte concept-id
    assert "test-concept" in patched_api.render_calls, (
        f"render_concept_fiche niet aangeroepen na save_record. render_calls: {patched_api.render_calls}"
    )


def test_save_record_render_fout_faalt_save_niet(patched_api, test_record):
    """
    Als render_concept_fiche een fout gooit, faalt save_record NIET.
    ADR-019 §"Content-sync": render-fout → log WARNING, geen rollback.
    """
    import tools.lib.records_api as api

    patched_api.set_render_fail()

    # save_record moet slagen ondanks render-fout
    api.save_record(test_record, chroma_path=patched_api.chroma_path)

    # Record staat op disk (render-fout mag dit niet terugdraaien)
    pad = patched_api.records_dir / "test-concept.json"
    assert pad.exists(), "Record verdwenen na render-fout — ten onrechte rollback"

    # Daemon-call wél gedaan
    assert any(c[0] == "index-concept" for c in patched_api.daemon_calls)


def test_delete_record_verwijdert_markdown(patched_api, test_record):
    """
    delete_record ruimt de markdown-fiche op.
    ADR-019 §"Content-sync": stap 3 na disk delete + RAG delete.
    """
    import tools.lib.records_api as api

    api.save_record(test_record, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()
    patched_api.render_calls.clear()
    patched_api.delete_fiche_calls.clear()

    api.delete_record("test-concept", chroma_path=patched_api.chroma_path)

    # _verwijder_concept_fiche moet zijn aangeroepen voor het correcte id
    assert "test-concept" in patched_api.delete_fiche_calls, (
        f"_verwijder_concept_fiche niet aangeroepen bij delete_record. "
        f"delete_fiche_calls: {patched_api.delete_fiche_calls}"
    )


def test_rename_record_verwijdert_oude_markdown_en_maakt_nieuwe(patched_api, test_record):
    """
    rename_record verwijdert de oude markdown-fiche en maakt een nieuwe aan.
    ADR-019 §"Content-sync": render(nieuw) + markdown delete(oud).
    """
    import tools.lib.records_api as api

    api.save_record(test_record, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()
    patched_api.render_calls.clear()
    patched_api.delete_fiche_calls.clear()

    nieuw_record = dict(test_record, id="test-concept-hernoemd", naam="Hernoemd")
    api.rename_record("test-concept", nieuw_record, chroma_path=patched_api.chroma_path)

    # Nieuwe markdown gerenderd
    assert "test-concept-hernoemd" in patched_api.render_calls, (
        "Nieuwe markdown-fiche niet gerenderd na rename_record"
    )
    # Oude markdown verwijderd
    assert "test-concept" in patched_api.delete_fiche_calls, (
        "Oude markdown-fiche niet verwijderd na rename_record"
    )


def test_rename_record_render_fout_faalt_rename_niet(patched_api, test_record):
    """
    Als render_concept_fiche een fout gooit bij rename_record, faalt rename NIET.
    ADR-019 §"Content-sync": render-fout → log WARNING, geen rollback.
    """
    import tools.lib.records_api as api

    api.save_record(test_record, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()
    patched_api.set_render_fail()

    nieuw_record = dict(test_record, id="test-concept-hernoemd")
    api.rename_record("test-concept", nieuw_record, chroma_path=patched_api.chroma_path)

    # Disk-state is correct ondanks render-fout
    assert not (patched_api.records_dir / "test-concept.json").exists()
    assert (patched_api.records_dir / "test-concept-hernoemd.json").exists()


def test_audit_parity_detecteert_content_drift_ontbreekt(monkeypatch, patched_api, test_record):
    """
    audit_parity detecteert records op disk zonder overeenkomstige markdown-fiche.
    ADR-019 §"Content-sync": content_ontbreekt = op disk, niet als markdown.
    """
    import tools.lib.records_api as api

    # Schrijf record op disk zonder render (bypass API)
    pad = patched_api.records_dir / "test-concept.json"
    pad.write_text(json.dumps(test_record) + "\n", encoding="utf-8")

    # RAG-ids simuleren als in sync
    monkeypatch.setattr(api, "_laad_rag_ids", lambda chroma_path: {"test-concept"})

    # content_dir is leeg → content_ontbreekt
    resultaat = api.audit_parity(
        chroma_path=patched_api.chroma_path,
        content_dir=patched_api.content_dir,
    )
    assert resultaat["ok"] is False
    assert "test-concept" in resultaat["content_ontbreekt"]
    assert resultaat["content_extra"] == []


def test_audit_parity_detecteert_content_extra(monkeypatch, patched_api):
    """
    audit_parity detecteert markdown-fiches die geen overeenkomstig record op disk hebben.
    ADR-019 §"Content-sync": content_extra = markdown bestaat, geen record op disk.
    """
    import tools.lib.records_api as api

    # Schrijf een markdown-fiche zonder record
    markdown_pad = patched_api.content_dir / "weesje.md"
    markdown_pad.write_text("# Weesje\n\nGeen record meer.", encoding="utf-8")

    # Disk en RAG zijn leeg
    monkeypatch.setattr(api, "_laad_rag_ids", lambda chroma_path: set())

    resultaat = api.audit_parity(
        chroma_path=patched_api.chroma_path,
        content_dir=patched_api.content_dir,
    )
    assert resultaat["ok"] is False
    assert "weesje" in resultaat["content_extra"]
    assert resultaat["content_ontbreekt"] == []


# ─── Orphan-management (ADR-019 §"Orphan-management") ───────────────────────


def test_delete_record_cascadeert_edge_removal(patched_api, test_record):
    """
    delete_record verwijdert dangling edges in andere records.

    Scenario: record A heeft een edge.target naar B. Na delete(B) moet A's
    edges-lijst geen verwijzing naar B meer bevatten en moet A opnieuw zijn
    geïndexeerd (save_record aangeroepen voor A).

    ADR-019 §"Orphan-management": auto-cascade bij delete.
    """
    import tools.lib.records_api as api

    record_a = {
        "id": "record-a",
        "naam": "Record A",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [{"type": "verwant", "target": "record-b", "redenering": "test"}],
        "vergelijkingsparen": [],
    }
    record_b = {
        "id": "record-b",
        "naam": "Record B",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [],
    }

    # Schrijf beide records via API
    api.save_record(record_a, chroma_path=patched_api.chroma_path)
    api.save_record(record_b, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()

    # Delete B → cascade moet A bijwerken
    api.delete_record("record-b", chroma_path=patched_api.chroma_path)

    # A staat nog op disk (niet verwijderd)
    pad_a = patched_api.records_dir / "record-a.json"
    assert pad_a.exists(), "record-a onterecht verwijderd"

    # A's edges bevatten geen target 'record-b' meer
    bijgewerkt_a = json.loads(pad_a.read_text(encoding="utf-8"))
    targets = [e.get("target") for e in bijgewerkt_a.get("edges", [])]
    assert "record-b" not in targets, (
        f"Dangling edge naar record-b nog aanwezig in record-a: {bijgewerkt_a['edges']}"
    )

    # save_record voor record-a aangeroepen (cascade-herindexering)
    index_calls_voor_a = [
        c for c in patched_api.daemon_calls
        if c[0] == "index-concept" and c[1].get("record", {}).get("id") == "record-a"
    ]
    assert len(index_calls_voor_a) >= 1, (
        "record-a niet hergeïndexeerd na cascade-delete van record-b"
    )


def test_delete_record_cascadeert_vergelijkingsparen_removal(patched_api, test_record):
    """
    delete_record verwijdert dangling vergelijkingsparen in andere records.

    Scenario: record A heeft vergelijkingsparen[].vergelijking_met == B.
    Na delete(B) mag A geen vergelijkingspaar naar B meer bevatten.

    ADR-019 §"Orphan-management": auto-cascade bij delete.
    """
    import tools.lib.records_api as api

    record_a = {
        "id": "record-a-vp",
        "naam": "Record A (vergelijkingsparen)",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [
            {
                "vergelijking_met": "record-b-vp",
                "verschil": "Testomschrijving",
                "trigger": "Bij examen",
                "confidence": "inferred-common-knowledge",
            }
        ],
    }
    record_b = {
        "id": "record-b-vp",
        "naam": "Record B (vergelijkingsparen)",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [],
    }

    api.save_record(record_a, chroma_path=patched_api.chroma_path)
    api.save_record(record_b, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()

    api.delete_record("record-b-vp", chroma_path=patched_api.chroma_path)

    pad_a = patched_api.records_dir / "record-a-vp.json"
    assert pad_a.exists()
    bijgewerkt_a = json.loads(pad_a.read_text(encoding="utf-8"))
    vergelijkingen = [
        p.get("vergelijking_met")
        for p in bijgewerkt_a.get("vergelijkingsparen", [])
    ]
    assert "record-b-vp" not in vergelijkingen, (
        f"Dangling vergelijkingspaar naar record-b-vp nog aanwezig in record-a-vp: "
        f"{bijgewerkt_a['vergelijkingsparen']}"
    )


def test_rename_record_redirects_edges(patched_api, test_record):
    """
    rename_record herleidt edges in andere records van old_id naar new_id.

    Scenario: A heeft edge.target == B. Na rename(B → C) moet A's edge
    naar C wijzen, en moet A hergeïndexeerd zijn.

    ADR-019 §"Orphan-management": auto-redirect bij rename.
    """
    import tools.lib.records_api as api

    record_a = {
        "id": "source-record",
        "naam": "Source",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [{"type": "verwant", "target": "oud-doel", "redenering": "test"}],
        "vergelijkingsparen": [],
    }
    record_b = {
        "id": "oud-doel",
        "naam": "Oud doel",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [],
    }

    api.save_record(record_a, chroma_path=patched_api.chroma_path)
    api.save_record(record_b, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()

    nieuw_record_b = dict(record_b, id="nieuw-doel", naam="Nieuw doel")
    api.rename_record("oud-doel", nieuw_record_b, chroma_path=patched_api.chroma_path)

    # A's edge wijst nu naar nieuw-doel
    pad_a = patched_api.records_dir / "source-record.json"
    assert pad_a.exists()
    bijgewerkt_a = json.loads(pad_a.read_text(encoding="utf-8"))
    targets = [e.get("target") for e in bijgewerkt_a.get("edges", [])]
    assert "nieuw-doel" in targets, (
        f"Edge niet geredirect naar nieuw-doel in source-record: {bijgewerkt_a['edges']}"
    )
    assert "oud-doel" not in targets, (
        f"Oude edge target nog aanwezig in source-record: {bijgewerkt_a['edges']}"
    )

    # source-record hergeïndexeerd
    index_calls_voor_source = [
        c for c in patched_api.daemon_calls
        if c[0] == "index-concept"
        and c[1].get("record", {}).get("id") == "source-record"
    ]
    assert len(index_calls_voor_source) >= 1, (
        "source-record niet hergeïndexeerd na cascade-redirect van oud-doel → nieuw-doel"
    )


def test_delete_zonder_incoming_edges_geen_onnodige_saves(patched_api, test_record):
    """
    delete_record op een record zonder inkomende edges doet geen cascade-saves.

    Verwacht gedrag: alleen de normale delete-flow (disk + RAG + content),
    geen save_record voor andere records. Verifieer via daemon_calls.

    ADR-019 §"Orphan-management": correctness vóór performance.
    """
    import tools.lib.records_api as api

    # Schrijf één geïsoleerd record (geen ander record wijst ernaar)
    api.save_record(test_record, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()

    api.delete_record("test-concept", chroma_path=patched_api.chroma_path)

    # Alleen /delete-concept voor test-concept zelf — geen /index-concept
    index_calls = [c for c in patched_api.daemon_calls if c[0] == "index-concept"]
    assert index_calls == [], (
        f"Onnodige cascade-save aangetroffen bij delete van geïsoleerd record: "
        f"{index_calls}"
    )

    # /delete-concept moet wel aangeroepen zijn (voor test-concept zelf)
    delete_calls = [c for c in patched_api.daemon_calls if c[0] == "delete-concept"]
    assert len(delete_calls) == 1, (
        f"Verwachtte exact 1 delete-concept call, kreeg: {delete_calls}"
    )


def test_audit_parity_ok_met_content_in_sync(monkeypatch, patched_api, test_record):
    """
    audit_parity geeft ok=True als disk, RAG en content allemaal in sync zijn.
    ADR-019 §"Content-sync": disk_and_rag_and_content = volledig OK.
    """
    import tools.lib.records_api as api

    concept_id = test_record["id"]

    # Record op disk
    pad = patched_api.records_dir / f"{concept_id}.json"
    pad.write_text(json.dumps(test_record) + "\n", encoding="utf-8")

    # Markdown-fiche in content_dir
    (patched_api.content_dir / f"{concept_id}.md").write_text("# Test\n", encoding="utf-8")

    # RAG in sync
    monkeypatch.setattr(api, "_laad_rag_ids", lambda chroma_path: {concept_id})

    resultaat = api.audit_parity(
        chroma_path=patched_api.chroma_path,
        content_dir=patched_api.content_dir,
    )
    assert resultaat["ok"] is True
    assert resultaat["ghosts"] == []
    assert resultaat["missing"] == []
    assert resultaat["content_ontbreekt"] == []
    assert resultaat["content_extra"] == []


# ─── Orphan-management: gebaseerd_op_concepten + wikilinks ───────────────────


def test_delete_record_verwijdert_gebaseerd_op_concepten(patched_api):
    """
    delete_record verwijdert target_id uit gebaseerd_op_concepten[] in andere records.

    Scenario: synthese-record A heeft gebaseerd_op_concepten: [B, C, D].
    Na delete(D) → A's lijst wordt [B, C]; A is hergeïndexeerd.

    ADR-019 §"Orphan-management": gebaseerd_op_concepten[] bij delete.
    """
    import tools.lib.records_api as api

    record_a = {
        "id": "synthese-a",
        "naam": "Synthese A",
        "node_type": "synthese",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [],
        "gebaseerd_op_concepten": ["concept-b", "concept-c", "concept-d"],
    }
    record_d = {
        "id": "concept-d",
        "naam": "Concept D",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [],
    }

    api.save_record(record_a, chroma_path=patched_api.chroma_path)
    api.save_record(record_d, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()

    # Delete D → cascade moet A bijwerken
    api.delete_record("concept-d", chroma_path=patched_api.chroma_path)

    # A staat nog op disk
    pad_a = patched_api.records_dir / "synthese-a.json"
    assert pad_a.exists(), "synthese-a onterecht verwijderd"

    # A's gebaseerd_op_concepten bevat concept-d niet meer
    bijgewerkt_a = json.loads(pad_a.read_text(encoding="utf-8"))
    gebaseerd_op = bijgewerkt_a.get("gebaseerd_op_concepten", [])
    assert "concept-d" not in gebaseerd_op, (
        f"concept-d nog aanwezig in gebaseerd_op_concepten van synthese-a: {gebaseerd_op}"
    )
    # B en C staan er nog wél in
    assert "concept-b" in gebaseerd_op, "concept-b ten onrechte verwijderd"
    assert "concept-c" in gebaseerd_op, "concept-c ten onrechte verwijderd"

    # A is hergeïndexeerd
    index_calls_a = [
        c for c in patched_api.daemon_calls
        if c[0] == "index-concept" and c[1].get("record", {}).get("id") == "synthese-a"
    ]
    assert len(index_calls_a) >= 1, "synthese-a niet hergeïndexeerd na cascade-delete van concept-d"


def test_rename_record_redirecteert_gebaseerd_op_concepten(patched_api):
    """
    rename_record herleidt gebaseerd_op_concepten[] van old_id naar new_id.

    Scenario: synthese-record A heeft gebaseerd_op_concepten: [B, C, D].
    Na rename(D → D2) → A's lijst wordt [B, C, D2].

    ADR-019 §"Orphan-management": gebaseerd_op_concepten[] bij rename.
    """
    import tools.lib.records_api as api

    record_a = {
        "id": "synthese-a-rename",
        "naam": "Synthese A rename",
        "node_type": "synthese",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [],
        "gebaseerd_op_concepten": ["concept-b", "concept-c", "concept-d-oud"],
    }
    record_d = {
        "id": "concept-d-oud",
        "naam": "Concept D oud",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [],
    }

    api.save_record(record_a, chroma_path=patched_api.chroma_path)
    api.save_record(record_d, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()

    nieuw_record_d = dict(record_d, id="concept-d-nieuw", naam="Concept D nieuw")
    api.rename_record("concept-d-oud", nieuw_record_d, chroma_path=patched_api.chroma_path)

    # A's gebaseerd_op_concepten is bijgewerkt
    pad_a = patched_api.records_dir / "synthese-a-rename.json"
    assert pad_a.exists()
    bijgewerkt_a = json.loads(pad_a.read_text(encoding="utf-8"))
    gebaseerd_op = bijgewerkt_a.get("gebaseerd_op_concepten", [])
    assert "concept-d-nieuw" in gebaseerd_op, (
        f"concept-d-nieuw niet gevonden in gebaseerd_op_concepten: {gebaseerd_op}"
    )
    assert "concept-d-oud" not in gebaseerd_op, (
        f"concept-d-oud nog aanwezig in gebaseerd_op_concepten: {gebaseerd_op}"
    )
    assert "concept-b" in gebaseerd_op, "concept-b ten onrechte verwijderd"
    assert "concept-c" in gebaseerd_op, "concept-c ten onrechte verwijderd"


def test_delete_record_verwijdert_wikilink_naar_target(patched_api):
    """
    delete_record vervangt wikilinks naar het verwijderde record door plain tekst.

    Scenario: record A heeft definitie.text = "Onderdeel van [[B]] en [[C]]".
    Na delete(B) → tekst wordt "Onderdeel van B en [[C]]" (link weg, tekst behouden).

    ADR-019 §"Orphan-management": wikilink delete→plain tekst.
    """
    import tools.lib.records_api as api

    record_a = {
        "id": "record-met-wikilinks",
        "naam": "Record met wikilinks",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [],
        "definitie": {"text": "Onderdeel van [[concept-te-verwijderen]] en [[concept-c]]"},
    }
    record_b = {
        "id": "concept-te-verwijderen",
        "naam": "Concept Te Verwijderen",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [],
    }

    api.save_record(record_a, chroma_path=patched_api.chroma_path)
    api.save_record(record_b, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()

    api.delete_record("concept-te-verwijderen", chroma_path=patched_api.chroma_path)

    # A staat nog op disk
    pad_a = patched_api.records_dir / "record-met-wikilinks.json"
    assert pad_a.exists()
    bijgewerkt_a = json.loads(pad_a.read_text(encoding="utf-8"))

    tekst = bijgewerkt_a.get("definitie", {}).get("text", "")
    # [[concept-te-verwijderen]] moet plain tekst geworden zijn
    assert "[[concept-te-verwijderen]]" not in tekst, (
        f"Kapotte wikilink nog aanwezig: {tekst}"
    )
    assert "concept-te-verwijderen" in tekst, (
        f"Tekst-inhoud verdwenen na wikilink-verwijdering: {tekst}"
    )
    # [[concept-c]] moet intact zijn
    assert "[[concept-c]]" in tekst, (
        f"Ongeraakte wikilink [[concept-c]] gewijzigd: {tekst}"
    )


def test_rename_record_redirecteert_wikilink_naar_target(patched_api):
    """
    rename_record vervangt wikilinks van old_id door new_id.

    Scenario: record A heeft definitie.text = "Onderdeel van [[B]] en [[C]]".
    Na rename(B → B2) → tekst wordt "Onderdeel van [[B2]] en [[C]]".

    ADR-019 §"Orphan-management": wikilink rename→link-update.
    """
    import tools.lib.records_api as api

    record_a = {
        "id": "record-met-wikilinks-rename",
        "naam": "Record met wikilinks rename",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [],
        "definitie": {"text": "Onderdeel van [[concept-b-oud]] en [[concept-c]]"},
    }
    record_b = {
        "id": "concept-b-oud",
        "naam": "Concept B oud",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [],
    }

    api.save_record(record_a, chroma_path=patched_api.chroma_path)
    api.save_record(record_b, chroma_path=patched_api.chroma_path)
    patched_api.daemon_calls.clear()

    nieuw_record_b = dict(record_b, id="concept-b-nieuw", naam="Concept B nieuw")
    api.rename_record("concept-b-oud", nieuw_record_b, chroma_path=patched_api.chroma_path)

    # A's wikilink is bijgewerkt
    pad_a = patched_api.records_dir / "record-met-wikilinks-rename.json"
    assert pad_a.exists()
    bijgewerkt_a = json.loads(pad_a.read_text(encoding="utf-8"))

    tekst = bijgewerkt_a.get("definitie", {}).get("text", "")
    assert "[[concept-b-nieuw]]" in tekst, (
        f"Wikilink niet geredirect naar concept-b-nieuw: {tekst}"
    )
    assert "[[concept-b-oud]]" not in tekst, (
        f"Oude wikilink [[concept-b-oud]] nog aanwezig: {tekst}"
    )
    assert "[[concept-c]]" in tekst, (
        f"Ongeraakte wikilink [[concept-c]] gewijzigd: {tekst}"
    )


def test_wikilink_met_display_naam_bij_delete_en_rename(patched_api):
    """
    Wikilinks met display-naam: [[id|Display]] → bij delete: "Display", bij rename: [[new_id|Display]].

    ADR-019 §"Orphan-management": display-naam optioneel scenario.
    """
    import tools.lib.records_api as api

    record_a = {
        "id": "record-display-wikilink",
        "naam": "Record display wikilink",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [],
        "definitie": {
            "text": "Zie [[concept-x|Verklaring van X]] voor details."
        },
    }
    record_x = {
        "id": "concept-x",
        "naam": "Concept X",
        "node_type": "begrip",
        "status": "seed",
        "schema_version": "1.4",
        "linked_anchors": [],
        "edges": [],
        "vergelijkingsparen": [],
    }

    # --- delete scenario ---
    api.save_record(record_a, chroma_path=patched_api.chroma_path)
    api.save_record(record_x, chroma_path=patched_api.chroma_path)

    api.delete_record("concept-x", chroma_path=patched_api.chroma_path)

    pad_a = patched_api.records_dir / "record-display-wikilink.json"
    bijgewerkt_a = json.loads(pad_a.read_text(encoding="utf-8"))
    tekst_na_delete = bijgewerkt_a.get("definitie", {}).get("text", "")

    # display-naam behouden, link weg
    assert "[[concept-x" not in tekst_na_delete, (
        f"Kapotte wikilink nog aanwezig na delete: {tekst_na_delete}"
    )
    assert "Verklaring van X" in tekst_na_delete, (
        f"Display-naam verdwenen na delete: {tekst_na_delete}"
    )

    # --- rename scenario: herstellen en dan rename testen ---
    # Herstel record_a met originele tekst en schrijf record_x opnieuw
    api.save_record(record_a, chroma_path=patched_api.chroma_path)
    api.save_record(record_x, chroma_path=patched_api.chroma_path)

    nieuw_record_x = dict(record_x, id="concept-x-nieuw", naam="Concept X nieuw")
    api.rename_record("concept-x", nieuw_record_x, chroma_path=patched_api.chroma_path)

    bijgewerkt_a_na_rename = json.loads(pad_a.read_text(encoding="utf-8"))
    tekst_na_rename = bijgewerkt_a_na_rename.get("definitie", {}).get("text", "")

    # link bijgewerkt, display-naam bewaard
    assert "[[concept-x-nieuw|Verklaring van X]]" in tekst_na_rename, (
        f"Wikilink met display-naam niet correct bijgewerkt na rename: {tekst_na_rename}"
    )
