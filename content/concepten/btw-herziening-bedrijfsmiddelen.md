---
title: "BTW-herziening bedrijfsmiddelen"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.4.IV
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/btw-herziening-bedrijfsmiddelen.json"
---

# BTW-herziening bedrijfsmiddelen

_Procedure_

📋 Regeling · Anchors: `2.4.IV` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: herzieningsperiode bedrijfsmiddelen · 5-jaar / 15-jaar regel BTW

## Definitie

📖 BTW-herziening bedrijfsmiddelen is het mechanisme dat de oorspronkelijk afgetrokken BTW op een bedrijfsmiddel corrigeert wanneer de bestemming van dat middel binnen een wettelijk herzieningstijdvak verandert. Voor roerende bedrijfsmiddelen (machines, computers, voertuigen) loopt het tijdvak 5 jaar (KB nr. 3 art. 9 §1); voor onroerende bedrijfsmiddelen (gebouwen, verbouwingen) 15 jaar (art. 9 §2); voor gebouwen verhuurd onder optionele BTW-regeling 25 jaar (art. 9 §3). Bij wijziging van bestemming binnen het tijdvak wordt een evenredig deel van de oorspronkelijke aftrek terugbetaald aan of teruggevorderd van de fiscus.

<small>📚 WBTW — art. 48 — _wettekst_ · KB nr. 3 — art. 9 §1-3 — _kb_ · KB nr. 3 — art. 10 — _kb_</small>

## Substantie

🔗 Het herzieningsmechanisme realiseert het beginsel: de aftrek moet evenredig blijven met het werkelijke gebruik over de hele levensduur (vereenvoudigd tot 5/15/25 jaar). Wie 100 % aftrek krijgt op een machine en die machine na 2 jaar overschakelt naar volledig privé-gebruik, moet 3/5 (drie resterende jaren) van de oorspronkelijke aftrek terugbetalen. Praktisch: de herziening wordt jaarlijks in de eerste aangifte van het kalenderjaar uitgevoerd, ofwel ineens bij het trigger-event (verkoop, stopzetting). Het bedrag wordt opgenomen in rooster 61 (te betalen herziening) of rooster 62 (te vorderen herziening).

<small>📚 KB nr. 3 — art. 10 + art. 11 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Rationale

📖 Een bedrijfsmiddel werkt jaren mee in de activiteit. Als BTW-aftrek alleen op aankoopmoment definitief zou zijn, zou een belastingplichtige aftrek kunnen claimen voor een investering en kort daarna de bestemming wijzigen zonder gevolg — perverse prikkel. Het herzieningsmechanisme spreidt de aftrek 'fictief' over de levensduur en laat de fiscus corrigeren bij bestemmingswijziging. EU-grondslag: art. 184-192 Richtlijn 2006/112 (verplicht 5 jaar, optioneel 20 jaar voor onroerend — België heeft 15 + 25).

<small>📚 Richtlijn 2006/112/EG — art. 184-192 — _richtlijn_</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WBTW art. 48 + KB nr. 3 art. 6-13

Stabiel regime. Bijzondere termijn 25 jaar voor onder optie verhuurde gebouwen (art. 44 §3, 2°, d) sinds 01-01-2019.

## Sub-concepten

### 📦 Herzieningstermijnen — 5 / 15 / 25 jaar  
_`regime` (subconcept)_

#### Definitie

📖 Drie regimes, alle te tellen vanaf 1 januari van het jaar van ingebruikneming: (1) roerende bedrijfsmiddelen: 5 jaar (KB nr. 3 art. 9 §1) — machines, voertuigen, computers, kantoormeubels; (2) onroerende bedrijfsmiddelen: 15 jaar (art. 9 §2) — gebouwen (nieuwbouw, aankoop met BTW), grondverbeteringen, ingrijpende verbouwingen; (3) gebouwen verhuurd onder optionele BTW-regeling: 25 jaar (art. 9 §3) — verlengd regime sinds 2019 om optie-misbruik te voorkomen.

<small>📚 KB nr. 3 — art. 9 §1 — _kb_ · KB nr. 3 — art. 9 §2 — _kb_ · KB nr. 3 — art. 9 §3 — _kb_</small>

### 📦 Trigger-events voor herziening  
_`regime` (subconcept)_

#### Definitie

📖 Vijf gevallen trigger herziening (KB nr. 3 art. 10 §1): (1) bedrijfsmiddel wordt geheel of gedeeltelijk privé gebruikt, of gebruikt voor handelingen zonder aftrekrecht, of in andere verhouding dan oorspronkelijk; (2) wijziging in de factoren die aan de oorspronkelijke aftrek ten grondslag liggen (bv. pro-rata-verhoudingsgetal wijzigt); (3) bedrijfsmiddel wordt verkocht onder BTW-belastbare regeling (positieve herziening mogelijk in voordeel belastingplichtige); (4) bedrijfsmiddel houdt op te bestaan in de onderneming (verkoop zonder BTW, schenking, uittrede uit BTW-eenheid); (5) belastingplichtige verliest hoedanigheid of stopt aftrekplichtige activiteit (vooral relevant voor onroerend).

