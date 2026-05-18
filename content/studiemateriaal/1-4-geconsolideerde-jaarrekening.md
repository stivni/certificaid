---
title: 1.4 Geconsolideerde jaarrekening en wetgeving betreffende de geconsolideerde
  jaarrekening
tags:
- minicursus
- po-1-4
programmaonderdeel: '1.4'
gerelateerde_concepten:
- afbakenen-consolidatiekring
- belangenpercentage
- bepalen-consolidatieverplichting
- berekenen-controle-en-belangenpercentage
- consolidatiekring
- consolidatiemethodes-vergelijking
- consolidatieplicht-beslisboom
- consolidatieverplichting
- consolidatieverschil
- consortium
- controle
- controlepercentage
- dochteronderneming
- eerste-consolidatie
- evenredige-consolidatie
- exclusieve-controle
- geassocieerde-onderneming
- geconsolideerd-jaarverslag
- geconsolideerde-jaarrekening
- gemeenschappelijke-dochteronderneming
- gezamenlijke-controle
- groep-van-beperkte-omvang
- groottecriteria-consolidatie
- horizontale-consolidatie
- ifrs-consolidatieraamwerk
- integrale-consolidatie
- intragroep-eliminaties
- invloed-van-betekenis
- kiezen-consolidatiemethode
- kwalificeren-relatie-deelneming
- minderheidsbelangen
- moedervennootschap
- step-acquisition
- toepassen-uniforme-waarderingsregels
- uitvoeren-eerste-consolidatie
- uitvoeren-intragroep-eliminaties
- uniforme-waarderingsregels-consolidatie
- vermogensmutatiemethode
- verwerken-wijziging-consolidatiekring
- vrijstelling-subconsolidatie
- wijziging-consolidatiekring
gegenereerd_op: '2026-05-18'
---
> [!warning]- Open beslissingen
> De volgende gaps zijn nog open voor dit programmaonderdeel — inhoud kan onvolledig zijn:
> - `edges.target-ontbreekt` op `consolidatieverplichting`: Drie edges van type 'contrasteert-met' zijn gedeprecieerd (niet toegelaten in schema 1.4+). Targets:…

## Wat verwacht het examen van jou?

> [!abstract] Dit programmaonderdeel wordt getoetst op niveau *toepassen*.
> Je moet deze regels en begrippen kunnen toepassen op een nieuwe casus — herkennen welk concept geldt en de stappen correct uitvoeren.


**Taken** (uit het ITAA-examenprogramma):

- **1.4.taak.1** — Opstellen van de individuele en geconsolideerde jaarrekening *(7 doelstellingen)*

## Leesgids

<!-- TODO: Opus-glue leesgids -->

## Waarom dit programmaonderdeel telt

<!-- TODO: Opus-glue waarom_po -->

## Wat is consolideren? Waarom een geconsolideerde jaarrekening?

<!-- TODO: Opus-glue oriëntatie -->

## Moet ik consolideren? — Beslisboom

<!-- TODO: Opus-glue synthese-intro -->

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

**Kerninzichten**:
- Geen enkele moeder is automatisch consolidatieplichtig — er zijn altijd vijf parallelle toetsen die elk een 'nee' kunnen geven. Een examenvraag die zegt 'moeder X heeft controle over dochter Y, dus moet zij consolideren' kapt de redenering te vroeg af.
- Een natuurlijke persoon kan nooit moeder zijn (geen rechtspersoonlijkheid), maar haar gecontroleerde vennootschappen kunnen samen wel een consortium vormen. De plicht verschuift dan van één entiteit naar 'de leden samen'.
- De groottecriteria zijn 'op geconsolideerde basis' — je moet dus een fictieve geconsolideerde balans opbouwen om te beslissen of je een echte moet maken. Dat is geen circulariteit maar een toetscriterium.
- Beursnotering breekt zowel de 'groep van beperkte omvang'-vrijstelling als de subconsolidatie-vrijstelling. Voor genoteerde vennootschappen geldt: altijd consolideren, drempels of hogere moeder doen er niet toe.

