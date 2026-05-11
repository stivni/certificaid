---
tags: [VI.B, '2.4']
itaa-lex-sectie: VI.B
wet: K.B. 22 juni 2020 tot uitvoering van art. 93ter WBTW, art. 412bis en 433–435 WIB92 en art. 35–37, 43–45 en 47 Wetboek Invordering inzake het e-notariaat
bron_rol: itaa_lex
status: beschikbaar
bijgewerkt: '2020'
bron: Fisconetplus.be (officieuze gecoördineerde versie)
chunk:
  level: 2
  type: Art.
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
    status: rejected
    confirmed_at: '2026-05-11T11:46:28Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Bestand is feitelijk leeg (307 chars body): titel breekt af mid-zin en het KB is opgeheven per 10-03-2025. D1: afgekapte titel. F1: frontmatter 'wet'-veld verwijst naar art. 93ter WBTW / WIB92 / Wetboek Invordering (e-notariaat), maar de body verwijst enkel naar art. 2, 2quater en 8 WBTW — naam-mismatch. Geen bruikbare inhoud voor RAG."
    layer1:
      status: pass
      run_id: 20260509-212552
      run_at:
      heading_count: 0
      max_section_chars: 307
      file_size_chars: 307
      flags: []
    layer2:
      status: rejected
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T11:46:28Z'
      rationale: "Bestand is feitelijk leeg (307 chars body): titel breekt af mid-zin en het KB is opgeheven per 10-03-2025. D1: afgekapte titel. F1: frontmatter 'wet'-veld verwijst naar art. 93ter WBTW / WIB92 / Wetboek Invordering (e-notariaat), maar de body verwijst enkel naar art. 2, 2quater en 8 WBTW — naam-mismatch. Geen bruikbare inhoud voor RAG."
      concrete_problemen:
        - regel: 62
          categorie: D1
          type: abrupt-cutoff
          voorbeeld: 22 JUNI 2020. - Koninklijk besluit tot uitvoering van de artikelen 2, derde lid, 2quater en 8, tweede lid, van het
        - regel: 64
          categorie: G1
          type: other
          voorbeeld: 'Bron : FINANCIEN (kale metadata-tekst zonder verdere inhoud)'
        - regel: 65
          categorie: D2
          type: missing-section
          voorbeeld: '[Opgeheven] <KB 2025-01-31/18, art. 15, 002; Inwerkingtreding : 10-03-2025>'
        - regel: 4
          categorie: F1
          type: naam-mismatch
          voorbeeld: "frontmatter 'wet': e-notariaat (art. 93ter WBTW); body: art. 2/2quater/8 WBTW"
---

# BTW KB 22/06/2020 — E-notariaat

*Bijgewerkt tot en met 2020 — gecoördineerde versie.*

Titel

22 JUNI 2020. - Koninklijk besluit tot uitvoering van de artikelen 2, derde lid, 2quater en 8, tweede lid, van het

Bron : FINANCIEN

[Opgeheven] <KB 2025-01-31/18, art. 15, 002; Inwerkingtreding : 10-03-2025>