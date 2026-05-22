# Schema v1.4 — user-feedback + discussie

**Status**: open discussie (22 mei 2026 namiddag)
**Werkwijze**: per cluster doorlopen, beslissing → schema-update + ADR-aanpassing.

---

## Cluster A — Identiteit & metadata

### A1. `naam_blok` te ruim
> "andere talen zijn niet relevant, tenzij het een term is die niet nederlands is (bv. Anti Money Laundering Compliance Officer). Synoniemen alleen als gangbaar."

**Pushback**: ik ben eens. Probleem: agent zal `andere_talen` invullen "omdat het kan". Beter: weghalen behalve voor non-NL-primaire termen.

**Voorstel**:
- `naam.primair` blijft (de NL-naam, of de EN-naam als het concept geen NL-equivalent heeft)
- `naam.afkorting` blijft (echte afkorting in vakgebruik)
- `naam.synoniemen` blijft maar prompt-discipline: "alleen breed gangbaar — niet bedacht"
- `naam.andere_talen` → **drop**. Of: behoud alleen `nl: "..."` als primair niet-NL is (voor "AML Compliance Officer" zou je `nl: "Anti-witwas-compliance-functionaris"` willen)

**Beslispunt**: drop `andere_talen` volledig, of behoud met strikte regel "alleen als primair geen NL is"?

---

### A2. `dekt_tdks` vs `linked_anchors`
> "lijken hetzelfde"

**Analyse**: ze zijn niet identiek maar overlappen sterk.
- `linked_anchors` = alle anchors waarover dit concept iets zegt (breed)
- `dekt_tdks` = subset = anchors die DIT concept expliciet dekt (smaller — toetsbaarheid)

In de praktijk werd `dekt_tdks` op skelet leeg gelaten (alleen uit candidates-DB als die het had). Voor render maakt onderscheid niet veel uit.

**Voorstel**: **drop `dekt_tdks`**. Behoud alleen `linked_anchors`. Render-laag kan zelf eerste-anker als "primair" tonen.

**Beslispunt**: mergen tot één veld?

---

### A3. `primary_po`
> "kan toch aan 2 PO's hangen? en vinden we dat niet terug via linked_anchors?"

**Pushback**: technisch ja, kan via `linked_anchors[0]` afleiden. Maar:
- Skelet-script + records-index gebruiken `primary_po` voor grouping/filtering
- "Eerste anker" = niet altijd primair (alfabetisch ≠ semantisch)
- Render kan willen tonen: "Vooral relevant voor PO 1.1, ook PO 2.x"

Wel: voor sommige cross-PO concepten is "primary" arbitrair (bv. `verbonden-partijen` is even centraal in 1.1, 1.4, 1.6, 2.x).

**Voorstel**:
- **Optie A**: `primary_po` behouden, agent kan kiezen welke (eerste in volgorde van schrijven)
- **Optie B**: drop `primary_po`, render-laag kiest eerste anker uit `linked_anchors`
- **Optie C**: `primary_po` array `["1.1", "1.4"]` met "primair voor X PO's"

Mijn voorkeur: B (simpelste). Of A blijven (jouw keuze).

**Beslispunt**: drop, behouden, of array?

**Beslissing ✅ Stijn 22 mei**: **drop `primary_po`**. Render werkt met `linked_anchors[0]` of toont meerdere PO's expliciet.

---

### A4. `tags`
> "geen idee wat nuttig is, beter weglaten?"

**Eens**. Geen agent gebruikt 't nu, render-laag heeft niet nodig. Voor toekomst (filters bv. "alles waar `fiscaal-pb`-tag op zit") nog nuttig — maar **YAGNI** principe.

**Voorstel**: **drop `tags`** uit schema. Toevoegen later als concrete use-case opduikt.

**Beslispunt**: drop?

---

### A5. `cross_po`
> (impliciet via A2)

Boolean die af te leiden is uit `len(set(po uit anchors)) > 1`. Render kan dat zelf doen.

