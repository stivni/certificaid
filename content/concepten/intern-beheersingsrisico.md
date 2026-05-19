---
title: Intern beheersingsrisico
tags:
- concept
- begrip
- po-1-6
- po-1-7
linked_anchors:
- 1.6.II.B
- 1.6.II.C
- 1.7.V.E
- 1.7.III.B
- 1.7.VIII.F
programmaonderdelen:
- '1.6'
- '1.7'
confidence: grounded
node_type: begrip
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/intern-beheersingsrisico.json
gegenereerd_op: '2026-05-18'
---
# Intern beheersingsrisico ⚖️

Intern beheersingsrisico is het risico dat de interne beheersing van de cliënt een potentiële afwijking niet voorkomt of niet tijdig detecteert. Het is een eigenschap van de cliënt — de auditor beïnvloedt het niet, hij toetst het via test-of-controls en stuurt zijn substantive werkzaamheden ernaar. Samen met inherent risico vormt het het risico op een afwijking van materieel belang.

> [!summary] Korte inhoud
> Intern beheersingsrisico is het risico dat een afwijking die kan optreden in een bewering (over een transactiestroom, rekeningsaldo of toelichting) — afzonderlijk of samen met andere van materieel belang — niet wordt voorkomen of niet tijdig wordt gedetecteerd en hersteld door de….

> [!info] Behoort tot: [[auditrisicomodel]]

Intern beheersingsrisico is het risico dat een afwijking die kan optreden in een bewering (over een transactiestroom, rekeningsaldo of toelichting) — afzonderlijk of samen met andere van materieel belang — niet wordt voorkomen of niet tijdig wordt gedetecteerd en hersteld door de interne beheersing van de cliënt.

_Bron: ITAA KMO-controlenorm Bijlage 1_


## Bouwstenen

### Plaats in het auditrisicomodel ⚖️

Auditrisico = inherent risico × intern beheersingsrisico × detectierisico. Intern beheersingsrisico is een eigenschap van de cliënt, niet beïnvloedbaar door de auditor — hij toetst het en stuurt zijn werkzaamheden ernaar.

**Waarom?** Bij hoog intern beheersingsrisico moet de auditor zijn detectierisico verlagen door méér substantieve toetsen — direct kost-driver.




_Grondslag: ISA 200 §13 + ISA 315 (herzien-2019)_

### Inschatting begint met design en implementatie ⚖️

De auditor moet eerst evalueren of de IC-maatregelen goed ontworpen zijn én daadwerkelijk geïmplementeerd vooraleer hij hun werking kan testen.

**Waarom?** Een prachtig ontworpen procedure die niemand uitvoert is geen IC. Walkthrough en inquiry zijn standaardprocedures hiervoor.




_Grondslag: ISA 315 (herzien-2019)_

### Test-of-controls bij lage inschatting ⚖️

Wanneer de auditor het beheersingsrisico laag inschat en daarop wil steunen, MOET hij de werking effectief testen via test-of-controls — niet alleen ontwerp.

**Waarom?** Steunen op IC zonder werkingstoets = ongegrond optimisme.




_Grondslag: ISA 330 §8_


## In de praktijk

<h3 id="onmogelijk-volledig-nul">Onmogelijk volledig nul</h3>

> [!tip]- Onmogelijk volledig nul
> Zelfs een sterke interne beheersing kan niet alle risico's elimineren — beperkingen zoals management override, menselijke fout en cost-benefit-afwegingen blijven. Intern beheersingsrisico > 0 is dus normaal. 🤖

<h3 id="steunen-op-interne-beheersing-testen-verplicht">Steunen op interne beheersing → testen verplicht</h3>

> [!tip]- Steunen op interne beheersing → testen verplicht
> Wil de auditor steunen op de effectieve werking van de interne beheersing om minder gegevensgerichte werkzaamheden te doen, dan MOET hij toetsingen van interne beheersing uitvoeren (test of controls). Pas dan mag hij het intern beheersingsrisico als laag inschatten. ⚖️


## Zie ook

- **Getriggerd door**: [[toetsing-interne-beheersing]]
- **Vereist kennis van**: [[interne-controle]]

## Voorbeelden

Sofie Janssens schat het beheersingsrisico voor verkoop-cyclus van Yperse Werkplaats BV in als 'midden': automatische ERP-validaties werken, maar één werknemer (Karen De Backer) heeft volledige toegang van bestelling tot betaling — beperkte functiescheiding. Daarom test ze 25 verkopen op effectiviteit van compenserende review-controle door Pieter Vermeulen.

## Bronnen

[^1]: `ITAA-norm-kmo-controlenorm__sec_bijlage-1-definities_part4`
[^2]: `ITAA-norm-kmo-controlenorm__sec_3-2-1-manieren-om-in-te-spelen-op-ingeschatte-risico-s`
[^3]: `ITAA-norm-kmo-controlenorm__sec_toetsingen-van-interne-beheersingsmaatregelen`
[^4]: `ITAA-norm-kmo-controlenorm__sec_bijlage-1-definities_part2`
[^5]: `ISA-200__sec_definities`
[^6]: `ISA-315-herzien-2019__sec_bijlage-3`
[^7]: `ISA-330__sec_definities`
