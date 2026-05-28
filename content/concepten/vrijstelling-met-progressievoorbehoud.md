---
title: "Vrijstelling met progressievoorbehoud"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.8.I
  - 2.8.II
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/vrijstelling-met-progressievoorbehoud.json"
---

# Vrijstelling met progressievoorbehoud

_Regime_

📋 Regeling · Anchors: `2.8.I` · `2.8.II` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: exemption with progression · vrijstelling onder progressievoorbehoud · exonération sous réserve de progressivité — **Vertalingen**: en: exemption with progression · fr: exonération sous réserve de progressivité

## Definitie

📖 Vrijstelling met progressievoorbehoud is een methode om dubbele belasting te vermijden waarbij de woonstaat (België) de buitenlandse inkomsten niet zelf belast, maar wél meetelt om het belastingtarief op de Belgische inkomsten te bepalen. In de PB is het de standaardmethode van België in de meeste klassieke dubbelbelastingverdragen (DBV) voor onroerende inkomsten uit het buitenland en beroepsinkomsten via een buitenlandse vaste inrichting. Het wettelijke anker is art. 155 WIB92: 'Inkomsten die krachtens internationale overeenkomsten ter voorkoming van dubbele belasting zijn vrijgesteld, komen in aanmerking voor het bepalen van de belasting, maar deze wordt verminderd naar verhouding van het deel van de inkomsten dat is vrijgesteld in het totale netto-inkomen.'

<small>📚 WIB92 — art. 155 — _wettekst_ · OESO-modelverdrag — art. 23A — _modelverdrag_ · Circulaire 2022/C/106 — A. Vrijstelling met progressievoorbehoud — _circulaire_</small>

## Substantie

📖 Concreet: de fiscus berekent eerst de belasting alsof alle inkomsten (Belgisch + buitenlands) in België waren belast — dat geeft een 'virtuele' belastingbedrag dat de volle progressie van de PB-schijven weerspiegelt. Vervolgens wordt dat bedrag proportioneel verminderd in dezelfde verhouding als waarin het vrijgestelde inkomen zich verhoudt tot het totale netto-inkomen. Effect: het Belgische deel wordt belast tegen het tarief dat zou gelden als alles in BE was — dus tegen een hoger gemiddeld tarief dan zonder buitenlandse inkomsten. De belastingplichtige betaalt geen Belgische belasting op de vrijgestelde inkomsten zelf, maar verliest het voordeel van zijn lagere PB-schijven dat hij anders op de Belgische inkomsten zou genieten.

<small>📚 WIB92 — art. 155 — _wettekst_ · Circulaire 2022/C/106 — B. Belasting tegen een afzonderlijke aanslagvoet — _circulaire_</small>

## Rationale

🔗 De rationale is dubbel. (1) Voorkoming van dubbele belasting: de buitenlandse staat heft (typisch op onroerend goed of VI-winst), dus België verzaakt aan eigen heffing op datzelfde inkomen. (2) Behoud van progressiviteit: zonder progressievoorbehoud zou een rijke belastingplichtige zijn Belgische inkomen kunnen 'verstoppen' in lage PB-schijven door grote buitenlandse inkomsten te genereren — dat ondergraaft de fiscale solidariteit. De methode is bewust strikter dan vrijstelling-zonder-progressievoorbehoud (waar buitenlandse inkomsten écht volledig uit het tarief-vergelijk worden gehaald) maar zachter dan de FBB-verrekenmethode (waar de Belgische belasting volledig wordt geheven en buitenlandse belasting verrekend).

<small>📚 OESO-modelverdrag — art. 23A — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 155 (PB); art. 240bis-240quater (verdragsvrijstellingen onroerend); OESO-MV art. 23A; concrete DBV's

Belgische standaardmethode in klassieke DBV's voor onroerende inkomsten (art. 6 DBV) en beroepsinkomsten via VI (art. 7 + 15). Voor passieve inkomsten (dividenden, interesten, royalty's) gebruikt België meestal de FBB-verrekenmethode.

