---
title: Signaleren van oprichtersaansprakelijkheid-risico's aan de cliënt
tags:
- concept
- competentie
- po-3-0
linked_anchors:
- 3.0.taak.1
- 3.0.VII
programmaonderdelen:
- '3.0'
confidence: inferred
node_type: competentie
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/signaleren-oprichtersaansprakelijkheid-risico.json
gegenereerd_op: '2026-05-20'
---
# Signaleren van oprichtersaansprakelijkheid-risico's aan de cliënt 🤖

Adviescompetentie: vóór de notariële akte de cliënt schriftelijk informeren over de drie hoofdgronden van oprichtersaansprakelijkheid (kennelijk ontoereikend aanvangsvermogen, kennelijke overwaardering inbreng in natura, onjuiste of ontbrekende akte-vermeldingen) en hoe het ontwerp van akte + financieel plan deze risico's afdekt. Doel: cliënt maakt geïnformeerde keuze; accountant bouwt dossier op tegen latere claims van onvoldoende advies.


## In de praktijk

- Een schriftelijke aansprakelijkheidsnota is geen verplichting volgens WVV — maar wel volgens accountantsplichtenleer-praktijk en is essentieel voor latere zelfverdediging.
- Het 3-jaars venster voor 'kennelijk ontoereikend' loopt vanaf verkrijging rechtspersoonlijkheid (datum akte), niet vanaf start operationele activiteit.
- Een revisorenverslag voor inbreng in natura ontheft de oprichter NIET van aansprakelijkheid — het is een waarderings-validatie, geen aansprakelijkheidsdekking.

## Stappen

### 1. Inventariseren van de drie hoofdgronden van oprichtersaansprakelijkheid

Loop systematisch de aansprakelijkheidsgronden uit art. 5:16 (BV) / 7:18 (NV) na: (a) onjuistheid/ontbrekende vermeldingen, (b) kennelijke overwaardering inbreng in natura, (c) faillissement binnen 3 jaar bij kennelijk ontoereikend aanvangsvermogen.

**Waarom?** Elke grond werkt apart en heeft eigen verdedigingsstrategie. Cliënt moet alle drie kennen, niet alleen de meest besproken (kennelijk ontoereikend aanvangsvermogen).

**📥 Input**:
- Concept-akte + concept financieel plan + revisorenverslag → **Volledig oprichtingsdossier** _(tekst-document)_

**📤 Output**:
- Aansprakelijkheids-checklist per grond → **Status per grond + mitigering** _(tabel)_

**🛠️ Hoe**:

1. Voor 'onjuiste/ontbrekende vermeldingen' (art. 5:16 1°, 7:18 1° eerste lid):
   - Loop checklist art. 2:8 §2 + 5:11-5:12 (BV) / 7:13-7:14 (NV) af.
   - Voor elke verplichte vermelding: aanwezig + juist?
   - Risico-niveau: laag bij volledige akte + geverifieerde gegevens.
2. Voor 'kennelijke overwaardering inbreng in natura' (art. 5:16 1° tweede lid, 7:18 1° tweede lid):
   - Voor elke inbreng in natura: revisorenverslag aanwezig?
   - Waardering conservatief gemotiveerd?
   - Risico-niveau: laag bij goed-onderbouwd revisor-werk, hoog bij IP/handelsfonds-waarderingen zonder marktverwijzing.
3. Voor 'kennelijk ontoereikend aanvangsvermogen' (art. 5:16 2°, 7:18 2°):
   - Faillissement binnen 3 jaar mogelijk?
   - Financieel plan onderbouwd? Buffer aanwezig?
   - Risico-niveau: hoog bij krappe financiering + optimistische projectie; laag bij ruime financiering + conservatieve hypothesen.

**Grondslag**: [[oprichtersaansprakelijkheid]]; WVV art. 5:16, 7:18

### 2. Beoordelen specifieke risico-trigger 'kennelijk ontoereikend'

Voer een gedetailleerde analyse uit van de financiering vs. de verwachte cashbehoefte over de eerste 24 maanden — om te toetsen of het aanvangsvermogen 'kennelijk' onvoldoende is.

**Waarom?** Dit is de meest voorkomende grond in praktijk. 'Kennelijk' is geen exacte juridische drempel maar wordt door rechters ingevuld op basis van het financieel plan op moment van oprichting.

**📥 Input**:
- Financieel plan (zie [[opstellen-financieel-plan-oprichting]]) → **Volledige projectie** _(tekst-document)_

**📤 Output**:
- Risico-oordeel 'kennelijk ontoereikend' → **Laag / midden / hoog + onderbouwing** _(tekst-document)_

