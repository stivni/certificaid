---
title: "Controleopdracht"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.6.I
  - 1.6.I.A
  - 1.6.I.B
  - 1.6.II
  - 1.6.taak.1
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/controleopdracht.json"
---

_Procedure_ · ook: assurance-opdracht · audit-cyclus · audit-aanpak · opdracht-uitvoering · engagement lifecycle

## Definitie

Een controleopdracht is een assurance-opdracht waarbij de gecertificeerd accountant of bedrijfsrevisor voldoende en geschikte controle-informatie verzamelt om met een redelijke mate van zekerheid (reasonable assurance) te oordelen of de financiële overzichten in alle van materieel belang zijnde opzichten een getrouw beeld geven volgens het van toepassing zijnde stelsel inzake financiële verslaggeving. De opdracht doorloopt een dwingende cyclus van vier fasen — aanvaarden, plannen, bewijswerk, afronden — die elkaar opvolgen maar ook iteratief blijven verlopen: nieuwe bevindingen in fase 3 kunnen de planning uit fase 2 doen herzien. De ruggengraat van een controleopdracht ligt in de International Standards on Auditing (ISA), met voor kleine en middelgrote entiteiten in België een specifieke uitwerking via de ITAA-KMO-controlenorm.

<small>📖 ISA 300 — par. 2 — _norm_ · ISA 200 — Algehele doelstellingen — _norm_ · ITAA-norm-kmo-controlenorm — § 2.2.1 — _norm_</small>

## Substantie

Wat de controleopdracht in de praktijk doet is geen ‘nakijken of de cijfers kloppen’ — het is een gestructureerde risico-georiënteerde overtuigingsoefening. De accountant gaat uit van de assertions (beweringen) die het bestuur impliciet doet door de jaarrekening voor te leggen: bestaan, volledigheid, waardering, rechten/verplichtingen, presentatie. Voor elke materiële post bepaalt hij waar het risico op een afwijking van materieel belang het grootst is en stemt zijn werk daarop af. De cyclus eindigt niet met ‘alles is OK’ maar met een geargumenteerd oordeel — vier mogelijke formuleringen (zonder voorbehoud · met voorbehoud · afkeurend · onthouding) — dat de stakeholders (aandeelhouders, banken, fiscus, AV) gebruiken om te beslissen of ze zich op de cijfers kunnen verlaten.

```mermaid
flowchart LR
  A[Fase 1: Aanvaarden] --> B[Fase 2: Plannen]
  B --> C[Fase 3: Bewijswerk]
  C --> D[Fase 4: Afronden + Oordeel]
  C -.iteratief.-> B
  D --> E[Controleverklaring]
```

<small>🔗 ISA 300 — par. A3 (planning als iteratief proces) — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Waarom een dwingende 4-fase-cyclus? Twee redenen. (1) Bewijslast-architectuur: een oordeel ‘in alle materiële opzichten’ kan alleen rusten op een keten van gedocumenteerde stappen — wie controleert moet kunnen aantonen dát hij de juiste risico's zag, dáárop inspeelde, en zijn besluit op concreet bewijs steunt. Spring je een fase over, dan vervalt het oordeel als juridisch verdedigbaar product. (2) Onafhankelijkheid van resultaat: de accountant moet zijn oordeel kunnen geven onafhankelijk van wat het management hoopt. De fase-discipline (eerst onafhankelijkheid checken, dan plannen, dan bewijs, dan oordelen) is precies wat hem beschermt tegen ‘achteraf de cijfers goedmaken’. De ISA-architectuur en de ITAA-KMO-controlenorm zetten deze logica om in proceduregaranties.

<small>🔗 ISA 200 — Algehele doelstellingen — _norm_ · ITAA-norm-kmo-controlenorm — § 4.3.7 — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: ISA-stelsel (IAASB) · ITAA-KMO-controlenorm · WVV (commissaris) · Wet 7 december 2016 (organisatie ITAA en bedrijfsrevisorenfunctie)

De 4-fase-cyclus is structureel: alle ISA's en de ITAA-KMO-controlenorm bouwen erop voort. ISA-herzieningen wijzigen detail (bv. ISA 315 (herzien 2019), ISA 220 (herzien), ISA 600 herzien voor groepen), maar niet de architectuur.

