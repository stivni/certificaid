---
title: Opbrengsten onder IFRS (IFRS 15) — 5-stappen-model
tags:
- concept
- cluster
- po-1-5
linked_anchors:
- 1.5.V.D
- 1.5.V
programmaonderdelen:
- '1.5'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/opbrengsten-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Opbrengsten onder IFRS (IFRS 15) — 5-stappen-model 🤖

IFRS 15 — Opbrengsten van contracten met klanten vervangt sinds 1 januari 2018 IAS 18 (Opbrengsten uit gewone activiteiten) en IAS 11 (Onderhanden projecten in opdracht van derden). Het **kernprincipe** (alinea 2): een entiteit neemt opbrengsten op om de overdracht van beloofde goederen of diensten aan klanten weer te geven, voor een bedrag dat de vergoeding weerspiegelt waarop de entiteit recht zal hebben in ruil. De toepassing volgt een **5-stappen-model**: (1) identificeer het contract met de klant; (2) identificeer de prestatieverplichtingen in het contract; (3) bepaal de transactieprijs; (4) wijs de transactieprijs toe aan de prestatieverplichtingen; (5) neem opbrengsten op wanneer (of naarmate) een prestatieverplichting wordt vervuld. Het model is **principe-georiënteerd** en geldt voor alle sectoren, met uitzondering van leasing (IFRS 16), verzekeringen (IFRS 17) en financiële instrumenten (IFRS 9).


## Berekening

### Significante financieringscomponent (IFRS 15) — contante waarde van uitgestelde betalingen

**Contante waarde van een reeks gelijke jaarlijkse betalingen (annuïteit-achterstal)** 
```
CW = Σ_{t=1..n} K / (1+r)^t = K × [1 − (1+r)^(−n)] / r
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `CW` | Contante verkoopprijs op contractdatum = transactieprijs onder IFRS 15 (alinea 61). | EUR |
| `K` | Vaste jaarlijkse termijn die de klant betaalt. | EUR |
| `r` | Disconteringspercentage bij contractaanvang: het percentage dat tot uitdrukking zou komen in een afzonderlijke financieringstransactie tussen entiteit en klant (alinea 64) — typisch de marktrente op de kredietmarkt voor vergelijkbaar krediet aan dezelfde klant. | decimaal (bv. 0,09 voor 9 %) |
| `n` | Aantal jaarlijkse termijnen. | jaren |

**Voorbeeld-invulling**: Zelena Bio NV verkoopt op 5 februari 2026 een productielijn voor nominaal € 5.000.000, betaalbaar in 5 gelijke jaarlijkse termijnen van € 1.000.000. Het contract verhoogt de prijs met 4 %/jaar contract-interest (€ 600.000 in totaal) → totaal te ontvangen € 5.600.000 in 5 stortingen. Marktrente voor vergelijkbaar krediet: 9 %.

```
Termijn K = € 5.600.000 / 5 = € 1.120.000. CW = 1.120.000 × [1 − (1,09)^(−5)] / 0,09 = 1.120.000 × 3,88965 = € 4.356.408. NB: de officiële ITAA-vraag (2014-1-vr4) start van K = € 1.000.000 (nominale termijn zonder contract-interest) en presenteert de extra 4 %-component apart; in dat geval is omzet = 5.600.000 − 600.000 (contract-interest) − 404.706 (disconto t.o.v. 9 % marktrente) = € 4.595.294.
```

_Resultaat in EUR_
**Splitsing nominale vergoeding in opbrengst + financiering** 
```
Opbrengst (rekening 70) = CW;  Te ontwikkelen renteopbrengst over de looptijd = Σ termijnen − CW
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `Opbrengst_70` | Bedrag dat bij overdracht zeggenschap op rekening 70 — Omzet wordt geboekt (= contante verkoopprijs). | EUR |
| `Rente_751` | Cumulatieve renteopbrengst (rekening 751 — opbrengsten uit vlottende activa / financieel resultaat) te ontwikkelen over de looptijd via effectieve-rentemethode. Onder IFRS 15 alinea 65 afzonderlijk te presenteren van opbrengsten uit contracten met klanten. | EUR |
| `Disconto_651` | Het deel van de contract-interest dat afwijkt van de marktrente, BE-GAAP-style geboekt op 651 (financiële kosten / disconto op vorderingen). Onder IFRS 15: er is geen aparte 'disconto'-categorie — alles wordt via effectieve-rente verdeeld als rentecomponent. | EUR |

