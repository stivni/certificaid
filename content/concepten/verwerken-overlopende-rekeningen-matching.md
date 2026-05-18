---
title: Verwerken van overlopende rekeningen volgens het matching-principe
tags:
- concept
- competentie
- po-1-1
linked_anchors:
- 1.1.taak.1
- 1.1.II.L
programmaonderdelen:
- '1.1'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/verwerken-overlopende-rekeningen-matching.json
gegenereerd_op: '2026-05-18'
---
# Verwerken van overlopende rekeningen volgens het matching-principe 🤖


## Stappen

### 1. Identificeer kosten/opbrengsten die periode-overschrijdend zijn

Stel een lijst op van facturen, contracten en bedragen die boeken vóór balansdatum maar economisch toebehoren aan een andere periode (of omgekeerd).

**Waarom?** Zonder identificatie loopt het resultaat scheef — kosten of opbrengsten worden in de verkeerde periode gerapporteerd.

**📥 Input**:
- Boekhoudoverzicht + contracten → **Huurcontracten, abonnementen, verzekeringen, interest, vakantiegeld, bonussen** _(document)_

**📤 Output**:
- Lijst overlopende posten → **Per item: kost/opbrengst + bedrag + periode-toewijzing** _(conclusie)_

**🛠️ Hoe**:

1. Overloop typische gevallen volgens [[overlopende-rekeningen]] §types:
   - Vooraf betaalde kosten: huur (rubriek 490), verzekeringspremie, leasing, abonnementen, prepaid software.
   - Toe te rekenen kosten: vakantiegeld, dertiende maand, niet-gefactureerde verbruiken, interestkost LT-schulden (rubriek 492).
   - Vooraf ontvangen opbrengsten: huur ontvangen, voorlopig betaalde subsidies (rubriek 493).
   - Toe te rekenen opbrengsten: rente op vorderingen, leasing-opbrengsten (rubriek 491).
2. Bij Uitgeverij Ukkel NV — verzekeringspremie € 12.000 betaald op 01/10/2026 voor periode 01/10/2026 → 30/09/2027. Op 31/12 is 3/12 verbruikt (€ 3.000) en 9/12 nog niet (€ 9.000).
3. Bij Rotex Roeselare NV — gas-verbruik dec 2026 nog niet gefactureerd op 31/12; geschat op € 4.500 op basis van vorige facturen.
4. Documenteer in werkdocument.


**Grondslag**: [[overlopende-rekeningen]] §identificatie, [[bedrijfsresultaat]] §matching

### 2. Bereken het pro-rata-bedrag per overlopende post

Splits het bedrag in een deel dat tot het lopende boekjaar behoort en een deel dat naar een ander boekjaar overgaat.

**Waarom?** Alleen het deel dat economisch in het lopende boekjaar valt mag in het resultaat blijven.

**📥 Input**:
- Lijst overlopende posten stap 1 → **Bedragen + periodes** _(berekening)_

**📤 Output**:
- Pro-rata-berekening per post → **Bedrag in periode / Bedrag uit periode** _(berekening)_

**🛠️ Hoe**:

1. Bereken pro-rata: bedrag × (dagen of maanden in lopend boekjaar) / (totaal dagen of maanden contract).
2. Voor verzekering Uitgeverij Ukkel NV — 3/12 × € 12.000 = € 3.000 binnen 2026 (kost); 9/12 × € 12.000 = € 9.000 over te dragen naar 2027 (actief 490).
3. Voor gas Rotex — volledige € 4.500 binnen 2026 (kost), nog te factureren door leverancier (passief 492).
4. Voor vakantiegeld voor te betalen in juni 2027 — opbouw 2026 + opname 2026 = ~ 18 dagen × loon = bv. € 28.000.


**Grondslag**: [[overlopende-rekeningen]] §pro-rata-berekening

### 3. Boek de aanpassing op de overlopende rekening

Boek elk pro-rata-bedrag op de juiste overlopende rekening (490/491/492/493) met tegenpost op de kost- of opbrengstrekening.

**Waarom?** De overlopende rekening "parkeert" het bedrag tot het andere boekjaar — daarna keert ze automatisch terug.

**📥 Input**:
- Pro-rata-berekening stap 2 → **Bedragen per post** _(berekening)_

**📤 Output**:
- Eindejaars-boekingen → **Per post een journaalpost** _(boekingsregel)_

**🛠️ Hoe**:

1. Vooraf betaalde kost: Debet 490 Over te dragen kosten; Credit 61X-kostrekening voor het deel dat naar volgend boekjaar verschuift.
2. Toe te rekenen kost: Debet 6X-kostrekening; Credit 492 Toe te rekenen kosten voor het deel dat nog niet gefactureerd is maar wel verbruikt.
3. Vooraf ontvangen opbrengst: Debet 70/74-opbrengstrekening; Credit 493 Over te dragen opbrengsten.
4. Toe te rekenen opbrengst: Debet 491 Verkregen opbrengsten; Credit 70/74-opbrengstrekening.
5. In begin volgend boekjaar: tegenboeking automatisch — bedrag keert naar resultatenrekening.


> [!example]- Voorbeeld: Uitgeverij Ukkel NV — verzekeringspremie € 12.000 betaald op 01/10/2026 voor periode 01/10/2026-30/09/2027
> Uitgeverij Ukkel NV — verzekeringspremie € 12.000 betaald op 01/10/2026 voor periode 01/10/2026-30/09/2027. Reeds geboekt op 01/10: D 6151 Verzekeringspremies € 12.000; C 5500 Bank € 12.000. Eindejaars-correctie op 31/12/2026.
>
> 1. **Berekening pro-rata** 🧮
>
>    Periode binnen 2026: 3 maanden (okt-nov-dec). Pro-rata 2026 = 3/12 × € 12.000 = € 3.000.
>    Periode binnen 2027: 9 maanden. Pro-rata 2027 = 9/12 × € 12.000 = € 9.000.
>    
>
> 2. **Boeking 31/12/2026 — overdracht naar 490** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 31/12/2026 | 490 Over te dragen kosten — verzekering | 9/12 deel 2027 | € 9.000,00 | |
>    | 31/12/2026 | 6151 Verzekeringspremies | terugname overschot 2026 | | € 9.000,00 |
>    
>
> 3. **Boeking 01/01/2027 — terug naar kost** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 01/01/2027 | 6151 Verzekeringspremies | terug binnen 2027 | € 9.000,00 | |
>    | 01/01/2027 | 490 Over te dragen kosten — verzekering | terugname | | € 9.000,00 |
>    
>

**Grondslag**: [[overlopende-rekeningen]] §boeking, KB-WVV art. 3:30

### 4. Verwerk toe te rekenen kosten (492) voor verbruik zonder factuur

Boek kosten die in het boekjaar zijn verbruikt maar pas later worden gefactureerd, op rubriek 492.

**Waarom?** Zonder deze boeking ontbreekt een werkelijke kost in het resultaat — matching-principe wordt geschonden.

**📥 Input**:
- Verbruiksgegevens → **Energie, water, telefonie, niet-gefactureerde diensten** _(document)_

**📤 Output**:
- Boeking toe te rekenen kost → **Kost + tegenpost 492** _(boekingsregel)_

**🛠️ Hoe**:

1. Identificeer verbruiken zonder factuur op balansdatum (vaak energie, telecom, einde-jaars-diensten).
2. Schat bedrag op basis van vorige facturen of contractuele tarieven.
3. Boek: Debet 6X-kost; Credit 492 Toe te rekenen kosten.
4. Bij Rotex Roeselare NV — gas-verbruik dec geschat € 4.500: D 6101 Verwarming € 4.500; C 492 € 4.500.
5. Wanneer factuur arriveert in januari: D 4400 Leverancier; C 492 (terugname); btw boeken op 411.


**Grondslag**: [[overlopende-rekeningen]] §toe-te-rekenen-kosten, [[bedrijfsresultaat]] §matching

### 5. Documenteer in toelichting en behoud audit trail

Vermeld materiële overlopende posten in de toelichting bij de jaarrekening + bewaar de berekeningswerkbladen.

**Waarom?** De gebruiker van de jaarrekening moet kunnen zien welke periode-correcties zijn gemaakt en op welke schattingen ze berusten.

**📥 Input**:
- Boekingsoverzicht overlopende posten → **Per post bedrag + grondslag** _(balans)_

**📤 Output**:
- Toelichting jaarrekening + werkdossier → **Specificatie 490/491/492/493** _(document)_

**🛠️ Hoe**:

1. Detailleer materiële overlopende bedragen in toelichting onder rubriek "Overlopende rekeningen".
2. Voor 492 toe te rekenen kosten: specificeer aard (lonen, energie, interest, ...).
3. Bewaar werkblad met pro-rata-berekening en bron-facturen.
4. Bij audit-vraag: producibel binnen 24 uur.


**Grondslag**: [[overlopende-rekeningen]] §toelichting, KB-WVV art. 3:73


## Voorbeelden





