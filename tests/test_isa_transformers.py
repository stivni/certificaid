"""
Tests voor de ISA-specifieke ETL-transformers.

Twee transformers worden gedekt:

1. `strip_isa_page_footers` — verwijdert de repeterende IBR-IRE / NBA-IBR
   page-footer-blokken die op elke pagina van een ISA-PDF herhaald worden
   (ALL-CAPS running title + `ISA <num>` + `NBA-IBR 20XX` + `N/M` +
   `Originele bron: Handbook ...` + `Versie 20XX`).

2. `inject_headings_isa` — promoot de standaard ISA-sectielabels in de
   body naar `## `-headings (`Inleiding`, `Doelstelling(en)`, `Definities`,
   `Vereisten`, `Toepassingsgerichte en overige verklarende teksten`,
   `Ingangsdatum`, `Bijlage(n)`, ...).

Beide transformers volgen het ADR-005 §4-contract:
    (body: str, frontmatter: dict) -> tuple[str, dict]

De tests worden geschreven vóór de implementatie (TDD). False-positive
bescherming is expliciet: nummering in TOC's, citaties van het sectielabel
in lopende zin en bestaande `## `-headings mogen NIET worden geraakt.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl.transformers.strip_isa_page_footers import (  # noqa: E402
    strip_isa_page_footers,
)
from tools.etl.transformers.inject_headings_isa import (  # noqa: E402
    inject_headings_isa,
)


def _strip(body: str) -> str:
    new, _ = strip_isa_page_footers(body, {})
    return new


def _inject(body: str) -> str:
    new, _ = inject_headings_isa(body, {})
    return new


# ─── strip_isa_page_footers ──────────────────────────────────────────────────


class TestStripIsaPageFooters:
    def test_verwijdert_volledig_footer_blok(self):
        body = (
            "Vorige paragraaf eindigt hier.\n"
            "\n"
            "ALGEHELE DOELSTELLINGEN VAN DE ONAFHANKELIJKE AUDITOR \n"
            " \n"
            " \n"
            "ISA 200 \n"
            "NBA-IBR 2022 \n"
            "3/28 \n"
            "Originele bron: Handbook of International Quality Management, "
            "Auditing, Review, Other Assurance, and Related Services "
            "Pronouncements, 2022 Edition Volume I \n"
            "Versie 2023 \n"
            "\n"
            "Volgende paragraaf begint hier.\n"
        )
        out = _strip(body)
        assert "Vorige paragraaf eindigt hier." in out
        assert "Volgende paragraaf begint hier." in out
        assert "NBA-IBR" not in out
        assert "Originele bron" not in out
        assert "ALGEHELE DOELSTELLINGEN VAN DE ONAFHANKELIJKE AUDITOR" not in out
        assert "ISA 200 \n" not in out and "ISA 200\n" not in out

    def test_verwijdert_footer_met_en_dash_variant(self):
        # ISA 700 gebruikt `NBA – IBR` (en-dash) i.p.v. `NBA-IBR`.
        body = (
            "Body-tekst hierboven.\n"
            "\n"
            "HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN \n"
            "ISA 700 (herzien) \n"
            "NBA – IBR 2022 \n"
            " 4/50 \n"
            " \n"
            "Originele bron : Handbook of International Quality Management, "
            "Auditing, Review, Other Assurance, and Related Services "
            "Pronouncements, 2022 Edition Volume I \n"
            " \n"
            "Versie 2023 \n"
            "\n"
            "Onderstaande paragraaf.\n"
        )
        out = _strip(body)
        assert "Body-tekst hierboven." in out
        assert "Onderstaande paragraaf." in out
        assert "NBA" not in out
        assert "HET VORMEN VAN EEN OORDEEL" not in out
        assert "Originele bron" not in out
        assert "Versie 2023" not in out

    def test_verwijdert_meerdere_opeenvolgende_footers(self):
        body = (
            "Eerste alinea.\n"
            "\n"
            "CONTROLE-INFORMATIE \n"
            " \n"
            " \n"
            "ISA 500 \n"
            "NBA-IBR 2023 \n"
            "2/22 \n"
            "Originele bron: Handbook X \n"
            "Versie 2023 \n"
            "\n"
            "Tussentekst.\n"
            "\n"
            "CONTROLE-INFORMATIE \n"
            " \n"
            " \n"
            "ISA 500 \n"
            "NBA-IBR 2023 \n"
            "3/22 \n"
            "Originele bron: Handbook X \n"
            "Versie 2023 \n"
            "\n"
            "Laatste alinea.\n"
        )
        out = _strip(body)
        assert "Eerste alinea." in out
        assert "Tussentekst." in out
        assert "Laatste alinea." in out
        assert out.count("CONTROLE-INFORMATIE") == 0
        assert out.count("NBA-IBR") == 0

    def test_behoudt_legitime_isa_verwijzingen_inline(self):
        # Inline references naar `ISA 200` in zinnen mogen niet weg.
        body = (
            "De auditor past ISA 200 toe op de controle van financiële "
            "overzichten. Dit is geen page-footer maar lopende tekst.\n"
            "\n"
            "Verder noemt ISA 315 (herzien) de risico-inschatting expliciet.\n"
        )
        out = _strip(body)
        assert "De auditor past ISA 200 toe" in out
        assert "ISA 315 (herzien)" in out

    def test_behoudt_top_h1_titel_van_document(self):
        # De `# ISA 200 — ...` H1 boven het body-blok blijft intact.
        body = (
            "# ISA 200 — Algehele doelstellingen\n"
            "\n"
            "> Bron: IBR-IRE PDF.\n"
            "\n"
            "ALGEHELE DOELSTELLINGEN VAN DE ONAFHANKELIJKE AUDITOR \n"
            "ISA 200 \n"
            "NBA-IBR 2022 \n"
            "2/28 \n"
            "Originele bron: Handbook \n"
            "Versie 2023 \n"
            "\n"
            "Echte body-tekst.\n"
        )
        out = _strip(body)
        assert "# ISA 200 — Algehele doelstellingen" in out
        assert "Echte body-tekst." in out
        assert "NBA-IBR" not in out

    def test_idempotent(self):
        body = (
            "Tekst.\n"
            "\n"
            "DOELSTELLINGEN \n"
            "ISA 200 \n"
            "NBA-IBR 2022 \n"
            "5/28 \n"
            "Originele bron: Handbook \n"
            "Versie 2023 \n"
            "\n"
            "Meer tekst.\n"
        )
        once = _strip(body)
        twice = _strip(once)
        assert once == twice

    def test_verwijdert_glued_anker_met_pagenr_isa805(self):
        # ISA-805 glue-t anker + NBA-IBR + page-num op één regel.
        body = (
            "Body-tekst.\n"
            "\n"
            "AUDITS OF SINGLE FINANCIAL STATEMENTS \n"
            "ISA 805 (herzien)                                          "
            "NBA-IBR 2025                                                "
            "5/27                                         \n"
            "Originele bron : Handbook of International Quality "
            "Management, Auditing, Review, Other Assurance, and Related "
            "Services \n"
            "Pronouncements, 2022 Edition Volume I \n"
            "Version 2025 \n"
            "\n"
            "Volgende body.\n"
        )
        out = _strip(body)
        assert "Body-tekst." in out
        assert "Volgende body." in out
        assert "NBA-IBR" not in out
        assert "ISA 805 (herzien)" not in out

    def test_verwijdert_anker_met_bijlage_suffix_isa810(self):
        # ISA-810 Bijlage-pagina's gebruiken `ISA 810 (Herzien) - Bijlage`.
        body = (
            "Bovenstaande body.\n"
            "\n"
            "ISA 810 (Herzien) - Bijlage \n"
            "NBA-IBR 2025  \n"
            "17/27 \n"
            "Originele bron : Handbook \n"
            "Pronouncements, 2022 Edition Volume I \n"
            "Version 2025 \n"
            "\n"
            "Onderstaande body.\n"
        )
        out = _strip(body)
        assert "Bovenstaande body." in out
        assert "Onderstaande body." in out
        assert "NBA-IBR" not in out
        assert "ISA 810 (Herzien) - Bijlage" not in out

    def test_verwijdert_glued_anker_variant_isa810(self):
        # ISA-810 (en latere updates) gebruikt `ISA 810 (herzien)<sp>NBA-IBR 2025`
        # op één regel + `Version 2025` (Engels) als afsluiter.
        body = (
            "Body-tekst hierboven.\n"
            "\n"
            "OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN \n"
            "ISA 810 (herzien)                                                          NBA-IBR 2025  \n"
            "4/27 \n"
            "Originele bron : Handbook of International Quality Management, Auditing, Review, "
            "Other Assurance, and Related Services \n"
            "Pronouncements, 2022 Edition Volume I \n"
            "Version 2025 \n"
            "\n"
            "Volgende body-tekst.\n"
        )
        out = _strip(body)
        assert "Body-tekst hierboven." in out
        assert "Volgende body-tekst." in out
        assert "NBA-IBR" not in out
        assert "ISA 810 (herzien)" not in out
        assert "OPDRACHTEN OM TE RAPPORTEREN" not in out
        assert "Version 2025" not in out

    def test_geen_wijziging_op_body_zonder_footer(self):
        body = (
            "Gewone markdown-body.\n"
            "\n"
            "Met meerdere paragrafen.\n"
        )
        out = _strip(body)
        assert out == body


# ─── inject_headings_isa ─────────────────────────────────────────────────────


class TestInjectHeadingsIsa:
    def test_promoot_inleiding_label(self):
        body = (
            "Voorgaande tekst.\n"
            "\n"
            "Inleiding\n"
            "\n"
            "Toepassingsgebied van deze ISA\n"
            "\n"
            "1. \n"
            "Deze ISA behandelt de algehele verantwoordelijkheden.\n"
        )
        out = _inject(body)
        assert "## Inleiding" in out
        assert "## Toepassingsgebied van deze ISA" in out

    def test_promoot_doelstelling_en_definities_en_vereisten(self):
        body = (
            "Wat tekst.\n"
            "\n"
            "Doelstellingen\n"
            "\n"
            "3. \n"
            "De doelstelling van de auditor is X.\n"
            "\n"
            "Definities\n"
            "\n"
            "4. \n"
            "Voor de toepassing van deze ISA: ...\n"
            "\n"
            "Vereisten\n"
            "\n"
            "5. \n"
            "De auditor dient X te doen.\n"
        )
        out = _inject(body)
        assert "## Doelstellingen" in out
        assert "## Definities" in out
        assert "## Vereisten" in out

    def test_promoot_toepassingsgerichte_tekst(self):
        body = (
            "Sluitende tekst van Vereisten.\n"
            "\n"
            "Toepassingsgerichte en overige verklarende teksten\n"
            "\n"
            "A1. \n"
            "Toelichting bij paragraaf 1.\n"
        )
        out = _inject(body)
        assert "## Toepassingsgerichte en overige verklarende teksten" in out

    def test_promoot_ingangsdatum_en_bijlage(self):
        body = (
            "Sluitende paragraaf.\n"
            "\n"
            "Ingangsdatum\n"
            "\n"
            "10. \n"
            "Deze ISA is van toepassing vanaf 15 december.\n"
            "\n"
            "Bijlage\n"
            "\n"
            "Voorbeelden van controleverklaringen.\n"
        )
        out = _inject(body)
        assert "## Ingangsdatum" in out
        assert "## Bijlage" in out

    def test_geen_promotie_van_inhoudsopgave_entries(self):
        # In de TOC heeft het label vaak een dotted-leader en pagina-nummer
        # achter zich op dezelfde regel — die mag NIET gepromoot worden.
        body = (
            "INHOUDSOPGAVE\n"
            "Paragraaf\n"
            "Inleiding\n"
            "Toepassingsgebied van deze ISA ........................................................................................................... 1-2\n"
            "Doelstelling ........................................................................................................................................... 4\n"
            "Definities ............................................................................................................................................. 5\n"
        )
        out = _inject(body)
        # Geen ## headings in TOC-regels met dotted leaders
        assert "## Toepassingsgebied van deze ISA ......" not in out
        assert "## Doelstelling ....." not in out
        # Het kale TOC-label `Inleiding` direct na `Paragraaf` mag ook niet
        # gepromoot worden — het zit binnen het TOC-blok.
        # (na het echte body-blok komt `Inleiding` opnieuw en MAG gepromoot)
        toc_inleiding_line = "\nInleiding\n"
        # Mag niet beginnen met ## op die TOC-positie
        assert "INHOUDSOPGAVE" in out

    def test_geen_promotie_van_inline_woord_in_zin(self):
        # 'Inleiding tot de norm.' is geen sectielabel — staat midden in een zin.
        body = (
            "Dit is een Inleiding tot de norm en een andere zin.\n"
            "\n"
            "De auditor moet zijn Doelstelling behalen door X.\n"
        )
        out = _inject(body)
        assert "## Inleiding" not in out
        assert "## Doelstelling" not in out
        assert "Dit is een Inleiding tot de norm" in out

    def test_idempotent(self):
        body = (
            "Tekst.\n"
            "\n"
            "Inleiding\n"
            "\n"
            "1. \n"
            "Body.\n"
            "\n"
            "Doelstelling\n"
            "\n"
            "2. \n"
            "Body.\n"
        )
        once = _inject(body)
        twice = _inject(once)
        assert once == twice

    def test_behoudt_bestaande_h2_heading(self):
        body = (
            "## Inleiding\n"
            "\n"
            "1. \n"
            "Body.\n"
        )
        out = _inject(body)
        # Mag niet `## ## Inleiding` of dubbele headings opleveren
        assert out.count("## Inleiding") == 1
        assert "## ## Inleiding" not in out

    def test_lege_input(self):
        out = _inject("")
        assert out == ""

    def test_geen_wijziging_zonder_sectielabels(self):
        body = "Gewone tekst zonder ISA-sectielabels.\n\nNog wat tekst.\n"
        out = _inject(body)
        assert out == body


# ─── Integration: beide transformers + helper-flow ───────────────────────────


class TestIntegration:
    def test_strip_dan_inject_geeft_h2_headings(self):
        # Realistisch fragment: footer tussen Inleiding en eerstvolgende
        # paragraaf. Na strip + inject moet er een ## Inleiding zijn.
        body = (
            "INHOUDSOPGAVE\n"
            "Paragraaf\n"
            "Inleiding\n"
            "Toepassingsgebied van deze ISA ........................................................................................................... 1-2\n"
            "\n"
            "CONTROLE-INFORMATIE \n"
            "ISA 500 \n"
            "NBA-IBR 2023 \n"
            "4/22 \n"
            "Originele bron: Handbook X \n"
            "Versie 2023 \n"
            "\n"
            "Inleiding\n"
            "\n"
            "Toepassingsgebied van deze ISA\n"
            "\n"
            "1. \n"
            "Deze ISA legt uit wat controle-informatie vormt.\n"
            "\n"
            "Doelstelling\n"
            "\n"
            "4. \n"
            "De doelstelling van de auditor is X.\n"
        )
        stripped, _ = strip_isa_page_footers(body, {})
        injected, _ = inject_headings_isa(stripped, {})
        # Page-footer weg
        assert "NBA-IBR" not in injected
        assert "Originele bron" not in injected
        # ## headings op body-positie
        assert "## Inleiding" in injected
        assert "## Toepassingsgebied van deze ISA" in injected
        assert "## Doelstelling" in injected
        # TOC blijft TOC (geen ## op TOC-regel)
        # We zoeken specifiek de TOC-regel met dotted leaders:
        assert "## Toepassingsgebied van deze ISA ......" not in injected

    def test_apply_helper_op_temp_isa_file(self, tmp_path):
        # Simuleer een mini-ISA bestand met frontmatter + body, runt de helper
        # en verifieert dat body wordt geschoond én provenance trust resette
        # naar unreviewed.
        import frontmatter as fm
        from tools.etl.apply_isa_transformers import process_file

        body = (
            "# ISA 200 — Top H1 blijft\n"
            "\n"
            "ALGEHELE DOELSTELLINGEN \n"
            "ISA 200 \n"
            "NBA-IBR 2022 \n"
            "3/28 \n"
            "Originele bron: Handbook \n"
            "Versie 2023 \n"
            "\n"
            "Inleiding\n"
            "\n"
            "Toepassingsgebied van deze ISA\n"
            "\n"
            "1. \n"
            "Deze ISA legt X uit.\n"
            "\n"
            "Doelstelling\n"
            "\n"
            "11. \n"
            "Body.\n"
            "\n"
            "Definities\n"
            "\n"
            "13. \n"
            "Body.\n"
            "\n"
            "Vereisten\n"
            "\n"
            "14. \n"
            "Body.\n"
        )
        md_file = tmp_path / "ISA-test.md"
        post = fm.Post(content=body, metadata={
            "title": "ISA TEST",
            "provenance": {
                "tooling": {"pipeline": "tools/old/old.py"},
                "trust": {"status": "needs-rework"},
            },
        })
        with md_file.open("wb") as f:
            fm.dump(post, f)

        result = process_file(md_file, dry_run=False)
        assert result["changed"] is True
        assert result["h2_after"] >= 4

        # Re-read
        loaded = fm.load(str(md_file))
        # Body checks
        assert "NBA-IBR" not in loaded.content
        assert "# ISA 200 — Top H1 blijft" in loaded.content
        assert "## Inleiding" in loaded.content
        assert "## Doelstelling" in loaded.content
        assert "## Definities" in loaded.content
        assert "## Vereisten" in loaded.content
        # Provenance checks
        prov = loaded.metadata["provenance"]
        assert prov["trust"]["status"] == "unreviewed"
        assert "apply_isa_transformers.py" in prov["tooling"]["pipeline"]

    def test_apply_helper_idempotent_geen_changes_op_clean_file(self, tmp_path):
        import frontmatter as fm
        from tools.etl.apply_isa_transformers import process_file

        body = (
            "# ISA 200 — Header\n"
            "\n"
            "## Inleiding\n"
            "\n"
            "1. \n"
            "Schone body.\n"
        )
        md_file = tmp_path / "ISA-clean.md"
        post = fm.Post(content=body, metadata={"title": "X", "provenance": {}})
        with md_file.open("wb") as f:
            fm.dump(post, f)

        result = process_file(md_file, dry_run=False)
        # Geen wijzigingen op een al-gestructureerd bestand → changed=False
        assert result["changed"] is False

    def test_minstens_3_headings_uit_realistische_sample(self):
        # Mini-versie van de ISA-200 body-structuur.
        body = (
            "INHOUDSOPGAVE\n"
            "Paragraaf\n"
            "Inleiding\n"
            "Doelstelling ........................................................................................................................................... 11-12\n"
            "Definities ................................................................................................................................................... 13\n"
            "Vereisten\n"
            "\n"
            "Inleiding\n"
            "\n"
            "Toepassingsgebied van deze ISA\n"
            "\n"
            "1. \n"
            "Deze ISA legt X uit.\n"
            "\n"
            "Doelstelling\n"
            "\n"
            "11. \n"
            "Body.\n"
            "\n"
            "Definities\n"
            "\n"
            "13. \n"
            "Body.\n"
            "\n"
            "Vereisten\n"
            "\n"
            "Ethische voorschriften\n"
            "\n"
            "14. \n"
            "Body.\n"
        )
        out = _inject(body)
        h2_count = out.count("\n## ")
        assert h2_count >= 3, f"Verwacht ≥3 ## headings, kreeg {h2_count}"
