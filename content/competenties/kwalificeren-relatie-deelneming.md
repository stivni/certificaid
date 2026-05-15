---
title: Kwalificeren van de relatie met een deelneming (controle, gezamenlijke controle
  of invloed van betekenis)
tags:
- competentie
- po-1-4
programmaonderdelen:
- '1.4'
status: voorgesteld
schema_version: '1.0'
gegenereerd_uit: data/concepten/competenties/kwalificeren-relatie-deelneming.yaml
gegenereerd_op: '2026-05-15'
---
# Kwalificeren van de relatie met een deelneming (controle, gezamenlijke controle of invloed van betekenis)

**⚖️ 75% · 🤖 25%** · Status: `voorgesteld`

> De drempelvermoedens (> 50 %, 50/50 met overeenkomst, ≥ 20 %) zijn wettelijk vastgelegd in WVV art. 1:14-1:22, maar 'controle in feite' en het weerleggen van het 20 %-vermoeden vergen feitelijke beoordeling.

## Aanbevolen werkwijze

### 1. Vaststellen van het stemrechtpercentage

📥 **Input**: Aandelenstructuur, aandelen met meervoudig stemrecht, eigen aandelen, stemafspraken
📤 **Output**: Het direct en indirect aangehouden stemrechtpercentage in de doelvennootschap
**Waarom**: Het stemrechtpercentage is het vertrekpunt voor alle wettelijke vermoedens.
**Grondslag**: [[controlepercentage]]
### 2. Toetsen of er exclusieve controle bestaat

