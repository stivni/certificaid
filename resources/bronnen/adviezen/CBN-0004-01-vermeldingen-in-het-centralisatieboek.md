---
bron: https://www.cbn-cnc.be/nl/adviezen/vermeldingen-in-het-centralisatieboek
datum: 1977-08-01
gerelateerde_adviezen:
  - datum: '2011-10-05'
    titel: Bewaring van de boeken en verantwoordingsstukken
    url: https://www.cbn-cnc.be/nl/adviezen/bewaring-van-de-boeken-en-verantwoordingsstukken
  - datum: '2010-09-24'
    titel: Bewaring van boeken en verantwoordingsstukken
    url: https://www.cbn-cnc.be/nl/adviezen/bewaring-van-boeken-en-verantwoordingsstukken
  - datum: '1981-04-01'
    titel: Over het centraal boek
    url: https://www.cbn-cnc.be/nl/adviezen/over-het-centraal-boek
nummer: CBN-advies 4/1
themas:
  - boeken
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/vermeldingen-in-het-centralisatieboek
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
    confirmed_at: '2026-05-13T13:08:13Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: Alle door vorige verdict gemelde tekstfouten (berokken, dee vermelding, wttelijke, centraisatieboek, bewegingn, angegeven) staan letterlijk in de bron-HTML en vallen onder de source-uitzondering. A4 (U+2010 in r87 'ondergaan -gelet') is eveneens een bron-karakter uit de CBN-website. Geen ETL-bugs gevonden buiten deze source-categorieën. Inhoud volledig, voetnoot intact.
    layer1:
      status: pass
      run_id: 20260512-233938
      run_at: '2026-05-12T23:39:38Z'
      heading_count: 0
      max_section_chars: 2830
      file_size_chars: 2830
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T13:08:13Z'
      rationale: Alle door vorige verdict gemelde tekstfouten (berokken, dee vermelding, wttelijke, centraisatieboek, bewegingn, angegeven) staan letterlijk in de bron-HTML en vallen onder de source-uitzondering. A4 (U+2010 in r87 'ondergaan -gelet') is eveneens een bron-karakter uit de CBN-website. Geen ETL-bugs gevonden buiten deze source-categorieën. Inhoud volledig, voetnoot intact.
      concrete_problemen:
        - regel: 75
          categorie: (source)
          type: source-typo
          voorbeeld: berokken rekeningen — source-typo voor 'betrokken'
        - regel: 83
          categorie: (source)
          type: source-typo
          voorbeeld: dee vermelding betrekking moet hebben ... wttelijke vereisten
        - regel: 85
          categorie: (source)
          type: source-typo
          voorbeeld: inschrijving in het centraisatieboek te beperken
        - regel: 87
          categorie: (source)
          type: source-typo
          voorbeeld: de bewegingn die elk ervan hebben ondergaan ... angegeven
        - regel: 87
          categorie: (source)
          type: source-typo
          voorbeeld: ondergaan -gelet op de moeilijkheid — U+2010 of gewoon koppelteken uit bron-HTML
---
# CBN-advies 4-1 - Vermeldingen in het centralisatieboek

**Dit advies is verouderd als gevolg van publicatie van het koninklijk besluit nr. 22 van 15 december 1978 (B.S. 4 januari 1979).**

Krachtens artikel 4, tweede lid van de wet van 17 juli 1975 moeten al de in de hulpdagboeken ingeschreven gegevens met vermelding van de diverse berokken rekeningen gecentraliseerd worden in één centralisatieboek. 

De interpretatie van deze bepaling heeft talrijke vragen doen oprijzen. Ze hebben de Commissie ertoe gebracht aan de Regering voor te stellen de tekst ervan te wijzigen om de draagwijdte ervan nadertoe te lichten.[^1] 

Naar de mening van de Commissie moet de huidige tekst als volgt worden geïnterpreteerd: 

Het is evident dat de wetgever niet het overschrijven in het centralisatieboek heeft willen opleggen van elk der in de hulpdagbeken geregistreerde gegevens, maar wel het geheel van deze gegevens. De term «gecentraliseerd» houdt namelijk in dat de gegevens vooraf worden gegroepeerd volgens hun gemeenschappelijke kenmerken. 

De verplichting om in het centralisatieboek de gegevens over te nemen die in de hulpdagboeken zijn ingeschreven houdt in dat dee vermelding betrekking moet hebben op de geregistreerde bewegingen. De eenvoudige vermelding van de saldi van de rekeningen die door deze boekingen beïnvloed werden beantwoordt dus niet aan de wttelijke vereisten. 

Doordat de tekst de vermelding voorschrijft van de diverse betrokken rekeningen volstaat het niet de inschrijving in het centraisatieboek te beperken tot het totaal van de debet- en creditbewegingen van de diverse hulpdagboeken, en minder nog ze te beperken tot een boeking «diversen aan diversen». 

De centralisatie moet gehecht zijn aan het rekeningstelsel van de onderneming en derhalve verricht worden voor de rekeningen warin dat stelsel voorziet. In vele gevallen echter bevat het rekeningstelsel een groot aantal rekeningen en het overschrijven met de hand van de bewegingn die elk ervan hebben ondergaan -gelet op de moeilijkheid om mechanische middelen te gebruiken voor het inschrijven in een register - kan niet alleen een aanzienlijk werkvolume vertegenwoordigen, het kan ook een bron van vergissingen zijn. Er mag worden aangenomen dat de bedoeling van de wetgever - veilig stellen dat de boekingen niet achteraf gewijzigd kunnen worden - niet uitsluit dat de vermeldingen in het centralisatieboek betrekking hebben op de syntheserekeningen van het rekeningstelsel van de onderneming, voor zover deze boeking wordt gestaafd door een verantwoordingsstuk van de centralisatieverrichtingen. Onder syntheserekening moeten de posten worden verstaan die in het als minimum geldend genormaliseerd rekeningstelsel worden angegeven met een getal van twee cijfers.

[^1]: Zie: Advies over bepaalde wijzigingen aan de wet van 17 juli 1975.
