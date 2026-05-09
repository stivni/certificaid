---
tags: ["VI.B", "2.4"]
itaa-lex-sectie: "VI.B"
wet: "K.B. 22 juni 2020 tot uitvoering van art. 93ter WBTW, art. 412bis en 433–435 WIB92 en art. 35–37, 43–45 en 47 Wetboek Invordering inzake het e-notariaat"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "2020"
bron: "Fisconetplus.be (officieuze gecoördineerde versie)"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/btw-kbs/WBTW-KB22jun2020-e-notariaat.pdf
      sha256: be45dc386b376439de59378c86082c733e467259a0ac3b2762a84ac514054d31
      version: '2020'
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 7a134f4
    model:
    prompt_version:
  generated_at: '2026-05-09T16:15:17Z'
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
      heading_count: 0
      max_section_chars: 307
      file_size_chars: 307
      flags: []
      run_id: 20260509-212552
    layer1_5_diff:
      verdict: improvement
      rationale: 'Auto-synthesized: heading-injection (inject_wbtw_headings.py) — staging is structureel beter dan resources-versie.'
      kritieke_observaties: []
      auto: true
      run_id: trust-rework-2
    layer2_content:
      verdict: rejected
      rationale: "Bestand is feitelijk leeg (307 chars body): titel breekt af mid-zin ('Koninklijk besluit tot uitvoering van de artikelen 2, derde lid, 2quater en 8, tweede lid, van het') en KB is sinds 10-03-2025 opgeheven. Geen Artikel-content aanwezig. Bovendien: frontmatter 'wet'-veld noemt e-notariaat (art. 93ter, art. 412bis WIB92, Wetboek Invordering) terwijl de pagebody alleen verwijst naar 'art. 2, 2quater en 8 WBTW' — frontmatter past niet bij de (lege) body en pdf-extractie heeft de hoofdtekst niet meegenomen."
      problemen:
        - regel: 40
          type: abrupt-cutoff
          voorbeeld: "Titel eindigt: 'van de artikelen 2, derde lid, 2quater en 8, tweede lid, van het'"
        - regel: 44
          type: other
          voorbeeld: '[Opgeheven] <KB 2025-01-31/18, art. 15, 002; Inwerkingtreding : 10-03-2025>'
        - regel: 4
          type: naam-mismatch
          voorbeeld: frontmatter 'wet' verwijst naar art. 93ter WBTW + WIB92 + Wetboek Invordering (e-notariaat); body verwijst naar art. 2/2quater/8 WBTW
      sterkte:
        - Provenance + sha256 aanwezig
      auto: false
      run_id: qa-batch-W3
---

# BTW KB 22/06/2020 — E-notariaat

*Bijgewerkt tot en met 2020 — gecoördineerde versie.*

Titel

22 JUNI 2020. - Koninklijk besluit tot uitvoering van de artikelen 2, derde lid, 2quater en 8, tweede lid, van het

Bron : FINANCIEN

[Opgeheven] <KB 2025-01-31/18, art. 15, 002; Inwerkingtreding : 10-03-2025>