---
title: IFRIC-5 — Belangen in ontmantelings-, herstel- en milieusaneringsfondsen
tags:
- '1.5'
- ifrs
- ifric
itaa-lex-sectie: ''
wet: Verordening (EU) 2023/1803 — geconsolideerde IFRS
bron_rol: normatief
bron_categorie: ifrs
standaard_type: IFRIC
standaard_nummer: '5'
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
    pages: 936-938
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

IFRIC-INTERPRETATIE 5 Belangen in ontmantelings-, herstel- en milieusaneringsfondsen

## Referenties

— IFRS 9 Financiële instrumenten — IFRS 10 Geconsolideerde jaarrekening — IFRS 11 Gezamenlijke overeenkomsten — IAS 8 Grondslagen voor financiële verslaggeving, schattingswijzigingen en fouten — IAS 28 Investeringen in geassocieerde deelnemingen en joint ventures — IAS 37 Voorzieningen, voorwaardelijke verplichtingen en voorwaardelijke activa

## Achtergrond

1 Ontmantelings-, herstel- en milieusaneringsfondsen, hierna “ontmantelingsfondsen ” of “fondsen” genoemd, hebben tot doel activa te scheiden met het oog op de financiering van alle kosten, of een deel daarvan, van de ont manteling van een fabriek (bv. een kerncentrale) of bepaalde bedrijfsmiddelen (bv. auto’s), of van alle kosten, of een deel daarvan, van een milieusanering (zoals de zuivering van vervuild water of het herstel van gronden waar mijnbouw heeft plaatsgevonden), gezamenlijk “ontmanteling” genoemd. 2 Bijdragen aan deze fondsen kunnen vrijwillig zijn of bij wet- en regelgeving zijn voorgeschreven. De fondsen kunnen een van de volgende structuren hebben:
(a) fondsen die door één contribuant zijn opgericht om zijn eigen ontmantelingsverplichtingen te financieren, hetzij voor een bepaald terrein, hetzij voor een aantal geografisch verspreide terreinen;
(b) fondsen die zijn opgericht met verschillende contribuanten om hun individuele of gezamenlijke ontmantelings verplichtingen te financieren, waarbij contribuanten recht hebben op vergoeding van de ontmantelingskosten tot het niveau van hun bijdragen plus eventuele werkelijke winsten op deze bijdragen verminderd met hun aandeel in de kosten voor het beheer van het fonds. Contribuanten kunnen een verplichting hebben om aanvullende bijdragen te betalen, bijvoorbeeld in geval van het faillissement van een andere contribuant;
(c) fondsen die zijn opgericht met verschillende contribuanten ter financiering van hun individuele of gezamenlijke ontmantelingsverplichtingen waarbij de vereiste omvang van de bijdragen gebaseerd is op de huidige activi teiten van een contribuant, en het door die contribuant verkregen voordeel gebaseerd is op zijn activiteiten in het verleden. In dergelijke gevallen is er een mogelijke mismatch tussen het bedrag van de door een contribuant betaalde bijdragen (op basis van zijn huidige activiteiten) en de waarde die uit het fonds kan worden gerea liseerd (op basis van activiteiten in het verleden). 3 Dergelijke fondsen hebben doorgaans de volgende kenmerken:
(a) het fonds wordt afzonderlijk beheerd door onafhankelijke beheerders;
(b) entiteiten (contribuanten) betalen bijdragen aan het fonds die worden belegd in diverse activa die zowel schuldbewijzen als eigenvermogensinstrumenten kunnen omvatten, en die beschikbaar zijn om de ontmante lingskosten van de contribuanten te helpen betalen. De beheerders bepalen hoe bijdragen worden belegd, binnen de beperkingen die zijn vastgelegd in de statuten van het fonds en in eventuele toepasselijke wetgeving of andere voorschriften;
(c) de contribuanten blijven verplicht om de ontmantelingskosten te betalen. Contribuanten kunnen van het fonds een vergoeding ontvangen voor de ontmantelingskosten, tot het laagste bedrag van de gemaakte ontmante lingskosten en het aandeel van de contribuant in de activa van het fonds;

(d) de contribuanten kunnen beperkte of geen rechten hebben ten aanzien van een eventueel surplus aan activa van het fonds boven de activa die worden gebruikt om daarvoor in aanmerking komende ontmantelingskosten te vergoeden.

## Toepassingsgebied

