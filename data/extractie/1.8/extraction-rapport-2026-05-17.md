# PO 1.8 — Concept-extractie rapport

**Datum**: 2026-05-17
**Run-tag**: `concept-extractie-v4-2026-05-17T00:00Z`
**Model**: claude-opus-4-7
**Prompt-versie**: `prompts/concept-extractie-v4.md` (schema 1.4) + delta op v3
**Bundles verwerkt**: 26 (1.8.taak.1, 1.8.I + I.A-B, 1.8.II + II.A-D, 1.8.III + III.A-F, 1.8.IV + IV.A-C, 1.8.V, 1.8.VI + VI.A-D)

---

## Samenvatting

- **44 nieuwe concept-records** aangemaakt, gegroepeerd in 5 clusters:
  - Cluster I/IV (presentatie + organisatie): 9 records
  - Cluster II (kostencomponenten): 8 records
  - Cluster III (calculatiemethoden): 12 records
  - Cluster V/VI (budget): 7 records
  - Stub + cross-PO context: 2 records (`algemene-boekhouding`, `voorraadwaardering`)
  - Beslissingsraamwerk (taak.1): 3 records (`kostenanalyse-make-or-buy`, `sunk-cost`, `opportuniteitskost`)
  - Synthese-records: 3 records (`typologie-van-kosten`, `costing-methodes-vergelijking`, `budget-cyclus`)
- **Geen bestaande records bijgewerkt** — clean slate voor PO 1.8.
- **Geen dangling-references-bestand** geschreven (geen significante hiaten gedetecteerd buiten de bron-gap-claims hieronder).

---

## Anchor-coverage (records per anchor — minstens 2 per anchor verwacht)

| Anchor | # records |
|---|---|
| 1.8.taak.1 | 5 |
| 1.8.I | 4 |
| 1.8.I.A | 2 |
| 1.8.I.B | 3 |
| 1.8.II | 0* |
| 1.8.II.A | 9 |
| 1.8.II.B | 3 |
| 1.8.II.C | 2 |
| 1.8.II.D | 2 |
| 1.8.III | 5 |
| 1.8.III.A | 11 |
| 1.8.III.B | 5 |
| 1.8.III.C | 4 |
| 1.8.III.D | 4 |
| 1.8.III.E | 8 |
| 1.8.III.F | 4 |
| 1.8.IV | 3 |
| 1.8.IV.A | 6 |
| 1.8.IV.B | 3 |
| 1.8.IV.C | 5 |
| 1.8.V | 2 |
| 1.8.VI | 6 |
| 1.8.VI.A | 2 |
| 1.8.VI.B | 3 |
| 1.8.VI.C | 2 |
| 1.8.VI.D | 4 |

\*1.8.II is een overzichtsanchor (KOSTENCOMPONENTEN); de 4 subanchor II.A-D dekken het fenomeen volledig.

---

## Bron-gap-lijst (vakdoctrine-claims)

Voor PO 1.8 zijn veel kernconcepten **management-accounting-doctrine** zonder Belgische trusted wettelijke of CBN-bron. Onderstaande records dragen één of meer claims met `confidence: "inferred-common-knowledge"` en hebben een `_provenance.bron_gap`-veld.

| Concept | Bron-gap-aard | Wel grounded in CBN? |
|---|---|---|
| `analytische-boekhouding` | Geen wettelijke definitie | Begrip 'algemene boekhouding' wel (CBN 174/1); analytische is conventioneel |
| `doelstellingen-analytische-boekhouding` | Klassieke 4-doelen-opsomming | Geen |
| `typologie-van-kosten` | Direct/indirect, vast/variabel = vakdoctrine | CBN 132/7 §2.1 gebruikt 'directe' en 'onrechtstreekse' productiekosten — partieel grounded |
| `vaste-kosten` / `variabele-kosten` | Begripsdefinitie | Niet rechtstreeks |
| `directe-kosten` / `indirecte-kosten` | Definitie + verdeelsleutel-keuze | Wettelijke noodzaak indirecte deel in vervaardigingsprijs wél (CBN 132/7) |
| `kostencentrum` / `kostendrager` / `verdeelsleutel` | Conventionele indeling | Niet rechtstreeks |
| `volledige-kostencalculatie` (full costing) | Methode-stappen | Wettelijk verankerd in CBN 132/7 + 2012/15 — grounded voor voorraadwaardering |
| `direct-costing` | Methode-stappen | Wettelijk toegelaten — CBN 2012/15 |
| `voorbepaalde-kosten` / `werkelijke-kostencalculatie` | Standaardkostprijs-mechaniek | Niet rechtstreeks |
| `break-even-analyse` | Formule + concept | **Geen Belgische trusted bron** — pure management-accounting-doctrine |
| `contributiemarge` | Definitie + formule | Geen |
| `marginale-kostprijs` / `gemiddelde-kostprijs` | Beslissingsbegrippen | Geen |
| `abc-methode` (Activity Based Costing) | 5-stappen-protocol + cost-driver-concept | **Geen Belgische trusted bron** — Cooper-Kaplan 1980s |
| `budgetbeheer` + alle budget-records | Procedure + verschillen-analyse | Geen — vakdoctrine in toto |
| `sunk-cost` / `opportuniteitskost` | Beslissings-economische begrippen | Geen |
| `kostenanalyse-make-or-buy` | Afwegingsraamwerk | Geen |

