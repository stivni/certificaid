# Leerpad-skelet PO 1.9 — Financiële analyse en fundamentele principes van financieel bedrijfsbeheer

**Status**: v2 — 2026-05-31 (uitvoering loopt autonoom).

**Scope-besluit (sparring 2026-05-31)**: **1.3 = techniek, 1.9 = integratie + beheer + vooruitkijken** — twee pakketten met een duidelijke snijlijn. 1.3-agent werkt parallel aan zijn techniek-pakket; 1.9 wordt nu autonoom gebouwd met de 4 leerstukken die geen techniek-overlap hebben. Cross-PO-verwijzingen gebeuren via concept-records (definitorisch, slug-stabiel) i.p.v. leerstuk-slugs (in flux bij 1.3).

**Definitieve scope-snijlijn**:

| Onderwerp | Hoort bij | Notitie |
|---|---|---|
| Functionele balans + NBK/BBK/NT berekenen | **1.3** | Techniek; 1.9 verwijst naar concept `[[functionele-balans]]` |
| Vier ratio-families berekenen + interpreteren | **1.3** | Techniek; 1.9 verwijst naar `[[liquiditeits-ratios]]`, `[[solvabiliteits-ratios]]`, `[[rentabiliteits-ratios]]`, `[[activiteits-ratios]]`, `[[ratio-interpretatie]]` |
| Kasstroomoverzicht opstellen (IAS 7) + FCF berekenen | **1.3** | Techniek; 1.9 verwijst naar `[[kasstroom-analyse]]` + `[[free-cash-flow]]` |
| Werkkapitaal-**beleid** (BBK reduceren, financieringsmix, dividend-capaciteit) | **1.9** | Management-beslissingen |
| Kredietbeoordeling (DSCR, matching-principe, kasstroomprognose voor investering) | **1.9** | Integratie van techniek naar beslissing |
| Continuïteit + WVV 7:228 + CBN 2018/18 + 2021/14 + Z-score + ISA 570 | **1.9** | Juridisch-financieel snijvlak |
| Financiële diagnose-rapport opstellen (proces + rollen + aanbevelingen) | **1.9** | Eindproduct, het integratie-leerstuk |

**Werkstroom**: §3 hieronder is v2-leerstuk-voorstel (4 leerstukken). Uitvoering loopt autonoom door (voorbeeldgroep, scripts, render, minicursus, samenvatting, oefening) zonder verdere sparring. v1-voorstel in commit-historie bewaard als referentie.

---

## 1. Programma-analyse

### Officiële taken en doelstellingen

PO 1.9 heeft **één hoofdtaak** met **11 doelstellingen** en niveau `integratie` (hoogste niveau in het programma).

> **Taak 1.9.1**: Opstellen van de individuele en geconsolideerde jaarrekening

| Doel | Tekst (verkort) | Kern voor 1.9? |
|---|---|---|
| 1.9.1.1 | Financiële analyse als bron van informatie voor stakeholders (decisiekader) | Kern — meta-context |
| 1.9.1.2 | Lezen en begrijpen van relevante jaarrekeningen | Kern — entry |
| 1.9.1.3 | Consistentie en relevantie van gegevens waarborgen | Kern — methodologie |
| 1.9.1.4 | Contextualiseren van de omgeving van de onderneming | Kern — diagnose-laag |
| 1.9.1.5 | Een grondige financiële diagnose stellen | Kern — eindproduct |
| 1.9.1.6 | Problematiek vaststellen + aanbevelingen formuleren | Kern — eindproduct |
| 1.9.1.7 | Passende ratio's gebruiken naargelang de problematiek | Kern — techniek |
| 1.9.1.8 | Relevante informatie verzamelen + databanken gebruiken | Rakend — tools |
| 1.9.1.9 | Tools voor financiële analyse en beheer gebruiken | Rakend — tools |
| 1.9.1.10 | Financiële prognoses maken | Kern — vooruitkijken |
| 1.9.1.11 | Onderneming bijstaan in haar levensfasen (oprichting → vereffening) | Rakend — andere PO's |

### Cruciale observatie: titel ≠ doelstellingen (zelfde patroon als 1.4)

