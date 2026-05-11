---
bijgewerkt: 20.07.1970
bron: Afgesplitst uit Fisconet-compilatie (pdftotext_compilatie_btw)
bron_rol: itaa_lex
chunk:
  level: 3
  sub_strategy:
  type: Art.
itaa-lex-sectie: VI.B
provenance:
  generated_at: '2026-05-11T13:40:00Z'
  inputs:
    - id: resources/raw/wetteksten/btw-kbs/WBTW-KB-compilatie.pdf
      sha256: 5f1bad7278d1f8e1f5c00efb5d792f61342d3f7a14a7950caca2937924bfa91c
      version: 06.03.2020
  stale: false
  stale_reason:
  tooling:
    model:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    prompt_version:
  trust:
    confirmed_at: '2026-05-11T11:46:28Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      status: warn
      run_id: 20260511-134044
      run_at: '2026-05-11T13:40:47Z'
      heading_count: 9
      max_section_chars: 128566
      file_size_chars: 143226
      flags:
        - name: max_section_size
          status: warn
          detail: 'langste sectie op ###-niveau: 128566 chars (>24000); chunker splitst auto op alinea-grenzen via split_long_chunk'
          samples: []
    layer2:
      agent: subagent-sonnet-4-6
      concrete_problemen:
        - categorie: A1
          regel: 121
          type: form-feed
          voorbeeld: Tarieven                                       www.fisconetplus.be                             KB20   pg. I/1
        - categorie: A1
          regel: 348
          type: form-feed
          voorbeeld: T. A - Goederen 6 pct.                       www.fisconetplus.be                          KB20      pg. II/1
        - categorie: B4
          regel: 276
          type: other
          voorbeeld: BIJLAGE / Tabel A – Goederen en diensten onderworpen aan het tarief van 6 pct. als plain text
        - categorie: B4
          regel: 293
          type: other
          voorbeeld: 'I.     Levende dieren. (plain text rubriek zonder ##-prefix)'
        - categorie: B7
          regel: 100
          type: dotted-leader
          voorbeeld: '## AFDELING 5.       Slotbepalingen.                                                    Art. 22 - 24'
      rationale: 'A1: 30+ pagina-kopteksten (''Tarieven www.fisconetplus.be KB20 pg. I/1'' enz.) doorheen de body op vaste pagina-intervallen — nooit door een mens zo getypt. B4: tabel-rubrieken I t/m XL en Tabel A/B/C staan als plain text zonder ##-prefix; alleen ### Art. 1-artikelen en één ## Afdeling II zijn als headings gemarkeerd. B7: TOC-heading ''## AFDELING 5. Slotbepalingen. Art. 22 - 24'' eindigt op artikelbereik. Inhoud en volgorde zijn inhoudelijk compleet.'
      run_at: '2026-05-11T11:46:28Z'
      status: needs-rework
    rationale: 'A1: 30+ pagina-kopteksten (''Tarieven www.fisconetplus.be KB20 pg. I/1'' enz.) doorheen de body op vaste pagina-intervallen — nooit door een mens zo getypt. B4: tabel-rubrieken I t/m XL en Tabel A/B/C staan als plain text zonder ##-prefix; alleen ### Art. 1-artikelen en één ## Afdeling II zijn als headings gemarkeerd. B7: TOC-heading ''## AFDELING 5. Slotbepalingen. Art. 22 - 24'' eindigt op artikelbereik. Inhoud en volgorde zijn inhoudelijk compleet.'
    status: needs-rework
status: beschikbaar
tags:
  - VI.B
  - '2.4'
wet: K.B. nr. 20 van 20 juli 1970, tot vaststelling van de tarieven van de belasting over de toegevoegde waarde en tot indeling van de goederen en de diensten bij die tarieven
---

# K.B. nr. 20 van 20 juli 1970, tot vaststelling van de tarieven van de belasting over de toegevoegde waarde en tot indeling van de goederen en de diensten bij die tarieven

*Bijgewerkt tot en met 20.07.1970 — gecoördineerde versie.*

Koninklijk besluit nr. 20, van 20 juli 1970, tot vaststelling van de tarieven van
de belasting over de toegevoegde waarde en tot indeling van de goederen en
de diensten bij die tarieven.

(Uitvoering van artikel 37 van het Wetboek - Officieuze coördinatie)
Laatstelijk gewijzigd bij:
-   KB van 29.08.2019 - Koninklijk besluit tot aanpassing van sommige federale fiscale
    bepalingen aan het Wetboek van vennootschappen en verenigingen en aan het koninklijk
    besluit van 29 april 2019 tot uitvoering van het Wetboek van vennootschappen en
    verenigingen en houdende diverse bepalingen (B.S. 13.09.2019, pg. 86195).
    Dit KB wijzigt met ingang van 01.05.2019, Tabel A, rubriek XXXII van de bijlage.

### Art. 1

       (De tekst van KB nr. 20, artikel 1, werd aangevuld met de bepaling onder c), met
       ingang van 01.04.2019 (Art. 2, KB 13.04.2019, B.S. 26.04.2019, pg. 40552))

       Het normale tarief van de belasting over de toegevoegde waarde voor goederen en diensten bedoeld
in het Wetboek bedraagt 21 pct.
       In afwijking van het eerste lid wordt de belasting geheven tegen het verlaagd tarief van:
       a)     6 pct. voor de goederen en diensten opgenomen in tabel A van de bijlage bij dit besluit. Dit
              verlaagd tarief mag evenwel niet toegepast worden als de diensten bedoeld in tabel A
              bijkomstig deel uitmaken van een complexe overeenkomst die hoofdzakelijk andere diensten
              tot voorwerp heeft;
       b)     12 pct. voor de goederen en diensten opgenomen in tabel B van de bijlage bij dit besluit.
       c)     0 pct. voor de goederen en diensten opgenomen in tabel C van de bijlage bij dit besluit.

                                        Tijdelijke bepalingen

### Art. 1bis

       (De tekst van KB nr. 20, artikel 1bis, § 1 werd gewijzigd en § 3, werd ingevoegd met
       ingang van 01.09.2015 (Art. 1, KB 23.08.2015, B.S. 31.08.2015, pg. 55460, bekrachtigd
       bij art. 11, W 27.06.2016, B.S. 07.07.2016, pg. 42305))

§ 1.    In afwijking van artikel 1 wordt vanaf 1 april 2014 tot en met 31 augustus 2015 onderworpen aan
het verlaagd tarief van zes percent, de levering van elektriciteit aan huishoudelijke afnemers als bedoeld in
artikel 2, 16° bis, van de wet van 29 april 1999 betreffende de organisatie van de elektriciteitsmarkt.

§ 2.     Onverminderd het tweede lid is het toe te passen btw-tarief voor de voorschotten aangerekend tot
uiterlijk 31 maart 2014, het tarief dat van kracht is op het tijdstip van de facturering van deze voorschotten,
zelfs als deze geheel of gedeeltelijk betrekking hebben op de levering van elektriciteit vanaf 1 april 2014.
       Voor de definitieve heffing van de btw op de eindafrekening die betrekking heeft op de periode die
aanvangt vóór en eindigt na het tijdstip van de tariefwijziging op 1 april 2014, wordt de maatstaf van
heffing met betrekking tot het volledige verbruik tijdens die periode per onderscheiden btw-tarief
omgeslagen en dit rekening houdend met het verbruik vóór en na het tijdstip van de tariefwijziging.
      De berekening van het verbruik met het oog op de in het tweede lid bedoelde omslag per btw-tarief,
wordt uitgevoerd aan de hand van het in de elektriciteitsmarkt vastgelegde verbruiksprofiel (SLP of
synthetisch lastprofiel) dat per kwartier of per uur van een volledig jaar het relatieve gebruik weergeeft van
een bepaald type van klanten.

§ 3.     Onverminderd het tweede lid is het toe te passen btw-tarief voor de voorschotten aangerekend tot
uiterlijk 31 augustus 2015 en die geheel of gedeeltelijk betrekking hebben op de levering van elektriciteit
vanaf 1 september 2015, het tarief dat van kracht is op het tijdstip van de facturering van deze
voorschotten.
       Voor de definitieve heffing van de btw op de eindafrekening die betrekking heeft op de periode die
aanvangt voor en eindigt na het tijdstip van de tariefwijziging op 1 september 2015, wordt de maatstaf van
heffing met betrekking tot het volledige verbruik tijdens die periode per onderscheiden btw-tarief
omgeslagen en dit rekening houdend met het verbruik voor en na het tijdstip van de tariefwijziging.

      De berekening van het verbruik met het oog op de in het tweede lid bedoelde omslag per btw-tarief,
wordt uitgevoerd aan de hand van het in de elektriciteitsmarkt vastgelegde verbruiksprofiel (SLP of
synthetisch lastprofiel) dat per kwartier of per uur van een volledig jaar het relatieve gebruik weergeeft van
een bepaald type van klanten.

### Art. 1ter

       (De tekst van KB nr. 20, artikel 1ter, werd opgeheven met ingang van 01.07.2011
       (Art. 26, W 04.07.2011, B.S. 19.07.2011))

### Art. 1quater

       (KB nr. 20, artikel 1quater, werd gewijzigd met ingang van 01.01.2010 (Art. 1,
       KB 09.12.2009,   B.S. 14.12.2009, bekrachtigd  bij   art.  14,  W   19.05.2010,
       B.S. 28.05.2010))

       Vanaf 1 januari 2009 tot en met 31 december 2010 is het voordeel van het verlaagd tarief van zes
percent voor het werk in onroerende staat en de andere handelingen opgesomd in rubriek XXXI, § 3, 3° tot
6°, van tabel A van de bijlage bij dit besluit, die tot voorwerp hebben de afbraak en de daarmee gepaard
gaande heropbouw van een woning, onderworpen aan de in rubriek XXXVII van dezelfde tabel A opgenomen
voorwaarden, met uitzondering van de bepaling onder 2°, en voor zover de aanvraag voor de
stedenbouwkundige vergunning met betrekking tot bedoelde werken wordt ingediend bij de bevoegde
overheid vóór 1 april 2010.

### Art. 1quinquies

       (De tekst van KB nr. 20, artikel 1quinquies, § 1, tweede lid, 2°, werd opgeheven met
       ingang van 17.06.2010 (Art. 2, KB 02.06.2010, B.S. 07.06.2010))

§ 1.   In afwijking van artikel 1 worden vanaf 1 januari 2009 tot en met 31 december 2010 onderworpen
aan het tarief van zes percent over een totale gecumuleerde maatstaf van heffing van 50.000 euro,
exclusief btw, het werk in onroerende staat en andere handelingen opgesomd in rubriek XXXI, § 3, 3° tot
6°, van tabel A van de bijlage bij dit besluit, die de oprichting tot voorwerp hebben van een woning die na
uitvoering van de werken hetzij uitsluitend, hetzij hoofdzakelijk, wordt gebruikt als vaste privé-woning van
de bouwheer die er zonder uitstel zijn domicilie zal hebben.
       Het voordeel van het verlaagd tarief is onderworpen aan het vervullen van volgende voorwaarden:
       1°     het tijdstip waarop de belasting opeisbaar wordt overeenkomstig artikel 22 van het Wetboek,
              moet zich voordoen vóór de eerste ingebruikneming van het gebouw en uiterlijk op 31
              december 2010;
       2°     [opgeheven];
       3°     de bouwheer of zijn vertegenwoordiger moet:
              a)     vooraleer de belasting opeisbaar wordt overeenkomstig artikel 22 van het Wetboek, bij
                     een dienst van de administratie die de belasting over de toegevoegde waarde onder
                     haar bevoegheid heeft, verklaren in de vorm bepaald door of vanwege de Minister van
                     Financiën, dat het gebouw dat hij laat oprichten bestemd is om, hetzij uitsluitend,
                     hetzij hoofdzakelijk, te worden gebruikt als vaste privé-woning van de bouwheer die er
                     zijn domicilie zal hebben;
              b)     aan de dienstverrichter een kopie van de verklaring bedoeld onder a) overhandigen;
       4°     de dienstverrichter moet:
              a)     op de factuur die hij uitreikt en op het dubbel dat hij bewaart, de datum en het
                     referentienummer vermelden van de verklaring bedoeld in de bepaling onder 3°, a),
                     alsmede het controlekantoor van de belasting over de toegevoegde waarde waar de
                     verklaring werd ingediend;
              b)     uiterlijk de laatste werkdag van de maand na die waarin de factuur met toepassing van
                     het tarief van zes percent werd uitgereikt, een kopie van deze factuur toesturen aan
                     het controlekantoor van de belasting over de toegevoegde waarde waaronder hij
                     ressorteert;
       5°     voor zover de voorwaarden bedoeld in de bepaling onder 4° vervuld zijn en behalve in geval
              van samenspannen tussen partijen of klaarblijkelijk niet naleven van onderhavige bepaling,
              ontlast de verklaring van de afnemer de dienstverrichter van de aansprakelijkheid betreffende
              de vaststelling van het tarief.

       6°     de aanvraag voor de stedenbouwkundige vergunning met betrekking tot bedoelde werken
              moet worden ingediend bij de bevoegde overheid vóór 1 april 2010.

§ 2.    In afwijking van artikel 1 worden vanaf 1 januari 2009 tot en met 31 december 2010 onderworpen
aan het tarief van zes percent over een totale gecumuleerde maatstaf van heffing van 50.000 euro,
exclusief btw, de leveringen van gebouwen en de vestigingen, overdrachten en wederoverdrachten van
zakelijke rechten op gebouwen die niet vrijgesteld zijn door artikel 44, § 3, 1°, van het Wetboek, wanneer
die gebouwen hetzij uitsluitend, hetzij hoofdzakelijk, gebruikt worden als vaste privé-woning van de
verkrijger die er zonder uitstel zijn domicilie zal hebben en die vóór 1 januari 2009 nog niet in gebruik zijn
genomen.
      Het voordeel van het verlaagd tarief is onderworpen aan het vervullen van de volgende
voorwaarden:
       1°     degene die het gebouw levert of een zakelijk recht op het gebouw vestigt, overdraagt of
              wederoverdraagt in omstandigheden waarbij de belasting opeisbaar wordt, moet:
              a)     vooraleer de belasting opeisbaar wordt overeenkomstig artikel 17 van het Wetboek, bij
                     het controlekantoor van de belasting over de toegevoegde waarde van het
                     ambtsgebied waarin hij zijn woonplaats of maatschappelijke zetel heeft, verklaren in de
                     vorm bepaald door of vanwege de Minister van Financiën, dat het gebouw dat hij
                     overdraagt of waarop hij een zakelijk recht vestigt, overdraagt of wederoverdraagt,
                     hetzij uitsluitend, hetzij hoofdzakelijk, bestemd is om te worden gebruikt als vaste
                     privé-woning van de verkrijger die er zijn domicilie zal hebben;
              b)     deze verklaring moet bovendien aangevuld en mede ondertekend worden door de
                     verkrijger van het gebouw of van het zakelijk recht op het gebouw;
       2°     de door de vervreemder uitgereikte factuur en het dubbel dat hij moet bewaren moeten
              melding maken dat het gebouw hetzij uitsluitend, hetzij hoofdzakelijk, gebruikt wordt als
              vaste privé-woning van de verkrijger die er zijn domicilie zal hebben;
       3°     uiterlijk de laatste werkdag van de maand na die waarin de factuur met toepassing van het
              tarief van zes percent werd uitgereikt, moet de vervreemder een kopie van deze factuur
              toesturen aan het controlekantoor van de belasting over de toegevoegde waarde waaronder
              hij ressorteert.
       4°     de aanvraag voor de stedenbouwkundige vergunning met betrekking tot bedoelde werken
              moet worden ingediend bij de bevoegde overheid vóór 1 april 2010.

§ 3.  De voorwaarden bedoeld onder § 1, eerste lid, en § 2, eerste lid, moeten vervuld blijven gedurende
een periode die eindigt op:
       1°     wat de oprichting van een woning betreft, 31 december van het vijfde jaar volgend op het
              jaar van de eerste ingebruikneming van het gebouw;
       2°     wat de levering van een gebouw en de vestiging, overdracht en wederoverdracht van
              zakelijke rechten op een gebouw die niet vrijgesteld zijn door artikel 44, § 3, 1°, van het
              Wetboek betreft, 31 december van het vijfde jaar volgend op het jaar van de eerste
              ingebruikneming van het gebouw door de verkrijger.
      Indien de bouwheer of verkrijger tijdens de hierboven genoemde periode wijzigingen aanbrengt
waardoor de voorwaarden bedoeld onder § 1, eerste lid en § 2, eerste lid, niet meer vervuld zijn, moet hij:
       1°     hiervan aangifte doen op het controlekantoor van de belasting over de toegevoegde waarde
              van het ambtsgebied waarin het gebouw is gelegen binnen de termijn van een maand vanaf
              de datum waarop de wijzigingen aangevangen worden;
       2°     het belastingvoordeel dat hij heeft genoten terugstorten aan de Staat.

§ 4.   Het verlaagd tarief van zes percent is in geen geval van toepassing op:
       1°     werk in onroerende staat en andere onroerende handelingen die geen betrekking hebben op
              de eigenlijke woning, zoals bebouwingswerkzaamheden, tuinaanleg en het oprichten van
              afsluitingen;
       2°     werk in onroerende staat en andere onroerende handelingen die tot voorwerp hebben de
              bestanddelen of een gedeelte van de bestanddelen van zwembaden, sauna’s, midget-
              golfbanen, tennisterreinen en dergelijke installaties;
       3°     werk in onroerende staat en andere onroerende handelingen opgesomd in rubriek XXXI, § 3,
              3° tot 6°, van tabel A van de bijlage bij dit besluit, die betrekking hebben op een gebouw dat
              reeds het voorwerp heeft uitgemaakt van een onder paragraaf 2 bedoelde handeling met
              toepassing van het verlaagd tarief van zes percent.

### Art. 1sexies

       (KB nr. 20, artikel 1sexies, werd gewijzigd met ingang van 01.01.2010 (Art. 3,
       KB 09.12.2009, B.S. 14.12.2009, bekrachtigd bij art. 14, W 19.05.2010, B.S.
       28.05.2010))

        In afwijking van artikel 1, tweede lid, b) worden vanaf 1 januari 2009 tot en met 31 december 2010
onderworpen aan het tarief van zes percent de handelingen bedoeld in tabel B, rubriek X, § 1, van de
bijlage bij dit besluit voor zover de aanvraag voor de stedenbouwkundige vergunning met betrekking tot
bedoelde werken wordt ingediend bij de bevoegde overheid vóór 1 april 2010. De uitsluitingen opgenomen
in rubriek X, § 2, van dezelfde tabel B blijven van toepassing.

