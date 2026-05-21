---
title: Herstructureren van de resultatenrekening en isoleren van de toegevoegde waarde
tags:
- concept
- competentie
- po-1-9
linked_anchors:
- 1.9.taak.1
- 1.9.III
- 1.9.III.B
- 1.9.III.C
- 1.9.V.A
programmaonderdelen:
- '1.9'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/herstructureren-resultatenrekening-en-toegevoegde-waarde.json
gegenereerd_op: '2026-05-21'
---
# Herstructureren van de resultatenrekening en isoleren van de toegevoegde waarde 🔗

Operationele competentie: de wettelijke resultatenrekening herwerken naar de vier blokken (bedrijfs-, financieel, uitzonderlijk, belastingen) en binnen het bedrijfsblok de toegevoegde waarde isoleren. Vraagt extra werk voor verkort/microschema waar bepaalde rubrieken samengevoegd zijn — accountant moet desaggregatie reconstrueren via toelichtingsstaten.



## Stappen

### 1. Identificeren van het jaarrekeningschema

Bepaal of de onderneming rapporteert in volledig, verkort of microschema en welke gevolgen dat heeft voor de detail-niveau van de resultatenrekening.

**Waarom?** Het schema bepaalt of aankopen handelsgoederen (60) van diensten en diverse goederen (61) gescheiden zijn — dat detail is nodig om toegevoegde waarde correct te berekenen.

**📥 Input**:
- Neergelegde jaarrekening (eDepot) → **Schema-indicator + rubriekenstructuur RR** _(document)_

**📤 Output**:
- Schema-classificatie → **volledig / verkort / micro** _(conclusie)_

**🛠️ Hoe**:

1. Open de gepubliceerde jaarrekening op de NBB-Centrale voor Balansen.
2. Lees de schema-aanduiding bovenaan (model 11 voor verkort, model 11a voor micro, model 10 voor volledig).
3. Controleer of rubrieken 60 en 61 afzonderlijk zijn of samengevoegd. Volgens [[herstructurering-resultatenrekening]] §verkort-microschema vraagt verkort/micro bijkomende toelichting voor TW-detail.


**Grondslag**: [[herstructurering-resultatenrekening]] §verkort-microschema, KB WVV — schemas 10/11/11a

### 2. Groeperen van rubrieken in vier blokken

Herorden de resultatenrekening in bedrijfsblok (60-64 + 70-74), financieel blok (65 + 75), uitzonderlijk blok (66 + 76, indien oud schema) en belastingblok (67 + 77).

**Waarom?** Elk blok beantwoordt een andere analyse-vraag: bedrijf = winstgevendheid kernactiviteit, financieel = financieringskost-impact, uitzonderlijk = eenmalige items, belasting = effectieve aanslagvoet.

**📥 Input**:
- RR uit jaarrekening → **Alle 6X- en 7X-rubrieken met bedragen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geherstructureerde RR-tabel → **Vier sub-totalen per blok + nettoresultaat** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Pas de groepering toe uit [[herstructurering-resultatenrekening]] §vier-blokken.
2. Bereken per blok het sub-totaal (opbrengsten min kosten).
3. Sluit af met nettoresultaat = som van de vier blok-resultaten.
4. Bij nieuw WVV-schema: blok "uitzonderlijk" is meestal leeg — vermeld dit expliciet en herschik eenmalige items naar bedrijfs- of financieel blok zoals het schema voorschrijft.


> [!example]- Voorbeeld: Rotex Roeselare NV — boekjaar 20X3, volledig schema
> Rotex Roeselare NV — boekjaar 20X3, volledig schema.
>
> 1. **Vier-blokken-herstructurering** 🧮
>
>    | Blok | Opbrengsten | Kosten | Sub-totaal |
>    |---|---:|---:|---:|
>    | Bedrijfsresultaat | € 51.000.000 | € 45.000.000 | + € 6.000.000 |
>    | Financieel resultaat | € 100.000 | € 700.000 | − € 600.000 |
>    | Uitzonderlijk resultaat | — | — | € 0 |
>    | Belastingen | — | € 1.500.000 | − € 1.500.000 |
>    | **Nettoresultaat** | | | **+ € 3.900.000** |
>    
>
> 2. **Opmerking nieuw schema** 💬
>
>    In het nieuwe WVV-schema verdwijnt het uitzonderlijk blok grotendeels. Eenmalige items zijn nu in het bedrijfsblok geïntegreerd (rubrieken 76 → 74/64). Vermeld dit in de notitie bij de geherstructureerde RR.
>    
>

**Grondslag**: [[herstructurering-resultatenrekening]] §vier-blokken, KB WVV — schema RR

### 3. Berekenen van de toegevoegde waarde

Bereken toegevoegde waarde als bedrijfsopbrengsten min aankopen goederen en diensten van derden.

**Waarom?** Toegevoegde waarde toont de welvaart die de onderneming zelf creëert — de basis voor productiviteitsmaten (TW per VTE) en voor de verdeling-analyse over productiefactoren.

