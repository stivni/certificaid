---
title: Vermogensmutatiemethode (equity method)
tags:
- concept
- methode
- po-1-4
linked_anchors:
- 1.4.I.E
- 1.4.I.D
- 1.4.I.G
- 1.4.II.C
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: grounded
node_type: methode
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/vermogensmutatiemethode.json
gegenereerd_op: '2026-05-16'
---
# Vermogensmutatiemethode (equity method) ⚖️

> Een deelneming verschijnt in de geconsolideerde jaarrekening niet activum-per-activum, maar als één samengevatte balanspost. Bij de eerste opname waardeer je die post aan jouw pro-rata aandeel in het eigen vermogen van de andere onderneming op de datum van aankoop. Daarna pas je die boekwaarde elk boekjaar aan met jouw aandeel in het resultaat en in directe wijzigingen van het eigen vermogen. Je gebruikt deze methode voor (a) geassocieerde ondernemingen (invloed van betekenis, geen controle), (b) gemeenschappelijke dochters waarvan de activiteit niet nauw geïntegreerd is in die van de moeder, en (c) dochters die uit de consolidatie zijn gelaten op grond van KB WVV art. 3:98 of art. 3:99.
>
> _Bron: KB WVV art. 3:142 jo. art. 3:141 — 3:145_


> [!summary] Korte definitie
> Een deelneming verschijnt in de geconsolideerde jaarrekening niet activum-per-activum, maar als één samengevatte balanspost.

> [!info] Behoort tot: [[consolidatiemethodes-vergelijking]]
> [!info] Bestaat uit: [[consolidatieverschil]]
## Bouwstenen

### Eerste consolidatie — vervang aankoopwaarde door pro-rata EV ⚖️

Bij eerste opname vervang je de aankoopwaarde van de deelneming door jouw pro-rata aandeel in het eigen vermogen van de andere vennootschap (inclusief resultaat van het boekjaar). Een eventueel verschil reken je toe aan onder- of overgewaardeerde bezittingen of schulden; het residu boek je als 'Consolidatieverschillen' (positief of negatief) en je schrijft het positieve verschil af.

**Waarom?** Op de enkelvoudige balans van de moeder staat de deelneming aan historische kostprijs — een 'dood' getal. De vermogensmutatie maakt de deelneming levend door haar aan jouw effectieve aandeel in EV te koppelen, zodat de geconsolideerde jaarrekening een eerlijker beeld geeft.

**Voorbeeld**: Antwerpse Investments NV koopt 25 % van Drukkerij Dendermonde BV voor 200; EV Drukkerij = 600 → vervang 200 (aankoopwaarde) door 25 % × 600 = 150 + 50 consolidatieverschil. Boekwaarde 'Vennootschappen waarop vermogensmutatie is toegepast' = 150; positief consolidatieverschil 50 wordt apart bijgehouden en afgeschreven.

_Grondslag: CBN 2022/11 — Eerste consolidatie_

### Latere consolidaties — beweeg mee met EV-wijzigingen ⚖️

Elk volgend boekjaar pas je de boekwaarde van de deelneming aan met jouw pro-rata aandeel in: (a) het resultaat van de andere vennootschap, exclusief het deel dat als dividend wordt uitgekeerd (dat dividend boek je apart als financiële opbrengst); (b) directe wijzigingen binnen het eigen vermogen (herwaarderingsmeerwaarde, kapitaalsubsidie, omrekeningsverschillen).

**Waarom?** De deelneming-post moet meebewegen met wat economisch gebeurt in de andere vennootschap. Anders blijft de balanspost statisch en verdwijnt het didactische voordeel van de methode.

**Voorbeeld**: Drukkerij Dendermonde BV maakt in jaar 1 winst van 100, keert geen dividend uit → Antwerpse boekt 25 % × 100 = 25 als 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast'; 'Vennootschappen waarop vermogensmutatie is toegepast' stijgt met 25 (150 → 175).

_Grondslag: KB WVV art. 3:143_

### Presentatie op de balans — één lijn ⚖️

De deelneming verschijnt in de geconsolideerde balans onder een afzonderlijke post van de financiële vaste activa met naam 'Vennootschappen waarop vermogensmutatie is toegepast'.

**Waarom?** Door één duidelijk gelabelde lijn weet de lezer dat het hier niet om een gewone deelneming gaat maar om een geassocieerde of niet-geïntegreerde gemeenschappelijke dochter — andere economische realiteit dan een 100 %-dochter.

