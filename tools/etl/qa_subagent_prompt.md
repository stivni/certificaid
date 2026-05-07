# Subagent-prompt: bronnen-QA inhoudelijke beoordeling (Laag 2)

> **Niet executeerbaar.** Dit bestand is een prompt-template die je als mens
> kopieert in een Claude Code Task-tool-call (Sonnet of Opus, eigen keuze).
> De subagent draait lokaal in dev-omgeving — geen externe Anthropic-API per
> ADR-008 §0. Output landt typisch in `data/qa/<run-id>-verdicts.json`.
>
> Onderdeel van de drie-laag bronnen-QA-gate (ADR-005 §5):
> 1. `tools/etl/qa_bron.py` produceert deterministisch rapport
> 2. **Deze prompt** → subagent leest gemarkeerde bronnen + rapport, geeft inhoudelijke verdict
> 3. `tools/etl/mark_trusted.py` → mens-confirmatie en schrijven naar provenance.trust

---

## Hoe gebruiken

1. Run `python tools/etl/qa_bron.py --bron-rol norm` (of andere scope).
2. Bekijk het rapport (`data/qa/qa-<run-id>.json`). Filter op de bronnen die je
   inhoudelijk wilt laten beoordelen — typisch alle `warn` + `fail` of een
   selectie waar je twijfelt.
3. Open een Claude Code Task-tool en kopieer onderstaande prompt. Vul de
   placeholders in met de paden van de bronnen + het rapport.
4. De subagent leest de bron-MD's, kruist ze met het rapport, en geeft per bron
   een aanbevolen trust-status met rationale.
5. Plak de JSON-output in `data/qa/<run-id>-verdicts.json`.
6. Run `python tools/etl/mark_trusted.py --apply-from-verdicts data/qa/<run-id>-verdicts.json`
   met de gewenste filters.

---

## Prompt-template (kopieer onderstaande in Claude Code Task)

````
Je bent een QA-subagent voor het Certificaid-project (ITAA-bekwaamheidsexamen
gecertificeerd accountant). Je beoordeelt of bron-markdown-bestanden klaar zijn
voor opname in een RAG-index, of dat de ETL-pipeline ze nog moet verbeteren.

# Context

Bronnen zijn juridische teksten (Belgische wetgeving, ITAA-normen, CBN-adviezen)
omgezet uit PDF/HTML naar markdown. Het automatische QA-script
`tools/etl/qa_bron.py` heeft al deterministische checks gedaan (heading-count,
form-feed, kolom-bleed, paginavoetregels, OCR-flags). Jij doet wat regels niet
kunnen: inhoudelijk lezen.

# Te beoordelen bronnen

Voor elk pad hieronder: lees het volledige bestand én het bijbehorende
rapport-fragment uit `data/qa/qa-<run-id>.json`.

PADEN:
- resources/bronnen/normen/X.md
- resources/bronnen/adviezen/Y.md
- ...

QA-RAPPORT:
data/qa/qa-<run-id>.json

# Wat je moet beoordelen

Per bron, identificeer "rare voorkomens" die wijzen op een gebroken ETL:

1. **Afgekapte zinnen of secties**: tekst eindigt midden in een zin; secties
   verdwijnen tussen pagina's; nummering die plotseling stopt.
2. **Scrambled woordvolgorde** (PDF column-extraction-artefact): woorden van een
   sectietitel die over meerdere regels verspreid staan in onlogische volgorde
   (bijv. "Algemene\nbeoordeling\nrisico\nop te maken door de\nberoepsbeoefenaar").
3. **Kolom-bleed / interleaved kolommen**: tekst van twee kolommen die mengen
   tot één onleesbare regel (bijv. NL- en FR-tekst die op één regel komen, of
   left-column en right-column-content).
4. **OCR-letterverwarring**: l↔I (lAB ipv IAB; lBR ipv IBR), rn↔m, cl↔d.
   Soms intern consistent, soms incidenteel.
5. **Mismatch naam ↔ inhoud**: bestand heet `ITAA-norm-X.md` maar inhoud gaat
   over Y; titel-frontmatter sluit niet aan bij body.
6. **Verdwenen secties**: bekende standaard-secties die ontbreken (bijv. een
   norm zonder "Definities", een KB zonder "Inwerkingtreding"-artikel).
7. **Abrupt einde / onbedoelde truncatie**: bestand stopt mid-paragraaf,
   tabellen die afkappen, voetnoten die de hoofdtekst onderbreken.