**Wel grounded (met CBN/KB-bron)**:
- `vervaardigingsprijs` — KB 21.10.2018 art. 22 + CBN 132/7 §2.1
- `materiaalkosten` (voorraad-component) — CBN 132/7
- `arbeidskosten` (bezoldigingsbegrip) — WIB92 art. 30-31 + Wet 3 juli 1978
- `overige-kosten` (klasse 61, 63, 64) — KB 21.10.2018 MAR
- `registratiesysteem-eenvoudige-integratie` / `proportionele-integratie` / `waarderingsneutraal` — CBN 3/3 (joint-venture-context, analoog gebruikt)
- `rekeningenstelsel-analytisch` (klasse 9 vrij) — KB 21.10.2018 MAR Bijlage 1
- `voorraadwaardering` — CBN 132/7

---

## Anti-collisie-log (overlap met andere PO's)

PO 1.8 overlapt deels met:

- **PO 1.1** (algemene boekhouding) — *kostenboeking* en *voorraadboekhouding* horen primair bij 1.1. Hier behouden:
  - `materiaalkosten` (perspectief: kostprijs-component, niet boekingstechniek)
  - `arbeidskosten` (perspectief: kostencomponent voor productie)
  - `algemene-boekhouding` — **stub-record** met expliciete `extractie_opmerking`; volledige uitwerking hoort in PO 1.1
  - `voorraadwaardering` — overlapt met PO 1.1 voorraad-record (PO 1.1 record bestaat nog niet; tijdelijk hier behouden, eventueel later mergen)
