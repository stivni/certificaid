# ADR-037 — Leerstuk als vierde leerlaag (tussen minicursus en concept)

**Status**: Draft (2026-05-30)
**Gerelateerd**: [ADR-036](ADR-036-drie-lagen-leermateriaal.md) (amendeert — themafiche-rol verschuift), [ADR-030](ADR-030-granulariteit-typologie.md) (concept-granulariteit blijft; nieuw atoom op leerlaag), [ADR-029](ADR-029-schema-21-operaties-model.md) (conceptlaag-bron)

---

## Context

Sparring-sessie 2026-05-30 bracht twee samenhangende observaties aan het licht:

1. **De minicursus-laag (ADR-036) springt te ver naar de conceptlaag.** Een leerpad als [PO 1.4](../../content/leerpaden/1.4.md) verwijst in §3 "Wat je daarvoor moet kennen" direct naar 10+ losse concepten (`consolidatieverplichting`, `consolidatiekring`, `controle-bij-consolidatie`, `wijziging-consolidatiekring`, drie methode-records, …). De stagiair die "moet ik consolideren?" probeert te begrijpen, moet vier fiches naast elkaar leggen om één samenhangend antwoord te krijgen. Er is geen integrerende vraag-gerichte tussenstap.

2. **De conceptlaag zelf is té definitorisch en te versnipperd.** RAG-zoek `consolidatie` geeft 18+ records boven similarity 0.55 — elk met zware juridische definities, dubbele uitleg van overlappende begrippen (controle staat in `consolidatiekring`, `controle-bij-consolidatie`, `consolidatieverplichting` alle drie), en in sommige gevallen feitelijke verschuivingen (`consolidatieverplichting` verwees voor de "kleine groep"-drempels naar art. 1:24 § 6 i.p.v. art. 1:26 § 1). Dit is een aparte opkuis-actie op de conceptlaag; ADR-037 raakt die niet.

Het versnipperings-probleem op concept-niveau wordt **niet** opgelost door records te mergen. Atomair-blijvende concepten behouden hun nut voor opzoekgedrag ("wat is precies goodwill?"). De oplossing is een **integrerende leerlaag bovenop concepten** die de pedagogische bundeling doet.

ADR-036 dekt momenteel drie lagen — minicursus (PO-niveau) · themafiche (cluster-overzicht, kapstok) · concept-fiche (atomair). Themafiche is geen geschikte kandidaat voor de integrerende rol: hij is gepositioneerd als **printbare herhalings-kapstok**, en de schrijfregels expliciteren "veronderstelt herkenning, geen uitleg" en "dichtheid > verhaal". Iemand die de stof voor het eerst leert, krijgt daar geen pedagogisch handvat.

## Beslissing

Voeg een vierde leerlaag in: het **leerstuk**.

| Laag | Atoom | Lezer-state | Locatie |
|---|---|---|---|
| **Minicursus** | Eén PO (of spoor) | "Ik begin aan dit vak — geef me het verhaal en de routekaart" | `content/leerpaden/<po-code>.md` |
| **Leerstuk** *(NIEUW)* | Eén didactische vraag of samenhangend leerstuk binnen een cluster | "Ik wil deze vraag nu echt snappen — leid me door" | `content/leerstukken/<slug>.md` |
| **Themafiche** | Eén cluster | "Ik moet dit opfrissen — geef me alles op één pagina" | `content/themafiches/<cluster>.md` |
| **Concept** | Eén begrip | "Wat is precies X?" | `content/concepten/<concept-id>.md` (gerenderd uit records) |

**Studie-volgorde (canoniek, geactualiseerd)**:

1. **Minicursus** — verhaal + routekaart van het PO
2. **Leerstukken** — per leerstuk de samenhangende vraag doorwerken
3. **Concept-fiches** — voor wie dieper of nauwkeuriger wil dan het leerstuk biedt
4. **Themafiche** — opfrissingsdocument na bestudering, printbaar

De minicursus verwijst primair naar leerstukken (in §3 "Wat je daarvoor moet kennen" en §4 "Studie-aanpak"). Concept-wikilinks in een minicursus blijven enkel waar pinpoint-precisie nodig is (specifieke definitie, voorbeeld dat alleen in dat record staat).

### Naamkeuze

**"Leerstuk"** — gekozen boven `lesfiche`, `leervraag`, `studie-eenheid`, `didactische fiche` omdat:

- "fiche" is al overbelast in het project-vocabularium (concept-fiche, themafiche)
- "les" klinkt schools en suggereert frontaal onderricht
- "leervraag" vangt het atoom (één vraag) maar het *bestand* is geen vraag — het is een antwoord
- "leerstuk" past bij examen-context (NL/Vlaams gangbaar voor "samenhangend stuk leerstof")

