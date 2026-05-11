---
bijgewerkt: 24.12.2025
bron: ejustice.just.fgov.be (gecoördineerde versie)
bron_rol: itaa_lex
chunk:
  level: 3
  sub_strategy:
  type: Art.
itaa-lex-sectie: XI
provenance:
  inputs:
    - id: resources/raw/wetteksten/BW-boek1-algemene-bepalingen.pdf
      sha256: ad2ba310c4c88af06d92641f8080f97a843a97717565956ee687d5928e0474cb
      version: 24.12.2025
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 11f9196
    model:
    prompt_version:
  generated_at: '2026-05-11T16:21:26Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T16:30:30Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "D2: het bestand bevat vrijwel geen artikelinhoud — enkel frontmatter + één titellijn + één cursieve subkop (51 regels, 114 chars body). Laag-1 geeft heading_count=0 en file_size_chars=114. De wet 'Burgerlijk Wetboek — Boek 1 — Algemene bepalingen' heeft artikkels (o.a. Art.1 t/m Art.34 in de BW-structuur); de PDF is vermoedelijk niet of leeg geconverteerd. Dit is een extractie-failure, niet een source-fout."
    layer1:
      status: pass
      run_id: 20260511-162232
      run_at: '2026-05-11T16:22:33Z'
      heading_count: 0
      max_section_chars: 114
      file_size_chars: 114
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T16:30:30Z'
      rationale: "D2: het bestand bevat vrijwel geen artikelinhoud — enkel frontmatter + één titellijn + één cursieve subkop (51 regels, 114 chars body). Laag-1 geeft heading_count=0 en file_size_chars=114. De wet 'Burgerlijk Wetboek — Boek 1 — Algemene bepalingen' heeft artikkels (o.a. Art.1 t/m Art.34 in de BW-structuur); de PDF is vermoedelijk niet of leeg geconverteerd. Dit is een extractie-failure, niet een source-fout."
      concrete_problemen:
        - regel: 49
          categorie: B4
          type: missing-section
          voorbeeld: '# Burgerlijk Wetboek — Boek 1 — Algemene bepalingen\n\n*Bijgewerkt...*\n[EOF]'
status: beschikbaar
tags:
  - XI
  - '3.1'
wet: Burgerlijk Wetboek — Boek 1 — Algemene bepalingen
---

# Burgerlijk Wetboek — Boek 1 — Algemene bepalingen

*Bijgewerkt tot en met 24.12.2025 — gecoördineerde versie.*