**Voorstel**: **drop `cross_po`**, render-laag berekent.

**Beslispunt**: drop?

---

### A6. `changelog.wijziging` — wie schrijft het?
> "lijkt nog niet te kloppen en door de LLM ingevuld, juist? Het veld 'wijziging' lijkt me wel iets nuttigs om door LLM te laten invullen. SoC."

**Eens** — separation of concerns:
- `operatie` + `timestamp` + `model` + `wave_id` + `metriek` → **mechanisch** (orchestrator/records-API)
- `wijziging` (samenvatting wat is gedaan) → **door LLM** als eindrapport van de operatie (max 200 chars?)

**Voorstel**:
- LLM rapporteert na elke operatie: "wijziging: 'Voegde 8 elementen toe + 5 relaties; 3 betwijfeld voor exacte tarieven'"
- Orchestrator vult mechanische velden in en plaatst LLM's `wijziging` erbij
- maxLength toevoegen aan `wijziging` (bv. 300)

**Beslispunt**: maxLength voor `wijziging`? 200/300/500?

---

## Cluster B — Top-niveau structuur

### B1. `voorkennis_leespad` — nut?
> "niet zeker van het nut. Er kan al veel door bronnen, links. Voorlopig eruit?"

**Pushback**: voorkennis-leespad is wel anders dan relaties:
- `relaties[type=valt_onder]` = "ik val onder dat kader" (structureel)
- `relaties[type=vereist]` = "ik vereis kennis van X" (hard)
- `voorkennis_leespad.voorvereisten` = "om mij te begrijpen, lees eerst X" (didactisch)
- `voorkennis_leespad.volgkennis` = "nadat je mij snapt, X is logische next" (didactisch)

Didactisch leespad is écht iets anders dan structurele relatie. Maar... in run-1 vulden agents het soms half-leeg.

**Voorstel**:
- **Optie A**: drop voorlopig (YAGNI)
- **Optie B**: behouden + maken naar aparte operatie `leespad_aanvullen` (na claims_checken, want vereist context van andere records)

Mijn voorkeur: B. Aparte operatie waar render later gebruik kan maken.

**Beslispunt**: drop of behouden-als-eigen-operatie?

**Beslissing ✅ Stijn 22 mei**: behouden als **aparte operatie** `leespad_aanvullen` (na claims_checken). LLM vult dit niet in `beschrijven`-operatie.

---

### B2. `definitie` + `substantie` + `rationale` als groep?
> "volgens mij moet die altijd samen voorkomen. Kunnen we ze niet in een objectje nesten?"

**Pushback nodig**: ze horen WEL bij elkaar (3 lagen "wat is het" → "wat gebeurt economisch" → "waarom"), maar:
- `definitie` = altijd verplicht
- `substantie` = optioneel (niet voor `kader`/`familie`)
- `rationale` = altijd optioneel

Conditional. Een gegroepeerd `kernuitleg`-object met 3 sub-velden zou structuur opleveren:

```json
"kernuitleg": {
  "definitie":  { "text": "...", "grondslag": {...} },     // verplicht
  "substantie": { ... },                                    // optioneel
  "rationale":  { ... }                                     // optioneel
}
```

**Voor-argumenten**:
- Groepeert wat samenhoort
- Render kan de groep als één blok tonen (drie tabs / accordeon)
- Validator kan eisen ≥1 van de 3

**Tegen-argumenten**:
- Extra nesting-laag
- Bij element-niveau heb je nu rechtstreeks `element.definitie` — wordt `element.kernuitleg.definitie`

**Beslispunt**: groeperen onder `kernuitleg`, of plat houden?

---

### B3. `gebruikscontext` waarom geen deel van `inhoud`?

**Beslissing ✅ Stijn 22 mei**: misverstand — gebruikscontext zit al onder inhoud. Niets te wijzigen.

```json
"inhoud": {
  ...,
  "gebruikscontext": ...,    ← al hier
}
```

---

