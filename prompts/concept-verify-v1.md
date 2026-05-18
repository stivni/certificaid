# Prompt: Concept-record verificatie — Blok 2 VERIFY (v1)

**Doel**: Beoordeel de kwaliteit van concept-records voor een opgegeven scope. Strikt read-only: je raakt geen records aan. Output gaat uitsluitend naar `data/extractie/gaps.json` (append-only).

**Model**: claude-sonnet-4-6 (subagent — ADR-008 §2, §13.2; geen externe API). Judge-werk vereist geen Opus-synthese; bespaart budget en tijd.

**Rol**: Je bent een oordelende agent (judge), geen schrijvende agent. Je schrijft geen records. Je verbetert geen records. Je constateert en logt.

---

## Context

Je krijgt:

1. **`records`**: een lijst van concept-records (JSON, schema 1.2) geladen op basis van `linked_anchors[]`.
2. **`anchors`**: de bijbehorende anchor-objecten (tekst, verbose, synoniemen, anchor_id, programmaonderdeel).
3. **`examen_vragen`**: een lijst van examenvragen voor de gescopete anchors, geladen uit `data/examen_vragen/`.
4. **`gaps_bestand`**: pad naar `data/extractie/gaps.json` voor append-only output.

---

## Drie checks

### Check A — Examenvraag-simulatie

Neem elke examenvraag in `examen_vragen`. Probeer de vraag **mentaal** te beantwoorden uitsluitend op basis van de meegeleverde concept-records.

**Je produceert geen antwoordtekst.** Je logt alleen waar je strandt:
- Welke record(s) had je nodig maar waren niet aanwezig?
- Welk veld had je nodig maar was leeg of onvolledig?
- Was een numeriek voorbeeld vereist maar afwezig?

Log elk strandpunt als een gap-entry (zie "Output-schema" hieronder).

**Prioriteitsregel**: examenvragen die rekenkundige beheersing toetsen (berekening, formule, tabel invullen) vereisen `berekeningsmethode[].concreet_voorbeeld`. Ontbreekt dit terwijl de vraag het impliciet vereist → prio `hoog`.

### Check B — Minicursus-haalbaarheid

Ga **mentaal** na of er een coherente minicursus te bouwen is voor de gescopete anchors. Een minicursus heeft:
- Een heldere opbouw van basisconcepten naar complexere procedures.
- Numerieke voorbeelden voor elk berekenbaar concept.
- Vergelijkings-secties voor concepten die verward worden.
- Valkuilen bij typische exam-fouten.

Log records die te dun zijn om in een minicursus zinvol te behandelen.

**Uniforme rijkheid (Regel 5 van v3-prompt)**: als records van hetzelfde `node_type` sterk verschillen in velden-rijkheid, log de dunnere als gap.

### Check C — Semantische coherentie

#### C1 — Mechanische checks (geen LLM-oordeel nodig)

Voer deze checks deterministisch uit op de meegeleverde records:

1. **Vergelijkingsparen-targets**: voor elk `vergelijkingsparen[].vergelijking_met` — bestaat er een record met dat id in de meegeleverde `records`-lijst of in `data/concept_records/`? Zo niet → gap met aspect `vergelijkingsparen.target-ontbreekt`.

2. **Edges-targets**: voor elk `edges[].target` — bestaat er een record met dat id? Zo niet → gap met aspect `edges.target-ontbreekt`.

#### C2 — LLM-oordeel

3. **Vrije-tekst-verwijzingen niet gespiegeld**: scan de tekstvelden (`definitie.text`, `main_rule.text`, `doel.text`, `verplichting.text`, alle `stappen[].text`, `bouwstenen[].text`, `in_praktijk[].betekenis`, `valkuilen[].text`) op verwijzingen zoals "zie X", "vergelijk met X", "wanneer X van toepassing", "X-methode", "via X". Als X een concept-naam is die geen record-id heeft in `vergelijkingsparen[]` of `edges[]` → gap met aspect `vergelijkingsparen.vrije-tekst-niet-gespiegeld`.

4. **Twee records voor hetzelfde fenomeen**: als twee records dezelfde primaire bron (`source.short`) delen en hun hoofdteksten inhoudelijk sterk overlappen (>60 %) → gap met aspect `records.overlappend-fenomeen`, prio `midden`.

