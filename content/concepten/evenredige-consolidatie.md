---
title: Evenredige consolidatie (proportionele consolidatie)
tags:
- concept
- methode
- po-1-4
linked_anchors:
- 1.4.I.D
- 1.4.I.B
- 1.4.II.C
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: grounded
node_type: methode
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/evenredige-consolidatie.json
gegenereerd_op: '2026-05-16'
---
# Evenredige consolidatie (proportionele consolidatie) ⚖️

> Een gemeenschappelijke dochter (een vennootschap die door een beperkt aantal vennoten samen wordt gecontroleerd, op grond van een overeenkomst) neem je in de geconsolideerde jaarrekening van elke gezamenlijk controlerende moeder op naar rato van haar aandeel in het kapitaal (of in de inbreng bij vennootschappen zonder kapitaal). Alleen jouw pro-rata stuk van de bezittingen, schulden, opbrengsten en kosten komt erin — geen afzonderlijke 'belangen van derden' nodig, want het deel buiten de groep wordt simpelweg niet opgenomen.
>
> _Bron: KB WVV art. 3:124, 2° jo. art. 3:140_


> [!summary] Korte definitie
> Een gemeenschappelijke dochter (een vennootschap die door een beperkt aantal vennoten samen wordt gecontroleerd, op grond van een overeenkomst) neem je in de geconsolideerde jaarrekening van elke gezamenlijk controlerende moeder op naar rato van haar aandeel in het kapitaal (of in de inbreng bij vennootschappen zonder kapitaal).

> [!info] Behoort tot: [[consolidatiemethodes-vergelijking]]
> [!info] Bestaat uit: [[intragroep-eliminaties]]
## Bouwstenen

### Pro-rata opname ⚖️

Neem elke bezitting, schuld, opbrengst en kost van de gemeenschappelijke dochter op naar rato van jouw aandeel in het kapitaal (of in de inbreng bij vennootschappen zonder kapitaal).

**Waarom?** Je deelt de macht over deze dochter met andere vennoten; je hebt geen 100 %-zeggenschap. De geconsolideerde jaarrekening reflecteert die gedeelde macht door alleen jouw stuk te tonen.

**Voorbeeld**: Cardinal Group NV bezit 50 % van Filmstudio Florence BV (gezamenlijke controle). Filmstudio Florence heeft 800 vaste activa → Cardinal neemt 50 % × 800 = 400 op in haar geconsolideerde balans.

_Grondslag: KB WVV art. 3:140, b_

### Integrale-consolidatie-regels gelden, maar op het pro-rata stuk ⚖️

Op het opgenomen pro-rata deel pas je alle technieken van integrale consolidatie toe: schrappen van de deelneming (KB WVV art. 3:127, a), toerekening van verschillen (art. 3:128 jo. 3:130), boeken van consolidatieverschil (art. 3:130) met afschrijving (art. 3:131), gedeeltelijke realisatie (art. 3:132–3:133) en eliminatie van onderlinge posten (art. 3:134, 3:136, 3:139). Het verschil: alles wat 100 % was bij integrale consolidatie, gebeurt nu pro-rata.

**Waarom?** Door dezelfde technieken op een kleinere schaal toe te passen behoud je consistentie binnen de geconsolideerde jaarrekening — een goodwill bij een gemeenschappelijke dochter werkt boekhoudkundig op dezelfde manier als bij een gewone dochter, alleen voor jouw deel.

**Voorbeeld**: Cardinal koopt haar 50 %-belang in Filmstudio Florence voor 300; pro-rata EV Filmstudio op aankoopdatum = 250 → bruto-verschil 50 op pro-rata basis, eventueel toe te rekenen aan stille meerwaarden in Filmstudio's apparatuur.

_Grondslag: KB WVV art. 3:140, a_

### Geen 'Belangen van derden'-post 🤖

