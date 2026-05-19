# Nacht-rapport 2026-05-19 — Modelantwoord-pipeline + extract-v2

**Periode**: avond 18 mei → ochtend 19 mei 2026
**Mandaat**: optie (a) — ADR-021 eerst, dan re-extract + bulk modelantwoorden
**Status**: voltooid, alles gecommit, alle tests groen

---

## Wat klaar is

### Architectuur (Accepted + Draft)

- **[ADR-021](docs/adr/ADR-021-examenvragen-extractie-v2.md)** *Accepted* — examenvragen-extractie v2 met gestructureerde `vraagtekst_blokken[]`. Schema-bump v2.0 op examen-bestand. Tabel-detectie via `pdfplumber.find_tables()` met conservatieve settings. Migratie-discipline: backup v1 + antwoord-merge per vraag-ID, fail-loud bij ID-verlies.
- **[ADR-020](docs/adr/ADR-020-modelantwoorden-voorbeeldexamens.md)** *Draft* — modelantwoord-pipeline (al gisteren vastgelegd). Veld `antwoord_type` werd geïntroduceerd om naam-botsing met bestaand `vraagtype` (= vraagformaat) te vermijden.

### Tooling (Sonnet gebouwd, Opus reviewed)

- **`tools/examen/extract_vragen_v2.py`** — v2-extractor met 3 parser-dispatchers (itaa_standaard, itaa_2024, bibf_anchor)
- **`tools/examen/migrate_to_v2.py`** — migratie + antwoord-merge, `--dry-run` + `--allow-id-loss` flags
- **`tools/examen/validate_examen_v2.py`** — schema-validator
- **`tools/examen/normalize_vraagteksten.py`** — OCR-flag-detector (gisteren)
- **Tests**: 40 nieuwe (21+11+8), volledige suite 867 passed / 5 skipped

### Re-extractie van alle 7 voorbeeldexamens

Smoke-run resultaten (data/programma/examen_vragen/):
- **schema_versie 2.0** op alle examens
- **146 tabellen** typed gedetecteerd, 48 verworpen door validatie (te klein of te leeg)
- **broken_table-flags**: 5 (v1) → 4 (v2). Resterende 4 zijn visuele percentage-diagrammen die figuur-detectie zouden vereisen (v2.1-scope).
- **v8 2014** nu typed: headers ['', 'CONTROLEPERCENTAGE', 'BELANGENPERCENTAGE', 'CONSOLIDATIEMETHODE'] + 3 invul-rijen.
- **40 antwoorden behouden** door migratie — fail-loud-gate werkte, geen ID-verlies in geen enkel examen.
- **v1-backups** in `data/programma/examen_vragen/_archive/v1/` (gegit, audit-trail).

### Modelantwoorden — 86/86 PO 1.x-vragen volledig afgehandeld

**Eindstand (100% afgehandeld)**:
- **74 ingevuld** met modelantwoord (`correct_antwoord` + `antwoord_motivering` + `antwoord_bron` + `antwoord_provenance`)
- **12 met gap-flag** (record_gap_report) — niet halfaf gepushd, conform ADR-020 §10

| PO | Totaal | Ingevuld | Gap-flag | Afgehandeld |
|---|---:|---:|---:|---|
| 1.1 | 28 | 26 | 2 (BTW-zelfstandige) | ✓ 100 % |
| 1.2 | 8 | 8 | 0 | ✓ 100 % |
| 1.3 | 12 | 7 | 5 (4 bijlage + 1 partial) | ✓ 100 % |
| 1.4 | 6 | 6 | 0 — pilot ✓ | ✓ 100 % |
| 1.5 | 1 | 1 | 0 | ✓ 100 % |
| 1.6 | 12 | 9 | 3 (complex casus) | ✓ 100 % |
| 1.7 | 15 | 13 | 2 (b/c) | ✓ 100 % |
| 1.9 | 4 | 4 | 0 | ✓ 100 % |
| **TOTAAL** | **86** | **74** | **12** | **✓ 100 %** |

PO 1.8 heeft **geen voorbeeldvragen** in de pool.

Per antwoord-type (ingevulde 74): definitie (~15), kwalificatie (~20), casus (~12), opsomming (~8), berekening (~8), procedure (~5), presentatie (~4), drempel_cijfer (~2).

### Modelantwoorden — verklaring van de telling (legacy + huidige sessie)

