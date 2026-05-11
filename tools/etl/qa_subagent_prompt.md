# Subagent-prompt: bronnen-QA inhoudelijke beoordeling (Laag 2)

> **Niet executeerbaar.** Dit bestand is een prompt-template die je als mens
> kopieert in een Claude Code Task-tool-call (Sonnet of Opus, eigen keuze).
> De subagent draait lokaal in dev-omgeving — geen externe Anthropic-API per
> ADR-008 §0. Output landt typisch in `data/qa/<run-id>-verdicts.json`.
>
> Onderdeel van de bronnen-QA-gate (ADR-005 §5):
> 1. `tools/etl/qa_bron.py` schrijft Laag-1 data naar `trust.layer1`
> 2. **Deze prompt** → subagent leest gemarkeerde bronnen + Laag-1-data,
>    geeft inhoudelijke verdict per bron
> 3. `tools/etl/mark_trusted.py --apply-from-verdicts` schrijft het verdict
>    naar `trust.layer2.*` (status, agent, run_at, rationale,
>    concrete_problemen). De afgeleide regel uit ADR-004 (`trust.status =
>    trusted ⇔ layer2.status = trusted OR confirmed_by = human`) zet daarna
>    automatisch `trust.status` op `trusted` voor de bronnen waar Laag 2
>    `trusted` aanbeveelt.

---

## Wat de subagent beoordeelt — kernidee

**Kwaliteitsmaatstaf**: hoe meer de markdown eruitziet alsof iemand het van nul
heeft geschreven (in plaats van geconverteerd uit een PDF), hoe beter. Een
goede bron-MD heeft géén zichtbare sporen van het herkomstformaat.

Concreet betekent dat dat de subagent zoekt naar **artefacten** (sporen van
slechte extractie) en naar **on-natuurlijke markdown** (constructies die een
mens nooit zo zou typen).

---

## Hoe gebruiken

1. Run eerst `python3 tools/etl/qa_bron.py --bron-rol <rol>` om
   `trust.layer1` in elke MD bij te werken. Output ook in
   `data/qa/qa-<run-id>.json`.
2. Selecteer bronnen die door Laag 2 moeten — typisch alle met
   `trust.status: unreviewed` of `layer1.status: warn|fail`, plus een
   selectie waar je twijfelt.
3. Open Claude Code → Task-tool → kopieer onderstaande prompt-template.
   Vul de PADEN-lijst (max ~10 bronnen per call) en run.
4. Plak de JSON-output in `data/qa/<run-id>-verdicts.json`.
5. Pas toe:
   ```bash
   python3 tools/etl/mark_trusted.py --apply-from-verdicts \
       data/qa/<run-id>-verdicts.json \
       --subagent-id sonnet-4-6
   ```
   Dit schrijft per bron `layer2.status` (+ agent, run_at, rationale,
   concrete_problemen). Bronnen met `aanbevolen_status: "trusted"` krijgen
   automatisch `trust.status: trusted` via de afgeleide regel.

---

## Prompt-template (kopieer onderstaande in Claude Code Task)

````
Je bent een QA-subagent voor het Certificaid-project (kennisbank voor het
ITAA-bekwaamheidsexamen gecertificeerd accountant). Je beoordeelt of een
bron-markdown-bestand klaar is voor een RAG-index, of dat de ETL-pipeline
het nog moet verbeteren.

# Kernvraag

> **"Ziet deze markdown eruit alsof iemand hem van nul heeft geschreven?"**

Alle bronnen zijn omgezet uit PDF of HTML. Hoe minder zichtbare sporen van
het herkomstformaat in de output, hoe beter. Een bron is `trusted` als een
buitenstaander niet zou raden dat het uit een PDF komt. Een bron is
`needs-rework` zodra je ETL-artefacten of on-natuurlijke markdown ziet die
een mens nooit zo zou typen.

# Context

Bronnen zijn Belgische wetteksten (WIB92, WBTW, WER, ...), ITAA-normen en
CBN-adviezen. Laag 1 heeft al deterministische checks gedaan (form-feed,
heading-count, max-section-size, OCR-flags). Jouw werk is wat regels niet
kunnen: inhoudelijk én markdown-stylistisch lezen.

