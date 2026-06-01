# Leerpad-skelet PO 1.7 — Interne controle

**Status**: voorstel (2026-06-01). Sparring-document voor de bouw van het volledige leerpad-pakket (overzicht + leerstukken + samenvatting + oefening + voorbeeldexamenvragen-auto).

**Volgende stap**: voorbeeldgroep + scripts per leerstuk via één Opus-run + render via parallel Sonnet-agenten + minicursus-update (themafiche-refs raus) + samenvatting from-scratch (PO 2.5/2.7-aanpak, NIET themafiche-migratie).

---

## 1. Programma-analyse

### Officiële taken en doelstellingen

PO 1.7 telt **één hoofdtaak met zes doelstellingen**. Niveau: **integratie** — hoogste cognitieve laag.

| Code | Tekst (kort) | Rol |
|---|---|---|
| 1.7.taak.1 | Opstellen van specifieke verslagen en analyses (extern + intern + juridisch/contractueel) | anchor |
| 1.7.taak.1.doel.1 | Begrijpen van redelijke zekerheid + naleving/compliance | context |
| 1.7.taak.1.doel.2 | Zoeken van referentiepunten t.o.v. verwachtingen van belanghebbenden | context |
| 1.7.taak.1.doel.3 | Opsporen van risico's | context |
| 1.7.taak.1.doel.4 | Evenwicht beheren tussen redelijke zekerheid en compliance | context |
| 1.7.taak.1.doel.5 | Interpreteren van aanbevelingen van revisoren/accountants (managementletter) | context |
| 1.7.taak.1.doel.6 | Formuleren van aanbevelingen naar aanleiding van vastgestelde risico's | context |

### Kenniselementen-tree (acht hoofdblokken)

- **1.7.I — BEGRIPPEN VAN INTERNE CONTROLE**: definitie · externe controle (afbakening) · managementcontrole (afbakening) · interne audit
- **1.7.II — DEFINITIES EN HERHALINGEN**: onderneming · informatiesysteem · stromen · informatie · controle · controleproces · ethiek
- **1.7.III — KENMERKEN VAN INTERNE CONTROLE**: dubbele dimensie (preventief/detectief) · vier doelstellingen · redelijke zekerheid · actoren-verscheidenheid (3 Lines)
- **1.7.IV — ACTOREN EN MIDDELEN VAN DE INTERNE CONTROLE**
- **1.7.V — AUDIT**: interne audit · functie interne auditor · externe audit · auditcomité · auditrisico's
- **1.7.VI — FOUTEN EN FRAUDE**: fouten · fraude · verspilling
- **1.7.VII — FUNCTIESCHEIDING** (eigen hoofdblok — wijst op gewicht)
- **1.7.VIII — UITVOERING VAN INTERNE CONTROLE**: aanpak · taakverdeling · opvolging verrichtingen · controlemiddelen · IT-omgeving · evaluatie

**Structuur-observatie**:

1. Het programma is **inhoudelijk gedupliceerd**: interne audit verschijnt in I.D én V.A; functiescheiding in VII én VIII.B; controlemiddelen in II.E (controle) én VIII.D. Dit signaleert dat het programma "ronddenkt" rond een handvol kernbegrippen — die kernbegrippen verdienen de eigen leerstukken.
2. **Vier doelstellingen** (III.B.1) en **vijf COSO-componenten** (impliciet in I.A) zijn de dubbele kapstok — beide moeten elke leerstuk-leesroute openen.
3. **VIII.A (aanpak uitwerking) + doel.6 (aanbevelingen formuleren)** vormen samen het "ontwerp-luik" — vaak vergeten maar examen-relevant.

### Kern vs rakend

**Kern (in leerstukken uitgewerkt)**:
- Definitie + 4 doelstellingen + redelijke zekerheid + 5 inherente beperkingen (oordeel · breakdown · collusie · management override · kosten-baten)
- COSO IC 2013 (5 componenten + 17 principes — impliciet) + KMO-proportionaliteit (ITAA KMO-controlenorm)
- Functiescheiding — ACR-IH-leer (Autoriseren / Controleren / Registreren / Uitvoeren-Initiëren / Houden-Bewaren) + 4-categorieën-typologie (1 Autorisatie · 2 Bewaring · 3 Registratie · 4 Controleprocedures) ⚖️
- 5 transactionele cycli (aankoop · verkoop · voorraad · kas-treasury · lonen) + sleutelcontroles per cyclus + 3-way match + autorisatiematrix
- IT-controles — ITGC (toegang · change management · operations) vs application controls + cloud shared responsibility
- Fouten · fraude · fraudedriehoek (druk · gelegenheid · rationalisatie) ⚖️ + 3 categorieën fraude (misappropriatie · frauduleuze rapportering · corruptie)
- Aanpak uitwerking interne controle (8 stappen: doelstellingen → proces-mapping → risico-identificatie → risico-evaluatie → controle-selectie → documentatie → uitrol → monitoring)
- Interne audit (3e lijn) + auditcharter + risk-based auditplan + IIA-standards
- Auditcomité (WVV art. 7:99 voor genoteerde + OOB)
- Evaluatie interne controle — design vs operating effectiveness + walkthrough vs test of controls + management letter (ISA 265 communicatie)
- Aanbevelingen formuleren — SMART · prioriteit · verantwoordelijke · termijn

