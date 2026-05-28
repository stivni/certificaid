---
title: "Wijziging consolidatiekring"
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
gegenereerd_uit: "data/concepten/records/wijziging-consolidatiekring.json"
---

# Wijziging consolidatiekring

_Verrichting_

📅 Gebeurtenis · Anchors: `1.4.I.G` · `1.4.II.D` · Wave: `skeleton-consolidatie-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: changes in scope of consolidation · consolidation scope changes

## Definitie

📖 Een wijziging in de consolidatiekring is elke gebeurtenis tijdens een boekjaar waardoor een entiteit aan de groep wordt toegevoegd (acquisitie van een dochter/JV/associate, oprichting), uit de groep verdwijnt (verkoop, vereffening, verlies van controle), of een ander statuut krijgt (verhoging van associate naar dochter via stap-acquisitie; verlaging van dochter naar associate bij verlies van controle). De geconsolideerde jaarrekening moet die wijzigingen pro rata temporis weergeven: een dochter verworven op 1 juli wordt voor 6 maanden geconsolideerd; een verkochte dochter telt mee tot de afstotings-datum. Art. 3:125 KB WVV en IFRS 10 + IFRS 3 regelen de specifieke verwerking.

<small>📚 KB WVV — art. 3:125 — _kb_ · Verordening (EU) 2023/1803 — IFRS 10 alinea 19-26 — _wettekst_</small>

## Substantie

📖 Vier typische scenario's: (1) Nieuwe acquisitie — een vennootschap wordt voor het eerst geconsolideerd → eerste consolidatie + bepaling consolidatieverschil + opname pro rata vanaf verkrijgingsdatum (control date, IFRS 3). (2) Verkoop met verlies van controle — dochter verlaat de kring → verwijderen activa/passiva uit groepsbalans + recyclage CTA + winst/verlies-bepaling. (3) Stap-acquisitie — bv. een 25 %-associate wordt door extra aankoop van 30 % een 55 %-dochter → onder IFRS: fair-value-stap-up van het bestaande belang naar verkrijgingsdatum (step-up via P&L). (4) Partiële verkoop zonder verlies van controle — geen P&L-impact, wel herallocatie tussen groeps-EV en minderheidsbelang (IFRS 10 alinea 23). De gemeenschappelijke regel: alleen het deel van het resultaat dat verband houdt met de groeps-periode wordt opgenomen — pro rata temporis op de datum van verandering.

<small>📚 KB WVV — art. 3:125 — _kb_ · Verordening (EU) 2023/1803 — IFRS 10 alinea 23, 25; IFRS 3 alinea 41-42 — _wettekst_</small>

## Rationale

🔗 Ratio: een onderneming hoort pas tot de groep vanaf het moment dat de controle (of invloed, of gezamenlijke controle) wordt verworven. Het zou de gebruiker misleiden om bv. een vóór de overname behaald verlies van een dochter aan de groep toe te schrijven — die was toen nog geen groepsentiteit. Tegelijk moet bij verkoop de relatie afgebroken worden vanaf het moment dat controle verloren gaat — anders wordt na-verkoop-resultaat ten onrechte in de groeps-RR opgenomen. Pro rata temporis garandeert dat alleen de juiste periode wordt geconsolideerd.

<small>📚 KB WVV — art. 3:125 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: KB WVV art. 3:125 (Belgisch); IFRS 10 + IFRS 3 (internationaal)

Stabiele regeling. IFRS 3 (Business Combinations, 2008) bracht de stap-acquisitie-fair-value-step-up-vereiste.

## Sub-concepten

### 📦 Acquisitie tijdens het jaar  
_`verrichting` (subconcept)_

#### Definitie

📖 Bij verwerving van een dochter op datum D tijdens het boekjaar: vanaf D wordt de balans van de dochter integraal opgenomen. Het resultaat van de dochter wordt voor de periode D tot balansdatum opgenomen in de groeps-RR. De cijfers vóór D blijven volledig buiten de groepsrekeningen — die periode behoorde de dochter niet tot de groep. Het consolidatieverschil wordt berekend op basis van het EV van de dochter op datum D (niet op begin- of einde-boekjaar).

<small>📚 KB WVV — art. 3:125 §1 — _kb_ · Verordening (EU) 2023/1803 — IFRS 3 alinea 8-9 — _wettekst_</small>

#### 📜 Bepaling verkrijgingsdatum (acquisition date)  
_`regel`_

📖 De verkrijgingsdatum is de datum waarop de overnemende partij effectief controle verwerft (IFRS 3 alinea 8). Vaak de closing date van de transactie, maar niet altijd — het is de juridische én economische overdracht. De aandelenovereenkomst kan een datum stipuleren, maar opschortende voorwaarden (regulatoire goedkeuring, due diligence) kunnen de werkelijke datum verschuiven. Documenteer zorgvuldig — alle daaropvolgende boekingen hangen ervan af.

<small>📚 Verordening (EU) 2023/1803 — IFRS 3 alinea 8-9 — _wettekst_</small>

### 📦 Desinvestering (verkoop dochter)  
_`verrichting` (subconcept)_

#### Definitie

📖 Bij verkoop op datum D: cijfers van de dochter tot D worden in de groeps-RR opgenomen (laatste pro-rata-periode). Op de afstotingsdatum: (a) activa en passiva van de dochter worden uit de groepsbalans verwijderd; (b) minderheidsbelang (zo aanwezig) wordt verwijderd; (c) eventueel niet-gerecycleerde CTA wordt overgeboekt naar de RR; (d) opbrengst van verkoop minus boekwaarde netto-activa-dochter (inclusief overgebleven goodwill) = winst/verlies op verkoop, gerapporteerd in groeps-RR.

<small>📚 Verordening (EU) 2023/1803 — IFRS 10 alinea 25; IAS 21 alinea 48 — _wettekst_</small>

### 📦 Stap-acquisitie (control bereiken in stappen)  
_`verrichting` (subconcept)_

#### Definitie

📖 Wanneer een bestaande deelneming (bv. 25 %-associate, VMM) wordt opgehoogd door extra aankoop tot een controlerend belang (bv. 55 %), gelden onder IFRS de regels van IFRS 3 'business combination achieved in stages' (alinea 41-42): het bestaande belang wordt geherwaardeerd naar fair value op de verkrijgingsdatum; het verschil tussen fair value en VMM-boekwaarde komt in de RR (fair-value-step-up gain/loss); cumulatieve CTA + OCI-componenten verbonden aan het oude belang worden gerecycleerd naar RR; vanaf dan integrale consolidatie.

<small>📚 Verordening (EU) 2023/1803 — IFRS 3 alinea 41-42 — _wettekst_</small>

### 📦 Verlies van controle (zonder volledige verkoop)  
_`verrichting` (subconcept)_

#### Definitie

📖 Wanneer de moeder controle verliest (bv. door verkoop van een deel maar niet alle aandelen, of door verwatering bij kapitaalverhoging zonder participatie), gelden de regels van IFRS 10 alinea 25-26: derecognise alle activa + passiva + NCI van de dochter; recycle de cumulatieve CTA en OCI; herwaardeer het overblijvend belang naar fair value (start-meting voor IFRS 9, IAS 28 of IFRS 11 — afhankelijk van de nieuwe relatie); verschil = winst/verlies in groeps-RR. Onderscheid duidelijk: gedeeltelijke verkoop ZONDER verlies controle = enkel EV-beweging (alinea 23); MET verlies controle = volledige derecognition + remeasurement.

<small>📚 Verordening (EU) 2023/1803 — IFRS 10 alinea 23, 25-26 — _wettekst_</small>

## Bouwstenen

### 📜 Pro-rata-temporis-toepassing  
_`regel`_

🔗 Toepassing pro rata temporis op het resultaat van een nieuw verworven of verkochte dochter: in praktijk worden ofwel (1) tussentijdse rekeningen op de verkrijgings-/afstotingsdatum opgemaakt en die periode-cijfers in de groepscijfers opgenomen; ofwel (2) bij benadering: het volledige jaarresultaat wordt evenredig verdeeld naar maanden/dagen — methode 2 alleen toegelaten bij stabiele resultatenverdeling. Methode 1 is principieel (geeft accuratere cijfers), maar duur — methode 2 in praktijk frequent voor niet-materiële acquisities.

<small>📚 KB WVV — art. 3:125 §1 — _kb_ · Verordening (EU) 2023/1803 — IFRS 3 alinea 8 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 IFRS 12 — toelichting wijzigingen consolidatiekring  
_`regel`_

📖 IFRS 12 alinea 12 + B10 vereisen dat de geconsolideerde toelichting de samenstelling van de groep vermeldt + de wijzigingen tijdens het jaar (acquisities, desinvesteringen, oprichtingen). Per materiële business combination: aankoopprijs, fair value identifiable net assets, goodwill, gerealiseerde winst/verlies, redenen voor verwerving. Per desinvestering met verlies van controle: winst/verlies + uitsplitsing naar herwaardering vs verkoopopbrengst.

<small>📚 Verordening (EU) 2023/1803 — IFRS 12 alinea 12, B10 — _wettekst_ · Verordening (EU) 2023/1803 — IFRS 3 alinea 59-63 — _wettekst_</small>

## Voorbeelden

### 💡 Acquisitie dochter op 1 juli — pro rata 6 maanden 🔗

_Groep G koopt op 1/7/2024 100 % aandelen van dochter D voor 5.000 EUR. EV D op 1/7/2024 = 4.500 EUR. D's resultaat 2024: 600 EUR (waarvan 250 in H1, 350 in H2). Groep G heeft boekjaar = kalenderjaar._

**Berekening:**
- Stap 1 — Consolidatieverschil = 5.000 - 4.500 = 500 (positieve goodwill, geactiveerd)
- Stap 2 — In groeps-balans 31/12/2024: alle activa + passiva D integraal opgenomen (per 31/12/2024-stand) + goodwill 500
- Stap 3 — In groeps-RR 2024: alleen resultaat D voor periode 1/7 - 31/12 = 350 EUR opgenomen
- Stap 4 — De 250 EUR resultaat H1 zit NIET in groepscijfers — die behoorde D nog niet tot de groep
- Stap 5 — Belangrijk: groeps-vergelijkende cijfers 2023 bevatten ZERO van D (was nog niet in kring)

→ **Resultaat**: Pro rata temporis: 6/12-de van het resultaat (of meer accuraat: H2-cijfer 350) wordt opgenomen. De jaarrekening D voor H1 wordt apart bewaard maar niet geconsolideerd.

<small>📚 KB WVV — art. 3:125 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Stap-acquisitie — van 25 % associate naar 55 % dochter 🔗

_Groep G hield sinds 2022 25 % in A (associate, VMM). DW-boekwaarde 1/1/2024 = 800 EUR. Op 1/1/2024 koopt G nog 30 % bij voor 1.500 EUR. Fair value van de hele entiteit A op 1/1/2024 = 5.000 EUR._

**Berekening:**
- Stap 1 — Fair value oude belang (25 %) = 25 % × 5.000 = 1.250 EUR
- Stap 2 — Stap-up gain = 1.250 - 800 (oude DW) = 450 EUR — in RR 2024
- Stap 3 — Acquisitieprijs nieuwe 30 % = 1.500 EUR
- Stap 4 — Totale 'cost of investment' voor IFRS 3-doel = FV oud belang + nieuwe prijs = 1.250 + 1.500 = 2.750 EUR voor 55 %
- Stap 5 — Identifiable net assets fair value × 55 % wordt afgeleid van due-diligence-waardering. Goodwill = 2.750 - aandeel in identifiable net assets
- Stap 6 — Vanaf 1/1/2024 integrale consolidatie van A (was VMM)

→ **Resultaat**: De step-up gain (450) raakt het groeps-resultaat 2024. Daarna verloopt A als gewone dochter in de groep.

<small>📚 Verordening (EU) 2023/1803 — IFRS 3 alinea 41-42 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Volledige jaarresultaat van nieuwe dochter opnemen

**Verkeerde assumptie**: Bij acquisitie van een dochter in juli: heel haar jaarresultaat in groeps-RR.

**Kernpunt**: Alleen het deel ná verkrijgingsdatum hoort thuis in groep. Een acquisitie op 1 juli → maximaal 6 maanden resultaat in groepscijfers. Volledige jaarresultaat opnemen overschat groeps-resultaat — typische fout bij eerste consolidatie.

<small>📚 KB WVV — art. 3:125 — _kb_ · Verordening (EU) 2023/1803 — IFRS 3 alinea 8 — _wettekst_</small>

### ⚠️ Stap-acquisitie: oud belang aan boekwaarde laten

**Verkeerde assumptie**: Bij stap-acquisitie blijft het oude VMM-belang aan zijn boekwaarde, alleen het nieuwe deel wordt aan acquisitieprijs gewaardeerd.

**Kernpunt**: IFRS 3 alinea 41-42 vereist remeasurement van het oude belang naar fair value op verkrijgingsdatum — het verschil komt door P&L. Vergeten van de step-up onder-rapporteert goodwill én onder-rapporteert de winst die de groep maakte op haar eerdere belang.

<small>📚 Verordening (EU) 2023/1803 — IFRS 3 alinea 41-42 — _wettekst_</small>

### ⚠️ Gedeeltelijke verkoop zonder controleverlies: winst boeken

**Verkeerde assumptie**: Verkoop van 10 % van een 80 %-dochter (resterend 70 %, nog steeds controle) → winst in RR.

**Kernpunt**: IFRS 10 alinea 23: een transactie met aandeelhouders die geen verlies van controle veroorzaakt = equity-transactie, geen P&L-impact. Verschil tussen ontvangen prijs en boekwaarde van overgedragen NCI-deel komt rechtstreeks in EV. Anders bij verlies van controle (alinea 25-26): volledig P&L-impact.

<small>📚 Verordening (EU) 2023/1803 — IFRS 10 alinea 23, 25-26 — _wettekst_</small>

## Accountant-perspectieven

### Groep met M&A-activiteit

_De accountant van een actief overnemend bedrijf._

#### 📒 Boekhouder

##### 👣 Van due diligence naar eerste consolidatie  
_`stap`_

📖 Pre-deal: due-diligence-waardering levert reële waarde van identifiable assets + liabilities van de target. Op verkrijgingsdatum: openings-balans target opmaken in groepswaarderingsregels + fair-value-stap (purchase price allocation, PPA — IFRS 3 alinea 18-31). PPA-periode: max 12 maanden om provisional values te finaliseren. Documenteer goodwill-allocatie naar cash-generating units (IAS 36).

<small>📚 Verordening (EU) 2023/1803 — IFRS 3 alinea 18-31, 45-50; IAS 36 — _wettekst_</small>

#### 💰 Fiscaal adviseur

##### 📜 Fiscale impact wijziging consolidatiekring  
_`regel`_

📖 Belangrijke aandachtspunten: (1) bij verwerving Belgische dochter — DBI-aftrek (art. 202 WIB92) voor toekomstige dividenden indien deelneming-vereisten vervuld (10 % + 12 maanden); (2) bij verkoop met meerwaarde — vrijstelling onder art. 192 WIB92 indien deelneming-aandeel niet als belegging gekwalificeerd; (3) bij stap-acquisitie: fair-value-step-up gain in de groepscijfers is geen belastbaar resultaat (geen reële transactie); (4) goodwill is fiscaal niet aftrekbaar in België (art. 198 WIB92, geen impairment), wel onder IFRS via impairment-test.

<small>📚 WIB92 — art. 192 — _wettekst_ · WIB92 — art. 198 — _wettekst_ · WIB92 — art. 202 — _wettekst_</small>

#### 🔍 Auditor

##### 👣 Audit wijziging consolidatiekring  
_`stap`_

📖 Specifieke audit-aandachtspunten: (1) verkrijgings-/afstotingsdatum-bepaling (impact op pro-rata-periode); (2) PPA-volledigheid en redelijkheid (waardering identifiable intangibles, contingent considerations); (3) bij stap-acquisities: correcte fair-value-remeasurement oude belang; (4) recyclage CTA bij verlies van controle; (5) IFRS 12-toelichting compleet (samenstelling kring + wijzigingen + materiale acquisities). ISA 540 voor schattingen-elementen in PPA.

<small>📚 ISA 540 — Vereisten — _norm_ · ISA 600 — Bijlage 2 — _norm_ · Verordening (EU) 2023/1803 — IFRS 3, IFRS 10, IFRS 12 — _wettekst_</small>

## Verder lezen (scope-out)

- → Eerste consolidatie (initial-consolidation) → [[eerste-consolidatie]] _(moet-verwijzen)_
- → Consolidatiekring (algemeen overzicht) → [[consolidatiekring]] _(moet-verwijzen)_
- ↪ Reorganisatie (fusie-context) _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[geconsolideerde-jaarrekening]]
### `vereist`
- [[consolidatiekring]]
### `triggert`
- [[consolidatieverschil]] — Elke nieuwe acquisitie genereert een te bepalen consolidatieverschil (goodwill of badwill).
- [[minderheidsbelangen]] — Wijziging in % bezit beïnvloedt het minderheidsbelang.
### `vergelijkbaar_met`
- [[eerste-consolidatie]]
    - **Gelijkenissen**:
        - Beide regelen de boekhoudkundige verwerking van een nieuwe groepsentiteit
    - **Verschillen**:
        - Eerste consolidatie: de allereerste opname van een entiteit in de kring (acquisitie + initial PPA)
        - Wijziging kring: omvat ook alle latere mutaties — desinvesteringen, stap-acquisities, verlies van controle
