---
title: Interne controle in een geïnformatiseerde omgeving
tags:
- concept
- cluster
- po-1-7
linked_anchors:
- 1.7.VIII.E
- 1.7.X
- 1.7.X.A
- 1.7.X.B
- 1.7.X.D
programmaonderdelen:
- '1.7'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/geinformatiseerde-omgeving-ic.json
gegenereerd_op: '2026-05-18'
---
# Interne controle in een geïnformatiseerde omgeving ⚖️

Interne controle in een geïnformatiseerde omgeving combineert klassieke organisatorische maatregelen met IT-specifieke controles op vier lagen (applicatie, database, OS, netwerk). De architectuur valt uiteen in twee complementaire lagen: IT general controls op omgevings-niveau en application controls op transactie-niveau. Specifieke aandachtspunten (anchor 1.7.VIII.E): toegangsbeheer, geautomatiseerde validaties, audit trails, logbestanden en het scheiden van ontwikkelings-, test- en productie-omgevingen. Daarnaast vereisen cyberrisico's gerichte maatregelen. Stagiairs herkennen dit als één van de meest examen-relevante onderwerpen van programmaonderdeel 1.7.

> [!summary] Korte inhoud
> Interne controle in een geïnformatiseerde omgeving omvat alle maatregelen die de betrouwbaarheid, integriteit en beschikbaarheid van data in ICT-systemen waarborgen.

> [!info] Behoort tot: [[interne-controle]]

Interne controle in een geïnformatiseerde omgeving omvat alle maatregelen die de betrouwbaarheid, integriteit en beschikbaarheid van data in ICT-systemen waarborgen. Twee lagen vormen de kern: IT general controls die de IT-omgeving beheersen (toegang, change, operations) en application controls die binnen specifieke applicaties werken (input, processing, output).

_Bron: ISA 315 (herzien-2019) Bijlage 5 + Bijlage 6_


## Bouwstenen

### Twee complementaire lagen — ITGC en application controls ⚖️

ITGC werken op omgevings-niveau (toegang, change, operations); application controls werken op transactie-niveau binnen een specifieke applicatie. Application controls zijn enkel betrouwbaar als de onderliggende ITGC betrouwbaar zijn.

**Waarom?** Zonder dit onderscheid valt elke discussie over IT-IC platte: een ERP-three-way-match is een application control die onbruikbaar wordt zonder change-management-ITGC over zijn configuratie.




_Grondslag: [[it-general-controls]] + [[it-application-controls]]_

### Vier lagen waarop IT-IC werkt ⚖️

Applicatie (binnen ERP, salaris), database (onderliggende data), besturingssysteem (Windows, Linux), netwerk (firewall, segmentatie). Elke laag heeft eigen risico's en controles.

**Waarom?** Een ERP-gebruikersrol kan worden omzeild door iemand met directe database-toegang of OS-admin-rechten; de vier lagen moeten samen sluiten.


**In de praktijk**: Bij Yperse Werkplaats BV mag inkoper Tom Lefèvre alleen de aankoop-module gebruiken (applicatie-laag); enkel database-beheerder Helena Devos heeft SQL-toegang (database-laag); servers staan in afgesloten serverroom (OS/fysieke laag); netwerk heeft VPN-verplicht remote access (netwerk-laag).


_Grondslag: ISA 315 (herzien-2019) Bijlage 6 par. 1_

### Fysieke beveiliging als sluitstuk ⚖️

Fysieke toegang tot servers, datacenters en eindapparatuur via toegangscontrole, camerabewaking en milieubeheer (brand, klimaat, UPS).

**Waarom?** Logische controles worden waardeloos als iemand fysiek bij de server kan: een USB-stick volstaat om de boot-volgorde te wijzigen of admin-credentials te resetten.


**In de praktijk**: Serverroom met badge-toegang en log; brandblusser op CO2; UPS voor stroomuitval; cloud-providers leveren SOC 2-rapport over hun fysieke controles.

Bij Yperse Werkplaats BV staat de on-premise ERP-server in een aparte ruimte met badge-toegang; alleen IT-verantwoordelijke Helena Devos en CFO David Janssens hebben badge-rechten. Bezoekers (technici, leveranciers) tekenen een logboek en worden door Helena begeleid. Brandblusser op CO2, UPS van 30 minuten, klimaat-monitoring met alert bij temperatuur > 28 °C. 🤖
### Scenario

Rotex Roeselare NV migreert in 2025 het ERP naar een hyperscaler-cloud. Voor de fysieke beveiliging steunt de auditor op het SOC 2 type 2-rapport van de provider (Microsoft Azure, EU-region). Aanvullend leest de auditor de Complementary User Entity Controls: 'klant moet (a) MFA afdwingen, (b) IP-allowlisting configureren, (c) admin-accounts apart beheren'. Het ontbreken van CUEC-implementatie maakt de provider-controles waardeloos in de IC-architectuur.
🤖



