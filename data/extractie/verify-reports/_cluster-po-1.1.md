# Cluster-aggregatie verify-rapport — PO 1.1 boekhouding (Pass 2 sample, 10 records)

## Sample-context

- **Doel**: representatief sample van 10 PO 1.1-records om Pass 2-feedback te genereren voor prompt-verfijning + Pass 3 verbeter-acties.
- **Datum**: 2026-05-28.
- **Records verwacht**: 10 (`boekhouding`, `jaarrekening`, `dubbele-boekhouding`, `eindejaarsverrichtingen`, `balansschema-volledig`, `resultatenrekeningschema`, `waarderingsregels-jaarrekening`, `voorraden`, `voorzieningen`, `resultaatverwerking`).
- **Records effectief geverifieerd**: 7 (3 niet-bestaand — out-of-sample, zie sub-rapporten).
- **Schema-validatie**: alle 7 records valide volgens `schema-2.2.schema.json`.

## Sample-coverage-gap

3 van 10 records bestaan niet als top-level `.json` in `data/concepten/records/`:
- `balansschema-volledig` → bestaat als bouwsteen onder `jaarrekening`
- `resultatenrekeningschema` → bestaat als sub-concept onder `jaarrekening` + bouwsteen onder `dubbele-boekhouding`
- `waarderingsregels-jaarrekening` → bestaat verspreid (bouwsteen + speelruimte onder `jaarrekening`; per-balanspost in respectievelijke records)

**Implicatie voor Pass 3**: ofwel het skeleton-document aanvullen met deze records, ofwel bewust de informatie laten als bouwsteen-niveau onder parent-records. Aanbeveling: verifieer of examen-vragen genoeg specifieke aandacht aan een van deze drie geven om eigen record te rechtvaardigen.

## Severity-verdeling (records die wel bestaan)

| Record | Critical | Major | Minor | Verdict |
|---|---|---|---|---|
| boekhouding | 0 | 0 | 5 | OK (publicatie-klaar) |
| jaarrekening | 0 | 2 | 5 | BLOCKING (missing relatie-targets) |
| dubbele-boekhouding | 0 | 0 | 7 | OK (sterke kern) |
| eindejaarsverrichtingen | 0 | 2 | 6 | BLOCKING (missing relatie-targets) |
| voorraden | 0 | 2 | 6 | Te dun (te weinig voorbeelden + geen perspectieven) |
| voorzieningen | 0 | 1 | 8 | Mist contextlagen + perspectieven |
| resultaatverwerking | 0 | 3 | 7 | Te dun — Pass 3 substantieel verbreden |

**Aggregaat severity** (7 records):
- **Critical: 0**
- **Major: 10** (vooral missing cross-relatie-targets + ontbrekende voorbeelden + ontbrekende perspectieven)
- **Minor: 44**
- **Totaal: 54 issues**

## Top 5 voorkomende issues (voor prompt-verfijning)

### 1. Cross-relatie-targets niet-bestaand (4 instanties — major)
Records (jaarrekening, eindejaarsverrichtingen) hebben relaties naar targets die NIET als record bestaan:
- `groottecategorie-vennootschap` (jaarrekening) — wel: `vennootschap-groottecategorieen.json`
- `nationale-bank-van-belgie` (jaarrekening) — niet aanwezig als autoriteit-record
- `uitkering-aan-aandeelhouders` (eindejaarsverrichtingen) — wel: `winstuitkering.json`
- `controle-opdracht` (eindejaarsverrichtingen) — onduidelijk welke alias

**Prompt-verfijning**: cluster-extract.md moet expliciet eisen dat de agent **vóór het schrijven van een relatie** verifieert of het target bestaat via MCP-tool `check_record_bestaat`. Bij niet-bestaan: ofwel gebruiken van bestaande synoniem-id ofwel relatie in scope.out plaatsen met `mag-verwijzen` zonder hard ref.

### 2. Ontbreken `accountant_perspectieven` op balanspost-records (3 instanties — major)
`voorraden`, `voorzieningen`, `resultaatverwerking` hebben geen `accountant_perspectieven`-blok. Dit zijn nochtans concepten waar de accountant concrete rollen vervult (boekhouder bij waardering + auditor bij voorraadtelling + adviseur bij dividend-bestemming).

**Prompt-verfijning**: cluster-extract.md moet voor record-types `balanspost`, `procedure`, `verrichting`, `regime` expliciet eisen: minstens 1 perspectief met minstens 1 rol. Voor `instrument`, `principe`, `kader` mag het optioneel zijn.

### 3. Te weinig `voorbeelden[]` top-level (3 instanties — major)
`voorraden` (1), `voorzieningen` (2 — marginaal), `resultaatverwerking` (0 top-level, alleen in bouwsteen). Cluster-verify-richtlijn ≥2.

**Prompt-verfijning**: harde regel in cluster-extract.md — minstens 2 top-level `voorbeelden[]`-items per record, met verschillende invalshoeken (één eenvoudig + één scenario/complex). Bouwsteen-illustraties tellen niet als top-level voorbeeld.

### 4. Ontbreken `gebruikscontext` en `voorkennis_leespad` op balanspost-records (5 instanties — minor)
`voorraden`, `voorzieningen`, `resultaatverwerking` missen gebruikscontext (voor/voorwaarden/risico/geldigheid) én `voorkennis_leespad`. Kader-records (`boekhouding`, `jaarrekening`, `dubbele-boekhouding`, `eindejaarsverrichtingen`) hebben deze wel.

