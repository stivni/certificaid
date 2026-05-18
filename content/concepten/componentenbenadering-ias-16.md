---
title: Componentenbenadering (IAS 16) — afschrijving per onderdeel
tags:
- concept
- cluster
- po-1-5
linked_anchors:
- 1.5.V.A
- 1.5.V.B
- 1.5.V
programmaonderdelen:
- '1.5'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/componentenbenadering-ias-16.json
gegenereerd_op: '2026-05-18'
---
# Componentenbenadering (IAS 16) — afschrijving per onderdeel ⚖️

> [!summary] Korte inhoud
> De componentenbenadering (IAS 16 alinea 43-47) verplicht een entiteit om elk **bestanddeel** (component) van een materieel vast actief met een **substantiële kostprijs** in verhouding tot de totale kostprijs van het actief **afzonderlijk af te schrijven** wanneer dat bestanddeel….

> [!info] Behoort tot: [[materiele-vaste-activa-ifrs]]

De componentenbenadering (IAS 16 alinea 43-47) verplicht een entiteit om elk **bestanddeel** (component) van een materieel vast actief met een **substantiële kostprijs** in verhouding tot de totale kostprijs van het actief **afzonderlijk af te schrijven** wanneer dat bestanddeel een andere gebruiksduur of een ander verbruikspatroon heeft dan de rest van het actief. Componenten met dezelfde gebruiksduur én methode mogen gegroepeerd worden. Overige bestanddelen (zonder substantieel deel in de kostprijs) mogen samen worden afgeschreven volgens een 'rest'-categorie, met benaderingstechnieken indien nodig.

_Bron: IAS 16 alinea 43-47_


## Bouwstenen

### Wat is een 'substantiële kostprijs'? ⚖️

IAS 16 definieert geen vaste drempel. De entiteit maakt een **professional judgment**: een component is substantieel als zijn kostprijs significant is in verhouding tot de totale kostprijs van het actief. In de praktijk wordt vaak 10-15% van het totaal als richtlijn gehanteerd, maar dat is geen IFRS-regel.

**Waarom?** Een rigide percentage zou willekeur creëren. Bij een vliegtuig is een motor van 5% van de totaalkostprijs nog steeds zo belangrijk dat aparte afschrijving zinvol is; bij een gebouw is een lift van 5% misschien op te nemen onder 'rest'.

**Voorbeeld**: Zelena Bio's productielijn (kostprijs € 13.800.000): motor € 4.000.000 (29%), reactor € 7.000.000 (51%), bedieningssoftware € 2.800.000 (20%). Alle drie boven 15% → alle drie afzonderlijk afschrijven.

_Grondslag: IAS 16 alinea 43 + judgment_

### Vervanging — oude component schrappen ⚖️

Wanneer een component wordt vervangen, neem je de **boekwaarde van het vervangen onderdeel niet langer op** (alinea 70). Indien die boekwaarde niet meer afzonderlijk te bepalen is, mag je de **kosten van de vervanging gebruiken als indicatie** voor de oorspronkelijke kostprijs van het vervangen onderdeel (uiteraard verminderd met geaccumuleerde afschrijvingen).

**Waarom?** Een nieuw onderdeel activeren zonder het oude eruit te halen zou dubbel-tellen op de balans. De componentenbenadering werkt alleen als je consistent oude én nieuwe onderdelen behandelt.

**Voorbeeld**: In 2034 (na 8 jaar) wordt de motor van Zelena Bio's productielijn vervangen. Oude motor: kostprijs € 4.000.000, geaccumuleerde afschrijving 8/8 × € 4.000.000 = € 4.000.000 → boekwaarde € 0. Nieuwe motor: kostprijs € 5.500.000 → geactiveerd, afgeschreven over 8 jaar (€ 687.500/jaar).

_Grondslag: IAS 16 alinea 13 + 70_

### Grondige inspecties — eigen component ⚖️

Periodieke **grondige inspecties** (bv. revisie van een vliegtuig elke 5 jaar, regulatoir verplichte controle van een installatie) mogen als afzonderlijke 'component' worden behandeld: de kostprijs van de inspectie wordt geactiveerd en afgeschreven tot de volgende inspectie (alinea 14).

**Waarom?** Inspectiekosten zijn substantieel maar niet aan een fysiek onderdeel verbonden. Ze als kost meteen erkennen zou een ongelijke verdeling van kosten over de tijd geven; ze activeren en spreiden tot de volgende inspectie is conceptueel correcter.

**Voorbeeld**: Zelena Bio's reactor vereist elke 5 jaar een wettelijk verplichte grondige inspectie (kosten € 800.000). Bij aanschaf wordt € 800.000 als 'inspectie-component' geactiveerd, afgeschreven over 5 jaar. Bij volgende inspectie: oude inspectiekost niet langer opnemen + nieuwe € 800.000 activeren.

_Grondslag: IAS 16 alinea 14_


## Berekening

### Splitsing kostprijs in componenten — voorbeeld productielijn

*Identificeer elke component met substantiële kostprijs en verschillende gebruiksduur. Bereken jaarlijkse afschrijving per component. Totaal jaarafschrijving = som over alle componenten.*

### 1. Identificeer de componenten

Maak een inventaris van de fysieke en logische onderdelen met verschillende gebruiksduur of verbruikspatroon.

