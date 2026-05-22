---
title: liquidatiereserve
tags:
- concept
- po-2-3
linked_anchors:
- 2.3.II.F
- 2.3.II.I
- 2.3.taak.2
- 2.3.taak.3
programmaonderdelen:
- '2.3'
confidence: grounded
node_type: ''
status: draft
schema_version: '2.0'
gegenereerd_uit: data/concepten/records/liquidatiereserve.json
gegenereerd_op: '2026-05-21'
---
#  ⚖️

> [!summary] Korte inhoud
> De liquidatiereserve is een facultatief fiscaal regime waarbij een kleine vennootschap een gedeelte of het geheel van haar boekhoudkundige winst na belasting boekt naar een afzonderlijke passiefrekening, tegen betaling van een anticipatieve aanslag van 10 % — waarna uitkering aan….

De liquidatiereserve is een facultatief fiscaal regime waarbij een kleine vennootschap een gedeelte of het geheel van haar boekhoudkundige winst na belasting boekt naar een afzonderlijke passiefrekening, tegen betaling van een anticipatieve aanslag van 10 % — waarna uitkering aan aandeelhouders bij ontbinding vrijgesteld is van roerende voorheffing, of bij tussentijdse uitkering na 5 jaar slechts 5 % roerende voorheffing verschuldigd is.



## Wat er economisch echt gebeurt 🔗

De vennootschap betaalt vandaag 10 % belasting op haar jaarwinst na vennootschapsbelasting als anticipatieve heffing — een soort vooruitbetaling op de latere uitkering. In ruil daarvoor zijn de gereserveerde bedragen bij effectieve uitkering slechts belast aan 5 % roerende voorheffing (na 5 jaar wachttijd) of 0 % bij vereffening, in plaats van het standaardtarief van 30 %. Het totale belastingeffect over de twee fasen bedraagt economisch gezien ca. 13,64 % (10 % + 5 % op het resterende 90 %) versus 30 % standaard — een aanzienlijk voordeel voor aandeelhouders-natuurlijke-personen die niet onmiddellijk liquiditeiten nodig hebben. Voor aandeelhouders-vennootschappen is het regime minder aantrekkelijk omdat DBI-aftrek dikwijls een betere piste is.


## Voorkennis & leespad

- **Lees eerst** (voorvereisten):
  [[vennootschapsbelasting]]
  [[kleine-vennootschap]]
  [[roerende-voorheffing-dividend]]

- **Past binnen kader**: [[vennootschapsbelasting]]

- **Naast deze fiche relevant**:
  [[vvprbis]]
  [[dividenduitkering]]
  [[liquidatiebonus]]

- **Bij vervolgvragen**:
  [[vereffening]]
  [[kapitaalvermindering]]



## Hoe het werkt

### Fase 1 — Aanleg: anticipatieve aanslag van 10 % ⚖️

Bij de jaarlijkse resultaatverwerking beslist de algemene vergadering om een gedeelte of het geheel van de boekhoudkundige winst na belasting (code 9905 jaarrekening NBB) over te boeken naar een afzonderlijke passiefrekening (subrekening per jaar van aanleg). Tegelijk wordt een afzonderlijke aanslag van 10 % gevestigd op het aangelegde bedrag. Deze aanslag staat los van de gewone vennootschapsbelasting en wordt samen met die belasting ingekohierd. De aanslag is definitief — niet verrekenbaar en niet terugbetaalbaar.

_Bron: WIB92 art. 184quater + art. 219quater; CBN-advies 2015/2 §Algemeen_

1. 1. Bestuursorgaan stelt jaarrekening op en bepaalt te bestemmen winst (code 9905).
2. 2. Algemene vergadering keurt jaarrekening goed, inclusief bestemming naar liquidatiereserve.
3. 3. Liquidatiereserve wordt geboekt op afzonderlijke passiefrekening (rek. 133X per jaar).
4. 4. Bijzondere aangifte ingediend + 10 % afzonderlijke aanslag betaald.
5. 5. Opgave gevoegd bij aangifte vennootschapsbelasting (model minister van Financiën).

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 6921 | Toevoeging aan de overige reserves | 1200 | None |
| 133X | Beschikbare reserves art. 184quater WIB92 (boekjaar N) | None | 1200 |

