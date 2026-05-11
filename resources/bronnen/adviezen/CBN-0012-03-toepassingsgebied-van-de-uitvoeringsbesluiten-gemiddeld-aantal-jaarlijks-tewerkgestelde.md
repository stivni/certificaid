---
nummer: CBN-advies 12/3
datum: 1979-05-01
themas:
  - gemiddeld aantal tewerkgestelde personen
  - omvangcriteria
  - tewerkgestelde personen
  - uitzendkracht
bron: https://www.cbn-cnc.be/nl/adviezen/toepassingsgebied-van-de-uitvoeringsbesluiten-gemiddeld-aantal-jaarlijks-tewerkgestelde
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/toepassingsgebied-van-de-uitvoeringsbesluiten-gemiddeld-aantal-jaarlijks-tewerkgestelde
      sha256: c30b11e8f6ea09cb21a53e7702fb6c211469e2f1ae15a369f21938c195d047ad
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:33:31Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T11:51:19Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "B3: duplicate heading op r44-46 — de H1-titel '# CBN advies 12-3 - Toepassingsgebied van de uitvoeringsbesluiten - Gemiddeld aantal jaarlijks tewerkgestelde personen' staat twee maal achter elkaar. Identiek scraping-artefact als CBN-0007-03. Verder: footnote-formatting r50 heeft ongebruikelijke '[^1] ,[^2]' met spatie voor de komma (minor). Inhoud volledig."
    layer1:
      status: pass
      run_id: 20260511-083333
      run_at:
      heading_count: 0
      max_section_chars: 2379
      file_size_chars: 2379
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T11:51:19Z'
      rationale: "B3: duplicate heading op r44-46 — de H1-titel '# CBN advies 12-3 - Toepassingsgebied van de uitvoeringsbesluiten - Gemiddeld aantal jaarlijks tewerkgestelde personen' staat twee maal achter elkaar. Identiek scraping-artefact als CBN-0007-03. Verder: footnote-formatting r50 heeft ongebruikelijke '[^1] ,[^2]' met spatie voor de komma (minor). Inhoud volledig."
      concrete_problemen:
        - regel: 46
          categorie: B3
          type: other
          voorbeeld: '# CBN advies 12-3 - Toepassingsgebied van de uitvoeringsbesluiten - Gemiddeld... [duplicaat]'
        - regel: 50
          categorie: D4
          type: other
          voorbeeld: koninklijk besluit van 18 oktober 1978[^1] ,[^2].
---

# CBN advies 12-3 - Toepassingsgebied van de uitvoeringsbesluiten - Gemiddeld aantal jaarlijks tewerkgestelde personen

# CBN advies 12-3 - Toepassingsgebied van de uitvoeringsbesluiten - Gemiddeld aantal jaarlijks tewerkgestelde personen

De vraag werd gesteld welk criterium in aanmerking moet genomen worden voor de berekening van het gemiddeld aantal tewerkgestelde personen zoals bedoeld in artikel 12 van de wet van 17 juli 1975 en artikel 39 van het koninklijk besluit van 8 oktober 1976. 

Naar het oordeel van de Commissie is het aangewezen voor de berekening van het gemiddeld aantal tewerkgestelde personen - in overeenstemming met de bedoelingen van de wetgever - aan te leunen bij het koninklijk besluit van 18 oktober 1978 betreffende de ondernemingsraden en de comités voor veiligheid, gezondheid en verfraaiing van de werkplaatsen[^1] ,[^2].

Krachtens artikel 18 van dit besluit van 18 oktober 1978 komen alle werknemers van de onderneming die arbeid verrichten krachtens een arbeidsovereenkomst of een leerovereenkomst in aanmerking voor de berekening van de personeelssterkte van de onderneming. Naar analogie met ditzelfde artikel wordt het gemiddeld aantal tewerkgestelde personen verkregen door het gewone rekenkundige gemiddelde te nemen van het aantal tijdens het jaar tewerkgestelde personen. Dit aantal wordt bekomen door het totaal der gedurende het jaar gepresteerde arbeidsdagen en daarmee gelijkgestelde dagen te delen door het aantal arbeidsdagen in de onderneming. Daarbij wordt elke prestatie, ongeacht de duur ervan, beschouwd als een werkelijke arbeidsdag. 

Indien de onderneming gebruikmaakt van uitzendkrachten, dan moet tevens rekening worden gehouden met de wet van 28 juni 1976 houdende voorlopige regeling van de tijdelijke arbeid, de uitzendarbeid en het ter beschikking stellen van werknemers ten behoeve van gebruikers[^3]. Krachtens artikel 27 van deze wet worden bij de bepaling van het aantal tewerkgestelde personen, zowel in hoofde van de gebruikende onderneming als van het uitzendbureau, de uitzendkrachten meegerekend.

[^1]: Belgisch Staatsblad van 14 november 1978.

[^2]: Dit besluit vervangt grotendeels het koninklijk besluit van 18 februari 1971 tot regeling van de ondernemingsraden, zoals gewijzigd door de koninklijke besluiten van 24 januari 1975 en 8 december 1976.

[^3]: Belgisch Staatsblad van 7 augustus 1976.
