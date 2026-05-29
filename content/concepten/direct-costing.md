---
title: "Direct costing (variabele-kost-aanpak)"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 1.8.III.B
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/direct-costing.json"
---

_Procedure_ · ook: variable costing · marginal costing · variabele-kostencalculatie

## Definitie

Direct costing (ook variable of marginal costing) is de kostprijsmethode waarbij alleen de variabele kosten van een product in de kostprijs worden opgenomen. Vaste kosten — productie én niet-productie — worden behandeld als periodekosten die direct in het resultaat van de periode komen. De resultatenrekening wordt opgesteld in een 'contributiemarge-formaat': omzet minus variabele kosten = contributiemarge, en daarvan worden de vaste kosten afgetrokken om het resultaat te bepalen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

Direct costing draait de redenering om: niet 'wat kost dit product gemiddeld om te produceren?', maar 'wat brengt dit product bij als ik er één extra verkoop?'. Die laatste vraag is beslissings-relevant — vaste kosten lopen toch door, of we nu één tafel meer of minder verkopen. Het ratio omzet ↔ contributiemarge wordt zo de prijsondergrens voor kortetermijn-beslissingen (extra order, special order, make-or-buy in bestaande capaciteit). Voor langetermijn-prijszetting en jaarrekening volstaat direct costing echter niet — daar moet full costing gebruikt worden.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Het uitgangspunt van direct costing is dat vaste kosten niet causaal verbonden zijn aan één extra eenheid productie — ze ontstaan door beslissingen over capaciteit en niet door beslissingen over volume binnen die capaciteit. Daarom is het misleidend ze in de productkost te stoppen wanneer je beslissingen evalueert binnen het relevant range. De contributiemarge meet de werkelijke marginale bijdrage per eenheid, los van toerekening-arbitraires.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Korte-termijn beslissingen waarbij vaste kosten onvermijdelijk zijn: accept-or-reject extra order, make-or-buy in bestaande capaciteit, product-mix-optimalisatie bij capaciteitsbeperking, break-even-analyse, sensitiviteitsanalyse bij prijs- of volume-wijzigingen.

**🚫 Niet voor**
- 🔗 Stockwaardering in de jaarrekening — onder IAS 2 én KB W.Venn. moeten voorraden gewaardeerd worden inclusief vaste productie-overhead (= full costing). Direct costing voor de jaarrekening is dus niet toegestaan. Direct costing is ook misleidend voor langetermijn-prijszetting — verkoopprijzen die alleen de variabele kost dekken, leiden over de cyclus tot verlies.

## Bouwstenen

### 🧮 Contributiemarge — kern-begrip

Contributiemarge (CM) = verkoopprijs per eenheid − variabele kost per eenheid. Op totaal-niveau: CM-totaal = totale omzet − totale variabele kosten. De CM 'draagt bij' aan de dekking van de vaste kosten + winst. CM-ratio = CM / omzet (% van omzet dat beschikbaar blijft na variabele kosten). Een hoge CM-ratio (typisch dienstverlening: 60-80%) betekent dat één extra verkochte eenheid bijna volledig naar winst gaat zodra vaste kosten gedekt zijn; een lage CM-ratio (typisch handel: 10-25%) betekent dat je veel volume nodig hebt om winst te maken.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Contributiemarge-formaat resultatenrekening

In direct costing wordt de resultatenrekening opgesteld in vijf lagen: (1) Omzet; (2) min Variabele productiekosten = Contributiemarge productie; (3) min Variabele verkoopkosten (bv. commissies) = Contributiemarge totaal; (4) min Vaste productiekosten + Vaste verkoop/administratie-kosten; (5) = Bedrijfsresultaat. Dit verschilt van het full-costing-formaat (omzet − cost of goods sold = brutomarge − operationele kosten = bedrijfsresultaat). Het verschil is leerzaam: in direct-costing-formaat zie je onmiddellijk de hefboomstructuur (operating leverage).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Verschil in resultaat — full vs direct costing bij voorraadwijziging

