# ADR-025 — Schema 2.0: didactische concept-laag

**Status**: Draft
**Datum**: 2026-05-21
**Laatste revisie**: 2026-05-21 — §4 rol-set herzien van 7 naar 5 rollen (vóór bulk-extract); `eigen-kantoor`-perspectief toegevoegd
**Vervangt deels**: ADR-007 schema 1.5/1.6 (didactische top-laag + element-vocabulaire + nieuwe kinds)
**Bouwt op**: ADR-007 (conceptmodel), ADR-008 (concept-extractie), ADR-019 (records-API)
**Gerelateerd**: ADR-010 (drie lagen + collapsibility), ADR-006 (RAG-strategie)

---

## Context

In een sparring-cyclus 2026-05-20/21 zijn acht concept-mockups uitgewerkt in `content/experiment/` om empirisch te valideren wat ontbreekt in schema 1.5/1.6. De resultaten leggen drie systemische tekortkomingen bloot in de huidige concept-laag:

1. **Descriptief, niet prescriptief** — records beschrijven *wat X is*, niet *wat een stagiair-GA met X moet doen voor een klant*. Het examen + de praktijk toetsen het laatste.
2. **Geen taal voor adviezen-as** — `in_praktijk` is gedefinieerd als "vertaal definitie naar stagiair-Nederlands". Daar ontbreekt: wanneer kies je dit · voor wie · wanneer niet · risico/voordeel voor klant · economische substantie in mensentaal.
3. **Geen kader-laag** — generieke principes (jaarrekeninganalyse-discipline, uitkeringsalternatieven-keuze, financieringsstructuur) worden in elke specifieke fiche herhaald of weggelaten. Synthese-records zijn een patch maar dekken niet de kader-rol.

Daarnaast bleek tijdens de mockups dat **de huidige zes node-types overloaded zijn** (`cluster` is een vergaarbak voor instrumenten, operaties, regimes, kader-concepten) en dat de **boekhoudkundige verwerking systematisch slecht gepositioneerd is**: of in onderdelen (waar ze conceptueel onnodig zijn) of in een Perspectieven-blok dat niet expliciet de accountant-rol noemt.

Mockups online ter referentie:
- `content/experiment/obligatielening-v7.md` (kanoniek instrument)
- `content/experiment/solvabiliteitsratio-v2.md` (kanoniek ratio)
- `content/experiment/jaarrekeninganalyse-v1.md` · `uitkering-aan-aandeelhouders-v1.md` · `lange-termijn-financiering-v1.md` (kader)
- `content/experiment/leasing-v1.md` (familie) + financiele/operationele-leasing (leden)
- `content/experiment/vvprbis-v1.md` (fiscale regeling) · `inkoop-eigen-aandelen-nv-v1.md` (operatie)

---

## Beslissing

Schema 2.0 — vier samenhangende wijzigingen.

### 1. Didactische top-volgorde (verplicht)

Elk record volgt deze vaste volgorde van top-secties. Sommige zijn kind-afhankelijk leeg.

| # | Sectie | Verplicht? | Doel |
|---|---|---|---|
| 1 | **Definitie** (kort, 1–2 zinnen) | ja | "Wat is dit?" / "Waar spreken we over?" |
| 2 | **Wat er economisch echt gebeurt** | ja | Mensentaal · substance over form |
| 3 | **Voorkennis & leespad** | aanbevolen | Voorvereisten · kader · naaste · volgkennis |
| 4 | **Wanneer kies je dit?** | bij kiesbare instrumenten/operaties | Voor wie · wel · niet · hoofdrisico · hoofdvoordeel |
| 5 | **Hoe het werkt** | ja | Onderdelen recursief (concept-laag) |
| 6 | **Rol van de accountant** | ja indien rollen relevant | Perspectief × rol (uitvoering-laag) |
| 7 | **Veelvoorkomende verwarringen** | aanbevolen | Verward met · expliciet kenbaar |
| 8 | **Alternatieven (zelfde doel)** of **Familie & alternatieven** | bij kiesbare | Kader-link + buren |
| 9 | **Wat dit record dekt** | aanbevolen | Competenties (chronologisch) + termen (alfabetisch) + formules + regimes |
| 10 | **Bronnen en verwijzingen** | ja | ⚖️ grounded · ⚠️ te verifiëren · edges |

