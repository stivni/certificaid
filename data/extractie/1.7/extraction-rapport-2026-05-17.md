# Extraction-rapport PO 1.7 (Interne controle) — concept-extractie-v4

**Run-id**: concept-extractie-v4-2026-05-17  
**Model**: claude-opus-4-7  
**Datum**: 2026-05-17  
**Schema**: ADR-007 v1.4  
**Output-locatie**: `data/concepten/records/`

---

## Samenvatting

| Metric | Aantal |
|---|---|
| Nieuwe records (primary = 1.7-anchor) | 53 |
| Bestaande records bijgewerkt (1.7-anchor toegevoegd aan `linked_anchors`) | 3 |
| Synthese-records (`node_type: synthese`) | 9 |
| Records die expliciet `confidence: inferred-common-knowledge` gebruiken | ~30 |
| Bron-gap-notities (vakdoctrine-claims zonder Belgische bron) | 22 |
| Anchors gedekt (van 58 in 1.7) | 58 (100%) |

---

## Nieuwe records

### Hoofdconcepten — begrippen en fenomenen (1.7.I, II, III, VI)

| Record | Primair anchor | Aanvullende anchors |
|---|---|---|
| `interne-controle` | 1.7.I.A | 1.7.I, II.E, III.A, III.B, IV, taak.1 |
| `externe-controle` | 1.7.I.B | 1.7.I, V.C |
| `managementcontrole` | 1.7.I.C | 1.7.I |
| `interne-audit` | 1.7.I.D / V.A | 1.7.V.B, V, IV |
| `onderneming-begrip-ic` | 1.7.II.A | 1.7.II |
| `informatiesysteem-onderneming` | 1.7.II.B | 1.7.II.C, II.D, II |
| `stromen-onderneming` | 1.7.II.C | 1.7.II, II.B |
| `informatie-kwaliteit-ic` | 1.7.II.D | 1.7.II |
| `controle-begrip-algemeen` | 1.7.II.E | 1.7.II |
| `controleproces-organisatie` | 1.7.II.F | 1.7.II.E, II |
| `ethiek-organisatie-ic` | 1.7.II.G | 1.7.II, III.A |
| `kenmerken-interne-controle` (synth) | 1.7.III | 1.7.III.A, III.B |
| `controle-omgeving` | 1.7.III.A | 1.7.III.B, III, XII.D |
| `fouten-en-fraude` (synth) | 1.7.VI | 1.7.VI.A, VI.B |
| `fouten-ic` | 1.7.VI.A | 1.7.VI |
| `fraude` | 1.7.VI.B | 1.7.VI |
| `verspilling` | 1.7.VI.C | 1.7.VI |

### Actoren + audit (1.7.IV, V)

| Record | Primair anchor | Aanvullende anchors |
|---|---|---|
| `actoren-interne-controle` (synth) | 1.7.IV | 1.7.V |
| `drie-lijnen-model` | 1.7.IV | 1.7.V, V.A, V.B |
| `functie-interne-auditor` | 1.7.V.B | 1.7.V.A, V |
| `externe-auditor-relatie-ic` | 1.7.V.C | 1.7.I.B, V |
| `auditcomite` | 1.7.V.D | 1.7.V, IV |
| `auditrisico-1-7-context` | 1.7.V.E | 1.7.V |

### Functiescheiding + uitvoering (1.7.VII, VIII)

| Record | Primair anchor | Aanvullende anchors |
|---|---|---|
| `functiescheiding` | 1.7.VII | 1.7.VIII.B, X.C |
| `uitvoering-interne-controle` | 1.7.VIII.A | 1.7.VIII, VIII.B, VIII.C, VIII.F, XIII |
| `taakverdeling-ic` | 1.7.VIII.B | 1.7.VII |
| `opvolging-verrichtingen-ic` | 1.7.VIII.C | 1.7.VIII |
| `beheersactiviteiten` | 1.7.VIII.D | 1.7.VIII, X.D |
| `controlemiddelen-ic` | 1.7.VIII.D | 1.7.VIII, X.D |
| `geinformatiseerde-omgeving-ic` | 1.7.VIII.E | 1.7.X, X.A, X.B, X.D |
| `evaluatie-interne-controle` | 1.7.VIII.F | 1.7.XI |
| `monitoring-interne-controle` | 1.7.VIII.F | 1.7.VIII.C, XI |
| `risico-inschatting-organisatie` | 1.7.XII.F | 1.7.XII.E, III.B |
| `informatie-en-communicatie-ic` | 1.7.II.D | 1.7.II.B, II |

