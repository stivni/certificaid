"""Tests voor `tools/etl/diff_review.py` (Laag 1.5 regressie-diff)."""
from __future__ import annotations

import json
import sys
import textwrap
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl import diff_review as dr  # noqa: E402


def _make_md(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


# ─── Test 1: print-prompt — auto no_op voor nieuwe bron + diff-blok voor bestaande ──

def test_print_prompt_separates_new_and_diff(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    staging = tmp_path / "staging"
    head_root = tmp_path / "resources" / "bronnen" / "wetteksten"
    output = tmp_path / "out.md"

    # Bron 1: bestaat in HEAD én in staging, met verschil
    _make_md(staging / "BronA.md", "# A\n\nNieuwe inhoud regel.\n")
    _make_md(head_root / "BronA.md", "# A\n\nOude inhoud regel.\n")

    # Bron 2: alleen in staging (nieuwe bron) → auto no_op
    _make_md(staging / "BronNieuw.md", "# Nieuw\n\nContent.\n")

    # Bron 3: bestaat in HEAD, identiek aan staging → auto no_op
    identical_body = "# C\n\nIdentiek.\n"
    _make_md(staging / "BronC.md", identical_body)
    _make_md(head_root / "BronC.md", identical_body)

    # Patch ROOT en config-loader: lege config zodat fallback op
    # resources/bronnen/wetteksten/<naam> gebruikt wordt
    monkeypatch.setattr(dr, "ROOT", tmp_path)
    monkeypatch.setattr(dr, "load_config", lambda: {})

    args = type("Args", (), {
        "staging_dir": staging,
        "bron": None,
        "out": output,
        "run_id": "TEST-RUN",
        "print_prompt": True,
        "apply_verdicts": None,
    })()
    dr.cmd_print_prompt(args)

    prompt = output.read_text(encoding="utf-8")
    assert "TEST-RUN" in prompt
    assert "BronA.md" in prompt
    assert "```diff" in prompt
    # BronNieuw en BronC krijgen geen diff-blok in de prompt
    assert "## Bestand: " in prompt
    # Slechts één diff-blok (BronA); de andere twee zijn auto-no_op
    assert prompt.count("## Bestand: ") == 1

    # Auto-verdicts-bestand bevat BronNieuw en BronC met no_op
    auto_path = output.with_suffix(".auto-verdicts.json")
    auto_data = json.loads(auto_path.read_text(encoding="utf-8"))
    bestanden = {v["bestand"] for v in auto_data["verdicts"]}
    assert any("BronNieuw.md" in b for b in bestanden)
    assert any("BronC.md" in b for b in bestanden)
    assert all(v["diff_verdict"] == "no_op" for v in auto_data["verdicts"])


# ─── Test 2: apply-verdicts — parse, valideer, schrijf canonical ───────────────

def test_apply_verdicts_parses_and_writes_canonical(tmp_path: Path) -> None:
    # Subagent-output in mixed format: één JSON-array met markdown-fence eromheen
    subagent_out = tmp_path / "subagent.txt"
    subagent_out.write_text(textwrap.dedent("""\
        ```json
        [
          {
            "bestand": "data/etl-staging/B.md",
            "diff_verdict": "improvement",
            "rationale": "Artefacten weg.",
            "kritieke_observaties": []
          },
          {
            "bestand": "data/etl-staging/A.md",
            "diff_verdict": "regression",
            "rationale": "Artikel weg.",
            "kritieke_observaties": ["Art. 5 ontbreekt"]
          }
        ]
        ```
    """), encoding="utf-8")

    out = tmp_path / "verdicts.json"

    args = type("Args", (), {
        "apply_verdicts": subagent_out,
        "out": out,
        "run_id": "RUN1",
        "merge_auto": None,
    })()
    dr.cmd_apply_verdicts(args)

    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["run_id"] == "RUN1"
    # Sortering op bestand: A komt voor B
    bestanden = [v["bestand"] for v in data["verdicts"]]
    assert bestanden == sorted(bestanden)
    assert data["totals"]["improvement"] == 1
    assert data["totals"]["regression"] == 1

    # Idempotentie: tweede run met zelfde input + run-id = identiek bestand
    out2 = tmp_path / "verdicts2.json"
    args2 = type("Args", (), {
        "apply_verdicts": subagent_out,
        "out": out2,
        "run_id": "RUN1",
        "merge_auto": None,
    })()
    dr.cmd_apply_verdicts(args2)
    assert out.read_text(encoding="utf-8") == out2.read_text(encoding="utf-8")


# ─── Test 3: validatie weigert ongeldige verdicts ─────────────────────────────

def test_validate_rejects_invalid_verdict_value() -> None:
    bad = [{"bestand": "x.md", "diff_verdict": "huh"}]
    errors = dr.validate_verdicts(bad)
    assert any("diff_verdict" in e for e in errors)


def test_validate_rejects_duplicate_bestand() -> None:
    dup = [
        {"bestand": "x.md", "diff_verdict": "improvement"},
        {"bestand": "x.md", "diff_verdict": "no_op"},
    ]
    errors = dr.validate_verdicts(dup)
    assert any("duplicate" in e for e in errors)
