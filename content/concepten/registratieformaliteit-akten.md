---
title: "Registratieformaliteit van akten"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
  - regeling
ankers:
  - 2.6.I.A
  - 2.6.I.B
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/registratieformaliteit-akten.json"
---

# Registratieformaliteit van akten

_Procedure_

📅 Gebeurtenis · 📋 Regeling · Anchors: `2.6.I.A` · `2.6.I.B` · Wave: `skeleton-fiscaliteit-klein-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: formaliteit der registratie — **Vertalingen**: fr: formalité d'enregistrement

## Definitie

📖 De registratieformaliteit is de procedure waardoor bepaalde akten verplicht aan een ontvangstkantoor van de Algemene Administratie van de Patrimoniumdocumentatie (federaal) of VLABEL (Vlaanderen) worden aangeboden om geregistreerd te worden. Twee gevolgen: (1) FISCAAL — de toepasselijke registratiebelasting (verkooprecht, schenkbelasting, verdeelrecht, hypotheekrecht, vast recht) wordt geïnd; (2) JURIDISCH — de akte verkrijgt vaste datum (rechtszekerheid + tegenwerpbaarheid aan derden) en wordt opgenomen in het repertorium. Drie categorieën akten: notariële akten (alle), onderhandse akten (sommige — bv. handelshuur, verkoop onroerend goed), gerechtelijke akten (sommige). Termijn standaard 4 maanden voor schenkings-akten + akten over onroerende goederen.

<small>📚 Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 19 — _wettekst_ · Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 32 — _wettekst_</small>

## Substantie

🔗 Praktisch is de notaris de centrale actor bij registratie van notariële akten: hij is wettelijk verplicht de akte ter registratie aan te bieden binnen 15 dagen (notariële akten) of soms binnen 4 maanden (schenkingsakte). De cliënt betaalt aan de notaris die op zijn beurt de registratie regelt + de belasting overmaakt. Voor onderhandse akten ligt de verantwoordelijkheid bij de partijen zelf — typisch bij handelshuren, leasingovereenkomsten, of compromis-akten van verkoop. De accountant kan optreden als gemandateerd vertegenwoordiger om onderhandse akten aan te bieden (volmacht volstaat). Niet-registratie of laattijdige registratie wordt bestraft met een verhoging van het verschuldigd recht (typisch 50-200% — gewest-afhankelijk).

<small>📚 Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 32 — _wettekst_ · Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 41bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Twee samenhangende doelen: (1) fiscaal — de Staat wil zekerheid dat alle belastbare overdrachten worden vastgesteld; zonder registratieplicht kunnen partijen onderhands transacties verbergen; (2) civielrechtelijk — registratie geeft vaste datum + bewijswaarde + tegenwerpbaarheid aan derden, wat essentieel is voor rechtszekerheid in het vermogensverkeer (vooral bij onroerend goed, schenkingen, huurcontracten). De boete bij laattijdige registratie steunt op het belang van tijdige fiscale inning + ontmoediging van uitstelgedrag.

<small>📚 Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 19 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: W.Reg. art. 19-41bis + 161-165 (federaal en regionaal) + VCF Titel 3 hoofdstuk 1 (Vlaanderen)

Stabiel regime. Elektronische registratie is sinds 2018 gefaseerd ingevoerd: notariële akten kunnen via E-registration; onderhandse akten via MyMinFin. Volledige verplichte elektronische registratie voor alle akten uiterlijk 2028 (federaal).

**▶️ Trigger start**
- 📖 De ondertekening van een akte die onderworpen is aan de registratieplicht — typisch bij notariële verlijding, bij ondertekening van een onderhandse compromis-akte of bij een gerechtelijke uitspraak.

## Bouwstenen

### 📜 Registratieplichtige akten  
_`regel`_

📖 Verplicht te registreren binnen welbepaalde termijn: (a) ALLE notariële akten verleden in België (art. 19 W.Reg.); (b) onderhandse akten betreffende verkoop, ruil, schenking, deling van onroerend goed; (c) onderhandse akten van huur, onderverhuur, overdracht van huur van onroerend goed; (d) gerechtelijke beslissingen die overdracht van onroerend goed bevatten; (e) bepaalde commerciële akten (handelshuur). Onderhandse akten over louter roerend goed (bv. een gewone factuur) zijn NIET registratieplichtig — tenzij men ze vrijwillig laat registreren voor de vaste datum.

<small>📚 Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 19 — _wettekst_ · Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 33 — _wettekst_</small>

### 📏 Termijnen voor aanbieding  
_`drempel`_

📖 Notariële akten in België: 15 dagen vanaf ondertekening (W.Reg. art. 32). Onderhandse akten over onroerend goed (verkoop, schenking onroerend, deling, ruil, hypotheek): 4 maanden. Onderhandse huurakten: 4 maanden vanaf datum akte. Schenkingsakten: 4 maanden. Gerechtelijke akten: 4 maanden vanaf datum uitspraak.

<small>📚 Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 32 — _wettekst_</small>

### ⚙️ Repertorium + vaste datum  
_`mechanisme`_

📖 Bij registratie wordt elke akte opgenomen in het 'repertorium' van het registratiekantoor — een chronologisch register dat de akte een vaste datum geeft en haar bestaan officieel maakt. De vaste datum is essentieel voor: (a) tegenwerpbaarheid aan derden (een ongedateerde of post-gedateerde akte is verdacht); (b) berekening van termijnen (bv. 3-jaars-vermoeden art. 7 W.Succ.); (c) volgorde van zekerheidsrechten. Het repertorium is openbaar raadpleegbaar voor partijen + notarissen + advocaten — andere derden alleen mits gerechtvaardigd belang.

<small>📚 Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 175 e.v. — _wettekst_</small>

### 📜 Sancties bij niet- of laattijdige registratie  
_`regel`_

📖 Boete bij laattijdige aanbieding: doorgaans dezelfde grootteorde als het ontdoken recht (50-200%, gewest-afhankelijk). Voor onjuiste opgave van de graad van verwantschap tussen schenker en begiftigde: ondeelbare boete gelijk aan het ontdoken recht (W.Reg. art. 139). Bovenop: nalatigheidsinteresten op het verschuldigd bedrag. Bij volledige niet-aanbieding (= fiscale fraude): strafrechtelijke sancties + administratieve verhoging tot 200%. Notaris die zijn registratieplicht niet nakomt: tuchtrechtelijke aansprakelijkheid + persoonlijke boete.

<small>📚 Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 41bis — _wettekst_ · Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 139 — _wettekst_</small>

### ↪️ Vrijstellingen van de formaliteit  
_`uitzondering`_

📖 Bepaalde akten zijn vrijgesteld van de registratieformaliteit (W.Reg. art. 161-165): bv. authentieke akten verleden in het buitenland en aangeboden ter erkenning, bepaalde fiscale documenten van de Staat, bepaalde gerechtelijke uitspraken (uitvoeringsbevelen, afsluitingen faillissement). Vrijstelling van formaliteit betekent geen vrijstelling van belasting — de belasting kan langs een andere weg verschuldigd zijn. Het 'recht in debet' (art. 159bis Wal / art. 162 federaal) laat toe registratie te krijgen zonder onmiddellijke betaling bij bepaalde gevallen (rechtsbijstand, voorlopige zekerheidsmaatregelen).

<small>📚 Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 161 — _wettekst_ · Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 162 — _wettekst_</small>

## Valkuilen

### ⚠️ Registratie verwarren met inschrijving in hypotheekkantoor

**Verkeerde assumptie**: Een akte 'registreren' en een hypotheek 'inschrijven' zijn hetzelfde.

**Kernpunt**: Registratie (kantoor Patrimoniumdocumentatie/VLABEL) = fiscaal-juridische formaliteit op de akte zelf: vaste datum + heffing van verkooprecht/schenkbelasting/andere rechten. Inschrijving (kantoor Rechtszekerheid, vroeger hypotheekkantoor) = zakelijk-publicitair op het onroerend goed: nodig voor tegenwerpbaarheid van eigendomsoverdracht of hypotheek aan derden. Bij vastgoedoverdracht: eerst registratie (binnen 15 dagen / 4 maanden), daarna pas inschrijving (verzendt notaris naar Rechtszekerheid).

<small>📚 Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 32 — _wettekst_ · Hypotheekwet 16 december 1851 — art. 1 + 90 — _wettekst_</small>

### ⚠️ Onderhandse huurakten 'mogen wachten'

**Verkeerde assumptie**: Een ondertekende huurovereenkomst kan zonder problemen later worden geregistreerd zodra de verhuurder daar tijd voor heeft.

**Kernpunt**: Onderhandse huurakten over onroerend goed zijn registratieplichtig binnen 4 maanden. Niet-geregistreerde huurovereenkomst is niet tegenwerpbaar aan derden (incl. nieuwe eigenaar bij verkoop), wat de huurder zonder bescherming kan laten. Bij geschillen kan de huurder zelf de registratie afdwingen.

<small>📚 Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 33 — _wettekst_</small>

## Accountant-perspectieven

### Vertegenwoordiging bij registratie + administratie

_De accountant treedt als gemandateerd vertegenwoordiger op voor cliënten bij VLABEL of het federaal registratiekantoor — voor aanbieden van akten, attestaanvragen of bezwaarschriften._

#### 👥 Begeleider

##### 👣 Mandaat + volmacht regelen  
_`stap`_

🔗 Voor handelingen ten aanzien van VLABEL of het federaal kantoor: vraag bij elke nieuwe cliënt een schriftelijk mandaat met expliciete bevoegdheid voor 'fiscale vertegenwoordiging registratie- en successierechten'. Algemene volmacht inkomstenbelasting volstaat niet steeds — bezwaarprocedures vereisen specifiek mandaat.

<small>📚 Vlaamse Codex Fiscaliteit — art. 3.4.1.0.1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Termijnbewaking voor onderhandse akten  
_`stap`_

🔗 Voor onderhandse akten waarvan de cliënt zelf instaat voor registratie (handelshuur, leasingovereenkomst, samenwerkingsakkoord met fiscale impact): registreer een agenda-trigger op datum + 4 maanden. Vermijd boete door automatische opvolging.

<small>📚 Wetboek der Registratie-, Hypotheek- en Griffierechten — art. 41bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Concrete rechten (verkoop/verdeel/hypotheek) → [[verkooprecht]] _(moet-verwijzen)_
- → Schenkbelasting bij schenking → [[schenkbelasting]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[registratie-en-successierechten]]
