---
title: "Erfbelasting"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.6.VI
  - 2.6.VI.A
  - 2.6.VI.B
  - 2.6.VI.C
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/erfbelasting.json"
---

# Erfbelasting

_Regime_

📋 Regeling · Anchors: `2.6.VI` · `2.6.VI.A` · `2.6.VI.B` · `2.6.VI.C` · Wave: `skeleton-fiscaliteit-klein-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: successierecht — **Vertalingen**: fr: droit de succession

## Definitie

📖 De erfbelasting is een gewestelijke belasting die wordt geheven op de overgang van vermogen ten gevolge van het overlijden van een Rijksinwoner. In Vlaanderen heet de belasting officieel 'erfbelasting' (VCF) en wordt zij geïnd door VLABEL; in Brussel en Wallonië heet zij 'successierecht' en blijven de oude W.Succ.-regels van toepassing (geïnd door de federale Administratie van de Patrimoniumdocumentatie). De belasting wordt berekend op het netto-aandeel dat elke verkrijger ontvangt — niet op de nalatenschap als geheel — volgens een progressieve schaal die afhangt van de verwantschap met de overledene.

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.1.0.1 — _wettekst_ · Wetboek der Successierechten — art. 48 — _wettekst_</small>

## Substantie

🔗 De erfbelasting werkt vermogensoverdracht-belastend: bij overlijden 'verschuift' een vermogen van overledene naar erfgenaam, en de Staat heft op die overgang. Drie elementen bepalen de aanslag: (1) de samenstelling van het belastbaar voorwerp — alle goederen plus de fictiebepalingen (schenkingen <3 jaar, levensverzekeringen, gesplitste aankopen) minus aftrekbare passiva; (2) de toepasselijke gewestelijke tarieftabellen volgens verwantschap (rechte lijn vs broers/zussen vs anderen); (3) vrijstellingen, abattementen en verminderingen (gezinswoning langstlevende partner, gunstregime familiale onderneming, kinderlast). Het belastingbedrag kan tot 55% (Vl andere personen) of 65% (federaal historisch tarief) van het netto-aandeel oplopen — wat erfbelasting tot één van de zwaarste vermogenslastingen maakt en de motor is achter successieplanning.

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.4.1.1 — _wettekst_ · Wetboek der Successierechten — art. 48 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De erfbelasting steunt op twee samenhangende rationale: (1) een fiscaal-distributief beginsel — vermogensoverdrachten 'om niet' bij overlijden zijn een geschikt moment om vermogen progressief te herverdelen, omdat de overledene niet meer kan reageren en de erfgenaam een onverdiend voordeel ontvangt; (2) een gewestelijk-financierings-beginsel — sinds de 6e Staatshervorming is de erfbelasting volledig regionaal bevoegd (lokalisatie via 5-jaars-fiscale-woonplaats van de overledene). De progressie en het verwantschapsonderscheid weerspiegelen de maatschappelijke aanvaardbaarheid: hoe verder van de overledene, hoe hoger het tarief.

<small>📚 Bijzondere Financieringswet — art. 3 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: VCF Titel 2 Hoofdstuk 7 (Vlaanderen) + W.Succ. (Brussel/Wallonië, regionaal)

Stabiel regime onder gewestelijke bevoegdheid (Bijzondere Financieringswet 16-01-1989). Vlaanderen werd in 2015 vereenvoudigd via de VCF; Brussel en Wallonië werken met het federaal-gestructureerde W.Succ. dat zij regionaal wijzigen. Vlaanderen heeft recent (2024-2026) de tarieven verder hervormd voor partners en stiefkinderen.

**📋 Voorwaarden**
- 📖 Belastbaar voorwerp = alle goederen die toebehoorden aan de overledene op de dag van overlijden (roerend + onroerend, wereldwijd voor een Rijksinwoner) + de fictief tot de nalatenschap behorende goederen (fictiebepalingen W.Succ. art. 4 t/m 14 — Vlaams overgenomen in VCF 2.7.1.0.3-7).

**▶️ Trigger start**
- 📖 Overlijden van een Rijksinwoner (= persoon met laatste fiscale woonplaats in België) of overlijden van een niet-Rijksinwoner met onroerend goed in België (recht van overgang bij overlijden).

## Sub-concepten

### 📦 Tarieven erfbelasting  
_`regime` (subconcept)_

#### Definitie

📖 De erfbelasting wordt geheven op het netto-aandeel van elke verkrijger volgens twee progressieve tarieftabellen, gedifferentieerd naar verwantschap: Tabel I (rechte lijn + partners) en Tabel II (andere personen — broers/zussen of derden). De tarieven verschillen per gewest. In Vlaanderen (VCF art. 2.7.4.1.1): rechte lijn en partners 3% (tot 50.000 EUR), 9% (50.000-250.000 EUR), 27% (boven 250.000 EUR); broers/zussen 25%-30%-55%; andere personen 25%-45%-55%. In Brussel: rechte lijn 3-30%, broers/zussen 20-65%, anderen 35-80%. In Wallonië: vergelijkbaar met Brussel maar eigen schalen.

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.4.1.1 — _wettekst_ · Wetboek der Successierechten — art. 48 — _wettekst_</small>

#### Substantie

🔗 De progressie werkt per schijf, niet vlak: elke schijf wordt afzonderlijk belast, het bedrag van de voorgaande schijven wordt cumulatief opgeteld. De tabellen kennen drie hoofdverschillen tussen gewesten: (a) Vlaanderen heeft de zwaarste laagdrempel-tarieven afgevlakt naar 3%/9%/27% voor rechte lijn; (b) Brussel en Wallonië behouden steile progressie tot 30% rechte lijn boven 500.000 EUR; (c) tussen broers/zussen en derden zijn de Vlaamse tarieven aanzienlijk gemilderd in de hervorming 2024. Exacte schaalbedragen voor het lopende AJ steeds in het Cijferzakboekje opzoeken — niet uit het hoofd kennen.

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.4.1.1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Vlaamse tabel I — rechte lijn + partners  
_`drempel`_

📖 Vlaanderen, Tabel I (rechte lijn, echtgenoot, wettelijk samenwonenden + bepaalde feitelijk samenwonenden): 3% tot 50.000 EUR; 9% van 50.000 tot 250.000 EUR; 27% boven 250.000 EUR. De schalen gelden per verkrijger.

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.4.1.1 — _wettekst_</small>

#### 📏 Vlaamse tabel II — broers en zussen  
_`drempel`_

📖 Vlaanderen, Tabel II tussen broers en zussen: 25% tot 35.000 EUR; 30% van 35.000 tot 75.000 EUR; 55% boven 75.000 EUR. Voor andere personen (geen verwantschap) gelden 25%/45%/55% op overeenkomstige schijven. Bedragen geïndexeerd via Cijferzakboekje.

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.4.1.1 — _wettekst_</small>

#### 📜 Voordeligste tarief bij meerdere hoedanigheden  
_`regel`_

📖 Als een persoon in verschillende hoedanigheden tot de nalatenschap komt (bv. erfgenaam in rechte lijn én legataris uit testament), wordt het voor die persoon voordeligste tarief toegepast op alles wat hij verkrijgt (VCF art. 2.7.4.1.3).

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.4.1.3 — _wettekst_</small>

### 📦 Vrijstellingen en abattementen  
_`regime` (subconcept)_

#### Definitie

📖 De erfbelasting kent verschillende vrijstellingen en abattementen die de belastbare grondslag verlagen of de eindbelasting matigen. Drie hoofdcategorieën: (1) integrale vrijstellingen (Vlaanderen: gezinswoning voor langstlevende partner — 100% vrijgesteld; specifieke verminderingen voor kinderen <21 jaar); (2) abattementen (vast bedrag dat van de belastbare grondslag wordt afgetrokken — partners + rechte lijn Vlaanderen 50.000 EUR aan roerend goed); (3) verminderingen op het belastingbedrag zelf (bv. vermindering bij overlijden binnen het jaar — art. 57 W.Succ. — om dubbele heffing te beperken).

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.4.1.1 — _wettekst_ · Vlaamse Codex Fiscaliteit — art. 2.7.5.0.1 — _wettekst_ · Wetboek der Successierechten — art. 57 — _wettekst_</small>

#### ↪️ Gezinswoning — volledige vrijstelling langstlevende partner (Vl)  
_`uitzondering`_

📖 In Vlaanderen is het aandeel dat de langstlevende echtgenoot of wettelijk samenwonende verkrijgt in de gezinswoning (gemeenschappelijke hoofdverblijfplaats op datum overlijden) integraal vrijgesteld van erfbelasting (VCF art. 2.7.4.1.1 §2 derde lid). Voor de berekening van de erfbelasting op de rest van de nalatenschap wordt het vrijgestelde aandeel ook niet meegenomen in de nettoverkrijging (VCF art. 2.7.5.0.1 eerste lid). Brussel kent een gedeeltelijke vrijstelling voor de gezinswoning; Wallonië heeft een ander regime gericht op het aandeel.

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.4.1.1 — _wettekst_ · Vlaamse Codex Fiscaliteit — art. 2.7.5.0.1 — _wettekst_</small>

#### 📜 Vermindering bij verkrijging door broer/zus  
_`regel`_

📖 VCF art. 2.7.5.0.1: erfbelasting verschuldigd door een broer of zus wordt verminderd met (a) 2.000 EUR × (nettoverkrijging / 20.000 EUR) als nettoverkrijging ≤ 18.750 EUR; (b) 2.500 EUR × [1 - (nettoverkrijging / 75.000 EUR)] als nettoverkrijging tussen 18.750 en 75.000 EUR. Vermindering verdwijnt boven 75.000 EUR. Bedoeling: kleine verkrijgingen op niveau Tabel II ontzien.

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.5.0.1 — _wettekst_</small>

#### 📜 Vermindering bij opeenvolgende overdrachten binnen het jaar  
_`regel`_

📖 Als goederen die met successierecht zijn belast binnen het jaar na het overlijden van de erflater opnieuw door overlijden overgaan (bv. ouder overlijdt, kind erft, kind overlijdt binnen het jaar), worden de rechten op die tweede overdracht met de helft verminderd — zonder dat de vermindering de op de eerste overdracht geheven rechten kan overschrijden (art. 57 W.Succ.). Bedoeling: dubbele heffing op hetzelfde vermogen binnen korte tijd verzachten.

<small>📚 Wetboek der Successierechten — art. 57 — _wettekst_</small>

#### ↪️ Vrijstelling 'duo-legaat'-achtige technieken (afgeschaft Vl 2021)  
_`uitzondering`_

📖 Het oude 'duo-legaat' (kind erft via vrijstelling van een goed doel) is in Vlaanderen sinds 1 juli 2021 afgeschaft en vervangen door (a) een 0% tarief voor legaten aan erkende goede doelen en (b) een vriendenerfenis (begunstigde aangewezen in niet-herroepen testament, vermindering volgens VCF art. 2.7.5.0.6 — formule X = a × (b - c)). Testament moet vóór 1-1-2026 gedagtekend zijn om vriendenerfenis te genieten op recente nalatenschappen.

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.5.0.6 — _wettekst_</small>

### 📦 Fictiebepalingen  
_`regime` (subconcept)_

#### Definitie

📖 Fictiebepalingen zijn wettelijke regels die bepaalde goederen, hoewel ze juridisch niet meer in het patrimonium van de overledene zaten op datum overlijden, toch fiscaal tot de nalatenschap rekenen voor de berekening van de erfbelasting. Bedoeling: anti-misbruik-bescherming tegen technieken die successie ontwijken via schenking, levensverzekering of constructie. Drie kernfictie's: (1) schenkingen door de overledene binnen de drie jaar vóór overlijden (art. 7 W.Succ. / VCF 2.7.1.0.5); (2) levensverzekering ten gunste van een derde (art. 8); (3) gesplitste aankoop vruchtgebruik/blote eigendom waarbij vruchtgebruiker overlijdt (art. 9).

<small>📚 Wetboek der Successierechten — art. 7 — _wettekst_ · Wetboek der Successierechten — art. 8 — _wettekst_ · Wetboek der Successierechten — art. 9 — _wettekst_</small>

#### 📜 3-jaarsregel: schenking <3 jaar vóór overlijden (art. 7 W.Succ.)  
_`regel`_

📖 Schenkingen door de overledene in de drie jaar vóór overlijden worden, indien zij niet werden geregistreerd en dus niet aan schenkbelasting onderworpen zijn, voor de heffing van de erfbelasting geacht deel uit te maken van de nalatenschap. Doel: voorkomen dat erfgenamen via een sterfbed-schenking de progressieve erfbelasting omzeilen. Geregistreerde schenkingen (met betaalde schenkbelasting) zijn vrijgesteld van deze fictie — vandaar het belang van vooraf registreren bij planningsadvies. Vlaanderen verlengt de termijn naar 5 jaar voor schenkingen van familie-onderneming-aandelen waar het 0%-gunstregime werd toegepast.

<small>📚 Wetboek der Successierechten — art. 7 — _wettekst_ · Vlaamse Codex Fiscaliteit — art. 2.7.1.0.5 — _wettekst_</small>

#### 📜 Levensverzekering (art. 8 W.Succ.)  
_`regel`_

📖 De som die bij overlijden van de verzekerde wordt uitgekeerd aan een derde begunstigde op grond van een levensverzekering, wordt voor de heffing van de erfbelasting geacht als legaat verkregen door de begunstigde van de overledene-verzekeringnemer. Toepassing: typische zogenaamde 'AB-BC'-constructies en branche-21/branche-23-verzekeringen. Het tarief volgt de verwantschap tussen verzekeringnemer en begunstigde.

<small>📚 Wetboek der Successierechten — art. 8 — _wettekst_</small>

#### 📜 Gesplitste aankoop vruchtgebruik / blote eigendom (art. 9)  
_`regel`_

📖 Wanneer goederen door de overledene werden aangekocht voor het vruchtgebruik en door een derde (typisch een kind) voor de blote eigendom, wordt bij overlijden vermoed dat de volle eigendom in de nalatenschap zit — tenzij het bewijs wordt geleverd dat het kind de middelen voor de blote eigendom werkelijk zelf bezat (geregistreerde voorafgaande schenking + geleverd bewijs). Doel: voorkomen dat ouders via gesplitste aankoop het volledig goed belastingvrij naar de kinderen overhevelen.

<small>📚 Wetboek der Successierechten — art. 9 — _wettekst_</small>

#### 📜 Bedingen ten behoeve van derde (art. 4)  
_`regel`_

📖 Sommen die ten gevolge van een beding ten behoeve van derde door een derde worden ontvangen na het overlijden (bv. handgift met derden-beding, bepaalde maatschap-constructies), worden als legaat aangemerkt voor de erfbelasting (art. 4 W.Succ.). Geldt ook voor huwelijksvoordelen die kwalificeren als verkapte schenking aan langstlevende echtgenoot — sinds Vl-decreet 2018 specifiek geregeld via art. 2.7.1.0.4 VCF.

<small>📚 Wetboek der Successierechten — art. 4 — _wettekst_ · Vlaamse Codex Fiscaliteit — art. 2.7.1.0.4 — _wettekst_</small>

## Bouwstenen

### 🧮 Berekeningswijze per verkrijger  
_`formule`_

📖 Per verkrijger: (1) bepaal netto-aandeel = brutoverkrijging - aftrekbare passiva - vrijstellingen; (2) pas de toepasselijke tarieftabel toe (Tabel I rechte lijn/partner of Tabel II broers-zussen/anderen) volgens progressieve schijven; (3) tel verminderingen af (kinderen <21, broers/zussen, binnen-het-jaar, vriendenerfenis); (4) som de bedragen op alle erfgenamen. De berekening is dus per verkrijger en niet op de totale nalatenschap.

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.4.1.1 — _wettekst_ · Wetboek der Successierechten — art. 48 — _wettekst_</small>

### ⚙️ Wijze van heffing  
_`mechanisme`_

📖 De erfbelasting wordt gevestigd op zicht van de ingediende aangifte van nalatenschap. Bij niet-indiening, laattijdigheid, onjuistheid of onvolledigheid kan de fiscus de aanslag ambtshalve vestigen (VCF art. 2.7.7.0.1). Voor opeenvolgende overgangen van een onder opschortende voorwaarde verkregen goed is de belasting slechts wegens de laatste overgang verschuldigd (VCF art. 2.7.7.0.2).

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.7.0.1 — _wettekst_ · Vlaamse Codex Fiscaliteit — art. 2.7.7.0.2 — _wettekst_</small>

## Voorbeelden

### 💡 Vlaamse erfbelasting — overlijden ouder, één kind, gezinswoning 🔗

_Een Vlaamse erflater overlijdt en laat één kind na. Nalatenschap: gezinswoning 400.000 EUR, effectenportefeuille 200.000 EUR. Echtgenoot al overleden. Kind erft alles._

**Berekening:**
- Stap 1 — Nettoverkrijging kind: 600.000 EUR (geen langstlevende dus geen gezinswoning-vrijstelling).
- Stap 2 — Toepassing Tabel I (rechte lijn): schijf 1 = 0-50.000 × 3% = 1.500 EUR; schijf 2 = 50.000-250.000 × 9% = 18.000 EUR; schijf 3 = 350.000 × 27% = 94.500 EUR.
- Stap 3 — Totaal: 1.500 + 18.000 + 94.500 = 114.000 EUR erfbelasting.

→ **Resultaat**: Het kind betaalt 114.000 EUR op 600.000 EUR nettoverkrijging = 19% effectief.

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.4.1.1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Tarief toepassen op totale nalatenschap i.p.v. per verkrijger

**Verkeerde assumptie**: Studenten passen het tarief toe op de totale nalatenschap (bv. 600.000 EUR) en verdelen daarna.

**Kernpunt**: De tarieftabellen werken per verkrijger en op het netto-aandeel van die verkrijger. Vier kinderen die elk 150.000 EUR erven betalen elk afzonderlijk de progressieve schijven 3%-9% — niet de schijf 27% — wat substantieel verschilt van één kind dat 600.000 EUR alleen erft.

<small>📚 Wetboek der Successierechten — art. 48 — _wettekst_</small>

### ⚠️ Fictiebepalingen vergeten in aangifte

**Verkeerde assumptie**: Schenking die 2 jaar vóór overlijden gedaan werd zonder registratie 'telt niet meer mee'.

**Kernpunt**: Onregistreerde schenkingen binnen 3 jaar vóór overlijden vallen onder art. 7 W.Succ. en moeten in de aangifte van nalatenschap worden vermeld en belast tegen het tarief dat anders op de erfenis zou zijn toegepast.

<small>📚 Wetboek der Successierechten — art. 7 — _wettekst_</small>

### ⚠️ Gewestelijke tarieven verwarren

**Verkeerde assumptie**: Studenten leren één set tarieven (typisch Vlaamse) en passen ze toe ongeacht woonplaats van de erflater.

**Kernpunt**: De gewestelijke bevoegdheid leidt tot drie zeer verschillende tariefschalen. Eerst toepassingsregels checken (5-jaars-fiscale-woonplaats van de overledene), dan correcte gewestelijke tabel raadplegen (Vl: VCF 2.7.4.1.1; Br/Wal: regionaal W.Succ.). Bij grensoverschrijdende dossiers ook de buitenlandse aanknopingspunten checken.

<small>📚 Bijzondere Financieringswet — art. 5 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Fiscaal advies aan erfgenamen

_De accountant die de erfgenamen na overlijden begeleidt om de erfbelasting correct en optimaal te berekenen._

#### 💰 Fiscaal adviseur

##### 👣 Toepasselijk gewestelijk tarief bepalen  
_`stap`_

📖 Eerste stap: identificeer het toepasselijke gewest via de 5-jaars-fiscale-woonplaatsregel van de overledene. Indien in 5 jaar vóór overlijden in meerdere gewesten gewoond, geldt het gewest waar de overledene het langst gewoond heeft. Vervolgens: raadpleeg de actuele gewestelijke tarieftabel in het Cijferzakboekje (geen tarieven uit het hoofd toepassen — geïndexeerd of recent gewijzigd).

<small>📚 Bijzondere Financieringswet — art. 5 — _wettekst_ · Vlaamse Codex Fiscaliteit — art. 2.7.4.1.1 — _wettekst_</small>

##### 👣 Vrijstellingen + verminderingen optimaliseren  
_`stap`_

🔗 Doorloop systematisch alle beschikbare vrijstellingen en verminderingen: gezinswoning langstlevende partner (Vl 100%); gunstregime familiale onderneming (3% Vl); abattement roerend goed (Vl 50.000 EUR rechte lijn); kinderbijslag-vermindering (<21 jaar); vriendenerfenis (testament <01-01-2026); binnen-het-jaar-vermindering. Een niet-geclaimde vrijstelling is onnodige belasting.

<small>📚 Vlaamse Codex Fiscaliteit — art. 2.7.5.0.1 — _wettekst_ · Vlaamse Codex Fiscaliteit — art. 2.7.5.0.6 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Planning-advies na eerste overlijden  
_`vuistregel`_

🔗 Na eerste overlijden van een echtgenoot is de langstlevende partner een belangrijke planningsklant: gezinswoning is doorgaans vrijgesteld, maar de partner zit nu met een groot vermogen waarvan opnieuw erfbelasting zal worden geheven bij zijn/haar overlijden. Onderzoek schenkingen op leeftijd, levensverzekeringsplanning en gunstregime familiale onderneming. De binnen-het-jaar-regel (art. 57 W.Succ.) biedt automatische verzachting bij dichtbijzijnde overlijdens — maar plannen moet vooraf.

<small>📚 Wetboek der Successierechten — art. 57 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Aangifte-nalatenschap-procedure → [[aangifte-nalatenschap]] _(moet-verwijzen)_
- → Erfrecht-grondslag (burgerlijk recht) → [[erfrecht]] _(moet-verwijzen)_
- → Successieplanning instrumenten → [[successieplanning]] _(moet-verwijzen)_
- → Gunstregime familiale onderneming → [[gunstregime-familiale-onderneming]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[registratie-en-successierechten]]
### `triggert`
- [[aangifte-nalatenschap]] — Heffing volgt op de aangifte.
### `vereist`
- [[erfrecht]] — Burgerlijk recht bepaalt wie erfgenaam is + welke aandelen — de fiscale heffing bouwt daarop voort.
### `beinvloed_door`
- [[schenkbelasting]] — 3-jaarsregel + interactie schenking ↔ successie.
- [[huwelijksvermogensrecht]] — Wat tot de nalatenschap behoort hangt af van het huwelijksstelsel.