**Voorbeeld-invulling**: Zelena-scenario (zie boven). Nominaal € 5.600.000, omzet € 4.595.294, te ontwikkelen renteopbrengsten € 600.000 (contract-interest) + 'gerealiseerd' disconto € 404.706 (verschil contract-interest 4 % vs. marktrente 9 %) over de 5 termijnen.

```
Omzet 70 = 4.595.294. Cumulatieve financiële component over 5 jaar = 5.600.000 − 4.595.294 = 1.004.706, opgesplitst (BE-GAAP-rekeningenstelsel) in interest 751 € 600.000 + disconto 651 € 404.706 over de 5 terugbetalingstermijnen. Onder IFRS 15 (alinea 65): één renteopbrengst-lijn, afzonderlijk van omzet, via effectieve-rentemethode.
```

_Resultaat in EUR_

## In de praktijk

<h3 id="verkoop-op-afbetaling-met-looptijd-1-jaar-typisch-dossier">Verkoop op afbetaling met looptijd > 1 jaar — typisch dossier</h3>

> [!tip]- Verkoop op afbetaling met looptijd > 1 jaar — typisch dossier
> Een stagiair-gecertificeerd accountant ziet deze configuratie typisch bij B2B-investeringsgoederen (machines, productielijnen, vrachtwagens), grondverkopen tussen verbonden partijen en bouwprojecten met geactiveerde betalingsschema's. Eerste reflex onder IFRS 15: looptijd > 1 jaar → financieringscomponent significant (alinea 60), praktische oplossing alinea 63 valt weg. Omzet ≠ nominaal contractbedrag — omzet = contante verkoopprijs op overdrachtsdatum. Het verschil wordt rente, niet omzet, en wordt afzonderlijk gepresenteerd in het overzicht van het totaalresultaat (alinea 65). ⚖️

<h3 id="disconteringspercentage-kiezen-niet-de-contract-rente">Disconteringspercentage kiezen — niet de contract-rente</h3>

> [!tip]- Disconteringspercentage kiezen — niet de contract-rente
> Een veelgemaakte fout: de in het contract vermelde rente (hier 4 %) gebruiken om de financieringscomponent te bepalen. Alinea 64 vereist dat de entiteit het percentage gebruikt dat in een afzonderlijke financieringstransactie tussen entiteit en klant tot uitdrukking zou komen — dus de **markt**rente voor vergelijkbaar krediet (hier 9 %). Als de contractuele rente onder de marktrente ligt, wordt het verschil (in dit voorbeeld € 404.706) extra rente onder IFRS 15, en omzet zakt evenredig. Dit percentage wordt na contractaanvang niet meer geactualiseerd (alinea 64, slot). ⚖️

<h3 id="presentatie-in-w-v-rente-apart-van-omzet">Presentatie in W&V — rente apart van omzet</h3>

> [!tip]- Presentatie in W&V — rente apart van omzet
> Onder IFRS 15 alinea 65 worden renteopbrengsten of rentelasten afzonderlijk gepresenteerd van opbrengsten uit contracten met klanten. Belgisch GAAP-rekeningenstelsel splitst de financieringscomponent traditioneel in (a) contract-interest op 751 — Opbrengsten uit vlottende activa, en (b) disconto-effect t.o.v. marktrente op 651 — Disconto op vorderingen. Voor een IFRS-rapporterende entiteit: één rentelijn, niet uitgesplitst. Voor een BE-GAAP-rapporterende entiteit: behoud van de 751/651-splitsing over de terugbetalingstermijnen, conform CBN-leer. ⚖️


