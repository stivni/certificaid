---
title: "Geldbeleggingen en liquide middelen"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.1.II.G
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/geldbeleggingen-en-liquide-middelen.json"
---

_Balanspost_ · ook: klasse 5

## Definitie

MAR-klasse 5 omvat de twee meest liquide categorieën op het actief: (a) geldbeleggingen (50-53) = kortetermijn-beleggingen aangehouden voor speculatief of liquide-overschot beheer — 50 eigen aandelen · 51 aandelen (genoteerd of niet) · 52 vastrentende effecten · 53 termijndeposito's (sub 530 > 1 jaar, 531/532 ≤ 1 jaar). (b) Liquide middelen (54-58) = onmiddellijk beschikbare middelen — 54 te incasseren waarden · 55 kredietinstellingen (giro + bank rekening-courant) · 56 postchecks · 57 kassen. Sub-rekening 8 = geboekte meerwaarden; 9 = waardeverminderingen (-).

<small>📖 MAR-KB 21.10.2018 — Bijlage 1 klasse 5 — _kb_</small>

## Substantie

Onderscheid klasse 5 ↔ klasse 28 (financiële vaste activa) zit in INTENTIE + DUUR: klasse 5 = speculatief of tijdelijk parkeren van overtollige cash; klasse 28 = duurzaam aanhouden van deelneming. Dezelfde aandelen kunnen in beide rubrieken — afhankelijk van bedoeling. Belangrijke wettelijke regels (KB 29.04.2019 art. 3:52-3:53): geldbeleggingen tegen aanschaffingswaarde, waardevermindering verplicht bij duurzame waardedaling, geen herwaardering toegestaan tenzij actieve markt + voorzichtigheid. Eigen aandelen (50) hebben speciale regels — verbod opnemen onder activa indien gehouden tot vernietiging (WVV art. 7:215).

<small>📖 KB 29.04.2019 — art. 3:52-3:53 — _kb_</small>

## Rationale

De afzonderlijke rubriek 'eigen aandelen' (50) reflecteert het juridisch eigen-vermogens-karakter: bij aanhouden tegen vernietiging is het géén actief maar een EV-correctie. KB 29.04.2019 dwingt tot voorzichtige waardering (geen herwaardering, wel waardevermindering) om winstuitkering op basis van papieren meerwaarde te voorkomen. Voor de stagiair: klasse 5 herken aan onmiddellijke beschikbaarheid + speculatieve/kortetermijn-intentie.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Sub-concepten

### 📦 50 — Eigen aandelen

#### Definitie

Aandelen die de vennootschap zelf bezit (na inkoop). Gedurende aanhouding: rubriek 500 aanschaffingswaarde + 509 waardevermindering. Bij doel = vernietiging: niet als actief maar afzonderlijk EV-correctie. WVV art. 7:215 stelt strikte voorwaarden (maximaal 20% kapitaal, voldoende uitkeerbare winst, beslissing AV).

<small>📖 MAR-KB — klasse 50 — _kb_ · WVV — art. 7:215 — _wettekst_</small>

### 📦 51 — Aandelen

#### Definitie

Aandelen aangehouden als kortetermijn-belegging — niet duurzaam (anders klasse 28). Sub: 510 aanschaffingswaarde + 519 waardevermindering. Genoteerd aandeel: waardevermindering op basis van beurskoers eind boekjaar als lager dan aanschaffingswaarde. Niet-genoteerd: schatting op basis van intrinsieke waarde of meest recente transactie.

<small>📖 KB 29.04.2019 — art. 3:52 — _kb_</small>

### 📦 52 — Vastrentende effecten

#### Definitie

Obligaties + andere vastrentende effecten aangehouden als kortetermijn-belegging. Actuarieel rendement-aanpak: verschil aanschaffingswaarde ↔ terugbetalingswaarde wordt pro rata in resultaat opgenomen (CBN 148/5). Sub: 520 aanschaffingswaarde + 529 waardevermindering.

<small>📖 CBN-advies 148/5 — Actuarieel rendement vastrentende effecten — _cbn_</small>

### 📦 53 — Termijndeposito's

#### Definitie

Cash geblokkeerd op een rekening tegen vooraf vastgelegde looptijd + rente. 530 op meer dan één jaar · 531 op één maand tot één jaar · 532 op ten hoogste één maand.