[[consolidatieplicht-beslisboom|→ Volledige synthese-fiche]]

## Het fundamentele begrippenkader: controle en de actoren in een groep

> [!info] Hoort bij taak: **1.4.taak.1** (Opstellen van de individuele en geconsolideerde jaarrekening)

<!-- TODO: Opus-glue thematisch-intro -->

- [[controle|Controle]] · `begrip`
- [[moedervennootschap|Moedervennootschap]] · `autoriteit`
- [[dochteronderneming|Dochteronderneming]] · `autoriteit`
- [[exclusieve-controle|Exclusieve controle]] · `begrip`
- [[gezamenlijke-controle|Gezamenlijke controle]] · `begrip`
- [[invloed-van-betekenis|Invloed van betekenis]] · `begrip`
- [[geassocieerde-onderneming|Geassocieerde onderneming]] · `autoriteit`
- [[gemeenschappelijke-dochteronderneming|Gemeenschappelijke dochteronderneming]] · `autoriteit`
- [[consortium|Consortium (horizontale groep)]] · `autoriteit`

## Bepalen of een vennootschap een geconsolideerde jaarrekening moet opstellen

> [!info] Hoort bij taak: **1.4.taak.1** (Opstellen van de individuele en geconsolideerde jaarrekening)

<!-- TODO: Opus-glue competentie-intro -->

[[competenties/bepalen-consolidatieverplichting|→ Volledige procedure]]

## Afbakenen van de consolidatiekring en beoordelen van uitsluitings- of weglatingsgronden

> [!info] Hoort bij taak: **1.4.taak.1** (Opstellen van de individuele en geconsolideerde jaarrekening)

<!-- TODO: Opus-glue competentie-intro -->

[[competenties/afbakenen-consolidatiekring|→ Volledige procedure]]

## Kwalificeren van de relatie met een deelneming (controle, gezamenlijke controle of invloed van betekenis)

> [!info] Hoort bij taak: **1.4.taak.1** (Opstellen van de individuele en geconsolideerde jaarrekening)

<!-- TODO: Opus-glue competentie-intro -->

[[competenties/kwalificeren-relatie-deelneming|→ Volledige procedure]]

## Berekenen van controle- en belangenpercentage in een ketenstructuur

> [!info] Hoort bij taak: **1.4.taak.1** (Opstellen van de individuele en geconsolideerde jaarrekening)

<!-- TODO: Opus-glue competentie-intro -->

[[competenties/berekenen-controle-en-belangenpercentage|→ Volledige procedure]]

## De drie consolidatiemethoden: integrale, evenredige en vermogensmutatie

> [!info] Hoort bij taak: **1.4.taak.1** (Opstellen van de individuele en geconsolideerde jaarrekening)

<!-- TODO: Opus-glue thematisch-intro -->

- [[integrale-consolidatie|Integrale consolidatie]] · `cluster`
- [[evenredige-consolidatie|Evenredige consolidatie (proportionele consolidatie)]] · `cluster`
- [[vermogensmutatiemethode|Vermogensmutatiemethode (equity method)]] · `cluster`
- [[horizontale-consolidatie|Horizontale consolidatie]] · `procedure`

## De vier consolidatiemethodes vergeleken

<!-- TODO: Opus-glue synthese-intro -->

