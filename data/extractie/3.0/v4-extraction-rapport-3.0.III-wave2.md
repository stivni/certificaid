# EXTRACT v4 — PO 3.0 — Wave 2 — Anker 3.0.III sub-anchors (A+B+C)

**Datum**: 2026-05-20
**Scope**: sub-anchors `3.0.III.A` (procedure bijeenroeping + werking AV), `3.0.III.B` (wie mag bijwonen), `3.0.III.C` (volmachten).
**Wave-1-baseline**: 15 records onder parent-anker `3.0.III` (algemene vergadering, soorten AV, bijeenroeping, agenderingsrecht, stemrecht, schriftelijke besluitvorming, belangenconflict, quorum-statutenwijziging, registratiedatum-genoteerde-nv, volmacht, + 3 syntheses).
**State**: 647 records vóór wave-2, 650 records na wave-2. Audit-parity OK.

## Output

### Nieuwe records (3)

| ID | Type | Anchor | Korte beschrijving |
|---|---|---|---|
| `notulen-algemene-vergadering` | cluster | 3.0.III.A | Schriftelijke vastlegging AV (bureau, ondertekening, genoteerde-NV-specifieke stem-rapport, notariële akte bij buitengewone AV, register bij eenpersoonsvennootschap). 5 bouwstenen + 2 voorbeelden (scenario Brugse Brouwerij BV + eenvoudig Zelena Bio NV) + 3 valkuilen. |
| `vraagrecht-aandeelhouder` | regel | 3.0.III.A | Antwoord-/vraagrecht uit WVV art. 5:70/6:77/7:126/9:18 — 4 voorwaarden + 2 uitzonderingen (vennootschapsschade, beroepsgeheim commissaris). 2 voorbeelden (Brugse Brouwerij BV met geheimhouding, Zelena Bio NV met gegroepeerde antwoorden). |
| `aanwezigheidsrecht-algemene-vergadering` | cluster | 3.0.III.B | 6 bouwstenen (stemgerechtigde aandeelhouders, bijwoners met raadgevende stem, commissaris, vertegenwoordigers obligatiehouders, bestuurders + raadgevende derden, bedrijfsrevisor bij ondernemingsraad). Bijstandsrecht-derden gemarkeerd inferred — wettelijk niet expliciet. |

### Bijgewerkte records (15)

| ID | Wijziging |
|---|---|
| `volmacht-algemene-vergadering` | **Upgrade `begrip` → `cluster`** + 8 bouwstenen toegevoegd (BV/CV basisregime, NV niet-genoteerd, genoteerde NV één-volmachtdrager, belangenconflict, openbaar verzoek, afwijken van instructies, herroeping/geldigheidsduur, transparantie volmachtadviseurs) + vergelijkingspaar BV/CV vs genoteerde NV + edges-uitbreiding + 1 extra in_praktijk-punt. `linked_anchors: [3.0.III] → [3.0.III, 3.0.III.C]`. |
| `algemene-vergadering` | `linked_anchors → [3.0.III, 3.0.III.A, 3.0.III.B]` |
| `bijeenroeping-algemene-vergadering`, `agenderingsrecht-aandeelhouder`, `gewone-algemene-vergadering`, `bijzondere-algemene-vergadering`, `buitengewone-algemene-vergadering`, `quorum-en-meerderheid-statutenwijziging`, `schriftelijke-besluitvorming-aandeelhouders`, `registratiedatum-genoteerde-nv`, `synthese-soorten-algemene-vergadering`, `synthese-quorum-meerderheid-algemene-vergadering`, `synthese-bevoegdheidsverdeling-av-vs-bestuur` | `linked_anchors → [3.0.III, 3.0.III.A]` |
| `stemrecht-aandeelhouder`, `belangenconflict-aandeelhouder` | `linked_anchors → [3.0.III, 3.0.III.B]` |

### Hernoemd / verwijderd

Geen.

### Migraties (schema 1.5 → 1.6)

Geen — alle wave-1-records gebruikten al schema 1.6 (situering ipv doel, geen voorbeeld_inline).

## Gaps.json — toegevoegd: 5 entries

| Aspect | Record | Prio | Korte beschrijving |
|---|---|---|---|
| `bron-gap` | — | midden | Anchor 3.0.III.B noemt expliciet "advocaat / gecertificeerd accountant" als bijwoners; WVV-Boeken 5-7 codificeren dit nergens (0 hits in 150-chunk-top). Aanvullende bron nodig. |
| `dangling-reference` | `vraagrecht-aandeelhouder` | midden | Edge `verwijst-naar beroepsgeheim-bedrijfsrevisor` pending — record bestaat niet (alleen `beroepsgeheim-accountant`). |
| `records.ontbreekt` | — | laag | `bureau-algemene-vergadering` — granulariteit-twijfel; voor nu bouwsteen op notulen-cluster. |
| `records.ontbreekt` | — | midden | Algemene vergadering van obligatiehouders (WVV art. 7:154-7:161) — eigen procedureel regime, ontbrekend record. Hoort vermoedelijk onder 3.0.IV of dedicated sub-anchor. |
| `records.ontbreekt` | — | laag | `volmachtadviseur` (proxy advisor — WVV onderafdeling 8) — momenteel als bouwsteen, maar zelfstandige transparantieregeling rechtvaardigt mogelijk eigen record. |

