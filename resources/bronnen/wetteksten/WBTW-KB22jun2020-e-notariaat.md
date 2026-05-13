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
    pipeline_version: dbf933a-dirty
    model:
    prompt_version:
  generated_at: '2026-05-13T10:54:03Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-13T11:05:03Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Bestand is feitelijk leeg na de header: de body bevat 1 onvolledige zin die mid-woord afbreekt ('22 JUNI 2020. - Koninklijk besluit tot uitvoering van de artikelen 2, derde lid, 2quater en 8, tweede lid, van het'). Layer1 meldt heading_count: 0 en file_size_chars: 207. Het hele bronartefact is corrupt of de extractie heeft gefaald. Geen enkel artikel is geëxtraheerd."
    layer1:
      status: pass
      run_id: 20260513-105636
      run_at: '2026-05-13T10:56:39Z'
      heading_count: 0
      max_section_chars: 207
      file_size_chars: 207
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T11:05:03Z'
      rationale: "Bestand is feitelijk leeg na de header: de body bevat 1 onvolledige zin die mid-woord afbreekt ('22 JUNI 2020. - Koninklijk besluit tot uitvoering van de artikelen 2, derde lid, 2quater en 8, tweede lid, van het'). Layer1 meldt heading_count: 0 en file_size_chars: 207. Het hele bronartefact is corrupt of de extractie heeft gefaald. Geen enkel artikel is geëxtraheerd."
      concrete_problemen:
        - 'Bestand heeft 0 ## Art.-headings — heading_count: 0 in layer1'
        - Body bestaat uit 1 onvolledige zin die mid-woord afbreekt na 'van het'
        - 'file_size_chars: 207 — alle wetsinhoud ontbreekt'
        - 'Bron is daarmee onbruikbaar voor RAG: geen content om te indexeren'
---

# BTW KB 22/06/2020 — E-notariaat

*Bijgewerkt tot en met 2020 — gecoördineerde versie.*

22 JUNI 2020. - Koninklijk besluit tot uitvoering van de artikelen 2, derde lid, 2quater en 8, tweede lid, van het

