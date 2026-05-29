---
title: "Ontwerp van interne controle"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.7.VIII
  - 1.7.VIII.A
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/ontwerp-interne-controle.json"
---

_Procedure_ · ook: control design · interne-controle-implementatie · control framework design · uitwerking interne controle

## Definitie

Het ontwerp van interne controle is de methodologische stappen-flow waarmee een onderneming haar interne-controle-systeem opzet, herziet of uitbreidt. Het is een procedurele toepassing van de COSO-componenten op de feitelijke processen van de onderneming, doorgaans in vijf stappen: proces-mapping, risico-identificatie, controle-selectie, documentatie en implementatie. Wordt gebruikt bij het opstarten van een nieuwe onderneming, na een fusie of overname, na een ingrijpende organisatiewijziging, of als remediering na vastgestelde tekortkomingen door interne of externe audit.

<small>🔗 ISA 315 (herzien-2019) — par. 21-26 vijf componenten — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

Ontwerp van interne controle is een design-discipline, geen audit-discipline. De accountant is hier in de rol van adviseur of begeleider, niet van controleur. Hij vertrekt van de feitelijke processen van de cliente (vaak nog niet of slechts informeel beschreven), brengt ze in kaart, identificeert de risicopunten en stelt geschikte controles voor. De kwaliteit van het ontwerp wordt door externe auditors later getoetst via design effectiveness (is de controle theoretisch geschikt) en operating effectiveness (werkt de controle ook in de praktijk).