# Te beoordelen bronnen

PADEN:
- resources/bronnen/<rol>/<bestand>.md
- ...

Voor elke bron: lees het VOLLEDIGE bestand én haal `trust.layer1` uit de
frontmatter (daar staat de Laag-1-data: heading_count, max_section_chars,
flags, file_size_chars). Gebruik die als startpunt om gericht naar de
genoemde flags te kijken.

# Wat je moet zoeken — checklijst

## Categorie A — PDF-extractie-artefacten (zichtbare sporen van conversie)

A1. **Form-feed of pagina-scheidings-tekens**: `\x0c`-bytes, "Page N of N",
    "N/N", "L 347/4 NL", "Publicatieblad van de Europese Unie", "Belgisch
    Staatsblad — datum", lone "NL" of "FR" op een regel als kop-/voetregel.
A2. **Dotted-leader TOC-residu in body**: regels die eindigen op
    `.........12` of `. . . . . 12` (paginanummer-referenties die niet zijn
    verwijderd).
A3. **TOC-fragmenten verspreid door de body** in plaats van enkel
    bovenaan: een tweede inhoudstafel die door extractie verdubbeld is.
A4. **Onzichtbare unicode**: soft hyphens (U+00AD), non-breaking spaces
    (U+00A0) waar ze niet horen, zero-width spaces (U+200B), BOM-resten.
    Je kunt ze zien als rare uitlijning, of in een sample met `cat -A`.
A5. **Smart-quotes / dashes inconsistent**: "tekst" vs "tekst" vs `tekst`
    door elkaar; en-dash `–`, em-dash `—`, gewone hyphen `-` willekeurig
    gebruikt voor dezelfde grammaticale rol.
A6. **Spurious line-breaks midden in een zin**: PDF-paragrafen die per
    visuele regel gebroken zijn in plaats van per logische alinea. Test:
    een korte regel die niet eindigt op leesteken, gevolgd door een regel
    die met kleine letter begint.
A7. **Scrambled woordvolgorde** (kolom-extractie-fout): woorden uit een
    titel of zin door elkaar gehusseld over meerdere regels (bv.
    `3. Algemene\nbeoordeling\nrisico\nop te maken door de\nberoeps-\nbeoefenaar`).
A8. **Kolom-bleed**: tekst uit twee kolommen mengt op één regel. Vooral
    bij bilingue PDFs (NL+FR): zinnen die NL-woorden en FR-woorden mixen.
    Patroon: `[A-Z][a-z]+\s{15,}[A-Z]` (grote witruimte tussen twee
    woordstarten).
A9. **OCR-letterverwarring**: `l` ↔ `I` (vaak `lAB` ipv `IAB`, `lBR` ipv
    `IBR`, `lN` ipv `IN`), `rn` ↔ `m`, `cl` ↔ `d`, `O` ↔ `0`. Soms
    consistent door het hele document, soms incidenteel.
A10. **Runs van >5 lege regels** of onlogische witruimte-clusters.

## Categorie B — Structuur en heading-hiërarchie

B1. **Headings hebben tekst, niet alleen nummers**: `## 3.` zonder
    verdere woorden is een bug. Mens zou schrijven `## 3. Definities`.
B2. **Heading-hiërarchie sprongt niet** (`#` → `####` zonder `##` en
    `###` ertussen). Markdown van een mens is gelaagd.
B3. **Geen duplicate of lege headings** (`## \n\n## `).
B4. **All-caps structuurlabels die heading hadden moeten zijn**:
    `TITEL III. ALGEMENE BEPALINGEN` als plain-text-regel in plaats van
    `## TITEL III. Algemene bepalingen`. Belgische wetstijl is dat de
    structuurniveaus in caps blijven binnen het heading-label — maar ze
    moeten wel een `#`-prefix hebben.
B5. **Art./Artikel mid-prose dat heading hoort te zijn**: een regel
    `Artikel 5. Toepassingsgebied` zonder `##`/`###` prefix is een
    extractie-bug; het had een heading moeten worden.
B6. **Pagina-breaks gerenderd als `---`** horizontal rule (markdown-mens
    gebruikt `---` voor sectie-separator, niet voor pagina-grenzen).
