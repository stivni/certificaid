# Leerpad-skelet PO 1.4 — Geconsolideerde jaarrekening en wetgeving

**Status**: retroactief skelet (geschreven 2026-05-31, ná de implementatie). Dient als **gold-standard voorbeeld** voor andere PO's en als context voor toekomstige feedback.

**Gebruik**: zie [docs/leerstuk-procedure.md](leerstuk-procedure.md) Stap 1. Voor PO 1.4 zelf is dit een naslagdocument; de scripts + markdown leven in [`data/leerstukken/`](../data/leerstukken/) resp. [`content/studiemateriaal/1-4/`](../content/studiemateriaal/1-4/).

---

## 1. Programma-analyse

### Officiële taken en doelstellingen

PO 1.4 heeft **één hoofdtaak** met **7 doelstellingen**:

> **Taak 1.4.1**: Opstellen van de individuele en geconsolideerde jaarrekening

| Doel | Tekst | Anchor-rol |
|---|---|---|
| 1.4.1.1 | Uitvoeren van eindejaarsverrichtingen | context |
| 1.4.1.2 | Bepalen van het boekhoudkundig resultaat en verwerking van de bestemming van het resultaat | context |
| 1.4.1.3 | Opstellen van de proefbalans en de saldibalans | context |
| 1.4.1.4 | Opstellen van de jaarrekening (balans, resultatenrekening, toelichting) | context |
| 1.4.1.5 | Verwerken van de sociale balans | context |
| 1.4.1.6 | Toepassen van de waarderingsregels (voorraden, afschrijving van vaste activa) | context |
| 1.4.1.7 | Executeren van vorderingen en schulden, op korte en lange termijn | context |

**Vereist niveau**: *toepassen* (volgens PO-metadata `niveau: toepassen`)

### Cruciale observatie: titel ≠ doelstellingen

De PO heet **"Geconsolideerde jaarrekening en wetgeving betreffende de geconsolideerde jaarrekening"**, maar de 7 officiële doelstellingen gaan **allemaal over enkelvoudige jaarrekening-opmaak** (eindejaarsverrichtingen, resultaatbestemming, proefbalans, sociale balans, waarderingsregels). Geen enkele doelstelling vermeldt expliciet consolidatie.

Conclusie: het PO dekt twee onderwerpen die in de programma-tekst **niet symmetrisch** zijn:
- **Kern (uit PO-titel)**: geconsolideerde jaarrekening — opmaak, methodes, eliminaties, goodwill, rapportering
- **Rakend (uit doelstellingen)**: enkelvoudige jaarrekening — overlapt sterk met PO 1.1 (Boekhouding) en PO 1.2 (Boekhoud- en jaarrekeningenrecht)

Het leerstuk-pakket moet **beide kanten dekken** — anders mist het examen-relevante stof.

### Kern vs rakend

- **Kern (consolidatie)**: vier leerstukken die de PO-titel inhoudelijk uitwerken
- **Rakend (enkelvoudig)**: één leerstuk dat doelstellingen 1.4.1.1 t/m 1.4.1.6 dekt (gedeeld met 1.1/1.2)

---

## 2. Voorbeeldexamen-patronen

Uit [voorbeeldexamens 2013-2015](../content/studiemateriaal/1-4/voorbeeldexamenvragen.md): 4 unieke vraag-eenheden voor dit PO (6 voorkomens, 2 echte duplicaten).

| Onderwerp | Hoe vaak | Type vraag | Centraal concept |
|---|---|---|---|
| Consolidatieverschillen — definitie + 4 oorzaken | 2× (2013-2, 2015-1) | Begrip + opsomming | consolidatieverschil |
| Maximale afwijking afsluitingsdatum (3 maanden) | 2× (2013-1, 2014-1) | Cijfer + onderbouwing | opmaak-geconsolideerde-jaarrekening |
| Controle-, belangenpercentage en methode bepalen | 1× (2014-1) | Toepassings-case met groepsstructuur | consolidatiemethoden + controle-bij-consolidatie |
| Vermelding minderheidsbelangen in resultatenrekening | 1× (2013-1) | Boekhoudkundige plaats | minderheidsbelangen |

**Patroon**: het examen toetst niet de uitvoering van een hele consolidatie, maar:
- **Kernbegrippen scherp formuleren** (definitie consolidatieverschil)
- **Getallen en grenzen kennen** (3 maanden afsluit-afwijking, drempels)
- **Gestructureerd toepassen op mini-groepsstructuur** (controle vs belang berekenen)

