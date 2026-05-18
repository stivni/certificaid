---
title: 'Vennootschapsgrootte-cascade: micro &mdash; klein &mdash; groot'
tags:
- concept
- synthese
- po-1-2
linked_anchors:
- 1.2.IV.B
- 1.2.IV.C
- 1.2.IV.D
- 1.2.IV.E
- 1.2.IV.F
- 1.2.IV
programmaonderdelen:
- '1.2'
confidence: inferred
node_type: synthese
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/vennootschapsgrootte-cascade.json
gegenereerd_op: '2026-05-18'
---
# Vennootschapsgrootte-cascade: micro &mdash; klein &mdash; groot 🤖


De Belgische wetgever koppelt de jaarrekeningverplichtingen aan de omvang van de vennootschap volgens drie groottecategorieën: micro, klein en groot. De drempels uit WVV art. 1:24 en 1:25 (personeelsbezetting, jaaromzet, balanstotaal) bepalen niet alleen welk schema gebruikt mag worden, maar cascaderen door naar zes andere verplichtingen: jaarverslag, commissaris, sociale balans, openbaarmaking, audit-comité, en CSRD-rapportering. Eén klassering = zes gevolgen. Dit synthese-record toont de cascade in één tabel en geeft de beslisboom om snel van cijfers naar verplichtingen te gaan.

## Vergelijkingstabel

| Aspect | [[microvennootschap\|Micro]] | [[kleine-vennootschap\|Klein]] | Groot |
|---|---|---|---|
| Drempels (max 1 overschrijden) | ≤ 10 VTE · ≤ € 900.000 omzet · ≤ € 450.000 balans | ≤ 50 VTE · ≤ € 11.250.000 omzet · ≤ € 6.000.000 balans | Boven de kleine-drempels (2 of 3 overschreden) |
| Extra voorwaarde | Mag geen moeder of dochter zijn | Verbondenheid telt op geconsolideerde basis | &mdash; |
| [[jaarrekening-schema\|Schema]] | Microschema (Bijlage 3 KB-WVV) | Verkort schema (Bijlage 2) | Volledig schema (Bijlage 1) |
| [[jaarverslag\|Jaarverslag]] | Vrijgesteld | Vrijgesteld | Verplicht (WVV art. 3:32) |
| [[commissaris\|Commissaris]] | Niet verplicht | Niet verplicht (tenzij groep groot is) | Verplicht (WVV art. 3:72) |
| [[sociale-balans\|Sociale balans]] | Vereenvoudigd | Verplicht (WVV art. 3:31) | Verplicht |
| [[openbaarmaking-jaarrekening\|Neerlegging NBB]] | Verplicht binnen 7 maanden na boekjaar | Verplicht binnen 7 maanden na boekjaar | Verplicht binnen 7 maanden na boekjaar |
| CSRD-duurzaamheidsrapportering | Niet van toepassing | Niet van toepassing | Vanaf 2024 voor grote vennootschappen die voldoen aan EU-omvangscriteria |

## Beslisboom

```mermaid
flowchart TD
  A[Cliënt-vennootschap &mdash; welke verplichtingen?] --> B[Verzamel 3 cijfers van afgesloten boekjaar:<br/>VTE &mdash; omzet excl. BTW &mdash; balanstotaal]
  B --> C{Behoort vennootschap tot groep?}
  C -->|Ja| D[Tel op geconsolideerde basis<br/>verbondenheid trekt cijfers op]
  C -->|Nee| E[Gebruik enkelvoudige cijfers]
  D --> F{Boven kleine-drempel<br/>op meer dan 1 criterium?}
  E --> F
  F -->|Ja| G[Groot: volledig schema<br/>jaarverslag + commissaris + sociale balans]
  F -->|Nee &mdash; max 1 criterium boven| H{Onder microdrempels<br/>op meer dan 1 criterium?}
  H -->|Ja én geen moeder/dochter| I[Micro: microschema<br/>geen jaarverslag<br/>geen commissaris]
  H -->|Ja maar moeder of dochter| J[Klein: verkort schema<br/>geen jaarverslag<br/>geen commissaris tenzij groep groot]
  H -->|Nee| J
  G --> K{Beursgenoteerd<br/>of grote PIE?}
  K -->|Ja| L[Bijkomend: CSRD-duurzaamheidsrapport<br/>via [[fsma\|FSMA]] toezicht]
  K -->|Nee| M[Enkel WVV-verplichtingen<br/>via [[nationale-bank-belgie\|NBB]] neerlegging]
  style I fill:#a8e6cf
  style J fill:#ffeaa7
  style G fill:#fdcb6e
  style L fill:#ff7675
  style M fill:#dfe6e9
```

