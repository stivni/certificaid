---
title: Kiezen van de toe te passen consolidatietechniek per entiteit
tags:
- competentie
- po-1-4
programmaonderdelen:
- '1.4'
status: voorgesteld
schema_version: '1.0'
gegenereerd_uit: data/concepten/competenties/kiezen-consolidatiemethode.yaml
gegenereerd_op: '2026-05-15'
---
# Kiezen van de toe te passen consolidatietechniek per entiteit

**⚖️ 80% · 🤖 20%** · Status: `voorgesteld`

> De koppeling kwalificatie → techniek is wettelijk: KB WVV art. 3:124 e.v. dwingt integrale consolidatie voor dochters, evenredige voor gemeenschappelijke dochters, vermogensmutatie voor geassocieerden; alleen 'nauwe integratie' van een gemeenschappelijke dochter is een beoordelingselement.

## Aanbevolen werkwijze

### 1. Vaststellen van de kwalificatie van de entiteit

📥 **Input**: Uitkomst van [[competenties/kwalificeren-relatie-deelneming|kwalificeren relatie deelneming]]: dochter, gemeenschappelijke dochter, geassocieerde onderneming, of gewone deelneming
📤 **Output**: Eén kwalificatie per entiteit in de consolidatiekring
**Waarom**: De kwalificatie bepaalt mechanisch welke consolidatietechniek wettelijk vereist is.
**Grondslag**: 🤖 Beroepspraktijk — Pre-requisite — voorafgaande competentie.
### 2. Toepassen integrale consolidatie op exclusief gecontroleerde dochters

📥 **Input**: Lijst van dochters waarover exclusieve controle bestaat en die in de consolidatiekring zitten
📤 **Output**: Beslissing om de activa, passiva, rechten, verplichtingen, opbrengsten en kosten voor 100 % op te nemen, met afzondering van het deel dat toebehoort aan derden als 'Belangen van derden' (balans) en 'Aandeel van derden in het resultaat' (resultatenrekening)
**Waarom**: Integrale consolidatie geeft het beeld 'alsof het geheel één enkele onderneming was' en is de standaardtechniek voor exclusieve dochters.
**Grondslag**: [[integrale-consolidatie]]
### 3. Toepassen evenredige consolidatie op gemeenschappelijke dochterondernemingen

📥 **Input**: Lijst van gemeenschappelijke dochters; beoordeling of het bedrijf nauw geïntegreerd is in dat van de consoliderende vennootschap
📤 **Output**: Beslissing om de activa, passiva, opbrengsten en kosten pro-rata (volgens belang in kapitaal of inbreng) op te nemen — zonder afzondering van aandeel van derden — TENZIJ de gemeenschappelijke dochter niet nauw geïntegreerd is, in welk geval de vermogensmutatiemethode wordt toegepast
**Waarom**: Evenredige consolidatie weerspiegelt het gezamenlijke karakter van de controle; bij gebrek aan operationele integratie volstaat de vermogensmutatie.
**Grondslag**: [[evenredige-consolidatie]]
- ⚠️ **Bij evenredige consolidatie moet een 'aandeel van derden' worden geboekt voor het deel buiten de groep.** → Bij evenredige consolidatie wordt enkel het pro-rata deel opgenomen; er is geen aandeel van derden omdat het derden-deel niet wordt opgenomen. ([[evenredige-consolidatie]])
### 4. Toepassen vermogensmutatiemethode op geassocieerde ondernemingen en bepaalde dochters

📥 **Input**: Lijst van geassocieerde ondernemingen; gemeenschappelijke dochters zonder nauwe integratie; dochters uitgesloten op grond van KB WVV art. 3:98 (controle in feite indruisend tegen getrouw beeld) of art. 3:99 (geen going concern)
📤 **Output**: Beslissing om de deelneming als één gesynthetiseerde balanspost op te nemen, initieel tegen het pro-rata aandeel in het eigen vermogen op verwervingsdatum (met eventueel consolidatieverschil), en jaarlijks aangepast voor het pro-rata aandeel in de wijzigingen in dat eigen vermogen
**Waarom**: Vermogensmutatie weerspiegelt de invloed (niet de controle) over het netto-actief en het resultaat van de geassocieerde onderneming.
**Grondslag**: [[vermogensmutatiemethode]]
### 5. Toepassen horizontale consolidatie bij een consortium

