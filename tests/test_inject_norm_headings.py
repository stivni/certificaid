"""Tests voor de two-column-glitch fix in `tools.etl.inject_norm_headings`.

De NL-kolom-extractor (`extract_nl_column`) verliest in sommige BeExcellent
twee-kolom PDFs (zoals ITAA-norm-aww-geconsolideerd) de losse sectie-titel-
regels: `1.\nALGEMENE BEPALINGEN ----- 4` in de TOC, maar in de body
verschijnt `1. Algemene bepalingen` wél, terwijl `2. Organisatie en interne
controle`, `3. ...`, `4. ...`, `6. ...`, `9. ...`, `10. ...` verdwenen zijn.
De subsecties (`2.1.`, `2.2.`, …) staan dan zonder voorafgaande `## N. titel`-
heading in de body.

Daarnaast komen sommige sectie-koppen inline mee met body-text: `7. Beperkingen
van het gebruik van contanten Wanneer de beroepsbeoefenaar weet, ...` — heading
en body op één regel.

De fix combineert twee passes vóór de bestaande Pattern A:

  1. TOC-parse → ``{section_num: TitleCase}``.
  2. Walk de body; injecteer voor elke ``N.x.`` subsectie de bijbehorende
     ``N. <TitleCase>`` regel als die nog niet gezien is. Splits ook inline
     ``N. <Title> Body...`` regels.
"""
from __future__ import annotations

from tools.etl.inject_norm_headings import inject_headings


# ─── Fixtures: minimale reproducties uit ITAA-norm-aww-geconsolideerd ────────


_TOC_FIXTURE = """## Inhoudstafel

1.
ALGEMENE BEPALINGEN ----------------------------------------------------------------------------------------------------------- 4

2.
ORGANISATIE EN INTERNE CONTROLE ----------------------------------------------------------------------------------------- 5

3.
ALGEMENE RISICOBEOORDELING OP TE MAKEN DOOR DE BEROEPSBEOEFENAAR ------------------------------ 7

4.
WAAKZAAMHEID TEN AANZIEN VAN DE CLIËNTEN EN DE VERRICHTINGEN --------------------------------------- 8

5.
ONDERZOEK VAN DE VERRICHTINGEN ---------------------------------------------------------------------------------------- 11

6.
DOCUMENTATIE EN BEWARING VAN DOCUMENTEN -------------------------------------------------------------------- 11

7.
BEPERKINGEN VAN HET GEBRUIK VAN CONTANTEN --------------------------------------------------------------------- 12

8.
TOEZICHT EN CONTROLE ---------------------------------------------------------------------------------------------------------- 12

9.
OVERGANGSBEPALINGEN (NIET MEER VAN TOEPASSING) ------------------------------------------------------------- 12

10.
SLOTBEPALINGEN ---------------------------------------------------------------------------------------------------------------- 12

"""


# ─── Test 1: missende parent-section vóór subsectie 2.x ──────────────────────


def test_inject_norm_headings_synthetiseert_missing_parent_section_2():
    """Bug: bij two-column PDFs ontbreekt de regel `2. Organisatie en interne
    controle` in de body. Subsecties (`2.1.`, `2.2.`) volgen direct op
    `1.x` zonder dat de parent-heading ooit wordt gepromoveerd.

    Fix: gebruik de TOC om te zien dat sectie 2 bestaat en de titel
    'Organisatie en interne controle' draagt, en injecteer de heading vlak
    voor de eerste subsectie.
    """
    body = _TOC_FIXTURE + (
        "1. Algemene bepalingen\n"
        "\n"
        "Definities 1.1. Voor de toepassing van deze norm ...\n"
        "\n"
        "1.2. Voor het overige ...\n"
        "\n"
        "2.1. Elke beroepsbeoefenaar, die rechtspersoon is, moet ...\n"
        "\n"
        "2.2. Elke beroepsbeoefenaar moet een AMLCO aanduiden.\n"
    )

    out = inject_headings(body, filename="ITAA-norm-aww-geconsolideerd.md")

    assert "## 1. Algemene bepalingen" in out
    assert "## 2. Organisatie en interne controle" in out, (
        "Sectie 2 ontbreekt — TOC-fallback heeft niet gewerkt"
    )


def test_inject_norm_headings_synthetiseert_missing_parent_section_3_en_4():
    """Sectie 3 en 4 hebben dezelfde glitch (zelfs zonder eigen standalone
    regel zoals sectie 5). De fix moet beide synthetiseren."""
    body = _TOC_FIXTURE + (
        "1. Algemene bepalingen\n"
        "\n"
        "Definities 1.1. ...\n"
        "\n"
        "2.1. ...\n"
        "\n"
        "3.3.\n"
        "De algemene risicobeoordeling wordt bepaald en uitgevoerd ...\n"
        "\n"
        "3.4.\n"
        "De beroepsbeoefenaar documenteert ...\n"
        "\n"
        "4.2.\n"
        "Het cliëntacceptatiebeleid bepaalt ...\n"
    )

    out = inject_headings(body, filename="ITAA-norm-aww-geconsolideerd.md")

    assert "## 2. Organisatie en interne controle" in out
    assert "## 3. Algemene risicobeoordeling op te maken door de beroepsbeoefenaar" in out
    assert "## 4. Waakzaamheid ten aanzien van de cliënten en de verrichtingen" in out


