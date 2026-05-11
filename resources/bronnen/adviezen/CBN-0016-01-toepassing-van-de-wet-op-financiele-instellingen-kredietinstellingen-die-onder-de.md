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
  generated_at: '2026-05-11T17:48:38Z'
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/toepassing-van-de-wet-op-financiele-instellingen-kredietinstellingen-die-onder-de
      sha256: f8e4652436db7b0cecba38ff5200255e61355b17c7d905b26369463da1ad4923
      version:
  stale: false
  stale_reason:
  tooling:
    model:
    pipeline: tools/etl/convert.py
    pipeline_version: 11f9196
    prompt_version:
  trust:
    confirmed_at: '2026-05-11T17:05:20Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      status: pass
      run_id: 20260511-174840
      run_at: '2026-05-11T17:48:40Z'
      heading_count: 0
      max_section_chars: 1668
      file_size_chars: 1668
      flags: []
    layer2:
      agent: subagent-sonnet-4-6
      concrete_problemen:
        - categorie: G2
          regel: 9
          type: other
          voorbeeld: 'titel: Het begrip &quot;financiële instelling&quot; — HTML-entity niet gedecode in YAML'
        - categorie: (source)
          regel: 63
          type: source-typo
          voorbeeld: ondernemingen die onder de toepassing valln van het koninklijk besluit nr. 64
      rationale: Frontmatter regel 9 bevat ongeparseerde HTML-entity '&quot;' in de YAML-waarde van gerelateerde_adviezen[1].titel ('Het begrip &quot;financiële instelling&quot;') — dit is een ETL-bug (HTML niet gedecode), geen source-typo. De typo 'valln' op regel 63 in de body-tekst is een source-typo (staat letterlijk op de CBN-website). Body zelf is verder volledig en clean.
      run_at: '2026-05-11T17:05:20Z'
      status: needs-rework
    rationale: Frontmatter regel 9 bevat ongeparseerde HTML-entity '&quot;' in de YAML-waarde van gerelateerde_adviezen[1].titel ('Het begrip &quot;financiële instelling&quot;') — dit is een ETL-bug (HTML niet gedecode), geen source-typo. De typo 'valln' op regel 63 in de body-tekst is een source-typo (staat letterlijk op de CBN-website). Body zelf is verder volledig en clean.
    status: needs-rework
themas:
  - financiële instelling
  - kredietinstelling
---

# CBN-advies 16-1 Toepassing van de wet op financiële instellingen - Kredietinstellingen die onder de toepassing vallen van een bijzondere wet

Dit advies is verouderd als gevolg van de aangebrachte wijzigingen aan de betrokken bepalingen, actueel artikel 15 van de wet

Luidens artikel 16 van de wet, zijn artikel 5 en de artikelen 10 tot 15 van die wet, evenals de besluiten getroffen ter uitvoering van artikel 4, zesde lid, en van artikel 7, vierde lid, niet van toepassing op kredietinstellingen waarvoor een bijzondere wet geldt, op door die instellingen erkende kredietverenigingen, op banken, op private spaarkassen, op ondernemingen die onder hoofdstuk I van de wet van 10 juni 1964 en op ondernemingen die onder het koninklijk besluit nr. 64 van 10 november 1967 vallen. 

In antwoord op een vraag over de betekenis van de termen «Kredietinstellingen waarvoor een bijzondere wet geldt» heeft de Commissie geantwoord dat deze alleen de gevallen betreffen waarin een wet een onderneming creëert of organiseert (Nationale Bank van België - Algemene Spaar- en Lijfrentekas - Nationale Maatschappij voor Krediet aan de Nijverheid - Nationale Kas voor Beroepskrediet -Nationaal Instituut voor Landbouwkrediet - Centraal Bureau voor Hypothecair Krediet, enz.) en niet de gevallen waarin een wet van toepassing zou zijn op categorieën ondernemingen. De afzonderlijke vermelding in artikel 16 van de banken, de private spaarkassen, de ondernemingen die onder toepassing vallen van hoofdstuk I van de wet van 10 juni 1964 en die welke onder de toepassing valln van het koninklijk besluit nr. 64 van 10 november 1967 sluit duidelijk alle extensieve interpretatie uit.