## Stappen

### 1. Identificeer het contract met de klant

Een contract is alleen administratief te verwerken onder IFRS 15 als VIJF criteria vervuld zijn (alinea 9): (a) partijen hebben het contract goedgekeurd en zich verbonden tot nakoming; (b) rechten over te dragen goederen/diensten zijn identificeerbaar; (c) betalingsvoorwaarden zijn identificeerbaar; (d) het contract heeft economische betekenis; (e) inbaarheid van de vergoeding is waarschijnlijk.

**Waarom?** Een contract is de basis: zonder afdwingbare rechten en verplichtingen ontstaan er geen prestatieverplichtingen en dus geen IFRS 15-opbrengst. Het waarschijnlijkheidscriterium (e) sluit klanten met onbetwijfeld slecht krediet uit van opbrengstopname.

**📥 Input**:
- Schriftelijk of mondeling contract met klant → **Voorwaarden** _(contractdocument)_

**📤 Output**:
- Boekhoudkundige bestempeling → **Contract erkend onder IFRS 15** _(beslissing)_

**🛠️ Hoe**:

1. Zelena Bio NV ontvangt een bestelling van Brugse Brouwerij BV voor 500.000 doseflesjes ingrediënt X, prijs € 0,80/flesje (€ 400.000 totaal), levering Q3 2026, betaling 60 dagen na levering.
2. Check criterium (a): Brugse heeft schriftelijke bestelorder gestuurd, Zelena heeft die bevestigd. → OK.
3. Check (b): 500.000 doseflesjes ingrediënt X — duidelijk geïdentificeerd. → OK.
4. Check (c): € 0,80/flesje, betaling 60 dagen. → OK.
5. Check (d): Zelena verwacht een nieuwe kasstroom; Brugse krijgt een bedrijfsmiddel. → OK.
6. Check (e): Brugse is een gevestigde klant met goede betaalhistoriek. → OK.
7. Contract is opneembaar onder IFRS 15.

> [!example]- Voorbeeld: Brugse Brouwerij BV sluit een contract met Aurelia Holding NV voor leveringen van bier gedurende 2 jaar, met een vaste v…
> Brugse Brouwerij BV sluit een contract met Aurelia Holding NV voor leveringen van bier gedurende 2 jaar, met een vaste vergoeding van € 240.000.
>
> 1. **Contractidentificatie** 💬
>
>    Bestaat er een contract met afdwingbare rechten? Ja — getekende overeenkomst. Stap 1 voldaan.
>

**Grondslag**: IFRS 15 alinea 9-13

### 2. Identificeer de prestatieverplichtingen

Een **prestatieverplichting** (performance obligation, PO) is een belofte om aan de klant een **onderscheiden** goed/dienst (of bundel/reeks daarvan) over te dragen (alinea 22). Goed/dienst is onderscheiden als (a) de klant ervan kan profiteren op zichzelf of in combinatie met gemakkelijk beschikbare middelen, EN (b) de belofte is afzonderlijk identificeerbaar van andere beloften in het contract (alinea 27).

**Waarom?** Een contract bevat soms meerdere afzonderlijke prestaties (verkoop machine + installatie + onderhoud). Elke prestatie kan op een ander moment vervuld zijn → opbrengstopname op verschillende tijdstippen. Eén grote bundel als één PO behandelen zou de timing vervalsen.

**📥 Input**:
- Contract Zelena-Brugse → **Lijst van beloofde goederen/diensten** _(contractdocument)_

**📤 Output**:
- PO-inventaris → **Lijst van onderscheiden prestatieverplichtingen** _(registerlijst)_

**🛠️ Hoe**:

