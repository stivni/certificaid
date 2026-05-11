---
bron: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-onderzoeksfondsen-in-de-jaarrekening-van-grote-en-zeer
datum: 2011-07-20
gerelateerde_adviezen:
  - datum: '2019-04-12'
    titel: Gevolgen op gebied van financiële rapportering als gevolg van de brexit
    url: https://www.cbn-cnc.be/nl/adviezen/gevolgen-op-gebied-van-financiele-rapportering-als-gevolg-van-de-brexit-0
  - datum: '2016-09-07'
    titel: 'Bestellingen in uitvoering: wijzigingen door het koninklijk besluit van 18 december 2015'
    url: https://www.cbn-cnc.be/nl/adviezen/bestellingen-in-uitvoering-wijzigingen-door-het-koninklijk-besluit-van-18-december-2015
  - datum: '2015-09-30'
    titel: Boekhoudkundige verwerking van de aankoop van een onroerend goed bestemd voor verkoop
    url: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-de-aankoop-van-een-onroerend-goed-bestemd-voor-verkoop
  - datum: '2012-10-10'
    titel: Bestellingen in uitvoering
    url: https://www.cbn-cnc.be/nl/adviezen/bestellingen-in-uitvoering
nummer: CBN-advies 2011/17
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-onderzoeksfondsen-in-de-jaarrekening-van-grote-en-zeer
      sha256: b28435f5f77a0ad5b6b19eb05ff737fafd55d49bf2953afc6c1b8ffb6e617a0f
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-11T15:15:31Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T15:19:36Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "E2: tabel op regels 241-246 heeft rij-labels die buiten de tabelcellen lopen ('6620', 'en kosten', 'met terugnemingsrecht' elk als losse tabelrijen). Zelfde patroon op regels 262-267 ('168', 'met terugnemingsrecht', '6621', 'risico's en kosten (-)' buiten cellen). E2: regels 293-294 en 301-302 tonen 'Aanschaffingswaarde' als een losse tabelrij onder de eigenlijke rekening-rij in plaats van in dezelfde cel. Alle voetnoten [^1]-[^12] correct gedefinieerd."
    layer1:
      file_size_chars: 18931
      flags: []
      heading_count: 7
      max_section_chars: 5056
      run_at: '2026-05-11T15:05:50Z'
      run_id: 20260511-150547
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T15:19:36Z'
      rationale: "E2: tabel op regels 241-246 heeft rij-labels die buiten de tabelcellen lopen ('6620', 'en kosten', 'met terugnemingsrecht' elk als losse tabelrijen). Zelfde patroon op regels 262-267 ('168', 'met terugnemingsrecht', '6621', 'risico's en kosten (-)' buiten cellen). E2: regels 293-294 en 301-302 tonen 'Aanschaffingswaarde' als een losse tabelrij onder de eigenlijke rekening-rij in plaats van in dezelfde cel. Alle voetnoten [^1]-[^12] correct gedefinieerd."
      concrete_problemen:
        - regel: 243
          categorie: E2
          type: pseudo-table
          voorbeeld: "| | 6620 | Voorzieningen voor uitzonderlijke risico's | | |\n| | en kosten | 100.000 | | |"
        - regel: 264
          categorie: E2
          type: pseudo-table
          voorbeeld: "| | 168 | Voorzieningen voor schenkingen en legaten | | |\n| | met terugnemingsrecht | 100.000 | | |"
        - regel: 293
          categorie: E2
          type: pseudo-table
          voorbeeld: "| aan | 7170 | Wijziging in de bestellingen in uitvoering: | | 70.000 |\n| | Aanschaffingswaarde | | | |"
themas:
  - bestellingen in uitvoering
  - completed contract method
  - exploitatiesubsidie
  - onderzoekskost
  - onderzoeksfondsen
  - ontvangen vooruitbetalingen op bestellingen
  - over te dragen opbrengsten
  - percentage of completion method
