---
bron: https://www.cbn-cnc.be/nl/adviezen/aanrekening-van-vergoedingen-van-beheerders-of-leden-van-het-personeel-toegekend-door-0
datum: 1977-08-01
nummer: CBN-advies 105-5
provenance:
  generated_at: '2026-05-11T17:48:38Z'
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/aanrekening-van-vergoedingen-van-beheerders-of-leden-van-het-personeel-toegekend-door-0
      sha256: 1be95bcf721b9668f270171df616a7e70c5338c8a49feb9bd492179f2356a47d
      version:
  stale: false
  stale_reason:
  tooling:
    model:
    pipeline: tools/etl/convert.py
    pipeline_version: 11f9196
    prompt_version:
  trust:
    confirmed_at: '2026-05-11T17:05:20Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      status: pass
      run_id: 20260511-174840
      run_at: '2026-05-11T17:48:40Z'
      heading_count: 0
      max_section_chars: 1623
      file_size_chars: 1623
      flags: []
    layer2:
      agent: subagent-sonnet-4-6
      concrete_problemen:
        - categorie: F1
          regel: 4
          type: naam-mismatch
          voorbeeld: 'nummer: CBN-advies 105-5 (frontmatter, koppelteken) vs # CBN-advies 105/5 (body, schuine streep)'
      rationale: 'F1: frontmatter-veld ''nummer'' bevat ''CBN-advies 105-5'' (koppelteken) terwijl de body-heading op regel 52 ''CBN-advies 105/5'' schrijft (schuine streep) — de schuine streep is de correcte advies-notatie; de scraper heeft de URL-slug-hyphen overgenomen in het nummer-veld, wat een ETL-normaliseringsflout is. Body-tekst is clean en volledig.'
      run_at: '2026-05-11T17:05:20Z'
      status: needs-rework
    rationale: 'F1: frontmatter-veld ''nummer'' bevat ''CBN-advies 105-5'' (koppelteken) terwijl de body-heading op regel 52 ''CBN-advies 105/5'' schrijft (schuine streep) — de schuine streep is de correcte advies-notatie; de scraper heeft de URL-slug-hyphen overgenomen in het nummer-veld, wat een ETL-normaliseringsflout is. Body-tekst is clean en volledig.'
    status: needs-rework
themas:
  - vennootschap behorende tot dezelfde groep
  - aanrekening van vergoedingen door vennootschappen behorende tot dezelfde groep
  - beheerder
  - compensatie
---

# CBN-advies 105/5 - Aanrekening van vergoedingen, van beheerders of leden van het personeel toegekend door vennootschappen behorende tot dezelfde groep

Het gebeurt vaak dat beheerders of leden van het personeel van een onderneming functies vervullen bij vennootschappen behorend tot dezelfde groep; de daaraan verbonden vergoeding wordt dan vaak ofwel aangerekend op de vergoeding voor de hoofdfunctie uitgeoefend op het vlak van de onderneming ofwel rechtstreeks betaald aan deze onderneming of terugbetaald aan deze onderneming door de beneficiaris. 

De Commissie is van mening dat wanneer de door de vennootschap van dezelfde groep uitgekeerde vergoeding eenvoudig wordt aangerekend, alleen het complementaire bedrag betaald door de onderneming door deze laatste moet worden vermeld als eigen kosten. Daarentegen, wanneer er een werkelijke storting is of wanneer er een terugstorting is van de vergoeding aan de onderneming, dan moet de uitgeoefende functie bij de andere vennootschap beschouwd worden als verricht voor rekening van de onderneming en moet de daaraan verbonden vergoeding behandeld worden als een eigen opbrengst voor deze laatste. De vergoeding mag dan ook niet in mindering worden gebracht van het bedrag van de door de onderneming uitgekeerde bezoldigingen. 

Wat de reisonkosten van de beheerders of leden van het personeel betreft, uitgekeerd door de onderneming maar terugbetaald door de andere vennootschappen, deze uitkeringen kunnen worden beschouwd als een voorschot en niet als een kost indien bewezen is dat de reisonkosten werden aangegaan voor rekening van deze andere vennootschappen.