Slug-conventie is vrij: óf vraag-gericht (`wie-moet-consolideren`, `hoe-consolideren`, `wat-is-een-geconsolideerde-jaarrekening`) óf thema-aspect (`geconsolideerde-jaarrekening-opmaken`, `consolidatie-toepassingsgebied`). De auteur kiest wat natuurlijk leest. Schrijfregels leggen geen rigide template op. Slug moet uniek zijn binnen de hele `content/`-boom (botst niet met concept-slugs).

### Granulariteits-stelregel

> **Een leerstuk mag groot zijn als het verhaal samenhangt; eerder samen dan splitsen.**

Concreet: één leerstuk per **didactische vraag-met-eenduidig-antwoord**. Sub-vragen mogen secties zijn — geen apart leerstuk. Voorbeelden voor PO 1.4:

| Leerstuk (voorgesteld) | Dekt concepten |
|---|---|
| `wat-is-een-geconsolideerde-jaarrekening` | `geconsolideerde-jaarrekening` + relevante delen van `jaarrekening` |
| `wie-moet-consolideren` | `consolidatieverplichting` + `consolidatiekring` + `controle-bij-consolidatie` + `wijziging-consolidatiekring` |
| `hoe-consolideren` | `consolidatiemethoden` + `integrale-consolidatie` + `evenredige-consolidatie` + `vermogensmutatiemethode` + `uniforme-waarderingsregels-consolidatie` + `eerste-consolidatie` + `eliminatie-intercompany` |
| `goodwill-bij-consolidatie` | `consolidatieverschil` |
| `rapportering-en-controle-geconsolideerde-jaarrekening` | `opmaak-geconsolideerde-jaarrekening` + `geconsolideerd-jaarverslag` + link naar `controleverklaring` |
| `individuele-jaarrekening-opmaken` *(enkelvoudig deel van 1.4)* | eindejaarsverrichtingen + resultaatbestemming + proefbalans + sociale balans + waarderingsregels-enkelvoudig — secties binnen één leerstuk, niet 5 aparte |

→ Totaal **6 leerstukken voor PO 1.4** (5 consolidatie + 1 enkelvoudig). Hoeveelheidsorde voor het hele corpus: 19 PO's × 4-7 leerstukken ≈ **80-130 leerstukken**. Handelbaar voor mens-onderhoud, en groot genoeg om de integratie-functie waar te maken.

### Wikilink-grafiek

Een leerstuk mag wikilink-en naar:

- **Andere leerstukken** — voor verwijzing zonder dupliceren (`wie-moet-consolideren` → `hoe-consolideren` zodra de stagiair de scope-vraag beantwoord heeft)
- **Concepten** — voor wie het detail wil opzoeken (`[[consolidatieverschil]]` als doorklik naar de atomaire definitie)
- **Themafiches en minicursussen** — voor zoom-out

Een minicursus wijst primair naar leerstukken. Een themafiche blijft cluster-niveau (verwijst naar concepten voor doorklik). Een leerstuk **wijst niet terug** naar zijn minicursus (backlink-relatie is render-laag-keuze, geen schrijftaak).

### Wettekstreferenties

**Wetsartikel-nummers staan NIET in de lopende tekst.** Reden: leesvloeiendheid en pedagogische toon — een stagiair die "wie moet consolideren?" probeert te snappen, wil geen onderbreking door `(art. 3:22 e.v. WVV)` mid-zin.

Alle wetsverwijzingen worden gebundeld in een sectie **"Wettelijk fundament"** aan het einde van het leerstuk — één lijn per claim:

```markdown
## Wettelijk fundament

- Consolidatieplicht: WVV art. 3:22 e.v. + KB-WVV
- Drempels groep van beperkte omvang: WVV art. 1:26 § 1 (cijfers in Cijferzakboekje)
- Vrijstelling kleine groep: WVV art. 3:25
- Controle-test: WVV art. 1:14 + 1:18 + 1:20
```

De stagiair die "waar staat dit?" vraagt, scrolt naar dat blok. De stagiair die de redenering wil snappen, leest ongestoord door.

De render-laag mag dit later optioneel uitbreiden naar superscript-voetnoten — schrijver hoeft dat niet te annoteren.

### Visualiteits-eis

> **Praten over jaarrekeningen → jaarrekeningen tonen.**

Een leerstuk moet **minstens twee** visuele elementen bevatten uit volgende lijst:

- Echte (of mock) jaarrekening-tabel met getallen
- Vergelijkingstabel (drempels, methodes, regimes …)
- Mermaid beslisboom of groepsstructuur-diagram
- T-rekening / boekingsschema
- KaTeX-formule met genoemde variabelen
- Side-by-side scenario-tabel (bv. drie groepen, gevolg per drempel-toets)

