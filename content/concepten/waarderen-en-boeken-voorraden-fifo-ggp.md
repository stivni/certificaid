---
title: Waarderen en boeken van voorraden volgens FIFO of gewogen gemiddelde
tags:
- concept
- competentie
- po-1-1
linked_anchors:
- 1.1.taak.1
- 1.1.II.E
programmaonderdelen:
- '1.1'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/waarderen-en-boeken-voorraden-fifo-ggp.json
gegenereerd_op: '2026-05-18'
---
# Waarderen en boeken van voorraden volgens FIFO of gewogen gemiddelde 🤖


## Stappen

### 1. Bepaal de aanschaffingswaarde per voorraadbeweging

Bereken voor elke inkomende voorraad de aanschaffingswaarde incl. bijkomende kosten.

**Waarom?** Een correcte ingangsprijs is voorwaarde voor zinvolle waardering — FIFO of GGP gebruiken beide deze ingangsprijs als basis.

**📥 Input**:
- Aankoopfacturen + transportfacturen + douanedocumenten → **Aankoopprijs, transport, invoerrechten, niet-aftrekbare btw** _(document)_

**📤 Output**:
- Voorraadkaart inkomend → **Datum, aantal, eenheidsprijs incl. bijkomende kosten** _(berekening)_

**🛠️ Hoe**:

1. Som per inkomende lading volgens [[aanschaffingswaarde]] §componenten: factuurprijs + transport + douane + niet-aftrekbare btw.
2. Trek af: kortingen, kortingen voor contante betaling indien benut.
3. Voor Naaiatelier Ninove BV — januari 1.000 m textielgaren € 4,20/m + transport € 200 (verdeeld over 1.000 m = € 0,20/m) → eenheidsprijs € 4,40/m.
4. Documenteer in voorraadkaart per artikel — basis voor FIFO of GGP-berekening.


**Grondslag**: [[aanschaffingswaarde]] §componenten, [[voorraden]] §ingangsprijs

### 2. Kies en motiveer waarderingsmethode (FIFO of GGP)

Bepaal welke voorraadwaarderingsmethode best aansluit bij de aard van de voorraad en leg ze vast in de waarderingsregels.

**Waarom?** Methode moet aansluiten bij de werkelijke voorraadrotatie en bestendig worden toegepast — wijziging vraagt motivering in toelichting.

**📥 Input**:
- Activiteitenbeschrijving + voorraadrotatie → **Aard goederen, rotatiesnelheid, verwerkingsproces** _(document)_

**📤 Output**:
- Waarderingsregel-vermelding → **Gekozen methode + motivering** _(conclusie)_

**🛠️ Hoe**:

1. FIFO (First In First Out) — geschikt voor voorraden met vervaldatum of fysieke rotatie volgens binnenkomst (bv. handelsgoederen, voedsel).
2. Gewogen gemiddelde prijs (GGP) — geschikt voor homogene voorraden die niet apart traceerbaar zijn (bv. grondstoffen, bulk).
3. LIFO is sinds KB van 26/06/2018 NIET MEER toegelaten voor de jaarrekening (wel nog fiscaal beperkt).
4. Individuele identificatie — verplicht voor unieke goederen (bv. tweedehandswagens, kunstwerken).
5. Voor Naaiatelier Ninove BV — grondstoffen-textielgaren is homogeen → GGP.
6. Voor Meubelzaak Mertens BV — handelsgoederen-meubelen met verschillende referenties → FIFO of individueel.
7. Leg keuze vast in waarderingsregels (KB-WVV art. 3:6).


**Grondslag**: [[voorraden]] §waarderingsmethoden, KB-WVV art. 3:15

### 3. Hou de voorraadkaart bij gedurende het boekjaar

Registreer per artikel alle inkomende en uitgaande bewegingen volgens de gekozen methode.

**Waarom?** De voorraadkaart is het werkdocument waarmee balansdatum-waardering en kost van verkochte goederen worden berekend.

**📥 Input**:
- Voorraadkaart-template → **Datum, aantal in/uit, eenheidsprijs, saldo** _(berekening)_

**📤 Output**:
- Bijgewerkte voorraadkaart → **Multi-period overzicht per artikel** _(balans)_

**🛠️ Hoe**:

1. Bij FIFO: registreer elke uitgaande beweging tegen de oudste resterende ingangsprijs.
2. Bij GGP: bereken bij elke inkomende beweging een nieuwe gewogen gemiddelde prijs = (saldo × oude GGP + nieuwe × ingangsprijs) / (saldo + nieuwe).
3. Uitgaande bewegingen waardeer je tegen de actuele GGP.
4. Op balansdatum: eindvoorraad × FIFO-prijs (= prijs van de meest recente in) of × GGP.