**Voorbeeld**: Op de geconsolideerde balans van Antwerpse Investments NV staat 'Vennootschappen waarop vermogensmutatie is toegepast' 175 (voor Drukkerij Dendermonde) als aparte post bij de financiële vaste activa.

_Grondslag: KB WVV art. 3:141_

### Presentatie op de resultatenrekening — afzonderlijke post ⚖️

Jouw aandeel in het resultaat van de andere vennootschap komt in de geconsolideerde resultatenrekening als afzonderlijke post 'Aandeel in het resultaat van de vennootschappen waarop vermogensmutatie is toegepast'.

**Waarom?** Zo blijft het zichtbaar dat dit resultaat niet uit de eigen activiteit komt maar uit jouw aandeel in een andere vennootschap — anders zou het vermengd raken met de gewone bedrijfsresultaten en het beeld vertroebelen.

**Voorbeeld**: Aandeel Antwerpse Investments NV in het resultaat van Drukkerij Dendermonde BV in jaar 1: 25 → afzonderlijke regel op de geconsolideerde resultatenrekening (positief).

_Grondslag: KB WVV art. 3:145_


## Berekening

### Eerste consolidatie — herwaardering en consolidatieverschil

**Pro-rata aandeel in eigen vermogen (eerste consolidatie)** 
```
pro-rata aandeel EV = belangenpercentage × eigen vermogen geassocieerde op aankoopdatum
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage` | Aandeel van moeder in kapitaal geassocieerde (zie [[belangenpercentage]]) | % |
| `eigen vermogen geassocieerde op aankoopdatum` | Kapitaal + reserves + overgedragen resultaat + resultaat tot aankoopdatum | EUR |

**Voorbeeld-invulling**: belang Antwerpse Investments NV in Drukkerij Dendermonde BV = 25 %; EV Drukkerij = 600

```
25 % × 600 = 150
```

