---
title: IT general controls (ITGC)
tags:
- concept
- cluster
- po-1-7
linked_anchors:
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
gegenereerd_uit: data/concepten/records/it-general-controls.json
gegenereerd_op: '2026-05-21'
---
# IT general controls (ITGC) ⚖️

IT general controls (ITGC) zijn de overkoepelende interne controles op de IT-omgeving die de werking van geautomatiseerde controles binnen applicaties ondersteunen en beschermen. Ze beslaan vier lagen (applicatie, database, besturingssysteem, netwerk) en drie processen (toegang beheren, programma-wijzigingen beheren, IT-activiteiten beheren). Stagiairs komen ITGC tegen bij elke audit met ISA 315 risico-inschatting: als ITGC tekortschieten, kunnen geautomatiseerde controles in applicaties niet betrouwbaar steunen.

> [!summary] Korte inhoud
> IT general controls (ITGC) zijn interne controles op het niveau van de gehele IT-omgeving (applicaties, databases, besturingssysteem, netwerk) die de integriteit van financiële informatie beschermen door ongeautoriseerde toegang, ongecontroleerde programma-wijzigingen en falen va….

> [!info] Behoort tot: [[geinformatiseerde-omgeving-ic]]

IT general controls (ITGC) zijn interne controles op het niveau van de gehele IT-omgeving (applicaties, databases, besturingssysteem, netwerk) die de integriteit van financiële informatie beschermen door ongeautoriseerde toegang, ongecontroleerde programma-wijzigingen en falen van IT-activiteiten te voorkomen of te detecteren.

_Bron: ISA 315 (herzien-2019) Bijlage 6_



## Bouwstenen

### Toegang beheren ⚖️

Authenticatie, autorisatie, het verlenen en intrekken van toegangsrechten, periodieke gebruikerstoegang-reviews en fysieke toegang tot datacenter.

**Waarom?** Ongeautoriseerde toegang ondermijnt elke geautomatiseerde controle en functiescheiding; toegangsbeheer is de eerste verdedigingslinie.


**In de praktijk**: Rol-gebaseerde rechten (RBAC) waarbij de financieel directeur betalingen kan vrijgeven maar de boekhouder niet; toegang van een uitdienst getreden werknemer wordt op de dag van uitdiensttreding ingetrokken; jaarlijkse user-access-review per applicatie.

Bij Yperse Werkplaats BV worden de access rights van werknemers maandelijks tegen het Dimona-bestand gematched: iedere actieve gebruiker moet een actief contract hebben. Verschillen worden opgevolgd door IT-verantwoordelijke Helena Devos. _(Yperse Werkplaats BV, Helena Devos)_ 🤖

_Grondslag: ISA 315 (herzien-2019) Bijlage 6 par. 2(a)_

### Programma- en wijzigingsbeheer (change management) ⚖️

Geformaliseerd proces voor het ontwerpen, testen en migreren van wijzigingen naar productie, met functiescheiding tussen wie wijzigt en wie migreert.

**Waarom?** Ongecontroleerde wijzigingen kunnen geautomatiseerde controles uitschakelen of ongemerkt frauduleuze logica introduceren.


**In de praktijk**: Ontwikkelaars werken in een test-omgeving; een aparte release-manager migreert naar productie na goedkeuring; alle wijzigingen worden gelogd met traceerbare ticketnummers.


_Grondslag: ISA 315 (herzien-2019) Bijlage 6 par. 2(b)_

### Beheer van IT-activiteiten (computer operations) ⚖️

Taakplanning, taakmonitoring, back-up en herstel, en monitoring op indringers.

**Waarom?** Falen van back-ups bij ransomware of corruption van rapport-jobs verstoort de continuïteit van financiële verslaggeving.


**In de praktijk**: Nightly back-up naar offline locatie; jaarlijkse restore-test; intrusion-detection-systeem met alerts naar IT-verantwoordelijke.


_Grondslag: ISA 315 (herzien-2019) Bijlage 6 par. 2(c)_

### Vier lagen waarop ITGC werken ⚖️

ITGC werken op vier lagen: applicatie, database, besturingssysteem en netwerk. Elke laag heeft eigen risico's en specifieke controles.

**Waarom?** Een controle op applicatieniveau (bijvoorbeeld autorisatie binnen ERP) wordt omzeild bij directe database-toegang als de database-laag niet apart wordt afgeschermd.


**In de praktijk**: Een ERP-gebruiker mag enkel de bedrijfsfuncties van het ERP gebruiken; alleen DB-beheerders hebben SQL-toegang tot de onderliggende database; servers staan in een afgesloten serverroom met beperkte fysieke toegang.


_Grondslag: ISA 315 (herzien-2019) Bijlage 6 par. 1_


## In de praktijk

<h3 id="wanneer-is-steun-op-geautomatiseerde-controles-mogelijk">Wanneer is steun op geautomatiseerde controles mogelijk?</h3>

> [!tip]- Wanneer is steun op geautomatiseerde controles mogelijk?
> ISA 315 (herzien-2019) stelt dat als de entiteit steunt op een IT-applicatie voor de integriteit van financiële informatie, de auditor de ITGC over die applicatie moet identificeren en toetsen. Falen van ITGC betekent dat geautomatiseerde controles binnen die applicatie niet betrouwbaar zijn als onderdeel van de risicorespons. ⚖️


## Valkuilen

> [!warning]- Cloud-uitbesteding verlegt sommige ITGC naar de provider, maar de entiteit blijft eindverantwoordelijk
> ⚠️ Cloud-uitbesteding verlegt sommige ITGC naar de provider, maar de entiteit blijft eindverantwoordelijk. Audit-stap: vraag SOC 2 type 2 of ISO 27001-rapport en lees de complementary user entity controls (de controles die de klant zelf moet inbouwen). 🤖


> [!warning]- ITGC enkel testen voor de applicatie-laag is onvolledig
> ⚠️ ITGC enkel testen voor de applicatie-laag is onvolledig. Direct database access via SQL-tools, OS-admin rechten of netwerkverkeer kan applicatie-controles omzeilen. ISA 315 Bijlage 6 maakt deze vier-lagen-structuur expliciet. ⚖️
>
> _Bron: ISA 315 Bijlage 6 par. 1_



## Zie ook

- **Vereist kennis van**: [[functiescheiding]]
- **Wordt voorondersteld in** (6): [[cyberrisico-ic]] · [[geinformatiseerde-omgeving-ic]] · [[informatiesysteem-onderneming]] · [[it-application-controls]] · [[it-audit-procedures]] · [[nis-2-richtlijn]]
## Bronnen

[^1]: `ISA-315-herzien-2019__sec_bijlage-6_part2`
[^2]: `ISA-315-herzien-2019__sec_bijlage-6-overwegingen-voor-het-verwerven-van-inzicht-in-gen`
