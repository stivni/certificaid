---
title: "Gespreide belasting van meerwaarden"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.3.II.F
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/gespreide-belasting-meerwaarden.json"
---

# Gespreide belasting van meerwaarden

_Regime_

📋 Regeling · Anchors: `2.3.II.F` · Wave: `fiscale-voordelen-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: herinvesteringsregime art. 47 · spreidingsregime meerwaarden

## Definitie

📖 De gespreide belasting van meerwaarden (art. 47 WIB92) laat een vennootschap toe om de belasting op een gerealiseerde meerwaarde op materiële of immateriële vaste activa niet ineens te betalen, maar te spreiden over de afschrijvingsperiode van een herinvestering. Voorwaarde: het ontvangen bedrag (verkoopprijs of schadevergoeding) wordt binnen de wettelijke termijn herbelegd in een afschrijfbaar activum in een EER-land dat voor de beroepswerkzaamheid wordt gebruikt. De meerwaarde wordt dan progressief belast naarmate het herbeleggingsactivum wordt afgeschreven.

<small>📚 WIB92 — art. 47 §1 — _wettekst_</small>

## Substantie

🔗 Praktisch effect: een vennootschap die bv. een gebouw verkoopt met grote meerwaarde, hoeft die niet ineens in het belastbaar resultaat op te nemen. Door binnen 5 jaar (onroerend goed) of 3 jaar (roerend) opnieuw te investeren in een afschrijfbaar bedrijfsactivum, wordt de meerwaarde gespreid belast — telkens een evenredig deel pro rata van de afschrijving van het herbeleggingsactivum. Dit verzacht de cash-flow-schok van een grote eenmalige meerwaarde en stimuleert herinvestering in de bedrijfsactiviteit i.p.v. uitkering.

<small>📚 WIB92 — art. 47 §4 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Ratio legis: meerwaarden op vaste activa kunnen aanzienlijk zijn (bv. een bedrijfspand dat 20 jaar geleden gekocht werd). Ineens-belasten zou de vennootschap dwingen tot uitkering of dwingen om de meerwaarde-cash te gebruiken voor belastingbetaling i.p.v. herinvestering. Het spreidingsregime is een fiscaal investeringsstimulus: de fiscus geeft uitstel (geen vrijstelling — de belasting komt er, alleen gespreid) op voorwaarde dat het kapitaal in de Belgische/EER-economie blijft.

<small>📚 WIB92 — art. 47 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 47

Stabiel regime sinds invoering WIB92. Geen recente afschaffing aangekondigd.

**✅ Voor**
- 📖 Vennootschap (of eenmanszaak met beroepsinkomen) die een meerwaarde realiseert op materiële of immateriële vaste activa die sinds meer dan 5 jaar in het bedrijf gebruikt werden (gedwongen meerwaarden zoals onteigening of vernieling met verzekeringsuitkering hebben geen 5-jaars-voorwaarde).

**📋 Voorwaarden**
- 📖 Cumulatief: (1) gerealiseerde meerwaarde op MVA/IVA in beroepswerkzaamheid; (2) activum sedert meer dan 5 jaar in gebruik (uitzondering bij gedwongen meerwaarde — onteigening, brand, ...); (3) volledige verkoopprijs (niet enkel meerwaarde) herbelegd binnen 3 jaar (roerend) of 5 jaar (onroerend) in een afschrijfbaar activum gebruikt voor het beroep in EER-land; (4) uitdrukkelijke keuze in aangifte; (5) onaantastbaarheidsvoorwaarde: de gespreide meerwaarde blijft als belastingvrije reserve geboekt tot ze pro rata belast wordt.

**👍 Voordeel**
- 🔗 Cash-flow-spreiding van een grote eenmalige belastingschuld over de afschrijvingsperiode van de herinvestering (typisch 5-20 jaar voor MVA). Combineerbaar met andere aftrekken op het lopende resultaat — de gespreide meerwaarde is een 'pro rata' belastbare component, geen aparte aanslag.

**⚠️ Risico**
- 📖 Bij niet-tijdige of onvolledige herinvestering wordt het saldo van de niet-belaste meerwaarde belast in het jaar waarin de termijn verstrijkt, vermeerderd met nalatigheidsinteresten vanaf het oorspronkelijke jaar van realisatie. Effectieve kost is dus hoger dan wanneer men de meerwaarde van bij aanvang gewoon zou belasten.

## Bouwstenen

### 📏 Herinvesteringstermijn  
_`drempel`_

📖 3 jaar voor herbelegging in roerende activa (gerekend vanaf de eerste dag van het belastbaar tijdperk waarin de meerwaarde gerealiseerd is). 5 jaar voor herbelegging in onroerende activa (en voor schepen). Voor gedwongen meerwaarden (onteigening, ramp): 5 jaar voor zowel roerend als onroerend. Termijn is fataal — verstrijken zonder volledige herbelegging triggert onmiddellijke belasting van het niet-herbelegde saldo.

<small>📚 WIB92 — art. 47 §3 — _wettekst_</small>

### 📜 Onaantastbaarheidsvoorwaarde  
_`regel`_

📖 De gespreide meerwaarde moet op een afzonderlijke onbeschikbare reserve worden geboekt (art. 190 WIB92). Zolang ze niet pro rata belast is, mag ze niet uitgekeerd worden als dividend of overgedragen worden naar een belastbare reserve. Bij schending: volledige meerwaarde wordt onmiddellijk belastbaar in het jaar van de schending, ongeacht of de herinvestering nog binnen termijn was.

<small>📚 WIB92 — art. 190 — _wettekst_</small>

### ⚙️ Pro rata belasting bij afschrijving herbeleggingsactivum  
_`mechanisme`_

📖 Het belastbare deel van de meerwaarde per jaar = meerwaarde × (afschrijving herbeleggingsactivum dat jaar / aanschaffingswaarde herbeleggingsactivum). Bv. meerwaarde 100.000 EUR, herbelegd in machine 500.000 EUR afgeschreven over 10 jaar (50.000/jaar): jaarlijks belastbaar deel = 100.000 × (50.000/500.000) = 10.000 EUR. Bij verkoop of buitengebruikstelling van het herbeleggingsactivum vóór einde: het resterende saldo wordt ineens belast.

<small>📚 WIB92 — art. 47 §4 — _wettekst_</small>

### 📜 Kwalificerende herinvestering  
_`regel`_

📖 Het herbeleggingsactivum moet: (a) afschrijfbaar zijn (geen grond, geen aandelen — die zijn niet afschrijfbaar); (b) gebruikt worden voor de beroepswerkzaamheid in een EER-lidstaat; (c) volledig herbelegd worden — de hele verkoopprijs (niet alleen de meerwaarde). Onvolledige herbelegging leidt pro rata tot belasting van het niet-herbelegde deel.

<small>📚 WIB92 — art. 47 §2 — _wettekst_</small>

## Voorbeelden

### 💡 Aurelia Holding NV — gespreide belasting bij verkoop bedrijfsgebouw 🔗

_Aurelia Holding verkoopt in jaar N haar oude productiegebouw (boekwaarde 200.000 EUR, verkoopprijs 800.000 EUR — meerwaarde 600.000 EUR). Het gebouw was sinds 15 jaar in gebruik. In jaar N+2 herbelegt Aurelia het volledige bedrag van 800.000 EUR in een nieuw productiegebouw (afschrijving lineair 5 % over 20 jaar = 40.000 EUR/jaar)._

**Berekening:**
- Stap 1 — meerwaarde 600.000 EUR; herinvesteringstermijn voor onroerend = 5 jaar; volledige verkoopprijs (800.000 EUR) volledig herbelegd in jaar N+2 → voorwaarden vervuld.
- Stap 2 — pro rata-belasting: jaarlijks belastbaar deel = 600.000 × (40.000 / 800.000) = 30.000 EUR per jaar gedurende 20 jaar.
- Stap 3 — in plaats van 600.000 EUR ineens belastbaar in jaar N, wordt 30.000 EUR/jaar belastbaar van N+2 tot N+21.
- Stap 4 — boekhouding: 600.000 EUR als belastingvrije reserve geboekt; jaarlijks 30.000 EUR overboeking naar belastbare reserve (= belastbaar in dat jaar).
- Stap 5 — bij verkoop herbeleggingsactivum in jaar N+10: nog niet-belast saldo = 600.000 − 8 × 30.000 = 360.000 EUR ineens belastbaar in N+10.

→ **Resultaat**: Cash-flow-voordeel: belastingschuld op 600.000 EUR meerwaarde wordt 20 jaar gespreid — bij 25 % tarief: 150.000 EUR fiscale schuld gespreid over 20 jaar i.p.v. ineens in jaar N.

<small>📚 WIB92 — art. 47 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Enkel meerwaarde herbeleggen i.p.v. volledige verkoopprijs

**Verkeerde assumptie**: Studenten denken dat alleen het meerwaarde-bedrag binnen de termijn herbelegd moet worden.

**Kernpunt**: Art. 47 §2 vereist herbelegging van de VOLLEDIGE verkoopprijs (boekwaarde + meerwaarde), niet alleen de meerwaarde. Onvolledige herbelegging triggert pro rata belasting van het niet-herbelegde deel.

<small>📚 WIB92 — art. 47 §2 — _wettekst_</small>

### ⚠️ Gespreid regime kiezen waar 'meerwaarde-aandelen' van toepassing is

**Verkeerde assumptie**: Op meerwaarden op aandelen art. 47 toepassen.

**Kernpunt**: Aandelen zijn niet afschrijfbaar en vallen niet onder art. 47. Voor meerwaarden op aandelen geldt art. 192 WIB92 (mogelijke 0 %-vrijstelling indien DBI-voorwaarden vervuld). Andere systematiek, andere voorwaarden.

<small>📚 WIB92 — art. 47 — _wettekst_ · WIB92 — art. 192 — _wettekst_</small>

### ⚠️ 5-jaar-gebruiks-voorwaarde vergeten

**Verkeerde assumptie**: Elke meerwaarde op MVA komt in aanmerking voor gespreide belasting.

**Kernpunt**: Het verkochte activum moet sinds MEER DAN 5 JAAR in beroepswerkzaamheid gebruikt zijn (uitzondering: gedwongen meerwaarden). Verkoop van recent gekochte activa kan niet gespreid belast worden — die meerwaarde wordt onmiddellijk belast.

<small>📚 WIB92 — art. 47 §1 — _wettekst_</small>

## Accountant-perspectieven

### Vennootschap-verkoper (cliënt)

_Accountant adviseert vennootschap die een MVA met meerwaarde gaat verkopen._

#### 💰 Fiscaal adviseur

##### 👣 Keuze in aangifte registreren  
_`stap`_

📖 De keuze voor gespreide belasting is een aangifte-keuze: vinkje in de aangifte VenB + boeking van de meerwaarde als belastingvrije onbeschikbare reserve (rekening 132 'Onbeschikbare reserve'). Zonder expliciete keuze: meerwaarde direct belastbaar in jaar van realisatie. De keuze is definitief — geen retroactieve wijziging mogelijk.

<small>📚 WIB92 — art. 47 §1 — _wettekst_ · WIB92 — art. 190 — _wettekst_</small>

##### 👣 Monitoring herinvesteringstermijn  
_`stap`_

🔗 Vanaf realisatie meerwaarde: termijn van 3 jaar (roerend) of 5 jaar (onroerend) bewaken. Bij naderend einde: herinneren aan cliënt + concrete investerings-plannen valideren. Bij niet-tijdig: in aangifte van het jaar waarin termijn verstrijkt, het niet-herbelegde saldo opnemen als belastbaar + nalatigheidsinteresten voorzien.

<small>📚 WIB92 — art. 47 §6 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 👣 Boeking belastingvrije reserve  
_`stap`_

🔗 Bij realisatie meerwaarde: meerwaarde-bedrag boeken op rekening 132 'Onbeschikbare reserve — belastingvrije reserve' via winstverdeling. Jaarlijks bij afschrijving herbeleggingsactivum: pro rata-deel overboeken van 132 naar 133 'Beschikbare reserves' (of direct via resultaatverdeling) — dat deel is dan belastbaar in het lopende jaar.

<small>📚 WIB92 — art. 190 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- ↪ Σ-keuzekader VenB-voordelen → [[fiscale-voordelen-vennootschap]] _(mag-verwijzen)_
- ↪ Meerwaarde-aandelen-venb (specifieker regime) → [[meerwaarde-aandelen-venb]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscale-voordelen-vennootschap]]
### `vereist`
- [[meerwaarde-mva]] — Veronderstelt een gerealiseerde meerwaarde op materiële of immateriële vaste activa.
### `triggert`
- [[aangifte-vennootschapsbelasting]] — Keuze gespreide belasting wordt in de aangifte uitgedrukt.
