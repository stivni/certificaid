---
bron: https://www.cbn-cnc.be/nl/adviezen/renteloze-vorderingen-schulden-en-vorderingen-schulden-met-een-abnormaal-lage-rente-op
datum: 1986-09-01
gerelateerde_adviezen:
  - datum: '1993-02-28'
    titel: Actualisering van vorderingen en schulden op korte termijn (update)
    url: https://www.cbn-cnc.be/nl/adviezen/actualisering-van-vorderingen-en-schulden-op-korte-termijn-update
nummer: CBN-advies 137/4
provenance:
  generated_at: '2026-05-11T13:05:06Z'
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/renteloze-vorderingen-schulden-en-vorderingen-schulden-met-een-abnormaal-lage-rente-op
      sha256: 83a65bba87ad55a209a297397675381773d2a0fa8645a76b1147c23efa2f0782
      version:
  stale: false
  stale_reason:
  tooling:
    model:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    prompt_version:
  trust:
    confirmed_at: '2026-05-11T12:04:41Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      status: pass
      run_id: 20260511-130524
      run_at: '2026-05-11T13:05:26Z'
      heading_count: 12
      max_section_chars: 7707
      file_size_chars: 8375
      flags: []
    layer2:
      agent: subagent-sonnet-4-6
      concrete_problemen:
        - categorie: D2
          regel: 70
          type: missing-section
          voorbeeld: '### Renteloze vordering, éénmalig terugbetaalbaar na n jaar\n\n### Vordering met een abnormaal lage rente'
        - categorie: E2
          regel: 116
          type: other
          voorbeeld: '| | 493 | Over te dragen opbrengsten | | |'
        - categorie: A6
          regel: 100
          type: other
          voorbeeld: '...als\n\nzodanig geboekt.'
        - categorie: D2
          regel: 147
          type: missing-section
          voorbeeld: '#### Vaststelling van de actuele waarde en van het disconto\n\n### Actuele waarde...'
      rationale: 'Meerdere problemen: (1) D2: ### heading ''Renteloze vordering, éénmalig terugbetaalbaar na n jaar'' (regel 70) heeft geen body — de formule ontbreekt volledig, waarschijnlijk een afbeelding in de PDF die niet geëxtraheerd kon worden; zelfde voor headings op regels 72, 76, 80. (2) E2: boekingstabellen (regels 114-125) hebben lege Debet/Credit-cellen — waarden ontbreken. (3) A6: spurious line-break midden in een zin op regels 100-102 (''als \n\n zodanig geboekt''). (4) D2: voorbeeld-sectie (regels 147-175) heeft losstaande berekeningen zonder de bijhorende tabellen die in de PDF stonden.'
      run_at: '2026-05-11T12:04:41Z'
      status: needs-rework
    rationale: 'Meerdere problemen: (1) D2: ### heading ''Renteloze vordering, éénmalig terugbetaalbaar na n jaar'' (regel 70) heeft geen body — de formule ontbreekt volledig, waarschijnlijk een afbeelding in de PDF die niet geëxtraheerd kon worden; zelfde voor headings op regels 72, 76, 80. (2) E2: boekingstabellen (regels 114-125) hebben lege Debet/Credit-cellen — waarden ontbreken. (3) A6: spurious line-break midden in een zin op regels 100-102 (''als \n\n zodanig geboekt''). (4) D2: voorbeeld-sectie (regels 147-175) heeft losstaande berekeningen zonder de bijhorende tabellen die in de PDF stonden.'
    status: needs-rework
themas:
  - Vorderingen met een abnormaal lage rente
  - disconto
  - renteloze schulden
  - renteloze vorderingen
  - samengestelde intrest
  - schulden
  - schulden met een abnormaal lage rente
  - vordering
---

# CBN-advies 137/4 - Renteloze vorderingen (schulden) en vorderingen (schulden) met een abnormaal lage rente, op meer dan één jaar

Overeenkomstig artikel 27*bis*, § 2, eerste lid,* litt*. c) van het koninklijk besluit van 8 oktober 1976 wordt bij boeking voor haar nominale waarde van een vordering op meer dan één jaar, een disconto geboekt wanneer het gaat om een renteloze vordering of een vordering met een abnormaal lage rente. Dit disconto wordt in de overlopende rekeningen van het passief geboekt en pro rata temporis in resultaat genomen.

