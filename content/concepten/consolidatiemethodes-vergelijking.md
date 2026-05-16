---
title: De vier consolidatiemethodes vergeleken
tags:
- concept
- synthese
- po-1-4
linked_anchors:
- 1.4.I.C
- 1.4.I.D
- 1.4.I.E
- 1.4.I.G
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: inferred
node_type: synthese
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/consolidatiemethodes-vergelijking.json
gegenereerd_op: '2026-05-16'
---
# De vier consolidatiemethodes vergeleken 🤖


Voor één en hetzelfde fenomeen — een groep van vennootschappen — bestaan vier consolidatiemethodes. Welke je toepast hangt af van het soort relatie tussen moeder en dochter (exclusieve controle, gezamenlijke controle, invloed van betekenis, of horizontale groep zonder moeder). Dit synthese-record toont de vier methodes naast elkaar en geeft een beslisboom.

## Vergelijkingstabel

| Methode | Voorwaarde | Op balans | Belangen van derden | Consolidatieverschil |
|---|---|---|---|---|
| [[integrale-consolidatie\|Integrale consolidatie]] | Exclusieve controle (> 50% stemrechten of controle in feite) | Activa/passiva voor 100% opgenomen | Apart op passiefzijde | Wel mogelijk |
| [[evenredige-consolidatie\|Evenredige consolidatie]] | Gezamenlijke controle (overeenkomst tussen vennoten) | Activa/passiva pro-rata opgenomen | Niet apart (zit niet in de cijfers) | Wel mogelijk |
| [[vermogensmutatiemethode\|Vermogensmutatiemethode]] | Invloed van betekenis (≥ 20% stemrechten) of uitgesloten dochter | Eén balanspost: 'Vennootschappen waarop vermogensmutatie is toegepast' | Niet van toepassing | Wel mogelijk |
| [[horizontale-consolidatie\|Horizontale consolidatie (consortium)]] | Horizontale groep zonder moeder; centrale leiding (kan natuurlijke persoon zijn) | Activa/passiva voor 100% per consortium-lid, eigen-vermogensposten behouden hun karakter | Per consortium-lid | Wel mogelijk |

## Beslisboom

```mermaid
flowchart TD
  A[Welk type relatie tussen moeder en dochter?] --> B{Is er een echte moeder<br/>die de andere(n) controleert?}
  B -->|Nee — alle leden onder<br/>gemeenschappelijke leiding| C[Horizontale consolidatie<br/>consortium-leden samen]
  B -->|Ja, één moeder| D{Welk niveau van controle?}
  D -->|Exclusieve controle<br/>meer dan 50% stemrechten| E[Integrale consolidatie]
  D -->|Gezamenlijke controle<br/>vennoten-overeenkomst| F[Evenredige consolidatie]
  D -->|Invloed van betekenis<br/>vanaf 20% stemrechten<br/>geen controle| G[Vermogensmutatiemethode]
  D -->|Geen invloed| H[Niet in consolidatiekring<br/>gewone deelneming op balans]
  style C fill:#ffeaa7
  style E fill:#74b9ff
  style F fill:#74b9ff
  style G fill:#74b9ff
  style H fill:#dfe6e9
```

## Kerninzichten

- Controle (in rechte of feite) bepaalt eerst of er een groep is. Pas daarna kies je de methode op basis van controle-niveau. 🤖
  - _Rationale_: De wettelijke architectuur begint bij de controle-vraag (WVV art. 1:14). Methode-keuze is een afgeleide stap.
- Het ENIGE verschil tussen integrale en evenredige consolidatie is of je activa/passiva volledig opneemt (en het derden-deel apart presenteert) of pro-rata (zonder afzonderlijke derden-post). 🤖
  - _Rationale_: Beide methodes produceren een uitgewerkte balans en resultatenrekening; vermogensmutatie reduceert de dochter tot één balanspost.
- Horizontale consolidatie is de buitenbeentje: er is geen moeder, er zijn alleen consortium-leden die door een gemeenschappelijke leiding samen opereren. Een natuurlijke persoon (bv. Pieter Vermeulen) kan die leiding zijn. 🤖
  - _Rationale_: WVV art. 3:24 voorziet expliciet in consortium-consolidatie wanneer de centrale leiding geen vennootschap is.

## Verwante competenties

- [[competenties/kiezen-consolidatiemethode]]
- [[competenties/kwalificeren-relatie-deelneming]]
- [[competenties/afbakenen-consolidatiekring]]

## Bronnen

[^1]: `KB-WVV-2019__art_3_123`
[^2]: `KB-WVV-2019__art_3_124`
[^3]: `KB-WVV-2019__art_3_141`
[^4]: `WVV__art_3_24`
[^5]: `WVV__art_1_14`
[^6]: `WVV__art_1_22`