### FIFO-regel: oudste reserves worden eerst aangetast ⚖️

Indien een gedeelte van de liquidatiereserve wordt aangetast, worden de oudst gevormde reserves geacht eerst te zijn aangetast. Dit is wettelijk vastgelegd en bepaalt het tarief dat van toepassing is bij uitkering. Het is de reden waarom de CBN aanbeveelt om per jaar van aanleg een afzonderlijke subrekening bij te houden.

_Bron: WIB92 art. 184quater lid 4; CBN-advies 2015/2 §Vorming_

### Fase 2a — Uitkering na 5 jaar: 5 % roerende voorheffing ⚖️

Wanneer de liquidatiereserve wordt uitgedeeld als dividend en de reserve al gedurende minstens 5 jaar op de afzonderlijke rekening is gebleven (te rekenen vanaf de laatste dag van het belastbaar tijdperk van aanleg), bedraagt de roerende voorheffing 5 %. Gecombineerd met de 10 % anticipatieve aanslag bedraagt het totale fiscale gewicht ca. 13,64 % op de originele winst.

_Bron: WIB92 art. 269 §1 8°; CBN 2015/2 voetnoot 14_

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 694 | Vergoeding van het kapitaal | 1200 | None |
| 470 | Dividenden en tantièmes over vorige boekjaren | None | 1140 |
| 453 | Ingehouden voorheffingen (5 % van 1.200) | None | 60 |

### Fase 2b — Uitkering binnen 5 jaar: 15 % roerende voorheffing ⚖️

Wordt de liquidatiereserve uitgedeeld als dividend vóórdat de reserve 5 jaar oud is, bedraagt de roerende voorheffing 15 %. Gecombineerd met de 10 % anticipatieve aanslag wordt de effectieve belastingdruk hoger dan bij een gewone dividenduitkering aan 30 %. Dit is het voornaamste risico bij onverwachte vroegtijdige uitkering.

_Bron: WIB92 art. 269 §1 8°_

### Fase 2c — Uitkering bij ontbinding: vrijgesteld van roerende voorheffing ⚖️

Wanneer de liquidatiereserve wordt verdeeld ten gevolge van de ontbinding (vereffening) van de vennootschap, is geen roerende voorheffing verschuldigd. De liquidatiebonus die voortkomt uit de liquidatiereserve is vrijgesteld op grond van art. 21 11° WIB92. Dit maakt de liquidatiereserve tot het meest efficiënte instrument voor exit-planning via vereffening.

_Bron: WIB92 art. 21 11°; CBN 2015/2 §Boeking — noot 15_

### Uitsluiting: carried interest vehikel ⚖️

Een vennootschap kan de liquidatiereserve niet aanleggen zolang zij aandelen of deelbewijzen van een Carried interest vehikel bezit, met inbegrip van het jaar van definitieve vervreemding. Dit is een anti-misbruikbepaling.

_Bron: WIB92 art. 184quater laatste lid_



## Veelvoorkomende verwarringen

### Liquidatiereserve vs VVPRbis ⚖️

Beide regimes verlagen de roerende voorheffing bij uitkering, maar ze zijn niet combineerbaar op dezelfde reserves en werken fundamenteel anders. VVPRbis verlaagt de RV op dividend uit vers ingebracht kapitaal (15 % na 3 boekjaren na inbreng), zonder anticipatieve aanslag. Liquidatiereserve verlaagt via een anticipatieve 10 % aanslag bij aanleg tot 5 % RV na 5 jaar (of 0 % bij ontbinding). De keuze is definitief per schijf winst.

### Liquidatiereserve vs gewone liquidatiebonus ⚖️

De gewone liquidatiebonus (verschil vereffeningssaldo minus fiscaal gestort kapitaal) is belastbaar aan 30 % roerende voorheffing. De liquidatiebonus die voortkomt uit een liquidatiereserve is vrijgesteld (art. 21 11°). Dit onderscheid is cruciaal bij vereffening: de vereffenaar moet weten welk gedeelte van het eigen vermogen kwalificeert als liquidatiereserve.

### Afzonderlijke aanslag van 10 % is aftrekbaar als beroepskost ⚖️

