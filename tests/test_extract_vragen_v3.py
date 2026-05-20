"""Tests voor v3-pattern-detectoren en transformatie (ADR-021 v3.0)."""
from __future__ import annotations

from tools.examen import _v3_blok_detectoren as D
from tools.examen import extract_vragen_v3 as V3


class TestParseBedrag:
    def test_komma_decimaal(self):
        assert D.parse_bedrag("500,00") == 500.0

    def test_punt_thousands(self):
        assert D.parse_bedrag("7.000,00") == 7000.0

    def test_spatie_thousands(self):
        assert D.parse_bedrag("105 000,50") == 105000.50

    def test_geen_decimaal_punt_thousands(self):
        assert D.parse_bedrag("12.500") == 12500.0

    def test_ongeldig(self):
        assert D.parse_bedrag("abc") is None

    def test_leeg(self):
        assert D.parse_bedrag("") is None


class TestLiftTopLevelVelden:
    def test_punten_uppercase(self):
        rest, v = D.lift_top_level_velden("Tekst hier. 5 PUNTEN")
        assert v["punten"] == 5.0
        assert "PUNTEN" not in rest

    def test_punten_lowercase(self):
        rest, v = D.lift_top_level_velden("Vraag 1 / 12 punten Tekst")
        assert v["punten"] == 12.0

    def test_vraag_prefix_decimal(self):
        rest, v = D.lift_top_level_velden("A.1. Voorraden")
        assert v["vraag_prefix"] == "A.1"
        assert "Voorraden" in rest

    def test_vraag_prefix_vraag_n(self):
        rest, v = D.lift_top_level_velden("Vraag 4 … Tekst hier")
        assert v["vraag_prefix"] == "Vraag 4"

    def test_geen_velden(self):
        rest, v = D.lift_top_level_velden("Gewone tekst zonder header")
        assert v["punten"] is None
        assert v["vraag_prefix"] is None
        assert v["vraag_header_geextracteerd"] is False


class TestDetecteerProefSaldibalans:
    def test_bibf_voorbeeld(self):
        tekst = "staan volgende bedragen: 32 Goederen in bewerking D 500,00 euro 34 Handelsgoederen D 7.000,00 euro De inventaris"
        blokken = D.detecteer_typed_blokken(tekst)
        psb = [b for b in blokken if b["type"] == "proef_saldibalans"]
        assert len(psb) == 1
        assert len(psb[0]["regels"]) == 2
        assert psb[0]["regels"][0]["rekening"] == "32"
        assert psb[0]["regels"][0]["zijde"] == "D"
        assert psb[0]["regels"][0]["bedrag"] == 500.0
        assert psb[0]["regels"][1]["bedrag"] == 7000.0

    def test_solo_regel_geen_blok(self):
        # Eén regel is geen PSB-blok (minstens 2 nodig)
        tekst = "Ergens 99 Voorraden D 100,00 ergens anders"
        blokken = D.detecteer_typed_blokken(tekst)
        assert not any(b["type"] == "proef_saldibalans" for b in blokken)


class TestDetecteerInventaris:
    def test_bullet_lijst(self):
        tekst = "geeft - goederen in bewerking 400,00 - handelsgoederen 8.500,00 De marktprijs"
        blokken = D.detecteer_typed_blokken(tekst)
        inv = [b for b in blokken if b["type"] == "inventaris"]
        assert len(inv) == 1
        assert len(inv[0]["regels"]) == 2
        assert inv[0]["regels"][1]["bedrag"] == 8500.0


class TestDetecteerMarktwaarde:
    def test_marktprijs(self):
        tekst = "De marktprijs van de handelsgoederen bedraagt 8.250,00 euro."
        blokken = D.detecteer_typed_blokken(tekst)
        m = [b for b in blokken if b["type"] == "marktwaarde"]
        assert len(m) == 1
        assert m[0]["bedrag"] == 8250.0


class TestDetecteerAanpassing:
    def test_afprijzing(self):
        tekst = "moeten afgeprijsd worden voor een totaal bedrag van 75,00 euro."
        blokken = D.detecteer_typed_blokken(tekst)
        a = [b for b in blokken if b["type"] == "aanpassing"]
        assert len(a) == 1
        assert a[0]["subtype"] == "afprijzing"
        assert a[0]["bedrag"] == 75.0


