---
title: "Uitgestelde belastingen"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
  - regeling
ankers:
  - 1.1.II.I
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/uitgestelde-belastingen.json"
---

_Balanspost_ · ook: deferred taxes · fiscale latenties · klasse 168

## Definitie

**Uitgestelde belastingen** (Engels: *deferred tax*) zijn een passiefpost (**MAR-rekening 168**) of activapost (zeldzaam onder B-GAAP) die de **fiscale impact** weerspiegelt van een **tijdelijk verschil** tussen het **boekhoudkundig resultaat** en het **fiscaal belastbaar resultaat**. Een tijdelijk verschil ontstaat wanneer een opbrengst of kost in boekjaar X wordt erkend voor boekhoudkundige doeleinden maar pas in boekjaar Y (eerder of later) belastbaar of aftrekbaar wordt — bv. een meerwaarde die boekhoudkundig vrijgesteld is met latere taxatie, of een versnelde fiscale afschrijving versus lineaire boekhoudkundige afschrijving. Het Belgische B-GAAP-systeem kent een **beperkte erkenning** van uitgestelde belastingen, in tegenstelling tot IFRS (IAS 12) dat een **volledige erkenning** vereist.

<small>📖 KB 21-10-2018 — Bijlage 1 MAR — Klasse 16 — rekening 168 — _kb_ · KB 29-04-2019 WVV — art. 3:30 — _kb_</small>

## Substantie

**B-GAAP**: uitgestelde belastingen worden in België **alleen** geboekt voor **specifieke gevallen** die de wetgever heeft aangeduid — typisch:
- Vrijgestelde meerwaarden op materiële vaste activa onder de **gespreide taxatie**-regeling (art. 47 WIB92);
- Vrijgestelde meerwaarden op aandelen onder voorwaarde-regeling;
- Kapitaalsubsidies (KB-AR 1976 — taxatie gespreid pro-rata afschrijving).

Geen algemene boeking van **tijdelijke verschillen** zoals onder IFRS — het Belgische systeem is **historisch-kost-conservatief** en vertrouwt op het matching tussen boekhoudkundig en fiscaal resultaat.

**IFRS (IAS 12)**: alle tijdelijke verschillen tussen boekwaarde en fiscale waarde van activa/passiva geven aanleiding tot uitgestelde belasting-actief of -passief, te waarderen aan het **verwachte toekomstige tarief**.

**Boekingsschema B-GAAP** voor een vrijgestelde meerwaarde van 100.000 EUR (gespreide taxatie 5 jaar):
```
Boekjaar X — bij realisatie meerwaarde:
7100 Meerwaarde op realisatie    C 100.000 (in resultaat)
168 Uitgestelde belastingen      C 25.000 (latente VenB 25%)

Boekjaar X+1 t/m X+4 — proportionele taxatie 5.000 EUR latentie per jaar:
168 Uitgestelde belastingen      D 5.000
   77 Onttrekking belasting       C 5.000 (of rechtstreeks tegen 6700)
```

<small>📖 KB 29-04-2019 WVV — art. 3:30 — _kb_ · WIB92 — art. 47 — _wettekst_ · IAS 12 — IAS 12 par. 5 — _richtlijn_</small>

## Rationale

Uitgestelde belastingen bestaan om het **matching-principe** ook bij fiscaliteit te respecteren: een opbrengst die boekhoudkundig in jaar X is erkend maar pas in jaar X+3 fiscaal belastbaar wordt, moet de **toekomstige belastinglast** al in jaar X laten doorklinken — anders is het boekhoudkundig nettoresultaat in X overgewaardeerd en in X+3 onderschat. Het B-GAAP heeft dit principe **selectief** geïmplementeerd voor situaties waar het verschil structureel en omvangrijk is (vrijgestelde meerwaarden, kapitaalsubsidies). IFRS heeft het **veralgemeend** — wat de jaarrekeningen IFRS-conform vergelijkbaar maakt over jurisdicties met verschillende belastingstelsels.

<small>🔗 IAS 12 — IAS 12 — basis for conclusions — _richtlijn_</small>

## Bouwstenen

### ⚙️ Voorbeeld gespreide taxatie meerwaarde (WIB art. 47)

