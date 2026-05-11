---
bron: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-leveringontvangst-van-handelsgoederen-om-niet-update-0
datum: 2011-01-12
nummer: CBN-advies 2011/4
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-leveringontvangst-van-handelsgoederen-om-niet-update-0
      sha256: 72aa22e5a94a24cef31611e115d2507720b175904234b657608a618a50f5119c
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-11T13:15:11Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T13:23:04Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Regels 61 en 73: 'Voorbeeld'-labels zijn opgemaakt als ***Voorbeeld*** (bold+italic gecombineerd via triple asterisk) in plaats van een heading of consistente inline-stijl (D4/stijlinconsistentie tov overige adviezen die ## of plain 'Voorbeeld' gebruiken). Voetnoot [^1] is gedefinieerd (redactionele noot over publieke consultatie) maar heeft geen body-referentie — dit is acceptabel als redactionele annotatie maar het ontbreken van een [^1]-callout in de body is onconventioneel. Verder is het advies correct en volledig."
    layer1:
      status: pass
      run_id: 20260511-131513
      run_at: '2026-05-11T13:15:16Z'
      heading_count: 2
      max_section_chars: 1351
      file_size_chars: 2041
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T13:23:04Z'
      rationale: "Regels 61 en 73: 'Voorbeeld'-labels zijn opgemaakt als ***Voorbeeld*** (bold+italic gecombineerd via triple asterisk) in plaats van een heading of consistente inline-stijl (D4/stijlinconsistentie tov overige adviezen die ## of plain 'Voorbeeld' gebruiken). Voetnoot [^1] is gedefinieerd (redactionele noot over publieke consultatie) maar heeft geen body-referentie — dit is acceptabel als redactionele annotatie maar het ontbreken van een [^1]-callout in de body is onconventioneel. Verder is het advies correct en volledig."
      concrete_problemen:
        - regel: 61
          categorie: D4
          type: other
          voorbeeld: '***Voorbeeld***'
        - regel: 73
          categorie: D4
          type: other
          voorbeeld: '***Voorbeeld***'
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