---

# CBN-advies 2011/17 - Boekhoudkundige verwerking van “onderzoeksfondsen” in de jaarrekening van grote en zeer grote verenigingen en stichtingen

1. Onderzoeksfondsen zonder exclusief gebruiksrecht 
2. Onderzoeksfondsen met exclusief gebruiksrecht 

Verenigingen en stichtingen ontvangen geregeld “onderzoeksfondsen” met het oog op de uitvoering van welbepaalde onderzoeksactiviteiten. 

De boekhoudkundige verwerking van dergelijke onderzoeksfondsen is afhankelijk van de modaliteiten waaronder het onderzoeksfonds wordt toegekend[^1].

## Onderzoeksfondsen zonder exclusief gebruiksrecht

Een eerste mogelijkheid is dat de toekennende instantie[^2] middelen ter beschikking stelt met het oog op het voeren van een onderzoek waarvan de resultaten vrij verspreid mogen worden. 

De vereniging of stichting mag de gelden die zij ontvangt onmiddellijk in resultaat boeken als ‘exploitatiesubsidies’, maar dient in de toelichting wel te vermelden aan welke voorwaarden het behoud van deze subsidie gebonden is. 

Indien de onderzoeksfondsen in één keer worden uitbetaald, maar betrekking hebben op een onderzoek dat meerdere jaren in beslag zal nemen, dan dient een deel van de subsidies via de passiefrekening 493 *Over te dragen opbrengsten* overgedragen te worden naar de boekjaren waarop ze betrekking hebben.

## Voorbeeld 1

Op 1 april van het jaar x ontvangt een vereniging 300.000 euro voor de uitvoering van een onderzoek. De 300.000 euro dient te worden aangewend om de kosten van het onderzoek te dekken. De onderzoeksresultaten zullen verspreid worden via artikels in wetenschappelijke tijdschriften. Op het einde van het jaar x werden in het kader van het onderzoek reeds 225.000 euro kosten gemaakt waarvoor de eerder verkregen fondsen werden aangewend. Op 1 juni van het jaar x+1 wordt het onderzoek afgerond en worden de onderzoeksresultaten publiek gemaakt. 

- Boeking op 01/04/x: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 550 | Kredietinstellingen: rekening-courant | 300.000 | |
| aan | 737 | Exploitatiesubsidies | | 300.000 |

- Boeking op 31/12/x (de vereniging heeft in jaar x 225.000 euro kosten gemaakt in het kader van het onderzoek): 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 737 | Exploitatiesubsidies | 75.000 | |
| aan | 493 | Over te dragen opbrengsten | | 75.000 |

- Boeking op 01/01/x+1: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 493 | Over te dragen opbrengsten | 75.000 | |
| aan | 737 | Exploitatiesubsidies | | 75.000 |

## Voorbeeld 2

Op 1 april van het jaar x ontvangt een vereniging 350.000 euro voor de uitvoering van een onderzoek. De onderzoeksresultaten zullen verspreid worden via artikels in wetenschappelijke tijdschriften. Op het einde van het jaar x werden in het kader van het onderzoek reeds 225.000 euro kosten gemaakt waarvoor de eerder verkregen fondsen werden aangewend. De vereniging berekent dat het onderzoek haar in totaal 300.000 euro zal kosten en dat zij dus 50.000 euro positief resultaat zal behalen met het onderzoek. Aangezien het onderzoek op 31/12/x al voor 75 % afgerond is en de vereniging volgens haar berekeningen nog slechts 75.000 euro kosten zal moeten maken in het jaar x+1 om het onderzoek af te ronden, besluit zij om 37.500 euro (75 % van 50.000) van het geschatte positieve resultaat toe te rekenen aan het boekjaar x. Op 1 juni van het jaar x+1 wordt het onderzoek afgerond en worden de onderzoeksresultaten publiek gemaakt. 

