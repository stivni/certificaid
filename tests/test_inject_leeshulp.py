"""Tests voor `tools.leermateriaal.inject_leeshulp` (ADR-034)."""

from __future__ import annotations

import pytest

from tools.leermateriaal.inject_leeshulp import (
    Callout,
    cmd_check,
    inject,
    parse_leeshulp,
    split_frontmatter,
)


# ────────────────────────────────────────────────────────────────────────────
# split_frontmatter
# ────────────────────────────────────────────────────────────────────────────


class TestSplitFrontmatter:
    def test_basic_split(self):
        text = "---\nfoo: bar\n---\n# Heading\nbody\n"
        fm, body = split_frontmatter(text)
        assert fm == "---\nfoo: bar\n---\n"
        assert body == "# Heading\nbody\n"

    def test_no_frontmatter(self):
        text = "# Just a heading\nbody\n"
        fm, body = split_frontmatter(text)
        assert fm == ""
        assert body == text

    def test_unclosed_frontmatter(self):
        text = "---\nfoo: bar\n# never closed\n"
        fm, body = split_frontmatter(text)
        assert fm == ""
        assert body == text


# ────────────────────────────────────────────────────────────────────────────
# parse_leeshulp
# ────────────────────────────────────────────────────────────────────────────


class TestParseLeeshulp:
    def test_intro_and_na(self):
        text = (
            "---\nvoor: X\n---\n\n"
            "# Leeshulp-titel\n\n"
            "Wat beschrijvende tekst die wordt genegeerd.\n\n"
            "## @intro\n\n"
            "> [!info] hallo\n\n"
            '## @na "## 2. Verslag"\n\n'
            "> [!tip] kijk uit\n"
        )
        callouts = parse_leeshulp(text)
        assert len(callouts) == 2
        assert callouts[0] == Callout(directive="intro", arg=None, body="> [!info] hallo")
        assert callouts[1].directive == "na"
        assert callouts[1].arg == "## 2. Verslag"
        assert callouts[1].body == "> [!tip] kijk uit"

    def test_empty(self):
        assert parse_leeshulp("---\nfoo: bar\n---\n\nGeen anchors hier.\n") == []


# ────────────────────────────────────────────────────────────────────────────
# inject
# ────────────────────────────────────────────────────────────────────────────


BRON_MIN = (
    "---\ntags: [x]\n---\n"
    "# H1 titel\n\n"
    "## 1. Eerst\n"
    "tekst van sectie 1.\n"
    "## 2. Tweede\n"
    "tekst van sectie 2.\n"
    "meer tekst.\n"
    "## 3. Derde\n"
    "laatste sectie.\n"
)


class TestInject:
    def test_no_leeshulp_is_passthrough(self):
        assert inject(BRON_MIN, None) == BRON_MIN

    def test_empty_leeshulp_is_passthrough(self):
        leeshulp = "---\nvoor: x\n---\n\nGeen anchors.\n"
        assert inject(BRON_MIN, leeshulp, "x") == BRON_MIN

    def test_intro_only(self):
        leeshulp = (
            "---\nvoor: x\n---\n\n## @intro\n\n> [!info] intro-callout\n"
        )
        out = inject(BRON_MIN, leeshulp, "resources/leeshulp/x.md")
        # Frontmatter staat vooraan
        assert out.startswith("---\ntags: [x]\n---\n")
        # HTML-marker verwijst naar leeshulp-pad
        assert "<!-- LEESHULP-INJECT: bron=resources/leeshulp/x.md (ADR-034) -->" in out
        # Callout staat vóór de H1
        marker_idx = out.find("LEESHULP-INJECT")
        callout_idx = out.find("> [!info] intro-callout")
        h1_idx = out.find("# H1 titel")
        assert marker_idx < callout_idx < h1_idx

    def test_na_middle_section(self):
        leeshulp = (
            "---\nvoor: x\n---\n\n"
            '## @na "## 2. Tweede"\n\n'
            "> [!tip] na sectie 2\n"
        )
        out = inject(BRON_MIN, leeshulp, "x")
        # De callout staat NA de inhoud van §2 maar VÓÓR §3
        sectie2_einde = out.find("meer tekst.")
        callout = out.find("> [!tip] na sectie 2")
        sectie3 = out.find("## 3. Derde")
        assert sectie2_einde < callout < sectie3
        # Originele bron-tekst is intact gebleven
        assert "tekst van sectie 2.\nmeer tekst.\n" in out

    def test_na_last_section_eof(self):
        leeshulp = (
            "---\nvoor: x\n---\n\n"
            '## @na "## 3. Derde"\n\n'
            "> [!warning] eof-callout\n"
        )
        out = inject(BRON_MIN, leeshulp, "x")
        # Callout staat NA de inhoud van §3 en file eindigt met newline
        assert out.endswith("> [!warning] eof-callout\n")
        assert "laatste sectie.\n\n> [!warning] eof-callout\n" in out

    def test_unknown_heading_raises(self):
        leeshulp = (
            "---\nvoor: x\n---\n\n"
            '## @na "## 999. Bestaat niet"\n\n'
            "> [!info] zal niet werken\n"
        )
        with pytest.raises(ValueError, match="niet gevonden"):
            inject(BRON_MIN, leeshulp, "x")

    def test_unknown_directive_raises(self):
        leeshulp = (
            "---\nvoor: x\n---\n\n"
            "## @bogus\n\n"
            "> [!info] verkeerd\n"
        )
        with pytest.raises(ValueError, match="Onbekend leeshulp-directive"):
            inject(BRON_MIN, leeshulp, "x")


# ────────────────────────────────────────────────────────────────────────────
# Pre-commit gate: idempotentie van de bestaande content/-versies
# ────────────────────────────────────────────────────────────────────────────


def test_content_bronnen_in_sync_met_leeshulp():
    """Pre-commit gate: alle bronnen-met-leeshulp moeten gesynced zijn in `content/`.

    Faalt? → `python3 -m tools.leermateriaal.inject_leeshulp inject-all`.
    """
    assert cmd_check(only_with_leeshulp=True) == 0, (
        "content/bronnen/-versies out-of-sync met inject(bron, leeshulp); "
        "run: python3 -m tools.leermateriaal.inject_leeshulp inject-all"
    )
