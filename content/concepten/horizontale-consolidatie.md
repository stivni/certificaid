---
title: Horizontale consolidatie
tags:
- concept
- procedure
- po-1-4
linked_anchors:
- 1.4.I.C
- 1.4.I.B
- 1.4.I.D
- 1.4.II.B
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: grounded
node_type: procedure
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/horizontale-consolidatie.json
gegenereerd_op: '2026-05-16'
---
# Horizontale consolidatie ⚖️

> [!summary] Korte inhoud
> De consolidatietechniek die je toepast wanneer vennootschappen onder gemeenschappelijke leiding staan zonder dat één rechtspersoon de andere controleert — een consortium.

> [!info] Behoort tot: [[consortium]] · [[consolidatiemethodes-vergelijking]]

De consolidatietechniek die je toepast wanneer vennootschappen onder gemeenschappelijke leiding staan zonder dat één rechtspersoon de andere controleert — een consortium. De leden van het consortium en hun eigen dochters worden via integrale consolidatie samengevoegd (KB WVV art. 3:124, 1° jo. WVV art. 3:24). De posten van het eigen vermogen blijven per lid zichtbaar (beschikbare/onbeschikbare reserves behouden hun karakter — WVV art. 3:30, § 2).

_Bron: CBN 2022/09 — Consolidatie bij de horizontale groep (consortium)_


## In de praktijk

<h3 id="voorrang-van-verticale-consolidatie">Voorrang van verticale consolidatie</h3>

> [!tip]- Voorrang van verticale consolidatie
> Het begrip 'consortium' is uitgesloten zodra twee of meer vennootschappen al in een verticale moeder-dochter-relatie staan met elkaar of met een gemeenschappelijke moeder. Zo voorkomt de wet dat dezelfde groep zowel verticaal als horizontaal wordt opgesteld. Eerst de verticale check, dan eventueel horizontaal. ⚖️

> [!tip]- Herkennen op het examen
> Examen-zin 'Aurelia is dochter van Antwerpse én partner in consortium met Cardinal' → geen consortium — gewoon verticale consolidatie Aurelia+Antwerpse; Cardinal apart.

<h3 id="geen-moeder-gezamenlijke-verantwoordelijkheid">Geen moeder, gezamenlijke verantwoordelijkheid</h3>

> [!tip]- Geen moeder, gezamenlijke verantwoordelijkheid
> Anders dan bij verticale consolidatie is er bij een consortium geen 'moeder'. De leden van het consortium maken samen de geconsolideerde jaarrekening op, laten ze controleren en publiceren ze. De centrale leider — vaak een natuurlijke persoon zoals Pieter Vermeulen of een private stichting — moet zelf géén geconsolideerde jaarrekening opstellen (CBN 2022/09 — voorbeeld 7). ⚖️


## Stappen

### 1. Harmoniseer de waarderingsregels van alle leden

Voer aanpassingsboekingen uit zodat alle consortium-leden hun balans en resultatenrekening volgens dezelfde waarderingsregels opstellen.

**Waarom?** Als de leden verschillende waarderingsregels hanteren (bv. lineair vs. degressief afschrijven, FIFO vs. gewogen gemiddelde), zou de samenvoeging niet zinvol zijn — appels en peren bij elkaar.

**📥 Input**:
- Waarderingsregels van Industria Antwerpen NV → **Set toegepaste regels** _(document)_
- Waarderingsregels van Jachthaven Jezus-Eik NV → **Set toegepaste regels** _(document)_

**📤 Output**:
- Geharmoniseerde balansen per lid → **Aangepaste boekwaarden** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Vergelijk de waarderingsregels van Industria Antwerpen NV en Jachthaven Jezus-Eik NV per balanspost (afschrijvingen, voorraden, voorzieningen).
2. Spreek één gezamenlijke set af voor de geconsolideerde jaarrekening (CBN 2022/09 — stap 1).
3. Voor leden die afwijken: bereken de impact van de overstap en boek de aanpassing in een werkpapier (niet in de individuele jaarrekening).
4. Documenteer de afwijking in de toelichting bij de geconsolideerde jaarrekening.


**Grondslag**: KB WVV art. 3:118 (uniformiteit waarderingsregels) jo. CBN 2022/09 stap 1

### 2. Doe per lid eerst de verticale consolidatie

Heeft een consortium-lid zelf dochters? Doe dan voor dat lid eerst de verticale (gewone) consolidatie: integraal voor exclusief gecontroleerde dochters, evenredig voor gemeenschappelijke dochters, vermogensmutatie voor geassocieerde ondernemingen.

