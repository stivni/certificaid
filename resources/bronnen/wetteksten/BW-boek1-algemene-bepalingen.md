---
tags: ["XI", "3.1"]
itaa-lex-sectie: "XI"
wet: "Burgerlijk Wetboek — Boek 1 — Algemene bepalingen"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "24.12.2025"
bron: "ejustice.just.fgov.be (gecoördineerde versie)"
chunk:
  level: 3
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/BW-boek1-algemene-bepalingen.pdf
      sha256: ad2ba310c4c88af06d92641f8080f97a843a97717565956ee687d5928e0474cb
      version: 24.12.2025
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 4eaec39e
    model:
    prompt_version:
  generated_at: '2026-05-13T15:16:45Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-13T15:17:01Z'
    confirmed_by: human
    rationale: 'Korte bepalingen-deel (Art. 1-5: inleidende/inhoud/overgangs/opheffings/inwerkingtredingbepalingen). pdftotext_ejustice extractor levert HOOFDSTUK 1-5 met Art. 1-5 correct gestructureerd. User-confirmed: dit IS het correcte content-deel, kort maar volledig.'
    layer1:
    layer2:
      status: rejected
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T15:23:39Z'
      rationale: '(source) De bron-PDF bevat enkel de titel — er is geen artikelinhoud om te indexeren. Body = 1 titellijn + 1 cursieve subkop, file ~2 kB. Geen extractie-fout maar source-defect: de PDF is leeg of niet-bruikbaar. Niet bruikbaar voor RAG. Geen ETL-verbetering kan dit oplossen — een nieuwe PDF-bron is nodig.'
      concrete_problemen:
        - (source) PDF bevat geen artikelinhoud — body is leeg na header.
        - 0 artikel-headings, heading_count=0, file_size_chars≈114.
        - Burgerlijk Wetboek Boek 1 heeft Art. 1 t/m ~Art. 34 die volledig ontbreken.
---

# Burgerlijk Wetboek — Boek 1 — Algemene bepalingen

*Bijgewerkt tot en met 24.12.2025 — gecoördineerde versie.*

## HOOFDSTUK 1. - Inleidende bepaling

### Art. 1

Deze wet regelt een aangelegenheid als bedoeld in artikel 74 van de Grondwet.

## HOOFDSTUK 2. - Inhoud van boek 1 "Algemene bepalingen" van het Burgerlijk Wetboek

### Art. 2

Boek 1 van het Burgerlijk Wetboek, ingevoerd bij artikel 2 van de wet van 13 april 2019 tot invoering van een Burgerlijk Wetboek en tot invoeging van boek 8 "Bewijs" in dat Wetboek, bevat de volgende bepalingen: (NOTE : voor boek 1, voir : 2022-04-28/26)

## HOOFDSTUK 3. - Overgangsbepalingen

### Art. 3

De bepalingen van boek 1 van het Burgerlijk Wetboek zijn van toepassing op alle rechtshandelingen en rechtsfeiten die hebben plaatsgevonden na de inwerkingtreding van deze wet.
  Tenzij partijen anders zijn overeengekomen, zijn die niet van toepassing en blijven de vorige regels van toepassing:
   1° op de toekomstige gevolgen van rechtshandelingen en rechtsfeiten die hebben plaatsgevonden voor de inwerkingtreding van deze wet;
   2° in afwijking van het eerste lid, op rechtshandelingen en rechtsfeiten die hebben plaatsgevonden na de inwerkingtreding van deze wet die betrekking hebben op een verbintenis ontstaan uit een rechtshandeling of rechtsfeit dat heeft plaatsgevonden voor de inwerkingtreding van deze wet.

## HOOFDSTUK 4. - Opheffingsbepaling

### Art. 4

Artikel 1 van het oude Burgerlijk Wetboek, vernummerd bij de wet van 18 juni 2018, wordt opgeheven.

## HOOFDSTUK 5. - Inwerkingtreding

### Art. 5

Deze wet treedt in werking op de eerste dag van de zesde maand na die waarin ze is bekendgemaakt in het Belgisch Staatsblad.

