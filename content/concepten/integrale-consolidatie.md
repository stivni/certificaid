---
title: Integrale consolidatie
tags:
- concept
- cluster
- po-1-4
linked_anchors:
- 1.4.I.D
- 1.4.I.B
- 1.4.II.C
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/integrale-consolidatie.json
gegenereerd_op: '2026-05-18'
---
# Integrale consolidatie ⚖️

> [!summary] Korte inhoud
> De geconsolideerde jaarrekening voorstellen alsof het geheel van de consoliderende vennootschap en haar exclusief gecontroleerde dochterondernemingen één enkele economische entiteit vormt.

> [!info] Behoort tot: [[consolidatieverschil]] · [[minderheidsbelangen]] · [[consolidatiemethodes-vergelijking]]

De geconsolideerde jaarrekening voorstellen alsof het geheel van de consoliderende vennootschap en haar exclusief gecontroleerde dochterondernemingen één enkele economische entiteit vormt. De activa, passiva, rechten, verplichtingen, opbrengsten en kosten van de moeder en van haar exclusief gecontroleerde dochters worden integraal opgenomen (voor 100 %); het deel dat toebehoort aan derden (minderheidsaandeelhouders) wordt afzonderlijk gepresenteerd in 'Belangen van derden' (balans) en 'Aandeel van derden in het resultaat' (resultatenrekening).

_Bron: KB WVV art. 3:123 jo. art. 3:124, 1°_


## Bouwstenen

### Volledige opname van beide balansen ⚖️

Alle bezittingen en schulden van moeder en dochter komen samen in de geconsolideerde balans — voor 100 %. Het belangenpercentage speelt in deze stap nog geen rol.

**Waarom?** De groep wordt voorgesteld als één economische entiteit; je doet alsof het één bedrijf is, ook al heeft de moeder maar een belang van bijvoorbeeld 80 %.


_Grondslag: KB WVV art. 3:126_

### Schrappen van deelneming tegen aandeel in EV ⚖️

Schrap de post 'Deelneming dochter' uit de balans van de moeder en schrap het bijhorend aandeel van de moeder in het eigen vermogen van de dochter. Gebruik daarvoor het eigen vermogen op de datum van aankoop, niet op afsluitingsdatum.

**Waarom?** Anders zou je dezelfde economische waarde tweemaal tellen: één keer als 'Deelneming' bij de moeder en één keer als 'Eigen vermogen' van de dochter.


_Grondslag: KB WVV art. 3:127, a) jo. art. 3:129_

### Verschil eerst toerekenen, dan pas goodwill ⚖️

Zie [[consolidatieverschil]] §berekening voor de volledige procedure (toerekening aan stille meer-/minwaarden, residu als 'Consolidatieverschillen', niet-saldering tussen verschillende dochters). Bij integrale consolidatie is dit één bouwsteen van de procedure; de inhoudelijke regel staat in het concept-record `consolidatieverschil`.

**Waarom?** Verwijzen i.p.v. dupliceren — de regel KB WVV art. 3:130 is een fenomeen op zichzelf en heeft een eigen concept-record.


_Grondslag: [[consolidatieverschil]] · KB WVV art. 3:130_

### Schrappen van onderlinge posten ⚖️

Verwijder vorderingen en schulden tussen moeder en dochter (en tussen dochters onderling) uit de geconsolideerde balans. Verwijder ook winsten of verliezen die uit interne verkopen nog in activa (zoals voorraden) zitten. Idem voor onderlinge opbrengsten en kosten in de resultatenrekening.

**Waarom?** Een groep kan niet aan zichzelf verkopen of geld lenen — economisch is dat één bedrijf. Als je die posten zou laten staan, blaast de geconsolideerde balans onterecht op.


_Grondslag: KB WVV art. 3:134, 3:136_

### Aandeel van derden apart presenteren ⚖️

Bereken welk deel van het eigen vermogen en het resultaat van de dochter aan andere aandeelhouders toebehoort dan de moeder. Op de balans verschijnt dat als 'Belangen van derden' aan passiefzijde, op de resultatenrekening als 'Aandeel van derden in het resultaat'.

**Waarom?** Bij integrale consolidatie zit 100 % van de dochter-balans erin, maar de moeder bezit economisch maar (bv.) 80 %. De 20 % die aan derden toebehoort moet zichtbaar blijven — anders krijgt de moeder krediet voor cijfers die niet aan haar toekomen.


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

**Voorbeeld-invulling**: Aurelia 'Vlottende activa' = € 4.000.000; Brugse 'Vlottende activa' = € 1.000.000; intragroep-vordering = € 250.000