- Boeking op 01/04/x: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 550 | Kredietinstellingen: rekening-courant | 350.000 | |
| aan | 737 | Exploitatiesubsidies | | 350.000 |

- Boeking op 31/12/x (de vereniging heeft in jaar x 225.000 euro kosten gemaakt in het kader van het onderzoek en rekent 37.500 van het geschatte positieve resultaat toe aan het boekjaar): 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 737 | Exploitatiesubsidies | 87.500 | |
| aan | 493 | Over te dragen opbrengsten | | 87.500 |

- Boeking op 01/01/x+1: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 493 | Over te dragen opbrengsten | 87.500 | |
| aan | 737 | Exploitatiesubsidie | | 87.500 |

## Voorbeeld 3

Een vereniging krijgt op 1 juli van het jaar x een onderzoeksfonds van 500.000 euro toegekend voor het voeren van een onderzoek, waarvan de resultaten vrij verspreid mogen worden. De vereniging dient hiervoor binnen een termijn van vijf jaar een bepaald aantal welomschreven proeven uit voeren. De 500.000 euro dient te worden aangewend om de kosten van het onderzoek te dekken. Indien de vereniging het onderzoek niet (volledig) uitvoert, zal zij de gelden (gedeeltelijk) moeten terugbetalen (naar rato van het percentage van het uitgevoerde onderzoek). Op het einde van het jaar x+4 vreest de vereniging dat zij slechts 80 % van de vooropgestelde proeven zal kunnen voltooien tegen 1 juli van het jaar x+5. Zij besluit om een voorziening aan te leggen ten belope van 100.000 euro (20 % van 500.000), aangezien zij naar schatting 20 % van het ontvangen onderzoeksfonds zal moeten terugbetalen. Op 1 juli van het jaar x+5 blijkt dat de vereniging effectief maar 80 % van de vooropgestelde proeven heeft kunnen afronden. Zij zal dus 100.000 euro van het ontvangen onderzoeksfonds dienen terug te storten. 

- Boeking op 01/07/x: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 550 | Kredietinstellingen: rekening-courant | 500.000 | |
| aan | 737 | Exploitatiesubsidies | | 500.000 |

- Boeking op 31/12/x (we veronderstellen dat de vereniging in jaar x 50.000 euro kosten heeft gemaakt in het kader van het onderzoek): 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 737 | Exploitatiesubsidies | 450.000 | |
| aan | 493 | Over te dragen opbrengsten | | 450.000 |

- Boeking op 01/01/x+1: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 493 | Over te dragen opbrengsten | 450.000 | |
| aan | 737 | Exploitatiesubsidies | | 450.000 |

- Boeking op 31/12/x+1 (we veronderstellen dat de vereniging in jaar x+1 100.000 euro kosten heeft gemaakt in het kader van het onderzoek): 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 737 | Exploitatiesubsidies | 350.000 | |
| aan | 493 | Over te dragen opbrengsten | | 350.000 |

- Boeking op 01/01/x+2: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 493 | Over te dragen opbrengsten | 350.000 | |
| aan | 737 | Exploitatiesubsidies | | 350.000 |

- Boeking op 31/12/x+2 (we veronderstellen dat de vereniging in jaar x+2 100.000 euro kosten heeft gemaakt in het kader van het onderzoek): 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 737 | Exploitatiesubsidies | 250.000 | |
| aan | 493 | Over te dragen opbrengsten | | 250.000 |

- Boeking op 01/01/x+3: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 493 | Over te dragen opbrengsten | 250.000 | |
| aan | 737 | Exploitatiesubsidies | | 250.000 |

- Boeking op 31/12/x+3 (we veronderstellen dat de vereniging in jaarx+3 100.000 euro kosten heeft gemaakt in het kader van het onderzoek): 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 737 | Exploitatiesubsidies | 150.000 | |
| aan | 493 | Over te dragen opbrengsten | | 150.000 |

