---
bron: https://www.cbn-cnc.be/nl/adviezen/zakelijke-waarborgen-gesteld-voor-rekening-van-derden
datum: 1980-06-01
gerelateerde_adviezen:
  - datum: '2021-05-12'
    titel: Invloed van het buitengerechtelijk minnelijk akkoord en de gerechtelijke reorganisatie op de schulden en vorderingen (update)
    url: https://www.cbn-cnc.be/nl/adviezen/invloed-van-het-buitengerechtelijk-minnelijk-akkoord-en-de-gerechtelijke-reorganisatie-1
  - datum: '2020-12-11'
    titel: Boekhoudkundige verwerking van de aan-/verkoop van een actief via een geblokkeerde rekening
    url: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-de-aan-verkoop-van-een-actief-via-een-geblokkeerde-0
  - datum: '2018-11-16'
    titel: Schulden gewaarborgd door een zakelijke zekerheid – Niet in de balans opgenomen rechten en verplichtingen
    url: https://www.cbn-cnc.be/nl/adviezen/schulden-gewaarborgd-door-een-zakelijke-zekerheid-niet-in-de-balans-opgenomen-rechten-en
  - datum: '2018-05-09'
    titel: Gebeurtenissen na afsluitingsdatum van het boekjaar
    url: https://www.cbn-cnc.be/nl/adviezen/gebeurtenissen-na-afsluitingsdatum-van-het-boekjaar
nummer: CBN-advies R101/1
provenance:
  generated_at: '2026-05-11T13:05:05Z'
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/zakelijke-waarborgen-gesteld-voor-rekening-van-derden
      sha256: dd346a1d84ea751247cf3d70d6316785147f7a5e680b36ea1ceb22e549ac5e51
      version:
  stale: false
  stale_reason:
  tooling:
    model:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    prompt_version:
  trust:
    confirmed_at: '2026-05-11T11:51:19Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      status: pass
      run_id: 20260511-130524
      run_at: '2026-05-11T13:05:24Z'
      heading_count: 0
      max_section_chars: 3525
      file_size_chars: 3525
      flags: []
    layer2:
      agent: subagent-sonnet-4-6
      concrete_problemen:
        - categorie: E2
          regel: 66
          type: pseudo-table
          voorbeeld: '| 01 | | Waarborgen gesteld voor rekening van derden | (3 cols vs 5 cols sub-rijen)'
        - categorie: D3
          regel: 82
          type: other
          voorbeeld: '[^2] en [^3] identieke tekst, enkel ''cfr.'' vs ''cf.'' verschil — duplicate scrape'
      rationale: 'E2: de twee pipe-tabellen (regels 66-68 en 70-72) hebben inconsistente kolomaantallen — de ''moeder''-rijen hebben 3 kolommen (4 pipes) terwijl de ''kind''-rijen 5 kolommen hebben (6 pipes). Dit rendert als gebroken tabel in elke markdown-parser. D3: voetnoot [^2] en [^3] zijn inhoudelijk bijna identiek (duplicaat tekst, alleen kleine stijlverschillen), wat wijst op een scraping-artefact waarbij dezelfde noot tweemaal werd gevangen.'
      run_at: '2026-05-11T11:51:19Z'
      status: needs-rework
    rationale: 'E2: de twee pipe-tabellen (regels 66-68 en 70-72) hebben inconsistente kolomaantallen — de ''moeder''-rijen hebben 3 kolommen (4 pipes) terwijl de ''kind''-rijen 5 kolommen hebben (6 pipes). Dit rendert als gebroken tabel in elke markdown-parser. D3: voetnoot [^2] en [^3] zijn inhoudelijk bijna identiek (duplicaat tekst, alleen kleine stijlverschillen), wat wijst op een scraping-artefact waarbij dezelfde noot tweemaal werd gevangen.'
    status: needs-rework
themas:
  - niet in de balans opgenomen rechten en verplichtingen
  - rekeningenstelsel
  - waarborg
  - waarborgen gesteld voor rekening van derden
  - zakelijke waarborgen
  - zakelijke waarborgen gesteld op eigen tegoeden
  - zakelijke waarborgen gesteld voor rekening van derden
  - zakelijke zekerheden
  - zekerheden