def test_inject_norm_headings_splits_inline_section_heading():
    """Sectie 7 verschijnt inline met body: `7. Beperkingen van het gebruik
    van contanten Wanneer de beroepsbeoefenaar weet, ...`. De fix splitst
    de regel zodat alleen de heading-titel als ## promoveert en de body
    behouden blijft.
    """
    body = _TOC_FIXTURE + (
        "1. Algemene bepalingen\n"
        "\n"
        "Definities 1.1. ...\n"
        "\n"
        "7. Beperkingen van het gebruik van contanten Wanneer de "
        "beroepsbeoefenaar weet, vermoedt of redelijke gronden heeft om te "
        "vermoeden dat feiten of verrichtingen verband houden met het WG/FT "
        "dient hij dit vermoeden onmiddellijk te melden aan de CFI.\n"
        "\n"
        "8. Toezicht en controle Teneinde de Toezichtautoriteit toe te laten de\n"
    )

    out = inject_headings(body, filename="ITAA-norm-aww-geconsolideerd.md")

    assert "## 7. Beperkingen van het gebruik van contanten" in out
    assert "## 8. Toezicht en controle" in out
    # Body-content na de heading moet bewaard blijven
    assert "Wanneer de beroepsbeoefenaar weet" in out
    assert "Teneinde de Toezichtautoriteit" in out


def test_inject_norm_headings_promoot_alleen_geldige_toc_secties():
    """Pre-condition voor de fix: geen sectie-anchors synthetiseren voor
    subsecties wiens parent-N niet in de TOC staat. We willen geen valse
    `## 11. ...`-injecties.
    """
    body = (
        # TOC met alleen secties 1-3
        "## Inhoudstafel\n\n"
        "1.\nALGEMENE ---------- 4\n\n"
        "2.\nORGANISATIE ---------- 5\n\n"
        "3.\nRISICO ---------- 7\n\n"
        # Body: subsectie 99.1. (nepnummer dat niet in TOC voorkomt)
        "1. Algemene bepalingen\n\n"
        "99.1. Onbestaande subsectie.\n"
    )

    out = inject_headings(body, filename="ITAA-norm-aww-geconsolideerd.md")

    # Sectie 99 staat niet in de TOC → geen synthetische heading
    assert "## 99." not in out


def test_inject_norm_headings_overrride_vult_glitched_toc_titel():
    """Als de NL-kolom-extractie een TOC-titel volledig verloor (de regel
    `4.` staat in de body maar de volgende regel is blank i.p.v. de titel),
    moet de file-specifieke override-map de gap vullen.

    Concreet voor ITAA-norm-aww-geconsolideerd: sectie 4 = 'Waakzaamheid
    ten aanzien van de cliënten en de verrichtingen'.
    """
    # TOC waarin sectie 4 een glitched titel heeft (blank ipv title-regel)
    body = (
        "## Inhoudstafel\n\n"
        "1.\nALGEMENE BEPALINGEN ---------- 4\n\n"
        "4.\n\n"
        "CLIENTACCEPTATIEBELEID ---------- 8\n"
        "IDENTIFICATIEVERPLICHTING ---------- 9\n\n"
        # Body
        "1. Algemene bepalingen\n\n"
        "1.1. ...\n\n"
        "4.2.\nHet cliëntacceptatiebeleid bepaalt ...\n"
    )

    out = inject_headings(body, filename="ITAA-norm-aww-geconsolideerd.md")

    # Override moet de TOC-glitch overrulen
    assert "## 4. Waakzaamheid ten aanzien van de cliënten en de verrichtingen" in out
    # En NIET het subsectie-niveau als heading nemen
    assert "## 4. Clientacceptatiebeleid" not in out


def test_inject_norm_headings_splits_inline_bijlage_heading():
    """Bijlage IV verschijnt in AWW-geconsolideerd inline met body-text:
    `BIJLAGE IV: Beslissingsbomen ter illustratie Elk kantoor is ertoe...`.
    De fix moet Bijlage + titel als ## promoveren en de body-rest bewaren.
    """
    body = _TOC_FIXTURE + (
        "1. Algemene bepalingen\n\n"
        "1.1. ...\n\n"
        "BIJLAGE IV: Beslissingsbomen ter illustratie Elk kantoor is ertoe "
        "gehouden een methodologie vast te leggen teneinde de gedragslijnen "
        "te bepalen.\n"
    )

    out = inject_headings(body, filename="ITAA-norm-aww-geconsolideerd.md")

    assert "## Bijlage IV. Beslissingsbomen ter illustratie" in out
    # Body-rest moet bewaard zijn
    assert "Elk kantoor is ertoe gehouden" in out


def test_inject_norm_headings_geen_dubbele_heading_als_parent_al_bestaat():
    """Sectie 5 staat normaal wél als standalone regel in de body. De fix
    mag dan geen tweede `## 5. ...` injecteren.
    """
    body = _TOC_FIXTURE + (
        "1. Algemene bepalingen\n\n"
        "1.1. ...\n\n"
        "5. Onderzoek van de verrichtingen\n\n"
        "5.1. Onderkennen van atypische verrichtingen.\n\n"
        "5.2. ...\n"
    )

    out = inject_headings(body, filename="ITAA-norm-aww-geconsolideerd.md")

    # Mag maar één keer voorkomen
    assert out.count("## 5. Onderzoek van de verrichtingen") == 1
