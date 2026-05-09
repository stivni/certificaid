"""Tests voor `tools/etl/promote_staging.py` (ADR-005 §5 Laag-3 promotie).

Werkt volledig in pytest tmp_path; raakt resources/bronnen niet aan.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl import promote_staging as ps  # noqa: E402


# ─── Fixtures ────────────────────────────────────────────────────────────────

def _staging_md(
    path: Path,
    *,
    bron_rol: str = "itaa_lex",
    titel: str = "Fixture-bron",
    body: str = "# Fixture\n\nLichaam.\n",
) -> None:
    """Schrijf een staging-MD met minimale frontmatter incl. trust-blok unreviewed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fm = (
        "---\n"
        f"titel: {titel}\n"
        f"bron_rol: {bron_rol}\n"
        "tags: []\n"
        "chunk:\n"
        "  level: 6\n"
        "  type: \"Art.\"\n"
        "  sub_strategy:\n"
        "provenance:\n"
        "  inputs:\n"
        "    - id: dummy.pdf\n"
        "      sha256: abc123\n"
        "  tooling:\n"
        "    pipeline: tools/etl/dummy.py\n"
        "    pipeline_version: deadbee\n"
        "  generated_at: '2026-05-01T09:00:00Z'\n"
        "  stale: false\n"
        "  stale_reason:\n"
        "  trust:\n"
        "    status: unreviewed\n"
        "    qa_version:\n"
        "    confirmed_at:\n"
        "    confirmed_by: default\n"
        "    rationale:\n"
        "---\n"
    )
    path.write_text(fm + body, encoding="utf-8")


def _write_qa(path: Path, run_id: str, entries: dict[str, str]) -> None:
    """Schrijf qa_bron.py-achtig rapport. entries = {bestandsnaam: verdict}."""
    path.parent.mkdir(parents=True, exist_ok=True)
    bronnen = [
        {
            "bestand": f"data/etl-staging/{name}",
            "bron_rol": "itaa_lex",
            "file_size_chars": 100,
            "heading_count": 5,
            "max_section_chars": 50,
            "verdict": verdict,
            "checks": [],
        }
        for name, verdict in entries.items()
    ]
    rapport = {"run": {"id": run_id}, "totals": {}, "bronnen": bronnen}
    path.write_text(json.dumps(rapport, indent=2), encoding="utf-8")


def _write_diff(path: Path, run_id: str, entries: dict[str, str]) -> None:
    """Schrijf diff_review.py canonical-format. entries = {bestand: verdict}."""
    path.parent.mkdir(parents=True, exist_ok=True)
    verdicts = [
        {
            "bestand": f"data/etl-staging/{name}",
            "diff_verdict": v,
            "rationale": f"test {v}",
            "kritieke_observaties": [],
            "auto": False,
        }
        for name, v in entries.items()
    ]
    payload = {"run_id": run_id, "verdicts": verdicts, "totals": {}}
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _write_content(path: Path, run_id: str, entries: dict[str, str]) -> None:
    """Schrijf Laag-2 content-verdicts. entries = {bestand: aanbevolen_status}."""
    path.parent.mkdir(parents=True, exist_ok=True)
    verdicts = [
        {
            "bestand": f"data/etl-staging/{name}",
            "aanbevolen_status": v,
            "rationale": f"content {v}",
            "concrete_problemen": [],
            "concrete_sterke_punten": [],
        }
        for name, v in entries.items()
    ]
    payload = {"run_id": run_id, "verdicts": verdicts}
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


@pytest.fixture
def workspace(tmp_path: Path):
    """Maak een tmp_path-gebaseerde 'project root' met staging + resources/bronnen."""
    staging = tmp_path / "data" / "etl-staging"
    resources = tmp_path / "resources" / "bronnen"
    qa_dir = tmp_path / "data" / "qa"
    staging.mkdir(parents=True)
    (resources / "wetteksten").mkdir(parents=True)
    (resources / "normen").mkdir(parents=True)
    (resources / "adviezen").mkdir(parents=True)
    qa_dir.mkdir(parents=True)
    return tmp_path, staging, resources, qa_dir


# ─── Test 1: combine_verdicts dekt alle tabel-rijen ──────────────────────────