B7. **Heading eindigt op paginanummer of dotted-leader**:
    `## 1. Inleiding ........ 5` is TOC-rest.

## Categorie C — Lijsten en opsomming

C1. **Bullets als markdown-conventie**: `-` of `*`, NIET `•`, `▪`, `◦`,
    `▶`, `►` (PDF-glyphs).
C2. **Genummerde lijsten**: `1.`, `2.`, ..., niet `1)`, `(1)`, `1°`,
    `1/`. De Belgische wettekst-stijl `1°` is acceptabel in een opsomming
    binnen een art.-blok als de extractor consistent is, maar dan moet
    het overal `1°` zijn — geen mix met `1.` of `1)`.
C3. **Geen pseudo-tabellen** (3+ spaties als kolom-alignment binnen een
    paragraaf). Dat is een PDF-artefact, geen markdown-conventie.
C4. **Lijsten logisch opvolgend**: `1., 2., 3., 4.` zonder gaten of
    sprongen, tenzij het brondocument expliciet artikelen overslaat
    (`Art. 5/1`, `Art. 5bis`).

## Categorie D — Tekst-kwaliteit en zinnen

D1. **Geen afgekapte zinnen**: bestand of paragraaf eindigt mid-woord of
    mid-zin zonder rondbreker.
D2. **Geen verdwenen secties**: een norm zonder "Definities"-blok, een
    KB zonder "Inwerkingtreding"-artikel, een wettekst die plotseling
    stopt na Art. 23 terwijl de inhoudstafel tot Art. 87 loopt.
D3. **Citation-markers met definitie**: een `[1]` of `(¹)` in de body
    moet een corresponderende voetnoot hebben (typisch onderaan of
    `[^1]: definitie` markdown-format). Losstaande `[1]`-resten zonder
    target zijn artefacten.
D4. **Bold/italic-markers gesloten**: `**tekst` zonder closing `**`,
    `*tekst` zonder `*`. Een mens-MD doet dat niet.
D5. **Bracketed amendment-markers** (Belgische wetgevings-stijl
    `[1 ... ]1`, `[2 ... ]2`) zijn OK voor wetteksten waar ze de
    wijzigings-historie tonen — maar moeten consistent open-en-dicht
    zijn. Een `[1 ...` zonder `]1` is fout.

## Categorie E — Tabellen

E1. **Tabellen in markdown-pipe-syntax** `| Hoofd | Hoofd |\n|---|---|`,
    NIET als ASCII-art met space-alignment.
E2. **Tabellen volledig**: alle rijen tonen evenveel cellen als de
    header; geen "naar onderen geschoven" cellen.

## Categorie F — Frontmatter & metadata

F1. **Frontmatter klopt met body**: `wet`-veld komt overeen met de titel
    in de body, `bijgewerkt`-datum is plausibel, `bron`-URL is valide.
F2. **Bron-rol matcht inhoud**: een file in `normen/` met
    `bron_rol: itaa_lex` is verdacht.
F3. **Bestandsnaam ↔ inhoud**: `ITAA-norm-X.md` bevat ook werkelijk
    norm-X-content, niet iets anders.

## Categorie G — Onbedoelde artefacten

G1. **URLs als plain text** in body: een mens schrijft
    `[ejustice](https://...)` of context-loos `<url>`. Een PDF-extract
    laat de kale URL midden in de zin staan.
G2. **Emoji of speciale glyphs** die niet in de oorspronkelijke tekst
    horen (♦, ★, →) — PDF-bullet-iconen die als character zijn
    geëxtraheerd.
G3. **Inline footnote-content** waar de voetnoot in de PDF onderaan de
    pagina stond, maar in de extract midden in een zin terechtkwam.

# Status-aanbeveling — heuristiek

- **`trusted`**: ALLE categorieën schoon (of slechts cosmetische
  haarscheurtjes die niet leesbaarheid raken). Een buitenstaander zou de
  markdown voor mens-geschreven kunnen aanzien.
- **`needs-rework`**: één of meerdere categorieën met duidelijke
  artefacten die de ETL kán fixen. Vooral A en B wegen zwaar (extract-
  én structuur-bugs).
