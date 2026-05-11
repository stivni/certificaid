---
bron: https://www.cbn-cnc.be/nl/adviezen/actuarieel-rendement-op-vastrentende-effecten-aanpassing-van-de-adviezen-1375-en-1484
datum: 1993-12-01
gerelateerde_adviezen:
  - datum: '1992-02-01'
    titel: Inresultaatneming van het actuariële rendement van vastrentende effecten
    url: https://www.cbn-cnc.be/nl/adviezen/inresultaatneming-van-het-actuariele-rendement-van-vastrentende-effecten
nummer: CBN-advies 148/5
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/actuarieel-rendement-op-vastrentende-effecten-aanpassing-van-de-adviezen-1375-en-1484
      sha256: 9a05429dbe510b4e87feb0e2aabca76f9ed492da6f32da5e1fac2cd203f35761
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-11T15:15:31Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T17:05:21Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "E2 (regel 245): 'aan 751 Opbrengsten uit vlottende activa' samengesmolten in één tabelcel — ongewijzigd t.o.v. ronde 2. E2 (regel 256): losse cijferrij '| | 124.553 | | | |' buiten tabelcontext — ongewijzigd. Nieuw gevonden: E2 (regel 234) rekening '52' gelabeld als 'Kredietinstellingen' i.p.v. '55'; B1 (regel 71) heading '## 1 jaar : 80 000' bevat enkel jaar en bedrag."
    layer1:
      file_size_chars: 9362
      flags: []
      heading_count: 7
      max_section_chars: 4403
      run_at: '2026-05-11T15:05:49Z'
      run_id: 20260511-150547
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T17:05:21Z'
      rationale: "E2 (regel 245): 'aan 751 Opbrengsten uit vlottende activa' samengesmolten in één tabelcel — ongewijzigd t.o.v. ronde 2. E2 (regel 256): losse cijferrij '| | 124.553 | | | |' buiten tabelcontext — ongewijzigd. Nieuw gevonden: E2 (regel 234) rekening '52' gelabeld als 'Kredietinstellingen' i.p.v. '55'; B1 (regel 71) heading '## 1 jaar : 80 000' bevat enkel jaar en bedrag."
      concrete_problemen:
        - regel: 245
          categorie: E2
          type: other
          voorbeeld: '| | aan 751 Opbrengsten uit vlottende activa | 13.027 | | |'
        - regel: 256
          categorie: E2
          type: other
          voorbeeld: '| | 124.553 | | | |'
        - regel: 234
          categorie: E2
          type: other
          voorbeeld: '| aan | 52 | Kredietinstellingen | | 1.205.000 |'
        - regel: 71
          categorie: B1
          type: other
          voorbeeld: '## 1 jaar : 80 000'
themas:
  - actuarieel rendement op vastrentende effecten
  - actuariële rendement
  - kapitalisatiebon
  - toerekening van kosten en opbrengsten
  - vastrentende effecten
---

# CBN-advies 148/5 - Actuarieel rendement op vastrentende effecten - Aanpassing van de adviezen 137/5 en 148/4

Artikel 27*bis*, § 3 van het koninklijk besluit van 8 oktober 1976, zoals gewijzigd door het koninklijk besluit van 30 december 1991, bepaalt dat wanneer het actuariële rendement van vastrentende effecten berekend bij de aankoop, met inachtneming van hun terugbetalingswaarde op vervaldag, verschilt van hun nominaal rendement, het verschil tussen de aanschaffingswaarde en de terugbetalingswaarde *pro rata temporis* over de resterende looptijd van de effecten in resultaat wordt genomen als bestanddeel van de renteopbrengst, en naar gelang van het geval toegevoegd aan of afgetrokken van de aanschaffingswaarde van de effecten.

Dit principe geldt zowel voor de inschrijver of de koper als voor de emittent. Ingevolge voornoemde wijziging doorgevoerd door het K.B. van 30 december 1991, zijn de adviezen 137/5 en 148/4 achterhaald. De Commissie heeft het nuttig geacht deze nieuwe waarderingsregels toe te lichten door aanpassing van het voorbeeld dat zij verstrekte in advies 148/4[^1]. 

