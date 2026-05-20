---
title: "Solvabiliteitsratio — v1 (ratio-mockup)"
tags:
  - experiment
  - mockup
status: experimental
mockup: true
---

> **Mockup om het schema 1.7-model te testen op een ratio** — structureel
> heel anders dan instrument/operatie/regime. Een ratio meet iets, heeft
> drempels en bijbehorende acties. Geen actoren, geen boekingen, geen
> formaliteiten.
>
> **Confidence-tekens**: ⚖️ uit bron · 🔗 afgeleid · 🧭 vuistregel · ⚠️ te verifiëren

# Solvabiliteitsratio

De **solvabiliteitsratio** meet de **financiële onafhankelijkheid** van
een onderneming: welk deel van haar totale vermogen wordt door eigen
middelen (eigen vermogen) gefinancierd, t.o.v. door vreemd vermogen
(schulden). Een hogere ratio betekent meer eigen draagkracht en minder
afhankelijkheid van schuldeisers.

🔗 Het is een **structuur-ratio**, niet een **liquiditeit-ratio**: ze
zegt iets over de balans-positie op een moment, niet over de
cashstroom-positie. Voor liquiditeit-analyse → [[current-ratio]],
[[quick-ratio]], [[cash-ratio]].

🔗 Ze wordt door **banken, leveranciers, kredietverzekeraars en het
bestuursorgaan** gebruikt als een eerste indicatie van **kredietwaardigheid
en draagkracht bij tegenslag**.

## Wat ze meet

🔗 De solvabiliteitsratio antwoordt op de vraag: **"Hoeveel van de
onderneming is eigendom van de aandeelhouders zelf, en hoeveel is
gefinancierd via derden?"**

Een hoge ratio (bv. 60 %) betekent: van elke € 100 vermogen is € 60
ingebracht door of opgebouwd voor aandeelhouders (eigen vermogen), en
€ 40 ontleend van derden. Bij tegenslag heeft de onderneming dus veel
**eigen buffer** om verliezen op te vangen vóór de schuldeisers geraakt
worden.

Een lage ratio (bv. 15 %) betekent het omgekeerde: zware afhankelijkheid
van vreemd vermogen, weinig buffer, hoger faillissementsrisico bij
verlies-jaren.

## Formule

⚖️ Klassieke formule:

$$\text{Solvabiliteitsratio} = \frac{\text{Eigen vermogen}}{\text{Totaal vermogen (= Totaal passief = Totaal actief)}} \times 100\%$$

Of equivalent geformuleerd:

$$\text{Solvabiliteitsratio} = \frac{\text{Eigen vermogen}}{\text{Eigen vermogen} + \text{Vreemd vermogen}} \times 100\%$$

🔗 **Eigen vermogen** = MAR rubriek 10 t/m 15 (kapitaal, uitgiftepremies,
herwaarderingsmeerwaarden, reserves, overgedragen resultaat,
kapitaalsubsidies).

🔗 **Vreemd vermogen** = MAR rubriek 16 t/m 49 (voorzieningen,
schulden > 1 jaar, schulden ≤ 1 jaar, overlopende rekeningen passief).

🔗 **Totaal passief** = MAR rubriek 10-49 = balanstotaal = som van
actiefzijde (rubriek 20-58).

### Varianten van de formule

🔗 Er bestaan **verschillende definities** van solvabiliteit in de
praktijk — let op welke je gebruikt:

1. **Klassiek (boven)**: Eigen vermogen / Totaal vermogen.
2. **Schuldgraad omgekeerd**: 100 % − Solvabiliteitsratio = Schuldgraad.
3. **Eigen-vermogen / Vreemd-vermogen** (debt-to-equity omgekeerd) —
   zelfde info, andere schaal.
4. **NBB-versie**: ⚠️ Nationale Bank van België publiceert sectorale
   solvabiliteitsstatistieken met eigen, lichtjes andere definitie.
   Te verifiëren.
5. **Bank-versie** (Basel-context): risicogewogen activa — niet van
   toepassing op gewone vennootschappen.

🧭 *In examen-context: gebruik formule 1 tenzij anders gevraagd. Als de
opgave een andere formule impliceert, lees de definitie zorgvuldig.*

## Voorbeeld berekening