- Boeking op 01/01/x+4: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 493 | Over te dragen opbrengsten | 150.000 | |
| aan | 737 | Exploitatiesubsidies | | 150.000 |

- Boekingen op 31/12/x+4: 
- Overdracht deel exploitatiesubsidies naar volgend boekjaar (we veronderstellen dat de vereniging in jaar x+4 100.000 euro kosten heeft gemaakt in het kader van het onderzoek): 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 737 | Exploitatiesubsidies | 50.000 | |
| aan | 493 | Over te dragen opbrengsten | | 50.000 |

- Aanleg voorziening: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 6620 | Voorzieningen voor uitzonderlijke risico’s | | |
| | en kosten | 100.000 | | |
| aan | 168 | Voorzieningen voor schenkingen en legaten | | 100.000 |
| | met terugnemingsrecht | | | |

- Boeking op 01/01/x+5:

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 493 | Over te dragen opbrengsten | 50.000 | |
| aan | 737 | Exploitatiesubsidies | | 50.000 |

- Boekingen op 01/07/x+5:

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 664 | Overige uitzonderlijke kosten | 100.000 | |
| aan | 489 | Andere diverse schulden | | 100.000 |

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 168 | Voorzieningen voor schenkingen en legaten | | |
| | met terugnemingsrecht | 100.000 | | |
| aan | 6621 | Bestedingen voorzieningen voor uitzonderlijke | | |
| | risico’s en kosten (-) | 100.000 | | |

## Onderzoeksfondsen met exclusief gebruiksrecht

Een tweede mogelijkheid is dat de toekennende instantie middelen ter beschikking stelt van de vereniging of stichting teneinde een specifiek onderzoek exclusief voor haar te laten verrichten. De opdrachtgever bekomt een exclusief recht op de onderzoeksbevindingen resulterend uit het verrichte onderzoek. Het gaat hier als het ware om een “bestelling in uitvoering”[^11]. De Commissie is van oordeel dat de toegekende middelen als *Ontvangen vooruitbetalingen op bestellingen* dienen geboekt te worden. Op het moment van de ‘oplevering’ van de resultaten van het onderzoek, zullen de ontvangen vooruitbetalingen afgeboekt worden en in resultaat worden genomen.

Bestellingen in uitvoering worden gewaardeerd tegen vervaardigingsprijs vermeerderd, naarmate de productie of de werkzaamheden vorderen, met het verschil tussen de in de overeenkomst bepaalde prijs en de vervaardigingsprijs wanneer dit verschil met voldoende zekerheid als verworven mag worden beschouwd (*percentage of completion method* of het toerekenen van de winst naar rato van de vooruitgang der werken). Een vereniging kan echter ook als regel aannemen bestellingen in uitvoering op de balans te boeken tegen hun vervaardigingsprijs zonder een pro rata toerekening van de theoretisch vooropgestelde winst (*completed contract method* of het toerekenen van de winst aan het boekjaar waarin de bestelling wordt opgeleverd). In de toelichting dienen onder de waarderingsregels de methoden en de criteria voor de waardering te worden vermeld (art. 7 KB 19 december 2003 *juncto* art. 71 KB W.Venn.)

Ten aanzien van de bestellingen in uitvoering worden waardeverminderingen toegepast indien hun vervaardigingsprijs, vermeerderd met het geraamde bedrag van de nog te maken kosten, hoger is dan het ontvangen onderzoeksfonds (*cf*. art. 72 KB W.Venn.). Waardeverminderingen mogen niet worden gehandhaafd in die mate, waarin ze op het einde van het boekjaar hoger zijn dan vereist is volgens de actuele beoordeling (art. 55 KB W.Venn.). Voor risico’s en kosten verbonden aan de verdere uitvoering van bestellingen in uitvoering worden voorzieningen gevormd, voorzover deze risico’s niet zijn gedekt door waardeverminderingen, geboekt met toepassing van artikel 72 KB W.Venn. (art. 71 KB W.Venn.).