### B4. `keuzekader` voelt te speciaal op hoog niveau
> "het stoort me dat 'keuzekader' op het hoogste niveau zit... is dat de enige vorm van synthese? Misschien ruimte voorzien voor 'synthese'?"

**Eens**. `keuzekader` is één specifieke synthese-vorm (assen + vergelijkingstabel). Andere syntheses mogelijk:
- **Tijdslijn-overzicht** (cyclus-records: jaarrekening-cyclus chronologisch)
- **Beslisboom** (gerelateerde keuzes geneste)
- **Vergelijkingsmatrix** (3+ varianten naast elkaar)
- **Heat-map** / dashboard (ratio-grenzen)

**Voorstel**: vervang `keuzekader` door `synthese` met sub-type:

```json
"synthese": {
  "type": "keuzekader" | "tijdslijn" | "beslisboom" | "matrix" | "dashboard",
  "intro": "...",
  "inhoud": { ... }   // type-afhankelijk
}
```

Of: `synthese` is gewoon een array van weergaven (gebruik bestaande `weergave`-mechanisme).

**Beslispunt**: vervang door generieke `synthese`-key met sub-types? Of behoud `keuzekader` + voeg later andere top-level synthese-keys toe?

---

### B5. `trigger_start`, `trigger_einde`, `voordeel`, `risico` als lijsten?
> "iets kan meerdere triggers of meerdere voordelen hebben"

**Eens**. Concept kan meerdere triggers hebben (faillissement triggered door betalingsstaking ÉN duurzaamheid). Idem meerdere voor-/risico's.

**Voorstel**: alle gebruikscontext-velden worden arrays:

```json
"gebruikscontext": {
  "voor": [...],              // al array
  "voorwaarden": [...],       // al array
  ...
  "trigger_start": [...],     // ← nu enkel-item, wordt array
  "trigger_einde": [...],     // ← idem
  "voordeel": [...],          // ← idem
  "risico": [...]             // ← idem
}
```

**Beslispunt**: confirm alle naar lijsten?

---

## Cluster C — Bouwstenen

### C1. `contextitem` vs `tekstblok` — abstractie zoeken
> "lijkt op het openings trio. Een 'claim' met rationale en bronnen. Toch eens abstractie zoeken?"

**Eens — sterk punt**. Vergelijk:

| Veld | `tekstblok` | `contextitem` |
|---|---|---|
| `text` | ✓ | ✓ |
| `grondslag` | ✓ | ✓ |
| `rationale` | — | ✓ |
| `relateert_naar` | — | ✓ |

`contextitem` ⊃ `tekstblok`. Voorstel: **unify**.

**Voorstel**: één **`claim`**-object met optionele velden:
```json
"claim": {
  "text": "...",
  "grondslag": {...},
  "rationale": "...",         // optioneel
  "relateert_naar": "..."     // optioneel
}
```

Of: behoud `tekstblok` als naam (vakwoord), voeg `rationale` + `relateert_naar` toe als optioneel.

**Beslispunt**: unify onder welke naam? `tekstblok` / `claim` / iets anders?

---

### C2. `element` overlap met top-level
> ("Veel overlap met top-level inhoud" zelfs in $comment)

**Eens** — element bevat: id/naam/inhoud_type/grondslag/definitie/substantie/rationale/weergaven/elementen/voorbeelden/verwijst_naar. Sommige overlappen met top-level inhoud.

Kan abstractie helpen? Element = mini-concept met identiteit. Maar geen aparte metadata/relaties (those zijn op record-niveau).

**Voorstel** (radicaal):
- Behoud overlap voor recursie-doel
- Drop `beschrijving` (zie C3 hieronder — al gevraagd)
- Drop `verwijst_naar` (zie C5 — relaties op record-niveau)
- → Element wordt simpeler

**Beslispunt**: behouden zoals nu of trimmen?

---

### C3. `element.beschrijving` vs `element.definitie`
> "lijkt me dat we gewoon definitie kunnen gebruiken. Of is dit een 'inleiding'?"