_Resultaat in EUR_
**Consolidatieverschil (eerste consolidatie vermogensmutatie)** (volgt op: eerste-consolidatie-vm-pro-rata-ev)
```
consolidatieverschil = aankoopwaarde − pro-rata aandeel EV − toerekening aan stille meer-/minderwaarden
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `aankoopwaarde` | Wat de moeder betaalde voor de aandelen | EUR |
| `pro-rata aandeel EV` | Resultaat van vorige formule | EUR |
| `toerekening aan stille meer-/minderwaarden` | Som van bedragen toegerekend aan onder-/overgewaardeerde posten van de geassocieerde | EUR |

**Voorbeeld-invulling**: aankoopwaarde = 200; pro-rata aandeel EV = 150; toerekening = 0

```
200 − 150 − 0 = 50 (positief)
```

_Resultaat in EUR_
*Bij verwerving betaalt de moeder vaak een prijs die afwijkt van haar pro-rata aandeel in het netto-actief van de geassocieerde. Dat verschil reken je eerst toe aan onder- of overgewaardeerde posten van de geassocieerde; pas daarna boek je het residu als 'Consolidatieverschil'.*

### . 

**Voorbeeld**: Antwerpse Investments NV koopt in 20X1 een belang van 25 % in Drukkerij Dendermonde BV. Aankoopwaarde 200. Eigen vermogen Drukkerij op aankoopdatum: 600.

```
Pro-rata aandeel in EV op aankoopdatum = 25 % × 600 = 150.
Verschil = 200 − 150 = 50 (positief).
Geen onder-/overwaarderingen aangewezen → het volledige verschil van 50 wordt geboekt als positief consolidatieverschil.
Boeking: 'Vennootschappen waarop vermogensmutatie is toegepast' (balans) +150; 'Positief consolidatieverschil' (balans) +50; tegenpost: 'Deelnemingen' −200.
```

Resultaat: Eerste consolidatie: deelneming wordt voorgesteld als 'Vennootschappen waarop vermogensmutatie is toegepast' voor 150 + 'Positief consolidatieverschil' 50 — som 200 (gelijk aan aankoopwaarde). Positief consolidatieverschil wordt afgeschreven over bv. 5 jaar = 10/jaar in de geconsolideerde resultatenrekening (afzonderlijke post bij bedrijfs- of financiële kosten — KB WVV art. 3:131).
### Latere consolidatie — pro-rata aandeel in resultaat

**Pro-rata aandeel in resultaat (latere consolidatie)** 
```
Δ boekwaarde = belangenpercentage × (resultaat boekjaar − uitgekeerd dividend) + belangenpercentage × directe EV-mutaties
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage` | Aandeel van moeder in kapitaal geassocieerde | % |
| `resultaat boekjaar` | Winst of verlies van de geassocieerde in het lopende boekjaar | EUR |
| `uitgekeerd dividend` | Deel van het resultaat dat door de geassocieerde als dividend wordt uitgekeerd (wordt apart geboekt als financiële opbrengst) | EUR |
| `directe EV-mutaties` | Wijzigingen in eigen vermogen buiten het resultaat om (herwaarderingsmeerwaarde, kapitaalsubsidie, omrekeningsverschillen) | EUR |

**Voorbeeld-invulling**: belang Antwerpse = 25 %; resultaat Drukkerij = 1.500; geen dividend; geen directe EV-mutaties

```
25 % × (1.500 − 0) + 25 % × 0 = 375
```

_Resultaat in EUR_
**Verliesgrens bij vermogensmutatie** 
```
doorgeboekt verlies = min(belangenpercentage × verlies geassocieerde, huidige boekwaarde deelneming)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage × verlies geassocieerde` | Pro-rata aandeel in het verlies | EUR |
| `huidige boekwaarde deelneming` | Boekwaarde 'Vennootschappen waarop vermogensmutatie is toegepast' vóór deze verlies-verwerking | EUR |

**Voorbeeld-invulling**: verlies Drukkerij = 7.000; belang Antwerpse = 25 %; huidige boekwaarde = 150

```
min(25 % × 7.000 = 1.750; 150) = 150
```

_Resultaat in EUR_
*Het pro-rata aandeel in winst of verlies van de geassocieerde verandert direct de boekwaarde van de deelneming op de geconsolideerde balans, met een tegenpost als afzonderlijke regel 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast' in de geconsolideerde resultatenrekening.*

### . 

**Voorbeeld**: Geassocieerde Drukkerij Dendermonde BV; belang van Antwerpse Investments NV = 25 %. Boekwaarde deelneming bij eerste consolidatie was 150 + 50 consolidatieverschil = totaal 200. Hypothese 1: Drukkerij maakt in 20X2 winst van 1.500. Hypothese 2: Drukkerij maakt verlies van 1.500. Hypothese 3: Drukkerij maakt verlies van 7.000 (groter dan boekwaarde 150).

```
Hypothese 1: 25 % × 1.500 = +375 — verhoging boekwaarde 'Vennootschappen waarop vermogensmutatie is toegepast' (150 → 525) + opname 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast' = 375.
Hypothese 2: 25 % × (−1.500) = −375 — verlaging boekwaarde (150 → niet onder 0, dus reductie tot 0 met 150) + 'Aandeel in het verlies …' van −150 (beperkt). De rest 225 wordt niet doorgeboekt tenzij er een aanvullende verplichting is.
Hypothese 3: 25 % × (−7.000) = −1.750 — boekwaarde gaat naar 0 (was 150); verlies in resultatenrekening 150 (niet 1.750). Resterend 1.600 niet doorgeboekt.
```

Resultaat: Hypothese 1: boekwaarde +375 → 525; resultaat verbetert met 375. Hypothese 2 & 3: boekwaarde wordt afgeboekt tot nul; aandeel in verlies in resultatenrekening beperkt tot 150 (oorspronkelijke boekwaarde) — overige verlies wordt niet doorgeboekt zolang geen verplichting bestaat (CBN 2022/11, hypothese 3).

## In de praktijk

### Eliminatie van intra-groepswinsten {id="eliminatie-van-intra-groepswinsten"}

Resultaten van verrichtingen tussen de moeder (of haar dochters) en de vennootschap waarop vermogensmutatie wordt toegepast, die nog in de waardering van een actief zitten, worden uit het 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast' geweerd voor het pro-rata aandeel — zowel bij upstream als downstream sales. ⚖️

### Geen vrijstelling van consolidatie {id="geen-vrijstelling-van-consolidatie"}

Het opnemen van een vennootschap via de vermogensmutatiemethode (in plaats van integraal of evenredig) geeft de groep géén vrijstelling van haar consolidatieplicht. De moeder blijft consolidatieplichtig zolang ze een dochter heeft. ⚖️

### Verkoop van de deelneming {id="verkoop-van-de-deelneming"}

Bij verkoop boek je het verschil tussen verkoopprijs en boekwaarde (op vermogensmutatie-basis, inclusief mutaties tot verkoopdatum) als meer- of minderwaarde in de geconsolideerde resultatenrekening. Een resterend positief consolidatieverschil wordt mee afgeboekt. ⚖️


<details>
<summary><strong>Niet verwarren met</strong> (2 vergelijkingen)</summary>

- **vs [[integrale-consolidatie]]** — Vermogensmutatie behoudt de deelneming als één balanspost; integrale consolidatie neemt de bezittingen en schulden regel voor regel op (en zondert de derden af).
  - _Trigger_: Soort relatie: controle → integraal; invloed van betekenis (of uitgesloten dochters / niet-geïntegreerde gemeenschappelijke dochters) → vermogensmutatie.
- **vs [[evenredige-consolidatie]]** — Evenredig neemt bezittingen en schulden pro-rata op (regel voor regel). Vermogensmutatie houdt de deelneming als één post 'Vennootschappen waarop vermogensmutatie is toegepast'. Evenredig is de regel voor gemeenschappelijke dochters; vermogensmutatie de uitzondering bij gebrek aan integratie.
  - _Trigger_: Mate van integratie van de gemeenschappelijke dochter: nauw geïntegreerd → evenredig; los → vermogensmutatie.

</details>


## Valkuilen

- ⚠️ Het pro-rata aandeel in een verlies kan de boekwaarde van de deelneming nooit onder nul brengen. Verdere verliezen worden niet doorgeboekt zolang er geen aanvullende verplichting (bv. borg, garantie) bestaat (CBN 2022/11, hypothese 3). ⚖️
- ⚠️ Een dividend dat de geassocieerde uitkeert vermindert haar eigen vermogen — maar wordt in de jaarrekening van de moeder geboekt als financiële opbrengst (zonder voor een tweede maal als 'aandeel in resultaat' te worden geteld). De vermogensmutatie corrigeert dat: het resultaat-aandeel wordt berekend exclusief het deel dat als dividend wordt uitgekeerd. ⚖️
- ⚠️ Wijzigingen in het eigen vermogen van de geassocieerde buiten het resultaat om (herwaarderingsmeerwaarde, kapitaalsubsidie, omrekeningsverschillen) moeten óók in de vermogensmutatie worden meegenomen — niet alleen het resultaat. Dit was vroeger een onderbelicht punt; CBN 2014/3 verduidelijkte het en CBN 2022/11 codificeerde de werkwijze. ⚖️

## Zie ook

- **Getriggerd door**: [[invloed-van-betekenis]]

## Bronnen

[^1]: `CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied`
[^2]: `CBN-2022-11-vermogensmutatiemethode__sec_eerste-consolidatie`
[^3]: `KB-WVV-2019__art_3_113`
[^4]: `KB-WVV-2019__art_3_115`
[^5]: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_inleiding`
[^6]: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking`
[^7]: `KB-WVV-2019__art_3_78`
[^8]: `KB-WVV-2019__art_3_77`
[^9]: `CBN-2022-11-vermogensmutatiemethode__sec_voorbeeld`
[^10]: `CBN-2022-11-vermogensmutatiemethode__sec_latere-consolidaties`
[^11]: `CBN-2014-03-de-boekhoudkundige-verwerking-van-mutaties-binnen-het-eigen-vermogen-van-een-geassocieerde__sec_inleiding`
[^12]: `KB-WVV-2019__art_3_112`
[^13]: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_voorbeeld-1`
[^14]: `CBN-2022-11-vermogensmutatiemethode__sec_herberekening-van-het-bedrag-van-de-deelneming-waarop-de-ver`
[^15]: `CBN-2022-11-vermogensmutatiemethode__sec_herberekening-van-het-bedrag-van-de-deelneming-waarop-de-ver_2`
[^16]: `CBN-2022-11-vermogensmutatiemethode__sec_herberekening-van-het-bedrag-van-de-deelneming-waarop-de-ver_3`
[^17]: `CBN-2022-11-vermogensmutatiemethode__sec_intra-groepsverkopen-upstream-downstream-sales`
[^18]: `CBN-2022-11-vermogensmutatiemethode__sec_toepassing-van-de-vermogensmutatiemethode`
[^19]: `CBN-2022-11-vermogensmutatiemethode__sec_voorbeeld-2-verkoop-van-de-deelnemingen-waarop-vermogensmuta`
[^20]: `CBN-2022-11-vermogensmutatiemethode__sec_directe-mutaties-binnen-het-eigen-vermogen-van-de-geassociee`