Bij evenredige consolidatie verschijnt er geen post 'Belangen van derden' of 'Aandeel van derden in het resultaat'. Het deel buiten je groep neem je gewoon niet op — er valt dus niets af te zonderen.

**Waarom?** Bij integrale consolidatie zit 100 % van de dochter in de geconsolideerde balans, en moet de niet-moeder-fractie zichtbaar worden gemaakt. Bij evenredige consolidatie zit alleen jouw stuk er al in — het deel van de andere vennoten verschijnt nooit; daarom geen derden-correctie nodig.

**Voorbeeld**: Cardinal neemt 50 % van Filmstudio Florence op; Energiehuis Evergem neemt de andere 50 % op in haar eigen geconsolideerde jaarrekening. Geen 'Belangen van derden' aan beide zijden.

_Grondslag: KB WVV art. 3:140 (geen verwijzing naar KB WVV art. 3:137)_


## Berekening

### Evenredige consolidatie — pro-rata opname

**Pro-rata opname van een post** 
```
geconsolideerde post = post moeder + (post gemeenschappelijke dochter × belangenpercentage) − pro-rata intragroep-eliminaties
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `post moeder` | Bedrag van de post bij de moeder (en eventueel integraal geconsolideerde dochters) | EUR |
| `post gemeenschappelijke dochter` | 100 %-bedrag van dezelfde post bij de gemeenschappelijke dochter | EUR |
| `belangenpercentage` | Aandeel van moeder en haar groep in het kapitaal van de gemeenschappelijke dochter | % |
| `pro-rata intragroep-eliminaties` | Onderlinge transacties × belangenpercentage | EUR |

**Voorbeeld-invulling**: Cardinal-vaste activa = 500; Filmstudio Florence-vaste activa = 800; belang Cardinal in Filmstudio = 50 %; geen intragroep op deze post

```
500 + (800 × 50 %) − 0 = 500 + 400 = 900
```

_Resultaat in EUR_
**Eliminatie intra-groepsverkoop (op pro-rata basis)** 
```
te elimineren winst = nog-niet-gerealiseerde winst op intra-groepsverkoop × belangenpercentage
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `nog-niet-gerealiseerde winst op intra-groepsverkoop` | Winstmarge die de dochter op een interne verkoop heeft gerealiseerd, voor zover de goederen nog in voorraad zitten bij de koper binnen de groep | EUR |
| `belangenpercentage` | Aandeel van moeder in kapitaal gemeenschappelijke dochter | % |

**Voorbeeld-invulling**: winst op intra-groepsverkoop Filmstudio aan Cardinal = 10 (nog in voorraad); belang Cardinal = 50 %

```
10 × 50 % = 5
```

_Resultaat in EUR_
*Bij gezamenlijke controle deel je de zeggenschap met andere vennoten. De geconsolideerde jaarrekening laat dat zien door alleen jouw deel van bezittingen, schulden, opbrengsten en kosten op te nemen. Het deel buiten de groep verschijnt niet — er is dus geen derden-post zoals bij integrale consolidatie.*

### . 

**Voorbeeld**: Cardinal Group NV en Energiehuis Evergem BV oefenen gezamenlijke controle uit over Filmstudio Florence BV via een aandeelhoudersovereenkomst — elk bezit 50 % van het kapitaal. Balans Filmstudio Florence: vaste activa 800, voorraden 200, kas 100; eigen vermogen 600, schulden 500. Resultatenrekening: omzet 1.000, kosten 800, resultaat 200. Cardinal koopt voor 60 goederen bij Filmstudio (intra-groepsverkoop, nog in voorraad bij Cardinal; Filmstudio realiseerde daarop 10 winst).