def test_combine_verdicts_alle_tabelrijen():
    cv = ps.combine_verdicts

    # Auto-trust
    assert cv("pass", "improvement", "trusted")[0] == "auto-trust"
    assert cv("pass", "no_op", "trusted")[0] == "auto-trust"

    # Review-pending
    assert cv("pass", "structural_change", "trusted")[0] == "review-pending"
    assert cv("warn", "improvement", "trusted")[0] == "review-pending"
    assert cv("warn", "structural_change", "trusted")[0] == "review-pending"

    # Blocked: regression / fail / needs-rework / rejected
    assert cv("pass", "regression", "trusted")[0] == "blocked"
    assert cv("fail", "improvement", "trusted")[0] == "blocked"
    assert cv("pass", "improvement", "needs-rework")[0] == "blocked"
    assert cv("pass", "improvement", "rejected")[0] == "blocked"

    # Content ontbreekt: trusted-equivalent alleen bij pass + improvement/no_op/None
    assert cv("pass", "improvement", None)[0] == "auto-trust"
    assert cv("pass", "no_op", None)[0] == "auto-trust"
    assert cv("pass", None, None)[0] == "auto-trust"
    assert cv("warn", "improvement", None)[0] == "blocked"
    assert cv("pass", "structural_change", None)[0] == "blocked"


# ─── Test 2: end-to-end promote met gemixte verdicts ─────────────────────────

def test_promote_end_to_end_mixed(workspace):
    tmp_root, staging, resources, qa_dir = workspace

    # 4 bronnen: auto-trust, review-pending (warn), review-pending (struct),
    # blocked (regression). Allemaal bron_rol=itaa_lex → wetteksten/.
    _staging_md(staging / "auto.md", bron_rol="itaa_lex")
    _staging_md(staging / "warn.md", bron_rol="itaa_lex")
    _staging_md(staging / "struct.md", bron_rol="itaa_lex")
    _staging_md(staging / "regress.md", bron_rol="itaa_lex")

    qa_path = qa_dir / "RUN1.json"
    diff_path = qa_dir / "RUN1-diff.json"
    content_path = qa_dir / "RUN1-content.json"

    _write_qa(qa_path, "RUN1", {
        "auto.md": "pass",
        "warn.md": "warn",
        "struct.md": "pass",
        "regress.md": "pass",
    })
    _write_diff(diff_path, "RUN1", {
        "auto.md": "improvement",
        "warn.md": "no_op",
        "struct.md": "structural_change",
        "regress.md": "regression",
    })
    _write_content(content_path, "RUN1", {
        "auto.md": "trusted",
        "warn.md": "trusted",
        "struct.md": "trusted",
        "regress.md": "trusted",
    })

    rapport = ps.promote(
        run_id="RUN1",
        qa_path=qa_path,
        diff_path=diff_path,
        content_path=content_path,
        staging_dir=staging,
        resources_dir=resources,
        qa_dir=qa_dir,
        config_path=tmp_root / "nonexistent.yaml",
        timestamp="2026-05-09T14:00:00Z",
        project_root=tmp_root,
    )

    assert rapport["auto_trusted"] == ["auto.md"]
    assert sorted(rapport["review_pending"]) == ["struct.md", "warn.md"]
    assert [b["bron"] for b in rapport["blocked"]] == ["regress.md"]

    # auto.md is gepromoot naar wetteksten/auto.md met sample_pick=false
    auto_dest = resources / "wetteksten" / "auto.md"
    assert auto_dest.exists()
    data, _ = ps._read_frontmatter(auto_dest)
    trust = data["provenance"]["trust"]
    assert trust["status"] == "trusted"
    assert trust["sample_pick"] is False
    assert trust["qa_version"] == "RUN1"
    assert trust["agent_verdict_at"] == "2026-05-09T14:00:00Z"
    assert trust["sample_reviewed_at"] is None
    assert trust["sample_reviewed_by"] is None
    assert "L1=pass" in trust["rationale"]
    assert "L2=trusted" in trust["rationale"]

    # warn.md is gepromoot met sample_pick=true (review-pending)
    warn_dest = resources / "wetteksten" / "warn.md"
    assert warn_dest.exists()
    wdata, _ = ps._read_frontmatter(warn_dest)
    wtrust = wdata["provenance"]["trust"]
    assert wtrust["status"] == "trusted"
    assert wtrust["sample_pick"] is True

    # struct.md ook review-pending
    struct_dest = resources / "wetteksten" / "struct.md"
    assert struct_dest.exists()
    sdata, _ = ps._read_frontmatter(struct_dest)
    assert sdata["provenance"]["trust"]["sample_pick"] is True

    # regress.md is NIET gepromoot
    assert not (resources / "wetteksten" / "regress.md").exists()
    # ... maar staat nog wel in staging
    assert (staging / "regress.md").exists()

    # Result-rapport en blocked-bestand zijn geschreven
    assert (qa_dir / "RUN1-promote-result.json").exists()
    blocked_data = json.loads((qa_dir / "RUN1-blocked.json").read_text(encoding="utf-8"))
    assert blocked_data["run_id"] == "RUN1"
    assert blocked_data["blocked"][0]["bron"] == "regress.md"
    assert "regression" in blocked_data["blocked"][0]["reden"]


# ─── Test 3: idempotentie ────────────────────────────────────────────────────

