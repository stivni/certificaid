---
title: Boeken van waardeverminderingen op vorderingen en voorraden
tags:
- competentie
- po-1-1
programmaonderdelen:
- '1.1'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/boeken-waardeverminderingen-op-vorderingen-en-voorraden.yaml
gegenereerd_op: '2026-05-17'
---
# Boeken van waardeverminderingen op vorderingen en voorraden

**⚖️ 70% · 🤖 30%**

> De boekingsregels (rubrieken 407/409 dubieuze klanten en 30X9 waardevermindering voorraden) zijn voorgeschreven in KB-WVV en KB-MAR; het voorzichtigheidsbeginsel verplicht boeking. Praktijk komt kijken bij de inschatting van het verlies-percentage en het criterium "dubieus" (al dan niet meer dan 6 maanden achterstand).

## Aanbevolen werkwijze

### 1. Identificeer dubieuze vorderingen

Stel een lijst op van klanten waarvan inning onzeker is op balansdatum.

**Waarom?** Niet elke openstaande vordering is dubieus; alleen wanneer inning onzeker is, moet waardevermindering geboekt worden.

**📥 Input**:
- Klantenbalans + ouderdomsanalyse → **Openstaand bedrag per klant + ouderdom** _(berekening)_

**📤 Output**:
- Lijst dubieuze klanten → **Klant + bedrag + reden onzekerheid** _(conclusie)_

**🛠️ Hoe**:

1. Maak een ouderdomsanalyse van de klantenrekening (4000) per balansdatum.
2. Identificeer klanten met betalingsachterstand > 6 maanden, klanten in WCO/faillissement, klanten waarvan dagvaarding loopt.
3. Bij Meubelzaak Mertens BV — klant Wegener heeft € 8.500 sinds maart openstaan; geen reactie op aanmaningen; geen formele dagvaarding maar bestuurder schat 50% kans op verlies.
4. Klanten in faillissement: boek volledig dubieus (100% waardevermindering tot eventueel uitkering).
5. Documenteer in werkdocument met datum aanmaningen + reactie klant.


**Grondslag**: [[bedrijfsvorderingen]] §dubieus-criterium, [[voorzichtigheidsbeginsel]] §risico-detectie

### 2. Verschuif dubieuze klanten van 4000 naar 407

Boek een tussenboeking die de dubieuze vordering uit de gewone klantenrekening verwijdert.

**Waarom?** Aparte rubriek 407 maakt zichtbaar dat het niet langer een gewone vordering is en respecteert de informatieplicht in de toelichting.

**📥 Input**:
- Lijst dubieuze klanten stap 1 → **Bedragen per klant** _(berekening)_

**📤 Output**:
- Journaalpost verschuiving → **Boeking 407 ← 4000 incl. btw** _(boekingsregel)_

**🛠️ Hoe**:

1. Boek inclusief btw — de hele vordering verschuift, niet alleen het netto bedrag.
2. Debet 407 Dubieuze handelsvorderingen [bedrag incl. btw]; Credit 4000 Handelsvorderingen [bedrag incl. btw].
3. Bij Meubelzaak Mertens BV — Wegener € 8.500 incl. btw: D 407 € 8.500; C 4000 € 8.500.
4. Geen waardevermindering nog — die volgt in stap 3.


**Grondslag**: [[bedrijfsvorderingen]] §verschuiving-dubieus

### 3. Boek de waardevermindering op het netto-bedrag (excl. btw)

Boek het waarschijnlijke verlies op het netto bedrag, zonder btw, omdat btw bij definitief verlies later teruggevorderd wordt.

**Waarom?** Voorzichtigheidsbeginsel verplicht boeking van waarschijnlijk verlies; btw wordt apart via btw-aangifte teruggevorderd bij definitief verlies (KB nr. 4 art. 3).

**📥 Input**:
- Journaalpost stap 2 → **Verplaatste bedragen op 407** _(balans)_

**📤 Output**:
- Waardevermindering-boeking → **Dotatie + waardeverminderingsrekening** _(boekingsregel)_

**🛠️ Hoe**:

1. Bereken het waarschijnlijke verlies — vaak een percentage (50%, 75% of 100% afhankelijk van situatie).
2. Werk op het netto bedrag (excl. btw) — bij € 8.500 incl. btw 21% = € 7.024,79 excl. btw.
3. Voor Mertens BV — Wegener 50% verlies × € 7.024,79 = € 3.512,40.
4. Boek: Debet 6340 Waardeverminderingen op handelsvorderingen (dotatie); Credit 4079 Waardeverminderingen op dubieuze klanten (correctief actiefrekening).
5. Op balansdatum: rubriek 407 staat voor brutowaarde € 8.500; rubriek 4079 voor € 3.512; netto € 4.987.


> [!example]- Voorbeeld: Meubelzaak Mertens BV — klant Wegener € 8.500 incl. btw 21%, 8 maanden achterstand, geschat 50% verlies
> Meubelzaak Mertens BV — klant Wegener € 8.500 incl. btw 21%, 8 maanden achterstand, geschat 50% verlies.
>
> 1. **Verschuiving naar dubieus** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 31/12/2026 | 407 Dubieuze handelsvorderingen — Wegener | herklassering | € 8.500,00 | |
>    | 31/12/2026 | 4000 Handelsvorderingen — Wegener | -- | | € 8.500,00 |
>    
>
> 2. **Boeking waardevermindering** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 31/12/2026 | 6340 Waardeverm. op handelsvord. — dotatie | 50% × € 7.024,79 | € 3.512,40 | |
>    | 31/12/2026 | 4079 Waardeverm. op dubieuze klanten | correctief actief | | € 3.512,40 |
>    
>

**Grondslag**: [[waardeverminderingen]] §boeking-vorderingen, [[voorzichtigheidsbeginsel]] §waarschijnlijke-verliezen

> [!warning]- Boek waardevermindering op het netto bedrag excl. btw — de btw kan apart teruggevorderd worden bij definitief verlies.
>
> _Vaak fout gedaan_: De waardevermindering boeken op het totaal incl. btw en zo dubbel verlies registreren.
>
> _Grondslag_: [[bedrijfsvorderingen]] §btw-bij-verlies, KB nr. 4 art. 3

### 4. Boek waardevermindering op voorraden bij ondergewaardeerde of incourante voorraad

Indien de marktwaarde of realisatiewaarde van voorraad onder de aanschaffingswaarde valt, boek het verschil als waardevermindering.

**Waarom?** Voorraadwaardering volgt de regel "laagste van aanschaffingswaarde of marktwaarde" (Lower of Cost or Market) — zonder waardevermindering wordt voorraad overgewaardeerd.

**📥 Input**:
- Voorraadwaarderingsstaat → **Per artikel: aantal, aanschaffingswaarde, marktwaarde** _(berekening)_

**📤 Output**:
- Waardevermindering-boeking → **Dotatie + correctief actiefrekening 30X9** _(boekingsregel)_

**🛠️ Hoe**:

1. Bereken per artikel: marktwaarde minus aanschaffingswaarde (kan negatief zijn).
2. Indien negatief: boek waardevermindering ter grootte van het verschil — zie [[voorraden]] §waardering.
3. Voor Naaiatelier Ninove BV — voorraad oude collectie 2024 nog € 12.000 aanschaffingswaarde, marktwaarde tweedehandsmarkt € 7.000: waardevermindering € 5.000.
4. Boek: Debet 6310 Waardeverminderingen op voorraden (dotatie); Credit 30X9 Geboekte waardeverminderingen op voorraden (correctief op rubriek 30 grondstoffen, 31 hulpstoffen, 32 goederen in bewerking, 33 gereed product of 34 handelsgoederen).
5. Bij incourant artikel zonder marktwaarde: 100% afwaarderen.


> [!example]- Voorbeeld: Naaiatelier Ninove BV — voorraad oude collectie 2024: aanschaffingswaarde € 12.000, geschatte netto-realisatiewaarde € 7…
> Naaiatelier Ninove BV — voorraad oude collectie 2024: aanschaffingswaarde € 12.000, geschatte netto-realisatiewaarde € 7.000 op balansdatum 31/12/2026.
>
> 1. **Boeking waardevermindering voorraad** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 31/12/2026 | 6310 Waardeverm. op voorraden — dotatie | oude collectie 2024 | € 5.000,00 | |
>    | 31/12/2026 | 3409 Geboekte waardeverm. op handelsgoederen | -- | | € 5.000,00 |
>    
>