**📥 Input**:
- Geherstructureerde RR (stap 2) → **Rubrieken 70 + 71 + 72 + 74 + 60 + 61** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Toegevoegde waarde in € → **Eén bedrag + TW per VTE** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Pas de formule toe uit [[toegevoegde-waarde-financiele-analyse]] §formule: TW = bedrijfsopbrengsten − aankopen goederen en diensten van derden.
2. Tel de bedrijfsopbrengsten: omzet (70) + andere bedrijfsopbrengsten (74) + voorraadwijziging gereed product en bestellingen in uitvoering (71) + geactiveerde productie (72).
3. Trek af: aankopen handelsgoederen, grond- en hulpstoffen (60) + diensten en diverse goederen (61).
4. Deel door het gemiddeld aantal voltijdse equivalenten (sociale balans) om TW per VTE te bekomen.


> [!example]- Voorbeeld: Rotex Roeselare NV — TW boekjaar 20X3
> Rotex Roeselare NV — TW boekjaar 20X3.
>
> 1. **Bouwstenen RR** 🧮
>
>    Omzet (70): € 50.000.000
>    Voorraadwijziging (71): + € 200.000
>    Andere bedrijfsopbrengsten (74): € 800.000
>    Aankopen handelsgoederen (60): − € 25.000.000
>    Diensten en diverse goederen (61): − € 8.000.000
>    
>
> 2. **Berekening** 🧮
>
>    TW = € 50.000.000 + € 200.000 + € 800.000 − € 25.000.000 − € 8.000.000 = **€ 18.000.000**
>    Gemiddeld VTE: 120
>    TW per VTE = € 18.000.000 / 120 = **€ 150.000 per VTE**
>    
>

**Grondslag**: [[toegevoegde-waarde-financiele-analyse]] §formule, [[herstructurering-resultatenrekening]] §isoleer-toegevoegde-waarde

### 4. Verdelen van de toegevoegde waarde over de productiefactoren

Analyseer hoe de TW verdeeld wordt over personeel (lonen + sociale lasten), kapitaalverschaffers (financiële kosten + dividenden), overheid (belastingen) en de onderneming zelf (reserves + afschrijvingen).

**Waarom?** De verdeling toont strategische posities: een onderneming met hoge personeels-share is arbeidsintensief; eentje met hoge zelf-bestemming bouwt zelffinanciering op. Examenvraag op bekwaamheid-niveau verwacht deze interpretatie.

**📥 Input**:
- Geherstructureerde RR + TW (stappen 2-3) → **Personeelskosten (62), afschrijvingen (630), financiële kosten (65), belastingen (67), netto-resultaat** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Verdelingstabel TW → **Per productiefactor: bedrag + percentage van TW** _(conclusie)_

**🛠️ Hoe**:

1. Lijst de vier bestemmingen uit [[toegevoegde-waarde-financiele-analyse]] §verdeling-productiefactoren.
2. Personeel = rubriek 62 (lonen, sociale lasten, pensioenen).
3. Kapitaalverschaffers = financiële kosten (65) + uitgekeerde dividenden uit resultaatverwerking.
4. Overheid = belastingen op resultaat (67).
5. Onderneming zelf = afschrijvingen (630) + dotaties aan reserves + overgedragen resultaat.
6. Bereken per bestemming het percentage van TW. Som = 100% (controle).


> [!example]- Voorbeeld: Rotex Roeselare NV — verdeling TW 20X3
> Rotex Roeselare NV — verdeling TW 20X3.
>
> 1. **Verdelingstabel** 🧮
>
>    | Bestemming | Bedrag | % van TW |
>    |---|---:|---:|
>    | Personeel (62) | € 12.000.000 | 66,7% |
>    | Onderneming (afschr. + reserves) | € 2.700.000 | 15,0% |
>    | Overheid (belastingen) | € 1.500.000 | 8,3% |
>    | Kapitaalverschaffers (financ. + div.) | € 1.800.000 | 10,0% |
>    | **Totaal** | **€ 18.000.000** | **100%** |
>    
>
> 2. **Interpretatie** 💬
>
>    Rotex Roeselare NV is matig arbeidsintensief (67% naar personeel — sector mediaan ligt rond 70%). Zelf-bestemming 15% wijst op gezonde herinvestering. Aandeel kapitaalverschaffers laag = beperkte schuldfinanciering. Combineer met solvabiliteitsratio voor compleet beeld.
>    
>

**Grondslag**: [[toegevoegde-waarde-financiele-analyse]] §verdeling-productiefactoren

> [!warning]- Tel afschrijvingen mee onder "onderneming zelf" — ze zijn de impliciete kapitaal-vergoeding voor in het verleden geïnvesteerde middelen.
>
> _Vaak fout gedaan_: Afschrijvingen vergeten of bij "kapitaalverschaffers" plaatsen. Ze zijn geen cashuitkering aan derden maar interne herallocatie.
>
> _Grondslag_: [[toegevoegde-waarde-financiele-analyse]] §verdeling-productiefactoren


## Voorbeelden




## Bronnen

[^1]: `aggregate`