**HYPOTHESE**

Een kapitalisatiebon wordt uitgegeven en er wordt op ingeschreven voor 1 000 000, terugbetaalbaar na vijf jaar tegen 1 469 328. Het verschil tussen uitgifteprijs en terugbetalingsprijs stemt overeen met een actuarieel rendement van 8 %.

De roerende voorheffing bedraagt 10 %.

De gekapitaliseerde rente bedraagt pro rato : na

## 1 jaar : 80 000

2 jaar : 166 400 

3 jaar : 259 712 

4 jaar : 360 489 

5 jaar : 469 328 

Na drie jaar wordt de kapitalisatiebon overgedragen voor de prijs (kosten niet inbegrepen) van 1 205 000. 

## BOEKINGEN BIJ DE EMITTENT

**Bij uitgifte** 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 55 | Kredietinstellingen | 1.000.000 | |
| aan | 17 | Schulden op meer dan één jaar | | 1.000.000 |

**Na 1 jaar**

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 65 | Financiële kosten | 80.000 | |
| aan | 17 | Schulden op meer dan één jaar | | 80.000 |

**Na 2 jaar**

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 65 | Financiële kosten | 86.400 | |
| aan | 17 | Schulden op meer dan één jaar | | 86.400 |

**Na 3 jaar**

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 65 | Financiële kosten | 93.312 | |
| aan | 17 | Schulden op meer dan één jaar | | 93.312 |

**Na 4 jaar**

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 65 | Financiële kosten | 100.777 | |
| aan | 17 | Schulden op meer dan één jaar | | 100.777 |

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 17 | Schulden op meer dan één jaar | 1.360.489 | |
| aan | 42 | Schulden op meer dan één jaar die binnen het jaar vervallen | | 1.360.489 |

**Na 5 jaar**

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 65 | Financiële kosten | 108.839 | |
| aan | 42 | Schulden op meer dan één jaar die binnen het jaar vervallen | | 108.839 |

## Bij de terugbetaling

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 42 | Schulden op meer dan één jaar | 1.469.328 | |
| aan | 453 | Ingehouden voorheffingen | | 46.933 |
| | 55 | Kredietinstellingen | 1.422.395 | |

## Boeking bij de oorspronkelijke inschrijver

**Bij de inschrijving**

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 52 | Vastrentende effecten | 1.000.000 | |
| aan | 55 | Kredietinstellingen | | 1.000.000 |

**Na 1 jaar**

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 52 | Vastrentende effecten | 72.000 | |
| | 6700 | Verschuldigde of gestorte belastingen en voorheffingen | 8.000 | |
| aan | 751 | Opbrengsten uit vlottende activa | | 80.000 |

**Na 2 jaar**

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 52 | Vastrentende effecten | 77.760 | |
| | 6700 | Verschuldigde of gestorte belastingen en voorheffingen | 8.640 | |
| aan | 751 | Opbrengsten uit vlottende activa | | 86.400 |

**Na 3 jaar**

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 52 | Vastrentende effecten | 83.981 | |
| | 6700 | Verschuldigde of gestorte belastingen en voorheffingen | 9.331 | |
| aan | 751 | Opbrengsten uit vlottende activa | | 93.312 |

**Bij de overdracht**

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 55 | Kredietinstellingen | 1.205.000 | |
| | 652 | Minderwaarden op de realisatie van vlottende activa | 28.741 | |
| aan | 52 | Vastrentende effecten | | 2.233.741 |

## Boekingen bij de koper

**Bij de verwerving** 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 52 | Vastrentende effecten | 1.205.000 | |
| aan | 55 | Kredietinstellingen | | 1.205.000 |

Het rendement voor de koper wordt dan : 

1 205 000 x (1+ i)exp2 = 1 443 357 [= 1 469 328 - 25 971] 

i = (1 443 357/1 205 000)exp1/2 - 1 = 9,44435 % 

