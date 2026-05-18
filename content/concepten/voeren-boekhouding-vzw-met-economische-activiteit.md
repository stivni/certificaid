---
title: Voeren van de boekhouding van een VZW met economische activiteit
tags:
- concept
- competentie
- po-1-1
linked_anchors:
- 1.1.taak.1
- 1.1.I.A
- 1.1.II
programmaonderdelen:
- '1.1'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/voeren-boekhouding-vzw-met-economische-activiteit.json
gegenereerd_op: '2026-05-18'
---
# Voeren van de boekhouding van een VZW met economische activiteit 🤖


## Stappen

### 1. Bepaal het VZW-regime (microvereniging / klein / groot)

Toets de VZW aan de groottecriteria die het boekhoudregime bepalen.

**Waarom?** Microvereniging mag vereenvoudigd boekhouden; kleine en grote VZW's moeten dubbel boekhouden volgens VZW-rekeningstelsel.

**📥 Input**:
- Statuten + financiële cijfers vorig boekjaar → **Omzet, balanstotaal, personeel-equivalent** _(document)_

**📤 Output**:
- Werknotitie classificatie → **Regime + drempels-toets** _(conclusie)_

**🛠️ Hoe**:

1. Toets drempels uit KB-WVV art. 3:47 en CBN 2020/15 — zie [[jaarrekening-vzw-stichting]] §groottecriteria:
   - Microvereniging: ontvangsten ≤ € 334.500 EN balanstotaal ≤ € 1.337.000 EN personeel ≤ 5 voltijdse.
   - Kleine VZW: niet micro + niet groot.
   - Grote VZW: minstens 2 van 3 criteria overschreden: ontvangsten > € 9.000.000, balans > € 4.500.000, personeel > 50.
2. Bij VZW Quelle de Vie — ontvangsten € 280.000 (lidgelden + cursussen) + subsidies € 95.000 = totaal € 375.000; balans € 215.000; personeel 2 voltijdse → niet micro (ontvangsten > drempel), wel klein → dubbele boekhouding.
3. Documenteer in cliëntdossier.


**Grondslag**: [[jaarrekening-vzw-stichting]] §groottecriteria, KB-WVV art. 3:47

### 2. Pas het VZW-rekeningstelsel toe

Gebruik het specifieke VZW-rekeningenplan met aangepaste rubrieken voor bijdragen, schenkingen, subsidies en VZW-eigen vermogen.

**Waarom?** Het VZW-stelsel verschilt van het ondernemings-MAR op enkele rubrieken die de specificiteit van een vereniging weerspiegelen.

**📥 Input**:
- VZW-rekeningstelsel (KB 19/12/2003 + KB-WVV-aanpassingen) → **Volledige lijst rekeningen** _(document)_

**📤 Output**:
- Aangepast VZW-rekeningenplan → **Rekeningen + sub-rekeningen** _(document)_

**🛠️ Hoe**:

1. Centrale VZW-eigenheden volgens [[jaarrekening-vzw-stichting]] §rekeningenplan:
   - 10 Beginvermogen / fondsen — geen aandelenkapitaal, wel "fondsen van de vereniging".
   - 13 Bestemde fondsen — voor donaties met specifiek doel (bv. cursusprojecten).
   - 730/731 Lidgelden + bijdragen.
   - 736/737 Schenkingen + legaten.
   - 738 Subsidies (overheidstoelagen) — soms toegerekend pro-rata project.
   - 731 Sponsoring zonder economische tegenprestatie.
2. Volg voor klasse 6 grotendeels het MAR maar pas op voor analytische uitsplitsing per project.
3. Voor VZW Quelle de Vie — sub-rekeningen: 7301 Lidgelden 2026; 7361 Schenkingen privé; 7381 Subsidie Vlaamse Gemeenschap.


**Grondslag**: [[jaarrekening-vzw-stichting]] §rekeningenplan, KB 19/12/2003

### 3. Boek bijdragen, subsidies en schenkingen op de juiste rekeningen

Onderscheid duidelijk tussen lidgelden, vrije schenkingen en geconditioneerde subsidies.

**Waarom?** De onderscheid bepaalt of de opbrengst direct in het resultaat valt of via overlopende rekeningen wordt gespreid.

**📥 Input**:
- Stortingen + subsidie-besluiten + schenkingsovereenkomsten → **Bedragen + bedoeling + voorwaarden** _(document)_

**📤 Output**:
- Boekingen opbrengsten → **Per categorie op juiste rekening** _(boekingsregel)_

**🛠️ Hoe**:

1. Lidgelden: D 5500 Bank; C 730 Lidgelden — onmiddellijk opbrengst (geen prestatie tegenover).
2. Schenkingen vrij (geen voorwaarde): D 5500; C 736 Schenkingen.
3. Subsidies met voorwaarde (bv. project moet uitgevoerd worden): D 5500; C 4930 Over te dragen subsidies — bij voltooiing van project verschuiven naar 738.
4. Subsidies zonder voorwaarde (operationele toelage): D 5500; C 738 Operationele subsidies.
5. Legaten via 737 — meestal eenmalig.
6. Voor VZW Quelle de Vie — subsidie € 95.000 voor cursusproject 2026: boek op 4930 bij ontvangst; verschuif naar 738 pro-rata bij uitvoering.