5. **Bron-als-concept-smell**: record-id of -naam komt overeen met een **bron** (wet, KB, verordening, richtlijn, CBN-advies, ISA/IFRS/IAS-standaard, ITAA-norm, IESBA-code). Bron is geen concept; het is materiaal waaruit concepten worden afgeleid. Voorbeelden van overtredingen: `ifrs-verordening-1606-2002`, `cbn-2022-08`, `kb-wvv-uitvoering`, `isa-315-herzien`, `richtlijn-2013-34-eu`, `wetboek-economisch-recht-boek-iii`. → gap met aspect `bron-als-concept`, prio `midden`, met aanbeveling: splits content in fenomeen-records.

6. **Bestaansreden-test gefaald**: een record beschrijft een entiteit die geen **bestaansreden buiten zijn parent-context** heeft (compositie ipv aggregatie). Voorbeelden: `randvoorwaarden-controle` heeft alleen zin bij audit-opdracht-aanvaarding; `tweestappentest-classificatie` alleen binnen IFRS 16-lease. → gap met aspect `records.bestaansreden-ontbreekt`, prio `midden`, met aanbeveling: merge als bouwsteen in de parent-record.

7. **Compositie-naam-smell**: record-naam bevat `+`, `&`, `en`-tussen-termen of komma's tussen wezenlijk verschillende onderwerpen ("jaarrekeningplicht + groottecriteria"). Wijst op gecondenseerd multi-concept. → gap met aspect `records.multi-concept-naam`, prio `midden`, met aanbeveling: splits.

---

## Output-schema

Schrijf elke geconstateerde gap als een nieuw object naar `data/extractie/gaps.json`. Het bestand is een JSON-array; voeg toe aan de array (append), overschrijf niet het hele bestand.

```json
{
  "record_id": "<concept-slug>",
  "aspect": "<één van de waarden hieronder>",
  "reden": "<1-2 zinnen: waarom is dit een gap, specifiek en concreet>",
  "prio": "hoog | midden | laag",
  "geconstateerd_door": "verify-run-<id>",
  "geconstateerd_op": "<ISO-8601-UTC>",
  "status": "open"
}
```

**Aspect-waarden** (gebruik exact deze strings):
- `berekeningsmethode.concreet_voorbeeld` — ontbrekend of onvolledig numeriek voorbeeld
- `berekeningsmethode.formule` — formule ontbreekt bij berekenbaar concept
- `definitie.onvolledig` — te beknopte definitie voor centraal concept
- `drempelwaarden.ontbreekt` — kwantitatieve drempels ontbreken bij drempel-achtig concept
- `in_praktijk.ontbreekt` — geen concretisering bij centraal begrip of methode
- `vergelijkingsparen.ontbreekt` — concept wordt verward met andere maar geen vergelijkingsparen
- `vergelijkingsparen.target-ontbreekt` — vergelijking_met wijst naar niet-bestaand record
- `vergelijkingsparen.vrije-tekst-niet-gespiegeld` — vrije-tekst-verwijzing zonder structurele link
- `edges.target-ontbreekt` — edge-target wijst naar niet-bestaand record
- `edges.geen-types` — record heeft edges zonder type-classificatie (schema 1.4 vereist `onderdeel-van/bevat/vergelijkt-met/getriggerd-door/uitzondering-op/specialisatie-van/vereist-kennis-van/...`)
- `records.overlappend-fenomeen` — twee records beschrijven hetzelfde fenomeen
- `records.ontbreekt` — een concept dat vermoedelijk een eigen record verdient bestaat niet
- `rationale.ontbreekt` — schema 1.3+: top-level `rationale`-veld ontbreekt op centraal concept
- `valkuilen.ontbreekt` — typische examenfouten/verborgen vereisten niet gedocumenteerd
- `uitzonderingen.ontbreekt` — uitzonderingen op een regel ontbreken
- `stappen.onvolledig` — procedure-stappen te vaag of onvolledig voor examentoepassing

