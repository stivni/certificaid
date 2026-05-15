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
schema_version: '1.2'
gegenereerd_uit: data/concepten/records/controlepercentage.json
gegenereerd_op: '2026-05-15'
---
# Controlepercentage 🤖

> Het percentage van de stemrechten dat een vennootschap (direct of indirect via dochterondernemingen) in een andere vennootschap aanhoudt. Het controlepercentage dient om te beoordelen of er sprake is van controle in rechte. In een ketenstructuur (M → A → B) wordt het controlepercentage doorgaans niet vermenigvuldigd: zodra elke schakel exclusieve controle uitoefent, telt het volledige stemrechtpercentage van de onderste schakel mee als 'gecontroleerd door de moeder'.
>
> _Bron: WVV art. 1:14 jo. art. 1:16_


## Berekening

### Controlepercentage in een verticale keten

**Formule**: `controle% (M in B) = controle% (A in B), op voorwaarde dat M exclusieve controle uitoefent op A`

*Zodra elke tussenliggende schakel exclusief wordt gecontroleerd, vloeit de zeggenschap over de onderste schakel volledig door naar de top. Vermenigvuldigen geldt enkel voor het belang (economisch eigenaarschap), niet voor de controle (zeggenschap).*

**Stappen**:
1. {'volgorde': 1, 'text': 'Bepaal of M elke tussenliggende schakel exclusief controleert (> 50 % stemrechten of andere onweerlegbare titel).'}
2. {'volgorde': 2, 'text': 'Zo ja: het controlepercentage van M in B is gelijk aan het controlepercentage van de directe moeder (A) in B.'}
3. {'volgorde': 3, 'text': 'Zo niet: er is geen doorlopende controle; B is geen dochter van M maar mogelijk een geassocieerde of een gemeenschappelijke dochter, afhankelijk van de structuur.'}

**Voorbeeld**: M bezit 80 % van A; A bezit 60 % van B. A is exclusief gecontroleerd door M.

```
controle% (M in B) = controle% (A in B) = 60 %. (Belangenpercentage (M in B) = 0,80 × 0,60 = 0,48 = 48 %.)
```

Resultaat: M controleert B exclusief (> 50 % stemrechten via A). B is een dochteronderneming van M en wordt integraal geconsolideerd. Het aandeel van derden in B bedraagt 1 − 0,48 = 52 % van het eigen vermogen van B.

## In de praktijk

### Onderscheid met belangenpercentage {id="onderscheid-met-belangenpercentage"}

Het controlepercentage meet de macht (stemrechten); het belangenpercentage meet het economisch eigenaarschap (kapitaal, winstrecht). Beide kunnen verschillen bij stemrechtenstructuren (preferente aandelen, certificering, stemrechtloze aandelen). In een keten M → 80 % A → 60 % B bedraagt het controlepercentage van M in B nog steeds 60 % (zolang A exclusief gecontroleerd wordt), terwijl het belangenpercentage 80 % × 60 % = 48 % bedraagt. 🤖

**Herkenningspunt**: Tabelopgaven met 'M x % van A en A y % van B' — controle: niet vermenigvuldigen zolang elke schakel controleert; belang: wel vermenigvuldigen.

### Beoordelen van consolidatieverplichting {id="beoordelen-van-consolidatieverplichting"}

Een controlepercentage > 50 % stemrechten levert in beginsel exclusieve controle (in rechte) op en triggert integrale consolidatie. Bij precies 50 % zonder stemovereenkomst is er géén controle. Bij stemovereenkomst tussen meerdere vennoten ontstaat gezamenlijke controle. 🤖


## Vergelijkingsparen

| Verwarrend met | Verschil | Trigger |
|---|---|---|
| [[belangenpercentage]] | Controlepercentage = stemrechten (zeggenschap); belangenpercentage = kapitaal/eigendomsverhouding. Bij ketens: controle wordt niet vermenigvuldigd, belang wel. | Vraagstellingen die expliciet vragen 'wie heeft controle' versus 'welk aandeel van de winst' — twee verschillende berekeningen. |
| [[controle]] | Controlepercentage is een kwantitatief getal; controle is een kwalitatief oordeel (al dan niet). Een controlepercentage > 50 % triggert het onweerlegbaar vermoeden van controle in rechte, maar controle kan ook bij lager percentages bestaan (controle in feite, gezamenlijke controle). | — |

## Valkuilen

- ⚠️ Niet alle aandelen geven stemrechten. Bij stemrechtloze aandelen of preferente aandelen valt het kapitaal (belangenpercentage) níet samen met de stemrechten (controlepercentage). Lees de opgave nauwkeurig. 🤖

## Bronnen

[^1]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen`
[^2]: `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_voorbeeld-7`
[^3]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_geval-2-de-vennootschap-a-en-de-vennootschap-b-hebben-geen-o_2`
