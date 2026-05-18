---
title: Moet ik consolideren? — Beslisboom
tags:
- concept
- synthese
- po-1-4
linked_anchors:
- 1.4.I.B
- 1.4.I.G
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: inferred
node_type: synthese
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/consolidatieplicht-beslisboom.json
gegenereerd_op: '2026-05-18'
---
# Moet ik consolideren? — Beslisboom 🤖


De vraag 'moet mijn cliënt een geconsolideerde jaarrekening opmaken' wordt nooit door één criterium beantwoord. Vijf elementen werken samen: bestaat er controle? heeft de moeder rechtspersoonlijkheid? overschrijdt de groep de groottecriteria? geldt er een vrijstelling? is de groep een consortium? Dit synthese-record volgt de wettelijke beslissingsvolgorde en koppelt elke vraag aan het concept-record dat het beantwoordt.

## Vergelijkingstabel

| Stap | Toets | Welk concept? | Bij 'ja' | Bij 'nee' |
|---|---|---|---|---|
| 1 | Is de moeder een vennootschap met rechtspersoonlijkheid? | [[moedervennootschap]] | Door naar stap 2 | Geen consolidatieplicht (natuurlijke persoon → eventueel consortium-piste) |
| 2 | Bestaat er controle (in rechte of in feite) over één of meer dochters? | [[controle]] | Door naar stap 3 | Geen consolidatieplicht |
| 3 | Of: zijn er meerdere vennootschappen onder centrale leiding zonder onderlinge moeder-dochter? | [[consortium]] | Consortium-consolidatie (horizontaal), door naar stap 4 | Verticale groep, door naar stap 4 |
| 4 | Overschrijdt de groep meer dan één van de groottecriteria op geconsolideerde basis? | [[groottecriteria-consolidatie]] · [[groep-van-beperkte-omvang]] | Door naar stap 5 | Vrijstelling 'groep van beperkte omvang' — geen consolidatieplicht (tenzij beursgenoteerd) |
| 5 | Wordt de moeder zelf al opgenomen in een gelijkwaardige geconsolideerde jaarrekening hogerop in de EU (≥ 90 % deelneming)? | [[vrijstelling-subconsolidatie]] | Vrijstelling subconsolidatie — moeder consolideert niet zelf, tenzij dochter beursgenoteerd | **Consolideren** — moeder maakt geconsolideerde jaarrekening op |

## Beslisboom

```mermaid
flowchart TD
  A[Aurelia Holding NV — moet zij consolideren?] --> B{Rechtspersoonlijkheid?}
  B -->|Nee — natuurlijke persoon Pieter Vermeulen| C{Onder centrale leiding<br/>met andere vennootschappen?}
  C -->|Ja| D[Consortium-consolidatie<br/>Industria Antwerpen NV + Jachthaven Jezus-Eik NV samen]
  C -->|Nee| E[Geen consolidatieplicht]
  B -->|Ja| F{Controle over één of meer<br/>dochterondernemingen?}
  F -->|Nee — alleen deelneming<br/>20-50 stemrechten| G[Geen consolidatieplicht<br/>vermogensmutatie op enkelvoudige jaarrekening]
  F -->|Ja — exclusief of gezamenlijk| H{Overschrijdt groep<br/>twee van drie groottecriteria<br/>op geconsolideerde basis?}
  H -->|Nee — Gent Garantie BV als kleine groep| I[Vrijstelling<br/>groep van beperkte omvang<br/>tenzij beursgenoteerd]
  H -->|Ja| J{Hogere moeder<br/>consolideert al EU-breed<br/>≥ 90% deelneming?}
  J -->|Ja — Kappers Köln GmbH consolideert| K[Vrijstelling subconsolidatie<br/>tenzij dochter beursgenoteerd]
  J -->|Nee| L[**Consolideren**<br/>moeder maakt geconsolideerde jaarrekening op]
  style D fill:#ffeaa7
  style E fill:#dfe6e9
  style G fill:#dfe6e9
  style I fill:#a8e6cf
  style K fill:#a8e6cf
  style L fill:#74b9ff
```

## Kerninzichten

- Geen enkele moeder is automatisch consolidatieplichtig — er zijn altijd vijf parallelle toetsen die elk een 'nee' kunnen geven. Een examenvraag die zegt 'moeder X heeft controle over dochter Y, dus moet zij consolideren' kapt de redenering te vroeg af. 🤖
  - _Rationale_: De wettelijke architectuur (WVV art. 3:22-3:24 + art. 1:26) bouwt de plicht op uit cumulatieve voorwaarden + uitzonderingen.
- Een natuurlijke persoon kan nooit moeder zijn (geen rechtspersoonlijkheid), maar haar gecontroleerde vennootschappen kunnen samen wel een consortium vormen. De plicht verschuift dan van één entiteit naar 'de leden samen'. 🤖
  - _Rationale_: Consortium-figuur in WVV art. 3:24 lost juist deze situatie op.
- De groottecriteria zijn 'op geconsolideerde basis' — je moet dus een fictieve geconsolideerde balans opbouwen om te beslissen of je een echte moet maken. Dat is geen circulariteit maar een toetscriterium. 🤖
  - _Rationale_: Veelvoorkomende stagiair-verwarring: 'maar ik kan geen geconsolideerde balans maken zonder geconsolideerd te hebben' — antwoord: het is een aggregatie-oefening, niet een formele consolidatie.
- Beursnotering breekt zowel de 'groep van beperkte omvang'-vrijstelling als de subconsolidatie-vrijstelling. Voor genoteerde vennootschappen geldt: altijd consolideren, drempels of hogere moeder doen er niet toe. ⚖️
  - _Rationale_: WVV art. 1:26 §3 + KB WVV-specifieke bepalingen.

## Verwante competenties

- [[competenties/bepalen-consolidatieverplichting]]
- [[competenties/afbakenen-consolidatiekring]]

## Bronnen

[^1]: `WVV__art_3_22`
[^2]: `WVV__art_3_24`
[^3]: `WVV__art_1_26`
[^4]: `KB-WVV-2019__art_3_96`