Render-laag toont secties als h2-koppen; collapsibility per sectie staat aan (ADR-010 §collapsibility — uit te werken bij render-update).

### 2. Element-vocabulaire (`inhoud_type` + `weergaven`)

Een onderdeel of rol-cel bevat *elementen* — ieder met een **inhoud-type** (wat is het conceptueel) en één-of-meer **weergaven** (hoe tonen we het).

**Inhoud-types** (semantiek; mag groeien):
```
begrip · procedure · stap · voorwaarde · drempel · regel · uitzondering
· vuistregel · mechanisme · keuze · risico · formule · berekening
· vergelijking · principe · valkuil
```

**Weergave-types** (presentatie; mag groeien):
```
proza · tabel · boeking · balans-snapshot · resultatenrekening-snapshot
· t-rekening · beslisboom · stappenlijst · tijdslijn · vergelijkingstabel
· formule-expressie · diagram · casus
```

JSON-vorm:
```json
{
  "element_id": "disagio-bij-uitgifte",
  "inhoud_type": "mechanisme",
  "titel": "Disagio (uitgifte beneden pari)",
  "beschrijving": "...",
  "confidence": "grounded|inferred|vuistregel|te_verifieren",
  "bron": { "type": "kb", "ref": "KB-WVV#art-3-37" },
  "weergaven": [
    { "type": "berekening", "content": { ... } },
    { "type": "boeking", "rekeningen": [ ... ] },
    { "type": "balans-snapshot", "actief": [...], "passief": [...] }
  ]
}
```

Render kiest per weergave-type de juiste component. Eén concept-eenheid (bv. "disagio") kan dus vier weergaven tonen onder één titel — niet vier losse rubrieken zoals in schema 1.5.

### 3. Nieuwe kinds (functionele specialisatie binnen `node_type`)

Naast de zes bestaande `node_type`'s (begrip · regel · cluster · synthese · autoriteit · competentie) krijgt elk record een **`kind`-tag** die functioneel typeert. Schema 2.0 erkent:

| Kind | Wat is het | Voorbeelden |
|---|---|---|
| `instrument` | Financieringsvorm · belegging · structureel ding | obligatielening · banklening · BV · holding |
| `operatie` | Eenmalige handeling met boekhoudkundig gevolg | inkoop-eigen-aandelen · kapitaalverhoging · fusie |
| `procedure` | Wettelijke stappensequentie | gerechtelijke-reorganisatie · vereffening |
| `regime` of `fiscale-regeling` | Tariefmechanisme met voorwaarden | VVPRbis · DBI · liquidatiereserve · EBITDA-regel · investeringsaftrek |
| `ratio` | Meting + interpretatie-drempels | solvabiliteit · current ratio · ROE |
| `kader` | Cross-cutting denkraam met eigen taken | jaarrekening (artefact + cyclus) · jaarrekeninganalyse · uitkering-aan-aandeelhouders · lange-termijn-financiering · boekhoudbeginselen-discipline · waarderingsregels-discipline |
| `familie` | Groep verwante leden + onderscheidingscriteria | leasing (financieel/operationeel/renting) |
| `balanspost` | Boekhoudkundige rubriek per balansgroep — eigen waardering · presentatie · auditor-discipline | oprichtingskosten · materiële-vaste-activa · voorraden · eigen-vermogen · voorzieningen · overlopende-rekeningen |
| `begripscluster` | Verzameling samenhangende begrippen zonder operationeel karakter | (overloaded `cluster` gevallen die geen instrument/operatie/balanspost zijn) |

**Balanspost-kind toegevoegd (2026-05-21)**: na POC-validatie via `content/experiment/oprichtingskosten-v1.md`. Kenmerkend skelet: MAR-rubriek · componenten · waarderingsregels (verwijst naar `waarderingsregels-discipline`-kader) · afschrijving/wijziging · verplichting in toelichting · netto-actief-toets-interactie (waar van toepassing) · fiscaal aspect · rol-perspectief.

