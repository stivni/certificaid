---
bron: https://www.cbn-cnc.be/nl/adviezen/verkoop-van-oplaadbare-betaalkaarten
datum: 2018-05-30
nummer: CBN-advies 2018/11
provenance:
  generated_at: '2026-05-11T13:05:08Z'
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/verkoop-van-oplaadbare-betaalkaarten
      sha256: f053794d73bf6c56003c22777a980d226e59c1ca1a3b1e51e0f0b1075766901f
      version:
  stale: false
  stale_reason:
  tooling:
    model:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    prompt_version:
  trust:
    confirmed_at: '2026-05-11T12:21:40Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      status: pass
      run_id: 20260511-130524
      run_at: '2026-05-11T13:05:29Z'
      heading_count: 6
      max_section_chars: 4094
      file_size_chars: 8098
      flags: []
    layer2:
      agent: subagent-sonnet-4-6
      concrete_problemen:
        - categorie: A3
          regel: 47
          type: other
          voorbeeld: 1. Algemeen \n2. Kleine\n vereniging of stichting \n3. Ondernemingen...
        - categorie: A3
          regel: 52
          type: other
          voorbeeld: ' vereniging of stichtingOndernemingen en niet-kleine verenigingen en stichtingen'
        - categorie: D4
          regel: 58
          type: other
          voorbeeld: '*vouchers voor enkelvoudig gebruik[^2] *'
        - categorie: D4
          regel: 65
          type: other
          voorbeeld: '*Genormaliseerd minimaal schema van de Staat van de ontvangsten en uitgaven[^5] *'
        - categorie: D4
          regel: 67
          type: other
          voorbeeld: '*Andere schulden *in het* Genormaliseerd minimaal schema van de staat van het vermogen*'
      rationale: 'D4: meerdere gevallen van malformed italic met spatie voor sluitende asterisk (categorie *term *) op regels 58, 65, 67. B3: de TOC-fragmenten op regels 47-52 bevatten een duplicate regel (''vereniging of stichtingOndernemingen en niet-kleine verenigingen en stichtingen'') zonder heading-prefix, wat een aaneengesmeten TOC-rest is. Verdere inhoud structureel intact.'
      run_at: '2026-05-11T12:21:40Z'
      status: needs-rework
    rationale: 'D4: meerdere gevallen van malformed italic met spatie voor sluitende asterisk (categorie *term *) op regels 58, 65, 67. B3: de TOC-fragmenten op regels 47-52 bevatten een duplicate regel (''vereniging of stichtingOndernemingen en niet-kleine verenigingen en stichtingen'') zonder heading-prefix, wat een aaneengesmeten TOC-rest is. Verdere inhoud structureel intact.'
    status: needs-rework
themas:
  - betaalkaart
  - oplaadbare betaalkaart
  - tegoedbon
  - tegoedkaart
  - cadeaubon
---

# CBN-advies 2018/11 – Verkoop van (oplaadbare) betaalkaarten

1. Algemeen 
2. Kleine
 vereniging of stichting 
3. Ondernemingen en niet-kleine verenigingen en stichtingen 

 vereniging of stichtingOndernemingen en niet-kleine verenigingen en stichtingen 

## Algemeen

In onderhavig advies verduidelijkt de Commissie de boekhoudkundige verwerking van de verkoop van betaalkaarten of de heroplading van dergelijke kaarten. Dergelijke kaarten kunnen al dan niet op naam zijn. Onderhavig advies verduidelijkt zowel de boekhoudkundige verwerking in hoofde van verenigingen en stichtingen als voor ondernemingen. 

De betaalkaarten bedoeld in onderhavig advies betreffen uitsluitend de tegoedkaarten of tegoedbonnen (cadeaubonnen) die worden uitgereikt of opgeladen als tegenprestatie voor de ontvangst van een som geld. Onderhavig advies gaat dus niet verder in op de boekhoudkundige verwerking van bijvoorbeeld tegoed- of kortingbonnen die worden uitgereikt naar aanleiding van een lancering van een nieuw product of ter promotie van de aankoop van producten. Onderhavig advies gaat evenmin nader in op de boekhoudkundige verwerking van uitgereikte *vouchers voor enkelvoudig gebruik[^2]* . 