**✅ Voor**
- 🔗 Een volwaardige controleopdracht (reasonable assurance) past bij: wettelijke commissaris-opdrachten in (middel-)grote vennootschappen (WVV art. 3:72 e.v.), vrijwillige audit bij banken/leningen, due diligence bij overname, audit van geconsolideerde jaarrekening, controle in gereglementeerde sectoren (verzekeringen, kredietinstellingen). Voor KMO's onder de groottecriteria is doorgaans samenstellings- of beoordelingsopdracht passender — de keuze ligt bij de cliënt, niet bij de wet.

**📋 Voorwaarden**
- 📖 Randvoorwaarden vóór aanvaarding (ISA 210 + ITAA-KMO-controlenorm § 2.2.1): (a) het bestuur erkent zijn verantwoordelijkheid voor de financiële overzichten; (b) het van toepassing zijnde verslaggevingsstelsel is aanvaardbaar (BE-GAAP, IFRS-EU, ...); (c) de accountant beschikt over de bekwaamheid, medewerking, middelen en tijd om de opdracht uit te voeren; (d) geen beperking van de reikwijdte die een oordeel onmogelijk zou maken; (e) onafhankelijkheid verzekerd (IESBA-code + ITAA-deontologie).

**▶️ Trigger start**
- 📖 De cyclus start formeel met de ondertekende opdrachtbrief — het contractueel-deontologisch beginpunt. Bij commissaris-opdrachten gaat daaraan een benoeming door de algemene vergadering vooraf (WVV art. 3:58, mandaat 3 jaar hernieuwbaar).

**⏹ Trigger einde**
- 📖 De cyclus eindigt bij ondertekening en uitgifte van de controleverklaring. De handtekening mag pas dateren nadat: (a) voldoende en geschikte controle-informatie verkregen is, (b) bestuur formele schriftelijke bevestigingen (letter of representation, ISA 580) leverde, (c) jaarrekening door bestuur is goedgekeurd. Gebeurtenissen na de einddatum maar vóór de verklaring (ISA 560) blijven in scope.

**⚠️ Risico**
- 🔗 Hoofdrisico voor de accountant: een ten onrechte goedkeurend oordeel afgeven (Type II audit-risico). Sancties: tucht (ITAA), beroepsaansprakelijkheid (schadevergoeding aan misleide derden), strafrechtelijk in fraude-gevallen, reputatieschade. Mitigatie: rigoureuze fase-discipline, professioneel-kritische instelling, dossier-discipline (zie revisiedossier).

## Sub-concepten

### 📦 Fase 1 — Aanvaarden

#### Definitie

Pre-opdracht-activiteiten waarmee de accountant beslist of hij de opdracht aanvaardt of voortzet. Drie deelhandelingen: (a) cliënten-onderzoek inclusief antiwitwas-KYC en integriteits-check; (b) capaciteits-check — kan het kantoor deze opdracht aan in termen van bekwaamheid, middelen en tijd?; (c) onafhankelijkheids- en ethiek-check (IESBA + ITAA); en pas dan (d) opdrachtbrief opstellen en wederzijds laten ondertekenen.

<small>📖 ITAA-norm-kmo-controlenorm — § 2.2.1 §32-§38 — _norm_ · ISA 210 — Vereisten — overeenkomen voorwaarden — _norm_ · ISA 220 (herzien) — Cliëntaanvaarding en -continuering — _norm_</small>

#### Rationale

Wie een verkeerde opdracht aanvaardt, sleept zich vier fasen lang door problemen. Beter vooraf weigeren dan achteraf onthouding moeten formuleren of de opdracht teruggeven. Deze fase is dus geen formaliteit maar een eerste risico-filter.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Fase 2 — Plannen

#### Definitie

Vaststellen van (a) algehele controle-aanpak (overall audit strategy) — reikwijdte, timing, richting, beschikbare middelen — en (b) gedetailleerd controleprogramma (audit plan) op basis van inzicht in entiteit en omgeving (ISA 315), risico-inschatting (audit risk model), materialiteit (ISA 320) en geplande verdere controlewerkzaamheden (ISA 330). Planning is geen losse fase maar een doorlopend iteratief proces — gestart kort na afsluiting van vorige controle en bijgewerkt tot afronding.

<small>📖 ISA 300 — par. 2, 7, 8, 9, A3 — _norm_ · ISA 315 (herzien 2019) — risico-inschatting — _norm_ · ISA 320 — materialiteit — _norm_</small>

### 📦 Fase 3 — Bewijswerk

#### Definitie

