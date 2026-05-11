---
bron: https://www.cbn-cnc.be/nl/adviezen/gegeven-borgtochten-in-contanten-en-effecten-update
datum: 2017-02-01
nummer: CBN-advies 2017/04
provenance:
  generated_at: '2026-05-11T13:05:08Z'
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/gegeven-borgtochten-in-contanten-en-effecten-update
      sha256: 43a9e497b9a01bd3cd9f1045f41cc40ead351e4b7b5c88168b7d0b195b380ac5
      version:
  stale: false
  stale_reason:
  tooling:
    model:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    prompt_version:
  trust:
    confirmed_at: '2026-05-11T12:16:34Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      status: pass
      run_id: 20260511-130524
      run_at: '2026-05-11T13:05:29Z'
      heading_count: 2
      max_section_chars: 1989
      file_size_chars: 2566
      flags: []
    layer2:
      agent: subagent-sonnet-4-6
      concrete_problemen:
        - categorie: A6
          regel: 47
          type: other
          voorbeeld: ', bijgewerkt op 10 september 2025[^2]'
        - categorie: D4
          regel: 60
          type: other
          voorbeeld: rekening 418 *Borgtochten betaald in contanten *corresponderen
        - categorie: D4
          regel: 62
          type: other
          voorbeeld: Op de rekening 288 *Borgtochten betaald in contanten *en 418 *Borgtochten betaald in
      rationale: 'D4: Meerdere malformed italics — spatie vóór het sluitende asterisk: ''*Borgtochten betaald in contanten *'' (regel 60 en 62) en ''*Borgtochten betaald in contanten *'' (regel 62). Dit is een gekend PDF-extractiepatroon waarbij spaties rond cursief-markering niet correct worden gesloten. Verder staat '', bijgewerkt op 10 september 2025[^2]'' als los fragment na H1 (regel 47).'
      run_at: '2026-05-11T12:16:34Z'
      status: needs-rework
    rationale: 'D4: Meerdere malformed italics — spatie vóór het sluitende asterisk: ''*Borgtochten betaald in contanten *'' (regel 60 en 62) en ''*Borgtochten betaald in contanten *'' (regel 62). Dit is een gekend PDF-extractiepatroon waarbij spaties rond cursief-markering niet correct worden gesloten. Verder staat '', bijgewerkt op 10 september 2025[^2]'' als los fragment na H1 (regel 47).'
    status: needs-rework
themas:
  - borgtochten
  - borgtochten in contanten
  - borgtochten in effecten
  - waarborgen
  - financiële vaste activa
---

# CBN-advies 2017/04 – Gegeven borgtochten in contanten en effecten (update)

, bijgewerkt op 10 september 2025[^2]

## Inleiding

Aan de Commissie werd de vraag gesteld op welke rekening van het algemeen rekeningstelsel een borgverstrekker een gegeven borgtocht in effecten boekhoudkundig dient te registreren.

Daarnaast werd tevens de zienswijze van de Commissie gevraagd omtrent de boekhoudkundige verwerking van interesten[^3] met betrekking tot een geboekte borg op rekening 288 *Borgtochten betaald in contanten* en 418 *Borgtochten betaald in contanten*.

## Conclusie

In artikel 3:89 van het koninklijk besluit tot uitvoering van het Wetboek van vennootschappen en verenigingen wordt bepaald dat borgtochten dienen te worden opgenomen als deel van de financiële vaste activa indien deze borgtochten worden gestort als doorlopende waarborg. Dit impliceert dat ze duurzaam worden aangehouden.

Daarnaast, indien een borg vervalt binnen de 12 maanden lijkt het aangewezen het op te nemen op de rekening 418 *Borgtochten betaald in contanten*. De rekeningen 750* Opbrengsten uit financiële vaste activa* en 751 *Opbrengsten uit vlottende activa* corresponderen respectievelijk met de rekeningen 288 *Borgtochten betaald in contanten* en 418 *Borgtochten betaald in contanten* voor de verwerking van eventuele financiële opbrengsten (interesten of dividenden).

Op de rekening 288 *Borgtochten betaald in contanten* en 418 *Borgtochten betaald in contanten* kunnen enkel, op basis van de omschrijving, borgtochten worden opgenomen die afgewikkeld worden in contanten (m.a.w. in cash). Het lijkt de Commissie niet aangewezen om een aparte rubriek te voorzien voor borgtochten die worden afgewikkeld in bijvoorbeeld effecten; vandaar zal de Commissie op een gepast ogenblik aan de Regering voorstellen om de omschrijving van de rekeningen 288 *Borgtochten betaald in contanten* en 418 *Borgtochten betaald in contanten* op passende wijze aan te passen. Borgverstrekkers die reeds op heden worden geconfronteerd met de problematiek van gegeven borgtochten in effecten kunnen hiervoor de rekeningen 288 en 418 gebruiken.

[^1]: Onderhavig advies is tot stand gekomen nadat het ontwerp van dit advies op 28 november 2016 ter publieke consultatie werd gepubliceerd op de website van de CBN.

[^2]: Onderhavig geactualiseerd advies is tot stand gekomen nadat het ontwerpadvies op 8 mei 2025 ter publieke consultatie werd gepubliceerd op de website van de CBN.

[^3]: In het geval van een borgtocht gegeven in effecten zal er sprake zijn van dividenden of interesten.