<small>📖 MAR-KB — klasse 53 — _kb_</small>

### 📦 54-58 — Liquide middelen

#### Definitie

Onmiddellijk beschikbare middelen. 54 te incasseren waarden (cheques in incassoportefeuille) · 55 kredietinstellingen — bank rekening-courant (550-557 per bank) · 56 postchecks · 57 kassen (cash + biljetten). Vreemde valuta tegen koers eind boekjaar (CBN 152/1) — koersverschil naar resultaat.

<small>📖 MAR-KB — klasse 54-58 — _kb_ · CBN-advies 152/1 — Deviezenverrichtingen — _cbn_</small>

> [!example]- Klant betaalt 1.000 EUR op bank
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 550 — Bank A — rekening-courant | 1.000 |  |
> | 400 — Klanten |  | 1.000 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Klasse 5 vs klasse 28 verwarren
> **Verkeerde assumptie**: Alle aandelen aangehouden door een vennootschap horen onder klasse 28.
>
> **Kernpunt**: Onderscheid op INTENTIE + DUUR. Klasse 28: duurzaam (controle/invloed/strategisch). Klasse 51: kortetermijn-belegging (winst halen uit koers, parkeren cash). Wijziging intentie: overdracht tussen klassen via uitzonderlijke verrichting.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Vreemde-valuta-koers vergeten bij eindejaar
> **Verkeerde assumptie**: Bankrekening in USD blijft tegen historische koers staan.
>
> **Kernpunt**: CBN 152/1: vreemde-valuta tegoeden worden eind boekjaar omgezet aan slotkoers. Koersverschil → 654 (negatief koersverschil) of 754 (positief koersverschil). Bij rekening in EUR-zone: geen probleem; bij USD/GBP/CHF: jaarlijks adjustment.
>
> <small>📖 CBN-advies 152/1 — Deviezenverrichtingen — _cbn_</small>

## Accountant-perspectieven

### Onderneming zelf — kasbeheer

#### 📒 Boekhouder

##### 👣 Maandelijkse bank-reconciliatie

Per maand: vergelijk saldo 550 (boekhouding) met bankstaat. Identificeer afwijkingen (cheques in transit, niet-geboekte rente, automatische incasso). Maak reconciliatieverslag — verplicht bewijsstuk voor audit. Saldo 57 (kas) telt fysiek na: registreer afwijking (kasverschil) op 658 (uitzonderlijke kost) of 758.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 Bank confirmation + kas-telling

Bank confirmation: direct contact met alle banken voor saldobevestiging + opgave faciliteiten + waarborgen + tekenbevoegdheden. Kas-telling: fysieke tel op balansdatum (of dichtbij + cut-off-procedures). Voor termijndeposito's: bevestiging looptijd + vroegtijdige uitstap-clausules. ISA 505.

<small>📖 ISA 505 — Externe bevestigingen — _norm_</small>

#### 💰 Fiscaal adviseur

##### 📜 Belasting van meerwaarden + dividenden klasse 5

Meerwaarden aandelen (klasse 51) → belastbaar tegen 25% VenB (art. 192 WIB92), tenzij vrijstelling DBI-aftrek voor deelnemingen met houdduur en minimum-deelneming. Vastrentende effecten (klasse 52): rente naar 750/751, belastbaar als gewone opbrengst. Dividenden ontvangen: roerende voorheffing 30%, te verrekenen tegen VenB.

<small>📖 WIB92 — art. 192 + DBI-regime art. 202-205 — _wettekst_</small>

## Verder lezen (scope-out)

- → Eindejaarsverrichtingen (waardering + correcties) → [[eindejaarsverrichtingen]] _(moet-verwijzen)_
- → Jaarrekening (presentatie balans) → [[jaarrekening]] _(moet-verwijzen)_
- ↪ IFRS-perspectief → [[ifrs]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- ⏳ balans — Vlottende activa — meest liquide categorie.
### `vergelijkbaar_met`
- [[deelneming-financieel-vast-actief]]
    - **Gelijkenissen**:
        - Beide kunnen aandelen bevatten
    - **Verschillen**:
        - Klasse 5 = kortetermijn-belegging; klasse 28 = duurzaam aanhouden
### `triggert`
- [[eindejaarsverrichtingen]] — Waardeverminderings-toets + valutaire conversie.
