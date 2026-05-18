---
title: Toegevoegde waarde (economische maatstaf in financiële analyse)
tags:
- concept
- cluster
- po-1-9
linked_anchors:
- 1.9.V.A
- 1.9.taak.1
programmaonderdelen:
- '1.9'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/toegevoegde-waarde-financiele-analyse.json
gegenereerd_op: '2026-05-18'
---
# Toegevoegde waarde (economische maatstaf in financiële analyse) 🤖

> [!summary] Korte inhoud
> Toegevoegde waarde meet de welvaart die de onderneming zelf creëert door productie of dienstverlening, los van de waarde die ze inkoopt bij derden.

> [!info] Behoort tot: [[ratio-vier-doelen-vergelijking]]

Toegevoegde waarde meet de welvaart die de onderneming zelf creëert door productie of dienstverlening, los van de waarde die ze inkoopt bij derden. Het is de economische bovenbouw van de resultatenrekening: hoeveel waarde voegt de onderneming toe aan de aangekochte goederen en diensten?

_Bron: Financiële analyse — NBB-Centrale voor Balansen_


## Bouwstenen

### Bedrijfsopbrengsten min externe aankopen 🤖

Tel de bedrijfsopbrengsten (omzet + andere bedrijfsopbrengsten + voorraadwijziging) en trek daar alle goederen en diensten die de onderneming bij derden inkocht van af.

**Waarom?** Het verschil is wat de onderneming binnen haar eigen muren heeft toegevoegd — beschikbaar om personeel, kapitaal en de overheid te vergoeden.


_Grondslag: Vakdoctrine financiële analyse_

### Verdeling over productiefactoren 🤖

De toegevoegde waarde wordt verdeeld over vier bestemmingen: personeel (lonen + sociale lasten), kapitaalverschaffers (financiële kosten), overheid (belastingen) en de onderneming zelf (zelffinanciering, gereserveerd).

**Waarom?** Wie ontvangt welk deel van de gecreëerde welvaart? Dit is de structurele lezing van de resultatenrekening — verklaart waarom hetzelfde bedrijfsmodel verschillend uitpakt afhankelijk van loonkosten- of intrestbeleid.


_Grondslag: Vakdoctrine financiële analyse_


## Berekening

### Toegevoegde waarde

**Toegevoegde waarde (bruto)** 
```
TW = bedrijfsopbrengsten − aankopen goederen en diensten van derden
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `TW` | Bruto toegevoegde waarde | EUR |
| `bedrijfsopbrengsten` | Omzet + andere bedrijfsopbrengsten + voorraadwijziging (rubrieken 70-74) | EUR |
| `aankopen goederen en diensten` | Aankopen handelsgoederen + diensten en diverse goederen (rubrieken 60-61) | EUR |

**Voorbeeld-invulling**: bedrijfsopbrengsten = € 50.000.000, aankopen = € 32.000.000

```
€ 50.000.000 − € 32.000.000 = € 18.000.000
```

_Resultaat in EUR_
**Toegevoegde waarde per VTE (productiviteit)** (volgt op: toegevoegde-waarde)
```
TW per VTE = toegevoegde waarde / gemiddeld aantal voltijdse equivalenten
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `VTE` | Voltijdse equivalent (gemiddeld over boekjaar) | personen |

**Voorbeeld-invulling**: TW = € 18.000.000, VTE = 250

```
€ 18.000.000 / 250 = € 72.000 per VTE
```

_Resultaat in EUR/VTE_

## In de praktijk

<h3 id="1.9.V.A">Productiviteits-benchmark</h3>

> [!tip]- Productiviteits-benchmark
> TW per VTE is de standaard productiviteits-vergelijking met de sector. NBB publiceert deze ratio per NACE-code. Een TW per VTE die structureel onder het sectorgemiddelde ligt, signaleert dat de onderneming relatief veel personeel inzet voor relatief weinig waardecreatie — examenvalkuil voor diagnose-vragen. 🤖


> [!info]- Niet verwarren met [[rentabiliteit-totaal-activa-roa]]
> ROA meet rendement op de geïnvesteerde activa (kapitaalproductiviteit); toegevoegde waarde meet welvaartscreatie vóór verdeling (economische productiviteit). Beide kunnen tegelijk goed of slecht zijn.
>
> _Trigger_: Examenvraag 'productiviteit vs rendabiliteit': TW/VTE = arbeidsproductiviteit; ROA = totale kapitaalproductiviteit. Mix niet.


## Zie ook

- **Vereist kennis van**: [[horizontale-analyse-jaarrekening]]

## Bronnen

[^1]: `anchor-1.9.V.A`
