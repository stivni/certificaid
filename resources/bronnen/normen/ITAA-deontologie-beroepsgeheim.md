---
tags: [norm, itaa, deontologie, beroepsgeheim]
naam: Het beroepsgeheim van de accountant en de belastingadviseur
type: norm
itaa-lex-sectie: XXI
toepassingsgebied: Alle ITAA-leden — beroepsgeheim onder Wet-ITAA-2019 art. 57 + Sw. art. 458
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
    confirmed_at:
    confirmed_by:
    rationale:
    layer1:
      status: pass
      run_id: 20260511-085756
      run_at: '2026-05-11T08:57:56Z'
      heading_count: 0
      max_section_chars: 130
      file_size_chars: 130
      flags: []
    layer2:
      status: needs-rework
      agent:
      run_at:
      rationale: 'Inhoudelijk volledig (BeExcellent extract van vragen 1-13 met voetnoten 1-67), maar frontmatter zet chunk.level=2 terwijl alle 13 hoofdsecties als ### staan en er 0 ## headings zijn. De chunker zal bij level=2 het hele document als één chunk behandelen. Tussen H1 en eerste ### staat een orphan TOC-lijstje met section-titels.'
      concrete_problemen:
        - regel: 27
          type: other
          voorbeeld: 'chunk.level=2 maar 0 ## headings, 13 ### headings — mismatch met chunker-config'
        - regel: 55
          type: other
          voorbeeld: 'L55-67: orphan TOC-lijst met sectienamen tussen intro en eerste vraag, zonder nummering of context'
        - regel: 72
          type: other
          voorbeeld: "'### 2. Wat is de reden van bestaan van het beroepsgeheim?1' — losse 1 (voetnoot-marker) ingebed in heading"
note: >-
  Gedownload van ITAA BeExcellent platform (Deontologie > Beroepsgeheim).
  Behandelt het beroepsgeheim van accountants en belastingadviseurs onder
  artikel 57 van de Wet-ITAA-2019 en strafrechtelijke onderbouwing via
  Sw. art. 458. Bevat handleiding-vorm: wat is beroepsgeheim, wettelijke
  uitzonderingen, witwasmeldplicht, samenwerking met collega's.
---

# Het beroepsgeheim van de accountant en de belastingadviseur

(automatisch gegenereerd — body wordt aangemaakt door convert.py)