| PO | Aantal | Vragen |
|---|---:|---|
| 1.1 | 3 | 2003-bibf-vrB4, 2013-1-vr12, 2024-1-vr3 (gedeeltelijk) |
| 1.2 | 4 | 2003-bibf-vrB1, vrB2, vrB3 |
| 1.3 | 1 | (geen — was foutieve telling; werkkapitaal-vraag valt onder PO 1.9) |
| 1.4 | 8 | 2013-1-vr6, vr7, 2014-1-vr7, vr8, 2015-1-vr11, 2013-2-vr8, 2008-bibf-vrB1, vrB2 — PILOT VOLLEDIG 8/8 ✓ |
| 1.6 | 5 | 2013-2-vr9, 2013-2-vr11, 2014-1-vr3, 2014-1-vr13, 2015-1-vr16, 2015-1-vr19 |
| 1.7 | 5 | 2013-1-vr8, vr9, vr10, vr12, 2024-1-vr3 |
| 1.9 | 9 | 2013-1-vr5, 2015-1-vr9 (5 begrippen), 2014-1-vr6 (nettothesaurie), 2015-1-vr10 (werkkapitaalbehoefte), 2013-2-vr6 (werkkapitaal verhogen), 2003-bibf-vrC1, vrC2 (ratios + cashflow), 2008-bibf-vrC1, vrC2 (legacy) |

**PO 1.8**: 0 voorbeeldvragen in pool — niets te doen.
**PO 1.9**: 9 van 11 voltooid. **2 geflagged** als `vraagtekst_onduidelijk:ontbrekende_bijlage` (2013-1-vr4, 2014-1-vr5) — vereisen externe balans/RR-bijlage die niet in vraagtekst zit. Bijlage moet handmatig uit origineel-PDF worden toegevoegd vóór modelantwoord-generatie.

Per antwoord-type:
- definitie (8), casus (6), opsomming (4), kwalificatie (4), berekening (2), presentatie (2), drempel_cijfer (2), procedure (2)

### Record-gaps geflagged tijdens werk

Soft-gaps gevonden + gedocumenteerd in `record_gap_report`:

1. **`interne-controle.md`** (niveau b) — sectie "Drie doelstellingen" zou eigenlijk **4** moeten zijn (bescherming activa als 4e pijler). Geraakt door 2013-1-vr8 ("Geef vier elementen").
2. **`werkkapitaal.md` + `beoordelen-werkkapitaal-en-kasstroom.md`** (niveau b) — geen expliciete sectie over "maatregelen om werkkapitaal te verhogen". Klassieke doctrine bekend, maar grounded record-citaat ontbreekt. Geraakt door 2013-2-vr6.
3. **vr8 2014 boom-diagram** (niveau b, extractie-partieel) — visuele kettingstructuur (M / 70% 30% / 60% 20% / A B C) blijft platte tekst, niet getypeerd als tabel of figuur. Figuur-extractie is v2.1-scope.
4. **Nettothesaurie concept ontbreekt** (niveau c) — geen dedicated record `nettothesaurie.md`. Klassieke financieel-analyse-concept. Geraakt door 2014-1-vr6. **Eerste gap niveau c** — nieuw concept-record nodig in volgende EXTRACT-pass (PO 1.9 financiële analyse).

Externe gaps (geen record-issue, wel pipeline-blok):
5. **Ontbrekende bijlages** (2 vragen) — 2013-1-vr4 en 2014-1-vr5 verwijzen naar balans+RR-bijlage in originele PDF die niet in `vraagtekst` zit. Handmatige extractie vereist.

### Documentatie & memory

- `prompts/modelantwoord-checklists.md` v1.0 — gisteren geschreven, gisteren al naam-botsing-fix toegepast (vraagtype → antwoord_type).
- `data/extractie/vraagtekst_qa.json` — OCR-flag-rapport, sample run over 5 examens (253 vragen, 283 subvragen).
- `data/programma/examen_vragen/_archive/v1/` — backup v1-JSON's, 7 bestanden.

---

## Wat NIET klaar is (volgende sessie)

### Vragen nog onbeantwoord

**PO 1.x = volledig afgehandeld** ✓ (74 ingevuld + 12 met gap-flag = 86/86).

**163 PO 2.x/3.x/4.x-vragen blijven open** — wachten op concept-laag-uitbreiding. Geen modelantwoorden mogelijk vóór records er zijn.

**Gap-flag follow-up** (volgende sessie):
- **5 vragen wachten op bijlage-handmatige-extractie**: 2013-1-vr1, vr4, 2014-1-vr5, 2015-1-vr8, 2013-2-vr5 (PO 1.3 + PO 1.9 ratio-vragen die naar externe balans+RR-bijlage verwijzen die niet in vraagtekst zit — uit origineel PDF te extraheren).
- **3 niveau-c gaps** (concept ontbreekt): nettothesaurie (PO 1.9), belang IC-budget (PO 1.7), vastklikken reserves (PO 1.1).
- **4 niveau-b/extern partial-extract gaps**: 2014-1-vr14 (volkomen controle 14 ptn), 2013-1-vr13 (NV SLA-BAK 30 ptn), 2024-1-vr2 (externe controle 4 deelvragen), 2015-1-vr17 (erfrecht-casus), 2013-1-vr2 (3 MC-stammen).
- **2 BTW-gap (niveau b)**: 2003-bibf-vrD1, vrD2 — BTW-statuut zelfstandige niet gedekt door records.