```
€ 4.000.000 + € 1.000.000 − € 250.000 = € 4.750.000
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

**Voorbeeld-invulling**: belangenpercentage Aurelia = 80 %; EV Brugse op afsluitingsdatum = € 2.000.000

```
(1 − 80 %) × € 2.000.000 = 20 % × € 2.000.000 = € 400.000
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

**Voorbeeld-invulling**: belangenpercentage Aurelia = 80 %; resultaat Brugse boekjaar = € 500.000

```
(1 − 80 %) × € 500.000 = 20 % × € 500.000 = € 100.000
```

_Resultaat in EUR_
*De moeder controleert de dochter volledig, dus presenteer de groep als één bedrijf. Activa en schulden van beide kanten komen voor 100 % in de geconsolideerde balans. Het deel dat niet aan de moeder toebehoort (de minderheidsaandeelhouders) zet je apart als 'Belangen van derden' aan passiefzijde, zodat het cijferbeeld eerlijk blijft.*

### 1. Tel alle activa en passiva voor 100 % op

Voeg alle bezittingen en schulden van moeder en dochter samen in één geconsolideerde balans — voor 100 %, los van het belangenpercentage.

**Waarom?** De groep wordt voorgesteld als één economische entiteit; pro-rata-opname zou de schaal van de groep verbergen.

**📥 Input**:
- Balans moeder → **Alle posten** _(boekhoudkundig-bedrag)_
- Balans dochter → **Alle posten** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans (tussentijds) → **Alle posten samengevoegd** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Open de balans van Aurelia Holding NV.
2. Open de balans van Brugse Brouwerij BV.
3. Tel post per post de bedragen op: vaste activa moeder + vaste activa dochter, vlottende activa moeder + vlottende activa dochter, schulden moeder + schulden dochter.
4. Eigen vermogen van de dochter komt nog niet definitief in de geconsolideerde balans — daar komt stap 2 aan te pas.


**Grondslag**: KB WVV art. 3:126

### 2. Schrap de deelneming en boek het verschil

Schrap de post 'Deelneming dochter' uit de moeder-balans en schrap het bijhorend aandeel van de moeder in het eigen vermogen van de dochter. Het verschil tussen die twee bedragen heet het consolidatieverschil.

**Waarom?** Anders zou je dezelfde economische waarde tweemaal tellen: één keer als 'Deelneming' bij de moeder en één keer als 'Eigen vermogen' van de dochter.

**📥 Input**:
- Balans Aurelia Holding NV → **Deelnemingen (Brugse Brouwerij BV)** _(boekhoudkundig-bedrag)_
- Balans Brugse Brouwerij BV op datum van aankoop → **Eigen vermogen totaal** _(boekhoudkundig-bedrag)_
- Aandelenkoopovereenkomst → **Belangenpercentage moeder** _(percentage)_

**📤 Output**:
- Geconsolideerde balans → **Deelnemingen** _(geëlimineerde-post)_
- Geconsolideerde balans → **Consolidatieverschillen** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Zoek in de balans van Aurelia Holding NV de post 'Deelnemingen' voor Brugse Brouwerij BV (bv. € 1.600.000).
2. Zoek in de balans van Brugse Brouwerij BV op datum van aankoop het eigen vermogen totaal (kapitaal + reserves + overgedragen resultaat — bv. € 1.500.000).
3. Bereken jouw aandeel: belangenpercentage × eigen vermogen dochter (80 % × € 1.500.000 = € 1.200.000).
4. Schrap € 1.600.000 (deelneming bij moeder) en schrap € 1.200.000 (jouw aandeel in EV dochter).
5. Boek het verschil € 1.600.000 − € 1.200.000 = € 400.000 als 'Consolidatieverschillen' (actiefzijde als positief, passiefzijde als negatief).
6. Belangrijk: gebruik het eigen vermogen op de datum van aankoop, niet op afsluitingsdatum.


