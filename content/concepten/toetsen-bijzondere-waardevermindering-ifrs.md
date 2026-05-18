---
title: Toetsen van een actief op bijzondere waardevermindering onder IFRS (IAS 36)
tags:
- concept
- competentie
- po-1-5
linked_anchors:
- 1.5.taak.1
- 1.5.V.A
- 1.5.V.B
- 1.5.IV.C
programmaonderdelen:
- '1.5'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/toetsen-bijzondere-waardevermindering-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Toetsen van een actief op bijzondere waardevermindering onder IFRS (IAS 36) 🤖


## Stappen

### 1. Scan op aanwijzingen voor mogelijke waardevermindering

Toets op balansdatum (of vaker bij triggers) op externe en interne aanwijzingen — bv. waardedaling marktsector, technologische veroudering, fysieke schade, slechtere bedrijfsresultaten, of indicaties dat netto-realiseerbare waarde gedaald is.

**Waarom?** De volledige impairment-test (stap 2-4) is duur en wordt alleen uitgevoerd als er aanwijzingen zijn. Goodwill en immateriële vaste activa met onbeperkte gebruiksduur worden echter **jaarlijks** getest, ongeacht aanwijzingen (alinea 10).

**📥 Input**:
- Externe rapporten (sector, markt) → **Indicatoren marktdaling, technologische evolutie** _(document)_
- Interne managementrapporten → **Resultaten, schadegevallen, herstructureringsplannen** _(document)_

**📤 Output**:
- Werkpapier impairment-scan → **Lijst aanwijzingen + activa-categorieën te testen** _(conclusie)_

**🛠️ Hoe**:

1. Volg [[bijzondere-waardevermindering-ifrs]] §stap-1 voor de standaardlijst van aanwijzingen (alinea 12).
2. Doorloop voor Zelena Bio NV: marktrentes gestegen (externe aanwijzing — verhoogde disconteringsvoet kan bedrijfswaarde drukken); operationele marges productielijn 'PL-3' gedaald van 18 % naar 6 % (interne aanwijzing — slechtere prestaties); een patent verloopt over 2 jaar (interne aanwijzing — kortere kasstroomhorizon).
3. Conclusie: lijst activa/CGU's voor volledige test = productielijn PL-3 (€ 12.000.000 boekwaarde) + goodwill segment 'Bio-feed' (€ 8.500.000, jaarlijkse test sowieso verplicht).
4. Documenteer aanwijzingen + scope in werkpapier.


**Grondslag**: [[bijzondere-waardevermindering-ifrs]] §stap-1, IAS 36 alinea 9-17

### 2. Identificeer het kasstroomgenererende niveau (individueel actief of CGU)

Bepaal of het actief zelfstandig kasstromen genereert (dan: individueel testen) of niet (dan: kasstroomgenererende eenheid (CGU) bepalen — kleinste groep activa die onafhankelijke kasstromen genereert).

**Waarom?** Veel productieactiva (machines, gebouwen) genereren geen onafhankelijke kasstroom — alleen samen met andere activa. CGU-niveau voorkomt overschatting van realiseerbare waarde door artificiële segmentering.

**📥 Input**:
- Operationele structuur van de onderneming → **Welke activa werken samen voor een output-kasstroom?** _(document)_

**📤 Output**:
- Werkpapier → **Per te testen actief: CGU-afbakening** _(conclusie)_

**🛠️ Hoe**:

1. Volg [[bijzondere-waardevermindering-ifrs]] §cgu-afbakening voor de criteria.
2. Voor productielijn PL-3 van Zelena Bio: lijn produceert biologisch veevoer dat afzonderlijk wordt verkocht aan klanten → onafhankelijke kasstroom mogelijk → CGU = de productielijn zelf met haar machines + voorraad + werkkapitaal (boekwaarde € 12.000.000).
3. Voor goodwill 'Bio-feed' segment: goodwill genereert zelf geen kasstromen → toets op het **laagste niveau** waar de goodwill wordt opgevolgd (alinea 80) — typisch business segment. CGU = volledig segment Bio-feed (€ 45.000.000 boekwaarde inclusief goodwill).
4. Documenteer CGU-grenzen, consistentie met vorige periodes (alinea 72), en de allocatie van goodwill aan CGU's.


