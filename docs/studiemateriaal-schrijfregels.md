# Studiemateriaal-schrijfregels

Inhoudelijke conventies voor de **leermateriaal-laag** — minicursussen in `content/studiemateriaal/<programmaonderdeel>.md` en de bijbehorende glue-prompts. Wordt door de glue-renderer geladen als prompt-input en geldt evenzeer voor menselijke aanvullingen.

> **Doelpubliek**: stagiair gecertificeerd accountant met boekhoudkundige en fiscale basiskennis — geen jurist.
>
> **Verhouding tot [concept-schrijfregels](concept-schrijfregels.md)**: die documenteren de **data-laag** (records, samen-aanpassen-met-regel). Dit document documenteert de **interpretatieve laag** (per leerpad). Heuristiek uit [ADR-010](adr/ADR-010-leermateriaal-tutor.md) §interpretatieve-laag: hoort iets *samen aangepast te worden bij elke regelwijziging* → data-laag. Hoort het *per leerpad anders gefraseerd* te zijn → leermateriaal-laag.

---

## Wat IS een minicursus?

Een minicursus is een **leerverhaal** voor één programmaonderdeel — geen render van concept-records, geen samenvatting van wetteksten, geen examenoplossingen-bundel. Een goed leerverhaal weeft concepten samen volgens de cognitieve volgorde die een student helpt de stof te bezitten.

Een minicursus is **interpretatief**:
- Volgorde van concepten dient de leercurve, niet de records-graph-topologie
- Transities tussen secties zijn pedagogisch ("nu we X kennen, kunnen we Y bekijken"), niet structureel
- Framing per PO mag verschillen ("dit is een van drie reserves; vergelijk met X en Y")
- Voorbeelden en illustraties komen uit records — geen nieuwe voorbeelden bedenken (zie §8 anti-fabricatie)

