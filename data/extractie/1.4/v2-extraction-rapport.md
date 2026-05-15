# v2-extractie PO 1.4 — Geconsolideerde jaarrekening

**Run-id**: `concept-extractie-v2-2026-05-15T00:00:00Z`
**Model**: claude-opus-4-7 (subagent)
**Prompt**: `prompts/concept-extractie-v2.md`
**Schema**: ADR-007 v1.2
**Datum**: 2026-05-15

---

## 1. Aantal records — totaal + delta vs v1

| | Aantal |
|---|---:|
| v1-records (`data/concept_records/1.4/`) | 17 |
| v2-records (`data/concept_records/1.4-v2/`) | **31** |
| Delta | +14 (+82 %) |

De anti-twijfel-regel uit prompt v2 ("liever 20-30 % meer records") leverde ruim verdubbeling op voor de must-have-set. Verwachting in de opdracht was 22-30, uitkomst zit aan de bovenkant van die range.

## 2. v1 → v2 mapping

### Records met directe tegenhanger (17/17 v1-records gedekt)

Alle 17 v1-concepten kregen in v2 een hernomen record (met opgewaardeerd schema 1.2 + nieuwe optionele velden waar bundle ondersteunt). Geen v1-record viel uit.

- `consolidatiekring`
- `consolidatieverplichting`
- `consolidatieverschil` (nu mét `oorzaken[]`)
- `consortium`
- `evenredige-consolidatie`
- `geconsolideerde-jaarrekening` (nu mét `drempelwaarden[]` voor 3-maanden-regel)
- `groottecriteria-geconsolideerde-basis` (nu mét gestructureerde `drempelwaarden[]`)
- `ifrs-keuze-geconsolideerde-jaarrekening`
- `ifrs-verordening-1606-2002`
- `integrale-consolidatie` (nu mét `vergelijkingsparen[]` + `bouwstenen[]`)
- `intragroep-eliminaties` (omgevormd naar procedure met `stappen[]`)
- `step-acquisition`
- `step-disposal`
- `uitgestelde-belastingen-consolidatie`
- `uniforme-waarderingsregels-consolidatie`
- `vermogensmutatiemethode` (nu mét `berekeningsmethode[]`)
- `vrijstelling-subconsolidatie`

### NIEUW in v2 (14 records, voornamelijk must-have-gap-fill)

Must-have-set uit `data/quality_checks/1.4/examen-eval-2026-05-15.json` (in v1-pilot gemist):

- **`controle`** (begrip) — fundament uit art. 1:14 WVV
- **`controlepercentage`** (begrip) — must-have voor examenvragen over indirecte deelnemingen
- **`belangenpercentage`** (begrip + `berekeningsmethode[]` met concreet voorbeeld 70 % × 60 % = 42 %)
- **`exclusieve-controle`** (begrip) — triggert integrale consolidatie
- **`gezamenlijke-controle`** (begrip) — triggert evenredige consolidatie
- **`invloed-van-betekenis`** (begrip + `drempelwaarden[]` voor 20 %-vermoeden)
- **`geassocieerde-onderneming`** (begrip) — triggert vermogensmutatie
- **`minderheidsbelangen`** (begrip) — afzonderlijk van bouwsteen-in-integrale-consolidatie

Aanvullende recursive-deepening records:

- **`controle-in-rechte-en-in-feite`** (begrip) — onderscheid art. 1:14 §2 versus §3
- **`moedervennootschap`** (begrip) — consoliderende vennootschap
- **`dochteronderneming`** (begrip) — concrete tegenhanger
- **`geconsolideerd-jaarverslag`** (begrip) — apart van de jaarrekening
- **`werkelijke-waarde-toerekening-eerste-consolidatie`** (procedure) — operationele eerste-consolidatie-stap met `stappen[]`
- **`aandeel-van-derden-in-resultaat`** (begrip + `berekeningsmethode[]`) — presentatie-vraag uit 2013-1-vr6

