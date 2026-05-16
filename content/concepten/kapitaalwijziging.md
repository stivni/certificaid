---
title: Kapitaalwijziging (verhoging en vermindering)
tags:
- concept
- procedure
- po-1-1
linked_anchors:
- 1.1.II.T
- 1.1.II.H
programmaonderdelen:
- '1.1'
confidence: grounded
node_type: procedure
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/kapitaalwijziging.json
gegenereerd_op: '2026-05-16'
---
# Kapitaalwijziging (verhoging en vermindering) ⚖️

> [!summary] Korte inhoud
> Een **wijziging van het maatschappelijk kapitaal** (NV) of de **eigen vermogensinbreng** (BV).

> [!info] Behoort tot: [[eigen-middelen]]

Een **wijziging van het maatschappelijk kapitaal** (NV) of de **eigen vermogensinbreng** (BV). Twee richtingen: (1) **kapitaalverhoging** — door inbreng in geld, in natura, of door incorporatie van reserves/uitgiftepremies, (2) **kapitaalvermindering** — door werkelijke terugbetaling aan aandeelhouders of door verliesaanzuivering. Boekhoudkundig: aanpassing rekening 100 'Geplaatst kapitaal' (of 'Eigen vermogensinbreng'). Beide vereisen statutenwijziging (notariële akte) en hebben beschermingsregels voor schuldeisers.

_Bron: WVV art. 7:177 — 7:218 (NV); 5:120 — 5:154 (BV)_


## In de praktijk

<h3 id="incorporatie-van-reserves-of-uitgiftepremie">Incorporatie van reserves of uitgiftepremie</h3>

> [!tip]- Incorporatie van reserves of uitgiftepremie
> Een kapitaalverhoging zonder externe inbreng: bestaande reserves of uitgiftepremies worden 'omgezet' in kapitaal. Geen cashflow; alleen boekhoudkundige overheveling. Vereist statutenwijziging. ⚖️

> [!tip]- Herkennen op het examen
> Examen: 'beschikbare reserves € 80.000 + kapitaal € 50.000; AV besluit € 30.000 te incorporeren' → Debet 133 / Credit 100 voor € 30.000.


## Stappen

### 1. Beslissing algemene vergadering

Algemene vergadering beslist over kapitaalverhoging/-vermindering bij bijzondere meerderheid (typisch 75 % NV, 75 % BV). Notaris stelt akte op.

**Waarom?** Wijziging van het kapitaal raakt fundamentele aandeelhoudersrechten en schuldeiserspositie; vereist verzwaarde meerderheid + formaliteiten.

**🛠️ Hoe**:

1. Bestuursverslag bij voorstel.
2. Bijzondere AV.
3. Stemming bij verzwaarde meerderheid (typisch 75 %).
4. Notariële akte.


**Grondslag**: WVV art. 7:179 — 7:185 (NV); 5:121 (BV)

### 2. Storting / inbreng + boeking

Bij verhoging: inbrenger stort in geld of brengt activa in natura in (laatste vereist revisor-verslag). Bij vermindering: terugbetaling of verliesaanzuivering.

**🛠️ Hoe**:

1. Voor inbreng in natura: bedrijfsrevisor controleert werkelijke waarde.
2. Boeking verhoging: Debet 550 Bank (of relevante activa) / Credit 100 Kapitaal + Credit 11 Uitgiftepremie (verschil).
3. Boeking vermindering met terugbetaling: Debet 100 Kapitaal / Credit 550 Bank.
4. Vermindering tot dekking verlies: Debet 100 / Credit 141 Overgedragen verlies.


> [!example]- Voorbeeld: Naaiatelier Ninove BV met kapitaal € 100.000 en cumul. verlies € 35.000 (op rekening 141) beslist tot kapitaalverminderi…
> Naaiatelier Ninove BV met kapitaal € 100.000 en cumul. verlies € 35.000 (op rekening 141) beslist tot kapitaalvermindering ter dekking verlies van € 35.000.
>
> 1. **Voor-toestand eigen vermogen** 📊
>
>    | Eigen vermogen vóór             |        |
>    |---------------------------------|--------:|
>    | Kapitaal                        | 100.000 |
>    | Overgedragen verlies (-)        | −35.000 |
>    | **Netto-actief**                | **65.000** |
>
> 2. **Boeking** 📝
>
>    Debet 100 Kapitaal € 35.000 / Credit 141 Overgedragen verlies € 35.000
>    (Som debet = som credit ✓ — geen cashflow)
>
> 3. **Na-toestand** 📊
>
>    | Eigen vermogen na               |        |
>    |---------------------------------|--------:|
>    | Kapitaal                        | 65.000  |
>    | Overgedragen verlies            |     0   |
>    | **Netto-actief**                | **65.000** |
>

**Grondslag**: WVV + KB WVV; CBN praktijk

### 3. Bekendmaking en bescherming schuldeisers (bij vermindering)

Een kapitaalvermindering met werkelijke terugbetaling moet eerst gepubliceerd worden. Schuldeisers hebben 2 maanden bezwaartermijn om zekerheid te eisen.

**Waarom?** Schuldeisers verliezen door de kapitaalvermindering een deel van hun bescherming; ze krijgen tijd om zekerheid te eisen.

**🛠️ Hoe**:

1. Publicatie in Belgisch Staatsblad.
2. 2 maanden wachten.
3. Behandeling eventuele bezwaren (zekerheid stellen of vermindering uitstellen).
4. Pas dan: werkelijke terugbetaling.


**Grondslag**: WVV art. 7:209 (NV); 5:153 (BV)


## Valkuilen

> [!warning]- Kapitaalvermindering bij BV: sinds WVV 2019 vereist ook bij de BV de bescherming van schuldeisers (2 maanden bezwaartermijn) plus de dubbele…
> ⚠️ Kapitaalvermindering bij BV: sinds WVV 2019 vereist ook bij de BV de bescherming van schuldeisers (2 maanden bezwaartermijn) plus de dubbele uitkeringstest (netto-actief- en liquiditeitstest). Het oude WVB liet hier meer ruimte; nieuwe WVV is strenger. ⚖️
>
> _Bron: WVV art. 5:153_



## Zie ook

- **Getriggerd door**: [[uitgiftepremie]]

## Bronnen

[^1]: `MAR-ondernemingen__art_1`
[^2]: `CBN-2021-01-uitgiftepremie-0__sec_uitgiftepremie-is-geen-reserve-aanwending-van-de-uitgiftepre`
