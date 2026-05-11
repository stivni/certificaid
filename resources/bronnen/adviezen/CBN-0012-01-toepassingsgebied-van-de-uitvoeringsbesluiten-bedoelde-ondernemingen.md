---
nummer: CBN-advies 12/1
datum: 1977-12-01
themas:
  - uitvoerend beslag
bron: https://www.cbn-cnc.be/nl/adviezen/toepassingsgebied-van-de-uitvoeringsbesluiten-bedoelde-ondernemingen
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/toepassingsgebied-van-de-uitvoeringsbesluiten-bedoelde-ondernemingen
      sha256: 851f88bac6c753745e09aeeb0d2dfef6363d5a0d13cf668f0cbfe5140d3098c9
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:33:30Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T11:51:19Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "A6: de zin 'In zijn antwoord op een parlementaire vraag[^1]\\n  over de al dan niet cumulatieve aard...' is gesplitst over twee regels door een harde newline na de footnote-referentie (r51-52). Dit breekt de zin midden in de verwijzing. Verder: spelfout 'oger' (r49, moet zijn 'hoger') en A4: 4 gevallen U+2010 HYPHEN in r47 en r54. Inhoud correct maar structureel beïnvloed door de split-zin."
    layer1:
      status: pass
      run_id: 20260511-083333
      run_at:
      heading_count: 0
      max_section_chars: 1711
      file_size_chars: 1711
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T11:51:19Z'
      rationale: "A6: de zin 'In zijn antwoord op een parlementaire vraag[^1]\\n  over de al dan niet cumulatieve aard...' is gesplitst over twee regels door een harde newline na de footnote-referentie (r51-52). Dit breekt de zin midden in de verwijzing. Verder: spelfout 'oger' (r49, moet zijn 'hoger') en A4: 4 gevallen U+2010 HYPHEN in r47 en r54. Inhoud correct maar structureel beïnvloed door de split-zin."
      concrete_problemen:
        - regel: 51
          categorie: A6
          type: other
          voorbeeld: parlementaire vraag[^1]\n  over de al dan niet cumulatieve
        - regel: 49
          categorie: D1
          type: other
          voorbeeld: en het totaal van hun balans bij het einde van het boekjaar niet oger
        - regel: 47
          categorie: A4
          type: other
          voorbeeld: bulletin 1‐24 augustus 1977‐september 1989
gerelateerde_adviezen:
  - titel: De boekhoudkundige verwerking van de inbeslagname in hoofde van de beslagen schuldenaar
    url: https://www.cbn-cnc.be/nl/adviezen/de-boekhoudkundige-verwerking-van-de-inbeslagname-in-hoofde-van-de-beslagen-schuldenaar
    datum: '2012-01-11'
---

# CBN-advies 12-1 - Toepassingsgebied van de uitvoeringsbesluiten: bedoelde ondernemingen

Dit advies is verouderd gezien het nieuwe artikel 12 van de wet 17 juli 1975 (artikel 8 van de wet van 1 juli 1983) (zie lijst van gepubliceerde adviezen, bulletin 1‐24 augustus 1977‐september 1989)

Luidens artikel 12 van de wet van 17 juli 1975 zijn de besluiten genomen ter uitvoering van artikel 4, zesde lid, van artikel 7, vierde lid, en van de artikelen 10 en 11, 1°, niet van toepassing op de ondernemingen die jaarlijks gemiddeld niet meer dan 50 werknemers in dienst hebben, voor zover hun omzetcijfer, buiten de belasting over de toegevoegde waarde, voor het jongste boekjaar niet hoger is dan 50 miljoen frank en het totaal van hun balans bij het einde van het boekjaar niet oger is dan 25 miljoen frank. 

In zijn antwoord op een parlementaire vraag[^1]
  over de al dan niet cumulatieve aard van de drie in dat artikel vermelde voorwaarden, heeft de Minister van Economische Zaken gepreciseerd dat de uitvoeringsbesluiten bedoeld in dat artikel van de wet van toepassing zijn op al de ondernemingen, met uitzondering van die welke cumulatief voldoen aan de drie voorwaarden gesteld in dat artikel. Bijgevolg is een onderneming aan de bepalingen van deze besluiten onderworpen van zodra ze meer dan 50 werknemers heeft of haar omzetcijfer, buiten de belasting over de toegevoegde waarde, voor het jongste boekjaar hoger is dan 50 miljoen of het totaal van haar balans voor het jongste boekjaar hoger is dan 25 miljoen frank.

[^1]: Parlementaire vraag van de Heer Gramme van 9 december 1976 aan de Minister van Economische Zaken, Vragen en Antwoorden ‐ Senaat, Zitting 1976‐1977, 28 december 1976, p. 406.