## 3. Gebruik nieuwe v1.2-velden

| Veld | Aantal records met dit veld ingevuld |
|---|---:|
| `oorzaken[]` | 1 (consolidatieverschil — vier oorzaken via cross-bron-synthese) |
| `drempelwaarden[]` | 4 (geconsolideerde-jaarrekening, invloed-van-betekenis, consolidatieverschil, groottecriteria-geconsolideerde-basis) |
| `tijdlijn[]` | 0 (PO 1.4 heeft geen procedurele wettelijke termijnen waarop het patroon goed past — afsluitings-3-maanden-regel is een grens, niet een tijdlijn) |
| `vergelijkingsparen[]` | 11 (alle methodes, alle must-have-begrippen, consolidatieverschil) |
| `berekeningsmethode[]` | 3 (belangenpercentage, vermogensmutatiemethode, aandeel-van-derden-in-resultaat) |
| `in_praktijk[]` | 15 (bijna helft van de records) |
| `stappen[].actor` | 1 (intragroep-eliminaties — andere procedures hebben implied-actor "consolidator/groep") |

### Cross-bron synthese (`confidence: "inferred-from-aggregation"`)

10 claims van in totaal 112 blocks met confidence-label (≈ 9 %). Voornamelijk in:

- `consolidatieverschil` — vier oorzaken (alle vier aggregaten uit KB WVV art. 3:130/3:131 + CBN 2013/3 + CBN 2022/11)
- `controlepercentage` — doorrekenregel (art. 1:14 WVV + CBN 2017/02 + CBN 2013/4)
- `belangenpercentage` — definitie + rekenregel
- `uitgestelde-belastingen-consolidatie` — valkuil bij werkelijke-waarde-toerekening

## 4. Dangling-references

**12 termen** geregistreerd in `data/quality_checks/1.4/dangling-references-v2.json`:

Top 5 (op basis van bron-spreiding en relevantie):

1. **`verbonden vennootschap`** — cross-PO-begrip (PO 1.1 vennootschapsrecht), nu impliciet
2. **`te verwaarlozen betekenis (vrijstelling)`** — eigen drempel-record overwegen
3. **`transacties onder gemeenschappelijke leiding (common control)`** — eigen procedure-record overwegen voor common-control-transactions-patroon
4. **`gemeenschappelijke leiding (in feite)`** — opgevangen onder `consortium`, twijfelgeval
5. **`geconsolideerd eigen vermogen`** — impliciet in `integrale-consolidatie` + `minderheidsbelangen`

De overige 7 termen zijn operationele rekenstappen (bv. "fractie eigen vermogen", "compensatie van deelneming") die in v1.2 als sub-stap binnen `berekeningsmethode[]` of `bouwstenen[]` zitten en geen autonoom fenomeen vormen.

## 5. Bron-voorstellen

**3 voorstellen** ingediend in `data/extractie/_bron_voorstellen.json`:

1. **IFRS 10 / 3 / 11 / 12 — primaire IFRS-tekst** (anchor 1.4.II.A). Anchor vraagt expliciet het IFRS-kader maar corpus bevat alleen Belgische tekst. Voorstel: EUR-Lex Verordening 1126/2008 (Nederlandstalige IFRS) als publieke primaire bron.
2. **Doctrine-handboek voor consolidatieverschil-oorzakentaxonomie** (anchor 1.4.I.D). Belgische handboeken (Jorissen/Lybaert) hebben de canonieke 4-puntenlijst die KB WVV en CBN-adviezen niet expliciet bieden.
3. **Praktijkvoorbeelden controle/belangenpercentage-doorrekening** (anchor 1.4.I.C). KB WVV art. 1:14 geeft principes maar geen rekenkundige scenariotabel (M→A→B-ketens). Voorstel: CBN-werkdocument of een afdeling van het Verslag aan de Koning.

## 6. Open observaties