class TestDetecteerBijlage:
    def test_in_bijlage(self):
        tekst = "Achtergrond. In bijlage vindt u de balans en de resultatenrekening. Vraag: bereken."
        blokken = D.detecteer_typed_blokken(tekst)
        b = [x for x in blokken if x["type"] == "bijlage_verwijzing"]
        assert len(b) == 1


class TestDetecteerVraagInstructie:
    def test_geef(self):
        tekst = "Casus tekst. Geef de afsluitingsboekingen."
        blokken = D.detecteer_typed_blokken(tekst)
        i = [b for b in blokken if b["type"] == "vraag_instructie"]
        assert len(i) == 1
        assert "Geef" in i[0]["inhoud"]

    def test_bereken(self):
        tekst = "Gegevens hier. Bereken het belangenpercentage."
        blokken = D.detecteer_typed_blokken(tekst)
        i = [b for b in blokken if b["type"] == "vraag_instructie"]
        assert len(i) == 1


class TestDetecteerMCOptie:
    def test_letter_opties(self):
        tekst = """Wat is een aanloopkost?
A. Stichtingskost
B. Werkingskost
C. Investeringskost"""
        blokken = D.detecteer_typed_blokken(tekst)
        mc = [b for b in blokken if b["type"] == "mc_optie"]
        assert len(mc) == 3
        assert mc[0]["label"] == "A"

    def test_lower_opties(self):
        tekst = """Welke methode:
a) FIFO
b) LIFO
c) gewogen gemiddelde"""
        blokken = D.detecteer_typed_blokken(tekst)
        mc = [b for b in blokken if b["type"] == "mc_optie"]
        assert len(mc) >= 2

    def test_solo_letter_geen_mc(self):
        # Eén losse "A." aan begin is geen MC-set
        tekst = "A. Iets enkels.\n\nGewone tekst eronder."
        blokken = D.detecteer_typed_blokken(tekst)
        assert not any(b["type"] == "mc_optie" for b in blokken)


class TestDetecteerCasusContext:
    def test_de_bvba(self):
        tekst = "De BVBA Albert legt volgende balans af, met cijfers."
        blokken = D.detecteer_typed_blokken(tekst)
        c = [b for b in blokken if b["type"] == "casus_context"]
        assert len(c) >= 1


class TestTransformeerVraag:
    def test_2003_vrA2_full_pipeline(self):
        """End-to-end: 2003-bibf-vrA2 vraagtekst krijgt typed blokken."""
        v2_vraag = {
            "id": "test-vrA2",
            "vraagtekst": "A.2. Voorraden. Op de proef- en saldibalans staan volgende bedragen: 32 Goederen in bewerking D 500,00 euro 34 Handelsgoederen D 7.000,00 euro De inventaris per einde boekjaar geeft - goederen in bewerking 400,00 - handelsgoederen 8.500,00 De marktprijs van de handelsgoederen bedraagt 8.250,00 euro. Er werd ook vastgesteld dat bepaalde goederen moeten afgeprijsd worden voor een totaal bedrag van 75,00 euro. Vraag : geef de afsluitingsboekingen. 5 PUNTEN",
            "vraagtekst_blokken": [
                {
                    "type": "tekst",
                    "inhoud": "A.2. Voorraden. Op de proef- en saldibalans staan volgende bedragen: 32 Goederen in bewerking D 500,00 euro 34 Handelsgoederen D 7.000,00 euro De inventaris per einde boekjaar geeft - goederen in bewerking 400,00 - handelsgoederen 8.500,00 De marktprijs van de handelsgoederen bedraagt 8.250,00 euro. Er werd ook vastgesteld dat bepaalde goederen moeten afgeprijsd worden voor een totaal bedrag van 75,00 euro. Vraag : geef de afsluitingsboekingen. 5 PUNTEN",
                }
            ],
        }
        v3 = V3.transformeer_vraag(v2_vraag)
        types = [b["type"] for b in v3["vraagtekst_blokken"]]
        assert "proef_saldibalans" in types
        assert "inventaris" in types
        assert "marktwaarde" in types
        assert "aanpassing" in types
        assert "vraag_instructie" in types
        # Top-level velden
        assert v3["punten"] == 5.0
        assert v3["vraag_prefix"] == "A.2"
        assert v3["vraag_header_geextracteerd"] is True

    def test_behoud_antwoord_velden(self):
        v2_vraag = {
            "id": "t-vr1",
            "vraagtekst": "Bereken X.",
            "vraagtekst_blokken": [{"type": "tekst", "inhoud": "Bereken X."}],
            "correct_antwoord": "42",
            "antwoord_motivering": "Omdat",
            "record_gap_report": {"type": "test"},
        }
        v3 = V3.transformeer_vraag(v2_vraag)
        # Deze velden moeten in v3 nog steeds aanwezig zijn — de transformatie
        # mag ze niet weggooien.
        assert v3["correct_antwoord"] == "42"
        assert v3["antwoord_motivering"] == "Omdat"
        assert v3["record_gap_report"] == {"type": "test"}

    def test_tabel_blok_doorgegeven(self):
        v2_vraag = {
            "id": "t-vr1",
            "vraagtekst": "Vul aan.",
            "vraagtekst_blokken": [
                {"type": "tekst", "inhoud": "Vul aan."},
                {"type": "tabel", "headers": ["A", "B"], "rows": [["1", "2"]]},
            ],
        }
        v3 = V3.transformeer_vraag(v2_vraag)
        types = [b["type"] for b in v3["vraagtekst_blokken"]]
        assert "tabel" in types