### Art. 2

       (De tekst van KB nr. 20, artikel 2, is van toepassing met ingang van 01.01.1971
       (Art. 98, W 03.07.1967))

      Dit besluit treedt in werking op dezelfde datum als de wet van 3 juli 1969 tot invoering van het
Wetboek van de belasting over de toegevoegde waarde.

### Art. 3

       (De tekst van KB nr. 20, artikel 3, is van toepassing met ingang van 01.01.1971
       (Art. 98, W 03.07.1967))

       Onze Minister van Financiën is belast met de uitvoering van dit besluit.

                                                          BIJLAGE

Tabel A – Goederen en diensten onderworpen aan het tarief van 6 pct.
             Goederen aan 6 pct. .........................................................................................    II/1
             Diensten aan 6 pct. ..........................................................................................   III/1

Tabel B – Goederen en diensten onderworpen aan het tarief van 12 pct. ...................................                     IV/1

Tabel C – Goederen en diensten onderworpen aan het tarief van 0 pct. .....................................                    V/1

                                               TABEL A
            Goederen en diensten onderworpen aan het tarief van 6 pct.

                                             GOEDEREN

I.     Levende dieren.

       (De tekst van KB nr. 20, TABEL A, I, 1°, is van toepassing met ingang van 01.07.2003.
       (Art. 1 t/m 7, KB 11.07.2003, B.S. 24.07.2003))

       1°    Runderen, varkens, schapen, geiten, ezels, muildieren en muilezels; paarden van de rassen
             die gewoonlijk als trekpaard, zwaar of halfzwaar, worden gebruikt; herten; paarden verkocht,
             intracommunautair verworven of ingevoerd om te worden geslacht.
       2°    Pluimvee; tamme duiven; tamme konijnen.

II.    Vlees en slachtafvallen.

       1°    Vlees en eetbare slachtafvallen van alle soorten, ook indien bereid of verduurzaamd.
       2°    Darmen, blazen en magen van dieren, in hun geheel of in stukken.

III.   Vis, schaal-, schelp- en weekdieren.

       (De tekst van KB nr. 20, TABEL A, III, is van toepassing met ingang van 01.07.2003.
       (Art. 1 t/m 7, KB 11.07.2003, B.S. 24.07.2003))

       Vis, schaal-, schelp- en weekdieren voor menselijke consumptie, ook indien bereid of verduurzaamd,
       met uitzondering van:
       a)    kaviaar en kaviaarsurrogaten;
       b)    langoesten, zeekreeften, krabben, rivierkreeften en oesters, vers (zowel levend als dood),
             gekookt in water, gekoeld, bevroren, gedroogd, gezouten, gepekeld, ook indien zij ontdaan
             zijn van de schaal of de schelp;
       c)    bereidingen en gebruiksklare gerechten van langoesten, zeekreeften, krabben, rivierkreeften
             en oesters, in de schaal of de schelp, al dan niet in gehele staat.

IV.    Melk en zuivelprodukten; eieren; honig.

       1°    Melk en zuivelprodukten (yoghurt, room, boter, kaas, wrongel melkdranken, enz.).
       2°    Vogeleieren en eigeel.
       3°    Natuurhonig.

V.     Groenten, planten, wortels en knollen, voor voedingsdoeleinden.

       Groenten, planten, wortels en knollen, voor voedingsdoeleinden, ook indien bereid of verduurzaamd,
       en plantgoed daarvan.

VI.    Fruit; schillen van citrusvruchten en van meloenen.

       1°    Fruit, ook indien bereid of verduurzaamd.
       2°    Schillen van citrusvruchten en van meloenen, ook indien bereid of verduurzaamd.

VII.   Plantaardige produkten.

       (De tekst van KB nr. 20, TABEL A, VII, bepalingen 13. en 14., werd vervangen met
       ingang van 01.04.2019 (Art. 2, W 27.02.2019, B.S. 14.03.2019, pg.26797))

       1°    Granen.
       2°    Oliehoudende zaden en vruchten, ook indien gebroken.
       3°    Zaaigoed, sporen daaronder begrepen.
       4°    Suikerbieten, ook indien gesneden; suikerriet.

      5°    Cichoreiwortels.
      6°    Hop.
      7°    Planten, plantedelen, zaden en vruchten, hoofdzakelijk gebruikt in de reukwerkindustrie, in de
            geneeskunde of voor insekten- of parasietenbestrijding of voor dergelijke doeleinden.
      8°    Sint-Jansbrood; vruchtepitten    en   plantaardige     produkten,   hoofdzakelijk    gebruikt voor
            menselijke voeding.
      9°    Stro en kaf van graangewassen, onbewerkt, ook indien gehakt.
      10°   Voederbieten en andere voederwortels; hooi, klaver, voederkool en andere dergelijke
            voedergewassen.
      11°   Teen.
      12°   Hout op stam; hout, onbewerkt, ook indien ontschorst of ruw behakt of ontdaan van het
            spint; brandhout; houtafval.
      13°   Levende woudbomen, levende fruitbomen, -heesters en -struiken, alsmede plantgoed
            daarvan, ook wanneer deze goederen bij de aanleg en het onderhoud van tuinen worden
            geleverd.
      14°   Levende sierbomen, -heesters, -struiken en andere levende sierplanten; bollen, knollen,
            wortels en ander plantgoed voor de sierteelt, ook wanneer deze goederen bij de aanleg en het
            onderhoud van tuinen worden geleverd; verse snijbloemen en vers snijgroen
      15°   Vlas.
      Van deze rubriek zijn uitgezonderd de goederen te koop aangeboden als voedsel voor honden,
      katten, kooivogels zoals papegaaien en zangvogels, voor aquariumvissen, voor hamsters, guinese
      biggetjes en andere troeteldiertjes.

VIII. Produkten van de meelindustrie; mout; zetmeel.

      1°    Meel, grutten, gries, griesmeel en vlokken, van granen, van zaden van peulgroenten, van
            vruchten, van aardappelen of van andere wortels en knollen; gort en parelgort en andere
            gepelde, geparelde, gebroken of geplette granen; graankiemen, ook indien gemalen.
      2°    Mout, ook indien gebrand.
      3°    Zetmeel, met uitzondering van oplosbare, gerooste of tot lijm verwerkte produkten, alsmede
            van produkten die verwerkt zijn tot of opgemaakt zijn als parfumerie of toiletartikel en van
            preparaten voor het appreteren.
      Van deze rubriek zijn uitgezonderd de goederen te koop aangeboden als voedsel voor honden,
      katten, kooivogels zoals papegaaien en zangvogels, voor aquariumvissen, voor hamsters, guinese
      biggetjes en andere troeteldiertjes.

IX.   Vetten en oliën.

      1°    Dierlijke vetten en oliën, ruw, gesmolten, geperst of geraffineerd.
      2°    Plantaardige vette oliën, ruw, gezuiverd of geraffineerd.
      3°    Dierlijke en plantaardige oliën en vetten, gehydrogeneerd, gehard of in vaste toestand
            gebracht, ook indien gezuiverd, doch niet verder bereid.
      4°    Bereide spijsvetten met uitzondering van margarine.

X.    Andere voedingsmiddelen.

      (De tekst van KB nr. 20, TABEL A, X, tweede lid, is van toepassing met ingang van
      01.04.2004. (Art. 371, W 22.12.2003, B.S. 31.12.2003))

      1°    Koffie, cafeïnevrije koffie daaronder begrepen, ook indien gebrand; thee; maté; specerijen.
      2°    Pectine en vloeibare of poedervormige stoffen op basis van pectine, bestemd voor de
            vervaardiging van jam en gelei.
      3°    Vleesextracten en vleessappen.
      4°    Suiker, stroop en melasse, ook indien gecarameliseerd, gearomatiseerd of met toegevoegde
            kleurstoffen; suikerwerk; kunsthonig.
      5°    Cacaobonen, cacaomassa (cacaopasta), cacaopoeder, cacaoboter; chocolade en andere
            voedingsmiddelen, welke cacao bevatten.
      6°    Moutextract; preparaten voor kindervoeding, voor dieetvoeding of voor keukengebruik;
            deegwaren; tapioca; graanpreparaten vervaardigd door poffen of door roosteren;
            bakkerswaren, gebak en biscuits; hosties, ouwels voor geneesmiddelen en dergelijke
            produkten.

       7°    Jam, gelei, marmelade, vruchtenmoes en vruchtenpasta.
       8°    Gebrande cichorei, andere gebrande koffiesurrogaten, en extracten daarvan.
       9°    Extracten en essences, van koffie, van thee of van maté; preparaten van deze extracten en
             essences.
       10°   Mosterdmeel en bereide mosterd.
       11°   Sausen; samengestelde kruiderijen en dergelijke produkten.
       12°   Preparaten voor soepen of voor bouillons; gebruiksklare soepen en bouillons.
       13°   Natuurlijke gist, ook indien inactief; samengestelde bakpoeders; cultures van micro-
             organismen voor de vervaardiging van voedingsmiddelen.
       14°   Tafelazijn (natuurlijke en kunstmatige).
       15°   Zout bestemd voor menselijke consumptie.
       16°   Gelatine voor de voeding, in dunne vellen.
       17°   Produkten voor menselijke consumptie niet hierboven genoemd.
       Van deze rubriek zijn uitgezonderd de bieren met een effectief alcoholvolumegehalte van meer dan
       0,5 % vol. en andere dranken met een effectief alcoholvolumegehalte van meer dan 1,2 % vol.

XI.    (Opgeheven bij KB 11.08.1972)

XII.   Voedsel voor dieren; meststoffen; dierlijke produkten.

       1°    Gedroogd bloed.
       2°    Meel en poeder van vlees, van slachtafvallen, van vis of van schaal-, schelp- of weekdieren;
             kanen.
       3°    Zemelen, slijpsel en andere resten van het zeven, van het malen of van andere bewerkingen
             van granen of van peulgroenten.
       4°    Bietenpulp, uitgeperst suikerriet (ampas) en andere afvallen van de suikerindustrie; bostel
             (brouwerijafval); afvallen van branderijen; afvallen van zetmeelfabrieken en dergelijke
             afvallen.
       5°    Perskoeken, ook die van olijven, en andere bij de winning van plantaardige oliën verkregen
             afvallen, met uitzondering van droesem of bezinksel.
       6°    Plantaardige produkten van de soorten welke worden gebruikt als voedsel voor dieren
             (droesem van appelen en van ander fruit, enz.))
       7°    Veevoeder, samengesteld met melasse of met suiker, en ander bereid voedsel voor dieren;
             andere bereidingen gebezigd voor het voederen van dieren (veevoedersupplementen, enz.).
       8°    Meststoffen
       9°    Dierlijke produkten gebruikt voor de voortplanting.
       10°   Wol, niet gekaard en niet gekamd.
       Van deze rubriek zijn uitgezonderd de goederen te koop aangeboden als voedsel voor honden,
       katten, kooivogels zoals papegaaien en zangvogels, voor aquariumvissen, voor hamsters, guinese
       biggetjes en andere troeteldiertjes.

XIII. Waterdistributie

       Gewoon natuurlijk water geleverd door middel van waterdistributie.

XIV.   (Opgeheven bij KB 17.03.1992)

XV.    (opgeheven bij KB 29.12.1992)

XVI.   (Opgeheven bij KB 17.03.1992)

XVII. Geneesmiddelen en medische hulpmiddelen

       (De tekst van KB nr. 20, TABEL A, XVII, 1, 2, 3 en 5, is van toepassing met ingang
       van 01.07.2003 (Art. 1 t/m 7, KB 11.07.2003, B.S. 24.07.2003))

       1.    a)     Elke enkelvoudige of samengestelde substantie bedoeld in artikel 1 van de wet van 25
                    maart 1964 op de geneesmiddelen en geregistreerd als geneesmiddel door de Minister
                    die de Volksgezondheid onder zijn bevoegdheid heeft of waarvoor de vergunning voor
                    het in de handel brengen bedoeld in artikel 1, § 1, eerste lid, 1) van het koninklijk

                      besluit van 3 juli 1969 betreffende de registratie van geneesmiddelen ter kennis is
                      gegeven aan de Minister die de Volksgezondheid onder zijn bevoegdheid heeft.
              b)      Bloed, bloedplaatjes, plasma en witte en rode bloedlichaampjes bestemd om te worden
                      toegediend aan mens of dier voor therapeutisch of profylactisch gebruik en die niet
                      bedoeld zijn in punt a) hiervoor.
              c)      Geneesmiddelen voor menselijk en diergeneeskundig gebruik die door de apotheker in
                      zijn officina worden bereid en verkocht.
       2°     (...)
       3°     Watten, gaas, verband en dergelijke artikelen (zwachtels, pleisters, enz.), die een
              geneesmiddel met een bijkomende activiteit ten opzichte van het hulpmiddel bevatten of
              opgemaakt voor de verkoop in het klein voor geneeskundige of voor chirurgische doeleinden;
              tassen, dozen, trommels en dergelijke, gevuld met artikelen voor eerste hulp bij ongelukken.
       4°     Condomen.
       5°     Steriele hypodermatische wegwerpspuiten bestemd voor de inspuiting van insuline, waarop de
              daartoe nodige schaalverdeling in internationale insuline-eenheden is aangebracht; steriele
              wegwerpnaalden voor insuline-pennen.
       6°     Bloedafnamezakken die anticoagulantia bevatten.
       7°     Botcement dat antibiotica met een bijkomende activiteit ten opzichte van het hulpmiddel
              bevat.
       8°     Steriele visco-elastische substanties uitsluitend bestemd voor humane of veterinaire medische
              of chirurgische doeleinden.

XVIII. (Opgeheven bij KB 17.03.1992)

XIX.   Kranten, tijdschriften en boeken

       (De tekst van KB 20, Tabel A, rubriek XIX, werd vervangen met ingang van 01.04.2019
       (Art. 3, W 13.04.2019, B.S. 26.04.2019, pg. 40552))

       Het verlaagd tarief is van toepassing op:
       1°     boeken, brochures, folders en dergelijke publicaties, met inbegrip van atlassen;
       2°     kranten en tijdschriften, ook indien geïllustreerd, waarop het verlaagd tarief van 0 pct.
              bedoeld in Tabel C, rubriek I, niet van toepassing is;
       3°     prentenalbums, prentenboeken, tekenboeken en kleurboeken voor kinderen;
       4°     muziekpartituren, ook indien geïllustreerd.
       Het verlaagd tarief is van toepassing op de publicaties bedoeld in het eerste lid, ongeacht de manier
             waarop ze aan de lezer ter beschikking worden gesteld, met name:
       1°     op papier of karton, dan wel op enige andere fysieke drager;
       2°     langs elektronische weg.
       Van deze rubriek zijn uitgesloten, de publicaties die:
       1°     uitsluitend of hoofdzakelijk bestaan uit reclamemateriaal;
       2°     uitsluitend of hoofzakelijk bestaan uit video-inhoud of beluisterbare muziek.

XX.    (opgeheven bij KB 29.12.1992)

XXI.   Kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten.

       (De tekst van KB nr. 20, TABEL A, XXI, is van toepassing met ingang van 01.11.1995
       (Art. 2, A t/m C, KB 20.10.1995))

       § 1.  Het verlaagd tarief, is van toepassing op de invoer van de in § 2 hieronder omschreven
       kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten.
       Het verlaagd tarief is eveneens van toepassing:
       1°     op de leveringen van in § 2, 1°, hieronder omschreven kunstvoorwerpen:
              a)      die door de maker of diens rechthebbenden worden verricht;
              b)      die incidentieel worden verricht door een andere belastingplichtige dan een
                      belastingplichtige   wederverkoper     wanneer   die   kunstvoorwerpen   door  die
                      belastingplichtige zelf zijn ingevoerd of hem zijn geleverd door de maker of diens
                      rechthebbenden of wanneer ze te zijnen gunste het recht op volledige aftrek van de
                      belasting over de toegevoegde waarde hebben doen ontstaan;

     2°     op de intracommunautaire verwervingen van in § 2, 1°, hieronder omschreven
            kunstvoorwerpen wanneer de verkoper in de Lid-Staat van vertrek van de verzending of het
            vervoer van de verworven goederen:
            a)     de maker is of een rechthebbende van de maker;
            b)     of een andere belastingplichtige is dan een belastingplichtige wederverkoper, die
                   incidenteel handelt, wanneer die kunstvoorwerpen door die belastingplichtige zelf zijn
                   ingevoerd of hem zijn geleverd door de maker of diens rechthebbenden of wanneer ze
                   te zijnen gunste het recht op volledige aftrek van de belasting over de toegevoegde
                   waarde hebben doen ontstaan.

     § 2.   Voor de toepassing van onderhavige rubriek worden aangemerkt als:
     1°     "kunstvoorwerpen":
            a)     schilderijen, collages en dergelijke decoratieve platen, schilderijen en tekeningen
                   geheel van de hand van de kunstenaar, met uitzondering van:
                   -      bouwtekeningen en andere tekeningen              voor   industriële,   commerciële,
                          topografische en dergelijke doeleinden;
                   -      met de hand versierde voorwerpen;
                   -      beschilderd doek voor theatercoulissen, voor achtergronden van studio's of voor
                          dergelijk gebruik;
            b)     originele gravures, originele etsen én originele litho's;
            c)     originele standbeelden en origineel beeldhouwwerk geheel van de hand van de
                   kunstenaar, ongeacht het materiaal waarvan zij vervaardigd zijn; afgietsels van
                   beeldhouwwerken in een oplage van maximaal acht exemplaren die door de
                   kunstenaar of diens rechthebbenden wordt gecontroleerd;
            d)     tapisserieën en wandtextiel, met de hand vervaardigd volgens originele ontwerpen van
                   kunstenaars, mits er niet meer dan acht exemplaren van elk bestaan;
            e)     unieke voorwerpen van keramiek, geheel van de hand van de kunstenaar en door hem
                   gesigneerd, met uitzondering van gebruiksvoorwerpen;
            f)     emailwerk op koper, geheel met de hand vervaardigd tot maximaal acht genummerde
                   en door de kunstenaar of het atelier gesigneerde exemplaren, met uitsluiting van
                   sieraden, juwelen, edelsmidswerk en gebruiksvoorwerpen;
            g)     foto's die genomen zijn door de kunstenaar, door hem of onder zijn toezicht zijn
                   afgedrukt, gesigneerd en genummerd, met een oplage van maximaal dertig
                   exemplaren voor alle formaten en dragers samen;
     2°     "voorwerpen voor verzamelingen":
            a)     postzegels,      fiscale    zegels,    gefrankeerde enveloppen   en     postkaarten,
                   eerstedagenveloppen en dergelijke, gestempeld of, indien ongestempeld, voor zover zij
                   niet geldig zijn of niet geldig zullen worden;
            b)     verzamelingen en voorwerpen voor verzamelingen, met een zoölogisch, botanisch,
                   mineralogisch, anatomisch, historisch, archeologisch, paleontologisch, etnografisch of
                   numismatisch belang;
     3°     "antiquiteiten": andere voorwerpen dan de kunstvoorwerpen en                   voorwerpen   voor
            verzamelingen bedoeld in 1° en 2° hierboven, ouder dan honderd jaar.

