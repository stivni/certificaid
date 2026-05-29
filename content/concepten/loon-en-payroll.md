---
title: "Loon en payroll"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 2.2.taak.3
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/loon-en-payroll.json"
---

_Kader_ · ook: payroll · loonberekening · loonadministratie

## Definitie

Loon-en-payroll is het kader dat beschrijft hoe een werkgever in België het loon van een werknemer berekent en de daaruit voortvloeiende verplichtingen voldoet: van het contractueel afgesproken bruto-loon, via de verplichte inhoudingen (RSZ-werknemer + bedrijfsvoorheffing), naar het netto-loon dat de werknemer ontvangt; én van het bruto-loon naar de totale loonkost van de werkgever (bruto + RSZ-werkgever). Het is een deterministische techniek — geen keuze-regime — die alle Belgische werkgevers identiek moeten toepassen op basis van federale wettelijke schalen (RSZ-percentages + BV-schalen uit KB/WIB92 Bijlage III, jaarlijks geïndexeerd in het Cijferzakboekje).

<small>📖 WIB92 — art. 270-275 — _wettekst_ · RSZ-wet 27 juni 1969 — art. 14-23 — _wettekst_</small>

## Substantie

Voor de stagiair is loon-en-payroll het 'rekenmechaniek-record' dat alle losse begrippen (bruto-loon, RSZ, BV, netto) samenbrengt. Vier verschijningsvormen van 'loon' moet je leren onderscheiden: (1) het contractuele bruto-loon (wat in de overeenkomst staat), (2) het belastbaar loon (bruto − RSZ-werknemer; basis voor BV-berekening), (3) het netto-loon (wat de werknemer ontvangt), (4) de totale loonkost werkgever (bruto + RSZ-werkgever). De numerieke afstand tussen (1) en (4) bedraagt ≈ 25-30 %; tussen (1) en (3) ≈ 35-50 %. De 'fiscaal-sociale wig' in België is dus ongeveer de helft van elke euro bruto-loon.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Het loon-en-payroll-kader bestaat als zelfstandig didactisch onderwerp omdat de berekening niet triviaal is en herhaaldelijk dezelfde structuur volgt voor verschillende soorten bezoldigingen (gewoon loon, dertiende maand, vakantiegeld, opzegvergoeding, voordeel alle aard). Door de cascade éénmaal goed te begrijpen, kan de stagiair daarna alle specifieke loonscomponenten correct kwalificeren en boeken. In de praktijk is payroll grotendeels uitbesteed aan sociaal secretariaten (Securex, SD Worx, Acerta, Partena, ...) — maar de accountant blijft eindverantwoordelijk voor de correcte boekhoudkundige verwerking en voor het advies over loonpakket-keuzes.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 270-275 + RSZ-wet 27 juni 1969 + KB/WIB92 Bijlage III

**✅ Voor**
- 📖 Iedere Belgische werkgever met werknemers onder arbeidsovereenkomst. De cascade is verplicht en uniform — geen alternatieven of opt-outs.

## Bouwstenen

### ⚙️ Bruto → BV → RSZ → netto cascade (werknemer-zijde)

De werknemer-zijde van de payroll-cascade in vier stappen: (1) bruto-loon = wat in de arbeidsovereenkomst staat (basisloon + variabel + voordelen in geld); (2) RSZ-werknemer 13,07 % wordt ingehouden op het bruto-loon → restant is het belastbaar loon; (3) bedrijfsvoorheffing wordt ingehouden volgens de schaal van KB/WIB92 Bijlage III (progressief, afhankelijk van belastbaar maandloon + gezinssituatie); (4) netto-loon = belastbaar loon − BV (eventueel + bijzondere bijdrage sociale zekerheid voor hogere lonen). De werkgever stort RSZ-werknemer aan de RSZ en BV aan de fiscus.

<small>📖 RSZ-wet 27 juni 1969 — art. 14-23 — _wettekst_ · WIB92 — art. 270-273 — _wettekst_</small>

### ⚙️ Bruto + RSZ-werkgever → totale loonkost (werkgever-zijde)

De werkgever-zijde: (1) bruto-loon = basis; (2) + werkgevers-RSZ ≈ 25 % (variabel per sector + ondernemingsgrootte, met eventuele structurele verminderingen en doelgroepverminderingen — bv. lage-lonen-bonus, eerste-aanwervings-vermindering); (3) + eventuele Sociaal Fonds-bijdragen (sectoraal); (4) + provisies vakantiegeld en eindejaarspremie (accrual); (5) = totale loonkost werkgever. Bij KMO's komt daar nog bij: aansprakelijkheidsverzekering arbeidsongevallen (FEDRIS), arbeidsgeneeskunde, sociaal secretariaat-fee.