**Waarom?** Anders zou je de derden-belangen in de dochters van een lid verkeerd behandelen. Je horizontaliseert pas wat al netjes verticaal opgesteld is.

**📥 Input**:
- Balans + resultatenrekening lid + zijn dochters → **Alle posten** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Verticaal geconsolideerde jaarrekening per lid → **Tussenresultaat** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Inventariseer per consortium-lid de eigen dochters.
2. Voor elke groep lid+dochters: voer de procedure integrale consolidatie uit (zie [[integrale-consolidatie]]).
3. Heeft een lid een gemeenschappelijke dochter? → evenredige consolidatie. Een geassocieerde? → vermogensmutatie.
4. Het resultaat per lid is een 'verticaal geconsolideerde jaarrekening van dat lid'.
5. Pas in stap 3 voeg je die per-lid-jaarrekeningen samen.


**Grondslag**: CBN 2022/09 — Verticale consolidatie voorafgaand aan horizontale

### 3. Voeg de cijfers van alle leden samen voor 100 %

Tel de (eventueel verticaal geconsolideerde) cijfers van alle consortium-leden post per post op. Activa, schulden, rechten, verplichtingen, opbrengsten en kosten worden voor 100 % per lid opgenomen — net als bij integrale consolidatie.

**Waarom?** Het consortium wordt voor het cijferbeeld als één economische entiteit gepresenteerd. Pro-rata-opname zou de schaal van de groep verbergen.

**📥 Input**:
- Verticaal geconsolideerde jaarrekening per lid → **Alle posten** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Horizontaal geconsolideerde balans → **Samengevoegde posten** _(nieuwe-balanspost)_
- Horizontaal geconsolideerde resultatenrekening → **Samengevoegde opbrengsten/kosten** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Neem de balans van Industria Antwerpen NV (eventueel verticaal geconsolideerd).
2. Neem de balans van Jachthaven Jezus-Eik NV (eventueel verticaal geconsolideerd).
3. Tel post per post de bedragen op: vaste activa Industria + vaste activa Jachthaven, vlottende activa, schulden, opbrengsten, kosten.
4. Het eigen vermogen wordt apart behandeld in stap 4 — niet zomaar optellen.
5. Idem voor de resultatenrekening: tel de bedrijfsopbrengsten en -kosten samen, met behoud van vergelijkbare presentatie.


> [!example]- Voorbeeld: Industria Antwerpen NV en Jachthaven Jezus-Eik NV vormen een consortium onder leiding van Pieter Vermeulen
> Industria Antwerpen NV en Jachthaven Jezus-Eik NV vormen een consortium onder leiding van Pieter Vermeulen.
>
> 1. **Balans Industria Antwerpen NV** 📊
>
>    | Industria Antwerpen NV — Activa  | Bedrag (€) |
>    |----------------------------------|-----------:|
>    | Vaste activa                     |  4.000.000 |
>    | Vlottende activa                 |  3.000.000 |
>    | **Totaal**                       | **7.000.000** |
>
> 2. **Balans Jachthaven Jezus-Eik NV** 📊
>
>    | Jachthaven Jezus-Eik NV — Activa | Bedrag (€) |
>    |----------------------------------|-----------:|
>    | Vaste activa                     |  2.500.000 |
>    | Vlottende activa                 |  2.000.000 |
>    | **Totaal**                       | **4.500.000** |
>
> 3. **Horizontaal geconsolideerde balans (vóór intragroep-eliminaties)** 📊
>
>    | Geconsolideerde balans — Activa            | Bedrag (€) |
>    |--------------------------------------------|-----------:|
>    | Vaste activa (Industria + Jachthaven)      |  6.500.000 |
>    | Vlottende activa (Industria + Jachthaven)  |  5.000.000 |
>    | **Totaal**                                 | **11.500.000** |
>

**Grondslag**: KB WVV art. 3:124, 1° jo. WVV art. 3:24

### 4. Houd de aard van het eigen vermogen per lid zichtbaar

Voeg de eigen-vermogensposten van Industria Antwerpen NV en Jachthaven Jezus-Eik NV samen, maar houd het bedrag dat aan elk lid toebehoort apart zichtbaar onder dezelfde posten van het eigen vermogen. Beschikbare reserves van een lid blijven beschikbaar; onbeschikbare blijven onbeschikbaar.

