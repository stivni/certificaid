---
title: Verkoopcyclus — interne controle
tags:
- concept
- procedure
- po-1-7
linked_anchors:
- 1.7.IX.C
- 1.7.IX
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: procedure
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/verkoopcyclus-ic.json
gegenereerd_op: '2026-05-18'
---
# Verkoopcyclus — interne controle 🤖

> [!summary] Korte inhoud
> Boekhoudkundige + btw-verplichtingen (correcte facturen, tijdige uitreiking).

> [!info] Behoort tot: [[interne-controle]]

Boekhoudkundige + btw-verplichtingen (correcte facturen, tijdige uitreiking).


## Stappen

### 1. Klantenacceptatie + krediettoekenning

Toets vooraf de kredietwaardigheid van de klant; ken een kredietlimiet toe.

**Waarom?** Levering zonder kredietcheck = risico op oninbare vordering.

**🛠️ Hoe**:

1. Nieuwe klant: doe due-diligence (KBO, jaarrekening, kredietverzekeraar).
2. Bepaal kredietlimiet op basis van solvabiliteit en sector.
3. ERP blokkeert leveringen aan klanten in over-limit of in mora.

**Grondslag**: Audit-cyclus-doctrine

### 2. Order + leveringsautorisatie

Order aanvaarden + magazijn-uitlevering autoriseren.

**Waarom?** Levering zonder geldige order = leveringen op naam van fictieve klant, of leveringen die later 'vergeten' worden te factureren.

**🛠️ Hoe**:

1. Sales tekent order; ERP creëert delivery note.
2. Magazijn levert uit op basis van delivery note (geen 'mondelinge instructie').

**Grondslag**: Functiescheiding-doctrine

### 3. Levering + facturatie

Goederen leveren tegen ondertekende leveringsbon; factuur uitschrijven binnen 15 dagen (BTW-vereiste).

**Waarom?** Time-gap tussen levering en factuur is fraude-risico (cut-off): omzet niet boeken in juiste periode.

**🛠️ Hoe**:

1. Klant tekent leveringsbon bij ontvangst.
2. ERP genereert automatisch factuur uit delivery note.
3. Maandelijks bestand: alle delivery notes zonder factuur — onderzoeken.

**Grondslag**: WBTW + cut-off-doctrine

### 4. Inning + opvolging

Klant betaalt; bij niet-tijdige betaling herinnering + ingebrekestelling.

**Waarom?** Vorderingen zonder follow-up worden oninbaar; cijferanalyse (DSO) detecteert problemen.

**🛠️ Hoe**:

1. Wekelijks: aged-receivables-rapport.
2. > 30 dagen: herinnering.
3. > 60 dagen: ingebrekestelling.
4. > 90 dagen: juridische actie + voorziening voor dubieuze debiteuren.

**Grondslag**: Boekhoudkundige voorzichtigheid


## Zie ook

- **Vereist kennis van**: [[functiescheiding]]

> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

