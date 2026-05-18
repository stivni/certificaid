---
title: Bedrijfsvorderingen
tags:
- concept
- begrip
- po-1-1
linked_anchors:
- 1.1.II.F
- 1.1.II.D
programmaonderdelen:
- '1.1'
confidence: grounded
node_type: begrip
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/bedrijfsvorderingen.json
gegenereerd_op: '2026-05-18'
---
# Bedrijfsvorderingen ⚖️

> [!summary] Korte inhoud
> **Vorderingen op derden** die voortkomen uit de gewone bedrijfsuitoefening (verkoop van goederen of diensten op krediet).

> [!info] Specialisatie van: [[voorzichtigheidsbeginsel]]

**Vorderingen op derden** die voortkomen uit de gewone bedrijfsuitoefening (verkoop van goederen of diensten op krediet). Hoofdzakelijk **handelsdebiteuren** (rekening 400) plus te innen bedragen wegens leveringen of dienstprestaties. Op de balans gegroepeerd onder rubriek VII (vlottende activa, vorderingen op ten hoogste één jaar) en rubriek V (vorderingen op meer dan één jaar). Waardering: **nominale waarde** verminderd met geboekte **waardeverminderingen** in geval van onzekerheid over geheel of gedeeltelijke inbaarheid (KB WVV art. 3:46).

_Bron: KB WVV art. 3:46_


## Bouwstenen

### Onderscheid op meer dan / hoogstens één jaar ⚖️

Vorderingen met een resterende looptijd langer dan één jaar staan op rubriek V (rekening 29 — vorderingen op meer dan één jaar). Vorderingen met resterende looptijd ≤ één jaar staan op rubriek VII (rekening 40 — handelsdebiteuren, 41 — overige vorderingen).

**Waarom?** De jaarrekening onderscheidt korte- en lange-termijn-posities zodat de gebruiker de liquiditeit kan inschatten. Het is de resterende termijn op balansdatum die telt, niet de oorspronkelijke termijn.



Uitgeverij Ukkel NV verleent een lening op 3 jaar aan een freelance-auteur voor € 25.000 (terugbetaling jaarlijks). Op 31/12/20X1: € 16.500 resterend, waarvan € 8.250 binnen het jaar (rubriek VII) en € 8.250 op meer dan één jaar (rubriek V).

_Grondslag: KB WVV art. 3:46 + MAR_

### Waardevermindering bij onzekere inbaarheid ⚖️

Wanneer er onzekerheid bestaat over de inbaarheid van een vordering (geheel of gedeeltelijk), wordt een waardevermindering geboekt op rekening 409 'Geboekte waardeverminderingen op handelsvorderingen'. De waardevermindering wordt geraamd op basis van de werkelijke situatie van de klant en de bestaande zekerheden.

**Waarom?** Het voorzichtigheidsbeginsel vereist dat verliezen al worden geboekt als ze waarschijnlijk zijn. Een dubieuze vordering volledig op nominale waarde laten staan zou de activa overschatten.



Klant X van Meubelzaak Mertens BV: vordering € 18.000, advocaat schat 70 % verlies. Waardevermindering = € 12.600 op rekening 409. Boeking: Debet 6340 Waardeverminderingen op handelsvorderingen € 12.600 / Credit 409 € 12.600. Netto op balans: € 18.000 − € 12.600 = € 5.400.

_Grondslag: KB WVV art. 3:46_

### Definitief verlies: definitief afboeken 🤖

Bij definitief verlies (faillissement met dividend 0, kwijtschelding) wordt de vordering definitief afgeboekt op rekening 642 'Niet-recurrente kosten op vlottende activa' of vergelijkbaar. De eerder geboekte waardevermindering wordt teruggenomen ter compensatie.

**Waarom?** Een waardevermindering is voorzichtigheidsmatig; een definitief verlies is een feit. Het feit moet zichtbaar zijn in resultaat, niet meer als correctierekening.



