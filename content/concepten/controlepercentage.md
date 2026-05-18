---
title: Controlepercentage
tags:
- concept
- begrip
- po-1-4
linked_anchors:
- 1.4.I.C
- 1.4.I.B
- 1.4.I.D
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: inferred-from-aggregation
node_type: begrip
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/controlepercentage.json
gegenereerd_op: '2026-05-18'
---
# Controlepercentage 🤖

> [!summary] Korte inhoud
> Het percentage van de stemrechten dat een moeder direct of indirect (via dochters) in een andere vennootschap aanhoudt.

Het percentage van de stemrechten dat een moeder direct of indirect (via dochters) in een andere vennootschap aanhoudt. Het controlepercentage gebruik je om te toetsen of er sprake is van controle in rechte. Belangrijk verschil met belangenpercentage: in een keten (moeder → tussenschakel → onderste dochter) wordt het controlepercentage níet vermenigvuldigd. Zolang elke schakel exclusief gecontroleerd wordt, telt het volledige stemrechtpercentage van de onderste schakel mee als 'gecontroleerd door de moeder'.

_Bron: WVV art. 1:14 jo. art. 1:16_


## Berekening

### Controlepercentage in een verticale keten

**Controlepercentage doorvloei bij ononderbroken keten** 
```
controle (top-moeder in onderste dochter) = stemrecht% (directe moeder van onderste dochter)  — op voorwaarde dat elke schakel exclusief gecontroleerd wordt
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `stemrecht% (directe moeder van onderste dochter)` | Percentage van de stemrechten dat de directe moeder van de onderste dochter rechtstreeks aanhoudt | % |

**Voorbeeld-invulling**: Aurelia → Brugse (80 % stemrechten, exclusieve controle) → Drukkerij Dendermonde (60 % stemrechten)

```
controle% Aurelia in Drukkerij Dendermonde = 60 % (geen vermenigvuldiging — keten is ononderbroken)
```

_Resultaat in %_
*Zodra elke tussenschakel exclusief gecontroleerd wordt, vloeit de zeggenschap over de onderste schakel volledig door naar de top. Vermenigvuldigen geldt enkel voor het belang (economisch eigendom), niet voor de controle (zeggenschap).*

### 1. Toets of elke schakel exclusief gecontroleerd wordt

Ga voor elke tussenschakel na of de bovenliggende vennootschap er exclusieve controle over uitoefent (> 50 % stemrechten of een andere onweerlegbare titel zoals statutaire macht of stemovereenkomst).

**Waarom?** De doorlopende-controle-redenering werkt alleen als elke schakel zelf exclusief gecontroleerd wordt. Breekt de keten op één plek (bv. 50/50-joint venture), dan stopt de zeggenschap daar.

**📥 Input**:
- Aandeelhoudersregister + statuten per schakel → **Stemrechten + stemovereenkomsten** _(document)_

**📤 Output**:
- Ketenanalyse → **Per schakel: exclusieve controle ja/nee** _(conclusie)_

**🛠️ Hoe**:

1. Start bij de top (Aurelia Holding NV).
2. Voor elke schakel: open het aandeelhoudersregister + de statuten.
3. Bepaal het stemrechtpercentage van de bovenliggende vennootschap in de onderliggende.
4. Stemrechten > 50 % → exclusieve controle in rechte (onweerlegbaar).
5. Stemrechten ≤ 50 % → controleer of er een andere titel is (stemovereenkomst, statutaire macht, controle in feite via twee-vergaderingen-test).
6. Noteer per schakel ja/nee.


**Grondslag**: WVV art. 1:14, § 2 jo. art. 1:16

### 2. Bij doorlopende controle: controle% = stemrecht% in onderste schakel

Als elke schakel exclusief gecontroleerd wordt, is het controlepercentage van de top-moeder in de onderste dochter gelijk aan het stemrechtpercentage dat de directe moeder van die onderste dochter aanhoudt. Geen vermenigvuldiging.

**Waarom?** Zeggenschap is geen breuk maar een geheel: zodra je elke schakel kunt sturen, kun je ook het stemgedrag van de onderste vennootschap volledig bepalen — niet maar 'voor een fractie'.

**📥 Input**:
- Ketenanalyse uit stap 1 → **Stemrechten per schakel** _(percentage)_

**📤 Output**:
- Resultaat → **Controlepercentage top-moeder in onderste dochter** _(percentage)_

**🛠️ Hoe**:

1. Bevestig uit stap 1: elke schakel exclusief gecontroleerd → ja.
2. Neem het stemrechtpercentage van de directe moeder van de onderste dochter.
3. Dat percentage is meteen het controlepercentage van de top-moeder.
4. Voor Aurelia → Brugse (80 %) → Drukkerij Dendermonde (60 %): controle% Aurelia in Drukkerij Dendermonde = 60 %.


**Grondslag**: Synthese WVV art. 1:14

### 3. Bij gebroken keten: geen doorlopende controle

Als één tussenschakel niet exclusief gecontroleerd wordt (bv. 50/50-joint venture of geassocieerde), valt de doorlopende-controle-redenering weg. De onderste vennootschap is geen dochter van de top-moeder — afhankelijk van de structuur wordt zij geassocieerde of gemeenschappelijke dochter.

**Waarom?** Zonder ononderbroken zeggenschap kun je het stemgedrag van de onderste vennootschap niet eenzijdig bepalen. De wet erkent dat als 'geen controle' en stuurt door naar de andere consolidatiemethoden (evenredig, vermogensmutatie).

**📥 Input**:
- Ketenanalyse uit stap 1 → **Eén schakel zonder exclusieve controle** _(conclusie)_

**📤 Output**:
- Resultaat → **Geen dochter; mogelijk geassocieerde of gemeenschappelijke dochter** _(conclusie)_

**🛠️ Hoe**:

1. Identificeer de schakel die de keten breekt (geen exclusieve controle).
2. Beoordeel die schakel apart: is er invloed van betekenis (20–50 % zonder controle)? → geassocieerde → vermogensmutatie.
3. Is er gezamenlijke controle (overeenkomst tussen vennoten)? → gemeenschappelijke dochter → evenredige consolidatie of vermogensmutatie.
4. De top-moeder beoordeelt haar relatie tot die schakel rechtstreeks, niet via de onderbroken keten.


> [!example]- Voorbeeld: Aurelia Holding NV bezit 80 % van Cardinal Group NV; Cardinal Group NV bezit 50 % van Filmstudio Florence BV samen met E…
> Aurelia Holding NV bezit 80 % van Cardinal Group NV; Cardinal Group NV bezit 50 % van Filmstudio Florence BV samen met Energiehuis Evergem BV (gezamenlijke controle door overeenkomst).
>
> 1. **Ketenanalyse** 💬
>
>    Aurelia → Cardinal: 80 % → exclusieve controle ja.
>    Cardinal → Filmstudio Florence: 50 % met overeenkomst → géén exclusieve controle, wel gezamenlijke controle.
>
> 2. **Conclusie controle-doorvloei** 💬
>
>    De keten breekt bij Cardinal → Filmstudio Florence. Aurelia heeft daarom geen exclusieve controle over Filmstudio Florence. Filmstudio Florence is op Cardinal-niveau een gemeenschappelijke dochter (evenredige consolidatie of vermogensmutatie); Aurelia consolideert op haar beurt Cardinal integraal — Filmstudio Florence verschijnt in de Aurelia-cijfers via de Cardinal-cijfers.
>

**Grondslag**: Synthese WVV art. 1:14 + CBN 2017/02

**Voorbeeld**: Aurelia Holding NV bezit 80 % van Brugse Brouwerij BV; Brugse bezit 60 % van Drukkerij Dendermonde BV. Brugse wordt exclusief gecontroleerd door Aurelia.

```
controle% (Aurelia in Drukkerij Dendermonde) = controle% (Brugse in Drukkerij Dendermonde) = 60 %. (Belangenpercentage (Aurelia in Drukkerij Dendermonde) = 0,80 × 0,60 = 0,48 = 48 %.)
```

Resultaat: Aurelia Holding NV controleert Drukkerij Dendermonde exclusief (via Brugse, > 50 % stemrechten). Drukkerij Dendermonde is een dochter van Aurelia en wordt integraal geconsolideerd. Het aandeel van derden in Drukkerij Dendermonde bedraagt 1 − 0,48 = 52 % van haar eigen vermogen.

## In de praktijk

<h3 id="onderscheid-met-belangenpercentage">Onderscheid met belangenpercentage</h3>

> [!tip]- Onderscheid met belangenpercentage
> Controlepercentage meet macht (stemrechten); belangenpercentage meet eigendom (kapitaal en winstrecht). Beide kunnen uiteenlopen bij bijzondere structuren: preferente aandelen, certificering, stemrechtloze aandelen. In de keten Aurelia → 80 % Brugse → 60 % Drukkerij Dendermonde is het controlepercentage van Aurelia in Drukkerij Dendermonde nog steeds 60 % (zolang Brugse exclusief gecontroleerd wordt), terwijl het belangenpercentage 80 % × 60 % = 48 % is. 🤖

> [!tip]- Herkennen op het examen
> Tabelopgave 'X % van A en A heeft Y % van B' — controle: niet vermenigvuldigen zolang elke schakel exclusief gecontroleerd wordt; belang: wél vermenigvuldigen.

<h3 id="beoordelen-van-consolidatieverplichting">Beoordelen van consolidatieverplichting</h3>

> [!tip]- Beoordelen van consolidatieverplichting
> Een controlepercentage > 50 % stemrechten levert in beginsel exclusieve controle in rechte op en triggert integrale consolidatie. Bij precies 50 % zonder stemovereenkomst is er géén controle. Bij stemovereenkomst tussen meerdere vennoten ontstaat gezamenlijke controle (evenredige consolidatie of vermogensmutatie). 🤖


## Valkuilen

> [!warning]- Niet alle aandelen geven stemrechten
> ⚠️ Niet alle aandelen geven stemrechten. Bij stemrechtloze aandelen of preferente aandelen kunnen kapitaal (belangenpercentage) en stemrechten (controlepercentage) uit elkaar lopen. Lees de opgave nauwkeurig: gaat het over 'aandelen', 'stemrechten' of 'kapitaal'? 🤖
>
> _Bron: Synthese WVV/CBN_



## Zie ook

- **Vereist kennis van**: [[controle]]
- **Getriggerd door**: [[integrale-consolidatie]]

## Bronnen

[^1]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen`
[^2]: `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_voorbeeld-7`
[^3]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_geval-2-de-vennootschap-a-en-de-vennootschap-b-hebben-geen-o_2`
