---
title: Rentabiliteit van het totaal der activa (ROA)
tags:
- concept
- cluster
- po-1-3
- po-1-9
linked_anchors:
- 1.3.I.A
- 1.3.II.C
- 1.3.taak.1
- 1.9.V
- 1.9.V.B
- 1.9.taak.1
programmaonderdelen:
- '1.3'
- '1.9'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/rentabiliteit-totaal-activa-roa.json
gegenereerd_op: '2026-05-18'
---
# Rentabiliteit van het totaal der activa (ROA) ⚖️

> [!summary] Korte inhoud
> Meten welk rendement de onderneming behaalt op het totaal van haar bezittingen — onafhankelijk van hoe ze die bezittingen heeft gefinancierd.

> [!info] Behoort tot: [[doelstellingen-financiele-analyse]]

Meten welk rendement de onderneming behaalt op het totaal van haar bezittingen — onafhankelijk van hoe ze die bezittingen heeft gefinancierd. ROA staat voor 'Return On Assets' (rentabiliteit totaal der activa). Het toont de economische rentabiliteit zonder vertekening door belasting- of financieringsstructuur.

_Bron: CBN-2011/14 §rentabiliteit van het totaal van de activa: voorbeeldmethoden_


## Bouwstenen

### Nettorentabiliteit totaal der activa — vóór belasting en kosten van schulden ⚖️

Verhouding tussen 'nettoresultaat vóór belasting + kosten van schulden' en het balanstotaal. De kosten van schulden tellen we erbij omdat we juist het economische rendement willen meten, los van de financieringskeuze.

**Waarom?** Zo krijg je zicht op de winstgevendheid van de bedrijfsmiddelen zelf — losgekoppeld van de vraag of die met eigen vermogen of met schuld zijn gefinancierd.


_Grondslag: CBN-2011/14 §rentabiliteit totaal activa_

### Brutorentabiliteit totaal der activa — vóór belasting en kosten van schulden ⚖️

Idem als netto-ROA maar met cashflow als teller: nettoresultaat vóór belasting + niet-kaskosten + kosten van schulden, gedeeld door het balanstotaal.

**Waarom?** Filtert ook de boekhoudkundige niet-kaselementen weg. Toont het kasrendement op de geïnvesteerde activa.


_Grondslag: CBN-2011/14 §rentabiliteit totaal activa_


## Berekening

### Berekening ROA (netto en bruto)

**Nettorentabiliteit totaal der activa, vóór belasting en kosten van schulden** 
```
netto ROA = (nettoresultaat boekjaar vóór belasting + kosten van schulden) / totaal van de activa
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `nettoresultaat vóór belasting` | Winst (verlies) van het boekjaar vóór belastingen op het resultaat | EUR |
| `kosten van schulden` | Intresten en andere financiële kosten op leningen | EUR |
| `totaal van de activa` | Balanstotaal op afsluitingsdatum | EUR |

**Voorbeeld-invulling**: Rotex: winst vóór belasting € 3.300.000; kosten van schulden € 600.000; balanstotaal € 30.000.000

```
(€ 3.300.000 + € 600.000) / € 30.000.000 = € 3.900.000 / € 30.000.000 = 13,0 %
```

_Resultaat in %_
**Brutorentabiliteit totaal der activa (op cashflow)** 
```
bruto ROA = (nettoresultaat vóór belasting + niet-kaskosten + kosten van schulden) / totaal van de activa
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `niet-kaskosten` | Afschrijvingen, waardeverminderingen, voorzieningen | EUR |
| `kosten van schulden` | Intresten op leningen | EUR |
| `totaal van de activa` | Balanstotaal | EUR |

**Voorbeeld-invulling**: Rotex: winst vóór belasting € 3.300.000; niet-kaskosten € 1.700.000; kosten van schulden € 600.000; balanstotaal € 30.000.000

```
(€ 3.300.000 + € 1.700.000 + € 600.000) / € 30.000.000 = € 5.600.000 / € 30.000.000 = 18,7 %
```

