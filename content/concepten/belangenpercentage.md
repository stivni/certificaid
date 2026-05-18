---
title: Belangenpercentage
tags:
- concept
- begrip
- po-1-4
linked_anchors:
- 1.4.I.C
- 1.4.I.D
- 1.4.I.E
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: inferred-from-aggregation
node_type: begrip
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/belangenpercentage.json
gegenereerd_op: '2026-05-18'
---
# Belangenpercentage 🤖

Een meetbegrip uit het Belgische boekhoudrecht-consolidatieregime (Boek 3, Titel 2 van het KB WVV). Samen met het controlepercentage onderbouwt het de kwalificatie van de relatie met een deelneming en de keuze van de consolidatietechniek. Waar controle de macht meet, meet het belangenpercentage het economisch winstrecht.

> [!summary] Korte inhoud
> Het deel van het kapitaal (en dus van het winstrecht) dat een moeder in een dochter of geassocieerde onderneming bezit.

> [!info] Behoort tot: [[minderheidsbelangen]]

Het deel van het kapitaal (en dus van het winstrecht) dat een moeder in een dochter of geassocieerde onderneming bezit. Bij een keten van vennootschappen wordt het belangenpercentage van schakel tot schakel vermenigvuldigd. Het belangenpercentage bepaalt welk stuk van het eigen vermogen en het resultaat van die andere onderneming aan de moeder mag worden toegerekend; het complement (1 − belangenpercentage) is het aandeel van derden bij integrale consolidatie.

_Bron: KB WVV art. 3:137 (toepassing aandeel van derden)_


## Berekening

### Belangenpercentage in een verticale keten

**Belangenpercentage in een verticale keten** 
```
belang (moeder in onderste dochter) = belang (moeder in schakel1) × belang (schakel1 in schakel2) × … × belang (schakeln-1 in onderste dochter)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belang (X in Y)` | Direct kapitaalaandeel van X in Y, uitgedrukt als breuk of percentage | % |

**Voorbeeld-invulling**: belang Aurelia in Brugse = 80 %; belang Brugse in Drukkerij Dendermonde = 60 %

```
0,80 × 0,60 = 0,48
```

_Resultaat in %_
**Aandeel van derden** 
```
aandeel van derden = 1 − belangenpercentage moeder
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage moeder` | Effectief belang van de moeder in de dochter (eventueel na ketenvermenigvuldiging) | % |

**Voorbeeld-invulling**: belangenpercentage Aurelia in Brugse = 80 %

```
1 − 80 % = 20 %
```

_Resultaat in %_
*Een eigendomsbelang vloeit niet onverdund door schakels; elke schakel verdeelt een evenredig stuk eigendom over derden. Anders dan voor controle wordt het belangenpercentage dus wél vermenigvuldigd over een keten.*

### 1. Teken de keten uit

Maak een lijstje of pijldiagram met alle vennootschappen die tussen de uiteindelijke moeder en de onderste dochter staan.

**Waarom?** Zonder duidelijke ketenstructuur weet je niet welke schakels je moet vermenigvuldigen, en mis je makkelijk een tussenniveau.

**📥 Input**:
- Aandelenstructuur-overzicht → **Wie bezit welk percentage van wie** _(document)_

**📤 Output**:
- Ketenschema → **Opeenvolging van schakels** _(document)_

**🛠️ Hoe**:

1. Start bij de uiteindelijke moeder (bv. Aurelia Holding NV).
2. Noteer elke directe deelneming met een pijl en het percentage: Aurelia → Brugse Brouwerij BV (80 %).
3. Doe hetzelfde voor de volgende schakel: Brugse Brouwerij BV → Drukkerij Dendermonde BV (60 %).
4. Stop bij de onderste dochter waarin je het belang wil bepalen.


**Grondslag**: KB WVV art. 3:137 (toepassing)

### 2. Bepaal het directe belang per schakel

Schrijf per schakel het belangenpercentage uit: welk deel van het kapitaal bezit de bovenliggende vennootschap in de onderliggende.

**Waarom?** De berekening werkt alleen als je elke schakel correct hebt; één foutief percentage vervalst het eindresultaat over de hele keten.

**📥 Input**:
- Aandeelhoudersregister of statuten per schakel → **Aandeel in kapitaal** _(percentage)_

**📤 Output**:
- Lijst directe belangen → **Eén percentage per schakel** _(percentage)_

**🛠️ Hoe**:

1. Open per schakel het aandeelhoudersregister of de aandelenkoopovereenkomst.
2. Neem het percentage dat de bovenliggende vennootschap bezit van het kapitaal (niet de stemrechten — die horen bij controle).
3. Let op preferente aandelen of certificaten: die kunnen ervoor zorgen dat belang en controle uiteenlopen.
4. Noteer voor de keten Aurelia → Brugse: 80 %. Voor Brugse → Drukkerij Dendermonde: 60 %.


**Grondslag**: KB WVV art. 3:137 (toepassing)

### 3. Vermenigvuldig de schakels

Vermenigvuldig de directe belangenpercentages over alle schakels om het effectieve belang van de uiteindelijke moeder in de onderste dochter te bekomen.

**Waarom?** Eigendom verdunt: een belang van 80 % in een schakel die zelf maar 60 % bezit, levert maar 48 % effectief belang in de onderste vennootschap op.