Een minicursus is **geen**:
- Concept-fiche: die is opzoek-vorm + tutor-RAG-context, referentie-toon ([ADR-010](adr/ADR-010-leermateriaal-tutor.md) §implicatie-1)
- Wettekst-bundel: citaten alleen waar ze inhoudelijk nodig zijn ([§1](#1-parafrase-grens))
- Examen-oefen-pakket: voorbeeldvragen komen in een **eind-rubriek "Examenfocus"**, niet vermengd met leerstof ([ADR-009](adr/ADR-009-examenpatronen.md) §6)

---

## 1. Parafrase-grens — wanneer woordelijk, wanneer parafraseren

[ADR-010 §implicatie-3 (glue v3)](adr/ADR-010-leermateriaal-tutor.md) versoepelt de eerdere strenge verbod op parafrase — onder strikte voorwaarden.

### Toegestaan

| Type claim | Voorbeeld | Voorwaarde |
|---|---|---|
| **Parafraseren** van een record-veld in cursus-stem | "De alarmbelprocedure springt aan bij twee triggers" → afgeleid uit `[[alarmbelprocedure]]`-record | Wikilink bij de claim in dezelfde zin |
| **Concept verbinden** aan eerder behandeld concept | "Zoals we zagen bij [[continuïteitsbeginsel]], …" | Doelconcept moet bestaan en eerder in de minicursus aangeraakt zijn |
| **Compacte synthese**: "kort: dit zijn drie reserves die elkaar opvolgen in prioriteit" | Afgeleid uit `vergelijkingsparen[]` of edge-structuur | De synthese mag niet meer beweren dan de records onderliggend dragen |
| **Pedagogische framing**: "let op het verschil tussen X en Y" | Verwijst naar bestaande `vergelijkingsparen[]` of `synthese`-record | Geen examenvraag-spoiler of camouflage-onthulling |
| **Voorbeeld-introductie**: "stel je voor: een vennootschap…" | Brug naar een record-voorbeeld | Het voorbeeld zelf komt uit records, niet uit de glue |

### Niet toegestaan

- Een **feit verzinnen** zonder record-grondslag (cijfer, drempelwaarde, termijn, definitie)
- Een **wikilink bedenken** naar een non-existent record
- Een **wettekst-citaat als prozetekst** ("Artikel 2:52 WVV stelt dat..."). Citeren mag wel **als blockquote met bron** en alleen waar de exacte bewoordingen ertoe doen.
- Een **voorbeeld bedenken** (de illustraties komen uit records, niet uit de glue)
- Een **examenvraag-camouflage** ontmaskeren ("let op, dit is een schijngelijkenis"). Camouflage-info hoort in de eind-rubriek, niet in de hoofdtekst.

---

## 2. Wikilink-discipline — élke feitelijke claim krijgt wikilink

**Principe**: een paragraaf zonder wikilink mag geen wettekst- of cijfer-claim bevatten. De wikilink markeert *waar de claim onderliggend gedragen wordt* — niet als sierraad, maar als grondingsmechanisme.

**Implementatie**:
- Elke zin die een feit, regel, drempel, termijn, definitie of berekening bevat → wikilink `[[record-id]]` in dezelfde zin
- Pedagogische zinnen ("nu we X kennen") of bruggen ("laten we kijken naar…") hoeven geen wikilink — die dragen geen feitelijke last
- Bij meerdere claims in één zin: meerdere wikilinks (geen "verwijzingen-aan-het-eind"-stijl)

**Validator** (te implementeren in [§6.3 code-werk](TODO.md)): bij build faalt een minicursus wanneer een paragraaf cijfers, datums, "%" of "art." bevat zonder wikilink. Lijst uitsluitings-tokens (bv. paginanummers, "1e", "2e", "p.x") wordt centraal vastgelegd.

---

## 3. Voice en stem — minicursus spreekt de student aan, fiche niet

**Minicursus** (interpretatieve laag): tweede persoon ("je ziet", "let op", "als je dit toepast…"). De student is in het verhaal aanwezig. Hoofdstuk-intro's gebruiken werkwoorden die aansluiten bij het PO-niveau (zie §9 niveau-toelichtingen).

**Concept-fiche** (referentie-laag): geen persoonsaanduiding. Definities en regels staan in feitelijke-vorm ("De alarmbelprocedure verplicht…", niet "Je moet de alarmbelprocedure volgen…"). De fiche is een naslagwerk, niet een lestekst.

**Tutor-antwoord** (interactief): mag persoonlijker ("dat klopt", "je zou kunnen overwegen…") maar volgt voor feitelijke claims dezelfde grondingsregels als minicursus (wikilinks, bronvermelding bij wettekst).

---

## 4. Doorlink-conventies — wanneer parafraseren, wanneer doorlinken

**Heuristiek**: lengte van de claim bepaalt het pad.

| Claim past in | Conventie |
|---|---|
| 1 zin | **Parafraseer** intern in minicursus + wikilink |
| 2+ zinnen of een tabel/lijst | **Doorlink** naar `[[record-id]]` zonder herhaling; één-zin-aanduiding wat er staat |
| Meer dan een paragraaf | Vraag op: hoort dit niet in een **eigen hoofdstuk** van de minicursus? Of: is dit een **synthese-inbedding** (§6)? |

**Reden**: parafrase voor één zin houdt het verhaal leesbaar zonder de student steeds weg te halen. Doorlink voor langere stof voorkomt duplicatie en houdt de record als single source of truth.

**Voorbeeld**:

> Goed:
> > De alarmbelprocedure heeft twee triggers — bij nettoactief minder dan de helft van het kapitaal moet de algemene vergadering binnen drie maanden bijeen ([[alarmbelprocedure]]).
>
> Niet goed (te veel parafrase):
> > De alarmbelprocedure heeft twee triggers. De eerste is wanneer het nettoactief minder dan de helft van het kapitaal bedraagt, dan moet de algemene vergadering binnen drie maanden bijeengeroepen worden om over ontbinding te beslissen. De tweede trigger is wanneer het nettoactief minder dan een vierde van het kapitaal bedraagt, dan geldt een kortere termijn van drie maanden voor bijeenroeping en de ontbindingsbeslissing kan met een gewone meerderheid genomen worden ([[alarmbelprocedure]]).
>
> Beter (doorlink omdat het meer dan één zin is):
> > De alarmbelprocedure kent twee triggers met elk eigen termijnen en stemvereisten — zie [[alarmbelprocedure]] voor de volledige tabel.

---

## 5. Examenrubriek-vorm — eind-rubriek "Examenfocus"

Volledige spec in [ADR-009 §6](adr/ADR-009-examenpatronen.md) en [ADR-010 §implicatie-4](adr/ADR-010-leermateriaal-tutor.md). Hier de schrijfregels-samenvatting:

**Plek**: laatste H2 van elke minicursus, **vóór** "Verder lezen" (indien aanwezig). Vaste titel: `## Examenfocus`.

**Vorm**: `> [!question]-` callouts (collapsed). **Eén callout per voorbeeldvraag** — bij multi-voorbeeldvragen onder dezelfde examenfocus krijgt elke vraag een eigen callout (zie [ADR-009 §6](adr/ADR-009-examenpatronen.md)):
- **Callout-titel**: `<examenpatroon-naam> · <examen-ID> vraag <vraag-nr>` — **geen** vraag-tekst in de titel (anti-spoiler)
- **Callout-body** (geopend door student): de exacte vraag-tekst uit `data/programma/examen_vragen/<examen_id>.json`
- **Optioneel binnen body**: `> [!success]-` collapsed met `antwoord_motivering` (uit examen-vragen-JSON, indien beschikbaar) of `redenering` (voor `voorbeeldvraag`)

Voor `voorbeeldvraag--*.json` is er per object één voorbeeldvraag (de gegenereerde vraag zelf) → één callout per voorbeeldvraag.

**Twee subkoppen onder Examenfocus** (geen mixing):
1. *Voorbeeldvragen uit ITAA/BIBF-examens* (⚖️) — gerenderd per voorbeeldvraag uit alle `examenfocus--*.json` waarvan `concept_ids ⊆ records(PO X)`. Sortering: tier A → B → C, binnen tier op examen-jaar.
2. *Synthetische oefenvarianten* (🤖) — gerenderd per `voorbeeldvraag--*.json`. Sortering: alfabetisch op patroon-naam.

**Wat NIET in deze rubriek**:
- Studieadvies ("oefen dit vaak", "let op valkuilen") — hoort in concept-record `valkuilen[]` of synthese-`kerninzichten`
- Vraag-tekst zonder grondingsobject (examenfocus of voorbeeldvraag) — alle vragen moeten een onderliggend object hebben

---

## 6. Synthese-inbedding — synthese-records inline, niet als losse fiche

[ADR-010 §implicatie-2](adr/ADR-010-leermateriaal-tutor.md): records met `node_type: synthese` worden **niet** gerenderd als losse concept-fiche. Ze leven uitsluitend ingebed in een minicursus.

**Inbed-vormen** (te beslissen tijdens leerpad-curation):

| Synthese-vorm | Inbed-conventie in minicursus |
|---|---|
| `vergelijkingstabel` | Inline tabel in de relevante sectie, voorafgegaan door 1 zin glue ("In één oogopslag: …") |
| `beslisboom` (mermaid) | Inline mermaid-diagram, voorafgegaan door 1-2 zinnen die de keuzes situeren |
| `stappenplan` | Genummerde lijst in de relevante sectie |
| `tijdlijn` | Inline tabel of mermaid-gantt |

**Wikilinks vanuit minicursus naar `[[synthese-id]]`**: resolveren niet meer naar een losse pagina ([ADR-010 §implicatie-2](adr/ADR-010-leermateriaal-tutor.md)). Render-laag zet die wikilinks om naar **anchor-links binnen de minicursus** indien de synthese in deze minicursus voorkomt; anders wordt de wikilink weggehaald en vervangen door een korte parafrase + wikilink naar de constituerende `gebaseerd_op_concepten[]`.

**Schrijfregel**: gebruik synthese-records bewust per leerpad. Een synthese-record dat in geen enkele minicursus wordt ingebed, is een onaffe data-laag (waarschuwing in validator).

---

## 7. Compactheidscontract — woordlimiet en ritme

**Glue-richtlijn** (ADR-010 §implicatie-3, v3): **700–1100 woorden per minicursus** voor het glue-werk (intro's, transities, framing, syntheses-aanduiding). Concept-content (definities, voorbeelden) is *aanvullend* en telt niet mee voor de glue-limiet.

**Per-element-richtlijnen**:

| Element | Richtlijn |
|---|---|
| Hoofdstuk-intro (begin van elke H2) | 2–3 zinnen — context + wat komt eraan |
| Sectie-transities | 1 zin — bruggetje naar volgende concept |
| Eind-rubriek "Examenfocus" | Geen glue — direct de callouts (anti-spoiler) |
| Vroege oriëntatie "Wat verwacht het examen van jou?" ([ADR-010 §implicatie-5A](adr/ADR-010-leermateriaal-tutor.md)) | Niveau-callout (1-zin-toelichting per niveau) + compacte taken-lijst |
| Eind-dashboard "Heb je deze taken in de vingers?" ([ADR-010 §implicatie-5C](adr/ADR-010-leermateriaal-tutor.md)) | Lijst met ✓/⚠/✗-indicator + secties-links — geen lange uitleg |

**Compactheid + parafrase-vrijheid = grotere informatie-dichtheid per zin**, niet meer woorden. Een goed geschreven minicursus zegt veel met weinig.

---

## 8. Anti-fabricatie-grens — wat validator afdwingt, wat reviewer

**Validator** ([§6.3 code](TODO.md) `tools/leermateriaal/validate_minicursus.py`):

| Check | Niveau |
|---|---|
| Elke wikilink resolveert naar bestaand record | error (fail build) |
| Paragraaf met cijfer/datum/"%"/"art." heeft wikilink in zelfde paragraaf | error |
| Glue blijft binnen 700–1100 woorden (per minicursus) | warning |
| Examenfocus-callouts alleen in `## Examenfocus`-sectie (anti-spoiler) | error |
| Niveau-callout aanwezig in eerste H2 (Implicatie 5A) | warning |
| Taak-marker in elke H2 behalve `voorbereiding`-hoofdstukken (Implicatie 5B) | warning |
| Eind-dashboard aanwezig vóór Examenfocus (Implicatie 5C) | warning |
| Synthese-records die in deze minicursus voorkomen via leerpad-YAML, krijgen inbed (geen dangling-link) | error |

**Reviewer-verantwoordelijkheid** (niet automatiseerbaar):
- Klopt de pedagogische volgorde van concepten?
- Voelt de stem natuurlijk aan voor het PO-niveau?
- Past de framing bij het beoogde studiemoment (begin / verdieping / examenvoorbereiding)?
- Doet de eind-rubriek "Examenfocus" recht aan de patroon-verscheidenheid van dit PO?

---

## 9. Niveau-toelichtingen — werkwoorden en framing per PO-niveau

Het ITAA-examenprogramma (`data/programma/programma.json`) noteert per programmaonderdeel een **niveau** (`kennen`, `begrijpen`, `toepassen`, `integratie`). Dat niveau bepaalt hoe diep de student de stof moet beheersen en welke werkwoorden in de minicursus-stem passend zijn.

### Eén-zin-toelichting per niveau (voor oriëntatie-sectie)

| Niveau | Toelichting voor de student |
|---|---|
| **Kennen** | "Je moet de definities, regels en termijnen van dit programmaonderdeel paraat hebben — woordelijk weten." |
| **Begrijpen** | "Je moet de samenhang tussen de begrippen kunnen uitleggen — niet alleen weten *wat*, ook *waarom*." |
| **Toepassen** | "Je moet deze regels en begrippen kunnen toepassen op een nieuwe casus — herkennen welk concept geldt en de stappen correct uitvoeren." |
| **Integratie** | "Je moet meerdere concepten samen kunnen inzetten in complexe casussen — onderdelen herkennen, prioriteren, en tot een coherent oordeel komen." |

Deze zinnen worden letterlijk gebruikt in de **niveau-callout** van de vroege oriëntatie-sectie van elke minicursus ([ADR-010 §implicatie-5A](adr/ADR-010-leermateriaal-tutor.md)).

### Werkwoorden in hoofdstuk-intro's (open punt — zie hieronder)

> **OPEN PUNT — hoe sturend?** ([TODO §6.3](TODO.md))
>
> Voor *toepassen*- en *integratie*-PO's moeten werkwoorden in de minicursus-stem niet beperkt zijn tot kennen/begrijpen. Concrete invulling — één-zin in intro vs. expliciete framing vs. impliciet weefsel — is nog niet vastgelegd. Glue-prompt v3 krijgt PO-niveau als input; de stijl-richtlijn landt in dit document zodra besloten.
>
> Voorlopige indicatie (te valideren):
>
> | Niveau | Voorbeeld-werkwoorden in hoofdstuk-intro |
> |---|---|
> | Kennen | "we bekijken", "je leert kennen", "de regel is dat…" |
> | Begrijpen | "we doorgronden waarom", "je leert het verband tussen", "de logica is dat…" |
> | Toepassen | "je leert deze regel toepassen op", "we werken een casus uit waarbij", "stap voor stap doorlopen we…" |
> | Integratie | "je leert deze concepten samen inzetten in", "we bouwen een coherent oordeel op uit", "in een complexe casus moet je…" |

---

## 10. Verwijzingen

- [ADR-007](adr/ADR-007-conceptmodel.md) — Conceptmodel (schema 1.6, leerpad-schema 1.1)
- [ADR-009](adr/ADR-009-examenpatronen.md) — Examenpatronen (§6 render-integratie, §7 schema examenfocus/voorbeeldvraag)
- [ADR-010](adr/ADR-010-leermateriaal-tutor.md) — Leermateriaal & tutor (§interpretatieve-laag, implicaties 1–5)
- [concept-schrijfregels](concept-schrijfregels.md) — Data-laag schrijfregels (parallel document)
- [TODO §6](TODO.md) — Fase 6 sub-taken (6.0 schrijfregels-doc, 6.1–6.5 code-werk, 6.6 pilot)