**Prompt-verfijning**: cluster-extract.md moet voor alle concept_types expliciet eisen: `voorkennis_leespad` (minstens kader + 1 voorvereiste) en `gebruikscontext.geldigheid` (minstens status-veld). Andere `gebruikscontext`-velden mogen sparse blijven.

### 5. MAR/KB bron-ref-onnauwkeurigheid (5 instanties — minor)
- `dubbele-boekhouding`: MAR-klasse 4 tabel mengt actief/passief
- `voorraden`: "KB 29-04-2019 WVV — bijlage MAR" — MAR zit in KB 21-10-2018
- `jaarrekening`: NBB-toeslag-bedragen gemerged met art. 3:10 WVV
- `eindejaarsverrichtingen`: BV-wettelijke-reserve met art. 5:142 (foutieve ref) ipv 5:153
- `boekhouding`: ITAA-norm-naam onvolledig

**Prompt-verfijning**: cluster-extract.md + claims_checken-operatie moet expliciet eisen dat bij elke `geciteerd`-claim de bron-ref **letterlijk** verifieerbaar is. MAR-bronnen ALTIJD uit KB 21-10-2018, waarderingsregels uit KB 29-04-2019. Bij vermenging → split-claims.

### Bonus issue 6 — Type-mismatch concept_type/bouwsteen_type
- `jaarrekening`: subconcept `jaarverslag-bestuursorgaan` als `concept_type: procedure` — eerder `kader`/`instrument`
- `voorraden`: bouwsteen `waardevermindering-voorraad` als `mechanisme` — past, maar verifieer of het niet eerder `regel` is

## Aanbevelingen voor Pass 3 Verbeter

### Hoge prioriteit (BLOCKING)
1. **Fix missing cross-relatie-targets** in jaarrekening + eindejaarsverrichtingen (4 instances) — kan eenvoudig via sed/script + audit_parity
2. **Voeg perspectieven toe** aan voorraden + voorzieningen + resultaatverwerking — minstens 1 perspectief met 1 rol
3. **Voeg voorbeelden toe** aan voorraden (+1) + resultaatverwerking (+2 top-level)

### Middel prioriteit
4. **Voorkennis_leespad** voor alle balanspost-records aanvullen
5. **Gebruikscontext.geldigheid** voor balanspost-records minimaal status-veld
6. **Bron-ref-precisie** — split MAR-bronnen (KB 21-10-2018) van waardering-bronnen (KB 29-04-2019)
7. **Wetreserve-refs** voor BV vs NV unificeren (art. 5:153 vs 7:211)

### Lage prioriteit (cosmetisch)
8. Resultaatverwerking — denkfout-tussenstap in bouwsteen-voorbeeld weghalen
9. Subconcept-types in jaarrekening heroverwegen
10. Cliënt-zijde perspectief toevoegen aan boekhouding (parallel met jaarrekening)
11. Speelruimtes toevoegen waar relevante keuzes bestaan (vereenvoudigd-vs-dubbele, actualisatie LT-voorziening, dividend-bestemming)

### Sample-uitbreiding
12. **Besliscriterium voor 3 niet-bestaande records** (balansschema-volledig, resultatenrekeningschema, waarderingsregels-jaarrekening): eigen record of bouwsteen? Examenvragen-analyse aanbevolen.

## Prompt-verfijning samenvatting (voor cluster-extract.md)

Voorstel deltas aan cluster-extract.md prompt:

1. **Sectie "Cross-relatie-discipline"**: verplicht `check_record_bestaat` MCP-call voor élk relatie-target voor commit. Bij missing → ofwel scope.out met richting `mag-verwijzen` zonder ref ofwel synoniem-id gebruiken.
2. **Sectie "Voorbeelden quota"**: minstens 2 top-level `voorbeelden[]`-items per record (NIET in bouwstenen). Geen "voorbeeld in bouwsteen telt als top-level".
3. **Sectie "Accountant_perspectieven verplichting per concept_type"**: matrix definiëren. `balanspost`/`procedure`/`verrichting`/`regime` = verplicht ≥1 perspectief; andere = optioneel.
4. **Sectie "Bron-ref-precisie"**: MAR vs waarderingsregels vs WVV expliciet splitsen — checklist met top-bronnen per discipline.
5. **Sectie "Voorkennis_leespad minimaal"**: kader + 1 voorvereiste verplicht.

## Conclusie

Sample-kwaliteit is in algemene zin **hoog** voor kader-records (`boekhouding`, `jaarrekening`, `dubbele-boekhouding`, `eindejaarsverrichtingen`) — rijke 3-laag kernen + meerdere voorbeelden + bouwstenen + valkuilen + perspectieven. Balanspost-records (`voorraden`, `voorzieningen`) en de `resultaatverwerking`-procedure zijn **dunner** — minder voorbeelden, geen perspectieven, ontbrekende gebruikscontext. Dit suggereert dat de cluster-extract-prompt **type-gediffentieerde verwachtingen** mist: zware kader-records krijgen automatisch meer dekking, lichtere balanspost-records glijden uit.

**Belangrijkste actie voor Pass 3**: fix cross-relatie-targets (BLOCKING) + voeg perspectieven en voorbeelden toe aan balanspost-records.
