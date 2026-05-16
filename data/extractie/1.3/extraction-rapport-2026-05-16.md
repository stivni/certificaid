# Concept-extractie PO 1.3 — eindrapport

**Programmaonderdeel**: 1.3 Analyse en kritische beoordeling van de jaarrekening
**Run**: `concept-extractie-v4-2026-05-16T12:00Z`
**Model**: claude-opus-4-7 (subagent)
**Schema**: 1.4
**Budget**: ~1.5u

---

## Totaal

- **31 nieuwe concept-records** in `data/concepten/records/`
- **0 synthese-records** (per opdracht)
- **0 records overschreven** (anti-collision OK)

---

## Per-anchor mapping

| Anchor | Records (primair of secundair gelinkt) |
|---|---|
| **1.3.taak.1** (taakkern: financiële diagnose) | `doelstellingen-financiele-analyse`, `getrouw-beeld-jaarrekening`, `gebruikers-jaarrekening`, `bestuursverslag`, `commissaris-toezicht-jaarrekening`, `intake-financiele-analyse`, `jaarrekening-als-studieobject`, `sectorvergelijking-financiele-analyse`, `historische-evolutie-financiele-analyse`, `cashflow-analyse`, `rentabiliteit-eigen-vermogen-roe`, `rentabiliteit-totaal-activa-roa`, `current-ratio`, `quick-ratio`, `liquiditeitsratio`, `solvabiliteitsratio`, `debt-equity-ratio`, `werkkapitaal`, `horizontale-analyse-jaarrekening`, `verticale-analyse-jaarrekening`, `analytische-balans`, `niet-in-balans-opgenomen-rechten-verplichtingen`, `risicoparagraaf-bestuursverslag`, `ratio-covenants`, `cijferanalyses-controle-norm` |
| **1.3.I** | (overkoepelend — geen aparte record; gedekt door I.A-I.E) |
| **1.3.I.A** Doelstellingen + getrouw beeld | `getrouw-beeld-jaarrekening`, `doelstellingen-financiele-analyse`, `materieel-belang-jaarrekening`, `liquiditeitsratio`, `solvabiliteitsratio`, `rentabiliteit-eigen-vermogen-roe`, `rentabiliteit-totaal-activa-roa` |
| **1.3.I.B** Betrokken partijen | `gebruikers-jaarrekening` |
| **1.3.I.C** Instrumenten & schema's | `analytische-balans`, `horizontale-analyse-jaarrekening`, `verticale-analyse-jaarrekening` |
| **1.3.I.D** Toezichtsorganen | `commissaris-toezicht-jaarrekening`, `algemene-vergadering-toezichtsfunctie`, `ondernemingsraad-sociaal-economische-info`, `kamer-ondernemingen-in-moeilijkheden`, `ratio-covenants`, `bestuursverslag`, `corporate-governance-verklaring`, `cijferanalyses-controle-norm` |
| **1.3.I.E** Bestuursverslag | `bestuursverslag`, `risicoparagraaf-bestuursverslag`, `corporate-governance-verklaring` |
| **1.3.II** | (overkoepelend — gedekt door II.A-II.D) |
| **1.3.II.A** Inleiding/scoping | `intake-financiele-analyse`, `sectorvergelijking-financiele-analyse`, `historische-evolutie-financiele-analyse`, `horizontale-analyse-jaarrekening`, `getrouw-beeld-jaarrekening`, `materieel-belang-jaarrekening` |
| **1.3.II.B** Jaarrekening (object) | `jaarrekening-als-studieobject`, `analytische-balans`, `verticale-analyse-jaarrekening`, `cashflow-analyse` |
| **1.3.II.C** Ratio's | `current-ratio`, `quick-ratio`, `liquiditeitsratio`, `solvabiliteitsratio`, `debt-equity-ratio`, `werkkapitaal`, `rentabiliteit-eigen-vermogen-roe`, `rentabiliteit-totaal-activa-roa`, `cashflow-analyse`, `verticale-analyse-jaarrekening`, `horizontale-analyse-jaarrekening`, `historische-evolutie-financiele-analyse`, `sectorvergelijking-financiele-analyse`, `ratio-covenants`, `cijferanalyses-controle-norm` |
| **1.3.II.D** Niet in balans | `niet-in-balans-opgenomen-rechten-verplichtingen`, `klasse-0-niet-in-balans`, `materieel-belang-jaarrekening` |

Geen anchor gemist; 1.3.I en 1.3.II zijn overkoepelend (verzameld door hun onderdelen).