XXII. Automobielen voor personenvervoer voor invaliden. Onderdelen, uitrustingsstukken en
      toebehoren voor deze voertuigen.

     (De tekst van KB nr. 20, TABEL A, XXII, afdeling 1, § 5, 4° lid, werd vervangen met
     ingang van 25.05.2019 (Art. 16, W 02.05.2019, B.S. 15.05.2019, pg. 46586))

     Eerste afdeling. - Automobielen voor personenvervoer voor invaliden.

     § 1.   Mits voldaan is aan de hierna gestelde voorwaarden en onder voorbehoud van de regularisatie
     voorzien in § 5, is het verlaagd tarief van 6 pct. van toepassing op automobielen voor
     personenvervoer langs de weg, welke worden ingevoerd, intracommunautair verworven of hier te
     lande verkregen door een der nagenoemde personen om door hen als persoonlijk vervoermiddel te
     worden gebruikt:
     1°     militaire en burgerlijke oorlogsinvaliden, die een invaliditeitspensioen van ten minste 50 pct.
            genieten;
     2°     personen die volledig blind zijn, volledig verlamd zijn aan de bovenste ledematen of wier
            bovenste ledematen zijn geamputeerd, en personen met een blijvende invaliditeit die
            rechtstreeks toe te schrijven is aan de onderste ledematen en ten minste 50 pct. bedraagt.

     § 2.    Het voordeel van het verlaagd tarief kan slechts worden ingeroepen voor één enkel voertuig
     tegelijk en veronderstelt het gebruik van het ingevoerd, intracommunautair verworven of hier te
     lande verkregen voertuig door de verkrijger als persoonlijk vervoermiddel gedurende een periode
     van drie jaar, te rekenen vanaf de eerste dag van de maand waarin de invoer, de
     intracommunautaire verwerving of de levering van het voertuig plaatsvindt.

     § 3.  Wordt geacht het voertuig te bestemmen voor andere doeleinden dan voor zijn persoonlijk
     vervoer:
     1°    de invalide of gehandicapte die de verkeersbelasting betaalt niettegenstaande hij kan
           genieten van de vrijstelling van die belasting;
     2°    de invalide of gehandicapte wiens voertuig wordt ingeschreven op een andere naam dan de
           zijne of, in voorkomend geval, dan die van zijn wettige vertegenwoordiger;
     3°    de invalide of gehandicapte die, terwijl hij nog een voertuig gebruikt dat werd ingevoerd,
           intracommunautair verworven of hier te lande verkregen met toepassing van de fiscale
           voordelen inzake belasting over de toegevoegde waarde, voor een ander voertuig het
           voordeel van hetzelfde regime vraagt;

     § 4.   Het voordeel van het verlaagd tarief bij de invoer, de intracommunautaire verwerving of de
     verkrijging hier te lande van een personenauto wordt slechts verleend indien de volgende
     vormvoorwaarden tesamen vervuld zijn:
     1°    de invalide of gehandicapte moet voordat de invoer, de intracommunautaire verwerving of de
           levering van het voertuig plaatsvindt aan het hoofd van het controlekantoor in het
           ambtsgebied waarvan hij zijn woonplaats heeft een getuigschrift overleggen dat vermeldt tot
           welke categorie van invaliden of gehandicapten, beoogd in § 1, hij behoort en dat is
           uitgereikt:
           a)     voor de oorlogsinvaliden, door de overheid die het invaliditeitspensioen heeft
                  toegekend;
           b)     voor de personen die een pensioen, uitkering of vergoeding genieten door tussenkomst
                  van de Dienst voor tegemoetkomingen aan de minder-validen, door of vanwege de
                  Minister die deze dienst onder zijn bevoegdheid heeft;
           c)     voor de personen die een vergoedingspensioen of een militair pensioen genieten
                  wegens een invaliditeit opgelopen in vredestijd, door of vanwege de Minister van
                  Financiën;
           d)     voor de andere personen, door of vanwege de Minister die de Volksgezondheid onder
                  zijn bevoegdheid heeft;
     2°    na onderzoek van het getuigschrift en mits ontvangst van een schriftelijke verbintenis van de
           invalide of gehandicapte het voertuig uitsluitend te gebruiken als persoonlijk vervoermiddel,
           reikt het controlekantoor een document uit, opgesteld in de vorm bepaald door of vanwege de
           Minister van Financiën, dat toelating verleent tot invoer, intracommunautaire verwerving of
           levering van het voertuig tegen het verlaagd tarief;
     3°    de invalide of gehandicapte moet, ten laatste op het ogenblik van de invoer, van de indiening
           van de bijzondere BTW-aangifte inzake de intracommunautaire verwerving van nieuwe
           vervoermiddelen of van de levering van het voertuig, aan de douane of aan de verkoper, het
           document beoogd onder 2° overleggen;
     4°    het invoerdocument, de bijzondere BTW-aangifte inzake de intracommunautaire verwerving
           van nieuwe vervoermiddelen of de aankoopfaktuur en het dubbel ervan moeten opgesteld zijn
           op naam van de invalide of gehandicapte of, in voorkomend geval, op naam van zijn wettige
           vertegenwoordiger, en moeten melding maken van de datum van het in 2° bedoelde
           document, het referentienummer ervan en de benaming van het controlekantoor dat het heeft
           uitgereikt;
     5°    het onder 2° beoogde document wordt door de douane gevoegd bij het invoerdocument of het
           luik C van de bijzondere BTW-aangifte inzake de intracommunautaire verwerving van nieuwe
           vervoermiddelen dat op het douanekantoor wordt bewaard, of door de verkoper bij het dubbel
           van de factuur, dat hij bewaart.

     § 5.   Indien gedurende de periode van drie jaar, te rekenen vanaf de eerste dag van de maand
     waarin de invoer, de intracommunautaire verwerving of de levering van het voertuig plaatsvond, dit
     voertuig wordt aangewend voor andere doeleinden dan het persoonlijk vervoer van de invalide of
     gehandicapte, of door de invalide of gehandicapte wordt afgestaan, is deze gehouden het verschil
     tussen de belasting die tegen het tarief voorzien in het normale regime verschuldigd is voor de
     verkrijging, de intracommunautaire verwerving of de invoer van het voertuig en de belasting voldaan
     tegen het verlaagd tarief, aan de Staat te storten ten belope van zoveel zesendertigsten als er nog
     volledig te lopen maanden zijn tussen de datum van de wijziging van de bestemming of de datum
     van de afstand en de datum van het verstrijken van de periode van drie jaar.

      Deze storting dient evenwel niet te gebeuren:
      1°    in geval van overlijden van de invalide of gehandicapte of bij elke behoorlijk
            verrechtvaardigde oorzaak, onafhankelijk van zijn wil, welke hem definitief verhindert het
            voertuig nog voor zijn persoonlijk vervoer te gebruiken, zelfs indien hij dit voertuig laat
            besturen door een derde;
      2°    in geval van volledig verlies van het voertuig en de verkoop ervan als wrak ten gevolge van
            een ernstig ongeval;
      3°    meer algemeen, in elk geval van overmacht dat behoorlijk wordt verrechtvaardigd.
      De storting van de belasting ten gevolge van de regularisatie gebeurt op basis van een aangifte,
      opgesteld in de vorm bepaald door of vanwege de Minister van Financiën, welke de invalide of
      gehandicapte, binnen een maand te rekenen vanaf de datum van de wijziging van bestemming of
      van de afstand van het voertuig, moet indienen bij het controlekantoor in het ambtsgebied waarvan
      zijn woonplaats is gelegen.
      De te storten belasting wordt betaald binnen een maand te rekenen vanaf de datum van het
      betalingsbericht dat de dienst aangewezen door de minister van Financiën of zijn gemachtigde aan
      de invalide of gehandicapte stuurt. De betaling wordt uitgevoerd overeenkomstig het bepaalde in
      hoofdstuk 1 van het koninklijk besluit van 17 februari 2019 tot uitvoering van diverse wetten en tot
      aanpassing van diverse koninklijke besluiten met het oog op onder meer de harmonisatie van de
      betalingsmodaliteiten binnen de administratie van de Federale Overheidsdienst Financiën belast met
      de inning en de invordering van fiscale en niet-fiscale schuldvorderingen.

## Afdeling II - Onderdelen, uitrustingsstukken en toebehoren van voertuigen voor invaliden.

      Het verlaagd tarief van 6 pct., is van toepassing op onderdelen, uitrustingsstukken en toebehoren die
      ingevoerd, intracommunautair verworven of hier te lande verkregen worden door in de eerste
      afdeling hierboven aangewezen personen ten behoeve van de aldaar bedoelde automobielen.
      Het voordeel van het verlaagd tarief van 6 pct. is afhankelijk van de uitreiking van een factuur aan
      de koper en van de voorlegging door deze laatste, aan de douane of aan de verkoper, van een attest
      opgesteld in de vorm bepaald door of vanwege de Minister van Financiën, dat het voertuig
      identificeert waarvoor de gunstregeling wordt ingeroepen. Daarenboven dienen het invoerdocument
      of de factuur en het dubbel ervan, de datum en het referentienummer van het bovengenoemde
      attest en het controlekantoor dat dit attest heeft uitgereikt te vermelden.

XXIII. Diversen

      (De tekst van KB nr. 20, Tabel A, XXIII, 5°, werd gewijzigd, met ingang van
      01.01.2019   (Art.   175,  Decr.Vl.   18.05.2018,  B.S.  17.08.2018,  pg.   65011).
      Voorwaardelijk toekomstig recht beschikbaar (Art. 2, W 13.04.2019, B.S. 29.04.2019,
      pg. 41032) – zie de historiek in de html-versie.)

      1.    Doodkisten
      2.    Orthopedische toestellen (medisch-chirurgische gordels daaronder begrepen); breukspalken
            en andere artikelen en apparaten voor de behandeling van breuken in het beendergestel;
            kunstgebitten,   kunsttanden,     kunstogen,   kunstledematen     en    dergelijke   artikelen;
            hoorapparaten voor hardhorigen en andere voor het verhelpen of verlichten van gebreken of
            van kwalen dienende apparatuur, die door de patiënt in de hand worden gehouden of op
            andere wijze worden gedragen, dan wel worden geïmplanteerd; individueel materiaal speciaal
            ontworpen om te worden gedragen door stomapatiënten en door personen die lijden aan
            incontinentie, met uitzondering […] van luiers voor kinderen jonger dan zes jaar; het
            individueel toebehoren dat deel uitmaakt van een kunstnier inclusief de gebruikte trousses.
      3.    Looprekken, rolstoelen en dergelijke wagentjes voor invaliden en zieken, ook indien met
            motor of ander voortbewegingsmechanisme; onderdelen en toebehoren voor deze wagens.
      4.    Aërosolapparatuur en toebehoren; individueel materiaal voor de toediening van mucomyst.
      5.    Anti-decubitusmateriaal.
      6.    Hulpmiddelen speciaal ontworpen voor slechtzienden en blinden, met uitzondering van
            monturen, brilglazen en contactlenzen.
      7.    Infuuspompen voor pijnbestrijding.
      8.    Glucosemeters en toebehoren.
      9.    Assistentiehonden die personen met een handicap of ziekte assisteren en die opgeleid zijn in
            een assistentiehondenschool die door de bevoegde overheid is erkend en de speciaal
            ontworpen uitrusting voor dergelijke honden zoals harnassen.
            Als assistentiehonden worden aangemerkt: de blindengeleidehonden, de hulphonden, de
            hoorhonden, de meldhonden en de therapiehonden.

      10.    Maandverbanden, tampons, inlegkruisjes en gelijkaardige producten bestemd voor de
             hygiënische bescherming van de vrouw en de intieme tissues bestemd voor de hygiënische
             bescherming van de genitale zone van personen andere dan baby's.
      11.    Externe defibrillatoren.

XXIIIbis. Leveringen van goederen door instellingen met sociaal oogmerk

      (De tekst van KB nr. 20, TABEL A, XXIIIbis,                  is van toepassing    met   ingang van
      01.10.2000 (Art. 1 en 2, KB 20.09.2000))

      § 1.   Het verlaagd tarief van 6 pct., is van toepassing op de levering van goederen, met uitsluiting
      van de goederen beoogd in artikel 1, § 8, van het Wetboek, van goederen opgesomd in artikel 35
      van dit Wetboek, van de goederen onderworpen aan de belasting zoals beoogd in artikel 44, § 3, 1°,
      van hetzelfde Wetboek, van de goederen verkregen om te worden gebruikt als investeringsgoederen,
      van de kunstvoorwerpen of de voorwerpen voor verzamelingen of antiquiteiten, welke de in § 2
      beoogde instellingen verrichten binnen de voorwaarden voorzien in § 3, onder voorbehoud van de in
      de §§ 4 en 5 opgenomen bepalingen.

      § 2.   De toepassing van het verlaagd tarief van 6 pct. wordt voorbehouden aan de instellingen:
      1°     van Belgisch recht of van recht van een andere Lidstaat van de Europese Economische
             Ruimte;
      2°     die geenszins het stelselmatig streven naar winstbejag tot doel hebben. Met het oog hierop
             bepalen de statuten onder meer dat de eventuele winst in geen geval mag worden verdeeld,
             maar daarentegen integraal dient te worden bestemd tot het handhaven of het verbeteren
             van de verstrekte handelingen. De statuten bepalen eveneens dat ingeval van liquidatie het
             totaal van het netto-actief opnieuw wordt geïnvesteerd in een andere instelling van dezelfde
             aard;
      3°     die in hoofdzaak vrijwillig worden beheerd en bestuurd door personen die, noch voor zich
             persoonlijk noch via tussenpersonen, enig direct of indirect belang hebben in het
             exploitatieresultaat;
      4°     waarvan het doel in de zin
             -      van het besluit van de Vlaamse regering van 16 november 1994 houdende doorvoering
                    van experimenten in verband met invoegbedrijven en leereilandprojecten, of van
                    Hoofdstuk 3, Afdeling 3.5, van het besluit van de Vlaamse regering, van 17 december
                    1997, tot vaststelling van het Vlaams reglement inzake afvalvoorkoming en -beheer;
             -      van het koninklijk besluit van 30 maart 1995 tot uitvoering van Hoofdstuk II van Titel
                    IV van de wet van 21 december 1994 houdende sociale bepalingen op de
                    inschakelingsbedrijven;
             -      van het decreet van de Franse gemeenschapscommissie van Brussel-Hoofdstad van 27
                    april 1995 betreffende de erkenning van organismen voor socio-professionele
                    inschakeling en de subsidiëring van hun beroepsopleidingsactiviteiten voor werklozen
                    en laag geschoolde werkzoekenden gericht op het vergroten van hun kans op het
                    vinden of terugvinden van werk in het raam van gecoördineerde voorzieningen voor
                    socio-professionele inschakeling;
             -      van het decreet van de Waalse Gewestelijke Raad en van de Waalse regering van 16
                    juli 1998 betreffende de voorwaarden waaronder de inschakelingsbedrijven worden
                    erkend en gesubsidieerd;
             -      van het besluit van de Vlaamse regering van 10 november 1998 houdende doorvoering
                    van experimenten in verband met invoegbedrijven;
             -      van de ordonnantie van de Raad van het Brusselse Hoofdstedelijk Gewest en van de
                    Brusselse Hoofdstedelijke Regering van 22 april 1999 betreffende de erkenning en de
                    financiering van de inschakelingsondernemingen;
             -      van het besluit van de Vlaamse regering van 8 juni 1999 tot wijziging van het besluit
                    van de Vlaamse regering van 8 december 1998 tot uitvoering van het decreet inzake
                    sociale werkplaatsen;
                    of
             -      van het besluit van de Waalse regering van 18 november 1999 tot wijziging van het
                    besluit van de Waalse regering van 6 april 1995 betreffende de erkenning van de
                    "Enterprises de formation par le travail" (Bedrijven voor vorming door arbeid), bestaat
                    in het tewerkstellen alsook in het verzekeren van de werkgelegenheid van de laag- of
                    middelmatig geschoolde werkloze werkzoekenden die uit de traditionele arbeidscircuits
                    zijn uitgesloten of bijzonder moeilijk bemiddelbaar zijn;
      5°     en die daartoe erkend zijn door de overheid die door die decreten, besluiten of ordonnantie
             bevoegd wordt verklaard.

     § 3.  De toepassing van het verlaagd tarief van 6 pct. is eveneens onderworpen aan de volgende
     voorwaarden waaraan samen moet worden voldaan:
     1°     de in § 2 beoogde instelling moet haar werkzaamheden uitsluitend beperken tot de verkoop
            van goederen beoogd in § 1, die zij gratis aan huis bij particulieren of ondernemingen ophaalt
            of op een andere manier;
     2°     deze instelling dient prijzen toe te passen die zijn goedgekeurd door de overheid, of prijzen
            die niet hoger liggen dan de goedgekeurde prijzen, of nog, voor handelingen waarvoor geen
            goedkeuring van prijzen plaatsvindt, prijzen die lager zijn dan die welke voor soortgelijke
            diensten in rekening worden gebracht door commerciële ondernemingen die aan de
            belastingen over de toegevoegde waarde zijn onderworpen;
     3°     het voordeel van het verlaagd tarief mag niet van dien aard zijn dat het leidt tot
            concurrentievervalsing ten nadele van commerciële ondernemingen die aan de belasting over
            de toegevoegde waarde zijn onderworpen.

     § 4.     Het verlaagd tarief is van rechtswege niet meer van toepassing vanaf het ogenblik dat de
     instelling die er de toepassing van inroept, niet meer voldoet aan het geheel van de ter zake vereiste
     voorwaarden.

     § 5.  De Minister van Financiën informeert zich bij de in § 2, 5° beoogde bevoegde overheden naar
     de door deze overheden verleende, ingetrokken of opgeschorte erkenningen. Hij licht diezelfde
     overheden in van gedane vaststellingen waarbij de toepassing van het verlaagd tarief vervalt of is
     komen te vervallen wegens het niet naleven van één of meerdere in § 3 bepaalde voorwaarden.

                                              DIENSTEN