# ---------------------------------------------------------------------------
# v3.1: vraag-cleanup tests (ADR-023 §v3.1)
# ---------------------------------------------------------------------------


class TestVraagOnderwerpDetectie:
    def test_kapitaalsubsidies(self):
        """User-voorbeeld 2003-bibf-vrA1."""
        rest, v = D.lift_top_level_velden(
            "Kapitaalsubsidies. Gedurende het boekjaar 2002 werd een machine aangekocht."
        )
        assert v["vraag_onderwerp"] == "Kapitaalsubsidies"
        assert v["vraag_header_geextracteerd"] is True
        assert "Kapitaalsubsidies" not in rest
        assert "Gedurende" in rest

    def test_voorraden(self):
        rest, v = D.lift_top_level_velden(
            "Voorraden. Op de proef- en saldibalans staan volgende bedragen."
        )
        assert v["vraag_onderwerp"] == "Voorraden"

    def test_geen_onderwerp_bij_eigennaam(self):
        # 'Dhr' staat NIET in de whitelist → geen onderwerp
        rest, v = D.lift_top_level_velden(
            "Dhr. Janssens is bestuurder. Hij wenst advies over zijn pensioenplan."
        )
        assert v["vraag_onderwerp"] is None

    def test_geen_onderwerp_bij_vraag_woord(self):
        rest, v = D.lift_top_level_velden("Vraag: bereken X.")
        assert v["vraag_onderwerp"] is None

    def test_geen_onderwerp_bij_lange_zin(self):
        rest, v = D.lift_top_level_velden(
            "De BVBA Albert legt volgende balans af, met cijfers."
        )
        # 'De' niet in whitelist → geen onderwerp
        assert v["vraag_onderwerp"] is None


class TestResidueStrip:
    def test_vraag_colon_in_instructie(self):
        tekst = "Casus tekst. Vraag : geef de afsluitingsboekingen."
        blokken = D.detecteer_typed_blokken(tekst)
        instr = [b for b in blokken if b["type"] == "vraag_instructie"]
        assert len(instr) == 1
        assert "Vraag" not in instr[0]["inhoud"]
        assert instr[0]["inhoud"].startswith("geef") or instr[0]["inhoud"].startswith("Geef")

    def test_punten_residue_strip(self):
        """5 PUNTEN aan einde wordt gelift naar punten + uit body."""
        rest, v = D.lift_top_level_velden("Vraag 1. Bereken iets. 5 PUNTEN")
        assert v["punten"] == 5.0
        assert "PUNTEN" not in rest

    def test_antwoord_residue_uit_body(self):
        """Een losse 'Antwoord' kop-residu wordt uit body verwijderd."""
        rest, v = D.lift_top_level_velden("Vraag 1. Casus tekst.\nAntwoord\nBereken iets.")
        # "Antwoord" als eigen regel wordt uit body gestript
        assert "\nAntwoord\n" not in rest


# ---------------------------------------------------------------------------
# v3.2: kosten_lijst, mc_optie ↮ subvraag-dedup, tabel→mc, gevraagd-splitter
# ---------------------------------------------------------------------------


