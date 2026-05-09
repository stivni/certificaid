---
tags: ["VI.C", "2.4"]
itaa-lex-sectie: "VI.C"
wet: "M.B. nr. 11 van 3 november 1972, met betrekking tot de controle op de toepassing van de belasting over de toegevoegde waarde ten aanzien van de facturen betreffende oprichting van gebouwen"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "03.11.1972"
bron: "Afgesplitst uit Fisconet-compilatie (pdftotext_compilatie_btw)"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/btw-kbs/WBTW-MB-compilatie.pdf
      sha256: e2e322b0d748d0314e5f16d11a0aac6c964d684451d00738c9352b4f32f9171c
      version: 29.04.2024
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 7a134f4
    model:
    prompt_version:
  generated_at: '2026-05-09T16:15:20Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    qa_version: trust-rework-2
    confirmed_at: '2026-05-09T21:27:46Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "L1=pass; L1.5=improvement (Auto-synthesized: heading-injection (inject_wbtw_headings.py) — staging is structureel beter dan resources-versie.); L2=trusted (ETL-fix toegepast: inject_wbtw_headings.py heeft TOC-strip + Artikel-N → ## Art. heading-injectie + AFDELING-normalisatie uitgevoerd. Eerdere needs-rework op 'missing-section' opgeheven.)"
    agent_verdict_at: '2026-05-09T21:27:46Z'
    sample_pick: false
    sample_reviewed_at:
    sample_reviewed_by:
    layer1:
      verdict: pass
      heading_count: 2
      max_section_chars: 537
      file_size_chars: 816
      flags: []
      run_id: 20260509-212552
    layer1_5_diff:
      verdict: improvement
      rationale: 'Auto-synthesized: heading-injection (inject_wbtw_headings.py) — staging is structureel beter dan resources-versie.'
      kritieke_observaties: []
      auto: true
      run_id: trust-rework-2
    layer2_content:
      verdict: needs-rework
      rationale: 'Klein MB (910 chars) met volledige inhoud, maar 0 ##-headings; Artikel-1 en Artikel-2 staan als plain centerlines.'
      problemen:
        - regel: 0
          type: missing-section
          voorbeeld: 'Artikel 1 / Artikel 2 zonder ##-prefix'
      sterkte:
        - Inhoud volledig en leesbaar
      auto: false
      run_id: qa-batch-W4
---

# M.B. nr. 11 van 3 november 1972, met betrekking tot de controle op de toepassing van de belasting over de toegevoegde waarde ten aanzien van de facturen betreffende oprichting van gebouwen

*Bijgewerkt tot en met 03.11.1972 — gecoördineerde versie.*

Ministerieel besluit nr. 11, van 3 november 1972, met betrekking tot de controle
op de toepassing van de belasting over de toegevoegde waarde ten aanzien van
de facturen betreffende oprichting van gebouwen
Uitvoering van artikel 61, § 4, van het Btw-Wetboek.
Officieuze coördinatie

## Art. 1

De ambtenaar bedoeld in artikel 64, § 4, laatste lid, van het Wetboek van de belasting over de toegevoegde
waarde is het hoofd van het controlekantoor in wiens gebied het pas opgerichte gebouw is gelegen.

## Art. 2

Dit besluit treedt in werking op 20 november 1972.
