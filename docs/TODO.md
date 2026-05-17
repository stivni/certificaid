# TODO — Certificaid roadmap

_Centrale inhoudsopgave van openstaand werk, geordend per afhankelijkheid._
_Voor de gedetailleerde issues: zie de gelinkte bronbestanden — dit document
houdt het overzicht, geen content-duplicatie._

**Laatste update**: 2026-05-17 (na refresh-gate + CBN-fix)

## Logica van de volgorde

Elke laag bouwt op de vorige. Wat we niet eerst stabiliseren, slepen we als
zwakte mee in de bovenliggende lagen:

```
1. Bronnen-laag    →  2. Records-laag    →  3. Render-template  →  4. PO-rollout
   (C1, C2)           (E1, A1-A4)            (D1)                   (B1, B2, B3)
```

Daarna polish (5) en continu onderhoud (6).

---

## Fase 1 — Bronnen-laag compleet maken

Blokkeert PO-rollout voor fiscaliteit (2.x) en deontologie (4.0). PO 3.0
(vennootschapsrecht) zou ook al kunnen — daar is geen bronnen-blokkade — maar
de records-fundering (Fase 2) profiteert ook deze PO. Dus: eerst basis stabiel.

### 1.1 — Wet-beroepskwalificaties-2008 — ETL-fix
- Issue: `Art. N_WAALS_GEWEST`-varianten splitsen één artikel in twee secties.
- Fix: extractor aanpassen om regio-varianten correct te merge'n.
- Trigger voor: PO 4.0 (deontologie).

### 1.2 — 8 fiscale gidsen — ETL-fixes (needs-rework)
Narratieve type-3 PDFs, ETL-uitdagingen (TOC-residu, single-word-splitsing,
ontbrekende heading-injectie, max-sectie-overschrijding). Per-bron rationale in `provenance.trust.rationale`.

- `Almanak-BTW-2026.md`, `Almanak-VenB-2026.md`, `Belastingalmanak-2026.md`
- `Cijfers-Tarieven-2026.md`
- `belastinggids-aclvb-2025.md`, `fiscaal-memento-2025.md`
- `toelichting-PB-2025-deel1-VG.md`, `toelichting-PB-2025-deel2.md`, `toelichting-VenB-2025.md`

