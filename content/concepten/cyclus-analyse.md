---
title: "Cyclus-analyse"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.7.IX
  - 1.7.IX.A
  - 1.7.IX.B
  - 1.7.IX.C
  - 1.7.IX.D
  - 1.7.IX.E
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/cyclus-analyse.json"
---

_Kader_ · ook: business cycle analysis · cyclusbenadering · transaction cycles · procure-to-pay (P2P) · order-to-cash (O2C) · hire-to-retire (H2R) · process cycles · cyclus-aanpak

## Definitie

Cyclus-analyse is de standaard-methodologische benadering waarbij de bedrijfsvoering van een onderneming wordt opgesplitst in een beperkt aantal typische transactionele cycli - elk met eigen processtappen, risico's, sleutelcontroles en informatica-systemen. De vijf canonieke cycli in audit-praktijk en interne-controle-ontwerp zijn: aankoop (procure-to-pay), productie, verkoop (order-to-cash), personeel (hire-to-retire) en voorraad. De cyclus-aanpak structureert zowel het ontwerp van interne controle (welke controles per cyclus) als de externe audit (welk bewijs verzamelen per cyclus).

<small>🔗 ISA 315 (herzien-2019) — par. 16 - bedrijfsprocessen en transactiestromen — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

De waarde van cyclus-analyse is praktisch: in plaats van losse risico's te lijsten, biedt de cyclus-aanpak een coherent verhaal dat correspondeert met de feitelijke werking. De stagiair leert risico's herkennen in volgorde van transactie-uitvoering (bv. fictieve verkoop kan ontstaan op order-stap, niet op betalingsstap). Per cyclus zijn er typische sleutelcontroles (three-way matching in aankoop, kredietcheck in verkoop, fysieke telling in voorraad) die in elke onderneming terugkomen - de cyclus-aanpak is daarmee een pedagogisch zeer effectief raster. ERP-systemen zijn overigens ook langs deze cycli opgebouwd (modules Purchasing, Manufacturing, Sales, HR, Inventory).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Een cyclus-aanpak operationaliseert de COSO-component 'controle-activiteiten' (component 3) en het ISA 315-vereiste van inzicht in de bedrijfsprocessen (par. 16). Zonder cyclus-aanpak loopt risico-identificatie chaotisch (random lijstje); met cyclus-aanpak verzamelt de auditor op systematische manier de relevante beweringen (volledigheid, juistheid, bestaan, ...) per cyclus en evalueert hij of de bijhorende sleutelcontroles werken. Voor het management is de cyclus-aanpak de operationele lens om interne controle te ontwerpen en te budgeteren - je investeert in controles waar de cyclus ze nodig heeft.

<small>📖 ISA 315 (herzien-2019) — par. 16 en par. 26 - significant transactiestromen identificeren — _norm_</small>

## Gebruikscontext

**Status**: `in-voege`

Universele methodologie in audit en interne-controle-ontwerp. Cyclus-namen kunnen verschillen (sommige handboeken gebruiken 4 cycli, andere 6 of 7) maar de essentie is constant.

**✅ Voor**
- 📖 Bij ontwerp van interne controle (één deelproject per cyclus), bij planning externe audit (significante transactiestromen identificeren - ISA 315 par. 26), bij interne audit (jaarplan met cyclus-audits), bij ERP-implementatie (modules per cyclus uitrollen).

## Sub-concepten

### 📦 Aankoopcyclus (Procure-to-Pay, P2P)

#### Definitie

Cyclus van behoefte naar betaling: aanvraag (behoefte uiten) - inkooporder (autorisatie en bestelling) - ontvangst (goederen of dienst geleverd) - facturatie (leveranciersfactuur) - boeking - betaling. Sleutelcontrole: three-way matching - inkooporder, ontvangstbon en factuur moeten kwalitatief en kwantitatief overeenstemmen voordat tot betaling wordt overgegaan.

<small>🔗 ISA 315 (herzien-2019) — Bijlage 3 — _norm_</small>

#### ⚠️ Aankoop-risico's

(1) Ongeoorloofde aankopen - bestellingen zonder autorisatie; (2) Fictieve leveranciers - betaling naar eigen of bevriende rekening (klassieke interne fraude); (3) Dubbele betaling van dezelfde factuur; (4) Niet-conforme leveringen (kwantiteit, kwaliteit, prijs); (5) Cut-off-issues rond jaareinde (factuur in verkeerd boekjaar).