**Jaarrekening als kader** (2026-05-21): één-fiche-aanpak gevalideerd via `content/experiment/jaarrekening-v1.md`. Kader bevat: artefact-componenten (balans · resultatenrekening · toelichting · sociale balans · jaarverslag) · formaten (volledig · verkort · micro) + groottecriteria · cyclus (8 stappen) · waarderingsregels-bijlage. Splitsing in `artefact` + `procedure` werd verworpen (cross-link-flikkering).

**Kind als tag-set** (open, geen enum-validatie): bij twijfel mag de agent een nieuw kind voorstellen via VERIFY-flag. Schema-validator waarschuwt bij onbekend kind, blokkeert niet.

### 4. Rol × perspectief structuur (verplichte sectie bij toepasselijke kinds)

`rol_van_de_accountant` wordt een **gestructureerde matrix**, niet een vrije lijst. Twee niveaus:

- **Perspectief** (wie zit aan de andere kant van de tafel — of: voor wiens kantoor werkt de accountant). Twee soorten:
  - **Klant-type-perspectieven** — typisch 2–4 per record: uitgever · belegger NP · belegger venn. · auditor (extern) · bestuur · KMO-handelsonderneming · familiale holding · beursgenoteerde onderneming · vzw · …
  - **`eigen-kantoor`-perspectief** (toegevoegd 2026-05-21) — de accountant past iets toe op zijn eigen praktijk, niet op een cliënt. Vooral PO 4.0-relevant: AWW-eigen-kantoor-procedures, ITAA-deontologie-naleving, ITAA-kwaliteitstoetsing, GDPR-eigen-kantoor. Voor concepten waar de accountant zélf onderhevig is aan een regeling.
- **Rol** binnen dat perspectief — uit een **vaste set van 5** (revised 2026-05-21):
  - **`adviseur`** — strategisch/operationeel advies + begeleiding (algemeen toepasbaar; inclusief klant-begeleiding bij insolventie of faillissement)
  - **`boekhouder`** — boekings-uitvoering, MAR-toepassing, jaarrekening-opmaak (PO 1.1/1.2; ook afsluitende rekeningen voor curator bij faillissement)
  - **`externe auditor`** — commissaris-mandaat, assurance-opdrachten, controleverklaring; inclusief fraude-detectie-verantwoordelijkheid (ISA 240) en frauderisico-evaluatie (PO 1.6)
  - **`interne-controle-adviseur`** — interne-controle-systemen ontwerpen of evalueren voor cliënt. **Niet de in-house interne-audit-functie zelf** (PO 1.7)
  - **`fiscaal adviseur`** — fiscaal advies + aangifte-opmaak + fiscale procedure (PO 2.x)

Geen aparte rollen voor compliance, curator, of forensisch werk:
- **Compliance-werk**: AWW-cliëntonderzoek (`adviseur` of `externe auditor`) of AWW-eigen-kantoor (perspectief `eigen-kantoor` × `interne-controle-adviseur`)
- **Curator** is een externe actor in faillissement-context, geen rol-van-de-accountant. Wat de accountant doet bij klant-faillissement valt onder `adviseur` of `boekhouder`
- **Forensisch** werk binnen audit-mandaat valt onder `externe auditor` (ISA 240); specialistische forensische opdrachten buiten de basis-rol-set worden in body vermeld waar relevant

Per cel: takenpakket + elementen (recursief; mag boekingen + balans-snapshots + berekeningen bevatten). Lege cellen worden niet getoond.

