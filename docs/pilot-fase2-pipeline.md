# Pilot Fase 2 — Schema 2.0 herextract-pipeline

**Status**: werkdocument (geen ADR)
**Verband**: ADR-025 (schema 2.0), EXTRACT v5, VERIFY v3
**Doel**: pilot-run om EXTRACT v5 + schema 2.0 te valideren op echte concept-volumes binnen 24–36 u

---

## Doel & succescriteria

**Doel**: 460+ bestaande records herextract'en in schema 2.0 met behoud van inhoudelijke kennis + opvulling van didactische tekortkomingen (rol × perspectief · economische substantie · kader-cross-links).

**Succescriteria pilot**:
- 30–50 records geherextract op één PO als referentie
- ≥ 80 % van records voldoet aan kind-completeness (VERIFY)
- ≤ 15 % hallucinatie-risico (VERIFY bron-validatie)
- Geen catastrofale data-loss (oude records gearchiveerd, herstelbaar)
- Mens-in-de-loop steekproef bevestigt kwaliteits-stijging t.o.v. 1.6

**Succescriteria Fase 2 volledig**:
- Alle 460+ records in 2.0
- Kader-fiches voor 5–8 belangrijke domeinen (jaarrekeninganalyse, uitkering, financiering, …)
- Familie-fiches waar gepast
- ≥ 80 % kind-completeness over alle records
- Cross-PO-completeness: geen record dat "fiscaal volgt later" zegt

---

## Pre-pilot voorbereiding

### Foundations check (eenmalig, klaar in 2026-05-21)

- [x] ADR-025 spec
- [x] EXTRACT v5 prompt
- [x] VERIFY v3 prompt
- [x] 8 mockup-referentie-fiches in `content/experiment/`
- [ ] Records-API soft-validator update (herkent 2.0 + 1.5/1.6) — uit te voeren
- [ ] Archief-mechanisme: `data/concepten/_archive/v1.x/` aanmaken — uit te voeren
- [ ] Bronnen-werk: cijferzakboekje + extra fiscale bronnen (parallel, jouw werk)

### Wave-planning per PO

Volgorde voor pilot (kleine controleerbare batch eerst):

1. **Wave 0 (pilot)**: PO 1.1 — kern boekhoudkundige operaties (~30–50 records)
2. **Wave 1**: PO 1.x — andere boekhoud-gerichte PO's
3. **Wave 2**: PO 2.x — fiscaliteit
4. **Wave 3**: PO 3.x — vennootschapsrecht
5. **Wave 4**: PO 4.x — audit
6. **Wave 5+**: overige PO's
7. **Wave laatste**: kader- en familie-fiches die over alle waves heen relevant zijn

**Cross-PO-completeness**: per record worden ALLE relevante PO's in één extract afgehandeld. Bv. obligatielening (gestart in wave 0 voor PO 1.1) krijgt meteen ook fiscale + audit perspectieven mee.

---

## Pilot run — Wave 0

### Stap 1 — Archivering

```bash
mkdir -p data/concepten/_archive/v1.x
# Identificeer records gelinkt aan PO 1.1
python3 -c "
import json, pathlib
records = pathlib.Path('data/concepten/records').glob('*.json')
po11_records = []
for r in records:
    d = json.loads(r.read_text())
    if any(a.startswith('1.1') for a in d.get('linked_anchors', [])):
        po11_records.append(r.name)
print('\n'.join(po11_records))
" > data/concepten/_archive/v1.x/po11-record-list.txt

# Move (niet copy — we willen geen verwarring)
while IFS= read -r f; do
  cp "data/concepten/records/$f" "data/concepten/_archive/v1.x/$f"
done < data/concepten/_archive/v1.x/po11-record-list.txt
```

Records blijven leesbaar in archief; nieuwe versies komen naast bestaande tot we de oude bewust verwijderen.

### Stap 2 — Subagent-fleet

Voor parallelle extract: één Opus-subagent per ~5 records. Bij 50 records dus ~10 subagents tegelijk.

Orchestrator-prompt (sketch):
```
Je orchestreert een parallelle herextract-wave. Verdeel de meegeleverde record-lijst over 10 subagents (5 records elk). Elke subagent krijgt:
- prompts/concept-extractie-v5.md als systeem-instructie
- content/experiment/obligatielening-v7.md (+ 2-3 andere mockups) als in-context referentie
- 5 specifieke records uit archief + alle relevante anchors + RAG-access

Resultaat: nieuwe 2.0-records via records-API geschreven.
```

Subagent-prompt per batch:
```
Lees prompts/concept-extractie-v5.md voor instructies + de drie referentie-fiches uit content/experiment/.
Herextract deze 5 records in 2.0-formaat:
- record-1, record-2, record-3, record-4, record-5

Voor elk: lees archief-versie als seed, raadpleeg RAG voor extra bronnen, identificeer kind, volg top-volgorde, schrijf via save_record.
```

### Stap 3 — VERIFY-pass (na elke wave)