1. Bekijk wat Zelena Bio aan Brugse Brouwerij belooft: 500.000 doseflesjes ingrediënt X (productverkoop) — één PO.
2. Geen aparte installatie of onderhoud beloofd → één onderscheiden PO.
3. Was het contract complexer (bv. productverkoop + 12 maanden helpdesk + 3 trainingssessies), dan zou de stagiair drie PO's identificeren — mits elk onderscheiden is in de zin van alinea 27.

> [!example]- Voorbeeld: Het contract bevat twee prestatieverplichtingen: levering van bier (200 hl/maand, 24 maanden) en jaarlijkse kwaliteitsco…
> Het contract bevat twee prestatieverplichtingen: levering van bier (200 hl/maand, 24 maanden) en jaarlijkse kwaliteitscontroles ter plaatse.
>
> 1. **Identificatie prestatieverplichtingen** 💬
>
>    Twee afzonderlijke leveringen: (a) bier per maand = 24 leveringen + (b) twee kwaliteits-bezoeken. Elk een aparte prestatieverplichting omdat ze afzonderlijk identificeerbaar zijn.
>

**Grondslag**: IFRS 15 alinea 22-30

### 3. Bepaal de transactieprijs

De transactieprijs is de vergoeding waarop de entiteit verwacht recht te hebben in ruil voor de overdracht — exclusief namens derden geïnde bedragen (bv. btw). Mee in rekening houden: vaste bedragen, variabele bedragen (kortingen, prestatiebonussen — schatten via verwachte waarde of meest waarschijnlijk bedrag, alinea 53), beperking van schattingen variabele vergoeding (alinea 56-58), significante financieringscomponent (alinea 60-65), niet-geldelijke vergoeding (66-69), aan klant te betalen vergoeding (70-72).

**Waarom?** De transactieprijs is wat ECHT zal worden ontvangen — niet wat er op het contract staat als 'kale prijs'. Variabele componenten (kortingen, bonus) maken de werkelijke verwachting anders dan de lijstprijs.

**📥 Input**:
- Contract Zelena-Brugse → **Prijsbedingen + kortingsregels** _(contractdocument)_

**📤 Output**:
- Transactieprijs → **Verwachte vergoeding** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Zelena's prijs: € 0,80/flesje × 500.000 = € 400.000 vaste prijs.
2. Variabele component: Brugse krijgt 2% korting bij betaling binnen 30 dagen. Verwachte waarschijnlijkheid betaling binnen 30 dagen = 70% → verwachte korting = 70% × 2% × € 400.000 = € 5.600.
3. Transactieprijs = € 400.000 − € 5.600 = € 394.400.
4. Geen significante financieringscomponent (betaaltermijn ≤ 1 jaar — alinea 63 praktische oplossing).

**Grondslag**: IFRS 15 alinea 47-58

### 4. Wijs de transactieprijs toe aan de prestatieverplichtingen

Bij meerdere PO's: verdeel de transactieprijs **proportioneel** op basis van de **opzichzelfstaande verkoopprijs** (standalone selling price) van elke PO bij contractaanvang. Als die niet observeerbaar is: schatten via marktbenadering (aangepaste prijzen vergelijkbare entiteiten), kostprijsplus-marge of restwaarde-benadering (alinea 79).

**Waarom?** Bij een bundel-aanbod (machine + installatie + onderhoud aan gebundelde prijs) moet de totale prijs eerlijk verdeeld worden over de drie PO's, anders krijgt één PO te veel en een andere te weinig opbrengst.

**📥 Input**:
- PO-inventaris → **Lijst PO's** _(registerlijst)_
- Prijslijst Zelena Bio → **Opzichzelfstaande prijs per PO** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Toewijzingstabel → **Transactieprijs per PO** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Zelena-Brugse heeft maar één PO (productverkoop ingrediënt X) → volledige € 394.400 aan die PO toegewezen. Geen splitsing nodig.
2. Was er ook € 30.000 helpdesk (opzichzelfstaande prijs) en € 10.000 training (opzichzelfstaande prijs), bij gebundelde totaalprijs € 400.000: verdelen op basis van prijsverhouding 400 : 30 : 10 → product € 363.636, helpdesk € 27.273, training € 9.091.