**✅ Voor**
- 📖 Belgische rijksinwoner met huurinkomsten of meerwaarden op een buitenlands onroerend goed in een verdragsstaat (bv. tweede verblijf in Frankrijk, Spanje).
- 📖 Belgische rijksinwoner-werknemer die loon ontvangt voor werk uitgevoerd in het buitenland (mits VI of >183 dagen — art. 15 DBV).

**🚫 Niet voor**
- 📖 Buitenlandse dividenden, interesten en royalty's — die vallen onder de FBB-verrekenmethode (art. 285-289 WIB92), niet onder vrijstelling.
- 🔗 Inkomsten uit niet-verdragslanden — geen vrijstelling, alleen mogelijke FBB-verrekening.

**📋 Voorwaarden**
- 📖 Cumulatief: (1) belastingplichtige is Belgisch rijksinwoner; (2) inkomsten komen uit een staat waarmee België een DBV heeft; (3) het toepasselijke DBV-artikel kent de heffingsbevoegdheid toe aan de bronstaat én voorziet vrijstelling als methode (art. 23A); (4) bewijs van werkelijke belastbaarheid in de bronstaat kan vereist zijn ('subject-to-tax'-clausule in moderne verdragen).

**👍 Voordeel**
- 🔗 Het buitenlandse inkomen ontsnapt aan Belgische belasting. Bij hoge buitenlandse belastingdruk: economisch voordeliger dan FBB-verrekening (waar slechts een forfaitair deel wordt verrekend).

**⚠️ Risico**
- 🔗 Verlies van progressievoordeel: de Belgische schijven worden 'opgeschoven'. Een belastingplichtige met enkel Belgisch inkomen X betaalt minder dan dezelfde persoon met BE-inkomen X + buitenlands inkomen Y onder vrijstelling-met-progressievoorbehoud. Dit verschil moet aan de cliënt worden uitgelegd om frustratie te vermijden.

## Bouwstenen

### 🧮 Formule vermindering (art. 155 WIB92)  
_`formule`_

📖 Belasting verschuldigd = belasting op het totale netto-inkomen (incl. buitenlands) × (Belgisch netto-inkomen / totaal netto-inkomen). Of equivalent: vermindering = belasting op totaal × (vrijgesteld inkomen / totaal netto-inkomen). Resultaat: de Belgische belasting wordt berekend op het tarief dat zou gelden als alles in België was, maar enkel het Belgische deel wordt effectief belast.

<small>📚 WIB92 — art. 155 — _wettekst_</small>

### 👣 Drie-stappen-berekening  
_`stap`_

📖 Stap 1: bepaal totaal netto belastbaar inkomen = Belgisch netto + vrijgesteld netto (apart aangeven in aangifte). Stap 2: bereken virtuele belasting op dit totaal volgens de gewone PB-schijven + belastingvrije som + verminderingen. Stap 3: verminder die virtuele belasting in de verhouding (vrijgesteld netto / totaal netto) — het resulterende bedrag is de werkelijke Belgische belasting.

<small>📚 WIB92 — art. 155 — _wettekst_</small>

### ⚙️ Subject-to-tax-clausule (modernere verdragen)  
_`mechanisme`_

🔗 Modernere Belgische DBV's bevatten een subject-to-tax-clausule: vrijstelling met progressievoorbehoud wordt enkel toegekend voor zover de buitenlandse staat het inkomen daadwerkelijk in de heffing betrekt. Doel: voorkomen dat een belastingplichtige zowel buitenland-vrijstelling (geen lokale heffing) als BE-vrijstelling geniet ('dubbele non-belasting'). Voorbeeld: DBV BE-NL bevat geen volledige subject-to-tax voor onroerend; sommige nieuwere verdragen wél.

<small>📚 OESO-modelverdrag — art. 23A §4 (2017-versie) — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Toepassing op buitenlands onroerend  
_`regel`_