Uitvoeren van de in fase 2 geplande controlewerkzaamheden om voldoende en geschikte controle-informatie te verzamelen per audit-bewering (assertion). Twee categorieën: (a) systeemgerichte werkzaamheden (test of controls) — verifiëren of interne beheersingsmaatregelen effectief werken; (b) gegevensgerichte werkzaamheden (substantive procedures) — cijferanalyses en detailwerkzaamheden (inspectie, observatie, navraag, externe bevestiging, herberekening, opnieuw uitvoeren). De auditor blijft alert: onverwachte bevindingen kunnen risico-inschatting en programma (fase 2) doen herzien.

<small>📖 ISA 330 — Inspelen op ingeschatte risico's — _norm_ · ISA 500 — Controle-informatie — _norm_ · ISA 505 — Externe bevestigingen — _norm_</small>

### 📦 Fase 4 — Afronden en oordelen

#### Definitie

Eindbalans van het bewijswerk: (a) overall analytical review (laatste plausibiliteits-check), (b) evaluatie van geaccumuleerde misstatements vs materialiteit (clearing memo, ISA 450), (c) toetsing gebeurtenissen na einddatum (ISA 560), (d) verkrijgen schriftelijke bevestiging management (ISA 580), (e) communicatie met de met governance belaste personen (ISA 260), (f) vormen van het oordeel (ISA 700) en (g) opstellen + uitgeven controleverklaring. Pas na deze sequentie mag de verklaring gedateerd en ondertekend worden.

<small>📖 ISA 700 (herzien) — Het vormen van een oordeel — _norm_ · ISA 560 — Gebeurtenissen na einddatum — _norm_ · ISA 580 — Schriftelijke bevestigingen — _norm_ · ISA 260 (herzien) — Communicatie met governance — _norm_</small>

## Bouwstenen

### ✴️ Professioneel-kritische instelling (professional skepticism)

Een houding die de hele opdracht doordringt: de accountant gaat niet uit van eerlijkheid noch oneerlijkheid van het management, maar van een alert vragend kritisch perspectief. Concreet: niet tevreden zijn met een eerste antwoord, doorvragen bij ongebruikelijke patronen, tegenstrijdig of ontbrekend bewijsmateriaal als rode vlag behandelen, geen genoegen nemen met enkel kopieën waar originelen verwacht worden, ongebruikelijke balansverhoudingen of laat-aangebrachte boekingen onderzoeken.

<small>📖 ISA 200 — definitie professional skepticism — _norm_ · ISA 240 — Bijlage 3 — fraude-indicatoren — _norm_</small>

**Rationale**: Zonder kritische instelling vervalt de controle in een check-the-box-oefening die fraude en materiële afwijkingen mist. ISA 200 maakt het tot een verplichte basishouding, ISA 240 vertaalt het concreet naar fraude-alertheid.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Delegatie en supervisie binnen het opdrachtteam

Een controleopdracht is teamwerk maar met persoonlijke eindverantwoordelijkheid. De opdrachtpartner (engagement partner, of bij wettelijke controle: de commissaris zelf) blijft persoonlijk verantwoordelijk voor het oordeel; junior teamleden voeren werk uit onder review. ISA 220 (herzien) eist dat de partner: (a) voldoende geschikte middelen toewijst, (b) actief betrokken is bij planning en kritische oordeelsmomenten, (c) toezicht houdt en review uitvoert, (d) eindverantwoordelijkheid neemt voor de archivering. Review-piramide: junior werk → senior review → manager review → partner review (engagement quality reviewer bij PIE-controles).

<small>📖 ISA 220 (herzien) — Kwaliteitsmanagement op opdrachtniveau — _norm_ · ISA 300 — par. 5 betrokkenheid kernleden — _norm_</small>

### ⚙️ Iteratief karakter — fasen lopen niet strikt lineair

**Substantie**: Fasen zijn op papier sequentieel maar in praktijk iteratief: een onverwachte bevinding in fase 3 (bv. een grote ongedocumenteerde transactie) doet de risico-inschatting herzien (terug naar fase 2), wat nieuwe procedures genereert (opnieuw fase 3). Planning is daarom volgens ISA 300 A3 ‘geen afzonderlijke fase maar een voortdurend en iteratief proces dat vaak kort na (of in samenhang met) de afronding van de voorgaande controle begint en verder gaat tot de afronding van de lopende controleopdracht’.

<small>📖 ISA 300 — par. A3 — _norm_</small>

### 📜 Doorlopende vs initiële controleopdracht

