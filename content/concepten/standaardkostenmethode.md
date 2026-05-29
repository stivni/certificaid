---
title: "Standaardkostenmethode"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 1.8.III.C
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/standaardkostenmethode.json"
---

_Procedure_ · ook: standard costing · voorafbepaalde kostenmethode · norm-kostenmethode

## Definitie

De standaardkostenmethode (standard costing) is de kostprijsmethode die werkt met voorafbepaalde norm-kosten per eenheid. Voor elke kostencategorie (grondstof, productie-arbeid, overhead) wordt vóór de productie-periode een standaard vastgelegd in termen van hoeveelheid × prijs (bv. 2 kg hout × 50 EUR/kg = 100 EUR grondstof per tafel). Tijdens de periode wordt geboekt aan standaardkost; aan het eind van de periode worden de werkelijke kosten vergeleken met de standaard en de afwijkingen (varianties) systematisch geanalyseerd via variantieanalyse.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

Voor de stagiair: de standaardkostenmethode draait de logica om. In plaats van eerst werkelijke kosten te boeken en dan te analyseren, leg je eerst de norm vast en boek je 'aan norm'. Het verschil tussen norm en werkelijkheid wordt zichtbaar — en dat verschil is de management-informatie. Het systeem dwingt de organisatie om te denken in termen van wat een product 'hoort te kosten' en niet alleen wat het 'kost'. Daardoor wordt efficiency meetbaar: een 5% prijsstijging op grondstoffen is een prijsvariantie waar de inkoop verantwoordelijk voor is; een 5% extra grondstofverbruik per tafel is een hoeveelheidsvariantie waar de productie verantwoordelijk voor is.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Twee redenen voor het gebruik: (1) management-by-exception — de directie hoeft niet alle cijfers te lezen, maar krijgt alleen de afwijkingen boven een materialiteitsdrempel; (2) verantwoordelijkheid afbakenen — door varianties op te splitsen naar oorzaak (prijs versus hoeveelheid, inkoop versus productie) kunnen ze toegewezen worden aan de manager die ze kan beïnvloeden. De methode werkt het best in productie-omgevingen met repetitieve, voorspelbare productieprocessen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Productie-ondernemingen met repetitieve, voorspelbare processen (massaproductie, batch-productie van uniforme artikelen). Branches: maakindustrie, voedingsverwerking, chemische productie. Efficiency-opvolging op afdelingsniveau.

**🚫 Niet voor**
- 🔗 Project-organisaties (bouw, consulting, software-ontwikkeling) waar elke opdracht uniek is — daar werkt offerte-calculatie + nacalculatie per project beter dan een standaardkostenmethode. Ook ondernemingen met sterk fluctuerende inputprijzen (commodity-trading): de standaard veroudert te snel.

## Bouwstenen

### 💡 Soorten standaarden — ideaal · haalbaar · historisch

Ideale (theoretische) standaard: kost bij perfecte efficiency, zonder uitval, stilstand of fouten — alleen relevant als motiverend doel, niet als budget-basis. Haalbare (realistische) standaard: kost bij goede maar realistische operationele werking — accepteert normale uitval, korte stilstanden, leerkromme. Meest gebruikt voor budget en variantieanalyse. Historische (gemiddelde) standaard: gemiddelde van werkelijke kost vorig jaar — sluit weinig motiverende kracht in want bevestigt bestaande inefficiëntie. De keuze van de standaard bepaalt de interpretatie van varianties.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Componenten van een standaardkost per eenheid

Elke standaardkost-component bestaat uit hoeveelheid × prijs: (1) Grondstof: standaardverbruik (kg, liter, stuks) × standaardprijs (EUR/eenheid grondstof); (2) Productie-arbeid: standaarduren × standaardloontarief; (3) Variabele overhead: standaarduren-driver × standaardtarief per uur; (4) Vaste overhead: standaarduren × standaardvast-overhead-tarief gebaseerd op normale capaciteit. Een tafel-standaardkost zou bv. zijn: 2 kg hout × 50 + 1 u arbeid × 30 + 1 u × 20 variabele OH + 1 u × 40 vaste OH = 190 EUR.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Boekingsflow — werkelijk vs standaard

Productie wordt geboekt aan standaardkost; werkelijke kosten worden parallel verzameld op aparte rekeningen. Het verschil = totale variantie. De totale variantie wordt opgesplitst per oorzaak (prijs versus hoeveelheid, per kostencategorie). Aan het einde van de periode worden de varianties geanalyseerd, gerapporteerd aan de verantwoordelijke managers en weggewerkt — typisch direct in resultaat (klasse 6 of 7) of bij significante afwijkingen pro-rata herverdeeld over voorraad + verkoop.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 👣 Periodieke herziening van standaarden

