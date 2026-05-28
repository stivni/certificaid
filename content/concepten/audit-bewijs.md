---
title: "Audit-bewijs"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.6.III
  - 1.6.III.A
  - 1.6.III.B
  - 1.6.III.C
  - 1.6.III.D
  - 1.6.III.E
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/audit-bewijs.json"
---

# Audit-bewijs

_Procedure_

🏛️ Kader · Anchors: `1.6.III` · `1.6.III.A` · `1.6.III.B` · `1.6.III.C` · `1.6.III.D` · `1.6.III.E` · Wave: `skeleton-controle-beroep-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: controle-informatie · audit evidence · controlebewijs · audit procedures · audit techniques — **Vertalingen**: fr: éléments probants · en: audit evidence

## Definitie

📖 Audit-bewijs (controle-informatie) is alle informatie waarop de auditor zich baseert om tot conclusies te komen die zijn oordeel onderbouwen. Bron-types: financiële administratie van de entiteit zelf én bronnen van buiten (externe bevestigingen, fysieke observatie, externe deskundigen). Twee kwaliteitseisen die ISA 500 oplegt: **voldoende** (sufficient — voldoende kwantiteit) én **geschikt** (appropriate — relevant en betrouwbaar). Hoe hoger het ingeschatte risico op afwijking van materieel belang, hoe meer of overtuigender het bewijs nodig is.

<small>📚 ISA 500 — Doelstellingen + definities — _norm_ · ISA 530 — par. 2 (steunpunt op ISA 500) — _norm_</small>

## Substantie

🔗 Bewijs is geen verzameling losse documenten maar een **gestructureerde stapel argumenten per assertion**. Voor elke materiële post in de jaarrekening vraagt de auditor: ‘welke beweringen moeten waar zijn opdat dit cijfer correct is, en welke procedure overtuigt mij van elk?’ Voorbeeld: handelsvorderingen 1.250.000 EUR — assertions: (a) bestaan: er bestaan klanten die ons dit verschuldigd zijn (procedure: externe bevestiging, ISA 505); (b) waardering: het bedrag is recupereerbaar (procedure: ouderdomsanalyse + waardevermindering); (c) rechten: wij zijn eigenaar van de vordering (procedure: factuur-leveringsbon-overeenkomst inspectie); (d) cut-off: vorderingen horen tot juiste boekjaar (procedure: cut-off test rond 31/12); (e) presentatie: correcte klassering KT/LT.

De **bewijspiramide** (overtuigingskracht oplopend): inspectie kopieën < inspectie originelen < externe bevestiging < eigen herperformance van controle door auditor.

<small>📚 ISA 315 (herzien 2019) — par. A190 categorieën beweringen — _norm_ · ISA 500 — par. A30 betrouwbaarheid bewijs — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom zo formeel? De auditor geeft een oordeel dat juridisch tegenstelbaar moet zijn — bij latere fraude of insolventie kan een schadeclaim volgen. Zonder bewijs-traceability per cijfer kan hij in een tuchtprocedure of voor een rechtbank niet aantonen dát hij zorgvuldig werkte. Door bewijs gestructureerd per assertion te ordenen, kan een ervaren auditor die niet bij de controle betrokken was (ISA 230 par. 8) achteraf reconstrueren wat gedaan is en waarom. Dat is de bewijslast-architectuur van de hele beroepsgroep.

<small>📚 ISA 230 — par. 8 (ervaren auditor-test) — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: ISA 500-599 (bewijsfamilie) · ISA 315/330 (link met planning) · ITAA-KMO-controlenorm

ISA 540 (herzien 2018, ingangsdatum 15/12/2019) versterkt verwachtingen rond schattingen. ISRS 4400 (herzien 2020) regelt AUP buiten audit-context.

**✅ Voor**
- 🔗 Audit-bewijs wordt verzameld doorheen heel de bewijsfase (typisch jan-feb na boekafsluiting 31/12), maar ook tijdens interim-werk (nov-dec) voor risk-assessment + controls-tests, en in afronding (mrt-apr) voor subsequent events + LOR.

## Sub-concepten

### 📦 Audit-beweringen (assertions)  
_`kader` (subconcept)_

#### Definitie

📖 Beweringen zijn impliciete beweringen van het bestuur door het opstellen van de jaarrekening — de auditor identificeert ze om risico's per bewering in te schatten (ISA 315 herzien 2019 par. A190). Drie groepen:

**Voor transactiestromen en gebeurtenissen**: (1) occurrence — heeft de transactie zich werkelijk voorgedaan en betreft ze de entiteit; (2) volledigheid — alle transacties zijn opgenomen; (3) juistheid — correcte bedragen; (4) cut-off — in juiste boekjaar; (5) classificatie — in juiste rekening.

**Voor balanssaldi op einddatum**: (1) bestaan; (2) rechten en verplichtingen; (3) volledigheid; (4) juistheid waardering en allocatie.

**Voor presentatie en toelichtingen**: (1) occurrence/rechten/verplichtingen; (2) volledigheid; (3) classificatie/begrijpelijkheid; (4) juistheid waardering.

<small>📚 ISA 315 (herzien 2019) — par. A190 — _norm_</small>

### 📦 De 7 controleprocedures (ISA 500/505/520)  
_`kader` (subconcept)_

#### Definitie

📖 **1. Inspectie** — onderzoeken van administratieve vastleggingen of documenten (intern of extern) of fysieke activa. Voorbeeld: factuur-leveringsbon-bestelbon trio bekijken; voorraad-aanwezigheid in magazijn inspecteren.

**2. Observatie** — toezien op een proces dat door anderen wordt uitgevoerd. Voorbeeld: aanwezig zijn bij voorraadopname rond 31/12.

**3. Externe bevestiging** (ISA 505) — rechtstreeks ontvangen schriftelijk antwoord van een derde. Voorbeeld: banken-bevestiging (saldi + facilities + ondertekeningsbevoegden), debiteuren-circularisatie, advocaat-bevestigingsbrief.

**4. Herrekening** — wiskundige juistheid van documenten of administratieve vastleggingen verifiëren.

**5. Herperformance** — onafhankelijk uitvoeren van procedures of interne beheersingsmaatregelen die oorspronkelijk door de entiteit werden gedaan.

**6. Cijferanalyses** (ISA 520) — evaluaties van financiële informatie via plausibele relaties tussen financiële en niet-financiële data (bv. loonkost/headcount, bruto-marge per product).

**7. Navraag** — vragen stellen aan management, governance of derden — schriftelijk of mondeling. Alleen voldoende: zelden — meestal combineren met andere procedure.

<small>📚 ISA 500 — par. A14-A25 — _norm_ · ISA 505 — Externe bevestigingen — _norm_ · ISA 520 — Cijferanalyses — _norm_</small>

### 📦 Steekproef (ISA 530)  
_`procedure` (subconcept)_

#### Definitie

📖 Steekproef = toepassen van procedures op minder dan 100% van de items binnen een populatie, zodanig dat elk item een kans heeft om geselecteerd te worden. Twee benaderingen:

**Statistische steekproef**: random of systematische selectie + waarschijnlijkheidstheorie om resultaat naar populatie te extrapoleren met gekende foutmarge. Vereist gedefinieerde steekproefomvang gebaseerd op tolerable error, expected error en confidence level. Voorbeeld: monetary unit sampling (MUS) bij debiteuren.

**Niet-statistische steekproef**: professionele oordeelsvorming bepaalt selectie (bv. alle items boven materialiteit + steekproef onder). Geen formele statistische extrapolatie maar wel geredeneerde conclusie.

De auditor moet evalueren of identificeerde afwijkingen representatief zijn voor de hele populatie (projection of misstatements).

<small>📚 ISA 530 — par. 1-2 + definities — _norm_</small>

### 📦 Schriftelijke bevestiging management (Letter of Representation)  
_`instrument` (subconcept)_

#### Definitie

📖 Een schriftelijke verklaring van het management aan de auditor, gedateerd dicht bij maar niet later dan de datum van de controleverklaring, met bevestigingen over: (a) verantwoordelijkheid management voor opstellen jaarrekening; (b) alle informatie en toegang verschaft; (c) toepassing continuïteitsveronderstelling; (d) alle transacties geboekt; (e) verbonden partijen, claims, schattingen, subsequent events bekendgemaakt. **Niet vervangen** door andere bewijsvormen — wel aanvullend en niet voldoende op zichzelf. Indien management weigert te ondertekenen → mogelijk oordeelonthouding (ISA 580 par. 17-20).

<small>📚 ISA 580 — Schriftelijke bevestigingen — _norm_</small>

### 📦 IT-bewijs en CAATs  
_`procedure` (subconcept)_

#### Definitie

🔗 In moderne entiteiten is veel bewijs IT-gedreven: ERP-systemen genereren journaalboekingen automatisch, ondersteunende documenten zijn elektronisch. De auditor moet (1) de IT-controle-omgeving evalueren (general IT controls — toegangsbeheer, change management, backup; application controls — input validation, geautoriseerde workflow); (2) zelf computer-assisted audit techniques (CAATs) gebruiken: data-extractie + analyse via tools (IDEA, ACL, scripting). Voorbeeld: volledige populatie verkoopfacturen testen op anomalieën, niet steekproef-gebaseerd.

<small>📚 ISA 315 (herzien 2019) — par. 25 + A99-A115 IT-omgeving — _norm_ · ISA 330 — par. A14 CAATs — _norm_</small>

### 📦 Boekhoudkundige schattingen (ISA 540 herzien)  
_`procedure` (subconcept)_

#### Definitie

📖 Schattingen (voorzieningen, afschrijvingen, waardeverminderingen, fair values, going concern) zijn intrinsiek onzeker. ISA 540 (herzien, ingangsdatum 15/12/2019) versterkt de aanpak: (1) inzicht in de gevolgde methode + onderliggende assumpties van management; (2) inschatting van inherent risico via complexiteit, subjectiviteit, schattingsonzekerheid; (3) test van de uitkomst, OF herperformance met eigen methode + ranges, OF terugkijken naar uitkomst-vs-realisatie van vorige boekjaren; (4) overall evaluatie of geheel van schattingen leidt tot redelijke uitkomst — geen systematische optimist/pessimist-bias.

<small>📚 ISA 540 (herzien) — Vereisten + definities — _norm_</small>

### 📦 Niet-naleving van wet- en regelgeving (NOCLAR — Non-Compliance with Laws and Regulations)  
_`regime` (subconcept)_

#### Definitie

📖 ISA 250 (herzien) regelt hoe de auditor in zijn werkzaamheden rekening houdt met wet- en regelgeving. Twee categorieën: (1) wetgeving met **directe impact op de jaarrekening** (fiscale wetten, sociale zekerheid, milieuwetgeving die provisies vereist) — auditor controleert naleving als deel van zijn werk; (2) **overige wetgeving** (corruptiewetten, antiwitwas, sectorregulering) — auditor blijft alert voor signalen, voert specifieke werkzaamheden uit (navraag bij management/governance, leest notulen) zonder dat hij volledige naleving controleert. Bij vermoeden van niet-naleving: communicatie met management en governance, eventueel rapportering aan toezichthouder, mogelijk gevolgen voor verklaring.

<small>📚 ISA 250 (herzien) — Vereisten + Inleiding — _norm_</small>

## Bouwstenen

### 📜 Voldoende EN geschikt — twee aparte kwaliteiten  
_`regel`_

📖 **Voldoende** = kwantiteit. Hoeveel bewijs is nodig? Hangt af van risico (hoger risico → meer bewijs) en bewijskwaliteit (hogere kwaliteit → minder hoeveelheid nodig). **Geschikt** = kwaliteit, opgedeeld in: (a) **relevantie** — bewijs gericht op de juiste assertion (een externe bankbevestiging is relevant voor bestaan kas-banktegoed maar niet voor waardering voorraden); (b) **betrouwbaarheid** — bron-eigenschappen: extern > intern; schriftelijk > mondeling; origineel > kopie; door entiteit met goede IB > slechte IB; door auditor zelf verkregen > door management aangereikt.

<small>📚 ISA 500 — par. A4 + A30 — _norm_</small>

### 📜 Positieve vs negatieve externe bevestiging (ISA 505)  
_`regel`_

📖 **Positieve bevestiging**: derde wordt gevraagd het saldo te bevestigen — antwoord vereist (zonder antwoord = follow-up). Hoogste betrouwbaarheid. **Negatieve bevestiging**: derde wordt alleen gevraagd te reageren indien hij niet akkoord is. Lagere zekerheid (uitblijven antwoord ≠ bevestiging). ISA 505 staat negatieve bevestiging alleen toe als combinatie van: laag RMM, kleine homogene saldi, betrouwbaar IB-systeem, geen verwachte uitzonderingen.

<small>📚 ISA 505 — par. A23 negatieve bevestigingen — _norm_</small>

### 👣 Accumuleren van geïdentificeerde afwijkingen (ISA 450)  
_`stap`_

📖 Alle tijdens de controle vastgestelde afwijkingen (behalve duidelijk triviale) worden in een lijst (Summary of Audit Differences / SAD-list) gehouden. Bij afronding (fase 4) worden ze gecommuniceerd aan management voor correctie; niet-gecorrigeerde afwijkingen worden vergeleken met materialiteit voor het uiteindelijke oordeel. Een ‘triviaal’-drempel (vaak 5% van materialiteit, max 5.000 EUR) wordt vooraf vastgelegd.

<small>📚 ISA 450 — par. 5-13 — _norm_</small>

## Valkuilen

### ⚠️ Documenten = bewijs

**Verkeerde assumptie**: Alles wat de cliënt aanlevert is bewijs voor zijn beweringen.

**Kernpunt**: Bewijs heeft kwaliteit. Een door management gegenereerd Excel zonder doorklik naar onderliggende systemen is zwak bewijs; een door de bank rechtstreeks naar de auditor gestuurde bevestiging is sterk. Bovendien zijn betalingsbewijzen geen bewijs voor het bestaan van een vordering — alleen voor de inning. Wie ‘ik heb het document gezien’ als enige bewijs aanvoert, faalt op het kwaliteitsvereiste.

<small>📚 ISA 500 — par. A30 betrouwbaarheid — _norm_</small>

### ⚠️ Steekproef = automatisch geldig

**Verkeerde assumptie**: Als ik een steekproef trek, mag ik die naar de hele populatie extrapoleren.

**Kernpunt**: Alleen statistische steekproef met random of systematic selection mag extrapoleren met gekende foutmarge. ‘Ik nam de eerste 10 facturen’ is geen geldige steekproef. Bovendien geldt: gevonden fouten moeten *geprojecteerd* worden naar de populatie (ISA 530 par. 14) — niet alleen ‘we vonden 3 fouten dus 3 fouten’.

<small>📚 ISA 530 — par. 14 projectie — _norm_</small>

### ⚠️ LOR = vrijbrief

**Verkeerde assumptie**: Een ondertekende letter of representation van het bestuur vervangt eigen bewijswerk.

**Kernpunt**: ISA 580 par. 4: een LOR is *aanvullend* bewijs, niet vervangend. Zelfs een uitgebreide LOR ontslaat de auditor niet van zijn substantief werk. Bij twijfel over de integriteit van het bestuur kan een LOR zelfs onbetrouwbaar zijn — dan moet de auditor de hele bewijslast herevalueren.

<small>📚 ISA 580 — par. 4 + A1 — _norm_</small>

## Syntheses

### 🧩 Synthese  
_`matrix`_

Bewijs-piramide — oplopende overtuigingskracht.

## Accountant-perspectieven

### De accountant als bewijsverzamelaar

#### 🔍 Auditor

##### 👣 Concrete uitvoering bewijswerk per cyclus  
_`stap`_

🔗 Per cyclus (verkopen-debiteuren, aankopen-crediteuren, voorraad, lonen, vaste activa, EV, schulden, belastingen): (1) walk-through bij planning — flow begrijpen; (2) controls-test indien plan was te steunen op IB; (3) substantive analytical procedure als marge/ratio plausibel is; (4) tests of details: steekproef facturen (occurrence + juistheid), cut-off-test rond 31/12 (volledigheid), externe bevestigingen voor saldi (bestaan); (5) waardevermindering-evaluatie (waardering); (6) presentatie/disclosure-check tegen verslaggevingsstelsel.

<small>📚 ISA 330 — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Cyclus-context (fase 3) → [[controleopdracht]] _(moet-verwijzen)_
- → Planning stuurt bewijswerk (input) → [[audit-planning]] _(moet-verwijzen)_
- → Afronding gebruikt bewijs voor oordeel (output) → [[audit-afronding]] _(moet-verwijzen)_
- → Dossier-documentatie → [[revisiedossier]] _(moet-verwijzen)_
- → IT-controles als bewijs in IT-omgeving (cross IC) → [[it-controles]] _(moet-verwijzen)_
- → Cyclus-substantive-testing → [[cyclus-analyse]] _(moet-verwijzen)_
- ↪ Verbonden-partijen-procedures → ⏳ verbonden-partijen _(mag-verwijzen)_
- → Fraude-procedures (ISA 240) → ⏳ fraude _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[controleopdracht]]
### `beinvloed_door`
- [[audit-planning]]
### `triggert`
- [[audit-afronding]]
### `gedocumenteerd_in`
- [[revisiedossier]]
### `vereist`
- [[it-controles]]
