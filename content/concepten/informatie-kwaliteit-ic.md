---
title: Informatie en haar kwaliteitseisen
tags:
- concept
- begrip
- po-1-7
linked_anchors:
- 1.7.II.D
- 1.7.II
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: begrip
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/informatie-kwaliteit-ic.json
gegenereerd_op: '2026-05-18'
---
# Informatie en haar kwaliteitseisen 🤖

Informatiekwaliteit is in PO 1.7 de minimumvoorwaarde voor zinvolle managementbeslissing en betrouwbare rapportering. Voor de stagiair komt dit overal terug: ISA 500 stelt kwaliteitseisen aan audit-evidence; ISA 315 vereist dat hij beoordeelt of de cliënt-informatie betrouwbaar is; bij adviesopdrachten is dit waarom een KPI 'zonder bron' geen managementbeslissing kan dragen. Examen-vragen testen vooral de vijf criteria (relevant, betrouwbaar, tijdig, volledig, begrijpelijk) en hoe te toetsen.

> [!summary] Korte inhoud
> Informatie in IC-context is verwerkte data die geschikt is voor besluitvorming en rapportering.

> [!info] Behoort tot: [[informatie-en-communicatie-ic]]

Informatie in IC-context is verwerkte data die geschikt is voor besluitvorming en rapportering. Voor bruikbaarheid moet ze voldoen aan kwaliteitseisen: (1) relevant — raakt de te nemen beslissing; (2) betrouwbaar — accuraat, neutraal, verifieerbaar; (3) tijdig — beschikbaar wanneer nodig; (4) volledig — geen kritieke ontbrekende elementen; (5) begrijpelijk — formaat past bij gebruiker.


## Bouwstenen

### Vijf kwaliteitscriteria 🤖

(1) Relevant — raakt de beslissing. (2) Betrouwbaar — accuraat, neutraal, verifieerbaar. (3) Tijdig — op tijd voor de beslissing. (4) Volledig — geen kritieke elementen ontbreken. (5) Begrijpelijk — formaat past bij gebruiker.

**Waarom?** Een rapport dat één van de vijf mist is potentieel misleidend. Voor de externe auditor zijn (2) en (4) zwaarder; voor managementgebruik wegen (1) en (3) zwaarder.




_Grondslag: ISA 315 Bijlage 3 §17 + algemene bedrijfsdoctrine_

### Bron-traceerbaarheid 🤖

Voor elke beslissingscijfer moet de oorspronkelijke registratiebron achterhaalbaar zijn (audit trail).

**Waarom?** Zonder bron-trace kan niemand later achterhalen of een cijfer accuraat is — fataal voor zowel managementbeslissingen als audit.


**In de praktijk**: Stagiair-test: vraag voor één KPI 'waar komt dit cijfer vandaan?'. Geen antwoord of vage 'het rapport zegt het' = kwaliteitsval.


_Grondslag: ISA 500 + COBIT IT-audit-richtlijnen_

### Kwaliteit van controle-informatie (ISA 500) ⚖️

ISA 500 vereist dat de auditor 'voldoende en geschikte' controle-informatie verkrijgt. 'Voldoende' = kwantiteit (genoeg bewijsstukken, schaalt met ingeschatte risico). 'Geschikt' = kwaliteit, met twee dimensies: (a) relevant — de informatie raakt de bewering die getoetst wordt; (b) betrouwbaar — afhankelijk van bron, aard en omstandigheden (origineel > kopie; extern > intern; geschreven > mondeling).

**Waarom?** De kwaliteitseisen aan auditbewijs zijn de externe-audit-vertaling van de algemene informatie-kwaliteitseisen op managementniveau. Begrip van beide laat de stagiair zien waarom een betrouwbaar IS bij de cliënt rechtstreeks de auditefficiency raakt.


**In de praktijk**: Cliënt-rapport zonder audit trail naar onderliggende facturen = niet 'voldoende en geschikt' — auditor moet dan eigen detailtest doen.


_Grondslag: ISA 500 §6-§9_


## Valkuilen

> [!warning]- Kwaliteit verwarren met volume: 'we hebben heel veel data' bewijst geen kwaliteit
> ⚠️ Kwaliteit verwarren met volume: 'we hebben heel veel data' bewijst geen kwaliteit. Een rapport van 50 pagina's met onverifiabele cijfers is informatie-kwantiteit zonder kwaliteit. 🤖



## Voorbeelden

Bij Yperse Werkplaats BV is een maandrapport drie weken te laat = niet tijdig → kan beslissingen niet sturen → niet bruikbaar voor IC. Als de gebruikte omzetgegevens steekproefachtig zijn en niet 100% van het boekjaar = niet volledig → vertekend beeld. Een rapport in technische jargon voor directie zonder financiële achtergrond = niet begrijpelijk → genegeerd.

## Bronnen

[^1]: `ISA-315-herzien-2019__sec_bijlage-3`
[^2]: `ISA-500__sec_vereisten`
