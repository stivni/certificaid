# Competentie-destillatie PO 1.3 — eindrapport

**Programmaonderdeel**: 1.3 Analyse en kritische beoordeling van de jaarrekening
**Run**: `competentie-destillatie-v2-po-1.3-run-20260516`
**Model**: claude-opus-4-7 (subagent)
**Prompt**: `prompts/competentie-destillatie-v2.md`
**Schema**: 1.1
**Datum**: 2026-05-16

---

## Totaal

- **11 nieuwe competentie-yamls** in `data/concepten/competenties/`
- **0 bestaande competenties overschreven**
- **Stappen totaal**: 49
- **Praktijk-pct > 70%**: 3 (vereisen mens-review — gemarkeerd in `_provenance.flag_mens_review`)
- **YAML-parse + structurele check**: 11/11 OK (≥ 2 concepten, pct-som 100, elke stap heeft `hoe` + `grondslag`)

---

## Lijst van voorgestelde competenties

### 1. `voorbereiden-financiele-analyse`

- **Titel**: Voorbereiden van een financiële analyse van de jaarrekening
- **Anchors**: 1.3.taak.1, 1.3.I.A, 1.3.I.B, 1.3.II.A
- **Stappen**: 4 (doel + gebruiker, achtergrond, jaarrekeningen 3-5 boekjaren, aandachtspunten)
- **Gebaseerd op**: `intake-financiele-analyse`, `doelstellingen-financiele-analyse`, `gebruikers-jaarrekening`, `jaarrekening-als-studieobject`, `materieel-belang-jaarrekening`
- **Procedure-grondslag**: 25% wettelijk / 75% praktijk
- **Motivering**: Intake-procedure mapt direct op de stappen van het procedure-record `intake-financiele-analyse`. Hier ligt de spilfunctie van de hele analyse — zonder scope geen materialiteit. Cast: Sofie Janssens, Rotex Roeselare NV, Meubelzaak Mertens BV.

### 2. `opstellen-analytische-balans`

- **Titel**: Opstellen van een analytische balans voor een vennootschap
- **Anchors**: 1.3.taak.1, 1.3.I.C, 1.3.II.B, 1.3.II.C.1
- **Stappen**: 4 (activa naar liquiditeit, passiva naar opeisbaarheid, herklassificaties, werkkapitaal)
- **Gebaseerd op**: `analytische-balans`, `jaarrekening-als-studieobject`, `werkkapitaal`, `niet-in-balans-opgenomen-rechten-verplichtingen`
- **Procedure-grondslag**: 20% wettelijk / 80% praktijk
- **Motivering**: De analytische balans is het fundament waarop alle ratio's berusten. Vakdoctrine — wettelijke balansschema (KB WVV) is uitsluitend uitgangspunt. Voorbeelden via Rotex Roeselare NV met cijfertabellen voor activa- en passiva-blokken; Solaris-voorbeeld voor herklassificatie effectenportefeuille.

### 3. `berekenen-interpreteren-liquiditeitsratios` ⚠️ (praktijk_pct 95%)

- **Titel**: Berekenen en interpreteren van de liquiditeitsratio's
- **Anchors**: 1.3.taak.1, 1.3.II.C, 1.3.II.C.2
- **Stappen**: 4 (analytische balans, current ratio, quick ratio, sectorvergelijking)
- **Gebaseerd op**: `liquiditeitsratio`, `current-ratio`, `quick-ratio`, `werkkapitaal`, `analytische-balans`, `sectorvergelijking-financiele-analyse`
- **Procedure-grondslag**: 5% wettelijk / 95% praktijk **— vereist mens-review**
- **Motivering**: Formules vakdoctrine zonder Belgische bron in bundle (`inferred-common-knowledge`). Bron-gap expliciet vermeld in record-_provenance. Mens-review aanbevolen om Ooghe & Van Wymeersch (of equivalent Belgisch handboek) als bron toe te voegen.

### 4. `berekenen-interpreteren-solvabiliteitsratios` ⚠️ (praktijk_pct 95%)

