"""Tests voor tools/etl/sample_review.py.

Werkt met fixture-MDs in pytest tmp_path; raakt resources/bronnen/ niet aan.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from tools.etl import sample_review as sr


def _write_bron(
    path: Path,
    *,
    status: str = "trusted",
    qa_version: str = "run-A",
    confirmed_by: str = "subagent-sonnet-4-6",
    agent_verdict_at: str = "2026-05-01T10:00:00Z",
    sample_pick: bool = False,
    sample_reviewed_at=None,
    rationale: str = "auto-trusted",
    extra_body: str = "Inhoud van de bron.\n",
) -> None:
    """Schrijf een minimaal bron-MD met provenance.trust-blok."""
    fm_lines = [
        "---",
        "titel: Fixture",
        "provenance:",
        "  inputs:",
        "    - id: dummy.pdf",
        "      sha256: abc123",
        "  tooling:",
        "    pipeline: tools/etl/dummy.py",
        "    pipeline_version: deadbee",
        "  generated_at: 2026-05-01T09:00:00Z",
        "  stale: false",
        "  stale_reason:",
        "  trust:",
        f"    status: {status}",
        f"    qa_version: {qa_version}",
        f"    confirmed_at: {agent_verdict_at}",
        f"    agent_verdict_at: {agent_verdict_at}",
        f"    confirmed_by: {confirmed_by}",
        f"    rationale: \"{rationale}\"",
        f"    sample_pick: {'true' if sample_pick else 'false'}",
    ]
    if sample_reviewed_at is None:
        fm_lines.append("    sample_reviewed_at:")
        fm_lines.append("    sample_reviewed_by:")
    else:
        fm_lines.append(f"    sample_reviewed_at: {sample_reviewed_at}")
        fm_lines.append("    sample_reviewed_by: human")
    fm_lines.append("---")
    path.write_text("\n".join(fm_lines) + "\n" + extra_body, encoding="utf-8")


@pytest.fixture
def fake_corpus(tmp_path, monkeypatch):
    """Maak een tmp_path/wetteksten/ + tmp_path/normen/ met fixture-MDs en
    monkeypatch BRON_DIRS + ROOT zodat sample_review.py daarmee werkt."""
    wett = tmp_path / "wetteksten"
    norm = tmp_path / "normen"
    adv = tmp_path / "adviezen"
    wett.mkdir()
    norm.mkdir()
    adv.mkdir()

    monkeypatch.setattr(sr, "BRON_DIRS", [wett, norm, adv])
    monkeypatch.setattr(sr, "ROOT", tmp_path)
    return tmp_path, wett, norm, adv


def test_pick_zet_sample_pick_op_steekproef(fake_corpus, capsys):
    _, wett, _, _ = fake_corpus
    # 10 auto-trusted bronnen in dezelfde run; rate=30 → 3 picks
    for i in range(10):
        _write_bron(wett / f"bron-{i:02d}.md", qa_version="run-X")

    sr.cmd_pick("run-X", rate=30.0, seed=42)

    picks = []
    for f in sorted(wett.glob("*.md")):
        data, _ = sr._read_frontmatter(f)
        trust = sr._get_trust(data)
        if trust.get("sample_pick"):
            picks.append(f.name)

    assert len(picks) == 3, f"Verwachtte 3 picks, kreeg {len(picks)}: {picks}"

    # Bronnen zonder sample_pick blijven onveranderd
    others = [f.name for f in sorted(wett.glob("*.md")) if f.name not in picks]
    assert len(others) == 7

    out = capsys.readouterr().out
    assert "Auto-trusted kandidaten: 10" in out
    assert "Steekproef (3)" in out


def test_pick_skipt_human_confirmed_en_andere_run(fake_corpus):
    _, wett, _, _ = fake_corpus
    # 1 human-confirmed → moet niet meegenomen worden
    _write_bron(wett / "human.md", confirmed_by="human", qa_version="run-X")
    # 1 in andere run → niet meegenomen
    _write_bron(wett / "other-run.md", qa_version="run-Y")
    # 2 valide auto-trusted → beide moeten gepickt worden bij rate=100
    _write_bron(wett / "ok-1.md", qa_version="run-X")
    _write_bron(wett / "ok-2.md", qa_version="run-X")

    sr.cmd_pick("run-X", rate=100.0, seed=1)

    def is_picked(name: str) -> bool:
        data, _ = sr._read_frontmatter(wett / name)
        return bool(sr._get_trust(data).get("sample_pick"))

    assert is_picked("ok-1.md") is True
    assert is_picked("ok-2.md") is True
    assert is_picked("human.md") is False
    assert is_picked("other-run.md") is False


def test_mark_ok_zet_reviewed_velden_en_behoudt_trusted(fake_corpus, capsys):
    _, wett, _, _ = fake_corpus
    target = wett / "pick.md"
    _write_bron(target, qa_version="run-X", sample_pick=True)

    sr.cmd_mark_ok(str(target))

    data, _ = sr._read_frontmatter(target)
    trust = sr._get_trust(data)
    assert trust["status"] == "trusted"
    assert trust["sample_reviewed_by"] == "human"
    assert trust["sample_reviewed_at"] is not None
    assert "T" in trust["sample_reviewed_at"]  # ISO-format

    out = capsys.readouterr().out
    assert "OK" in out


def test_mark_ok_faalt_zonder_sample_pick(fake_corpus):
    _, wett, _, _ = fake_corpus
    target = wett / "geenpick.md"
    _write_bron(target, qa_version="run-X", sample_pick=False)

    with pytest.raises(SystemExit) as exc:
        sr.cmd_mark_ok(str(target))
    assert "sample_pick" in str(exc.value)


def test_mark_not_ok_cascadeert_hele_batch(fake_corpus, capsys):
    _, wett, _, adv = fake_corpus
    # Batch run-X: 1 pick + 3 andere auto-trusted in dezelfde batch
    pick = wett / "pick.md"
    _write_bron(pick, qa_version="run-X", sample_pick=True, rationale="auto OK")
    other_x = [wett / "x1.md", wett / "x2.md", adv / "x3.md"]
    for p in other_x:
        _write_bron(p, qa_version="run-X", sample_pick=False, rationale="auto OK")

    # Bron in andere batch run-Y: mag NIET geraakt worden
    _write_bron(wett / "y.md", qa_version="run-Y", sample_pick=False)

    # Bron met human-confirmed: mag NIET geraakt worden
    _write_bron(wett / "human.md", qa_version="run-X", confirmed_by="human")

    sr.cmd_mark_not_ok(str(pick))

    # Pick zelf is reviewed
    pdata, _ = sr._read_frontmatter(pick)
    ptrust = sr._get_trust(pdata)
    assert ptrust["sample_reviewed_by"] == "human"
    assert ptrust["sample_reviewed_at"] is not None

    # Alle batch-X bronnen (ook de pick zelf via cascade) → status=unreviewed
    for p in [pick, *other_x]:
        d, _ = sr._read_frontmatter(p)
        t = sr._get_trust(d)
        assert t["status"] == "unreviewed", f"{p.name} is niet teruggezet"
        assert "sample_review afgekeurd" in (t.get("rationale") or "")

    # run-Y onaangetast
    yd, _ = sr._read_frontmatter(wett / "y.md")
    yt = sr._get_trust(yd)
    assert yt["status"] == "trusted"

    # human-confirmed onaangetast
    hd, _ = sr._read_frontmatter(wett / "human.md")
    ht = sr._get_trust(hd)
    assert ht["status"] == "trusted"

    out = capsys.readouterr().out
    assert "Cascade" in out
    assert "Totaal teruggezet: 4" in out  # pick + 3 anderen


def test_status_categoriseert_correct(fake_corpus, capsys):
    import os
    import time

    _, wett, _, _ = fake_corpus

    # uitstaand: pick, mtime ≤ agent_verdict_at, niet reviewed
    out_path = wett / "uitstaand.md"
    _write_bron(out_path, qa_version="run-X", sample_pick=True,
                agent_verdict_at="2030-01-01T00:00:00Z")
    # Forceer mtime in het verleden
    past = time.mktime((2020, 1, 1, 0, 0, 0, 0, 0, 0))
    os.utime(out_path, (past, past))

    # bewerkt-niet-gemerkt: pick, mtime > agent_verdict_at, niet reviewed
    edit_path = wett / "bewerkt.md"
    _write_bron(edit_path, qa_version="run-X", sample_pick=True,
                agent_verdict_at="2020-01-01T00:00:00Z")
    # mtime is "nu" → groter dan agent_verdict_at
    now = time.time()
    os.utime(edit_path, (now, now))

    # ok: reviewed + status trusted
    ok_path = wett / "ok.md"
    _write_bron(ok_path, qa_version="run-X", sample_pick=True,
                sample_reviewed_at="2026-05-09T15:00:00Z")

    # geen pick: mag niet voorkomen
    _write_bron(wett / "geenpick.md", qa_version="run-X", sample_pick=False)

    sr.cmd_status(None)
    out = capsys.readouterr().out

    assert "uitstaand" in out
    assert "bewerkt-niet-gemerkt" in out
    assert "OK" in out
    assert "geenpick.md" not in out