XXIV. Landbouwdiensten.

      Bebouwingswerkzaamheden, oogstwerkzaamheden en teeltwerkzaamheden, met uitzondering van:
      a)    diensten met betrekking tot dieren, andere dan die bedoeld in rubriek I;
      b)    aanleg en onderhoud van tuinen.
      De goederen die ter gelegenheid van die werkzaamheden worden geleverd worden belast tegen het
      tarief dat erop van toepassing zou geweest zijn waren ze afzonderlijk geleverd.

XXV. Vervoer.

      Personenvervoer, alsmede vervoer van niet geregistreerde bagage en van dieren welke de reizigers
      vergezellen.

XXVI. Onderhoud en herstelling.

      (De tekst van KB nr. 20, Tabel A, rubriek XXVI, eerste lid, werd gewijzigd met ingang
      van 01.01.2018 (Art. 2, KB 10.12.2017, B.S. 22.12.2017, pg. 114228))

      Onderhouds- en herstellingswerken aan de goederen bedoeld in de rubrieken XXII en XXIII, cijfers 2
      tot en met 8 en cijfer 11.
      Het tarief van 6 pct. is eveneens van toepassing op de benodigdheden, de onderdelen en het
      toebehoren gebruikt bij de uitvoering van die werken.
      Voor onderhouds- en herstellingswerken aan automobielen verricht voor rekening van in rubriek
      XXII, eerste afdeling, aangewezen personen, ten behoeve van de aldaar bedoelde automobielen, is
      het voordeel van het verlaagd tarief afhankelijk van de uitreiking van een factuur aan de klant en
      van de voorlegging door deze laatste aan de dienstverrichter van een attest, opgesteld in de vorm
      bepaald door of vanwege de Minister van Financiën, dat het voertuig identificeert waarvoor de
      gunstregeling wordt ingeroepen. Daarenboven dienen de factuur en het dubbel ervan de datum en
      het referentienummer van het bovengenoemde attest en het controlekantoor dat dit attest heeft
      uitgereikt te vermelden.

XXVII. (Opgeheven bij KB 25.03.1977)

XXVIII. Inrichtingen voor cultuur, sport of vermaak.

      (De tekst van KB nr. 20, TABEL A, XXVIII, is van toepassing met ingang van 01.04.1998
      (Art. 1, A en B, KB 25.03.1998 en art. 1, A en B, KB 30.03.1998))

      De toekenning van het recht op toegang tot inrichtingen voor cultuur, sport of vermaak, alsmede de
      toekenning van het recht gebruik ervan te maken, met uitzondering van:
      a)    de toekenning van het recht gebruik te maken van automatische ontspanningstoestellen;
      b)    de terbeschikkingstelling van roerende goederen;

XXIX. Auteursrechten; uitvoeren van concerten en voorstellingen.

      (De tekst van KB nr. 20, TABEL A, XXIX, is van toepassing met ingang van 01.04.1998
      (Art. 1, A en B, KB 25.03.1998 en art. 1, A en B, KB 30.03.1998))

      1°    De overdracht van auteursrechten en het verlenen van rechten op auteursrechten met
            uitzondering van deze die betrekking hebben op computerprogramma's.
      2°    De diensten die bestaan in het uitvoeren van toneelwerken, balletten, muziekstukken, circus-,
            variété- of cabaretvoorstellingen en soortgelijke activiteiten en die behoren tot de normale
            werkzaamheid van acteurs, orkestleiders, muzikanten en andere artiesten, ook indien deze
            diensten verstrekt worden door een rechtspersoon of een feitelijke vereniging of groepering.
      Van deze rubriek worden uitgesloten de diensten die betrekking hebben op reclame.

XXX. Hotels, camping.

      1°    Het verschaffen van gemeubeld logies met of zonder ontbijt.
      2°    De terbeschikkingstelling van plaats om te kamperen.

XXXI. Werk in onroerende staat met betrekking tot privé-woningen.

     (De tekst van KB nr. 20, Tabel A, rubriek XXXI, § 1, werd gewijzigd met ingang van
     01.01.2013. (Art. 24, KB 30.04.2013, B.S. 08.05.2013))

     § 1.  Het werk in onroerende staat en de andere handelingen bedoeld in paragraaf 3 worden
     onderworpen aan het verlaagd tarief, voor zover de volgende voorwaarden zijn vervuld:
     1°     de handelingen moeten de omvorming, renovatie, rehabilitatie, verbetering, herstelling of het
            onderhoud, met uitsluiting van de reiniging, geheel of ten dele van een woning tot voorwerp
            hebben;
     2°     de handelingen moeten betrekking hebben op een woning die, na de uitvoering ervan, hetzij
            uitsluitend, hetzij hoofdzakelijk, als privé-woning wordt gebruikt;
     3°     de handelingen moeten worden verricht aan een woning waarvan de eerste ingebruikneming
            ten minste vijftien jaar voorafgaat aan het eerste tijdstip van opeisbaarheid van de btw dat
            zich voordoet overeenkomstig artikel 22, § 1 of artikel 22bis van het Wetboek;
     4°     de handelingen moeten worden verstrekt en gefactureerd aan een eindverbruiker;
     5°     de door de dienstverrichter uitgereikte factuur en het dubbel dat hij bewaart, moeten, op
            basis van een duidelijk en nauwkeurig attest van de afnemer, melding maken van het
            voorhanden zijn van de elementen die de toepassing van het verlaagd tarief rechtvaardigen;
            behalve in geval van samenspanning tussen de partijen of klaarblijkelijk niet naleven van
            onderhavige bepaling, ontlast het attest van de afnemer de dienstverrichter van de
            aansprakelijkheid betreffende de vaststelling van het tarief.

     § 2.   Worden aangemerkt als eindverbruikers in de zin van deze bepaling, voor het werk in
     onroerende staat en de andere handelingen omschreven in § 3, met betrekking tot de woningen
     daadwerkelijk gebruikt voor de huisvesting van bejaarden, leerlingen en studenten, minderjarigen,
     thuislozen, personen in moeilijkheden, personen met een psychische stoornis, mentaal
     gehandicapten en psychiatrische patiënten, de publiekrechtelijke of privaatrechtelijke personen die
     beheren:
     1°     verblijfsinrichtingen voor bejaarden welke door de bevoegde overheid zijn erkend in het kader
            van de wetgeving inzake bejaardenzorg;
     2°     internaten die zijn toegevoegd aan scholen of universiteiten of die ervan afhangen;
     3°     jeugdbeschermingstehuizen en residentiële voorzieningen die op duurzame wijze, in dag- en
            nachtverblijf, minderjarigen huisvesten en die erkend zijn door de bevoegde overheid in het
            kader van de wetgeving op de jeugdbescherming of de bijzondere jeugdbijstand;
     4°     opvangtehuizen die in dag- en nachtverblijf thuislozen en personen in moeilijkheden
            huisvesten en die erkend zijn door de bevoegde overheid.
     5°     psychiatrische verzorgingstehuizen die op een duurzame wijze in dag- en nachtverblijf
            personen met een langdurige en gestabiliseerde psychische stoornis of mentaal gehandicapten
            huisvesten en die door de bevoegde overheid erkend zijn;
     6°     gebouwen waar, ten titel van een initiatief van beschut wonen erkend door de bevoegde
            overheid, het op een duurzame wijze huisvesten in dag- en nachtverblijf en het begeleiden
            van psychiatrische patiënten plaatsheeft.

     § 3.   Worden beoogd:
     1°     het verbouwen, het afwerken, het inrichten, het herstellen en het onderhouden, met
            uitsluiting van het reinigen, geheel of ten dele, van een uit zijn aard onroerend goed;
     2°     prestaties die erin bestaan een roerend goed te leveren en het meteen op zodanige wijze aan
            te brengen aan een onroerend goed dat het onroerend uit zijn aard wordt;
     3°     iedere handeling, ook indien niet beoogd in 2° hierboven, die tot voorwerp heeft zowel de
            levering als de aanhechting aan een gebouw:
            a)     van de bestanddelen of een gedeelte van de bestanddelen van een installatie voor
                   centrale verwarming of airconditioning, daaronder begrepen de branders, de reservoirs
                   en de regel- en controletoestellen verbonden aan de ketel of aan de radiatoren;
            b)     van de bestanddelen of een gedeelte van de bestanddelen van een sanitaire installatie
                   van een gebouw en, meer algemeen, van al de vaste toestellen voor sanitair of
                   hygiënisch gebruik aangesloten op een waterleiding of een riool;
            c)     van de bestanddelen of een gedeelte van de bestanddelen van een elektrische
                   installatie van een gebouw, met uitzondering van toestellen voor de verlichting en van
                   lampen;
            d)     van de bestanddelen of een gedeelte van de bestanddelen van een elektrische
                   belinstallatie, van brandalarmtoestellen, van alarmtoestellen tegen diefstal en van een
                   huistelefoon;

            e)     van opbergkasten, gootstenen, gootsteenkasten en meubels met ingebouwde
                   gootsteen, wastafels en meubels met ingebouwde wasbak, zuigkappen, ventilators en
                   luchtverversers waarmee een keuken of een badkamer is uitgerust;
            f)     van luiken, rolluiken en rolgordijnen die aan de buitenkant van het gebouw worden
                   geplaatst;
     4°     iedere handeling, ook indien niet beoogd in 2° hierboven, die tot voorwerp heeft zowel de
            levering van wandbekleding of vloerbekleding of -bedekking als de plaatsing ervan in een
            gebouw ongeacht of die bekleding of bedekking aan het gebouw wordt vastgehecht of
            eenvoudig ter plaatse op maat gesneden volgens de afmetingen van de te bedekken
            oppervlakte;
     5°     het aanhechten, het plaatsen, het herstellen en het onderhouden, met uitsluiting van het
            reinigen, van goederen bedoeld in 3° en 4° hierboven;
     6°     de terbeschikkingstelling van personeel met het oog op het verrichten van de hierboven
            bedoelde handelingen.

     § 4.   Het verlaagd tarief is in geen geval van toepassing op:
     1°     werk in onroerende staat en andere onroerende handelingen die geen betrekking hebben op
            de eigenlijke woning, zoals bebouwingswerkzaamheden, tuinaanleg en oprichten van
            afsluitingen;
     2°     werk in onroerende staat en andere onroerende handelingen die tot voorwerp hebben de
            bestanddelen of een gedeelte van de bestanddelen van zwembaden, sauna's, midget-
            golfbanen, tennisterreinen en dergelijke installaties.

XXXII. Privé-woningen voor gehandicapten.

     (De tekst van KB nr. 20, Tabel A, rubriek XXXII, § 1, 1°, c en 3°, werd gewijzigd met
     ingang van 01.05.2019 (Art. 27, KB 29.08.2019, B.S. 13.09.2019, pg. 86195).
     Artikel 27 heeft uitwerking met ingang van 1 mei 2019 en is van toepassing op de erin
     vermelde vennootschappen vanaf de dag waarop de bepalingen van het Wetboek van
     vennootschappen en verenigingen die betrekking hebben op deze vennootschappen op hen
     van toepassing worden (Art. 39 KB 29.08.2019))

     § 1.     Mits voldaan is aan de hierna gestelde voorwaarden, is het verlaagd tarief van toepassing op
     de werken in onroerende staat in de zin van artikel 19, § 2, tweede lid, van het Wetboek, met
     uitsluiting van het reinigen, en op de andere handelingen opgesomd in rubriek XXXI, § 3, 3° tot 6°:
     1°     de handelingen moeten worden verstrekt en gefactureerd aan hetzij:
            a)      een gewestelijke huisvestingsmaatschappij of een door haar erkende maatschappij
                    voor sociale huisvesting;
            b)      een provincie, een intercommunale, een gemeente, een intercommunaal openbaar
                    centrum voor maatschappelijk welzijn of een openbaar centrum voor maatschappelijk
                    welzijn;
            c)      een vereniging zonder winstoogmerk of een coöperatieve vennootschap erkend als
                    sociale onderneming overeenkomstig artikel 8:5 van het Wetboek van
                    vennootschappen en verenigingen die in het kader van het huisvestingsbeleid van
                    personen met een handicap worden erkend door de bevoegde overheid of door een
                    door haar opgericht agentschap of fonds voor personen met een handicap;
     2°     de handelingen moeten worden verricht aan een woning die, in ieder geval na de uitvoering
            ervan, specifiek aangepast is om door een gehandicapte als privé-woning te worden gebruikt;
     3°     de handelingen moeten worden verricht aan een woning die bestemd is om te worden
            verhuurd, door een onder 1° bedoelde instelling, maatschappij, vereniging zonder
            winstoogmerk of coöperatieve vennootschap erkend als sociale onderneming overeenkomstig
            artikel 8:5 van het Wetboek van vennootschappen en verenigingen aan een persoon met een
            handicap die een tegemoetkoming geniet van een fonds of een agentschap voor personen met
            een handicap dat door de bevoegde overheid is erkend;
     4°     de door de dienstverrichter uitgereikte factuur en het dubbel dat hij bewaart, moeten, op
            basis van een duidelijk en nauwkeurig attest van de afnemer, melding maken van het
            voorhanden zijn van de elementen die de toepassing van het verlaagd tarief rechtvaardigen;
            behalve in geval van samenspanning tussen de partijen of klaarblijkelijk niet naleven van
            onderhavige bepaling, ontlast het attest van de afnemer de dienstverrichter van de
            aansprakelijkheid betreffende de vaststelling van het tarief.

     § 2.   Het verlaagd tarief is in geen geval van toepassing op:
     1°     werk in onroerende staat en de andere onroerende handelingen die geen betrekking hebben
            op de eigenlijke woning, zoals bebouwingswerkzaamheden, tuinaanleg en oprichten van
            afsluitingen;
     2°     werk in onroerende staat en andere onroerende handelingen die tot voorwerp hebben de
            bestanddelen of een gedeelte van de bestanddelen van zwembaden, sauna's, midget-
            golfbanen, tennisterreinen en dergelijke installaties.

      § 3.    Het verlaagd tarief is eveneens van toepassing op de leveringen van goederen bedoeld in
      artikel 1, § 9, van het Wetboek alsook op de vestigingen, overdrachten en wederoverdrachten van
      zakelijke rechten op zulke goederen die niet overeenkomstig artikel 44, § 3, 1°, van het Wetboek
      van de belasting zijn vrijgesteld, wanneer die goederen:
      -      speciﬁek zijn aangepast om door een gehandicapte als privé-woning te worden gebruikt;
      -      worden geleverd en gefactureerd aan de instellingen of maatschappijen bedoeld in paragraaf
             1, 1°;
      -      en bestemd zijn om te worden verhuurd door deze instellingen of maatschappijen aan
             gehandicapten bedoeld in paragraaf 1, 3°.

      § 4.   Het verlaagd tarief is eveneens van toepassing op de onroerende financieringshuur of
      onroerende leasing bedoeld in artikel 44, § 3, 2°, b), van het Wetboek en op de onroerende verhuur
      bedoeld in artikel 44, § 3, 2°, d), van het Wetboek, die betrekking hebben op gebouwen die specifiek
      aangepast zijn om door een gehandicapte als privéwoning te worden gebruikt, wanneer de afnemer
      een in § 1, 1°, genoemde maatschappij of instelling is die deze gebouwen verhuurt aan de in § 1, 3°,
      genoemde gehandicapten.

XXXIII. Instellingen voor gehandicapten.

      (De tekst van KB nr. 20, Tabel A, rubriek XXXIII, § 4, werd vervangen met ingang van
      01.01.2019   (Art.  10,   W  14.10.2018,   B.S.  25.10.2018,   pg.   81448.  Erratum
      B.S. 30.11.2018, pg. 91362))

      § 1.     Mits voldaan is aan de hierna gestelde voorwaarden, is het verlaagd tarief van toepassing op
      de werken in onroerende staat in de zin van artikel 19, § 2, tweede lid, van het Wetboek, met
      uitsluiting van het reinigen, en op de andere handelingen opgesomd in rubriek XXXI, § 3, 3° tot 6°:
      1°     de handelingen moeten worden verricht aan woningcomplexen bestemd om te worden
             gebruikt voor huisvesting van gehandicapten;
      2°     de handelingen moeten worden verstrekt en gefactureerd aan een publiekrechtelijke of
             privaatrechtelijke persoon die een instelling beheert die op duurzame wijze, in dag- en
             nachtverblijf, personen met een handicap huisvest en die om deze reden een tegemoetkoming
             geniet van een fonds of een agentschap voor personen met een handicap dat door de
             bevoegde overheid is erkend;
      3°     de door de dienstverrichter uitgereikte factuur en het dubbel dat hij bewaart, moeten, op
             basis van een duidelijk en nauwkeurig attest van de afnemer, melding maken van het
             voorhanden zijn van de elementen die de toepassing van het verlaagd tarief rechtvaardigen;
             behalve in geval van samenspanning tussen de partijen of klaarblijkelijk niet naleven van
             onderhavige bepaling, ontlast het attest van de afnemer de dienstverrichter van de
             aansprakelijkheid betreffende de vaststelling van het tarief.

      § 2.   Het verlaagd tarief is in geen geval van toepassing op:
      1°     werk in onroerende staat en de andere onroerende handelingen die geen betrekking hebben
             op de eigenlijke woning, zoals bebouwingswerkzaamheden, tuinaanleg en oprichten van
             afsluitingen;
      2°     werk in onroerende staat en andere onroerende handelingen die tot voorwerp hebben de
             bestanddelen of een gedeelte van de bestanddelen van zwembaden, sauna's, midget-
             golfbanen, tennisterreinen en dergelijke installaties.

      § 3.    Het verlaagd tarief is eveneens van toepassing op de leveringen van goederen bedoeld in
      artikel 1, § 9, van het Wetboek alsook op de vestigingen, overdrachten en wederoverdrachten van
      zakelijke rechten op zulke goederen die niet overeenkomstig artikel 44, § 3, 1°, van het Wetboek
      van de belasting zijn vrijgesteld, wanneer die gebouwen bestemd zijn om als woningcomplex te
      worden gebruikt voor de huisvesting van gehandicapten en ze worden geleverd en gefactureerd aan
      een in paragraaf 1, 2° bedoelde publiekrechtelijke of privaatrechtelijke persoon.

      § 4.   Het verlaagd tarief is eveneens van toepassing op de onroerende financieringshuur of
      onroerende leasing bedoeld in artikel 44, § 3, 2°, b), van het Wetboek en op de onroerende verhuur
      bedoeld in artikel 44, § 3, 2°, d), van het Wetboek, die betrekking hebben op woningcomplexen
      bestemd om te worden gebruikt voor de huisvesting van gehandicapten, wanneer de afnemer een in
      § 1, 2°, genoemde publiekrechtelijke of privaatrechtelijke persoon is.