JSON-vorm:
```json
"rol_van_de_accountant": {
  "perspectieven": [
    {
      "actor": "vennootschap-uitgever",
      "emoji": "🏢",
      "rollen": [
        {
          "rol": "adviseur",
          "emoji": "🎯",
          "taken": ["keuze instrument vs alternatieven", "structuur-advies", "..."],
          "elementen": [ ... ]
        },
        { "rol": "boekhouder", "emoji": "📋", "elementen": [ ... ] }
      ]
    },
    {
      "actor": "eigen-kantoor",
      "emoji": "🏛️",
      "rollen": [
        {
          "rol": "interne-controle-adviseur",
          "emoji": "🛡️",
          "taken": ["KYC-procedures eigen kantoor", "UBO-register-update", "..."],
          "elementen": [ ... ]
        }
      ]
    }
  ]
}
```

**Vuistregel "voor wie werkt de accountant"** als extract-heuristic — agent vraagt zich bij elk concept af welke perspectieven raken (klant-types + evt. `eigen-kantoor`) + welke rollen binnen elk perspectief zinvol zijn. Geen lege cellen.

**Render-implicatie**: bij de samenvatting van PO 1.6 (externe controle) wordt automatisch elk record met cel `rol=externe-auditor` opgenomen; voor PO 1.7 (interne controle): elk record met cel `rol=interne-controle-adviseur`. Voor PO 4.0: elk record met perspectief `eigen-kantoor`. Dat maakt PO-samenvattingen deterministisch te genereren uit de fiche-set.

### 4bis. Naming- en consolidatie-regels (toegevoegd 2026-05-21 na empirische skeleton-fase)

De eerste skeleton-pass over 19 programmaonderdelen leverde 425 kandidaten op, waarvan ~30 duplicaten, fluffy meta-kaders of pair-trap-overtredingen. Onderstaande regels zijn de **lessen-leerlingen** geformaliseerd als guidelines voor alle skeleton/extract/verify-passes.

#### Regel 1 — Fiche-naam = concept-naam, niet kind-naam, niet bron-naam

- **GEEN kind-suffix in `fiche_id`**: schrap `-kader`, `-familie`, `-procedure`. De kind staat in frontmatter (`node_type`). Voorbeeld: `registratiebelasting-kader` → `registratiebelasting`.
- **Bron-referenties (IAS-X, IFRS-X, ISA-X) horen in body als bron, niet in fiche-naam**. Het concept zit *verborgen* in de bron — de fiche dekt het concept. Voorbeeld: `ifrs-15-opbrengsten` → `opbrengstverantwoording` (met IFRS-15 als bron in body); `ias-2-voorraden-ifrs` → merge in bestaande `voorraden` met IFRS-perspectief.
- **Uitzondering**: als de bron *letterlijk* het concept IS, dan mag het. Voorbeeld: `ifrs` (= de EU-Verordening + Conceptueel Framework als koepelconcept).

#### Regel 2 — Pair-trap: één fiche met vergelijkingsmatrix is de default

- Bij varianten op één concept (NV/BV, drie gewesten Vl/Br/Wa, BGAAP/IFRS, …): **één fiche met perspectief-uitsplitsing inside**, niet aparte fiches per variant.
- Splitsen alleen als één variant écht zoveel complexiteit toevoegt dat de hoofdfiche onleesbaar wordt.
- Beslissing om te splitsen valt niet *vooraf* (in skeleton) maar *post-hoc* (via VERIFY of mens-review).
- Default flow: **prefer merge, split alleen als VERIFY of mens-review besluit "te verschillend"**.

#### Regel 3 — Rol × perspectief is de kapstok voor "wat doet de accountant"

- "Hoe doet de accountant X" → rol×perspectief-cel **IN het X-fiche**, niet als aparte `audit-X`-fiche of `aangifte-X`-fiche.
- Specifiek voorbeeld: `audit-van-geconsolideerde-jaarrekening` werd in skeleton als losse procedure-fiche voorgesteld; correct is: cel `externe auditor × consolidatie-perspectief` IN `geconsolideerde-jaarrekening`.
- "Wat doet de accountant zelf" (AWW eigen kantoor, ITAA-deontologie-naleving, GDPR-eigen-kantoor): perspectief `eigen-kantoor`, geen aparte rol of fiche.

#### Regel 4 — Families krijgen leden-edges in dezelfde pass