Net als bij PO 1.4 gaat de taaktekst over **opstellen** terwijl de doelstellingen volledig over **analyseren** gaan. De PO heet "Financiële analyse en fundamentele principes van financieel bedrijfsbeheer" — de 11 doelstellingen wijzen ondubbelzinnig naar analyse, diagnose, ratio-keuze, prognose. Geen enkele doelstelling vraagt om een jaarrekening te *maken*.

Conclusie: het pakket dekt **analyse + financieel beheer**. Opstellen van de individuele jaarrekening leeft in PO 1.1/1.2/1.4 (`individuele-jaarrekening-opmaken` cross-PO-leerstuk bestaat al).

### Kenniselementen (uit programma.json, niveau dieper)

- **1.9.I** — Inleiding tot financiële analyse (basisbegrippen, gebruikers, methoden)
- **1.9.II** — *zie programma.json voor de overige kenniselementen — typisch: functionele balans / werkkapitaal-drieluik / kasstroom-analyse / ratio-families / continuïteits-veronderstelling / faillissementspredictie / financiële diagnose*

### Kern vs rakend

- **Kern (financiële analyse + financieel beheer)**: 5 leerstukken die het volledige analyse-traject dekken van herstructurering → ratio's → kasstromen → continuïteit → integrale diagnose
- **Rakend**:
  - **PO 1.3** (Analyse van de jaarrekening) — sterk inhoudelijk raakvlak. Klassieke afbakening: 1.3 = techniek, 1.9 = integratie + beheer + voorspelling. Risico op dubbel werk; we beschouwen 1.9 als de "diagnose-stelt-aanbevelingen-voor"-laag bovenop 1.3
  - **PO 1.6** (Externe controle) — going-concern-toets ISA 570 → leerstuk `continuiteit-en-faillissementspredictie`
  - **PO 1.2 / 3.0** — alarmprocedure WVV 7:228, ondernemingsrechtbank-context → idem leerstuk
  - **PO 1.4** (Geconsolideerd) — analyse-technieken werken ook op geconsolideerde JR; opstellen ligt bij 1.4
  - **PO 1.8** (Management accounting) — interne (ex ante) ↔ externe (ex post) cijfers; budget-vs-realisatie raakt rentabiliteits-interpretatie

---

## 2. Voorbeeldexamen-patronen

Uit [voorbeeldexamens 2003-2019](../content/leerpaden/1-9/voorbeeldexamenvragen.md): **7 unieke vraag-eenheden** in 5 examens. Lichter bevraagd dan PO 1.6, maar de vragen die er zijn zijn **cijfer-intensief en case-georiënteerd** — niet enkel definities.

| Onderwerp | Voorkomens | Type vraag | Centraal in leerstuk |
|---|---|---|---|
| Werkkapitaal-drieluik — netto kas + permanent vermogen + DSO/DIO-stellingen | 2019-bibf | Begrip + multiple choice | `jaarrekening-lezen-en-herstructureren` |
| NBK verhogen — drie maatregelen | 2013-2 | Advies | `jaarrekening-lezen-en-herstructureren` |
| Definities financiële begrippen (intrinsieke waarde, fractiewaarde, ROA, schuldgraad, operationele CF) | 2013-1 | Theorie | `ratios-en-hun-interpretatie` + `kasstromen-en-financieringscapaciteit` |
| BBK — definitie + berekening + reductiemaatregelen | 2008-bibf | Begrip + advies | `jaarrekening-lezen-en-herstructureren` |
| Investeringskrediet-haalbaarheid (DSCR + annuïteit) | 2008-bibf | Cijfercase | `kasstromen-en-financieringscapaciteit` |
| Liquiditeit + solvabiliteit berekenen (current, acid test, solvabiliteit) | 2003-bibf | Cijfercase | `ratios-en-hun-interpretatie` |
| Operationele cash-flow berekenen (indirect, geen WK-correctie) | 2003-bibf | Cijfercase | `kasstromen-en-financieringscapaciteit` |
| Nulcouponobligatie | 2019-bibf | Begrip | Rakend — financiële techniek, niet kern-1.9 |