**🛠️ Hoe**:

1. Bereken EV / verwachte gemiddelde maandelijkse cashbehoefte → maanden 'buffer'.
2. Buffer < 3 maanden = HOOG risico.
3. Buffer 3-6 maanden = MIDDEN — alleen acceptabel met sterke argumentatie.
4. Buffer > 6 maanden = LAAG.
5. Combineer met sector-specifieke risico: hoge debiteurendoorlooptijd, voorraadintensief, hoge CAPEX-fase → buffer-eis hoger.
6. Test scenario-analyse: bij −20% omzet jaar 1, gaat cash dan onder nul?
7. Documenteer het oordeel met cijfermatige onderbouwing.

**Grondslag**: [[kennelijk-ontoereikend-aanvangsvermogen]]; WVV art. 5:16 2°, 7:18 2°

> [!warning]- 'Kennelijk' is geen statische cijfer-drempel — rechter beoordeelt achteraf. Conservatief plannen biedt de beste verdediging.
>
> _Vaak fout gedaan_: Denken dat een minimum-bedrag (bv. 'minstens € 18.600' uit oude regelgeving) voldoende is — dit cijfer bestaat sinds WVV 2019 niet meer als minimum-kapitaal voor BV.

### 3. Schriftelijk informeren van de cliënt

Stel een schriftelijke aansprakelijkheidsnota op die de drie gronden, het risico-niveau per grond, de mitigerende maatregelen in het huidig dossier, en de resterende restrisico's expliciet aan de cliënt presenteert.

**Waarom?** Schriftelijke informatie + bevestiging van ontvangst beschermt de accountant tegen latere claim 'ik was niet gewaarschuwd'. Voor cliënt verlaagt het de informatie-asymmetrie zodat oprichting bewust gebeurt.

**📥 Input**:
- Aansprakelijkheids-checklist (stap 1) + risico-oordeel (stap 2) → **Aggregate beoordeling** _(tekst-document)_

**📤 Output**:
- Aansprakelijkheidsnota aan cliënt + ontvangstbevestiging → **Gestructureerde brief** _(tekst-document)_

**🛠️ Hoe**:

1. Open de nota met situering: 'Onderstaande informeert u over de aansprakelijkheidsrisico's verbonden aan uw oprichting.'
2. Voor elke grond:
   - Wat is het risico (één paragraaf)?
   - Welke voorwaarden moeten cumulatief vervuld zijn voor activering?
   - Hoe is het risico in uw dossier afgedekt (verwijzing naar plan, revisor, akte)?
   - Welk restrisico blijft?
3. Sluit af met aanbeveling indien risico-niveau MIDDEN of HOOG: 'Wij adviseren ... vóór ondertekening akte.'
4. Vraag cliënt om de nota voor akkoord af te tekenen.
5. Bewaar de getekende kopie in cliëntdossier — bescherming tegen latere claim.

**Grondslag**: Plichtenleer accountancy; KB van 1 maart 1998

### 4. Bijsturen oprichtingsdossier op basis van risico-feedback

Wanneer een grond MIDDEN of HOOG scoort: stel een concreet bijsturings-traject voor (extra kapitaal, krediet vóór akte, conservatievere waardering inbreng, extra akte-clausule).

**Waarom?** Risico-signalering zonder voorstel-tot-mitigering is half werk. De accountant is adviseur, niet alleen informant.

**📥 Input**:
- Aansprakelijkheidsnota (stap 3) → **Risico-oordeel per grond** _(tekst-document)_

**📤 Output**:
- Mitigatie-voorstellen → **Aanbevelingen per grond met MIDDEN/HOOG-risico** _(tekst-document)_

**🛠️ Hoe**:

1. Voor 'kennelijk ontoereikend' MIDDEN/HOOG:
   - Stel voor: extra EV-inbreng, of LT-krediet vóór akte zekerstellen, of conservatievere projectie + plan-herziening.
2. Voor 'kennelijke overwaardering' MIDDEN/HOOG:
   - Stel voor: tweede onafhankelijke waardering, of waardering met expliciete down-side bandbreedte, of inbrengwaarde naar beneden bijstellen.
3. Voor 'onjuiste vermeldingen' MIDDEN/HOOG:
   - Stel voor: extra review-cyclus akte-ontwerp, of notaris vragen om specifieke clausule te dubbel-checken.
4. Bespreek met cliënt + beslis samen welke mitigatie wordt toegepast — niet alles is altijd nodig, het is een afweging.

**Grondslag**: Plichtenleer; vakpraktijk


## Voorbeelden