## Voorbeeld 4: Completed contract-methode

Een farmaceutisch bedrijf stelt op 1 februari van het jaar x 150.000 euro te beschikking van een bepaalde vereniging teneinde deze vereniging onderzoek naar een bepaald geneesmiddel te laten verrichten. De onderzoeksresultaten worden exclusief eigendom van het farmaceutische bedrijf. De vereniging kiest als waarderingsmethode voor de completed contract-methode. Op 3 maart van het jaar x+2 rondt de vereniging het onderzoek af en maakt ze de resultaten over aan haar ‘sponsor’. 

- Boeking op 01/02/x: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 550 | Kredietinstellingen: rekening-courant | 150.000 | |
| aan | 46 | Ontvangen vooruitbetalingen op bestellingen | | 150.000 |

- Boeking op 31/12/x (we veronderstellen dat de vereniging reeds 70.000 euro kosten heeft gemaakt in het kader van het onderzoek): 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 370 | Bestellingen in uitvoering: aanschaffingswaarde | 70.000 | |
| aan | 7170 | Wijziging in de bestellingen in uitvoering: | | 70.000 |
| | Aanschaffingswaarde | | | |

- Boeking op 31/12/x+1 (we veronderstellen dat de vereniging in het jaar x+1 60.000 euro kosten heeft gemaakt in het kader van het onderzoek): 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 370 | Bestellingen in uitvoering: aanschaffingswaarde | 60.000 | |
| aan | 7170 | Wijziging in de bestellingen in uitvoering: | | 60.000 |
| | Aanschaffingswaarde | | | |

- Boeking op 03/03/x+2: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 46 | Ontvangen vooruitbetalingen op bestellingen | 150.000 | |
| aan | 700 | Verkopen en dienstprestaties | | 150.000 |

- Boeking op 31/12/x+2: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 7170 | Wijziging in de bestellingen in uitvoering: | 130.000 | |
| | Aanschaffingswaarde | | | |
| aan | 370 | Bestellingen in uitvoering: | | |
| | aanschaffingswaarde | 130.000 | | |

## Voorbeeld 5: Percentage of completion-methode

Een vereniging krijgt op 1 juli van het jaar x 150.000 euro van de stad G. met het oog op het uitvoeren van een mobiliteitstudie in de regio G. De vereniging dient hiervoor in hoofdzaak 2.000 enquêtes af te nemen en de resultaten van deze enquêtes te analyseren. De onderzoeksresultaten van deze studie dienen uiterlijk op 1 juli van het jaar x+1 aan de stad G. overgemaakt te worden. Indien het onderzoek niet tijdig wordt afgerond, zal de vereniging de som van 150.000 euro dienen terug te betalen. Op het einde van het jaar x werden in het kader van het onderzoek reeds 60.000 euro kosten gemaakt. De vereniging heeft op dat moment reeds de helft van het onderzoek afgerond en zij zal, volgens haar berekeningen, nog 60.000 euro kosten dienen te maken in het kader van het onderzoek. De vereniging zal dus normalerwijze een positief resultaat van 30.000 euro behalen met het onderzoek. De vereniging kiest als waarderingsmethode voor de percentage of completion-methode. In jaar x+1 kan de vereniging echter, wegens onvoorziene omstandigheden, het onderzoek toch niet afronden en dient zij de 150.000 euro terug te betalen. 

- Boeking op 01/07/x: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 550 | Kredietinstellingen: rekening-courant | 150.000 | |
| aan | 46 | Ontvangen vooruitbetalingen op bestellingen | | 150.000 |