📥 **Input**: Vaststelling dat het om een consortium gaat (zonder moeder-dochter-relatie tussen de leden, maar onder centrale leiding)
📤 **Output**: Beslissing om: (a) voor elk consortiumlid eerst een verticale consolidatie uit te voeren volgens de gebruikelijke technieken voor hun eigen dochters; (b) vervolgens de verticaal geconsolideerde cijfers van alle consortiumleden integraal samen te voegen via horizontale consolidatie, met behoud van het karakter van de eigen-vermogenposten per lid
**Waarom**: Bij een consortium ontbreekt een verticale moeder; de geconsolideerde jaarrekening wordt gezamenlijk opgesteld via horizontale samenvoeging.
**Grondslag**: [[horizontale-consolidatie]]

## Beslisboom

**Is er een consortium (horizontale groep)?**
- Ja: Horizontale consolidatie (voor elk lid eerst verticaal, dan samenvoegen). Stop hier voor de keuze.
- Nee: Ga per entiteit naar volgende vraag.

**Bestaat exclusieve controle?**
- Ja: Integrale consolidatie.
- Nee: Ga naar volgende vraag.

**Bestaat gezamenlijke controle en is het bedrijf nauw geïntegreerd?**
- Ja: Evenredige consolidatie.
- Nee: Bestaat gezamenlijke controle maar zonder nauwe integratie, of invloed van betekenis? → Vermogensmutatie.

**Werd de dochter uitgesloten op grond van KB WVV art. 3:98 of art. 3:99?**
- Ja: Toch opnemen via vermogensmutatie (KB WVV vereist dit).
- Nee: —


## Voorbeelden

**Situatie**: Moeder M bezit 100 % van D1 (exclusieve controle); 50 % van D2 onder aandeelhoudersovereenkomst met een vennoot die de andere 50 % bezit, met nauwe integratie in M's bedrijfsactiviteit; 25 % van D3 met bestuursvertegenwoordiging.

**Conclusie**: D1 wordt integraal geconsolideerd; D2 wordt evenredig geconsolideerd (50 %); D3 wordt opgenomen via vermogensmutatie.

**Grondslag**: [[integrale-consolidatie]] §exclusieve controle; [[evenredige-consolidatie]] §gezamenlijke controle + nauwe integratie; [[vermogensmutatiemethode]] §geassocieerde onderneming

**Redenering**: De kwalificatie van elke entiteit dwingt mechanisch een techniek af; voor D2 vereist nauwe integratie evenredige consolidatie eerder dan vermogensmutatie.

---
**Situatie**: Vennootschap X bezit 100 % van X1 (verticale moeder-dochter); X en Y staan onder centrale leiding van drie natuurlijke personen (consortium).

**Conclusie**: X voert eerst een verticale integrale consolidatie uit (X + X1); vervolgens worden (X + X1) en Y horizontaal samengevoegd via integrale consolidatie, met behoud van het eigen-vermogenkarakter per consortiumlid.

**Grondslag**: [[horizontale-consolidatie]] §stappen; [[consortium]] §gezamenlijke plicht

**Redenering**: Het consortium triggert horizontale consolidatie; eigen dochters van een lid worden eerst verticaal verwerkt voordat de horizontale samenvoeging plaatsvindt.

---

## Gebaseerd op concepten

[[integrale-consolidatie]] · [[evenredige-consolidatie]] · [[vermogensmutatiemethode]] · [[horizontale-consolidatie]] · [[dochteronderneming]] · [[gemeenschappelijke-dochteronderneming]] · [[geassocieerde-onderneming]] · [[consortium]] · 
## Voortkomend uit

**Taken**: 1.4.taak.1**Kenniselementen**: 1.4.I.D, 1.4.I.E, 1.4.I.B, 1.4.II.C