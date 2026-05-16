---
title: Kwalificeren van de relatie met een deelneming (controle, gezamenlijke controle
  of invloed van betekenis)
tags:
- competentie
- po-1-4
programmaonderdelen:
- '1.4'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/kwalificeren-relatie-deelneming.yaml
gegenereerd_op: '2026-05-16'
---
# Kwalificeren van de relatie met een deelneming (controle, gezamenlijke controle of invloed van betekenis)

**⚖️ 75% · 🤖 25%**

> De drempelvermoedens (> 50 %, 50/50 met overeenkomst, ≥ 20 %) zijn wettelijk vastgelegd in WVV art. 1:14-1:22. Controle-in-feite en het weerleggen van het 20 %-vermoeden vergen feitelijke beoordeling.

## Aanbevolen werkwijze

### 1. Vaststellen van het stemrechtpercentage

Bereken het direct en indirect aangehouden stemrechtpercentage in de doelvennootschap.

**Waarom?** Het stemrechtpercentage is het vertrekpunt voor alle wettelijke vermoedens.

**📥 Input**:
- Aandelenregister van doelvennootschap → **Aandelen per aandeelhouder** _(document)_
- Statuten van doelvennootschap → **Aandelen met meervoudig stemrecht, eigen aandelen** _(document)_
- Stemafspraken in aandeelhoudersovereenkomsten → **Bindende stemafspraken** _(document)_

**📤 Output**:
- Werkpapier kwalificatie → **Stemrechtpercentage moeder (direct + indirect)** _(percentage)_

**🛠️ Hoe**:

1. Open het aandelenregister van Drukkerij Dendermonde BV.
2. Bereken het stemrechtpercentage van Antwerpse Investments NV — niet het aandeel in het kapitaal, maar in de stemrechten.
3. Corrigeer voor aandelen met meervoudig stemrecht en eigen aandelen (die hebben geen stemrecht in de AV).
4. Voeg indirect gehouden stemrechten toe via gecontroleerde tussenschakels (gebruik de keten-regels uit [[berekenen-controle-en-belangenpercentage]]).
5. Noteer het eindresultaat als startpunt voor stap 2-4.


**Grondslag**: [[controlepercentage]] §berekening, WVV art. 1:14

### 2. Toetsen of er exclusieve controle bestaat

Ga na of de moeder exclusieve controle in rechte of in feite uitoefent.

**Waarom?** Bij exclusieve controle is de doelvennootschap een dochter en moet zij integraal worden geconsolideerd.

**📥 Input**:
- Stemrechtpercentage uit stap 1 → **Percentage** _(percentage)_
- Statuten + aandeelhoudersovereenkomsten → **Benoemingsrechten, vetorechten** _(document)_
- Notulen laatste twee algemene vergaderingen (AV) → **Aanstelling bestuurders** _(document)_

**📤 Output**:
- Werkpapier kwalificatie → **Ja/nee exclusieve controle + grondslag** _(conclusie)_

**🛠️ Hoe**:

1. Toets het onweerlegbaar vermoeden: > 50 % stemrechten? → exclusieve controle in rechte, ga naar stap 5.
2. Statutaire of contractuele benoemingsmacht? → exclusieve controle in rechte.
3. Geen drempel gehaald? Open de notulen van de laatste twee AV's van de doelvennootschap.
4. Heeft de moeder met haar effectieve stemrechten op twee opeenvolgende AV's de meerderheid van bestuurders aangesteld? → controle in feite (zie [[exclusieve-controle]] §controle-in-feite).
5. Conclusie: exclusieve controle → dochter → integrale consolidatie (zie [[kiezen-consolidatiemethode]] stap 2).


**Grondslag**: [[exclusieve-controle]] §soorten, WVV art. 1:14 en 1:15

> [!warning]- Toets ook controle in feite — controle vereist niet altijd meer dan 50 %.
>
> _Vaak fout gedaan_: Aannemen dat 49 % stemrechten nooit controle oplevert.
>
> _Grondslag_: [[exclusieve-controle]] §controle-in-feite

### 3. Toetsen of er gezamenlijke controle bestaat

Ga na of een beperkt aantal vennoten samen controle uitoefent op basis van een aandeelhoudersovereenkomst.