XXXIV. Diversen.

      (De tekst van KB nr. 20, Tabel A, rubriek XXXIV, cijfer 1, werd gewijzigd met ingang
      van 01.01.2018 (Art. 3, KB 10.12.2017, B.S. 22.12.2017, pg. 114288). Voorwaardelijk
      toekomstig recht beschikbaar (Art. 2, W 06.06.2019, B.S. 26.06.2019, pg. 65569) – zie
      de historiek in de html-versie.)

      1°     De verhuur van goederen bedoeld in rubriek XXIII, cijfers 2 tot en met 8 en cijfer 11.
      2°     De diensten die gewoonlijk door begrafenisondernemers worden verstrekt in de normale
             uitoefening van hun beroepswerkzaamheid, met uitzondering van:
             a)     het verschaffen van spijzen of dranken om ter plaatse te worden verbruikt;
             b)     de diensten verstrekt door kelners, diensters en alle andere personen die tussenkomen
                    bij het verschaffen van spijzen en dranken aan de verbruikers in omstandigheden die
                    het verbruik ter plaatse mogelijk maken;
             c)     de diensten met betrekking tot de levering met plaatsing van grafkelders of -
                    monumenten.
      3°     De opleiding van assistentiehonden, bedoeld in cijfer 9 van rubriek XXIII door een
             assistentiehondenschool die door de bevoegde overheid is erkend en de diensten verstrekt
             door dierenartsen aan deze assistentiehonden.
      4°     (opgeheven).

XXXV. Diensten verricht door instellingen met sociaal oogmerk

      (De tekst van KB nr. 20, TABEL A, XXXV, is van toepassing met ingang van 01.10.2000
      (Art. 1 en 2, KB 20.09.2000))

      § 1.   Het verlaagd tarief van 6 pct., is van toepassing op de diensten, met uitzondering van het
      werk in onroerende staat in de zin van artikel 19, § 2, tweede lid, van het Wetboek, van de
      handelingen opgesomd in rubriek XXXI, § 3, 3° tot 6°, van de huidige tabel A, alsook van het
      onderhoud en de herstellingen van de goederen opgesomd in artikel 35 van het Wetboek, inbegrepen
      de leveringen van onderdelen, uitrustingsstukken en toebehoren die worden gebruikt voor de
      uitvoering van die werken, die in de § 2 beoogde instellingen verrichten binnen de voorwaarden
      voorzien in § 3, onder voorbehoud van de in §§ 4 en 5 opgenomen bepalingen.

      § 2.   De toepassing van het verlaagd tarief van 6 pct. wordt voorbehouden aan de instellingen:
      1°     van Belgisch recht of van recht van een andere Lidstaat van de Europese Economische
             Ruimte;
      2°     die geenszins het stelselmatig streven naar winstbejag tot doel hebben. Met het oog hierop
             bepalen de statuten onder meer dat de eventuele winst in geen geval mag worden verdeeld,
             maar daarentegen integraal dient te worden bestemd tot het handhaven of het verbeteren
             van de verstrekte handelingen. Deze statuten bepalen eveneens dat ingeval van liquidatie het
             totaal van het netto-actief opnieuw wordt geïnvesteerd in een andere instelling van dezelfde
             aard;
      3°     die in hoofdzaak vrijwillig worden beheerd en bestuurd door personen die, noch voor zich
             persoonlijk noch via tussenpersonen, enig direct of indirect belang hebben in het
             exploitatieresultaat;
      4°     waarvan het doel in de zin
             -      van het besluit van de Vlaamse regering van 16 november 1994 houdende doorvoering
                    van experimenten in verband met invoegbedrijven en leereilandprojecten, of van
                    Hoofdstuk 3, Afdeling 3.5, van het besluit van de Vlaamse regering, van 17 december
                    1997, tot vaststelling van het Vlaams reglement inzake afvalvoorkoming en -beheer;
             -      van het koninklijk besluit van 30 maart 1995 tot uitvoering van Hoofdstuk II van Titel
                    IV van de wet van 21 december 1994 houdende sociale bepalingen op de
                    inschakelingsbedrijven;
             -      van het decreet van de Franse gemeenschapscommissie van Brussel-Hoofdstad van 27
                    april 1995 betreffende de erkenning van organismen voor socio-professionele
                    inschakeling en de subsidiëring van hun beroepsopleidingsactiviteiten voor werklozen
                    en laag geschoolde werkzoekenden gericht op het vergroten van hun kans op het
                    vinden of terugvinden van werk in het raam van gecoördineerde voorzieningen voor
                    socio-professionele inschakeling;
             -      van het decreet van de Waalse Gewestelijke Raad en van de Waalse regering van 16
                    juli 1998 betreffende de voorwaarden waaronder de inschakelingsbedrijven worden
                    erkend en gesubsidieerd;
             -      van het besluit van de Vlaamse regering van 10 november 1998 houdende doorvoering
                    van experimenten in verband met invoegbedrijven;

             -      van de ordonnantie van de Raad van het Brusselse Hoofdstedelijk Gewest en van de
                    Brusselse Hoofdstedelijke Regering van 22 april 1999 betreffende de erkenning en de
                    financiering van de inschakelingsondernemingen;
             -      van het besluit van de Vlaamse regering van 8 juni 1999 tot wijziging van het besluit
                    van de Vlaamse regering van 8 december 1998 tot uitvoering van het decreet inzake
                    sociale werkplaatsen;
                    of
             -      van het besluit van de Waalse regering van 18 november 1999 tot wijziging van het
                    besluit van de Waalse regering van 6 april 1995 betreffende de erkenning van de
                    "Entreprises de formation par le travail" (Bedrijven voor vorming van arbeid),
             -      Bestaat in het tewerkstellen alsook in het verzekeren van de werkgelegenheid van de
                    laag-of middelmatig geschoolde werkloze werkzoekenden die uit de traditionele
                    arbeidscircuits zijn uitgesloten of bijzonder moeilijk bemiddelbaar zijn;
      5°     en die daartoe erkend zijn door de overheid die door die decreten, besluiten of ordonnantie
             bevoegd wordt verklaard.

      § 3.  De toepassing van het verlaagd tarief van 6 pct. is eveneens onderworpen aan de volgende
      voorwaarden waaraan samen moet worden voldaan:
      1°     de in § 2 beoogde instelling moet haar werkzaamheden uitsluitend beperken tot de diensten
             beoogd in § 1;
      2°     deze instelling dient prijzen toe te passen die zijn goedgekeurd door de overheid, of prijzen
             die niet hoger liggen dan de goedgekeurde prijzen, of nog, voor handelingen waarvoor geen
             goedkeuring van prijzen plaatsvindt, prijzen die lager zijn dan die welke voor soortgelijke
             diensten in rekening worden gebracht door commerciële ondernemingen die aan de
             belastingen over de toegevoegde waarde zijn onderworpen;
      3°     het voordeel van het verlaagd tarief mag niet van dien aard zijn dat het leidt tot
             concurrentievervalsing ten nadele van commerciële ondernemingen die aan de belasting over
             de toegevoegde waarde zijn onderworpen.

      § 4.     Het verlaagd tarief is van rechtswege niet meer van toepassing vanaf het ogenblik dat de
      instelling die er de toepassing van inroept, niet meer voldoet aan het geheel van de ter zake vereiste
      voorwaarden.

      § 5.  De Minister van Financiën informeert zich bij de in § 2, 5° beoogde bevoegde overheden naar
      de door deze overheden verleende, ingetrokken of opgeschorte erkenningen. Hij licht diezelfde
      overheden in van gedane vaststellingen waarbij de toepassingen van het verlaagd tarief vervalt of is
      komen te vervallen wegens het niet naleven van één of meerdere in § 3 bepaalde voorwaarden.

XXXVI. Huisvesting in het kader van het sociaal beleid

      (De tekst van KB nr. 20, Tabel A, rubriek XXXVI, § 1, 3°, werd vervangen met ingang
      van 01.01.2019 (Art. 11, W 14.10.2018, B.S. 25.10.2018, pg. 81448. Erratum
      Nederlandse tekst B.S. 30.11.2018, pg. 91362))

      § 1.   Het verlaagd tarief van zes percent is van toepassing op:
      1°     de leveringen van nagenoemde goederen bedoeld in artikel 1, § 9, van het Wetboek alsook de
             vestigingen, overdrachten en wederoverdrachten van zakelijke rechten op zulke goederen die
             niet overeenkomstig artikel 44, § 3, 1°, van het Wetboek van de belasting zijn vrijgesteld,
             wanneer die goederen bestemd zijn voor de huisvesting in het kader van het sociaal beleid:
             a)     privé-woningen die worden geleverd en gefactureerd aan de gewestelijke
                    huisvestingsmaatschappijen en aan de door hen erkende maatschappijen voor sociale
                    huisvesting, aan het Vlaams Woningfonds, "le Fonds du Logement des familles
                    nombreuses de Wallonie" en het Woningfonds van het Brussels Hoofdstedelijk Gewest
                    en die door deze maatschappijen of fondsen worden bestemd om te worden verhuurd;
             b)     privé-woningen die worden geleverd en gefactureerd aan de gewestelijke
                    huisvestingsmaatschappijen, aan de door hen erkende maatschappijen voor sociale
                    huisvesting, aan het Vlaams Woningfonds, "le Fonds du Logement des Familles
                    nombreuses de Wallonie" en het Woningfonds van het Brussels Hoofdstedelijk Gewest
                    en die door deze maatschappijen of fondsen worden bestemd om te worden verkocht;
             c)     privé-woningen die worden geleverd en gefactureerd door de gewestelijke
                    huisvestingsmaatschappijen, door de door hen erkende maatschappijen voor sociale
                    huisvesting en door het Vlaams Woningfonds, "le Fonds du Logement des Familles
                    nombreuses de Wallonie" en het Woningfonds van het Brussels Hoofdstedelijk Gewest;

     2°     werk in onroerende staat in de zin van artikel 19, § 2, tweede lid, van het Wetboek, met
            uitsluiting van het reinigen, en de andere handelingen opgesomd in rubriek XXXI, § 3, 3° tot
            6°, van tabel A met betrekking tot de onder 1° genoemde privé-woningen mits die worden
            verstrekt en gefactureerd aan de gewestelijke huisvestingmaatschappijen, aan de door hen
            erkende maatschappijen voor sociale huisvesting en aan het Vlaams Woningfonds, "le Fonds
            du Logement des Familles nombreuses de Wallonie" en het Woningfonds van het Brussels
            Hoofdstedelijk Gewest;
     3°     de onroerende financieringshuur of onroerende leasing bedoeld in artikel 44, § 3, 2°, b), van
            het Wetboek en de onroerende verhuur bedoeld in artikel 44, § 3, 2°, d) van het Wetboek, die
            betrekking hebben op de onder 1° bedoelde privéwoningen wanneer de afnemer een
            gewestelijke huisvestingsmaatschappij, een door die maatschappij erkende maatschappij voor
            sociale huisvesting of het Vlaams Woningfonds, "le Fonds du Logement des Familles
            nombreuses de Wallonie" en het Woningfonds van het Brussels Hoofdstedelijk Gewest is..

     § 2.   Het verlaagd tarief van 6 pct. is in geen geval van toepassing op:
     1°     werk in onroerende staat en andere onroerende handelingen die geen betrekking hebben op
            de eigenlijke woning, zoals bebouwingswerkzaamheden, tuinaanleg en oprichten van
            afsluitingen;
     2°     werk in onroerende staat en andere onroerende handelingen die tot voorwerp hebben de
            bestanddelen of een gedeelte van de bestanddelen van zwembaden, sauna's, midget-
            golfbanen, tennisterreinen en dergelijke installaties.

XXXVII. Afbraak en heropbouw van gebouwen in stadsgebieden

     (De tekst van KB nr. 20, Tabel A, rubriek XXXVII, tweede lid, 4°, a), en 5°, werd
     gewijzigd met ingang van 01.01.2013 (Art. 27, KB 30.04.2013, B.S. 08.05.2013))

     Het verlaagd tarief van 6 pct., is van toepassing op het werk in onroerende staat en de andere
     handelingen opgesomd in rubriek XXXI, § 3, 3° tot 6°, die tot voorwerp hebben de afbraak en de
     daarmee gepaard gaande heropbouw van een woning.
     Het voordeel van het verlaagd tarief is onderworpen aan het vervullen van de navolgende
     voorwaarden:
     1°     de handelingen moeten betrekking hebben op een woning die, na de uitvoering van de
            werken, hetzij uitsluitend, hetzij hoofdzakelijk als privé-woning wordt gebruikt;
     2°     de handelingen moeten betrekking hebben op een woning die gelegen is in één van de grote
            steden opgesomd in de koninklijke besluiten van 12 augustus 2000, 26 september 2001 en 28
            april 2005 ter uitvoering van artikel 3 van de wet van 17 juli 2000 tot bepaling van de
            voorwaarden waaronder de plaatselijke overheden een financiële bijstand kunnen genieten
            van de Staat in het kader van het stedelijk beleid;
     3°     [opgeheven]
     4°     de bouwheer moet:
            a)     vooraleer de belasting opeisbaar wordt overeenkomstig de artikelen 22, § 1 en 22bis
                   van het Wetboek, bij het controlekantoor van de belasting over de toegevoegde
                   waarde van het ambtsgebied waarin het gebouw is gelegen een verklaring indienen.
                   Deze verklaring dient te vermelden dat het gebouw dat hij laat afbreken en
                   heroprichten bedoeld is om hetzij uitsluitend, hetzij hoofdzakelijk, als privé-woning te
                   worden gebruikt en dient vergezeld te zijn van een afschrift van:
                   -      de bouwvergunning;
                   -      het (de) aannemingscontract(en).
            b)     aan de dienstverrichter een afschrift van de verklaring bedoeld onder a) overhandigen.
     5°     het tijdstip waarop de belasting opeisbaar wordt overeenkomstig de artikelen 22, § 1 en 22bis
            van het Wetboek, moet zich voordoen uiterlijk op 31 december van het jaar van de eerste
            ingebruikneming van het gebouw;
     6°     de door de dienstverrichter uitgereikte factuur en het dubbel dat hij bewaart, moeten, op
            basis van het afschrift bedoeld onder punt 4°, b), hiervoor, melding maken van het
            voorhanden zijn van de elementen die de toepassing van het verlaagd tarief rechtvaardigen;
            behalve in geval van samenspanning tussen de partijen of klaarblijkelijk niet naleven van
            onderhavige bepaling, ontlast de verklaring van de afnemer de dienstverrichter van de
            aansprakelijkheid betreffende de vaststelling van het tarief.
     Het verlaagd tarief is in geen geval van toepassing op:
     1°     werk in onroerende staat en andere onroerende handelingen die geen betrekking hebben op
            de eigenlijke woning, zoals bebouwingswerkzaamheden, tuinaanleg en oprichten van
            afsluitingen;

     2°     werk in onroerende staat en andere onroerende handelingen die tot voorwerp hebben de
            bestanddelen of een gedeelte van de bestanddelen van zwembaden, sauna's, midget-
            golfbanen, tennisterreinen en dergelijke installaties;
     3°     gehele of gedeeltelijke reiniging van een woning.

