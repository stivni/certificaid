---
bron: https://www.cbn-cnc.be/nl/adviezen/waardering-van-de-aanschaffingsprijs-van-de-voorraden-op-grond-van-de-verkoopprijs
datum: 1989-09-01
gerelateerde_adviezen:
  - datum: '2025-06-06'
    titel: 'Aanschaffingsprijs : bijkomende kosten (update) [ONTWERP]'
    url: https://www.cbn-cnc.be/nl/adviezen/aanschaffingsprijs-bijkomende-kosten-update-ontwerp
  - datum: '2017-02-01'
    titel: 'Invoer: douanerechten en verlegging van de heffing van de btw'
    url: https://www.cbn-cnc.be/nl/adviezen/invoer-douanerechten-en-verlegging-van-de-heffing-van-de-btw
  - datum: '2012-10-10'
    titel: De boekhoudkundige verwerking van immateriële vaste activa
    url: https://www.cbn-cnc.be/nl/adviezen/de-boekhoudkundige-verwerking-van-immateriele-vaste-activa
  - datum: '2002-05-01'
    titel: Bepaling van de aanschaffingswaarde van activa verkregen onder bezwarende titel of om niet
    url: https://www.cbn-cnc.be/nl/adviezen/bepaling-van-de-aanschaffingswaarde-van-activa-verkregen-onder-bezwarende-titel-of-om-niet
nummer: CBN-advies 126/7
provenance:
  generated_at: '2026-05-11T19:17:25Z'
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/waardering-van-de-aanschaffingsprijs-van-de-voorraden-op-grond-van-de-verkoopprijs
      sha256: a116e35af0dd89b793235e46cdd8b2a8b8bdfc379ce3aee5c522c23738e79043
      version:
  stale: false
  stale_reason:
  tooling:
    model:
    pipeline: tools/etl/convert.py
    pipeline_version: 11f9196
    prompt_version:
  trust:
    confirmed_at: '2026-05-11T17:05:20Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      status: pass
      run_id: 20260511-191727
      run_at: '2026-05-11T19:17:28Z'
      heading_count: 2
      max_section_chars: 2181
      file_size_chars: 4690
      flags: []
    layer2:
      agent: subagent-sonnet-4-6
      concrete_problemen:
        - categorie: C3
          regel: 85
          type: pseudo-table
          voorbeeld: '| | --------- | ------------- | | |'
        - categorie: E2
          regel: 92
          type: other
          voorbeeld: '| | Theoretische eindinventaris\n\t\t\t(tegen detailprijs) | 22.000 | | |'
        - categorie: E2
          regel: 96
          type: other
          voorbeeld: '| | Fysieke eindinventaris\n\t\t\t(tegen detailprijs) | 20.000 | | |'
      rationale: 'C3: regels 85, 88, 91 bevatten ''--------- | -------------'' als gewone tabelcellen — ASCII-art scheidingsrijen die geen valide markdown-tabelseparatoren zijn. E2: tabelrijen ''Theoretische eindinventaris'' (regels 92-93) en ''Fysieke eindinventaris'' (regels 96-97) zijn gesplitst over twee regels met tab-inspringing — breekt de pipe-table structuur.'
      run_at: '2026-05-11T17:05:20Z'
      status: needs-rework
    rationale: 'C3: regels 85, 88, 91 bevatten ''--------- | -------------'' als gewone tabelcellen — ASCII-art scheidingsrijen die geen valide markdown-tabelseparatoren zijn. E2: tabelrijen ''Theoretische eindinventaris'' (regels 92-93) en ''Fysieke eindinventaris'' (regels 96-97) zijn gesplitst over twee regels met tab-inspringing — breekt de pipe-table structuur.'
    status: needs-rework
themas:
  - aanschaffingsprijs
  - aftrekmethode
  - verkoopprijs
  - voorraden
  - waardering
  - waardering van voorraden
---

# CBN-advies 126/7 - Waardering van de aanschaffingsprijs van de voorraden op grond van de verkoopprijs

Het koninklijk besluit van 8 oktober 1976 stelt als beginsel dat voorraden - zoals de andere actiefbestanddelen -in de jaarrekening worden gewaardeerd tegen aanschaffingsprijs. Deze waarde wordt gewoonlijk vastgesteld volgens een additieve methode, waarbij aan de voorraadrekening de diverse kostenbestanddelen worden toegerekend die aan de betrokken voorraden toerekenbaar zijn en werden gemaakt om ze op dat ogenblik op die plaats te brengen in de staat waarin zij zich bevinden. Deze methode is uitdrukkelijk verwoord in de artikelen 21 en 22 van voornoemd besluit, waar de aanschaffings- en de vervaardigingsprijs worden omschreven. 