📖 Voor een buitenlands gelegen onroerend goed (huur of meerwaarde) is vrijstelling-met-progressievoorbehoud de standaardmethode in Belgische DBV's. De Belgische rijksinwoner moet het onroerend goed aangeven volgens recente regels (sinds AJ 2022 op basis van kadastraal inkomen voor verdragslanden, of werkelijk gehuurd inkomen volgens lokaal recht). Belastingplichtige hoeft geen buitenlandse belasting bewijs te leveren voor de toepassing, maar moet wél het exacte buitenlandse netto-inkomen aangeven voor de progressie-berekening.

<small>📚 WIB92 — art. 240bis (verdragsvrijstellingen onroerend) — _wettekst_ · OESO-modelverdrag — art. 6 + 23A — _modelverdrag_</small>

### 📜 Toepassing op buitenlandse beroepsinkomsten  
_`regel`_

📖 Voor loon of zelfstandig inkomen verworven door werk in het buitenland: vrijstelling-met-progressievoorbehoud geldt indien het DBV-artikel 15 (loon) of 14 (vrije beroepen) het heffingsrecht aan de werkstaat toekent én art. 23A vrijstelling voorziet. Klassiek geval: Belg gedetacheerd > 183 dagen in Duitsland met DE-belastbaarheid. De aangifte: aparte rubriek 'buitenlandse beroepsinkomsten vrijgesteld bij verdrag'. Modernere verdragen kunnen FBB-methode voorzien — DBV-specifiek nakijken.

<small>📚 OESO-modelverdrag — art. 15 + 23A — _modelverdrag_</small>

### ⚙️ Vergelijking met FBB-verrekening (art. 23B)  
_`mechanisme`_

📖 Twee verdragsmethodes: (A) vrijstelling-met-progressievoorbehoud (art. 23A) en (B) FBB-verrekening (art. 23B + art. 285-289 WIB92). Bij A: woonstaat heft geen belasting op buitenlandse inkomen, maar tariefdruk-effect via progressie. Bij B: woonstaat heft volle belasting, vermindert met (gedeeltelijke) verrekening van buitenlandse belasting. Verschil voor stagiair: bij A is BUITENLANDSE belasting niet relevant voor de Belgische berekening (alleen het netto-inkomen); bij B moet je beide bedragen kennen (BE-belasting + buitenlandse belasting).

<small>📚 OESO-modelverdrag — art. 23A + 23B — _modelverdrag_ · WIB92 — art. 285 — _wettekst_</small>

## Voorbeelden

### 💡 Belgische gepensioneerde met tweede verblijf in Frankrijk 🔗

_Jean en Marie (rijksinwoners BE, gehuwd, geen kinderen) hebben in N: pensioen Belgisch 40.000 EUR netto-belastbaar; huurinkomsten woning Frankrijk 8.000 EUR netto. DBV BE-FR (oude versie) hanteert vrijstelling-met-progressievoorbehoud voor onroerend._

**Berekening:**
- Stap 1 — totaal belastbaar netto: 40.000 + 8.000 = 48.000 EUR.
- Stap 2 — virtuele belasting op 48.000 EUR (volgens PB-schijven, gemeenschappelijke aanslag): bv. 14.000 EUR (illustratief — exact tarief uit Cijferzakboekje).
- Stap 3 — vermindering = 14.000 × (8.000 / 48.000) = 14.000 × 0,1667 = 2.333 EUR.
- Stap 4 — Belgische belasting na vermindering = 14.000 − 2.333 = 11.667 EUR.
- Stap 5 — vergelijk: zonder buitenlands inkomen zou de PB op 40.000 EUR alleen circa 10.800 EUR zijn (lagere gemiddelde belasting omdat geen hogere schijf wordt aangeraakt). Verschil 11.667 − 10.800 ≈ 867 EUR = het progressie-effect.

