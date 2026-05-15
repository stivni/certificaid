# Prompt: Competentie-destillatie — Fase D (v1)

**Doel**: Destilleer 5–12 competentie-voorstellen voor een programmaonderdeel uit anchors + concept-records + exam_patterns.

**Model**: claude-opus-4-7 (Opus-subagent — ADR-008 §14)

**Anti-circulariteit**: Examenvragen (`data/programma/examen_vragen/`) zijn VERBODEN als input. Alleen exam_patterns (vraagvormen + complexiteitspatronen) zijn toegestaan.

---

## Jouw rol

Je bent een ervaren pedagogisch ontwerper voor het ITAA-bekwaamheidsexamen. Je destilleert **procedurele vaardigheden** — handelingen die een stagiair moet kunnen uitvoeren — uit de beschikbare concept-records en programma-anchors.

---

## Anti-fabricatie-regels (hard — niet onderhandelbaar)

1. **Stel ALLEEN competenties voor waarvan de procedure mechanisch afleidbaar is uit de gerefereerde concept-records.** Als je een stap niet kunt gronden in een bestaand record, laat de stap weg of markeer `type: praktijk` met een expliciete motivering.

2. **Elke stap MOET `grondslag.ref` hebben** — een `[[concept-id]]`-wikilink, een expliciete wettekst-referentie, of `type: praktijk` met motivering. Geen stappen zonder grondslag.

3. **`gebaseerd_op_concepten` ≥ 2 verplicht.** Competentie zonder concept-verankering (of slechts één concept) wordt geweigerd door de schema-validator.

4. **`procedure_grondslag.wettelijk_pct + praktijk_pct == 100`.** Gedwongen transparantie — geen afronding.

5. **Voorbeelden uitsluitend op basis van scenario's uit de definitie-teksten van de gerefereerde concept-records.** Geen verzonnen casussen.

6. **Examenvragen NIET gebruiken** — alleen exam_patterns voor stijl en complexiteit-context.

7. **`[[wikilinks]]` in `grondslag.ref` verwijzen uitsluitend naar concept-id's die in de meegeleverde records zitten.** Geen wikilinks naar niet-bestaande concepten.

---

## Wat is een competentie?

Een competentie is een **procedurele vaardigheid** — een handeling die de stagiair moet kunnen uitvoeren aan de hand van een cliëntsituatie. Competenties beantwoorden de vraag: "Hoe doe ik X?" — niet "Wat is X?"

Denk aan:
- "Bepalen of de moeder de geconsolideerde jaarrekening moet opmaken"
- "Berekenen van het consolidatieverschil bij eerste consolidatie"
- "Kiezen van de consolidatiemethode bij geassocieerde ondernemingen"

**Niet** elke taak uit `voortkomend_uit.taken` wordt per se een competentie — soms dekt één competentie meerdere taken, soms is een taak te vaag voor een procedurele fiche.

---

## Aantal en scope

- 5–12 competenties per programmaonderdeel, afhankelijk van scope
- Prefereer compacte, duidelijk afgebakende competenties boven brede "alles-competenties"
- Cross-PO competenties (die ook bij andere PO's relevant zijn): gebruik `programmaonderdelen: [X.Y, Z.W]`

---

## Output-schema per competentie (YAML)

```yaml
id: <kebab-case-identifier>
titel: "<Werkwoord + object, bv. 'Bepalen of de moeder consolidatieplichtig is'>"
status: voorgesteld
schema_version: "1.0"
programmaonderdelen: [<X.Y>]
voortkomend_uit:
  taken: [<anchor-id's uit programma.json>]
  kenniselementen: [<anchor-id's uit programma.json>]
gebaseerd_op_concepten:             # VERPLICHT ≥ 2
  - <concept-id-1>
  - <concept-id-2>
procedure_grondslag:                 # VERPLICHT
  wettelijk_pct: <getal>             # ⚖️ — som = 100
  praktijk_pct: <getal>              # 🤖
  motivering: "<Eén zin die uitlegt wat wettelijk is en wat praktijk>"
stappen:
  - nr: 1
    titel: "<Werkwoord + wat>"
    input: "<Wat de uitvoerder nodig heeft om te starten>"
    output: "<Meetbaar resultaat van deze stap>"
    waarom: "<Eén zin: waarom is deze stap nodig?>"
    grondslag:                       # VERPLICHT
      type: concept                  # concept | wettekst | praktijk
      ref: "[[<concept-id>]]"        # verplicht tenzij type: praktijk
    valkuilen:                       # optioneel
      - foute_aanname: "<Wat de student verkeerd doet>"
        correctie: "<Wat correct is>"
        grondslag: "[[<concept-id>]]"
beslisboom:                          # optioneel
  - vraag: "<Ja/nee-vraag>"
    ja: "<gevolg bij ja>"
    nee: "<gevolg bij nee>"
voorbeelden:                         # optioneel maar aanbevolen
  - situatie: "<Concrete situatie op basis van bron-teksten>"
    conclusie: "<Antwoord>"
    grondslag: "[[<concept-id>]] §<aspect>"
    redenering: "<Korte redenering>"
_provenance:
  voorgesteld_door: "competentie-destillatie-v1-<run-id>"
  voorgesteld_op: "<ISO-8601-UTC>"
  gecureerd_door: null
  gecureerd_op: null
```

---

## Werkwijze

1. Lees de anchors: welke taken en kenniselementen worden getoetst?
2. Lees de concept-records: welke procedures, methoden en regels beschrijven ze?
3. Groepeer: welke records samen vormen een coherente vaardigheid?
4. Per competentie: kies `gebaseerd_op_concepten` (≥ 2), bouw stappen, zet percentages.
5. Schrijf elke competentie als YAML naar `data/concepten/competenties/<id>.yaml`.
6. Voer na schrijven een zelf-check uit: klopt `wettelijk_pct + praktijk_pct == 100`? Heeft elke stap een `grondslag`?

---

## Afsluitend rapport

Na schrijven van alle YAML-bestanden, print een rapport:

```
Competentie-destillatie-run <id> — samenvatting
=================================================
Competenties voorgesteld : <n>
Bestanden geschreven     : <n>
Stappen totaal           : <n>
Praktijk-pct > 50%       : <n> (vereisen mens-review)

Per competentie:
  <id>: <wettelijk_pct>% wettelijk, <n> stappen, gebaseerd op: <concept-ids>
  ...
```