**📥 Input**:
- Lijst directe belangen uit stap 2 → **Percentage per schakel** _(percentage)_

**📤 Output**:
- Effectief belangenpercentage → **Belang uiteindelijke moeder in onderste dochter** _(percentage)_

**🛠️ Hoe**:

1. Zet alle percentages op een rij: 80 % en 60 %.
2. Reken om naar decimaal: 0,80 en 0,60.
3. Vermenigvuldig: 0,80 × 0,60 = 0,48.
4. Zet terug naar percentage: 48 %.
5. Dit is het belang van Aurelia Holding NV in Drukkerij Dendermonde BV via Brugse Brouwerij BV.


> [!example]- Voorbeeld: Aurelia Holding NV bezit 80 % van Brugse Brouwerij BV; Brugse Brouwerij BV bezit 60 % van Drukkerij Dendermonde BV (gewo…
> Aurelia Holding NV bezit 80 % van Brugse Brouwerij BV; Brugse Brouwerij BV bezit 60 % van Drukkerij Dendermonde BV (gewone aandelen, geen preferente regelingen).
>
> 1. **Ketenschema** 💬
>
>    Aurelia Holding NV --80 %--> Brugse Brouwerij BV --60 %--> Drukkerij Dendermonde BV
>
> 2. **Berekening effectief belang** 🧮
>
>    belang Aurelia in Drukkerij Dendermonde = 0,80 × 0,60 = **0,48 = 48 %**
>    aandeel van derden in Drukkerij Dendermonde = 100 % − 48 % = **52 %**
>
> 3. **Toepassing op resultaat** 🧮
>
>    Resultaat Drukkerij Dendermonde boekjaar = 100
>    Aandeel Aurelia (via belang) = 48 % × 100 = **48**
>    Aandeel van derden in resultaat = 52 % × 100 = **52**
>

**Grondslag**: KB WVV art. 3:137 (toepassing)

**Voorbeeld**: Aurelia Holding NV bezit 80 % van A; A bezit 60 % van B (beide via kapitaal en stemrechten, geen preferente regelingen).

```
belang% (M in B) = 0,80 × 0,60 = 0,48 = 48 %
```

Resultaat: Aurelia Holding NV heeft een economisch belang van 48 % in B. Het aandeel van derden in B = 100 % − 48 % = 52 %. Indien B een resultaat van 100 heeft, bedraagt het aandeel van derden in het resultaat 52.

## In de praktijk

<h3 id="berekening-in-ketenstructuur">Berekening in ketenstructuur</h3>

> [!tip]- Berekening in ketenstructuur
> Belangenpercentages vermenigvuldigen zich langs een keten. Voorbeeld: Aurelia Holding NV bezit 80 % van Brugse Brouwerij BV, en Brugse Brouwerij BV bezit 60 % van Drukkerij Dendermonde BV → belang van Aurelia in Drukkerij Dendermonde = 0,80 × 0,60 = 48 %. 🤖

> [!tip]- Herkennen op het examen
> Examen-tabel 'X % van A, A heeft Y % van B' → belangenpercentage van X in B = X % × Y %.

<h3 id="bepaling-aandeel-van-derden-bij-integrale-consolidatie">Bepaling aandeel van derden bij integrale consolidatie</h3>

> [!tip]- Bepaling aandeel van derden bij integrale consolidatie
> Bij integrale consolidatie komt 100 % van de activa en schulden van de dochter in de geconsolideerde balans. Het deel dat niet aan de moeder toebehoort (1 − belangenpercentage) verschijnt apart als 'Belangen van derden' op de balans en als 'Aandeel van derden in het resultaat' op de resultatenrekening. ⚖️


> [!info]- Niet verwarren met [[controlepercentage]]
> Belangenpercentage = aandeel in het kapitaal (en winst); wordt over een keten vermenigvuldigd. Controlepercentage = aandeel in de stemrechten (zeggenschap); wordt niet vermenigvuldigd zolang elke schakel exclusief gecontroleerd wordt door de bovenliggende.
>
> _Trigger_: Examen: vraag eerst 'wat moet ik berekenen?' — winstaandeel of aandeel van derden → belangenpercentage; consolidatieverplichting of -methode → controlepercentage.


## Valkuilen

> [!warning]- Belangenpercentage en controlepercentage worden vaak verward
> ⚠️ Belangenpercentage en controlepercentage worden vaak verward. Een opgave die zegt 'Aurelia bezit 60 %' is dubbelzinnig — 60 % van de stemrechten (controle) of 60 % van het kapitaal (belang)? Bij gewone aandelen vallen die samen, bij preferente aandelen of certificaten kunnen ze uit elkaar lopen. 🤖
>
> _Bron: Synthese examenpraktijk_



## Zie ook

- **Vereist kennis van**: [[controle]]
- **Getriggerd door**: [[integrale-consolidatie]]

## Voorbeelden

Aurelia Holding NV bezit 80 % van Brugse Brouwerij BV → belangenpercentage = 80 %; aandeel van derden = 20 %.

## Bronnen

[^1]: `KB-WVV-2019__art_3_108`
[^2]: `CBN-2022-11-vermogensmutatiemethode__sec_eerste-consolidatie`
[^3]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen`
