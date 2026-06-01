# ADR-039 — PO-niveau samenvatting vervangt cluster-themafiche

**Status**: Accepted (2026-05-31)
**Gerelateerd**: ADR-036 (drie-lagen leermateriaal — wordt op één punt geamendeerd door dit ADR) · ADR-037 (leerstuk-laag) · ADR-038-kandidaat (oefening-laag)

---

## Context

ADR-036 plaatste themafiches op **cluster-niveau**: één themafiche per concept-cluster (consolidatie, kostprijsmethoden, break-even, …). Dat klonk schoon in theorie. In de praktijk breekt het bij grotere PO's:

- **PO 1.4 Geconsolideerde jaarrekening** heeft ruwweg één cluster (consolidatie) → 1 themafiche → werkt nog
- **PO 1.8 Analytische boekhouding** kreeg al **4 themafiches** voor één PO: `analytische-boekhouding-stelsel` · `kostprijsmethoden` · `break-even-en-marginale-analyse` · `budget-en-variantieanalyse`. Voor een student die zich op het examen voorbereidt is dat versnipperd — vier aparte kapstokken voor één vak.
- Examen-voorbereiding gebeurt op **PO-niveau** (één PO = één examen-onderdeel), niet op cluster-niveau. De geheugen-kapstok hoort daar te leven.

Daarnaast: cluster-themafiches lopen het risico te dupliceren of over-overlappen met leerstukken (die zelf al cluster-niveau zijn sinds ADR-037).

## Beslissing

**Themafiches op cluster-niveau worden vervangen door samenvattingen op PO-niveau.** Eén samenvatting per PO, niet per cluster. Naam: **samenvatting** (signaleert de PO-scope en is leesbaarder dan "themafiche").

| Was (ADR-036) | Wordt (ADR-039) |
|---|---|
| `content/themafiches/<cluster>.md` | `content/studiemateriaal/<po-slug>/samenvatting.md` |
| Eén per cluster | Eén per PO |
| Cap: ~5 A4 | Cap: **2-4 A4 printbaar** |
| Schrijfregels: `docs/themafiche-schrijfregels.md` | Schrijfregels: `docs/samenvatting-schrijfregels.md` (geen aparte naamgeving meer; PO-scope) |

**Locatie binnen leerpad-folder** maakt het PO-leerpad self-contained:

```
content/studiemateriaal/<po-slug>/
├── index.md          # minicursus (verhaal + routekaart)
├── <leerstuk-1>.md
├── ...
├── samenvatting.md   # printbaar geheugen-kapstok (2-4 A4)
└── oefening.md       # doorgewerkte case (optioneel, kandidaat ADR-038)
```

### Drie pijlers van een samenvatting

1. **Visueel-dominant**: tabellen, beslisbomen, formules. Niet doorlopend proza.
2. **Printbaar**: 2-4 A4 (cap). Wat niet past, hoort in een leerstuk of concept-fiche.
3. **Wijst niet uit**: leeft uitsluitend binnen het PO. Verwijzingen naar leerstukken (binnen PO) en concept-fiches mogen; verwijzingen naar leerstukken in ándere PO's vermijden (die context heeft de student niet bij examen-voorbereiding).

## Migratiepad

### PO 1.4 — POC (deze ronde)

1. `content/themafiches/consolidatie.md` → `content/studiemateriaal/1-4/samenvatting.md` (rename + minimale content-aanpassing — was al PO-equivalent want PO 1.4 ≈ cluster consolidatie)
2. Wikilink-updates in 5 leerstuk-YAMLs + minicursus + leerpad-skelet-doc
3. Themafiche-mapping in `content/themafiches/index.md`-achtige indexen bijwerken

### PO 1.8 — Follow-up

4 themafiches mergen tot één `content/studiemateriaal/1-8/samenvatting.md`. Werk voor de sessie die met PO 1.8 bezig is. Volgt nieuwe schrijfregels.

### Themafiche-laag retreert volledig — drie categorieën

**Principe**: cluster-themafiches stoppen volledig met bestaan. Er zijn alleen nog **concept-fiches** (één per begrip) en **PO-samenvattingen** (één per PO). Niets ertussenin.

Praktisch zijn er drie categorieën bestaande themafiches, elk met eigen migratie-pad:

| Categorie | Beschrijving | Status nu | Migratie-pad |
|---|---|---|---|
| **A. cluster ≈ PO, leerpad bestaat** | Themafiche dekt feitelijk al één PO; dat PO heeft inmiddels een leerpad | PO 1.4 ✅ gemigreerd; PO 1.8 in queue | Migreren naar `content/studiemateriaal/<po-slug>/samenvatting.md` volgens [`docs/samenvatting-procedure.md`](../samenvatting-procedure.md) § Migratie. Oude themafiche-md's verwijderen in dezelfde commit. |
| **B. cluster ≈ PO, geen leerpad** | Themafiche dekt feitelijk al één PO, maar dat PO heeft nog geen leerpad-bouw gehad | Meeste bestaande themafiches (PO 1.1, 1.2, 1.3, 1.5, 1.6, 1.7, 1.9, 2.x, 3.0) — ~50 stuks | **Voorlopig blijven staan** met deprecation-callout. Bij leerpad-bouw voor die PO: zelfde migratie als categorie A. Geen aparte beslissing nodig. |
| **C. echte cross-PO themafiche** | Vergelijking tussen verschillende PO's (bv. `be-gaap-vs-ifrs-vergelijking`, `reorganisatie-en-bijzondere-mandaten`) | Klein aantal (~2-3 stuks); blijft staan met deprecation-callout | **Aparte beslissing per fiche** bij relevante leerpad-bouw. Twee opties: (1) inhoud incorporeren in alle relevante PO-samenvattingen (duplicatie aanvaardbaar als compact); (2) upgraden naar concept-fiche (bv. `be-gaap-vs-ifrs` als concept-record met diepe vergelijking). Geen behoud als losse themafiche-laag. |

**Operationeel nu**: alle 60+ bestaande themafiches krijgen een deprecation-callout bovenaan ("Voorlopig — themafiche-laag wordt uitgefaseerd") die naar dit ADR verwijst. Werkende sessies kunnen de inhoud blijven gebruiken; nieuwe content wordt niet meer als themafiche maar als PO-samenvatting (categorie A/B) of als concept-fiche (eventueel categorie C) gepubliceerd.

## Gevolgen

### Voor andere docs

- **ADR-036** wordt geamendeerd op één punt — themafiche-positionering. De drie-lagen-architectuur blijft (concept + leerstuk + minicursus); de themafiche-laag wordt vervangen door PO-samenvatting onder de minicursus.
- **`docs/themafiche-schrijfregels.md`** → archiveer (`docs/archive/`) met supersede-noot naar `docs/samenvatting-schrijfregels.md`
- **`docs/leerstuk-procedure.md`** Stap 6 "Themafiche-update" → "Samenvatting"
- **`docs/leerstuk-status.md`** kolom "Themafiche tweelaags" → "Samenvatting"
- **CLAUDE.md** wegwijzer-rij themafiche → samenvatting
- **`docs/minicursus-schrijfregels.md`** themafiche-verwijzingen → samenvatting

### Voor agenten / andere sessies

Werkende sessies die nog naar het themafiche-concept verwijzen, blijven werken (de bestaande themafiche-md's bestaan nog tot ze gemigreerd zijn). Nieuwe PO's volgen de nieuwe schrijfregels via `docs/samenvatting-schrijfregels.md`. Zie ook update in `docs/leerstuk-status.md` voor de migratie-status per PO.

### Voor de tutor en zoek

Tutor-app + RAG-indexering volgen automatisch: `content/studiemateriaal/<po-slug>/samenvatting.md` wordt geïndexeerd zoals elk ander markdown-bestand. Geen tooling-wijziging nodig.

## Open punten

- **Categorie C-beslissingen** (echte cross-PO themafiches): aparte beslissing per fiche bij relevante leerpad-bouw. Concrete fiches: `be-gaap-vs-ifrs-vergelijking` (PO 1.4 + 1.5), `reorganisatie-en-bijzondere-mandaten` (PO 1.6 + 3.0 + insolventie). Bij meer dan 3 fiches met zelfde patroon → vervolg-ADR-040.
- **Print-CSS** voor samenvatting (`@media print` styles in Quartz) — buiten scope dit ADR; al deels aanwezig via `.no-print` klassen in leerstukken en minicursus.
- **Bestandsnaam** in URL: `/studiemateriaal/1-4/samenvatting/` is duidelijk. Of we sub-naamgeving willen (`samenvatting-1-4.md`) — niet nodig; folder-context geeft het PO al.
- **Inventaris-tracking**: voor elke nog-bestaande themafiche moet bij leerpad-bouw beslist worden — categorie A/B migratie of categorie C aparte beslissing. Tracking in `docs/leerstuk-status.md` § Themafiche-migratie-inventaris.

---

*Vervangt: ADR-036 §"Themafiche"-positionering. ADR-036 blijft canoniek voor de andere twee lagen (concept, minicursus).*