> [!example]- Voorbeeld: Transactieprijs € 240.000 verdeeld over twee prestatieverplichtingen op basis van standalone-verkoopsprijzen: € 220.000…
> Transactieprijs € 240.000 verdeeld over twee prestatieverplichtingen op basis van standalone-verkoopsprijzen: € 220.000 voor leveringen, € 20.000 voor kwaliteitscontroles.
>
> 1. **Allocatie op basis van standalone-prijzen** 🧮
>
>    Bier: € 220.000 / 24 maanden = € 9.167 per maandelijkse levering
>    Kwaliteitscontrole: € 20.000 / 2 bezoeken = € 10.000 per bezoek
>

**Grondslag**: IFRS 15 alinea 73-80

### 5. Neem opbrengst op bij vervulling prestatieverplichting

Opname is **over een periode** (over time) of **op een tijdstip** (point in time). Over periode (alinea 35) bij minstens één van drie criteria: (a) klant ontvangt en consumeert gelijktijdig de voordelen; (b) prestaties creëren of versterken een actief waarover klant zeggenschap heeft naarmate dat actief wordt gecreëerd; (c) prestaties creëren geen actief met alternatieve gebruiksmogelijkheid voor entiteit én entiteit heeft afdwingbaar recht op betaling voor reeds verrichte prestaties. Anders: opname op het **tijdstip** waarop de klant zeggenschap over het goed verkrijgt (alinea 38) — indicatoren: actueel betalingsrecht, juridische eigendom, fysiek bezit, risico's en beloningen overgedragen, aanvaarding door klant.

**Waarom?** Een productverkoop wordt typisch op één tijdstip overgedragen (klant ontvangt het goed → opbrengstopname). Een dienst zoals consultancy of bouwproject loopt over tijd → opbrengstopname proportioneel aan de voortgang (input- of outputmethode, alinea 41).

**📥 Input**:
- PO + transactieprijs → **PO-status** _(registerlijst)_
- Leveringsdocumentatie → **Datum overdracht zeggenschap** _(datum)_

**📤 Output**:
- Boeking opbrengst → **Bedrag + tijdstip** _(boekingsregel)_

**🛠️ Hoe**:

1. Zelena's PO is een productverkoop → opname op tijdstip van overdracht zeggenschap.
2. Leveringsdatum Q3 2026, bv. 15 september 2026. Op die datum: juridische eigendom over, fysiek bezit over, risico's over → alle indicatoren wijzen op overdracht.
3. Boek opbrengst € 394.400 op 15 september 2026; tegelijk vordering € 394.400 op Brugse.
4. Bij betaling op 15 oktober 2026 (binnen 30 dagen, korting realiseerbaar): klant betaalt € 392.000 (€ 400.000 − 2%). Gerealiseerde korting € 8.000 was deels al voorzien (€ 5.600). Verschil € 2.400 → aanpassing variabele vergoeding in W&V.

> [!example]- Voorbeeld: Zelena Bio NV verkoopt 500.000 doseflesjes ingrediënt X aan Brugse Brouwerij BV, contract 1 mei 2026, levering 15 septem…
> Zelena Bio NV verkoopt 500.000 doseflesjes ingrediënt X aan Brugse Brouwerij BV, contract 1 mei 2026, levering 15 september 2026, betaling 15 oktober 2026 (binnen 30 dagen, 2% korting effectief gerealiseerd).
>
> 1. **Boeking opbrengst en vordering bij levering (15 september 2026)** 📝
>
>    Debet 4000 Handelsvorderingen          € 394.400
>    Credit 7000 Opbrengsten productverkoop        € 394.400
>    
>    Debet 6040 Kostprijs voorraad verkocht       € 200.000
>    Credit 3000 Voorraad ingrediënt X            € 200.000
>
> 2. **Ontvangst betaling met korting (15 oktober 2026)** 📝
>
>    Debet 5500 Bank                              € 392.000
>    Debet 7300 Aanpassing variabele vergoeding    € 2.400
>    Credit 4000 Handelsvorderingen               € 394.400
>

