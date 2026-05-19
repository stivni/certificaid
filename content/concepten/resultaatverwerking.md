---
title: Resultaatverwerking (winst- of verliesbestemming)
tags:
- concept
- cluster
- po-1-1
linked_anchors:
- 1.1.II.Q
programmaonderdelen:
- '1.1'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/resultaatverwerking.json
gegenereerd_op: '2026-05-18'
---
# Resultaatverwerking (winst- of verliesbestemming) ⚖️

Het eindjaars-paraplu-proces dat AV-besluit, wettelijke reserve-toets en uitkeerbaarheid in één boekingscyclus samenbrengt. Voor een stagiair-GA: cruciaal om de wettelijke reserve niet te vergeten zolang het 10 %-minimum niet bereikt is, en om de uitkeerbaarheidstoets correct toe te passen vóór een dividend wordt voorgesteld.

> [!summary] Korte inhoud
> Het proces waarbij het boekhoudkundige resultaat na winstbelasting wordt verdeeld over de verschillende bestemmingen: opname van wettelijke reserve, vrije bestemming aan beschikbare reserves, dividenduitkering, vergoeding bestuurders, overdracht naar volgend boekjaar.

Het proces waarbij het boekhoudkundige resultaat na winstbelasting wordt verdeeld over de verschillende bestemmingen: opname van wettelijke reserve, vrije bestemming aan beschikbare reserves, dividenduitkering, vergoeding bestuurders, overdracht naar volgend boekjaar. De resultaatverwerking gebeurt formeel door **goedkeuring van de algemene vergadering** op voorstel van het bestuursorgaan; tot dan staat het resultaat als 'te bestemmen' (rekening 79 of voorlopig overgedragen).

_Bron: WVV art. 7:211 + 5:142; KB WVV_


## In de praktijk

<h3 id="uitkeringstest-bv-dubbele-toets">Uitkeringstest BV: dubbele toets</h3>

> [!tip]- Uitkeringstest BV: dubbele toets
> Voor BV's geldt sinds WVV 2019 een dubbele uitkeringstest: (1) netto-actief-test (uitkering mag niet leiden tot negatief netto-actief), (2) liquiditeitstest (BV moet 12 maanden vooruit haar opeisbare schulden kunnen voldoen). Bestuursorgaan moet motiveren. Geen uitkering zonder positief uitkomst. ⚖️

> [!tip]- Herkennen op het examen
> Examen BV: 'mag dividend uitgekeerd worden van € 50.000?' → eerst beide testen uitvoeren.

<h3 id="verliesverwerking">Verliesverwerking</h3>

> [!tip]- Verliesverwerking
> Bij verlies van het boekjaar: het bestuur stelt voor om over te dragen naar volgend boekjaar (rekening 141 Overgedragen verlies), eventueel met aanwending van beschikbare reserves of onttrekking aan kapitaal. Klasse 79 'Onttrekkingen aan reserves / kapitaal' wordt dan gebruikt. ⚖️


## Tijdlijn

| Stap | Termijn | Actor | Actie |
|---|---|---|---|
| Afsluiting boekjaar | 31 december (klassiek) | bestuursorgaan | Inventaris + opstelling jaarrekening |
| Bijeenroeping AV | Binnen 6 maanden na boekjaareinde | bestuursorgaan | Bijeenroeping algemene vergadering voor goedkeuring |
| Neerlegging jaarrekening | Binnen 30 dagen na goedkeuring door AV | bestuursorgaan | Neerlegging bij Nationale Bank van België |

## Stappen

### 1. Bereken belastingen op het resultaat (klasse 67)

Verschuldigde vennootschapsbelasting op de fiscale winst van het boekjaar (670), aangevuld met regularisaties van vorige boekjaren (671) en gevormde fiscale voorzieningen (672, 6712).

**Waarom?** De vennootschapsbelasting is een echte kost die het resultaat verlaagt. Aparte rubriek toont de fiscale druk.