**Waarom?** Zonder identificatie geen componentenbenadering. De inventaris vormt de basis voor alle latere afschrijvingsberekeningen.

**📥 Input**:
- Technische documentatie installatie → **Onderdelenlijst met levensduur** _(documentatie)_

**📤 Output**:
- Componenteninventaris → **Lijst van onderscheiden bestanddelen** _(registerlijst)_

**🛠️ Hoe**:

1. Vraag technische documentatie op van de fabrikant van de productielijn van Zelena Bio.
2. Identificeer onderdelen met eigen vervangingsschema: motor (8 jaar), reactor (20 jaar), bedieningssoftware (5 jaar).
3. Documenteer in vastactivafile per component.

**Grondslag**: IAS 16 alinea 43

### 2. Verdeel de totale kostprijs

Reken een fractie van de totale kostprijs toe aan elke component. Methode: facturatie-uitsplitsing van fabrikant of relatieve marktwaarde.

**Waarom?** De afschrijving per component moet vertrekken van een correcte kostprijs. Verkeerde toerekening = verkeerd afschrijvingsbedrag.

**📥 Input**:
- Inkoopfactuur productielijn → **Per-component-prijs of totaal** _(boekhoudkundig-bedrag)_
- Componenteninventaris → **Onderdelenlijst** _(registerlijst)_

**📤 Output**:
- Componentenboek → **Kostprijs per component** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Vraag de fabrikant om een uitsplitsing in zijn factuur.
2. Voor Zelena Bio: motor € 4.000.000, reactor € 7.000.000, software € 2.800.000 — totaal aankoopprijs € 13.800.000.
3. Indien geen factuuruitsplitsing: gebruik relatieve marktwaarde of professionele schatting.

**Grondslag**: IAS 16 alinea 44

### 3. Bereken jaarlijkse afschrijving per component

Afschrijving = (kostprijs − restwaarde) / gebruiksduur, per component afzonderlijk.

**Waarom?** Verschillende componenten verbruiken aan verschillend tempo. Aparte afschrijvingsplannen geven de getrouwste cost-allocation.

**📥 Input**:
- Componentenboek → **Kostprijs, restwaarde, gebruiksduur** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Afschrijvingstabel → **Jaarlijkse afschrijving per component** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Voor de motor van Zelena Bio (restwaarde 0): € 4.000.000 / 8 = € 500.000/jaar.
2. Reactor: € 7.000.000 / 20 = € 350.000/jaar.
3. Software: € 2.800.000 / 5 = € 560.000/jaar.
4. Totaal jaarlijkse afschrijving = € 1.410.000.

> [!example]- Voorbeeld: Zelena Bio NV's productielijn: aanschaffingsdatum 1 januari 2026, kostprijs € 13.800.000
> Zelena Bio NV's productielijn: aanschaffingsdatum 1 januari 2026, kostprijs € 13.800.000.
>
> 1. **Componententabel met afschrijving** 🧮
>
>    | Component         | Kostprijs (€) | Gebruiksduur | Restwaarde (€) | Jaarafschrijving (€) |
>    |-------------------|--------------:|-------------:|---------------:|---------------------:|
>    | Motor             |     4.000.000 |        8 jaar |              0 |              500.000 |
>    | Reactor           |     7.000.000 |       20 jaar |              0 |              350.000 |
>    | Bedieningssoftware|     2.800.000 |        5 jaar |              0 |              560.000 |
>    | **Totaal**        |  **13.800.000** |             |                |        **1.410.000** |
>
> 2. **Vergelijking met niet-componenten-benadering** 🧮
>
>    Zou Zelena de hele productielijn als één actief afschrijven over 20 jaar (gemiddelde gewogen levensduur):
>    Jaarafschrijving = € 13.800.000 / 20 = € 690.000/jaar.
>    
>    Verschil: componenten-benadering geeft € 1.410.000/jaar in eerste 5 jaar (= +€ 720.000/jaar). Dit weerspiegelt het werkelijk snellere verbruik van software (5 jaar) en motor (8 jaar).
>

**Grondslag**: IAS 16 alinea 50 (afschrijfbaar bedrag)


## Valkuilen

> [!warning]- Componenten met dezelfde gebruiksduur EN dezelfde afschrijvingsmethode mogen wél worden samengevoegd (alinea 45)
> ⚠️ Componenten met dezelfde gebruiksduur EN dezelfde afschrijvingsmethode mogen wél worden samengevoegd (alinea 45). Niet alles hoeft afzonderlijk — het criterium is verschillend verbruikspatroon. ⚖️
>
> _Bron: IAS 16 alinea 45_


> [!warning]- Bij vervanging mag je de boekwaarde van het vervangen onderdeel NIET aanhouden naast het nieuwe — alinea 70 verplicht 'niet langer opnemen'
> ⚠️ Bij vervanging mag je de boekwaarde van het vervangen onderdeel NIET aanhouden naast het nieuwe — alinea 70 verplicht 'niet langer opnemen'. Anders heb je dubbel-tellen op de balans. ⚖️
>
> _Bron: IAS 16 alinea 70_



## Bronnen

[^1]: `IAS-16-materiele-vaste-activa__sec_waardering-na-eerste-opname`
[^2]: `IAS-16-materiele-vaste-activa__sec_niet-langer-opnemen`
[^3]: `IAS-16-materiele-vaste-activa__sec_opname`
