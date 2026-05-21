---
title: Audit-procedures in een IT-omgeving
tags:
- concept
- cluster
- po-1-7
linked_anchors:
- 1.7.X
- 1.7.X.A
- 1.7.X.D
programmaonderdelen:
- '1.7'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/it-audit-procedures.json
gegenereerd_op: '2026-05-21'
---
# Audit-procedures in een IT-omgeving ⚖️

Wanneer de cliënt een complexe IT-omgeving gebruikt, moet de auditor zijn werkzaamheden aanpassen. Walkthroughs verlopen via systeem-rapporten, controles worden geautomatiseerd getest, en steekproeven worden vaak vervangen door volledige populatie-analyses (data-analytics). Computer-assisted audit techniques (CAATs) en moderne data-analytics tools maken full-population testing haalbaar. Stagiairs herkennen dit bij audits van ERP-omgevingen, e-commerce-klanten en grote volumes terugkerende transacties.

> [!summary] Korte inhoud
> Audit-procedures in een IT-omgeving zijn de werkzaamheden die de auditor specifiek aanpast aan geautomatiseerde verwerking: walkthroughs door geautomatiseerde controles, toetsen van ITGC, toetsen van geautomatiseerde toepassings-controles, en gegevensgerichte werkzaamheden uitgev….

Audit-procedures in een IT-omgeving zijn de werkzaamheden die de auditor specifiek aanpast aan geautomatiseerde verwerking: walkthroughs door geautomatiseerde controles, toetsen van ITGC, toetsen van geautomatiseerde toepassings-controles, en gegevensgerichte werkzaamheden uitgevoerd met computer-assisted audit techniques (CAATs) of data-analytics tools.

_Bron: ISA 315 (herzien-2019) Bijlage 5 + ISA 330_



## Bouwstenen

### Walkthrough door geautomatiseerde verwerking ⚖️

De auditor doorloopt een transactie van trigger tot eindboeking en identificeert welke stappen handmatig en welke geautomatiseerd zijn; geautomatiseerde controles worden expliciet benoemd.

**Waarom?** Geautomatiseerde controles zijn betrouwbaarder bij grote volumes — als ze effectief werken, kan substantieve toetsing worden teruggeschroefd; maar dan moeten ITGC eerst getest worden.


**In de praktijk**: Voor de aankoopcyclus loopt de auditor één PO van aanvraag tot betaling: ERP-screen voor aanvraag, workflow-autorisatie, three-way match-screen, betalingsbestand. Elke schermafdruk wordt opgeslagen in het werkdossier.


_Grondslag: ISA 315 (herzien-2019) par. 25 + 26_

### Computer-assisted audit techniques (CAATs) ⚖️

Tools en technieken waarmee de auditor populaties van transacties analyseert via software: query-tools (SQL), audit-software (ACL, IDEA), spreadsheet-analyse en custom scripts.

**Waarom?** Steekproef-testen op grote volumes is niet betrouwbaar; CAATs maken full-population analysis haalbaar voor bestaan, volledigheid en cut-off-bewering.


**In de praktijk**: Met IDEA exporteert de auditor het volledige verkoopjournaal en zoekt automatisch naar dubbele factuurnummers, facturen op zaterdag/zondag, sequentie-gaps en transacties net onder de autorisatie-drempel. Geen steekproef nodig — de populatie zelf wordt gescand.

Bij Yperse Werkplaats BV draait externe auditor Sofie Janssens een IDEA-script op het complete payroll-bestand: groepering per IBAN ontdekt twee werknemers met identiek rekeningnummer — verder onderzoek wijst uit dat één ervan een ghost employee is. _(Yperse Werkplaats BV, Sofie Janssens)_ 🤖

_Grondslag: ISA 500 par. A16 + ISA 330 par. 18 (gegevensgerichte werkzaamheden)_

### Data-analytics in audit ⚖️

Geavanceerdere CAATs die patronen en uitzonderingen detecteren over populaties: Benford-analyse, journal-entry-testing op ongebruikelijke combinaties, time-series-analyse van omzet, risico-scoring per transactie.

**Waarom?** ISA 240 verplicht journal-entry-testing op fraude; data-analytics maakt dit schaalbaar en risicogericht.


**In de praktijk**: Een Benford-analyse op de eerste cijfers van factuurbedragen detecteert anomalieën die op manipulatie wijzen; journal-entries op zon- en feestdagen of door ongebruikelijke gebruikers worden automatisch geflagd.


_Grondslag: ISA 240 par. 32-33 (journal entry testing) + ISA 520 (cijferanalyses)_

### Toetsen van ITGC en application controls ⚖️

Wanneer de auditor steunt op geautomatiseerde controles voor zijn risico-respons, toetst hij eerst de ITGC over de betreffende applicatie (zie [[it-general-controls]]) en daarna de geautomatiseerde toepassings-controle (zie [[it-application-controls]]).

**Waarom?** Application controls zonder betrouwbare ITGC zijn niet als basis te gebruiken — ISA 315 (herzien-2019) par. 26(c) maakt deze keten expliciet.




_Grondslag: ISA 315 (herzien-2019) par. 26(c) + Bijlage 5 par. 8-9_


## In de praktijk

<h3 id="schaalbaarheid-voor-kmo-audits">Schaalbaarheid voor KMO-audits</h3>

> [!tip]- Schaalbaarheid voor KMO-audits
> ISA 315 (herzien-2019) Bijlage 5 erkent expliciet dat KMO's vaak commerciële software gebruiken zonder maatwerk. Dan kan de auditor zich beperken tot inzicht in de configuratie van het pakket en steunen op de bestaande reputatie van de software; full ITGC-testing is dan niet altijd nodig. Bij grotere of complexere ERP-omgevingen stijgt de testintensiteit. ⚖️


## Valkuilen

> [!warning]- CAATs zonder bron-verificatie zijn gevaarlijk: een script dat draait op een onvolledige extract leidt tot foute conclusies
> ⚠️ CAATs zonder bron-verificatie zijn gevaarlijk: een script dat draait op een onvolledige extract leidt tot foute conclusies. Eerste audit-stap: reconcilieer de extract tegen het ERP-saldo voordat je de analyse draait. 🤖


> [!warning]- Data-analytics is geen vervanger van professional skepticism: een algoritme dat geen anomalieën rapporteert betekent niet dat er geen fraude…
> ⚠️ Data-analytics is geen vervanger van professional skepticism: een algoritme dat geen anomalieën rapporteert betekent niet dat er geen fraude is — de fraudeur kan binnen de normale patronen blijven (small frauds, structured to look like business as usual). 🤖



## Zie ook

- **Vereist kennis van**: [[it-general-controls]]
- **Vereist kennis van**: [[it-application-controls]]
- **Vereist kennis van**: [[fraudedriehoek]]

## Bronnen

[^1]: `ISA-315-herzien-2019__sec_bijlage-5_part2`
[^2]: `ISA-315-herzien-2019__sec_bijlage-5_part3`