Bij een eerste-jaar-controle (initial engagement, ISA 510) gelden bijkomende eisen omdat de accountant geen ervaring met de entiteit heeft. Bijkomende aandachtspunten: (a) afspraken met vorige auditor (overdrachtsgesprek, inzage werkdocumenten tenzij wettelijk verboden); (b) verkrijgen voldoende controle-informatie over beginsaldi (anders mogelijke beperking oordeel); (c) zorgvuldige beoordeling van verslaggevingsprincipes die de voorgaande accountant toepaste. Bij doorlopende controle (recurring engagement) start de planning kort na afronding van de vorige cyclus.

<small>📖 ISA 510 — Initiële controleopdrachten — beginsaldi — _norm_ · ISA 300 — par. 12 + A24 — _norm_</small>

## Valkuilen

> [!warning]- Controle = ‘alles checken’
> **Verkeerde assumptie**: De accountant moet elke transactie en elk bedrag in de boekhouding nakijken om er zeker van te zijn dat alles klopt.
>
> **Kernpunt**: Een controle werkt met redelijke (niet: absolute) zekerheid en met materialiteit. Het is een risico-georiënteerde opdracht: tijd en middelen gaan naar de posten met het hoogste risico op een afwijking van materieel belang. Steekproeven (ISA 530) en cijferanalyse (ISA 520) zijn legitiem omdat 100%-controle noch nodig noch haalbaar is.
>
> <small>📖 ISA 200 — Algehele doelstellingen — redelijke zekerheid — _norm_ · ISA 320 — Materialiteit — _norm_</small>

> [!warning]- Planning één keer in januari afvinken
> **Verkeerde assumptie**: De controle-aanpak wordt aan het begin vastgelegd en vervolgens uitgevoerd zonder herziening.
>
> **Kernpunt**: ISA 300 A3 stelt expliciet dat planning iteratief is. Bewijswerk in fase 3 kan nieuwe risico's blootleggen die de planning doen herzien. Wie blindelings het oorspronkelijke plan afwerkt mist de signalen waarvoor net dat werk diende.
>
> <small>📖 ISA 300 — par. A3 — _norm_</small>

> [!warning]- Onthouding als ‘veilige optie’
> **Verkeerde assumptie**: Bij twijfel formuleert de accountant gewoon een oordeelonthouding — dat is risicoloos.
>
> **Kernpunt**: Onthouding is geen escape: het signaleert aan de markt dat de accountant geen oordeel kan geven (massief negatief signaal voor cliënt). ISA 705 eist dat onthouding alleen wordt gebruikt wanneer mogelijke effecten van niet-verkregen bewijs van materieel belang én diepgaand zijn. Een ‘gemakzucht-onthouding’ is een tuchtprobleem.
>
> <small>📖 ISA 705 (herzien) — Aanpassingen van het oordeel — _norm_</small>

## Syntheses

### 🧩 Tijdslijn

Typische tijdsverdeling controleopdracht (boekjaar dat afsluit per 31 december).

- **September-oktober jaar T** — Cliëntaanvaarding/-continuering · opdrachtbrief · planning startwerkzaamheden

- **November-december jaar T** — Inzicht entiteit & risico-inschatting (ISA 315) · interim-bewijswerk · voorraad-opname bijwonen rond 31/12

- **Januari-februari jaar T+1** — Hoofdfase bewijswerk: substantieve procedures, externe bevestigingen, schattingen testen

- **Maart-april jaar T+1** — Afronding: subsequent events, clearing memo, overall analytical review, LOR, communicatie met governance

- **April-mei jaar T+1** — Ondertekening controleverklaring (vóór AV, meestal binnen 6 maanden na afsluiting boekjaar — WVV)

## Accountant-perspectieven

### De accountant als uitvoerder van de controleopdracht

_Wat doet de gecertificeerd accountant (of bedrijfsrevisor) concreet doorheen de cyclus?_

#### 🔍 Auditor

##### 👣 Concrete handelingen in fase 1 (aanvaarden)

(1) KYC-dossier opbouwen (identificatie cliënt, lasthebbers, uiteindelijke begunstigden — antiwitwas). (2) Integriteits-check management (open bronnen, eventueel referenties). (3) Bekwaamheids- en capaciteitscheck binnen kantoor (deskundigheid sector, beschikbare uren). (4) Onafhankelijkheids-evaluatie (IESBA-bedreigingen identificeren + safeguards). (5) Overdrachtsgesprek vorige accountant indien nieuwe opdracht. (6) Opdrachtbrief opstellen volgens ISA 210/ITAA-model, ondertekenen en bewaren in permanent dossier.