**Rakend (in overzicht vermeld, geen eigen leerstuk-uitwerking)**:
- **PO 1.6 — Externe controle**: dezelfde IC wordt door commissaris geëvalueerd (ISA 315 herzien-2019 + ISA 330 + ISA 240 fraude + ISA 265 communicatie + ISA 610 reliance op interne audit). PO 1.7 schrijft het IC-systeem; PO 1.6 toetst het van buitenaf.
- **PO 1.1/1.2 — Boekhouding**: het boekhoudkundig registratiesysteem is één van de 5 COSO-componenten (informatie & communicatie); art. III.82 e.v. WER + KB 29.04.2019.
- **PO 3.0 — Vennootschapsrecht**: bestuursverantwoordelijkheid voor IC (WVV art. 7:96 alarmbel-context + 7:99 auditcomité bij genoteerde) ⚠️ te verifiëren in skelet-uitwerking
- **PO 4.0 — Deontologie / AML**: anti-witwas-controles + KYC + interne reglementen zijn een specifieke laag van IC; AMLCO ↔ COSO controleomgeving
- **PO 2.5 — Fiscale procedure**: fiscale interne controle (juiste boeking → juiste aangifte → audit-trail bij BvW)

### Verbinding tussen taak en kennis

De ene taak "Opstellen van specifieke verslagen en analyses" is **misleidend smal** als beschrijving van wat de stagiair moet kunnen. De zes doelstellingen tonen waar het echt om gaat: **een IC-systeem leren analyseren, evalueren én erover schriftelijk adviseren** — niet alleen rapporteren. Het is een **integratie-vak**: de stagiair moet zowel COSO-theorie kunnen toepassen op een KMO-context als concrete cyclus-controles ontwerpen en als ontvanger van een externe-auditor-managementletter de aanbevelingen kunnen herinterpreteren naar bestuur-actie.

---

## 2. Voorbeeldexamen-patronen

Uit `content/studiemateriaal/1-7/voorbeeldexamenvragen.md`: **20 unieke vraag-eenheden** in 6 examens (2010-2, 2013-1, 2013-2, 2014-1, 2015-1, 2024-1) — PO 1.7 wordt **elk examen** getest, vaak meerdere keren.

| Onderwerp | Hoe vaak? | Type vraag | Wijst naar leerstuk |
|---|---|---|---|
| **Functiescheiding** — indeling van taken naar categorie (1 Autorisatie · 2 Bewaring · 3 Registratie · 4 Controle) | 2× (2014-1, 2013-2) | Classificatie 8 activiteiten | `functiescheiding-en-controlemaatregelen` |
| **Doelstellingen van interne controle** — drie/vier hoofddoelen | 2× (2024-1, 2013-1) | Begrip + opsomming | `wat-is-interne-controle-en-coso` |
| **Verkoopcyclus** — risico's, adviezen, doelstellingen indelen (Fin/Op/Conf) | 2× (2024-1, 2015-1) | Open + classificatie | `cyclus-analyse-en-controlemiddelen` |
| **Soorten controle-maatregelen** — preventief, repressief, corrigerend | 2× (2013-2, 2015-1) | Classificatie + voorbeelden | `functiescheiding-en-controlemaatregelen` |
| **Accountingcontrole vs administratieve controle** — begripsverklaring + voorbeelden | 1× (2015-1) | Begrip + voorbeelden | `functiescheiding-en-controlemaatregelen` |
| **COSO-risicoclassificatie** — vier categorieën (Strategisch/Informatie/Operationeel/Financieel) | 1× (2024-1) | Theorie | `wat-is-interne-controle-en-coso` |
| **Onregelmatigheden door boekhouder** — maatregelen | 1× (2013-1) | Toepassingscase | `fouten-fraude-en-risicobeheersing` |
| **Risico's bij aanmaken klantenfiches door verkoop** | 1× (2014-1) | Toepassingscase | `cyclus-analyse-en-controlemiddelen` |
| **Externe bevestiging leveranciers door interne audit** | 1× (2013-1) | Procedure | `interne-audit-evaluatie-en-aanbevelingen` |
| **Procedure kasbetalingen kleine kosten** (2 functiescheidingen) | 2× (2014-1 + 2013-1 dupl.) | Toepassing functiescheiding | `functiescheiding-en-controlemaatregelen` |
| **Analytische test tussentijdse resultaten** | 1× (2013-1) | Procedure interne audit | `interne-audit-evaluatie-en-aanbevelingen` |
| **Belang van budget voor interne controle** | 1× (2013-1) | Theorie | `wat-is-interne-controle-en-coso` |
| **Controletechnieken goederenbestand magazijn** | 1× (2015-1) | Procedure | `cyclus-analyse-en-controlemiddelen` + `interne-audit-evaluatie-en-aanbevelingen` |
| **Doelstellingen boekhoudkundige registratie — juist/fout** (autorisatie · bescherming activa · realiteit · cut-off · reconciliatie) | 1× (2014-1) | Juist/fout | `wat-is-interne-controle-en-coso` |

