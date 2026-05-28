---
title: "Opmaak van geconsolideerde jaarrekening"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
ankers:
  - 1.4.I.F
  - 1.4.taak.1
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/opmaak-geconsolideerde-jaarrekening.json"
---

# Opmaak van geconsolideerde jaarrekening

_Procedure_

📅 Gebeurtenis · Anchors: `1.4.I.F` · `1.4.taak.1` · Wave: `skeleton-consolidatie-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: consolidatie-opmaak · consolidation process

## Definitie

📖 De opmaak van een geconsolideerde jaarrekening is het procedureel proces waarbij de moedervennootschap de jaarrekeningen van alle entiteiten in de consolidatiekring samenbrengt tot één set financiële overzichten die de groep als economische eenheid presenteren. Volgens art. 3:31 KB WVV moet de geconsolideerde jaarrekening worden opgesteld binnen zes maanden na balansdatum en worden onderworpen aan controle door de commissaris vóór ze aan de algemene vergadering wordt voorgelegd. Het resultaat bestaat uit: geconsolideerde balans + geconsolideerde resultatenrekening + geconsolideerde toelichting (en bij IFRS ook geconsolideerd overzicht totaalresultaat + EV-mutatieoverzicht + kasstroomoverzicht) + geconsolideerd jaarverslag.

<small>📚 KB WVV — art. 3:31 — _kb_ · KB WVV — art. 3:103 — _kb_ · KB WVV — art. 3:107 — _kb_</small>

## Substantie

🔗 In de praktijk is de opmaak een gestructureerd proces met meerdere fasen, meestal aangestuurd door een centraal consolidatiebureau (consolidation department) binnen de moeder. Het bureau verstuurt aan elke dochter een rapporteringspakket (reporting package) met groepsdefinities, koersen, klantcoderingen en deadlines; ontvangt de individuele jaarrekeningen terug; harmoniseert (uniforme waarderingsregels + omrekening buitenlandse dochters); voegt samen volgens de gekozen consolidatiemethode (integraal/evenredig/vermogensmutatie); en elimineert intercompany-transacties. Elke stap wordt gedocumenteerd in werkdocumenten met audit-traceability. Het tijdspad is strak: jaarrekening dochters moet typisch al binnen 60 dagen na balansdatum afgeleverd zijn, opdat de groep ruim voor de 6-maandsdeadline (art. 3:31) klaar is.

<small>📚 ISA 600 — par. A23 + Bijlage 2 — _norm_ · ITAA-norm-algemene-controlenorm — par. 4 Werkdocumenten — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Ratio: een goed gestructureerd consolidatieproces is de enige manier om de groepsdimensie van complexe transacties (intercompany-leveringen, intra-groep-financiering, herallocaties) consistent en getrouw weer te geven. Zonder centrale aansturing zijn afwijkingen in waarderingsregels, asynchroniteit in balansdata, en niet-geëlimineerde intercompany-saldi onvermijdelijk — de geconsolideerde jaarrekening verliest dan haar voorspellende waarde voor schuldeisers en investeerders. De 6-maanden-termijn beoogt actualiteit voor de gebruikers.

<small>📚 KB WVV — art. 3:31 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: KB 29-04-2019 ter uitvoering WVV, art. 3:31, 3:103-3:107

Standaardprocedure voor alle consolidatieplichtige groepen onder Belgisch recht. Voor beursgenoteerde groepen: aanvullend IAS 27 (geconsolideerde jaarrekening — single-entity-versie) en IFRS 10.

## Bouwstenen

### 👣 Stap 1 — Bepaling consolidatiekring  
_`stap`_

📖 Identificeer welke entiteiten in de consolidatie opgenomen worden: dochterondernemingen (controle, art. 1:14), gezamenlijke dochters (gezamenlijke controle, art. 1:18), geassocieerde ondernemingen (notabele invloed, art. 1:20). Bepaal per entiteit de toe te passen methode (integraal/evenredig/VMM). Documenteer wijzigingen t.o.v. vorige periode (instroom + uitstroom).

<small>📚 KB WVV — art. 1:14 — _kb_ · KB WVV — art. 1:18 — _kb_ · KB WVV — art. 1:20 — _kb_</small>

### 👣 Stap 2 — Versturen rapporteringspakket aan dochters  
_`stap`_

📖 Het consolidatiebureau verstuurt aan elke dochter een rapporteringspakket met: (1) groeps-rekeningenstelsel + mapping-instructies; (2) uniforme waarderingsregels (afschrijvingsmethodes, voorraadwaardering, voorzieningenbeleid); (3) deadlines voor levering (typisch 30-60 dagen na balansdatum); (4) intercompany-confirmatie-matrices (saldi en transacties); (5) wisselkoersen (slotkoers + gemiddelde koers); (6) lijst van significante events na balansdatum die te rapporteren zijn. De norm 'uniforme grondslagen voor financiële verslaggeving' (ISA 600 Bijlage 2) is hier het kerninstrument.

<small>📚 ISA 600 — Bijlage 2 — Consolidatieproces — _norm_</small>

### 👣 Stap 3 — Harmonisatie (waarderingsregels + valuta)  
_`stap`_

📖 Pre-consolidatie-aanpassingen op elke dochter-jaarrekening: (1) waarderingsregels uniformiseren (art. 3:117 KB WVV) — verschillen in lokale GAAP, afschrijvingsmethoden, voorzieningenbeleid wegwerken; (2) omrekening buitenlandse dochters naar groepspresentatiemunt (current-rate of temporal); (3) reclassificaties tussen rubrieken voor consistente groepspresentatie. Elke aanpassing geboekt in 'consolidatieboek' (apart van statutaire boekhouding dochter), met source-document en motivatie.

<small>📚 KB WVV — art. 3:117 — _kb_</small>

### 👣 Stap 4 — Samenvoegen volgens methode  
_`stap`_

📖 Per entiteit toepassen van de gekozen methode: integraal → 100 %-opname + eliminatie deelneming tegen EV-aandeel + consolidatieverschil + minderheidsbelang; evenredig → pro-rata-opname; VMM → één-regel-deelneming met aandeel in resultaat. Resultaten samenvoegen tot eerste versie groepsbalans + groeps-RR.

<small>📚 KB WVV — art. 3:131 — _kb_ · KB WVV — art. 3:139 — _kb_ · KB WVV — art. 3:140 — _kb_</small>

### 👣 Stap 5 — Intercompany-eliminaties  
_`stap`_

📖 Matching en eliminatie van intercompany-vorderingen + schulden (cross-confirmatie tussen dochters); intercompany-omzet + aankopen; niet-gerealiseerde winsten in voorraden + vaste activa (intercompany-marge die nog niet aan derden is gerealiseerd); intra-groep-dividenden. Verschillen tussen matching-partijen (timing-verschillen, intransit-goederen, valuta-discrepanties) worden geanalyseerd en opgelost vóór finale consolidatie.

<small>📚 KB WVV — art. 3:135 — _kb_ · ISA 600 — Bijlage 2 — _norm_</small>

### 👣 Stap 6 — Opmaak toelichting + jaarverslag  
_`stap`_

📖 Geconsolideerde toelichting bevat o.a. (art. 3:103 e.v. KB WVV): consolidatiekring + wijzigingen tijdens jaar, gehanteerde consolidatiemethoden, waarderingsregels groepsniveau, segmentinformatie, buitenbalanstoezeggingen, transacties met verbonden partijen, beloning bestuurders. Geconsolideerd jaarverslag (apart document, art. 3:32 WVV) beschrijft activiteiten + risico's groepsniveau. Beide worden samen gepubliceerd.

<small>📚 KB WVV — art. 3:103 — _kb_ · KB WVV — art. 3:107 — _kb_</small>

### 👣 Stap 7 — Commissaris-controle + publicatie  
_`stap`_

📖 De groepscommissaris (ISA 600) onderwerpt de geconsolideerde jaarrekening aan een controle en levert een controleverslag. AVA keurt geconsolideerde jaarrekening goed (tegelijk met statutaire jaarrekening moeder). Neerlegging bij NBB binnen 30 dagen na goedkeuring AV, maximaal 7 maanden na balansdatum (art. 3:10 KB WVV).

<small>📚 KB WVV — art. 3:10 — _kb_ · ISA 600 — par. A23 — _norm_</small>

## Valkuilen

### ⚠️ Verschillende balansdata dochter vs moeder

**Verkeerde assumptie**: Een dochter met boekjaar afsluitend 30/9 kan 'gewoon' geconsolideerd worden in de moeder per 31/12.

**Kernpunt**: Art. 3:121 KB WVV: balansdata moeten samenvallen, of een dochter sluit een tussentijdse balans af op de groepsdatum, of als het verschil ≤3 maanden bedraagt, dan mag de dochter-jaarrekening per haar eigen balansdatum gebruikt worden mits aanpassingen voor significante transacties tussen die data. >3 maanden → tussenbalans verplicht.

<small>📚 KB WVV — art. 3:121 — _kb_</small>

### ⚠️ Audit-traceability vergeten (werkdocumenten)

**Verkeerde assumptie**: Consolidation-spreadsheets zijn 'het bewijs' van de consolidatie.

**Kernpunt**: ITAA-controlenorm + ISA 230: werkdocumenten moeten een ervaren auditor zonder voorkennis toelaten om de uitgevoerde werkzaamheden en getrokken conclusies te begrijpen. Excels met formules zonder bron-document-trail, eliminatie-boekingen zonder verantwoording, manuele topside-aanpassingen zonder management-approval = audit-failure-risico's. Iedere aanpassing in het consolidatieboek krijgt een journaal-nummer + source-doc + approver.

<small>📚 ITAA-norm-algemene-controlenorm — par. 4 — _norm_ · ISA 600 — Bijlage 2 — _norm_</small>

## Accountant-perspectieven

### Consolidatieverantwoordelijke / -bureau

_De accountant binnen de moeder die het consolidatieproces aanstuurt._

#### 📒 Boekhouder

##### 🧭 Opzet consolidatiebureau  
_`vuistregel`_

🔗 Voor groepen >5 entiteiten: rechtvaardigt een centraal consolidatiebureau. Verantwoordelijkheden: uniformeren rapporteringspakket; valideren input van dochters (sanity-checks aansluiting EV, aansluiting saldi vorig jaar); uitvoeren consolidatie-aanpassingen; opmaak toelichtingen; bewaring werkdocumenten 10 jaar. Software-keuze: dedicated consolidation tools (LucaNet, Tagetik, OneStream, SAP BPC) reduceren manueel werk + verbeteren audit-trail t.o.v. Excel-only.

<small>📚 ISA 600 — Bijlage 2 — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 ISA 600 — werkdocumenten + groepsonderdelen-audit  
_`stap`_

📖 De groepsauditor verwerft inzicht in (a) het consolidatieproces — handmatige + geautomatiseerde stappen, interne beheersing op consolidatie-aanpassingen, omrekenings-procedure buitenlandse dochters; (b) significante groepsonderdelen — eigen audit of werk van component-auditors; (c) intra-groepstransacties — matching + eliminatie. Werkdocumenten ISA 230: ervaren auditor zonder voorkennis moet de werkzaamheden + conclusies kunnen volgen.

<small>📚 ISA 600 — par. A23 + Bijlage 2 — _norm_ · ITAA-norm-algemene-controlenorm — par. 4 — _norm_</small>

## Verder lezen (scope-out)

- → Geconsolideerd jaarverslag (apart document) → [[geconsolideerd-jaarverslag]] _(moet-verwijzen)_
- → Eliminatie-intercompany (sub-stap) → [[eliminatie-intercompany]] _(moet-verwijzen)_
- → Uniforme waarderingsregels (input-stap) → [[uniforme-waarderingsregels-consolidatie]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[geconsolideerde-jaarrekening]]
### `vereist`
- [[uniforme-waarderingsregels-consolidatie]]
- [[consolidatiekring]]
### `triggert`
- [[eliminatie-intercompany]]