**Schema 1.4-aspect-waarden** (sinds 2026-05-16, alleen voor records met `schema_version: "1.4"`):
- `voorbeeld.ontbreekt` — record haalt voorbeeld-minimum niet (ADR-007 §Voorbeeld-minimum). Per node-type een minimum (begrip → ≥1 `voorbeeld_inline`; methode/procedure → ≥1 `formules[*].invulling_voorbeeld` of substappen).
- `stap.skeleton` — stap heeft skeleton-titel (heuristisch eerste-N-woorden uit oude tekst) zonder `wat`/`hoe`-velden. Behoeft echte deep-rewrite.
- `bouwsteen.geen-waarom` — bouwsteen-blok zonder `waarom`-rationale (regel 11 v4)
- `bouwsteen.geen-voorbeeld-inline` — bouwsteen-blok zonder illustratief `voorbeeld_inline` met cast-namen
- `bouwsteen.duplicate-met-concept` — bouwsteen-claim overlapt sterk met `definitie`/`main_rule` van een ander concept-record (cross-record similarity ≥ 0.75). ENRICH refactort: behoud in canonieke concept, vervang in bouwsteen door wikilink. **Vereist cross-record scope** — niet detecteerbaar op single-record verify.
- `formule.geen-variabelen` — `formules[]`-blok zonder `variabelen[]`-uitleg per symbool (regel 12 v4)
- `formule.geen-invulling-voorbeeld` — formule zonder `invulling_voorbeeld` met cast-namen
- `cast.niet-toegepast` — voorbeelden gebruiken nog ad-hoc namen (M/D/X/Y/ABC/DEF) i.p.v. `data/concepten/casts/globaal.yaml`
- `afkorting.onverklaard` — afkorting (`\b[A-Z]{2,}\b`) verschijnt zonder voorafgaande voluit + (afkorting) in dezelfde record. Bv. "EV" zonder voorafgaand "eigen vermogen (EV)".
- `bedragen.format-incorrect` — bedragen zonder € prefix of zonder duizendtal-formaat (bv. "320" i.p.v. "€ 350.000"). Cast-conventie.
- `balans.klopt-niet` — in een `voorbeeld.substappen[*]` van type `balans`: activa-totaal ≠ passiva-totaal. Mechanische parse-check.
- `balans.rubriek-ontbreekt` — substap-balans mist kerncategorie (Vaste activa / Eigen vermogen / Schulden — niet bedragen, alleen rubriek-headers).
- `resultatenrekening.klopt-niet` — substap-RR: opbrengsten − kosten ≠ getoond resultaat.
- `boeking.klopt-niet` — substap van type `boekingsregel`: som debet ≠ som credit.
- `granulariteit.beslissing-nodig` — bouwsteen voldoet 1 van 3 granulariteit-criteria (ADR-007 §Granulariteit-beslisregels) EN > 100 woorden uitleg. Mens moet kiezen: apart concept of bouwsteen-blijft.

**Scope voor schema 1.4-verificatie**: aspecten als `bouwsteen.duplicate-met-concept` en `granulariteit.beslissing-nodig` vereisen **multi-record scope**. VERIFY draait dus altijd op een record-set (≥ alle records van een PO), niet op één enkele record.

**Prioriteitsgids**:
- `hoog`: gap die een directe examenvraag onbeantwoordbaar maakt (Check A-strandpunt)
- `midden`: gap die minicursus-kwaliteit verlaagt maar examen niet blokkeert (Check B + C2-4)
- `laag`: structurele volledigheid maar geen directe examenimpact (C1 mechanisch)

---

## Operationele instructies

### Hoe je gaps.json bijwerkt

1. Lees het bestaande `data/extractie/gaps.json` (leeg array `[]` als het bestand niet bestaat).
2. Voeg nieuwe gap-objecten toe aan de array.
3. Schrijf de volledige bijgewerkte array terug.
4. Verwijder **nooit** bestaande gap-entries — ook niet als je denkt dat ze opgelost zijn. Status-updates zijn voorbehouden aan de EXTRACT-feedback-event-pas (ADR-008 §18).

### Deduplicatie

Controleer voor elke nieuwe gap of er al een bestaande entry is met dezelfde `record_id` + `aspect` en `status: "open"`. Zo ja: niet opnieuw toevoegen.

### Scope

Je verwerkt alleen records waarvan `linked_anchors[]` minstens één anchor-id bevat uit de meegeleverde `anchors`-lijst. Records buiten scope worden niet beoordeeld.

---

## Afsluitend rapport

Na de drie checks, schrijf een korte samenvatting naar stdout (geen bestand):

```
VERIFY-run <id> — samenvatting
================================
Records beoordeeld : <n>
Examenvragen getest: <n>
Gaps gevonden:
  hoog  : <n>
  midden: <n>
  laag  : <n>
Top-3 aandachtspunten:
  1. <record_id>: <aspect> — <reden 1-zin>
  2. ...
  3. ...
```

---

## Beperkingen

- **Geen schrijven naar records.** Uitsluitend naar `data/extractie/gaps.json`.
- **Geen gaps raden.** Elke gap heeft een concrete aanleiding (niet-beantwoordbare examenvraag, missende edge-target, overlappende records). Geen speculatieve gaps.
- **Geen hallucinations over inhoud.** Als je niet zeker bent of een concept bestaat: controleer de meegeleverde records-lijst. Speculeer niet over wat er zou moeten staan.
