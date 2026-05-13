---
tags: ["VI.B", "2.4"]
itaa-lex-sectie: "VI.B"
wet: "K.B. nr. 39 van 17 oktober 1980, tot regeling van de toepassingsmodaliteiten van artikel 93duodecies van het Wetboek van de belasting over de toegevoegde waarde"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "17.10.1980"
bron: "Afgesplitst uit Fisconet-compilatie (pdftotext_compilatie_btw)"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/btw-kbs/WBTW-KB-compilatie.pdf
      sha256: 5f1bad7278d1f8e1f5c00efb5d792f61342d3f7a14a7950caca2937924bfa91c
      version: 06.03.2020
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 4126295-dirty
    model:
    prompt_version:
  generated_at: '2026-05-13T11:20:58Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-13T11:21:10Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Bestand bevat een opgeheven KB. Inhoudelijk OK maar voetnoot (1) wordt mid-tekst geïnjecteerd tussen Art. 3 en het tweede deel van Art. 3 (regels 73-79): 'Art. 138... 1°... 5°... 6°... ## Art. 139: De Koning kan...' - die '## Art. 139' is een PDF-doorkruising van een footnote met de werkelijke heading-structuur. Daarna gaat de Art. 3 tekst verder met 'Er moet evenwel een nieuw attest...'. Dit is een duidelijke kolom-/footnote-bleed."
    layer1:
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T11:21:10Z'
      rationale: "Bestand bevat een opgeheven KB. Inhoudelijk OK maar voetnoot (1) wordt mid-tekst geïnjecteerd tussen Art. 3 en het tweede deel van Art. 3 (regels 73-79): 'Art. 138... 1°... 5°... 6°... ## Art. 139: De Koning kan...' - die '## Art. 139' is een PDF-doorkruising van een footnote met de werkelijke heading-structuur. Daarna gaat de Art. 3 tekst verder met 'Er moet evenwel een nieuw attest...'. Dit is een duidelijke kolom-/footnote-bleed."
      concrete_problemen:
        - "Footnote (1) doorkruist Art. 3 inhoudelijk (regels 73-79); 'Art. 138' en 'Art. 139' opgenomen als footnote-residu maar 'Art. 139' krijgt zelfs een ## heading (regel 77) wat niet klopt"
        - Footnote-content '1°', '5°', '6°' staat dus als sublist binnen footnote - schadelijk voor retrieval want lijkt op een artikel-lijst
        - Het echte Art. 3-vervolg ('Er moet evenwel een nieuw attest...') komt pas op regel 79, ná de footnote-injection
---

# K.B. nr. 39 van 17 oktober 1980, tot regeling van de toepassingsmodaliteiten van artikel 93duodecies van het Wetboek van de belasting over de toegevoegde waarde

*Bijgewerkt tot en met 17.10.1980 — gecoördineerde versie.*

Koninklijk besluit nr. 39, van 17 oktober 1980, tot regeling van de toepassingsmodaliteiten van artikel 93duodecies van het Wetboek van de belasting over de toegevoegde waarde.

(Uitvoering van artikel 93duodecies van het Wetboek)

Officieuze coördinatie

Opgeheven met ingang van 01.01.2020 (Art. 135, W 13.04.2019 B.S. 30.04.2019, pg. 41412) (1)

Dit koninklijk besluit nr. 39 werd opgeheven met ingang van 01.01.2020

## Art. 1
(De tekst van KB nr. 39, artikel 1 is van toepassing met ingang van 01.04.2007. (Art. 21, KB 17.05.2007, B.S. 31.05.2007))

De ambtenaar bedoeld in artikel 93duodecies van het Wetboek is het hoofd van het ontvangkantoor van de belasting over de toegevoegde waarde waaronder de begunstigde ressorteert aan wie een in dat artikel bedoeld krediet, lening of voorschot wordt toegekend.

## Art. 2
(De tekst van KB nr. 39, artikel 2 is van toepassing met ingang van 01.04.2007. (Art. 21, KB 17.05.2007, B.S. 31.05.2007))

Het attest bedoeld in artikel 93duodecies van het Wetboek wordt uitgereikt nadat door de begunstigde een aanvraag in drie exemplaren is ingediend. De aanvraag en het attest worden gesteld op een formulier waarvan het model wordt vastgesteld door de directeur-generaal van de Administratie van de belasting over de toegevoegde waarde, registratie en domeinen. Het attest wordt uitgereikt binnen acht dagen na de indiening van de aanvraag.