class TestKostenLijstDetector:
    def test_kosten_lijst_basis(self):
        tekst = (
            "Volgende kosten werden gemaakt:\n"
            "- vooronderzoek studiebureau 20.000,00\n"
            "- ontwikkeling door derden 15.000,00\n"
            "- aankopen materiaal 180.000,00\n"
            "Gevraagd: bereken."
        )
        blokken = D.detecteer_typed_blokken(tekst)
        kl = [b for b in blokken if b["type"] == "kosten_lijst"]
        assert len(kl) == 1
        assert len(kl[0]["regels"]) == 3
        assert kl[0]["regels"][0]["post"].startswith("vooronderzoek")
        assert kl[0]["regels"][0]["bedrag"] == 20000.0

    def test_geen_intro_geen_blok(self):
        # Bullet-lijst zonder kosten/uitgaven/posten/investeringen-intro
        # — moet als inventaris of tekst herkend worden, niet als kosten_lijst.
        tekst = (
            "Beschrijving van het magazijn:\n"
            "- iets 100,00\n"
            "- nog iets 200,00\n"
        )
        blokken = D.detecteer_typed_blokken(tekst)
        assert not any(b["type"] == "kosten_lijst" for b in blokken)


class TestTabelNaarMCConversie:
    def test_1koloms_tabel_wordt_mc(self):
        blokken = [
            {"type": "tekst", "inhoud": "Kruis het juiste antwoord aan."},
            {"type": "tabel", "rows": [["Optie A", ""], ["Optie B", ""], ["Optie C", ""]]},
        ]
        nieuw = D.converteer_1koloms_tabel_naar_mc_opties(blokken)
        mc = [b for b in nieuw if b.get("type") == "mc_optie"]
        assert len(mc) == 3
        assert mc[0]["label"] == "A"
        assert mc[2]["tekst"] == "Optie C"

    def test_zonder_instructie_geen_conversie(self):
        blokken = [
            {"type": "tekst", "inhoud": "Beschrijf wat hier staat."},
            {"type": "tabel", "rows": [["a", ""], ["b", ""], ["c", ""]]},
        ]
        nieuw = D.converteer_1koloms_tabel_naar_mc_opties(blokken)
        # Tabel blijft tabel
        assert any(b["type"] == "tabel" for b in nieuw)


class TestMCSubvraagDedup:
    def test_dedup_op_label(self):
        blokken = [
            {"type": "mc_optie", "label": "a", "tekst": "Iets"},
            {"type": "mc_optie", "label": "b", "tekst": "Iets anders"},
        ]
        sub_labels = ["a)", "b)"]
        nieuw = D.deduplicate_mc_optie_subvraag(blokken, sub_labels)
        # Beide MC-blokken verwijderd, want labels matchen subvragen
        assert not any(b.get("type") == "mc_optie" for b in nieuw)

    def test_geen_dedup_zonder_subvragen(self):
        blokken = [{"type": "mc_optie", "label": "A", "tekst": "Iets"}]
        nieuw = D.deduplicate_mc_optie_subvraag(blokken, [])
        assert len(nieuw) == 1


class TestGevraagdSplitter:
    def test_splitst_casus_en_vraag(self):
        blokken = [
            {
                "type": "tekst",
                "inhoud": (
                    "Lange verhalende casus over een vennootschap die kosten "
                    "maakt voor onderzoek. Er werden materialen aangekocht, "
                    "personeel betaald en studies gemaakt. "
                    "Gevraagd: bereken de boekingen."
                ),
            }
        ]
        nieuw = D.splits_blokken_op_gevraagd(blokken)
        types = [b["type"] for b in nieuw]
        assert "casus_context" in types or "tekst" in types
        # En de instructie zou opnieuw door de pipeline moeten
        assert any(b.get("type") == "vraag_instructie" or "bereken" in (b.get("inhoud","").lower()) for b in nieuw)


class TestSubvraagWhitespaceCleanup:
    def test_kort_residue_plakt_aan_vorige(self):
        blokken = [
            {"type": "mc_optie", "label": "c", "tekst": "rekening?"},
            {"type": "tekst", "inhoud": "tot op 2 cijfers."},
            {"type": "mc_optie", "label": "d", "tekst": "Aantal jaren?"},
        ]
        sub_labels = ["c)", "d)"]
        nieuw, plak = D.cleanup_subvraag_whitespace_residue(blokken, sub_labels)
        # Tekst-blok moet weg zijn
        assert not any(b.get("type") == "tekst" and "2 cijfers" in (b.get("inhoud") or "") for b in nieuw)
        # En plak_aan moet de tekst doorgeven voor sub 'c'
        assert "c" in plak
        assert "2 cijfers" in plak["c"]