> **NV ABC** heeft op balansdatum:
> - Eigen vermogen: € 600.000 (rubriek 10-15)
> - Voorzieningen + schulden + overlopende rekeningen passief: € 400.000
>   (rubriek 16-49)
> - Balanstotaal: € 1.000.000
>
> Solvabiliteitsratio = 600.000 / 1.000.000 × 100 % = **60 %**
>
> 🧭 Interpretatie: zeer gezonde positie — 60 % van het vermogen is
> "eigen". Voor elke € 1 schuld heeft de onderneming € 1,5 aan eigen
> middelen om op terug te vallen.

## Interpretatie — drempels en bijbehorende acties

⚠️ *De volgende drempels zijn **vuistregels** uit de praktijk, geen
wettelijke normen. Sectorgebonden — een industriële onderneming heeft
typisch andere normen dan een vastgoed-vennootschap of een dienstverlener.
Cijferzakboekje of NBB-sectorstatistieken te raadplegen voor
sector-specifieke benchmarks.*

| Ratio | 🧭 Algemene interpretatie | Aanbevolen actie |
|---:|---|---|
| **> 50 %** | Zeer gezond — sterke eigen buffer; mogelijk overgekapitaliseerd | Overweeg rendabel beleggen / uitkering aan aandeelhouders |
| **33 % – 50 %** | Gezond — comfortabele financieringsstructuur | Geen actie nodig; bewaken |
| **25 % – 33 %** | Aanvaardbaar — typisch beeld voor veel KMO's | Vermijd verdere schuldopbouw |
| **15 % – 25 %** | Zwak — verhoogde gevoeligheid voor tegenslag | Eigen vermogen versterken (kapitaal · winstinhouding) |
| **< 15 %** | Kritisch — faillissementsrisico bij verlies-jaar | Urgente herstructurering of kapitaalinjectie nodig |
| **Negatief** | Insolvabel — eigen vermogen verteerd door verliezen | ⚖️ Alarm-procedure ([[WVV#art-2-52]] e.v.) verplicht |

### Bijzondere drempels (wettelijk)

⚖️ Onder het **WVV-alarmbel-procedure**:

- **BV**: bij verlies van **meer dan helft** van het netto-actief
  (verlies > 50 % EV): bestuursorgaan moet algemene vergadering bijeenroepen
  binnen 2 maanden ⚖️ [[WVV#art-5-153]].
- **BV**: bij verlies van **meer dan driekwart** van het netto-actief
  (verlies > 75 % EV): minderheid kan **ontbinding** vorderen.
- **NV**: vergelijkbare regels in ⚖️ [[WVV#art-7-228]] e.v. ⚠️ exacte
  drempels en procedure te verifiëren.
- **Negatief netto-actief**: in principe **ontbindingsgrond**.

🔗 Deze wettelijke drempels werken niet rechtstreeks op de
solvabiliteitsratio, maar op het **netto-actief tegenover de geplaatste
vermogen of het kapitaal**. Toch tonen ze hetzelfde fenomeen: zwakke
eigen vermogen-positie triggert juridische gevolgen.

## Sectorgebondenheid — let op de norm

🔗 De solvabiliteitsratio is **niet over sectoren heen vergelijkbaar
zonder context**:

- 🧭 **Industriële onderneming** met zware vaste activa: typisch 30–50 %.
- 🧭 **Vastgoedvennootschap** of holding: kan lager (20–35 %) zonder
  alarm — vaste activa worden vaak met lange-termijn-schuld gefinancierd.
- 🧭 **Dienstverlener** zonder veel materiele activa: typisch hoger
  (40–60 %) omdat investeringen in mensen niet activeerbaar zijn.
- 🧭 **Start-up / scale-up**: kan kunstmatig hoog zijn (cash uit
  investeringsronde nog niet besteed) of laag (verliezen al consumed).

⚠️ NBB sectorale statistieken (Centrale voor Balansen) als benchmark —
te raadplegen.

## Verwante ratios — samen lezen

🔗 Solvabiliteitsratio op zich is **nooit voldoende** voor een oordeel.
Lees altijd samen met:

- **[[current-ratio]]** of **[[quick-ratio]]** — liquiditeit op korte
  termijn. Een solvabele onderneming kan toch kortetermijn-liquiditeitsproblemen
  hebben.
- **[[rentabiliteit-eigen-vermogen]]** (ROE) — geeft hoog eigen vermogen
  voldoende rendement?
- **[[schuldgraad]]** — omgekeerd; bevestigt verhouding.
- **[[interest-coverage-ratio]]** — kan de operationele winst de
  intrestlast dragen?

🧭 *Vuistregel*: "een onderneming met solvabiliteit 50 % maar quick ratio
0,3 staat op springen". Twee ratios, twee dimensies, beide nodig.

## Valkuilen in interpretatie

- 🎯 *Adviseur* — 🧭 **Ratio in isolatie lezen** zonder sectorbenchmark
  → verkeerd alarm of vals comfort.
- 🎯 *Adviseur* — 🧭 **Tijdspunt-fixatie** — één balansdatum kan vertekend
  zijn door eindejaars-effecten (grote leverancierskrediet net binnen,
  dividend net uitbetaald, …). Lees evolutie over 3-5 jaar.
- 🔍 *Auditor* — 🧭 **Herwaarderingsmeerwaarden** kunnen het eigen vermogen
  artificieel opblazen — kijk naar **gestort kapitaal + reserves** zonder
  herwaardering voor een conservatiever beeld.
- 🔍 *Auditor* — 🧭 **Achtergestelde leningen** (van bv. de aandeelhouder)
  staan technisch onder vreemd vermogen maar dragen economisch eigen-vermogen-functie.
  Verschillende analisten passen hier verschillende correcties toe — wees
  consistent.
- 📋 *Boekhouder* — 🔗 **Overlopende rekeningen** correct toewijzen aan
  passief vs actief — een fout schuift de ratio.
- 🎯 *Adviseur* — 🧭 **KMO-bias**: KMO's hebben vaak lagere solvabiliteit
  dan grote ondernemingen, niet omdat ze ongezonder zijn maar omdat hun
  kapitalisatie typisch minder uitgesproken is. Vergelijk met sector +
  groottecategorie.

## Veelvoorkomende verwarringen

- **Solvabiliteit ≠ liquiditeit**. Solvabiliteit = lange-termijn balans-positie;
  liquiditeit = korte-termijn cashflow-positie. Een onderneming kan
  solvabel én illiquide zijn (en omgekeerd).
- **Solvabiliteit ≠ rentabiliteit**. Een onderneming met hoge solvabiliteit
  kan slecht renderen; rentabiliteit (ROE) meet winstgevendheid van het
  eigen vermogen.
- **"Eigen vermogen / Vreemd vermogen"** (debt-to-equity omgekeerd) wordt
  soms ook "solvabiliteit" genoemd. Schaal is anders dan de klassieke
  formule (60 / 40 = 1,5 i.p.v. 60 %). Lees de definitie!
- **NBB-solvabiliteit** voor banken (Tier 1 ratio's) is een ander concept
  — risicogewogen activa, niet van toepassing op gewone ondernemingen.

## Niet van toepassing op (scope)

- 🔗 **Banken en verzekeringsondernemingen** — gebruiken eigen
  prudentiële solvabiliteitsindicatoren (Basel · Solvency II), niet
  deze klassieke formule.
- 🔗 **Verenigingen zonder winstoogmerk** (vzw) — hebben geen
  aandeelhouders; eigen vermogen-concept verschilt.
- 🔗 **Eenmanszaken** — geen onderscheid tussen vennootschapsvermogen en
  privé-vermogen; ratio is minder zinvol.

## Wat dit record dekt

### Behandelde competenties (chronologisch — bij analyse)

1. **Balans lezen** en eigen vermogen vs vreemd vermogen onderscheiden.
2. **Solvabiliteitsratio berekenen** uit jaarrekening.
3. **Interpreteren** t.o.v. drempels en sectornorm.
4. **Evolutie analyseren** over 3-5 jaar.
5. **Correcties toepassen** voor achtergestelde leningen, herwaarderingsmeerwaarden.
6. **Samen lezen** met liquiditeit- en rentabiliteit-ratios.
7. **Bestuur of klant adviseren** op basis van geconstateerd niveau.
8. **Alarm-procedure** herkennen bij negatieve eigen vermogen-positie
   ⚖️ [[WVV]].

### Behandelde termen (alfabetisch)

achtergestelde lening (correctie) · alarm-procedure · balansdatum-effect ·
debt-to-equity · eigen vermogen · financiële onafhankelijkheid ·
herwaarderingsmeerwaarde · liquiditeitsratio (vergelijking) · netto-actief ·
rentabiliteitsratio (vergelijking) · schuldgraad · sectornorm ·
solvabiliteit · Tier 1 (banken — niet van toepassing) ·
totaal passief · vreemd vermogen

### Behandelde formules

- **Solvabiliteitsratio (klassiek)** = Eigen vermogen / Totaal passief × 100 %
- **Schuldgraad** = 100 % − Solvabiliteitsratio
- **Debt-to-equity (omgekeerd)** = Eigen vermogen / Vreemd vermogen

### Drempels (vuistregels — geen wet)

| Niveau | Drempel | Acties |
|---|---|---|
| Zeer gezond | > 50 % | Overweeg uitkering of investering |
| Gezond | 33–50 % | Bewaken |
| Aanvaardbaar | 25–33 % | Vermijd schuldopbouw |
| Zwak | 15–25 % | Versterk eigen vermogen |
| Kritisch | < 15 % | Urgente actie |
| Negatief | < 0 % | ⚖️ Alarm-procedure WVV |

### Wettelijke drempels

- **BV verlies > 50 % EV**: AV bijeenroepen ⚖️ [[WVV#art-5-153]]
- **BV verlies > 75 % EV**: ontbinding vorderbaar
- **NV vergelijkbaar**: ⚖️ [[WVV#art-7-228]] ⚠️ te verifiëren

## Alternatieven (zelfde doel: financiële sterkte beoordelen)

- [[current-ratio]] — liquiditeit korte termijn
- [[quick-ratio]] — strenge liquiditeit
- [[cash-ratio]] — meest stringente liquiditeit
- [[interest-coverage-ratio]] — kan winst rentelast dragen?
- [[ROE]] · [[ROA]] — rentabiliteit-ratios
- [[schuldgraad]] — omgekeerd; zelfde info
- [[werkkapitaalbehoefte]] — operationele cashbehoefte

→ Vergelijkingsmatrix: [[vergelijking-financiele-ratios]]

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

**Cross-record edges**:
- `gerelateerd` → [[current-ratio]], [[quick-ratio]], [[cash-ratio]],
  [[ROE]], [[ROA]], [[interest-coverage-ratio]], [[schuldgraad]]
- `verward_met` → [[current-ratio]] *(solvabiliteit ≠ liquiditeit)*,
  [[ROE]] *(solvabiliteit ≠ rentabiliteit)*
- `triggert_procedure` → [[alarmbel-procedure-bv]],
  [[alarmbel-procedure-nv]]
- `niet_van_toepassing_op` → [[banken]] *(Basel)*, [[verzekeringsondernemingen]]
  *(Solvency II)*, [[vzw]], [[eenmanszaak]]

---

## Iteratie-log

**v1 (huidige)** — eerste mockup van een **ratio**. Structuur fundamenteel
anders dan instrument/operatie/regime.

**Wat opvalt vs de andere kinds**:

- **Geen "Hoe het werkt"-met-onderdelen**, geen boekingen, geen perspectieven
  per actor. Een ratio is een **meting** + **interpretatie**, geen
  uitvoering van een operatie.
- **Centrale rubrieken**:
  1. *Wat meet ze* (concept)
  2. *Formule* (berekening)
  3. *Voorbeeld* (toepassing)
  4. *Interpretatie-drempels* (vuistregels per niveau)
  5. *Bijbehorende acties* per drempel
  6. *Sectorgebondenheid* (norm verschilt per sector)
  7. *Verwante ratios* (samen lezen)
  8. *Valkuilen in interpretatie*
  9. *Niet van toepassing op* (scope)
- **Drempels-tabel als hoofd-rubriek**, niet als bijzaak. De analyse-actie
  hangt direct af van de waarde — vandaar dat drempels + acties samen
  in één tabel staan.
- **Wettelijke drempels** apart (alarmbelprocedure) — ook al is het strikt
  niet de ratio zelf, het tikt aan op dezelfde realiteit.
- **Geen Cijferzakboekje-issue**: ratio-drempels zijn vuistregels, niet
  wettelijke cijfers. Sectorale NBB-statistieken wel relevant maar niet
  blokkerend.

**Open punten**:
- Voor ratios: moet **"Wettelijke drempels"** een eigen rubriek zijn, of
  geïntegreerd in de drempels-tabel met ⚖️-markering?
- **Sectorgebondenheid** krijgt eigen rubriek — bij andere kinds was dit
  geen issue. Mogelijk een nieuw rubriek-type voor ratios.
- **Bijzondere ratios** (bank-Tier 1, verzekering-Solvency II) — eigen
  records of in deze als sub-onderdeel?
- **Aansluiting met kader-records**: solvabiliteitsratio hoort bij het
  bredere kader [[financiele-analyse]] — moet die kader-link er expliciet
  zijn?
- **Drempels in JSON-schema**: hoe modeleren we `drempels[]` met
  `niveau`, `range`, `interpretatie`, `actie`? Nieuwe sub-structuur in
  schema 1.7.
