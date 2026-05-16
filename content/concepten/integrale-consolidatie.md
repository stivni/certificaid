---
title: Integrale consolidatie
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
gegenereerd_uit: data/concepten/records/integrale-consolidatie.json
gegenereerd_op: '2026-05-16'
---
# Integrale consolidatie ⚖️

> De geconsolideerde jaarrekening voorstellen alsof het geheel van de consoliderende vennootschap en haar exclusief gecontroleerde dochterondernemingen één enkele economische entiteit vormt. De activa, passiva, rechten, verplichtingen, opbrengsten en kosten van de moeder en van haar exclusief gecontroleerde dochters worden integraal opgenomen (voor 100 %); het deel dat toebehoort aan derden (minderheidsaandeelhouders) wordt afzonderlijk gepresenteerd in 'Belangen van derden' (balans) en 'Aandeel van derden in het resultaat' (resultatenrekening).
>
> _Bron: KB WVV art. 3:123 jo. art. 3:124, 1°_


> [!summary] Korte definitie
> De geconsolideerde jaarrekening voorstellen alsof het geheel van de consoliderende vennootschap en haar exclusief gecontroleerde dochterondernemingen één enkele economische entiteit vormt.

> [!info] Behoort tot: [[consolidatieverschil]] · [[minderheidsbelangen]] · [[consolidatiemethodes-vergelijking]]
> [!info] Bestaat uit: [[intragroep-eliminaties]] · [[minderheidsbelangen]]
## Bouwstenen

### Volledige opname van beide balansen ⚖️

Alle bezittingen en schulden van moeder en dochter komen samen in de geconsolideerde balans — voor 100 %. Het belangenpercentage speelt in deze stap nog geen rol.

**Waarom?** De groep wordt voorgesteld als één economische entiteit; je doet alsof het één bedrijf is, ook al heeft de moeder maar een belang van bijvoorbeeld 80 %.

**Voorbeeld**: Aurelia Holding NV heeft activa 1000, Brugse Brouwerij BV heeft activa 600 → geconsolideerde activa (vóór intragroep-eliminaties): 1600.

_Grondslag: KB WVV art. 3:126_

### Schrappen van deelneming tegen aandeel in EV ⚖️

Schrap de post 'Deelneming dochter' uit de balans van de moeder en schrap het bijhorend aandeel van de moeder in het eigen vermogen van de dochter. Gebruik daarvoor het eigen vermogen op de datum van aankoop, niet op afsluitingsdatum.

**Waarom?** Anders zou je dezelfde economische waarde tweemaal tellen: één keer als 'Deelneming' bij de moeder en één keer als 'Eigen vermogen' van de dochter.

**Voorbeeld**: Aurelia Holding NV bezit een 'Deelneming Brugse Brouwerij BV' van 320; aandeel in EV Brugse op aankoopdatum = 80 % × 300 = 240. Beide bedragen worden geschrapt.

_Grondslag: KB WVV art. 3:127, a) jo. art. 3:129_

### Verschil eerst toerekenen, dan pas goodwill ⚖️

Het verschil dat uit de schrapping overblijft, reken je eerst toe aan bezittingen of schulden waarvan de werkelijke waarde afwijkt van de boekwaarde. Pas wat dan nog overblijft, boek je als 'Consolidatieverschillen' (positief → actiefzijde, negatief → passiefzijde). Positieve en negatieve verschillen mag je niet tegen elkaar wegstrepen, tenzij ze dezelfde dochter betreffen — dan moet het.

**Waarom?** Boekwaarden weerspiegelen niet altijd de werkelijke waarde. Door eerst die verborgen meer- of minwaarden te erkennen, voorkom je dat het hele verschil onterecht als goodwill (consolidatieverschil) wordt geboekt.

**Voorbeeld**: Aurelia Holding NV koopt Brugse Brouwerij BV; consolidatieverschil = 80. Het vastgoed van Brugse staat op 200 maar is werkelijk 250 waard → reken 50 toe aan vastgoed; resterende 30 boek je als 'Consolidatieverschillen'.

_Grondslag: KB WVV art. 3:130_

### Schrappen van onderlinge posten ⚖️

Verwijder vorderingen en schulden tussen moeder en dochter (en tussen dochters onderling) uit de geconsolideerde balans. Verwijder ook winsten of verliezen die uit interne verkopen nog in activa (zoals voorraden) zitten. Idem voor onderlinge opbrengsten en kosten in de resultatenrekening.

**Waarom?** Een groep kan niet aan zichzelf verkopen of geld lenen — economisch is dat één bedrijf. Als je die posten zou laten staan, blaast de geconsolideerde balans onterecht op.

**Voorbeeld**: Aurelia Holding NV heeft een vordering van 50 op Brugse Brouwerij BV. In de geconsolideerde balans verdwijnen zowel de vordering bij Aurelia als de schuld bij Brugse.