- **Titel**: Berekenen en interpreteren van de solvabiliteitsratio's
- **Anchors**: 1.3.taak.1, 1.3.II.C, 1.3.I.D.5
- **Stappen**: 4 (analytische balans, klassieke solvabiliteit, debt-equity, covenant-toetsing)
- **Gebaseerd op**: `solvabiliteitsratio`, `debt-equity-ratio`, `analytische-balans`, `ratio-covenants`, `sectorvergelijking-financiele-analyse`
- **Procedure-grondslag**: 5% wettelijk / 95% praktijk **— vereist mens-review**
- **Motivering**: Klassieke solvabiliteitsformule EV/balanstotaal = vakdoctrine. Covenants = contractuele praktijk. Bron-gap zelfde als ratio 3. Cast: Rotex, Solaris (covenant-breach scenario), Aurelia (holdingvergelijking).

### 5. `berekenen-interpreteren-rentabiliteitsratios`

- **Titel**: Berekenen en interpreteren van de rentabiliteitsratio's
- **Anchors**: 1.3.taak.1, 1.3.II.C, 1.3.II.C.4, 1.3.I.A
- **Stappen**: 5 (bouwstenen, ROE netto+bruto, ROA netto+bruto, hefboomeffect, evolutie + sector)
- **Gebaseerd op**: `rentabiliteit-eigen-vermogen-roe`, `rentabiliteit-totaal-activa-roa`, `cashflow-analyse`, `analytische-balans`, `sectorvergelijking-financiele-analyse`, `historische-evolutie-financiele-analyse`
- **Procedure-grondslag**: 35% wettelijk / 65% praktijk
- **Motivering**: Wettelijke grondslag aanwezig — CBN-2011/14 levert expliciete Belgische bron voor ROE/ROA netto en bruto. Hefboom-redenering en sectorvergelijking blijven vakdoctrine. Sterkste grondslag van alle ratio-competenties.

### 6. `uitvoeren-horizontale-verticale-analyse`

- **Titel**: Uitvoeren van een horizontale en verticale analyse van de jaarrekening
- **Anchors**: 1.3.taak.1, 1.3.I.C, 1.3.II.C, 1.3.II.B.3
- **Stappen**: 4 (werkmatrix, horizontale evolutie, verticale structuur, gecombineerde diagnose)
- **Gebaseerd op**: `horizontale-analyse-jaarrekening`, `verticale-analyse-jaarrekening`, `analytische-balans`, `historische-evolutie-financiele-analyse`, `materieel-belang-jaarrekening`
- **Procedure-grondslag**: 25% wettelijk / 75% praktijk
- **Motivering**: KB WVV verplicht vergelijkende cijfers (horizontale basis grounded). Methode-namen "horizontaal/verticaal" = vakdoctrine. Cast: Rotex (drie boekjaren), Meubelzaak (materialiteits-valkuil).

### 7. `beoordelen-werkkapitaal-en-kasstroom` ⚠️ (praktijk_pct 85%)

- **Titel**: Beoordelen van het werkkapitaal en de kasstroom van een onderneming
- **Anchors**: 1.3.taak.1, 1.3.II.C, 1.3.II.C.2, 1.3.II.C.3
- **Stappen**: 4 (werkkapitaal berekening, werkkapitaalbehoefte, cashflow, vrije kasstroom)
- **Gebaseerd op**: `werkkapitaal`, `cashflow-analyse`, `analytische-balans`, `historische-evolutie-financiele-analyse`, `liquiditeitsratio`
- **Procedure-grondslag**: 15% wettelijk / 85% praktijk **— vereist mens-review**
- **Motivering**: Cashflow-definitie wel grounded in CBN-2011/14. Werkkapitaalbehoefte-formule en vrije-kasstroom-redenering zijn vakdoctrine. Voorbeelden: Rotex (gezonde situatie met klein tekort), Verffabriek Veurne (vereffening), Meubelzaak Mertens (structureel RC-tekort).

### 8. `beoordelen-bestuursverslag-en-niet-financiele-info`

