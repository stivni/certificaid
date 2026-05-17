---
title: Boeken van uitgifte en aflossing van een obligatielening
tags:
- competentie
- po-1-1
programmaonderdelen:
- '1.1'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/boeken-uitgifte-en-aflossing-obligatielening.yaml
gegenereerd_op: '2026-05-17'
---
# Boeken van uitgifte en aflossing van een obligatielening

**⚖️ 70% · 🤖 30%**

> De boekhoudkundige verwerking (rubriek 170 obligatieleningen op meer dan 1 jaar, 420 obligatieleningen op ten hoogste 1 jaar) en de interestmatching volgen uit KB-WVV art. 3:42 en CBN 2019/07. De keuze tussen rente-spreiding methoden en boekhoudkundige verwerking van uitgiftedisagio is praktijkspecifiek.

## Aanbevolen werkwijze

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

> [!example]- Uitgeverij Ukkel NV emitteert 01/01/2026 obligatielening nominaal € 1.000.000, uitgifteprijs € 980.000, looptijd 5 jaar,…
> **Conclusie**: Aanvangsboeking — D 5500 € 980.000; D 4900 € 20.000; C 170 € 1.000.000. Jaarlijks 31/12 — coupon bruto € 45.000, RV € 13.500, netto € 31.500 via bank. Plus disagio-spreiding € 4.000/jaar via 6500 / 4900. Eind 2030: reclasseren 170 → 420, dan aflossing tegen pari.
>
> **Grondslag**: [[obligatielening]] §uitgifte; [[obligatielening]] §coupon
>
> **Redenering**: Uitgifte onder pari → disagio gespreid over looptijd. Werkelijke financieringskost = coupon + disagio-spreiding = € 45.000 + € 4.000 = € 49.000 (4,9% effectief op nominaal).

> [!example]- Aurelia Holding NV emitteert op 01/07/2026 obligatielening € 500.000 tegen pari, coupon 5% jaarlijks op 30/06
> **Conclusie**: 6 maanden interest opgelopen: € 500.000 × 5% × 6/12 = € 12.500. Boek op 31/12/2026: D 6500 Interest € 12.500; C 492 Toe te rekenen kosten — interest obligatie € 12.500. Bij coupon 30/06/2027: D 492 € 12.500 + D 6500 € 12.500 (resterende 6 mnd 2027); C 4531 RV € 7.500; C 5500 € 17.500 netto.
>
> **Grondslag**: [[obligatielening]] §pro-rata-interest; [[overlopende-rekeningen]] §toe-te-rekenen
>
> **Redenering**: Coupon-datum valt buiten balansdatum → pro-rata-verdeling. Werkelijke kost in 2026 = 6/12 van jaarlijkse coupon.

> [!example]- Uitgeverij Ukkel NV koopt op 30/06/2028 (halfweg looptijd) een deel € 200.000 nominaal van eigen obligaties terug op de…
> **Conclusie**: Vermindering schuld 170 met € 200.000 nominaal; bank uitgaande € 195.000; verschil € 5.000 meerwaarde op 763 Andere niet-recurrente financiële opbrengsten. Disagio-saldo 4900 toerekenen pro-rata aan teruggekocht deel.
>
> **Grondslag**: [[obligatielening]] §inkoop-eigen-obligaties; CBN 2019/07
>
> **Redenering**: Inkoop onder pari realiseert meerwaarde (gerealiseerde winst). Niet vergeten dat het pro-rata disagio van het teruggekochte deel ook in resultaat moet (kost via 6500).


## Gebaseerd op concepten

[[obligatielening]] · [[schulden]] · [[overlopende-rekeningen]] · [[financiele-verrichtingen]]
## Voortkomend uit

- **Taken**: 1.1.taak.1
- **Kenniselementen**: 1.1.II.V, 1.1.II.J