### Cycli (1.7.IX)

| Record | Primair anchor | Aanvullende anchors |
|---|---|---|
| `cyclus-analyse-ic` (synth) | 1.7.IX | 1.7.IX.A-E |
| `aankoopcyclus-ic` | 1.7.IX.A | 1.7.IX |
| `productiecyclus-ic` | 1.7.IX.B | 1.7.IX |
| `verkoopcyclus-ic` | 1.7.IX.C | 1.7.IX |
| `hr-cyclus-ic` | 1.7.IX.D | 1.7.IX |
| `voorraadcyclus-ic` | 1.7.IX.E | 1.7.IX |

### Digitale ecosystemen (1.7.X)

| Record | Primair anchor | Aanvullende anchors |
|---|---|---|
| `cyberrisico-ic` | 1.7.X.A | 1.7.X, X.D |
| (zie `geinformatiseerde-omgeving-ic` voor X.B, X.C, X.D) | | |

### Evaluatiecriteria (1.7.XI)

| Record | Primair anchor | Aanvullende anchors |
|---|---|---|
| `evaluatiecriteria-ic` | 1.7.XI | 1.7.VIII.F |

### Referentiestelsels (1.7.XII)

| Record | Primair anchor | Aanvullende anchors |
|---|---|---|
| `wettelijk-kader-ic` (synth) | 1.7.XII.A | 1.7.XII.G, XII.H, XII |
| `isa-standaarden-ic` (synth) | 1.7.XII.B | 1.7.XII, V.E |
| `itaa-normen-ic` (synth) | 1.7.XII.C | 1.7.XII.G, XII |
| `coso-i-framework` | 1.7.XII.D | 1.7.XII |
| `coso-ii-erm-framework` | 1.7.XII.E | 1.7.XII.F, XII |
| `coso-componenten-synthese` (synth) | 1.7.XII.D | 1.7.III, III.B, VIII |
| `iso-31000-risicobeheer` | 1.7.XII.F | 1.7.XII |
| `klokkenluiderregeling` | 1.7.XII.A | 1.7.XII.H, VI.B |
| `avg-interne-controle` | 1.7.XII.A | 1.7.XII.H, X, X.A |

### Bijzondere verslagen (1.7.taak.1, 1.7.XIII)

| Record | Primair anchor | Aanvullende anchors |
|---|---|---|
| `bijzondere-verslagen-overzicht` (synth) | 1.7.taak.1 | 1.7.XIII |
| `inbreng-in-natura-verslag` | 1.7.taak.1 | — |

---

## Bestaande records bijgewerkt (PO 1.6 → ook 1.7-anchors)

| Record | Toegevoegde 1.7-anchors | Reden |
|---|---|---|
| `toetsing-interne-beheersing.json` | 1.7.V.C, 1.7.VIII.F, 1.7.XI | Test of controls is centraal in zowel externe audit (1.6) als evaluatie van IC (1.7) |
| `intern-beheersingsrisico.json` | 1.7.V.E, 1.7.III.B, 1.7.VIII.F | Concept overlapt audit-risico (1.6) en IC-eigenschappen (1.7) |
| `auditrisicomodel.json` | 1.7.V.E | Auditrisico's expliciet anchor 1.7.V.E |

---

## Anti-collision met PO 1.6 (audit-context)

Volgende PO 1.6-records werden bewust **NIET dupliceerd** voor PO 1.7 — ze zijn relevant maar overlappen met `linked_anchors`-uitbreiding (zie hierboven). Bij rendering van PO 1.7 zullen ze via wikilinks bereikbaar zijn:

- `auditrisicomodel.json` — IR × CR × DR
- `toetsing-interne-beheersing.json` — test of controls
- `intern-beheersingsrisico.json` — CR
- `inherent-risico.json` — IR (geen 1.7-anchor toegevoegd: minder direct)
- `ontdekkingsrisico.json` — DR (idem)
- `auditplanning.json` — planning context (geen 1.7-anchor: te audit-specifiek)
- `professioneel-kritische-instelling.json` — relevant voor fraude-detectie (1.7.VI.B), MAAR niet expliciet 1.7-anchor toegevoegd om scope-clean te houden
- `cijferanalyses-audit.json` — overlap met opvolging-verrichtingen (1.7.VIII.C) maar audit-specifiek geformuleerd
- `bedrijfsrevisor.json`, `gecertificeerd-accountant-ga.json` — actoren in externe controle, blijven 1.6-georiënteerd
- `onafhankelijkheid-externe-accountant.json` — wel relevant voor 1.7.I.B + 1.7.V.C maar via wikilink

**Beslissing**: 1.7-records die deze concepten nodig hebben verwijzen via `edges[]` of vrije tekst (`[[concept-id]]`) i.p.v. duplicatie. Drie records gekregen anchor-uitbreiding bovenop (zie tabel).

---

## Bron-gap-lijst — vakdoctrine-claims (confidence: inferred-common-knowledge)

PO 1.7 heeft **geen Belgische trusted bron** voor interne controle als discipline. COSO (US, privé sector), IIA (US, professional body), ISO 31000 (internationaal) en ACFE (US) leveren de primaire vakdoctrine. Volgende claims zijn als `inferred-common-knowledge` gelabeld zonder Belgische primaire bron:

| Concept / record | Bron-gap |
|---|---|
| COSO I 5 componenten + 17 principes (`coso-i-framework`, `interne-controle`, `controle-omgeving`, `risico-inschatting-organisatie`, `beheersactiviteiten`, `informatie-en-communicatie-ic`, `monitoring-interne-controle`, `coso-componenten-synthese`) | COSO 1992/2013 — US-vakdoctrine, geen Belgische omzetting |
| COSO II ERM framework (`coso-ii-erm-framework`) | COSO 2004/2017 — internationale vakdoctrine |
| ISO 31000 risk management (`iso-31000-risicobeheer`) | ISO-standaard, niet wettelijk in België |
| Drie-lijnen-model / Three Lines of Defense (`drie-lijnen-model`, `actoren-interne-controle`) | IIA 2013/2020 — vakdoctrine |
| Fraude-driehoek (Cressey, 1953) (`fraude`) | Vakdoctrine |
| ACFE fraude-typologie 3 types (`fraude`) | ACFE Report to the Nations — vakdoctrine |
| 'Functiescheiding 4 functies' (autoriseren/uitvoeren/bewaren/registreren) (`functiescheiding`) | Internationale audit-doctrine via COSO en ISA 315 — geen specifiek Belgisch wetsartikel |
| IT general controls + application controls (`geinformatiseerde-omgeving-ic`) | ISA 315 + cyber-vakdoctrine |
| Cycli-aanpak voor IC-analyse (`aankoopcyclus-ic`, `verkoopcyclus-ic`, etc.) | Audit-vakdoctrine, geen Belgische bron |
| ISA-standaarden (`isa-standaarden-ic`) | IFAC — geraakt via ITAA-normen, niet zelf trusted Belgische bron |
| Managementcontrole als discipline (`managementcontrole`) | Anthony/Simons vakdoctrine |
| Evaluatiecriteria design + operating effectiveness (`evaluatiecriteria-ic`) | ISA 315/330 vakdoctrine |
| Interne audit IIA-functieprofiel (`interne-audit`, `functie-interne-auditor`) | IIA Standards |
| 'Dubbele dimensie' IC (hard + zacht) (`interne-controle`, `kenmerken-interne-controle`) | Vakdoctrine |
| Risk appetite begrip (`coso-ii-erm-framework`) | COSO 2017 vakdoctrine |
| Cyber-risico-typologie (`cyberrisico-ic`) | IT-security-vakdoctrine; NIS-2 alleen genoemd |
| Auditcomité-functieprofiel detail (`auditcomite`) | WVV regelt bestaan voor OIB's; concrete invulling = vakdoctrine + Corporate Governance Code |

