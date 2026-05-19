---
title: Wettelijke reserve
tags:
- concept
- regel
- po-1-1
linked_anchors:
- 1.1.II.H
- 1.1.II.Q
programmaonderdelen:
- '1.1'
confidence: grounded
node_type: regel
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/wettelijke-reserve.json
gegenereerd_op: '2026-05-18'
---
# Wettelijke reserve ⚖️

De wettelijk verplichte buffer in het eigen vermogen die de uitkeerbaarheid en de schuldeisersbescherming bewaakt — 5 % van de jaarwinst tot een minimum van 10 % van het kapitaal (NV) of eigen vermogensinbreng (BV) is bereikt. Voor een stagiair-GA: een terugkerende eindjaarsverrichting bij resultaatverwerking — vergeten van de afhouding ondergraaft direct de geldigheid van een dividendvoorstel.

> [!summary] Korte inhoud
> **Verplichte jaarlijkse afhouding** van **5 % van de nettowinst** voor de **wettelijke reserve**, totdat deze reserve **10 % van het maatschappelijk kapitaal** bereikt (NV) of **één tiende van de eigen vermogensinbreng** (BV).

> [!info] Behoort tot: [[eigen-middelen]]

**Verplichte jaarlijkse afhouding** van **5 % van de nettowinst** voor de **wettelijke reserve**, totdat deze reserve **10 % van het maatschappelijk kapitaal** bereikt (NV) of **één tiende van de eigen vermogensinbreng** (BV). Geboekt op rekening 130 'Wettelijke reserve'. Niet uitkeerbaar zolang ze niet boven het wettelijk minimum staat. De afhouding wordt opgenomen in de winstbestemming bij goedkeuring jaarrekening door algemene vergadering (WVV art. 7:211, § 1; 5:200).

_Bron: WVV art. 7:211 (NV); 5:200 (BV)_


## Bouwstenen

### Verplichte afhouding 5 % per jaar tot 10 % kapitaal ⚖️

Zolang de wettelijke reserve niet 10 % van het kapitaal (NV) of de eigen vermogensinbreng (BV) bedraagt, MOET 5 % van de jaarwinst worden afgehouden. Bij verlies: geen afhouding (er is geen winst).

**Waarom?** De wettelijke reserve is een **veiligheidsbuffer** voor de schuldeisers: een wettelijk-vast bedrag dat niet vrij uitkeerbaar is. 10 % van het kapitaal is een redelijk minimum bescherming.



Naaiatelier Ninove BV kapitaal € 100.000, wettelijke reserve op 1/1 = € 6.500. Winst 20X1 = € 35.000. Verplichte afhouding 5 % × € 35.000 = € 1.750. Saldo eind 20X1 = € 8.250 (nog onder plafond € 10.000) → in 20X2 nog verplichte afhouding tot € 10.000 bereikt is.

_Grondslag: WVV art. 7:211 § 1_

### Niet uitkeerbaar zolang minimum niet bereikt ⚖️

De wettelijke reserve mag NIET worden uitgekeerd zolang het wettelijk minimum (10 % van kapitaal/inbreng) niet is bereikt. Het bedrag is een 'gebonden' deel van het eigen vermogen.

**Waarom?** De bedoeling van de reserve is precies om een buffer te zijn die de schuldeisers beschermt. Uitkering zou de bescherming uithollen.



Meubelzaak Mertens BV met wettelijke reserve € 5.600 (boven minimum € 5.000). Het surplus van € 600 zou in theorie kunnen worden uitgekeerd, maar in de praktijk wordt de wettelijke reserve in haar geheel meestal gehandhaafd als zekerheidsbuffer.

_Grondslag: WVV art. 7:211_

### Bij verlies: geen afhouding, maar reserve blijft staan 🤖

In een verliesjaar is er geen winst om uit te houden. De wettelijke reserve blijft op haar boekwaarde staan. Pas wanneer de cumulatieve verliezen het bestaande overgedragen resultaat overschrijden, kan de wettelijke reserve eventueel worden aangewend om verlies te dekken (uitzonderlijk).

**Waarom?** De jaarlijkse afhouding heeft enkel zin bij winst. Maar de bestaande reserve verdwijnt niet — ze beschermt actief tegen toekomstige verliezen.



Verffabriek Veurne BV maakt verlies € 18.000 in 20X1; wettelijke reserve € 8.000. Geen verplichte afhouding in 20X1 (geen winst). De € 8.000 blijft staan op rekening 130; het verlies komt op rekening 141 Overgedragen verlies.

_Grondslag: WVV art. 7:211_


## Berekening

### Verplichte afhouding wettelijke reserve

