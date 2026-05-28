---
title: "Eerste consolidatie"
concept_type: "verrichting"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
ankers:
  - 1.4.I.G
  - 1.4.II.D
tags:
  - concept
  - schema-2.2
  - type-verrichting
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/eerste-consolidatie.json"
---

# Eerste consolidatie

_Verrichting_

📅 Gebeurtenis · Anchors: `1.4.I.G` · `1.4.II.D` · Wave: `skeleton-cross-cutting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: initial consolidation · first consolidation — **Vertalingen**: fr: première consolidation · en: initial consolidation

## Definitie

📖 Eerste consolidatie is de boekhoudkundige verrichting waarmee een verworven (of voor het eerst gecontroleerde) dochter in de geconsolideerde jaarrekening wordt opgenomen. Op de overnamedatum worden de identificeerbare activa en verplichtingen van de dochter geherwaardeerd tegen reële waarde, het aandeel van de moeder daarin wordt vergeleken met de koopprijs, en het verschil komt op de geconsolideerde balans als goodwill (positief) of badwill (negatief).

<small>📚 KB-WVV — art. 3:130, eerste lid — _wettekst_ · IFRS 3 — Bedrijfscombinaties — §4-7 — _norm_ · CBN-advies 2013/3 — Inleiding — _cbn_</small>

## Substantie

🔗 Eerste consolidatie is geen routine-jaarafsluitings-verrichting maar een eenmalige 'foto' op de overnamedatum: alle cijfers van de dochter worden hertekend alsof de groep haar net gekocht heeft tegen marktprijs. Pas vanaf dat moment beweegt de boekhouding van de dochter mee met de groep. De fair-value-stap is cruciaal: zonder herwaardering zou de goodwill kunstmatig groot zijn (omdat boekwaarden vaak onder fair value liggen, vooral voor afgeschreven activa).

<small>📚 IFRS 3 — §10-17 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: KB-WVV art. 3:130 + IFRS 3 (via Verordening EU 2023/1803)

**✅ Voor**
- 📖 Elke verrichting waarmee een entiteit voor het eerst in de consolidatiekring komt: acquisitie, oprichting van een dochter, eerste keer overschrijden van de controle-drempel.

**▶️ Trigger start**
- 📖 De overnamedatum (acquisition date) is de datum waarop de moeder de controle verkrijgt. Niet noodzakelijk de signing-datum van het contract; vaak de closing-datum waarop de aandelen daadwerkelijk overgedragen worden. Onder IFRS 3 §8 wordt de overnamedatum gedefinieerd als de datum waarop de overnemer effectief de control over de overgenomen partij krijgt.

## Sub-concepten

### 📦 Procedure eerste consolidatie — 5 stappen  
_`procedure` (subconcept)_

#### Definitie

🔗 Standaardprocedure voor één nieuwe dochter in de kring.

<small>📚 KB-WVV — art. 3:130 — _wettekst_ · IFRS 3 — §4-17 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

#### 👣 Stap 1 — overnamedatum vaststellen  
_`stap`_

📖 Bepaal de exacte datum waarop control overgaat. Dit is vaak de closing-datum, niet de signing-datum. Belangrijk voor de cut-off van resultaten: enkel resultaat ná overnamedatum hoort tot de groep.

<small>📚 IFRS 3 — §8-9 — _norm_</small>

#### 👣 Stap 2 — koopprijs (consideration transferred)  
_`stap`_

📖 Bepaal de totale tegenprestatie: cash + uitgegeven aandelen (fair value) + overgenomen schulden + contingent consideration (fair value). Transactiekosten worden onder IFRS NIET in de koopprijs opgenomen — ze gaan rechtstreeks in resultaat (IFRS 3 §53).

<small>📚 IFRS 3 — §37-53 — _norm_</small>

#### 👣 Stap 3 — fair value identificeerbare activa en verplichtingen  
_`stap`_

📖 Herwaardeer elke identificeerbare actief en verplichting van de dochter naar fair value op overnamedatum. Identificeer immateriële activa die nog niet op de balans staan (klantenrelaties, merken, technologie). Voorwaardelijke verplichtingen ook opnemen indien betrouwbaar meetbaar. Externe waarderingsexperten (Purchase Price Allocation-experts) worden vaak ingeschakeld voor materiële overnames.

<small>📚 IFRS 3 — §10-17 — _norm_ · KB-WVV — art. 3:130, eerste lid — _wettekst_</small>

#### 👣 Stap 4 — consolidatieverschil bepalen  
_`stap`_

📖 Verschil = koopprijs − aandeel moeder in fair-value-NA dochter. Positief verschil = goodwill (op activa); negatief = badwill (na hertoetsing in resultaat). Bij minderheidsbelangen kiest de groep onder IFRS tussen 'partial goodwill' (alleen aandeel moeder in goodwill) en 'full goodwill' (volledige goodwill incl. aandeel minderheid).

<small>📚 IFRS 3 — §19, §32-36 — _norm_ · KB-WVV — art. 3:130-3:131 — _wettekst_</small>

#### 👣 Stap 5 — measurement period (IFRS) tot 12 maanden  
_`stap`_

📖 Onder IFRS 3 §45-50 heeft de overnemer maximaal 12 maanden ná overnamedatum om de fair-value-metingen te finaliseren ('measurement period'). Tijdens dat venster mogen aanpassingen retroactief naar overnamedatum geboekt worden. Na 12 maanden zijn correcties enkel nog mogelijk als foutcorrecties (IAS 8).

<small>📚 IFRS 3 — §45-50 — _norm_</small>

### 📦 Step acquisition — stapsgewijze verwerving  
_`verrichting` (subconcept)_

#### Definitie

📖 Bij een step acquisition (CBN-advies 2013/3) verwerft de moeder controle in meerdere stappen. Onder IFRS 3 §41-42 wordt de eerder aangehouden deelneming op overnamedatum geherwaardeerd naar fair value; het verschil met de boekwaarde gaat in resultaat. CBN volgt een andere benadering: elke stap apart verwerken met eigen consolidatieverschil-berekening.

<small>📚 CBN-advies 2013/3 — Praktische uitwerking — _cbn_ · IFRS 3 — §41-42 — _norm_</small>

## Voorbeelden

### 💡 Aurelia verwerft 80 % van Vermeer Verpakking BV 🔗

_Overnamedatum 1 oktober 2025. Aurelia betaalt 4.000.000 EUR cash. Boekwaarde eigen vermogen Vermeer: 3.500.000 EUR. Fair-value-herwaardering: gebouw +400.000 EUR (boekwaarde lager dan markt), niet-geboekte klantenrelaties +200.000 EUR, latente belastingschuld op herwaarderingen +150.000 EUR._

**Berekening:**
- Stap 1 — overnamedatum: 1 oktober 2025 (closing).
- Stap 2 — koopprijs: 4.000.000 EUR cash.
- Stap 3 — fair-value-NA Vermeer: 3.500.000 (boekwaarde) + 400.000 (gebouw) + 200.000 (klantenrelaties) − 150.000 (latente belasting) = 3.950.000 EUR.
- Stap 4a — aandeel moeder in fair-value-NA: 80 % × 3.950.000 = 3.160.000 EUR.
- Stap 4b — consolidatieverschil: 4.000.000 − 3.160.000 = 840.000 EUR positief → goodwill.
- Stap 4c — minderheidsbelangen (partial goodwill, B-GAAP-aanpak): 20 % × 3.950.000 = 790.000 EUR op passief 'belangen van derden'.
- Stap 5 — resultaat 1 januari–30 september 2025 van Vermeer: NIET in geconsolideerd resultaat (vóór overnamedatum). Resultaat 1 oktober–31 december: WEL in geconsolideerd resultaat, met 20 % toegerekend aan minderheidsbelangen.

→ **Resultaat**: Geconsolideerde balans 31 december 2025 toont: gebouw geherwaardeerd, klantenrelaties als immaterieel actief 200.000 EUR, goodwill 840.000 EUR, latente belastingschuld 150.000 EUR, belangen van derden 790.000 EUR.

<small>📚 KB-WVV — art. 3:130 — _wettekst_ · IFRS 3 — §10-19, §32 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Volledig boekjaar van dochter consolideren

**Verkeerde assumptie**: Wanneer Aurelia op 1 oktober 80 % van Vermeer koopt, neemt zij het volledige boekjaar (jan-dec) van Vermeer in de geconsolideerde resultatenrekening op.

**Kernpunt**: Enkel het resultaat ná overnamedatum hoort bij de groep. Resultaat 1 januari–30 september blijft bij de vroegere aandeelhouders en wordt niet geconsolideerd. Dit vereist een 'cut-off'-balans op overnamedatum (KB-WVV art. 3:130 + IFRS 3 §8-9).

<small>📚 IFRS 3 — §8-9 — _norm_ · KB-WVV — art. 3:130 — _wettekst_</small>

### ⚠️ Fair value-stap overslaan

**Verkeerde assumptie**: Boekwaarde eigen vermogen dochter gebruiken om consolidatieverschil te berekenen.

**Kernpunt**: Eerst ALLE activa en passiva van de dochter herwaarderen naar fair value op overnamedatum. Boekwaarde-vergelijking leidt tot kunstmatig opgeblazen goodwill (omdat boekwaarden vaak onder fair value liggen). Bijgevolg ook latente belastingen op herwaarderingen erkennen.

<small>📚 IFRS 3 — §10-17, §24-25 — _norm_ · KB-WVV — art. 3:130, eerste lid — _wettekst_</small>

### ⚠️ Transactiekosten in koopprijs opnemen onder IFRS

**Verkeerde assumptie**: Adviseurs-fees, due-diligence-kosten en bankcommissies worden aan de koopprijs toegevoegd en dus aan de goodwill toegerekend.

**Kernpunt**: IFRS 3 §53 zegt expliciet dat transactiekosten direct in winst-en-verliesrekening gaan in het jaar waarin ze opgelopen worden. Goodwill blijft beperkt tot het echte 'overgaande' verschil. Onder B-GAAP is de behandeling minder uniform; CBN-advies aanvaardt activering bij oprichtingskosten / immateriële activa, maar transactiekosten van overnames vallen typisch in resultaat.

<small>📚 IFRS 3 — §53 — _norm_</small>

## Accountant-perspectieven

### Overnemende groep

_De accountant die de eerste consolidatie technisch uitvoert en de PPA (Purchase Price Allocation) coördineert._

#### 📒 Boekhouder

##### 👣 Purchase Price Allocation uitvoeren  
_`stap`_

🔗 (1) Snelle inventarisatie van alle activa/passiva op overnamedatum (cut-off-balans van de dochter); (2) extern waarderingsexpert inschakelen voor onroerend goed, immateriële activa, voorraden van bijzondere waarde; (3) latente belastingen op herwaarderingen (vaak vergeten); (4) consolidatieverschil berekenen en boeken; (5) measurement period openen — markeer in dossier wanneer 12 maanden verstrijken voor afsluitende boeking.

<small>📚 IFRS 3 — §B41-B49, §24-25 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Advies bij deal-structurering  
_`vuistregel`_

🤖 Voor de signing: simulatie van post-acquisition geconsolideerde cijfers maken. Hoeveel goodwill ontstaat? Welke impact op groepsratio's (solvabiliteit, EBITDA-marge)? Welke latente belastingen worden geboekt? Bij hoge goodwill onder IFRS: management bewust maken van toekomstige impairment-risico en bijhorende communicatie-implicaties.

<small>📚 claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Consolidatieverschil (goodwill/badwill-rekening) → [[consolidatieverschil]] _(moet-verwijzen)_
- → Wijziging consolidatiekring (algemeen) → [[wijziging-consolidatiekring]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[wijziging-consolidatiekring]]
### `triggert`
- [[consolidatieverschil]]
