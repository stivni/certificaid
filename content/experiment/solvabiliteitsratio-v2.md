---
title: "Solvabiliteitsratio — v2 (ratio + rol×perspectief)"
tags:
  - experiment
  - mockup
status: experimental
mockup: true
linked_anchors:
  - "1.4.III.A"
  - "1.4.III.B"
  - "1.1.III.C"
---

> **Mockup v2 voor ratio-kind** — herstructureerd met rol × perspectief.
> Drempels conceptueel in "Hoe het werkt"; acties per drempel verspreid
> over relevante rollen. Generieke valkuilen verwezen naar kader
> [[jaarrekeninganalyse]]. Vergelijk met
> [[solvabiliteitsratio-v1]].
>
> **Confidence-tekens**: ⚖️ uit bron · 🔗 afgeleid · 🧭 vuistregel · ⚠️ te verifiëren

# Solvabiliteitsratio

De **solvabiliteitsratio** meet de **financiële onafhankelijkheid** van
een onderneming: welk deel van haar totale vermogen wordt door eigen
middelen (eigen vermogen) gefinancierd, t.o.v. door vreemd vermogen
(schulden). Een hogere ratio betekent meer eigen draagkracht en minder
afhankelijkheid van schuldeisers.

## Wat ze economisch echt meet

🔗 Solvabiliteit is een **structuur-ratio** — ze meet de
balans-positie op een moment, niet de cashstroom-positie. Een hoge ratio
(bv. 60 %) betekent: van elke € 100 vermogen is € 60 ingebracht door of
opgebouwd voor aandeelhouders, en € 40 ontleend van derden. Bij tegenslag
heeft de onderneming dus veel **eigen buffer** om verliezen op te vangen
vóór de schuldeisers geraakt worden.

🔗 Een lage ratio (bv. 15 %) betekent het omgekeerde: zware afhankelijkheid
van vreemd vermogen, weinig buffer, hoger faillissementsrisico bij
verlies-jaren.

🔗 Voor liquiditeit-analyse (kan de onderneming haar korte-termijn-verplichtingen
betalen?) gebruik je [[current-ratio]], [[quick-ratio]] of [[cash-ratio]] —
niet de solvabiliteit. Een onderneming kan solvabel *én* illiquide zijn
(en omgekeerd).

## Voorkennis & leespad

- **Lees eerst** (voorvereisten): [[eigen-vermogen]] · [[vreemd-vermogen]]
  · [[jaarrekening-structuur]]
- **Past binnen kader**: [[jaarrekeninganalyse]] — generieke interpretatie-discipline
  (evolutie, sectornorm, balansdatum-effect, correcties) staat daar; in deze
  fiche niet herhaald.
- **Naast deze fiche relevant**: [[current-ratio]] · [[quick-ratio]] ·
  [[interest-coverage-ratio]] · [[ROE]] · [[schuldgraad]]
- **Bij vervolgvragen** lees: [[alarmbel-procedure-bv]] · [[alarmbel-procedure-nv]]

## Hoe het werkt

### Formule

Klassieke formule:

$$\text{Solvabiliteitsratio} = \frac{\text{Eigen vermogen}}{\text{Totaal vermogen}} \times 100\%$$

Equivalent:

$$\text{Solvabiliteitsratio} = \frac{\text{Eigen vermogen}}{\text{Eigen vermogen} + \text{Vreemd vermogen}} \times 100\%$$

Met:
- **Eigen vermogen** = MAR rubriek 10 t/m 15 (kapitaal · uitgiftepremies ·
  herwaarderingsmeerwaarden · reserves · overgedragen resultaat ·
  kapitaalsubsidies)
- **Vreemd vermogen** = MAR rubriek 16 t/m 49 (voorzieningen · schulden > 1 jaar
  · schulden ≤ 1 jaar · overlopende rekeningen passief)
- **Totaal vermogen** = balanstotaal = som van actiefzijde (rubriek 20–58)

