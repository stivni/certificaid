---
title: Kwalificeren en boeken van leasing (operationeel vs financieel)
tags:
- concept
- competentie
- po-1-1
linked_anchors:
- 1.1.taak.1
- 1.1.II.W
programmaonderdelen:
- '1.1'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/kwalificeren-en-boeken-leasing.json
gegenereerd_op: '2026-05-18'
---
# Kwalificeren en boeken van leasing (operationeel vs financieel) 🤖


## Stappen

### 1. Lees het leasingcontract en identificeer kerngegevens

Verzamel de cruciale parameters: contractduur, totale leasingbetalingen, optieprijs, onderhoudsverantwoordelijkheid, restwaarde.

**Waarom?** De kwalificatie hangt af van een aantal contractuele indicatoren — zonder volledig contract kan geen correcte boekhoudkundige verwerking gebeuren.

**📥 Input**:
- Leasingcontract → **Leasinggever, leasingnemer, looptijd, periodiek bedrag, optie, restwaarde, onderhoudsclausule** _(document)_

**📤 Output**:
- Werknotitie kerngegevens → **Tabel met parameters** _(conclusie)_

**🛠️ Hoe**:

1. Lees het contract volledig. Voor Transport Tongeren BV — vrachtwagen MAN, contract met leasinggever Bestleasing NV.
2. Noteer: aanvangsdatum 01/04/2026, looptijd 60 maanden, periodiek bedrag € 1.450/maand excl. btw, koopoptie aan einde € 5.000, totale leasingbetalingen € 87.000.
3. Catalogusprijs (referentie aanschaffingswaarde) € 95.000.
4. Onderhoud + verzekering: ten laste van leasingnemer.
5. Eigendomsoverdracht: niet automatisch; optie tegen € 5.000 (5,3% catalogusprijs).


**Grondslag**: [[leasing]] §contractanalyse, CBN 2015/04

### 2. Toets de kwalificatie-criteria (financieel of operationeel)

Bepaal of het contract overdracht van risico's en voordelen impliceert — dan financiële leasing — of niet — dan operationele leasing.

**Waarom?** Financiële leasing wordt geactiveerd + schuld op balans; operationele leasing blijft buiten balans als huurkost. Het verschil bepaalt het hele beeld van de balans.

**📥 Input**:
- Werknotitie stap 1 → **Parameters contract** _(berekening)_

**📤 Output**:
- Kwalificatie-conclusie → **Financieel of operationeel + grondslag** _(conclusie)_

**🛠️ Hoe**:

1. Toets aan de KB-WVV art. 3:46-criteria voor financiële leasing — zie [[leasing]] §kwalificatie:
   a. Looptijd ≥ bulk van de economische gebruiksduur.
   b. Som van leasingbetalingen ≥ kapitaal-component (= catalogusprijs minus restwaarde).
   c. Koopoptie tegen prijs lager dan vermoedelijke marktwaarde op einde contract.
   d. Activum is dermate specifiek dat enkel de leasingnemer het zinvol kan gebruiken.
2. Volstaat één criterium → financiële leasing.
3. Voor Transport Tongeren BV: contractduur 5 jaar ≈ economische levensduur van vrachtwagen; som leasingbetalingen € 87.000 + optie € 5.000 = € 92.000 ≈ catalogusprijs € 95.000. → Financiële leasing.
4. Operationeel: bv. kortlopende huur van kantoorruimte (3 jaar) waar verhuurder onderhoud verzorgt — risico/voordeel bij verhuurder.


**Grondslag**: [[leasing]] §kwalificatie-criteria, KB-WVV art. 3:46

> [!warning]- Kijk niet alleen naar contractbenaming — een "huurcontract" kan boekhoudkundig financiële leasing zijn als de criteria vervuld zijn.
>
> _Vaak fout gedaan_: Vertrouwen op de woorden 'huur' of 'leasing' op het contract zonder de KB-WVV-criteria toe te passen.
>
> _Grondslag_: [[leasing]] §substance-over-form

### 3. Boek bij financiële leasing: activering + schuld bij aanvang

Activeer het gehuurde goed onder rubriek 25 en boek de uitstaande schuld onder 172/422.

**Waarom?** Substance-over-form — economisch is leasingnemer eigenaar zoals bij koop; balans moet dit weergeven.

**📥 Input**:
- Kwalificatie financieel stap 2 → **Bedragen** _(berekening)_

**📤 Output**:
- Aanvangsboeking + afschrijvingsplan + schuldenschema → **Activering + schuld + interest-schema** _(boekingsregel)_

**🛠️ Hoe**:

1. Bereken de kapitaal-component = som leasingbetalingen + optie - interestcomponent. Bij Transport Tongeren BV: totaal € 92.000; kapitaal-component (catalogusprijs) € 95.000 ≈ activeringsbasis. Interestcomponent = som termijnen - kapitaal-component ≈ € 5.000 over 5 jaar (interest spreiding).
2. Boek bij aanvang: Debet 25 Vaste activa in leasing — voertuig € 95.000; Credit 172 Schulden uit leasing langlopend € 75.000; Credit 422 Schulden uit leasing kortlopend (deel < 1 jaar) € 20.000.
3. Stel afschrijvingsplan op zoals voor een gekocht voertuig — zie competentie [[opstellen-afschrijvingsplan-vaste-activa]].
4. Periodieke termijn splitsen in interest (kost 650) + kapitaalaflossing (vermindering 172/422).
5. Op einde contract bij uitoefening optie: Debet 24 Materiële vaste activa — eigen + Credit 25 Vaste activa in leasing.


> [!example]- Voorbeeld: Transport Tongeren BV — leasing vrachtwagen 01/04/2026, 5 jaar, € 1.450/maand, optie € 5.000
> Transport Tongeren BV — leasing vrachtwagen 01/04/2026, 5 jaar, € 1.450/maand, optie € 5.000. Kwalificatie: financieel. Activeringsbasis: € 95.000.
>
> 1. **Aanvangsboeking** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 01/04/2026 | 25 Vaste activa in leasing — voertuig | aanvang leasing MAN | € 95.000,00 | |
>    | 01/04/2026 | 172 Leasingschulden langlopend (> 1 jaar) | -- | | € 75.000,00 |
>    | 01/04/2026 | 422 Leasingschulden kortlopend (< 1 jaar) | -- | | € 20.000,00 |
>    
>
> 2. **Maandelijkse termijn — splitsing** 🧮
>
>    Termijn € 1.450 = ~ € 1.350 kapitaal + ~ € 100 interest (gemiddeld; werkelijk varieert volgens schuldsaldo).
>    
>
> 3. **Boeking maandtermijn** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 01/05/2026 | 422 Leasingschulden kortlopend | kapitaalaflossing | € 1.350,00 | |
>    | 01/05/2026 | 650 Kosten van schulden — interest leasing | interest | € 100,00 | |
>    | 01/05/2026 | 411 Aftrekbare btw 21% | btw op termijn | € 304,50 | |
>    | 01/05/2026 | 5500 Bank — KBC | betaling Bestleasing | | € 1.754,50 |
>    
>

**Grondslag**: [[leasing]] §boeking-financieel, KB-WVV art. 3:46-3:47

### 4. Boek bij operationele leasing: huurkost zonder activering

Boek elke leasingtermijn als huurkost op rubriek 610 — geen activering, geen schuldopname.

**Waarom?** Bij operationele leasing zijn risico's en voordelen bij verhuurder; balans van leasingnemer toont alleen de periodieke kost.

**📥 Input**:
- Kwalificatie operationeel stap 2 → **Contractgegevens** _(berekening)_

**📤 Output**:
- Maandelijkse boekingen + toelichting niet-in-balans → **Kost + btw + toelichting jaarrekening** _(boekingsregel)_

**🛠️ Hoe**:

1. Boek elke termijn: Debet 610 Huur en huurlasten; Debet 411 Aftrekbare btw; Credit 4400 Leverancier of 5500 Bank.
2. Geen actief, geen schuld op balans.
3. Wel toelichting verplicht in jaarrekening — totale toekomstige leasingverplichtingen vermelden onder "rechten en verplichtingen buiten balans" (zie [[rechten-verplichtingen-buiten-balans]] §huurverplichtingen).
4. Vermeld in toelichting de bedragen: < 1 jaar, 1-5 jaar, > 5 jaar.


**Grondslag**: [[leasing]] §boeking-operationeel, KB-WVV art. 3:80

### 5. Documenteer kwalificatie en boekingen

Bewaar het werkdocument met kwalificatie-analyse, leasingschema en afschrijvingstabel.

**Waarom?** Bij latere controle (commissaris, fiscale audit) moet de keuze tussen financieel en operationeel reproduceerbaar zijn.

**📥 Input**:
- Werknotitie + boekingen → **Volledig dossier** _(document)_

**📤 Output**:
- Leasingdossier → **Contract + kwalificatie + schema's** _(document)_

**🛠️ Hoe**:

1. Voeg toe: contract, KB-WVV-criteria-analyse, kapitaal/interest-schema, afschrijvingsplan.
2. Vermeld classificatie in waarderingsregels-toelichting.
3. Update jaarlijks de toelichting met openstaande bedragen.


**Grondslag**: [[leasing]] §dossierplicht, [[waarderingsregels-jaarrekening]] §vastlegging