class TestCasusContextOpzuig:
    def test_lange_verhalende_tekst_voor_instructie(self):
        # Lange verhalende casus + korte instructie → casus_context wordt gevormd
        verhaal = "De NV Aldra is een productiebedrijf. " + ("Het had een belangrijk jaar. " * 20)
        tekst = verhaal + " Bereken het resultaat."
        blokken = D.detecteer_typed_blokken(tekst)
        types = [b["type"] for b in blokken]
        # Moet een vraag_instructie hebben + een casus_context (opzuig)
        assert "vraag_instructie" in types
        # casus_context kan komen via _scan_casus_context OF opzuig
        casus = [b for b in blokken if b["type"] == "casus_context"]
        assert len(casus) >= 1

    def test_korte_tekst_blijft_tekst(self):
        # Korte tekst-prefix (< 50 tokens) wordt NIET gepromoveerd
        tekst = "Een kort iets. Bereken X."
        blokken = D.detecteer_typed_blokken(tekst)
        casus = [b for b in blokken if b["type"] == "casus_context"]
        # Geen opzuig voor korte tekst
        assert len(casus) == 0


# ---------------------------------------------------------------------------
# v3.3: MC-toewijzing aan subvragen (ADR-021 v3.3)
# ---------------------------------------------------------------------------