_Grondslag: ISA 315 (herzien-2019) Bijlage 6 par. 2(a) — fysieke toegang als sub-aspect van toegangsbeheer ("Interne beheersingsmaatregelen over fysieke toegang tot het datacenter en hardware")_

### Risicocategorieën specifiek voor IT 🤖

Ongeautoriseerde toegang (intern of extern), dataverlies, integriteitsverlies, beschikbaarheidsverlies, privacy-inbreuk.

**Waarom?** Stagiair moet de typische IT-risico's herkennen om te beoordelen of de IC-maatregelen ze afdekken.




_Grondslag: [[cyberrisico-ic]] §dreigingen + [[avg-interne-controle]] §risico's_

### Scheiding ontwikkel-, test- en productie-omgevingen ⚖️

Drie afzonderlijke logische omgevingen (vaak ook fysiek): ontwikkeling (developers experimenteren), test (gevalideerde wijzigingen op realistische data), productie (live, met echte transacties). Verschillende rollen en toegang per omgeving; wijzigingen volgen een formele change-management-flow van dev → test → prod.

**Waarom?** Zonder scheiding kunnen ongeteste wijzigingen direct in productie terechtkomen — risico op data-corruptie, financiële afwijkingen, security-gaten. Bovendien: developers met productie-toegang doorbreken functiescheiding tussen 'systeem bouwen' en 'systeem operationeel houden'.


**In de praktijk**: Bij Rotex Roeselare NV: developer Lukas heeft alleen dev-omgeving toegang; test-omgeving wordt beheerd door QA-team; productie-deployment alleen door release-manager Helena na getekende change-approval. Audit trail logt elke prod-deployment met user + change-ticket-nummer.

Bij Yperse Werkplaats BV worden ERP-aanpassingen eerst getest in een sandbox-database met geanonimiseerde productie-kopie; pas na getekende go-live-checklist (functioneel + IT-security) komt de change in productie.

_Grondslag: ISA 315 (herzien-2019) Bijlage 6 §change management + IIA Standard 2120_


## In de praktijk

<h3 id="toepassing-op-een-erp-context">Toepassing op een ERP-context</h3>

> [!tip]- Toepassing op een ERP-context
> Bij Yperse Werkplaats BV draait alles op ERP. ITGC laag: serverroom op slot (fysieke beveiliging), userprofielen met rol-gebaseerde rechten (toegangsbeheer), nightly back-up naar externe site (operations), test/productie-scheiding bij upgrades (change management). Application controls binnen het ERP: dubbele invoer-validatie op IBAN, automatische btw-berekening, drempel-autorisaties. 🤖


## Valkuilen

> [!warning]- Een ERP-pakket geeft schijnzekerheid: data zit in één systeem, dus 'het klopt automatisch'
> ⚠️ Een ERP-pakket geeft schijnzekerheid: data zit in één systeem, dus 'het klopt automatisch'. Zonder geconfigureerde controles (autorisaties, audit trail, validaties) is een ERP gewoon een efficiënter foutverspreidings-systeem. 🤖


> [!warning]- Cloud-systemen verleggen sommige IT-controles naar de provider, maar de onderneming blijft eindverantwoordelijk
> ⚠️ Cloud-systemen verleggen sommige IT-controles naar de provider, maar de onderneming blijft eindverantwoordelijk. SLA en assurance-rapporten van provider (SOC 2 type 2, ISO 27001) zijn onmisbaar; lees ook de complementary user entity controls die de klant zelf moet inbouwen. 🤖


> [!warning]- Application controls testen zonder ITGC-toetsing is een audit-fout
> ⚠️ Application controls testen zonder ITGC-toetsing is een audit-fout. Geprogrammeerde validaties zijn afhankelijk van de change-management-controle die voorkomt dat ze stiekem worden aangepast. ⚖️
>
> _Bron: ISA 315 (herzien-2019) par. 26(c)_



## Zie ook

- **Vereist kennis van**: [[it-general-controls]]
- **Vereist kennis van**: [[it-application-controls]]
- **Vereist kennis van**: [[functiescheiding]]
- **Vereist kennis van**: [[avg-interne-controle]]
- **Vereist kennis van**: [[cyberrisico-ic]]

## Voorbeelden

Bij Yperse Werkplaats BV draait alles op ERP (Odoo). IT general controls: serverroom op slot (fysieke beveiliging), userprofielen met rol-gebaseerde rechten (toegangsbeheer), nightly back-up naar externe site (continuïteit), test/productie-scheiding bij upgrades (change management). Application controls binnen Odoo: dubbele invoer-validatie op IBAN, automatische btw-berekening, drempel-autorisaties.

## Bronnen

[^1]: `ISA-315-herzien-2019__sec_bijlage-5_part2`
[^2]: `ISA-315-herzien-2019__sec_bijlage-6_part2`
