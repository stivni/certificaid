"""
Tests voor `strip_norm_toc_residue` — verwijdert TOC-residu (dotted-leader-regels
+ omringende "Inhoudstafel"-header) uit ITAA-norm-MDs.

Fixtures volgen patronen uit echte affected bronnen (ITAA-norm-omzetting-
vennootschap, ITAA-norm-aww-geconsolideerd, samenstellingsopdrachten-isrs4410,
ITAA-norm-aww-richtlijn-bibf).
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl.transformers.strip_norm_toc_residue import strip_norm_toc_residue  # noqa: E402


# ─── POSITIVE: regels die wél gestript moeten worden ─────────────────────────


class TestPositiveDottedLeader:
    def test_klassieke_dotted_leader_met_4_dots(self):
        """`Toepassingsgebied .... 6` is een TOC-residu — strip."""
        body = (
            "## Inleiding\n"
            "\n"
            "Toepassingsgebied .... 6\n"
            "\n"
            "Echte inhoud volgt.\n"
        )
        new_body, _ = strip_norm_toc_residue(body, {})
        assert "Toepassingsgebied" not in new_body
        assert "Echte inhoud volgt." in new_body

    def test_klassieke_dotted_leader_met_lange_dotstring(self):
        """Lange dotted-leader uit ITAA-norm-omzetting-vennootschap."""
        body = (
            "## Inhoudstafel\n"
            "\n"
            "Toepassingsgebied ............................................. 6\n"
            "Datum van inwerkingtreding ................................... 7\n"
            "Definities ..................................................... 8\n"
            "\n"
            "## Toepassingsgebied\n"
            "\n"
            "1. Onderhavige norm is van toepassing.\n"
        )
        new_body, _ = strip_norm_toc_residue(body, {})
        assert "Toepassingsgebied .." not in new_body
        assert "Datum van inwerkingtreding .." not in new_body
        # Inhoudstafel-header zelf ook gestript
        assert "## Inhoudstafel" not in new_body
        # Echte sectie behouden
        assert "## Toepassingsgebied" in new_body
        assert "Onderhavige norm" in new_body

    def test_dashed_leader_uit_aww_geconsolideerd(self):
        """Dash-leaders (`----`) zijn een variant van dotted-leaders."""
        body = (
            "## Inhoudstafel\n"
            "\n"
            "1.\n"
            "ALGEMENE BEPALINGEN ----------------------------------- 4\n"
            "DEFINITIES --------------------------------------------- 5\n"
            "TOEPASSINGSGEBIED -------------------------------------- 6\n"
            "\n"
            "## Algemene bepalingen\n"
            "\n"
            "Hier begint de echte inhoud.\n"
        )
        new_body, _ = strip_norm_toc_residue(body, {})
        assert "ALGEMENE BEPALINGEN --" not in new_body
        assert "DEFINITIES --" not in new_body
        assert "## Inhoudstafel" not in new_body
        assert "## Algemene bepalingen" in new_body
        assert "Hier begint de echte inhoud." in new_body

    def test_drie_dots_met_paginanummer_uit_samenstellingsnorm(self):
        """`Model 3: ... 49` met slechts 3 dots — ook TOC-residu."""
        body = (
            "## Bijlage\n"
            "\n"
            "Model 1: Samenstelling van historische financiële informatie ... 47\n"
            "Model 2: Samenstellingsverslag bij prospectieve informatie ... 48\n"
            "Model 3: Samenstellingsverslag bij een liquiditeitsprognose ... 49\n"
            "\n"
            "## Inleiding\n"
        )
        new_body, _ = strip_norm_toc_residue(body, {})
        assert "Model 1:" not in new_body
        assert "Model 3:" not in new_body
        assert "## Inleiding" in new_body

    def test_inhoudstafel_header_zonder_hash_prefix(self):
        """`INHOUDSTAFEL` als plain text gevolgd door dotted-leaders."""
        body = (
            "Voorgaande tekst.\n"
            "\n"
            "INHOUDSTAFEL\n"
            "\n"
            "Hoofdstuk 1 ............ 3\n"
            "Hoofdstuk 2 ............ 7\n"
            "Hoofdstuk 3 ............ 12\n"
            "\n"
            "## Hoofdstuk 1\n"
            "\n"
            "Body.\n"
        )
        new_body, _ = strip_norm_toc_residue(body, {})
        assert "INHOUDSTAFEL" not in new_body
        assert "Hoofdstuk 1 ......" not in new_body
        assert "## Hoofdstuk 1" in new_body
        assert "Voorgaande tekst." in new_body

    def test_inhoud_als_korte_header(self):
        """`Inhoud` als plain-text header bij TOC-blok."""
        body = (
            "Aanhef.\n"
            "\n"
            "Inhoud\n"
            "Organisatie van de beroepsbeoefenaar ......... 7\n"
            "Definities ..................................... 10\n"
            "Bijlagen ....................................... 25\n"
            "\n"
            "## 1. Algemene bepalingen\n"
        )
        new_body, _ = strip_norm_toc_residue(body, {})
        assert "Organisatie van de beroepsbeoefenaar ..." not in new_body
        assert "Inhoud\n" not in new_body
        assert "## 1. Algemene bepalingen" in new_body


# ─── NEGATIVE: dingen die NIET gestript mogen worden ─────────────────────────


class TestNegativePreservation:
    def test_echte_h2_heading_blijft(self):
        """`## Toepassingsgebied` zonder dotted-leader is een echte heading."""
        body = (
            "## Toepassingsgebied\n"
            "\n"
            "Onderhavige norm is van toepassing op de verrichtingen.\n"
        )
        new_body, _ = strip_norm_toc_residue(body, {})
        assert new_body == body

    def test_body_zin_met_punten_en_cijfer_blijft(self):
        """Een echte zin met afkortingen en een cijfer mag niet als TOC tellen."""
        body = (
            "Zie K.B. van 29 april 2019.\n"
            "De wet bepaalt in art. 5:120 WVV dat het bestuursorgaan een verslag opstelt.\n"
            "Bijvoorbeeld bij omzetting in B.V., N.V., C.V., enz. is dit van toepassing op 1.\n"
        )
        new_body, _ = strip_norm_toc_residue(body, {})
        assert new_body == body

    def test_bullet_points_met_getallen_blijven(self):
        """Opsomming met cijfers eindigend op aan einde mag niet TOC zijn."""
        body = (
            "- punt een\n"
            "- punt twee\n"
            "- punt drie met paginanummer 12\n"
            "- punt vier eindigend op getal 99\n"
        )
        new_body, _ = strip_norm_toc_residue(body, {})
        assert new_body == body

    def test_lege_body_passthrough(self):
        body = ""
        new_body, _ = strip_norm_toc_residue(body, {})
        assert new_body == body

    def test_geen_dotted_leaders_geen_verandering(self):
        """Body zonder dotted-leaders blijft byte-voor-byte gelijk."""
        body = (
            "## Inleiding\n"
            "\n"
            "Dit is een norm-bron. Geen TOC-residu hier.\n"
            "\n"
            "## Vereisten\n"
            "\n"
            "1. Eerste vereiste.\n"
            "2. Tweede vereiste.\n"
        )
        new_body, _ = strip_norm_toc_residue(body, {})
        assert new_body == body

    def test_inhoudstafel_zonder_dotted_leaders_blijft_staan(self):
        """`## Inhoudstafel` met inhoudelijke tekst (geen TOC-pagina-leaders)
        mag niet onterecht gestript worden."""
        body = (
            "## Inhoudstafel\n"
            "\n"
            "De inhoudstafel van dit document is opgenomen als bijlage 1.\n"
            "Zie bijlage 1 voor details.\n"
            "\n"
            "## Sectie 2\n"
        )
        new_body, _ = strip_norm_toc_residue(body, {})
        # Geen dotted-leaders → header blijft, geen wijziging
        assert "## Inhoudstafel" in new_body
        assert "De inhoudstafel van dit document" in new_body

    def test_enkele_dotted_leader_zonder_cluster_blijft(self):
        """Eén losse dotted-leader-regel zonder TOC-context blijft staan —
        kan een legitieme invul-stippellijn zijn (bv. `voor de som van .......`)."""
        body = (
            "## Sectie\n"
            "\n"
            "De vergoeding bedraagt ............ euro per maand.\n"
            "\n"
            "Echte body daarna.\n"
        )
        new_body, _ = strip_norm_toc_residue(body, {})
        # 1 losse leader, geen cluster, geen Inhoudstafel-header → behouden
        assert "............ euro" in new_body


# ─── IDEMPOTENTIE ────────────────────────────────────────────────────────────


class TestIdempotentie:
    def test_dubbele_pass_zelfde_output(self):
        """Twee keer toepassen geeft hetzelfde resultaat als één keer."""
        body = (
            "## Inhoudstafel\n"
            "\n"
            "Sectie 1 ............ 3\n"
            "Sectie 2 ............ 7\n"
            "Sectie 3 ............ 12\n"
            "\n"
            "## Sectie 1\n"
            "\n"
            "Body.\n"
        )
        first, _ = strip_norm_toc_residue(body, {})
        second, _ = strip_norm_toc_residue(first, {})
        assert first == second


# ─── FRONTMATTER passthrough ──────────────────────────────────────────────────


class TestFrontmatterPassthrough:
    def test_frontmatter_unchanged(self):
        body = "## Inhoudstafel\n\nA ........ 1\nB ........ 2\nC ........ 3\n\n## A\nBody.\n"
        fm = {"wet": "Test-norm", "tags": ["foo"]}
        _, new_fm = strip_norm_toc_residue(body, fm)
        assert new_fm == {"wet": "Test-norm", "tags": ["foo"]}