_Resultaat in %_
*Het balanstotaal is wat er aan kapitaal en schuld samen in de zaak zit. We willen weten of die middelen samen voldoende opbrengen — onafhankelijk van wie het geld leverde. Daarom tellen we de financiële kosten van schulden bij het resultaat: anders zou een vennootschap met veel schuld onterecht slechter scoren.*

### 1. Lees nettoresultaat vóór belasting

Neem 'Winst van het boekjaar vóór belastingen' uit de resultatenrekening (de regel net vóór de belastingen op het resultaat).

**Waarom?** Door vóór belasting te werken filter je het belastingtarief weg — twee vennootschappen met dezelfde economische winst maar verschillende belastingstatus krijgen zo vergelijkbare cijfers.

**📥 Input**:
- Resultatenrekening → **Winst vóór belastingen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad analyse → **Eerste teller-component** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Open de resultatenrekening van Rotex Roeselare NV.
2. Zoek de regel 'Winst van het boekjaar vóór belastingen' (€ 3.300.000).
3. Noteer.


**Grondslag**: CBN-2011/14 §rentabiliteit totaal activa

### 2. Tel de kosten van schulden erbij

Voeg de financiële kosten van schulden (intresten op leningen, kortingen op betaalde wisselbrieven, enz.) toe aan het resultaat.

**Waarom?** We willen het rendement los van de financieringskeuze. Door intresten terug op te tellen meet je wat de bezittingen 'als geheel' opbrengen — zoals een onderneming-zonder-schuld het zou doen.

**📥 Input**:
- Resultatenrekening → **Financiële kosten van schulden (intresten)** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad analyse → **Teller ROA** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Open in de resultatenrekening de rubriek 'Financiële kosten'.
2. Selecteer de kosten van schulden (intresten op leningen, dotaties op kredietkosten — bv. € 600.000).
3. Teller ROA = € 3.300.000 + € 600.000 = € 3.900.000.


**Grondslag**: CBN-2011/14 §rentabiliteit totaal activa

### 3. Deel door balanstotaal

Deel de teller (resultaat + kosten van schulden) door het balanstotaal op afsluitingsdatum.

**Waarom?** Het balanstotaal weerspiegelt alle economische middelen die in de onderneming zijn ingezet — eigen vermogen én schulden samen.

**📥 Input**:
- Balans → **Balanstotaal (activa = passiva)** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Ratio-tabel → **Netto-ROA** _(percentage)_

**🛠️ Hoe**:

1. Lees balanstotaal Rotex Roeselare NV (€ 30.000.000).
2. Bereken: € 3.900.000 / € 30.000.000 = 0,13 = 13,0 %.
3. Plaats in vergelijkingsbasis (vorig jaar, sector).


> [!example]- Voorbeeld: Rotex Roeselare NV — boekjaar 20X1
> Rotex Roeselare NV — boekjaar 20X1.
>
> 1. **Inputgegevens** 📊
>
>    | Rotex Roeselare NV — uittreksel             | Bedrag (€) |
>    |---------------------------------------------|-----------:|
>    | Winst boekjaar vóór belastingen             |  3.300.000 |
>    | Financiële kosten van schulden (intresten)  |    600.000 |
>    | Balanstotaal                                | 30.000.000 |
>
> 2. **Berekening netto-ROA** 🧮
>
>    Teller = € 3.300.000 + € 600.000 = **€ 3.900.000**
>    Netto-ROA = € 3.900.000 / € 30.000.000 = **13,0 %**
>

**Grondslag**: CBN-2011/14 §rentabiliteit totaal activa

### 4. Bereken bruto-ROA met cashflow

Tel ook de niet-kaskosten bij het resultaat, naast de kosten van schulden. Dan krijg je de bruto-cashbasis van het rendement op activa.

**Waarom?** Filtert boekhoudkundige niet-kaselementen uit: bruto-ROA toont het kasrendement op alle geïnvesteerde middelen.

