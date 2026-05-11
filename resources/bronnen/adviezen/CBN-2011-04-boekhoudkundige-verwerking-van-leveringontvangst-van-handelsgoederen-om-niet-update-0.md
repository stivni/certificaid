---
nummer: CBN-advies 2011/4
datum: 2011-01-12
themas:
  - gratis handelsgoederen
  - levering handelsgoederen om niet
  - ontvangst handelsgoederen om niet
  - Verkrijging om niet
  - voorraad
  - voorraadwijziging
  - aankoopverplichting
bron: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-leveringontvangst-van-handelsgoederen-om-niet-update-0
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-leveringontvangst-van-handelsgoederen-om-niet-update-0
      sha256: 72aa22e5a94a24cef31611e115d2507720b175904234b657608a618a50f5119c
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:36:08Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T12:09:18Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Regel 53: '***Voorbeeld***' gebruikt drievoudige asterisk (bold+italic gecombineerd) terwijl regel 66 hetzelfde patroon herhaalt. Dit is een inconsistentie tov de andere adviezen die '*Voorbeeld*' of '*Voorbeeld' gebruiken (D4/stijl-inconsistentie). Anderzijds is dit een zeer kort advies (2042 chars) met slechts twee headings en één tabel — laag 1 meldt heading_count 2 wat klopt. Voetnoot [^1] is gedefinieerd maar er is geen [^1]-referentie in de body (de footnote is een redactionele noot over de publieke consultatie, wat in orde is). Toch wijst het triple-asterisk patroon op een ETL-stijlinconsistentie ten opzichte van de rest van de batch."
    layer1:
      status: pass
      run_id: 20260511-083333
      run_at:
      heading_count: 2
      max_section_chars: 1351
      file_size_chars: 2042
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T12:09:18Z'
      rationale: "Regel 53: '***Voorbeeld***' gebruikt drievoudige asterisk (bold+italic gecombineerd) terwijl regel 66 hetzelfde patroon herhaalt. Dit is een inconsistentie tov de andere adviezen die '*Voorbeeld*' of '*Voorbeeld' gebruiken (D4/stijl-inconsistentie). Anderzijds is dit een zeer kort advies (2042 chars) met slechts twee headings en één tabel — laag 1 meldt heading_count 2 wat klopt. Voetnoot [^1] is gedefinieerd maar er is geen [^1]-referentie in de body (de footnote is een redactionele noot over de publieke consultatie, wat in orde is). Toch wijst het triple-asterisk patroon op een ETL-stijlinconsistentie ten opzichte van de rest van de batch."
      concrete_problemen:
        - regel: 53
          categorie: D4
          type: other
          voorbeeld: '***Voorbeeld***'
        - regel: 66
          categorie: D4
          type: other
          voorbeeld: '***Voorbeeld***'
---

# CBN-advies 2011/4 - Boekhoudkundige verwerking van levering/ontvangst van handelsgoederen om niet (update)

## Levering van handelsgoederen om niet

Een onderneming die aan een derde handelsgoederen om niet levert, dient in zijn boekhouding weer te geven dat deze goederen zijn voorraad hebben verlaten. 

***Voorbeeld***

Een onderneming levert handelsgoederen ter waarde van 500 euro[^2]
 gratis aan haar klant. Op inventarisdatum zal de rekening 340 *Handelsgoederen*, via het boeken van de voorraadwijzigingen, voor 500 euro worden beïnvloed. 

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