Alle vier vragen vallen in de "consolidatie"-kern, geen enkelvoudig. Maar enkelvoudig kan in andere PO's getoetst worden waar 1.4-leerstukken dan herbruikbaar zijn.

---

## 3. Leerstuk-voorstel

Vijf consolidatie-leerstukken + één enkelvoudig spoor. Per leerstuk:

### Leerstuk 1 — `wat-is-een-geconsolideerde-jaarrekening`

- **Vraag**: Wat is een geconsolideerde jaarrekening, voor wie, en wat zit erin?
- **Type**: entry-fiche (kort, doorklik-zwaar)
- **Gedekte doelstellingen**: 1.4.1.4 (gedeeltelijk — algemene structuur)
- **Gedekte concepten**: `geconsolideerde-jaarrekening` (hoofdconcept) + `jaarrekening`
- **Rationale**: Stagiair moet eerst snappen WAT het document is voordat hij wie/hoe/specifiek-leerstukken aankan. Zonder entry verspilt de stagiair tijd in detail-fiches die hij niet kan plaatsen.

### Leerstuk 2 — `wie-moet-consolideren`

- **Vraag**: Wanneer is een groep verplicht een geconsolideerde JR op te maken?
- **Type**: scope-fiche
- **Gedekte doelstellingen**: scope-vraag staat niet als aparte doelstelling, maar is impliciet voorwaarde voor 1.4.1.4 (consolidatie-deel)
- **Gedekte concepten**: `consolidatieverplichting` + `consolidatiekring` + `controle-bij-consolidatie` + `wijziging-consolidatiekring`
- **Rationale**: Controle-test + drempels + vrijstellingen zijn één pedagogische beweging ("moeten wij?"). Bevat de drempel-tabel die in andere leerstukken ge-referencet wordt.

### Leerstuk 3 — `hoe-consolideren`

- **Vraag**: Hoe verloopt consolidatie technisch — welke methode, eerste consolidatie, eliminaties?
- **Type**: techniek-fiche (zwaarste leerstuk in het pakket)
- **Gedekte doelstellingen**: 1.4.1.4 (consolidatie-deel), 1.4.1.1 (eindejaarsverrichtingen relevant voor uniforme waarderingsregels)
- **Gedekte concepten**: `consolidatiemethoden` + `integrale-consolidatie` + `evenredige-consolidatie` + `vermogensmutatiemethode` + `eerste-consolidatie` + `uniforme-waarderingsregels-consolidatie` + `eliminatie-intercompany` + `minderheidsbelangen`
- **Rationale**: Drie methodes naast elkaar tonen + de eerste-consolidatie als zwaarste verrichting + drie families courante eliminaties horen in één doorgewerkt verhaal. Splitsen zou de cohesie breken. Verdient extra schrijfregels-lengte-ruimte (tot ~5000 woorden).

### Leerstuk 4 — `goodwill-bij-consolidatie`

- **Vraag**: Wat gebeurt er met goodwill na de eerste consolidatie? Afschrijving, impairment, badwill.
- **Type**: specifiek-fiche (smal onderwerp, diep)
- **Gedekte doelstellingen**: 1.4.1.4 (gedeeltelijk)
- **Gedekte concepten**: `consolidatieverschil` (goodwill + badwill)
- **Rationale**: Examen-favoriet (4 vragen in voorbeeldexamens noemen consolidatieverschillen). B-GAAP afschrijving ↔ IFRS impairment is een examen-klassieker. Verdient eigen fiche want het onderwerp staat zelfstandig genoeg.

### Leerstuk 5 — `rapportering-en-controle-geconsolideerde-jaarrekening`

- **Vraag**: Hoe wordt een geconsolideerde JR opgemaakt, gecontroleerd en gepubliceerd?
- **Type**: proces-fiche
- **Gedekte doelstellingen**: 1.4.1.4 (rapportering-aspect), procesinformatie die niet in andere consolidatie-leerstukken past
- **Gedekte concepten**: `opmaak-geconsolideerde-jaarrekening` + `geconsolideerd-jaarverslag` + `controleverklaring` (in mindere mate)
- **Rationale**: Opmaak-proces, jaarverslag-inhoud, commissarisverslag (12 elementen art. 3:77), termijnen en NBB-publicatie. Doelstelling 1.4.1.4 vereist "opstellen" wat impliciet het proces meeneemt.

### Leerstuk 6 — `individuele-jaarrekening-opmaken` (cross-PO)