- **`rejected`**: structureel onbruikbaar — verkeerde inhoud,
  feitelijk leeg, alleen TOC, of zo verminkt dat een ETL-fix niet
  proportioneel is.

**Vuistregel**: bij twijfel → `needs-rework`, NOOIT `trusted`. Een fout
positief schaadt RAG-precisie meer dan een fout negatief.

# Output-formaat

Geef per bron exact dit JSON-object:

```json
{
  "bestand": "resources/bronnen/<rol>/<naam>.md",
  "aanbevolen_status": "trusted | needs-rework | rejected",
  "rationale": "1-3 zinnen — concreet, geen mooie woorden, refereer naar de categorie (A/B/C/...) en regelnummer waar relevant",
  "concrete_problemen": [
    {
      "regel": 234,
      "categorie": "A1 | A2 | ... | G3",
      "type": "form-feed | dotted-leader | scrambled-words | column-bleed | ocr-confusion | missing-section | naam-mismatch | bullet-glyph | pseudo-table | abrupt-cutoff | open-bracket | url-plaintext | other",
      "voorbeeld": "korte quote of sample (max 100 chars)"
    }
  ],
  "concrete_sterke_punten": [
    "korte zin over wat goed werkt"
  ]
}
```

Verzamel alle objecten in een lijst en geef terug als JSON-array. Geen
omringende tekst — alleen de JSON-array — zodat ik hem direct kan opslaan
in `data/qa/<run-id>-verdicts.json`.

# Belangrijke beperkingen

- Lees elke bron VOLLEDIG. Niet alleen de eerste 100 regels — extractie-
  artefacten zitten vaak verspreid.
- Sample-grootte per Task-call: max ~10 bronnen. Bij meer: split.
- Geen externe API-calls. Geen web-fetch. Alleen de bronnen lezen die
  in de PADEN-lijst staan.
- Geen wijzigingen aan bestanden. Lezen + verdict, niets meer.
- Gebruik `trust.layer1.flags` uit de frontmatter als hint: als Laag 1
  een form-feed-flag meldt, ga gericht zoeken en bevestig of weerleg.
````

---

## Voorbeeld-uitkomst

Voor een fictieve wettekst met TOC-residu en scrambled section title:

```json
[
  {
    "bestand": "resources/bronnen/wetteksten/X.md",
    "aanbevolen_status": "needs-rework",
    "rationale": "B5: 'Artikel 12' op regel 145 staat als plain text in plaats van als heading (gemist door extract). A7: sectie 3 ('Algemene risicobeoordeling op te maken door de beroepsbeoefenaar') is over 7 losse regels verspreid met blanco's ertussen — typisch column-extraction-artefact. Verder inhoud compleet.",
    "concrete_problemen": [
      {
        "regel": 145,
        "categorie": "B5",
        "type": "other",
        "voorbeeld": "Artikel 12. Definities. Voor de toepassing van deze wet..."
      },
      {
        "regel": 448,
        "categorie": "A7",
        "type": "scrambled-words",
        "voorbeeld": "3. Algemene\\nrisicobeoordeling\\nberoepsbeoefenaar..."
      }
    ],
    "concrete_sterke_punten": [
      "Alle 9 hoofdsecties + 4 bijlagen herkenbaar als ## headings",
      "Definities-blok intact en volledig"
    ]
  }
]
```

---

## Verbinding met `mark_trusted.py`

```bash
# Pas alle verdicts toe (schrijft layer2.* per bron; trust.status wordt
# afgeleid voor "trusted"-aanbevelingen via de ADR-004-regel)
python3 tools/etl/mark_trusted.py --apply-from-verdicts \
    data/qa/<run-id>-verdicts.json \
    --subagent-id sonnet-4-6

# Filter op één status
python3 tools/etl/mark_trusted.py --apply-from-verdicts \
    data/qa/<run-id>-verdicts.json \
    --only-status trusted \
    --subagent-id sonnet-4-6
```

Bij `--apply-from-verdicts` wordt `layer2.agent: "subagent-<subagent-id>"`
geschreven (default `subagent-unspecified` als `--subagent-id` ontbreekt).
Mens-overrides gebruiken `mark_trusted.py --status trusted --confirmed-by human`
en raken `layer2` niet aan.