De afzonderlijke aanslag van 10 % op de liquidatiereserve is GEEN belasting op winst in de klassieke zin; ze wordt geboekt als overige belasting (sub 6702). Ze is definitief verworven door de Staat — niet verrekenbaar met de gewone vennootschapsbelasting en eventuele overschotten zijn niet terugbetaalbaar. Aftrekbaarheid als beroepskost: te verifiëren.

### 5-jaar wachttijd berekend vanaf aanleg, niet vanaf uitkering ⚖️

De 5-jaartermijn loopt vanaf de laatste dag van het belastbaar tijdperk waarin de liquidatiereserve werd aangelegd. Een reserve aangelegd op 31/12/2025 wordt 5 jaar oud op 31/12/2030. Uitkeringen in 2031 komen dus in aanmerking voor 5 % RV. FIFO bepaalt welke schijf wordt aangetast.



## Wat dit record dekt

### Behandelde competenties (chronologisch)

1. **KMO-status van cliënt toetsen (art. 1:24 WVV)** — zie [KMO-status van cliënt toetsen (art. 1:24 WVV)](#kmo-vennootschap-uitkerend)2. **Beslissen of liquidatiereserve aanleggen zinvol is (timing-analyse)** — zie [Beslissen of liquidatiereserve aanleggen zinvol is (timing-analyse)](#fiscaal-adviseur-timing)3. **Aanleg boekhoudkundig verwerken (afzonderlijke subrekening per jaar)** — zie [Aanleg boekhoudkundig verwerken (afzonderlijke subrekening per jaar)](#boekhouder-aanleg)4. **Afzonderlijke aanslag 10 % berekenen en aangeven** — zie [Afzonderlijke aanslag 10 % berekenen en aangeven](#aanleg-liquidatiereserve)5. **FIFO-regel toepassen bij uitkering (oudste schijf eerst)** — zie [FIFO-regel toepassen bij uitkering (oudste schijf eerst)](#wachttermijn-fifo)6. **Uitkering na 5 jaar boekhoudkundig verwerken (5 % RV)** — zie [Uitkering na 5 jaar boekhoudkundig verwerken (5 % RV)](#boekhouder-uitkering)7. **Uitkering bij ontbinding verwerken (0 % RV)** — zie [Uitkering bij ontbinding verwerken (0 % RV)](#uitkering-bij-ontbinding)8. **Exit-planning adviseren via jaarlijkse opbouw liquidatiereserve** — zie [Exit-planning adviseren via jaarlijkse opbouw liquidatiereserve](#fiscaal-adviseur-exit-planning)9. **Toelichting jaarrekening over liquidatiereserves opstellen** — zie [Toelichting jaarrekening over liquidatiereserves opstellen](#boekhouder-toelichting-jaarrekening)
### Behandelde termen (alfabetisch)

- **afzonderlijke aanslag (10 %)** — zie [↑](#aanleg-liquidatiereserve)- **anticipatieve heffing** — zie [↑](#aanleg-liquidatiereserve)- **bijzondere liquidatiereserve (aanslagjaren 2013-2014)** — zie [↑](#aanleg-liquidatiereserve)- **boekhoudkundige winst na belasting (code 9905)** — zie [↑](#aanleg-liquidatiereserve)- **carried interest vehikel** — zie [↑](#carried-interest-uitsluiting)- **FIFO-regel liquidatiereserve** — zie [↑](#wachttermijn-fifo)- **kleine vennootschap** — zie [↑](#kmo-vennootschap-uitkerend)- **liquidatiebonus uit liquidatiereserve** — zie [↑](#verwarring-liquidatiebonus)- **liquidatiereserve** — zie [↑](#definitie)- **roerende voorheffing 5 %** — zie [↑](#uitkering-na-5-jaar)- **roerende voorheffing 15 % (voor 5 jaar)** — zie [↑](#uitkering-voor-5-jaar)- **vrijstelling bij vereffening** — zie [↑](#uitkering-bij-ontbinding)
### Behandelde formules

- {'naam': 'Afzonderlijke aanslag bij volledige aanleg', 'expressie': 'Aanslag = 10/110 × (boekhoudkundige winst na gewone VenB)'}
- {'naam': 'Effectief gecombineerd tarief na 5 jaar', 'expressie': '10 % + 5 % × (1 − 10 %) = 14,5 % [of ~13,64 % als de aanslag zelf meetelt in de basis]'}