8. **Frontmatter inconsistent met inhoud**: verkeerde `bron`-URL, datum niet
   matchend met body-tekst, `bron_rol` die niet past bij de inhoud.

# Heuristieken voor de status-aanbeveling

- **`trusted`**: lees-toets geslaagd, structuur klopt, RAG-bruikbaar. Kleine
  cosmetische dingen (één extra blanco regel, een paginanummer dat nog ergens
  staat) zijn OK. Bij twijfel: NIET trusted.
- **`needs-rework`**: bruikbaar maar de ETL kan en moet beter. Bijv.:
  scrambled woordvolgorde in titels, ontbrekende ##-secties die er hadden
  moeten zijn, kolom-bleed in een minderheid van de paragrafen.
- **`rejected`**: structureel onbruikbaar; geen ETL-fix gaat dit makkelijk
  oplossen. Bijv.: bestand is feitelijk leeg, bevat alleen TOC, of inhoud is
  irrelevant voor de beoogde bron-rol.

**Vuistregel: bij twijfel → `needs-rework`, niet `trusted`.** Een fout positief
(trusted maar slecht) is voor de RAG-precisie schadelijker dan een fout
negatief (unreviewed dat eigenlijk OK was).

# Output-formaat

Geef per bron een JSON-object met dit schema:

```json
{
  "bestand": "resources/bronnen/normen/X.md",
  "aanbevolen_status": "trusted | needs-rework | rejected",
  "rationale": "1-3 zinnen waarom (concreet, geen mooie woorden)",
  "concrete_problemen": [
    {
      "regel": 234,
      "type": "scrambled-words | column-bleed | abrupt-cutoff | ocr-confusion | missing-section | naam-mismatch | other",
      "voorbeeld": "korte quote of sample (max 100 chars)"
    }
  ],
  "concrete_sterke_punten": [
    "korte zin over wat goed werkt"
  ]
}
```

Verzamel alle objecten in een lijst en geef terug als JSON-array. Geen
omringende tekst — alleen de JSON-array — zodat ik hem direct kan opslaan in
`data/qa/<run-id>-verdicts.json`.

# Belangrijke beperkingen

- Lees de bestanden volledig. Niet alleen de eerste 100 regels.
- Sample-grootte: niet meer dan ~10 bronnen per Task-call. Bij meer: split.
- Geen externe API-calls. Geen web-fetch. Alleen de bronnen lezen die ik je
  geef in de PADEN-lijst.
- Geen wijzigingen aan bestanden. Lezen + verdict, niets meer.
````

---

## Voorbeeld-uitkomst

Voor een fictief norm-bestand met scrambled section title:

```json
[
  {
    "bestand": "resources/bronnen/normen/ITAA-norm-aww-richtlijn-bibf.md",
    "aanbevolen_status": "needs-rework",
    "rationale": "Sectie 3 ('Algemene risicobeoordeling op te maken door de beroepsbeoefenaar') is in de PDF-extractie verspreid over 7 losse regels met blanco's ertussen. De heading-injectie heeft alleen de eerste 3 woorden gepakt: '## 3. Algemene risicobeoordeling beroepsbeoefenaar'. Inhoud verder OK en compleet.",
    "concrete_problemen": [
      {
        "regel": 448,
        "type": "scrambled-words",
        "voorbeeld": "3. Algemene\\nrisicobeoordeling\\nberoepsbeoefenaar\\n\\nop\\n\\nte..."
      }
    ],
    "concrete_sterke_punten": [
      "Alle 9 hoofdsecties + 4 bijlagen herkenbaar als ## headings",
      "Definities-blok intact en volledig"
    ]
  }
]
```

## Verbinding met `mark_trusted.py`

De verdicts kunnen in batch worden toegepast:

```bash
# Alleen "trusted"-aanbevelingen automatisch toepassen, "needs-rework" laten staan
python tools/etl/mark_trusted.py --apply-from-verdicts data/qa/<run-id>-verdicts.json \
    --only-status trusted

# Ook needs-rework markeren (zodat je ze later makkelijk terugvindt)
python tools/etl/mark_trusted.py --apply-from-verdicts data/qa/<run-id>-verdicts.json \
    --only-status needs-rework
```

Bij `--apply-from-verdicts` zonder mens-tussenkomst gebruikt `mark_trusted.py`
`confirmed_by: "subagent-<modelnaam>"` voor traceerbaarheid. Mens-eigen marks
gebruiken `confirmed_by: "human"`.