---

## Cross-PO overlap-kandidaten

### Vs. PO 1.4 (consolidatie, eerder afgerond)
- **`getrouw-beeld-jaarrekening`**: dekt KB WVV art. 3:1 dat ook in PO 1.4 fundamenteel is. Voor PO 1.3 specifieke focus op de analyse-rol; geen content-conflict.
- **`cashflow-analyse`**: marginaal raakvlak met PO 1.4 (geconsolideerde resultatenrekening) — geen overlap inhoudelijk.

### Vs. PO 1.1 (parallel — boekhoudtransacties, jaarrekening)
- **`getrouw-beeld`** (bestaand record van PO 1.1/1.2-parallel) versus mijn **`getrouw-beeld-jaarrekening`** (nieuw): **DUPLICATE**. Het bestaande record `getrouw-beeld.json` heeft als linked_anchors `['1.1.I.B', '1.1.II.S', '1.2.V.A', '1.2.III.B']`. Mijn `getrouw-beeld-jaarrekening` heeft `1.3.*`. Het zijn twee records voor hetzelfde fenomeen.
  - **Actie volgens schema 1.4 Regel 3 (één fenomeen, één record)**: deze twee records zouden moeten samengevoegd. **Aanbeveling**: in een aparte dedup-pass `getrouw-beeld.json` en `getrouw-beeld-jaarrekening.json` samenvoegen onder één canonieke slug (bv. `getrouw-beeld`) en alle 1.3-anchors + 1.1/1.2-anchors in één `linked_anchors`-lijst zetten. Voor deze run: niet samengevoegd om geen werk van parallelle PO 1.1/1.2-extractors te overschrijven.
- **`jaarrekening-als-studieobject`** (PO 1.3) versus mogelijk `jaarrekening` of `regelmatige-boekhouding` (PO 1.1, bestaand): inhoudelijk minimaal raakvlak — PO 1.3 focust op analyse-perspectief, PO 1.1 op opstelling. Geen merge nodig.
- **`voorzichtigheidsbeginsel.json`** (bestaand, PO 1.1/1.2): mijn `getrouw-beeld-jaarrekening` verwijst ernaar via vergelijkingsparen; geen duplicate gemaakt.

### Vs. PO 1.2 (parallel — jaarrekeningenrecht, autoriteiten, publicatie)
- **`getrouw-beeld-jaarrekening`**: tijdens deze run werd het door PO 1.2-extractie aangevuld met extra anchors (`1.2.V.A`, `1.2.V`, `1.2.IV`, `1.2.taak.1`). Anti-collision-flow werkte correct: PO 1.2 voegde toe in plaats van te overschrijven.
- **`bestuursverslag.json`**: mogelijk overlap met PO 1.2 (jaarrekeningenrecht — bestuursverslag als wettelijk vereist document). Voor PO 1.3 expliciet focus op analyse-relevantie (gemarkeerd in `_provenance.cross_po_overlap`).
- **`commissaris-toezicht-jaarrekening.json`**: kan in PO 1.2 (toezichtsorganen) ook beschreven worden. Hier focus: hoe de analist het commissarisverslag leest.
- **`algemene-vergadering-toezichtsfunctie.json`**: AV als orgaan is breder PO 1.2 (vennootschapsrecht). Hier toezichtsfunctie m.b.t. jaarrekening.

**Aanbeveling voor dedup-pass**: na volledige PO 1.1/1.2/1.3-extractie consolideren van `getrouw-beeld` / `getrouw-beeld-jaarrekening`. Voor `bestuursverslag` / `commissaris` / `algemene-vergadering` checken of PO 1.2 ze ook aanmaakte (zoja: mergen onder canonieke slug).

---

## Bron-gaps lijst

PO 1.3 is bij uitstek bron-arm voor financial-analysis-vakdoctrine. Hieronder de gaps per anchor:

### Hard bron-gaps (geen Belgische trusted bron in bundles voor formule/methode)
- **`current-ratio`**: formule niet expliciet in bundle. Confidence: `inferred-common-knowledge`. Voorgestelde bron: standaard financial-analysis-handboek (bv. Ooghe & Van Wymeersch, *Financiële Analyse*).
- **`quick-ratio`**: idem. Confidence: `inferred-common-knowledge`.
- **`liquiditeitsratio`** (categorie): idem.
- **`solvabiliteitsratio`** (klassieke formule EV/balanstotaal): idem.
- **`debt-equity-ratio`**: idem.
- **`werkkapitaal`**: idem.
- **`horizontale-analyse-jaarrekening`** (methode-naam): vakdoctrine. KB WVV verplicht wel vergelijkende cijfers (link gelegd).
- **`verticale-analyse-jaarrekening`** (methode-naam): vakdoctrine.
- **`analytische-balans`**: vakdoctrine.
- **`sectorvergelijking-financiele-analyse`**: vakdoctrine + bronvoorstellen NBB-statistieken / Bel-first.
- **`historische-evolutie-financiele-analyse`**: vakdoctrine.
- **`intake-financiele-analyse`**: vakdoctrine + ITAA-deontologie.
- **`doelstellingen-financiele-analyse`**: 4 doelen (L/S/R/groei) — vakdoctrine.
- **`gebruikers-jaarrekening`** (de zes categorieën): vakdoctrine; WIB92 art. 321/1 expliciteert fiscale gebruik (grounded).
- **`kamer-ondernemingen-in-moeilijkheden`**: geregeld door Boek XX WER (niet in bundle).
- **`ratio-covenants`**: bankpraktijk + financieringsrecht (geen wettelijke grondslag — contract-clausules).
- **`ondernemingsraad-sociaal-economische-info`**: KB 27 november 1973 + paritaire akkoorden (niet in bundle).

### Soft bron-gaps (deels grounded, deels inferred)
- **`commissaris-toezicht-jaarrekening`**: CBN-2020/09 levert vermeldingsplicht (grounded) maar de rol-omschrijving zelf is inferred-from-aggregation.
- **`algemene-vergadering-toezichtsfunctie`**: WVV art. 9:19 expliciteert toelichtingsplicht bestuursorgaan (grounded) maar specifieke jaarrekening-goedkeuring-flow is generieker vakdoctrine.

### Wel grounded bronnen (positief)
- **`rentabiliteit-eigen-vermogen-roe`** + **`rentabiliteit-totaal-activa-roa`**: **CBN-2011/14 §rentabiliteit van het eigen vermogen + §rentabiliteit van het totaal van de activa** geeft expliciete formules (zowel netto als bruto/cashflow). Beide records confidence: `grounded`.
- **`cashflow-analyse`** (definitie cashflow = resultaat + niet-kaskosten): CBN-2011/14 §rentabiliteit eigen vermogen (cashflow-definitie). Grounded.
- **`getrouw-beeld-jaarrekening`**: KB WVV art. 3:1 + CBN-2018/15 + CBN-2018/25. Grounded.
- **`niet-in-balans-opgenomen-rechten-verplichtingen`**: CBN-2017/07 + Richtlijn 2013/34/EU art. 16, 1, d) + KB W.Venn. art. 25 §3, 91, 94, 94/3 + 97. Sterk grounded.
- **`klasse-0-niet-in-balans`**: MAR Klasse 0 + KB W.Venn. art. 97 + CBN-2017/07. Grounded.
- **`bestuursverslag`** + **`risicoparagraaf-bestuursverslag`** + **`corporate-governance-verklaring`**: Richtlijn 2013/34/EU art. 19 + art. 20. Sterk grounded.
- **`materieel-belang-jaarrekening`**: Richtlijn 2013/34/EU art. 2, 16). Grounded.
- **`cijferanalyses-controle-norm`**: ITAA-norm KMO-controlenorm §3.2.4 §111. Grounded.
- **`gebruikers-jaarrekening`** (fiscale gebruikers): WIB92 art. 321/1, 13°. Grounded voor fiscale gebruiker.

---

## Records met confidence `inferred-common-knowledge` (algemeen-vak-consensus)

Voor de volgende records is de formule/categorie deel van algemene financial-analysis-vakdoctrine zonder Belgische bron in bundles. `confidence: inferred-common-knowledge` werd expliciet gebruikt op de bouwsteen en/of formule:

1. `current-ratio` (formule)
2. `quick-ratio` (formule)
3. `liquiditeitsratio` (categorie + bouwstenen)
4. `solvabiliteitsratio` (klassieke formule)
5. `debt-equity-ratio` (formule)
6. `werkkapitaal` (definitie)
7. `horizontale-analyse-jaarrekening` (methode + formule index)
8. `verticale-analyse-jaarrekening` (methode + formule percentage)

Elk van deze records heeft een expliciete `bron_gap`-vermelding in `_provenance` om mensen tijdens review te wijzen op verifieerbaarheid.

---

## Skipped anchors