- Een familie zonder `heeft_lid`-edges is incompleet en onleesbaar.
- Schrijf familie + leden + edges in één extract-pass (niet later).
- Vermijd "ghost families" zoals `controlemaatregelen` zonder gedefinieerde leden.
- Edges via `heeft_lid` op familie + `lid_van` op elke lid (bidirectioneel).

#### Regel 5 — Granulariteit: grover-is-beter, split alleen als nodig

- Bouwstenen van een concept horen **in** het ouder-concept, niet als losse meta-kaders.
- Voorbeeld: `doelstellingen-financiele-analyse` + `instrumenten-financiele-analyse` zijn onderdelen van `jaarrekeninganalyse`, geen aparte kaders.
- Een fiche dat alleen "wat het is" zonder eigen mechaniek of domein-werking = **signal voor merge** in een groter concept.
- Per-PO richtsnoer: ~20-25 fiches, niet 40+. Overschrijding is OK als het PO inhoudelijk dat vereist (BTW kan ~30 zijn door fragmentatie van regimes).

#### Regel 6 — Cross-PO-completeness in eerste extract-pass

- Bij eerste aanraking van een concept: **ALLE PO-perspectieven** (boekhoud + fiscaal + audit + advies + eigen-kantoor) in één extract-pass.
- Latere PO's die hetzelfde concept raken: vullen aan via `aanvul_kandidaat`, schrijven geen aparte fiche.
- Reden: latere re-extracten zijn duurder dan grondig eerste werk.

#### Regel 7 — Open `kind` tag-set, met discipline

- Nieuwe `kind`-waarden zijn toegestaan (open tag-set).
- Worden voorgesteld via VERIFY-flag of expliciete rationale in extract-output.
- Schema-validator waarschuwt bij onbekend kind, blokkeert niet.
- Tijdens skeleton: gebruik bestaande set tenzij echt nieuw type concept; anders explicieten in motivatie.

#### Regel 8 — Schema-jargon blijft in frontmatter

- `kind`, `linked_anchors`, `node_type`, `_provenance` enzovoort: alleen in frontmatter, nooit in body-tekst.
- In body-tekst gebruik je gewone Nederlandstalige termen ("Dit kader beschrijft …" — niet "Deze kader-node valt onder PO 1.6.II.A").
- PO-codes (1.6.II.A) blijven in frontmatter; render-laag bouwt PO-navigatie automatisch.

#### Toepassings-loop

| Fase | Toepassing |
|---|---|
| **Skeleton-voorstel** | Volg regels 1-7 preventief tijdens skeleton-fase (skeleton-voorstel-v1.md) |
| **Concept-extractie** | Volg regels 1-8 tijdens record-schrijven (concept-extractie-v5.md) |
| **VERIFY** | Detecteer overtredingen + voorstel consolidatie of split (concept-verify-v3.md) |
| **Mens-review** | Bevestig of weerleg merge/split-voorstellen na VERIFY |

### 5. Confidence-vocabulaire (uniform)

| Token | Betekenis | Visueel |
|---|---|---|
| `grounded` | Direct uit wet/KB/CBN/norm | ⚖️ |
| `inferred` | Redenering uit combinatie bronnen | 🔗 |
| `vuistregel` | Beroepswijsheid, geen harde regel | 🧭 |
| `te_verifieren` | Bron ontbreekt of nog te checken | ⚠️ |
| `tegenstrijdig` | Bron is gevonden en spreekt de claim **tegen** — fix vereist | ❌ |

In JSON: string-veld `confidence` per element/claim. In markdown-render: emoji-prefix.

**Verschil ⚠️ vs ❌**: ⚠️ = nog niet gecheckt (mogelijk OK); ❌ = gecheckt en fout volgens bron. ❌ is een actie-eis voor de volgende refinement-pass, geen wachtwoord.

**🧭-gradatie**: vuistregel toegestaan voor *strategisch advies* (wanneer kies je · voor wie · hoofdrisico/voordeel · speelruimte · valkuilen-in-uitvoering) — niet voor *procedures · cijfers · wettelijke voorwaarden · rekening-codes · tarieven*. Daar geldt: ⚖️ of ⚠️ (of ❌ als bron tegenspreekt).