- Boeking op 31/12/x (we veronderstellen dat de vereniging reeds 60.000 euro kosten heeft gemaakt in het kader van het onderzoek en de helft van het geschatte positieve resultaat toerekent aan het boekjaar[^12]): 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 370 | Bestellingen in uitvoering: aanschaffingswaarde | 60.000 | |
| | 371 | Bestellingen in uitvoering: toegerekende winst | 15.000 | |
| aan | 7170 | Wijziging in de bestellingen in uitvoering: | | 60.000 |
| | aanschaffingswaarde | | | |
| | 7171 | Wijziging in de bestellingen in uitvoering: | 15.000 | |
| | toegerekende winst | | | |

- Op 1 juli x+1 blijkt dat de vereniging de mobiliteitsstudie niet correct heeft uitgevoerd (er werden bijvoorbeeld maar 1.000 enquêtes afgenomen). De vereniging moet de gelden bijgevolg terugbetalen aan de stad G.: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 46 | Ontvangen vooruitbetalingen op bestellingen | 150.000 | |
| aan | 550 | Kredietinstellingen: rekening-courant | | 150.000 |

- Boeking op 31/12/x+1: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 7170 | Wijziging in de bestellingen in uitvoering: | 60.000 | |
| | aanschaffingswaarde | | | |
| | 7171 | Wijziging in de bestellingen in uitvoering: | 15.000 | |
| | toegerekende winst | | | |
| aan | 370 | Bestellingen in uitvoering: aanschaffingswaarde | | 60.000 |
| | 371 | Bestellingen in uitvoering: toegerekende winst | 15.000 | |

[^1]: De Commissie spreekt zich niet uit over de eventuele BTW-implicaties van de toekenning van onderzoeksfondsen. Indien de ontvangen gelden geïnvesteerd dienen te worden in vaste activa, dan dienen deze gelden als fondsen van de vereniging of als kapitaalsubsidies geboekt te worden (zie advies 2010/16 “Boekhoudkundige verwerking van subsidies, schenkingen en legaten, toegekend in contanten, in de jaarrekening van begunstigde grote en zeer grote verenigingen en stichtingen”, Bulletin CBN, nr. 56, december 2010, 17-30).

[^2]: Overheid, privépersoon, onderneming, andere vereniging of stichting, ...

[^3]: 300.000 – 225.000= 75.000.

[^4]: 350.000 – 225.000 – 37.500 = 87.500.

[^5]: 500.000 – 50.000 (kosten gemaakt in jaar x) = 450.000.

[^6]: 500.000 – 50.000 (kosten gemaakt in jaar x) – 100.000 (kosten gemaakt in jaar x+1) = 350.000.

[^7]: 500.000 – 50.000 (kosten gemaakt in jaar x) – 100.000 (kosten gemaakt in jaar x+1) – 100.000 (kosten gemaakt in jaar x+2) = 250.000.

[^8]: 500.000 – 50.000 (kosten gemaakt in jaar x) – 100.000 (kosten gemaakt in jaar x+1) – 100.000 (kosten gemaakt in jaar x+2) – 100.000 (kosten gemaakt in jaar x+3) = 150.000.

[^9]: 500.000 – 50.000 (kosten gemaakt in jaar x) – 100.000 (kosten gemaakt in jaar x+1) – 100.000 (kosten gemaakt in jaar x+2) – 100.000 (kosten gemaakt in jaar x+3) – 100.000 (kosten gemaakt in jaar x+4) = 50.000.

[^10]: De Commissie zal voorstellen om de benaming van rekening 168 aan te passen als volgt: “Voorzieningen voor terug te betalen subsidies en legaten en voor schenkingen met terugnemingsrecht”.

[^11]: Overeenkomstig artikel 9 KB 19 december 2003 juncto artikel 95, § 1, VI.B KB W.Venn. worden onder die post de “dienstprestaties die voor rekening van een derde op bestelling worden uitgevoerd en die nog niet werden geleverd, tenzij het gaat om een standaardtype van dienstprestaties” opgenomen.

[^12]: De winsttoerekening gebeurt a rato van de totaal verwachte kosten.
