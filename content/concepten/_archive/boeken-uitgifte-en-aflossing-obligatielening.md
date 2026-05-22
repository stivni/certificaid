---
title: Boeken van uitgifte en aflossing van een obligatielening
tags:
- concept
- competentie
- po-1-1
linked_anchors:
- 1.1.taak.1
- 1.1.II.V
- 1.1.II.J
programmaonderdelen:
- '1.1'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/boeken-uitgifte-en-aflossing-obligatielening.json
gegenereerd_op: '2026-05-21'
---
# Boeken van uitgifte en aflossing van een obligatielening 🔗

Een specialistischer financierings-competentie: meer dan een banklening vergt een obligatielening boekingen op uitgifte (eventueel met disagio of agio), prorata-rente op balansdatum, couponbetalingen, en aflossing. Voor een stagiair-GA: typisch examen-onderwerp omdat het verschillende boekhoudbeginselen tegelijk test (matching via prorata, voorzichtigheid bij disagio, voorstelling op de balans).



## Stappen

### 1. Analyseer het emissieprospectus

Verzamel cruciale kenmerken: nominale waarde, uitgifteprijs, terugbetalingsprijs, looptijd, couponrente, betalingsritme.

**Waarom?** Een correcte boeking vergt onderscheid tussen nominale waarde (schuld in balans), uitgifteprijs (ontvangen bedrag) en eventueel emissiedisagio (verschil).

**📥 Input**:
- Emissieprospectus → **Nominale waarde totaal, uitgifteprijs, coupon-%, looptijd, terugbetaling** _(document)_

**📤 Output**:
- Werknotitie kenmerken → **Tabel parameters** _(conclusie)_

**🛠️ Hoe**:

1. Voor Uitgeverij Ukkel NV — uitgifte 01/01/2026, nominale waarde € 1.000.000, uitgifteprijs € 980.000 (98% pari), terugbetaling tegen pari na 5 jaar, couponrente 4,5% jaarlijks betaalbaar op 31/12.
2. Bereken disagio = nominale waarde - uitgifteprijs = € 1.000.000 - € 980.000 = € 20.000.
3. Couponkost = nominale waarde × % = € 1.000.000 × 4,5% = € 45.000 per jaar.
4. Documenteer in werknotitie.


**Grondslag**: [[obligatielening]] §emissieparameters, CBN 2019/07

### 2. Boek de uitgifte van de obligatielening

Boek de ontvangst van het uitgifteprijs-bedrag op bank, de nominale schuld op passief, en het disagio als over te dragen actief.

**Waarom?** Disagio is geen kost van het emissiejaar maar moet over de looptijd worden gespreid (matching met de financieringsperiode).

**📥 Input**:
- Werknotitie stap 1 → **Bedragen** _(berekening)_

**📤 Output**:
- Aanvangsboeking → **Bank + schuld + disagio** _(boekingsregel)_

**🛠️ Hoe**:

1. Boek nominale schuld op 170 Obligatieleningen op meer dan 1 jaar (deel met looptijd > 1 jaar).
2. Bank-ontvangst op 5500.
3. Disagio op 4900 Over te dragen kosten (uitgiftedisagio) — wordt jaarlijks afgeschreven over de looptijd.
4. Bij eventuele agio (uitgifteprijs > nominaal): op 4930 Over te dragen opbrengsten.
5. Eventuele uitgiftekosten (notaris, drukker, FSMA-vergoeding) zijn aparte: activeerbaar op 200 Oprichtingskosten of op 4900 (CBN 2019/07 §1.3).


> [!example]- Voorbeeld: Uitgeverij Ukkel NV — emissie 01/01/2026: nominaal € 1.000.000, uitgifteprijs € 980.000, looptijd 5 jaar, coupon 4,5% pe…
> Uitgeverij Ukkel NV — emissie 01/01/2026: nominaal € 1.000.000, uitgifteprijs € 980.000, looptijd 5 jaar, coupon 4,5% per jaar.
>
> 1. **Aanvangsboeking** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 01/01/2026 | 5500 Bank — KBC | netto-ontvangst emissie | € 980.000,00 | |
>    | 01/01/2026 | 4900 Over te dragen kosten — uitgiftedisagio | disagio € 20.000 te spreiden 5 jaar | € 20.000,00 | |
>    | 01/01/2026 | 170 Obligatieleningen op meer dan 1 jaar | nominaal | | € 1.000.000,00 |
>    
>

**Grondslag**: [[obligatielening]] §uitgifte-boeking, [[schulden]] §langlopende-schulden

### 3. Spreid het disagio jaarlijks over de looptijd

Boek elk boekjaar een deel van het disagio als financiële kost.

**Waarom?** De economische kost van de obligatielening = coupon + spreiding disagio; samen geven ze de werkelijke rente.

**📥 Input**:
- Disagio-bedrag stap 2 → **Saldo 4900** _(balans)_