XXXVIII. Renovatie en herstel van privéwoningen

     (KB nr. 20, Tabel A, rubriek XXXVIII, § 1, 3°, werd gewijzigd met ingang van
     12.02.2016 (Art. 1, KB 26.01.2016, B.S. 02.02.2016. Het KB 26.01.2016 werd
     bekrachtigd bij art. 16, 1°, W 22.10.2017, B.S. 10.11.2017, pg. 98213))

     § 1.     Het werk in onroerende staat en de andere handelingen bedoeld in paragraaf 3, met
     uitsluiting van de materialen die een beduidend deel vertegenwoordigen van de verstrekte dienst,
     worden onderworpen aan het verlaagd tarief, voor zover de volgende voorwaarden zijn vervuld:
     1°     de handelingen moeten de omvorming, renovatie, rehabilitatie, verbetering, herstelling of het
            onderhoud, met uitsluiting van de reiniging, geheel of ten dele van een woning tot voorwerp
            hebben;
     2°     de handelingen moeten betrekking hebben op een woning die, na de uitvoering ervan, hetzij
            uitsluitend, hetzij hoofdzakelijk, als privé-woning wordt gebruikt;
     3°     de handelingen moeten worden verricht aan een woning waarvan de eerste ingebruikneming
            ten minste tien jaar voorafgaat aan het eerste tijdstip van opeisbaarheid van de btw dat zich
            voordoet overeenkomstig artikel 22, § 1 of artikel 22bis van het Wetboek;
     4°     de handelingen moeten worden verstrekt en gefactureerd aan een eindverbruiker;
     5°     de door de dienstverrichter uitgereikte factuur en het dubbel dat hij bewaart, moeten, op
            basis van een duidelijk en nauwkeurig attest van de afnemer, melding maken van het
            voorhanden zijn van de elementen die de toepassing van het verlaagd tarief rechtvaardigen;
            behalve in geval van samenspanning tussen de partijen of klaarblijkelijk niet naleven van
            onderhavige bepaling, ontlast het attest van de         afnemer de dienstverrichter van de
            aansprakelijkheid betreffende de vaststelling van het tarief.

     § 2.   Worden aangemerkt als eindverbruikers in de zin van deze bepaling, voor het werk in
     onroerende staat en de andere handelingen omschreven in § 3, met betrekking tot de woningen
     daadwerkelijk gebruikt voor de huisvesting van bejaarden, leerlingen en studenten, minderjarigen,
     thuislozen, personen in moeilijkheden, personen met een psychische stoornis, mentaal
     gehandicapten en psychiatrische patiënten, de publiekrechtelijke of privaatrechtelijke personen die
     beheren:
     1°     verblijfsinrichtingen voor bejaarden welke door de bevoegde overheid zijn erkend in het kader
            van de wetgeving inzake bejaardenzorg;
     2°     internaten die zijn toegevoegd aan scholen of universiteiten of die ervan afhangen;
     3°     jeugdbeschermingstehuizen en residentiële voorzieningen die op duurzame wijze, in dag- en
            nachtverblijf, minderjarigen huisvesten en die erkend zijn door de bevoegde overheid in het
            kader van de wetgeving op de jeugdbescherming of de bijzondere jeugdbijstand;
     4°     opvangtehuizen die in dag- en nachtverblijf thuislozen en personen in moeilijkheden
            huisvesten en die erkend zijn door de bevoegde overheid;
     5°     psychiatrische verzorgingstehuizen die op een duurzame wijze in dag- en nachtverblijf
            personen met een langdurige en gestabiliseerde psychische stoornis of mentaal gehandicapten
            huisvesten en die door de bevoegde overheid erkend zijn;
     6°     gebouwen waar, ten titel van een initiatief van beschut wonen erkend door de bevoegde
            overheid, het op een duurzame wijze huisvesten in dag- en nachtverblijf en het begeleiden
            van psychiatrische patiënten plaatsheeft.

     § 3.   Worden beoogd:
     1°     het verbouwen, het afwerken, het inrichten, het herstellen en het onderhouden, met
            uitsluiting van het reinigen, geheel of ten dele, van een uit zijn aard onroerend goed;
     2°     prestaties die erin bestaan een roerend goed te leveren en het meteen op zodanige wijze aan
            te brengen aan een onroerend goed dat het onroerend uit zijn aard wordt;
     3°     iedere handeling, ook indien niet beoogd in de bepaling onder 2°, die tot voorwerp heeft zowel
            de levering als de aanhechting aan een gebouw:
            a)     van de bestanddelen of een gedeelte van de bestanddelen van een installatie voor
                   centrale verwarming of airconditioning, daaronder begrepen de branders, de reservoirs
                   en de regel- en controletoestellen verbonden aan de ketel of aan de radiatoren;
            b)     van de bestanddelen of een gedeelte van de bestanddelen van een sanitaire installatie
                   van een gebouw en, meer algemeen, van al de vaste toestellen voor sanitair of
                   hygiënisch gebruik aangesloten op een waterleiding of een riool;

             c)     van de bestanddelen of een gedeelte van de bestanddelen van een elektrische
                    installatie van een gebouw, met uitzondering van toestellen voor de verlichting en van
                    lampen;
             d)     van de bestanddelen of een gedeelte van de bestanddelen van een elektrische
                    belinstallatie, van brandalarmtoestellen, van alarmtoestellen tegen diefstal en van een
                    huistelefoon;
             e)     van opbergkasten, gootstenen, gootsteenkasten en meubels met ingebouwde
                    gootsteen, wastafels en meubels met ingebouwde wasbak, zuigkappen, ventilators en
                    luchtverversers waarmee een keuken of een badkamer is uitgerust;
             f)     van luiken, rolluiken en rolgordijnen die aan de buitenkant van het gebouw worden
                    geplaatst;
      4°     iedere handeling, ook indien niet beoogd in de bepaling onder 2°, die tot voorwerp heeft zowel
             de levering van wandbekleding of vloerbekleding of -bedekking als de plaatsing ervan in een
             gebouw ongeacht of die bekleding of bedekking aan het gebouw wordt vastgehecht of
             eenvoudig ter plaatse op maat gesneden volgens de afmetingen van de te bedekken
             oppervlakte;
      5°     het aanhechten, het plaatsen, het herstellen en het onderhouden, met uitsluiting van het
             reinigen, van goederen bedoeld in de bepaling onder 3° en 4°;
      6°     de terbeschikkingstelling van personeel met het oog op het verrichten van de hierboven
             bedoelde handelingen.

      § 4.   Het verlaagd tarief is in geen geval van toepassing op:
      1°     werk in onroerende staat en andere onroerende handelingen, die geen betrekking hebben op
             de eigenlijke woning, zoals bebouwingswerkzaamheden, tuinaanleg en oprichten van
             afsluitingen;
      2°     werk in onroerende staat en andere onroerende handelingen, die tot voorwerp hebben de
             bestanddelen of een gedeelte van de bestanddelen van zwembaden, sauna’s,
             midgetgolfbanen, tennisterreinen en dergelijke installaties;
      3°     het gedeelte van de prijs met betrekking tot de levering van verwarmingsketels in
             appartementsgebouwen alsook op de levering van de bestanddelen of een gedeelte van de
             bestanddelen van liftinstallaties.

XXXIX. Kleine hersteldiensten

      (KB nr. 20, Tabel A, rubriek XXXIX, werd                      ingevoegd   met   ingang   van    01.07.2011
      (Art. 27, W 04.07.2011, B.S. 19.07.2011))

      1.     De herstelling van ﬁetsen.
      2.     De herstelling van schoeisel en lederwaren.
      3.     De herstelling en het vermaken van kleding en huishoudlinnen.

XL.   Gebouwen bestemd voor onderwijs en leerlingenbegeleiding

      (De tekst van KB nr. 20, Tabel A, rubriek XL, 4°, werd vervangen met ingang van
      01.01.2019   (Art.  12,   W  14.10.2018, B.S. 25.10.2018,  pg.  81448.  Erratum
      B.S. 30.11.2018, pg. 91362))

      Het verlaagd tarief van zes pct. is van toepassing op:
      1°     de leveringen van gebouwen, bestemd voor het school- of universitair onderwijs dat op grond
             van artikel 44, § 2, 4°, a), van het Wetboek is vrijgesteld, alsook de vestigingen,
             overdrachten en wederoverdrachten van zakelijke rechten op zulke goederen die niet
             overeenkomstig artikel 44, § 3, 1°, van het Wetboek van de belasting zijn vrijgesteld;
      2°     de levering van gebouwen bestemd voor de psycho-medisch-sociale centra en de centra voor
             leerlingenbegeleiding, die op grond van artikel 44, § 2, 2°, tweede lid, zesde streepje, van het
             Wetboek zijn vrijgesteld alsook de vestigingen, overdrachten en wederoverdrachten van
             zakelijke rechten op zulke goederen die niet overeenkomstig artikel 44, § 3, 1°, van het
             Wetboek van de belasting zijn vrijgesteld;
      3°     het werk in onroerende staat in de zin van artikel 19, § 2, tweede lid, van het Wetboek, met
             uitsluiting van de reiniging, en de andere handelingen bedoeld in rubriek XXXI, § 3, 3° tot 6°,
             met betrekking tot de onder 1° en 2° genoemde gebouwen;
      4°     de onroerende financieringshuur of onroerende leasing bedoeld in artikel 44, § 3, 2°, b), van
             het Wetboek en de onroerende verhuur bedoeld in artikel 44, § 3, 2°, d), van het Wetboek,
             die betrekking hebben op de onder 1° en 2° bedoelde gebouwen.

                                                  TABEL B

              Goederen en diensten onderworpen aan het tarief van 12 pct.

I.     Restaurant- en cateringdiensten

       (De tekst van KB nr. 20, Tabel B, I, werd hersteld met ingang van 01.01.2010 (Art. 4,
       KB   09.12.2009,  B.S.   14.12.2009,   bekrachtigd  bij   art.   14,  W   19.05.2010,
       B.S. 28.05.2010))

       Restaurant- en cateringdiensten, met uitsluiting van het verschaffen van dranken.

II.    (Opgeheven bij KB 29.12.1992)

III.   Fytofarmacie.

       De fytofarmaceutische produkten erkend door de Minister die de Landbouw onder zijn bevoegdheid
       heeft.

IV.    (opgeheven bij KB 24.06.1993)

V.     (opgeheven bij KB 24.06.1993)

VI.    Margarine

       Margarine

VII.   Banden en binnenbanden.

       Banden en binnenbanden voor wielen van landbouwmachines en -tractors, met uitsluiting van
       banden of binnenbanden voor bosbouwtractors en motoculteurs.
       Het voordeel van het verlaagd tarief van 12 pct. is afhankelijk van de afgifte door de verkrijger of
       invoerder, aan de leverancier of aan de douane, van een schriftelijke verklaring waarin hij zijn
       registratienummer voor de belasting over de toegevoegde waarde vermeldt en bevestigt dat hij
       landbouwondernemer is en dat hij de goederen werkelijk zal gebruiken voor de behoeften van zijn
       landbouwbedrijf.

VIII. Brandstoffen

       Steenkool en van steenkool vervaardigde vaste brandstoffen; bruinkool en geperste bruinkool, met
       uitzondering van git; cokes en halfcokes van steenkool, van bruinkool of van turf; niet-gecalcineerde
       petroleumcokes, als brandstof gebruikt.

IX.    Betaaltelevisie.

       (De tekst van KB nr. 20, Tabel B, IX, werd opgeheven met ingang van 01.01.2012 (Art.
       55,W 28.12.2011, B.S. 30.12.2011))

X.     Huisvesting in het kader van het sociaal beleid

       (De tekst van KB nr. 20, Tabel B, rubriek X, § 1, C), werd vervangen met ingang van
       01.01.2019   (Art.  13,   W  14.10.2018,  B.S.   25.10.2018,  pg.   81448.  Erratum
       B.S. 30.11.2018, pg. 91362))

       § 1.    Het verlaagd tarief van 12 pct., is van toepassing op:
       A)      de leveringen van nagenoemde goederen bedoeld in artikel 1, § 9, van het Wetboek alsook de
               vestigingen, overdrachten en wederoverdrachten van zakelijke rechten op zulke goederen die

             niet overeenkomstig artikel 44, § 3, 1°, van het Wetboek van de belasting zijn vrijgesteld,
             wanneer die goederen bestemd zijn voor de huisvesting in het kader van het sociaal beleid:
             a)     privé-woningen die worden geleverd en gefactureerd aan de provincies, de
                    intercommunales, de gemeenten, de intercommunale openbare centra voor
                    maatschappelijk welzijn, de openbare centra voor maatschappelijk welzijn en de
                    gemengde holdingmaatschappijen waarin de overheid een meerderheid heeft, en die
                    door deze instellingen of maatschappijen worden bestemd om […] te worden verhuurd;
             b)     privé-woningen die worden geleverd en gefactureerd aan de openbare centra voor
                    maatschappelijk welzijn en die door deze centra worden bestemd om […] te worden
                    verkocht;
             c)     privé-woningen die […] worden geleverd en gefactureerd door de openbare centra voor
                    maatschappelijk welzijn;
             d)     woningcomplexen bestemd om te worden gebruikt voor de huisvesting van bejaarden,
                    leerlingen en studenten, minderjarigen, thuislozen, personen in moeilijkheden,
                    personen met een psychische stoornis, mentaal gehandicapten en psychiatrische
                    patiënten en die worden geleverd en gefactureerd aan publiekrechtelijke of
                    privaatrechtelijke personen die beheren:
                    1°     verblijfsinrichtingen voor bejaarden welke door de bevoegde overheid zijn
                           erkend in het kader van de wetgeving inzake bejaardenzorg;
                    2°     internaten die zijn toegevoegd aan scholen of universiteiten of die ervan
                           afhangen;
                    3°     jeugdbeschermingstehuizen en residentiële voorzieningen die op duurzame
                           wijze, in dag- en nachtverblijf, minderjarigen huisvesten en die erkend zijn door
                           de bevoegde overheid in het kader van de wetgeving op de jeugdbescherming
                           of de bijzondere jeugdbijstand;
                    4°     opvangtehuizen die in dag- en nachtverblijf thuislozen en personen in
                           moeilijkheden huisvesten en die erkend zijn door de bevoegde overheid;
                    5°     psychiatrische verzorgingstehuizen die op een duurzame wijze in dag-en
                           nachtverbijf personen met een langdurige en gestabiliseerde psychische stoornis
                           of mentaal gehandicapten huisvesten en die door de bevoegde overheid erkend
                           zijn;
                    6°     gebouwen waar, ten titel van een initiatief van beschut wonen erkend door de
                           bevoegde overheid, het op een duurzame wijze huisvesten in dag- en
                           nachtverblijf en het begeleiden van psychiatrische patiënten plaatsheeft;
      B)     werk in onroerende staat in de zin van artikel 19, § 2, tweede lid, van het Wetboek, met
             uitsluiting van het reinigen, en de andere handelingen opgesomd in rubriek XXXI, § 3, 3° tot
             6°, van tabel A met betrekking tot de onder A genoemde privé-woningen en
             woningcomplexen mits die worden verstrekt en gefactureerd […] aan de onder A genoemde
             publiekrechtelijke en privaatrechtelijke personen;
      C)     de onroerende financieringshuur of onroerende leasing bedoeld in artikel 44, § 3, 2°, b), van
             het Wetboek en de onroerende verhuur, bedoeld in artikel 44, § 3, 2°, d), van het Wetboek,
             die betrekking hebben op de onder A bedoelde privéwoningen en woningcomplexen wanneer
             de afnemer een onder A genoemde publiekrechtelijke of privaatrechtelijke persoon is.

      § 2.   Het verlaagd tarief van 12 pct. is in geen geval van toepassing op:
      1°     werk in onroerende staat en de andere onroerende handelingen die geen betrekking hebben
             op de eigenlijke woning, zoals bebouwingswerkzaamheden, tuinaanleg en oprichten van
             afsluitingen;
      2°     werk in onroerende staat en andere onroerende handelingen die tot voorwerp hebben de
             bestanddelen of een gedeelte van de bestanddelen van zwembaden, sauna's, midget-
             golfbanen, tennisterreinen en dergelijke installaties.

