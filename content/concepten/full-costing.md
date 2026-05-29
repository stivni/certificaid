---
title: "Full costing (volledige kostencalculatie)"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 1.8.III.A
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/full-costing.json"
---

_Procedure_ · ook: absorptie-methode · full absorption costing · volledige kostencalculatie

## Definitie

Full costing (volledige kostencalculatie of absorptie-methode) is de kostprijsmethode waarbij alle productiekosten — zowel variabele als vaste — worden toegerekend aan het product. Variabele kosten (grondstof, productie-arbeid, energie) gaan rechtstreeks naar het product; vaste productiekosten (huur fabriek, afschrijving productie-uitrusting, salaris werkleider) worden via een toerekeningssleutel (cost-driver: machine-uren, arbeidsuren, productie-eenheden) verdeeld over de productie van de periode. Resultaat: één integrale kostprijs per eenheid die de volledige kost van produceren weerspiegelt.

<small>🔗 Verordening (EU) 2023/1803 — geconsolideerde IFRS — IAS 2.10-15 — voorraden gewaardeerd inclusief vaste productie-overhead — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

Voor de stagiair: full costing is 'wat de jaarrekening doet'. Wanneer een product op voorraad ligt op 31 december, draagt het zijn aandeel in de vaste productiekosten met zich mee in de balans — die kosten worden pas resultaat-effectief bij verkoop. Dit is wettelijk vereist onder zowel B-GAAP (KB W.Venn.) als IAS 2 (IFRS). Daardoor is full costing niet alleen een management-keuze, maar voor stockwaardering ook een verplichting. Het management gebruikt full costing daarbij voor langetermijn-prijszetting: een verkoopprijs onder de full cost dekt de vaste kosten niet en is onhoudbaar over een volle conjunctuurcyclus.

<small>🔗 Verordening (EU) 2023/1803 — geconsolideerde IFRS — IAS 2 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De wetgever vraagt full costing voor stockwaardering omdat een product op voorraad 'gemaakt' is met behulp van vaste productiemiddelen — het zou een verkeerd beeld geven om de afschrijving op de productiehal volledig in resultaat te boeken in het jaar van productie en niet in het jaar van verkoop. Het matching-principe (kosten matchen met de opbrengsten die ze genereren) vereist dat productiekosten — vast én variabel — in de stockwaardering blijven tot verkoop.

<small>🔗 Verordening (EU) 2023/1803 — geconsolideerde IFRS — IAS 2.10 + matching-principle — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Stockwaardering in de jaarrekening (verplicht onder B-GAAP en IAS 2) · langetermijn-prijszetting · winstmarge-analyse per product · interne benchmarking tussen vestigingen of perioden.

**🚫 Niet voor**
- 🔗 Korte-termijn beslissingen waarbij vaste kosten onvermijdelijk zijn (extra order accepteren, make-or-buy in bestaande capaciteit). In die context misleidt full costing — gebruik direct costing.

## Bouwstenen

### 👣 Toerekeningsstappen — directe → indirecte kosten

Stap 1 — directe variabele kosten rechtstreeks aan het kostenobject toerekenen (grondstof, productie-arbeid). Stap 2 — directe vaste kosten (machine specifiek voor één product) eveneens rechtstreeks toerekenen. Stap 3 — indirecte productiekosten (huur fabriek, kaderloon werkleider, afschrijving CNC die meerdere producten bedient) bundelen in cost-pools per afdeling of activity. Stap 4 — elke cost-pool via een cost-driver (machine-uren, directe arbeidsuren, productie-eenheden) verdelen over de kostenobjecten. Stap 5 — niet-productiekosten (verkoop, administratie, financieel) NIET in de productkost meenemen — die zijn periodekosten (KB W.Venn. + IAS 2 sluiten deze uit van voorraadwaardering).

<small>📖 Verordening (EU) 2023/1803 — geconsolideerde IFRS — IAS 2.10-19 — _richtlijn_</small>

### 📜 Onderbenutting van capaciteit — idle capacity expense

Wanneer de werkelijke productie onder de normale capaciteit ligt (gepland productieniveau bij normale bezetting), mag de vaste productiekost niet volledig over de werkelijk geproduceerde eenheden worden uitgesmeerd — dat zou de eenheidskost kunstmatig opblazen. IAS 2.13 vereist dat de niet-toegerekende vaste overhead direct als periodekost (idle capacity expense) wordt geboekt. Concreet: vaste overhead 100.000 EUR voor normale productie van 1.000 eenheden = 100 EUR/eenheid normkost. Bij werkelijke productie van 700 eenheden: alleen 70.000 EUR in stockwaardering, 30.000 EUR direct als periodekost (verlies door onderbenutting).

<small>📖 Verordening (EU) 2023/1803 — geconsolideerde IFRS — IAS 2.13 — _richtlijn_</small>

### 💡 Productie- versus periodekosten

Productiekosten (in stockwaardering): grondstoffen, productie-arbeid, fabriekshuur, afschrijving productiemiddelen, kwaliteitscontrole, productie-toezicht, productie-energie. Periodekosten (direct in resultaat): verkoopcommissies, administratiekantoor, marketing, financiële kosten, R&D (tenzij gekapitaliseerd onder IAS 38). Bij onduidelijke kosten (huurkost gebouw met productie + administratie): toerekening pro rata vloeroppervlak of FTE.