---

# CBN-advies R101/1 - Zakelijke waarborgen gesteld voor rekening van derden

Indien een onderneming haar eigen bezittingen bezwaart met een zakelijke zekerheid voor rekening van een derde dan wordt dit in het minimum genormaliseerd rekeningstelsel uitgedrukt in een dubbel stel rekeningen:

| 01 | | Waarborgen gesteld voor rekening van derden | 
| | | 014 | | Debiteuren wegens zakelijke zekerheden | 
| | | 015 | | Crediteuren wegens zakelijke zekerheden | 

| 02 | | Zakelijke waarborgen gesteld op eigen tegoeden | 
| | | 022 | | Crediteuren van derden, houders van zakelijke waarborgen[^1] | 
| | | 023 | | Zakelijke waarborgen gesteld voor rekening van derden[^2] | 

Verschillende vragen werden gesteld over de juiste werking van deze rekeningen en meer bepaald over het verband tussen rekening 015 en de rekening 022.

De boekingen waarin het rekeningstelsel voorziet voor het geval waarin door de onderneming zakelijke zekerheden werden gesteld voor rekening van derden drukken in feite twee afzonderlijke aspecten uit van één en dezelfde rechtshandeling : enerzijds de band tussen de potentiële schulden en vorderingen (014 en 015), anderzijds de toestand van gebondenheid waarin de goederen, die eigendom zijn van de onderneming, zich bevinden als gevolg van het feit dat ze met een zakelijke zekerheid werden bezwaard (022 en 023). In het eerste stel rekeningen (014 en 015) wordt de nadruk gelegd op de door de onderneming aangegane verplichting (uitgedrukt door de rekening 015). Het verhaalrecht tegen de derde voor wiens rekening de zekerheid werd gesteld (uitgedrukt door de rekening 014) hangt rechtstreeks af van deze verplichting. In het tweede stel rekeningen (022 en 023) valt de nadruk op de bezwaarde activa zelf (023). De begunstigde van de waarborg wordt aangeduid door de rekening 022[^3]. Deze boekingen geven aan wat er zou gebeuren indien als gevolg van het ingebreke blijven van de derde voor wiens rekening de waarborg werd gesteld de onderneming die de waarborg heeft gesteld de tegeldemaking van de activa waarop de waarborg betrekking heeft zou moeten ondergaan ten voordele van de schuldeiser van de derde, die nu zelf schuldeiser is geworden van de onderneming. 

Deze dubbele benadering maakt het ook mogelijk een onderscheid te maken tussen twee bedragen die in de meeste gevallen verschillend zijn : enerzijds, het bedrag van de gewaarborgde schuld of het maximumbedrag waarvoor de schuld is gewaarborgd en anderzijds, de boekwaarde van de activa die met een zakelijke zekerheid werden bezwaard.

[^1]: Tekst zoals hij luidt na verbetering door het erratum, gepubliceerd in het Belgisch Staatsblad van 10 november 1978.

[^2]: Vermits rekening 022 in zekere mate een dubbel gebruik vormt met rekening 015, legt het besluit geen verplichting op om voor de op deze rekening geboekte bedragen, in tegenstelling tot hetgeen is bepaald door rekening 015, een onderscheid door te voeren volgens de verschillende categorieën van schuldeisers (cfr. a contrario het tweede lid van de definitie van de rubriek 02 Zakelijke waarborgen gestelde op eigen tegoeden).

[^3]: Vermits rekening 022 in zekere mate een dubbel gebruik vormt met rekening 015, legt het besluit geen verplichting op om voor de op deze rekening geboekte bedragen, in tegenstelling tot hetgeen is bepaald door rekening 015, een onderscheid door te voeren volgens de verschillende categorieën van schuldeisers (cf. a contrario het tweede lid van de definitie van de rubriek 02 Zakelijke waarborgen gesteld op eigen tegoeden).
