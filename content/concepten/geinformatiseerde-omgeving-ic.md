---
title: Interne controle in geïnformatiseerde omgeving
tags:
- concept
- begrip
- po-1-7
linked_anchors:
- 1.7.VIII.E
- 1.7.X
- 1.7.X.A
- 1.7.X.B
- 1.7.X.D
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: begrip
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/geinformatiseerde-omgeving-ic.json
gegenereerd_op: '2026-05-18'
---
# Interne controle in geïnformatiseerde omgeving 🤖

> [!summary] Korte inhoud
> Interne controle in een geïnformatiseerde omgeving omvat alle maatregelen om de betrouwbaarheid, integriteit en beschikbaarheid van data in ICT-systemen te waarborgen.

> [!info] Behoort tot: [[interne-controle]]

Interne controle in een geïnformatiseerde omgeving omvat alle maatregelen om de betrouwbaarheid, integriteit en beschikbaarheid van data in ICT-systemen te waarborgen. Onderscheidt twee lagen: (1) IT general controls — generieke IT-omgeving (toegangsbeheer, change management, backups, fysieke beveiliging), (2) application controls — controles binnen specifieke applicaties (input checks, calculaties, output reviews).


## In de praktijk

<h3 id="vijf-risico-categorieen-in-it-omgeving-1-7-x-a">Vijf risico-categorieën in IT-omgeving (1.7.X.A)</h3>

> [!tip]- Vijf risico-categorieën in IT-omgeving (1.7.X.A)
> (1) Ongeautoriseerde toegang (interne én externe dreigingen). (2) Dataverlies (uitval, malware, fouten). (3) Integriteitsverlies (data manipuleren). (4) Ononderbroken beschikbaarheid (DOS-attacks, infrastructuurfalen). (5) Privacy-inbreuk (GDPR-implicaties — zie [[avg-interne-controle]]). 🤖

<h3 id="fysieke-beveiliging-1-7-x-b">Fysieke beveiliging (1.7.X.B)</h3>

> [!tip]- Fysieke beveiliging (1.7.X.B)
> Servers in afgesloten ruimte, klimaatregeling, brandblusser, UPS voor stroomonderbreking, badge-toegang, camerabewaking. Bij cloud-providers: vraag SOC 2-rapport of ISO 27001-certificaat. 🤖

<h3 id="functiescheiding-in-it-1-7-x-c">Functiescheiding in IT (1.7.X.C)</h3>

> [!tip]- Functiescheiding in IT (1.7.X.C)
> Zie [[functiescheiding]] §IT-omgeving. Kerneis: gebruikersprofielen met rol-gebaseerde rechten, gescheiden ontwikkel-/test-/productie-omgevingen, IT-admin-acties gelogd en periodiek gereviewd door iemand anders. 🤖


## Valkuilen

> [!warning]- ERP-pakket geeft schijnzekerheid: data zit in één systeem dus 'het klopt automatisch'
> ⚠️ ERP-pakket geeft schijnzekerheid: data zit in één systeem dus 'het klopt automatisch'. Zonder geconfigureerde controles (autorisaties, audit trail, validaties) is een ERP gewoon een efficiënter foutverspreidingssysteem. 🤖


> [!warning]- Cloud-systemen verleggen sommige IT-controles naar de provider — maar de onderneming blijft eindverantwoordelijk
> ⚠️ Cloud-systemen verleggen sommige IT-controles naar de provider — maar de onderneming blijft eindverantwoordelijk. SLA en assurance-rapporten van provider zijn onmisbaar. 🤖



## Zie ook

- **Vereist kennis van**: [[functiescheiding]]
- **Vereist kennis van**: [[avg-interne-controle]]