- **Vraag**: Hoe maakt een Belgische vennootschap haar enkelvoudige jaarrekening op?
- **Type**: enkelvoudig-spoor (rakend met 1.1/1.2)
- **Gedekte doelstellingen**: 1.4.1.1, 1.4.1.2, 1.4.1.3, 1.4.1.5, 1.4.1.6 (zes van de zeven — alles behalve consolidatie en vorderingen/schulden-management)
- **Gedekte concepten**: `jaarrekening` + `vennootschap-groottecategorieen` + indirect: eindejaarsverrichtingen + resultaatbestemming + proefbalans + sociale balans
- **Rationale**: PO-doelstellingen vereisen dit deel volledig. Cross-PO: hoort eerder bij 1.1/1.2 vanuit topic-perspectief, maar zit hier omdat 1.4 het in doelstellingen vraagt. Wanneer 1.1/1.2 hun eigen leerstuk krijgen → beslis dan over dedupliceren of cross-PO-tag.

---

## 4. Gap-check

| Doelstelling | Gedekt door | Notitie |
|---|---|---|
| 1.4.1.1 Eindejaarsverrichtingen | `individuele-jaarrekening-opmaken` (sectie) + `hoe-consolideren` Stap 0 (waarderingsregels-uniformiteit) | Volledig |
| 1.4.1.2 Resultaatbestemming | `individuele-jaarrekening-opmaken` (sectie) | Volledig |
| 1.4.1.3 Proefbalans + saldibalans | `individuele-jaarrekening-opmaken` (sectie) | Volledig |
| 1.4.1.4 Opstellen jaarrekening | `wat-is-...` (entry) + `hoe-consolideren` (consolidatie) + `goodwill-bij-...` (specifiek) + `rapportering-en-controle-...` (proces) + `individuele-jaarrekening-opmaken` (enkelvoudig) | Volledig — gespreid over vier leerstukken |
| 1.4.1.5 Sociale balans | `individuele-jaarrekening-opmaken` (sectie) | Volledig |
| 1.4.1.6 Waarderingsregels | `individuele-jaarrekening-opmaken` (sectie) | Volledig |
| 1.4.1.7 Vorderingen en schulden korte/lange termijn | Niet apart gedekt — sub-aspect van `individuele-jaarrekening-opmaken` | **Gap**: bij review konden we de specifiek-doelstelling 1.4.1.7 niet duidelijk lokaliseren in een leerstuk. Mogelijk impliciet via waarderingsregels-sectie. Verdient een latere verfijning. |

**Extra dekking** (PO-titel "geconsolideerde jaarrekening en wetgeving"):
- Wetgeving: niet als aparte doelstelling, maar verspreid in "Wettelijk fundament" van elke consolidatie-leerstuk + samengevat in themafiche
- Consolidatie-proces zelf: 5 leerstukken dekken het volledig

---

## 5. Minicursus-skelet

Volgt de canonieke 5-secties-structuur van ADR-036 (na samenvoeging §3+§4 in deze ronde):

### §1 — Waarom dit vak?

- Motivatie: groep-jaarrekening is fundamenteel anders dan één-entiteit-JR
- Bredere-programma-tabel: relatie tot 1.2 (boekhoudrecht), 1.3 (analyse), 1.5 (IFRS), 3.0 (vennootschapsrecht)

### §2 — Wat is dit vak?

Vijf compacte sub-secties, elk eindigend met wikilink naar het leerstuk dat het uitwerkt:

- "Het probleem" → context voor [[wat-is-een-geconsolideerde-jaarrekening]]
- "De oplossing" → [[wat-is-een-geconsolideerde-jaarrekening]]
- "Het plichten-spel" → [[wie-moet-consolideren]]
- "Drie technieken" → [[hoe-consolideren]] + [[goodwill-bij-consolidatie]]
- "Wat doet de accountant hier?" → [[rapportering-en-controle-geconsolideerde-jaarrekening]]

### §3 — Wat moet je kunnen + hoe pak je het aan

Leerstukken-leesroute in 4 stappen: entry+scope → techniek → goodwill → rapportering. Plus verwijzing naar themafiche voor herhaling. Geen rol-blokken meer (die zitten in de leerstukken zelf).

### §4 — Examen-radar

Tabel met 4 voorbeeldexamen-patronen + observatie ("toetst kernbegrippen + getallen + mini-toepassing, niet hele consolidaties").

### §5 — Concepten cross-PO

Tabel van concepten die ook in 1.3 / 1.5 / 1.6 / 2.3 / 3.0 leven.

---

## 6. Voorbeeldgroep

**Naam**: `aurelia`
**Locatie**: [data/voorbeeldgroepen/aurelia.yaml](../data/voorbeeldgroepen/aurelia.yaml)

### Keuze-rationale

