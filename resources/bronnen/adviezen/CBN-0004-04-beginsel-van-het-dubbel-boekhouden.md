---
bron: https://www.cbn-cnc.be/nl/adviezen/beginsel-van-het-dubbel-boekhouden
datum: 1993-02-01
nummer: CBN-advies 4/4
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/beginsel-van-het-dubbel-boekhouden
      sha256: 189ed488644d5d8e86a771346dd9e6ec8e3c92bafe18bf3bbd7219ce8ad3f25b
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-11T13:15:10Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T13:16:01Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Drie resterende problemen na scraper-fix: (1) D1: 'gebruikeljke' (r59, typo voor 'gebruikelijke') en 'rekeningenstelel' (r64, typo voor 'rekeningstelsel') en 'ee volledige' (r63, vermoedelijk 'een volledige'). (2) D3: '[^2]: Artikel 25, §1 van het koninklijk besluit van het koninklijk besluit van 30 januari 2001' bevat een duidelijke woordduplicatie ('van het koninklijk besluit' tweemaal, r71). A6-bug (bullet gesplitst over meerdere regels) lijkt verholpen in de nieuwe scrape: de bullet staat nu op één regel (r65). A4 (U+2010) kan niet worden bevestigd of ontkend zonder hex-inspectie."
    layer1:
      status: pass
      run_id: 20260511-131513
      run_at: '2026-05-11T13:15:13Z'
      heading_count: 0
      max_section_chars: 2052
      file_size_chars: 2052
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T13:16:01Z'
      rationale: "Drie resterende problemen na scraper-fix: (1) D1: 'gebruikeljke' (r59, typo voor 'gebruikelijke') en 'rekeningenstelel' (r64, typo voor 'rekeningstelsel') en 'ee volledige' (r63, vermoedelijk 'een volledige'). (2) D3: '[^2]: Artikel 25, §1 van het koninklijk besluit van het koninklijk besluit van 30 januari 2001' bevat een duidelijke woordduplicatie ('van het koninklijk besluit' tweemaal, r71). A6-bug (bullet gesplitst over meerdere regels) lijkt verholpen in de nieuwe scrape: de bullet staat nu op één regel (r65). A4 (U+2010) kan niet worden bevestigd of ontkend zonder hex-inspectie."
      concrete_problemen:
        - regel: 59
          categorie: D1
          type: other
          voorbeeld: strookt met de boekhoudwet. Een dergelijke werkwijze kan ... gebruikeljke regels
        - regel: 63
          categorie: D1
          type: other
          voorbeeld: op ee volledige en correcte wijze werden overgeschreven
        - regel: 64
          categorie: D1
          type: other
          voorbeeld: het koninklijk besluit over de minimumindeling ... rekeningenstelel
        - regel: 71
          categorie: D1
          type: other
          voorbeeld: van het koninklijk besluit van het koninklijk besluit van 30 januari 2001
themas:
  - beginsel van dubbel boekhouden
  - compensatie
  - compensatieverbod
---

# CBN-advies 4-4 - Beginsel van het dubbel boekhouden

In een bepaald boekhoudsoftwarepakket worden creditnota's voor cliënten en creditnota's opgesteld door leveranciers als «aftrek» geboekt op de debetzijde van de cliëntenrekening of creditzijde van de leveranciersrekening. Aan de Commissie werd gevraagd of dit wel strookt met de boekhoudwet. 

Een dergelijke werkwijze kan volgens de Commissie enkel worden toegestaan voor zover zij in overeenstemming is met de gebruikeljke regels op het dubbel boekhouden waarnaar artikel 4, eerste lid van de wet van 17 juli 1975 uitdrukkelijk verwijst alsook met de bijzondere regels van haar uitvoeringsbesluiten. 

Dit houdt in: 

- dat zowel in het dagboek als in de rekeningen dezelfde boekingswijze moet worden toegepast. Zo niet, zouden de mutaties over een bepaalde periode aan debet- en creditzijde in de dagboeken niet overeenstemmen met de mutaties aan debet- en creditzijde in de rekeningen. Er zou dan een belangrijk gegeven verloren gaan aan de hand waarvan kan worden nagegaan of de gegevens in de dagboeken op ee volledige en correcte wijze werden overgeschreven in de rekeningen, met als gevolg dat de betrouwbaarheid van de boekhouding in het gedrang zou komen; 
- dat deze methode niet mag worden toegepast voor kortingen, ristorno's en rabatten die werden ontvangen of toegekend. Een boeking in de vorm van een «aftrek» zou immers strijdig zijn met de bepalingen van het koninklijk besluit over de minimumindeling van het algemeen rekeningenstelel dat voor dergelijke verrichtingen specifieke rekeningen bevat (608 - 708); 
- dat het beginsel van het compensatieverbod[^1] alsook het beginsel van de volledige aard van de jaarrekening[^2] in elk geval moeten worden nageleefd. 

Bijgevolg kan een dergelijke boekingswijze in de vorm van een «aftrek» in feite enkel worden toegestaan als correctie van een vroegere boeking.

[^1]: Artikel 25, §2 van het koninklijk besluit van 30 januari 2001.

[^2]: Artikel 25, §1 van het koninklijk besluit van het koninklijk besluit van 30 januari 2001.