**Grondslag**: IFRS 15 alinea 31-45


## Valkuilen

> [!warning]- Btw en andere namens-derden geïnde bedragen zijn GEEN onderdeel van de transactieprijs (alinea 47)
> ⚠️ Btw en andere namens-derden geïnde bedragen zijn GEEN onderdeel van de transactieprijs (alinea 47). Opbrengst wordt netto-vergoeding gerapporteerd. ⚖️
>
> _Bron: IFRS 15 alinea 47_


> [!warning]- Variabele vergoeding (kortingen, bonus, terugbetalingen) wordt in de transactieprijs opgenomen alleen tot het bedrag waar het 'zeer waarschi…
> ⚠️ Variabele vergoeding (kortingen, bonus, terugbetalingen) wordt in de transactieprijs opgenomen alleen tot het bedrag waar het 'zeer waarschijnlijk' is dat geen significante terugneming zal plaatsvinden (alinea 56). Te optimistische schatting → onnodige opbrengstcorrecties later. ⚖️
>
> _Bron: IFRS 15 alinea 56-58_


> [!warning]- Voorschotbetalingen vóór levering creëren GEEN opbrengst maar een **contractverplichting** (deferred revenue)
> ⚠️ Voorschotbetalingen vóór levering creëren GEEN opbrengst maar een **contractverplichting** (deferred revenue). Pas bij vervulling van de prestatieverplichting wordt de contractverplichting omgezet in opbrengst. ⚖️
>
> _Bron: IFRS 15 alinea 105-107_


> [!warning]- Het 'aanvaarden van de klant' is slechts één indicator voor zeggenschapsoverdracht — niet doorslaggevend
> ⚠️ Het 'aanvaarden van de klant' is slechts één indicator voor zeggenschapsoverdracht — niet doorslaggevend. Een entiteit mag opbrengst opnemen bij overdracht van fysiek bezit en risico's, ook al heeft de klant nog niet formeel 'aanvaard'. ⚖️
>
> _Bron: IFRS 15 alinea 38_



## Zie ook

- **Vereist kennis van**: [[prestatieverplichting]]

## Voorbeelden

### Verkoop met uitgesteld betalingsplan en disconto (IFRS 15 financieringscomponent + BE-GAAP-rekeningen)

_Personages: Zelena Bio NV, Brugse Brouwerij BV_

Op 5 februari 2026 verkoopt Zelena Bio NV een productielijn aan Brugse Brouwerij BV. Nominale verkoopprijs € 5.000.000. Brugse betaalt in 5 jaarlijkse stortingen van € 1.000.000. Wegens de toegestane betalingstermijn werd de verkoopprijs verhoogd met een contract-interest van 4 % per jaar → totaal € 600.000 bijkomende interest, te ontvangen € 5.600.000. De op de kredietmarkt geldende discontovoet voor vergelijkbaar krediet aan Brugse bedraagt 9 % → disconto € 404.706. Onder IFRS 15 alinea 60-65 is dit een significante financieringscomponent (looptijd > 1 jaar, alinea 63 niet van toepassing). De transactieprijs (omzet bij overdracht) wordt de contante verkoopprijs; de renteopbrengsten worden afzonderlijk gepresenteerd (alinea 65) en ontwikkeld over de 5 termijnen via de effectieve-rentemethode.

