---
bron: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-afvalstoffen
datum: 1995-03-01
nummer: CBN-advies 171
provenance:
  generated_at: '2026-05-11T19:17:26Z'
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-afvalstoffen
      sha256: ef019e5fa8d5ff93cfeecf2422b2fa22e0858ffe7d0bbce9d35b95e64f9dcf00
      version:
  stale: false
  stale_reason:
  tooling:
    model:
    pipeline: tools/etl/convert.py
    pipeline_version: 11f9196
    prompt_version:
  trust:
    confirmed_at: '2026-05-11T17:05:21Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      status: pass
      run_id: 20260511-191727
      run_at: '2026-05-11T19:17:29Z'
      heading_count: 6
      max_section_chars: 10337
      file_size_chars: 12010
      flags: []
    layer2:
      agent: subagent-sonnet-4-6
      concrete_problemen:
        - categorie: A9
          regel: 96
          type: ocr-confusion
          voorbeeld: '| | 602 | AAankopen van diensten of | | |'
        - categorie: A6
          regel: 198
          type: other
          voorbeeld: '...zal enkel voor de tweede benadering kunnen worden \n\ngeopteerd.'
      rationale: 'Vorig verdict bevestigd. A9 r.96: ''| | 602 | AAankopen van diensten of | | |'' — dubbele ''A'' (OCR-duplicatie). A6 r.198-200: slotzin ''zal enkel voor de tweede benadering kunnen worden'' gevolgd door een lege regel en ''geopteerd.'' op een nieuwe alinea — afgebroken alinea-patroon.'
      run_at: '2026-05-11T17:05:21Z'
      status: needs-rework
    rationale: 'Vorig verdict bevestigd. A9 r.96: ''| | 602 | AAankopen van diensten of | | |'' — dubbele ''A'' (OCR-duplicatie). A6 r.198-200: slotzin ''zal enkel voor de tweede benadering kunnen worden'' gevolgd door een lege regel en ''geopteerd.'' op een nieuwe alinea — afgebroken alinea-patroon.'
    status: needs-rework
themas:
  - afvaldienstenonderneming
  - afvalstoffen
  - exploitatie van een stortplaats, steengroeve, kerncentrale, booreiland
  - financiële kosten
  - gereed produkt
  - goederen in bewerking
  - ondernemingen die afvalstoffen produceren
  - ophaling van afvalstoffen
  - sanering terrein
  - vervaardigingsprijs
  - Voorraad afvalstoffen
  - voorraden
---

# CBN advies 171 - Boekhoudkundige verwerking van afvalstoffen
Aan de Commissie werd gevraagd hoe de produktie, de ophaling, de vernietiging, de verwerking of de recyclage van afvalstoffen alsook de exploitatie van stortplaatsen in de jaarrekening van ondernemingen moeten worden verwerkt. De ondernemingen, zoals trouwens ook de overheid, worden immers met steeds grotere afvalverwerkingsproblemen geconfronteerd. De Commissie heeft derhalve beslist daaraan een algemeen advies te wijden. 

Dit advies slaat echter niet op de waardering van de voorzieningen die de ondernemingen moeten vormen voor de dekking van hun eventuele aansprakelijkheid die zal voortvloeien uit de productie, de verwerking, het vervoer of het bezit van afvalstoffen of het storten ervan op een stortplaats. 

Dit advies zal achtereenvolgens aandacht besteden aan de ondernemingen die afvalstoffen "produceren", de ondernemingen die diensten verstrekken op het vlak van de ophaling of de verwerking van afvalstoffen en, ten slotte, de ondernemingen waarvan de exploitatie een terrein aantast of vervuilt. 

## Ondernemingen die afvalstoffen "produceren"
##### De onderneming verwerkt haar afvalstoffen niet zelf, maar belast een derde met de ophaling ervan
Voor die onderneming is de ophaling van haar afvalstoffen door een derde een dienst die haar wordt verleend, waarvan de kost als bedrijfskost onder *Diensten en diverse goederen* (rekening 61) moet worden geboekt.

Voor de afvalstoffen die, aan het einde van de boekhoudperiode, nog niet zouden zijn opgehaald, zal een voorziening moeten worden gevormd om de ophalingskosten te dekken. 

##### De onderneming verwerkt zelf haar afvalstoffen
    Voor die onderneming vormt de kost voor de afvalverwerking een bedrijfskost die wordt geboekt in de verschillende rekeningen van kosten naar hun aard. 

   Voor de afvalstoffen die, aan het einde van de boekhoudperiode, nog niet zouden zijn verwerkt, zal een voorziening moeten worden gevormd om de verwerkingskosten te dekken. 