#### Balans-illustratie (welke rubrieken tellen mee)

**Eigen vermogen — rubriek 10-15**

| Code | Rubriek |
|---:|---|
| 10 | Kapitaal · gestort + niet-opgevraagd |
| 11 | Uitgiftepremies |
| 12 | Herwaarderingsmeerwaarden |
| 13 | Reserves · wettelijk · onbeschikbaar · beschikbaar |
| 14 | Overgedragen winst (verlies) |
| 15 | Kapitaalsubsidies |

**Vreemd vermogen — rubriek 16-49**

| Code | Rubriek |
|---:|---|
| 16 | Voorzieningen + uitgestelde belastingen |
| 17 | Schulden > 1 jaar |
| 42-49 | Schulden ≤ 1 jaar + overlopende rekeningen passief |

### Varianten van de formule

🔗 Er bestaan **verschillende definities** van solvabiliteit in de
praktijk — let op welke je gebruikt:

| Variant | Formule | Schaal |
|---|---|---|
| Klassiek (boven) | EV / Totaal vermogen | 0–100 % |
| Schuldgraad omgekeerd | Vreemd vermogen / Totaal vermogen | 0–100 % |
| Debt-to-equity (omgekeerd) | EV / Vreemd vermogen | ratio (>1 = sterk) |
| NBB-versie ⚠️ | (te verifiëren — lichtjes andere definitie) | — |
| Bank-versie (Basel) | Risicogewogen — niet voor gewone vennootschappen | — |

🧭 *Vuistregel*: gebruik klassieke formule tenzij de context anders vereist;
lees de definitie van de bron die je gebruikt.

### Voorbeeld berekening

> **NV ABC** heeft op balansdatum:

**Balans-snapshot — NV ABC** (verkort)

| Code | Actief | Bedrag |
|---:|---|---:|
| 20-28 | Vaste activa | 700.000 |
| 29-58 | Vlottende activa | 300.000 |
| | **Balanstotaal** | **1.000.000** |

| Code | Passief | Bedrag |
|---:|---|---:|
| 10-15 | Eigen vermogen | 600.000 |
| 16-49 | Vreemd vermogen (voorzieningen + schulden + overlopende) | 400.000 |
| | **Balanstotaal** | **1.000.000** |

*Berekening*: 600.000 / 1.000.000 × 100 % = **60 %**

🧭 *Interpretatie* (algemeen): zeer gezonde positie — 60 % van het
vermogen is "eigen". Voor elke € 1 schuld heeft de onderneming € 1,5 aan
eigen middelen om op terug te vallen.

> Sector-specifieke benchmarks + algemene interpretatie-discipline
> (evolutie · sectornorm · achtergestelde lening-correctie · samen-lezen):
> zie [[jaarrekeninganalyse]] (kader).

### Interpretatie-drempels (vuistregels)

