---
title: "Interne audit"
concept_type: "actor"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
  - kader
ankers:
  - 1.7.I.D
  - 1.7.V
  - 1.7.V.A
  - 1.7.V.B
tags:
  - concept
  - schema-2.2
  - type-actor
  - cat-entiteit
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/interne-audit.json"
---

# Interne audit

_Actor_

🏢 Entiteit · 🏛️ Kader · Anchors: `1.7.I.D` · `1.7.V` · `1.7.V.A` · `1.7.V.B` · Wave: `cluster-extract-controle-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: internal audit · third line of defense · interne auditfunctie · interne controleurs — **Vertalingen**: fr: audit interne

## Definitie

📖 Interne audit is een onafhankelijke en objectieve beoordelingsfunctie die binnen een organisatie wordt opgezet om de werking van het interne-controle-systeem, het risicomanagement en de governance kritisch te toetsen. De interne auditor is werknemer of vertegenwoordiger van de onderneming zelf, maar rapporteert onafhankelijk aan het auditcomite of het bestuursorgaan - niet aan het uitvoerend management dat hij controleert. Volgens het Three-Lines-of-Defense-model is interne audit de derde lijn, na het operationeel management (eerste lijn) en de risk- en compliance-functies (tweede lijn).

<small>📚 ISA 315 (herzien-2019) — Bijlage 4 - interne audit als monitoringactiviteit — _norm_ · ISA 610 (herzien) — par. 14 - gebruikmaken van werkzaamheden interne audit functie — _norm_</small>

## Substantie

🔗 Een interne-audit-functie is geen wettelijke verplichting voor de meeste Belgische ondernemingen - alleen bij beursgenoteerde ondernemingen, kredietinstellingen en verzekeraars verplicht in de bedrijfsstructuur. Bij andere grote ondernemingen vaak opgezet als een stafdienst van enkele tot tientallen mensen onder leiding van een Chief Audit Executive (CAE) die hierarchisch onder de CEO valt voor administratieve aspecten maar functioneel rapporteert aan het auditcomite. Internationaal aanvaard normenkader: de International Standards for the Professional Practice of Internal Auditing van het Institute of Internal Auditors (IIA). Voor de externe auditor: een goed werkende interne audit kan een belangrijke bron van bewijs zijn (ISA 610) en de scope van externe controle aanzienlijk inperken.

<small>📚 ISA 610 (herzien) — Toepassingsgebied en doelstellingen — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De ratio voor een interne-audit-functie is governance-economisch: het bestuursorgaan kan zonder onafhankelijke informatiebron niet weten of het uitvoerend management daadwerkelijk doet wat het rapporteert. Externe audit komt te laat (jaarlijks, beperkt tot financiele rapportering) en is te duur voor doorlopende monitoring. Interne audit vult dat gat: continue, gerichte, op risico gebaseerde monitoring die rechtstreeks rapporteert aan toezichtsniveau. Voor bestuurders is een interne-audit-functie ook een aansprakelijkheidsmitigatie - art. 2:56 WVV stelt zorgvuldigheidsplicht; een toezicht-mechanisme aanwezig hebben is een element van die zorgvuldigheid.

<small>📚 WVV — art. 2:56 - bestuurdersaansprakelijkheid — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege`

Verplicht voor beursgenoteerde ondernemingen (Belgische Corporate Governance Code), kredietinstellingen (NBB-circulaire), verzekeraars (FSMA). Optioneel maar gangbaar in grote ondernemingen en organisaties met complexe risico-profielen.

**✅ Voor**
- 🔗 Ondernemingen met voldoende omvang, complexiteit of regulatorische druk om een interne-audit-functie te rechtvaardigen. Typische triggers: beursnotering, financiele-sector-vergunning, omzet boven 50 miljoen EUR met meerdere vestigingen, hoge cyber-risico-blootstelling, governance-vereisten bij overheidsondernemingen.

**👍 Voordeel**
- 🔗 Onafhankelijke assurance voor bestuursorgaan, vroegtijdige detectie van risico's en fraude, voortdurende verbetering van interne controle via aanbevelingen, scope-reductie voor externe audit (kostenefficiente), zorgvuldigheidsplicht-mitigatie voor bestuurders, hogere kwaliteit financiele rapportering.

**⚠️ Risico**
- 📖 Verlies van onafhankelijkheid wanneer interne audit operationele taken op zich neemt (bv. zelf controles uitvoeren die ze achteraf zou moeten toetsen). Te beperkt budget of personeel waardoor risico-gebaseerde planning niet realiseerbaar is. Druk van het management op de bevindingen (verzachten, niet rapporteren naar auditcomite). Slechte tone at the top - als het bestuur niet luistert naar de interne auditor verliest de functie haar effect.

## Bouwstenen

### 💡 Audit charter (intern auditreglement)  
_`begrip`_