## Kleine[^3] vereniging of stichting

De vereniging of stichting die een vereenvoudigde boekhouding voert zoals bedoeld in de artikelen 17, § 2, 37, § 2, of 53, § 2 van de wet van 27 juni 1921 betreffende de verenigingen zonder winstoogmerk, de stichtingen en de Europese politieke partijen en stichtingen (hierna: de vzw-wet) moet de mutaties in contanten of op rekeningen inschrijven in een ongesplitst dagboek volgens een genormaliseerd model[^4].

De sommen die door een kleine vereniging of stichting worden ontvangen om geplaatst te worden op een betaalkaart, worden aldus onmiddellijk ingeschreven onder de ontvangsten zonder de door de vereniging of stichting te leveren tegenprestatie af te wachten en maken deel uit van de totaliteit van de Ontvangsten op te nemen in het *Genormaliseerd minimaal schema van de Staat van de ontvangsten en uitgaven[^5]* .

In een heel aantal gevallen zijn de bedragen gestort op een betaalkaart terugbetaalbaar wanneer deze bedragen niet worden verbruikt. Wanneer in dergelijk geval de betaalkaart op inventarisdatum nog niet verbruikte sommen bevat, moeten deze sommen opgenomen worden onder de *Andere schulden* in het* Genormaliseerd minimaal schema van de staat van het vermogen* [^6] ,[^7]. 

## Ondernemingen en niet-kleine verenigingen en stichtingen

Ondernemingen en verenigingen en stichtingen die hun boekhouding voeren met inachtneming van de regels van het dubbel boekhouden registreren de bedragen die worden ontvangen om een betaalkaart op te laden onmiddellijk als een schuld. Wanneer deze betaalkaart vervolgens wordt gebruikt ter betaling van de aankoop van een goed of een geleverde dienst wordt deze schuldenrekening gedebiteerd en wordt een opbrengst geregistreerd.

| 

*Voorbeeld*

Een onderneming ontvangt van een klant 100 euro om deze op te laden op een betaalkaart. Vervolgens koopt deze klant een product ter waarde van 1,06 euro inclusief 6 procent btw.

## Boeking bij herlading van de betaalkaart

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 570 | Kassen-contanten | 100,00 | |
| aan | 489 | Diverse schulden | | 100,00 |

## Boeking bij verkoop en betaling product

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 489 | Diverse schulden | 1,06 | |
| aan | 451 | Te betalen btw | | 0,06 |
| | 70 | Omzet | 1,00 | |

 | 

Indien de betaalkaart niet terugbetaalbaar is en op de vervaldatum het opgeladen krediet niet volledig werd verbruikt, wordt het niet verbruikte gedeelte van de betaalkaart als opbrengst geboekt.

| 

*Voorbeeld*

Op de vervaldatum van (het saldo op) een uitgegeven betaalkaart komt een bedrag van 13,00 euro toe aan de onderneming zonder dat deze nog enige prestatie moet doen.

## Boeking op de vervaldatum

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 489 | Diverse schulden | 13,00 | |
| aan | 743 | Diverse bedrijfsopbrengsten | | 13,00 |

 | 

 De natuurlijke personen die koopman zijn, de vennootschappen onder firma en de gewone commanditaire vennootschappen mogen evenwel een vereenvoudigde boekhouding voeren als hun omzet exclusief btw over het laatste boekjaar het bedrag van 500.000 euro niet overschrijdt.[^9]
 Net zoals de kleine verenigingen en stichtingen kunnen zij zich er toe beperken om de ontvangsten en de uitgaven te registreren en jaarlijks een inventaris op te maken. In deze inventaris worden in voorkomend geval de op de betaalkaarten nog aanwezige terugbetaalbare tegoeden vermeld onder de schulden en/of verplichtingen.