class TestAssignMCOptiesAanSubvragen:
    """Verifieer dat mc_opties op vraag-niveau correct verdeeld worden over
    subvragen op basis van positie in de oorspronkelijke vraagtekst (PDF-
    volgorde). Casus: 2013-1-vr2 (3 subvragen + 11 mc_opties → 3+4+4)."""

    def _bouw_vr2_fixture(self):
        origineel = (
            "Gelieve voor de onderstaande gevallen het juiste antwoord aan te kruisen.\n"
            "a) Onderneming A heeft een openstaande leveranciersschuld.\n"
            "A. Boeking-optie a-1.\n"
            "B. Boeking-optie a-2.\n"
            "C. Boeking-optie a-3.\n"
            "b) Onderneming A besluit een kapitaalvermindering door te voeren.\n"
            "A. Boeking-optie b-1.\n"
            "B. Boeking-optie b-2.\n"
            "C. Boeking-optie b-3.\n"
            "D. Boeking-optie b-4.\n"
            "c) Buitenlandse onderneming AB heeft een vaste inrichting.\n"
            "A. Belgische boekhouding c-1.\n"
            "B. Belgische boekhouding c-2.\n"
            "C. Belgische boekhouding c-3.\n"
            "D. Belgische boekhouding c-4.\n"
        )
        blokken = [
            {"type": "tekst", "inhoud": "Gelieve voor de onderstaande gevallen..."},
            {"type": "mc_optie", "label": "A", "tekst": "Boeking-optie a-1."},
            {"type": "mc_optie", "label": "B", "tekst": "Boeking-optie a-2."},
            {"type": "mc_optie", "label": "C", "tekst": "Boeking-optie a-3."},
            {"type": "mc_optie", "label": "A", "tekst": "Boeking-optie b-1."},
            {"type": "mc_optie", "label": "B", "tekst": "Boeking-optie b-2."},
            {"type": "mc_optie", "label": "C", "tekst": "Boeking-optie b-3."},
            {"type": "mc_optie", "label": "D", "tekst": "Boeking-optie b-4."},
            {"type": "mc_optie", "label": "A", "tekst": "Belgische boekhouding c-1."},
            {"type": "mc_optie", "label": "B", "tekst": "Belgische boekhouding c-2."},
            {"type": "mc_optie", "label": "C", "tekst": "Belgische boekhouding c-3."},
            {"type": "mc_optie", "label": "D", "tekst": "Belgische boekhouding c-4."},
        ]
        subvragen = [
            {"label": "a)", "tekst": "Onderneming A heeft ..."},
            {"label": "b)", "tekst": "Onderneming A besluit ..."},
            {"label": "c)", "tekst": "Buitenlandse onderneming AB ..."},
        ]
        return blokken, subvragen, origineel

    def test_verdeling_3_4_4(self):
        blokken, subvragen, origineel = self._bouw_vr2_fixture()
        nieuwe, per_sub = D.assign_mc_opties_aan_subvragen(
            blokken, subvragen, origineel
        )
        # Alle 11 mc_opties moeten verplaatst zijn → vraag-niveau bevat alleen
        # de openings-tekst nog.
        assert [b["type"] for b in nieuwe] == ["tekst"]
        assert len(per_sub["a"]) == 3
        assert len(per_sub["b"]) == 4
        assert len(per_sub["c"]) == 4

    def test_labels_per_subvraag_opnieuw_genummerd(self):
        blokken, subvragen, origineel = self._bouw_vr2_fixture()
        _, per_sub = D.assign_mc_opties_aan_subvragen(
            blokken, subvragen, origineel
        )
        assert [m["label"] for m in per_sub["a"]] == ["A", "B", "C"]
        assert [m["label"] for m in per_sub["b"]] == ["A", "B", "C", "D"]
        assert [m["label"] for m in per_sub["c"]] == ["A", "B", "C", "D"]

    def test_zonder_subvragen_no_op(self):
        blokken = [
            {"type": "tekst", "inhoud": "Vraag zonder subvragen."},
            {"type": "mc_optie", "label": "A", "tekst": "Optie 1"},
            {"type": "mc_optie", "label": "B", "tekst": "Optie 2"},
        ]
        nieuwe, per_sub = D.assign_mc_opties_aan_subvragen(
            blokken, [], "Vraag zonder subvragen. A. Optie 1 B. Optie 2"
        )
        # Geen mutatie: alle mc_opties blijven op vraag-niveau
        assert nieuwe == blokken
        assert per_sub == {}

    def test_mc_voor_eerste_marker_blijft_vraagniveau(self):
        origineel = (
            "A. Algemene voor-marker optie A.\n"
            "B. Algemene voor-marker optie B.\n"
            "a) Subvraag a.\n"
            "A. Sub-a-optie 1.\n"
            "B. Sub-a-optie 2.\n"
            "b) Subvraag b.\n"
            "A. Sub-b-optie 1.\n"
        )
        blokken = [
            {"type": "mc_optie", "label": "A", "tekst": "Algemene voor-marker optie A."},
            {"type": "mc_optie", "label": "B", "tekst": "Algemene voor-marker optie B."},
            {"type": "mc_optie", "label": "A", "tekst": "Sub-a-optie 1."},
            {"type": "mc_optie", "label": "B", "tekst": "Sub-a-optie 2."},
            {"type": "mc_optie", "label": "A", "tekst": "Sub-b-optie 1."},
        ]
        subvragen = [
            {"label": "a)", "tekst": "..."},
            {"label": "b)", "tekst": "..."},
        ]
        nieuwe, per_sub = D.assign_mc_opties_aan_subvragen(
            blokken, subvragen, origineel
        )
        # Eerste twee mc_opties (vóór de eerste subvraag-marker) blijven op
        # vraag-niveau
        assert len([b for b in nieuwe if b.get("type") == "mc_optie"]) == 2
        assert len(per_sub["a"]) == 2
        assert len(per_sub["b"]) == 1