4 Deze interpretatie is van toepassing op de administratieve verwerking in de jaarrekening van een contribuant van de belangen in ontmantelingsfondsen die beide van de volgende kenmerken hebben:
(a) de activa worden afzonderlijk beheerd (hetzij doordat ze worden aangehouden in een afzonderlijke rechts persoon of als gescheiden activa binnen een andere entiteit); en
(b) de contribuant heeft slechts een beperkt recht op toegang tot de activa. 5 Een overblijvend belang in een fonds dat verder gaat dan een recht op vergoeding, zoals een contractueel recht op uitkeringen zodra de volledige ontmanteling is voltooid of bij de liquidatie van het fonds, kan een binnen het toepassingsgebied van IFRS 9 vallend eigenvermogensinstrument zijn en valt niet binnen het toepassingsgebied van deze interpretatie.

## Probleemstelling

6 In deze interpretatie worden de volgende punten behandeld:
(a) hoe moet een contribuant zijn belang in een fonds administratief verwerken?
(b) wanneer een contribuant verplicht is om aanvullende bijdragen te doen, bijvoorbeeld in geval van het faillisse ment van een andere contribuant, hoe moet die verplichting dan administratief worden verwerkt?

## Consensus

Administratieve verwerking van een belang in een fonds 7 De contribuant moet zijn verplichting om ontmantelingskosten te betalen opnemen als een verplichting en moet zijn belang in het fonds afzonderlijk verwerken, tenzij hij niet verplicht is ontmantelingskosten te betalen, zelfs niet als het fonds niet uitkeert. 8 De contribuant moet bepalen of hij over het fonds zeggenschap, gezamenlijke zeggenschap of invloed van betekenis heeft op basis van IFRS 10, IFRS 11 en IAS 28. Als dit het geval is, moet de contribuant zijn belang in het fonds administratief verwerken in overeenstemming met die standaarden. 9 Als een contribuant geen zeggenschap of gezamenlijke zeggenschap heeft over, of invloed van betekenis heeft op, het fonds, moet hij het recht op ontvangst van een vergoeding uit het fonds opnemen als een vergoeding in overeenstemming met IAS 37. Deze vergoeding zal worden gewaardeerd tegen het laagste bedrag van:
(a) het bedrag van de opgenomen ontmantelingsverplichting; en
(b) het aandeel van de contribuant in de reële waarde van de nettoactiva van het fonds die aan contribuanten kunnen worden toegerekend. Wijzigingen in de boekwaarde van het recht op vergoedingen anders dan bijdragen aan en uitkeringen door het fonds moeten in winst of verlies worden opgenomen in de periode waarin die wijzigingen plaatsvinden. Administratieve verwerking van verplichtingen om aanvullende bijdragen te doen 10 Wanneer een contribuant een verplichting heeft om mogelijke aanvullende bijdragen te doen, bijvoorbeeld in geval van het faillissement van een andere contribuant of als de waarde van de door het fonds aangehouden beleggingen dermate daalt dat deze activa niet volstaan om de vergoedingsverplichtingen van het fonds na te komen, is die verplichting een voorwaardelijke verplichting die binnen het toepassingsgebied van IAS 37 valt. De contribuant moet alleen een verplichting opnemen als het waarschijnlijk is dat er aanvullende bijdragen zullen worden gedaan.

## Informatieverschaffing

11 Een contribuant moet de aard van zijn belang in een fonds en beperkingen inzake de toegang tot de activa in het fonds in de toelichting vermelden. 12 Als een contribuant een verplichting heeft om mogelijke aanvullende bijdragen te betalen die niet is opgenomen als een verplichting (zie alinea 10), moet hij de informatie verstrekken die vereist is op grond van alinea 86 van IAS 37. 13 Als een contribuant zijn belang in het fonds administratief verwerkt overeenkomstig alinea 9, moet hij de infor matie verstrekken die vereist is op grond van alinea 85(c) van IAS 37.

## Ingangsdatum

14 Een entiteit moet deze interpretatie toepassen op jaarperioden die op of na 1 januari 2006 aanvangen. Eerdere toepassing wordt aanbevolen. Als een entiteit deze interpretatie toepast op een verslagperiode die vóór 1 januari 2006 aanvangt, moet zij dit feit vermelden. 14A [Verwijderd] 14B De alinea’s 8 en 9 worden gewijzigd door IFRS 10 en IFRS 11 (vastgesteld in mei 2011). Een entiteit moet deze wijzigingen toepassen wanneer zij IFRS 10 en IFRS 11 toepast. 14C [Verwijderd] 14D Alinea 5 is gewijzigd en de alinea’s 14A en 14C zijn verwijderd door IFRS 9, als uitgegeven in juli 2014. Een entiteit moet die wijzigingen toepassen wanneer zij IFRS 9 toepast.

## Overgang

15 Wijzigingen in de grondslagen voor financiële verslaggeving moeten administratief worden verwerkt overeenkom stig de vereisten van IAS 8.
