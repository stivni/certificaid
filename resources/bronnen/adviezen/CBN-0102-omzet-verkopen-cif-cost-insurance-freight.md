---
nummer: CBN-advies 102
datum: 1977-08-01
themas:
  - CIF
  - concordantietabel
  - continuïteit
  - continuïteitsgedachte
  - eerste boekjaar
  - omzet
  - vergelijkende cijfers
  - verkopen CIF (Cost, Insurance, Freight)
bron: https://www.cbn-cnc.be/nl/adviezen/omzet-verkopen-cif-cost-insurance-freight
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/omzet-verkopen-cif-cost-insurance-freight
      sha256: db7fa26a1d8463a7affca192233a4ce68cd7dbdc66641feada8969f7ba9e955d
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:33:42Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T11:51:19Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "B3: de hoofd-heading is gedupliceerd op regels 48 en 50 ('# CBN advies 102 - Omzet - Verkopen CIF (Cost, Insurance, Freight)' twee keer) — zelfde scraping-patroon als CBN-0100-omzet-begrip. Inhoudelijk verder volledig."
    layer1:
      status: pass
      run_id: 20260511-083333
      run_at:
      heading_count: 0
      max_section_chars: 517
      file_size_chars: 517
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T11:51:19Z'
      rationale: "B3: de hoofd-heading is gedupliceerd op regels 48 en 50 ('# CBN advies 102 - Omzet - Verkopen CIF (Cost, Insurance, Freight)' twee keer) — zelfde scraping-patroon als CBN-0100-omzet-begrip. Inhoudelijk verder volledig."
      concrete_problemen:
        - regel: 50
          categorie: B3
          type: other
          voorbeeld: '# CBN advies 102 - Omzet - Verkopen CIF (Cost, Insurance, Freight) (duplicate van regel 48)'
---

# CBN advies 102 - Omzet - Verkopen CIF (Cost, Insurance, Freight)

# CBN advies 102 - Omzet - Verkopen CIF (Cost, Insurance, Freight)

In geval van verkoop C.I.F. omvat de aan de koper gerekende prijs, naast de verkoopprijs F.O.B., onder meer de kosten voor vervoer en verzekering; deze laatste worden door de verkoper echter voor eigen rekening aangegaan. 

Daaruit volgt dat, in dit geval, de omzet de totale aan de koper gerekende prijs omvat, dat wil zeggen zonder aftrek van de vervoer- en verzekeringskosten.