**Waarom?** Bij gezamenlijke controle is de doelvennootschap een gemeenschappelijke dochter en wordt zij evenredig geconsolideerd (of via vermogensmutatie indien niet nauw geïntegreerd).

**📥 Input**:
- Aandeelhoudersovereenkomsten → **Vereiste van gemeenschappelijke instemming voor beleidsbeslissingen** _(document)_

**📤 Output**:
- Werkpapier kwalificatie → **Ja/nee gezamenlijke controle** _(conclusie)_

**🛠️ Hoe**:

1. Open de aandeelhoudersovereenkomst tussen Cardinal Group NV en Energiehuis Evergem BV met betrekking tot Filmstudio Florence BV.
2. Zoek de clausule over beleidsbeslissingen: wordt 'gemeenschappelijke instemming' of 'unanimiteit' vereist?
3. Ja → gezamenlijke controle, onweerlegbaar vermoeden (WVV art. 1:18).
4. Nee, zelfs niet impliciet → geen gezamenlijke controle. Filmstudio is dan geen gemeenschappelijke dochter; mogelijk wel geassocieerde (ga naar stap 4).


**Grondslag**: [[gezamenlijke-controle]] §kwalificatie, WVV art. 1:18

> [!warning]- Zonder schriftelijke afspraak over gemeenschappelijke instemming is er geen gezamenlijke controle.
>
> _Vaak fout gedaan_: Aannemen dat een 50/50-deelneming automatisch gezamenlijke controle oplevert.
>
> _Grondslag_: [[gezamenlijke-controle]] §overeenkomst-vereiste

### 4. Toetsen of er invloed van betekenis bestaat

Ga na of de moeder zonder controle wel invloed van betekenis uitoefent — weerlegbaar vermoeden vanaf 20 % stemrechten.

**Waarom?** Bij invloed van betekenis (zonder controle) is de doelvennootschap een geassocieerde onderneming en wordt zij via vermogensmutatie opgenomen.

**📥 Input**:
- Stemrechtpercentage uit stap 1 → **Percentage** _(percentage)_
- Samenstelling bestuursorgaan van doelvennootschap → **Bestuurders aangesteld door of in vertegenwoordiging van moeder** _(document)_
- Beleidsdocumenten + transactieoverzicht → **Deelname aan beleid, materiële transacties, technologische uitwisseling** _(document)_

**📤 Output**:
- Werkpapier kwalificatie → **Ja/nee invloed van betekenis** _(conclusie)_

**🛠️ Hoe**:

1. Toets eerst het 20 %-vermoeden: bezit Antwerpse Investments NV ≥ 20 % stemrechten in Drukkerij Dendermonde BV?
2. Ja → vermoeden invloed van betekenis. Bekijk of er weerleggende elementen zijn: geen vertegenwoordiging in bestuur, geen deelname aan beleid, geen materiële transacties.
3. Geen weerlegging? → invloed van betekenis bevestigd, Drukkerij Dendermonde is geassocieerde onderneming.
4. < 20 % maar duidelijke invloed via bestuursvertegenwoordiging en deelname aan strategische beslissingen? → invloed van betekenis kan toch bestaan.
5. Volg [[invloed-van-betekenis]] §indicatoren voor de toetsing.


> [!example]- Voorbeeld: Antwerpse Investments NV verwerft 25 % van Drukkerij Dendermonde BV. Drukkerij Dendermonde stelt een vertegenwoordiger v…
> Antwerpse Investments NV verwerft 25 % van Drukkerij Dendermonde BV. Drukkerij Dendermonde stelt een vertegenwoordiger van Antwerpse aan in haar bestuursorgaan. Antwerpse neemt deel aan strategische beslissingen.
>
> 1. **Toets aan 20 %-vermoeden** 🧮
>
>    Stemrechtpercentage Antwerpse in Drukkerij Dendermonde = 25 %
>    25 % ≥ 20 % → vermoeden invloed van betekenis bevestigd.
>    
>
> 2. **Aanvullende indicatoren** 💬
>
>    - Vertegenwoordiging in bestuursorgaan: ja
>    - Deelname aan beleidsbeslissingen: ja
>    - Materiële transacties: niet vermeld
>    Conclusie: vermoeden niet weerlegd, integendeel versterkt. Drukkerij Dendermonde BV is geassocieerde onderneming van Antwerpse Investments NV.
>    
>
> 3. **Gevolg voor consolidatie** 💬
>
>    Drukkerij Dendermonde wordt opgenomen volgens de vermogensmutatiemethode (zie [[kiezen-consolidatiemethode]] stap 4).
>    
>

