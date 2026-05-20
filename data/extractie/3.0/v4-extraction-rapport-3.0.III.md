# EXTRACT v4 — PO 3.0.III "De algemene vergadering"

**Run**: `concept-extractie-v4-2026-05-20T09:00:00Z`
**Anchor**: `3.0.III`
**Model**: claude-opus-4-7
**Schema**: 1.6

## Telling

| Kategorie | Aantal |
|---|---|
| Nieuwe records | 15 |
| Waarvan synthese | 3 |
| Bijgewerkte records | 0 |
| Hernoemde records | 0 |
| Verwijderde records | 0 |
| Audit-status na save | OK (574 disk = 574 RAG) |
| Gaps toegevoegd | 7 |

## Nieuwe records

### Algemene cluster (1)
1. `algemene-vergadering` (cluster) — algemene definitie, bouwstenen-structuur, voorbehouden bevoegdheden vs. residuair bestuur

### Soorten algemene vergadering (3)
2. `gewone-algemene-vergadering` (cluster) — jaarvergadering, jaarrekening + kwijting, uitstel-recht
3. `bijzondere-algemene-vergadering` (begrip) — ad hoc tussen jaarvergaderingen
4. `buitengewone-algemene-vergadering` (cluster) — notarieel, statutenwijziging, verzwaarde drempels, bijzonder bestuursverslag

### Procedurele regels (5)
5. `bijeenroeping-algemene-vergadering` (cluster) — regime-bouwstenen BV/CV/NV niet-genoteerd/NV genoteerd, oproepingsinhoud
6. `agenderingsrecht-aandeelhouder` (regel) — drempels 10% (BV/CV/NV) en 3% (NV genoteerd)
7. `quorum-en-meerderheid-statutenwijziging` (regel) — quorum 50% + meerderheid 3/4 (gewoon) of 4/5 (voorwerp/doelen)
8. `schriftelijke-besluitvorming-aandeelhouders` (regel) — eenparig schriftelijk, behalve statutenwijziging
9. `belangenconflict-aandeelhouder` (regel) — minder strikt dan bestuurder; vergelijking-edge

### Deelname en stemming (3)
10. `stemrecht-aandeelhouder` (begrip) — één-aandeel-één-stem (NV), meervoudig in BV, schorsing/zonder stemrecht
11. `volmacht-algemene-vergadering` (begrip) — proxy voting, openbaar verzoek genoteerde NV + FSMA
12. `registratiedatum-genoteerde-nv` (begrip) — record date 14 dagen vóór AV

### Syntheses (3)
13. `synthese-soorten-algemene-vergadering` — vergelijkingstabel gewone / bijzondere / buitengewone
14. `synthese-quorum-meerderheid-algemene-vergadering` — BV × CV × NV × 3 besluit-types
15. `synthese-bevoegdheidsverdeling-av-vs-bestuur` — 11 materies × bevoegd orgaan × vorm × grondslag

## Edges-overzicht

- `onderdeel-van` → `algemene-vergadering`: 8 records (alle deelaspecten)
- `verwijst-naar` → `algemene-vergadering-toezichtsfunctie` (PO 1.3 cross-link, behoud bestaand record)
- `vergelijkt-met`: 3 edges (AV ↔ bestuursorgaan; bijzondere ↔ buitengewone AV; aandeelhouder-conflict ↔ bestuurder-conflict)
- Cross-PO edges naar `kwijting-bestuurder`, `kapitaalverhoging-nv`, `vrijwillige-ontbinding`, `bevoegdheid-bestuursorgaan`, `belangenconflict-bestuurder`, `vennoot-vs-aandeelhouder`, `naamloze-vennootschap-nv` (alle resolved)
- 2 pending edges (target nog niet gemaakt): `minderheidsvordering` (3.0.VIII later), `jaarrekening` (PO 1.2)

## Gaps.json — toegevoegd

| Aspect | Aantal | Prio mix |
|---|---|---|
| `records.ontbreekt` | 2 | midden, midden |
| `dangling-reference` | 1 | laag |
| `context-edge-ontbreekt` | 2 | laag, laag |
| `bron-gap` | 1 | midden |
| `granulariteit.beslissing-nodig` | 1 | laag |
| **Totaal** | **7** | |