Standaarden verouderen — door technologische verbetering, prijsstijgingen, leerkromme, organisatie-wijzigingen. Vuistregel: jaarlijkse herziening met grondige update om de 2-3 jaar (rolling-revision). Een standaard die ouder is dan 5 jaar levert systematisch negatieve prijsvarianties op (inflatie) en wordt motiverend nutteloos.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Zelena Bio NV — standaardkost tafel + variantie
> _Standaardkost per tafel: 100 EUR grondstof (2 kg × 50 EUR) + 30 EUR arbeid (1 u × 30 EUR) + 60 EUR overhead = 190 EUR. In maart 100 tafels geproduceerd. Werkelijk verbruikt: 220 kg hout aan 52 EUR/kg (= 11.440 EUR); 105 uren arbeid aan 31 EUR/u (= 3.255 EUR); 6.500 EUR overhead._
>
> **🧮 Variantie-decompositie grondstof**
>
> - Standaardgebruik = 100 tafels × 2 kg = 200 kg
> - Werkelijk gebruik = 220 kg → hoeveelheidsvariantie (HV) = (220 − 200) × 50 = +1.000 EUR ongunstig (productie-verantwoordelijk)
> - Standaardprijs = 50 EUR/kg; werkelijke prijs = 52 EUR/kg → prijsvariantie (PV) = 220 × (52 − 50) = +440 EUR ongunstig (inkoop-verantwoordelijk)
> - Totale grondstof-variantie = 1.000 + 440 = +1.440 EUR ongunstig
> - Verificatie: werkelijke kost 11.440 − standaardkost 10.000 = 1.440 ✓
>
> **🧮 Variantie-decompositie arbeid**
>
> - Standaarduren = 100 tafels × 1 u = 100 u
> - Werkelijke uren = 105 u → efficiency-variantie = (105 − 100) × 30 = +150 EUR ongunstig
> - Standaardloon = 30 EUR/u; werkelijk loon = 31 EUR/u → loontarief-variantie = 105 × (31 − 30) = +105 EUR ongunstig
> - Totale arbeids-variantie = +255 EUR ongunstig
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Variantie altijd in resultaat schrijven, ongeacht materialiteit
> **Verkeerde assumptie**: Alle varianties worden zonder uitzondering in klasse 6 of 7 geboekt.
>
> **Kernpunt**: Bij significante varianties (materieel ten opzichte van werkelijk geproduceerde kost) vereist IAS 2 dat de varianties pro-rata herverdeeld worden over de verkochte goederen én de eindvoorraad. Anders zou de stockwaardering niet de werkelijke kost weerspiegelen, wat IAS 2 schendt. Vuistregel: variantie < 5% van standaardkost → direct in resultaat; > 5% → herverdelen.
>
> <small>📖 Verordening (EU) 2023/1803 — geconsolideerde IFRS — IAS 2.10-13 — _richtlijn_</small>

> [!warning]- Ideale standaard gebruiken voor variantieanalyse
> **Verkeerde assumptie**: Een uitdagende ideale standaard motiveert de organisatie meer.
>
> **Kernpunt**: Een ideale standaard genereert systematisch ongunstige varianties — wat de variantieanalyse onbruikbaar maakt voor sturing (alles is rood, niets staat eruit). Voor sturing gebruik je een haalbare standaard zodat varianties betekenisvol zijn. De ideale standaard kan parallel als 'stretch goal' meeleven, maar niet als basis voor de operationele rapportering.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Implementatie standaardkosten bij productie-cliente

_Productie-cliente wil overschakelen van werkelijke-kost-systeem naar standaardkostenmethode._

#### 🧭 Adviseur

##### 👣 Standaarden vastleggen — samen met productie en inkoop

Standaarden niet in het kantoor maken — samen met productie-managers (verbruik, uren) en inkoop (prijzen) vastleggen. Anders mist de cliente buy-in en worden varianties betwist. Vastleggen op basis van historische data van 6-12 maanden + correctie voor verwachte verbeteringen of prijsschommelingen. Halfjaarlijkse review eerste jaar; daarna jaarlijks.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Kostprijsmethoden Σ-keuze-kader → [[kostprijsmethoden]] _(moet-verwijzen)_
- ↪ Variantieanalyse (toepassings-cross) → [[variantieanalyse]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[kostprijsmethoden]]
### `triggert`
- [[variantieanalyse]] — Variantieanalyse is de logische opvolger van standaardkostenmethode — zonder variantieanalyse heeft het werken met standaarden geen sturend nut.