**Verplichte afhouding wettelijke reserve** 
```
afhouding = min(5 % × nettowinst ;  (10 % × kapitaal) − huidige saldo wettelijke reserve)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `nettowinst` | Resultaat van het boekjaar na belastingen | EUR |
| `kapitaal` | Maatschappelijk kapitaal (NV) of eigen vermogensinbreng (BV) | EUR |
| `huidige saldo wettelijke reserve` | Saldo van rekening 130 op begin boekjaar | EUR |

**Voorbeeld-invulling**: nettowinst = € 42.000; kapitaal = € 50.000; huidige reserve = € 3.500

```
min(5 % × € 42.000 ; 10 % × € 50.000 − € 3.500) = min(€ 2.100 ; € 1.500) = € 1.500
```

_Resultaat in EUR_
*5 % van de jaarwinst zolang de wettelijke reserve onder 10 % van het kapitaal/eigen vermogensinbreng blijft.*

### 1. Bepaal het wettelijk minimum (10 % regel)

10 % van het kapitaal (NV) of de eigen vermogensinbreng (BV).

**🛠️ Hoe**:

1. Neem het kapitaal/inbreng-saldo van rekening 100.
2. Vermenigvuldig met 10 %.
3. = wettelijk minimum reserve.


**Grondslag**: WVV art. 7:211

### 2. Vergelijk huidige reserve met het minimum

Saldo op rekening 130 vs minimum berekend in stap 1.

**🛠️ Hoe**:

1. Lees saldo rekening 130 op 1/1.
2. Indien ≥ minimum: geen verplichte afhouding meer.
3. Indien < minimum: afhouding van 5 % winst, MAAR maximaal het bedrag dat nodig is om het minimum te bereiken.


**Grondslag**: WVV art. 7:211

### 3. Bereken en boek de afhouding

Min(5 % × nettowinst, minimum − huidige reserve).

**📥 Input**:
- Resultatenrekening 20X1 → **Nettowinst** _(boekhoudkundig-bedrag)_
- Saldo rekening 130 → **Huidige reserve** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Winstbestemming → **Toevoeging wettelijke reserve** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Bereken 5 % × nettowinst.
2. Bereken het tekort: minimum − huidige reserve.
3. Neem het minimum van beide (om niet boven het wettelijk minimum te gaan).
4. Boek: Debet 6921 Toevoeging wettelijke reserve / Credit 130 Wettelijke reserve.


> [!example]- Voorbeeld: Meubelzaak Mertens BV: kapitaal € 50.000; wettelijke reserve op 1/1 = € 3.500; winst 20X1 = € 42.000
> Meubelzaak Mertens BV: kapitaal € 50.000; wettelijke reserve op 1/1 = € 3.500; winst 20X1 = € 42.000.
>
> 1. **Wettelijk minimum berekenen** 🧮
>
>    Minimum = 10 % × € 50.000 = **€ 5.000**
>    Huidige reserve = € 3.500 → tekort = € 1.500
>
> 2. **Verplichte afhouding** 🧮
>
>    5 % × € 42.000 = **€ 2.100**
>    Tekort = € 1.500
>    **Werkelijke afhouding** = min(€ 2.100, € 1.500) = **€ 1.500**
>    → Minimum bereikt; surplus € 600 (= € 2.100 − € 1.500) blijft beschikbaar voor andere bestemming.
>
> 3. **Boeking via winstbestemming** 📝
>
>    Debet 6921 Toevoeging aan wettelijke reserve € 1.500 / Credit 130 Wettelijke reserve € 1.500
>    Eindstand 130 = € 5.000 ✓
>

**Grondslag**: WVV art. 7:211


## In de praktijk

<h3 id="bv-zonder-kapitaal-10-van-eigen-vermogensinbreng">BV zonder kapitaal: 10 % van eigen vermogensinbreng</h3>

> [!tip]- BV zonder kapitaal: 10 % van eigen vermogensinbreng
> Voor BV's geldt sinds WVV 2019 dat het 10 %-plafond berekend wordt op de eigen vermogensinbreng (vroeger: maatschappelijk kapitaal). Boekhoudkundig komt dat neer op rekening 100, ongeacht de terminologische verschuiving. ⚖️


## Drempelwaarden

| Naam | Waarde | Eenheid | Gevolg |
|---|---|---|---|
| Verplichte afhouding van de nettowinst | 5 % | van de nettowinst van het boekjaar | Verplichte toevoeging aan wettelijke reserve uit winstbestemming. |
| Plafond wettelijke reserve | 10 % | van het maatschappelijk kapitaal (NV) of van de eigen vermogensinbreng (BV) | Wanneer de wettelijke reserve dit plafond bereikt, vervalt de verplichte jaarlijkse afhouding. |


> [!info]- Niet verwarren met [[beschikbare-reserves-aspect]]
> Wettelijke reserve: verplicht, geboden in WVV, minimum 10 % kapitaal, niet uitkeerbaar onder minimum. Beschikbare reserves: vrijwillig (vrije winstbestemming), vrij uitkeerbaar als dividend mits uitkeringstest.
>
> _Trigger_: Examen: 'kunnen we deze reserves uitkeren?' — Wettelijke: nee onder minimum. Beschikbare: ja na uitkeringstest.


## Valkuilen

> [!warning]- 5 % is van de NETTOWINST (na belastingen), niet van de omzet of brutowinst
> ⚠️ 5 % is van de NETTOWINST (na belastingen), niet van de omzet of brutowinst. Examen-fout: 'omzet × 5 %' is geen wettelijke reserve. ⚖️
>
> _Bron: WVV art. 7:211_


> [!warning]- Afhouding stopt zodra minimum bereikt — niet stelselmatig 5 % blijven afhouden
> ⚠️ Afhouding stopt zodra minimum bereikt — niet stelselmatig 5 % blijven afhouden. Verwarring: 'elke winst → automatisch 5 % wettelijke reserve' is fout zodra het plafond van 10 % is bereikt. ⚖️
>
> _Bron: WVV art. 7:211_



## Zie ook

- **Getriggerd door**: [[resultaatverwerking]]

## Voorbeelden

Meubelzaak Mertens BV heeft kapitaal/eigen vermogensinbreng € 50.000 → wettelijk minimum wettelijke reserve = 10 % × € 50.000 = € 5.000. Wettelijke reserve op 1/1 = € 3.500. Winst 20X1 = € 42.000. Verplichte afhouding = 5 % × € 42.000 = € 2.100. Boeking: Debet 6921 Toevoeging aan wettelijke reserve € 2.100 / Credit 130 Wettelijke reserve € 2.100. Saldo eind 20X1: € 5.600 — boven minimum, dus volgend jaar geen verplichte afhouding meer.

## Bronnen

[^1]: `MAR-ondernemingen__art_1`