> [!example]- Voorbeeld: Aurelia Holding NV koopt op 1 januari 20X1 een belang van 80 % in Brugse Brouwerij BV voor € 1.600.000
> Aurelia Holding NV koopt op 1 januari 20X1 een belang van 80 % in Brugse Brouwerij BV voor € 1.600.000. Eigen vermogen van Brugse Brouwerij BV op die datum: € 1.500.000.
>
> 1. **Vertrekpunt: balans Aurelia Holding vóór consolidatie** 📊
>
>    | Aurelia Holding NV — Activa            | Bedrag (€) |
>    |----------------------------------------|-----------:|
>    | Vaste activa (zonder deelneming)       |  5.000.000 |
>    | **Deelneming (Brugse Brouwerij BV)**   | **1.600.000** |
>    | Vlottende activa                       |  4.000.000 |
>    | **Totaal**                             | **10.600.000** |
>
> 2. **Balans Brugse Brouwerij BV op datum van aankoop** 📊
>
>    | Brugse Brouwerij BV — Passiva | Bedrag (€) |
>    |-------------------------------|-----------:|
>    | Kapitaal                      |  1.000.000 |
>    | Reserves                      |    500.000 |
>    | **Eigen vermogen totaal**     | **1.500.000** |
>    | Schulden aan derden           |  4.000.000 |
>    | **Totaal**                    | **5.500.000** |
>
> 3. **Berekening consolidatieverschil** 🧮
>
>    Aandeel Aurelia in eigen vermogen Brugse Brouwerij = 80 % × € 1.500.000 = **€ 1.200.000**
>    Aanschaffingswaarde deelneming                       =              = **€ 1.600.000**
>    Consolidatieverschil                                  = € 1.600.000 − € 1.200.000 = **€ 400.000** (positief, actiefzijde)
>

**Grondslag**: KB WVV art. 3:127, a) jo. art. 3:129

### 3. Reken het verschil eerst toe aan onder- of overgewaardeerde posten

Vóór je het hele verschil onder 'Consolidatieverschillen' boekt, kijk je of bepaalde bezittingen of schulden van de dochter méér of minder waard zijn dan hun boekwaarde. Reken het verschil zoveel mogelijk daaraan toe. Pas het overschot komt onder 'Consolidatieverschillen'.

**Waarom?** De boekwaarde uit de dochter-balans is niet altijd de werkelijke waarde. Een vastgoed dat 50 jaar geleden is gekocht staat boekhoudkundig laag; de werkelijke waarde is hoger. Door eerst die verborgen meerwaarde te erkennen, vermijd je dat het hele verschil onterecht goodwill (consolidatieverschil) wordt.

**📥 Input**:
- Consolidatieverschil uit stap 2 → **bedrag** _(boekhoudkundig-bedrag)_
- Balans dochter → **Posten met afwijkende werkelijke waarde** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans → **Geherwaardeerde activa/passiva van dochter** _(nieuwe-balanspost)_
- Geconsolideerde balans → **Consolidatieverschillen (overschot)** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Maak een lijst van bezittingen/schulden van Brugse Brouwerij BV waarvan de werkelijke waarde afwijkt van de boekwaarde (typisch: vastgoed, voorraden, voorzieningen).
2. Trek voor elke post de boekwaarde af van de werkelijke waarde — dat is de onder- of overwaardering.
3. Reken (een deel van) het consolidatieverschil toe aan die posten — opwaardering bij meerwaarde, afwaardering bij minderwaarde.
4. Het stuk dat overblijft, boek je definitief als 'Consolidatieverschillen' (positief → actiefzijde; negatief → passiefzijde).
5. Belangrijke regel: positieve en negatieve consolidatieverschillen van verschillende dochters mag je niet tegen elkaar wegstrepen, behalve binnen dezelfde dochter (dan moet het).


**Grondslag**: KB WVV art. 3:130 (lid 1 toerekening, lid 2 restant)

### 4. Schrap intragroep-vorderingen, schulden en winsten

Verwijder alle vorderingen en schulden tussen moeder en dochter (en tussen dochters onderling). Verwijder ook de winst die de groep aan zichzelf heeft 'verkocht' (intra-groep-winst in voorraden of vaste activa). Idem voor onderlinge opbrengsten en kosten in de resultatenrekening.

**Waarom?** Een groep kan niet aan zichzelf verkopen of zichzelf geld lenen — economisch is dat één bedrijf. Als je die posten zou laten staan, blaast de geconsolideerde balans onterecht op.

**📥 Input**:
- Boekhouding moeder en dochter → **Onderlinge vorderingen, schulden, verkopen, aankopen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans → **Onderlinge posten** _(geëlimineerde-post)_
- Geconsolideerde resultatenrekening → **Onderlinge opbrengsten en kosten** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Maak een lijst van alle bedragen die Aurelia Holding NV nog van Brugse Brouwerij BV te ontvangen heeft (en omgekeerd).
2. Schrap die bedragen wederzijds: vordering bij moeder weg én schuld bij dochter weg, voor hetzelfde bedrag.
3. Voor goederen die de moeder aan de dochter heeft verkocht (of omgekeerd): bepaal hoeveel daarvan nog in de voorraad of vaste activa zit, en schrap de winstmarge die de groep aan zichzelf heeft toegerekend.
4. In de resultatenrekening: schrap de onderlinge omzet en de onderlinge aankoopkosten — voor exact hetzelfde bedrag.
5. Praktische uitzondering: posten van te verwaarlozen betekenis mag je laten staan (KB WVV art. 3:139).


