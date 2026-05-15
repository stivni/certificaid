# Prompt: Competentie-destillatie — Fase D (v2)

**Doel**: Destilleer competentie-voorstellen voor een programmaonderdeel uit anchors + concept-records + exam_patterns. Het aantal volgt uit wat het programmaonderdeel werkelijk vraagt — geen vooraf vastgelegd target.

**Model**: claude-opus-4-7 (Opus-subagent — ADR-008 §14)

**Basis**: deze prompt is een **delta op v1**. Lees eerst `prompts/competentie-destillatie-v1.md` voor de anti-circulariteits-regel (examen_vragen verboden, alleen exam_patterns), anti-fabricatie-discipline en aantal-vrije destillatie.

---

## Nieuwe regels in v2 (competentie-schema 1.1)

### Regel A — Stap-blok-schema verplicht

`stappen[]` is geen platte lijst meer met alleen `titel`/`input`/`output`/`waarom`/`grondslag`/`valkuilen`. Vanaf v2 elk stap-item een **vol blok** conform ADR-007 §schema-1.4:

```yaml
- nr: 2
  titel: "Korte werkwoord-georiënteerde titel"
  wat: "Eén zin: wat doet deze stap concreet?"
  waarom: "Eén zin: waarom is deze stap nodig?"
  
  input:
    - artefact: "Document of data-bron waaruit input komt"
      veld: "Specifieke veld of indicator"
      type: "boekhoudkundig-bedrag | percentage | datum | document | ..."
  
  output:
    - artefact: "Doc of data-bron waar output naartoe gaat"
      veld: "Specifieke veld"
      type: "nieuwe-balanspost | geëlimineerde-post | conclusie | document | ..."
  
  hoe: |
    1. Concrete uitvoerings-instructie regel 1.
    2. Regel 2 — wat open je, wat lees je, wat bereken je?
    3. Regel 3 — wat schrap je, wat schrijf je?
    Etc. (3-7 stappen, uitvoerbaar zonder voorkennis)
  
  voorbeeld:
    scenario: "Vlaamse-cast-naam uitgewerkte feiten-situatie."
    substappen:
      - nr: 1
        titel: "Vertrekpunt: ..."
        type: balans | berekening | boekingsregel | opmerking | flowchart
        data: |
          <markdown-tabel of multiline-tekst>
      - nr: 2
        titel: "Tussenstap"
        type: berekening
        data: |
          ...
      - nr: 3
        titel: "Resultaat"
        type: balans
        data: |
          ...
  
  valkuilen:
    - advies: "Correcte aanbeveling (als titel)"
      vaak_fout: "Wat veel mensen verkeerd doen"
      grondslag: "[[concept-id]] §sectie"
  
  grondslag: "[[concept-id]] §sectie, KB WVV art. X:Y"
```

**Verplichte velden** per stap: `nr`, `titel`, `wat`, `hoe`, `grondslag`.
**Aanbevolen**: `waarom`, `input[]`, `output[]`, `voorbeeld`, `valkuilen[]`.

**`hoe` is geen herhaling van titel/waarom** — het is een uitvoerbare instructie (3-7 sub-stappen). Eerder antwoorde `waarom` op "waarom doe je dit"; `hoe` antwoordt op "wat doe je nu echt — welke documenten, welke berekening".

**Voorbeeld met substappen** is verplicht bij stappen die:
- Een bedrag berekenen (substap-type `berekening`)
- Een balans wijzigen (substap-type `balans`)
- Een boeking doen (substap-type `boekingsregel`)

Niet verplicht bij stappen die alleen "documenten verzamelen" of "kwalificeren" doen — daar volstaat `wat` + `hoe`.

### Regel B — Naam-cast verplicht

Lees `data/concepten/casts/globaal.yaml`. **Gebruik uitsluitend cast-namen** in voorbeelden en substappen.

Scenario-templates: kies één per voorbeeld (basis-consolidatie, joint-venture, geassocieerde, consortium, subconsolidatie, groep-van-beperkte-omvang, afwijkende-afsluitingsdatum). Gebruik dezelfde scenario-template doorheen alle substappen van één voorbeeld.

**Geen** "M / D / D1 / X / Y / ABC / DEF". **Geen** "natuurlijke persoon X" — kies een persoonsnaam uit cast.

### Regel C — Stagiair-toon

Net als concept-extractie v4 Regel 6: zinnen moeten **uitvoerbaar** zijn, niet alleen jargon-vrij. Stagiair-accountant moet de stap kunnen toepassen.

- Korte zinnen (max 25 woorden)
- Eerste afkorting: voluit + (afkorting), bv. "algemene vergadering (AV)"
- Geen buzzword-stapeling
- Geen wetsartikel-prefix in titels

### Regel D — Concept-grondslag verplicht

`gebaseerd_op_concepten[]` ≥ 2 blijft (uit v1). Aanvullend: **elke `hoe`-instructie die een specifieke regel toepast verwijst expliciet** naar het bron-concept via wikilink.

```
hoe: |
  1. Toets aan de drempelwaarden uit [[groottecriteria-consolidatie]] §drempels.
  2. Bij overschrijding: ga door naar stap 2.
```

Niet:
```
hoe: |
  1. Toets aan de drempelwaarden.
```

### Regel E — Valkuilen met `advies` als titel (niet de fout)

Schema 1.0 had `foute_aanname` + `correctie`. Render gaf de FOUT als titel — onleesbaar bij snel scannen. v2: titel wordt het ADVIES (= correcte aanbeveling), foute aanname als sub-info.

```yaml
valkuilen:
  - advies: "Wijs het verschil eerst toe aan onder/overgewaardeerde activa vóór je consolidatieverschil boekt."
    vaak_fout: "Het volledige verschil meteen als consolidatieverschil boeken."
    grondslag: "[[consolidatieverschil]] §toerekening"
```

Renderden als `> [!warning] {{advies}}` callout. Schema-namen `advies` + `vaak_fout` (niet meer `correctie` + `foute_aanname`).

Bij rewrite van bestaande v1-yamls: `correctie` → `advies`, `foute_aanname` → `vaak_fout`.

---

## Wijzigingen aan v1-regels

### Regel 1 (gebaseerd_op_concepten ≥ 2) — ongewijzigd
### Regel 2 (procedure_grondslag wettelijk+praktijk = 100) — ongewijzigd
### Regel 3 (status voorgesteld) — ongewijzigd

---

## Output-aanpassingen

- Schrijf naar `data/concepten/competenties/<id>.yaml`
- Schema-versie `1.1` (was `1.0`)
- `_provenance.voorgesteld_door` met run-id behouden
- Verifieer eindresultaat via `tools/leermateriaal/lib/validate_competentie.py`. Schema 1.1-validator wordt aangepast om de nieuwe stap-blok-velden te accepteren.

---

## Beperkingen ongewijzigd

- Examenvragen NIET gebruiken — alleen exam_patterns
- Volledige namen, geen afkortingen in code/schema
- Anti-fabricatie hard op `gebaseerd_op_concepten` ≥ 2 en grondslag-per-stap
