# Prep-doc: PO 1.1-doorloop (en alle volgende PO's)

**Datum**: 2026-05-16
**Status**: Draft — wacht op review + design-sessie (P1+P4)
**Context**: PO 1.4 is af (Sessies 3+4+5 + 12 template-bugs + 5 regression-tests + ADR-010 §template-discipline). Dit document plant de doorloop voor PO 1.1 (Algemene boekhouding, 29 anchors) — en is herbruikbaar voor PO 1.2, 1.3, etc.

---

## 1. Staat van PO 1.1 vs PO 1.4

| | PO 1.4 (klaar) | PO 1.1 (nu) |
|---|---|---|
| Anchors | 13 | **29** (al in `anchors.json`) |
| Concept-records | 32 | 0 |
| Competentie-yamls | 9 | 0 |
| Leerpad | ja | nee |
| Examenvragen-classificatie | 5 vragen | 0 |
| Concept-fiches gerenderd | 32 | 0 |
| Bronnen | n.v.t. | resources/bronnen/ heeft normen + adviezen + wetteksten — **scope-check nodig** |

## 2. Eenmalig versus per-PO

**Eenmalig (al klaar — niets meer voor PO 1.1):**
- Schema 1.4 + alle Jinja2-templates + render-scripts
- ADRs (007/008/010) + 56 regression-tests + render-discipline
- Cast-yaml infrastructuur + balans/RR-templates
- Pipeline-scripts (`build_anchors`, `match_bronnen`, `enrich_records`, `propose_competenties`, `propose_leerpad`, render-scripts)

**Per-PO te doorlopen (Stap 1–14 hieronder):**

| Stap | Wat | Tooling | Tijd |
|---|---|---|---|
| 1 | Cast uitbreiden met PO-specifieke namen + scenario's | Mens edit `casts/globaal.yaml` | ~30 min |
| 2 | Anchor-verrijking | `build_anchors.py --programmaonderdeel 1.1` | ~5 min |
| 3 | Anchor-embeddings | `embed_anchors.py --programmaonderdeel 1.1` | ~5 min |
| 4 | Bron-first matching | `match_bronnen.py --programmaonderdeel 1.1` | ~5 min |
| 5 | Concept-extractie (Opus subagent met prompt v5) | Opus, per anchor of per cluster | ~2u |
| 6 | VERIFY-pass (Opus subagent) | `prompts/concept-verify-v1.md` | ~30 min |
| 7 | ENRICH-pass + auto-merge | `enrich_records.py` + `auto_merge.py` | ~30 min |
| 8 | Examenvragen-classificatie | Opus subagent → `_programmaonderdeel_classificatie.json` | ~30 min |
| 9 | Competentie-destillatie (Fase D) | `propose_competenties.py` → Opus subagent | ~45 min |
| 10 | Mens-curatie competenties (voorgesteld → gecureerd) | Mens, ~5 min per yaml | ~30 min |
| 11 | Leerpad-voorstel (Fase E) | `propose_leerpad.py` → Opus subagent | ~20 min |
| 12 | Render alle fiches + skeleton minicursus | `render_*` scripts | ~5 min |
| 13 | Minicursus-glue (~20 TODOs) | Opus subagent met `prompts/minicursus-glue-v1.md` | ~10 min |
| 14 | Quality-pass + targeted fixes à la Sessie 3+5 | Mens visuele inspectie + Opus | ~30 min |

**Totaal**: 5–8 uur, waarvan ~80 % autonoom Opus-werk.

---

## 3. Vier beslissingen (genomen 2026-05-16)

1. **Cast-strategie**: nieuwe namen voor boekhoudingscontext. Aurelia/Brugse/Antwerpse blijven gereserveerd voor consolidatie. Nieuwe namen kiezen bij Stap 1 — kandidaten: Bakkerij Bert (kleine BV handel), Garage Marc (BV diensten), Schilderbedrijf Sofie (eenmanszaak), VZW De Pluim (vzw), etc.