**Drie patronen die opvallen**:

1. **Functiescheiding domineert** — komt direct of indirect in elk examen voor. De **4-categorieën-typologie** (1 Autorisatie · 2 Bewaring · 3 Registratie · 4 Controle) en de **5-functies-leer ACR-IH** (Beschikken · Uitvoeren · Registreren · Controleren · Bewaren) worden door elkaar gebruikt; beide moeten beheerst worden.
2. **Cyclus-toepassing** — vooral verkoop (klantenfiches, omzet, verkooporders) en aankoop (3-way match, leveranciers-master, betalingen). Examenstijl: een proces wordt beschreven, kandidaat moet risico's én controles benoemen.
3. **Classificatie-vragen** — preventief/repressief/corrigerend · financieel/operationeel/conformiteit · accountingcontrole/administratieve controle. Drie taxonomieën die door elkaar getest worden.

**Wat opvalt afwezig**:
- Geen vragen over **COSO ERM 2017** apart (alleen IC 2013 / vier doelstellingen / vier risicocategorieën)
- Geen vragen over **3 Lines of Defense** als model — wel impliciet via interne audit
- Geen vragen over **WVV art. 7:96** als wettelijke grondslag voor IC

---

## 3. Leerstuk-voorstel

**Vijf leerstukken** — afdekking van alle zes doelstellingen + alle 8 kenniselementen-blokken. Granulariteits-stelregel (eerder samen dan splitsen) toegepast: functiescheiding + controlemaatregel-taxonomieën samen; cyclus + IT-controles samen; interne audit + auditcomité + evaluatie + aanbevelingen samen.

### Leerstuk 1 — `wat-is-interne-controle-en-coso`

- **Vraag**: Wat is interne controle, welke doelstellingen dient zij, en welk referentiekader (COSO) structureert haar?
- **Type**: entry (kortste leerstuk, doorklik-zwaar)
- **Gedekte doelstellingen**: 1.7.taak.1.doel.1 (redelijke zekerheid + compliance) + 1.7.taak.1.doel.2 (referentiepunten) + 1.7.taak.1.doel.4 (evenwicht)
- **Gedekte kenniselementen**: 1.7.I (begrippen — definitie + afbakening externe/management/internal audit) + 1.7.II (woordenschat) + 1.7.III (kenmerken — dubbele dimensie + 4 doelstellingen + redelijke zekerheid + 3 Lines) + 1.7.IV (actoren-overzicht)
- **Gedekte concepten**: `interne-controle` · `coso-framework` (deels)
- **Rationale**: Eén entry-leerstuk dat de stagiair de **kapstok** geeft: wat is IC (niet externe controle, niet management control, niet interne audit), welke 4 doelen dient ze (operations · reporting · compliance · safeguarding), wat is redelijke zekerheid + de 5 inherente beperkingen, welke 5 COSO-componenten + 4 risicocategorieën (strategisch/operationeel/informatie/financieel — examen-favoriet 2024), KMO-proportionaliteit (ITAA-norm). Lengte 1800-2200 woorden.

### Leerstuk 2 — `functiescheiding-en-controlemaatregelen`

