---
title: "Financiele leasing"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 3.0.IV.D
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/financiele-leasing.json"
---

_Instrument_ · ook: financial lease · capital lease · on-balance lease

## Definitie

Financiele leasing is een leasingvorm waarbij economisch gezien bijna alle risico's en voordelen van de eigendom van het actief overgaan op de leasingnemer, ook al blijft de leasinggever juridisch eigenaar tijdens de looptijd. Boekhoudkundig boekt de leasingnemer het actief op als eigen vast actief en de tegenwaarde van de leaseverplichtingen als schuld - 'on-balance verwerking'. Het actief wordt afgeschreven over zijn economische levensduur; de jaarlijkse leasevergoeding wordt gesplitst in een kapitaalaflossing (afboeking van de leasingschuld) en een rente-element (financiële kost). Onder BE-GAAP wordt de kwalificatie gestuurd door de wedersamenstelling-van-kapitaal-test en de 15%-koopoptieregel (CBN-advies 2015/4).

<small>📖 KB WVV — art. 3:89 — _kb_ · CBN-advies 2015/4 — Kwalificatiecriteria — _cbn_ · IFRS 16 (Verordening (EU) 2023/1803) — Definitie financiele lease - alinea 62 — _wettekst_</small>

## Substantie

Voor de leasingnemer voelt een financiele leasing economisch aan als een banklening voor een investering: hij gebruikt het actief als ware hij eigenaar (afschrijft het, betaalt de financieringskost), maar moet pas op het einde via de koopoptie de formele eigendom verwerven. Op de balans zijn de gevolgen dezelfde als een gekochte machine met banklening: actief in vaste activa, schuld in passief. De winst-en-verliesrekening toont afschrijving + rentekost - geen 'huurpenning' meer. Het verschil met een banklening zit in de waarborgenstructuur: bij financiele leasing is het actief zelf de waarborg (de leasinggever blijft eigenaar), wat soepelere kredietvoorwaarden mogelijk maakt.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De rationale van de on-balance-verwerking is substantie-over-vorm: wanneer de economische realiteit (de leasingnemer draagt het ondernemingsrisico, geniet de voordelen, betaalt alles terug) overeenstemt met eigendom, mag de juridische vorm van een huurcontract dat niet verbergen. Anders zou een onderneming makkelijk schulden buiten balans kunnen schuiven via een leasingstructuur en de solvabiliteitsratio's verbeteren. CBN-advies 2015/4 (BE-GAAP) en IFRS 16 (internationaal) volgen beide dit principe, zij het met andere drempels: BE-GAAP via wedersamenstelling + 15%-regel, IFRS 16 sinds 2019 via een eenvoudige regel 'bijna alle leases on-balance bij lessee'.

<small>🔗 CBN-advies 2015/4 — Economische realiteit primeert — _cbn_ · IFRS 16 (Verordening (EU) 2023/1803) — alinea 63 — _wettekst_</small>

## Gebruikscontext

**Status**: `in-voege` · basis: BE-GAAP: KB WVV art. 3:89 + CBN-advies 2015/4. IFRS: IFRS 16 (Verordening (EU) 2023/1803).

**✅ Voor**
- 🔗 Lange-termijn-financiering van een duurzaam actief waarbij de leasingnemer het actief tot het einde van zijn economische levensduur (of significant deel daarvan) wil gebruiken en uiteindelijk eigenaar wil worden. Typische voorbeelden: industriële machines, vrachtwagens, gebouwen.

**👍 Voordeel**
- 🔗 Volledige financiering zonder eigen inbreng. Aftrekbaarheid via afschrijving + rente (volledig aftrekbaar binnen art. 198/1 WIB92). Actief zelf dient als waarborg - vaak soepelere kredietvoorwaarden dan een banklening. Bij koopoptie <=15%: eigenaarschap op het einde tegen lage uitoefenprijs.

**⚠️ Risico**
- 🔗 On-balance-verwerking verzwaart de balans (hoger balanstotaal) en kan de solvabiliteitsratio verlagen. Vroegtijdige beëindiging is vaak duur (vergoedingsclausules in het contract). Bij faillissement van de leasingnemer kan de leasinggever het actief terugnemen - de leasingnemer verliest zowel het gebruik als de reeds betaalde bedragen.