<small>📖 ITAA-norm-kmo-controlenorm — § 2.2.1 §32-§38 — _norm_ · ISA 210 — Vereisten — _norm_</small>

##### 👣 Concrete handelingen in fase 2 (plannen)

(1) Inzicht verwerven in entiteit + omgeving (ISA 315 herzien 2019): sector, governance, IT, regelgeving, interne beheersing. (2) Discussiemeeting met opdrachtteam over fraude-risico (ISA 240). (3) Materialiteit bepalen: overall + performance + specifieke (ISA 320). (4) Risico's op afwijkingen van materieel belang inschatten per assertion. (5) Algehele controle-aanpak documenteren. (6) Controleprogramma opstellen (test of controls + substantive procedures) en middelen toewijzen.

<small>📖 ISA 300 — par. 7-9 — _norm_ · ISA 315 (herzien 2019) — _norm_ · ISA 320 — _norm_</small>

##### 👣 Concrete handelingen in fase 3 (bewijswerk)

(1) Test of controls waar steunen op IB-systeem efficiënt is. (2) Substantive analytical procedures op posten met logische verbanden (loonkost vs personeelsbestand). (3) Tests of details: inspectie facturen, observatie voorraadopname, externe bevestigingen (debiteuren, banken, advocaten), navraag management, herberekening. (4) Sampling waar volledig onderzoek niet praktisch is (ISA 530). (5) Schattingen testen (waardevermindering, voorzieningen) — ISA 540. (6) Werkdocumenten opbouwen met conclusie per programmapunt.

<small>📖 ISA 330 — _norm_ · ISA 500 — _norm_ · ISA 505 — _norm_ · ISA 530 — _norm_</small>

##### 👣 Concrete handelingen in fase 4 (afronden + oordeel)

(1) Overall analytical review op definitieve jaarrekening. (2) Clearing memo: alle ongecorrigeerde misstatements geaccumuleerd, vergeleken met materialiteit (ISA 450). (3) Subsequent events review tot datum verklaring (ISA 560). (4) LOR (letter of representation) verkrijgen, ondertekend door bestuur (ISA 580). (5) Communicatie met de met governance belaste personen — significante bevindingen, kernpunten, fraude-indicaties (ISA 260, 265). (6) Engagement quality review bij PIE/grote dossiers. (7) Vormen oordeel (ISA 700) → opstellen controleverklaring → dateren niet vóór bestuur jaarrekening goedkeurde.

<small>📖 ISA 450 — _norm_ · ISA 560 — _norm_ · ISA 580 — _norm_ · ISA 260 (herzien) — _norm_ · ISA 700 (herzien) — _norm_</small>

## Verder lezen (scope-out)

- → Opdracht-types (controle/beoordeling/samenstelling/AUP) bepaalt verslag-stijl in fase 4 → [[opdracht-types]] _(moet-verwijzen)_
- → Planning-detail (kennis-entiteit · risicomodel · materialiteit) → [[audit-planning]] _(moet-verwijzen)_
- → Bewijs-procedures + assertions → [[audit-bewijs]] _(moet-verwijzen)_
- → Afronding + governance-communicatie → [[audit-afronding]] _(moet-verwijzen)_
- → Eindverslag-vormen + oordelen → [[controleverklaring]] _(moet-verwijzen)_
- → Dossier-discipline → [[revisiedossier]] _(moet-verwijzen)_
- → Start: aanvaardingsproces + opdrachtbrief → [[opdrachtaanvaarding-en-opdrachtbrief]] _(moet-verwijzen)_
- → Uitvoerder bij wettelijke controle → [[commissaris]] _(moet-verwijzen)_
- → Kantoor-niveau-overlay (ISQM 1) → [[kwaliteitsmanagement-opdracht]] _(moet-verwijzen)_

## Relaties

### `bevat`
- [[audit-planning]]
- [[audit-bewijs]]
- [[audit-afronding]]
- [[controleverklaring]]
- [[revisiedossier]]
### `vereist`
- [[opdrachtaanvaarding-en-opdrachtbrief]]
- [[kwaliteitsmanagement-opdracht]]
### `uitgevoerd_door`
- [[commissaris]]
### `valt_onder`
- [[opdracht-types]]