**Scenario**: Verkoop van een bedrijfsmachine boekt een meerwaarde van **100.000 EUR**. De vennootschap herinvesteert binnen 3 jaar in nieuwe MVA met 5-jarige afschrijving en kiest voor **gespreide taxatie** (art. 47 WIB92): de meerwaarde wordt belast pro rata van de afschrijving van het nieuwe actief (20 % per jaar).

**Boekhoudkundig in jaar 0**:
- Meerwaarde 100.000 EUR in resultatenrekening (763 of 70x).
- Fiscaal NIET onmiddellijk belast — uitgestelde belastinglast.
- VenB-tarief 25 % → uitgestelde belasting 25.000 EUR.

**Boekingen jaar 0**:
```
6701 Verschuldigde belastingen op resultaat (totaal): vermindert met 25.000 uitstel
168 Uitgestelde belastingen        C 25.000
   (tegenpost in 7700 Onttrekking aan uitgestelde belastingen)
```

**Jaar 1 t/m 5 — proportionele afbouw**:
```
168                                D 5.000
   7700                            C 5.000
```
Het fiscaal belastbaar resultaat van die jaren wordt verhoogd met 20 % × 100.000 = 20.000 EUR; de bijhorende VenB van 5.000 EUR verhoogt klasse 67, gecompenseerd door de onttrekking uit klasse 168.

<small>📖 WIB92 — art. 47 — _wettekst_ · KB 29-04-2019 WVV — art. 3:30 — _kb_</small>

## Valkuilen

> [!warning]- B-GAAP verwarren met IFRS-systeem
> **Verkeerde assumptie**: Voor elk timing-verschil tussen boekhouding en fiscaliteit moet een uitgestelde belasting worden geboekt.
>
> **Kernpunt**: Onder **B-GAAP** is dit **niet** zo. Alleen de wettelijk aangeduide gevallen (gespreide taxatie, kapitaalsubsidies, vrijstellingsregimes met voorwaarden) leiden tot klasse 168. Voor alle andere timing-verschillen (versnelde fiscale afschrijving op een investeringsaftrek bv.) wordt **geen** uitgestelde belasting geboekt — het verschil wordt impliciet door de fiscale herzieningsberekening opgevangen. Onder **IFRS (IAS 12)** is volledige erkenning vereist.
>
> <small>📖 KB 29-04-2019 WVV — art. 3:30 — _kb_ · IAS 12 — IAS 12 — _richtlijn_</small>

> [!warning]- Klasse 168 met voorziening verwarren
> **Verkeerde assumptie**: Klasse 16 = voorzieningen — dus klasse 168 is een voorziening voor toekomstige belastingen.
>
> **Kernpunt**: Klasse 168 is **conceptueel anders** dan de voorzieningen (160-163). Een voorziening dekt een **risico of verplichting** met onzeker bedrag of termijn. Klasse 168 dekt een **vastgestelde latente belastingverplichting** voortvloeiend uit een specifieke gespreide-taxatie- of vrijstellings-regeling — bedrag is bekend, alleen de uitbetaling/aftrek is gespreid in de tijd.
>
> <small>📖 KB 21-10-2018 — MAR — Klasse 16 (160-163 vs 168) — _kb_</small>

## Verder lezen (scope-out)

- → Voorzieningen (zelfde klasse 16 ander fenomeen) → [[voorzieningen]] _(moet-verwijzen)_
- ↪ IFRS-IAS 12 perspectief → [[ifrs]] _(mag-verwijzen)_
- ↪ Vennootschapsbelasting-context → [[vennootschapsbelasting]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[boekhouding]]
### `vergelijkbaar_met`
- [[voorzieningen]]
    - **Gelijkenissen**:
        - Beide MAR-klasse 16
        - Beide passief-rubrieken voor toekomstige uitstromen
    - **Verschillen**:
        - Voorziening: onzeker bedrag/termijn, risico-driven
        - Uitgestelde belasting: bekend bedrag, timing-verschil-driven, alleen specifieke wettelijke gevallen onder B-GAAP
    - ⚠️ **Verwarringsrisico**: Studenten boeken een algemene 'fiscale voorziening' in klasse 168 of een gespreide-taxatie-latentie in klasse 161 (belasting-voorziening).
