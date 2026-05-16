---
title: Belangen van derden / Aandeel van derden in het resultaat (minderheidsbelangen)
tags:
- concept
- fenomeen
- po-1-4
linked_anchors:
- 1.4.I.D
- 1.4.I.B
- 1.4.I.F
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: grounded
node_type: fenomeen
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/minderheidsbelangen.json
gegenereerd_op: '2026-05-16'
---
# Belangen van derden / Aandeel van derden in het resultaat (minderheidsbelangen) ⚖️

> [!summary] Korte inhoud
> Het deel van het eigen vermogen en van het resultaat van een integraal geconsolideerde dochter dat toebehoort aan andere aandeelhouders dan de moeder of de andere dochters in de consolidatiekring.

> [!info] Behoort tot: [[integrale-consolidatie]]

Het deel van het eigen vermogen en van het resultaat van een integraal geconsolideerde dochter dat toebehoort aan andere aandeelhouders dan de moeder of de andere dochters in de consolidatiekring. Op de geconsolideerde balans verschijnt dat als 'Belangen van derden' aan passiefzijde; in de geconsolideerde resultatenrekening als 'Aandeel van derden in het resultaat'. Dit fenomeen ontstaat enkel bij integrale consolidatie van een dochter waarvan de moeder minder dan 100 % bezit.

_Bron: KB WVV art. 3:137 (resultaat); art. 3:130 (herberekening)_


## Berekening

### Aandeel van derden — balans en resultatenrekening

**Belangen van derden (balans, passiefzijde)** 
```
belangen van derden = (1 − belangenpercentage moeder) × eigen vermogen dochter op afsluitingsdatum
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage moeder` | Aandeel van moeder in kapitaal dochter (zie [[belangenpercentage]]) | % |
| `eigen vermogen dochter op afsluitingsdatum` | Kapitaal + reserves + overgedragen resultaat + resultaat boekjaar van de dochter, einde boekjaar | EUR |

**Voorbeeld-invulling**: belangenpercentage Aurelia = 80 %; EV Brugse op afsluitingsdatum = € 2.000.000

```
(1 − 80 %) × € 2.000.000 = 20 % × € 2.000.000 = € 400.000
```

_Resultaat in EUR_
**Aandeel van derden in het resultaat (resultatenrekening)** 
```
aandeel derden in resultaat = (1 − belangenpercentage moeder) × resultaat dochter boekjaar
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage moeder` | Aandeel van moeder in kapitaal dochter | % |
| `resultaat dochter boekjaar` | Winst of verlies van de dochter in dit boekjaar | EUR |

**Voorbeeld-invulling**: belangenpercentage Aurelia = 80 %; resultaat Brugse boekjaar = € 500.000

```
(1 − 80 %) × € 500.000 = 20 % × € 500.000 = € 100.000
```

_Resultaat in EUR_
*Bij integrale consolidatie wordt 100 % van de cijfers van de dochter samengevoegd, ook al houdt de moeder slechts (bv.) 80 %. Het deel dat economisch aan minderheidsaandeelhouders toebehoort, wordt apart gepresenteerd zodat de geconsolideerde jaarrekening transparant toont welk deel aan de groep toekomt en welk deel aan derden.*

### 1. Stel het belangenpercentage van de moeder vast

Bepaal welk percentage van het kapitaal van de dochter de moeder (rechtstreeks of indirect) aanhoudt.

**Waarom?** Het derden-percentage is het complement van het belangenpercentage. Een fout cijfer hier propageert zich door de hele berekening.

**📥 Input**:
- Aandelenregister van Brugse Brouwerij BV → **Belang Aurelia Holding NV** _(percentage)_

**📤 Output**:
- Werkblad derden-aandeel → **Belangenpercentage moeder** _(percentage)_

**🛠️ Hoe**:

1. Raadpleeg het aandelenregister van Brugse Brouwerij BV.
2. Lees af hoeveel aandelen Aurelia Holding NV bezit, in verhouding tot het totaal van de stemgerechtigde aandelen.
3. Resultaat: belangenpercentage Aurelia = 80 % (voorbeeld).


**Grondslag**: KB WVV art. 3:137 jo. [[belangenpercentage]]

### 2. Bereken het derden-percentage als 1 minus belangenpercentage

Trek het belangenpercentage van de moeder af van 100 %. Het verschil is het derden-percentage — het deel dat aan minderheidsaandeelhouders toebehoort.

**Waarom?** De moeder consolideert 100 % integraal, maar economisch bezit ze slechts haar belangenpercentage. Het derden-percentage drukt uit hoeveel aan andere aandeelhouders toekomt.