_Grondslag: KB WVV art. 3:134, 3:136_

### Aandeel van derden apart presenteren ⚖️

Bereken welk deel van het eigen vermogen en het resultaat van de dochter aan andere aandeelhouders toebehoort dan de moeder. Op de balans verschijnt dat als 'Belangen van derden' aan passiefzijde, op de resultatenrekening als 'Aandeel van derden in het resultaat'.

**Waarom?** Bij integrale consolidatie zit 100 % van de dochter-balans erin, maar de moeder bezit economisch maar (bv.) 80 %. De 20 % die aan derden toebehoort moet zichtbaar blijven — anders krijgt de moeder krediet voor cijfers die niet aan haar toekomen.

**Voorbeeld**: Eigen vermogen Brugse Brouwerij BV op afsluitingsdatum = 400; belang Aurelia = 80 %. Belangen van derden = 20 % × 400 = 80, gepresenteerd aan passiefzijde van de geconsolideerde balans.

_Grondslag: KB WVV art. 3:137_


## Berekening

### Integrale consolidatie — werkstroom (compensatie + eliminatie + aandeel van derden)

**Geconsolideerde post (vóór aandeel van derden)** 
```
geconsolideerde post = post moeder + post dochter (voor 100 %) − intragroep-eliminaties
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `post moeder` | Bedrag van de post in de balans van de moeder | EUR |
| `post dochter (voor 100 %)` | Bedrag van dezelfde post bij de dochter, los van belangenpercentage | EUR |
| `intragroep-eliminaties` | Onderlinge vorderingen, schulden of niet-gerealiseerde winsten die je schrapt | EUR |

**Voorbeeld-invulling**: Aurelia 'Vlottende activa' = 800; Brugse 'Vlottende activa' = 200; intragroep-vordering = 50

```
800 + 200 − 50 = 950
```

_Resultaat in EUR_
**Aandeel van derden in het eigen vermogen** (volgt op: geconsolideerde-post)
```
belangen van derden = (1 − belangenpercentage moeder) × eigen vermogen dochter op afsluitingsdatum
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage moeder` | Aandeel van moeder in kapitaal dochter (zie [[belangenpercentage]]) | % |
| `eigen vermogen dochter op afsluitingsdatum` | Kapitaal + reserves + overgedragen resultaat van de dochter, einde boekjaar | EUR |

**Voorbeeld-invulling**: belangenpercentage Aurelia = 80 %; EV Brugse op afsluitingsdatum = 400

```
(1 − 80 %) × 400 = 20 % × 400 = 80
```

_Resultaat in EUR_
**Aandeel van derden in het resultaat van het boekjaar** 
```
aandeel derden in resultaat = (1 − belangenpercentage moeder) × resultaat dochter boekjaar
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage moeder` | Aandeel van moeder in kapitaal dochter | % |
| `resultaat dochter boekjaar` | Winst of verlies van de dochter in dit boekjaar | EUR |

**Voorbeeld-invulling**: belangenpercentage Aurelia = 80 %; resultaat Brugse boekjaar = 100

```
(1 − 80 %) × 100 = 20 % × 100 = 20
```

_Resultaat in EUR_
*De moeder controleert de dochter volledig, dus presenteer de groep als één bedrijf. Activa en schulden van beide kanten komen voor 100 % in de geconsolideerde balans. Het deel dat niet aan de moeder toebehoort (de minderheidsaandeelhouders) zet je apart als 'Belangen van derden' aan passiefzijde, zodat het cijferbeeld eerlijk blijft.*

### . 

**Voorbeeld**: Moeder M bezit 80 % van de stemrechten en het kapitaal van dochter D. Op acquisitiedatum: aanschaffingswaarde aandelen = 320; eigen vermogen D = 300; geen onder-/overwaarderingen. Balans D bij afsluiting jaar 1: activa 600, schulden aan derden 200, eigen vermogen 400 (waarvan resultaat boekjaar 100). M heeft een vordering op D van 50 (D dus een schuld van 50 aan M).

```
Stap 1: integrale opname. Activa geconsolideerd = activa M + 600 (D, 100 %). Schulden geconsolideerd = schulden M + 200 (D, 100 %).
Stap 2: compensatie. Boekwaarde aandelen (320) − aandeel M in EV op acquisitiedatum (80 % × 300 = 240) = positief consolidatieverschil van 80; geboekt onder 'Consolidatieverschillen' actiefzijde (KB WVV art. 3:130) en afgeschreven over passend plan (KB WVV art. 3:131).
Stap 3: eliminatie van de onderlinge vordering/schuld 50: de vordering van M en de schuld van D worden allebei geschrapt; geconsolideerde activa en schulden dalen elk met 50.
Stap 4: aandeel van derden. Eigen vermogen D op afsluitingsdatum = 400; aandeel van derden in EV = 20 % × 400 = 80 (post 'Belangen van derden', passiefzijde). Resultaat D = 100; aandeel van derden in resultaat = 20 % × 100 = 20 (post 'Aandeel van derden in het resultaat').
```

Resultaat: In de geconsolideerde balans staan de 600 activa en 200 schulden van D voor 100 % opgenomen (na eliminatie van 50 intra-groep); 'Consolidatieverschillen' = 80 (actief); 'Belangen van derden' = 80 (passief). In de geconsolideerde resultatenrekening wordt het volledige resultaat van D meegenomen, met 20 afzonderlijk gepresenteerd als 'Aandeel van derden in het resultaat'. Het deel dat aan M toekomt: 80 % × 100 = 80.

## In de praktijk

### Wanneer toepassen {id="wanneer-toepassen"}

Integrale consolidatie is verplicht voor exclusief gecontroleerde dochters die in de consolidatiekring zitten (KB WVV art. 3:124, 1°). Bij consortium-leden is integrale consolidatie ook van toepassing op de leden zelf (samenlezing WVV art. 3:24 en KB WVV art. 3:124, 1°). ⚖️

**Herkenningspunt**: Stemrechten > 50 % → integraal (tenzij uitgesloten of in feite-controle die het getrouwe beeld zou aantasten).

### Eigen aandelen van de consoliderende vennootschap {id="eigen-aandelen-van-de-consoliderende-vennootschap"}

Eigen aandelen van de consoliderende vennootschap (én aandelen in de consoliderende vennootschap die door een in de consolidatie opgenomen dochter worden gehouden) worden in de geconsolideerde balans geboekt onder actiefpost IX. De toelichting vermeldt hoeveel aandelen aldus in bezit zijn. ⚖️


<details>
<summary><strong>Niet verwarren met</strong> (2 vergelijkingen)</summary>

- **vs [[evenredige-consolidatie]]** — Integrale consolidatie neemt 100 % van activa/passiva op (met aandeel van derden afzonderlijk) — voor exclusief gecontroleerde dochters. Evenredige consolidatie neemt activa/passiva op naar rato van de kapitaaldeelname (zonder afzonderlijke
  - _Trigger_: Soort controle / type relatie tussen moeder en dochter bepaalt welke methode.
- **vs [[vermogensmutatiemethode]]** — Integrale consolidatie neemt de individuele activa/passiva op (regel voor regel). Vermogensmutatie behoudt de deelneming als één post 'Vennootschappen waarop vermogensmutatie is toegepast' (geherwaardeerd naar het pro-rata aandeel in het ei
  - _Trigger_: Soort controle / type relatie tussen moeder en dochter bepaalt welke methode.

</details>


## Valkuilen

- ⚠️ De compensatie van de deelneming gebeurt op verwervingsdatum, niet op afsluitingsdatum. Het eigen vermogen op verwervingsdatum bevriest; latere wijzigingen in het eigen vermogen van de dochter worden behandeld als geconsolideerde reserves of resultaat — niet als toename of afname van het consolidatieverschil. ⚖️
- ⚠️ Bij eerste consolidatie van een vennootschap kan de compensatie ten belope van de aandelen in haar bezit op die datum gebeuren op de aanvangsdatum van het boekjaar (KB WVV art. 3:129, b)). Dit is een uitzondering die in de toelichting kan worden gemotiveerd. ⚖️
- ⚠️ De weglatingen van KB WVV art. 3:134 en 3:136 mogen achterwege blijven 'wanneer de betrokken bedragen, gelet op het doel van artikel 3:105, slechts van te verwaarlozen betekenis zijn' (KB WVV art. 3:138 jo. art. 3:139). Praktisch beoordelen op materialiteit. ⚖️

## Zie ook

- **Getriggerd door**: [[exclusieve-controle]]

## Bronnen

[^1]: `KB-WVV-2019__art_3_97`
[^2]: `KB-WVV-2019__art_3_98`
[^3]: `KB-WVV-2019__art_3_108`
[^4]: `KB-WVV-2019__art_3_75`
[^5]: `KB-WVV-2019__art_3_76`
[^6]: `KB-WVV-2019__art_3_100`
[^7]: `KB-WVV-2019__art_3_101`
[^8]: `KB-WVV-2019__art_3_102`
[^9]: `KB-WVV-2019__art_3_106`
[^10]: `KB-WVV-2019__art_3_107`
[^11]: `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_consolidatiemethode`
[^12]: `KB-WVV-2019__art_3_105`
[^13]: `KB-WVV-2019__art_3_111`
[^14]: `KB-WVV-2019__art_3_112`
[^15]: `KB-WVV-2019__art_3_109`
[^16]: `KB-WVV-2019__art_3_110`
