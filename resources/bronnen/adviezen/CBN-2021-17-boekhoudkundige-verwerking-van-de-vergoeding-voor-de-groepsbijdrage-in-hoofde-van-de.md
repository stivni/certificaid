---
bron: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-de-vergoeding-voor-de-groepsbijdrage-in-hoofde-van-de
datum: 2021-12-22
gerelateerde_adviezen:
  - datum: '2019-07-02'
    titel: Groepsbijdrage
    url: https://www.cbn-cnc.be/nl/adviezen/groepsbijdrage
nummer: CBN-advies 2021/17
themas:
  - groepsbijdrage
  - belastingen
  - fiscale consolidatie
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-de-vergoeding-voor-de-groepsbijdrage-in-hoofde-van-de
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: f1177ef
    model:
    prompt_version:
  generated_at: '2026-05-12T23:23:43Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-12T23:30:18Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: Geen ETL-artefacten aangetroffen. Heading-structuur aanwezig (8 headings), inhoud volledig, voetnoten correct gerenderd, geen form-feeds of column-bleed.
    layer1:
      status: pass
      run_id: 20260512-232428
      run_at: '2026-05-12T23:24:33Z'
      heading_count: 7
      max_section_chars: 1362
      file_size_chars: 4249
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-12T23:30:18Z'
      rationale: Geen ETL-artefacten aangetroffen. Heading-structuur aanwezig (8 headings), inhoud volledig, voetnoten correct gerenderd, geen form-feeds of column-bleed.
      concrete_problemen: []
---
# CBN-advies 2021/17 – Boekhoudkundige verwerking van de vergoeding voor de groepsbijdrage in hoofde van de overdragende vennootschap bij gebrek aan Belgische belastingen op het resultaat op rekening 4500 (addendum bij advies 2019/06)

## Inleiding
Naar aanleiding van een vraag aan de Commissie voor boekhoudkundige normen werd vastgesteld dat een bepaalde situatie niet wordt behandeld in CBN-advies 2019/06 – *Groepsbijdrage*, meer bepaald het boeken van de vergoeding voor de groepsbijdrage in hoofde van de overdragende vennootschap.

In voormeld advies wordt gesteld dat de groepsbijdrage-overeenkomst boekhoudkundig als volgt moet worden verwerkt: op balansdatum van boekjaar N wordt de geraamde belastingschuld geboekt door debitering van rekening 6702 Geraamde belastingen met als tegenpost rekening 4500 *Belgische winstbelastingen*. In het volgende boekjaar (N+1), bij de afsluiting van de groepsbijdrage-overeenkomst, wordt rekening 4500* Belgische winstbelastingen* gedebiteerd met als tegenpost de boeking van een schuld (rekening 489 *Diverse schulden*) aan de groepsvennootschap waarmee de groepsbijdrage-overeenkomst werd gesloten.

Deze boekhoudkundige verwerking kan evenwel niet worden toegepast indien rekening 4500 *Belgische winstbelastingen* niet voldoende werd gecrediteerd op balansdatum van boekjaar N. Dit kan bijvoorbeeld voorvallen wanneer de overdragende vennootschap winst boekt en tegelijk recupereerbare fiscale verliezen heeft.

In onderhavig addendum verduidelijkt de Commissie de boekhoudkundige verwerking van de vergoeding voor de groepsbijdrage in laatstgenoemd geval.

## Boekhoudkundige verwerking
Gelet op het voorgaande is de Commissie van oordeel dat de vennootschap die de vergoeding voor de groepsbijdrage verschuldigd is, bij de afsluiting van de groepsbijdrage-overeenkomst, rekening 6710 *Verschuldigde of gestorte belastingsupplementen* dient te debiteren en rekening 489 *Diverse schulden* dient te crediteren ten belope van het bedrag van de belasting die wordt uitgespaard.

## Voorbeeld
Binnenlandse vennootschappen A en B, die beide het boekjaar afsluiten op 31/12/N, voldoen aan de voorwaarden om de aftrek van de groepsbijdrage toe te passen.

In de loop van het boekjaar dat eindigt op 31/12/N realiseerde vennootschap A, vóór toepassing van de groepsbijdrage, een fiscaal verlies van 100.000 euro.

In de loop van hetzelfde boekjaar (N) behaalde vennootschap B, vóór toepassing van de groepsbijdrage, een fiscaal resultaat van 80.000 euro. Daarnaast had vennootschap B verrekenbare verliezen van 120.000 euro. De geraamde fiscale lasten van de vennootschap B waren dus nihil voor boekjaar N.

Vennootschap A en vennootschap B sluiten in jaar N+1 een groepsbijdrage-overeenkomst voor een bedrag van 80.000 euro.

De belastingbesparing die vennootschap B naar aanleiding van de groepsbijdrage realiseert, wordt geraamd op 20.000 euro[^2]. De vergoeding die vennootschap B verschuldigd is aan vennootschap A bedraagt aldus 20.000 euro.

De groepsbijdrage vindt plaats buiten de boekhouding om en geeft op zich dus geen aanleiding tot een boeking.

De vergoeding voor de groepsbijdrage wordt als volgt verwerkt:

In hoofde van vennootschap B

## Bij de eindejaarsverrichtingen op 31/12/N
Vennootschap B boekt geen geraamde belastingen op rekening 6702.

## Bij het sluiten van de groepsbijdrage-overeenkomst (in boekjaar N+1)
| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 6710 | Verschuldigde of gestorte belastingsupplementen | 20.000 | |
| aan | 489 | Overige schulden | | 20.000 |

In hoofde van vennootschap A

## Bij de eindejaarsverrichtingen op 31/12/N
Er vindt geen boeking plaats.

## Bij het sluiten van de groepsbijdrage-overeenkomst (in boekjaar N+1)
| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 2810 | Vorderingen op rekening | 20.000 | |
| aan | 764 | Andere niet-recurrente bedrijfsopbrengsten | | 20.000 |

[^1]: Onderhavig advies is tot stand gekomen nadat het ontwerpadvies op 9 augustus 2021 ter publieke consultatie werd gepubliceerd op de website van de CBN.

[^2]: Er wordt in dit voorbeeld uitgegaan van een tarief van de vennootschapsbelasting van 25 procent.
