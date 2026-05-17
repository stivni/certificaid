"""
Smoke-tests voor `tools.etl.refresh_rag_and_matches` (ADR-005 §9 + §9.1).

We mocken `subprocess.run` zodat we de wrapper-orchestratie controleren
zonder daadwerkelijk MPS-embedding of cosine-matching te draaien.
"""
from __future__ import annotations

import subprocess
from unittest.mock import patch, MagicMock

import pytest

from tools.etl import refresh_rag_and_matches as wrapper


def _ok_run(*_, **__):
    m = MagicMock()
    m.returncode = 0
    return m


def _fail_run_first_call():
    """Eerste call faalt (rag_index), tweede zou succes zijn."""
    calls = {"n": 0}

    def _run(*_, **__):
        calls["n"] += 1
        m = MagicMock()
        m.returncode = 1 if calls["n"] == 1 else 0
        return m

    return _run, calls


def test_refresh_draait_rag_index_dan_match():
    """Happy path: beide stappen worden in volgorde aangevuurd."""
    captured: list[list[str]] = []

    def _run(cmd, *, cwd=None):
        captured.append(list(cmd))
        m = MagicMock()
        m.returncode = 0
        return m

    with patch.object(subprocess, "run", side_effect=_run):
        wrapper.refresh()

    assert len(captured) == 2
    # Stap 1 is rag_index.py
    assert any("rag_index.py" in part for part in captured[0])
    # Stap 2 is match_bronnen module
    assert "tools.extractie.match_bronnen" in captured[1]


def test_refresh_stopt_bij_falende_rag_index():
    """Als rag_index crasht mag match_bronnen NIET draaien — voorkomt mismatch."""
    _run, calls = _fail_run_first_call()
    with patch.object(subprocess, "run", side_effect=_run):
        with pytest.raises(SystemExit):
            wrapper.refresh()
    # Alleen stap 1 mocht uitgevoerd worden
    assert calls["n"] == 1


def test_refresh_geeft_bron_rol_door_aan_rag_index():
    captured: list[list[str]] = []

    def _run(cmd, *, cwd=None):
        captured.append(list(cmd))
        return _ok_run()

    with patch.object(subprocess, "run", side_effect=_run):
        wrapper.refresh(bron_rol="norm")

    assert "--bron-rol" in captured[0]
    assert "norm" in captured[0]


def test_refresh_geeft_match_args_door_aan_match_bronnen():
    captured: list[list[str]] = []

    def _run(cmd, *, cwd=None):
        captured.append(list(cmd))
        return _ok_run()

    with patch.object(subprocess, "run", side_effect=_run):
        wrapper.refresh(match_margin=0.20, match_threshold=0.60)

    match_cmd = captured[1]
    assert "--margin" in match_cmd
    assert "0.2" in match_cmd
    assert "--threshold" in match_cmd
    assert "0.6" in match_cmd
