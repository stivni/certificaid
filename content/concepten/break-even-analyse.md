---
title: Break-even-analyse
tags:
- concept
- cluster
- po-1-8
linked_anchors:
- 1.8.III.D
- 1.8.III
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/break-even-analyse.json
gegenereerd_op: '2026-05-18'
---
# Break-even-analyse 🤖

> [!update] Bijgewerkt sinds `b2f4a4ad` — laatste wijziging 2026-05-18


De break-even-analyse (kosten-volume-winst-analyse, CVP) berekent welke omzet of welk volume nodig is om alle vaste kosten te dekken — het punt waarop de onderneming geen verlies en geen winst maakt. Aan dat volume betekent elke extra eenheid winst; eronder wordt verlies geleden.

> [!info] Behoort tot: [[direct-costing]]


## Bouwstenen

### Werking van het break-even-punt 🤖

Bij volume nul: vaste kosten worden niet gedekt — totaal verlies = vaste kosten. Bij elke verkochte eenheid komt een contributiemarge binnen die een stukje vaste kost dekt. Het break-even-volume is het aantal eenheden waarbij de totale contributiemarge precies gelijk is aan de totale vaste kosten.

**Waarom?** Geeft een aanvoelpunt voor 'hoe groot moet ons bedrijf minimaal zijn om uit verlies te raken?'



Yperse Werkplaats BV heeft vaste kosten € 800.000/jaar en eenheidscontributie € 47 per tapijt. Break-even = € 800.000 / € 47 = 17.022 tapijten/jaar. Daaronder = verlies; daarboven = winst.


### In eenheden vs. in omzet 🤖

Break-even kan in stuks (vaste kost / eenheidscontributie) of in omzet (vaste kost / CM-ratio) worden uitgedrukt. Bij multi-product-mix is omzet-vorm handiger.

**Waarom?** Stuks helpt productie-planning; omzet helpt commercieel team.



Yperse Werkplaats BV — break-even in stuks: € 800.000 / € 47 = 17.022 tapijten. In omzet: € 800.000 / 78,3 % = € 1.021.711.


### Veiligheidsmarge 🤖

Verschil tussen verwachte verkoop en break-even, in % of in absolute eenheden. Een hoge veiligheidsmarge betekent dat de onderneming volume kan verliezen voordat ze in verlies komt.

**Waarom?** Risicoanalyse: hoe gevoelig is de onderneming voor volumedaling?



Yperse Werkplaats BV verwacht 22.000 tapijten te verkopen. Veiligheidsmarge = (22.000 − 17.022) / 22.000 = 22,6 %. Het volume mag met 22,6 % dalen voordat verlies optreedt.



## Berekening

### Break-even-berekening

**Break-even-volume (in eenheden)** (volgt op: eenheidscontributie)
```
BE-volume = vaste kosten / eenheidscontributie
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `vaste kosten` | Totale vaste kosten van de onderneming (productie + administratie + commercieel) | EUR |
| `eenheidscontributie` | Verkoopprijs − variabele kost per eenheid | EUR/stuk |

**Voorbeeld-invulling**: Yperse Werkplaats BV: vaste kosten € 800.000; eenheidscontributie € 47

```
€ 800.000 / € 47 = 17.021,3 → 17.022 stuks
```

_Resultaat in stuks_
**Break-even-omzet (in EUR)** (volgt op: contributiemarge-ratio)
```
BE-omzet = vaste kosten / CM-ratio
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `vaste kosten` | Totale vaste kosten | EUR |
| `CM-ratio` | Contributiemarge gedeeld door verkoopprijs | % |

**Voorbeeld-invulling**: Yperse: vaste kosten € 800.000; CM-ratio 78,3 %

```
€ 800.000 / 78,3 % = € 1.021.711
```