Artikel 27*bis*, § 4, stelt dat deze bepaling op overeenkomstige wijze van toepassing is op de renteloze schulden en schulden met een abnormaal lage rente op meer dan één jaar. 

Aan de Commissie werden verschillende vragen gesteld in verband met de berekeningswijze van het disconto en de betrokken boekingen.

## Berekening van het disconto 

Voor de berekening van het disconto moet de methode van het disconto bij samengestelde interest worden gebruikt. 

De berekening mag niet tegen enkelvoudige interest gebeuren. Vooral voor vorderingen op middellange en lange termijn, leidt deze methode tot een overwaardering van het disconto en een onderwaardering van de actuele waarde, waardoor, vanaf een bepaalde duur, deze actuele waarde zelfs negatief wordt; hieruit blijkt dat deze methode fundamenteel ongeschikt is. 

Het op de overlopende rekening te boeken disconto (E) is gelijk aan het verschil tussen de nominale waarde van de vordering of van de schuld (C) en de actuele waarde (c), berekend tegen marktrente (i), van de kasstromen die de vordering of schuld doet ontstaan. 

In dit advies wordt enkel ingegaan op de boekhoudtechnische implicaties terzake. Het is dus geenszins bedoeld als een overzicht van de mogelijk toepasselijke technieken van financiële algebra op zeer uiteenlopende concrete situaties. Evenwel zullen de vaakst voorkomende gevallen hierna worden toegelicht. 

### Renteloze vordering, éénmalig terugbetaalbaar na n jaar 