### Belangrijkste gap
**Bron-gap WVV.md**: artikelen **5:81 (bevoegdheden AV BV)**, **7:124, 7:128, 7:131, 7:139** ontbreken in `resources/bronnen/wetteksten/WVV.md`. Reconstructie via naburige artikelen + MvT-WVV-chunks. Impact: drempel '3% van het kapitaal voor genoteerde NV' (art. 7:130) komt nu via MvT-chunks, niet rechtstreeks via wetteksten. Vooral 5:81 is structureel relevant — de bevoegdhedenkern van de AV-BV. Bron-MD opnieuw extraheren uit officiële tekstversie aanbevolen.

## Migraties / clean-up

- Geen schema-1.4→1.5 migraties (alle records nieuw)
- Geen `voorbeeld_inline`→`voorbeelden[]` migraties (alle records nieuw, direct in v1.6-vorm)
- Geen gedeprecieerde edge-types geschreven

## `inferred-from-aggregation` claims

- `bijzondere-algemene-vergadering.definitie` + `situering` — niet één wetsartikel definieert "bijzondere AV"; gebouwd uit WVV-systematiek + MvT
- `bijeenroeping-algemene-vergadering.bouwstenen[2]` (NV genoteerd) — gecombineerd uit art. 7:128–7:129 + MvT, want 7:128 zelf ontbreekt in bron-MD
- `belangenconflict-aandeelhouder.voorwaarden[0]` — aggregatie regels-bestuurder vs aandeelhouder
- `stemrecht-aandeelhouder.situering` — aggregatie BV-vrijheid (art. 5:42) + NV-principe (art. 7:51)
- Alle drie syntheses (13, 14, 15) — `inferred-from-aggregation` op situering, kerninzichten en/of vergelijkingstabel

## Open observaties (narratief)

1. **Genoteerde NV als parallel-regime kandidaat**: bijeenroeping, registratiedatum, volmacht openbaar verzoek, stempubliciteit, 3%-agenderingsdrempel — vormen samen een coherent regime. Heroverweeg in latere wave of `algemene-vergadering-genoteerde-nv` (cluster, specialisatie-van: algemene-vergadering, regime: genoteerd) inhoudelijk volstaat — nu zit deze stof verspreid over 4 records (bijeenroeping, agenderingsrecht, volmacht, registratiedatum).

2. **Regime-cluster-aanpak**: bewust niet 4× parallelle records aangemaakt (BV-AV, CV-AV, NV-AV, NV-genoteerd-AV). De gemeenschappelijke regels zijn dominant; verschillen in bijeenroeping en agenderingsrecht zijn als regime-bouwstenen ondergebracht. Validering bij VERIFY of voldoende.

3. **Cross-link met PO 1.3-record `algemene-vergadering-toezichtsfunctie`**: blijft staan (toezichtsperspectief op jaarrekening — andere lens dan generieke AV-cluster). Geen merge, wel `verwijst-naar`-edge.

4. **WVV-citeernoot**: bestuurdersconflict-edge ligt op `belangenconflict-bestuurder`. Belangenconflict-aandeelhouder is bewust een dunne regel — diepe procedure-eisen zijn er niet onder WVV (in tegenstelling tot bestuurders). Bij verfijning kan dit een synthese-record worden ('belangenconflict-vergelijking-bestuurder-aandeelhouder').

5. **`notulen-algemene-vergadering`** als zelfstandig record overwogen, beslist als bouwsteen van `algemene-vergadering`. Bij latere uitbreiding met genoteerde NV-publiciteit kan de afsplitsing zinvol worden. Gap toegevoegd.

## Volgende anchor (wave-planning suggestie)

PO 3.0.V "Aandelen en effecten" (kapitaal- en effectenstructuur) is een natuurlijke vervolgwave — daar landen `aandelen-zonder-stemrecht`, `meervoudig-stemrecht-bv`, `soorten-aandelen` en de andere stem-gerelateerde concepten die hier als gap zijn gemarkeerd.