**📤 Output**:
- Eindejaars-boeking disagio → **Dotatie kost** _(boekingsregel)_

**🛠️ Hoe**:

1. Methode lineair: jaarlijkse dotatie = totaal disagio / looptijd in jaren.
2. Voor Uitgeverij Ukkel NV: € 20.000 / 5 = € 4.000 per jaar.
3. Boek op 31/12: Debet 6500 Kosten van schulden — disagio-spreiding; Credit 4900 Over te dragen kosten — uitgiftedisagio.
4. Alternatief: effectieve-rentemethode (gemiddeld over looptijd; complex) — CBN 2019/07 staat ook deze methode toe.
5. Saldo 4900 wordt 5 jaar lang afgebouwd tot 0.


**Grondslag**: [[obligatielening]] §disagio-spreiding, [[overlopende-rekeningen]] §langlopende

### 4. Boek jaarlijks de coupon en eventuele toe-te-rekenen interest

Boek elke coupon-betaling als financiële kost; bij niet-samenvallend boekjaar / coupon-datum doe je pro-rata via 492.

**Waarom?** Coupon is reële kost van het boekjaar; matching met tijdverloop verplicht.

**📥 Input**:
- Coupon-betalingsdatum + bedrag → **€ coupon per periode** _(berekening)_

**📤 Output**:
- Coupon-boekingen → **Bij betaling + bij toerekening** _(boekingsregel)_

**🛠️ Hoe**:

1. Bij directe betaling op balansdatum (zoals Uitgeverij Ukkel NV: coupon op 31/12 elk jaar): D 6500 Kosten van schulden — interest € 45.000; C 5500 Bank € 45.000 (na inhouding RV).
2. Inhouding roerende voorheffing op interest 30% (tenzij specifieke vrijstelling): D 6500 € 45.000; C 4530 RV € 13.500; C 5500 € 31.500 (netto aan obligatiehouders).
3. Bij niet-samenvallende boekjaar/coupon-datum: pro-rata via 492 Toe te rekenen kosten — zie competentie [[verwerken-overlopende-rekeningen-matching]].
4. RV-aangifte binnen 15 dagen aan fiscus: D 4530; C 5500.


> [!example]- Voorbeeld: Uitgeverij Ukkel NV — eerste coupon-betaling op 31/12/2026: € 45.000 bruto, RV 30% = € 13.500, netto € 31.500
> Uitgeverij Ukkel NV — eerste coupon-betaling op 31/12/2026: € 45.000 bruto, RV 30% = € 13.500, netto € 31.500.
>
> 1. **Boeking coupon** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 31/12/2026 | 6500 Kosten van schulden — coupon | bruto-coupon | € 45.000,00 | |
>    | 31/12/2026 | 4531 Roerende voorheffing op interest | RV 30% | | € 13.500,00 |
>    | 31/12/2026 | 5500 Bank — KBC | netto aan obligatiehouders | | € 31.500,00 |
>    
>
> 2. **Boeking spreiding disagio einde 2026** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 31/12/2026 | 6500 Kosten van schulden — disagio | 1/5 spreiding | € 4.000,00 | |
>    | 31/12/2026 | 4900 Over te dragen kosten — uitgiftedisagio | -- | | € 4.000,00 |
>    
>

**Grondslag**: [[obligatielening]] §coupon-boeking, [[financiele-verrichtingen]] §interest-roerende-voorheffing

### 5. Boek tussentijdse reclassificatie en uiteindelijke aflossing

Reclasseer naar kortlopende schuld in het laatste jaar; boek aflossing tegen pari op vervaldatum.

**Waarom?** Balans-presentatie moet onderscheid LT/KT respecteren (KB-WVV); aflossing maakt schuld nul.

**📥 Input**:
- Saldo 170 + balansdatum → **Resterende looptijd** _(balans)_

**📤 Output**:
- Reclassificatie + eindaflossing → **Verschuiving 170 → 420 + uiteindelijke aflossing** _(boekingsregel)_

**🛠️ Hoe**:

1. Op balansdatum waarop resterende looptijd ≤ 1 jaar: D 170; C 420 Obligatieleningen op ten hoogste 1 jaar.
2. Voor Uitgeverij Ukkel NV — op 31/12/2030 staat aflossing op 01/01/2031 voor de deur: D 170 € 1.000.000; C 420 € 1.000.000.
3. Op vervaldatum (01/01/2031): D 420 € 1.000.000; C 5500 Bank € 1.000.000 (tegen pari).
4. Laatste coupon boeken samen met aflossing.
5. Saldo 4900 moet op vervaldatum nul zijn (alle disagio reeds gespreid).
6. Bij vervroegde aflossing aan andere prijs: meer- of minderwaarde via 663 of 763.


**Grondslag**: [[obligatielening]] §aflossing, [[schulden]] §reclassificatie-LT-KT


## Voorbeelden