Bij gelijke verkoop en productie geven full costing en direct costing hetzelfde resultaat. Bij stijgende voorraad geeft full costing een hoger resultaat dan direct costing (omdat een deel van de vaste productiekosten in voorraad blijft 'opgeslagen' en niet in resultaat valt). Bij dalende voorraad omgekeerd. Het verschil = vaste overhead per eenheid × voorraadwijziging in eenheden. Examenvalkuil: studenten denken dat de twee methodes 'hetzelfde resultaat over tijd' geven — dat klopt alleen als de totale productie = totale verkoop over de gehele beschouwingsperiode.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Zelena Bio NV — direct costing vs full costing bij voorraadwijziging
> _Zelena Bio produceert 1.000 tafels in jaar 1, verkoopt 800 (200 in voorraad). Variabele kost: 250 EUR/tafel. Vaste productiekost jaar: 100.000 EUR. Verkoopprijs: 500 EUR/tafel. Geen variabele verkoopkosten._
>
> | Post | Direct costing | Full costing |
>
> | --- | --- | --- |
>
> | Omzet | 800 × 500 = 400.000 | 800 × 500 = 400.000 |
>
> | min Variabele productiekost verkocht | 800 × 250 = 200.000 | — |
>
> | = Contributiemarge | 200.000 | — |
>
> | min Cost of goods sold (variabel + vast pro rata) | — | 800 × (250 + 100) = 280.000 |
>
> | = Brutomarge | — | 120.000 |
>
> | min Vaste productiekost in resultaat | 100.000 (volledig) | 20.000 (alleen idle-deel + niet-toegerekend) |
>
> | = Bedrijfsresultaat | 100.000 | 120.000 |
>
> **🧮 Verklaring verschil**
>
> - Verschil = 120.000 − 100.000 = 20.000 EUR
> - Bij full costing zit 200 tafels × 100 EUR vaste overhead = 20.000 EUR 'opgesloten' in de stockwaardering
> - Bij direct costing valt die 20.000 EUR direct in het resultaat van jaar 1
> - Wanneer jaar 2 de voorraad terug naar 0 brengt, draait het verschil zich om — over de twee jaren samen geven beide methodes hetzelfde resultaat.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Direct costing-prijs als langetermijn-prijs gebruiken
> **Verkeerde assumptie**: 'De variabele kost is 250 EUR; als ik 350 EUR vraag heb ik 100 EUR winst per tafel.'
>
> **Kernpunt**: 100 EUR contributiemarge per tafel is geen winst — het is een bijdrage aan de dekking van de vaste kosten. Pas wanneer de totale CM > totale vaste kosten ontstaat er winst. Bij 100.000 EUR vaste kosten heb je 1.000 tafels nodig om break-even te draaien.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Direct costing gebruiken in de gepubliceerde jaarrekening
> **Verkeerde assumptie**: Direct costing is een geldige boekhoudkundige methode voor voorraadwaardering.
>
> **Kernpunt**: Direct costing is interne management-keuze en GEEN aanvaarde methode onder IAS 2 of KB W.Venn. voor externe rapportering. Voor de jaarrekening moet de voorraad gewaardeerd worden inclusief vaste productie-overhead (full costing). Direct costing leeft alleen in de interne dashboards.
>
> <small>📖 Verordening (EU) 2023/1803 — geconsolideerde IFRS — IAS 2.10 — _richtlijn_</small>

## Accountant-perspectieven

### Advies extra order met restcapaciteit

_Een productie-cliente krijgt een extra order onder de normale verkoopprijs en vraagt of ze die mag accepteren._

#### 🧭 Adviseur

##### 👣 Contributiemarge-test

Als de extra order capaciteit gebruikt die anders ongebruikt blijft (geen extra vaste kosten): aanvaardingscriterium = aangeboden prijs > variabele kost. Elke euro daarboven is contributiemarge en dus winstverhogend. Belangrijk: dit geldt alleen op korte termijn en bij vrije capaciteit. Bij volle capaciteit ontstaan opportunity costs (gemiste verkoop tegen normale prijs) — die moeten meegeteld worden als 'kost' van de extra order.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Kostprijsmethoden Σ-keuze-kader → [[kostprijsmethoden]] _(moet-verwijzen)_
- ↪ Break-even-analyse (toepassings-cross) → [[break-even-analyse]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[kostprijsmethoden]]
### `vergelijkbaar_met`
- [[full-costing]]
    - **Gelijkenissen**:
        - Beide rekenen variabele productiekosten toe aan het product
        - Beide gebruiken cost-drivers voor toerekening van indirecte kosten waar dat zinvol is
    - **Verschillen**:
        - Direct costing behandelt vaste productiekosten als periodekost; full costing rekent ze toe aan productkost
        - Direct costing is interne management-keuze; full costing is verplicht voor jaarrekening-stockwaardering
        - Bij voorraadwijziging geven beide verschillende resultaten — verschil = vaste overhead × voorraad-Δ
    - ⚠️ **Verwarringsrisico**: Studenten gebruiken direct costing voor de jaarrekening — dat is niet toegestaan.
### `vereist`
- [[break-even-analyse]] — Break-even-analyse bouwt op de contributiemarge-redenering van direct costing.