## Afvaldienstenondernemingen
De onderneming zorgt voor de ophaling van de afvalstoffen alsook voor de onmiddellijke storting of afvoer "als zodanig", d.i. zonder opslag of verwerking
De facturatie van de afvalophaling zal als volgt worden geboekt :

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 400 | Handelsdebiteuren | | |
| aan | 70 | Verkopen en dienstprestaties | | |
| | 451 | Te betalen btw | | |

De facturatie ten laste van diezelfde onderneming in verband met de overdracht of het storten van afvalstoffen, zal als volgt worden geboekt : 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 602 | AAankopen van diensten of | | |
| | 61 | Diensten en diverse goederen | | |
| | 411 | Terug te vorderen btw | | |
| aan | 440 | Leveranciers | | |
| | 451 | Te betalen btw | | |

De onderneming zorgt voor de ophaling en de opslag van de afvalstoffen in afwachting van hun latere overdracht aan een derde die ze zal verwerken
De verrichtingen met derden worden op dezelfde manier geboekt als in de onder A hierboven vermelde gevallen. 

De verworven maar nog niet afgevoerde afvalstoffen vormen geen voorraden als bedoeld in de boekhoudreglementering waar de voorraden (grondstoffen of goederen) kosten vormen waarvan de inresultaatneming via de rekening van de voorraadwijziging is; uitgesteld tot het boekjaar waarin de voorraden worden verbruikt, maar zij worden ingecalculeerd in materiële roerende goederen bestemd om als zodanig te worden doorverkocht, om te worden omgevormd of gebruikt in het productieproces, en die dienovereenkomstig op de balans onder de activa worden geboekt. De voorraden van goederen in bewerking en van afgewerkte produkten vertegenwoordigen op hun beurt kosten die worden ingecalculeerd in goederen in bewerking of goederen die kunnen worden verkocht. De ophaling, de opslag of de verwerking van afvalstoffen vormt daarentegen een opbrengst die de onderneming effectief ontvangt. In de veronderstelling echter dat de economische cyclus niet is voltooid - en dat is het geval met verworven afvalstoffen die nog niet zijn afgevoerd door de onderneming[^1]
- betreft het een opbrengst die is ontvangen maar nog niet verworven en die bijgevolg moet worden overgedragen. Daaruit vloeit voort dat, aan het einde van de boekhoudperiode, het bedrag van de opbrengsten die bij de aanschaffing van de afvalstoffen als omzet zijn geboekt, zal moeten worden gecorrigeerd naar verhouding van de wijzigingen in de "voorraad" afvalstoffen die de onderneming bezit, via een boeking van het volgende type : 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 70 | Verkopen en dienstprestaties | | |
| aan | 493 | Over te dragen opbrengsten | | |

### wanneer de "voorraad" toeneemt, en
| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 493 | Over te dragen opbrengsten | | |
| aan | 70 | Verkopen en dienstprestaties | | |

wanneer de "voorraad" afneemt.
De onderneming verwerft de afvalstoffen om ze (a) te vernietigen, (b) in haar eigen produktieproces te gebruiken of (c) te recycleren
Zoals in beide voornoemde gevallen, zal de facturatie van de ophaling en de ontvangst van de afvalstoffen als volgt worden geboekt : 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 400 | Handelsdebiteuren | | |
| aan | 70... | Verkopen en dienstprestaties | | |
| | 451 | Te betalen B.T.W. | | |

1. De verworven afvalstoffen worden vernietigd 

	De kosten verbonden aan de vernietiging van de afvalstoffen worden geboekt in de verschillende rekeningen van kosten naar hun aard (hulpstoffen, diensten en diverse goederen, bezoldigingen, afschrijvingen, enz.). 

	Aan het einde van de boekhoudperiode zal de gerealiseerde omzet voor de ophaling van de afvalstoffen, worden gecorrigeerd naar verhouding van de wijziging in de "voorraad" afvalstoffen die nog moet worden vernietigd, volgens de regels 2.2. hierboven. 
2. De verworven afvalstoffen worden gebruikt in het productieproces (bij voorbeeld als brandstof) 

	In het productieproces zijn er aan het gebruik van die afvalstoffen, wat de aankoopprijs betreft, geen rechtstreekse kosten verbonden. 

	Het is echter niet uitgesloten en wellicht waarschijnlijk dat het gebruik van afvalstoffen in plaats van andere producten in het productieproces, over het algemeen zal leiden tot een stijging van de bedrijfskosten, die wordt gecompenseerd door de inkomsten verworven bij de ophaling van de betrokken afvalstoffen. De kosten die voortvloeien uit het gebruik van de afvalstoffen zullen bijgevolg in de resultatenrekening worden geboekt als diverse kosten naar hun aard. Als dat het geval is voor de betrokken onderneming, zal het als omzet geboekte bedrag aan het einde van de boekhoudperiode volgens de voornoemde regels moeten worden gecorrigeerd naar verhouding van de wijziging in de voorraad afvalstoffen die de onderneming op die datum bezit. 