<small>📚 KB nr. 3 — art. 10 §1 1°-5° — _kb_</small>

## Bouwstenen

### 🧮 Formule herziening — roerend (5 jaar)  
_`formule`_

🔗 Herziening = oorspronkelijke aftrek × (resterende jaren in 5-jaar-tijdvak / 5). Resterende jaren = vol jaren tot einde tijdvak op moment van trigger. Het jaar van ingebruikneming én het jaar van het trigger-event tellen volledig mee in de oorspronkelijke aftrek (geen pro-rata-maand). Formule: Herziening_te_betalen = oorspronkelijke_aftrek × (resterende_jaren / 5).

<small>📚 KB nr. 3 — art. 11 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 🧮 Formule herziening — onroerend (15 of 25 jaar)  
_`formule`_

🔗 Voor onroerend: vervang noemer door 15 (gewoon regime) of 25 (optieverhuur). Voor jaarlijkse herziening bij bestemmingswijziging: per-jaar-correctie = oorspronkelijke aftrek × (verschil aftrek-percentage / 15 of 25). Formule: Herziening_te_betalen = oorspronkelijke_aftrek × (resterende_jaren / 15 of 25).

<small>📚 KB nr. 3 — art. 9 §2 + §3 — _kb_ · KB nr. 3 — art. 11 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### ⚙️ Positieve herziening (in voordeel belastingplichtige)  
_`mechanisme`_

📖 Wanneer een bedrijfsmiddel dat eerst met beperkte aftrek werd verworven (bv. pro-rata 40 %, of vrijgestelde activiteit met 0 %) binnen het tijdvak gebruikt gaat worden voor (meer) belaste handelingen, ontstaat een herziening in het voordeel: de belastingplichtige mag een evenredig deel van de niet-afgetrokken BTW alsnog claimen. Typisch geval: vrijgesteld → optie tot belasting (huurder schakelt over). Wordt aangegeven in rooster 62 (te vorderen herziening).

<small>📚 KB nr. 3 — art. 10 §1, 3° — _kb_</small>

### 📜 Inventaris bedrijfsmiddelen aan herziening onderworpen  
_`regel`_

🔗 De belastingplichtige moet voor elk bedrijfsmiddel met aanvankelijke BTW-aftrek > drempel (verworven bedrijfsmiddel) een inventaris bijhouden met: aankoopdatum, ingebruikneming, aanschaffingsprijs, oorspronkelijk afgetrokken BTW, bestemming, % aftrek. Deze inventaris dient als basis voor herzieningsberekeningen. Bij BTW-controle = onmiddellijk voor te leggen.

<small>📚 KB nr. 3 — art. 11 + art. 13 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Bestelwagen — overgang naar privégebruik na 2 jaar 🔗

_Zelena Bio koopt op 15 maart 2024 een bestelwagen voor 30.000 EUR + 6.300 EUR BTW. Volledig beroep → 100 % aftrek = 6.300 EUR. Op 1 juli 2026 wijzigt bestemming naar 100 % privé._

**Berekening:**
- Stap 1 — type bedrijfsmiddel: roerend → tijdvak 5 jaar
- Stap 2 — tijdvak: van 01-01-2024 tot 31-12-2028 (5 kalenderjaren)
- Stap 3 — oorspronkelijke aftrek: 6.300 EUR (100 %)
- Stap 4 — moment trigger: 2026 — resterend zijn 2026, 2027, 2028 = 3 jaar
- Stap 5 — herziening = 6.300 × (3 / 5) = 3.780 EUR te storten
- Stap 6 — boeking: D 615 'BTW-herziening' 3.780 / C 451 'Te betalen BTW' 3.780. Rooster 61.

→ **Resultaat**: Zelena stort 3.780 EUR aan de fiscus in de aangifte van het tijdvak waarin de bestemmingswijziging valt. Niet de volledige 6.300 EUR — de 2 jaren bedrijfsgebruik (2024 + 2025) blijven afgetrokken want correct gebruik.

<small>📚 KB nr. 3 — art. 9 §1 + art. 10 §1, 1° — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 💡 Kantoorgebouw — verkoop zonder BTW na 8 jaar 🔗

_Aurelia Holding bouwt in 2018 een kantoor (1.000.000 EUR + 210.000 EUR BTW = 100 % aftrek omdat 100 % beroep). Verkoopt in 2026 (zonder BTW want > 5 jaar = 'oud gebouw')._

