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
gegenereerd_op: '2026-05-16'
---
# Controlepercentage 🤖

> Het percentage van de stemrechten dat een moeder direct of indirect (via dochters) in een andere vennootschap aanhoudt. Het controlepercentage gebruik je om te toetsen of er sprake is van controle in rechte. Belangrijk verschil met belangenpercentage: in een keten (moeder → tussenschakel → onderste dochter) wordt het controlepercentage níet vermenigvuldigd. Zolang elke schakel exclusief gecontroleerd wordt, telt het volledige stemrechtpercentage van de onderste schakel mee als 'gecontroleerd door de moeder'.
>
> _Bron: WVV art. 1:14 jo. art. 1:16_


> [!summary] Korte definitie
> Het percentage van de stemrechten dat een moeder direct of indirect (via dochters) in een andere vennootschap aanhoudt.

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

### . 

**Voorbeeld**: Aurelia Holding NV bezit 80 % van Brugse Brouwerij BV; Brugse bezit 60 % van Drukkerij Dendermonde BV. Brugse wordt exclusief gecontroleerd door Aurelia.

```
controle% (Aurelia in Drukkerij Dendermonde) = controle% (Brugse in Drukkerij Dendermonde) = 60 %. (Belangenpercentage (Aurelia in Drukkerij Dendermonde) = 0,80 × 0,60 = 0,48 = 48 %.)
```

Resultaat: Aurelia Holding NV controleert Drukkerij Dendermonde exclusief (via Brugse, > 50 % stemrechten). Drukkerij Dendermonde is een dochter van Aurelia en wordt integraal geconsolideerd. Het aandeel van derden in Drukkerij Dendermonde bedraagt 1 − 0,48 = 52 % van haar eigen vermogen.

## In de praktijk

### Onderscheid met belangenpercentage {id="onderscheid-met-belangenpercentage"}

Controlepercentage meet macht (stemrechten); belangenpercentage meet eigendom (kapitaal en winstrecht). Beide kunnen uiteenlopen bij bijzondere structuren: preferente aandelen, certificering, stemrechtloze aandelen. In de keten Aurelia → 80 % Brugse → 60 % Drukkerij Dendermonde is het controlepercentage van Aurelia in Drukkerij Dendermonde nog steeds 60 % (zolang Brugse exclusief gecontroleerd wordt), terwijl het belangenpercentage 80 % × 60 % = 48 % is. 🤖

**Herkenningspunt**: Tabelopgave 'X % van A en A heeft Y % van B' — controle: niet vermenigvuldigen zolang elke schakel exclusief gecontroleerd wordt; belang: wél vermenigvuldigen.

### Beoordelen van consolidatieverplichting {id="beoordelen-van-consolidatieverplichting"}

Een controlepercentage > 50 % stemrechten levert in beginsel exclusieve controle in rechte op en triggert integrale consolidatie. Bij precies 50 % zonder stemovereenkomst is er géén controle. Bij stemovereenkomst tussen meerdere vennoten ontstaat gezamenlijke controle (evenredige consolidatie of vermogensmutatie). 🤖


## Valkuilen

- ⚠️ Niet alle aandelen geven stemrechten. Bij stemrechtloze aandelen of preferente aandelen kunnen kapitaal (belangenpercentage) en stemrechten (controlepercentage) uit elkaar lopen. Lees de opgave nauwkeurig: gaat het over 'aandelen', 'stemrechten' of 'kapitaal'? 🤖

## Zie ook

- **Vereist kennis van**: [[controle]]
- **Getriggerd door**: [[integrale-consolidatie]]

## Bronnen

[^1]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen`
[^2]: `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_voorbeeld-7`
[^3]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_geval-2-de-vennootschap-a-en-de-vennootschap-b-hebben-geen-o_2`