### 6. Nieuwe edges

Aan de zeven canonieke edges (ADR-007) worden toegevoegd:

| Edge | Richting | Wanneer |
|---|---|---|
| `lid_van` | specifiek → familie/kader | Een lid in een familie of kader |
| `heeft_lid` | familie/kader → specifiek | Omgekeerd (auto-afgeleid in render) |
| `beïnvloed_door` | concept → fiscale-regeling | Concept wordt gemodificeerd door een regeling |
| `beïnvloedt` | regeling → concept | Omgekeerd |
| `is_uitzondering_op` | specifiek → algemene-regel | Cursus-waarde × 10 mechanisme |
| `verward_met` | concept → ander-concept | Veelvoorkomende verwarring |
| `valt_onder_kader` | concept → kader | Welk kader het concept overstijgt (synoniem voor `lid_van` waar `lid` ongepast voelt) |

**`heeft_lid` is niet-transitief in data, transitief in render**. Kader declareert alleen direct-onder-hem; render-laag traverseert recursief voor "alle eindbladen"-views.

### 7. Voorkennis & leespad

Elk record krijgt optionele velden voor pedagogische navigatie:

```json
"voorkennis_leespad": {
  "voorvereisten": ["concept-id", ...],
  "kader": "kader-id",
  "naast_relevant": [...],
  "volgkennis": [...]
}
```

Geen anchor-codes of PO-referenties in body. `linked_anchors[]` blijft in frontmatter/metadata; render-laag bouwt PO-navigatie eruit op.

### 8. "Wat dit record dekt"

Verplichte slotsection met:
- `competenties_chronologisch[]` (volgorde van uitvoeren)
- `termen_alfabetisch[]` (verwijzingen naar interne anchors)
- `formules[]`
- `regimes[]` (links naar gerelateerde fiscale regelingen)

Schaalbaar: render-laag aggregeert deze data over alle records per PO-anchor → automatische PO-leerpad-navigatie.

---

## Migratie van schema 1.5/1.6 → 2.0

**Beslissing: opnieuw extracten, niet 1-op-1 converteren.**

Rationale: rol × perspectief structuur + element-vocabulaire + economische substantie + accountant-bril zijn niet uit 1.5-velden af te leiden. Een transformer zou een lege rol-sectie produceren of velden raden. Beter: gebruik oude records als **enriched seed** voor EXTRACT v5.

Concreet:
1. Oude records → `data/concepten/_archive/v1.x/` (read-only)
2. EXTRACT v5 gebruikt archief-records + RAG + anchors + bestaande edges als seed
3. Nieuwe records geschreven in 2.0-formaat naar `data/concepten/records/`
4. `schema_version: "2.0"` in elk nieuw record
5. Records-API validator herkent zowel 1.5/1.6 als 2.0 tijdens overgangsperiode; nieuwe writes verplicht 2.0
6. Wave-planning per PO (ADR-008 §18.7) bepaalt volgorde

**Tijdsdoel**: Fase 2 binnen 24–36 u via parallelle subagent-fleet (één agent per record-batch). Verifieerbaarheid via VERIFY v3 als zachte guideline-pass.

---

## Backward compatibility

- `node_type` blijft (zes bestaande types); `kind` is additief
- Bestaande edge-types blijven; nieuwe edges zijn additief
- Bestaande velden (`definitie`, `bouwstenen`, `in_praktijk`, …) blijven leesbaar; in 2.0 worden ze gedeprecieerd ten gunste van de nieuwe top-volgorde
- `linked_anchors[]` blijft de fine-granular metadata-laag (anchor > PO)

Records-API krijgt validator-functie `valideer_schema_versie(record)`. Bij `schema_version == "2.0"`: nieuwe top-volgorde-check + element-vocabulaire-check + rol × perspectief-check (alle drie als warnings, niet als blockers — guideline-discipline).

---