def test_promote_is_idempotent(workspace):
    tmp_root, staging, resources, qa_dir = workspace

    _staging_md(staging / "auto.md", bron_rol="itaa_lex")
    _staging_md(staging / "regress.md", bron_rol="itaa_lex")

    qa_path = qa_dir / "RUN2.json"
    diff_path = qa_dir / "RUN2-diff.json"

    _write_qa(qa_path, "RUN2", {"auto.md": "pass", "regress.md": "pass"})
    _write_diff(diff_path, "RUN2", {
        "auto.md": "improvement",
        "regress.md": "regression",
    })

    common = dict(
        run_id="RUN2",
        qa_path=qa_path,
        diff_path=diff_path,
        content_path=None,
        staging_dir=staging,
        resources_dir=resources,
        qa_dir=qa_dir,
        config_path=tmp_root / "nonexistent.yaml",
        timestamp="2026-05-09T14:00:00Z",
        project_root=tmp_root,
    )

    rapport_a = ps.promote(**common)
    promoted = resources / "wetteksten" / "auto.md"
    bytes_a = promoted.read_bytes()
    result_a = (qa_dir / "RUN2-promote-result.json").read_text(encoding="utf-8")
    blocked_a = (qa_dir / "RUN2-blocked.json").read_text(encoding="utf-8")

    rapport_b = ps.promote(**common)
    bytes_b = promoted.read_bytes()
    result_b = (qa_dir / "RUN2-promote-result.json").read_text(encoding="utf-8")
    blocked_b = (qa_dir / "RUN2-blocked.json").read_text(encoding="utf-8")

    assert rapport_a == rapport_b
    assert bytes_a == bytes_b
    assert result_a == result_b
    assert blocked_a == blocked_b


# ─── Test 4: bron-rol-pad-mapping en source_config-override ──────────────────

def test_resolve_destination_via_source_config(workspace, tmp_path):
    tmp_root, staging, resources, _ = workspace

    # source_config met expliciet output: pad
    source_config = {
        "MyBron": {
            "bron_rol": "interpretatief",
            "output": "resources/bronnen/normen/Aangepaste-Naam.md",
        },
    }

    staging_md = staging / "Aangepaste-Naam.md"
    _staging_md(staging_md, bron_rol="interpretatief")

    dest = ps._resolve_destination(
        staging_md, source_config, "interpretatief",
        resources_root=resources,
        project_root=tmp_root,
    )
    assert dest == resources / "normen" / "Aangepaste-Naam.md"


def test_resolve_destination_fallback_op_bron_rol(workspace):
    tmp_root, staging, resources, _ = workspace

    # Geen source_config-match → fallback op bron_rol
    cases = [
        ("itaa_lex", "wetteksten"),
        ("normatief", "wetteksten"),
        ("praktijkgids", "wetteksten"),
        ("formulier", "wetteksten"),
        ("interpretatief", "normen"),  # geen advies-prefix
    ]
    for rol, expected_sub in cases:
        f = staging / f"X-{rol}.md"
        _staging_md(f, bron_rol=rol)
        dest = ps._resolve_destination(
            f, {}, rol,
            resources_root=resources,
            project_root=tmp_root,
        )
        assert dest == resources / expected_sub / f.name, f"rol={rol}"

    # Interpretatief met advies-prefix → adviezen/
    advies_md = staging / "advies-2024-01.md"
    _staging_md(advies_md, bron_rol="interpretatief")
    dest_advies = ps._resolve_destination(
        advies_md, {}, "interpretatief",
        resources_root=resources,
        project_root=tmp_root,
    )
    assert dest_advies == resources / "adviezen" / "advies-2024-01.md"


# ─── Test 5: dry-run schrijft niets ──────────────────────────────────────────

def test_promote_dry_run_schrijft_niets(workspace):
    tmp_root, staging, resources, qa_dir = workspace

    _staging_md(staging / "auto.md", bron_rol="itaa_lex")
    qa_path = qa_dir / "RUN3.json"
    diff_path = qa_dir / "RUN3-diff.json"
    _write_qa(qa_path, "RUN3", {"auto.md": "pass"})
    _write_diff(diff_path, "RUN3", {"auto.md": "improvement"})

    rapport = ps.promote(
        run_id="RUN3",
        qa_path=qa_path,
        diff_path=diff_path,
        content_path=None,
        staging_dir=staging,
        resources_dir=resources,
        qa_dir=qa_dir,
        config_path=tmp_root / "nonexistent.yaml",
        dry_run=True,
        timestamp="2026-05-09T14:00:00Z",
        project_root=tmp_root,
    )

    assert rapport["auto_trusted"] == ["auto.md"]
    assert not (resources / "wetteksten" / "auto.md").exists()
    assert not (qa_dir / "RUN3-promote-result.json").exists()
