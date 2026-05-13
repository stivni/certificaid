---
bron: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-loontussenkomst-door-de-overheid-in-hoofde-van-de-werkgever
datum: 2010-09-08
gerelateerde_adviezen:
  - datum: '2013-04-24'
    titel: De boekhoudkundige verwerking van de door de Waalse regering gecreëerde opleidingscheques
    url: https://www.cbn-cnc.be/nl/adviezen/de-boekhoudkundige-verwerking-van-de-door-de-waalse-regering-gecreeerde-opleidingscheques
  - datum: '2009-11-18'
    titel: De boekhoudkundige verwerking van het stelsel tot gedeeltelijke vrijstelling van betaling van de bedrijfsvoorheffing, zoals geregeld door artikel 275/3 van het Wetboek van de Inkomstenbelastingen 1992
    url: https://www.cbn-cnc.be/nl/adviezen/de-boekhoudkundige-verwerking-van-het-stelsel-tot-gedeeltelijke-vrijstelling-van-0
nummer: CBN-advies 2010/11
themas:
  - bedrijfssubsidie
  - bezoldiging
  - exploitatiesubsidie
  - loonlast
  - loontussenkomst
  - overheid
  - werkuitkering
  - win-win aanwervingsplan
  - vrijstelling van betaling
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-loontussenkomst-door-de-overheid-in-hoofde-van-de-werkgever
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: b4eac1f-dirty
    model:
    prompt_version:
  generated_at: '2026-05-12T23:38:07Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-13T13:45:17Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: Geen ETL-artefacten aangetroffen. Heading-structuur aanwezig (1 headings), inhoud volledig, voetnoten correct gerenderd, geen form-feeds of column-bleed.
    layer1:
      status: pass
      run_id: 20260512-233938
      run_at: '2026-05-12T23:39:41Z'
      heading_count: 0
      max_section_chars: 3489
      file_size_chars: 3489
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T13:45:17Z'
      rationale: Geen ETL-artefacten aangetroffen. Heading-structuur aanwezig (1 headings), inhoud volledig, voetnoten correct gerenderd, geen form-feeds of column-bleed.
      concrete_problemen: []
---
# CBN-advies 2010/11 – Boekhoudkundige verwerking van loontussenkomst door de overheid in hoofde van de werkgever (update)

CBN-advies 2010/11 – Boekhoudkundige verwerking van loontussenkomst door de overheid in hoofde van de werkgever (update)

De Commissie werd gevraagd naar de boekhoudkundige verwerking van loontussenkomsten door de overheid in het kader van het “win-win aanwervingsplan”[^2].

Het win-win aanwervingsplan houdt in dat de overheid gedurende een aantal maanden een “werkuitkering” betaalt aan een werknemer die op het ogenblik van de indienstneming uitkeringsgerechtigde volledige werkloze was, voor zover werknemer en werkgever voldoen aan alle voorwaarden omschreven in het koninklijk besluit van 19 december 2001.

Deze werkuitkering wordt in mindering gebracht van het door de werkgever te betalen nettoloon[^3]. De loontussenkomst betekent dus voor de werkgever een vrijstelling van betaling van een deel van het nettoloon aan de werknemer. 

Van zodra het ontstaan van de loonlast enerzijds en de eventueel gedeeltelijke vrijstelling van betaling anderzijds hun oorsprong vinden in verschillende juridische kaders, kan er, volgens de Commissie, niet worden overgegaan tot de boeking van deze vrijstelling op de creditzijde van de rekening 620 “Bezoldigingen en rechtstreekse sociale voordelen”, aangezien compensatie verboden is (artikel 3:2, § 2 van het koninklijk besluit van 29 april 2019 tot uitvoering van het Wetboek van vennootschappen en verenigingen)[^4].

De loonlast resulteert uit het arbeidscontract dat gesloten werd tussen werknemer en werkgever. De werkuitkering, die in mindering wordt gebracht van het te betalen nettoloon, vindt daarentegen haar oorsprong in het koninklijk besluit van 19 december 2001. Aangezien er dus sprake is van twee verschillende juridische verhoudingen, is de Commissie van mening dat de loonlast van de desbetreffende werknemers bruto geregistreerd moet worden. 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 620 | Bezoldigingen en rechtstreekse sociale voordelen | x | |
| | 621 | Werkgeversbijdragen voor sociale verzekeringen | x | |
| aan | 453 | Ingehouden voorheffingen | | x |
| | 454 | Rijksdienst voor sociale zekerheid | x | |
| | 455 | Bezoldigingen | x | |

Het wegvallen van een deel van de schuld met betrekking tot bezoldigingen dient als een exploitatiesubsidie beschouwd te worden, aangezien dit rechtstreeks het exploitatieresultaat beïnvloedt. Dit moet geboekt worden onder de bedrijfsopbrengsten, in de rubriek I.D. *Andere bedrijfsopbrengsten*.

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 455 | Bezoldigingen | x | |
| aan | 740 | Bedrijfssubsidies en compenserende bedragen | | x |

[^1]: Onderhavig geactualiseerd advies is tot stand gekomen nadat het ontwerpadvies op 30 april 2025 ter publieke consultatie werd gepubliceerd op de website van de CBN.

[^2]: Koninklijk besluit van 19 december 2001 tot bevordering van de tewerkstelling van langdurig werkzoekenden, BS 12 januari 2002.

[^3]: Het bedrag van de werkuitkering wordt begrensd tot het nettoloon waarop de werknemer voor de betreffende maand recht heeft (art. 15, § 2 KB 19 december 2001).

[^4]: CBN-advies 2009/13 - De boekhoudkundige verwerking van het stelsel tot gedeeltelijke vrijstelling van betaling van de bedrijfsvoorheffing, zoals geregeld door artikel 275/3 van het Wetboek van de Inkomstenbelastingen 1992.