In distributiebedrijven, vooral deze waar vele, uiteenlopende produkten worden verkocht, blijkt het vaak moeilijk om precies en omstandig, op grond van deze additieve methode, de aanschaffingsprijs vast te stellen van de voorraden in de rekken en op grond daarvan de follow-up van deze voorraden te organiseren. Het komt dan ook veel voor dat de aanschaffingsprijs van deze voorraden in de jaarrekening wordt vastgesteld volgens een «aftrekmethode», waarbij van de detailverkoopprijs van deze voorraden de marge wordt afgetrokken waarmee de aanschaffingsprijs werd verhoogd om de verkoopprijs vast te stellen. 

Volgend voorbeeld illustreert hoe de aanschaffingsprijs door reconstitutie wordt vastgesteld[^1]. 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | Kost | Detailverkoop | Marge | |
| | Begininventaris | 12.000 | 16.000 | |
| | Aankopen van de periode | 72.000 | 100.000 | |
| | Verhoging van de verkoopprijs | 4.000 | | |
| | --------- | ------------- | | |
| | TOTAAL | 84.000 | 120.000 | 70% |
| | Afprijzing | - 8.000 | | |
| | --------- | ------------- | | |
| | Te koop gestelde goederen | 84.000 | 112.000 | 75% |
| | Bedrag van de verkopen | - 90.000 | | |
| | ------------ | | | |
| | Theoretische eindinventaris
			(tegen detailprijs) | 22.000 | | |
| | ------------ | | | |
|---|---|---|---|---|
| | Fysieke eindinventaris
			(tegen detailprijs) | 20.000 | | |

## Winkelvoorraden
In de veronderstelling dat de prijsbewegingen naar verhouding werden omgeslagen over de verkochte goederen en de goederen in de rekken, levert deze methode een aanschaffingsprijs op van 15 000 (20 000 x 75 %). 

Deze door de Angelsaksische «retail inventory method» en «gross profit method» ingegeven methode, is naar het oordeel van de Commissie geldig en aanvaardbaar, op voorwaarde dat daarmee de aanschaffingsprijs van de betrokken voorraden voldoende bij benadering kan worden gereconstrueerd. 

Hieruit volgt dat de aftrek op de verkoopprijs niet forfaitair - a fortiori, niet arbitrair - mag worden vastgesteld. Deze aftrek moet het resultaat zijn van een berekening die slaat op het hele verloop van de normale cyclus voor de commercialisering van de momenteel voorradige goederen. Dit impliceert dan ook dat hij periodiek opnieuw moet worden getoetst op grond van de effectieve band tussen het gerealiseerde omzetcijfer en de kosten die tijdens de periode zijn gemaakt voor de aankoop van de verkochte of nog voorradige goederen. De aftrek moet worden becijferd per categorie van - qua commercialisatie -homogene producten. Het bedrag uit de toepassing van deze marge mag geen kosten bevatten die geen deel uitmaken van de aanschaffingsprijs van de betrokken voorraden. De methode moet dermate strikt worden toegepast dat zij leidt tot een statistisch aanvaardbare reconstructie van de aanschaffingsprijs van de diverse categorieën van betrokken handelsgoederen. 

## Centraal opgeslagen voorraden
Aangezien de aanschaffingsprijs hier wordt bepaald op grond van de verkoopprijs, is deze methode slechts dienstig voor handelsgoederen die zich in de verkoopcentra bevinden. Zij kan niet worden toegepast voor centraal opgeslagen voorraden; deze methode kan immers pas worden toegepast op het ogenblik waarop die worden ten toon gesteld of te koop aangeboden, tegen een welbepaalde verkoopprijs. Centraal opgeslagen voorraden moeten derhalve worden beheerd tegen een rechtstreeks vastgestelde aanschaffingsprijs. 

Het gebruik van deze methode is conform het besluit van 8 oktober 1976 en vereist derhalve geen afwijking. 

Het Contractcomité opgericht door de vierde richtlijn voor een geharmoniseerde toepassing van de bepalingen hiervan, heeft bevestigd dat deze methode verenigbaar is met de vierde richtlijn.

[^1]: Overgenomen uit Eldon S. Hendriksen, Accounting theory, fourth edition, International Edition, 1982, p. 329. Bron : Bulletin CBN, nr. 24, september 1989, p. 13-14