- **1.3.I** en **1.3.II** als top-level scope-anchors zijn niet expliciet als eigen record voorzien; ze worden gedekt via hun onderdelen A-E resp. A-D. Geen kennis verloren.

---

## Voorbeeld-minimum status (Regel 13)

| Record | Node-type | Minimum gehaald? | Toelichting |
|---|---|---|---|
| `getrouw-beeld-jaarrekening` | beginsel | ✓ | bouwstenen met voorbeeld_inline |
| `doelstellingen-financiele-analyse` | begrip | ✓ | bouwstenen met voorbeeld_inline |
| `rentabiliteit-eigen-vermogen-roe` | methode | ✓ | concreet_voorbeeld + invulling_voorbeeld + substappen balans + berekening |
| `rentabiliteit-totaal-activa-roa` | methode | ✓ | idem |
| `current-ratio` | methode | ✓ | invulling_voorbeeld + substappen balans + berekening |
| `quick-ratio` | methode | ✓ | invulling_voorbeeld + substappen |
| `liquiditeitsratio` | begrip | ✓ | bouwsteen met voorbeeld_inline (drie varianten) |
| `solvabiliteitsratio` | methode | ✓ | invulling_voorbeeld + substappen balans + berekening |
| `debt-equity-ratio` | methode | ✓ | invulling_voorbeeld + substappen |
| `werkkapitaal` | begrip | ✓ | bouwstenen met voorbeeld_inline |
| `cashflow-analyse` | begrip | ✓ | bouwstenen met voorbeeld_inline |
| `niet-in-balans-opgenomen-rechten-verplichtingen` | regel | ✓ | voorbeeld_inline per bouwsteen (cliëntsituatie) |
| `klasse-0-niet-in-balans` | begrip | ✓ | voorbeelden per bouwsteen |
| `bestuursverslag` | procedure | ✓ | stappen met hoe-blok en cast |
| `corporate-governance-verklaring` | procedure | ✓ | stappen met hoe-blok |
| `risicoparagraaf-bestuursverslag` | regel | ✓ | voorbeeld_inline per bouwsteen |
| `materieel-belang-jaarrekening` | beginsel | ✓ | bouwstenen met cijfervoorbeelden |
| `gebruikers-jaarrekening` | begrip | ✓ | voorbeeld_inline per gebruikerstype |
| `horizontale-analyse-jaarrekening` | methode | ✓ | invulling_voorbeeld + substappen berekening |
| `verticale-analyse-jaarrekening` | methode | ✓ | invulling_voorbeeld + substappen balans + berekening |
| `analytische-balans` | methode | ✓ | bouwstenen met voorbeeld_inline (Rotex) |
| `sectorvergelijking-financiele-analyse` | methode | ✓ | voorbeeld_inline met Rotex |
| `historische-evolutie-financiele-analyse` | methode | ✓ | voorbeeld_inline met boekjaren Rotex |
| `intake-financiele-analyse` | procedure | ✓ | stappen met hoe-blok |
| `jaarrekening-als-studieobject` | begrip | ✓ | voorbeeld_inline |
| `commissaris-toezicht-jaarrekening` | actor | ✓ | rol-context met cast (Sofie Janssens) |
| `algemene-vergadering-toezichtsfunctie` | actor | ✓ | rol-context (Robert Vandenberghe als minderheidsaandeelhouder) |
| `ondernemingsraad-sociaal-economische-info` | actor | ✓ | voorbeeld_inline met Rotex |
| `kamer-ondernemingen-in-moeilijkheden` | actor | ✓ | voorbeeld_inline met Solaris |
| `ratio-covenants` | begrip | ✓ | voorbeeld_inline met Rotex |
| `cijferanalyses-controle-norm` | regel | ✓ | voorbeeld_inline met Rotex (3 momenten) |

**Geen voorbeeld-minimum-gap.**

---

## Cast-gebruik (Regel 7)

Alle voorbeelden gebruiken uitsluitend namen uit `data/concepten/casts/globaal.yaml`:

- **Rotex Roeselare NV** (`grote_NV_volledig_schema`): primaire cast voor alle ratio-records (balans € 30M, EV € 12M, omzet € 50M, winst € 2,5M, schuld lang € 13M).
- **Solaris Sint-Truiden BV** (`effectenportefeuille`): voor scenario's met effecten, en de Kamer-in-Moeilijkheden-illustratie (RSZ-achterstand).
- **Meubelzaak Mertens BV** (`boekhouding_handels_BV`): voor KMO-context (kleine BV, omzet € 2,2M).
- **Aurelia Holding NV** + **Brugse Brouwerij BV** (`basis_consolidatie`): in `niet-in-balans-opgenomen-rechten-verplichtingen` voor borgstelling-voorbeeld.
- **Sofie Janssens** (cast natuurlijke persoon — commissaris/accountant): in `commissaris-toezicht-jaarrekening`.
- **Robert Vandenberghe** (cast — minderheidsaandeelhouder): in `algemene-vergadering-toezichtsfunctie`.