**Pushback**: `beschrijving` werd toegevoegd omdat **agents alleen-titel-elementen** schreven (zonder enige inhoud). Beschrijving = mini-vrije-tekst zonder volledige grondslag-overhead.

Maar als we forceren dat elke element minimum `definitie.text` heeft (al gewoon string in tekstblok-objectje), dan kan `beschrijving` weg.

**Voorstel**: drop `beschrijving`, eis dat element minstens `definitie` of `substantie` heeft.

**Beslispunt**: drop `beschrijving`?

---

### C4. `weergaven` brainstorm
> "Op veel meer plaatsen nuttig? Definitie van jaarrekening? Rationale? Groepen? Toelichting per weergave? Stappenplan?"

**Brainstorm met je**:

**Waar weergaven nuttig zijn** (huidige + voorstel):
| Locatie | Nu | Voorstel |
|---|---|---|
| `element.weergaven` | ✓ | ✓ behoud |
| `voorbeeld.weergaven` | ✓ | ✓ behoud |
| `definitie.weergaven` | ✗ | ✓ toevoegen (bv. jaarrekening = balans+RR+toelichting visueel) |
| `substantie.weergaven` | ✗ | ✓ toevoegen (economische flow diagram) |
| `rationale.weergaven` | ✗ | mss niet — rationale is tekstueel |
| `relatie.weergaven` (bij vergelijkbaar_met) | ✗ | ✓ toevoegen (vergelijkingstabel inline) |
| `contextitem.weergaven` | ✗ | mss — voorwaarde kan visualisatie hebben |

**Weergaven met toelichting**: nu is `weergave = {type, ...payload}`. Voorstel: voeg `weergave.toelichting` (string) en/of `weergave.naam` (kort label) toe.

**Groepen weergaven**: nu kun je `weergaven: [{...}, {...}]` doen (zonder grouping). Voor render-cohesie: voeg `weergaven_groep` met optionele `intro` toe? Of: laat element zelf de grouping-laag zijn.

**Weergaven afwisselen met tekst**: nu is alles split (text in `definitie`, weergaven apart). Voor "uitleg met afwisseling" zou je een **stream** willen: paragraaf → weergave → paragraaf → weergave. Dat is wat een **element** met `elementen[]`-recursie eigenlijk al kan doen — elk sub-element heeft zelf weergaven.

**Stappenplan** = al gedekt door `weergave_type: stappenlijst`. Geen extra abstractie.

**Mijn voorstel** (minst-invasief):
- `weergaven` toevoegen aan `definitie` + `substantie` (op record EN element-niveau) als optioneel
- `weergave.toelichting` + `weergave.naam` optioneel toevoegen
- Niet structuur dwingen — render-laag bepaalt opmaak

**Beslispunt**: welke locaties? Toelichting binnen weergave?

---

### C5. `verwijst_naar` = relaties?
> "zijn dat gewoon relaties?"

**Eens**. Element kan refereren naar ander concept of element. Dat is een relatie met `from = element_id`. Maar nu staat alles met from=record op record-niveau.

**Voorstel**:
- **Optie A**: drop `element.verwijst_naar`. Relaties altijd op record-niveau, met optioneel `from_element_id` voor herkomst.
- **Optie B**: behoud `element.verwijst_naar` als shortcut voor inline-relaties (lichte syntax).
- **Optie C**: element.verwijst_naar = lijst van canonical_refs (huidig). Render maakt graag links. Geen volle relatie-structuur.

Mijn voorkeur: C (lichte sjabloon-shortcut). Of A (consistent op één plek).

**Beslispunt**: drop, lichte ref-lijst, of full relatie-objects?

---

### C6. Voorbeelden — drie definities tot één
> "geen verschil tussen voorbeeld_inline en voorbeeld_top. Naam_blok overkill. Drie definities tot één."

**Analyse**:
- `voorbeelden_top` = `{intro, cases}` waar cases = `voorbeeld_case[]` met id + naam + context + elementen + grondslag
- `voorbeeld_inline` = lichter blok onder element.voorbeelden (geen id verplicht, geen naam_blok)