**📥 Input**:
- Fiscale aangifte → **Verschuldigde vennootschapsbelasting** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Boekhouding → **Klasse 67 Belastingen** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Bepaal fiscale belastbare basis (= boekhoudkundige winst + verworpen uitgaven − fiscaal aftrekbare elementen).
2. Pas tarief toe (25 % standaard, 20 % verlaagd op eerste schijf voor KMO's onder voorwaarden).
3. Trek voorafbetalingen af.
4. Boek: Debet 670 Verschuldigde belasting / Credit 4500 Verschuldigde belastingen op resultaat.


**Grondslag**: MAR klasse 67 + WIB92

### 2. Bereken winst (verlies) van het boekjaar (na belasting)

Resultaat vóór belasting min belastingen op het resultaat. Dit is het 'nettoresultaat' van de RR.

**📥 Input**:
- RR → **Resultaat vóór belasting** _(boekhoudkundig-bedrag)_
- Klasse 67 → **Belastingen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- RR → **Winst (verlies) van het boekjaar** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Neem resultaat vóór belasting (uit klasse 70-66).
2. Trek klasse 67 af.
3. Resultaat = nettowinst (verlies).


**Grondslag**: MAR klasse 6 + 7

### 3. Voorstel winstbestemming (klasse 69)

Bestuursorgaan stelt winstbestemming voor: (6920) toevoeging wettelijke reserve, (6921) toevoeging onbeschikbare reserves, (6922/3) belastingvrije/beschikbare reserves, (694) vergoeding van kapitaal (dividend), (695) bestuurders/zaakvoerders, (696) overdracht naar volgend jaar.

**Waarom?** De winst wordt niet automatisch uitgekeerd; algemene vergadering beslist op voorstel van bestuur over verdeling. Klasse 69-rekeningen registreren elk bestemmings-element.

> [!example]- Voorbeeld: Meubelzaak Mertens BV winst boekjaar 20X1 (na belasting) = € 42.000
> Meubelzaak Mertens BV winst boekjaar 20X1 (na belasting) = € 42.000. Voorstel bestuur.
>
> 1. **Voorstel winstbestemming** 🧮
>
>    Winst boekjaar:                           € 42.000
>    (a) Wettelijke reserve (5 %):              € 2.100
>    (b) Toevoeging beschikbare reserves:       € 10.000
>    (c) Dividend aan aandeelhouders:           € 15.000
>    (d) Vergoeding bestuurders:                € 5.000
>    (e) Overdracht naar volgend jaar:          € 9.900
>    **Totaal**:                                **€ 42.000** ✓
>
> 2. **Boekhoudkundige verwerking** 📝
>
>    Debet 6920 Toevoeging wettelijke reserve € 2.100
>    Debet 6921 Toevoeging onbeschikbare reserves €  0
>    Debet 6923 Toevoeging beschikbare reserves € 10.000
>    Debet 694 Vergoeding van het kapitaal (dividenden) € 15.000
>    Debet 695 Vergoeding bestuurders € 5.000
>    Debet 696 Overgedragen winst (overdracht) € 9.900
>      Credit 130 Wettelijke reserve € 2.100
>      Credit 133 Beschikbare reserves € 10.000
>      Credit 471 Tantièmes en dividenden te betalen € 20.000
>      Credit 140 Overgedragen winst € 9.900
>    (Debet = Credit = € 42.000 ✓)
>

**Grondslag**: MAR klasse 69 + WVV art. 7:211

### 4. Goedkeuring door algemene vergadering

Algemene vergadering keurt de jaarrekening + winstbestemming goed. Dividend wordt opeisbaar; alle reserve-mutaties worden definitief.

**Waarom?** AV is het hoogste orgaan; haar goedkeuring is constitutief voor de uitkeerbaarheid van dividend en de juridische geldigheid van de bestemming.

**🛠️ Hoe**:

1. Bestuur stelt verslag op en roept AV bijeen (binnen 6 maanden na boekjaareinde).
2. AV behandelt jaarrekening + bestemming + kwijting bestuursorgaan + commissaris.
3. Notulen opmaken; neerlegging jaarrekening bij NBB.


**Grondslag**: WVV art. 7:181 (NV); 5:80 (BV) jaarvergadering


## Valkuilen

> [!warning]- Boekhoudkundig resultaat ≠ uitkeerbaar resultaat
> ⚠️ Boekhoudkundig resultaat ≠ uitkeerbaar resultaat. De winst van het boekjaar wordt eerst gecorrigeerd voor wettelijke reserve, niet-uitkeerbare reserves en uitkeringstesten vóór er sprake is van dividend. ⚖️
>
> _Bron: WVV art. 7:211_


> [!warning]- Dividenden boekhoudkundig: VERGOEDING VAN HET KAPITAAL (rekening 694), GEEN financiële kost
> ⚠️ Dividenden boekhoudkundig: VERGOEDING VAN HET KAPITAAL (rekening 694), GEEN financiële kost. Onderscheid van klasse 65 cruciaal. ⚖️
>
> _Bron: MAR klasse 69_



## Zie ook

- **Getriggerd door**: [[eindejaarsverrichtingen]]
- **Vereist kennis van**: [[wettelijke-reserve]]
- **Vereist kennis van**: [[eigen-middelen]]

## Bronnen

[^1]: `MAR-ondernemingen__art_1`
[^2]: `MAR-ondernemingen__art_6`
