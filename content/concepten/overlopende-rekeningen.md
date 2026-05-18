---
title: Overlopende rekeningen
tags:
- concept
- cluster
- po-1-1
- po-1-2
linked_anchors:
- 1.1.II.L
- 1.2.V
- 1.2.taak.1
- 1.2.III.D
programmaonderdelen:
- '1.1'
- '1.2'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/overlopende-rekeningen.json
gegenereerd_op: '2026-05-18'
---
# Overlopende rekeningen ⚖️

> [!summary] Korte inhoud
> **Balansrekeningen** die het verschil tussen kasstroom en economische toerekening zichtbaar maken aan het eind van het boekjaar.

> [!info] Specialisatie van: [[matching-principe]]

**Balansrekeningen** die het verschil tussen kasstroom en economische toerekening zichtbaar maken aan het eind van het boekjaar. Twee paren: (1) **Over te dragen kosten** (490, actief): al betaalde kosten die op een volgend boekjaar betrekking hebben — vooruitbetaalde huur, premie verzekering 12 maanden. (2) **Verkregen opbrengsten** (491, actief): opbrengsten verdiend in lopend jaar maar nog niet ontvangen — bv. te ontvangen rente. (3) **Toe te rekenen kosten** (492, passief): kosten die op lopend jaar slaan maar nog niet zijn betaald — bv. december-elektriciteit, gewerkte uren personeel. (4) **Over te dragen opbrengsten** (493, passief): ontvangen bedragen die op volgend jaar betrekking hebben — bv. vooruitbetaalde abonnementen.

_Bron: KB WVV art. 3:60; MAR klasse 49_


## Bouwstenen

### Over te dragen kosten (490, actief) ⚖️

Kosten die in lopend boekjaar zijn betaald of geboekt maar economisch betrekking hebben op een volgend boekjaar. Worden op het actief uitgesteld om in het juiste boekjaar te belasten.

**Waarom?** Matching: kosten waar de baten in een toekomstig boekjaar liggen, mogen niet de winst van het lopende jaar drukken. Uitstellen via 490 corrigeert dat.


_Grondslag: KB WVV art. 3:60_

### Toe te rekenen kosten (492, passief) ⚖️

Kosten die op lopend boekjaar slaan maar nog niet betaald of gefactureerd zijn op balansdatum. Worden op het passief opgenomen als 'te betalen' kost.

**Waarom?** Volledigheid: alle kosten van het lopende jaar moeten in het resultaat, ook als de financiële afhandeling later komt.


_Grondslag: KB WVV art. 3:60_

### Verkregen opbrengsten (491, actief) ⚖️

Opbrengsten die in lopend jaar zijn verdiend maar nog niet ontvangen of gefactureerd. Bv. opgelopen rente op uitstaande vorderingen.

**Waarom?** Voorbeeld van matching aan opbrengstzijde: de rente die je verdient over december is een opbrengst van december, ook al vervalt ze pas in januari.


_Grondslag: KB WVV art. 3:60 + CBN 148/4_

### Over te dragen opbrengsten (493, passief) ⚖️

Opbrengsten die in lopend jaar al ontvangen of gefactureerd zijn maar economisch betrekking hebben op een volgend boekjaar.

**Waarom?** Voorzichtigheid + matching: ontvangen geld is geen opbrengst zolang de prestatie nog niet is geleverd. Uitstellen tot het juiste boekjaar.


_Grondslag: KB WVV art. 3:60_


## In de praktijk

<h3 id="klassieke-cut-off-correcties-bij-jaarafsluiting">Klassieke cut-off-correcties bij jaarafsluiting</h3>

> [!tip]- Klassieke cut-off-correcties bij jaarafsluiting
> De vier overlopende rekeningen zijn de werkpaarden van de jaarafsluiting. Typisch cut-off-werkblad: huur, verzekeringen, elektriciteit/gas, telecom, leasings, lonen + sociale bijdragen december, intresten op leningen, abonnementen ontvangen of geleverd. ⚖️

> [!tip]- Herkennen op het examen
> Examen: 'voorraad uit 31/12 ontvangen, factuur 5/1' = te ontvangen factuur (444), niet overlopende. 'huur vooruitbetaald in december voor januari' = over te dragen kost (490).

<h3 id="prorata-berekening-obligatie-intresten">Prorata-berekening obligatie-intresten</h3>

> [!tip]- Prorata-berekening obligatie-intresten
> Voor obligaties met periodieke coupons moet op balansdatum de gelopen-maar-nog-niet-vervallen rente prorata worden geboekt (CBN 148/4): coupon × (verstreken maanden / 12). ⚖️


## Valkuilen

> [!warning]- Overlopende rekeningen (klasse 49) zijn iets ANDERS dan handelsschulden of -vorderingen (klasse 4)
> ⚠️ Overlopende rekeningen (klasse 49) zijn iets ANDERS dan handelsschulden of -vorderingen (klasse 4). Toe te rekenen kosten (492) ≠ leveranciersschuld (44) — de leveranciersschuld vereist een factuur; toe te rekenen kost wordt geboekt op basis van schatting/contract als de factuur nog niet binnen is en GEEN aparte 'te ontvangen factuur'-status heeft. 🤖
>
> _Bron: MAR_



## Zie ook

- **Getriggerd door**: [[jaarafsluiting]]

> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

## Bronnen

[^1]: `MAR-ondernemingen__art_4`