**Eens — unify naar één type `voorbeeld`**:

```json
"voorbeeld": {
  "id":          { "type": "string", "pattern": "..." },    // optioneel (alleen voor top-level cases die je willen anker-en)
  "titel":       { "type": "string" },                       // verplicht
  "context":     { "type": "string" },                       // optioneel ("NV ABC heeft...")
  "beschrijving":{ "type": "string" },                       // optioneel inleiding
  "grondslag":   { ... },                                    // optioneel
  "weergaven":   [...],                                      // optioneel
  "elementen":   [...]                                       // recursie OK
}
```

`naam_blok` overkill voor voorbeeld → `titel: string` volstaat.

`inhoud.voorbeelden` wordt array van `voorbeeld` (geen `{intro, cases}`-wrapper meer, of houd `voorbeelden: {intro?, items: voorbeeld[]}` voor intro-mogelijkheid).

**Beslispunt**: `titel` ipv `naam_blok`? Behoud `intro` op group-niveau?

---

## Cluster D — Enums

### D1. `inhoud_type` te uitgebreid (19 waarden)
> "die lijst vind ik wel heel uitgebreid"

**Eens — trim-voorstel**:

Behouden (kern):
- `begrip`
- `procedure_stap` (drop `stap_in_cyclus` — onnodig onderscheid, render-laag of context bepaalt)
- `voorwaarde`
- `drempel`
- `regel`
- `uitzondering`
- `vuistregel`
- `mechanisme`
- `formule`
- `principe`
- `valkuil`
- `component`

Drop:
- `keuze` (onduidelijk; mss vervangen door element-niveau "wanneer wel/niet")
- `risico` (zit ook in gebruikscontext; redundant)
- `berekening` (= weergave_type, geen inhoud_type)
- `vergelijking` (= weergave_type)
- `moment_in_tijd` (vaag; vervang door procedure_stap)
- `eigenschap` (te generiek; ander inhoud_type kan)

→ 12 waarden ipv 19.

**Beslispunt**: voorstel passen, of welke subset?

---

### D2. `weergave_type` formele schemas
> "voor sommige weergaven gaan we een specifieke definitie moeten geven om structuur vast te leggen (jaarrekening, boeking, ...)"

**Eens** — nu is `weergave.{...payload}` met `additionalProperties: true` (ongedefinieerd). Voor render-laag is voorspelbare structuur nodig per type.

**Voorstel**:
- Per `weergave_type` een sub-schema definiëren met `oneOf` of `if/then`
- Bv. `boeking` vereist `rekeningen: [{rek, naam, debet?, credit?}]`
- `balans_snapshot` vereist `moment, actief[], passief[]`
- `formule_expressie` vereist `expressie, variabelen?`

Maar: dit kan ook **incrementeel** — eerst alle als `additionalProperties: true`, schrijf records, en pas per type validatie toe wanneer render-laag het type implementeert.

**Lijst trimmen**:
Behouden (kern):
- `proza`
- `tabel`
- `boeking`
- `balans_snapshot`
- `resultatenrekening_snapshot`
- `stappenlijst`
- `tijdslijn`
- `vergelijkingstabel`
- `formule_expressie`
- `berekening`
- `voorbeeld` (nieuw uit casus-rename)

Drop:
- `t_rekening` (= variant van boeking; render kiest)
- `beslisboom` (= weergave van keuzekader-data; geen apart type)
- `diagram` (te vaag)

→ 11 waarden ipv 14.

**Hoe nieuwe types ontdekken?** Agent moet kunnen aanmelden:
- Optie: `weergave.type_voorstel: "..."` als type niet in enum
- Of: agent gebruikt bestaand type + log in eindrapport
- Of: orchestrator scant changelog voor frequentie van onbekende types

**Beslispunt**: trim-voorstel passen + welke aanmeld-mechanisme?

---

