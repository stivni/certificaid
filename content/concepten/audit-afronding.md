---
title: "Audit-afronding"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.6.IV
  - 1.6.IV.A
  - 1.6.IV.B
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/audit-afronding.json"
---

# Audit-afronding

_Procedure_

🏛️ Kader · Anchors: `1.6.IV` · `1.6.IV.A` · `1.6.IV.B` · Wave: `skeleton-controle-beroep-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: afronding van de opdracht · audit completion · opdrachtafronding · eindfase audit · audit closing — **Vertalingen**: fr: achèvement de l'audit · en: audit completion

## Definitie

📖 Audit-afronding is fase 4: de laatste fase vóór de ondertekening en uitgifte van de controleverklaring. Het is niet ‘alles is al gedaan, nog snel ondertekenen’ maar een eigen werkstroom met zes hoofdcomponenten: (1) toetsen van gebeurtenissen na de einddatum van de verslagperiode (ISA 560); (2) evaluatie van geaccumuleerde misstatements tegen materialiteit (ISA 450); (3) overall analytical review op de definitieve jaarrekening; (4) going-concern-evaluatie (ISA 570 herzien); (5) verkrijgen van schriftelijke bevestiging management (ISA 580); (6) communicatie met de met governance belaste personen (ISA 260) en management (ISA 265). Pas na deze sequentie kan het oordeel gevormd en de verklaring gedateerd worden.

<small>📚 ISA 700 (herzien) — par. 41 datering — _norm_ · ISA 560 — Doelstellingen par. 4 — _norm_</small>

## Substantie

🔗 De afronding is qua karakter anders dan de drie eerdere fasen: minder procedure-uitvoering, meer **synthese en oordeelsvorming**. De auditor stapt terug en kijkt naar de jaarrekening als geheel: kloppen de cijfers ook bij elkaar? Geven ze een coherent beeld? Welk patroon ontstaat in de niet-gecorrigeerde fouten — willekeurig of systematisch in één richting (bias)? Tegelijk loopt een communicatie-stroom: management krijgt voorgestelde correcties, governance krijgt significante bevindingen en management letter. Het hele werk culmineert in één moment: het ondertekenen van de verklaring — pas dan is de opdracht juridisch afgerond.

<small>📚 ISA 450 — par. 11 bias-evaluatie — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom een aparte afrondingsfase met eigen procedures? (1) **Tijdsverloop**: tussen einddatum boekjaar (31/12) en ondertekening verklaring (april/mei) gebeuren dingen — faillissementen klanten, brand, rechtszaken — die de jaarrekening kunnen beïnvloeden. ISA 560 dwingt de auditor om die periode actief te onderzoeken. (2) **Cumulatieve evaluatie**: tijdens fase 3 worden afwijkingen één voor één gevonden; pas in fase 4 wordt het **totaal** beoordeeld vs materialiteit. (3) **Governance-loop**: management en bestuur krijgen formeel feedback, kunnen reageren, eventueel correcties doorvoeren — beslissingen die het oordeel beïnvloeden. (4) **Going-concern als overall judgment**: alleen op afronding heeft de auditor het volle beeld om continuïteit te beoordelen.

<small>📚 ISA 560 — _norm_ · ISA 450 — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: ISA 560 · ISA 450 · ISA 570 (herzien) · ISA 260 (herzien) · ISA 265 · ISA 700 (herzien) · WVV (timing verklaring vóór AV)

Afrondingsfase timing wordt mee bepaald door WVV: jaarrekening en commissarisverslag moeten 15 dagen vóór algemene vergadering ter beschikking liggen voor de aandeelhouders (art. 3:67 WVV).

**▶️ Trigger start**
- 🔗 Afronding start zodra substantief bewijswerk afgerond is (typisch eind februari/begin maart voor 31/12-afsluitingen) en het management een definitief ontwerp van jaarrekening voorlegt.

**⏹ Trigger einde**
- 📖 Afronding eindigt met ondertekening en datering controleverklaring (ISA 700 par. 41) — niet vóórdat (a) voldoende en geschikt bewijs verzameld is, (b) ondertekende LOR ontvangen, (c) jaarrekening door bestuur goedgekeurd, (d) afrondings-werkdocumenten compleet in dossier.

## Sub-concepten

### 📦 Subsequent events (gebeurtenissen na einddatum verslagperiode)  
_`procedure` (subconcept)_

#### Definitie

📖 ISA 560 verplicht de auditor om actief de periode tussen einddatum (typ. 31/12) en datum verklaring te onderzoeken op gebeurtenissen die de jaarrekening beïnvloeden. Twee categorieën (IAS 10 / CBN-advies 2009/9):

**Adjusting events** — leveren bewijs over een toestand die op einddatum reeds bestond → cijfers in jaarrekening *aanpassen*. Voorbeeld: faillissement van een grote klant op 15 februari → waardevermindering op handelsvordering 31/12.

**Disclosing events** — wijzen op nieuwe toestand na einddatum → *toelichting* in jaarrekening, geen aanpassing cijfers. Voorbeeld: brand in fabriek op 10 februari → toelichting in commentaar bestuursorgaan, geen retroactieve aanpassing voorraadwaardering 31/12.

Procedures: navraag management, lezen tussentijdse cijfers en bestuursvergaderingen, lezen recente notulen, gesprek met advocaat over claims/processen, opvolging post-balansdatum-transacties.

<small>📚 ISA 560 — Doelstellingen + Vereisten — _norm_ · CBN-advies 2009/9 — IAS 10 Gebeurtenissen na balansdatum — _advies_</small>

### 📦 Misstatements-evaluatie (clearing memo, ISA 450)  
_`procedure` (subconcept)_

#### Definitie

📖 Alle tijdens de controle geaccumuleerde afwijkingen worden in een **summary of audit differences (SAD-list)** opgenomen. Bij afronding: (1) niet-gecorrigeerde fouten optellen → vergelijken met materialiteit; (2) **kwalitatieve evaluatie** — ook kleine bedragen kunnen materieel zijn (verandering verlies→winst, schending convenant, omgekeerde trend); (3) **bias-check** — zijn correcties systematisch in één richting? (vaak winst-maximaliserend = bias-indicator); (4) management vragen om correctie; (5) niet-gecorrigeerde materiële afwijkingen → impact op oordeel (oordeel met voorbehoud of afkeurend).

<small>📚 ISA 450 — par. 8-13 — _norm_</small>

### 📦 Overall analytical review  
_`procedure` (subconcept)_

#### Definitie

🔗 Een laatste plausibiliteits-check op de jaarrekening als geheel — *na* alle correcties verwerkt zijn. De auditor herkent het beeld terug: omzet vs sector, marge vs voorgaande jaren, EBITDA vs cash flow, ratio's vs business-model. Onverklaarde anomalieën dwingen tot terugkeer naar fase 3 voor extra bewijswerk. Doel: voorkomen dat individuele procedures wel pass-en maar de jaarrekening als geheel niet klopt — een hardnekkig fenomeen bij grote organisaties waar één team één cyclus doet en niemand het overzicht heeft.

<small>📚 ISA 520 — Cijferanalyses bij afronding — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Going-concern-evaluatie (ISA 570 herzien)  
_`procedure` (subconcept)_

#### Definitie

📖 Het bestuursorgaan moet de continuïteit van de entiteit beoordelen over een horizon van minstens 12 maanden vanaf einddatum (in BE doorgaans uitgebreid tot 12 maanden vanaf controleverklaring-datum onder CBN-advies 2018/18). De auditor evalueert deze beoordeling: (1) lopen omstandigheden of gebeurtenissen die significante twijfel doen rijzen? (verliezen, negatieve kasstroom, schulden boven activa, klantverlies, geschillen, ontbrekende financiering, ...); (2) is management-plan om twijfel weg te nemen realistisch? (3) is de toelichting in jaarrekening adequaat?

Uitkomsten: continuïteit OK → standaard oordeel; significante onzekerheid passend toegelicht → ongewijzigd oordeel + paragraaf ‘materiële onzekerheid m.b.t. continuïteit’ (ISA 570 par. 22); continuïteit niet adequaat toegelicht → oordeel met voorbehoud of afkeurend; bewijs van niet-continuïteit terwijl jaarrekening op going-concern-basis is opgesteld → afkeurend oordeel.

<small>📚 ISA 570 (herzien) — Vereisten + par. 22 — _norm_ · CBN-advies 2018/18 — Jaarlijkse beoordeling continuïteitsveronderstelling — _advies_</small>

### 📦 Communicatie met de met governance belaste personen (ISA 260)  
_`procedure` (subconcept)_

#### Definitie

📖 ISA 260 vereist dat de auditor de met governance belaste personen (typisch raad van bestuur of auditcomité) tijdens en bij afronding informeert over: (a) verantwoordelijkheden auditor + scope; (b) significante bevindingen — kwalitatieve aspecten van accounting practices, kernpunten van de controle, problemen rond schattingen, niet-gecorrigeerde afwijkingen; (c) onafhankelijkheids-bevestiging; (d) eventueel oneens met management. Tweerichtingscommunicatie: bestuur kan informatie verstrekken die controle helpt. Vorm: schriftelijk verslag bij PIE-controles + voor materiële zaken.

<small>📚 ISA 260 (herzien) — Vereisten — _norm_</small>

### 📦 Management letter — interne-controle-deficiënties (ISA 265)  
_`instrument` (subconcept)_

#### Definitie

📖 ISA 265 verplicht de auditor om significante interne-controle-deficiënties die hij identificeerde tijdens het bewijswerk, schriftelijk te communiceren — primair aan de met governance belaste personen, met afschrift aan management. ‘Significant’ = belangrijk genoeg om bestuur aandacht te vragen, ook al beïnvloedde het direct geen materiële afwijking. Bevat: omschrijving deficiëntie + mogelijke gevolgen + (typisch ook) aanbeveling tot remediëring. Wordt vaak afgegeven als ‘management letter’ — een nuttig product voor de cliënt naast de wettelijke verklaring.

<small>📚 ISA 265 — Vereisten + Toepassingsgerichte teksten — _norm_</small>

## Bouwstenen

### 📜 Datering van de controleverklaring  
_`regel`_

📖 ISA 700 par. 41: datering niet eerder dan datum waarop voldoende geschikt bewijs verkregen is + bestuur de jaarrekening heeft goedgekeurd. Praktisch: LOR-datum, bestuursbesluit-datum en verklaring-datum vallen vaak op dezelfde dag samen. Subsequent events worden onderzocht tot deze datum. Gebeurtenissen die ná deze datum maar vóór uitgifte aan derden aan de auditor bekend worden (ISA 560 par. 10-13): auditor moet inschatten of jaarrekening moet worden aangepast en kan zijn verklaring intrekken/wijzigen.

<small>📚 ISA 700 (herzien) — par. 41 — _norm_ · ISA 560 — par. 10-13 — _norm_</small>

### 📜 Andere informatie naast de jaarrekening (ISA 720 herzien)  
_`regel`_

📖 Het jaarverslag bevat naast de jaarrekening ook bestuurdersverslag, niet-financiële informatie (CSRD-rapportering), kerncijferoverzicht, ... ISA 720 (herzien) verplicht de auditor om deze ‘andere informatie’ door te lezen en te toetsen op (a) materiële inconsistentie met jaarrekening, (b) materiële inconsistentie met door auditor verkregen kennis, (c) anderszins ogenschijnlijk misleidende stellingen. Indien onverbeterd → toevoeging aan controleverklaring.

<small>📚 ISA 720 (herzien) — Definities + Vereisten — _norm_</small>

### 👣 Engagement Quality Review (EQR)  
_`stap`_

📖 Voor controles van organisaties van openbaar belang (PIE), beursgenoteerden en andere ‘high-risk’-opdrachten vereist ISA 220 (herzien) een onafhankelijke kwaliteitsreviewer (engagement quality reviewer) die het werk van het opdrachtteam beoordeelt vóór ondertekening — in het bijzonder de kritische oordeelsmomenten (materialiteit, significant risks, kernpunten, oordeel-classificatie). De EQR ondertekent een aparte verklaring in het dossier. Voor KMO-controles is EQR niet verplicht maar wel beschikbaar als interne kwaliteitsmaatregel binnen het kantoor.

<small>📚 ISA 220 (herzien) — Engagement Quality Review — _norm_</small>

## Valkuilen

### ⚠️ Subsequent events = ‘nog snel even checken’

**Verkeerde assumptie**: Tijdens afronding even bij management vragen of er iets gebeurd is na 31/12 — antwoord ‘nee’ → klaar.

**Kernpunt**: ISA 560 vraagt actief onderzoek: notulen lezen, tussentijdse cijfers analyseren, advocatenbrief volgen, post-31/12-transacties bekijken. Een eenvoudig ‘nee’ van management is geen voldoende controle-informatie — daar gaat de auditor onderuit als zich later iets materiëel blijkt voorgedaan te hebben.

<small>📚 ISA 560 — Vereisten par. 6-9 — _norm_</small>

### ⚠️ Going concern = boekhoudprobleem van management

**Verkeerde assumptie**: Het is aan management om continuïteit te beoordelen — de auditor heeft daar geen eigen mening over.

**Kernpunt**: Management beoordeelt, maar ISA 570 verplicht de auditor tot eigen evaluatie. Bij significant twijfel + adequate toelichting → ‘material uncertainty’-paragraaf. Stilzwijgend volgen van management terwijl tegenstrijdig bewijs voorhanden is = audit-falen (vele zaken in faillissement-rechtbank lopen daarop terug).

<small>📚 ISA 570 (herzien) — Vereisten par. 16-23 — _norm_</small>

### ⚠️ Niet-gecorrigeerde fout < materialiteit = OK

**Verkeerde assumptie**: Zolang de niet-gecorrigeerde afwijking onder de materialiteit blijft, ga je voor een schoon oordeel.

**Kernpunt**: ISA 450 par. 11: ook kwalitatieve overwegingen tellen. Een fout die verlies in winst doet kantelen, een covenant in inbreuk doet komen, of management-bonus-target precies haalt — ook al kwantitatief klein — kan materieel zijn. Bias-patroon (alle correcties richting verbetering) is op zich al een waarschuwing.

<small>📚 ISA 450 — par. 11 — _norm_</small>

## Syntheses

### 🧩 Synthese  
_`tijdslijn`_

Typische afrondings-activiteiten in chronologische volgorde (voor jaarafsluiting 31/12).

## Accountant-perspectieven

### De accountant in de afrondingsfase

#### 🔍 Auditor

##### 👣 Afrondings-checklist  
_`stap`_

📖 (1) Definitieve jaarrekening + finale draft commissarisverslag samenleggen. (2) SAD-list + clearing memo bijwerken met laatste correcties. (3) Subsequent-events-procedure-werkdocument vullen (notulen-review, tussentijdse cijfers, advocaatbrieven). (4) Going-concern-werkdocument met management-prognose, eigen analyse. (5) Memo overall analytical review. (6) LOR opstellen + management laten ondertekenen op datum verklaring. (7) Memo bestuur/auditcomité (ISA 260) + management letter (ISA 265) opstellen. (8) Reviewen alle werkdocumenten zijn afgetekend door reviewers. (9) Datum vaststellen samen met bestuursbesluit + ondertekening verklaring. (10) Werkdocumenten archiveren binnen 60 dagen na uitgifte (ISA 230 par. 14-16).

<small>📚 ISA 700 (herzien) — _norm_ · ISA 560 — _norm_ · ISA 230 — par. 14-16 — _norm_</small>

## Verder lezen (scope-out)

- → Cyclus-context (fase 4) → [[controleopdracht]] _(moet-verwijzen)_
- → Bewijs als input → [[audit-bewijs]] _(moet-verwijzen)_
- → Eindverslag als output → [[controleverklaring]] _(moet-verwijzen)_
- → Going-concern-principe + diepe inhoud → ⏳ continuiteit-going-concern _(moet-verwijzen)_
- → Auditcomité-communicatie → [[auditcomite]] _(moet-verwijzen)_
- → IC-deficiënties bron → [[interne-controle]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[controleopdracht]]
### `beinvloed_door`
- [[audit-bewijs]]
- ⏳ continuiteit-going-concern
### `triggert`
- [[controleverklaring]]
### `gedocumenteerd_in`
- [[auditcomite]]