Vordering met een abnormaal lage rente (i'), éénmalig terugbetaalbaar na n jaar.
De actuele waarde is hier gelijk aan het totaal van de geactualiseerde waarde van de vordering op de vervaldag en de actuele waarde van een annuïteit overeenstemmend met de rentevergoeding :

### Vordering terugbetaalbaar via vaste annuïteiten 

De actuele waarde van de vordering is gelijk aan de geactualiseerde waarde van de annuïteiten, ongeacht de vordering renteloos of tegen een abnormaal lage rente is aangegaan.

Renteloze vordering of vordering met een abnormaal lage rente, terugbetaalbaar anders dan op vaste termijn of tegen constante annuïteiten
In dit geval dienen alle kasstromen (V1 ... Vk) afzonderlijk te worden geactualiseerd tegen de marktrente naar hun respectievelijke looptijden (n 1 ... n k). Hun som geeft de actuele waarde van de vordering weer. 

Wanneer de resterende looptijd van de vordering niet in volle jaren is uitgedrukt, bestaat de factor "n" uit een decimale fractie van een jaar. Het is een gangbare praktijk in dergelijk geval de actuele waarde zoals berekend voor een volledig jaar te vermenigvuldigen met 1 / (1 + i)t.

De waarde per maand, van deze fractie, voor een interestvoet gaande van 6 tot en met 10,5 % is in de tabel in bijlage vermeld. 

Wanneer het een vordering op meer dan één jaar betreft wordt het disconto berekend op het geheel van de verschuldigde stortingen en niet enkel op deze die na één jaar vervallen. De stortingen die tijdens het jaar vervallen op een vordering op meer dan één jaar zijn dus begrepen in de berekening van de actuele waarde van de vordering en het disconto.

## Boekhoudkundige verwerking 

### Boeking van het disconto 

Artikel 27*bis*, § 2 van het koninklijk besluit van 8 oktober 1976 bepaalt dat het disconto in de overlopende rekeningen van het passief (rekening 493) wordt geboekt wanneer het om een vordering gaat. Betreft het een schuld, dan wordt het disconto geboekt in de overlopende rekeningen van het actief (rekening 490). 

Het besluit bepaalt niet uitdrukkelijk onder welke rubriek het disconto aan het resultaat moet worden toegerekend. Deze toerekening dient te gebeuren volgens de aard van de verrichting die aan de renteloze vordering of aan de vordering tegen abnormaal lage rente ten grondslag ligt. 

Wanneer de vordering (schuld) verband houdt met hetzij als opbrengsten (kosten) in de resultatenrekening opgenomen bedragen, hetzij de prijs van de overdracht (aanschaffing) van vaste activa, dan dient het disconto te worden beschouwd als een regularisatie van het betrokken resultaat of als een vermindering van de overdracht- of aanschaffingsprijs van het betrokken actief. 

Ingeval het ontbreken van een interestvergoeding op een vordering het gevolg is van een gerechtelijk akkoord, dan wordt het disconto beschouwd als een waardevermindering op de vordering en als 

zodanig geboekt. Indien een onderneming in het kader van een gerechtelijk akkoord het voordeel van een renteloze schuld bekomt, vertegenwoordigt het disconto een uitzonderlijk resultaat (764 tot 769 Andere uitzonderlijke opbrengsten). 

### Het disconto wordt pro rata temporis in resultaat genomen 

De toepassing van de actuariële methode voor de berekening van het disconto impliceert dat de toekomstige inresultaatneming volgens dezelfde methode plaatsvindt. Zij veronderstelt aldus een heractualisering van de toekomstige kasstromen op elke balansdatum. Deze heractualisering dient te geschieden tegen de oorspronkelijke actualisatievoet en niet tegen de marktrente op balansdatum. 

Het verstreken disconto wordt in resultaat genomen als financieel resultaat. 

De boekingen zijn : 

1. Bij een vordering :

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 493 | Over te dragen opbrengsten | | |
| aan | 750 | Opbrengsten uit financiële vaste activa | | |
| | 751 | Opbrengsten uit vlottende activa | | |

2. Bij een schuld : 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 650 | Kosten van schulden | | |
| aan | 490 | Over te dragen kosten | | |

## De actualisatievoet 

Het koninklijk besluit van 8 oktober 1976 bepaalt dat het disconto wordt berekend op basis van de voor dergelijke vorderingen geldende marktrente op het ogenblik waarop de vordering is opgenomen in het vermogen van de onderneming. 

Gezien het per definitie gaat om vorderingen (schulden) op middellange of lange termijn, wordt "de voor dergelijke vorderingen geldende marktrente" vastgesteld onder verwijzing naar een marktrente op middellange of lange termijn zoals bij voorbeeld de rente op kasbons met een gelijkaardige looptijd uitgegeven door de kredietinstellingen, de door de kredietinstellingen aangerekende rente op kredieten van overeenkomende duur op het brutorendement op overheidsfondsen met een overeenkomende resterende looptijd, zoals dit uit de beursnotering blijkt. 

De rente van de kapitaalmarkt op korte termijn zoals de discontovoet of de rente op voorschotten van overheidsfondsen van de Nationale Bank van België vormen in principe een minder geschikte referentiebasis voor dergelijke vorderingen. 

In deze context wordt erop gewezen dat, voor de toepassing van de inkomstenbelastingen, de actualisatievoet de discontovoet van de Nationale Bank van België niet mag overschrijven[^1]. 

*Voorbeeld*

Gegevens: 

Een vordering van 100 000 BEF, verkregen op 30 september 1985 tegen een interestvoet van 3 %, is terugbetaalbaar als volgt : 

20 000 op 31 december 1986 30 000 op 31 december 1987 50 000 op 31 december 1988. 

De interest wordt jaarlijks op 31 december geïnd, te beginnen vanaf 1986. De marktrente bedraagt 9 %.

#### Vaststelling van de actuele waarde en van het disconto 

### Actuele waarde van de kasstromen 

*- Op 31 december 1985*

(1) Art. 25*bis*, § 3, WIB.

*- Op 30 september 1985* 

88.823 x 0,9789 = 86.931 

### Disconto op 30 september 1985 

100 000 (nominale waarde) - 86 931 (actuele waarde) = 13 069 

#### Evolutie van de actuele waarde en van het disconto

(1) (32.400 x 0,9174) + (51.500 x 0,8416)

(2) (51.500 x 0,9174)

#### Boekingen 

 (1) 3 750 (interest) + 4 243 (vermindering van het disconto). 

(2) 2 400 (interest) + 4 180 (vermindering van het disconto). 

(3) 1 500 (interest) + 2 754 (vermindering van het disconto).

[^1]: WIB, art. 25bis, § 3.