Trigger voor: PO 2.1-2.8 (fiscaliteit, 8 PO's).

### 1.3 — Refresh-gate na elke trust-promotie
Reflex die nu vastligt: `python3 -m tools.etl.refresh_rag_and_matches` na elke
mutatie. Niet vergeten na 1.1 en 1.2.

---

## Fase 2 — Records-laag stabiel maken (focus PO 1.x)

PO 1.5-1.9 records hebben gaten op primaire-bron-grondslag. Competenties +
leerpaden + minicursussen erven die zwakte. Eerst herstellen vóór we PO's
toevoegen die er via cross-PO concepten op steunen.

### 2.1 — Bestaande gaps verwerken (gaps.json afwerking)
142 open issues (snapshot 2026-05-17):
- 33× `edges.target-ontbreekt` (wikilink-doelen)
- 29× `concept-gap` (records die ontbreken)
- 20× `in_praktijk.ontbreekt`
- 9× `records.overlappend-fenomeen`
- 9× `stappen.onvolledig`
- 8× `records.ontbreekt`
- 6× `vergelijkingsparen.ontbreekt` / `vergelijkingsparen.target-ontbreekt`
- 5× `bron-gap`
- 3× `valkuilen.ontbreekt`

Verwerken via gestandaardiseerde ENRICH-cyclus (Opus-subagent, monotoon
contract, append-only). Verbetert per-record kwaliteit én lost edges-graph op.

### 2.2 — PO 1.5 fabricated chunk-ids fixen (4 records)
Subagent uit PO 1.5-doorloop verzon chunk-ids met `<filename>__sec_<sectie>`-
patroon zonder validatie. 3 daarvan bestaan niet in chromaDB. Records die dit bevatten:
- `bijzondere-waardevermindering-ias-36.json`
- `ias-1-balans-presentatie.json`
- `ifrs-16-lessee-vs-lessor-overzicht.json`
- `leasing-ifrs.json`

Fix: vervangen door echte chunk-ids tijdens 2.3 EXPAND-pass.

### 2.3 — Records-strategie kiezen voor PO 1.5 + 1.6
Drie opties (zie chat 2026-05-17 voor onderbouwing):
- **EXPAND-only**: bestaande records behouden, alleen primaire-bron-refs toevoegen via ENRICH-pass. ~3-5 uur Opus.
- **EXPAND + selectief overdoen**: records met `bron_gap` of fabricated chunk-ids opnieuw extracten. ~5-8 uur.
- **Volledig herextract PO 1.5+1.6**: hoogste kwaliteit, ~8-12 uur.

Diagnose-input: `data/extractie/delta-rapport.md` — 251 HIGH + 93 MED records met echte stale-impact.

**Beslissing wacht op**: gebruiker.

### 2.4 — Examenvragen-classificatie PO 1.5-1.9
Check A van VERIFY werd geskipt voor deze PO's omdat
`data/programma/examen_vragen/_programmaonderdeel_classificatie.json` deze PO's
niet dekt. Classificatie-subagent draaien om examenvragen te koppelen aan
PO-anchors. Maakt `> [!question]-` callouts mogelijk in minicursussen.

### 2.5 — Cross-PO dedup 1.x
Bekende overlaps:
- `getrouw-beeld` × `getrouw-beeld-jaarrekening` (1.1 ↔ 1.3)
- `jaarverslag` × `bestuursverslag` (1.2 ↔ 1.3)
- 3-way `rechten-verplichtingen-buiten-balans` / `klasse-0-niet-in-balans` / `niet-in-balans-opgenomen-rechten-verplichtingen`
- Vermoedelijk meer in 1.5-1.7-overlap zone.

---

## Fase 3 — Render-template upgrade

Eenmalige template-aanpassing, propageert naar elke minicursus bij her-render.
Beter dit doen vóór massale PO-rollout zodat alle nieuwe PO's de scherpere
binding direct meekrijgen.

### 3.1 — Minicursus: taken+doelstellingen-binding
Spawned-task chip (2026-05-17): meer expliciete koppeling van minicursus-secties
aan `programma.json` taken/doelstellingen voor scherpere studie-focus.

Concreet:
- Header-blok "Wat train je hier?" met taken + doelstellingen bullets
- Per hoofdstuk een chip "→ taak 1.4.T.2, doelstelling 1.4.D.3"
- Zelftoets-blok aan het eind per taak

Status: chip beschikbaar in UI om aparte sessie te starten.

---

## Fase 4 — PO-rollout (10 PO's nog)

Pas hier starten als Fase 1+2+3 stabiel zijn. Per PO: standaardproces uit
`docs/po-1.1-doorloop-prep.md`. Refresh-gate respecteren tussen PO's.

### 4.1 — PO 3.0 — Vennootschapsrecht
- Primaire bronnen al trusted (WVV + KB-WVV-2019).
- Niet blocked door Fase 1.
- Lichte stale-risico (geen IFRS/ISA-relevant).

### 4.2 — PO 4.0 — Deontologie
- **Vereist Fase 1.1** (Wet-beroepskwalificaties) eerst.
- Primaire bronnen: IESBA-code + ITAA-normen (deels trusted).

### 4.3 — PO 2.1 t/m 2.8 — Fiscaliteit (8 PO's)
- **Vereist Fase 1.2** (8 fiscale gidsen) eerst.
- Volgorde binnen 2.x: nog te bepalen (vermoedelijk 2.1 startpunt: directe belastingen NP).

---

## Fase 5 — Polish (nice-to-have)

### 5.1 — NotebookLM-export: PO splitsen in podcast-eenheden
Spawned-task chip (2026-05-17): grote PO's opdelen in ~10-15 min content-blokken
voor 20-25 min podcasts.

### 5.2 — Tutor-app reactivatie
`tutor/app.py` bestaat (Streamlit). Was ooit overwogen als interactieve
interface. Dormant.

---

## Continu — Onderhoud op de achtergrond

### 6.1 — ADR-017 bronnen-migratie (12/116 done)
Eenvormig extract-schema. Backlog: 104 bronnen.

### 6.2 — Backup-tags archeology (8 tags)
Bij twijfel over verloren werk in cleanup-cyclus: `git checkout <tag>` om
historische state te bekijken. Tags:
- `backup/etl-tdd-fixes-2026-05-16-pre-cleanup`
- `backup/experiment-bron-first-extractie-pre-cleanup`
- `backup/hardcore-euclid-06385d-pre-cleanup`
- `backup/isa-transformers-2026-05-17-pre-cleanup`
- `backup/jovial-kirch-c0dc7f-pre-cleanup`
- `backup/optimistic-fermat-af2960-pre-cleanup`
- `backup/stoic-panini-65e9ae-pre-cleanup`
- `backup/worktree-agent-adb888276d8792083-pre-cleanup`

Bij geen issue gedurende 30 dagen: tags verwijderbaar.

### 6.3 — Open punten in ADRs
Verspreid over 10 ADRs in `docs/adr/`. Bekijken per ADR via `## Open punten`-secties. Voorbeelden:
- ADR-008 §13.2: content-pattern-based VERIFY-checks (i.p.v. schema-veld-gebonden)
- ADR-005 §refresh-gate (NIEUW): wachten op cross-PO impact in praktijk

---

## Achtergrondinfo

- **Memory-snapshots**: `memory/project_*.md` houdt per-onderwerp status (project_status, project_bronnen_competenties, project_examenpatronen, project_conceptmodel). Update na grote mijlpalen.
- **Architectuur-fasering**: `docs/roadmap.md` toont Fase 0-5 indeling van het project zelf (architectuur-evolutie, niet werk-fasen zoals deze TODO).

## Onderhoud van deze TODO

- **Nieuwe taak**: voeg toe aan correcte fase op basis van afhankelijkheid.
- **Taak afgerond**: streep door + commit, of verwijder bij definitief klaar.
- **Bij grote sessie-shifts**: actualiseer "laatste update" datum.
- **Diepere details**: link naar `gaps.json` / `delta-rapport.md` / ADRs — niet inhoud kopiëren.
