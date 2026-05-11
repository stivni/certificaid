---
bron: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-leveringontvangst-van-handelsgoederen-om-niet-update-0
datum: 2011-01-12
nummer: CBN-advies 2011/4
provenance:
  generated_at: '2026-05-11T19:17:26Z'
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-leveringontvangst-van-handelsgoederen-om-niet-update-0
      sha256: 72aa22e5a94a24cef31611e115d2507720b175904234b657608a618a50f5119c
      version:
  stale: false
  stale_reason:
  tooling:
    model:
    pipeline: tools/etl/convert.py
    pipeline_version: 11f9196
    prompt_version:
  trust:
    confirmed_at: '2026-05-11T17:09:38Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      status: pass
      run_id: 20260511-191727
      run_at: '2026-05-11T19:17:30Z'
      heading_count: 2
      max_section_chars: 1350
      file_size_chars: 2038
      flags: []
    layer2:
      agent: subagent-sonnet-4-6
      concrete_problemen:
        - categorie: D4
          regel: 61
          type: other
          voorbeeld: '***Voorbeeld***'
        - categorie: D4
          regel: 73
          type: other
          voorbeeld: '***Voorbeeld***'
      rationale: 'D4 bevestigd: r61 en r73 bevatten ''***Voorbeeld***'' (triple asterisk = bold+italic gecombineerd) als sectielabel — ETL-artefact, inconsistent met standaard plain-text label of heading zoals in andere adviezen. Voetnoot [^1] heeft geen body-callout (redactionele noot over publieke consultatie zonder referentie in de body) maar dit is een randgeval met beperkte retrieval-impact. De pipe-tabel en overige inhoud zijn correct.'
      run_at: '2026-05-11T17:09:38Z'
      status: needs-rework
    rationale: 'D4 bevestigd: r61 en r73 bevatten ''***Voorbeeld***'' (triple asterisk = bold+italic gecombineerd) als sectielabel — ETL-artefact, inconsistent met standaard plain-text label of heading zoals in andere adviezen. Voetnoot [^1] heeft geen body-callout (redactionele noot over publieke consultatie zonder referentie in de body) maar dit is een randgeval met beperkte retrieval-impact. De pipe-tabel en overige inhoud zijn correct.'
    status: needs-rework
themas:
  - gratis handelsgoederen
  - levering handelsgoederen om niet
  - ontvangst handelsgoederen om niet
  - Verkrijging om niet
  - voorraad
  - voorraadwijziging
  - aankoopverplichting
---

# CBN-advies 2011/4 - Boekhoudkundige verwerking van levering/ontvangst van handelsgoederen om niet (update)

## Levering van handelsgoederen om niet
Een onderneming die aan een derde handelsgoederen om niet levert, dient in zijn boekhouding weer te geven dat deze goederen zijn voorraad hebben verlaten. 

***Voorbeeld***

Een onderneming levert handelsgoederen ter waarde van 500 euro[^2] gratis aan haar klant. Op inventarisdatum zal de rekening 340 *Handelsgoederen*, via het boeken van de voorraadwijzigingen, voor 500 euro worden beïnvloed. 

De Commissie spreekt zich niet uit over de BTW-implicaties van de levering van goederen om niet.

## Ontvangst van handelsgoederen om niet
De Commissie stelt vast dat er in de praktijk aan de ontvangst van handelsgoederen om niet meestal een aankoopverplichting is verbonden.

De onderneming die, bij aankoop van een welbepaalde hoeveelheid handelsgoederen, handelsgoederen ‘gratis’ ontvangt van zijn leverancier, dient hiervoor geen extra boeking te verrichten.

***Voorbeeld***

Een onderneming ontvangt bij de aankoop van 100 handelsgoederen, 10 stuks ‘gratis’. De prijs per stuk bedraagt 110 euro. De aankoop van 100 stuks dient als volgt te worden ingeschreven:

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 604 | Aankopen van handelsgoederen | 11.000 | |
| aan | 440 | Leveranciers | | 11.000 |

Bij ontvangst van de 10 ‘gratis’ stuks, dient de onderneming geen bijkomende boeking te verrichten. 

Er dient hierbij wel opgemerkt te worden dat de prijs per stuk bij voorraadwaardering 100 euro (11.000 euro/110 stuks) zal bedragen in plaats van 110 euro.

De Commissie spreekt zich evenmin uit over de BTW-implicaties van de ontvangst van goederen om niet.

[^1]: Onderhavig geactualiseerd advies is tot stand gekomen nadat het ontwerpadvies op 8 mei 2025 ter publieke consultatie werd gepubliceerd op de website van de CBN.

[^2]: De waarde van de uitgaande voorraad dient te worden bepaald overeenkomstig artikel 3:21 KB WVV.