## Art. 3
(De tekst van KB nr. 39, artikel 3 is van toepassing met ingang van 01.11.1980 (KB 17.10.1980))

Per krediet, lening of voorschot, waarvoor een voordeel inzake economische expansie is aangevraagd, moeten de kredietinstellingen en -organismen bedoeld in artikel 93duodecies van het Wetboek, in principe, in het bezit zijn van slechts één attest.

De datum van uitreiking van dat attest mag niet vroeger zijn dan één maand voor de datum van de aanvraag tot verkrijging van het voordeel, noch later dan deze datum.

(1) Art. 138: Deze wet is niet van toepassing:
1° op het administratieve dwangbevel inzake belasting over de toegevoegde waarde dat ter kennis werd gebracht of werd betekend voor de datum van haar inwerkingtreding;
5° op fiscale en niet-fiscale schuldvorderingen opgenomen in een kohier, een bijzonder kohier of een inningsen invorderingsregister, uitvoerbaar verklaard voor de datum van haar inwerkingtreding;
6° op fiscale en niet-fiscale schuldvorderingen, andere dan deze waarvan de inning en de invordering verzekerd zijn in toepassing van de wet van 21 februari 2003 tot oprichting van een Dienst voor alimentatievorderingen bij de FOD Financiën, die het voorwerp hebben uitgemaakt van een in kracht van gewijsde getreden rechterlijke beslissing houdende veroordeling tot hun betaling, voor de datum van haar inwerkingtreding.
## Art. 139: De Koning kan voor iedere categorie van schuldvordering een vroegere datum van inwerkingtreding bepalen

Er moet evenwel een nieuw attest worden overgelegd wanneer de beslissing tot toekenning van het voordeel niet is genomen binnen zes maanden te rekenen van de datum van het attest.

## Art. 4
(De tekst van KB nr. 39, artikel 4, tweede lid, werd gewijzigd met ingang van 01.01.2013.
(Art. 41, KB 30.04.2013, B.S. 08.05.2013, pg. 26764))

Een exemplaar van het attest bedoeld in artikel 93duodecies van het Wetboek wordt door de in artikel 1 van dit besluit aangewezen ambtenaar gezonden aan de overheid vermeld in de aanvraag van het attest.
Wanneer uit het attest blijkt dat een bedrag als belastingen of toebehoren opeisbaar is in hoofde van de begunstigde die een voordeel inzake economische expansie heeft aangevraagd, bepaalt de beslissing tot toekenning van het voordeel dat de kredietinstelling of het kredietorganisme de fondsen niet geheel mag vrijgeven tenzij de betrokkene zijn belastingschuld heeft betaald.

## Art. 5
(De tekst van KB nr. 39, artikel 5, § 1, eerste lid, werd gewijzigd met ingang van 01.01.2013 (Art. 41, KB 30.04.2013, B.S. 08.05.2013, pg. 26764))

§ 1. Wanneer uit het uitgereikte attest dat aan de kredietinstelling of het kredietorganisme wordt overgelegd blijkt dat een bedrag als belastingen of toebehoren opeisbaar is in hoofde van de begunstigde aan wie een krediet, lening of voorschot is toegekend waarvoor een voordeel inzake economische expansie is aangevraagd, mogen de fondsen die afkomstig zijn van het krediet, de lening of het voorschot tot beloop van dat bedrag niet worden vrijgegeven, tenzij de begunstigde een attest overlegt waarin de in artikel 1 van dit besluit aangewezen ambtenaar verklaart dat die belastingen en toebehoren betaald zijn.

Met instemming van de begunstigde mag de kredietinstelling of het kredietorganisme deze fondsen evenwel rechtstreeks overmaken aan het in artikel 1 van dit besluit bedoelde ontvangkantoor.

§ 2. In het geval bedoeld in artikel 3, derde lid, van dit besluit, hoeft de kredietinstelling of het kredietorganisme met de gegevens van het nieuwe attest slechts rekening te houden in de mate dat de fondsen nog niet zijn vrijgegeven vóór het verstrijken van de in die bepaling bedoelde termijn van zes maanden.

## Art. 6
(De tekst van KB nr. 39, artikel 6 is van toepassing met ingang van 01.11.1980 (KB 17.10.1980))

Dit besluit treedt in werking op 1 november 1980.

## Art. 7
(De tekst van KB nr. 39, artikel 7 is van toepassing met ingang van 01.11.1980 (KB 17.10.1980))

Onze Minister van Financiën is belast met de uitvoering van dit besluit.