class TestTransformeerVraagMCToewijzing:
    """End-to-end via transformeer_vraag: verifieer dat in een v2-vraag-record
    met subvragen + mc_opties op vraag-niveau, de mc_opties correct
    gedistribueerd worden naar de subvragen.
    """

    def test_vr2_distributie(self):
        # Reproduceert 2013-1-vr2: PDF levert 3 tekst-blokken + 3 1-koloms
        # tabel-blokken aan. v3-pipeline converteert tabellen naar mc_opties
        # (na dedup); v3.3-pass verdeelt ze over de subvragen.
        origineel_vraagtekst = (
            "Gelieve voor de onderstaande gevallen het juiste antwoord aan te kruisen.\n"
            "a) Onderneming A heeft een openstaande leveranciersschuld.\n"
            "Zij dient de volgende boeking aan te brengen.\n"
            "Boeking-optie a-1.\n"
            "Boeking-optie a-2.\n"
            "Boeking-optie a-3.\n"
            "b) Onderneming A besluit een kapitaalvermindering.\n"
            "Boeking-optie b-1.\n"
            "Boeking-optie b-2.\n"
            "Boeking-optie b-3.\n"
            "Boeking-optie b-4.\n"
            "c) Buitenlandse onderneming AB heeft een vaste inrichting.\n"
            "Belgische boekhouding c-1.\n"
            "Belgische boekhouding c-2.\n"
            "Belgische boekhouding c-3.\n"
            "Belgische boekhouding c-4.\n"
        )
        v2_vraag = {
            "id": "test-vr2",
            "vraagtekst": origineel_vraagtekst,
            "vraagtekst_blokken": [
                {
                    "type": "tekst",
                    "inhoud": (
                        "Gelieve voor de onderstaande gevallen het juiste antwoord aan te kruisen.\n"
                        "a) Onderneming A heeft een openstaande leveranciersschuld.\n"
                        "Zij dient de volgende boeking aan te brengen."
                    ),
                },
                {
                    "type": "tabel",
                    "headers": [""],
                    "rows": [
                        ["Boeking-optie a-1."],
                        ["Boeking-optie a-2."],
                        ["Boeking-optie a-3."],
                    ],
                },
                {
                    "type": "tekst",
                    "inhoud": "b) Onderneming A besluit een kapitaalvermindering.",
                },
                {
                    "type": "tabel",
                    "headers": [""],
                    "rows": [
                        ["Boeking-optie b-1."],
                        ["Boeking-optie b-2."],
                        ["Boeking-optie b-3."],
                        ["Boeking-optie b-4."],
                    ],
                },
                {
                    "type": "tekst",
                    "inhoud": "c) Buitenlandse onderneming AB heeft een vaste inrichting.",
                },
                {
                    "type": "tabel",
                    "headers": [""],
                    "rows": [
                        ["Belgische boekhouding c-1."],
                        ["Belgische boekhouding c-2."],
                        ["Belgische boekhouding c-3."],
                        ["Belgische boekhouding c-4."],
                    ],
                },
            ],
            "subvragen": [
                {"label": "a)", "tekst": "Onderneming A heeft een openstaande leveranciersschuld."},
                {"label": "b)", "tekst": "Onderneming A besluit een kapitaalvermindering."},
                {"label": "c)", "tekst": "Buitenlandse onderneming AB heeft een vaste inrichting."},
            ],
        }
        v3 = V3.transformeer_vraag(v2_vraag)
        # Geen mc_opties meer op vraag-niveau
        vraag_mc = [
            b for b in v3["vraagtekst_blokken"] if b.get("type") == "mc_optie"
        ]
        assert vraag_mc == []
        # Per subvraag: 3, 4, 4 mc_opties, labels herstartend bij A
        sub_a, sub_b, sub_c = v3["subvragen"]
        sub_a_mc = [
            b for b in (sub_a.get("vraagtekst_blokken") or [])
            if b.get("type") == "mc_optie"
        ]
        sub_b_mc = [
            b for b in (sub_b.get("vraagtekst_blokken") or [])
            if b.get("type") == "mc_optie"
        ]
        sub_c_mc = [
            b for b in (sub_c.get("vraagtekst_blokken") or [])
            if b.get("type") == "mc_optie"
        ]
        assert [m["label"] for m in sub_a_mc] == ["A", "B", "C"]
        assert [m["label"] for m in sub_b_mc] == ["A", "B", "C", "D"]
        assert [m["label"] for m in sub_c_mc] == ["A", "B", "C", "D"]

    def test_vraag_zonder_subvragen_geen_mutatie(self):
        v2_vraag = {
            "id": "test-vr-zonder-subs",
            "vraagtekst": (
                "Welke is correct?\n"
                "A. Optie 1.\n"
                "B. Optie 2.\n"
                "C. Optie 3.\n"
            ),
            "vraagtekst_blokken": [
                {
                    "type": "tekst",
                    "inhoud": (
                        "Welke is correct?\n"
                        "A. Optie 1.\n"
                        "B. Optie 2.\n"
                        "C. Optie 3.\n"
                    ),
                }
            ],
        }
        v3 = V3.transformeer_vraag(v2_vraag)
        # mc_opties blijven op vraag-niveau
        mc_op_vraagniveau = [
            b for b in v3["vraagtekst_blokken"] if b.get("type") == "mc_optie"
        ]
        assert len(mc_op_vraagniveau) >= 2