## Cluster E — Rollen

### E1. Rol-set terug naar 5 "hoedjes"
> "we gingen minder rollen doen, alleen de hoedjes van de accountant"

**Eens** — terug:

| Behouden | Drop |
|---|---|
| `adviseur` (🎯 strategie) | `bestuurder` (zit in klant-perspectief) |
| `boekhouder` (📋 verwerking) | `curator` (zit in actor-records) |
| `auditor` (🔍 controle) | `forensisch` (zit in audit als specialisatie) |
| `fiscaal` (💰 belasting) |  |
| `begeleider` (🛡️ procedure-begeleiding) |  |

→ 5 hoedjes.

**Beslispunt**: confirm? Of nog inkrimpen (bv. fiscaal valt onder adviseur+boekhouder)?

---

### E2. `rollen_per_perspectief` hiërarchie te diep
> "is dat geen niveau of twee te veel?"

**Analyse huidige structuur**:
```
inhoud.rollen_per_perspectief
└── perspectieven[]
    └── perspectief { id, naam, rollen[] }
        └── rol_invulling { rol, elementen[] }
            └── elementen[]
                └── element { id, naam, beschrijving?, ... }
```

Vijf niveaus diep voor "wat doet de auditor voor de uitgevende vennootschap?" — wel veel.

**Vereenvoudigings-voorstel**:
```
inhoud.accountant_perspectieven[]
└── perspectief { id, naam, rol_invullingen[] }
    └── rol_invulling { rol, elementen[] }
```

Hernoeming + één omslag-niveau (`rollen_per_perspectief` → direct array) weg.

Of nog verder:
```
inhoud.accountant_per_perspectief[]
└── { perspectief_id, perspectief_naam, rol, elementen[] }   // flat
```

Per perspectief × rol = één entry. Render-laag bouwt matrix uit lijst.

**Pushback**: meerdere rollen per perspectief is logisch ("voor uitgever: én adviseur, én boekhouder, én fiscaal"). Twee-niveau (perspectief > rollen[] > elementen[]) blijft natuurlijk.

**Voorstel**: hernoem naar **`inhoud.accountant_perspectieven`** (rechtstreeks array), behouden 2-niveau (perspectief > rollen). Drop top-level wrapper.

**Beslispunt**: hernoeming + 1 niveau weg?

---

### E3. Element-invulling onder rol meer sturing?
> "invulling van de rol via elementen mag misschien iets meer gestuurd worden"

Element onder rol is een normaal element. Geen specifieke sturing nu. Mogelijke verbeteringen:
- Per rol-type vooraf-gedefinieerde element-categorieën (bv. boekhouder = boeking-momenten; auditor = controle-procedures)
- Of: `inhoud_type`-subset per rol

**Beslispunt**: open — wil je een specifiek voorstel?

---

## Wat we NIET hebben behandeld

- `relaties` structuur (alle 14 relatie-types, vergelijkbaar_met-velden)
- `synthese`/`keuzekader` sub-structuur details (na B4 beslissing)

---

## Voorgestelde volgorde van bespreken

Mijn voorkeur — clusters die elkaar versterken:

1. **A1-A5** (identiteit & anker-velden) — snelste beslissingen
2. **C1** (claim-unify tekstblok) — fundament voor andere bouwstenen
3. **C3, C5, C6** (element vereenvoudiging + voorbeelden unify)
4. **B2** (definitie/substantie/rationale groep)
5. **B4** (keuzekader vs synthese)
6. **C4** (weergaven brainstorm) — afhankelijk van C1
7. **D1, D2** (enums) — nadat structuur vast
8. **E1, E2** (rollen) — laatste

Welke cluster eerst?

---

## Beslissings-tracker (in te vullen tijdens discussie)