<small>🔗 ISA 330 — par. 8 verschil design effectiveness vs operating effectiveness — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Een goed ontworpen interne controle is veel goedkoper en doeltreffender dan een ad-hoc-stelsel dat groeit door reactieve fixes na incidenten. Voor de cliente: lagere kans op verliezen door fouten of fraude, snellere en goedkopere externe controle. Voor de externe auditor: een controleerbare basis. Voor de wetgever: een vereiste van zorgvuldig bestuur (bestuurdersaansprakelijkheid art. 2:56 WVV).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege`

Ontwerpmethodologie is geen wettelijke procedure maar een professionele praktijk, gebaseerd op COSO en ISA 315. Steeds toepasbaar.

**✅ Voor**
- 🔗 Opstart van een nieuwe onderneming, na fusie of overname, na ingrijpende organisatiewijziging (nieuwe IT-systemen, nieuwe bedrijfslijn), of als remediering na auditbevindingen.

**▶️ Trigger start**
- 🔗 Significante tekortkomingen gerapporteerd door de externe auditor (management letter, ISA 265), opening nieuwe vestiging of dochter, implementatie nieuw ERP-systeem, antiwitwas-verplichting voor onderworpen entiteiten, eerste keer commissaris aanstellen bij overschrijden van groottecriteria.

## Bouwstenen

### 👣 Stap 1 - Proces-mapping en as-is-analyse

Per cyclus (verkoop, aankoop, voorraad, personeel, treasury, vaste activa) worden de actuele processen in kaart gebracht: wie doet wat, in welke volgorde, met welke documenten en welke IT-systemen. Resultaat: flowcharts, narratives of process descriptions per cyclus. Eventueel walk-through-tests om de mapping te valideren. Hiermee wordt de as-is-toestand vastgelegd vooraleer over remediering wordt nagedacht.

<small>🔗 ISA 315 (herzien-2019) — par. 25 informatiesysteem en bedrijfsprocessen — _norm_</small>

### 👣 Stap 2 - Risico-identificatie per processtap

Per processtap worden de risico's geinventariseerd: wat kan er fout gaan? Veelgebruikte categorieen: foutieve invoer, ontbrekende boeking, dubbele boeking, ongeautoriseerde transactie, fraude, IT-storing, niet-naleving van wet- en regelgeving. Voor de financiele rapportering wordt teruggekoppeld naar de assertions (volledigheid, juistheid, bestaan, waardering, toerekening, presentatie). De methodologie volgt ISA 315 (risico-identificatie op niveau beweringen) - ook al gebeurt het ontwerp niet door de auditor.

<small>📖 ITAA-norm-kmo-controlenorm — par. 74 - risico-identificatie op niveau financiele overzichten en beweringen — _norm_ · ISA 315 (herzien-2019) — par. 28 - risico's identificeren via beweringen — _norm_</small>

### 👣 Stap 3 - Controle-selectie per risico

Per geidentificeerd risico wordt een geschikte controle gekozen langs drie assen: (a) preventief versus detectief versus correctief; (b) manueel versus geautomatiseerd (geprefereerd waar mogelijk - reproduceerbaar, audit-trail); (c) sleutelcontrole (key control - dekt majeur risico) versus aanvullende controle (compensating - secundair). Voor majeure risico's gelden vaak meerdere lagen (defense in depth).

<small>📖 ISA 315 (herzien-2019) — Bijlage 3 - interne beheersingsactiviteiten en general IT controls — _norm_</small>

### 👣 Stap 4 - Documentatie in procedures, rolbeschrijvingen en autorisatiematrix

De geselecteerde controles worden geformaliseerd in drie complementaire documenten: (1) procedures - wat moet er stap voor stap gebeuren; (2) rolbeschrijvingen - wie is verantwoordelijk voor welke stap; (3) autorisatiematrix - welke functie mag welke transactie tot welk bedrag goedkeuren. Documentatie is essentieel: zonder geschreven procedures kan een externe auditor geen design effectiveness toetsen en kan de onderneming de werking niet bewijzen bij een fiscale of regelgevende controle.

<small>📖 ITAA-norm-kmo-controlenorm — par. 43 - documentatie aangepast aan omvang en aard — _norm_</small>

### 👣 Stap 5 - Implementatie, training en monitoring

De gedocumenteerde procedures worden uitgerold: kick-off-training, integratie in IT-systemen (workflow, autorisatie-instellingen), aanpassing van handtekenmandaten bij de bank, periodieke awareness-sessies. Monitoring sluit de cirkel: een interne audit of accountant toetst periodiek of de controles ook effectief werken (operating effectiveness). Resultaat van de monitoring voedt een nieuwe ontwerpiteratie - interne controle is doorlopend, niet eenmalig.

<small>🔗 ISA 315 (herzien-2019) — par. 24 monitoring-component — _norm_</small>

### 💡 Design effectiveness versus operating effectiveness

Design effectiveness antwoordt op de vraag: zou de controle, indien correct uitgevoerd, het beoogde risico afdekken? Operating effectiveness antwoordt op: wordt de controle ook effectief uitgevoerd zoals ontworpen? Bij ontwerp van interne controle gaat het vooral over design; bij evaluatie door de externe auditor (ISA 330) komt operating effectiveness erbij. Een controle kan design-effectief maar operating-ineffectief zijn (procedure is goed maar wordt niet gevolgd) - en omgekeerd kan operating-ineffectiviteit een design-tekortkoming verbergen.

<small>📖 ISA 330 — par. 8 — _norm_</small>

### 🧭 Schaalbaarheid naar kmo-context

Voor een kmo wordt de methodologie schaalbaar toegepast: minder formele flowcharts (eenvoudige narratives volstaan), minder controles maar wel de sleutelcontroles, autorisatiematrix in een eenvoudige tabel. ISA 315 par. A156 erkent expliciet dat de inhoud van de componenten vergelijkbaar is met grotere entiteiten, alleen de mate van formaliteit verschilt.

<small>📖 ISA 315 (herzien-2019) — par. A156 schaalbaarheid — _norm_</small>

## Valkuilen

> [!warning]- Ontwerp door auditor in plaats van door management
> **Verkeerde assumptie**: De externe auditor mag de interne controle van zijn cliente ontwerpen en achteraf controleren.
>
> **Kernpunt**: De verantwoordelijkheid voor opzet en werking van interne controle ligt bij het management (ISA 200). De auditor mag adviseren bij ontwerp, maar nooit beslissingen nemen voor het management - anders ontstaat een onafhankelijkheidsprobleem (self-review threat in IESBA-Code). Splitsing taken in het kantoor is dan vereist.
>
> <small>🔗 ISA 200 — Algemene doelstellingen - verantwoordelijkheidsverdeling auditor/management — _norm_</small>

> [!warning]- Eenmalig ontwerp zonder updates
> **Verkeerde assumptie**: Eens de procedures opgeschreven zijn is het werk gedaan.
>
> **Kernpunt**: Interne controle is doorlopend, niet eenmalig. Bij elke ingrijpende wijziging (nieuw ERP, fusie, nieuwe bedrijfsactiviteit, wetswijziging) moet het ontwerp opnieuw geevalueerd worden. Een procedure-handboek dat drie jaar niet aangepast is verliest snel zijn relevantie - en zijn audit-waarde.
>
> <small>🔗 ISA 315 (herzien-2019) — par. 24 monitoring — _norm_</small>

> [!warning]- Geen prioritering: alle risico's evenwaardig behandelen
> **Verkeerde assumptie**: Elk geidentificeerd risico krijgt zijn eigen controle.
>
> **Kernpunt**: Risico-prioritering is essentieel: niet elk risico verdient een eigen controle (kosten-baten). Focus op de significante risico's (ISA 315) en op de risico's met grootste impact x grootste waarschijnlijkheid. Voor lage risico's volstaat soms een algemene oversight-controle.
>
> <small>🔗 ISA 315 (herzien-2019) — par. 32 significante risico's — _norm_</small>

## Accountant-perspectieven

### Adviesopdracht ontwerp interne controle bij cliente

_De accountant in een adviesopdracht voor het opzetten of herzien van het interne-controle-systeem van een cliente._

#### 🧭 Adviseur

##### 👣 Het vijfstappenproject leiden

De accountant begeleidt het management door de vijf stappen: workshops voor proces-mapping met afdelingshoofden, risico-brainstorm met sleutelfiguren, voorstellen voor controles (incl. quick wins en lange-termijn-investeringen), opstellen van templates voor procedures en autorisatiematrix, begeleiding bij implementatie en eerste interne reviews.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 📜 Onafhankelijkheid bewaken indien ook auditor

Indien hetzelfde kantoor de externe controle uitvoert: ontwerpadvies geven kan een self-review threat creeren. Mitigatie: andere ploeg, kwaliteits-review, in extreme gevallen weigering van de adviesopdracht. Bij audit van publieke entiteiten of beursgenoteerde ondernemingen is ontwerp van interne controle door de commissaris meestal niet toegestaan.

<small>🔗 ITAA-norm-intern-kwaliteitsmanagement — ISQM 1 - onafhankelijkheid bij niet-controle-opdrachten — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 👥 Begeleider

##### 👣 Training en awareness bij personeel

Procedures op papier hebben pas effect als ze gekend en aanvaard zijn. De accountant begeleidt kick-off-sessies per afdeling, levert e-learning-content voor nieuwe medewerkers en organiseert opfrissessies. Tone at the top is cruciaal: visible support van zaakvoerder of CEO bepaalt of medewerkers de procedures ernstig nemen.

<small>🔗 ISA 315 (herzien-2019) — par. 21 controleomgeving en tone at the top — _norm_</small>

## Verder lezen (scope-out)

- → Interne-controle-kader (parent) → [[interne-controle]] _(moet-verwijzen)_
- → COSO-componenten als input → [[coso-framework]] _(moet-verwijzen)_
- → Cyclus-toepassing → [[cyclus-analyse]] _(moet-verwijzen)_
- → Functiescheiding als kerntechniek → [[functiescheiding]] _(moet-verwijzen)_
- → Evaluatie van interne controle (audit-kant - design vs operating effectiveness) → [[evaluatie-interne-controle]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[interne-controle]]
### `vereist`
- [[coso-framework]] — De vijf COSO-componenten leveren de ontwerp-input voor elke stap.
- [[functiescheiding]] — Functiescheiding is doorgaans de eerste en belangrijkste sleutelcontrole bij ontwerp.
### `triggert`
- [[evaluatie-interne-controle]] — Elk ontwerp wordt achteraf getoetst op design effectiveness en operating effectiveness.
