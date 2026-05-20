"""Tests voor `structureer_antwoorden.py` (ADR-023).

STRICT geen nieuwe inhoud: parser leest bestaande motivering en deelt op in
typed blokken. Geen LLM, geen externe info.
"""
from __future__ import annotations

from tools.examen import structureer_antwoorden as S


class TestDetecteerConfidence:
    def test_grounded(self):
        assert S._detecteer_confidence("Iets ⚖️ hier") == "grounded"

    def test_inferred(self):
        assert S._detecteer_confidence("Iets 🤖 hier") == "inferred"

    def test_mix_geeft_inferred(self):
        assert S._detecteer_confidence("⚖️ en 🤖") == "inferred"

    def test_geen(self):
        assert S._detecteer_confidence("Geen marker") is None


class TestParseBedrag:
    def test_belgisch_format(self):
        assert S._parse_bedrag("10.000,00") == 10000.0

    def test_zonder_decimaal(self):
        assert S._parse_bedrag("500") == 500.0


class TestExtraheerGrondslag:
    def test_simpele_grondslag(self):
        m = "Tekst ⚖️\n\n_Grondslag: KB WVV art. 3:50._"
        blok, rest = S._extraheer_grondslag(m)
        assert blok is not None
        assert blok["type"] == "grondslag"
        assert "KB WVV art. 3:50" in blok["bronnen"]
        assert "_Grondslag:" not in rest

    def test_meerdere_bronnen(self):
        m = "_Grondslag: KB WVV art. 3:50; CBN-advies 2018/02._"
        blok, _ = S._extraheer_grondslag(m)
        assert len(blok["bronnen"]) == 2


class TestExtraheerBoekingenCodeblock:
    def test_codeblock_boeking(self):
        am = """Hier de boeking:

```
Debet 280 Deelnemingen in verbonden ondernemingen 50.000,00
Credit 550 Kredietinstellingen 50.000,00
```

Verder tekst."""
        blokken, rest = S._extraheer_boekingen(am)
        assert len(blokken) == 1
        assert blokken[0]["type"] == "boeking"
        assert len(blokken[0]["regels"]) == 2
        assert blokken[0]["regels"][0]["zijde"] == "D"
        assert blokken[0]["regels"][0]["rekening"] == "280"
        assert blokken[0]["regels"][0]["bedrag"] == 50000.0
        # Codeblock weg uit rest
        assert "```" not in rest
        assert "Verder tekst" in rest

    def test_inline_boekingsgroep(self):
        am = "Boeking volgt: Debet 416 Diverse vorderingen 10.000,00 Credit 15 Kapitaalsubsidies 10.000,00. Klaar."
        blokken, rest = S._extraheer_boekingen(am)
        assert len(blokken) == 1
        assert len(blokken[0]["regels"]) == 2


class TestExtraheerTabel:
    def test_markdown_tabel(self):
        am = """Hier:

| Component | Bedrag (€) |
|---|---|
| Resultaat | 100.000 |
| Afschrijvingen | 25.000 |

Klaar."""
        blokken, rest = S._extraheer_tabellen(am)
        assert len(blokken) == 1
        assert blokken[0]["type"] == "tabel"
        assert blokken[0]["headers"] == ["Component", "Bedrag (€)"]
        assert len(blokken[0]["rows"]) == 2


class TestStructureerAntwoord:
    def test_lege_input(self):
        assert S.structureer_antwoord(None, None) == []

    def test_alleen_ca(self):
        blokken = S.structureer_antwoord("Antwoord", None)
        assert len(blokken) == 1
        assert blokken[0]["type"] == "motivatie"

    def test_fallback_bij_simpele_motivering(self):
        # Eén korte paragraaf zonder structuur → motivatie-blok
        ca = "Antwoord X"
        am = "Korte uitleg zonder structuur."
        blokken = S.structureer_antwoord(ca, am)
        assert blokken
        # Motivatie-blok aanwezig
        assert any(b["type"] == "motivatie" for b in blokken)

    def test_definitie_blok_bij_type(self):
        ca = "Het is een definitie."
        am = "**Een definitie** is iets dat een fenomeen beschrijft. ⚖️\n\n_Grondslag: ISA 200._"
        blokken = S.structureer_antwoord(ca, am, antwoord_type="definitie")
        types = [b["type"] for b in blokken]
        assert "definitie" in types
        assert "grondslag" in types
        # Definitie-blok heeft lemma + zin
        d = [b for b in blokken if b["type"] == "definitie"][0]
        assert d["lemma"] == "Een definitie"
        assert "Een definitie" in d["definitie_zin"]

    def test_opsomming_bij_type(self):
        am = (
            "Oorzaken:\n\n"
            "1. **Eerste oorzaak** — uitleg hier. ⚖️\n"
            "2. **Tweede oorzaak** — uitleg twee. ⚖️\n"
            "3. **Derde oorzaak** — uitleg drie. 🤖\n\n"
            "_Grondslag: KB WVV art. 3:130._"
        )
        blokken = S.structureer_antwoord("Drie oorzaken", am, antwoord_type="opsomming")
        types = [b["type"] for b in blokken]
        assert "opsomming" in types
        ops = [b for b in blokken if b["type"] == "opsomming"][0]
        assert len(ops["items"]) == 3
        assert ops["items"][0]["lemma"] == "Eerste oorzaak"
        assert ops["items"][0]["confidence"] == "grounded"
        assert ops["items"][2]["confidence"] == "inferred"

    def test_procedure_bij_type(self):
        am = (
            "Stappen:\n\n"
            "1. **Brief opstellen** — auditor stelt brief op. ⚖️\n"
            "2. **Cliënt tekenen** — handtekening cliënt. ⚖️\n"
            "3. **Versturen** — auditor verstuurt. ⚖️\n"
        )
        blokken = S.structureer_antwoord("Werkwijze", am, antwoord_type="procedure")
        types = [b["type"] for b in blokken]
        assert "procedure" in types
        proc = [b for b in blokken if b["type"] == "procedure"][0]
        assert len(proc["stappen"]) == 3
        assert proc["stappen"][0]["nummer"] == 1

    def test_boekingsblok_in_kwalificatie(self):
        am = (
            "Boekhoudkundige verwerking:\n\n"
            "### Stap 1: Bij toezegging\n\n"
            "```\n"
            "Debet 416 Diverse vorderingen 10.000,00\n"
            "Credit 15 Kapitaalsubsidies 10.000,00\n"
            "```\n\n"
            "_Grondslag: KB WVV art. 3:50._"
        )
        blokken = S.structureer_antwoord("Boekingen", am, antwoord_type="kwalificatie")
        types = [b["type"] for b in blokken]
        assert "boeking" in types
        assert "grondslag" in types

    def test_conclusie_blok(self):
        am = "Lange redenering.\n\n**Conclusie:** Optie 3 is juist."
        blokken = S.structureer_antwoord("3", am)
        types = [b["type"] for b in blokken]
        assert "conclusie" in types

    def test_strict_geen_nieuwe_inhoud(self):
        """Bij onstructureerbare input: één motivatie-blok met volledige tekst.

        Geen verzonnen grondslag, geen verzonnen claims.
        """
        am = "Een vrijgevormde tekst zonder duidelijke structuur of markers."
        blokken = S.structureer_antwoord("X", am)
        assert len(blokken) == 1
        assert blokken[0]["type"] == "motivatie"
        assert blokken[0]["inhoud"] == am


