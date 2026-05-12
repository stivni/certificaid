"""Unit-tests voor de `md_passthrough` extractor."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.lib.extractors.md_passthrough import extract  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures" / "md_passthrough"


def _make_fixture(name: str, content: str) -> Path:
    """Maak een raw-fixture in tests/fixtures/md_passthrough/."""
    FIXTURES.mkdir(parents=True, exist_ok=True)
    p = FIXTURES / name
    p.write_text(content, encoding="utf-8")
    return p


def test_extract_reads_plain_body():
    """Plain markdown zonder frontmatter wordt onveranderd teruggegeven."""
    p = _make_fixture("plain.md", "# Mijn bron\n\nDit is de body.\n")
    try:
        cfg = {"raw": str(p.relative_to(ROOT))}
        result = extract(cfg, "plain")
        assert result == "# Mijn bron\n\nDit is de body.\n"
    finally:
        p.unlink()


def test_extract_strips_existing_frontmatter():
    """Als raw zelf YAML-frontmatter bevat, wordt die gestript."""
    p = _make_fixture(
        "with_fm.md",
        "---\ntitle: 'Test'\nfoo: bar\n---\n\n# Body start\n\nInhoud.\n",
    )
    try:
        cfg = {"raw": str(p.relative_to(ROOT))}
        body = extract(cfg, "with_fm")
        assert body.startswith("# Body start")
        assert "title:" not in body
        assert "Inhoud." in body
    finally:
        p.unlink()


def test_extract_raises_when_raw_missing():
    """ValueError als 'raw'-veld ontbreekt."""
    with pytest.raises(ValueError, match="raw"):
        extract({}, "test")


def test_extract_raises_when_raw_empty():
    """ValueError als 'raw'-veld leeg is."""
    with pytest.raises(ValueError, match="raw"):
        extract({"raw": ""}, "test")


def test_extract_raises_when_file_not_found():
    """FileNotFoundError als raw niet bestaat."""
    with pytest.raises(FileNotFoundError):
        extract({"raw": "tests/fixtures/md_passthrough/__nope__.md"}, "test")