> [!example]- Voorbeeld: VZW Quelle de Vie — januari 2026: lidgelden € 25.000, schenking privé € 8.000, subsidie Vlaamse Gemeenschap € 95.000 (ge…
> VZW Quelle de Vie — januari 2026: lidgelden € 25.000, schenking privé € 8.000, subsidie Vlaamse Gemeenschap € 95.000 (gekoppeld aan cursussen 2026).
>
> 1. **Boekingen ontvangsten januari** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 31/01/2026 | 5500 Bank | lidgelden | € 25.000,00 | |
>    | 31/01/2026 | 730 Lidgelden 2026 | -- | | € 25.000,00 |
>    | 31/01/2026 | 5500 Bank | schenking | € 8.000,00 | |
>    | 31/01/2026 | 736 Schenkingen | -- | | € 8.000,00 |
>    | 15/02/2026 | 5500 Bank | subsidie VG | € 95.000,00 | |
>    | 15/02/2026 | 4930 Over te dragen subsidies | nog te besteden | | € 95.000,00 |
>    
>
> 2. **Verschuiving van overlopende naar opbrengst (pro-rata)** 📝
>
>    Bij elke kwartaal-rapportering verschuif 25% van subsidie naar opbrengst:
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 31/03/2026 | 4930 Over te dragen subsidies | Q1 voltooid | € 23.750,00 | |
>    | 31/03/2026 | 738 Operationele subsidies | -- | | € 23.750,00 |
>    
>

**Grondslag**: [[jaarrekening-vzw-stichting]] §bijdragen-schenkingen-subsidies, CBN 2020/15

> [!warning]- Boek geconditioneerde subsidies eerst op overlopende rekening — vrijgeven aan opbrengst pas bij voldoen aan de voorwaarde.
>
> _Vaak fout gedaan_: Direct als opbrengst boeken in jaar van ontvangst, ook wanneer voorwaarden nog niet vervuld zijn.
>
> _Grondslag_: [[jaarrekening-vzw-stichting]] §subsidies-toerekenen

### 4. Verwerk economische activiteit + btw-plicht bij gemengde VZW

Wanneer de VZW economische activiteit ontplooit, gelden ook btw-verplichtingen + commerciële boekhouding voor dat deel.

**Waarom?** Een VZW met substantiële economische activiteit (verkoop boeken, cursussen tegen betaling) wordt btw-belastingplichtige; dat deel volgt het gewone aankoop-/verkoopdagboek-regime.

**📥 Input**:
- Activiteitenoverzicht → **Aandeel commerciële activiteit** _(document)_

**📤 Output**:
- Btw-aangifteplicht + pro-rata-aftrek → **Aankoop/verkoop met of zonder btw** _(boekingsregel)_

**🛠️ Hoe**:

1. Toets btw-status: VZW met "economisch zelfstandige activiteit" en omzet > € 25.000 (vrijstellingsregeling kleine ondernemingen) is btw-belastingplichtige voor het commerciële deel.
2. Bij Quelle de Vie — cursussen tegen betaling vormen commerciële activiteit; jaarlijkse cursus-omzet € 145.000 → btw-plichtig (21% op meeste cursussen, vrijstelling indien onderwijs strikt erkend).
3. Boek verkoop cursussen volgens competentie [[boeken-aankoop-verkoop-met-btw]] stap 3.
4. Pro-rata btw-aftrek op gemengde kosten (bv. kantoor): aandeel commerciële omzet / totale ontvangsten.
5. Subsidies en lidgelden zijn buiten btw-toepassing.


**Grondslag**: [[jaarrekening-vzw-stichting]] §gemengde-vzw, btw-wetboek art. 44

### 5. Maak de VZW-jaarrekening op en deponeer bij Nationale Bank

Stel de balans, resultatenrekening + sociale balans op volgens het VZW-schema en neerleg binnen de wettelijke termijn.

**Waarom?** Wettelijke neerleggingsplicht voor kleine en grote VZW's (microvereniging deponeert bij griffie); termijn 30 dagen na AV, AV binnen 6 maanden na boekjaar.

**📥 Input**:
- Proefbalans VZW → **Saldi per VZW-rekening** _(balans)_

**📤 Output**:
- VZW-jaarrekening + neerlegging → **Balans + resultatenrekening + bestemming** _(document)_

**🛠️ Hoe**:

1. Schema-keuze: microvereniging → vereenvoudigd schema bij griffie ondernemingsrechtbank; klein → verkort schema bij NBB; groot → volledig schema + commissarisverslag bij NBB.
2. Resultatenrekening VZW-presentatie: scheiding "Bedrijfsactiviteit" / "Financiële activiteit" / "Niet-recurrent" zoals onderneming, maar met VZW-eigen opbrengsten 730-738 in plaats van 70.
3. Bestemming resultaat (klasse 69/79 VZW): geen dividend mogelijk — saldo gaat naar overgedragen resultaat 14 of bestemde fondsen 13.
4. Voor Quelle de Vie (klein) — neerleggen verkort VZW-schema bij NBB binnen 30 dagen na AV (juni 2027).


**Grondslag**: [[jaarrekening-vzw-stichting]] §schema-en-neerlegging, [[jaarrekening]] §publicatieplicht