- **Vraag**: Hoe scheidt men onverenigbare functies, en welke taxonomieën gebruiken auditoren om controlemaatregelen te classificeren?
- **Type**: techniek (denkmotor)
- **Gedekte doelstellingen**: 1.7.taak.1.doel.3 (risico's opsporen) + 1.7.taak.1.doel.4 (evenwicht zekerheid/compliance)
- **Gedekte kenniselementen**: 1.7.VII (functiescheiding eigen blok) + 1.7.VIII.B (taakverdeling) + 1.7.II.E (begrip controle — preventief/detectief/correctief) + 1.7.III.A (dubbele dimensie)
- **Gedekte concepten**: `functiescheiding` · `interne-controle` (deels — controle-typologieën)
- **Rationale**: Eén leerstuk dat **drie taxonomieën** doceert die in elk examen terugkomen: (1) **5 controletechnische functies ACR-IH** — Beschikken / Uitvoeren / Registreren / Controleren / Bewaren ("BURCB-ezelsbruggetje") met regel "min 2 niet-aangrenzende per persoon"; (2) **4-categorieën-typologie** (1 Autorisatie · 2 Bewaring · 3 Registratie & rapportering · 4 Controleprocedures) — examen 2013-2 en 2014-1 gebruiken deze; (3) **karakter-driehoek preventief/detectief/correctief** met klassieke voorbeelden + KMO-compensaties (management override-monitoring door zaakvoerder). Plus **accountingcontrole vs administratieve controle** (Starreveld-traditie, vraag 2015-1). Lengte 2200-2600 woorden.

### Leerstuk 3 — `cyclus-analyse-en-controlemiddelen`

- **Vraag**: Hoe analyseer je een onderneming per transactiecyclus en welke sleutelcontroles passen per cyclus — inclusief in een IT-gedreven omgeving?
- **Type**: proces (zwaarste leerstuk)
- **Gedekte doelstellingen**: 1.7.taak.1.doel.3 (risico's opsporen) + 1.7.taak.1.doel.6 (aanbevelingen formuleren)
- **Gedekte kenniselementen**: 1.7.VIII.A (aanpak uitwerking) + 1.7.VIII.C (opvolging verrichtingen) + 1.7.VIII.D (controlemiddelen) + 1.7.VIII.E (geïnformatiseerde omgeving) + 1.7.II.C (stromen) + 1.7.II.B (informatiesysteem)
- **Gedekte concepten**: `cyclus-analyse` · `it-controles` · `ontwerp-interne-controle` (deels)
- **Rationale**: Cyclus-aanpak is **het werkpaard** van IC-design en IC-evaluatie. Vijf cycli systematisch doorlopen: **aankoop (P2P)** met 3-way match + leveranciersmaster · **verkoop (O2C)** met kredietacceptatie + facturatie + DSO · **voorraad** met cyclische tellingen + cut-off · **kas/treasury** met functiescheiding en periodieke reconciliatie · **lonen (H2R)** met spookmedewerker-risico + onboarding-offboarding. Per cyclus: top-risico's + sleutelcontroles. Daarna **IT-laag**: ITGC (toegang RBAC · change management · backup) vs application controls (veld-validaties · automatische reconciliatie) + IT-dependent manual + cloud shared responsibility + walkthrough-techniek. Lengte 2800-3200 woorden.

### Leerstuk 4 — `fouten-fraude-en-risicobeheersing`

- **Vraag**: Wat is het onderscheid tussen fouten en fraude, hoe ontstaat fraude, en hoe organiseert men de risicoanalyse die de IC-architectuur stuurt?
- **Type**: specifiek (smal, diep)
- **Gedekte doelstellingen**: 1.7.taak.1.doel.3 (risico's opsporen) + 1.7.taak.1.doel.4 (evenwicht)
- **Gedekte kenniselementen**: 1.7.VI (fouten + fraude + verspilling) + 1.7.II.G (ethiek — tone at the top) + 1.7.III.B.3 (redelijke zekerheid + inherente beperkingen)
- **Gedekte concepten**: `fouten-en-fraude` · `interne-controle` (deels — risico-analyse-laag)
- **Rationale**: Eén leerstuk dat **drie zaken samen doet**: (1) onderscheid fout vs fraude vs verspilling — drie verschillende oorzaken vragen drie verschillende mitigaties; (2) **fraudedriehoek Cressey** (druk · gelegenheid · rationalisatie) + 3 fraudecategorieën (misappropriatie · frauduleuze rapportering · corruptie) — wat de fraudeur in de hand werkt en hoe IC daarop antwoordt; (3) **risico-identificatie-methode** (PESTEL voor extern + cyclus-scan voor intern + heat map kans×impact) als input voor de controle-architectuur uit leerstuk 3. Plus **management override** als grootste inherente beperking + ethiek/tone-at-the-top als zachte controle. Examen 2013-1 (onregelmatigheden door boekhouder) past hier perfect. Lengte 1800-2200 woorden.

### Leerstuk 5 — `interne-audit-evaluatie-en-aanbevelingen`

- **Vraag**: Wie evalueert het IC-systeem (intern + extern), hoe doet hij dat, hoe rapporteert hij, en hoe vertaalt men die aanbevelingen naar actie?
- **Type**: proces
- **Gedekte doelstellingen**: 1.7.taak.1.doel.5 (interpreteren aanbevelingen revisor) + 1.7.taak.1.doel.6 (aanbevelingen formuleren) + 1.7.taak.1.doel.2 (referentiepunten — IIA + ISA)
- **Gedekte kenniselementen**: 1.7.V (audit — interne audit + functie + externe audit + auditcomité + auditrisico's) + 1.7.VIII.F (evaluatie) + 1.7.I.D (interne audit — herhaling van V.A)
- **Gedekte concepten**: `interne-audit` · `auditcomite` · `evaluatie-interne-controle`
- **Rationale**: Het **afdwingings- en evaluatie-luik**. Vier zaken samen omdat ze één pedagogische beweging vormen: (1) **interne audit** als 3e-lijn-functie — onafhankelijkheid · auditcharter · risk-based auditplan · IIA-standards · technieken (inspectie · observatie · navraag · herrekening · analytische review · externe bevestiging — examenstof 2013-1 + 2015-1); (2) **auditcomité** als governance-orgaan (WVV art. 7:99 voor genoteerde + OOB) — schakel tussen bestuur + interne audit + commissaris; (3) **evaluatie IC** — design effectiveness (walkthrough) vs operating effectiveness (test of controls over periode) + de drie types tekortkomingen (deficiency · significant deficiency · material weakness); (4) **management letter (ISA 265)** — hoe de externe auditor IC-tekortkomingen communiceert en hoe de stagiair als adviseur die vertaalt naar **SMART-aanbevelingen** (specifiek · meetbaar · acceptabel · realistisch · tijd-gebonden) voor het bestuur. Lengte 2400-2800 woorden.

---

## 4. Gap-check

| Doelstelling | Gedekt door | Notitie |
|---|---|---|
| 1.7.taak.1.doel.1 Redelijke zekerheid + compliance | Leerstuk 1 (volledige sectie) | Volledig |
| 1.7.taak.1.doel.2 Referentiepunten + stakeholder-verwachtingen | Leerstuk 1 (COSO + ITAA-norm) + Leerstuk 5 (IIA + ISA) | Volledig |
| 1.7.taak.1.doel.3 Risico's opsporen | Leerstuk 2 (functiescheidings-risico's) + Leerstuk 3 (per cyclus) + Leerstuk 4 (risico-identificatie-methode) | Drievoudig — bewust over leerstukken verdeeld |
| 1.7.taak.1.doel.4 Evenwicht zekerheid/compliance | Leerstuk 1 (kosten-baten + 5 inherente beperkingen) + Leerstuk 2 (KMO-pragmatisme) + Leerstuk 4 (management override) | Volledig |
| 1.7.taak.1.doel.5 Interpreteren managementletter | Leerstuk 5 (sectie management letter ISA 265 + ernst-classificatie) | Volledig |
| 1.7.taak.1.doel.6 Aanbevelingen formuleren | Leerstuk 3 (per cyclus zwaktes → controle-aanbeveling) + Leerstuk 5 (SMART-framework + management letter follow-up) | Volledig |

| Kenniselement | Gedekt door | Notitie |
|---|---|---|
| 1.7.I.A definitie | Leerstuk 1 | Volledig |
| 1.7.I.B externe controle (afbakening) | Leerstuk 1 (kort) | Verwijst naar PO 1.6 |
| 1.7.I.C managementcontrole (afbakening) | Leerstuk 1 (kort) | Afbakening + verwijst naar PO 1.8 |
| 1.7.I.D + V.A interne audit | Leerstuk 5 | Volledig (één plek voor herhaalde concept) |
| 1.7.II (woordenschat) | Leerstuk 1 + 2 + 3 verspreid | Volledig (impliciet via context) |
| 1.7.III dubbele dimensie + doelen + redelijke zekerheid | Leerstuk 1 + Leerstuk 2 (preventief/detectief) | Volledig |
| 1.7.IV actoren en middelen | Leerstuk 1 (3 Lines-overzicht) + Leerstuk 5 (interne audit + auditcomité) | Volledig |
| 1.7.V audit (inclusief auditrisico's) | Leerstuk 5 | Auditrisico-model (inherent · controle · ontdekking) als info-box; diepere uitwerking in PO 1.6 |
| 1.7.VI fouten + fraude + verspilling | Leerstuk 4 | Volledig |
| 1.7.VII functiescheiding | Leerstuk 2 | Volledig (eigen leerstuk-status omdat programma er hoofdblok van maakt) |
| 1.7.VIII.A aanpak uitwerking | Leerstuk 3 (8-stappen-flow) | Volledig |
| 1.7.VIII.B taakverdeling | Leerstuk 2 | Volledig (zelfde concept als VII) |
| 1.7.VIII.C opvolging verrichtingen | Leerstuk 3 (per cyclus) | Volledig |
| 1.7.VIII.D controlemiddelen | Leerstuk 2 (taxonomieën) + Leerstuk 3 (per cyclus) | Volledig |
| 1.7.VIII.E geïnformatiseerde omgeving | Leerstuk 3 (IT-laag) | Volledig |
| 1.7.VIII.F evaluatie | Leerstuk 5 | Volledig |

**Bewuste keuzes**:
- **Auditrisico-model** (inherent · controle · ontdekking) krijgt info-box-status in leerstuk 5, geen eigen sectie — diepere uitwerking hoort in PO 1.6.
- **COSO ERM 2017** wordt vermeld in leerstuk 1 als "complementair aan IC 2013", maar krijgt geen apart blok — examen-relevantie is nul.
- **3 Lines of Defense** krijgt **mermaid-diagram** in leerstuk 1 (overzicht) + uitwerking 3e lijn in leerstuk 5.
- **Verbinding met WVV art. 7:96 / 7:99** (bestuursverantwoordelijkheid + auditcomité): claim te verifiëren via MCP in script-fase. Bij twijfel: vermelden als rakend met PO 3.0, niet doceren.

---

## 5. Voorbeeldgroep — voorstel

**Naam**: `bracke-instal` *(voorstel — nog vrij)*
**Locatie**: `data/voorbeeldgroepen/bracke-instal.yaml`

### Keuze-rationale

Interne controle als vak werkt het beste met een **middelgrote KMO met meerdere processen + meerdere medewerkers + een gangbaar ERP** — groot genoeg dat functiescheiding zinvol is, klein genoeg dat KMO-proportionaliteit relevant blijft. Geen geconsolideerde groep nodig (anders dan PO 1.4); geen fiscale complexiteit nodig (anders dan PO 2.x).

**Mock-onderneming**: **Bracke Installatie BV** — middelgrote Belgische installateur (HVAC + sanitair + elektriciteit voor renovatie- en nieuwbouwprojecten). 32 werknemers (8 administratief + 24 op de werf), 1 zaakvoerder + 1 mede-zaakvoerder, omzet 6,8 mln EUR (boekjaar 2025), balanstotaal 4,2 mln EUR. Werkt met **Odoo-ERP** + **TimeSquare-tijdregistratie** + **bank-koppeling Isabel 6**. Cliënten: 70 % B2B (algemene aannemers + property-developers) + 30 % particulier (renovatie). Gemiddelde projectgrootte: 25.000 EUR voor B2B (40 dagen doorlooptijd), 8.000 EUR voor particulier (10 dagen).

### Inhoud van de voorbeeldgroep-YAML

- **Bedrijfsprofiel**: bezetting + organogram + ERP-landschap + relevante KPIs (DSO 68 dagen / DPO 45 / voorraadrotatie magazijn 8×/jaar)
- **Organogram mermaid** — zaakvoerders → administratief (boekhouder · projectadministratie · receptie/aankoop) + technisch (werfleiders × 3 · monteurs × 24)
- **Bezetting-tabel** met expliciete rol-aanduidingen — wie kan wat in Odoo, wie heeft kassasleutel, wie tekent betaalopdrachten — bewuste **zwakke plekken in de huidige functiescheiding** voor didactische illustratie (bv. boekhouder Eline kan zowel leveranciers-master aanpassen als betaalbatches aanmaken — geen 4-ogen op betalingen onder 10.000 EUR — zaakvoerder doet zelf alle kasstortingen)
- **Per-cyclus walkthroughs (5 cycli)**:
  - **Aankoop**: bestelaanvraag werfleider → goedkeuring zaakvoerder (>5.000) → bestelling administratie → ontvangst magazijnier of werfleider → factuur-binnenkomst boekhouder → 3-way match (waar de match faalt is een case) → betaal-batch boekhouder → goedkeuring zaakvoerder of co-zaakvoerder (>10.000)
  - **Verkoop**: offerte werfleider → goedkeuring zaakvoerder → werkbon → eindfactuur projectadministratie → verzending klant → opvolging DSO door boekhouder
  - **Voorraad**: aankomst werf-spullen → magazijnier (centraal) of werfleider (decentraal) → cyclische telling — een geval van **voorraad-discrepantie van ca 18.000 EUR**
  - **Kas/treasury**: gedeeltelijk fysiek kas-systeem voor klein-kosten + bank-betalingen via Isabel 6 + creditcards-werfleiders
  - **Lonen**: TimeSquare-prikregistratie → goedkeuring werfleider → boekhouder → SD Worx export → betaling
- **Fraude-case (voor leerstuk 4)**: een **gewezen werfleider Bart** heeft 14 maanden lang fictieve materiaal-aankopen via een gefingeerde leverancier op zijn schoonbroer's BV doorgesluisd (totaal ca 47.000 EUR) — drie controle-zwaktes die dit mogelijk maakten + drie controles die het opgemerkt hadden
- **Mini-cases**:
  - Klantenfiches: nieuwe klant ingevoerd door verkoop met fout BTW-regime → factuur 21 % i.p.v. 6 % verlegd → BTW-rechtzetting (cyclus-leerstuk)
  - Spookmedewerker: ex-monteur kreeg 4 maanden door-betaald na ontslag (lonen-cyclus)
  - Kasbetaling-procedure voor klein onderhoud — actueel ad-hoc, te herontwerpen met min 2 functiescheidingen (leerstuk 2 examen-vraag)
  - Externe leveranciers-bevestiging steekproef (interne audit, leerstuk 5)
- **Mock-managementletter** van commissaris (fictief — Bracke is niet auditplichtig, maar krijgt review-opdracht): 3 IC-tekortkomingen geclassificeerd (1 significant deficiency rond functiescheiding boekhouder, 2 deficiencies rond magazijntelling en kasprocedure)
- **Voorbeeld-aanbevelingen** in SMART-formaat — input voor leerstuk 5

---

## 6. Themafiche-mapping (PO 1.7-specifiek)

**Bestaande themafiches** in `content/themafiches/` voor PO 1.7 (per `docs/leerstuk-status.md` Themafiche-migratie-inventaris):
- `interne-controle-frameworks.md` — COSO IC + ERM + 3 Lines + 4 doelstellingen + ontwerp-flow
- `functiescheiding-en-cyclus.md` — ACR-IH-leer + 5 cycli + IT-controles + walkthrough

**Beslissing — van-de-tafel-en-ervaring-van-PO-2.5-en-2.7**: themafiches **verwijderen** (geen migratie). Samenvatting wordt **from scratch** geschreven op basis van de gerendere leerstukken — niet via thematische merge van bestaande fiches. Reden: themafiche-format is dichter bij "spiekblad" en dupliceert wat in leerstukken al staat; samenvatting krijgt geheugen-kapstok-stijl (telegram + visueel dominant) volgens [`docs/samenvatting-schrijfregels.md`](samenvatting-schrijfregels.md).

**Bijkomende beslissing — `fouten-en-fraude-controle.md`** (in `content/themafiches/`): deze themafiche raakt PO 1.7 (leerstuk 4) maar wordt door PO 1.6 (controleopdracht) gedeeld via [[themafiches/controleopdracht-aanpak]]-referenties. Behandelen bij leerstuk-pakket PO 1.6 — niet hier. Indien overlap met PO 1.7-samenvatting: korte verwijzing naar PO 1.6-themafiche; geen duplicatie.

**Themafiche-verwijdering**: `git rm content/themafiches/{interne-controle-frameworks,functiescheiding-en-cyclus}.md` in de PO 1.7-commit. Backlink-scan: deze fiches worden in `content/studiemateriaal/1-7/index.md` §4 vermeld — die referentie schrijven we weg in dezelfde commit.

---

## 7. Minicursus-update (`content/studiemateriaal/1-7/index.md`)

De huidige `index.md` (versie 2026-05) is **inhoudelijk al goed** maar **werkt nog met cluster-themafiches**. Aanpassingen per ADR-036/039/041:

### §1 — Waarom dit vak?
Behouden zoals nu — verhaal over "bestuur ontwerpt, externe auditor toetst". Bredere-programma-tabel: WVV-verwijzing nakijken op accuraatheid (art. 7:96 vs 7:99 vs 9:96).

### §2 — Wat is dit vak?
Behouden + per sub-sectie wikilink toevoegen naar het leerstuk dat het uitwerkt:
- "Het probleem" + "De oplossing" → context voor [[wat-is-interne-controle-en-coso]]
- "Het werkingsveld" → [[wat-is-interne-controle-en-coso]] (COSO + 5 componenten)
- "De bouwstenen" → [[functiescheiding-en-controlemaatregelen]] + [[cyclus-analyse-en-controlemiddelen]]
- "Wat doet de accountant hier?" → [[interne-audit-evaluatie-en-aanbevelingen]]

### §3 — Wat moet je kunnen + hoe pak je het aan
**Samenvoegen** van bestaande §3 (Kern/Rakend per rol) + §4 (Studie-aanpak) zoals in PO 1.4/2.1/2.5/2.7 — vervang de losse-concept-lange-lijst door een **leerstuk-leesroute in 5 stappen**:

1. Begin met [[wat-is-interne-controle-en-coso]] — de kapstok: 4 doelen + 5 componenten + redelijke zekerheid
2. Dan [[functiescheiding-en-controlemaatregelen]] — drie taxonomieën die de examen-vragen 80 % van de tijd toetsen
3. Dan [[cyclus-analyse-en-controlemiddelen]] — het werkpaard, vooral verkoop + aankoop + kas
4. Dan [[fouten-fraude-en-risicobeheersing]] — de risico-architectuur die het hele systeem stuurt
5. Sluit af met [[interne-audit-evaluatie-en-aanbevelingen]] — wie evalueert + hoe rapporteer je IC-tekortkomingen

**Drie-rollen-paragraaf behouden** (bedrijfsleider · interne auditor · externe auditor) — maar verkort + verwijzend naar de leerstukken i.p.v. lange concept-lijst.

### §4 (oud) → wordt "Voor herhaling"
Themafiche-tabel verwijderen; vervangen door verwijzing naar [`samenvatting.md`](samenvatting) (Quartz-wikilink). Eén regel: "Wanneer de stof gezien is, gebruik je de [[samenvatting]] (3-4 A4 printbaar) voor de laatste sprint voor het examen."

### §5 → "Actief testen — oefening" (nieuw, indien oefening gemaakt)
Korte alinea + wikilink naar `oefening.md`.

### §6 — Examen-radar (was §5)
Behouden, tabel uitbreiden met de **20 unieke vraag-eenheden** uit het huidige voorbeeldexamenvragen.md (nu 17 in tabel — bijwerken naar wat in `voorbeeldexamenvragen.md` staat). Patroon-observatie versterken met de drie observaties uit §2 van dit skelet.

### §7 — Concepten cross-PO (was §6)
Behouden — bestaande tabel is correct.

### Verwijderingen
- Themafiche-sectie (§4 in huidige versie) volledig weg
- Lange concept-doorklik-lijst in §3 (oude versie) inkorten — leerstukken dragen die doorklik

---

## 8. Oefening — beslissing

**Voorstel: ja maken** — past hier goed. Een geïntegreerde IC-evaluatie-oefening kan steunen op meerdere leerstukken tegelijk en is realistisch werk-werk dat de stagiair in zijn eerste maanden als accountant zal moeten doen.

**Format-voorstel**: **IC-quickscan voor Bracke Installatie BV** in 5 stappen, 60-75 min:

1. **Cyclus-mapping** — voor 1 cyclus (aankoop) flowchart aanvullen en de 3 zwaktes in de huidige functiescheiding aanduiden (leerstuk 2 + 3)
2. **Classificatie-test** — 8 controle-activiteiten uit Bracke indelen volgens de 4-categorieën-typologie (Aut · Bew · Reg · Contr) — replica van examen 2013-2 maar op Bracke-cijfers (leerstuk 2)
3. **Risico-identificatie** — bij het aanmaken-van-klantenfiches-door-verkoop-bij-Bracke 3 risico's detecteren (leerstuk 3 + 4 — replica van examen 2014-1)
4. **Fraude-analyse** — de Bart-case (fictieve leveranciers) analyseren via fraudedriehoek + de drie zwaktes benoemen die het mogelijk maakten + de drie controles die het opgemerkt hadden (leerstuk 4)
5. **Managementletter-respons** — gegeven de mock-managementletter met 3 bevindingen, formuleer voor één bevinding een SMART-aanbeveling + actie-plan (leerstuk 5)

Output: één markdown-pagina `content/studiemateriaal/1-7/oefening.md` zonder hints in de opgave, drie pijlers (zie [`docs/oefening-procedure.md`](oefening-procedure.md)). Bracke-voorbeeldgroep wordt apart geconsumeerd — geen herhaling.

---

## 9. Open beslismomenten — voor de uitvoeringsronde

1. **Voorbeeldgroep**: `bracke-instal` (nieuwe groep, niet hergebruikt) — passend voor 5 cycli + IT + lonen.
2. **Leerstuk-granulariteit**: 5 leerstukken (1+2+3 vs 1+2+3+4+5 vs 6 — afgewogen, 5 lijkt optimaal). Geen verdere splitsing nodig — taxonomieën samen in leerstuk 2, evaluatie + audit + auditcomité samen in leerstuk 5.
3. **Cross-PO leerstuk?**: geen — alle 5 zijn PO-specifiek. Externe-controle-perspectief in leerstuk 5 verwijst naar [[1.6]] maar dupliceert geen werk.
4. **Themafiches**: verwijderen, niet migreren — samenvatting from-scratch.
5. **Oefening**: ja maken (5 stappen, Bracke-gebaseerd).
6. **Voorbeeldexamenvragen**: al gerendered (20 unieke vragen) — geen actie.
7. **Wettelijke verwijzingen-discipline**: WVV art. 7:96 (alarmbel / IC-verantwoordelijkheid bestuur) + 7:99 (auditcomité bij genoteerde + OOB) — bij script-fase MCP-verifieren. ISA 315 (herzien 2019) bijlage 3 §20-22 (preventief/detectief), ISA 240 (fraude), ISA 265 (communicatie IC-tekortkomingen), ISA 330 (responses to assessed risks), ISA 500/501 (controletechnieken/voorraad), ISA 610 (interne audit reliance) — primair via RAG `zoek_bronnen`. ITAA KMO-controlenorm (Bijlage 1 definities + §99-§101 functiescheiding-context) — beschikbaar via RAG.

---

## Lessen vooraf

- **PO 1.7 examineert classificatie en toepassing, niet theorie.** Vier doelstellingen + vijf COSO-componenten + drie taxonomieën (1234 · ACR-IH · prev/det/corr) zijn de toetssteen — niet "leg COSO uit in eigen woorden".
- **Functiescheiding is hier echt centraal** — niet voor niets eigen kenniselement-hoofdblok (VII). Drie aparte examen-jaren testen specifiek de classificatie van activiteiten naar functie-categorie.
- **Cyclus-aanpak vereist tactiel werk** — de Bracke-voorbeeldgroep moet rijke per-cyclus walkthroughs hebben, niet alleen abstracte risicotabellen.