**Waarom?** Het consortium kent geen 'moeder' die het eigen vermogen samentrekt; elke aandeelhouder houdt rechten op zijn eigen lid. De aard van die rechten (uitkeerbaar of niet) moet daarom transparant blijven (WVV art. 3:30, § 2).

**📥 Input**:
- Eigen vermogen Industria Antwerpen NV → **Kapitaal + reserves + overgedragen resultaat** _(boekhoudkundig-bedrag)_
- Eigen vermogen Jachthaven Jezus-Eik NV → **Idem** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerd eigen vermogen → **Per consortium-lid + per posttype** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Maak een tabel met de eigen-vermogensposten per lid (kapitaal, herwaarderingsmeerwaarden, beschikbare reserves, onbeschikbare reserves, overgedragen resultaat).
2. Tel de bedragen per posttype op, maar splits in de toelichting per consortium-lid.
3. Bewaak: een onbeschikbare reserve van Jachthaven mag niet plots als beschikbaar verschijnen.
4. Vermeld in de toelichting hoeveel van elke post toe te rekenen is aan elk lid (transparantie).


**Grondslag**: WVV art. 3:30, § 2

### 5. Schrap intra-groeptransacties tussen leden onderling en met hun dochters

Verwijder alle wederzijdse vorderingen, schulden, verkopen, aankopen, intra-groepswinsten in voorraden of vaste activa tussen consortium-leden onderling én tussen leden en hun dochters.

**Waarom?** Het consortium is voor het cijferbeeld één entiteit; transacties binnen die entiteit zijn economisch geen echte transacties.

**📥 Input**:
- Boekhouding leden + dochters → **Onderlinge vorderingen, schulden, verkopen, aankopen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans en RR → **Onderlinge posten** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Inventariseer alle bedragen die Industria Antwerpen NV nog te ontvangen heeft van Jachthaven Jezus-Eik NV (en omgekeerd), en idem met hun dochters.
2. Schrap die bedragen wederzijds: vordering bij lid 1 weg én schuld bij lid 2 weg, voor hetzelfde bedrag.
3. Bij onderlinge verkopen: bepaal hoeveel van de verkochte goederen nog in voorraad zit en schrap de winstmarge.
4. In de resultatenrekening: schrap de onderlinge omzet en de onderlinge aankoopkosten voor exact hetzelfde bedrag.
5. Praktische uitzondering: posten van te verwaarlozen betekenis mag je laten staan (KB WVV art. 3:139).


**Grondslag**: KB WVV art. 3:134 (balans), art. 3:136 (resultatenrekening)


> [!info]- Niet verwarren met [[integrale-consolidatie]]
> Horizontale consolidatie gebruikt de techniek van integrale consolidatie maar past die toe op een horizontale groep (consortium) in plaats van op een verticale moeder-dochter-relatie. Geen moeder, geen aandeel van derden tussen de leden onderling; wel mogelijk binnen verticale subgroepen onder een lid.
>
> _Trigger_: Het type relatie (verticaal vs. horizontaal) bepaalt of je het integrale-consolidatie-recept op een moeder + haar dochters toepast (verticaal) of op een set zelfstandige consortium-leden onder gemeenschappelijke leiding (horizontaal).


## Valkuilen

> [!warning]- Een consortium-lid dat zelf dochters heeft, moet eerst verticaal consolideren v…
> ⚠️ Een consortium-lid dat zelf dochters heeft, moet eerst verticaal consolideren vooraleer aan de horizontale samenvoeging deel te nemen. Wie deze volgorde omkeert, krijgt incorrecte resultaten omdat de derden-belangen in de dochters van een lid anders verkeerd worden behandeld. Bv. Industria Antwerpen NV met dochter Brugse Brouwerij BV (80 %): eerst Industria+Brugse verticaal consolideren (incl. 20 % belangen van derden), dan pas horizontaal samenvoegen met Jachthaven Jezus-Eik NV. ⚖️
>
> _Bron: CBN 2022/09 — verticale voorafgaand aan horizontale_



## Zie ook

- **Getriggerd door**: [[consortium]]
- **Vereist kennis van**: [[integrale-consolidatie]]

## Bronnen

[^1]: `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_consolidatiemethode`
[^2]: `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_verticale-consolidatie-voorafgaand-aan-de-horizontale-consol`
[^3]: `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_voorbeeld-1`
[^4]: `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_consolidatieverplichting-consoliderende-vennootschap`
[^5]: `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_voorbeeld-7`
[^6]: `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_horizontale-groep`