<small>🔗 ISA 240 — Bijlage 1 - frauderisicofactoren oneigenlijke toe-eigening — _norm_</small>

#### ⚙️ Aankoop-sleutelcontroles

(1) Autorisatie inkooporder boven een grens door manager of zaakvoerder; (2) Three-way matching (inkooporder + ontvangstbon + factuur); (3) Geautomatiseerde duplicaat-detectie op factuurnummer per leverancier; (4) Validatie van nieuwe leveranciers (KBO-check, bankrekening-validatie, fysiek bezoek); (5) Functiescheiding aankoop versus betaling.

<small>🔗 ISA 315 (herzien-2019) — Bijlage 3 — _norm_</small>

### 📦 Productiecyclus

#### Definitie

Cyclus van grondstoffen tot afgewerkt product: behoefte-planning (MRP, master production schedule) - vrijgave van grondstoffen uit magazijn - bewerking (work in progress, WIP) - kwaliteitscontrole - afgewerkt product. Centrale boekhoudkundige kwesties: kostprijsallocatie (directe en indirecte kosten naar producten), voorraadwaardering en voorraadmutaties.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### ⚠️ Productie-risico's

(1) Rendementsverlies of schroot dat niet correct wordt geregistreerd; (2) Foute toewijzing indirecte kosten aan producten (over- of underabsorption); (3) WIP-waardering (welke kosten in WIP, welke al kost); (4) Verlies of diefstal in productie; (5) Cut-off-issues bij in-uit-stroming WIP rond balansdatum.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### ⚙️ Productie-sleutelcontroles

(1) Vergelijking standaardkosten versus werkelijke kosten met variance-analyse; (2) Goedkeuring schroot-meldingen door productiemanager; (3) Fysieke tellingen WIP op specifieke meetmomenten; (4) Standaardtijden geverifieerd via tijdsregistratie; (5) Periodieke review van kostprijscalculatie-parameters.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Verkoopcyclus (Order-to-Cash, O2C)

#### Definitie

Cyclus van order tot inning: klantorder - kredietwaardigheidstoets - levering - facturatie - inning - opvolging openstaande vorderingen. Sleutelcontrole bij elke schakel: het bedrag aan vorderingen, de waardering en de cut-off zijn klassiek de eerste audit-risico's.

<small>📖 ISA 240 — par. 26 - verplichte focus op revenue recognition — _norm_</small>

#### ⚠️ Verkoop-risico's

(1) Fictieve verkopen - omzet boeken voor niet-bestaande transacties (klassieke management fraude voor target-druk); (2) Cut-off - omzet in verkeerd boekjaar boeken; (3) Oneigenlijke kortingen of credit notes om relaties met klanten te verbergen; (4) Verkoop zonder kredietcheck waardoor oninbare vorderingen ontstaan; (5) Bill-and-hold-transacties (omzet boeken voor goederen die nog niet verzonden zijn).

<small>📖 ISA 240 — par. 26 + Bijlage 1 - revenue recognition risico's — _norm_</small>

#### ⚙️ Verkoop-sleutelcontroles

(1) Geautomatiseerde kredietcheck voor nieuwe klanten en bij order-creatie; (2) Aansluiting facturatie met levering (geleverde hoeveelheden facturatie matchen); (3) Manager-goedkeuring voor credit notes; (4) Cut-off-procedure rond balansdatum (laatste vrachtbrieven en facturen); (5) Periodieke review openstaande vorderingen ageing.

<small>🔗 ISA 315 (herzien-2019) — Bijlage 3 — _norm_</small>

### 📦 HR-cyclus (Hire-to-Retire, H2R)

#### Definitie

Cyclus van aanwerving tot uitdiensttreding: aanwerving - contract - tijdsregistratie of prestaties - loonberekening - uitbetaling - sociale lasten - uitdiensttreding. In Belgie typisch via een sociaal secretariaat (Acerta, Securex, SD Worx) dat een groot deel van de loonberekening overneemt - de IC-vraag wordt dan ook: hoe betrouwbaar is het sociaal secretariaat (ISAE 3402-rapport vragen).

<small>🔗 ISA 402 — Serviceorganisatie en gebruikersorganisatie — _norm_</small>

#### ⚠️ HR-risico's

(1) Fictieve werknemers ('ghost employees') in de loonadministratie; (2) Foute loonparameters (uurloon, anciennitsspremies, gezinslast) - kost de werkgever of nadeel voor werknemer; (3) Niet-afgesloten contracten na uitdiensttreding (loon blijft betaald); (4) Foute toepassing wetgeving (RSZ, bedrijfsvoorheffing, vakantiegeld); (5) Toegang tot loonsysteem niet correct beheerd.

