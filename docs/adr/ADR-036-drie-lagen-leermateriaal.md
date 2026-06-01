# ADR-036 — Drie-lagen leermateriaal: minicursus · themafiche · concept-fiche

**Status**: Draft (2026-05-28)
**Gerelateerd**: ADR-002 (examenprogramma-scoping) · ADR-007 (conceptmodel) · ADR-008 (concept-extractie — supersedeert §14 Fase D + §15 Fase E + §16 competentie-gap) · ADR-010 (leermateriaal & tutor) · ADR-029 (schema 2.1 v1.5 — `accountant_perspectieven` als drager van operationele acties) · ADR-030 (granulariteit-skelet → clusters)

---

## Context

De `data/concepten/records/` zit vol: 359 schema 2.2-records met definitie, perspectieven, valkuilen, voorbeelden. Per record een gerenderde concept-fiche in `content/concepten/`. Goed voor *"ik wil concept X begrijpen"*.

Wat ontbreekt voor een ITAA-kandidaat die zich voorbereidt op het examen:

1. **PO-niveau verhaal** — *"wat is dit vak eigenlijk en hoe vallen de onderdelen samen?"* Een kandidaat die binnenstapt op PO 1.4 (Geconsolideerde jaarrekening) wil niet meteen in losse fiches gestort worden — ze wil eerst weten *waarom* dit vak, *wat* een accountant hier doet, en *hoe* de stof samenhangt. De concept-fiches geven dat niet (te atomair).
2. **Cluster-niveau samenvatting** — *"alles van consolidatie op één pagina, om snel te herhalen"*. De maand vóór het examen wil je niet 16 losse fiches doorploegen — je wil één kapstok-document dat alle methodes vergelijkt, de plicht-drempels in één tabel zet, de valkuilen herinnert. Dat soort document past niet in een individuele fiche (te beperkt) noch in een rendering van losse records (te versnipperd).

De **vroegere leerpad-flow** (ADR-008 §15 — Fase E, `tools/leermateriaal/propose_leerpad.py` + `prompts/leerpad-propose-v1.md`) probeerde de PO-niveau-laag te dekken via een YAML-schema met drie hoofdstuk-types: `oriëntatie` (LLM-glue), `competentie` (verwees naar competentie-YAML), `thematisch` (concept-cluster). Die flow is om twee redenen achterhaald:

- **Competenties bestaan niet meer als aparte laag.** Schema 2.1/2.2 verwerkt operationele vaardigheden ("kring bepalen", "methode kiezen") binnen het concept-record onder `accountant_perspectieven.rollen[].elementen[]`. ADR-008 §14 (Fase D — `propose_competenties.py`) is daarmee superseded.
- **Het render-formaat (YAML met `oriëntatie` / `competentie` / `thematisch`) en het taalniveau (interne jargon: "anchor", "rationale_hint", "thematisch hoofdstuk")** matchen niet wat een kandidaat wil zien. Een minicursus moet leesbaar zijn als doorlopend studiedocument, geen geserialiseerd schema.

De cluster-niveau-laag was er helemaal niet — een gat.

## Beslissing

Drie-lagen leermateriaal-architectuur, naast elkaar:

| Laag | Naam | Scope | Doel | Locatie |
|---|---|---|---|---|
| **Concept-fiche** | `<concept-id>` | Eén concept | "Ik wil concept X begrijpen tot in detail" | `content/concepten/<concept-id>.md` (gerenderd uit `data/concepten/records/`) |
| **Themafiche** | `<cluster-naam>` | Eén cluster uit granulariteit-skelet | "Ik wil alles van dit thema op één pagina, om snel te herhalen" | `content/themafiches/<cluster-naam>.md` (handgeschreven of via prompt) |
| **Minicursus** | `<po-code>[-<sub>]` | Eén programmaonderdeel (of een spoor binnen een PO) | "Ik wil dit vak begrijpen — verhaal, opbouw, leesroute" | `content/studiemateriaal/<po-slug>/index.md` |

De drie lagen zijn complementair en bedienen verschillende leesmodi van dezelfde kandidaat. Een minicursus *verwijst naar* themafiches en concept-fiches; ze lijfen die niet in.

**Studie-volgorde voor een kandidaat** (canoniek):

1. **Minicursus** — verhaal + routekaart van het PO
2. **Concept-fiches** — diepgang per begrip, in de volgorde van de leesroute in §4 van de minicursus
3. **Themafiche** — opfrissingsdocument na bestudering, printbaar voor de week vóór het examen

Themafiches zijn dus **complementair** aan de leerpad-laag, niet er onderdeel van. De leesroute in een minicursus loopt uitsluitend door concept-fiches. De themafiche wordt vermeld in de minicursus als "voor de herhaling, gebruik X", niet als studie-stap.

### Naamkeuzes en alternatieven

**"Minicursus"** — gekozen boven `leerpad` omdat:
- "leerpad" suggereert een lineaire weg, terwijl het document ook overzicht/context biedt
- "minicursus" past bij de bestaande project-terminologie (`tools/leermateriaal/render_minicursus.py` bestond al voor studiemateriaal-snapshots in ADR-010)
- voor de kandidaat klinkt het natuurlijker als didactisch document