🔗 Het formele document dat het mandaat, de autoriteit, de verantwoordelijkheid en de onafhankelijkheid van de interne-audit-functie vastlegt. Goedgekeurd door het auditcomite of het bestuursorgaan. Bevat typisch: scope (alle activiteiten van de groep, inclusief dochters), toegangsrechten (onbeperkte toegang tot alle gegevens en personen), rapporteringslijn (functioneel aan auditcomite, administratief aan CEO), middelen (budget, FTE-aantal), kwaliteitsstandaarden (IIA-standards), evaluatie-mechanisme (jaarlijkse externe assessment elke vijf jaar).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 👣 Risico-gebaseerd auditplan  
_`stap`_

🔗 Jaarlijks of meerjarig auditplan opgesteld op basis van risico-inschatting van alle business-units en processen. Hoge risico's krijgen prioriteit; lage risico's volstaan met een audit elke drie tot vijf jaar. Het plan wordt aan het auditcomite voorgelegd ter goedkeuring. Tussentijds kan worden aangepast bij wijzigingen in risico-profiel of bij speciale verzoeken van management of auditcomite (special investigations).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 👣 Cyclus van een interne audit  
_`stap`_

🔗 Per audit-opdracht doorloopt de interne auditor een vaste cyclus: (1) scoping en planning, (2) opening meeting met auditee, (3) field work met testing van controles en gesprekken, (4) draft-rapport met bevindingen en aanbevelingen, (5) closing meeting met auditee om feedback en management response te krijgen, (6) finale rapport aan auditcomite, (7) follow-up van implementatie van aanbevelingen (cruciaal - een audit zonder follow-up verliest impact).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Afbakening tegenover externe audit  
_`mechanisme`_

📖 Externe audit (commissaris, gecertificeerd accountant) is wettelijk verplicht voor entiteiten boven de groottecriteria en geeft een wettelijk assurance-oordeel over de jaarrekening aan derden (aandeelhouders, crediteuren, fiscus). Interne audit is bedrijfsintern, vrijwillig (tenzij voor specifieke sectoren), geeft geen wettelijk oordeel maar wel rapportering aan het bestuur, en heeft een veel breder onderwerpenpalet (niet alleen financiele rapportering maar ook operationele efficientie, compliance, IT, fraude-onderzoek). De externe auditor kan steunen op het werk van interne audit (ISA 610) maar behoudt zijn eigen verantwoordelijkheid voor het oordeel.

<small>📚 ISA 610 (herzien) — par. 5 - relatie tot werkzaamheden onafhankelijke auditor — _norm_</small>

### ⚙️ Afbakening tegenover compliance-functie  
_`mechanisme`_

🔗 Compliance is een tweede-lijn-functie die actief monitort dat de onderneming voldoet aan wet- en regelgeving (antiwitwas, GDPR, fiscaal, sectorregels). Interne audit is een derde-lijn-functie die periodiek beoordeelt of compliance zelf goed werkt. Verschillende positie: compliance werkt mee aan de naleving (operationeel), interne audit oordeelt erover (oversight).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Externe auditor steunt op interne audit (ISA 610)  
_`regel`_

📖 ISA 610 (herzien) regelt onder welke voorwaarden de externe auditor mag steunen op werkzaamheden van de interne-audit-functie. Drie criteria: (a) objectiviteit (organisatorische status en interne-audit-charter), (b) bekwaamheid (kwalificaties van de interne auditors), (c) gestructureerde aanpak (kwaliteitscontrole en documentatie). Indien voldaan: externe auditor kan specifieke werkzaamheden of bevindingen van interne audit gebruiken als controle-informatie. Bij significante risico's of bij hoge subjectiviteit niet aanbevolen.

<small>📚 ISA 610 (herzien) — par. 15-17 — _norm_</small>

### 📜 Verplichting in financiele sector en beursgenoteerden  
_`regel`_

📖 Voor kredietinstellingen, beursvennootschappen en verzekeraars is een onafhankelijke interne-audit-functie wettelijk verplicht (NBB-circulaires, Wet op het toezicht op de financiele sector, Solvency II). Voor beursgenoteerde ondernemingen verwacht de Belgische Corporate Governance Code (2020) dat ofwel een interne-audit-functie ofwel een gemotiveerde alternatieve regeling bestaat (comply or explain). Het auditcomite (verplicht in beursgenoteerden via art. 7:99 WVV) heeft een specifieke taak om toezicht te houden op de interne-audit-functie.

<small>📚 WVV — art. 7:99 - auditcomite — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Interne audit zelf controles laten uitvoeren

**Verkeerde assumptie**: De interne auditor kan ook helpen bij het opzetten en uitvoeren van controles.

**Kernpunt**: Wie controles uitvoert mag ze niet auditen - dat is een self-review threat. Interne audit moet objectief blijven; operationele controle-uitvoering is een eerste- of tweede-lijn-taak. Indien een interne auditor tijdelijk een operationele rol heeft opgenomen, moet hij minstens een jaar wachten vooraleer hij dat domein opnieuw kan auditen (IIA-Standaard 1130.A1).

<small>📚 ISA 610 (herzien) — par. 15(a) objectiviteit — _norm_</small>

### ⚠️ Interne audit verwarren met commissaris

**Verkeerde assumptie**: De interne auditor controleert de jaarrekening.