## Claims `inferred` / `inferred-from-aggregation`

- `aanwezigheidsrecht-algemene-vergadering` — bouwsteen "Bestuurders en derde-raadgevers" (bijstandsrecht door advocaat/gecertificeerd accountant). Confidence `inferred` omdat dit niet expliciet uit het corpus volgt; afgeleid uit afwezigheid wettelijk verbod en algemeen rechtsbeginsel.
- `aanwezigheidsrecht-algemene-vergadering` voorbeeld 2 (Brugse Brouwerij BV — Robert Vandenberghe met advocaat Sofie Janssens). Confidence `inferred`.
- `vraagrecht-aandeelhouder` beide voorbeelden — concrete cijfers/scenario's zijn afgeleid; rechtsregel is grounded.

## Open observaties (narratief, niet in gaps.json)

### Wave 1 had het meeste werk al gedaan voor 3.0.III.A en 3.0.III.C

Bundle-analyse bevestigde dat de hoofdarchitectuur van bijeenroeping + soorten AV + quorum + volmacht reeds gedekt was. Detail-gaps die wave 2 ophaalde:
- **Notulen-procedure** — wave 1 had alleen een bouwsteen op `algemene-vergadering` (4 regels); wave 2 promoveert dit tot een cluster met 5 bouwstenen die het bureau, de ondertekeningskringen, het genoteerde-NV-stem-rapport en de notariële-akte-vereiste expliciet uitwerken. Deze granulariteit is gerechtvaardigd: notulen bestaan als domein-object buiten de specifieke AV-context (bewijslast jaarrekeningdeponering, geschillen, due diligence).
- **Vraagrecht** — afwezig in wave 1, maar prominente plek in WVV (5:70 / 6:77 / 7:126 / 9:18) en MvT, met gestructureerde voorwaarden + twee uitzonderingsgronden. Eigen record gerechtvaardigd door cross-boek herhaling + interactie met beroepsgeheim commissaris.

### 3.0.III.B blijkt een hybride scope

Het anchor-verbose noemt "advocaat, gecertificeerd accountant, ..." als bijwoners. Het WVV codificeert dit niet expliciet — bundle-search op deze termen leverde 0 hits in 150 top-chunks. Het corpus dekt wél uitgebreid het *wie van het WVV bijwonen mag* (stemgerechtigden, raadgevende-stem-bijwoners, commissaris, obligatie-vertegenwoordigers, bedrijfsrevisor bij ondernemingsraad). Het nieuwe `aanwezigheidsrecht-algemene-vergadering`-cluster dekt beide invalshoeken:
- Bouwstenen 1-4, 6 = grounded op WVV-artikelen
- Bouwsteen 5 (Bestuurders en derde-raadgevers) = `inferred` met bron-gap-entry gelogd

Dit is de meest eerlijke manier om de anchor-tekst te respecteren zonder fictieve regels in te schrijven.

### Volmacht-upgrade: van begrip naar cluster

`volmacht-algemene-vergadering` was in wave 1 een begrip zonder bouwstenen. Met 19 bundle-hits op "volmacht" in 3.0.III.C, allemaal regime-specifiek (BV/CV-vrij regime vs NV-kernregels vs genoteerde NV-strikte set), bleek de cluster-vorm met 8 bouwstenen de juiste granulariteit. Dit voorkomt dat latere PO's (3.5 corporate governance, 3.6 genoteerde vennootschappen) elk een eigen volmacht-record zouden moeten aanmaken — alle regimes leven nu samen.

### Aandachtspunt voor volgende wave (3.0.IV — minderheidsrechten, of 3.0.VIII — conflicten)

`algemene-vergadering-van-obligatiehouders` is een echt gat. WVV art. 7:154-7:161 + MvT-equivalenten verschenen herhaaldelijk in beide bundles A en B, maar passen niet bij het aandeelhouders-perspectief van wave 1+2. Aanbevolen: dedicated extractie-pass onder een obligaties-sub-anchor.

## Audit-resultaat na wave 2

```
[audit] disk: 650 records (54 synthese), RAG: 650 records, content: 596 fiches
[audit] OK — disk, RAG en content zijn in sync.
```

650 records — 3 nieuwe records (notulen-algemene-vergadering, vraagrecht-aandeelhouder, aanwezigheidsrecht-algemene-vergadering), 15 bijgewerkt (volmacht upgrade + 14 linked_anchors-updates).
