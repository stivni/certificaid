# ADR-034 — Bron-leeshulp via injectie in publicatie-laag

**Status**: Draft (2026-05-26)
**Gerelateerd**: ADR-005 (bronnen-ETL) · ADR-010 (leermateriaal & tutor) · ADR-029 (schema 2.1 v1.5 — operatie `didactisch_verrijken`)

## Context

Veel bronnen in `resources/bronnen/` (wetteksten, ITAA-normen, IESBA-code, …) zijn voor een GA-stagiair zeer droog: kale wettelijke tekst zonder kader, voorbeelden, of synthese. Concrete case: [`ITAA-norm-algemene-controlenorm`](../../content/bronnen/normen/ITAA-norm-algemene-controlenorm.md) — 7 secties bullet-tekst uit 1991, geen aanwijzing waar te beginnen, sectietitels die de lading niet dekken (§7 heet "Commissie van Toezicht" maar regelt verslag-inhoud + ITAA-afschrift).

Bestaande architectuur vangt dit deels af:
- **Concept-fiches** (ADR-029, Fase 7) renderen mensvriendelijke fenomeen-fiches uit `data/concepten/records/`. Goed voor *"ik wil concept X begrijpen"*, niet voor *"ik wil de norm zélf lezen, met begeleiding"*.
- **Studiemateriaal** per programmaonderdeel (ADR-010) synthetiseert over meerdere bronnen heen. Niet gekoppeld aan de individuele bron-pagina.

Wat ontbreekt: een laag die de **canonieke bron-tekst zelf** leesbaarder maakt op zijn publicatie-pagina, zonder die tekst aan te raken.

Regel 1 (geen wetsinhoud zonder bronverwijzing) en de trust-discipline van ADR-005 maken duidelijk dat de bron in `resources/bronnen/` heilig is: re-conversie via `tools/etl/convert.py` overschrijft die map; QA-agent gates ze; trust-status zit in `provenance.trust`. Een didactische bewerking direct op die bestanden zou:
- het bron/commentaar-onderscheid breken (regel 2 — confidence-labeling);
- bij re-conversie verloren gaan of de QA-pipeline corrumperen;
- het idee van "primaire bron" ondergraven.

## Beslissing

Drie-laag-architectuur voor publicatie van bronnen:

```
resources/bronnen/<type>/X.md     ← BRON (canoniek, trusted, nooit aangepast door leeshulp)
                ↓ +
resources/leeshulp/<type>/X.md    ← LEESHULP (handgeschreven didactische callouts)
                ↓
        [tools/leermateriaal/inject_leeshulp.py]
                ↓
content/bronnen/<type>/X.md       ← PUBLICATIE (gegenereerd = bron + callouts samengevoegd)
```

**Eigenschappen:**

1. **Bron blijft heilig.** `resources/bronnen/` wordt door geen enkele leeshulp-tool aangeraakt. ADR-005 trust-flow blijft ongewijzigd.
2. **Leeshulp leeft apart** in `resources/leeshulp/<type>/X.md` — leesbare markdown met frontmatter (`voor:`, `versie:`, `auteur_label:`, `review_status:`) en anchor-gestructureerde callouts (`## @intro`, `## @na "## 2. Verslag"`).
3. **`content/`-versie is build-output**, gegenereerd door `inject_leeshulp.py`. Niet bedoeld om manueel te editen na introductie van de tool (POC-fase mag handmatig). Pre-commit hook waarschuwt als `content/`-versie niet matcht met `inject(bron, leeshulp)`.
4. **Idempotent.** Re-run vervangt `content/`-versie netjes. Bij re-conversie van een bron: `inject_leeshulp.py` opnieuw draaien → nieuwe publicatie met behoud van leeshulp.
5. **Leeshulp is optioneel.** Bronnen zonder bijbehorend `resources/leeshulp/`-bestand worden 1-op-1 gekopieerd naar `content/`. Geen verplichte coverage.

**Anchor-syntax in leeshulp-bestand:**
- `## @intro` — callout vóór de eerste H1 (na frontmatter)
- `## @na "<exacte heading-tekst>"` — callout na de aangegeven heading-sectie (vóór de volgende heading van gelijke of hogere niveau)
- `## @vervang "<exacte heading-tekst>"` — *toekomst, niet in v1* — callout vervangt sectie-titel

**Confidence-labeling:** elke leeshulp-callout markeert zichzelf met 🤖 (inferred). De bron-tekst blijft ⚖️ (grounded). Geen vermenging.

