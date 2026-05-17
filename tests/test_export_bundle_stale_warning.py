"""
Smoke-tests voor de staleness-waarschuwing in `tools.extractie.export_bundle`
(ADR-005 §9 runtime-sanity-check, SQLite-store-variant §9.1).
"""
from __future__ import annotations

import os
import time
from pathlib import Path

from tools.extractie import export_bundle


def test_warn_if_store_stale_zwijgt_bij_verse_store(tmp_path, capsys, monkeypatch):
    """Geen waarschuwing als de store recenter is dan alle bronnen."""
    bron_dir = tmp_path / "wetteksten"
    bron_dir.mkdir()
    bron = bron_dir / "X.md"
    bron.write_text("---\nfoo: bar\n---\n")

    # Wacht een tikje, dan schrijf store → store recenter
    time.sleep(0.05)
    store = tmp_path / "matches.sqlite3"
    store.write_bytes(b"")

    monkeypatch.setattr(export_bundle, "_BRON_DIRS", (bron_dir,))
    export_bundle._warn_if_store_stale(store)
    captured = capsys.readouterr()
    assert "WAARSCHUWING" not in captured.out


def test_warn_if_store_stale_waarschuwt_bij_nieuwere_bron(tmp_path, capsys, monkeypatch):
    """Waarschuwing als minstens één bron recenter is dan de store."""
    bron_dir = tmp_path / "wetteksten"
    bron_dir.mkdir()

    store = tmp_path / "matches.sqlite3"
    store.write_bytes(b"")

    # Wacht een tikje, dan schrijf bron → bron recenter
    time.sleep(0.05)
    bron = bron_dir / "X.md"
    bron.write_text("---\nfoo: bar\n---\n")
    # Forceer een mtime bump (sommige FS geven dezelfde mtime bij snelle writes)
    os.utime(bron, (time.time() + 1, time.time() + 1))

    monkeypatch.setattr(export_bundle, "_BRON_DIRS", (bron_dir,))
    export_bundle._warn_if_store_stale(store)
    captured = capsys.readouterr()
    assert "WAARSCHUWING" in captured.out
    assert "X.md" in captured.out
    assert "refresh-gate" in captured.out


def test_warn_skipt_index_en_readme_bestanden(tmp_path, capsys, monkeypatch):
    """INDEX.md/README.md tellen niet mee — die genereren zichzelf."""
    bron_dir = tmp_path / "wetteksten"
    bron_dir.mkdir()

    store = tmp_path / "matches.sqlite3"
    store.write_bytes(b"")

    # Schrijf alleen index-bestanden recenter
    time.sleep(0.05)
    for naam in ("INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"):
        p = bron_dir / naam
        p.write_text("# index\n")
        os.utime(p, (time.time() + 1, time.time() + 1))

    monkeypatch.setattr(export_bundle, "_BRON_DIRS", (bron_dir,))
    export_bundle._warn_if_store_stale(store)
    captured = capsys.readouterr()
    assert "WAARSCHUWING" not in captured.out


def test_warn_geeft_geen_crash_zonder_store(tmp_path, capsys, monkeypatch):
    """Ontbrekende store → stille no-op (export_bundle stopt daarna toch)."""
    monkeypatch.setattr(export_bundle, "_BRON_DIRS", (tmp_path,))
    export_bundle._warn_if_store_stale(tmp_path / "nope.sqlite3")
    captured = capsys.readouterr()
    assert captured.out == ""
