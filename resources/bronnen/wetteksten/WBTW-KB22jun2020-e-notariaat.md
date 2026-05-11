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
  inputs:
    - id: resources/raw/wetteksten/btw-kbs/WBTW-KB22jun2020-e-notariaat.pdf
      sha256: be45dc386b376439de59378c86082c733e467259a0ac3b2762a84ac514054d31
      version: '2020'
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 11f9196
    model:
    prompt_version:
  generated_at: '2026-05-11T16:34:24Z'
  stale: false
  stale_reason:
  trust:
    status: rejected
    confirmed_at: '2026-05-11T16:56:58Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "D2/D1: Het bestand bevat slechts 59 regels en 308 chars. Na de frontmatter en intro-regel staat alleen de onvolledige titel ('22 JUNI 2020. - Koninklijk besluit tot uitvoering van de artikelen 2, derde lid, 2quater en 8, tweede lid, van het') gevolgd door 'Bron : FINANCIEN' — de volledige wettekst ontbreekt. Extractie is structureel mislukt; er is geen bruikbare inhoud."
    layer1:
      file_size_chars: 308
      flags: []
      heading_count: 0
      max_section_chars: 308
      run_at: '2026-05-11T13:40:47Z'
      run_id: 20260511-134044
      status: pass
    layer2:
      status: rejected
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T16:56:58Z'
      rationale: "D2/D1: Het bestand bevat slechts 59 regels en 308 chars. Na de frontmatter en intro-regel staat alleen de onvolledige titel ('22 JUNI 2020. - Koninklijk besluit tot uitvoering van de artikelen 2, derde lid, 2quater en 8, tweede lid, van het') gevolgd door 'Bron : FINANCIEN' — de volledige wettekst ontbreekt. Extractie is structureel mislukt; er is geen bruikbare inhoud."
      concrete_problemen:
        - regel: 56
          categorie: D1
          type: abrupt-cutoff
          voorbeeld: 22 JUNI 2020. - Koninklijk besluit tot uitvoering van de artikelen 2, derde lid, 2quater en 8, tweede lid, van het
        - regel: 0
          categorie: D2
          type: missing-section
          voorbeeld: Bestand bevat 308 chars, 0 headings — volledig ontbrekende wettekst
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
