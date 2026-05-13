---
bron: https://www.cbn-cnc.be/nl/adviezen/verwerving-van-een-bebost-terrein
datum: 2016-06-15
nummer: CBN-advies 2016/9
themas:
  - bebost terrein
  - goederen in bewerking
  - terrein
  - voorraad
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/verwerving-van-een-bebost-terrein
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: b4eac1f-dirty
    model:
    prompt_version:
  generated_at: '2026-05-12T23:38:28Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-13T13:34:43Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Klein en schoon bestand (3340 tekens). Drie headings correct, twee voorbeeldboekingstabellen in pipe-syntax, voetnoten [^1]–[^3] volledig gedefinieerd. Geen artefacten aangetroffen in geen enkele categorie. Inhoud compleet: beide scenario's (vervreemding / geen vervreemding) behandeld."
    layer1:
      status: pass
      run_id: 20260512-233938
      run_at: '2026-05-12T23:39:42Z'
      heading_count: 3
      max_section_chars: 1427
      file_size_chars: 3325
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T13:34:43Z'
      rationale: "Klein en schoon bestand (3340 tekens). Drie headings correct, twee voorbeeldboekingstabellen in pipe-syntax, voetnoten [^1]–[^3] volledig gedefinieerd. Geen artefacten aangetroffen in geen enkele categorie. Inhoud compleet: beide scenario's (vervreemding / geen vervreemding) behandeld."
      concrete_problemen: []
---
# CBN-advies 2016/9 – Verwerving van een bebost terrein

## Inleiding
In dit advies behandelt de Commissie voor boekhoudkundige normen de boekhoudkundige verwerking van de verwerving van een bebost terrein. De verwerver schaft dit terrein in eerste instantie aan voor houtkap.

Op het ogenblik van de verwerving van het bebost terrein bestaat de mogelijkheid dat het terrein na de houtkap terug wordt vervreemd of dat het terrein zal deel uitmaken van het vermogen van de vennootschap. Beide scenario’s worden vervolgens uiteengezet.

## Aankoop bebost terrein met vervreemding terrein na houtkap
In het geval dat de vennootschap een bebost terrein aankoopt voor houtkap en op het ogenblik van de aankoop de intentie heeft om het terrein te vervreemden na de houtkap is de Commissie van oordeel dat het terrein als een onroerend goed bestemd voor verkoop dient te worden geboekt. Concreet zal er op het ogenblik van de verwerving wel een onderscheid moeten worden gemaakt tussen de waarde van een ontbost terrein en de waarde van de te kappen bomen. Deze bomen zullen als goederen in bewerking worden geboekt. De Commissie is van oordeel dat deze opsplitsing noodzakelijk is aangezien de aard van de terrein- en houtcomponent fundamenteel verschillend is.

*Voorbeeld*

NV XYZ betaalt 150 EUR voor een bebost terrein waarvan 1/3 van de aanschaffingswaarde correspondeert met de terreincomponent en 2/3 van de aanschaffingswaarde met de houtcomponent. De vennootschap heeft de intentie om de grond te vervreemden na de houtkap. Op datum van de verwerving wordt het volgende geboekt[^2]:

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 350 | Onroerende goederen bestemd voor verkoop | 50 | |
| | 320 | Goederen in bewerking | 100 | |
| aan | 489 | Andere diverse schulden | | 150 |

## Aankoop bebost terrein zonder vervreemding terrein na houtkap
In het geval dat de vennootschap een bebost terrein aankoopt en op het ogenblik van de verwerving niet de intentie heeft om het ontbost terrein te vervreemden, is de Commissie van oordeel dat enkel de houtcomponent mag worden verwerkt als goederen in bewerking. De terreincomponent zal worden geboekt op de rekening 220 *Terreinen*. Indien de vennootschap beslist na de houtkap het terrein toch te vervreemden zal enkel een overboeking naar rekening 26*Overige materiële vaste activa* noodzakelijk zijn.

*Voorbeeld*

NV XYZ betaalt 150 EUR voor een bebost terrein waarvan 1/3 van de aanschaffingswaarde correspondeert met de terreincomponent en 2/3 van de aanschaffingswaarde met de houtcomponent. De vennootschap heeft niet de intentie om de grond te vervreemden na de houtkap. Op datum van de verwerving wordt het volgende geboekt[^3]:

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 220 | Terreinen | 50 | |
| | 320 | Goederen in bewerking | 100 | |
| aan | 489 | Goederen in bewerking | | 150 |

[^1]: Onderhavig advies is tot stand gekomen nadat een ontwerp van het advies op 22 februari 2016 ter consultatie werd gepubliceerd op de website van de CBN.

[^2]: De bijhorende kosten verbonden aan de verwerving van het terrein worden buiten beschouwing gelaten.

[^3]: De bijhorende kosten verbonden aan de verwerving van het terrein worden buiten beschouwing gelaten.
