---
tags: ["XI", "3.1"]
itaa-lex-sectie: "XI"
wet: "Burgerlijk Wetboek — Boek 1 — Algemene bepalingen"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "24.12.2025"
bron: "onbekend"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/BW-boek1-algemene-bepalingen.pdf
      sha256: ad2ba310c4c88af06d92641f8080f97a843a97717565956ee687d5928e0474cb
      version: 24.12.2025
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 8add68e
    model:
    prompt_version:
  generated_at: '2026-05-12T19:14:55Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-12T19:27:15Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: 'D2: bestand is vrijwel leeg (115 chars, 0 headings, geen inhoud buiten de titel). De PDF bevat enkel een introductie/titelblad zonder eigenlijke artikelinhoud. Structureel leeg voor RAG-doeleinden.'
    layer1:
      status: pass
      run_id: 20260512-210357
      run_at: '2026-05-12T21:03:58Z'
      heading_count: 0
      max_section_chars: 115
      file_size_chars: 115
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-12T19:27:15Z'
      rationale: 'D2: bestand is vrijwel leeg (115 chars, 0 headings, geen inhoud buiten de titel). De PDF bevat enkel een introductie/titelblad zonder eigenlijke artikelinhoud. Structureel leeg voor RAG-doeleinden.'
      concrete_problemen:
        - regel: 1
          categorie: D2
          type: abrupt-cutoff
          voorbeeld: Bestand heeft enkel H1 titel + italic datum — 0 headings, 115 chars
---

# Burgerlijk Wetboek — Boek 1 — Algemene bepalingen

*Bijgewerkt tot en met 24.12.2025 — gecoördineerde versie.*

