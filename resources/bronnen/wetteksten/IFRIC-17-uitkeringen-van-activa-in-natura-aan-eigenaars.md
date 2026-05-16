---
title: IFRIC-17 — Uitkeringen van activa in natura aan eigenaars
tags:
- '1.5'
- ifrs
- ifric
itaa-lex-sectie: ''
wet: Verordening (EU) 2023/1803 — geconsolideerde IFRS
bron_rol: normatief
bron_categorie: ifrs
standaard_type: IFRIC
standaard_nummer: '17'
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
    pages: 964-966
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

IFRIC-INTERPRETATIE 17 Uitkeringen van activa in natura aan eigenaars

## Referenties

— IFRS 3 Bedrijfscombinaties (herziene versie van 2008) — IFRS 5 Vaste activa aangehouden voor verkoop en beëindigde bedrijfsactiviteiten — IFRS 7 Financiële instrumenten: informatieverschaffing — IFRS 10 Geconsolideerde jaarrekening — IFRS 13 Waardering tegen reële waarde — IAS 1 Presentatie van de jaarrekening (herziene versie van 2007) — IAS 10 Gebeurtenissen na de verslagperiode

## Achtergrond

1 Soms keert een entiteit andere activa dan geldmiddelen (activa in natura) uit als dividenden aan haar eigenaars ( 66 ) in hun hoedanigheid van eigenaars. Hierbij kan een entiteit haar eigenaars eventueel ook de keuze bieden tussen ontvangst van activa in natura of een alternatief in contanten. Het IFRIC heeft vragen ontvangen om leidraden te verschaffen over hoe een entiteit dergelijke uitkeringen moet verwerken. 2 De International Financial Reporting Standards (IFRSs) verschaffen geen leidraden voor de wijze waarop een entiteit uitkeringen aan haar eigenaars (gewoonlijk dividenden genoemd) moet waarderen. Op basis van IAS 1 moet een entiteit informatie presenteren over dividenden die zijn opgenomen als uitkeringen aan eigenaars, ofwel in het mutatieoverzicht van het eigen vermogen ofwel in de toelichting bij de jaarrekening.

## Toepassingsgebied

3 Deze interpretatie is van toepassing op de volgende soorten niet-wederkerige uitkeringen van activa door een entiteit aan haar eigenaars in hun hoedanigheid van eigenaars:
(a) uitkeringen van activa in natura (bv. materiële vaste activa, bedrijven zoals gedefinieerd in IFRS 3, eigen domsbelangen in een andere entiteit of groepen activa die worden afgestoten zoals gedefinieerd in IFRS 5); en
(b) uitkeringen die eigenaars de keuze laten tussen ontvangst van activa in natura of een alternatief in contanten. 4 Deze interpretatie is slechts van toepassing op uitkeringen waarbij alle eigenaars van dezelfde klasse van eigen vermogensinstrumenten gelijk worden behandeld. 5 Deze interpretatie is niet van toepassing op een uitkering van een actief in natura waarover dezelfde partij of partijen zowel vóór als na de uitkering de uiteindelijke zeggenschap heeft (hebben). Deze uitsluiting is van toepassing op de enkelvoudige, individuele en geconsolideerde jaarrekening van een entiteit die de uitkering doet. ( 66 ) In alinea 7 van IAS 1 worden eigenaars gedefinieerd als houders van als eigen vermogen geclassificeerde instrumenten.

6 In overeenstemming met alinea 5 is deze interpretatie niet van toepassing als dezelfde partijen zowel vóór als na de uitkering de uiteindelijke zeggenschap over het actief in natura hebben. In alinea B2 van IFRS 3 is het volgende bepaald: “Een groep personen moet worden geacht zeggenschap uit te oefenen over een entiteit indien die personen als gevolg van contractuele afspraken gezamenlijk de macht hebben om het financiële en ope rationele beleid van die entiteit te sturen teneinde voordelen te verkrijgen uit haar activiteiten”. Wil een uitkering buiten het toepassingsgebied van deze interpretatie vallen op basis van het feit dat dezelfde partijen zowel vóór als na de uitkering de zeggenschap hebben over het actief, dan moet een groep individuele aandeelhouders die de uitkering ontvangen, als gevolg van contractuele afspraken, dergelijke uiteindelijke gezamenlijke macht hebben over de entiteit die de uitkering doet. 7 In overeenstemming met alinea 5 is deze interpretatie niet van toepassing als een entiteit een aantal van haar eigendomsbelangen in een dochteronderneming uitkeert maar de zeggenschap over de dochteronderneming behoudt. Een entiteit die een uitkering doet die ertoe leidt dat de entiteit een belang zonder zeggenschap in haar dochteronderneming opneemt, verwerkt de uitkering overeenkomstig IFRS 10. 8 Deze interpretatie behandelt alleen de administratieve verwerking door een entiteit die activa in natura uitkeert. Ze behandelt niet de administratieve verwerking door aandeelhouders die een dergelijke uitkering ontvangen.

