---
bron: https://www.cbn-cnc.be/nl/adviezen/waarderingsregels
datum: 1992-02-01
gerelateerde_adviezen:
  - datum: '2025-04-25'
    titel: Afschrijvingsmethoden (update) [ONTWERP]
    url: https://www.cbn-cnc.be/nl/adviezen/afschrijvingsmethoden-update-ontwerp
  - datum: '2017-12-13'
    titel: Afschrijving van materiële vaste activa in aanbouw en vooruitbetalingen - Inresultaatname van kapitaalsubsidies
    url: https://www.cbn-cnc.be/nl/adviezen/afschrijving-van-materiele-vaste-activa-in-aanbouw-en-vooruitbetalingen-inresultaatname
  - datum: '2012-10-10'
    titel: De boekhoudkundige verwerking van immateriële vaste activa
    url: https://www.cbn-cnc.be/nl/adviezen/de-boekhoudkundige-verwerking-van-immateriele-vaste-activa
  - datum: '2010-10-06'
    titel: Afschrijvingsmethoden
    url: https://www.cbn-cnc.be/nl/adviezen/afschrijvingsmethoden
nummer: CBN-advies 112/8
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/waarderingsregels
      sha256: 5f9735a6cc71f59d06a1d68dce41ce8103eaf065ab88ae29197085c9ba315c0f
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
    confirmed_at: '2026-05-11T17:05:20Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "A6: paragraaf op regels 73-75 is gesplitst over een lege regel midden in een zin ('om duidelijk het' → lege regel → 'onderscheid te laten blijken') — typisch PDF-kolom-extractie-artefact. E2: tabel (regels 79-86) bevat lege spacer-cellen (| | |) als visuele opvulling uit het bronformaat, geen valide markdown-tabelkolommen."
    layer1:
      file_size_chars: 1899
      flags: []
      heading_count: 0
      max_section_chars: 1899
      run_at: '2026-05-11T15:05:48Z'
      run_id: 20260511-150547
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T17:05:20Z'
      rationale: "A6: paragraaf op regels 73-75 is gesplitst over een lege regel midden in een zin ('om duidelijk het' → lege regel → 'onderscheid te laten blijken') — typisch PDF-kolom-extractie-artefact. E2: tabel (regels 79-86) bevat lege spacer-cellen (| | |) als visuele opvulling uit het bronformaat, geen valide markdown-tabelkolommen."
      concrete_problemen:
        - regel: 73
          categorie: A6
          type: other
          voorbeeld: om duidelijk het [LEGE REGEL] onderscheid te laten blijken
        - regel: 79
          categorie: E2
          type: pseudo-table
          voorbeeld: '| | | **Lineair afschrijvingspercentage op aanschaffingswaarde** | | **Aanvankelijk...**'
themas:
  - afschrijvingen
  - degressieve afschrijving
  - toelichting
  - waarderingsregels
---

# COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN

Artikel 15 van het koninklijk besluit van 8 oktober 1976 stelt dat het bestuursorgaan de regels bepaalt die, met naleving van de bepalingen van het besluit doch rekening houdend met de eigen karakteristieken, gelden voor de waardering van de inventaris en, onder meer, voor de vorming en de aanpassing van afschrijvingen (...). De waarderingsregels worden samengevat in de toelichting op een nauwkeurige wijze die inzicht geeft in de toegepaste waarderingsmethoden. 

Bij onderzoek van een aantal jaarrekeningen neergelegd bij de Balanscentrale, blijkt dat in relatief veel gevallen de samenvatting van de waarderingsregels in de toelichting de lezer onvoldoende inzicht verschaft in de toegepaste waarderingsregels, zodat hun impakt op de rekeningen moeilijk kan beoordeeld worden. 

De Commissie is van plan in de toekomst enige aanbevelingen over dit probleem te formuleren na de betrokken personen en ondernemingen hierover geraadpleegd te hebben. 

Toch zou de Commissie met betrekking tot degressieve afschrijvingen een aanbeveling willen geven om op een bondige wijze de uitwerking van het degressieve systeem toe te lichten, om duidelijk het 

onderscheid te laten blijken met andere afschrijvingsvormen. 

Om elke verkeerde interpretatie over het degressieve afschrijvingspercentage te vermijden, raadt de Commissie aan, bij toepassing van een degressief afschrijvingsplan, in de toelichting te vermelden:

| | | **Lineair afschrijvingspercentage op aanschaffingswaarde** | | **Aanvankelijk toegepast verhoogd afschrijvingspercentage op netto-boekwaarde** | 
|---|---|---|---|---|
| Immateriële vaste activa | | ...% | | ...% | 
| Gebouwen | | ...% | | ...% | 
| Installaties, machines en uitrusting | | ...% | | ...% | 
| Meubilair | | ...% | | ...% | 
| Rollend materieel | | ...% | | ...% | 
| Overige materiële vaste activa | | ...% | | ...% |