## Verhouding tot ADR-029 / Fase 7

Leeshulp ≠ concept-fiche. Twee verschillende leesmodi voor de stagiair:

| Laag | Doel | Bestaat in |
|---|---|---|
| **Concept-fiche** (ADR-029, Fase 7) | "Ik wil concept X begrijpen" → definitie + relaties + voorbeelden + bron-citaten | `data/concepten/records/` → render naar `content/concepten/` |
| **Geannoteerde bron** (deze ADR) | "Ik wil de norm zélf lezen, met leesbegeleiding" | `resources/leeshulp/` + injectie → `content/bronnen/` |

Beide lagen bestaan náást elkaar; ze concurreren niet. Een leeshulp-callout op de algemene controlenorm en een concept-record "onafhankelijkheid van de accountant" mogen overlap hebben — de eerste is lokale navigeerhulp in de bron, de tweede is een atomair kennisstuk in de tutor-architectuur.

**Geen unificatie nagestreefd.** De operatie `didactisch_verrijken` (ADR-029) opereert op een concept-record en produceert valkuilen/speelruimtes/syntheses **in dat record**. De leeshulp-injectie opereert op een bron-pagina en produceert callouts **rond de bron-tekst**. Verschillende inputs, verschillende outputs, verschillende doelgroep-aanvliegroute.

## POC + tool — uitgevoerd

- Leeshulp-source: [`resources/leeshulp/normen/ITAA-norm-algemene-controlenorm.md`](../../resources/leeshulp/normen/ITAA-norm-algemene-controlenorm.md) — 4 callouts (intro + na §2, §4, §7).
- Publicatie: [`content/bronnen/normen/ITAA-norm-algemene-controlenorm.md`](../../content/bronnen/normen/ITAA-norm-algemene-controlenorm.md), gegenereerd door de injectie-tool.
- Tool: [`tools/leermateriaal/inject_leeshulp.py`](../../tools/leermateriaal/inject_leeshulp.py) — `inject-all` (regenereer) + `check` (exit 1 bij drift).
- Tests: [`tests/test_inject_leeshulp.py`](../../tests/test_inject_leeshulp.py) — unit-tests + integration-test die als pre-commit gate fungeert (pytest draait in pre-commit hook).

## Open punten — resolutie

| # | Punt | Resolutie v1 |
|---|---|---|
| 1 | Heading-disambiguation | **Eerste match.** Bij conflict moet de leeshulp-auteur het heading-argument uniek maken (bv. door het volledig over te nemen incl. nummering). Geen `#occurrence:N`-syntax in v1. |
| 2 | Pre-commit gate | **Pytest-test** `test_content_bronnen_in_sync_met_leeshulp` (in `tests/test_inject_leeshulp.py`). Faalt als ten minste één `content/`-versie afwijkt van `inject(bron, leeshulp)`. Draait via bestaande pre-commit hook (`scripts/install-git-hooks.sh`). |
| 3 | Leeshulp-bestanden in Quartz? | **Nee in v1.** `resources/leeshulp/` is build-input, niet site-content. |
| 4 | Coverage wetteksten | **Niet in v1.** Tool ondersteunt enkel `normen/` via `SUPPORTED_TYPES`. |
| 5 | Review-discipline | **Geen automatische QA-gate.** Leeshulp-frontmatter heeft `review_status: draft`; expliciete review-pass door gebruiker. |

## Open — voor latere ronde

**Drift-opkuis bronnen zónder leeshulp.** De tool default-scope is `only_with_leeshulp=True` — d.w.z. `cmd_check` ignoreert de 38 normen-bestanden waar `content/bronnen/normen/X.md` afwijkt van `resources/bronnen/normen/X.md` (gevonden bij eerste tool-run, 2026-05-26). Dit gaat over bron-versies waar `resources/` recenter is bijgewerkt dan `content/` (re-conversies + trust-confirms). Verdere opties:

- Tool runnen met `--all`-flag om alle 38 bronnen 1-op-1 te re-syncen (separate commit).
- Het re-sync-werk afhandelen via een aparte sync-pipeline die buiten leeshulp leeft.

Niet in deze ronde — POC-scope.

## Niet-doelen

- Het concept-extractie- of render-systeem (ADR-029, Fase 7) wijzigen.
- Een nieuwe LLM-pipeline opzetten. Leeshulp is handgeschreven (mogelijk via Sonnet-agent, maar deterministisch ingevoegd, niet via runtime LLM-call).
- De `resources/bronnen/`-tree of de ETL-pipeline aanraken.