1. Toets praktische oplossing alinea 63: looptijd 5 jaar > 1 jaar → financieringscomponent moet aangepast worden.
2. Bepaal disconteringspercentage (alinea 64): marktrente voor afzonderlijke financieringstransactie met deze klant = 9 %.
3. Bereken contante verkoopprijs: nominaal € 5.600.000 verdisconteerd aan 9 % over 5 jaarlijkse termijnen = € 4.595.294 (= omzet bij overdracht zeggenschap).
4. Financieringscomponent = € 5.600.000 − € 4.595.294 = € 1.004.706, op te splitsen over de 5 jaren via effectieve-rente.
5. Boek bij levering (5 februari 2026) opbrengst € 4.595.294 op rekening 70 — Omzet, met vordering nominaal € 5.600.000 en tegenboeking 'over te dragen rente' € 1.004.706 (passief).
6. Ontwikkel jaarlijks de rente: het contract-interest-deel (€ 600.000 totaal) loopt op rekening 751 — Opbrengsten uit vlottende activa / renteopbrengsten; het disconto-deel (€ 404.706 totaal) wordt onder BE-GAAP-rekeningenstelsel geboekt op 651 — Disconto op vorderingen / financiële kosten over de 5 terugbetalingstermijnen. Onder IFRS 15: één renteopbrengstlijn, los van omzet (alinea 65).
#### Boeking bij overdracht zeggenschap — 5 februari 2026 (BE-GAAP-rekeningen, IFRS 15-bedragen)
_Vordering wordt geboekt aan nominale waarde (€ 5.600.000); omzet onder IFRS 15 = contante verkoopprijs (€ 4.595.294); het verschil zit als nog-te-ontwikkelen-rente in een passiefrekening die over de looptijd in resultaat wordt genomen._

| Rekening | Debet | Credit |
|---|---:|---:|
| 4000 Handelsvorderingen — nominaal | 5600000 |  |
| 70 Omzet (contante verkoopprijs = transactieprijs IFRS 15) |  | 4595294 |
| 4960 Over te dragen renteopbrengsten / disconto (nog-te-ontwikkelen rente) |  | 1004706 |

#### Jaarlijkse ontwikkeling van rente bij ontvangst termijn (BE-GAAP-uitsplitsing 751 / 651)
_Onder het Belgisch rekeningenstelsel wordt de € 1.004.706 financieringscomponent uitgesplitst in (a) contract-interest 4 % → rekening 751 (€ 600.000 cumulatief), en (b) disconto-effect t.o.v. marktrente 9 % → rekening 651 (€ 404.706 cumulatief), telkens pro rata over de 5 terugbetalingstermijnen. Bij elke jaarlijkse aflossing wordt het pro-rata-deel vrijgemaakt uit de overlopende rekening. Onder IFRS 15 (alinea 65) zou de uitsplitsing tot één renteopbrengst-lijn worden gereduceerd, los van omzet._

| Rekening | Debet | Credit |
|---|---:|---:|
| 5500 Bank (ontvangst jaarlijkse termijn) | 1120000 |  |
| 4000 Handelsvorderingen |  | 1120000 |
| 4960 Over te dragen renteopbrengsten / disconto | 200941 |  |
| 751 Opbrengsten uit vlottende activa (contract-interest 4 %, pro rata) |  | 120000 |
| 651 (tegenboeking — disconto-effect 9 % vs. 4 %, pro rata; in IFRS 15 onderdeel rente) |  | 80941 |

_Bron: IFRS 15 alinea 60-65_ ⚖️


## Bronnen

[^1]: `IFRS-15-opbrengsten-van-contracten-met-klanten__sec_waardering`
[^2]: `IFRS-15-opbrengsten-van-contracten-met-klanten__sec_presentatie`
[^3]: `IFRS-15-opbrengsten-van-contracten-met-klanten__sec_opname`
[^4]: `IFRS-15-opbrengsten-van-contracten-met-klanten__sec_doel`