class TestStructureerKwalificatieMetTabel:
    def test_tabel_en_grondslag(self):
        am = """
**Regel**: stemrecht > 50% → integrale consolidatie. ⚖️

| Deelneming | Controle | Methode |
|---|---|---|
| M in A | 70 % | Integraal |
| M in B | 30 % | Equity |

_Grondslag: KB WVV art. 3:124._
"""
        blokken = S.structureer_antwoord("Zie tabel", am, antwoord_type="kwalificatie")
        types = [b["type"] for b in blokken]
        assert "tabel" in types
        assert "grondslag" in types


class TestExtraheerJuistFout:
    def test_inline_pijl(self):
        am = (
            "a) De stelling over winst → fout, omdat er geen winst meer is.\n"
            "b) De stelling over schuld → juist, want de boeking klopt.\n"
        )
        blokken, rest = S._extraheer_juist_fout(am, antwoord_type="kwalificatie")
        assert len(blokken) == 2
        assert blokken[0]["juistheid"] == "fout"
        assert blokken[1]["juistheid"] == "juist"
        assert "winst" in blokken[0]["claim"].lower()
        assert "geen winst meer is" in blokken[0]["motivatie"]

    def test_geen_match(self):
        am = "Gewone prozatekst zonder stellingen."
        blokken, rest = S._extraheer_juist_fout(am, antwoord_type="kwalificatie")
        assert blokken == []
        assert rest == am


class TestExtraheerMCKeuze:
    def test_antwoord_optie_b(self):
        am = "Antwoord: optie B. Dit is de juiste keuze omdat het saldo klopt."
        blok, rest = S._extraheer_mc_keuze(am, antwoord_type="kwalificatie")
        assert blok is not None
        assert blok["geselecteerde_labels"] == ["B"]
        assert "juiste keuze" in blok.get("motivatie", "")

    def test_meerdere_labels(self):
        am = "Antwoord: A en C. Beide voldoen aan de criteria."
        blok, rest = S._extraheer_mc_keuze(am, antwoord_type="kwalificatie")
        assert blok is not None
        assert set(blok["geselecteerde_labels"]) == {"A", "C"}

    def test_geen_match(self):
        am = "Gewone proza zonder MC-keuze."
        blok, rest = S._extraheer_mc_keuze(am, antwoord_type="kwalificatie")
        assert blok is None


class TestValidatorNieuweTypes:
    def test_juist_fout_geldig(self):
        from tools.examen import validate_antwoord_blokken_v1 as V

        b = {
            "type": "juist_fout",
            "claim": "Schuld is overgeboekt naar kapitaal",
            "juistheid": "juist",
            "motivatie": "Want art. X.",
        }
        assert V.valideer_blok(b, "t") == []

    def test_juist_fout_ongeldige_juistheid(self):
        from tools.examen import validate_antwoord_blokken_v1 as V

        b = {"type": "juist_fout", "claim": "x", "juistheid": "misschien"}
        fouten = V.valideer_blok(b, "t")
        assert any("juistheid" in x for x in fouten)

    def test_mc_keuze_geldig(self):
        from tools.examen import validate_antwoord_blokken_v1 as V

        b = {
            "type": "mc_keuze",
            "geselecteerde_labels": ["B"],
            "motivatie": "Klopt.",
            "verworpen_labels_met_motivatie": [
                {"label": "A", "motivatie": "Te eng."}
            ],
        }
        assert V.valideer_blok(b, "t") == []

    def test_mc_keuze_mist_labels(self):
        from tools.examen import validate_antwoord_blokken_v1 as V

        b = {"type": "mc_keuze", "motivatie": "Klopt."}
        fouten = V.valideer_blok(b, "t")
        assert any("geselecteerde_labels" in x for x in fouten)
