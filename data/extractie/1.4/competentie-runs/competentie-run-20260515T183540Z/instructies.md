# Competentie-destillatie-run competentie-run-20260515T183540Z — Instructies voor Opus

**Programmaonderdeel**: 1.4
**Run-id**: competentie-run-20260515T183540Z
**Gegenereerd op**: 2026-05-15T18:35:40+00:00
**Model**: claude-opus-4-7

## Jouw taak

Destilleer 5–12 competentie-voorstellen voor programmaonderdeel 1.4
conform `prompts/competentie-destillatie-v1.md`.

**KRITISCH**: Gebruik GEEN examenvragen als input. Alleen de meegeleverde
concept-records, anchors en exam_patterns.

## Anti-fabricatie-regels (hard — herhaling voor zekerheid)

1. Stel ALLEEN competenties voor waarvan de procedure mechanisch afleidbaar is
   uit de gerefereerde concept-records hieronder.
2. Elke stap MOET grondslag.ref hebben — [[concept-id]], wettekst, of
   type: praktijk met expliciete motivering.
3. gebaseerd_op_concepten ≥ 2 verplicht.
4. Voorbeelden ALLEEN op basis van scenario's uit de definitie-teksten hieronder.
5. procedure_grondslag.wettelijk_pct + praktijk_pct == 100.

## Input-bestanden

- **Records** (30 stuks):
  
- `belangenpercentage` (begrip): Het economische eigendomsaandeel dat een moedervennootschap (direct en indirect, naar rato vermenigv...  - `consolidatiekring` (begrip): De verzameling entiteiten die in de geconsolideerde jaarrekening worden opgenomen: de consoliderende...  - `consolidatieverplichting` (regel): Elke moedervennootschap die, alleen of gezamenlijk, één of meer dochterondernemingen controleert, is...  - `consolidatieverschil` (fenomeen): Het verschil dat ontstaat bij de eerste consolidatie tussen (a) de aanschaffingswaarde van een deeln...  - `consortium` (actor): Een horizontale groep van vennootschappen die niet door een onderlinge moeder-dochter-relatie verbon...  - `controle` (begrip): De bevoegdheid in rechte of in feite om een beslissende invloed uit te oefenen op de aanstelling van...  - `controlepercentage` (begrip): Het percentage van de stemrechten dat een vennootschap (direct of indirect via dochterondernemingen)...  - `dochteronderneming` (actor): De vennootschap (dochtervennootschap) of het organisme (in ruime zin volgens WVV art. 3:22) ten opzi...  - `eerste-consolidatie` (fenomeen): De boekjaar-overschrijdende boekhoudkundige verwerking waarbij een nieuw verworven (of voor het eers...  - `evenredige-consolidatie` (methode): Een gemeenschappelijke dochteronderneming (een vennootschap waarover een beperkt aantal vennoten gez...  - `exclusieve-controle` (begrip): De controle die één vennootschap alleen uitoefent over een andere vennootschap, in tegenstelling tot...  - `geassocieerde-onderneming` (actor): Een onderneming, andere dan een dochteronderneming of een gemeenschappelijke dochteronderneming, waa...  - `geconsolideerd-jaarverslag` (begrip): Het door het bestuursorgaan opgestelde toelichtende verslag dat samen met de geconsolideerde jaarrek...  - `geconsolideerde-jaarrekening` (begrip): De jaarrekening die het vermogen, de financiële positie en het resultaat van het geconsolideerde geh...  - `gemeenschappelijke-dochteronderneming` (actor): De vennootschap of onderneming ten opzichte waarvan een gezamenlijke controle bestaat: een beperkt a...  - `gezamenlijke-controle` (begrip): De controle die een beperkt aantal vennoten samen uitoefenen, wanneer zij zijn overeengekomen dat be...  - `groep-van-beperkte-omvang` (begrip): Een groep die op geconsolideerde of geaggregeerde basis niet meer dan één van de criteria van WVV ar...  - `groottecriteria-consolidatie` (drempel): Een moedervennootschap is vrijgesteld van de verplichting om een geconsolideerde jaarrekening en jaa...  - `horizontale-consolidatie` (procedure): De consolidatietechniek die wordt toegepast wanneer vennootschappen onder centrale leiding staan zon...  - `ifrs-consolidatieraamwerk` (begrip): Het geheel van IAS/IFRS-standaarden die het wettelijk kader voor geconsolideerde jaarrekeningen onde...  - `integrale-consolidatie` (methode): De geconsolideerde jaarrekening voorstellen alsof het geheel van de consoliderende vennootschap en h...  - `intragroep-eliminaties` (procedure): Bij de opstelling van de geconsolideerde jaarrekening moeten alle wederzijdse opbrengsten, kosten, v...  - `invloed-van-betekenis` (begrip): De macht om deel te nemen aan de financiële en operationele beleidsbeslissingen van een andere onder...  - `minderheidsbelangen` (fenomeen): Het deel van het eigen vermogen en van het resultaat van integraal geconsolideerde dochters dat kan ...  - `moedervennootschap` (actor): De vennootschap die een controlebevoegdheid uitoefent over een andere vennootschap (de dochtervennoo...  - `step-acquisition` (fenomeen): Het fenomeen waarbij een onderneming haar belang in een andere onderneming in twee of meer fasen ver...  - `uniforme-waarderingsregels-consolidatie` (regel): De consoliderende vennootschap moet, onverminderd KB WVV art. 3:118, voor haar geconsolideerde jaarr...  - `vermogensmutatiemethode` (methode): Een deelneming wordt in de geconsolideerde jaarrekening niet activum-per-activum opgenomen, maar als...  - `vrijstelling-subconsolidatie` (regel): Een tussenliggende (sub)moedervennootschap wordt vrijgesteld van de verplichting om een geconsolidee...  - `wijziging-consolidatiekring` (fenomeen): Elke aanpassing aan de samenstelling van de consolidatiekring tussen twee opeenvolgende boekjaren: o...

- **Anchors** (13 stuks): `data/extractie/1.4/competentie-runs/competentie-run-20260515T183540Z`
- **Exam-patterns** (0 bestanden): vraagvormen + complexiteitspatronen

## Programmaonderdeel-context

Titel: Geconsolideerde jaarrekening en wetgeving betreffende de geconsolideerde jaarrekening
Intro: None

## Output-locatie

Schrijf elke competentie als YAML-bestand naar:
`data/concepten/competenties/<id>.yaml`

Schema: zie `prompts/competentie-destillatie-v1.md` §Output-schema

---

## Prompt-referentie (competentie-destillatie-v1.md)

# Prompt: Competentie-destillatie — Fase D (v1)

**Doel**: Destilleer competentie-voorstellen voor een programmaonderdeel uit anchors + concept-records + exam_patterns. Het aantal volgt uit wat het programmaonderdeel werkelijk vraagt — geen vooraf vastgelegd target.

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

- **Geen vooraf vastgelegd aantal.** Stel zoveel competenties voor als het programmaonderdeel werkelijk vraagt. Te weinig is onvolledig; te veel verwatert. Bij twijfel: liever twee scherpe dan één brede.
- Prefereer compacte, duidelijk afgebakende competenties boven brede "alles-competenties".
- Een competentie verdient pas een eigen fiche als ze een herkenbare cliëntsituatie of beslissing dekt. Geen pseudo-competenties voor concepten die louter "kennen" zijn (die horen bij de concept-laag).
- Cross-PO competenties (die ook bij andere PO's relevant zijn): gebruik `programmaonderdelen: [X.Y, Z.W]`.

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

