---
title: "Handelsvorderingen"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.1.II.F
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/handelsvorderingen.json"
---

# Handelsvorderingen

_Balanspost_

🏢 Entiteit · Anchors: `1.1.II.F` · Wave: `cluster-extract-balansposten-activa-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: klantenvorderingen · trade receivables — **Vertalingen**: en: trade receivables · fr: créances commerciales

## Definitie

📖 Handelsvorderingen zijn de openstaande bedragen die klanten verschuldigd zijn aan de onderneming voor geleverde goederen of diensten in het kader van de gewone bedrijfsuitoefening, vervaldatum ≤ 1 jaar. MAR-klasse 40-41: 400 klanten · 401 te innen wissels · 404 dubieuze debiteuren · 406 vooruitbetalingen · 408 ontvangen aanbetalingen op contracten · 409 geboekte waardeverminderingen (-). Een handelsvordering ontstaat bij factuur en verdwijnt bij betaling — daartussen circa 30-90 dagen krediettermijn typisch. Voor LT-deel (> 1 jaar) zie klasse 29.

<small>📚 MAR-KB 21.10.2018 — Bijlage 1 klasse 40-41 — _kb_</small>

## Substantie

📖 Handelsvorderingen zijn vaak de grootste vlottende-activa post (40-60% van actief bij dienstondernemingen). Drie boekhoudkundige aandachtspunten: (1) Waardering. Nominale waarde minus waardeverminderingen voor dubieuze klanten. Twee methodes (CBN 127/1): forfaitair (% op totaal, op basis van historische oninbaarheid) of individueel (per debiteur op basis van concrete risico-inschatting — verplicht voor materieel risico). (2) Wisselbrieven en cheques. Klasse 401 'te innen wissels' onderscheidt vorderingen vertegenwoordigd door een wisselbrief — kan vóór vervaldag worden gedisconteerd bij bank. (3) Definitief oninbaar. Bij faillissement debiteur, gehomologeerd reorganisatieplan, of verjaring: vordering uitboeken (642 minderwaarde) + btw recupereren via aanvullende aangifte (KB Btw nr. 4 art. 4).

<small>📚 CBN-advies 127/1 — Forfaitaire waardeverminderingen op vorderingen — _cbn_ · CBN-advies 2011/15 — Waardeverminderingen op handelsvorderingen — _cbn_</small>

## Rationale

🔗 De aparte rubrieken 400 (gezond) / 404 (dubieus) / 409 (waardevermindering) bestaan voor analytische redenen: ratio-analyse van DSO (days sales outstanding) gebruikt 400 alleen; provisie-percentage = 409 / (400 + 404) toont risico-profiel. Belangrijk voor liquiditeitsanalyse + audit. Het onderscheid forfaitair vs individueel waardevermindering komt uit het voorzichtigheidsbeginsel: bij groot aantal kleine vorderingen is individuele beoordeling onmogelijk — forfaitair is dan een pragmatische schatting.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Sub-concepten

### 📦 400 — Klanten (handelsdebiteuren)  
_`balanspost` (subconcept)_

#### Definitie

📖 Hoofdrubriek voor openstaande klantenfacturen. Boekingscyclus: bij factuur 400 D / 700 (omzet) C + 451 (btw) C → bij betaling 55 (bank) D / 400 C. Saldo 400 = nog niet geïnde verkopen.

<small>📚 MAR-KB — rubriek 400 — _kb_</small>

#### 💡 Factuur klant 5.000 EUR + btw, inning na 60 dagen 🔗

_Zelena Bio NV verkoopt aan Aurelia Holding NV._

**Boeking:**


**Boeking:**


<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 404 — Dubieuze debiteuren + 409 waardevermindering  
_`balanspost` (subconcept)_

#### Definitie

📖 Bij twijfel over inbaarheid (lange achterstand, financiële moeilijkheden debiteur, rappels zonder gevolg): vordering verschuiven van 400 naar 404 (zelfde bedrag — geen impact resultaat) + waardevermindering boeken van inschattings-deel op 6340 (waardevermindering kost) tegen 409 (correctierekening).

<small>📚 CBN-advies 2011/15 — Boeking waardevermindering — _cbn_</small>

#### 💡 Klant 1.000 EUR met 40% risico op oninbaarheid 🔗

_Klant 90 dagen achter, geen reactie op rappels._

**Boeking:**


**Boeking:**


<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Definitief oninbare vordering  
_`procedure` (subconcept)_

#### Definitie

📖 Bij faillissement debiteur, gehomologeerd reorganisatieplan dat schuld kwijtscheldt, of verjaring: vordering uitboeken. Boeking: 642 (minderwaarde handelsvorderingen) D + 409 D (terugneming waardevermindering) / 404 C. Fiscaal aftrekbaar als de vordering 'zeker en vaststaand verloren' is — art. 49 + 195 WIB92. Btw-terugvordering via creditnota of art. 77 § 1 6° KB nr. 1 + art. 4 KB Btw nr. 4 (insolvabiliteit).

<small>📚 WIB92 — art. 49 + 195 — _wettekst_ · CBN-advies 137/6 — Overdracht schuldvordering — _cbn_</small>

## Valkuilen

### ⚠️ Forfaitair vermijden bij materieel risico

**Verkeerde assumptie**: Forfaitair 5% op alle vorderingen volstaat altijd.

**Kernpunt**: CBN 127/1: forfaitair OK voor groot aantal kleine vorderingen met statistisch gelijkaardig risico. Voor materiële vorderingen (groot bedrag of duidelijk risico) MOET individueel beoordeeld worden. Dubieuze klant 50.000 EUR die geen reactie geeft: niet onder forfaitaire categorie laten — individueel evalueren.

<small>📚 CBN-advies 127/1 — Forfaitaire waardeverminderingen — _cbn_</small>

### ⚠️ Btw terugvorderen zonder formaliteit

**Verkeerde assumptie**: Bij dubieuze vordering kan de btw direct worden teruggevorderd.

**Kernpunt**: Btw-terugvordering vereist bewijs van definitieve oninbaarheid (faillissement, gehomologeerd reorganisatieplan). Loutere waardevermindering 409 is GEEN basis. Aanvullende aangifte met bewijsstukken. Bij gewone betalingsachterstand: alleen boekhoudkundige waardevermindering, btw blijft verschuldigd.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Geboekte waardevermindering = fiscaal aftrekbaar

**Verkeerde assumptie**: Elke boekhoudkundige waardevermindering is automatisch fiscaal aftrekbaar.

**Kernpunt**: Fiscaal vereist art. 22-27 KB/WIB92 (zie aangifte VenB-staat 204.3) bewijs van waarschijnlijke insolvabiliteit (rappels zonder gevolg, juridische actie, betalingsmoeilijkheden gedocumenteerd). Pure 'voorzichtigheid' zonder onderbouwing wordt verworpen — komt op verworpen uitgaven in aangifte.

<small>📚 WIB92 — art. 48 + KB/WIB92 art. 22-27 — _wettekst_</small>

## Accountant-perspectieven

### Onderneming zelf — handelsvorderingen-beheer

#### 📒 Boekhouder

##### 👣 Ouderdoms-staat (aging) per kwartaal  
_`stap`_

🔗 Per kwartaal: opstellen aging-staat = saldo per debiteur ingedeeld naar leeftijd (0-30 d / 30-60 d / 60-90 d / > 90 d). Item > 90 d = trigger voor verschuiving naar 404 + waardevermindering. Documenteer rappel-historiek per debiteur (boekhouder-DMS).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 Saldo-bevestiging (positief + negatief)  
_`stap`_

📖 ISA 505 saldo-bevestiging handelsvorderingen: stuur bevestigingsverzoek aan steekproef debiteuren rond balansdatum. Positieve bevestiging (debiteur moet bevestigen) voor materiële + risicovolle saldi; negatieve bevestiging (alleen reageren bij afwijking) voor klein bedrag homogene populatie. Volg-up alternatieve procedures bij niet-antwoord (toets latere betaling, bron-documenten).

<small>📚 ISA 505 — Externe bevestigingen — _norm_</small>

#### 💰 Fiscaal adviseur

##### 👣 VenB-staat 204.3 (waardeverminderingen handelsvorderingen)  
_`stap`_

📖 Bij VenB-aangifte (formulier 275.1) hoort staat 204.3 met opgave waardeverminderingen handelsvorderingen + onderbouwing per debiteur. Forfaitaire waardeverminderingen vereisen schadepercentage gebaseerd op historische data (3-5 jaar gemiddeld). Bij rappel-bewijs: aftrekbaar. Geen bewijs = verworpen uitgave (vak Z).

<small>📚 WIB92 — KB/WIB92 art. 22-27 — _wettekst_ · aangifte-VenB-2025-reserves — staat 204.3 — _aangifte_</small>

## Verder lezen (scope-out)

- → Eindejaarsverrichtingen (waardering + correcties) → [[eindejaarsverrichtingen]] _(moet-verwijzen)_
- → Jaarrekening (presentatie balans) → [[jaarrekening]] _(moet-verwijzen)_
- ↪ IFRS-perspectief → [[ifrs]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[balans]] — Vlottende activa — sub-rubriek 'Vorderingen ≤ 1 jaar'.
### `beinvloed_door`
- [[bedrijfsopbrengsten]] — Bij elke verkoopfactuur ontstaat een handelsvordering.
### `vergelijkbaar_met`
- [[vorderingen-op-meer-dan-een-jaar]]
    - **Gelijkenissen**:
        - Beide vorderingen op derden
    - **Verschillen**:
        - Klasse 40-41 ≤ 1 jaar; klasse 29 > 1 jaar
        - Disconteringsplicht bij LT (art. 3:45 KB)
### `triggert`
- [[eindejaarsverrichtingen]] — Waardeverminderings-toets bij jaarafsluit.