## Bouwstenen

### 📜 Kwalificatie BE-GAAP - wedersamenstelling en 15%-regel

Een leasing wordt onder BE-GAAP gekwalificeerd als financiele leasing wanneer de som van (a) de contractuele leasevergoedingen + (b) de uitoefenprijs van de koopoptie (alleen indien <=15% van het door de leasinggever geinvesteerde kapitaal in het goed) het volledig geinvesteerde kapitaal van de leasinggever wedersamentelt. De wedersamenstelling betekent: terugbetaling van het kapitaal + rentevergoeding. Wanneer deze cumulatie inclusief koopoptie het geinvesteerde kapitaal niet bereikt (typisch wanneer koopoptie boven 15% ligt), of wanneer de wedersamenstelling onvolledig is, kwalificeert de leasing als operationele leasing.

<small>📖 CBN-advies 2015/4 — Aankoopoptie + wedersamenstelling kapitaal — _cbn_</small>

### ⚙️ On-balance verwerking - boekingsschema

Bij aanvang: D actief (22 gebouwen / 23 machines / 24 voertuigen, ...) | C 172 'Leasingschulden en soortgelijke' voor de actuele waarde van de leaseverplichtingen (= geinvesteerd kapitaal van de leasinggever). Bij elke leasevergoeding: split kapitaalaflossing en rente. Boeking: D 172 (kapitaaldeel) + D 650 (rentedeel) | C 55 Bank (totale vergoeding). Bij elke afsluiting: afschrijving van het actief - D 6302 | C 23X (geboekte afschrijvingen). Het deel van de leasingschuld dat binnen het jaar opeisbaar wordt, wordt overgeheveld van 172 naar 423 (kortlopend deel).

<small>📖 CBN-advies 2015/4 — Boekhoudkundige verwerking financiele leasing — _cbn_ · KB 29-04-2019 jaarrekening — MAR rekeningen 172 / 423 / 6302 / 650 — _kb_</small>

### 📜 Afschrijving - keuze tussen economische levensduur en leasingperiode

Als de leasingnemer redelijke zekerheid heeft dat hij op het einde de eigendom zal verwerven (lage koopoptie of automatische overdracht), wordt het actief afgeschreven over zijn volledige economische levensduur. Heeft hij die zekerheid niet, dan wordt afgeschreven over de korter looptijd van leasingperiode of economische levensduur. Belangrijk voor afschrijvingsplan en fiscale optimalisatie.

<small>🔗 CBN-advies 2015/4 — Afschrijving leasing-actief — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 👣 Verwerking koopoptie aan einde van het contract

Bij lichting van de koopoptie: D 22-24 (actief, tegen uitoefenprijs) | C 55 Bank. Bij niet-lichting en teruggave van het actief: afboeking netto-boekwaarde - D 6302 (afschrijving versneld) | C 23X (geboekte afschrijvingen) tot netto-boekwaarde = 0, dan D 23X | C 22-24 om het actief volledig af te boeken. Eventueel verschil met de uitoefenprijs in resultaat. Belangrijk: de boeking moet kloppen met de werkelijke transactie - er is geen volledige standaardroute.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Financiele leasing voor een productiemachine
> _BV Optima least een productiemachine van 100.000 EUR. Looptijd 5 jaar, jaarlijkse leasingvergoeding 22.000 EUR (waarvan ~20.000 EUR kapitaal + ~2.000 EUR rente in jaar 1), koopoptie 1.000 EUR (= 1% van kapitaal, ruim onder 15%). Machine afgeschreven over 10 jaar economische levensduur._
>
> **📒 Aanvang - opname actief en leasingschuld**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 23 - Installaties, machines, uitrusting | 100.000 |  |
> | 172 - Leasingschulden en soortgelijke |  | 100.000 |
>
> **📒 Jaarlijkse leasingvergoeding (jaar 1)**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 172 - Leasingschulden (kapitaalaflossing) | 20.000 |  |
> | 650 - Rentelasten | 2.000 |  |
> | 55 - Bank |  | 22.000 |
>
> **📒 Jaarlijkse afschrijving (10% lineair over 10 jaar)**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 6302 - Afschrijvingen op materiele vaste activa | 10.000 |  |
> | 239 - Geboekte afschrijvingen |  | 10.000 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28) · CBN-advies 2015/4 — Methodologie — _cbn_</small>