**Grondslag**: [[voorraden]] §waardering-lower-of-cost-or-market, [[waardeverminderingen]] §boeking-voorraden, KB-WVV art. 3:15

### 5. Herzie of stop waardevermindering wanneer reden wegvalt

Indien klant alsnog betaalt of voorraad terug in waarde stijgt, terugnemen of bij definitief verlies definitief boeken.

**Waarom?** Waardevermindering is geen blijvende boeking; voortdurende herevaluatie verplicht (CBN 2010/15).

**📥 Input**:
- Latere informatie → **Betaling, faillissement, voorraadherwaardering** _(document)_

**📤 Output**:
- Terugname of definitieve boeking → **7600 Terugname waardeverm. of 642 Minderwaarde** _(boekingsregel)_

**🛠️ Hoe**:

1. Bij alsnog betaling: terugname via Debet 4079; Credit 7600 Terugneming van waardeverminderingen op handelsvorderingen.
2. Bij definitief verlies (vonnis, faillissement-afsluiting): boek volledig verlies via 6420 Minderwaarden op realisatie van handelsvorderingen + btw-terugvordering via 411.
3. Voor voorraden: indien marktwaarde stijgt boven aanschaffingswaarde — waardevermindering terugnemen (maar boekwaarde NOOIT boven historische kost).
4. Documenteer beslissing in cliëntdossier.


**Grondslag**: [[waardeverminderingen]] §terugname, CBN 2010/15


## Voorbeelden

> [!example]- Meubelzaak Mertens BV heeft op 31/12/2026 vordering € 8.500 incl. btw 21% op klant Wegener (8 maanden onbetaald, geen da…
> **Conclusie**: Wegener — verschuiving naar 407 (€ 8.500), waardevermindering 50% op netto € 7.024,79 = € 3.512,40 op 4079 + dotatie 6340. Lievegem — verschuiving naar 407 (€ 3.025), waardevermindering 100% op netto € 2.500 = € 2.500 op 4079 + dotatie 6340. Btw terugvordering pas bij afsluiting curatele.
>
> **Grondslag**: [[bedrijfsvorderingen]] §dubieus; [[waardeverminderingen]] §percentage
>
> **Redenering**: 8 maanden zonder reactie rechtvaardigt 50%-inschatting (matig risico). Faillissement rechtvaardigt 100%, maar btw blijft afhankelijk van curator-rapport.

> [!example]- Naaiatelier Ninove BV — voorraad oude textielcollectie 2024 staat op 31/12/2026 nog op € 12.000 aanschaffingswaarde, net…
> **Conclusie**: Waardevermindering € 5.000 op 3409 Correctief op handelsgoederen, dotatie via 6310. Voorraad blijft op rubriek 34 voor € 12.000 bruto; netto presentatie € 7.000 na correctief.
>
> **Grondslag**: [[voorraden]] §lower-of-cost-or-market
>
> **Redenering**: Voorzichtigheidsbeginsel vraagt afwaardering tot netto-realisatiewaarde wanneer markt onder historische kost zakt; voorraad mag niet bovenwaarde getoond worden.

> [!example]- In juni 2027 betaalt Wegener alsnog € 6.000 (zonder rechtszaak)
> **Conclusie**: Boek inkomst Debet 5500 Bank € 6.000; Credit 407 Dubieuze handelsvorderingen — Wegener € 6.000. Resterend saldo 407 = € 2.500. Terugname waardevermindering ter grootte van het deel dat geïnd is — Debet 4079 € 3.512,40 — Credit 7600 Terugneming € 3.512,40. Resterend 407 € 2.500 verder opvolgen.
>
> **Grondslag**: [[waardeverminderingen]] §terugname; [[bedrijfsvorderingen]] §gedeeltelijke-inning
>
> **Redenering**: Inning vermindert de dubieuze vordering en doet de geboekte waardevermindering volledig terugnemen — eerder pessimisme corrigeren.


## Gebaseerd op concepten

[[waardeverminderingen]] · [[voorzichtigheidsbeginsel]] · [[bedrijfsvorderingen]] · [[voorraden]]
## Voortkomend uit

- **Taken**: 1.1.taak.1
- **Kenniselementen**: 1.1.II.D, 1.1.II.E, 1.1.II.F
