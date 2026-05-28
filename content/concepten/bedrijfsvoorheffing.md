---
title: "Bedrijfsvoorheffing"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.taak.3
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/bedrijfsvoorheffing.json"
---

# Bedrijfsvoorheffing

_Regime_

📋 Regeling · Anchors: `2.2.taak.3` · Wave: `skeleton-cross-cutting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Afk.**: BV — **Synoniemen**: précompte professionnel — **Vertalingen**: fr: précompte professionnel

## Definitie

📖 Bedrijfsvoorheffing (BV) is een gedeeltelijke voorheffing op de inkomstenbelasting (PB of BNI), opeisbaar bij het betalen of toekennen van belastbare bezoldigingen, pensioenen, renten of toelagen (art. 273 WIB92). De voorheffing is verschuldigd door de werkgever, schuldenaar of mandataris (art. 270 WIB92), die ze van het brutobedrag inhoudt en aan de fiscus doorstort. De berekening gebeurt forfaitair volgens schalen vastgesteld door de Koning (KB/WIB art. 86-95 + Bijlage III), naargelang de categorie inkomen, de gezinssituatie en de kinderlast.

<small>📚 WIB92 — art. 270, 273, 275 — _wettekst_</small>

## Substantie

🔗 BV is het 'pay-as-you-earn'-systeem van de Belgische personenbelasting. Het systeem heeft drie effecten: (1) **Spreiding voor de overheid** — maandelijkse cash-flow in plaats van één betaling per jaar. (2) **Aansprakelijkheid bij de werkgever** — de werkgever is fiscaal aansprakelijk voor de juiste berekening + tijdige doorstorting (art. 272 + boetes art. 444 e.v.); een vergissing (onder-inhouding) levert hem een rechtstreekse schuld bij de fiscus op. (3) **Quasi-eindafrekening voor werknemers** — voor zuivere loontrekkenden met geen andere inkomsten ligt het ingehouden bedrag dicht bij de finale PB; bij gemengde inkomens (loon + huur + dividenden) of gunstvariabelen (huwelijksquotient, kinderlast laat aangepast) ontstaan correcties via de finale aanslag. Vanaf 2003 bestaan 'BV-vrijstellingen van doorstorting' (R&D-onderzoekers, ploegen-/nachtarbeid, overuren, startende ondernemingen) als steunmechanisme: de werkgever houdt wel BV in, maar mag een percentage niet doorstorten — een directe loonkost-subsidie.

<small>📚 WIB92 — art. 270, 272, 275 — _wettekst_</small>

## Rationale

🔗 De BV als bronheffing is een algemeen principe in moderne belastingstelsels (PAYE in VK, prélèvement à la source in FR, Lohnsteuer in DE). Drie redenen: (a) belastinginkomsten worden gespreid over het jaar i.p.v. één piek bij eindafrekening; (b) de overheid verzekert zich tegen wanbetaling/insolvabiliteit van de belastingplichtige; (c) administratieve eenvoud voor de meeste belastingplichtigen (75-80 % van de loontrekkenden hoeven geen aanvulling te betalen).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 270-275 + KB/WIB art. 86-95 + Bijlage III

**✅ Voor**
- 📖 Bij elke uitbetaling van bezoldiging (werknemer of bedrijfsleider), pensioen, vervangingsinkomen door een Belgische schuldenaar.

**▶️ Trigger start**
- 📖 Betalen of toekennen van bezoldigingen (art. 273-1°) — dus het moment van uitbetaling (boekhoudkundig: D 455/618 C 5500), niet de datum van prestatie.

## Bouwstenen

### 📜 Schuldenaars BV (art. 270)  
_`regel`_

📖 BV is verschuldigd door (art. 270 WIB92): (1) personen die bezoldigingen, pensioenen, renten of toelagen betalen of toekennen — werkgever, vennootschap, RSZ, RVA, pensioenfonds; (2) opdrachtgevers van werknemers wier loon hoofdzakelijk uit fooien bestaat; (3) schuldenaars van inkomsten van podiumkunstenaars/sportbeoefenaars; (4) mandatarissen van niet-inwoners. De BV moet worden ingehouden (art. 272) zonder dat partijen contractueel kunnen afwijken — d.w.z. de werknemer ontvangt netto, niet bruto.

<small>📚 WIB92 — art. 270, 272 — _wettekst_</small>

### 📜 BV-schalen en parameters (KB/WIB Bijlage III)  
_`regel`_

📖 De BV wordt berekend volgens schalen vastgesteld bij KB (art. 275 § 1, in uitvoering art. 86-95 KB/WIB + Bijlage III). Drie hoofdschalen: (I) gewone bezoldigingen werknemers (maandelijks/wekelijks); (II) bedrijfsleiders; (III) vervangingsinkomens/pensioenen. Parameters: bruto-belastbaar bedrag, burgerlijke staat (alleenstaande/gehuwd/wettelijk samenwonend), gezinslast (aantal kinderen ten laste, gehandicapt kind, andere personen ten laste), specifieke verminderingen (bv. lage lonen, woon-werk). De BV-schaal is daarom progressief gestaffeld zodat ze een eerste benadering geeft van de finale PB.

<small>📚 WIB92 — art. 275 § 1 — _wettekst_ · KB/WIB 92 — art. 86-95 + Bijlage III — _kb_</small>

### ⚙️ Aangifteformulieren 274 + fiches 281  
_`mechanisme`_

**Substantie**: 📖 Twee periodieke verplichtingen:

<small>📚 KB/WIB 92 — art. 86-95 — _kb_</small>

### 📜 Verrekening BV op finale PB (art. 296)  
_`regel`_

📖 De ingehouden BV wordt op de finale aanslag PB van de belastingplichtige verrekend (art. 296 WIB92). Indien BV > finale PB: terugbetaling. Indien BV < finale PB: te-betalen-saldo. Drie correctieoorzaken: (a) inkomsten buiten loon (huur, dividenden, alimentatie) waarop geen BV werd ingehouden; (b) verminderingen niet door werkgever toegepast (bv. extra kinderlast tijdens jaar); (c) belastingvermindering (langetermijnsparen, pensioenfonds) die enkel via aangifte werkt. Loontrekkenden zonder andere inkomsten zien typisch een kleine teruggave (≈ € 100-300) of een klein saldo.

<small>📚 WIB92 — art. 296 — _wettekst_</small>

### ↪️ Vrijstelling van doorstorting BV — steunmechanisme  
_`uitzondering`_

📖 Voor bepaalde categorieën van werkgevers/werknemers houdt de werkgever wel de BV in op het loon (werknemer 'voelt het niet'), maar moet hij een **percentage van die BV NIET doorstorten** aan de fiscus — wat een directe loonkost-subsidie is voor de werkgever (art. 275 § 3 e.v. WIB92). Belangrijkste: BV-vrijstelling onderzoekers/R&D (80 % op masters in wetenschappelijke richtingen, art. 275/3); ploegen- en nachtarbeid (22,8 %, art. 275/5); overuren (vrijstelling op de eerste 130 uur, art. 275/1); startende ondernemingen (10/20 % voor 4 jaar). Aangifte 274.32 / 274.33 voor afzonderlijke claim.

<small>📚 WIB92 — art. 275/1, 275/3, 275/5 — _wettekst_</small>

### 📜 Boekhoudkundige verwerking (rekening 4530)  
_`regel`_

📖 BV wordt boekhoudkundig geboekt op rekening 4530 'Ingehouden voorheffingen — Bedrijfsvoorheffing' (MAR). Bij toekenning bezoldiging: D 620/618 / C 4530 + 454 + 455. Bij doorstorting: D 4530 / C 5500. Saldo 4530 op balansdatum = nog niet-doorgestorte BV (typisch december-BV die in januari doorgestort wordt → vlottend passief).

<small>📚 MAR (KB 21.10.2018) — Bijlage 1, rek. 4530 — _kb_</small>

## Voorbeelden

### 💡 Werknemer bruto € 3.000/maand — BV-berekening en boeking 🔗

_Alleenstaand, geen kinderen ten laste. BV-schaal werknemers (illustratief, AJ 2025)._

**Berekening:**

**Boeking:**


<small>📚 WIB92 — art. 270, 296 — _wettekst_ · KB/WIB 92 — art. 86-95 + Bijlage III — _kb_</small>

### 💡 Verrekening BV op finale aanslag — kleine teruggave 🔗

_Werknemer bruto € 45.000 jaar X; BV ingehouden € 9.500; aanvulling huwelijksquotient (huwelijk met niet-werkende partner) effect € 1.200 belastingvermindering._

**Berekening:**

<small>📚 WIB92 — art. 87, 296 — _wettekst_</small>

### 💡 BV-vrijstelling 80 % onderzoekers (art. 275/3) 📖

_Tech-vennootschap met 5 onderzoekers (master wetenschap/ingenieurswetenschap). Brutoloon elk € 4.500/maand. BV ingehouden ± € 1.200/maand per onderzoeker._

**Berekening:**

<small>📚 WIB92 — art. 275/3 — _wettekst_</small>

## Valkuilen

### ⚠️ BV ingehouden ≠ definitieve PB

**Verkeerde assumptie**: De BV-inhouding is de definitieve belasting op het loon.

**Kernpunt**: BV is een voorheffing — een 'voorschot' (art. 273). De finale aanslag PB (AJ X+1) wordt berekend op het wereldwijd belastbaar inkomen, met alle correcties (huwelijksquotient, kinderlast laat aangepast, langetermijnsparen, dividenden, huur). BV wordt dan verrekend (art. 296) en kan tot teruggave OF te-betalen-saldo leiden.

<small>📚 WIB92 — art. 273, 296 — _wettekst_</small>

### ⚠️ Werkgever aansprakelijk bij onder-inhouding (geen verhaal op werknemer)

**Verkeerde assumptie**: Wanneer de werkgever vergeet BV in te houden, krijgt hij dat bedrag later terug van de werknemer.

**Kernpunt**: Art. 272 + 444 WIB stellen de werkgever rechtstreeks aansprakelijk voor onder-inhouding. De fiscus vordert de niet-ingehouden BV bij de werkgever (niet bij de werknemer) + boete. De werkgever heeft theoretisch een burgerlijk verhaal op de werknemer, maar in de praktijk vaak verloren wegens fout van de werkgever zelf.

<small>📚 WIB92 — art. 272 — _wettekst_</small>

### ⚠️ BV op VAA mag niet vergeten worden

**Verkeerde assumptie**: Op een voordeel alle aard wordt geen BV ingehouden want er gaat geen geld door.

**Kernpunt**: VAA wordt fiscaal als belastbaar loon beschouwd. De werkgever moet maandelijks BV inhouden op het fictief totaalloon (geldloon + VAA-forfait per maand). Vergeet hij dat, dan blijft hij aansprakelijk. Sociaal secretariaat doet dit normaliter automatisch, maar boekhouder moet controleren dat alle VAA op fiche 281.10/281.20 staan.

<small>📚 WIB92 — art. 31, 273 — _wettekst_</small>

## Accountant-perspectieven

### Boekhouder/HR-administrator bij werkgever

_Maandelijkse cyclus berekening + aangifte 274 + jaarafsluiting fiches 281._

#### 📒 Boekhouder

##### 👣 Maandcyclus BV-administratie  
_`stap`_

**Substantie**: 🔗 (1) Verkrijg loonstrook + samenvatting van sociaal secretariaat. (2) Controleer BV-bedrag (eventueel via simulator-tool voor steekproef). (3) Boek 620/618 D bruto + 4530 C BV + 454 C RSZ + 455 C netto. (4) Vóór 15e van maand M+1: aangifte 274 elektronisch indienen + BV via Belconnect doorstorten. (5) Bij jaareinde: fiches 281.10/281.20 + opgave 325 indienen vóór 1 maart.

<small>📚 WIB92 — art. 270-275 — _wettekst_</small>

#### 💰 Fiscaal adviseur

##### 👣 Claim BV-vrijstelling R&D / ploegen / overuren  
_`stap`_

**Substantie**: 📖 (1) Identificeer kwalificerende werknemers (master wetenschap voor R&D-vrijstelling; ploegenarbeid > X% prestatie; overuren > 130/jr). (2) Houd normale BV in op loon (werknemer-side ongewijzigd). (3) Bereken vrijstellingspercentage (80 % R&D / 22,8 % ploegen / 41,25 % overuren). (4) Vul aangifte 274.33 (R&D), 274.32 (ploegen), 274.31 (overuren). (5) Documenteer Belspo-erkenning + ploegrooster + uurstaten in dossier (controle-bestand). (6) Doorstort enkel niet-vrijgesteld deel.

<small>📚 WIB92 — art. 275/1, 275/3, 275/5 — _wettekst_</small>

## Verder lezen (scope-out)

- → Werknemers-bezoldiging — onderworpen-grondslag → [[werknemersbezoldiging]] _(moet-verwijzen)_
- → Bedrijfsleidersbezoldiging — onderworpen-grondslag → [[bedrijfsleidersbezoldiging]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[personenbelasting]]
### `beinvloed_door`
- [[werknemersbezoldiging]]
- [[bedrijfsleidersbezoldiging]]