## Kerninzichten

- Eén grootteklassering = zes parallelle verplichtingen. Stagiairs maken vaak de fout schema te kiezen en de cascade te vergeten. Voor Meubelzaak Mertens BV (klein) volgt uit de classering: verkort schema + geen jaarverslag + geen commissaris + verplichte sociale balans + neerlegging NBB binnen 7 maand. Vergeet je commissaris-vrijstelling, dan misbillijk je de cliënt met onnodige kosten. 🤖
  - _Rationale_: Cascade volgt uit WVV-art. 3:6, 3:32, 3:72 en KB-WVV-bijlagen 1-3.
- Microvennootschap heeft een extra voorwaarde die klein-vennootschap niet heeft: GEEN moeder of dochter zijn. Oprichtingen Oostende BV (omzet € 400K, 4 VTE) is micro &mdash; maar als ze morgen 60% van Industria Antwerpen NV verwerft, kantelt ze automatisch naar klein. De groottecascade is dynamisch. ⚖️
  - _Rationale_: WVV art. 1:25 § 2 sluit groepsstructuur expliciet uit voor microstatus.
- Twee opeenvolgende boekjaren-regel beschermt tegen heen-en-weer-schommelen. Eénmalige overschrijding kantelt status niet. Bij Brugse Brouwerij BV met uitschieter omzet in 2024: pas vanaf 2026 kantelen als 2025 ook overschrijdt. Examenvraag-camouflage: 'in 2024 had vennootschap X 55 VTE, dus is ze groot' &mdash; mis, je moet 2023 erbij hebben. ⚖️
  - _Rationale_: WVV art. 1:24 § 4 lock-in-regel.
- Kleine groep beïnvloedt kleine vennootschap. Een kleine dochter van een grote groep wordt voor jaarrekening behandeld als groot (consolidatie-perspectief: WVV art. 1:24 § 5). Aurelia Holding NV (klein op zich) met 4 dochters die samen 60 VTE en € 18M omzet hebben &mdash; wordt voor jaarrekening grote vennootschap. Dit is de meest gemiste examen-valkuil. ⚖️
  - _Rationale_: CBN-advies 2017/10 + WVV art. 1:24 § 5.
- Onderscheid [[groottecriteria-jaarrekening\|groottecriteria-jaarrekening]] (WVV art. 1:24-1:25) en [[groottecriteria-consolidatie\|groottecriteria-consolidatie]] (WVV art. 1:26). Eerste bepaalt schema en cascade-verplichtingen van enkelvoudige jaarrekening. Tweede bepaalt vrijstelling consolidatieplicht. Andere drempels, ander doel &mdash; verwar nooit. ⚖️
  - _Rationale_: WVV-architectuur scheidt expliciet beide regimes.

## Verwante competenties

- [[competenties/klasseren-vennootschap-naar-grootte]]
- [[competenties/bepalen-schema-jaarrekening]]
- [[competenties/afleiden-cascade-verplichtingen-uit-grootte]]

## Bronnen

[^1]: `anchor-1.2.IV.B`
[^2]: `CBN-2022-03-beoordeling-van-de-groottecriteria-overeenkomstig-artikelen-124-en-125-van-het-wetboek-van__sec_definitie-van-kleine-vennootschappen-en-microvennootschappen`
[^3]: `KB-WVV-2019__art_3_82`
[^4]: `KB-WVV-2019__art_3_104`
[^5]: `CBN-2017-10-groottecriteria-artikel-15-w-venn-verbonden__sec_algemeen`