Klant X gaat failliet met 0% dividend. Vordering € 18.000 definitief verloren. Boekingen: (a) Terugname waardevermindering: Debet 409 € 12.600 / Credit 7340 Terugname waardeverminderingen € 12.600. (b) Definitieve afboeking: Debet 642 Minderwaarde op realisatie van handelsvorderingen € 18.000 / Credit 400 Handelsdebiteuren € 18.000.

_Grondslag: KB WVV art. 3:46 + MAR klasse 642_

### Verzekerde vorderingen — gedeeltelijke waardevermindering ⚖️

Voor handelsvorderingen die kredietverzekerd zijn (Coface, Atradius, etc.) wordt enkel het **niet-verzekerde gedeelte** voorwerp van waardevermindering. De verzekeringspolis dekt de rest.

**Waarom?** Anders zou dubbel rekening worden gehouden met het risico. Het ongedekte deel is het reële economische risico voor de onderneming.



Naaiatelier Ninove BV heeft kredietverzekering 80 % op een vordering van € 50.000. Klant betaalt niet. Verzekerd: 80 % × € 50.000 = € 40.000. Waardevermindering te boeken: 100 % × € 10.000 (ongedekt deel) = € 10.000.

_Grondslag: CBN praktijk waardeverminderingen op verzekerde handelsvorderingen_


## In de praktijk

<h3 id="hulpklantenrekening-analytische-opvolging">Hulpklantenrekening + analytische opvolging</h3>

> [!tip]- Hulpklantenrekening + analytische opvolging
> Per individuele klant wordt een hulpklantenrekening bijgehouden (de zogenoemde 'klantenfiche'). Het globaal-totaal van alle hulpklantenrekeningen moet gelijk zijn aan rekening 400 in de algemene boekhouding. Dit maakt aanmaning en inbaarheid-beoordeling per klant mogelijk. 🤖

> [!tip]- Herkennen op het examen
> Examen: 'rekening 400 Handelsdebiteuren € 145.000' — dit is een totaalsaldo dat opgebouwd is uit individuele klantenfiches met elk hun eigen ouderdomsanalyse.

<h3 id="ouderdomsbalans-als-basis-voor-waardevermindering">Ouderdomsbalans als basis voor waardevermindering</h3>

> [!tip]- Ouderdomsbalans als basis voor waardevermindering
> Bij afsluiting analyseert de boekhouder de openstaande vorderingen per ouderdomsbucket (< 30 d, 30-60 d, 60-90 d, > 90 d). Hoe ouder de vordering, hoe hoger het inbaarheidsrisico. Vaak gebruikt: vermoedelijke waardevermindering-percentages per bucket. 🤖


> [!info]- Niet verwarren met [[vorderingen-op-meer-dan-een-jaar]]
> Beide zijn bedrijfsvorderingen, MAAR rubriek V (op meer dan één jaar) staat boven rubriek VII (op hoogstens één jaar) in de balans. De grens is de RESTERENDE looptijd op balansdatum, niet de oorspronkelijke.
>
> _Trigger_: Examen: 'lening 3 jaar verleend in jaar 1, op 31/12/20X2 nog 18 maanden te lopen' → splitsen: 12 maanden op rubriek VII, 6 maanden op rubriek V.


## Valkuilen

> [!warning]- Waardevermindering ≠ definitieve afboeking
> ⚠️ Waardevermindering ≠ definitieve afboeking. Waardevermindering = correctie zolang inbaarheid onzeker is (kan teruggenomen worden). Definitieve afboeking = wegnemen van de vordering bij feitelijk verlies (faillissement, kwijtschelding). ⚖️
>
> _Bron: KB WVV art. 3:46_



## Zie ook

- **Vereist kennis van**: [[waardeverminderingen]]

## Voorbeelden

Meubelzaak Mertens BV verkoopt voor € 8.500 + BTW € 1.785 = € 10.285 op factuur aan klant X (30 dagen krediet). Boeking: Debet 400 Handelsdebiteuren € 10.285 / Credit 700 Verkopen € 8.500 + Credit 451 BTW € 1.785. Bij niet-betaling na 6 maanden + aanmaningen: waardevermindering op rekening 409 voor 70 % = € 7.200.

## Bronnen

[^1]: `KB-WVV-2019__art_3_46`