<small>🔗 ISA 240 — Bijlage 1 - ghost employees — _norm_</small>

#### ⚙️ HR-sleutelcontroles

(1) Aansluiting personeelsbestand met sociaal secretariaat; (2) Goedkeuring HR-manager voor nieuwe werknemers en loonwijzigingen; (3) Functiescheiding aanwerving (HR) versus loonberekening (boekhouder) versus uitbetaling (treasury); (4) Periodieke review actieve werknemers door zaakvoerder; (5) Maandelijkse trendanalyse loonkost.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Voorraadcyclus

#### Definitie

Beheer van voorraad in alle vormen (grondstoffen, WIP, afgewerkt product, handelsvoorraad). Twee modellen: perpetual inventory (continue boekhoudkundige opvolging van elke beweging) versus periodic inventory (alleen via fysieke tellingen). In de meeste moderne ondernemingen: perpetual via ERP, aangevuld met periodieke fysieke tellingen voor validatie.

<small>📖 ISA 501 — par. 4-8 - voorraad-opname — _norm_</small>

#### ⚠️ Voorraad-risico's

(1) Diefstal of verlies dat niet wordt geregistreerd; (2) Cut-off-issues rond balansdatum (welke voorraad is van wie); (3) Verouderde of onverkoopbare voorraad zonder afwaardering (waardering tegen NRV); (4) Verkeerde kostenallocatie aan voorraad; (5) Niet-eigendomsvoorraad (consignment, in transit) verkeerd opgenomen.

<small>📖 ISA 501 — par. 4-8 — _norm_</small>

#### ⚙️ Voorraad-sleutelcontroles