**📥 Input**:
- Werkblad derden-aandeel → **Belangenpercentage moeder** _(percentage)_

**📤 Output**:
- Werkblad derden-aandeel → **Derden-percentage** _(percentage)_

**🛠️ Hoe**:

1. Neem het belangenpercentage uit stap 1 (80 %).
2. Bereken 100 % − 80 % = 20 %.
3. Dat is het derden-percentage voor alle volgende berekeningen.


**Grondslag**: KB WVV art. 3:137

### 3. Reken belangen van derden uit (balans, passiefzijde)

Vermenigvuldig het derden-percentage met het eigen vermogen van de dochter op afsluitingsdatum. Het resultaat boek je in de geconsolideerde balans als 'Belangen van derden' aan passiefzijde.

**Waarom?** Bij integrale consolidatie heb je 100 % van het eigen vermogen van de dochter mee opgenomen — terwijl een deel daarvan economisch aan derden toebehoort. Door 'Belangen van derden' apart te tonen, blijft duidelijk wat aan de groep toekomt.

**📥 Input**:
- Balans dochter op afsluitingsdatum → **Eigen vermogen totaal** _(boekhoudkundig-bedrag)_
- Werkblad derden-aandeel → **Derden-percentage** _(percentage)_

**📤 Output**:
- Geconsolideerde balans → **Belangen van derden (passiefzijde)** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Neem het eigen vermogen van Brugse Brouwerij BV op afsluitingsdatum (kapitaal + reserves + overgedragen resultaat + resultaat boekjaar; bv. € 2.000.000).
2. Vermenigvuldig met het derden-percentage uit stap 2: 20 % × € 2.000.000 = € 400.000.
3. Boek € 400.000 aan passiefzijde van de geconsolideerde balans onder 'Belangen van derden'.


> [!example]- Voorbeeld: Aurelia Holding NV bezit 80 % van Brugse Brouwerij BV; eigen vermogen Brugse op afsluitingsdatum = 500
> Aurelia Holding NV bezit 80 % van Brugse Brouwerij BV; eigen vermogen Brugse op afsluitingsdatum = 500.
>
> 1. **Berekening belangen van derden** 🧮
>
>    Eigen vermogen Brugse Brouwerij BV (afsluit) = € 2.000.000
>    Derden-percentage = 100 % − 80 % = **20 %**
>    Belangen van derden = 20 % × € 2.000.000 = **€ 400.000**
>
> 2. **Geconsolideerde balans (passiefzijde, fragment)** 📊
>
>    | Geconsolideerde passiva     |     |
>    |-----------------------------|----:|
>    | Eigen vermogen Aurelia (incl. 80 % Brugse) | ... |
>    | **Belangen van derden**     | **100** |
>    | Schulden                    | ... |
>

**Grondslag**: KB WVV art. 3:137

### 4. Reken aandeel van derden in resultaat (resultatenrekening)

Vermenigvuldig het derden-percentage met het resultaat van het boekjaar van de dochter. Boek dit als 'Aandeel van derden in het resultaat' onderaan de geconsolideerde resultatenrekening.

**Waarom?** Idem als bij de balans: het volledige resultaat van Brugse zit in de geconsolideerde resultatenrekening, maar het deel dat aan derden toebehoort moet expliciet zichtbaar zijn. Pas na deze post weet je wat het 'geconsolideerd resultaat van de groep' is.

**📥 Input**:
- Resultatenrekening dochter → **Resultaat van het boekjaar** _(boekhoudkundig-bedrag)_
- Werkblad derden-aandeel → **Derden-percentage** _(percentage)_

**📤 Output**:
- Geconsolideerde resultatenrekening → **Aandeel van derden in het resultaat** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Neem het resultaat van het boekjaar van Brugse Brouwerij BV (bv. 100).
2. Vermenigvuldig met het derden-percentage: 20 % × 100 = 20.
3. Boek 20 als aparte post 'Aandeel van derden in het resultaat'.
4. Wat overblijft (80 % × 100 = 80) is het deel voor de moeder — dat zit al in het geconsolideerd nettoresultaat van de groep.


**Grondslag**: KB WVV art. 3:137

### 5. Verwerk derden-aandeel in herberekende balansposten

Wanneer bezittingen of schulden van de dochter werden geherwaardeerd (KB WVV art. 3:130, lid 1) — bv. door toerekening van stille meerwaarden — boek je het bijbehorend deel van die herberekening ook in 'Belangen van derden' aan passiefzijde.

