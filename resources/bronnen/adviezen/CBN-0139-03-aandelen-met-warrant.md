---
nummer: CBN-advies 139/3
datum: 1988-06-01
themas:
  - geen inhoud
bron: https://www.cbn-cnc.be/nl/adviezen/aandelen-met-warrant
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/aandelen-met-warrant
      sha256: 6a6e46b69fc6c00e8d3e61bcaeb496d426ca91783f92453b11e42afa4a32aed3
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:35:05Z'
  stale: false
  stale_reason:
  trust:
    status: rejected
    confirmed_at: '2026-05-11T12:04:41Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "D2: het advies bevat vrijwel geen inhoud — één verwijzingszin naar advies 139/1. Themas-veld in frontmatter bevat 'geen inhoud' wat bevestigt dat de scraper niets relevants kon ophalen. Dit bestand is als standalone RAG-chunk onbruikbaar: het mist context (139/1 wordt niet geciteerd) en levert geen zelfstandige informatie op."
    layer1:
      status: pass
      run_id: 20260511-083333
      run_at:
      heading_count: 0
      max_section_chars: 149
      file_size_chars: 149
      flags: []
    layer2:
      status: rejected
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T12:04:41Z'
      rationale: "D2: het advies bevat vrijwel geen inhoud — één verwijzingszin naar advies 139/1. Themas-veld in frontmatter bevat 'geen inhoud' wat bevestigt dat de scraper niets relevants kon ophalen. Dit bestand is als standalone RAG-chunk onbruikbaar: het mist context (139/1 wordt niet geciteerd) en levert geen zelfstandige informatie op."
      concrete_problemen:
        - regel: 5
          categorie: F1
          type: other
          voorbeeld: '- geen inhoud'
        - regel: 56
          categorie: D2
          type: abrupt-cutoff
          voorbeeld: Voor aandelen met warrant zijn de beginselen verwoord in voornoemd advies 139/1 volledig van toepassing.
gerelateerde_adviezen:
  - titel: Terugbetaling van kapitaal in vreemde valuta aan de aandeelhouders
    url: https://www.cbn-cnc.be/nl/adviezen/terugbetaling-van-kapitaal-in-vreemde-valuta-aan-de-aandeelhouders
    datum: '2024-03-13'
  - titel: Dividenduitkering en kapitaalvermindering in natura
    url: https://www.cbn-cnc.be/nl/adviezen/dividenduitkering-en-kapitaalvermindering-in-natura-0
    datum: '2019-03-12'
  - titel: 'Verenigingen en stichtingen: certificatie van aandelen van handelsvennootschappen'
    url: https://www.cbn-cnc.be/nl/adviezen/verenigingen-en-stichtingen-certificatie-van-aandelen-van-handelsvennootschappen
    datum: '2016-09-07'
  - titel: Verrichtingen met betrekking tot inschrijvingsrechten
    url: https://www.cbn-cnc.be/nl/adviezen/verrichtingen-met-betrekking-tot-inschrijvingsrechten
    datum: '2016-03-09'
---

# CBN-advies 139/3 - Aandelen met warrant

Voor aandelen met warrant zijn de beginselen verwoord in voornoemd advies 139/1 volledig van toepassing.