(1) Periodieke (minstens jaarlijkse) fysieke voorraadtelling met onafhankelijke telploeg; (2) Cut-off-procedure rond telmoment (geen bewegingen tijdens telling, sluitnummering vrachtbrieven); (3) Magazijnbeveiliging (toegangscontrole, camera's, alarm); (4) Periodieke review slow-movers en obsolete inventory; (5) Aansluiting magazijnsysteem met grootboek.

<small>📖 ISA 501 — par. 4-8 — _norm_</small>

## Bouwstenen

### 💡 Vergelijkingsmatrix van de vijf cycli

Compacte vergelijking van de cycli op vijf assen: processtappen, typische risico's, sleutelcontroles, ERP-module en relevante boekhoudbeweringen. Helpt de stagiair om systematisch te denken en niet een cyclus over te slaan in zijn analyse.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Treasury-cyclus (optionele zesde cyclus)

Sommige handboeken behandelen treasury (beheer liquide middelen, financieringen, intresten, valuta) als een aparte zesde cyclus. Sleutelcontroles: bankreconciliatie, dubbele handtekening voor uitgaande betalingen, autorisatie van leningen door bestuursorgaan, hedging-policies. Voor de meeste kmo's gegroepeerd onder aankoop en verkoop, maar bij grotere ondernemingen of bij specifiek treasury-risico apart te behandelen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Vaste-activa-cyclus (optionele cyclus)

Cyclus van investeringsbeslissing tot desinvestering: capex-budget - autorisatie - aankoop - activering - afschrijving - revaluatie of impairment - verkoop of buitengebruikstelling. Sleutelcontroles: autorisatie capex door bestuursorgaan boven een grens, fysieke inventaris vaste activa periodiek, review afschrijvingsmethode en restwaarde, impairment-tests bij triggers. Bij investeringsintensieve ondernemingen een aparte audit-focus.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧭 Aanpassing voor kmo-context

In een kmo zijn cycli vaak minder strikt gescheiden - dezelfde persoon werkt over verschillende cycli. De cyclus-aanpak blijft pedagogisch zinvol maar wordt operationeel pragmatisch toegepast: minder formele documentatie per cyclus, focus op de sleutelcontroles met grootste impact, gebruik van standaardchecklists in plaats van uitgewerkte flowcharts. ITAA-norm-KMO-controlenorm erkent expliciet deze schaalbaarheid.

<small>📖 ITAA-norm-kmo-controlenorm — par. 43 documentatie aangepast aan omvang — _norm_ · ISA 315 (herzien-2019) — par. A156 schaalbaarheid — _norm_</small>

## Valkuilen

> [!warning]- Cyclus-indeling als rigide regel toepassen
> **Verkeerde assumptie**: Er zijn exact vijf cycli, niet meer en niet minder.
>
> **Kernpunt**: De cyclus-indeling is een pragmatische conventie, geen wet. Sommige handboeken hanteren 4 cycli, andere 6 of 7 (treasury, vaste activa, IT als aparte cyclus). Belangrijk is dat de gekozen indeling de bedrijfsprocessen van de cliente goed dekt - in een holding zonder personeel of voorraad zijn die cycli niet relevant.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Cycli onafhankelijk benaderen
> **Verkeerde assumptie**: Aankoop, verkoop en voorraad kunnen los geanalyseerd worden.
>
> **Kernpunt**: De cycli zijn sterk verweven. Een verkoop triggert een voorraadafname; een aankoop triggert een schuld; productie zit tussen voorraad-grondstoffen en voorraad-afgewerkt-product. Cut-off-issues kruisen vaak twee cycli. Bij audit: cross-checks tussen cycli zijn waardevol (verkoop versus voorraadbeweging, aankoop versus voorraadtoename).
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Cyclus-analyse vervangt risico-inschatting
> **Verkeerde assumptie**: Door de cyclus-aanpak heb ik vanzelf alle risico's gevat.
>
> **Kernpunt**: De cyclus-aanpak structureert risico-identificatie maar vervangt het niet. Cliente-specifieke risico's (afhankelijkheid van een dominante klant, complex IFRS-toepassingsdomein, fraude-context, regulatoire druk) overstijgen de standaard-cycli en moeten apart worden ingeschat conform ISA 315.
>
> <small>📖 ISA 315 (herzien-2019) — par. 19 - inzicht in entiteit en omgeving — _norm_</small>

## Accountant-perspectieven

### Auditor structureert planning via cycli

_De externe auditor gebruikt cyclus-analyse in zijn risico-inschatting en bewijsverzameling._

#### 🔍 Auditor

##### 👣 Identificeren significante transactiestromen per cyclus

ISA 315 par. 26 vereist dat de auditor significante transactiestromen, rekeningsaldi en toelichtingen identificeert. Cyclus-analyse is hier het ordenende principe: per cyclus de typische transactiestromen lijsten, met materialiteit-relevante volumes en risico-inschatting per bewering. Output: audit-strategie per cyclus.

<small>📖 ISA 315 (herzien-2019) — par. 26 — _norm_</small>

##### 👣 Cyclus-audit-programma opstellen

Per cyclus een geintegreerd auditprogramma dat (1) ITGC-relevantie inschat, (2) sleutelcontroles toetst (operating effectiveness), (3) cyclus-specifieke gegevensgerichte werkzaamheden plant (detailcontroles, cijferanalyses), (4) cut-off-werkzaamheden rond balansdatum, (5) specifieke risicogerichte werkzaamheden (bv. revenue recognition-focus per ISA 240 par. 26).

<small>📖 ISA 330 — par. 6 - opzet van verdere controlewerkzaamheden — _norm_</small>

### Adviseur structureert ontwerp interne controle per cyclus

_De accountant in adviesopdracht gebruikt cyclus-analyse als ontwerp-structuur._

#### 🧭 Adviseur

##### 👣 Een deelproject per cyclus

Strakke project-structuur: een verantwoordelijke per cyclus, een werkgroep met de relevante operationele managers, een geintegreerd schema voor proces-mapping, risico-identificatie, controle-selectie en documentatie. Prioritering op basis van materialiteit en risico - aankoop en verkoop typisch eerst, gevolgd door voorraad en personeel, tot slot productie (vaak meest complex).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Interne controle als toepassings-kader → [[interne-controle]] _(moet-verwijzen)_
- → COSO-controle-activiteiten per cyclus toegepast → [[coso-framework]] _(moet-verwijzen)_
- → Functiescheiding concreet per cyclus → [[functiescheiding]] _(moet-verwijzen)_
- → Substantive testing per cyclus (externe audit) → [[audit-bewijs]] _(moet-verwijzen)_
- → Cyclus-specifieke applicatiecontroles → [[it-controles]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[interne-controle]]
### `vereist`
- [[coso-framework]] — Cyclus-analyse is de operationele toepassing van de COSO-component 'controle-activiteiten' op de feitelijke bedrijfsprocessen.
- [[functiescheiding]] — Functiescheiding wordt per cyclus concreet ingevuld (besteller versus betaler in aankoop, verkoper versus inning in verkoop, ...).