**Grondslag**: KB WVV art. 3:134 (balans), art. 3:136 (resultatenrekening), art. 3:139 (materialiteit)

### 5. Zet het aandeel van derden apart

Bereken welk deel van het eigen vermogen en het resultaat van de dochter toebehoort aan andere aandeelhouders dan de moeder. Presenteer dat bedrag apart: op de balans als 'Belangen van derden' aan passiefzijde, op de resultatenrekening als 'Aandeel van derden in het resultaat'.

**Waarom?** Bij integrale consolidatie heb je de 100 %-balans van de dochter opgenomen, maar economisch heeft de moeder maar 80 % (of welk percentage ook). Het verschil tussen die 100 % en het belangenpercentage hoort niet aan de moeder toe — dat moet de geconsolideerde jaarrekening transparant tonen.

**📥 Input**:
- Eigen vermogen dochter op afsluitingsdatum → **totaal** _(boekhoudkundig-bedrag)_
- Resultaat dochter boekjaar → **winst of verlies** _(boekhoudkundig-bedrag)_
- Aandelenstructuur → **Belangenpercentage moeder** _(percentage)_

**📤 Output**:
- Geconsolideerde balans (passiefzijde) → **Belangen van derden** _(nieuwe-balanspost)_
- Geconsolideerde resultatenrekening → **Aandeel van derden in het resultaat** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Neem het eigen vermogen totaal van Brugse Brouwerij BV op afsluitingsdatum (bv. € 2.000.000).
2. Bereken het derden-percentage: 100 % − belangenpercentage moeder (bv. 100 % − 80 % = 20 %).
3. Vermenigvuldig: 20 % × € 2.000.000 = € 400.000 → boek dit als 'Belangen van derden' aan passiefzijde van de geconsolideerde balans.
4. Doe hetzelfde voor het resultaat: 20 % × € 500.000 = € 100.000 → boek dit als 'Aandeel van derden in het resultaat' onderaan de resultatenrekening (RR).
5. Het resultaat dat overblijft voor de moeder (80 % × € 500.000 = € 400.000) zit dan al impliciet in het geconsolideerde nettoresultaat na aftrek van het derden-aandeel.


**Grondslag**: KB WVV art. 3:137

**Voorbeeld**: Aurelia Holding NV bezit 80 % van de stemrechten en het kapitaal van Brugse Brouwerij BV. Op acquisitiedatum: aanschaffingswaarde aandelen = € 1.600.000; eigen vermogen Brugse = € 1.500.000; geen onder-/overwaarderingen. Balans Brugse bij afsluiting jaar 1: activa € 3.000.000, schulden aan derden € 1.000.000, eigen vermogen € 2.000.000 (waarvan resultaat boekjaar € 500.000). Aurelia heeft een vordering op Brugse van € 250.000 (Brugse dus een schuld van € 250.000 aan Aurelia).

```
Stap 1: integrale opname. Activa geconsolideerd = activa Aurelia + € 3.000.000 (Brugse, 100 %). Schulden geconsolideerd = schulden Aurelia + € 1.000.000 (Brugse, 100 %).
Stap 2: compensatie. Boekwaarde aandelen (€ 1.600.000) − aandeel Aurelia in EV op acquisitiedatum (80 % × € 1.500.000 = € 1.200.000) = positief consolidatieverschil van € 400.000; geboekt onder 'Consolidatieverschillen' actiefzijde (KB WVV art. 3:130) en afgeschreven over passend plan (KB WVV art. 3:131).
Stap 3: eliminatie van de onderlinge vordering/schuld € 250.000: de vordering van Aurelia en de schuld van Brugse worden allebei geschrapt; geconsolideerde activa en schulden dalen elk met € 250.000.
Stap 4: aandeel van derden. Eigen vermogen Brugse op afsluitingsdatum = € 2.000.000; aandeel van derden in EV = 20 % × € 2.000.000 = € 400.000 (post 'Belangen van derden', passiefzijde). Resultaat Brugse = € 500.000; aandeel van derden in resultaat = 20 % × € 500.000 = € 100.000 (post 'Aandeel van derden in het resultaat').
```

