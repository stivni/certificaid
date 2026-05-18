---
title: Gebruiken van financiële-analyse-software voor ratio-set en sectorvergelijking
tags:
- concept
- competentie
- po-1-9
linked_anchors:
- 1.9.taak.1
- 1.9.VII
- 1.9.VII.A
- 1.9.VII.B
- 1.9.VII.C
programmaonderdelen:
- '1.9'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/gebruiken-financiele-analyse-software.json
gegenereerd_op: '2026-05-18'
---
# Gebruiken van financiële-analyse-software voor ratio-set en sectorvergelijking 🤖

Operationele competentie: een gepaste tool kiezen (NBB-Online, Belfius Score, Graydon, ...), jaarrekeninggegevens importeren, automatisch berekende ratio-set lezen, sectorbenchmarking interpreteren en eindrapportage filteren op wat relevant is voor de specifieke analyse-vraag. Verantwoordelijk blijven voor selectie en interpretatie — software is geen black box.


## Stappen

### 1. Kiezen van een gepaste tool voor de analyse-vraag

Selecteer de geschikte financiële-analyse-software op basis van het type analyse — individuele onderneming, sectorvergelijking, kredietrating of going-concern-screening.

**Waarom?** Tools verschillen in scope en abonnementskost. NBB-Online is gratis voor individuele ondernemingen; Bel-First levert sector-databases; Graydon en Belfius Score focussen op kredietratings. Verkeerde keuze leidt tot ofwel onnodige kost ofwel ontbrekende functies.

**📥 Input**:
- Analyse-vraag van de cliënt → **Type opdracht (jaarrekening-analyse, kredietdossier, fusie/overname, going-concern-toets)** _(document)_

**📤 Output**:
- Tool-keuze → **Naam van tool + motivatie** _(conclusie)_

**🛠️ Hoe**:

1. Plaats de analyse-vraag in een van de vier categorieën uit [[financiele-analyse-software]] §belgische-marktspelers:
   - Individuele onderneming, ratio's + visualisatie → NBB-Online (gratis) of Bel-First.
   - Sectorvergelijking via NACE → Bel-First (uitgebreid).
   - Kredietrating + betaalmoraliteit → Graydon.
   - Banksector-screening kredietaanvraag → Belfius Score.
2. Controleer of de cliënt zelf een abonnement heeft of dat het kantoor zijn licentie inzet.
3. Bij twijfel: NBB-Online volstaat voor de meeste examen-relevante analyses.


**Grondslag**: [[financiele-analyse-software]] §belgische-marktspelers

### 2. Importeren van de jaarrekening

Laad de jaarrekening in de gekozen tool — manueel of via XBRL-import uit de NBB-Centrale voor Balansen.

**Waarom?** Tools steunen op de gestandaardiseerde NBB-rapportering. Manuele input is mogelijk voor niet-neergelegde rapporten (interne tussentijdse balansen) maar invoer-fouten kunnen de hele analyse vervuilen.

**📥 Input**:
- Jaarrekening → **NBB-Centrale URL of XBRL-bestand of manuele invoer-velden** _(document)_

**📤 Output**:
- Geïmporteerde dataset in tool → **Balans + RR + bijlagen, geladen per boekjaar** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Open de tool (bv. Bel-First) en zoek de onderneming op via ondernemingsnummer (BCE-nummer).
2. Selecteer minstens 3 opeenvolgende boekjaren — voor evolutie-analyse vereist door [[interpretatie-financiele-ratios]] §evolutie-lezen.
3. Controleer dat het correcte schema (volledig/verkort/micro) wordt herkend.
4. Voor niet-neergelegde data (bv. tussentijdse jaarrekening): gebruik manuele invoer + flag dat dit niet uit NBB komt.
5. Verifieer dat balanstotaal activa = balanstotaal passiva (controle import-integriteit).


**Grondslag**: [[financiele-analyse-software]] §functionaliteit, KB WVV — neerlegging jaarrekening

### 3. Genereren en lezen van de automatisch berekende ratio-set

Laat de tool de standaard-ratio-set berekenen (liquiditeit, solvabiliteit, rentabiliteit, productiviteit) en controleer de formule-keuze.

**Waarom?** Tools gebruiken vaak licht afwijkende formule-varianten — bv. cashflow-definitie of solvabiliteits-formule. Een ratio uit Bel-First kan licht verschillen van die uit een handboek. Op bekwaamheid-niveau wordt verwacht dat de student dit herkent.

**📥 Input**:
- Geïmporteerde dataset (stap 2) → **Drie boekjaren** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Ratio-tabel → **Ratio's per doel-categorie + bedrijfs- en sectorgemiddelden** _(berekening)_

**🛠️ Hoe**:

1. Vraag de tool om de standaard-ratio-set (bv. in Bel-First: tabblad "Ratios").
2. Vergelijk de berekende ratio's met je eigen handmatige berekening van de hoofdratio's:
   - Current ratio = vlottende activa / kortlopende schulden.
   - Solvabiliteitsratio = eigen vermogen / totaal activa.
   - ROE = nettoresultaat / eigen vermogen.
