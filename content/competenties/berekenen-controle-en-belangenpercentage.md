---
title: Berekenen van controle- en belangenpercentage in een ketenstructuur
tags:
- competentie
- po-1-4
programmaonderdelen:
- '1.4'
status: voorgesteld
schema_version: '1.0'
gegenereerd_uit: data/concepten/competenties/berekenen-controle-en-belangenpercentage.yaml
gegenereerd_op: '2026-05-15'
---
# Berekenen van controle- en belangenpercentage in een ketenstructuur

**⚖️ 60% · 🤖 40%** · Status: `voorgesteld`

> De definities en de drempel (> 50 %) zijn wettelijk; de rekenregels in ketens (controle-% niet vermenigvuldigen, belangen-% wél vermenigvuldigen) zijn praktijkconventies die in de CBN-doctrine en KB WVV-toepassing worden gehanteerd.

## Aanbevolen werkwijze

### 1. Tekenen van de aandeelhoudersketen

📥 **Input**: Aandeelhouderslijst per vennootschap in de groep, met stemrechtpercentage per directe deelneming
📤 **Output**: Schema van directe deelnemingen tussen alle relevante entiteiten (M → A → B → ...)
**Waarom**: Een correcte berekening vereist een visueel of tabellarisch overzicht van alle schakels.
**Grondslag**: 🤖 Beroepspraktijk — Werkmethodologische voorbereiding — geen aparte wettelijke regel.
### 2. Berekenen van het controlepercentage in elke schakel

📥 **Input**: Stemrechtpercentages per directe deelneming
📤 **Output**: Per schakel: controlepercentage = direct gehouden stemrechten + stemrechten die de moeder indirect controleert via dochters die zelf exclusieve controle hebben (NIET vermenigvuldigen)
**Waarom**: Zodra elke tussenschakel exclusieve controle heeft, telt het volledige stemrechtpercentage van de onderste schakel mee als 'gecontroleerd door de moeder'.
**Grondslag**: [[controlepercentage]]
- ⚠️ **Het controlepercentage wordt zoals het belangenpercentage vermenigvuldigd langs de keten.** → Het controlepercentage wordt NIET vermenigvuldigd: zolang elke schakel exclusieve controle heeft, telt het stemrechtpercentage van de onderste schakel volledig mee voor de moeder. ([[controlepercentage]])
### 3. Berekenen van het belangenpercentage in elke schakel

📥 **Input**: Belangenpercentages per directe deelneming (economisch eigendomsaandeel)
📤 **Output**: Per schakel: belangenpercentage = product van de belangenpercentages langs de keten (M → 80 % A → 60 % B = 0,80 × 0,60 = 48 %)
**Waarom**: Het economische eigendomsaandeel verdunt door tussenliggende derden en moet daarom worden vermenigvuldigd.
**Grondslag**: [[belangenpercentage]]
- ⚠️ **Het belangenpercentage en het controlepercentage zijn altijd gelijk.** → Ze kunnen verschillen: het belangenpercentage wordt vermenigvuldigd, het controlepercentage niet. Bij M → 80 % A → 60 % B is controle = 60 % (controle in elke schakel), belang = 48 %. ([[belangenpercentage]])
### 4. Toetsen of er in elke schakel exclusieve controle bestaat

📥 **Input**: Per schakel: controlepercentage > 50 % of andere onweerlegbare vermoedens
📤 **Output**: Per schakel: bevestiging of breuk in de controle-keten (waardoor het 'volledig meetellen' van de onderste schakel niet meer geldt)
**Waarom**: Indien een schakel geen exclusieve controle heeft, breekt de keten en moet het controlepercentage van de moeder over de onderste schakel opnieuw beoordeeld worden — vaak als geen-controle of als invloed van betekenis.
**Grondslag**: [[exclusieve-controle]]
### 5. Toepassen van het belangenpercentage in de consolidatieverwerking

📥 **Input**: Belangenpercentage per dochter (eventueel pro-rata bij gemeenschappelijke dochter)
📤 **Output**: Berekeningsbasis voor: aandeel van derden (1 − belang%) bij integrale consolidatie; pro-rata opname (belang%) bij evenredige consolidatie; pro-rata aandeel in eigen vermogen bij vermogensmutatie
**Waarom**: Het belangenpercentage is de rekenmaatstaf voor de bedragen die uiteindelijk in de geconsolideerde jaarrekening verschijnen.
**Grondslag**: [[belangenpercentage]]


## Voorbeelden

**Situatie**: Vennootschap M bezit 80 % van vennootschap A; A bezit 60 % van vennootschap B. In elke schakel bezit de bovenliggende vennootschap exclusieve controle in rechte (> 50 %).

**Conclusie**: Controlepercentage van M in B = 60 % (NIET vermenigvuldigen — elke schakel heeft exclusieve controle, dus 60 % telt volledig mee voor M). Belangenpercentage van M in B = 0,80 × 0,60 = 48 %.

**Grondslag**: [[controlepercentage]] §keten; [[belangenpercentage]] §keten

**Redenering**: Controlepercentage en belangenpercentage volgen verschillende rekenregels; M consolideert B integraal omdat zij via A exclusieve controle uitoefent, maar derden (52 %) wordt afgezonderd op basis van het belangenpercentage.

---
**Situatie**: M bezit 90 % van dochter D. D heeft een industriële activiteit, D's eigen vermogen op afsluitingsdatum = 1.000.

**Conclusie**: Belangenpercentage = 90 %; aandeel van derden = (1 − 0,90) × 1.000 = 100 (op de balans) en (1 − 0,90) × resultaat D in de resultatenrekening.

**Grondslag**: [[belangenpercentage]] §berekening aandeel van derden; [[minderheidsbelangen]] §formule

**Redenering**: Bij integrale consolidatie wordt 100 % van D opgenomen; het complement van het belangenpercentage bepaalt het deel dat als 'belangen van derden' wordt afgezonderd.

---

## Gebaseerd op concepten

[[controlepercentage]] · [[belangenpercentage]] · [[exclusieve-controle]] · [[controle]] · 
## Voortkomend uit

- **Taken**: 1.4.taak.1
- **Kenniselementen**: 1.4.I.C, 1.4.I.D, 1.4.I.E
