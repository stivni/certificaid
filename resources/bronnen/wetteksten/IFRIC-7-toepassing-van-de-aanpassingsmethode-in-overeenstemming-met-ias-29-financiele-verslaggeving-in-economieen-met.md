---
title: IFRIC-7 — Toepassing van de aanpassingsmethode in overeenstemming met IAS 29
  Financiële verslaggeving in economieën met
tags:
- '1.5'
- ifrs
- ifric
itaa-lex-sectie: ''
wet: Verordening (EU) 2023/1803 — geconsolideerde IFRS
bron_rol: normatief
bron_categorie: ifrs
standaard_type: IFRIC
standaard_nummer: '7'
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
    pages: 941-942
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

IFRIC-INTERPRETATIE 7 Toepassing van de aanpassingsmethode in overeenstemming met IAS 29 Financiële verslaggeving in economieën met hyperinflatie

## Referenties

— IAS 12 Winstbelastingen — IAS 29 Financiële verslaggeving in economieën met hyperinflatie

## Achtergrond

1 Deze interpretatie biedt een leidraad voor de wijze waarop de vereisten van IAS 29 moeten worden toegepast in een verslagperiode waarin een entiteit het bestaan van hyperinflatie in de economie van haar functionele valuta con stateert ( 61 ), terwijl deze economie in de voorgaande verslagperiode niet met hyperinflatie te kampen had, en de entiteit bijgevolg haar jaarrekening aanpast in overeenstemming met IAS 29.

## Probleemstelling

2 In deze interpretatie worden de volgende vragen behandeld:
(a) hoe moet het in alinea 8 van IAS 29 vastgelegde vereiste “… gepresenteerd in termen van de maateenheid die op het einde van de verslagperiode wordt gebruikt” worden geïnterpreteerd wanneer een entiteit de standaard toepast?
(b) hoe moet een entiteit uitgestelde belastingvorderingen en -verplichtingen aan het begin van het jaar in haar aangepaste jaarrekening verwerken?

## Consensus

3 In de verslagperiode waarin een entiteit het bestaan van hyperinflatie in de economie van haar functionele valuta constateert, terwijl deze economie in de voorgaande verslagperiode niet met hyperinflatie te kampen had, moet de entiteit de vereisten van IAS 29 toepassen alsof de economie altijd met hyperinflatie te kampen heeft gehad. Wat tegen de historische kostprijs gewaardeerde niet-monetaire posten betreft, moet het openingsoverzicht van de finan ciële positie van de entiteit aan het begin van de vroegste periode die in de jaarrekening wordt gepresenteerd, bijgevolg voor het effect van de inflatie worden aangepast vanaf de datum waarop de activa werden verworven en de verplichtingen werden aangegaan tot het einde van de verslagperiode. Voor niet-monetaire posten die in het openingsoverzicht van de financiële positie worden verantwoord op bedragen die actueel zijn op andere data dan de datum waarop de activa werden verworven of de verplichtingen werden aangegaan, moet deze aanpassing daar entegen het effect van de inflatie weerspiegelen vanaf de data waarop deze boekwaarden zijn bepaald tot het einde van de verslagperiode. 4 Op het einde van de verslagperiode worden de uitgestelde belastingvorderingen en -verplichtingen opgenomen en gewaardeerd in overeenstemming met IAS 12. De in het openingsoverzicht van de financiële positie voor de ver slagperiode opgenomen bedragen met betrekking tot uitgestelde belastingen worden evenwel als volgt bepaald:
(a) de entiteit herbepaalt de waarde van de uitgestelde belastingvorderingen en -verplichtingen in overeenstemming met IAS 12 nadat zij de nominale boekwaarden van de niet-monetaire posten op de datum van het openings overzicht van de financiële positie van de verslagperiode heeft aangepast door de op die datum geldende maat eenheid toe te passen;
(b) de uitgestelde belastingvorderingen en -verplichtingen waarvan de waarde overeenkomstig (a) is herbepaald, worden voor de wijziging in de maateenheid aangepast vanaf de datum van het openingsoverzicht van de financiële positie van de verslagperiode tot het einde van die verslagperiode. De entiteit past de in (a) en (b) beschreven methode toe voor de aanpassing van de uitgestelde belastingvorderingen en -verplichtingen die zijn opgenomen in het openingsoverzicht van de financiële positie van alle vergelijkende perioden die worden gepresenteerd in de aangepaste jaarrekening voor de verslagperiode waarin de entiteit IAS 29 toepast. 5 Nadat een entiteit haar jaarrekening heeft aangepast, worden alle overeenkomstige cijfers in de jaarrekening voor een daaropvolgende verslagperiode, met inbegrip van uitgestelde belastingvorderingen en -verplichtingen, aangepast door de wijziging in de maateenheid voor de daaropvolgende verslagperiode alleen op de aangepaste jaarrekening voor de voorgaande verslagperiode toe te passen. ( 61 ) De constatering van het bestaan van hyperinflatie is gebaseerd op de beoordeling door de entiteit van de criteria die zijn opge nomen in alinea 3 van IAS 29.

## Ingangsdatum

6 Een entiteit moet deze interpretatie toepassen op jaarperioden die op of na 1 maart 2006 aanvangen. Eerdere toepassing wordt aanbevolen. Als een entiteit deze interpretatie toepast op financiële overzichten die betrekking hebben op een verslagperiode die vóór 1 maart 2006 aanvangt, moet zij dit feit vermelden.