## Probleemstelling

9 Als een entiteit een uitkering aankondigt en een verplichting heeft de desbetreffende activa aan haar eigenaars uit te keren, moet ze een verplichting opnemen voor dit uit te keren dividend. In deze interpretatie worden de volgende vragen behandeld:
(a) Wanneer moet de entiteit de dividendverplichting opnemen?
(b) Hoe moet een entiteit de dividendverplichting waarderen?
(c) Wanneer een entiteit de dividendverplichting afwikkelt, hoe moet ze dan een eventueel verschil tussen de boekwaarde van de uitgekeerde activa en de boekwaarde van de dividendverplichting administratief ver werken?

## Consensus

Wanneer een dividendverplichting opnemen 10 De verplichting om een dividend uit te keren moet worden opgenomen wanneer het dividend op de juiste wijze is goedgekeurd en de entiteit er niet langer over beschikt, zijnde de datum:
(a) waarop de dividendaankondiging, gedaan door bijvoorbeeld het management of de raad van bestuur, wordt goedgekeurd door de bevoegde autoriteit, bijvoorbeeld de aandeelhouders, indien dergelijke goedkeuring in het betrokken rechtsgebied vereist is; of
(b) waarop de dividendaankondiging wordt gedaan, bijvoorbeeld door het management of de raad van bestuur, indien in het betrokken rechtsgebied geen verdere goedkeuring vereist is. Waardering van een dividendverplichting 11 Een entiteit moet een verplichting om activa in natura als dividend aan haar eigenaars uit te keren, waarderen tegen de reële waarde van de uit te keren activa. 12 Als een entiteit haar eigenaars de keuze laat tussen ontvangst van een actief in natura of een alternatief in contanten, moet ze bij het schatten van de dividendverplichting rekening houden met zowel de reële waarde van elk alternatief als de waarschijnlijkheid dat het door eigenaars wordt gekozen.

13 Aan het eind van elke verslagperiode en op de datum van afwikkeling moet de entiteit de boekwaarde van de dividendverplichting beoordelen en aanpassen, waarbij eventuele veranderingen in de boekwaarde van de divi dendverplichting in het eigen vermogen moeten worden opgenomen als aanpassingen aan het uit te keren bedrag. Administratieve verwerking van een eventueel verschil tussen de boekwaarde van de uitgekeerde activa en de boekwaarde van de dividendverplichting wanneer een entiteit de dividendverplichting afwikkelt 14 Wanneer een entiteit de dividendverplichting afwikkelt, moet ze het verschil, in voorkomend geval, tussen de boekwaarde van de uitgekeerde activa en de boekwaarde van de dividendverplichting in de winst of het verlies opnemen. Presentatie en informatieverschaffing 15 Een entiteit moet het in alinea 14 beschreven verschil als een afzonderlijke post in winst of verlies presenteren. 16 Een entiteit moet de volgende informatie verschaffen, indien van toepassing:
(a) de boekwaarde van de dividendverplichting aan het begin en einde van de periode; en
(b) de toename of afname van de boekwaarde opgenomen in de periode overeenkomstig alinea 13 als gevolg van een verandering van de reële waarde van de uit te keren activa. 17 Als een entiteit na het einde van een verslagperiode maar voordat de jaarrekening wordt goedgekeurd, voor publicatie aankondigt een actief in natura als dividend te willen uitkeren, moet ze het volgende vermelden:
(a) de aard van het uit te keren actief;
(b) de boekwaarde van het uit te keren actief aan het eind van de verslagperiode; en
(c) de reële waarde van het uit te keren actief aan het eind van de verslagperiode, indien deze verschilt van zijn boekwaarde, en de informatie die op grond van de alinea’s 93(b), (d), (g) en (i) en 99 van IFRS 13 moet worden verstrekt over de methode(n) die is (zijn) gebruikt om die reële waarde te bepalen.

## Ingangsdatum

18 Entiteiten moeten deze interpretatie prospectief toepassen op jaarperioden die op of na 1 juli 2009 aanvangen. Retroactieve toepassing is niet toegestaan. Eerdere toepassing is toegestaan. Als een entiteit deze interpretatie toepast op een periode die vóór 1 juli 2009 aanvangt, moet ze dat feit vermelden en moet ze eveneens IFRS 3 (herziene versie van 2008), IAS 27 (herziene versie van mei 2008) en IFRS 5 (gewijzigd door deze interpretatie) toepassen. 19 IFRS 10, uitgegeven in mei 2011, wijzigde alinea 7. Een entiteit moet deze wijziging toepassen wanneer ze IFRS 10 toepast. 20 IFRS 13, uitgegeven in mei 2011, wijzigde alinea 17. Een entiteit moet deze wijziging toepassen wanneer ze IFRS 13 toepast.
