---
bron: https://www.cbn-cnc.be/nl/adviezen/toepassing-van-de-wet-op-financiele-instellingen-kredietinstellingen-die-onder-de
datum: 1977-12-01
gerelateerde_adviezen:
  - datum: '1988-06-01'
    titel: Coördinatiecentrum - Financiële instelling
    url: https://www.cbn-cnc.be/nl/adviezen/coordinatiecentrum-financiele-instelling
  - datum: '1980-01-01'
    titel: Het begrip &quot;financiële instelling&quot;
    url: https://www.cbn-cnc.be/nl/adviezen/het-begrip-financiele-instelling
nummer: CBN-advies 16/1
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/toepassing-van-de-wet-op-financiele-instellingen-kredietinstellingen-die-onder-de
      sha256: f8e4652436db7b0cecba38ff5200255e61355b17c7d905b26369463da1ad4923
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-11T13:15:10Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T13:16:01Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Twee hardnekkige problemen niet opgelost door scraper-fix: (1) G2/frontmatter: in de YAML-sectie gerelateerde_adviezen staat nog steeds een ongeparseerde HTML-entity op r9 ('Het begrip &quot;financiële instelling&quot;') — downstream YAML-parsing kan hier falen. (2) D1: typo 'valln' (r67) in de body. A4 (U+2010 in de heading r61 '‐ Kredietinstellingen') lijkt nog aanwezig gezien de heading tekst. Geen duplicate headings."
    layer1:
      status: pass
      run_id: 20260511-131513
      run_at: '2026-05-11T13:15:13Z'
      heading_count: 0
      max_section_chars: 1668
      file_size_chars: 1668
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T13:16:01Z'
      rationale: "Twee hardnekkige problemen niet opgelost door scraper-fix: (1) G2/frontmatter: in de YAML-sectie gerelateerde_adviezen staat nog steeds een ongeparseerde HTML-entity op r9 ('Het begrip &quot;financiële instelling&quot;') — downstream YAML-parsing kan hier falen. (2) D1: typo 'valln' (r67) in de body. A4 (U+2010 in de heading r61 '‐ Kredietinstellingen') lijkt nog aanwezig gezien de heading tekst. Geen duplicate headings."
      concrete_problemen:
        - regel: 9
          categorie: G2
          type: other
          voorbeeld: 'titel: Het begrip &quot;financiële instelling&quot;'
        - regel: 61
          categorie: A4
          type: other
          voorbeeld: CBN-advies 16-1 Toepassing van de wet op financiële instellingen ‐ Kredietinstellingen
        - regel: 67
          categorie: D1
          type: other
          voorbeeld: die onder de toepassing valln van het koninklijk besluit nr. 64
themas:
  - financiële instelling
  - kredietinstelling
---

# CBN-advies 16-1 Toepassing van de wet op financiële instellingen - Kredietinstellingen die onder de toepassing vallen van een bijzondere wet

Dit advies is verouderd als gevolg van de aangebrachte wijzigingen aan de betrokken bepalingen, actueel artikel 15 van de wet

Luidens artikel 16 van de wet, zijn artikel 5 en de artikelen 10 tot 15 van die wet, evenals de besluiten getroffen ter uitvoering van artikel 4, zesde lid, en van artikel 7, vierde lid, niet van toepassing op kredietinstellingen waarvoor een bijzondere wet geldt, op door die instellingen erkende kredietverenigingen, op banken, op private spaarkassen, op ondernemingen die onder hoofdstuk I van de wet van 10 juni 1964 en op ondernemingen die onder het koninklijk besluit nr. 64 van 10 november 1967 vallen. 

In antwoord op een vraag over de betekenis van de termen «Kredietinstellingen waarvoor een bijzondere wet geldt» heeft de Commissie geantwoord dat deze alleen de gevallen betreffen waarin een wet een onderneming creëert of organiseert (Nationale Bank van België - Algemene Spaar- en Lijfrentekas - Nationale Maatschappij voor Krediet aan de Nijverheid - Nationale Kas voor Beroepskrediet -Nationaal Instituut voor Landbouwkrediet - Centraal Bureau voor Hypothecair Krediet, enz.) en niet de gevallen waarin een wet van toepassing zou zijn op categorieën ondernemingen. De afzonderlijke vermelding in artikel 16 van de banken, de private spaarkassen, de ondernemingen die onder toepassing vallen van hoofdstuk I van de wet van 10 juni 1964 en die welke onder de toepassing valln van het koninklijk besluit nr. 64 van 10 november 1967 sluit duidelijk alle extensieve interpretatie uit.
