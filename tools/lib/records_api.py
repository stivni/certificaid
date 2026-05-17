"""
Centrale records-API voor Certificaid concept-records (ADR-019).

Enige toegestane interface voor mutaties aan data/concepten/records/*.json.
Garandeert dat elke disk-write ook de `concepten` ChromaDB-collection bijwerkt
(RAG-parity-discipline).

Atomiciteitscontract per operatie (ADR-019 §"Atomiciteitscontract"):
  save_record:   daemon /index-concept → disk write. Disk-fail → /delete-concept rollback.
  rename_record: daemon /delete-concept(oud) → daemon /index-concept(nieuw) → disk delete + write.
  delete_record: disk delete → daemon /delete-concept (log loud bij stap-2-fail).

Gebruik:
  from tools.lib.records_api import save_record, rename_record, delete_record, audit_parity

  # CLI
  python3 -m tools.lib.records_api audit
  python3 -m tools.lib.records_api audit --fix
  python3 -m tools.lib.records_api reindex-all
  python3 -m tools.lib.records_api reindex <concept_id>
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Optional

import requests

logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
CHROMA_PATH_DEFAULT = ROOT / "data" / "rag" / "main"
COLLECTIE_NAAM = "concepten"

DAEMON_URL = "http://127.0.0.1:8765"
DAEMON_TIMEOUT = 10  # seconden — ADR-019 §"Failure modes": >10s → raise

ALLOWED_DATA_PREFIX = str(ROOT / "data")


# ---------------------------------------------------------------------------
# Uitzonderingen
# ---------------------------------------------------------------------------

class DaemonUnavailableError(RuntimeError):
    """Daemon is niet bereikbaar — geen disk-write toegestaan."""


class RecordNotFoundError(KeyError):
    """Record bestaat niet op disk of in RAG."""


# ---------------------------------------------------------------------------
# Interne helpers
# ---------------------------------------------------------------------------

def _default_chroma_path() -> str:
    return str(CHROMA_PATH_DEFAULT)


def _post_daemon(endpoint: str, payload: dict, chroma_path: str) -> dict:
    """
    POST naar daemon-endpoint. Gooit DaemonUnavailableError bij connectie-probleem,
    RuntimeError bij HTTP-fout, requests.Timeout bij overschrijding DAEMON_TIMEOUT.
    """
    volledig_payload = dict(payload, chroma_path=chroma_path)
    try:
        r = requests.post(
            f"{DAEMON_URL}/{endpoint}",
            json=volledig_payload,
            timeout=DAEMON_TIMEOUT,
        )
        r.raise_for_status()
        return r.json()
    except requests.exceptions.ConnectionError as exc:
        raise DaemonUnavailableError(
            f"Embedding-daemon niet bereikbaar op {DAEMON_URL}. "
            f"Start de daemon eerst (ADR-018). Originele fout: {exc}"
        ) from exc
    except requests.exceptions.Timeout as exc:
        raise DaemonUnavailableError(
            f"Embedding-daemon timeout (>{DAEMON_TIMEOUT}s) op /{endpoint}."
        ) from exc
    except requests.exceptions.HTTPError as exc:
        raise RuntimeError(
            f"Daemon /{endpoint} HTTP-fout: {exc.response.status_code} — "
            f"{exc.response.text}"
        ) from exc


def _record_pad(record_id: str) -> Path:
    """Geef het verwachte bestandspad terug voor een record-id."""
    return RECORDS_DIR / f"{record_id}.json"


def _laad_rag_ids(chroma_path: str) -> set[str]:
    """Lees alle concept-ids uit de ChromaDB-collection (read-only)."""
    try:
        import chromadb  # type: ignore
        client = chromadb.PersistentClient(path=chroma_path)
        try:
            collectie = client.get_collection(COLLECTIE_NAAM)
        except Exception:
            return set()
        resultaat = collectie.get(include=[])
        return set(resultaat.get("ids", []))
    except Exception as exc:
        logger.warning("RAG-ids ophalen mislukt (%s): %s", chroma_path, exc)
        return set()


def _laad_disk_ids() -> set[str]:
    """Lees alle concept-ids van disk (bestandsnamen zonder .json)."""
    if not RECORDS_DIR.exists():
        return set()
    return {
        pad.stem
        for pad in RECORDS_DIR.glob("*.json")
        if not pad.name.startswith("_")
    }


# ---------------------------------------------------------------------------
# Publieke API
# ---------------------------------------------------------------------------

def save_record(
    record: dict,
    chroma_path: Optional[str] = None,
) -> None:
    """
    Atomair: schrijf record naar disk + upsert in concept-RAG.

    Atomiciteitscontract (ADR-019 §"Atomiciteitscontract"):
    1. Daemon /index-concept → 200 OK
    2. Disk write
    Als stap 2 faalt → /delete-concept rollback + raise.

    Faalt loud als daemon niet bereikbaar — geen disk-only writes.
    Bestaande id → in-place update (zowel disk als RAG).
    Nieuwe id → nieuwe entry in beide.

    Args:
        record: volledig concept-record dict (schema 1.x, ADR-007)
        chroma_path: pad naar ChromaDB-instantie. Default: data/rag/main

    Raises:
        DaemonUnavailableError: daemon niet bereikbaar of timeout
        RuntimeError: daemon HTTP-fout bij upsert
        ValueError: record heeft geen 'id'-veld
    """
    concept_id = record.get("id")
    if not concept_id:
        raise ValueError("record heeft geen 'id'-veld — save_record geweigerd")

    resolved_chroma = chroma_path or _default_chroma_path()

    # Stap 1: daemon upsert (RAG eerst — atomiciteitscontract)
    _post_daemon("index-concept", {"record": record}, resolved_chroma)
    logger.debug("save_record: daemon /index-concept OK voor %s", concept_id)

    # Stap 2: disk write
    pad = _record_pad(concept_id)
    pad.parent.mkdir(parents=True, exist_ok=True)
    try:
        pad.write_text(
            json.dumps(record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    except OSError as exc:
        # Disk-write mislukt → rollback RAG
        logger.error(
            "save_record: disk-write mislukt voor %s, rollback RAG …", concept_id
        )
        try:
            _post_daemon(
                "delete-concept",
                {"concept_id": concept_id},
                resolved_chroma,
            )
            logger.info(
                "save_record: rollback RAG OK voor %s (record verwijderd uit RAG)",
                concept_id,
            )
        except Exception as rollback_exc:
            logger.error(
                "save_record: rollback RAG ook mislukt voor %s: %s",
                concept_id,
                rollback_exc,
            )
        raise OSError(
            f"Disk-write mislukt voor {concept_id}: {exc}"
        ) from exc

    logger.info("save_record: %s opgeslagen (disk + RAG)", concept_id)


def rename_record(
    old_id: str,
    new_record: dict,
    chroma_path: Optional[str] = None,
) -> None:
    """
    Atomair: verwijder old_id uit RAG + verwijder oud bestand,
    schrijf nieuw bestand + upsert nieuwe id in RAG.

    new_record['id'] moet ≠ old_id zijn.

    Atomiciteitscontract (ADR-019 §"Atomiciteitscontract"):
    1. daemon /delete-concept(old_id)
    2. daemon /index-concept(new_record)
    3. disk delete oud + write nieuw
    Bij stap 2 of 3 falen: rollback van eerder gelukte stappen + raise.

    Args:
        old_id: bestaande concept-id die hernoemd wordt
        new_record: volledig nieuw record dict (new_record['id'] ≠ old_id)
        chroma_path: pad naar ChromaDB-instantie. Default: data/rag/main

    Raises:
        ValueError: new_record['id'] == old_id
        RecordNotFoundError: old_id bestaat niet op disk
        DaemonUnavailableError: daemon niet bereikbaar
        RuntimeError: daemon HTTP-fout
    """
    new_id = new_record.get("id")
    if not new_id:
        raise ValueError("new_record heeft geen 'id'-veld")
    if new_id == old_id:
        raise ValueError(
            f"rename_record: new_id == old_id ('{old_id}') — "
            "gebruik save_record voor in-place updates"
        )

    oud_pad = _record_pad(old_id)
    if not oud_pad.exists():
        raise RecordNotFoundError(
            f"rename_record: oud bestand niet gevonden: {oud_pad}"
        )

    resolved_chroma = chroma_path or _default_chroma_path()

    # Stap 1: verwijder old_id uit RAG
    _post_daemon("delete-concept", {"concept_id": old_id}, resolved_chroma)
    logger.debug("rename_record: daemon /delete-concept OK voor %s", old_id)

    # Stap 2: upsert new_record in RAG
    try:
        _post_daemon("index-concept", {"record": new_record}, resolved_chroma)
        logger.debug("rename_record: daemon /index-concept OK voor %s", new_id)
    except Exception as exc:
        # Stap 2 mislukt → rollback stap 1: herstel old_id in RAG
        logger.error(
            "rename_record: /index-concept mislukt voor %s, rollback: re-index old_id %s",
            new_id,
            old_id,
        )
        try:
            oud_record = json.loads(oud_pad.read_text(encoding="utf-8"))
            _post_daemon("index-concept", {"record": oud_record}, resolved_chroma)
            logger.info("rename_record: rollback OK — %s terug in RAG", old_id)
        except Exception as rollback_exc:
            logger.error(
                "rename_record: rollback ook mislukt: %s", rollback_exc
            )
        raise RuntimeError(
            f"rename_record: /index-concept mislukt voor {new_id}: {exc}"
        ) from exc

    # Stap 3: disk delete oud + write nieuw
    nieuw_pad = _record_pad(new_id)
    nieuw_pad.parent.mkdir(parents=True, exist_ok=True)
    try:
        oud_pad.unlink()
        nieuw_pad.write_text(
            json.dumps(new_record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    except OSError as exc:
        # Disk-operatie mislukt → rollback RAG-stappen 1 en 2
        logger.error(
            "rename_record: disk-operatie mislukt, rollback RAG voor %s en %s",
            old_id,
            new_id,
        )
        try:
            _post_daemon("delete-concept", {"concept_id": new_id}, resolved_chroma)
            if oud_pad.exists():
                oud_record = json.loads(oud_pad.read_text(encoding="utf-8"))
                _post_daemon("index-concept", {"record": oud_record}, resolved_chroma)
        except Exception as rollback_exc:
            logger.error("rename_record: rollback ook mislukt: %s", rollback_exc)
        raise OSError(
            f"Disk-operatie mislukt bij rename van {old_id} → {new_id}: {exc}"
        ) from exc

    logger.info("rename_record: %s → %s (disk + RAG)", old_id, new_id)


def delete_record(
    record_id: str,
    chroma_path: Optional[str] = None,
) -> None:
    """
    Atomaar: verwijder bestand + verwijder uit RAG.

    Atomiciteitscontract (ADR-019 §"Atomiciteitscontract"):
    1. disk delete
    2. daemon /delete-concept
    Bij stap 2 falen: log loud (niets meer op disk, entry nog in RAG —
    zal bij volgende delete-aanroep opnieuw weggehaald kunnen worden).

    Args:
        record_id: id van het te verwijderen record
        chroma_path: pad naar ChromaDB-instantie. Default: data/rag/main

    Raises:
        RecordNotFoundError: record bestaat niet op disk én niet in RAG
        DaemonUnavailableError: daemon niet bereikbaar bij stap 2
    """
    pad = _record_pad(record_id)
    resolved_chroma = chroma_path or _default_chroma_path()

    # Sanity-check: bestaat het record?
    disk_bestaat = pad.exists()
    rag_ids = _laad_rag_ids(resolved_chroma)
    rag_bestaat = record_id in rag_ids

    if not disk_bestaat and not rag_bestaat:
        raise RecordNotFoundError(
            f"delete_record: record '{record_id}' bestaat niet op disk "
            f"en niet in RAG — niets te verwijderen"
        )

    # Stap 1: disk delete
    if disk_bestaat:
        pad.unlink()
        logger.debug("delete_record: disk delete OK voor %s", record_id)

    # Stap 2: RAG verwijderen (log loud bij falen)
    try:
        _post_daemon("delete-concept", {"concept_id": record_id}, resolved_chroma)
        logger.info("delete_record: %s verwijderd (disk + RAG)", record_id)
    except Exception as exc:
        logger.error(
            "delete_record: disk delete OK, maar /delete-concept MISLUKT voor %s: %s. "
            "State: niets op disk, entry nog in RAG (ghost). "
            "Voer `records_api audit --fix` uit om de ghost te verwijderen.",
            record_id,
            exc,
        )
        # Niet re-raiseable — disk is al clean, ghost wordt bij audit opgeruimd


def audit_parity(
    chroma_path: Optional[str] = None,
) -> dict:
    """
    Vergelijk disk-records met RAG-collectie. Read-only.

    Returns:
        {
          'disk_ids': set[str],
          'rag_ids': set[str],
          'ghosts': list[str],     # in RAG, niet op disk
          'missing': list[str],    # op disk, niet in RAG
          'ok': bool,
        }

    Veilig om vaak te draaien — geen mutaties.
    """
    resolved_chroma = chroma_path or _default_chroma_path()
    disk_ids = _laad_disk_ids()
    rag_ids = _laad_rag_ids(resolved_chroma)

    ghosts = sorted(rag_ids - disk_ids)
    missing = sorted(disk_ids - rag_ids)

    return {
        "disk_ids": disk_ids,
        "rag_ids": rag_ids,
        "ghosts": ghosts,
        "missing": missing,
        "ok": len(ghosts) == 0 and len(missing) == 0,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cli_audit(chroma_path: Optional[str], fix: bool) -> int:
    """
    Draai audit_parity() en rapporteer. Exit 0 als ok=True, exit 1 anders.
    Met --fix: verwijder ghosts uit RAG en reindex missing van disk.
    """
    parity = audit_parity(chroma_path)
    ghosts = parity["ghosts"]
    missing = parity["missing"]

    print(f"[audit] disk: {len(parity['disk_ids'])} records, "
          f"RAG: {len(parity['rag_ids'])} records")

    if parity["ok"]:
        print("[audit] OK — disk en RAG zijn in sync.")
        return 0

    if ghosts:
        print(f"[audit] {len(ghosts)} ghost(s) in RAG (niet op disk):")
        for ghost in ghosts:
            print(f"  GHOST  {ghost}")

    if missing:
        print(f"[audit] {len(missing)} missing record(s) in RAG (wel op disk):")
        for missed in missing:
            print(f"  MISSING  {missed}")

    if not fix:
        print(
            "\n[audit] Drift gevonden. Gebruik 'audit --fix' om te herstellen "
            "of 'reindex-all' om alle records opnieuw te indexeren."
        )
        return 1

    # --fix modus
    resolved_chroma = chroma_path or _default_chroma_path()
    herstel_fouten = 0

    # Verwijder ghosts uit RAG
    for ghost in ghosts:
        try:
            _post_daemon("delete-concept", {"concept_id": ghost}, resolved_chroma)
            print(f"  [fix] ghost verwijderd uit RAG: {ghost}")
        except Exception as exc:
            print(f"  [fix] ghost NIET verwijderd ({ghost}): {exc}", file=sys.stderr)
            herstel_fouten += 1

    # Reindex missing records
    for missed in missing:
        pad = _record_pad(missed)
        try:
            record = json.loads(pad.read_text(encoding="utf-8"))
            _post_daemon("index-concept", {"record": record}, resolved_chroma)
            print(f"  [fix] missing geïndexeerd in RAG: {missed}")
        except Exception as exc:
            print(f"  [fix] missing NIET geïndexeerd ({missed}): {exc}", file=sys.stderr)
            herstel_fouten += 1

    if herstel_fouten == 0:
        print(f"[audit --fix] herstel voltooid: {len(ghosts)} ghost(s) + "
              f"{len(missing)} missing(s) verwerkt.")
        return 0
    else:
        print(f"[audit --fix] herstel gedeeltelijk: {herstel_fouten} fout(en).", file=sys.stderr)
        return 1


def _cli_reindex_all(chroma_path: Optional[str]) -> int:
    """Indexeer alle disk-records opnieuw in RAG via save_record."""
    disk_ids = _laad_disk_ids()
    if not disk_ids:
        print("[reindex-all] Geen records gevonden op disk.")
        return 0

    print(f"[reindex-all] {len(disk_ids)} records opnieuw indexeren …")
    resolved_chroma = chroma_path or _default_chroma_path()
    fouten = 0

    for record_id in sorted(disk_ids):
        pad = _record_pad(record_id)
        try:
            record = json.loads(pad.read_text(encoding="utf-8"))
            save_record(record, chroma_path=resolved_chroma)
            print(f"  ✓ {record_id}")
        except Exception as exc:
            print(f"  ✗ {record_id}: {exc}", file=sys.stderr)
            fouten += 1

    print(f"\n[reindex-all] {len(disk_ids) - fouten}/{len(disk_ids)} records geïndexeerd.")
    return 0 if fouten == 0 else 1


def _cli_reindex_one(record_id: str, chroma_path: Optional[str]) -> int:
    """Indexeer één record opnieuw."""
    pad = _record_pad(record_id)
    if not pad.exists():
        print(f"[reindex] Record niet gevonden op disk: {pad}", file=sys.stderr)
        return 1

    resolved_chroma = chroma_path or _default_chroma_path()
    try:
        record = json.loads(pad.read_text(encoding="utf-8"))
        save_record(record, chroma_path=resolved_chroma)
        print(f"[reindex] ✓ {record_id}")
        return 0
    except Exception as exc:
        print(f"[reindex] ✗ {record_id}: {exc}", file=sys.stderr)
        return 1


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Centrale records-API CLI (ADR-019). "
                    "Beheer en controleer concept-records + RAG-parity.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Subcommands:
  audit             Controleer disk/RAG parity (read-only). Exit 0 = ok, 1 = drift.
  audit --fix       Herstel drift: verwijder ghosts, reindex missing.
  reindex-all       Indexeer alle disk-records opnieuw in RAG.
  reindex <id>      Indexeer één record opnieuw in RAG.

Voorbeelden:
  python3 -m tools.lib.records_api audit
  python3 -m tools.lib.records_api audit --fix
  python3 -m tools.lib.records_api reindex-all
  python3 -m tools.lib.records_api reindex beroepsgeheim-gecertificeerd-accountant
""",
    )
    parser.add_argument(
        "--chroma",
        default=None,
        metavar="PAD",
        help=f"ChromaDB-pad (default: {CHROMA_PATH_DEFAULT.relative_to(ROOT)})",
    )

    subparsers = parser.add_subparsers(dest="subcommand")

    # audit
    audit_parser = subparsers.add_parser(
        "audit",
        help="Controleer disk/RAG parity",
    )
    audit_parser.add_argument(
        "--fix",
        action="store_true",
        help="Herstel drift na de check",
    )

    # reindex-all
    subparsers.add_parser(
        "reindex-all",
        help="Indexeer alle disk-records opnieuw in RAG",
    )

    # reindex <id>
    reindex_parser = subparsers.add_parser(
        "reindex",
        help="Indexeer één record opnieuw in RAG",
    )
    reindex_parser.add_argument(
        "concept_id",
        help="Concept-id (bestandsnaam zonder .json)",
    )

    args = parser.parse_args()

    if args.subcommand is None:
        parser.print_help()
        sys.exit(0)

    chroma = str(Path(args.chroma).resolve()) if args.chroma else None

    if args.subcommand == "audit":
        sys.exit(_cli_audit(chroma, fix=args.fix))
    elif args.subcommand == "reindex-all":
        sys.exit(_cli_reindex_all(chroma))
    elif args.subcommand == "reindex":
        sys.exit(_cli_reindex_one(args.concept_id, chroma))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