**Grondslag**: [[invloed-van-betekenis]] §kwalificatie, WVV art. 1:22

> [!warning]- Het 20 %-vermoeden is weerlegbaar; toets ook de feitelijke indicatoren.
>
> _Vaak fout gedaan_: Bij precies 20 % automatisch tot invloed van betekenis besluiten, zonder de feiten te toetsen.
>
> _Grondslag_: [[invloed-van-betekenis]] §weerlegbaarheid

### 5. Formuleren van de eindkwalificatie

Stel de finale kwalificatie van de relatie op basis van stappen 2-4.

**Waarom?** Deze kwalificatie is noodzakelijke input voor [[kiezen-consolidatiemethode]].

**📥 Input**:
- Werkpapier kwalificatie → **Resultaten stappen 2-4** _(conclusie)_

**📤 Output**:
- Eindkwalificatie → **Dochter / gemeenschappelijke dochter / geassocieerde / gewone deelneming** _(conclusie)_

**🛠️ Hoe**:

1. Combineer de resultaten:
   - Exclusieve controle → dochteronderneming.
   - Gezamenlijke controle → gemeenschappelijke dochteronderneming.
   - Invloed van betekenis → geassocieerde onderneming.
   - Geen van bovenstaande → gewone deelneming (opname tegen aanschaffingswaarde, geen consolidatie).
2. Documenteer in het werkpapier: kwalificatie + grondslag (wettekst + concept-link).
3. Geef de kwalificatie door aan [[kiezen-consolidatiemethode]].


**Grondslag**: [[controle]] §kwalificatie-overzicht (praktijk-synthese)


## Voorbeelden

> [!example]- Cardinal Group NV en Energiehuis Evergem BV bezitten elk 50 % van Filmstudio Florence BV. Geval 1: zij hebben een aandee…
> **Conclusie**: Geval 1: gezamenlijke controle → Filmstudio is gemeenschappelijke dochter van Cardinal en Energiehuis. Geval 2: noch Cardinal noch Energiehuis heeft controle. Filmstudio kan kwalificeren als geassocieerde (mits invloed van betekenis bewezen).
>
> **Grondslag**: [[gezamenlijke-controle]] §overeenkomst-vereiste; [[geassocieerde-onderneming]] §20-%-vermoeden
>
> **Redenering**: De overeenkomst is de wettelijke voorwaarde voor gezamenlijke controle. Zonder overeenkomst kan Filmstudio enkel via vermogensmutatie behandeld worden als invloed van betekenis bewezen is.

> [!example]- Antwerpse Investments NV verwerft 20 % in Drukkerij Dendermonde BV. Drukkerij Dendermonde heeft Antwerpse in haar bestuu…
> **Conclusie**: Antwerpse heeft invloed van betekenis over Drukkerij Dendermonde. Drukkerij Dendermonde is een geassocieerde onderneming en wordt via vermogensmutatie opgenomen.
>
> **Grondslag**: [[invloed-van-betekenis]] §weerlegbaar-vermoeden-vanaf-20-percent; [[geassocieerde-onderneming]] §kwalificatie
>
> **Redenering**: Het 20 %-vermoeden wordt versterkt door bestuursvertegenwoordiging en deelname aan beleidsbeslissingen — kenmerkende aanwijzingen van invloed van betekenis.


## Gebaseerd op concepten

[[controle]] · [[exclusieve-controle]] · [[gezamenlijke-controle]] · [[invloed-van-betekenis]] · [[dochteronderneming]] · [[geassocieerde-onderneming]] · [[gemeenschappelijke-dochteronderneming]] · 
## Voortkomend uit

- **Taken**: 1.4.taak.1
- **Kenniselementen**: 1.4.I.C, 1.4.I.B, 1.4.I.D, 1.4.I.E, 1.4.II.B