2. **Bronnen-strategie**: bronnen zijn niet rigide PO-gelinkt, maar voor de evidente gaten (CBN-adviezen rond boekhouding-specifiek, KB Boekhouding) doen we een lichte gap-scan vóór Stap 5.

3. **Doorloop**: heel PO 1.1 in één rush (Stap 1–14), feedback-iteratie pas daarna.

4. **Cross-PO concepten**: laten van granulariteit afhangen — extractor doet zijn werk, maar markeert **thema's**. Cross-PO synthese-records aggregeren waar nodig. Plus: **sector-labels** voor concepten die alleen voor bepaalde vennootschapsvormen relevant zijn.

---

## 4. Schema-uitbreiding 1.5 (voorstel — vereist design-sessie P1)

Drie nieuwe top-level-velden op concept-records:

```json
{
  "themas": ["afschrijving", "voorzieningen", "intrest-berekening"],
  "sectoren": ["kleine-vennootschap", "vzw", "eenmanszaak"],
  "synthese_clusters": ["afschrijvingen-overzicht"]
}
```

**Semantiek**:
- `themas[]`: vrije-tekst thematische labels, cross-PO traceerbaar
- `sectoren[]`: gestructureerde lijst (gecontroleerd vocabulaire — kleine-vennootschap, vzw, eenmanszaak, NV, BV-groot, holding, etc.) — leeg = geldt voor alle
- `synthese_clusters[]`: id's van synthese-records die dit concept aggregeren

**Render-impact**:
- Frontmatter-tags krijgen `thema-X` chips (Quartz-filterbaar)
- Sector-label rendert als badge bovenaan fiche (`⚠️ Alleen voor VZW`)
- Synthese-cluster-records aggregeren cross-PO thema's met vergelijkings­tabel + Mermaid (zoals `consolidatiemethodes-vergelijking` doet binnen PO 1.4)

---

## 5. Voorbereidings-bundel (P1–P6) — vóór PO 1.1 start

| Prep-stap | Wat | Wie | Volgorde |
|---|---|---|---|
| **P1** | Schema 1.5 ADR draften (themas + sectoren + synthese-cluster + sector-vocabulaire) | Opus design-sessie | Eerst |
| **P2** | Cast-uitbreiding `globaal.yaml` met boekhouding-scenario's + nieuwe namen + plausibele ranges (kosten € 100–€ 50.000; voorraden € 5.000–€ 500.000; loonkost € 30.000-€ 80.000/wpf) | Mens (~30 min) | Parallel met P1 |
| **P3** | Bronnen-gap-scan: welke bronnen heb je nodig voor de 29 anchors van PO 1.1 die nog ontbreken in `resources/bronnen/` | Auto-scan + mens-review (~30 min) | Parallel |
| **P4** | Concept-extractie-prompt v5 (themas + sectoren + scope-instructies + cast-verwijzing naar nieuwe boekhouding-cast) | Opus design-sessie (in lijn met P1) | Na P1 |
| **P5** | Render-templates uitbreiden: thema-chips in frontmatter + sector-badge boven fiche-titel | Opus uitvoering (~30 min) | Na P1+P4 |
| **P6** | `validate_concept.py` + regression-tests voor schema 1.5 | Opus uitvoering | Na P5 |

---

## 6. Sequencing van hier tot PO 1.1 in productie

1. **Nu (deze sessie)**: doc komt klaar; autonomous loop blijft draaien voor laatste sweep van PO 1.4
2. **Reviewen**: jij bekijkt minicursus 1.4 lokaal (`npm run dev`); eventuele Sessie 6 voor 1.4-records-fixes als nodig
3. **Design-sessie (Opus, ~1-2u)**: P1+P4 — schema 1.5 ADR + extractie-prompt v5
4. **Uitvoering-sessie (semi-autonoom, ~2u)**: P2 (cast) + P3 (bronnen-scan) + P5 (template) + P6 (validator + tests). Kan grotendeels parallel
5. **PO 1.1 doorloop** (~5-8u, grotendeels autonoom): Stap 1–14

