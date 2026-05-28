---
title: "Consolidatieverschil (goodwill / badwill)"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.4.I.D
  - 1.4.II.C
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/consolidatieverschil.json"
---

# Consolidatieverschil (goodwill / badwill)

_Kader_

🏛️ Kader · Anchors: `1.4.I.D` · `1.4.II.C` · Wave: `skeleton-cross-cutting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: consolidatieverschil-goodwill · goodwill · badwill — **Vertalingen**: fr: écart de consolidation / goodwill · en: goodwill / bargain purchase gain

## Definitie

📖 Het consolidatieverschil is het verschil dat ontstaat bij de eerste consolidatie tussen (1) de aanschaffingsprijs van de deelneming en (2) het aandeel van de moeder in het netto-eigen vermogen van de dochter op de overnamedatum, na herwaardering van de identificeerbare activa en verplichtingen tegen reële waarde. Een positief verschil (te veel betaald) heet 'goodwill'; een negatief verschil (koopje) heet 'badwill' of 'bargain purchase gain'. Goodwill verschijnt als immaterieel actief op de geconsolideerde balans; badwill wordt onder IFRS direct in resultaat genomen.

<small>📚 KB-WVV — art. 3:130 — _wettekst_ · KB-WVV — art. 3:131 — _wettekst_ · IFRS 3 — Bedrijfscombinaties — §32-34 — _norm_</small>

## Substantie

🔗 Goodwill is het 'onverklaarde surplus' in de koopprijs: niet toewijsbaar aan identificeerbare activa (gebouw, machine, klantenbestand). Economisch staat het voor: synergieën die de koper verwacht, marktpositie van de dochter, kwaliteit van het personeel, merknaam — items die je niet apart op een balans kan zetten. Badwill is omgekeerd: de koper betaalt minder dan de gewaardeerde netto-activa, vaak omdat de verkoper haast had of het bedrijf in moeilijkheden is. De wet behandelt badwill voorzichtig: vóór erkenning eerst nogmaals nakijken of de fair-value-meting van activa en passiva correct is.

<small>📚 IFRS 3 — §32-36 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Het consolidatieverschil is geen 'kunstgreep' maar volgt uit het principe dat de geconsolideerde balans het werkelijke geheel weergeeft. Als de moeder 1500 betaalt voor een dochter met netto-activa van 1200, moet die 300 ergens terug te vinden zijn in de geconsolideerde cijfers — anders verdwijnt geld uit het 'kader' van de groep. Goodwill is de balanspost die deze 300 zichtbaar maakt. De impairment-test (IAS 36) of afschrijving (B-GAAP art. 3:131 KB-WVV) zorgt ervoor dat de goodwill realistisch blijft: als de overnemende verwachting niet uitkomt, moet de boekwaarde dalen.

<small>📚 KB-WVV — art. 3:105 — _wettekst_ · IAS 36 — §80-99 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: KB-WVV art. 3:130-3:131 (B-GAAP) + IFRS 3 + IAS 36 (IFRS, via EU-endorsement Verordening (EU) 2023/1803)

**✅ Voor**
- 📖 Elke groep die een dochter integraal of evenredig consolideert (KB-WVV art. 3:130 e.v.) of die een geassocieerde onderneming volgens vermogensmutatie verwerkt (art. 3:142 § 3 KB-WVV). Goodwill ontstaat ook bij IFRS-bedrijfscombinaties (IFRS 3).

**⚠️ Risico**
- 🔗 Bij IFRS-impairment kan een grote goodwill-impairment het geconsolideerd resultaat in één boekjaar zwaar drukken. Markten reageren sterk op goodwill-impairments — vandaar de behoefte aan vroege signalering en degelijke documentatie van de impairment-test.

## Sub-concepten

### 📦 Berekening eerste consolidatieverschil  
_`procedure` (subconcept)_

#### Definitie

📖 Formule: consolidatieverschil = aanschaffingsprijs deelneming − aandeel moeder in herwaardeerd netto-eigen vermogen van dochter op overnamedatum.

<small>📚 KB-WVV — art. 3:130 — _wettekst_ · IFRS 3 — §32 — _norm_</small>

**Weergave** `formule_expressie`:

```json
{
  "tekst": "Consolidatieverschil = Koopprijs − ( % belang × Fair-value-NA dochter )\n\nwaarbij Fair-value-NA = som van geherwaardeerde identificeerbare activa − geherwaardeerde passiva (incl. voorwaardelijke verplichtingen)"
}
```

#### 👣 Stap 1 — fair value van identificeerbare activa en verplichtingen  
_`stap`_

📖 Op de overnamedatum worden alle identificeerbare activa en verplichtingen van de dochter geherwaardeerd tegen reële waarde — niet tegen boekwaarde. Dit kan immateriële activa onthullen die niet op de individuele balans van de dochter staan (bv. klantenrelaties, merken).

<small>📚 IFRS 3 — §10-17 — _norm_ · KB-WVV — art. 3:130, eerste lid — _wettekst_</small>

#### 👣 Stap 2 — toewijzing van het verschil  
_`stap`_

📖 Bij integrale of evenredige consolidatie wordt het eerste verschil 'zoveel mogelijk' toegewezen aan de identificeerbare activa en passiva (art. 3:130 KB-WVV). Het residu is goodwill (positief) of badwill (negatief). Bij vermogensmutatie wordt het verschil 'voor zover mogelijk' toegewezen (art. 3:142 § 3 KB-WVV) — minder strikt.

<small>📚 KB-WVV — art. 3:130 — _wettekst_ · KB-WVV — art. 3:142 § 3 — _wettekst_</small>

### 📦 Behandeling goodwill: B-GAAP vs IFRS  
_`kader` (subconcept)_

#### Definitie

📖 B-GAAP (art. 3:131 KB-WVV): positieve goodwill wordt afgeschreven over de gebruiksduur (max 10 jaar tenzij economisch verantwoorde langere duur, in toelichting). Onder IFRS 3 + IAS 36 wordt goodwill NIET afgeschreven maar jaarlijks getoetst op impairment.

<small>📚 KB-WVV — art. 3:131 — _wettekst_ · IFRS 3 — §B63 — _norm_ · IAS 36 — §10, §80-99 — _norm_</small>

**Weergave** `vergelijkingstabel`:

```json
{
  "tekst": "| Aspect | B-GAAP (KB-WVV art. 3:131) | IFRS (IFRS 3 + IAS 36) |\n|---|---|---|\n| Goodwill na eerste opname | Afschrijving over gebruiksduur | Geen afschrijving |\n| Toets impairment | Wanneer indicatoren wijzen op duurzame waardevermindering | Jaarlijks verplicht + bij indicatoren |\n| Niveau impairment | Per dochteronderneming (of CGU) | Per cash-generating unit (CGU) |\n| Badwill | Direct in resultaat (uitzonderlijke baat) | Bargain purchase gain — direct in resultaat na hertoetsing |\n| Wijziging boekwaarde | Lineaire afschrijving voorspelbaar | Schoksgewijs door impairment |"
}
```

### 📦 Impairment-test goodwill (IAS 36)  
_`procedure` (subconcept)_

#### Definitie

📖 Onder IFRS wordt goodwill bij eerste opname toegerekend aan een cash-generating unit (CGU) — de kleinste groep activa die onafhankelijke kasstromen genereert. Jaarlijks (en bij indicatoren) wordt de recoverable amount van de CGU vergeleken met haar boekwaarde inclusief goodwill. Bij tekort: verlies erkennen, eerst op goodwill, dan pro-rata op andere activa van de CGU.

<small>📚 IAS 36 — §66, §80-99, §104 — _norm_</small>

## Voorbeelden

### 💡 Aurelia koopt Zelena Bio — positieve goodwill 🔗

_Aurelia Holding NV verwerft 100 % van Zelena Bio NV voor 1.500.000 EUR. Op overnamedatum bedraagt het netto-eigen vermogen van Zelena (na herwaardering van activa naar fair value) 1.200.000 EUR._

**Berekening:**
- Stap 1 — bepaal aandeel in fair-value-NA: 100 % × 1.200.000 = 1.200.000 EUR.
- Stap 2 — consolidatieverschil: 1.500.000 − 1.200.000 = 300.000 EUR (positief = goodwill).
- Stap 3 — toewijzing aan identificeerbare activa: niet meer mogelijk (alle activa al op fair value).
- Stap 4a (B-GAAP) — boek 300.000 EUR als 'goodwill' onder klasse 21 immateriële vaste activa; afschrijving 30.000 EUR/jaar over 10 jaar.
- Stap 4b (IFRS) — boek 300.000 EUR als 'goodwill'; toewijzen aan CGU 'biotech-divisie'; jaarlijkse impairment-test.

→ **Resultaat**: Geconsolideerde balans toont 300.000 EUR goodwill op activa. Onder B-GAAP daalt deze elk jaar met 30.000 EUR; onder IFRS blijft 300.000 EUR staan tenzij impairment vereist.

**Boeking:**


<small>📚 KB-WVV — art. 3:130-3:131 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 💡 Reorganisatie-overname met badwill 🔗

_Aurelia koopt 100 % van een dochter in moeilijkheden voor 800.000 EUR. Fair-value-NA van de dochter bedraagt 1.100.000 EUR (verkoper had haast)._

**Berekening:**
- Stap 1 — verschil: 800.000 − 1.100.000 = −300.000 EUR (negatief = badwill).
- Stap 2 — eerst hertoetsen: zijn alle activa correct gewaardeerd? Verplichtingen volledig? Pensioenverplichtingen niet vergeten? Indien hertoetsing badwill niet wegneemt:
- Stap 3 (IFRS) — 300.000 EUR opnemen als 'bargain purchase gain' direct in winst-en-verliesrekening van het overnamejaar.
- Stap 3 (B-GAAP) — KB-WVV art. 3:131 voorziet dat een negatief verschil dat een goed gefundeerd vooruitzicht op een ongunstig resultaat van de dochter weerspiegelt, in resultaat genomen wordt naargelang dit ongunstige resultaat zich realiseert; andere badwill direct in resultaat.

→ **Resultaat**: Badwill = uitzonderlijke winst van 300.000 EUR in jaar van overname. Vereist motivering in toelichting waarom de verkoper akkoord ging met een verlies-deal.

<small>📚 IFRS 3 — §32-36 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Boekwaarde gebruiken in plaats van fair value

**Verkeerde assumptie**: Het consolidatieverschil = koopprijs − boekwaarde-eigen-vermogen van de dochter.

**Kernpunt**: De vergelijking gebeurt met het fair-value-eigen-vermogen na herwaardering van activa en passiva. Eerst alle activa en passiva op fair value, eventueel nieuwe immateriële activa identificeren (klantenrelaties, merken) en dan het residu als goodwill boeken.

<small>📚 KB-WVV — art. 3:130, eerste lid — _wettekst_ · IFRS 3 — §10-18 — _norm_</small>

### ⚠️ Goodwill afschrijven onder IFRS

**Verkeerde assumptie**: Goodwill wordt jaarlijks afgeschreven over een nuttige levensduur, zoals andere immateriële activa.

**Kernpunt**: IFRS schrijft goodwill NIET af (IFRS 3 §B63). Enkel impairment-test. B-GAAP doet wel afschrijven (art. 3:131 KB-WVV) — dit is een fundamenteel verschil tussen de twee referentiestelsels.

<small>📚 IFRS 3 — §B63 — _norm_ · KB-WVV — art. 3:131 — _wettekst_</small>

### ⚠️ Badwill direct als winst boeken zonder hertoetsing

**Verkeerde assumptie**: Negatief consolidatieverschil = mooie uitzonderlijke winst, boek meteen.

**Kernpunt**: Bij badwill schrijft IFRS 3 §36 voor om eerst de identificatie en waardering van activa, verplichtingen en aanschaffingsprijs te hertoetsen. Pas als badwill na hertoetsing standhoudt, wordt deze als bargain purchase gain in resultaat erkend. Een 'goedkope overname' is zeldzaam en vereist documentatie.

<small>📚 IFRS 3 — §36 — _norm_</small>

## Accountant-perspectieven

### Groep na overname

_Accountant die de eerste consolidatie en de jaarlijkse opvolging van goodwill verzorgt._

#### 📒 Boekhouder

##### 👣 Boeking eerste consolidatieverschil  
_`stap`_

🔗 Op overnamedatum: (1) fair-value-waardering door externe expert documenteren; (2) identificeerbare immateriële activa identificeren (klantenlijsten, merken, technologie); (3) consolidatieverschil berekenen; (4) bij positief verschil: goodwill onder rubriek 21 Immateriële vaste activa (in toelichting: gebruiksduur en methode bij B-GAAP; CGU-allocatie bij IFRS); (5) afschrijvingsplan opstellen of impairment-monitoring opzetten.

<small>📚 KB-WVV — art. 3:130-3:131 — _wettekst_ · IFRS 3 — §B64-B67 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 Audit van impairment-test goodwill  
_`stap`_

🔗 De commissaris controleert: (1) is goodwill correct toegerekend aan CGU's? (2) zijn de impairment-assumpties (groeivoet, disconteringsvoet, kasstroomprognose) verdedigbaar in licht van marktomstandigheden? (3) wordt de test jaarlijks uitgevoerd of enkel bij triggers? (4) bij impairment-verlies: is verdeling correct (eerst goodwill, dan pro-rata)? Goodwill is een hoog-risico-area in groepsaudits vanwege subjectiviteit van kasstroom-assumpties.

<small>📚 IAS 36 — §80-104 — _norm_ · ISA 540 — Auditing Accounting Estimates — §A45-A60 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Eerste consolidatie (ontstaans-moment) → [[eerste-consolidatie]] _(moet-verwijzen)_
- → Minderheidsbelangen (full-goodwill vs partial-goodwill) → [[minderheidsbelangen]] _(moet-verwijzen)_
- ↪ IFRS-IAS 36 impairment context → [[ifrs]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[geconsolideerde-jaarrekening]]
### `beinvloed_door`
- [[eerste-consolidatie]] — Het consolidatieverschil ontstaat bij de eerste consolidatie van een dochter.
### `vergelijkbaar_met`
- [[ifrs]]
    - **Gelijkenissen**:
        - Beide kennen het concept consolidatieverschil bij bedrijfscombinaties
        - Beide vereisen toewijzing aan identificeerbare activa vóór goodwill-erkenning
    - **Verschillen**:
        - B-GAAP: afschrijving over max 10 jaar (art. 3:131 KB-WVV)
        - IFRS: geen afschrijving, wel jaarlijkse impairment-test (IAS 36)
        - Badwill: IFRS vereist hertoetsing vóór erkenning (§36); B-GAAP heeft een specifieke regel voor 'verwachte verliezen'-badwill
    - ⚠️ **Verwarringsrisico**: Studenten halen B-GAAP-afschrijving en IFRS-impairment door elkaar — fundamenteel verschillende benadering van goodwill na eerste opname.