**Mitigatie**: in elk record waar zo'n claim staat is `confidence: inferred-common-knowledge`. Het `_provenance.inputs` is leeg of bevat alleen ITAA-norm-chunks die het concept generiek raken maar niet expliciet definiëren. `_provenance.bron_gap` veld bevat expliciete uitleg.

---

## Gegrond materiaal — waar Belgische bronnen WEL droegen

| Concept | Belgische bron |
|---|---|
| Definitie 'interne beheersing' (Bijlage 1) | ITAA-norm-kmo-controlenorm |
| Toetsing IC door externe auditor (§97-§98) | ITAA-norm-kmo-controlenorm |
| Auditor moet IC begrijpen (§6) | ITAA-norm-algemene-controlenorm |
| Externe controle — onafhankelijkheid + signature | KB plichtenleer art. 13, 17, 18 |
| Fraude — strafrechtelijk kader | Strafwetboek 2024 Boek 2 art. 479 (oplichting), art. 488 (informaticabedrog) |
| Klokkenluiderregeling | Wet 28 november 2022 |
| AVG/GDPR-verplichtingen | AVG + Wet 30 juli 2018 |
| Voorraadcyclus — jaarlijkse inventaris | KB 21.10.2018 |
| Bestellingen in uitvoering (waardering) | CBN 2012/15, 2016/14 |
| Inbreng in natura-verslag | WVV art. 5:7 / 7:7 |

---

## Schema 1.4 — veld-gebruik

| Veld | Aantal records |
|---|---|
| `definitie` (begrippen, actoren, fenomenen) | ~25 |
| `main_rule` (regels, beginselen) | 2 (klokkenluiderregeling, avg-interne-controle) |
| `doel` (methodes) | 6 |
| `verplichting` + `stappen[]` (procedures) | 8 |
| `bouwstenen[]` met v1.4-bloks | 10 records (kerncconcepten) |
| `voorbeeld_inline` (cast-namen) | ALLE 53 nieuwe records |
| `vergelijkingsparen[]` (echte verwarring-risico) | 8 |
| `edges[]` met types | 53 (allen) |
| `node_type: synthese` met `vergelijkingstabel` | 9 |
| `gebaseerd_op_concepten` (synthese) | 9 |
| `beslisboom` (synthese) | 6 |
| `_provenance.bron_gap` (expliciet) | 22 |

---

## Voorbeeld-minimum check (Regel 13)

| Node-type | Records | Voldoen aan minimum |
|---|---|---|
| `begrip` / `fenomeen` | 28 | ALLE — `voorbeeld_inline` aanwezig |
| `methode` | 6 | ALLE — `bouwstenen[*].voorbeeld_inline` aanwezig |
| `procedure` | 8 | ALLE — stappen[*].hoe + voorbeeld aanwezig in minstens één stap |
| `actor` | 3 | ALLE — `voorbeeld_inline` met rol-context |
| `synthese` | 9 | ALLE — `vergelijkingstabel` + `voorbeeld_inline` |
| `regel` | 2 | ALLE — `voorbeeld_inline` |

---

## Cast-namen check (Regel 7)

Alle records gebruiken namen uit `data/concepten/casts/globaal.yaml`. Centrale cast voor 1.7:
- **Yperse Werkplaats BV** (productie-KMO, intern-controle-systeem) — gebruikt in 48 records
- **Xenon Expertise BV** (advies-/IC-firma) — gebruikt in 8 records
- **Rotex Roeselare NV** (grote NV, beursgenoteerd) — gebruikt in 18 records (voor formele IC-context met auditcomité, IA)
- **Wolters & Partners CVBA** (audit-firma) — gebruikt in 6 records
- **Sofie Janssens** (interne auditor / commissaris) — gebruikt in 14 records
- **Pieter Vermeulen** (zaakvoerder/voorzitter RvB) — gebruikt in 9 records
- **Marleen De Cock** (Risk Officer) — 3 records
- **Robert Vandenberghe** (niet-uitvoerende bestuurder met financiële expertise) — 1 record
- **Tom Lefèvre** (inkoper/aankoopdirecteur) — 3 records
- **Meubelzaak Mertens BV** (kleine handelsBV) — 2 records voor KMO-uitdagingen
- **Praktijk Persenaire** (eenmanszaak) — 2 records voor extreme KMO