**"Themafiche"** — gekozen boven `synthese`, `cluster-synthese`, `samenvatting`, `overzichtsfiche`, `kapstok` omdat:
- "fiche" zit al in het project-vocabularium (concept-fiche, competentie-fiche)
- "thema" verduidelijkt dat het document een cluster afdekt, niet één concept
- "synthese" werd als te abstract ervaren tijdens sparring (mei 2026)
- "kapstok" is metaforisch krachtig maar voelt te informeel voor een document-typenaam

**"Kern" en "Rakend"** — gekozen boven `Spoor A/B` als labels voor het onderscheid binnen een minicursus tussen *het deel dat specifiek bij dit PO hoort* en *het deel dat gedeeld is met andere PO's*:
- "Spoor A/B" is meta-jargon zonder semantische lading
- "Kern" = wat dit vak van jou vraagt
- "Rakend" = waar dit vak overlapt met andere vakken (en dus naar de minicursus van die andere PO doorverwezen wordt)

### Per-laag structuur (canoniek)

**Minicursus — zes vaste secties:**

1. **Waarom dit vak?** Korte motivatie + tabel "Hoe past dit in het bredere programma?" (relatie tot 3-5 andere PO's)
2. **Wat is dit vak?** Het *verhaal* in vijf H3-sub-secties (probleem · oplossing · plichten-spel · technieken · wat doet de accountant). Doorlopend proza, doelgroep-toon (kandidaat).
3. **Wat moet je kunnen?** Drie sub-blokken:
   - **Kern** — per rol (boekhouder/commissaris/adviseur) wat de kandidaat moet kunnen, elk gelinkt naar de relevante concept-fiches via wikilinks
   - **Rakend** — verwijst naar andere minicursussen voor gedeelde stof
   - **Wat je daarvoor moet kennen** — verzamelt records die niet via een rol-actie genoemd waren + wettelijke kaders als context
4. **Studie-aanpak** — leesroute in 4-5 stappen + verwijzing naar relevante themafiches
5. **Examen-radar** — tabel van bevraagde onderwerpen uit `content/studiemateriaal/<po-slug>/voorbeeldexamenvragen.md` (frequentie · type vraag · centraal concept) + patroon-observatie + doorklik naar de volledige vragen
6. **Concepten die ook in andere PO's leven** — cross-PO-tabel voor kandidaten die meerdere PO's tegelijk voorbereiden ("dubbele rendementen")

Volledige schrijfregels: [`docs/minicursus-schrijfregels.md`](../minicursus-schrijfregels.md).

**Themafiche — zeven vaste blokken:**

1. **Take-away** — 3-5 bullets, het kennen-niveau in zakformaat
2. **Vergelijkingstabel** — als het cluster een onderscheid bevat (bv. drie consolidatie-methodes), met expliciete laatste rij voor B-GAAP↔IFRS-verschillen waar van toepassing
3. **Beslisboom** (mermaid) — als het cluster een "welk regime / welke procedure" vraag bevat
4. **Drempels & formules** — gefactualiseerd, met KaTeX waar wiskundig
5. **Klassieke valkuilen** — examen-radar in "wat klopt er niet / wat klopt wél"-formaat (uit `inhoud.valkuilen` van het hoofdrecord)
6. **Verbinding met examen** — taken+doelstellingen uit programma.json verbatim, per rij gemapped naar synthese-secties + wikilinks
7. **Concept-index** — `<div class="no-print">` web-only sectie met groepering per functie (scope / methodes / verrichtingen / opmaak)

Volledige schrijfregels: [`docs/themafiche-schrijfregels.md`](../themafiche-schrijfregels.md).

## Verhouding tot bestaande lagen

| Laag | Owner | Trigger voor update |
|---|---|---|
| **Concept-fiche** | `data/concepten/records/<id>.json` → `render_concept_v22.py` → `content/concepten/` | Record-edit (operatie-pipeline of mens) |
| **Themafiche** | Handgeschreven `content/themafiches/<cluster>.md` (mockup voorlopig in `content/experiment/`) | Records van het cluster materieel gewijzigd OF nieuwe valkuil/formule ontdekt |
| **Minicursus** | Handgeschreven `content/studiemateriaal/<po-slug>/index.md` | Examenprogramma-edit OF nieuwe themafiches OF nieuwe voorbeeldexamens-data |

**Geen automatische auto-regen tussen lagen.** Conform ADR-003: een record-wijziging stale-flagged eventueel de themafiche of minicursus, mens beslist of/wanneer regen.

## Generatie-aanpak

POC-fase: **handgeschreven** door Opus tijdens sparring, daarna door Sonnet-agent op basis van de schrijfregels-docs.

Per regel 7 (Opus ↔ Sonnet werkverdeling):
- **Opus** ontwerpt de eerste mockup van een nieuw document-type (zoals gebeurd voor `synthese-consolidatie-v1` en `studiemateriaal/1-4`)
- **Sonnet** repliceert het format voor andere clusters/PO's binnen de schrijfregels — Opus reviewt het eerste batch-resultaat

Een formele generatie-prompt (analoog aan operatie-prompts in `prompts/operaties/`) komt in een later werkpakket, zodra we genoeg variatie hebben gezien om het patroon te bevriezen.

## Mockups (POC — handgeschreven door Opus, mei 2026)

- **Themafiche-POC**: [`content/experiment/synthese-consolidatie-v1.md`](../../content/experiment/synthese-consolidatie-v1.md) — cluster `consolidatie` (PO 1.4). Status: voorgesteld, niet inhoudelijk gecureerd. Verplaatsen naar `content/themafiches/consolidatie.md` zodra structuur bevroren.
- **Minicursus-POC**: [`content/studiemateriaal/1-4/index.md`](../../content/studiemateriaal/1-4/index.md) — PO 1.4 (Geconsolideerde jaarrekening). Status: voorgesteld.

## CSS-conventies (Quartz publication layer)

Bij de POC zijn twee Quartz-conventies toegevoegd in [`quartz-custom/styles/custom.scss`](../../quartz-custom/styles/custom.scss):

- **`@media print`-blok** — synthese-pagina's en minicursussen zijn printbaar als PDF (A4, 1.2cm marges, sidebar/toc/explorer/footer verborgen, tabellen met repeat-header, callouts met print-color-adjust). Cmd+P → Save as PDF op elke pagina.
- **`.no-print`-class** — markeert secties die alleen op web bestaan (zoals "Concept-index" in een themafiche, dubbel met de concept-fiche-laag). Verbergt in print.
- **Volle-breedte tabellen** — `.table-container > table { width: 100%; padding: 0; margin: 1rem 0 }` overrijdt Quartz' shrink-to-content default.

Conventies blijven projectbreed; mocht een ander documenttype andere print-keuzes nodig hebben → eigen `@media print`-block per pagina via inline `<style>`.

## Wat dit supersedeert

| Artefact | Status na ADR-036 | Reden |
|---|---|---|
| ADR-008 §14 (Fase D — Competentie-destillatie) | Superseded | Competenties verhuisd naar `accountant_perspectieven` in schema 2.1 v1.5 (ADR-029) |
| ADR-008 §15 (Fase E — Leerpad-opstelling) | Superseded | Vervangen door minicursus-format in dit ADR |
| ADR-008 §16 (`competentie-gap` in gaps.json) | Superseded | Geen aparte competentie-laag meer; gaps op concept-niveau |
| `tools/leermateriaal/propose_leerpad.py` | Verwijderd | Oud YAML-schema; minicursus is markdown |
| `tools/leermateriaal/propose_competenties.py` | Verwijderd | Competenties niet meer apart |
| `tools/leermateriaal/render_competentie_fiche.py` | Verwijderd | Geen competentie-records meer |
| `prompts/leerpad-propose-v1.md` | Verwijderd | Vervangen door minicursus-schrijfregels |
| `prompts/competentie-destillatie-v1.md` + `-v2.md` | Verwijderd | Competenties niet meer apart |
| `data/concepten/studiemateriaal/*.yaml` (10 stuks) | Gearchiveerd in `_archive/` | Oude format; inhoud bewaard als sparring-historiek |

## Open punten — voor latere ronde

| # | Punt | Trigger |
|---|---|---|
| 1 | Generatie-prompts voor Sonnet-agent (minicursus + themafiche) | Zodra we ≥3 voorbeelden hebben van elk type — patroon bevroren |
| 2 | Themafiches per cluster: welke clusters prioriteren? Voorstel: starten met de 15 zwaarste (waar examenvragen op samenkomen) | Wanneer de massa-generatie start |
| 3 | Render-tooling voor themafiche/minicursus (`render_themafiche.py`?) — of blijft handgeschreven? | Wanneer 50+ documenten bestaan en consistentie-onderhoud manueel onhaalbaar wordt |
| 4 | Render-laag-status (Fase 7 `render_concept_v22.py`): integratie van wikilinks naar minicursus/themafiche in elke concept-fiche-render — automatische backlink? | Wanneer minicursus/themafiches stabiel zijn |
| 5 | Multi-PO-filter / overlap-highlight (kandidaat zit op 5 PO's tegelijk; welke clusters raken meerdere?) | Wanneer alle minicursussen bestaan |
| 6 | PDF-bundle ("print alle 5 syntheses voor mijn 5 PO's als één boekje") | Quartz print-flow valideren met meerdere documenten |

## Veranderlog

- **2026-05-28** — ADR opgesteld na sparring-sessie (Opus). Twee POC-mockups gemaakt (`synthese-consolidatie-v1.md` + `studiemateriaal/1-4/index.md`). Naamkeuzes `minicursus` / `themafiche` / `Kern`/`Rakend` vastgelegd. Opkuis van Fase D + Fase E artefacten (zie tabel boven).