- **PO 1.3** (analyse van financiële situatie) — analyse-aspect van 1.8.taak.1 ('Analyseren van de financiële situatie'). Hier focus op kostprijs-redenering (make-or-buy, marginale kost). Algemene financiële analyse (ratio's, balans-analyse) blijft PO 1.3. Geen records gedupliceerd.
- **PO 1.4** (consolidatie) — geen overlap.
- **PO 1.7** (interne controle) — kostencentrum-budgetcontrole heeft raakvlak met intern-controle-systeem. Hier focus op het budgetbeheer als instrument, niet op intern-controle-design.

Geen records geskipt wegens duplicaat. Stub voor `algemene-boekhouding` toegevoegd (geen volledige uitwerking).

---

## Schema-1.4-feature-gebruik

| Feature | Aantal records | Voorbeelden |
|---|---|---|
| `bouwstenen[]` met titel + wat + waarom + voorbeeld_inline + grondslag + confidence | ±20 | `integrale-consolidatie`-stijl: `vervaardigingsprijs`, `arbeidskosten`, `indirecte-kosten` |
| `berekeningsmethode[]` met `formules[]` (id + wiskunde + variabelen + invulling_voorbeeld) | 6 | `contributiemarge` (3 formules), `break-even-analyse` (3 formules), `verschillenboekhouding` (2), `vervaardigingsprijs` (1), `voorbepaalde-kosten` (impliciet), `direct-costing` (impliciet) |
| `stappen[]` met `voorbeeld.substappen[]` (balans-/berekening-substappen) | 3 | `vervaardigingsprijs`, `break-even-analyse`, `budgetprocedure` |
| `edges[]` (gepopuleerd, niet leeg) | 44 (alle) | `onderdeel-van`, `bevat`, `vergelijkt-met`, `vereist-kennis-van`, `getriggerd-door`, `specialisatie-van` |
| `vergelijkingsparen[]` (echte verwarringsrisico's) | ±18 | `directe-kosten` ↔ `variabele-kosten`, `marginale-kostprijs` ↔ `gemiddelde-kostprijs`, `full costing` ↔ `direct costing` |
| `node_type: synthese` (vergelijkingstabel + beslisboom) | 3 | `typologie-van-kosten`, `costing-methodes-vergelijking`, `budget-cyclus` |
| Cast-namen (Yperse Werkplaats BV + Marleen De Cock + ...) | 44 (alle voorbeelden) | Geen 'M / D / X / Y' meer |
| €-bedragen met duizendtal-formaat | Bijna alle voorbeelden | `€ 800.000`, `€ 12.000`, `€ 250.000` etc. |

---

## Voorbeeld-minimum-check per node-type (regel 13)

| Node-type | Minimum | Records die daaraan voldoen |
|---|---|---|
| `begrip` / `fenomeen` (≥ 1 `voorbeeld_inline`) | OK | Alle 20+ begrip-records bevatten `voorbeeld_inline` op record-niveau of in bouwsteen |
| `methode` / `procedure` (≥ 1 numeriek voorbeeld via formule of substappen) | OK | `volledige-kostencalculatie`, `direct-costing`, `voorbepaalde-kosten`, `werkelijke-kostencalculatie`, `abc-methode`, `break-even-analyse`, `verschillenboekhouding`, `budgetprocedure`, `vervaardigingsprijs`, `registratiesysteem-*` — allemaal met concrete Yperse-cijfers |
| `regel` / `verplichting` (≥ 1 voorbeeld met cliëntsituatie) | OK | `vervaardigingsprijs`, `voorraadwaardering` |
| `synthese` (worked example in tabel of beslisboom) | OK | Alle 3 synthese-records bevatten zowel vergelijkingstabel als beslisboom (mermaid) |

**Geen records met `> [!todo] Voorbeeld ontbreekt`-status.**

---

## Bedragen-consistentie (regel 14a)

Gebruikt cast-`kostenanalyse_volledig`-scenario (Yperse Werkplaats BV + Spinnerij/Weverij/Confectie) doorlopend:

- Directe arbeidskost: **€ 25/uur** (per opdracht, inclusief lasten in standaard)
- Kostencentrum-budget Confectie: **€ 250.000** (kwartaal) of **€ 950.000** (jaar)
- Vaste kosten total: **€ 800.000/jaar** (voor break-even)
- Contributiemarge tapijt: verkoopprijs **€ 60** − variabele kost **€ 13** = **€ 47**
- Break-even-volume: **17.022 tapijten**
- Naaimachine-aankoop: **€ 280.000** (10 jaar lineair = € 28.000/jaar afschrijving)
- Wol-prijs: € 4,50–5,30/kg (plausibele range)
- Werknemer bruto: € 2.800/maand → totaal kost werkgever ± **€ 3.976**

Geen abstracte getallen (`320`, `80`, etc.) in voorbeelden.

---

## Open observaties / follow-ups

1. **PO 1.1 voorraadboekhouding** zou de records `voorraadwaardering` en `materiaalkosten` (boekingstechniek) moeten dupliceren of incorporeren — coördinatie nodig wanneer PO 1.1 wordt geëxtraheerd.
2. **`algemene-boekhouding`-stub** moet worden uitgewerkt in PO 1.1; hier alleen als anchor voor cross-references.
3. **ABC-methode** mist Belgische trusted bron — als gewenst kan een `_bron_voorstellen.json`-entry worden toegevoegd voor een ITAA-publicatie of erkende vakliteratuur (bv. Drury 'Management and Cost Accounting'). Niet gedaan in deze run; vakdoctrine-status volstaat voor extractie.
4. **Budgetbeheer + alarmbelprocedure** raakvlak: in `budgetbeheer.in_praktijk` wordt verwezen naar WVV art. 7:228 / 5:153. Een wikilink naar een `alarmbelprocedure`-record (PO 1.2?) zou waardevol zijn.
5. **`prijsverschil-arbeid`** is een variant op `verschillenboekhouding` voor arbeid; eventueel mergen in toekomst (één record met aparte secties materiaal/arbeid).
6. **`registratiesysteem-eenvoudige-integratie` / `proportionele-integratie`** zijn extrapolaties van CBN 3/3 (joint-venture-context) naar analytische boekhouding. Vakdoctrine-correcte interpretatie, maar de exacte CBN-tekst spreekt over tijdelijke verenigingen, niet over analytische registratiesystemen. Heroverwegen bij PO 1.7-context als daar joint-venture-specifieke records komen.

---

## Status

- **Output-locatie**: `/Users/stivni/Documents/ITAA/certificaid/data/concepten/records/` (44 nieuwe JSON-bestanden, alle valid)
- **Eindrapport**: dit bestand
- **`status: "seed"`** op alle records — wacht op review (`reviewed_by: null`)
- **Geen commit** — workflow eindigt hier