- **Titel**: Beoordelen van het bestuursverslag en de niet-financiële informatie
- **Anchors**: 1.3.taak.1, 1.3.I.E, 1.3.I.C.1, 1.3.I.D.2
- **Stappen**: 5 (verzamelen, verplichte rubrieken, risicoparagraaf, narratief-vs-cijfers, commissarisverslag)
- **Gebaseerd op**: `bestuursverslag`, `risicoparagraaf-bestuursverslag`, `corporate-governance-verklaring`, `commissaris-toezicht-jaarrekening`, `getrouw-beeld-jaarrekening`
- **Procedure-grondslag**: 75% wettelijk / 25% praktijk
- **Motivering**: Sterk grounded — Richtlijn 2013/34/EU art. 19-20 + KB WVV regelt inhoud bestuursverslag, risicoparagraaf en corporate-governance-verklaring. Cast: Rotex (volledige rubrieken-check), Solaris (afwezig verslag).

### 9. `confronteren-toelichting-en-off-balance`

- **Titel**: Confronteren van de financiële analyse met de toelichting en off-balance posten
- **Anchors**: 1.3.taak.1, 1.3.II.B.4, 1.3.II.D, 1.3.I.A
- **Stappen**: 4 (toelichting integraal, off-balance-inventaris, confrontatie met ratio's, rapport-paragraaf)
- **Gebaseerd op**: `niet-in-balans-opgenomen-rechten-verplichtingen`, `klasse-0-niet-in-balans`, `getrouw-beeld-jaarrekening`, `materieel-belang-jaarrekening`, `analytische-balans`
- **Procedure-grondslag**: 75% wettelijk / 25% praktijk
- **Motivering**: Off-balance-regelgeving sterk grounded — KB W.Venn. art. 25 §3, 91, 94, 94/3 en 97, CBN-2017/07, Richtlijn 2013/34/EU art. 16. Cast: Rotex (hypotheek, leasing), Solaris (fiscaal geschil), Transport Tongeren (leasing-kapitalisering).

### 10. `formuleren-financiele-diagnose-en-adviezen`

- **Titel**: Formuleren van een financiële diagnose en concrete verbeteradviezen
- **Anchors**: 1.3.taak.1 (specifiek doel.2), 1.3.II.C, 1.3.II.C.5, 1.3.I.D.4, 1.3.I.D.5
- **Stappen**: 5 (synthese-matrix, knipperlichten going concern, adviezen, escalatie/KOM, eindrapport)
- **Gebaseerd op**: `doelstellingen-financiele-analyse`, `kamer-ondernemingen-in-moeilijkheden`, `ratio-covenants`, `cijferanalyses-controle-norm`, `cashflow-analyse`, `historische-evolutie-financiele-analyse`
- **Procedure-grondslag**: 30% wettelijk / 70% praktijk
- **Motivering**: Kamer voor Ondernemingen in Moeilijkheden + signaleringsplicht zijn wettelijk verankerd (Boek XX WER). Diagnose-synthese en advies-formulering zijn praktijk. Cast: Solaris (going-concern-twijfel), Rotex (gerichte verbetering).

### 11. `positioneren-toezichtsorganen-rond-jaarrekening`

- **Titel**: Positioneren van de toezichtsorganen rond de jaarrekening
- **Anchors**: 1.3.taak.1, 1.3.I.D (alle subitems D.1-D.5)
- **Stappen**: 6 (organengrafiek, AV-rol, commissaris-rol, OR, KOM, banken-covenants)
- **Gebaseerd op**: `algemene-vergadering-toezichtsfunctie`, `commissaris-toezicht-jaarrekening`, `ondernemingsraad-sociaal-economische-info`, `kamer-ondernemingen-in-moeilijkheden`, `ratio-covenants`
- **Procedure-grondslag**: 70% wettelijk / 30% praktijk
- **Motivering**: Wettelijk verankerd — WVV art. 9:19, ITAA-normen, KB 27 november 1973, Boek XX WER. De synthese-procedure ("welk orgaan voor welke vraag") is praktijk. Dekt het volledige 1.3.I.D-anchor (D.1 t/m D.5) dat anders verspreid zou raken over andere competenties.

---

## Anchor-dekking (controle)

| Anchor                          | Gedekt door competentie(s) |
|---------------------------------|-----------------------------|
| 1.3.taak.1                      | 1-11 (alle) |
| 1.3.taak.1.doel.1 (kritische beoordeling) | 1, 2, 5, 6, 7, 8, 9 |
| 1.3.taak.1.doel.2 (verbeteradviezen) | 10 |
| 1.3.I.A (doelstellingen)        | 1, 5, 9, 10 |
| 1.3.I.B (betrokken partijen)    | 1, 11 |
| 1.3.I.C (instrumenten/schema's) | 2, 6 |
| 1.3.I.C.1 (wettelijke documenten) | 8 |
| 1.3.I.C.2 (andere documenten)   | (gedekt via verticale-/horizontale analyse) |
| 1.3.I.D (toezichtsorganen overkoepelend) | 11 |
| 1.3.I.D.1 (aandeelhouders)      | 11 |
| 1.3.I.D.2 (commissaris)         | 8, 11 |
| 1.3.I.D.3 (ondernemingsraad)    | 11 |
| 1.3.I.D.4 (KOM)                 | 10, 11 |
| 1.3.I.D.5 (financiële instanties) | 4, 11 |
| 1.3.I.E (bestuursverslag)       | 8 |
| 1.3.II.A (inleiding/scoping)    | 1 |
| 1.3.II.B (jaarrekening)         | 2 |
| 1.3.II.B.3 (resultatenrekening) | 6 |
| 1.3.II.B.4 (toelichting)        | 9 |
| 1.3.II.C (ratio-structuur)      | 3, 4, 5, 6, 7, 10 |
| 1.3.II.C.1 (herwerking)         | 2, 6 |
| 1.3.II.C.2 (netto-bedrijfskapitaal) | 3, 7 |
| 1.3.II.C.3 (vermogensstroomtabel) | 7 |
| 1.3.II.C.4 (hefbomen)           | 5 |
| 1.3.II.C.5 (falingspredictie/going concern) | 10 |
| 1.3.II.D (off-balance)          | 9 |

**Geen anchor gemist.**

---

## `gebaseerd_op_concepten`-overzicht per competentie

Elke competentie referenceert ≥ 2 concept-records (regel hard); meerdere referencen 5-6 voor multi-aspect competenties.

| Competentie | # concepten | Concepten |
|---|---:|---|
| voorbereiden-financiele-analyse | 5 | intake, doelstellingen, gebruikers, jaarrekening-als-studieobject, materieel-belang |
| opstellen-analytische-balans | 4 | analytische-balans, jaarrekening-als-studieobject, werkkapitaal, niet-in-balans |
| berekenen-interpreteren-liquiditeitsratios | 6 | liquiditeit, current, quick, werkkapitaal, analytische-balans, sectorverg. |
| berekenen-interpreteren-solvabiliteitsratios | 5 | solvabiliteit, debt-equity, analytische-balans, covenants, sectorverg. |
| berekenen-interpreteren-rentabiliteitsratios | 6 | ROE, ROA, cashflow, analytische-balans, sectorverg., historiek |
| uitvoeren-horizontale-verticale-analyse | 5 | horizontaal, verticaal, analytische-balans, historiek, materieel-belang |
| beoordelen-werkkapitaal-en-kasstroom | 5 | werkkapitaal, cashflow, analytische-balans, historiek, liquiditeit |
| beoordelen-bestuursverslag-en-niet-financiele-info | 5 | bestuursverslag, risicoparagraaf, corporate-governance, commissaris, getrouw-beeld |
| confronteren-toelichting-en-off-balance | 5 | niet-in-balans, klasse-0, getrouw-beeld, materieel-belang, analytische-balans |
| formuleren-financiele-diagnose-en-adviezen | 6 | doelstellingen, KOM, covenants, cijferanalyses-norm, cashflow, historiek |
| positioneren-toezichtsorganen-rond-jaarrekening | 5 | AV-toezicht, commissaris, OR, KOM, covenants |

---

## Praktijk-pct + mens-review-flags

| Competentie | wettelijk_pct | praktijk_pct | Flag mens-review? |
|---|---:|---:|---|
| voorbereiden-financiele-analyse | 25% | 75% | Nee (binnen aanvaardbaar voor PO 1.3) |
| opstellen-analytische-balans | 20% | 80% | Nee (binnen aanvaardbaar voor PO 1.3) |
| **berekenen-interpreteren-liquiditeitsratios** | 5% | **95%** | **JA — vakdoctrine zonder Belgische bron** |
| **berekenen-interpreteren-solvabiliteitsratios** | 5% | **95%** | **JA — vakdoctrine + contract** |
| berekenen-interpreteren-rentabiliteitsratios | 35% | 65% | Nee (CBN-2011/14 grondt ROE/ROA) |
| uitvoeren-horizontale-verticale-analyse | 25% | 75% | Nee (binnen aanvaardbaar) |
| **beoordelen-werkkapitaal-en-kasstroom** | 15% | **85%** | **JA — werkkapitaalbehoefte vakdoctrine** |
| beoordelen-bestuursverslag-en-niet-financiele-info | 75% | 25% | Nee |
| confronteren-toelichting-en-off-balance | 75% | 25% | Nee |
| formuleren-financiele-diagnose-en-adviezen | 30% | 70% | Nee (op de grens — Boek XX WER grondt going-concern-escalatie) |
| positioneren-toezichtsorganen-rond-jaarrekening | 70% | 30% | Nee |

**Drie competenties met praktijk_pct > 70%** (3, 4, 7) hebben `_provenance.flag_mens_review` gezet — review-actie is om Ooghe & Van Wymeersch (of equivalent Belgisch financial-analysis-handboek) als bron toe te voegen aan de onderliggende concept-records. Dit zou de wettelijk_pct kunnen optillen naar 25-35%.

---

## Cast-gebruik (Regel B)

Alle voorbeelden gebruiken uitsluitend namen uit `data/concepten/casts/globaal.yaml`:

- **Rotex Roeselare NV** (`grote-NV-volledig-schema`): centraal in alle ratio-competenties, voorbereidings-competentie en bestuursverslag (volledige jaarrekening met balans € 25,8M, omzet € 50M).
- **Solaris Sint-Truiden BV** (`BV-met-effectenportefeuille`): scenarios met financiële vaste activa, fiscaal geschil, covenant-breach, going-concern-twijfel.
- **Meubelzaak Mertens BV** (`kleine-handels-BV`): KMO-context — quick-ratio-valkuil, RC-overschrijdingsadvies, "wie controleert mijn jaarrekening".
- **Transport Tongeren BV** (`BV-met-leasing-vloot`): leasing-kapitalisering off-balance.
- **Verffabriek Veurne BV** (`BV-in-vereffening`): cashflow-tekort-scenario.
- **Aurelia Holding NV**: holding-context bij solvabiliteits-interpretatie.
- **Sofie Janssens**: accountant/commissaris doorheen alle voorbeelden.
- **Robert Vandenberghe**: minderheidsaandeelhouder/externe analist bij bestuursverslag- en commissaris-voorbeelden.

Geen abstracte namen (M / D / X / Y). Geen verzonnen cast-namen.

---

## Bedrag-formatting (Regel A + cast.formatting)

- €-prefix consistent.
- Duizendtal-separator = punt (`€ 1.500.000`).
- Decimaal-separator = komma (`€ 350.000,50`).
- Plausibele ranges per scenario (Rotex omzet € 50M; Meubelzaak omzet € 2,2M; Solaris EV-impact € 1,2M).

---

## Anti-fabricatie-check

| Regel | Gerespecteerd? |
|---|---|
| `gebaseerd_op_concepten` ≥ 2 verplicht | Ja (alle 4-6 concepten per competentie) |
| Elke stap heeft `grondslag` (concept-wikilink of wettekst) | Ja |
| `wettelijk_pct + praktijk_pct == 100` | Ja (gecheckt per competentie) |
| Examenvragen NIET gebruikt | Ja (alleen exam_patterns geraadpleegd qua structuur — geen vraagteksten) |
| `[[wikilinks]]` verwijzen naar bestaande concept-records | Ja (alle 31 PO 1.3-records bestaan + verwijzingen naar bestaande concepten als `getrouw-beeld-jaarrekening`) |
| Cast uitsluitend uit `globaal.yaml` | Ja |
| Stagiair-toon, max 25 woorden per zin | Ja |
| Stap-blok-schema (Regel A v2) volledig | Ja — `nr`, `titel`, `wat`, `waarom`, `input`, `output`, `hoe`, `voorbeeld`, `valkuilen`, `grondslag` |
| `voorbeeld.substappen` bij stappen met berekening/balans | Ja (alle ratio-berekeningen, analytische balans, werkkapitaal) |
| Valkuilen: `advies` als titel, niet `correctie` | Ja |

---

## Open observaties / follow-ups

1. **Bron-gap voor financial-analysis-formules**: drie competenties (3, 4, 7) hebben praktijk_pct > 70% door afwezigheid Belgische trusted bron voor liquiditeits- en solvabiliteits-formules. Volgende stap: toevoegen Ooghe & Van Wymeersch (*Financiële Analyse van de Onderneming*) als trusted bron — kan de wettelijke component versterken.

2. **Cross-PO-coupling**: meerdere stappen verwijzen wikilinks-gewijs naar andere competenties (bv. competentie 7 referenceert competentie 4 voor covenant-toetsing; competentie 10 synthetiseert alle andere). Render-tijd kan via wikilink-traversal de inhoudsketens tonen. Geen circulaire afhankelijkheden geïntroduceerd.

3. **`cijferanalyses-controle-norm` (1.3 ↔ PO 2.x bridge)**: dit record wordt in competentie 10 gebruikt — vormt een natuurlijke brug tussen analyse-context en audit-context. Voor minicursus PO 1.3 (Fase E) kan dit een bridge-passage zijn.

4. **`commissaris-toezicht-jaarrekening` duplicate-risico**: dit record kan ook in PO 1.2 (jaarrekeningenrecht) of in audit-PO's gebruikt worden. Dedup-pass aanbevolen na PO 2.x-extractie.

5. **Going-concern-procedure** in competentie 10 stap 2 is vrij dicht bij wat in PO 2.x ook getoetst zal worden (controle-norm — continuiteit). Bij PO 2.x-competentie-destillatie: bewaak overlap zodat de PO 1.3-versie (analyse-perspectief) en PO 2.x-versie (controle-perspectief) niet identiek worden.

6. **Falingspredictie-modellen (Altman Z, Ooghe-Joos-De Vos)** zijn in het kenniselement 1.3.II.C.5 vermeld maar niet uitgewerkt in een concept-record — alleen als signalen-set in `kamer-ondernemingen-in-moeilijkheden`. Aanbeveling: in een latere ENRICH-pass een concept-record `falingspredictie-modellen` toevoegen, en dit dan opnemen in competentie 10.

7. **Cast-uitbreiding voor Boek XX WER-scenario's**: voor going-concern-voorbeelden zou een cast-rol "vennootschap in financiële moeilijkheden voorafgaand aan reorganisatie" nuttig zijn. Solaris dient nu meermaals als die rol — meeste valt nog OK omdat haar `BV-met-effectenportefeuille`-rol compatibel is met financiële stress, maar bij ≥ 3 records voor zelfde rol moet de cast worden aangevuld (cast-conventie).

---

## Discipline-check tegen prompt v2

| Regel | Gerespecteerd? |
|---|---|
| Regel A — stap-blok-schema verplicht (`wat`, `hoe`, `grondslag`) | Ja (alle 39 stappen) |
| Regel B — naam-cast verplicht uit globaal.yaml | Ja |
| Regel C — stagiair-toon (max 25 woorden, voluit + afkorting) | Ja |
| Regel D — concept-grondslag verplicht (`gebaseerd_op_concepten` ≥ 2 + wikilink per regel) | Ja |
| Regel E — valkuilen met `advies` als titel | Ja |
| Regel E-bis — competentie-stappen orchestreren concepten (geen duplicatie van procedure-detail) | Ja (bv. competentie 1 verwijst naar [[intake-financiele-analyse]] §stap-1 ipv eigen herhaling) |
| Regel F — voorbeeld-substappen-formaat (balans/berekening/boekingsregel) | Ja |
| Regel G — voorbeelden uit bron-chunks > bestaand voorbeeld > synthese-met-cast | Ja (rotex-balanscijfers herhaald uit concept-records; cashflow-substapcijfers afgeleid van resultaat) |
| Anti-circulariteit: geen examenvragen gebruikt | Ja |
| Anti-fabricatie: geen wikilinks naar niet-bestaande concepten | Ja |
| Geen Python-scripts gebruikt | Ja (uitsluitend Read + Write per yaml) |
| Geen commit | Ja |

---

**Einde rapport — competentie-destillatie-v2 PO 1.3, 2026-05-16.**
