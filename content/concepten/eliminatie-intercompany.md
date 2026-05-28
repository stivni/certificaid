---
title: "Eliminatie van intercompany-verrichtingen"
concept_type: "verrichting"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
ankers:
  - 1.4.I.D
tags:
  - concept
  - schema-2.2
  - type-verrichting
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/eliminatie-intercompany.json"
---

# Eliminatie van intercompany-verrichtingen

_Verrichting_

📅 Gebeurtenis · Anchors: `1.4.I.D` · Wave: `skeleton-cross-cutting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: intercompany elimination · intra-group elimination — **Vertalingen**: fr: élimination des opérations intra-groupe · en: intercompany elimination

## Definitie

📖 Eliminatie van intercompany-verrichtingen is de boekhoudkundige stap waarmee in de consolidatie alle onderlinge transacties, vorderingen, schulden en niet-gerealiseerde winsten/verliezen tussen groepsentiteiten worden weggewerkt. Een groep mag niet 'aan zichzelf verkopen' — alle intra-groep-effecten verdwijnen zodat de geconsolideerde cijfers enkel transacties met derden tonen.

<small>📚 KB-WVV — art. 3:123 — _wettekst_ · KB-WVV — art. 3:127 — _wettekst_ · KB-WVV — art. 3:128 — _wettekst_ · IFRS 10 — §B86(c) — _norm_</small>

## Substantie

🔗 De groep wordt als één enkele economische entiteit gepresenteerd. Wanneer Aurelia een product aan haar dochter Zelena verkoopt, gebeurt er economisch niets buiten de groep — toch zou zonder eliminatie de geconsolideerde omzet en kostprijs allebei stijgen. Eliminatie zet beide bewegingen terug op nul. Hetzelfde geldt voor leningen tussen moeder en dochter, voor dividenden binnen de groep, en — moeilijker — voor winsten op intercompany-voorraad die nog niet aan derden zijn verkocht ('unrealised gains'). Op die laatste worden ook latente belastingen geboekt.

<small>📚 KB-WVV — art. 3:127 — _wettekst_ · IAS 12 — §39 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Zonder eliminatie zou de geconsolideerde jaarrekening de groep groter en winstgevender doen lijken dan ze werkelijk is. Bedrijven zouden via interne verkoop met opslag fictieve winsten kunnen creëren. De ratio legis van eliminatie is dezelfde als die van de geconsolideerde jaarrekening zelf: 'substance over form' — toon enkel wat de groep daadwerkelijk uit transacties met derden haalt. Het eliminatie-principe is universeel: B-GAAP (art. 3:123 KB-WVV: 'volledige eliminatie') en IFRS (IFRS 10 §B86c) zijn hier inhoudelijk identiek.

<small>📚 KB-WVV — art. 3:123 — _wettekst_ · IFRS 10 — §B86 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: KB-WVV art. 3:123 + art. 3:127 + art. 3:128 (B-GAAP) + IFRS 10 §B86 (IFRS)

**✅ Voor**
- 📖 Elke groep die integraal of evenredig consolideert. Bij evenredige consolidatie gebeurt eliminatie proportioneel; bij vermogensmutatie is eliminatie beperkter (enkel resultaten van transacties met de geassocieerde onderneming, voor zover informatie beschikbaar is — art. 3:142 § 2 KB-WVV).

## Sub-concepten

### 📦 Vier categorieën intercompany-eliminaties  
_`kader` (subconcept)_

#### Definitie

📖 (1) Wederzijdse vorderingen en schulden tussen groepsentiteiten; (2) wederzijdse opbrengsten en kosten (omzet ↔ aankopen); (3) niet-gerealiseerde winsten/verliezen op intercompany-verkopen waarvan de goederen nog in voorraad zijn bij de groep; (4) intra-groep-dividenden en aandelen-deelnemingen. Latente belastingen worden bij (3) bijgeboekt omdat het 'wegnemen' van winst een tijdelijk verschil creëert tussen geconsolideerde en fiscale waarde.

<small>📚 KB-WVV — art. 3:127 — _wettekst_ · KB-WVV — art. 3:128 — _wettekst_ · KB-WVV — art. 3:129 — _wettekst_ · IAS 12 — §39 — _norm_</small>

#### ⚙️ Wederzijdse vorderingen en schulden  
_`mechanisme`_

📖 Wanneer Aurelia 100 EUR vordert van Zelena, staat dezelfde 100 EUR als schuld op de balans van Zelena. In de geconsolideerde balans verdwijnen beide bedragen — netto-effect op groepsbalans = nul. Aandachtspunt: rekening-houden met cut-off-verschillen (vordering al geboekt, schuld nog niet) — vereist reconciliatie vóór eliminatie.

<small>📚 KB-WVV — art. 3:128 — _wettekst_</small>

#### ⚙️ Intercompany-omzet en -kosten  
_`mechanisme`_

📖 Wanneer Aurelia een dienst voor 50 EUR factureert aan Zelena, staat 50 EUR omzet bij Aurelia en 50 EUR kost bij Zelena. Geconsolideerd: beide worden geëlimineerd. Wanneer Zelena de dienst zelf doorrekent aan een externe klant, blijft enkel de eindverkoop in de geconsolideerde resultatenrekening.

<small>📚 KB-WVV — art. 3:127 — _wettekst_</small>

#### ⚙️ Niet-gerealiseerde winsten op intercompany-voorraad  
_`mechanisme`_

📖 Wanneer Aurelia goederen met een kostprijs van 80 verkoopt aan Zelena voor 100, en Zelena heeft die op balansdatum nog in voorraad, dan zit er 20 EUR 'winst' in de groepsvoorraad die economisch niet gerealiseerd is. Eliminatie: voorraad verminderen met 20 + omzet en kostprijs (elk 100 + 80) verwijderen. Latente belasting (IAS 12 §39): de aftrekbare tijdelijk verschil creëert een latente belastingvordering = 20 × tarief vennootschapsbelasting.

<small>📚 KB-WVV — art. 3:127 — _wettekst_ · IAS 12 — §39 — _norm_</small>

#### ⚙️ Deelnemingen en intra-groep-dividenden  
_`mechanisme`_

📖 De deelnemingsrekening van de moeder (klasse 28) wordt geëlimineerd tegen het aandeel in het eigen vermogen van de dochter (art. 3:129 KB-WVV). Dividenden die de dochter aan de moeder uitkeert, verdwijnen uit het geconsolideerd resultaat — anders zou dezelfde winst dubbel verschijnen (eens als winst bij dochter, eens als financieel resultaat bij moeder).

<small>📚 KB-WVV — art. 3:129 — _wettekst_ · CBN-advies 2022/11 — Intra-groepsdividenden — _cbn_</small>

## Voorbeelden

### 💡 Aurelia verkoopt voorraad met opslag aan Zelena 🔗

_Aurelia (moeder, 100 % deelneming in Zelena) heeft een product met kostprijs 800 EUR verkocht aan Zelena voor 1.000 EUR. Op balansdatum heeft Zelena het product nog in voorraad (niet doorverkocht aan derde). Vennootschapsbelasting Aurelia = 25 %._

**Berekening:**
- Stap 1 — opslag: 1.000 − 800 = 200 EUR ongerealiseerde intercompany-winst.
- Stap 2 — voorraad Zelena op groepsbalans verminderen met 200 EUR (terug naar groepskostprijs 800).
- Stap 3 — omzet Aurelia 1.000 elimineren tegen aankoop Zelena 1.000.
- Stap 4 — kostprijs verkopen Aurelia 800 elimineren (geen externe verkoop voorgevallen).
- Stap 5 — latente belastingvordering: 200 × 25 % = 50 EUR (op groepsbalans) + uitgestelde belastingbaat 50 EUR in geconsolideerd resultaat.

→ **Resultaat**: Geconsolideerd resultaat van deze transactie = nul (correcte voorstelling: economisch nog niets gerealiseerd). Voorraad verlaagd met 150 (200 − 50 latente belasting). Wanneer Zelena het product later aan een derde verkoopt voor 1.200 EUR: groepsomzet 1.200, kostprijs 800, brutowinst 400 — dat is het correcte beeld.

**Boeking:**


<small>📚 KB-WVV — art. 3:127 — _wettekst_ · IAS 12 — §39 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 💡 Intercompany-lening met interest 🔗

_Aurelia leent 500.000 EUR aan Zelena tegen 4 % per jaar. Op balansdatum: vordering Aurelia 500.000, schuld Zelena 500.000, ontvangen interest Aurelia 20.000, betaalde interest Zelena 20.000._

Eliminatie:
- Vordering 500.000 (Aurelia) ↔ schuld 500.000 (Zelena) → geconsolideerd 0.
- Interestopbrengst 20.000 (Aurelia) ↔ interestkost 20.000 (Zelena) → geconsolideerd 0.

Netto-effect op groepscijfers: balans krimpt met 500.000 (verdwijnt aan beide kanten); resultaat onveranderd. De groep heeft economisch enkel zichzelf geld geleend — geen vermogensbeweging buiten de groep.

<small>📚 KB-WVV — art. 3:127 — _wettekst_ · KB-WVV — art. 3:128 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Cut-off-verschillen negeren

**Verkeerde assumptie**: Wederzijdse vorderingen en schulden zijn altijd in balans en kunnen zonder reconciliatie geëlimineerd worden.

**Kernpunt**: In de praktijk zijn intercompany-saldi vaak NIET in balans op balansdatum: facturen onderweg, kosten geboekt vóór factuur, valuta-omzetting. Vóór eliminatie altijd een intercompany-reconciliatie uitvoeren, met identificatie van het verschil (cut-off, valuta, discussie). Onbalanseringen zonder verklaring leiden tot fouten in geconsolideerde balans.

<small>📚 KB-WVV — art. 3:128 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### ⚠️ Latente belasting op unrealised gains vergeten

**Verkeerde assumptie**: Bij eliminatie van intercompany-voorraadwinst hoeft enkel de winst zelf weggenomen te worden — latente belastingen zijn niet relevant.

**Kernpunt**: De geëlimineerde winst is fiscaal al belast (in hoofde van de verkopende entiteit), maar boekhoudkundig in de groep nog niet erkend. Dit creëert een aftrekbare tijdelijk verschil → latente belastingvordering (IAS 12 §39). Vergeten leidt tot overdreven impact op groepsresultaat.

<small>📚 IAS 12 — §39 — _norm_</small>

### ⚠️ Bij vermogensmutatie volledig elimineren

**Verkeerde assumptie**: Net als bij integrale consolidatie worden intercompany-transacties met een geassocieerde onderneming volledig geëlimineerd.

**Kernpunt**: Bij vermogensmutatie wordt enkel het aandeel van de groep in unrealised gains/losses geëlimineerd, en dan nog 'voor zover informatie beschikbaar is' (art. 3:142 § 2 KB-WVV + IAS 28 §28). De geassocieerde onderneming staat niet integraal in de groep; eliminatie is dus beperkter.

<small>📚 KB-WVV — art. 3:142 § 2 — _wettekst_ · IAS 28 — §28 — _norm_</small>

## Accountant-perspectieven

### Groep — consolidator

_Accountant die de eliminatie-stap uitvoert op het consolidatie-werkblad._

#### 📒 Boekhouder

##### 👣 Intercompany-reconciliatie vóór eliminatie  
_`stap`_

🔗 Op consolidatiedatum: (1) lijst alle intercompany-saldi op uit hoofd-grootboeken van elke dochter; (2) match per tegenpartij (Aurelia vs Zelena, Aurelia vs Vermeer, ...); (3) onderzoek verschillen > materialiteit; (4) corrigeer cut-off-fouten op niveau van dochter (niet via eliminatie); (5) bekom een gestabiliseerde lijst van saldi voor eliminatie. Aandachtspunt: valuta-verschillen bij buitenlandse dochters apart afhandelen.

<small>📚 KB-WVV — art. 3:128 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 Audit van eliminatieboekingen  
_`stap`_

🔗 De commissaris controleert de volledigheid en juistheid van eliminaties: (1) zijn alle materiële intercompany-relaties geïdentificeerd? (2) zijn cut-off-verschillen verklaard? (3) zijn unrealised gains correct berekend (vooral bij intercompany-voorraad)? (4) is latente belasting geboekt? Bij grote groepen vaak een 'intercompany-audit'-module met steekproef op grootste tegenpartijen.

<small>📚 ISA 600 — §22, §A22-A24 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Opmaak-geconsolideerde-jaarrekening (procedure) → [[opmaak-geconsolideerde-jaarrekening]] _(moet-verwijzen)_
- ↪ Voorraden-context (bij intercompany-voorraadverkoop) → [[voorraden]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[opmaak-geconsolideerde-jaarrekening]]
