---
tags: [norm, itaa, deontologie, beroepsgeheim]
naam: "Het beroepsgeheim van de accountant en de belastingadviseur"
type: norm
itaa-lex-sectie: "XXI"
toepassingsgebied: "Alle ITAA-leden — beroepsgeheim onder Wet-ITAA-2019 art. 57 + Sw. art. 458"
themas:
  - beroepsgeheim
  - confidentialiteit
  - deontologie
  - informatieplicht
  - wettelijke uitzonderingen
bron: beexcellent.itaa.be
url: https://beexcellent.itaa.be/Articles/article/1238
provenance:
  inputs:
    - id: resources/raw/normen/itaa-deontologie-beroepsgeheim.docx
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version:
    model:
    prompt_version:
  generated_at:
  stale: false
  stale_reason:
  trust:
    status: unreviewed
    qa_version:
    confirmed_at:
    confirmed_by: default
    rationale:
    layer1:
      verdict: warn
      heading_count: 24
      max_section_chars: 39045
      file_size_chars: 39045
      flags:
        - name: max_section_size
          status: warn
          detail: 'langste sectie op ##-niveau: 39045 chars (>24000); chunker splitst auto op alinea-grenzen via split_long_chunk'
          samples: []
      run_id: 20260509-212552
    layer1_5_diff:
      verdict: improvement
      rationale: 'Auto-synthesized: ETL-fixes vandaag (NBSP, sub_strategy, justel-extractor, etc.) verbeteren bestaande versie.'
      kritieke_observaties: []
      auto: true
      run_id: trust-finalize-1
    layer2_content:
      verdict: needs-rework
      rationale: 'Inhoudelijk volledig (BeExcellent extract van vragen 1-13 met voetnoten 1-67), maar frontmatter zet chunk.level=2 terwijl alle 13 hoofdsecties als ### staan en er 0 ## headings zijn. De chunker zal bij level=2 het hele document als één chunk behandelen. Tussen H1 en eerste ### staat een orphan TOC-lijstje met section-titels.'
      problemen:
        - regel: 27
          type: other
          voorbeeld: 'chunk.level=2 maar 0 ## headings, 13 ### headings — mismatch met chunker-config'
        - regel: 55
          type: other
          voorbeeld: 'L55-67: orphan TOC-lijst met sectienamen tussen intro en eerste vraag, zonder nummering of context'
        - regel: 72
          type: other
          voorbeeld: "'### 2. Wat is de reden van bestaan van het beroepsgeheim?1' — losse 1 (voetnoot-marker) ingebed in heading"
      sterkte:
        - 'Alle 13 hoofdvragen herkenbaar als ### headings, plus geneste #### / ##### voor sub-secties'
        - Voetnoten 1-67 volledig bewaard onderaan
        - Frontmatter met juiste metadata (bron_rol=interpretatief, themas, url)
      auto: false
      run_id: qa-batch-normen
note: >-
  Gedownload van ITAA BeExcellent platform (Deontologie > Beroepsgeheim).
  Behandelt het beroepsgeheim van accountants en belastingadviseurs onder
  artikel 57 van de Wet-ITAA-2019 en strafrechtelijke onderbouwing via
  Sw. art. 458. Bevat handleiding-vorm: wat is beroepsgeheim, wettelijke
  uitzonderingen, witwasmeldplicht, samenwerking met collega's.
---

# Het beroepsgeheim van de accountant en de belastingadviseur

(automatisch gegenereerd — body wordt aangemaakt door convert.py)
