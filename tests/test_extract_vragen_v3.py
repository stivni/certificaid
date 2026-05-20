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
