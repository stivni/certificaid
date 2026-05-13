---
bron: https://www.cbn-cnc.be/nl/adviezen/verwerking-in-de-jaarrekening-van-de-door-de-vlaamse-regering-gecreeerde-opleidingscheques
datum: 2008-12-01
gerelateerde_adviezen:
  - datum: '2024-05-22'
    titel: Boekhoudkundige verwerking van de taks tot vergoeding der successierechten
    url: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-de-taks-tot-vergoeding-der-successierechten
  - datum: '2013-03-06'
    titel: De boekhoudkundige verwerking van de afzonderlijke aanslag op interne pensioenvoorzieningen
    url: https://www.cbn-cnc.be/nl/adviezen/de-boekhoudkundige-verwerking-van-de-afzonderlijke-aanslag-op-interne
nummer: CBN-advies 180/1
themas:
  - bedrijfsbelastingen
  - financiële kosten
  - liquide middelen
  - opleidingscheques
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/verwerking-in-de-jaarrekening-van-de-door-de-vlaamse-regering-gecreeerde-opleidingscheques
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: b4eac1f-dirty
    model:
    prompt_version:
  generated_at: '2026-05-12T23:38:03Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-13T13:08:18Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Laag-1 pass, heading_count 0 klopt: het advies is één doorlopend tekstblok zonder expliciete secties (zo ook in het origineel — kort advies van één paragraaf). Inhoud volledig, geen artefacten, geen voetnoten nodig, geen bullets. Eén typ-artefact ('daaarentegen' met drie a's op regel 61) maar dat is waarschijnlijk originele tekst."
    layer1:
      status: pass
      run_id: 20260512-233938
      run_at: '2026-05-12T23:39:40Z'
      heading_count: 0
      max_section_chars: 2305
      file_size_chars: 2305
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T13:08:18Z'
      rationale: "Laag-1 pass, heading_count 0 klopt: het advies is één doorlopend tekstblok zonder expliciete secties (zo ook in het origineel — kort advies van één paragraaf). Inhoud volledig, geen artefacten, geen voetnoten nodig, geen bullets. Eén typ-artefact ('daaarentegen' met drie a's op regel 61) maar dat is waarschijnlijk originele tekst."
      concrete_problemen:
        - regel: 61
          categorie: D1
          type: other
          voorbeeld: wanneer daaarentegen de aankoop (driemaal 'a' — vermoedelijk tikfout in origineel)
---
# CBN-advies 180/1 - Verwerking in de jaarrekening van de door de Vlaamse regering gecreëerde opleidingscheques

Het besluit van de Vlaamse regering van 14 december 2001 en het ministerieel besluit van 21 december 2001 creëerden in Vlaanderen het systeem van "opleidingscheques". Vennootschappen kunnen maximaal 200 opleidingscheques met een zichtwaarde van 30 euro aankopen. Het Vlaamse Gewest levert een bijdrage van 50% in het totaalbedrag van de aangekochte opleidingscheques. De opleidingscheques hebben een geldigheidsduur van twaalf maanden vanaf de datum van uitgifte en moeten aangewend worden voor een opleiding die heeft plaatsgevonden vóór het verstrijken van de geldigheidsduur.

Naar het oordeel van de Commissie voor Boekhoudkundige Normen dienen deze opleidingscheques als volgt verwerkt te worden in de jaarrekening van de vennootschap die ze aankoopt.

Bij aankoop boekt de vennootschap de opleidingscheque als een actief in post IX van de activa: *Liquide middelen*. De tussenkomst van de Vlaamse overheid in de aankoopprijs ervan (15 euro) wordt geboekt als een opbrengst in post I,D van de resultatenrekening:*Andere bedrijfsopbrengsten*.

Na het volgen van de gekozen opleiding wordt de door de opleidingsverstrekker aangerekende prijs ten laste genomen.De geactiveerde opleidingscheque wordt afgeboekt wanneer hij als betaalmiddel wordt gebruikt.

De aanbevolen verwerkingswijze heeft tot gevolg dat netto geen resultaat erkend wordt wanneer de aankoop van de vormingscheque en het volgen van de opleiding in hetzelfde boekjaar plaatsvinden: de opbrengst verbonden met de tussenkomst van de overheid in de aankoopprijs van de opleidingscheque, wordt immers geneutraliseerd door het ten laste nemen van de kostprijs van de gevolgde opleiding; wanneer daaarentegen de aankoop van de vormingscheque en het volgen van de opleiding in verschillende boekjaren plaatsvinden, worden ook de opbrengst van de overheidstussenkomst bij het aankopen van de opleidingscheque en de kostprijs van de gevolgde opleiding in verschillende boekjaren geboekt.

Opleidingscheques die waardeloos worden omdat zij niet gebruikt worden vóór hun vervaldatum, leiden tot een verlies ten belope van hun zichtwaarde (30 euro) dat geboekt wordt in post V,C van de resultatenrekening: *Andere financiële kosten*.
