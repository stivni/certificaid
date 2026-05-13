---
bron: https://www.cbn-cnc.be/nl/adviezen/obligaties-met-warrant
datum: 1988-06-01
gerelateerde_adviezen:
  - datum: '2019-07-11'
    titel: Boekhoudkundige verwerking van de uitgifte van een obligatielening
    url: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-de-uitgifte-van-een-obligatielening
  - datum: '1991-03-01'
    titel: Passende boekhoudkundige verwerking van de tegenwaarde van participatiecertificaten CPC&#039;s
    url: https://www.cbn-cnc.be/nl/adviezen/passende-boekhoudkundige-verwerking-van-de-tegenwaarde-van-participatiecertificaten-cpcs
  - datum: '1990-06-01'
    titel: Boeking van de prorata van gelopen interest op obligaties en kasbons
    url: https://www.cbn-cnc.be/nl/adviezen/boeking-van-de-prorata-van-gelopen-interest-op-obligaties-en-kasbons
  - datum: '1984-10-01'
    titel: 'Vastrentende effecten : financiële vaste activa of geldbeleggingen ? Criteria'
    url: https://www.cbn-cnc.be/nl/adviezen/vastrentende-effecten-financiele-vaste-activa-of-geldbeleggingen-criteria
nummer: CBN-advies 139/2
themas:
  - obligaties
  - obligaties met warrant
  - warrant
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/obligaties-met-warrant
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: b4eac1f-dirty
    model:
    prompt_version:
  generated_at: '2026-05-12T23:37:45Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-13T13:34:31Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: Geen ETL-artefacten aangetroffen. Heading-structuur aanwezig (1 headings), inhoud volledig, voetnoten correct gerenderd, geen form-feeds of column-bleed.
    layer1:
      status: pass
      run_id: 20260512-233938
      run_at: '2026-05-12T23:39:40Z'
      heading_count: 0
      max_section_chars: 3656
      file_size_chars: 3656
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T13:34:31Z'
      rationale: Geen ETL-artefacten aangetroffen. Heading-structuur aanwezig (1 headings), inhoud volledig, voetnoten correct gerenderd, geen form-feeds of column-bleed.
      concrete_problemen: []
---
# CBN-advies 139/2 - Obligaties met warrant

De Commissie werd ondervraagd over de boekingswijze van obligaties uitgegeven met warranten evenals over de aanschaffingswaarde die moet worden toegekend respectievelijk aan de obligatie en aan de warrant bij afzondering van deze laatste. 

Zij heeft deze vraagstelling onderzocht redenerend op het meest voorkomende geval waarin de warrant aan zijn titularis het recht geeft om tegen een van bij de aanvang vastgestelde, vaste prijs, in te schrijven op aandelen hetzij van de vennootschap die de obligaties uitgeeft, hetzij van een derde, verwante vennootschap. De vastgestelde beginselen zijn evenwel op analogische wijze van toepassing wanneer, zoals recent het geval was, de uitoefeningsprijs van de warrant vastgesteld is door verwijzing naar de beurskoers van de aandelen waarop kan worden ingeschreven, op het ogenblik van de inschrijving of gedurende een periode die deze voorafgaat (in dat geval is de waarde van de warrant in beginsel nihil of onbelangrijk), of wanneer de warrant recht geeft op de aanschaffing van een goed van een andere aard (bijvoorbeeld goud). 

Naar het oordeel van de Commissie bezit een warrant in se het karakter van een inschrijvingsrecht van hetzelfde type als bij uitgifte van nieuwe aandelen. De Commissie verwijst derhalve naar advies 139/1 gepubliceerd in *Bull. CBN* nr. 13 van januari 1984 (pp. 14-18). 

Uit dit advies blijkt wat volgt : 

- bij afzondering van de warrant om hetzij in te schrijven op de aandelen waarop hij recht geeft, hetzij om hem te verkopen, moet de aanschaffingswaarde van de obligatie met warrant worden omgeslagen over de obligatie enerzijds, en de warrant anderzijds; 
- de tegenwaarde kan niet zonder meer als opbrengst in de resultatenrekening worden geboekt; 
- ingeval het recht wordt uitgeoefend, maakt de boekwaarde van de warrant integraal deel uit van de aanschaffingswaarde van de nieuwe effecten; 
- bij verkoop van de warrant wordt de ten opzichte van de boekwaarde gerealiseerde meer- of minderwaarde, in resultaat genomen. 

De boekwaarde van de warrant - die in mindering moet worden gebracht van de aanschaffingswaarde van een obligatie met warrant - wordt, naar analogie van het inschrijvingsrecht, als volgt berekend: 

aanschaffingswaarde van de obligatie met warrant x [verkoopprijs warrant[^1]
 / (marktkoers obligaties ex-warrant + verkoopprijs warrant)] 

*Voorbeeld*

- Aanschaffingswaarde obligatie met warrant = 1.000 
- Marktkoers obligatie ex-warrant = 900 
- Verkoopprijs warrant = 300 
- Boekwaarde warrant = 1.000 x 300/(900 + 300) = 250 
- Boekwaarde obligatie ex-warrant = 1.000 - 250 = 750 Een verkoop van de warrant wordt als volgt geboekt : 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 55 | Kredietinstellingen | 300 | |
| aan | 52 | Vastrentende effecten | | 250 |
| | 75 | Financiële opbrengsten | 50 | |

Samengevat :

- enkel de volgens voornoemde formule berekende boekwaarde van de warrant mag in mindering worden gebracht van de aanschaffingswaarde van het effect waaraan hij is gehecht, met uitsluiting dus van de marktwaarde; 
- enkel het verschil tussen deze boekwaarde van de warrant en zijn verkoopprijs mag in resultaat worden genomen. 

Dezelfde redenering geldt wanneer de obligatie en de warrant, hoewel afgezonderd, samen werden verworven tegen een totaalprijs. 

[^1]: Bij uitvoering van het recht wordt de "waarde van het recht" bedoeld. Die waarde wordt bepaald op grond van de werkelijke marktkoers, volgens een gelijkaardige methode als voor de bepaling van de koers van de obligatie ex-warrant (zie Bull CBN nr. 13, p. 17).