3. Indien afwijking > 5%: open de tool-documentatie en achterhaal welke formule-variant wordt gebruikt. Documenteer dit in je rapport.
4. Plaats elke ratio in een van de vier doel-categorieën volgens [[ratio-vier-doelen-vergelijking]].


> [!example]- Voorbeeld: Rotex Roeselare NV — Bel-First ratio-output 20X3
> Rotex Roeselare NV — Bel-First ratio-output 20X3.
>
> 1. **Ratio-tabel** 🧮
>
>    | Ratio (Bel-First) | Waarde Rotex | Sector NACE 1623 |
>    |---|---:|---:|
>    | Current ratio | 1,45 | 1,80 |
>    | Quick ratio | 0,75 | 0,85 |
>    | Solvabiliteit (EV/TA) | 40,0% | 32,5% |
>    | ROE | 32,5% | 18,7% |
>    | Altman Z (geautomatiseerd) | 3,15 | n.v.t. |
>    
>

**Grondslag**: [[financiele-analyse-software]] §functionaliteit, [[ratio-vier-doelen-vergelijking]]

### 4. Sectorvergelijking via NACE-code en interpretatie

Vergelijk de ratio-set van de onderneming met het sector-gemiddelde (NACE-niveau 4 of 5) en interpreteer de afwijkingen.

**Waarom?** Een ratio in absolute zin is moeilijk te interpreteren — pas in vergelijking met de sector wordt zinvol. De tool levert de sector-data; de interpretatie blijft mensenwerk.

**📥 Input**:
- Ratio-tabel + NACE-code → **Eigen ratio's + sector-mediaan + percentiel-positie** _(berekening)_

**📤 Output**:
- Sectorvergelijkings-rapport → **Per ratio: positie in sector + signalering** _(conclusie)_

**🛠️ Hoe**:

1. Bevestig de NACE-code van de onderneming via [[sectorvergelijking-financiele-analyse]] §NACE-classificatie. Voor diversifieerders: gebruik hoofd-activiteit.
2. Vraag in de tool de sector-mediaan en de kwartielen (Q1, Q3) op voor minstens de hoofdratio's.
3. Plaats de onderneming in de sector-distributie (boven mediaan, in Q1, etc.).
4. Onderzoek elke afwijking > 1 standaarddeviatie (of buiten Q1-Q3 interval):
   - Is het signaal van zwakte (slecht beheer)?
   - Of strategische keuze (specialisatie, premium-positionering)?
   - Of cyclus-fase (groei vs volwassen)?
5. Combineer met de interpretatie-methode uit [[interpretatie-financiele-ratios]] §triangulair-lezen.


> [!example]- Voorbeeld: Rotex Roeselare NV — sectorvergelijking 20X3 in NACE 1623 (kuiperij/houtbewerking)
> Rotex Roeselare NV — sectorvergelijking 20X3 in NACE 1623 (kuiperij/houtbewerking).
>
> 1. **Positionering** 🧮
>
>    - Current ratio 1,45 < sector 1,80 → onder sector, in 1ste kwartiel.
>    - Solvabiliteit 40% > sector 32,5% → boven sector, in 3de kwartiel.
>    - ROE 32,5% >> sector 18,7% → ver boven sector, in 4de kwartiel.
>    
>
> 2. **Interpretatie** 💬
>
>    Rotex is conservatief gefinancierd (hoge solvabiliteit) en zeer rentabel (hoge ROE). De lage current ratio is geen alarm — past bij efficiënt werkkapitaal-beheer (kort BBK-cyclus). Strategische keuze, geen zwakte. Aanbeveling: monitor evolutie van de current ratio; daling onder 1,2 zou wel zorgwekkend zijn.
>    
>

**Grondslag**: [[financiele-analyse-software]] §functionaliteit, [[sectorvergelijking-financiele-analyse]]

> [!warning]- Lees de tool-output kritisch — vergelijk met je eigen berekening voor de hoofdratio's.
>
> _Vaak fout gedaan_: De tool-output blind overnemen zonder formule-controle. Verschillende tools gebruiken licht afwijkende cashflow- of solvabiliteits-formules.
>
> _Grondslag_: [[financiele-analyse-software]] §valkuilen

> [!warning]- Combineer sector-benchmark met evolutie over 3+ jaren én met business-context.
>
> _Vaak fout gedaan_: Een afwijking van sector-mediaan automatisch als probleem labelen — vaak is het een strategische keuze.
>
> _Grondslag_: [[interpretatie-financiele-ratios]] §plaats-ratio-in-doel-categorie

> [!warning]- Documenteer welke tool werd gebruikt en welke versie / data-snapshot.
>
> _Vaak fout gedaan_: Tool-output overnemen zonder bronvermelding — bij latere herziening of audit niet meer reproduceerbaar.
>
> _Grondslag_: Beroepsstandaard documentatie


## Voorbeelden




## Bronnen

[^1]: `anchor-1.9.VII`