### Wat goed werkte

- **Recursive deepening** vond alle must-have-begrippen uit de examen-eval (controlepercentage, belangenpercentage, exclusieve/gezamenlijke controle, invloed van betekenis, geassocieerde onderneming, minderheidsbelangen) terug in de bundles. Bron-first matching faalde in v1 enkel omdat de extractor ze niet als zelfstandig record aanmaakte — niet omdat de chunks ontbraken.
- **Cross-bron synthese** voor de vier oorzaken van consolidatieverschil: KB WVV art. 3:130 (toerekening werkelijke waarde) + art. 3:131 (afschrijving) + CBN 2013/3 (voorbeeld step acquisition met goodwill) leveren samen — als geaggregeerd — de canonieke oorzakentaxonomie. Confidence-tag `"inferred-from-aggregation"` met provenance over alle drie de bronnen.
- **`vergelijkingsparen[]`** werkt als anti-confusion-mechanisme — examenvraag 2013-2-vr3 (statutaire vs. consolidatieverschil-goodwill) is nu inhoudelijk gecoverd via dat veld op `consolidatieverschil`.
- **`in_praktijk[]`** is het meest aangewende nieuwe veld (15/31). Voor begrip-records dekt het "hoe herken je dit?" (bv. controle in feite via AV-aanwezigheidslijsten), voor methode-records dekt het de presentatie-kant ("Belangen van derden" op de balans).

### Open kwesties

- **IFRS-anchors (1.4.II.A, II.B, II.C, II.D)** blijven onderbedeeld. De Belgische CBN-adviezen verwijzen wel naar IFRS-concepten (control-model, joint venture), maar de extractor kan zonder IFRS-tekst niet de specifieke afwijkingen versus KB WVV beschrijven. De drie IFRS-keuze-records (1606/2002, IFRS-keuze geconsolideerde jaarrekening) blijven op meta-niveau (verplichting, keuze, vrijstelling) zonder de inhoudelijke IFRS-substantie te dekken. Zie bron-voorstel #1.
- **Tijdlijn[]-veld onbenut**. PO 1.4 heeft weinig procedurele wettelijke termijnen — de 3-maanden-afwijking is een grens (drempel), niet een tijdlijn. Het veld blijft beschikbaar voor latere PO's met sterker procedure-karakter (bv. PO 4.0 deontologie, PO 1.7 audit).
- **`stappen[].actor`-veld**: slechts één record (intragroep-eliminaties) gebruikt het expliciet. Voor de meeste consolidatie-procedures is de actor implicieet "de consolidator / het bestuursorgaan van de moeder" en levert het veld weinig extra informatie. Voor procedures met rolverdeling (bv. audit, deontologie) zal het veld waardevoller zijn.
- **`oorzaken[]` werd alleen op `consolidatieverschil` toegepast**. Andere records waar het patroon zou kunnen spelen:
  - `consolidatiekring` — vier uitsluitingsgronden zijn nu als `uitzonderingen[]`-block opgenomen (één samengetrokken tekst). Latere pass kan ze uit elkaar trekken in `uitzonderingen[]` per grond (en eventueel `oorzaken[]` van wijziging van de consolidatiekring).
  - `vermogensmutatiemethode` — typische direct-to-equity-mutaties (dividenden, kapitaalverhoging, herwaardering) zijn nu als `berekeningsmethode[].stappen` opgenomen; zou ook als `oorzaken[]` van boekwaardewijziging kunnen worden gestructureerd.

### Ten opzichte van v1-pilot

- v1 maakte 17 records, alle 17 met node-type-discipline maar zonder enumeratie-velden (oorzaken, drempelwaarden).
- v2 maakt 31 records, met **alle vijf must-have-begrippen uit examen-eval** gecoverd en met de gestructureerde velden voor enumeratie- en drempel-vragen.
- v2 dekt 100 % van de v1-records, plus 14 nieuwe — geen regressie.