> [!example]- Voorbeeld: Naaiatelier Ninove BV — textielgaren 2026, methode GGP
> Naaiatelier Ninove BV — textielgaren 2026, methode GGP. Beginvoorraad 01/01: 500 m × € 4,30 = € 2.150. Bewegingen: 15/01 in 1.000 m × € 4,40 = € 4.400. 20/02 uit 800 m. 10/03 in 600 m × € 4,50 = € 2.700. Eindvoorraad op 31/03 = ?
>
> 1. **Voorraadkaart GGP** 🧮
>
>    | Datum | Beweging | Aantal | Eenheidsprijs | Bedrag | Saldo aantal | Saldo GGP | Saldo bedrag |
>    |---|---|---|---|---|---|---|---|
>    | 01/01 | Begin | 500 | € 4,30 | € 2.150 | 500 | € 4,30 | € 2.150 |
>    | 15/01 | In | 1.000 | € 4,40 | € 4.400 | 1.500 | € 4,367 | € 6.550 |
>    | 20/02 | Uit | -800 | € 4,367 | € -3.494 | 700 | € 4,367 | € 3.056 |
>    | 10/03 | In | 600 | € 4,50 | € 2.700 | 1.300 | € 4,428 | € 5.756 |
>    
>
> 2. **Berekening nieuwe GGP na 15/01** 🧮
>
>    GGP = (500 × € 4,30 + 1.000 × € 4,40) / 1.500 = (€ 2.150 + € 4.400) / 1.500 = € 4,367
>    
>
> 3. **Berekening nieuwe GGP na 10/03** 🧮
>
>    GGP = (700 × € 4,367 + 600 × € 4,50) / 1.300 = (€ 3.057 + € 2.700) / 1.300 = € 4,428
>    
>

**Grondslag**: [[voorraden]] §berekening-FIFO-GGP

### 4. Voer de voorraadboeking uit op balansdatum (inventarisaanpassing)

Boek het verschil tussen openings- en eindvoorraad op de resultatenrekening.

**Waarom?** De voorraadbeweging is een resultaat-element — een toename is een opbrengst (productie), een afname een kost (verkoop).

**📥 Input**:
- Voorraadkaart einde boekjaar → **Eindwaarde per rubriek (30, 31, 32, 33, 34)** _(balans)_

**📤 Output**:
- Voorraadboeking → **Aanpassing actief + tegenpost resultaat** _(boekingsregel)_

**🛠️ Hoe**:

1. Vergelijk eindvoorraad met beginvoorraad per rubriek (handelsgoederen 34, grondstoffen 30, eindproducten 33, ...).
2. Bij toename: Debet 3X Voorraad; Credit 609X Voorraadwijziging grondstoffen OF 71X Wijziging in voorraad gereed product.
3. Bij afname: omgekeerde boeking.
4. Voor Naaiatelier Ninove BV — textielgaren toename van € 2.150 naar € 5.756 = + € 3.606: Debet 30 Grondstoffen € 3.606; Credit 609 Voorraadwijziging € 3.606.
5. Boek waardeverminderingen apart volgens [[waardeverminderingen]] §boeking-voorraden.


**Grondslag**: [[voorraden]] §inventarisboeking, KB-WVV art. 3:15

### 5. Toets aan lower-of-cost-or-market regel

Vergelijk de FIFO/GGP-waarde met de marktwaarde en boek waardevermindering indien lager.

**Waarom?** Voorzichtigheidsbeginsel dwingt voorraad NIET hoger te waarderen dan de te realiseren prijs.

**📥 Input**:
- Voorraadkaart einde + marktinformatie → **FIFO/GGP-waarde vs. verkoopprijs - verkoopkosten** _(berekening)_

**📤 Output**:
- Waardevermindering-boeking (indien nodig) → **Dotatie + correctief 30X9** _(boekingsregel)_

**🛠️ Hoe**:

1. Bereken netto-realisatiewaarde = verwachte verkoopprijs - verkoopkosten - verdere verwerkingskosten.
2. Vergelijk met FIFO/GGP-waarde.
3. Indien marktwaarde < FIFO/GGP: boek waardevermindering — zie [[waardeverminderingen]] §boeking-voorraden.
4. Bij Naaiatelier Ninove BV — voorraad textielgaren op 31/03/2026 GGP € 5.756, marktwaarde € 6.500 → geen waardevermindering nodig (FIFO/GGP-waarde is reeds lager dan markt).


**Grondslag**: [[voorraden]] §lower-of-cost-or-market, [[waardeverminderingen]] §boeking-voorraden


## Voorbeelden