en het actuariële rendement 

van het vierde jaar : 113 804 

van het vijfde jaar : 124 553 

**Na 4 jaar** 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 52 | Vastrentende effecten | 103.726 | |
| | 6700 | Verschuldigde of gestorte belastingen en voorheffingen | 10.078 | |
| aan | 751 | Opbrengsten uit vlottende activa | | 113.804 |

**Na 5 jaar** 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 52 | Vastrentende effecten | 113.669 | |
| | 6700 | Verschuldigde of gestorte belastingen en voorheffingen | 10.884 | |
| aan | 751 | Opbrengsten uit vlottende activa | | 124.553 |

## Bij de terugbetaling

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 55 | Kredietinstellingen | 1.422.395 | |
| aan | 52 | Vastrentende effecten | | 1.422.395 |

Aan de Commissie werd een alternatieve methode voorgesteld voor de boeking bij de koper, wanneer die aankoop, zoals in bovenstaand voorbeeld, geschiedt tegen een prijs die verschilt van de theoretische waarde van het effect, berekend op basis van de interestvoet zoals die voortvloeit uit de uitgiftevoorwaarden. Deze alternatieve methode heeft betrekking op de boeking van het effect bij aankoop tegen theoretische waarde, waarbij het verschil op een overlopende rekening wordt geboekt, naargelang van het geval, aan actief- of aan passiefzijde, en later gespreid in resultaat genomen over de resterende looptijd. 

In bovenstaand voorbeeld, zou die boeking er dan als volgt uitzien (in de boeken van de koper) : 

**Bij de aankoop** 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 52 | Vastrentende effecten | 1.422.395 | |
| aan | 52 | Kredietinstellingen | | 1.205.000 |
| | 493 | Over te dragen opbrengsten | 28.741 | |

**Na 4 jaar** 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 52 | Vastrentende effecten | 90.699 | |
| | 6700 | Verschuldigde of gestorte belastingen en voorheffingen | 10.078 | |
| aan | 751 | Opbrengsten uit vlottende activa | | 100.777 |
| | 493 | Over te dragen opbrengsten | 13.027 | |
| | aan 751 Opbrengsten uit vlottende activa | 13.027 | | |

**Na 5 jaar** 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 52 | Vastrentende effecten | 97.955 | |
| | 6700 | Verschuldigde of gestorte belastingen en voorheffingen | 10.884 | |
| aan | 751 | Opbrengsten uit vlottende activa | | 108.839 |
| | 493 | Over te dragen opbrengsten | 15.714 | |
| aan | 751 | Opbrengsten uit vlottende activa | | 15.714 |
| | 124.553 | | | |

## Bij de terugbetaling

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 55 | Kredietinstellingen | 1.422.395 | |
| aan | 52 | Vastrentende effecten | | 1.422.395 |

In dit boekingsschema stemmen de boekingen bij de emittent overeen met die bij de koper. Er is een mechanische relatie tussen het bedrag van de roerende voorheffing en de rente op de hoofdsom, zonder rekening te houden met de in resultaatneming van het prijsverschil dat enkel betrekking heeft op de relaties tussen de verkoper en de koper. 

Deze alternatieve boekingswijze heeft op resultaatniveau hetzelfde effect als de eerste methode: het verschil zit hierin, dat de effecten niet in de boekhouding worden opgenomen tegen aanschaffingswaarde, aangepast op basis van de gelopen interesten. Die waarde wordt uitgesplitst over twee balansposten. 

Hoewel die methode minder nauw aansluit bij het voorschrift van artikel 27*bis*, § 3 van het koninklijk besluit van 8 oktober 1976, is de Commissie van oordeel dat zij ten gronde geen bezwaren oproept. Weliswaar moet, voor de toepassing van waardeverminderingen om rekening te houden met de marktwaarde, uiteraard het (algebraïsche) totaal van beide balansposten tegenover de marktwaarde worden geplaatst.

[^1]: Bull. CBN nr. 25, juni 1990.