**📥 Input**:
- Resultatenrekening → **Afschrijvingen, waardeverminderingen, voorzieningen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Ratio-tabel → **Bruto-ROA** _(percentage)_

**🛠️ Hoe**:

1. Som: winst vóór belasting € 3.300.000 + niet-kaskosten € 1.700.000 + kosten van schulden € 600.000 = € 5.600.000.
2. Deel door balanstotaal € 30.000.000.
3. Bruto-ROA = € 5.600.000 / € 30.000.000 = 18,7 %.


**Grondslag**: CBN-2011/14 §rentabiliteit totaal activa (cashflow-variant)

**Voorbeeld**: Rotex Roeselare NV: winst vóór belasting € 3.300.000; financiële kosten van schulden € 600.000; niet-kaskosten € 1.700.000; balanstotaal € 30.000.000.

```
Netto-ROA = (€ 3.300.000 + € 600.000) / € 30.000.000 = € 3.900.000 / € 30.000.000 = 13,0 %. Bruto-ROA = (€ 3.300.000 + € 1.700.000 + € 600.000) / € 30.000.000 = € 5.600.000 / € 30.000.000 = 18,7 %.
```

Resultaat: ROA van 13 % toont een gezonde economische winstgevendheid op de bedrijfsmiddelen, los van financieringsstructuur. Vergelijk met de gemiddelde kapitaalkost (WACC) — als ROA > WACC creëert de onderneming waarde.

## In de praktijk

<h3 id="1.3.II.C">Waarom de intresten op schulden terug erbij?</h3>

> [!tip]- Waarom de intresten op schulden terug erbij?
> Anders zou een vennootschap met veel schuld onterecht een lagere rentabiliteit lijken te hebben — door de intresten, niet door slechtere activa-prestatie. Door intresten weg te denken meet je de economische prestatie zelf. ⚖️


> [!info]- Niet verwarren met [[rentabiliteit-eigen-vermogen-roe]]
> ROA = rendement op alle middelen (economisch). ROE = rendement op eigen vermogen (aandeelhoudersperspectief). Als ROE > ROA → schulden versterken het aandeelhoudersrendement (hefboomeffect positief); als ROE < ROA → de kosten van schulden vreten meer op dan de schuld bijbrengt.
>
> _Trigger_: Examenvraag 'economisch vs financieel rendement': economisch = ROA; financieel/aandeelhouder = ROE.


## Valkuilen

> [!warning]- ROA wordt 'vóór belasting' berekend — verwar niet met nettowinst-marges, die vaak ná belasting zijn
> ⚠️ ROA wordt 'vóór belasting' berekend — verwar niet met nettowinst-marges, die vaak ná belasting zijn. Wees consistent: alle vergelijkingsbasis (sectorgemiddelden, vorige boekjaren) moet dezelfde tellerconventie gebruiken. ⚖️
>
> _Bron: CBN-2011/14 §rentabiliteit totaal activa_


> [!warning]- Een herwaardering doet het balanstotaal stijgen, waardoor ROA daalt — zelfs als de winst stabiel blijft
> ⚠️ Een herwaardering doet het balanstotaal stijgen, waardoor ROA daalt — zelfs als de winst stabiel blijft. CBN-2011/14 wijst expliciet op dit effect bij beoordeling van rentabiliteitsvoorwaarde voor een herwaarderingsmeerwaarde. ⚖️
>
> _Bron: CBN-2011/14 §rentabiliteitsvoorwaarden_



## Bronnen

[^1]: `CBN-2011-14-herwaarderingsmeerwaarden__sec_rentabiliteit-van-het-totaal-van-de-activa-voorbeeldmethoden`
[^2]: `CBN-2011-14-herwaarderingsmeerwaarden__sec_rentabiliteit-van-het-eigen-vermogen-voorbeeldmethoden`
[^3]: `CBN-2011-14-herwaarderingsmeerwaarden__sec_rentabiliteitsvoorwaarden_part2`