```
Pro-rata deel van Cardinal in Filmstudio = 50 %.
Geconsolideerde activa van Filmstudio (vóór eliminatie): 50 % × (800 + 200 + 100) = 50 % × 1.100 = 550. Geconsolideerde schulden van Filmstudio: 50 % × 500 = 250. Geconsolideerd eigen vermogen van Filmstudio: 50 % × 600 = 300.
Geconsolideerde omzet uit Filmstudio: 50 % × 1.000 = 500. Geconsolideerde kosten uit Filmstudio: 50 % × 800 = 400. Geconsolideerd resultaat uit Filmstudio (vóór eliminatie): 50 % × 200 = 100.
Intra-groepselimatie (KB WVV art. 3:140 jo. art. 3:134, op pro-rata deel): de winst op de intra-groepsverkoop wordt geëlimineerd voor 50 % × 10 = 5. Geconsolideerde voorraden Cardinal verminderen met 5; geconsolideerd resultaat vermindert met 5.
```

Resultaat: In de geconsolideerde balans van Cardinal verschijnen 550 activa en 250 schulden uit Filmstudio (na intra-groep-eliminatie 545 activa); van het resultaat 200 wordt 100 meegenomen, verminderd met 5 → 95 in het geconsolideerd resultaat. Er is géén post 'Aandeel van derden in resultaat' — de andere 50 % van Filmstudio komt niet voor in Cardinal's geconsolideerde jaarrekening (Energiehuis Evergem doet dezelfde oefening met haar eigen 50 %).

## In de praktijk

### Wanneer toepassen {id="wanneer-toepassen"}

Standaard voor gemeenschappelijke dochters bij gezamenlijke controle. Uitzondering: gemeenschappelijke dochters die niet nauw geïntegreerd zijn in de activiteit van de moeder mogen via vermogensmutatie worden verwerkt (CBN 2013/3). ⚖️

**Herkenningspunt**: Gezamenlijke controle (overeenkomst, vetorecht) + integratie → evenredige consolidatie.


<details>
<summary><strong>Niet verwarren met</strong> (2 vergelijkingen)</summary>

- **vs [[integrale-consolidatie]]** — Integraal = 100 % opname met afzondering van derden-deel via 'Belangen van derden'. Evenredig = pro-rata opname (% kapitaaldeelname), geen derden-post.
  - _Trigger_: Soort controle bepaalt de methode: exclusieve controle → integraal; gezamenlijke controle → evenredig (of vermogensmutatie als niet-geïntegreerd).
- **vs [[vermogensmutatiemethode]]** — Evenredige consolidatie neemt bezittingen/schulden regel voor regel pro-rata op. Vermogensmutatie houdt de deelneming als één gesynthetiseerde post ('Vennootschappen waarop vermogensmutatie is toegepast'). Bij gezamenlijke controle van een niet-geïntegreerde dochter mag je kiezen voor vermogensmutatie.
  - _Trigger_: Mate van integratie van de gemeenschappelijke dochter in de groep — nauw geïntegreerd → evenredig; los → vermogensmutatie.

</details>


## Valkuilen

- ⚠️ Het opgenomen pro-rata deel volgt het belangenpercentage (kapitaal), niet het controlepercentage. Een 50/50-joint venture wordt voor 50 % opgenomen, ook al heeft elke vennoot via de overeenkomst eigenlijk een gelijke beleidsmacht (gedeelde 100 % controle). ⚖️
- ⚠️ Intra-groepsverkopen tussen moeder en gemeenschappelijke dochter worden geëlimineerd op het pro-rata deel — niet voor 100 %. Andere bronnen (oudere W.Venn., IFRS 11) kennen andere regels; in WVV-context geldt de pro-rata-eliminatie. 🤖

## Zie ook

- **Getriggerd door**: [[gezamenlijke-controle]]

## Bronnen

[^1]: `KB-WVV-2019__art_3_111`
[^2]: `KB-WVV-2019__art_3_110`
[^3]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen`
[^4]: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking`
[^5]: `KB-WVV-2019__art_3_108`
[^6]: `KB-WVV-2019__art_3_106`
[^7]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_voorbeeld-2`
[^8]: `KB-WVV-2019__art_3_98`