## VERIFY v3 — guidelines, geen blockers

VERIFY werkt voortaan als **soft advisor**:
- Vlagt afwijkingen van schrijfregels als suggesties, niet als fouten
- Detecteert hallucinaties via RAG-cross-check (claim niet aantoonbaar uit bron-chunks)
- Vlagt te-veel-🧭 (drempel: > 40 % vuistregel-claims per record)
- Vlagt ontbrekende voorbeelden bij kinds waar voorbeelden essentieel zijn (ratio · operatie · instrument)
- Schrijft suggesties naar `data/extractie/gaps.json` met severity `suggestion` (nieuw) i.p.v. `blocker`

EXTRACT v5 mag VERIFY-suggesties negeren als er reden is — beslissing wordt in record-`_provenance.verify_overrides` gelogd.

Volledige guidelines: zie `prompts/concept-verify-v3.md`.

---

## EXTRACT v5

Nieuwe extract-prompt: `prompts/concept-extractie-v5.md`. Belangrijkste wijzigingen t.o.v. v4:

- **In-context referentie-fiches**: agent krijgt 3–4 mockups uit `content/experiment/` als templates
- **Verplichte sectie-volgorde** + element-vocabulaire-instructies
- **Cross-PO-completeness**: bij eerste aanraking van een concept (bv. obligatielening in PO 1.1) worden ALLE perspectieven + alle relevante PO-doorsneden in één pass behandeld — geen "skeleton nu, fiscaal later"
- **Familie/kader-detectie**: agent voorstelt familie- of kader-record als hij meerdere verwante records ziet ontstaan
- **Rol × perspectief heuristic**: "voor wie werkt de accountant" + "welke hoeden"
- **Confidence-gradatie-regel**: 🧭 alleen voor strategisch advies

---

## Renderlaag

Geen direct ADR-werk hier; bij start van Fase 2 wordt parallel een Quartz-component-update gestart in `tools/leermateriaal/templates/` voor:
- Collapsible secties (default open voor primaire, default dicht voor secundaire details)
- Element-vocabulaire-renderers (per weergave-type een component)
- Rol × perspectief layout (matrix of accordeon-stijl)
- Familie-recursie (uitvouwbare boomweergave)
- Optioneel: browser-state-persistentie voor user-keuzes (jouw "vrouw-confidence"-idee)

---

## Gevolgen

**Positief**:
- Records worden naslagwerk voor elke accountant, niet alleen ITAA-stagiair
- Cursus-waarde-hefboom via kader-fiches + uitzonderingen-edges
- Rol × perspectief maakt expliciet wat de accountant in welke situatie moet doen
- Element-vocabulaire opent rijke render-mogelijkheden (filters, search, mobile-vs-desktop)

**Risico's en mitigatie**:
- *Verlies van inhoud bij herextract* → oude records als seed; archief read-only blijft
- *Tijdsdruk Fase 2* → parallelle subagent-fleet; cross-PO-completeness per record voorkomt rework
- *🧭-drift* → VERIFY drempel-detectie; mens-in-de-loop steekproef per wave
- *Schema-bump-werk in tooling* → records-API krijgt soft-validator; bestaande 1.5/1.6 leesbaar gedurende overgang

**Vervolgwerk (niet in dit ADR vastgelegd)**:
- Concrete Quartz-component-update (ADR-010-revisie)
- Pilot-run definitie + retrospect-formaat (`docs/pilot-fase2-pipeline.md` apart)
- Wave-planning per PO update voor Fase 2

---

## Open punten

- Versionering: behouden we 2.0 of doen we 2.x incrementeel bij latere bijsturingen?
- Kader-fiche `kind`-veld: één `kader` of subtypes (`kader-analyse`, `kader-keuze`, `kader-financiering`)? Voorlopig één.
- Familie-genest-in-kader (zie leasing-v1 in lange-termijn-financiering-v1): `heeft_lid` transitief in render bewezen werkbaar — laten zo, herzien indien render-laag schrijft anders eist.
- Browser-state voor user-confidence: bewerken in ADR-010-revisie.
