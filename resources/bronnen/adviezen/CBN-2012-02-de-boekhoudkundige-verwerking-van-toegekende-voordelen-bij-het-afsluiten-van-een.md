---
bron: https://www.cbn-cnc.be/nl/adviezen/de-boekhoudkundige-verwerking-van-toegekende-voordelen-bij-het-afsluiten-van-een
datum: 2012-01-11
gerelateerde_adviezen:
  - datum: '2021-06-23'
    titel: Rekening 26 Overige materiële vaste activa
    url: https://www.cbn-cnc.be/nl/adviezen/rekening-26-overige-materiele-vaste-activa
  - datum: '2021-04-06'
    titel: Boekhoudrechtelijke behandeling van kwijtschelding van huur ten gevolge van de COVID-19-pandemie
    url: https://www.cbn-cnc.be/nl/adviezen/boekhoudrechtelijke-behandeling-van-kwijtschelding-van-huur-ten-gevolge-van-de-covid-19
  - datum: '2015-06-24'
    titel: Leasing
    url: https://www.cbn-cnc.be/nl/adviezen/leasing
  - datum: '1986-07-01'
    titel: Bouwwerken op andermans grond
    url: https://www.cbn-cnc.be/nl/adviezen/bouwwerken-op-andermans-grond
nummer: CBN-advies 2012/2
themas:
  - Huur
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/de-boekhoudkundige-verwerking-van-toegekende-voordelen-bij-het-afsluiten-van-een
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: ccd9afd
    model:
    prompt_version:
  generated_at: '2026-05-12T22:48:05Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-12T22:59:56Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: Geen ETL-artefacten aangetroffen. Heading-structuur aanwezig (9 headings), inhoud volledig, voetnoten correct gerenderd, geen form-feeds of column-bleed.
    layer1:
      status: pass
      run_id: 20260512-225123
      run_at: '2026-05-12T22:51:27Z'
      heading_count: 8
      max_section_chars: 2369
      file_size_chars: 6121
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-12T22:59:56Z'
      rationale: Geen ETL-artefacten aangetroffen. Heading-structuur aanwezig (9 headings), inhoud volledig, voetnoten correct gerenderd, geen form-feeds of column-bleed.
      concrete_problemen: []
---
# CBN-advies 2012/2 – De boekhoudkundige verwerking van toegekende voordelen bij het afsluiten van een huurovereenkomst

## Inleiding
Bij het onderhandelen van een nieuwe huurovereenkomst of de verlenging van een bestaande huurovereenkomst, voorziet de verhuurder soms voordelen die de huurder kan genieten bij afsluiting van de overeenkomst. Voorbeelden van dergelijke voordelen zijn: de betaling van een vergoeding bij het tekenen van de overeenkomst, het vergoeden door de verhuurder van door de huurder gemaakte kosten (zoals verhuiskosten, aanpassingen aan het vastgoed en opzegvergoedingen verbonden aan de bestaande huurovereenkomst). Het komt ook voor dat de huurder gedurende de eerste maanden van de nieuwe huurovereenkomst geen (“gratuïteiten”) of slechts een lagere huur dient te betalen.

## Waarderingregels
### Algemeen
Artikel 33, tweede lid van het koninklijk besluit van 30 januari 2001 tot uitvoering van het Wetboek van Vennootschappen (hierna KB W.Venn.) vereist dat er rekening wordt gehouden met de kosten en de opbrengsten die betrekking hebben op het boekjaar of op voorgaande boekjaren, ongeacht de dag waarop deze kosten en opbrengsten worden betaald of geïnd, behalve indien de effectieve inning van deze opbrengsten onzeker is. 

Verder stelt het bewuste artikel dat, wanneer de opbrengsten of de kosten in belangrijke mate worden beïnvloed door opbrengsten of kosten die aan een ander boekjaar moeten worden toegerekend, daarvan melding dient te worden gemaakt in de toelichting.

### Boekhoudkundige verwerking
#### De verhuurder
De voordelen aan de huurder worden verondersteld integraal deel uit te maken van de huurovereenkomst, ongeacht de aard, vorm of tijdstip van betalingen. 

