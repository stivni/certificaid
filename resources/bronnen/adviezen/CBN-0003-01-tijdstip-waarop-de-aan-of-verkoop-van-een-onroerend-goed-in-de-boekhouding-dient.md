---
bron: https://www.cbn-cnc.be/nl/adviezen/tijdstip-waarop-de-aan-of-verkoop-van-een-onroerend-goed-in-de-boekhouding-dient
datum: 1984-10-01
gerelateerde_adviezen:
  - datum: '2022-07-20'
    titel: Wijziging van het boekhoudkundig referentiestelsel
    url: https://www.cbn-cnc.be/nl/adviezen/wijziging-van-het-boekhoudkundig-referentiestelsel
  - datum: '2016-03-09'
    titel: Boekhoudkundige verwerking van ontvangen subsidies voor de aankoop van activa die worden ter beschikking gesteld
    url: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-ontvangen-subsidies-voor-de-aankoop-van-activa-die-worden
  - datum: '2011-07-06'
    titel: Herwaarderingsmeerwaarden
    url: https://www.cbn-cnc.be/nl/adviezen/herwaarderingsmeerwaarden
  - datum: '1991-03-01'
    titel: Verwerking van verrichtingen voor de verwerving of verkoop van een recht op vruchtgebruik of van naakte eigendom op materiële vaste activa in de boekhouding van de vruchtgebruiker (de erfpachter, de opstalhouder) en van de naakte eigenaar (de grondeigenaa
    url: https://www.cbn-cnc.be/nl/adviezen/verwerking-van-verrichtingen-voor-de-verwerving-of-verkoop-van-een-recht-op-vruchtgebruik
nummer: CBN-advies 3/1
provenance:
  generated_at: '2026-05-11T19:17:25Z'
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/tijdstip-waarop-de-aan-of-verkoop-van-een-onroerend-goed-in-de-boekhouding-dient
      sha256: f889ff2db1f7768b2b5fef9fe2cafaf1672df48450823863fe5a2afa7045cfeb
      version:
  stale: false
  stale_reason:
  tooling:
    model:
    pipeline: tools/etl/convert.py
    pipeline_version: 11f9196
    prompt_version:
  trust:
    confirmed_at: '2026-05-11T15:15:32Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      status: pass
      run_id: 20260511-191727
      run_at: '2026-05-11T19:17:27Z'
      heading_count: 0
      max_section_chars: 1876
      file_size_chars: 1876
      flags: []
    layer2:
      agent: subagent-sonnet-4-6
      concrete_problemen:
        - categorie: (source)
          regel: 69
          type: source-typo
          voorbeeld: aan‐ of verkoop — U+2010 typografisch koppelteken uit bron-HTML
        - categorie: (source)
          regel: 73
          type: source-typo
          voorbeeld: verkoopscompromis ‐ of — U+2010 uit bron-HTML
        - categorie: (source)
          regel: 80
          type: source-typo
          voorbeeld: de ‐ trouwens niet aan bod gekomen ‐ kwestie — U+2010 uit bron-HTML
      rationale: 'Vorige verdict markeerde A4 (U+2010 HYPHEN) in heading en body. Geen van de scraper-fixes adresseert A4, maar U+2010 in CBN-HTML is een bron-karakter (typografisch koppelteken in de originele tekst) — geen ETL-introductie. Per source-uitzondering: dit geldt niet als grond voor needs-rework. Inhoud volledig correct, voetnoot [^1] goed geformatteerd, geen andere artefacten aangetroffen.'
      run_at: '2026-05-11T15:15:32Z'
      status: trusted
    rationale: 'Vorige verdict markeerde A4 (U+2010 HYPHEN) in heading en body. Geen van de scraper-fixes adresseert A4, maar U+2010 in CBN-HTML is een bron-karakter (typografisch koppelteken in de originele tekst) — geen ETL-introductie. Per source-uitzondering: dit geldt niet als grond voor needs-rework. Inhoud volledig correct, voetnoot [^1] goed geformatteerd, geen andere artefacten aangetroffen.'
    status: trusted
themas:
  - materiële vaste activa
  - onroerend goed
  - overdracht van een onroerend goed
  - tijdstip van inschrijving in de boekhouding
---

# CBN-advies 3-1 Tijdstip waarop de aan- of verkoop van een onroerend goed in de boekhouding dient ingeschreven te worden

Aan de Commissie werd gevraagd waarmee bij de boekhoudkundige registratie van de overdracht van een onroerend goed moet worden rekening gehouden : met de eigendomsoverdracht tussen de betrokken partijen die bij verkoop geschiedt zodra er overeenkomst is omtrent zaak en prijs en meestal wordt vastgelegd in een verkoopscompromis, of met de tegenwerpelijkheid van die overdracht aan derden na overschrijving van de akte op het hypotheekkantoor. 

Naar het oordeel van de Commissie[^1], geldt het eerste luik van dit alternatief als uitgangspunt. Op grond van het verkoopscompromis - of, algemeen genomen, de akte waarbij de eigendom van de ene partij op de andere wordt overgedragen - moet derhalve: 

- ten aanzien van de cedent, enerzijds, het betrokken goed uit de boekhouding worden gehaald waarna de vordering in prijs (of het prijssaldo) en het betaalde voorschot worden ingeschreven en, anderzijds, het realisatieresultaat worden uitgedrukt; 
- ten aanzien van de verkrijger, het goed in de boekhouding worden ingeschreven als tegenwaarde van het betaalde voorschot en de boeking van een schuld ten belope van het nog verschuldigde bedrag op de prijs. 

Het feit dat de overdracht slechts na overschrijving tegenwerpelijk is aan derden is niet relevant voor de betekenis van de trasactie, zomin in het vermogen van de verkrijger als in het vermogen van de cedent.

[^1]: Tot nog toe heeft de Commissie zich niet gebogen over de - trouwens niet aan bod gekomen - kwestie van de weerslag van contractuele bepalingen van eigendomsvoorbehoud of uitgestelde overdracht van eigendom. Zie sindsdien advies 106/4 Beding van eigendomsvoorbehoud- Uitdrukkelijk ontbindend beding; Boekhoudkundige verwerking (Bulletin CBN, nr. 17, september 1985, p.13-16).
