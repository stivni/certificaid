---
bron: https://www.cbn-cnc.be/nl/adviezen/beginsel-van-het-dubbel-boekhouden
datum: 1993-02-01
nummer: CBN-advies 4/4
themas:
  - beginsel van dubbel boekhouden
  - compensatie
  - compensatieverbod
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/beginsel-van-het-dubbel-boekhouden
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: b4eac1f-dirty
    model:
    prompt_version:
  generated_at: '2026-05-12T23:37:14Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-13T13:29:36Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Alle door vorige verdict gemelde problemen zijn source-typos: 'gebruikeljke' (r63), 'rekeningenstelel' (r68), 'ee volledige' (r67) staan in de bron-HTML. De woordduplicatie in [^2] ('van het koninklijk besluit van het koninklijk besluit', r75) is eveneens een fout in de officiële CBN-tekst. Geen ETL-artefacten (A-G) aangetroffen buiten deze source-categorie. Bullet op r65 correct op één regel. Inhoud volledig."
    layer1:
      status: pass
      run_id: 20260512-233938
      run_at: '2026-05-12T23:39:38Z'
      heading_count: 0
      max_section_chars: 2051
      file_size_chars: 2051
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T13:29:36Z'
      rationale: "Alle door vorige verdict gemelde problemen zijn source-typos: 'gebruikeljke' (r63), 'rekeningenstelel' (r68), 'ee volledige' (r67) staan in de bron-HTML. De woordduplicatie in [^2] ('van het koninklijk besluit van het koninklijk besluit', r75) is eveneens een fout in de officiële CBN-tekst. Geen ETL-artefacten (A-G) aangetroffen buiten deze source-categorie. Bullet op r65 correct op één regel. Inhoud volledig."
      concrete_problemen:
        - regel: 63
          categorie: (source)
          type: source-typo
          voorbeeld: gebruikeljke regels op het dubbel boekhouden
        - regel: 67
          categorie: (source)
          type: source-typo
          voorbeeld: op ee volledige en correcte wijze werden overgeschreven
        - regel: 68
          categorie: (source)
          type: source-typo
          voorbeeld: het koninklijk besluit over de minimumindeling ... rekeningenstelel
        - regel: 75
          categorie: (source)
          type: source-typo
          voorbeeld: van het koninklijk besluit van het koninklijk besluit van 30 januari 2001 — dubbele tekst in bron
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