---

## 7. Risico's + open punten

- **Schaal**: PO 1.1 heeft 29 anchors versus 13 voor 1.4. Verwacht ~50–70 concept-records (grofweg 2× zoveel als 1.4). Opus-context-window kan een limiet zijn — eventueel per-cluster batchen.
- **Cross-PO botsingen**: schema 1.5 `themas[]`-veld lost dit op, maar VERIFY-aspect `records.overlappend-fenomeen` moet aangepast om thema-overlap niet automatisch als duplicaat te flaggen.
- **Sector-vocabulaire**: must-have lijst opstellen in P1. Voorstel: `[kleine-vennootschap, microvennootschap, grote-vennootschap, beursgenoteerd, NV, BV, CV, VOF, maatschap, eenmanszaak, VZW, stichting, holding]`. Concrete keuze in design-sessie.
- **Boekhouding-bronnen**: CBN-adviezen 2010-2025 die op boekhouding-techniek slaan moeten geïnventariseerd. Eventueel deel-batch in `tools/download/`.
- **Minicursus-glue per PO**: nu een Opus-subagent-aanroep per PO. Voor 18 PO's = 18 glue-passes. Kan in een orchestrator als de pipeline stabiel is.
- **Re-render-discipline**: render_minicursus.py heeft `--forceer` glue-protectie (commit `ad27aa74`); zelfde discipline mogelijk nodig voor concept-fiches als die later handmatig nageschoven worden.

---

## 8. Checklist voor start PO 1.1

```
Pre-flight:
[ ] Minicursus 1.4 visueel gevalideerd in Quartz (npm run dev)
[ ] Eventuele Sessie 6 fixes op PO 1.4 gecommit
[ ] Schema 1.5 ADR (P1) gecommit
[ ] Extractie-prompt v5 (P4) gecommit
[ ] Cast-yaml uitgebreid met boekhouding-scenario's (P2) gecommit
[ ] Bronnen-gap-scan uitgevoerd; eventuele evidente gaten opgevuld (P3)
[ ] Render-templates ondersteunen thema-chips + sector-badge (P5) gecommit
[ ] validate_concept.py + tests groen voor schema 1.5 (P6) gecommit

PO 1.1 doorloop start:
[ ] Stap 1: cast-namen specifiek voor PO 1.1 toegevoegd
[ ] Stap 2-4: anchors verrijkt, geëmbed, gematcht (deterministisch)
[ ] Stap 5: concept-extractie (Opus, ~50-70 records verwacht)
[ ] Stap 6-7: VERIFY + ENRICH + auto-merge tot 0 hoge-prio gaps
[ ] Stap 8: examenvragen-classificatie voor 1.1
[ ] Stap 9-11: competenties + curatie + leerpad
[ ] Stap 12-13: render + minicursus-glue
[ ] Stap 14: quality-pass + targeted fixes
[ ] Quartz build + commit-batch
```

---

## 9. Herbruikbaarheid voor PO 1.2, 1.3, 2.x, ...

Dit doc is geschreven voor PO 1.1 maar 90 % is herbruikbaar voor elk volgend PO:
- Stap 1 (cast) verschilt per onderwerp (audit, fiscaliteit, etc. krijgen eigen casts)
- Stap 2–4 zijn deterministisch en identiek
- Stap 5–13 zijn identiek qua tooling — alleen de inhoud verschilt
- P1–P6 zijn éénmalig: schema 1.5 + prompt v5 + templates gelden voor alle PO's na 1.1

Per nieuw PO: ~5-8u doorloop, mits de pre-flight (P1–P6) eenmaal gedaan is.

Na PO 1.1: een **doorloop-script** maken dat Stap 2–4 + Stap 12 als one-shot draait per PO. Stappen 5–11 blijven Opus-subagent territoire (manual orkestratie).