Pure-tekst leerstukken zijn een red flag. Bij review: "kun je dit *zien*?" — zo niet, herwerken.

### Bron-traceerbaarheid (in het hoofd van de auteur)

Geen confidence-iconen (⚖️/🤖) in de body. Maar de auteur draagt onverminderd de verantwoordelijkheid:

- Geen claim zonder bron in het hoofd
- Bij twijfel: herformuleren of weglaten, niet "⚠️"-labelen
- Drempels, percentages en datums staan in de "Wettelijk fundament"-sectie of komen uit het Cijferzakboekje-pointer

Dit is **soepeler dan concept-records** (waar 📖/🔗/🤖 verplicht zijn) en **harder dan losse studieblogs** (waar je vermoedens mag opschrijven). De gap reflecteert de leerlaag-functie: pedagogische helderheid boven juridische compleetheid — maar nooit ten koste van correctheid.

## Amendement op ADR-036 (themafiche-rol verschuift)

ADR-036 kadert themafiche als "kapstok-document op 1-2 A4 — visueel dominant, tekst minimaal". Sparring 2026-05-30 bevestigt: **themafiche moet vooral visueel zijn — een infographic-achtig overzicht, geen pedagogisch instructiedocument**. Aangezien het leerstuk de tekstuele-pedagogische rol overneemt, kunnen themafiches verder opschuiven naar het visuele uiterste:

- Vergelijkingsmatrices, beslisbomen, formule-blokken, schema's blijven kern
- Verklarende prozá-bullets mogen krimpen — de leerstuk-laag draagt nu de verklaring
- Take-away-bullets blijven zinvol als one-liners ("methode volgt het doel, niet andersom")
- "Valkuilen"-tabel blijft

Themafiche-schrijfregels-revisie volgt in een aparte werkronde nadat eerste leerstukken bestaan en we het overlap-gebied empirisch zien.

### Themafiche-doorklik: primair naar leerstukken (amendement vastgelegd 2026-05-31)

ADR-036 §"Themafiche — zeven vaste blokken" §7 "Concept-index" beschrijft een web-only doorklik-sectie die groepeert per functie en wijst naar **concept-fiches**. Met de invoering van de leerstuk-laag (deze ADR) verschuift die rol:

- **Themafiche-doorklik wijst primair naar leerstukken** voor pedagogische opfris (de stagiair die "hoe zat het ook al weer met methodes?" stelt, klikt door naar het leerstuk dat hem het verhaal terug brengt).
- **Concepten blijven secundair** voor wie definitorisch detail of een wettekst-pointer zoekt.
- Sectie-naam verschuift van "Concept-index" naar **"Verdieping"** (mens-leesbaarder, omvat beide categorieën).

Concrete render-structuur in de themafiche:

```markdown
## Verdieping

### Leerstukken — voor pedagogische opfris
- [[wat-is-een-geconsolideerde-jaarrekening]] — wat is het, voor wie, vier onderdelen
- [[wie-moet-consolideren]] — controle, kring, drempels, vrijstellingen
- [[hoe-consolideren]] — vier stappen + drie methodes + drie families
- [[goodwill-bij-consolidatie]] — afschrijving + impairment + badwill
- [[rapportering-en-controle-...]] — opmaak, jaarverslag, commissarisverslag

### Concept-fiches — voor definitorisch detail
- [[consolidatiekring]] · [[consolidatieverplichting]] · [[controle-bij-consolidatie]]
- [[integrale-consolidatie]] · [[evenredige-consolidatie]] · [[vermogensmutatiemethode]]
- (...)
```

Themafiche-schrijfregels-update voor andere themafiches (jaarrekening-schema, eindejaarsverrichtingen, kostprijsmethoden …) volgt zodra leerstukken in andere PO's bestaan — niet alle clusters hebben nu al een leerstuk-tegenhanger.

## Verhouding tot bestaande lagen

| Laag | Owner | Trigger voor update |
|---|---|---|
| **Concept-fiche** | `data/concepten/records/<id>.json` → render | Record-edit |
| **Leerstuk** *(NIEUW)* | Handgeschreven `content/leerstukken/<slug>.md` | Onderliggende concepten materieel gewijzigd OF nieuwe didactische inzicht |
| **Themafiche** | Handgeschreven `content/themafiches/<cluster>.md` | Records van het cluster materieel gewijzigd |
| **Minicursus** | Handgeschreven `content/leerpaden/<po>.md` | Examenprogramma-edit OF nieuwe leerstukken/themafiches |