<small>🔗 RSZ-wet 27 juni 1969 — art. 14-23 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Referentie-tabellen — Cijferzakboekje

De exacte percentages en schalen veranderen jaarlijks (indexering, wetswijzigingen). Het Cijferzakboekje van de ITAA — bij het examen beschikbaar — bevat de actuele tarieven: RSZ-percentages werknemer/werkgever per sector, BV-schalen (KB/WIB92 Bijlage III) per gezinssituatie, GGMMI, vakantiegeld-percentages, doelgroepverminderingen. Niet uit het hoofd kennen — opzoeken in het Cijferzakboekje is de juiste methode.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ↪️ Correcties — werkbonus + fiscale aftrekken

Twee belangrijke correcties op de standaard-cascade: (1) werkbonus = vermindering van RSZ-werknemer voor lage lonen (geleidelijk afnemend tot een bovengrens) — verhoogt het netto zonder de werkgever extra te kosten; (2) fiscale werkbonus = vermindering van BV voor lage lonen, vergelijkbaar mechanisme. Beide worden automatisch toegepast door het sociaal secretariaat; de werknemer hoeft niets te vragen. Voor hoge lonen geldt de bijzondere bijdrage voor de sociale zekerheid (BBSZ, geïnde door RSZ, kleinere extra inhouding bovenop RSZ 13,07 %).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Volledige cascade — bediende met bruto € 3.500
> _Sven, bediende PC 200, alleenstaand zonder kinderen, bruto-maandloon 3.500 EUR._
>
> **Berekening:**
>
> - WERKNEMER-ZIJDE
> - 1. Bruto-loon: 3.500,00
> - 2. − RSZ-werknemer 13,07 %: 457,45
> - 3. = Belastbaar loon: 3.042,55
> - 4. − Bedrijfsvoorheffing (schaal alleenstaande, indicatief ≈ 23,8 %): 725,00
> - 5. = Netto-loon: ≈ 2.317
> - WERKGEVER-ZIJDE
> - 1. Bruto-loon: 3.500,00
> - 2. + RSZ-werkgever ≈ 25 %: 875,00
> - 3. + Provisies (1/12 × dubbel vakantiegeld + 1/12 × 13e maand): ≈ 583 (= 16,7 %)
> - 4. = Loonkost van de maand: ≈ 4.958
>
> → **Resultaat**: Voor 3.500 EUR bruto-loon kost de werknemer ≈ 4.958 EUR loonkost (cash + provisies). De werknemer ontvangt ≈ 2.317 EUR netto. Ratio netto/loonkost ≈ 47 % — het andere 53 % gaat naar RSZ, fiscus en uitgestelde verloning.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Eén loonbegrip — 'wat krijg je betaald' — gebruiken voor alle calculaties
> **Verkeerde assumptie**: Het 'loon' van een werknemer is één duidelijk bedrag — wat hij verdient.
>
> **Kernpunt**: Er zijn vier loonbegrippen die je strikt moet onderscheiden: bruto (contract), belastbaar (basis BV), netto (cash naar werknemer), totale loonkost (basis voor accountant). Elke vraag — werknemer-onderhandeling, advies-pricing van talent, audit-test, vergelijking met sector-statistieken — vereist het juiste loonbegrip. Foute keuze = foute conclusie.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Werkgevers-RSZ vergeten in loonkost-budget
> **Verkeerde assumptie**: Een werknemer aanwerven voor 4.000 EUR bruto = 4.000 EUR extra kost.
>
> **Kernpunt**: Voeg minstens 25 % werkgevers-RSZ toe + provisies vakantiegeld en eventueel 13e maand (samen ≈ 18 % extra). Werkelijke jaarkost van een 4.000 EUR-bruto-werknemer voor de werkgever: ≈ 4.000 × (1 + 0,25 + 0,18) = ≈ 5.720 EUR per maand. Plus eenmalige kosten (rekrutering, opleiding) en jaarlijkse kosten (arbeidsgeneeskunde, vorming).
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- BV-schalen uit het hoofd toepassen
> **Verkeerde assumptie**: BV ≈ 25-30 % van het belastbaar loon — 'rond' getal volstaat.
>
> **Kernpunt**: BV is progressief en hangt af van: belastbaar maandloon + gezinssituatie + aantal kinderen ten laste + leeftijd partner. KB/WIB92 Bijlage III bevat ≈ 12 schalen. Bij examen altijd via Cijferzakboekje opzoeken — een wijziging in gezinssituatie kan een verschil van enkele honderden EUR per maand opleveren.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Werkgever-cliënt (alle KMO's met personeel)

_De accountant die loonadministratie superviseert en advies geeft over loonpakketten._

#### 📒 Boekhouder

##### 👣 Verwerking maandelijkse loonjournaal

Sociaal secretariaat levert maandelijks een loonjournaal: per werknemer een lijn met bruto, BV, RSZ-werknemer, RSZ-werkgever, netto. Boekhoudkundige journaalpost: 620 (bruto), 621 (werkgevers-RSZ), tegen 453 (BV), 454 (RSZ-totaal), 455 (netto te betalen). Controleren: aansluiting tussen totaal van loonjournaal en betalingen + aangiften (DmfA, BV-aangifte 274). Doorstortingstermijnen: RSZ kwartaalstaat + BV ten laatste de 15e van de volgende maand.

<small>📖 CBN-advies 2016/15 — Boekingen tijdens het boekjaar — _advies_</small>

#### 🧭 Adviseur

##### 🧭 Loonpakket-mix optimalisatie

Bij vraag 'hoe het netto van mijn werknemer verhogen zonder mijn kost te verdubbelen': de cascade is ongeveer 1 EUR netto = 2 EUR loonkost. Alternatieven met betere ratio: maaltijdcheques (≈ 1 EUR netto = 1,09 EUR kost), ecocheques, groepsverzekering (uitstel naar pensioen, gunstig regime), mobiliteitsbudget, bedrijfsfiets. Adviseer cliënt om eerst maaltijd- en ecocheques tot het maximum te benutten alvorens loonsverhoging te overwegen. Zie werknemers-vergoedingen-cluster voor het keuzepalet.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 Volledigheidstest payroll

Substantieve audit-procedure: (1) aansluiting jaartotaal klasse 62 ↔ som van fiches 281.10 (alle werknemers) + 281.20 (alle bedrijfsleiders); (2) provisies vakantiegeld en eindejaarspremie cijfermatig recompureren (18,2 % bedienden bruto-jaarloon); (3) gevoeligheid voor cut-off december/januari; (4) doelgroepverminderingen verifiëren (een misbruikte vermindering is materiële fraude-indicator).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Werknemers-vergoedingen Σ (alternatieven vs loon) → [[werknemers-vergoedingen]] _(moet-verwijzen)_
- → Bedrijfsleider-bezoldigingsmix (geen RSZ-werknemer) → [[bedrijfsleidersbezoldiging]] _(moet-verwijzen)_
- → Componenten — bruto-loon → [[bruto-loon]] _(moet-verwijzen)_
- → Componenten — bedrijfsvoorheffing → [[bedrijfsvoorheffing]] _(moet-verwijzen)_
- → RSZ-werknemer → [[rsz-werknemer]] _(moet-verwijzen)_
- → RSZ-werkgever → [[rsz-werkgever]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[werknemers-vergoedingen]]
### `bevat`
- [[bruto-loon]]
- [[bedrijfsvoorheffing]]
- [[rsz-werknemer]]
- [[rsz-werkgever]]
- [[dertiende-maand]]
- [[eindejaarspremie]]
- [[enkel-en-dubbel-vakantiegeld]]
- [[opzegvergoeding]]
### `vergelijkbaar_met`
- [[bedrijfsleidersbezoldiging]]
    - **Gelijkenissen**:
        - Beide zijn bezoldigings-cascades: van bruto naar netto
        - Beide worden onderworpen aan bedrijfsvoorheffing
    - **Verschillen**:
        - Werknemer-payroll: RSZ-werknemer 13,07 % + RSZ-werkgever 25 %
        - Bedrijfsleider: sociale bijdragen zelfstandigen (degressief, plafond)
        - Werknemer: BV via Bijlage III maandelijkse schaal
        - Bedrijfsleider: BV soms via afzonderlijke berekening of voorafbetalingen
    - ⚠️ **Verwarringsrisico**: Voor een bedrijfsleider-werknemer-mix (= zaakvoerder + tweede pet als werknemer) moet je beide cascades naast elkaar berekenen — courante fout bij familiale vennootschappen.
