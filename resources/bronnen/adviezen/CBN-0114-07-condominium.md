---
nummer: CBN-advies 114/7
datum: 1986-07-01
themas:
  - beslissende invloed
  - condominium
  - doorslaggevende invloed
  - joint-venture
  - omvangcriteria
  - verbonden onderneming
bron: https://www.cbn-cnc.be/nl/adviezen/condominium
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/condominium
      sha256: d90e6655287e42fdccee1525db502d4bd176db78351a15ce989959edfddc3211
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:34:21Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T11:57:45Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "A5/B: De H1-heading op regel 46 bevat een en-dash (U+2013) '–' in plaats van een gewone koppelteken '-': '# CBN-advies 114/7 – Condominium'. Alle andere adviezen in de serie gebruiken het gewone koppelteken '-'. Dit is een inconsistente typografie die door de extractor is geïntroduceerd en niet aanwezig is in het bronadvies. De rest van het bestand (één alinea-blok, geen voetnoten) is schoon."
    layer1:
      status: pass
      run_id: 20260511-083333
      run_at:
      heading_count: 0
      max_section_chars: 2196
      file_size_chars: 2196
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T11:57:45Z'
      rationale: "A5/B: De H1-heading op regel 46 bevat een en-dash (U+2013) '–' in plaats van een gewone koppelteken '-': '# CBN-advies 114/7 – Condominium'. Alle andere adviezen in de serie gebruiken het gewone koppelteken '-'. Dit is een inconsistente typografie die door de extractor is geïntroduceerd en niet aanwezig is in het bronadvies. De rest van het bestand (één alinea-blok, geen voetnoten) is schoon."
      concrete_problemen:
        - regel: 46
          categorie: A5
          type: other
          voorbeeld: '# CBN-advies 114/7 – Condominium (en-dash U+2013 i.p.v. gewone koppelteken)'
---

# CBN-advies 114/7 – Condominium

Aan de Commissie werd de vraag gesteld of de berekening op geconsolideerde basis van de criteria voor de kleine en middelgrote ondernemingen, zoals bedoeld in artikel 12, § 2 van het koninklijk besluit van 12 september 1983, van toepassing is op een joint venture, namelijk wanneer twee of meer ondernemingen samen voor een evenredig deel het gehele kapitaal van een andere onderneming bezitten. 

Volgens de bewoordingen van het koninklijk besluit van 8 oktober 1976 waarnaar de betrokken bepaling verwijst, is er sprake van een dochteronderneming «wanneer een andere onderneming, in rechte of in feite, een doorslaggevende invloed kan uitoefenen op de benoeming van ten minste de helft van haar leiders of op de oriëntering van haar beleid, en zulks krachtens overeenkomsten of uit hoofde van gehouden deelnemingen». 

Wanneer twee ondernemingen, elk voor een gelijk deel, het kapitaal van een derde bezitten, mag men veronderstellen dat zij elk afzonderlijk in staat zijn een beslissende invloed uit te oefenen op de benoeming van ten minste de helft van de leiders van deze laatste. De situatie is gelijkaardig wanneer zij elk, rechtstreeks of onrechtstreeks, een zelfde fractie - minder dan 50 % - in het kapitaal bezitten en het resterende deel van de aandelen is verdeeld onder houders die niet in staat zijn een beslissende invloed op de benoeming van de leiders van de onderneming uit te oefenen. Hetzelfde geldt ook nog wanneer beide, hoewel zij qua aandelenbezit geen gelijke fractie bezitten, overeenkomen eenzelfde bevoegdheid uit te oefenen voor de benoeming van deze leiders. 

Wanneer de controle verdeeld is over meer dan twee ondernemingen en geen van hen een beslissende invloed kan uitoefenen op de benoeming van ten minste de helft van de leiders van de betrokken onderneming, kan in de huidige stand van de wetgeving gesteld worden dat het in dit geval niet gaat om dochters en bijgevolg niet om verbonden ondernemingen zodat er geen verplichting bestaat om, voor de toepassing van bovenvermeld artikel 12, § 2, deze ondernemingen met een gedeelde controlebevoegdheid in de berekening van de criteria op geconsolideerde basis op te nemen.