Geen "M / D / X / Y / ABC" abstracties.

---

## Bedragen-format check (Regel 14a)

Alle bedragen gebruiken € prefix + Belgische duizendtal-puntnotatie. Voorbeelden:
- `€ 25.000`, `€ 850.000`, `€ 5.000.000`, `€ 95.000.000`, `€ 280.000`

---

## Open observaties / TODOs

1. **Reglementsteksten 1.7.XII.H** ("Wets- en reglementsteksten") — verzameld in `wettelijk-kader-ic` als synthese; geen apart deelrecord per wet/reglement omdat de meeste hun primaire wettelijke domein in andere PO's hebben (WVV in 1.4, plichtenleer in 1.6).

2. **Anchor 1.7.XIII** (Organisatie en evaluatie IC in kader van specifieke verrichtingen) — gedekt door `bijzondere-verslagen-overzicht` + `inbreng-in-natura-verslag`. Andere specifieke verrichtingen (fusie/splitsing IC, ontbinding IC) zijn beter geplaatst in PO 1.10/1.11 records.

3. **Geen apart record voor:**
   - 1.7.X.B (Fysieke beveiliging) — opgenomen als sectie in `geinformatiseerde-omgeving-ic`
   - 1.7.X.C (Functiescheiding IT) — opgenomen als sectie in `functiescheiding` + `geinformatiseerde-omgeving-ic`
   - 1.7.X.D (Controlemaatregelen IT) — opgenomen als sectie in `geinformatiseerde-omgeving-ic` + `controlemiddelen-ic`
   
   Reden: 3-cross-refs-eis voor eigen record (ADR-007 §Granulariteit) niet gehaald; alle inhoud past in bouwstenen.

4. **Sub-anchor 1.7.XII.G** (Gereglementeerde beroepen) — niet apart record; gedekt door wikilinks naar bestaande PO 1.6 records `bedrijfsrevisor.json`, `gecertificeerd-accountant-ga.json`, `commissaris.json`.

5. **Mogelijke nieuwe bronnen voor toekomstige passes**:
   - COSO Framework Executive Summary (publiek beschikbaar, NL-vertaling soms in vakliteratuur) — zou veel `inferred-common-knowledge` naar grounded verschuiven
   - IIA Standards (NL-vertaling beschikbaar via IIA Belgium)
   - Belgische Corporate Governance Code 2020 (volledige tekst publiek)
   - NIS-2 omzettings-wet (federaal, sinds 2024) — kan cyberrisico-record verrijken

Geadviseerd: bron-voorstel toevoegen aan `data/extractie/_bron_voorstellen.json` voor de bovenstaande items.

---

## Validatie

Alle records voldoen aan:
- ✓ `schema_version: "1.4"`
- ✓ `status: "seed"`
- ✓ `linked_anchors[]` bevat minstens primair anchor + dekkende anchors
- ✓ `_provenance.anchor_id` ingevuld
- ✓ `_provenance.dekt_ook_anchors[]` ingevuld waar relevant
- ✓ Geen wetsartikelnummers verzonnen — alle ingenomen claims hebben grondslag in chunk of zijn `inferred-common-knowledge`
- ✓ Cast-namen uit `globaal.yaml`
- ✓ Bedragen met € prefix + duizendtal-punt
- ✓ Edges met types (onderdeel-van / vergelijkt-met / vereist-kennis-van / getriggerd-door / specialisatie-van)
- ✓ Vergelijkingsparen alleen bij echte verwarring-risico (test: heeft een examen-keuze-trigger)
