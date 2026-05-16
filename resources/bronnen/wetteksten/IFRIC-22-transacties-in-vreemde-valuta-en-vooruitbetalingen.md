---
title: IFRIC-22 — Transacties in vreemde valuta en vooruitbetalingen
tags:
- '1.5'
- ifrs
- ifric
itaa-lex-sectie: ''
wet: Verordening (EU) 2023/1803 — geconsolideerde IFRS
bron_rol: normatief
bron_categorie: ifrs
standaard_type: IFRIC
standaard_nummer: '22'
status: beschikbaar
bijgewerkt: 13.08.2023
bron: EUR-Lex CELEX 32023R1803
chunk:
  level: 2
  type: Sectie
  sub_strategy: null
provenance:
  inputs:
  - id: resources/raw/wetteksten/EU-Verordening-2023-1803-IFRS-Geconsolideerd.pdf
    sha256: 20512af4119d8dc42de857d3ccca87d9e0dac728b0c79f0eb047ca16e9694132
    version: 13.08.2023
    pages: 976-979
  tooling:
    pipeline: tools/etl/split_ifrs_verordening.py
    pipeline_version: '1.0'
    model: null
    prompt_version: null
  generated_at: '2026-05-16T19:10:07Z'
  stale: false
  stale_reason: null
  trust:
    status: trusted
    confirmed_at: '2026-05-16T20:31:37Z'
    confirmed_by: subagent-qa-2026-05-16
    rationale: >-
      QA-pass 2026-05-16: gestructureerde body met heading-detectie op
      DOEL/TOEPASSINGSGEBIED/DEFINITIES + paragraph-numbers; inhoud is volledig en
      RAG-bruikbaar. Kolomwrap-splits ('instru menten', 'voorwaar den') zijn inherent aan de
      bron-PDF (EUR-Lex CELEX 32023R1803 kolommen), niet aan de ETL — analoog aan
      EU-IFRS-verordening-1606-2002.md die trusted is.
    caveat: >-
      pymupdf-heading-detector promoot incidenteel paragraph-nummers en korte regels (zoals '##
      38A', '## B12', '## (X)', '## Ifrs 9;') tot ## — over-segmentation maar geen
      content-verlies; chunker handelt dit af. Tweetalig is geen issue (NL-only
      EUR-Lex-extractie).
    layer1: null
    layer2: null
---

IFRIC-INTERPRETATIE 22 Transacties in vreemde valuta en vooruitbetalingen

## Referenties

— Conceptual Framework for Financial Reporting ( 69 ) — IAS 8 Grondslagen voor financiële verslaggeving, schattingswijzigingen en fouten — IAS 21 De gevolgen van wisselkoerswijzigingen

## Achtergrond

1. Op grond van alinea 21 van IAS 21 De gevolgen van wisselkoerswijzigingen moet een entiteit een transactie in vreemde valuta, bij eerste opname in haar functionele valuta, opnemen door op het bedrag in vreemde valuta de precieze wisselkoers toe te passen die op de datum van de transactie geldt tussen de functionele valuta en de vreemde valuta (“de wisselkoers”). In alinea 22 van IAS 21 is bepaald dat de transactiedatum de datum is waarop de transactie voor het eerst in aanmerking komt voor opname overeenkomstig de International Financial Reporting Standards (“de IFRSs” of “de standaarden”). 2. Wanneer een entiteit een vooruitbetaling in een vreemde valuta doet of ontvangt, neemt zij deze veelal als een niet-monetair actief of een niet-monetaire verplichting op ( 70 ) voordat zij het daarmee verband houdende actief of de daarmee verband houdende baat of last opneemt. Het daarmee verband houdende actief of de daarmee verband houdende baat of last (of een deel daarvan) is het overeenkomstig de relevante standaarden opgenomen bedrag dat resulteert in het niet langer opnemen van het niet-monetaire actief dat of de niet-monetaire ver plichting die uit de vooruitbetaling voortvloeit. 3. Oorspronkelijk heeft het IFRS Interpretations Committee (“het Interpretations Committee”) de vraag ontvangen hoe bij de toepassing van de alinea’s 21 en 22 van IAS 21 “de datum van de transactie” moet worden bepaald voor de opname van opbrengsten. De vraag had specifiek betrekking op de omstandigheden waarin een entiteit een uit de ontvangst van een vooruitbetaling voortvloeiende niet-monetaire verplichting opneemt voordat zij de daarmee verband houdende opbrengsten opneemt. Bij de bespreking van de kwestie merkte het Interpretations Committee dat het ontvangen of het doen van vooruitbetalingen in een vreemde valuta niet alleen bij opbreng sten genererende transacties voorkomt. Het Interpretations Committee heeft dan ook besloten duidelijkheid te scheppen over de datum van de transactie voor de bepaling van de wisselkoers die bij eerste opname van het daarmee verband houdende actief of de daarmee verband houdende baat of last moet worden gehanteerd wanneer een entiteit een vooruitbetaling in een vreemde valuta heeft ontvangen of gedaan.

## Toepassingsgebied

4. Deze interpretatie is van toepassing op een transactie in vreemde valuta (of een deel daarvan) wanneer een entiteit overgaat tot de opname van een niet-monetair actief dat of een niet-monetaire verplichting die uit het doen of het ontvangen van een vooruitbetaling voortvloeit voordat de entiteit het daarmee verband houdende actief of de daarmee verband houdende baat of last (of een deel daarvan) opneemt. 5. Deze interpretatie is niet van toepassing wanneer een entiteit het daarmee verband houdende actief of de daarmee verband houdende baat of last bij eerste opname opneemt:
(a) reële waarde; of
(b) tegen de reële waarde van de vergoeding die is betaald of ontvangen op een andere datum dan de datum van eerste opname van het niet-monetaire actief dat of de niet-monetaire verplichting die uit de vooruitbetaling voortvloeit (bijvoorbeeld de waardering van goodwill in overeenstemming met IFRS 3 Bedrijfscombinaties ). ( 69 ) De verwijzing betreft het Conceptual Framework for Financial Reporting, dat in 2010 is uitgegeven en van kracht was toen de Interpretatie werd ontwikkeld. ( 70 ) In alinea 106 van IFRS 15 Opbrengsten van contracten met klanten is bijvoorbeeld het volgende bepaald: als een klant een vergoeding betaalt, of een entiteit een recht op een vergoeding die onvoorwaardelijk is (d.w.z. een vordering) heeft, moet de entiteit alvorens een goed of een dienst aan de klant over te dragen het contract als een contractverplichting presenteren wanneer de betaling wordt gedaan of, wanneer dit vroeger valt, wanneer de betaling verschuldigd is.

6. Een entiteit is niet verplicht deze interpretatie toe te passen op:
(a) winstbelastingen; of
(b) door haar uitgegeven verzekeringscontracten (met inbegrip van herverzekeringscontracten) of door haar gehouden herverzekeringscontracten.

## Probleemstelling

7. Deze interpretatie behandelt de vraag hoe de datum van de transactie moet worden bepaald voor de bepaling van de wisselkoers die bij eerste opname van het daarmee verband houdende actief of de daarmee verband houdende baat of last (of een deel daarvan) moet worden gehanteerd bij het niet langer opnemen van een niet-monetair actief dat of een niet-monetaire verplichting die uit het doen of ontvangen van een vooruitbetaling in een vreemde valuta voortvloeit.

## Consensus

8. Bij de toepassing van de alinea’s 21 en 22 van IAS 21 is de datum van de transactie voor de bepaling van de wisselkoers die bij eerste opname van het daarmee verband houdende actief of de daarmee verband houdende baat of last (of een deel daarvan) moet worden gehanteerd, de datum waarop een entiteit het niet-monetaire actief dat of de niet-monetaire verplichting die uit het doen of ontvangen van een vooruitbetaling voortvloeit, voor het eerst opneemt. 9. Indien er meerdere vooruitbetalingen worden gedaan of ontvangen, moet de entiteit elke keer als er een voor uitbetaling wordt gedaan of ontvangen, een transactiedatum bepalen.

Bijlage A

## Ingangsdatum En Overgang

Deze bijlage is een integraal onderdeel van IFRIC 22 en heeft hetzelfde gezag als de andere delen van IFRIC 22.

## Ingangsdatum

A1 Een entiteit moet deze interpretatie toepassen op jaarlijkse verslagperioden die op of na 1 januari 2018 aan vangen. Eerdere toepassing is toegestaan. Als een entiteit deze interpretatie op een eerdere periode toepast, moet zij dit feit vermelden.

## Overgang

A2 Bij eerste toepassing moet een entiteit deze interpretatie als volgt toepassen:
(a) ofwel retroactief toepassen bij de toepassing van IAS 8 Grondslagen voor financiële verslaggeving, schattings wijzigingen en fouten;
(b) ofwel prospectief toepassen op alle binnen het toepassingsgebied van de interpretatie vallende activa, baten en lasten die voor het eerst zijn opgenomen aan of na:
(i) het begin van de verslagperiode waarin de entiteit de interpretatie voor het eerst toepast; of
(ii) het begin van een voorafgaande verslagperiode die als vergelijkende informatie is gepresenteerd in de jaarrekening van de verslagperiode waarin de entiteit de interpretatie voor het eerst toepast. A3 Een entiteit die alinea A2(b) toepast, moet, bij eerste toepassing, de interpretatie toepassen op activa, baten en lasten die voor het eerst zijn opgenomen aan of na het begin van de in alinea A2(b)(i) of (ii) bedoelde ver slagperiode waarvoor de entiteit niet-monetaire activa of niet-monetaire verplichtingen had opgenomen die uit vooruitbetalingen vóór die datum voortvloeien.

Bijlage B De wijziging in deze bijlage moet worden toegepast op jaarlijkse verslagperioden die op of na 1 januari 2018 aanvangen. Indien een entiteit deze interpretatie op een eerdere periode toepast, moet deze wijziging voor die eerdere periode worden toegepast.
