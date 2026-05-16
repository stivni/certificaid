---
title: Step acquisition (trapsgewijze verwerving)
tags:
- concept
- fenomeen
- po-1-4
linked_anchors:
- 1.4.I.G
- 1.4.II.D
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: grounded
node_type: fenomeen
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/step-acquisition.json
gegenereerd_op: '2026-05-16'
---
# Step acquisition (trapsgewijze verwerving) ⚖️

> [!summary] Korte inhoud
> Het fenomeen waarbij een onderneming haar belang in een andere onderneming in twee of meer fasen verhoogt — met als gevolg dat (a) een eerste deelneming met invloed van betekenis ontstaat of (b) een bestaande geassocieerde wordt opgeschaald, al dan niet tot dochter.

> [!info] Specialisatie van: [[wijziging-consolidatiekring]]
Het fenomeen waarbij een onderneming haar belang in een andere onderneming in twee of meer fasen verhoogt — met als gevolg dat (a) een eerste deelneming met invloed van betekenis ontstaat of (b) een bestaande geassocieerde wordt opgeschaald, al dan niet tot dochter. Bij elke trap controleer je of de kwalificatie verandert (geen invloed → invloed van betekenis → controle). Verandert ze, dan schakelt ook de consolidatietechniek (van geen consolidatie naar vermogensmutatie, of van vermogensmutatie naar integrale of evenredige consolidatie).

_Bron: CBN 2013/3 — De boekhoudkundige verwerking van step acquisitions (update)_


## Bouwstenen

### Variant 1 — geassocieerde blijft geassocieerd ⚖️

Je verhoogt het belang in een geassocieerde maar blijft onder de controlegrens — de geassocieerde blijft geassocieerd. De bijkomende aankoop verhoog je gewoon de post 'Vennootschappen waarop vermogensmutatie is toegepast' en bereken je eventueel een extra consolidatieverschil op het bijkomend belang.

**Waarom?** Geen kwalificatieverandering = geen wisseling van techniek. De vermogensmutatie blijft de juiste methode; alleen het bedrag en het residu groeien mee.

**Voorbeeld**: Antwerpse Investments NV bezit 25 % in Drukkerij Dendermonde BV (vermogensmutatie) en koopt 5 % bij voor € 75.000 → nu 30 %, nog steeds geassocieerd → 'Vennootschappen waarop vermogensmutatie is toegepast' wordt verhoogd met het pro-rata bedrag + eventueel consolidatieverschil op de bijkomende 5 %.

_Grondslag: CBN 2013/3_

### Variant 2 — geassocieerde wordt dochter ⚖️

Je verhoogt het belang en overschrijdt de controlegrens — de geassocieerde wordt dochter. De vermogensmutatie eindigt; vanaf nu pas je integrale consolidatie toe. Voor het bijkomende belang bereken je een nieuw consolidatieverschil op de datum waarop controle is verworven; activa en schulden van de nieuwe dochter komen voor 100 % in de geconsolideerde balans (met derden-aandeel apart).

**Waarom?** Een wisseling van consolidatietechniek wijst op een fundamenteel andere economische werkelijkheid: van 'meepraten over beleid' naar 'beleid bepalen'. De jaarrekening moet die overgang weergeven.

**Voorbeeld**: Antwerpse bezit 25 % in Drukkerij Dendermonde (vermogensmutatie). In 20X3 koopt Antwerpse 35 % bij voor € 700.000 → totaal 60 % → exclusieve controle → integrale consolidatie. Voor de bijkomende 35 % wordt een nieuw consolidatieverschil berekend op datum 20X3.

_Grondslag: CBN 2013/3_

### Variant 3 — niet-geassocieerde wordt geassocieerd ⚖️

Eerste verwerving van een belang dat invloed van betekenis triggert (typisch ≥ 20 %). Eerste consolidatie via vermogensmutatie: je berekent het consolidatieverschil zoals bij elke eerste consolidatie (aanschaffingswaarde − pro-rata aandeel in EV; toerekenen aan stille meer-/minderwaarden; residu boeken).

**Waarom?** Bij het kantelmoment 'geen invloed → invloed van betekenis' begin je effectief met consolideren — er moet dus een eerste consolidatieverschil worden vastgesteld, op basis van de aanschaffingsdatum van de eerste tranche.

**Voorbeeld**: Antwerpse Investments NV verwerft in 20X1 een eerste tranche van 25 % in Drukkerij Dendermonde BV voor € 350.000; eigen vermogen (EV) Drukkerij op aankoopdatum = € 1.250.000 → pro-rata = € 312.500; consolidatieverschil = € 350.000 − € 312.500 = € 37.500, te boeken bij eerste consolidatie via vermogensmutatie.

_Grondslag: CBN 2013/3_


## In de praktijk

<h3 id="kantelpunten-detecteren">Kantelpunten detecteren</h3>

> [!tip]- Kantelpunten detecteren
> Bij elke trap controleer je éérst of de kwalificatie verandert. De drie typische kantelpunten staan gestructureerd in het top-level veld `kantelpunten[]` (van_situatie → naar_situatie + drempel + gevolg + grondslag). Bij elk kantelpunt schakelt mogelijk de consolidatietechniek. ⚖️
>
> > [!tip]- Herkennen op het examen
> > Examen-zin 'Antwerpse Investments NV koopt eerst 25 %, daarna 35 % bij': twee opeenvolgende kwalificaties — eerst vermogensmutatie (25 %), daarna integrale consolidatie (totaal 60 %). Het is geen één continue boekhoudkundige rekening, maar twee afzonderlijke regimes.


## Valkuilen

> [!warning]- Bij de overgang van vermogensmutatie naar integrale consolidatie verdwijnt het …
> ⚠️ Bij de overgang van vermogensmutatie naar integrale consolidatie verdwijnt het bestaande consolidatieverschil niet. Voor de bijkomende tranche bereken je een nieuw consolidatieverschil op de aanschaffingsdatum van die nieuwe tranche; het oude residu blijft bestaan voor de eerdere tranche. ⚖️
>
> _Bron: CBN 2013/3_


## Zie ook

- **Getriggerd door**: [[eerste-consolidatie]]
- **Vereist kennis van**: [[consolidatieverschil]]

## Bronnen

[^1]: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_inleiding`
[^2]: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking`
[^3]: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_voorbeeld-1`
