---
title: "Activity-Based Costing (ABC)"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 1.8.III.F
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/activity-based-costing.json"
---

# Activity-Based Costing (ABC)

_Procedure_

📋 Regeling · Anchors: `1.8.III.F` · Wave: `cluster-extract-management-accounting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Afk.**: ABC — **Synoniemen**: activity-based-costing · abc-methode — **Vertalingen**: fr: comptabilité par activités

## Definitie

🔗 Activity-Based Costing (ABC) is een kostprijstoerekening-methode die indirecte (overhead-)kosten niet via één globale toerekeningssleutel maar via meerdere 'activiteiten' en bijbehorende cost-drivers verdeelt over de kostenobjecten. ABC herkent dat verschillende activiteiten (machine instellen, kwaliteitscontrole, klant-orderverwerking, productie zelf) verschillende verbruikspatronen hebben — en dus elk met een eigen driver moeten worden toegerekend. Het 4-stappen-model: (1) identificeer de activiteiten; (2) wijs kosten toe aan elke activiteit; (3) bepaal de cost-driver per activiteit; (4) reken activiteitskosten toe aan producten op basis van hun werkelijke verbruik van die activiteit.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Traditioneel wordt overhead verdeeld op basis van één toerekeningssleutel — vaak directe arbeidsuren of machine-uren. Maar bij modern productie-werk is overhead niet meer evenredig met arbeids- of machine-tijd: kleine batches van speciale producten vergen onevenredig veel set-up-tijd, kwaliteitscontrole en klantenondersteuning. ABC corrigeert dit door per activiteit te kijken naar de werkelijke driver. Gevolg: kleine batches van complexe producten krijgen hogere kostprijs (correcter), grote batches van eenvoudige producten lagere kostprijs (correcter). ABC ontmaskert vaak dat 'winstgevende' specialiteiten in werkelijkheid verliesmakend zijn, en dat 'magere' bulkproducten meer bijdragen dan gedacht.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De rationale is precision-pricing en winstgevendheids-inzicht in heterogene productie. Hoe heterogener de producten en hoe groter het aandeel van overhead in de totale kost, hoe groter het verschil tussen ABC en traditionele full costing. In sterk-geautomatiseerde productie waar machine-uren overal evenredig zijn, levert ABC weinig extra inzicht boven full costing met machine-uren-driver. Een Time-Driven ABC-variant (TDABC) vereenvoudigt het systeem: één driver per activiteit (tijd) in plaats van veel verschillende.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Heterogene productie met meerdere productlijnen + significant aandeel indirecte kosten (>30% van totale kost) + diverse batchsizes. Vooral nuttig in maakindustrie met setup-intensieve productie, ziekenhuizen (per ingreep), banken (per producttype), advocatenkantoren (per dossiertype).

**🚫 Niet voor**
- 🔗 Homogene productie met één productlijn — daar volstaat klassieke full costing met één driver. Ook ondernemingen met lage overhead-verhouding (<20% van totale kost) — de implementatie-kost van ABC weegt dan niet op tegen het marginale precisie-voordeel.

## Bouwstenen

### 👣 4-stappen-model  
_`stap`_

🔗 Stap 1 — Identificeer activiteiten: lijst alle waardetoevoegende én ondersteunende activiteiten op (typisch 20-50 in een mid-size productieonderneming). Voorbeelden: machine instellen, productie draaien, kwaliteitscontrole, orderverwerking, klantenservice, R&D. Stap 2 — Wijs kosten toe aan activiteiten: elke overhead-rekening (huur, afschrijving, indirect personeel) wordt op basis van enquêtes en time-studies toegewezen aan de activiteiten die ze ondersteunt. Resultaat: kostprijs per activiteit. Stap 3 — Identificeer drivers: voor elke activiteit een driver die de oorzakelijkheid weerspiegelt (aantal set-ups, aantal kwaliteitscontroles, aantal orderlines, aantal klantcontacten). Stap 4 — Reken activiteitskosten toe aan producten op basis van werkelijk verbruik: een specialiteits-product met veel set-ups krijgt veel set-up-kosten; een bulk-product met weinig set-ups krijgt weinig.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Types cost-drivers  
_`begrip`_

🔗 Drivers verschillen in granulariteit en accuratesse. (1) Transaction drivers: tellen voorvallen (aantal set-ups, aantal orders, aantal facturen) — eenvoudig maar veronderstelt dat elk voorval evenveel werk vergt. (2) Duration drivers: meten tijd per voorval (set-up-tijd in minuten, orderverwerkingstijd per orderline) — accurater maar duurder te meten. (3) Intensity drivers: kosten worden direct toegerekend per geval op basis van werkelijk verbruik — meest accuraat (kostbaar). Vuistregel: gebruik transaction drivers waar de activiteit homogeen is; duration drivers waar de tijd per voorval significant verschilt.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Time-Driven ABC (TDABC)  
_`begrip`_

🔗 Time-Driven Activity-Based Costing (Kaplan & Anderson 2004) vereenvoudigt klassiek ABC: in plaats van vele drivers wordt voor elke activiteit één gemiddelde tijd per voorval bepaald + één tarief per uur van praktische capaciteit. De kostprijs per voorval = (tijd × tarief). Voordeel: minder data-collectie, sneller updateerbaar bij wijziging. TDABC werkt met praktische capaciteit (typisch 80% van theoretische) — onbenutte capaciteit wordt expliciet als kost gerapporteerd, niet verstopt in het tarief.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Zelena Bio NV — traditioneel vs ABC bij twee productlijnen 🔗

_Zelena Bio maakt standaard-tafels (100 stuks/maand, 1 set-up) en luxe-tafels op maat (10 stuks/maand, 10 set-ups). Variabele kost per tafel: 250 EUR. Totale overhead maand: 20.000 EUR. Stel directe arbeidsuren: 100 u standaard, 50 u luxe — totaal 150 u._

**Weergave** `vergelijkingstabel`:

```json
{
  "kolommen": [
    "Aanpak",
    "Standaard-tafel",
    "Luxe-tafel",
    "Inzicht"
  ],
  "rijen": [
    [
      "Traditioneel (overhead/arbeidsuren = 20.000/150 = 133 EUR/u)",
      "250 + 1 u × 133 = 383 EUR",
      "250 + 5 u × 133 = 915 EUR",
      "Luxe lijkt 'duur' maar redelijk"
    ],
    [
      "ABC (set-up-pool 10.000 EUR; productie-pool 10.000 EUR — drivers: set-ups + arbeidsuren)",
      "250 + (10.000/11 × 1) + (10.000/150 × 1) = 250 + 909 + 67 = 1.226 EUR",
      "Wacht — bereken opnieuw",
      "Zie hieronder"
    ]
  ]
}
```

**Berekening:**
- Set-up-pool 10.000 EUR / totaal 11 set-ups = 909 EUR per set-up
- Productie-pool 10.000 EUR / 150 arbeidsuren = 67 EUR/u
- Standaard-tafels: per 100 stuks = 1 set-up × 909 + 100 u × 67 = 909 + 6.700 = 7.609 EUR overhead, dus per tafel ≈ 76 EUR overhead → kostprijs 250 + 76 = 326 EUR
- Luxe-tafels: per 10 stuks = 10 set-ups × 909 + 50 u × 67 = 9.090 + 3.350 = 12.440 EUR overhead, dus per tafel ≈ 1.244 EUR overhead → kostprijs 250 + 1.244 = 1.494 EUR

→ **Resultaat**: Traditioneel gaf luxe-tafel 915 EUR, ABC geeft 1.494 EUR. De luxe-tafel is veel duurder dan gedacht — vooral door set-up-kost. Indien verkocht aan 1.200 EUR was traditioneel zogenaamd winst, ABC toont verlies. Prijszetting moet bijgesteld of productlijn herzien worden.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ ABC implementeren zonder management-buy-in

**Verkeerde assumptie**: ABC is een boekhoudkundige verfijning die in de boekhouding kan plaatsvinden zonder de productie te betrekken.

**Kernpunt**: ABC vereist time-studies en interviews met productiepersoneel om kosten aan activiteiten toe te wijzen. Zonder hun medewerking blijven de drivers theoretisch en de cijfers betwist. Bovendien: als de directie niets doet met de ABC-inzichten (geen prijswijziging, geen portfolio-rationalisatie), verliest het systeem zijn waarde en sterft het uit.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Te veel activiteiten — verlamming

**Verkeerde assumptie**: Hoe meer activiteiten, hoe accurater het systeem.

**Kernpunt**: Boven 50 activiteiten wordt het systeem onbeheerbaar — meting wordt te duur en updates blijven achter. Vuistregel: start met 10-20 activiteiten die samen 80% van de overhead dekken; verfijn alleen waar significante volume of strategisch belang.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### ABC-implementatie bij heterogene productie-cliente

_Een productie-cliente met diverse productlijnen vraagt advies over winstgevendheid per product._

#### 🧭 Adviseur

##### 👣 Pilot eerst — niet meteen volledige uitrol  
_`stap`_

🔗 Voor de volledige ABC-implementatie eerst een pilot draaien op één productlijn of één afdeling. Zo wordt het systeem gevalideerd en kan de organisatie ervaren wat de inzichten zijn — en of die de extra kost rechtvaardigen. Pas na 6-12 maanden pilot uitrol naar de hele onderneming. Veel ondernemingen blijven in de praktijk bij een 'lichte ABC' op een paar productlijnen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Kostprijsmethoden Σ-keuze-kader → [[kostprijsmethoden]] _(moet-verwijzen)_
- ↪ Analytische boekhouding (parent) → [[analytische-boekhouding]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[kostprijsmethoden]]
### `vergelijkbaar_met`
- [[full-costing]]
    - **Gelijkenissen**:
        - Beide rekenen alle productiekosten toe aan het kostenobject
        - Beide gebruiken cost-drivers
    - **Verschillen**:
        - Full costing gebruikt typisch één globale driver (arbeids- of machine-uren); ABC gebruikt meerdere drivers per activiteit
        - ABC is significant duurder in implementatie en onderhoud
        - ABC is vooral nuttig bij heterogene productie + hoge overhead-verhouding
    - ⚠️ **Verwarringsrisico**: ABC wordt soms gepresenteerd als 'vierde methode naast full/direct/standaard' — in werkelijkheid is het een verfijning van full costing op de toerekenings-as.