```mermaid
flowchart TD
  A[Welk type relatie tussen moeder en dochter?] --> B{Is er een echte moeder<br/>die de dochters controleert?}
  B -->|Nee &mdash; alle leden onder<br/>gemeenschappelijke leiding| C[Horizontale consolidatie<br/>consortium-leden samen]
  B -->|Ja &mdash; één moeder| D{Welk niveau van controle?}
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

**Kerninzichten**:
- Controle (in rechte of feite) bepaalt eerst of er een groep is. Pas daarna kies je de methode op basis van controle-niveau.
- Het ENIGE verschil tussen integrale en evenredige consolidatie is of je activa/passiva volledig opneemt (en het derden-deel apart presenteert) of pro-rata (zonder afzonderlijke derden-post).
- Horizontale consolidatie is de buitenbeentje: er is geen moeder, er zijn alleen consortium-leden die door een gemeenschappelijke leiding samen opereren. Een natuurlijke persoon (bv. Pieter Vermeulen) kan die leiding zijn.

[[consolidatiemethodes-vergelijking|→ Volledige synthese-fiche]]

## Kiezen van de toe te passen consolidatietechniek per entiteit

> [!info] Hoort bij taak: **1.4.taak.1** (Opstellen van de individuele en geconsolideerde jaarrekening)

<!-- TODO: Opus-glue competentie-intro -->

[[competenties/kiezen-consolidatiemethode|→ Volledige procedure]]

## Toepassen van uniforme waarderingsregels en hercorrigeren van enkelvoudige cijfers

> [!info] Hoort bij taak: **1.4.taak.1** (Opstellen van de individuele en geconsolideerde jaarrekening)

<!-- TODO: Opus-glue competentie-intro -->

[[competenties/toepassen-uniforme-waarderingsregels|→ Volledige procedure]]

## Uitvoeren van de eerste consolidatie van een nieuw verworven dochter of geassocieerde onderneming

> [!info] Hoort bij taak: **1.4.taak.1** (Opstellen van de individuele en geconsolideerde jaarrekening)

<!-- TODO: Opus-glue competentie-intro -->

[[competenties/uitvoeren-eerste-consolidatie|→ Volledige procedure]]

## Uitvoeren van intragroep-eliminaties en berekenen van het aandeel van derden

> [!info] Hoort bij taak: **1.4.taak.1** (Opstellen van de individuele en geconsolideerde jaarrekening)

<!-- TODO: Opus-glue competentie-intro -->

[[competenties/uitvoeren-intragroep-eliminaties|→ Volledige procedure]]

## Verwerken van een wijziging in de consolidatiekring (inclusief step acquisition)

> [!info] Hoort bij taak: **1.4.taak.1** (Opstellen van de individuele en geconsolideerde jaarrekening)

<!-- TODO: Opus-glue competentie-intro -->

[[competenties/verwerken-wijziging-consolidatiekring|→ Volledige procedure]]

## Publicatie en rapportering: jaarrekening en jaarverslag

> [!info] Hoort bij taak: **1.4.taak.1** (Opstellen van de individuele en geconsolideerde jaarrekening)

<!-- TODO: Opus-glue thematisch-intro -->

- [[geconsolideerde-jaarrekening|Geconsolideerde jaarrekening]] · `begrip`
- [[geconsolideerd-jaarverslag|Geconsolideerd jaarverslag]] · `begrip`

## IFRS-context: het internationale consolidatieraamwerk

> [!info] Hoort bij taak: **1.4.taak.1** (Opstellen van de individuele en geconsolideerde jaarrekening)

<!-- TODO: Opus-glue thematisch-intro -->

- [[ifrs-consolidatieraamwerk|IFRS-consolidatieraamwerk (IFRS 3 / IFRS 10 / IFRS 11 / IFRS 12)]] · `begrip`


## Synthese-stappenplan

<!-- TODO: Opus-glue synthese -->

## Cheatsheet

### Kritische drempelwaarden

| Concept | Naam | Waarde | Eenheid | Gevolg |
|---|---|---|---|---|
| [[exclusieve-controle]] | Onweerlegbaar vermoeden van controle in rechte | > 50 % | stemrechten | Onweerlegbaar vermoeden van exclusieve controle → moeder → integrale consolidatie van de dochter |
| [[geassocieerde-onderneming]] | Weerlegbaar vermoeden invloed van betekenis (= geassocieerde onderneming) | ≥ 20 % | stemrechten | Vermoeden dat de moeder invloed van betekenis heeft op het beleid → kwalificatie als geassocieerde onderneming → opname… |
| [[geassocieerde-onderneming]] | Bovengrens (overgang naar dochter) | > 50 % stemrechten of andere titel van controle | stemrechten | Vanaf controle (in rechte of in feite) is de onderneming geen geassocieerde meer maar een dochter → integrale consolidat… |
| [[geconsolideerde-jaarrekening]] | Maximale afwijking afsluitingsdatum dochter ↔ geconsolideerde jaarrekening | 3 | maanden | KB WVV art. 3:110, tweede lid: als het uiterst moeilijk is om bezittingen, schulden, rechten, verplichtingen, opbrengste… |
| [[groep-van-beperkte-omvang]] | Drempels groep van beperkte omvang (KB WVV art. 1:26 — geaggregeerde basis +20 %) | Maximaal 1 van 3 drempels overschreden | criteria | Wordt aan deze test voldaan, dan is de moeder vrijgesteld van het opstellen van een geconsolideerde jaarrekening en een… |
| [[groottecriteria-consolidatie]] | Kleine vennootschap (WVV art. 1:24) — referentie | jaaromzet ≤ 11.250.000 EUR; balanstotaal ≤ 6.000.000 EUR; jaargemiddelde werknemers ≤ 50 | criteria-set | Hoogstens één drempel overschreden → kleine vennootschap (verkorte schema's mogelijk) |
| [[groottecriteria-consolidatie]] | Vereenvoudigde berekening op geaggregeerde basis (WVV art. 1:24, § 6) | drempels balanstotaal en omzet vermeerderd met 20 % | %-toeslag | Een moeder die niet wettelijk verplicht is om te consolideren, mag voor de groottetoets alle bedragen van haar verbonden… |
| [[invloed-van-betekenis]] | Weerlegbaar vermoeden van invloed van betekenis | ≥ 20 % | deelnemingspercentage in stemrechten | Weerlegbaar vermoeden van invloed van betekenis → kwalificatie als geassocieerde onderneming → vermogensmutatiemethode i… |
| [[invloed-van-betekenis]] | Bovengrens (overgang naar controle) | > 50 % stemrechten of controle in feite | stemrechten | Boven 50 % stemrechten of bij vastgestelde controle in feite kantelt 'invloed van betekenis' naar 'exclusieve controle' |

### Vergelijkingsparen-matrix

| Concept | Verwarrend met | Trigger |
|---|---|---|
| [[belangenpercentage]] | [[controlepercentage]] | Examen: vraag eerst 'wat moet ik berekenen?' — winstaandeel of aandeel van derden → belangenpercentage; consolidatieverplichting of -methode → controlepercentage. |
| [[controle]] | [[invloed-van-betekenis]] | Bij percentages 20–50 %: standaard vermogensmutatie (invloed van betekenis). Bij overeenkomst voor gezamenlijke uitoefening van beleid: gezamenlijke controle. |
| [[controle]] | [[controlepercentage]] | Wanneer een opgave een percentage geeft: vraag eerst of het over stemrechten (controle) of over kapitaal (belang) gaat. |
| [[dochteronderneming]] | [[geassocieerde-onderneming]] | Stel de controlevraag: heeft de moeder beslissende invloed (eventueel samen met enkele anderen)? Zo ja: dochter. Zo nee maar wel betekenisvolle invloed (typisch 20-50 %): geassocieerde. |
| [[evenredige-consolidatie]] | [[integrale-consolidatie]] | Soort controle bepaalt de methode: exclusieve controle → integraal; gezamenlijke controle → evenredig (of vermogensmutatie als niet-geïntegreerd). |
| [[evenredige-consolidatie]] | [[vermogensmutatiemethode]] | Mate van integratie van de gemeenschappelijke dochter in de groep — nauw geïntegreerd → evenredig; los → vermogensmutatie. |
| [[exclusieve-controle]] | [[gezamenlijke-controle]] | Cruciale vraag in elke opgave: is er een overeenkomst dat beleidsbeslissingen alleen samen mogen worden genomen? Zo ja: gezamenlijke controle; anders: exclusieve controle of geen controle. |
| [[horizontale-consolidatie]] | [[integrale-consolidatie]] | Het type relatie (verticaal vs. horizontaal) bepaalt of je het integrale-consolidatie-recept op een moeder + haar dochters toepast (verticaal) of op een set zelfstandige consortium-leden onder gemeenschappelijke leiding (horizontaal). |
| [[integrale-consolidatie]] | [[evenredige-consolidatie]] | Soort controle / type relatie tussen moeder en dochter bepaalt welke methode. |
| [[integrale-consolidatie]] | [[vermogensmutatiemethode]] | Soort controle / type relatie tussen moeder en dochter bepaalt welke methode. |
| [[vermogensmutatiemethode]] | [[integrale-consolidatie]] | Soort relatie: controle → integraal; invloed van betekenis (of uitgesloten dochters / niet-geïntegreerde gemeenschappelijke dochters) → vermogensmutatie. |
| [[vermogensmutatiemethode]] | [[evenredige-consolidatie]] | Mate van integratie van de gemeenschappelijke dochter: nauw geïntegreerd → evenredig; los → vermogensmutatie. |
| [[vrijstelling-subconsolidatie]] | [[groottecriteria-consolidatie]] | Examen-keuze-vraag: 'Welke vrijstelling beroept Aurelia zich op?' → toets eerst structuur (is er een top-moeder die al consolideert? → subconsolidatie), daarna omvang (zit de groep onder de drempels? → beperkte omvang). |


## Heb je deze taken in de vingers?

Loop deze taken na vóór je verder gaat met examenfocus. Twijfel je bij een taak? Lees de aangegeven secties nog eens.

- ✓ **1.4.taak.1** — Opstellen van de individuele en geconsolideerde jaarrekening _Behandeld in §5, §6, §7, §8, §9, §10, §11, §12, §13, §14, §15, §16, §17, §18, §19._

## Examenfocus

<!-- TODO: Opus-glue examenfocus -->

> [!question]- 2008-bibf-vrB.1 (punten onbekend)
> B.1 In een groep controleert vennootschap A twee dochters B en C.
> Vennootschap B koopt voor 50.000,00 EUR aandelen aan die 12%
> vertegenwoordigen van het stemrecht in C.
> Boek deze aankoop in de onderneming B.
>
> _Thema's: deelneming-verbonden-onderneming, groepsstructuur_

> [!question]- 2008-bibf-vrB.2 (punten onbekend)
> B.2 De hierboven vermelde vennootschap B stelt 5 voltijdse equivalenten tewerk
> en heeft een jaarlijkse omzet van 2.000.000 EUR. De moedervennootschap A
> telt 120 werknemers, berekend in voltijdse equivalenten.
> Welk schema moet / mag de vennootschap A voor haar jaarrekening
> gebruiken?
> Welk schema moet / mag de vennootschap B voor haar jaarrekening
> gebruiken?
>
> _Thema's: jaarrekening-schema, groottecriteria, geconsolideerde-grondslag_

> [!question]- 2013-1-vr3 (3.0 pt)
> Vraag 3 … / 3 punten
> Een onderneming, die een geconsolideerde jaarrekening moet opstellen, vraagt U onder
> welke post in de geconsolideerde resultatenrekening het gedeelte van het resultaat van de
> volledig geconsolideerde dochterondernemingen dat kan worden toegerekend aan aandelen
> die worden gehouden door andere personen dan de consoliderende vennootschap of de in
> de consolidatie opgenomen dochterondernemingen moet worden vermeld.
> Antwoord
>
> _Thema's: consolidatie_

> [!question]- 2013-1-vr4 (3.0 pt)
> Vraag 4 … / 3 punten
> De geconsolideerde jaarrekening wordt in principe op dezelfde datum afgesloten als de
> jaarrekening van de consoliderende vennootschap. In bepaalde gevallen kan men hiervan
> afwijken. Hoeveel bedraagt de maximale afwijking qua afsluitingsdatum ?
> Antwoord
>
> _Thema's: consolidatie_

> [!question]- 2013-2-vr4 (10.0 pt)
> Vraag 4 … / 10 punten
> a) Wat is een positief consolidatieverschil ?
> Antwoord … / 2 punten
> b) Geef de vier voornaamste oorzaken van positieve consolidatieverschillen ?
> Antwoord … / 8 punten
>
> _Thema's: consolidatie_

> [!question]- 2014-1-vr3 (3.0 pt)
> Vraag 3 … / 3 punten
> De geconsolideerde jaarrekening wordt in principe op dezelfde datum afgesloten als de
> jaarrekening van de consoliderende vennootschap. In bepaalde gevallen kan men hiervan
> afwijken.
> Hoeveel bedraagt de maximale afwijking qua afsluitingsdatum ?
> Antwoord
>
> _Thema's: consolidatie_

> [!question]- 2014-1-vr4 (9.0 pt)
> Vraag 4 … / 9 punten
> Vul onderstaande tabel aan op basis van volgende gegevens.
> M
> 70 % 30 %
> 60 % 20 %
> A B C
> Antwoord
> CONTROLEPERCENTAGE BELANGENPERCENTAGE CONSOLIDATIEMETHODE
> M IN A
> M IN B
> M IN C
>
> _Thema's: consolidatie_

> [!question]- 2015-1-vr4 (6.0 pt)
> Vraag 4 … / 6 punten
> a) Wat is een positief consolidatieverschil ?
> Antwoord … / 2 punten
> b) Geef de vier voornaamste oorzaken van positieve consolidatieverschillen ?
> Antwoord … / 4 punten
>
> _Thema's: consolidatie_


## Competentie-index

<div class="two-column-list">

- [[competenties/afbakenen-consolidatiekring|Afbakenen van de consolidatiekring en beoordelen van uitsluitings- of weglatingsgronden]]
- [[competenties/bepalen-consolidatieverplichting|Bepalen of een vennootschap een geconsolideerde jaarrekening moet opstellen]]
- [[competenties/berekenen-controle-en-belangenpercentage|Berekenen van controle- en belangenpercentage in een ketenstructuur]]
- [[competenties/kiezen-consolidatiemethode|Kiezen van de toe te passen consolidatietechniek per entiteit]]
- [[competenties/kwalificeren-relatie-deelneming|Kwalificeren van de relatie met een deelneming (controle, gezamenlijke controle of invloed van betekenis)]]
- [[competenties/toepassen-uniforme-waarderingsregels|Toepassen van uniforme waarderingsregels en hercorrigeren van enkelvoudige cijfers]]
- [[competenties/uitvoeren-eerste-consolidatie|Uitvoeren van de eerste consolidatie van een nieuw verworven dochter of geassocieerde onderneming]]
- [[competenties/uitvoeren-intragroep-eliminaties|Uitvoeren van intragroep-eliminaties en berekenen van het aandeel van derden]]
- [[competenties/verwerken-wijziging-consolidatiekring|Verwerken van een wijziging in de consolidatiekring (inclusief step acquisition)]]

</div>

## Concept-index

<div class="two-column-list">

- [[afbakenen-consolidatiekring|Afbakenen van de consolidatiekring en beoordelen van uitsluitings- of weglatingsgronden]] · `competentie`
- [[minderheidsbelangen|Belangen van derden (minderheidsbelangen)]] · `cluster`
- [[belangenpercentage|Belangenpercentage]] · `begrip`
- [[bepalen-consolidatieverplichting|Bepalen of een vennootschap een geconsolideerde jaarrekening moet opstellen]] · `competentie`
- [[berekenen-controle-en-belangenpercentage|Berekenen van controle- en belangenpercentage in een ketenstructuur]] · `competentie`
- [[consolidatiekring|Consolidatiekring]] · `begrip`
- [[consolidatieverplichting|Consolidatieverplichting]] · `regel`
- [[consolidatieverschil|Consolidatieverschil]] · `cluster`
- [[consortium|Consortium (horizontale groep)]] · `autoriteit`
- [[controle|Controle]] · `begrip`
- [[controlepercentage|Controlepercentage]] · `begrip`
- [[consolidatiemethodes-vergelijking|De vier consolidatiemethodes vergeleken]] · `synthese`
- [[dochteronderneming|Dochteronderneming]] · `autoriteit`
- [[eerste-consolidatie|Eerste consolidatie]] · `cluster`
- [[evenredige-consolidatie|Evenredige consolidatie (proportionele consolidatie)]] · `cluster`
- [[exclusieve-controle|Exclusieve controle]] · `begrip`
- [[geassocieerde-onderneming|Geassocieerde onderneming]] · `autoriteit`
- [[geconsolideerd-jaarverslag|Geconsolideerd jaarverslag]] · `begrip`
- [[geconsolideerde-jaarrekening|Geconsolideerde jaarrekening]] · `begrip`
- [[gemeenschappelijke-dochteronderneming|Gemeenschappelijke dochteronderneming]] · `autoriteit`
- [[gezamenlijke-controle|Gezamenlijke controle]] · `begrip`
- [[groep-van-beperkte-omvang|Groep van beperkte omvang]] · `begrip`
- [[groottecriteria-consolidatie|Groottecriteria voor de consolidatievrijstelling]] · `regel`
- [[horizontale-consolidatie|Horizontale consolidatie]] · `procedure`
- [[ifrs-consolidatieraamwerk|IFRS-consolidatieraamwerk (IFRS 3 / IFRS 10 / IFRS 11 / IFRS 12)]] · `begrip`
- [[integrale-consolidatie|Integrale consolidatie]] · `cluster`
- [[intragroep-eliminaties|Intragroep-eliminaties]] · `procedure`
- [[invloed-van-betekenis|Invloed van betekenis]] · `begrip`
- [[kiezen-consolidatiemethode|Kiezen van de toe te passen consolidatietechniek per entiteit]] · `competentie`
- [[kwalificeren-relatie-deelneming|Kwalificeren van de relatie met een deelneming (controle, gezamenlijke controle of invloed van betekenis)]] · `competentie`
- [[moedervennootschap|Moedervennootschap]] · `autoriteit`
- [[consolidatieplicht-beslisboom|Moet ik consolideren? — Beslisboom]] · `synthese`
- [[step-acquisition|Step acquisition (trapsgewijze verwerving)]] · `cluster`
- [[toepassen-uniforme-waarderingsregels|Toepassen van uniforme waarderingsregels en hercorrigeren van enkelvoudige cijfers]] · `competentie`
- [[uitvoeren-eerste-consolidatie|Uitvoeren van de eerste consolidatie van een nieuw verworven dochter of geassocieerde onderneming]] · `competentie`
- [[uitvoeren-intragroep-eliminaties|Uitvoeren van intragroep-eliminaties en berekenen van het aandeel van derden]] · `competentie`
- [[uniforme-waarderingsregels-consolidatie|Uniforme waarderingsregels in de consolidatie]] · `regel`
- [[vermogensmutatiemethode|Vermogensmutatiemethode (equity method)]] · `cluster`
- [[verwerken-wijziging-consolidatiekring|Verwerken van een wijziging in de consolidatiekring (inclusief step acquisition)]] · `competentie`
- [[vrijstelling-subconsolidatie|Vrijstelling van subconsolidatie]] · `regel`
- [[wijziging-consolidatiekring|Wijziging van de consolidatiekring]] · `cluster`

</div>