**Patroon**:
- **Werkkapitaal-drieluik domineert** (4 van 7 vragen raken NBK/BBK/NT)
- **Cashflow + DSCR** is examen-favoriet (3 vragen)
- **Ratio-berekening + interpretatie** klassiek (2 vragen, beide in cijfercase-vorm)
- **Continuïteit/diagnose** komt **niet** in voorbeeldexamens voor — maar het PO-niveau "integratie" suggereert dat dit in nieuwe ITAA-examens wel kan opduiken (vs oude BIBF-stijl). Voorzichtig dekken.
- BIBF-examens leunen sterk op definities; ITAA-niveau "integratie" zal eerder integrale diagnose-cases vragen — pakket moet **beide aankunnen**.

---

## 3. Leerstuk-voorstel v2 — 4 leerstukken onder integratie-scope

Onder de scope-snijlijn (§0) blijven 4 leerstukken in 1.9. Alles wat techniek is gaat naar 1.3. De 4 leerstukken hieronder zijn allemaal *beslissings-* of *integratie-*leerstukken, niet techniek.

### Leerstuk 1 — `werkkapitaalbeheer-en-financieringskeuzes`

- **Vraag**: Hoe stuur je werkkapitaal en kies je een gezonde financieringsmix?
- **Type**: beheers-fiche (beslissingen, niet formules)
- **Gedekte doelstellingen**: voedt 1.9.1.5 (diagnose-input), 1.9.1.6 (aanbevelingen), 1.9.1.10 (kasplanning)
- **Gedekte concepten**: `[[functionele-balans]]` (verwijzing — formules bij 1.3) · BBK-reductiemaatregelen · financieringsmix EV/VV/korte/lange termijn · dividend-capaciteit (kapitaalbeschermings-test) · matching-principe activa/passiva
- **Examen-anker**: 2013-2 NBK-verhogen (3 maatregelen) + 2008 BBK-reductie-maatregelen + 2019 stellingen DSO/DIO
- **Rationale**: De beheers-laag: aangenomen dat NBK/BBK/NT-formules elders staan, hier draait alles om de **beslissingen** op die metingen. Drie families maatregelen (voorraden afbouwen, klantenkrediet beheren, leverancierskrediet rekken) + de tegenkracht (commerciële kost, leveranciers-relatie). Financieringsmix-keuzes en dividend-capaciteit zitten erbij omdat ze structureel ingrijpen op de balans-mix.

### Leerstuk 2 — `kredietbeoordeling-en-kasstroomprognose`