**Kernpunt**: De interne auditor geeft geen wettelijk assurance-oordeel over de jaarrekening. Die rol is wettelijk voorbehouden aan de commissaris (extern, ITAA-bedrijfsrevisor) bij entiteiten die boven de groottecriteria gaan. Interne audit kan wel componenten van de financiele rapportering toetsen, maar publiceert geen verklaring voor derden.

<small>📚 ISA 610 (herzien) — par. 5 — _norm_</small>

### ⚠️ Externe auditor steunt blindelings op interne audit

**Verkeerde assumptie**: Als er een interne-audit-rapport is, hoeft de externe auditor het werk niet meer over te doen.

**Kernpunt**: Steunen op interne audit kan alleen na evaluatie van objectiviteit en bekwaamheid (ISA 610 par. 15). Bij significante risico's of subjectieve waardering (bv. goodwill-impairment) is steunen op interne audit niet aanbevolen. De externe auditor blijft eindverantwoordelijk voor zijn oordeel en moet dat documenteren.

<small>📚 ISA 610 (herzien) — par. 15-17 — _norm_</small>

## Accountant-perspectieven

### Externe auditor evalueert interne audit van cliente

_De auditor die in de planningsfase moet inschatten of hij op de interne-audit-functie kan steunen._

#### 🔍 Auditor

##### 👣 Evaluatie objectiviteit en bekwaamheid (ISA 610)  
_`stap`_

📖 Bestudeer het audit charter, de rapporteringslijn, de kwalificaties van de Chief Audit Executive en zijn team, de IIA-conformiteit, de externe kwaliteitsbeoordeling (verplicht elke vijf jaar). Op basis daarvan: ja of nee steunen, en zo ja voor welke domeinen en in welke mate. Documenteer het oordeel in het audit-dossier.

<small>📚 ISA 610 (herzien) — par. 15-17 — _norm_</small>

##### 👣 Gebruik van specifieke werkzaamheden van interne audit  
_`stap`_

📖 Bij gunstige evaluatie: review van specifieke interne-audit-rapporten en werkpapieren voor de domeinen waar de externe auditor wil steunen. Voor sommige werkzaamheden kan ISA 610 par. 31 een direct gebruik (direct assistance) toestaan: de interne auditor voert onder supervisie van de externe auditor specifieke werkzaamheden uit (vooraf afgestemd, geen significant subjectief oordeel vereist). Bij significante risico's: geen direct assistance toegestaan.

<small>📚 ISA 610 (herzien) — par. 27-34 direct assistance — _norm_</small>

### Interne auditor in de organisatie

_De interne auditor zelf - kan ook een ITAA-beroepsbeoefenaar zijn (bv. via outsourcing-opdracht)._

#### 🔍 Auditor

##### 📜 Onafhankelijkheid en objectiviteit bewaken  
_`regel`_

🔗 Concreet: rapportering aan auditcomite (niet aan operationeel management); geen operationele taken in de domeinen die geaudit worden; rotatie van auditteams; verklaring van geen belangenconflict per opdracht; voldoende budget en toegang (vastgelegd in audit charter); externe kwaliteitsreview elke vijf jaar.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Interne controle als toetsings-object → [[interne-controle]] _(moet-verwijzen)_
- → Auditcomite als rapporteringslijn → [[auditcomite]] _(moet-verwijzen)_
- → Externe accountant kan steunen via ISA 610 → [[controleopdracht]] _(moet-verwijzen)_
- ↪ Intern kwaliteitsmanagement als parallel kwaliteits-concept voor externe-audit-firms → [[kwaliteitsmanagement-opdracht]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[interne-controle]] — Interne audit is een specifieke functie (derde lijn) binnen het bredere systeem van interne controle.
### `gecontroleerd_door`
- [[auditcomite]] — Functioneel rapporteert interne audit aan het auditcomite (verplicht in beursgenoteerden via art. 7:99 WVV).
### `vergelijkbaar_met`
- [[controleopdracht]]
    - **Gelijkenissen**:
        - Beide zijn audit-werk in de breedste zin
        - Beide vereisen onafhankelijkheid en objectiviteit
        - Beide hanteren een gestructureerde aanpak (planning, fieldwork, rapport)
        - Beide gebruiken risico-gebaseerde scoping
    - **Verschillen**:
        - Interne audit: werknemer of vertegenwoordiger van de onderneming, rapportering intern aan auditcomite, geen wettelijk assurance-oordeel naar derden, breder onderwerpenpalet (ook operationeel, IT, compliance, fraude)
        - Externe controleopdracht: onafhankelijke externe partij (commissaris, gecertificeerd accountant), wettelijk assurance-oordeel over jaarrekening publiek voor aandeelhouders en derden, scope beperkt tot financiele rapportering, ISA-normenkader
        - Interne audit volgt IIA-standards; externe audit volgt ISA + ITAA-normen
    - ⚠️ **Verwarringsrisico**: Studenten gebruiken 'audit' vaak los voor beide functies. Vraag altijd: rapporteert deze auditor intern (interne audit) of extern aan derden (commissaris/externe audit)? En heeft hij een wettelijke assurance-rol?