**Grondslag**: [[bijzondere-waardevermindering-ifrs]] §cgu-afbakening, IAS 36 alinea 65-87

### 3. Bereken de realiseerbare waarde (hoogste van reële waarde min verkoopkosten en bedrijfswaarde)

**Realiseerbare waarde** = max(reële waarde min verkoopkosten, bedrijfswaarde). Reële waarde min verkoopkosten: marktprijs of taxatie min directe verkoopkosten. Bedrijfswaarde: contante waarde van toekomstige kasstromen × passende disconteringsvoet (WACC of asset-specifiek).

**Waarom?** Een actief is alleen waarde-aangetast als noch verkoop (reële waarde) noch verder gebruik (bedrijfswaarde) een waarde bovenop de boekwaarde oplevert. Eén van beide volstaat om impairment te vermijden.

**📥 Input**:
- Marktdata of taxatierapport → **Reële waarde + verkoopkosten** _(boekhoudkundig-bedrag)_
- Toekomstige-kasstroomprognose CGU → **Per jaar over typisch 5 jaar + terminal value** _(boekhoudkundig-bedrag)_
- Disconteringsvoet (WACC) → **Vóór belasting, asset-specifiek risico** _(percentage)_

**📤 Output**:
- Werkpapier → **Realiseerbare waarde per CGU** _(berekening)_

**🛠️ Hoe**:

1. Volg [[bijzondere-waardevermindering-ifrs]] §realiseerbare-waarde voor de definitie.
2. **Reële waarde min verkoopkosten** productielijn PL-3: taxatie tweedehandsmarkt machines € 7.500.000 − afbraakkosten € 200.000 = **€ 7.300.000**.
3. **Bedrijfswaarde** PL-3: prognose 5 jaar netto-kasstroom (€ 2.000.000; € 1.800.000; € 1.500.000; € 1.200.000; € 900.000) + terminal value (kasstroom jaar 5 × 2) = € 1.800.000. Disconteringsvoet 9 % (WACC vóór belasting, asset-specifiek aangepast). Contante waarde = bv. € 1.835.000 + € 1.515.000 + € 1.158.000 + € 850.000 + € 585.000 + terminal contante € 1.170.000 = **€ 7.113.000**.
4. Realiseerbare waarde = max(€ 7.300.000; € 7.113.000) = **€ 7.300.000**.
5. Aandachtspunt: kasstromen mogen GEEN financieringscashflows of belastingen bevatten (alinea 50-51).


> [!example]- Voorbeeld: Berekening realiseerbare waarde productielijn PL-3 Zelena Bio NV op 31 december 2027
> Berekening realiseerbare waarde productielijn PL-3 Zelena Bio NV op 31 december 2027.
>
> 1. **Reële waarde min verkoopkosten** 🧮
>
>    reële waarde markttaxatie  = € 7.500.000
>    ─ verkoopkosten (afbraak)  = € 200.000
>    = **€ 7.300.000**
>    
>
> 2. **Bedrijfswaarde (contante kasstromen)** 🧮
>
>    | Jaar | Kasstroom (€) | Factor 9 % | Contante (€) |
>    |------|--------------:|-----------:|-------------:|
>    | 1    |     2.000.000 |    0,9174  |    1.834.800 |
>    | 2    |     1.800.000 |    0,8417  |    1.515.060 |
>    | 3    |     1.500.000 |    0,7722  |    1.158.300 |
>    | 4    |     1.200.000 |    0,7084  |      850.080 |
>    | 5    |       900.000 |    0,6499  |      584.910 |
>    | TV   |     1.800.000 |    0,6499  |    1.169.820 |
>    | **Totaal**                            | **7.112.970** |
>    
>
> 3. **Realiseerbare waarde** 🧮
>
>    realiseerbare waarde = max(reële − verkoopkosten ; bedrijfswaarde)
>                         = max(€ 7.300.000 ; € 7.113.000)
>                         = **€ 7.300.000**
>    
>

**Grondslag**: [[bijzondere-waardevermindering-ifrs]] §realiseerbare-waarde, IAS 36 alinea 18-57