Resultaat: In de geconsolideerde balans staan de € 3.000.000 activa en € 1.000.000 schulden van Brugse voor 100 % opgenomen (na eliminatie van € 250.000 intragroep); 'Consolidatieverschillen' = € 400.000 (actief); 'Belangen van derden' = € 400.000 (passief). In de geconsolideerde resultatenrekening wordt het volledige resultaat van Brugse meegenomen, met € 100.000 afzonderlijk gepresenteerd als 'Aandeel van derden in het resultaat'. Het deel dat aan Aurelia toekomt: 80 % × € 500.000 = € 400.000.

## In de praktijk

<h3 id="wanneer-toepassen">Wanneer toepassen</h3>

> [!tip]- Wanneer toepassen
> Integrale consolidatie is verplicht voor exclusief gecontroleerde dochters die in de consolidatiekring zitten (KB WVV art. 3:124, 1°). Bij consortium-leden is integrale consolidatie ook van toepassing op de leden zelf (samenlezing WVV art. 3:24 en KB WVV art. 3:124, 1°). ⚖️

> [!tip]- Herkennen op het examen
> Stemrechten > 50 % → integraal (tenzij uitgesloten of in feite-controle die het getrouwe beeld zou aantasten).

<h3 id="eigen-aandelen-van-de-consoliderende-vennootschap">Eigen aandelen van de consoliderende vennootschap</h3>

> [!tip]- Eigen aandelen van de consoliderende vennootschap
> Eigen aandelen van de consoliderende vennootschap (én aandelen in de consoliderende vennootschap die door een in de consolidatie opgenomen dochter worden gehouden) worden in de geconsolideerde balans geboekt onder actiefpost IX. De toelichting vermeldt hoeveel aandelen aldus in bezit zijn. ⚖️


## Voorwaarden / uitzonderingen

- Er moet exclusieve controle bestaan over de dochteronderneming (controle in rechte of in feite, exclusief uitgeoefend door één moedervennootschap). ⚖️
- De dochter behoort tot de consolidatiekring (geen uitsluiting op grond van KB WVV art. 3:97-3:99). ⚖️
> [!info]- Niet verwarren met [[evenredige-consolidatie]]
> Integrale consolidatie neemt 100 % van activa/passiva op (met aandeel van derden afzonderlijk) — voor exclusief gecontroleerde dochters. Evenredige consolidatie neemt activa/passiva op naar rato van de kapitaaldeelname (zonder afzonderlijke
>
> _Trigger_: Soort controle / type relatie tussen moeder en dochter bepaalt welke methode.

> [!info]- Niet verwarren met [[vermogensmutatiemethode]]
> Integrale consolidatie neemt de individuele activa/passiva op (regel voor regel). Vermogensmutatie behoudt de deelneming als één post 'Vennootschappen waarop vermogensmutatie is toegepast' (geherwaardeerd naar het pro-rata aandeel in het ei
>
> _Trigger_: Soort controle / type relatie tussen moeder en dochter bepaalt welke methode.


## Valkuilen

> [!warning]- De compensatie van de deelneming gebeurt op verwervingsdatum, niet op afsluitingsdatum
> ⚠️ De compensatie van de deelneming gebeurt op verwervingsdatum, niet op afsluitingsdatum. Het eigen vermogen op verwervingsdatum bevriest; latere wijzigingen in het eigen vermogen van de dochter worden behandeld als geconsolideerde reserves of resultaat — niet als toename of afname van het consolidatieverschil. ⚖️
>
> _Bron: KB WVV art. 3:129_


> [!warning]- Bij eerste consolidatie van een vennootschap kan de compensatie ten belope van de aandelen in haar bezit op die datum gebeuren op de aanvang…
> ⚠️ Bij eerste consolidatie van een vennootschap kan de compensatie ten belope van de aandelen in haar bezit op die datum gebeuren op de aanvangsdatum van het boekjaar (KB WVV art. 3:129, b)). Dit is een uitzondering die in de toelichting kan worden gemotiveerd. ⚖️
>
> _Bron: KB WVV art. 3:129, b)_


> [!warning]- De weglatingen van KB WVV art. 3:134 en 3:136 mogen achterwege blijven 'wanneer de betrokken bedragen, gelet op het doel van artikel 3:105,…
> ⚠️ De weglatingen van KB WVV art. 3:134 en 3:136 mogen achterwege blijven 'wanneer de betrokken bedragen, gelet op het doel van artikel 3:105, slechts van te verwaarlozen betekenis zijn' (KB WVV art. 3:138 jo. art. 3:139). Praktisch beoordelen op materialiteit. ⚖️
>
> _Bron: KB WVV art. 3:139_



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