## Valkuilen

> [!warning]- Kapitaal en rente samen als 'leasingkost' boeken
> **Verkeerde assumptie**: Bij financiele leasing boek je de leasingvergoeding gewoon als kost in resultaat.
>
> **Kernpunt**: Bij financiele leasing wordt de leasingvergoeding gesplitst: het kapitaalgedeelte gaat af van de leasingschuld (172), het rentegedeelte komt in resultaat (650). Het volledige bedrag als kost boeken is fout - daarmee zou je de financiering ineens als kost erkennen en het actief op de balans dubbel afschrijven. De rentecomponent wordt typisch via een actuariële berekening bepaald op basis van het uitstaande saldo en de impliciete interestvoet van de lease.
>
> <small>📖 CBN-advies 2015/4 — Boekhoudkundige verwerking - splitsing kapitaal/rente — _cbn_</small>

> [!warning]- Het actief afschrijven over de leasingperiode in plaats van de economische levensduur
> **Verkeerde assumptie**: Het leasing-actief wordt afgeschreven over de looptijd van het contract.
>
> **Kernpunt**: Wanneer de leasingnemer redelijke zekerheid heeft van eigendomsoverdracht aan het einde (lage koopoptie, automatische overdracht), wordt afgeschreven over de volledige economische levensduur. Een 5-jaars-leasing op een machine met 10 jaar economische levensduur en lage koopoptie wordt afgeschreven over 10 jaar - niet over 5. Wel afschrijven over de leasingperiode als die korter is en eigendomsoverdracht onzeker.
>
> <small>🔗 CBN-advies 2015/4 — Afschrijving — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Leasingnemer (cliëntvennootschap)

_De accountant die de financiele leasing bij de cliënt-vennootschap boekhoudkundig verwerkt en de jaarlijkse afsluiting opvolgt._

#### 📒 Boekhouder

##### 👣 Stappenplan boekhoudkundige verwerking

(1) Kwalificeer eerst de leasing als financieel (CBN 2015/4). (2) Bij aanvang: boek het actief tegen de waarde van de leaseverplichtingen (= geinvesteerd kapitaal leasinggever). (3) Bouw een leasingschema op met per jaar: leasingvergoeding, kapitaaldeel, rentedeel, uitstaand saldo. (4) Bij elke periodieke betaling: gebruik dat schema voor de boeking. (5) Bij elke boekjaarafsluiting: afschrijving op het actief + overheveling van het binnen het jaar opeisbare deel van 172 naar 423. (6) Bij eindtermijn: koopoptie lichten of teruggave - boek conform de werkelijke transactie.

<small>🔗 CBN-advies 2015/4 — Boekhoudkundige verwerking — _cbn_</small>

## Verder lezen (scope-out)

- → Leasing-parent - algemeen kader → [[leasing]] _(moet-verwijzen)_
- → Operationele leasing - tegenpool met off-balance-verwerking → [[operationele-leasing]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[leasing]]
### `vergelijkbaar_met`
- [[operationele-leasing]]
    - **Gelijkenissen**:
        - Beide vallen onder hetzelfde fiscale en juridische leasingkader (BE-GAAP + IFRS 16)
        - Beide hebben dezelfde driepartijenstructuur (leasinggever - leasingnemer - actief)
    - **Verschillen**:
        - Financiele leasing: on-balance bij lessee onder BE-GAAP (actief + leasingschuld); operationele: off-balance (huurkost in resultaat)
        - Financiele leasing: substantie van eigendomsoverdracht (lage koopoptie, lange looptijd); operationele: gebruiksrecht zonder eigendomsoverdracht
        - Financiele leasing: aftrek via afschrijving + rente; operationele: volledige huurpenning aftrekbaar
        - IFRS 16: voor lessee is dit onderscheid verdwenen - alles on-balance behalve short-term en low-value
    - ⚠️ **Verwarringsrisico**: Kwalificatie hangt af van details (koopoptieprijs, contractduur, gebruiksgraad). Zelfde economische situatie kan onder BE-GAAP operationeel en onder IFRS financieel zijn.
