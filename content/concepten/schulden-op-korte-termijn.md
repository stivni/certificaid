---
title: "Schulden op korte termijn"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.1.II.K
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/schulden-op-korte-termijn.json"
---

_Balanspost_ · ook: vlottende schulden · korte-termijn-schulden · klasse 42-49

## Definitie

**Schulden op korte termijn** (kt-schulden) zijn passief-posten met een **restlooptijd van maximaal één jaar** vanaf balansdatum. Ze omvatten **MAR-klassen 42 tot en met 48** en bevatten alle financiële, commerciële, sociale, fiscale en overige verplichtingen die binnen 12 maanden moeten worden afgewikkeld. Een belangrijk type is **rekening 42 — Schulden op meer dan een jaar die binnen het jaar vervallen**: hier wordt het deel van een langetermijn-lening overgeboekt dat binnen de komende 12 maanden moet worden afgelost. Schulden op korte termijn vormen samen met de overlopende rekeningen passief (klasse 89) de **vlottende passiva** — een belangrijke component voor de liquiditeitsanalyse.

<small>📖 KB 21-10-2018 — Bijlage 1 MAR — Klasse 4 (42-48) — _kb_</small>

## Substantie

**MAR-klassen 42-48 — Schulden op ten hoogste één jaar**:
- **42** Schulden op meer dan een jaar die binnen het jaar vervallen (overheveling vanuit 17)
- **43** Financiële schulden (kredietinstellingen kortlopend, kasgeld-krediet, overige leningen ≤ 1 jaar)
- **44** Handelsschulden (440 Leveranciers, 441 Te ontvangen facturen)
- **45** Schulden m.b.t. belastingen, bezoldigingen, sociale lasten
  - 450-454 BTW, bedrijfsvoorheffing, vennootschapsbelasting, onroerende voorheffing
  - 455 Bezoldigingen
  - 456 Sociale lasten — RSZ-werkgever + werknemer
  - 459 Andere sociale schulden
- **46** Ontvangen vooruitbetalingen op bestellingen (klant-voorschotten)
- **47** Schulden uit aanwending van bestemde fondsen
- **48** Diverse schulden

**Boeking aankoop op rekening van leverancier**:
```
604 Aankopen goederen           D 10.000
   440 Leveranciers              C 10.000 (incl. btw via 411 vorderingen op btw)
```

**Bij betaling**:
```
440 Leveranciers                D 10.000
   55 Bank                       C 10.000
```

<small>📖 KB 21-10-2018 — MAR — Klasse 4 — _kb_</small>

## Rationale

Het onderscheid tussen **korte-** en **langetermijn-schulden** dient de **liquiditeitsanalyse**: een lezer van de balans moet onmiddellijk kunnen vaststellen welke verplichtingen op korte termijn moeten worden gehonoreerd. Belangrijke ratio's zoals **current ratio** (vlottende activa / korte-termijn-schulden), **quick ratio** ((vlottende activa - voorraden) / kt-schulden) en **werkkapitaal** (vlottende activa - kt-schulden) bouwen rechtstreeks op deze classificatie. Vandaar de **expliciete overheveling** via klasse 42: een lening die initieel 5 jaar liep maar nog 8 maanden te gaan heeft op balansdatum, moet als kt-schuld worden gepresenteerd — niet meer als lt-schuld.

<small>🔗 KB 29-04-2019 WVV — Bijlagen balansschema's — _kb_</small>

## Bouwstenen

### ⚙️ Overheveling LT-aflossing naar klasse 42

**Scenario**: Banklening van 200.000 EUR met 10-jarige terugbetaling, jaarlijkse aflossing 20.000 EUR. Beginbalans: 200.000 EUR op klasse 17.

**Bij jaarafsluit** (eindejaar 1) — de 20.000 EUR die in jaar 2 vervalt moet naar klasse 42:
```
173 Schulden op meer dan een jaar (afname)    D 20.000
   42 Schulden op meer dan een jaar die binnen het jaar vervallen  C 20.000
```

**Aflossing tijdens jaar 2**:
```
42                                D 20.000
   55 Bank                         C 20.000
```

Bij **elke** jaarafsluit wordt deze overheveling **opnieuw** uitgevoerd voor de volgende 20.000 EUR aflossing van klasse 17 naar klasse 42.

<small>📖 KB 29-04-2019 WVV — Balansschema's bijlage — _kb_</small>

### ⚙️ Sociale schulden — RSZ + bedrijfsvoorheffing

**Maandloon brut 5.000 EUR** voor een werknemer (vereenvoudigd):
- RSZ-werknemer (13,07 %) = 653,50 EUR
- Belastbaar = 4.346,50 EUR
- Bedrijfsvoorheffing (geschat 25 %) = ca. 1.086 EUR
- Nettoloon = 3.260,50 EUR
- RSZ-werkgever (ca. 25 %) = 1.250 EUR

**Boeking maandloon**:
```
620 Bezoldigingen                    D 5.000   (bruto)
621 RSZ-werkgever (sociale lasten)   D 1.250
   455 Bezoldigingen te betalen      C 3.260,50
   453 Bedrijfsvoorheffing           C 1.086
   456 Sociale lasten — RSZ          C 1.903,50 (werknemer + werkgever)
```

De **455, 453, 456** zijn dus passief-posten op kt-schulden die binnen 1-3 maanden moeten worden afgewikkeld bij RSZ en fiscus.

<small>🔗 KB 21-10-2018 — MAR — Klasse 45 — _kb_</small>

## Valkuilen

> [!warning]- Klasse 17 niet splitsen op balansdatum
> **Verkeerde assumptie**: Een 10-jarige lening blijft volledig op klasse 17 tot ze afbetaald is.
>
> **Kernpunt**: Bij elke jaarafsluit moet het **deel van de lening dat binnen de 12 maanden vervalt** overgeheveld worden naar klasse 42. Anders is de balans-classificatie LT/KT verkeerd, en zijn de liquiditeitsratio's geflatteerd (current ratio te hoog).
>
> <small>📖 KB 29-04-2019 WVV — Balansschema's — _kb_</small>

> [!warning]- Vooruitbetalingen klanten als omzet boeken
> **Verkeerde assumptie**: Een klant betaalt vooraf 30 % van een bestelling — dat is omzet voor de vennootschap.
>
> **Kernpunt**: Vooruitbetalingen van klanten zijn een **schuld** (rekening **46 Ontvangen vooruitbetalingen op bestellingen**) — geen omzet. De omzet wordt pas erkend wanneer de prestatieverplichting (levering of dienst) is vervuld. Dit is een veel voorkomende **revenue-recognition-fout**, vooral bij bouw, IT-projecten en abonnementen.
>
> <small>📖 KB 21-10-2018 — MAR — Klasse 46 — _kb_</small>

## Verder lezen (scope-out)

- → Schulden op meer dan een jaar (primair schuldfinanciering) _(moet-verwijzen)_
- → Overlopende rekeningen passief → [[overlopende-rekeningen]] _(moet-verwijzen)_
- ↪ Loon-en-payroll (sociale schulden-context) → [[loon-en-payroll]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[boekhouding]]