```bash
python3 -m tools.extractie.verify --prompt prompts/concept-verify-v3.md \
  --records "1.1.*" \
  --rapport-out data/extractie/verify-reports/wave-0-rapport.md
```

VERIFY draait soft — schrijft suggesties naar `gaps.json` en het rapport. Geen blocker.

### Stap 4 — Steekproef-review (mens-in-de-loop)

10 % van records (5 uit 50): handmatig lezen in Quartz-render, vergelijken met archief-versie.

Vragen voor de review:
1. Is de nieuwe versie didactisch sterker?
2. Bevat ze alle inhoud van de oude versie (geen verlies)?
3. Past de rol × perspectief structuur?
4. Werken de cross-record-edges?
5. Welke patronen zie ik dat naar prompt-aanpassing wijzen?

### Stap 5 — Beslismoment

Na pilot:
- ✅ Doorgaan met Wave 1: criteria gehaald, prompt OK
- 🔁 Prompt-aanpassing: enkele iteraties op EXTRACT v5 + opnieuw pilot
- ❌ Schema-revisie: pilot onthult fundamentele tekortkoming → ADR-025 bijwerken

---

## Volledige Fase 2 — schaling

### Parallelle waves

Na succesvolle pilot:
- Waves 1–5 kunnen **parallel** lopen — verschillende PO's, verschillende subagent-fleets
- Cross-PO-completeness garandeert dat records in één wave volledig zijn

Voorbeeld: bij 8 concurrent waves van 50 records elk → 400 records in één nacht-batch. Per record gemiddeld ~10 min Opus-tijd → totaal 67 u Opus-tijd, parallel verdeeld over 8 fleets → ~8 u wandklok.

### VERIFY tussendoor

VERIFY draait per wave automatisch — bevindingen accumuleren in `gaps.json` voor latere refining-passes (Fase 3).

### Bronnen-stroom (parallel)

Jouw bronnen-werk (Cijferzakboekje + extra fiscale bronnen) loopt parallel:
- Nieuwe bronnen → tools/etl pipeline → RAG-index update
- Records met `te_verifieren`-claims op nieuwe bronnen kunnen via VERIFY ge-upgrade worden naar `grounded`
- Dit gebeurt in Fase 3 (refinement), niet in Fase 2 (initial extract)

---

## Fase 3 — refinement

Na Fase 2: een refinement-loop:
- VERIFY suggesties verwerken (bv. voorbeeld_ontbreekt → bijwerken)
- Hallucinatie-risico claims onderzoeken (handmatig of via gerichte sub-pass)
- ⚠️ → ⚖️ upgraden waar nieuwe bronnen het toelaten
- Cross-record edges aanvullen
- Kader- en familie-fiches verbeteren met inzichten uit specifieke leden

Geen tijdsdoel; doorlopend werk.

---

## Renderlaag — parallel aan Fase 2

Quartz-component-update gebeurt parallel aan extract:
- Collapsible secties (default open: 1-2-3-4; default dicht: 7-8-9-10)
- Element-vocabulaire-renderers (boeking · balans-snapshot · t-rekening · …)
- Rol × perspectief layout (accordeon of matrix-grid)
- Familie-recursie-component (uitvouwbare boom)
- Browser-state-persistentie voor confidence-keuze (jouw "vrouw-confidence"-idee — default dicht voor non-essentiële, opt-in voor diepere lezing)

Geen blokkering voor extract — markdown-render werkt al; collapsible is verfijning bovenop.

---

## Risico's & mitigatie

| Risico | Mitigatie |
|---|---|
| Data-loss bij herextract | Oude records in `_archive/`; herstelbaar |
| Tijdsdruk Fase 2 | Parallelle subagent-fleet; cross-PO-completeness per record |
| Kwaliteits-regressie | VERIFY soft-pass + mens-in-de-loop steekproef |
| Records-API timeout bij batch | Existing cold-start-mitigatie (60 s eerste call); subagents zelf via worktree-discipline |
| Hallucinatie in 🧭-claims | VERIFY hallucinatie-detectie; 🧭-gradatie-regel in prompt |
| Kader-fiche-cyclus (afhankelijkheden) | Pre-EXTRACT scan; orchestrator beslist kader-eerst-volgorde |

---

## Open punten

- Records-API soft-validator-implementatie: uit te voeren in Python (`tools/lib/records_api.py` — `_valideer_schema_versie` helper)
- Archief-pad-conventie: `data/concepten/_archive/v1.x/po-XX/` of plat? Voorlopig plat.
- Hoe bewaren we `_provenance.verify_overrides`-history over meerdere passes? Append-only lijst.
- Render-component-spec: aparte werkdoc bij Quartz-update.

---

## Eerste acties (vandaag)

1. ADR-025 + prompts gepushed → klaar
2. Bronnen-werk (jij) parallel starten
3. Records-API soft-validator implementeren (Python-werk — kleine PR)
4. Archief-mechanisme uitwerken (Bash + Python helper)
5. Subagent-orchestrator-prompt finaliseren
6. Pilot-wave 0 op PO 1.1 launchen