Eén centrale mock-groep die alle controle-niveaus en methodes laat zien — geen aparte cases per leerstuk nodig. Structuur:

- **Moeder**: Aurelia NV
- **Bellator BVBA** (80 %) — exclusieve controle → integrale consolidatie
- **Concordia SE** (50 %) — gezamenlijke controle → evenredige (B-GAAP) of VMM (IFRS)
- **Dynamica NV** (30 %) — notabele invloed → vermogensmutatie
- **Erion NV** (18 %) — geen invloed → gewone belegging (illustreert grens)

### Inhoud (genereerd in 1 ronde)

- Groepsstructuur + 2 mermaid-diagrammen
- Balansen: Aurelia individueel + Bellator (boekwaarde vs reële waarde) + Bellator na herwaardering
- Resultatenrekening Aurelia individueel
- 4 boekingen in T-rekening-stijl: eerste-consolidatie + 3 eliminatie-families
- Mock geconsolideerde balans (mutatie-tabel-vorm)
- 2 mini-cases voor evenredige + VMM
- Drempel-toets-tabel
- Vergelijkings-tabellen methodes + controle-niveaus

Voor andere PO's: overweeg eerst hergebruik (vooral als context vergelijkbaar is — bv. fiscaal kan Aurelia hergebruiken als belastingplichtige).

---

## 7. Themafiche-mapping

**Bestaande themafiche**: [content/studiemateriaal/1-4/samenvatting.md](../content/studiemateriaal/1-4/samenvatting.md) — gemigreerd uit themafiche per ADR-039.

Geüpdatet in deze ronde:
- Sectie "Concept-index" → "Verdieping" met tweelaags-doorklik
- Leerstukken (primair) + concepten (secundair) volgens ADR-037 amendement

Geen nieuwe themafiche nodig voor 1.4.

---

## 8. Open vragen / beslismomenten

Tijdens de implementatie waren er enkele sparring-momenten waar de mens beslist heeft:

1. **Granulariteit** — 5 of 6 of 7 leerstukken? Beslist: 5 + 1 cross-PO = 6 totaal. Geen verdere splitsing van `hoe-consolideren` (zwaarste leerstuk) want pedagogische cohesie wint. Gestut door schrijfregels-cap optrek voor "hoe"-leerstukken naar 4500-5000 woorden.

2. **`individuele-jaarrekening-opmaken` location** — Eerst onder `content/studiemateriaal/1-4/`, daarna verplaatst naar `content/leerstukken/` (cross-PO holder). De wikilink-resolutie via Quartz basename blijft werken. Tag `verborgen` toegevoegd om hem uit de sidebar te filteren.

3. **PO 1.4 folder-naam** — Eerst `1.4/`, daarna gehernoemd naar `1-4/` wegens Quartz dev-server bug met punt-in-folder-naam. Live (GitHub Pages) werkt beide; lokaal vereist de dash.

4. **`title` vs `explorer_title`** — Quartz' standaard mapFn leest geen frontmatter rechtstreeks; custom emitter-plugin gebouwd (zie ADR-037 open punten + `quartz-custom/plugins/emitters/contentIndex.tsx`).

5. **Themafiche-doorklik** — Vroeger naar concepten direct (ADR-036). Nu primair naar leerstukken (ADR-037 amendement) want leerstuk = pedagogische opfris, concept = definitorisch opzoek.

---

## Lessen voor andere PO's

1. **PO-titel kan misleidend zijn**: check altijd of de doelstellingen overeenstemmen met wat de titel suggereert (1.4 doet dat duidelijk niet). Splits dan bewust in kern vs rakend.

2. **Voorbeeldgroep eerst**: één coherente mock met realistische cijfers + alle controle-niveaus / regimes / scenario's dekt het hele PO. Aurelia werkt voor 1.4 omdat alle methodes erin passen.

3. **Examen-radar verankeren**: schets de leerstukken zo dat de bevraagde patronen er natuurlijk in vallen. Voor 1.4: consolidatieverschil-vraag landt in `goodwill-bij-`, methode-bepaling landt in `wie-moet-` + `hoe-`.

4. **Cross-PO leerstukken zijn normaal**: niet elk PO is een silo. Beslis bewust over locatie (PO-folder vs `content/leerstukken/`) en zichtbaarheid (`verborgen` tag) per geval.

5. **Beats-vocabulair**: na 6 leerstukken zien we duidelijk welke beat-instructies werken ("introduceer met intuïtie", "concretiseer met getallen", "blockquote-aside voor achtergrond"). Formaliseer dit als appendix bij `leerstuk-schrijfregels.md` zodra het patroon over meer PO's bevestigd is.
