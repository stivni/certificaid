---
title: "Uniforme waarderingsregels bij consolidatie"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 1.4.I.D
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/uniforme-waarderingsregels-consolidatie.json"
---

# Uniforme waarderingsregels bij consolidatie

_Regime_

📋 Regeling · Anchors: `1.4.I.D` · Wave: `skeleton-consolidatie-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: uniforme groepswaarderingsregels · consistent accounting policies

## Definitie

📖 Het beginsel van uniforme waarderingsregels (art. 3:117 KB WVV; vroeger art. 145 KB van 30 januari 2001) houdt in dat alle vennootschappen in de consolidatiekring hun activa, passiva, opbrengsten en kosten op een uniforme wijze moeten waarderen vóór ze worden samengevoegd in de geconsolideerde jaarrekening. Wanneer een dochteronderneming in haar statutaire jaarrekening andere waarderingsregels hanteert (bv. andere afschrijvingsmethode, andere voorraadwaardering, andere voorzieningenbeleid) dan de groepsregels, moeten pre-consolidatie-aanpassingen die verschillen wegwerken. Doel: vergelijkbaarheid en getrouw beeld van de groep.

<small>📚 KB WVV — art. 3:117 — _kb_</small>

## Substantie

🔗 Concreet werken: de moedervennootschap stelt een set van groepswaarderingsregels op (typisch onderdeel van het rapporteringspakket en de groeps-accounting-manual). Dochters voeren hun lokale boekhouding volgens hun statutaire/lokale GAAP (Belgian GAAP, USGAAP, lokale GAAP in BU's), maar leveren voor consolidatie-doeleinden cijfers die geherwaardeerd zijn naar groepsregels. Voorbeelden: een dochter met afschrijvingen op gebouwen over 25 jaar terwijl groep 33 jaar hanteert → pre-consolidatie-aanpassing van afschrijvingskosten + cumulatieve afschrijvingen. Een dochter met LIFO-voorraadwaardering in een land waar dat mag, terwijl groep FIFO/gemiddelde kost gebruikt → herwaardering voorraad + impact op COGS. Verschillen in voorzieningen (pensioenen, garanties) idem.

<small>📚 KB WVV — art. 3:117 — _kb_ · ISA 600 — Bijlage 2 — _norm_ · CBN-advies — 2022/09 — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Zonder uniforme regels heeft de geconsolideerde jaarrekening geen samenhang: een groep waarvan de Belgische dochter winst toont door agressieve voorraadwaardering en de Franse dochter verlies door conservatieve voorzieningen, geeft geen getrouw beeld van de groepsprestaties. Het beginsel van getrouw beeld (art. 3:1 KB WVV) en vergelijkbaarheid over entiteiten heen vereist één set waarderingsregels op groepsniveau. Het is een direct gevolg van het 'one-entity-view': de groep wordt behandeld als één economische eenheid, dus één boekhoudkundig referentiestelsel.

<small>📚 KB WVV — art. 3:117 — _kb_ · KB WVV — art. 3:1 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: KB 29-04-2019 ter uitvoering WVV, art. 3:117

Hercodificatie van het oude art. 145 KB 30-01-2001 zonder inhoudelijke wijziging. Voor IFRS-groepen: IFRS 10 alinea B86 + IFRS 10 alinea 19 — 'Uniform accounting policies'.

**✅ Voor**
- 📖 Toepasselijk op alle entiteiten in de consolidatiekring: dochterondernemingen (integraal), gezamenlijke dochters (evenredig), geassocieerde ondernemingen (VMM — alinea 35 IAS 28 voor IFRS).

**📋 Voorwaarden**
- 🔗 Pre-consolidatie-aanpassingen moeten gedocumenteerd worden in een apart 'consolidatieboek' (niet in de statutaire boekhouding van de dochter). Elke aanpassing krijgt een journaal-entry met source-document, kwantitatieve impact, en motivatie. Permanente bewaring (minimum tot 5 jaar na boekjaar — Belgische boekhoudbewaarplicht).

**⛔ Uitsluitingen**
- 📖 Vrijstelling toegelaten wanneer een dochter andere waarderingsregels hanteert die door de bijzondere aard van haar activiteit zijn gerechtvaardigd (art. 3:117 §2 KB WVV) — bv. een bank-dochter met IFRS 9-financiële-instrumenten-waardering in een verder industriële groep. Vermelding in toelichting verplicht.

## Bouwstenen

### 💡 Typische verschillen die uniformisering vragen  
_`begrip`_

🔗 Top-vijf categorieën waar dochter-statutair en groeps-regels typisch afwijken: (1) Afschrijvingen — economisch leven en methode (lineair vs degressief); (2) Voorraadwaardering — LIFO/FIFO/gewogen gemiddelde; (3) Voorzieningen — pensioen-verplichtingen (DBO-methode of forfait); (4) Financiële instrumenten — kostprijs vs fair value (IFRS 9 vs lokaal); (5) Subsidies — opname-tijdstip (cash vs prestatie-gebaseerd) + classificatie (resultaat vs EV).

<small>📚 KB WVV — art. 3:117 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 👣 Pre-consolidatie-aanpassing — methodiek  
_`stap`_

🔗 Stappen per identifiseerd verschil: (1) Kwantificeer impact op opening balans (cumulatief verschil sinds verkrijgingsdatum + tot huidig boekjaar); (2) Boek opening-correctie in consolidatieboek tegen 'aanpassingen openingsreserves' (EV); (3) Boek periode-correctie voor het lopende jaar tegen relevante P&L-rekeningen; (4) Bereken belastingeffect (uitgestelde belastingen op het verschil); (5) Documenteer in toelichting van geconsolideerde jaarrekening (transparency).

<small>📚 KB WVV — art. 3:117 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ↪️ Vrijstelling bij onbeduidende verschillen  
_`uitzondering`_

🔗 Wanneer een verschil tussen lokale en groeps-waarderingsregels onbeduidend is (verwaarloosbare impact op groepsbalans en -resultaat), mag de aanpassing achterwege blijven om praktische redenen — toepassing van het materialiteitsbeginsel. Beoordeling per dochter én cumulatief over alle dochters. Auditor reviewt deze cost-benefit-afweging.

<small>📚 KB WVV — art. 3:117 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Aanpassing afschrijvingen — dochter 25 jaar, groep 33 jaar 🔗

_Dochter D heeft een gebouw aanschaffingswaarde 3.300 EUR. Statutair afgeschreven over 25 jaar (132 EUR/jaar). Groep schrijft over 33 jaar af (100 EUR/jaar). Eindstand jaar 5: cumulatief verschil = 5 × (132 - 100) = 160 EUR teveel afgeschreven._

**Boeking:**


<small>📚 KB WVV — art. 3:117 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Aanpassing alleen op P&L, niet op balans

**Verkeerde assumptie**: Het corrigeren van het lopend jaar volstaat.

**Kernpunt**: Verschillen accumuleren over jaren. Bij eerste implementatie of bij verkrijging dochter: bereken cumulatief verschil sinds verkrijgingsdatum en boek het deel van vorige jaren als correctie van openingsreserves (EV). Anders zit een 'gat' in de openings-balansvergelijking.

<small>📚 KB WVV — art. 3:117 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Belastingimpact vergeten

**Verkeerde assumptie**: Een pre-consolidatie-aanpassing is een 'consolidatie-only'-effect dus geen fiscale impact.

**Kernpunt**: De aanpassing creëert een tijdelijk verschil tussen boekhoudkundige en fiscale waarde (de fiscale waarde blijft die van de statutaire boekhouding). → uitgestelde belastingen boeken (active of passieve, IAS 12 / KB WVV art. 3:91).

<small>📚 KB WVV — art. 3:91 — _kb_ · Verordening (EU) 2023/1803 — IAS 12 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Verschillen tussen IFRS-dochter en BE-GAAP-groep niet harmoniseren

**Verkeerde assumptie**: Een dochter rapporteert IFRS, groep rapporteert BE-GAAP → IFRS is 'superieur' dus geen aanpassing nodig.

**Kernpunt**: De groeps-referentie is bepalend. Voor een BE-GAAP-consolidatie moet ook de IFRS-rapporterende dochter herwaardeerd worden naar BE-GAAP-regels — anders geen consistente groepscijfers. Omgekeerd voor IFRS-groep met BE-GAAP-dochter.

<small>📚 KB WVV — art. 3:117 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Groepsmoeder — consolidatieverantwoordelijke

_De accountant die verantwoordelijk is voor de uniformiseringsstap._

#### 📒 Boekhouder

##### 👣 Opstellen + verspreiden groeps-accounting-manual  
_`stap`_

🔗 De moedervennootschap stelt een groeps-accounting-manual op met (1) groeps-waarderingsregels per balansrubriek + RR-categorie; (2) groeps-rekeningenstelsel met mapping naar IFRS- of BE-GAAP-rubrieken; (3) materiale-drempels voor verplichte versus optionele aanpassingen; (4) confirmatie-vereisten dochters. Actualisatie minstens jaarlijks (impact van nieuwe IFRS, fiscale wijzigingen).

<small>📚 KB WVV — art. 3:117 — _kb_ · ISA 600 — Bijlage 2 — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 Audit uniformiteit waarderingsregels  
_`stap`_

🔗 Audit-werkzaamheden: (1) bestaan + actualiteit groeps-accounting-manual; (2) per significante dochter: review pre-consolidatie-aanpassingen op materiele verschillen; (3) belastingimpact van aanpassingen (uitgestelde belastingen); (4) bij joint ventures + associates verwerkt via VMM: ook hier moeten lokale GAAP-cijfers naar groeps-regels herwaardeerd worden vóór VMM-toepassing (IAS 28 alinea 35); (5) toelichting in geconsolideerde jaarrekening (vrijstellingsgevallen!).

<small>📚 KB WVV — art. 3:117 — _kb_ · Verordening (EU) 2023/1803 — IAS 28 alinea 35 — _wettekst_ · ISA 600 — Bijlage 2 — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Waarderingsregels jaarrekening (statutair) → [[jaarrekening]] _(moet-verwijzen)_
- → Opmaak-procedure (input-stap) → [[opmaak-geconsolideerde-jaarrekening]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[geconsolideerde-jaarrekening]]
### `vereist`
- [[opmaak-geconsolideerde-jaarrekening]] — Input-stap binnen het opmaak-proces — gebeurt vóór samenvoegen + eliminaties.
### `vergelijkbaar_met`
- [[omrekening-buitenlandse-dochter]]
    - **Gelijkenissen**:
        - Beide zijn pre-consolidatie-aanpassingen op de dochter-cijfers
        - Beide gebeuren in het consolidatieboek (niet in de statutaire dochterboekhouding)
    - **Verschillen**:
        - Uniforme waarderingsregels: kwalitatieve harmonisering (afschrijvingsmethode, voorraadwaardering, voorzieningen)
        - Omrekening: kwantitatieve conversie tussen valuta
        - Beide kunnen samen voorkomen bij dezelfde dochter (bv. UK-dochter met afwijkende afschrijvingen + GBP-omrekening)