De verhuurder zal de totale kost verbonden aan de voordelen gedurende de huurperiode lineair (tenzij een andere systematische basis representatief is voor het tijdspatroon volgens hetwelk het voordeel van het gehuurde actief afneemt) in resultaat opnemen als een vermindering van de huuropbrengsten. De Commissie is de mening toegedaan dat, gezien de huuropbrengsten en de toegekende voordelen hun oorsprong vinden in dezelfde contractuele overeenkomst, deze tevens vanuit een boekhoudkundig standpunt samen moeten verwerkt worden.

### Voorbeeld
Bij het afsluiten van een huurovereenkomst biedt de verhuurder aan de huurder bij wijze van compensatie voor de gemaakte kosten gedurende de verhuis gratuïteiten aan. Dit voordeel houdt in dat de huurder gedurende de eerste twee maanden geen huur dient te betalen. De huurperiode bedraagt 3 jaren. Als gevolg van dit voordeel realiseert de huurder een besparing van 36.000 €.
Het voordeel zal als volgt boekhoudkundig worden verwerkt.
De huurovereenkomst heeft een looptijd van 36 maanden. De maandelijkse huur bedraagt normalerwijze 18.000 €. Gezien de gratuïteiten over de looptijd in resultaat zullen worden genomen, zal de verhuurder maandelijks slechts een opbrengst van 17.000 € in zijn resultatenrekening erkennen.
Gedurende de eerste twee maanden zal de verhuurder dus de volgende boeking verrichten:

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 491 | Verkregen opbrengsten | 17.000 | |
| aan | 744 | Huuropbrengsten | | 17.000 |

Gedurende de daaropvolgende maanden zal de verhuurder maandelijks de volgende boeking verrichten:
| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 550 | Kredietinstelling: rekening-courant | 18.000 | |
| aan | 491 | Verkregen opbrengsten | | 1.000 |
| | 744 | Huuropbrengsten | 17.000 | |

Indien de overeenkomst vroegtijdig zou worden ontbonden, wordt het saldo van de overlopende rekening onmiddellijk als periodekost erkend.
#### De huurder
De huurder zal de opbrengst verbonden aan de voordelen gedurende de huurperiode lineair (tenzij een andere systematische basis representatief is voor het tijdspatroon volgens hetwelk het voordeel van het gehuurde actief afneemt) in resultaat boeken als een vermindering van de huurkosten. De Commissie is de mening toegedaan dat, gezien de huurkosten en de verkregen voordelen hun oorsprong vinden in dezelfde contractuele overeenkomst, deze tevens vanuit een boekhoudkundig standpunt samen moeten verwerkt worden. 

Andere kosten die werden gemaakt als gevolg van het aangaan van de huurovereenkomst (bijvoorbeeld opzegvergoedingen, verhuiskosten of aanpassingen aan het vastgoed) en die betrekking hebben op het boekjaar of op voorgaande boekjaren zullen in overeenstemming met artikel 33 van het KB W.Venn gedurende het boekjaar in de resultatenrekening worden verwerkt.

### Voorbeeld
Bij het afsluiten van een huurovereenkomst biedt de verhuurder aan de huurder, bij wijze van compensatie voor de gemaakte kosten gedurende de verhuis, gratuïteiten aan. Dit voordeel houdt in dat de huurder gedurende de eerste twee maanden geen huur dient te betalen. De huurperiode bedraagt 3 jaren. Als gevolg van dit voordeel realiseert de huurder een besparing van 36.000 €.
Het voordeel zal als volgt boekhoudkundig worden verwerkt.
De huurovereenkomst heeft een looptijd van 36 maanden. De maandelijkse huur bedraagt normalerwijze 18.000 €. Gezien de gratuïteiten over de looptijd in resultaat zullen worden genomen, zal de huurder maandelijks slechts een kost van 17.000 € in zijn resultatenrekening boeken.
Gedurende de eerste twee maanden zal de huurder dus de volgende boeking verrichten:

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 610 | Huur en huurlasten | 17.000 | |
| aan | 492 | Toe te rekenen kosten | | 17.000 |

Gedurende de daaropvolgende maanden zal de huurder maandelijks de volgende boeking verrichten:
| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 610 | Huur en huurlasten | 17.000 | |
| | 492 | Toe te rekenen kosten | 1.000 | |
| aan | 550 | Kredietinstelling: rekening-courant | | 18.000 |

Indien de overeenkomst vroegtijdig zou worden ontbonden, wordt het saldo van de overlopende rekening onmiddellijk als opbrengst van de periode erkend.
