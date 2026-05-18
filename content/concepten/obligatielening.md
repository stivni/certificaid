---
title: Obligatielening
tags:
- concept
- cluster
- po-1-1
linked_anchors:
- 1.1.II.V
- 1.1.II.J
programmaonderdelen:
- '1.1'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/obligatielening.json
gegenereerd_op: '2026-05-18'
---
# Obligatielening ⚖️

> [!summary] Korte inhoud
> Een **leningsovereenkomst** waarbij de vennootschap **obligaties** uitgeeft aan beleggers — verhandelbare schuldbewijzen met een vaste of variabele rente en een vooraf bepaalde looptijd (typisch 5 — 15 jaar).

> [!info] Behoort tot: [[schulden]]

Een **leningsovereenkomst** waarbij de vennootschap **obligaties** uitgeeft aan beleggers — verhandelbare schuldbewijzen met een vaste of variabele rente en een vooraf bepaalde looptijd (typisch 5 — 15 jaar). De vennootschap ontvangt het kapitaal en betaalt jaarlijkse coupons (rente) plus terugbetaling op vervaldag. Boekhoudkundig: rekening **170 'Obligatieleningen'** onder schulden op meer dan één jaar. Bijhorende kosten van uitgifte: rekening 201 (oprichtingskosten).

_Bron: CBN 2019/07 — Boekhoudkundige verwerking van obligaties_


## Bouwstenen

### Drie hoofdelementen: nominaal, coupon, looptijd ⚖️

Bij uitgifte beslist de NV over: **nominaal bedrag** per obligatie (typisch € 1.000 of veelvoud), **couponrente** (vast of variabel, jaarlijks of zes-maandelijks), **looptijd** (5 — 30 jaar). Alle drie staan in het emissieprospectus.

**Waarom?** Deze parameters bepalen de cashflows en de financieringskost over de hele looptijd. Beleggers vergelijken ze met marktrente om de prijs te bepalen.


_Grondslag: WVV art. 7:54; CBN 2019/07_

### Uitgifte beneden of boven pari ⚖️

Obligaties kunnen worden uitgegeven aan een uitgifteprijs die afwijkt van het nominaal bedrag: (a) **beneden pari** = disagio (terugbetalingswaarde > ontvangen bedrag), (b) **boven pari** = premie. Het verschil wordt verspreid in de tijd als financiële kost/opbrengst.

**Waarom?** Marktrente vs couponrente verschillen vaak; uitgifteprijs corrigeert. Het verschil moet over de looptijd verspreid worden om matching te garanderen.


_Grondslag: CBN 2019/07_

### Coupons en prorata-intrest ⚖️

Couponbetalingen worden geboekt als financiële kosten op rekening 650. Tussen couponbetalingen en balansdatum: de gelopen-maar-nog-niet-vervallen rente wordt prorata geboekt via rekening 492 'Toe te rekenen kosten' (CBN 148/4).

**Waarom?** Matching: rente moet in het juiste boekjaar staan, ook al wordt ze pas later cash betaald.


_Grondslag: CBN 148/4 + KB WVV art. 3:60_

### Terugbetaling op vervaldag ⚖️

Op vervaldag betaalt de NV het nominaal bedrag terug aan de obligatiehouders. Schuld wordt nul; bank vermindert met het terugbetaalde bedrag.



_Grondslag: Boekhoudkundige verwerking_


## In de praktijk

<h3 id="onderscheid-met-converteerbare-obligatie">Onderscheid met converteerbare obligatie</h3>

> [!tip]- Onderscheid met converteerbare obligatie
> Een converteerbare obligatie geeft de houder recht om op vervaldag te kiezen tussen terugbetaling of conversie in aandelen (volgens vooraf vastgelegde conversieratio). Boekhoudkundig deels behandeld als schuld (170), deels als kapitaalcomponent. 🤖


## Valkuilen

> [!warning]- Uitgiftekosten van een obligatielening (notaris, publicatie, bankcommissies) mogen GESPREID worden over de looptijd van de lening — uitzonde…
> ⚠️ Uitgiftekosten van een obligatielening (notaris, publicatie, bankcommissies) mogen GESPREID worden over de looptijd van de lening — uitzondering op de 5-jaars-regel voor oprichtingskosten (KB WVV art. 3:37). Niet vergeten in toelichting bij uitgifte > 5 jaar. ⚖️
>
> _Bron: KB WVV art. 3:37_



## Zie ook

- **Getriggerd door**: [[oprichtingskosten]]

> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

## Bronnen

[^1]: `CBN-2019-07-boekhoudkundige-verwerking-van-de-uitgifte-van-een-obligatielening__sec_kosten-bij-uitgifte-van-leningen`
[^2]: `MAR-ondernemingen__art_1`
