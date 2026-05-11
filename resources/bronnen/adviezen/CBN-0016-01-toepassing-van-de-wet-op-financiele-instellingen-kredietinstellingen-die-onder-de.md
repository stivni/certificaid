---
nummer: CBN-advies 16/1
datum: 1977-12-01
themas:
  - financiële instelling
  - kredietinstelling
bron: https://www.cbn-cnc.be/nl/adviezen/toepassing-van-de-wet-op-financiele-instellingen-kredietinstellingen-die-onder-de
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/toepassing-van-de-wet-op-financiele-instellingen-kredietinstellingen-die-onder-de
      sha256: f8e4652436db7b0cecba38ff5200255e61355b17c7d905b26369463da1ad4923
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:33:34Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T11:51:19Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "G1/G2: in de frontmatter-sectie gerelateerde_adviezen staat op r44 een ongeparseerde HTML-entity: 'Het begrip &quot;financiële instelling&quot;' — de scraper heeft de HTML-entities niet gedecodeerd. Dit is een frontmatter-kwaliteitsdefect dat voor downstream YAML-parsing problemen kan geven. Verder: A4: 7 gevallen U+2010 HYPHEN in r49 en r55 (titels van instellingen zoals 'Spaar‐ en Lijfrentekas'). Spelfout 'valln' (r55). Geen duplicate headings."
    layer1:
      status: pass
      run_id: 20260511-083333
      run_at:
      heading_count: 0
      max_section_chars: 1668
      file_size_chars: 1668
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T11:51:19Z'
      rationale: "G1/G2: in de frontmatter-sectie gerelateerde_adviezen staat op r44 een ongeparseerde HTML-entity: 'Het begrip &quot;financiële instelling&quot;' — de scraper heeft de HTML-entities niet gedecodeerd. Dit is een frontmatter-kwaliteitsdefect dat voor downstream YAML-parsing problemen kan geven. Verder: A4: 7 gevallen U+2010 HYPHEN in r49 en r55 (titels van instellingen zoals 'Spaar‐ en Lijfrentekas'). Spelfout 'valln' (r55). Geen duplicate headings."
      concrete_problemen:
        - regel: 44
          categorie: G2
          type: other
          voorbeeld: 'titel: Het begrip &quot;financiële instelling&quot;'
        - regel: 55
          categorie: D1
          type: other
          voorbeeld: de ondernemingen die onder toepassing valln van het koninklijk besluit
        - regel: 49
          categorie: A4
          type: other
          voorbeeld: financiële instellingen ‐ Kredietinstellingen die onder de toepassing
gerelateerde_adviezen:
  - titel: Coördinatiecentrum - Financiële instelling
    url: https://www.cbn-cnc.be/nl/adviezen/coordinatiecentrum-financiele-instelling
    datum: '1988-06-01'
  - titel: Het begrip &quot;financiële instelling&quot;
    url: https://www.cbn-cnc.be/nl/adviezen/het-begrip-financiele-instelling
    datum: '1980-01-01'
---

# CBN-advies 16-1 Toepassing van de wet op financiële instellingen ‐ Kredietinstellingen die onder de toepassing vallen van een bijzondere wet

Dit advies is verouderd als gevolg van de aangebrachte wijzigingen aan de betrokken bepalingen, actueel artikel 15 van de wet

Luidens artikel 16 van de wet, zijn artikel 5 en de artikelen 10 tot 15 van die wet, evenals de besluiten getroffen ter uitvoering van artikel 4, zesde lid, en van artikel 7, vierde lid, niet van toepassing op kredietinstellingen waarvoor een bijzondere wet geldt, op door die instellingen erkende kredietverenigingen, op banken, op private spaarkassen, op ondernemingen die onder hoofdstuk I van de wet van 10 juni 1964 en op ondernemingen die onder het koninklijk besluit nr. 64 van 10 november 1967 vallen. 

In antwoord op een vraag over de betekenis van de termen «Kredietinstellingen waarvoor een bijzondere wet geldt» heeft de Commissie geantwoord dat deze alleen de gevallen betreffen waarin een wet een onderneming creëert of organiseert (Nationale Bank van België ‐ Algemene Spaar‐ en Lijfrentekas ‐ Nationale Maatschappij voor Krediet aan de Nijverheid ‐ Nationale Kas voor Beroepskrediet ‐Nationaal Instituut voor Landbouwkrediet ‐ Centraal Bureau voor Hypothecair Krediet, enz.) en niet de gevallen waarin een wet van toepassing zou zijn op categorieën ondernemingen. De afzonderlijke vermelding in artikel 16 van de banken, de private spaarkassen, de ondernemingen die onder toepassing vallen van hoofdstuk I van de wet van 10 juni 1964 en die welke onder de toepassing valln van het koninklijk besluit nr. 64 van 10 november 1967 sluit duidelijk alle extensieve interpretatie uit.