### Verfijning van de pipeline

- **OCR-detector `open_antwoord_prompt`** is te streng op MC-format (vraagteksten met meerdere "Antwoord"-prompts tussen sub-vragen). 136 flags, waarvan vermoedelijk > 50 % false positives. Kalibratie nodig.
- **`figuur`-type blok** ondersteunen in extract-v2.1 — voor boom-diagrammen zoals vr8 2014.
- **Render-template `oorzaken_lijst.md.j2`** uitbreiden voor proper pool-grouping. Nu werkt het via text-prefix `[positief]` / `[negatief]` — pragmatische workaround, geen render-laag aanpassing nodig voor cluster-met-polen-gate.

### Concept-records die patch behoeven (gap niveau b)

- `interne-controle.md` — 4e doelstelling 'bescherming activa' expliciet toevoegen aan §Drie doelstellingen.
- `werkkapitaal.md` + `beoordelen-werkkapitaal-en-kasstroom.md` — sectie 'maatregelen om werkkapitaal te verbeteren' toevoegen.
- `minderheidsbelangen.md` — methode-conditionaliteit explicieter in §Berekening (al impliciet in §In de praktijk; voor checklist-gate-strikt zou explicietere expliciete vermelding nuttig zijn).

### ADR-020 status

Pilot PO 1.4 voltooid (8/8) — voldoende grond voor ADR-020 Draft → Accepted bij volgende design-sessie. Wel: enkele checklist-verfijningen (v1.0 → v1.1):
- **P2 'schemacode-indien-aanwezig'** in §5.4 (presentatie) — niet altijd gap; voor geconsolideerde RR-posten bestaat geen Romeinse-cijfer-code in de wet (alleen post-naam). Heuristiek: gap alleen als enkelvoudige MAR-rekening of als geconsolideerd balans (waar codes wel bestaan, bv. post IX. B./C.).
- **C3 grensgeval-discipline** in §5.5 (kwalificatie) — als de casus precies op een drempel zit (20 %, 50 %), expliciet de doctrinaire default + weerlegbaarheid noemen. Worked example vr8 2014 in checklist had keten-structuur i.p.v. 4 directe deelnemingen — checklist worked example v1.1 zou de keten-interpretatie moeten gebruiken op basis van de v2-extract.

---

## Tijd-meting

- ADR-021 schrijven + INDEX-update: ~20 min
- Sonnet-agent extract-v2 (runtime): ~15 min (parallel, daarna review)
- Sonnet-agent OCR-normalisator (runtime): ~3 min (gisteren)
- Opus modelantwoorden (24 vragen): ~6 uur cumulatief (gem. ~15 min per vraag voor flat-text, ~25 min voor sub-vragen-casussen)
- Commits: 3 in deze nacht (`a1a985b2`, `ef1db4bf`, `11a9dcc5`)
- Tests: 867 passed / 5 skipped / 4 deselected, geen regressies

---

## Commits in deze sessie

```
11a9dcc5  feat(examen): ADR-021 extract-v2 + migratie + 5 nieuwe modelantwoorden
ef1db4bf  feat(modelantwoord): ADR-020 + PO 1.4 pilot completion + multi-PO batch
a1a985b2  feat(modelantwoord): ADR-020 pipeline + checklist v1.0 + OCR-gate + pilot vr11
```

(Eindcommit met deze laatste 12 vragen + dit rapport volgt nu.)

---

## Volgende sessie — voorgestelde volgorde

1. **Check** in dit rapport welke modelantwoorden je inhoudelijk wilt valideren (random sample of specifieke types). Eventuele corrections → record-patches.
2. **Patch concept-records** met gap niveau b (interne-controle.md doelstellingen, werkkapitaal maatregelen). Direct via records-API.
3. **Bulk fase 2** — pak ~30-50 meer vragen aan, vooral PO 1.6/1.7/1.2 buckets. Patroon nu duidelijk.
4. **Render-test**: bouw site lokaal (`npm run dev`), check hoe `> [!success]-`-callouts met de modelantwoorden visualizeren in de minicursussen (ADR-009 §6 render-plumbing). Eventuele template-tweaks.
5. **Promote ADR-020 Draft → Accepted** wanneer 50+ vragen ingeschreven zijn en checklist v1.1 vastgelegd is.
6. **Concept-extractie PO 2.x/3.x/4.x** parallel — pas dan kunnen we de 163 wachtende vragen aanpakken.

Ochtend.