- **Vraag**: Hoe beoordeel je of een onderneming een nieuwe lening of investering aankan?
- **Type**: integratie-fiche (techniek → beslissing)
- **Gedekte doelstellingen**: 1.9.1.7 (passende ratio's voor probleem) + 1.9.1.10 (prognoses)
- **Gedekte concepten**: `[[free-cash-flow]]` (techniek bij 1.3) · DSCR · annuïteit-formule · matching-principe lening ↔ economische levensduur · kasstroomprognose · `[[financiele-diagnose]]`
- **Examen-anker**: 2008 investeringskrediet-haalbaarheid (DSCR + alternatieven)
- **Rationale**: Cash-as-decision-driver. DSCR-vuistregel + annuïteit-rekening + matching-principe + bullet/ballonkrediet-alternatieven. Bovenop dat een kasstroomprognose-sectie (omzetdrivers → kostenstructuur → werkkapitaalmutaties → CF) voor de 1.9.1.10 prognose-doelstelling. Examen-anker 2008 is een paradevoorbeeld van dit leerstuk.

### Leerstuk 3 — `continuiteit-en-faillissementspredictie`

- **Vraag**: Hoe toets je de continuïteit van een onderneming + welke wettelijke kaders raken eraan?
- **Type**: specifiek-fiche (juridisch-financieel snijvlak, één van de hardste secties)
- **Gedekte doelstellingen**: 1.9.1.5 (diagnose: risico-as), 1.9.1.6 (early warning ↔ aanbeveling), voedt 1.9.1.11 (vereffenings-fase)
- **Gedekte concepten**: `[[continuiteit]]` · `[[faillissementspredictie-modellen]]` (Z-score, O-score) · raakvlak `[[faillissement]]` · `[[kapitaalbescherming]]` (alarmprocedure-link)
- **Wettelijk kader (verifiëren via RAG)**:
  - WVV art. 3:6 — jaarverslag risico's en onzekerheden ⚖️
  - WVV art. 7:228, 7:229 — alarmprocedure netto-actief NV ⚖️
  - WVV art. 5:153 — alarmprocedure BV (kapitaalloze variant) ⚖️
  - CBN-advies 2018/18 — going concern + waarderingsregels bij stopzetting ⚖️
  - CBN-advies 2021/14 — jaarrekeningrechtelijke analyse alarmbelprocedure ⚖️
  - ISA 570 — auditor going-concern-werk (PO 1.6 raakvlak) ⚖️
- **Examen-anker**: niet bevraagd in BIBF-cyclus; ITAA-integratie-niveau plausibel.
- **Rationale**: Drie lagen die natuurlijk samen werken: (1) wettelijke triggers (alarmbel + jaarverslag-vermelding) (2) kwantitatieve early-warning indicatoren (Z-score + 6 financiële + 5 niet-financiële signalen ISA 570) (3) keten naar PO 1.6 audit-werk. Eigen leerstuk omdat juridische triggers + predictie-modellen niet in een ratio-leerstuk passen.

### Leerstuk 4 — `financiele-diagnose-stellen`

- **Vraag**: Hoe integreer je alle analyses in één diagnose-rapport met aanbevelingen?
- **Type**: proces-fiche (het integratie-leerstuk; recht-doend aan PO-niveau "integratie")
- **Gedekte doelstellingen**: 1.9.1.1 (stakeholders), 1.9.1.4 (contextualiseren), 1.9.1.5 (diagnose), 1.9.1.6 (aanbevelingen), 1.9.1.8 (databanken), 1.9.1.9 (tools), 1.9.1.11 (fase-begeleiding)
- **Gedekte concepten**: `[[financiele-diagnose]]` (hoofdconcept) · `[[ratio-interpretatie]]` (techniek bij 1.3, integratie hier) · `[[financiele-analyse-software]]` (NBB Balanscentrale, Bel-first, Trends Top, Belfius Companyweb)
- **Examen-anker**: niet bevraagd in BIBF-cyclus; ITAA-integratie-niveau klassieke kandidaat voor scenario-cases.
- **Rationale**: Het eindproduct-leerstuk. Bestaat uit: (1) data-discipline en bronnenkeuze (databanken, peer-data, NACE-codes, consistentie-correcties) (2) diagnose-template (executive summary → 4 ratio-families × trend × sector → cashflow → continuïteit → SWOT financieel) (3) aanbevelingen per stakeholder (bestuur, bank, aandeelhouder) (4) rol-perspectieven (adviseur-analist, CFO-intern, commissaris-going-concern) (5) fase-context (groei vs maturiteit vs herstructurering).

---

### Mapping examen-vragen → leerstuk (voor v2)

| Examen-vraag | Lands-leerstuk | Hoofdtechniek hoort bij |
|---|---|---|
| 2003 NBK-berekening | L1 sectie "diagnostisch lezen NBK" | 1.3 techniek |
| 2003 current/acid/solvabiliteit | (concept-records, geen 1.9-leerstuk) | 1.3 techniek |
| 2003 operationele cashflow | L2 (als input voor DSCR-case) | 1.3 techniek |
| 2008 BBK definitie + reductie | L1 (reductie-as) | Definitie naar 1.3 |
| 2008 investeringskrediet DSCR | **L2 kern-case** | — |
| 2013-1 definities (intrinsieke/fractie/ROA/schuld/operationele CF) | (concept-records, geen 1.9-leerstuk) | 1.3 techniek + concept-laag |
| 2013-2 NBK-verhogen 3 maatregelen | **L1 kern-case** | — |
| 2019 nulcoupon | (concept-record, geen 1.9-leerstuk) | techniek elders |
| 2019 stellingen permanent vermogen + DSO | L1 (DSO/DIO-stellingen-sectie) | Definitie naar 1.3 |

---

## 4. Gap-check

| Doelstelling | Gedekt door | Notitie |
|---|---|---|
| 1.9.1.1 Financiële analyse als info voor stakeholders | L5 (intro-context) + L1 (entry-frame) | Volledig |
| 1.9.1.2 Lezen + begrijpen jaarrekening | L1 (kern) | Volledig |
| 1.9.1.3 Consistentie + relevantie gegevens | L1 (sectie methodologie) + L5 (data-discipline) | Volledig |
| 1.9.1.4 Contextualiseren omgeving | L5 (sector + peer + macro) + L2 (peer-vergelijking-laag in interpretatie) | Volledig |
| 1.9.1.5 Financiële diagnose stellen | L5 (kern) + L4 (continuïteits-as) | Volledig — eindproduct |
| 1.9.1.6 Problematiek vaststellen + aanbevelingen | L5 (template + rol-perspectieven) | Volledig |
| 1.9.1.7 Passende ratio's gebruiken | L2 (kern) + L3 (cash-ratio's) | Volledig |
| 1.9.1.8 Databanken (Balanscentrale, Bel-first, Trends Top) | L5 (data-discipline-sectie) | Volledig |
| 1.9.1.9 Tools financiële analyse | L5 (software-sectie + concept-fiche) | Volledig |
| 1.9.1.10 Financiële prognoses | L3 (kasstroomprognose-aspect) + L5 (scenario-laag) | **Mogelijk gap** — prognose-bouwen (geprojecteerde balans/resrek/CF + drivers) krijgt geen eigen leerstuk. Voorstel: opnemen als sectie in L3 + L5. Indien examen-frequentie stijgt, latere splitsing als 6e leerstuk overwegen. |
| 1.9.1.11 Fase-begeleiding (oprichting → vereffening) | L5 (fase-context-sectie) + cross-PO-tabel | Rakend — kern leeft in andere PO's. Volstaat. |

