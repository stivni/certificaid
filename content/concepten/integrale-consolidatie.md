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
schema_version: '1.2'
gegenereerd_uit: data/concepten/records/integrale-consolidatie.json
gegenereerd_op: '2026-05-15'
---
# Integrale consolidatie ⚖️

> De geconsolideerde jaarrekening voorstellen alsof het geheel van de consoliderende vennootschap en haar exclusief gecontroleerde dochterondernemingen één enkele economische entiteit vormt. De activa, passiva, rechten, verplichtingen, opbrengsten en kosten van de moeder en van haar exclusief gecontroleerde dochters worden integraal opgenomen (voor 100 %); het deel dat toebehoort aan derden (minderheidsaandeelhouders) wordt afzonderlijk gepresenteerd in 'Belangen van derden' (balans) en 'Aandeel van derden in het resultaat' (resultatenrekening).
>
> _Bron: KB WVV art. 3:123 jo. art. 3:124, 1°_


## Bouwstenen

- **Integrale opname (KB WVV art. 3:126)**: Alle actief- en passiefbestanddelen van de consoliderende vennootschap en van de in de consolidatie opgenomen dochterondernemingen worden in de geconsolideerde balans opgenomen. ⚖️
- **Compensatie van de deelneming (KB WVV art. 3:127, a))**: De boekwaarde van de aandelen van de dochteronderneming wordt gecompenseerd met het deel van het eigen vermogen van de dochter dat door die aandelen wordt vertegenwoordigd, op de datum waarop de aandelen werden verworven (of nabijzijnde datum, KB WVV art. 3:129). ⚖️
- **Toerekening van het compensatieverschil en consolidatieverschil (KB WVV art. 3:130)**: Het verschil uit de compensatie wordt zoveel mogelijk toegerekend aan actief- en passiefbestanddelen waarvan de waarde hoger of lager is dan hun boekwaarde bij de dochter. Het overblijvende verschil wordt geboekt onder 'Consolidatieverschillen' (actiefzijde indien positief, passiefzijde indien negatief). Positieve en negatieve consolidatieverschillen mogen niet worden gecompenseerd, behalve indien ze betrekking hebben op dezelfde dochter (in dat geval verplicht). ⚖️
- **Eliminatie van onderlinge vorderingen/schulden en interne winsten (KB WVV art. 3:134, 3:136)**: Uit de geconsolideerde balans worden weggelaten: onderlinge vorderingen en schulden tussen consoliderende vennootschap en in de consolidatie opgenomen dochters; in activa begrepen winsten/verliezen uit intra-groepsverkopen. Uit de geconsolideerde resultatenrekening worden onderlinge opbrengsten/kosten weggelaten. ⚖️
- **Afzondering van het aandeel van derden (KB WVV art. 3:137)**: Het gedeelte van het resultaat van de volledig geconsolideerde dochters dat kan worden toegerekend aan aandelen gehouden door andere personen dan de consoliderende vennootschap of de in de consolidatie opgenomen dochters, wordt onder 'Aandeel van derden in het resultaat' vermeld. Op de balans verschijnen deze als 'Belangen van derden' aan passiefzijde. ⚖️

## Berekening

### Integrale consolidatie — werkstroom (compensatie + eliminatie + minderheidsbelang)

**Formule**: `Geconsolideerde post = (post moeder) + (post dochter × 100 %) − intragroep-eliminaties; Aandeel derden = (1 − belang%) × eigen vermogen of resultaat dochter`

*De moeder controleert de dochter en de groep wordt gepresenteerd als één economische entiteit. Bezittingen en schulden vloeien voor 100 % door; het derden-deel wordt op de passiefzijde van de balans als 'Belangen van derden' afgezonderd zodat de geconsolideerde gegevens transparant blijven.*