⚠️ *De volgende drempels zijn **vuistregels** uit de praktijk, geen
wettelijke normen. Sectorgebonden — een industriële onderneming heeft
typisch andere normen dan een vastgoed-vennootschap of een dienstverlener.
Sector-specifieke benchmarks: zie [[jaarrekeninganalyse#sectornorm]].*

| Ratio | Niveau | 🧭 Algemene interpretatie |
|---:|---|---|
| **> 50 %** | Zeer gezond | Sterke eigen buffer; mogelijk overgekapitaliseerd |
| **33–50 %** | Gezond | Comfortabele financieringsstructuur |
| **25–33 %** | Aanvaardbaar | Typisch beeld voor veel KMO's |
| **15–25 %** | Zwak | Verhoogde gevoeligheid voor tegenslag |
| **< 15 %** | Kritisch | Faillissementsrisico bij verlies-jaar |
| **Negatief** | Insolvabel | ⚖️ Alarm-procedure WVV verplicht |

> De **acties** per drempel staan onder
> [Rol van de accountant](#rol-van-de-accountant) per relevante rol —
> wat doet de adviseur, wat doet de boekhouder, wat doet de auditor.

### Wettelijke drempels (alarmbel-procedure WVV)

⚖️ Onder het **WVV-alarmbel-mechanisme**:

| Vennootschap | Drempel | Gevolg |
|---|---|---|
| **BV** | Netto-actief verlies > 50 % EV | Bestuursorgaan roept AV samen binnen 2 maanden ([[WVV#art-5-153]]) |
| **BV** | Netto-actief verlies > 75 % EV | Minderheid kan ontbinding vorderen |
| **NV** | Vergelijkbare regels | ⚠️ [[WVV#art-7-228]] e.v. — exacte drempels te verifiëren |
| **Beide** | Negatief netto-actief | In principe ontbindingsgrond |

🔗 Deze wettelijke drempels werken niet rechtstreeks op de
solvabiliteitsratio, maar op het **netto-actief tegenover het geplaatst
kapitaal of EV**. Toch tonen ze hetzelfde fenomeen: zwakke eigen
vermogen-positie triggert juridische gevolgen.

> Acties per actor bij overschrijden alarm-drempel: zie
> [Rol van de accountant](#rol-van-de-accountant).

### Bijzondere ratio-varianten — wanneer NIET deze formule

- 🔗 **Banken en verzekeringsondernemingen** — gebruiken eigen
  prudentiële solvabiliteitsindicatoren (Basel · Solvency II), niet deze
  klassieke formule.
- 🔗 **Verenigingen zonder winstoogmerk** (vzw) — hebben geen
  aandeelhouders; eigen vermogen-concept verschilt.
- 🔗 **Eenmanszaken** — geen onderscheid tussen vennootschapsvermogen en
  privé-vermogen; ratio is minder zinvol.

### Conceptuele valkuilen (denkfouten)

- 🧭 **Solvabiliteit ≠ liquiditeit**. Solvabiliteit = lange-termijn
  balans-positie; liquiditeit = korte-termijn cashflow-positie.
- 🧭 **Solvabiliteit ≠ rentabiliteit**. Een onderneming met hoge
  solvabiliteit kan slecht renderen; rentabiliteit (ROE) meet
  winstgevendheid.
- 🧭 **"Solvabiliteit" definitie wisselt** tussen bronnen — lees altijd
  welke formule de bron gebruikt.

> **Generieke interpretatie-valkuilen** (één meting in isolatie lezen,
> tijdspunt-fixatie, herwaarderingsmeerwaarden niet corrigeren,
> achtergestelde lening-correctie missen, KMO-bias): zie kader
> [[jaarrekeninganalyse#interpretatie-valkuilen]].

---

## Rol van de accountant

*De accountant zet verschillende hoeden op afhankelijk van voor wie hij
werkt en op welk niveau de ratio actie vereist.*

### 🏢 Voor de onderneming (klant met de ratio)

#### 🎯 Adviseur

**Wat doe je per niveau**:

| Ratio-niveau | Aanbevolen actie |
|---:|---|
| **> 50 %** | 🧭 Overweeg rendabel beleggen of uitkering aan aandeelhouders ([[uitkering-aan-aandeelhouders]]) — overgekapitaliseerd kapitaal rendeert vaak slecht |
| **33–50 %** | 🧭 Geen actie nodig; bewaken via jaarlijkse monitoring |
| **25–33 %** | 🧭 Vermijd verdere schuldopbouw; bewaak schuldgraad |
| **15–25 %** | 🧭 Versterk eigen vermogen — winstinhouding · kapitaalverhoging · achtergestelde lening van aandeelhouders |
| **< 15 %** | 🧭 Urgente actie — herstructurering · kapitaalinjectie · eventueel afstoten niet-strategische activa |
| **Negatief** | ⚖️ Bestuursorgaan attent maken op alarmbel-procedure ([[WVV#art-5-153]]) — AV bijeenroepen binnen 2 maanden, vermogensherstel-plan opstellen |

**Aanvullend**:
- 🧭 Lees ratio in **evolutie over 3-5 jaar** + tegen **sectornorm** — niet
  in isolatie. Methodologie: zie [[jaarrekeninganalyse]].
- 🧭 Bij **achtergestelde leningen** van aandeelhouders: overweeg correctie
  (technisch vreemd vermogen, economisch eigen-vermogen-functie). Methodologie:
  zie [[jaarrekeninganalyse#correcties]].

#### 📋 Boekhouder (verantwoordelijke jaarrekening)

**Bij jaarafsluiting**:
- 🔗 Bereken solvabiliteit als onderdeel van financiële analyse-rapport.
- 🔗 Bij **drempel-overschrijding** (alarm-drempel) → onmiddellijk signaleren
  naar bestuursorgaan; documenteer in werkpapier.
- 🔗 Wettelijke alarmbel-vermelding in toelichting jaarrekening indien
  van toepassing. ⚠️ exacte vermeldingsverplichting te verifiëren.

**Uitvoerings-valkuilen**:
- 🔗 **Herwaarderingsmeerwaarden** (rubriek 12) kunnen ratio kunstmatig
  opblazen → eventueel apart rapporteren (met/zonder herwaardering)
- 🔗 **Overlopende rekeningen** (rubriek 49 vs rubriek 29) correct toewijzen
  aan passief vs actief — een fout schuift de ratio

#### ⚖️ Begeleider bij alarm-procedure (indien drempel overschreden)

🔗 Bij alarm-drempel-overschrijding (BV: > 50 % EV-verlies of negatief
netto-actief):
- ⚖️ Organiseer **bijeenroeping AV** door bestuursorgaan binnen 2 maanden
  ([[WVV#art-5-153]])
- 🔗 Werk mee aan **vermogensherstel-plan** (kapitaalverhoging · inbreng ·
  herstructurering · afstoting)
- 🔗 Documenteer beslissingsproces voor traceerbaarheid (audit-trail)

### 🔍 Als auditor / commissaris (extern perspectief)

#### Beoordeling continuïteit

- ⚖️ Solvabiliteit-niveau als indicator voor **going-concern-beoordeling**
- 🔗 Bij **kritisch niveau** of negatief netto-actief: extra audit-procedures
  vereist (cashflow-projectie, herfinancierings-plan, brieven van aandeelhouders)
- ⚖️ Bij overschrijden wettelijke alarmbel-drempel: controleren of
  **bestuur de procedure heeft gevolgd** (AV-bijeenroeping · vermogensherstel-plan)
- ⚠️ Vermelding in auditverslag bij niet-naleving — exacte formulering
  per ITAA-norm/IBR te verifiëren.

#### Controle-aandachtspunten

- 🔗 Berekeningsmethode consistent t.o.v. vorig boekjaar
- 🔗 Correcte rubricering eigen vs vreemd vermogen
- 🔗 Achtergestelde leningen correct geclassificeerd
- 🔗 Toelichting jaarrekening volledig bij overschrijden van wettelijke
  drempels

### 💰 Voor externe partij (kredietverstrekker · due diligence)

🧭 Optioneel relevant — bv. bij **due diligence vóór overname** of bij
**kredietbeoordeling**:

- 🧭 Solvabiliteit als één van meerdere kerngetallen voor
  kredietwaardigheidsbeoordeling
- 🧭 Vergelijk met sectornorm + concurrenten
- 🧭 Bij overname-context: correctie voor goodwill en hidden reserves

## Veelvoorkomende verwarringen

- **Solvabiliteit ≠ liquiditeit**. Solvabiliteit = lange-termijn balans-positie;
  liquiditeit = korte-termijn cashflow-positie. Een onderneming kan solvabel
  én illiquide zijn (en omgekeerd).
  Edge `verward_met` → [[current-ratio]].
- **Solvabiliteit ≠ rentabiliteit**. Een onderneming met hoge solvabiliteit
  kan slecht renderen; rentabiliteit (ROE) meet winstgevendheid.
  Edge `verward_met` → [[ROE]].
- **"Eigen vermogen / Vreemd vermogen"** (debt-to-equity omgekeerd) wordt
  soms ook "solvabiliteit" genoemd — andere schaal (60/40 = 1,5 i.p.v.
  60 %). Lees de definitie!
- **NBB-solvabiliteit** voor banken (Tier 1 ratio's) is een ander concept —
  risicogewogen activa, niet van toepassing op gewone ondernemingen.

## Familie & alternatieven

### Binnen kader [[jaarrekeninganalyse]] (verwante ratios — samen lezen)

- [[current-ratio]] — liquiditeit korte termijn
- [[quick-ratio]] — strenge liquiditeit
- [[cash-ratio]] — meest stringente liquiditeit
- [[interest-coverage-ratio]] — kan operationele winst de rentelast dragen?
- [[ROE]] · [[ROA]] — rentabiliteit-ratios
- [[schuldgraad]] — omgekeerd; zelfde info
- [[werkkapitaalbehoefte]] — operationele cashbehoefte

🧭 *"Een onderneming met solvabiliteit 50 % maar quick ratio 0,3 staat op
springen"* — twee ratios, twee dimensies, beide nodig.

### Buiten dit kader, maar gerelateerd

- [[alarmbel-procedure-bv]] · [[alarmbel-procedure-nv]] — juridische procedure
  die gemarkeerd wordt door negatieve solvabiliteit
- [[kapitaalverhoging]] · [[achtergestelde-lening]] — instrumenten om EV
  te versterken

## Wat dit record dekt

### Behandelde competenties (chronologisch — bij analyse)

1. **Balans lezen** en eigen vermogen vs vreemd vermogen onderscheiden.
2. **Solvabiliteitsratio berekenen** uit jaarrekening.
3. **Interpreteren** t.o.v. vuistregel-drempels en sectornorm.
4. **Evolutie analyseren** over 3-5 jaar (zie [[jaarrekeninganalyse]]).
5. **Correcties toepassen** voor achtergestelde leningen,
   herwaarderingsmeerwaarden.
6. **Samen lezen** met liquiditeit- en rentabiliteit-ratios.
7. **Bestuur of klant adviseren** op basis van geconstateerd niveau (per
   drempel andere actie) — zie [🎯 Adviseur](#-adviseur).
8. **Alarm-procedure** herkennen bij negatieve eigen vermogen-positie ⚖️ —
   zie [⚖️ Begeleider bij alarm-procedure](#-begeleider-bij-alarm-procedure-indien-drempel-overschreden).
9. **Auditor-beoordeling** going concern + alarm-naleving — zie
   [🔍 Als auditor](#-als-auditor--commissaris-extern-perspectief).

### Behandelde termen (alfabetisch)

achtergestelde lening (correctie) · alarm-procedure · balansdatum-effect ·
debt-to-equity · eigen vermogen · financiële onafhankelijkheid ·
herwaarderingsmeerwaarde · liquiditeitsratio (vergelijking) · netto-actief ·
rentabiliteitsratio (vergelijking) · schuldgraad · sectornorm ·
solvabiliteit · Tier 1 (banken — niet van toepassing) · totaal passief ·
vreemd vermogen

### Behandelde formules

- **Solvabiliteitsratio (klassiek)** = Eigen vermogen / Totaal passief × 100 %
- **Schuldgraad** = 100 % − Solvabiliteitsratio
- **Debt-to-equity (omgekeerd)** = Eigen vermogen / Vreemd vermogen

### Drempels (vuistregels — geen wet)

Zie tabel onder [Interpretatie-drempels](#interpretatie-drempels-vuistregels)
+ acties onder [🎯 Adviseur](#-adviseur).

### Wettelijke drempels (alarmbel)

- **BV verlies > 50 % EV**: AV bijeenroepen ⚖️ [[WVV#art-5-153]]
- **BV verlies > 75 % EV**: ontbinding vorderbaar
- **NV vergelijkbaar**: ⚠️ [[WVV#art-7-228]] te verifiëren

## Bronnen en verwijzingen

**Bronnen (grounded)** ⚖️:
- [[WVV#art-5-153]] — Alarmbel-procedure BV
- ⚠️ [[WVV#art-7-228]] e.v. — Alarmbel NV (te verifiëren)
- [[MAR]] — Eigen vermogen rubriek 10-15; vreemd vermogen 16-49

**Praktijk-referenties**:
- ⚠️ Nationale Bank van België (NBB) — Centrale voor Balansen, sectorale
  statistieken
- ⚠️ ITAA-praktijkgids financiële analyse — drempels en interpretatie

**Te verifiëren** ⚠️:
- Exact artikel alarmbelprocedure NV
- NBB-definitie solvabiliteit (eventueel afwijkend)
- Sector-specifieke benchmarks per NACE-categorie
- Toelichtingsverplichting bij alarmbel

**Cross-record edges**:
- `onderdeel_van` → [[jaarrekeninganalyse]] *(kader)*
- `gerelateerd` → [[current-ratio]], [[quick-ratio]], [[cash-ratio]],
  [[ROE]], [[ROA]], [[interest-coverage-ratio]], [[schuldgraad]]
- `verward_met` → [[current-ratio]] *(solvabiliteit ≠ liquiditeit)*,
  [[ROE]] *(solvabiliteit ≠ rentabiliteit)*
- `triggert_procedure` → [[alarmbel-procedure-bv]], [[alarmbel-procedure-nv]]
- `niet_van_toepassing_op` → banken *(Basel)*, verzekeringsondernemingen
  *(Solvency II)*, vzw, eenmanszaak

---

## Iteratie-log

**v2 (huidige)** — herstructureerd t.o.v. v1:

- **Top-volgorde uniform** met andere kinds: Definitie → Wat economisch →
  Voorkennis & leespad → Hoe het werkt → Rol van de accountant →
  Verwarringen → Familie & alternatieven → Wat dit record dekt → Bronnen.
- **Drempels-tabel conceptueel** in "Hoe het werkt"; **acties per drempel**
  verhuisd naar Rol > 🎯 Adviseur (drempel-actie-tabel).
- **Wettelijke alarmbel-drempels** verspreid over alle relevante rollen
  (Adviseur · Boekhouder · Begeleider · Auditor) — niet alleen auditor.
- **Generieke valkuilen verwezen** naar [[jaarrekeninganalyse]] (kader) —
  evolutie · sectornorm · balansdatum-effect · achtergestelde lening-correctie ·
  KMO-bias. In dit record alleen ratio-specifieke valkuilen.
- **Balans-illustratie** voor MAR-rubrieken (ipv tekstuele opsomming).
- **Rol-structuur** met vier klant-perspectieven: onderneming · auditor ·
  optioneel externe partij. Bij onderneming meerdere rollen (Adviseur ·
  Boekhouder · Begeleider bij alarm).
- **Leespad-suggestie** — voorkennis + kader + nabije fiches.
- **Examen-context weggehaald** — geen "in examen-context"-zinnen meer.

**Open punten**:
- Bij "Bijzondere ratio-varianten" (banken Basel, vzw, eenmanszaak):
  eigen records of in deze als afsluitende rubriek? Voorlopig laatste.
- **Beslisboom** voor "wanneer welke ratio?" hoort in
  [[jaarrekeninganalyse]] (kader), niet hier.
- ⚠️ Achtergestelde lening-correctie wordt nu in twee fiches genoemd
  (hier + kader) — checken of we het exact één keer schrijven (in kader)
  + alleen referentie hier.
