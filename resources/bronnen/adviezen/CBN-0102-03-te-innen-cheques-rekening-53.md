---
nummer: CBN-advies R102/3
datum: 1980-06-01
themas:
  - cheque
  - kredietinstelling
  - liquide middelen
  - ontvangen cheques
  - rekeningenstelsel
  - te innen cheque
bron: https://www.cbn-cnc.be/nl/adviezen/te-innen-cheques-rekening-53
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/te-innen-cheques-rekening-53
      sha256: 12b8080766e2af5298adf3b6eb47536b6f89ad40b946bb4389913aacb249e578
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:33:41Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T11:51:19Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "D4: op regel 52 staat '*Kredietinstellingen *' — de sluitende asterisk heeft een spatie vóór zich waardoor de italic niet correct sluit in de meeste markdown-parsers ('rekening *Kredietinstellingen *zodra'). Verder is het advies erg kort maar volledig."
    layer1:
      status: pass
      run_id: 20260511-083333
      run_at:
      heading_count: 0
      max_section_chars: 497
      file_size_chars: 497
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T11:51:19Z'
      rationale: "D4: op regel 52 staat '*Kredietinstellingen *' — de sluitende asterisk heeft een spatie vóór zich waardoor de italic niet correct sluit in de meeste markdown-parsers ('rekening *Kredietinstellingen *zodra'). Verder is het advies erg kort maar volledig."
      concrete_problemen:
        - regel: 52
          categorie: D4
          type: other
          voorbeeld: rekening *Kredietinstellingen *zodra het krediet werd verleend
gerelateerde_adviezen:
  - titel: 'Uitgegeven cheques : werking van rekening 559'
    url: https://www.cbn-cnc.be/nl/adviezen/uitgegeven-cheques-werking-van-rekening-559
    datum: '1980-06-01'
---

# CBN-advies R102/3 - Te innen cheques : rekening 53

Ontvangen cheques en andere ontvangen betaalmiddelen moeten op het ogenblik waarop zij worden ontvangen, worden geboekt op de rekening 53 *Te innen vervallen waarden* in afwachting van hun inning. Als de financiële instelling die met de inning belast is dadelijk krediet verleent, onder voorbehoud van goede afloop, dan wordt het bedrag van de betrokken "waarden" geboekt in de rekening *Kredietinstellingen *zodra het krediet werd verleend.