_Resultaat in EUR_
**Veiligheidsmarge** (volgt op: be-volume)
```
veiligheidsmarge = (verwachte verkoop − BE-volume) / verwachte verkoop
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `verwachte verkoop` | Geplande verkoop in eenheden of EUR | stuks of EUR |
| `BE-volume` | Break-even-volume in zelfde eenheid | stuks of EUR |

**Voorbeeld-invulling**: Yperse: verwacht 22.000 tapijten; BE = 17.022

```
(22.000 − 17.022) / 22.000 = 22,6 %
```

_Resultaat in %_
*Op het break-even-punt: totale opbrengsten = totale kosten. Equivalent: contributiemarge × volume = vaste kosten.*

### 1. Splits kosten in vast en variabel

Identificeer welke kosten meebewegen met volume (variabel) en welke constant blijven (vast). Semi-variabele kosten splitsen.

**🛠️ Hoe**:

Klassieke aanpak: variabel = directe materiaal, directe variabele arbeid, variabele energie. Vast = huur, afschrijving, vaste lonen, verzekering.

**Grondslag**: [[typologie-van-kosten]]

### 2. Bereken eenheidscontributie

Verkoopprijs per eenheid − variabele kost per eenheid.

**🛠️ Hoe**:

Zie [[contributiemarge]] §berekening.

**Grondslag**: [[contributiemarge]]

### 3. Bereken break-even-volume

Vaste kosten gedeeld door eenheidscontributie geeft het minimumvolume.

**🛠️ Hoe**:

1. Tel alle vaste kosten op (productie, administratie, commercieel — voor de onderneming als geheel).
2. Deel door eenheidscontributie.
3. Rond naar boven af (gedeeltelijk product = niet verkocht).


> [!example]- Voorbeeld: Yperse Werkplaats BV verkoopt tapijten aan € 60
> Yperse Werkplaats BV verkoopt tapijten aan € 60. Variabele kost per stuk € 13. Vaste kosten € 800.000/jaar.
>
> 1. **Eenheidscontributie** 🧮
>
>    eenheidscontributie = € 60 − € 13 = **€ 47/stuk**
>
> 2. **Break-even in stuks** 🧮
>
>    BE-volume = € 800.000 / € 47 = **17.022 tapijten** (afgerond naar boven)
>
> 3. **Break-even in omzet** 🧮
>
>    CM-ratio = € 47 / € 60 = 78,3 %
>    BE-omzet = € 800.000 / 78,3 % = **€ 1.021.711**
>    Controle: 17.022 × € 60 = € 1.021.320 (verschil door afronding)
>
> 4. **Controle: totale opbrengsten = totale kosten** 🧮
>
>    Bij 17.022 stuks:
>      Omzet            = 17.022 × € 60 =  **€ 1.021.320**
>      Variabele kost   = 17.022 × € 13 =  **€   221.286**
>      Vaste kost       =                  **€   800.000**
>      Totaal kost      =                  **€ 1.021.286**
>      Resultaat        =                  **€         34** (≈ 0; afrondingsverschil)
>

**Grondslag**: Vakdoctrine

**Voorbeeld**: Yperse Werkplaats BV, productlijn tapijten: verkoopprijs € 60; variabele kost € 13/stuk; vaste kosten € 800.000/jaar.

```
Eenheidscontributie = € 60 − € 13 = € 47. BE-volume = € 800.000 / € 47 = 17.022 stuks. BE-omzet = € 800.000 / 78,3 % = € 1.021.711.
```

Resultaat: Yperse moet jaarlijks minstens 17.022 tapijten verkopen om uit verlies te raken; daarboven levert elk stuk € 47 winst.

## In de praktijk

<h3 id="aannames">Aannames</h3>

> [!tip]- Aannames
> Break-even-analyse veronderstelt: (1) lineaire relatie tussen volume en kost/opbrengst, (2) verkoopprijs constant, (3) productmix constant, (4) vaste kosten constant binnen relevante range. Bij realiteit met staffelkortingen, capaciteitssprongen of mix-shift is de eenvoudige formule een benadering. 🤖

<h3 id="doelwinst-volume">Doelwinst-volume</h3>

> [!tip]- Doelwinst-volume
> Variant: hoeveel volume om een doelwinst W te halen? Formule: (vaste kosten + W) / eenheidscontributie. Bij Yperse, doelwinst € 200.000: (800.000 + 200.000) / 47 = 21.277 stuks. 🤖


## Valkuilen

> [!warning]- Vergeten dat 'vaste kosten' ook commerciële en administratieve overhead bevat — niet enkel productie-vaste-kosten
> ⚠️ Vergeten dat 'vaste kosten' ook commerciële en administratieve overhead bevat — niet enkel productie-vaste-kosten. Wie alleen productie-vaste-kosten in de teller stopt, krijgt een te optimistisch break-even-punt. 🤖


> [!warning]- Semi-variabele kosten (basis-abonnement + verbruik) eerst splitsen via high-low-methode of regressie
> ⚠️ Semi-variabele kosten (basis-abonnement + verbruik) eerst splitsen via high-low-methode of regressie. Een 'semi-variabele' kost volledig vast of volledig variabel rekenen vertekent de break-even met 10-20 %. 🤖


> [!warning]- Break-even-punt is een momentopname
> ⚠️ Break-even-punt is een momentopname. Bij sterk seizoensgebonden verkopen of stijgende vaste kosten in de tijd moet de berekening per periode worden bijgehouden. 🤖



## Zie ook

- **Vereist kennis van**: [[contributiemarge]]
- **Vereist kennis van**: [[vaste-kosten]]
- **Vereist kennis van**: [[variabele-kosten]]
- **Wordt voorondersteld in** (2): [[contributiemarge]] · [[vaste-kosten]]