→ **Resultaat**: BE-belasting 11.667 EUR (vs hypothetisch 10.800 EUR zonder buitenlands inkomen). Het verschil = de prijs van het progressievoorbehoud.

<small>📚 WIB92 — art. 155 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Detachering werknemer naar Duitsland (>183 dagen) 🔗

_Sophie, BE-rijksinwoner, werkte van januari tot november N (>183 dagen) in Duitsland voor haar Belgische werkgever; bezoldiging voor die periode 50.000 EUR werd in Duitsland belast (DBV BE-DE art. 15). Daarnaast 8.000 EUR loon voor december in België._

Toepassing van vrijstelling-met-progressievoorbehoud op de 50.000 EUR Duits inkomen. Sophie geeft het aan in de aangifte als 'beroepsinkomsten verworven in het buitenland, vrijgesteld bij verdrag met progressievoorbehoud'. Totaal netto = 58.000 EUR; virtuele PB op 58.000 EUR; vermindering met factor 50/58. Effectief BE-belasting = virtuele PB × (8/58). Het Duitse inkomen ontsnapt aan BE-belasting maar de 8.000 EUR worden belast tegen het tarief dat hoort bij 58.000 EUR (dus de hogere schijven worden aangeraakt).

<small>📚 DBV BE-DE — art. 15 + 23A — _modelverdrag_</small>

### 💡 Afzonderlijk belastbaar buitenlands inkomen (Circ. 2022/C/106) 📖

_Achterstallige bezoldiging uit Duitsland (afzonderlijk belastbaar conform art. 171 WIB92) van 20.000 EUR + Belgische bezoldigingen 40.000 EUR._

Voor afzonderlijk belastbare inkomsten die bij verdrag zijn vrijgesteld: de Circulaire 2022/C/106 bevestigt dat ze meetellen voor de bepaling van de gemiddelde aanslagvoet die op de Belgische afzonderlijk-belaste inkomsten zou toegepast worden — maar zelf vrijgesteld blijven. Mechaniek dezelfde als bij gezamenlijk belaste inkomsten: virtueel meetellen, vervolgens proportioneel kwijtschelden.

<small>📚 Circulaire 2022/C/106 — B. Belasting tegen een afzonderlijke aanslagvoet — _circulaire_</small>

## Valkuilen

### ⚠️ Denken dat 'vrijgesteld' = geen impact op Belgische belasting

**Verkeerde assumptie**: Cliënten en stagiairs lezen 'vrijstelling' en denken: buitenlands inkomen heeft geen invloed op de Belgische aanslag.

**Kernpunt**: Vrijgestelde inkomsten beïnvloeden wél het tarief op de Belgische inkomsten via progressievoorbehoud. Het buitenlandse inkomen verhoogt de effectieve aanslagvoet — soms aanzienlijk wanneer de buitenlandse inkomsten groot zijn ten opzichte van de Belgische.

<small>📚 WIB92 — art. 155 — _wettekst_</small>

### ⚠️ Vrijstelling toepassen zonder DBV te controleren

**Verkeerde assumptie**: Buitenlands inkomen automatisch 'vrijstelling-met-progressievoorbehoud' krijgen.

