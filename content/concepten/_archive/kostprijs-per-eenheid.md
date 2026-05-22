---
title: Kostprijs per eenheid
tags:
- concept
- begrip
- po-1-8
linked_anchors:
- 1.8.III.A
- 1.8.taak.1
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: begrip
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/kostprijs-per-eenheid.json
gegenereerd_op: '2026-05-21'
---
# Kostprijs per eenheid 🔗

De kostprijs per eenheid is het bedrag aan opgeofferde middelen per geproduceerd product, geleverde dienst of uitgevoerde order. Welke kosten erin zitten hangt van het gekozen kostprijsmodel af: wettelijke vervaardigingsprijs (CBN 132/7 — directe + indirecte productiekosten), volledige bedrijfskostprijs (intern, ook commercieel en administratief), of variabele kostprijs (alleen variabele kosten, voor direct-costing-marge-analyse). De stagiair moet expliciet kunnen aangeven welke variant gevraagd is.

> [!summary] Korte inhoud
> De kostprijs per eenheid is het bedrag aan opgeofferde middelen om één eenheid van een product, dienst of order te realiseren.

> [!info] Behoort tot: [[analytische-boekhouding]]

De kostprijs per eenheid is het bedrag aan opgeofferde middelen om één eenheid van een product, dienst of order te realiseren. De kostprijs kan een vervaardigingsprijs zijn (wettelijk, CBN 132/7), een volledige bedrijfskostprijs (interne, inclusief commercieel + administratief) of een variabele kostprijs (direct costing). De interpretatie hangt af van het beoogde gebruik (voorraadwaardering / verkoopprijszetting / beslissing).

_Bron: Management accounting — bron-gap_



## Berekening

### Drie varianten kostprijs per eenheid

**Vervaardigingsprijs per eenheid (wettelijk, CBN 132/7)** 
```
vervaardigingsprijs_per_eenheid = (direct materiaal + directe productiekosten + toegerekende indirecte productiekosten) / aantal eenheden
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `direct materiaal` | Verbruikt materiaal aan voorraadprijs | EUR |
| `directe productiekosten` | Arbeid en andere rechtstreeks toewijsbare kosten | EUR |
| `toegerekende indirecte productiekosten` | Productiegebonden overhead × sleutel | EUR |
| `aantal eenheden` | Geproduceerde eenheden in de periode | stuks |

**Voorbeeld-invulling**: Yperse Werkplaats BV partij van 100 tapijten: materiaal € 12.000 + directe arbeid € 4.500 + overhead € 3.600

```
(€ 12.000 + € 4.500 + € 3.600) / 100 = € 201/tapijt
```

_Resultaat in EUR/stuk_
**Volledige bedrijfskostprijs per eenheid (intern)** (volgt op: vervaardigingsprijs-per-eenheid)
```
volledige_kostprijs_per_eenheid = vervaardigingsprijs_per_eenheid + toegerekende commerciële_en_administratieve_kosten
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `vervaardigingsprijs_per_eenheid` | Zie formule 1 | EUR/stuk |
| `toegerekende commerciële_en_administratieve_kosten` | Verdeelde overhead voor verkoop, marketing, administratie | EUR/stuk |

**Voorbeeld-invulling**: Yperse tapijt: vervaardigingsprijs € 201, commercieel/administratief toegerekend € 35/tapijt

```
€ 201 + € 35 = € 236/tapijt
```

_Resultaat in EUR/stuk_
**Variabele kostprijs per eenheid (direct costing)** 
```
variabele_kostprijs_per_eenheid = (directe + indirecte variabele kosten) / aantal eenheden
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `directe + indirecte variabele kosten` | Alle kosten die mee variëren met volume (materiaal, productie-arbeid, variabele overhead) | EUR |
| `aantal eenheden` | Geproduceerde eenheden | stuks |

**Voorbeeld-invulling**: Yperse partij 100 tapijten: variabele kosten € 13.000

```
€ 13.000 / 100 = € 130/tapijt
```

_Resultaat in EUR/stuk_
*Welke kostprijs per eenheid je berekent, hangt af van het doel: voorraadwaardering (vervaardigingsprijs), full bedrijfsbeoordeling (volledige kostprijs) of marge-/beslisanalyse (variabele kostprijs).*


## In de praktijk

<h3 id="drie-gebruiksdoelen-drie-cijfers">Drie gebruiksdoelen, drie cijfers</h3>

> [!tip]- Drie gebruiksdoelen, drie cijfers
> Voor voorraadwaardering: vervaardigingsprijs (wettelijk verplicht voor balans). Voor lange-termijn-prijszetting: volledige bedrijfskostprijs (dekt alle overhead). Voor extra-order-beslissingen: variabele kostprijs of marginale kostprijs (vaste kost is sunk). Examen-valkuil: één kostprijs gebruiken voor alle vragen. 🤖


## Zie ook

- **Vereist kennis van**: [[vervaardigingsprijs]]
- **Vereist kennis van**: [[marginale-kostprijs]]

## Voorbeelden

Yperse Werkplaats BV tapijt — drie kostprijsbegrippen: vervaardigingsprijs € 18 (materiaal + directe arbeid + productie-overhead), volledige bedrijfskostprijs € 22 (+ commercieel + administratief), variabele kostprijs € 13 (alleen variabele kosten). Verkoopprijs € 60. Welke kostprijs gebruiken? Hangt af van vraag.

## Bronnen

[^1]: `CBN-0132-07-boeking-en-waardering-van-voorraden__sec_vervaardigingsprijs`
