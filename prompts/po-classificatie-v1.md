# Prompt: Programmaonderdeel-classificatie — PO-CLASSIFICATIE v1

**Status**: permanent prompt-artefact
**Output**: voegt `programmaonderdeel_ids: [string]` veld toe aan elke `_interpretaties/<examen>/<vraag-id>.json`
**Schema-bump**: interpretatie v1.1 → v1.2 (additief, één nieuw veld)
**Spec-referentie**: ADR-024 (uitbreiding voor minicursus-integratie) + ADR-002 (PO-scoping)
**Model**: subagent (lokaal Claude Code) — Sonnet. **Geen** `anthropic.Anthropic()`-call.

---

## 1. Rol

Je classificeert één examenvraag naar het meest passende programmaonderdeel (PO). Eén vraag = doorgaans één PO. Hoogstens twee bij echt dubbel-onderwerp. **Nooit drie of meer** — dan eerder een herkadering naar het meest centrale PO.

## 2. Input

- Het interpretatie-artefact: `data/programma/examen_vragen/_interpretaties/<examen_id>/<vraag_id>.json` (v1.1)
- De PO-definities: `data/programma/programma.json` (top-level `programmaonderdelen[]`, met velden `code`, `titel`, `intro_tekst`, `taken`, `kenniselementen`)

## 3. PO-catalogus

| Code | Titel |
|---|---|
| 1.1 | Algemene boekhouding |
| 1.2 | Boekhoudrecht en jaarrekeningenrecht |
| 1.3 | Analyse en kritische beoordeling van de jaarrekening |
| 1.4 | Geconsolideerde jaarrekening en wetgeving betreffende de geconsolideerde jaarrekening |
| 1.5 | Beginselen van de Europese wetgeving en internationale boekhoudkundige normen |
| 1.6 | Externe controle |
| 1.7 | Interne controle |
| 1.8 | Analytische boekhouding en management accounting |
| 1.9 | Financiële analyse en fundamentele principes van financieel bedrijfsbeheer |
| 2.1 | Algemene beginselen van fiscaal recht |
| 2.2 | Personenbelasting |
| 2.3 | Vennootschapsbelasting |
| 2.4 | Belasting over de toegevoegde waarde (BTW) |
| 2.5 | Fiscale procedure |
| 2.6 | Registratie- en successierechten |
| 2.7 | Regionale en lokale belastingen |
| 2.8 | Europees en internationaal fiscaal recht |
| 3.0 | Vennootschaps- en verenigingsrecht en insolventiewetgeving |
| 4.0 | Deontologische beginselen in verband met het beroep en beginselen op het vlak van antiwitwaswetgeving |

Lees de volledige PO-definities (taken + kenniselementen) in `data/programma/programma.json` voor elk PO dat je serieus overweegt.

## 4. Output

Voeg één veld toe aan het interpretatie-JSON:

```json
"programmaonderdeel_ids": ["1.4"]
```

Of in zeldzame dubbel-onderwerp-gevallen:

```json
"programmaonderdeel_ids": ["2.3", "3.0"]
```

Schrijf terug naar dezelfde file via `Path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")`.

**Volgorde**: voeg `programmaonderdeel_ids` toe direct na `themas` (alfabetisch-logische plek), maar als de JSON-schrijfvolgorde anders is mag dat ook. Behoud `schema_versie` op `"1.1"` — dit is een additieve uitbreiding die we als schema 1.2 erkennen na de batch.

## 5. Discipline-regels

### 5.1. Eén PO is de regel

De meeste examenvragen hebben **één** primair onderwerp dat duidelijk in één PO valt. Voorbeeld:
- Vraag over interne controle bij vorderingen → `["1.7"]`
- Vraag over WVV-vennootschapsvormen → `["3.0"]`
- Vraag over BTW-aftrek → `["2.4"]`

### 5.2. Twee PO's bij echt dubbel-onderwerp

Hoogstens **twee** als de vraag wezenlijk twee onderwerpen combineert die elk substantieel zijn voor het antwoord. Voorbeeld:
- "Boek de vennootschapsbelasting op de afsluitingsdatum" → `["1.1", "2.3"]` (boekhouding + vennootschapsbelasting samen)
- "Welke fiscale gevolgen heeft de geconsolideerde herwaardering?" → `["1.4", "2.3"]`

Tweede PO toevoegen **alleen** als de vraag onbeantwoordbaar is zonder kennis uit beide PO's. Niet als één PO de hoofdmoot is en het andere alleen achtergrond.

### 5.3. Nooit drie of meer

Als je drie of meer PO's overweegt: terug naar het **meest centrale** PO. Een vraag die "echt overal raakt" past meestal in één hoofdcategorie + de rest is context. Kies één.

### 5.4. Themas zijn een hint, geen waarheid

`themas[]` (3–8 keywords per vraag) helpt bij oriëntatie, maar is vrij gekozen door de interpretatie-agent. Een vraag met thema "WVV" hoeft niet automatisch PO 3.0 te zijn — kijk naar de **vraagstelling** en **antwoord-vorm** voor het echte centrum.

### 5.5. Examen-context kan kleur geven

Sommige examens hebben karakteristieken (BIBF 2003/2008 = boekhouding-zwaar, 2024-1 = breed). Maar laat de **inhoud van de specifieke vraag** doorslaggevend zijn, niet het examen.

### 5.6. Wettelijke-context-vragen

Vragen over wetsartikelen (WVV, IB92, BTW-wetboek, ITAA-deontologie, ...) gaan naar het **inhoudelijke PO**, niet naar een algemeen "wettelijk" PO:
- WVV-art over kapitaalbescherming → 3.0 (vennootschapsrecht)
- WIB92-art over kostenaftrek → 2.2 of 2.3 (afhankelijk van persoon vs. vennootschap)
- BTW-art → 2.4
- Deontologische normen → 4.0

## 6. Werkwijze

Voor elke vraag:

1. Lees het interpretatie-artefact (`vraag_onderwerp`, `themas`, deelvragen-vraagstellingen, context-blokken).
2. Identificeer het primaire onderwerp (1 zin in je hoofd: "Deze vraag gaat over X").
3. Zoek de PO die dat onderwerp het scherpst dekt — lees `programma.json` voor de overwogen PO('s).
4. Test of een tweede PO **substantieel** bijdraagt (regel 5.2). Standaard: nee.
5. Voeg `programmaonderdeel_ids: [string]` toe en schrijf het JSON terug.

## 7. Wat NIET te doen

- Geen wijzigingen aan andere velden van de interpretatie
- Geen `schema_versie`-bump (we erkennen 1.2 als additief na de batch — laat 1.1 staan)
- Geen drie of meer PO-codes per vraag
- Geen anthropic.Anthropic()-calls
- Geen git-commits

## 8. Verificatie

- JSON parseert correct na schrijven
- `programmaonderdeel_ids` heeft 1 of 2 entries
- Elke entry is een geldige PO-code uit de catalogus (§3)
