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
    pipeline_version: b893061-dirty
    model:
    prompt_version:
  generated_at: '2026-05-13T12:25:00Z'
  stale: false
  stale_reason:
  trust:
    status: rejected
    confirmed_at: '2026-05-13T13:01:17Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: '(source) De bron-PDF bevat enkel de titel — er is geen artikelinhoud om te indexeren. Body = 1 titellijn + 1 cursieve subkop, file ~2 kB. Geen extractie-fout maar source-defect: de PDF is leeg of niet-bruikbaar. Niet bruikbaar voor RAG. Geen ETL-verbetering kan dit oplossen — een nieuwe PDF-bron is nodig.'
    layer1:
    layer2:
      status: rejected
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T13:01:17Z'
      rationale: '(source) De bron-PDF bevat enkel de titel — er is geen artikelinhoud om te indexeren. Body = 1 titellijn + 1 cursieve subkop, file ~2 kB. Geen extractie-fout maar source-defect: de PDF is leeg of niet-bruikbaar. Niet bruikbaar voor RAG. Geen ETL-verbetering kan dit oplossen — een nieuwe PDF-bron is nodig.'
      concrete_problemen:
        - (source) PDF bevat geen artikelinhoud — body is leeg na header.
        - 0 artikel-headings, heading_count=0, file_size_chars≈114.
        - Burgerlijk Wetboek Boek 1 heeft Art. 1 t/m ~Art. 34 die volledig ontbreken.
---

# Burgerlijk Wetboek — Boek 1 — Algemene bepalingen

*Bijgewerkt tot en met 24.12.2025 — gecoördineerde versie.*