**Berekening:**
- Stap 1 — type: onroerend → tijdvak 15 jaar
- Stap 2 — tijdvak: 01-01-2018 tot 31-12-2032
- Stap 3 — oorspronkelijke aftrek: 210.000 EUR
- Stap 4 — moment trigger (verkoop zonder BTW = handeling zonder aftrekrecht): 2026 — resterend zijn 2026 t/m 2032 = 7 jaar
- Stap 5 — herziening = 210.000 × (7 / 15) = 98.000 EUR te storten
- Stap 6 — aangifte in periode van verkoop, rooster 61

→ **Resultaat**: Aurelia moet 98.000 EUR herzien BTW terugbetalen aan de Staat omdat ze haar 'oud gebouw' verkoopt zonder BTW. Alternatief: optionele BTW-regeling toepassen op verkoop (mits voorwaarden) → geen herziening + koper aftrek op zijn beurt.

<small>📚 KB nr. 3 — art. 9 §2 + art. 10 §1, 4° — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Herzieningstermijn vanaf aankoopdatum tellen

**Verkeerde assumptie**: Het tijdvak loopt 5 jaar vanaf de aankoopdatum.

**Kernpunt**: Het tijdvak loopt vanaf 1 januari van het jaar van INGEBRUIKNAME (KB nr. 3 art. 9). Een machine gekocht in december 2024 en in gebruik genomen in februari 2025 begint zijn tijdvak op 01-01-2025 — niet op aankoopdatum 2024. Aankoop ≠ ingebruikname.

<small>📚 KB nr. 3 — art. 9 §1 — _kb_</small>

### ⚠️ Verkoop = einde herziening

**Verkeerde assumptie**: Bij verkoop van een bedrijfsmiddel is geen herziening meer nodig.

**Kernpunt**: Het hangt af van de aard van de verkoop: (a) verkoop MET BTW = belaste handeling → geen herziening, want bestemming blijft 'aftrekplichtig'; (b) verkoop ZONDER BTW (typisch 'oud gebouw' of intracommunautair niet-belast) = trigger voor herziening voor resterende jaren. Onderscheid scherp bewaken bij vastgoed-verkopen.

<small>📚 KB nr. 3 — art. 10 §1, 3° + 4° — _kb_</small>

### ⚠️ Inventaris-administratie verwaarlozen

**Verkeerde assumptie**: 'Mijn BTW is correct afgetrokken bij aankoop — verder niets nodig.'

**Kernpunt**: Bedrijfsmiddelen moeten in een afzonderlijk register staan met datum ingebruikname, BTW-bedrag, % aftrek. Zonder dit register is herziening niet uit te voeren én bij controle bewijslast omgekeerd. Software-pakketten doen dit automatisch via koppeling activa-register ↔ BTW-pakket; bij gebrek aan koppeling moet kantoor manueel bijhouden.

<small>📚 KB nr. 3 — art. 13 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Kantoor bewaakt herzieningsadministratie cliënt

_De accountant die het bedrijfsmiddelen-register en de herzieningsberekeningen onderhoudt._

#### 📒 Boekhouder

##### 👣 Onderhouden van bedrijfsmiddelen-register  
_`stap`_

🔗 Per aanschaf bedrijfsmiddel: registreren in afzonderlijk register: type (roerend/onroerend), datum ingebruikname, aanschafprijs, BTW-bedrag, aftrekpercentage, einde-tijdvak. Bij bestemmingswijziging of verkoop: herzieningsberekening + boeking in rooster 61 of 62. Eind elk jaar: scan van het register voor automatische bestemmingswijziging-correcties (gemengde belastingplichtige).

<small>📚 KB nr. 3 — art. 11 + art. 13 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Advies bij verkoop bedrijfsvastgoed  
_`vuistregel`_

🔗 Bij geplande verkoop van een gebouw dat nog binnen 15-jaar-tijdvak valt: simuleer herzieningskost vs alternatief 'optie-BTW' bij verkoop. Bij omvangrijke restwaarde: optie-BTW vaak voordeliger (verkoper geen herziening + koper recupereert BTW = neutraal). Aandachtspunt: optie-BTW vereist samenwerking koper + naleving voorwaarden art. 44 §3, 1° WBTW.

<small>📚 WBTW — art. 44 §3, 1° — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → BTW-vastgoed (15-jaar herzieningsregime) → [[btw-vastgoed]] _(moet-verwijzen)_
- → Stopzetting BTW-activiteit (trigger herziening) → [[stopzetting-btw]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `vereist`
- [[btw-aftrek]] — Herziening corrigeert een eerder uitgeoefend recht op aftrek — vereist dus dat er aftrek was.
### `beinvloed_door`
- [[stopzetting-btw]] — Stopzetting BTW-activiteit met openstaande onroerende bedrijfsmiddelen triggert herziening voor resterende jaren.