XI.   Huisvesting in het kader van het sociaal beleid - Privé-initiatief

      (De tekst van KB nr. 20, Tabel B, rubriek XI, § 3, werd vervangen met ingang van
      01.01.2019 (Art. 14, W 14.10.2018, B.S. 25.10.2018, pg. 81448. Erratum 30.11.2018,
      pg. 91362))

      § 1.   Het verlaagd tarief van 12 %. is van toepassing op de leveringen van de nagenoemde
      goederen bedoeld in artikel 1, § 9, van het Wetboek, en op de vestigingen, overdrachten en
      wederoverdrachten van zakelijke rechten op zulke goederen, die niet overeenkomstig artikel 44, § 3,
      1°, van het Wetboek, van de belasting zijn vrijgesteld, wanneer die goederen bestemd zijn voor de
      huisvesting in het kader van het sociaal beleid:
      1°     de privéwoningen die worden verhuurd aan navolgende publiekrechtelijke of privaatrechtelijke
             rechtspersonen en die door hen worden bestemd om te worden verhuurd:

            a)     de provincies, de autonome            provinciebedrijven   en   de   provinciale   extern
                   verzelfstandigde agentschappen;
            b)     de intercommunales en andere intergemeentelijke samenwerkingsverbanden, de
                   gemeenten, de autonome gemeentebedrijven en de gemeentelijke extern
                   verzelfstandigde agentschappen;
            c)     de intercommunale openbare centra voor maatschappelijk welzijn en de openbare
                   centra voor maatschappelijk welzijn;
            d)     de gemengde holdingmaatschappijen waarin de overheid een meerderheid heeft;
            e)     de sociale verhuurkantoren;
            f)     de gewestelijke huisvestingsmaatschappijen en de door hen erkende maatschappijen
                   voor sociale huisvesting;
            g)     het Vlaams Woningfonds, het "Fonds du Logement des familles nombreuses de
                   Wallonie" en het Woningfonds van het Brusselse Hoofdstedelijk Gewest;
            h)     andere publiekrechtelijke en privaatrechtelijke rechtspersonen met sociaal oogmerk die
                   door de bevoegde overheid zijn erkend;
     2°     de woningcomplexen die worden verhuurd aan de personen bedoeld in rubriek X, § 1, A, punt
            d).
     Het voordeel van het verlaagd tarief is onderworpen aan de volgende voorwaarden:
     1°     degene die een privéwoning, een woningcomplex of een zakelijk recht hierop verkrijgt in
            omstandigheden waarbij de belasting opeisbaar wordt, moet:
            a)     vooraleer de belasting opeisbaar wordt overeenkomstig artikel 17 van het Wetboek, bij
                   het controlekantoor belast met de belasting over de toegevoegde waarde in het
                   ambtsgebied waar hij zijn woonplaats of maatschappelijke zetel heeft, een verklaring
                   indienen in de vorm bepaald door de minister van Financiën of zijn gemachtigde, dat in
                   het kader van het sociaal beleid deze privéwoning of dit woningcomplex bestemd is om
                   te worden verhuurd aan een in het eerste lid, bedoelde publiekrechtelijke of
                   privaatrechtelijke rechtspersoon; deze verklaring moet eveneens worden ondertekend
                   door laatstgenoemde;
            b)     aan de vervreemder een kopie van de verklaring bedoeld in de bepaling onder a)
                   overhandigen;
            c)     een voor eensluidend verklaard afschrift van het verhuurcontract gesloten met een in
                   het eerste lid, bedoelde publiekrechtelijke of privaatrechtelijke rechtspersoon
                   voorleggen bij het controlekantoor bedoeld in de bepaling onder a), binnen de maand
                   vanaf de ondertekening van het contract;
     2°     de door de vervreemder uitgereikte factuur en het dubbel dat hij moet bewaren moet de
            datum en het referentienummer vermelden van de verklaring alsook de aanduiding van het
            controlekantoor bedoeld in de bepaling onder 1°, a);
     3°     uiterlijk de laatste werkdag van de maand die volgt op de maand waarin de factuur met
            toepassing van het verlaagd tarief van 12 %. werd uitgereikt, moet de vervreemder een kopie
            van deze factuur toesturen naar het controlekantoor waaronder hij ressorteert.

     § 2.    Het verlaagd tarief van 12 %. is van toepassing op het werk in onroerende staat in de zin van
     artikel 19, § 2, tweede lid, van het Wetboek, met uitsluiting van het reinigen, en op de gelijkgestelde
     handelingen bedoeld in rubriek XXXI, § 3, 3° tot en met 6°, van tabel A, met betrekking tot de in
     paragraaf 1, eerste lid, bedoelde privéwoningen en woningcomplexen, wanneer zij na de uitvoering
     van de werken, bestemd zijn voor de huisvesting in het kader van het sociaal beleid.
     Het voordeel van het verlaagd tarief is onderworpen aan de volgende voorwaarden:
     1°     de bouwheer die een privéwoning of een woningcomplex opricht of laat oprichten of voor wie
            werken in onroerende staat worden verricht die tot voorwerp hebben de gehele of
            gedeeltelijke omvorming van een gebouw tot één of meer privéwoningen onder
            omstandigheden die de belasting opeisbaar maken, moet:
            a)     vooraleer de belasting opeisbaar wordt overeenkomstig artikel 22bis van het Wetboek,
                   bij het controlekantoor belast met de belasting over de toegevoegde waarde in het
                   ambtsgebied waar hij zijn woonplaats of maatschappelijke zetel heeft, een verklaring
                   indienen in de vorm bepaald door de minister van Financiën of zijn gemachtigde, dat in
                   het kader van het sociaal beleid deze privéwoning of dit woningcomplex bestemd is om
                   te worden verhuurd aan een in paragraaf 1, eerste lid, bedoelde publiekrechtelijke of
                   privaatrechtelijke rechtspersoon; deze verklaring moet eveneens worden ondertekend
                   door laatstgenoemde;
            b)     aan de dienstverrichter een kopie van de verklaring bedoeld in de bepaling onder a)
                   overhandigen;
            c)     een voor eensluidend verklaard afschrift van het verhuurcontract gesloten met een in
                   paragraaf 1, eerste lid, bedoelde publiekrechtelijke of privaatrechtelijke rechtspersoon,
                   voorleggen bij het controlekantoor bedoeld in de bepaling onder a), binnen de maand
                   vanaf de ondertekening van het contract;

     2°     de eigenaar of de hoofdhuurder van een privéwoning of een woningcomplex voor wie andere
            werken in onroerende staat dan bedoeld in de bepaling onder 1° worden verricht, is ertoe
            gehouden een voor eensluidend verklaard afschrift van het verhuurcontract dat in het kader
            van het sociaal beleid werd gesloten, te overhandigen aan de dienstverrichter;
     3°     in het geval bedoeld in de bepaling onder 1°, moet de dienstverrichter:
            a)     op de factuur die hij uitreikt en op het dubbel dat hij moet bewaren de datum en het
                   referentienummer vermelden van de verklaring en de aanduiding van het
                   controlekantoor, bedoeld in de bepaling onder 1°, a);
            b)     uiterlijk de laatste werkdag van de maand die volgt op de maand waarin de factuur
                   met toepassing van het verlaagd tarief van 12 %. werd uitgereikt, een kopie van deze
                   factuur toesturen naar het controlekantoor waaronder hij ressorteert;
     4°     in het geval bedoeld in de bepaling onder 2°, moet de dienstverrichter:
            a)     op de factuur die hij uitreikt en op het dubbel dat hij moet bewaren de datum
                   vermelden van het verhuurcontract en de aanduiding van het controlekantoor, bedoeld
                   in de bepaling onder 1°, a);
            b)     uiterlijk de laatste werkdag van de maand die volgt op de maand waarin de factuur
                   met toepassing van het verlaagd tarief van 12 %. werd uitgereikt, een kopie van deze
                   factuur toesturen naar het controlekantoor waaronder hij ressorteert.

     § 3.   Het verlaagd tarief van 12 % is van toepassing op de onroerende financieringshuur of
     onroerende leasing bedoeld in artikel 44, § 3, 2°, b), van het Wetboek en op de onroerende verhuur
     bedoeld in artikel 44, § 3, 2°, d), van het Wetboek, die betrekking hebben op de onder paragraaf 1,
     eerste lid, bedoelde privéwoningen en woningcomplexen, wanneer die bestemd zijn voor de
     huisvesting in het kader van het sociaal beleid.
     Het voordeel van het verlaagd tarief is onderworpen aan de volgende voorwaarden:
     1°     de persoon die een privéwoning of een woningcomplex in leasing of in huur neemt in
            omstandigheden waarbij de belasting opeisbaar wordt, moet:
            a)     vooraleer de belasting opeisbaar wordt, overeenkomstig artikel 22bis van het Wetboek,
                   bij het controlekantoor belast met de belasting over de toegevoegde waarde in het
                   ambtsgebied waar hij zijn woonplaats of maatschappelijke zetel heeft, een verklaring
                   indienen in de vorm bepaald door de minister van Financiën of zijn gemachtigde, dat in
                   het kader van het sociaal beleid deze privéwoning of dit woningcomplex bestemd is om
                   te worden verhuurd aan een in paragraaf 1, eerste lid, bedoelde publiekrechtelijke of
                   privaatrechtelijke rechtspersoon; deze verklaring moet eveneens worden ondertekend
                   door laatstgenoemde;
            b)     aan de leasinggever of de verhuurder een kopie van de verklaring bedoeld in de
                   bepaling onder a) overhandigen;
            c)     een voor eensluidend verklaard afschrift van het verhuurcontract gesloten met een in
                   paragraaf 1, eerste lid, bedoelde publiekrechtelijke of privaatrechtelijke rechtspersoon,
                   voorleggen bij het controlekantoor bedoeld in de bepaling onder a) binnen de maand
                   vanaf de ondertekening van het contract;
     2°     de door de leasinggever of de verhuurder uitgereikte factuur en het dubbel dat hij moet
            bewaren moet de datum en het referentienummer vermelden van de verklaring en de
            aanduiding van het controlekantoor bedoeld in de bepaling onder 1°, a);
     3°     uiterlijk de laatste werkdag van de maand die volgt op de maand waarin de factuur met
            toepassing van het verlaagd tarief van 12 % werd uitgereikt, moet de leasinggever of de
            verhuurder een kopie van deze factuur toesturen naar het controlekantoor waaronder hij
            ressorteert.

     § 4.    Het verlaagd tarief van 12 %. is van toepassing op de in paragraaf 1, eerste lid, paragraaf 2,
     eerste lid, en paragraaf 3, eerste lid, bedoelde handelingen, met betrekking tot privéwoningen en
     woningcomplexen die bestemd zijn voor de huisvesting in het kader van het sociaal beleid en die
     worden verhuurd in het kader van een beheersmandaat toegekend aan een in paragraaf 1, eerste
     lid, 1°, bedoelde publiekrechtelijke of privaatrechtelijke rechtspersoon.
     Het voordeel van het verlaagd tarief is onderworpen aan de volgende voorwaarden:
     1°     de verwerver, de bouwheer of leasingnemer moet:
            a)     vooraleer de belasting opeisbaar wordt, overeenkomstig de artikelen 17 of 22bis van
                   het Wetboek, bij het controlekantoor belast met de belasting over de toegevoegde
                   waarde in het ambtsgebied waar hij zijn woonplaats of maatschappelijke zetel heeft,
                   een verklaring indienen in de vorm bepaald door de minister van Financiën of zijn
                   gemachtigde, dat in het kader van het sociaal beleid deze privéwoning of dit
                   woningcomplex bestemd is om te worden verhuurd in het kader van een
                   beheersmandaat toegekend aan een in paragraaf 1, eerste lid, bedoelde
                   publiekrechtelijke of privaatrechtelijke rechtspersoon; deze verklaring moet eveneens
                   worden ondertekend door laatstgenoemde;

            b)     aan de vervreemder, dienstverrichter of leasinggever een kopie van de verklaring
                   bedoeld in de bepaling onder a) overhandigen;
            c)     een voor eensluidend verklaard afschrift van het verhuurcontract voorleggen bij het
                   controlekantoor bedoeld in de bepaling onder a) binnen de maand vanaf de
                   ondertekening van het contract;
     2°     de eigenaar voor wie andere werken in onroerende staat worden uitgevoerd dan bedoeld in
            paragraaf 2, tweede lid, 1°, moet een voor eensluidend verklaard afschrift van het
            verhuurcontract aan de dienstverrichter overhandigen;
     3°     al naargelang het geval moeten de voorwaarden bedoeld in paragraaf 1, tweede lid, 2° en 3°,
            paragraaf 2, tweede lid, 3° of 4°, of paragraaf 3, tweede lid, 2° en 3° eveneens vervuld zijn.

     § 5.   Voor zover de voorwaarden bedoeld in paragraaf 1, tweede lid, paragraaf 2, tweede lid, 1° en
     3°, paragraaf 3, tweede lid, en paragraaf 4, tweede lid, vervuld zijn, en behalve in geval van
     samenspanning tussen partijen of het klaarblijkelijk niet naleven van deze rubriek, ontlast de
     verklaring van de verwerver, de bouwheer of de leasingnemer de vervreemder, de dienstverrichter of
     de leasinggever van de aansprakelijkheid betreffende de vaststelling van het tarief.
     Voor zover de voorwaarden bedoeld in paragraaf 2, tweede lid, 2° en 4°, vervuld zijn, en behalve in
     geval van samenspanning tussen partijen of het klaarblijkelijk niet naleven van deze rubriek, ontlast
     het voor eensluidend verklaard afschrift van het verhuurcontract dat hem door de eigenaar werd
     overhandigd, de dienstverrichter van de aansprakelijkheid betreffende de vaststelling van het tarief.

     § 6.    Om het verlaagd tarief te kunnen genieten eindigt de voorziene verhuurtermijn ten vroegste
     op 31 december van het vijftiende jaar volgend op het jaar waarin de eerste ingebruikneming van de
     woning of het woningcomplex bedoeld in de paragrafen 1 tot 4 heeft plaats gevonden. In de gevallen
     bedoeld in de paragrafen 1 tot 3 wordt die minimum verhuurtermijn bij de aanvang van de
     verhuurovereenkomst vastgelegd en in het geval bedoeld in paragraaf 4 wordt die termijn vastgelegd
     bij de aanvang van het beheersmandaat.
     Indien zich tijdens de voormelde termijn wijzigingen voordoen waardoor de voorwaarden bedoeld in
     paragraaf 1, eerste lid, paragraaf 2, eerste lid, paragraaf 3, eerste lid, of paragraaf 4, eerste lid, niet
     meer zijn vervuld, moet:
     1°     enerzijds, de verwerver, de bouwheer, de eigenaar of de leasingnemer en, anderzijds, de
            hoofdhuurder of, in voorkomend geval, de beheerder en de huurder bij het controlekantoor
            belast met de belasting over de toegevoegde waarde in het ambtsgebied waar zij hun
            woonplaats of maatschappelijke zetel hebben hiervan binnen de maand die volgt op deze
            wijziging een verklaring indienen in de vorm bepaald door de minister van Financiën of zijn
            gemachtigde; deze verklaring moet eveneens door de betrokken partijen worden
            ondertekend;
     2°     de verwerver, de bouwheer, de eigenaar of de leasingnemer het belastingvoordeel dat hij
            heeft genoten, terugstorten aan de Staat voor het jaar waarin de wijziging zich voordoet en
            voor de nog te lopen jaren tot beloop van een vijftiende per jaar.

     § 7.   Het verlaagd tarief is in geen geval van toepassing op:
     1°     werk in onroerende staat en de andere onroerende handelingen die geen betrekking hebben
            op de eigenlijke woning, zoals bebouwingswerkzaamheden, tuinaanleg en oprichten van
            afsluitingen;
     2°     werk in onroerende staat en andere onroerende handelingen die tot voorwerp hebben de
            bestanddelen of een gedeelte van de bestanddelen van zwembaden, sauna's,
            midgetgolfbanen, tennisterreinen en dergelijke installaties.".

                                                 TABEL C

             Goederen en diensten onderworpen aan het tarief van 0 pct.
                         (Tabel C, werd ingevoegd met ingang van 01.04.2019,
                         (Art. 4, W 13.04.2019, B.S. 26.04.2019, pg. 40552))

I. Periodieke publicaties

      (De tekst van KB nr. 20, Bijlage, Tabel C, rubriek I, werd ingevoegd met ingang van
      01.04.2019 (Art. 4, W 13.04.2019, B.S. 26.04.2019, pg. 40552)

      § 1.    Het verlaagd tarief is van toepassing op de gedrukte periodieke publicaties die:
      1°      bestemd zijn voor het grote publiek, rekening houdend met de aard van de thema's en de
              manier waarop die worden behandeld;
      2°      niet uitsluitend of hoofdzakelijk bestaan uit reclamemateriaal;
      3°      die een coherent geheel omvatten van persartikels die:
              a)     auteursrechtelijk beschermd zijn;
              b)     werden geschreven en samengesteld onder de eindverantwoordelijkheid van een
                     professionele redactie die hoofdzakelijk is samengesteld uit journalisten, die:
                     -   gerechtigd zijn om de titel van beroepsjournalist te voeren bedoeld in de wet van
                         30 december 1963 betreffende de erkenning en de bescherming van de titel van
                         beroepsjournalist of die gerechtigd zijn om de titel van journalist van beroep te
                         voeren bedoeld in het koninklijk besluit van 12 april 1965 tot instelling van
                         identificatiedocumenten en -kentekens ten behoeve van de leden van de periodieke
                         pers voor gespecialiseerde informatie, als het Belgische periodieke publicaties
                         betreft;
                     -   geaccrediteerd zijn als    beroepsjournalisten, als    het buitenlandse        periodieke
                         publicaties betreft;
      4°      verschijnen:
              a)     zonder beperking in de duur;
              b)     bij regelmatige, vooraf bepaalde tussenpozen;
              c)     minimaal achtenveertig keer per jaar;
              d)     onder een gemeenschappelijke benaming;
              e)     met de duidelijke kenmerken van hun periodiciteit.

      § 2.   Het verlaagd tarief is niet van toepassing op de volgende categorieën gedrukte periodieke
      publicaties:
      1°      de publicaties die in hoofdzaak een volledige roman, verhaal of werk van welke aard ook of
              afleveringen van dergelijke werken bevatten, hetzij in de vorm van een al of niet verluchte
              tekst, hetzij in de vorm van een beeldverhaal met al of niet in- of ondergeschreven korte
              tekst;
      2°      de in afleveringen uitgegeven boeken, waarvan de verschijning een beperkte tijdruimte
              beslaat of die een bijvoegsel of een bijwerking vormen van reeds verschenen werken;
      3°      de advertentiebladen, prospectussen, catalogussen, almanakken, prijscouranten, koerslijsten,
              scheepsberichten, notariële berichten, dienstregelingen;
      4°      de gespecialiseerde publicaties voor professioneel gebruik;
      5°      de publicaties die enkel denkspellen bevatten;
      6°      de publicaties die onder de naam van een industriële, financiële, commerciële of andere
              onderneming worden uitgegeven, zelfs indien ze uitsluitend teksten of illustraties van
              algemeen belang bevatten zonder rechtstreekse reclame;
      7°      de publicaties die als voornaamste doel hebben het opzoeken, in stand houden en uitbreiden
              van overeenkomsten ten voordele van industriële, financiële, commerciële of andere
              ondernemingen en die voor ondernemingen slechts een publiciteitsmiddel zijn;
      8°      de publicaties die het voorwerp uitmaken van een levering, een intracommunautaire
              verwerving of een invoer na het verstrijken van de termijn van één jaar vanaf de datum van
              verschijning;
      9°      de publicaties die verenigd zijn in volledige of onvolledige verzamelingen, in één band, of in al
              dan niet periodieke albums;
      10°     de publicaties die uitsluitend of hoofdzakelijk bestaan uit video-inhoud of beluisterbare
              muziek;
      11°     de publicaties die als oud papier of karton worden verkocht.

     § 3.   Het verlaagd tarief is van toepassing op digitale publicaties die:
     1°     beantwoorden aan de voorwaarden bedoeld in paragraaf 1, 1° tot 3°;
     2°     beantwoorden aan de voorwaarde bedoeld in paragraaf 1, 4°, of die geregeld en voldoende
            worden bijgewerkt en geactualiseerd, inzonderheid door het toevoegen van nieuwe
            persartikels.

     § 4.   Het verlaagd tarief is niet van toepassing op digitale publicaties bedoeld in paragraaf 2, 1°
     tot 10°.

   Overzicht van de nog geldende verlaagde tarieven (officieuze toevoeging)
     Tabel A – Goederen en diensten onderworpen aan het tarief van 6 pct.
        Goederen aan 6 pct.
           I.          Levende dieren.
           II.         Vlees en slachtafvallen.
           III.        Vis, schaal-, schelp- en weekdieren.
           IV.         Melk en zuivelprodukten; eieren; honig.
           V.          Groenten, planten, wortels en knollen, voor voedingsdoeleinden.
           VI.         Fruit; schillen van citrusvruchten en van meloenen.
           VII.        Plantaardige produkten.
           VIII.       Produkten van de meelindustrie; mout; zetmeel.
           IX.         Vetten en oliën.
           X.          Andere voedingsmiddelen.
           XII.        Voedsel voor dieren; meststoffen; dierlijke produkten.
           XIII.       Waterdistributie.
           XVII.       Geneesmiddelen en medische hulpmiddelen.
           XIX.        Kranten, tijdschriften en boeken.
           XXI.        Kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten.
           XXII.       Automobielen     voor   personenvervoer    voor   invaliden.          Onderdelen,
                       uitrustingsstukken en toebehoren voor deze voertuigen.
           XXIII.      Diversen.
           XXIIIbis.   Leveringen van goederen door instellingen met sociaal oogmerk.

        Diensten aan 6 pct.
          XXIV.        Landbouwdiensten.
          XXV.         Vervoer.
          XXVI.        Onderhoud en herstelling.
          XXVIII.      Inrichtingen voor cultuur, sport of vermaak.
          XXIX.        Auteursrechten; uitvoeren van concerten en voorstellingen.
          XXX.         Hotels, camping.
          XXXI.        Werk in onroerende staat met betrekking tot privé-woningen.
          XXXII.       Privé-woningen voor gehandicapten.
          XXXIII.      Instellingen voor gehandicapten.
          XXXIV.       Diversen.
          XXXV.        Diensten verricht door instellingen met sociaal oogmerk.
          XXXVI.       Huisvesting in het kader van het sociaal beleid.
          XXXVII.      Afbraak en heropbouw van gebouwen in stadsgebieden.
          XXXVIII.     Renovatie en herstel van privéwoningen.
          XXXIX.       Kleine hersteldiensten.
          XL.          Gebouwen bestemd voor onderwijs en leerlingenbegeleiding.

     Tabel B – Goederen en diensten onderworpen aan het tarief van 12 pct.
          I.           Restaurant- en cateringdiensten.
          III.         Fytofarmacie.
          VI.          Margarine.
          VII.         Banden en binnenbanden.
          VIII.        Brandstoffen.
          X.           Huisvesting in het kader van het sociaal beleid.
          XI.          Huisvesting in het kader van het sociaal beleid - Privé-initiatief.

     Tabel C – Goederen en diensten onderworpen aan het tarief van 0 pct.
          I.           Periodieke publicaties.

Bijlage A
Lijst van de bijwerkingen

    Bijwerking                                           Vervangen pagina’s

Bijw. 01 / 01.01.2012   - Volledige uitgave

Bijw. 02 / 08.05.2013   - pg. I/1                                    - Bijw. 02 - pg. I/1
                        - pg. III/2                                  - Bijw. 02 - pg. III/2
                        - pg. III/6 en III/7                         - Bijw. 02 - pg. III/6 en III/7
                        - pg. Bijw./1                                - Bijw. 02 - pg. Bijl.A/1
                        - nihil                                      - Bijw. 02 - pg. Bijl.B/1

