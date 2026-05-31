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
| `content/themafiches/<cluster>.md` | `content/leerpaden/<po-slug>/samenvatting.md` |
| Eén per cluster | Eén per PO |
| Cap: ~5 A4 | Cap: **2-4 A4 printbaar** |
| Schrijfregels: `docs/themafiche-schrijfregels.md` | Schrijfregels: `docs/samenvatting-schrijfregels.md` (geen aparte naamgeving meer; PO-scope) |

**Locatie binnen leerpad-folder** maakt het PO-leerpad self-contained:

```
content/leerpaden/<po-slug>/
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

1. `content/themafiches/consolidatie.md` → `content/leerpaden/1-4/samenvatting.md` (rename + minimale content-aanpassing — was al PO-equivalent want PO 1.4 ≈ cluster consolidatie)
2. Wikilink-updates in 5 leerstuk-YAMLs + minicursus + leerpad-skelet-doc
3. Themafiche-mapping in `content/themafiches/index.md`-achtige indexen bijwerken

### PO 1.8 — Follow-up

4 themafiches mergen tot één `content/leerpaden/1-8/samenvatting.md`. Werk voor de sessie die met PO 1.8 bezig is. Volgt nieuwe schrijfregels.

### Cross-cluster themafiches (open scope-vraag)

Bestaande themafiches die meerdere PO's raken (bv. `boekhoudplicht-en-rechtsbronnen` raakt PO 1.1 + 1.2; `eindejaarsverrichtingen-en-waardering` raakt PO 1.1 + 1.2; `vennootschapsvormen` raakt PO 3.0; `be-gaap-vs-ifrs-vergelijking` raakt PO 1.4 + 1.5; `ifrs-toepassingskader` raakt PO 1.5; `reorganisatie-en-bijzondere-mandaten` raakt meerdere PO's):

**Voorlopige beslissing**: niet aanraken tot de PO's die ze raken een leerpad krijgen. Dan beslissen per geval:

- **Optie A** — content insplitsen naar de PO-samenvattingen (kan duplicatie geven; aanvaardbaar als de inhoud écht PO-specifiek interpretabel is)
- **Optie B** — behouden als gedeelde cross-PO referentie-fiche in `content/themafiches/` (uitzondering op de regel, expliciet als zodanig gelabeld)

Voorkeur: **A** waar mogelijk (vermijdt het "themafiche-laag voor uitzonderingen"-probleem). **B** alleen voor compacte, zuiver-referentie-fiches.

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

Tutor-app + RAG-indexering volgen automatisch: `content/leerpaden/<po-slug>/samenvatting.md` wordt geïndexeerd zoals elk ander markdown-bestand. Geen tooling-wijziging nodig.

## Open punten

- **Hoe omgaan met cross-cluster themafiches** wanneer alle relevante PO's leerpaden krijgen — beslissingen per fiche (zie scope-vraag hierboven). Plan in een vervolg-ADR-040 indien meerdere fiches dezelfde behandeling vragen.
- **Print-CSS** voor samenvatting (`@media print` styles in Quartz) — buiten scope dit ADR; al deels aanwezig via `.no-print` klassen in leerstukken en minicursus.
- **Bestandsnaam** in URL: `/leerpaden/1-4/samenvatting/` is duidelijk. Of we sub-naamgeving willen (`samenvatting-1-4.md`) — niet nodig; folder-context geeft het PO al.

---

*Vervangt: ADR-036 §"Themafiche"-positionering. ADR-036 blijft canoniek voor de andere twee lagen (concept, minicursus).*