### 4. Vergelijk met boekwaarde en boek de bijzondere waardevermindering

Indien realiseerbare waarde < boekwaarde → boek het verschil als bijzondere waardevermindering. Volgorde voor CGU: eerst goodwill, dan pro rata over andere activa van de CGU (alinea 104).

**Waarom?** De boekwaarde mag nooit hoger zijn dan de waarde die de onderneming nog uit het actief kan halen — door verkoop of door verder gebruik. De impairment-boeking herstelt deze regel.

**📥 Input**:
- Boekwaarde CGU/actief vóór impairment → **Bedrag** _(boekhoudkundig-bedrag)_
- Realiseerbare waarde uit stap 3 → **Bedrag** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Boekingen W&V + balans → **Bijzondere waardevermindering** _(boekingsregel)_

**🛠️ Hoe**:

1. Volg [[bijzondere-waardevermindering-ifrs]] §boeking-impairment voor de boekingsregel.
2. Voor productielijn PL-3 Zelena Bio: boekwaarde € 12.000.000 versus realiseerbare waarde € 7.300.000 → **impairment € 4.700.000**.
3. Allocatie: PL-3 bevat geen goodwill, dus heel het bedrag verlaagt activa pro rata over de componenten van de CGU. Bv. machines −€ 3.200.000; gebouw −€ 1.000.000; werkkapitaal niet onder grens (alinea 105 — actief mag niet onder hogere van reële waarde, bedrijfswaarde, nul gedrukt worden).
4. Boek: debet 'Bijzondere waardeverminderingen' € 4.700.000 (W&V); credit 'Cumulatieve waardevermindering productielijn PL-3' € 4.700.000.
5. Bij CGU met goodwill (Bio-feed segment): vergelijk goodwill € 8.500.000 + andere activa. Stel realiseerbare waarde € 38.000.000 versus boekwaarde € 45.000.000 = impairment € 7.000.000. Eerst goodwill afboeken: − € 7.000.000 → goodwill van € 8.500.000 daalt naar € 1.500.000. Andere activa onaangetast.
6. Belangrijke regel: **goodwill-impairment kan nooit worden teruggenomen** (alinea 124). Voor andere activa: terugname mogelijk indien aanwijzingen wijzigen.


> [!example]- Voorbeeld: Bijzondere waardevermindering productielijn PL-3 op 31 december 2027
> Bijzondere waardevermindering productielijn PL-3 op 31 december 2027.
>
> 1. **Berekening impairment** 🧮
>
>    boekwaarde CGU PL-3            = € 12.000.000
>    realiseerbare waarde (uit stap 3) = € 7.300.000
>    **impairment**                  = **€ 4.700.000**
>    
>
> 2. **Boeking** 📝
>
>    Debiteer:  Bijzondere waardeverminderingen (W&V) € 4.700.000
>    Crediteer: Cumulatieve waardevermindering PL-3   € 4.700.000
>    
>    (Allocatie pro rata over componenten: machines € 3.200.000, gebouw € 1.000.000, overige € 500.000.)
>    
>
> 3. **Herzien afschrijvingsplan** 💬
>
>    Nieuwe boekwaarde PL-3 = € 7.300.000.
>    Resterende gebruiksduur = 5 jaar (oud plan).
>    Nieuwe lineaire afschrijving = € 7.300.000 / 5 = **€ 1.460.000/jaar** (versus eerder € 2.400.000/jaar).
>    Herziening en gebruik nieuwe afschrijvingsbedrag vanaf boekjaar 2028.
>    
>

**Grondslag**: [[bijzondere-waardevermindering-ifrs]] §boeking-impairment, IAS 36 alinea 58-99 + 104 + 124

> [!warning]- Bij CGU met goodwill: eerst alle goodwill afboeken vóór andere activa te raken — en goodwill-impairment is nooit terug te nemen.
>
> _Vaak fout gedaan_: Goodwill-impairment in latere jaren terugnemen omdat de markt opnieuw aantrekt. IAS 36 alinea 124 verbiedt dit categorisch.
>
> _Grondslag_: [[bijzondere-waardevermindering-ifrs]] §terugname


