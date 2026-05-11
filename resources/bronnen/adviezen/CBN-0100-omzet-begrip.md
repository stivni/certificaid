---
nummer: CBN-advies 100
datum: 1977-08-01
themas:
  - verwerking van vermogensbestanddelen
  - voordelen bovenop het loon
  - omzet
bron: https://www.cbn-cnc.be/nl/adviezen/omzet-begrip
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/omzet-begrip
      sha256: 0651a46284667473bcb25099b0a2a168d21a95975e629ef2f6a6dbe5efa8c061
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:33:36Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T11:51:19Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "B3: de hoofd-heading is gedupliceerd op regels 47 en 49 ('# CBN advies 100 - Omzet – Begrip' twee keer). Scraper heeft de paginatitel en de article-heading als twee aparte regels gepakt. Inhoudelijk verder volledig en correct."
    layer1:
      status: pass
      run_id: 20260511-083333
      run_at:
      heading_count: 0
      max_section_chars: 854
      file_size_chars: 854
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T11:51:19Z'
      rationale: "B3: de hoofd-heading is gedupliceerd op regels 47 en 49 ('# CBN advies 100 - Omzet – Begrip' twee keer). Scraper heeft de paginatitel en de article-heading als twee aparte regels gepakt. Inhoudelijk verder volledig en correct."
      concrete_problemen:
        - regel: 49
          categorie: B3
          type: other
          voorbeeld: '# CBN advies 100 - Omzet – Begrip (duplicate van regel 47)'
gerelateerde_adviezen:
  - titel: Verwerking in de geconsolideerde jaarrekening van de vermogensbestanddelen en de resultaten op de datum waarop de geconsolideerde jaarrekening wordt afgesloten
    url: https://www.cbn-cnc.be/nl/adviezen/verwerking-in-de-geconsolideerde-jaarrekening-van-de-vermogensbestanddelen-en-de
    datum: '1991-03-01'
---

# CBN advies 100 - Omzet – Begrip

# CBN advies 100 - Omzet – Begrip

Tal van bepalingen van de wet van 17 juli 1975 en van het koninklijk besluit van 8 oktober 1976 verwijzen naar het begrip omzetcijfer[^1]. 

Het omzetcijfer wordt als volgt bepaald door het koninklijk besluit van 8 oktober 1976: 

"Het bedrag van de verkopen en dienstverleningen aan derden die tot de gebruikelijke activiteit van de onderneming behoren, onder aftrek van de op de verkopen toegestane verminderingen; dit bedrag omvat niet de belasting over de toegevoegde waarde en de andere rechtstreeks met de omzet verbonden belastingen; wat de handelaars, natuurlijke personen, betreft, omvat de omzet tevens het verbruik in natura, anders dan ten behoeve van hun handel".

[^1]: Wet, artikelen 5 en 12, koninklijk besluit, artikel 39 en rubriek 5.109 van de resultatenrekening.