Bijw. 03 / 31.12.2013   - pg. I/1                                    - Bijw. 03 - pg. I/1
                        - pg. III/3 t.e.m. III/9                     - Bijw. 03 - pg. III/3 t.e.m. III/9
                        - pg. Bijl.A/1                               - Bijw. 03 - pg. Bijl.A/1
                        - pg. Bijl.B/1                               - Bijw. 03 - pg. Bijl.B/1

Bijw. 04 / 27.03.2014   - pg. I/1                                    - Bijw. 04 - pg. I/1
                        - pg. Bijl.A/1                               - Bijw. 04 - pg. Bijl.A/1
                        - pg. Bijl.B/1                               - Bijw. 04 - pg. Bijl.B/1

Bijw. 05 / 31.08.2015   - pg. I/1 t.e.m. I/3                         - Bijw. 05 - pg. I/1 t.e.m. I/4
                        - pg. Bijl.A/1                               - Bijw. 05 - pg. Bijl.A/1
                        - pg. Bijl.B/1                               - Bijw. 05 - pg. Bijl.B/1

Bijw. 06 / 15.12.2015   - pg. I/1                                    - Bijw. 06 - pg. I/1
                        - pg. III/9                                  - Bijw. 06 - pg. III/9
                        - pg. V/1                                    - Bijw. 06 - pg. V/1
                        - pg. Bijl.A/1                               - Bijw. 06 - pg. Bijl.A/1
                        - pg. Bijl.B/1                               - Bijw. 06 - pg. Bijl.B/1

Bijw. 07 / 02.02.2016   - pg. I/1                                    - Bijw. 07 - pg. I/1
                        - pg. II/7 en II/8                           - Bijw. 07 - pg. II/7 en II/8
                        - pg. III/5                                  - Bijw. 07 - pg. III/5
                        - pg. III/8 en III/9                         - Bijw. 07 - pg. III/8 en III/9
                        - pg. Bijl.A/1                               - Bijw. 07 - pg. Bijl.A/1
                        - pg. Bijl.B/1                               - Bijw. 07 - pg. Bijl.B/1 en Bijl.B/2

Bijw. 08 / 07.07.2016   - pg. I/1                                    - Bijw. 08 - pg. I/1
                        - pg. Bijl.A/1                               - Bijw. 08 - pg. Bijl.A/1
                        - pg. Bijl.B/1 en Bijl.B/2                   - Bijw. 08 - pg. Bijl.B/1 en Bijl.B/2

Bijw. 09 / 19.08.2016   - pg. I/1                                    - Bijw. 09 - pg. I/1
                        - pg. III/9                                  - Bijw. 09 - pg. III/9
                        - pg. Bijl.A/1                               - Bijw. 09 - pg. Bijl.A/1
                        - pg. Bijl.B/1 en Bijl.B/2                   - Bijw. 09 - pg. Bijl.B/1 en Bijl.B/2

Bijw. 10 / 31.08.2016   - pg. I/1                                    - Bijw. 10 - pg. I/1
                        - pg. III/9                                  - Bijw. 10 - pg. III/9
                        - pg. V/1                                    - Bijw. 10 - pg. V/1
                        - pg. Bijl.A/1                               - Bijw. 10 - pg. Bijl.A/1
                        - pg. Bijl.B/1 en Bijl.B/2                   - Bijw. 10 - pg. Bijl.B/1 en Bijl.B/2

Bijw. 11 / 29.12.2016   - pg. I/1                                    - Bijw. 11 - pg. I/1
                        - pg. IV/2                                   - Bijw. 11 - pg. IV/2 t.e.m. IV/5
                        - pg. V/1                                    - Bijw. 11 - pg. V/1
                        - nihil                                      - Bijw. 11 - pg. Bijl.A/2
                        - pg. Bijl.B/1 en Bijl.B/2                   - Bijw. 11 - pg. Bijl.B/1 en Bijl.B/2

Bijw. 12 / 10.11.2017   - pg. I/1                                    - Bijw. 12 - pg. I/1
                        - pg. II/7                                   - Bijw. 12 - pg. II/7
                        - pg. III/5                                  - Bijw. 12 - pg. III/5
                        - pg. III/8 en III/9                         - Bijw. 12 - pg. III/8 en III/9
                        - pg. Bijl.A/2                               - Bijw. 12 - pg. Bijl.A/2
                        - pg. Bijl.B/1 en Bijl.B/2                   - Bijw. 12 - pg. Bijl.B/1 en Bijl.B/2

Bijw. 13 / 22.12.2017   - pg. I/1                                    - Bijw. 13 - pg. I/1
                        - pg. II/7                                   - Bijw. 13 - pg. II/7
                        - pg. III/1                                  - Bijw. 13 - pg. III/1
                        - pg. III/5                                  - Bijw. 13 - pg. III/5
                        - pg. Bijl.A/2                               - Bijw. 13 - pg. Bijl.A/2
                        - pg. Bijl.B/1 en Bijl.B/2                   - Bijw. 13 - pg. Bijl.B/1 t.e.m. Bijl.B/3

Bijw. 14 / 25.10.2018   - pg. I/1                                    - Bijw. 14 - pg. I/1
                        - pg. III/3 en III/4                         - Bijw. 14 - pg. III/3 en III/4
                        - pg. III/6 en III/7                         - Bijw. 14 - pg. III/6 en III/7
                        - pg. III/9                                  - Bijw. 14 - pg. III/9
                        - pg. IV/1 t.e.m. IV/5                       - Bijw. 14 - pg. IV/1 t.e.m. IV/5
                        - pg. Bijl.A/2                               - Bijw. 14 - pg. Bijl.A/2
                        - pg. Bijl.B/1 en Bijl.B/2                   - Bijw. 14 - pg. Bijl.B/1 t.e.m. Bijl.B/3

Bijw. 15 / 14.03.2019   - pg. I/1                                    - Bijw. 15 - pg. I/1
                        - pg. II/1 en II/2                           - Bijw. 15 - pg. II/1 en II/2
                        - pg. Bijl.A/2                               - Bijw. 15 - pg. Bijl.A/2
                        - pg. Bijl.B/1 t.e.m. Bijl.B/3               - Bijw. 15 - pg. Bijl.B/1 t.e.m. Bijl.B/3

Bijw. 16 / 26.06.2019   - Volledige uitgave

Bijw. 17 / 13.09.2019   - pg. I/1 t.e.m. I/4                         - Bijw. 17 - pg. I/1 t.e.m. I/4
                        - pg. Bijl.A/2                               - Bijw. 17 - pg. Bijl.A/2
                        - pg. Bijl.B/1 t.e.m. Bijl.B/3               - Bijw. 17 - pg. Bijl.B/1 t.e.m. Bijl.B/4

Bijlage B
Recente wijzigingen

De historische versies kunnen geraadpleegd worden op www.fisconetplus.be

*   KB van 29.08.2019 - Koninklijk besluit tot aanpassing van sommige federale fiscale bepalingen aan het
    Wetboek van vennootschappen en verenigingen en aan het koninklijk besluit van 29 april 2019 tot
    uitvoering van het Wetboek van vennootschappen en verenigingen en houdende diverse bepalingen
    (B.S. 13.09.2019, pg. 86195)
         Wijzigt met ingang van 01.05.2019:

              -   Bijlage, tabel A, rubriek XXXII (§ 1, 1°, c en 3°, gewijzigd)

*   Wet van 06.06.2019 - Wet tot wijziging van koninklijk besluit nr. 20 van 20 juli 1970 tot vaststelling
    van de tarieven van de belasting over de toegevoegde waarde en tot indeling van de goederen en de
    diensten bij die tarieven (B.S. 26.06.2019, pg. 65569)
         De inwerkingtreding van deze wet is onderworpen aan de instemming van de Europese
         Unie met een wijziging van bijlage III van de btw-Richtlijn 2006/112/EG aangaande de beoogde
         dienst en beoogt de wijziging van:

              -   Bijlage, tabel A, rubriek XXXIV (de bepaling onder 4°, wordt hersteld met een
                  andere inhoud – Voorwaardelijk toekomstig recht)

*   Wet van 02.05.2019 - Wet houdende diverse bepalingen inzake belasting over de toegevoegde waarde
    en tot wijziging van de belastingvermindering voor giften (B.S. 15.05.2019, pg. 46586)
         Wijzigt met ingang van 25.05.2019:

              -   Bijlage, tabel A, rubriek XXII (afdeling 1, § 5, 4° lid, vervangen)

*   Wet van 13.04.2019 - Wet tot instelling van een verlaagd btw-tarief bij de aankoop van fietsen en
    elektrische fietsen (B.S. 29.04.2019 pg. 41032)
         De inwerkingtreding van deze wet is onderworpen aan de instemming van de Europese
         Unie met een wijziging van bijlage III van de btw-Richtlijn 2006/112/EG aangaande de beoogde
         goederen en beoogt de wijziging van:

              -   Bijlage, tabel A, rubriek XXIII        (het cijfer 12, wordt ingevoegd – Voorwaardelijk
                  toekomstig recht)

*   Wet van 13.04.2019 - Wet tot wijziging van het koninklijk besluit nr. 20 van 20 juli 1970 tot
    vaststelling van de tarieven van de belasting over de toegevoegde waarde en tot indeling van de
    goederen en de diensten bij die tarieven wat bepaalde publicaties betreft (B.S. 26.04.2019, pg. 40552)
         Wijzigt met ingang van 01.04.2019:

              -   art. 1 (tweede lid, c), ingevoegd )
              -   Bijlage, tabel A, rubriek XIX (volledige rubriek vervangen)
         en voegt, met ingang van 01.04.2019, de nieuwe tabel C “Goederen en diensten onderworpen
         aan het tarief van 0 pct.” in:

              -   Bijlage, tabel C, rubriek I ( nieuwe rubriek ingevoegd in de nieuwe tabel C)

*   Wet van 27.02.2019 - Wet tot wijziging van het koninklijk besluit nr. 20 van 20 juli 1970 tot
    vaststelling van de tarieven van de belasting over de toegevoegde waarde en tot indeling van de
    goederen en de diensten bij die tarieven wat betreft het btw-tarief voor de levering van planten en
    bloemen bij tuinaanleg en -onderhoud (B.S. 14.03.2019, pg. 26797)
         Wijzigt met ingang van 01.04.2019:

              -   Bijlage, tabel A, rubriek VII (bepalingen 13. en 14., vervangen)

*   Wet van 14.10.2018 - Wet tot wijziging van het Wetboek van de belasting over de toegevoegde waarde
    wat de optionele belastingheffing inzake verhuur van uit hun aard onroerende goederen betreft en tot
    wijziging van het koninklijk besluit nr. 20, van 20 juli 1970, tot vaststelling van de tarieven van de
    belasting over de toegevoegde waarde en tot indeling van de goederen en de diensten bij die tarieven
    wat het verlaagde btw-tarief inzake de belaste verhuur van uit hun aard onroerende goederen betreft
    (B.S. 25.10.2018, pg. 81448)
         Wijzigt met ingang van 01.01.2019:

              -   Bijlage, tabel A, rubriek XXXII (§ 4, vervangen)
              -   Bijlage, tabel A, rubriek XXXIII (§ 4, vervangen)
              -   Bijlage, tabel A, rubriek XXXVI (§ 1, 3°, vervangen)
              -   Bijlage, tabel A, rubriek XL (4°, vervangen)
              -   Bijlage, tabel B, rubriek X (§ 1, C), vervangen)
              -   Bijlage, tabel B, rubriek XI (§ 3, vervangen)

*   KB van 10.12.2017 - Koninklijk besluit tot wijziging van het koninklijk besluit nr. 20 van 20 juli 1970
    tot vaststelling van de tarieven van de belasting over de toegevoegde waarde en tot indeling van de
    goederen en de diensten bij die tarieven wat bepaalde producten bestemd voor de intieme hygiënische
    bescherming en de externe defibrillatoren betreft (B.S. 22.12.2017, pg. 114228)
         Wijzigt met ingang van 01.01.2018:

              -   Bijlage, tabel A, rubriek XXIII (2°, gewijzigd; rubriek aangevuld met de cijfers 10 en
                  11)
              -   Bijlage, tabel A, rubriek XXVI (eerste lid, gewijzigd)
              -   Bijlage, tabel A, rubriek XXXIV (cijfer 1, gewijzigd)

*   Wet van 22.10.2017 – Wet houdende diverse fiscale bepalingen I (B.S. 10.11.2017, pg. 98213)
         Bekrachtigt (art. 16, 1°) met ingang van 12.02.2016 de wijzigingen van de Bijlage, Tabel A,
         rubrieken XXIII; XXXIV en XXXVIII, bij het KB 26.01.2016
         Bekrachtigt (art. 16, 2°) met ingang van 01.01.2016 de wijzigingen van de Bijlage, Tabel A,
         rubriek XL, bij het KB 03.08.2016

*   Wet van 25.12.2016 – Programmawet (B.S. 29.12.2016, pg. 90879)
         Wijzigt met ingang van 01.01.2017:

              -   Bijlage, tabel B, rubriek XI. Huisvesting in het kader van het sociaal beleid -
                  Privé-initiatief (nieuwe rubriek toegevoegd)

*   KB van 03.08.2016 – Erratum (B.S. 21.09.2016, pg. 63849)
         Verbetert:

              -   Enkel de tekst van het advies van de Raad van State, niet het KB zelf

*   KB van 03.08.2016 – Errata (B.S. 31.08.2016, pg. 59029)
         Verbetert:

              -   Bijlage, tabel A, rubriek XL (4°, erratum Nederlandse tekst)

*   KB van 03.08.2016 - Koninklijk besluit tot wijziging van het koninklijk besluit nr. 20 van 20 juli 1970
    tot vaststelling van de tarieven van de belasting over de toegevoegde waarde en tot indeling van de
    goederen en de diensten bij die tarieven wat de gebouwen voor leerlingenbegeleiding betreft (B.S.
    19.08.2016 – Ed. 2, pg. 52546. Bekrachtigt bij W 22.10.2017, B.S. 10.11.2017, pg. 98213)
         Wijzigt met ingang van 01.01.2016:

              -   Bijlage, tabel A, rubriek XL (rubriek vervangen)

*   Wet van 27.06.2016 - Wet tot wijziging van het Wetboek van de belasting over de toegevoegde waarde
    (B.S. 07.07.2016, pg. 42305)
         Bekrachtigt met ingang van 01.09.2015 de wijzigingen van KB nr. 20 bij het KB 23.08.2015

*   KB van 26.01.2016 - Koninklijk besluit tot wijziging van het koninklijk besluit nr. 20 van 20 juli 1970
    tot vaststelling van de tarieven van de belasting over de toegevoegde waarde en tot indeling van de
    goederen en de diensten bij die tarieven, wat het werk in onroerende staat en de gelijkgestelde
    handelingen en de assistentiehonden betreft (B.S. 02.02.2016, pg. 7596. Bekrachtigt bij W 22.10.2017,
    B.S. 10.11.2017, pg. 98213)
         Wijzigt met ingang van 12.02.2016:

              -   Bijlage, tabel A, rubriek XXIII (9°, ingevoegd)
              -   Bijlage, tabel A, rubriek XXXIV (3°, hersteld)
              -   Bijlage, tabel A, rubriek XXXVIII (§ 1, 3°, gewijzigd)

*   Wet van 26.12.2015 - Wet houdende maatregelen inzake versterking van jobcreatie en koopkracht
    (B.S. 30.12.2015, Ed. 2, pg. 80648)
         Wijzigt met ingang van 01.01.2016:

              -   Bijlage, tabel A, rubriek XL (invoering rubriek bij KB 14.12.2015 bekrachtigd)

*   KB van 14.12.2015 - Koninklijk besluit tot wijziging van het koninklijk besluit nr. 20 van 20 juli 1970
    tot vaststelling van de tarieven van de belasting over de toegevoegde waarde en tot indeling van de
    goederen en de diensten bij die tarieven (B.S. 15.12.2015, Ed. 2, pg. 74130)
         Wijzigt met ingang van 01.01.2016:

              -   Bijlage, tabel A, rubriek XL (nieuwe rubriek ingevoegd)

*   KB van 23.08.2015 - Koninklijk besluit tot wijziging van het koninklijk besluit nr. 20 van 20 juli 1970
    tot vaststelling van de tarieven van de belasting over de toegevoegde waarde en tot indeling van de
    goederen en de diensten bij die tarieven (B.S. 31.08.2015, pg. 55460. Bekrachtigd bij W 27.06.2016
    (B.S. 07.07.2016, pg. 42305)
         Wijzigt met ingang van 01.09.2015:

              -   art. 1bis (§ 1, gewijzigd en § 3, ingevoegd)

*   KB van 21.03.2014 - Koninklijk besluit tot wijziging van de koninklijke besluiten nrs. 4 en 20 met
    betrekking tot de belasting over de toegevoegde waarde (B.S. 27.03.2014, Ed. 2, pg.. 26734)
         Wijzigt met ingang van 01.04.2014:

              -   art. 1bis (het voorheen opgeheven artikel werd hersteld)

*   KB van 21.12.2013 - Koninklijk besluit tot wijziging van het koninklijk besluit nr. 20 van 20 juli 1970
    tot vaststelling van de tarieven van de belasting over de toegevoegde waarde en tot indeling van de
    goederen en de diensten bij die tarieven (B.S. 31.12.2013, pg. 103757)
         Wijzigt met ingang van 01.01.2014:

              -   Bijlage, tabel A, rubriek XXXII (§ 1, 1° en 3°, vervangen)
              -   Bijlage, tabel A, rubriek XXXIII (§ 1, 2°, vervangen)
              -   Bijlage, tabel A, rubriek XXXVI (§ 1, vervangen)

*   KB van 30.04.2013 - Koninklijk besluit tot wijziging van de koninklijke besluiten nrs. 1, 2, 3, 4, 7, 10,
    13, 14, 18, 19, 20, 22, 23, 24, 31, 39, 46, 48, 51, 53, 54 en 56 met betrekking tot de belasting over
    de toegevoegde waarde (B.S. 08.05.2013)
         Wijzigt met ingang van 01.01.2013:

              -   Bijlage, tabel A, rubriek XXII (gewijzigd) [enkel de Franse tekst]
              -   Bijlage, tabel A, rubriek XXVI (gewijzigd) [enkel de Franse tekst]
              -   Bijlage, tabel A, rubriek XXXI (gewijzigd)
              -   Bijlage, tabel A, rubriek XXXII (gewijzigd) [enkel de Franse tekst]

            -   Bijlage, tabel A, rubriek XXXIII (gewijzigd) [enkel de Franse tekst]
            -   Bijlage, tabel A, rubriek XXXVII (gewijzigd)
            -   Bijlage, tabel A, rubriek XXXVIII (gewijzigd)