**Kernpunt**: Vrijstelling is enkel mogelijk wanneer een DBV bestaat én dat DBV-artikel (art. 23A) vrijstelling als methode kiest voor dat type inkomen. Voor passieve inkomsten (dividend, interest, royalty's) geldt typisch FBB-verrekening. Voor niet-verdragsland: helemaal geen vrijstelling.

<small>📚 OESO-modelverdrag — art. 23A + 23B — _modelverdrag_</small>

### ⚠️ Buitenlands inkomen niet aangeven omdat het 'toch vrijgesteld is'

**Verkeerde assumptie**: Sommige belastingplichtigen geven het buitenlandse vrijgestelde inkomen helemaal niet aan in de Belgische PB-aangifte.

**Kernpunt**: Aangifteplicht blijft: ook vrijgesteld bij verdrag inkomen MOET worden aangegeven in de daartoe voorziene codes (anders kan de fiscus het progressievoorbehoud niet toepassen — wat technisch tot een te lage belasting leidt en bij controle hertaxatie + boete). Vakcode 1130/1131 PB (verdrag-vrijgesteld onroerend); 1180 e.v. (vrijgesteld loon buitenland).

<small>📚 WIB92 — art. 305 (aangifteplicht) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Syntheses

### 🧩 Synthese  
_`matrix`_

Welke methode geldt voor welk type buitenlands inkomen?

## Accountant-perspectieven

### Particulier met buitenlands onroerend goed

_Belgische rijksinwoner met tweede verblijf of huurpand in een verdragsstaat — typische adviespraktijk PB._

#### 💰 Fiscaal adviseur

##### 👣 Aangifte correct invullen + progressievoorbehoud uitleggen  
_`stap`_

🔗 (1) Identificeer het type buitenlands inkomen + verdragsstaat. (2) Raadpleeg het DBV: vrijstellingsmethode? (3) Vul de correcte aangifte-rubriek in voor 'verdrag-vrijgesteld' inkomen (geen vrijstelling-zonder-aangifte). (4) Leg aan de cliënt het progressie-effect uit voorafgaand aan de aanslag — vermijdt verbazing. (5) Bewaar bewijzen van buitenlandse belastbaarheid voor het geval subject-to-tax wordt opgevraagd.

<small>📚 WIB92 — art. 155 + 305 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Voorafgaand advies bij aankoop buitenlands onroerend  
_`vuistregel`_

🔗 Voor cliënt die aankoop overweegt: simuleer beide aangiften (zonder en met buitenlands inkomen) om het exacte progressie-effect te tonen. Hou rekening met: buitenlandse onroerende voorheffing, lokale registratiekosten, eventuele schenkings-/erfbelasting-implicaties. Voor verhuur: lokale belasting in bronstaat is dikwijls hoger dan Belgisch KI-systeem zou opleveren — bespreek netto-rendement na alle belastingen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → FBB-methode (verrekening — alternatieve methode) → [[forfaitair-gedeelte-buitenlandse-belasting]] _(moet-verwijzen)_
- → Internationaal onroerend goed (toepassing) → [[internationaal-onroerend-goed]] _(moet-verwijzen)_
- ↪ Personenbelasting context → [[personenbelasting]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[internationaal-fiscaal]]
- [[personenbelasting]]
### `triggert`
- [[belastingberekening-pb]] — Vrijstelling met progressievoorbehoud werkt op het niveau van de aanslagberekening — beïnvloedt de effectieve aanslagvoet.
- [[internationaal-onroerend-goed]] — Typische toepassing op buitenlands gelegen onroerend goed.
### `vereist`
- [[dubbelbelastingverdrag]] — Methode-keuze (vrijstelling vs FBB) komt uit het concrete DBV; zonder DBV geen vrijstelling.
### `vergelijkbaar_met`
- [[forfaitair-gedeelte-buitenlandse-belasting]]
    - **Gelijkenissen**:
        - Beide voorkomen dubbele belasting bij grensoverschrijdende inkomsten
        - Beide passen DBV-mechanismes toe (art. 23 OESO-MV)
    - **Verschillen**:
        - Vrijstelling: woonstaat heft niet op buitenlands inkomen — alleen progressie-impact
        - FBB: woonstaat heft wél, vermindert met verrekening van buitenlandse belasting
        - Vrijstelling: typisch voor onroerend + actieve beroepsinkomsten
        - FBB: typisch voor passieve inkomsten (dividend/interest/royalty)
    - ⚠️ **Verwarringsrisico**: Beide methodes komen voor in dezelfde aangifte. Studenten gebruiken soms FBB-formules op verdrag-vrijgestelde inkomsten — fout. Eerst type inkomen + DBV-artikel nakijken.