**Stappen**:
1. {'volgorde': 1, 'text': 'Neem alle actief- en passiefbestanddelen van moeder en dochter volledig op in de geconsolideerde balans (KB WVV art. 3:126).'}
2. {'volgorde': 2, 'text': 'Compenseer de boekwaarde van de deelneming met het overeenkomstig deel van het eigen vermogen van de dochter op verwervingsdatum (KB WVV art. 3:127, a)).'}
3. {'volgorde': 3, 'text': "Reken het verschil zoveel mogelijk toe aan onder-/overgewaardeerde actief-/passiefbestanddelen (KB WVV art. 3:130, lid 1); het overblijvende verschil wordt 'Consolidatieverschillen' (KB WVV art. 3:130, lid 2)."}
4. {'volgorde': 4, 'text': 'Elimineer onderlinge vorderingen/schulden en intra-groepswinsten/-verliezen in voorraad of activa (KB WVV art. 3:134); elimineer onderlinge opbrengsten/kosten (KB WVV art. 3:136).'}
5. {'volgorde': 5, 'text': "Bereken en presenteer het aandeel van derden in het eigen vermogen (balans, 'Belangen van derden') en in het resultaat (resultatenrekening, 'Aandeel van derden in het resultaat') voor het deel (1 − belang%) (KB WVV art. 3:137)."}

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


## Vergelijkingsparen

| Verwarrend met | Verschil | Trigger |
|---|---|---|
| [[evenredige-consolidatie]] | Integrale consolidatie neemt 100 % van activa/passiva op (met aandeel van derden afzonderlijk) — voor exclusief gecontroleerde dochters. Evenredige consolidatie neemt activa/passiva op naar rato van de kapitaaldeelname (zonder afzonderlijke post 'aandeel van derden' want het deel buiten de groep wordt gewoon niet opgenomen) — voor gemeenschappelijke dochters. | Soort controle: exclusief → integraal; gezamenlijk → evenredig. |
| [[vermogensmutatiemethode]] | Integrale consolidatie neemt de individuele activa/passiva op (regel voor regel). Vermogensmutatie behoudt de deelneming als één post 'Vennootschappen waarop vermogensmutatie is toegepast' (geherwaardeerd naar het pro-rata aandeel in het eigen vermogen). Integraal → controle; vermogensmutatie → invloed van betekenis (of uitgesloten dochter). | — |
| [[consolidatieverschil]] | Integrale consolidatie genereert vaak een consolidatieverschil bij de eerste opname (verschil tussen aanschaffingswaarde van de deelneming en het overeenkomstige deel van het eigen vermogen van de dochter). Dit verschil is een gevolg van de techniek, niet de techniek zelf. | — |
| [[minderheidsbelangen]] | Minderheidsbelangen ('Belangen van derden' op de balans, 'Aandeel van derden in het resultaat' op de resultatenrekening) zijn typische posten die uitsluitend bij integrale consolidatie ontstaan — bij evenredige consolidatie wordt het derden-deel gewoon niet opgenomen, dus is er geen aparte derden-post. | — |

## Valkuilen

- ⚠️ De compensatie van de deelneming gebeurt op verwervingsdatum, niet op afsluitingsdatum. Het eigen vermogen op verwervingsdatum bevriest; latere wijzigingen in het eigen vermogen van de dochter worden behandeld als geconsolideerde reserves of resultaat — niet als toename of afname van het consolidatieverschil. ⚖️
- ⚠️ Bij eerste consolidatie van een vennootschap kan de compensatie ten belope van de aandelen in haar bezit op die datum gebeuren op de aanvangsdatum van het boekjaar (KB WVV art. 3:129, b)). Dit is een uitzondering die in de toelichting kan worden gemotiveerd. ⚖️
- ⚠️ De weglatingen van KB WVV art. 3:134 en 3:136 mogen achterwege blijven 'wanneer de betrokken bedragen, gelet op het doel van artikel 3:105, slechts van te verwaarlozen betekenis zijn' (KB WVV art. 3:138 jo. art. 3:139). Praktisch beoordelen op materialiteit. ⚖️

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