3. De afvalstoffen worden gerecycleerd en vervolgens doorverkocht De recyclage van afvalstoffen zal als volgt worden geboekt: 
- *Verwerkingskosten*  

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 6.. | Diverse kosten naar hun aard | | |
| aan | ... | Verschillende passief- of creditrekeningen | | |

- *Verkoop van gerecycleerde producten*  

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 400 | Handelsdebiteuren | | |
| aan | 70... | Verkopen en dienstprestaties | | |
| | 451 | Te betalen btw | | |

- *Wijzigingen in de "voorraden" afvalstoffen* 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 493 | Over te dragen opbrengsten | | |
| aan | 70... | Verkopen en dienstprestaties | | |

of

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 493 | Over te dragen opbrengsten | | |
| aan | 70... | Verkopen en dienstprestaties | | |

- *Wijzigingen in de voorraad gerecycleerde producten* 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 32 (33) | Goederen in bewerking (Gereed product) | | |
| aan | 712 (713) | Wijzigingen in de voorraad goederen in bewerking (Wijzigingen in de voorraad gereed product) | | |

of 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 712 (713) | Wijzigingen in de voorraad goederen in bewerking (Wijzigingen in de voorraad gereed product) | | |
| aan | 32 (33) | Goederen in bewerking (Gereed product) | | |

Wanneer er verschillen zijn tussen de facturatieprijs voor de ophaling of de verwerving van afvalstoffen, zal, wat de wijzigingen in de "voorraden" afvalstoffen betreft, bij de correctieboekingen met betrekking tot het omzetcijfer rekening moeten worden gehouden met een welbepaalde volgorde van de uitgaande voorraden. Naar analogie van de regels voor uitgaande voorraden in de echte zin van het woord, zal de onderneming moeten kiezen tussen een van de methodes bedoeld in artikel 33 van het koninklijk besluit van 8 oktober 1976, namelijk : individualisering van de prijs van elk bestanddeel, gewogen gemiddelde, eerst in -eerst uit of laatst in - eerst uit. 

### Ondernemingen waarvan de exploitatie een terrein aantast of vervuilt
De onderneming waarvan de exploitatie een terrein aantast of vervuilt (exploitatie van een stortplaats, steengroeve, kerncentrale, booreiland) zal over het algemeen later worden geconfronteerd met kosten die, enerzijds, betrekking hebben op de milieubescherming (aangelegenheid van algemeen belang) en, anderzijds, op de sanering van het terrein (aangelegenheid van particulier belang). 

De kosten die verbonden zijn aan de bescherming van het milieu zullen worden behandeld in een later advies. 

Wat de sanering van het terrein betreft en los van de overwegingen inzake milieubescherming, moet een onderscheid worden gemaakt tussen de activiteit op andermans terrein en de activiteit die op eigen terrein wordt verricht. 

Indien de activiteit op andermans terrein wordt verricht, houden de bepalingen van het contract of de concessie over het algemeen een verplichting in voor de exploitant om het terrein te saneren na afloop van de in het contract of de concessie vastgelegde periode. Die sanering zal later ook kosten met zich brengen. In dat geval moeten voorzieningen worden gevormd voor die kosten. 

Indien de activiteit op een eigen terrein wordt verricht, rijst de vraag of, los van de te vormen voorzieningen in verband met de verplichtingen inzake milieubescherming, waardeverminderingen moeten worden geboekt die verband houden met de minderwaarde die voor het terrein voortvloeit uit de exploitatie van de stortplaats dan wel of het aangewezen is voorzieningen te vormen voor de sanering van het terrein. 

Het antwoord op die vraag zal afhangen van feitelijke elementen. Indien de ontwaarding van het terrein ingevolg de exploitatie van de stortplaats de aanschaffingswaarde van het terrein niet kan overstijgen, is de eerste benadering verantwoord. Indien de exploitatie daarentegen het terrein een negatieve waarde kan bezorgen - wat ongetwijfeld vaak het geval zal zijn - zal enkel voor de tweede benadering kunnen worden 

geopteerd.

[^1]: Dit heeft geen betrekking op de produkten of het deel van de produkten waarvan de economische cyclus niet daadwerkelijk is voltooid aan het einde van de boekhoudperiode. Zo zal bijvoorbeeld, indien voor het vervoer van de afvalstoffen een andere overeenkomst werd gesloten of een andere vergoeding werd afgesproken dan voor hun aanschaffing, moet de vergoeding voor het vervoer als definitief verworven worden beschouwd zodra de afvalstoffen zijn vervoerd en zal zij niet kunnen worden overgedragen ten belope van het bedrag van de op die datum opgeslagen afvalstoffen.
