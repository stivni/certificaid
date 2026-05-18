---
title: Opbrengsten onder IFRS (IFRS 15) — 5-stappen-model
tags:
- concept
- methode
- po-1-5
linked_anchors:
- 1.5.V.D
- 1.5.V
programmaonderdelen:
- '1.5'
confidence: grounded
node_type: methode
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/opbrengsten-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Opbrengsten onder IFRS (IFRS 15) — 5-stappen-model ⚖️

> [!summary] Korte inhoud
> IFRS 15 — Opbrengsten van contracten met klanten vervangt sinds 1 januari 2018 IAS 18 (Opbrengsten uit gewone activiteiten) en IAS 11 (Onderhanden projecten in opdracht van derden).

IFRS 15 — Opbrengsten van contracten met klanten vervangt sinds 1 januari 2018 IAS 18 (Opbrengsten uit gewone activiteiten) en IAS 11 (Onderhanden projecten in opdracht van derden). Het **kernprincipe** (alinea 2): een entiteit neemt opbrengsten op om de overdracht van beloofde goederen of diensten aan klanten weer te geven, voor een bedrag dat de vergoeding weerspiegelt waarop de entiteit recht zal hebben in ruil. De toepassing volgt een **5-stappen-model**: (1) identificeer het contract met de klant; (2) identificeer de prestatieverplichtingen in het contract; (3) bepaal de transactieprijs; (4) wijs de transactieprijs toe aan de prestatieverplichtingen; (5) neem opbrengsten op wanneer (of naarmate) een prestatieverplichting wordt vervuld. Het model is **principe-georiënteerd** en geldt voor alle sectoren, met uitzondering van leasing (IFRS 16), verzekeringen (IFRS 17) en financiële instrumenten (IFRS 9).

_Bron: IFRS 15 alinea 2 + 9-46_


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
7. Contract is opnemeer onder IFRS 15.

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

- **Vereist kennis van**: [[prestatieverplichting-ifrs-15]]

## Bronnen

[^1]: `IFRS-15-opbrengsten-van-contracten-met-klanten__sec_doel`
[^2]: `IFRS-15-opbrengsten-van-contracten-met-klanten__sec_opname`
[^3]: `IFRS-15-opbrengsten-van-contracten-met-klanten__sec_waardering`
[^4]: `IFRS-15-opbrengsten-van-contracten-met-klanten__sec_presentatie`