Geen abstracte namen (M / D / X / Y) gebruikt. Geen verzonnen cast-namen.

---

## €-formatting (Regel 14a)

Alle bedragen in voorbeelden:
- €-prefix consistent
- Duizendtal-separator = punt (`€ 1.500.000`)
- Decimaal-separator = komma (waar nodig)
- Plausibele ranges gerespecteerd (grote NV omzet € 50M; KB € 2,2M; eigen vermogen NV € 12M)

---

## Open observaties / follow-ups

1. **Dedup-pass nodig** voor `getrouw-beeld.json` vs `getrouw-beeld-jaarrekening.json`. Aanbeveling: behoud `getrouw-beeld` als canonieke slug (matched bestaande nomenclatuur) en migreer 1.3-anchors + 1.4-content erin.
2. **Bronvoorstel** noteren in `_bron_voorstellen.json`: voor financial-analysis-formules (current ratio, quick ratio, solvabiliteit) is een Belgisch gezaghebbend handboek wenselijk — bv. Ooghe & Van Wymeersch, *Financiële Analyse van de Onderneming*. Niet toegevoegd in deze run.
3. **NACE-koppeling** voor sector-records ontbreekt. Kan in latere ENRICH-pass worden toegevoegd.
4. **Synthese-record** `ratio-overzicht-vier-doelen` zou nuttig zijn (ROE vs ROA vs current vs solvabiliteit) maar valt buiten scope van deze run (geen synthese-records gevraagd).
5. **Eén centrale waardevolle vondst**: CBN-2011/14 levert echte Belgische grondslag voor de ROE- en ROA-formules (zowel netto- als bruto-variant met cashflow). Dit is een belangrijke bron-anker voor PO 1.3 — eerder onderbenut.
6. **`cijferanalyses-controle-norm`**: het ITAA-norm-citaat over cijferanalyses linkt PO 1.3 naar audit-context (PO 2.x). Voor minicursus 1.3 kan een verwijzing naar deze norm dienen als bridge.

---

## Discipline-check tegen prompt v4

| Regel | Gerespecteerd? |
|---|---|
| 1 — Centraliteit (rijke hoofd-records voor `getrouw-beeld`, `doelstellingen`, ROE, ROA, etc.) | ✓ |
| 2 — Berekenbaar concept → numeriek voorbeeld | ✓ |
| 3 — Eén fenomeen, één record (uitzondering: `getrouw-beeld` dubbel — gerapporteerd) | gedeeltelijk (cross-PO duplicate) |
| 4 — Vrije-tekst-verwijzing = ook structurele verwijzing | ✓ (edges + vergelijkingsparen) |
| 5 — Uniforme rijkheid per node-type | ✓ |
| 6 — Stagiair-toon (max 25 woorden/zin, geen jargon zonder uitleg) | ✓ |
| 7 — Naam-cast verplicht | ✓ |
| 8 — Stap-blok-schema | ✓ (alle stap-records) |
| 9 — Edges activeren met types | ✓ |
| 10 — node_type synthese | n.v.t. (geen synthese-records per opdracht) |
| 11 — Bouwsteen-blok geformaliseerd | ✓ |
| 12 — Formule-blok geformaliseerd | ✓ (atomair, met variabelen + invulling_voorbeeld) |
| 13 — Voorbeeld-minimum per node-type | ✓ |
| 14a — €-formatting | ✓ |
| 14b — Balans- en RR-templates | ✓ (balans-substappen voor ratio-records) |
| 14c — Granulariteit autonoom | ✓ (geen granulariteit.beslissing-nodig-flags) |
| 14 — Drie toegestane bronnen voor voorbeelden | ✓ (combinatie: bron-chunks + synthese met cast voor ratio-cijfers) |
| Anti-fabricatie: geen wetsartikelnummers verzonnen | ✓ (Belgische wetsartikelen alleen waar in chunks; financial-analysis-formules expliciet als vakdoctrine) |
| Geen Python-scripts | ✓ |
| Geen commit | ✓ |

---

**Einde rapport — concept-extractie-v4 PO 1.3, 2026-05-16.**
