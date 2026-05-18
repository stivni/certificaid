---
title: Direct costing (gedeeltelijke kostencalculatie)
tags:
- concept
- cluster
- po-1-8
linked_anchors:
- 1.8.III.B
- 1.8.III
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/direct-costing.json
gegenereerd_op: '2026-05-18'
---
# Direct costing (gedeeltelijke kostencalculatie) 🤖

> [!update] Bijgewerkt sinds `b2f4a4ad` — laatste wijziging 2026-05-18


Direct costing (synoniem: variable costing, gedeeltelijke kostencalculatie) berekent een kostprijs die enkel directe en variabele kosten omvat. Vaste indirecte kosten worden niet op de kostendrager toegerekend maar direct als periodekost in de resultatenrekening geboekt. Doel: transparante zicht op variabele kostengedrag en contributiemarge per product — input voor break-even-analyse, prijsbeslissingen en make-or-buy.

> [!info] Behoort tot: [[costing-methodes-vergelijking]]

> [!info] Bestaat uit (2): [[break-even-analyse]] · [[contributiemarge]]


## Bouwstenen

### Enkel variabele kosten in kostprijs ⚖️

Materiaal, directe arbeid (mits stukloon of variabel uurtarief), variabele machine-kost, variabele indirecte productiekosten (energie) gaan in de kostprijs. Vaste kosten (huur, afschrijvingen, vaste lonen) gaan rechtstreeks naar RR als periode-last.

**Waarom?** Periodewinst weerspiegelt het verkochte volume zonder verstorend effect van veranderende voorraad-waardering.



Yperse Werkplaats BV — direct costing voor partij tapijten: materiaal € 12.000 + variabele arbeid € 4.500 + variabele energie € 500 = € 17.000 kostprijs. De € 3.500 vaste indirecte kost van de Weverij gaat meteen in de RR als periode-last.

_Grondslag: CBN 2012/15_

### Wettelijke toelaatbaarheid ⚖️

Direct costing is in België toegelaten voor voorraadwaardering, op voorwaarde dat de keuze in de waarderingsregels wordt vastgelegd en consistent wordt toegepast. CBN-advies 2012/15 bevestigt dit voor bestellingen in uitvoering.

**Waarom?** Belgisch boekhoudrecht laat keuze tussen full en direct, mits transparantie in toelichting.



Yperse Werkplaats BV vermeldt in de toelichting bij de jaarrekening: 'Voorraden gereed product worden gewaardeerd aan de directe vervaardigingskost (direct costing). Vaste indirecte productiekosten worden in de periode waarin ze ontstaan als kost erkend.'

_Grondslag: CBN 2012/15_

### Impact op periodewinst 🤖

Bij groei (productie > verkoop, voorraad stijgt): direct costing rapporteert lagere winst dan full costing, want vaste kosten worden niet meegeschoven in stijgende voorraad. Bij krimp (verkoop > productie): omgekeerd effect.

**Waarom?** Direct costing dwingt management om vaste kosten elk jaar te verantwoorden in de RR.



Yperse Werkplaats BV in groeijaar: productie 12.000 tapijten, verkoop 10.000. Vaste indirecte productiekost € 800.000. Bij full costing: € 800.000 / 12.000 = € 66,67/stuk; verkocht: 10.000 × € 66,67 = € 666.700 in COGS; voorraad neemt € 133.300 vaste kost mee. Bij direct costing: volledige € 800.000 in RR; voorraad-impact: nul.



## In de praktijk

<h3 id="gebruik-voor-interne-sturing">Gebruik voor interne sturing</h3>

> [!tip]- Gebruik voor interne sturing
> Voor break-even, marge-analyse, beslissingen over extra-orders is direct costing de aangewezen aanpak. De contributiemarge (verkoopprijs − variabele kost) toont onmiddellijk hoeveel een extra-eenheid bijdraagt aan dekking van vaste kosten en winst. 🤖

> [!tip]- Herkennen op het examen
> Vragen over 'minimum verkoopprijs' of 'extra-order al dan niet aannemen' → direct costing.


> [!info]- Niet verwarren met [[volledige-kostencalculatie]]
> Volledige kostencalculatie (full costing) → alle productie-indirect mee in kostprijs; voorraad bevat vaste kosten. Direct costing → enkel variabel mee; vaste kost is periode-last; contributiemarge zichtbaar.
>
> _Trigger_: Examen-vraag: bij voorraadwaardering = full costing standaard; bij break-even of beslissingen = direct costing standaard.


## Valkuilen

> [!warning]- Direct costing voor voorraadwaardering geeft een lagere voorraad
> ⚠️ Direct costing voor voorraadwaardering geeft een lagere voorraad. Banken die balansratio's bekijken (current ratio, working capital) zien een lager getal. Wie van methode wisselt zonder uitleg veroorzaakt jaarrekeningvergelijkbaarheid-issues. 🤖



## Zie ook

- **Vereist kennis van**: [[contributiemarge]]
- **Wordt voorondersteld in** (1): [[variabele-kosten]]
## Bronnen

[^1]: `CBN-2012-15-bestellingen-in-uitvoering__sec_waarderingsaspecten-n-a-v-de-toepassing-van-direct-costing`