**Extra dekking** (PO-titel "fundamentele principes financieel bedrijfsbeheer"):
- Werkkapitaalbeheer (BBK-reductiemaatregelen) → L1
- Aflossingscapaciteit + kredietbeoordeling → L3
- Going-concern monitoring + alarmprocedure → L4
- Geen aparte sectie voor "financieringskeuzes" (eigen vs vreemd, korte vs lange termijn) — gedekt in L1 (NBK-verhogen-maatregelen) + L3 (cash). Voldoende.

---

## 5. Minicursus-skelet

Volgt de canonieke 5-secties-structuur (ADR-036, samenvoeging §3+§4 sinds 1.4).

### §1 — Waarom dit vak?

- Motivatie: jaarrekening *lezen* zoals een bank, investeerder of rechter doet — niet maken (1.4) of auditen (1.6)
- Bredere-programma-tabel: relatie tot 1.3 (analyse-techniek), 1.4 (geconsolideerd), 1.6 (going concern), 1.8 (interne vs externe cijfers), 3.0 (alarmprocedure)

### §2 — Wat is dit vak?

Vier compacte sub-secties, elk eindigend met wikilink naar het leerstuk dat het uitwerkt:

- "Het probleem en de herstructurering" → [[wat-is-een-geconsolideerde-jaarrekening|jaarrekening-lezen-en-herstructureren]]
- "De vier ratio-families" → [[ratios-en-hun-interpretatie]]
- "De cash-dimensie" → [[kasstromen-en-financieringscapaciteit]]
- "Vooruitkijken — continuïteit en diagnose" → [[continuiteit-en-faillissementspredictie]] + [[financiele-diagnose-stellen]]

### §3 — Wat moet je kunnen + hoe pak je het aan

Leerstukken-leesroute in **5 stappen** (één per leerstuk, in volgorde van afhankelijkheid):

1. Herstructureer eerst — `jaarrekening-lezen-en-herstructureren`
2. Bereken ratio's met betekenis — `ratios-en-hun-interpretatie`
3. Voeg de cash-laag toe — `kasstromen-en-financieringscapaciteit`
4. Toets continuïteit — `continuiteit-en-faillissementspredictie`
5. Integreer in een diagnose — `financiele-diagnose-stellen`

Samenvatting-verwijzing (printbaar 2-4 A4) voor herhaling vlak voor examen.

### §4 — Examen-radar

Tabel met 7 voorbeeldexamen-eenheden + observatie ("werkkapitaal-drieluik domineert, DSCR-case recurrent, geen continuïteits-vraag in oude BIBF — maar ITAA-integratie-niveau verschuift dat").

### §5 — Concepten cross-PO

Tabel met concepten die ook in 1.3, 1.4, 1.5, 1.6, 1.8, 3.0 leven (continuiteit, jaarrekeninganalyse, kasstroom-analyse, liquiditeits-ratios, solvabiliteits-ratios, free-cash-flow, faillissementspredictie-modellen).