📥 **Input**: Stemrechtpercentage, statutaire of contractuele benoemingsrechten, stemafspraken, historiek van aanstellingen op de twee laatste algemene vergaderingen
📤 **Output**: Conclusie of er exclusieve controle in rechte (> 50 % stemrechten, statutaire macht, contractuele macht) of in feite (afgeleid uit het feitelijke aanstellingsgedrag op de twee laatste AV's) bestaat
**Waarom**: Bij exclusieve controle is de doelvennootschap een dochteronderneming en wordt zij integraal geconsolideerd.
**Grondslag**: [[exclusieve-controle]]
- ⚠️ **Met 49 % stemrechten bestaat nooit controle.** → Controle in feite kan met minder dan 50 % bestaan wanneer de vennootschap met haar effectieve stemrechten op twee opeenvolgende AV's de meerderheid van bestuurders heeft aangesteld. ([[exclusieve-controle]])
### 3. Toetsen of er gezamenlijke controle bestaat

📥 **Input**: Aandeelhoudersovereenkomsten of stemafspraken die bepalen dat beleidsbeslissingen alleen met gemeenschappelijke instemming worden genomen
📤 **Output**: Conclusie of er een beperkt aantal vennoten samen controle uitoefent op basis van een overeenkomst — onweerlegbaar vermoeden van controle door die vennoten
**Waarom**: Bij gezamenlijke controle is de doelvennootschap een gemeenschappelijke dochteronderneming en wordt zij evenredig geconsolideerd (of via vermogensmutatie indien niet nauw geïntegreerd).
**Grondslag**: [[gezamenlijke-controle]]
- ⚠️ **Zodra twee partijen elk 50 % bezitten, is er automatisch gezamenlijke controle.** → Gezamenlijke controle vereist een overeenkomst dat beleidsbeslissingen alleen met gemeenschappelijke instemming worden genomen; zonder overeenkomst is X géén dochter van A of B. ([[gezamenlijke-controle]])
### 4. Toetsen of er invloed van betekenis bestaat (geen controle)

📥 **Input**: Stemrechtpercentage, vertegenwoordiging in het bestuursorgaan, deelname aan beleidsbeslissingen, materiële transacties, technologische uitwisseling
📤 **Output**: Conclusie of er invloed van betekenis bestaat — weerlegbaar vermoeden vanaf 20 % stemrechten
**Waarom**: Bij invloed van betekenis (zonder controle) is de doelvennootschap een geassocieerde onderneming en wordt zij volgens de vermogensmutatiemethode opgenomen.
**Grondslag**: [[invloed-van-betekenis]]
- ⚠️ **Bij precies 20 % is er automatisch invloed van betekenis.** → Het vermoeden is weerlegbaar; bij gebrek aan vertegenwoordiging, geen deelname aan beleid en geen materiële transacties kan het vermoeden weerlegd worden. Omgekeerd kan invloed bestaan bij minder dan 20 % wanneer de feiten dit aantonen. ([[invloed-van-betekenis]])
### 5. Formuleren van de kwalificatie

📥 **Input**: Resultaten van stappen 2-4
📤 **Output**: Eén van: dochteronderneming (exclusieve controle), gemeenschappelijke dochteronderneming (gezamenlijke controle), geassocieerde onderneming (invloed van betekenis), of gewone deelneming (geen van bovenstaande)
**Waarom**: De kwalificatie is de noodzakelijke input voor de keuze van consolidatiemethode (zie [[competenties/kiezen-consolidatiemethode|kiezen consolidatiemethode]]).
**Grondslag**: 🤖 Beroepspraktijk — Synthese — de uitkomst is een combinatie van de voorgaande wettelijke toetsen.

## Beslisboom

**Heeft de vennootschap > 50 % stemrechten of een onweerlegbaar vermoeden van controle in rechte (statutair/contractueel/feitelijk via twee laatste AV's)?**
- Ja: Exclusieve controle → dochteronderneming.
- Nee: Ga naar volgende vraag.

**Is er een overeenkomst dat beleidsbeslissingen alleen met gemeenschappelijke instemming kunnen worden genomen?**
- Ja: Gezamenlijke controle → gemeenschappelijke dochteronderneming.
- Nee: Ga naar volgende vraag.

**Bedraagt het stemrechtpercentage ≥ 20 % of zijn er feitelijke aanwijzingen van invloed (bestuursvertegenwoordiging, deelname aan beleid)?**
- Ja: Invloed van betekenis → geassocieerde onderneming (mits niet weerlegd).
- Nee: Gewone deelneming — geen consolidatietechniek; opname tegen aanschaffingswaarde.


## Voorbeelden

**Situatie**: Vennootschap A en vennootschap B bezitten elk 50 % van vennootschap X. Geval 1: zij hebben een aandeelhoudersovereenkomst dat beleidsbeslissingen alleen samen worden genomen. Geval 2: er is geen overeenkomst.

**Conclusie**: Geval 1: gezamenlijke controle → X is gemeenschappelijke dochteronderneming van A en B. Geval 2: noch A noch B heeft controle; X kan kwalificeren als geassocieerde onderneming (mits invloed van betekenis).

**Grondslag**: [[gezamenlijke-controle]] §overeenkomst-vereiste; [[geassocieerde-onderneming]] §20 %-vermoeden

**Redenering**: De overeenkomst is de wettelijke voorwaarde voor gezamenlijke controle. Zonder overeenkomst kan X enkel via vermogensmutatie behandeld worden als de invloed van betekenis bewezen is.

---
**Situatie**: Onderneming ABC verwerft een belang van 20 % in onderneming DEF; DEF heeft ABC in haar bestuursorgaan opgenomen en ABC neemt deel aan strategische beslissingen.

**Conclusie**: ABC heeft invloed van betekenis over DEF; DEF is een geassocieerde onderneming en wordt via vermogensmutatie opgenomen.

**Grondslag**: [[invloed-van-betekenis]] §weerlegbaar vermoeden vanaf 20 %; [[geassocieerde-onderneming]] §kwalificatie

**Redenering**: Het 20 %-vermoeden wordt versterkt door de bestuursvertegenwoordiging en deelname aan beleidsbeslissingen — kenmerkende aanwijzingen van invloed van betekenis.

---

## Gebaseerd op concepten

[[controle]] · [[exclusieve-controle]] · [[gezamenlijke-controle]] · [[invloed-van-betekenis]] · [[dochteronderneming]] · [[geassocieerde-onderneming]] · [[gemeenschappelijke-dochteronderneming]] · 
## Voortkomend uit

**Taken**: 1.4.taak.1**Kenniselementen**: 1.4.I.C, 1.4.I.B, 1.4.I.D, 1.4.I.E, 1.4.II.B