<small>📖 Verordening (EU) 2023/1803 — geconsolideerde IFRS — IAS 2.16 — uitgesloten kosten — _richtlijn_</small>

## Voorbeelden

> [!example]- Zelena Bio NV — full costing met idle capacity
> _Zelena Bio plant 1.000 tafels per maand (normale capaciteit). Variabele productiekost: 250 EUR/tafel. Vaste productiekost: 100.000 EUR/maand (huur, afschrijving, kaderloon). In maart werkelijk 700 tafels geproduceerd._
>
> **🧮 Stockwaardering full costing met idle capacity**
>
> - Normale vaste overhead per tafel = 100.000 / 1.000 = 100 EUR (normkost)
> - Full cost per tafel (normaal) = 250 (variabel) + 100 (vast) = 350 EUR
> - Werkelijke productie maart = 700 tafels
> - Vaste overhead in stockwaardering = 700 × 100 = 70.000 EUR
> - Niet-toegerekende vaste overhead (idle capacity) = 100.000 − 70.000 = 30.000 EUR → direct als periodekost
> - Stockwaardering totaal: 700 × 350 = 245.000 EUR (175.000 variabel + 70.000 toegerekende vaste overhead)
>
> → **Resultaat**: 30.000 EUR verschijnt als 'verlies door onderbenutting' in resultatenrekening, los van de verkoopwinst op de tafels.
>
> **📒 Boeking idle capacity expense**
>
> | Rekening | Debet | Credit | Omschrijving |
> | --- | --- | --- | --- |
> | 640 — Andere bedrijfskosten (idle capacity) | 30.000 |  |  |
> | 32 — Voorraad afgewerkte producten | 245.000 |  |  |
> | Diverse productiekosten (klasse 60-62) |  | 275.000 | Totaal werkelijk gemaakte kosten |
>
> <small>🔗 Verordening (EU) 2023/1803 — geconsolideerde IFRS — IAS 2.13 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Vaste overhead 'gewoon' delen door werkelijke productie
> **Verkeerde assumptie**: Vaste kost van de maand / aantal geproduceerd = kostprijs.
>
> **Kernpunt**: Bij onderbenutting (werkelijke productie < normale capaciteit) mag de vaste overhead alleen pro-rata-normaal in de stockwaardering. Het surplus (idle capacity) is een periode-verlies. IAS 2.13 schrijft dit expliciet voor. Anders verberg je structurele onderbenutting in opgepompte stockwaarden.
>
> <small>📖 Verordening (EU) 2023/1803 — geconsolideerde IFRS — IAS 2.13 — _richtlijn_</small>

> [!warning]- Verkoopkosten in productkost meenemen
> **Verkeerde assumptie**: Alle kosten van de onderneming verdelen over de producten — ook administratie en verkoop.
>
> **Kernpunt**: Alleen productiekosten gaan in de stockwaardering. Verkoop, administratie en financiële kosten zijn periodekosten — direct in resultaat van de periode waarin ze gemaakt worden. Dit volgt direct uit IAS 2.16 én KB W.Venn.
>
> <small>📖 Verordening (EU) 2023/1803 — geconsolideerde IFRS — IAS 2.16 — _richtlijn_</small>

## Accountant-perspectieven

### Audit van stockwaardering

_De auditor controleert dat de stock correct full-costing-gewaardeerd is._

#### 🔍 Auditor

##### 👣 Controle op idle capacity expense

Bij sterke productie-daling (>15% onder normale capaciteit): nagaan of de cliente vaste overhead pro-rata-werkelijk in stockwaardering heeft gestoken (verkeerd) of pro-rata-normaal (correct, IAS 2.13). Bij verkeerde toerekening: stockwaardering opwaarts vertekend, resultaat opwaarts vertekend. Materialiteit-risico hoog bij sterk-conjunctuurgevoelige industrieën.

<small>🔗 Verordening (EU) 2023/1803 — geconsolideerde IFRS — IAS 2.13 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Kostprijsmethoden Σ-keuze-kader → [[kostprijsmethoden]] _(moet-verwijzen)_
- ↪ Analytische boekhouding (parent) → [[analytische-boekhouding]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[kostprijsmethoden]]
### `vergelijkbaar_met`
- [[direct-costing]]
    - **Gelijkenissen**:
        - Beide rekenen variabele productiekosten toe aan het product
        - Beide vereisen een onderscheid tussen productiekosten en niet-productiekosten
    - **Verschillen**:
        - Full costing rekent vaste productiekosten ook toe aan productkost; direct costing behandelt vaste productiekosten als periodekost
        - Full costing is verplicht voor jaarrekening-stockwaardering; direct costing is interne management-keuze
        - Bij voorraadwijziging geeft full costing en direct costing verschillende resultaten in dezelfde periode
    - ⚠️ **Verwarringsrisico**: Studenten denken dat de keuze 'full vs direct' een vrije keuze is — voor de jaarrekening is dat niet zo. Voor stockwaardering is full costing wettelijk verplicht.