| # | Onderwerp | Beslissing | Status |
|---|---|---|---|
| A1 | naam.andere_talen / synoniemen | ✅ drop andere_talen; optioneel `vertaling` voor non-NL primair; synoniemen alleen gangbaar | besloten |
| A2 | dekt_tdks merge met linked_anchors | ✅ merge naar `ankers` | besloten |
| A3 | primary_po houden / drop / array | ✅ drop | besloten |
| A4 | tags drop | ✅ drop | besloten |
| A5 | cross_po drop | ✅ drop | besloten |
| A6 | changelog.wijziging maxLength | ✅ 300, mag concreet | besloten |
| B1 | voorkennis_leespad drop / operatie | ✅ operatie `leespad_aanvullen` | besloten |
| B2 | definitie/substantie/rationale groeperen | ✅ BEHOUD trio onder `kern`-wrapper. Drie tekst-objecten (alle optioneel, ≥1 verplicht). Comment: definitie kan hard (juridisch) of zacht (uitleg) zijn — geen structuur-verschil | besloten |
| B3 | gebruikscontext-positie (verduidelijking?) | ✅ misverstand, geen wijziging | besloten |
| B4 | keuzekader → syntheses lijst | ✅ array `syntheses`, sub-types TBD, kan aparte operatie | besloten |
| B5 | trigger/voordeel/risico → arrays | ✅ alle naar arrays | besloten |
| C1 | tekstblok/contextitem unify | ✅ unify naar `tekst` (schema + property NL); structuur `{tekst, grondslag, weergaven?, relaties?, rationale?}` | besloten |
| C2 | element trim | ✅ fractale recursie: element ≡ inhoud-structuur | besloten |
| C3 | element.beschrijving drop | ✅ drop. Element heeft fractaal `kern` als tekst-object (C2/B2 voldoende) | besloten |
| C4 | weergaven op meer plaatsen | ✅ weergaven optioneel op elk tekst-object (kern.definitie/substantie/rationale, element.kern.*, contextitems). Render kiest of/hoe te tonen | besloten |
| C5 | verwijst_naar | ✅ drop element.verwijst_naar; gebruik `relateert_naar` op claims/contextitems; top-level `relaties` = concept-naar-concept (geen from_element_id) | besloten |
| C6 | voorbeelden unify | ✅ unify naar `voorbeeld` met titel + context (intro); rest = elementen + weergaven | besloten |
| D1 | inhoud_type trim | ✅ 12 types: behoud begrip/stap/drempel/regel/uitzondering/vuistregel/mechanisme/risico/formule/principe/subconcept/beperking. Drop: berekening/vergelijking/moment_in_tijd/eigenschap/valkuil/voorwaarde. Merge stap_in_cyclus→stap. Rename component→subconcept. Plus element-properties `valkuilen[]` + `speelruimtes[]` | besloten |
| D2 | weergave_type trim + sub-schemas | ✅ drop `voorbeeld` (was nooit weergave); beslisboom blijft; geen nieuwe types in JSON (alleen rapporteren); detail-schemas voor boeking/balans/tabel | besloten |
| E1 | rol-set | ✅ behoud 5 rollen (adviseur/boekhouder/auditor/fiscaal/begeleider) | besloten |
| E2 | rollen_per_perspectief hiërarchie | ✅ vereenvoudig naar `accountant_perspectieven` (1 niveau weg) | besloten |
| E3 | rol-element sturing | ⏳ na wave-2 met meer rol-data; nu licht-prompt-discipline | uitgesteld |
| B4 | keuzekader → synthese generiek | | open |
| B5 | trigger/voordeel/risico → arrays | | open |
| C1 | tekstblok/contextitem unify | | open |
| C2 | element trim | | open |
| C3 | element.beschrijving drop | | open |
| C4 | weergaven op meer plaatsen + toelichting | | open |
| C5 | verwijst_naar | | open |
| C6 | voorbeelden unify naar titel-only | | open |
| D1 | inhoud_type trim naar 12 | | open |
| D2 | weergave_type trim + sub-schemas | | open |
| E1 | rol-set terug naar 5 | | open |
| E2 | rollen_per_perspectief hiërarchie | | open |
| E3 | rol-element sturing | | open |