---

## 6. Voorbeeldgroep — voorstel

**Naam (voorgesteld)**: `belmonte` — Belmonte Industries NV

**Niet hergebruiken**: `aurelia` is consolidatie-gericht en mist trend-data + werkkapitaal-spanning. Voor 1.9 hebben we nodig:
- **3 boekjaren** (om trend te tonen) — bv. 2023-2025
- **Werkkapitaal-spanning** die meetbaar verslechtert (dalende NBK, stijgende BBK, krimpende nettothesaurie)
- **Krimpende margin** + één eenmalige post (zodat correctie nodig is voor consistentie-doelstelling 1.9.1.3)
- **Kredietaanvraag-case** voor DSCR (parallel aan examen 2008)
- **Z-score-input** mogelijk (alle 5 ratio's berekenbaar)
- **Sector-benchmark-data** (3 peers in dezelfde NACE-code) om peer-vergelijking-laag te illustreren

**Inhoud (te genereren in stap 2)**:
- Bedrijfsbeschrijving + sector + NACE-code + balansdatum + 3 boekjaren
- Balansen 2023-2025 (verkort schema, intern consistent)
- Resultatenrekeningen 2023-2025 + één eenmalige post (bv. desinvestering of voorzieningstoevoeging)
- Functionele-balans-herrangschikking (NBK · BBK · NT) per boekjaar
- Ratio-tabel (4 families × 3 boekjaren) + peer-medianen
- Mock kasstroomoverzicht (indirecte methode) voor 1 boekjaar
- Investeringskrediet-aanvraag-case (analoog aan examen 2008: bedrag + looptijd + jaarlijkse cashflow + DSCR-toets)
- Z-score-berekening + interpretatie
- Eén "early warning"-event (bv. RSZ-achterstand, langer wordende klantkrediettermijn)

**Open vraag voor sparring**: wil je een nieuwe groep van scratch, of liever Aurelia uitbreiden met meerjarige cijfers + werkkapitaal-spanning (hergebruik-voordeel: cross-PO-cohesie). Voorstel: **nieuwe groep `belmonte`** — een industriële KMO met werkkapitaal-spanning leest pedagogisch anders dan een groepsstructuur, en mengt zou de voorbeeldgroepen onleesbaar maken.

---

## 7. Samenvatting + oefening

### Samenvatting

Per [`docs/samenvatting-procedure.md`](samenvatting-procedure.md): YAML in `data/samenvattingen/1-9.yaml`, gerendere markdown in `content/leerpaden/1-9/samenvatting.md`. Pijlers:
- Werkkapitaal-drieluik-formules + visuele balans-herrangschikking
- Vier ratio-families formule-tabel
- Kasstroom-categorieën IAS 7 + DSCR-formule
- Continuïteits-trigger-tabel (3:6/3:32 + 7:228 drempels + CBN 2018/18 + 2021/14)
- Z-score-formule + interpretatie-banden

### Oefening (5e laag)

Per [`docs/oefening-procedure.md`](oefening-procedure.md). Voorstel: **Belmonte-diagnose-case** — leerling krijgt 3 boekjaren ruwe data + sector-medianen + één vraag aan de boekhouder ("bank vraagt of ze ons een investeringskrediet van X kunnen geven"). Leerling moet:
- Herstructureren naar functionele balans
- Ratio's berekenen + interpreteren (trend + sector)
- Kasstroom-analyse + DSCR-toets
- Continuïteits-indicatoren screenen + Z-score
- Diagnose-rapport met sterktes/zwaktes/aanbevelingen

Geen hints in de opgave. Aparte intra-groep-mapping (oefening-data uit voorbeeldgroep + extra "ruw"-versie zonder reeds-herstructureerde cijfers).

---

## 8. Open vragen voor sparring

Beslismomenten waar de gebruiker moet kiezen voordat we naar Stap 2 (voorbeeldgroep) gaan:

1. **Granulariteit ratio-leerstuk** — Voorstel: 1 leerstuk met 4 sub-secties + interpretatie-laag (4500-5000 woorden cap). Alternatief: 2 leerstukken (statische/structurele = liquiditeit+solvabiliteit, dynamische = rentabiliteit+activiteit). Of zelfs 4 (per familie). **Aanbevolen: 1 leerstuk** — stelregel "eerder samen", examen vraagt families altijd in combinatie, kunstmatige splitsing creëert herhaalde inleidingen.

2. **`financiele-diagnose-stellen` als apart leerstuk vs rol-blokken in elk leerstuk** — Bij PO 1.4 zijn rol-perspectieven in elk leerstuk geïntegreerd (geen apart rol-leerstuk). Voor PO 1.9 stel ik wel een apart integratie-leerstuk voor omdat het PO-niveau letterlijk "integratie" is en de diagnose-template (data → herstructurering → ratio's → CF → continuïteit → advies) zelfstandig pedagogisch werk is. **Aanbevolen: apart leerstuk** maar bevestig.

3. **Cross-PO leerstukken** — Geen. Alle 5 leerstukken leven in `content/leerpaden/1-9/`. `continuiteit-en-faillissementspredictie` raakt sterk PO 1.6/3.0 maar de financieel-analyse-invalshoek is hier kern; voor PO 1.6 schrijven we later een eigen leerstuk vanuit auditor-perspectief met wikilink naar dit leerstuk.

4. **Voorbeeldgroep** — Nieuwe groep `belmonte` (industriële KMO met werkkapitaal-spanning + kredietaanvraag-case) vs uitbreiden Aurelia. **Aanbevolen: nieuw**.

5. **Verhouding met PO 1.3 (Analyse jaarrekening)** — Sterke overlap. Voorstel: 1.9 is *het* analyse-PO; 1.3 wordt later een afgeleide minicursus die naar 1.9-leerstukken doorlinkt (geen eigen leerstuk-pakket). Of houden we 1.3 separaat met eigen ratio-leerstukken? **Sparring nodig** — voor nu schrijven we voor 1.9 zonder 1.3-coördinatie; bij 1.3-aanpak passen we cross-PO-tabel aan.

6. **Prognose-leerstuk** — In voorstel niet apart; verdeeld over L3 (kasstroomprognose) en L5 (scenario's). Bij toename examen-frequentie 6e leerstuk toevoegen. **Aanbevolen: niet apart nu**.

7. **Themafiche-mapping** — Per ADR-039 vervangen we oude cluster-themafiches door één PO-samenvatting (2-4 A4). Welke bestaande themafiches in `content/themafiches/` raken 1.9? Te checken in stap 6 — naar verwachting (uit oude 1.9.md): `continuiteit-en-diagnose`, `jaarrekeninganalyse-aanpak`, `kasstroom-analyse`, `ratio-families`. Worden alle vier gemigreerd naar `content/leerpaden/1-9/samenvatting.md` en daarna verwijderd, behalve als ze écht cross-PO zijn (te beoordelen).

---

## 9. Rapport (max 6 bullets)

- **5 leerstukken voorgesteld** (entry+herstructurering · ratio's · cash · continuïteit · integratie-diagnose)
- **Hoofdtaak** van het PO: financiële analyse + diagnose (niveau integratie); titel-doel mismatch zoals bij 1.4
- **Gaten geïdentificeerd**: prognose-bouwen krijgt geen eigen leerstuk maar wordt verdeeld over L3+L5 — accepteren of als 6e leerstuk?
- **Nieuwe voorbeeldgroep** `belmonte` (3-jaars industriële KMO met werkkapitaal-spanning + kredietaanvraag) — Aurelia is niet geschikt
- **Belangrijkste onzekerheid**: verhouding 1.9 ↔ 1.3 (overlap analyse-techniek) en granulariteit ratio-leerstuk (1 vs 2 vs 4)
- **Volgende stap na akkoord**: voorbeeldgroep-data (`data/voorbeeldgroepen/belmonte.yaml`) + parallel script-pass voor 5 leerstukken

---

*Skelet geschreven door Opus, 2026-05-31. Bron-discipline: programma.json (primair) + 12 bestaande concept-records (gecontroleerd via RAG) + 7 voorbeeldexamen-eenheden + CBN 2018/18 + CBN 2021/14 + WVV 3:6/3:32/7:228 (bevestigd via RAG). Oude `content/leerpaden/1-9.md` als achtergrond-context gebruikt, niet als source-of-truth.*