[^1]: Onderhavig advies is tot stand gekomen nadat een ontwerpadvies op 10 april 2018 ter publieke consultatie werdgepubliceerd op de website van de CBN.

[^2]: Voucher voor enkelvoudig gebruik in de zin van artikel 30bis van Richtlijn 2006/112/EG van 28 november 2006 van de Raad betreffende het gemeenschappelijke stelsel van belasting over de toegevoegde waarde, ingevoegd door artikel 1 van Richtlijn (EU) 2016/1065 van de Raad van 27 juni 2016 tot wijziging van Richtlijn 2006/112/EFG wat de behandeling van vouchers betreft. Een voucher voor enkelvoudig gebruik wordt hierin gedefinieerd als een instrument ten aanzien waarvan de verplichting bestaat dat instrument als tegenprestatie of gedeeltelijke tegenprestatie voor goederenleveringen of diensten te aanvaarden en waarbij de te verrichten goederenleveringen of diensten, of de identiteit van de potentiële verrichters ervan, vermeld staan op het instrument zelf of in de bijbehorende documentatie, inclusief de voorwaarden voor het gebruik van het instrument waarbij de plaats van de goederenlevering of dienstverrichting waarop de voucher betrekking heeft, alsmede het bedrag van de over die goederen of diensten verschuldigde btw, bekend zijn op het tijdstip van uitgifte van de voucher.

[^3]: Hier worden bedoeld de verenigingen beoogd in artikel 17, § 2 van de wet van 27 juni 1921 betreffende de verenigingen zonder winstoogmerk, de stichtingen en de Europese politieke partijen en stichtingen (hierna: de vzw-wet, de stichtingen beoogd in artikel 37, § 2 vzw-Wet en de internationale verenigingen beoogd in artikel 53, § 2 vzw-wet (die zich niet vrijwillig hebben onderworpen aan de boekhoudkundige verplichtingen bedoeld in de respectievelijke artikelen 17, § 3, 37, § 3 en 53, § 3 van de vzw-wet).

[^4]: Bijlage A bij het KB van 26 juni 2003 (II) betreffende de vereenvoudigde boekhouding van bepaalde verenigingen zonder winstoogmerk, internationale verenigingen zonder winstoogmerk en stichtingen.

[^5]: Bijlage B bij het KB van 26 juni 2003 (II) betreffende de vereenvoudigde boekhouding van bepaalde verenigingen zonder winstoogmerk, internationale verenigingen zonder winstoogmerk en stichtingen.

[^6]: Artikel 14 KB van 26 juni 2003 (II) betreffende de vereenvoudigde boekhouding van bepaalde verenigingen zonder winstoogmerk, internationale verenigingen zonder winstoogmerk en stichtingen.

[^7]: Bijlage C, punt 4 bij het KB van 26 juni 2003 (II) betreffende de vereenvoudigde boekhouding van bepaalde verenigingen zonder winstoogmerk, internationale verenigingen zonder winstoogmerk en stichtingen.

[^8]: Indien er onvoldoende provisie aanwezig is op de kaart wordt een vordering geboekt.

[^9]: Artikel III.85 Wetboek van economisch recht in samenlezing met artikel 1 KB 12 september 1983 (I) tot uitvoering van de wet van 17 juli 1975 op de boekhouding van de ondernemingen. Het bedrag wordt op 620.000 euro gebracht voor de natuurlijke personen die koopman zijn, voor de vennootschappen onder firma en de gewone commanditaire vennootschappen die als voornaamste beroepsbezigheid gasvormige of vloeibare koolwaterstoffen, bestemd voor het voortbewegen van motorvoertuigen op de openbare weg, in het klein verkopen. Artikel III.95 Wetboek van economisch recht voorziet hierop evenwel een aantal uitzonderingen.