Geen auto-regen tussen lagen. Conform ADR-003 stale-flagging.

## Generatie-aanpak

POC-fase: **handgeschreven** door Opus tijdens sparring. Eerste mockup wordt `content/leerstukken/wie-moet-consolideren.md` (deze ronde). Indien het format zich bevestigt → Sonnet-agent voor de resterende ~80-130 leerstukken op basis van [`docs/leerstuk-schrijfregels.md`](../leerstuk-schrijfregels.md).

## Mockup (POC — handgeschreven door Opus, 2026-05-30)

- **Leerstuk-POC**: [`content/leerstukken/wie-moet-consolideren.md`](../../content/leerstukken/wie-moet-consolideren.md) — PO 1.4, scope-vraag. Visualiteits-eis ingevuld via drempel-tabel + groepsstructuur-mermaid + beslisboom + doorgewerkte voorbeeldgroep.
- **Minicursus-edit (POC)**: [`content/leerpaden/1.4.md`](../../content/leerpaden/1.4.md) §3 "Wat je daarvoor moet kennen" — herstructureerd rond leerstuk-wikilinks.

## Wat dit superseert / amendeert

| Artefact | Status na ADR-037 | Reden |
|---|---|---|
| ADR-036 §"Drie-lagen leermateriaal-architectuur" | **Amendement**: vier lagen i.p.v. drie | Leerstuk toegevoegd tussen minicursus en concept |
| ADR-036 §"Studie-volgorde voor een kandidaat" | **Amendement**: 4 stappen i.p.v. 3 | Leerstuk wordt stap 2; concept-fiches schuiven naar stap 3 |
| ADR-036 §"Themafiche — zeven vaste blokken" | **Marge-amendement**: themafiche schuift visueler | Pedagogische tekstuele rol verhuist naar leerstuk |
| `docs/themafiche-schrijfregels.md` | **Revisie nodig** (latere ronde) | Tekstuele bullets mogen krimpen ten gunste van visuele dichtheid |
| `docs/minicursus-schrijfregels.md` | **Update §3-richtlijn**: primair naar leerstukken wijzen | Geen aparte ADR-revisie nodig |
| `content/leerpaden/1.4.md` | **POC-edit deze ronde** | §3 wijst nu naar leerstukken |

## Open punten — voor latere ronde

| # | Punt | Trigger |
|---|---|---|
| 1 | Conceptlaag-opkuis: dedupliceren (controle in 3 records) + feitelijke correcties (`consolidatieverplichting` art. 1:24 § 6 → art. 1:26 § 1) + minder "definitorisch" schrijven | Apart werkpakket; trigger = ≥3 leerstukken geschreven zodat we duidelijk zien welke concept-content nog vereist is en welke door leerstuk wordt overgenomen |
| 2 | Themafiche-schrijfregels herzien (visueel-dominanter) | Wanneer 3-5 leerstukken bestaan voor één cluster (consolidatie) en we de tekstuele overlap zien |
| 3 | Volledige 1.4 leerstuk-set schrijven (5 consolidatie + 1 enkelvoudig) — Sonnet-agent | Na approval van mockup `wie-moet-consolideren` |
| 4 | Render-laag-keuze: wetsverwijzingen-sectie blijven of opschuiven naar superscript-voetnoten? | Wanneer 10+ leerstukken bestaan en het footer-blok kwantitatief in beeld komt |
| 5 | Quartz-explorer: `content/leerstukken/` in sidebar opnemen | Wanneer ≥5 leerstukken gepubliceerd zijn |
| 6 | Backlink-render: een concept-fiche toont "Genoemd in leerstukken X, Y" (automatisch) | Wanneer leerstukken-corpus stabiel genoeg is |
| 7 | Multi-PO leerstukken: kan één leerstuk PO-overstijgend zijn (bv. waarderingsregels)? | Empirisch wanneer een leerstuk in twee minicursussen relevant blijkt |

## Veranderlog

- **2026-05-30** — ADR opgesteld na sparring-sessie (Opus). Aanleiding: stagiair vraag op `/concepten/consolidatieverplichting` over drempels groottecriteria → ontdekking dat (a) concepten-laag versnipperd is voor pedagogisch gebruik, (b) `art. 1:24 § 6` ≠ `art. 1:26 § 1` (feitelijke fout in record), (c) themafiche/minicursus-gap = integrerende leerlaag ontbreekt. Naam `leerstuk` vastgelegd. Granulariteits-stelregel "eerder samen dan splitsen". Wettekst-conventie "voetensectie ipv inline". Visualiteits-eis "twee visuele elementen verplicht". POC `wie-moet-consolideren` als test-case voor consolidatie-cluster.