**Waarom?** De herberekeningen zijn ook voor derden van toepassing — niet enkel voor het belang van de moeder. Anders zou je een meerwaarde volledig aan de moeder toerekenen terwijl een deel ervan economisch aan derden hoort.

**📥 Input**:
- Werkblad consolidatieverschil → **Toerekening aan herberekende posten** _(boekhoudkundig-bedrag)_
- Werkblad derden-aandeel → **Derden-percentage** _(percentage)_

**📤 Output**:
- Geconsolideerde balans → **Belangen van derden (incl. derden-deel herberekeningen)** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Identificeer de stille meerwaarden die bij eerste consolidatie zijn toegerekend (bv. terreinen van Brugse € 250.000 ondergewaardeerd).
2. Bereken het derden-deel van die herberekening: 20 % × € 250.000 = € 50.000.
3. Voeg dit bedrag toe aan de post 'Belangen van derden' (stap 3): € 400.000 + € 50.000 = € 450.000.
4. Belangrijk: KB WVV art. 3:130, lid 4 vereist dat derden meedelen in de herberekeningen — niet alleen in het boekhoudkundige EV.


**Grondslag**: KB WVV art. 3:130, lid 4

**Voorbeeld**: Aurelia Holding NV bezit 80 % van Brugse Brouwerij BV (integrale consolidatie). Eigen vermogen van Brugse op afsluitingsdatum = 500 (incl. resultaat boekjaar 100). Resultaat boekjaar Brugse = 100.

```
Belang% (Aurelia in Brugse) = 80 %. Derden-percentage = 20 %.
Belangen van derden (balans, passief) = 20 % × € 2.000.000 = € 400.000.
Aandeel van derden in het resultaat (resultatenrekening) = 20 % × € 500.000 = € 100.000.
Deel van het resultaat voor Aurelia (na aftrek derden) = 80 % × € 500.000 = € 400.000.
```

Resultaat: In de geconsolideerde balans: 'Belangen van derden' = 100 (passiefzijde). In de geconsolideerde resultatenrekening: 'Aandeel van derden in het resultaat' = 20. De resterende 80 zit in het geconsolideerd resultaat van de groep dat aan Aurelia toekomt.

## In de praktijk

<h3 id="enkel-bij-integrale-consolidatie">Enkel bij integrale consolidatie</h3>

> [!tip]- Enkel bij integrale consolidatie
> Minderheidsbelangen verschijnen alleen bij integrale consolidatie (waarbij 100 % van de dochter wordt opgenomen). Bij evenredige consolidatie wordt het derden-deel gewoon niet opgenomen → geen aparte derden-post nodig. Bij vermogensmutatie zit alleen het pro-rata aandeel van de moeder in de balans → ook geen derden-post. ⚖️

> [!tip]- Herkennen op het examen
> Examen: zie je een post 'Belangen van derden' op een geconsolideerde balans? → integrale consolidatie. Geen 'Belangen van derden' → evenredige consolidatie of vermogensmutatie.

<h3 id="negatief-aandeel-van-derden">Negatief aandeel van derden</h3>

> [!tip]- Negatief aandeel van derden
> Maakt een dochter een verlies en consolideert de moeder integraal, dan kan het derden-aandeel ook negatief uitkomen (waardoor 'Belangen van derden' op de balans afneemt). Anders dan bij vermogensmutatie (waar de boekwaarde niet onder nul mag gaan) wordt bij integrale consolidatie het volledige resultaat opgenomen, en het derden-deel volgt naar evenredigheid — ook in min. 🤖


## Valkuilen

> [!warning]- Het derden-aandeel bereken je op het eigen vermogen van de dochter ná herberekening van onder- of overgewaardeerde bezittingen en schulden (…
> ⚠️ Het derden-aandeel bereken je op het eigen vermogen van de dochter ná herberekening van onder- of overgewaardeerde bezittingen en schulden (KB WVV art. 3:130, lid 4). De derden-correctie geldt dus ook voor stille meer- of minderwaarden die bij eerste consolidatie zijn vastgesteld — niet enkel voor het boekhoudkundige EV. Voorbeeld: bij Brugse Brouwerij BV werden terreinen € 250.000 opgewaardeerd; dan komt 20 % × € 250.000 = € 50.000 erbij in 'Belangen van derden'. ⚖️
>
> _Bron: KB WVV art. 3:130, lid 4_



## Zie ook

- **Vereist kennis van**: [[belangenpercentage]]

## Bronnen

[^1]: `KB-WVV-2019__art_3_108`
[^2]: `KB-WVV-2019__art_3_102`
[^3]: `KB-WVV-2019__art_3_111`
