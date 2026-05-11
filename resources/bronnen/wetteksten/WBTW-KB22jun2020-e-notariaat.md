---
bijgewerkt: '2020'
bron: Fisconetplus.be (officieuze gecoördineerde versie)
bron_rol: itaa_lex
chunk:
  level: 2
  sub_strategy:
  type: Art.
itaa-lex-sectie: VI.B
provenance:
  generated_at: '2026-05-11T13:40:00Z'
  inputs:
    - id: resources/raw/wetteksten/btw-kbs/WBTW-KB22jun2020-e-notariaat.pdf
      sha256: be45dc386b376439de59378c86082c733e467259a0ac3b2762a84ac514054d31
      version: '2020'
  stale: false
  stale_reason:
  tooling:
    model:
    pipeline: tools/etl/convert.py
    pipeline_version: 7a134f4
    prompt_version:
  trust:
    confirmed_at: '2026-05-11T11:46:28Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      status: pass
      run_id: 20260511-134044
      run_at: '2026-05-11T13:40:47Z'
      heading_count: 0
      max_section_chars: 308
      file_size_chars: 308
      flags: []
    layer2:
      agent: subagent-sonnet-4-6
      concrete_problemen:
        - categorie: D1
          regel: 62
          type: abrupt-cutoff
          voorbeeld: 22 JUNI 2020. - Koninklijk besluit tot uitvoering van de artikelen 2, derde lid, 2quater en 8, tweede lid, van het
        - categorie: G1
          regel: 64
          type: other
          voorbeeld: 'Bron : FINANCIEN (kale metadata-tekst zonder verdere inhoud)'
        - categorie: D2
          regel: 65
          type: missing-section
          voorbeeld: '[Opgeheven] <KB 2025-01-31/18, art. 15, 002; Inwerkingtreding : 10-03-2025>'
        - categorie: F1
          regel: 4
          type: naam-mismatch
          voorbeeld: 'frontmatter ''wet'': e-notariaat (art. 93ter WBTW); body: art. 2/2quater/8 WBTW'
      rationale: 'Bestand is feitelijk leeg (307 chars body): titel breekt af mid-zin en het KB is opgeheven per 10-03-2025. D1: afgekapte titel. F1: frontmatter ''wet''-veld verwijst naar art. 93ter WBTW / WIB92 / Wetboek Invordering (e-notariaat), maar de body verwijst enkel naar art. 2, 2quater en 8 WBTW — naam-mismatch. Geen bruikbare inhoud voor RAG.'
      run_at: '2026-05-11T11:46:28Z'
      status: rejected
    rationale: 'Bestand is feitelijk leeg (307 chars body): titel breekt af mid-zin en het KB is opgeheven per 10-03-2025. D1: afgekapte titel. F1: frontmatter ''wet''-veld verwijst naar art. 93ter WBTW / WIB92 / Wetboek Invordering (e-notariaat), maar de body verwijst enkel naar art. 2, 2quater en 8 WBTW — naam-mismatch. Geen bruikbare inhoud voor RAG.'
    status: rejected
status: beschikbaar
tags:
  - VI.B
  - '2.4'
wet: K.B. 22 juni 2020 tot uitvoering van art. 93ter WBTW, art. 412bis en 433–435 WIB92 en art. 35–37, 43–45 en 47 Wetboek Invordering inzake het e-notariaat
---

# BTW KB 22/06/2020 — E-notariaat

*Bijgewerkt tot en met 2020 — gecoördineerde versie.*

Titel

22 JUNI 2020. - Koninklijk besluit tot uitvoering van de artikelen 2, derde lid, 2quater en 8, tweede lid, van het

Bron : FINANCIEN

[Opgeheven] <KB 2025-01-31/18, art. 15, 002; Inwerkingtreding : 10-03-2025>
